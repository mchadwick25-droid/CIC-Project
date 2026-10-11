# don: leftover spoken-scaffolding fields, single review, 2026-10-08

Reviewer: Opus 5.5. Branch `records/identity-scaffolding-don-leftovers`, `git diff origin/main...HEAD` (commits 106b0849, 7f0ae427). One review of new work. This is not a fourth round on the identity-and-scaffolding pass (rounds 1-3 in this folder).

Scope: `don.dw.written-by-our-opponents` `text` (first sentence), `don.witness.refusal-and-recourse` `positions[0]`, body commentary in both records, removal of the `spoken-scaffolding/don` waiver in `engine/m1/cross_world.py`, the rebuilt package and its pin in `records/worlds/don.yaml`, and OG-28 in `Build/worlds/don/Open_Gaps_Tracking.md`.

## Verdict: REVISE

One substantial finding: `python -m engine.m9.cli check` fails on the branch and passes on `origin/main`. The fix is mechanical (one integer). The record text itself is sound and needs no change.

## What was checked, and held

- **Claims kept, nothing added, no yes/no invented.** `written-by-our-opponents`: old "A historian would ask one question about everything we have said, and it is the right question: who wrote it down? The answer, for nearly all of it, is our enemies." New "Almost everything we have said was written down by our enemies, and a historian is right to ask who wrote it down." Both claims kept (nearly all of it is the enemies' hand; the question is the right one). No new fact. No yes or no. The rest of `text` is byte-identical to `origin/main`. `refusal-and-recourse` `positions[0]`: the stance, the primate attribution ("is remembered to"), the retort, "we hold it still", the three rulings (Rome 313, Arles 314, Carthage 411), and the closing clause are all kept. "He may rule" became "The emperor may rule"; that only restores the antecedent the reorder took away. "Put it in one line" matches the existing wording in the same record's `text`. No new claim.
- **Quote.** `cic/texts/optatus_against-the-donatists.txt` line 1904 reads `'What has the Emperor to do with the Church?'`. `don.quote.donatus-quid-est-imperatori` `text` gives `("What has the Emperor to do with the Church?")`. `positions[0]` now reads `"What has the Emperor to do with the Church?"`. All three match verbatim, capitals included. The old lower-case "emperor"/"church" was a real misquote and is now fixed. No other quote sits in either touched sentence. The `text` field of `refusal-and-recourse` already carried the correct capitals and was not touched.
- **Quote after the opener.** Acceptable. The field now opens on the world's own claim, and the quotation follows as the evidence for it. That is the same shape the record's `text` already uses ("The emperor has no standing to judge us. Our primate put it in one line: ..."). It also reads better: the participant hears the answer before the retort.
- **Scaffolding.** `regate don --base origin/main` passes with the waiver removed. `scaffolding_findings` fails a world that has hits and no waiver, so a pass means `scaffolding_hits` finds nothing for don. A waiver left on a clean world would also fail, so removing it was required, not optional.
- **Readability.** Scored with `engine.m7.turn_readability.score_turn`: `positions[0]` went from FK 10.6 / FRE 68.6 (failing, above the ceiling of 10) to FK 8.2 / FRE 75.9 (passing). `written-by-our-opponents` `text` went from FK 6.9 / FRE 73.7 to FK 7.0 / FRE 73.4, with no new failure. `regate` reports no regression on either record.
- **Body commentary.** `written-by-our-opponents`: the source basis (`world_core` `thinness` and `cautions`), the two transcript ids, and the unanswered fourth variant are kept. The old body put "this world's evidence survives in INVERSE proportion ..." inside quotation marks as `world_core` wording. The current `world_core` `thinness` does not contain that sentence (it reads "The less directly a claim can be checked, free of a hostile hand, the better this world's evidence survives for it"). Dropping the quotation marks removes a false verbatim claim. `refusal-and-recourse`: Doc_04 SS3.6 with its three dated instances, Doc_07 SS4/SS6, the quote record, and the F1-E fit are kept. "Already-cleared", "after this script runs" and "this is the first" were process narration and are gone.
- **Package.** `sha256sum packages/don/2026-10-08T15-41-59Z/manifest.json` = `d98ede906cfba7b5afc451b6f6b70d5d8a09b000a2430b6102307fe3df93c227`. That equals the `manifest_hash` in `records/worlds/don.yaml` and in OG-28. `diff -rq records/don packages/don/2026-10-08T15-41-59Z/records` shows no difference.
- **Gates run.** `engine.m10.cli records don`: PASS. `engine.m10.cli regate don --base origin/main`: PASS. `tools/check_live_commentary.py --base origin/main --enforce`: exit 0. `pytest engine/m1/tests engine/m10/tests`: 596 passed. `engine.m9.cli check`: FAIL (finding 1). On a clean `origin/main` worktree, `engine.m9.cli check` reports no problem.

## Findings

### 1. SUBSTANTIAL - the don readability waiver is now stale, and `engine.m9.cli check` fails

`python -m engine.m9.cli check` on the branch:

```
library access gate: 1 problem(s)
  m1:readability/don: waiver says 327, this run found 326 - the waiver is stale - tighten it
```

Cause: the rewrite of `refusal-and-recourse` `positions[0]` cleared that field's FK failure (10.6 to 8.2). This is a good outcome, but the count waiver must follow it. CLAUDE.md treats a stale waiver as a failing run.

Fix: in `engine/m9/enforce.py` line 171, change
`"m1:readability/don": Waiver(count=327, ...`
to
`"m1:readability/don": Waiver(count=326, ...`
Then rerun `engine.m9.cli check`, and add it to OG-28's Gates line (finding 2).

### 2. NOT SUBSTANTIAL - OG-28 Gates line omits `engine.m9.cli check` and the readability gain

Old: "**Gates.** `engine.m10.cli records don` and `regate don --base origin/main`: pass."
Fix: "**Gates.** `engine.m10.cli records don`, `regate don --base origin/main` and `engine.m9.cli check`: pass. `positions[0]` no longer fails the readability ceiling (FK 10.6 to 8.2), so the `m1:readability/don` waiver in `engine/m9/enforce.py` is tightened from 327 to 326."

### 3. NOT SUBSTANTIAL - OG-28 says the Optatus line pointer was "kept" in the body; it was added

The old `refusal-and-recourse` body named no Optatus line. It cited only "the already-cleared don.quote.donatus-quid-est-imperatori record". The new body adds "Optatus, Against the Donatists, Book III, line 1904, `cic/texts/optatus_against-the-donatists.txt`". That pointer is true: it matches the source file and the frontmatter `sources` locus. But it is new to the body.
Old (OG-28): "Kept: the source basis (...), the two transcript record ids, the Doc_04/Doc_07 grounding, the Optatus line pointer, and the fact that ..."
Fix: "Kept: the source basis (...), the two transcript record ids, the Doc_04/Doc_07 grounding, and the fact that ... The `refusal-and-recourse` body now also gives the Optatus line pointer, taken from the record's own `sources` locus."

### 4. NOT SUBSTANTIAL - OG-28 calls two old sentences the "Old first sentence"

The quoted old text is two sentences ("... who wrote it down? The answer, for nearly all of it, is our enemies."). Fix: "Old first two sentences:".

### 5. NOT SUBSTANTIAL - OG-28's list of removed commentary is incomplete

The diff also removes "T1 already has a classified gravity record ... this is the first" and "which is a harder and truer thing to say than a general defence of the sources". It also drops the double quotation marks around the inverse-proportion sentence, and the old wording was not verbatim `world_core` (see "Body commentary" above). Fix: add these to the "Commentary removed" sentence, and note the quotation marks dropped because the wording is not in the current `world_core`.

### 6. NOT SUBSTANTIAL - the reordered `written-by-our-opponents` opener puts the question after its answer

New: "Almost everything we have said was written down by our enemies, and a historian is right to ask who wrote it down." The claim is accurate and the sentence is 21 words. But it gives the answer before the question, so it can read slightly backwards. An optional tighter form that keeps both claims: "Almost everything we have said was written down by our enemies. A historian is right to ask who held the pen." Not required. The current text is accurate and clears the gates.

### 7. NOT SUBSTANTIAL - "We hold" twice in `positions[0]`

"We hold that the question ... One of our own primates ... We hold it still." The repetition is deliberate emphasis and carries the old "we hold it still". It is acceptable as is. Optional: drop "that" in the first clause so the stance reads as the world's voice: "The question of which church is the true one is not the emperor's to settle." That cuts the first "hold" and leaves "We hold it still" as the only one.

### 8. NOT SUBSTANTIAL - pre-existing, outside this change: `refusal-and-recourse` `sources[0].locus` puts the Latin at line 1904

The locus reads "Book III, line 1904, Donatus's own reported retort ('Quid est imperatori cum ecclesia?')". Line 1904 of `optatus_against-the-donatists.txt` carries only the English. The quote record's `divergence_note` puts the Latin at `optatus_libri-vii-critical_ziwsa1893.txt` line 6557. This change did not touch it, so it does not block. It should be logged as an open gap for the don record thread rather than fixed here.

## Disposition

Fix finding 1 and rerun `engine.m9.cli check`. Fold findings 2-5 into OG-28 in the same commit. No package rebuild is needed, because the package does not include `engine/` or `Build/`. Findings 6-7 are optional. Finding 8 goes to the don gap log. A recheck of finding 1 alone suffices; the record text needs no further review.
