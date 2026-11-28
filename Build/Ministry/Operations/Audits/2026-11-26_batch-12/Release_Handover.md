# Release 13: handover

The release thread stopped here because its context passed 150,000 tokens. The work is on branch `claude/cft-release-batch12-13`, committed and pushed. No pull request is open. The Artifact page for Mark is published (https://claude.ai/artifact/QZQb8kfjtZYCd6VytZwaVU) and the managing session has the link.

## Done

1. **Branch** from `main` at d729d319 (kit PR #1842 merged). The 13 folders and the batch's `Second_Readings*.md` files were brought in from `claude/batch12-era1-persons`.
2. **"The Jewish people" rule** on Tacitus, Origen, Suetonius and Anatolius: 41 changes in brief, card `modern` and narration fields, and two Suetonius entry fields (`teaser`, Mirbt's `modernWorks` note). Printed wording untouched. Each change, old beside new, is in the story's `Revision.md` and `Card_Edits.md`, "after review, carrying out Mark's ruling". No work title in the four needed the own-title rule.
3. **Second readings** (SR2) set on Anatolius, Hippolytus, Lactantius and Tatian, with the two `uncertain` notes (Tatian [1], Otto 1851; Anatolius [0], Schwartz's νήπια), checked at the cited lines. Recorded in each `Card_Edits.md`.
4. **Census** (`cic-website/data/world-census.json`), the 13 entries only: `longDescription` from each `brief.txt`, `card` from each `card.json` (each census card first checked equal to `Card.existing.json`), new `modernWorks` from each `Card_Edits.md` "Entry fields" section with the card checks' fixes, and every worded entry-field change those sections give (teasers, dates, `why`, `floorNote`, `legacy`, `sourcing`, `voices`, `relationsSummary`, Pontius `regions`). The script is reproducible from the folders.
5. **`tools/quote_renderings.json`**: the 47 old listings for the 13 removed; 38 new ones added, one per span the validator found not verbatim. Records: `Second_Readings_SR1.md` (nine stories) or `Second_Readings.md` (the four SR2 stories). "Checked at card" spans are listed as "same", as batches 8 to 10 did.
6. **`tools/quote_scan_readings.json`**: one reading added, Mirbt line 2541 "Cliristus" reads "Christus" (Tacitus Q1; the card check upheld it against Hooker's print).
7. **Rebuild**: atlas-sync, tree pages, corpus coverage. The 13 pages, the index, and five tradition pages changed (each lists a changed person's shown dates). `cft-website/privacy.html` was also rewritten by the generator with older text; it was restored from `main` and left out.
8. **Ledger**: none of the 13 was in `Earlier-Approved.yaml`; `list_story_status.py --write` moved them to batch 12 in `Story-Ledger.md`.

## Checks seen passing before the stop

- `validate-census.mjs --atlas … --tree …`: "629 movements, 736 edges, 10 eras — 0 errors, 4 warnings" (the four are existing shortName warnings on other entries).
- `atlas-check` and `atlas-check --edges-only`: exit 0, no changes.
- `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs`: exit 0.
- `check_open_gaps_numbers.py`: exit 0. `check_spelling.py --enforce`: 0 found. `check_standard_lock.py`: no locked standard file changed.
- `profile_readability`: all 13 briefs graded, 0 failing.

## Still to do

1. Run and read: `node --test tools/tests/validate_census_*.test.mjs`; `python tools/check_live_commentary.py --base origin/main --enforce`; `node tools/build_tree_site.mjs`.
2. Josephus (`claude/cft-story-josephus`) had not merged at the stop. Once it has, merge `main` into this branch, then rerun atlas-sync, the tree pages and the checks.
3. Write `Release.md` in this folder from this handover, with the cost.
4. One draft PR into `main`, pushed once after the checks pass, then marked ready; merge on green CI; check two of the 13 on churchfamilytree.com; send the managing session the merge note with the cost.

## Judgment calls, for Mark to keep or strike

- **Suetonius, "a Jew"** (Aquila; brief and two card fields) is singular and outside the ruling's wording, so it stands.
- **Pamphilus `legacy`**: the card edits call "Two later worlds in the Library name him." builder's wording but give no replacement, so the sentence stands. Only the worded "Eusebius's Apology" change was made.
- **Origen `legacy`**: "Jerome ... later called his teachings poison" was not found at the lines checked, but no change was worded, so it stands.
- **Regions** flagged "Asia Minor" with no change worded (Tacitus, Suetonius, Valentinus, Tatian) stand. Only Pontius's, which its card check passed, changed.
- **Pontius `start`** stays as it is; the card edits left it to release, and the shown `dates` carry the years.

## Cost

About $10 at API rates, worked from the token counts in this session's transcript (48k output, 16.1M cache read, 180k cache write). It is telemetry, not a bill. The session record's `total_cost_usd` is the measure to report.
