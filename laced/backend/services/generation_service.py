from backend.models.generation_model import Generation

class GenerationService:

    async def create_generation(self, payload, user):
        return await Generation.create(user_id=user.id, **payload.dict())

    async def get_generations(self, user):
        return await Generation.filter(user_id=user.id)

    async def delete_generation(self, generation_id: str, user):
        generation = await Generation.get_or_none(id=generation_id, user_id=user.id)
        if not generation:
            return False
        await generation.delete()
        return True
