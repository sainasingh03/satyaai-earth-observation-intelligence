from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile


router = APIRouter(
    prefix="/api/data",
    tags=["Satellite Data"],
)


UPLOAD_DIR = Path(
    "../data/uploads"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


ALLOWED_EXTENSIONS = {
    ".tif",
    ".tiff",
    ".png",
    ".jpg",
    ".jpeg",
}


@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
):

    extension = Path(
        file.filename or ""
    ).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail="Unsupported file type.",
        )

    filename = (
        f"{uuid4().hex}"
        f"{extension}"
    )

    destination = (
        UPLOAD_DIR / filename
    )

    content = await file.read()

    destination.write_bytes(
        content
    )

    return {
        "filename": filename,
        "size_bytes": len(content),
        "status": "uploaded",
    }