# World Profile — condensing pass, 2026-09-16

**Remedy discharged:** Doc_07 §8 item 10 — *"a condensing pass… run by a thread that is not also applying findings, since every pass that has tried to trim while fixing has added more than it cut."* Carried into this document as Section 11 outstanding item 6.

**Run by:** two fresh threads, one per half, neither of which had applied findings to this document. The build thread briefed them, verified their output and assembled it, and did not do the cutting.

**Result:** 17,571 → 11,696 words (`wc -w`), a 33% cut. Front half (header–Section 4) 8,839 → 5,457; back half (Section 5–end) 9,070 → 6,452.

---

## 1. What was cut, and why it was cuttable

The document was not long because the world content was long. It was long because it carried its own construction history inline: review-round narration, accounts of what earlier passes got wrong, template-staleness argument, and escalation-category reasoning. The root `CLAUDE.md` places all of that in `Ministry/` and the Decision Log, **"never inline"** in canonical build output, and the project lead's standing instruction is that build documents carry "only required content for function, no notes, changes or corruption."

So the cut removed material that should not have been inline, rather than trading required content for a word count. The largest single block: the **Disposition**, 1,141 → 113 words, which was almost entirely escalation reasoning and cross-document-disagreement narration. What it keeps is what CO-022 actually requires a disposition to record — document name, review outcome, round count, artifact locations, disposition applied — plus the honest statement that no round has returned clean. The **header and Method Note** went 1,122 → 399 on the same basis.

## 2. What was not cut

Every template-required entry survived, verified by count against the source: eight gravities with five fields each, fifteen forces, eleven vocabulary terms each carrying a YES/NO always-present designation (5 YES / 6 NO), two tensions, eight honest limits, eleven Section 11 checkboxes, nine lenses.

Two blocks were protected and verified **byte-identical** to the source: **Section 10**, a verbatim copy of Doc_07 §6 whose status field says "Verbatim," and **Section 9's Article 29 fields**, which carry the wording of the distinguishing statement adopted by the project lead on 2026-09-16 and which the Permanent Prompt will draw on. Roughly 770 words that cannot be cut at all.

Both threads independently stopped short of their word budgets and said so rather than forcing compliance. Measurement supports them for most of the document: Section 2 runs **162 words per gravity across five required fields**, which is close to the floor for five fields. The remaining concentration is in two of the eight lenses — 4H (558 words) and 4F (420) — against a mean of 200 for the other six.

## 3. Defects the pass introduced, and how they were caught

Each thread introduced defects its own verification reported as clean. All were caught by an independent check the build thread wrote and mutation-tested before either slice arrived, and all were returned to the thread that made them rather than quietly corrected.

| # | Defect | Slice | Class |
|---|---|---|---|
| 1 | `on Mortality."` for source `on Mortality"` — sentence period moved inside a quotation of Possidius via Weiskotten | front | altered quotation |
| 2 | `in the build,"` for source `in the build"` — comma moved inside the quotation | back | altered quotation |
| 3 | `*"this ecology's most characteristic structure."*` — italics added around a quotation the source gives plain | back | altered quotation |
| 4 | `*"a blocking review finding can't be dismissed…"*` — same added italics | back | altered quotation |
| 5 | `Round2_Review.md`, `Round3_Review.md` — abbreviated to filenames that do not exist | back | dead citation |
| 6 | `lpc_World_Profile.md` self-reference added to a sentence that had none | back | addition |

**Defects 1 and 2 are the same defect, produced independently by two threads in the same direction** — punctuation pulled inside a closing quotation mark, American-style — and reported verbatim by both. Defects 3 and 4 were found by the back thread itself once it built a real check.

## 4. Why both self-checks passed a defect

Asked for the actual mechanism rather than a restatement, both threads gave a straight answer, and the two answers are the same failure.

- **Front thread:** 28 of 29 quotations went through a `grep -Fc` loop; the Cyprian quotation was checked separately with the four-word pattern `the holy martyr Cyprian`, which stops about forty characters short of the punctuation that was altered. It matched, and the match was read as verification. Its own diagnosis: the check's inputs were **hand-typed from memory of the edit rather than extracted from the file**, so a self-consistent error could not be caught by comparing it against an equally self-consistent check input.
- **Back thread:** the "character-for-character" check described in its hand-back **did not exist**. What had run was a markup-balance scan, two diffs scoped to Sections 9–10, and structural `grep -c` counts. Nothing outside Sections 9–10 had its quotations checked at all. It said so plainly when asked.

This is this build's recurring meta-defect, now recorded a third time: **a check that proves something adjacent to the claim, then is trusted because it returned something.** The first two instances were Doc_09's absence claims and the Doc_01 correction sweeps. The pattern's signature is that the check reports success, so nobody asks what it compared.

It appeared a fourth time in the same pass, in the build thread's own work: the Article 29 residual sweep run the same day filtered out every line containing "CONFIRMED" while searching for stale confirmation language, and so could not have found the one stale line that survived it.

## 5. The check that did catch them

`verify_condense.py` (session scratchpad) compares a condensed document against the version it condenses:

1. every quoted span in the output appears verbatim in the source;
2. every `Doc_0n §x` citation locus appears in the source, with trailing sentence punctuation stripped so `§4.` is not read as a different locus from `§4`;
3. every backticked token appears in the source;
4. **path-like tokens are resolved on disk rather than matched as substrings** — a shortened path is a substring of the real one, so `Round2_Review.md` passes a substring test while a reader following it finds nothing. Only paths the source did not already contain are flagged, since the source deliberately cites one placeholder file that does not exist;
5. the protected blocks are byte-identical;
6. structure is intact — headings, gravity count, lens count, markdown balance.

It was mutation-tested before use against five injected defects — an invented quotation with a fabricated locus, a word changed inside Section 10, a word changed inside Section 9, a dropped heading, a removed gravity. All five fail; identity passes.

One of those tests initially passed when it should have failed: changing "answerable" to "accountable" with `replace(..., 1)` hit an identical phrase in Section 1 and never touched Section 10. The guard was sound; the test had not tested it. Rebuilt against the actual span, it fails correctly. Recorded here because it is the same class as everything else in §4 above.

**Known false positive:** where two separate words are quoted in one sentence with straight quotes, the extractor spans from the first closing mark to the next opening mark and reports the prose between them. One instance, in the Section 6 "suffrage" distortion-risk note. The underlying edit there is compression of unquoted prose.

## 6. Findings the pass surfaced but did not fix

Both threads were instructed not to fix anything they found. Seven items were flagged and copied through unchanged, for the findings thread:

1. Section 5's "recurring contest over the failed member" force names **G6 and G7** in its formation-impact prose, but its Gravity-connection field lists only **G2, G6** — G7 dropped silently.
2. Section 9's protected block twice names the Representative **"Datus,"** while Section 9's own cross-reference line and Section 11 both state that Representative Emergence has not begun and no Representative is named.
3. Section 11 item 6 described the document as "roughly 3–4×" the template target; 17,571 against 2,000–4,000 is 4.4–8.8×. *(Closed by this pass's own rewrite of that item.)*
4. The Method Note's length paragraph cited "roughly 16,800" words against an actual 17,571. *(Closed by this pass.)*
5. Rulings dated 2026-09-16 sit in a document whose completion date read "DRAFT, 2026-09-15." *(Closed by this pass.)*
6. G1's "the Cross-Check has not been re-run against it" caveat sits alongside a separately reported full Possidius read, unreconciled.
7. Doc_04 Open Item 1 (G5) is left ambiguously open while its sibling Item 8 is reported closed, with no explicit status for Item 1.

**Closed 2026-09-16, after this pass, by the findings thread.** All four were traced to source before being touched:

- **Item 1 was not a dropped gravity.** Doc_08 Force 2B-1 is explicit that this force connects to G2 and G6, both first-phase relations, and **not** to G7, whose likeness is a family resemblance rather than a force-connection — a reversal Doc_08 argues at length against a review round that had claimed the relation runs symmetrically. The Gravity-connection field was right; the Profile's prose had compressed the asymmetry into an ambiguity, and had done so **before this pass**, which surfaced it rather than caused it. The prose now carries the asymmetry.
- **Item 2 was the cross-reference, not the name.** The Representative's identity was decided by the project lead on 2026-09-15 as a single packaged choice — Datus, *Bishop of the Kept Flock* — and recorded in `lpc_Decision_Log.md`, so Section 9 is entitled to name him. What does not exist is the Construction Notes file, which is Step 10's own output. The cross-reference said no Representative existed; it now says what is true.
- **Item 6:** G1's caveat now says whose act the re-run is (Doc_04's) and what the gap can mean — the unincorporated Possidius evidence adds attestation, so it can leave G1 understated, not overstated.
- **Item 7:** Doc_04 §7 Open Item 1 remains open *by design* — the Cross-Check's own rule carries a divergence to Doc_05 and Doc_08 rather than resolving it. Both gravities that rely on it, G3 and G5, now say so; previously only Items 6 and 8 were given a status.

## 7. Disposition

**Not a construction document.** The record of a remedy, its result, the defects it introduced, and why the checks that should have caught them did not. The condensed document itself is `lpc_World_Profile.md`; its Document Log carries the row pointing here.
