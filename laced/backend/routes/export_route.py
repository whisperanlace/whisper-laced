from fastapi import APIRouter, Depends, HTTPException
from backend.controllers.exports_controller import ExportsController
from backend.schemas.exports_schema import ExportSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
exports_ctrl = ExportsController()

@router.get("/", response_model=list[ExportSchema])
async def list_exports(current_user=Depends(get_current_user)):
    return await exports_ctrl.list_exports(current_user)

@router.post("/", response_model=ExportSchema)
async def create_export(current_user=Depends(get_current_user)):
    try:
        return await exports_ctrl.create_export(current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{export_id}", status_code=204)
async def delete_export(export_id: str, current_user=Depends(get_current_user)):
    await exports_ctrl.delete_export(export_id, current_user)
    return {"detail": "Deleted"}
