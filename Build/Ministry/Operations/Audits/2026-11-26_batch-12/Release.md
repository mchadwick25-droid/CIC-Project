# Release 13: batch 12, era 1 people

Thirteen people released into the census and the tree: Anatolius of Alexandria and Laodicea, Clement of Alexandria, Hippolytus of Rome, Ignatius of Antioch, Lactantius, Methodius of Olympus, Origen, Pamphilus of Caesarea, Pontius the Deacon, Suetonius, Tacitus, Tatian and Valentinus. Mark's word: "fix the easy ones and release". Branch `claude/cft-release-batch12-13`, from `main` at d729d319, with `main` merged in after Josephus (#1843) and the card-rule kit fix (#1844).

## What changed

- **Census** (`cic-website/data/world-census.json`), the 13 entries only: `longDescription` from each `brief.txt`, `card` from each `card.json`, new `modernWorks` and the worded entry-field changes from each `Card_Edits.md` (teasers, dates, `why`, `floorNote`, `legacy`, `sourcing`, `voices`, `relationsSummary`, Pontius's `regions`).
- **"The Jewish people" rule** on Tacitus, Origen, Suetonius and Anatolius: 41 changes in brief, card and two Suetonius entry fields. Printed wording untouched. Each is in the story's `Revision.md` and `Card_Edits.md`.
- **Second readings** (SR2) on Anatolius, Hippolytus, Lactantius and Tatian (`Second_Readings.md`); the other nine from `Second_Readings_SR1.md`.
- **`tools/quote_renderings.json`**: the 47 old listings for the 13 removed, 38 new ones added. **`tools/quote_scan_readings.json`**: Mirbt line 2541 "Cliristus" reads "Christus".
- **Rebuild**: atlas-sync, tree pages and corpus coverage. The 13 pages, the index and five tradition pages changed (each lists a changed person's shown dates). The generator also rewrote `cft-website/privacy.html` with older text; it was restored from `main` and is not in the diff.
- **Ledger**: none of the 13 was in `Earlier-Approved.yaml`; `list_story_status.py --write` lists them, with Josephus, under batch 12. The merge conflict in `Story-Ledger.md` was settled by regenerating it.

## Mark's rulings and where they live

- **"The Jewish people" in the narrator's words** (2026-11-28): `Brief-Kit/Kit.md`, Part 1, Accessibility, "Plain modern words"; Decision-Log. Kit-wide.
- **The release judgment calls** ("yes", 2026-11-28), this release only, each recorded in the story's `Card_Edits.md` (and `Revision.md` for brief text) and on his record page (https://claude.ai/artifact/QZQb8kfjtZYCd6VytZwaVU):
  - Suetonius: "a Jew" for Aquila → "a Jewish man", in the brief and two card fields.
  - Pamphilus: the entry `legacy`'s "Two later worlds in the Library name him." cut.
  - Origen: "Jerome ... later called his teachings poison" kept. It is in Jerome's own words: Apology against Rufinus III ("Origen's poisoned dish", `npnf203` lines 55571-55574) and Against John of Jerusalem 25 (`npnf206` lines 41464-41468).
  - The "Asia Minor" regions (Tacitus, Suetonius, Valentinus, Tatian) and Pontius's `start` stand.

## Judgment calls at release

- **Valentinus timeline reference.** `check_live_commentary.py --enforce` flagged the census slug in the card check's worded reference to the tradition entry. The entry is already named by its title, so only ", entry valentinian-and-other-gnostic-christianities" was cut. This is a format fix only, recorded in Valentinus's `Card_Edits.md`.

## Checks

- `validate-census.mjs --atlas … --tree …`: "629 movements, 736 edges, 10 eras — 0 errors, 4 warnings" (the four are existing shortName warnings on other entries), after the merge and after the Valentinus fix.
- `node --test tools/tests/validate_census_*.test.mjs`: 124 tests, 124 pass, 0 fail.
- `check_live_commentary.py --base origin/main --enforce`: exit 0 after the Valentinus fix (3 REWRITE record-slug lines before it, one source).
- `build_tree_site.mjs`: "1778 own files …, 174 shared files, 0 mismatched", exit 0.
- From the first session, before the merge: `atlas-check` and `--edges-only` exit 0; `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs` exit 0; `check_open_gaps_numbers.py` exit 0; `check_spelling.py --enforce` 0 found; `check_standard_lock.py` no locked file changed; `profile_readability` 13 briefs, 0 failing (Suetonius re-graded after the ruling: grade 9.0, 0 failing).

## Reviews

Each story's three review counts are in its own folder (`Review.md`, `Recheck_Review.md`, `Fresh_*.md`). They were not re-tallied at release.

## Cost

Telemetry, not a bill: the session records' `cost_usd`. First release session (`session_01JMNsSDcFQXR3ndvDbRVu4u`): $6.14. This session (`session_01JMNsSAeDenFyzgYiMQUQXd`): $2.02 when this was written, before the PR and merge. Total about $8.16, plus the PR steps.

## Not done

- No audio recorded.
- The generator's rewrite of `privacy.html` is open: Open-Gaps, "The tree-page generator rewrites the privacy page with older text" (2026-11-28).
- Two of the 13 are checked on churchfamilytree.com after the merge; the result goes to the managing session.
