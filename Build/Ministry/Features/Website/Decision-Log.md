# Website Thread — Decision Log

Dated entries only. Each entry: what was decided (or what's still open), the reasoning
(including the heart of it, not just the operational logic), and the specific next
action. See `Ministry/Technology/CiC_Website_Thread_Launch_2026-07-19.md` for this
thread's scope, governing docs, and coordination boundary.

---

## 2026-07-19 — Thread opened

**Context:** the public site (`cic-website/`) went live at `churchinconversation.org`
and `churchinconversation.com` (System Hub build, date unconfirmed by this thread —
verify against System Hub's own log rather than assuming). Mark asked for "a clean web
thread" to own it going forward, distinct from System Hub's broader ops role.

**Verified live, same day, by direct browser check (not assumed):** Home, About,
Atlas, Tour, Support, Pilot pages, both domains resolving. Found and flagged in the
launch doc: the live "Atlas" page is a simple orientation page, not the same artifact
as the rich 178-entry interactive World Orientation Map (that's merged separately into
`cic-poc`, not the public site) — open question, not yet decided, for this thread to
carry forward.

**Next action:** await the Brand Voice Complete Rethink thread's output before doing
any content-audit pass; in the meantime, confirm with Mark whether the mass of
just-recovered-but-uncommitted work sitting in the shared repo (see the launch doc's
opening warning) has been committed yet.

---

## 2026-07-24 — New visual resources available for this site, cross-referenced from the In-App Icons & Graphics thread

**Not a decision, a resource handoff** — full reasoning for all of this lives in
`Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`; this entry exists so this
thread knows what's available without duplicating that record.

**Six approved Representative portraits** (painterly, historically-researched,
one per world — Albina, Theon, Chloe, Marius, Yausep, Papnoute):
`Ministry/Communication/Brand-Assets/Representative-Portraits/<world>/<Name>_Portrait.png`.
Already wired into `cic-poc`'s own World Selector tiles as a working reference for
scale/crop/placement, if this site wants to use the same images anywhere (About page,
world pages, etc.).

**Six real, license-verified architectural/artifact photos**, one per world's own
region and era (not stock imagery) — sourced from Wikimedia Commons, already used as
the same World Selector tiles' backgrounds:
`Ministry/Communication/Brand-Assets/World-Media/<world>/<file>.jpg`, with full
sourcing/story/license/attribution data in that folder's own
`world-media-sources.json` and README.

**⚠ License requirement, more consequential here than in-app:** five of the six
world photos are CC BY-SA (2.0–3.0) — legally requiring visible photographer credit
wherever they're displayed; only Hagia Irene (Church and Empire) is public domain.
Since this is the public marketing site, not a gated app screen, don't drop the
attribution line if any of these get used here — it's in the `attribution` field of
`world-media-sources.json` for each one, ready to copy in.

**Also available:** the consolidated brand guidelines PDF/MD
(`Ministry/Communication/Brand-Assets/CiC_Brand_Guidelines_Consolidated_V1_0.{md,pdf}`)
— voice, messaging, and visual identity in one place, useful if this thread ever does
a copy/visual audit pass.

**Status of the underlying feature work, for context:** all six portraits and all
six world photos are complete and locked as of this entry — not a partial/in-progress
set. Whether/how this site's own pages use any of them is this thread's own call, not
decided here.

---

## 2026-07-24 (later) — The homepage's static representative grid replaced with a real interactive carousel; live

**Found already built, not started from scratch:** by the time this landed, another
session had already executed the "simple landing page" rebuild (2026-07-25 header
comment in `index.html` — The Table primary, Atlas secondary) and had a static,
non-interactive six-portrait grid in place, using the portraits from the resource
handoff above (already copied to `assets/portraits/`). This entry upgrades that
static grid into the real thing, not a from-scratch build.

**What changed, in `index.html` only:** the static grid is now a chronological,
scrollable carousel — era-tinted backgrounds and era labels (from `data/world-
census.json`'s own `eras` array, the same file the Atlas reads, so this can never
drift from it the way two independently-maintained copies of this data have before).
Click any Representative → a lightweight panel with the same info their program tile
shows, then two links: **"Launch an Interview with [Name]"** (real, working, goes
straight into a free single-representative conversation, no picker shown) and "Read
more in the Atlas →" (real link to `atlas.html`).

**Business-model boundary made real, not just labeled:** Mark's direction —
interviews free, multi-representative tables a planned future paid tier — meant this
entry point specifically must never expose the multi-select picker. Required an
actual `cic-poc` app fix, not just this site's own button text: `WorldSelector.tsx`'s
`mode=interview` param was documented in that file's own code comment as part of the
URL contract but never actually read. Wired up (separate commit, `cic-poc` repo):
when exactly one world is requested with `mode=interview`, it now skips the picker
entirely and starts the conversation directly. Verified locally both ways — the
direct-interview path skips straight to a real conversation, and the existing
multi-world hand-off (no `mode=interview`) is unaffected, still lands on the picker
with pre-selection as before.

**Two real bugs caught in this pass, not shipped un-checked:**
- The census's own `id` for Church and Empire (`imperial-and-juridical-christianity`)
  doesn't match the live app's actual `world_id` (`imperial-juridical-christianity`)
  — would have 404'd that one entry's interview link. Corrected defensively in this
  file's own JS with a flagged fix, not at the source (that's this census file's own
  fix to make, separately).
- Dark-mode contrast: both the era-tinted cards and the info panel initially let text
  inherit the page's own dark-mode color while sitting on a background that stayed
  light, washing names and body text out to near-illegible. Fixed by giving both an
  explicit, theme-aware text color rather than relying on inheritance.

**Verified before shipping:** light mode, dark mode, phone width (390px), the
interview link's actual resolved URL (confirmed using the corrected id, not the
census's), and no regression on the existing multi-world hand-off path.

**Committed and pushed directly to `main`** (`3566031` this repo; the `cic-poc`
`mode=interview` fix is `83d058f`), per Mark's explicit go-ahead — live once
Cloudflare's auto-deploy completes. Deliberately scoped to only these two files;
a large amount of unrelated, uncommitted work was sitting in the shared repo at push
time (signed legal/entity documents, Gantt files, other threads' launch prompts) and
was explicitly left untouched, not swept in.

---

## 2026-08-06 — Deploy confirmation: `support.html` "Get Involved" rebuild is live

**Dispatch received** from the Funding Strategy thread: `support.html` rebuilt (door
imagery, real $2-$5/hr cost figures, four-part response including a new Academic
Review Fund, nav renamed "Support" → "Get Involved" sitewide, URL kept as
`support.html` deliberately since that link was already given to Stripe), committed
as `b0e5583` on `main`. Ask: confirm live status and complete the Cloudflare
connection if it wasn't already done.

**Verified, not assumed:** `b0e5583` confirmed on `origin/main`
(`git merge-base --is-ancestor`). Checked the actual production URL directly —
`churchinconversation.com/support.html` — title "Get Involved — Church in
Conversation," headline "Help Us Open the Door a Little Wider," the real cost
figures all present, no console errors. **Already live, confirmed — no deploy action
needed.**

**Context for why this worked cleanly:** earlier the same day, Mark found and fixed
a real Cloudflare Worker misconfiguration — "Builds for non-production branches" was
enabled with an unconditional `npx wrangler deploy` command, so every push to *any*
branch (including a very active, unrelated Atlas branch) was deploying straight to
production and repeatedly overwriting the live landing page with stale snapshots.
Disabled now; `main`'s own pushes are deploying correctly since. This dispatch's
clean, immediate live status is a direct result of that fix holding.

**Next action:** none for this dispatch. Reported back to the Funding Strategy
thread's session per its own completion-criteria convention.
