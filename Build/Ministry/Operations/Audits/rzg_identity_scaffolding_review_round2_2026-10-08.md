# rzg — identity-and-scaffolding record pass, adversarial review round 2 (2026-10-08)

Branch `records/identity-scaffolding-rzg` (PR #828). Targeted recheck of the changes made after round 1 (`rzg_identity_scaffolding_review_round1_2026-10-08.md`): commits 31ca4c20 and 2341db4a, `git diff fe21a17f HEAD`. Reviewer: Opus 5.5. No model or API spend. No records edited.

**Verdict: CLEARED.**

## Scope

Since round 1, three files changed beyond the round 1 review file: `rzg.witness.a-narrow-true-church.md` (one line, `text`), `Build/worlds/rzg/Open_Gaps_Tracking.md` (entry 61), and the package (`packages/rzg/2026-10-08T06-41-07Z/manifest.json`, `records/worlds/rzg.yaml`). Nothing else moved.

## Findings

### 1. Round 1 finding 1 (SUBSTANTIAL) — resolved

New opener: "We held the alternatives we refused to be wrong, not merely different. The charge is that this made us too narrow, one way among every way people have ever reached for God. We will not answer it more gently than it deserves."

Against `git show origin/main:` the main text is "Too narrow, one way among every way people have ever reached for God? We will not answer that more gently than it deserves. We held the alternatives we refused to be wrong, not merely different." The answer now comes first. The three sentences are the record's own. The only new words are the frame "The charge is that this made us", which turns the old scripted question into a statement, and "that" → "it". The frame claims nothing the old question did not put; "this made us" only names what the charge is aimed at. Nothing is lost. The rest of `text` is byte-identical to main. It is exactly the fix round 1 prescribed. No other field in the record changed.

### 2. Round 1 finding 2 (not substantial) — not taken; acceptable

"Each time, the same test: does this reading hold against Scripture?" remains. Round 1 marked it optional: it states the test, it does not put a question to the participant. `scaffolding_hits` does not flag it. Not substantial.

### 3. Gap entry 61 — exact (not substantial, no defect)

The entry quotes the new opener word for word, notes it as "the record's own sentences, reordered so the answer comes first", and now names package `packages/rzg/2026-10-08T06-41-07Z`. The rest of the entry is unchanged from the version round 1 checked. Round 1's optional addition (a), the Consensus Tigurinus dating note, was not taken; it stays optional.

### 4. Package pin — matches (not substantial, no defect)

`sha256sum packages/rzg/2026-10-08T06-41-07Z/manifest.json` = `6f3d177f…e951b5`, matching `records/worlds/rzg.yaml` `package.manifest_hash`. `location` matches. Manifest `records_commit` and `built_by` are 31ca4c20, the commit carrying the record edit. The compiled `repository.json` carries the new opener.

### 5. Site JSON — not stale (not substantial, no defect)

`cic-website/data/worlds/the-reformed-cities-zurich-and-geneva.json` holds only `census_id`, `narrative`, `orientation`, `skim`. It carries no witness text and no package hash, and it is untouched on this branch. Nothing in this change reaches it.

### 6. Scaffolding and regressions — clean (not substantial, no defect)

`scaffolding_hits(load_world_records('rzg'))` returns `[]`. The reorder adds one word to the record and moves no sentence boundary, so the readability count behind the m9 waiver (131) cannot have moved by a sentence; the full m9 check was not re-run here (long suite). No other record, engine or waiver file changed since round 1.

## Result

Round 1's one substantial finding is fixed as specified. Nothing regressed. Entry 61 may move from OPEN when the PR's CI passes.
