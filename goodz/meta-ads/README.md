# Goodz Meta Ads Data Pipeline (Phase 1: Read-only)

This folder contains the first-step ingestion flow for Meta Ads historical reporting.

## What it does
- Pulls account objects:
  - campaigns
  - adsets
  - ads
- Pulls insights:
  - daily, ad-level metrics
- Writes JSON + CSV outputs to timestamped folders under `data/raw/`

## Secrets
Expected env file:
- `Goodz/.secrets/meta.env`

Required keys:
- `META_SYSTEM_USER_TOKEN`
- `AD_ACCOUNT_ID` (usually `act_...`)

Optional (kept for future phases):
- `META_APP_ID`
- `META_APP_SECRET`

## Run
From workspace root:

```bash
python3 Goodz/meta-ads/scripts/fetch_meta_ads.py
```

Optional date range backfill (lighter call load):

```bash
python3 Goodz/meta-ads/scripts/fetch_meta_ads.py --since 2023-03-01 --until 2026-03-23 --insights-level campaign --time-increment monthly
```

Higher-granularity pull (heavier API load):

```bash
python3 Goodz/meta-ads/scripts/fetch_meta_ads.py --since 2025-01-01 --until 2026-03-23 --insights-level ad --time-increment 1
```

## Output layout
- `Goodz/meta-ads/data/raw/<timestamp>/campaigns.json|csv`
- `Goodz/meta-ads/data/raw/<timestamp>/adsets.json|csv`
- `Goodz/meta-ads/data/raw/<timestamp>/ads.json|csv`
- `Goodz/meta-ads/data/raw/<timestamp>/insights_daily_ad.json|csv`
- `Goodz/meta-ads/data/raw/<timestamp>/manifest.json`
- `Goodz/meta-ads/data/raw/LATEST.json`

## Notes
- This is read-only and safe for initial discovery.
- Next phase will add normalized reporting tables and derived KPI summaries.
