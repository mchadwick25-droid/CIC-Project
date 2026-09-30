# hus, Round 1 revision of Doc_01, Doc_02, Source_Registry and Open_Gaps_Tracking (2026-09-30)

Drafter: Sonnet 5.5, session `session_019FXuEebrCDmzYe987sNAxL`. Inputs: `Build/worlds/hus/Review-Artifacts/Doc01_Round1_Review.md` (0 P0, 8 P1, 12 P2) and `Build/worlds/hus/Review-Artifacts/Doc02_Round1_Review.md` (0 P0, 9 P1, 12 P2), both committed at 2e22e8398. Drafts under review: 06551b798 (Doc_01 also a1cefcb61). This is revision round 2 of Doc_01 and of Doc_02, the Registry and Open_Gaps. No review was run or written in this pass. Independent review follows.

## The project lead's ruling, as given to the drafting worker

The instruction to the worker contained this decision, quoted verbatim:

> Decision already made by the project lead (2026-09-30): Hussites are ONE world with THREE strands (Utraquist, Taborite, Unity), 1402-1517. Doc_01 §5/§9 must state this as the project lead's ruling, while still stating the two-strand and two-world alternatives and their costs honestly (Unity's living-tradition case; hostile-source Taborite evidence; Tabor's 1419-52 phase). Article 29 tradition(s), Representative identity, and registering hus in records/worlds.yaml remain OPEN for the project lead; do not decide or imply them.

And these limits, quoted verbatim:

> Limits: do NOT edit cic/texts/, cic/corpus-map/, records/, packages/, Build/worlds/hus/build/hus_Build_State.yaml (except if a review finding requires it, then say so). Registry rows are allowed only for works the corpus map already assigns to hus; a vendored work assigned only to another world (e.g. Foxe vol. III, Van Braght) is recorded as a candidate/request in Open_Gaps_Tracking.md, not as a Registry row and not claimed in Doc_02 as supporting evidence (cross-world placement needs the project lead's authorization; tell me in your report which ones).

The record of the ruling is this instruction. No Build_State file was edited.

## Re-verification method

Every corrected quotation, locus and figure was re-read in the vendored file by the drafter, and every quotation in the four live files was matched by script against the vendored files after whitespace, quotation-mark, spacing-before-punctuation and line-break-hyphen normalisation (case-insensitive). Corpus figure, two methods: (1) decoded UTF-8 character length per file, in Python, over the eight assigned files: 6,654,664 characters in all (Gillett 1,466,903; Schaff 735,667; Workman & Pope 672,550; Lützow *Bohemia* 1,036,422; Lützow *Hussite Wars* 989,672; Lützow *Life & Times* 1,025,417; Piccolomini 385,464; Seifferth 342,569). (2) `cat` of the eight files piped to `wc -m` under `LC_ALL=C.UTF-8`: 6,654,664. The two Hus files are 1,408,217 characters, 21.2 per cent. A third run, `wc -m` on the file list under the default locale, printed 6,668,037, because that locale does not decode multi-byte characters; it is not a valid count. The shelf holds 315 text files (277 `.txt`, 38 `.xml`); the directory has 322 entries (five metadata files, `INDEX.sqlite`, `_intake/`).

## Disposition table: Doc_01 review

| Finding | Disposition | Where | Drafter's check |
|---|---|---|---|
| P1-1 cup not Hus's concern | Fixed | Doc_01 §2, §3 gravity 2; Registry rows 3, 42; Doc_02 §2, §3 item 6, §8 | Letter LXXI read (lines 11986–12002). Workman's note is printed before Letter XLIII (heading 8824), not under Letter XLI as Registry row 3 said. Corrected. |
| P1-2 Letter VI | Fixed | Doc_01 §7 | Letter VI is Hus's reply; the crowd of "nearly ten thousand" hears of Wyche's letter; Workman's contents line says he read it in the Bethlehem. |
| P1-3 Unity non-resistance | Fixed | Doc_01 §1, §3 gravity 6, §4, §5, §6; Doc_02 §8; Open_Gaps 10 | Lützow *Bohemia* 10111–10124 read. Tagged Inferential/Thin (single secondary account; Lützow hedges "As far as we can judge"). |
| P1-4 strand finding | Fixed | Doc_01 §5, §9; Open_Gaps 5, 13 | Ruling stated as the project lead's. Two alternatives given at full strength with costs. Tábor is 33 of the window's 115 years (about 29 per cent), not "about a third". The Unity's Preface (declining the name "Hussites"; praise of Tábor) and Lützow's remark that the Brethren's protest against the Taborite link was "not justified by the facts of the case" are carried. |
| P1-5 two misstated grounds | Fixed | Doc_01 §4 | Census structure labelled portfolio-level. Preface names Hus's principle but not the cup or the Czech language. A search of the Seifferth file finds no "Czech", "mother tongue" or "vernacular". The cup appears only in the *Ratio* body (line 4881). |
| P1-6 (a) crusade count | Fixed | Doc_01 §2 | The "modern writers generally" footnote (6324–6326) is attached to the 1422 expedition, which Lützow doubts was a crusade. Contested; census counts five. |
| P1-6 (b) Adamites | Fixed | Doc_01 §5, §8; Doc_02 §3, §8 | Contested, both readings carried. |
| P1-6 (c) household discipline | Fixed | Doc_01 §4 | Inferential/Thin. |
| P1-7 Article 4 check | Fixed, with a correction to the review | Doc_01 §8; Open_Gaps 4 | Five commitments quoted verbatim from the Constitution (checked against the docx). Clause by clause. The review said the third day was not shown. It is: Letter LXXIII, "He knew He would rise again on the third day". Also shown in Hus's voice: burial for three days (Letter XXVIII), ascension (*De Ecclesia* p. 28, "ascended again into heaven"). Not shown: "bodily", "in glory to judge", "maker of heaven and earth", "seen and unseen", "only Son … of one Being", "incarnate of the Holy Spirit", "Lord and giver of life" (the Preface's "Lord and Giver of Life" is the editors' phrase). |
| P1-8 violence against Germans and Jews in 1419 | Fixed | Doc_01 §2, §6 | The 1419 event names no group. Lützow: 1422 riot with attack on Jews (line 5810); a massacre of "Germans and Jews" before the 1485 peace (10760–10761, no year given). |
| P2-1 "fourth person" attribution | Fixed | Doc_01 §8 | Workman 10938–10940; Gillett 2685–2686. |
| P2-2 "All-powerful" | Fixed | Doc_01 §8 | Scan "All- / powerful" joined at line break. |
| P2-3 Letters from Constance range | Fixed | Doc_01 §2 | Letter XXXVII is dated Constance, 4 November 1414 (line 7962). |
| P2-4 "insufficient evidence" | Fixed | Doc_01 §5; Doc_02 §3 | About Michael, curate of Žamberk; no year. |
| P2-5 name *Bohemia* for Rokycan quotations | Fixed | Doc_01 §2 | Lines 9504–9510. |
| P2-6 Gillett's categories | Fixed | Doc_01 §3 | Lines 17708–17710; source is "the Calixtine narrative". |
| P2-7 "later took the name" | Fixed | Doc_01 §1 | Seifferth line 172–174: "At an early period of this association it assumed the name". |
| P2-8 *Diarium* identification | Fixed | Doc_01 §2; Doc_02 §2; Registry row 13 | Tagged Inferential/Thin. Not proved. |
| P2-9 Unity's Preface on Tábor | Fixed | Doc_01 §5 | Lines 4081–4087. |
| P2-10 continuity questions | Fixed | Doc_01 §7 | New paragraph answering the Framework's three questions. |
| P2-11 readability | Fixed in part | Doc_01 throughout | Scored with `engine.m7.turn_readability.score_turn`, markdown symbols stripped: whole document FK 9.2 and FRE 51.6 before; FK 7.7 and FRE 58.8 after. FRE remains below 60. The residue is quoted nineteenth-century sentences and proper nouns. Not fully met. |
| P2-12 non-sentence | Fixed | Doc_01 §4 | Rewritten. |

## Disposition table: Doc_02, Registry and Open_Gaps review

| Finding | Disposition | Where | Drafter's check |
|---|---|---|---|
| P1-1 Forces lens | Fixed | Doc_02 §6 "Forces lens" | Read Framework V7.4 Step 2, the forces-lens bullet. Names sources, silences and survivorship. |
| P1-2 corpus total | Fixed | Doc_02 §1 | Two methods, above. |
| P1-3 loci | Fixed | Registry rows 1, 2, 7; Doc_02 §2, §8; Doc_01 §2 | 1401 note under Letter XVIII (heading 5392); "hopelessly doctored" under Letter XX (5617/5650); p. 70 in ch. VIII (5274). |
| P1-4 in-window Unity text | Fixed | Registry rows 32, 43; Doc_02 §1, §6, §7, §8; Open_Gaps 1 | Both fragments read (548–555; 8242–8268). The first is partly garbled in the scan, so only the clean words are quoted. |
| P1-5 Adamite rating | Fixed in part | Doc_02 §3, §8; Open_Gaps 22 | Contested. Not confirmed: that Piccolomini ties the Adamites to Tábor (his chapter, as far as legible, attributes them to a Picard from Belgian Gaul). The tie rests on Březová as Lützow reports him (5382–5392). The Kaminsky point is reviewer knowledge, unchecked, and is carried as a to-do (Open_Gaps 22). |
| P1-6 Piccolomini licence | Fixed | Doc_02 §7 item 3; Registry rows 11, 12; Open_Gaps 3 | The file has no ſ (count 0); the gate normalises only ſ (`engine/m1/quote_verbatim.py` line 279); `REGISTRY.yaml` gives no apparatus; ruling point 5 read. |
| P1-7 missing rows | Fixed | Registry rows 44–51; also 52–54 for the recall and PRESS answers | Loci for each named in the vendored apparatus. Publication years for Kybal, Novotný, Loserth, Palacký come from the builder's knowledge and are marked as such. |
| P1-8 Van Braght | Declined as a Registry row; recorded as a candidate | Open_Gaps E2; Registry saturation statement | The project lead's limit forbids rows for works assigned to other worlds. The section is real (47370–47660). The saturation statement is corrected. The reviewer's count of 106 files is a case-insensitive count; a whole-word, case-sensitive count gives 53. Three of eight "Brethren" matches are false. |
| P1-9 R2 misreads Schaff | Fixed | Open_Gaps R2; Registry rows 9, 48 | Schaff lines 2265–2267 hope for a Flajšhans edition; none existed. Also found: Loserth's note says the 1558 edition was printed at Nuremberg; Schaff says Frankfurt. |
| P2-1 line markers | Fixed | Registry | Letter I heading is at 1684, not 1683 (the review is off by one). Others confirmed. |
| P2-2 A letters | Fixed | Registry header | Row 25 vacated. Header states what A attests on an Excluded row. |
| P2-3 rights basis | Fixed | Registry | Rights stated per row. Rows 30 and 40 marked in copyright. |
| P2-4 vocabulary | Fixed | Doc_02 §3, §8 | Lützow 1909 (line 3429) gives the year 1402 independently. Workman explains the 1401 reckoning. |
| P2-5 Jews | Fixed | Doc_02 §5, §6 | Limited to the window: 1422; before 1485. |
| P2-6 women | Fixed | Doc_02 §6 | Letter II to nuns; Letter XXXV to Martin. |
| P2-7 hedge | Fixed | Doc_02 §7 item 1; Registry row 32 | The scan reads "leem … fint" for "seem … first"; described as garbled and not quoted. |
| P2-8 duplicated pages | Fixed | Doc_02 §7 item 3; Registry row 11 | Confirmed at 3889/4513 and 4056/4664. |
| P2-9 "322" | Fixed | Doc_02 §9 | 315 text files. |
| P2-10 Open_Gaps | Fixed | Open_Gaps | `records/worlds/hus.yaml`; duplicate entries cross-referenced, not deleted. |
| P2-11 narration and attribution | Fixed | Doc_02 §1, §2 | Creighton credited. Lützow credits Droysen for the Slav–Teuton line, cited to row 17. |
| P2-12 row 14 note | Fixed | Registry row 14 | "Rests on Poggio's letter, not on presence." |

## Corrections the drafter found beyond the reviews

- Registry row 3 cited the wrong letter for Workman's note (before Letter XLIII).
- Doc_02 said the Piccolomini dedicatee is not legible. The heading "AD ALPHONSVM REGEM ARAGONVM" (line 319) is legible, and line 421 carries the sentence on partly seeing and partly hearing.
- Doc_01 quoted "genuine offspring" although the scan prints "genubie". Now quoted as printed, with the gloss.
- Unsourced glosses removed: an Utraquist "consistory", "moral reform by force" for Tábor, the Hutterites remark.
- The reviewer's "third day" claim was wrong (see P1-7).

## Cross-world placement requests (need the project lead's authorisation)

Recorded in `Open_Gaps_Tracking.md` section E: E1 Foxe Vol. III (Lollardy); E2 Van Braght, *Martyrs Mirror* (Anabaptist movements); E3 Loserth's introduction to Wyclif's *De Ecclesia* (Lollardy); E4 the Luther files and the Bacon–Allen hymn (Luther worlds); E5 passing mentions in Vedder, Kempis, the *Fasciculi Zizaniorum*, Sarpi and Zwingli vol. 3. Registry rows 25 to 28 (Foxe; two Luther rows; Wyclif) are vacated and their numbers are not reused.

## Not verified

Kaminsky's treatment of the Adamites (reviewer knowledge). Publication years and rights of the works in rows 44 to 54 and 29 to 41 (no external instrument). The identification of the *Diarium* with Březová. Whether the Notes' 1508 quotation is Comenius's or Seifferth's selection. The Registry rows at Confidence B were checked for structure only.

## Tool results

`python tools/check_live_commentary.py --surface worlds`: exit 0. The Registry rows still carry iso-date hits in the Added and Discovery cells, which V7.4 Step 2 requires. `python -m engine.m10.cli gaps hus`: Doc_01, Doc_02, Registry and Open_Gaps have no unmatched item. The command still fails with 85 findings, all in `Review-Artifacts/Doc02_Round1_Review.md`. Cause: that file's H1 title contains "Open Gaps", so `engine/m10/gaps.py` (`_OPEN_HEADING`) treats the whole file as an open-items section. The review artifact was not edited. Either the title or the checker needs a change, and both belong to the project lead.
