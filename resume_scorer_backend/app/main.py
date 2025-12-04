from fastapi import FastAPI
from app.routers.predict import router as predict_router
from fastapi.middleware.cors import CORSMiddleware
from app.routers.rank import router as rank_router






app = FastAPI(title="Resume Scorer (Modular)")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(rank_router)
app.include_router(predict_router)
