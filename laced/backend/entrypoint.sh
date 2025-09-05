#!/usr/bin/env bash
set -euo pipefail

# Wait for DB/Redis if needed (simple check loop)
wait_for() {
  host=$1
  port=$2
  n=0
  until nc -z $host $port; do
    n=$((n+1))
    if [ $n -ge 60 ]; then
      echo "timeout waiting for $host:$port"
      exit 1
    fi
    echo "waiting for $host:$port..."
    sleep 1
  done
}

if [ -n "${DB_HOST:-}" ]; then
  wait_for "${DB_HOST}" "${DB_PORT:-5432}"
fi

if [ -n "${REDIS_HOST:-}" ]; then
  wait_for "${REDIS_HOST}" "${REDIS_PORT:-6379}"
fi

# Run migrations
if [ -f "./alembic.ini" ]; then
  alembic upgrade head || echo "alembic upgrade failed"
fi

# Start Uvicorn
exec uvicorn backend.app.main:app --host ${SERVER_HOST:-0.0.0.0} --port ${SERVER_PORT:-8888} --workers ${WORKERS:-4}
