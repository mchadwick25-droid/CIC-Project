# Review: Step 0 — Eras 8 and 9 global completeness sweep (P2-G89), V1.0

Reviewer: independent Opus 5.5 review · 2026-11-10 · Round 2 (targeted recheck)

**Record under review:** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`, branch `claude/p2-g89-sweep`, at `9fd75bdb` (the merge of main, data release 29, onto `eca623a2`, "sweep record revised after Round 1").
**Diff checked:** `adc2ad80` to the branch head, for the record only.
**Scope (targeted recheck only):**
1. Whether the Round 1 findings S1, S2, M1-M9 and C1-C8 are closed.
2. The new counts, recomputed from the §2 Class column, and every place that states them.
3. Any new error the revision brought in (new claims; the new sub-questions in G89-6 and G89-26; VII.23's start).
4. Added by the coordinator after the merge of main: the rows that data release 29 added to `cic-website/data/world-census.json`, checked against the record's candidates (ME-4, RV-2 and RV-7 especially) and its §1 counts.
5. `tools/check_spelling.py` and `tools/check_paths.py`.

**Method:**
- I read the diff and the revision log, and the sections each fix touches.
- I opened the Paul of Aleppo file in `cic/texts/` at the cited lines.
- I fetched Bleby's raw text again with curl (archive.org `b24870109_djvu.txt`) into this session's scratchpad.
- I recomputed the §2 counts with a script over the Class column.
- I compared the census at `adc2ad80` (release 28) with the census at the branch head (release 29), by script: new IDs, changed era 8 and 9 rows, new links, and the §1 table.
- No repo file other than this review was written. No metered model call was made.

---

## 1. Round 1 findings: closure

| Finding | State | Evidence |
|---|---|---|
| S1 held-but-unread items | **Closed** | Volney vol. 2 (ME-4 item 4), Paisii (ME-13), Denisov (ME-5 item 3), Theiner vol. 4 (ME-10 item 2 and B1) and Duwayhī (ME-2 item 4) all read "[S] (held, not read)". No sentence rests on any of them as V. ME-13's registry wording is out of quotation marks. Paul of Aleppo is dropped from ME-4's Section A, which rests on the Charon berat. I opened `cic/texts/paul-of-aleppo_travels-of-macarius-v1_belfour1836.txt`. Lines 972-974 read "Paul by name, Archdeacon, or Shammas, of the Orthodox / Religion, of Aleppo", across a line break. Line 11828 has "this being / the year 1654", with the break after "being" (11827-11828). Both are verbatim apart from OCR spacing. The §2b and §6 Melkite rows now limit him to "the 1654 journey only". Two wording leftovers: R2-C4. |
| S2 AP3 | **Closed** | AP3 is "enter once (Section A settled)" in §2, its Recommendation, §2b and G89-26. G89-26's A5 sub-question gives two real options and a recommendation, and leaves the ruling to Mark. |
| M1 one home | **Closed** | G89-1(b), G89-23(a), §2 (AP2, RV-1) and RV-1's Overlap agree: AP2 tells the court mission and the Rites, ME-8 the 1698 union, and RV-1 points to each. |
| M2 links | **Closed** | The IV.26 flags read "continues as VIII.13 directly". The two re-routings are named in G89-6, G89-8 and G89-43. VI.24 "gave rise to" VII.4. |
| M3 VII.23's start | **Closed** | Presented as a proposal throughout ("by change order", "if the Melkite line goes there", with VII.18 as the alternative), and listed in G89-6. The census still has VII.23 at 1724-1815, so nothing is stated as done. Data release 29 changes VII.23 in another way: see R2-M1. |
| M4 era lines | **Closed** | G89-6 sub-question 2 states the rule with two options. G89-8 shows that (a) reaches outside scope, and gives (b) as the fallback. Release 29 adds a census precedent: see R2-M2. |
| M5 by precedent | **Closed** | §0 names the state. G89-6 sub-question 1 puts it to Mark. §2 writes "by precedent (row)". AP4's de Rhodes item is "for its date only". |
| M6 living marks | **Closed** | Every living line in §3-§7 without a dated item reads "none" (or "n/a" for a segment). "CR at most" survives only beside "Grade: none" (AF-4, AF-5, AF-7, ME-1). AF-1's sentence is gone. |
| M7 Bleby | **Closed** | The raw text, line 5785, reads "he learnt from his Bible, that the whites had no niore right". The record now quotes "he learnt", with "niore" read as "more" and flagged. One cosmetic leftover: R2-C5. |
| M8 G89-28 | **Closed** | Rec. (a) with its reason. (b) is the named alternative. |
| M9 ME-20 | **Closed** | "hold" in §2, §6 and G89-48. |
| C1-C8 | **Closed** | C1: the four hits are kept as titles and a name (re-run: 4 hits, 0 in enforced trees). C2: the path is full, and `check_paths.py` reports nothing for this file. C3: G89-36 reads "A line in VIII.31", and G89-39's (a) and (c) differ plainly. C4: Merolla and Zucchelli are [S]. C5: VIII.30 and VI.6 are added. C6: §2b gains the Propaganda line and "1245 to 1660". C7: AP1's Section A matches the fix. C8: G89-44 stops the Exarchate line at 1906. |

## 2. Counts

Recomputed from the §2 Class column (68 rows):

| Class | Africa | Latin America | Asia | Middle East | Rivers | All |
|---|---|---|---|---|---|---|
| enter | 5 | 2 | 5 | 8 | 3 | 23 |
| enter once | 0 | 0 | 1 | 0 | 2 | 3 |
| named line | 3 | 3 | 3 | 6 | 2 | 17 |
| hold | 1 | 4 | 6 | 5 | 2 | 18 |
| out of scope / carried | 0 | 0 | 1 | 0 | 0 | 1 |
| not counted | 0 | 2 | 1 | 3 | 0 | 6 |

Every cell matches the record's table. The two other places that state counts (the revision log's S2, M9 and closing lines, and the note that "enter" falls to 22 if G89-5 takes (b)) agree with it. R2-M1 and R2-M2 will change these counts again.

## 3. New errors from the revision

None of substance. The G89-6 and G89-26 sub-questions are real choices, each with options and a reasoned recommendation, and each marked as the merge's reading for Mark to rule. No new name, date or source is invented. The two cosmetic leftovers are R2-C4 and R2-C5.

## 4. Data release 29 against the record

Release 29 brings the census to 353 entries (23 of them persons) and 689 links. I compared it with release 28, the census the passes used. New rows in eras 7-9: VI.32 `hutterite-brethren` (1528-1785), VII.30 `swedish-lutherans-of-new-sweden` (1638-1786), VII.31 `english-unitarianism` (1774-1813), VII.32 `mennonites-and-amish-after-1650` (1650-1890), VII.33 `john-wesley` (a person, told within the Methodist revival) and VIII.52 `melkite-greek-catholic-church-after-1815` (1815-1911). One existing row changed: VII.23 now has `continuesAs` VIII.52, and a people list.

- **VII.30 (New Sweden) and VII.33 (Wesley):** North America and North Europe, outside the sweep's scope. No candidate touches them. Clean.
- **VI.32, VII.32 and VIII.52:** see R2-M1 and R2-M2.
- **VII.31:** see R2-C2.

---

## Substantial findings

None.

## Moderate findings

### R2-M1. ME-4's Catholic row now exists as VIII.52
- **Location:** §6 ME-4 (break note, B3, Recommendation, G-ME4); §2 row ME-4; §2b Melkite row; §6 §3 ranked list and coverage table; G89-42.
- **Evidence:** VIII.52, "The Melkite Greek Catholic Church after 1815", runs 1815-1911, in the 3<->5 bridge lane. It carries Maximos III Mazloum, the synods from 1816, the 1831 synod called by Propaganda and the 1848 berat, on Charon (1910-1911) and Mansi vol. 46. VII.23 now continues as VIII.52 (Documented). So ME-4's "neither Melkite church has any entry after VII.23 ends in 1815" and its B3 ("Both Melkite churches vanish from the tree between 1815 and the present") are now false for the Catholic side. Its "enter one era 9 row for both churches" would duplicate VIII.52. What is still missing is the Antiochian Orthodox side after 1815. ME-4 rates that side "thin" (Fortescue only, a hostile witness). The 1650-1724 line is untouched by the release.
- **Fix:**
  - Mark ME-4's Catholic side "already carried (VIII.52)".
  - Restate ME-4's row as the Orthodox Patriarchate of Antioch, 1815-1906. By the pass's own B1 that is "hold" until an Orthodox source is read, for example on the 1899 election. A named line in VII.18's or VIII.28's story is the alternative. A line in VIII.52 would mis-home it, since VIII.52 is the Catholic church alone.
  - Rewrite G-ME4 and G89-42 so their options follow from this. Option (b) already has this shape.
  - Rewrite the break note, B3, Overlap (add VIII.52), and the §2b, §2 and §6 tables.
  - Recount: on "hold", enter 23 → 22 (Middle East 8 → 7) and hold 18 → 19 (Middle East 5 → 6).

### R2-M2. RV-2's "one Anabaptist continuation row" now exists as VII.32, and the Hutterites have VI.32
- **Location:** §7 RV-2 (Recommendation and options); §2 row RV-2; §6 ME-22 and its coverage table; §7 river table; G89-49; G89-6 sub-question 2.
- **Evidence:** VII.32, "The Mennonites and the Amish", runs 1650-1890. It has the link "the-anabaptist-movements continued as" VII.32 (Documented). Its regions are the Netherlands and Pennsylvania only, with no Russia. VI.32, the Hutterite Brethren (1528-1785), ends with "A few families kept the faith and moved on to Russia". It rests on the same Beck 1883 file that RV-2 cites. Three things are now false: RV-2's and G89-49(a)'s premise that the continuation row has yet to be made; ME-22's "has no Mennonite row in eras 8-9"; and the tables' "none after VI.3" and "VI.3 to 1650". G89-6 sub-question 2 lists "RV-2 1650-1906" as a new crossing row. Its era-line question now has a census precedent, since VII.32 itself crosses 1815.
- **Fix:**
  - Restate G89-49:
    - (a) The Russian colonies as a named chapter in VII.32. This needs a change order: Russia and Ukraine added to VII.32's countries and text, and VII.32's end checked against 1906.
    - (b) A Russian Mennonite and Hutterite row, 1789-1906, with links from VII.32, and "continued as" from VI.32 for the Hutterites.
    - (c) A named line in VIII.51, as now.
  - Recommend one of them with its reason. Rewrite the three false statements, and add VII.32 and VI.32 to RV-2's Overlap.
  - In G89-6 sub-question 2, drop "RV-2 1650-1906" and cite VII.32 as the census's own crossing row.
  - Recount for the option the record recommends. Under (a), RV-2 becomes "named line" (rivers: enter 3 → 2, named line 2 → 3).

## Cosmetic findings

- **R2-C1. §1 is at release 28.** It is dated correctly ("data release 28: 322 movements"), but the record now sits on release 29. Either restate §1 at release 29 or add one line that §1 is the passes' census. At release 29:
  - 353 entries.
  - Era 8: 34 entries, one of them a person (VII.33), with 44 region tags (North Europe 21, North America 4, the rest unchanged).
  - Era 9: 52 entries and 70 tags (Middle East 2).
  - Era 8's Protestant and Evangelical river: 15 entries (North Europe 12, North America 3).
  - The §1 prose ("30 entries, and 18 of them carry North Europe"; "51 entries and 69 region tags") follows these numbers.
- **R2-C2. RV-7 and VII.31.** English Unitarianism (England, 1774-1813, lane 8, a floor question) is a different body from the Transylvanian Unitarians, so there is no overlap and no change of class. Add VII.31 to RV-7's lane 8 precedents ("as VI.14, VII.27 and VIII.37") and to its Overlap.
- **R2-C3. A data flag.** VIII.52 runs to 1911, past era 9's end in 1906, which is the window the record holds every era 9 history to. Log it in §10 as noticed and not touched.
- **R2-C4. S1 wording leftovers.**
  - ME-2's Section A still begins "Dated own statement in the era: Duwayhī's *Tārīkh* ... [S]". Write "No dated own statement read; Duwayhī held, not read [S]", to match §2's "by precedent".
  - §6's "Non-English sources used" lists Denisov and Paisii. Write "held, not read" beside them.
- **R2-C5. Bleby's "I".** The record quotes "I would rather die upon yonder gallows". The OCR (line 5791) has "would rather die upon", and Round 1 said the page image must settle the "I". Write "[I] would rather die ...", or note that the "I" is supplied pending the page-image check.

## Clean checks

- **S1, S2, M1-M9, C1-C8:** all closed (table in section 1).
- **Paul of Aleppo:** both cited strings are verbatim at the cited lines.
- **Bleby:** "he learnt from his Bible" is verbatim at OCR line 5785.
- **Counts:** every cell recomputes, and every statement of them agrees.
- **New sub-questions (G89-6 sub-questions 1 and 2; G89-26's A5 sub-question):** real options, a reasoned recommendation, the ruling left to Mark.
- **VII.23's start:** a proposal, not a fact. The census still reads 1724-1815.
- **Release 29, out of scope:** VII.30 and VII.33 touch no candidate.
- **`tools/check_spelling.py`:** 4 hits, 0 in enforced trees. All four are titles or a proper name, as Round 1 found.
- **`tools/check_paths.py`:** no unresolved path in this record.

---

## Verdict

**PASS WITH FIXES.** Every Round 1 finding is closed. The revision added no error of substance. The two moderate findings come from data release 29, which landed after the passes ran. Each is fully set out above, and neither needs new research: each reclassifies one row, rewrites its gate question and recounts. The cosmetic findings are wording only.

**Counts: S 0, M 2, C 5.**

No substantial finding remains. This is round 2 of 3 under the cap. The reviser can apply the fixes and check them against this list. A third review should be a targeted check of R2-M1 and R2-M2 only, if one is wanted.
