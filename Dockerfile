FROM python:3.11-slim AS builder
WORKDIR /w
COPY requirements.txt /w/requirements.txt
RUN pip install --upgrade pip && pip wheel --no-cache-dir -r /w/requirements.txt -w /w/wheels

FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /w/wheels /wheels
RUN pip install --no-cache /wheels/* && useradd -m appuser
COPY backend/ /app/backend/
COPY requirements.txt /app/requirements.txt
ENV PYTHONPATH=/app
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=15s --timeout=3s --retries=10 CMD python - <<'PY' || exit 1
import json,urllib.request
try:
    with urllib.request.urlopen("http://127.0.0.1:5000/health",timeout=2) as r:
        d=json.load(r); 
        raise SystemExit(0 if d.get("status")=="ok" else 1)
except Exception: raise SystemExit(1)
PY
CMD ["uvicorn","backend.app.prod_main:app","--host","0.0.0.0","--port","5000","--workers","2"]
