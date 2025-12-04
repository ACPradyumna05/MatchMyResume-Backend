import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class FeatureBuilder:
    def __init__(self, embedder, preproc):
        self.embedder = embedder
        self.preproc = preproc

    def build(self, resume_text, resume_skills, jd_name=None, jd_text=None, jd_keywords=None, jd_skills=None):
        jd = self.preproc.get_jd(jd_name, jd_text, jd_keywords, jd_skills)
        features = {}

        features["jd_skill_count"] = len(jd["skills"])
        features["jd_keyword_count"] = len(jd["keywords"])

        rs = [s.lower() for s in resume_skills]
        matches = sum(1 for js in jd["skills"] if js in rs)
        features["exact_skill_match_pct"] = matches / max(1, len(jd["skills"]))

        txt = resume_text.lower()
        kw_hits = sum(1 for kw in jd["keywords"] if kw in txt)
        features["keyword_coverage_pct"] = kw_hits / max(1, len(jd["keywords"]))

        jd_emb = self.embedder.encode([jd["combined_text"]], convert_to_numpy=True)
        res_emb = self.embedder.encode([resume_text], convert_to_numpy=True)
        skills_emb = self.embedder.encode([" ".join(resume_skills)], convert_to_numpy=True)

        features["jd_resume_cosine"] = float(cosine_similarity(jd_emb, res_emb)[0, 0])
        features["skillset_cosine"] = float(cosine_similarity(jd_emb, skills_emb)[0, 0])

        for c in self.preproc.numeric_cols:
            features[c] = 0.0

        X = np.array([[features.get(c, 0.0) for c in self.preproc.feature_cols]], dtype=float)

        return features, X, jd
