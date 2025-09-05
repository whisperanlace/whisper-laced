from backend.models.job_model import Job

class JobService:

    async def create_job(self, payload, user):
        return await Job.create(user_id=user.id, **payload.dict())

    async def get_jobs(self, user):
        return await Job.filter(user_id=user.id)

    async def delete_job(self, job_id: str, user):
        job = await Job.get_or_none(id=job_id, user_id=user.id)
        if not job:
            return False
        await job.delete()
        return True
