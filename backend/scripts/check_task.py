import sys, json
from celery.result import AsyncResult
from backend.celery_app import app

def main(task_id: str):
    r = AsyncResult(task_id, app=app)
    out = {
        "id": task_id,
        "ready": r.ready(),
        "successful": r.successful() if r.ready() else None,
        "status": r.status,
        "result": r.result if r.ready() else None,
    }
    print(json.dumps(out, indent=2, default=str))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m backend.scripts.check_task <task_id>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])