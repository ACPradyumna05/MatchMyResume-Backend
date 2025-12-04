
from fastapi import APIRouter, UploadFile, File, Form
from typing import List
from app.services.scorer import ScoreService

router = APIRouter()

@router.post("/rank_candidates")
async def rank_candidates(
    files: List[UploadFile] = File(...),
    jd_name: str = Form(""),
    jd_text: str = Form(""),
    jd_keywords: str = Form(""),
    jd_skills: str = Form(""),
):
    """
    Batch resume ranking for employers.
    Upload 1–50 resumes + one JD text.
    """

    if not jd_text or len(jd_text.strip()) < 50:
        return {"entries": [], "error": "JD text must be at least 50 characters."}

    service = ScoreService()
    results = []

    for file in files:
        pdf_bytes = await file.read()

        out = service.score_resume(
            resume_bytes=pdf_bytes,
            filename=file.filename,
            jd_name=jd_name,
            jd_text=jd_text,
            jd_keywords=jd_keywords,
            jd_skills=jd_skills,
        )

        results.append({
            "id": file.filename.replace(" ", "_"),
            "fileName": out["fileName"],
            "score": round(out["score"], 2),
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {"entries": results}
