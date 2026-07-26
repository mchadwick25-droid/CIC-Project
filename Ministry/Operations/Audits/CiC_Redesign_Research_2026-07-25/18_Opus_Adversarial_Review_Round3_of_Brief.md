# Adversarial review (round 3): `CiC_System_Redesign_Fable_Brief_2026-07-25.md`

*Opus review, dispatched 2026-07-26 — the third adversarial pass on this brief. Scoped specifically to material added since round 2 that had never been checked by anyone: research docs 12-17 folded in, the operational-parameter and sense-field additions to §9, the three-level content spec, and the new measurement-plan deliverable (§10 #9). Read `11_Opus_Adversarial_Review_of_Brief.md` and the decision log's record of round 2 first for calibration — not as a description of the brief's current state, which has moved well past both. Genuinely adversarial by design, not a rubber stamp, given Fable is a capped resource (2 passes/week).*

*Verification method: every finding below was checked by reading the brief text and the cited research doc side by side; the two most severe were re-verified independently rather than trusted from a delegated summary.*

## Bottom line

**Not ready to send.** The brief is genuinely strong — the round-1 and round-2 P0s are all really fixed, the balance problem is fixed, and all 27 internal `§N` cross-references resolve correctly. But the material folded in since round 2 had not been checked by anyone, and it carries **five send-blocking defects**, four of them the same class the prior two rounds caught: a claim that will not survive the verification the brief itself demands.

The most serious is in §4, where the new "certainty distortion" clause **inverts research doc 13's actual argument** about which direction an adjudicator's bias defends. §4 is the "don't rebuild this" section, and the inverted version could lead Fable to flip a live safety mechanism's deliberate fail-open direction.

The single highest-risk new addition overall is deliverable 9 (the measurement plan). It contains a misattributed citation, an unsourced framework presented as "industry-standard," an overstated "zero cost, available today" claim, and an instruction Fable cannot execute within Pass 1's own stated scope — where the likely failure is Fable *fabricating* baseline numbers, which is this project's central failure mode.

---

## P0 — fix before sending

**1. §4's certainty-distortion clause inverts doc 13's direction argument and attaches the published term to the wrong failure.**

Brief §4: *"the second failure is the field's own **certainty distortion** — a 2026 finding that models inflate expressed certainty 1.5–2x more often than they deflate it, exactly the direction the adjudicator's opposite bias defends against."*

The brief's "second failure" is, by its own preceding sentence, *"a real conviction must never be second-guessed into false hesitation"* — the **deflation** failure. But doc 13 assigns "certainty distortion" to **over-settling**, i.e. inflation (§1c: *"Rename or subtitle OVER_SETTLING to certainty distortion"*). And doc 13 line 84 says the opposite of the brief's final clause outright:

> "Given a measured 1.5–2× inflation bias in the *generator*, biasing the *detector* toward clearing **looks backwards at first glance** — and CiC's stated reason is exactly right... That is the *deflation* failure the same literature measures, applied at the correction layer instead of the generation layer. **CiC is defending both directions. Say that.**"

The brief encodes precisely the naive reading doc 13 flags as backwards. Two consequences: a verifying Fable finds the claim contradicted at its own cited source, and Fable could conclude the over-settling adjudicator should fail toward *finding* to match the inflation direction — flipping a live bias. Doc 13's own formulation ("CiC is defending both directions") is stronger and shorter than what's there. Also dropped: `epistemic faithfulness`, which doc 13 names as the property being protected and recommends using alongside the term.

**2. §10 #9's "40–100%" field-compliance figure is attributed to doc 12 and is not in doc 12 at all.**

Brief: *"the same measurement that already caught 40–100% real variance in a single field's compliance (research doc 12)."* Doc 12 contains no per-world field-completion audit and no such number. The real source is `01_DesignDoc_Mining.md` (Desert 56%, Hieronymian 40%, Alexandria 100%), restated more fully in `03_WorldBuilds_Validation_Sweep.md` — which reports **two** vocabularies, not one field (Author-Gravity compliance ran 7%/22%/100%, so the true span is 7–100%), across **three** worlds, not six. "Already caught... per world" overstates an audit that covered half the portfolio. Wrong doc, wrong scope, wrong single-field framing.

**3. §10 #9's "RAG Triad" is unsourced across all 17 research docs, and it is attached to the one sentence carrying doc 15's zero-cost claim.**

`RAG Triad`, `context relevance`, and the triad framing appear **nowhere** in the research directory (grep across all 18 files). The concept is real (TruLens), so this isn't fabrication — but the brief labels it "industry-standard" in a document whose preamble promises *"Every claim in this brief traces back to specific evidence there."* Three compounding problems:

- Doc 15's zero-cost argument depends specifically on choosing **ID-based** RAGAS variants *instead of* judge-model metrics: *"No judge model, no API cost, no LLM-grader-grading-an-LLM-grader circularity."* The Triad's metrics are LLM-judged. The brief's sentence structure lets "zero API cost" bleed onto them.
- *"computable today at zero API cost from data already logged"* overstates availability. Doc 15 scopes the harness at *"~1 day of code, ~1 day per world of case authoring"* for a golden set of *"12–20 cases per world, ~90 total"* that does not exist. The retrieved-side inputs are already logged; the gold side must be hand-authored first.
- *"groundedness and answer relevance, both measurable per turn from the adjudicators' own verdicts"* is unsupported. Doc 13 (line 49) places answer relevance on the **retrieval** side, not generation, and nothing in CiC measures whether an answer addresses the question.

There is a properly-sourced home for this: doc 13's High-confidence "SHOULD ADOPT" finding that the fabrication check *is* **groundedness / AIS (Attributable to Identified Sources)**, Rashkin et al. 2023. Cite that instead of an unsourced triad.

**4. §10 #9's closing instruction cannot be executed within Pass 1's own scope, and the likely failure mode is fabricated numbers.**

*"Run this as a real baseline against today's system before claiming the redesign improved anything."* §10 states twice that Pass 1 produces *"a design document... not code, not schema files"* and that neither pass produces *"ready-to-ship artifacts."* Computing Pass@k/recall@k/MRR against the live system requires code and a golden set that doesn't exist. Given a brief this concrete, the realistic outcomes are Fable burning pass budget on it or inventing a plausible-looking scorecard. Reword to "specify the baseline measurement Mark's build should run," or address it explicitly to Pass 2.

**5. The newest edits silently invalidated round 2's delivery-method resolution.**

The decision log records the delivery question as resolved because *"Mark is pasting the brief into a new Fable thread directly rather than via repo access."* But the material added since then makes the brief **depend** on repo access: the preamble now instructs *"Read the raw documents themselves, not just what this brief quotes"* (~800KB across 17 docs); §10 #8 instructs `git show CiC-Fable-Experiment:World-Builds/...`; §10 #8 instructs *"Check what actually exists per world before citing one."* Under paste-only delivery a large fraction of the brief's instructions are dead, and the "verify against primary sources" discipline the brief leans on throughout cannot happen. Good news: everything is now committed (all 18 research files and the brief are tracked; working tree clean), so repo delivery is viable — but this needs an explicit decision before sending, not an inherited assumption.

**Resolved same day, 2026-07-26:** Mark confirmed repo-access delivery — this review and the standard-practice doc below are being committed specifically so Fable can read them alongside the rest of the research corpus. P0 #5 is closed.

---

## P1 — materially improves the result

**6. §6's eighth job has no field anywhere in §9 — the brief commits the exact failure mode §6 names.** §6 says *"The failure mode is a job with no field responsible for it,"* and job 8 (contestation/pressure-holding) adds *"No other job above owns this."* Yet §9 — seven paragraphs, ~1,260 words, four added this round — never mentions contestation. Every one of the other seven jobs gained new fields this round (`period_sense`, `semantic_domain`, `field_relations`, `register`, `attribution_status`, `discovery_channel`, the three confidence axes, eviction priority). Job 8 is served only by a runtime mechanism (§10 #5) and a metric (§10 #9), never by a record field.

**7. §7 contradicts §5c and doc 15 on whether eviction ranking exists.** §7: *"Explicit permanence/eviction ranking on every field... **CiC has no equivalent today.**"* Doc 15 corrects this explicitly: `## Quick Meaning` *"is the persona-framework 'permanence/eviction ranking' concept doc 09 flagged CiC as lacking — **except CiC does have it, in the data, and the runtime discards it.** That is a plumbing defect on top of a correct design, which is a much better position than a missing design."* The brief folded doc 15 into §5c (which now says Quick Meaning exists and is dropped by the parser) but left §7's contradicting sentence untouched.

**8. Eviction priority / cache stability is filed in the wrong paragraph.** It sits inside the paragraph that opens *"Operational/variable parameters are **not** content records"* — but a field's eviction priority and cache stability are per-field schema attributes, not tunable operational values like turn caps. Move to the schema material; it also belongs with the §7 correction above.

**9. "the one recommendation in this whole research arc with a controlled measurement behind it" is false, and falsified by the brief's own next sentence.** Doc 16 scoped that claim to *"this document,"* not the arc — and doc 16's finding 2 (Roque & Traum's Degrees of Grounding, *"improved appropriateness-of-response at p<0.01 and p<0.05"*) is also controlled, and doc 16 calls it *"the highest-value structural fix in this document."* That is the very next requirement in §10 #5. The superlative creates a priority inversion, telling Fable the direct-address rule is uniquely well-evidenced and quietly demoting the mechanism doc 16 ranks first.

**10. Doc 16's highest-severity grounding finding is absent, and it directly qualifies §3's constitutional framing.** Doc 16's Tier-1 fix 5: Facilitator turns are excluded from the public transcript (`if msg.name == "facilitator": continue`), which *"silently breaks the modern-term bridge's own repair mechanism"* — described as *"the cheapest fix to the highest-severity grounding gap found."* Critically, doc 16 argues this **tightens** rather than loosens the boundary: *"the boundary says only spoken words cross. The Facilitator's words are spoken. Excluding them was never what the boundary required."* §3 currently presents the isolation boundary as a constitutional line Fable must flag before breaching, with no hint that part of its current implementation exceeds what it requires. Two of doc 16's five Tier-1 fixes made it into the brief; this is the one that matters most.

**11. The doc-14 recall-channel claim is presented as measured and isn't.** Brief: *"the one real live-fabrication pattern found in this project's own record concentrated specifically in unlabeled recall-sourced entries."* Doc 14 cannot measure concentration — its central finding is that discovery channel was **never recorded** (*"the schema records how well the source was checked and never records where it came from"*). The fabricated-precision rows are **Syriac**; the rows explicitly declared recall-sourced are **Imperial-Juridical**. Doc 14's actual claim is characterological (*"the recall channel is exactly where the fabricated precision lives"*), not a distributional finding. This is the closest thing in the new material to round 1's fabricated-composite class.

**12. The attribution-status claim rests on a Medium-confidence finding whose editorial wording doc 12 explicitly fenced off — and the brief describes CPG using CiC's own vocabulary.** Doc 12: *"Confidence: Medium (Brepols and Corpus Christianorum project pages; I did not consult the printed Clavis)"* and *"the exact editorial language is not verified."* CPG's marked values are **genuine / dubia / spuria**; "pseudonymous" is a value in **CiC's proposed** controlled vocabulary, imported back into the description of CPG. "Basic organizing distinction" also overstates — CPG's organizing principle is per-author numbered listing. This is §9's highest-severity gap, stated flatly.

**13. "Author Gravity" is orphaned and miscategorized.** It appears exactly once in the brief (§10 #2), undefined, inside a list ending *"everything doc 12 recommends."* In doc 12, Author Gravity appears exclusively under **what CiC already does at academic standard** and as the baseline against which gaps are stated — it is not in doc 12's Tier 1/2 field recommendations. Fable will not know what it is, and will be told an existing strength is a new recommendation. Doc 11 flagged Author Gravity as omitted; the fix put it in one parenthesis and nowhere else.

**14. §10 #3's doc-17 warrant overstates its source.** Brief: *"the sequence itself checks out against real methodology in every field with a published answer."* Doc 17: *"either endorses context-before-persona **or is silent**. Nobody recommends the reverse."* And doc 17 §2a's own heading: *"'Build the world before the character' is not an established principle. **The opposite is closer to consensus.**"* All four of doc 17's area verdicts are PARTIAL; three name a REAL GAP; the living-history endorsement is *"High for the sequence, as a verified table of contents. I did not read the book."* The operative ask (add a gate, don't reorder) is right; the warrant is stronger than the evidence.

**15. §10 #3's causal clause is contradicted by doc 17's own chronology.** *"reached zero of five deployed Permanent Prompts because no multi-voice test ever ran until the sixth and last world's did."* Doc 17 records three-Representative live testing 07-11→07-13, a multi-world acute-distress test on 07-17, and the four-voice roundtable — all before IJC Round 4 on 07-20. Doc 17's claim is narrower and sharper: this *specific* convention was never checked, and no multi-voice test was ever a **per-world gate** (*"never inside a world's own build loop"*). The narrower version is also the better argument for the gate the deliverable is asking for. Doc 17's qualifier is also dropped: the fix propagated *"once, manually, at Mark's direct request, after six worlds."*

**16. Confidence caveats are dropped systematically across the new material, and §2 shows the brief knows better.** §2 caveats the cost baseline carefully. The new material states flatly:
- the ~25% pushback-reversal figure — doc 16 rates finding 5 **Medium** and lists it under *"Do not cite"*: *"These come from a fetch-summary of the HTML, not my own read... verify the specific numbers before citing them."*
- Barr's illegitimate totality transfer — on doc 13's **"Do not cite"** list: *"I did not read Barr. Cite the terms and the target (Kittel's TDNT)."* The brief drops the named target and the paired **root fallacy** doc 13 instructs citing alongside it.
- Archer's morphogenetic cycle — **Medium-High**, *"I did not read Realist Social Theory,"* plus a scope caution (*"not adopt critical realism as CiC's philosophy of history"*) and the **stasis** outcome, both dropped.
- the LoC scaffold and the Chicago §3d finding — both **Medium**.

None of these individually changes the design. Collectively they mean a Fable instructed to verify will find the brief's standard of care uneven, which undercuts the whole verification posture.

**17. §9 has become a stack of addenda, and it models the opposite of what §10 #1 asks for.** Seven paragraphs, six opening with a bolded "One X…"/"Every X…" formula, three consecutive paragraphs beginning with the literal word "One," no sub-headings, and one ~350-word block covering four sense fields plus `semantic_domain` plus `field_relations` plus Barr. Meanwhile §10 #1 asks Fable for *"concrete field-level specification tables."* A single consolidated field table at the end of §9 would fix the readability problem and demonstrate the format being requested.

**18. The new §9 material walks into §7's own headline warning with no link between them.** §7 leads with doc 09's parroting verdict: *"A world's own distinctive vocabulary in the retrieval/persona slot is the highest-parroting-risk configuration there is."* §9 then adds a four-field block that substantially expands the world-vocabulary surface, and §10 #2 routes `period_sense` directly into Level 1 conversation. Nothing connects them. §7 explicitly asks for *"an explicit guard against parroting instead of voice"* — the new material increased the exposure without acknowledging it.

**19. "Construction Framework" is ambiguous in the sentence that most depends on it.** Doc 17's "table = 0" count is for the **world-build** Construction Framework V7.4. §3 names `CiC_L3C_Representative_Construction_Framework_V3.2.docx` as current; doc 17 records **V3.2 mentions "table" 5 times** — *"the only real bridge, and a thin one."* §10 #3 references both V7.4 and V3.2 in the same block. Also dropped: the mirror statistic, *"Facilitator Governance V3.6 mentions forces and gravities **zero** times"* — *"not underused, absent"* — which supports §5d's thesis more directly than anything currently in the brief. Relatedly, *"the three governing documents this redesign touches"* doesn't match §3's four named documents: doc 17's trio is V7.4 / Table Design V2.3 / Facilitator Governance V3.6, excluding the Constitution and V3.2.

---

## P2 — polish

- **`p<0.001` against "both of today's two turn-selection approaches."** The measurement was against the paper's own two baselines (EQUAL, SS) in a Murder Mystery Agents system. Doc 16 does map CiC's engines onto their *failure modes* (*"the plain endpoint is equal rotation, the streaming selector is holistic self-selection-by-proxy"*), but also says plainly *"CiC's streaming selector implements neither rule."* A compression, not a fabrication — one clause fixes it.
- **"roughly the first 150 words"** vs doc 15's "150–170 words," and doc 15 rates the exact cutoff **Medium** (*"256 word-pieces is not 256 words, and the ratio differs for Greek and Syriac script"*).
- **Desert has no `Quick Meaning` at all (0 of 9).** Doc 15 flags this as a build-completeness gap *"this recommendation depends on closing."* §5c's fix is stated without its prerequisite.
- **The LoC scaffold is relocated.** Doc 12 places Observe→Reflect→Question as *"the top layer... with the full registry row reachable beneath it"* — the layer **above** Level 3. §10 #2 says Level 3 itself is presented as the scaffold.
- **LSJ appears in no research doc** (0 hits for `LSJ|Liddell` across all 18 files). The LSJ→Lampe supplementation argument is unsourced; doc 13 explicitly declines to re-verify the Begriffsgeschichte/Lampe grounding, inheriting it from the brief.
- **Louw & Nida is New Testament Greek**; *"this exact Christian-Greek vocabulary"* overstates for the Syriac and Latin-juridical worlds.
- **Doc 14's headline shape constraint is missing**: *"Do not adopt PRISMA proper, do not pre-register a protocol, and do not aim at comprehensiveness"* (STARLITE over PRISMA). And §8 objective 1 — the objective doc 14 actually governs — still says only *"collecting, organizing, and rating,"* never discovery.
- **§10 #9 omits cost as a measurement category** even though its own design-quality test is *"every §8 objective having a corresponding deliverable"* and §8 objective 6 is cost. Either name it a sixth category or explicitly delegate it to #7.
- **Doc 16's resolved drift-signal count isn't folded in.** §3 still calls it *"an unresolved drift-signal count"*; doc 16 answers it (*"10 in the monitoring prompt, 12 accepted, 15 declared, 17 actually emitted"*) and ties the answer to §9's own operational-parameters requirement. Doc 16's *second*, worse drift bottleneck (`pending_guidance` as a single-slot dict) is also absent, while §3 names only the first.
- **"the cheapest way to force them to"** is the brief's superlative, not doc 17's (zero hits for `cheap` in that sense). Doc 17 assigns the vocabulary-seam fix to a *different* recommendation (rec 3, "make the seam a documented interface") and cautions against solving it with a test: *"making the shared layer explicit is the fix; adding a seventh drift monitor is not."*
- **§5a's "third instance of the same pattern" is not doc 17's diagnosis.** Doc 17 frames the missing Facilitation Brief as end-of-sequence attrition (*"A hand-authored artifact at the end of a 17-step sequence is the thing that gets dropped"*), not prose/structured-artifact desync. The 2-of-6 and last-world-has-none numbers are exact and High-confidence.
- **§10 #9 cites doc 11's catch as precedent** (*"the same check that caught two missing ones in an earlier draft"*) while the preamble tells Fable doc 11 is historical. Harmless but slightly confusing.
- **Research-layer conflict, not a brief error:** doc 12 and doc 14 disagree on whether source-registry row 33 belongs to W1 or Syriac. The brief follows doc 12 and is right.

---

## Answers to the four structural questions

**Balance: materially better, but watch absolute length.** Requested split — preamble + §1–§5 vs §6–§10 — is now **46.5% / 53.5%** (3,861 / 4,445 words), against round 1's ~68/32. The ask now outweighs the diagnosis. But total length grew **~3,300 → 8,306 words**: the diagnosis half nearly doubled (+95%) and only lost the ratio because the ask grew faster (+238%). The round-1 failure mode ("an excellent re-diagnosis with a thin design attached") is genuinely addressed. The new risk is different: 8,300 words of brief plus 17 required documents (~800KB) is a large orientation load before any design work starts, which makes P0 #5 (delivery method) more consequential than it looks.

**Cross-references: clean.** All 27 `§N` occurrences resolve to the right section — §3 governing, §4 six items (six bullets confirmed), §5a fan-out, §5c retrieval, §5d relational, §6 eight jobs, §7 external patterns, §8 objectives (2 and 3 map correctly), §9 dataset shape, §10 passes. Nothing broke in the renumbering. Also confirmed: all six §8 objectives still have a §10 home (round 1's structural bug stayed fixed).

**§9 coherence: coherent in argument, incoherent in form, with two real defects** — the eviction-priority mis-filing (P1 #8) and the missing contestation field (P1 #6). No paragraph contradicts another *within* §9; the contradiction is between §9's new material and §7 (P1 #7).

**§10 overlap: #9 doesn't duplicate #7 or #8, but three deliverables now independently require baselining against today's system** (#7 cost, #8 turn-by-turn transcript comparison, #9 scorecard) with no statement of how they relate. #9's "held-position / concession rate" also overlaps #5's third requirement and #8's pressure test. Worth one sentence sequencing them.

**On framework sourcing:** Boehm and Wang & Strong appear nowhere in the research docs *and nowhere in the brief* — §10 #9 uses the validation/verification distinction unattributed and "field-completion rate" with no framework named. So two of #9's five categories have no external anchor, which weakens its own instruction to *"borrow real, external frameworks rather than inventing metrics from scratch."* Naming them would be a cheap improvement.

---

## Prioritized fix list

**Before sending (P0):**
1. ~~Rewrite §4's certainty-distortion clause...~~ **Closed 2026-07-26** — rewritten to doc 13's own formulation ("CiC is defending both directions"), `epistemic faithfulness` added.
2. ~~Reattribute the 40–100% figure...~~ **Closed 2026-07-26** — reattributed to docs 01/03, corrected to the real 7–100% span across two fields, three of six worlds.
3. ~~In §10 #9, drop or properly source the RAG Triad...~~ **Closed 2026-07-26** — replaced with doc 13's groundedness/AIS finding; "zero API cost" replaced with the real golden-set authoring cost.
4. ~~Reword §10 #9's closing instruction...~~ **Closed 2026-07-26** — reworded from "run this" to "specify this," with the reason (Pass 1 is a design document, not code) stated inline.
5. ~~Decide delivery method explicitly.~~ **Closed 2026-07-26** — Mark confirmed repo access.

**All five P0s closed as of 2026-07-26.** The brief is clear to send on the P0 standard; 14 P1 and 12 P2 findings below remain open by choice, same as after round 2.

**Materially improves it (P1) — all 14 closed 2026-07-26:** added a `contested_claims` field for job 8 to §9 (#6); fixed §7's "no equivalent today" against doc 15's Quick Meaning finding (#7); moved eviction priority/cache stability into §7 as per-field schema attributes, out of the operational-parameters paragraph (#8); dropped the "one recommendation in this whole research arc" superlative in §10 #5, corrected the p<0.001 baseline description, and gave Roque & Traum its measured due (#9); added doc 16's Facilitator-turns-in-public-transcript finding and its boundary clarification, plus the resolved drift-signal count and the `pending_guidance` bottleneck, to §3 (#10); softened the doc-14 recall-channel claim to doc 14's actual characterological framing (#11); caveated attribution_status/CPG (Medium confidence, project pages not the printed Clavis) and fixed the values to genuine/dubia/spuria in both places (#12); defined Author Gravity in §10 #2 as an existing strength doc 12 uses as its own baseline, not a doc-12 recommendation (#13); corrected §10 #3's doc-17 warrant to "endorses or is silent; nobody recommends the reverse," checked against all four fields (#14); narrowed the "no multi-voice test ever ran" clause to "was never checked as a per-world gate," restoring doc 17's actual chronology (#15); restored dropped confidence caveats on the ~25% pushback figure, Barr (plus the paired root-fallacy term and Kittel's TDNT target), and Archer's morphogenetic cycle (plus its stasis outcome) (#16); added a consolidated field table at the end of §9 (#17); connected §9's expanded vocabulary surface directly to §7's parroting warning (#18); disambiguated Construction Framework V7.4 vs V3.2 and restored the Facilitator-Governance-zero-mentions mirror statistic in §10 #3 (#19).

**Also folded in while fixing the above, since the same sentences were already open:** the LoC scaffold's placement above Level 3 rather than as Level 3 itself, the Chicago/Turabian citation-convention confidence caveat, and the "cheapest way to force them to" superlative softened to "one low-cost way."

**Polish (P2):** the twelve items listed above — none blocking.

Every P0 is a one-to-three-sentence edit. The brief's substance is sound; what it needed was a correction pass over material nobody had yet read skeptically, not restructuring.
