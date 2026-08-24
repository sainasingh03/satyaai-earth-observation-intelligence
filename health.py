from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["System"],
)


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "SATYAAI",
    }