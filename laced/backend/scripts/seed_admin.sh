#!/usr/bin/env bash
set -euo pipefail

# This script uses the backend manage endpoint to create the seed admin via a POST.
# It expects .env to be present with SEED_ADMIN_PASSWORD and SEED_ADMIN_EMAIL (optional)
SEED_EMAIL=${SEED_ADMIN_EMAIL:-admin@example.com}
SEED_PASSWORD=${SEED_ADMIN_PASSWORD:-ChangeMeNow!}

python3 - <<PY
import os
import requests
base = os.getenv("BASE_URL","http://localhost:8888")
url = f"{base}/internal/seed-admin"
payload = {"email": os.getenv("SEED_ADMIN_EMAIL","admin@example.com"), "password": os.getenv("SEED_ADMIN_PASSWORD","ChangeMeNow!")}
try:
    r = requests.post(url, json=payload, timeout=10)
    print("seed-admin status:", r.status_code, r.text)
except Exception as e:
    print("Failed to call seed endpoint:", e)
PY
