import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
from app.services.pdf_parser import PDFParser
from app.services.feature_builder import FeatureBuilder
from app.services.nlp_extract import NLPExtractor
from app.utils.preproc_loader import PreprocLoader

class ScoreService:
    def __init__(self):
        model_path = "models_out_fixed/resume_match_xgb.joblib"
        data = joblib.load(model_path)
        self.pdf = PDFParser()
        embed_name = data["embed_model_name"]
        self.embedder = SentenceTransformer(embed_name)
        self.nlp = NLPExtractor()
        self.preproc = PreprocLoader()
        self.feature_builder = FeatureBuilder(self.embedder, self.preproc)


        self.model = data["model"]
        self.feature_cols = data["feature_cols"]
        self.numeric_cols = data.get("numeric_cols", [])
        self.y_min = data["y_min"]
        self.y_max = data["y_max"]

        

        print("Loaded fixed XGB model:", model_path)

    def predict(self, X):

        norm_score = float(self.model.predict(X)[0])

        norm_score = max(0.0, min(1.0, norm_score))

        raw_score = norm_score * (self.y_max - self.y_min) + self.y_min

        return raw_score
    def score_resume(self, resume_bytes, filename, jd_name, jd_text, jd_keywords, jd_skills):

        resume_text = self.pdf.parse(resume_bytes)

        resume_skills = self.nlp.extract_skills(resume_text)

        kw_list = [k.strip().lower() for k in jd_keywords.split(",")] if jd_keywords else []
        sk_list = [s.strip().lower() for s in jd_skills.split(",")] if jd_skills else []

        features, X, jd_struct = self.feature_builder.build(
            resume_text=resume_text,
            resume_skills=resume_skills,
            jd_name=jd_name,
            jd_text=jd_text,
            jd_keywords=kw_list,
            jd_skills=sk_list,
        )

        score = self.predict(X)

        return {
            "fileName": filename,
            "score": score,
            "features": features,
            "jd_struct": jd_struct,
            "resume_skills": resume_skills,
        }