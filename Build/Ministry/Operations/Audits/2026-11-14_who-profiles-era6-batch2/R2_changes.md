# R2 changes: era 6 batch 2

Round 2 found 6 blocking and 54 minor points (Part A 1 and 15, Part B 3 and 10, Part C 2 and 14, Part D 0 and 19). Each part's points were applied by a fresh Opus fixer that reopened every cited source line with its context before applying; where the fixer judged the proposed wording wrong or unclear, the difference is listed. Records and README edits for Parts C and D were written as exact replacement pairs and applied in one pass. After the fixes the briefs were rescored with `engine.m1.gates.grade_text` and the audio scripts rebuilt and checked against the briefs.

| Profile | Words | FK | Flesch |
|---|---|---|---|
| catherine-of-siena | 405 | 6.76 | 71.72 |
| bridget-of-sweden | 405 | 6.85 | 68.68 |
| bernardino-of-siena | 405 | 7.21 | 69.87 |
| angelo-clareno | 406 | 8.16 | 62.55 |
| william-of-ockham | 405 | 8.07 | 63.19 |
| gregory-palamas | 407 | 7.77 | 63.26 |
| gregory-of-sinai | 406 | 8.59 | 63.48 |
| nicholas-cabasilas | 406 | 7.99 | 61.45 |

### Part A (Catherine of Siena, Bridget of Sweden, README)

Every cited source was reopened with 20+ lines of context (BIRGL l.8155-8182, 11100-11126, 98405-98422, 98545-98615, 98770-98820; BIRGE l.920-1062; MANSI26 l.1-6, 53385-53420; CATHI l.14496-14516; COVEL l.51450-51468; ASMAR3 l.132875-132900, 132970-132985, 133255-133275; TERESA l.675-690). The reviewer's readings hold. Both briefs now match the scratchpad texts `r2a/cath.txt` and `r2a/brid.txt` exactly; every difference from the prior brief is one of the findings below. The birth-year search for A2-M12 was rerun (year search: only BIRGE l.857 gives a year; ASJUN5 l.14879 and the file headers give none).

- A2-M1 (Catherine brief, "her" read as Bridget): applied as worded.
- A2-M2 (Catherine brief, "Mansi's councils"): applied as worded. Also applied to Bridget's card `legacy.remembered` 4, which had the same phrase ("in Mansi's collection of church councils"); same defect, no claim added.
- A2-M3 (Catherine card `uncertain` 1, Duranti's first name and role): applied as worded.
- A2-M4 (Catherine card `legacy.traces` 3, "as it is held"): applied as worded.
- A2-M5 (Catherine card `dates`, 30-word Covel sentence): applied as worded.
- A2-B1 (Bridget card `place` and records, Rome years given to "Cumming's reckoning"): records replacement applied as worded, tag set to Contested. Card applied with difference: "Rome, where she lived and died. Her daughter's Life says the daughter spent twenty-five years there with her, and a Bollandist note reckons them from 1348." The proposed "counts the daughter's twenty-five years there with her from 1348" was hard to parse aloud; the new wording keeps the same two claims (ASMAR3 l.132892-132893, 133269) and splits who says what.
- A2-M6 (Bridget brief, "him" after "Christ"): applied as worded, with the offset "Gregory reached Rome in January 1377."
- A2-M7 (Bridget brief and card, "gives all eight books to"): applied as worded in both.
- A2-M8 (Bridget brief para 4): applied with difference. The last clause reads "and died within a month of reaching Avignon" (the r2a/brid.txt variant the review names), in place of "died there within a month of arriving", where "there" could attach to the Order rather than Avignon. Cumming: "died the same year, in less than a month after returning to Avignon" (BIRGE l.1022-1024). Offset in para 6 ("carried to Vadstena") applied. The records' Montefiascone claim now carries Duranti's two places after Platina ("dum enim proficiscebatur in Galliam ... mortuus est, vel ut alij volunt, Auenione vitam finiuit", BIRGL l.98604-98609, OCR noted) and Cumming's death line, with BIRGE l.1022-1024 in the witness.
- A2-M9 (Bridget card, Council of Constance twice): applied as worded.
- A2-M10 (Bridget card `dates`, 40-word sentence): applied as worded.
- A2-M11 (Bridget card, Wilkens's role): applied as worded.
- A2-M12 (Bridget records, birth-year absent note): applied as worded.
- A2-M13 (README, Open-Gaps entry): not applied as worded, by the coordinator's instruction. The entry will be registered just before merge and its number taken then, so the README keeps "an era 6 entry is registered with this batch", with no number cited and no "to be registered". The sentence is true once the entry exists.
- A2-M14 (README, Cabasilas bullet "tagged Contested"): not applied; already resolved by Part C (C2-M6, commit 98d1c291). The bullet now says the three are tagged Contested and the archbishop claim is tagged Widely Accepted, which matches the records. Applying A2-M14's wording on top would be a fix on a fix.
- A2-M15 (README, English-quotation list): applied as worded.

Audio for both rebuilt from the brief ("[calmly] " at the start, "[warmly] " at the last paragraph) and diffed: exact, two tags each. Both cards and records.json parse.

| Brief | Words | FK | Flesch |
|---|---|---|---|
| catherine-of-siena | 405 | 6.76 | 71.72 |
| bridget-of-sweden | 405 | 6.85 | 68.68 |

### Part B (Bernardino of Siena, Angelo Clareno)

All 3 blocking and 10 minor points applied. Before each fix the cited lines were reopened (GLASS l.21735-21740; BANCHI1 l.6408-6413; EHRLE1 l.27768-27790, 28488-28493; PG88 l.43307; LEA3 l.8222-8225; CARL l.1461).
- B2-B1, B2-M1 to B2-M4 (Bernardino) as worded. B2-M1: the records witness field also takes LEA3 l.8223-8224. The note on the Roman-hearing side (l.6410-6412) is added as the reviewer's records point asks.
- B2-B2, B2-B3, B2-M1, B2-M3 to B2-M6 (Clareno) as worded. Records: EHRLE1 l.27785-27786 and Ehrle's hedge added to the death claim; the 1331 side reworded; CARL l.1461 added to the 1331 claim; EHRLE1 l.28490-28492 (OCR "Bubertus") added to the Bollandists claim.
- B2-M2 (Clareno): the `uncertain` and README wording as proposed. In `dates` the proposed "from a weekday note, using the years Daniel Papebroch, a Bollandist, had found for that weekday" left "found for that weekday" unclear; it reads "from a note dated by weekday and the years in which Daniel Papebroch, a Bollandist, had found that weekday fell on 13 June" (the same claim, EHRLE1 l.27792-27795).

### Part C (William of Ockham, Nicholas Cabasilas)

All cited lines were reopened with 20+ lines of context; every reading below was confirmed. Records and README edits are in `C_records_pairs.json` and `C_readme_pairs.json` (each old_string validated to occur once; records.json still parses with all pairs applied).

**william-of-ockham**
- C2-M1 (Eubel "editor of 1898"): applied as worded (BUL5 l.70-77).
- C2-M2 ("walked into persecution"): applied as worded, brief and records pair (SCHOLZ l.25858-25863; Christ's leave to flee kept in records).
- C2-M3 (knownFor "he" reads as Lea): applied as worded.
- C2-M4 (dates "he notes" reads as Lea): applied as worded (the note is Carlini's, CARL l.6278-6280).
- C2-M5 (Gerson 39-word sentence): applied as worded (GERSON l.27010-27016, 27205-27208).
- C2-M6 (title-page witnesses): applied as worded, in the house witness form, "BUL5 (...) l.70-77 (title page)" and "CARL (...) l.195-198 (title page)". The Eubel claim text "(file header and title page)" was changed to quote the title page too.
- Optional heading fix on the arrest-letters claim: applied ("to German bishops and lords, the English bishops and the King of England").
- Not applied here: Müller to the Open-Gaps entry (C-M14 status note). That file is outside this worker's scope; left for the coordinator.

**nicholas-cabasilas**
- C2-B1 (who-line inside Kantakouzenos's attribution): applied as worded (CANT3 l.16599-16601, 16629).
- C2-B2 (1353 put in Gass's mouth): applied as worded, card and records side (GASS l.1773-1786: the "some years" follow Palamas and the 1351 synod).
- C2-M1 ("he" heard as Gass): applied as worded.
- C2-M2 (Gass's hedge on the wrong point): applied as worded (GASS l.1374-1375 states the succession; "Muthmasslich" covers only the late start).
- C2-M3 (God came down, heard as narrator's): applied as worded (PG150 l.36579-36582).
- C2-M4 (Mark gloss inside Gass's witness): applied with difference. "Sent to answer the Latins" became "the only two Greek prelates charged with answering the Latins". Petit's "avaient seuls reçu mission" means they alone were given the task; "sent" could be heard as travel, and "only" keeps "seuls" (PO15 l.627-641). Card item 5 shortened as proposed. Records pair adds the Petit claim (Documented).
- C2-M5 (Boivin "edited"): applied as worded (GREG2 l.1, 168, 36471; his note "Nicolaus scilicet" is signed BOIVIN, l.47127-47138).
- C2-M6 (README vs tag): applied with difference. The proposed text joined the archbishop clause and the Gregoras clause with a semicolon; split into separate sentences, with "on Fabricius, Gass and a Thessalonica record" in place of the parenthesis. Same claims. The coordinator's open call on the `contested_claims` entry ("When he became archbishop ..., and whether he did") remains; the card's uncertain item still carries that heading.
- C2-M7 (1865 witness): applied as worded in the claim; the witness field also gains "261" for PG150 and "PG161 (bessarion_opera-omnia-pg161-grc-lat_migne1866.txt) l.110885".
- C2-M8 (Fabricius notice in ownWords): applied as worded; new "about" entry placed first in the about list.

Audio: both scripts rebuilt from the briefs ("[calmly] " at the start, "[warmly] " at the last paragraph) and confirmed by script to equal the brief with the tags removed; the word diff against the old audio shows only this round's brief changes.

| Brief | Words | FK | Flesch |
|---|---|---|---|
| william-of-ockham | 405 | 8.07 | 63.19 |
| nicholas-cabasilas | 406 | 7.99 | 61.45 |

### Part D (Gregory Palamas, Gregory of Sinai)

Each cited source reopened with 20+ lines of context (CANT2 l.11265-11310, 34285-34340; MANSI26 l.10170-10190, 19565-19610; GREG3 l.13053-13058, 13158-13194; PAISK l.1-45, 9830-9840; PAISZ l.3984-4008, 10995-11035, 14190-14220; MEYER l.1-3, 3992-4012; PG150 l.69105-69146, 72570-72605). The reviewer's readings hold throughout. Records and README edits are in D_records_pairs.json and D_readme_pairs.json (each old string checked to occur once; records parse as JSON after applying).

- D2-M1: applied as worded in the brief ("for justice and truth"; offset "lay in prison"). Records note applied as worded. Records witness applied with a difference: my read puts the Greek at CANT2 l.34298-34303 ("Παλαμᾶν δὲ ἐπήνει" opens l.34298) and the Latin at l.34333-34336 ("Palamam contra laudavit" is l.34333), one line earlier than the review's l.34299-34304, 34334-34336.
- D2-M2: applied as worded.
- D2-M3: applied as worded on the card; records "the 1347 tome" applied as worded.
- D2-M4: applied as worded.
- D2-M5: applied as worded.
- D2-M6: applied as worded (sentence deleted; GREG3 witness merged).
- D2-M7: applied as worded. Also, with a difference: the same records claim's text "put Palamas on prayer into Slavonic" had the broken English D2-M8 fixes on the card; changed to "translated Palamas's piece on prayer into Slavonic (title page and contents ...)" so records and card agree.
- D2-M8: applied as worded.
- D2-M9: applied as worded (README pair).
- D2-M10: applied as worded.
- D2-M11: applied as worded in the brief; on the card the title went to Paisius's first mention (legacy.traces 2) per D2-M14 and was dropped from uncertain 1 per D2-M16.
- D2-M12: applied with a difference: "Some teach saying it with the mouth, some with the mind" (brief and card) in place of "Some teach it said with the mouth". Same reading of "διδάσκουσι λέγειν αὐτήν" (they teach saying it), same word count; "it said" reads awkwardly aloud and the gerund keeps the teach/say distinction plainer.
- D2-M13: applied as worded.
- D2-M14: Meyer (via D2-M15) and Rački applied as worded (later trace now "Rački, retelling ..."). Basil/Paisius trace applied with a difference: "Basil, elder of the Poiana Marului monastery, wrote a preface for those who wish to read Gregory's book. He was a friend of Paisius Velichkovsky, abbot of Neamț in Moldavia, and the preface is printed among the writings of Paisius's circle." The proposed wording had "his book" and "his friend" one sentence apart with different referents (Gregory, Basil); naming Gregory and Paisius removes the ambiguity. Same sources (PAISZ l.3991-3994, 14198-14202).
- D2-M15: applied as worded on the card; records side 2 applied as worded.
- D2-M16: applied as worded.
- D2-M17: applied as worded.
- D2-M18: applied as worded.
- D2-M19: applied as worded (card here; README pair).

Audio for both rebuilt from the brief ("[calmly] " at the start, "[warmly] " at the last paragraph); diff against the brief with the two tags stripped is empty, two tags each. Both cards parse as JSON. American spelling outside quotations; no change was needed.

| Brief | Words | FK | Flesch |
|---|---|---|---|
| gregory-palamas | 407 | 7.77 | 63.26 |
| gregory-of-sinai | 406 | 8.59 | 63.48 |

Kept, as Part C's fixer left open: the Cabasilas contested claim on when he became archbishop and whether he did (a date on one side and a silence on the other); the card's uncertain item carries it.
