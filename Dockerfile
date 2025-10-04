FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Helpful tools for healthcheck & builds
RUN apt-get update && apt-get install -y --no-install-recommends curl build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install deps first (better layer cache)
COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# App code
COPY backend ./backend

EXPOSE 8000

# Runtime healthcheck (executed when the container runs, NOT during build)
HEALTHCHECK --interval=15s --timeout=3s --retries=10 CMD curl -fsS http://127.0.0.1:8000/healthz || exit 1

# Run DB migrations then start API
# Expect DATABASE_URL at runtime (RunPod / docker run)
CMD ["sh","-c","alembic -c backend/alembic.ini upgrade head && exec uvicorn backend.app.main:app --host 0.0.0.0 --port 8000"]
