from fastapi import FastAPI
from app.db.init_db import initialize_database
from fastapi.middleware.cors import CORSMiddleware

from app.api.ai import router as ai_router
from app.api.health import router as health_router
from app.api.upload import router as upload_router


initialize_database()
app = FastAPI(
    title="SATYAAI",
    description="Ask the Earth. Understand the Change.",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_router)
app.include_router(ai_router)
app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "name": "SATYAAI",
        "tagline": "Ask the Earth. Understand the Change.",
        "status": "online",
    }