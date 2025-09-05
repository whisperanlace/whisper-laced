#!/usr/bin/env bash
set -euo pipefail
STORAGE=${STORAGE_PATH:-/var/lib/laced/storage}
# Delete files older than 90 days (images, temporary)
find "${STORAGE}" -type f -mtime +90 -name '*.png' -or -name '*.jpg' -or -name '*.jpeg' -or -name '*.webp' -delete
echo "Cleanup completed in ${STORAGE}"
