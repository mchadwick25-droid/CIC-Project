# VERDICT: REVISION REQUIRED

**Counts by severity:** 2 HIGH · 0 MEDIUM · 1 LOW · 0 COSMETIC

---

## What this review actually checked

**Scope discipline.** This is the internal-and-cross-document-consistency dimension only. I did not assess condensation loss (what the 33% cut removed) or verify quotation fidelity against primary vendored texts (whether a quoted string is transcribed correctly) — those are the other two reviewers' lanes. Where I quote a source below, it is to compare the Profile's *restatement* against the upstream document's *current status/claim*, not to re-verify the upstream quotation against Cyprian or Augustine's own text.

**Method.** I read `lpc_World_Profile.md` in full (both halves, 761 lines) before extracting anything. I then built the count/status table below by pulling every numeric claim (gravity count, force count, term count, lens count, limit count, tension count, word count) and every status/date claim (dispositions, open-item closures, escalation-category decisions) that appears more than once in the document, or that restates an upstream document's own status field. For each row I opened the cited upstream file directly (`Doc_04_Gravity_Discovery.md`, `Doc_06_Full_Lexicon_Development.md`, `Doc_07_Integrated_Ecology_Analysis.md`, `Doc_08_Forces_Document.md`, `Doc_09_Story_Inventory.md`, `Doc_02_Source_Ecology.md`, `Doc_03_Lexicon_Candidate_List.md`, `Doc_01...md`, `Source_Registry.md`, `lpc_Decision_Log.md`, `Lexicon_Deployment_Index.md`) and grepped/read the relevant section rather than trusting the Profile's paraphrase of it.

**What I swept exhaustively:**
- Every count claim in the document (gravities, forces, vocabulary terms, lenses, limits, tensions, word counts) — cross-checked against the body content that instantiates each count and against the one or two upstream documents that are each count's own source of truth (Doc_04 §4 for gravities/classifications, Doc_08 for the 17-force total and the two omitted forces, Doc_06 + `Lexicon_Deployment_Index.md` for the 7/19 and 4-of-6 vocabulary math, Doc_07 §1/§2 for the nine-lens claim).
- Doc_04 §7's numbered open-items list (all 8 items) against every place the Profile cites it (G3, G5's Confidence/Cross-strand/Brief-description/Grounding fields, Section 11 item 7).
- Doc_07 §8's "Open Items and Handoff" list (all 10 items) against the Profile's Section 11 items 2 and 7.
- Section 11's own eleven checkboxes and seven-item outstanding list against the document's own body content and against the Document Log and Disposition.
- Section 9 (Living Tradition) word-for-word against `lpc_Decision_Log.md`'s Article 29 confirmation entry and against `Living_Tradition_Distinguishing_Statement_DRAFT_2026-09-16.md` §2–§3 (its stated source).
- Section 10 (Integrative Observation) byte-for-byte against the live `Doc_07_Integrated_Ecology_Analysis.md` line the Method Note cites (line 222) — confirmed identical.
- Each of Doc_01 through Doc_09's own Disposition sections, to check the Profile's own claim about which documents were "self-disposed" versus "approved by the project lead."
- The full set of files in `Review-Artifacts/` by filename and mtime, to check whether anything the Profile's Section 11 calls "not performed" has, in fact, already run.

**What I sampled rather than exhaustively checked:**
- I did not re-verify every one of the ~90 `Doc_0n §x` citation loci in the Profile against its target section (Section 11 item 11 itself discloses this sweep has never been completed by anyone, and that is consistent with what I found — I did not attempt to close that gap myself, only to spot-check a dozen or so citations that carried a count or status claim).
- I did not check `lpc_Force_Index.md` or `lpc_Story_Index.md` against Doc_08/Doc_09 in full — I used `lpc_Force_Index.md` only for the single G1-naming cross-check the Profile itself flags.
- I did not open `Lexicon-Chunks/` or `Story-Chunks/` individually.
- I did not re-derive Doc_04's six-test verdicts or Doc_08's force-confidence ratings from primary sources; I took Doc_04/Doc_08's own current text as the standard the Profile must match, per this review's brief ("verify at source" means the immediate upstream document, not re-deriving that document's own findings from Cyprian/Augustine).

**What I did not cover at all:**
- Quotation-level fidelity (another reviewer's dimension).
- Condensation loss / whether the 33% cut dropped required content (another reviewer's dimension).
- `records/worlds.yaml`, `cic/corpus-map/`, or any file outside this world's own folder and `Review-Artifacts/`.
- The sibling Donatism build (referenced twice by the Profile for a "portfolio-level ruling" and an "already-adopted direction on scope") — I searched `lpc_Decision_Log.md` for a record of the nine-lens/M4 portfolio ruling the Method Note attributes to "the Donatism build" and did not find it under that description; I did not chase it into the Donatism world's own files, so I cannot confirm or refute that specific attribution. This is a gap, flagged rather than closed.

---

## Count / status extraction table

| # | Claim | Location(s) in Profile | Upstream / cross-check source | Agree? |
|---|---|---|---|---|
| 1 | 8 gravities (4 Primary / 3 Supporting / 1 Tensional) | Section 2 body; Section 11 item 2; closing italic line | Doc_04 §4 table (Candidates 1,2,3,6 Primary; 4,5,7 Supporting; 8 Tensional) | Yes |
| 2 | 15 of 17 forces carried; omitted = 1A-2, 1B-3 | Method Note; Section 5 header; Section 11 item 5; closing line | Doc_08 §checklist ("17 forces" total, 1A-2 and 1B-3 named as the two the Profile omits) | Yes |
| 3 | 11 vocabulary terms (7 Tier 1 + 4-of-6 Tier 2 [AS]) | Section 6 header; closing line | Doc_06 §2 ("7 Tier 1, 12 Tier 2... across nineteen terms"); `Lexicon_Deployment_Index.md` §3 (6 [AS] terms named, of which the Profile excludes *libelli* and *libellatici*/*sacrificati*) | Yes |
| 4 | 9 ecological lenses (§2A–§2I) | Method Note; Section 4 header; closing line | Doc_07's own current numbering (§2A–§2I) as the Method Note itself restates | Yes |
| 5 | 8 honest-limit domains | Method Note; Section 8 (8 entries counted); Section 11 item; closing line | Internal only (no single upstream "count" to check against; consistent within document) | Yes |
| 6 | 2 tensions | Section 7 (2 entries); closing line | Doc_04's one Tensional gravity (G8) plus Doc_05 §9.2's second named tension point | Yes |
| 7 | Word count 17,571 → 11,696 (condensing pass) | Method Note; Document Log; Section 11 item 6 | `Review-Artifacts/WorldProfile_Condensing_Pass_2026-09-16.md` ("17,571 → 11,696 words... a 33% cut") | Yes |
| 8 | Live file word count vs. the 11,696 figure | Method Note discloses the live file has since grown past 11,696 | `wc -w lpc_World_Profile.md` = 12,142 | Yes — Method Note's own disclosure matches actual growth |
| 9 | Condensing pass run by "a thread" (singular) vs. "two threads" | Method Note (line 16, singular) vs. Document Log and Section 11 item 6 (both "two threads") | `WorldProfile_Condensing_Pass_2026-09-16.md`: "**Run by:** two fresh threads, one per half" | **No — see LOW-1** |
| 10 | Doc_04 §7 Open Item 1 open-by-design; Items 6 and 8 closed 2026-09-15 | G3 Confidence field; G5 Confidence/Brief-description/Grounding fields | Doc_04 §7 items 1, 6, 8 read directly — Item 6 "CLOSED... 2026-09-15," Item 8 "CLOSED, 2026-09-15," Item 1 carried forward, not marked closed | Yes |
| 11 | G5 classification ruled Supporting by the project lead, 2026-09-14 | Section 2, G5 Gravity-type field | Doc_04 §7 items 2 and 7 ("on the project lead's ruling of 2026-09-14"; "Closed 2026-09-14... ruled Supporting") | Yes |
| 12 | G1 named two ways: "Pastoral Office as Territorial Flock-Keeping" (this doc, Doc_08, Force Index) vs. "Pastoral Office as Flock-Keeping" (Doc_04 §4) | Section 2 opening line; Section 11 item 2 | Doc_04 §4 table row 1 ("Pastoral Office as Flock-Keeping"); `lpc_Force_Index.md` line 62 and Doc_08 line 27 (both "...Territorial Flock-Keeping") | Yes — accurately disclosed, not a defect |
| 13 | Force 2B-1 connects to G2, G6 only, not G7 (family resemblance, not a force-connection) | Section 5, "recurring contest over the failed member" entry | Doc_08 Force 2B-1: "This force therefore connects to G2 and to G6 — both first-phase relations — and not to G7" | Yes |
| 14 | Doc_01–Doc_09 disposition: "Doc_01 self-disposed; Doc_02–Doc_09 approved by the project lead" | Section 1, "Required inputs" line (line 6) | Doc_02's own Status/Disposition ("self-disposed 2026-09-12, on Round 30's clearing verdict... per CO-022's own rule... self-dispositioning path"); Doc_03's own Disposition ("self-disposed to Approved to proceed, 2026-09-09") | **No — see HIGH-1** |
| 15 | Section 11 item 4: independent verification of Doc_01 §2's propagation "not performed by the thread that applied it," listed as an open (non-struck) outstanding item | Section 11, Outstanding item 4 (line 733) | `Review-Artifacts/Doc01_Correction_Propagation_Verification_2026-09-16.md`, `..._Round2_2026-09-16.md`, `..._Round3_2026-09-16.md` (three completed independent verification rounds, the last concluding "the correction can be called closed"); `lpc_Decision_Log.md` line 1766 ("a third pass closed the two HIGH findings") | **No — see HIGH-2** |
| 16 | Representative "Datus, Bishop of the Kept Flock," decided 2026-09-15, single packaged choice | Section 9, Cross-reference paragraph | `lpc_Decision_Log.md` "2026-09-15 — M1 RESOLVED: Representative identity and image" table | Yes |
| 17 | Living Tradition Status CONFIRMED 2026-09-16, flag true, statement adopted, four fields verbatim | Section 9 (all fields) | `lpc_Decision_Log.md` "2026-09-16 — Project lead's Article 29 confirmation" entry; `Living_Tradition_Distinguishing_Statement_DRAFT_2026-09-16.md` §2 | Yes — word-for-word match on divergences and contested-standing lists |
| 18 | Article 3 / gapped-formation question closed 2026-09-16, "lpc is one formation world" | Section 11 item 5 | `lpc_Decision_Log.md` "2026-09-16 — Project lead's ruling: Article 3 permits gapped formation-types" | Yes |
| 19 | Section 10 Integrative Observation copied verbatim from Doc_07 §6, re-verified at line 222 | Section 10 | Doc_07 line 222, read directly — byte-identical | Yes |
| 20 | "Seven items carried from Doc_07 §8 item 4" (3 portfolio-level + 4 governance/methodology) | Section 11 item 7 | Doc_07 §8 item 4: "three portfolio-level items... four governance/methodology items" | Yes |
| 21 | Liturgical material "never read as liturgical evidence," "the highest-value unblocked task in the build," still open | Section 11 item 2 | Doc_07 §8 item 8, same wording, still listed open there | Yes (both still open; no evidence either has since closed it) |
| 22 | Registry row 27 = Optatus of Milevis, *Against the Donatists*, writing inside the 133-year interval but native to Donatism's own territory | Section 1; Section 5 (Force, "asymmetrically attested span"); Section 8 (133-year-interval domain) | `Source_Registry.md` row 27 | Yes |
| 23 | Doc_09 §7 item 1: "the silence is a subject-matter gap, not an empty archive" | Section 1 | Doc_09 line 120: "The silence is a subject-matter gap and a build choice, not an empty archive" | Yes (Profile drops "and a build choice" — compression, not contradiction) |

---

## Findings

### HIGH-1 — The document's own "Required inputs" line misstates two of its own inputs' disposition status

**Text A (the Profile, line 6):** *"**Required inputs:** Doc_01–Doc_09 are all **Approved to proceed** (Doc_01 self-disposed; Doc_02–Doc_09 approved by the project lead, several with findings or escalation categories carried open)."*

**Text B (`Doc_02_Source_Ecology.md`, line 3, its own Status field):** *"**Status:** **Approved to proceed** (self-disposed 2026-09-12, on Round 30's clearing verdict — 0 HIGH, 0 MEDIUM, 0 LOW, 1 disclosed COSMETIC — per CO-022's own rule that a cleared review with no escalation category applying is self-disposed by the build thread)."* Confirmed at Doc_02's own Disposition section (line 158): *"This disposition rests on CO-022's own standard self-dispositioning path, for the first time since Round 14."*

**Text C (`Doc_03_Lexicon_Candidate_List.md`, line 92, its own Disposition):** *"...this document is self-disposed to Approved to proceed, 2026-09-09, on the project lead's own direct instruction..."*

**The contradiction.** The Profile draws a two-way distinction — Doc_01 is the one self-disposed document, everything from Doc_02 onward was "approved by the project lead" — and states it as a fact a reader would rely on to understand this document's own evidentiary basis. Doc_02's own governing record says the opposite in Doc_02's own words: it was *self-*disposed, by the ordinary CO-022 clearing path (a clean Round 30, no escalation category), with no project-lead act named at all. Doc_03 also explicitly calls itself self-disposed, albeit on the project lead's direct instruction rather than a clean review — a genuinely different, hybrid case the Profile's binary (self-disposed vs. project-lead-approved) does not have room for. Doc_04 through Doc_09 do match the Profile's claim — each explicitly states "It is not a build-thread self-disposition" — so the error is confined to Doc_02 and Doc_03, but it is stated as a blanket claim covering all eight.

**Which is wrong:** the Profile's line 6. It should read something closer to "Doc_01–Doc_03 self-disposed (Doc_02 by clean clearing, Doc_03 on the project lead's direct instruction); Doc_04–Doc_09 approved by the project lead," or otherwise account for Doc_02 and Doc_03 by name.

**Why this matters at HIGH:** a reader relying on this line to understand how much project-lead oversight actually stands behind this world's nine inputs would conclude Doc_02 (Source Ecology — the document underlying every gravity's own evidentiary base) required direct project-lead sign-off, when in fact it cleared on its own and was disposed by the build thread with no project-lead act in the record at all. That is a materially different governance picture than the one stated.

**Fix:** correct line 6 to name Doc_02 and Doc_03's actual disposition path, or drop the binary framing and cite each document's own Disposition section.

---

### HIGH-2 — Section 11's outstanding-items list carries a verification as unperformed after it ran three times and closed

**Text A (the Profile, Section 11, Outstanding item 4, line 733, listed as an open item — not struck through, unlike items 1, 5 and 6 in the same list which are struck through when closed):** *"**Independent verification that the Doc_01 §2 correction propagated cleanly** across all eight files — required by the project lead's own ruling of 2026-09-16, and not performed by the thread that applied it."*

**Text B (`Review-Artifacts/Doc01_Correction_Verification_Round3_2026-09-16.md`, closing section):** *"**The correction can be called closed.**... **The ruling's second limb is discharged a third time, and this time it holds.**"* This is the third of three dated, completed, independent verification rounds in the same folder: `Doc01_Correction_Propagation_Verification_2026-09-16.md` (Round 1, verdict NOT VERIFIED, 4H/4M/6L), `Doc01_Correction_Verification_Round2_2026-09-16.md` (Round 2, verdict NOT VERIFIED, 2H/5M/8L), and Round 3 (verdict: correction closed, "Three findings: one MEDIUM, two LOW. No HIGH.").

**Text C (`lpc_Decision_Log.md`, line 1766):** *"**Second limb, discharged twice and failed twice, then a third correction pass.** The propagation was independently verified on 2026-09-16 and returned **NOT VERIFIED**; a second correction pass answered it and was verified again, returning **NOT VERIFIED** a second time; a third pass closed the two HIGH findings."*

**The contradiction.** The exact independent verification Section 11 item 4 describes as "not performed" was performed three separate times by three separate threads (each verification file states it did not apply the correction and did not write the escalation, satisfying the "not performed by the thread that applied it" independence requirement), and the third round explicitly reports the correction closed. The Decision Log — the Profile's own cited authority for this kind of record — already reflects this in its own text. File timestamps confirm the Profile was last edited (05:04) after all three verification rounds completed (the latest, Round 3, at 02:19), so this is not a case of the verification running after the Profile's last edit.

**Which is wrong:** Section 11 item 4. It should be struck through like items 1, 5 and 6 in the same list, with a note pointing to the three verification files and the Decision Log entry, the way those other items point to their own closing records.

**Why this matters at HIGH:** this is precisely the failure mode this review was commissioned to catch — a document's own "what's still open" record saying a check has not run while the check's own dated output sits in the same folder, having concluded successfully. A reader consulting Section 11 to decide whether the Doc_01 §2 correction can be trusted would be told to treat it as an open, unverified risk, when the governing record says it is closed.

**Fix:** strike item 4, record it as closed with a pointer to the three Review-Artifacts files and the Decision Log's "third pass closed the two HIGH findings" entry, following the same pattern items 1, 5 and 6 already use.

---

### LOW-1 — Method Note describes the condensing pass as run by "a thread" (singular); Document Log and Section 11 describe it as run by "two threads"

**Text A (Method Note, line 16):** *"Doc_07 §8 item 10's remedy — a condensing pass run by a thread that is not also applying findings — was run on 2026-09-16..."*

**Text B (Document Log, line 748):** *"Condensing pass, run by **two threads** not applying findings (Doc_07 §8 item 10's remedy)..."*

**Text C (Section 11 item 6, line 735):** *"~~A condensing pass~~ — run 2026-09-16 by **two threads** that were not applying findings..."*

**Text D (`WorldProfile_Condensing_Pass_2026-09-16.md`):** *"**Run by:** two fresh threads, one per half..."*

**Assessment.** The Method Note's "a thread" most likely carries over Doc_07 §8 item 10's own singular phrasing for the *remedy as specified* ("a condensing pass on §2 is the remedy... it should be run by a thread that is not also applying findings"), rather than asserting the pass was actually executed by one thread. But the Method Note presents this as a description of what "was run," immediately followed by the actual word-count result — a reader has no signal that "a thread" is a carried-over quotation of the requirement rather than a report of what happened, and the two documents that do describe the actual execution agree it was two threads. This is a minor, low-stakes instance of exactly the "carry the exact wording across or state plainly why it differs" rule this review is checking for: the Method Note should either match "two threads" or explicitly flag that it is quoting Doc_07's original singular framing of the remedy rather than describing the execution.

**Fix:** change "a thread" to "two threads" in the Method Note, or add "(actually run by two threads, one per half — see Document Log)" alongside the quoted remedy language.

---

## Summary

Across 23 count/status claims checked against their own cited upstream sources, 21 are consistent — including several places where this document does real, disclosed work reconciling a genuine naming or classification divergence (the G1 name, Doc_04 §7 Item 1's open-by-design status, Section 10's verbatim copy, and the entire Section 9 Living Tradition apparatus, which matches its Decision Log source word for word). The two HIGH findings are both stale self-descriptions of the document's own state — one about which inputs the project lead actually approved, one about whether a required verification has run — and both are directly falsified by dated records sitting in this same folder. Neither concerns a scholarly or gravity-classification claim; both are governance/record-keeping claims the document makes about itself.
