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

## Entry 1 — witt: REWRITE removals, PR #506 (branch `step1-live-surface-cleanup-pr-witt`)

**What was removed.** Every line `tools/check_live_commentary.py` classified REWRITE across `records/witt/*.md` (252 line-hits, roughly 150 distinct files), resolved by pure word/token/sentence deletion — no wording invented. Two shapes:

1. **Internal citation/ruling leaks** (the large majority): a "Source Registry R##" row citation, a bare `R\d\d` ruling number, or (inside a record type's own SPOKEN field per `engine/m1/spoken_fields.py`) a `Doc_0N`/`§N` citation or a formation_confidence-taxonomy word used as a spoken predicate ("is Documented"). Removed in place; the surrounding sentence's substantive claim is unchanged. Full file:line list is in PR #506's own body, not duplicated here.
2. **Settled correction narrative**, removed whole rather than token-trimmed, once re-reading confirmed the record's own current fields already state the corrected fact and the narrative explaining how it got there carried nothing else:
   - `witt.figure.brussels-martyrs-john-and-henry`, `witt.story.brussels-martyrs` (`confidence.divergence_note`): "the Registry's own technical correction fixed an earlier, unverified 'Augustinian friars' wording to what the text actually supports."
   - `witt.core.witt` (world_core body): three "CORRECTION:" paragraphs on how `.thinness`/`.cautions`/`.thin_topics` reached their current 1525/1543 treatment (the Doc_10-review reversal logged there as OG-15; a follow-on `.thin_topics` fix; a two-part overclaim fix).
   - `witt.voice.craft` (voice_craft body): a "QUOTE / DOCTRINAL_WITNESS GAP" passage (self-labeled "kept as the historical record... not a description of this world's current store") and two "CORRECTION:" paragraphs on the `guard` field's 1525/1543 wording.

**Where it moved from.** `records/witt/*.md` — bodies and front-matter free-text fields, per the file:line list in PR #506's own body.

**Where the settled-history detail lives.** `worlds/witt/build/BUILD-LOG.md` (created; witt had no build log before this PR) carries the fuller account of the five whole-paragraph removals in item 2, including what each record's own current fields say and how that was confirmed before deleting the narrative. This entry is the pointer; that file has the reasoning.

**One open item ROUTE'd, not REWRITE'd.** `witt.source.marburg-articles`'s inline "Doc_01 open item 1 / §7" note moved to `worlds/witt/Open_Gaps_Tracking.md` OG-32 (the Marburg Articles remain unvendored) — a still-open acquisition gap, not settled history, so it belongs there rather than here.

**Eighteen items left unedited**, flagged Words-for-Mark in PR #506's own body: pure deletion would break grammar or destroy real content (most commonly a formation_confidence word fused as a sentence's own verb — "is Documented", "is Contested" — with no way to remove it without either inventing a replacement or losing the clause's only content). Awaiting Mark's wording, not resolved here.

**Known gap, not addressed by this PR.** `tools/check_live_commentary.py` is a line-based scan and does not reliably catch a multi-paragraph narrative block where only one line independently matches a pattern while the surrounding sentences carry the same process narrative without their own trigger word — found in this PR only by re-reading the paragraph around an already-flagged line, not by the tool. Both `witt.core.witt` (world_core) and `witt.voice.craft` (voice_craft) turned out to carry this shape. Other worlds' `world_core`/`voice_craft`/`world_front` records likely do too and have not been checked here — flagged in `worlds/witt/build/BUILD-LOG.md` and PR #506's own body for whoever runs the next world's pass.

---
