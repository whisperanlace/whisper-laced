from fastapi import HTTPException
from backend.services.toggle_service import ToggleService

toggle_service = ToggleService()

class ToggleController:

    async def list_toggles(self, current_user):
        return await toggle_service.get_toggles(current_user)

    async def update_toggle(self, toggle_id: str, enabled: bool, current_user):
        try:
            return await toggle_service.update_toggle(toggle_id, enabled, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
