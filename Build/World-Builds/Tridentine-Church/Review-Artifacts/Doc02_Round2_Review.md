Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: Opus Round 2 reviewer, Tridentine (targeted recheck)
Drafter agent: addc920a5d1ee7b8a (Sonnet)
Round: 2
Truncation check, method 1: wc -l on the three Revision 2 files: Doc_02 431 lines, its last heading "## 11. Disposition" (line 427) followed by "*End Doc_02.*"; Source_Registry 208 lines, ending in the saturation statement "(rows 91, 92, 93, 94)."; Open_Gaps_Tracking 228 lines, last entry OG-22. Each file ends in a complete sentence and a newline (tail -c).
Truncation check, method 2: independent parse in Python of the Registry table: 114 data rows numbered 1 to 114, with counts Native 99, Excluded 15 (Named Comparandum 6, Out-of-Boundary 9), Confidence A 36, B 39, C 35, D 4, matching the header line; diff of each file against the Round 1 copy kept in scratch shows only the revised passages, and every change ends on a complete line; Open_Gaps holds 22 "## OG-" headings in order.

# Review of Doc_02_Source_Ecology.md and Source_Registry.md (The Tridentine Church)

Also rechecked: `Open_Gaps_Tracking.md`. Scope: the Round 1 findings and the Revision 2 diff only, at lower effort. Every quotation that was added or changed was checked against its cited line in `cic/texts`.

## Verdict

**Cleared.** All nine Round 1 blocking findings are resolved. Eleven of the twelve cosmetic findings are resolved, and one is mostly resolved. There are two new cosmetic findings and no new blocking finding. Nothing that remains changes a claim, a confidence rating, a sourcing conclusion or a scope boundary.

## Quotations added or changed in Revision 2

I checked eight new quotations at their cited lines under the Round 1 normalisation rule. All match:

- Waterworth "The Cardinal of Lorraine. To the most blessed Pius, Pope, and our lord" (lines 24035–24036).
- The Catechism "SECOND REVISED EDITION" (line 72), "SIXTH PRINTING, SEPTEMBER, 1937" (line 73) and "DIE 3 JANUARII, 1923" (line 107).
- The Bullarium "Dar. P. A. c. die 25. Febr." (lines 85574–85575).
- Pius V "die vit. Octobris, M. p. 1xv11. Pontificatus noftri anno fecundo" (lines 1999–2001).
- Giussano "OF THE VIRTUE OF FAITH IN ST. CHARLES." (line 10888).

The Reformed cities' Step 0 sentence quoted in §3 item 12 matches its source word for word. Its quotation marks are cosmetic finding N1. The four Doc_01 phrases quoted in OG-21 and §7 item 16 match Doc_01: "chiefly through a hostile 1681 Anglican polemical reprinting (Barlow)", "by devotional material only", "have no vendored source" and "McHugh & Callan, 1923 English translation".

The new life-date sources in the §2 lead-in check out. The Creator lines give Bellarmine 1542–1621, Granada 1504–1588, Pole 1500–1558 and Pius V 1504–1572. Giussano vol. I gives Borromeo's birth in 1538 and death in 1584 (lines 245, 248). In the Giussano vol. II contents, Book IX is "OF THE MIRACLES" (line 414), as §4 now says.

## Round 1 findings

### Blocking

1. **Resolved. The Borromeo voice question.**
   - Rows 29 to 33 are now Native, held as context and not licensed for this world's Representative, with "world ownership pending" and no ownership sentence.
   - §1 (table and bullets), §6 items 5 and forces, and §7 items 5 and 15 now say the same thing.
   - OG-4 cites the "six decisions" entry and the Tatian co-ownership entry, and states what each possible ruling would do to the rows.
   - §11 names the cross-world question as routed, not decided.
2. **Resolved. The Catechism edition and its rights.**
   - Rows 10 and 11, §1, §2, §3 and §7 items 9 and 16 state the second revised edition (copyright 1934, sixth printing 1937) and cite lines 72, 73, 107 and 110.
   - OG-20 asks the Library for a renewal check and a corrected header. The rows are "used, pending the rights check".
3. **Resolved. The Goa letter's date.** Row 16 now gives the heading at line 1873 and the letter's own dating clause at lines 1999–2001, with the year stated as garbled. It also says the line-1869 date belongs to the previous letter.
4. **Resolved. Giussano's book of the virtues.** Row 35 and §4 now give Book VIII, the contents entries at lines 338 and 341, the body heading at line 10888, and Book VII as narrative (line 275).
5. **Resolved. Lorraine's acclamations.** §3 item 4 and the §8 table now split the claim. That he led them is Documented from the decrees, which name him as speaker. That he composed them is "Documented as the editor's statement and as Sarpi's, from opposite sides". The table says that the decrees do not state it.
6. **Resolved. The three confidence tags.**
   - (a) The Contested tag is withdrawn, and Doc_01's Widely Accepted and Inferential-Thin stand.
   - (b) The Massarelli attribution is now stated as an absence, not a level.
   - (c) The Carranza row now reads "Documented as Sarpi's statement, from one hostile witness". It places the approval with the Index deputies and their Congregation, and §4 says the same.
7. **Resolved. The Reformed cities' Step 0.** §3 item 12 and §7 item 6 now say that it names the Tridentine Church twice in §3 B3, the second time as a direct doctrinal rival.
8. **Resolved. The Schaff and Reusch quotability flags.**
   - The file table now flags Schaff "split by part" (Latin second witness, English verbatim-ready) and Reusch "second witness only (whole file)".
   - Row 6 and row 20 match the table. Doc_02 §1 matches too, and says the 8,306,934 figure is an upper bound.
9. **Resolved. The overtaken Doc_01 statements.** §7 item 16 and the new OG-21 list four Doc_01 statements as change-order candidates, each with the row that overtakes it. Doc_01 is not edited.

### Cosmetic

1. **Mostly resolved. ISO dates and route cues.** Every ISO-date line in Doc_02 and in Registry line 204 is gone. In prose, dates are now written as months and the decision-log entries are cited by title. Re-running the checker's `scan_file` on copies placed as if under `Build/worlds/<code>/` gives one remaining hit in each file: Doc_02 has 0 REWRITE and 1 ROUTE, and the Registry has 1 ROUTE. Both are the route cue "still pending", and the next item lists them. Open_Gaps stays protected.
2. **Resolved. The day of *Regnans*.** §3 item 3, row 13 and the §8 table now cite the margin note and say that it may belong to another constitution on the page.
3. **Resolved. The single-mark convention.** It is now declared in Doc_02's header note on quotations.
4. **Resolved. The Python counting method.** §1 now says the files are decoded from raw bytes.
5. **Resolved. The tag's spelling.** "Inferential/Thin" no longer appears.
6. **Resolved. Builder-memory dates and claims.**
   - The §2 lead-in now sources each heading's dates, and tags Pius V's reign as builder knowledge.
   - "The Acta were later adopted widely" is replaced by "not tested on this shelf".
   - Row 50 no longer gives a 1620 date.
7. **Resolved. Four Lives or five.** §2 and §6 now count Peña's work as a canonisation summary, and §4 says it is counted with the Lives for the formation narrative. The wording now explains the difference.
8. **Resolved. Row 9's exclusion reason.** Row 9 is now Out-of-Boundary, and OG-5 matches.
9. **Resolved. The Society of Jesus cross-reference.** §7 item 4 now cites `jes` Doc_02 §7 item 3 and §3 item 6.
10. **Resolved. The Early English Books list.** §7 item 9 and OG-14 now add the Hall, Foxton and 1688 tract files.
11. **Resolved. Process narration in the disposition.** §11 and OG-3 no longer narrate the Doc_01 corrections, and §11 now names the one escalation category as routed.
12. **Resolved. Quotation addresses for the handoff.** This is recorded as OG-22, for Step 2 close.

## New findings

**N1. COSMETIC: nested single marks in the Reformed cities' quotation.** Doc_02 §3 item 12. The quotation is opened and closed with single marks ('will almost certainly ... relationship to Trent'). It also contains the source's own inner quotation, which is shown with single marks too ('direct doctrinal rival'). The words are verbatim. Use double marks for the outer quotation so the nesting reads correctly.

**N2. COSMETIC: two lines still trip the live-surface route cue.** Doc_02 line 295 (§7 item 11) cites the gap ledger entry by a title that contains "still pending". Registry line 67 (row 49's Comparandum Note) says the wider re-check "is still pending (Open_Gaps)". The checker flags both as ROUTE. Rewording to "is outstanding" (or citing the entry as "Open_Gaps: Living Tradition Status, October 2026") would clear both before the world moves to `Build/worlds/<code>/`.

**Observation, not a finding.** Revision 2 rewrote several Open_Gaps entries in place (OG-1, OG-3, OG-4, OG-5, OG-10, OG-14, OG-15). The ledger has not been merged, so the append-only rule for merged entries is not engaged. After the merge, changes should go in as new numbered entries.

## Escalation-category check

- **Representative identity:** not touched.
- **Portfolio or cross-world:** yes, the ownership of Borromeo's voice (VI.12 or VI.22). It is routed to the project lead in OG-4, with the nearest records cited, and the Registry no longer decides it.
- **Governance or methodology:** none. The Catechism rights question is a Library rights check (OG-20).
- **Unresolved tension:** none. Both new findings are cosmetic.

Disposition: (left for the drafter)
