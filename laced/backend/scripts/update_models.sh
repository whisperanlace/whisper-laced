#!/usr/bin/env bash
set -euo pipefail
# Pull updated model bundles to local mounted storage path.
STORAGE=${STORAGE_PATH:-/var/lib/laced/storage}
MODEL_REPO=${MODEL_REPO:-""} # optional remote model repo URL
if [ -z "${MODEL_REPO}" ]; then
  echo "MODEL_REPO not configured; falling back to local checks"
  exit 0
fi
git -C "${STORAGE}" pull || git clone "${MODEL_REPO}" "${STORAGE}/models"
echo "Model update complete"
