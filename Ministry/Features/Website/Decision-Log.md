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
