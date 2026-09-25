# Step 0 Review, Round 2 — The Tridentine Church

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck, not a full re-review.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md`, Revision 2, as it stands after the narration-stripping hygiene pass (commit `4b4ce830`). Compared against the pre-hygiene Revision 2 text (commit `e3d87bb8`) and the Round 1 findings (commit `acd9a888`).
**Scope of this recheck:** (1) whether each Round 1 finding was actually fixed; (2) whether the hygiene rewrite dropped, softened, or distorted any fact, quote, date, or citation; (3) every quote re-verified by direct grep of the vendored files; (4) consistency with the current corpus-map.

## Verdict

**Revision needed: one substantial finding, five moderate.** The Round 1 fixes themselves hold. S1 (Trent/Chalcedon) and S2 (the floor as yardstick) are correctly and precisely fixed. Every quote checks out verbatim.

The substantial finding is new, and it is not a failure of the Revision 2 author. After Revision 2 was drafted, a source-acquisition pass vendored the very leads this document still calls "not yet vendored" or "closed" (the corpus-map rows call it the "post-Step0-Revision-2 PD source-acquisition pass"). The corpus-map defect the document flags has also since been fixed. As it stands, the document's sourcing section, ecology, Tier rationale, and three binding §4 obligations describe a Library that no longer exists. The hygiene pass rewrote the prose but did not catch this.

## Findings

### Substantial

**S1. The sourcing picture is stale against the current Library. Several binding claims are now false.** `cic/texts/` and `cic/corpus-map/the-tridentine-church.yaml` now hold, for this world:

- **Pole:** `pole_seditious-oration_wythers1560.txt` is vendored (role: tradition). B1, B2, the Tier rationale, and §4 item 1 all still say "not yet vendored." The document also misses the file's real live status. The corpus-map flags it under the OCR ruling "a" (2026-09-25, `worlds/_cross-world/LIBRARY-DECISION-LOG.md`) as a garbled black-letter scan. It stays **second witness** until a cleaner edition is vendored. That is the fact Doc_02 needs.
- **Liturgical books:** `roman-breviary_bute1908.txt` and `roman-missal_england1843.txt` are vendored (both role: tradition). B1, B2, and §4 item 3 still say "not yet vendored" and "unassessed." The Breviary caveat is also now incomplete. Only **one of four** seasonal volumes is vendored. Leo XIII's later revision is still correctly disclosed.
- **Borromeo:** `borromeo_acta-ecclesiae-mediolanensis-lat_1599.txt` is vendored as role: tradition. Under Mark's 2026-09-25 Library ruling (original-language sources can be primary evidence), this Latin text is primary evidence directly. B1/B2 ("Borromeo's remains genuinely closed"), the Tier rationale ("Borromeo closed"), §4 item 1, and especially **§4 item 5** ("not as a source of his own primary voice") now contradict both the corpus-map and a standing ruling. The Wigley/English caveat is still true as a statement about English translation. "Closed" is no longer true as a statement about Borromeo's primary voice.
- **Unmentioned additions:** Pius V's own apostolic letters (`pius-v_apostolicarum-epistolarum-lat_1640.txt`, Latin, role: tradition) and five Bellarmine works (role: tradition) are also now mapped to this world. B1 still inventories four files and gives "~1.22M raw OCR words across all four files." That figure is correct for those four (independently re-counted: 1,216,996). But it now describes 4 of 14 mapped files.

This changes a sourcing conclusion, the ecology's central "thin personal/pastoral voice" claim, and binding carry-forward obligations. It meets the bar for substantial. It is not a "could be stronger" point. The fix is a factual update against the corpus-map, not a re-argument.

### Moderate

**M1. The corpus-map defect the document still flags has been fixed.** B3, §4 item 4, and §5 all say this world's corpus-map sets the Waterworth Canons/Decrees to `role: context` and that "neither world currently holds the text as 'native.'" The current corpus-map has that row at **role: tradition, confidence: assigned**, described as "this world's own defining conciliar voice." The Society of Jesus map holds the same file at role: context. The native/implementing split the Round 1 review (M10) found missing now exists. The document should report it as resolved, not open. §4 item 4 should drop its blocking precondition.

**M2. The hygiene pass distorted the Imperial Juridical Christianity precedent (B2).** Revision 2 said the IJC precedent "doesn't actually support 'no personal voice at all'": IJC's Doc_02 rests on first-person voices (confirmed: Eusebius; Ambrose, including *Sermo contra Auxentium*). The rewrite says the precedent "does not support treating a thin personal-voice gap as disqualifying." That is a different claim, and the supporting clause does not support it. IJC having rich first-person voices shows it is *not a precedent* for a voice-thin world. It says nothing about whether a thin gap disqualifies. This is a meaning change introduced by the rewrite. Restore Round 1 M4's actual point.

**M3. The hygiene pass is incomplete. Revision-history narration remains throughout.** Examples: "not the 'no figure word-extracted' boilerplate Revision 1 carried" (B1); "dropped in Revision 1's 'no PD English translation anywhere' overclaim" (B1, Borromeo); "'Alongside the Society of Jesus, the cleanest... in this batch' is also dropped" (Section A conclusion, a sentence that only makes sense as a changelog); "narrower than Revision 1 described" and "than Revision 1's purely 'ecological' framing suggested" (Tier); "narrower than previously stated" (§4 item 1); "Revision 1 called him a 'critical Venetian outsider'" (§4 item 2); "(§3 B3, corrected)" (§4 item 4); "Per §0/§1, corrected" (§4 item 7); the A1 heading ("on corrected evidence and a corrected relationship"). The pass did not meet its own stated goal. If the document is meant to read as present-tense prose, these need the same treatment.

**M4. The Round 1 review this document cites is not in this tree.** The status line and §6 point to `Step0_Review_Round1.md` "for the full finding list." After the hygiene pass, §6 no longer summarizes S1–S4 itself. That file exists only on `origin/source-research/step0-review-round1` (commit `acd9a888`). It is not on this branch or in `World-Builds/Tridentine-Church/`. The audit trail currently points at nothing. Either merge the Round 1 file alongside this one, or keep a one-line finding summary in §6.

**M5. §5's Library-defect list is partly stale and partly under-stated.**
- The corpus-map native/implementing item is fixed (M1).
- The Paul III language question can now be stated with more confidence. A direct read of the Barlow file finds *Regnans in Excelsis* in genuine English/Latin parallel columns (English "He that reigneth on high…" c. lines 2263–2294; Latin c. 2305 onward). The Paul III bull ("Paulus Episcopus, Servus Servorum Dei," c. line 28698 onward) appears in **Latin only**. No English rendering was found, and the only English near it is Barlow's own commentary and the table of contents. The new Barlow tradition row that was just split out repeats "printed in English and Latin parallel columns" for **both** bulls. So the defect was carried into the new row, not fixed.
- The dossier itself still says of Pole: "No PD English translation found anywhere" (dossier line 68). That is a Library-level contradiction §5 should list.

### Minor (not grounds for another round on their own)

- **m1. A1, last sentence:** "not a floor complication-free exemption" is garbled. It no longer clearly withdraws Revision 1's "no floor complication exists or could exist." Suggest: "This is a considered clearance like every other candidate's; it does not claim the floor question could never arise."
- **m2. A1, "'Nicaea' appears solely in a footnote citation":** true as scoped to Session III (footnote "Concil. Nicnen.", c. line 12356). But the decrees name Nicaea in body text twice elsewhere. Session XIII, ch. VI (c. line 15232) cites "the age of the Council of Nicaea" on reserving the Eucharist. Session XXV (c. line 21978) cites "the second Synod of Nicaea" on images. Neither reaffirms the creed by name, so the substance holds. Add "in Session III" explicitly so the sentence can't be read as covering the whole decrees.
- **m3. Window wording is inconsistent in direction.** §1 says the 1517–1650 window "is looser than the Council's own dates." §4 item 7 says "the stated window is looser than the actual 1517–1650 range." One sentence should state it: the document's own described scope (Paul III through the early 17th century) is narrower than the census's 1517–1650 window.
- **m4. Pole rights wording.** B1 says the item has "no access restriction." That is an access fact, not a rights fact. The vendored file's own header records that the archive.org item carries **no** `possible-copyright-status` tag, unlike the Breviary, Missal, and Barlow items, which carry `NOT_IN_COPYRIGHT`. PD by date (1560) is sound on its face, so nothing here is contradicted. But the document should not let "no access restriction" stand in for a rights check. Whatever the pending cross-world rights re-check on this EEB scan concludes, Doc_02 should cite that, not this sentence. (No written record of that re-check was found in `worlds/_cross-world/` or `Ministry/`; if it exists, it should be registered there.)
- **m5. Barlow characterization.** The document doesn't call the whole Barlow file "tradition." B1 describes it as a file that "prints" the bull, and the Pole paragraph names Barlow's "hostile Protestant frame." That is consistent with the new two-row split, so there is no error. Once S1 is fixed, B1 should name the split explicitly: bull text = tradition; Barlow's own commentary = context.

## Round 1 findings: status

| R1 | Status | Note |
|---|---|---|
| S1 Trent/Chalcedon | **Fixed, verified** | See "Confirmed accurate." Precise, not cosmetic. |
| S2 Floor-yardstick framing | **Fixed** | Minor garble (m1). |
| S3 Pole | Fixed at the time. **Now stale** | Superseded by vendoring (S1). Pole role quote verified. |
| S4 Liturgical books | Fixed at the time. **Now stale** | Superseded by vendoring (S1). |
| M1 Borromeo caveat | Fixed, quote verified. **Now stale** | Latin Acta vendored as tradition (S1). |
| M2 B5 superlative | Fixed | Census "Rome, then the world" confirmed. |
| M3 Stale Jesuit Constitutions contrast | Fixed by removal | Acceptable. |
| M4 IJC precedent | Fixed in Rev 2. **Distorted by hygiene pass** | See M2. |
| M5 Session count | Fixed | |
| M6 Window | Fixed in substance | Wording inconsistent (m3). |
| M7 Sarpi status | Fixed | Pseudonym (Pietro Soave Polano) and Protestant framing (Brent's dedication: "an erroneous opinion of the infallibility of this pretended Council") confirmed in file. |
| M8 Batch arithmetic / unfindable rationale | Fixed | "Sharpest possible three-way" confirmed absent outside World-Builds. |
| M9 Word counts | Fixed, re-counted | 1,216,996, but see S1. |
| M10 Corpus-map native split | Flagged in Rev 2. **Now resolved in the Library** | Document stale (M1). |

## Confirmed accurate

- **Trent/Chalcedon (S1), independently confirmed by grep of `council-of-trent_canons-and-decrees_waterworth1848.txt`:**
  - Session III (Decree Touching the Symbol of Faith, c. lines 12306–12375) recites the full creed and names it only as "the Symbol of faith which the holy Roman Church makes use of" (lines 12339–12340, verbatim across the line break).
  - The only Nicaea reference in Session III is the footnote "Concil. Nicnen." (line 12356).
  - The filioque, "who proceedeth from the Father and the Son" (lines 12368–12369), is verbatim.
  - "Chalcedon" occurs three times in the file. Two are in Waterworth's historical essay (lines 2820 and 11383), before the decrees begin at line 12150. The **only** occurrence in the decrees is Session XXIII, ch. XVI (line 19846): "adhering to the traces of the sixth canon of the Council of Chalcedon, ordains that no one shall for the future be ordained without being attached to that church…" That is a disciplinary citation on ordination, exactly as the document says.
  - The document no longer makes the blanket "by name" claim. It states the opposite precisely.
- **Pole's role:** "composed by Cardinal Pole" is verbatim at lines 3662–3663 ("…a long exhortation, composed by / Cardinal Pole, in which the prelates were exhorted…"), in the Session II account (7 January 1546). The "three legates… presiding" framing matches the decrees' own "the same three legates of the Apostolic See presiding therein." The document does not undersell Pole as merely "implementing."
- **Pole lead details** match the vendored file header: title (*The Seditious and Blasphemous Oration of Cardinal Pole*; the document's ellipsis is fair), translator Fabian Wythers, 1560, and the archive.org identifier `bim_early-english-books-1475-1640_the-seditious-oration_pole-reginald_1560`. The document correctly says "a PD English translation exists" and no longer says "survives only in Latin."
- **Article 4's five commitments** are verbatim against the Constitution (the docx carries "Version 2.3" internally despite its `V2_2` filename). "Belief, not institutional submission to any council's authority" is verbatim ("a test of belief, not institutional submission to any council's authority"). The ELLC/filioque-free/381 description is confirmed.
- **Dossier Borromeo caveat** is verbatim: "closed as not found, not assumed available" (dossier line 69, with the Dolman/Wigley 1857 details).
- **Other checks:** *Regnans in Excelsis* is in English and Latin in the Barlow file. The Breviary title and 1908 Leo XIII caveat match the file header. The Missal title and 1843 date match. Census VI.22 fields (1517–1650, `continuesAs`, "the reformed liturgical books") are correct. The corpus-map's "not the Society's own composed voice" wording is verbatim, though now on the Society of Jesus side of the double-placement.
- **Hygiene pass, apart from M2/M3/m1:** every other fact, date, citation, line reference, and quote in the Revision 2 text survives the rewrite unchanged. The diff between `e3d87bb8` and `4b4ce830` was checked line by line.

## Disposition

Per `cic-build-cycle`: S1 changes a sourcing conclusion and three binding §4 obligations, so it is a substantial finding. But it comes from supervening Library work, not from a defect in how Revision 2 answered Round 1. Round 1's own findings are genuinely fixed, not cosmetically. The Trent/Chalcedon and Pole nuances are preserved exactly as they should be.

A Revision 3 should do the following:
- Update B1/B2/B3/Tier/§4/§5 against the current corpus-map (S1, M1, M5).
- Restore the IJC point (M2).
- Finish the narration strip (M3).
- Make the Round 1 file reachable (M4).
- Optionally take the minors.

A targeted Round 3 recheck should then look only at those sections. **This is Round 2 of the 3-round cap.** If Round 3 finds a substantial problem, the pipeline must escalate rather than open a fourth round. Because S1 is a factual sync, not a contested argument, one pass should close it.

**Separate from this document (Library-level, not fixed by this review):**
- The new Barlow tradition row's "English and Latin" claim for the Paul III bull (M5).
- The dossier's stale Pole line (M5).
- The absence of any written record of the Pole EEB rights re-check (m4).
