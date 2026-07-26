# Report: Retrieval / data-access failures in real CiC conversations

Organized by five areas. Bucket labels used throughout: **(A)** information not available at all · **(B)** available but not surfaced at that moment · **(C)** surfaced but wrong quantity/form · **(D)** pure prompt wording with right data in hand.

---

## 1. Cross-World Roundtable Validation (`CiC-Fable-Experiment:World-Builds/Cross_World_Roundtable_Validation.md`, 505 lines, Parts I–XXII)

Branch confirmed as `CiC-Fable-Experiment`; file read in full via `git show`.

**The honest headline: this document is almost entirely a prompt-wording record, not a retrieval record.** Every fix in Parts I–XVII is a change to Permanent Prompt text (v3→v9 of the subject-of-utterance rule). No part of it touches `retriever.py`, chunk metadata, or Retrieve-When conditions. But three findings inside it are genuinely about data access, and one is explicitly diagnosed as architectural:

**1.1 — Part XVIII (Task 88), Theon's Gregory-of-Nyssa defect. Bucket (A), then explicitly re-diagnosed as a data-organization gap by the document itself.** Theon passed the grammar rule cleanly (v9) while producing three Tier-E claims — the burning-bush "sandals as the soul's dead coverings," "the bush burns and the soul is entered without being consumed," and theosis as "an endless road, no one has claimed its end" — all traceable to Gregory of Nyssa, a Cappadocian, not to any Alexandrian source. It recurred in *both* independently generated transcripts. The root-cause paragraph is the single most important sentence in the file for this question:

> "The underlying cause is architectural, not a wording defect fixable by another prompt patch alone: none of the five worlds' Permanent Prompts currently constrain the Representative to draw specific imagery and claims from an approved, world-correct source list. Generation currently relies on the model's own parametric training knowledge, unconstrained, at the moment of answering"

And the failure mode named precisely (Part XX): "confident, fluent borrowing from a bounded universe of real, well-attested, but *wrong-for-this-world* sources — a failure mode a bounded, checkable list can prevent by construction rather than catch by audit."

The fix was a new **data structure**, not a prompt tweak: Doc_02B (`L3B-World-Build-Methodology/Doc_02B_Approved_Source_Database_Template.md`), with a `Licensed-For` field and a `NOT-approved-for` field naming the adjacent tradition's more famous treatment of the same subject. This is the clearest case in the whole corpus of a voice/fidelity failure traced to missing structure in the source data rather than to instruction wording.

**1.2 — Part XIX, the unlocated Origen locus. Bucket (A), still open.** Several of the project's own construction documents (`08_Spiritual_Life_and_Ascent.md`, `World Activation.md`, `alexstory002...`, Theon's Construction Notes) already carry an elaborated burning-bush reading attributed generally to "Origen's homilies and commentaries," which the session "could not confirm to a specific extant locus — a pre-existing internal citation risk, not created by this fix."

**1.3 — Part XXI/XXII, Chloe's Novatian-schism elaboration. Bucket (A)/(C) hybrid.** The reviewer found the answer "elaborated past the prompt's single licensed sentence ('we learned, with fear, one mercy') into an invented tension-and-resolution narrative arc... not actually supported by that sentence or by any named source." The diagnosis names the data-model cause directly: correcting it "likely requires either a tighter version of the existing baked line or **a dedicated Doc_02B entry naming exactly how much the Representative may say about this topic**." That is a granularity/licensing gap in the data, not a wording gap.

**1.4 — Part VI, the "grammar instruction cannot verify truth" finding. Bucket (D)-that-cannot-be-fixed-by-(D).** Confirmed by independent review:

> "a grammar/reasoning instruction can shape how confidently a claim is expressed, but it cannot verify whether the claim is true — the model's sense of 'this feels like documented consensus' is the identical faculty that invented the false claim in the first place... the grammar instruction is a style governor, not a truth gate, and the truth gate has to live outside the generation step."

Concrete instance: Cordus's "we could not tell what we were weeping for" at the baptismal vigil has no primary-source attestation; Augustine's account describes weeping at the hymns afterward, not at the water-rite.

**Everything else in this file — Parts VII–XVII, the entire self-narration/fabrication line — is bucket (D).** The five-world baselines, the v3 regression (quoting a banned phrase made the model produce it), the museum-guide analogy, the pronoun-defense gap, the Theon carve-out — all of it is instruction text against data the Representative already had. Worth stating plainly since it's the bulk of the document.

---

## 2. Per-world Phase 5 / live-test transcripts and scoring

Sources: `World-Builds/{01-Post-Apostolic-House-Church,Alexandria-Catechetical-School,Desert-Monasticism,Hieronymian-Ascetic-Literary,Imperial-Juridical-Christianity,Syriac-Christianity-Edessa-Nisibis}/` plus `CiC_W1_Phase5_RelationalSafety_Retest_Against_Proposed_Mechanism_DRAFT.md`.

### Bucket (A) — the source material had nothing

Every fabrication in this corpus is **a proper noun or a specific scene demanded at a granularity the world only holds "as a shape, not a story."**

- `Desert-Monasticism/LiveTest_Scoring_Review.md`: "**Abba Poemen, given an invented, specific, unattested episode**... Poemen does not appear anywhere in this world's own Doc_09a Story Inventory." Under harder pressure: "Papnoute invented two full, detailed, specific episodes — an elaborate 'Poemen and Anoub' testing-scene, and an invented deathbed scene for a new figure, 'Sisoes'... Neither appears anywhere in Doc_09a." The inventory's real size is named: "Papnoute carries exactly four vetted sayings whole."
- `Imperial-Juridical-Christianity/Step10_Phase5_Boundary_Testing_Record.md`: "four responses reached into real-but-unregistered general historical knowledge (a Gaul mission, service under two popes, letters from Cyril of Alexandria and John Cassian)... none of it traceable to the actual Source Registry" — which "holds only two Leo entries: the Tome, and the Canon-28 rejection letters." Same doc carries the sharpest granularity statement anywhere in the project: "a bare fact (an event this world holds only as a shape, not a story) does not license inventing named participants around it merely because a question asks for vividness."
- `01-Post-Apostolic-House-Church/CiC_W1_Phase5_BoundaryTesting_Independent_Verification_Round1.md`: "**the word 'Christian' does not appear anywhere in either the Permanent Prompt or the Capsule Core.** This is invented content presented as grounded voice."
- Same file, the most consequential (A): "Nothing in the deployed Permanent Prompt or World Capsule Core contains any crisis-detection logic, any bridge to a real-world resource... or any instruction for when to step outside the persona for safety reasons." Desk-fixed in `CiC_W1_Phase5_RelationalSafety_Retest_Against_Proposed_Mechanism_DRAFT.md`, where Amma's own turns are "unchanged from original transcript."

### Bucket (B) — the right material existed and was not reached for

- **The cleanest proof in the corpus** (`Desert-Monasticism/LiveTest_Scoring_Review.md`): Papnoute "invented the *occasion* of Amma Sarah's saying (elders asking why she prayed a particular way) rather than its attested occasion (elders coming to test/humble her about being a woman) — the saying's actual content was rendered accurately elsewhere in the same transcript." Same transcript, right data, wrong turn.
- Same file: "Papnoute attached the leaking-jug story to 'Macarius,' when the story is Abba Moses's own (Doc_09a Story 2.1), and additionally mischaracterized its content." A background-knowledge variant surfaced instead of the vetted chunk.
- Same file: "narrated the Chalcedonian two-natures Christological controversy as something he had personally lived through... its actual documented late dispute is the Origenist controversy over Evagrius's systematized naming of the thoughts." The fix was literally a pointer to the in-horizon material the build already had.
- `Imperial-Juridical-Christianity/Step10_Phase5_Boundary_Testing_Record.md`: a multi-world convention "does not actually exist as instructional text in Marius's, Albina's, or Papnoute's real deployed Permanent Prompts — it lives only in the Construction Framework's own builder guidance and in Alexandria/Theon's build documentation." The transcript's clean behavior was "test-harness-instructed, not artifact-native." Content present in the project, absent from the artifact that had to produce it.

### Bucket (C) — surfaced, but in the wrong form. This is the biggest and most under-recognized cluster.

The dominant cause is **upstream vocabulary already sitting in the approved artifact**, not turn-level drift:

- `Imperial-Juridical-Christianity/Step10_Phase5_Boundary_Testing_Record.md`: Marius "used 'our record,' 'no chancery drafted an account,' 'never reached a letter' language to *explain* thin domains — documentation-hedging dressed in world vocabulary." Two scoring categories failed from this one root.
- `Syriac.../Review-Artifacts/Phase5_LiveTest_Scoring_Review.md`: "'Our own record' / 'the record' phrasing recurs across all three independently-generated scenarios... **Recommend inspecting the assembled Permanent Prompt's own vocabulary for this pattern directly.**"
- `01-Post-Apostolic-House-Church/...Independent_Verification_Round1.md`: "'**nothing survives of you but letters**'... The word 'survives' is a preservation/documentation-register word, and it is baked into the *approved Capsule Core*, not just improvised in this transcript."
- Quantity failures proper: Marius produced "an 8-sentence response averaging ~44 words/sentence, with one 75-word sentence chaining two em-dashes and a semicolon — far outside the Framework's own Flesch-Kincaid grade 8-10 target, **despite good register content**"; after the first fix, "three sentences of 38–49 words each, still chaining em-dashes and colons."
- Mar Yausep, called "the single most consequential finding of this pass": he "went far beyond SF-1's cleared model... into manuscript-transmission narration ('copying hands, generations after...'), a reception-history dispute among later readers, and direct reference to 'the parchment in front of you'" — with the diagnosis "the current instruction is not specific enough to prevent an elaborate excursus when pressed harder."
- Theon (`Alexandria.../Phase5_BoundaryTesting_Scoring.md`): three sentences of self-narration *prefixed* to a correct answer — "the back half recovers... that part is correct world-internal thinness." Right material surfaced; unwanted material in front of it. Notably graded "a tuning gap, not an architectural incapacity."

### Bucket (D) — genuinely prompt-wording only

- Mar Yausep's frame-break Turn 7 "argued back... instead of the required plain non-recognition," while Turn 6 passed with the same content — only rhetorical framing differed.
- Desert: "The soft instruction ('say so plainly... rather than inventing') was not absolute enough to survive direct narrative pressure — a genuine illusory-fix risk." Identical data before and after; only absoluteness changed.

---

## 3. How retrieval actually decides — and whether Retrieve-When conditions can carry the weight

Files read in full: `cic-poc/backend/app/rag/retriever.py`, `story_retriever.py`, `batch_evaluate.py`, plus `indexer.py` and real chunks across six worlds.

### 3.1 The Tier-1 short-circuit is effectively unconditional for three of six worlds

`batch_evaluate.py:42` sets `TIER1_SHORT_CIRCUIT_RANK = 2`; `partition_tier1_short_circuit` auto-retrieves any Tier-1 doc landing in the top 2 semantic hits, **without ever reading its Retrieve-When or Do-Not-Retrieve-When text.** Actual tier distributions (`cic-poc/backend/data/*/lexicon_chunks/`):

| world | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| pahc | 4 | 7 | 2 |
| syriac | 4 | 4 | 2 |
| imperial-juridical | 5 | 5 | 2 |
| **desert** | **9** | 0 | 0 |
| **alexandria** | **45** | 0 | 0 |
| **hieronymian** | **15** | 0 | 0 |

For Desert, Alexandria, and Hieronymian, **every chunk is Tier 1**, so the top-2 semantic matches always auto-retrieve and their conditions are never evaluated at all. Since lexicon `k=3`, that means the LLM vote decides only the third slot. Retrieval for those three worlds is essentially pure vector similarity.

The same all-Tier-1 fact defeats the second mechanism. `evaluate_batch` splits Tier 1 into its own call because "mixed into a 6-candidate batch dominated by peripheral Tier 2/3 terms, the model reverted to uniform literal keyword-matching across the whole batch and the exception was lost." With no Tier 2/3 present, there is nothing to split from — every candidate receives the generous "this representative would still reach for it" instruction.

### 3.2 The one Do-Not-Retrieve-When case the short-circuit honors almost never fires

The guard is `label.lower() in context_lower` — a literal substring test of the chunk's own `Term:` field against the transcript. Term fields are authored differently per world:

- pahc: `episkopos (ἐπίσκοπος)`, desert: `Diakrisis (Discernment)`, syriac: `raza (ܐܪܙܐ) / shrara` → these strings will essentially never appear verbatim in speech, so `already_discussed` never fires.
- alexandria: `Logos`, `Catechesis`, `Illumination`, `Theosis`, `Participation` → these fire constantly.

The guard's behavior is therefore an accident of each world's Term-line formatting, not a design decision. **This is the structural cause of a real live failure**: commit `1252fd4` records "Albina and Papnoute each reached for the same story twice across different topics before being asked for a different one." The story retriever's only de-dup is this same substring test against `story_title` — titles like `Antony's Call — Hearing Matthew 19:21` can never match a transcript. It was fixed with an anti-repetition *prompt clause* on both worlds, leaving the retrieval-layer cause untouched.

The `force_llm_vote` escape hatch exists (`batch_evaluate.py:88`) but is used in exactly **two files project-wide**, both Syriac: `syrlex004_madrasha.md` and `syrlex010_anti-jewish-demonstrations.md`. Zero use in the three all-Tier-1 worlds that need it most.

### 3.3 Are Retrieve-When conditions specific enough? It varies enormously by world, and several are unevaluable by construction.

Best case, Syriac `syrlex002_qyama.md` — genuinely operational, multi-clause, names the confusion risk:
> `Retrieve-When: participant asks about celibacy, asceticism, or vowed life in this world; participant asks how this world's ascetics differ from desert monks; participant uses "monk," "nun," or "monastery" in a way that may import Egyptian-desert assumptions; conversation reaches Aphrahat's Demonstration 6...`

Worst case, Desert (`desertlex005_diakrisis.md`, `desertlex007_cheironaxia.md`) — a topic label, nothing more:
> `Retrieve-When: participant asks how ascetics decided how much fasting/discipline was appropriate, or about discernment generally`
> `Retrieve-When: participant asks about daily life, work, or how ascetics supported themselves`

And five of nine Desert chunks have `Do-Not-Retrieve-When: —` — a literal em-dash, which is non-empty, so it passes the "no conditions" check in `evaluate_batch:118` and is rendered into the prompt as `DO-NOT-RETRIEVE-WHEN: —`. The model is handed an em-dash as a condition.

Three classes of condition **the runtime cannot evaluate at all**:

1. *Cross-world guards.* Desert: `Do-Not-Retrieve-When: discussion concerns a different world's own withdrawal-adjacent practice (do not cross-apply)`. The filter LLM sees only the message and transcript — it has no per-world ownership map.
2. *Capsule-Core state.* Syriac and Alexandria repeatedly use `the World Capsule Core has already surfaced this term's core distinction in the current turn`. The filter call is never shown the Capsule Core. **This phrasing is prescribed by the project's own template** (`L4-Templates/Deployment_Lexicon_Chunk_Template.md`, Do-Not-Retrieve-When example), so it propagates by design.
3. *Representative internal need.* `desert_world/story_chunks/desertstory001...`: `Retrieve-When: ... Representative needs a formation example for gravity 1 (withdrawal) or gravity 7 (practical scriptural engagement).` The classifier runs before generation and has no view of what the Representative "needs."

**Verdict on your question:** for Syriac, Alexandria, Imperial-Juridical, and PAHC the Retrieve-When conditions are specific enough to be meaningful — but for Alexandria they are bypassed on the top 2 slots anyway. For Desert and Hieronymian, retrieval is guessing: the conditions are topic labels, the negative conditions are empty or unevaluable, and every chunk short-circuits. That is not a small subset — Desert is the world with the worst confirmed live fabrication record in the corpus.

### 3.4 One structural mismatch worth naming separately

`1ca09da` documents a case where retrieval worked and the prompt blocked it: Papnoute's Permanent Prompt "explicitly licensed exactly three named scenes to tell as narrative — all Tier 2 sayings... while giving zero narrative voice to any of the world's three Tier-1 stories... the most solidly attested material in the whole world." The story chunks were being retrieved and cited; the prompt's whitelist forbade narrating them. After the fix, "the backing story chunks (desertstory002, desertstory003) correctly retrieved and cited — a marked improvement over the prior behavior, where this material could only be summarized as background fact, never actually told as a scene." **Bucket (B), with the block on the prompt side rather than the retrieval side** — a licensing model in the prompt that was never reconciled against the tier model in the data.

---

## 4. Quantity: how much material actually enters a turn

### 4.1 Retrieval volume has never been tuned — at all

`git log -S "k: int = "` over `cic-poc/backend/app/rag/` returns exactly two commits: `09a59c4` (the original POC scaffold, which set `k=3` lexicon / `k=2` story) and `6c328ff` (which added the short-circuit and left both values alone). **There is no tuning record, no measurement, no live finding about chunk count anywhere in the repo.** The only justification on record is a one-line docstring in `story_retriever.py:76`: "A lower default k than the lexicon retriever — stories are longer and a representative should draw on at most one or two per turn."

This stands in sharp contrast to the generation-length caps, which have an exhaustively documented empirical record (`nodes.py:73–140`): 500→700→900 for reactive, "460 still truncated one sample in five. 500 and 550 both ran clean (0 truncations)," then 550→1200 as your own call; per-world retry multiples 1.5x/1.2x derived from observed distributions ("Papnoute's uncorrected drafts landed around 175-180 words against a 60-word ceiling... Albina's landed consistently at 220-245 against a 180-word ceiling"); lane ceilings "Measured over 45 live turns."

**So: output length is one of the most carefully measured things in the system. Input retrieval volume has never been looked at once.**

### 4.2 The actual volumes, measured

Whole-file lexicon chunk word counts (`cic-poc/backend/data/*/lexicon_chunks/`):

| world | min | mean | max | n |
|---|---|---|---|---|
| pahc | 164 | 479 | 736 | 13 |
| desert | 275 | 314 | 356 | 9 |
| syriac | 232 | 636 | 919 | 10 |
| **alexandria** | **683** | **1,229** | **1,767** | **45** |

For Alexandria, a single turn can inject 3 lexicon chunks averaging 1,229 words plus 2 story chunks — roughly **4,300 words of retrieved context to produce a turn capped at 1,200 tokens (~900 words), against a prompt target of "one to two short paragraphs."** Retrieved input outweighs the licensed output by roughly 5:1, and nothing anywhere caps or trims it.

### 4.3 What is inside those chunks is worse than the word count suggests

`indexer.py:117-118` does `content.split("---", 2)` and takes `parts[2]`. Verified against the real files (`---` at lines 14, 20, 30, 36, 46, 54 in `alexlex001_logos.md`), this has two effects:

**The `## Quick Meaning` section is silently dropped.** It sits between the 1st and 2nd `---`. The template describes it as "the runtime-facing summary of this term... **Does not require the full entry to be surfaced**" — i.e. the data model already contains a lightweight-surfacing tier, and the runtime discards it.

**Everything builder-facing is injected in full.** What actually reaches the Representative under the header "# Context That May Be Relevant / Draw on this naturally if it fits" (`representative_prompts.py:163-168`) includes:

- `## Ecological Function` — e.g. `pahclex004_eucharistia.md`: "This term anchors the Liturgical Practice gravity (G07), which the ecological reconstruction treats as doing the heaviest lifting of any single practice in this world."
- `## Distortion Risk` → `**Modern Hearing:**` — e.g. `alexlex001_logos.md`: "A technical concept from Hellenistic metaphysics that the early church adopted to give Christianity intellectual credibility — one doctrine among many, of interest mainly to specialists."
- `## Key Sources` and `## Related-Terms Reciprocity Note`.

**This closes a loop with the Phase 5 findings.** The Syriac review's own recommendation was to "inspect the assembled Permanent Prompt's own vocabulary" for the recurring "our record"/"the record" register leak. The Permanent Prompt is only half the story: every turn also injects scholarly-register meta-commentary — "the ecological reconstruction," "Modern Hearing," "Key Sources," gravity codes — directly into the generation context. Marius's "documentation-hedging dressed in world vocabulary," Mar Yausep's manuscript-transmission excursus, and Theon's "the kind of record" / "settles your scholars' dispute" leak are all **bucket (C) failures with a live, per-turn, retrieval-side supply of exactly that vocabulary** that the reviews never looked at because they were auditing static artifacts.

### 4.4 One more quantity-adjacent note

For reactive turns, `nodes.py:932-934` sets the retrieval query to `"{participant question}\n\n{OtherRep} just said: {their full turn}"`. The other Representative's entire turn — in *their* world's vocabulary — becomes part of this world's vector query. The comment justifies this for conversational responsiveness, and it is a real improvement on that axis, but it means a reactive turn's retrieval is partly driven by another world's terms. Given `check_cross_world_vocabulary_drift` was later built specifically because "Representatives were adopting each other's terminology" (`bb0698c`, `65dfca9`), the retrieval query construction is a plausible untested contributor that nothing in the record examines.

---

## 5. Tonight's two bugs as data-organization problems

Commit `4697e2b`, "Stop the anachronism bridge from hijacking multi-world rounds, and tighten its word-vs-formula matching," from the live test "what is faith" to a three-world table.

### 5.1 The "faith" over-fire: yes, this is a structural data-modeling gap, and the file proves it

`definitions.json` (`cic-poc/backend/data/modern_term_bridge/definitions.json`, 10 terms) stores exactly these fields per term: `term_id`, `display_terms`, `modern_sense`, `period_originated`, `origin_year`, `contested_today`, `underlying_subject`. **There is no field for the term's distinguishing claim.**

And the classifier is handed only display phrases (`modern_term_bridge.py:123-126`):

```python
lines = [
    f"- {tid}: {'; '.join(d.get('display_terms', [tid]))}"
    for tid, d in definitions.items()
]
```

So the model's entire evidence for `sola-fide` is the string `sola fide; faith alone; justification by faith alone; saved by faith not works` — in which the universal root word "faith" appears four times and the distinguishing feature (faith *excluding works*) appears nowhere as a labelled field. **`modern_sense` — the only place the distinguishing claim is actually written — is never passed to the classifier at all.** It is only ever spoken aloud by the Facilitator after the match has already been made (`stream_modern_term_bridge`, line 196-202).

Tonight's fix added three lines of prose to the shared `_CLASSIFIER_PROMPT`:

```
- A bare question about a universal Christian concept that merely SHARES A WORD with a modern term's name is NOT the same as asking about that term's specific, distinguishing formula...
  - "What is faith?" -> NONE ...
  - "Is it faith alone that saves you, and not anything you do?" -> sola-fide (the distinguishing claim - faith excluding works - is actually present).
```

That is a **general rule plus one hand-written worked example for one term**. It does not add structure. Every other dictionary entry with the same universal-root shape is left with no equivalent guard:

- `born-again` -> `display_terms: ["born again", ...]`, and the file's own `period_originated` admits "(the phrase itself is ancient)" — an admission that exists as prose in a field the classifier never sees.
- `original-sin-developed` -> `display_terms` include `"the fall"` and `"born sinful"`.
- `transubstantiation` -> `display_terms` include `"real presence in the Eucharist"`. A house-church participant asking whether Christ is really present in the bread is asking a *native* question — pahc has a Tier-1 `eucharistia` chunk for exactly it — but `origin_year: 1215` means it bridges for all six shipped worlds.
- `sola-scriptura` -> `"the Bible is the only authority"`; `personal-relationship-with-jesus` -> `"personal relationship with God"`.

**Structural answer to your question: the dictionary stores display phrases and a prose gloss, never the distinguishing feature as its own addressable field. The classifier is given only the display phrases. Tonight's fix moved the missing distinction from "absent everywhere" to "present as one English example inside a shared prompt string," which is a real improvement for `sola-fide` and does nothing for the other nine terms.** Note also that the Part XIV lesson from the roundtable file — "quoting a specific banned phrase as a negative example made the model more likely to produce it" — applies uncomfortably to a fix whose mechanism is a quoted example.

### 5.2 A second consequence of the same gap: the bridge replaces the retrieval query

Because the intercept runs before any Representative is invoked (`main.py:809-814`), a bridged turn never runs the world's own retrieval against the participant's actual words. `stream_modern_term_bridge` builds a working state whose last `HumanMessage` is the generic handback (`"In your own world... what did your community actually hold about {subject}?"`), and `_prepare_representative_turn` takes the most recent `HumanMessage` as its retrieval query. So on a false positive, the world's lexicon is searched against a world-agnostic paraphrase rather than the participant's question — the world's own Tier-1 chunks are being matched against text written for no world in particular. **Bucket (C): the right chunks may exist, but the query that would find them was replaced.**

### 5.3 The multi-world short-circuit

Root cause, per the commit and confirmed in `main.py:1020-1041`: the bridge branch returned unconditionally. The fix seeds the shared continuation loop (`bridge_seed_messages`, `bridge_seed_world_id`, `turns_completed = 1`) so the remaining seated worlds still speak. Verified correct in the code as it stands.

**Two residual data-model asymmetries this fix does not address**, both visible in `classify_modern_term`:

1. `world_id = seated_world_ids[0]` — the anachronism determination is made against the **first seated world only**. `_is_anachronistic` compares `origin_year` against that one world's end year. Parsed manifest end years are pahc 200, alexandria 400, syriac 410, hieronymian 420, desert 430, imperial-juridical 451. So at a table seating pahc + imperial-juridical, a question about the Trinity (`origin_year: 325`) fires the "that is a later term" Facilitator beat because pahc happens to be seated first — and it is simply false for Marius's world, which sits squarely inside 325–451. After tonight's fix, Marius now speaks *after* that incorrect framing rather than the round ending, which arguably makes the wrongness more visible.
2. The reframe is never persisted (spec §5, `modern_term_bridge.py:170-171`). So world[0] answers a term-free reframe while worlds 2..n, entering through the continuation loop against `working_messages`, answer the **raw modern-term question** — the last `HumanMessage` there is still the participant's original. The table gives two different treatments of the same question depending on speaking order.

---

## Summary of the distinction you asked for

| | count | where |
|---|---|---|
| **(A) not available at all** | ~10 | Desert (Poemen, Sisoes), Imperial (Leo's pre-papal life, the Tome's courier), PAHC ("Christian," all crisis material), Syriac (post-410 reception, qyama admission criteria), Theon (no approved-source list) |
| **(B) available, not surfaced** | ~5 | Sarah's occasion, the leaking-jug attribution, Origenist-vs-Chalcedon horizon, the convention living only in builder docs, Papnoute's Tier-1 scenes blocked by a prompt whitelist |
| **(C) surfaced, wrong quantity/form** | ~17, the largest cluster | preservation-register vocabulary leaking from artifacts *and* from injected chunk sections; Marius's sentence lengths; Mar Yausep's transmission excursus; Theon's prefixed self-narration; ~4,300 words of retrieved context per Alexandria turn; the repeated-story de-dup that cannot fire |
| **(D) pure prompt wording** | the entire self-narration line, Parts VII–XVII | plus Mar Yausep's Turn 7 framing and the Desert soft-instruction absoluteness |

**The single most load-bearing observation for your redesign:** the project has treated retrieval as solved and generation as the problem. Generation length has an exhaustive empirical tuning record. Retrieval has `k=3`/`k=2` untouched since the scaffold commit, a Tier-1 short-circuit that bypasses conditions entirely for half the worlds, a de-duplication guard that is a substring match against strings nobody says, Retrieve-When conditions that in two worlds are topic labels and in several worlds reference state the runtime cannot see, a parser that drops the one field designed for lightweight surfacing while injecting builder-facing scholarly apparatus verbatim, and a bridge dictionary whose schema has no slot for the thing it needs to discriminate on. Every bucket-(C) register failure in Phase 5 has a plausible per-turn supply line running through that stack, and no review has yet looked at it.
