# Doc_09 (Step-9 Bundle) — Round 2 Independent Adversarial Review (Confirmation Pass)

**Simulated review — informational only, not an Article 31 substitute.**

**Reviewer role:** Independent adversarial AI reviewer, with no visibility into Round 1's own reasoning process during analysis (Round 1's disposition was read only afterward, for comparison, per this pass's charge to *re-derive*, not re-confirm).
**Reviewed at:** 2026-07-19.
**Occasion:** A portfolio consistency audit found Alexandria's Doc_09 was the only sibling-world Doc_09-equivalent to clear on a single review round (Desert-Monasticism Doc_09: 2 rounds; Hieronymian Doc_09a/Doc_09c: 2 rounds each; Syriac Doc_09 + Validation Layer: 3 + 2 rounds). This pass closes that gap.
**Artifacts reviewed:** `Doc_09_Story_Inventory.md`; `Story_Index.xlsx` (all 6 sheets, extracted and diffed against the prose); `Doc_01`, `Doc_02`, `Doc_04`, `Doc_08` (re-read in full as ground truth, not taken on Doc_09's or Round 1's word); `Doc_05` §3/§6.5 and `Doc_07` §4/§5 (spot-checked as validation-basis citations); `alex_Rep_Phase2_Formation_Calibration.md` and `alex_World_Capsule_Core.md` (drift check, built after Doc_09).
**Method:** independent re-derivation of all 10 tier justifications against the four-tier criteria and Doc_02's Author-Gravity entries; independent No-Tier-5 re-audit; Absent-Stories substance check against Doc_02 §6's own named list of structurally-suppressed voices; independent re-verification of all 9 Validation Layer PASS rows against Doc_01–08 (not against Doc_09's own summary); xlsx↔md sync re-check via direct XML extraction; cross-build flag check; Native-source spot-check; drift check against the Representative layer built after Doc_09.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED — 2 substantial findings (+ 2 cosmetic, 1 informational correction to the Round 1 record)

The single-round closure was **not fully justified in retrospect**. Independent re-derivation surfaced one validation-row citation-integrity defect Round 1 did not catch at all, and one tier-justification gap Round 1 flagged but under-rated. Both are narrow and fixable without reopening the document's core determinations (No Tier 5 holds; the Absent Stories answer is substantive; the Validation Layer's honesty about deferral holds; no fabrication or Theon leak). This is a confirmation-and-tightening pass, not a rebuild.

---

## Findings

### F1 [SUBSTANTIAL] — The Differentiation validation row cites a comparandum ("the Syriac world") that appears nowhere in Alexandria's own cleared construction record (Doc_01–08)

**Location:** Doc_09 §5.2, table row:
> "Differentiation | **PASS** | distinct from Antioch (hermeneutics/Christology), **the Syriac world**, and the (held-open) Desert world; shared inheritance functions distinctively"

**The check.** The review brief specifically asks whether "Anachronism — PASS" is "genuinely checked... or asserted" — the same test applies to every row. I traced "the Syriac world" through the entire cited record:
- Doc_01 §3.4 ("Adjacent worlds — exchange partners, not part of this ecology") names exactly three: Palestine/Caesarea, Cappadocia, and Antioch. Syriac Christianity is not listed.
- Doc_07 (the document whose §4/§5 the Emergence/Balance rows correctly cite) contains no differentiation argument against a Syriac world anywhere.
- A repo-wide grep for "Syriac" across Doc_01–Doc_08 and Doc_09 returns **zero** matches outside this one Doc_09 table cell. The only other "Syriac" hit in the Alexandria folder is `alex_World_Profile.md` §0, which cites the Syriac World Profile only as a **formatting model**, not as a differentiation comparandum.

**Why it matters.** Alexandria and the Syriac world are almost certainly distinct in fact — that is not in question. What is in question is whether this PASS row reflects a *checked* determination against this world's own cleared record, as every other row in §5.2 does (each other row carries a specific Doc_0X§Y citation that verifiably supports it). This one does not: it is an assertion smuggled into a Part VI validation table with the same evidentiary weight as the checked rows around it, and it reads as if imported from cross-referencing the sibling Syriac build rather than argued from Alexandria's own Doc_01–08. This is exactly the category of defect (an unargued claim resting on no traceable citation in a load-bearing document) that Round 1 reviews elsewhere in this portfolio (Doc_01 R1, Doc_02 R1) treated as Substantial when found in comparable load-bearing rows.

**Fix.** Either (a) strike "the Syriac world" from the row and let Antioch + the held-open Desert world carry Differentiation (which they do, on solid citation), or (b) if the comparison is wanted, add the argument to Doc_01 §3.4's adjacent-worlds list first and cite it from there. Trivial to correct; the underlying PASS determination survives either way.

---

### F2 [SUBSTANTIAL] — `alexstory003`'s Tier-1 justification does not resolve whether Eusebius functions here as narrator or as quoted-primary-source, and its stated confidence breaches the tier's own pre-declared cross-walk

**Location:** Doc_09 §2, `alexstory003`; §1's confidence cross-walk sentence.

**The check.** Doc_09 §1 pre-declares a clean mapping: "Tier 1 → Documented/Widely Accepted." `alexstory003` is assigned Tier 1, sourced to "Eusebius *HE* 6." But:

1. **The tier-criteria gap.** Tier 1 ("Documented Historical Narrative") is elsewhere in this same document correctly built on *direct* textual attestation — Gregory's own first-person Address (`alexstory001`), Palladius's own firsthand encounter with Didymus (`alexstory002`). Eusebius, by contrast, is Doc_02's flagged **HIGH Author-Gravity risk author "for institutional/biographical claims" specifically** (Doc_02 §3.6) — writing roughly a century after Origen's imprisonment, not as an eyewitness. Doc_02 §3.6 draws a sharp distinction for Eusebius between his own narrative construction (HIGH risk) and his verbatim quotation of a primary document (lower risk — "e.g., Dionysius's letters"). Doc_09's tier justification for `alexstory003` never establishes which of these two modes applies here: is "Origen imprisoned and tortured under Decius" Eusebius's own narration, or is it (as with the Dionysius material) Eusebius quoting a document that itself constitutes more direct attestation? That distinction is exactly what the Tier-1 "direct textual attestation" criterion turns on, and the justification as written doesn't engage it — it asserts "well-attested" without saying attested *how*, by whom, directly or at one remove.
2. **The cross-walk breach.** The story's own confidence line reads: "**Documented** for the persecutions as events; **Widely Accepted** for Origen's Decian imprisonment specifically; **Contested-leaning** for the Leonidas particulars." That third clause — Contested-leaning — falls outside the pre-declared Tier-1 range ("Documented/Widely Accepted") stated two pages earlier in §1, with no stated exception for split-confidence stories. `alexstory009` (Tier 3) does the same event/particulars split, but Tier 3's cross-walk ("Contested (portrait)/Inferential-Thin (specific events)") is wide enough to absorb it; Tier 1's is not.

**Round 1's handling.** Round 1's C1 cosmetic observation noticed the HIGH-risk-author-under-a-Tier-1-label tension and judged it "nonetheless defensible," recommending only that the split be made "one notch more prominently" — it did not identify the cross-walk breach, and did not ask the narrator-vs-quotation question. Independently re-deriving the justification (rather than re-confirming Round 1's) surfaces both. The underlying tier call may well still be defensible once these are answered — the empire-wide Decian persecution is independently documented well beyond Eusebius (papyri, the *libelli*, Dionysius's own correspondence on the Alexandrian persecution) — but the document as written doesn't make that case; it asserts the conclusion.

**Fix.** Either (a) give `alexstory003` the same explicit three-part split Doc_09 already models at `alexstory009` (persecution-as-event / Origen's imprisonment / Leonidas particulars), each with its own confidence label, and add one clause to §1's cross-walk sentence noting that composite persecution-narratives are split-confidence by design; or (b) state directly whether the Origen-imprisonment claim rests on Eusebius's own construction or on a quoted primary source, closing the gap Doc_02 §3.6 opens.

---

### F3 [COSMETIC] — §1's confidence cross-walk is stated as an unqualified one-to-one mapping, but two stories (`alexstory003`, `alexstory009`) are split-confidence composites that don't fit inside one cell

Doc_09 §1: "Tier 1 → Documented/Widely Accepted; Tier 2 → Widely Accepted/DMR (attributions Contested); Tier 3 → Contested (portrait)/Inferential-Thin (specific events); Tier 4 → Inferential-Thin (labeled reconstruction)." This reads as an exhaustive per-tier confidence range, but two of the ten stories intentionally straddle it (a design choice the document itself names — "*Event-vs-particulars split stated explicitly, as at `alexstory009`*"). A single added clause ("persecution-narrative stories may carry internally split confidence spanning these ranges, per §2") would make the stated cross-walk match the document's own practice. Bound up with F2; not independently blocking.

---

### F4 [COSMETIC] — Catechumens, one of Doc_02 §6's five explicitly-named structurally-suppressed voices, are not given their own line in the Absent Stories answer

Doc_02 §6 names five voice-categories the Article 20 duty covers: women, ordinary non-literate believers, rural/Coptic Christians, **catechumens** ("present only as recipients, never as authors"), and enslaved persons. Doc_09 §3 names four absences with real specificity (non-literate majority, women, enslaved believer, martyr's interior) plus the cross-build desert absence — but does not give the catechumen's own voice (the ordinary person's first-person account of undergoing the initiatory catechumenate itself, as distinct from `alexstory001`'s advanced-student account or the majority's general interior) a separate line. It is arguably subsumed under the non-literate-majority bullet, but not every catechumen is non-literate, so the subsumption is imperfect. Optional: add a sixth bullet, or note explicitly that the catechumen's voice is covered by the majority-interior absence. Non-blocking — §3 already clears the "substantive, not placeholder" bar on its own terms.

---

### Informational — correcting the Round 1 record (no action on Doc_09 required)

Round 1's cosmetic observation **C2** stated: "the composite `alexstory010` cites 'Origen's *On Prayer*'; Doc_02's catechetical stream enumerates Origen's homilies and *Contra Celsum* but not *On Prayer* by title." This is **incorrect** — Doc_02 §2 **Stream 3 (Worship and Prayer)** names "Origen's *On Prayer*" explicitly and directly: *"Sources: Origen's* On Prayer*; Athanasius's* Festal Letters *(the paschal-dating letters)..."* Round 1 checked the wrong stream (Stream 2, Catechetical Formation) rather than Stream 3. The underlying disposition (no Native-source violation) was still correct, and no Doc_09 defect exists here at all — `alexstory010`'s citation is in fact more directly grounded than Round 1 realized. Flagged here only because it shows Round 1's citation-tracing, while reaching the right answer, was not as careful as its own verdict language ("all citations web-verified") claimed.

---

## Checks that held up under independent re-derivation

- **No Tier 5.** Re-derived independently, not re-confirmed: all 10 stories are sourced; `alexstory010` is built only from attested elements (Clement's *Paedagogus*, Origen's *On Prayer* — now confirmed doubly, see above — Athanasius's *Festal Letters*), narrates practice not a named individual, and correctly excludes the non-literate majority's interior. Holds.
- **Tier justifications 001, 002, 004, 005, 006, 007, 008, 009, 010** — each independently checked against Doc_02's Author-Gravity entries and the tier criteria; each engages the criteria substantively (not just an assigned number) and matches the upstream cleared record (Doc_02 §5, §3.6). Only `alexstory003` (F2) has a live gap.
- **Absent Stories (§3).** Substantive, specific, tied to real evidentiary reasons (OG-4, Doc_02 §6, Doc_01 §3.3), meets Article 20's affirmative-duty standard. F4 is a completeness refinement, not a placeholder problem.
- **Validation Layer rows other than Differentiation** — Historical Plausibility, Ecological Integrity–Balance, Reduction, Complexity, Emergence, Worship Integration, Author Dominance, Anachronism: each independently traced to a real citation in Doc_01/02/04/05/07/08 (spot-verified Doc_05 §3 Worship Ecology and Doc_07 §4/§5 directly) and each citation genuinely supports the PASS claim. Anachronism specifically re-checked: the 553 condemnation, Chalcedon (451), and the Arab conquest (641) are all correctly kept outside the horizon throughout Doc_01, Doc_04 T3, and Doc_08 3A-1/3A-2 — no hindsight read-back found anywhere in the chain.
- **Cross-build discipline (`alexstory004`, `alexstory005`).** Checked directly against Doc_01 §3.3: both carry the held-open flag, and Antony's literacy is correctly carried as Contested (Rubenson) rather than asserted as fact. Holds.
- **Source Native-check.** Spot-checked (Gregory, Palladius, Eusebius, Apophthegmata, Athanasius/*Life of Antony*, Clement/*Paedagogus*, Origen/*On Prayer*, Athanasius/*Festal Letters*) directly against Doc_02 §3.6, §5, and the evidence streams — all Native, no cross-world borrowing found.
- **Story_Index.xlsx sync.** Re-extracted all 6 sheets independently via XML (not trusted from Round 1's report). Zero drift: every story ID, tier, source, confidence, cross-build flag, and Native-source flag in the workbook matches Doc_09's current prose exactly, including the `alexstory003` event-vs-particulars split Round 1's own recommendation produced.
- **Representative-layer drift check (new since Round 1).** `alex_Rep_Phase2_Formation_Calibration.md` and `alex_World_Capsule_Core.md` (both built after Doc_09) were checked for consistency, not assumed. Temporal horizon (c. 150–400, firm c. 400 edge), Origen's treasure-and-unease framing, the Teacher–Bishop/Learning–Community/Speculative-Doctrinal/Martyrdom tensions, and the stratum-bias limit are all carried forward without contradiction. No drift found.
- **No Theon/Representative leak.** Re-swept independently; the only "Theon" occurrence in Doc_09 is the Status line's own meta-reference to Round 1 having checked for a leak (a correct negation), not an actual leak.

---

## Summary count

- **Substantial findings: 2** (F1 — ungrounded Syriac-world differentiation citation; F2 — `alexstory003` tier-criteria gap + cross-walk breach)
- **Cosmetic findings: 2** (F3, F4 — both optional)
- **Informational: 1** (correction to the Round 1 review record; no Doc_09 action needed)

**Disposition recommendation:** SUBSTANTIAL REVISION REQUIRED, but narrow — both substantial findings are single-row/single-story fixes that do not touch the document's core determinations (No Tier 5, Absent Stories substance, honest Validation-Layer deferral, no fabrication) and do not require reopening Doc_01–08.

**Was the single-round closure justified in retrospect?** No, not fully. This Round 2 pass surfaced one defect Round 1 missed entirely (F1 — Round 1's five required explicit answers and F1–F10 findings never traced the Differentiation row's citations item-by-item the way the other eight rows were traced) and elevated one defect Round 1 spotted but under-diagnosed (F2 — Round 1 saw the HIGH-risk-author tension but not the cross-walk breach or the narrator-vs-quotation ambiguity). Both are the kind of narrow, single-row gaps a genuinely independent second reviewer is positioned to catch precisely because a synthesis document reviewed once, under the reasoning "the material was already cleared upstream," is exactly where citation-tracing against the *downstream document's own new claims* (as opposed to the upstream claims it synthesizes) can go unchecked. The portfolio-parity concern that prompted this pass was warranted.

*End Doc_09 Round 2 Review. "Simulated review — informational only, not an Article 31 substitute" (Constitution Article 31).*
