Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry: targeted recheck of the Registry rulings and the new rows of 2026-09-29 (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** Library-thread drafting worker (commits 3da8738f2 and 75c29ccb0; commit trailers read "Claude Sonnet 5.5")
- **Round:** 33 (a targeted recheck of the project lead's Registry rulings and of rows 243–272; not a new revision cycle)
- **Truncation check, method 1:** structural count. Registry: 274 table lines (header, separator, 272 rows), every one with exactly 12 pipes; the 272 numbered rows form exactly the set 1 to 272, no gap and no duplicate; the file ends on a complete sentence and a newline. Doc_02: headings §1 to §10 all present, in order; §10 ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD 75c29ccb0. `wc -c` equals `git cat-file -s` (Registry 418,997 bytes; Doc_02 89,472 bytes), and `git hash-object` equals `git rev-parse HEAD:<path>` for both files (Registry ead2d754…, Doc_02 f2bf8996…). Neither file has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/lpc/Doc_02_Source_Ecology.md`, `Build/worlds/lpc/Source_Registry.md`, as committed at HEAD 75c29ccb0
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish (P0/P1/P2 correspond to HIGH/MEDIUM/LOW in Rounds 1 to 30).

## Verdict

**Not clear.** 0 P0, 3 P1, 6 P2.

Every ruling is applied as ruled. Both P1 findings of Round 32 are fixed: the Registry's sweep paragraph now says `csel-dev` holds Cyprian and Optatus, and Doc_02 §3 counts fifteen secondary works. Its P2-1 and P2-2 (rows 217 and 214) are fixed too. The census figures are right by two methods. Every new TEI row matches its file at the title, the opening, the close, the page count, the licence line and the scan lines.

The three P1 findings are: a Boundary Status outside the Template's two values (row 265); a reason Doc_02 gives for row 229 that the file does not support; and new change-history text in the Discovery cells of rows 243–248.

Nothing found misstates the historical world or invents a source.

## Scope 1: the rulings

| Ruling | Applied | Checked at source |
|---|---|---|
| Row 44 at A | Yes | `XVI, 5, 21 (392 lun. 15).` at 86853; `denis libris auri viritim` at 86856; `censemua` at 86857; `denis libris auri proposita condemnatione multentur` at 86863; `XVI, 5, 52 (412 lan. 30>.` at 87872; `circumcelliones argenti pondo decem` at 87882. The Licensed-For is only the statute, and the statute's operative and penalty clauses were read, so A fits the rule. |
| Row 33 at B | Yes | Bibliographic row; B matches rows 30–32. |
| Rows 11 and 14 narrowed; 243 and 244 at B | Yes | Row 11 licenses four letters: `vii.1.XXXI` 25749 (§4 at 25841, the Valerius passage 25851–25857), `vii.1.CCXIII` 55243 (§4 at 55357, 55367), `vii.1.CXXVI` 44459 with `411.` at 44463, `vii.1.CCXI` 54736 with `423.` at 54740. Row 14 licenses one locus: `div4 n="51"` at 16903, the chair sentence at 16912 (one marker is off by a line, P2-3). Row 243's split is 17 + 11 + 2 + 138 = 168. Row 244's Book markers are at 15292, 15346, 15751 and 18192. |
| Rows 227, 228, 230 at B | Yes | 227: `SERMO PRIMUS` 699, `CLASSIS IV.` 106615, `CLASSIS V.` 117124 (P2-6). 228: `TRACTATUS I. CAPUT I.` 4549, `TRACTATUS CXXIV. CAPUT XXI.` 46242, 46795, 46895. 230: `SERMOJNES INEDITI.` 40, 3105, `SERMO I.` 3798. |
| Rows 191 and 193 at C on OCR grounds | Yes | Both state that C rests on OCR, a ground the rule's text does not name. Row 193's CSEL 58 claim is now limited to the Internet Archive (Round 32 P2-7). |
| Rows 231 and 232 split, one row per status | Yes | 231 and 232 now carry only the three Cyprianic acts. Knopf: `13. Akten Cyprians.` 4820, opening 4823; `15.` 5166/5169; `16.` 5629/5632. Gebhardt: `XI.` 6471, 6474–6475, 6481–6482; `XII.` 6917, 6920; 7492. Rows 245–248 are Excluded on the grounds of rows 28 and 204. Their markers are real: Knopf 164, 2437, 2438, 2441–2442, 168, 2909, 2910, 2913; Gebhardt 439, 3486, 3489, 3492. |
| Row 229 left unsplit | Yes | The nine tractatus are named as unassessed, with no row and no status. `MCMXVH` 100, `Septembris MCMXVII` 118, `TRACTATVS TRIQINTA TRES` 1775, `TRACTATVS NOVEM` 10303. |

The OCR counts were reproduced exactly for Knopf (6 of 5,964) and Morin (5 of 11,209). For rows 266 and 267 they were reproduced to within a few lines. The small difference comes from how non-ASCII letters are counted.

## Scope 2: new rows

Calibration rule, as the Registry states it: "Confidence **A** is used only where a row's Licensed-For content was itself directly read and verified against the vendored text … **B** is used where a specific work or locus is named accurately but was not independently re-checked against the vendored text."

**Rows 249–263 (Cyprian TEI, 15 files) and 264–265 (Optatus TEI).** I checked every row by script against its file:

- the path exists;
- line 17's title element matches the row;
- line 49 is the CC BY-SA 4.0 licence element;
- the header's Rights line reads `CC BY-SA 4.0 … NOT public domain as a digital edition`;
- the `urn:cts` and `csel-dev` path are in the header;
- the opening and closing phrases are at the lines the row gives;
- the `<pb/>` count and the first and last `n` match the row (row 261 states only the first, and says why);
- the scan line range is in the header, and the scan's lines at both ends carry the heading and the close.

All seventeen rows pass. Every row gives B, and each says why: the text between opening and close was not read, and the file is machine-corrected. Row 256 quotes the TEI title `De Mortalite`, which is what the file prints. Row 264's scan markers check out: `LIBEE PRIMUS.` 2229, close 13187–13189. So do row 265's: `Appendix` 13206, `dirigamus!` 15283. No row says a file is held when it is not, or not held when it is.

**Rows 266–272 (Petschenig, CSEL 52–53).** Every marker was read at source:

- 266: 24199–24201, 24752–24753, 24769 `LIBKK PRLMUS.`, 24772, 24774, 25771, 25773, 33390, 33392, 36657–36660 `pai nostra`, and §118 at 29228, with the chair sentence at 29239–29242.
- 267: `V.` 36699, 36701–36702, 36712, 36718 `Memini8tis`, 41765–41767 `Abiahae`; the Praefatio at 24361–24363, 24495 (`ubi esset ecclesia` follows at 24499) and 24523.
- 268: `VIII.` 62771, 62773, 63022, the three `COLLATIO` headings 63030, 63478 and 63568, the opening 63032, the close 66054, and 66064 `CCM`.
- 269: `VIIIL` 66509, 66511, 66523, 71451, 71467, 71473, 71487.
- 270: `X.` 71495, 71497–71499, `Gratianopolitanus 152` 71502, 71507, 72026–72029, 72032; Praefatio 60755–60762, 60766–60767, 24466–24472.
- 271: `XI.` 72035, 72037, 72044, 72049 `Gloriosissirais`, 72770, 72782, 72784, 72802.
- 272: `XII.` 73562, 73564, 73575, 77170 `SECDNDUS`, 73578, 78570, 78578, 78580; the date `Circiter annum 420` at 60809.

The rights basis (public domain, 1908–1910) is recorded at row 214 and matches the file header. On letters: 266 is at B, with the reason stated; 267–272 are at A (P2-1).

**Rows 214–217.** Round 32's P2-1 is fixed: `Constantine frater` is now cited at 60985, and the file has it there. Its P2-2 is fixed: row 214 now reports the current header (CSEL 51, 52 and 53; `Rights: Public Domain`) and puts the G5 note in `REGISTRY.yaml`.

## Scope 3: Doc_02

- **Census (§1), counted two ways.** A YAML parse of `latin-pastoral-congregational-christianity.yaml` gives 173 raw, 153 `tradition` and 151 distinct titles. `grep` gives 173 `- work:` lines and 153 `role: tradition` lines (one further match is inside a note). The next-largest files are as stated: `latin-apologists` 100/97/45 and `alexandria-catechetical` 69/61/61. There are twenty `context` entries. Seventeen are modern works dated 1894–1930, and three are ancient, as stated. The two duplicates are as stated. The corpus map has 15 Cyprian TEI entries and one *Contra Litteras Petiliani* entry, so the sixteen new second witnesses are right. The arithmetic 153 − 2 − 55 = 96 holds.
- **§3, fifteen secondary works in seventeen files.** Recounted: Monceaux I–III (three files), von Soden ×3, Harnack, Delehaye, Koch ×3, Poschmann, d'Alès, Benson, Mesnage, Toulotte and Audollent. That is fifteen works in seventeen files, and every file is in `cic/texts/`.
- **§1, "nine further anti-Donatist works … in Latin only" (rows 215–217, 267–272), and "eleven … from Petschenig's CSEL 51–53" (rows 214–217, 266–272).** Both counts are right.
- **The sweep paragraph.** Registry line 361 now reads "It holds Augustine (41 files), Cyprian (`data/stoa0104a`, 15 works), Optatus (`data/stoa0215a` …)". Doc_02 has no `csel-dev` statement to contradict it. Round 32's P1-A is fixed.
- **§2 (line 47), the Latin gap for the Sermons, Tractates and catechetical works.** The catechetical and Tractates parts are true at source: row 226 for *De catechizandis rudibus*, row 200 for *De doctrina christiana* and the *Enchiridion*, and row 228 for the Tractates. The Sermons part has two errors (P1-2 and P2-2).

## Scope 4: truncation, commentary, counts

Two truncation methods, both clean (header). `python tools/check_live_commentary.py --surface worlds` exits 0.

For these two files, I compared the classifier's output at HEAD~2 (dfb3bd01b) with HEAD:

- Registry REWRITE lines rose from 66 to 73, and ROUTE lines fell from 8 to 7.
- Doc_02 is unchanged: 1 REWRITE, 5 ROUTE.

The seven new REWRITE lines are rows 243–248 and row 11. Row 11's line moved from ROUTE to REWRITE. See P1-3.

## Findings

**P1-1. Row 265, Boundary Status: "Not assessed for this world …".** `Source_Registry_Template.md` (the Boundary Status field and its assignment rule) allows two values only, Native or Excluded, and requires one for every source. The ruling on row 229 kept its nine unassessed tractatus off the table for this reason. Row 265 puts an unassessed item on the table with a value the Template does not allow. Assign Native or Excluded, with the ground. If the answer is not yet known, the choice goes to the project lead.

**P1-2. Doc_02 §2, line 47: the Sermons "are vendored in Latin as second witnesses only, because their scans misread many words (rows 227, 229 and 230 …)".** This is true for rows 227 and 230, whose headers say so. It is not true for row 229. The Morin header says nothing about misreads, and row 229's own count is 5 flagged lines of 11,209. The text reads clean at lines 2000–2012 and 6000–6008. Row 229 bases its second-witness status on something else: it is a first edition, and the only Latin witness of those sermons. Every Latin file here is a second witness under `cic/texts/INTAKE.md` anyway, whatever the scan quality. Give row 229's reason, or drop the causal clause.

**P1-3. Rows 243–248, Discovery column: change history in a live file.** Row 243 reads "body-level claim carried apart from row 11 / 2026-09-29". Row 244 has the same wording for row 14, and rows 245–248 read "portion of row 231 [232] carried apart from it / 2026-09-29". The classifier marks all six REWRITE. The Registry's REWRITE count went up in this edit (66 to 73), which is the opposite of what the project rule requires. The rule is that an edit to a live file removes the commentary already in it. The Discovery cell should name the channel, instrument and date only. Each row's Source cell already says which row carries the rest of the work.

**P2-1. Rows 267–272 at A, row 266 at B.** All seven rows were read to the same depth: headings, opening, close, and the testimonium or Praefatio. Row 266 gives B because the use it licenses was checked at one sentence only. Rows 249–265 give B because "the text between was not read". Rows 267–272 give A with no stated reason, and each says "The work's content has not been read beyond the markers above". A defensible reason exists: the Licensed-For of 268, 269, 271 and 272 is the work's identity and kind, and the markers verify that. Rows 215–217 set this pattern, and Round 32 accepted it. Rows 267 and 270, though, license "the Latin text". Add each row's Confidence sentence, as every other new row has.

**P2-2. Doc_02 §2, line 47: "Still not vendored in any Latin edition: … the sermons outside the Migne and Morin and Caillau collections".** The *Sermo ad Caesariensis ecclesiae plebem* (row 270) is a sermon outside those three collections, and it is vendored in Latin in Petschenig. Name it as the exception.

**P2-3. Row 14:** the paragraph `v.v.iv.li-p3` is at line 16910, not 16909. Line 16909 is blank.

**P2-4. Row 268:** the *Retractationes* pointer is quoted as `PAG. 177, 12`. Line 66062 prints `(PAO. 177, 12 ED. KNOELL)`. Rows 266 and 269 quote `PAO.` as printed.

**P2-5. Row 264, Boundary Status:** the cell holds a sentence of reasoning after "Native". The shelf and census facts belong in the Verification Note, which already states them.

**P2-6. Row 227:** it puts `CLASSIS V` and `SERMONES DUBII` both at line 117124. Line 117124 is `CLASSIS V.`, and the next line, 117125, prints `SERXffONES DUBII.`

## Not verified

- The per-work OCR counts for rows 268–272 and rows 227, 228 and 230 were not recomputed.
- The grep file counts in the Licensed-For cells of rows 267–272 (`Breviculus` 11, `Contra partem Donati` 10, `cum Emerito` 10, `Gaudentium` 17 and the rest) were not recomputed.
- The first group of the fifty-five second witnesses (the twelve entries Round 32 already checked) was not recounted item by item. Only the two new totals (27 and 16) and the final arithmetic were.
- In the TEI files, the text between opening and close was not read, as in the rows themselves.
- Doc_02 sections outside §1–§3 and §7 were not re-read.

## Outside this scope, noted only

- **Doc_02 §7, line 120:** "no row in `Source_Registry.md` dates from within this 133-year gap" (258–391). Row 27 (Optatus, *Against the Donatists*, Native) conflicts with this, and so do rows 64 and 264, which treat the same text as Native. Optatus wrote inside that interval. Row 265's documents may conflict with it too, but the row assigns them no date. Not fixed here, as instructed.
- Row 11's Source cell still describes the whole 138-letter body, though the row's A now covers four letters. Row 243 carries the same description. This is consistent with the ruling, but a reader has to rely on the Licensed-For cell to see the narrowing.
