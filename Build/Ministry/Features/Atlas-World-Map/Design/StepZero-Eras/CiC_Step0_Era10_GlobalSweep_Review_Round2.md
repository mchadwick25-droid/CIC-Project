# Review: Step 0 — Era 10 global completeness sweep, V1.0

Reviewer: independent Opus 5.5 review · 2026-11-09 · Round 2 (targeted recheck)

**Record under review:** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_GlobalSweep_V1_0.md`, branch `claude/era10-global-sweep`, pulled 2026-11-09 at `d0e9f1b2c` (2,661 lines).
**Diff checked:** `33802d821` ("Global sweep: Review Round 1") to `d0e9f1b2c` ("Global sweep: Round 1 fixes and the supplementary pass"). The diff touches the record and `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (new entry 137).
**Scope (targeted recheck only):**
1. Whether the Round 1 findings S1–S5, M1–M18 and C1–C5 are closed, with M17's departure judged on its merits.
2. The new §6b supplementary pass (SUP-1 to SUP-15) and its questions G-136 to G-150.
3. The new questions G-132 and G-133.
4. The §2 counts, whether all 71 questions parse, and spelling.

**Method:**
- I downloaded 30 pages and read their raw text (curl plus an HTML-stripping script, no summarizer). I used one web search, for Cottesloe, and then opened the PDF it found.
- I recomputed the §2 counts from the table's Class column with a script.
- I parsed §7 with a regex that checks the number, title, ID, at least two options, and that the recommended letter names an option that exists.
- I checked the IX.11 wording in the census JSON (`cic-website/data/world-census.json`) directly.
- I ran `tools/check_spelling.py` on the file.
- No repo file was edited, and no metered model call was made.

---

## 1. Round 1 findings: closure

| Finding | State | Evidence |
|---|---|---|
| S1 LA-4 | **Closed** | §2 class is "enter once". The Recommendation, G-LA4 and G-93 all name the Liga's 1925 program or a dated *cristero* manifesto. They also say that neither the episcopal act nor the 2000 homily is the movement's own text, and that the episode-row precedent does not waive the rule. |
| S2 LA-2, GS-A8, GS-A11 | **Closed** | All three are "enter once" in §2 and in their Recommendations. G-109 and G-112 carry the condition. LA-2 names the *Cremos* and the *Pontos de Doutrina e da Fé*. The four regions' counts are now 14 / 11 / 20 / 14 = 59, which I recomputed. |
| S3 IX.11 | **Closed** | LA-2's B3 and Overlap name "Two Swedes Sail for Pará" and Alencar 2010. I confirmed the story in the census. G-91(a) states the move, and G-132 is a real scope question (see §3 below, with one minor link fix, R2-M3). |
| S4 living marks | **Closed** for the rows named | GS-A9, GS-A11, GS-A15, GS-A8, GS-A10, GS-A12, LA-5 and C6 are now "none". GS-A13 is "CR (2023), once the volume's date is verified". The §8 subsection "Dated items for the living marks" lists every one. The same error recurs once in the new SUP-11 (R2-M2). |
| S5 Nguyễn Xuân Hùng | **Closed** | The item is [S], the 1927 name in the Dates line is [S], and the item is on the §8 wanted list. |
| M1 spelling | **Closed** | `check_spelling.py` reports 0. "Coloured" and "Centre for the Study of Australian Christianity" are kept as names. |
| M2–M6 | **Closed** | M2: 29 June 1958, with the vatican.va URL. M3: the DOI. M4: the Cambridge UL archive record. M5: "Malua" [S]. M6: Studia Missionalia Upsaliensia 74 [S]. |
| M7 E1/IX.22 | **Closed** | The list and the Overlap name Tikhon, the 2000 Jubilee Council and the 2007 Act as IX.22's. |
| M8 Medellín/Puebla | **Closed** | G-90(a) states the change to IX.8. |
| M9 charismatic placement | **Closed** | Cross-references are in G-95 and G-107. G-133 is added. |
| M10 old G-132/G-133 | **Closed** | Both are dropped and the numbers reused. The §7 opening paragraph is updated. |
| M11 G-134/G-135 | **Closed** | Each has a recommendation, attributed to Round 1, and G-135 now has option (c). |
| M12 | **Closed** | E2 says "Three of the four…", with Derewenda V-s. G-104(b) says "not yet eligible". E3a names the 1999 posthumous edition as V-s. |
| M13 C6 | **Closed** | The Recommendation line now matches G-85 and §2. |
| M14 E4 tier | **Closed** | Tier 2 is set on B1–B5, and the balance point is in G-125. |
| M15 | **Closed** | The 2025 Kairos sentence is gone. E5 reads "patriarch from 1979". |
| M16 balance | **Closed** | §2 has a "Not swept" list by region, and §6b covers the places Round 1 named. Open-Gaps entry 137 logs the three areas still unswept. The CHAI *History of Christianity in India* is on the §8 list. |
| M17 Cottesloe | **Departure accepted; closable now (R2-M1)** | See below. |
| M18 C1 lane | **Closed** | G-80 names the other Catholic regional rows, SUP-1 included, and frames the choice as cross-cutting. |
| C1–C5 | **Closed** | C1: the 1956 doubt is deleted. C2: the signatory count is qualified. C3: the 1 June 1939 notice date is added. C4: the Cerf note is reworded. C5: no "summarizer" caveat remains. |

**M17 on its merits.** The departure is right. Moving C2's start to 1985 would have cut the movement off from its own beginning. The Kairos Document is the movement's mid-point, not its founding. A 1960 start was acceptable while it stayed [S], was named as [S] in the Dates line and the four-marks line, and sat on the §8 wanted list. It no longer needs to stay [S]. I opened a scholarly page that confirms the date (R2-M1). C2 is classed "enter", so the fix should be made before the gate. It is mechanical.

---

## 2. §6b supplementary pass: items re-verified

I re-verified 24 items marked V or V-q. Each was read in the raw text of a downloaded page. **All 24 match as stated.** The exceptions noted below are labeling issues, not wrong facts.

| # | Item (candidate) | What the page shows |
|---|---|---|
| 1 | **Falla**, *Quiché rebelde* (SUP-1) | The UT Press page gives the English edition: translated by Phillip Berryman, Jesuit anthropologist. It says, verbatim, "examines what happened when Acción Católica came into the Guatemalan municipio of San Antonio Ilotenango, Quiché". **The 1978 Editorial Universitaria imprint is not on the page**, so it is correctly V-s in the evidence list. See R2-M4 for B1. |
| 2 | **Kovic** 2005 (SUP-1) | UT Press: publication date 2005-05-01, 248 pages. Matches. |
| 3 | **Waterfield** 1973 (SUP-2) | Church History 43.1, March 1974, p. 129. Reviewer R. Pierce Beaver. The title gives Barnes and Noble, 1973, 192 pp. Matches. |
| 4 | **Gómez Treto** 1987 (SUP-3) | Atla record: "San José, Costa Rica: DEI. 1987". Matches. |
| 5 | **Kirk** 1989 (SUP-3) | The Americas 46.3, January 1990, pp. 407–408. Reviewer Daniel H. Levine. The title gives "Gainesville: University of South Florida Press, 1989. Pp. xxi, 231". Matches. |
| 6 | **Corse** 2007 (SUP-3) | JLAS 41.1 (2009), pp. 177–179. Reviewer Daniel R. Miller. The title gives "University Press of Florida, 2007, pp. xi+195". Matches. |
| 7 | **1998 Havana quote** (SUP-3), word for word | The page is headed "Ceremonia de bienvenida (Aeropuerto de La Habana, 21 de enero de 1998)". The raw text contains exactly «Que Cuba se abra con todas sus magníficas posibilidades al mundo y que el mundo se abra a Cuba». The sentence goes on with «, para que este pueblo…», and the record quotes the clause correctly. **Matches verbatim.** The page does not name "José Martí" (R2-C1). |
| 8 | **Walbridge** 2003 (SUP-4) | Routledge page: "Copyright 2003". The Contested quote matches verbatim: "In May 1998, John Joseph, the first native Pakistani Catholic bishop, shot himself in front of the courthouse where a Christian had been sentenced to death for blasphemy." The page names the publisher as Routledge. The record's "RoutledgeCurzon" is the 2003 imprint and is not wrong. |
| 9 | **O'Brien** (SUP-4) | CiNii: "[2006?]", Lahore, Subaltern studies series publication no. 1. Matches. |
| 10 | **Perry** 1989 (SUP-5) | Daystar catalog: "Kathmandu: Nepal Church History Project, 1989". Matches. |
| 11 | **Yale Nepal exhibit quote** (SUP-5) | Matches verbatim: "Until November 1990, changing religion was illegal. The law authorized severe penalties for attempting to convert another person." |
| 12 | **Sharkey** 2008 (SUP-6) | Church History 80.4, December 2011, pp. 956–959. Reviewer Akram F. Khater. The title gives Princeton 2008, xvi + 318 pp. Matches. |
| 13 | **MECC founding** (SUP-6) | mecc.org: Nicosia, "from the 28th till the 30th of May" [1974]. The evangelical members Aharonian, Dagher and Fares are named. Matches. |
| 14 | **Tegenfeldt** 1974 (SUP-8) | JSEAS 8.2, September 1977, pp. 246–248. Reviewer Frank N. Trager. The title gives William Carey Library 1974, xxv + 512 pp. Matches. |
| 15 | **Tan** 2011 (SUP-9) | STM page: "Oxford: Regnum Books International", "Copyright © Jin Huat Tan 2011", ISBN 978-1-870345-99-6, Regnum Studies in Missions. Matches. |
| 16 | **Prasit** 1984 (SUP-10) | CiNii: ประสิทธิ์ พงศ์อุดม, CCT Archives, 2527 BE (1984). Matches. |
| 17 | **Songkhon homily quote** (SUP-10) | vatican.va: "Here was a lay person who was deeply conscious that through Baptism he belonged to Christ, Priest, Prophet and King, and was thus personally called to proclaim the Gospel." Matches verbatim, and the page spells the village "Songkhong". |
| 18 | **Stirrat** 1992 (SUP-11) | Cambridge Core: print publication year 1992, "September 1992", Cambridge Studies in Social and Cultural Anthropology. Matches. |
| 19 | **Bal** 2007 (SUP-12) | Cambridge Core: ISEAS, 16 August 2007, ch. 7 "Garos and Christianity" (pp. 132–157). Matches. |
| 20 | **Peyrouse**, Nationalities Papers (SUP-13) | 32.3, September 2004, pp. 651–674. Matches. |
| 21 | **Pelkmans** 2009 (SUP-13) | Berghahn: "Published (November 2009)". Chapter 8 is "Temporary Conversions: Encounters with Pentecostalism in Muslim Kyrgyzstan", Mathijs Pelkmans, and is listed on the page (R2-C2). Matches. |
| 22 | **Römer** 2024 (SUP-2) | Torrossa: I.B. Tauris, 2024. Matches. |
| 23 | **Kirk/Corse/Gómez Treto as "three verified studies"** (G-138) | Holds, on items 4–6. |
| 24 | **Cottesloe date** (C2, for M17) | E. Van der Borght, "'Unity that sanctifies diversity'. Cottesloe Revisited", *Acta Theologica* 31.2 (2011). Its bibliography cites "The Report of the Consultation among South African Member Churches of the World Council of Churches 7-14 December 1960 at Cottesloe, Johannesberg". Source: https://scielo.org.za/pdf/at/v31n2/v31n2a03.pdf (PDF read). |

**Are any search-result-only items treated as verified?**
- In the evidence lists, every item seen only in a search result or summary is labeled V-s or [S].
- Two places in the prose claim more than the evidence list does:
  - SUP-1's B1 marks Falla's 1978 Spanish imprint "V" (R2-M4).
  - SUP-3's Dates line puts "(V-q)" on the whole 21–25 January visit (R2-C1).
- No class or recommendation rests on either claim.
- The legend's rule that V-s "never counts as verified" is otherwise kept. G-138's "three verified studies" and G-140's own-voice point both rest on items that really are V.

**§6b structure.** Each of the 15 candidates has every field the regions use, a Contested line where one is needed, and a stated class. §2 and §6b's own table agree on every class. Each recommendation follows from its evidence state:
- the four "enter once" rows each name a concrete condition;
- the eight holds each name what they wait for;
- the three named lines each name their receiver.

The cross-ties are stated (G-138 with G-90, G-139 with G-103). Three defects follow (R2-M2, R2-M5 and R2-M6).

---

## 3. G-132 and G-133

**G-132 (IX.11's future): real options, not pre-decided.**
- The question sets out IX.11's content accurately. I confirmed the census wording: "only a bounded window — one body, one country, one generation — describes anything real here". It names all six drawing candidates.
- The options are distinct: (a) umbrella, (b) narrow, (c) hold the country rows.
- It recommends (b) with a reason, gives a reason against (c), and marks itself as the reviser's recommendation and Mark's call.

There is one defect. G-91(a) already contains the move of the Pará story ("moves to this row by a named change order … (see G-132)"). So a ruling of G-91(a) with G-132(a) would contradict itself, and neither question says that the two must be ruled together (R2-M3).

**G-133 (Catholic charismatic rule): real options, not pre-decided.**
- (a) By movement, (b) by national church, and (c) a stated mixed rule are three different rules, and each is spelled out.
- The recommendation for (c) gives its basis: Wiegele's framing of El Shaddai as Philippine popular Catholicism, and the CCR's single origin.
- It says "Either single rule, (a) or (b), is also defensible".
- G-95 and G-107 each point to it.

Clean.

---

## 4. Counts, parsing and spelling

- **§2 counts:** I recomputed them from the table's Class column (74 rows):
  - Africa 3/1/5/4 (13); Latin America 2/3/4/4 (13); Asia 5/4/7/4 (20); East 4/3/4/2 (13); Supplement 0/4/3/8 (15).
  - All: enter 14, enter once 15, named line 23, hold 22, total 74.
  - Every cell of the counts table matches. The prose ("14 / 11 / 20 / 14 = 59"; "4 / 3 / 8") matches. §6b's own count ("enter once 4, hold 8, named line 3") matches.
- **§7 parse:** all 71 questions, G-80 to G-150, match `- **G-n. Title (ID)** … (a) …; (b) … **Rec. (x)**`. None is missing or duplicated. Every question has at least options (a) and (b), and every recommended letter names an option that exists. The opening paragraph's arithmetic (52 + 4 + 15 = 71) is right. A second copy of the 15 supplementary questions, numbered G-SUP-1 to G-SUP-15, sits in §6b (R2-M5).
- **Spelling:** `python3 tools/check_spelling.py` on the file gives "0 British spelling(s) found in 0 file(s); 0 in enforced trees".

---

## Substantial findings

None.

## Minor findings

- **R2-M1. C2's Cottesloe date can now be verified (closes M17).**
  - **Location:** C2 Dates line (line 310), four-marks line (line 321), §8 C2 wanted line (line 2643).
  - **Fix:**
    - Change "1960 (the Cottesloe consultation [S])" to "7–14 December 1960 (the Cottesloe Consultation, Johannesburg; verified)", citing E. Van der Borght, "'Unity that sanctifies diversity'. Cottesloe Revisited", *Acta Theologica* 31.2 (2011), whose bibliography cites the Consultation's Report of 7–14 December 1960 (https://scielo.org.za/pdf/at/v31n2/v31n2a03.pdf).
    - In the four-marks line, change "Cottesloe 1960 [S]" to "Cottesloe, December 1960 (verified)".
    - Delete the C2 line from §8.
  - Mechanical.
- **R2-M2. SUP-11's living mark repeats the S4 error.**
  - **Location:** SUP-11, Living today (line 2214).
  - **Evidence:** The record says "newest dated evidence: not fixed … (journalism; year [S]). Grade: CR." Under R3 an item counts only if it is dated after 2010. Round 1 regraded C6 to "none" because its year was [S], and the same rule applies here.
  - **Fix:** Change it to "Grade: none (no dated item after 2010)", and add "the year of the Global Sisters Report piece" to §8's "Dated items for the living marks". Mechanical.
- **R2-M3. G-91 and G-132 can be ruled into a contradiction.**
  - **Location:** G-91(a) (line 2392) and G-132 (line 2442).
  - **Evidence:** G-91(a) moves the Pará story to LA-2, while G-132(a) keeps it in IX.11.
  - **Fix:** Add to G-132: "Rule with G-91: G-91(a) as written assumes (b) here. If (a) is chosen here, G-91(a) enters LA-2 with a cross-reference to IX.11's Pará story instead of moving it." Add "(rule with G-132)" after "see G-132" in G-91(a). Mechanical.
- **R2-M4. SUP-1's B1 marks the Spanish Falla imprint as verified.**
  - **Location:** SUP-1, B1 (line about "Quiché rebelde (Editorial Universitaria, 1978; Spanish; V)").
  - **Evidence:** The evidence list correctly gives "V-s (Spanish imprint) / V (English edition)". The opened UT Press page does not show the 1978 imprint.
  - **Fix:** In B1, change "(Editorial Universitaria, 1978; Spanish; V)" to "(Editorial Universitaria, 1978, V-s; English edition, UT Press, V)". Mechanical.
- **R2-M5. A duplicate question set and a stale process note in §6b.**
  - **Location:** §6b "#### 3. Gate questions in the record's format" (lines 2326–2344).
  - **Evidence:** The section repeats all 15 questions as G-SUP-1 to G-SUP-15, under the note "Numbered G-SUP-1 onward for the assembler to renumber after G-135". §7 already carries them as G-136 to G-150, and each candidate in §6b carries its own copy too. A third copy under different numbers invites citing or ruling the wrong number. The note also describes a step that is already done.
  - **Fix:** Replace the subsection's body with one line: "These are G-136 to G-150 in section 7." Mechanical.
- **R2-M6. G-138 and G-139 drop the condition their candidates' class carries.**
  - **Location:** G-138 (SUP-3) and G-139 (SUP-4), and the matching "Recommended" lines in §6b.
  - **Evidence:** Both candidates are "enter once" in §2 and in their Recommendations: SUP-3 until the ENEC document is opened and the Protestant wing's Section A is settled; SUP-4 until the Church of Pakistan's Basis of Union is opened. Their gate recommendations read plain "**Rec. (a)**". G-136 and G-137 carry their conditions. Read alone, a ruling of (a) here would look like "enter now", which is the inconsistency S2 corrected.
  - **Fix:**
    - G-138: "**Rec. (a)** Once the ENEC final document is opened and the Protestant wing's Section A is settled on one dated statement."
    - G-139: "**Rec. (a)** Once the Church of Pakistan's Basis of Union is opened for Section A."
    - Make the same change in the §6b "Recommended" lines.
  - Mechanical.

## Cosmetic findings

- **R2-C1.** SUP-3 (Dates line and evidence item 5):
  - Change "John Paul II in Havana, 21-25 January 1998 (V-q)" to "21-25 January 1998 (the 21 January arrival speech V-q; the visit's end date V-s)".
  - The page says "Aeropuerto de La Habana", not "José Martí". Write "Havana airport", or mark "José Martí" [S].
- **R2-C2.** SUP-13: the Pelkmans chapter is listed on the opened Berghahn page ("Chapter 8. Temporary Conversions: Encounters with Pentecostalism in Muslim Kyrgyzstan"). "V (book) / V-s (chapter)" can become plain "V".

## Clean checks

- **Every Round 1 finding:** S1–S5, M1–M16, M18 and C1–C5 are closed. M17's departure is sound and closes with R2-M1.
- **§6b's 24 re-verified items:** all match, including the three quotes verbatim (Havana 1998, Yale Nepal, Songkhon 1989) and the Walbridge Contested quote.
- **§6b's labeling:** no V-s item carries a class or a recommendation. Holds and named lines follow from their evidence. The Contested lines (genocide, the 1994 killings, convert numbers, the SIL, Balasuriya, John Joseph's death) are present where needed.
- **G-132 and G-133:** both give real, distinct options with a reasoned recommendation, and leave the choice to Mark.
- **§2 counts:** every cell is correct.
- **§7:** 71 of 71 questions parse, with no gaps and no invalid recommendation letters.
- **Spelling:** clean (0).
- **Open-Gaps entry 137:** it logs the three unswept areas. It is append-only and numbered, and cites the record and section by name.

---

## Verdict

**GATE-ELIGIBLE AFTER FIXES.** The fixes are all mechanical: six minor and two cosmetic. None needs new research. R2-M1 uses the source cited above. No substantial finding remains, so no further review round is needed. The reviser can apply the fixes and check them against this list.
