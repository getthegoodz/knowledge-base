# Goodz Memory

Project-specific durable memory for Goodz.

## What belongs here

- important business context
- ongoing priorities
- decisions and rationale
- recurring people / partners / constraints
- links to more detailed docs in this folder

## Current continuity

- The overnight research doc lives at `research/overnight-2026-03-30-checkout-ideas.md`.
- Janet created an initial shareable web version at `publish/overnight-research/index.html`.
- The old standalone Vercel deploy for that one-off artifact was later deleted during cleanup; the canonical version should now live under the main publishing hub at `publish/site/overnight-research/index.html`.
- Janet also created a reusable Goodz publishing site root at `publish/site/`.
- Goodz publishing hub GitHub repo: `https://github.com/getthegoodz/knowledge-base`
- `publish/site/` is the local working copy for that repo.
- Canonical Vercel project: `knowledge-base`
- Live URL: `https://knowledge-base-one-livid.vercel.app`
- This project is now GitHub-linked, so pushes to `main` should auto-trigger deploys.
- Current structure:
  - `publish/site/index.html` = project home page / artifact index
  - `publish/site/<artifact-slug>/index.html` = individual published pages
- Default publishing path for shareable Goodz artifacts is GitHub + Vercel when appropriate, but Janet may deploy directly to Vercel from a project folder for lightweight static outputs.
- When Mike asks to push a Goodz artifact live, Janet should convert local notes/docs into a clean web-readable format if needed, add/update the artifact under `publish/site/`, deploy it, and save the resulting URL here.
- Operational publishing workflow is documented in `PUBLISHING.md`.
- Recommended long-term structure under `goodz/` is:
  - `research/`
  - `product/`
  - `prototypes/`
  - `dashboards/`
  - `publish/site/`
- Preferred deployment model: GitHub-backed Vercel projects where repo pushes trigger rebuilds automatically whenever practical.

## Durable business understanding

- Goodz is a physical-digital collectibles company built around NFC-enabled objects that unlock digital experiences on tap.
- The core framing is not "tech gadget" but modern collectible keepsake: tactile, giftable, sustainable, and emotionally resonant.
- Goodz should always be referred to as `Goodz` (plural brand term), not a singularized form.
- The business has two primary lanes:
  - D2C via Shopify
  - B2B / custom work for artists, labels, events, weddings, conferences, and brands
- Current active product lines are best understood as:
  - Mixtape Goodz: customizable playlist / personal-audio / gifting product; best-selling D2C item
  - Custom Goodz: tailored client work for artists, DJs, weddings, events, and branded activations
  - Artist Goodz / Crates: premium artist- or label-linked releases, including serialized or boxed experiences
  - Authenticator / Unlocker-style Goodz: NTAG424-based products for authenticated or gated fan access
- Goodz originated from the observation that physical music culture still matters emotionally even when playback is digital, and that existing merch formats have been stale.
- Founders are Mike Rosenthal and Chris Cerrito. Goodz was conceived in late 2023 during a period when Fanaply was financially constrained.
- Goodz positioning pillars:
  - physical + digital bridge
  - collectible / tactile / giftable
  - eco-friendly materials and production
  - fan connection over tech novelty
  - flexible enough for music, gifting, events, and branded activations
- The brand voice should feel clever, nostalgic, warm, music-loving, and not overly technical.
- Visual direction is retro / crate-digger / playful, with modern polish.

## Product / technology / operations

- Goodz commonly uses wooden collectibles with embedded NFC chips.
- Standard NFC products may use NTAG213; premium authenticated experiences may use NTAG424.
- Internal nickname `Unlocker` refers to NTAG424-enabled authenticated-tap products/flows.
- Core platform idea: a physical tap routes into a dynamic web destination / microsite where content can be updated and, in some cases, authenticated.
- Goodz has or has explored a custom CMS / SaaS layer for managing links, content, and analytics.
- The long-term product opportunity is not only the physical item but the software layer: creator tools, content swaps, analytics, microsites, and self-serve management.
- Manufacturing is based in China; operations are U.S.-based.
- Sustainability details that matter:
  - basswood collectibles
  - recycled PLA crates/accessories
  - VOC-free UV printing
  - recycled / biodegradable packaging when possible

## Commercial understanding

- D2C economics/material facts currently remembered:
  - Shopify storefront
  - Mixtape Goodz are a flagship / best-selling product
  - historical AOV around $37
  - repeat purchase rate around 25%
  - seasonality is strong, especially Q4 / gifting periods
- B2B facts currently remembered:
  - 13,000+ B2B units shipped by mid-2024 / in internal materials
  - clients / examples include They Might Be Giants, Concord / Original Jazz Classics, Sony / Britney Spears, Fania, Motorola, weddings, charity events, conferences
  - B2B often works as wholesale plus setup/design/customization work
- Goodz’s strongest use cases span:
  - artist and label drops
  - collector box/crate sets
  - weddings and celebrations
  - conference / event swag and activations
  - personalized gifts / mixtapes
  - gated fan experiences and exclusive content
- Licensed / credibility examples repeatedly referenced across internal materials:
  - Britney Spears `Oops!... I Did It Again` 25th anniversary release
  - Original Jazz Classics Crate Vol. 1 with Concord
  - Fania artist crates
  - They Might Be Giants crate work

## Strategic direction and tensions

- Goodz appears to have a real strategic fork between being:
  - a merch / collectibles company,
  - a custom B2B activation studio,
  - and a SaaS-enabled platform for creator-managed content and analytics.
- Internal materials suggest the most ambitious long-term upside is in SaaS/self-serve tools layered on top of the collectibles system.
- At the same time, the existing proof seems strongest in tangible product sales plus custom/B2B work, especially where exclusivity, gifting, or fandom are already strong.
- Goodz in 2025 is described in internal notes as largely dormant, so any current strategy work should distinguish between historical traction and present operating reality.
- The most promising near-term consumer concept Janet has identified so far is a pre-checkout creation flow (`Goodz Studio` / mixtape gift builder) that creates value before checkout instead of merely decorating Shopify checkout.

## Source docs worth trusting most

- Best-readable sources in `assets/` were:
  - `GOODZ_Overview.md`
  - `Goodz Gpt Knowledge Base.docx`
- Several PDFs in `assets/` were machine-readable only partially on this host. Their extracted text was noisy, so Janet should treat them as supporting signals unless reread with a better PDF parser / OCR setup.
