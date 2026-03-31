# Goodz Memory

Project-specific durable memory for Goodz.

## What belongs here

- important business context
- ongoing priorities
- decisions and rationale
- recurring people / partners / constraints
- links to more detailed docs in this folder

## Business understanding

- Goodz is a physical-digital collectibles company co-founded by Mike Rosenthal and Chris Cerrito in late 2023.
- The company emerged while Fanaply was in financial trouble and was conceived as a modern, sustainable, tech-enabled alternative to outdated physical media.
- Core concept: physical collectible objects with embedded NFC chips that unlock digital experiences when tapped with a smartphone.
- The product is meant to bridge physical ownership and digital content, especially around music, fandom, gifting, and special moments.

### Main business lines

- **D2C / Shopify:** direct-to-consumer sales of mixtapes, artist releases, crates, and gifts.
- **B2B / custom:** wholesale or project-based orders for artists, labels, weddings, conferences, private events, agencies, and brands.
- **SaaS/platform (in development / strategic direction):** tools for creators/partners to manage linked content, microsites, analytics, and user experiences themselves.

### Core product lines

- **Mixtape Goodz**
  - customizable playlist/music-sharing product
  - positioned as the best-selling product in the internal knowledge base
  - strong fit for gifting, self-expression, and personal sharing
- **Custom Goodz**
  - tailored for indie artists, DJs, events, weddings, conferences, and brand activations
  - links can point to playlists, landing pages, audio, video, merch, tickets, photos, or other digital content
  - content can be updated over time
- **Artist Goodz / album Goodz / crates**
  - premium or licensed artist/label releases
  - often serialized, collectible, and packaged as sets/crates
  - examples include jazz crate releases and larger artist drops
- **Authenticator Goodz / Unlockers**
  - use NTAG424 chips for secure/authenticated access to gated content, fan communities, or premium experiences

### Technology / platform understanding

- Standard Goodz may use NTAG213 chips; higher-security Goodz may use NTAG424.
- Goodz relies on a dynamic linking / landing-page system so a tap routes to a web destination that can be updated and tracked.
- Goodz has or intends to have a custom CMS / SaaS-style backend for managing links, content, analytics, and microsites.
- The digital destination experience is an important part of the product, not just an afterthought.

### Brand / positioning

- Brand tone should be clever, nostalgic, warm, and music-loving.
- Avoid overly technical language in customer-facing positioning.
- Goodz should be framed as a modern keepsake / collectible / key to an experience, not just an NFC gadget.
- Core emotional framing: physical connection to music, fandom, memory, gifting, and moments that matter.
- Visual identity direction: retro-influenced, bold, playful, crate-digger energy with modern polish.

### Sustainability

- Basswood is the core material for the collectible pieces.
- Recycled PLA is used for crates.
- UV printing process is VOC-free and part of the sustainability story.
- Packaging should use recycled / biodegradable materials where possible.

### Commercial signals / traction

- Internal materials claim 13,000+ B2B units sold.
- Internal materials claim ~25% Shopify repeat purchase rate.
- Internal materials cite roughly $37 AOV on the D2C side.
- Goodz has worked with credible music/brand partners including Warner, Sony, Concord, Fania, and at least one Britney Spears anniversary release.
- Goodz has also done weddings, conferences, Motorola event work, and charity activations.
- Mike clarified that the last 12 months had almost no Goodz revenue because the business was put on pause while focus went to Fanaply.
- Historically, the two real revenue drivers were:
  - D2C Shopify/store sales driven almost entirely by Meta Ads
  - B2B custom orders for record labels and other clients (including weddings and luxury real estate)
- Historically, D2C performance could be strong seasonally, with ROAS around 4–5x during certain holiday periods.
- Occasional legacy B2B orders from Sony Music still happen, but only a few in the last year.

### Strategic opportunities repeatedly suggested by internal materials

- Expand licensing / catalog deals for artist and label releases.
- Build self-serve creator tools and a dashboard for content swaps, analytics, and fan engagement.
- Improve gifting / holiday positioning, especially around Q4.
- Grow partnerships with festivals, agencies, labels, and brands.
- Develop more personalization, collectible accessories, and display/storage options.
- Support cross-platform playlist compatibility and easier customization flows.
- Mike believes a strong near-term opportunity is building a real B2B/custom checkout/configuration flow so buyers can self-serve instead of requiring hand-to-hand sales calls for every order.
- If that flow existed, Goodz could potentially run more scalable paid acquisition against B2B/custom segments such as wedding planners or other business buyers.
- Another promising segment Mike identified is indie bands using Goodz as tour merch.

### Business reality / timeline notes

- Goodz soft-launched in late 2023.
- Early 2024 included B2B shipments and growing D2C activity.
- Spring/mid-2024 included jazz crate / licensed work / Britney release / custom projects.
- Internal materials say the company began pivoting toward self-serve SaaS-enabled tools in fall 2024.
- Internal materials also say Goodz was largely dormant in 2025.
- This dormancy note is important context when thinking about what is current strategy versus historical plan.

### Important product/use-case framing

Goodz is simultaneously:
- a gift object
- a fandom collectible
- a custom event keepsake
- a branded activation object
- a gateway to digital content and potentially to authenticated fan/community experiences

That multi-use-case flexibility is a strength, but it can also create positioning ambiguity if the shopping and product flows do not clarify which problem is being solved for which buyer.

### Mike's current strategic read

- The business was paused, so recent revenue does not reflect demand ceilings as much as lack of focus.
- D2C + Meta ads is a historically proven engine worth revisiting, especially around holiday gifting windows.
- B2B/custom has strong order economics but has historically depended too much on labor-intensive founder selling.
- A self-serve B2B/custom web flow could be a major unlock if it reduces sales friction and makes paid acquisition feasible.
- A more sophisticated sales website is likely required for that path.
- Indie bands / tour merch is another plausible self-serve B2B-ish wedge worth exploring.
- Next high-value missing context to ask Mike: among the historical D2C products, which sold best, had the best margins, worked best in ads, and were easiest for customers to understand.

### Terminology to remember

- "Goodz" is the brand/product name and should stay plural in tone.
- "Crate" = themed set of multiple Goodz.
- "Microsite" = the mobile-friendly destination or experience the Goodz opens.
- "Unlocker" = internal nickname for NTAG424-enabled/authenticated Goodz.

## Operating system

- Goodz now has a defined operating model in `OPERATING_SYSTEM.md`.
- Janet is the main Goodz operator/coordinator rather than a swarm of loosely directed agents.
- The active Goodz work lanes are:
  - revenue / growth
  - product / funnel
  - build / prototype
  - research / intelligence
- The system should bias toward practical revenue-producing work over generic business theater.
- A key part of the operating model is regularly asking Mike compact, high-value onboarding questions so strategy stays grounded in the actual business.
- Current onboarding prompts live in `ONBOARDING_QUESTIONS.md`.

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

## Additional durable facts confirmed from the PDF pass (2026-03-31)

- The local PDFs in `goodz/assets/` are machine-readable enough to extract with a Node-based parser; full OCR was not required for these specific files.
- Investor deck (September 2024) confirms a more investor-facing snapshot of the business at that time:
  - five music-industry pilot programs launched
  - 10,000 Goodz sold B2B
  - patent filed
  - 21,000 website visitors
  - MVP of the user SaaS platform built
  - three product lines launched
  - 300+ D2C orders with ~$37 average order value
- The same investor deck frames the business model as a mix of physical-product margin plus a future SaaS layer, with an illustrative SaaS price point of `$5/month`.
- September 2024 fundraising plan in the deck:
  - raise target: `$500,000`
  - structure: SAFE
  - discount: `20%`
  - valuation cap: `$3M post-money`
  - estimated runway target: `12 months`
  - intended use of funds: `50% tech`, `30% BD`, `20% marketing`
- Named pilot / partner examples confirmed across the readable PDFs include:
  - They Might Be Giants
  - Concord Music / Original Jazz Classics (Miles Davis, John Coltrane, Charlie Parker)
  - Warner Music Group examples including Osamason and Bristol Maroney
  - festivals including Cascade Equinox, Elements, and Hulaween
- October 2024 music deck confirms a concrete They Might Be Giants case study claim: a limited-edition six-album crate distributed via the band’s merch company with `6,000+` Goodz sold wholesale.
- October 2024 music deck also confirms Osamason as an early-content / early-access use case and Concord as a legacy-catalog licensing use case.
- January 2024 Bandcamp proposal is useful evidence of how Goodz was being positioned strategically:
  - as the physical manifestation of digital track/album codes
  - as a dashboard-integrated artist ordering flow with low minimums and fast delivery
  - as a possible editorial / subscription product for Bandcamp playlists and franchises
  - as an authenticator key for gated content or forums
- Product spec facts now confirmed directly from the March 2024 spec sheet and July 2025 one-sheet:
  - standard card size: `2.56" x 2.56"`
  - rounded corner radius: about `0.25"`
  - card thickness: about `0.125"` / `0.12"`
  - cards link to one URL that can be updated later
  - crates typically hold `6-12` standard cards
  - cards use a `300 DPI` UV printed finish

## Source docs worth trusting most

- Best-readable sources in `assets/` now include:
  - `GOODZ_Overview.md`
  - `Goodz Gpt Knowledge Base.docx`
  - the extracted text files in `goodz/assets/extracted-text/` generated from the five PDFs
- A reusable local PDF extraction tool now lives at `tools/pdf-text-extractor/`.
- These five PDFs did **not** require OCR once the better parser was installed, but Janet should still be conservative with fine-grained claims from formatted decks and prefer facts that appear cleanly in extracted text.
