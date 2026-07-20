# Launch Prompt — Fix the public website's stale world-deployment status (Alexandria)

Paste this into a fresh UX Design thread.

---

## Scope note

The public website's World Orientation Map / Atlas (`cic-website/world-map.html`
and `cic-website/world-atlas-list.html`) shows Alexandria (Representative Theon,
Catechetical Teacher) as **"Selected - Not Yet Built."** That was correct when
it was written, but it is stale now — Alexandria has since been fully built,
live-tested, and deployed. Your job is to bring the site's status displays
back in line with what is actually true, and only that. Do not touch
`cic-poc/` (the actual app backend/frontend) — that is already done and
committed. This is a website/presentation-layer fix.

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

As of 2026-07-20, `cic-poc/backend/app/world_manifest.py` has **5** deployed
`world_id` entries, confirmed live:

1. `post-apostolic-house-church` (Chloe)
2. `syriac-edessa-nisibis` (Mar Yausep)
3. `desert-monasticism` (Papnoute)
4. `hieronymian-ascetic-literary` (Albina)
5. `alexandria-catechetical` (Theon, Catechetical Teacher)

Alexandria's full build (World-Builds/Alexandria-Catechetical-School/),
deployed runtime data, manifest entry, and both frontend sync points landed
in commit `6dbcef1`. It has been live-tested with a real conversation, not
mocked.

**Verify this directly against the manifest / a live API call yourself
before changing anything** — don't take this document's word for the exact
count, in case something changes between this being written and you picking
it up. This project has a real, recurring history of status claims (in
either direction) not holding up on direct check: earlier this same session
the website wrongly claimed "FIVE MOVEMENTS ARE LIVE TODAY" including
Alexandria *before* it was actually built (flagged, not yet fixed at the
time); now the live site *undersells* the same world after it became real.
Both are the same underlying failure — status copy drifting from actual
deployment state — so fix the failure, not just this one instance of it if
you can do so cleanly within scope.

**One more thing to check, not to blindly copy from:** there's a superseded
scratch draft at
`Ministry/Technology/World-Orientation-Map/CiC_World_Map_V0_4_DRAFT.html`
that already marks Alexandria `"Built & Live."` It predates refinements the
real committed site later received (extra data fields, a simplified detail
panel, a renamed lane label), so don't merge it wholesale — but its
Alexandria status line happens to be correct now. Treat it as one data
point, not a source of truth.

## What to produce

1. Update Alexandria's status in `cic-website/world-map.html` and
   `cic-website/world-atlas-list.html` to correctly reflect that it is live,
   in whatever status vocabulary the site already uses for the other 4 live
   worlds (match the existing pattern, don't invent a new status category).
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
