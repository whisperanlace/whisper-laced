from backend.models.apikey_model import Api_Key
import secrets

class Api_keyService:

    async def generate_api_key(self, user):
        key = secrets.token_urlsafe(32)
        return await Api_Key.create(user_id=user.id, key=key)

    async def list_keys(self, user):
        return await Api_Key.filter(user_id=user.id)

    async def revoke_key(self, key_id: str, user):
        key = await Api_Key.get_or_none(id=key_id, user_id=user.id)
        if not key:
            return False
        await key.delete()
        return True
