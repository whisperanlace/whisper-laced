from backend.models.activity_model import Activity

class ActivityService:

    async def log_activity(self, action: str, user):
        return await Activity.create(user_id=user.id, action=action)

    async def get_user_activity(self, user):
        return await Activity.filter(user_id=user.id)
