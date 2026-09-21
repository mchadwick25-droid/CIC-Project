# VERDICT: SUBSTANTIAL REVISION REQUIRED

**World Profile — Round 4 independent adversarial review, 2026-09-16.**

**Combined counts: 5 HIGH · 6 MEDIUM · 6 LOW · 1 COSMETIC.**

| Dimension | Artifact | Verdict | H | M | L | C |
|---|---|---|---|---|---|---|
| Condensation loss | `WorldProfile_Round4_Review_Condensation.md` | REVISION REQUIRED | 1 | 2 | 2 | 0 |
| Internal & cross-document consistency | `WorldProfile_Round4_Review_Consistency.md` | REVISION REQUIRED | 2 | 0 | 1 | 0 |
| Source & quotation fidelity | `WorldProfile_Round4_Review_SourceFidelity.md` | **SUBSTANTIAL REVISION REQUIRED** | 2 | 4 | 3 | 1 |

The worst dimension governs. **This document does not clear Round 4**, and on CO-022's own condition it is not eligible for disposition.

---

## How this round was run

Three reviewers, one dimension each, run in parallel and in isolation from one another. None had written or condensed the document. The build thread briefed them, **did not review**, and adjudicated afterwards — it has applied findings to this document all day and is not independent of it.

Splitting by dimension was deliberate: Rounds 1–3 were single-reviewer rounds over a document that is now 12,142 words, and a single reviewer asked for four things tends to do all four shallowly. Each reviewer here was required to state what it swept exhaustively, what it sampled, and what it did not cover, with this build's own meta-defect quoted at it.

**Round 4 is the first review to see the condensed document.** Rounds 1–3 all predate the 2026-09-16 condensing pass, which removed 5,875 words. Nothing had examined that cut.

## Independent verification by the adjudicating thread

**All five HIGH findings were re-verified at source before this artifact was written.** A reviewer's report is not evidence; the sources are. Results:

| # | Finding | Verified how | Result |
|---|---|---|---|
| H1 | A quotation attributed to the project lead is a build thread's own sentence | Compared all four sites: Profile, `Doc_04` line 214, `lpc_Decision_Log.md`, `lpc_Gapped_Formation_Precedent.md` §4b | **CONFIRMED** |
| H2 | Possidius "chs. XXII and XXIV" — content is entirely in XXIV | Split the de-hyphenated Weiskotten body by chapter and tested all six cited elements against XXII, XXIII, XXIV | **CONFIRMED** |
| H3 | A live cross-document contradiction disclosure was deleted | Read `Doc_08` lines 191 and 302 and `Doc_09` at source; checked the Decision Log for relocation | **CONFIRMED** |
| H4 | "Required inputs" misstates two inputs' disposition status | Read `Doc_02` and `Doc_03` Dispositions at source | **CONFIRMED** |
| H5 | Section 11 item 4 carries a verification as unperformed after three rounds closed it | Read all three `Doc01_Correction_*Verification*` artifacts | **CONFIRMED** |

No HIGH was downgraded. One check I ran initially appeared to refute H3's Doc_09 half; re-run precisely, the quoted string is present in `Doc_09` exactly once and the reviewer was right.

---

## The five HIGH findings

### H1 — A build thread's own conclusion is quoted as the project lead's words

Section 2, G5. The Profile reads:

> **Doc_04 §7 Open Item 8 is CLOSED (2026-09-15)**, on the gapped-formation precedent from the project lead: *"Candidate 5 is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding."*

Quotation marks, italics, and an explicit attribution to the project lead. At source, that sentence is **`Doc_04`'s own bolded editorial conclusion**, carrying no quotation marks:

> **Candidate 5 is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding.**

The Decision Log states it as its own sentence too, and in different words — *"Candidate 5 is Supporting and honestly thin, and that is the answer."* What the precedent document actually states in its own bolded voice, without quotation marks, is a **different sentence entirely**: **Treat five consecutive re-classifications of the same candidate as itself the signal to stop and accept the narrower finding.** *(Corrected 2026-09-16 while applying this finding. This paragraph first rendered that sentence as a quotation reading "a signal" and carrying a further clause, "not as five steps of legitimate progress toward a stronger one." That wording is `Doc_04`'s, not the precedent's — see the post-round finding below. Going to the precedent to quote it correctly is what caught it. Recorded rather than silently amended, because this artifact is the audit trail for this exact defect class.)*

This strikes the rule CO-022 states without qualification: **nothing is attributed to the project lead — a quote, a decision, an instruction — without a verifiable record that the project lead actually said or wrote it.** The underlying ruling is real and recorded; the words put in the project lead's mouth are not.

### H2 — A citation that resolves to the wrong chapter

Section 8, material limits. The Profile cites **Possidius chs. XXII and XXIV** for the treasury, the consistory, *"from which were supplied the things necessary for the altar,"* the holy vessels, the annual audit, and *"never had any desire"* for new buildings.

Tested against the de-hyphenated Weiskotten text, **all six sit in ch. XXIV.** Ch. XXII is *"Augustine's use of food and clothing"* and contains none of them; ch. XXIII is *"His use of the church revenues."* A locus that exists but says something else is worse than one that does not resolve, because it survives a spot-check.

### H3 — A live contradiction between three cleared documents is now undisclosed

Before the condensing pass, the Disposition disclosed that the Profile's "two mechanisms cross the 133-year silence" claim **contradicts two other *Approved to proceed* documents that still say there is one**, and that this was adjudicated rather than overlooked. Both still say it: `Doc_08` line 191, *"**This is the only mechanism** by which this world's formation logic demonstrably crosses its own 133-year silence"*; its connection table at line 302; and `Doc_09`, *"the only thing crossing the gap is a text."* The Profile now states *"One of two demonstrated mechanisms"* flatly at line 366.

The disclosure was **deleted, not relocated** — it is not in the Decision Log either. A downstream builder cross-checking the Profile against Doc_08 or Doc_09 now meets an unexplained contradiction with no breadcrumb anywhere in the live project. **This is also an escalation category** under CO-022: a contradiction between cleared documents is an unresolved tension the pipeline cannot close on its own.

### H4 — The document misstates its own inputs' status

The header reads *"Doc_01 self-disposed; Doc_02–Doc_09 approved by the project lead."* At source, `Doc_02` self-disposed by CO-022's ordinary clearing path with no project-lead act, and `Doc_03` self-disposed on the project lead's direct instruction — a third case again. Doc_04–Doc_09 match the claim; two of eight do not.

### H5 — A completed verification carried as unperformed

Section 11 outstanding item 4 states that independent verification of the Doc_01 §2 correction was *"not performed by the thread that applied it."* Three dated verification artifacts sit in this folder, and the third concludes **"The correction can be called closed."** The Profile was edited after all three completed, so this is stale text rather than a timing gap — the same shape as the Document Log that read "not yet run" beside three review files.

---

## What Round 4 found that Rounds 1–3 could not

Rounds 1–3 reviewed a document that no longer exists. Of the five HIGHs, **three are consequences of edits made after Round 3**: H3 and two of the MEDIUMs are condensation losses; H5 is text the condensing pass carried through faithfully while its subject changed underneath it.

**H1 and H2 are older**, and both survived three rounds. That is the more uncomfortable result: a fabricated attribution to the project lead and a wrong chapter citation sat in this document through three adversarial rounds that did not catch them, because no round before this one swept every quotation and every locus to source. The source-fidelity reviewer traced **44 distinct quoted spans and opened 21 loci in full**; 34 of 44 quotations passed clean.

## The pattern underneath H1

Source-fidelity Finding 4 names it as a pattern rather than an instance: **plain, unquoted prose from a source document re-presented as an italicized direct quotation.** H1 is that pattern at its worst, because the prose it dressed as a quotation was then attributed to the project lead.

The same confusion appeared independently in the condensing pass hours earlier, in both threads: italics added around quotations the source gives plain, and punctuation pulled inside closing quotation marks. **This build treats emphasis and quotation as interchangeable typography, and they are not.** Quotation marks are a claim about what a source says. That diagnosis belongs in the revision, not just the fix list.

## Coverage — what Round 4 did not check

Stated because a review's value depends on its limits being known:

- **No exhaustive sweep of the ~90 `Doc_0n §x` citation loci.** 21 were opened in full. Section 11 item 11 already discloses that this sweep has never been completed by anyone; Round 4 does not close it.
- **The broad "Grounding:" citation lists** at the end of each gravity entry were not verified.
- **Sections 3 and 4** were checked for condensation loss by targeted hedge-regex sweep and source spot-checks, not a word-for-word read.
- **Archaeological and material absence claims** are untestable from the vendored corpus and were not tested.
- **Doc_09-sourced absence claims** were spot-checked on one thread, relying partly on Doc_09's own eight prior rounds against that defect.
- Two absence claims *were* independently re-run as regex sweeps against the vendored texts rather than trusted from the CiC document asserting them — the *confessor* sweep and the *libellus* headword claim. Both reproduced exactly.

## Disposition

**Not disposed.** Four rounds, four sets of findings, none clean. The revision decision under CO-022 is unambiguous: these are substantial — they change a sourcing conclusion, an attribution, a citation, and the disclosure of a live contradiction — so the document is revised and goes back through review, not disposed of.

**One finding is not the build thread's to close.** H3's contradiction between three cleared documents is an unresolved tension under CO-022's fourth escalation category. The Profile's disclosure of it can and should be restored from the pre-condense text; **deciding which of the three documents is wrong is a project-lead act**, and a build thread does not overturn a cleared finding.


---

## Post-round finding, 2026-09-16 — H1 has an upstream parent

Found while applying H1, by opening `lpc_Gapped_Formation_Precedent.md` to quote the precedent correctly instead of trusting the documents that cite it.

**The precedent's own sentence**, stated in bold and carrying no quotation marks:

> **Treat five consecutive re-classifications of the same candidate as itself the signal to stop and accept the narrower finding.**

**`Doc_04` quotes it** — with quotation marks and italics — as *"Treat five consecutive re-classifications of the same candidate as itself a signal to stop and accept the narrower finding, not as five steps of legitimate progress toward a stronger one."*

Two alterations. *The* became *a*. And a fourteen-word clause was appended that **appears nowhere in the precedent, or anywhere else in this build** — `grep` finds it in `Doc_04` alone, and in this artifact, which reproduced it.

**`lpc_Decision_Log.md` quotes it** as *"…as itself a signal to stop and accept the narrower finding."* — the same *the*-to-*a* change, without the appended clause.

**Why this is worse than H1.** H1 sits in a document under revision. This sits in **`Doc_04`, Approved to proceed by the project lead on 2026-09-15**, and in the **Decision Log, which is this build's record of what was actually decided**. The precedent document records the project lead's own act narrowly — *"The project lead ruled it directly (2026-09-14: Supporting)"* — so the methodological sentence may be the precedent document's own formulation rather than the project lead's words at all. The Profile's H1 fix therefore quotes **neither** sentence as the project lead's, and attributes to the project lead only the verifiable 2026-09-14 ruling that Candidate 5 is Supporting.

**Not fixed here, deliberately.** A build thread does not edit a document the project lead approved, and does not rewrite the Decision Log's record of a decision. **Both need the project lead.** Recorded here so the finding is not lost between threads.

**What it says about the pattern.** Round 4 named the class — plain prose re-presented as a direct quotation — and traced it through the Profile and both condensing threads. It runs further: into a cleared construction document, into the record, and into this review artifact. **A quotation-mark sweep across the whole build, not just this document, is the proportionate response.**
