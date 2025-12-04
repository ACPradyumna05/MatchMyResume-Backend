import importlib.util
import os
import joblib

class PreprocLoader:
    def __init__(self):
        self.module_path = os.path.join(os.path.dirname(__file__), "preprocessed.py")
        spec = importlib.util.spec_from_file_location("preproc", self.module_path)
        preproc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(preproc)
        self.preproc = preproc
        model_info = joblib.load("models_out_fixed/resume_match_xgb.joblib")
        self.feature_cols = model_info["feature_cols"]
        self.numeric_cols = model_info["numeric_cols"]
        self.jd_requirements = getattr(preproc, "jd_requirements", {})

    def get_jd(self, jd_name=None, jd_text=None, jd_keywords=None, jd_skills=None):
        jd = {"skills": [], "keywords": [], "combined_text": ""}
        if jd_name and jd_name in self.jd_requirements:
            d = self.jd_requirements[jd_name]
            jd["skills"] = [s.lower() for s in d.get("skills", [])]
            jd["keywords"] = [k.lower() for k in d.get("keywords", [])]
            jd["combined_text"] = d.get("description", jd_name)
            return jd
        if jd_skills:
            jd["skills"] = [s.lower() for s in jd_skills]
        if jd_keywords:
            jd["keywords"] = [k.lower() for k in jd_keywords]
        jd["combined_text"] = jd_text or ""
        return jd