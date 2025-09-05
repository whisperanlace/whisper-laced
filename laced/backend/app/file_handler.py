# app/file_handler.py
import os
from fastapi import UploadFile
from uuid import uuid4
from ..config import settings

UPLOAD_DIR = settings.UPLOAD_DIR
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_file(file: UploadFile, subdir: str = "") -> str:
    folder = os.path.join(UPLOAD_DIR, subdir)
    os.makedirs(folder, exist_ok=True)

    filename = f"{uuid4()}_{file.filename}"
    file_path = os.path.join(folder, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return file_path
