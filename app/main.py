from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from app.database import init_db
from app.routers import auth as auth_router
from app.routers.predict import router as predict_router
from app.routers.rank import router as rank_router

app = FastAPI(title="Resume Scorer Backend")

init_db()

allowed = [

    os.getenv("FRONTEND_URL"),
    "https://match-my-resume-frontend.vercel.app",
    "https://match-my-resume-frontend-1jy1w2ymm-acpradyumna2103s-projects.vercel.app",
    "http://localhost:5173"


]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(predict_router, tags=["predict"])
app.include_router(rank_router, tags=["rank"])

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
