#!/usr/bin/env python3
import argparse
import hashlib
import hmac
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_VERSION = "v22.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"


def load_env(path: str):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k and k not in os.environ:
                os.environ[k.strip()] = v.strip()


def appsecret_proof(token: str, secret: str) -> str:
    return hmac.new(secret.encode(), msg=token.encode(), digestmod=hashlib.sha256).hexdigest()


def api_get(url, params):
    qs = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{qs}", method="GET")
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP {e.code} {url}\n{body}") from e


def fetch_pages(url, params):
    out = []
    req_params = params.copy()
    while True:
        payload = api_get(url, req_params)
        out.extend(payload.get("data", []))
        after = payload.get("paging", {}).get("cursors", {}).get("after")
        if not after:
            break
        req_params["after"] = after
    return out


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--env", default="/Users/mikerosenthal/.openclaw/workspace/Goodz/.secrets/meta.env")
    p.add_argument("--out", default="/Users/mikerosenthal/.openclaw/workspace/Goodz/meta-ads/data/raw")
    args = p.parse_args()

    load_env(args.env)
    token = os.environ.get("META_SYSTEM_USER_TOKEN")
    act_id = os.environ.get("AD_ACCOUNT_ID")
    app_secret = os.environ.get("META_APP_SECRET")
    if not token or not act_id:
        print("Missing META_SYSTEM_USER_TOKEN or AD_ACCOUNT_ID", file=sys.stderr)
        sys.exit(1)
    if not act_id.startswith("act_"):
        act_id = f"act_{act_id}"

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(args.out, stamp)
    os.makedirs(run_dir, exist_ok=True)

    params = {
        "access_token": token,
        "limit": 100,
        "fields": (
            "id,name,status,effective_status,campaign_id,adset_id,"
            "creative{id,name,title,body,object_type,call_to_action_type,"
            "image_url,thumbnail_url,video_id,object_story_spec,asset_feed_spec,"
            "object_url,link_url,url_tags}"
        ),
    }
    if app_secret:
        params["appsecret_proof"] = appsecret_proof(token, app_secret)

    print("Fetching ads with creative payloads...")
    ads = fetch_pages(f"{BASE_URL}/{act_id}/ads", params)

    write_json(os.path.join(run_dir, "ads_with_creatives.json"), ads)
    write_json(os.path.join(args.out, "LATEST_CREATIVES.json"), {"latest_creatives_run": stamp})

    print(json.dumps({"run": stamp, "ads_with_creatives": len(ads)}, indent=2))


if __name__ == "__main__":
    main()
