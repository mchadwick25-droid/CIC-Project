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

---

# Addendum — targeted re-check of the fix pass (commit `937cc51`), 2026-08-08

*Opus targeted re-check, per the Standard Practice's point 4 and this round's own closing instruction. Scope: `937cc51` ("Apply Design Round 1 adversarial findings…"), which claims all 6 P0s and 9 P1s. Aimed at the three failure classes this thread has proven: replacement facts in fix prose that carry new errors; a correction applied at one site while another site still carries the falsified claim; and reorganizations that change scope-reach.*

*Verification method. Every replacement fact executed or opened at source, not read against the commit message. `HARD_CEILING_WORLDS`/`RETRY_TRIGGER_MULTIPLES` read whole at `nodes.py:1617-1651` including all six per-world freeze comments. All six `wrs/records/*/voice_profile/*.md` read at `native_measure` (`typical_words` **and** the provenance note). The six Desert demonstration dialogues parsed and the Representative's turns word-counted independently. `leak_audit_apparatus_hits.json` re-partitioned from scratch. `world_ground.py` and `capsule_prompt_views.py` docstrings re-read; `wrs/views/` enumerated for capsule emitters and `wrs/views/staging/` for their outputs. `scripts/` and `wrs/gates/` enumerated for the named batteries. `facilitator_prompts.py` grepped for the three contrast phrases. All four §1 code-side per-world configs opened at their definitions. The whole document grepped for each of Round 1's falsified claims.*

## Bottom line

**Not ready. Blueprint must not sequence §2's turn-measure part (3), §4.3, or §1's capsule effort estimate as written.**

This is a real fix pass, not a cosmetic one — 4 of 6 P0s are substantially closed and all 9 P1s were attempted. But three replacement facts are new errors, one of them a live production-regression instruction, and one falsified claim survives verbatim at an uncorrected site.

**3 new P0. 6 new P1. 4 new P2.**

### Round 1 disposition, per finding

| Finding | Landed? |
|---|---|
| P0-1 demonstration mechanism | **Yes**, at every site. §0 rewritten with all four defects, §1 ground 3 rewritten, §2 Layer 2 hardened, §4.4 rebuilt. All four defects independently re-verified: IJC 0 `trait_scores` in all four records; `"weak"` absent fleet-wide; three worlds (HAL/SYR/PAHC) in `PASS`-vocabulary; PAHC's six scores all `PASS (predecessor evidence)` with `[predecessor validation persona…]` inline. *Residue: the selector rank key (P0-1's fifth problem) is still unspecified — see R2-P1-6.* |
| P0-2 Papnoute six-not-one | **Yes.** Counted the six dialogues myself: 146 / 164 / 168 / 218 / 205 / 311 Representative-turn words against `typical_words: 60`. §4.4's "all six… by 2–5× (146–311 words)" reproduces; "codify, not change" is gone from the document; the brief's own sentence is quoted. |
| P0-3 capsule | **Partly — and the replacement fact is inverted.** §8's "already merged" is correctly gone. But see R2-P0-2, and the capsule design paragraph Round 1 asked for was never written (R2-P1-4). |
| P0-4 turn measure | **Partly — three new errors.** Rationale correctly rebuilt around `HARD_CEILING_WORLDS`; Theon 140 / Marius 120 / Desert 60 all verified correct. But see R2-P0-1, R2-P0-3, R2-P1-1, R2-P1-3, R2-P1-5. |
| P0-5 gate scope | **Yes.** Re-partitioned the committed JSON from scratch: 104 flagged, **23** with no hit in EF/FEC/Final Assembly (World Meaning 14, Plural-Voices 3, Distortion Risk 2, Confidence 2, Related-Terms 2; Desert 9, ALX 6, IJC 4, PAHC 2, SYR 2), **20** Usage Guidance (PAHC 8, IJC 6, ALX 3, Desert 3), and the two sets are **disjoint** — so the tiering arithmetic (61 hard-fail / 43 report-only) is sound and "~23" is exact. |
| P0-6 insight-field license | **Yes — cleanly, and it is the best-executed fix in the pass.** Escalated to §7 as a named pre-Build Mark call, the brief's capsule-only limit stated, a serialization-side fallback given, §6 made contingent, §9 item 4 updated, and "the design does not proceed on the unlicensed reading" stated plainly. |
| P1-1 … P1-5, P1-7, P1-8, P1-9 | **Yes.** Stage attributions: all five misattributions gone, the one correct use of "this stage" (§0) retained. Facilitator: three occurrences confirmed at `facilitator_prompts.py:429/449/485`. §1's four code-side configs all verified real — `HARD_CEILING_WORLDS` (`nodes.py:1617`), `app/prompts/confirmed_glosses.py`'s per-world lists, the IJC guard extension (`nodes.py:1174-1181`), and `_migrated_world_ids` (`repair_classifier.py:157`, docstring: *"Worlds with a world_core record - the compatibility gate"*). |
| P1-6 existing batteries | **Yes in substance, no in the citation** — see R2-P1-2. |
| P2 ×10 | **5 applied or moot, 5 not.** Applied: P2-5 (the loose measure descriptors are gone with the rewrite), P2-3 and P2-4 (now resolvable, since §2 Layer 5 discusses Usage Guidance and §9 item 4 names `_HOW_YOU_ENGAGE`), P2-10 (§6 124 → 171 words with both missing items), P2-9 partly. **Not applied: P2-1** (`§4.1` still ambiguous at three sites), **P2-2**, **P2-6**, **P2-7**, **P2-8**. Four of those five are fair to skip as polish. P2-2 is not — see R2-P2-2. |

---

## New P0

### R2-P0-1. §2's turn-measure part (3) — "`HARD_CEILING_WORLDS` becomes assembly-fed from `native_measure`" — conflates a ceiling with a typical measure. Executed against the code's own freeze comments, it would cut five of six worlds' ceilings by 30–60% and put PAHC and IJC into regenerate-on-nearly-every-turn.

§2: *"(3) `HARD_CEILING_WORLDS`'s hardcoded dict becomes assembly-fed from `native_measure` (a Blueprint item), so the record layer is the single source for **the same number** the runtime enforces — ending the drift risk between a record's measure and **the dict's copy of it**."*

They are not the same number and the dict is not a copy. `native_measure.typical_words` is a **mean**; each ceiling was deliberately set at or above that world's measured **max**, or as a deliberate enforcing pull, and the code says so in each world's own freeze comment:

| World | ceiling | `typical_words` | the code's own stated basis |
|---|---|---|---|
| Desert | 60 | 60 | the ceiling *is* the record's number (the one world where they match) |
| Hieronymian | 160 | 94 | *"160 = just above the voice profile's measured solo max (range 41-157, mean 94) **so the solo register never triggers**"* |
| Alexandria | 160 | 140 | *"160 = this record's own measured max"* (record: 123/138/166/136) |
| Syriac | 165 | 98 | *"165 = the voice profile's measured max (range 41-165) so the solo register never triggers"* |
| PAHC | 150 | 70 | *"an **ENFORCING** ceiling… the battery measured 246-272w mean against pahcvoice001's DESIGNED 70w typical and the prompt's own two-short-paragraphs stop (~150w)"* |
| IJC | 180 | 120 | *"a MODERATE enforcing ceiling… the battery measured 251-256w mean / 389 max. 180 sits above the fleet band and below the measured mean"* |

Feed `typical_words` in as written and HAL goes 160→94, SYR 165→98, ALX 160→140, PAHC 150→70, IJC 180→120. With `RETRY_TRIGGER_MULTIPLES` at 1.2/1.5 the retry thresholds become 113 / 118 / 168 / 105 / 180 words — against measured means of 94, 98, ~141, 246–272 and 251–256. PAHC and IJC would fire a **full main-response regeneration** on close to every turn; HAL and SYR would fire on exactly the solo turns the freeze decisions were written to protect. The design's own §2 names this hazard one sentence earlier (*"a voice that only ever hits the backstop is regenerating constantly"*) and then instructs the change that causes it.

There is also no field to read: `native_measure` carries `typical_words` and a prose `note` only. The measured max the ceilings actually derive from exists **only inside the note's prose**. "Assembly-fed from `native_measure`" is not implementable as stated.

**Why this blocks.** It is a numbered part of a decision §9 reports as closed, addressed to Blueprint as a named item, touching the live runtime for all six worlds.

**Fix.** Either state the derivation rule (ceiling = the record's measured **max**, which requires adding a `max_words`/`range` field to `native_measure` first — name that as the Blueprint item), or keep the dict and add a build-time **consistency check** (ceiling ≥ measured max) instead of a feed. Do not describe the dict as a copy of `typical_words`.

### R2-P0-2. §0's and §1's replacement fact — "**no world's capsule assembles yet**… genuine new build work" — is false. Six capsule assemblers exist and every one of the six worlds has a staged generated capsule.

§0: *"and **no world's capsule assembles yet**… Capsule assembly is genuine new build work this design owns (§1), not an existing feature to inherit."* §1 ground 3: *"the capsule emitter for all six (**new work — no capsule assembles today**, §0)."*

`wrs/views/` carries six capsule emitters — `capsule_prompt_views.py` (Desert) plus `s62_alx_`, `s62_hal_`, `s62_ijc_`, `s62_pahc_`, `s62_syr_capsule_prompt_views.py` — and `wrs/views/staging/` carries their outputs for all six worlds:

```
alexandria_world/alex_World_Capsule_Core_generated.md
desert_world/desert_World_Capsule_Core_generated.md
hieronymian_world/hal_World_Capsule_Core_generated.md
imperial_juridical_world/ijc_World_Capsule_Core_generated.md
pahc_world/pahc_World_Capsule_Core_generated.md
syriac_world/syr_World_Capsule_Core_generated.md
```

They are `DELIBERATELY TEMPORARY` in exactly the sense the prompt-side S2.8 assemblers are — same docstring, same S5.2 successor, same "assembles from record FIELDS only." That is precisely the state §0 correctly describes for the **prompt** side ("five worlds' records waiting on `DELIBERATELY TEMPORARY` assemblers"). The capsule side is in the same place, not zero.

This is Round 1's P0-1 error with the sign flipped: Round 1 caught an effort claim that was too optimistic ("a generalization, not an invention"); the fix over-corrected the capsule half into an effort claim that is too pessimistic, and it is the claim Blueprint sizes six worlds' capsule work from. The two true statements are (a) no capsule is **deployed** from assembly — `permanent_prompt.py` writes two prompt-side files only — and (b) `capsule_prompt_views.py` records that hand-authored capsule prose **will not round-trip**, which is the real difficulty and is a *fidelity* problem, not an *absence* problem. Both are already in §0's next clause and both verified verbatim; the "no capsule assembles" sentence is the only wrong part.

**Fix.** Replace with: six temporary capsule assemblers exist and emit staged capsules for all six worlds; none is deployed; the S5.2-class real assembly and the non-round-tripping hand-authored prose are the actual work.

### R2-P0-3. The falsified turn-ceiling claim survives verbatim at an uncorrected site: §4.3 still says Theon has no per-turn ceiling, contradicting the amended §2 three paragraphs earlier.

§4.3: *"**Theon (Alexandria).** **No per-turn ceiling today** and the shared default becomes load-bearing…"*

§2, amended: *"`HARD_CEILING_WORLDS`… is a live per-world word ceiling with regenerate-on-overage **for all six worlds**."* `nodes.py:1619` carries `"alexandria-catechetical": 160` with `RETRY_TRIGGER_MULTIPLES` 1.2, and `alexvoice001.md`'s own note records the configuring decision: *"A ceiling WAS configured at the S6.2 freeze fix session (Mark's mandate, 2026-07-28): HARD_CEILING_WORLDS 160 with retry multiple 1.2."*

The claim is true only of Theon's **prompt file** (which I read — it states no numeric measure), which is exactly the prompt-file→record/runtime transposition Round 1's P0-4 named. The fix corrected the transposition in §2 and left it standing in §4, where it is the first stated fact of a per-world approach Build executes.

**Fix.** "No measure stated in his prompt file today; his runtime ceiling is 160 @1.2 and his record's measure is 140 — the shared prose default and his assembled measure both have to be written against those."

---

## New P1

- **R2-P1-1. "All six carrying a *measured* `native_measure`" (§0) and "each value derived from that world's *measured* `voice_profile` `native_measure`" (§2) are false for half the fleet.** Three of six are measured (HAL 94 from 22 responses; SYR 98 from 19; ALX 140 from the Round-2 retest). Desert's 60 is the *runtime ceiling* recorded as data. **PAHC's 70 is self-labelled "DESIGNED, NOT MEASURED - declared"**; **IJC's 120 is self-labelled "PROVISIONAL PLANNING FIGURE, declared."** Round 1's table carried these provenances; the fix flattened them to "measured." It matters because R2-P0-1's proposed feed would set two worlds' live ceilings from figures their own records disclaim.
- **R2-P1-2. The one instrument path the fix added is wrong, twice.** §5 cites `wrs/gates/freeze_battery.py` (in both the checkpoint bullet and the sustained-disagreement bullet). `wrs/gates/` contains `core.py`, `run_gates.py`, `content_coverage.py`, `fixtures.py` — no battery. The file is **`scripts/freeze_battery.py`**, with `scripts/freeze_battery_probes/{alx,desert,hal,ijc,pahc,syr}.py` and `scripts/freeze_battery_standards/*.yaml`. Round 1 cited it correctly; the fix relocated it. `s46_pushback_battery.py` is cited without a path and is fairly described (its docstring: *"the pushback battery (blind, two-trial)… held-position and concession rates computed"*; two-turn cases, as Round 1 said). Against brief Part Eight's "instruments by name, not prose aspiration," a name that does not resolve is the failure mode.
- **R2-P1-3. §9 item 2 was not updated and now under-reports its own section.** It still reads *"decided: shared default floor stays; per-world measures live in voice_profile records (§2)"* — the pre-fix two-part decision. §2's amended decision has three parts, and the third (the runtime ceiling) is the whole substance of P0-4. The answer table is where Mark and Blueprint read what was decided.
- **R2-P1-4. §8's capsule token-saving still does not follow from §1's own chosen path, and P0-3's requested capsule design paragraph was never written.** §8: *"once the capsule emitter lands (new work, §0) — capsule and prompt stop duplicating world-ground content."* §1 chooses parallel-emit: the capsule files *"stay as the runtime's read surface"* and become build artifacts. A capsule regenerated from records still carries world-ground content and is still concatenated every turn — `world_ground.py` is explicit that the duplication ends at **S6.5's compatibility retirement**, not when an emitter exists. Round 1 asked the design to decide fold-in vs parallel-emit, say what record fields carry capsule content, and say what happens to the prose that will not round-trip. None of the three is anywhere in the document; the decision is still being made by omission, and the token claim is now attached to the wrong milestone.
- **R2-P1-5. Two of P0-4's four fix items were dropped.** `length_ceiling_logging` appears once (§2) and is still **not named in §5**, whose per-world checkpoint lists "turn length" as a measured item — it is the built, per-world, denominatored instrument for exactly that. And **retry cost is still absent from §8 and from §3's 7.5–7.9 invisible-calls arithmetic**, though a ceiling retry is a full main-response regeneration and PAHC — the pilot — carries the one ceiling the code annotates as *"expected elevated retry rate initially."*
- **R2-P1-6. The selector rank key is still unspecified while §2 still mandates the targeted demonstration.** §2 hardens the selector only against the zero case ("a world selecting zero demonstrations fails the build"). `_selected()` remains `sorted(demos)[:cap]`, so a newly authored `syrdemo005`/`alexdemo005` sorts last and is cut by the cap — the design still mandates an artifact its own mechanism will not reliably include. Round 1's fix asked for the rank key by name.

---

## New P2

1. **Three `voice_profile` records assert that no `HARD_CEILING_WORLDS` entry exists for their world when one does** — `syrvoice001` ("NO… entry exists for syriac-edessa-nisibis"; 165 exists), `pahcvoice001` ("NO… entry exists"; 150 exists), `ijcvoice001` ("no HARD_CEILING_WORLDS entry exists for ijc"; 180 exists). `alexvoice001` contradicts itself within one note. Not the design's error, but the design now rests "the record layer is the single source" on fields whose own notes are stale about the runtime — worth a named Blueprint cleanup, and it is the concrete argument for the consistency-check option in R2-P0-1.
2. **P2-2 (the `repair_classifier` third branch) is no longer polish.** §5 now makes the classifier's adjudication rule the *scorer* for the sustained-disagreement probe ("the repair_classifier's own adjudication rule reused as the scorer") while §2 still describes it as HOLD/CONCEDE. It routes SUPPORTED→HOLD, UNSUPPORTED→CONCEDE, **UNCERTAIN→no directive**. A three-way classifier used as a two-way pass/fail scorer will mis-score exactly the turns the classifier singles out as dangerous.
3. **P2-1, P2-6, P2-7, P2-8 unapplied.** `§4.1` is still ambiguous at three sites (§2 Layer 1's "this is what §4.1 protects" and §3's "the transparency goal (§4.1)" mean the brief's; §7 and §9 item 1 mean this document's §4 item 1, which still has no numbered subsections). Fair as polish, but P2-1 was a grep-sized job.
4. **Two small imprecisions in fix prose.** "overrun… by 2–5×" understates the top of its own range (311/60 = 5.2×; the parenthetical numbers make it checkable, so this is cosmetic). And §0 still calls `segments/_common.py:voice` "the serialization helper" — it is a field-render helper that runs at assembly and matches parenthesised apparatus only, which is the very reason it misses PAHC's square brackets in the sentence that cites it.

---

## What the fix pass got right, verified

- **Every countable replacement fact re-derived independently and matched**: the six Desert word counts (146/164/168/218/205/311 vs a 60-word measure); the 23-file uncovered set and its per-section and per-world breakdown; the 20 Usage Guidance files and their disjointness from the 23; IJC's zero `trait_scores`; `"weak"` absent fleet-wide; the three-world `PASS`-vocabulary split; PAHC's predecessor-persona scores and bracketed apparatus; Theon 140 / Marius 120 / Desert 60; the three Facilitator contrast phrases at 429/449/485; all four §1 code-side per-world configs; `readability_check` at `wrs/gates/core.py:211`; `declining_initiative` genuinely absent from the codebase.
- **Both capsule quotations are verbatim and correctly used** — `world_ground.py`'s *"the full fold-in lands at S6.5's compatibility retirement"* and `capsule_prompt_views.py`'s *"Hand-authored capsule prose will not round-trip."* The error at R2-P0-2 is in the sentence around them, not in them.
- **P0-6 is a model of how to close a finding of that class**: the license claim removed at all three sites (Layer 5, §6, §9 item 4), the brief's actual limit stated, the decision moved to §7 as a pre-Build gate, a fallback designed so the escalation cannot stall Build, and the refusal to proceed stated in the document's own voice.
- **No scope-reach regression found.** The Layer-5 re-tiering narrows what hard-fails but names the residue and its size, and the escalation in Layer 5(c) narrows the authoring pass to two named fields contingent on Mark — both moves shrink reach honestly rather than quietly.

## Recommended fix list

1. **R2-P0-1** — rewrite §2 part (3) as a derivation rule against the measured max (with the record field that must exist) or as a build-time consistency check. *Only item that touches live runtime behaviour.*
2. **R2-P0-3** — §4.3's first clause. One sentence.
3. **R2-P0-2** — §0 and §1's capsule sentences: six temporary emitters, none deployed, non-round-tripping prose is the real work.
4. **R2-P1-4** — write the capsule design paragraph P0-3 asked for and re-point §8's bullet at S6.5 retirement, or drop the bullet.
5. **R2-P1-1, R2-P1-2, R2-P1-3, R2-P1-5, R2-P1-6** — provenance wording, the `freeze_battery` path (×2), §9 item 2, `length_ceiling_logging` in §5 + retry cost in §8, the selector rank key. All mechanical.
6. **R2-P2-2** then the rest of the P2s as one editing pass.

**Then send.** Every item above is a sentence-level correction against a fact now established in this file; none re-opens a design decision except R2-P0-1, which re-opens one clause of one. A third adversarial round is not proportionate — a verification that these ten hunks say what the sources say is.

---

# Final addendum — verification of the second fix pass (commit `aacaac8`), 2026-08-08

*Opus final verification, narrow scope: does `aacaac8` land the re-check addendum's 3 P0s / 6 P1s / 4 P2s plus Round 1's unapplied P2s, are its replacement facts true, and does the document now hang together. Method unchanged: every replacement fact executed or opened at source. `probe_parity.py` read whole and all six `*_probe_parity_result.json` verdicts re-tallied. `wrs/views/` re-enumerated for capsule emitters, `staging/` for their outputs. `nodes.py:1617-1651` and `repair_classifier.py:157` re-read. `alexvoice001` re-read at `native_measure`. The whole document re-grepped for each corrected claim.*

## Bottom line

**Not ready — but one editing pass from it, and no design decision re-opens.**

Twelve of the fifteen findings landed cleanly, several of them well. What remains is one class only, and it is this thread's signature failure: **a claim corrected at the site it was flagged and left standing at the other sites, now contradicting its own correction.** Two claims, four sites. Plus one new attribution that isn't true.

**2 P0. 2 P1. 3 P2.** Every one is a sentence deletion or a sentence rewrite against a fact already established in this file.

### What landed, verified

- **`ceiling_words` (R2-P0-1) — closed, and the design is right.** The diagnosis is correct (`typical_words` is a mean; the ceilings were set at or above measured max), the collapse figures are mine and reproduce (HAL 160→94, SYR 165→98), the remedy is a new field rather than a feed, and **migration seeding `ceiling_words` with the current dict values means the change is behaviour-neutral at landing** while carrying each freeze rationale into the record. That is a better answer than either option I offered.
- **§4.3 Theon (R2-P0-3) — closed.** *"No prose ceiling in his file (the runtime already backstops him at 160 words, `HARD_CEILING_WORLDS`)"* — 160 verified at `nodes.py:1619`, and it is now consistent with §2.
- **`native_measure` provenance (R2-P1-1) — closed at §0**, quoting the records verbatim: PAHC *"DESIGNED, NOT MEASURED"*, IJC *"PROVISIONAL PLANNING FIGURE"*, Desert's = the runtime ceiling. (Not at §2 — see F1.)
- **`scripts/freeze_battery.py` (R2-P1-2) — closed at both sites.**
- **§9 item 2 (R2-P1-3) — closed.** All three parts now reported, including the record-fed backstop.
- **`length_ceiling_logging` (R2-P1-5, instrument half) — closed, and better than asked**: §5's checkpoint now reports ceiling regeneration events as *"a full extra main-response call, a real cost line."*
- **Selector rank key (R2-P1-6) — closed.** Deterministic key (strong-score count desc, then id) plus a `required` flag that guarantees the targeted demonstration's selection — which is what makes §2's "one targeted demonstration per world" mandate actually deliverable.
- **R2-P2-2 — closed at both sites.** The UNCERTAIN branch now appears in the `_HOW_YOU_ENGAGE` license *and* in §5's scorer (*"UNCERTAIN turns route to the human read, never auto-scored"*), matching `repair_classifier`'s actual three-way routing.
- **Round 1's P2-6, P2-7, P2-8 — closed.** Layer 4 now states the real change (one Desert-authored guard applies to every migrated world today → six per-world exports, *"Build work, not formalization"*) — verified at `nodes.py:1152-1163`. The drift row now separates the two corrections. §5's Objective-3 read is stated honestly for a single operator.
- **The precision sweep — closed.** 2.4–5.2× with all six counts (matches my own parse exactly), and `segments/_common.py:voice` correctly described as a field-render helper matching parenthesised citations at assembly time.
- **The capsule design paragraph (R2-P1-4, structural half) — written, and its architecture is coherent.** "S6.5 fold-in as target, parallel-emit as transition" checks out against both modules: `world_ground.py` already declares the fold-in for S6.5's compatibility retirement, so the design adopts an existing planned end-state rather than inventing one; and the round-trip argument is sound — `capsule_prompt_views.py`'s failure is specifically about *hand-authored* prose, so a capsule emitted from records that Build authored has nothing left to round-trip. This is a real decision, made explicitly, where Round 1 found decision-by-omission.

---

## What still blocks

### F1 (P0). §2's turn-measure paragraph now contradicts itself. Its opening sentence still carries the falsified claim; its part (3) — three sentences later — refutes it.

Opening, unchanged: *"`HARD_CEILING_WORLDS`… is a live per-world word ceiling with regenerate-on-overage for all six worlds, **each value derived from that world's measured `voice_profile` `native_measure`** (all six records carry one — Theon 140, Marius 120, Desert 60…)."*

Part (3), new: *"…because **the existing `typical_words` is a mean, not a ceiling**, and feeding it directly would collapse ceilings to typical output (HAL 160→94, SYR 165→98)."*

Both cannot be true. If each dict value were derived from `native_measure`, feeding `native_measure` in could not change any of them. The correction was applied at §0 (provenance) and in part (3) (the mechanism) and left standing in the sentence that introduces the whole decision — the most-read sentence of the most-revised paragraph in the document. As written it also re-asserts the "measured" flattening R2-P1-1 corrected everywhere else.

**Fix.** *"…for all six worlds, each value set at that world's own freeze against its measured range — at or above the measured max, or as a deliberate enforcing pull (PAHC, IJC) — never equal to its `typical_words` (Theon's record measure is 140 against a 160 ceiling; Marius's 120 against 180; only Desert's 60 coincides)."*

### F2 (P0). "No capsule assembles today — new work" survives verbatim at §1 ground 3 and §8, contradicting the two paragraphs rewritten to correct it.

§1 ground 3, unchanged: *"the capsule emitter for all six (**new work — no capsule assembles today, §0**)."*
§8, unchanged: *"— once **the capsule emitter lands (new work, §0)** — capsule and prompt stop duplicating world-ground content."*

Both cite `§0` — and §0 now says the opposite, in the document's own voice: *"capsule emitters exist for all six worlds (`capsule_prompt_views.py` + the five `s62_*` variants) and all six have staged `*_World_Capsule_Core_generated.md` output… The capsule work this design owns is therefore **reconciliation, not creation**."* §1's own new capsule paragraph, twenty lines below ground 3, says *"the **existing** capsule emitters regenerate the capsule…"*

Re-verified: six emitters in `wrs/views/`, six staged generated capsules, one per world. §1 ground 3 is the effort-sizing list Blueprint reads; §8 is the cost claim Mark reads. Both are pointers into a section that refutes them.

**Fix.** §1 ground 3: *"capsule reconciliation for all six (emitters exist and emit; their output does not match deployed — §0, and the capsule design paragraph below)."* §8: see F4.

---

## Also

- **F3 (P1). New unverified attribution.** §0: *"…that generated output does not match the hand-authored deployed capsules (… **this mismatch is much of what probe_parity's 4-of-6 FAIL measures**)."* It is not. `probe_parity.py`'s own docstring: *"S2.8 probe-parity (P): **deployed prompt vs. generated prompt** - same voice?"*, and its design note: *"generation: … **system = the prompt text**."* No capsule is read anywhere in the harness. The four FAILs are voice categories from prompt comparison — ALX `scholarly-framework` + `self-referential`, HAL `naming-collision`, IJC `fabrication-tome-courier`, SYR `contested-identity` + `exact-quote` — none capsule-related. Capsule parity is a *separate* instrument: `capsule_prompt_views.py` says *"the S2.8 capsule parity is a **SECTION-level classified comparison**, recorded in the checkpoint artifact."* The 4-of-6 figure itself is right (I re-tallied all six verdicts). Only the causal link is invented — a plausible bridge sentence written to connect the new paragraph to an existing number. **Fix:** delete the parenthetical, or replace with the true instrument ("measured by the S2.8 capsule parity's section-level comparison, not by probe_parity").
- **F4 (P1). §8's token saving is now keyed to a milestone §1 says won't deliver it.** Under the transition §1 chose, parallel-emit, a regenerated capsule still carries world-ground content and is still concatenated on every turn; §1 is explicit that the duplication ends at the **S6.5 fold-in**. So the saving arrives at the fold-in, not "once the capsule emitter lands." **Fix:** *"and — at the S6.5 fold-in (§1's target state, not the transitional parallel-emit) — capsule and prompt stop duplicating world-ground content."* This closes the substance half of R2-P1-4.
- **F5 (P2). Retry cost still absent from §8 and from §3's 7.5–7.9 invisible-calls line.** §5 now reports regeneration events, which is the instrument half and the more important one; the arithmetic half is unchanged, and PAHC — the pilot — carries the one ceiling the code annotates as *"expected elevated retry rate initially."*
- **F6 (P2). Round 1's P2-1 was not applied**, though the commit message claims the unapplied P2s. `§4.1` still means the brief's at §2 Layer 1 and §3's `citation_grounding` row, and this document's §4 item 1 at §7 and §9 item 1. Still a grep-sized job.
- **F7 (P2). Two small things in the new capsule prose.** §0 runs an em-dash straight into a new capitalized sentence (*"…`DELIBERATELY TEMPORARY` assemblers —\nThe capsule side…"*). And §1's *"each world's Build step authors its world-ground content into records (capsule prose style is explicitly in scope per the brief)"* warrants a **content** move with a **style** license; for capsule files the brief does license style, so say re-homing preserves content and only the prose form is rewritten — the same distinction P0-6 was resolved on.

---

## Verdict for the Standing Practice's point 6

**Not ready for Mark's Design-stage sign-off — by two sentences and a parenthetical.**

Stated plainly rather than softened toward approval, because three rounds on this document have all turned on the same thing: this pass fixed the capsule claim in two places and the ceiling claim in two places, and left the older wording standing in four others, where it now reads as the document disagreeing with itself. A reader who starts at §1 ground 3 or §8 or the top of §2's turn-measure paragraph gets the pre-fix picture, and those are the three places Blueprint sizes work and Mark reads cost.

Nothing here re-opens a decision. F1 and F2 are deletions of superseded sentences; F3 is a parenthetical; F4 re-points a milestone the document has already chosen. The design underneath them — record-sourced assembly, the five layers, `ceiling_words`, the tiered gate, the escalated insight-field call, the fold-in-as-target capsule path — has now survived two adversarial passes at source and is, in my judgement, sound and ready to be built from.

**Apply F1–F4, sweep F5–F7, and send it to Mark. No further adversarial round is warranted** — the remaining items are checkable by grepping this file's own quoted strings against the document, which is a verification, not a review.
