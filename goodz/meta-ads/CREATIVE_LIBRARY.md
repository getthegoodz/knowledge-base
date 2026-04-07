# Goodz Meta Ads - Creative Library (Initial Pull)

_Last updated: 2026-03-23 (ET)_
_Data sources:_
- Insights: `data/raw/20260323T182209Z/insights_monthly_ad.json`
- Creative payloads: `data/raw/20260323T182126Z/ads_with_creatives.json`

## Notes
- This is an initial extraction of ad-level performance + creative metadata.
- Some ads include full copy in API fields; others only expose partial creative metadata (common in older/dynamic ads).
- ROAS here uses **canonical purchase value** from action values (prefer `omni_purchase`, else `purchase`, else `offsite_conversion.fb_pixel_purchase`) divided by spend.

## Top creatives by tracked purchase value (>= $100 spend)
1. **vid-ZoeUGC_tree_1_LP-home (out of stock)**
   - Spend: $2,593.49
   - Purchase Value: $6,842.73
   - ROAS: 2.64
   - CTR: 3.09%
   - CTA: LEARN_MORE
   - Copy: "The mixtape is back and better than ever! 📼 With Goodz, you can hold, collect, and share playlists..."

2. **vid-NickUGC_hook2-home - Evergreen**
   - Spend: $1,400.54
   - Purchase Value: $2,836.30
   - ROAS: 2.03
   - CTR: 2.61%
   - CTA: GET_OFFER
   - Copy: "The mixtape is back and better than ever! 📼 ..."

3. **05172024_a mix tape for you_static_HP**
   - Spend: $835.81
   - Purchase Value: $2,225.50
   - ROAS: 2.66
   - CTR: 4.23%

4. **vid-trueLoveDeserves - Copy**
   - Spend: $1,139.92
   - Purchase Value: $1,184.42
   - ROAS: 1.04
   - CTR: 2.39%

5. **03292024_Reel w/ text_PP URL**
   - Spend: $538.07
   - Purchase Value: $1,156.53
   - ROAS: 2.15
   - CTR: 4.64%
   - CTA: SHOP_NOW
   - Copy: "You’ve got amazing taste in music. Don’t keep it to yourself. Shop Now! 🎶"

6. **Ad 4**
   - Spend: $276.81
   - Purchase Value: $1,040.42
   - ROAS: 3.76
   - CTR: 7.37%

7. **Mix Tape Static**
   - Spend: $777.43
   - Purchase Value: $980.78
   - ROAS: 1.26
   - CTR: 3.32%

8. **Jazz Crate - Modern Twist**
   - Spend: $1,288.66
   - Purchase Value: $877.06
   - ROAS: 0.68
   - CTR: 2.70%

## Early creative pattern read
- **UGC-style mixtape framing** appears in top purchase-value winners.
- **Direct nostalgic hook** ("mixtape is back") is recurrent in stronger performers.
- **Simple explicit CTA** (Shop Now / Get Offer) is present in several high-value creatives.
- Some high-CTR ads are low-spend tests, so we should prioritize winners by spend-weighted outcomes.

## Next pass to improve creative intelligence
1. Pull thumbnail/video preview URLs into a gallery index.
2. Capture headline/body/CTA completeness score by ad.
3. Tag creative angles (nostalgia, gifting, holiday, artist-specific, social-proof).
4. Build a "Creative Winners" dashboard section sorted by purchase value and ROAS, with min-spend filters.
