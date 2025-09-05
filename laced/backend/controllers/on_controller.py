from fastapi import HTTPException
from backend.services.on_service import OnService

on_service = OnService()

class OnController:

    async def toggle_on_feature(self, feature_id: str, current_user):
        try:
            return await on_service.toggle_feature(feature_id, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
