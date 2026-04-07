#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/Users/mikerosenthal/.openclaw/workspace"
SRC_BASE="$WORKSPACE/Goodz/meta-ads"
DST_BASE="$WORKSPACE/Goodz/meta-ads-share"

LATEST_RUN=$(python3 - <<'PY'
import json
p='/Users/mikerosenthal/.openclaw/workspace/Goodz/meta-ads/data/raw/LATEST.json'
print(json.load(open(p))['latest_run'])
PY
)

LATEST_CREATIVES_RUN=$(python3 - <<'PY'
import json
p='/Users/mikerosenthal/.openclaw/workspace/Goodz/meta-ads/data/raw/LATEST_CREATIVES.json'
print(json.load(open(p))['latest_creatives_run'])
PY
)

echo "Publishing run: $LATEST_RUN (creatives: $LATEST_CREATIVES_RUN)"

mkdir -p "$DST_BASE/dashboard" "$DST_BASE/data/raw/$LATEST_RUN" "$DST_BASE/data/raw/$LATEST_CREATIVES_RUN" "$DST_BASE/data"

cp "$SRC_BASE/dashboard"/*.html "$DST_BASE/dashboard/"
cp "$SRC_BASE/data/raw/LATEST.json" "$DST_BASE/data/raw/LATEST.json"
cp "$SRC_BASE/data/raw/LATEST_CREATIVES.json" "$DST_BASE/data/raw/LATEST_CREATIVES.json"
cp "$SRC_BASE/data/raw/$LATEST_RUN"/*.json "$DST_BASE/data/raw/$LATEST_RUN/"
cp "$SRC_BASE/data/raw/$LATEST_CREATIVES_RUN"/*.json "$DST_BASE/data/raw/$LATEST_CREATIVES_RUN/"
cp "$SRC_BASE/data/creative_intelligence_latest.json" "$DST_BASE/data/creative_intelligence_latest.json"

cd "$DST_BASE"
git add dashboard/*.html data/raw/LATEST.json data/raw/LATEST_CREATIVES.json "data/raw/$LATEST_RUN"/*.json "data/raw/$LATEST_CREATIVES_RUN"/*.json data/creative_intelligence_latest.json
if git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git commit -m "Update dashboard snapshot: $LATEST_RUN"
git push origin main

echo "Published to GitHub. Vercel will auto-deploy."
