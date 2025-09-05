from backend.models.moderation_model import Moderation

class ModerationService:

    async def moderate_content(self, payload, user):
        return await Moderation.create(user_id=user.id, **payload.dict())

    async def get_moderation_logs(self, user):
        return await Moderation.filter(user_id=user.id)

    async def delete_moderation_log(self, log_id: str, user):
        log = await Moderation.get_or_none(id=log_id, user_id=user.id)
        if not log:
            return False
        await log.delete()
        return True
