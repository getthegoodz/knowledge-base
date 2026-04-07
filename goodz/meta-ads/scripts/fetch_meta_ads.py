#!/usr/bin/env python3
import argparse
import csv
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone

API_VERSION = "v22.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_env(path: str):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip()
            if k and k not in os.environ:
                os.environ[k] = v


def api_get(url, params):
    qs = urllib.parse.urlencode(params)
    full_url = f"{url}?{qs}"
    req = urllib.request.Request(full_url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", errors="ignore")
        except Exception:
            pass
        msg = f"HTTP {e.code} from Meta API at {url}"
        if body:
            msg += f"\nResponse: {body}"
        raise RuntimeError(msg) from e


def fetch_all_pages(url, params):
    out = []
    req_params = params.copy()
    while True:
        payload = api_get(url, req_params)
        data = payload.get("data", [])
        out.extend(data)

        after = payload.get("paging", {}).get("cursors", {}).get("after")
        if not after:
            break

        req_params["after"] = after
    return out


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def flatten(d, parent_key="", sep="."):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten(v, new_key, sep=sep))
        elif isinstance(v, list):
            items[new_key] = json.dumps(v, ensure_ascii=False)
        else:
            items[new_key] = v
    return items


def write_csv(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not rows:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write("")
        return

    flat_rows = [flatten(r) for r in rows]
    keys = sorted({k for r in flat_rows for k in r.keys()})
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(flat_rows)


def build_appsecret_proof(access_token: str, app_secret: str) -> str:
    digest = hmac.new(app_secret.encode("utf-8"), msg=access_token.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
    return digest


def main():
    parser = argparse.ArgumentParser(description="Fetch Meta Ads objects + insights")
    parser.add_argument("--env", default="/Users/mikerosenthal/.openclaw/workspace/Goodz/.secrets/meta.env")
    parser.add_argument("--out", default="/Users/mikerosenthal/.openclaw/workspace/Goodz/meta-ads/data/raw")
    parser.add_argument("--since", default=None, help="YYYY-MM-DD")
    parser.add_argument("--until", default=None, help="YYYY-MM-DD")
    parser.add_argument("--insights-level", default="campaign", choices=["account", "campaign", "adset", "ad"])
    parser.add_argument("--time-increment", default="1", help="1, monthly, or all_days")
    args = parser.parse_args()

    load_env(args.env)

    token = os.environ.get("META_SYSTEM_USER_TOKEN")
    act_id = os.environ.get("AD_ACCOUNT_ID")
    app_secret = os.environ.get("META_APP_SECRET")

    if not token or not act_id:
        print("Missing META_SYSTEM_USER_TOKEN or AD_ACCOUNT_ID", file=sys.stderr)
        sys.exit(1)

    if not act_id.startswith("act_"):
        act_id = f"act_{act_id}"

    common = {"access_token": token, "limit": 200}
    if app_secret:
        common["appsecret_proof"] = build_appsecret_proof(token, app_secret)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = os.path.join(args.out, stamp)
    os.makedirs(out_dir, exist_ok=True)

    campaign_fields = "id,name,status,objective,buying_type,created_time,updated_time,start_time,stop_time,daily_budget,lifetime_budget,special_ad_categories"
    adset_fields = "id,name,status,campaign_id,optimization_goal,billing_event,bid_strategy,daily_budget,lifetime_budget,start_time,end_time,targeting,created_time,updated_time"
    ad_fields = "id,name,status,campaign_id,adset_id,created_time,updated_time,creative,effective_status"

    print("Fetching campaigns...")
    campaigns = fetch_all_pages(
        f"{BASE_URL}/{act_id}/campaigns",
        {**common, "fields": campaign_fields},
    )
    write_json(os.path.join(out_dir, "campaigns.json"), campaigns)
    write_csv(os.path.join(out_dir, "campaigns.csv"), campaigns)

    print("Fetching ad sets...")
    adsets = fetch_all_pages(
        f"{BASE_URL}/{act_id}/adsets",
        {**common, "fields": adset_fields},
    )
    write_json(os.path.join(out_dir, "adsets.json"), adsets)
    write_csv(os.path.join(out_dir, "adsets.csv"), adsets)

    print("Fetching ads...")
    ads = fetch_all_pages(
        f"{BASE_URL}/{act_id}/ads",
        {**common, "fields": ad_fields},
    )
    write_json(os.path.join(out_dir, "ads.json"), ads)
    write_csv(os.path.join(out_dir, "ads.csv"), ads)

    insights_fields = ",".join([
        "account_id", "account_name", "campaign_id", "campaign_name",
        "adset_id", "adset_name", "ad_id", "ad_name",
        "date_start", "date_stop", "objective", "spend",
        "impressions", "reach", "clicks", "inline_link_clicks",
        "ctr", "cpc", "cpm", "actions", "action_values", "conversions", "conversion_values", "purchase_roas"
    ])

    params = {
        **common,
        "fields": insights_fields,
        "level": args.insights_level,
        "time_increment": args.time_increment,
    }

    if args.since and args.until:
        params["time_range"] = json.dumps({"since": args.since, "until": args.until})

    print(f"Fetching insights (level={args.insights_level}, time_increment={args.time_increment})...")
    insights = fetch_all_pages(
        f"{BASE_URL}/{act_id}/insights",
        params,
    )
    insights_base = f"insights_{args.time_increment}_{args.insights_level}"
    write_json(os.path.join(out_dir, f"{insights_base}.json"), insights)
    write_csv(os.path.join(out_dir, f"{insights_base}.csv"), insights)

    manifest = {
        "created_at": now_iso(),
        "api_version": API_VERSION,
        "ad_account_id": act_id,
        "counts": {
            "campaigns": len(campaigns),
            "adsets": len(adsets),
            "ads": len(ads),
            f"insights_{args.time_increment}_{args.insights_level}": len(insights),
        },
        "since": args.since,
        "until": args.until,
    }
    write_json(os.path.join(out_dir, "manifest.json"), manifest)

    latest_pointer = {
        "latest_run": stamp,
        "updated_at": now_iso(),
    }
    write_json(os.path.join(args.out, "LATEST.json"), latest_pointer)

    print("Done.")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
