# Adversarial review (round 1): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus review, dispatched 2026-08-06 — the first adversarial pass on this document, run immediately before its Friday Fable thread. No prior round exists for this brief; calibration was taken from `11_Opus_Adversarial_Review_of_Brief.md` and `18_Opus_Adversarial_Review_Round3_of_Brief.md` (a different, unrelated document — read for the failure *class* only, not for content).*

*Named failure mode hunted, per the Standard Practice's point 5: this brief's §5 finding (C) originally asserted that "worked examples carry real enforcement weight prose alone doesn't," a claim that did not survive being tested live the same day. The brief has since walked that back. This review assumes more claims of the same class are still sitting unchecked in the text — **and treats the revision itself as unverified until checked against the pilot's actual saved transcripts and usage data.**

*Verification method: every checkable claim was read against its cited primary source directly — all six permanent prompts and all six World Capsule Core files read in full; `representative_prompts.py`, `facilitator_prompts.py`, `nodes.py`, `sections.py`, `retriever.py`, `indexer.py`, `story_retriever.py`, `story_indexer.py`, `confirmed_glosses.py`, `wrs/parameters.yaml`, `wrs/gates/core.py` read at the cited lines; both .docx files extracted fresh from `word/document.xml` rather than read from an earlier session's extraction; all 118 lexicon chunks and all 60 story chunks measured programmatically; the pilot's saved transcripts and per-call usage records read as raw JSON, not as a description of them.*

---

## Bottom line

**Not ready to send.**

The brief is well-organised, honestly written, and structurally much healthier than the 2026-07-25 System Redesign brief was at the equivalent stage. Its balance ratio is **52.1 / 47.9** (diagnosis §1–§5 = 1,898 words; ask §6–§9 = 1,748 words) against round 1's 68/32 on the prior brief — the "excellent re-diagnosis with a thin design attached" failure mode is genuinely absent here. All **20** internal `§N` cross-references resolve correctly to sections that say what they are cited for. Several of its most load-bearing citations are exact, including line numbers.

But the diagnosis section is where the document is weakest, and §5 is what §7 and §9 are built on. **Eight send-blocking defects**, seven of them the same class the prior process exists to catch — a claim that sounds right and does not survive being checked against its own source:

- **§5(C)'s central mechanism is misattributed.** The FLAG-018 guard is not in `_HOW_YOU_ENGAGE`. There are **four** labelled FLAG-018 layers in the codebase, not two, and the strongest of them is composed at a wiring site in `nodes.py`, not in a prompt file at all. §7 Part A's core instruction therefore aims Fable's edit at the wrong location and would produce precisely the "parallel instruction competing with it" the brief tells Fable to avoid.
- **The pilot's most important measured result is missing from the brief entirely.** `fabrication_adjudication` fired in the Albina prototype arm — and nowhere else in the pilot or in any of the three baseline conversations. The brief reports only the FLAG-018 non-improvement. The one measured signal that lands on objective 4 ("No fabrication rule moves, anywhere, under any framing") is unreported.
- **The pilot is a matched control/treatment pair in which the guarded behaviour appears in BOTH arms.** §5(C) reports the treatment arm only, presenting a null result as a weak negative result about worked examples. The prototype's own text also instructed the guarded behaviour — a confound the revision does not name.
- **§7 Part B's mandate is premised on an absence Part Five does not have.** Part Five already carries a numeric, machine-gated readability floor (FK grade 8–10, FRE ≥ 60) with a parameters file and a running gate. Fable would spend a capped pass building operational teeth that already exist.
- **§5(A)'s headline is not supported by the comparative reading it claims.** Five of the six permanent prompts explicitly prescribe short, plain, paratactic sentences. Only one prescribes an elaborate rhythm, and it carries its own anti-stacking limiter.
- **§5(B)'s "every chunk carries" claim is false on measurement** — Tier reaches the model in 0 of 118 lexicon bodies; story chunks carry neither Ecological Function nor Distortion Risk, 0 of 60.
- **The Decision Log entry §3 makes mandatory reading still states the falsified claim as verified fact.**
- **§8 cannot measure a single one of §6's objectives**, and the project's own instrument that would measure the most central one is not named anywhere in the brief.

None of these is a writing problem. All eight would propagate into what Fable builds. Fixing them is mostly deletion and re-pointing, not new research — I'd estimate under two hours of edits, well worth doing before a capped pass.

---

## P0 — fix before sending

### P0-1. §5(C) puts the FLAG-018 guard in the wrong file, and counts two layers where the codebase labels four. §7 Part A's central instruction inherits the error.

Brief §5(C): *"`_HOW_YOU_ENGAGE` already carries an explicit guard (labeled FLAG-018 in its own comment, `representative_prompts.py:174-181`) against unprompted term-reclarification."*

The line numbers are **correct** — the guard text is `representative_prompts.py:174-181`. But `_HOW_YOU_ENGAGE` is the module-level string spanning **lines 5–76**. The FLAG-018 guard is not in it. It sits inside `build_representative_prompt`'s `dynamic_parts`, gated behind `if retrieved_context:` (line 164), which means it is **absent from the prompt entirely on any turn where retrieval surfaces nothing**, and it rides in the never-cached dynamic suffix rather than the cached static prefix.

And there are not two layers. Grepping `FLAG-018` across the backend returns four labelled ones:

| Layer | Location | What it is |
|---|---|---|
| 2 | `app/prompts/representative_prompts.py:168-181` | the retrieved-context guard the brief cites |
| 2 (per-world) | `wrs/views/s62_pahc_prompt_coverage.py:110` — *"clause is the FLAG-018 layer-2 rule carried into the voice's own"* | Chloe's own copy (`pahc_..._Chloe.txt:29`) |
| 3 | `app/graph/nodes.py:1155-1167` | the **post-history guard**, composed at the wiring site, riding closest to generation |
| 4 | `app/graph/nodes.py:3871`, `app/graph/modern_term_bridge.py:237` | a mechanism (`plan_restricted_offer`), not prose |

Layer 3's own comment carries a measured prior result the brief never cites:

> *"the no-unprompted-sense-clarification constraint survived only partially when placed before the retrieved context (**one false 'I meant X earlier' opener remained in 16 turns**). Doc 09's own post_history finding — the instruction that must survive attention decay rides closest to generation — is why it now ALSO rides here"* — `nodes.py:1156-1163`

Layer 3 applies to migrated worlds only. I verified **all six** worlds have a `world_core` record (`wrs/records/*/world_core/*.md`), so `_migrated_world_ids()` returns all six and layer 3 was live in both the baseline test and the pilot.

**Why this blocks.** §7 Part A tells Fable to rewrite `_HOW_YOU_ENGAGE` with the new Ecological-Function/Distortion-Risk instruction *"worded as an **extension** of the existing FLAG-018 guard rather than a parallel instruction competing with it."* Executed literally, that is impossible: the guard is not in that block. The result would be exactly the competing parallel instruction the brief forbids — a bridge-first instruction in the cached static prefix, arguing against a guard in the dynamic suffix and a second guard at the `nodes.py` wiring site.

**Fix.** State the four layers and their real locations. Say plainly that the strongest layer is composed in `nodes.py`, not in a prompt file, and that any new instruction competing with it must be reconciled *there*. Cite the 1-in-16 measured residual as finding (C)'s real baseline.

---

### P0-2. The pilot's single most important measured result is absent from §5(C): the prototype tripped the fabrication check, on Albina, and nowhere else.

Reading the saved per-call usage records in `mark_voice_simulation_results.json`, counted by `label`:

| Run | `fabrication_adjudication` calls |
|---|---|
| Chloe — current | 0 |
| Chloe — prototype | 0 |
| **Albina — prototype** | **1** |
| Albina — current | 0 |
| All three 2026-08-05 baselines (Papnoute, Chloe, Yausep, 12 turns) | 0 |

It fired on Albina prototype turn 1 — the turn containing:

> *"consider what actually happened to the widow whose house Alaric's soldiers broke into during the sack of Rome: she had given away most of what she owned years before, and when the soldiers came demanding treasure, there was none left to give them. She died soon after, from what followed... **That is the record of someone who had actually made herself poor enough that an army found nothing worth taking.**"*

I checked the underlying claim against the world's own record and it is **not** a fabrication — it traces to `data/hieronymian_world/story_chunks/hal_story05_marcella-death.md`. But that chunk's own Usage Guidance says:

> *"The specific reported detail (soldiers demanding treasure from an already-emptied house) follows the epitaph genre's conventions of dramatic irony and should be handled with the same genre-awareness as other epitaph material in this repository — **real, but shaped by a commemorative genre, not a transcript**."*

The prototype delivered it flatly, as "the record," without the genre caveat its own source demands. The most defensible reading is not fabrication but over-settling of genre-shaped material — which is exactly what the source chunk warns about, and exactly what the fabrication screen caught as a candidate.

Note also the knock-on: on that turn `over_settling_screen` did **not** run at all (Albina prototype shows 2 over-settling pairs across 3 turns, against 3/3 in every other arm), because the drift chain short-circuits on a fabrication signal (`nodes.py:1956`).

**Why this blocks.** Objective 4 is the brief's single stated non-negotiable. The pilot produced one measured signal bearing on it, in the direction of concern, in the world §5(D) names as the primary acceptance evidence and §7 sequences first. Reporting the FLAG-018 non-improvement while omitting this is the most consequential asymmetry in the document.

**Fix.** Report it, with the caveat about what it does and does not prove, and add a fabrication-signal check to §8 (see P0-8).

---

### P0-3. The pilot is a matched control/treatment pair in which the FLAG-018 behaviour appears in *both* arms. §5(C) reports one arm and draws an inference the data cannot support.

Brief §5(C): *"The FLAG-018 behavior still surfaced, on the same turn, with both additions present. That is one data point, not a verdict — it shows positive-only worked examples aren't sufficient by themselves for this specific guard, in this one instance."*

Reading the actual transcripts, Chloe turn 3 in **both** arms:

> **current (no prototype changes at all):** *"When I speak of the ekklesia, I mean the assembly itself — the gathering of the called-out people, not a building, not an office. That's the thing this question actually touches."*
>
> **prototype:** *"When I speak of the ekklesia, I mean the assembly itself — not a building, just the people gathered under whatever roof will hold them. Does that match what you had in mind?"*

Same turn, same behaviour, both arms. The pilot therefore has **zero discriminating power** on the worked-examples question — you cannot tell whether the examples helped, hurt, or did nothing, because the outcome is identical with and without them. The brief presents a null result as a (weak) negative result about worked examples.

There is a second, unnamed confound. `PROTOTYPE_ADDITIONS` (`mark_voice_simulation.py:112-120`) contains:

> *"where a retrieved note names the gap between a modern assumption and your own world's actual view, **that gap is often exactly the bridge worth opening with**, not a footnote added after the fact."*

That instruction sits in the static prefix and tells the model to open turns with Distortion Risk material. The FLAG-018 guard, in the dynamic suffix, says *"never open a turn by clarifying a term's sense unprompted."* The prototype **instructed the guarded behaviour**. Any inference about worked-example efficacy from this run is confounded before it starts.

Two further prototype-only observations §5(C) does not carry:

- Chloe prototype turn 1 opens *"You asked this before, or someone standing where you stand asked it."* No one had. This is a **false conversational memory about the participant** — structurally the same family as FLAG-018's *"never say you used a word earlier unless you actually spoke it in this conversation,"* inverted onto the other speaker. New defect, introduced by the prototype, unreported.
- Chloe prototype turn 3 is measurably **more** honest than the current arm on the same fact. Current turn 2: *"Corinth read it, took it seriously, and **by all report set things right**."* Prototype turn 3: *"whether Corinth took it up, how it was received there... **that part of the story isn't one I can hand you with confidence**."* A real improvement, also unreported.

**Fix.** Rewrite §5(C)'s pilot paragraph to state: the behaviour appeared in both arms; the pilot is therefore non-discriminating; the prototype carried an instruction contradicting the guard; and the prototype introduced one new false-conversational-memory defect while improving one over-settling case. Then let §9's Research stage design an actual controlled test.

---

### P0-4. §7 Part B tells Fable to give Part Five "concrete operational teeth" it already has — a numeric, machine-gated readability floor.

Brief §7 Part B: *"**Part Five (Voice Construction)** — the framework already states the right destination... **Give that principle concrete operational teeth**."*

Extracted directly from `CiC_L3C_Representative_Construction_Framework_V3.2.docx`, Part Five, "Language and Register":

> *"A further standard governs this Representative's prose independent of register, and is not itself a register choice: sentence structure must remain accessible. Whatever register a world's own evidence supports — plain and terse, or formally rhetorical and elaborate — the Representative's sentences should typically fall within a **Flesch-Kincaid grade band of roughly 8 to 10 and a Flesch Reading Ease of 60 or above**, achieved by keeping sentences reasonably short and avoiding long chains of clauses joined by em-dashes, colons, and semicolons... The operational values of this floor... are recorded in the parameters file at **cic-poc/backend/wrs/parameters.yaml (reading_floor), which the machine gates read directly**."*

And immediately after it, the exact guidance §6 objective 3 and §7's Albina paragraph believe they are inventing:

> *"Construction note on accessibility versus register: these are two independent checks and must not be conflated... **A world whose own sources are rhetorically trained and elaborate should still keep its sentences within the accessibility band — elaboration belongs in vocabulary, imagery, and clause content, not in unbroken sentence length.**"*

Both ends verified in code:

- `wrs/parameters.yaml:102-114` — `reading_floor: flesch_kincaid_grade_band: [8, 10]`, `flesch_reading_ease_min: 60`, `source:` citing RCF V3.2 Part Five, `notes:` *"Sentence structure only, never vocabulary. Instrument: S1.3's readability gate."*
- `wrs/gates/core.py:211` — `def readability_check(text, fk_max=10.0, fre_min=60.0)`, implemented, hard-failing rather than silently passing if `textstat` is missing.

**Why this blocks.** Part B is half the brief's mandate and it is the half justified as "the actual 'self-sufficient' fix." Written as-is, Fable spends capped budget re-deriving a standard that is already numeric, already parameterised, already gated, and already sourced to the exact paragraph the brief quotes. Worse, the brief's own framing — *"the gap across six builds is enforcement, not philosophy"* — is disproved by its own cited source: the enforcement exists. The real, unanswered question is whether the gate ran against these six builds and what it found. The brief never asks it.

**Fix.** Replace "give that principle concrete operational teeth" with the actual gap. Part Five's *missing* pieces are the pattern-repertoire concept, the bridge-first instinct, the Ecological-Function/Distortion-Risk instruction, and the worked-example requirement — none of which the reading floor covers. Add a Research-stage task: run `readability_check` against all six deployed permanent prompts and both pilot arms' output, and report the numbers.

---

### P0-5. §5(A)'s headline claim is not supported by the comparative reading it says it rests on, and §7 contradicts it.

Brief §5(A): *"**The archaic/formal register is 100% sourced from the six per-world permanent prompt files — not the shared engagement instructions.** ... Confirmed by direct comparative reading of all six files."*

I read all six in full. Five of the six carry an explicit, near-interchangeable instruction to write **short, plain, paratactic sentences** and an explicit warning against clause-stitched elaboration:

| World | Line | Text |
|---|---|---|
| Papnoute | :7 | *"Say the thing. Stop. Say the next thing."* (+ :13 *"four sentences is already long for you"*) |
| Chloe | :23 | *"build it as a line of short, separate sentences, not one sentence carrying several ideas stitched together with dashes. Land one part. Stop."* |
| Marius | :117 | *"It sets down one finding. Then the next... one short sentence for the first fact. A full stop... you do not reach for one long sentence threaded with clause after clause"* |
| Theon | :37 | *"You keep each thought in its own short sentence. You land one thing, and stop, and begin the next fresh."* |
| Yausep | :41 | *"Each stage is its own short sentence, not several ideas stitched into one long sentence with dashes. Land one thought. Stop."* |

Only **Albina** prescribes the opposite (`:29`, periodic/hypotactic) — and even she carries a self-limiter the brief does not mention: *"a periodic sentence is not a license for a long one: one clause answering one clause is this rhythm at its best. A sentence built from three or four clauses stacked in reserve is not more scholarly for the stacking — it is merely longer."*

So the labelled register instructions in these files point overwhelmingly **away** from elaboration. Whatever elevated feel exists is coming from somewhere else — and §7 already knows where, correctly:

> §7: *"the elevated register runs through more than the paragraph explicitly labeled 'how you speak' (confirmed by direct reading: identity, era, and vocabulary paragraphs carry the same stylization)"* — **verified true**
>
> §7: *"the capsule sits in the cached prefix at equal weight to the permanent prompt on every turn, in the same elevated register"* — **verified true** (`build_representative_prompt` appends `world_capsule` to `static_parts` at `representative_prompts.py:141-143`; the six `*_World_Capsule_Core.md` files are second-person literary prose, 2,129–3,353 words each)

§7 is right and §5(A) is wrong, and §7's own capsule paragraph directly falsifies §5(A)'s word "100%."

**Why this blocks.** §5(A) is the foundation of §7's entire per-world track and §9's "individual adaptation" premise. As written it sends Fable to audit the labelled register paragraphs — which are already plain-prescribing and mostly identical — rather than the narrative body prose and the capsules, which is where the effect actually lives. It also overstates how divergent the six voices are: on this specific dimension they are 5-of-6 uniform.

**Fix.** Rewrite (A) around what the reading actually shows: five of six files already prescribe plain paratactic sentences; the elevated register lives in the surrounding narrative prose of the permanent prompts and, at equal cached weight, in the World Capsule Core files; Albina is the sole prescribed exception and already self-limits. Drop "100%."

---

### P0-6. §5(B)'s "Every lexicon/story chunk carries Tier, Ecological Function, and Distortion Risk" is false on all three counts as measured. §7 Part A's instruction is a silent no-op on a real fraction of turns.

Brief §5(B): *"**Every lexicon/story chunk carries `Tier`..., `Ecological Function`..., and `Distortion Risk`...** Confirmed directly via `app/rag/sections.py` and `app/rag/retriever.py:get_context_for_response`: only `Key Sources` is stripped before generation."*

Measured, by applying the real serialisation path (`indexer.parse_lexicon_file`'s `content.split("---", 2)[2]` → `truncate_at(body, KEY_SOURCES_MARKERS)`) to every chunk in the repo:

| | chunks | Ecological Function reaches model | Distortion Risk reaches model | Tier reaches model |
|---|---|---|---|---|
| lexicon | 118 | **109** (92%) | 118 (100%) | **0** (0%) |
| story | 60 | **0** | **0** | 60 (as a header string) |

Specifics:

- **Tier: 0 of 118 lexicon chunks.** Tier lives in the `## Retrieval Front-Matter` block, which `parse_lexicon_file` discards. It survives only as `metadata["tier"]` (`indexer.py:227`), which `get_context_for_response` never serialises into `context_parts`. The model cannot see it. Story chunks do get it — `story_retriever.py` writes `f"### {title} (Tier {tier})\n"` — but lexicon chunks do not.
- **Ecological Function absent entirely from 9 chunks**: `pahclex012_hetaeria`, `pahclex013_pertinacia`, `alexlex051_apokatastasis`, `alexlex059_catechetical-school`, `alexlex074_fall-descent`, `alexlex081_homoousios`, `alexlex090_logikos`, `syrlex005_memra`, `syrlex008_mar`. (Alexandria — Theon's world — carries five of the nine.)
- **Story chunks carry neither field, 0 of 60.** Their analogue is `## Formation Ecology Connection` (60/60). There is no Distortion Risk equivalent anywhere in the story corpus.
- *"only Key Sources is stripped"* is also wrong: `retriever.py:224` calls `excise_section(body, QUICK_MEANING_MARKERS)` for migrated worlds — and all six are migrated.
- `sections.py` is cited as confirming this and cannot: it knows only `QUICK_MEANING_MARKERS` and `KEY_SOURCES_MARKERS`. It has nothing to say about Ecological Function or Distortion Risk. It confirms only the negative — that they aren't stripped *by name*.

**Why this blocks.** §7 Part A instructs Fable to write an *"explicit instruction to lead with Ecological Function/Distortion Risk material."* On a story-context turn that instruction points at material that does not exist, in a corpus of 60 chunks. On ~8% of lexicon retrievals it points at a missing section. And §6 objective 2's *"built in a defensible order: most sure first"* has no Tier visibility to build from, while §4 defers the retrieval-ordering work that would provide it. An instruction that silently no-ops is worse than no instruction: the model will improvise something to satisfy it.

**Fix.** State the real numbers. Name `Formation Ecology Connection` as the story-side field. Either add the story-side instruction explicitly or scope the instruction to lexicon context. Decide whether Tier needs to become visible to generation — and if objective 2 depends on it, un-defer that piece of the retrieval work.

---

### P0-7. The Decision Log entry §3 makes mandatory reading still states the falsified claim as verified fact.

Brief §3: *"`Decision-Log.md`, entry dated **2026-08-05 — 'Live conversation test run'**... **Read this before assuming you know the starting state; it's the direct evidentiary basis for everything in §5.**"*

`Decision-Log.md:15`, in the 2026-08-05 "later, same day" entry, under the heading *"What this session found, **verified directly against the code rather than guessed**"*:

> *"...direct evidence that **worked example dialogues, present in only 1 of 6 worlds' permanent prompts, carry real enforcement weight prose alone doesn't**."*

That is verbatim the claim §5(C) was revised to retract. It is unrevised, presented as verified, in the document Fable is told to read *before* the brief's own diagnosis. Line 12 of the same entry carries the unverified "100%" claim from P0-5. Line 14 carries the "governance is confirmed content-based" claim.

Two further §3 accuracy problems in the same sentence:

- §3 says that entry contains *"the actual live transcripts."* It does not. The entry's own line 57: *"Full transcripts, cost tables, and citation excerpts: **rendered as a styled Artifact**... **not reproduced in full here** to keep this log scannable."*
- §3 lists the governing Vision doc's commitments as *"Participant Agency, Trustworthy Transparency, Encounter Over Persuasion, Technology Serves Encounter Never Replaces It."* All four exist, but two are **Foundational Values** (Participant Agency, Encounter Over Persuasion) and two are **Convictions** (#4 *"Authentic Encounter Requires Trustworthy Transparency"*, #5 *"Technology Should Serve Encounter, Never Replace It"*). The two Foundational Values most relevant to a no-fabrication voice rebuild — **Historical Responsibility** and **Intellectual Humility** — are omitted. (Category conflation, not fabrication — see P2-6.)

**Fix.** Add a superseding note to the Decision Log entry (lines 12 and 15), or add an explicit warning in §3 that the entry predates the finding-C revision and the "100%" claim, and which lines are superseded. Correct §3's claim about where the transcripts live.

---

### P0-8. §8 cannot measure a single one of §6's objectives, and the one project instrument that would measure the most central one is not named anywhere in the brief.

§8 names exactly two before/after metrics: *"the `FLATTENING` drift-signal rate"* and *"the `over_settling_adjudication` firing rate."* Checked against the harness §8 names for the job:

**The FLATTENING rate is not capturable by `mark_conversation_test.py` at all.** Its `UsageCapture` handler (`mark_conversation_test.py:88-98`) reads only `[llm_usage]` log lines. I confirmed against the saved records that the captured fields are exactly `label, model, request_id, session_id, input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens`. `drift_detection` appears as one undifferentiated label; **which of the ten signals fired is never recorded.** §8's first named metric cannot be produced by §8's own named instrument without modifying it.

**The `over_settling_adjudication` rate measures the wrong thing.** It counts how often the *screen* flagged — and the screen is deliberately built to over-flag:

> `nodes.py:2162-2164`: *"Deliberately tuned to over-flag — the prompt tells it to flag when unsure — because every flag is handed to a source-fed second pass that can clear it, and only a miss is unrecoverable."*
>
> `facilitator_prompts.py:226`: *"Your only failure that costs anything is a claim you let through... So when you are unsure, flag it."*
>
> `facilitator_prompts.py:271`: *"**Most turns should produce none at all**: the first pass forwards everything it wonders about precisely because it cannot check, and clearing all of its candidates is the ordinary result, not a failure to look hard enough."*

A high adjudication-call rate is the architecture working as designed. The number that bears on voice safety is the **confirmed** rate, which *is* logged — `log_over_settling_decision(world_id, screened, confirmed)` in `app/over_settling_logging.py` — but into a different stream the harness does not capture. §4's framing of 10-of-12 as an *"already-diagnosed defect"* inherits the same misreading. (The 10-of-12 count itself is exact: 3 + 3 + 4 = 10 over 12 turns; `over_settling_screen` ran 11.)

**The instrument that would work is unnamed.** `wrs/gates/core.py:211 readability_check()` — the project's own machine gate, keyed to Part Five's `reading_floor` — directly measures the thing objective 3 is about. The brief never mentions it, `wrs/parameters.yaml`, or the gate layer at all.

**And objective 4 has no metric at all.** No fabrication-signal rate is watched, despite it being the brief's one stated non-negotiable and despite the pilot having produced exactly such a signal (P0-2).

The per-world consequences of this gap are worked through in the Conversation-Improvement Prediction section below: **none of the six predictions is falsifiable by the two metrics §8 names.**

**Fix.** Replace §8's two metrics with: (1) the *confirmed* over-settling rate, capturing `app/over_settling_logging.py`; (2) per-signal drift counts, which requires logging the signal type; (3) `readability_check` FK/FRE before and after, per world; (4) the fabrication-signal rate; (5) a counted unprompted-term-clarification tally, since that is the behaviour finding (C) is actually about and nothing currently counts it.

---

## P1 — materially improves, not disqualifying

### P1-1. The `wrs/` record layer is entirely absent from §4's scope carve-outs and §7's edit targets.

Every world has a structured record set under `wrs/records/<world>/` including a `voice_profile/` record (e.g. `hieronymian_world/voice_profile/halvoice001.md`, which carries `identity`, `speaking_model`, `persona_name`, `role_label`, and `identity_rationale_ref` — all register-relevant). There is a generation-and-parity workflow alongside it: `wrs/views/permanent_prompt.py`, `wrs/views/capsule_prompt_views.py`, and `wrs/views/probe_parity.py`, which compares the **deployed** `data/<world>/*_Permanent_Prompt_*.txt` against a generated `*_Permanent_Prompt_generated.txt` in a staging directory.

The runtime source of truth *is* `data/` (`app/main.py:156` reads `world_config.permanent_prompt_path`), so §7's edit target is correct for runtime. But hand-editing six deployed `.txt` files without touching the corresponding `voice_profile` records desynchronises the record layer that the project's own gates and parity views read. §4 lists five things not to rebuild and this layer is not among them; §7 lists edit targets and does not mention it.

**Fix.** Add the `wrs/` record layer to §4 with an explicit decision — either "records follow the deployed prompt, update after" or "records lead, regenerate" — and give the Research stage the task of confirming which.

### P1-2. §8's regression baseline does not durably exist.

§8: *"Regression-check the original three baselines (**transcripts already saved**, referenced in the Decision Log entry in §3)."*

`mark_conversation_test.py:195-197` writes to `<repo-root>/mark_conversation_test_results.json`. That file is **not in the repo** (`ls /home/user/CIC-Project/*.json` returns nothing; `git status --short` is clean). The only copy is in a session-scratchpad temp directory. The Decision Log entry does not carry them either (P0-7). A fresh Fable thread on Friday will have no baseline to regress against.

**Fix.** Commit the three baseline transcripts to a durable path in the workstream folder and cite that path in §8.

### P1-3. §5(D)'s "they're the three plainest worlds already" is measurably false for Yausep.

Measured mean sentence length across the Representative turns of the three saved baselines:

| World | words | sentences | **mean sentence length** | em-dashes / 100 words |
|---|---|---|---|---|
| Papnoute | 553 | 38 | **14.6** | 1.81 |
| Chloe | 1,061 | 64 | **16.6** | 1.51 |
| **Mar Yausep** | 1,149 | 50 | **23.0** | **1.83** |
| *(Albina, pilot current arm)* | *708* | *30* | *23.6* | *1.55* |

Yausep's sentences are as long as Albina's — the world the brief calls the elaborate exception — and he has the highest dash density of the three. §5(A)'s own text half-concedes this (*"more archaic-leaning surrounding vocabulary"*), which makes (D)'s "three plainest" an internal contradiction as well as a measurement error. It matters because (D) is the argument for why the acceptance evidence has to come from Albina and Marius; that argument holds for Papnoute and Chloe and does not hold for Yausep.

### P1-4. Yausep's permanent prompt already contains objective 1's mechanism — and that world still showed the failure. The "direct comparative reading" missed it.

`syr_..._Yausep.txt:45`:

> *"**Before you reach for raza, qyama, or Iḥidaya as your first word, ask whether your own record gives you a face, a name, or a scene for this question instead** — a seat kept empty twenty years, a bishop killed for holding his post, a demonstration given while your teachers were dying. Where such a thing exists, begin there. **Let the word follow the story, not stand in front of it.** And when your own vocabulary does carry the answer, bring it one term at a time. Ground each one, briefly, in what it means before reaching for the next."*

That is objective 1 ("Period flavor arrives once the bridge is built, not as the price of admission") and the term-grounding half of objective 2, already written, in a world that nonetheless produced the FLAG-018 behaviour in the same live test finding (C) cites. This is a second, independent instance of the "prose guard already present and already insufficient" pattern — free evidence, available from the six files §5(A) claims to have read comparatively, and it strengthens finding (C)'s case considerably.

### P1-5. §4's scope carve-outs miscount which files carry which shared blocks.

| Brief §4 says | Verified |
|---|---|
| near-verbatim "museum guide" fabrication-guard block in **Yausep, Theon, Marius** | `grep -l "museum guide"` → **Yausep and Marius only** (2 of 6). Theon carries a *reworded* version (`alex_..._Theon.txt:7`, *"Picture one who keeps the reading of a school long since scattered"*) — the same three-failures structure, different image. |
| "witness not recruitment" block in **Chloe, Albina, Yausep, Theon, Marius** (5, silently excluding Papnoute) | present in **all six**. Papnoute has it at `:17` (*"You make this way of life intelligible to someone who does not share its assumptions... Whoever is speaking with you is free to leave this conversation exactly as they arrived"*). Confirmed by `grep -l` on both marker phrases: 6/6. |
| — | Not stated: **Chloe and Albina carry no museum-guide-class fabrication-guard block at all.** Their anti-fabrication content is distributed through other paragraphs. |

§4's instruction is *"Do not edit, shorten, or soften this under any framing"* — a carve-out whose file list must be right, in a brief that schedules all six of those files for rewrite. Papnoute is 4th in the sequence and the brief's list implies his file has no witness-not-recruitment block to protect.

### P1-6. §5(C) names only Chloe as carrying a per-world FLAG-018 analogue. Marius carries one too — and Marius is one of the two acceptance-evidence worlds.

`ijc_..._Marius.txt:119`:

> *"A finding once rendered stands as rendered. When you have used one of your own words and its sense has been given — by you, or by the gloss that travels with it — you do not circle back in a later turn to re-explain it or to ask whether it was taken rightly, unless the petitioner themselves asks. A chancery does not reopen its own entries to confirm they were read; if a word's sense matters again, the clarity arrives inside the new finding, while the word is doing its work."*

Structurally identical to Chloe's `:29`. Marius also uniquely receives an extra IJC-scoped post-history guard appended at `nodes.py:1174-1180` that no other world gets. Both facts matter for a world §5(D) names as primary acceptance evidence.

### P1-7. Objective 4 has no deliverable in §7 and no metric in §8 — a completeness-mapping gap on the brief's own non-negotiable.

Mapping §6 → §7/§9:

| Objective | Deliverable |
|---|---|
| 1 — bridge-first | §7 Part A bullet 1; §7 Part B ✓ |
| 2 — Ecological Function / Distortion Risk + shape repertoire | §7 Part A bullets 1 & 3; §7 Part B ✓ |
| 3 — plain everyday English, Albina exception | §7 Part A "full diction/rhythm audit" + Albina paragraph ✓ |
| **4 — no fabrication rule moves** | **none in §7; none in §8; §4 says only "don't touch it"** |
| 5 — Framework self-sufficiency | §7 Part B ✓ |

Reverse mapping is clean except for §7's "three 'distinct from period diction' occurrences" bullet, which traces to no §6 objective and no §5 finding — it is introduced fresh in §7 and justified inline. That's acceptable but should be named as an in-scope addendum rather than appearing to descend from something.

Objective 4's gap is the one that matters: "don't touch it" is not a verification. Given P0-2 (the prototype tripped the fabrication check on Albina), a fabrication-signal regression check belongs in §8.

### P1-8. §7's "pilot against Chloe alone" contradicts §5(D)'s own logic — and the ad hoc pilot already demonstrated why.

§7 Part A: *"Pilot it against Chloe alone, verify in isolation (§8) before touching any other file."*
§5(D): *"re-testing only these three worlds and finding they 'still read fine' proves nothing, since they weren't shown to be broken in the first place."*

Chloe is one of those three. The same-day pilot did exactly this and produced a result that could not discriminate anything (P0-3). Chloe is a reasonable *safety* pilot — she is the plainest file, lowest blast radius — but the brief should say that, and should not imply the pilot produces acceptance evidence. Pair the Chloe pilot with a second pilot world that §5(D)'s own logic says can actually show a difference.

### P1-9. §4's "over_settling_adjudication ... not a rare safety net in practice" misreads the architecture as a defect.

Covered in P0-8's evidence. The Decision Log's original framing (line 49) is a **cost** finding — *"Second-biggest line item in the whole cost table"* — which is accurate and well-supported. §4 re-frames it as a governance-quality defect for Mark's triage. The screen is designed to over-flag; a 10-of-12 flag rate with an unknown confirmation rate is not evidence of anything being wrong with the check. It is evidence the second stage is expensive.

### P1-10. Theon is scheduled for a rewrite in §7 and verified nowhere in §8.

§7 sequences six per-world passes. §8 names Albina and Marius as primary acceptance evidence, and "the original three baselines" (Papnoute, Chloe, Yausep) as regression checks. **Theon appears in neither list.** He is the only one of the six with a scheduled rewrite and no verification of any kind — and he is third in the risk-ordered sequence, ahead of three worlds that do get checked. Alexandria also carries five of the nine chunks missing Ecological Function (P0-6), so his world is the one where §7 Part A's instruction no-ops most often.

---

## P2 — polish

1. **`app/rag/indexer.py:32` should be `:227`.** Line 32 is `tier: int`, a `LexiconEntry` dataclass field. `doc.metadata["tier"]` is constructed at `:227`. The substantive claim (per-chunk tier exists in metadata) is correct.
2. **Papnoute quote is inexact.** Brief: *"sentences stand next to each other, do not lean on each other."* Actual (`:7`): *"Your sentences stand next to each other; they do not lean on each other."*
3. **`over_settling` quote has a silent internal deletion.** Brief: *"the question is whether the specific qualification is present."* Actual (`facilitator_prompts.py:241`): *"The question is whether the specific qualification **this claim needs** is present."* Not misleading, but unmarked.
4. **"distinct from period diction" omits the template variable.** Actual text at 429/449/485 is *"distinct from `{representative_name}`'s period diction."* The **line numbers are exact** — a good catch by whoever wrote it.
5. **§1 attributes Article 6 to the wrong document.** Article 6 is a **Constitution** article (`L1-Foundation/CiC_L1_Constitution_V2_2.docx`); the Vision doc only notes it (*"Note: Constitution Article 6 refines the testable expression of this standard"*). The brief's four-condition rendering is otherwise **faithful and verified**.
6. **§3's commitment list mixes two Foundational Values with two Convictions** and omits Historical Responsibility and Intellectual Humility. See P0-7.
7. **§5(B) cites `sections.py` for something it cannot confirm.** It knows only Quick Meaning and Key Sources markers.
8. **§8's probe-category name is off.** Part Eight's category is **"Sustained Engagement Testing,"** not "sustained-multi-turn-coherence." ("Confidence-Under-Thinness" and "Self-Referential Probes" are both **exact**, and Part Eight genuinely has **no** naturalness/register probe category — that part of §7 Part B's mandate is a real, correctly-identified gap.)
9. **§8 says "Reuse `mark_conversation_test.py`."** Its `SCENARIOS` are hardcoded to desert / pahc / syriac (`:111-142`). Albina and Marius must be added. `mark_voice_simulation.py` already shows the pattern.
10. **§5(A) "Papnoute — richest register instruction" is arguable.** Marius's file is larger (4,431 vs 4,099 words) and its SECTION 3 is the longest single register block in any of the six. "The only file with worked example dialogues" is **verified exactly** (`{{random_user}}` appears in Papnoute only).

---

## What verified clean

Worth stating plainly, since this document is more right than wrong:

- **All 20 internal `§N` cross-references resolve** to sections that say what they are cited for. Zero broken pointers.
- **Balance ratio 52.1 / 47.9** (§1–§5: 1,898 words; §6–§9: 1,748). Per-section: §1 143, §2 129, §3 222, §4 552, §5 852, §6 220, §7 590, §8 293, §9 645. The prior brief's round-1 failure mode is absent.
- `app/rag/retriever.py:192` — **exact**. Line 192 is `for doc in result.documents:`, the per-document loop, and a sort key before it is the correct hook point.
- `facilitator_prompts.py` lines **429 / 449 / 485** — **exact**, all three.
- `representative_prompts.py:174-181` — **exact** for the guard text (though the file/segment attribution is wrong, P0-1).
- `truncate_at(body, KEY_SOURCES_MARKERS)` at `retriever.py:204`, stripping Key Sources — **verified**, and Ecological Function / Distortion Risk do precede it in every chunk that has them.
- **Article 6's four conditions quoted faithfully** from the Vision docx.
- **10-of-12 `over_settling_adjudication`** — verified exactly from the saved usage records (3 + 3 + 4).
- **`over_settling` screen prompt is genuinely tone-agnostic** — §4's core governance-safety argument holds. `citation_grounding` is paraphrase-tolerant content mapping. §4's conclusion is right even where P1-9 quibbles with one framing.
- **§7's capsule paragraph** and its *"the elevated register runs through more than the paragraph explicitly labeled 'how you speak'"* claim are both **correct**, and are the sharpest observations in the document.
- **Chloe's per-world FLAG-018 analogue** (`:29`) — verified.
- **Marius: "SECTION 3 — VOICE AND REASONING MODE," "the only one with explicit section headers," register/reasoning-mode entangled** — all verified.
- **Albina's periodic/hypotactic prescription** (`:29`) — verified, including that it is the sole exception among the six.
- **`confirmed_glosses.py` scope claim** — verified against its own docstring.
- **`mark_conversation_test.py` exists and does what §8 says it does**, with the network-free stand-in honestly documented in the script's own header (`:20-29`).
- **The `CitationModal.tsx` / `key_sources` defect is real and correctly characterised.** Confirmed structurally: `## CT Contest Type` and `## Related-Terms Reciprocity Note` sit *after* `## Key Sources` in the chunk files, so they are stripped from generation context but ride along in the `key_sources` metadata the modal renders.

---

## Conversation-Improvement Prediction

*What each of the six Representatives' actual conversations will look like after this brief is executed as written — with a falsification condition for each, and whether §8 would catch it.*

*Albina and Chloe are grounded in the real pilot transcripts (`mark_voice_simulation_results.json`, 3 turns each, current vs. prototype, run through the real backend). The other four are **untested extrapolations** from the comparative file reading and the 2026-08-05 baseline measurements — labelled as such, not measured results.*

**Measurement baseline used throughout** (Representative turns only, mean words per sentence / em-dashes per 100 words):

| | mean sentence length | dashes / 100w |
|---|---|---|
| Papnoute (baseline) | 14.6 | 1.81 |
| Chloe (baseline) | 16.6 | 1.51 |
| Chloe (pilot, current) | 17.9 | 1.26 |
| Chloe (pilot, prototype) | **16.7** | **2.04** |
| Yausep (baseline) | 23.0 | 1.83 |
| Albina (pilot, current) | 23.6 | 1.55 |
| Albina (pilot, prototype) | **23.5** | **1.70** |

---

### 1. Albina (Hieronymian) — *grounded in pilot transcripts*

**Prediction.** Her register will not measurably change, and the visible improvement will be entirely in first-sentence uptake.

The pilot is unambiguous on the first half: prototype mean sentence length 23.5 against current 23.6 — **a change of 0.1 words across three turns**. The prototype kept her periodic rhythm exactly, which §6 objective 3 wants, and moved her prose not at all.

What did change is where the turn starts. Current turn 1 opens on the question's *wording*:

> *"The word 'rich' cuts both ways here, and I will not dodge it."*

Prototype turn 1 opens on the participant's *assumption*:

> *"You ask this as though the wealth we gave away simply reappeared under another name, and I understand why it looks that way from outside."*

Same on turn 3 — current: *"Not the same — and I would not have you think otherwise, for it is Rome's whole aristocratic world that shaped even our own household..."*; prototype: *"You are asking whether it was equal, and I will not give you a comfortable yes to that."*

The prototype also reached deeper into the story corpus: it surfaced `hal_story05_marcella-death` (the Alaric sack) where the current arm reached only for the general Paula/hostel/hospital material. That is objective 2 working. It is also the turn that tripped `fabrication_adjudication` (P0-2), because it delivered epitaph-genre material as flat record against its own chunk's Usage Guidance.

**So, concretely, post-rebuild Albina will:** open two or three of three turns by naming the participant's own assumption in their words; keep sentences at 22–25 words; reach for named story chunks rather than generalised summary; and be at elevated risk of stating genre-shaped or single-source material more firmly than its own Usage Guidance permits.

**Falsification.** Wrong if any of: (a) mean sentence length drops below **19 words** — her prescribed periodic rhythm has been flattened and objective 3's stated exception has failed; (b) her three first sentences still open on the question's wording rather than the participant's assumption — objective 1 has not landed; (c) her story-chunk reach does not increase over the current arm's baseline of zero named story chunks in three turns.

**Would §8 catch it?** **No, on all three.** FLATTENING is not capturable (P0-8) and would not measure sentence length even if it were. `over_settling_adjudication` fired 3/3 in her current arm and 2/3 in her prototype arm — it would report a *decrease*, which is an artefact of the fabrication signal short-circuiting the chain, not a voice improvement. The one instrument that would catch (a) is `wrs/gates/core.py:readability_check`, which the brief never names. **Gap — P0-8.**

---

### 2. Chloe (PAHC) — *grounded in pilot transcripts*

**Prediction.** Sentences get marginally shorter, em-dash density gets meaningfully worse, and the unprompted term-clarification survives.

The pilot measured all three. Mean sentence length 17.9 → 16.7 (−7%). Em-dash density 1.26 → **2.04 per 100 words, a 62% increase** — directly against `_HOW_YOU_ENGAGE`'s own explicit prohibition (*"The em dash as a default connector... A dash-linked clause every sentence or two is a mechanical tic, not a style"*) and against Part Five's *"avoiding long chains of clauses joined by em-dashes."* This is a predictable mechanical consequence of bridge-first prose: naming the participant's assumption before answering adds an appositive framing clause, and the appositive reaches for a dash.

The clarification survived in both arms (P0-3), and the prototype made it slightly worse by appending a check-in: *"Does that match what you had in mind?"*

The prototype also introduced a false conversational memory in turn 1 (*"You asked this before"*) and, on the other side of the ledger, produced the clearest genuine improvement in the whole pilot — turn 3's explicit retraction of the over-settled Corinth outcome the current arm had asserted.

**So, concretely, post-rebuild Chloe will:** run at 16–18 words per sentence; carry roughly **2 em-dashes per 100 words**, up from 1.3; still open at least one turn in three with an unprompted term clarification unless the fix is placed at the `nodes.py` layer-3 wiring site rather than in `_HOW_YOU_ENGAGE`; and be measurably more honest about where the record stops.

**Falsification.** Wrong if a three-turn post-rebuild run shows **zero** unprompted term clarifications *and* em-dash density at or below **1.3 per 100 words**. Either alone falsifies half of it.

**Would §8 catch it?** **No.** Nothing in §8 counts term clarifications — the behaviour finding (C) is entirely about — and nothing counts dashes. `over_settling_adjudication` fired 3/3 in *both* pilot arms: §8's own metric would report **no change** on the turn where the prototype produced its single clearest improvement. This is the sharpest instance of the metric gap: the number §8 watches is flat across exactly the change the brief most wants. **Gap — P0-8.**

---

### 3. Mar Yausep (Syriac) — **untested extrapolation, not a measured result**

**Prediction.** Yausep will show the **smallest** register change of the six, because the instructions §7 would add to him are already in his file and already not being followed.

He carries an explicit paratactic short-sentence rule (`:41`) and an explicit bridge-first "let the word follow the story" rule (`:45`) — and his measured baseline output is 23.0 words per sentence with the highest dash density of the three baselines (1.83/100w). His file already says the thing; the output already doesn't do it. Adding a shared-file version of the same instruction is adding a fourth voice to a chorus that is already being ignored.

**So, concretely:** expect his mean sentence length to remain **above 20** and dash density **above 1.5/100w** after the §7 pass. Expect his stage-by-stage demonstration mode to survive intact (it is deeply entangled with his content and §7 correctly flags it). Expect the FLAG-018 behaviour that surfaced in his baseline to persist unless the fix lands at layer 3.

**Falsification.** Wrong if his post-rebuild mean sentence length drops below **18 words** while his demonstration mode stays recognisable. If that happens, prose instruction in the shared file *was* sufficient after all — which would be genuinely informative and would partly rehabilitate finding (C)'s original claim.

**Why this is the cheapest discriminating test in the whole brief.** §9's Research stage names the Papnoute worked-example check as the discriminator. Yausep is better: he is the one world where the *specific instruction the rebuild proposes to add* already exists verbatim and demonstrably fails. Papnoute tells you whether worked examples work; Yausep tells you whether **prose instruction of any kind** is the right lever, which is the prior question.

**Would §8 catch it?** **No — and worse, it would mis-score it.** Yausep is a regression-check world in §8, checked against *"confirm nothing about them got worse."* A null result — the outcome this prediction expects — would be recorded as a pass. That is precisely the non-informative outcome §5(D) warned about, applied to the one world that could have discriminated. **Gap — P0-8 and P1-8.**

---

### 4. Papnoute (Desert) — **untested extrapolation, not a measured result**

**Prediction.** The §7 pass will move Papnoute in the **wrong direction**: his turns will get longer, not plainer.

He is already the plainest measured voice at 14.6 words per sentence, and his file's own hard measure is stricter than anything §6 asks for: *"four sentences is already long for you, and most of what you say should be one to three"* (`:13`). His baseline output ran ~138 words per turn.

The risk is §7 Part A's shape repertoire. Three of the four named shapes — *story-first*, *question-behind-the-question*, *consensus-then-contrast* — are structurally longer than his four-sentence ceiling. "Consensus-then-contrast" in particular ("most sure first, genuinely distinctive second, honestly unsettled last") is a three-movement structure that cannot fit in three sentences without becoming the stacked-list shape `_HOW_YOU_ENGAGE` explicitly forbids. §7 tells Fable to *"reconcile the new shape repertoire against that world's own existing reasoning-mode paragraph"* — for Papnoute the honest reconciliation is that most of the repertoire does not apply, and the brief should say so rather than leave Fable to discover it.

**So, concretely:** expect mean turn length to rise above 138 words and sentence length above 15 unless his four-sentence measure is explicitly protected in the per-world pass.

**Falsification.** Wrong if his post-rebuild mean turn length stays at or below ~138 words and his mean sentence length at or below 15.

**Would §8 catch it?** **No.** Papnoute is a regression-check world with no metric attached. "Nothing got worse" read by eye will not catch a 20% turn-length increase, and §8's two named metrics do not measure length. **Gap — P0-8.**

---

### 5. Theon (Alexandria) — **untested extrapolation, not a measured result. Never live-tested at any point.**

**Prediction.** Theon will show the **largest** improvement in first-sentence uptake and the smallest change in diction — and the §7 Part A instruction will silently no-op on ~10% of his retrievals.

His file's dominant relational instruction is already bridge-shaped: *"if the engagement has become a lecture, with the participant a spectator, it has departed from the way this world formed anyone. When you find yourself explaining at length, turn back into a question, back to reading-with"* (`:45`). A bridge-first instruction is closer to native here than in any other world. He also already carries the paratactic rule (`:37`) that §5(A) calls his register instruction "thin."

His "lyrical/devotional diction" is carried by *vocabulary* — light, the eye of the soul, nous, illumination, the door, the ascent — which objective 3 explicitly protects as *"seasoning, not performance."* So the diction change should be near zero if objective 3 is executed correctly.

The silent-no-op risk is specific and measurable: **5 of Alexandria's 50 lexicon chunks have no Ecological Function section at all** (`alexlex051`, `alexlex059`, `alexlex074`, `alexlex081`, `alexlex090`) — the highest absolute count of any world. On those retrievals, "lead with Ecological Function" points at nothing.

**So, concretely:** expect his opening sentences to shift from world-framing to participant-uptake in most turns; expect his period vocabulary count to stay within ±20% of baseline; expect roughly one turn in ten where the Ecological-Function instruction has nothing to act on.

**Falsification.** Wrong if his period-vocabulary count drops by more than a third — the rebuild has stripped the seasoning objective 3 protects rather than the performance it targets.

**Would §8 catch it?** **No — Theon is not in §8 at all.** Not a primary acceptance world, not one of the named three regression worlds. He is the only one of the six with a scheduled rewrite and zero verification. **Gap — P1-10, and this is the most complete verification hole in the document.**

---

### 6. Marius (Imperial-Juridical) — **untested extrapolation, not a measured result. Named acceptance world; never live-tested.**

**Prediction.** Marius will show the **least register change of any of the six**, and the real risk is not register at all — it is disturbing his precedent-first reasoning mode.

His SECTION 3 already prescribes exactly what objective 3 asks for, in more detail than any other file: *"A chancery does not write in one breathless clause. It sets down one finding. Then the next... you do not reach for one long sentence threaded with clause after clause to hold it all together. You break it the way a clerk breaks a long petition into numbered points: one short sentence for the first fact. A full stop."* There is close to nothing for a register pass to add.

What is genuinely at risk is the entanglement §7 correctly names. His register instruction and his reasoning-mode instruction are the *same paragraphs*: the short-sentence rule is derived from chancery practice, and the precedent-first rule (*"You reach first for precedent — a letter, a canon, a prior judgment — before you reach for a general argument from first principles"*, `:111`) sits in the same section. Editing one for rhythm risks loosening the other. He also carries a per-world FLAG-018 analogue at `:119` (P1-6) and a unique IJC-scoped post-history guard at `nodes.py:1174-1180` — both of which a careless per-world pass could contradict.

**So, concretely:** expect his mean sentence length to move less than 2 words; expect the measurable change to be in bridge-first opening rather than diction; expect his Section 2A source-anchoring behaviour (Julius, Leo's Tome, the Constantinople canon, Ambrose, Damasus) to be the thing most at risk from a rewrite, because §7's diction audit covers "identity, era, and vocabulary paragraphs" and SECTION 2A is exactly that kind of paragraph.

**Falsification.** Wrong if a post-rebuild run shows him **stopping** leading with precedent — a letter, a canon, a prior judgment — in the majority of turns. If precedent-first survives and sentence length moved less than 2 words, the prediction holds.

**Would §8 catch it?** **Partially, and not the part that matters.** Marius *is* a named acceptance world, so he will be run. But neither of §8's two metrics measures precedent-first ordering, and neither of the two Part Eight probe categories §8 names (confidence-under-thinness, sustained engagement) tests it either. The Part Eight category that *would* is **Source-Awareness Probes**, which §8 does not name. **Gap — P0-8.**

---

### The aggregate gap, stated plainly — **P0-8**

Across all six predictions, **not one is falsifiable by either metric §8 names.** The two named metrics are:

- `FLATTENING` drift-signal rate — **not capturable at all** by the harness §8 names for the job, because the usage log records `drift_detection` as one undifferentiated label with no signal type.
- `over_settling_adjudication` firing rate — **measures the deliberately-over-flagging screen**, not the confirmed rate, and was flat at 3/3 across both pilot arms on exactly the turn where the prototype's clearest improvement occurred.

The instruments that *would* work all exist and none is named in the brief: `wrs/gates/core.py:readability_check` (sentence length, the project's own gate for objective 3), `app/over_settling_logging.py`'s confirmed rate (objective 2's honesty half), a per-signal drift log (FLATTENING), the `fabrication_adjudication` call rate (objective 4), and a counted term-clarification tally (finding C's actual subject).

Two of the six worlds' predictions would additionally be **mis-scored** rather than merely unmeasured: Yausep's expected null result reads as a regression-check pass, and Albina's over-settling count would show an improvement that is an artefact of the fabrication signal short-circuiting the chain.

This is the finding that most directly determines whether the Friday pass produces something verifiable or something that merely reads better. It is cheap to fix — five metrics, all with existing instruments — and expensive to skip.

---

## Recommended fix list, in order

1. Rewrite §5(C): four FLAG-018 layers with real locations; the guard is not in `_HOW_YOU_ENGAGE`; the pilot is a non-discriminating matched pair with a named confound; report the `fabrication_adjudication` firing; cite the 1-in-16 measured residual as the baseline. **(P0-1, P0-2, P0-3)**
2. Rewrite §5(A): drop "100%"; state the 5-of-6 paratactic uniformity; point the register hunt at the narrative body prose and the capsules, as §7 already correctly does. **(P0-5)**
3. Rewrite §5(B) with the measured numbers; name `Formation Ecology Connection` for stories; resolve whether Tier needs to reach generation. **(P0-6)**
4. Rewrite §7 Part B: Part Five already has the numeric floor and the gate. Name the actual gaps. Add a Research task to run the gate against all six deployed prompts. **(P0-4)**
5. Replace §8's two metrics with the five that exist. Add Theon to the verification list. **(P0-8, P1-10)**
6. Add the superseding note to `Decision-Log.md` lines 12 and 15; fix §3's transcript claim. **(P0-7)**
7. Commit the three baseline transcripts to a durable path and cite it in §8. **(P1-2)**
8. Correct §4's block-presence lists; add the `wrs/` record layer to scope. **(P1-1, P1-5)**
9. Add Yausep's existing bridge-first instruction to §5 and promote the Yausep check into §9's Research stage alongside the Papnoute check. **(P1-4)**
10. Sweep the P2 citation nits.

**Re-run this review after the edits.** Items 1–4 rewrite the diagnosis the whole brief rests on, which is exactly the material that has never been checked.
