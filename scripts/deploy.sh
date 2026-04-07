#!/bin/bash
# Goodz deploy script — pushes goodz/publish/site to Vercel via token auth
# Usage: ./scripts/deploy.sh [--prod]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SITE_DIR="$WORKSPACE_DIR/goodz/publish/site"
VERCEL_TOKEN="$(grep -E '^VERCEL_TOKEN=' ~/.config/janet/secrets.env | sed 's/VERCEL_TOKEN=//' | sed 's/#.*//' | tr -d ' \n')"

if [ -z "$VERCEL_TOKEN" ]; then
  echo "ERROR: VERCEL_TOKEN not found in ~/.config/janet/secrets.env"
  exit 1
fi

TARGET="--prebuilt"
if [ "$1" = "--prod" ]; then
  TARGET="--prod"
fi

echo "Deploying $SITE_DIR to Vercel..."
cd "$SITE_DIR"

/tmp/vercel-deploy/node_modules/.bin/vercel deploy . \
  --token="$VERCEL_TOKEN" \
  --yes \
  $TARGET

echo "Done."
