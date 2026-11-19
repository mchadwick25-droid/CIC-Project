Simulated review — informational only, not an Article 31 substitute.
# Second cap-ruling targeted review: `rcg` Doc_02 Source Ecology and Source_Registry

- **Reviewer model:** Opus 5.5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** second cap-ruling reviewer (fresh Opus 5.5 subagent, session_01JMNsSDRcCWuRTZfKoJ41wk)
- **Drafter agent:** rcg cap-ruling fix-pass thread (PR #1286)
- **Round:** 5 (the second cap-ruling review; it does not count toward the three-round cap)
- **Truncation check, method 1:** structural read of both files: Doc_02 carries §1 to §11 in order and ends on a complete Document Log row (the 2026-10-29 fix pass); the Registry carries rows 1, 1a and 2 to 19 in sequence (20 rows), then the "Named acquisition gaps" and "Living-document protocol" sections, and ends on a complete sentence
- **Truncation check, method 2:** byte comparison: each working file's byte count (Doc_02 41,629; Registry 15,383, by `wc -c`) equals its blob size on `origin/main` at `16dbad2e` (`git ls-tree -l`), and each file's last bytes are a complete line ending in a newline (`od -c`)
- **Documents reviewed:** `Build/worlds/rcg/Doc_02_Source_Ecology.md` and `Build/worlds/rcg/Source_Registry.md`, as on `origin/main` at `16dbad2e`
- **Date:** 2026-10-29

**Ruling under which this review runs.** The System Hub Decision Log entry "2026-10-29 - Cap ruling: rcg Doc_02 and Source_Registry, second extra review (project lead)" (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`) names this file. Under it, the narrow fixes to the first cap-ruling review's findings are checked by one more targeted Opus 5.5 review that **does not count toward the three-round cap**. If this review does not clear, the specific open findings go back to the project lead, and no further round runs on the build thread's own initiative. The same entry leaves Step 0's word-count line for the project lead to direct, so Step 0 is not judged here.

**Scope.** A targeted recheck. It takes each of CR-1 to CR-7 from `Doc02_CapRuling_Review.md` against the current two documents, and re-derives every changed claim, figure, quotation and locus from the vendored files in `cic/texts/`. That includes the drafter's further changes: Paul the Deacon, Gregory of Tours Book X, holdings §8, Registry rows 17 to 19, the Moralia ellipsis account, the Lombard loci, and the endnote locus `iii.v.i.xxx-p7`. It also looks for errors the edits introduced and for any "not vendored" claim that is still false.

## Verdict

**Verdict: SUBSTANTIAL REVISION REQUIRED (narrow). Not cleared; not Approved to proceed.**

All seven findings of the first cap-ruling review are closed. Every changed quotation is word for word against its file, and every changed figure recounts by two methods. Two findings remain substantial.

- **CR2-1 (MEDIUM):** Doc_02 §2 says no Constantinopolitan source is vendored. One is: John of Ephesus, written inside this world's window, with a passage on Patriarch John the Faster.
- **CR2-2 (LOW-MEDIUM):** the new Registry row 19 gives the *Liber Pontificalis* lives for 560–590 Native status as primary sources. Row 15 excludes the next life in the same compilation as "a later compiled record". The volume's own introduction dates all full texts after Gregory's death. Doc_02 §2's "every Native primary source is his own writing" is also now contradicted by rows 12 and 19.

Three LOW findings (CR2-3 to CR2-5) are cosmetic citation slips. Under the ruling, CR2-1 and CR2-2 go to the project lead.

## Prior findings (first cap-ruling review), status and evidence

| Finding | Status | Evidence |
|---|---|---|
| CR-1. Register word count and Moralia ratio | **Closed** | Doc_02 §1 (lines 17, 28) now gives about 261,000 words with endnotes, about 227,000 without, and ratios of 3.9 and 4.5. Recount, method A (line ranges, tags replaced by spaces, `wc -w`): `npnf212` lines 30953–48476 (div `iii.v`, Books I–VIII; Book headings at 30955, 33953, 36116, 38397, 40290, 42876, 45140, 47170) give 158,871, or 135,584 with `<note>` elements removed; `npnf213` lines 826–10408 (divs `ii.v`–`ii.x`, Books IX–XIV) give 102,366, or 91,427. Totals: 261,237 and 227,011. Method B (XML parse with `lxml`, text of the same divisions): 157,141 + 101,390 = 258,531 with notes, and 134,267 + 90,673 = 224,940 without. Method B runs about 1% lower because it joins words that touch across a tag. Both methods agree with the document's rounded figures. Moralia: `wc -w` over the four files gives 1,022,290 exactly. 1,022,290 / 261,237 = 3.91; / 227,011 = 4.50. `Superseded_Claims.md` 1.2 now points to 3.18. Step 0 lines 79 and 81 still carry the old figures. The ruling leaves that to the project lead, and `Open_Gaps_Tracking.md` entry 10 logs it. |
| CR-2. Gregory of Tours Book X called not vendored | **Closed** | §4 (line 55), §9 item 5 and Registry row 12 and its gaps section now say it is vendored in three witnesses. Checked: Dalton "HERE BEGINS THE TENTH BOOK" line 20149; deacon's report 20152–20169; "it first of all attacked Pope Pelagius" line 20164; "the whole people chose the deacon Gregory" line 20169; "sevenfold litanies" line 20275; Dalton's note "The sevenfold Litanies" line 29701. MGH "INCIPIT LIBER DECIMUS" line 31904, with X.1 at 31906–31918. Brehaut X.1 at 10274–10344, with the litany address left out ("[Because of the plague Gregory makes an address ...]", 10326–10327). The corpus map assigns all three files to `merovingian-gallic-christianity` (lines 171, 183, 195) and not to `roman-church-gregorian`. Gregory of Tours files also appear in other worlds' maps, which the document does not need to state. See CR2-3 on the scope sentence. |
| CR-3. Holdings stale; Ewald–Hartmann and Loomis files without lines | **Closed** | `python -m engine.m9.cli holdings rcg`, re-run on `16dbad2e`: 1,522 files; 2 by design, 14 in scope and unread, 150 out of window, 1,356 with no coverage entry. All match §8. The 14 named files match the tool's list exactly. Every file in `cic/corpus-map/roman-church-gregorian.yaml` has a §8 line: four Moralia volumes, `npnf212`, `npnf213`, the Dialogues, both Ewald–Hartmann files and Loomis. Loomis, the three Gregory of Tours files and Paul the Deacon show under "no coverage entry", as §8 says. `records/rcg/.gitkeep` exists, and the tool runs. Registry rows 17 to 19 exist. Row 17's paraphrase of the map note ("readable Latin with systematic OCR noise, critical apparatus interleaved") is accurate. |
| CR-4. Registry rows 4 and 8 verification notes | **Closed** | Row 4 now gives lines ~389–390, 469–470 and 548–555, with the scan's letters kept. That matches the file and §1. Row 8 now describes the headings as scan noise at ~3379 and 3393–3396, and the opening line at ~3407–3410. That matches the file: "Cbe OBnD of tbe jfirst IBook" at 3379, "€f)e g>econti ^oofc" at 3393, and the opening at 3407–3410, word for word with "blesse#by" and "Benedicts". |
| CR-5. Moralia ellipsis drops "I found myself" | **Closed** | §1 now quotes "... so under the cloak of the Ecclesiastical office, I found myself" ... "plunged on a sudden ...". That matches `bliss1844` lines 551–552 ("myself*^"). The claim that nothing is omitted is gone, and each gap is described. See CR2-4 on two line slips in that description. |
| CR-6. "Truces, tribute" locus | **Closed** | §1 line 24 and row 1a now cite ~22170–22206 (invasion; Agilulph at 22184), ~22228–22233 ("effecting truces with the enemy", 22231) and ~23156–23200 ("settled truce", 23159; "a second truce", 23200). A search of lines 22100–23700 finds no "tribute", and the word is removed from both documents. |
| CR-7. Smaller slips | **Closed** | Row 1 now names Book I Ep. XXXVI and Book VI Ep. LI. Checked: div `iii.v.i.xxvi` is "Epistle XXXVI. To Peter the Subdeacon." (line 32348), and `-p3` reads "Gregory, bishop, servant of the servants of God, to Peter the Subdeacon." Div `iii.v.vi.xxxii` is "Epistle LI. To the Brethren going to England" (line 44425), and `-p4` reads "Gregory, servant of the servants of God, to the servants of our Lord Jesus Christ." Row 4's Parts now match the corpus-map loci. §11 names `Doc02_RoundN_Review.md`. §1 now says the Register's endnote at `iii.v.i.xxx-p7` hedges the date. Checked: `-p7` is the endnote, line 32579, "The date of the letter before us, if rightly placed, is a.d. 591." |

## New findings

### CR2-1. MEDIUM (substantial). A Constantinopolitan witness from inside the window is vendored, but Doc_02 says none is.

**Location:** Doc_02 §2, *Limitations* (line 44): "Gregory's own account of John the Faster's claim and motives is not independently checked here against any Constantinopolitan source, none of which is currently vendored in this corpus."

`cic/texts/john-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` is the Third Part of John of Ephesus's *Ecclesiastical History* (tr. Payne Smith, 1860; `REGISTRY.yaml` line 3814, date_added 2026-09-25). A duplicate scan of the same translation is `john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`. John of Ephesus (c. 507–588, per the file header) wrote in Constantinople, inside this world's 560–604 window. At Book V.15 (from line 14772) he narrates how Maurice ordered the patriarch to arrest those who would not communicate with him. "But John the patriarch" (line 14789) refused in grief: "Think you that God will be pleased ..." (lines 14786–14812). The translator's note identifies him: "This was John the Faster, a very different character from John Scholasticus" (line 14813). The work's chapter list also names lost chapters on "the mercifulness and liberality of the patriarch John" (III.52, lines 1019–1020).

This does not touch the "Universal Bishop" title itself, since John of Ephesus died before the dispute. But it is an independent, contemporary, Constantinopolitan portrait of the same man whose "claim and motives" the sentence says cannot be checked. The holdings tool lists the file under "no coverage entry", so the error is a missed search, not a tool gap. This is the same kind of false "not vendored" claim as CR-2.

A smaller part of the same finding: §6 (line 70) says "No Lombard Arian, Istrian-schismatic, or Donatist primary source is currently vendored in this corpus." Donatist primary sources are vendored, for example `tyconius_liber-regularum_burkitt1894.txt` and `monumenta-vetera-donatistarum_migne-pl8.txt`. Both are fourth-century, and the tool marks them out of window. The sentence's meaning, that there is no voice of the Donatist remnant of the 590s, is right. But as worded it is false. The Registry's gaps section already scopes it correctly: "from within the window".

**Needed:** correct §2's sentence. Name the John of Ephesus file and what it does and does not cover, and give it a Registry row with whatever classification the build thread judges right. Scope §6's sentence to the window, matching the Registry. This review licenses no claim from John of Ephesus.

### CR2-2. LOW-MEDIUM (substantial). The new non-Gregorian Native rows contradict Registry row 15 and Doc_02 §2.

**Location:** Registry row 19 (Type P, Boundary Status Native) against row 15 (Excluded, Out-of-Boundary, "A later compiled record, not a within-window primary witness"); Doc_02 §2, *Visibility* (line 41).

- **Rows 15 and 19.** Both rows describe lives in the same compilation, Loomis's *Book of the Popes*, vol. I. Row 15 excludes the life of Gregory because the *Liber Pontificalis* is a later compilation. Row 19 then classifies the lives of 560–590, from the same compilation, as primary and Native, and gives no date of composition. The volume's own introduction says: "all forms of the complete text, in the shape that we have them, are products of the seventh century. The earliest recension or edition dates back perhaps to the first quarter of the century, not long after the death of Gregory I" (lines 973–976). On the file's own evidence, the 560–590 lives and the life of Gregory have the same standing. The two rows cannot both stand on the reasons given. This matters downstream: the Template hands only Native rows forward to Doc_03 (`Source_Registry_Template.md` line 21).
- **Doc_02 §2.** *Visibility* says "every Native primary source is his own writing". Registry row 12 (Gregory of Tours, P, Native) and row 19 (*Liber Pontificalis*, P, Native) are not Gregory's writing. §4 itself calls Gregory of Tours "not Gregory's own voice". The fix pass added these rows without carrying the change into §2, which the naming-and-propagation rule requires.

**Needed:** decide row 19's Boundary Status and Type on a basis consistent with row 15, citing Loomis lines 973–976. Then bring §2's *Visibility* sentence into line with the Registry. The overall finding, an evidentiary base that is almost entirely one man's writing, is not in question.

### CR2-3. LOW (cosmetic). Book X is used for more than "two phrases", and Registry row 12's note says only two were checked.

**Location:** Doc_02 §4 (line 55); Registry row 12, Licensed For and Verification Note.

§4 says that "beyond those two phrases this document uses Book X to support no claim". But it also quotes lines 20326–20327 ("could not rest till he came back from Ostia to see with his own eyes how the consecration was carried out"). It uses that passage and "related" for the eyewitness-deacon framing, and row 12 licenses it. The quotation is word for word, without the footnote mark after "Ostia". The framing is supported by "Our deacon, who was present, declared" (line 20316). The defect is only that the stated scope and the verification note understate what is used.

One reading point belongs with §9 item 5: the "he" who came back is ambiguous in Dalton. Brehaut makes it Gregory: "Our deacon did not leave until Gregory returned from the port to become bishop" (lines 10342–10344). The MGH Latin has *diaconus noster* as the subject and *de Porto* for "from Ostia" (lines 32134–32135).

### CR2-4. LOW (cosmetic). Two line slips in the Moralia ellipsis account.

**Location:** Doc_02 §1, paragraph after the Moralia quotation (line 30).

- **First gap.** The account says it runs from "by the" (line 390, "where the Leander footnote begins") to "At length being anxious to avoid all these" (lines 454–469). In the file, the footnote begins at line 393, and Gregory's text resumes at line 452 ("Ep. TO affairs'* of the Apostolical See"). The omitted words also run on to "inconveniences," (line 469), just before "I sought the haven".
- **Third gap.** It covers lines 548–549, "iVom ihe shipwreck of human Leand. life.". That includes a marginal "Leand.", not only line 548.

Every quoted segment is word for word. Only the description of the gaps is off.

### CR2-5. LOW (cosmetic). Two small description slips.

- **Doc_02 §8 (line 110):** "the bulk of the fourth beyond its own dedicatory epistle". The epistle is in the first volume (`bliss1844`), not the fourth.
- **Registry row 19, Source column:** "*Liber Pontificalis*, vol. I, the lives from Hormisdas (514) to Pelagius II (590)". This reads as if the volume holds only those lives. It runs from St Peter (chronological list from line ~395), and 514–590 is the corpus-map row's scope. The row should say which.

## Changed claims verified

| Claim | File and locus | Result |
|---|---|---|
| Register endnote hedges the Leander letter's date | `npnf212` `iii.v.i.xxx-p7`, line 32579 | Word for word |
| Reccared paragraph and the endnote it carries | `iii.v.i.xxx-p6`, line 32576 | Word for word |
| Ep. XXXVI and Ep. LI headings and the *servus* lines | lines 32348–32354, 44425–44463 | Correct |
| Lombard invasion, Agilulf, truces; no "tribute" | lines 22170–22206, 22228–22233, 23156–23200 | Correct |
| Moralia quotation, five segments, scan letters kept | `bliss1844` 389–390, 469–470, 548, 549–552, 552–555 | Word for word (see CR2-4) |
| Dialogues headings as noise; opening line | `gardner1911` 3379, 3393–3396, 3407–3410 | Correct; word for word |
| Gregory of Tours Book X, two phrases and the Ostia passage | Dalton 20164, 20169, 20326–20327 | Word for word (see CR2-3) |
| Book X loci in Dalton, MGH, Brehaut | Dalton 20149, 20152–20169, 20275, 29701; MGH 31904–31918; Brehaut 10274–10344 | Correct |
| Paul the Deacon vendored, tr. Foulke 1907; mapped as `context` to other worlds | file header; `early-benedictine-italian-monasticism.yaml` row at line 168, `gothic-and-vandal-homoian-christianity.yaml` line 182 | Correct |
| Loomis ends with Pelagius II and has no life of Gregory | chronological list (LXV. Pelagius II, line 474); life at 12339; header "to the pontificate of Gregory I" | Correct |
| Ewald–Hartmann files: Books VIII–IX and X–XIV; `tradition`/`provisional`; Books I–VII not vendored in that edition | `REGISTRY.yaml` line 22526ff; corpus map; directory listing | Correct |
| Whitby *Life*, John the Deacon's *Vita* not vendored | directory listing and text search | Correct |

## Figures recounted

| Figure | Document | Recount | Result |
|---|---|---|---|
| Register with endnotes | ~261,000 | 261,237 (method A); 258,531 (method B) | Correct |
| Register without endnotes | ~227,000 | 227,011 (A); 224,940 (B) | Correct |
| `npnf212` part | ~158,900 / ~135,600 | 158,871 / 135,584 (A) | Correct |
| `npnf213` part | ~102,400 / ~91,400 | 102,366 / 91,427 (A) | Correct |
| Moralia | 1,022,290 | 279,439 + 259,865 + 167,947 + 315,039 | Correct |
| Ratios | 3.9 / 4.5 | 3.91 / 4.50 | Correct |
| Holdings | 1,522 / 2 / 14 / 150 / 1,356 | same | Correct |

## Observations (not findings)

- `Superseded_Claims.md` 3.18 gives the Register ranges as lines 30953–48478 and 826–10409. The divisions close at 48476 and 10408. This does not change the counts, and the file is outside this review's scope.
- `john-moschus_pratum-spirituale-sophronius-opera-grc-lat_migne-pg87-3.txt` (c. 600) and the John of Biclaro chronicle in `chronica-minora-2_...mommsen1894.txt` are further in-window, non-Gregorian files under "no coverage entry". Neither document claims they are absent, so this is not a finding. A future pass may want to assess them.
- `REGISTRY.yaml` lines 1496–1500, in the Turchi entry, still say the Ewald–Hartmann edition "remains unvendored". That is Library metadata, not either reviewed document.

## Methods

- **Quotations:** the XML paragraphs were extracted by `id` with `lxml`, with tags stripped, endnotes separated and whitespace collapsed, then compared word for word. The OCR text files were read directly at the cited lines.
- **Word counts, two independent methods:** (A) a line-range `sed` extract, with tags replaced by spaces (`<note>` elements removed by a separate `perl` pass for the no-endnote figure), then `wc -w`; (B) an `lxml` parse of the same divisions, counting the joined element text, with `<note>` elements removed and their tails kept for the no-endnote figure. Scope: `npnf212` div `iii.v` (lines 30953–48476) and `npnf213` divs `ii.v`–`ii.x` (lines 826–10408). The `npnf213` "Registrum Epistolarum (Notes)" division `ii.iv` (lines 658–825) is excluded, as the document's own scope excludes it. Moralia: `wc -w` over the four whole files.
- **Holdings:** `python -m engine.m9.cli holdings rcg` was re-run on `16dbad2e`, and its full output was compared with §8.
- **"Not vendored" claims:** every such phrase in both documents was found by text search, then checked against a directory listing of `cic/texts/` and `REGISTRY.yaml`, and against the holdings output for in-window files with no coverage entry.
- **Truncation of the two reviewed files:** two independent methods (structural completeness, and byte count against the `origin/main` blob size with an intact final line). See the header.
- **Neither reviewed document was edited by this review, and no revision was drafted.**
