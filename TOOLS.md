# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Goodz / OpenClaw access

### SSH / tailnet

- Brooklyn OpenClaw box / Mac Mini hostname: `miniclaw`
- Tailscale IPv4: `100.115.33.48`
- Tailscale IPv6: `fd7a:115c:a1e0::bf01:21aa`
- Preferred remote SSH pattern when Mike is away:
  - `ssh mikerosenthal@100.115.33.48`

### Nerve access

- Nerve runs locally on the box at `127.0.0.1:3080`
- Preferred remote access pattern:
  - `ssh -L 3080:127.0.0.1:3080 mikerosenthal@100.115.33.48`
  - then open `http://127.0.0.1:3080` in the local browser
- No Tailscale Serve config yet

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
