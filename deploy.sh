#!/usr/bin/env bash
set -euo pipefail

if [[ -f ".env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source ".env"
  set +a
fi

required_vars=(
  SSH_HOST
  SSH_USER
  MAIN_REMOTE_DIR
  GUIDE_REMOTE_DIR
)

missing_vars=()
for var_name in "${required_vars[@]}"; do
  if [[ -z "${!var_name:-}" ]]; then
    missing_vars+=("${var_name}")
  fi
done

if (( ${#missing_vars[@]} > 0 )); then
  printf '%s\n' "${missing_vars[@]}"
  exit 1
fi

SSH_PORT="${SSH_PORT:-22}"
RSYNC_RSH="${RSYNC_RSH:-ssh -p ${SSH_PORT}}"

python3 scripts/build_public.py

rsync -avz --delete \
  --exclude '.git/' \
  --exclude '.vscode/' \
  --exclude '.env.example' \
  --exclude '*.ps1' \
  --exclude '*.md' \
  --exclude '*.txt' \
  --exclude '*.csv' \
  --exclude '*.json' \
  --exclude 'deploy.sh' \
  --exclude 'CHANGELOG.md' \
  -e "${RSYNC_RSH}" \
  ./public/ "${SSH_USER}@${SSH_HOST}:${MAIN_REMOTE_DIR%/}/"

rsync -avz --delete \
  --exclude '.git/' \
  --exclude '.vscode/' \
  --exclude '.env.example' \
  --exclude '*.ps1' \
  --exclude '*.md' \
  --exclude '*.txt' \
  --exclude '*.csv' \
  --exclude '*.json' \
  --exclude 'deploy.sh' \
  --exclude 'CHANGELOG.md' \
  -e "${RSYNC_RSH}" \
  ./guide/ "${SSH_USER}@${SSH_HOST}:${GUIDE_REMOTE_DIR%/}/"
