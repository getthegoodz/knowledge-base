# Goodz Meta Ads - Historical Findings (Initial)

_Last updated: 2026-03-23 (ET)_
_Source run: `data/raw/20260323T175913Z` (monthly, adset-level + campaign metadata)_

## Scope
This is a top-level retrospective of historical Goodz Meta ads performance.

## Topline
- Spend: **$18,981.15**
- Impressions: **761,833**
- Clicks: **29,567**
- Blended CTR: **~3.88%**
- Blended CPC: **~$0.64**

## Targeting patterns used historically
- Geography: **US-only** across all ad sets in this pull.
- Age targeting: overwhelmingly **18-65** (with only minor exceptions).
- Gender: mostly broad/unspecified.
- Audience strategy: mostly **broad + interest**; limited custom audience / retargeting usage.

## ROAS / purchase-signal findings
Purchase-linked data is present in this snapshot (Shopify/pixel-linked periods).

- Rows with `purchase_roas`: **48 / 85** monthly adset rows.
- Ad sets with some purchase signal: **35**.
- Aggregate where purchase signal exists:
  - Spend: **$18,068.61**
  - Tracked purchase value: **$76,277.69**
  - Calculated ROAS (value/spend): **4.22**

### Important caveat
`purchase_roas` from Meta and calculated ROAS from `action_values.purchase` do not always match exactly due to attribution settings, event mapping, reporting windows, and metric definitions. Use both, but treat them as directional unless we lock one canonical reporting definition.

## High-value ad sets (by tracked purchase value)
1. **DOD | ASC | 2024 | WC Ad set**
   - Spend: $5,988.26
   - Purchase value: $35,158.40
   - Calculated ROAS: 5.87
2. **Broad_IG only**
   - Spend: $1,375.65
   - Purchase value: $7,816.77
   - Calculated ROAS: 5.68
3. **Valentine's Day**
   - Spend: $403.42
   - Purchase value: $4,438.44
   - Calculated ROAS: 11.00
4. **35+ w/ Jazz Artist Interest**
   - Spend: $2,161.10
   - Purchase value: $3,517.38
   - Calculated ROAS: 1.63
5. **04012024_Broad_IG Only**
   - Spend: $551.68
   - Purchase value: $3,469.59
   - Calculated ROAS: 6.29

## Early "what worked" read
- **Broad + IG-forward** variants repeatedly produced strong efficiency.
- **Seasonal/gifting angles** showed standout click and purchase efficiency in some periods.
- **ASC** drove large volume and value in at least one major campaign, though with higher CPC than broad winners.
- **Retargeting in this data slice appears weak** (small spend but poor efficiency), likely due to audience size and/or setup quality at the time.

## Heuristic strategy bucket analysis (name-based classification)
- **ASC:** spend $6,499.81, calc ROAS 5.61, CTR 2.68%, CPC $1.76
- **Broad:** spend $3,912.72, calc ROAS 4.37, CTR 4.28%, CPC $0.53
- **Interest-based:** spend $5,879.13, calc ROAS 2.66, CTR 3.61%, CPC $0.51
- **Retargeting:** spend $562.91, calc ROAS 0.53, CTR 1.51%, CPC $2.79
- **Seasonal-angle:** spend $403.42, calc ROAS 11.00, CTR 7.60%, CPC $0.21 (small sample)

## Recommended relaunch testing matrix (ROAS-first)
1. **ASC Purchase** (always-on)
   - Goal: scale while monitoring MER/ROAS guardrails.
2. **Broad Purchase (IG-heavy placement split)**
   - Goal: lower CPC + healthy conversion rate.
3. **Curated interest clusters** (music nostalgia, gifting, artist affinity)
   - Goal: find efficient expansion pools.
4. **Retargeting reboot** (strictly segmented windows + creative refresh)
   - Goal: lift conversion efficiency from warm traffic.
5. **Seasonal offer cells** (event/holiday hooks)
   - Goal: exploit known high-intent windows.

## Next analysis pass (recommended)
- Pull **daily ad-level** insights for the last 12 months only (lower API stress).
- Add purchase event normalization by action type and attribution window.
- Rebuild dashboard with:
  - Spend, purchase value, calculated ROAS, Meta-reported purchase_roas
  - Trendlines by month
  - audience bucket breakout
  - creative/ad-level leaderboard
