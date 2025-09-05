#!/usr/bin/env bash
set -euo pipefail
if [ -z "${1:-}" ]; then
  echo "Usage: $0 backup-file.sql.gz"
  exit 1
fi
FILE=$1
PGHOST=${DB_HOST:-localhost}
PGPORT=${DB_PORT:-5432}
PGUSER=${DB_USER:-laced}
PGDATABASE=${DB_NAME:-laced}

gunzip -c "${FILE}" | psql -h "${PGHOST}" -p "${PGPORT}" -U "${PGUSER}" "${PGDATABASE}"
echo "Restore complete"
