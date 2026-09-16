# Source Registry — Independent Review, Round 3

**Reviewed document:** `cappadocian_Source_Registry.md`, third pass (116 rows, revised from Round 2's 112), 2026-08-31.
**Reviewer:** independent Opus-tier agent, fresh context, no prior involvement in drafting.
**Method:** read the Registry in full, the governing template, `cappadocian_Doc_02_Source_Ecology.md`, `cappadocian_Doc_01_World_Identification.md`, `cic/texts/README.md`, and `CAPPADOCIAN_BUILD_LEDGER.md` §9. Independently re-derived the full cross-reference check (118 reference clusters, 165 resolved targets) rather than trusting the revision's claim to have done so.

This file is the review's verbatim output, preserved as the actual review artifact per this project's build-cycle discipline. Row numbers below refer to the 116-row numbering in effect at the time of this review. Two of this review's findings (the §1.5 heading's Macrina cross-reference, and row 82's false "within npnf205" claim) were fixed directly after this review as cosmetic corrections — see the Registry's own living-document log, fourth entry, for the disposition.

---

## Verdict

**The claim does not hold.** The document's closing statement — *"every 'row N' and 'rows N–M' cross-reference in the document was checked by directly reading the target row's own content, not by confirming the number merely exists"* — is false for a third consecutive round. I re-derived it independently (118 reference clusters, 165 resolved targets, each read against its target row's Source field and surrounding sentence) and found **two defects**, one of them newly created by this round's own edits.

Everything else I checked holds. The findings below are narrow and mechanical, as a third round should be.

---

## Finding 1 — a wrong cross-reference introduced by this round's own edit (blocking)

`cappadocian_Source_Registry.md` line 107, the Part B §1.5 section heading:

&gt; `### The opponents (§1.5) — Macrina the Younger herself is covered under Gregory of Nyssa above (rows 48, 56), since her only evidentiary basis is his literary works`

**Row 56 is "Evagrius Ponticus' formation and ordination by this circle."** It has nothing to do with Macrina. The correct pair is **rows 48 and 49** — the *Life of St. Macrina* and *On the Soul and Resurrection*, which are exactly the "two literary works" Doc_02 §1.4 names as everything we have of Macrina. Row 49 is even described in-document as "staged at the same deathbed as the Vita."

This is not a survival from an earlier draft. `git diff 0e3a88de 978185d2` shows the old heading was plain — `### Macrina the Younger and the opponents (§1.4, §1.5)`, carrying no cross-reference at all. The third revision rewrote the heading and *added* the wrong reference. The likely mechanism is visible in the diff: row 56 is the last table row immediately above this heading, so "56" was picked up from adjacent context rather than from reading a target row. That is precisely the failure mode the claim asserts was eliminated — and it was committed in the same commit as the assertion.

It is also a `rows N, M` form sitting in a section heading rather than a table cell, i.e. in the residual category prior rounds under-swept.

## Finding 2 — a cross-reference whose target contradicts the claim it is cited for (blocking)

Row 82 (line 157), *In XL Martyres* II:

&gt; `Within npnf205 (row 41), not independently re-checked against this specific homily's text this session.`

Resolving row 41 by content shows it says the opposite. Row 41 (line 90) now reads: npnf205 "Does NOT include … **the Forty Martyrs/Theodore the Recruit homilies (row 53)** — confirmed absent per the G1 manifest's own audit." Row 53 (line 102) agrees: "Confirmed absent from the vendored npnf205." *In XL Martyres* II **is** one of Nyssen's homilies on the Forty — Doc_02 §3 groups them explicitly ("Nyssen on the Forty and on Theodore the Recruit" … "*In XL Martyres* II").

I verified this against the vendored file rather than resting on the rows: `/home/user/CIC-Project/cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt` (3.5 MB) yields **zero** occurrences of "Forty Martyrs" or "XL Martyres". The only hit for "Forty" in a martyr context is line 588, inside the NPNF editor's *Prolegomena* — a biographical retelling of Emmelia's ceremony at Annesi, not Gregory's homily.

This round caused the collision and missed it: it edited row 41 (adding the Forty Martyrs homilies to the absent list, correcting four wrong targets in that one cell) **and** edited row 82 (§6.3 → §6.1, plus the new row-113 pointer) in the same pass, without reconciling them. Consequences: rows 82 and 53 now directly contradict each other; row 82's Confidence B rests on a false locational claim ("Within npnf205") rather than on the "specific work named" ground the template actually supplies; and row 113 ("attested via row 48… Row 82's *In XL Martyres* II citation") inherits the chain.

---

## Secondary items (minor, non-blocking, listed for completeness)

- **Part G intro (line 209):** "Three of these close completeness gaps the second independent review found in Doc_02 **§4/§6**." Rows 113 and 115 are §4; **row 114 is §2** — "Gregory Nazianzen's oration on baptism" appears only at Doc_02 §2 (line 59), as row 114's own note correctly says. §6 belongs to row 116, described separately as "the fourth." Should read §2/§4.
- **Part C note (line 149) and Part H bullet (line 226):** "Valens' pressure on Nyssa and the 372 provincial division are attested via rows 5 and 62." Row 62's own Licensed For covers only Constantinople 360, the Homoian reconstruction, and the Julian episode; Doc_02 §2 attributes the 372 division to "the letters and orations," not the church historians.
- **Part H first bullet (line 224):** "conciliar documents, rows 77–79" — row 79 is CTh 16.1.3, an imperial law, not a conciliar document. Rows 77–78 are the conciliar ones.
- **Type-axis inconsistency:** row 56 states the principle "no primary text of his own to be Type P about" and takes S; row 74 (Julian's measures against Caesarea) is a bare event with no named text and is still P.
- **Doc_02 §8 completeness:** "Nyssen's own note of return joy at work level" supports a Tier 1 story candidate but no row licenses it (rows 41/55 cover Nyssa's letters for other targets). Outside the Registry's own stated §§1–6 scope, so not a broken claim — the only §7/§8 item I found unlicensed.

## What held up (verified, not assumed)

- **Row numbering:** 116 IDs, strictly sequential 1–116, no gaps, no duplicates.
- **Table integrity:** all 116 data rows carry exactly 11 pipes / 10 columns; all 11 table blocks are contiguous line-runs with header + delimiter. Row 71's Loeb pagination is now "pp. 245–293" with no stray pipes; no orphaning blank lines remain, including at row 81.
- **All 163 other resolved cross-reference targets** are correct on content, including every reference the log says was fixed this round (row 41's four-in-one-cell repair, rows 6/12, 16, 32, 44/45, 79, 81).
- **A/B discipline:** Confidence-A rows are exactly `[18, 21, 22, 33, 48, 57, 63, 71, 72]` — an exact match to the preamble's list. Each A-row's verification note checks out against `cic/texts/README.md` and ledger §9 (footnote counts, chapter ranges, colophons, the Padelford translator caveat).
- **Tier calibration:** rows 3, 24, 29, 30, 52, 53, 61, 74, 80, 84, 101, 107, 110, 111 are all now correct against the template's literal C ("tied to a real author/work") vs. D ("no specific text/author named") vs. B ("specific work/locus named") definitions. Named-author-only rows are C; rows 74 and 84 with no named author or text are D; acquisition status is no longer used as a downgrade anywhere. No row rests at E; no Native row lacks a Licensed For; no row has an empty Verification Note; every Named Comparandum has a Comparandum Note.
- **Boundary axis:** the six Excluded rows are correctly reasoned (row 64's Named Comparandum over Out-of-Boundary, row 116's temporal Out-of-Boundary, row 3 following Doc_01 §2). Part F remains entirely Native; nothing is Excluded for being copyrighted or unvendored.
- **Rows 113–116** are accurate against Doc_02 §4, §2, §4, §6.6 respectively, with verbatim quotations I checked against the source text. Row 24's "Bronwen/Mark DelCogliano" → "Mark DelCogliano" is a correct fix.

## Recommendation

Not clearable [as of the state reviewed]. Two targeted edits close it: line 107 `(rows 48, 56)` → `(rows 48, 49)`, and row 82's "Within npnf205 (row 41)" → an accurate statement that the homily is confirmed absent from npnf205 (per rows 41/53) and is a named acquisition gap, with its B tier re-grounded on "specific named work" rather than on containment.

Per this project's own discipline, the inaccurate self-verification claim in the third revision's log is a defect in its own right and should be corrected in the log alongside the two fixes — the log's own closing sentence ("each round's own self-audit has missed something the next round found") is now true of three rounds running, and the honest move is to stop asserting exhaustiveness rather than to assert it a fourth time.
