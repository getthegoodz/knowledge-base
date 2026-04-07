#!/usr/bin/env python3
import json
import os
import re
from collections import defaultdict

BASE = '/Users/mikerosenthal/.openclaw/workspace/Goodz/meta-ads'
RAW = f'{BASE}/data/raw'


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def action_map(arr):
    out = {}
    if isinstance(arr, list):
        for x in arr:
            k = x.get('action_type')
            try:
                v = float(x.get('value'))
            except Exception:
                continue
            out[k] = out.get(k, 0.0) + v
    return out


def extract_purchase_value(action_values):
    av = action_map(action_values)
    if av.get('omni_purchase'):
        return av['omni_purchase']
    if av.get('purchase'):
        return av['purchase']
    return av.get('offsite_conversion.fb_pixel_purchase', 0.0)


def extract_copy_and_media(ad):
    c = (ad or {}).get('creative') or {}
    spec = c.get('object_story_spec') or {}
    link = spec.get('link_data') or {}
    video = spec.get('video_data') or {}

    body = (c.get('body') or link.get('message') or video.get('message') or '').strip()
    headline = (c.get('title') or link.get('name') or video.get('title') or '').strip()
    cta = (c.get('call_to_action_type') or '').strip()

    image = c.get('image_url') or c.get('thumbnail_url') or ''
    video_id = c.get('video_id') or ''
    object_url = c.get('object_url') or c.get('link_url') or ''

    media_type = 'unknown'
    if video_id:
        media_type = 'video'
    elif image:
        media_type = 'image'

    return {
        'body': body,
        'headline': headline,
        'cta': cta,
        'image_url': image,
        'video_id': video_id,
        'media_type': media_type,
        'destination_url': object_url,
    }


def tag_angles(text):
    t = (text or '').lower()
    tags = []
    rules = [
        ('nostalgia', [r'nostalgia', r'mixtape', r'tape', r'back and better', r'miss']),
        ('gifting', [r'gift', r'gifting', r'for you', r'valentine', r"father'?s day", r'holiday']),
        ('artist_fandom', [r'artist', r'fans?', r'playlist', r'album', r'music']),
        ('urgency_offer', [r'offer', r'limited', r'shop now', r'get offer', r'out of stock']),
        ('ugc_social', [r'ugc', r'reel', r'creator', r'zoe', r'nick']),
    ]
    for name, pats in rules:
        if any(re.search(p, t) for p in pats):
            tags.append(name)
    return tags


def completeness_score(c):
    score = 0
    if c['body']:
        score += 1
    if c['headline']:
        score += 1
    if c['cta']:
        score += 1
    if c['image_url'] or c['video_id']:
        score += 1
    return score


def main():
    latest = load_json(f'{RAW}/LATEST.json')['latest_run']
    latest_creatives = load_json(f'{RAW}/LATEST_CREATIVES.json')['latest_creatives_run']

    insights = load_json(f'{RAW}/{latest}/insights_monthly_ad.json')
    ads = load_json(f'{RAW}/{latest_creatives}/ads_with_creatives.json')

    ads_by_id = {a['id']: a for a in ads}

    agg = defaultdict(lambda: {
        'spend': 0.0,
        'impressions': 0.0,
        'clicks': 0.0,
        'purchase_value': 0.0,
        'purchase_roas_rows': 0,
        'months': set(),
        'campaign_name': '',
        'adset_name': '',
        'ad_name': '',
    })

    for r in insights:
        ad_id = r.get('ad_id')
        if not ad_id:
            continue
        a = agg[ad_id]
        a['spend'] += float(r.get('spend') or 0)
        a['impressions'] += float(r.get('impressions') or 0)
        a['clicks'] += float(r.get('clicks') or 0)
        a['purchase_value'] += float(extract_purchase_value(r.get('action_values')))
        if r.get('purchase_roas'):
            a['purchase_roas_rows'] += 1
        if r.get('date_start'):
            a['months'].add(r['date_start'][:7])
        a['campaign_name'] = r.get('campaign_name') or a['campaign_name']
        a['adset_name'] = r.get('adset_name') or a['adset_name']
        a['ad_name'] = r.get('ad_name') or a['ad_name']

    creative_rows = []
    for ad_id, p in agg.items():
        if p['spend'] <= 0:
            continue
        ad = ads_by_id.get(ad_id, {})
        c = extract_copy_and_media(ad)
        roas = (p['purchase_value'] / p['spend']) if p['spend'] else 0.0
        ctr = (p['clicks'] / p['impressions'] * 100) if p['impressions'] else 0.0
        cpc = (p['spend'] / p['clicks']) if p['clicks'] else 0.0

        raw_text = ' '.join([
            p.get('ad_name', ''),
            p.get('adset_name', ''),
            p.get('campaign_name', ''),
            c.get('body', ''),
            c.get('headline', ''),
            c.get('cta', ''),
        ])

        creative_rows.append({
            'ad_id': ad_id,
            'ad_name': p['ad_name'] or ad.get('name', ''),
            'campaign_name': p['campaign_name'],
            'adset_name': p['adset_name'],
            'spend': round(p['spend'], 2),
            'impressions': int(round(p['impressions'])),
            'clicks': int(round(p['clicks'])),
            'ctr': round(ctr, 4),
            'cpc': round(cpc, 4),
            'purchase_value': round(p['purchase_value'], 2),
            'roas': round(roas, 4),
            'purchase_roas_rows': p['purchase_roas_rows'],
            'months_active': len(p['months']),
            'copy': c,
            'copy_completeness_score': completeness_score(c),
            'angles': tag_angles(raw_text),
        })

    winners_by_value = sorted(
        [r for r in creative_rows if r['purchase_value'] > 0 and r['spend'] >= 100],
        key=lambda x: x['purchase_value'],
        reverse=True,
    )
    winners_by_roas = sorted(
        [r for r in creative_rows if r['purchase_value'] > 0 and r['spend'] >= 100],
        key=lambda x: x['roas'],
        reverse=True,
    )

    out = {
        'generated_at': latest,
        'insights_run': latest,
        'creatives_run': latest_creatives,
        'creative_count_with_spend': len(creative_rows),
        'leaderboards': {
            'top_by_purchase_value': winners_by_value[:100],
            'top_by_roas_min100_spend': winners_by_roas[:100],
        },
        'creatives': creative_rows,
    }

    os.makedirs(f'{BASE}/data', exist_ok=True)
    with open(f'{BASE}/data/creative_intelligence_latest.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    with open(f'{RAW}/{latest}/creative_intelligence.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps({
        'insights_run': latest,
        'creatives_run': latest_creatives,
        'creative_count_with_spend': len(creative_rows),
        'top_by_purchase_value': len(winners_by_value),
        'top_by_roas': len(winners_by_roas),
    }, indent=2))


if __name__ == '__main__':
    main()
