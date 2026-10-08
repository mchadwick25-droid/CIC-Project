# Gallic progress-vs-alteration scaffolding fix: adversarial review (2026-10-08)

Scope: a single review of branch `records/identity-scaffolding-gallic-progress` (commits e348b916 and daa3c22b), read as `git diff origin/main...HEAD`. Files: `records/gallic/term/gallic.term.progress-vs-alteration.md`, `engine/m1/cross_world.py`, `packages/gallic/2026-10-08T16-21-34Z/manifest.json`, `records/worlds/gallic.yaml`, and OG-30 in `Build/worlds/gallic/Open_Gaps_Tracking.md`. No record was edited and no model or API call was made. This is the first review file on this change.

## Mechanical checks, run on the branch

- `python -m engine.m10.cli regate gallic --base origin/main`: PASS. Every note it prints is a field that already failed at the base and is unchanged. Nothing is printed for `gallic.term.progress-vs-alteration`.
- `python -m engine.m10.cli records gallic`: PASS.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0. `records`, `engine` and `packages` have 0 hits; the 215 `worlds` hits are all PROTECTED lines in `Open_Gaps_Tracking.md`.
- `python -m engine.m9.cli check`: exit 0 ("every finding is waived, every waiver is live and current").
- `python -m engine.m2.site_cli staleness-check`: exit 0; `gallic` is `"stale": false`.
- `python -m engine.m1.cross_world`: no `spoken-scaffolding/gallic` finding, and no stale-waiver finding. `spoken_scaffolding.scaffolding_hits` over the gallic records returns `[]`.
- Pin: the sha256 of `packages/gallic/2026-10-08T16-21-34Z/manifest.json` is `9bee797cddb0466778455f6dba4ab6679c17998d039c65bff523089a2cafe386`. That is the value in `records/worlds/gallic.yaml` and in OG-30. The record copy inside the package is identical to the branch record, body included. Only `manifest.json` is tracked, which matches the earlier package (`packages/*/*/**` is ignored).

## Quotation

- Source: `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`, Chapter XXIII [54], lines 13801-13803: "But some one will say, perhaps, Shall there, then, be no progress in Christ’s Church? Certainly; all possible progress." The source uses a curly apostrophe (U+2019).
- New `plain_meaning` text: "Shall there, then, be no progress in Christ's Church?" (straight apostrophe). `engine.m1.quote_verbatim.verify_quote_text(..., source_is_xml=True)` verifies it, with classes `punctuation` and `whitespace`. The apostrophe is matched by the gate's `_APOS_VARIANTS` class, so straight and curly are treated as the same mark. The line break after "Christ’s" is the `whitespace` class.
- The old text, "Shall there be no progress in the Church?", fails the same matcher and does not occur in the file. The correction is right.
- `engine.m1.embedded_quotations` (report-only) flags the span at 9 words; the old span was flagged at 8. No change in status.
- The `informational` sense is untouched by the diff. It still quotes "Shall there, then, be no progress in Christ's Church? Certainly; all possible progress. ..." as before.

## Claims in `plain_meaning`

Old: "Vincent's answer to "Shall there be no progress in the Church?" All possible progress - but real progress, not alteration. The grown man has the same joints he had as a child."

New: "All possible progress, but real progress, not alteration. That is Vincent's answer to his own question, "Shall there, then, be no progress in Christ's Church?" The grown man has the same joints he had as a child."

All three claims are kept: the answer, that it is Vincent's answer to that question, and the joints image. The field now opens on the answer. One phrase is new: "his own question" (see Finding 2).

Readability (`engine.m7.turn_readability.score_turn`): new FK 4.5, FRE 84.6, no failures; old FK 4.0, FRE 84.5. Both sit below the grade-8 band floor, which is reported, not failed. This is not a regression.

## Verdict: REVISE

One substantial finding: a relation note this change wrote does not match the record's own `relations`. The fix is a single phrase, followed by the same rebuild and repin. Everything else checks out.

## Findings

### 1. SUBSTANTIAL: the new relation note leaves out `council-synod`

The frontmatter `relations` has five `associated-with` targets: `the-rule`, `tradition`, `the-fathers-elders`, `council-synod` and `doctor-expositor`. The body sentence this change wrote lists four of them and reads as the full list:

- Old (origin/main): "Related-Terms also names the rule, novelty vs. antiquity, tradition, and the Fathers / elders - cross-batch at authoring time, added as relations (typed associated-with except as stated here) ..."
- New: "The rule, tradition, the Fathers / elders and the doctor-expositor are associated-with."

The new sentence adds `doctor-expositor`, which is correct. It leaves out `council-synod`, which is in the frontmatter, and which the Doc_06 chunk's Related-Terms names ("council / synod"). A builder reading the body would get the relation set wrong.

Fix: "The rule, tradition, the Fathers / elders, council / synod and the doctor-expositor are associated-with." Then rebuild the package, repin `records/worlds/gallic.yaml`, and update the location and `manifest_hash` in OG-30's Gates paragraph.

### 2. NOT SUBSTANTIAL: "his own question" is a new characterisation

The source does not give the question in Vincent's own voice. He puts it in an objector's mouth: "But some one will say, perhaps, Shall there, then, be no progress ...". The record's `informational` sense already says "Vincent asks the objection himself", so this does not contradict the record. But the old field did not say whose question it was, and OG-30 says "none is added".

Suggested wording, best made in the same revision as Finding 1: "That is Vincent's answer to the objection he raises himself, "Shall there, then, be no progress in Christ's Church?"" This scores FK 5.5, FRE 78.7, with no failures and no scaffolding hit.

### 3. NOT SUBSTANTIAL: the Doc_03 7.5 pointer was dropped

- Old: "Built from Doc_06 entry 057 (`galliclex057_progress-vs-alteration.md`, Tier 2, tags AS TC DR CT; Doc_03 7.5)."
- New: "Source: Doc_06 entry 057 (`galliclex057_progress-vs-alteration.md`, Tier 2)."

"Doc_03 7.5" is a source pointer, not process narration. Sibling gallic term bodies keep theirs (for example `galliclex011_the-rule.md; Doc_03 7.2`). It can be recovered, because the Doc_06 chunk names it (line 77). The tags are also recoverable from the chunk, and AS, DR and CT are carried in the frontmatter. Optional fix: restore "; Doc_03 7.5" after "Tier 2".

### 4. NOT SUBSTANTIAL: OG-30's list of what was removed is imprecise

OG-30 says the body lost "Built from Doc_06 entry 057 ... Tier 2, tags AS TC DR CT; Doc_03 7.5", and then says the Doc_06 pointer and Tier were kept. Only the tags and the Doc_03 pointer were actually removed. OG-30 also does not name three other removals:

- "the chunk's own CT section draws that line";
- "per the chunk's Ecological Function";
- the parallel to the rule's own `presupposes` ("the same shape as the rule's presupposes toward the axis (011 ...)").

None of these drops a disclosure. The CT source stays in `divergence_note` ("carried from Doc_06 section 3"). The Round-2 footnote caveat (ch. 17 [44] quotes Newman on Origen, not Vincent) stays in `divergence_note` and `sources[]`. Fix: reword this OG-30 paragraph when it is next updated for Finding 1.

### 5. NOT SUBSTANTIAL: OG-30's other statements check out

These all match the diff:

- the old and new field text;
- the quotation, file and line;
- that the `informational` sense already quoted it correctly;
- "Nothing else quoted in the record was touched";
- the waiver removal;
- `scaffolding_hits` is empty;
- both gates pass;
- the pin and hash.

OG-29 stays OPEN in place (append-only), and OG-30 closes it by subject and date, as the rules require. OG-30's "Status: CLOSED" rests on this review, so it should be rechecked after the Finding 1 fix.

## For the recheck

Recheck only these four things:

1. The body's associated-with list against the frontmatter.
2. Any `plain_meaning` rewording, using the same verbatim matcher and `regate`.
3. The new package hash in `gallic.yaml` and OG-30.
4. OG-30's removal list.
