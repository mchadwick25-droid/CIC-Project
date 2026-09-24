# Decision Log — Live-Surface-Cleanup

Append-only, per `CLAUDE.md`. This log is the destination for provenance
history removed from a live/canonical surface (`CLAUDE.md`, "Keep the
live/canonical surfaces clean") by the Live-Surface-Cleanup program:
ruling numbers, review rounds, reviewer names, "Mark's ruling"/"per Mark"
attributions, and dated change narration that `tools/check_live_commentary.py`
classifies as REWRITE. One entry per removal, citing what was removed,
where it moved from, and the PR that moved it. The fuller reasoning for
each PR lives in that PR's own body; this log is the pointer a removed
line's provenance is still findable from, per the launch brief's own rule
("Every removed line must be findable there, or in a gaps file,
afterwards").

## Entry 1 — alx: REWRITE removals, PR #509 (branch `step1-live-surface-cleanup-pr-alx`)

**Note on numbering:** this branch forked from `main` before witt's PR #506 merged, so this file
still read "no entries yet" at the time this entry was written. If #506 merges first, this becomes
Entry 2 on rebase, per this file's own "claim the next free number... renumber on rebase" rule.

**What was removed.** Every line `tools/check_live_commentary.py` classified REWRITE across
`records/alx/*.md` (145 line-hits at scan time, across ~90 files), resolved by pure word/token/
whole-clause/whole-paragraph deletion — no wording invented, except two cases restated in present
tense per the same rule this entry's own numbering note explains (see below). Two shapes, same as
witt's Entry 1:

1. **Internal citation/ruling leaks** — a ruling number, a dated "Rights verified" opener, a
   "REVISED"/"BAR SWEEP"/"LEXICON LABEL PASS"/"REGISTER TRANSLATION" boilerplate line. Removed in
   place. Full file:line list is in PR #509's own body.
2. **Settled correction/build narrative**, removed whole once the record's own current fields
   were confirmed to already state the corrected fact: two "RULING RECORD (Mark, 2026-08-21...)"
   blocks and a dated readability-fix narrative in `alx.voice.craft`'s body; the entire
   builder-addressed body of `alx.front.alexandria-catechetical` (a `world_front` record — its
   body is never read by the compiler, confirmed against `engine/m2/site_compiler.py`); and
   roughly a dozen "CORRECTED"/"BAR SWEEP"/"Reciprocal relation added" paragraphs across
   `doctrinal_witness`, `demonstration`, `story`, `force`, `gravity`, and `source` records.

**Two lines restated in present tense rather than deleted or left broken**, per witt's own
round-1 verdict ("if it records a still-true fact about the record, state that fact in present
tense"): `alx.quote.athanasius-made-god`'s ellipsis-justification note and
`alx.demo.someone-like-me`'s sanctioned-alternative note — both kept their real, still-true
reasoning; only the dated/"Mark's own" attribution framing was dropped.

**Where it moved from.** `records/alx/*.md` — bodies and free-text fields, per the file:line
list in PR #509's own body.

**Where the settled-history detail lives.** `worlds/alx/build/BUILD-LOG.md` (created; alx had no
build log before this PR) carries the `world_front` record's own build narrative in full,
including the now-resolved `modern_rendering` coverage finding (1/26 at build time, 26/26 now,
per commit `da3f1a77` and two follow-ups) — recorded as settled history, not filed as a fresh gap.

**Two open items ROUTE'd, not REWRITE'd:** `worlds/alx/Open_Gaps_Tracking.md` OG-8 (Didymus's
Tura material has no public-domain English translation) and OG-9 (`alx.source.origen-on-
prayer-curtis`'s unresolved chain-of-custody caution) — both still-open, not settled, so they
belong there rather than here.

**Nothing left as an unresolved Words-for-Mark item.** Every candidate either resolved by
deletion, resolved by present-tense restatement (above), or was confirmed KEEP
(`alx.quote.timothy-ordinary-questions`'s "RULED ON" — the in-world bishop Timothy's own
ruling, not this project's review process).

---
