# ijc — identity-and-scaffolding record pass, adversarial review round 1 (2026-10-08)

Branch `records/identity-scaffolding-ijc` (PR #827), six commits ahead of origin/main (4151a236 … 3ee88125). Diff checked: `git diff origin/main...HEAD -- records/ijc engine Build/worlds/ijc records/worlds`. Reviewer: Opus 5.5. No model or API spend. No records edited.

**Verdict: REVISE.**

## Method

- Compared the old text (`git show origin/main:<path>`) with the new, sentence by sentence, for all 7 changed witnesses. Only the `text` field and the markdown body changed in each file; no other frontmatter field moved.
- Read each cell's sealed probe (`canon/sealed_probes/plaintext/`) for the kind of question the opener must answer: F4-E (evidence connecting rituals to the earliest followers), F4-T ("born again"), F2-E (how much would survive scrutiny), F1-P (room for someone who struggled to believe), F6-P, C-E (what sources connected you to Jesus).
- Scanned every spoken field (`text`, `plain_meaning`, `quick_meaning`, `tellable_as`, `modern_contrast`, `absent_detail`, `prior_sense`, `retelling`, `modern_rendering`, nested included) of every witness, term and story under `records/ijc/` for question marks, "you"/"your", and answer-talk. Read the hits in context.
- Read every body diff against the old body for dropped caveats and pointers.
- Quotes: no sentence inside quotation marks was edited. The only quote-marked strings in touched sentences are 'Ancient custom' (a label, now capitalised at sentence start; not a source quotation — the quote record is `ijc.quote.let-the-ancient-customs-prevail`, untouched) and 'born again' (the participant's phrase). Nothing to re-verify against `cic/texts/`.
- Pin: `sha256sum packages/ijc/2026-10-08T05-36-20Z/manifest.json` = `a17f2408…a48422`, matching `records/worlds/ijc.yaml` `manifest_hash`; `location` matches. The manifest's `records_commit` is 944ba803, which is in the branch history.
- `engine/m1/cross_world.py`: the `spoken-scaffolding/ijc` waiver line is removed, nothing else. `engine/m9/enforce.py`: only the ijc readability count changed, 156 → 155.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0.

## Opener check, record by record

| Record | Removed question | New first sentence | Answers? |
|---|---|---|---|
| ancient-custom | How did we know our practices went back to the apostles? | 'Ancient custom' was our strongest currency, so we kept asking whether our own practices truly went back to the apostles. | Names the evidence the world used (positions[0]); see finding 6 |
| baptism-threshold | Were we 'born again'? | We would have pointed to baptism as our 'born again,' … | Yes |
| collections-discipline | Did we tithe, and how did we decide what to give? | We had a real giving discipline. | Partly; see finding 3 |
| received-not-seen | What did we actually have about Jesus? | What we had about Jesus was inheritance, not memory. | Yes |
| record-under-question | How much of our story would hold up in a library? | More of our story would hold up in a library than of most ancient worlds, … | Yes |
| room-for-hesitation | Was there room for doubt here? | There is documented room for hesitation, at the highest level, about the deepest things. | Yes |
| women-authority-cost | Could a woman carry real authority among us, and what did it cost her? | A woman could carry real authority among us. | Yes; the cost follows in sentence two |

No claim was added, dropped or reordered in a way that changes it, beyond the small word additions in finding 6. The women-authority-cost splits are faithful: each split falls at an existing joint ("when he refused" → "He had refused", which keeps the sequence; the penalty list's colon and commas become full stops; "and everything" → "Everything"; "and none of this" → "None of this"). The only new words there are "It happened" in sentence two.

## Findings

### 1. SUBSTANTIAL — three ijc witnesses still open with a second-person stage direction ("You ask …")

The checker matches "you asked" but not the present tense "You ask", so these were never counted in the spoken-scaffolding entry (2026-10-06). They are the same class the pass removes: the record scripts the participant's question and addresses them.

- `ijc.dw.bread-made-body`: "You ask what the bread and cup were to us, and whether we already held what your age calls transubstantiation."
- `ijc.dw.marriage-ranked`: "You ask what marriage meant among us."
- `ijc.dw.original-sin-transmitted`: "You ask whether we thought people were born already guilty."

Fixes (record's own words only; no quoted passage touched):
- bread-made-body: replace the first two sentences with "We would not have used your age's word, transubstantiation. But we taught the thing that word points to, plainly, to the newly baptized: …" (the rest unchanged). Leave "And you say, Amen" alone: it is Ambrose's own address to the newly baptized, not scaffolding.
- marriage-ranked: replace "You ask what marriage meant among us. It was not nothing, and it was not first either." with "Marriage among us was not nothing, and it was not first either."
- original-sin-transmitted: replace "You ask whether we thought people were born already guilty. Yes - and our own record says so …" with "Yes, we thought people were born already guilty - and our own record says so …".

Add the three to gap entry 29's changed-records list. Not a record fix, so not required here: the checker pattern in `engine/m1/spoken_scaffolding.py` should also catch "you ask"; that is a fleet-level change for whoever owns the check.

### 2. SUBSTANTIAL — scripted questions left mid-text, including in the identity witness

The pass turned the mid-text "How did we know the resurrection happened?" in `received-not-seen` into a statement. The same scripted-question shape remains in two untouched witnesses. The voice-errors entry (staging reading, 2026-10-07) records the voice pasting "a record's own scripted question" from `ijc.dw.jesus`, so this is a live defect, not style.

- `ijc.dw.jesus`: "Who was he? The creed answers: very God of very God, …" Fix: "The creed says who he was: very God of very God, …" (the creed words after the colon unchanged).
- `ijc.dw.how-we-read`: "And how did someone who could not read receive all this? The record barely says." Fix: "The record barely says how someone who could not read received all this."

Entry 29's line "`ijc.dw.jesus` … is untouched" then becomes "edited only to remove its mid-text question". Not substantial: `how-we-read`'s "Was the Son 'like the Father,' … or 'of one being' with the Father, a phrase scripture nowhere uses?" states the century's own dispute, not a participant's question; it may stay. The questions inside `ijc.story.emperor-penance`, `eutropius-at-the-altar` and `letter-that-outranked-a-council` are the sources' own words and stay.

### 3. SUBSTANTIAL — `collections-discipline` opener does not answer the tithe question

The removed question was "Did we tithe?" (cell F4-T). "We had a real giving discipline" reads as a yes; the actual answer, no fixed tenth, comes in the sixth sentence. Gap entry 29 notes this and leaves it, but a hearer who stops after the opener is misled.
Fix: "We had a real giving discipline, but not a fixed tenth." The later sentence "The measure was not a fixed tenth stated as law" stays; the claim is the record's own (positions[1]).

### 4. SUBSTANTIAL — stale cross-reference kept in the rewritten `collections-discipline` body

The pass rewrote the body sentence to: "Leo's own preached corpus (file lines 13503 and 13707) states a real, if proportional rather than fixed, giving discipline, against ijc.dw.baptism-threshold's own closing note that 'church funding in this record is imperial patronage and endowment, not tithe-discipline.'" No such note exists in `baptism-threshold` (it was removed in 68eb4e59, before this PR; `grep` finds the phrase only here). The clause is correction history pointing at text that is gone. Fix: end the sentence at "giving discipline." and delete the "against … tithe-discipline.'" clause.

### 5. SUBSTANTIAL — gap entry 29 has two inaccuracies and a bare-number cross-reference

(a) It quotes the women-authority-cost opener as "A woman could carry real authority among us - twice on the record's own terms - and both times the cost was steep." The record says "A woman could carry real authority among us. It happened twice on the record's own terms, and both times the cost was steep." It also says "only the joints changed", but "It happened" was added. Fix: quote the record's actual two sentences and say "only the joints changed, plus 'It happened' to make the second sentence whole".

(b) "entry 24 item (3)" cites a bare number. CLAUDE.md requires subject + date. Fix: "the record-defects entry (Record defects found while drafting and reviewing use notes (slice 6), 2026-10-04), item (3)".

(c) Update the entry for findings 1–4 once they land (records changed, openers, the dropped clause).

The known-wrong-claim list is otherwise complete: of the gap entries naming these 7 records, only the record-defects entry (2026-10-04) item (3) is a wrong claim (`baptism-threshold`, "in about a week"); it is carried unchanged and flagged. The voice-errors entry (2026-10-07) item (4) on `received-not-seen` is a copying defect in the voice, not a wrong claim in the record.

### 6. Not substantial — `ancient-custom` opener adds "truly" and "our own", and leads with the evidence rather than the verdict

"We kept asking whether our own practices truly went back to the apostles" adds two intensifiers the old question did not carry; neither changes a claim. The opener does answer the F4-E probe's kind (what evidence: appeal to ancient custom, positions[0]); the verdict (some old, some new and known new, the claim a tool) still comes last. Acceptable. Optional: drop "truly".

### 7. Not substantial — body trimming

The trims removed cell codes, "verified" narration, register boilerplate and design rationale. Every source and line pointer of substance survives (npnf209:3707-3741; npnf214 from line 20105; Socrates I.8; file lines 41434-41520 and line 704; Ep. XX.6-7, XCV, CV; file lines 13503 and 13707). The `ancient-custom` pointers "Canon 6 at the source record; Julius and Augustine at their quote records" went, but the frontmatter cites those records. The `baptism-threshold` "inward-experience gap stated rather than filled" went, but the text itself states it ("Our record marks the threshold, not the feeling").

`baptism-threshold` body keeps "The end-times question remains genuinely thin: … no comparable material was found for it." That is a coverage gap living only in a record body; no gap entry mentions end-times. Recommended, not required: log it in the gap file and drop it from the body, as the Cappadocian round 1 review did for its coverage notes.

### 8. Not substantial — wording

- `record-under-question`: "than of most ancient worlds" is stiff. Optional: "More of our story would hold up in a library than the story of most ancient worlds, …".
- `baptism-threshold`: "If by 'born again' you mean a datable, decisive crossing …" addresses the participant's term to define it; it is not a stage direction about reply order. It may stay.
- Several edited lines in the YAML block run long (unwrapped); harmless.

## Gates

`check_live_commentary --base origin/main --enforce` exit 0 (reviewer run). Pin and waiver edits verified by reading. `python -m engine.m9.cli check` exit 0, "clean - every finding is waived, every waiver is live and current", so the ijc readability waiver at 155 matches this run. `python -m engine.m10.cli records ijc`: PASS. The m1/m10 suites were not re-run.

## Round-2 recheck scope

Findings 1–5 only: the five witness edits (bread-made-body, marriage-ranked, original-sin-transmitted, jesus, how-we-read), the collections-discipline opener and body clause, gap entry 29 text, and the package rebuild, repin and readability-waiver count that follow.
