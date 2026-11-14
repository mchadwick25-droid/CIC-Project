# R3 recheck: era 6 batch 1

Round 3, the last review round, a targeted recheck by two fresh Opus agents that had not seen the drafting or the earlier rounds, at full effort. Part 1 covers John Wyclif, Thomas à Kempis, Geert Grote, the README and Open-Gaps 264; Part 2 covers Richard Rolle, Julian of Norwich, Meister Eckhart, Johannes Tauler and Henry Suso. Each part is given as its reviewer wrote it. Neither part found a blocking point; together they found 13 minor points.

## Era 6 Who batch 1, round 3 recheck: PART 1

**Scope.** Round 3, the last round, by a fresh reviewer. It covers `john-wyclif`, `thomas-a-kempis` and `geert-grote` (brief, card, audio script and each `records.json` entry), the batch `README.md`, Open-Gaps 264, and round 2 findings R2-1-B1 and R2-1-M1 to R2-1-M21 (Part 1 of R2_recheck.md). I also checked R2_changes.md's Part 1 entries against the diff. I edited no repo file and made no web, paid or model call.

**Method.**
- **Reading.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, and lessons.md (above all section 14). I used the R3 form of era 4 batch 8 R3_recheck.md. I also read R2_recheck.md Part 1 and R2_changes.md.
- **Diffs.** I ran `git diff --word-diff 13636fb0 HEAD` on the batch. I compared the three `records.json` entries field by field between 13636fb0 and HEAD by script. Five Kempis items and two Wyclif items changed. The Grote entry did not change.
- **Sources.** I reopened every changed string's lines in context:
  - DUTHOIT l.755-778, 900-970
  - WESLEY l.955-970
  - IGN-SCR1 l.24330-24350
  - IGN l.2596-2606
  - FOUNDERS l.3810-3824, 3868-3900
  - CHRON l.1705-1745, 1920-1925, 2018-2028, 2376-2383, 3411-3421, 3778-3790
  - BENHAM l.503-511, 634-636
  - NEALE l.4714-4723, 370
  - POLLARD l.7198-7208
  - F&M l.2310-2325, 4560-4660
  - BUSCH l.308-311, 15800-15820
  - DIEP l.439-442, 464-468
  - LANG l.160-162
  - the Vaughan, Matthew and Acquoy file headers
- **Quotes.** I checked every new or changed quotation by script against its file, allowing for whitespace, case, punctuation and hyphen breaks. That covers Wesley's "Yet I had frequently much sensible comfort in reading him" and "only in Dean Stanhope's translation", Duthoit's two Bethania lines and the Stanhope line, Neale's "editions as … months", Pollard's "greatest Clerk" and Benham's "somewhat uncertain". All match. The Duthoit "Chris tian Pattern" line matches only with the space closed up, because the OCR splits the word at a line break with no hyphen. I checked it by eye.
- **Absences.** I searched all of `cic/texts/` with whitespace-tolerant patterns for "most (frequently|often|widely) copied", "copied more" and "more copied", and for "copied" in the Kempis files. In FOUNDERS and CHRON I searched for "pulse", "Stuerman" and "Lambert". In F&M I searched for "two hundred", "250", "hundred and fifty" and "number of copies".
- **Scores.** I ran `grade_text` on all eight briefs and counted words with `str.split()`. I measured sentence lengths by script in the three briefs and in every card string.
- **Audio.** I compared each script with its brief by script, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph.
- **Open-Gaps 264.** I read the whole entry and checked it against the README. I spot-checked it against the files: the Kempis items (1), (2), (3), (6), (7), (9), (10) and (11); the Grote census items on the age at death and the Busch plague; the Lollardy "two hundred and fifty"; the Library header years; DIEP l.441 and 467; and LANG l.160-162.

---

### Round 2 findings

| R2 finding | Status | Note |
|---|---|---|
| R2-1-B1 | RESOLVED | The false "only" is gone. "He records that Grote died in a time of plague" rests on CHRON l.3784-3786. "Does not say how he caught it" holds, because neither CHRON nor FOUNDERS has a pulse, Stuerman or infection at Grote's death (FOUNDERS l.3880-3888 has only "smitten by the bolt"; Stuerman is Arthur's bequest note, l.1190). "Smitten" is gone. The reviewer's wording drops Kempis's "as far as might be" (see R3-1-M2). The sentence before still has the "tells the talk" slip that R2-1-M17 fixed in the brief (see R3-1-M1). |
| R2-1-M1 | RESOLVED | "nineteen of Wyclif's conclusions". |
| R2-1-M2 | RESOLVED | "the English Wycliffite Bible … probably Wyclif's own translation" (22 words). F&M l.2319 has "This translation might probably be the work of Wycliffe himself". |
| R2-1-M3 | RESOLVED | "a stroke took Wyclif's speech". |
| R2-1-M4 | RESOLVED | "He asked why men should not do so now." "He" follows "he answered" (Wyclif). |
| R2-1-M5 | RESOLVED | The text is 16 and 19 words. Alfred Pollard is placed at his first mention on the card, and the card has no earlier bare "Pollard". POLLARD l.7205 prints "Clerk [Divine]". |
| R2-1-M6 | RESOLVED | "places Wyclif's birth" and "Shirley says Wyclif appeared". |
| R2-1-M7 | RESOLVED | It is two sentences. The verbless first sentence is the knownFor house form (compare the Kempis card). |
| R2-1-M8 | RESOLVED | The side cites SHIRLEY l.737-805, 874-875, 972-977. The claim is retitled "The Leicester chronicle under Knighton's name, hostile" and stays Documented, as the reviewer asked. |
| R2-1-M9 | RESOLVED | DUTHOIT l.761-763 has "the convent of Bethania near Arnheim", and l.773 has "sent to Bethania, to attend his brother". All three offsetting cuts were made as worded. The records add DUTHOIT l.761-763, 773, and both ranges are exact. On the card, the inserted phrase puts Duthoit just before "his brother" (see R3-1-M3). |
| R2-1-M10 | RESOLVED | "grows somewhat uncertain" in both texts (BENHAM l.634-636). |
| R2-1-M11 | RESOLVED | The card has "usually" and "used to call". This matches "ordinarie" and "solebat appellare" (IGN-SCR1 l.24342-24346), and "quem" refers back to "Thomam de Kempis". The same overstatement still stands in a records note and in Open-Gaps 264 (see R3-1-M6). |
| R2-1-M12 | RESOLVED | It is two sentences. "res a se gestas Consalvio enarrans" (IGN l.2600). |
| R2-1-M13 | RESOLVED | "Benham says" now appears once. BENHAM l.506-510. |
| R2-1-M14 | PARTLY | The birth witness adds CHRON l.2327. The "most copied" note is true now, and the NEALE l.4719-4721 range is exact. The desk note no longer narrates the change. The Wesley range l.961-968 covers the comfort line. But the 1399 note was spliced into the old text and now reads as a broken fragment (R3-1-M4). The new Wesley tie also credits Henry Lee's words to Duthoit (R3-1-M5). |
| R2-1-M15 | RESOLVED | "Kempis's Chronicle says Grote gave his Deventer house". |
| R2-1-M16 | RESOLVED | "Grote's own notes". |
| R2-1-M17 | RESOLVED (brief) | "Only Busch tells of the talk". The card's uncertain[0] still says "Busch alone tells the talk" (R3-1-M1). |
| R2-1-M18 | RESOLVED | Poole is gone, and the line ends "Foxe, with the Oxford testimonial of 1406." |
| R2-1-M19 | RESOLVED | The README sentence, as rewritten under R2-2-M12, names the trial once. The rewrite dropped Evans's "known" (R3-1-M8). |
| R2-1-M20 | RESOLVED | It is applied as worded. "Among them" makes the list an example list, so it is true even though Neale, Benham, Ingram, Wesley and others are not named. |
| R2-1-M21 | RESOLVED | R2_changes.md records each R1_changes correction without rewriting the file. A-M7 (three sentences), A-M25 and R-M1 (now Open-Gaps 264), A-M27 (two items, Poole taken out again) and K-M12 (split) each match the diff and R2's finding. |

---

### New findings

No blocking findings.

**R3-1-M1 (geert-grote, card `uncertain[0]`: the "tells the talk" slip that R2-1-M17 fixed in the brief).**
- **Problem.** "Busch alone tells the talk with Florens Radewijns that began the common life, and that Grote caught the plague from his friend Lambert Stuerman." R2-1-M17 changed the brief's "tells the talk" to "tells of the talk", but the card has the same phrase and was left alone. Adding only "of" would give "tells of the talk …, and that Grote caught", a mismatched pair.
- **Source.** BUSCH l.15805-15818 (the pulse). "Busch alone" holds: Stuerman appears in no Kempis text except Arthur's bequest note, FOUNDERS l.1190.
- **Fix:** "Busch alone tells of the talk with Florens Radewijns that began the common life. He alone says Grote caught the plague from his friend Lambert Stuerman." (15 and 12 words.)

**R3-1-M2 (geert-grote, card `uncertain[0]`: Kempis's "as far as might be" dropped).**
- **Problem.** "Kempis gives Grote's rule that those who wished to live together should earn their living by their hands and live in common." This is R2-1-B1's wording. The rule's own limit on the common life is gone, so the card makes it absolute. R2's evidence quoted the qualifier, and its fix wording then left it out.
- **Source.** FOUNDERS l.3818-3821: "if any should wish to abide continually together, they should earn their own living by the labour of their hands, and, as far as might be, live in common under the discipline of the Church". The records claim quotes it in full and needs no change.
- **Fix:** "Kempis gives Grote's rule that those who wished to live together should earn their living by their hands. As far as they could, they were to live in common." (18 and 11 words. Keeping the qualifier in one sentence would take it to 27 words.)

**R3-1-M3 (thomas-a-kempis, card `place`: "his brother" now follows Duthoit).**
- **Problem.** "Bethany, a convent near Arnhem in William Duthoit's account, where his brother John died." The R2-1-M9 insertion puts William Duthoit right before "his brother", so it can be read as Duthoit's brother (lessons, section 14).
- **Source.** CHRON l.2021-2026 has John end his life "in Bethany" and Thomas sent to him. DUTHOIT l.761-763 places the convent near Arnheim.
- **Fix:** "Bethany, where his brother John died, his Chronicle says. William Duthoit places the convent near Arnhem." This matches the field's own form ("Kempen, …, where he was born, his Chronicle says").

**R3-1-M4 (thomas-a-kempis, records `claims[6]`, the 1399 claim: a broken splice).**
- **Problem.** The claim now ends: "The brief keeps 'indulgences' and glosses them as remissions of penance... by the Apostolic See' in modern words." The new sentence was dropped into the middle of the old one. The tail of the old note survives, with an unmatched quotation mark. R2_changes says the note "is brought up to date" and that the fix was "Applied as worded". Neither is so (a changes log that misdescribes the change, lessons, section 14).
- **Source.** R2-1-M14's fix wording. CHRON l.1097-1106.
- **Fix:** End the claim "… and I was received with mercy.' The brief keeps 'indulgences' and glosses them as remissions of penance." Note the correction in R3_changes.md.

**R3-1-M5 (thomas-a-kempis, records `claims[30]`, Wesley: Henry Lee's words credited to Duthoit).**
- **Problem.** "Duthoit's preface names Dean Stanhope's version of the Imitation and 'Dr. Stanhope's words in his preface to the "Christian Pattern"'". These are not Duthoit's words. His introduction quotes the preface of Henry Lee's 1760 English version of the Prayers ("But in his preface the 'translator' writes thus:"). And the passage is in Duthoit's introduction, not his preface (wrong man credited, lessons, section 5).
- **Source.** DUTHOIT l.915-917 (Henry Lee, LL.B., first edition 1760), l.926-930 and l.963-964.
- **Fix:** "Henry Lee's preface of 1760, quoted in Duthoit's introduction, names Dean Stanhope's version of the 'Imitation of Christ' and 'Dr. Stanhope's words in his preface to the "Christian Pattern"', so the Christian Pattern is Stanhope's Imitation." Witness: "… DUTHOIT (…) l.915-917, 926-930, 963-964".

**R3-1-M6 (thomas-a-kempis, records `absent_details[4]` and Open-Gaps 264, Kempis item (7): Manare's "usually" still dropped).**
- **Problem.** The card was fixed under R2-1-M11, but two texts still make Manare's rule absolute. The records note says "Ignatius kept on the table of his inner room no books but the New Testament and Thomas à Kempis". Open-Gaps 264 (7) says "Ignatius kept no books on the table of his inner room but the New Testament and Thomas à Kempis". The census owner will act on the second.
- **Source.** IGN-SCR1 l.24342-24346: "ordinarie super mensam alios libros non habebat … quem solebat appellare perdicem".
- **Fix:** In both, "Ignatius usually kept no books on the table of his inner room but the New Testament and Thomas à Kempis". In the records note, also change "whom he called" to "whom he used to call". Open-Gaps 264 is on this branch and not yet merged, so its text can still be corrected.

**R3-1-M7 (Open-Gaps 264, Kempis item (6): the wording R2-1-M14 corrected in the records).**
- **Problem.** "the most copied Christian book after the Bible" …: no held line says "copied"". As written this is false. BENHAM l.505 has "He copied the Bible", and the Kempis brief says "It says he copied the whole Bible". R2-1-M14 corrected the same sentence in the records, and the README's "No held line says "most copied"" is right. I grade it minor, as R2 graded the identical records sentence. The claim behind it is true, because "most copied" is found only in the Benham file header, the Library README and REGISTRY.yaml, so the census fix it leads to is the right one.
- **Source.** Whitespace-tolerant search of all of `cic/texts/` (method above).
- **Fix:** "… no held line calls it the most copied book; Neale has it "read more widely than any other in the Western Church", Benham "the most popular religious work in Christendom" (NEALE l.4717-4719; BENHAM l.663-664)."

**R3-1-M8 (README, "Card traditions", Eckhart: Evans's "known" dropped).**
- **Problem.** "Eckhart's birth falls before, and the Paris list of 1302 that first names him falls inside." This is the R2-2-M12 wording, which also met R2-1-M19. Evans says "The first known mention of his name". The card and brief keep the hedge ("The first known mention of his name, Evans says"; "Eckhart's name first appears, Evans says"). The README drops it (hedge dropped, lessons, section 2).
- **Source.** EVANS l.496-498, as quoted in the Eckhart records claim.
- **Fix:** "Eckhart's birth falls before, and the Paris list of 1302, the first known mention of him in Evans, falls inside."

**Process note, not a finding.** Open-Gaps 264's Lollardy item is true: the census's "two hundred and fifty" copies is not in the F&M preface. But F&M do give a count, "Nearly one hundred and fifty Mss." of Purvey's version examined (F&M l.4567, 4644, across a page break). The census owner may want that line.

---

### Checks that pass, beyond the table

- **Audio.** All three scripts equal their briefs, with `[calmly] ` at the start, `[warmly] ` at the start of the last paragraph, and two tags only. The other five scripts match too.
- **Changed brief sentences against sources.**
  - Kempis para 4, "The Chronicle says one had a dream that foretold the prior's death, and leaves the dreamer unnamed", matches CHRON l.1728-1731 ("one of them had a dream … which vision did foretell the Prior's death"). "One" points back to the two brothers, and "leaves" to the Chronicle.
  - Para 6, "Bethany, a house near Arnhem", uses the brief's own word for a religious house ("the brothers' house", "a new house of canons regular"). It rests on DUTHOIT l.763. The place adds no claim, like "Kempen in the diocese of Cologne".
  - Para 3, "for indulgences, remissions of penance the pope had granted there", matches CHRON l.1097-1103.
- **Pronouns and witnesses.** Each changed sentence keeps its witness, and no fix detached one. Two checks of the new card text:
  - Grote uncertain[0]: "He records that Grote died…" has Kempis as the subject of the sentence before, and "he caught it" is Grote.
  - Kempis traces[3]: "He writes" is Manare, named in the sentence before.
- **First mentions.** Alfred Pollard (Wyclif card) and William Duthoit (Kempis card, in `dates` first) are placed at first mention. Bethany is placed in the brief and on the card.
- **Sentence length.** No changed brief or card sentence goes past 25 words. Kempis traces[3] is 25 words. The only brief sentence over 25 is the Kempis close (31 words), which is unchanged and mostly quotation, as R2 noted.
- **Writing sweep.** In every changed sentence and its neighbors I found none of the following: "X, not Y", "not X but Y", "X and never Y", colon-reveals, tails, beat lines, thesis openers, unearned adjectives, loose quantifiers or process words. Every colon introduces a quotation. Spelling is American outside quotations ("laboring"; "favourite" and "labour" appear only in source lines).
- **Cuts.** The R2-1-M9 offsets in the Kempis brief (-4 words) remove no scene or turning point. The brief still runs choir, writing, 1399, the dream and Busch, the authorship dispute, Bethany, the death notice, close.
- **False absences.** I re-searched every new "only", "alone" and "no held line" in scope. Each holds except R3-1-M7:
  - "Busch alone" (card)
  - "Only Busch" (brief)
  - "does not say how he caught it"
  - "no held line calls it the most copied book"
  - the README's "No held line says "most copied""
- **Records ranges.** Each matches the quoted text:
  - DUTHOIT l.761-763 and 773
  - WESLEY l.961-968 (comfort at l.967-968; Stanhope at l.966-967)
  - DUTHOIT l.927-930 and 963-964
  - CHRON l.2327 ("June (July)" 1448) and 2378-2380
  - NEALE l.4719-4721
  - SHIRLEY l.874-875
- **README.**
  - "404 to 405 words", "grade 5.6 to 8.3" and "Flesch Reading Ease 62.8 to 80.5" match `grade_text` across the eight briefs. The low and high ends: Rolle, Julian, Eckhart and Grote at 404, with Wyclif, Kempis, Tauler and Suso at 405; Julian FK 5.59 and Wyclif 8.29; Wyclif Flesch 62.84 and Julian 80.45.
  - The Tauler line is true: "Henry of Nördlingen" is in the brief, and "Henry Charles Lea" is on the card and not in the brief.
  - "Those points are logged in Open-Gaps for a census fix" is now true. Open-Gaps 264 carries eleven Kempis and nine Wyclif census items.
- **Open-Gaps 264.** It covers what the README says: the census differences for both live entries, Library header years and defects, Library wants, and scan corrections. The spot checks match the files, apart from R3-1-M6 and R3-1-M7:
  - CHRON l.3413-3416 (ninety-second year), 1923-1924 and 2379-2382 (sub-prior twice), 2024-2026 (a year and two months)
  - 14 `kempis_` files
  - NEALE l.370 (dated 1857)
  - CHRON l.3787 and BUSCH l.15805-15818
  - DIEP l.441 "toe GroUe" and l.467 "r383"
  - LANG l.160-162 (Engelhusen)
  - the "c. 1330-1384" and "1340-1384" headers
- **R2_changes.md, Part 1.** Every entry matches the diff except the 1399 note under R2-1-M14 (R3-1-M4). Its scores table matches `grade_text` and `str.split()` for all eight briefs.

---

### Scores

| Brief | Words | FK | Flesch | After fixes: words / FK / Flesch | Blocking | Minor | Verdict |
|---|---|---|---|---|---|---|---|
| john-wyclif | 405 | 8.29 | 62.84 | unchanged | 0 | 0 | CLEAR |
| thomas-a-kempis | 405 | 7.18 | 69.86 | unchanged (card and records only) | 0 | 4 (R3-1-M3 to R3-1-M6) | CLEAR once R3-1-M3 to R3-1-M6 are applied |
| geert-grote | 404 | 5.66 | 79.09 | unchanged (card only) | 0 | 2 (R3-1-M1, R3-1-M2) | CLEAR once R3-1-M1 and R3-1-M2 are applied |
| README | | | | | 0 | 1 (R3-1-M8) | CLEAR once R3-1-M8 is applied |
| Open-Gaps 264 | | | | | 0 | 2 (R3-1-M6 in part, R3-1-M7) | CLEAR once R3-1-M6 and R3-1-M7 are applied |

All three briefs pass `grade_text` (FK 10 or below, Flesch 60 or above). No fix touches a brief, so the audio scripts need no rebuild.

### Count

- **Round 2 findings in scope: 22** (R2-1-B1, R2-1-M1 to R2-1-M21).
  - Resolved: 21.
  - Partly resolved: 1 (R2-1-M14).
  - Not resolved: 0.
- **New findings: 0 blocking, 8 minor** (R3-1-M1 to R3-1-M8), plus one process note.


---

## Era 6 Who batch 1, round 3 recheck: PART 2

**Scope.** I rechecked `richard-rolle`, `julian-of-norwich`, `meister-eckhart`, `johannes-tauler` and `henry-suso`: the brief, the card, the audio script and the records.json entry for each, with the README lines on them and the Open-Gaps 264 items that touch them. I checked every round 2 finding in Part 2 (R2-2-B1, R2-2-B2, R2-2-M1 to R2-2-M12). I edited no repo file and made no web, paid or model calls.

**Method.**
- **Reading.** CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"); Who_Profile_Pattern.md and its 14-item checklist; lessons.md, above all section 14; R2_recheck.md Part 2; R2_changes.md; the era 4 batch 8 R3_recheck.md as the form model.
- **Diffs.** `git diff --word-diff 13636fb0 HEAD` on the five briefs, the five cards, the five audio scripts, records.json (the five entries) and README.md.
- **Sources reopened in context.** COMPER l.2085-2110; WARRACK l.2080-2100; DALGAIRNS l.1770-1792, 2848-2900; PFEIFFER l.452-462; EVANS l.1-60 (title page), 372-382, 660-700; WINK l.826-830, 5118-5180, 5240-5290; SPENER l.5374-5380; KNOX l.3478-3504, 3766-3773; BIHL l.4878-4892, 6660-6680, 8290-8298; DENIFLE-II l.34960-34963, 35290-35294, 35833-35836; DENZ l.15218-15221; CRAFT l.258-266; LANG l.263; STAGEL l.1903-1912; GARDNER l.570-585.
- **Searches.** All of `cic/texts/`, whitespace- and hyphen-tolerant, case-insensitive: Tauler (and Thauler) within 250 characters of 1361, June, Juni or "16th of June", for the new "Winkworth alone gives the place and the day"; Seeberg and Seeherg in every file, for R2_changes' "no held line gives more than his name"; Preger's Geschichte; Rolle or Hampole with 29 September, Michaelmas or xxix, for Open-Gaps 264's "Horstman alone"; Margery Kempe with Julian, for 264's "in no held file"; Tauler in Jostes and Langenberg, for 264's "no Tauler sermons vendored".
- **Quotes.** Every new or changed quotation in the briefs, cards and records, checked by script (lowercase, letters and digits only, hyphen line-breaks joined) against its cited lines.
- **Scores.** `grade_text` on each brief; word counts by whitespace split (`wc -w` miscounts "à" in the Kempis brief); sentence lengths by script for every changed string.
- **Audio.** Each script rebuilt from its brief and compared.

---

### Round 2 findings

| R2 finding | Status | Note |
|---|---|---|
| R2-2-B1 | RESOLVED | The brief now reads "Winkworth alone gives the place and the day of his death". My search found no other held file giving Strasbourg as the place of death or giving 16 June. The 1361 lines are EVANS, SPENER l.5376, McCann l.16981, GARDNER l.243, the Luther volume l.6025, and Rohricht's notice of Anna Lau ("1290 — 1361"), which gives no place or day. The records claim names the year's other witnesses. Its new "alone" now covers only the place and the day, though the card's "His last months" also gives the move and the burial as hers alone. See R3-2-M4. |
| R2-2-B2 | PARTLY | The false absence is gone, and the claim adds DALGAIRNS l.2853-2854, 2876-2878. But the new "he says only that she was alive in 1443" is not true of the note, which goes on, "She had two servants to wait upon her" (l.2877-2878). It also turns Dalgairns's "All that is known is" into the narrator's "only". See R3-2-M1. The Lampet contested side still cites only l.1777-1789 and 1810-1813, though round 2 asked for the new lines there too. See R3-2-M4. |
| R2-2-M1 | RESOLVED | COMPER l.2102-2105: the illness "had returned to the recluse shortly after the hour of Richard's departure". "Rolle, he learned, had died shortly before they began again" says that. "He" is the rider, and "they" the fits of the sentence before. 8 and 10 words. |
| R2-2-M2 | RESOLVED | WARRACK l.2088: "The First was mind of His Passion". "The remembrance of" gives "mind" in its modern sense, and the three items are now parallel nouns. 24 words. |
| R2-2-M3 | RESOLVED | PFEIFFER l.455-459: the oldest and best manuscripts are "in Übereinstimmung mit Eckharts heimats- und geburtsort, Strassburg, fast durchweg in alemannischer mundart". The card's "He finds its Alemannic dialect in the oldest manuscripts" says that, and "Strasbourg" no longer echoes "Strassburg in Saxony". The records side adds PFEIFFER l.457-459. |
| R2-2-M4 | RESOLVED | WINK l.5124-5136: he "sided with the Emperor", "did not suspend his activity" and "preached ... from Cologne to Basle". One "She says" carries all three. "At Basel his old friend" is supported by WINK l.5171 ("In Basle, Tauler met with an old friend") and by Henry's own "Afterwards I came to Basle" (l.5262-5265). That sentence is 25 words, at the limit. |
| R2-2-M5 | RESOLVED | Eckhart is now placed as "a fellow Dominican", which follows "a Dominican friar of Strasbourg" two sentences before. The applied wording "the sermons" says more than Evans's book does. See R3-2-M3. |
| R2-2-M6 | RESOLVED | "Neither shows the two men meeting." "Neither" points back to Winkworth and Evans, the two named in the item. |
| R2-2-M7 | RESOLVED | KNOX l.3484-3485: "This temptation fell upon him through an inordinate fear." "The Life says" now owns "inordinate". 15 and 9 words. The cut is recorded in R2_changes under R2-1-M21 (D-M17). |
| R2-2-M8 | PARTLY | Preger is placed, and "in his history of German mysticism" is true (LANG l.263, "Preger, Geschichte der deutschen Mystik. II Leipzig 1881"; EVANS l.687). But R2_changes says "no held line gives more than his name and page" for Seeberg, and that is false. Bihlmeyer's own literature list places him: "R. Seeberg, Ein Kampf um jenseitiges Leben, Lebensbild eines mittelalterlichen Frommen (Seuse) in protestantischer Beleuchtung, Dorpat 1889" (BIHL l.4885-4887). Neither placement has a records witness. See R3-2-M2. |
| R2-2-M9 | RESOLVED | 25 words. CRAFT l.261-264: "It became a favourite book in the cloisters at the close of the Middle Ages". "By the close ... was a favorite" keeps the sense. |
| R2-2-M10 | RESOLVED | DANIELS l.51 «MÜNSTER i. W. 1923», SPENER l.126 «Leipzig 1841,» and KNOX l.5366 «* Thoss, near Winterthur, in Switzerland,» all match by script. The witness fields now cite l.51, l.126 and l.5366. |
| R2-2-M11 | PARTLY | Every asked-for claim is added, and Rolle's duplicate "Death in 1349" is gone (the Comper and Underhill claim carries the year; the Horstman claim keeps the day). But three new ranges begin one line after their quotation does: WINK l.828-829 ("The" is on l.827), KNOX l.3769-3772 ("In conse-" is on l.3768) and BIHL l.8295-8297 ("Freund und" is on l.8294). The Bihlmeyer quotation also silently restores "Nördlingen", where the file has "Nord- lingen". The short ranges were round 2's own wording. See R3-2-M4. |
| R2-2-M12 | RESOLVED | (a) The Tauler card names "Henry Charles Lea, in his history of the Inquisition of 1888", and the brief names Henry of Nördlingen. (b) EVANS l.497-498. The sentence no longer places the trial twice. |

### New findings

No blocking findings.

**R3-2-M1 (julian-of-norwich, card uncertain "When she died": a new "only" the note does not bear out).**
- **Problem.** "In a later note, citing Blomefield, he says only that she was alive in 1443, at a hundred." The note does not say only that. It goes on to say that she had two servants. "Only" is also the narrator's word for what is Dalgairns's own claim about the record, "All that is known is".
- **Source.** DALGAIRNS l.2876-2878: "* Blomfield, 546. All that is known is that she was alive in 1443, but was a hundred years old. She had two servants to wait upon hen".
- **Fix:** "A later note of his, citing Blomefield, says all that is known is that she was alive in 1443, at a hundred." (21 words. "His" follows "J. B. Dalgairns says" in the sentence before.)

**R3-2-M2 (henry-suso, card uncertain "The chapter that accused him": Seeberg left unplaced though Bihlmeyer places him; no records witness for either placement).**
- **Problem.** "Preger, in his history of German mysticism, and Seeberg, both cited by Bihlmeyer, chose 's-Hertogenbosch in 1335." Seeberg is a bare name to a general listener (the Pattern's reading aids; lessons section 14, names left unplaced). R2_changes calls him unplaceable, but Bihlmeyer's literature list gives his book, a life of Suso. The chapter claim's witness is BIHL l.6644-6645, 6673-6675 only, and "Mystik II" there does not by itself give "history of German mysticism".
- **Source.** BIHL l.4885-4887: "R. Seeberg, Ein Kampf um jenseitiges Leben, Lebensbild eines mittelalterlichen Frommen (Seuse) in protestantischer Beleuchtung, [Do]rpat 1889, 148 S." BIHL l.6674-6675: "Preger, Mystik II, 33ff. 360 und Seeherg 144 für das Provinzialkap. von Herzogenbusch 1335" (OCR "V reg er", "Seeherg", "Hersogenbusch"). LANG l.263: "Preger, Geschichte der deutschen Mystik. II Leipzig 1881."
- **Fix:** "Bihlmeyer adds that Preger, in his history of German mysticism, and R. Seeberg, in an 1889 life of Suso, chose 's-Hertogenbosch in 1335." (23 words. It replaces the last sentence of the item, and "Bihlmeyer adds" keeps the witness on the claim.) In the records, add "BIHL l.4885-4887; LANG (langenberg_quellen-und-forschungen-niederdeutschen-mystik-gml_1902.txt) l.263" to the chapter claim's witness and to the "Denifle: Bruges, 1336; Preger and Seeberg" contested side.

**R3-2-M3 (johannes-tauler, brief paragraph 3: "the sermons" says more than Evans's book).**
- **Problem.** "C. de B. Evans, who put the sermons of Meister Eckhart, a fellow Dominican, into English in the 1920s, gives 1300." "The sermons" says all of them. Evans's book is one volume of Pfeiffer's text, sermons and tractates, translated "with some omissions". The Eckhart brief has it right: "who put his German sermons into English".
- **Source.** EVANS l.1-9 (title page): "Translation with some omissions and additions by C. de B. Evans, Vol. I"; the content note gives "volume 1 only", and Volume 2 (1931) is not held.
- **Fix:** "C. de B. Evans, who put sermons of Meister Eckhart, a fellow Dominican, into English in the 1920s, gives 1300." (20 words; the brief becomes 404 words.)

**R3-2-M4 (records: ranges short after the round 2 fixes, an unmarked OCR change, one side not updated, one "alone" narrowed).**
- **Problem and source.**
  - johannes-tauler, keyWorks claim: the Leipsic quotation begins "The oldest", and "The" is on WINK l.827.
  - henry-suso, chapter claim: "In consequence" begins at KNOX l.3768 ("In conse-").
  - henry-suso, Henry of Nördlingen claim: "Freund und" is on BIHL l.8294. The file reads "Heinrich von Nord- lingen" (l.8295-8296), but the quotation prints "Nördlingen" with no OCR note, unlike the batch's other records (for example "OCR 'Nördiingen'" in the Horologium letter claim).
  - julian-of-norwich, contested claim "Whether the anchoress of St Julian's and Julian Lampet of Carrow are one woman": the Dalgairns side still cites only DALGAIRNS l.1777-1789 and footnote l.1810-1813. Round 2 (R2-2-B2) asked for the new lines on this side as well.
  - johannes-tauler, "Last illness" claim: "Winkworth alone for the place and the day" now leaves the move to his sister's convent and the school writer's reproach out of the "alone". The claim's own search note and the card's "His last months" ("The move to his aged sister's convent, the day of his death and his burial ... rest on Winkworth alone") still treat those as hers alone.
- **Fix:**
  - Tauler keyWorks witness: "WINK l.68, 954-970, 866-868; WINK l.827-829".
  - Suso chapter witness: "KNOX l.3752-3765, 3768-3772".
  - Suso Henry witness: "WINK (…) l.5171-5175; BIHL l.8294-8297", and after the Bihlmeyer quotation add "(OCR 'Nord- lingen')".
  - Julian Lampet side: "(DALGAIRNS l.1777-1789, footnote l.1810-1813; his later note l.2853-2854, 2876-2878)".
  - Tauler "Last illness" claim: "Winkworth alone for the place, the day, the move to his sister's convent and the reproach, and the burial (the year 1361 is also in Evans, Spener, McCann, Gardner and the Luther volume)".

**R3-2-M5 (R2_changes.md, Part 2: two descriptions that do not match the files).**
- **Problem.** (a) R2-2-M8: "Seeberg stays unplaced in the sources: no held line gives more than his name and page." Bihlmeyer gives his book (BIHL l.4885-4889, and again at l.4889: "R. Seeberg, Aus Religion und Geschichte, Gesammelte Aufsätze und Vorträge, I (1906)"). (b) R2-2-B2: "The records add DALGAIRNS l.2853-2854, 2876-2878". They were added to the claim only, not to the Lampet side the finding also named (R3-2-M4).
- **Fix:** Record both corrections in R3_changes.md, in the way R2_changes recorded R2-1-M21: "R2-2-M8: Seeberg is placed in Bihlmeyer's literature list (BIHL l.4885-4887); the card now places him under R3-2-M2." "R2-2-B2: the Lampet side was not updated at round 2; it is under R3-2-M4."

### Checks that pass, beyond the table

- **Audio.** All five scripts equal their briefs, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Each has exactly two tags.
- **Quotations.** By script, every new or changed quotation matches its lines once the ranges are corrected as in R3-2-M4. They are: WINK l.5133-5138 ("he did not confine his exertions ..."), l.4245-4251 ("he must, on returning from Paris to Strasburg ... the celebrated Master Eckart"), l.5171-5175 ("a priest from Constance"), l.5262-5265 ("helped me in every way he could with all fidelity"); KNOX l.3484-3490 ("inordinate fear"), l.3498-3501, l.5366; DALGAIRNS l.2876-2878; DANIELS l.51; SPENER l.126; DENIFLE-II l.35292-35293 ("magister Ekardus, doctor[!)] sacre theologie, ordinis predicatorum", where the dropped "!)" is a footnote mark); EVANS l.377-378. DENIFLE-II l.35835 reads "P. Heinrich Denifle O. P.", which supports "a Dominican scholar".
- **"Only", "alone", "never".** "Winkworth alone gives the place and the day of his death" stands (search above). "The History's own text never names the Master" is unchanged. Open-Gaps 264's "the day, 29 September, rests on Horstman alone" stands: the search found only HORST l.134 and 2160-2161. Its "Margery Kempe's visit is in no held file" stands: Gardner names Kempe and Juliana together (GARDNER l.575-579) but tells no visit. Its "Tauler's Middle High German sermons (none is vendored)" stands: Jostes and Langenberg name Tauler but hold none of his sermons.
- **Pronouns and witnesses.** "Rolle, he learned" (the rider); "they began again" (the fits); "He finds its Alemannic dialect" (Pfeiffer, Strasbourg's); "a fellow Dominican" (Eckhart, of Tauler); "Neither" (Winkworth and Evans); "The Life says this woke" (being told of the gift). "She says" now carries the whole Tauler 1338 sentence. "At Basel" keeps Henry's place. In the Suso brief, the witness now comes in the paragraph's second sentence.
- **Writing.** In the changed sentences and their neighbors I found no narrator "X, not Y", no colon-reveal, no thesis opener, no tail or beat line and no process word. The longest changed sentences are the Tauler Basel sentence and the Suso Horologium trace, both at 25 words. Spelling is American ("favorite", "gray", "defense"). The Rolle paragraph 5 runs eight sentences of 8 to 17 words. It reads as a told sequence rather than a choppy run, and joining the rider sentences would put the brief over 405 words.
- **Cut briefs.** None of the five lost a scene or turning point at round 2. The Tauler 1338 sentence lost "He also preached, she says" but keeps all three acts. The Suso split keeps the fear, the ten years, Eckhart and the chapter.
- **Eckhart.** The one change is the Pfeiffer sentence pair on the card. 12 and 9 words, and both Strasbourg spellings now say whose they are.
- **README.** "404 to 405 words, grade 5.6 to 8.3, Flesch 62.8 to 80.5" matches all eight briefs by whitespace count and `grade_text` (low: Rolle, Julian, Eckhart and Grote at 404, Julian FK 5.59, Wyclif Flesch 62.84; high: 405, Wyclif FK 8.29, Julian Flesch 80.45). The Tauler names line and the Rhineland placement sentence match the card (EVANS l.497-498). Its Tauler "death day rests on Winkworth alone" and Rolle "29 September ... Horstman's alone" match the records. The quotation sentence's "among them" no longer claims a full list.
- **Open-Gaps 264.** The entry exists, is numbered 264, and says what the README says it does ("logged in Open-Gaps for a census fix, and the census is not changed here"). Its Part 2 items hold against the files: the Julian, Eckhart, Tauler and Suso scan corrections; Eckhart's death "Denifle l.34962 and Denzinger l.15220" (DENIFLE-II "er starb 1327"; DENZ "(f 1327)"); the Tauler hedge on hearers' notes (WINK l.913-917, 7034-7036); the Töss book retelling (STAGEL l.1903-1911).
- **R2_changes.md, Part 2.** R2-2-B1, R2-2-M1 to R2-2-M7, M9, M10, M11 and M12 are described as the diff shows. The exceptions are at R3-2-M5.

### Scores

| Brief | Words | FK | Flesch | Verdict |
|---|---|---|---|---|
| richard-rolle | 404 | 6.19 | 75.15 | CLEAR |
| julian-of-norwich | 404 | 5.59 | 80.45 | CLEAR once R3-2-M1 and R3-2-M4 are applied |
| meister-eckhart | 404 | 7.98 | 63.98 | CLEAR |
| johannes-tauler | 405 | 7.17 | 68.06 | CLEAR once R3-2-M3 and R3-2-M4 are applied (R3-2-M3 brings it to 404 words) |
| henry-suso | 405 | 5.82 | 78.69 | CLEAR once R3-2-M2 and R3-2-M4 are applied |

All five pass `grade_text` (FK 10 or below, Flesch 60 or above) and stay at or under the cap of about 405 words. R3-2-M5 is the changes log's.

### Count

- **Blocking: 0.**
- **Minor: 5.** R3-2-M1 (Julian, "says only"), R3-2-M2 (Suso, Seeberg unplaced and no records witness), R3-2-M3 (Tauler, "the sermons"), R3-2-M4 (records, short ranges, an unmarked OCR change, the Lampet side, a narrowed "alone"), R3-2-M5 (R2_changes descriptions).
- **Round 2 status (Part 2, 14 findings):** 11 RESOLVED, 3 PARTLY (R2-2-B2, R2-2-M8, R2-2-M11), 0 NOT RESOLVED.

**Files reviewed**
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/richard-rolle.brief.txt, richard-rolle.card.json, audio/richard-rolle.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/julian-of-norwich.brief.txt, julian-of-norwich.card.json, audio/julian-of-norwich.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/meister-eckhart.brief.txt, meister-eckhart.card.json, audio/meister-eckhart.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/johannes-tauler.brief.txt, johannes-tauler.card.json, audio/johannes-tauler.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/henry-suso.brief.txt, henry-suso.card.json, audio/henry-suso.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/records.json (the five entries)
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/README.md
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md (entry 264)
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era6-batch1/R2_recheck.md (Part 2) and R2_changes.md
