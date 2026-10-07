# Doc_01 Review — Round 2: The Tridentine Church

**Document reviewed:** `Build/World-Builds/Tridentine-Church/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, Revision 2, commit 815477dc5)
**Scope:** targeted recheck of the 13 findings in `Doc_01_Review_Round1.md`, plus any new defect Revision 2 introduced. Items Round 1 accepted are not re-examined.
**Checked against:** `Step0_Movement_Scope_Confirmation.md` (Revision 3, Approved to proceed, per `Step0_Review_Round3.md`); `cic/corpus-map/the-tridentine-church.yaml`; the Hussite and Lollardy Step 0 documents; vendored files `council-of-trent_canons-and-decrees_waterworth1848.txt`, `barlow_brutum-fulmen_1681.txt`, and the four `bellarmine_*` devotional files in `cic/texts/`.
**Method:** every quotation and line citation that Revision 2 added or changed was re-read directly in the vendored file. None was accepted on the document's own "verified" claim.
**Date:** 2026-09-25

---

## Verdict

**SUBSTANTIAL REVISION NEEDED — narrow and targeted.**

Revision 2 resolves 11 of the 13 Round 1 findings in full and two in part. It also introduces three new substantial defects. All three are small, local fixes. None needs a restructuring of the document, and no escalation category is triggered. This is the second of the three capped rounds.

---

## Round 1 findings: status

| Finding | Status | Specifics |
|---|---|---|
| **H1** Session XXI misattribution | **Resolved** | The 1551 article list is gone. The heading "ON COMMUNION UNDER BOTH SPECIES, AND ON THE COMMUNION OF INFANTS" (lines 18004–18005) and Canon I (lines 18007–18010) are verbatim. The Chapter II quotation is verbatim, but its line citation is incomplete (see N5). |
| **H2** Stale Step 0 status | **Resolved** | The header cites Step 0 Revision 3, Approved to proceed, per `Step0_Review_Round3.md`. The old §7 item 10 discrepancy, the escalation claim and the next-step gate are all removed. §8 now says no escalation remains. |
| **M1** Society of Jesus separation | **Partially resolved** | The overlap is named openly, and the distinction is restated as unit-of-world, as required. The Lainez vote (lines 9382–9385) and the Castagna/Lainez persuasion of the Italian prelates (line 9489–9490) are accurate. But the new first-period sentence misstates the source (see N1). |
| **M2** Strand Determination | **Partially resolved** | The substance is fixed. §4 names the derivation-for-unity trap explicitly and stops using it. Test 1 engages the episcopal/papal divergence against the vendored narrative: 181 Fathers, 53 for Granada (lines 9376–9379), and the Legates told to abstain from defining (lines 9847–9849), all verbatim. Test 3 brings in the Missal and Breviary. Test 2 argues Bellarmine from his ground of authority, not from sequence, and defers it to Doc_04 as a plainly stated open item. Two defects remain. The confidence clause misuses the vocabulary in a new way (see N4). Test 2 miscounts the Bellarmine corpus (see N2). |
| **M3** Pre-1517 overclaim | **Resolved** | The claim is narrowed to the specific Lutheran/Reformed controversy. The Hussite 1436 Compactata and the Lollard 1401 statute both match their Step 0 documents. The narrowed claim is tagged. |
| **M4** Later third "unevidenced" | **Resolved** | The later third is now described as "thinly" evidenced, by devotional material only, with institutional developments unevidenced. Cell 3A is corrected. The 1615/1616 dates match the translator's preface (lines 211–214). |
| **M5** Dossier staleness | **Resolved** | §7 item 8 now names §1 (role/confidence and work count), §4, §5 and §6, including the Nicene/Chalcedonian phrasing. |
| **L1** Forces drift | **Resolved**, with a new defect | Confidence tags are added. The Cell 2B inference is labelled Inferential-Thin. The Cell 3B Layer 3 phrasing is removed, and the placement is marked provisional. But the new placement rationale adds an unsupported claim (see N3). |
| **L2** Regnans normalization | **Resolved** | The normalization is disclosed, with the OCR readings and line references. |
| **L3** Session XXII cross-reference | **Resolved** | Now cites Session XXII ch. VIII (line 18612 onward) and Session XXIV reform ch. VII (lines 21069–21077). Both are verbatim in substance. |
| **L4** Session IV cross-reference | **Resolved** | Session IV is now cited directly (lines 12414–12424) and the quotation is accurate. |
| **L5** "Incidental" | **Resolved** | The window is now presented as Doc_01's own decision. The wording keeps a trace of the old error (see N6). |
| **L6** Article 3 gloss | **Resolved** | The gloss is dropped. |

---

## Source-fidelity checks the brief required

- **Chalcedon:** Doc_01 nowhere says Trent reaffirms Chalcedon by name. §7 item 8 correctly says Trent's canons do not reaffirm either council by name. **Clean.**
- **Waterworth role:** described as role tradition (with the double placement as context for the Society of Jesus). **Clean.**
- **Barlow:** "parallel Latin/English text" is used only of *Regnans in Excelsis*, which is genuinely bilingual. Paul III's bull against Henry VIII is not described anywhere. The bull text (tradition) is kept apart from Barlow's commentary (context). **Clean.**
- **Bellarmine *Notes of the Church*:** §7 item 10 identifies it correctly as a 1687–88 Church of England refutation, role context, and says it is not cited as tradition voice anywhere. **Clean.**
- **Second-strand candidate:** Bellarmine's devotional works are stated plainly as an open Doc_04 item in §4 and §8. They are neither dropped nor silently resolved. **Clean**, subject to N2 and N4.
- **World file-code:** the header says "none assigned yet (per Step 0)". Step 0 says the same, and no `trid` code appears anywhere in the repository. This is consistent with the repo. When the code is registered, the header should be updated at that point. It is not a finding at this round.

---

## New findings introduced by Revision 2

### N1. The Lainez first-period sentence inverts the source. (Substantial: it misstates a claim tagged Documented)

§1 says Lainez "argued a minority position on justification in the first period (c. line 4902)". The vendored text says the opposite (lines 4900–4902): "Only five theologians supported this system, which was impugned by the rest, and especially, in a very able argument, by Lainez, of the Society of Jesus." The minority position was the double-justice system. Lainez argued against it, with the majority.

**Required fix:** say that Lainez argued against the double-justice position, which only five theologians supported. Alternatively, say only that he argued in the justification debate. Keep the line citation.

### N2. The "four genuine Bellarmine works" are two works in four translations. (Substantial: a sourcing conclusion that the strand test weighs)

The four vendored files contain only two Bellarmine works:

- *De ascensione mentis in Deum* (1615): *The Mind's Ascent to God* (1925) and *The Soul's Ascension to God, by the Steps of Creation* (Hall, 1703);
- *De aeterna felicitate sanctorum* (1616): *The Eternal Happiness of the Saints* (Dalton) and *The Joys of the Blessed* (Foxton, 1722). The Foxton file's own title page reads "Being, a Practical Discourse Concerning the Eternal Happiness of the Saints in Heaven."

Test 2 and the working determination weigh the candidate as "four works by one figure." §2 and §7 item 10 also say "four … works." The correct figure is two works, 1615–1616. That makes the candidate thinner than stated, not stronger. The conclusion (a deferred Doc_04 test) can stand.

**Required fix:** describe the corpus as two works, each in two English translations. Adjust "c. 1615–1620" in §2 to "1615–1616" for what is actually vendored. The translator's preface names three later works (1617–1620), but none of them is vendored.

### N3. The new Cell 3B placement rationale is unsupported. (Substantial: a new unverified claim)

Cell 3B now justifies the Internal placement "because it marks a late attempt to resolve the episcopal/papal authority question in Rome's own favor (§4 above)." Nothing in the vendored text or in §4 supports this. §4 uses *Regnans* only to show the papal-primacy position stated strongly. The bull itself is aimed at a temporal sovereign. It does not address whether episcopal jurisdiction comes from God or through the Pope. Attributing that purpose is also an interpretive move beyond Layer 1.

**Required fix:** drop the "because" clause. State the placement as provisional, with the two readings named for Doc_08 to test, as Round 1 L1 asked.

### N4. The §4 confidence clause contradicts itself. (Substantial: a confidence-vocabulary defect, and the unfinished part of M2)

The clause assigns "**Inferential-Thin** for whether Bellarmine's devotional works constitute a second strand," and then says the same question carries "no confidence tag of its own because it is an open question." It cannot be both. Round 1 asked for one or the other.

**Required fix:** delete the Inferential-Thin tag and leave the Bellarmine question as a named, untagged Doc_04 test. The Dominant Modern Reconstruction tag on the singular strand can stay.

### N5. The Chapter II line citation is incomplete. (Cosmetic)

The quotation's second sentence ("Wherefore, holy Mother Church … decreed that it was to be held as a law") is at lines 17955–17962, not within the cited 17930–17938. The wording itself is verbatim.

**Fix:** cite lines 17930–17962, or cite both ranges.

### N6. Process narration left in the text. (Cosmetic, but it must be cleared before the document moves to `worlds/`)

Several passages describe the document's own drafting history rather than the world:

- §4 Test 3: "that Doc_01's earlier drafting omitted from this analysis";
- Cell 3A: "The text once placed here is a sourcing-gap disclosure";
- §2 and §7 item 7: "not as its own characterization of the window as 'incidental'";
- §3: "restated honestly (§1 above)";
- §7 item 10: "corrected in the version of Step 0 this document read";
- header and §8: "(addressing `Doc_01_Review_Round1.md`)" and "addressing every finding in".

**Fix:** state the current content plainly and remove the revision narration. The review history belongs in the review files.

---

## Disposition

**Round 2: SUBSTANTIAL REVISION NEEDED.** Doc_01 is not Approved to proceed.

**Must change (substantial):**

1. N1: correct the Lainez first-period sentence.
2. N2: describe the Bellarmine corpus as two works in two translations each, and fix the dates.
3. N3: remove the Cell 3B "because" rationale.
4. N4: remove the self-contradicting Inferential-Thin tag.

**Fix in the same pass (cosmetic):** N5 and N6.

**Round 3** should be a spot-check of N1–N6 only. If Round 3 does not clear, the document hits the three-round cap and goes to the project lead as an unresolved tension.

No escalation category is triggered by this review.
