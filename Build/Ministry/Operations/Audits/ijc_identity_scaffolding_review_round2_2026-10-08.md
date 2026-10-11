# ijc — identity-and-scaffolding record pass, adversarial review round 2, targeted recheck (2026-10-08)

Branch `records/identity-scaffolding-ijc` (PR #827). Round 1: `ijc_identity_scaffolding_review_round1_2026-10-08.md` (REVISE, substantial findings 1-5). The round 1 file was added in the same commit as the fixes (c483e4fb), so the recheck diff is `git diff c483e4fb^..HEAD`: c483e4fb (record and gap-entry edits), b7fc3783 (package rebuild and repin), 8640b576 (site JSON). Reviewer: Opus 5.5. No model or API spend. No records edited. Long suites not run.

**Verdict: REVISE.** One new substantial defect, introduced by the finding-1 fix, plus one round-1 item not carried out. Both are one-line fixes.

## Round 1 findings, rechecked

| # | Asked | Done? |
|---|---|---|
| 1 | Drop the "You ask ..." openers in bread-made-body, marriage-ranked, original-sin-transmitted | marriage-ranked and original-sin-transmitted: yes, exactly as asked; claims unchanged. bread-made-body: the stage direction is gone, but the new wording adds a claim. See finding 1 below. |
| 2 | Turn the mid-text scripted questions in `jesus` and `how-we-read` into statements | Yes. `jesus`: "The creed answers who he was:" (creed words unchanged). `how-we-read`: "The record barely says how someone who could not read received all this." |
| 3 | `collections-discipline` opener | Yes: "We had a real giving discipline, but not a fixed tenth." |
| 4 | Drop the stale `baptism-threshold` clause in the `collections-discipline` body | Yes. The sentence ends at "giving discipline."; the line pointers (13503, 13707, ~13612) stay. |
| 5 | Gap entry 29 | (b) fixed: subject + date cross-reference. (c) fixed: 12 records listed; openers quoted match the records verbatim (checked each). (a) half done: the women-authority-cost opener is now quoted correctly, but the entry still says "only the joints changed" and does not note the added "It happened". See finding 2. |

Package and site: `sha256sum packages/ijc/2026-10-08T05-56-34Z/manifest.json` = `2adcbb3e…aa1fd1576`, matching `records/worlds/ijc.yaml` `manifest_hash`; `location` matches; manifest `records_commit` is c483e4fb, the last commit that touched `records/ijc`. The site JSON was recompiled from b7fc3783 (no record change between the two) and carries the new bread-made-body text.

Bodies of the 5 newly edited records, against `origin/main`: the trims removed "verified directly" narration, cell codes (F1-T, F2-I, F5-T), "the Center cell's composed answer-ground" and the register boilerplate. Kept: every file-line pointer (33189-33271, 38845-38850, 7398), the honest-limit pointers (`ijc.limit.later-questions`, `ijc.limit.marriage-money`) with what they cover, the companion quote ids in `jesus`, the vendored-instance list and the canon-list caveat in `how-we-read`. Only `how-we-read`'s "Doc_05 SS8's finding" went; the vendored instances it named stay. Acceptable.

Quotes: no quote record changed; no sentence in quotation marks was edited in the touched witnesses.

Scans: `engine.m1.spoken_scaffolding.scaffolding_hits(load_world_records('ijc'))` returns `[]`. A regex scan of every spoken field (nested included) of every ijc record for "you ask / you asked / your question" and for question-form first sentences, plus every "?" in a witness `text`, found only: participant turns in `ijc.demo.*` exchanges (questions by design); quote `text`/`modern_rendering` that are the sources' own questions; the `how-we-read` Homoian-dispute question round 1 allowed to stay; and `ijc.demo.ordinary-day` exchange[1] (see finding 3).

## Findings

### 1. SUBSTANTIAL — the new bread-made-body opener asserts more than the record holds

Old: "You ask ... whether we already held what your age calls transubstantiation. We would not have used your word. But we taught the thing your word points to ..." New: "We held what your age calls transubstantiation, though we would not have used your word."

The old text never said yes to the label; it said the world taught the thing the word points to. The new first sentence states flatly that the world held transubstantiation. The record's own `tensions` say the opposite of an identity: "the doctrine of a real change is plainly taught; its later precise philosophical formulation is not this record's own language", and `use_note.not_for` excludes "a claim that this world used the term transubstantiation or scholastic substance-and-accidents language". The voice will speak the first sentence as a settled yes to a contested anachronism. Gap entry 29 says nothing was added; here something was.

Fix (round 1's own wording, record's words only): "We would not have used your age's word, transubstantiation. But we taught the thing that word points to, plainly, to the newly baptized: ..." (the rest unchanged). Update the bread-made-body clause in entry 29 to quote it.

### 2. SUBSTANTIAL (small) — gap entry 29 still says "only the joints changed" for women-authority-cost

Round 1 finding 5(a) asked for "only the joints changed, plus 'It happened' to make the second sentence whole". The entry still reads "only the joints changed, and 'when he refused' became 'He had refused'". "It happened" is a word addition, and the audit line is inaccurate without it. Fix: add "plus 'It happened' to make the second sentence whole".

### 3. Not substantial — `ijc.demo.ordinary-day` exchange[1] opens "You ask for an ordinary day among us ..."

This is the Representative's turn in a demonstration exchange, answering a participant turn that really asked it, not a record scripting a question. Outside this pass's scope. If demos are meant to model the voice, the owner may want it rephrased in a later pass; no gap entry required here.

### 4. Not substantial — carried from round 1

Round 1 findings 6-8 (ancient-custom "truly", baptism-threshold end-times note in the body, record-under-question wording) were optional and are unchanged. No action required.

## Round-3 recheck scope

Findings 1-2 only: the bread-made-body opener, gap entry 29's bread-made-body and women-authority-cost clauses, and the package rebuild, repin and site recompile that follow the record edit. This would be the third review file on the pass; per the cap, a further failure escalates to Mark.
