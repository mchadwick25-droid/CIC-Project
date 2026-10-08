# ijc — identity-and-scaffolding record pass, adversarial review round 3, targeted recheck (2026-10-08)

Branch `records/identity-scaffolding-ijc` (PR #827). Round 2: `ijc_identity_scaffolding_review_round2_2026-10-08.md` (REVISE, substantial findings 1-2). Recheck diff: `git diff 8640b576..HEAD`, covering f41590e0 (record and gap-entry edits), d9081e9d (package rebuild and repin) and f9b41c48 (site JSON). Reviewer: Opus 5.5. No model or API spend. No records edited. Long suites not run. This is the third review file on the pass, which is the cap.

**Verdict: CLEARED.** Both round-2 substantial findings are fixed as asked. Nothing regressed.

## Round 2 findings, rechecked

| # | Asked | Done? |
|---|---|---|
| 1 | bread-made-body opener back to round 1's wording, no added claim | Yes. `text` now opens "We would not have used your age's word, transubstantiation. But we taught the thing that word points to, plainly, to the newly baptized: this is not what nature made, ..." The flat "We held what your age calls transubstantiation" is gone. The opener now agrees with the record's `tensions` and `use_note.not_for`. Only the first two sentences changed; the quoted blessing teaching that follows is untouched. |
| 2 | Gap entry 29: add "plus 'It happened'" for women-authority-cost; quote the new bread-made-body opener | Yes. The entry reads "only the joints changed, plus "It happened" to make the second sentence whole, and "when he refused" became "He had refused"". The record holds "It happened twice on the record's own terms, and both times the cost was steep." and "He had refused". The bread-made-body clause quotes the opener exactly as the record has it, and its gloss ("the world would not use the word and taught what it points to") is accurate. |

## Package, pin and site

- `sha256sum packages/ijc/2026-10-08T06-07-31Z/manifest.json` = `0e5aea46…0b20da`, matching `records/worlds/ijc.yaml` `manifest_hash`; `location` matches.
- Manifest `records_commit` is f41590e0, the last commit that touched `records/ijc`.
- The package's record copy, compiled chunk, `prompt.txt` and `repository.json` all carry the new opener. No file in the package, `records/` or `cic-website/` still holds "We held what your age calls".
- The site JSON was recompiled from d9081e9d (no record change after f41590e0) and carries the new opener.
- Gap entry 29 names the new package path.

## Regression checks

- `scaffolding_hits(load_world_records('ijc'))` returns `[]`.
- The only record changed since round 2 is `ijc.dw.bread-made-body`, one line of `text`. No quote record changed. No other field of that record changed.

## Findings

### 1. Not substantial — `ijc.demo.ordinary-day` exchange[1] opens "You ask for an ordinary day among us ..."

Carried from round 2, finding 3. It is a demonstration record, outside this pass. If demos are meant to model the voice, a later pass may rephrase it. No action here.

### 2. Not substantial — stray space in gap entry 29

The bread-made-body clause ends "...taught what it points to) ;" with a space before the semicolon. Cosmetic. It can be fixed in a later edit; it is not a reason for another round.

### 3. Not substantial — carried from round 1

Round 1 findings 6-8 (ancient-custom "truly", the baptism-threshold end-times note, record-under-question wording) were optional and are unchanged. The known-wrong baptism-threshold "in about a week" claim stays flagged for Mark in entry 29, as before.

## Closure

The pass may be marked approved to proceed on review. Entry 29's status line ("OPEN until the review clears") can now be updated by the build thread.
