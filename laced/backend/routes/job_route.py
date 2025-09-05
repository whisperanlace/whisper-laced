from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.job_controller import JobController
from backend.schemas.job_schema import JobSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
job_ctrl = JobController()

@router.get("/", response_model=List[JobSchema])
async def list_jobs(current_user=Depends(get_current_user)):
    return await job_ctrl.list_jobs(current_user)

@router.post("/", response_model=JobSchema)
async def create_job(payload: JobSchema, current_user=Depends(get_current_user)):
    try:
        return await job_ctrl.create_job(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{job_id}", status_code=204)
async def delete_job(job_id: str, current_user=Depends(get_current_user)):
    await job_ctrl.delete_job(job_id, current_user)
    return {"detail": "Deleted"}
