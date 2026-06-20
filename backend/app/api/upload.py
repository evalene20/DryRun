from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import shutil
import os

from app.utils.pdf_parser import extract_text
from app.services.resume_analyzer import analyze_resume

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@router.post("/resume")
def upload_resume(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = extract_text(file_path)

    analysis = analyze_resume(text)

    return {
        "filename": file.filename,
        "analysis": analysis
    }