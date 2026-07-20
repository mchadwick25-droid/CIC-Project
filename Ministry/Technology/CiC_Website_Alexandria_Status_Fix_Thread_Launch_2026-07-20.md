# Launch Prompt — Fix the public website's stale world-deployment status

Paste this into a fresh UX Design thread. **Held back deliberately** — do not
send until Imperial and Juridical Christianity ("Church and Empire") is
actually deployed into `cic-poc` (i.e. has a `world_id` entry in
`world_manifest.py`). Sending it now would mean touching this same status
copy twice in quick succession; batching both corrections into one pass
avoids that. Check `world_manifest.py` yourself before sending if you're not
sure it's landed yet.

## Scope note

The public website's World Orientation Map / Atlas (`cic-website/world-map.html`
and `cic-website/world-atlas-list.html`) has (at least) two stale world-status
entries by the time you're reading this:

1. **Alexandria** (Representative Theon, Catechetical Teacher) shows
   **"Selected - Not Yet Built."** That was correct when it was written, but
   is stale now — Alexandria has since been fully built, live-tested, and
   deployed (`cic-poc` commit `6dbcef1`).
2. **Imperial and Juridical Christianity** ("Church and Empire") almost
   certainly doesn't appear on the map/atlas at all yet, or appears at an
   earlier status — check current state directly. It should now be deployed
   (that's why this prompt was finally sent) and needs adding/correcting the
   same way Alexandria does.

Your job is to bring the site's status displays back in line with what is
actually true for **every** world, not just these two — check all of them
while you're in there rather than fixing only the two named above. Do not
touch `cic-poc/` (the actual app backend/frontend) — deployment itself is
already done and committed. This is a website/presentation-layer fix.

## What governs

- Follow the CiC brand kit for any public-facing copy you write or touch —
  check it before writing anything, not after. Protected lines stay verbatim;
  retired words stay retired.
- Website-thread work has its own decision log:
  `Ministry/Technology/CiC_Website_Decision_Log.md`. Log what you find and
  what you change there, same discipline as every other thread in this
  project — dated entries, nothing hidden, no self-graded "done."
- Do not publish/deploy the live site yourself. Publishing public content
  needs an explicit go-ahead in chat before it happens — bring your finished
  change back for that sign-off rather than pushing it live.

## Current-state grounding — verify this yourself, don't just trust this note

As of 2026-07-20 (before this prompt was sent), `cic-poc/backend/app/
world_manifest.py` had **5** deployed `world_id` entries, confirmed live:

1. `post-apostolic-house-church` (Chloe)
2. `syriac-edessa-nisibis` (Mar Yausep)
3. `desert-monasticism` (Papnoute)
4. `hieronymian-ascetic-literary` (Albina)
5. `alexandria-catechetical` (Theon, Catechetical Teacher)

Alexandria's full build (World-Builds/Alexandria-Catechetical-School/),
deployed runtime data, manifest entry, and both frontend sync points landed
in commit `6dbcef1`. It has been live-tested with a real conversation, not
mocked.

By the time you're reading this, a 6th should exist: **Imperial and
Juridical Christianity**, participant-facing card name **"Church and
Empire"** (both names decided directly by Mark, recorded in the System Hub
Decision Log's 2026-07-20 entry and `World-Builds/Imperial-Juridical-
Christianity/Open_Gaps_Tracking.md` item 12). Its Representative is
**Marius**, a deacon — decided directly by Mark in person, per that same
world's own build thread. Use whatever `world_id`/color/status values the
actual manifest entry has once it's deployed; don't guess them from this
note.

**Verify the current world count and every world's actual status directly
against the manifest / a live API call before changing anything** — don't
take this document's word for it, in case something changes between this
being written and you picking it up. This project has a real, recurring
history of status claims (in either direction) not holding up on direct
check: earlier this same session the website wrongly claimed "FIVE
MOVEMENTS ARE LIVE TODAY" including Alexandria *before* it was actually
built (flagged, not yet fixed at the time); then the live site *undersold*
Alexandria after it became real. Both are the same underlying failure —
status copy drifting from actual deployment state — so fix the failure
itself (every world's status genuinely matches the manifest), not just
these two named instances of it.

**One more thing to check, not to blindly copy from:** there's a superseded
scratch draft at
`Ministry/Technology/World-Orientation-Map/CiC_World_Map_V0_4_DRAFT.html`
that already marks Alexandria `"Built & Live."` It predates refinements the
real committed site later received (extra data fields, a simplified detail
panel, a renamed lane label), so don't merge it wholesale — but its
Alexandria status line happens to be correct now. Treat it as one data
point, not a source of truth.

## What to produce

1. Update every world's status in `cic-website/world-map.html` and
   `cic-website/world-atlas-list.html` to correctly match `world_manifest.py`
   — at minimum Alexandria (now live) and Church and Empire (newly deployed,
   likely absent or wrong entirely), but check all entries, not just those
   two, in whatever status vocabulary the site already uses (match the
   existing pattern, don't invent a new status category).
2. Check whether any other page (homepage counts, pilot pages, etc.) states
   a specific number of live worlds/movements and needs the same correction
   — if you find one, fix it the same way; if you don't, say so rather than
   assuming there isn't one.
3. Brief before/after note in the Website Decision Log: what was stale,
   what you verified it against, what you changed.

## Coordination boundary

Stay in the website/presentation lane. If you find something that looks
like it needs a backend or world-build fix (not just a status display), log
it and hand it back to System Hub rather than fixing it yourself — same
pattern as your prior status-report work. Don't publish the live site
without bringing the finished change back for an explicit go-ahead first.

## Logging

`Ministry/Technology/CiC_Website_Decision_Log.md`, dated entry, per standing
convention.
