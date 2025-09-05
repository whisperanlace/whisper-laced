from backend.models.upload_model import Upload

class UploadService:

    async def upload_file(self, file, user):
        upload = await Upload.create(user_id=user.id, file_path=file.filename)
        # implement actual file saving logic
        return upload

    async def get_uploads(self, user):
        return await Upload.filter(user_id=user.id)

    async def delete_upload(self, upload_id: str, user):
        upload = await Upload.get_or_none(id=upload_id, user_id=user.id)
        if not upload:
            return False
        await upload.delete()
        return True
