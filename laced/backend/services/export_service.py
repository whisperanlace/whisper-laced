from backend.models.export_model import Export

class ExportService:

    async def create_export(self, payload, user):
        export = await Export.create(user_id=user.id, **payload.dict())
        # implement file preparation/export logic
        return export

    async def get_exports(self, user):
        return await Export.filter(user_id=user.id)

    async def delete_export(self, export_id: str, user):
        export = await Export.get_or_none(id=export_id, user_id=user.id)
        if not export:
            return False
        await export.delete()
        return True
