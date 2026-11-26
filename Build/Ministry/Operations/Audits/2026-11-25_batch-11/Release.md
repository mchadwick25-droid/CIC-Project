# Release: batch 11, the twelve remaining tradition briefs

Mark's release ruling (2026-11-26, "yes"), under `Release_Prompt.filled.md`. The twelve: `alexandria-catechetical`, `antiochene-church-third-century`, `roman-church-third-century`, `apocryphal-and-pseudepigraphal-literature`, `ebionite-nazoraean-current`, `greek-apologists-second-century`, `latin-apologists`, `latin-pastoral-congregational-christianity`, `manichaeism`, `marcion-marcionism`, `post-apostolic-house-church`, `syriac-edessa-nisibis`. Montanism was released earlier (`montanism-the-new-prophecy/Release.md`) and nothing of it was touched. Not committed; no audio recorded.

## The briefs before release

Each brief's `wc -w` and scorer line match the last applied file (`Grade3_Fixes_Applied.md` for Roman Church and Syriac; `Grade2_Fixes_Applied.md` for Alexandria, Antioch, Greek Apologists, Latin Apologists, Manichaeism, Marcionism and the House Church; `Craft_Check.md` for Apocryphal; `Craft_Pass_Shape.md` for the Ebionites; `Fresh_Read_Applied.md` for Latin Pastoral). Greek Apologists' "honor" is in (`Card_Edits.md`, Spelling). Nothing differed, so the release went ahead.

| Brief | `wc -w` | Scorer |
|---|---|---|
| Alexandria | 628 | 625 words, grade 9.7 |
| Antioch | 665 | 665, 8.0 |
| Roman Church | 675 | 673, 8.1 |
| Apocryphal | 665 | 664, 8.3 |
| Ebionites | 667 | 664, 8.3 |
| Greek Apologists | 675 | 675, 8.4 |
| Latin Apologists | 673 | 671, 9.1 |
| Latin Pastoral | 772 | 769, 8.2 |
| Manichaeism | 840 | 833, 8.6 |
| Marcionism | 656 | 657, 9.6 |
| House Church | 672 | 672, 7.4 (under 8) |
| Syriac | 654 | 647, 7.5 (under 8) |

## What changed

**Step 1: the cards and the brief spellings.**
- Every FIX in each governing check is applied word for word: `Card_Check2.md` for Antioch (2 entry fields), Roman Church (PASS) and Syriac (2 card, 6 entry-text); `Card_Check.md` for the other nine (Alexandria 6, Apocryphal 9, Ebionites 4, Greek Apologists 1 (FIX 2 already applied), Latin Apologists 4, Latin Pastoral 11, Manichaeism 9, Marcionism 4, House Church 14).
- Card-field fixes went into each `<slug>.card.json`. Fixes to a held `modernWorks` went into that card's `Card_Edits.md` block: Alexandria FIX 1 and 4, Ebionites FIX 4, House Church FIX 10. House Church FIX 13 and 14 (record only) went into its `Card_Edits.md`.
- `secondReading` set on all 38 second-read entries from `Second_Readings.md` (22 same, 16 minor, 0 meaning). No reading changes meaning, so no brief rendering changed and no sentence goes for a targeted check.
- Spelling, brief and card `modern` together: Latin Apologists "laboured" and "favours" become "labored" and "favors" (backup `latin-apologists.brief.v5.txt`); House Church "neighbour" becomes "neighbor" (backup `post-apostolic-house-church.brief.v6.txt`). Word counts unchanged. The printed sources keep their own spelling.
- Ebionites `quotationOriginals[5]` (B11-16): `printed` now opens "qui credunt in", and `uncertain` says the edition's notes, page number and running head between the two lines are left out. See judgment call 1 on the line number.
- House Church FIX 7: the Greek `printed` now carries the file's own accents (oxia), checked equal to the old text under NFC.

**Step 2: the census (`cic-website/data/world-census.json`).** No new entries, keys, links, edge notes, map stories or narration. Fields changed, besides `longDescription` (each final brief, final newline removed):

| Entry | Fields |
|---|---|
| Alexandria | `legacy`, `voices` (FIX 2), `relationsSummary`; `entry.tile`, `intro`, `summary`, `recordHolds` (FIX 6) |
| Antioch | `sourcing`, `floorNote`, `voices`, `legacy`, `why` (edit 10 + FIX 2), `teaser` (17), `relationsSummary` (18 + FIX 1), `documentedStories` (14, 19-21; Williams and Mayer to the story's `modernWorks`) |
| Roman Church | `why`, `sourcing`, `teaser`, `voices`, `legacy`, `documentedStories` |
| Apocryphal | `voices`, `legacy`, `why`, `teaser`, `relationsSummary`, `documentedStories` (writer's edits + FIX 4-9; Foster and Ehrman to the stories' `modernWorks`) |
| Ebionites | `floorNote`, `voices`, `legacy`, `why` (FIX 1 + edit 10), `teaser`, `relationsSummary`, `peopleNote` |
| Greek Apologists | `why`, `teaser` (FIX 1), `voices`, `legacy`, `documentedStories`, `livingEvidence.basis` |
| Latin Apologists | `why`, `sourcing`, `floorNote`, `relationsSummary`, `teaser`, `voices`, `legacy`, `documentedStories`, `region` |
| Latin Pastoral | `why`, `teaser`, `voices`, `legacy`, `documentedStories`. No `entry` (not a built world; `Entry_Texts.not-applied.md` not applied) |
| Manichaeism | `voices`, `legacy`, `documentedStories` (BeDuhn to the story's `modernWorks`), `why`, `teaser` (edit 9 + FIX 2), `floorNote` (FIX 1) |
| Marcionism | `legacy`, `documentedStories`, `why`, `teaser`, `relationsSummary`, `dates` "2nd-5th c.", `end` 450 (FIX 3), `livingEvidence.basis` (FIX 4) |
| House Church | `why`, `sourcing`, `voices`, `legacy`; `entry.tile`, `intro`, `summary`, `recordHolds` (FIX 11, 12) |
| Syriac | `voices`, `legacy`, `why`, `relationsSummary`; `entry.tile`, `intro`, `summary`, `recordHolds` (FIX 3-8) |

**Step 4: rebuild.** `atlas-sync` changed only `cft-website/index.html` (the batch's records). `generate_tree_pages.mjs` changed only the twelve batch pages. `corpus_coverage.py` left `corpus-coverage.json` unchanged (629 entries, 303 with vendored coverage). Nothing else changed. The old "Audio Brief" players no longer show on the eight pages that had one, since the recordings no longer match the text; they return when the new recordings are made.

**Step 6: the ledger.** `Earlier-Approved.yaml` holds no entries, so nothing was removed. `python tools/list_story_status.py --write` left `Story-Ledger.md` unchanged: all thirteen batch 11 slugs stay under "On the kit, not in the census", because the tool counts only persons and councils (Open-Gaps 425).

**Open-Gaps.** 425 (story ledger and status tool), 426 (validator quotation checks), 427 (`quote_renderings.json`), 428 (where a tradition's card lives), 429 (timeline years no source gives), 430 (the kit's "brief" wording), 431 (card claims left as not found). Pliny's Book 10 is already entry 309 ("Library, Pliny the Younger's letter to Trajan", 2026-11-16), so no new entry; the House Church's province stays unnamed until it is vendored.

## Held, not applied

- **Card fields with no home on a tradition** (Open-Gaps 428): `sources`, `quotationOriginals` (now with `secondReading`), `uncertain`, `briefReferences`, and each entry-level `modernWorks`, for all twelve. Alexandria, Syriac and the House Church already have a census `sources` list; it stays as it was, though their cards' `sources` changed.
- **Step 3, `tools/quote_renderings.json`: nothing listed**, as for Montanism (Open-Gaps 427). The listings are ready: 43 of the twelve cards' 45 `quotationOriginals` need one (the 38 second-read ids B11-01 to B11-38 in `Second_Reading_Key.md` less B11-07 and B11-26, which are word for word in their cited English prints, plus the seven "checked at card" spans: Ebionites [2] and [3], Manichaeism [0]-[2], Marcionism [2], Syriac [3]). Each carries its file, lines and `secondReading` on the card, with record `Second_Readings.md`, and the American spellings. They wait on the ruling on where tradition cards live.
- **Dates no source gives**, listed for Mark (Open-Gaps 429): Latin Apologists `end` 320 and the years 205 and 250; Apocryphal `dates` c. 100-900; Marcionism `start` 140; Ebionites `dates`, `start`, `end` and `region`, with the three options its check gives.
- **Latin Apologists `dates` "c. 200-320" and `start` 200, passed by its check but held.** Applied, they made the validator fail: `start` 200 ties Latin Apologists with the Roman Church at the head of the Latin river, and the rule then wants that river's origin changed from Tertullian's declared parent to the House Church's "continued as" link to the Roman Church. That is a map change, not a mechanical fix, so both fields are back at "c. 197-320" and 197 for Mark (Open-Gaps 429).
- **Passed card text that contradicts the final brief:** none found. The checks were made against the final briefs.
- **Noted by the checks, already live, not changed:** Antioch's documented story keeps "7 January 312", "nine years" and "used across the Greek East for centuries"; Marcionism's documented story still says its primary text is "not yet read"; the House Church's `voices[5]` "met in their homes" and its and Syriac's entry `topics`; Manichaeism's `experienceToday` (Open-Gaps 431).

## Judgment calls

1. **Ebionites B11-16 line number.** `Second_Readings.md` puts "qui credunt in" at the end of line 23239. It stands at line 23237 (`grep -n`; the card's own `uncertain` already names line 23237 for the Nazaraei). I wrote `lines` "23237-23275" and named 23237 in the `uncertain` sentence, rather than copy a wrong line. Worth one independent look.
2. **`peopleNote` (Ebionites) and `region` (Latin Apologists)** are not in the release header's field list, but each is an existing field, the change is in `Card_Edits.md`, and the check passes it. Applied.
3. **Card fields kept in the card file** (`sourcing`, `voices`, `legacy` and the rest) were copied from the card to the census where the entry has the field and the card differs.
4. **One Open-Gaps entry for the ledger and the status tool**, not two: `Story-Ledger.md` is what `list_story_status.py --write` writes, so they share one cause.
5. **Card checks' "for Open Gaps" lists** (Alexandria's unsourced judgments and the rest) went into one entry, 431.

## Checks (step 5)

| Check | Result |
|---|---|
| `node tools/validate-census.mjs --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` | `629 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four standing shortName warnings). The first run, with Latin Apologists' `start` 200, gave 1 error (river origin 5); see Held. |
| `node --test tools/tests/validate_census_*.test.mjs` | `tests 122, pass 122, fail 0` |
| `python -m engine.m6.cli atlas-check` | `"changes": []` |
| `python -m engine.m6.cli atlas-check --edges-only` | `"changes": []` |
| `node tools/build_tree_site.mjs` | `tree site: 1778 own files (the map page slimmed, 629 card files added), 174 shared files, 0 mismatched` |
| `node --test cic-worker/worker.test.mjs Build/tools/generate_tree_pages.test.mjs` | `tests 82, pass 82, fail 0` |
| `python tools/check_live_commentary.py --base origin/main --enforce` | exit 0, nothing flagged |
| `python tools/check_open_gaps_numbers.py` | exit 0, no output |
| `python tools/check_spelling.py --enforce --base origin/main` | `0 British spelling(s) found in 0 file(s); 0 in enforced trees` |
| `python -m engine.m1.profile_readability` (the twelve briefs) | `12 brief(s) graded, 0 failing`; each line as in the table above (House Church 7.4 and Syriac 7.5 carry the under-8 note) |
| `python tools/check_standard_lock.py --base origin/main` | `No locked standard file changed.` |

No check failed on a brief's or a card's content.

## Mark's rulings in the batch, and where each lives

All from the batch README and the CFT Decision-Log. None changed a kit line; each is this batch only unless said.

- "Batch 11: the slate approved" (2026-11-25): this batch only.
- "Batch 11: hearts and lengths approved" (2026-11-25): this batch only.
- "Batch 11: lengths, up to 4:30 and cut at the outline" (2026-11-25): this batch only. A kit change for the hearts page's count would come to Mark on its own.
- "Batch 11: the first two briefs approved" (2026-11-25): this batch only.
- "Batch 11: the two long stories" (2026-11-25): this batch only. Its "Added" part (an independent grading of the 13 new texts after the batch, before batch 12) is still to do.
- "Batch 11: Montanism released alone and recorded" and "Montanism fixed and regraded before recording" (2026-11-25): this batch only.
- "Batch 11: the eight briefs, Manichaeism's length and the grade fixes" (2026-11-25): this batch only.
- "Batch 11: the two rebuilt stories ship" (2026-11-25): this batch only. A kit shape for traditions known only through opponents or writings is to come to Mark separately.
- "Batch 11: second-grade fixes" and "third grade and the two small fixes" (2026-11-25): this batch only.
- Heart wordings changed by checked fixes (README, "For the release's rulings list"): Antioch (`Fixes_Review.md`), Roman Church (`Fixes_Review.md`, `Recheck_Review.md`), Alexandria, Latin Apologists and House Church (lengths page), Ebionites (`Fixes_Review.md`), Greek Apologists ("A number of writers"), Marcionism ("called"), Latin Pastoral ("Their bishop"), Syriac (the harmony clause, `Review.md`), House Church ("met together", `Trust_Second.md`). Each lives in its outline only.
- Bearing on the kit, not yet in it: "The audio introduction is a brief, not a story" (2026-11-25; the kit wording is Open-Gaps 430); "The card design: one layout, and a timeline in periods" (2026-11-25; the kit and the card role change after batch 11); "Recording settings for tradition briefs" (2026-11-25), which lives in `Brief-Kit/Recording_Settings.md`.

## Reference counts beside the batch's

There is no `Reference_Read.md`. The tradition kit names no reference stories of its kind, and `Brief-Kit/reference/` holds only the three person references (README, "Reference read"). So the batch's fresh-trust counts stand beside the person references in `reference/Scores.md`, and its faults are the batch grades.

| | Basil | Epiphanius | Chrysostom | Batch 11, the twelve (`Fresh_Trust.md`) |
|---|---|---|---|---|
| Words | 733 | 756 | 742 | 628-840 (`wc -w`) |
| Held / summary holds | 16 / 18 | 33 / 7 | 26 / 11 | 16-26 / 7-15 |
| Softened or changed | 0 | 1 | 0 | 1 each in Antioch, Latin Pastoral, Manichaeism, Marcionism; 2 in the House Church |
| Assumption added | 0 | 0 | 0 | 1 (Greek Apologists) |
| Modern only | 0 | 0 | 0 | 1 (House Church) |
| Not found | 0 | 0 | 0 | 0 |

Every blocking mark in those reads carried an exact fix, applied before the grades. The faults: the regrade (`Grades2/Grades.md`) gave 6 B, 5 C and 1 D, with no modern opinion in any brief and craft blocking faults down from 19 to 13. The third grade (`Grades3/Grades.md`) left Antioch at C; Roman Church and Syriac took their small fixes, expected B, not graded again. The person references' own listener faults (Scores.md) run 0 to 5 sentences failing on one hearing; the batch's `Fresh_Listen.md` reads (before the grade fixes) run 1 to 5, each counted minor.

## Not done

- **The new recordings.** None made, as instructed (Mark's stop on the female-voice recordings, 2026-11-26; tradition settings in `Recording_Settings.md`). The pages show no player until they are.
- **Mark's rulings:** where a tradition's card lives (428), the timeline years (429), and the Latin river origin if Latin Apologists' `start` moves.
- **The independent grading** of the 13 new texts, ruled under "the two long stories", before batch 12.
- **Not done here:** commit, pull request.
