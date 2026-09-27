# Step 0 Review, Round 3 — The Hussite and Bohemian Brethren Movement

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. This is the final round under the three-round cap. It is a targeted recheck of Revision 3 against Round 2's findings and against the project lead's final window ruling, not a full re-review.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md`, Revision 3 (commit `70fe2e0f5`).
**Records used:** `Step0_Review_Round1.md` and `Step0_Review_Round2.md`, both now present in this folder.

## Verdict

**CLEARED — approved to proceed.** Revision 3 resolves all three of Round 2's substantial findings. The world's window is stated correctly and consistently throughout. Every quote checked matches the vendored text. The four minor findings below are wording and hygiene. None of them makes anything in the document wrong, unsupported or misleading.

**Checked:** every quote in the document that draws on the Hussite vendored texts, matched with a whitespace-normalised search against `cic/texts/hus_de-ecclesia-the-church_schaff1915.txt` and `cic/texts/hus_letters_workman-pope1904.txt`. Every date reference in the document. The current corpus-map `cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml`. The census entries for V.6 and `czech-churches-last-century` in `cic-website/data/world-census.json`.

## The window (the main check)

The final ruling sets the window at **c. 1402–1517**. The start moves back to Hus's preaching career. The end holds at 1517. The 1632 extension was superseded.

- **Stated consistently.** "c. 1402–1517" appears in §0, §1, B1 (twice), B5, the Section B conclusion and §4 item 5. The document never gives "1415–1517" as a window. "1415" appears only as the date of Hus's execution. "1632" (as "1632/33") appears only as the date of the *Ratio Disciplinae*, and every time it is placed outside the window (§0, §1, B1). The superseded 1632 extension is not mentioned anywhere.
- **The reasoning is sound.** §0 grounds the 1402 start in Hus's preaching career, not his death. The vendored *Letters* support this: "Two years later (March 14, 1402) he was appointed preacher at the Chapel of the Holy Innocents of Bethlehem." Workman also notes that the chapel's founders required its rector to "preach every Sunday and festival exclusively in the Czech language", which supports "preaching … in Czech." The reason given for the move also holds: the *Letters* (from June 1408) and *De Ecclesia* (1413) now fall inside the window as own-voice core rather than as background. The census's own `statusDescription`, quoted verbatim in §0, already says "Its Prague formation (1402–14) precedes Hus's burning." See R3-m1 for one small point of precision.
- **The *Ratio Disciplinae* is placed correctly.** §0, §1, B1 and B2 all describe it as outside this window and belonging to `czech-churches-last-century` (Atlas VI.24, census `dates: "1517-c. 1627"`, verified). The corpus-map now files it `role: context`, with a note giving the same reasoning. The document and the map agree.

## Round 2 findings — status

- **R2-S1 (misattributed floor quote): fixed.** The Paschasius footnote quote has been withdrawn. A1 now uses two passages that are Hus's own body text, not footnotes:
  - p. 18: "so Christ is the in- dividual, the true God and man, imparting spiritual life and motion to the church." This is exact once the OCR line-break hyphen is closed up. It sits in Hus's running argument on Christ as head of the church, between the running heads for pp. 18 and 19.
  - p. 84: "and so Peter confessed Christ to be very God and very man." This is exact, in Hus's exposition of Matt. 16:16, under the running head for p. 84.
  A1 claims no more than this evidence supports. It still defers a full five-commitment check to Doc_01.
- **R2-S2 (stale sourcing): fixed.** The corpus-map holds eight works: two `tradition` (Hus's *Letters* and *De Ecclesia*) and six `context` (Gillett; Lützow ×3; Piccolomini; *Ratio Disciplinae*). B1, B2, the Section B conclusion and §5 all state this correctly. "Two" now refers only to tradition-role works, which is accurate. B3 now cites Lollardy's vendored Wyclif *Tractatus de Ecclesia* (`wyclif_de-ecclesia-lat_loserth1886.txt`) by filename. The Tier's two provisional grounds have been re-grounded on the current map, and both still hold: no in-window Unity tradition voice, and single-author tradition sourcing.
- **R2-S3 (window): fixed, under the final ruling** (see above). The cross-world question has been settled by that ruling, and §4 item 5 is correctly marked resolved.
- **R2-m1 (reading-scope disclosure): fixed.** A1 now describes the provenance headers as OCR spot-check notes. It states the actual method: targeted search and verification of cited passages, not an exhaustive reading.
- **R2-m2 (narration): mostly fixed.** Every item Round 2 listed is gone. Two small remnants remain (R3-m3).
- **R2-m3 (Round 1 record missing): fixed.** `Step0_Review_Round1.md` is now in this folder.
- **R2-m4 (A5 vs B3): fixed.** A5 now calls the link direct textual borrowing, not a contemporary-influence question, and notes that Wyclif died in 1384.
- **R2-m5 (orphan word-count sentence): fixed.** The sentence has been removed.

## Quotes re-verified this round

All match the vendored files, allowing for OCR whitespace and hyphenation:
- *De Ecclesia*: the p. 18 and p. 84 passages above. Schaff's "Huss appropriated paragraph after paragraph from his predecessor and transferred them often with little verbal change to his own pages." "Never … did a man owe more to mortal teacher than Huss did to John Wyclif" (split by a page break at p. xxvii).
- *Letters*: "Hitherto, Hus had taken little interest in the matter — in fact, in his De Coena Domini, written at a later date, he still practically concedes the Roman position." "In the summer of 1414" (Jakoubek). "I have appealed to Christ" (the file reads "…to Christ Jesus"). The March 14, 1402 Bethlehem appointment. Letter VI to Richard Wyche, "He read it in the Bethlehem."
- Census: the `statusDescription` sentences quoted in §0 are verbatim.

## Minor findings (not blocking)

**R3-m1. The 1402 start is slightly more exact than the source.** §0 and §1 say Hus "began preaching reform in Czech at Prague's Bethlehem Chapel in 1402." The *Letters* give 1402 as the date of his **appointment** to the Bethlehem. Workman's footnote adds: "According to Hus's own statement, the first year of his preaching was 1401 … He was elected to the Bethlehem March 14, 1402." The window's "c." covers the difference, and the Bethlehem appointment is a reasonable anchor. Still, a Doc_01 that describes the start should say "appointed preacher at the Bethlehem Chapel in March 1402" rather than suggesting his preaching began then. Carry this forward to Doc_01. It does not require another revision here.

**R3-m2. B1's count sentence is awkward.** "Six further works … all filed `role: context`" is followed by a list of five and then "The … *Ratio Disciplinae* … is also vendored," which reads like a seventh. That list of five also ends "— all secondary," although the same sentence calls Piccolomini a contemporary source usable as primary evidence. The totals stated elsewhere (six context-role works, eight in all) are correct, so this is a matter of clarity, not accuracy.

**R3-m3. Two small pieces of process narration remain.** B1 says "vendored in a post-Revision-2 acquisition pass." §0 says "the same record shape Lollardy's own Step 0 correctly carried forward." Both are revision-history framing rather than present-tense content. Remove them at the next hygiene pass.

**R3-m4. The Status line and §6 still say "not independently reviewed at Revision 3."** Update both to point to this review and its disposition. This is a mechanical change.

## Outside this document (reported, not fixed)

- The census V.6 entry still reads `dates: "1415-1517"` (line ~13156 of `world-census.json`). It should follow the final ruling (c. 1402–1517).
- Corpus-map notes: the *Letters* note still says "his career at the university" (the letters begin in June 1408). Several notes still carry process narration ("post-Step0-Revision-2 PD source-acquisition pass", "no prior Source Readiness Dossier or corpus-map presence", "Fills out … previously only Hus's own two vendored works"). Fix these in `_staging/` and re-merge. Run `tools/check_live_commentary.py`.
- The Hussite Source Readiness Dossier is still stale, as Round 2 reported (two works; "contested" influence line; hymnbook attributed to `relationsSummary`).

## Disposition

**CLEARED — approved to proceed.** No substantial findings. Four minor findings (R3-m1 to R3-m4), none of which requires another review round. R3-m3 and R3-m4 are hygiene. R3-m1 is carried forward as binding on Doc_01. R3-m2 is optional clarity. This does not close anything at portfolio level. It also does not select the world for a build: the world has no file-code, and selection remains Mark's decision.
