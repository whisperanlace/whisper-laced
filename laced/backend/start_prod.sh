#!/usr/bin/env bash
set -euo pipefail
export $(grep -v '^#' .env | xargs -d '\n' || true)

# Build and start services
docker-compose build --pull
docker-compose up -d
