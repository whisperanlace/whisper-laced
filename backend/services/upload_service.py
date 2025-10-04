from sqlalchemy.orm import Session
from backend.models import Upload
from backend.schemas.upload_schema import UploadCreate

def create_upload(db: Session, upload: UploadCreate, user_id: int):
    db_upload = Upload(filename=upload.filename, file_url=upload.file_url, user_id=user_id)
    db.add(db_upload)
    db.commit()
    db.refresh(db_upload)
    return db_upload

def list_uploads(db: Session):
    return db.query(Upload).all()

