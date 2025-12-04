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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(predict_router)
app.include_router(rank_router)

@app.get("/health")
def health():
    return {"status": "ok"}
