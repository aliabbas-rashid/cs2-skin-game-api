from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pip._internal.network import auth

app = FastAPI(title="CS2 Skin Guessing Game API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(game.router, prefix="/api/game")

@app.get("/")
def root():
    return {"message": "API running!"}

@app.get("/health_check")
def health_check():
    return {"ok": True}