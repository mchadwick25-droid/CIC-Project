# P2-V, what "living" means: data release 30 — 2026-11-10

The Church Family Tree's written definition of "living" and the check of every living flag
against it (Build-Plan, P2-V; Decision-Log, "What 'living' means: P2-V applied as data release
30", same date). One data release: 353 movements and 689 links, unchanged; 264 living flags (192
before).

## What was ruled before, and what this applies

- Ruling 15 (2026-11-06): a written definition and a check of every flag before the leaf appears.
- The era 10 change order (2026-11-08), rules 2 and 4: the mark means alive today in every era;
  only the frozen Living-Era Protocol Addendum V1.0 governs it (R2 dated own-voice evidence, R3 the
  CD and CR grades, R4 present-tense humility).
- The gap sweep, principle 3 (2026-11-09): a successor entry, not a stretched one; otherwise a
  named gap.
- The era 10 gate, G-5 (a): episodes of living traditions keep the mark; bodies with no dated
  source keep it, with the source wanted.

## How it ran

1. `worksheet.mjs` lists every movement with its flag, its "continued as" line and the living
   entries it links to (`worksheet.json`).
2. `line_decisions.mjs`: the 59 entries in eras 1 to 9 whose "continued as" line reaches a living
   era 10 entry are the same tradition by the tree's identity rule (`line_decisions.json`).
3. Six Sonnet researchers checked the other 200 entries in eras 1 to 9 under `Research_Brief.md`
   (`research/result_batch_1.json` to `_6.json`). A seventh found dated evidence for the 12 era 10
   carriers that had none (`research/era10_evidence.json`). A Sonnet worker ran the backward check
   from 58 present-day families (`research/backward_check.json`).
4. `check_quotes.py` re-verified every quote by two methods: the page saved when it was taken, and a
   fresh fetch (`research/quote_check.json`, `research/quote_check_era10.json`). Quotes added in
   revision were checked the same way by the reviser (`reviews/Revision_Round1.json`, `_Round2.json`).
5. `merge.mjs` merged the results into `decisions_draft.json`, flattening carriers to the entries
   that hold their own evidence.
6. Opus reviewed under `Review_Brief.md`, which adds the consistency rule: round 1 (44 substantial,
   9 cosmetic, 4 change orders), round 2 as a targeted recheck (9 substantial, 5 cosmetic), round 3
   (approved: 0 substantial, 2 cosmetic). Sonnet revised after rounds 1 and 2
   (`decisions_r1.json`, `decisions_r2.json`, `era10_evidence_apply*.json`).
7. `decisions_final.json` is round 2's output with two spelling fixes (American spelling in
   paraphrase; a quoted title kept as written). `era10_evidence_final.json` is round 2's era 10
   file. `apply_living.mjs` applied both to main's census (`apply_log.json`).
8. `open_gaps_text.mjs` drafted Open-Gaps 157 to 163.
9. After merge with main, CI's fleet check (`engine/m1/tests/test_cross_world.py`) found the census
   flag for `alx` (the Alexandrian catechetical school) disagreed with its world registry. The
   world's own construction record confirms its Article 29 Living Tradition Status (Mark,
   2026-07-17), naming the Coptic Orthodox Church as its primary living heir. That ruling governs,
   so I.2 was restored as living, an episode carried by the Coptic line (`revisedBy`:
   `alx-article-29`). The research brief had not told researchers to read a built world's own
   status; the fleet check now catches it. Fleet check rerun: 0 new defects.

The lead's rulings on round 1's four change orders: CO-1 (era 10 evidence) is not a change order,
since grading a flag is this chunk's job, and was done; CO-2 (link grades) goes to P2-L11, and
descent grades no longer copy them; CO-3 (no end and no dated source) follows G-5 (a); CO-4 (the
Lérins text) goes to the entry's owner (Open-Gaps 160).

The raw research files keep each researcher's state as delivered. Round 2 corrected two era 10
citations (the Moscow Times URL; a staging copy of the Mar Thoma site, dropped); the corrected
citations are in `era10_evidence_final.json`, which is what the census carries (round 3, R3-01).

## Outcome

| | count |
|---|---|
| living before (eras 1 to 10) | 192 (era 10: 65) |
| eras 1 to 9, true flags kept | 117 |
| kept with a new descent grade | 9 |
| dropped | 1 (the North African Latin church) |
| added (false to true) | 73 |
| stay not living | 59 |
| living after | 264 (era 10: 65, unchanged; 12 gain dated evidence) |
| own grades in eras 1 to 9 | 6 CD, 62 CR, 4 none |
| descent grades | 23 |

## Checks run

- `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`: 0 errors, 2 old shortName warnings.
- `python -m engine.m6.cli atlas-sync`, then `atlas-check`: no changes left.
- `node Build/tools/generate_tree_pages.mjs`; `node tools/build_tree_site.mjs`: 0 mismatched.
- `node tools/check_tree_domains.mjs`: census identical on both domains.
- Node tests: the validator suite (44, with new tests for the living mark) and
  `generate_tree_pages.test.mjs` with `cic-worker/worker.test.mjs` (47).
- `python tools/check_live_commentary.py --base origin/main --enforce`: passes.
- `python tools/check_spelling.py`: 0 British spellings.
- The definition: Flesch-Kincaid grade 8.0, reading ease 65 (`engine.m1.gates.grade_text`).

No model call outside this conversation, no paid run, no recording. The method page has no
recording, so none goes stale.
