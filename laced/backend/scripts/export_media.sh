#!/usr/bin/env bash
set -euo pipefail
OUT=${1:-media-export-$(date +%Y%m%d).tar.gz}
STORAGE=${STORAGE_PATH:-/var/lib/laced/storage}
tar -czf "${OUT}" -C "${STORAGE}" .
echo "Media exported to ${OUT}"
