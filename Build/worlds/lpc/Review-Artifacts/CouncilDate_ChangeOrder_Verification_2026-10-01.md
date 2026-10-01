Simulated review — informational only, not an Article 31 substitute.

**Reviewer model:** claude-opus-5-5
**Drafter model:** Sonnet 5.5
**Reviewer agent:** separate change-order verification agent (Opus), council-date sweep, 2026-10-01
**Drafter agent:** lpc change-order fixer thread, commit 678d0a1a5
**Round:** 1 (change-order verification pass 1; not a Doc_02 revision round)
**Truncation check, method 1:** shell `wc -l` and `tail -n 2` on the saved file; the closing sentinel line is present as the last line.
**Truncation check, method 2:** Python read of the whole file; counts the level-2 headings (9 expected) and confirms the text ends with the sentinel line and a newline.
**Scope:** the change order on the date of the African council that petitioned the emperors (Letter 185 §25), approved by the project lead 2026-10-01; ledger entries on the council date (2026-10-01), on where Doc_02 uses 401 (2026-10-01) and the change order itself (2026-10-01). Diff checked: `git diff HEAD~1 -- Build/worlds/lpc/Doc_02_Source_Ecology.md Build/worlds/lpc/Source_Registry.md` (Doc_02 lines 17, 124, 126; Registry lines 25 and 58, rows 12 and 44).
**Status of this file:** a change-order verification by a separate agent, under the rule that a correction changing a claim is verified by a separate agent who sweeps every copy. It is not a Doc_02 review round and does not count toward the Doc_02 round cap. Its file name carries no document prefix, so the `roundcount` gate does not count it.
**Overall verdict:** the core correction holds. Both datings are stated accurately, and every cited locus says what the text claims. The change is not yet clean: 3 MEDIUM, 2 LOW and 2 COSMETIC findings, set out below. The MEDIUM findings need a fix and a targeted recheck by a separate agent.

## 1. Cited lines checked against the vendored files

Each locus was opened and placed by its structure marker, not by a search hit.

- **NPNF104, Letter 185 §§25–26 (`cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`).** `<div3 type="Chapter" n="7">` opens at line 19622; §25 runs lines 19624–19632, §26 begins at 19634. Endnote n. 2521 (`id="v.vi.ix-p1.2"`) is attached at "it was decreed in our council" (line 19628). Its text at line 19631 reads verbatim: "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), 401." The quotation in Registry rows 12 and 44 matches. Augustine's own §25 gives no year. **Verified.**
- **NPNF214, Code of Canons of the African Church (`cic/texts/npnf214_seven-ecumenical-councils.xml`).** The note sits in `<div4 type="Canon" n="XCII">` (opens line 35786), after Canon XCII's text and before its Notes (line 35832). The heading of Canon XCIII follows at line 35847. Line 35825 opens "This synod sent a legation to the Princes against the"; lines 35826–35831 read "Donatists." and then "The most glorious emperor Honorius Augustus, being consul for the sixth time, on the Calends of July, at Carthage in the basilica of the second region. In this council Theasius and Euodius received a legation against the Donatists. In this council was inserted the commonitorium which follows." Honorius's sixth consulship is 404. "The note before Canon XCIII" is an accurate description. **Verified.**
- **Bruns 1839 (`cic/texts/codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt`, Registry row 202).** Page header "CODEX ECCLESIAR AFRICANAE. 181" at line 12631; canon heading "XCIHI. Quale commonitorium acceperunt legati contra Donatistas" (OCR for XCIII) at line 12667. Lines 12658–12663 read "Haec synodus adversus Donatistas legationem ad principes dirigit. Gloriosissimo imperatore Honorio augusto sextum consule, Kalendas Julias *), Carthagine in basilica regionis secundae." The apparatus for that asterisk is at lines 12688–12689: "a. d. XVI. Kal. Jul. Hard. — VI. Kal. Jul. in textu Just. XII. Kal. Jul. Dion." (OCR "XH" for XII). These are 16, 26 and 20 June. "Kalendas Julias with variant readings in June" is accurate, but the variants sit at 12688–12689, outside the cited 12659–12663 (finding F3). **Verified, with a locus gap.**
- **Hefele-Leclercq (`cic/texts/hefele-leclercq_histoire-des-conciles-tome2-1-conciles-africains-slice-fra_1908.txt`, Registry row 247).** Page header "116. DU HUITIÈME AU QUINZIÈME CONCILE DE CARTHAGE" at line 4857. Lines 4882–4884: "Au mois de juin de l'année 404, le IXe concile de Carthage, s'occupa également des donatistes, et députa aux empereurs (Arcadius et Honorius) deux évêques, Théase et Evode." Lines 4892–4894 add the request to renew Theodosius's penal laws against heretics. **Verified.**
- **The identification.** None of the three sources names Letter 185. Treating the 404 council as the council of §25 rests on matching content: a council decision, envoys to the emperors, and renewal of Theodosius's law (Hefele 4892–4894). Hefele 4911–4914 also says Honorius issued an edict before the envoys reached him, which matches §26's account of a petition overtaken by a stricter law. The identification is sound, and rating the year Contested is the right frame.
- **Observation (inferential, not for the text).** The day readings in NPNF's endnote (26 June; 15 or 16 June) match the Latin variants VI and XVI Kal. Jul. for the 404 council. They also match Hefele's 15 or 16 June 401 dating of the fifth council (lines 3225–3227). This is consistent with the 401 dating having merged two councils. It is an inference only. No wording should rest on it.

## 2. The section 8 move (Documented / Widely Accepted)

- **Removal of "the 401 African council."** Doc_01 names no council of 401 except the one NPNF's endnote dates, at lines 160 and 182, and both are the petition council. The fixer's reading is correct: the phrase meant the petition council, so it did not belong in the Documented tier. **Verified.**
- **Retained clause.** "Councils met at Carthage in 401 (Hefele-Leclercq, Registry row 247, file lines 3227–3240 and 3463, June and September 401)." Lines 3223–3227 date the fifth council to "xvi ou xvii kalendas julias post consulatum Stiliconis, c'est-à-dire le 15 ou le 16 juin de l'année 401". Line 3234 places the sixth council in 401 as well. Line 3240 reads "ce concile du mois de juin de l'année 401". Line 3463 dates a council of Carthage to "13 septembre 401". NPNF104 independently attests the 13 September 401 council (lines 10290 and 18733). The clause is supported, and it now sits outside the parenthesis of Doc_01's sequence, which is correct, since Doc_01 does not establish it. The month "juin" falls at line 3226, one line before the cited range opens; line 3240 inside the range still names June (finding C1). **Verified.**
- **Nothing attested lost.** Every other item in the tier is unchanged word for word. The only content removed is a date that was never Documented. **Verified.**

## 3. Contested tier and Registry integrity

- **Contested item.** It names both datings and their sources correctly in substance: 401 from NPNF, 404 from the Code of Canons note (row 26, Latin row 202) and from Hefele-Leclercq (row 247). Two defects remain. First, it describes one NPNF note as two and attaches it to the wrong referent (finding F2). Second, it points to §1 for the Latin variants, and §1 does not mention them (finding F3). **Verified with findings.**
- **Registry rows 12 and 44.** Confidence letters are unchanged: A and A, before and after (checked at HEAD~1 and HEAD). Each row has 12 pipes, before and after. The row-number column of all 355 rows is identical at HEAD~1 and HEAD. **Verified.**
- **Row 44 chronology sentence.** It still asserts 401 as fact (finding F1).
- **Rows 26, 202 and 247.** Doc_02 now rests claims on them, and their Licensed For cells were not updated (finding F4).

## 4. Sweep of every copy of the claim

Searched for `401` across `Build/worlds/lpc/` (every document, chunk, index, Representative file, script and ledger), `records/lpc/`, `records/worlds/lpc.yaml` and the pinned package `packages/lpc/2026-10-01T15-26-09Z/` (including `compiled/prompt.txt` and `compiled/capsule.md`). The search then widened to the year-free phrasings of the same event ("not granted", "ungranted", "eleven years", "petition the emperors").

| Location | Text | Class | Ruling |
|---|---|---|---|
| Doc_02 line 17 (§1) | "dated 401 or 404 by the sources named below"; "NPNF's editorial footnote dates it 401, while ... (404 ...)" | Attributed; both datings | No change |
| Doc_02 line 124 (§8) | "councils met at Carthage in 401 (Hefele-Leclercq ...)" | Different councils, attested | No change (C1 optional) |
| Doc_02 line 126 (§8) | Contested item | Attributed; both datings | Fix F2, F3 |
| Registry line 25 (row 12) | "a council NPNF's own editorial footnote dates 401's own narrower solicitation ..."; Verification cell quoting n. 2521 | Attributed; both datings | Fix F5 (garbled opening) |
| Registry line 58 (row 44) | "dated 401 by NPNF's own endnote ... and 404 by ..." | Attributed; both datings | No change |
| Registry line 58 (row 44) | "XVI.5.52 is of 412 — eleven years after the events §25 recounts" | **Asserts 401 as fact** | Fix F1 |
| Doc_01 line 160 (§5) | "dated 401 by NPNF's editorial footnote at Letter 185 §25, not by Augustine's own text" | Attributed to NPNF | Not required; recommended (F6) |
| Doc_01 line 182 (§7) | "at a council NPNF's editorial note dates 401 (Letter 185 §25)" | Attributed to NPNF | Not required; recommended (F6) |
| Doc_01 line 206 (Round 9 disposition) | "the 401 petition's non-grant" | Dated audit line, unattributed label | Not required (C2) |
| `records/lpc/source/lpc.source.augustine-correction-of-the-donatists.md` lines 15, 18, and its package copy and `compiled/repository.json` | "footnote dates 401 (not Augustine's own text ...)"; "(the NPNF footnote dates it 401; ... 404, and Hefele-Leclercq to June 404)" | Attributed; both datings | No change |
| `scripts/wb_lpc_s21.py` lines 665, 669 | Same text as the record (its generator) | Attributed; both datings | No change |
| `compiled/prompt.txt` lines 155, 533; `compiled/capsule.md` line 19; facilitator brief line 317; demo `lpc.demo.compel-three-phase` | "early in his time as bishop"; "our bishops in council agreed to petition the emperors" | No year | No change. "Early" holds on either dating: 5–6 or 8–9 years into an episcopate of about 34 years. |
| `Representative/lpc_Rep_Phase5_Boundary_Testing_Round1.md` lines 162, 183 | "the narrow, ungranted 401 measure" | Dated audit record | No change; append-only record of that round |
| `lpc_Decision_Log.md` lines 27, 496, 2082 | "a council NPNF's own editorial note dates 401"; "statute 392, council 401, XVI.5.52 of 412"; "ungranted 401 measure" | Dated audit records | No change; superseded by the change-order entry (2026-10-01) |
| `Open_Gaps_Tracking.md` lines 1603, 2113 | Doc_01 quotation; "a council decision (401)" | Dated audit records | No change; append-only, superseded by the council-date entries (2026-10-01) |
| `Open_Gaps_Tracking.md` lines 825, 925 | "256 CE to ~400/401 CE"; "256-to-c.401 gap" | Unrelated (the date of *On Baptism*) | No change |
| `Doc_04_Superseded_Claims.md` line 33; `lpc_Decision_Log.md` line 730 | "401 `episcop-` tokens" | Unrelated (a token count) | No change |

No other copy was found in the World Profile, Capsule Core, Voice Configuration, Doc_04, Doc_05, Doc_07, Doc_08, Doc_09, Doc_10, the lexicon, story or context chunks, the other `wb_lpc_s*.py` scripts, or any other record. Doc_05 line 279, Doc_07 line 106 and lexicon chunk `lpclex016` carry the event without a year.

## 5. Gates

- `records lpc`: PASS.
- `regate lpc`: PASS. 150 edited fields below FK 8 were reported, not failed. Doc_02 and the Registry are not public-facing fields.
- `gaps lpc`: PASS.
- `claims lpc`: PASS (113 derived, 113 registered, 1 registered but unverified; none touch this claim).
- `citations lpc`: FAIL, 10 findings, all pre-existing and none in the changed files. They are unknown ids in `Open_Gaps_Tracking.md`, `Step0_Movement_Scope_Confirmation.md` and `lpc_Decision_Log.md`. `git blame` places the ledger lines in commits 2575323ba, 978d26c35 and ad548f75e, not in 678d0a1a5. `citations lpc Doc_02_Source_Ecology.md Source_Registry.md`: PASS. The change order did not harm readability or claims.

## 6. Findings with exact wording for each fix

**F1 — MEDIUM. Registry row 44 still asserts 401 as fact.** The chronology sentence that now names both datings ends: "XVI.5.52 is of 412 — eleven years after the events §25 recounts, under different emperors." Eleven years holds only on the 401 dating.
Replace with: "XVI.5.52 is of 412 — eight years after the events §25 recounts on the 404 dating, eleven on the 401 dating, under different emperors."

**F2 — MEDIUM. The Contested item misdescribes the NPNF evidence.** It reads: "401 on NPNF's editorial footnote to Letter 185 and its endnote on *Codex Theodosianus* XVI.5.21, which Augustine's own text does not support with any year". NPNF has one note dating this council, endnote n. 2521, at line 19631. It is attached to "it was decreed in our council", not to XVI.5.21. NPNF104 carries no note on XVI.5.21 in §25 (its only Codex note nearby, line 19710, cites XVI.5.52).
Replace with: "401 on NPNF's editorial endnote to Letter 185 §25 (n. 2521, `npnf104_augustine-anti-manichaean-anti-donatist.xml` line 19631: "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), 401"), a year Augustine's own text does not give".
The change-order ledger entry (2026-10-01) also says "footnote and endnote" for this one note. That entry is append-only and stays as written. The correcting ledger entry for this verification should say so.

**F3 — LOW. The pointer to the Latin variants is wrong, and the variant locus is missing.** The Contested item ends its 404 clause with "the Latin edition's variant readings for the day include June (§1)". Doc_02 §1 does not mention the variants. Only Registry row 44 does, and it cites lines 12659–12663, while the apparatus is at 12688–12689.
In Doc_02 line 126, replace "the Latin edition's variant readings for the day include June (§1)" with: "the Latin edition's apparatus gives three variant days, all in June (Registry rows 44 and 202; file lines 12688–12689)".
In Registry row 44, replace "reads *Kalendas Julias* with variant readings in June" with: "reads *Kalendas Julias*, and its apparatus at lines 12688–12689 gives the variant days XVI, VI and XII Kal. Jul. (16, 26 and 20 June)".

**F4 — MEDIUM. Rows 26 and 247 do not license the claims Doc_02 now rests on them.** Row 247's Licensed For cell reads "Not currently licensed for a specific claim". Doc_02 §1 and §8 now cite it for June 404 and for the 401 councils. Row 26 is licensed only for "the institutional skeleton of this world's own conciliar life" and is marked "Not independently re-collated". Doc_02 now cites it for the 404 dating note, which this verification read directly. The Registry's checkpoint rule ties every claim-supporting source to a row that licenses it. This is a follow-on of the same approved change order, not a new decision. Confidence letters should stay as they are: row 26's B covers content still not re-collated.
Row 247, replace the Licensed For cell with: "The petition council's 404 dating (the ninth council of Carthage, June 404, sending Theasius and Evodius to the emperors; file lines 4882–4884) and the councils of Carthage in 401 (June, lines 3223–3240; 13 September, line 3463), cited at Doc_02 §1 and §8. Secondary and consultation-only; licensed for these dates and nothing more".
Row 26, append to Licensed For: "; the note before Canon XCIII dating the council that sent Theasius and Evodius to the emperors to the Calends of July in Honorius's sixth consulship, 404 (Doc_02 §1, §8)". Append to Verification Note: "That note was read directly at `npnf214_seven-ecumenical-councils.xml` lines 35825–35831, 2026-10-01."
Row 202, append to Licensed For: "; the Latin of that dating note, *Kalendas Julias*, with its June variants (lines 12658–12663, 12688–12689; Doc_02 §8)".

**F5 — LOW. Row 12's Licensed For cell opens with a garbled phrase.** "a council NPNF's own editorial footnote dates 401's own narrower solicitation of state power" is not a sentence, and it leads with the 401 dating. It predates this change order, but it sits in the cell the change order edited. The project rule is that an edit to a canonical file also repairs what is broken in that cell.
Replace the text from "a council NPNF's own editorial footnote dates 401's own narrower solicitation of state power (" up to "so the date is Contested)" with: "Augustine's own narrower solicitation of state power at the African council that petitioned the emperors (Letter 185 §§25–26; Augustine's own text gives no year, per Doc_01's own established distinction, carried here rather than dropped; NPNF's editorial endnote dates the council 401, while the Code of Canons of the African Church's note before Canon XCIII (row 26; Latin edition row 202) dates it to the Calends of July in Honorius's sixth consulship, 404, and Hefele-Leclercq (row 247) to June 404, so the date is Contested)".

**F6 — LOW (recommended, not required). Doc_01 lines 160 and 182 give one dating.** Both attribute 401 to NPNF and say Augustine's text gives no year. That is accurate and asserts nothing. Doc_02 §1 says it carries "Doc_01's own established form for this distinction", and that form now names two datings. Doc_01 is approved to proceed and lies outside the approved change order, so editing it needs the project lead's extension of the change order.
If extended, at line 160 replace "dated 401 by NPNF's editorial footnote at Letter 185 §25, not by Augustine's own text, which does not date it" with: "dated 401 by NPNF's editorial footnote at Letter 185 §25 and 404 by the note before Canon XCIII in the Code of Canons of the African Church, not by Augustine's own text, which does not date it (the year is Contested, Doc_02 §8)". At line 182 replace "at a council NPNF's editorial note dates 401 (Letter 185 §25)" with: "at a council NPNF's editorial note dates 401 and the Code of Canons dates 404 (Letter 185 §25; Contested, Doc_02 §8)".

**C1 — COSMETIC.** Doc_02 line 124 cites Hefele lines "3227–3240". The day and month ("le 15 ou le 16 juin") fall at line 3226 and the dating clause opens at 3223. Line 3240 inside the range still names June 401, so the claim is supported. Optional wording: "file lines 3223–3240 and 3463".

**C2 — COSMETIC.** In Doc_02 line 17, two parentheses sit back to back: "(Registry row 247, file lines 4882–4884) (Letter 185 §§25–26, ...)". Optional: join them with a semicolon inside one parenthesis.

## 7. Rulings on the lines the fixer left

- **Doc_01 line 206, "the 401 petition's non-grant".** No change needed for this change order. It is a dated disposition line naming a question as the earlier "Pending" line named it, and rewriting it would alter the record of what Round 9 tested. It is also process narration inside a canonical document. If Doc_01 is edited under F6, the same edit should neutralise it to "the petition's non-grant (Letter 185 §26)" or move the disposition narration to the ledger, as the live-surface rule requires.
- **Phase 5 Round 1 audit lines (Representative file, lines 162 and 183), Decision Log lines 27, 496 and 2082, Open_Gaps_Tracking lines 1603 and 2113.** No change. These are dated, append-only records of what stood at the time, and the council-date ledger entries of 2026-10-01 supersede them. Neither the compiled prompt nor the capsule carries a year.
- **Doc_01 lines 160 and 182.** Accurate as written; a change is recommended under F6 and needs the project lead's extension of scope.

## 8. What follows

The MEDIUM findings F1, F2 and F4 need fixing, and a separate agent needs to recheck them in a targeted way. The same fix should take F3 and F5. F6 waits on the project lead. This verification's outcome belongs in `Open_Gaps_Tracking.md` as a new numbered entry, citing the change-order entry by subject and date. After any edit to `records/`, nothing needs a repin: no record or package text is affected by F1–F5.

## 9. Closing

Truncation checks on the saved file. Method 1 (shell): 113 lines, and `tail -n 2` shows this line and the sentinel. Method 2 (Python): 9 level-2 headings, and the text ends with the sentinel and a newline. Both passed. End of file, nine level-2 sections.
END OF CouncilDate_ChangeOrder_Verification_2026-10-01
