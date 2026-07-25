# Launch Prompt — Simplify the homepage: the conversation program is the center, the Atlas is a supporting link

Paste this into a fresh thread for `cic-website/` work.

## Why this exists

Mark's own direction, given directly to System Hub today (2026-07-24): pause the
4-lane Representative Modes rollout, keep things simple for now — general voice
only, no new complex features — and move to **a simple landing page, with the
conversation program as the central piece and the Atlas as a supporting link.**

That's a real inversion of what the site currently does, not a copy tweak. Verify
this yourself before changing anything, but as of this writing:
**`cic-website/index.html` *is* the full interactive Atlas Story experience** —
a 178-movement census, search, era-by-era scroll, status chips, a wall-chart
link. "Launch a Conversation" exists only as one CTA nested inside that
experience's thesis section (`#launchcta`), not as the page's own point.

## Scope

Rework the homepage so a first-time visitor's primary, obvious action is
launching a conversation — not exploring a census. Concretely, at minimum:

1. **Decide where the current Atlas Story experience goes.** It's real,
   built, working content — don't delete it. Two live options already exist
   that could absorb it: `atlas.html` (the standalone orientation page) or
   `world-atlas.html` (the wall-chart / full research-table page). Pick one
   (or propose a third) and say why, rather than silently duplicating the
   178-movement content across three pages.
2. **Build the new simple homepage** — conversation-program-first. It needs,
   at minimum: the brand mark/wordmark, a short orienting sentence (pull from
   the brand kit, don't write fresh copy), a single primary CTA to launch a
   conversation (reuse the existing `LIVE_APP_URL` pattern from `index.html`/
   `pilot.html` — don't reinvent it), and one clearly secondary link to the
   Atlas for people who want to explore first. Simple means simple — this is
   not the place to add a new feature, a new visual system, or a new page
   type.
3. **New visual resources are available if they help, not required.** Six
   approved Representative portraits and six real, license-verified world
   photos landed today — see this thread's own 2026-07-24 Decision Log entry
   for exact paths, and check `world-media-sources.json`'s `attribution`
   field before displaying any of the CC BY-SA ones (five of six require a
   visible photo credit — this is a public site, don't drop it). A few
   portraits as a visual teaser could suit a simple homepage well; the full
   178-movement census does not belong here anymore.

## What governs

- Follow the CiC brand kit for any public-facing copy — check
  `CiC_Messaging_Branding_Kit_QuickRef_V0_1.md` before writing, not after.
  Protected lines stay verbatim; retired words stay retired.
- Log dated entries in this thread's own `Ministry/Features/Website/
  Decision-Log.md` as you go — what you found, what you decided, what you
  built. Same discipline as every other thread here.
- Do not publish/deploy the live site yourself. Bring the finished change
  back for an explicit go-ahead in chat before it goes live — this is
  Cloudflare Pages, auto-deploying on push to the connected branch, so
  pushing *is* publishing.

## Coordination boundary

Stay in the website/presentation lane — don't touch `cic-poc/` (the actual
app). If the simplification surfaces something that looks like an app-side
gap (e.g. the `LIVE_APP_URL` hand-off itself needs a fix), log it and hand it
back to System Hub rather than fixing it there yourself.

## Logging

`Ministry/Features/Website/Decision-Log.md`, dated entry, per standing
convention.
