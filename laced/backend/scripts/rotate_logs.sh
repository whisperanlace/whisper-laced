#!/usr/bin/env bash
set -euo pipefail
LOG_DIR=${LOG_DIR:-/var/log/laced}
mkdir -p "${LOG_DIR}"
find "${LOG_DIR}" -maxdepth 1 -type f -mtime +7 -exec gzip {} \;
echo "Logs rotated"
