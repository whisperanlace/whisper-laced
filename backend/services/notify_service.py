from typing import Optional
from backend.tasks.notifications import notify_user_task

def notify_user(user_id: int, message: str, eager: bool = False) -> dict:
    if eager:
        return notify_user_task.apply(args=[user_id, message]).get()
    else:
        async_result = notify_user_task.delay(user_id, message)
        return {"task_id": async_result.id, "queued": True}
