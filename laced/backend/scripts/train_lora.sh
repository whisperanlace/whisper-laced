#!/usr/bin/env bash
set -euo pipefail
# Wrapper to kick off training in a containerized environment. Expects dataset path and config.
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <dataset-dir> [output-lora-name]"
  exit 1
fi
DATASET=$1
OUTNAME=${2:-lora_$(date +"%Y%m%d%H%M")}
docker run --gpus all --rm -v $(pwd)/${DATASET}:/data -v ${STORAGE_PATH:-/var/lib/laced/storage}:/storage laced-trainer:latest /bin/bash -lc "train-command --data /data --out /storage/loras/${OUTNAME}.pt"
echo "Training job submitted for ${OUTNAME}"
