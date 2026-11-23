# Batch 10: fresh-read fixes, independent check

Checked against Decision Log, 2026-11-23, "Batch 10: the fresh read, and the fixes after it". For each story: `diff <slug>.brief.v2.txt <slug>.brief.txt`, a search of the final text for each new wording (each found exactly once, and each removed wording absent), a straight read of the final brief, a scan for new repeated four-word runs and doubled words, and `python -m engine.m1.profile_readability`. The `Fresh_Read_Applied.md` reports were not relied on.

- **council-of-ephesus-431: VERIFIED.** Minors 1, 2 and 3 and trim 1, word for word. Nothing else changed. 585 words, pass.
- **eutyches: VERIFIED.** B1, M1 (as reworded by T2), M2, M3, M5, T1 and T2, word for word. Nothing else changed. 675, pass. Skipped: M4. The reason given ("no exact wording for the brief") does not fully hold. The fresh read gave a fallback: if the researcher adds no supporting line to the outline, "one Christ against Nestorius, and the creed of Nicaea with nothing added" → "one Christ against Nestorius". The outline still cites only Zach 1167-1172 and 4095-4097 for that clause. This stays open for the researcher step.
- **theodoret-of-cyrrhus: VERIFIED.** Blocking 1 and 2, word for word. Nothing else changed. 675, pass. Minor 1 ("no change needed") and minor 2 (only if words are free, and the brief is at 675) were rightly left.
- **pelagius: VERIFIED.** Findings 1 (with the paragraph move now made: the essence is paragraph 2 and the warning paragraph 3), 2 and 3, word for word, as `Craft_Pass_Check.md` rechecked. Nothing else changed. 674, pass.
- **john-cassian: VERIFIED.** The three minors and the offsetting cut "His books went on.", word for word. Nothing else changed. 674, pass. The "twenty-four" tie was rightly left ("no change required").
- **john-chrysostom: VERIFIED.** Only "That year the emperor's chief eunuch" → "Not long before, the emperor's chief eunuch". Nothing else changed from v2. 353, pass. Findings 2 and 3 were left, per the ruling.
- **rufinus-of-aquileia: VERIFIED.** Blocking 1 and minor 1, word for word. Nothing else changed. 675, pass. Minor 2 is marked optional and minor 3 is for the card, so both were rightly left.
- **frumentius: VERIFIED.** Minors 1, 2 and 3, word for word. Nothing else changed. 675, pass.
- **mesrop-mashtots: VERIFIED.** Minors 1 to 4 and trims 1 to 9, word for word. The doubled "who named him a preacher" is gone. Nothing else changed. 674, pass.
- **ulfila: VERIFIED.** Minor 2 (with "usual date" and "the name Homoian") and minor 3, word for word. Nothing else changed. 669, pass. Minor 1 was offered only "if a change is wanted", so it was rightly left.
- **priscillian: VERIFIED.** Finding 1 and its three offsetting cuts, finding 4, and trims 1 to 8, word for word. No trailing space is left. Nothing else changed. 675, pass. Findings 2 and 3 are now in, through trims 1 and 2. The `Fresh_Read_Applied.md` file still lists them as skipped and gives 676 words, so that report is stale. The matching clause for Story beat 1 is in `Outline.md`.
- **ephrem-the-syrian: VERIFIED.** Minor 1, "he says" → "Sozomen says", word for word. Nothing else changed from v2. 338, pass. Minor 2 goes to the second-reading step.

No sentence is doubled, broken or half-replaced, and no change makes the text next to it wrong. All twelve pass the scorer within their caps.
