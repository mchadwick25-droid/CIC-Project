# Adversarial review: `CiC_System_Redesign_Fable_Brief_2026-07-25.md`

*Opus review, dispatched 2026-07-25 specifically to find gaps and errors before the brief is sent to Fable — a capped, expensive resource (2 passes/week). Genuinely adversarial by design, not a rubber stamp.*

## Bottom line

The brief is well-argued and the diagnosis is genuinely strong, but **it is not ready to spend a capped pass on.** Three problems are severe enough to change what Fable produces:

1. **It never tells Fable that current governing documents exist for all four things it asks Fable to design.** Every one of the four domains — build process, representative construction, facilitator governance, table dynamics — has a current, named document in a clearly-labeled tier, and the brief names none of them. Fable will design in a vacuum against 370 archived files of superseded versions.
2. **Item 7 (the pressure test) cannot be executed as written.** No transcript of the "what is faith" case exists anywhere in the repo. Meanwhile real transcripts *do* exist — including a 20-turn multi-world safety battery — and the brief points at none of them.
3. **The brief and its entire required-reading folder are untracked in git.** If Fable receives this repo by clone rather than as an attached bundle, it gets neither.

Below, organized by the six review questions. Findings marked **[P0] / [P1] / [P2]** — real output-changing problems versus polish.

---

## 1. Simulating the actual output

Calibrated against the prior Fable pass in this repo (`CiC_Fable_Analysis_Disciplined_Rebuild_vs_Current_2026-07-04.md`), which verified every claim against a specific file it read directly. That's the baseline expectation for what Fable does with what it's given.

**The structural risk before any deliverable: the brief's center of gravity is diagnosis, not design.** Framing + evidence (preamble, §1-4, §6) = 1,981 words; the actual ask (§5, §7, §8, §9) = 1,314, and ~250 of that is Phase 2 detail Fable is told not to do. The real Phase 1 ask is roughly **32% of the document**. Given a diagnosis-weighted input and an unfamiliar generative ask, the most likely single outcome is **an excellent 40-page re-diagnosis with a thin design attached.**

### Deliverable-by-deliverable

**1. Schema/field spec per record type.** Competent, but will guess on which record types exist (the pipeline has far more than "a term, a story, a force, a source, a gravity" — Doc_01-10, Capsule Core, Context Layer, Priority Layer, Voice Configuration, Facilitation Brief, Approved Source Database), on the confidence vocabulary (Constitution Article 17's actual categories are never defined in the brief), and will omit **Author Gravity** entirely — a core Doc_02 construct rated "SYSTEMIC risk" for Origen in Alexandria, absent from the brief's seven jobs.

**2. Build-process methodology.** Will not know the strongest existing verification model is the **Permanent Prompt Final Assembly Instruction** (numeric Flesch-Kincaid check, register-fidelity check) plus **V7.4's Validation Protocol Rigor** (two independent trials, held-out probes, blind grading) — a ready-made answer to the brief's own "a real checkpoint, not a self-report" ask, withheld. Will not know written rules have a documented six-world failure record: a standing rule against self-certification, adopted before two later worlds existed, recurred in both anyway.

**3. Representative-construction methodology. Fable will stall hardest here.** `CiC_L3C_Representative_Construction_Framework_V3.2.docx` **is the current governing document for this exact deliverable and the brief never names it** — nor the Permanent Prompt Template, Voice Configuration Template, or Construction Notes Template. Fable will either reinvent them or burn a large share of an expensive pass orienting itself.

**4. Facilitator-governance design. The single worst gap.** `CiC_L3D_Facilitator_Governance_V3.7_PROPOSAL.docx` is a 69,000-character, 16-section governing document already specifying turn management, the public-transcript apparatus, and known limits. Concretely, Fable will re-derive or contradict:
- **The public-transcript isolation boundary** — described as *"the boundary that makes the table constitutionally sound"*: only spoken words cross between Representatives. The brief's own §7 ask ("forces/gravities actually informing how worlds engage each other") reads, on its face, as a proposal to breach exactly this, with no flag that it's a constitutional line.
- **Three different live numbers for the table-size ceiling** (5 design / 3 operative / 2 in one older doc), none in the brief.
- **Four already-enumerated Known Limits** for multi-world dynamics that Fable would otherwise rediscover at cost.
- **Mode-dominance drift** — defined in governance, zero implementation. A free finding, withheld.
- **The drift-signal count is unresolved in current documents (6→7→9→10→11→12).** Any schema keyed to "the drift signals" has no stable referent today.

**5-6. §3 accounting / cost comparison.** Poisoned by two factual errors in §3 (below), and **the brief contains zero cost numbers** despite a full cost model (`CiC_Go_Live_Cost_Model_V0_1.md`), real measured figures ($0.06-0.08/exchange, $2/hr actual vs $1/hr assumed), and a documented **costing trap**: a prior decision was approved at "~1.4x once cache-read is weighted at its true rate, not the raw 3x token multiple." **A cost comparison done on raw token counts will be wrong by roughly 2x**, and doc 10 (never cited) suggests the direction may even reverse — a larger *stable* cached prefix can be cheaper than a smaller per-turn-varying one.

**7. Pressure test.** Will be a hypothetical — see §3 below.

---

## 2. Internal contradictions — does the disclaimer actually hold?

**No. It reads as a spec with a disclaimer bolted on, and the deliverables make the disclaimer inoperative.** [P0]

The brief says the seven jobs, external patterns, dataset-not-prose shape, and §3 are *"a well-evidenced starting hypothesis... not a requirement."* Then §9 deliverable 1 **requires** a schema "explicitly mapped to the seven jobs in §5" — you cannot deliver it without adopting §5. Deliverable 5 **requires** "an accounting of what from §3 is preserved" — forcing §3's frame regardless. §8 opens with a flat declarative ("Not prose as the source of truth"), not a hypothesis. Three disclaimers do not offset the deliverable definitions that make them non-optional.

**§6 makes over-anchoring worse by reporting only the positive verdicts.** Research doc 09 renders three-valued verdicts — TRANSFERS CLEANLY / NEEDS ADAPTATION / DOESN'T APPLY. §6 reports only the first column. Missing entirely:
- **The single most important omission in the brief.** Doc 09's only verdict phrased as "TRANSFERS CLEANLY, *and is a warning*": with original (verbatim) personas, models *"unwittingly repeat profile information either verbatim or with significant word overlap"* — *"A world's own distinctive vocabulary in the persona slot is the highest-parroting-risk configuration there is."* The brief's entire §4c/§4d thrust is to make *more* lexicon and relational material reachable at speech time. Nothing in the brief asks Fable to guard against parroting instead of voice.
- Every identity-describing field (description, personality, scenario, self-description, exemplar characters) carries NEEDS ADAPTATION — the organizing distinction doc 09 itself draws (retrieval layers transfer cleanly; identity layers all need adaptation) is flattened into one undifferentiated "adopt" list.
- The "3-5 examples" figure is Anthropic's *few-shot prompting* guidance, not persona guidance — doc 09 records the opposite-pointing finding (Character.AI gives description 1.5% of demonstration's budget) and says plainly "it is not unanimous." The brief manufactures a consensus that isn't there.
- The negative-constraints-as-rubric-only claim is contradicted by CiC's own record: Desert's *soft* anti-fabrication guard failed retest while a *categorical* one held. Adopted as written, this argues for removing a mechanism that demonstrably works.

**One contradiction against the project's own governance.** [P1] The brief states "the only true bedrock is the mission, the Five Convictions, and a safe space." Vision V2.0 itself also lists **the story** as unchanged, and Constitution Article 5 states rigor is a *"constitutional requirement, not an aspiration... No... **resource constraint** overrides it."* The brief's §2 framing that cost "grounds this equally" sits in real tension with that. The brief cites zero Constitution article numbers anywhere, despite the Constitution binding the exact things being redesigned.

---

## 3. Missing inputs

### 3a. The pressure test cannot be executed as written [P0]

No "what is faith" transcript exists anywhere in the repo — only the code-level bug analysis in research doc 08 and the brief's own description. §9's ask to "show explicitly how the new design would have produced a better result than today's system did" is unanchored without a real transcript — Fable will invent a plausible bad one and then beat it.

**Real transcripts exist and the brief points at none of them:**
- `CiC_Live_Safety_Testing_Script_2026-07-21.docx` (repo root) — 20 turns, 7 batteries, all 5 worlds, both endpoints, including a three-world table. This is the source of the "19/20 clean" finding cited in §3.
- `cic-poc/backend/transcripts/` — 24 real runtime multi-world sessions. **Untracked in git.**
- Per-world Phase 5 transcript files across all six World-Builds folders — the transcripts behind every failure research docs 07 and 08 analyze.
- `World-Builds/Cross_World_Roundtable_Validation.md` — the 22-part turn-by-turn log — **only on branch `CiC-Fable-Experiment`, absent from main.** Fable on a default checkout cannot read it without being told the branch exists.

Also worth inheriting: the Guided Questions calibration study found its own desk-check was *"pessimistic on the axis it measures, and blind to the axis where failure actually happened."* A pressure test is a desk-check; Fable should know this going in. And a project design rule states a good multi-world question is one where worlds *genuinely diverge* — "what is faith" may itself be the wrong kind of test question, and the brief should say so rather than let Fable discover it.

### 3b. The brief never grants repo access or instructs verification [P0]

The brief says only to read the research folder — never that Fable has read access to the live repository, never instructs verification against primary sources, never names a branch. The prior Fable pass explicitly listed what it measured against; that house pattern was dropped here. This matters more than usual because the research summaries contain verifiable errors (3h below) that an unverifying Fable would inherit.

### 3c. Delivery risk: brief and research folder are untracked in git [P0]

Neither `Ministry/Technology/` nor `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/` is committed. If Fable receives this repo by clone or in a remote environment rather than direct file access, the entire "required reading" folder is not there. Verify delivery method before sending.

### 3d. 370 of 1,602 tracked files are superseded `Archive/` versions [P1]

The brief resolves one version conflict (Vision V2.0 vs V1.1) in a full paragraph and leaves every other one unstated — multiple Constitution versions, multiple Facilitator Governance versions, multiple Construction Framework versions all coexist in the tree.

### 3e. Withheld numbers the deliverables require [P1]

- **Reading level already has a real, checkable standard**: Flesch-Kincaid grade 8-10, Reading Ease 60+, plus a universal 10th-grade Level-2 floor that Article 30 says is *never gated by participant type*. The brief's §7 phrasing implies no such standard exists. It exists; it's just never enforced at runtime (zero hits for `flesch|kincaid|readability` in the codebase).
- **"Three-level access" is itself an ambiguous phrase in this project** — at least five different things use the word "tier." Constitution Article 30 defines the real one precisely: conversation / on-request reference explanation / full scholarly apparatus, **all three always present, none ever gated**. That hard invariant directly bounds any token-saving proposal and should be quoted, not paraphrased.

### 3f. Doc 10 (the conversation-realness study) is never cited, despite §2 calling its subject "the ground the whole redesign stands on" [P0]

Doc 10 is the only research document actually about conversation dynamics. It's never named, quoted, or alluded to anywhere in the brief. It contains: the actual provenance of `MIN_MULTI_WORLD_TURNS = 2` (the exact mechanism one of the brief's own cited live bugs broke); the finding that realness collapses over conversation length through three measurable modes (declining initiative, agreement-drift, style drift) — none of which any of the seven jobs covers; the standout finding that models "state a character but don't enact it, especially by refusing to disagree" — directly implying a missing schema field (what a world contests and holds under pressure); the "personality is versioned" governance lesson, directly relevant since §8 proposes regenerating every Permanent Prompt from a new dataset with no continuity-regression check specified; and the cache-weighting correction that makes several of the brief's own cost assumptions unreliable as stated.

### 3g. Architecture facts that would invalidate design assumptions [P1]

- **The LangGraph graph is vestigial** — real orchestration is hand-wired in `main.py`, not in `builder.py`'s own documented flow. A designer reading `builder.py` as documentation designs against fiction.
- **Two incompatible multi-world turn engines already coexist** in the codebase (streaming vs. non-streaming endpoints) — directly relevant to the facilitator-governance deliverable.
- **The participant-role/lane system is dead code** — the brief's three-level-access objective would be proposed on top of an already-inert role layer without knowing that.
- **Only one drift signal survives per turn by design**, with the code itself naming the risk: "a fabrication losing that slot to a stylistic complaint."
- **`GET /api/session/{id}/audit` already exists** and covers part of the brief's "repository/reference" job — already built, not credited.

### 3h. Two verified accuracy errors in the brief itself [P0] — the most important finding in this whole review

**(i) §3's confirmed-gloss claim is factually wrong.** The brief states the confirmed-gloss whitelist is "the mechanism found broken the same night this research was compiled." **No research document says this.** What was actually found broken that night was the **sensed closing sequence** (four Facilitator prompts imported but never defined; every closing turn threw an error) — a completely different mechanism. The confirmed-gloss system was, if anything, *improved* that same night: expanded from 22 to 87 confirmed terms, with a case-sensitivity bug fixed. As written, Fable would be told to replace a mechanism that was working and improving, while the mechanism that was actually found completely broken goes unmentioned in that section.

**(ii) §2's flagship supporting quote is a fabricated composite.** The brief quotes a lens synthesis being "explicitly deleted for being 'representative-construction work, out of scope for this document.'" That exact phrase exists nowhere in the research. It's a fusion of two *different* findings from research doc 07: the real quote about the lens deletion is that it was stripped "on **Article 3 grounds**" because "it was heavily Representative-oriented... all of that is excluded" — a **governance-mandated firewall deletion**, not an editorial scope call. The "out of scope for this document" phrase belongs to a *separate* finding (the Simeon bar Sabbae source-anchoring gap) that the brief already uses elsewhere. This matters doubly because the brief itself promises "every claim in this brief traces back to specific evidence" — and Fable, instructed to verify, would find this specific flagship quote does not check out. It also changes the fix: this can't be solved by "keep the section," since it was removed by constitutional rule, not oversight.

### 3i. §3's "19/20 clean" claim is real but under-caveated and ambiguous [P1]

Genuine finding, but: the one actual failure was never fixed (a de-escalation timing threshold still doesn't match the measured reality, judged "the safe direction" but not corrected); it covers 5 worlds and there are now 6; a *second*, unrelated "19/20" statistic exists elsewhere in the project (a voice-quality result, not a safety result) creating real ambiguity about which one is meant; and the original failing transcript that triggered building the mechanism in the first place was never specifically rerun through it.

### 3j. Other overstatements worth correcting [P2]

- §4a's "quality does not improve with build order" is stated more strongly than the source: the actual research also found the verification-discipline half of quality *did* durably improve, and named the newest world's higher defect rate as partly caused by a first-time-used new process component, not a general regression.
- §4d's "self-organized independently across all six worlds" overstates a four-world finding, and "reshaping" is misapplied — the source material is explicit that the relationship the brief wants (a force reshaped by the world's own response) is exactly what the current vocabulary *cannot* express.
- The 68% Ecological Function figure masks a real 3x spread between worlds that the source material explains mechanically (verb-shaped vs. noun-shaped writing) — a concrete, actionable schema constraint that the brief drops in favor of the single averaged number.
- §3's claim that Doc_02 is "the one place cost discipline already exists" is false — the codebase mining research names at least seven other cost mechanisms.

---

## 4. Scope-boundary clarity

**Two real problems.** [P1]

**(a) "Phase 1" is already a load-bearing, differently-meaning term in this project** — Facilitator Governance and the Table Process document both use "Phase 1" to mean a deployment/rollout stage, not "the first of two Fable passes." Fable reading both meanings risks a collision on live numbers (like the table-size ceiling) it needs to design against. Rename the brief's own phases (e.g., "Pass 1 / Pass 2") to avoid this entirely — a cheap, high-value fix.

**(b) §9 spends real space specifying Phase 2 in detail and then says not to do it.** Putting a detailed spec in front of a model and then saying "not this" is a documented risk pattern in this project's own research (a banned phrase used as a negative example made a model more likely to produce it). Cut the Phase 2 detail down substantially; save the detail for the actual later pass.

**(c) The brief never states the positive: what form Phase 1's output should actually take** — no target length, no document structure, no stated audience. Given how concrete the diagnosis sections are, Fable may be tempted to write literal code patches instead of a design document. Worth stating explicitly what "done" looks like.

---

## 5. Length and structure

Length itself (~3,300 words) is fine; the ordering and balance are not.

- **The most consequential structural bug: two of §7's six stated objectives (three-level access, full scholarly coverage) have no corresponding deliverable anywhere in §9.** §9 is the section shaped like an output contract; if Fable treats it that way, two of six objectives simply don't get built.
- Two internal notes addressed to Mark, not Fable, would ship as-is if not cut — including an unresolved "add before sending" TODO.
- "Mark" is referenced five times with no introduction — a reader with no other context doesn't know who that is.
- The "not a locked spec" framing appears three times in slightly different wording, which reads more like anxiety than clear permission, and still doesn't survive contact with §9's own required-mapping language.

---

## 6. Concrete fixes, prioritized

**P0 — fix before sending:**
1. Add an explicit "what governs, what to read, what not to break" section naming the real current documents (Constitution V2.2 with specific article numbers, Facilitator Governance V3.6/V3.7, Construction Framework V3.2, the Table Design Document, all L4 templates) and telling Fable to verify against them directly, flagging Archive/ as superseded.
2. Rewrite the pressure-test item to point at the real transcripts listed in §3a above, and be honest that the "what is faith" case is a specification of a known bug, not a saved transcript.
3. Fix both factual errors (3h) — correct the confirmed-gloss claim, correct and properly source the lens-deletion quote, and note it was an Article 3 governance removal, not an editorial one.
4. Add a missing deliverable covering three-level access and the browsable repository, so all six §7 objectives actually have a home in §9.
5. Rebalance §6 to report doc 09's full three-valued verdicts, not just the positive column — and lead with the parroting warning specifically, since it cuts directly against the brief's own central proposal.
6. Cite doc 10 explicitly in §2 and the cost section — it's the brief's own stated foundation and is currently invisible.
7. Commit the brief and the research folder to git, or confirm Fable receives them by direct attachment rather than a repo clone.
8. Rename "Phase 1/Phase 2" to avoid colliding with the project's own existing, different use of "Phase 1."

**P1 — materially improves the result:** reorder the document so mission and diagnosis lead, disclaimers and process notes move to a short "how to read this" block; state plainly that §9 is the real contract and §5/§6/§8 inform it; give the deliverable a stated shape (length, format, audience); insert the real cost baseline numbers directly; correct the "one place cost discipline exists" claim; add a short note on how many verification attempts a written-only rule took to actually hold, since that bears directly on whether Pass 2 is even viable as scoped; fix the §4 overstatements.

**P2 — polish:** trim the repeated disclaimer to one instance, cut Phase 2 detail to a few sentences, remove the redundant cost paragraph, note the real denominator behind the 68% figure.
