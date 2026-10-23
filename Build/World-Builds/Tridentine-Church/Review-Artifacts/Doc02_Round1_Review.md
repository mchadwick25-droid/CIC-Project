Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: Opus Round 1 reviewer, Tridentine
Drafter agent: addc920a5d1ee7b8a (Sonnet)
Round: 1
Truncation check, method 1: wc -l -c on the three files: Doc_02 414 lines and 68,246 bytes, its last heading "## 11. Disposition" (line 410) followed by "*End Doc_02.*"; Source_Registry 208 lines and 124,642 bytes, last heading "## Saturation statement" (line 202); Open_Gaps_Tracking 194 lines and 18,159 bytes, last heading "## OG-19" (line 187). Every file ends in a complete sentence and a newline.
Truncation check, method 2: independent parse in Python of the Registry table: 114 data rows numbered 1 to 114 with no gap, each with the full column set, and 59 rows in the file table (lines 140 to 198); tail -c of each file through od -c shows the closing text ("*End Doc_02.*", "(rows 91, 92, 93, 94).", "trace of the relation.") and a final newline; Open_Gaps entries run OG-1 to OG-19 in order.

# Review of Doc_02_Source_Ecology.md and Source_Registry.md (The Tridentine Church)

Also reviewed: `Open_Gaps_Tracking.md` in the same folder. Context read: Step 0 and Doc_01 (both Approved to proceed), the Tridentine and Borromean Milan dossiers, `cic/corpus-map/the-tridentine-church.yaml`, the census entry, `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, the Step 0 files of `witt` and `rzg`, and the `jes` Doc_02 exemplar.

## Verdict

**Substantial revision required.** Nine blocking findings and twelve cosmetic ones.

The draft is strong in most of what Step 2 asks. The corpus figures, the search counts, the Registry counts and almost every quotation check out. The forces lens is real work, not lip service: §6 names which sources speak to external and internal forces, what the silences show, and how survivorship shapes the shelf, and §2 carries Transmission History for every voice. The thin-evidence map, the holdings column, edition and language per work, the quotability and voice flags, and the cross-world file table are all present. The writing meets the bar: average sentence length in the prose is about 14 words, there are no em-dashes outside quoted text, and there are no AI tells.

The blocking findings are specific and fixable. The most important are finding 1 (the Registry decides the Borromeo voice question it says it leaves to the project lead) and finding 2 (the Catechism on the shelf is a 1934 revised edition, not the 1923 text, which bears on rights).

## What was verified

- **Quotations.** 122 quotations checked verbatim at their cited loci, across 27 vendored files: Waterworth (30), the Bullarium (11), Pius V's letters (6), the Collectanea (7), the Catechism (7), Sarpi (8), Pallavicino (8), the Acta (5), Bacci (4), Bellarmine (6), Giussano (4), Theiner (4), Schaff (5), and Barlow, the Missal, the Breviary, Gibbings, Granada, Jewel, Marnix, Teresa, the Lainez volume, the 1734 Profession and Reusch. Normalisation was limited to whitespace, line-break hyphens, words split across a line without a hyphen, and long s. Every quotation matched at its locus under that rule. Two used single marks for the scan's inner double marks (cosmetic finding 3). One quotation sits at its line but under the wrong division (finding 4). One date is quoted from the right line but belongs to the previous letter (finding 3).
- **Corpus figures (two methods, C.UTF-8 locale).** 64 rows over 59 files; 21 `tradition` and 43 `context`; 32 `assigned` and 32 `provisional`. 75,948,214 characters and 11,527,898 words, by Python (raw bytes decoded) and by `wc -m -w` on the piped files. The C-locale figures (77,073,634 bytes, 11,415,735 words) also match. The role split, the language split (it sums to the total) and the second-witness share (10 files, 8,306,934 characters) all match.
- **Search counts.** 835 `.txt` and `.xml` files among 842 entries; 223 match the stated regular expression; 43 of the 59 bucket files match, and the 16 that do not are the ones named in §9.
- **Sweep.** Two archive.org queries were re-run: query 2 ("acta genuina", 2 hits, `bub_gb_LeoCAAAAQAAJ` among them) and query 11 ("Breviarium Romanum", 1568 to 1650, 2 hits, `breviarium-romanum-1568` among them). Both match.
- **Registry counts.** 114 rows; Native 94, Excluded 20 (Named Comparandum 12, Out-of-Boundary 8); Confidence A 36, B 39, C 35, D 4. These match the header.
- **Dossier coverage.** Every dossier §3 lead has a matching Registry row, and every §5 question is carried in OG-19.

## Answers to the three directed checks

**(a) A recorded ruling on the Borromean Milan placement (OG-4).** I found none, so the drafter's account is accurate. In detail:

- `LIBRARY-DECISION-LOG.md` (633 lines) names the question once. That is in the entry "Era VII library pass: scope, corpus size, and placements left to Mark" (lines 113 to 114), which says the question is open.
- The later entry of the same date, "Era VII rulings after the two library passes (Mark, six decisions)", does not rule on it. Its item 1 sends "All 20 build-recommended worlds" into Steps 0 to 2, and the Borromean Milan dossier §6 (line 125) recommends building VI.12 as its own world. But the entry does not list the twenty by name. Its item 6 rules the seven `needs-ruling` rows, and Borromeo is not one of them.
- The entry "A voice may belong to several worlds of the same era; Tatian is co-owned" (29 September 2026) quotes Mark: "it doesn't have to be just one." The Library reads that narrowly, as a ruling on Tatian and on "figures that share Tatian's shape". It is the nearest standing rule, and Doc_02 and OG-4 cite neither entry.
- The Tridentine dossier §5 gives a reading and ends "A ruling for Mark." (line 123). The Borromean Milan dossier §5 passes the question on undecided (line 106).
- `NEEDS-RULING.md` has no Borromeo row.
- Under `Build/Ministry/`, Borromeo and VI.12 appear only in atlas design files and in the Atlas Decision-Log (line 3478, the removal of the V.10 to VI.12 identity link). The System Hub Decision Log has nothing. No record of the voice placement exists.

**(b) All eleven items of Doc_01 §7 addressed.** Yes, in name: Doc_02 §7 items 1 to 11 take Doc_01 §7 items 1 to 11 in order, and OG-1 records that. Three are not discharged as stated:

- Item 5 goes beyond what Doc_01 directs and decides the ownership question (finding 1).
- Item 6 misdescribes the Reformed cities' Step 0 (finding 7).
- Item 4 cites the `jes` passage on Sarpi rather than the one on the Waterworth split (cosmetic finding 9).

**(c) ISO dates in prose.** Build/World-Builds is not a surface that `tools/check_live_commentary.py` scans today. I copied the three files to a scratch tree as `Build/worlds/<code>/` and ran the checker's own `scan_file` on the copies. Doc_02 gives 18 REWRITE (iso-date) lines and the Registry gives 2 (one ROUTE, one REWRITE). Open_Gaps is protected (26 PROTECTED). See cosmetic finding 1. These lines will fail the live-surface rule when the world gets a code and moves.

## Findings

### Blocking

**1. BLOCKING: the Registry decides the Borromeo voice question that Doc_02 says it leaves to the project lead.** Files: Source_Registry rows 29 to 33; Doc_02 §1 (table row "The bishop of Milan"; the Borromeo bullets), §7 items 5 and 15, §11; OG-4 and OG-5. Locus checked: the corpus-map rows for the five Italian files (`context`, `provisional`), the Lives (`context`, `assigned`), and the two dossiers' §5.

- Rows 29 to 33 are "Excluded, Named Comparandum". Row 29's Comparandum Note states: "Borromeo's pastoral voice is the Borromean Milan world's (VI.12)." That answers "which world owns Borromeo's voice (VI.12 or VI.22)", the question the decision log leaves to Mark.
- Doc_02 §7 item 5 says "This document applies those placements" and "attributes no ruling to the project lead". It does not apply them. The map has the Italian files as `context` here, and the Registry excludes them. The map has the Lives as `context`, and the Registry holds them Native.
- §1's table says Borromeo's Italian "is held as context only". §7 item 15 and OG-5 then list the same files as placements Doc_02 does not follow.
- The draft does not mention the co-ownership ruling of 29 September 2026, which leans the other way.

Fix:

- Hold rows 29 to 33 at a status that does not assign ownership. For example: Native, held as context, not licensed for this world's Representative pending the project lead's ruling.
- Remove the ownership sentence from rows 29 to 33.
- Make §1, §7 item 5 and §7 item 15 say the same thing.
- Cite in OG-4 both the "six decisions" entry and the co-ownership entry as the nearest records, so Mark rules with them in view.

**2. BLOCKING: the vendored Catechism is the 1934 revised edition, not the 1923 text, and its rights basis is untested.** Files: Source_Registry rows 10 and 11 and the file table; Doc_02 §1 (table row "The commissioned catechism", the edition bullet), §2 "The Roman Catechism" (Limitations, Transmission History), §7 item 11. Locus checked: `council-of-trent_roman-catechism_mchugh-callan1923.txt`.

- The title page reads "SECOND REVISED EDITION" (line 72) and "SIXTH PRINTING, SEPTEMBER, 1937" (line 73). The imprint reads "Copyricut, 1934, by Josrpu F. Wacner, Inc., New York" (line 110).
- The imprimatur of 3 January 1923 (line 107) is carried over from the first edition.
- The file header's rights basis says "Published 1923; public domain in the US by date". That does not describe this printing. A 1934 copyright is public domain in the US only if it was not renewed.
- The draft calls the English "of 1923" throughout and reports the header's rights line without the conflict.

Fix:

- State the edition as the second revised edition (copyright 1934, sixth printing 1937).
- Open an Open_Gaps entry asking the Library for a renewal check, and mark rows 10 and 11 "used, pending the rights check" until it is done.
- Record that Doc_01 §1 and §2 say 1923, as a change-order candidate (see finding 9).
- Whether the revision changed the text at the passages quoted cannot be told from the shelf. Say so.

**3. BLOCKING: the letter to the Archbishop of Goa is given the previous letter's date.** File: Source_Registry row 16. Locus checked: `pius-v_apostolicarum-epistolarum-lat_1640.txt`, lines 1860 to 2000.

- Row 16 says Letter XVIII "is dated 'die 111. Octobris, M. D. LXVIII.' (line 1869)". That dating line closes Letter XVII. The heading "EPISTOLA XVIII" follows it (line 1873).
- Letter XVIII's own closing reads "die / vit. Octobris, M. p. 1xv11. Pontificatus noftri / anno fecundo" (lines 1999 to 2001). The year is garbled. The second year of the pontificate points to 1567.

Fix: correct row 16's date and locus, and state the year as garbled.

**4. BLOCKING: Giussano's book of the virtues is Book VIII, and the cited line is the contents list.** Files: Source_Registry row 35; Doc_02 §4 (first bullet). Locus checked: `giussano_life-of-st-charles-borromeo-v2_1884.txt`, lines 275, 338 to 341 and 10888.

- Row 35 says "Book VII opens with the chapter 'OF THE VIRTUE OF FAITH IN ST. CHARLES.' (line 341)", and names "Giussano's thematic Books VII to IX". Doc_02 §4 says "Giussano's Book VII is a thematic treatment of Borromeo's virtues."
- Line 341 is a contents entry under "BOOK YIIL" (Book VIII, line 338). The chapter heading in the body is at line 10888.
- Book VII (contents, line 275) opens with "LAST JOURNEY TO ROME, OCTOBER 1582", which is narrative.

Fix: correct the book number, the division and the line in row 35 and in §4. The quotation at lines 10934 to 10936 then sits in Book VIII, Chapter I.

**5. BLOCKING: the decrees' own text does not say the Cardinal of Lorraine composed the acclamations.** Files: Doc_02 §3 item 4 (closing paragraph) and the §8 table row "The Cardinal of Lorraine composed and led the acclamations." Locus checked: Waterworth lines 24031 to 24105, 11145 to 11147; Sarpi lines 70194 to 70196.

- The acclamations name the speaker as "The Cardinal of Lorraine." and then "The Cardinal.". That documents that he led them.
- That he composed them is in Waterworth's essay ("who also had composed them") and in Sarpi ("not only to compose the acclamations").

Fix: say that the decrees document his leading, and that the editor and Sarpi, from opposite sides, document the composing. The Documented tag can stand on that basis.

**6. BLOCKING: three confidence tags do not follow Article 17 on the evidence the draft gives.** Files: Doc_02 §3 items 1 and 5, and the §8 table.

- (a) §3 item 1 says the independence of the pre-1517 reform current "stays Contested", and §8 tags it "Contested; Inferential/Thin". Doc_01 never tagged it Contested. Doc_01 §2 and Cell 1B give Widely Accepted for the existence of the current and Inferential-Thin for its characterization. The shelf has no source that states the scholarly disagreement. Either add the contest as a flagged builder-knowledge claim with a Registry row, or keep Doc_01's Inferential-Thin. In either case drop "stays" and the double tag.
- (b) The census's attribution of the tears to Massarelli is tagged Inferential-Thin (§3 item 5; §8 row "The Fathers wept at the close"). Nothing on the shelf supports the attribution. That is an absent claim, to be stated as not supported on this shelf, not a confidence level.
- (c) The §8 row "Trent approved Carranza's Catechism" is tagged Inferential/Thin. But Sarpi states it directly: the Deputies for the Index found "nothing worthy of cenfure" and "the Con tion did approve it" (lines 65034 to 65038, partly garbled). On the draft's own practice elsewhere ("Documented as Pallavicino's and Sarpi's statement"), this is Documented as Sarpi's statement, from one hostile witness. Sarpi also places the approval with the Index deputies and their Congregation, not with a session of the Council. The claim's wording should follow that.

**7. BLOCKING: the Reformed cities' Step 0 is misdescribed.** Files: Doc_02 §3 item 12 and §7 item 6. Locus checked: `Build/worlds/rzg/Step0_Movement_Scope_Confirmation.md` §3 B3.

- Doc_02 says that Step 0 names the Tridentine Church "once, in its list of worlds with no figure overlap".
- It names it twice. The second time it says that "the Tridentine Church's own decrees, once vendored, will almost certainly need to be read directly against this candidate's own confessional documents, the same 'direct doctrinal rival' relationship Lutheran Wittenberg's own Step 0 names for its own relationship to Trent."
- The Wittenberg quotation is correct (`witt` Step 0 §2 A3).

Fix: correct the description, so that §7 item 6 discharges Doc_01 §7 item 6 as stated.

**8. BLOCKING: quotability flags disagree for Schaff and Reusch.** Files: Doc_02 §1 (scan-quality bullet); Source_Registry rows 6, 7 and 20 and the file table (rows "6, 7" and "19, 20").

- Doc_02 says "The English of Schaff, Reusch's German and the two Pallavicino texts that are clean stay quotable."
- The file table flags both whole files "second witness only". Row 20 (Reusch's German) says "second witness only (noisy OCR)". Row 6 says Schaff's English "is a cross-check, not the primary wording". Row 7 is Confidence A and "verbatim-ready (English)".
- The Article 4 check in §8 relies on rows 7 and 8.

Fix: pick one answer per file part and make the file table, the rows and §1 say it. A file-level flag split by language or part is fine if the table says so.

**9. BLOCKING: Doc_01 statements now overtaken are not named as such.** Files: Doc_02 §1, §6 item 4 and §7 item 16; OG-3. Locus checked: Doc_01 §2 (the 1600 to 1650 paragraph) and §5 (Cell 3B).

- Doc_01 says *Regnans* survives "chiefly through" Barlow and tags "its 1681 transmission" Documented. Doc_02 corrects the dossier on this, but not Doc_01.
- Doc_01 says 1600 to 1650 is evidenced "by devotional material only", and that Propaganda Fide, the Index and the Inquisition have no vendored source. Doc_02 reports the Collectanea, Reusch and the 1564 sentence without saying that these overtake Doc_01's words.
- The rule is that Doc_02 does not reopen Doc_01 silently.

Fix: add these three points, and the Catechism date of finding 2, to §7 item 16 and OG-3 as candidates for a change order. Doc_01 itself is not edited.

### Cosmetic

**1. COSMETIC: ISO dates in prose.** Doc_02 lines 18, 55 to 59, 70, 78, 208, 280, 287, 291, 293, 301, 303, 305, 372 and 396, and Registry lines 67 and 204, are flagged by the live-surface checker (method under directed check (c)). Most are "Open_Gaps: <subject>, 2026-10-23" cross-references and "the Library decision log of 2026-10-23". Cite the decision-log entry by its title, and write prose dates in words (as the draft already does for "25 September 2026"). The Registry's Added and Discovery columns and the §9 "Date:" header line are exempt and can stay.

**2. COSMETIC: the day of *Regnans* is in a margin note.** Doc_02 §3 item 3; Registry row 13; the §8 table. In the Bullarium, a margin note near the bull reads "Dar. P. A. c." and then "die 25. Febr." (lines 85574 to 85575). The page interleaves columns, so which constitution it belongs to is not certain. Replace "The day is not legible" with that statement.

**3. COSMETIC: the single-mark convention is declared only in the Registry.** Doc_02 §3 item 9 (Dalton, lines 94 to 97) and Registry row 55 (Jewel, lines 2375 to 2377) print the scan's inner double marks as single marks. The Registry header states this convention. Doc_02's quotation note in its header does not. Add it there.

**4. COSMETIC: the Python counting method needs one more word.** Doc_02 §1. Reading the files in Python's text mode translates the CRLF line ends of the Jewel file and gives 75,944,176 characters, which is 4,038 fewer. The stated figure matches when the files are decoded from raw bytes. Say "decoded from raw bytes".

**5. COSMETIC: the vocabulary form of the tag.** Doc_02 writes "Inferential/Thin" five times (lines 266, 333, 336, 352, 354) and "Inferential-Thin" twice. The project's vocabulary and Doc_01 use "Inferential-Thin".

**6. COSMETIC: dates and claims from the builder's memory are not tagged.** Doc_02 §2 gives life dates in the headings (Borromeo 1538 to 1584, Bellarmine 1542 to 1621, Granada 1504 to 1588, Pole 1500 to 1558) and says "The Acta were later adopted widely", with no row and no tag. Registry row 50 says "reprinting the 1620 English", while Doc_02 §7 item 2 says "The file does not give the date of Brent's translation". Tag each one as builder knowledge, or source it, and make row 50 and §7 item 2 agree.

**7. COSMETIC: four Lives or five.** Doc_02 §2 (Borromeo, Visibility) and §6 (Overrepresented) say "four Lives". §1's table and §4 name five works (Giussano, Possevino, Valier, Bascapè, Peña). If Peña's canonisation summary is not counted as a Life, say so.

**8. COSMETIC: row 9's exclusion reason.** Registry row 9 (the 1734 Grounds) is "Named Comparandum", while its Holdings column says "out of scope: after the window" and OG-5 asks for `out-of-window`. Out-of-Boundary fits, as it does for row 45.

**9. COSMETIC: the cross-reference to the Society of Jesus.** Doc_02 §7 item 4. Doc_01 §7 item 4 asks for the Society of Jesus document that engages the same text. That is `jes` Doc_02 §7 item 3 (the Waterworth split). The draft cites §3 item 6 (Sarpi and the Breviary). Cite both.

**10. COSMETIC: the list of Early English Books files.** Doc_02 §7 item 9 and OG-14. Hall's 1703 and Foxton's 1722 Bellarmine files come from the same Gale microfilm series on archive.org (`bim_eighteenth-century_...`). Either list them with the other files or say why the re-check does not cover them.

**11. COSMETIC: process narration and a mixed signal in the disposition.** Doc_02 §11 says "Doc_01 carries the three non-blocking corrections of its Round 3 review", and OG-3 says "Doc_02 does not edit Doc_01 beyond the three non-blocking corrections of Round 3". Neither says who made them, and both narrate process. §11 also says "No escalation category is triggered" next to "a portfolio-level question". Reword so the Borromeo request reads as the routed cross-world item it is.

**12. COSMETIC: quotation addresses for the handoff.** Process V2.0 §4 (Library-stage rules, "Quotations") asks for a `cic:<file>:<locus>` address in the same paragraph as each quotation, for `handoff-08-quotes`. Doc_02 cites by line and Registry row. The approved `jes` exemplar does the same, so this is a note for the handoff and not a defect of this round.

**Observation, not a finding.** The census entry for VI.22 carries `living: False`. Doc_01 §1 records Living Tradition Status as PENDING. OG-15 could note the census value so that Mark sees both when he rules.

## Escalation-category check

- **Representative identity:** not touched.
- **Portfolio or cross-world:** yes, the ownership of Borromeo's voice between VI.12 and VI.22. Doc_02 routes it correctly to the project lead through OG-4. Finding 1 asks the Registry not to decide it in the meantime. No new escalation beyond OG-4.
- **Governance or methodology:** none. The Catechism rights question (finding 2) is a Library rights check, not a governance change.
- **Unresolved tension:** none. This is Round 1 and every finding has a direct fix.

Disposition: (left for the drafter)
