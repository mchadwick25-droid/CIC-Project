# Launch prompt — Website thread

Paste this into a fresh thread. This is the standing thread for **the public
website** — `cic-website/`, live right now at both `churchinconversation.org` and
`churchinconversation.com` — as distinct from the conversational app itself
(`cic-poc`, owned by the world-build/front-end/System Hub threads) and distinct from
System Hub's broader monitor-everything/dispatch role.

**Scope note, read this first:** this thread owns the public marketing site's actual
content, page structure, and domain-level housekeeping (canonical domain, redirects,
SSL, nav consistency) — the front door people reach before they ever talk to a
Representative. It does not touch `cic-poc` frontend/backend code, does not make final
brand-voice/copy calls (a separate thread owns that right now, see below), and does not
execute hosting/deployment infrastructure itself (that's System Hub's hands-on job,
this thread coordinates with it, doesn't replace it).

---

## ⚠ Read this before touching anything in the shared repo

A cross-session file-loss incident already happened today (2026-07-19): multiple
Claude sessions working the same shared repo working directory at once, and a git
operation in that shared directory wiped several uncommitted files (Dashboard, task
board, System Hub's own decision log, some `cic-poc/backend` files, and a large swath
of the Communication/Funding/Marketplace folders). Most of it has since been recovered
— first from published Artifact copies, then more completely from an orphan
safety-snapshot git commit (`09f1de5`) — see
`Ministry/Communication/CiC_File_Recovery_Report_2026-07-19.md` for the full account.

**As of this writing, a large amount of that recovered content is sitting on disk
UNCOMMITTED** (confirmed directly via `git status`, not assumed) — meaning it is
vulnerable to being lost again the exact same way if another concurrent git operation
touches this working directory before it's committed. **This thread should treat
getting that work safely committed as the single highest-value first action** — but
committing is Mark's call to authorize explicitly (standing rule, not unique to this
thread), so ask him directly rather than just doing it.

---

## What already governs this, read in this order

1. **`Ministry/Communication/Vision, Mission, Convictions, and Foundational
   Commitments V1.1.docx`** — same as every thread. *Trustworthy Transparency* and
   *Encounter Over Persuasion* apply to marketing copy exactly as much as to the app
   itself — a landing page that oversells or quietly smooths over the "doorway, not a
   home" framing fails the same standard a Representative would.
2. **`Ministry/Communication/CiC_Brand_Voice_Complete_Rethink_Thread_Launch_2026-07-19.md`**
   — a separate thread is *already in motion*, on Claude Fable 5, doing a ground-up
   rewrite of brand voice and this exact site's live copy. It explicitly overturns
   language the restored Messaging & Branding Kit had treated as settled (the "doorway,
   not a home" line — Mark's own words, quoted there: *"even a door not a home should be
   on the table, why not just a door"*). **This thread does not own final copy calls
   while that rethink is live** — route language questions to it, and don't treat any
   currently-live page copy as permanent.
3. **`Ministry/Operations/CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md`** (V1.2) —
   the dependency-ordered path to hosting + Prototype Testing 1, including the
   full-feature-set scope decision. This site's Pilot page is part of that funnel.
4. **`Ministry/Operations/CiC_System_Hub_Thread_Launch_2026-07-19.md`** — the adjacent
   thread. System Hub monitors the running app, verifies handoffs, and does hands-on
   engineering across the whole system, including standing up hosting. This thread is
   narrower on purpose: the website's own content and structure, not general system
   ops. When the two threads' work overlaps (e.g. deploying `cic-website` itself),
   coordinate rather than duplicate.

## Current state, verified live just now — don't assume, re-verify if time has passed

- **`cic-website/`** is committed and pushed to `main`. Live pages, checked directly:
  Home, About, Atlas, Tour, Support, Pilot — both domains resolve to the same site.
- **The live "Atlas" page is NOT the same thing as the rich World Orientation Map.**
  What's live now is a simple 10-era-marker + 5-live-world orientation page. The full
  interactive 178-entry scrolling census map (built, verified,
  `Ministry/Technology/World-Orientation-Map/`) is a materially richer artifact that
  currently only exists merged into `cic-poc`'s own `/world-map/` path, on branch
  `claude/world-map-merge-into-main` (prepared in an isolated worktree, not yet landed
  on `main` — see `CiC_World_Map_Integration_Assessment_V0_1.md`). **Open question this
  thread should carry: does the public site's Atlas page get upgraded to the rich map,
  stay a deliberately simpler teaser, or do both keep their own separate jobs?** Nobody
  has decided this yet — don't assume either answer.
- **The Pilot page collects interest via a `mailto:` form only** — no backend
  integration, no live link yet to the actual conversational app itself. No subdomain
  or path serving the real `cic-poc` app was found from the public site's nav.
- **Direct Anthropic API hosting is the decided path** for `cic-poc` (Bedrock dropped);
  host TBD (Render/Fly.io-class). A Supabase-backed accounts/sign-in layer was added to
  `cic-poc` this session, smoke-tested but not deployed — needs Mark's own Supabase/
  Render account creation to proceed (account creation is off-limits for Claude to do
  on his behalf, standing rule).

## What to produce

1. **A content audit of the live site against current brand-voice reality** — once the
   Brand Voice Rethink thread lands its rewrite, reconcile every page (`about.html`,
   `atlas.html`, `tour.html`, `support.html`, `pilot.html`, `index.html`) against it.
   Don't do this before that thread lands; don't let the site silently drift out of
   sync after it does either.
2. **A recommendation on the Atlas-page question above** — with the actual tradeoffs
   (bundle size, mobile behavior, maintenance of two artifacts vs. one, whether a
   public marketing page should carry the full census's honesty-marking apparatus or a
   lighter teaser), not just a preference.
3. **Domain/canonical housekeeping** — confirm which of `.org` / `.com` is canonical
   (if either), that both actually redirect/resolve correctly long-term, SSL status,
   and that the nav is consistent across both.
4. **A standing content-accuracy check** whenever a world's status changes (a new world
   goes live, a world's description changes in `world_manifest.py`) — the site's own
   "Live Today" world list needs to stay a true mirror of what's actually live in
   `cic-poc`, not hand-maintained prose that quietly drifts.

## Coordination boundary, stated plainly

This thread owns the public website's content and structure. It does not:
- Touch `cic-poc` frontend/backend code — that's System Hub and the build threads.
- Make final brand-voice or copy decisions unilaterally while the Brand Voice Rethink
  thread is live — surface language questions to it.
- Execute hosting/deployment infrastructure itself, or make the Tier A/B World-Map
  scope call alone — those are System Hub's hands-on job and Mark's decision,
  respectively; this thread tracks and surfaces them, doesn't decide them solo.
- **Propose any repository reorganization.** A prior thread did exactly this today in
  a different context and was correctly shut down hard by Mark. Nothing about "the
  site needs cleaning up" extends to touching the repo's actual structure — if
  something there seems to need reorganizing, name it plainly and ask, don't act.

## Logging

Log real decisions in `Ministry/Technology/CiC_Website_Decision_Log.md` — same
dated-entry discipline every other thread uses (what was decided, the reasoning
including the heart of it, the next action). Don't let a real decision live only in
this thread's own conversation history.
