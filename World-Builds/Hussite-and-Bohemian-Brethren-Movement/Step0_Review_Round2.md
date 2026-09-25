# Step 0 Review, Round 2 — The Hussite and Bohemian Brethren Movement

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck of Revision 2 against Round 1's findings, not a full re-review.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md`, Revision 2, as it stands after the narration-stripping hygiene pass (commit `4b4ce830`).
**Round 1 record used:** `Step0_Review_Round1.md`, read from commit `acd9a888` (branch `origin/source-research/step0-review-round1`). It is not in this branch's tree or in `origin/main` (see R2-m3).

## Verdict

**Substantial revision needed.** Revision 2 fixed most of Round 1's findings properly, not just on the surface. F1, F2, F4, F6 and F7 are genuinely resolved, and every quote those fixes rely on checks out word for word against the vendored text. The hygiene pass did not drop, soften or distort any fact, quote, date or citation.

Three things still block it:

1. **A new misattribution, introduced by Revision 2's own F5 fix.** A1's "positive evidence" quote comes from the 1915 translator's footnote, not from Hus.
2. **The sourcing claims are now stale.** The corpus-map moved from two works to eight after Revision 2 was written.
3. **Mark's 2026-09-25 ruling extends the window to about 1632.** That supersedes the document's stated 1415–1517 window.

**Checked:** the full diff of Revision 2 against the hygiene pass (`a67b1b2e`→`4b4ce830`). Every quote in the document, matched with whitespace-normalised search against `cic/texts/hus_de-ecclesia-the-church_schaff1915.txt`, `cic/texts/hus_letters_workman-pope1904.txt` and the Constitution's Article 4 text (`reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx`). The census entry (`statusWord`, `statusDescription`, `sourcing`, `floorNote`, `relationsSummary`, `why`, `sources`). The current Hussite and Lollardy corpus-maps. REGISTRY.yaml. The Hussite dossier. The `czech-churches-last-century` census entry.

## Substantial findings

**R2-S1. A1's "positive evidence" quote is misattributed to Hus. The error is new in Revision 2.** A1 says *De Ecclesia* "in its own discussion of the Eucharist (c. p. 10) … quotes without dissent Paschasius's account of the body 'which was born of the Virgin Mary, suffered on the cross and rose again.'" The words are real, but they are not Hus's. They sit in **Schaff's own 1915 translator's footnote** explaining who Paschasius was: "This treatise of Paschasius, d. 865 … Without using the word, Paschasius set forth the view that in the Lord's Supper the very body 'which was born of the Virgin Mary, suffered on the cross and rose again,' is distributed by the priest."

Hus's own text at that point (Chapter I, "The Unity of the Church," pp. 9–10) quotes Paschasius on something else. His subject is the church as Christ's mystical body. He is not discussing the Eucharist.

So the claim is wrong on three counts:
- whose words these are (a modern translator's, not Hus's);
- what Hus was discussing (ecclesiology, not the Eucharist);
- "quotes without dissent" (Hus never quotes this line at all).

This is the misattributed-quote failure CLAUDE.md names as a recurring defect. It appears inside the floor argument, in a sentence written to replace absence-of-denial reasoning.

The floor result does not depend on it. Better evidence in Hus's own voice exists in the same file. These passages appear to be body text, but the reviser must confirm each one is not a footnote before using it:
- "so Christ is the individual, the true God and man, imparting spiritual life and motion to the church"
- "Peter confessed Christ to be very God and very man"
- "she is placed immediately after the Trinity, which is uncreate"

**Fix:** withdraw the Paschasius sentence. Replace it with a verified passage from Hus's own body text, cited to its page.

**R2-S2. The sourcing claims are stale against the current corpus-map (8 works, not 2).** `cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml` now assigns eight works, and all eight source files exist in `cic/texts/`. These were added by a PD acquisition pass after Revision 2:
- Piccolomini, *Historia Bohemica* (1592 Latin printing): a contemporary hostile source on the Hussite wars, which the corpus-map note says can be primary evidence under Mark's Latin-source ruling. It is filed `role: context`.
- Lützow, *Life & Times of Master John Hus* (1909), *The Hussite Wars* (1914) and *Bohemia: An Historical Sketch* (1920): secondary.
- Gillett, *Life and Times of John Huss*, Vol. II (1871): secondary.
- The Unity of the Brethren's own *Ratio Disciplinae* (1632/33, ed. Seifferth 1866): `role: tradition`.

The following statements are therefore no longer true:
- B1 heading, "two substantial works."
- B1: "Every word of the vendored corpus predates or barely opens this world's own 1415–1517 window." Also, "nothing speaks for … the crusade years, or the 1436 Compactata."
- §0: "no Unity primary material is currently vendored."
- Section B conclusion and Tier paragraph: "nothing vendored past 1415" and "the genuinely narrow, pre-1415, single-figure sourcing shape." This is one of the two stated grounds for the Tier being provisional.
- §4 item 2: "nothing vendored covers the movement's own institutional history from the Compactata (1436) onward."

B3's "Lollardy's own vendored Wyclif works (seven volumes)" is also stale. The Lollardy map now holds eight Wyclif-authored works plus the Wycliffite Bible. One of them is Wyclif's own *Tractatus de Ecclesia* (`wyclif_de-ecclesia-lat_loserth1886.txt`), the very treatise Schaff names as Hus's main source. This makes B3's direct-borrowing point stronger. The revision should say so and cite it.

§5's "two works sampled" is a correct historical statement of what this pass did, and may stand.

Revision 2's drafter did not cause this. The acquisition happened afterwards. But these statements change a sourcing conclusion and one of the Tier's two provisional grounds, so the document cannot proceed with them as written.

**R2-S3. The document's stated window, 1415–1517, is superseded by Mark's 2026-09-25 ruling.** The ruling extends the window to about 1632, so that the Unity of the Brethren's own *Ratio Disciplinae* counts as an in-window, own-voice source. The old window runs through the whole document: §1, §0's window-boundary bullet, B1, B5, the Tier paragraph, and §4 items 2 and 5. The §0 Unitas-segment question, B2's "zero primary-source representation" for the Unity, and B5's scale claim all need rethinking under the new window, not just a new date.

This needs a real revision pass, not a targeted line-fix.

It also raises a cross-world boundary question. A separate census entry, `czech-churches-last-century` (Atlas VI.24, Era 7, 1517–c. 1627, "Utraquists and Unitas"), covers overlapping later Unity material. That question has already gone to Mark separately and is not this review's to resolve. The revision may need to wait for his ruling on it.

Note also that the census entry for V.6 itself still reads `dates: "1415-1517"`. That also follows Mark's ruling. It is not this document's fix.

## Minor findings

**R2-m1. The reading-scope disclosure (Round 1 F5) now rests on a misread source.** A1 says: "Per each file's own provenance header, only 'the opening pages and a mid-document sample' were checked — sampling, not a reading."

The headers do not describe how much was read. They describe how much was **spot-checked for OCR quality**: "not independently spot-checked for OCR quality beyond…".

The quoted phrase is also exact only for the *Letters* header. The *De Ecclesia* header reads "the opening pages, a mid-document sample, and the opening of Chapter I."

And the document plainly did more than sample. It ran full-text searches of *De Ecclesia* for utraquism and cites passages from p. 177 of the *Letters* and from Schaff's introduction, p. xxvii.

**Fix:** state the actual method: targeted full-text searches plus passages checked in context, not an exhaustive reading. Cite the headers accurately, as OCR spot-check notes. Round 1's own F5 wording set up this conflation, so this is a refinement, not a relapse.

**R2-m2. The narration strip is incomplete.** Revision-history narration remains in what is meant to be a clean present-tense document:
- A1 heading: "with a correction to what 'vendored and read' actually means"
- §0: "per Revision 2, corrected below (§3 B3)"
- Section A conclusion: "(§0, corrected)"
- Section B conclusion: "(§0, §2 corrected)" and "(§3 B3, corrected)"
- §4 item 1: "corrected at Revision 2 to remove an inaccurate utraquism characterization"
- §4 item 3: "corrected at Revision 2 … rather than the earlier 'indirect influence' framing"
- §4 item 4: "not 'better scanning technology'", which rebuts the old wording
- §4 item 5: "Per §0, corrected at Revision 2"

Also, the Status line now has a stray "(see `Step0_Review_Round1.md`)" attached to the dossier path.

**R2-m3. The Round 1 record the document points to is not on this branch or on main.** The Status line and §6 both send the reader to `Step0_Review_Round1.md`. The file exists only in commit `acd9a888` on `origin/source-research/step0-review-round1`, which has not been merged into this branch (`library-thread/step0-revision2-hygiene`) or into `origin/main`. Until it lands, those pointers lead nowhere.

That commit also carried other fixes: the duplicate REGISTRY.yaml block, the Vaughan/Wyclif Society notes and the Benham publisher correction. Whether those have landed some other way was not checked here. Someone should confirm before the branches diverge further.

**R2-m4. A5 is inconsistent with B3.** A5 still frames the Lollardy link as "the Wycliffe-to-Hus influence line … a contemporary-influence question." B3 now correctly calls it direct textual borrowing. "Contemporary" is also inaccurate: Wyclif died in 1384, and the link runs through his texts, not through contact between the two men. **Fix:** make A5 match B3.

**R2-m5. A leftover methods note is still unfixed (a Round 1 minor).** B1 says "figures below are raw word counts from vendored .txt, not extracted from XML markup." No figures follow anywhere in the document. **Fix:** remove the sentence, or give the figures.

## Outside this document (reported, not fixed)

- **The Hussite dossier is stale, confirming the known fleet-level finding.** `worlds/_cross-world/dossiers/the-hussite-and-bohemian-brethren-movement_Source_Readiness_Dossier.md`:
  - §1 still lists "Two works."
  - §2 still says "None found or expected" for cross-links.
  - §2 and §5 still frame the link to Lollardy as a "contested Wycliffe-to-Hus influence line." The vendored Schaff introduction documents direct borrowing, and Lollardy now vendors Wyclif's *De Ecclesia*.
  - §4 still attributes the 1501 hymnbook to `relationsSummary`. It actually appears in `why`/`longDescription`, so Round 1 F6 was fixed in the Step 0 document but not in its source.
- **Corpus-map notes.**
  - The *Letters* note still says the letters span "his career at the university." They begin in June 1408.
  - Several notes carry process narration: "no prior Source Readiness Dossier or corpus-map presence", "post-Step0-Revision-2 PD source-acquisition pass", and "directly filling the gap the Step0 Revision 2 document's §4 binding item 2 named". Under CLAUDE.md, that belongs in the staging files' provenance or in Ministry, not in canonical notes. `tools/check_live_commentary.py --surface cic-corpus-map` should be run.
  - The *Ratio Disciplinae* note's "directly filling the gap" overstates the case. The gap §4 item 2 named was the 15th-century Unity voice (confessions, catechism, the 1501 hymnbook). A 1632/33 constitution does not supply that, even inside the extended window.
  - Piccolomini is filed `role: context` while its note calls it usable as primary evidence. That is a question for Doc_02.
- **Census V.6 `dates`** still reads 1415–1517 (see R2-S3).

## Confirmed accurate

- **F1 fixed.** §0 quotes `statusWord` and `statusDescription` verbatim against `cic-website/data/world-census.json`. It engages both scope notes (window boundary, Unitas segment), and A3, §5 and the Section A conclusion carry the finding forward consistently. Census `status` "Pre-Survey Candidate" is correct.
- **F2 fixed, not just reworded.** Both Schaff quotes are verbatim in the vendored *De Ecclesia* introduction:
  - "Huss appropriated paragraph after paragraph from his predecessor and transferred them often with little verbal change to his own pages": exact, c. line 1514.
  - "Never did a man owe more to mortal teacher than Huss did to John Wyclif": exact once the page break is closed up. The file breaks it as "Never / [footnotes] / INTRODUCTION xxvii / did a man owe more…".
  - The sources Hus drew on are named in Schaff's footnote as Wyclif's "de Ecclesia and his de potestate Papa[e]". The file's OCR reads "Papa", and the document's normalised title is fine.
  - Letter VI to Richard Wyche (September 1410), "He read it in the Bethlehem", and Workman's "an English Lollard, one Richard Wyche" are all confirmed.
  - §4 item 3 carries the correction forward.
- **F3 fixed** as of the time it was written. It is now overtaken by R2-S2.
- **F4 fixed.** Workman's note at p. 177 matches verbatim ("Hitherto, Hus had taken little interest in the matter — in fact, in his De Coena Domini, written at a later date, he still practically concedes the Roman position"). So does "in the summer of 1414." "Committed to it only late, from prison" is a fair reading: the note sits in the February 1415 Constance prison letters, and Workman adds that "he soon committed himself decisively to the opinions of Jakoubek."
- **F5 partly fixed.** The overstated "read" claim is gone throughout (A1, the Section A conclusion, §4 item 1 and §5 all say "sampled"). R2-m1 is about how the disclosure is grounded.
- **F6 fixed.** A3's `relationsSummary` quote ("A functioning non-Roman national church a century before Luther") is verbatim. The hymnbook is no longer attributed to that field.
- **F7 fixed.** The `sourcing` field is quoted verbatim. The named works (Mladoňovice *Relatio*, Fudge 2002, Unity confessions/discipline/hymnody, Spinka 1972) match the census `sources` array.
- **Round 1 minors fixed:** "uncontested" is removed; "career at the university" is removed from this document; Lollardy's A3 is "carried forward"; the Appeale route is now re-OCR/transcription; "I have appealed to Christ" is verbatim in the *Letters* ("I have appealed to Christ Jesus"). The one unfixed minor is R2-m5.
- **Article 4.** All five quotes match the Constitution's Article 4 text verbatim, apart from typographic quote marks. The repo file is `CiC_L1_Constitution_V2_2.docx`; the "V2.3" citation matches fleet usage.
- **1.4 million characters.** Correct: the two files total 1,410,931.
- **The hygiene pass (`4b4ce830`) is clean on substance.** A line-by-line diff shows no fact, quote, date or citation dropped, softened or altered. Each "Correction (Revision 2)" paragraph was restated as the corrected fact. "Provisional on the same grounds Revision 1 named" became "Provisional on two grounds", and they are the same two grounds. The pass was simply incomplete (R2-m2).

## Disposition

Per `cic-build-cycle`: R2-S1 corrects a misattributed quote inside the floor argument. R2-S2 changes a sourcing conclusion and one of the Tier's two provisional grounds. R2-S3 changes the world's scope boundary. Each meets the bar for substantial revision. Revision 2 does not clear review.

**Required for the next revision:**
1. R2-S1: withdraw the Paschasius footnote quote and substitute a verified passage from Hus's own body text.
2. R2-S2: re-state the sourcing against the current eight-work corpus-map, and re-ground the Tier's provisional conditions on it. Cite Lollardy's vendored Wyclif *Tractatus de Ecclesia* in B3.
3. **R2-S3 (contingent): rewrite the document to Mark's 2026-09-25 window extension (to about 1632).** This is a real scope revision across §0, §1, B1, B2, B5, the Tier paragraph and §4, not a date swap. **It depends on Mark's pending ruling on the cross-world boundary with `czech-churches-last-century` (VI.24, 1517–c. 1627).** The revision should not settle how the later Unity material divides between the two entries before he rules. It may need to wait for that ruling, or name the question as open and binding on Doc_01.
4. R2-m1 to R2-m5, all wording or hygiene.

**Round cap.** This is Round 2 of 3. If Revision 3 fails Round 3 on substance, escalate to Mark rather than attempt a fourth round. R2-S2 and R2-S3 come from events after Revision 2 was written (new vendoring and a new ruling), not from drafting failures. Whether that scope change counts against the cap, or is a change order that resets it, is a governance question for Mark. This review does not decide it.
