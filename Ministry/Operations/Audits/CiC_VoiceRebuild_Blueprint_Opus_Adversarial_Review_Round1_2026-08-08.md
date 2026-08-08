# Adversarial review (round 1): `CiC_VoiceRebuild_Stage3_Blueprint_2026-08-08.md`

*Opus review, dispatched 2026-08-08. This is the Stage-3 (Blueprint) gate required by the brief's §9 — the pass that decides whether Build is allowed to execute this sequence. Per the Standard Practice's point 4, the brief, the Stage-1 Research findings, the approved Stage-2 Design, and the whole Design review artifact (Round 1 + re-check addendum + final addendum + the `5e5871d` sign-off) were read before any new hunting began, so this round is aimed at what has never been checked: the sequencing itself, its checkpoints, and its budget.*

*Named failure modes hunted, per point 5, in this thread's proven forms: (1) new positive prose at ~1 P0 per 350–500 words — this document is 1,734 words and is ~100% new positive prose, so the prior is ~3.5–5 P0; (2) replacement/derived facts wrong, cost figures and counts specifically; (3) "already exists / already built" claims and their inverses; (4) a claim corrected at one site and left standing at another; (5) sequencing that silently contradicts the Design or brief it claims to implement; (6) a checkpoint bar that cannot be evaluated with the named instruments.*

*Verification method, per points 1 and 3. Every factual claim executed or opened at source. `voice_rebuild_research_probe.py` read at `SCENARIOS`. `voice_rebuild_research_probe_results.json` re-parsed and re-tallied per turn — word counts, words/sentence, FK, and every usage record grouped by turn and by label. `scripts/` enumerated. All six Desert `demonstration/*.md` read at `trait_scores` and the proposed rank key re-implemented against them by hand. `wrs/views/segments/demonstrations.py`, `identity.py` and `craft.py` read whole. `wrs/parameters.yaml` read at `reading_floor`; `wrs/gates/core.py:211` read at `readability_check`'s signature. `app/graph/nodes.py:1617-1676` re-read at `HARD_CEILING_WORLDS`, `RETRY_TRIGGER_MULTIPLES` and the regenerate branch. `Decision-Log.md:65` re-read and its arithmetic re-derived. Research §3.1's twelve-file readability table and §5.2's Papnoute result re-read at source. Every `§N` pointer in the Blueprint extracted and resolved by hand. Word counts computed per section. Design commitments enumerated and mapped in both directions, counted.*

---

## Bottom line

**Not ready. Build must not execute Phase 0.3's readability line, Phase 0's insight-field branch claim, Phase 1's gate-enforcement boundary, Phase 2's deploy/checkpoint ordering, or any checkpoint carrying the Objective-3 bar as written.**

**5 P0. 12 P1. 8 P2.**

The document is a real blueprint, not a re-statement of the Design with headings. It preserves the brief's risk order exactly, places all four of Mark's decision points at defensible moments, names an on-fail action for every checkpoint, adds a genuinely better answer than the Design had on baselines (a committed six-world pre-rebuild set rather than a diff against transcripts that don't exist in-repo), and flags one sequencing either/or with its rejected alternative and reason. Its balance is healthy: 1,734 words, of which framing (title block + §0) is 204 = **11.8%**, and sequenced work (§1–§5) is 1,359 = **78.4%**. The failure mode Round 1 named for the brief — an excellent re-diagnosis with a thin plan attached — does not recur.

**And its hardest factual claims survive checking.** I re-derived the cost arithmetic, re-tallied the probe results, re-implemented the selector's new rank key against Desert's actual records, and re-read the two harness files it names. Five of the six claims the dispatch flagged for verification are correct, one of them non-obviously so (see *What verified clean*).

**What blocks is a different class: five places where the sequence, executed literally, does something it cannot do or should not do.** Three of them are single-clause errors about the readability gate — a floor that does not exist in the file it cites, an enforcement boundary set one phase before the content it gates is rebuilt, and a pass bar with no baseline. The fourth is the document's own headline claim about Mark's decision branch, which is false. The fifth is an ordering hole in Phase 2 that puts an unverified voice on the participant-facing read surface before the checkpoint that is supposed to gate it, with no named revert.

None of the five is a writing problem. Each one, executed as written, spends the expensive stage on work that stalls, mis-measures, or ships red.

---

## P0 — fix before this document gates Build

### P0-1. §0's headline claim — "Phase 0 and Phase 1 are identical under both branches" of Mark's insight-field call — is false. The fallback branch is a code change that lands in Phase 0.2, and Checkpoint 0's leak-gate exit condition presupposes the other branch.

§0: *"**The one decision needed before Phase 2 starts (not before Phase 0):** Mark's insight-field scope call (Design §2 Layer 5 / §7) — extend the prose-style license to `Ecological Function`/`Formation Ecology Connection` for content-preserving rewrites, or use the serialization-side strip. **Phase 0 and Phase 1 are identical under both branches**; the branch is taken at Phase 2's first world."*

Design §2 Layer 5, verbatim on what the fallback actually is: *"If Mark declines, the fallback is serialization-side: those fields render through **an apparatus-sentence strip (code, not file edits)**, accepting cruder prose in exchange for untouched files."*

That strip is serialization-path code. Phase 0.2 is *"Serialization + leak gate,"* and it is the phase item that touches exactly that path (`truncate_at`, `_VOICE_UNSAFE_SECTIONS`, the tiered gate, the `retriever.py` sort key). So under the fallback branch, Phase 0.2 gains a work item — an apparatus-sentence strip for two named fields across 118 lexicon and 60 story chunks — that does not exist under the authoring branch. Phase 0 is not identical under both branches; it is the phase the branch most concretely changes.

**The same error propagates into Checkpoint 0's exit condition.** Checkpoint 0: *"leak gate runs clean on hard-fail classes **or names exactly the files Phase 2 must fix**."* Per the Design review's re-partition of the committed audit (104 flagged files → 61 hard-fail after the 23 out-of-section and 20 Usage Guidance files go report-only), the hard-fail class is dominated by apparatus inside `Ecological Function`/`Formation Ecology Connection` bodies. Under the authoring branch those are *"files Phase 2 must fix."* Under the strip branch there are no files Phase 2 fixes — the remedy is code, in Phase 0, and the gate's own target (source file vs. serialized output) has to be decided differently. Checkpoint 0 as written can only be evaluated on one of the two branches.

**And the deferral itself contradicts the Design.** Design §7: *"one scope call needed **BEFORE Build starts**: whether the prose-style license extends to the two insight fields."* Design §2 Layer 5: *"needs Mark's scope call **before any file is touched**."* Phase 0 is Build. The Blueprint moves a call the Design placed before Build to "before Phase 2," and justifies the move with a branch-independence claim that isn't true. This is the named failure mode "sequencing that silently contradicts the Design it claims to implement," and it is in the document's most prominent paragraph.

**Why this blocks.** §0 is what Mark reads to decide when he has to answer. If he is told the answer isn't needed until Phase 2 and he picks the fallback, Phase 0 has already been built and gated without the item the fallback requires, and Checkpoint 0 has been signed against a condition that doesn't apply.

**Fix.** State the true dependency: the branch determines whether Phase 0.2 carries an apparatus-sentence strip and whether Checkpoint 0's hard-fail residue is a Phase-2 file list or a Phase-0 code remedy. Either keep the Design's "before Build starts" placement, or state explicitly what Phase 0 builds under each branch and make Checkpoint 0's exit condition branch-aware.

---

### P0-2. "Per-world floor from `wrs/parameters.yaml`" — there is no per-world readability floor in that file. It carries one fleet-wide floor, and asserting per-world floors silently pre-empts the Albina values call this same document reserves for Mark.

Phase 0.3: *"Readability gate wired at assembly time (**per-world floor from `wrs/parameters.yaml`**), warn-only in Phase 0…"*

`wrs/parameters.yaml`, the whole of the relevant block:

```yaml
  reading_floor:
    flesch_kincaid_grade_band: [8, 10]
    flesch_reading_ease_min: 60
    source: >-
      L3C-Representative-Methodology/CiC_L3C_Representative_Construction_
      Framework_V3.2.docx, Part Five - "a Flesch-Kincaid grade band of roughly
      8 to 10 and a Flesch Reading Ease of 60 or above ..."
```

One floor, fleet-wide, sourced to Part Five. There is no per-world entry anywhere in the file (the per-world keys it does carry are `prefix_budget_per_world` and the multi-world turn caps, neither of them readability). `readability_check(text, fk_max=10.0, fre_min=60.0)` takes overrides as arguments, but no per-world values exist for anything to read.

**This is not a wording slip, because of what a per-world floor would mean.** Design §7 reserves for Mark exactly one decision about this floor: *"the Albina exception (on her first rebuilt output number, §4 item 1)"* — whether her sentence length comes down or *"a recorded, named exception to the floor for her world specifically."* The Blueprint itself honours that at Phase 2 item 4. But if Phase 0 has already wired a **per-world** floor, the exception is implemented by construction before Mark is asked, and the two sections of this document disagree: Phase 0 says per-world floors exist; Phase 2 treats a per-world exception as an open values call.

**Why this blocks.** It is a false claim about a named file, in a Phase-0 gate item marked [G] that four later phases depend on, and the false version of it decides a question the document elsewhere says is Mark's.

**Fix.** *"Readability gate wired at assembly time against `wrs/parameters.yaml`'s `reading_floor` (FK ≤ 10 / FRE ≥ 60, fleet-wide — the file carries no per-world floor); a per-world exception exists only if Mark grants one at Albina's checkpoint (Design §7), and is recorded there."*

---

### P0-3. "Enforcing from Phase 1 on" turns a hard readability gate on across the fleet at a boundary where five of six worlds' measured voice-bearing text fails it — and four of those five are not rebuilt until Phase 2, two of them not until worlds five and six.

Phase 0.3: *"Readability gate wired at assembly time (…), warn-only in Phase 0 (no rebuilt content yet), **enforcing from Phase 1 on**."*

Research §3.1 ran the project's own gate against all twelve voice-bearing files. The failures:

| File | FK | FRE | Verdict | Rebuilt at |
|---|---|---|---|---|
| Marius prompt | 11.6 | 59.8 | fail both | Phase 2, world **2** |
| Yausep prompt | 10.0 | 65.0 | fail (FK at line) | Phase 2, world **6** |
| Hieronymian capsule | 11.5 | 59.0 | fail both | Phase 2, world **1** |
| IJC capsule | 12.5 | 57.2 | fail both | Phase 2, world **2** |
| PAHC capsule | 13.3 | 56.1 | fail both (worst of 12) | Phase 2, world **5** |

Design §2 Layer 5 defines the assembly-time wiring as *"a floor check on what we ship"* against *"the assembled prompt+capsule text."* The Blueprint's own rationale for warn-only in Phase 0 is *"no rebuilt content yet"* — which is equally true of Phase 1. Phase 1A is a shared-block edit run live against Chloe; Phase 1B runs Desert's **current** records. Neither phase rebuilds a single world's voice content. The stated reason for warn-only does not stop applying at the Phase-0/Phase-1 boundary; it stops applying at each world's own Phase-2 pass.

Executed literally: at the start of Phase 1, the gate runner and CI that Phase 0.3 wires *"per world"* go hard-red on at least five files, and the Blueprint's own Checkpoint-0 rule — *"nothing in Phase 1+ starts on a red foundation item it depends on"* — makes that a stall rather than a warning. Phase 1B explicitly lists the readability gate among the machinery Desert runs through; Desert passes (prompt 9.7/62.4, capsule 9.6/66.3), so 1B survives, but the fleet-wide gate does not.

*Stated honestly:* the measured numbers above are for the **deployed** files. Only Desert's assembled output is known to be identical to its deployed file; the other five worlds' assembled output has never been measured. So this is an inference — but it is the only evidence available, it runs one way, and the Blueprint offers nothing against it.

**Why this blocks.** It is a gate switched to enforcing one full phase before the phase that produces the content it gates, with no per-world carve-out, in a plan whose own discipline forbids proceeding on a red gate.

**Fix.** One clause: *"enforcing per world from that world's Phase-2 pass onward; warn-only for any world whose records have not yet been rebuilt."* That is already how Phase 2 item 2 reads (*"all build gates green"* at each world's own pass) — Phase 0.3 just contradicts it.

---

### P0-4. "Objective-3 read ≥ baseline" is a pass bar at every checkpoint from 1A onward, and no baseline Objective-3 read is sequenced anywhere. The bar cannot be computed from what Phase 0 builds.

Checkpoint 1A: *"Objective-3 read scores **at or above baseline**."*
Phase 2 checkpoint: *"Objective-3 read **≥ baseline**."*

What Phase 0 actually builds, in full: 0.4 *"write the Objective-3 checklist instrument sheet from the Research §6 rubric rows"* — the instrument — and 0.4's baseline bullet, *"re-run the full battery (8-turn + disagreement) against ALL SIX current worlds and commit transcripts + metrics."* The battery is a harness run. The Objective-3 read is not a harness output.

Design §5 is explicit about what this instrument *is*: *"a structured human-read checklist… the read of record is **one reader (Mark or his designee) scoring the transcript twice on separate days**, with any self-disagreement re-read rather than averaged… Human reading is the instrument here by design; an LLM judge may *assist* but the score of record is the read."*

So the baseline half of every Objective-3 bar requires a human double-read of six worlds' baseline transcripts — twelve read sessions, on separate days, by the project's single scarcest resource — and the Blueprint never schedules one. "Objective-3" appears exactly three times in the document: once to write the sheet, twice as a bar. Never as a read event, never in Checkpoint 0's exit conditions, never in the budget section, which costs only live battery turns and treats Mark's time as free.

**Why this blocks.** This is the dispatch's named class exactly: a checkpoint bar that cannot be evaluated with the instruments the plan names. It sits in the pass bar of the pilot checkpoint and all six per-world checkpoints — seven of the plan's nine gates — and it is the *only* instrument in the whole verification design that measures Objective 3's positive goal, the objective the brief §6 says carries exactly as much weight as Objective 4.

**Fix.** Add the baseline Objective-3 read to Phase 0.4 as its own [G] item with its own resourcing (six transcript sets × two reads on separate days), name it in Checkpoint 0's exit conditions, and put the per-checkpoint read into §7's cost line as a schedule cost, not only a dollar cost. If Mark's time cannot carry fourteen double-reads, say so here and reduce the bar deliberately — do not leave it stated and unresourced.

---

### P0-5. Phase 2's item order puts the rebuilt voice on the participant-facing read surface *before* the checkpoint that is supposed to gate it, with no named swap step and no revert.

Phase 2's per-world structure, verbatim: *"1. Records rebuilt fresh… 2. Assemble; all build gates green… 3. **Checkpoint (per world): the full battery live**… **the world does not ship red**."*

The battery is live: it runs through the real backend (`TestClient` on `app.main`, the harnesses the Blueprint names). The runtime reads `data/<world>/*_Representative_Permanent_Prompt_*.txt` and `*_World_Capsule_Core.md` — `main.py:156`, unchanged by this design, as Design §1 says explicitly. Therefore the assembled prompt has to be **written into `data/`** before step 3 can measure it at all. Otherwise the "full battery live" measures the old hand-authored prompt and the checkpoint grades the wrong artifact.

Neither reading is safe as written:

- If the swap happens before step 3 (the only way the checkpoint means anything), then every world is deployed to the live read surface *before* its checkpoint runs, and "the world does not ship red" is unenforceable — it has already shipped. There is no revert step, no staging path, no "restore the previous file on fail" anywhere in the document.
- If the swap happens after step 3, the checkpoint is measuring the pre-rebuild voice and every Phase-2 pass bar is vacuous.

**This is the single production-facing state change the whole architecture turns on** — Design §1: the six `data/` files *"become build artifacts: emitted by the per-world assembler, marked generated-do-not-hand-edit, regenerated on any record change."* It is named nowhere in the Blueprint as a step. Checkpoint 0 implies it (*"deployed is still hand-authored until each world's Phase-2 pass"*), which is the only place in the document that acknowledges a swap exists at all.

**Why this blocks.** Build executes this literally, on the live participant-facing surface, six times. An unverified voice reaching participants with no named rollback is not a sequencing nicety.

**Fix.** Make the swap an explicit numbered step between 2 and 3, with the prior file retained and a stated revert-on-fail: *"2b. Emit to `data/`, marked generated-do-not-hand-edit, retaining the prior file; on checkpoint fail, revert `data/` to the retained file before iterating."* Also add the generated-do-not-hand-edit marking, which Design §1 requires and the Blueprint never mentions.

---

## P1 — materially improves, not disqualifying

**P1-1. The battery-run count is below its own floor, and "Phase 0/1 spends little" is contradicted by Phase 0's own largest item.** §7: *"on the order of **15–20 full-battery runs** across all phases **including failures** and the fleet regression… Phase 0/1 spends little (one pilot world + one proof world + the six-world baseline)."* Counting only what the document itself schedules, at its own definition of a full battery (14 turns = 8 probe + 6 disagreement), with **zero** failures and zero iterations: Phase 0 baseline, six worlds = **6.0**; Checkpoint 1A, Chloe = **1.0**; Checkpoint 1B, Desert 8-turn = **0.57**; Phase 2, six per-world checkpoints = **6.0** (and each *adds* the confidence-under-thinness and Sustained Engagement categories on top of the 14, so 6.0 is itself a floor); Phase 3 = S6.5 spot batteries (≥1.0) + relational-safety re-run (≥0.5) + `HARD_CEILING_WORLDS` trigger verification in Interview mode (≥0.5) + the `confirmed_glosses` without-arm on one world (1.0) + fleet regression on six (6.0) = **9.0**. Total **≥22.6**, before a single failed checkpoint — against a stated 15–20 that claims to include failures. The checkpoint discipline permits two consecutive iterations before escalation, so a realistic figure is 28–35. Separately, Phase 0/1 alone is 7.6 of the 22.6 — a third of the whole spend, and the largest single block before Phase 2 — which is the opposite of "spends little." The per-turn figure is right (see *What verified clean*); the multiplier is not.

**P1-2. Three of Design §1's four code-side per-world configs are missing or reduced to something else.** Design §1 names four that *"become assembly-fed Blueprint items"*: `HARD_CEILING_WORLDS`, `confirmed_glosses.py`'s per-world lists, the IJC post-history guard extension, and `_migrated_world_ids`'s world_core gate. Counted in the Blueprint: `HARD_CEILING_WORLDS` — fully sequenced (0.1 + Phase 3). `confirmed_glosses` — appears **once**, and only as §3's *retirement* check in Phase 3; the §1 item (its per-world lists become assembly-fed) appears nowhere. `IJC` — appears **zero** times; Phase 2's generic *"per-world post-history guard export"* covers Design §2 Layer 4's six exports but not the IJC-scoped extension at `nodes.py:1174-1181` that Design §1 and §4 item 2 both name specifically. `_migrated_world_ids` — appears **zero** times. Two absent, one substituted.

**P1-3. The sustained-disagreement probe is built and run at every per-world checkpoint and has no pass bar anywhere.** Phase 0.4 builds the 6-turn scripts; Phase 2 step 3 runs them. The Phase-2 pass bar lists five conditions — failure-measure regression, register/measure targets, fabrication 0 confirmed, Objective-3 read, ceiling regenerations — and none of them grades the disagreement probe. Design §5's criterion is specific and absent: *"pass = holds supported positions through turn 6 while conceding any genuinely unsupported claim the script plants,"* scored by the `repair_classifier`'s own three-way rule with *"UNCERTAIN turns route to the human read, never auto-scored."* This is Objective 6's only instrument, six turns per world per checkpoint of real spend, producing data nothing grades.

**P1-4. Design §5's per-world checkpoint instrument list is truncated by roughly half, including the two items §3 makes load-bearing.** Design §5 names, per checkpoint: reclarify openers (regex **plus mandatory manual read**), bridge-first adherence, output FK/w-s per turn, turn length, **per-signal drift**, fabrication/over-settling firing **and confirmed** rates, ceiling regeneration events, **callback and candidate-offer occurrence (manual read against transcript)**, plus the two Part Eight categories. The Blueprint's Phase-2 checkpoint carries the categories, register/measure, fabrication, Objective-3 and ceiling regenerations. Absent: per-signal drift entirely (the word "drift" appears twice in the document, both in Phase 0.4), §3's explicit *"put `FLATTENING` under an explicit verification watch during per-world rebuilds"*, callback and candidate-offer occurrence, bridge-first adherence (named only in 1A), and the over_settling **confirmed** rate — which Phase 3 then relies on as already collected: *"over_settling stage-2 downgrade decision (**confirmed rates now exist per world**)."* The harness surfaces them (0.4), but nothing requires the checkpoint to report them, and §6's discipline is *"numbers recorded in the phase's results file (committed)."*

**P1-5. Two Design mechanisms with no trace in the per-world structure.** (a) Layer 2's pre-committed fallback — *"if a world's Build verification shows positive-only insufficient, contrastive is adopted for that world, recorded, on its own evidence"* — is absent; "contrastive" appears zero times, and the Phase-2 on-fail action is only *"fix records, reassemble, re-run."* This is the Design's single pre-committed answer to the one form question the brief called genuinely open, and Build has no instruction to take it. (b) Layer 3's two design rules — any boundary that must hold under pressure stated *"in at least two segments in different words"*; any style default stated once and demonstrated rather than restated — are absent ("redundan" appears zero times). They govern how the per-world prose is written, which is Phase 2's core work.

**P1-6. `probe_parity`'s redefinition is used as a Phase-2 grading criterion and is not a Phase-0 build item.** Phase 2 step 3 grades against *"the redefined parity criterion (identity/fact/boundary SAME-VOICE; register/measure graded against rebuilt targets)."* That redefinition is a change to `wrs/views/probe_parity.py` and its five per-world variants — a real instrument change, and the only one in Design §5 not sequenced in Phase 0.4. `probe_parity` appears zero times in the document by name. This is the "used before the phase that builds it" check failing.

**P1-7. Both stop boundaries sacrifice Part B — the brief-review R3 P1-7 defect, reproduced and made concrete without a flag.** Stop boundary A is after Phase 1; stop boundary B is after Albina + Marius. Phase 4 (Part Five/Part Eight + the Decision Log entry) is last, so **every** named stop drops it. Part B is brief §7's *"two parts, both required"* and Objective 5, which brief §6 holds apart from the ranking as *"not optional scope; it's the actual point of doing this on a dedicated thread."* Round 3 of the brief's own review flagged exactly this and its fix was never applied to the brief; the Blueprint inherits it and hardens it into named boundaries. Phase 4 is also the cheapest item in the plan — zero battery turns — so it is the one thing that could survive any truncation. **Fix:** one sentence in §7 stating that the Part Five/Eight edits are budget-free and survive any stop, and that a stop drops per-world passes, never Part B.

**P1-8. Design §0's "mixed-provenance numbers the rebuild re-derives" is dropped, so two disclaimed figures become both the live ceiling basis and the grading target.** Design §0: *"not all measured: PAHC's is marked 'DESIGNED, NOT MEASURED', IJC's 'PROVISIONAL PLANNING FIGURE', and Desert's equals the runtime ceiling; **treat the fleet's numbers as mixed-provenance data the rebuild re-derives**."* The Blueprint seeds `ceiling_words` from the current dict *"behavior-neutral by construction — same numbers, new source"* (correct, and the Design's own chosen migration), and then Phase 2 grades each world on *"register/measure hit the world's **recorded targets**."* Nothing in Phase 2 asks any world to re-derive its `native_measure` from rebuilt sources. So PAHC's self-declared-designed 70 and IJC's self-declared-provisional 120 pass through the whole rebuild ungraded and become the bar the rebuilt voice is measured against. Add re-derivation of `native_measure`/`ceiling_words` from sources to Phase 2 item 1, with the freeze rationale re-stated or explicitly retained.

**P1-9. Checkpoint 1A's bar conflates no-regression with absolute zero, and one of its three conditions is not stateable.** *"Chloe's battery does not regress from her Phase-0 baseline on any failure measure (reclarify 0, no new register/measure violations, fabrication 0 confirmed)."* The parenthetical states absolute targets as if they were the baseline. Chloe's own measured baseline is not reclarify-0: the Decision Log's 2026-08-05 run records her opening a turn with *"When I said 'ekklesia' a moment ago — you understand that I mean…"*, one of the two instances that produced the finding. So "does not regress" and "reclarify 0" are different bars and the pilot can satisfy one while failing the other. Separately, *"at least directional improvement on uptake/bridge-first measures"* is not a bar the document's own §6 discipline permits (*"pass/fail stated against the written bar — never 'reads fine'"*) — state a direction *and* a threshold, or state it as reported-not-graded.

**P1-10. The fleet-wide segment-design freeze is relocated one phase earlier than the Design places it, onto Desert's un-rebuilt demonstrations, and the relocation isn't flagged in the section that claims to record the sequencing decisions.** Phase 1B is headed *"Assembly proof on Desert (Design §4 item 4's 'freezes the fleet-wide segment design')."* Design §4 item 4 places that freeze inside **his pass** — his Phase-2 rebuild, world four — and the Design review's P0-2 asked specifically that if the freeze happens on his pass it be stated to happen *"after his demonstrations are rebuilt to his measure, not before."* Phase 1B is explicit that they are not: *"His six demonstrations are NOT yet rewritten in this phase."* Those six overrun his own recorded 60-word measure by 2.4–5.2× (146/164/168/205/218/311). Proving the *render shapes* on un-rebuilt records is defensible — that is genuinely what 1B tests — but the quoted authority does not cover it, and §3's sequencing note claims to record *"the one genuine either/or Design left"* while this second relocation goes unnamed.

**P1-11. Design §4 item 5's pilot property is contradicted: PAHC no longer exercises the Layer-5 mechanisms at maximum load before other worlds depend on them.** Design §4 item 5: *"The pilot therefore exercises **every Layer-5 mechanism at maximum load before any other world depends on them**: insight-field authoring pass, build-time leak gate, capsule regeneration."* Design §2 Layer 5 sets the same priority for the authoring pass: *"prioritized by the audit's rates (**PAHC first at 81%, and it pilots**)."* In the Blueprint, Phase 1A's pilot is the shared block only, and Chloe's insight-field pass and capsule regeneration land at her Phase-2 slot — **fifth** in the risk order, after Albina, Marius, Theon and Papnoute have all had their insight fields rewritten. The gate half is arguably better covered than the Design planned (Phase 0 runs it fleet-wide), but the authoring-pass-first-on-the-81%-world commitment is inverted, unflagged, in the same section that says the brief's risk order is preserved *"because its rationale… outweighs the alternative."*

**P1-12. The per-turn cost is derived correctly and carries an expiry the same source states.** `Decision-Log.md:65`'s entry, which is where the $0.33–0.35 figure lives, also records: *"Sonnet 5's introductory pricing ends 2026-08-31 — per-token cost on every Sonnet call here rises ~50% after that with nothing else changing."* The visible `main_response` is *"only ~65% of the cost,"* so a Build running past 31 August pays roughly 30–35% more per turn than §7's figure. Given P1-1's undercount runs the same direction, the budget line is optimistic on both factors at once. One clause fixes it.

---

## P2 — polish

1. **"the prose-vs-code gap flagged 2026-08-08" resolves to nothing in the repository.** Grepped project-wide: the phrase occurs only in this document. No Decision Log entry, Research section, Design section, or Design-review finding carries it. *The underlying fact is true* — I verified it independently (see *What verified clean*) — but the provenance is invented, which is the instrument-provenance class the Design review's P1-3 named. Attribute it to this Blueprint's own check, or to the probe results file, and cite the evidence.
2. **0.1's section header mis-cites.** *"0.1 Schema + selector (Design §2 Layer 2, §0)"* covers a `ceiling_words` bullet that belongs to Design §2's turn-measure decision part (3), not Layer 2 or §0.
3. **"seeded with the current `HARD_CEILING_WORLDS` values and their freeze rationale" is true for five of six.** ALX, HAL, SYR, PAHC and IJC each carry a dated S6.2 freeze comment at `nodes.py:1617-1645`. Desert's `60` carries none — it predates the S6.2 sessions, and `desertvoice001`'s own note records that the record's 60 was taken *from* the ceiling, not the reverse. Say "their freeze rationale where one exists."
4. **Design §1's "marked generated-do-not-hand-edit" is not sequenced** (see P0-5's fix, where it belongs).
5. **Phase 4 names one of Part Eight's three additions.** Design §6 gives Part Eight the naturalness/register probe category *plus* the sustained-disagreement probe *plus* the per-world checkpoint structure; Phase 4 names only *"the probe category pointing at named instruments."*
6. **Design §1's quality governor is never named as a binding rule.** Its substance survives in the on-fail actions (*"the world does not ship red"*), but *"binding on every Blueprint/Build step"* and *"if assembly flattens any world's voice, that is an architecture defect to fix… never a cost to accept"* is the rule that decides what a checkpoint failure *means*, and it should be quotable in §6's checkpoint discipline.
7. **Phase 1B is not a pure machinery-neutrality test, and the document treats it as one.** Phase 0.2's `truncate_at` fail-closed mode and the `_VOICE_UNSAFE_SECTIONS` addition change what reaches generation at runtime, and Desert contributes 9 of the 23 out-of-section flagged files and 3 of the 20 Usage Guidance files. So a battery difference in 1B could come from retrieval, not assembly. The bar (0/8) is still evaluable; the attribution isn't.
8. **Stop boundary A is unreachable from where §7 invokes it.** *"If budget runs short **mid-Phase-2**, the stop boundaries above are the clean exits"* — boundary A is behind you at that point, and boundary B is only available after Marius. Between them there is no named boundary, though the same sentence's *"a world verified green ships independently"* is exactly the per-world boundary that should be named as one.

---

## What verified clean

Listed because it is most of the document, and because two of these took real work to confirm.

- **The Phase-1B "byte-identical AND schema-normalized" combination is coherent — and non-obviously so.** I checked whether normalizing the score vocabulary and installing the new rank key changes Desert's assembled output. It does not, for four independent reasons, all verified at source: (a) Desert's six demonstration records **already** score in the target vocabulary (`partial`/`strong`) — the vocabulary normalization is a no-op for this world, and the three worlds needing it are HAL/SYR/PAHC; (b) all six carry **exactly the same profile** — one `partial` on `terse economy`, four `strong` — so Design §2's rank key (strong-score count descending, then record id) ties all six at 4 and falls through to id order, selecting `desertdemo001/002/003`, byte-identical to today's `sorted(demos)[:3]` in `demonstrations.py:10-17`; (c) `ceiling_words` cannot reach the rendered text — `identity.py` renders fixed craft blocks from `craft.py`'s `DESERT_CRAFT`, and Desert's measure prose (para 11, *"four sentences is already long for you"*) is authored prose, not a rendered field; (d) no `required` flag exists for Desert until his Phase-2 targeted demonstration. **One caveat worth stating in the document:** byte-identity survives *because* the six records happen to share a profile. A single re-score during normalization — one `partial` promoted, one `strong` demoted — breaks the tie and changes which three assemble. Phase 1B should say the record contents are held constant, not merely that the schema is normalized.
- **"Byte-identical to deployed" for Desert, cited correctly.** Established by the Design review, which re-ran `wrs/views/permanent_prompt.py` and diffed empty against `data/desert_world/desert_Representative_Permanent_Prompt_Papnoute.txt`. Checkpoint 0's *"assembly-identity holds for Desert (already true)"* and its counterpart *"identity with deployed NOT expected yet"* for the other five are both stated exactly right — including the reason, which is the part these claims usually get wrong.
- **"The probe harness covers the two probe worlds today."** `voice_rebuild_research_probe.py`'s `SCENARIOS` is exactly two entries: `syriac-edessa-nisibis` (*"runs FIRST"*) and `desert-monasticism` (*"runs SECOND"*). Correct, and correctly scoped as an extension task.
- **`scripts/freeze_battery.py` exists**, and is better than the Blueprint needs: one script with a `--world` flag replacing six per-world copies, carrying RCF V3.2 Part Eight's eight probe categories plus parroting and pushback, with `freeze_battery_probes/{alx,desert,hal,ijc,pahc,syr}.py` and per-world standards YAML. "Extending its harness shape" is an accurate description.
- **Phase 1B's "0/8 failure measures" for Papnoute matches Research §5.2 exactly** — *"**0 of 8** on every failure measure: no term-first openers, no reclarification openers, no false referents."* The Research caveats (the regex tally is a floor requiring manual read; one `fabrication_adjudication` firing that the Research reads as the system working, not a failure) do not contradict the bar as stated.
- **The cost derivation is right, and holds at battery length.** `Decision-Log.md`'s measured $0.33–0.35 per **4-turn** conversation gives $0.0825–0.0875/turn; "~$0.08–0.09/turn" is the correct derivation and the attribution (*"Sonnet main + Haiku monitoring"*) matches the entry (`claude-sonnet-5` generation, `claude-haiku-4-5` classifiers). I also tested the obvious objection — that per-turn cost inflates as context accumulates over a 14-turn battery — by re-tallying the committed 8-turn probe usage per turn: input tokens run 24k–46k per turn with no upward trend across turns 1–8 in either world, because the per-turn cost is dominated by the re-sent cached prefix rather than by history. The figure travels. (What doesn't travel is the multiplier and the pricing expiry — P1-1 and P1-12.)
- **The `HARD_CEILING_WORLDS` claim is true, and I re-derived it independently.** *"Current 60-word Desert ceiling demonstrably didn't bind solo turns in the Research probes"*: Desert's ceiling is 60 with `RETRY_TRIGGER_MULTIPLES` 1.5, so the regenerate branch fires above 90 words. The committed probe results show turns 1–5 at 144/152/160/187/138 words — five turns above the trigger — against exactly **8** `main_response` calls for 8 turns. Zero regenerations. The ceiling did not fire. Phase 3's verification item is well-motivated (only its "flagged" provenance is not — P2-1).
- **Brief §7's risk order is reproduced exactly** — Albina → Marius → Theon → Papnoute → Chloe → Yausep — and the one sequencing either/or it creates is named, argued, and its rejected alternative recorded with its reason, which is exactly what the Standard Practice asks of a blueprint.
- **Cross-reference integrity: 19 `§N` pointers, all resolve** to sections that exist and, with the two exceptions at P2-2 and P1-10, say what they are cited for. Both quoted fragments from the Design (*"freezes the fleet-wide segment design"*, *"the seventh required output"*) are verbatim.
- **The brief's `wrs/` lockstep requirement (§4.2) is genuinely discharged** by Phase 2's records-then-assemble-then-deploy order, per Design §1 ground 2 — no per-world pass can produce a `data/`-only edit. Worth one sentence saying so, since the brief names it as a hard requirement.
- **Design §5's baseline instruction is honored and improved.** Design said the pre-rebuild reference set is the Research probes' two worlds and that *"Blueprint should not plan diffs against transcripts that don't exist in-repo."* Phase 0.4 commits a fresh six-world baseline instead, and says so in those terms. This is the best single decision in the document.

---

## Completeness mapping, counted (Standard Practice point 3)

**Direction A — Blueprint → Design.** 27 discrete work items across Phases 0–4. **25** trace to a Design section that actually contains them. **1** is Blueprint-originated and flagged as such (the six-world pre-rebuild baseline, which the document explicitly frames as answering the brief's missing-baseline gap). **1** is Blueprint-originated and *not* flagged as new — Phase 3's `HARD_CEILING_WORLDS` trigger-behavior verification, whose stated provenance resolves to nothing (P2-1) though its substance is sound.

**Direction B — Design → Blueprint.** 42 discrete Design commitments enumerated across §§1–7. **24 fully sequenced. 10 partial. 8 absent.**

The 8 absent: `confirmed_glosses` per-world lists as an assembly-fed config (§1); the IJC post-history guard extension (§1, §4.2); `_migrated_world_ids`'s world_core gate (§1); the per-world contrastive-demonstration fallback (§2 Layer 2); Layer 3's boundary-redundancy and state-once rules (§2 Layer 3); the `FLATTENING` verification watch during per-world rebuilds (§3); the sustained-disagreement pass criterion including the UNCERTAIN→human-read routing (§5); the Objective-3 read-of-record protocol and its baseline (§5).

The 10 partial: the generated-do-not-hand-edit marking (§1); assembly-identity taking over `probe_parity`'s drift-alarm role, with parity's own rework unsequenced (§1, §5); the quality governor as a named binding rule (§1); the insight-field call's placement and branch consequences (§2 Layer 5, §7); per-world measures rendering into each world's assembled prose (§2 turn-measure part 2); the mixed-provenance re-derivation (§0); over_settling firing-and-confirmed reporting at the per-world checkpoint (§3); the per-world checkpoint instrument list (§5); Part Eight's three additions (§6); PAHC's Layer-5 pilot property (§4.5).

**Balance ratio.** 1,734 words. Framing (title block + §0) 204 = **11.8%**; sequenced work (§1–§5) 1,359 = **78.4%**; discipline and budget (§6–§7) 171 = **9.9%**. Healthy — this is a plan, not a preamble.

**New-positive-prose prior.** At this thread's measured rate (~1 P0 per 350–500 words), 1,734 words of ~100% new prose predicts 3.5–5 P0. Found: 5. The prior held again, which is the reason this gate exists.

---

## Recommended fix list, in order

1. **P0-1** — §0's branch claim: state what Phase 0.2 builds under each branch and make Checkpoint 0's leak-gate exit condition branch-aware; restore the Design's "before Build starts" placement or justify the move on true grounds.
2. **P0-5** — insert the deploy step into Phase 2 with a retained prior file and revert-on-fail. *The only item that touches the live participant-facing surface.*
3. **P0-2, P0-3** — the two readability-gate clauses. One sentence each.
4. **P0-4** — schedule the baseline Objective-3 read as a Phase-0 [G] item with real resourcing, or reduce the bar deliberately and say so.
5. **P1-3, P1-4, P1-6** — the checkpoint's missing pass bar (disagreement), its truncated instrument list (drift/FLATTENING, callback, candidate-offer, over_settling confirmed rate), and `probe_parity`'s unsequenced rework. These three are what make the Phase-2 checkpoint actually evaluable.
6. **P1-1, P1-12** — recount the battery runs against the phase structure and add the pricing expiry. Arithmetic only.
7. **P1-2, P1-5, P1-8** — the missing configs, the two missing Design mechanisms, and the `native_measure` re-derivation. Each is a named Phase item.
8. **P1-7, P1-9, P1-10, P1-11** — the Part-B stop-boundary sentence, 1A's bar, and the two unflagged sequencing relocations. All prose.
9. **P2 ×8** as one editing pass.

**Then a targeted re-check, not a full round** — provided the fix pass is corrections plus the four or five short new items above. Per the brief's own operating rule and this thread's five-round history: a fix pass that adds substantial *new* positive prose (a rewritten Phase 2, a new phase, a new instrument design) earns another full round; a pass that corrects clauses and inserts named items earns a verification that the ten or so hunks say what the sources say.

---

## Verdict for the Standing Practice's point 6

**Not ready for Build. Not ready for Mark's Blueprint-stage sign-off.**

Stated plainly rather than softened. The Design underneath this reached READY after three passes and is sound; this Blueprint sequences it well in most places and improves on it in one (baselines). But five things in it, executed literally by the expensive stage, would stall a phase, mis-measure seven of nine checkpoints, decide a question reserved for Mark, or put an unverified voice in front of participants with nothing written down about how to take it back. The Standard Practice's own test — could this send Build to do work that cannot be done, or skip work that must be — is failed five times, and four of the five are single-clause fixes.

Nothing here re-opens a Design decision. P0-1 restores a placement the Design already made; P0-2 and P0-3 correct two clauses about one gate; P0-4 adds a resourcing line the Design already specified and the Blueprint dropped; P0-5 writes down a step the architecture already implies. The plan's shape — five phases, dual-track pilot, risk-ordered per-world passes with real per-world checkpoints, fleet closure, framework last — is right, and I would not restructure it.

**Fix the five, land the twelve, sweep the eight, and send it to Mark.**

---

# Targeted re-check — commit `995fe2b`, 2026-08-08

*Opus targeted re-check, narrow scope per the brief's own operating rule (a fix pass that adds new claims earns a re-check of what changed, not a full round). Question: did all 25 findings land at every site, are the replacement facts true, and did the fix introduce new contradictions? Method unchanged — every replacement fact executed or opened at source. The whole document re-grepped for each pre-fix string. `app/config.py` read whole at `Settings`, `WorldConfig`, the `worlds` property and the legacy properties; `.env.example` read; `app/main.py:153-158` re-read at `load_world_content`. Research §3.1's twelve-file readability table re-partitioned by world rather than by file. The §7 turn arithmetic re-summed against the document's own Phase-3 item list. Checkpoints enumerated and the Objective-3 consumers counted. `voice_rebuild_research_probe_results.json` re-checked against the new Phase-3 sentence.*

## Bottom line

**Not ready for Mark's Blueprint-stage sign-off — but one editing pass from it, and no design decision re-opens.**

**1 new P0. 3 new P1. 4 new P2.**

This is a strong fix pass. Twenty-one of twenty-five findings landed cleanly, several of them better than I asked: the staging-then-swap ordering closes P0-5 by construction rather than by exhortation, the Objective-3 baseline read is a gated Phase-0 item with a named reader and a stated consequence, the Part-B stop rule is written as a mini-phase that attaches to *every* boundary rather than as a caveat, and the Phase-2 checkpoint now carries the full Design §5 instrument list with the disagreement bar and the FLATTENING watch stated explicitly. Every one of the eight pre-fix strings I asked to be grepped is gone: `per-world floor` 0, `enforcing from Phase 1` 0, `identical under both branches` 0, `15–20` 0, `spends little` 0, `directional improvement` 0, `recorded targets` 0, `prose-vs-code` 0.

**What blocks is one thing, and it is the named risk exactly: a replacement fact in fix prose.** The mechanism the new staging step names for running the checkpoint against the candidate does not exist. Setting it changes nothing, silently, and the harness reads the live deployed files — which reinstates the precise defect P0-5 was written to close, in the sentence written to close it.

### Round 1 disposition, per finding

| Finding | Landed? |
|---|---|
| **P0-1** insight-field branch claim | **Yes.** §0 now states the Design's own "before Build starts" placement, names the fallback's Phase-0.2 strip, and concedes Checkpoint 0's exit condition "evaluates only on the rewrite branch." The operative deadline ("before Phase 0.2 is implemented") is a sharper statement of the dependency than the Design's own, and is fair. *Residue: Checkpoint 0 itself was not made branch-aware — see N-P2-3.* |
| **P0-2** per-world floor | **Yes, cleanly.** The fleet-wide `reading_floor` is quoted with its actual values (FK band [8,10], FRE ≥ 60 — matches `wrs/parameters.yaml` verbatim), and the reserved Albina call is protected in the same clause: *"never a config default."* |
| **P0-3** enforcement boundary | **Yes.** "Warn-only for any world whose records have not yet been rebuilt… enforces per world, at that world's own Phase-2 pass, and fleet-wide once all six are rebuilt" — which is both correct and better scoped than my proposed fix, since it also names the fleet-wide end state. *One count in the new rationale is wrong — see N-P1-1, and it is my error before it is the document's.* |
| **P0-4** Objective-3 baseline | **Yes, and well.** A [G] item, the Design §5 protocol quoted (one reader, twice, separate days), the reader named before Phase 0 ends, and the consequence stated as a fact rather than a hope: *"seven of the nine later checkpoints cannot be computed."* **That count is correct** — I enumerated the document's checkpoints: Checkpoint 0, 1A, 1B, six per-world, Final = 10 total, 9 after Checkpoint 0, of which 1A and the six per-world checkpoints (7) carry an Objective-3 bar; 1B and the Final checkpoint do not. |
| **P0-5** deploy-before-checkpoint | **Structurally yes, mechanically no.** The ordering is right and closes the defect: assemble to staging → checkpoint against the candidate → swap only on green → `git revert` as rollback → generated-do-not-hand-edit marking, all present. But one of the two named ways to run the candidate does not work — **N-P0-1**. |
| **P1-1** budget count | **Partly.** Restated honestly in turns with the derivation shown, and the "spends little" claim correctly inverted. But the component list omits four of Phase 3's five live-turn items — **N-P1-2**. |
| **P1-2** three missing code-side configs | **One of three.** The IJC guard extension landed (*"Marius's carries the existing IJC extension"*). `confirmed_glosses` still appears once, still only as Phase 3's retirement check — Design §1's "per-world lists become assembly-fed" item is still absent. `_migrated_world_ids` still appears **zero** times. |
| **P1-3** disagreement pass bar | **Yes.** *"Every supported position held through turn 6, every planted unsupported claim conceded, UNCERTAIN turns routed to the human read"* — matches Design §5 including the branch. |
| **P1-4** truncated instrument list | **Yes, in full.** Per-signal drift with the FLATTENING watch explicit, callback and candidate-offer occurrence by manual read, and over_settling firing **and** confirmed rates with the Phase-3 consumer named. |
| **P1-5** contrastive fallback + Layer 3 | **(a) Yes**, with a concrete trigger. **(b) Half** — the boundary-redundancy rule landed verbatim; Layer 3's second rule (a style default stated once and *demonstrated*, never restated) did not. |
| **P1-6** probe_parity unsequenced | **Yes.** Now a Phase 0.4 [G] item, with the reason stated (*"built here because Phase 2's checkpoints consume it"*). |
| **P1-7** Part B sacrificed by stopping | **Yes, better than asked.** Not a caveat but a closing mini-phase attached to any stop at any boundary, with the review history named. |
| **P1-8** mixed-provenance measures | **Yes.** Re-derivation is mandatory for PAHC and IJC with their records' own disclaimers quoted, and the guard clause — *"never used as grading targets before re-derivation"* — closes the loop into the checkpoint, which now grades "re-derived targets." |
| **P1-9** 1A bar | **Yes.** Baseline-relative on all three failure measures, with two pre-named improvement measures replacing "directional improvement." |
| **P1-10** segment-freeze relocation | **Partly.** 1B now states the freeze is deliberately on un-rebuilt records and why. It still does not say that Design §4 item 4 places the freeze inside his *Phase-2 pass*, which is the fact a reader checking fidelity needs. |
| **P1-11** PAHC's Layer-5 pilot property | **Not applied.** Design §4 item 5's *"exercises every Layer-5 mechanism at maximum load before any other world depends on them"* and Design §2 Layer 5's *"PAHC first at 81%, and it pilots"* remain contradicted by the insight-field pass landing fifth in risk order, and the sequencing note still claims to record "the one genuine either/or." |
| **P1-12** Sonnet pricing step | **Yes**, with the date and the ~50% figure, sourced to the same entry. |
| **P2 ×8** | **All eight applied.** Notably P2-1 (the invented "flagged 2026-08-08" provenance is replaced by the actual evidence, and the numbers are right — I re-checked: 8 `main_response` calls across 8 Desert turns, and turns 1–5 at 144/152/160/187/138 words against a 60×1.5 = 90-word trigger, so "five turns above the trigger" reproduces exactly); P2-3 (freeze rationale "where one exists (five of six; Desert's 60 predates the freeze sessions)" — correct); P2-8 (per-world boundaries named, and §7 now points at them rather than at the unreachable boundary A). |

---

## New P0

### N-P0-1. The staging step's named override, `DATA_PATH`, is dead config. Setting it changes nothing — silently — and the checkpoint harness would read the live deployed prompt, reinstating the exact defect the step was written to close.

Phase 2 step 3: *"the checkpoint harness runs the backend with the candidate files (git worktree checkout or **the backend's `DATA_PATH` override — Blueprint's named mechanism**, chosen at Phase 0.4 when the harness is extended), with the live `data/` untouched."*

`.env.example` does carry a line that looks like this mechanism — `DATA_PATH=./data/syriac_world` — which is presumably where it came from. It is stale. Three independent facts in `app/config.py`, any one of which is sufficient:

1. **`Settings` has no `data_path` field.** The only `data_path: Path` declaration (line 18) is on the `WorldConfig` dataclass, populated in code. `Settings.data_path` (lines 154–156) is a `@property`, under the comment *"Legacy properties for backwards compatibility (default to Syriac)"*, and pydantic-settings populates fields, not properties.
2. **`model_config` sets `extra="ignore"`** (line 49), so an unmatched `DATA_PATH` in the environment or `.env` is dropped without an error. The failure is silent — no exception, no warning, no log line.
3. **Dispositively, the runtime read chain never touches it.** `main.py:156`'s `load_world_content` → `settings.get_world_config(world_id).permanent_prompt_path` → `WorldConfig.data_path`, which the `worlds` property builds as **`self.data_base_path / entry.data_dir_name`** (line 129). The legacy `data_path` property is not in that chain for any world. Even if `DATA_PATH` were honoured, it would move nothing.

**Why this blocks.** The whole point of the new ordering is *"run against the candidate, not the deployed voice."* Under the `DATA_PATH` option, the harness runs against the **deployed** voice, produces a green checkpoint for a candidate it never executed, and the swap step then ships an unmeasured voice to participants under a checkpoint that certified something else. That is worse than the pre-fix state, because the pre-fix state at least measured the thing it shipped.

**Fix, and it is a rename.** The real override is **`DATA_BASE_PATH`** — a genuine `Settings` field (line 107, `data_base_path: Path = Path("./data")`), and a *root* swap, which is the right shape: point it at a candidate tree containing all six world directories and every world's prompt and capsule path follows. The git worktree option named alongside it also works, unmodified. Replace the name and, since the two options are not equivalent in what they carry, say which one Phase 0.4 picks rather than deferring it — see N-P1-3.

---

## New P1

**N-P1-1. "Five of six worlds' current text fails the floor somewhere" is four of six — and this is my Round 1 error, transcribed faithfully.** Research §3.1's table lists **five failing files**: Marius prompt (11.6/59.8), Yausep prompt (10.0 at the line), Hieronymian capsule (11.5/59.0), IJC capsule (12.5/57.2), PAHC capsule (13.3/56.1). Partitioned by **world**, IJC contributes two of the five, so the failing worlds are IJC, Syriac, Hieronymian and PAHC — **four**. Alexandria (prompt 6.2 / capsule 7.8) and Desert (9.7 / 9.6) pass on both surfaces. My Round 1 P0-3 heading said "five of six worlds," while its own table listed five *files*; the fix prose reproduced the heading. Correct both. The finding's substance is unchanged — four failing worlds still redden a fleet-wide gate, and two of them (PAHC fifth, Yausep sixth) are not rebuilt until the end of Phase 2.

**N-P1-2. §7's turn components sum to 274 and omit four of Phase 3's five live-turn items, so the range's floor (275) sits below the document's own zero-failure floor.** The stated components: baseline 84 + 1A 14 + 1B 8 + Phase 2 84 + fleet regression 84 = **274**, presented as *"roughly 275–350 turns with a realistic failure allowance."* But Phase 3 schedules four further live-turn items the list skips: the S6.5 *"spot batteries,"* the relational-safety probe category re-run, the `HARD_CEILING_WORLDS` trigger-behavior verification in Interview mode, and the `confirmed_glosses` without-arm on one world — ~40–45 turns at the floor. So the zero-failure floor is ~315–320, and the entire "realistic failure allowance" is the ~30 turns between there and 350 — against a checkpoint discipline that permits two consecutive failed iterations per checkpoint, where one failed per-world re-run alone costs 14. Separately, *"Phase 2 (~84 across six checkpoints)"* is itself a floor, because the Phase-2 checkpoint adds the confidence-under-thinness and Sustained Engagement categories *on top of* the 14. The restatement is a large improvement on 15–20 batteries and the per-turn derivation is now shown and correct ($0.33–0.35 ÷ 4 turns = $0.0825–0.0875). **Fix:** add a Phase-3 line (~40 turns beyond the fleet regression) and state ~320 as the zero-failure floor with 400–450 as the realistic figure; at $0.085 that is ~$34–38 before 31 August and ~$45–50 after the price step the same paragraph names. *(The "Phase 0/1 is roughly a third of that spend" claim survives recomputation: 106 of ~320 = 33%.)*

**N-P1-3. The candidate tree has no indices, and neither staging step says to build them.** Under the rewrite branch, the insight-field pass edits `Ecological Function` / `Formation Ecology Connection` bodies inside `data/<world>/lexicon_chunks` and `story_chunks`. Retrieval does not read those files at turn time — it reads the vector stores under `vector_store_base_path`, a *separate* setting from `data_base_path`, built by `build_indices.py`. A candidate tree reached by worktree or `DATA_BASE_PATH` therefore carries the new prompt and capsule but the **old** retrieved chunk text, so the per-world checkpoint would measure a hybrid that never ships, and the lead-with-insight instruction — the thing the insight-field pass exists to make non-hollow — would be graded against un-rewritten fields. **Fix:** add to step 2, *"re-index the candidate tree's lexicon and story vector stores and point `vector_store_base_path` at them,"* and pick the worktree option if it is the one that carries indices more cleanly. This also decides N-P0-1's deferred choice, which is why the two should be fixed together.

---

## New P2

1. **Layer 3's second rule is still missing.** Design §2 Layer 3 carries two: boundaries stated redundantly (landed), and *"any style default is stated once and demonstrated in Layer 2 rather than restated (prose restatement is the weakest lever and costs tokens)."* The second is the one that keeps Phase 2's fresh prose from re-growing the apparatus this rebuild exists to remove.
2. **A new internal collision at "twice."** Phase 2 step 1: the contrastive fallback fires *"if a world fails its checkpoint twice on a measure a demonstration targets."* §6: *"a checkpoint that fails twice consecutively escalates to Mark with the data rather than iterating silently."* Both rules fire on the same event and neither yields. One clause fixes it — e.g. the contrastive adoption is one of the options put to Mark *at* that escalation, not an alternative to it.
3. **P0-1's correction landed at §0 and not at Checkpoint 0 — this thread's signature failure mode, in miniature.** §0 now says Checkpoint 0's leak-gate condition *"evaluates only on the rewrite branch."* Checkpoint 0 itself still reads, unchanged, *"leak gate runs clean on hard-fail classes or names exactly the files Phase 2 must fix."* Honest at one site, stale at the other, and Checkpoint 0 is the one Build actually signs.
4. **Two things in 1B's new prose.** (a) The byte-identity reasoning is transcribed correctly — Desert already in `partial`/`strong`, all six tie at 4 strong, the rank key reproduces `sorted()[:3]` — but the fragility caveat is not: the identity holds *because* the six happen to share a profile, so 1B should say the record **contents** are held constant and that a single re-score during normalization breaks the tie and voids the expectation. (b) Limit (b)'s *"all six worlds share the profile schema"* is ambiguous and false on one reading: true of `voice_profile` structure (Design §0: "fleet-wide in structure"), false of demonstration `trait_scores`, where Design §0 says IJC carries none at all and three worlds use a `PASS` vocabulary — which is the entire reason 0.1 exists. Say which schema.

---

## What I re-verified as true in the new prose

- **The `$0.08–0.09/turn` derivation, now shown inline** — `$0.33–0.35 per 4-turn conversation` ÷ 4 = $0.0825–0.0875. Correct, correctly sourced, and (per Round 1) it does not inflate with battery length.
- **"Seven of the nine later checkpoints"** — enumerated: 10 checkpoints, 9 after Checkpoint 0, 7 carrying an Objective-3 bar. Exact.
- **The Phase-3 ceiling sentence** — `voice_rebuild_research_probe_results.json` re-parsed: 8 `main_response` calls in 8 Desert turns, turns 1–5 at 144/152/160/187/138 words against the 90-word trigger. "Five turns above the trigger threshold," "did not bind," and the file citation are all exact.
- **The `reading_floor` values** — FK band [8,10], FRE ≥ 60, quoted correctly from `wrs/parameters.yaml`.
- **Desert's freeze-rationale exception** — `nodes.py:1617-1645` carries dated S6.2 freeze comments for ALX, HAL, SYR, PAHC and IJC; Desert's `60` carries none. "Five of six" is right here.
- **The Marius/IJC guard placement** — `nodes.py:1174-1181`'s IJC-scoped extension is real and is Marius's, and Design §4 item 2 says *"keep his IJC-scoped post-history guard."* The new parenthetical is accurate.
- **`git revert` as the named rollback** — coherent with the swap being a commit to `data/`, and it is the right primitive given the files become generated artifacts.

---

## Verdict for the Standing Practice's point 6

**Not ready for Mark's Blueprint-stage sign-off. One editing pass, and no design decision re-opens.**

Stated plainly rather than softened toward approval, because the single P0 is the reason this gate exists: the sentence written to guarantee that a checkpoint measures the candidate names a mechanism that silently measures the deployed voice instead. That is not a proportionality call — it is a one-word rename (`DATA_PATH` → `DATA_BASE_PATH`), and until it is made, the plan's central safety property is false in one of its two branches.

Everything else is small. Three P1s: a count I introduced myself (four worlds, not five), a turn total that omits Phase 3's non-regression batteries, and an indexing step the new staging path needs. Four P2s, all clause-sized, one of which — Checkpoint 0 left stale against §0's own correction — is worth fixing precisely because it is this thread's recurring shape.

The plan underneath has now survived two passes at source. Its architecture-facing claims (assembly identity, the selector's behaviour on Desert's records, the ceiling's non-binding, the probe harness's coverage, the cost per turn) all reproduce. Its ordering — staging, checkpoint, swap-on-green, revert — is right, and it is the part I would have expected a fix pass to get wrong.

**Rename the override, add the re-index step and the Phase-3 turns, apply the three unlanded residues (`_migrated_world_ids`, `confirmed_glosses`'s assembly feed, PAHC's Layer-5 pilot property), sweep the four P2s, and send it to Mark. No further adversarial round is warranted** — what remains is checkable by grepping this file's own quoted strings against the document, which is a verification, not a review.
