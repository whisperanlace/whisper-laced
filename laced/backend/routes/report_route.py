from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.report_controller import ReportController
from backend.schemas.report_schema import ReportSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
report_ctrl = ReportController()

@router.get("/", response_model=List[ReportSchema])
async def list_reports(current_user=Depends(get_current_user)):
    return await report_ctrl.list_reports(current_user)

@router.post("/", response_model=ReportSchema)
async def create_report(payload: ReportSchema, current_user=Depends(get_current_user)):
    try:
        return await report_ctrl.create_report(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{report_id}", status_code=204)
async def delete_report(report_id: str, current_user=Depends(get_current_user)):
    await report_ctrl.delete_report(report_id, current_user)
    return {"detail": "Deleted"}
