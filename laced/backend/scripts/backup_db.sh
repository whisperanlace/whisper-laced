#!/usr/bin/env bash
set -euo pipefail
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
OUTFILE="db-backup-${TIMESTAMP}.sql.gz"
PGHOST=${DB_HOST:-localhost}
PGPORT=${DB_PORT:-5432}
PGUSER=${DB_USER:-laced}
PGDATABASE=${DB_NAME:-laced}

pg_dump -h "${PGHOST}" -p "${PGPORT}" -U "${PGUSER}" "${PGDATABASE}" | gzip > "${OUTFILE}"
echo "Backup written to ${OUTFILE}"
