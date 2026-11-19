Simulated review — informational only, not an Article 31 substitute.
# Cap-ruling targeted review: `rcg` Doc_02 Source Ecology and Source_Registry

- **Reviewer model:** Opus 5.5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** cap-ruling reviewer (fresh Opus 5.5 subagent, session_01JMNsSDRcCWuRTZfKoJ41wk)
- **Drafter agent:** rcg library-stage build thread
- **Round:** 4 (the cap-ruling review; it does not count toward the three-round cap)
- **Truncation check, method 1:** structural read of both files: Doc_02 carries §1 to §11 in order and ends on a complete Document Log row; the Registry carries rows 1, 1a and 2 to 16 in sequence (17 rows) and ends on a complete closing paragraph
- **Truncation check, method 2:** byte comparison: each working file's byte count (Doc_02 36,491; Registry 11,757) equals its blob size on `origin/main` (`git ls-tree -l`), and each file's last bytes are a complete line ending in a newline
- **Documents reviewed:** `Build/worlds/rcg/Doc_02_Source_Ecology.md` and `Build/worlds/rcg/Source_Registry.md`, as on `origin/main` at `5136d7f58`
- **Date:** 2026-10-29

**Ruling under which this review runs.** The project lead ruled on 2026-10-29, relayed via the coordination thread (Hub log entry pending), that Doc_02 and the Source Registry get one more targeted Opus review that does not count toward the three-round cap. If it does not clear, the result goes back to the project lead with the specific open findings, and no further round is run on the build thread's own initiative. The same ruling confirmed the Tier 1 recommendation for census II.18 as written, so Step 0 and Doc_01 proceed. That part is recorded in `build/rcg_Build_State.yaml`, not here. The round counter excuses this file only when a "Cap ruling" entry in the System Hub Decision Log names `Doc02_CapRuling_Review.md`. That entry is not yet written.

**Scope.** This is a targeted recheck, not a fresh full review. It covers the Round 3 findings on these two documents, anything changed since Round 3 (including the library around them), every quotation and every claim about a vendored file against `cic/texts/`, and an independent recount of the figures.

## Verdict

**Verdict: SUBSTANTIAL REVISION REQUIRED (narrow). Not approved to proceed.**

Every Round 3 finding on these two documents is fixed, and every quotation checked is word for word against its file. Four findings are still substantial. One figure is wrong: the Register's word count, and the Moralia ratio built on it. One sourcing conclusion is now false: Gregory of Tours, Book X, is vendored. The holdings disposition has gone stale, leaving two in-scope Register files without a line. And two Registry verification notes contradict the Doc_02 text they license. Each fix is narrow and mechanical. Under the ruling, these go back to the project lead. They are not grounds for a further round on the build thread's own initiative.

## Prior open findings (Round 3), status and evidence

| Round 3 finding | Status | Evidence |
|---|---|---|
| 1. MEDIUM, Doc_02 §6: Theodelinda exact quote and editorial-inference flag not carried from §1 | **Fixed** | §6 (line 68) quotes "whom he esteemed so highly" and "cordially", and says the "distressing to him" comment is the editor's. File: `npnf212` lines 22462–22465, word for word. |
| 2. MEDIUM, Doc_02 §1: emperor's-order quote at the wrong locus | **Fixed** | §1 (line 22) cites `iii.v.ii.xxiv-p8`. The `p8` paragraph (file line 35322) carries the quote word for word, after its endnote. The letter heading is `div4 n="XLVI"`, "To John, Bishop." (line 35289), and it sits inside Book II (heading at line 33953, Book III at 36116). |
| 3. MEDIUM, Registry: no row covered the Ep. II.46 quote | **Fixed** | Row 1 now names Book II Ep. XLVI and locus `iii.v.ii.xxiv-p8`. |
| 4. LOW-MEDIUM, Doc_02 §9: "two Confidence A primary quotations" for Istria overstated | **Fixed** | §1 (line 22) and §9 item 2 (line 110) now give one Confidence A quote (Ep. II.46). The "in vain" passage is apparatus text at Confidence B. |
| 9. LOW, Registry row 8: Equitius range not extended | **Fixed** | Row 8 now gives ~2054–2069 and ~2109–2204. Julianus and the summons narrative fall at file lines 2125–2204. |
| Round 2 D2-15 (V1.8 Step 2 outputs: quotability flags, edition/language pairing, `PAIRS.yaml`) | **Open, disclosed** | Doc_02 §9 item 7 names it as not done, and Round 3 did not carry it as a defect. It is still open, but it is disclosed and not misstated. It is not a finding of this review. The handoff gate may still require it. |
| Round 2 D2-7 (cross-world questions not logged) | **Closed** | `Open_Gaps_Tracking.md` entry 4 (Turchi, 2026-10-02) and entries 6–7 (early-Benedictine adjacency) carry them. |

## New findings

### CR-1. MEDIUM (substantial). The Register's word count is wrong, and the Moralia ratio built on it is wrong too.

**Location:** Doc_02 §1, line 17 ("Roughly 160,000 words") and line 28 ("roughly six times the length of the Register by direct word count (1,022,290 words ... against the Register's own ~160,000)").

Doc_02 defines the Register as Books I–XIV across both `npnf212` and `npnf213`. The ~160,000 figure counts only the `npnf212` part (Books I–VIII). Recount by two independent methods:

- **XML structure:** take the text of the Register divisions with tags stripped. `npnf212` div `iii.v` (lines 30953–48476) has 158,898 words with endnotes and 135,587 without. `npnf213` Books IX–XIV, divs `ii.v`–`ii.x` (lines 826–10408), have 102,401 with endnotes and 91,434 without.
- **Line ranges:** apply a plain tag-strip to the same line ranges and count with `wc -w`. This gives 158,871 and 102,366.

The full Register selection is therefore about 261,000 words with endnotes, or about 227,000 without. The Moralia's 1,022,290 words is confirmed exactly by `wc -w` over the four files. So the Moralia is about 3.9 times the Register (4.5 times against the count without endnotes), not "roughly six times".

**Disagreement with prior reviews, logged rather than resolved by recency:** Round 2 (finding 9) took the 160,000 figure at face value, called the earlier "four times" wrong, and gave about 6.4 times. Round 3 confirmed the ratio as "consistent at ~six times". `Superseded_Claims.md` 1.2 records "roughly four times" as withdrawn. The withdrawn claim was in fact the closer one. The same figure and ratio also stand in `Step0_Movement_Scope_Confirmation.md` (lines 79 and 81). Step 0 is outside this review's scope, but the cross-document consistency rule means the same correction must reach it. Step 0's status is the project lead's to direct.

**Needed:** a corrected figure stating whether endnotes are counted, a corrected ratio, the same figures carried into Step 0, and a correction to `Superseded_Claims.md` 1.2.

### CR-2. MEDIUM (substantial). Gregory of Tours, *History of the Franks* Book X, is vendored. Both documents say it is not.

**Location:** Doc_02 §4 (line 55, "**Not currently vendored in this corpus.**"), §9 item 5 (line 113); Registry row 12 (Confidence "— (not vendored ...)") and the "Named acquisition gaps" section (line 33, "Not currently vendored").

`cic/texts/gregory-tours_history-of-the-franks-v2_dalton1927.txt` is in `cic/texts/REGISTRY.yaml` (date_added 2026-09-25). Its "HERE BEGINS THE TENTH BOOK" (line 20149) narrates three things:

- the deacon returning from Rome, the Tiber flood, the plague that "first of all attacked Pope Pelagius", and the election, "the whole people chose the deacon Gregory" (lines 20152–20169, with the note "A.D. 590" at line 20188);
- the "sevenfold litanies" (line 20275);
- Dalton's notes on the sevenfold procession (lines 29672–29703).

Two more witnesses were vendored on 2026-10-23: `gregory-tours_history-of-the-franks-selections_brehaut1916.txt` and the Latin `gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt`. The documents' own "single most significant non-Gregorian acquisition lead" is therefore in the library. Row 12 cannot keep an unset Confidence on the ground that the text is not vendored.

**Needed:** set row 12's Confidence against the file, and restate §4, §9 item 5 and the acquisition-gaps section. Whether Book X.1 then supports a claim is the build thread's call. This review does not license any claim from it.

### CR-3. MEDIUM (substantial). The holdings disposition is stale. Two in-scope Register files have no disposition line and no Registry row.

**Location:** Doc_02 §8 (lines 83–105) and §1 (line 15); Registry (no rows).

`python -m engine.m9.cli holdings rcg` was re-run on 2026-10-29 against `origin/main`. It now reports:

- 1,522 vendored files;
- 2 "by design", 14 "in scope, unread", 150 "out of window" and 1,356 "no coverage entry".

§8 still reports 220, 2, 12, 86 and 120. The two new in-scope files have no §8 line:

- `gregory-great_registrum-epistolarum-t2-pars1-libri-8-9-lat_ewald-hartmann1893.txt`;
- `gregory-great_registrum-epistolarum-t2-pars2-libri-10-14-lat_ewald-hartmann1895.txt`.

`cic/corpus-map/roman-church-gregorian.yaml` now assigns both to this world at `role: tradition, confidence: provisional`. It also carries a `context` row for `liber-pontificalis_book-of-the-popes-v1_loomis1916.txt`, the lives from 514 to 590. None of these three has a Registry row. The template's rule, and handoff check 4, is that no corpus-map entry or holdings-report file lacks a line. Row 15 (the *Liber Pontificalis* entry on Gregory himself, "Not vendored") stays accurate, because the vendored volume ends with Pelagius II. But that volume covers 560–590 of this world's window and needs its own row.

The Ewald–Hartmann files also bear on §2's numbering note and on Open Gaps entry 4 (Turchi). The Latin critical edition whose numbering Turchi follows is now partly in the holdings (Books VIII–XIV).

A further, LOW part of this finding: §8's account of the tool failing because no `records/rcg/` exists is no longer true. `records/rcg/.gitkeep` is on `main`, and the tool runs as it stands.

**Needed:** re-run the tool and give every in-scope file a line. Add Registry rows for the two Ewald–Hartmann files and the Loomis volume.

### CR-4. LOW-MEDIUM (substantial). Two Registry verification notes contradict Doc_02 §1.

**Location:** Registry row 4 (Verification Note) and row 8 (Verification Note).

- **Row 4** says the Moralia epistle was "Verified word for word, lines ~384–548, with ... clear OCR character errors corrected". Doc_02 §1 (lines 28–30) says the quotations keep the scan's letters, with "1" for "I", and they do. The quoted text runs to line 555 of `bliss1844`, not 548.
- **Row 8** says "Book II heading and opening line verified word for word ... (~line 3396)". Doc_02 §1 (line 34) says the headings are scan noise and are described, not quoted, which matches the file (lines 3379 and 3393–3396 are garbled). The opening line it quotes is at line 3407–3410.

A verification note is a claim about how a quotation was checked, and these two now say something false about the text they license.

**Needed:** bring both notes into line with Doc_02 §1.

### CR-5. LOW (cosmetic). The Moralia ellipsis drops three words, while the disclosure says nothing is omitted.

**Location:** Doc_02 §1, lines 28 and 30.

The quote moves from "...so under the cloak of the Ecclesiastical office" straight to "...plunged on a sudden". The scan reads "Ecclesiastical office, I found myself*^ plunged on a sudden" (`bliss1844` line 552). The scan does not break between "office," and "I found myself": the footnote marker follows "myself". Each quoted segment is word for word, and the ellipsis marks the gap. But line 30's "nothing is added, omitted or altered", and the claim that the quotations "break where the scan breaks", overstate it. Include "I found myself" or correct the sentence.

### CR-6. LOW. The cited locus for the "truces, tribute" claim does not carry it.

**Location:** Doc_02 §1, line 24; Registry row 1a (the "~lines 22132–22206" range).

Lines 22132–22206 cover the Lombard invasion, Agilulph and Theodelinda, and Italy's misery "among the swords of the Lombards". They do not mention truces. Truces appear at line 22231 ("effecting truces with the enemy") and at lines 23156–23200 (the settled truce of 598–9 and the second truce of 603). "Tribute" was not found in the apparatus by search. The claim is at Confidence B and is already flagged as untraced. It still needs the right range, and either a located source for "tribute" or the word removed.

### CR-7. LOW (cosmetic). Smaller citation and cross-reference slips.

- **Registry row 1, Source column:** it names Books I, II and V. But the row licenses `iii.v.i.xxvi-p3` (Ep. I.36) and `iii.v.vi.xxxii-p4`, which is Book VI, Ep. LI ("To the Brethren going to England", line 44425).
- **Registry row 4:** "complete in 4 parts (Parts I–V ...)". The work is in six Parts across four volumes. `bliss1847`'s title page reads "THE FIFTH PART ... THE SIXTH PART".
- **Doc_02 §11 (line 125):** it points to `Review-Artifacts/RoundN_Library_Stage_Review.md`. The files are `Doc02_RoundN_Review.md`.
- **Doc_02 §1 (line 20):** it gives the Leander letter as "dated 591". The endnote reads "The date of the letter before us, if rightly placed, is a.d. 591" (`iii.v.i.xxx-p6`). The hedge belongs with the date.

## Quotations and source claims verified

Every quotation and locus claim in Doc_02 §1–§6 and the Registry's Verification Notes was read against the file. Paragraph text was taken from the XML with tags and endnotes separated. The OCR files were read at the cited lines.

| Claim | File and locus | Result |
|---|---|---|
| "Lo, he received the keys ... O tempora, O mores!" | `npnf212` `iii.v.v.x-p7` (Book V, Ep. XX, "To Mauricius Augustus", line 41075) | Word for word |
| "Lo, all things in the regions of Europe ... profane titles" (two ellipses) | `iii.v.v.x-p8` | Each segment word for word |
| Storm-metaphor segments; "our common son, the most glorious King Rechared"; "been converted with most entire devotion to the Catholic faith" | `iii.v.i.xxx-p5`, `-p6`; Ep. XLIII in Book I (lines 32528, 30955, 33953) | Word for word; "next paragraph" correct |
| *servus servorum Dei* at `iii.v.i.i-p7`, `iii.v.i.xxvi-p3`, `iii.v.vi.xxxii-p4`; endnote: Damasus, Augustine, "four times only" (I.1, I.36, VI.51, XIII.1), Bede | `npnf212` | Correct (see CR-7 on row 1's Book list) |
| Endnote `iii.v.i.xxx-p3`: Moralia's oral Constantinople origins, *Epistola Missoria*, Leander letters V.49 and IX.121 | `npnf212` | Correct |
| "ineffectual attempts, though apparently supported by the Emperor" ... Ep. 16; "invoking of the secular arm ..." Ep. 74 | lines 23069–23074 | Word for word (the file carries soft hyphens) |
| "He in vain endeavoured ... to conformity"; Vigilius and successors "including Gregory"; Theodelinda phrases; no Pelagius I, no date | lines 22453–22466 | Word for word; the attribution claims are correct |
| "I have learnt the truth ... from compelling them." | `iii.v.ii.xxiv-p8` | Word for word |
| Line 22132 is the Prefatory Note; John the Deacon and the 14 books at ~22971 | lines 22128–22144, 22966–22978 | Correct |
| Bertha, Ep. 29, apparatus discussion | lines 23662–23683 | Correct |
| "No one presumes to teach an art ... the art of arts!" | `iii.iv.ii.ii-p3` | Word for word |
| Five Moralia epistle segments; "iVom ihe"; "1" for "I"; footnote interleave; "further burden of the Pastoral charge was fastened on me" | `bliss1844` lines 389–390, 469–470, 548–555, 563–564 | Each segment word for word (see CR-5) |
| "a man of venerable life, blesse#by grace ... inferior to his virtue"; Book I end and Book II heading | `gardner1911` lines 3407–3410; 3379, 3393–3396 | Word for word (see CR-4 on row 8) |
| Turchi follows Ewald–Hartmann numbering; NPNF follows the Benedictine edition | `turchi1907` lines 37–67; `npnf212` lines 22122, 22975 | Correct |
| The four works assigned `role: tradition, confidence: assigned` | `cic/corpus-map/roman-church-gregorian.yaml` | Correct (see CR-3 on the new rows) |

## Figures recounted

| Figure | Document | Recount | Result |
|---|---|---|---|
| Moralia, four volumes | 1,022,290 | `wc -w`: 279,439 + 259,865 + 167,947 + 315,039 = 1,022,290 | Correct |
| Moralia Books I–X | ~279,000 | 279,439 | Correct |
| Pastoral Rule | ~70,000 | div `iii.iv`: 69,540 (68,545 without endnotes) | Correct |
| Register, Books I–XIV | ~160,000 | ~261,300 with endnotes, ~227,000 without (two methods, CR-1) | **Wrong** |
| Moralia to Register ratio | ~six times | ~3.9 (with endnotes) to ~4.5 (without) | **Wrong** |
| Holdings tool output | 220 / 2 / 12 / 86 / 120 | 1,522 / 2 / 14 / 150 / 1,356 | **Stale** (CR-3) |

## Observations (not findings)

- `bede_ecclesiastical-history-english-people_giles1903.txt` is vendored. Bede is out of window (c. 731), but he carries Gregory's own English-mission letters. The Register's endnote at `iii.v.i.i-p8` notes that the *servus servorum* formula appears in Bede's copies of those letters, though it is absent from the same letters in the Registrum. A future pass may want a row for it as a transmission witness.
- `chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt` contains John of Biclaro's chronicle, which runs to 590. This is a possible in-window, non-Gregorian witness for the Visigothic conversion. It is unassessed here.
- §1 reads Ep. II.46 as evidence of "continuing imperial partnership". The letter shows imperial authority overruling Gregory, who says he "shall not cease to write ... to the most serene lords". The same letter complains that the Exarch "evades fighting against our enemies and also forbids our making peace" (`iii.v.ii.xxiv-p5`). "Imperial engagement, not absence" is what the evidence directly shows. The document's framing is defensible and is not a finding.

## Methods

- **Quotations:** paragraph text was extracted from the XML by `id`, with tags stripped, endnotes separated and whitespace collapsed, then compared word for word. The OCR text files were read directly at the cited lines.
- **Word counts:** two independent methods for the Register (XML division structure, and plain line-range tag-strip with `wc -w`). `wc -w` alone was used for the plain-text Moralia files.
- **Holdings:** `python -m engine.m9.cli holdings rcg` was re-run on `origin/main` at `5136d7f58`.
- **Truncation of the two reviewed files:** two independent methods (structural completeness, and byte count against the `origin/main` blob size with an intact final line). See the header.
- **Neither reviewed document was edited by this review, and no revision was drafted.**
