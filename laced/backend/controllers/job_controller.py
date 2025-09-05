# controllers/job_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.job_schema import JobOut
from services.job_service import JobService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    job = JobService.get_job(db, job_id, user.id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
