# Goodz Publishing Workflow

This file is the operational source of truth for turning Goodz docs, dashboards, and prototypes into shareable web artifacts.

## Goal

When Mike says things like:
- "put this online"
- "publish this on Vercel"
- "make this shareable"
- "create a dashboard / knowledge base / prototype"

Janet should default to this workflow:
1. create or update the artifact in the `goodz/` workspace
2. convert it into a clean web-readable output if needed
3. publish it to Vercel using machine-local credentials from the local secrets file
4. return the live URL
5. save the URL and relevant continuity in project memory

## Credentials and access

Secrets are stored locally on the Mac Mini at:
- `/home/mikerosenthal/.config/janet/secrets.env`

Important:
- do not store secret values in markdown memory
- do not paste secret values into chat
- remember the path and purpose, not the token contents

Known credential types currently present there:
- `GITHUB_TOKEN`
- `VERCEL_TOKEN`
- Goodz-specific API credentials as needed for dashboards/integrations

## Current repo-backed publishing source

### Goodz knowledge base repo

GitHub repo:
- `https://github.com/getthegoodz/knowledge-base`

Current local working copy for the repo-backed publishing hub:
- `goodz/publish/site/`

Current status:
- dedicated repo created and initial site pushed to `main`
- this is now the source of truth for the Goodz publishing hub
- Vercel is now connected to this repo, so pushes to `main` should auto-trigger deploys

## Current deployed Goodz publishing projects

### 1) Goodz publishing hub
Local folder:
- `goodz/publish/site/`

Purpose:
- project home page / artifact index
- reusable base for published Goodz docs and ideas

Repo source of truth:
- `https://github.com/getthegoodz/knowledge-base`

Local structure:
- `goodz/publish/site/index.html`
- `goodz/publish/site/<artifact-slug>/index.html`
- `goodz/publish/site/vercel.json`
- `goodz/publish/site/.vercel/project.json`

Known Vercel project metadata:
- project name: `knowledge-base`
- project id: `prj_cCcmOPijYUStxJ5KDXRp5ow5RrWm`
- org id: `team_sebYhKfq1AHgmrp81DwUsybG`

Known live URLs:
- `https://knowledge-base-one-livid.vercel.app`
- `https://knowledge-base-getthegoodzs-projects.vercel.app`
- `https://knowledge-base-git-main-getthegoodzs-projects.vercel.app`

Linkage status:
- deployed on Vercel
- linked to GitHub repo `getthegoodz/knowledge-base`
- pushes to `main` should auto-trigger deploys
- old unlinked Vercel `site` project was deleted during cleanup

### 2) Overnight research artifact
Local folder:
- `goodz/publish/overnight-research/`

Purpose:
- original standalone published version of the overnight Goodz checkout memo

Current status:
- retained locally as an early one-off artifact source
- corresponding standalone Vercel project was deleted during cleanup because the preferred model is to publish through the main repo-backed hub instead
- current canonical published version should live under the main hub at `goodz/publish/site/overnight-research/`

## Recommended folder architecture

Use `goodz/` as the project root for all Goodz work.

Suggested structure:

- `goodz/memory.md` — durable Goodz continuity
- `goodz/PUBLISHING.md` — this publishing workflow
- `goodz/research/` — strategy docs, memos, market research
- `goodz/product/` — specs, PRDs, wireframes, UX flows
- `goodz/prototypes/` — interactive code prototypes
- `goodz/dashboards/` — analytics/reporting web outputs
- `goodz/publish/site/` — main shareable publishing hub
- `goodz/publish/site/<artifact-slug>/` — individual published artifacts
- `goodz/publish/archive/` — optional old standalone one-off deploy sources

## Publishing patterns

### Pattern A: add a page to the Goodz hub
Use this by default for:
- brainstorm docs
- knowledge base entries
- strategy memos
- research writeups
- simple dashboards

Flow:
1. create/update source doc in `goodz/`
2. render or handcraft a clean HTML page in `goodz/publish/site/<artifact-slug>/index.html`
3. update `goodz/publish/site/index.html` to link to it if appropriate
4. deploy from `goodz/publish/site/`
5. save the resulting URL in `goodz/memory.md`

### Pattern B: standalone Vercel project
Use when:
- the artifact should have its own deployment lifecycle
- it has its own codebase or runtime behavior
- it may later become a larger app

Examples:
- a dashboard with its own assets/scripts
- a prototype app
- a focused standalone share link

## GitHub vs direct Vercel deploy

Default preference:
- GitHub is the source of truth for durable Goodz web artifacts
- Vercel should ideally be connected to the relevant repo so pushes trigger automatic rebuilds/deploys

Acceptable shortcut:
- direct Vercel deploy from a local folder for lightweight static artifacts, especially when speed matters more than repo-link hygiene
- use this when the GitHub-linked path is not yet wired or when a one-off share link is enough

Interpretation rule:
- "push this live to Vercel" should bias toward a GitHub-backed flow when practical
- if the artifact is simple and speed matters, Janet may still deploy directly to Vercel first and then normalize into a repo-backed workflow afterward

## Operational checklist for Janet

Before publishing:
- decide whether this is a hub page or a standalone project
- ensure content lives in the correct Goodz subfolder
- avoid leaking secrets into code or output
- make sure the artifact is readable by non-technical viewers

After publishing:
- return the live URL to Mike
- update `goodz/memory.md`
- update `memory/YYYY-MM-DD.md` if the publish is important to broader continuity
- keep the source materials in place so the artifact can be revised later

## Current status

As of 2026-03-30 / 2026-03-30+:
- Goodz publishing on Vercel is real and working
- machine-local credentials exist
- a reusable Goodz publishing hub exists
- the next improvement is tightening folder structure and making future publishes consistent and low-friction
- Mike’s stated preference is to have GitHub pushes auto-trigger updated Vercel builds whenever possible
