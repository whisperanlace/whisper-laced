from backend.models.log_model import Log

class LogService:

    async def create_log(self, payload):
        return await Log.create(**payload.dict())

    async def get_logs(self, user=None):
        if user:
            return await Log.filter(user_id=user.id)
        return await Log.all()

    async def delete_log(self, log_id: str):
        log = await Log.get_or_none(id=log_id)
        if not log:
            return False
        await log.delete()
        return True
