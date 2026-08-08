# Adversarial review (round 1): `CiC_VoiceRebuild_Stage2_Design_2026-08-08.md`

*Opus review, dispatched 2026-08-08. This is the Stage-2 (Design) gate required by the brief's §9 — the pass that decides whether Blueprint is allowed to sequence this document. Per the Standard Practice's point 4, the brief (`Ministry/Features/Front-End-Integration-Strategy/CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`), the Stage-1 Research findings, and both Research review artifacts (`..._Research_Opus_Adversarial_Review_Round1_2026-08-08.md` and `..._TargetedRecheck_2026-08-08.md`) were read in full before any new hunting began, so this round is aimed specifically at what has never been checked: the design decisions themselves and the recon paragraph they rest on.*

*Named failure modes hunted, per point 5, in the form this thread's history has established: (1) fabricated or misattributed mechanism claims; (2) "already exists / already wired" claims about things that do not, and their inverse; (3) new positive prose at ~1 P0 per 350–500 words — this document is 3,655 words and is ~100% new positive prose; (4) instrument provenance — a claim that a committed artifact and a prose description are the same thing (the risk class the Research round named); (5) design decisions that quietly contradict a governing constraint.*

*Verification method, per points 1 and 3. Every recon claim in §0 executed, not read. Demonstration records counted per world directly from `wrs/records/*/demonstration/`. The S52 assembler run end to end (`python wrs/views/permanent_prompt.py`) and its output `diff`ed against both the committed staging file and the deployed `data/` prompt. The demonstration selector (`segments/demonstrations.py:_selected`) re-implemented against all six worlds' actual `trait_scores` and executed, world by world. All ten `wrs/views/segments/*.py` modules read whole, including `craft.py`'s 19 prose blocks. `wrs/records/*/voice_profile/*.md` read at `speaking_model`, `trait_rubric` and `native_measure` for all six worlds. `app/graph/nodes.py` read at 1140–1730 (post-history guard wiring, `HARD_CEILING_WORLDS`, the regenerate-on-overage branch), `app/length_ceiling_logging.py`, `app/prompts/representative_prompts.py` at 86–235, `app/prompts/facilitator_prompts.py` at 220–235, `app/rag/sections.py:150-160`, `app/rag/story_indexer.py:90-105`, `app/rag/indexer.py:225-229`, `app/rag/retriever.py:188-196`, `app/graph/repair_classifier.py`, `app/main.py:153-158` — each at the exact cited location. `leak_audit_apparatus_hits.json` re-parsed and its 104 files re-partitioned by section against the design's Layer-5 remediation scope. `scripts/` enumerated for existing instruments. Every number the document reuses from Research checked against the Research document's own tables. All 34 `§N` pointers extracted and resolved by hand. Word counts computed per section.*

---

## Bottom line

**Not ready. Blueprint must not sequence §1, §2 Layer 2, §2's turn-measure decision, §2 Layer 5, or §4.4 as written.**

**6 P0. 9 P1. 10 P2.**

Let me say what is genuinely strong first, because it is substantial and it is the reason this document is worth fixing rather than restarting.

**The document's central architectural claim survives the hardest test I could put to it.** I ran `wrs/views/permanent_prompt.py`. It regenerated `wrs/views/staging/desert_world/desert_Representative_Permanent_Prompt_S52.txt` byte-identical to the committed file, and `diff` against `data/desert_world/desert_Representative_Permanent_Prompt_Papnoute.txt` is **empty**. Desert's deployed prompt *is* the assembly output, today. The determinism claim ("same records → byte-identical output") holds, and the "assembly-identity check" §1 proposes as probe_parity's replacement already passes for Desert without anyone having built it. That is a real and load-bearing fact, and the document is right to build on it.

**The recon paragraph's countable claims are all correct.** Demonstration records: Desert 6, the other five 4 each — counted. All six worlds carry `voice_profile` and `world_core`. The `voice_profile` structure is exactly what §0 says it is: a Hymes SPEAKING model (`setting` / `participants` / `ends` / `act_sequence` / `key` / `instrumentalities` / `norms` / `genre`) plus a `trait_rubric` whose traits carry situation-conditioned intensities. The selection rule is verbatim in `demonstrations.py:1-17` ("the records whose trait_scores carry no 'weak'… capped at 3"). Segments carry `cache_stability` and `eviction_priority` and `ASSEMBLY_ORDER` really is static → session → turn. The post-history guard really is an assembly export (`guards.POST_HISTORY_GUARD`, consumed at `nodes.py:1154`, documented as "the assembly's own export" at `representative_prompts.py:214`). `main.py:156` is exactly the permanent-prompt read line.

**Every number reused from Research reproduces.** 81% PAHC; Albina prompt FK 9.3 and Hieronymian capsule 11.5; Chloe prompt 6.8 (second best); PAHC capsule 13.3 (worst of twelve); Marius the only prompt failing both numbers; Yausep at the FK line; 3/8 vs 6/8; 7.5–7.9 invisible calls; four per-world prompt ceilings; 26–76 source records with IJC at 41; Alexandria's 50 lexicon chunks and its EF-less lead; all six IJC story chunks shipping Final Assembly blocks. Every code citation I checked lands at the right line: `sections.py:159-160`'s fail-open, `story_indexer.py:98`'s two-entry strip list (so the one-line addition really does close 6 of the 8), `facilitator_prompts.py:228`'s "first tried as one signal among ten… and caught nothing" verbatim, `indexer.py:227`'s `tier`, `retriever.py:192`'s per-document loop, `repair_classifier`'s HOLD/CONCEDE adjudication, and the three-segment caching contract in `build_representative_prompt`.

**And the balance ratio is healthy — the failure mode Round 1 named for the brief does not recur here.** 3,655 words: framing and cost narrative (§0 + §8 + header) 448 = **12.3%**; actionable design (§1–§7, §9) 3,207 = **87.7%**. This is a design document, not a re-diagnosis with a design attached.

**But the recon paragraph says it was "verified directly before designing on it," and the parts of it that were read rather than executed are where the failures are.** Every P0 below is a claim about what the existing machinery does, made from reading a docstring or a filename rather than running the code against the fleet's actual records. When I ran it:

- **The demonstration selector — the mechanism §2 makes "the strongest voice lever we measured" — yields zero demonstrations for Marius**, and its only negative token, `"weak"`, appears in **zero** demonstration records fleet-wide. Three worlds score in a vocabulary (`PASS`, `PARTIAL (pre-fix register)`) the filter cannot read. The pilot world's four demonstrations are of a **predecessor persona**, self-labelled, carrying bracketed apparatus the assembly's stripper does not match.
- **All six** of Papnoute's demonstrations score `partial` on terse economy at 146–311 words against his record's own 60-word measure — not "one," as §4.4 says.
- **`world_ground.py`'s own docstring says the exact opposite** of §8's cost claim: "the capsule listing is NOT folded in… the deployed World Capsule file stays in place."
- **A live, per-world, code-enforced turn-length ceiling with regenerate-on-overage exists for all six worlds** (`nodes.py:1617`), wired to each world's `voice_profile.native_measure`, with its own logging module. §2's turn-measure decision does not know it exists, and its stated rationale is false because of that.
- **The Layer-5 build gate fails on 23 files that no Layer-5 remedy touches**, Desert alone contributing 9 of its 17.
- **The insight-field authoring pass claims a brief license the brief grants only to capsule files.**

None of the six is a writing problem. Each one, sequenced as written, would send Build to do work that cannot be done, or to skip work that must be.

---

## P0 — fix before this document gates Blueprint

### P0-1. The rubric-selected demonstration mechanism does not work on five of six worlds' records. Executed against the fleet: Marius gets zero demonstrations, and the filter's only negative token appears nowhere in the corpus.

§0: *"The S52 assembly machinery… **already implements, for Desert**: rubric-selected demonstrations (records with no "weak" trait score, capped at 3)… What exists is one world assembled and five worlds' records waiting on `DELIBERATELY TEMPORARY` assemblers."*

§1, ground 3: *"**The machinery is one world from done, not zero.** … **Five worlds need their records routed through the same segments — a generalization, not an invention.**"*

§2, Layer 2 makes this mechanism the load-bearing one: *"Demonstration (the strongest voice lever we measured)… rubric-scored, assembly-selected (no "weak" scores, cap 3–5…)."*

The selector, verbatim at `wrs/views/segments/demonstrations.py:10-17`:

```python
def _selected(demos: dict, cap: int = 3) -> list:
    keep = []
    for did in sorted(demos):
        d = demos[did]
        scores = [t.get("score") for t in d.get("trait_scores", [])]
        if scores and "weak" not in scores:
            keep.append(d)
    return keep[:cap]
```

I re-implemented this against all six worlds' actual `trait_scores` and ran it:

| World | demos | pass selector | assembled | score vocabulary actually present |
|---|---|---|---|---|
| Desert | 6 | 6 | 3 | `partial`, `strong` |
| Alexandria | 4 | 4 | 3 | `partial`, `strong` |
| Hieronymian | 4 | 4 | 3 | `PASS`, `PASS (strong)`, `PASS (scoped)`, `PASS (after escalated retest)` |
| **Imperial-Juridical** | 4 | **0** | **0** | *(no `trait_scores` field at all)* |
| PAHC (pilot) | 4 | 4 | 3 | `PASS (predecessor evidence)`, `PASS-PROVISIONAL (predecessor evidence…)` |
| Syriac | 4 | 4 | 3 | `PASS`, `PASS (after fix)`, `PASS (strong)`, `PARTIAL (pre-fix register)` |

Four separate defects, each verified at source:

1. **Marius assembles with no demonstrations.** All four IJC demonstration records carry **no `trait_scores` key** (`grep -c trait_scores wrs/records/imperial_juridical_world/demonstration/*.md` → `0` for all four). `scores` is empty, `if scores` is false, nothing is kept, and `render()` returns `""`. The design ranks Marius as **highest file risk** (§4.2) and makes demonstrations the strongest lever — and the mechanism it adopts gives him none.
2. **The rubric filter is a no-op fleet-wide.** `grep -ril "weak" wrs/records/*/demonstration/` returns **nothing**. The one score value the selector rejects exists in no record in the project. For every world that has scores at all, selection is therefore "the first three by sorted id," not "the rubric doing the selecting, not taste" as the module claims. Syriac's `PARTIAL (pre-fix register)` demonstration — a record explicitly labelled as pre-fix — passes and would be selected.
3. **IJC's demonstrations are fragments, not dialogues, and carry apparatus inline.** `ijcdemo001.md` self-declares: *"FRAGMENT DEMONSTRATION (declared shape difference from the PAHC full-dialogue demos)"*, and its `dialogue` field reads `MARIUS [Phase-5 validated fragment - see provenance]…` followed by `[The record's own grading note: 'no echo of the participant's own "evidence" wording…']`. §0's blanket characterisation — all six worlds' records "in `{{random_user}}` dialogue form with per-trait `trait_scores`" — is false for IJC on both halves.
4. **The pilot world's demonstrations are of a different persona, and carry unstripped apparatus.** All four PAHC demonstration records score `PASS (predecessor evidence)`; `pahcvoice001.md`'s own `native_measure` note explains why — *"no Chloe-era live responses exist to measure (the Phase-5 evidence tests the predecessor persona under a superseded prompt)."* `pahcdemo001.md`'s dialogue carries `[predecessor validation persona - see this record's provenance note]` **four times**. The assembly's stripper (`segments/_common.py:voice`) matches only parenthesised `(Doc|LiveTest|SS|Article|app/|representative_…)` — it does not touch square brackets. Routed through the existing segment as-is, that apparatus enters the pilot's prompt through the design's own strongest lever, which is precisely the leak class Layer 5 exists to close.

**A fifth, smaller problem inside the same layer.** Layer 2 mandates *"one targeted demonstration per world aimed at that world's own measured failure."* The selector takes `sorted(demos)[:cap]`. A newly authored targeted demonstration (`syrdemo005`, `alexdemo005`, …) sorts **last** and is cut by the cap. The design mandates an artifact the mechanism it adopts cannot be relied on to include.

**Why this blocks.** §1 ground 3 is one of four grounds for adopting the architecture, and it is the only one about *effort*. "A generalization, not an invention" is what tells Blueprint how to size the five remaining worlds. The true statement is: one world (IJC) needs its demonstration records rebuilt from scratch to a schema that does not exist in them; three worlds (HAL, PAHC, SYR) need their score vocabulary normalised before the rubric filter means anything; the pilot world needs its four demonstrations re-authored for the actual persona; and the selector needs a real rank key before "rubric-selected" and "one targeted demonstration per world" can both be true. That is a materially different Blueprint.

**Fix.** Replace §0's uniform characterisation with the per-world table above (or its equivalent, re-derived). Rewrite §1 ground 3 to state what actually generalizes (the segment shapes, the eviction/cache metadata, the assembly-identity property — all real) and what does not (the demonstration schema, which is inconsistent across four worlds and absent in one). Add a named Blueprint task for a demonstration-record schema normalisation with a single score vocabulary, and specify the selector's rank key so the targeted demonstration is guaranteed selection rather than cut by `sorted()[:3]`.

---

### P0-2. §4.4 says one of Papnoute's demonstrations overruns his measure. All six do, by 2.4×–5.2× — and "codify, not change" contradicts an explicit brief instruction naming Papnoute by name.

§4.4: *"**Papnoute (Desert).** The existence proof — approach is *codify, not change*: his records already assemble to the fleet's best-held voice. Work: bring his six demonstrations through the trait-score refresh (**one is scored "partial - essay-length" against his own measure — fix or replace it**), confirm the assembly reproduces his held battery, and **use his pass to freeze the fleet-wide segment design before riskier worlds run**."*

Every one of the six carries exactly one `partial`, and in every case it is `terse economy`. Their own notes, verbatim:

| Record | score | note |
|---|---|---|
| `desertdemo001` | partial | *"146 words - well over the 60-word native measure… the economy is essay-length, not saying-length."* |
| `desertdemo002` | partial | *"164 words… this still exceeds the native measure by 2.5x - predates the runtime ceiling."* |
| `desertdemo003` | partial | *"168 words; the fullest of the three… this length is the construction-era register, not the deployed measure."* |
| `desertdemo004` | partial | *"218 words - live-tested before the runtime 60-word measure… this is construction-era length"* |
| `desertdemo005` | partial | *"205 words; same construction-era note"* |
| `desertdemo006` | partial | *"311 words; same construction-era note"* |

`desertvoice001.md`'s `native_measure` is `typical_words: 60`, and its own note says: *"The Doc10 test exchanges predate this measure and run longer; their demonstration records score that honestly rather than retro-fitting."* The record layer knew this and said so.

Three consequences the design gets backwards:

1. **The assembled prompt currently injects three essay-length demonstrations into the world whose hard measure is four sentences.** `partial` is not `weak`, so all six pass the filter; the first three by sorted id (146/164/168 words) are selected; I confirmed they appear verbatim at lines 69/72/75 of the deployed prompt. The design's own §2 Layer 2 says demonstrations demonstrate "plain sentences at the world's own measure." Desert's do not, and Desert is the bar.
2. **"Use his pass to freeze the fleet-wide segment design" is therefore the riskiest sequencing choice in the document**, not the safest one. Freezing the segment design on a world whose demonstration set fails its own measure 6/6 propagates that as the fleet standard.
3. **"Codify, not change" contradicts the brief directly, in a sentence the brief wrote pre-emptively about Papnoute.** Brief §7 Part A: *"Write worked `{{random_user}}`-style example dialogues for **all six** worlds as part of this same fresh build (five currently lack them, **Papnoute doesn't — write his fresh too rather than treating him as already done**, so all six are built to the same standard)."* §4.4 treats him as already done and scopes his work to a trait-score refresh. It also contradicts this document's own §1: *"Voice prose inside records — register craft, **demonstration dialogues**, `voice_profile` trait descriptions — remains fresh, per-world human-reviewed writing… under the brief's clean-rebuild mandate."*

**Why this blocks.** §1's quality governor names "Papnoute's fully-held battery as the working bar" and §4.4 makes his pass the fleet-wide design freeze. Both rest on an account of his records that is wrong by a factor of six, and the approach attached to it is the one the brief specifically forbade.

**Fix.** Correct the count to six with the word counts and the 60-word `native_measure` stated. Change §4.4's approach from "codify, not change" to a fresh demonstration write per the brief's own instruction, keeping the assembly-identity and battery-reproduction checks. If the segment-design freeze is still to happen on Papnoute's pass, say explicitly that it happens *after* his demonstrations are rebuilt to his measure, not before.

---

### P0-3. §8's "the world_ground segment already merged them for Desert" is contradicted verbatim by `world_ground.py`. No assembler emits a capsule for any world, and the one that tried says hand-authored capsule prose "will not round-trip."

§8, first cost bullet: *"Fewer tokens per turn in steady state: … **capsule and prompt no longer duplicate world-ground content (the world_ground segment already merged them for Desert)**."*

`wrs/views/segments/world_ground.py`, the module's own docstring, lines 4–8, verbatim:

> *"**The world's-own-words capsule listing is NOT folded in: the deployed World Capsule file stays in place at the swap** (the runtime concatenation and the adjudicators' capsule evidence are unchanged - **the full fold-in lands at S6.5's compatibility retirement**, declared in the S5.2 artifact)."*

And its own `sources` string, line 25: *"…**capsule listing NOT folded in (capsule file stays deployed until S6.5)**."*

There is a genuinely confusing second artifact — `permanent_prompt.py`'s module docstring says *"the capsule's world-ground content now lives inside the assembly's own world_ground segment"* and its budget field says *"(§5.1; today's capsule folded in)"*. Two committed docstrings in the same view disagree. **The dispositive evidence is not either docstring but the deployed state:** `data/desert_world/desert_World_Capsule_Core.md` is still there, still 100 lines, still loaded on every turn by `main.py:157`, and its "What Organizes Everything" section still covers anachōrēsis, the logismoi, diakrisis, manual labour, and the tested-word-vs-office authority tension — the same material as `world_ground` paras 4, 5 and 6. **The duplication the cost bullet says was eliminated is present in the file the runtime reads today.** The design's own §1 concedes as much when it says the capsule files "stay as the runtime's read surface."

**The second half is worse, and it propagates further.** §1 says the capsule files "become build artifacts: emitted by the per-world assembler," and §4's preamble says *"both the prompt and capsule surfaces regenerate from the same records."* **No assembler emits a capsule for any world, including Desert.** `permanent_prompt.py` writes exactly two files, both prompt-side. The only capsule assembler in the repo is `capsule_prompt_views.py`, whose own docstring says:

> *"**DELIBERATELY TEMPORARY** (blueprint S2.8)… The capsule view assembles the same SS5.1 'world's own ground' material at fuller depth… **Hand-authored capsule prose will not round-trip** - the S2.8 capsule parity is a SECTION-level classified comparison."*

So the capsule half of the architecture is not "one world from done." It is zero worlds from done, with a committed statement that the record layer cannot currently reproduce capsule prose at all. Research §3.1 established the capsule layer as "the register's second carrier, measured" — three of six capsules fail both readability numbers, and the worst file of all twelve is a capsule. This is the half of the surface the design has the least mechanism for and says the least about.

**Why this blocks.** §8 is the section that answers Mark's "cheaper," and this is its only *already-demonstrated* token-reduction mechanism. §1 and §4 both sequence capsule regeneration as though it were the same operation as prompt regeneration. Blueprint would sequence six capsule regenerations against machinery that does not exist and a committed note saying the prose will not round-trip.

**Fix.** Delete or rewrite the §8 bullet: state that world-ground fold-in is *designed and deferred* (S6.5), not done, and do not claim the token saving until it is. Give the capsule its own named design paragraph: what record fields carry capsule content, what happens to the prose that "will not round-trip," and whether the fold-in (prompt absorbs world-ground, capsule retires) or the parallel-emit (capsule stays, regenerated) is the chosen path. This is a decision, and right now it is being made by omission.

---

### P0-4. §2's turn-measure decision is made without a code-enforced per-world turn-length ceiling that already exists for all six worlds — and the decision's stated rationale is false because of it.

§2, the turn-measure decision: *"Rationale: **the shared ceiling is the only brake for worlds whose records don't state one (Theon, Marius today)**, the highest-weighted naturalness trait is length restraint, and every addition above pushes length upward — **deleting the only universal brake** while adding instructions would be the exact failure the review rounds flagged."*

Both halves of the load-bearing clause are false.

**(a) Every one of the six `voice_profile` records states a measure.** I read all six at `native_measure`:

| World | `typical_words` | provenance per the record's own note |
|---|---|---|
| Desert | 60 | runtime ceiling |
| Hieronymian | 94 | MEASURED, 22 responses, range 41–157 |
| PAHC | 70 | DESIGNED, declared |
| Syriac | 98 | MEASURED, 19 responses, range 41–165 |
| **Alexandria (Theon)** | **140** | MEASURED from cleared Phase-5 Round-2 retest |
| **IJC (Marius)** | **120** | PROVISIONAL PLANNING FIGURE, declared |

Theon and Marius are precisely the two worlds the rationale names as record-silent. They are not. (Research §2's correction — Theon and Marius carry no ceiling — was about their **prompt files**, and was correct about those. This document transposed a prompt-file fact onto the record layer, in the same sentence in which it adopts an architecture that makes the record layer authoritative.)

**(b) There is a live, code-enforced, per-world turn-length ceiling with regenerate-on-overage, covering all six worlds.** `app/graph/nodes.py:1617`:

```python
HARD_CEILING_WORLDS = {"desert-monasticism": 60, "hieronymian-ascetic-literary": 160,
                       "alexandria-catechetical": 160, "syriac-edessa-nisibis": 165,
                       "post-apostolic-house-church": 150,
                       "imperial-juridical-christianity": 180}
RETRY_TRIGGER_MULTIPLES = {…1.5 / 1.2 per world…}
```

and, at `nodes.py:1668-1695`, if a first draft exceeds `ceiling * multiple`, the code injects a corrective turn (*"Your answer just now ran to N words; your own measure holds at most M. Say the same thing again, holding to it - fewer sentences, not less said."*) and **regenerates the whole response**. Outcomes are logged three ways — `OUTCOME_RETRIED`, `OUTCOME_DEAD_ZONE` (over ceiling, under trigger), `OUTCOME_UNDER` — through a dedicated module, `app/length_ceiling_logging.py`, whose docstring says it exists so *"the mechanism's fire rate, its dead-zone frequency, and the first-draft word distribution… become countable per world from a log."* The in-code comments record per-world freeze decisions by name (HAL-4, PAHC-5, IJC-5, the SYR and ALX freezes), each explicitly grounded in that world's `voice_profile` `native_measure`.

This matters in four places at once, and the document is silent in all four:

1. **The decision itself.** The real question is not "shared block, per-world records, or both" but "shared block, per-world records, or the runtime ceiling that already enforces it" — three layers, one of which is already the code enforcement the design's own Layer 5 argues for. §2's Layer 5 ("what stops being an instruction at all") lists the leak filter, the readability gate and retrieval ordering, and omits the single existing instance of exactly its own thesis, applied to the highest-weighted naturalness trait in the document.
2. **The duplicate source of truth.** The ceilings are hardcoded constants that *duplicate* `voice_profile.native_measure` (the code comments say so). Under "records become what humans write," this is exactly the desync the architecture exists to end — and it is the one instance the design never names.
3. **Verification.** §5's per-world checkpoint lists "turn length" as a measured item and names no instrument. `length_ceiling_logging.py` is that instrument, per world, already built, with a denominator.
4. **Cost.** §8 and §3 count invisible calls at 7.5–7.9 per reply. A ceiling retry is a **full main-response regeneration** — the most expensive call in the system — and it is in none of the design's cost arithmetic. PAHC's entry is annotated as "an ENFORCING ceiling… expected elevated retry rate initially"; PAHC is the pilot.

**Why this blocks.** §2 presents this as a decision "made and recorded," and §9 item 2 reports it as closed. It is made against a false account of both the record layer and the runtime, and it leaves the one mechanism that actually enforces turn length outside the design entirely — including outside the rebuild that will change every world's measure.

**Fix.** Rewrite the rationale against the true state: all six records carry a `native_measure`; all six worlds carry a runtime ceiling and retry multiple; the shared block's role is therefore a *default for the assembled prose*, not "the only brake." Add the third layer to the decision explicitly, decide whether `HARD_CEILING_WORLDS` should be read from `voice_profile.native_measure` rather than duplicated (this is the cleanest single win the architecture offers and the document misses it), name `length_ceiling_logging` in §5, and put retry cost into §8.

---

### P0-5. The Layer-5 build gate and the Layer-5 authoring pass have mismatched scope. Re-partitioning the committed audit's own 104 files: 23 fail the gate with no remedy anywhere in the design — 9 of them Desert's.

§2 Layer 5(b): *"…the general apparatus-pattern strip from the audit instrument's refined class **runs on serialized bodies as a build-time *gate* (fail the build, name the file)** rather than a runtime rewrite — authoring stays the fix, the gate makes leaks impossible to ship silently."*

§2 Layer 5(c) scopes the authoring fix: *"(c) **the insight fields (`Ecological Function`, `Formation Ecology Connection`)** get an authoring pass during each world's Build step…"*

The gate is the refined apparatus class. Its failing set is the 104 files in `leak_audit_apparatus_hits.json`. I re-partitioned that file by section against the design's remediation scope (EF + FEC + the `## Final Assembly Instruction` strip-list line from 5(b)):

| | files |
|---|---|
| Flagged by the refined class (= gate's failing set) | **104** |
| Carry a hit in `Formation Ecology Connection` | 45 |
| Carry a hit in `Ecological Function` | 33 |
| Carry a hit in `Final Assembly Instruction` | 8 |
| **Carry a hit in NONE of the three** | **23** |

The 23 uncovered files, by contaminated section: **World Meaning 14, Plural-Voices Note 3, Distortion Risk 2, Confidence 2, Related-Terms 2.** Per world:

| World | flagged | uncovered by any Layer-5 remedy |
|---|---|---|
| Alexandria | 33 | 6 |
| **Desert** | 17 | **9** |
| Hieronymian | 7 | 0 |
| IJC | 12 | 4 |
| PAHC (pilot) | 21 | 2 |
| Syriac | 14 | 2 |

**And a 20-file class the design cannot fix the way it proposes.** 20 files carry apparatus hits inside `## Usage Guidance` (IJC 6, PAHC 8, Alexandria 3, Desert 3). `app/rag/story_indexer.py:93-97` refuses to strip that section, for a stated anti-fabrication reason:

> *"'Usage Guidance' is deliberately NOT stripped here: it also carries real anti-fabrication instructions (e.g. 'must never narrate Peregrinus himself') that the Representative does need: any meta-scholarship language inside that section is fixed at the **chunk-authoring level** instead, case by case."*

So the gate would fail on files that a code-side strip is *specifically ruled out for*, and the authoring pass the design specifies does not reach them.

**Why this blocks.** Blueprint sequences this. A build-time gate whose failing set exceeds its remediation set by at least 23 files has three possible fates, all bad: it never gets switched on; the build stays permanently red; or somebody quietly narrows the gate to the two insight fields, at which point it stops being "the general apparatus-pattern strip" and stops catching the class the brief asked for ("build the filter to catch the pattern… not just the two confirmed examples"). Desert makes it concrete: §4.4 assigns Papnoute no leak remediation at all and then uses his pass to freeze the fleet-wide segment design — while 9 of his 17 flagged chunks are contaminated in `World Meaning` and `Distortion Risk`, outside every remedy in the document.

**Fix.** Either widen the authoring pass to every section the gate flags (and say so, with the per-world file counts above so Build can size it), or narrow the gate to the sections that have a remedy and state plainly that the residue is accepted with its size named. Add `Usage Guidance` as its own case with the `story_indexer` comment's reasoning carried, since it is the one class where code-side stripping is already ruled out on record. And add leak remediation to §4.4's Papnoute work list, or move the segment-design freeze to a world whose corpus the gate actually passes.

---

### P0-6. Layer 5(c) licenses rewriting lexicon and story chunk fields under "the brief's prose-style-in-scope rule." The brief grants that rule to World Capsule Core files only — in the same bullet that names chunks as fixed ground truth.

§2 Layer 5(c): *"…the insight fields (`Ecological Function`, `Formation Ecology Connection`) get an authoring pass during each world's Build step to translate apparatus vocabulary into voice-safe insight (**content unchanged, form rewritten — the brief's prose-style-in-scope rule**), prioritized by the audit's per-world rates."*

The brief's §4.1, fourth fixed item, verbatim and complete:

> *"**The world/source layer's actual content and historical fact** — **lexicon chunks, story chunks, source registries**, and, in every permanent prompt, who each Representative is, what span they speak from, their world's real terms. **Confirmed good by Mark directly. This is ground truth, not a technique — categorically different from everything in §4.2.** Prose *style* inside the **World Capsule Core files** is explicitly in scope (§7); their *content/sourcing* is not."*

The style carve-out is scoped, by name, to World Capsule Core files. It appears in the same bullet that lists lexicon chunks and story chunks as fixed, and the bullet's own "categorically different from everything in §4.2" line is there specifically to stop the §4.2 open-form license from reaching this material. Brief §7 Part A reinforces the direction: it asks for a **filter** ("build the filter to catch the pattern"), never a chunk-authoring pass. §7 Part A's per-world bullets scope the fresh writing to "each world's permanent prompt and World Capsule Core" — chunks are named only as *inputs*.

Research saw this coming and said so. Research §8 question 4: *"The leak fix's split… code-side vs authoring-side vs prompt-side — Research's finding is that all three exist and are different problems; **Design decides the combination and sequencing against the brief's §4 content-freeze rule.**"*

The design does not decide it against the freeze rule. It asserts the freeze rule already permits it, attributing to the brief a license the brief did not give, and does not escalate.

**Two things I want to be fair about.** First, the substance may well be right — Research §4's finding that "a prompt-side filter instruction alone cannot fix the first half (the model cannot un-see what the field says)" is sound, and there is in-repo precedent for chunk-authoring-level fixes (`story_indexer.py:96-97`, quoted in P0-5, says meta-scholarship inside Usage Guidance "is fixed at the chunk-authoring level instead"). Second, "form not content" is a real distinction and the design draws it correctly in principle. The defect is not the proposal; it is that a proposal touching material Mark personally confirmed and the brief personally froze is presented as already-licensed housekeeping rather than as the escalation Research told Design to make.

**Why this blocks.** §7 lists "Mark's calls, queued" and this is not among them. Blueprint would sequence an authoring pass over ~78 chunk files (45 FEC + 33 EF) — under P0-5's fix, potentially all 104 — as routine Build work, on files whose content the brief calls ground truth. If the license is wrong, that is the single largest scope error in the document.

**Fix.** Move this to §7 as a named Mark decision, with the brief's §4.1 text quoted and the case for it stated: the insight fields are the two most apparatus-contaminated fields in the corpus (Research §4); the leak cannot be closed prompt-side; the change is to form, with content and sourcing untouched; the `story_indexer` precedent exists. Then remove the claim that the brief's existing rule already covers it, in Layer 5, §6 (which carries the same "insight-field authoring standard" into the Construction Framework), and §9 item 4.

---

## P1 — materially improves, not disqualifying

### P1-1. Layer 2 presents an existence proof as comparative evidence for a form decision no CiC evidence bears on.

§2 Layer 2: *"**Form decision (Research q6): positive-only as the default.** **The evidence:** Papnoute's positive-only demonstrations are the one configuration that held the live battery completely; no measured CiC evidence shows contrastive pairs outperforming…"*

Research §5.3 is explicit: *"**Not settled:** that worked examples are *the cause* of Papnoute's clean run… **the comparison cannot isolate the examples variable.**"* And no contrastive condition was ever run — so Papnoute's battery is not evidence about positive-vs-contrastive at all, in either direction. The second clause ("no measured CiC evidence shows contrastive pairs outperforming") is true and empty: there is no measured CiC evidence about contrastive pairs.

The decision itself is defensible — the parroting caveat (Research P5) is real evidence against adding in-register negative text, and the recorded per-world fallback is good discipline. The defect is that the strongest-sounding clause is the one that carries no information, and it leads. **Fix:** lead with the parroting caveat and Anthropic's 3–5 guidance, state Papnoute's run as an existence proof for the *combination* (Research's own wording), and say plainly that positive-only is a default chosen under absent comparative evidence, which is what makes the recorded fallback necessary.

### P1-2. §3's cost argument for the rebuild rests on the cross-world comparison Research flagged as register-confounded, with the caveat dropped.

§3, `over_settling` adjudication row: *"The probes' own data says the rebuild itself is the cheapest fix candidate: **the plainest, best-held voice fired it at *half* the rate of the register-heavy one (3/8 vs 6/8)**."* And the net-cost posture: *"**voice quality is the cost fix** — a voice that doesn't over-settle doesn't pay for adjudication."*

Research §5, conditions: *"**cross-world comparison is register-confounded** (Papnoute's formation is intrinsically the plainest). **The within-world findings… are the clean half.**"* Papnoute vs Yausep differs in register, formation, corpus, retrieval surface and prompt structure at once; the 3/8-vs-6/8 gap supports the cost hypothesis but cannot carry "the rebuild itself is the cheapest fix candidate."

The **decision** (keep, measure, pre-commit the downgrade rule) is robust to the confound and is the right call — this is only the rationale overreaching. **Fix:** carry Research's confound sentence into §3 and label the hypothesis a hypothesis, which is what the pre-committed measurement is there to test.

### P1-3. Instrument provenance: Stage-1 instruments and results are attributed to Stage 2 in four places.

§1: *"five instances incl. **this stage's** live probes"*; §1: *"what held **this session's** battery"*; §2 Layer 5: *"the output wiring lives in the probe harness (**already built this stage**)"*; §5: *"the 8-turn probe battery (**this stage's** instrument)"* and *"**this stage's** Yausep/Papnoute probe transcripts."*

All of it is Stage 1's: `scripts/voice_rebuild_research_probe.py` and its results JSON are Research's committed instruments (Research §0, §7). This document ran no probes. §0 uses "this stage" correctly to mean Design (*"One recon fact this stage adds"*), which makes the other five uses actively misleading. It matters because §1 lists the probes among the *grounds* for adopting the architecture, implying Design added confirming evidence it did not add. **Fix:** replace with "Research's live probes" / "Stage 1's probe harness" throughout, and re-check §1's ground 1 count of "five instances" against Research P3's list once the attribution is right.

### P1-4. §5 names as the pre-rebuild reference set three transcripts that are not in the repository, and names a different missing artifact as the gap.

§5: *"**Baselines:** the three 2026-08-05 baseline transcripts plus this stage's Yausep/Papnoute probe transcripts are the pre-rebuild reference set; `mark_voice_simulation_results.json` remains uncommitted (named gap) — the Decision Log quotes stay its only record."*

The brief said the same thing about the transcripts, in §8: *"transcripts referenced in the Decision Log entry in §3, **not currently committed to this repository** — only a session-scratchpad copy exists; **commit a durable copy before this thread starts**."* I searched: no baseline transcript files exist anywhere in `cic-poc/backend`. The brief's precondition was never met, and the design designates the missing artifact as its baseline while flagging a *different* missing artifact (the 2026-08-05 pilot results) as the gap. Half the verification design's pre-rebuild reference set cannot be read. **Fix:** name both gaps, and either make committing the baselines a Blueprint precondition or re-baseline against Research's committed probe transcripts alone and say so.

### P1-5. The Facilitator contrast-phrase fix — a required brief §7 Part A output and a safety-UX cue — appears nowhere.

Brief §7 Part A's third bullet: *"**Facilitator's three 'distinct from period diction' occurrences** (`app/prompts/facilitator_prompts.py`, Acute Distress/Harmful Dynamic prompts, roughly lines 429/449/485) — fixed last… **This is a real safety-UX cue** (helps a participant register mid-conversation that the Facilitator, not the Representative, has broken in) — **don't just delete it, replace it with something still true.**"*

Grep of the design for "Facilitator": one hit, `facilitator_prompts.py:228`, in the over_settling row. The fix is not designed, not deferred to Build, and not among §7's list of what the design does not decide. It is also the one item whose *content* depends on this rebuild's outcome — the contrast phrase describes the voice being replaced, so it becomes false the moment the rebuild lands. **Fix:** add it, at minimum as a Blueprint task in §7 with the dependency ("after all six worlds settle") stated.

### P1-6. §5 and §6 design a per-world checkpoint and a sustained-disagreement probe from scratch without reference to the per-world blind two-trial batteries already in `scripts/`.

The repo carries `scripts/freeze_battery.py` (blind, two-trial, per-world), `scripts/freeze_battery_probes/{alx,desert,hal,ijc,pahc,syr}.py` with per-world 8-turn `TRIAL_A_SUSTAINED` / `TRIAL_B_SUSTAINED` scripts under a `"sustained-engagement"` category, `scripts/freeze_battery_standards/*.yaml`, `scripts/s56_sustained_rerun.py`, and `scripts/s46_pushback_battery.py` — the last being *"the pushback battery (blind, two-trial)… grounded challenges (claim supported by the record -> held…), ungrounded/thin-area challenges (-> plain concession), bare 'are you sure?' on both kinds; blind-graded, two trials; **held-position and concession rates computed**."*

Research was narrowly right that no *sustained* disagreement probe exists (s46 is two-turn). But §5's proposed instrument reinvents s46's scoring apparatus, and §5's per-world checkpoint — which explicitly names *"the Framework's confidence-under-thinness and **Sustained Engagement** categories"* — is what `freeze_battery` + its per-world probe modules and standards already run. Neither is mentioned. The brief's own Part Eight requirement is *"instruments by name, not prose aspiration."* **Fix:** name the existing batteries, state what s46 extends to (turns 3–6, escalation ladder, per-turn rather than terminal classification), and reuse the per-world standards YAML rather than inventing a second pass bar.

### P1-7. §6's Part Five list omits two of the four additions the brief explicitly requires.

Brief §7 Part B: *"add **the pattern-repertoire concept, the bridge-first instinct**, the Ecological Function/`Formation Ecology Connection` instruction, and the worked-example requirement — still real, needed additions, alongside whatever it takes to actually connect the gate to voice."*

§6's Part Five list adds: record-and-assembly requirement; demonstration requirement; redundancy rule; readability wiring; insight-field authoring standard. The **pattern repertoire** and **bridge-first entry** are absent — both are in §2's shared block, but §6 is the deliverable that makes world #7 inherit them, which is Objective 5's entire point. The EF/FEC item has also mutated: the brief asks for the *lead-with-insight instruction*; §6 carries only the *voice-safe form standard*, which is the leak fix, not the instruction. **Fix:** add both missing items and restore the lead-with-insight instruction alongside the form standard.

### P1-8. "No app-code migration is required" is true of file reading only; several per-world voice constants live in app code outside the record layer.

§1: *"(`main.py:156` unchanged — **no app-code migration is required for this rebuild**)."*

The file-reading claim is exactly right and I verified it. But under "records become what humans write; prompts become what the build system emits," these per-world voice constants remain in `app/` with no record source: `HARD_CEILING_WORLDS` and `RETRY_TRIGGER_MULTIPLES` (`nodes.py:1617`, duplicating `voice_profile.native_measure` — P0-4); `confirmed_glosses.py`'s per-world whitelists (which §3 makes a drop-candidate without saying where the strings would live if kept); the IJC-scoped post-history extension (`nodes.py:1174-1180`, which §2 Layer 4 says "IJC's stays" without saying whether it becomes a record); and `_migrated_world_ids()` as the gate on whether a world gets a post-history guard at all. **Fix:** narrow the claim to "no change to the runtime's file-read surface," and add a short list of the per-world constants that must either move into records or be declared deliberate code-side exceptions.

### P1-9. §8's "demonstrations are eviction-first" claims a token saving from a mechanism with no runtime consumer.

§8: *"Fewer tokens per turn in steady state: **demonstrations are eviction-first**; style prose stated once + demonstrated instead of restated…"*

`eviction_priority` appears only in `wrs/views/segments/*.py`, `wrs/views/permanent_prompt.py`'s manifest, and `wrs/migrate/s23_new_authoring.py`. Nothing in `app/` reads it; there is no token-pressure eviction path in the runtime. It is manifest metadata describing an intended policy. Compounding it: the demonstrations segment is `cache_stability: "static"` and sits inside the cached prefix, which `build_representative_prompt`'s docstring says is *"byte-identical on every turn… billed and processed at full cost only once per cache window"* — so per-turn steady-state token cost is where this claim has the least purchase anyway. **Fix:** state it as a designed property with the eviction executor named as a Blueprint task, or drop the bullet; the other three §8 bullets (cache contract, measured downgrades, world #7) are sound and don't need it.

---

## P2 — polish

1. **`§4.1` is overloaded and unlabelled.** It refers to the *brief's* §4.1 in §2 Layer 1 (second use) and in §3's `citation_grounding` row (*"which the transparency goal (§4.1) needs"*), and to *this document's* §4 item 1 in §4, §7 and §9. §4 has no numbered subsections at all — `§4.1`/`§4.2`/`§4.3` resolve only by list position. Of 34 `§N` pointers, all resolve to a real section in one document or the other; 5 are ambiguous between the two and 2 of those are unlabelled.
2. **`repair_classifier` is three-way, not two.** §2 says the disagreement license mirrors *"repair_classifier's existing HOLD/CONCEDE routing so prompt and adjudicator agree."* The classifier's own header (`repair_classifier.py:17-22`) routes SUPPORTED → HOLD, UNSUPPORTED → CONCEDE, **UNCERTAIN → no directive at all**. The prompt-side license needs the third branch, or it will not agree with the adjudicator in exactly the case the classifier singles out as the dangerous one.
3. **§9 item 10's "story serialization keeps Usage Guidance" appears in no section it cites.** It is absent from §2 Layer 2 and §5. It is also a restatement of existing behaviour with a documented reason (`story_indexer.py:93-97`), not a design decision — and see P0-5 for the 20 files where that section is itself contaminated.
4. **§9 item 4 mis-points.** It puts the prompt-side filter language in "§2 Layer 5"; it is in the shared-`_HOW_YOU_ENGAGE` paragraph, which is a separate block from Layer 5.
5. **The per-world measure descriptors are loose paraphrases.** "Yausep's stages" — his ceiling is *"two or three short paragraphs at the very most"* (`syr_…Yausep.txt:43`); stages are his reasoning mode. "Albina's letter-measure" and "Chloe's household measure" are neither the files' nor the records' own words. Since §2 is deciding where the measure lives, quote the measures.
6. **§2 Layer 4 understates its own change.** *"the guard text becomes an assembly export per world (it already is for Desert)"* — `guards.POST_HISTORY_GUARD` is Desert-authored and is currently applied to **every** migrated world (`nodes.py:1152-1163`). Going to six per-world guards is a real change, not formalization of an existing state.
7. **§3's drift row mislabels the correction.** *"the 20-calls reading was a review-caught error"* — what the reviews corrected was the *signal-type count* (ten/seventeen → twenty; FLAG-016 in `wrs/parameters.yaml`), and separately the brief's own "not twenty separate calls" clarification. Two different corrections compressed into one.
8. **§5's Objective-3 instrument assumes a second reader.** *"two independent reads, with disagreements adjudicated rather than averaged"* — on a single-operator project this is a resourcing commitment, not a design detail. Say who, or say what happens with one reader.
9. **§0 mischaracterises `segments/_common.py:voice`.** Called *"an apparatus-stripping serialization helper"*; it is a field-render helper that matches parenthesised `(Doc|LiveTest|SS|Article|app/|representative_…)` only, runs at assembly not serialization, and strips no square brackets. The distinction is load-bearing given P0-1's bracketed apparatus in PAHC's and IJC's demonstration dialogues.
10. **§6 is 124 words** for the brief's Objective 5 / Part B — "not optional scope; it's the actual point of doing this on a dedicated thread." The thinnest section against the least-negotiable mandate.

---

## What verified clean

Listed because it is most of the document and it is genuinely good work.

- **Determinism and assembly identity.** `permanent_prompt.py` regenerates the committed staging file byte-identical, and that file is byte-identical to the deployed Desert prompt. §1's "same records → byte-identical output" and its proposed assembly-identity check both already hold for Desert.
- **Every §0 recon count.** Desert 6 demonstrations, the other five 4 each. All six worlds carry `voice_profile` + `world_core` + `demonstration`. `{{random_user}}` dialogue form (5 of 6; IJC declared fragment — P0-1). `trait_scores` judged against the world's own `voice_profile` `trait_rubric` — I matched Desert's five traits and Alexandria's five against their rubrics, exactly.
- **The `voice_profile` structure claim.** SPEAKING-model `speaking_model` block plus situation-conditioned trait intensities — precisely as described.
- **The S52 selection rule as written in code**, the eviction/cache metadata, the static → session → turn `ASSEMBLY_ORDER`, and the post-history guard export.
- **`main.py:156`** is exactly the permanent-prompt read line; the runtime read-surface claim holds.
- **Layer 5(a) and (b)'s code facts.** `truncate_at` fail-open at `sections.py:159-160`; `_VOICE_UNSAFE_SECTIONS` at `story_indexer.py:98` with exactly two entries, so the one-line addition really does close 6 of the 8 known Final-Assembly files.
- **The retrieval-ordering addendum.** `doc.metadata["tier"]` at `indexer.py:227`; the sort hook is genuinely before the per-document loop at `retriever.py:192`.
- **§3's governance evidence.** `facilitator_prompts.py`'s screen prompt carries *"it was first tried as one signal among ten in a general drift monitor and caught nothing"* and *"Flagging something that turns out to be well-founded costs one cheap second look"* — both verbatim, both exactly as §3 uses them.
- **§8's cache claim.** `build_representative_prompt` really does return three segments with two cacheable breakpoints, and nothing in the design disturbs it.
- **Every reused Research number**, listed in the Bottom Line above.
- **Completeness against brief §9.2's Design mandate, counted both directions.** (a) shared-file approach confirmed/revised — delivered (§2). (b) per-world pattern for each of six — delivered (§4, all six present, risk-ordered per brief §7). (c) both tracks explicit — delivered. (d) keep/simplify/replace/drop for all four named governance mechanisms — delivered (§3, five rows covering four mechanisms, each with reasoning, two with pre-committed decision rules). **All ten of Research §8's questions answered in §9, and each answer traceable to the section named**, with the two exceptions at P2-3 and P2-4.
- **Balance ratio: 12.3% framing / 87.7% design.** The "excellent re-diagnosis with a thin design attached" failure does not recur.

---

## Why this round found what it found

The Research round's targeted re-check closed with a distinction worth restating, because this document reproduces it exactly: *"new prose describing what a script does is unsafe unless you re-read the script after rewriting it."*

Every P0 here is that class. §0 says its recon was "verified directly before designing on it," and for the parts that are counts and structures — how many demonstration records, what fields a `voice_profile` carries, whether the assembler is deterministic — it plainly was, and all of them hold. The failures are uniformly in the parts that were read as *descriptions of behaviour*: a module docstring saying demonstrations are "rubric-selected" (they are not, on five of six worlds); a docstring saying the capsule is folded in (its own segment says the opposite); a brief clause about capsule prose style (transposed onto chunk files); a Research correction about prompt-file ceilings (transposed onto the record layer, while a code-level ceiling for all six worlds went unseen).

The cheapest guard against the next round of this is mechanical and the document is unusually well positioned for it: this architecture is executable. `_selected()` can be run against all six worlds in ten lines. The gate's failing set can be re-partitioned against the remediation set from a committed JSON. `grep HARD_CEILING` finds the ceiling. Three of the six P0s would have been caught by running the thing the sentence describes, once.

---

## Recommended fix list, in order

1. **P0-1** — per-world demonstration table; rewrite §1 ground 3; add schema-normalisation and selector rank-key as named Blueprint tasks. *(Largest downstream effect: it re-sizes the Blueprint.)*
2. **P0-4** — turn-measure decision redone against `HARD_CEILING_WORLDS` and the six `native_measure` fields; add the ceiling to Layer 5, §5 and §8. *(Second largest: it changes a decision §9 reports as closed.)*
3. **P0-6** — move the chunk-authoring license to §7 as a Mark decision. *(Cheapest to fix, largest scope risk if left.)*
4. **P0-5** — reconcile gate scope with remediation scope; add Desert's 9 uncovered files to §4.4.
5. **P0-3** — correct §8's merged-capsule claim; give the capsule its own design paragraph.
6. **P0-2** — six not one; rewrite §4.4's approach to the brief's own instruction.
7. **P1-3, P1-4, P1-5** — provenance, baselines, Facilitator. All small, all mechanical.
8. **P1-1, P1-2** — soften two rationales to what the evidence carries. No decision changes.
9. **P1-6, P1-7, P1-8, P1-9** — existing instruments, Part Five's missing two, the app-code caveat, the eviction bullet.
10. **P2s** as an editing pass, with the `§4.1` disambiguation done by grep.

**Then re-check.** Per the brief's own standing rule: fixes 1, 3, 4 and 5 all require asserting *replacement facts about what code and records do*, which is the exact class this round found failing. A targeted re-check of those four hunks — run against the code, not read against the commit message — is proportionate. A full round is not.
