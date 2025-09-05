from backend.models.premium_model import Premium

class PremiumService:

    async def subscribe_premium(self, user, plan_id: str):
        return await Premium.create(user_id=user.id, plan_id=plan_id)

    async def get_premium_status(self, user):
        return await Premium.get_or_none(user_id=user.id)

    async def cancel_premium(self, premium_id: str, user):
        premium = await Premium.get_or_none(id=premium_id, user_id=user.id)
        if not premium:
            return False
        await premium.delete()
        return True
