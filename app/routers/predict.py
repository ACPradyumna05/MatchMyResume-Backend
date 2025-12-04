from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.scorer import ScoreService
from app.services.pdf_parser import PDFParser
from app.services.feature_builder import FeatureBuilder
from app.services.nlp_extract import NLPExtractor
from app.utils.preproc_loader import PreprocLoader

router = APIRouter()

score_service = ScoreService()
pdf_parser = PDFParser()
nlp_extractor = NLPExtractor()
preproc = PreprocLoader()
feature_builder = FeatureBuilder(score_service.embedder, preproc)


@router.post("/predict_file")
async def predict_file(
    file: UploadFile = File(...),
    jd_name: str | None = Form(None),
    jd_text: str | None = Form(None),
    jd_keywords: str | None = Form(None),
    jd_skills: str | None = Form(None),
):
    """
    Upload a PDF resume and provide JD name OR JD text.
    JD keywords & JD skills can be comma-separated lists.
    """

    pdf_bytes = await file.read()
    try:
        resume_text = pdf_parser.parse(pdf_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF parsing failed: {e}")

    resume_skills = nlp_extractor.extract_skills(resume_text)

    kw_list = [k.strip().lower() for k in jd_keywords.split(",")] if jd_keywords else []
    sk_list = [s.strip().lower() for s in jd_skills.split(",")] if jd_skills else []

    features, X, jd_struct = feature_builder.build(
        resume_text=resume_text,
        resume_skills=resume_skills,
        jd_name=jd_name,
        jd_text=jd_text,
        jd_keywords=kw_list,
        jd_skills=sk_list,
    )

    score = score_service.predict(X)

    text_lower = resume_text.lower()
    matched_keywords = [kw for kw in jd_struct["keywords"] if kw in text_lower]
    matched_skills = [s for s in resume_skills if s in jd_struct["skills"]]

    return {
        "score": round(score, 2),
        "features": features,
        "matched_skills": matched_skills,
        "matched_keywords": matched_keywords,
        "resume_text_snippet": resume_text[:1000],
    }


@router.get("/health")
def health():
    return {
        "status": "OK",
        "model_loaded": True,
        "embedder": type(score_service.embedder).__name__,
    }
