# Doc_08 (Forces Document) — Round 2 Independent Adversarial Re-Review
## The Reformed Cities — Zurich & Geneva

**Reviewed:** `Doc_08_Forces_Document.md` (Revision 2), plus `Open_Gaps_Tracking.md` item 25 and `rzg_Decision_Log.md`'s Doc_08 entry for accuracy against the live text.
**Scope:** targeted recheck against `Doc08_Round1_Review.md`'s eight findings, per this project's own Round-2+ cost discipline — not a full re-review from scratch. Every claim below was independently re-verified directly against the document's own text (`grep -n`/direct counting of Section 3 headers and Force Index rows) and against `Doc_04_Gravity_Discovery.md` and `Doc_05_Ecological_Reconstruction.md` directly (line-exact comparison via `sed`/`grep`), not accepted on Doc_08's own revision note or on `Open_Gaps_Tracking.md` item 25's own account of the fixes. The six-cell matrix's own cell assignments elsewhere, the two independently-verified quotations, the Transmission sections, the Forces-and-Gravities Synthesis's other gravity entries, the governing-principles self-checks other than From-Within, and the Donatism comparison claims were not re-reviewed — Round 1 already confirmed these and Revision 2 did not touch them.

---

## Verdict: **Clear, with two narrow gaps found and corrected directly as cosmetic fixes**

All three High findings are genuinely fixed at the root, not patched over. The force count is corrected to nineteen everywhere, independently re-counted directly against Section 3's own `#### Force` headers and the Force Index's own row count; the Proportionality Principle's own rewritten arithmetic (fourteen connected, five cross-cutting, 14+5=19) checks out exactly against an independent count of the Force Index's own "Connected Gravities" column. All five From-Within inline citations are genuinely moved into header form outside inhabited prose, and Section 8's own status paragraph now honestly discloses the violation found and fixed rather than falsely claiming a clean check. G1's connection to Force 1B-1 is genuinely removed from every location it previously appeared (Section 5, the Force Index, the inverted "By Connected Gravity" table) — a broad `grep` for every "G1"/"1B-1" co-occurrence in the document found no surviving or newly-introduced recurrence of the exact error this world's build has now checked for three times running. All three Medium findings and both Low/cosmetic findings are also genuinely fixed, each independently re-verified below.

The recheck found two further, narrow gaps — neither a factual error, neither reopening any of Round 1's three High findings — which are applied directly as cosmetic fixes below, per this world's own established Round-2+ precedent (`Open_Gaps_Tracking.md` items 22–24, Doc06/Doc07 Round 2) for exactly this situation: **(1)** Finding 1's own specifically-named completeness fix ("Add explicit prose confidence statements for Force 2A-4 and Force 2A-5 to Section 7") was not applied in Revision 2 — both forces remained absent from Section 7's prose despite carrying confidence levels in the Force Index; **(2)** Finding 3's fix left the document's own self-description slightly ahead of its own text — Section 5's Cross-Strand Gravity Note claims the Zwingli 1527 election-exposition material is "named at Force 1A-2's own entry," but Force 1A-2's own Section 3 entry (Layers 1–3) did not, in fact, mention it anywhere; it was named only in Section 5's own G1 gravity-connections list. No further review round required.

---

## Finding-by-Finding

### Finding 1 — HIGH — Wrong force count (seventeen vs. nineteen) and Proportionality Principle math — **Genuinely fixed, with one named completeness sub-fix missed**

Independently counted Section 3's own `#### Force` headers directly: Cell 1A (1A-1, 1A-2 — 2), Cell 1B (1B-1, 1B-2, 1B-3 — 3), Cell 2A (2A-1–2A-5 — 5), Cell 2B (2B-1–2B-6 — 6), Cell 3A (3A-1 — 1), Cell 3B (3B-1, 3B-2 — 2) = **19**, matching the Force Index's own 19 rows one-for-one. "Seventeen" no longer appears anywhere in the document except inside the masthead's own historical account of what Round 1 found (an accurate description of the past, not a current claim) — checked with a full-document `grep` for both "seventeen" and the bare numeral "17," neither of which survives as a live claim.

The Proportionality Principle's own rewritten second sentence was independently checked against the Force Index's own "Connected Gravities" column, counted row by row: 14 rows carry a real gravity (1A-1, 1A-2, 1B-1, 1B-2, 1B-3, 2A-1, 2A-3, 2A-5, 2B-1, 2B-2, 2B-3, 2B-4, 2B-5, 3B-1) and 5 carry an em-dash/cross-cutting notation (2A-2, 2A-4, 2B-6, 3A-1, 3B-2) — exactly matching the document's own "fourteen... five" claim, and 14+5=19 checks out against the total. The document's own split of the five cross-cutting forces into "two required Transmission entries (2B-6, 3B-2)" plus "three others, each with a stated reason" (2A-2 grounds a downstream force; 2A-4 sustains a lens rather than a gravity; 3A-1 is an honest absence-of-ending finding) is independently confirmed accurate and reasoned, not merely asserted.

**One gap: Round 1's own named completeness sub-fix was not applied.** Round 1 Finding 1 additionally required: "Add explicit prose confidence statements for Force 2A-4 and Force 2A-5 to Section 7." Checked directly: Section 7's "Forces at Documented or Widely Accepted Level" paragraph still named only 14 forces plus separate treatment for Force 1B-3 and Force 2B-6 (16 total) — Force 2A-4 and Force 2A-5 remained entirely absent from Section 7's prose, though both carry confidence levels in the Force Index (2A-4: "Documented, not independently assessed beyond Doc_01 §7's own characterization"; 2A-5: "Documented (scope); historiographical, not vendor-verified (delegate specifics)"). A full-document `grep` confirmed neither "2A-4" nor "2A-5" occurs anywhere between the Section 7 and Section 8 headers before this recheck's own fix.

**Applied directly as a cosmetic fix:** added a sentence to Section 7's "Forces at Documented or Widely Accepted Level" paragraph stating Force 2A-4's and Force 2A-5's own confidence levels in prose, restating (not changing) the confidence levels the Force Index already carries.

### Finding 2 — HIGH — From-Within Principle violated by five inline citations — **Genuinely fixed**

All five previously-flagged entries were checked directly. Force 1B-1 (line 81), Force 1B-2 (line 91), Force 1B-3 (line 101), Force 2A-1 (line 117), and Force 2B-5 (line 215) each now carry their own citation in a `*[Inhabited — ...]*` bracketed header immediately before the passage, with no inline citation surviving inside the inhabited prose of any of the five — independently confirmed by reading each passage in full, not merely checking for the header's presence. A `git diff` against the pre-Revision-2 text confirms each fix removed the parenthetical from mid-sentence and relocated it to a header, changing no other substantive content in four of the five (Force 1B-3's own additional content change is Finding 4, below). Section 8's own From-Within status paragraph now reads: "A full re-read of every Layer 2 entry before disposition found five entries (Force 1B-1, Force 1B-2, Force 1B-3, Force 2A-1, Force 2B-5) embedding their own source citation inline... All five are corrected in this revision" — an honest disclosure of the violation found and fixed, not the false "confirmed... no... inline citation survives" claim Round 1 flagged.

### Finding 3 — HIGH — G1 wrongly reconnected to Force 1B-1 — **Genuinely fixed, with one imprecise self-description found and corrected**

A full-document `grep` for every "G1" and "1B-1" occurrence found no remaining or newly-introduced co-occurrence connecting the two. Section 5's own G1 entry no longer lists 1B-1 as a connected force (only 1A-2, 2B-3, 2B-5, 2B-6, 2A-5 remain). The Force Index's own 1B-1 row now reads "Connected Gravities: G2, G3, T1, T2" — G1 removed. The inverted "By Connected Gravity" table's G1 row now reads "1A-2, 2A-5, 2B-3, 2B-5, 2B-6" — 1B-1 removed. Doc_04 §3.1's own Forces-connection statement for G1 (checked directly: "Cell 1A... Cell 2B... No Ending/Transforming force is attested") confirms Cell 1B is genuinely absent from G1's own governing entry, matching the fix.

**One imprecision found in the document's own self-description.** Section 5's Cross-Strand Gravity Note states the Zwingli 1527 election-exposition material is "named at Force 1A-2's own entry" — but, checked directly, Force 1A-2's own Section 3 entry (Layers 1–3, lines 61–68) made no mention of the 1527 exposition anywhere; it was named only in Section 5's own G1 gravity-connections list (the "1A-2" bullet), not inside Force 1A-2's own entry in Section 3. This is not a fabrication or a reopening of the G1/Cell-1B error — the substantive fix (G1 no longer connects to 1B-1 anywhere) is genuine and complete — but it is the same category of small self-description overstatement this document has now been caught on multiple times: a claim about where something is "named" that, checked directly, is not quite accurate. `Open_Gaps_Tracking.md` item 25 and `rzg_Decision_Log.md`'s Doc_08 entry both repeat this same phrasing ("re-cited... at Force 1A-2's own entry"), consistent with the document's own account rather than independently wrong.

**Applied directly as a cosmetic fix:** added a sentence to Force 1A-2's own Layer 3 (Formation Impact) naming the 1527 exposition's corroborating role there directly, making the existing claim in Section 5 and the Cross-Strand Gravity Note accurate rather than softening those claims instead. This is a root-cause fix (the material is now actually named at Force 1A-2's own entry, as claimed) rather than a wording patch.

### Finding 4 — MEDIUM — Force 1B-3's mislabeled, spliced quote — **Genuinely fixed**

Checked directly against `Doc_05_Ecological_Reconstruction.md` §4: the actual passage reads "The magistrate governs bodies and property; he does not sit in judgment on whether a soul may come to the Lord's own table. When the council's own men tried to claim that authority for themselves, the Consistory did not yield it — not because the pastors sought power for its own sake, but because a discipline answerable to the city's own shifting politics is no discipline at all." Doc_08's Force 1B-3 Layer 2 now quotes only the opening sentence, verbatim, under a header disclosing exactly this split: "*[Inhabited — the opening sentence carried from Doc_05 §4; the fuller passage, including its own middle sentence on the council's later challenge, belongs to Force 2B-4 below, where it is quoted in full]*" — and Force 2B-4's own Layer 2 does in fact carry the remainder verbatim ("When the council's own men tried to claim that authority for themselves..."), confirmed unchanged and already correctly attributed before this revision. No content is duplicated between the two forces, and neither carries a "carried directly" label anymore. The interpretive clause Round 1 flagged as invented and uncited ("which is why this body had to be its own thing from the start... not an arm of the council that had ratified the Sixty-Seven Articles at Zurich") now sits in Force 1B-3's own Layer 3 (Formation Impact) rather than inside quoted Layer 2 prose — appropriate, since Layer 3 is this document's own analytical layer, not inhabited voice requiring a source citation. Checked for redundancy with Force 1B-3's own pre-existing Layer 3 text: the relocated clause overlaps modestly in sense with the adjacent "an independence claim built into the institution from its own origin, not asserted later" (both describe the Consistory's built-in independence), but adds the specific comparative reasoning (not an arm of the council) rather than simply repeating the same words — a minor stylistic overlap, not a substantive or citation defect, and not corrected here as it states nothing false.

### Finding 5 — MEDIUM — False "mirror" illustrative phrase in Section 8 — **Genuinely fixed**

The "mirror" phrase is gone from Section 8's From-Within paragraph. Each of the three replacement phrases was checked directly against Section 3: "the sign not disjoined from the thing it signifies" is the same paraphrase of Force 2B-2's Layer 2 ("We do not divide the sign from the thing it signifies...") that Round 1 already confirmed clean and left untouched; "the bread that is bread while the body is in heaven" is a near-verbatim match of Force 2A-1's own Layer 2, which reads exactly "The bread is bread, and the body is in heaven..."; "the magistrate's sword for the body and the pastor's censure for the soul" is a fair paraphrase of Force 1B-2's own Layer 2 ("...not the magistrate, whose sword is for the body, but pastors and elders together, whose office is to unite in pronouncing censure..." — verified verbatim against Doc_05 §1, which Force 1B-2 quotes exactly). All three phrases now genuinely appear in Section 3.

### Finding 6 — MEDIUM — Force Index 1B-1 row missing Connection 1 — **Genuinely fixed**

The Force Index's 1B-1 row now reads "→ 2B-2 (Connection 1, jointly with 1B-2); → 2B-1 (Connection 2); → 2A-1 (Connection 3)" — Connection 1 added, matching Section 4's own prose and the already-correct 1B-2 and 2B-2 rows exactly.

### Finding 7 — LOW/COSMETIC — Connection 8 causal-arrow overstatement — **Genuinely fixed**

Connection 8 is now explicitly labeled "(a named contrast, not a produces/reshapes relationship — the arrow notation used for Connections 1–7 above does not fit this one, and is deliberately not used here)" and uses "↔" instead of "→". Matches Round 1's suggested framing exactly.

### Finding 8 — LOW/COSMETIC — Force 1B-1's smaller mislabel issue — **Genuinely fixed**

Checked directly against `Doc_05_Ecological_Reconstruction.md` §1: the Zurich passage reads, verbatim, "Scripture read continuously, book by book, not cut into a fixed year's own lectionary — that was the discipline Zwingli set for himself at the Grossmünster from his first January, and it is the discipline that made every later argument possible: whatever the text does not say, the church may not require." Doc_08's Force 1B-1 Layer 2 first sentence now matches this exactly, word for word, with "at the Grossmünster" restored. The header now discloses the two-source composite directly: "*[Inhabited — the first sentence carried from Doc_05 §1, the second from Doc_05 §5's own parallel Zurich passage]*" — and the second sentence is confirmed a fair paraphrase of Doc_05 §5's own Zurich passage ("...argued in public, before the city, not asserted from a chair"), not an unsupported invention.

---

## Newly Found Gaps — applied as direct cosmetic fixes per `cic-build-cycle`'s own rule, no further review round required

This recheck specifically searched for fresh defects introduced by the Round 1 fixes themselves (per this world's demonstrated pattern of a Round 1 fix introducing a fresh Round 2 defect, e.g. Doc_06 Round 2). Two were found, both already detailed above under Findings 1 and 3, both narrow and non-substantive:

1. **Section 7 missing prose confidence statements for Force 2A-4 and Force 2A-5** (Finding 1's own named sub-fix, not applied in Revision 2). **Fixed directly**: a sentence added to Section 7 stating both forces' own confidence levels in prose, matching the Force Index exactly.
2. **Section 5's Cross-Strand Gravity Note claim that the 1527 material is "named at Force 1A-2's own entry," which was not, in fact, true of Force 1A-2's own Section 3 entry** (an artifact of Finding 3's own fix). **Fixed directly**: a sentence added to Force 1A-2's own Layer 3 naming the corroboration there, making the existing claim accurate at its root rather than softening the claim elsewhere.

Neither is a factual, historical, or citation-fidelity error; neither reopens any High finding. No new instance of the G1/Force 1B-1 recurrence was found anywhere in the document. Force 1B-3's Layer 3 redundancy noted under Finding 4 is stylistic only and was not corrected, since it states nothing false and correcting it risks exactly the "fix on a fix" pattern this project's own discipline warns against for content that isn't actually wrong.

**Proportionality Principle's own arithmetic re-verified independently:** 14 (connected) + 5 (cross-cutting) = 19 (total) — confirmed by an independent row-by-row count of the Force Index's own "Connected Gravities" column, not accepted on the document's own restated sum.

**No lingering "seventeen," in word or numeral form, found anywhere** in a full-document search — the only two occurrences of "seventeen" that could be found are inside the masthead's own historical account of what Round 1 found, which accurately describes the past rather than making a current claim.

---

## `Open_Gaps_Tracking.md` item 25 and `rzg_Decision_Log.md`'s Doc_08 entry — checked for accuracy

Both accurately describe what Round 1 found and what Revision 2 actually contains, independently cross-checked against the live Doc_08 text and `Doc08_Round1_Review.md`:

- Both correctly state no regression on the two previously-flagged clean quotations and the six-file "Wherefore" fix — independently re-confirmed above (both quotations still exact; "seventeen" does not recur as a live claim).
- Both correctly and specifically describe all three High, all three Medium, and both Low findings, matching `Doc08_Round1_Review.md` verbatim in substance.
- Both correctly describe the fixes actually present in Revision 2 for all eight findings — matching what is independently verified above, including the same "re-cited... at Force 1A-2's own entry" phrasing this recheck found to be imprecise against Doc_08's own then-current text (now corrected directly, per above, rather than requiring these two records to be revised).
- **Both correctly avoid claiming a disposition.** Item 25 ends "Round 2 targeted recheck pending," not "Approved to proceed" — accurate, since this recheck had not yet occurred when item 25 was written. The Decision Log's Doc_08 entry likewise ends "Round 2 targeted recheck: pending." Both are updated below to record this recheck's own result and disposition, following the same in-place-extension pattern already used for Doc_04, Doc_05, Doc_06, and Doc_07's own entries (number/date unchanged, content only added).

---

## What checked clean (re-confirmed, not re-litigated)

- No regression on either of the two previously re-verified quotations (the Consensus Tigurinus 9th Head, the Institutes IV.3.8 passage) or on the six-file "Wherefore" fix from Doc_07 Round 1 — none of these was touched by Revision 2, and none shows any sign of drift.
- Cell 1B's own three-force assignment (Force 1B-1, Force 1B-2, Force 1B-3) is unchanged and still matches Doc_05 §11's corrected handoff exactly.
- Both required Transmission entries (Force 2B-6, Force 3B-2) are unchanged and still substantive, not perfunctory.
- The Donatism comparison claims, the six-cell matrix's other cell assignments, and the Forces-and-Gravities Synthesis's other gravity entries are unchanged from Round 1's own independently-verified text.
- All six cells remain populated; all six classified gravities still connect to at least one force with no empty row, independently re-confirmed against the corrected inverted table.

---

## Summary

All three High findings, all three Medium findings, and both Low/cosmetic findings from Round 1 are genuinely fixed at the root, independently re-verified against the document's own text and against Doc_04/Doc_05 directly rather than accepted on Doc_08's own revision note. The force count is exactly nineteen everywhere it is stated, the Proportionality Principle's own arithmetic is correct, all five inline citations are now in header form with an honest From-Within disclosure, and G1 no longer connects to Force 1B-1 anywhere in the document. Two narrow gaps were found on the specific "did a fix introduce a fresh defect" check this recheck ran: Section 7's own missing prose confidence statements for Force 2A-4/2A-5 (a named Round 1 sub-fix that Revision 2 missed), and an overstated self-description of where the relocated 1527 corroboration is "named." Both are narrow, non-substantive, and corrected directly as cosmetic fixes, per this world's own established precedent — no further review round required.

**Escalation categories:** none apply. This is ordinary self-certification-accuracy and cell-placement-precision recheck work — no Representative identity/title/voice question, no cross-world/portfolio-level decision, no governance/methodology change, and no unresolved tension the pipeline itself cannot close.

**Disposition: Approved to proceed.**
