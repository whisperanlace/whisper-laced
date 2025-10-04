from backend.celery_app import celery

@celery.task(name="notify.user")
def notify_user_task(user_id: int, message: str) -> dict:
    # Stub: integrate real email/sms/push later
    return {"status": "queued", "user_id": user_id, "message": message}
