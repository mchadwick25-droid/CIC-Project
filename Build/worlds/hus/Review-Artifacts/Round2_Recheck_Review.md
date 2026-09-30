Simulated review — informational only, not an Article 31 substitute.

# Doc_01, Doc_02, Source Registry and gap ledger: Round 2 targeted recheck (hus)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** hus build-thread drafting worker (revision commit 954bb9ae6; audit trail 86e9cde0a; retitle ca9381d4a)
- **Round:** 2
- **Truncation check, method 1:** structural count. Doc_01: headings §1 to §10 present and in order (lines 13 to 214), 216 lines, ends on a complete sentence and a newline. Doc_02: headings §1 to §11 present and in order (lines 11 to 180), ends on a complete sentence and a newline. Registry: 50 numbered rows, every one with exactly 12 pipes; the numbers form exactly the set 1 to 24 and 29 to 54, and the only missing numbers are 25 to 28, which the header declares vacated; letters A 18, B 8, C 23, D 1. Open_Gaps: entries 1 to 25, R1 to R9 and E1 to E5 all present; the file ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD ca9381d4a. For all four files `wc -c` equals `git cat-file -s` (Doc_01 46,632 bytes; Doc_02 33,899; Registry 40,450; Open_Gaps 21,245), and `git hash-object` equals `git rev-parse HEAD:<path>` (Doc_01 99991a80…, Doc_02 f3449029…, Registry 4a29138c…, Open_Gaps e14885dd…). None of the four has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/hus/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Open_Gaps_Tracking.md`, as committed at HEAD ca9381d4a
- **Prior findings rechecked:** `Review-Artifacts/Doc01_Round1_Review.md` (8 P1, 12 P2) and `Review-Artifacts/Doc02_Round1_Review.md` (9 P1, 12 P2). The drafter's table in `Build/Ministry/Operations/Audits/hus_Round1_Revision_2026-09-30.md` was treated as claims and checked at source.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** 0 P0, 3 P1, 7 P2.

All seventeen prior P1 findings are fixed at source, and the one declined P1 (Van Braght) is correctly declined. The corpus figures are right by three methods. The drafter's correction of the Round 1 reviewer is right: Hus does name the third day in his own voice (Letter LXXIII). Every new quotation checked matches the vendored text. Nothing is invented. Article 29, the Representative and the registration of `hus` are left open.

The three P1 findings are all in new material or in the record behind it:

1. The strand ruling is attributed to the project lead, but the only record of it is an agent's instruction to the drafter, not the project lead's own words.
2. The new Forces lens says Rome's opposition is best documented "because its own writers kept the record". Its own paragraph above says the opposite.
3. Doc_02 §2 and Registry row 48 rely on a Lollardy file (candidate E3) for a transmission fact. The Registry's rule forbids that, and Open_Gaps section E says Doc_02 does not rely on any such file.

Each is a small fix. This was the second revision round of each document; under the build cycle's cap, one more substantial round remains before escalation.

## Scope 1: prior P1 findings, checked at source

Quotations were matched by script against the vendored files after whitespace, quotation-mark, spacing-before-punctuation and line-break-hyphen normalisation, then read in context at the loci named.

**Doc_01 Round 1**

| Finding | Status | Checked at source |
|---|---|---|
| P1-1 cup | Fixed | Letter LXXI heading at 11980; "do not oppose the sacrament of the Lord's cup, which was instituted of Christ" at 11986–11987; "prepare to suffer for the eating of the bread and the communion of the cup" at 12001–12002. Workman's note at 8815 and 8818–8819 sits before the Letter XLIII heading (8824, printed "XLUL"). §3 gravity 2 now says he defended it late but did not begin it. |
| P1-2 Letter VI | Fixed | "numbering, I suppose, nearly ten thousand" and "they begged me to translate it into our mother tongue" match; the contents line reads "read it in the Bethlehem". |
| P1-3 Unity non-resistance | Fixed | *Bohemia* 10111–10124: "As far as we can judge", "which soon became extinct, maintained in its entirety the teaching of Chelcicky, which included doctrines such as non-resistance to evil-doers", "accommodated its teaching to a certain extent to temporal ideas", "reconciled itself with the world … secured the future existence of the 'Unity.'" The footnote to the passage reads "Goll.", which supports the new risk line in §3 gravity 6. Tagged Inferential/Thin in §4 and in Doc_02 §8, consistently. |
| P1-4 strand finding | Fixed in the document; see P1-1 below for the record | Both alternatives are argued at full strength with their costs. Tábor's 33 of 115 years is right (1419–52 inside 1402–1517). The Goll passage is at *Bohemia* 9416–9420 ("did not wish to be considered as continuators of the Taborites"; "not justified by the facts of the case"). The Preface's "the Calixtines had forestalled the denomination of Hussites" is at Seifferth 4153–4154, and its praise of Tábor at 4081–4087. |
| P1-5 two grounds | Fixed | The census structure is now labelled portfolio-level (§4 Finding, §5). The Preface's "the leading principle of Huss, that the law of Christ is sufficient for the government of the church militant" matches. The cup appears only in the *Ratio* body ("not only the cup, but the bread", 4881). §4 now says continuity of the cup and of Czech-language Scripture is not shown for 1457–1517. |
| P1-6 tags | Fixed | (a) *Hussite Wars* 6324–6326 reads "Modern writers generally call the invasion of Bohemia in 1421 the second, and that in 1427 the third crusade", under the 1422 expedition. The count is now Contested. (b) The Adamites are Contested in Doc_01 §5, §8 and Doc_02 §3, §8. (c) Household discipline is Inferential/Thin. |
| P1-7 Article 4 | Fixed | The five commitments in §8 match Constitution V2.3 (`Build/reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx`, paragraphs 160–164) word for word, as does the "need not have recited the Creed" sentence (165). Each clause-level "shown" quotation matches: Letter XX, 5659–5660 ("the All- / powerful", joined); Letter XVII, 5309; Letter XXI, 5848; Letter XXXIV, 7591; Letter XXXIX, 8332; *De Ecclesia* p. 18, p. 34, p. 70 (5429–5434), p. 84. The "not shown" clauses are not in the two works (see Scope 3). |
| P1-8 1419 violence | Fixed | 1419 now names no group. *Hussite Wars* 5806–5810 ("They then attacked the Jews") for 1422. *Bohemia* 10757–10761: "stormed the three town halls … a large number of Germans and Jews were massacred", followed by "In 1485 … Kutna Hora". Cell 2B matches. |

**Doc_02 Round 1**

| Finding | Status | Checked at source |
|---|---|---|
| P1-1 Forces lens | Fixed, with one new defect (P1-2 below) | Doc_02 §6 now has a named Forces-lens paragraph. It answers all three of Step 2's questions (which sources, what silences, what survivorship) and names rows. |
| P1-2 corpus total | Fixed | See Scope 2. |
| P1-3 loci | Fixed | Row 2: the note is under Letter XVIII (heading 5392, printed "XVHI."; the note at 5440, and the reckoning from 1400 at 5442–5443). "hopelessly doctored" at 5650 is under Letter XX (5617). Row 7: p. 70 is in ch. VIII (5274); ch. VII is at 4814 and ch. IX at 5509. |
| P1-4 in-window Unity text | Fixed | Row 43. Seifferth 548–555: "not contrary to the word of God, we willingly conform to them" (552), cited "Ad Doctoremi Augustinum, a.d. 1508" (554–555). The words before it are garbled ("nseful … hnitftil"), and the row rightly quotes only the clean words. Notes 8262–8264: "We are not ashamed of our priests because they labour according to their ability with their own hands to procure their food", cited "Fasciculus Berum Expetendarum et Fugiendarum, fol. 88" (8267–8268). Doc_02 §1, §6, §7, the Registry row 32 and Open_Gaps entry 1 are all restated as "fragments only". |
| P1-5 Adamites | Fixed | Contested throughout. *Hussite Wars* 5382–5392 gives Březová's account of the expulsion of "more then 200 people of both sexes from Tabor". Kaminsky is carried as a to-do (Open_Gaps entry 22), not as a claim. |
| P1-6 Piccolomini licence | Fixed | Doc_02 §7 item 3 and row 11 now say quotability waits on the Library's ruling, and that nothing is licensed for quotation. The corpus-map note's "the scan is clean, not flagged as garbled" is at line 81 of the corpus-map file. The preface heading "AD ALPHONSVM REGEM ARAGONVM" matches, and line 421 reads "quxpartjmyidimj,parrim vero auditu accepimus" (partly seen, partly heard), as Doc_02 §2 says. |
| P1-7 missing rows | Fixed | Rows 44–51 (and 52–54 for the Round 1 recall test and PRESS answers). Loci checked: Loserth at *Life & Times* 1035 and 16586 and Schaff 1544; Nedoma at *Hussite Wars* 5361; Kybal at *Life & Times* 193–196 and 16577; Flajšhans at Schaff 1676; *Historia et Monumenta* at Schaff 2225–2229; Palacký at *Hussite Wars* 4121 and *Life & Times* 2487 and 3074; Erben at Workman 1374–1375 ("Fez, Erben, and Falacky"). Each row is at C, which fits the header's rule (not vendored). |
| P1-8 Van Braght | Correctly declined | See Scope 4. |
| P1-9 R2 | Fixed | Schaff 2265–2267 reads "It is to be hoped that Dr. Flajshans will add to his other editions of Huss's writings a new edition of this". R2 and row 9 now say so. |

## Scope 2: the corpus figures, by three methods

The eight files the corpus map assigns to this world (`cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml`) were counted three ways:

1. Decoded UTF-8 length of each file, in Python: 6,654,664 characters in all.
2. `cat` of the eight files piped to `wc -m` under `LC_ALL=C.UTF-8`: 6,654,664.
3. `cat` of the eight files piped to Perl `length` under `-CSD`: 6,654,664.

The two Hus files are 735,667 and 672,550 characters, 1,408,217 together, which is 21.16 per cent. Doc_02 §1's "about 6.65 million" and "roughly a fifth (21 per cent)" are right. The shelf holds 315 `.txt` and `.xml` files. A whole-word, case-sensitive search for "Hus" or "Huss" matches 53 files, and a whole-word, case-insensitive search matches 106, as the saturation statement says. The Brethren-term search matches eight files: the five real ones and three false ones the statement names.

## Scope 3: the new material

**Doc_01 §8, the rebuilt Article 4 check.** The drafter's new loci hold, and all three are in Hus's own voice:

- The third day: Letter LXXIII (heading 12092, "To his friends at Constance"), 12168–12169: "that most patient and brave Soldier, although He knew He would rise again on the third day and overcome His foes". The Round 1 review's statement that the third day was not shown was wrong, and the drafter was right to correct it.
- Three days in the tomb: Letter XXVIII (heading 6437), 6615: "Christ was the Head of the Church, as without doubt He was, for the three days He was in the tomb."
- The ascension: *De Ecclesia* ch. IV (heading 3650), under the running head "28 THE CHURCH" (3685), line 3716: "the man who descended from heaven and who ascended again into heaven, as is said in John 3 : 13". Hus goes on in his own words: "the ascent was a local movement by which he took with himself the other parts of the body." That makes it his own statement, not only a citation (see P2-7).
- Session and return: p. 70 at 5432–5434.
- "who shall judge the living and the dead" (12568–12569) is Paul's charge to Timothy, which Hus quotes. The document is right not to count it as his own wording.

The Result is stated at the right strength: commitment 4 largely shown, commitments 1, 2, 3 and 5 shown in substance and not in the Nicene wording, and the unshown clauses silent, not denied. The Unity limit is stated honestly. Open_Gaps entry 4 matches.

**Doc_01 §5 and §9, the ruling.** The document states one world with three strands as a ruling. It gives both alternatives and their costs at full strength, and it labels the census grouping as a portfolio-level reason. It also says that Doc_04 tests the ruling. That meets Round 1 P1-4. The record behind the attribution is P1-1 below.

**Doc_02 §6, the Forces lens.** Checked: "the edict of Wladislaw against the Brethren" (Seifferth 423); Tábor taken in 1452 by "the utraquist King George of Podebrad" (*Life & Times* 15475–15478), which supports "an Utraquist commander"; the survivorship inference for the Unity, tagged Inferential/Thin. The last survivorship bullet is P1-2 below.

**Registry rows 42–54.** Every locus listed under Scope 1 (P1-7) was read. Row 42's letter A is earned: letter heading plus both passages. Row 43's letter A is earned: both passages were read, and each is marked by its printed citation and by Note [15]. Rows 44–50 name a vendored locus, so each is a real snowball find at C. Row 51 (Novotný) is marked as builder knowledge, and rows 52–54 are marked as knowledge of the field. Both are honest, and C fits a real author and work with no locus checked. No row claims more than it holds.

**Other new or revised claims checked at source:** Lützow's "obtained in 1402 the important appointment" (*Life & Times* 3429–3430); "Many Jews flocked to Conrad's sermons"; "desperate and fanatical courage" (Gillett); "form part of the great struggle between Slav and Teuton" (*Hussite Wars* 2036–2037); Creighton's "Everything Hus writes is the result of his own soul's experience"; "At an early period of this association it assumed the name" (Seifferth); the *Letters* Preface's "Lord and Giver of Life". All match.

**Confidence tags in the new material.** Only the five levels are used, and none is used as a sixth "absent" level. No new tag is too strong. The Unity's non-resistance and its Great and Small parties, the 1508 fragments, the *Diarium* identification and the Unity's survivorship chain are all Inferential/Thin. The crusade count, the Adamites and the Tábor–Unity link are Contested. One wording issue is at P2-2.

## Scope 4: the declined P1 and the vacated rows

**Van Braght (Doc_02 Round 1 P1-8).** The decline is correct under the rule the Registry header states. The rule is that a vendored work assigned only to another world gets no row here, and that placing it here is a cross-world decision for the project lead. The corpus map assigns `van-braght_martyrs-mirror_sohm1886.txt` only to `the-anabaptist-movements`. Candidate E2 describes it accurately: "not become a Christian to swear" at 47376; Mehrning at 47514 and 47612; "Praguers" and "Taborites" at 47622; the "confession of the Taborites, drawn up A. D. 1431" at 47614; the "Bohemian brethren" note at 47774–47776. The saturation statement no longer overclaims. This is not a finding. Cross-world placement stays with the project lead.

**Rows 25 to 28 vacated.** The four rows (Foxe, two Luther rows, Wyclif) were deleted, and their numbers are declared unused and not reusable. The Registry is append-only once merged. This branch is not merged (06551b798 is not an ancestor of `origin/main`), and the rows were created in a draft that had not cleared review. Vacating them is therefore within the rule. The header states the gap, and the Open_Gaps E section takes the content. A tombstone line per number would be clearer (P2-4). The same judgment covers R1's change to "Not used" in Open_Gaps.

## Scope 5: reserved decisions and invention

- **Article 29.** Left open (Doc_01 §1 and §9 item 2; Open_Gaps entries 5(b), 6 and 25). The phrase "the one-world ruling puts the Unity's living-tradition claim inside this world" is a consequence of the strand ruling. It does not name a present-day tradition.
- **Representative identity.** Not decided or implied (Doc_01 §5 last paragraph and §9 item 3; Open_Gaps entries 5(c) and 14).
- **Registration of `hus`.** Left open (Doc_01 §9 item 4; Open_Gaps entries 5(d) and 8(d)). `records/worlds/hus.yaml` does not exist, as stated.
- **Invention.** Nothing was found invented. Every builder-knowledge item (publication years in rows 44–54, Novotný, the *Urkundliche Beiträge* lead in R6) is marked as such.

## Scope 6: readability of Doc_01

Scored with `engine.m7.turn_readability.score_turn`, with markdown symbols and code spans stripped:

- Whole document: FK 7.7, FRE 58.8, confirming the drafter's figure. The FRE was 51.6 in Round 1.
- Drafter's own prose, with every quotation in double quotation marks removed: FK 7.1, FRE 60.3.
- By section: §1 54.9; §2 56.9; §3 56.1; §4 60.6; §5 56.6; §6 51.3; §7 56.0; §8 72.4; §9 65.2.
- Sentences: 621, averaging 11.8 words; 37 run past 25 words, and most of those carry a quotation.

**Judgment: acceptable, not a P1.** The NorthStar target governs participant-facing text. Doc_01 is a construction document, and its quotations must stay verbatim, so the drafter cannot shorten them. With the quotations removed, the drafter's own prose meets FRE 60. The document moved seven points toward the target, and its average sentence length is inside the Writing Standard's range. The one real residue is §6, which is 51.3 even though it holds few quotations. Its catalogue sentences, "What it was refusing" and the six-cell table, can be split. That is P2-3.

## Scope 7: tool runs

- `python -m engine.m10.cli gaps hus`: `gaps: PASS`, exit 0. The Round 1 failure (85 findings in the Doc_02 review) is cleared by the retitle in ca9381d4a.
- `python tools/check_live_commentary.py --surface worlds`: exit 0. For the four files:
  - Doc_01: 1 hit, PROTECTED (route-cue, the §9 heading).
  - Doc_02: 1 hit, PROTECTED (route-cue, the §10 heading).
  - Open_Gaps: 30 hits, all PROTECTED.
  - Registry: 50 hits (21 KEEP, 29 REWRITE), all iso-date, one per row. They are the Added and Discovery cells that Framework V7.4 Step 2 requires, the same schema data Round 1 cleared.
- No process narration or change history was found by reading.

## Findings

**P1-1. The strand ruling is attributed to the project lead on a relayed record only.**
- Where: Doc_01 header, §4 Finding, §5 "Ruling", §9 item 1; Open_Gaps entries 5(a) and 13.
- Doc_01 §5 says the ruling "is recorded in `Build/Ministry/Operations/Audits/hus_Round1_Revision_2026-09-30.md`". That file says: "The record of the ruling is this instruction". The instruction it means is the orchestrating session's instruction to the drafting worker. It is not the project lead's own words.
- The build cycle's rule is that nothing is attributed to the project lead without "a verifiable record that the project lead actually said or wrote it", held to the same bar as Frozen. From this context I cannot confirm that the ruling is the project lead's own. I also have no evidence that it is not.
- Fix: add to the audit file the project lead's own words, verbatim, and where and when they were given (session and date). If no such record exists, restate §5 and §9 as a recommendation awaiting the project lead's decision.
- None of the four documents needs any other change for this. An independent recheck should confirm the record.

**P1-2. The Forces lens contradicts itself on Rome's record.**
- Where: Doc_02 §6, the last "Survivorship patterns" bullet: "Rome's opposition is the best documented force because its own writers kept the record, and Piccolomini is one of them."
- The paragraph just above says the opposite: "Nothing on the shelf is a papal or conciliar document. There are no bulls, no Council acts and no crusade sermons in their own words … So the pressure is visible, but its own voice is absent."
- On this shelf, Rome's side has one witness, Piccolomini. Everything else is Hus, Bohemian-sympathetic historians and a Moravian editor. "Its own writers kept the record" is not supported by the vendored evidence. The Framework's survivorship question is the one this bullet answers, so the error sits in the required content.
- Fix: say what the shelf shows. Rome's pressure is well attested, but mostly through its targets and through later historians. Only one hostile contemporary, Piccolomini, speaks for Rome's side.

**P1-3. Doc_02 and the Registry rely on a file assigned to another world.**
- Where: Doc_02 §2, Transmission History ("Loserth's Wyclif volume gives the place of the 1558 edition as Nuremberg"), and Registry row 48 ("The note in Loserth's Wyclif volume (`wyclif_de-ecclesia-lat_loserth1886.txt`, line 676) reads 'Norimbergae'").
- The reading itself is right: line 676 has "Historia et monumenfa Johannis Hus (Norimbergae". But the file is assigned only to Lollardy, and it is candidate E3.
- The Registry header says such a work "is recorded as a candidate … not here". Doc_02 §1 says "no Registry row licenses anything from them". Open_Gaps section E says "Doc_02 does not rely on any of them".
- Doc_02 uses it anyway, in support of a transmission claim ("the place is not settled in the vendored evidence"), with no row. The Framework's checkpoint rule forbids that. It also makes the section E statement false.
- Fix: take the Nuremberg reading out of Doc_02 §2 and row 48, and carry it under E3 as one reason E3 matters. R2 may keep it as a lead. The alternative is to get the project lead's authorisation for E3 first.

**P2-1. Doc_01 quotes Piccolomini as evidence, and Doc_02 licenses nothing from the scan.** Doc_01 §5 ("What holds across strands") quotes "Martyrum honores" as evidence of what holds across strands. It notes that quotability is unruled, and the words are legible at line 4087. Doc_02 §7 item 3 says "nothing from it is licensed for quotation". Make the two match: paraphrase in Doc_01, or wait for the Library's ruling.

**P2-2. The creed row in Doc_02 §8 tags an absence.** The row says "Inferential/Thin for the Nicene wording, for 'incarnate of the Holy Spirit' and for 'Lord and giver of life'". The row's claim is "in his own words", and for those clauses there are no words. Doc_01 §8 and Open_Gaps entry 4 rightly call them silent, not denied. Carry those clauses as absent (not shown in his words). If an inferential rating is wanted, state the inference: that he held them, from the trial's Athanasian creed and the plain-sense test.

**P2-3. Doc_01 §6 readability.** §6 scores FRE 51.3 in largely the drafter's own prose. Split the catalogue sentences, "What it was refusing" and the long table cells. §1 (54.9) could also use one more split. The whole-document figure is acceptable (Scope 6).

**P2-4. Vacated Registry rows have no tombstone.** Readers of the Round 1 review who look up "row 25" to "row 28" find no line. Add one line per number, such as "25 | vacated 2026-09-30; see Open_Gaps E1". Carry it only in the table's own cells, with no narration.

**P2-5. Rights wording is uneven for rows that are not vendored.** Rows 45, 46, 47, 50 and 51 say "Rights unchecked". Rows 44, 48 and 49, whose dates are of the same kind, say "public domain by date … the Library must verify". Every one of these works carries a stated date before 1930. Use one formula.

**P2-6. Minor loci.** Row 43: the "Minutes of an old Synod" begins at line 8217, not 8218, and the 1508 quotation sits inside Note [15] ("to page 121", 8214). Row 7: "in judgment" is at 5434, one line past the 5429–5433 given.

**P2-7. Parity in the Article 4 evidence.** Doc_01 §8 counts the ascension from *De Ecclesia* p. 28, but that sentence ends "as is said in John 3 : 13". The same section discounts "who shall judge the living and the dead" as a scripture quotation. The ascension still counts, because Hus's next sentence glosses it in his own words. Say so in §8 and in row 7, so the two cases are visibly treated alike.

## Not re-verified

- Registry rows 5, 6, 8, 12, 15, 17, 19 and 21 (B), and rows 29 to 41, beyond their numbering and pipe count. They were unchanged except for rights wording.
- Doc_02 §4 and §5, and Doc_01 §2 and §7, beyond the revised sentences. The unchanged quotations there were covered by Round 1 and by the script match above.
- Publication years and rights of rows 44 to 54. No external instrument was used.
- Kaminsky's treatment of the Adamites (Open_Gaps entry 22). It is still reviewer knowledge from Round 1.
- Whether Lützow's 1909 statement of the 1402 appointment is independent of Workman's sources.
- The identification of Gillett's *Diarium* with Březová (still tagged Inferential/Thin).
- Workman's narrative of the burning ("Who was conceived of the Virgin Mary") beyond the phrase match.
- The Step 0 files and the Round 1 review files, which were read only for what this recheck needed.
