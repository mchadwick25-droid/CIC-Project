# Applying the whole-set rulings (P2-L11b), 2026-11-08

The whole-set review of eras 1 to 9 (`../2026-11-08_links-whole-set-review/`) held five questions for Mark. He ruled on each, one at a time, from options with a recommendation. The rulings are in the Church Family Tree's Decision-Log, "Whole-set rulings" (2026-11-08). This pass applies them as data release 18.

## The rulings and what changed

1. **One old account.** A link whose only support is one 19th- or early-20th-century account is Dominant Modern Reconstruction only where a modern study already cited in the repo supports the same reading. Otherwise it is Inferential-Thin.
   - 6 links moved from Dominant Modern Reconstruction to Inferential-Thin: four Kievan links and two Georgian ones.
   - 2 moved up: the Lavra's founding (Morris 1995) and the Alaskan mission (Oleksa; Black).
   - 4 stayed Dominant, each with its repo-cited modern study added: Franklin and Shepard, Morris, Obolensky, Dvornik.
   - 3 stayed Thin, because no modern study is cited in the repo.
   - Eight Dominant links rest on two or three pre-1930 accounts. The ruling's words ("one account") do not cover them, so they are unchanged.
2. **What `verified-direct` means.** The quoted lines were read and match. Whether they show the relationship is what the grade says. 47 links changed state: a link with a checked quote is verified-direct, and one without a quote is named-not-rechecked.
3. **A secondary work held in the Library.** It may carry file, lines and a verbatim quote, all three together. 29 links got back the lines and quotes that era 5's revision had stripped. Two era 4 links had their lines in the title text; these now carry them in the right fields, with quotes taken from those lines. `tools/validate-census.mjs` now checks every such quote word for word; all 218 existing ones pass. New tests: `tools/tests/validate_census_secondary.test.mjs`, run in CI.
4. **Deposed by any authority.** A church head or prelate deposed by any authority, church or state, counts as an institutional act for major links. The Avedik link (`armenian-christianity-era-8--armenian-apostolic-church-era-8`) now carries an outcome. 17 other candidates were checked and rejected, each with its reason in `Draft_Rulings_1_4.json`. The public method page and the launch prompt's step 4b say the same.
5. **Bogomils to Cathars.** `bogomils--cathars-albigensians` is retired, with a `retiredLinks` entry pointing to `balkan-bogomil-continuation--cathars-albigensians`.

Also amended: the Drafting Brief (`../2026-11-06_census-lineage-rigor/Drafting_Brief.md`) for rulings 1 to 3.

## Counts (release 17 to 18)

- Links changed: 77, including 1 retired.
- Fields changed: 47 check states, 32 source lists, 9 notes, 8 grades, 1 outcome.

## Rounds

1. **Draft** (Opus): `Draft_Rulings_1_4.json` for rulings 1 and 4. Ruling 3's restored sources came from era 5's own drafts (`Ruling3_Restored_Sources.json`). Rulings 2 and 5 were applied by script.
2. **Review round 1** (a separate Opus 5.5 agent, full): `Opus_Review_Round1.json`. Revise: 3 substantial, 3 minor. Applied: `Revision_Round1.json`.
3. **Review round 2** (separate Opus 5.5, targeted): `Opus_Review_Round2_TargetedRecheck.json`.

No model call was metered.

## Open

- Eight Dominant Modern Reconstruction links rest on two or three pre-1930 accounts with no modern study in the repo. They fall outside ruling 1's wording. Optional modern studies for two of them are in `Draft_Rulings_1_4.json` (Skinner 2009; Frazee 1983).
- The wider overlap of the two Bogomil entries stays open (Open-Gaps, "The Bogomil entries overlap", 2026-11-08).
