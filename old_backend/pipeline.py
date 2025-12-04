############################################################
# FIXED & CLEANED — GPU Resume Scoring Training Pipeline  #
############################################################

import importlib.util
import os
from pathlib import Path
import numpy as np
import pandas as pd
from tqdm import tqdm
import joblib
from sklearn.model_selection import GroupKFold
from sklearn.metrics import mean_absolute_error
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import xgboost as xgb
import torch


torch_device = "cuda" if torch.cuda.is_available() else "cpu"
print("Torch device for embeddings:", torch_device)

device = "cuda"
print("Using device:", device)


OUT_DIR = "models_out_fixed"
os.makedirs(OUT_DIR, exist_ok=True)

PREPROC_PY = r"C:\Users\prady\OneDrive\Desktop\edgeAI\SE\ResAnal\Backend\old_backend\preprocessed.py"
LABELS_CSV = r"C:\Users\prady\OneDrive\Desktop\edgeAI\SE\ResAnal\Backend\old_backend\resume_labels_improved.csv"


spec = importlib.util.spec_from_file_location("preproc", PREPROC_PY)
preproc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preproc)

print(f"Loaded {len(preproc.all_resumes)} resumes, {len(preproc.job_descriptions)} JDs")


labels_df = pd.read_csv(LABELS_CSV)
labels_df.columns = [c.strip() for c in labels_df.columns]

labels_df["email_norm"] = labels_df["Email"].astype(str).str.lower().str.strip()
labels_df["name_norm"] = labels_df["Candidate Name"].astype(str).str.lower().str.strip()


rows = []
for r in preproc.all_resumes:
    email = (r.get("email") or "").lower().strip()
    name = (r.get("name") or "").lower().strip()
    skills = r.get("skills") or []

    combined_text = " ".join([
        r.get("name", ""),
        " ".join(skills),
        " ".join(r.get("projects") or []),
        " ".join(r.get("achievements") or [])
    ])

    rows.append({
        "email": email,
        "name": name,
        "skills": skills,
        "text": combined_text,
    })

resumes_df = pd.DataFrame(rows)


email_to_idx = {e: i for i, e in enumerate(resumes_df["email"])}
name_to_idx = {n: i for i, n in enumerate(resumes_df["name"])}

labels_df["matched_idx"] = -1
for i, row in labels_df.iterrows():
    e = row["email_norm"]
    n = row["name_norm"]
    if e in email_to_idx:
        labels_df.at[i, "matched_idx"] = email_to_idx[e]
    elif n in name_to_idx:
        labels_df.at[i, "matched_idx"] = name_to_idx[n]

labels_df = labels_df[labels_df["matched_idx"] != -1].reset_index(drop=True)

merged = labels_df.merge(
    resumes_df.reset_index().rename(columns={"index": "matched_idx"}),
    on="matched_idx",
    how="left"
)

def jd_stats(jd_name):
    jd = preproc.jd_requirements.get(jd_name, {})
    skills = [s.lower() for s in jd.get("skills", [])]
    keywords = [k.lower() for k in jd.get("keywords", [])]
    return {
        "jd_skill_count": len(skills),
        "jd_keyword_count": len(keywords),
        "skills": skills,
        "keywords": keywords
    }

merged["jd_struct"] = merged["Assigned JD"].apply(jd_stats)
merged["jd_skill_count"] = merged["jd_struct"].apply(lambda d: d["jd_skill_count"])
merged["jd_keyword_count"] = merged["jd_struct"].apply(lambda d: d["jd_keyword_count"])
merged["jd_skills_list"] = merged["jd_struct"].apply(lambda d: d["skills"])
merged["jd_keywords_list"] = merged["jd_struct"].apply(lambda d: d["keywords"])

def exact_skill_match_pct(resume_skills, jd_skills):
    R = [s.lower() for s in (resume_skills or [])]
    if not jd_skills:
        return 0.0
    hits = sum(1 for js in jd_skills if js in R)
    return hits / len(jd_skills)

merged["exact_skill_match_pct"] = merged.apply(
    lambda r: exact_skill_match_pct(r["skills"], r["jd_skills_list"]), axis=1
)


def keyword_cov(text, jd_keywords):
    txt = (text or "").lower()
    if not jd_keywords:
        return 0.0
    hits = sum(1 for kw in jd_keywords if kw in txt)
    return hits / len(jd_keywords)

merged["keyword_coverage_pct"] = merged.apply(
    lambda r: keyword_cov(r["text"], r["jd_keywords_list"]), axis=1
)


merged["jd_text"] = (
    merged["Assigned JD"].astype(str).str.lower()
    + " Required skills: "
    + merged["jd_skills_list"].apply(lambda lst: " ".join(lst))
    + " Keywords: "
    + merged["jd_keywords_list"].apply(lambda lst: " ".join(lst))
)

merged["resume_text"] = merged["text"].astype(str).str.lower()

embedder = SentenceTransformer("all-MiniLM-L6-v2", device=torch_device)

jd_emb = embedder.encode(merged["jd_text"].tolist(), convert_to_numpy=True)
res_emb = embedder.encode(merged["resume_text"].tolist(), convert_to_numpy=True)
skill_emb = embedder.encode(
    merged["skills"].apply(lambda s: " ".join(s).lower()).tolist(),
    convert_to_numpy=True
)

merged["jd_resume_cosine"] = [
    float(cosine_similarity(jd_emb[i:i+1], res_emb[i:i+1])[0, 0])
    for i in range(len(merged))
]

merged["skillset_cosine"] = [
    float(cosine_similarity(skill_emb[i:i+1], jd_emb[i:i+1])[0, 0])
    for i in range(len(merged))
]

feature_cols = [
    "jd_skill_count",
    "jd_keyword_count",
    "exact_skill_match_pct",
    "keyword_coverage_pct",
    "jd_resume_cosine",
    "skillset_cosine",
]

print("FEATURES USED IN TRAINING:", feature_cols)

y_raw = merged["Match Score"].astype(float)

y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())  

print("Label normalization complete.")

X = merged[feature_cols].astype(float).values
groups = merged["Assigned JD"]


xgb_params = {
    "max_depth": 6,
    "learning_rate": 0.08,
    "n_estimators": 550,
    "subsample": 0.9,
    "colsample_bytree": 0.9,
    "objective": "reg:squarederror",
    "tree_method": "gpu_hist",
    "predictor": "gpu_predictor",
}

gkf = GroupKFold(n_splits=5)
maes = []

for fold, (tr, te) in enumerate(gkf.split(X, y, groups), start=1):
    model = xgb.XGBRegressor(**xgb_params)
    model.fit(X[tr], y[tr])
    preds = model.predict(X[te])
    mae = mean_absolute_error(y[te], preds)
    maes.append(mae)
    print(f"Fold {fold} MAE: {mae:.4f}")

print("Mean MAE:", np.mean(maes))


final_model = xgb.XGBRegressor(**xgb_params)
final_model.fit(X, y)


joblib.dump(
    {
        "model": final_model,
        "feature_cols": feature_cols,
        "numeric_cols": [],  # important
        "embed_model_name": "all-MiniLM-L6-v2",
        "y_min": float(y_raw.min()),
        "y_max": float(y_raw.max()),
    },
    os.path.join(OUT_DIR, "resume_match_xgb_fixed.joblib"),
)

print("Saved fixed model to models_out_fixed/resume_match_xgb_fixed.joblib")


merged["pred_norm"] = final_model.predict(X)
merged["pred_raw"] = merged["pred_norm"] * (y_raw.max() - y_raw.min()) + y_raw.min()

merged.to_csv(os.path.join(OUT_DIR, "training_report_fixed.csv"), index=False)

print("Saved training report.")
