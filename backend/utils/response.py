from fastapi import Response
import json

def json_ok(payload, status: int = 200) -> Response:
    return Response(content=json.dumps(payload), media_type="application/json", status_code=status)

def json_err(message: str, status: int = 400) -> Response:
    return Response(content=json.dumps({"detail": message}), media_type="application/json", status_code=status)
