# Step 0 Review, Round 3 — Devotio Moderna / Brethren of the Common Life

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck of Round 2's findings (R2-S1 to R2-S3, R2-M1 to R2-M6 and the minors), plus a spot re-verification of every quote this reviewer checked. This is the final round under the three-round cap.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` at Revision 3 (commit 1c25a20fc).
**Checked against:** the current text of `cic/texts/INTAKE.md`; the 2026-09-25 entry in `worlds/_cross-world/LIBRARY-DECISION-LOG.md`; follow-up commit cd63bbab; `cic/corpus-map/devotio-moderna-brethren-of-the-common-life.yaml`; the census entry in `cic-website/data/world-census.json`; and the vendored files in `cic/texts/`. Every quote was checked with whitespace normalized, because the Arthur and Benham files use double spacing. The document's own "verified" claims were not relied on.

## Verdict

**CLEARED. Approved to proceed.** No substantial revision is called for.

All three Round 2 substantial findings are fixed in substance. The Groote primary-versus-second-witness question is resolved correctly. Its citations of INTAKE.md and the Decision Log are accurate. The vendored-corpus picture is current. Both attribution errors are corrected.

What remains is a small set of corrections. Under the skill's *Revision decision* rule, each one is a wording, arithmetic or quote-form fix. None changes a claim's substance, a confidence rating, a sourcing conclusion or a scope boundary. These are applied directly and noted, with no fresh review round. One cross-document item goes to Mark for a decision-log entry, as disclosure only. It does not block this document.

## Round 2 findings: disposition check

| Round 2 | Fixed? | Verification |
|---|---|---|
| **R2-S1 Groote letters primary vs. second witness** | **Yes, resolved** | See the next section. |
| R2-S2 stale vendored picture | Yes | The corpus-map lists exactly 11 `source_file` entries, and all 11 exist in `cic/texts/`. B1's list matches them one for one: Benham, *Founders*, *Chronicle*, *Little Garden*, four Pohl volumes, Busch/Grube, Zerbolt/Arthur 1908 and Acquoy. Zerbolt is no longer called a gap. "Zero vendored representation" of the women's side has become "no vendored text carries the Sisters' own voice directly." The *Chronicle*'s Diepenveen investiture is at line 4282: "In the year 1408, on the Feast of St. Agnes the Virgin, the Sisters of the Order of Canons Regular in Diepenvene near Deventer were first invested." Van Engen's *Basic Writings* is now in the B2 gap list and in §4 item 5. |
| R2-S3a Utrecht letter | Yes | B1 now says the letter was "written on his behalf, not by him." *Founders* line 5096 reads verbatim "A Letter to the Bishop of Utrecht on behalf of Master Gerard Groote". Acquoy's introduction (line 3791) names the author as an unnamed friend. A1's "a friend's letter ... written on Groote's behalf" agrees. One quote-form issue remains (R3-M1). |
| R2-S3b *Founders* attribution | Yes | A1 now reads "Kempis's *Founders*". B1 gives *Founders* as "Kempis's own." |
| R2-M1 Protestatio overstated | Yes | A1 now calls it "a general profession of Catholic orthodoxy and submission to Rome." It says the Protestatio "has no Trinitarian or Christological content in the specific sense Article 4's five commitments name." The floor rests on the census "No question" and on the absence of any complication. Both quoted segments are verbatim: "in regard to those things that are of faith, I have steadfastly preached and defended that faith which is certain, pure, and Catholic, resting upon Jesus Christ Himself Who is the chief corner Stone" and "subject always to the judgement of the Holy Roman Church, to whom with all humility I everywhere and always submit myself." The ellipsis between them is honest. Ch. XVIII is at line 4147. |
| R2-M2 §0 "documented ... already-source-ready" | Yes | §0 now points to B3 "including the Luther direction's own contested status." The "already-source-ready" wording is gone. |
| R2-M3 selection history | Disclosed, not resolved | §0 and §4 item 6 now name the conflict with the Hussite Step 0 and flag it for a decision-log entry. The Hussite Step 0 (line 16) still reads "Selected directly by Mark ... to bring Era 6 to a three-candidate set." No decision-log entry exists yet. Deciding which account is right needs Mark, and it spans two documents, so it cannot be closed from inside this one. See the Disposition. |
| R2-M4 narration strip | Mostly | The "corrected" and "correction" tags are gone. A small residue remains (Minor, below). |
| R2-M5 Round 1 file missing | Yes, outside this document | `Step0_Review_Round1.md` is now in the folder (merged in 084e4bd20). |
| R2-M6 "14 of 66" | Yes | §4 item 2 reads "14 of the 64 letters attributable to Groote survive in this edition, of 66 total in the codex (two are William of Salvarvilla's)." Acquoy lines 891–898: "Hae epistolae sunt numero sexaginta sex ... Undevigesima et vigesima non sunt Gerardi Magni sed Guilielmi de Salvavarilla, cantoris Parisiensis." The file has 14 letter headings, EPISTOLA I–XIV, at lines 1380–7171. One wording point: "survive in this edition" should be "are edited in this edition." Acquoy's 14 are a selection from a codex of 64, not the only survivors (Round 1 S3). B1 gets this right ("covers 14 of them"). Folded into R3-m1. |
| Minor: "evidently" vs. "rests" | Yes | "Evidently" no longer appears. |
| Minor: Benham on Gersen | Yes | The document now reports "the advocates of the Gersen authorship" and "Whoever the author may be". Both are verbatim, at lines 660 and 663. On re-reading, Round 2's minor slightly understated Benham. He does lean towards Gersen: "there seems strong reason for accepting the belief that the writer of the Imitatio was John Gersen" (line ~628). The current neutral wording is accurate either way. See R3-m2 for a quote-form point. |
| Minor: Xavier anchor | Yes | It is now attributed to "Coleridge's 1872 editorial narration." "the Imitation of Christ" is at line 3509. The Alcazar footnote, "the book de Contemptu Mundi , i. e. the Imitation of Christ", is at lines 4534–4535. |
| Minor: dangling boilerplate | No | See R3-m3. |
| Minor: census dash | Yes | `relationsSummary` is quoted with " - ", matching the census. |

## The Groote question: resolved, and correctly cited

This was the most important check this round. It is **genuinely and correctly resolved.** It is not left open and not re-opened.

- **The Decision Log.** The 2026-09-25 entry in `LIBRARY-DECISION-LOG.md` records Mark's words: "non english sources are treated as primary sources if they are primary sources to the world. language should not matter, only the sources credibility and truth." Its point 1 reads: "A clean public-domain original-language text can be primary evidence, on the same footing as an English translation would be, when it is primary to the world it's assigned to."
  - B1 paraphrases this point almost word for word.
  - §4 item 2 cites the entry correctly.
- **INTAKE.md.** The current text (lines 27–30) reads: "**A clean public-domain original can be primary evidence (Mark's ruling, 2026-09-25).** Language is not what decides whether a source is primary — credibility and truth are." The document's "`cic/texts/INTAKE.md` states this as the current rule" is accurate.
  - The retired "second witnesses — never primary evidence" phrasing no longer appears in the document at all.
  - The false present-tense "quote" of the corpus-map that Round 2 flagged is also gone.
- **Applied to Groote specifically.** Follow-up commit cd63bbab ("Re-assess Latin/German sourcing across the six worlds under the new rule") re-assessed the Groote letters the same day. The corpus-map's Groote note now reads: "Under Mark's own 2026-09-25 ruling ... this label now has real backing: a clean public-domain original can be primary evidence when it's primary to the movement, which this is."
  - The document's "The corpus-map's Groote entry applies the ruling directly" is accurate.
  - Its "not reported through Kempis's later biography" paraphrases that note faithfully.
- **Mechanics.** B1 lays out how the letters are used: a quote record holds the verified Latin; the spoken English is an Opus rendering, independently Opus-checked; *Founders*' English is a cross-check, not a precondition. This matches INTAKE.md's three bullets and the Log's points 2–4 exactly.
- **The Jesuit precedent.** The document drops it and states why: the 1606 Constitutions and Nadal's 1595 *Adnotationes* are both on the Log's garbled-scan list under OCR ruling "a". That is correct.

One overstatement sits inside this otherwise correct resolution (R3-M2): the document says "the scan is clean." That affects how each quote is verified. It does not affect primary status.

## New findings

### Substantial

None.

### Moderate (correct directly; no review round needed)

**R3-M1. The Acquoy "quote" is a normalized reading, not the vendored text.**

- B1 quotes Acquoy's introduction as "quidam Gerardi amicus, cujus nomen non ad nos pervenit".
- The vendored file (lines 3790–3791) actually reads: "qoidam Girardi amicoa, cojos nomea non ad nos pervenit".
- The reading and the attribution (an unnamed friend) are both correct. But this project requires quotes to match the vendored file verbatim.
- **Fix:** Either quote the OCR as it stands, or mark the Latin as a normalized reading of the vendored OCR ("Acquoy, normalized from the scan: *quidam Gerardi amicus...*"). This is a form fix. The attribution does not change.

**R3-M2. "The scan is clean" is stronger than anything in the record supports.**

- The corpus-map's Groote note does not say this. The Busch note does. The file's own header says it was "not independently spot-checked for OCR quality beyond the opening pages and a mid-document sample".
- The scan is not on OCR ruling "a"'s garbled list.
- The letter bodies are readable Latin with scattered OCR errors: "spiritimi", "curiara", "Fapae" and "dicitar", all at lines 1411–1428. Acquoy's small-type introductions and notes are much worse, with systematic u→o and s→a substitutions; see R3-M1.
- INTAKE.md's own classification wording fits this case: a "primary original-language voice, ready to quote once verified against the scan."
- **Fix:** Replace "and the scan is clean" with "and the scan is not on OCR ruling 'a''s garbled list. Each quote is verified against the scan, and the editor's introductions are noticeably noisier than the letter bodies."
- **Why this is not substantial:** primary status is unchanged, and so is every sourcing conclusion. What the fix adds is a care point for Doc_02, carried into §4 item 2 as part of the same fix.

### Minor (apply directly)

- **R3-m1. A3 has an arithmetic slip.** It says "Groote died in 1384, six years after this world's own 1380 window-start." That is **four** years. The error has been there since Revision 2 (e3d87bb8), and Round 2 missed it. Both dates are stated correctly elsewhere, and the A3 conclusion does not depend on the interval. Also, per the R2-M6 row above, in §4 item 2 "survive in this edition" should become "are edited in this edition."
- **R3-m2. "Abbot John Gersen" is a composite quote.** B1 puts "Abbot John Gersen" in quotation marks, but Benham never uses that exact phrase. He writes "Abbot John," (line 614) and "Abbatis Joannis Gersen" (line 618), and states the 13th-century dating in his own words (line 604). **Fix:** Drop the quotation marks, or quote "Abbot John" alone.
- **R3-m3. The dangling boilerplate is still there** (carried from Round 2). "Figures in this document are raw word counts from vendored .txt" is still at the end of B1, and the document contains no word-count figures. **Fix:** Delete the sentence.
- **R3-m4. Some process narration remains.**
  - "Not independently reviewed at this revision" and "Revision 3" appear in the Status line and §6.
  - B2 has "closing what an earlier pass flagged only as an unverified lead."
  - The Tier paragraph has "stronger than the three-work base this document started from."
  - §5 has "reviewed twice under independent review before this revision."
  - The Status line and §6 should now point to this Round 3 file and record the disposition.
  - The rest is document-history narration and should be cut, per the CLAUDE.md "live/canonical surfaces" rule the hygiene pass enforced.

## Confirmed accurate (re-verified this round)

- The *Founders* quotes are verbatim:
  - "many prelates of the Church were opposed to him ... forbidden to preach by an edict craftily obtained" (~line 2754)
  - "Westphalia and Saxony" (line 3797)
  - "Resolutions and Intentions" and "not confirmed by vows" (~line 4223)
- The census quotes are verbatim: `statusWord`, `statusDescription`, `floorNote` "No question", `relationsSummary`, `longDescription` "After his death in 1384", `voices` "No single founding figure holds the women's side...", `legacy` "a household connected with the Brethren", and "forbidden to preach the year before for attacking the clergy's concubines."
- The census window is `start` 1380 / `end` 1517. The 1374 deed is dated "20 September 1374" in `documentedStories`.
- Benham gives "about the year 1380" (line 493) and "the erroneous notion that he was its author" (line 520). The header gives "c. 1380-1471".
- Acquoy says the Protestatio was printed after Kempis's Vita: "quam Thomas a Kempis Vitae ejus adjecit" (line ~3783, OCR normalized).
- The Section A and Tier 1 conclusions follow from the evidence as the document now states it.

## Disposition

**CLEARED. Approved to proceed** at the Step 0 level. No substantial revision is called for, so the three-round cap is not triggered and nothing is escalated for a fourth round.

- **Corrections to apply directly.** R3-M1, R3-M2 and R3-m1 to R3-m4 are wording, arithmetic and quote-form fixes. The drafter applies them directly and notes that they were applied, per the skill's *Revision decision* rule for non-substantial changes. They do not need a new review round.
- **For Mark (disclosure only, not blocking).** The Era 6 selection-sequence conflict between this document and the Hussite Step 0 (R2-M3) needs a decision-log entry recording what actually happened. Only Mark can confirm the sequence. It is a cross-document record question, not a scope or sourcing question for this candidate. This document already discloses it plainly.
- **Scope of this disposition.** "Approved to proceed" applies to this Step 0 document only. It does not select the candidate, assign a world file-code or open a build thread. Those remain Mark's call. Nothing closes before Phase Five boundary testing and full-system review.

**Outside this document (flagged, not touched):** The corpus-map's Groote staging entry still contains inline "Correction (2026-09-25)" narration. It also still calls the edition "Gerard Groote's own surviving letters", which should be "fourteen of them." Both are for the corpus-map owner.
