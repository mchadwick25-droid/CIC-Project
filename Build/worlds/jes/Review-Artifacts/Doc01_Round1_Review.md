Simulated review — informational only, not an Article 31 substitute.

# Round 1 review of Doc_01, Doc_02, the Source Registry and the gap ledger (jes)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** Sonnet 5.5 drafting worker (commits 13a49c1ad and d040f3c77; commit trailers read "Claude Sonnet 5.5")
- **Round:** 1 (full review of all four files)
- **Truncation check, method 1:** structural count. Doc_01 has headings §1 to §10 in order, and Doc_02 has §1 to §11 in order; each ends with its Disposition sentence and a newline. The Registry has 74 table lines (header, separator, 72 rows), every one with exactly 12 pipes. Its rows are numbered 1 to 72 with no gap or duplicate, and the saturation statement ends on a complete sentence and a newline. The gap ledger runs OG-1 to OG-16, then items 17 to 28 in sections B to F, and ends on a complete sentence.
- **Truncation check, method 2:** byte and hash comparison against the committed blobs at HEAD d040f3c77. For all four files, `wc -c` equals `git cat-file -s`, and `git hash-object` equals `git rev-parse HEAD:<path>` (Doc_01 188933bad0…, 37,743 bytes; Doc_02 cfb35117e6…, 38,770; Registry 9cff2c18b0…, 67,076; ledger 52554827b9…, 25,217). No file has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/jes/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md` and `Open_Gaps_Tracking.md`, as committed at HEAD d040f3c77. Context: `Step0_Movement_Scope_Confirmation.md` (Approved to proceed) and `Build/Ministry/Operations/Audits/jes_Steps1-2_Draft_2026-09-30.md`.
- **Compared against:** the `hus` files and the four `hus` review artifacts (the failure patterns), and the `lpc` Registry's calibration rule.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** 0 P0, 4 P1, 14 P2.

The four files are well built. They follow the `hus` template section for section. Every one of about 135 quotations checked is in the vendored file at the line given, or starts there and runs onto the next line. The Article 4 check quotes the five commitments word for word and states each result at the right strength. The corpus figures are right in a UTF-8 locale. The Forces lens is present and does its job. The strand finding is stated as a recommendation, and Article 29, the Representative and the registration of `jes` are left open. No invented source was found, and no row rests on a work assigned only to another world.

The four P1 findings are:

- The drafter's change order about the Generals is right in direction, but its counts are low, and it misses the largest body of Roman letters in Salmeron's volumes: about 146 letters by Polanco written on the General's commission.
- The Chinese and Malabar Rites dates are carried in Doc_01 with no confidence level.
- Two claims cite rows that do not support them: a Portuguese "royal right", and the 1542 report "from Ireland".
- The CI live-commentary gate will fail on 52 lines in `jes` files. The drafter reported only the report-mode run.

## Scope 1: template, boundaries and hygiene

- **Template.** The `##` headings of Doc_01 and Doc_02 match the `hus` files one for one; only the wording of the Doc_01 §8 heading differs. Every Part I field of Doc_01 is present, and Doc_02 has all of §1–§9 of Part II and the STARLITE search record. The Registry uses the Template's ten fields plus the Discovery column, as `hus` and `lpc` do.
- **Boundaries.** The window of 1540–1650 is argued from the bull, with the day disagreement shown. The *Autobiography* is handled correctly as a text dictated inside the window about events before it (row 7 stops at 1538; the only later dates are 1550 and August 1555, at lines 909 and 483). The ending is stated honestly: no shelf event closes the world in 1650, and the shelf itself stops in February 1585.
- **No decision presented as settled.** Doc_01 §5 and §9, Doc_02's header, the Registry header and OG-7 all call strand-singular a recommendation. Article 29, the Representative and the registration of `jes` are open in Doc_01 §9 and in OG-8, OG-9 and OG-10. The Step 0 change orders are routed to the project lead and not applied.
- **Invented history.** None found. Two statements come from the builder's own knowledge without a row: the "royal right" (P1-3) and the beatification year 1872 (P2-13). Both are historically sound, but neither is on the shelf.

## Scope 2: Doc_01 §5, the strand finding

**Judgment: honest, and adequate as a recommendation, with four weaknesses (P2-1).** The finding is labelled as the builder's, it is tagged Inferential/Thin, it names what would reopen it, and it hands the choice to the project lead. The two-strand case is real: it gives the language barrier in Japan, the patriarch in Ethiopia, the Nuncio's brief, the difference in audience, and the rites. It is not at full strength, though:

1. The "Cost" bullet is an argument *against* two strands, placed inside the case *for* them.
2. The strongest datum for a mission strand is in the document's own §7 and is not used in §5: the census's de Nobili, who "took up the life of a Hindu ascetic in order to be heard", and Ricci writing for Confucian scholars ("The same rule may hide different lives").
3. The Ethiopian patriarch is used on both sides. §4 cites him as continuity, because he acts as Ignatius's deputy. §5 cites him as a difference in authority. The conclusion ("They do not show … a different authority") does not answer the authority bullet.
4. The honest basis is Article 21's own default, which §5 does not cite: "A world without established strands is treated as strand-singular throughout construction." The recommendation rests more safely on that rule, plus the absence of a mission voice after 1552, than on "the evidence supports one world".

## Scope 3: the Article 4 check (Doc_01 §8)

The five commitments were compared with `Build/reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` (its internal text reads "Version 2.3"), paragraphs 160–164. They match word for word. Straight quotation marks replace curly ones, and the inner double quotation marks of commitment 3 become single ones. The "need not have recited the Creed" sentence (paragraph 165) and "never a standard imposed on any selected world's own voice" (166) match. Article 21's definition, Article 22's two phrases and Article 29's "touches a tradition that continues into the present" (591) also match.

Every "shown" quotation was found at source. These include the Faber Proemium (lines 510–523), the April 1543 notes (9537–9541, 9585–9591, 9612–9615, all under the running head "ANNO 1543, MENSE APRILI"), the Coleridge catechetical notes (18405, 18607, 18749, 18969, 19105, 19261–19262, 19269, 19298), the *Exercises* (2245, 2335, 3948, 5162, 5221, 5468, 5499), Letter X (2484–2489) and Letter XX (4064–4068). The Canisius paraphrase is supported by lines 1455–1500 ("the onely Sonne of God … begotten before all worldes, natural, conſubſtantial") and 2135–2151 ("coeternall, coequal, & conſubſtantial … with equal honour & adoration").

The results are at the right strength. Commitment 4 is "largely shown" because "in glory" is not found. Commitments 1, 2, 3 and 5 are "shown in substance", and the clauses that rest only on Coleridge's rendering are named. The floor is not claimed for the mission's later voice or for 1585–1650. Two small misalignments are at P2-3 and P2-4.

## Scope 4: quotes and loci at source

A script normalised whitespace and line-break hyphens and read ſ as s, then checked each quotation against the cited line range. I read by eye every case where the range was short.

**Registry rows spot-checked (38): 1–28, 30, 32–36, 67–70.** Every quotation in these rows is in the file. In about a dozen rows the line number is the first line of a quotation that runs onto the next line (rows 5, 7, 13, 16, 18, 22, 23, 24, 28, 30, 69). That is acceptable. Checked content beyond the quotations:

- Row 14 (129–137): the preface names the Formula and three letters.
- Row 15 (39960–39967, 40029–40036): the companions' vow to the Pope; Xavier in Bobadilla's place.
- Row 16 (38785–38790, 38859): the last letter headed by Ignatius, 28 February 1548.
- Row 17 (255–266, 280–298): the preface's account of the diary; the title page reads M.D.CCC.LXXII.
- Row 19 (7442–7450): the circular letter on Faber's death.
- Row 21 (4812–4823, 7200–7213, 4520–4538): the Tivoli approval, the Alcázar note, and the ballots of 4–5 April.
- Row 23 (900–903, 13290–13296, 13571–13575).
- Row 25 (196–204, 402–413, 450–456).
- Row 26 (518–546).
- Row 27 (127–135, 219–227, 244–253, 270–276, 285–288, 340–347, 390–397).
- Row 28 (738–750, 884–900).
- Row 30 (139–256, 272–280).
- Row 32 (640–702, 1010–1060, 1088–1102).
- Row 33 (228–262, 350–358, 486–600).
- Row 34 (1455–1500, 2135–2151).
- Row 36 (58–78).

The exceptions are at P1-3, P2-6 and P2-11.

**Doc_01 and Doc_02 claims checked (over 40, by structure marker).**

- Doc_01 §1: the Pamplona quotation; the eight provinces and sixty-one places; Lainez, Borgia and Mercurian to 1580; the *Exercises* quotation; the Trent instruction.
- Doc_01 §2: the bull's two days; the Tivoli approval; the ballots; Xavier's sailing; Lainez's and Salmeron's roles at Trent; Faber's death; the 1548 approval; the landing on the Assumption; the death on Friday 2 December; Nadal's carrying of the Constitutions; Lainez's election, the choir and the term, Poissy and his death; Borgia's and Mercurian's dates; Nadal's death; Goa, Malacca, Amboina, "Amangucium", "Bungum", Brazil and the Congo in the editors' list; the Ethiopia consistory; the 1554 attack on the *Exercises*; the "domesticas dissensiones"; Nadal's "stimulos".
- Doc_01 §3: the tertianship in the Scholia preface (694–715); the Regesta from 1547.
- Doc_01 §4: Nugnez as Ignatius's deputy.
- Doc_01 §5 and §6: the Coleridge address and "how vast a field".
- Doc_01 §7: the *Imitation* and the Monte Cassino note; Rudolph and the "Flowers of the Saints".
- Doc_02 §1: every percentage; the table of voices.
- Doc_02 §2: the Mullan, O'Conor, Bouix, Boero, Lainez, Nadal and Salmeron transmission statements; the Protestatio; the Second General Congregation's decrees 42 and 57.
- Doc_02 §6: the survivorship statements.
- Doc_02 §8: every row that cites a preface date.

The exceptions are at P1-1, P1-3, P2-7, P2-8, P2-9 and P2-10.

## Scope 5: the Registry

- **Letters.** Every row carries exactly one letter: 37 A, 4 B, 30 C, 1 D. The calibration matches `lpc`'s rule. The A rows I checked were read at their Licensed-For loci. The four B rows (29, 31, 36, 37) are correctly B, because their Licensed-For content is structure only or unread. Every C row is not vendored. I confirmed that none of Alcázar, Sommervogel, Orlandini, Sacchini, O'Malley, Schurhammer, Thwaites, Ricci or Trigault, Pachtler, Institutum, Monumenta Xaveriana, Borgia, Astrain, Codretto, Menchaca, Poussines or Philippucci has a file in `cic/texts/`. The single D (row 44) is a genre.
- **Rights.** The rights basis of each vendored row matches its file header: `NOT_IN_COPYRIGHT` for rows 1, 19, 27, 30, 32, 33 and 35; the Public Domain Mark for row 23; PD by date for rows 5, 9, 14, 17, 25, 28, 29, 31, 34 and 36. Rows for works not vendored say that rights are unchecked, or that the work is in copyright.
- **Held and not held.** Every statement of what is and is not vendored is true against `cic/texts/` and the corpus map (19 files, 15 `tradition` and 4 `context`).
- **Other worlds' works.** No row is entered for a work assigned only to another world. Row 35 (Trent) is double-placed in the corpus map as `context` for `jes`. The Tridentine, Reformed, Hussite and Donatist files are in ledger section E only.
- **Boundary Status.** Native or Excluded only. Row 65 is Excluded as a Named Comparandum, with a Comparandum Note.

## Scope 6: confidence tags

The five-level vocabulary is used throughout. "Documented as the editors' statement" is a qualified Documented, as `hus` used it, and it is honest. Contested is used for the founding motive and the residence count, and it fits both. The Xavier attribution and the three-removes address are Inferential/Thin, which is right. Too strong or misapplied:

- the rites dates, which carry no level (P1-2);
- Xavier's day of death, which is tagged Inferential/Thin although it is an explicit single-witness statement (P2-3);
- the Doc_02 map's "Documented for commitment 4" (P2-3).

## Scope 7: corpus figures, counted two ways

In a UTF-8 locale the figures reproduce exactly. Python `len()` of each decoded file sums to 23,171,710, and `cat | LC_ALL=C.UTF-8 wc -m` gives 23,171,710. Python `split()` gives 3,397,128 words, and `LC_ALL=C.UTF-8 wc -w` gives 3,397,128. The role split (18,076,236 / 5,095,474), the language split (16,938,883 Latin), the second-witness total (3,731,985, 16.1 per cent), the quotable Latin (13,206,898, 57.0 per cent) and the Monumenta-plus-Bouix total (12,499,392, 53.9 per cent) are all right.

The session's default is the C locale, and there the same commands give 23,333,736, which is the byte count, and 3,370,893 words. Step 0's 3,370,675 is a C-locale `wc -w` count. The same count on the tree before commit c11c0801b, which rewrote the seven Latin headers, gives 3,370,743, within 68 words of it. So the two figures differ by counting method and by header edits, and the difference can be explained (P2-2).

## Scope 8: special check, the Generals in Salmeron's volumes

**Method 1** counts sender headings: a line of the form `P. <NAME>` in capitals, with the next non-blank line read for the addressee. **Method 2** counts every `PATRI ALPHONSO SALMERONI` line and classifies the sender line above it.

| Sender | Drafter | Method 1 (all / to Salmeron) | Method 2 (to Salmeron) | Dates on the shelf |
|---|---|---|---|---|
| Lainez, Tomus Primus | "about twenty", some before his generalate | 21 / 17 (plus one to Salmeron and Madrid) | 17 | 2 to Salmeron as vicar (19 March 1557, 13 February 1558); **15 as General**, 6 November 1558 to 6 January 1565; 4 to others, 1556–57 |
| Polanco "ex comm.", Tomus Primus | not counted | 189 / 146 | 144 | 1556–65, mostly 1557–61 and 1564 |
| Borgia, Tomus Secundus | about 45 | 49 / 49 | 46 | **7 as vicar general**, 18 February to 26 May 1565; **42 as General**, 18 November 1565 to 10 March 1571; none after March 1571 |
| Mercurian, Tomus Secundus | about 76 | 88 / 86 | 87 | 9 October 1573 to 27 May 1580 |
| Aquaviva, Tomus Secundus | about 17 | 18 / 18 | 19 | 20 May 1581 to 14 July 1584 |
| Polanco "ex comm.", Tomus Secundus | not counted | 14 / 13 | 12 | 1565–72 |

The drafter's direction is right, and the vendored editors support it in their own words. The Tomus Secundus Prooemium (lines 233–237) says that the 200 and more letters to Salmeron are "quarum pars maxima ex praepositorum generalium regestis deprompta est", mostly drawn from the Generals' registers. The Lainez Praefatio (lines 521–537) says that his letters as vicar and General come "ex Regestis, ut plurimum … Lainii nomine a secretario exaratae". Step 0 §4 item 5 and OG-1 ("Nothing vendored gives Lainez's own voice as General, nor Borgia's or Mercurian's") are therefore wrong as written.

The drafter's own statement needs three corrections (P1-1):

- Mercurian is about 86, not 76.
- Seven of the Borgia letters, including the sample in row 69, are from before his election, when he was vicar general.
- The largest Roman body is not counted at all: about 146 letters headed "P. Joannes de Polanco ex comm.", in Tomus Primus, 1556–65.

**How Step 0 §4 item 5 and OG-1 should be corrected.** The correction cuts against a reviewed Step 0 finding (Round 3, S1), so it is an escalation to the project lead, as the drafter has routed it. OG-1 is append-only and stays unedited. A new dated ledger entry supersedes its sentence, and Step 0 is amended only by a named change order. Proposed wording for both:

> Institutional material is dense to 1556 (Lainez Tomus Primus, Polanco Tomus Quintus; Ignatius's own vendored letters end in early 1548 in the Latin *Monumenta* volume, the last dated 28 February 1548, and in 1547 in the English selection), runs to 1562 through Nadal's letters, and after that rests on Salmeron's two volumes alone, to February 1585. Those volumes print the Roman centre's letters to Salmeron as register copies, in Italian and Spanish, mostly written by secretaries in the General's name: about 146 by Polanco on the General's commission (1556–65), about 15 by Lainez as General (1558–65), about 42 by Borgia as General (1565–71, with 7 more as vicar general in 1565), about 86 by Mercurian (1573–80) and about 18 by Aquaviva (1581–84). No volume of any General's own correspondence is vendored, and these letters are, with a handful of exceptions, addressed to one provincial.

**Ignatius to March 1548.** Confirmed. The last letter headed by Ignatius is "ROMA 28 FEBRUARII 1548" (line 38789). The one after it, dated "EXEUNTE FEBRUARIO AUT INEUNTE MARTIO 1548" (line 38859), is headed "PATER JOANNES DE POLANCO EX COMM." So "early 1548" (Doc_02) is exact. "To March 1548" (row 16, OG-4) is true of the volume, but not of Ignatius's own letters (P2-11).

## Scope 9: the Forces lens (Doc_02 §6)

Doc_02 §6 answers the three questions of Forces Framework V1.1 Step 2 (paragraph 193): which sources speak to external forces, what the silences show, and the survivorship patterns. It names the transmission dimension of Author Gravity for every author in §2. The survivorship paragraph refuses to read the archive's bias as a finding about the threat, which is the right discipline. The Polanco correspondence (P1-1) belongs in the answer to "which sources speak to papal control and internal quarrels", for 1556–65.

## Scope 10: tool runs, readability and live-file hygiene

- `python -m engine.m10.cli gaps jes`: `gaps: PASS`.
- `python tools/check_live_commentary.py --surface worlds`: exit 0 (report mode).
  - Doc_01: 1 PROTECTED hit (the §9 heading).
  - Doc_02: 1 REWRITE (line 249, the search record's date) and 1 PROTECTED.
  - Registry: 28 KEEP and 44 REWRITE, all iso-date, in the Added and Discovery cells.
  - Ledger: PROTECTED only.
- I read every REWRITE line. Each is schema data required by Framework V7.4 Step 2, not narration. The classifier marks them REWRITE because the Discovery cell carries a file name longer than the 39 characters its bare-date pattern allows before the date. But `--base origin/main --enforce`, which CI's `live-commentary` job runs on a pull request, exits 1, and lists 52 `jes` lines among the failures (P1-4).
- **Readability** (`engine.m7.turn_readability.score_turn`, markdown and code spans stripped):
  - Doc_01 scores FK 7.6, FRE 59.5, and 60.2 with the quotations removed.
  - Doc_02 scores FK 7.5, FRE 56.4, and 56.5 without quotations, so the shortfall is in the drafter's own prose.
  - Doc_02's lowest sections are §2 (54.0), §8 (51.2) and §9 (49.4).
  - Under the `hus` Round 2 precedent this is P2 (P2-14).
- **Process narration.** None found by reading, except one "now" in Doc_02 §1 (P2-13).

## Findings

**P1-1. The Roman letters in Salmeron's volumes are undercounted, and the largest group is missing.** Scope 8 gives the counts. The consequences for each file:

- Doc_02 §1 lists Polanco as "chronicle … 1555 only".
- Doc_02 §2 says of Polanco "Visibility: One year on the shelf, 1555".
- Doc_02 §6 point 1 says "1556 to 1562. The order's central voice is thin." About 117 of Polanco's commissioned letters from Rome fall in 1556–61, beside 15 of Lainez's as General.
- Doc_02 §6 point 2, row 69 and OG-5 give Mercurian as about 76; the count is about 86.
- Row 69's sample Borgia letter of 4 March 1565 is offered as a General's letter, but Borgia was elected on 2 July 1565 (row 33, lines 352–357). The letter itself speaks of "il Padre vicario".
- Row 67 and OG-5 do not say that only 15 of the Lainez letters fall in his generalate.

Fix: add the Polanco correspondence to §1, §2 and §6, and give it a Registry row or widen row 67. Correct the counts and dates. Re-state the gap for 1556–62 as "one correspondent's view of the Roman centre". Put the Scope 8 wording to the project lead as the change order.

**P1-2. The rites dates carry no confidence level.** Doc_01 §2 lists "Gregory XV's ruling of 1623, the Jiading conference (1627–28) and the Propaganda Fide decree of 1645" as events inside the window. The §6 table repeats 1623, 1645 and 1627–28 as ongoing forces. Doc_02 §8 records them as "No tag. Unverified", and OG-15 says "No confidence tag is assigned to them". Constitution Article 17 (paragraph 407) requires that "Every reconstruction carries a calibrated, visible level of evidential confidence drawn from a single fixed vocabulary". "No tag" is not a level, and the project rules say "Not Attested" is not a sixth one. Their only basis is Step 0 §2 A3 and the dossier (line 79), and neither names a source. Two honest fixes:

- **(a)** Keep the in-window finding, which Step 0 §4 item 4 binds. Move the specific dates out of the §2 event list and the §6 table into an absence statement tied to row 53 and request R4.
- **(b)** Tag each date Inferential/Thin, with its basis stated as "Step 0 and the dossier; no source on the shelf".

Option (a) is better. Scholarship widely accepts the dates, but this world's documents cannot show that from its own shelf.

**P1-3. Two claims cite rows that do not support them.**

- **(a) The Portuguese "royal right".** Doc_01 §2 (Cultural Environment) says: "Portugal claimed a royal right over the mission in Asia." §5 says: "In Asia the Portuguese Crown held a royal right … (row 24)." §6 says the Iberian kings "claimed rights over missions (rows 15, 24)". Neither row says this. Row 24 (Coleridge Vol. II, 27757–27770) shows the Nuncio's brief granted "by the Pope at the request of the King". Row 15 shows the King asking for men. No "patronage", "padroado" or "royal right" occurs in either Coleridge volume. The shelf does show a royal say in one place: row 30, lines 272–275, where the King decides the Ethiopian party's make-up if the Patriarch and the others disagree. Fix: state what the rows show, or add a row and a tag for the royal patronage.
- **(b) The report "from Ireland".** Doc_01 §2 says: "Their group reports to Ignatius from Ireland on 9 April 1542 (row 68)." Row 68 calls the heading's place and date garbled. The date is garbled ("9 APBILIS I542"), but the place is legible: "ALATIS CASTRIS" (line 2627). The letter was written after the men had spent 34 days in Ireland (2644). It was written from "desta misma villa", the same town as their previous letter, and that letter came from the court of the King of Scotland (2620–2622). Its summary says they plan to leave Ireland "et forte ex Scotia" (2632). Fix: "report to Ignatius after leaving Ireland, 9 April 1542", and correct row 68's description of the heading.

**P1-4. The pull request's live-commentary gate will fail on `jes` files.** `python tools/check_live_commentary.py --surface worlds --base origin/main --enforce` exits 1. The `jes` failures are:

- 44 Registry lines, plus Doc_02 line 249. By reading, these are schema cells (Scope 10). They fail only because the Discovery cells carry long file names.
- 7 lines in `Step0_Movement_Scope_Confirmation.md` (11, 39, 57, 59, 85, 87, 90). The branch edited that file in commit 13a49c1ad. These lines carry dated provenance of the project lead's rulings and one route cue.

The drafting audit reports only the report-mode "exit 0" and says the tool reports "only iso-date hits in schema fields". That is true of the classes, but it leaves out that the gate CI runs will fail. The rule in `CLAUDE.md` is that a pull request editing a live file also removes the commentary already in it. Fix:

- Shorten the Discovery cells so the date cell classifies as bare provenance (for example "direct read / row 14 file / 2026-09-30", with the file name moved to the Verification Note).
- Clean the seven Step 0 lines, or take the question to the coach thread if the classifier, not the cell, should change.

The `hus` Registry on this branch has the same 29-line pattern, and its reviews cleared it in report mode only.

**P2-1. The strand argument (Scope 2).** Take the "Cost" bullet out of the two-strand case. Add the §7 de Nobili and Ricci data to that case. Reconcile the two uses of the Ethiopian patriarch. Cite Article 21's default rule as the basis. The Nadal bullet in the single-strand case is weak: the Latin says he sailed to Africa "ad milites in spiritu juvandos", to help the soldiers (Nadal Praefatio 250–252). That is not movement between Europe and the missions. Also, the first scholion joins the defence and spread of the faith *to* the Society's end ("Huic fini coniungi", line 894). "The single aim behind both" (§1) and "as a single end" (§5) read a little more into it.

**P2-2. Corpus figures.** State that the counts are in a UTF-8 locale. Replace "This document does not reconcile the two" with the reconciliation in Scope 7.

**P2-3. Two tags.** Doc_02 §8 tags Xavier's day of death Inferential/Thin. Coleridge states it outright ("on the Friday, the 2d of December", Vol. II 30587–30588), so the fitting form is the one used elsewhere: "Documented as Coleridge's statement", with the single witness named. In the same table, "Documented for commitment 4" should match Doc_01 §8's own result, "largely shown", with "in glory" not found.

**P2-4. OG-6 lists "eternally" among the clauses not found in the Society's own words.** Faber's "qui ipsum ab æterno genuit sibi æqualem" (row 18, lines 9612–9615) is "eternally begotten of the Father". Doc_01 §8 does not list "eternally", so the ledger and the document disagree. Correct OG-6 with a new entry, because the ledger is append-only.

**P2-5. The search record says that the *Ratio Studiorum* and Acosta match no file.** With whitespace normalised, "Ratio Studiorum" matches five files. Four are this world's own:

- the MHSI Ignatius volume, lines 2979 and 3588, which cites Pachtler's *Ratio Studiorum et Institutiones Scholasticae*, the *Monumenta Germaniae Paedagogica* edition that row 45 names;
- the Nadal *Scholia*, lines 18072 and 18084;
- Nadal's letters;
- Salmeron Tomus Secundus.

Acosta matches seven files, five of them this world's. Correct Doc_02 §9 and the Registry's saturation statement. Give row 45's discovery channel as the vendored apparatus.

**P2-6. Row 63 dates Salmeron's commentaries "1598–1602".** Tomus Primus, line 1097, prints "Anno 1597" for Volume VII. Doc_02 §2 and request R11 already say 1597–1602.

**P2-7. Doc_02 §6, women: "This pass did not read whether they wrote or received the letters."** The cited locus answers the question. The Tomus Secundus Prooemium (lines 238–262) lists the two countesses among the "viris egregiis" whose letters were written *to* Ignatius, Lainez, Borgia or Salmeron. Say that they wrote.

**P2-8. Doc_02 §2 (Salmeron) and §6: "The editors omit Polanco's letters on wine and food purchases."** The editors omit the *passages* in Polanco's letters that deal with wine, provisions and payment ("quae a nobis in Polanci epistolis omittuntur, ea sunt quae ad vini et obsoniorum emptionem … referuntur", Tomus Primus 1033–1035), not the letters. In the same §2 sentence, "most of the letters he wrote in Lainez's name" reads as Polanco. It is Salmeron, as vicar in 1561–62 (1054–1057).

**P2-9. Doc_02 §2 (Lainez): "They add that this holds even against Xavier."** The Xavier clause is part of Ignatius's own reported judgment ("etiamsi magnus ille Indiarum apostolus in hac recensione contineretur", Lainez Praefatio 200–204, citing the *Monumenta Ignatiana*). It is not the editors' addition.

**P2-10. The bull's day.** Coleridge's own sentence (row 21, lines 4821–4822) dates the bull "on the Feast of SS. Cosmas and Damian, Sept. 17, 1540". The feast named in that sentence bears on which of the two days is right. Doc_01 §2 and Doc_02 §3 should note it. If the feast's day is attested on this world's shelf, the day can be settled; if not, it stays open, with the reason stated.

**P2-11. Small points in rows.**

- Row 13 quotes the dateline as "Rome, May 24, 1541". Line 2575 prints "Rente , May 24 :, 1541 ." Quote the scan's reading, or drop the quotation marks.
- Row 16 and OG-4 say that the letters run "to March 1548". The March item is Polanco's by commission (Scope 8). Ignatius's own letters end on 28 February 1548.

**P2-12. Ledger.**

- OG-2's Status line still reads "Open", though OG-3 records it resolved.
- OG-3 cites OG-2 by bare number, in its title and in its body. The ledger's rule is subject and date.
- Section E, item E1, says "The file matches the Jesuit words six times". Only one of the four files matches (`bellarmine_minds-ascent-to-god_1925.txt`, 6 lines); the other three have none.

**P2-13. Two statements in Doc_02.**

- §1: "Each file's header now says so for the seven Latin scans of the 25 September pass." This narrates a change inside a live file. State the fact.
- §2 (Faber): "made as Faber was beatified, in 1872". The shelf does not give the beatification year. The Bouix title page prints 1872, and Boero speaks of "the sanction given by the Sacred Congregation of Rites" (lines 103–104). Cite what the shelf says, or tag the year as the builder's knowledge.

**P2-14. Readability.** Doc_02's own prose scores FRE 56.5. Split the long sentences in §2, §8 and §9, especially the Transmission History entries and the search record.

## Not verified

- Latin and Portuguese quotations were checked against the scan text only, as the files' headers require. No page image was seen.
- The rites dates (1623, 1627–28, 1645) were not tested against any source. None is on the shelf.
- The letter counts in Scope 8 come from OCR headings. A few headings may be misread (for example "P^TRI"), so the figures are approximate within a few letters. The dates of the Polanco letters were read from the date line after each heading, and seven could not be parsed.
- Rows 29, 31, 37 and 38–72 (the B, C and D rows) were checked only for their form, their held or not-held statements and, where a vendored locus is named, that locus. The bibliographic facts in the C rows (editions, dates, series) were not checked against any external catalogue.
- Nadal's letters, most of Salmeron's letters, the Canisius body and the 1606 Constitutions were not read beyond the loci named above.
- The census's own claims ("three hundred thousand", "two hundred and fifty" colleges) were not tested.
- I could not verify from any record outside this drafting session that the project lead assigned the code `jes` (OG-10, the commit message of 13a49c1ad, and `CiC_Repo_Structure_Tracking.md` line 890). If the assignment came from a relayed instruction, the record should cite it, as the `hus` Round 2 review required for the strand ruling.
- I did not run `engine/m1/quote_verbatim.py`. The quotations were checked by my own normalising script and by eye.
