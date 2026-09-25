# witt — Build log

No build log existed for this world before 2026-09-24 (`worlds/witt/build/` was empty). This file is
created by the Live-Surface-Cleanup program's witt PR to receive settled editorial history removed
from `records/witt/*.md` bodies and free-text fields, per CLAUDE.md's "Keep the live/canonical
surfaces clean" and `tools/check_live_commentary.py`'s REWRITE classification. It does not retroactively
document witt's original build (steps 1-9); that history, if wanted, would need reconstructing from
`git log` and is out of scope here.

## 2026-09-24 — Live-Surface-Cleanup, witt PR: settled corrections removed from record bodies

Each item below was previously narrated inline, in the record's own body or a free-text field, as a
dated/attributed correction. In every case the record's own current fields (front matter) already
state the corrected fact; the narrative explaining how it got there carried no information beyond
that, so it was removed by deletion rather than reworded. Listed here per this file's own role as the
destination for that removed history.

**`witt.figure.brussels-martyrs-john-and-henry` and `witt.story.brussels-martyrs`** (`confidence.divergence_note`):
both records once carried "the Registry's own technical correction fixed an earlier, unverified
'Augustinian friars' wording to what the text actually supports." The current, correct fact — "Augustinian"
does not occur anywhere in the vendored text in connection with the two martyrs — already stood as the
preceding sentence in both records and needed no rewording; the correction-narrative clause was deleted
whole.

**`witt.world_core.witt` (`witt.core.witt`)** (record body): three "CORRECTION:" paragraphs described,
at length, how `.thinness`/`.cautions`/`.thin_topics` reached their current existence-only treatment of
the 1525 peasants' tracts and the 1543 anti-Jewish treatise — a reversal caught at Doc_10 review (logged
there as OG-15), a follow-on `.thin_topics` correction, and a two-part overclaim fix (an uncreated
`contested_claim` record, since closed as `witt.contested.1543-treatise-later-effect`; a tertiary-sourced
clause dropped from a spoken field). All three describe now-closed, one-time corrections; the record's
own `.thinness`, `.cautions`, `.thin_topics`, and `confidence.divergence_note` fields already state the
corrected, current content directly (confirmed by reading them before removing the narrative). Removed
whole; no residual claim needed rewording.

**`witt.voice_craft.craft` (`witt.voice.craft`)** (record body): three narrative blocks removed —
(1) a "QUOTE / DOCTRINAL_WITNESS GAP" passage, explicitly self-labeled as "kept as the historical
record... not a description of this world's current store," describing a since-closed gap (zero quote/
doctrinal_witness records at B-7 authoring time; 7 and 14 respectively now) - the one still-relevant
fact inside it (the "tiles" saying at Worms is grounded only in `witt.story.worms-1521`, not a dedicated
quote/doctrinal_witness record of its own) is already durably tracked in
`worlds/witt/Open_Gaps_Tracking.md`, so nothing was re-added here; (2) and (3) two "CORRECTION:"
paragraphs describing how the `guard` field's 1525/1543 sentences reached their current wording (an
accidental over-license to voice the 1543 treatise's content, caught at Doc_10 review per OG-15; a
follow-on fix to an inaccurate "our record is silent" claim about 1525). The `guard` field itself
(confirmed by reading it) already states the corrected, current wording exactly. Removed whole.

**`witt.story.worms-1521`** (record body): "that document's own corrected handling of the 'tiles'/'Here
I stand' quotation question" — "corrected" removed as a single word (the sentence's substantive claim,
that this record follows Doc_09's own handling of the quotation question without re-litigating it, is
unaffected by dropping the implication that Doc_09's handling was itself a fix to something earlier).

All five files verified against `tools/check_live_commentary.py --surface records` after editing: none
of the removed passages remain flagged.

## Known gap, not addressed by this pass

This line-based scan does not reliably catch a multi-paragraph narrative block where only one line
independently matches a pattern (a ruling number, a date, "reviewer," "round N") while the surrounding
sentences carry the same process narrative without their own trigger word. All five instances above
were found this way — by re-reading the full paragraph around a line the tool *did* flag, not by the
tool itself. `records/witt/world_core/` and `records/witt/voice_craft/` both turned out to carry this
shape; other worlds' `world_core`/`voice_craft` records, and any other record type with a free-form
body, likely do too, and have not been checked. Flagged for whoever runs the next world's pass, and
worth a fleet-wide dedicated read of `world_core`/`voice_craft`/`world_front` bodies before the
program is considered complete, not assumed clean because a later PR's own targeted worklist came back
short.

---

## Source-form fragment re-author — 2026-09-25

`witt.quote.congregation-of-saints`: the larger sentence-completeness
parser (P3 Decision-Log Entry 29) flagged "As Paul says: one faith, one
baptism, one God and Father of all." as verbless. Under Mark's R44 ruling
of 2026-09-24 ("true ellipses get finished"), the quotation is finished
with the verb its structure implies: "As Paul says, there is one faith,
one baptism, one God and Father of all, and so on." The grader's first
objection also found real drift elsewhere in the same field, fixed here:
"congregation of saints" restored as "community of saints", "etc."
restored as "and so on", and "human traditions ... instituted by men"
restored as "human traditions -- that is, rites or ceremonies set up by
people", with "Nor" kept. Only `modern_rendering` changed; every other
field is byte-identical. Authored by Opus. Sonnet 4.6 reads translation
twice; Haiku 4.5 reads summary, recorded as a standing disagreement in
`Open_Gaps_Tracking.md` OG-35. P3 Decision-Log Entry 37 carries the
fleet-wide record of this pass.
