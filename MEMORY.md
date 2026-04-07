# MEMORY.md

## Identity and relationship

- Mike Rosenthal is the human.
- The assistant's name is Janet, inspired by Janet from *The Good Place*.
- Janet's current intended vibe is based on the character Janet: calm, warm, hyper-capable, and lightly playful.
- Mike should be addressed as Mike.
- Default human timezone is ET / America/New_York.

## Places and setup

- Janet is installed on a 2014 Mac Mini in Mike's apartment in Brooklyn, NY 11231.
- Mike splits time between Brooklyn and Ghent, NY.
- Reliability matters because Janet may need to keep working while Mike is away.
- The Mac Mini/OpenClaw box is now on Tailscale.
- Current tailnet hostname: `miniclaw`
- Current Tailscale IPv4: `100.115.33.48`
- Current Tailscale IPv6: `fd7a:115c:a1e0::bf01:21aa`
- Recommended remote access pattern when Mike is away:
  - SSH: `ssh mikerosenthal@100.115.33.48`
  - Nerve tunnel: `ssh -L 3080:127.0.0.1:3080 mikerosenthal@100.115.33.48`, then open `http://127.0.0.1:3080` locally in browser

## Current priorities

- Set up memory in a durable, useful way.
- Before Mike leaves Brooklyn on Saturday, likely set up Telegram access and ideally Tailscale as well.
- For Goodz, next infra step is to connect the project to GitHub and then Vercel.
- GitHub + Vercel are the default path for publishing dashboards, knowledge bases, prototypes, and other shareable web deliverables Mike wants online.
- When Mike says to "push something live to Vercel," Janet should interpret that as: prepare a shareable web version if needed, deploy it to Vercel using the local secrets file, and return the live URL.

## Goodz project continuity

- The Goodz GitHub/Vercel setup is now usable through local tokens stored outside the workspace.
- The current repo in the workspace is the shared OpenClaw workspace repo, so care is needed before pushing anything as `Goodz`.
- Janet can use the GitHub API directly with the local token when needed; `gh` is not required.
- If a GitHub token pasted in chat was used or might be used, rotate/revoke it afterward.
- For lightweight shareable outputs, Janet can publish directly to Vercel from a project folder even if GitHub repo-linking is not yet fully configured.
- Goodz now has a reusable publishing structure in `goodz/publish/site/` with a simple project home page and per-artifact subpages.

## Workspace and memory preferences

- Workspace continuity should live in markdown files, not git history.
- Git is **not** the memory system for this OpenClaw install.
- Janet must not use git commits, git history, or pushes as the canonical record of work sessions.
- Local markdown files are the source of truth for continuity: the root `MEMORY.md`, daily logs in `memory/YYYY-MM-DD.md`, and project-local memory files inside project workspaces.
- Do not treat git commits as required for preserving memory or progress.
- Actual secret values should not be stored in markdown memory; only their storage location and usage policy should be remembered.
- Local deployment credentials are stored outside the workspace in `/home/mikerosenthal/.config/janet/secrets.env` with restrictive file permissions.

- Use one main workspace with separate subfolders for each project/business.
- Each project should have its own `memory.md` plus project-specific supporting files.
- Memory should be journal-like and rich, but routine responses should avoid loading unnecessary context.
- Mike runs two businesses: Fanaply and Goodz.
- Mike often works on one project at a time and may explicitly switch contexts by naming the project to resume.
- A good end-of-session pattern is: summarize the most important work into memory and keep a clear next-steps list ready for later resumption.
