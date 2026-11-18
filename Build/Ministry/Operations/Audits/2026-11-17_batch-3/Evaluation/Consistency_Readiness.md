# Batch 3: consistency, quality and release readiness (2026-11-18)

One reader of four. This one checks consistency across the twelve, release readiness, the process and the exit criteria. It was run cold. It read the kit at git tree `49e3fb2f`, the batch folder, the Decision-Log entries of 2026-11-17 and 2026-11-18 on batch 3, Open-Gaps 326 and the first twelve's folders. It read no other evaluation file.

Method:
- Word counts and readability come from `python -m engine.m1.profile_readability`, run on each `<slug>.brief.txt`.
- Heard time uses Neo at about 164 words a minute for people and Daniel at about 137 for councils. These are the voices ruled for each kind (Decision-Log, "Audio review", 2026-11-17).
- The census test went further than reading. A scratch copy of `cic-website/data/world-census.json` was made in the session scratchpad, with each brief as `longDescription` and each card as `card` or `council`. `node tools/validate-census.mjs` was run on that copy three ways: as the cards stand, with `--skip-quotes`, and in full. The live census was also run in full, and it gives 0 errors. The census itself was not touched.

## 1. Consistency across the twelve

### Length, against the outline and the voice

| Piece | Outline | Words | Over the outline | Heard (voice) | Card `briefLength` | Card against heard |
|---|---|---|---|---|---|---|
| justin-martyr | 400–450, toward 3:00 | 471 | +5% | 2:52 (Neo) | 3:10 | +18 s |
| vardan-mamikonian | 400–450, 2:30–3:00 | 492 | +9% | 3:00 (Neo) | 3:15 | +15 s |
| moses-the-black | ~300, 2:00 | 333 | +11% | 2:02 (Neo) | 2:10 | +8 s |
| alopen | ~150, 1:00 | 170 | +13% | 1:02 (Neo) | 1:10 | +8 s |
| council-of-chalcedon-451 | 450, 3:00 (Mark: 560) | 560 | +24% (at Mark's 560) | **4:05 (Daniel)** | 3:45 | −20 s |
| third-council-of-toledo-589 | ~430, toward 3:00 | 501 | +17% | **3:39 (Daniel)** | 3:20 | −19 s |
| john-wyclif | ~380, 2:30 | 420 | +11% | 2:34 (Neo) | 2:50 | +16 s |
| thomas-a-kempis | ~375, 2:30 | 399 | +6% | 2:26 (Neo) | 2:40 | +14 s |
| narsai | ~375, 2:30 | 410 | +9% | 2:30 (Neo) | 2:45 | +15 s |
| pachomius | 400–450, 2:30–3:00 | 478 | +6% | 2:55 (Neo) | 3:10 | +15 s |
| arius | ~400, 2:30–3:00 | 457 | +14% | 2:47 (Neo) | 3:00 | +13 s |
| baudonivia | ~300, 2:00 | 347 | +16% | 2:07 (Neo) | 2:10 | +3 s |

What this shows:
- **Every brief runs past its outline's word figure.** The median is 11% over. Five are within 10%: Justin, Vardan, Kempis, Narsai and Pachomius. The outlines set words at about 150 a minute, which matches neither voice. Neo reads faster, so all ten people land inside their outline's minutes when heard. Daniel reads slower, so both councils land outside theirs.
- **The two councils run long in Daniel's voice.** Mark allowed Chalcedon 560 words as "about 3:45" (Decision-Log, 2026-11-18). In Daniel's voice it is about 4:05, longer than Nicaea's 3:50, which Mark allowed in release 50. Toledo, at 501 words, is about 3:39. Its length was never put to Mark: recheck 2 called it acceptable. The Standard says "up to three" minutes.
- **The cards' `briefLength` is wrong in a consistent way.** It was worked out at about 150 words a minute. So it overstates every person by 3 to 18 seconds and understates both councils by about 20 seconds. The census does not accept the field (see section 2), so this matters only as a record, and as the source of the "3:45" Mark ruled on.
- **Vardan's length ruling cited a line that is no longer in force.** The coordinator passed Vardan's 492 words as "inside the Standard's 3:30 ceiling" (Ledger). That ceiling is the 2026-11-16 length line, which the 2026-11-17 kit replaced with "up to three". The outcome stands, because Vardan is 3:00 in Neo's voice. The reason given is wrong.

### Readability

All twelve pass the hard limits.

| Piece | Grade (names out) | Reading ease, names out | Words a sentence | Longest sentence |
|---|---|---|---|---|
| justin-martyr | 7.2 (6.5) | 77.5 | 16.2 | 30 |
| vardan-mamikonian | 8.0 (7.0) | 73.8 | 16.4 | **38** |
| moses-the-black | 7.0 (6.4) | 78.8 | 16.6 | 28 |
| alopen | 8.0 (7.8) | 69.6 | 17.0 | 25 |
| council-of-chalcedon-451 | 9.3 (7.8) | 66.0 | 15.1 | 31 |
| third-council-of-toledo-589 | 9.8 (8.8) | 64.8 | 18.6 | 26 |
| john-wyclif | 8.3 (7.7) | 73.9 | 19.1 | 31 |
| thomas-a-kempis | 7.6 (6.4) | 77.3 | 16.0 | 30 |
| narsai | 8.1 (6.3) | 78.1 | 15.8 | 26 |
| pachomius | 7.8 (6.7) | 77.7 | 17.1 | 32 |
| arius | 8.2 (7.2) | 72.7 | 16.3 | 25 |
| baudonivia | 8.1 (6.7) | 77.6 | 17.4 | 29 |

- Four briefs score under grade 8: Justin, Moses, Kempis and Pachomius. Under the Standard, that is a matter for the listener read, not a fault.
- Toledo, at 9.8, is the closest to the grade 10 limit.
- Vardan's opening sentence is 38 words, past the Standard's "about 30". The reviewer's MINOR 6 gives the fix, which changes no words: end the narrator's sentence at "saw another meaning." and let the quotation stand as its own sentence. Vardan passed by ruling, so the fix was never made. It costs nothing to make before recording.

### Card shape

- **Ten cards share one shape:** the census person keys or council keys, plus `briefLength`.
- **Wyclif and Kempis are in the era 6 profile shape.** They carry `name`, `dates`, `place` and `tradition` where the census has `datesNote` and `placeNote`, and no census card exists for them. Their content is fine, but their shape is not the census shape.
- **Key order varies.** Vardan puts `quotationOriginals` before `briefReferences`, and Chalcedon puts `briefLength` last. This is cosmetic.

### Quotations, entries and second readings

- The twelve briefs hold 56 quoted spans. The cards hold 53 `quotationOriginals` entries, because some entries cover a quotation the brief breaks around "he says".
- **One span has no entry:** Arius's "Arian", the label his opponents used, in paragraph 6. The census check rejects it. The second readings and both card checks missed it, because the card check's scratch run set aside quotation errors.
- Every entry has a verdict from the blind second reading: 35 same, 18 minor, 0 changes meaning. One reading did change the meaning, Arius Q2 ("as atheists"). It was re-rendered as "as godless men" in both the brief and the card before the verdicts were set.
- The Ledger's "52 quotations" is a miscount. The requests give 25 + 26, plus 2 terms read later, which makes 53, the number on the cards.
- After the ending recasts, Alopen's and Baudonivia's cards still match their briefs. No quotation changed, and their `briefReferences` still hold.

### One fact checked independently

The card writer found that Kempis's brief dated the Utrecht interdict to 1429. The coordinator corrected it to 1425, with the departure in 1429, and no independent hand checked that correction. I checked it here against the Chronicle: the entry for 1425 begins at `kempis_chronicle-of-mount-st-agnes_arthur1906.txt` l.1777, the interdict is at l.1815–1829, and the departure is under 1429 at l.1883–1890. **The correction is right.**

## 2. Release readiness

### The census check, run on a scratch copy

**As the cards stand, with `--skip-quotes`: 21 errors.**
- `briefLength` is not an allowed key on any person card or council (12 errors). The census holds no `briefLength` anywhere. The first twelve dropped it at release.
- Wyclif and Kempis: `card.name`, `card.dates`, `card.place` and `card.tradition` are not allowed (8 errors).
- Arius: the quotation "Arian" has no entry (1 error).

**With those keys removed: 1 error left** (Arius's "Arian"). Every printed wording stands at its file and lines. Every original and English companion stands where it is cited. Every source file exists under `cic/texts/` and every verdict is valid. `briefReferences` passes as strings, and every council field passes.

**In full, with keys removed: 50 errors, all of them quotations not found verbatim.**
- **About 38 are brief quotations rendered into our English.** Each needs a listing in `tools/quote_renderings.json`, with its original file (already among the card's sources) and its second-reading record (`Second_Readings.md`, `_2`, `Blind_3`). This is the release step release 50 did for 37 renderings. None is listed yet for these twelve.
- **About 11 are quoted wordings the card writers added inside `briefReferences`.** They are labels, paraphrases or our English, and they do not stand in the files:
  - Justin: "in my stupidity"
  - Moses: "the late 300s"
  - Narsai: "Narses Leprosus" and "Edessa grew dark; Nisibis grew bright"
  - Baudonivia: "not polished, but rustic", "her eyes were closed, and ours were darkened" (lower case, so it differs from the brief's listing), "you will pardon good Baudonivia, who confesses her weakness" and "a little after 600"
  - Arius: three quotations repeated from the brief
  - Toledo: "by reason rather than command"

  Release 50's answer was to tell such lines as plain notes. The alternative is to list each one as a rendering.
- **1 is a scan fault on Wyclif's card**, which has never been through the census. Shirley's "If considered only as the father of English prose…" reads "tlie" for "the" at `fasciculi-zizaniorum_shirley1858.txt` l.2856. It needs a line in `tools/quote_scan_readings.json`.

None of the 50 is a content fault. All are the kind of release work release 50 did ("Made to pass the census check", Decision-Log 2026-11-17). They have to be done, though, and the full check must reach 0 errors.

### Open-Gaps 326

- **Bullet 1 is stale.** It still says the three held pieces "come to Mark", with word counts since replaced (552, 481 and 473 words; the final briefs are 501, 478 and 560). What happened after it is not in Open-Gaps: the second revision on Opus, Mark's fixes, the final checks that passed, and the drift recasts. The entries are append-only, so a new entry has to record the outcome.
- **Bullet 2, Arius's claim not found:** open. The card rule lets it stay. It does not block release.
- **Bullet 3, Pohl's Imitation file misnamed:** open, for the Library. It does not block release.
- **Bullet 4, the setting detector beaten by dropping dates:** open, a kit item for batch 4. It does not block release.
- **Bullet 5, Moses slotted as a thin record:** a note, not a gap.
- **Missing from 326.** Card check 2 asked for these and they were not logged:
  - Toledo's "two places in the printed text are damaged", of which only one was found (it asked for a gaps entry by name);
  - Chalcedon's "Leo's legates presided over the votes";
  - Chalcedon's "The Greek text of the definition now reads 'of two natures'";
  - Toledo's emended reading, which was upheld.

  The Chalcedon legates line also sits awkwardly beside the brief, which says the officials ran the council. Mark should see it.

## 3. The process

### Where the large corrections came from

| Step | What it caught | Pieces |
|---|---|---|
| Outline check | **Every outline failed its first check: 41 blocking faults**, 1 to 7 each. They were mostly two kinds. Witness-line faults: a side's view in the narrator's voice, an editor cited where the primary text is held, or one translator followed where others disagree (Alopen 7, Chalcedon 4 of 5, Arius 4). Misreadings: Gaunt as uncle, the Acts called contemporary, Amélineau's added name, Ardo misread. | 12 of 12 |
| Outline recheck | Slips the fixes brought in (two in Arius), leftover labels (Justin, Alopen) and an order and a citation (Chalcedon) | 4 |
| Write | Both Sonnet council drafts cut the outline's must-tell force: the idolatry canons, Priscus and the altar killings. The writers said so themselves. | 2 |
| Variety recast | **Brought in a fault.** Toledo lost Saragossa, which became blocking at review. Three writers dropped years to clear the detector. | 10 recast |
| First review | **14 blocking faults in 10 pieces.** About half were softening by omission: Alopen's opposition, Narsai's denunciation, Arius's coercion, Kempis's exile, Toledo's canon and impact, Chalcedon's violence, Pachomius's split. One outline fault got past both outline checks (Moses's "at night"). | 10 of 12 |
| Recheck | 3 failed. The revisions brought in new faults: Pachomius lost "at the start", Chalcedon got a misrendered Severus, cut must-tell material and a narrator's verdict. Toledo still lacked Saragossa. | 3 |
| Second revision (change order) and recheck 2 | All three failed again on narrow points. Chalcedon's must-tell list cannot fit its outline's 450 words. | 3 |
| Card | **A factual error in a finished brief** (Kempis 1429/1425), after the outline check, review and recheck had passed it. Four census-card corrections (Alopen 3, Kempis 1). | 2 |
| Second reading | One quotation changed meaning (Arius Q2) | 1 |
| Drift comparison (Mark's request; not a kit step) | The later-witness ending in 5 of 12, which the detector counted as 0. Two endings were recast. | 2 |

### Passes per piece

| Piece | Ledger rows | Brief versions | Route |
|---|---|---|---|
| justin-martyr | 8 | 1 | outline fix and label fix; review PASS |
| vardan-mamikonian | 7 | 2 | outline fix; recast; review PASS by the coordinator's ruling |
| moses-the-black | 9 | 2 | outline fix; revision; recheck PASS |
| alopen | 9 | 4 | outline fix; recast; revision; ending recast |
| baudonivia | 9 | 4 | the same as Alopen |
| john-wyclif | 9 | 3 | outline fix; recast; revision |
| narsai | 9 | 3 | the same as Wyclif |
| arius | 10 | 3 | outline fix and slip fix; recast; revision; Q2 re-rendered |
| thomas-a-kempis | 10 | 4 | outline fix; recast; revision; the coordinator's date correction |
| third-council-of-toledo-589 | 11 | 5 | revision; second revision; Mark's fix; final check |
| pachomius | 11 | 5 | the same as Toledo, after a Library fill |
| council-of-chalcedon-451 | 14 | 6 | revision; second revision; cut to 560; final check |

By the harness's counts, the batch ran to roughly 15 million tokens. That is about 0.9 million for each plain piece and 1.2 to 1.5 million for the three held ones, before the shared second-reading and card steps.

### Did the kit hold cold?

- **The kit itself did not change.** Its tree is still `49e3fb2f`, and its last commit (`8f9ad3ab6`) is from before the batch. The two change orders applied to this batch only: a second revision on Opus for the three held pieces, and Chalcedon allowed to 560 words.
- **The kit did not hold in five places:**
  - Step 5, one revision, failed for 3 of 12. That needed Mark twice.
  - The rule that Sonnet writes the councils failed both times, and only Opus rewrites came close.
  - The variety check can be passed by dropping a date, and a recast is never rechecked against the must-tell list.
  - The outline check does not test whether the must-tell list fits the outline's length.
  - The card role does not name the census schema: no `briefLength`, how to map era 6 keys, and quoting only printed words in references.
- **Coordinator fixes without an independent check.** There were about eight, including Kempis's date, Justin's label, Arius's slips "checked by the coordinator", and the Toledo and Pachomius sentences, which did get a final check. The project rule is that a blocking finding needs independent re-confirmation. The Kempis fix is now confirmed (section 1). The outline-level fixes used the checkers' own wording.

### Against the first twelve

- Their outlines also failed 12 of 12 first checks, but with smaller faults (1 to 3 blocking, mostly wording).
- About 4 of 12 passed their first review on the older kit. Batch 3 passed 1, or 2 with the ruling.
- **The difference is where the softening was caught.** In the first twelve, outside readers found it after release, and all twelve were revised and recorded again. In batch 3 the reviewer caught it before any recording. That is the kit working, at the cost of more passes.
- Drift is much lower (Drift_Comparison.md). The second readings that changed meaning fell from 2 of 48 to 1 of 53.

## 4. Exit criteria

| Criterion | Target | Result | Evidence |
|---|---|---|---|
| Pass first review | 10 of 12 | **Not met: 1 of 12** (2 with the coordinator's Vardan ruling) | Ledger review rows. Only Justin got PASS from the reviewer; ten got REVISE. |
| Pass the one-hearing test at first review | 12 of 12 | **Met: 12 of 12** | Every review row says "one-hearing PASS" (Chalcedon "narrowly"). |
| No quotation changes meaning at second reading | 0 | **Not met: 1 of 53** (re-rendered before release) | Second_Readings.md, arius Q2 |
| Within the outline's length | 10 of 12 | **Not met by words:** none at or under the figure, 5 within 10%. **Met by heard time:** 10 of 12, the councils over. | Section 1. The batch's own reviews measured words. |
| No opening or ending move in more than 3 of 12 | variety check | **Met by the check**: run 2 all at 3 or under. The later ending is 3 of 12 by hand after the recasts. **Caveat:** by hand, two other moves are at 4 of 12: opening on a source's words (Alopen, Arius, Baudonivia, Moses) and ending on the death (Kempis, Vardan, Arius, Moses). The Standard allows a death ending. | Variety_Check_run2.txt; Drift_Comparison.md; the openings and endings read for this report |
| Mark passes all 12 by ear | 12 of 12 | **Not yet run.** Nothing is recorded. Recording waits for a finished batch (2026-11-17 ruling). | Ledger; Decision-Log |

The README's Result column is still blank.

## Verdict

**The batch: ready to record and release after named fixes.** No content fault is open. Every blocking finding was resolved and checked. The must-fixes:

1. **Make the census check pass, 0 errors in full:**
   - drop `briefLength` from all twelve;
   - map Wyclif's and Kempis's era 6 keys to `datesNote` and `placeNote`, word for word, and reconcile `name` and `tradition` with the live entries;
   - give Arius's "Arian" an entry, or drop its quotation marks;
   - list about 38 renderings in `tools/quote_renderings.json` with their second-reading records;
   - turn the 11 quoted labels and paraphrases in `briefReferences` into plain notes, or list them;
   - add the "tlie" scan reading for Wyclif.
2. **Before the paid run, put the councils' real lengths in Daniel's voice to Mark:** Chalcedon about 4:05, not the 3:45 he ruled on, and Toledo about 3:39, never ruled.
3. **Append an Open-Gaps entry.** It records the outcome of the three held pieces, the drift recasts and Kempis's date. It also logs the four flagged card claims: Toledo's damaged places and emended reading, and Chalcedon's legates and "of two natures".

Recommended, not blocking: Vardan's 38-word sentence split at "saw another meaning." (no words change), and Mark's look at Chalcedon's legates line beside its brief. Exit criterion 6 is Mark's ear, after recording.

**The kit: not ready to scale toward 500.** At this batch's rates, 500 pieces would mean about 125 coming to Mark, and more than 400 failing their first review. These must change first:

1. **Councils are written on Opus.** Sonnet cut the must-tell force in both councils, twice. This is a model-rule change, for Mark.
2. **Outline length is set in each voice's words a minute,** and the outline check tests that the must-tell list fits it.
3. **The variety check counts moves by kind, not by date markers.** A recast gets a targeted must-tell recheck.
4. **The card role and card check carry the census schema.** The card check runs the full census check with draft renderings, so a missing entry like "Arian" shows up.
5. **Every coordinator fix gets an independent confirmation,** recorded in the batch.
