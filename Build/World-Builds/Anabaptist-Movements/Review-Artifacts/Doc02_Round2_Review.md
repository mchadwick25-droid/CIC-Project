Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: Opus Round 2 reviewer, Anabaptists (independent subagent; wrote none of the text under review)
Drafter agent: a308a6756db757d95 (Sonnet)
Round: 2
Truncation check, method 1: structural count. `wc -l -c` gives Doc_02 396 lines / 78,523 bytes, Registry 176 / 117,315, gap ledger 183 / 20,545. Doc_02 has eleven `##` headings, §1 to §11 in order, the last "## 11. Disposition". The Registry has 107 table rows numbered 1 to 107 with no gap or duplicate, every row with exactly 16 pipes. The header counts (107 rows; 99 Native, 8 Excluded; 28 A, 23 B, 51 C, 5 D; 81 P, 24 S, 2 M) reproduce exactly from the rows. The ledger runs OG-1 to OG-21.
Truncation check, method 2: tail read and byte check. Each file ends on a complete sentence followed by a newline (`tail -c1 | od -c` gives `\n`): Doc_02 ends "...note the new floor evidence (OG-10).", the Registry ends "...none relevant, and was dropped.", the ledger ends "...the title and edition are needed." SHA-256 prefixes at review time: Doc_02 18112f93eebf2400, Registry 8d15eab0f6d9f67c, ledger 3519ec91115b4ebd. All three differ from the Round 1 prefixes (48446021a65126e1, da2a5729082fafa6, acae82f1862dfe7d).

# Review of Doc_02_Source_Ecology.md and Source_Registry.md (The Anabaptist Movements, VI.3)

**Date:** 23 October 2026. **Scope:** a targeted recheck, as the cap rule requires from Round 2 onward. I rechecked the 18 Round 1 findings and the changed text. I spot-checked every quotation and locus that was added or changed, including rows 100 to 107, the Riedemann and Blaurock counts, the Middelburg loci and the Dirk Willems locus. I also ran the live-commentary checker on scratch copies. No git was available to this reviewer, so the diff was found by reading every passage the Round 1 findings named, plus the new rows and the new OG entries.

## Verdict

**Cleared.** 0 BLOCKING, 7 COSMETIC (all new, all small).

All eight Round 1 blocking findings are resolved. All ten Round 1 cosmetic findings are resolved. The quotation script was re-run on the revised files. It found 104 of 104 located quotations in Doc_02 and 138 of 139 in the Registry at their cited lines. The one miss is the all-capitals heading of row 20, which was accepted in Round 1. Nothing new is wrong in substance. The seven new cosmetic items are listed below for the drafter. None of them justifies another review round.

## Round 1 findings: status

| Finding | Status | Locus checked |
|---|---|---|
| B1 Orange's son | **Resolved** | Doc_02 §6 (line 194), Cell 2A (207), §8 (319) now name three acts: William I's letter of privilege, 26 January 1577 (*Mirror* 148004–148005, verified); the charge of 16 July 1578 (from 148155, verified); Maurice's letter "Gravenhage, on the 4th of March, 1593" (152809, verified). The Remark (148235–148239) is now read correctly as the son ending the renewed oppression. Doc_02 now agrees with Doc_01 §2 and §5. |
| B2 Riedemann's letters | **Resolved** | New row 100. Contents loci 534, 563, 569 and 595, and the letter openings at 12461 ("Will Euch mit kurzen Worten das Urteil dieses Spahns") and 12636 ("Peter, Dein Bruder und Vertrauter im Herren"), were verified in Wolkan. §2 Visibility, §7 item 2 and §1 are updated, and OG-20 is added. On the count, see N2. |
| B3 Sattler's date | **Resolved** | Doc_02 §4 (158) and §8 (305): Böhmer line 1733 "Sattlers märtyrertod, 21 Mai 1527" (verified); the *Mirror*'s closing line 58958 (verified); the Chronicle's 21 May given to the arrest. |
| B4 Dirk Willems locus | **Resolved** | Doc_02 §4 (160) and §8 (327) cite line 104653: "trustworthy persons, that when he fled he was hotly pursued by a thief-catcher" (verified). Line 86506 is no longer cited. |
| B5 baptism sequence and Doc_01 routing | **Resolved** | §3 item 2 and §8 (299) now read "*Documented* as the Chronicle's account; one witness on this shelf". OG-18 routes the baptism sequence to the lead, and OG-19 routes Sattler's authorship. |
| B6 rows 49 and 50 | **Resolved**, with one new slip (N3) | Ribbeck has 10 lines with "Wiedertäufer" (verified, with the eight ancient-sense lines listed correctly). For von Soden, two files have line 332 and line 1564 (verified). |
| B7 McGlothlin's Sixth Article | **Resolved** | Row 22, Doc_02 §7 item 3 (240), §8 (304) and OG-4. The file's lines 647–654 are now described as the Sixth Article's last paragraph. Jackson's parallel, lines 8281–8283, was verified. |
| B8 recall and PRESS | **Resolved**, with N5 and N7 | §9 records recall 5/10 and the PRESS answer. Rows 101 to 107 were added at C, with no claim resting on them, and OG-21 was added. §3 now says the modern scholarly view was not consulted (line 126). |
| C1 doubled loci | **Resolved** | No doubled locus remains in any of the three files (checked by pattern search). |
| C2 spliced sentences | **Resolved** | The §2 Sattler (88), Dirk (73) and §3 item 4 (134) passages and rows 13, 23 and 25 are rewritten as whole sentences. §3 item 2's Marx Bosshard sentence still reads awkwardly, but it is grammatical. |
| C3 row 27 Vorrede | **Resolved** | Row 27 now quotes "glaubhaften Menschen" (line 2888) and "auch was ich selbst in guter und gewisser Erfahrung hab" (2890–2891), both verified. |
| C4 query count | **Resolved** | Doc_02 §9 and the Registry's saturation statement both say 38 (27 first runs, 4 repeats, 7 for the recall works). |
| C5 title labels | **Resolved** | Row 4 now gives unquoted descriptions with the title-block loci (30255–30266, 26170–26180). |
| C6 OG-4 quotation | **Resolved** | OG-4 and Doc_02 §7 item 3 now quote the header as "were never printed and survive only in archival manuscript" (lines 18–19). |
| C7 Zapff | **Resolved** | Doc_02 §2 (102) gives the foreword's "Haupprecht Zapff" (117–118) and the text's "Haupprecht Zapf" (2952), and states which form it uses. |
| C8 Library-stage outputs | **Resolved** | A new paragraph at line 392 gathers the corpus-map corrections, says that PAIRS.yaml holds no ruling for this world, and names the dossier's three siblings, leaving the question to the Library and the lead. |
| C9 §7 item 9 | **Resolved** | Line 264 now says the German quotations carry weight and are provisional until the page images are read. |
| C10 process narration about the review | **Resolved** in Doc_02 | The "for Round 1" sentences are gone. The status lines name the round, which is accepted (the checker marks them PROTECTED). See N4 for a new instance. |

## Spot-checks of added or changed quotations and loci

All of these were verified at the cited lines:
- **Middelburg:** 148004–148005, 148155, 148235–148239, 152809.
- **Dirk Willems:** 104653.
- **Sattler:** Böhmer 1733; *Mirror* 58958; Wolkan 5816.
- **Riedemann:** Wolkan 534, 563, 569, 595, 12461, 12636, 13665, 13789, 13915, 14039, 20337–20413.
- **Chronicle Vorrede:** Wolkan 2888, 2890–2891.
- **McGlothlin:** 18–19, 647–654; Jackson 8281–8283.
- **Kolb:** 1306–1308.
- **Ribbeck:** the ten lines; von Soden 332 and 1564.
- **Funk title blocks:** 30255–30266, 26170–26180.

Rows 101 to 107 cite only `archive.org` identifiers and the Wikipedia reference lists. I did not re-fetch the archive.org metadata. The rows license nothing, so this does not affect any claim.

**The counts.**
- *Blaurock:* `Blaurock|Blabrock|Blaurok` gives 81 occurrences in 6 files, by a Python scan and by `grep -o`. That is correct.
- *Riedemann:* 95 is correct only with a fourth spelling (N2).

**Live-commentary checker.** I ran `tools/check_live_commentary.py`'s `scan_file` on copies placed in a scratch tree as if under the world's future code folder.
- *Doc_02:* 1 REWRITE (the ISO date at line 347, N1) and 2 PROTECTED.
- *Registry:* 107 KEEP (the Added-column dates in the table) and 1 PROTECTED.
- *Ledger:* 22 PROTECTED.
- There is no ROUTE hit.

## New findings

All are COSMETIC.

**N1. ISO date in Doc_02 prose.** Line 347 reads "**Date:** 2026-10-23." The checker classes it REWRITE (iso-date). Write the date as "23 October 2026", as the Tridentine revision did.

**N2. The Riedemann spelling set does not match the count.** Doc_02 §2 (line 77) says "95 times in five files, under three spellings ('Rideman', 'Ridemann' and 'Riedemann')". §9 Terms (line 339) and Results (line 349) name the same three spellings. Counted with exactly those three (`Riedemann|Ridemann|Rideman`, Python and `grep -o` agreeing), the total is 90: Wolkan 57, Beck 23. The figure 95 (Wolkan 58, Beck 27) is reached only by adding "Riedeman" (Wolkan 1, Beck 4), which row 100 mentions for the Chronicle. Name "Riedeman" in the spelling list wherever the 95 is stated. Beck's single "Riedmann" is outside both counts. Say so, or leave it out explicitly.

**N3. Row 49: line 1705 concerns the Montanists, not the Donatists.** The revised note says "line 1705 contrasts the Donatists with the Münster movement". Ribbeck lines 1700–1706 are about Montanus and his followers at Pepuza: "Dabei aber bewiesen sie sich nicht, wie die Münsterschen Wiedertäufer". Correct the name. The Excluded status is unaffected.

**N4. Process narration in Doc_02 §9.** Line 349 ends "the first run of this count did that (37 and 66)". The history of a corrected count belongs in the ledger (OG-20 already carries it) or in the build log, not in the document. Delete the clause.

**N5. The PRESS question is quoted incompletely.** Doc_02 §9 quotes it as "Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold." The Framework's verbatim question continues "If you can name none, say so explicitly." Quote it whole, or mark the cut.

**N6. Row 19 does not carry the Middelburg loci.** Doc_02 §6 and §8 cite "row 19" for the three acts of the House of Orange. Row 19's Verification Note still names only Menno's death (line 64106) and is marked Revision 1. Add the three loci (147918–148005, 148155–148215, 152765–152809) and the Remark (148227–148239) to row 19, or give the acts a row of their own. The checkpoint rule is met, since row 19 covers the remainder of the *Mirror*. Only the locus is missing.

**N7. Ruth is in the instrument after all.** OG-21 says Ruth's *Conrad Grebel, Son of Zurich* "does not appear in the reference lists of the Wikipedia article as read on 23 October, so it has no row". The reviewer's Round 1 fetch of the same article, the References part from character 100,000 onward on 23 October, listed "Ruth, John L. (1975). *Conrad Grebel, Son of Zurich*". The drafter should re-read that part of the page. If the entry is there, row it at C as a consultation lead (in copyright) and correct OG-21. If the page has changed, say so.

## Escalation-category check

- **Representative identity or title:** none.
- **Portfolio or cross-world:** none new. The sibling and pair question is left to the Library and the lead (line 392, OG-13, OG-14).
- **Governance or methodology:** none.
- **Unresolved tension:** none. This document clears in Round 2.

For the project lead, already routed and not decided here: OG-8 (census wording), OG-9 (regional boundary), OG-10 (Step 0 change order), OG-18 and OG-19 (possible Doc_01 change orders), and OG-20 (Doc_01 §7 item 2, the named voices).

Disposition: (left for the drafter)
