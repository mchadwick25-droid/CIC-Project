# Doc_07 — Integrated Ecology Analysis: Latin Pastoral-Congregational Christianity
## Round 2 Independent Adversarial Review — targeted recheck

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-15.

**Document under review:** `Doc_07_Integrated_Ecology_Analysis.md` at `2c012d08` (272 lines; 6,376 words by Round 1's own counting method — measurement below). REVISED after Round 1; not disposed.

**Scope.** Targeted recheck per `CLAUDE.md` ("from round 2 onward, do a targeted recheck — only what changed, against prior findings"). I reviewed **the diff, not a summary of it**: `git diff a750b783..2c012d08` across all three touched files (`Doc_07`, `Doc07_Round1_Review.md`, `lpc_Decision_Log.md`). I hold no prior position on Round 1 and did not write it or the document.

---

## What I checked, and how — stated so it can be re-run

**The diff itself.** `git diff a750b783..2c012d08 -- World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_07_Integrated_Ecology_Analysis.md` — twelve hunks, read in full, each classified as fix, trim, or both. Pre-fix text recovered with `git show a750b783:<path>` and compared site by site.

**Per-hunk word accounting**, to test the fix pass's own arithmetic. Word deltas computed per hunk with Round 1's own regex (`[A-Za-z'’]+`) over added and removed lines separately.

**Word count, two independent methods** (`CLAUDE.md`: "truncation checks use two independent methods, not one"), plus a third prose-only pass excluding table rows, headings and horizontal rules.

**Every Round 1 finding verified at the governing source, not against the fix pass's account of it:**
- H1 → `Doc_01_World_Identification_Boundaries_Orientation.md` §7 read in full at source, including its two in-place self-corrections.
- M1 → `World-Builds/Donatism/Doc_07_Integrated_Ecology_Analysis.md` §2B, §2C, §2E read at source; the new quotation character-compared against §2C's own opening line; `grep -n "richest\|concretely, repeatedly"` re-run across that document.
- M2 → `Doc_04_Gravity_Discovery.md` §7 Open Items 2, 6 and 8 and §3 Candidate 5 read at source; `Review-Artifacts/Doc04_Round9_Review.md` read for what it actually holds; the 2026-09-14 project-lead ruling traced in `lpc_Decision_Log.md`.
- L1 → `CiC_L3A_Forces_Framework_V1.1.docx` unzipped, `word/document.xml` tag-stripped, the sentence located at source (two occurrences) and character-compared.
- L2 → `Doc_02_Source_Ecology.md` §9 items 2 and 3 read in full.

**Every quotation re-verified with the mechanical `<note>` remedy applied.** `cic/texts/npnf101_augustine-confessions-letters.xml` and `npnf104_augustine-anti-manichaean-anti-donatist.xml` were read with `<note>…</note>` spans **marked before tags were stripped** (`re.sub(r'<note\b[^>]*>(.*?)</note>', '⟦NOTE:…⟧', x, flags=re.S)`, then tag-strip, then `html.unescape`), so that editorial matter is visibly separated from the source's own voice. This found one instance — see NEW-L4.

**Governing documents read as standard:** `L4-Templates/Integrated_Ecology_Analysis_Template.md` (full, including Section 6's four required sub-elements and its Target length line); `reference/method/CiC_World_Build_Completion_Standard_V1.3.md` §F (quoted at source); `CLAUDE.md`.

**House-form controls, opened directly rather than assumed:** `Doc_05` and `Doc_06` Document Logs and Dispositions in this world; `World-Builds/Donatism/Doc_07_Integrated_Ecology_Analysis.md` §7 and section map.

### Three checks that failed and were confirmed before being trusted, per the assignment's own instruction

**(1) "§8's items were renumbered when two were merged." They were not, and the document is not the defective party here.** I listed §8's items in the pre-fix and post-fix versions side by side. Pre-fix: items 1–9. Post-fix: items 1–9, one-to-one, same subjects in the same order. What actually happened is the opposite of a merge of two existing items: the **new** Open Item 8 material was folded **into** existing item 6 (the *Gesta*), which already existed and kept its number. **No item was lost, nothing was renumbered, and every §8 item is accounted for.** The premise I was handed was wrong; I report that rather than manufacture a finding to match it. (One cross-reference into §8 does dangle, but for a different reason — NEW-L1.)

**(2) Doc_01 §7's "two of three strands" sits next to an in-place correction notice that quotes an earlier draft's error as "two of its three strands."** My first read flagged Doc_07's paraphrase as repeating a claim Doc_01 had withdrawn. Before reporting it I traced the correction: Doc_01 §7's correction concerns the **state-power** claim (which strands ground authority in the state relationship), not the **primacy** claim. Doc_01's own corrected, live text then states that the primacy question is *"constitutive* of two of IJC's own three strands' own stated grounds." Doc_07's paraphrase is of the live sentence, not the withdrawn one. **The defect was in my check, which matched a remembered shape inside a correction notice rather than testing the claim at the site where it is used.**

**(3) The `[A]` bracket in §4's new Forces Framework quotation.** The source reads "A gravity that cannot be connected…" with a capital A at sentence start, so I first read the bracket as signalling a case change that did not occur. Confirmed against this document's own established convention at §1 (`"[A]sk all of Smart's seven dimensions…"`), which Round 1 read the same way: here brackets mark a **retained** capital carried into a subordinate position. Consistent, not a defect.

---

## VERDICT: REVISION REQUIRED

**Findings: 1 HIGH · 4 MEDIUM · 6 LOW · 3 COSMETIC — 14 in total.**

**All five Round 1 findings are genuinely fixed at the site, and I verified each at the primary source rather than accepting the fix pass's account.** The analytical substance of this document — the gravity spine, the seven-dimension coverage, the forces integration at §2H and §4, the §2G reconstruction, the cross-lens synthesis — is unchanged and holds. That is the bulk of the deliverable and it is sound.

**What the fix pass broke is the document's account of itself.** The Round 1 review and the fix pass were logged in `lpc_Decision_Log.md` and **not in the document**, leaving the Disposition asserting "No review round has been run against this document" in the same commit range that adds the review artifact. Four of the six trims cost something real: a blanket assurance at §1 now contradicts new material at §2D; the only expansion of three neighbouring worlds' names is gone; the only statement of the build-cycle rule being departed from is gone and is replaced by a pointer to a section that does not carry it; and a strengths clause was replaced by a cross-reference that does not hold. One cross-reference now points at an item number that does not exist. The new Open Item 8 material states a named review artifact's holding backwards.

---

## Round 1's five findings — status

| # | Round 1 finding | Status |
|---|---|---|
| H1 | §2E claimed to sharpen Doc_01's World #6 boundary without engaging Doc_01 §7 | **FIXED** (one LOW residue, NEW-L2; one COSMETIC, NEW-C1) |
| M1 | "among its richest" attributed to Donatism's Doc_07, which does not say it | **FIXED** |
| M2 | Doc_04 §7 item 2's fourth clause (Open Item 8) not carried | **FIXED** (the new material misstates the finding — NEW-M2) |
| L1 | A paraphrase printed as a verbatim Forces Framework quotation | **FIXED** |
| L2 | "Doc_02 §5, §9 items 2–3" overstated item 3's support | **FIXED** (one COSMETIC, NEW-C2) |

**H1 — FIXED.** §2E is rewritten in three paragraphs. It now cites Doc_01 **§7** by name, quotes it, and withdraws the "sharper" framing explicitly ("**An earlier draft claimed to *sharpen* Doc_01's boundary while citing only §1 and never opening §7**"). The mischaracterization Round 1 asked to be removed — that Doc_01 framed the boundary as "a contrast between a legal world and a non-legal one" — is gone. Checked at source in Doc_01 §7: *"episodic"* ✓ verbatim (Doc_01 italicizes it); *"one recurring pressure among several on this world's own ordinary pastoral office, not the axis this world's own ecology is organized around"* ✓ verbatim; "roughly two years of Cyprian's ten-year episcopate, plus the Apiarius affair" ✓ a faithful compression of Doc_01's "roughly two years of Cyprian's ten-year episcopate, and the Apiarius affair (419, running to c. 426) as one recurring episode within Augustine's own thirty-five-year episcopate"; "constitutive of two of IJC's three strands" ✓ an accurate unquoted paraphrase of Doc_01's live text (see failed check 2). §5's echo was corrected in the same pass ("§2E's added axis"). **Is "additional rather than sharper" honest? Substantially yes** — the framing is stated three times, "neither subsumes the other" is stated flatly, and the earlier overreach is named on the record. One clause still claims a comparative advantage it has not earned; that is NEW-L2, not a reopening of H1.

**M1 — FIXED, and better than the fix Round 1 asked for.** §2C no longer uses a superlative. The replacement quotes Donatism's own Doc_07 §2C opening line. Character-compared at source: Donatism §2C reads *"a specific, growing body of self-narrated story — not myth in the sense of invention, but the structured account this world told of its own founding and its own dead, distinct from the doctrinal argument built on top of it."* Doc_07 renders *"a specific, growing body of self-narrated story… the structured account this world told of its own founding and its own dead,"* — **both retained spans are verbatim, the elision is marked, and the comma after "dead" is the source's own.** The corrective parenthesis is also accurate: `grep` over Donatism's Doc_07 returns exactly two hits, §2B's *"the richest emotional evidence in this world's own vendored corpus"* and §2E's *"the single most concretely, repeatedly evidenced dimension in this document."* The substantive contrast survives without the superlative, exactly as Round 1 said it could.

**M2 — FIXED at the compliance level.** Doc_04 §7 item 2's fourth clause reads, at source: *"and note that Open Items 6 and 8 may both bear on the classification."* §2D now carries both; §8 item 6 carries both; §2D names item 2 as the binding instruction. All four clauses are now discharged. **But the new material states Round 9's holding backwards — see NEW-M2.**

**L1 — FIXED.** The Forces Framework sentence located at source in `CiC_L3A_Forces_Framework_V1.1.docx`, `word/document.xml` tag-stripped: *"A gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete."* (two occurrences, in the Layer-3 and gravity-assessment passages). §4 now reproduces it exactly, with the retained-capital bracket this document already uses at §1. The compressed label "incomplete ecology" no longer appears in quotation marks anywhere. (It survives, correctly unquoted and as the document's own descriptive label, at §8 item 2.)

**L2 — FIXED.** §2G now reads "Doc_02 §5 and §9 item 2; §9 item 3 concerns two recalled-from-field-knowledge secondary rows and is cited here only for the priority-review flag it carries, not for the site-report claim." Checked against Doc_02 §9 item 3 at source: rows 34 and 35 (Fahey, Rebillard) are indeed "recalled from field knowledge… flagged for priority review," and item 3 explicitly routes row 38's own flag elsewhere — "at §5's closing sentence and §9 item 2," which is exactly where §2G now cites. Precise and correct. One count is off — NEW-C2.

---

## NEW findings

## HIGH

### NEW-H1 — The Disposition states that no review round has been run against this document. One has, and the review artifact is committed in the same range as the fix pass

**Site:** Doc_07 Disposition (line 268): *"**Not disposed.** No review round has been run against this document. A build thread does not score its own work as passing."* And the Document Log (lines 260–262), which carries exactly one row: *"2026-09-15 | Initial draft | — | Step 7 deliverable produced."*

**What I found.** `Review-Artifacts/Doc07_Round1_Review.md` was added at `4cf937b7`, inside this fix pass's own commit range, returning REVISION REQUIRED (1H 2M 2L 0C), and all five findings were applied to the document in the same commit. The commit message at `2c012d08` reads "log the Round 1 fix pass" — and it logged it in `lpc_Decision_Log.md`, whose new entry closes *"**Status.** `Doc_07_Integrated_Ecology_Analysis.md` is **REVISED after Round 1 — not self-disposed.**"* **None of that reached the document.** The sentence a reader of Doc_07 alone encounters is false on its face, and false in the governance section, about the document's own review history.

This is not a house-form ambiguity. Both controls in this world go the other way, and both are documents in exactly this condition — reviewed, revised, undisposed:
- `Doc_06_Full_Lexicon_Development.md` Disposition: *"**Not disposed.** `Review-Artifacts/Doc06_Round1_Review.md` returned **REVISION REQUIRED** (3H 3M 2L 0C) and judged the deliverable adequate to proceed to Doc_07 after one narrow fix pass; that pass is this one…"*
- `Doc_05` and `Doc_06` Document Logs both carry a row per review round and a row per fix pass. Doc_06's runs to seven rows across three rounds.

Doc_07's own §1 input table applies the same discipline to its inputs — "REVISED after Rounds 1–3, not self-disposed" — while the document declines to say it of itself.

**Why this matters.** `CLAUDE.md`: "A record marked 'quotes verified' is a claim to re-check, not a fact to trust" — the governing concern is self-reporting accuracy, and this is a self-report that is simply untrue. It also breaks the audit trail at the one place a disposing reader looks. A document asserting that no review has been run cannot be disposed on the strength of two reviews, and the next reviewer or the project lead has no in-document record that Round 1 happened at all. The fix pass updated the Decision Log and left the deliverable contradicting it.

**Fix.** Two edits, both mechanical. (a) Document Log: add `| 2026-09-15 | Round 1 review | Review-Artifacts/Doc07_Round1_Review.md | REVISION REQUIRED — 1H 2M 2L 0C; adequate to proceed to Doc_08 |` and `| 2026-09-15 | Round 1 fix pass | — | All five findings applied |`, plus rows for this round. (b) Disposition: replace "No review round has been run against this document" with the Doc_06 form — name the round, its verdict, its counts, and that the pass applying it is this one — keeping the existing "A build thread does not score its own work as passing."

---

## MEDIUM

### NEW-M1 — §1's blanket assurance that no open finding bears on a claim made here is now contradicted by §2D, which the same fix pass added

**Site:** §1 (line 31, untouched by the fix pass): *"**No open finding against any of the three bears on a claim made here**, and §8 lists what is open rather than leaving the reader to reconstruct it."* Against §2D (line 95, added by the fix pass): *"**This document does not run it and does not treat the Supporting classification as beyond question**."*

**What I found.** Doc_04 is one of "the three." Doc_04 §7 Open Item 8 is an open finding against it. Doc_04 §7 item 2 says in its own words that Open Items 6 and 8 "may both bear on the classification," and §2D now states that the classification is not beyond question. G5's Supporting classification **is** a claim made in this document — it is asserted in the gravity spine at §2 ("Supporting — … **G5** Conciliar Authority Theory"), relied on at §2D, §2E, §3C, §4 and §8 item 2. So an open finding against one of the three does bear on a claim made here, and the document now says so in one section and denies it in another.

**Why this matters.** §1's sentence is load-bearing: it is the specific assurance that licenses proceeding on three undisposed inputs, offered "so a reviewer can check it rather than take it on trust." The fix pass added the material that falsifies it and did not revisit the assurance. This is the M2 fix creating an M1-shaped defect two sections upstream.

**Fix.** Narrow §1's sentence to what is true and let §2D be the exception it names — e.g. "No open finding against any of the three changes a lens finding below; the one that bears on a classification this document carries is Doc_04 §7 Open Item 8, disclosed at §2D and §8 item 6."

### NEW-M2 — §2D states `Doc04_Round9_Review.md`'s holding backwards: Round 9's determinate answer *is* Supporting, and it expressly does not revisit the classification

**Site:** §2D: *"`Doc04_Round9_Review.md` holds that **a determinate Framework classification for G5 is reachable from Doc_04's own premises and has not been run**, and Doc_04 records that finding as unaddressed. **This document does not run it and does not treat the Supporting classification as beyond question** — that classification rests on the project lead's ruling of 2026-09-14, and the open argument that it could be settled on the document's own evidence remains open."*

**What I found.** The first clause is accurate and tracks Doc_04 §7 item 8's own wording. The inference the sentence then invites is the reverse of what Round 9 holds. Read at source:
- Round 9, stated up front: *"**Candidate 5's classification is the project lead's ruling and is not revisited here.** What is tested here is the document's stated *warrant* for how it records that ruling."*
- Round 9's H4, the finding Open Item 8 carries: *"On the Framework's own three classes, **Supporting is what remains**, narrowly, and the document could say so — provisionally, on the search bound — **in one sentence that agrees with the ruling.**"*
- Round 9's own model sentence: *"The project lead's ruling of 2026-09-14 settles it as Supporting, and this document's own testing is consistent with that rather than silent about it."*

Running the argument Open Item 8 names would **confirm** Supporting, not unsettle it. It is a finding about Doc_04's reasoning, not about whether the label is right. §2D presents it as a reason to hold the Supporting classification open to question.

§2D also drops Doc_04 §7 item 8's own qualification, which sits in the same item it is carrying: *"**§3 excludes Primary explicitly; it does not currently exclude Tensional** — that exclusion was made in an earlier version and is recorded at `Doc_04_Superseded_Claims.md` §1.2, so the review's second premise is not presently stated by this document."* A reader of §2D alone learns that a determinate answer is available and unrun, and does not learn that Doc_04 itself records one of its premises as not presently stated.

**Why this matters.** This is the same defect class as Round 1's M1 — a named document's holding reported as something it does not hold — at the exact site created to discharge a binding instruction. It is also the fourth Candidate-5 mis-statement in this world's record (Round 9's H4 and H6 are two of the others), which is why it is worth stating precisely rather than waving at.

**Fix.** Two sentences: "Round 9 holds that a determinate Framework classification is reachable from Doc_04's own premises and has not been run — and that the answer it reaches is Supporting, agreeing with the ruling rather than disturbing it; its finding is about Doc_04's stated warrant, not about the label. Doc_04 §7 item 8 records the finding as unaddressed and notes that one of its premises is not presently stated by that document. This document runs nothing and carries the item forward."

### NEW-M3 — The §5 trim deleted the only expansions of three neighbouring worlds' names, and the §2E rewrite introduced "IJC" without ever expanding it

**Site:** §5, before: *"Against **World #6 (Imperial and Juridical Christianity)**… Against **World #9 (Hieronymian ascetic-literary)** and **World #2 (Alexandria)**…"* After: *"Against **World #6**… Against **Worlds #9 and #2**…"* And §2E, added by the same pass: *"where it is constitutive of two of **IJC's** three strands."*

**What I found.** `grep -n "IJC\|Imperial\|Hieronymian\|Alexandria"` over the whole document returns **two lines**: §2E's single unexpanded "IJC", and §5. **The document now never names Imperial-Juridical Christianity, the Hieronymian world or Alexandria in words anywhere.** "IJC" occurs exactly once and is never introduced. World #4 kept its gloss ("Donatism"), so the section is internally inconsistent as well as opaque.

**Why this matters.** The template's Section 4 requires distinctiveness stated "in comparison to neighboring worlds in the same period," and Doc_07 is a required input to Doc_08, the World Profile and Representative emergence — readers who are not holding Doc_01 open. `CLAUDE.md`'s writing standard also asks that "technical terms [be] introduced before they're used naturally." An unexpanded three-letter code used once, in the document's most-cited boundary argument, is the opposite. This is the trim costing something real: the words saved here are 25, against the 136 the new length disclosure spent.

**Fix.** Restore the glosses at §5's first mention of each world, and expand IJC once at §2E's first use ("Imperial-Juridical Christianity (World #6, 'IJC' below)").

### NEW-M4 — The Disposition trim removed the only statement of the build-cycle rule departed from, and points at a §1 that does not carry it

**Site:** Disposition, before: *"**The build-cycle departure, stated plainly rather than worked around.** `cic-build-cycle` provides that a document must reach at least *Approved to proceed* before the next begins. **Three have not**, because escalation categories are open against each and CO-022 forbids a build thread from self-disposing in that condition…"* After: *"**The build-cycle departure** is stated at §1 and not restated here."*

**What I found.** `grep -n "build-cycle\|departure"` over the document returns **one line** — the Disposition's own pointer. **§1 contains neither phrase.** §1 states the facts that constitute the departure (three inputs undisposed; CO-022; the project lead's direction) but never names the rule, never says a document must reach *Approved to proceed* before the next begins, and never says a departure from the cycle occurred. The same pass also cut §1's "The L4 template asks whether all six inputs were confirmed complete before lens work began," which was the other place the gate's own terms were stated. So the cross-reference does not resolve, and the disclosure is thinner than it was in both places at once.

The house control is decisive and is in this world: `Doc_06`'s Disposition carries the full form — *"`cic-build-cycle` provides that a document earlier in the sequence must reach at least *Approved to proceed* before the next begins, and that a document against which any escalation category applies **is not self-disposable by the build thread**… **That is a real departure from the cycle, and it is recorded here rather than smoothed over.**"* Doc_07 had that paragraph before this pass and does not have it now.

**Why this matters.** The assignment's standing instruction is not to re-litigate the departure but to judge whether §1 and the Disposition still record it honestly. **They record it less honestly than before.** Nothing false is asserted, but the one sentence that told a reader *what rule was broken* is gone, replaced by a pointer to a section that does not supply it. On a document whose central integrity claim is that it "does not pretend otherwise," that is the wrong trim to have made.

**Fix.** Either restore the deleted sentence to the Disposition, or move it into §1 so the pointer becomes true. Do not leave the pointer standing as it is.

---

## LOW

### NEW-L1 — §2D's "Carried at §8 item 6a" points at an item that does not exist

**Site:** §2D, final sentence of the new paragraph: *"Carried at §8 item 6a."*

**What I found.** §8 runs items 1–9 with no sub-items anywhere. The Open Item 8 material is carried at **§8 item 6**, which the same §2D paragraph names correctly three sentences earlier ("is carried at §7 and §8 item 6"). I verified the numbering directly in both the pre-fix and post-fix versions: nine items before, nine after, one-to-one, nothing renumbered. The "6a" is an artefact of drafting, not of a renumbering that happened.

**Fix.** "Carried at §8 item 6."

### NEW-L2 — §2E's "the wider one holds even where the primacy question is not live" misreads what Doc_01 §7's finding is a finding about

**Site:** §2E: *"**The two are compatible and neither subsumes the other**, though the wider one holds even where the primacy question is not live, which on §7's own finding is most of this world's span."*

**What I found.** Doc_01 §7's conclusion is not a claim that operates only while the primacy question is live. It is: *"the primacy question is one recurring pressure among several on this world's own ordinary pastoral office, not the axis this world's own ecology is organized around."* That is a claim about how the ecology is organized across the whole span — and §7 uses the episodicity of the primacy question as the **evidence** for it. So §7's boundary claim is at its strongest precisely where primacy is not live; it does not go dormant there. §2E's clause inverts that, presenting §7's axis as intermittent and its own as continuous, which is a comparative advantage claim dressed in the language of compatibility. It is also the one clause in the rewritten §2E that pulls against the paragraph's own stated posture two sentences earlier.

**Why this matters.** Narrow, and it does not reopen H1 — the rewrite is substantially honest and names the earlier overreach. But it is the residue of the same instinct, in the same section, and it is the kind of clause a reader checks against §7 and finds does not hold.

**Fix.** Delete from "though" to the end of the sentence, or restate: "the two axes answer different questions — how central the primacy contest is, and what the legal machinery is for — and §7's finding holds across the span rather than only where the contest is live."

### NEW-L3 — §7's "beyond what §5 already states" is not true of three of the four strengths it replaced

**Site:** §7, before: *"**What the gaps mean for the Representative.** Rich on pastoral reasoning, on the mechanics of failure and restoration, on sacramental argument, and on the texture of a bishop's answerability. **Naturally and unfixably thin** on: …"* After: *"**What the gaps mean for the Representative**, beyond what §5 already states: this voice is **naturally and unfixably thin** on…"*

**What I found.** §5's Representative paragraph reads: *"A voice that reaches for a case rather than a story (§2C), that argues from pastoral consequence, that can hold a sharp disagreement without treating the other party as outside, and that will not let one test decide a person."* Mapping the deleted clause against it: "pastoral reasoning" ✓ is covered ("argues from pastoral consequence"); **"the mechanics of failure and restoration," "sacramental argument," and "the texture of a bishop's answerability" are not in §5** and are now stated nowhere in the document as Representative-facing strengths. The trim saved 16 words and replaced the content with a pointer that holds for one item in four.

**Why this matters.** The template's Section 6 asks for gaps, not strengths, so nothing *required* was removed — this is not a compliance failure. But it is a cross-reference that does not resolve, introduced by a trim, which is what the recheck was asked to look for.

**Fix.** Restore the clause, or narrow the pointer to what §5 actually carries ("beyond the positive picture at §5").

### NEW-L4 — §2G prints *ad nostra subsellia* from an NPNF `<note>` span without marking it as editorial; the Latin is genuine, and this world's own practice is to check that

**Site:** §2G: *"the bishop withdrawing to his own seat (*ad nostra subsellia*)"*, cited to Letter CXXVI.

**What I found.** Reading `npnf101_augustine-confessions-letters.xml` with `<note>` spans marked before tags were stripped, the passage reads: *"I left the multitude, and returned to my own seat.**⟦NOTE: Ad nostra subsellia. ⟧** Thereupon, they being made for a little while to pause…"* — **the Latin tag is inside a `<note>` element. It is 19th-century NPNF editorial apparatus, not the letter's own words**, and Doc_07 presents it in italics in a parenthesis directly alongside two spans that *are* the letter's own words, with no marking of the difference.

**The substance is sound and I confirmed it independently.** The phrase is genuine Augustine: `cic/texts/augustine_epistulae-124-184a-lat_goldbacher-csel44.txt` lines 467–468 read *"…ad / nostra subsellia relicta turba redieram…"* So nothing is fabricated and nothing is mistranslated — what is wrong is undisclosed provenance, on a document that had a better source vendored and did not cite it.

**Why this matters.** This world has seven documented instances of 19th-century editorial matter quoted as the world's own voice, and this world's own remedy is already in operation: Doc_06's Disposition records that "Round 3 then verified the nineteenth chunk's eight quotations individually, **each outside every `<note>` span**." Doc_07's one Latin tag is inside one. It is pre-existing rather than introduced by the fix pass, and Round 1 saw the note and did not draw the consequence.

**Fix.** Cite the Latin to CSEL 44 (`Ep. 126`, "ad nostra subsellia relicta turba redieram"), which is vendored, or mark it as the NPNF editor's note. Do not leave it reading as the letter's own.

### NEW-L5 — §7 omits the template's required "What external scholarly review should focus on" element, which the sibling world's Doc_07 carries on the same house form

**Site:** §7 Gaps and Limits.

**What I found.** The template's Section 6 has four required sub-elements: optional lenses not applied; where required lenses produced thin analysis; what the gaps mean for the Representative; **and "What external scholarly review should focus on: [which synthesis judgments in this document are most uncertain and most in need of expert validation…]."** Doc_07 §7 carries the first three and not the fourth (`grep -n "external scholarly\|scholarly review"` returns nothing). `World-Builds/Donatism/Doc_07_Integrated_Ecology_Analysis.md`, built on the same M4 spine and the same 1–8 house section numbering, **does** carry it at §7 — so this is not the deliberate template departure that was ruled on, and not a house-form difference.

**Why this matters.** It is the one Section 6 element that routes this document's own most-synthetic claims to a specialist, and this document has obvious candidates for it — §2A's rite-generates-doctrine finding, §5's "three descriptions of one mechanism," §2D's refusal-of-the-single-test shape, all of which are the builder's synthesis rather than any source's statement. Pre-existing rather than introduced here; Round 1 certified "Template's other requirements" as met and missed it.

**Fix.** One paragraph at §7, naming the two or three synthesis judgements most in need of expert validation.

### NEW-L6 — The length disclosure's "roughly 350 words of genuine redundancy were cut" is not supported by the diff

**Site:** §1's length disclosure: *"**Roughly 350 words of genuine redundancy were cut in the same pass rather than letting the additions simply accumulate**."*

**What I found.** Per-hunk word deltas across the whole diff, computed with Round 1's own regex:

| Site | added | removed | net |
|---|---|---|---|
| §1 length disclosure | 136 | 0 | +136 |
| §1 gate paragraph | 73 | 115 | **−42** |
| §2C (M1 fix) | 191 | 113 | +78 |
| §2D (Open Item 8) | 121 | 0 | +121 |
| §2E (H1 fix) | 265 | 138 | +127 |
| §2G (L2 fix) | 111 | 83 | +28 |
| §2I lens roll-call | 66 | 80 | **−14** |
| §4 (L1 fix) | 125 | 102 | +23 |
| §5 neighbours | 110 | 135 | **−25** |
| §7 Representative | 68 | 84 | **−16** |
| §8 carried items | 246 | 225 | +21 |
| Disposition | 37 | 81 | **−44** |
| **Total** | | | **+393** |

The five trim sites net **−141 words**, not 350. (They delete 495 words of prose and re-add 354 in compressed form; neither figure is 350 either.) The additions the findings required total +534, and 534 − 141 = 393, which is exactly the document's measured growth — so 141 is the whole of what the trims saved.

**Why this matters.** Small in itself, but this sentence sits in a paragraph whose entire purpose is to let a reviewer check numbers instead of measuring ("disclosed rather than left for a reviewer to measure"). A figure in that paragraph that does not survive the check is worse than no figure.

**Fix.** "Roughly 140 words of redundancy were cut in the same pass," or drop the number.

---

## COSMETIC

**NEW-C1 — §2I still says the lens work "confirms and **sharpens**" Doc_01 §1, and points at the §2E that now disavows the word.** §2I (untouched): *"Doc_01 §1 names this formation logic as 'pastoral and sacramental before it is juridical,' and the lens work above both confirms and sharpens it **(§2E)**."* §2E (rewritten): *"**this lens should not be read as correcting it** — §2I resolves the two directly."* The two are not strictly contradictory — sharpening is not correcting, and §2E's disavowal is about the *boundary* claim — but a reader following §2I's own pointer lands on a passage that spends a paragraph withdrawing that verb. *Fix:* §2I → "both confirms it and states its mechanism (§2E)."

**NEW-C2 — §2G's "two recalled-from-field-knowledge secondary rows" undercounts Doc_02 §9 item 3.** Item 3 flags rows 34 and 35 (Fahey, Rebillard) **and** rows 46–47 (Clarke, van der Meer — "both are recalled from general field knowledge and each is flagged in its own row for priority second-opinion review"), and separately discusses row 38. Four flagged, not two. The count is inherited from Round 1's own description of item 3, so the fix pass reproduced a reviewer's compression rather than re-reading. *Fix:* "several recalled-from-field-knowledge secondary rows."

**NEW-C3 — the stated overage percentage is a shade low, and "allowance" overstates what the template's phrase grants.** Measured below: 6,376 words, which is **+6.3%** over 6,000, not "some 5–6%" (the document's own round figure of 6,350 yields 5.8%, which is where the band comes from). Separately, the template's line is *"**Target length:** 3,000–6,000 words depending on world complexity"* — that phrase governs where inside the band a world lands, not permission to exceed the top of it. Calling it "the template's own… allowance" for a 6% overrun claims a warrant the template does not give. The paragraph is otherwise honest: it states the overage plainly, gives the reason, and says "Recorded as a judgement, not an oversight." *Fix:* "some 6% over the top of the template's stated 3,000–6,000 target — a judgement, not an allowance the template grants."

---

## The word-count disclosure, measured independently

The document now discloses its own length, and the assignment asked for that to be measured rather than accepted.

| Method | Result |
|---|---|
| Round 1's own regex, `len(re.findall(r"[A-Za-z'’]+", text))`, whole file | **6,376** |
| `wc -w` / `len(text.split())` | 6,419 / 6,524 |
| Prose only (table rows, headings and horizontal rules excluded), same regex | 6,187 |
| Pre-fix draft, method 1 (reproduces Round 1's 5,983 exactly) | 5,983 |

**Verdict on the disclosure: substantially honest, with one small inaccuracy (NEW-C3) and one unsupported number (NEW-L6).** "Roughly 6,350" sits within **0.4%** of the method-1 count on the same method Round 1 used and the Decision Log's own progression (6,197 → 6,309 → 6,343) tracks, so the round number is not a way of avoiding a figure. The self-referential reasoning given for rounding — that stating the count changes the count — is true and correctly reasoned. The document is genuinely over the template's target, says so, and does not hide it. What it gets wrong is the percentage by a few tenths, the warrant it claims for the overage, and the size of the cut it made.

---

## Explicit verdict on the trims: they cost something

**Four of the six trims cost something real; two cost nothing.**

| Trim | Verdict |
|---|---|
| §1 gate paragraph (−42) | **Cost.** Removed the statement of what the gate asks. Combined with the Disposition trim, the document no longer states anywhere what rule it departed from (NEW-M4). The CO-022 substance, the three-of-six count and the project lead's direction all survive intact; the arithmetic ("three categories… across eight items" = 3 portfolio + 4 governance + 1 tension) checks out against §8 item 4. |
| §2I lens roll-call (−14) | **No cost.** Both versions name the same six lenses — §2A, §2B, §2D, §2E, §2F, §2H — in the same order, with the same content per lens. Nothing dropped. |
| §5 neighbour comparisons (−25) | **Cost, and the worst of them.** Deleted the only expansions of Worlds #6, #9 and #2 (NEW-M3). The substantive comparisons themselves all survive. |
| §7 Representative paragraph (−16) | **Cost.** Deleted four Representative-facing strengths and replaced them with a pointer §5 supports for one of the four (NEW-L3). |
| §8 carried items (+21 net) | **No cost, and no renumbering.** Items 1–9 before, items 1–9 after, one-to-one. The Open Item 8 material was added into existing item 6; nothing was merged away and nothing was lost. Compression at items 4, 5, 7, 8, 9 is genuinely redundant wording — "with no owner and no acceptance criterion. Doc_04 §7 Open Item 6" → "…(Doc_04 §7 Open Item 6)" and the like. The one defect touching §8 is a pointer *into* it from §2D (NEW-L1). |
| Disposition build-cycle paragraph (−44) | **Cost, and the most consequential.** See NEW-M4. |

**Every internal `§` cross-reference re-checked.** All resolve except §2D's "§8 item 6a" (NEW-L1) and, in substance, §7's "beyond what §5 already states" (NEW-L3) and the Disposition's "stated at §1" (NEW-M4). §2D→§8 item 6 ✓; Disposition→§8 item 5 (the M4/template divergence) ✓; §8 item 4→item 6 (the unresolved tension, the *Gesta*) ✓; §8 item 2→§4 ✓; §8 item 3→§3A ✓; §5→§2A/§2C/§2D/§2E/§2B ✓; §2E→§2I ✓; §2I→§2E ✓ (with NEW-C1); §2A→§2D/§2G ✓; §3C→§2D ✓.

---

## Was Round 1 right?

**On its five findings: yes, all five.** Each was a real defect at the site named. H1 was correctly graded HIGH — the rewritten §2E is a materially better argument than what it replaced, and the improvement is exactly what H1 asked for. M1 and M2 were correctly graded and correctly fixable. L1 and L2 were correctly graded LOW rather than inflated.

**Two places where Round 1 was imprecise or incomplete:**

1. **H1's site list names "§8 item 1's summary language" as repeating the sharper-boundary claim. It does not.** §8 item 1 reads, in both the pre-fix and post-fix versions, *"§4 is a synthesis, not a compilation…"* and contains no World #6 content of any kind. The claim appeared at §2E and §5 only. Harmless — the fix pass fixed the two sites that existed — but it is an inaccuracy in a finding's own evidence.

2. **Round 1 certified "Template's other requirements" as met and missed the Section 6 "external scholarly review" element** (NEW-L5), which the sibling Donatism Doc_07 carries.

**§2G's basilica reconstruction from Letter CXXVI: Round 1's SOUND judgement is correct, and I re-tested it at source.** Reading the letter with `<note>` spans marked, all three load-bearing English elements are the translation's own words, not inferences from silence: *"I left the multitude, and returned to my own seat"*; *"the more venerable and aged men who had come up to me in the apse"*; *"the crowd having gathered in front of the steps."* "Apse" and "steps" are the text's, not the document's. "Raised clergy seating area" and "congregational floor" are explicitly labelled inferences from "came up to me" and "gathered in front of," and §2G frames the whole passage as "architectural evidence recovered from a pastoral letter rather than a trench" rather than as excavation-grade fact. **The reconstruction is not over-read.** Round 1's one miss inside a correct judgement is the Latin tag (NEW-L4), which Round 1 noticed as a marginal note and did not follow through on.

**The §3B quotation was also re-verified with the note remedy** and is clean: *"are often corrected by those which follow them, when, by some actual experiment, things are brought to light which were before concealed"* sits in the body text of `npnf104`, outside every `<note>` span, verbatim.

---

## Is the deliverable adequate to proceed to Doc_08?

**Yes — the analysis is adequate; the document's self-record is not, and NEW-H1 must be fixed before either.**

Doc_08 draws on §8 items 1–3 (the six-cell matrix threads, G5's incomplete-ecology shape carried rather than resolved, Transmission as load-bearing via §3A). **None of this round's fourteen findings touches any of the three.** The gravity spine is unchanged. Every quotation in the document has now been verified at source across two rounds, including the two the fix pass rewrote. The forces integration at §2H delivers the Forces Framework's own three movements in the required lens, and §4 exceeds the minimum. The §2E rewrite improves the document's most-contested argument rather than damaging it.

What is not adequate is the document's account of itself. NEW-H1 is a false statement in the Disposition about the document's own review history, and it is two mechanical edits away from being true. NEW-M1, NEW-M3 and NEW-M4 are each a single restored or narrowed sentence. NEW-L1 is a one-character fix. **The whole fix pass for this round is under half an hour of editing and touches no analytical claim.** It should be run before Doc_08 begins, because Doc_08 will cite Doc_07 and should not cite a document that says it has never been reviewed.

---

## CO-022 escalation assessment

Checked against Doc_04, Doc_05 and Doc_06's current disposition records and Doc_07's own Disposition.

**None of this round's fourteen findings creates a new escalation category.** NEW-H1 and NEW-M4 are self-record defects inside this document's own editing authority. NEW-M1, NEW-M2, NEW-M3, NEW-L1, NEW-L2, NEW-L3 and NEW-L6 are all correctable in place. NEW-L4 is an instance of the corpus-wide editorial-apparatus question **already registered as portfolio-level item 1** — it does not add a fifth item, it is a new local instance of an existing one, and should be recorded that way rather than escalated afresh. NEW-L5 is an instance of the template/Framework divergence family **already registered at §8 item 5**.

**Doc_07's own CO-022 assessment is accurate as written**, and I re-confirmed each limb: *Representative identity* — does not apply; §3C and §5 describe patterns and recognizability, not an identity, title or voice decision. *Portfolio-level* — four items, the three inherited plus the M4/template divergence §8 item 5 adds. *Governance/methodology* — four, none added here. *Unresolved tensions* — one, the 411 *Gesta*, relied on for nothing in this document (verified: §7 and §8 item 6 name it, no lens draws on it).

**The settling point this round is asked to reach, stated plainly.** Doc_07 itself adds a portfolio-level item at §8 item 5. **A portfolio-level escalation category is therefore open against Doc_07**, and CO-022 forbids a build thread from self-disposing a document in that condition. So regardless of this review's verdict, **Doc_07 cannot be self-disposed by the build thread** — it joins Doc_04, Doc_05 and Doc_06 in awaiting a disposition only the project lead can give, making five. That is not a new escalation; it is the existing one applying to this document as it applies to the other three, and the Disposition should say so in those terms once NEW-H1 is fixed.

---

## VERDICT: REVISION REQUIRED

**1 HIGH · 4 MEDIUM · 6 LOW · 3 COSMETIC — 14 findings.**

**Round 1's five findings: 5 FIXED, 0 partially fixed, 0 not fixed, 0 fixed wrongly, 0 wrong.** Every one was verified at the primary source or governing document rather than against the fix pass's account of it. The fix pass did competent work on what it was asked to do.

**The trims cost something**, at four of six sites, and the document's self-record is now wrong in the Disposition. None of it touches the analysis, the gravity spine, the quotations, or anything Doc_08 needs. This is REVISION REQUIRED rather than SUBSTANTIAL REVISION REQUIRED because the fourteen findings together are a short editing pass on sentences about the document, not on the document's findings.

*End of Round 2 review. Simulated review — informational only, not an Article 31 substitute.*
