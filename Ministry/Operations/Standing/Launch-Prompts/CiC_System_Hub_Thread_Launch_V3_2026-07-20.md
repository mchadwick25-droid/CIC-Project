# Launch prompt — System Hub V3: verified state, after a night where work felt lost

Paste this into a fresh thread to succeed the current System Hub thread. Mark's own words
opening this handoff, kept verbatim rather than smoothed over: *"you are broken have cost me
hours of work loosing filing systems and docuements, a couple hours ago i had an almost ready
full version of the program ready and now between you and cic ux design we have lost most
everything."* **This thread's first job is to hold that seriously and verify plainly — not to
explain it away, and not to panic-recover from it either.**

---

## Read this section first. Verify every line yourself before doing anything else.

Everything below was checked directly, not assumed, at handoff time (commit `4af106e`,
2026-07-20 20:39 MDT). Re-run the checks yourself before inheriting any of it as settled fact.

- **Git history is completely intact.** `git log --oneline` on `main` shows an unbroken,
  linear commit history back through the entire session. `git fetch` + comparing `origin/main`
  to local `HEAD` shows **zero divergence** — `git rev-parse HEAD` and `git rev-parse
  origin/main` return the identical SHA (`4af106e...`). Nothing has been force-pushed,
  rebased, squashed, or rewritten. Every commit made tonight is still there, in order, with
  its full message. **Confirm this yourself first** — `git log --oneline -30` and `git status`
  — before treating anything as missing.
- **A real, concrete, non-speculative cause was found for tonight's confusion, not just a
  reassurance.** Attempting to restart the website's local preview server returned: *"Port
  5176 is in use by another chat's dev server 'cic-website'."* That means a genuinely separate,
  concurrent Claude Code session was serving `cic-website` on the exact same port at the same
  time tonight. **One honest caveat, not overclaimed**: it's possible (not confirmed either
  way) that this was actually this same session's own earlier server process, orphaned after
  an unrelated Browser-pane tool reset, and simply mis-attributed by the tool's own tracking —
  the port-ownership check doesn't fully rule that out. What IS independently confirmed,
  either way: the content being served on that port at handoff time matched this session's
  latest committed `index.html` exactly (checked via direct `curl`, not assumed).
- **This is not a new hazard.** This exact class of problem — two processes answering the
  same port, producing unpredictable, hard-to-diagnose behavior — was independently confirmed
  **twice already today**, both on port 8000 (a content-isolation investigation earlier in the
  day, and separately during the mobile-popover build thread). It's explicitly named as a
  standing, known risk in this project's own prior System Hub V2 launch doc: *"Multiple
  sessions may be running concurrently against this same repo. Today's file-loss incident
  happened during exactly that condition."* This is the third confirmed instance of the same
  underlying class of hazard on this machine today — treat it as a real, recurring
  environmental risk going forward, not a one-off.

## Do not do this, given how this thread came to exist

**Do not treat anything as "lost," "broken," or requiring recovery/restore/rollback until you
have personally run `git log`, `git fetch`, and confirmed local `HEAD` against `origin/main`
yourself.** A prior System Hub thread in this exact project already made the mirror-image
mistake once — it declared a real, fully recoverable body of work "permanently lost" because
it only checked its own published Artifacts instead of checking git first (see the
2026-07-19 file-recovery incident in the decision log below). Don't repeat that mistake in
either direction: don't assume things are fine without checking, and don't assume things are
lost without checking either. Check first, always, before either reassuring or alarming Mark.

**Before starting any local dev server, check what's already listening** (`netstat` for the
port, or the preview tool's own server list) rather than assuming a clean environment. If a
server start reports another session already owns the port, do not force past it or kill it —
that may be someone else's live work.

## Current state, verified at handoff — what's real right now

**The conversation program (`cic-poc/`) is deployable as one service, and the deploy path was
verified for real, not just written.** `cic-poc/Dockerfile` (moved here from
`cic-poc/backend/Dockerfile` so it can see both `backend/` and `frontend/` in one multi-stage
build) was found to have a real, deploy-blocking gap earlier tonight — it never actually built
or copied the frontend, so a fresh deploy would have silently served an API with no UI at all.
Fixed: a Node stage builds the frontend, the Python stage copies the built `dist/` in at the
exact path `app/main.py` already resolves. Verified directly: fresh `npm ci` + `npm run build`
both succeed; the actual combined server was run locally against the fresh build and confirmed
via `curl` that `/`, a real JS asset, an unmatched SPA path, `/health`, and `/api/worlds` all
serve correctly from one process.

**The website (`cic-website/`) front page is now the Atlas itself.** Mark's direction: the
front page should be the conversation + the atlas + minimal messaging, nothing else — no pilot
framing, no tour framing. `index.html` now contains the same proven, working Atlas Story-view
component that used to live only at `atlas.html` (vertical era-by-era scroll, sticky search,
status filters, honest redirects — confirmed genuinely vertical-scrolling, not the old
horizontal wall-chart model, which is `world-map.html`, already demoted to an opt-in link). A
real bug was found and fixed in the same pass: the Atlas's own "launch a conversation"
mechanism (the "Interview"/"Sit down at the Table" buttons) was a **permanent stub** that just
showed a fake "this is a design sketch, it ends here" modal, even once real hosting exists.
Both are now wired to a `LIVE_APP_URL` pattern (same one used in `pilot.html`): empty and
honest ("hosting is still being finished") on the real public domain, but auto-detects
`localhost` and points at the local demo server so local testing actually works end-to-end.

**The new positive-only messaging is live on the core pages.** Every remaining "honest/
honestly" instance was replaced per the Kit's own 2026-07-17 retirement rule; the flagged
negative/contrast-framed lines from the messaging audit were reframed; "We are committed to a
documented witness" (Mark's own final wording, replacing the retired "It will never try to
convert you") has its first live home in About's Safety section; "Join the pilot" is retired
as CTA language everywhere it mattered, replaced with "Come and join us at the Table" /
"Launch a Conversation."

**What's still genuinely gated on Mark, unchanged all evening:** a Render (or Railway/Fly.io)
account, `ANTHROPIC_API_KEY`, `CORS_ORIGINS`, and pointing the real domain at it. Nothing
about tonight's confusion changes this — it's still the one step only Mark can do. The
timeline Mark gave was "the next day or two," not necessarily tonight.

**What is honestly not built yet, if "all features" comes up:** Representative Modes/role
selection, Guided Questions, the S0 three-door threshold, and the Hosted Tour (deliberately
deferred by Mark until Friday 2026-07-24 — do not build or prioritize before then).

## Full commit range, this session (oldest → newest, all pushed, all on `origin/main`)

`fc66ced` (hold hosting behind UX design's pass) through `4af106e` (local-demo launch fix) —
run `git log --oneline fc66ced..4af106e` for the complete, exact list rather than trusting a
paraphrase. Every commit has a full message explaining what changed and why; read the ones
relevant to whatever you're picking up rather than re-deriving context from scratch.

## Standing references

- `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` — this session's full dated
  record, append-only convention, newest entries at the top.
- `Ministry/Operations/Standing/CiC_Task_Board_2026.md` — cross-thread status, kept current
  through tonight.
- `Ministry/Operations/Audits/CiC_Website_Messaging_Structure_Plan_2026-07-20.md` — the
  messaging audit and proposed structure, partially applied tonight; the deeper section-by-
  section pass is still Mark's own next step, by his own direction.
- `Ministry/Communication/CiC_Messaging_Branding_Kit_V0_1_DRAFT.md` and its own decision log —
  governs all public-facing language; check before writing new public copy.

## The one thing to do before anything else, once this thread starts

Say plainly, in the first message: *"Checked git — here's exactly what's on `main`, what's
pushed, and what isn't."* Ground Mark in verified fact before doing anything else, even before
apologizing or explaining. He needs to see the actual state before anything either of you says
about it will land.
