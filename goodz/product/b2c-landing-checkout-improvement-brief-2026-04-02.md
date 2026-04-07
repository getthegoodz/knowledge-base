# Goodz B2C landing + checkout improvement brief

Date: 2026-04-02

## Purpose

Define the highest-leverage B2C funnel improvements needed before or alongside a D2C Meta ads relaunch.

This brief is focused specifically on the **Mixtape Goodz gifting flow**.

---

## Core diagnosis

The current issue is likely **not** that the product fundamentally fails.

The current issue is more likely that the purchase flow does not fully sell the emotional outcome.

What already works:
- product concept
- fulfillment
- Shopify checkout path
- post-purchase setup instructions
- core playlist-on-Goodz mechanic

What likely needs improvement:
- landing-page persuasion
- product visualization
- emotional clarity
- pre-purchase personalization excitement
- confidence that the gift will feel special

---

## Primary goal

Increase conversion rate on the Mixtape Goodz path by making the experience feel:
- more emotionally compelling
- more giftable
- more visually concrete
- easier to imagine and personalize

---

## Primary audience

### Main buyer
- someone buying a meaningful music gift for a partner, friend, or loved one

### Secondary audience
- self-buyer who wants a physical form of playlist/music ownership

For this brief, optimize primarily for the **gift buyer**.

---

## Core message the page must communicate

Within a few seconds, the user should understand:

1. this is a modern physical mixtape gift
2. they can personalize it with playlists/music they choose
3. it becomes a tangible, thoughtful music object
4. it is easy enough to create without technical friction

---

## Funnel recommendation

## Recommended shape

### Option A — best near-term path
A dedicated pre-checkout landing page that sells the concept and optionally collects personalization inputs before routing into Shopify.

Why this is strong:
- easier to optimize emotionally than a normal Shopify PDP
- easier to test messaging and layout
- can still hand off to existing checkout plumbing

### Option B — lighter-weight fallback
A significantly improved Shopify product page / landing template.

Why this may be necessary initially:
- faster to launch
- lower implementation complexity

Recommendation:
Start with the best possible **landing-first experience**, even if Shopify checkout remains the final transaction endpoint.

---

## Proposed page structure

## 1. Hero section

Goal:
Immediately frame the product as a meaningful gift.

Needs:
- strong headline
- visual of the product in hand / as a set / in a gifting context
- short subhead explaining what it is
- primary CTA

Possible headline directions:
- Build them a mixtape they can hold
- The mixtape is back — and better than ever
- A playlist gift for someone you love

Possible subhead direction:
Create a physical set of music cards loaded with playlists, albums, or songs that mean something — a modern mixtape gift for the streaming era.

CTA directions:
- Create your mixtape
- Start your gift
- Build a set

---

## 2. “How it works” section

Goal:
Make the product feel easy and intuitive.

Ideal three-step flow:
1. Choose your set
2. Pick playlists / albums / songs
3. Give a physical music gift they can tap and play

This section should be visual and concise.

---

## 3. Why it feels special

Goal:
Sell the emotional difference.

Potential bullets:
- more personal than a playlist link
- more meaningful than a normal gift card
- tangible, collectible, and displayable
- easy to personalize
- built for streaming-era music lovers

---

## 4. Personalization / creation teaser

Goal:
Make customization feel exciting before full checkout.

Show that the buyer can:
- choose playlists/albums
- add a message or note
- maybe upload/select art
- optionally connect Spotify to browse favorites faster

Important:
This section should create desire even if the full interactive builder is not yet live.

---

## 5. Social proof / examples

Goal:
Reduce hesitation and make use cases concrete.

Could include:
- sample gift scenarios
- testimonials if available
- examples like:
  - for your partner
  - for your best friend
  - for your road-trip playlists
  - for your shared songs

---

## 6. FAQ / confidence section

Goal:
Neutralize purchase concerns.

Likely key questions:
- Do I need an app?
- How do I add playlists?
- Can I use Spotify or Apple Music?
- Do they come preloaded?
- How long does shipping take?
- What happens when they tap it?

Important note:
Since Mike says the setup flow already worked well in practice, FAQ should reinforce confidence, not carry the entire selling job.

---

## 7. CTA / conversion section

Goal:
Make the next step obvious.

Preferred CTA flow:
- start creating your mixtape
- then enter product/customization flow
- then hand off to Shopify checkout

---

## Product enhancements worth prioritizing

## 1. Optional Spotify OAuth / import

High priority enhancement.

Use it to:
- import buyer playlists
- surface favorite albums
- reduce copy-paste friction
- make the flow feel modern and magical

Do **not** require it.

Fast path must still exist:
- paste a playlist/album link manually

---

## 2. Playlist/album selection during purchase

High priority.

This is one of the clearest ways to improve the experience.
It changes the customer story from:
- buy a blank object now, figure it out later

to:
- create a personalized music gift now

Even if the old first-tap system remains under the hood, the front-end purchase story should feel richer.

---

## 3. Better visual preview

The page should help users imagine:
- what the physical set looks like
- what the playlists/content choices represent
- what the recipient experience feels like

This does not need to be a fully dynamic 3D preview at first.
Even good mockups would help.

---

## 4. Gift-use-case segmentation

Consider entry points like:
- for your partner
- for your best friend
- for music lovers
- for anniversaries / birthdays / Valentine's Day

This could improve ad-to-page message match significantly.

---

## 5. Owned-experience improvements (important, but secondary for this brief)

Longer-term improvements for self-buyers / repeat purchase:
- richer tap page
- embedded media / art / notes
- collection/account layer
- social collection browsing

Important, but likely secondary to immediate conversion work.

---

## What to prototype first

## Prototype 1 — landing-first gift page

A page that includes:
- hero
- how it works
- emotional framing
- creation teaser
- CTA into purchase

This is the most important first prototype.

## Prototype 2 — lightweight playlist import step

Could be mocked as:
- paste Spotify/Apple Music link
- or connect Spotify
- choose what arrives on the Goodz

## Prototype 3 — improved product detail view

Show:
- crate contents
- gifting scenarios
- stronger visuals
- clearer post-purchase expectation

---

## Shopify implementation paths

## Path A — landing page outside Shopify, checkout inside Shopify

Pros:
- fastest way to build a compelling experience without being trapped by theme limitations
- easier testing and iteration

Cons:
- more glue logic needed between landing flow and cart/checkout

## Path B — upgrade Shopify theme/product flow directly

Pros:
- simpler commerce integration
- less system sprawl

Cons:
- may constrain the experience
- may make the page feel like a normal PDP instead of a richer guided gift flow

Recommendation:
Prototype the richer version first, then decide how much needs to live in Shopify vs alongside it.

---

## Success criteria

A successful B2C landing/checkout refresh should:
- increase purchase intent from cold traffic
- make the product feel easier to understand emotionally
- strengthen gift framing
- create more excitement around customization
- support the best-performing historical ad angles

---

## Immediate next deliverables from this brief

1. draft landing-page wireframe / section outline
2. prototype a more enticing sales page concept
3. define the minimum viable purchase/customization flow
4. align that flow with Shopify implementation reality
