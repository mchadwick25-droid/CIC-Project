# Adversarial review (round 3): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus review, dispatched 2026-08-07 — the third adversarial pass on this document, run immediately before its Fable thread. Rounds 1 (`..._Round1_2026-08-06.md`) and 2 (`..._Round2_2026-08-07.md`) were read in full first, per the Standard Practice's point 4, before any new hunting began.*

*Named failure mode hunted, per point 5: **a fix commit that also carries a substantial unreviewed restructuring.** `b20005c4` did two things at once — it applied round 2's seven P0s and one P1, and it folded in a session's worth of priority-restructuring prose (a tiered §6, an extended Objective 1, 3, and 4, a new §4 scope bullet, a new §1 success test). The first half is a targeted repair against a written review; the second half is brand-new prose that nothing has ever checked. Round 2's own closing sentence named exactly this: "four of the seven P0s are in prose that was 24 hours old and had never been verified once." The commit's diff is 182 insertions, and roughly two-thirds of them are the unreviewed half.*

*Verification method: round 2's story-`Tier` and drift-signal-count fixes re-derived from scratch against `story_retriever.py`, `story_indexer.py`, `retriever.py`, `indexer.py`, `state.py`, and `wrs/parameters.yaml` — not against the commit message's account of itself. All 118 lexicon chunks and all 60 story chunks re-measured programmatically, including a structural (not string-match) scan for the `Ecological Function` section and a scan of every chunk for the `Key Sources` marker. The real serialisation path (`indexer`'s `split("---", 2)` → `truncate_at(body, KEY_SOURCES_MARKERS)` → `excise_section(body, QUICK_MEANING_MARKERS)`) executed directly against individual chunks to see what actually reaches generation. `09_External_AIPersona_Framework_Survey.md`, `07_RepresentativeVoice_Lenses_Audit.md`, and `10_Fable_Conversational_Realness_Study.md` opened and read at the relevant sections. `CiC_L3C_Representative_Construction_Framework_V3.2.docx` extracted fresh from `word/document.xml`. `table_discourse.py`, `nodes.py`, `representative_prompts.py`, `facilitator_prompts.py`, `CitationMarker.tsx` read at the cited symbols. Flesch-Kincaid / Flesch Reading Ease computed on all six permanent prompts and all six World Capsule Cores with a local implementation of the standard formulas (`textstat` is not installed in this environment — figures are indicative of the gate's verdict, not the gate's own output).*

---

## Bottom line

**Not ready to send.**

Round 2's fix half largely landed, and the two fixes this dispatch asked me to re-derive independently are both **exactly right**. The story-`Tier` mechanism is now correctly attributed (I re-measured: 60 story chunks, **35** carrying `## Retrieval Front-Matter`, `story_retriever.py:148` synthesising Tier from metadata, `retriever.py:194` with no equivalent line and no `tier` reference anywhere in the file). The drift-signal count is now correct (`state.py:21-42` declares exactly **20** types, `agreeing` third and `over_producing` fourth in both that Literal and the monitor prompt, `parameters.yaml:116-117` recording 20 with its own FLAG-016 history). Structural health held: balance ratio **53.3 / 46.7**, and **67 of 68** internal `§N` pointers resolve. Round 2's single broken cross-reference (Objective 6's `validation-probed (§8)`) is genuinely closed by §8's new sustained-disagreement probe.

But **five send-blocking defects remain**, and they split the same way round 2's did — with the balance now tipped hard toward the unreviewed half of the commit:

**Introduced by the unreviewed restructuring (3):**

- **§4's brand-new interview-vs-table bullet misattributes the mechanism it exists to protect.** `REACTIVE_TURN_GUIDANCE` carries no length ceiling — it explicitly refuses one ("does not need to be brief for its own sake"; "do not match your length to the turns around you"). The only turn-length ceiling in the system is `_HOW_YOU_ENGAGE`'s **"A Turn Has a Measure"** (`representative_prompts.py:59-60`) — *inside the block §7 Part A tells Fable to rewrite*. The bullet points Fable at a file §7 never touches and away from the one paragraph actually at risk. `table_discourse.py` also carries no per-world reasoning.
- **§6 Objective 3's Albina resolution names two levers, neither of which moves the instrument §8 assigns to test it.** Flesch-Kincaid is a function of exactly two variables: words per sentence and syllables per word. "Clause richness" is invisible to it; richer "vocabulary" makes it *worse*. At Albina's measured 23.6 words/sentence, FK ≤ 10 requires ≤ **1.39** syllables per word — below the 1.34–1.47 range every one of the six current prompts already runs at, and below general English. The one lever that would work is the one §6 tells her to preserve.
- **§8 still calls Objective 4 "the one non-negotiable objective in this brief" (line 725).** §6 lines 478-484 now names **two**. The document states its own priority structure two contradictory ways, and §9 explicitly instructs Fable to stop at a clean boundary if budget runs short — the one situation where knowing which objectives are non-negotiable decides what gets built.

**Round-2 P0 fixes that introduced a new error while correcting the old one (2):**

- **§3's Persona Framework Survey correction replaces one overclaim with a misattribution pointing the other way.** "Character Card's own spec allocates 0-32,000 characters to example dialogue against 500 for description (Character.AI's real production numbers match that ratio)" — the 32,000/500 figures are **Character.AI's** field limits (doc 09 lines 122-123), an entirely different system from the Character Card spec, which has no character limits at all and whose *actual* statement about example dialogue is the pruning rule round 2 blocked on. One data point is presented as two independent ones, sourced to a spec that says the opposite.
- **§5(B)'s build-process-leak finding is scoped one level too narrow, and its absence count is wrong.** Measured structurally rather than by string match: **11** lexicon chunks have no `Ecological Function` section, not 9 — Marius's world carries two nobody has flagged. And **six** chunks carry no `Key Sources` marker at all, so `truncate_at` is a no-op on them and non-EF build metalanguage reaches generation *verbatim*: `## Final Assembly Instruction` — including the literal path `L4-Templates/Deployment_Lexicon_Chunk_Template.md` — in Marius's world, `## Related-Terms Reciprocity Note` in Yausep's. I confirmed this by executing the real serialisation path, not by reading it.

**Cross-reference integrity: 67 of 68 resolve. The one that does not is new** — Objective 1's *"The Realness Study's 'proactive memory surfacing' finding (§3)"* points at a §3 whose Realness Study bullet names persona-enactment, sustained disagreement, and three drift signals, and says nothing about memory or callbacks. The finding is real and is in doc 10 (lines 13, 47) — it just isn't in the section cited.

**And the completeness map got worse, not better.** Round 2 found one objective with no deliverable and no instrument. There are now **three** holes, two of them opened by this commit: Objective 1's new circular/callback half (no deliverable, no instrument, no named Research task — `callback`, `circular`, and `memory` all appear **zero** times in §7, §8, and §9), Objective 4's new transparent-sourcing half (`transparen` appears **zero** times in §7 and §8), and Objective 6's licensing text, which the commit message claims to have closed but only half-closed (`disagree`, `pushback`, and `licens` all appear **zero** times in §7; §8 will now probe for a behaviour nothing in §7 was told to write).

The measurable shape of the problem: §6 grew from **302 to 901 words** (+198%) while §7 grew **+7.5%** and §8 **+4.9%**. The restructuring added priority prose at the top of the stack without adding execution paths underneath it. That is not the round-1 failure mode (an excellent re-diagnosis with a thin design attached) — the balance ratio is still healthy — but it is a close relative of it, localised inside §6.

None of the five is a writing problem. All five would propagate. Four of them are single-paragraph or single-clause fixes; the fifth (Objective 3's Albina resolution) needs an actual decision rather than an edit.

---

## P0 — fix before sending

### P0-1. §4's new interview-vs-table bullet points at the wrong file, and away from the one paragraph the register rewrite actually endangers.

Brief §4, lines 209-216, entirely new in `b20005c4`:

> *"A solo Deep Interview conversation and a multi-Representative Table conversation are already, deliberately, held to different pacing — **`REACTIVE_TURN_GUIDANCE`'s length ceiling for a non-first speaker in a round**, `OPENING_TURN_LARGE_TABLE_GUIDANCE`'s own separate allowance for a round's opening turn, and **`table_discourse.py`'s per-world reasoning** reached because a crowded table has to stay readable one idea per turn, **while a solo conversation can afford more room to develop a single idea**."*

Read at source, three of those four claims are wrong.

**1. `REACTIVE_TURN_GUIDANCE` has no length ceiling. It explicitly declines one.** `app/prompts/table_discourse.py:75` ff., verbatim:

> *"Let the length fit what the moment actually calls for — a real engagement is usually shorter than an opening statement, **but does not need to be brief for its own sake if there is a real view to add**. And **do not match your length to the turns around you**. The worlds at this table do not speak at one measure — one world's whole word is a sentence, another's is a staged case — and a round where every turn runs the same length has already flattened the voices in it. **Speak at your own formation's measure even when it is conspicuously shorter or longer than what the last voice gave.**"*

It also carries an anti-lengthening clause pointing the *other* way from a ceiling: *"'real depth' is not a license to override your own formation's own native measure — if your own permanent formation's characteristic word is markedly shorter than this shape implies... that shorter measure is your real depth."* This is a block about **not homogenising** length, not about capping it.

**2. The actual ceiling is inside `_HOW_YOU_ENGAGE` — the block §7 Part A rewrites.** `app/prompts/representative_prompts.py:59-60`:

> *"## A Turn Has a Measure — Your own permanent formation names how long your world's characteristic word runs — keep to that measure. Where it is silent, **default short: most turns are one to two short paragraphs, and a turn should almost never exceed three.** Length is not depth."*

`_HOW_YOU_ENGAGE` spans lines 5-76, which §7 Part A cites by that exact range and instructs Fable to rewrite.

**3. The solo path gets *less* length guidance, not more.** `nodes.py:1130-1140`: the primary-turn path — *"single-world 'Deep Interview' mode (always, since `is_reactive` is always False there)"* — sets `reactive_turn_guidance = ""`. Its own comment records why: *"Previously received its own `PRIMARY_TURN_GUIDANCE` block here; **folded into representative_prompts.py's always-present `_HOW_YOU_ENGAGE` instead** (Mark's own call, 2026-07-24/25)."* So the solo path's *only* pacing rule is `_HOW_YOU_ENGAGE`'s default-short ceiling. The table paths get extra length language layered *on top of* that same ceiling. The asymmetry runs the opposite direction from the bullet's description.

**4. `table_discourse.py` carries no per-world reasoning.** Its only world-specific content is `CROSS_WORLD_VOCABULARY_GUIDANCE` (`:57`), a single string listing four worlds' vocabularies as examples of terms *not* to borrow. Per-world reasoning-mode paragraphs live in the six permanent prompts, which §7 rewrites.

**Why this blocks.** The bullet's *purpose* is right and valuable: this tuning is real, it predates the rebuild, and a register pass could destroy it as a side effect. But a Fable pass executing the bullet literally will read `table_discourse.py` (which §7 never opens) carefully and treat `_HOW_YOU_ENGAGE` as the thing being replaced wholesale — deleting "A Turn Has a Measure" along with everything else in lines 5-76. That is the single highest-consequence deletion available in this rebuild, and it compounds directly with round 2's still-unapplied P1-3: the Realness Study's headline finding is that the "assistant register" (long, over-explaining replies) is the primary tell that breaks realness, and every addition §7 Part A makes — worked examples, a four-shape repertoire, a bridge-first opening that names the participant's assumption before answering — pushes length up. The one existing brake is inside the block being rewritten, and this bullet tells Fable it is somewhere else.

**Fix.** Rewrite the bullet: the shared default-short measure lives in `_HOW_YOU_ENGAGE` at `representative_prompts.py:59-60` and must survive the Part A rewrite verbatim or be deliberately re-decided; `REACTIVE_TURN_GUIDANCE` (`table_discourse.py:75`) is a *non-homogenisation* rule, not a ceiling, and is out of §7's edit path; `OPENING_TURN_LARGE_TABLE_GUIDANCE` (`:69`) is the one genuine table-specific allowance; drop "per-world reasoning" from the `table_discourse.py` clause.

---

### P0-2. §3's Persona Framework Survey correction fixes the direction and breaks the attribution. The 32,000/500 numbers belong to a different system than the one the brief credits, and the spec it credits says the opposite.

Brief §3, lines 106-115, new in `b20005c4`:

> *"Its own verdict on worked examples is **mixed, not industry-wide either direction — 'it is not unanimous,' the document's own words.** **Character Card's own spec allocates 0-32,000 characters to example dialogue against 500 for description (Character.AI's real production numbers match that ratio)** — a strong signal *for* worked examples as load-bearing, not evidence they're ephemeral. Two other major vendors structure persona work almost entirely around named traits instead."*

**What checks out.** *"So it is not unanimous"* is verbatim, `09_External_AIPersona_Framework_Survey.md:309`. *"Two other major vendors structure persona work almost entirely around named traits"* is near-verbatim from the same line (Microsoft and IBM). The overall direction — that the survey does not support a blanket "ephemeral" reading — is correct, and removing round 2's blocked claim was the right call.

**What does not.** The 32,000-vs-500 figures are **Character.AI's** field limits, from doc 09 §2, lines 122-123:

| Field | Limit | Doc 09's own wording |
|---|---|---|
| **Long Description** | 0–500 chars | *"A few sentences up to a paragraph that gives more detail"* |
| **Definition** | **0–32,000 chars** | *"A large, free-form field that can contain structured example dialogs or any text content"* |

Character.AI is the consumer product surveyed in doc 09 §2. The **Character Card spec** (V1/V2/V3) is the hobbyist JSON format surveyed in §1 — a different artifact with a different origin and **no character limits on any field**. What the Character Card spec actually says about example dialogue is doc 09 line 20, quoting V1 normatively:

> *"`mes_example` — 'Example conversations… **SHOULD**, by default, only be included in the prompt until actual conversation fills up the context size, and then be **pruned** to make room for actual conversation history.'"*

That is the pruning rule round 2's P0-3 blocked on, now attributed — with the numbers of a different system attached — as evidence *for* permanence. And "(Character.AI's real production numbers match that ratio)" presents Character.AI as a second, corroborating source for a figure that came from Character.AI in the first place. One data point rendered as two.

**A second, smaller problem in the same bullet: the balance is still misrepresented, now in the opposite direction.** The brief offers one point for (mis-sourced) and "two other major vendors" against — reading 1-for / 2-against while claiming "mixed." Doc 09's own table at lines 299-307 is **5 for / 2 against**:

| Source | Doc 09's status line |
|---|---|
| Google Conversation Design | *"Required, produced before flows and before code; one of only two high-level deliverables"* |
| Amazon Alexa | *"Required — terminal step of the persona procedure... and a mandatory storyboard component"* |
| Salesforce | *"Required Design-phase deliverable"* |
| Character.AI | *"32,000 chars for Definition vs. 500 for Long Description"* |
| Character card ecosystem | *"`mes_example` is a normative top-level field; Ali:Chat is an entire authoring school built on it"* |
| Microsoft | *"Not required — relegated to 'SCRATCH PAD'"* |
| IBM | *"Absent"* |

Google, Alexa, and Salesforce — the three round 2's fix instruction named explicitly — are still absent from the brief. So is Anthropic's own guidance at doc 09 line 315, which round 2 also named: *"Examples are one of the most reliable ways to steer Claude's output format, tone, and structure"*, with *"Include 3–5 examples for best results."* That is direct model-side evidence about the exact model CiC runs, on the exact question §9 sends Fable to research, in a document the brief cites and does not carry.

**Why this blocks.** §9's Research stage is sent to doc 09 for this question, and §3 remains the parenthetical that also tells Fable doc 09 covers *"(Character Card V1-V3, SillyTavern)"* — round 2's P2-7, unapplied. A Fable researcher opening the Character Card spec to verify the brief's headline number will find no such number and will find the pruning rule instead, and will not know which half of the bullet to trust. This is the same failure shape as round 2's own P0-1 (a mechanism attributed to the wrong artifact), inside the fix for round 2's P0-3.

**Fix.** Attribute the numbers correctly — Character.AI's `Definition` field allows 0–32,000 characters against 0–500 for `Long Description`, doc 09 lines 122-123, its own verdict at line 151 being *"the platform with the most persona-conversation volume in the world gives description 1.5% of the budget it gives demonstration."* State the Character Card spec's contribution separately and honestly: `mes_example` is a normative top-level field, and it is also the first thing evicted under context pressure — a prompt-economics rule, which `10_..._Realness_Study.md:42` records does not currently bind CiC's full-history-in-context caching. Name Google, Alexa, and Salesforce on the required side. Carry Anthropic's 3–5. Keep the "not unanimous" framing and the do-not-lean-in-advance instruction, both of which are right.

---

### P0-3. §6 Objective 3 resolves round 2's Albina contradiction with two levers, neither of which moves the instrument §8 names as Objective 3's test.

Round 2's P0-7 was the real one: §6 granted Albina a sentence-length exemption that Part Five withholds, and nothing resolved it before world #1 in the build order. The commit resolved it, in Part Five's favour, and the *reading* of Part Five is faithful. I extracted paragraphs 85 and 86 fresh from `word/document.xml` and confirmed:

- *"these are two independent checks and must not be conflated"* (para 86) → the brief's *"register elaborateness and accessibility are separate axes"*. **Faithful.**
- The quoted sentence — *"A world whose own sources are rhetorically trained and elaborate should still keep its sentences within the accessibility band — elaboration belongs in vocabulary, imagery, and clause content, not in unbroken sentence length"* — **verbatim exact** to para 86.
- *"Albina's periodic rhythm is not an exemption from that floor"* → para 86's *"should still keep its sentences within the accessibility band."* **Faithful.**

So the resolution is a faithful reading, not a convenient one. That part of the dispatch's question answers cleanly: **yes.**

**What does not survive is the operational instruction the brief builds on top of it.** Brief §6, lines 534-538:

> *"Measured today she runs 23.6 words/sentence — her periodic quality has to survive being achieved through **clause richness and vocabulary** rather than raw sentence length, a real design problem this rebuild has to actually solve for her, not wave past."*

§8 names `readability_check` (`wrs/gates/core.py:211`) as *"the instrument that actually tests Objective 3."* That function calls `textstat.flesch_kincaid_grade` and `textstat.flesch_reading_ease` — the standard formulas:

```
FK  = 0.39 × (words/sentence) + 11.8 × (syllables/word) − 15.59
FRE = 206.835 − 1.015 × (words/sentence) − 84.6 × (syllables/word)
```

Both are functions of **exactly two variables**. Neither can see a clause. So of the two levers §6 names:

- **"Clause richness" is invisible to the instrument.** Every clause structure at a fixed sentence length and syllable count scores identically.
- **"Vocabulary" moves the instrument the wrong way.** Richer vocabulary means more syllables per word, which raises FK and lowers FRE. Part Five's own para 85 explicitly forbids using vocabulary as the compensating lever in the other direction: *"this standard is independent of vocabulary: a world's own difficult or technical terms are not simplified or removed to meet it."*
- **Sentence length is the only lever that helps** — and it is the one §6 tells her to preserve.

The arithmetic, at Albina's own measured 23.6 words/sentence:

| words/sentence | syllables/word needed for FK ≤ 10 |
|---|---|
| **23.6** | **≤ 1.389** |
| 20.0 | ≤ 1.508 |
| 18.0 | ≤ 1.574 |
| 16.0 | ≤ 1.640 |
| 14.6 (Papnoute's measured baseline) | ≤ 1.686 |

For reference, the six current permanent prompts run **1.34–1.47** syllables per word. A Latinate scholar's register runs higher, not lower. At 23.6 words/sentence, Albina needs vocabulary *simpler than the project's current average* to clear the band — which is precisely what Part Five forbids adjusting and §6 Objective 3 protects in its own first sentence (*"keeping each world's genuine imagery, vocabulary, and actual distinctiveness"*).

There is a further precision problem in the same sentence. Part Five permits elaboration in *"clause **content**"*; the brief renders this as *"clause **richness**."* Those are different things on the exact axis para 86 says must not be conflated: clause *content* is what a clause carries, clause *richness* reads as how many clauses there are. And a **periodic** sentence is by definition one that suspends its main clause behind subordinate ones — a structure that requires clause-chaining, which para 85 names as the specific thing to avoid (*"avoiding long chains of clauses joined by em-dashes, colons, and semicolons"*). §6 asks Albina to keep a structure defined by clause-chaining while removing clause-chaining.

**Why this blocks.** Albina is **first** in §7's risk-ordered per-world sequence and a primary §8 acceptance world. §6 now states an outcome ("keep the periodic quality, hit the band") that is close to arithmetically unavailable, §8 names an instrument that cannot register the compensation §6 proposes, and round 2's second fix instruction — *"add the decision to §9's Research stage explicitly... whether Part Five's band binds her, whether her exception is a documented deviation, or whether Part Five needs amending. That decision gates §7's first per-world pass and cannot be discovered mid-build"* — **was not applied.** §9 task (c) still asks only *whether the gate has ever been run*, not what happens when it fails. Fable will discover this at the top of world #1 with no rule and a brief that says the problem is already solved in principle.

**Fix.** Two edits. In §6, replace *"clause richness and vocabulary"* with Part Five's own words — richer clause *content*, imagery, and vocabulary inside shorter sentences — and state plainly that sentence length is the only lever the gate can see, so hitting the band means her sentences get shorter and her periodic quality has to be carried by suspension within a shorter span or given up. In §9, add the decision round 2 asked for as an explicit Research-stage gate before world #1: run `readability_check` on Albina's current output, and if she fails, decide — band binds and the rhythm changes, or the rhythm holds and her deviation is documented against Part Five, or Part Five is amended. Nothing in §7 Part A's Albina pass should start before that is decided.

---

### P0-4. §5(B)'s build-process-leak finding is scoped to the wrong boundary, and its absence count is two chunks short. Six lexicon chunks have no `Key Sources` marker, so the strip that finding assumes is doing the work is a no-op on them.

Brief §5(B), lines 291-293 and 298-312:

> *"109 of 118 carry an explicit `Ecological Function` field (**9 missing** — 5 in Alexandria/Theon's own set, 2 each in Syriac and PAHC)"*
>
> *"...and this field sits before Key Sources, **so nothing currently strips it before it reaches generation context**."*

**The count is wrong: 11 chunks, not 9.** Measured structurally — locating an actual `## Ecological Function` heading or a `**Ecological Function:**` inline label, rather than string-matching the phrase — **107 of 118** carry the section. The two the earlier count missed are:

- `data/imperial_juridical_world/lexicon_chunks/ijclex011_basilica.md`
- `data/imperial_juridical_world/lexicon_chunks/ijclex012_martyrium.md`

Both contain the *string* "Ecological Function" — inside a `## Final Assembly Instruction` note declaring its **absence**: *"Tier 3: World Meaning brief, **Ecological Function and Key Sources omitted** per Template instruction."* A string grep counts them as present. Rounds 1 and 2 both measured 9 and the brief inherited it.

This is not cosmetic. IJC is **Marius's** world — one of §8's three primary acceptance worlds and second in §7's per-world sequence. §8's Theon bullet (lines 771-776) says *"Alexandria carries the single largest share of lexicon chunks missing an Ecological Function field (5 of 9 project-wide)."* The real figure is 5 of 11, and Marius carries 2 of 12 of his own world's chunks with no field at all — a 17% silent-no-op rate for §7 Part A's lead-with-insight instruction, in a world the brief never names as exposed.

**The boundary claim is wrong for six chunks.** `truncate_at` (`app/rag/sections.py:149-160`) returns *"`body` if section is None"* — i.e. it returns the body **unchanged** when no `Key Sources` marker exists. Scanning every chunk for all three marker forms, six have none:

| Chunk | World | What rides past the strip |
|---|---|---|
| `ijclex011_basilica.md` | Marius | `## Final Assembly Instruction` |
| `ijclex012_martyrium.md` | Marius | `## Final Assembly Instruction` |
| `syrlex005_memra.md` | Yausep | `## Related-Terms Reciprocity Note` |
| `syrlex008_mar.md` | Yausep | `## Related-Terms Reciprocity Note` |
| `pahclex012_hetaeria.md` | Chloe | `**Confidence:** Inferential-Thin...` |
| `pahclex013_pertinacia.md` | Chloe | `**Confidence:** Inferential-Thin...` |

I confirmed this by **executing the real path** — `content.split("---", 2)[2]` → `truncate_at(body, KEY_SOURCES_MARKERS)` → `excise_section(body, QUICK_MEANING_MARKERS)` — not by reading it. The serialised body for `ijclex011` ends, verbatim:

> *"## Final Assembly Instruction — Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0 (Tier 3: World Meaning brief, Ecological Function and Key Sources omitted per Template instruction). No brackets or builder notes remain. CT tag not applied."*

A literal internal template path, a build-audit statement, and an unresolvable reference to a "CT tag," reaching generation context whenever Marius retrieves "basilica" or "martyrium." `syrlex008`'s tail is lexicon bookkeeping in the same class: *"No reciprocal cross-reference asserted... included for completeness and runtime recognizability rather than because it organizes the ecology."*

This also **falsifies a round-1 "verified clean" item** that both later rounds inherited. Round 1: *"`## CT Contest Type` and `## Related-Terms Reciprocity Note` sit after `## Key Sources` in the chunk files, **so they are stripped from generation context**."* True for 112 chunks. False for these six, because the section they are stripped relative to does not exist.

**Why this blocks.** §7 Part A's new filter (lines 570-574) is scoped to *"Ecological Function fields [that] carry internal build-process vocabulary."* A filter written to that scope catches `hal_lex11` and misses everything in the table above — including the two worst instances, in the world §8 names as acceptance evidence. §4 freezes chunk content, so nobody in this thread is authorised to fix the six chunks, and §4's defect list presents the `CitationModal` `key_sources` leak as the only other build-process leak path. The brief's own framing thus certifies as clean a boundary that six chunks do not have.

**Fix.** Correct the count to 107/118 with the two IJC chunks named, and correct §8's Theon bullet to "5 of 11" while adding Marius's 2. Add one sentence to §5(B): six chunks carry no `Key Sources` marker, `truncate_at` is a no-op on them, and everything after their last content section reaches generation — with the two IJC `Final Assembly Instruction` blocks named as the worst case. Reword §7 Part A's filter from "Ecological Function fields carrying build-process vocabulary" to "any build-process, template, or lexicon-bookkeeping language reaching generation from a retrieved chunk, wherever it sits in the file," cross-referenced to §4's carve-out defect #1. Give the Research stage the question of whether the six chunks need a code-side fix (a general trailing-apparatus strip) rather than a prompt-side filter, since §4 freezes their content.

---

### P0-5. §8 says Objective 4 is "the one non-negotiable objective in this brief." §6, as restructured by the same commit, says there are two.

Brief §6, lines 478-484, new in `b20005c4`:

> *"**Two parallel, non-negotiable priorities — neither one waits on the other, and either one failing fails the whole program:** Objective 3 (conversation quality...) and Objective 4 (honest, rigorous representation...). These are not sequential; they're the two axes the Mission's plain-language test (§1) actually measures."*

Brief §8, line 725, untouched by the commit:

> *"This is the actual instrument for **Objective 4, the one non-negotiable objective in this brief**, which had no metric at all before this revision."*

**Why this blocks.** This is the same shape round 2 rated P0-5 — a document stating one fact two contradictory ways with no signal which to believe — and it lands on the newly-declared organising structure of the whole brief. §8 is the section that defines what "done" means, and §9's closing paragraph (lines 884-888) explicitly instructs Fable to *"stop at a clean boundary... rather than compressing quality to finish"* if budget runs short. That is precisely the moment a priority ranking gets used. A Fable pass reading §8 will treat Objective 3's `readability_check` as tradeable against a schedule and Objective 4's fabrication rate as not; §6 says both are program-ending. §6 was restructured specifically to make this call, and §8 still carries the pre-restructuring version of it.

**Fix.** One clause: *"the actual instrument for Objective 4, one of the two non-negotiable priorities §6 names."* Then re-read §8's `readability_check` bullet in the same light — it currently says only that this is *"the instrument that actually tests Objective 3"*, without flagging Objective 3's equal non-negotiable status.

---

## P1 — materially improves, not disqualifying

### P1-1. Objective 1's new circular/callback half has no deliverable, no instrument, and no Research task — and its own §3 pointer is the document's single broken cross-reference.

Brief §6, Objective 1, lines 504-511, new in `b20005c4`:

> *"**The circular half of this, not yet a concrete mechanism:** a real callback to something the participant already said is what actually closes the loop back to them... The Realness Study's 'proactive memory surfacing' finding (§3) is the closest existing lever — worth Fable's Research stage treating as a real design task, not an assumption that circularity falls out of bridge-first for free."*

Counted across the whole document: `callback` appears once (line 505, §6). `circular` appears at 38 (§2), 490/504/510 (§6). `memory` appears once (line 508, §6). **Zero occurrences of any of them in §7, §8, or §9.**

- **No §7 deliverable.** Part A's shared-file bullet list is bridge-first entry, the Ecological Function instruction and filter, the shape repertoire, and the FLAG-018 disambiguation. Nothing produces callback text. Part B's Part Five additions are the pattern repertoire, the bridge-first instinct, the Ecological Function instruction, and the worked-example requirement. Nothing there either.
- **No §8 instrument.** Round 2's P1-4 asked for a first-sentence-uptake tally for Objective 1's bridge half; it was not added (`uptake` appears **zero** times in the document). The circular half has nothing either.
- **No §9 Research task.** §9's Research stage enumerates four "at minimum" tasks (a)–(d). Circularity is not among them. "Worth Fable's Research stage treating as a real design task" is a gesture, not an assignment, in a section that assigns four other things by name.

**And the §3 pointer does not resolve.** §3's Realness Study bullet (lines 94-105) names the persona-enactment/sustained-disagreement finding and the three naturalness-collapse signals. It says nothing about memory, callbacks, or proactive surfacing. The finding is real — `10_Fable_Conversational_Realness_Study.md:13` and `:47` name *"proactive memory surfacing"* as *"the open frontier — flagged by Replika's founder as the single missing capability in the whole industry,"* and line 47 even supplies the exact mechanism §6 wants: *"surfacing a callback ('you asked earlier about suffering — what we're saying now touches that') needs zero new infrastructure, just prompt guidance."* It is simply not in the section cited, so a Fable reader following the pointer finds nothing and the cheapest, best-supported lever in the whole brief goes unused.

This is round 2's P1-1 recurring on a different objective — and on a worse one, because §6's own new framing makes Objective 1 *"the mechanism that makes Objective 3 achievable"*, i.e. structurally load-bearing for one of the two non-negotiables. §6 also concedes it is *"not yet a concrete mechanism."* A brief whose top-tier structure rests on an admittedly unbuilt mechanism, with no assignment anywhere, is handing Fable a hole at the centre of its own priority stack.

**Fix.** Add the callback requirement to §7 Part A's shared-file bullet list (doc 10 says it is prompt guidance, not infrastructure — the cheapest item in this brief), add a counted callback tally to §8 alongside the term-reclarification tally it would share transcripts with, add it to §9's Research list as task (e), and repoint the citation to `10_..._Realness_Study.md:47` — or add proactive memory surfacing to §3's doc-10 bullet so the `(§3)` pointer resolves.

### P1-2. Objective 6 got its §8 probe and still has no §7 deliverable. The commit message claims the gap is closed.

`b20005c4`'s message: *"Closed the Objective 6 execution gap round 2 flagged with a sustained-disagreement probe in Section 8."*

Round 2's P1-1 heading was *"Objective 6 has no deliverable in §7 **and** no probe in §8."* Its fix instruction was *"Either add a §7 Part A bullet giving disagreement its licensing text **and** a §8 probe... or demote Objective 6 to a Research-stage question."*

Counted: `disagree` appears at lines 99 (§3), 560 (§6), 777 (§8), 825 (§9). `pushback` at 450 (§5 D) and 554 (§6). `licens` at 45 (§2) and 558 (§6). **Zero occurrences in §7.**

Objective 6's own text still demands prompt-side work: *"**Explicitly licensed**, not just permitted by omission."* Licensing is text; §7 is where text gets written; nothing in §7 writes it. The net effect of the half-fix is worse than the original gap in one specific way: §8 will now run a multi-turn agreement-pressure probe against six rebuilt voices, and a failure will be reported against a behaviour no build step was assigned to produce.

There is a second-order version of the same problem. §7 Part B requires a *naturalness/register* probe category be added to Part Eight. Round 2 confirmed Part Eight has no **disagreement** category either. So §8's new probe has no home in the Construction Framework, which is exactly the gap Objective 5 ("world #7 doesn't reintroduce this") exists to close.

**Fix.** Add a §7 Part A bullet giving disagreement its explicit licence in the shared file — doc 10 line 34/75 puts it in the turn-guidance layer, and `_HOW_YOU_ENGAGE` is now that layer for the solo path (`nodes.py:1135-1140`) — and add a disagreement probe category to §7 Part B's Part Eight bullet alongside the naturalness one.

### P1-3. Objective 4's new transparent-sourcing half has no deliverable and no instrument.

Brief §6, Objective 4, lines 539-547, new in `b20005c4`:

> *"**Paired with transparent sourcing, not separable from it** — the existing three-level transparency mechanism (Article 30: inline in the text, hover for a summary, click for full detail — already built, `CitationMarker`/`LexiconHighlight`) has to keep working honestly through this rebuild... **both are this thread's job not to make worse by changing what citations actually carry.**"*

The mechanism claim verifies exactly. `frontend/src/components/CitationMarker.tsx:6-8`: *"Mirrors LexiconHighlight's Level 2/3 interaction pattern (hover for a short summary, click for full detail)... **per Article 30's Three-Level Transparency**."* Good citation.

But `transparen` appears at lines 54 (§3) and 483/540/541 (§6) — **zero times in §7 and §8**. "Not to make worse" is a do-no-harm requirement with no check that harm did not occur. Nothing in §8 verifies that citations still carry what they carried, and §7's per-world passes touch the prompt files that decide what gets said about sources. This is round 1's P1-7 recurring in a new place: the commit closed one half of Objective 4's completeness gap while opening a second.

One precision nit in the same bullet: it names the open placement question as *"per-turn marker vs. something closer to per-story."* The code's own stated open question (`CitationMarker.tsx:10-13`) is per-turn vs. **per-sentence**: *"Anchored at message end, not per-sentence: the backend currently attributes citations to a whole turn, not to the specific sentence they ground."*

**Fix.** Either add a citation-integrity check to §8 (the harness already captures citations — §8's own `mark_conversation_test.py` bullet says *"every citation shown are real"* — so a before/after diff of what citations carry is nearly free), or state plainly that the transparency half of Objective 4 is a standing constraint with no thread-level verification and say why that is acceptable.

### P1-4. The "Albina is the elaborate exception" premise that orders §7's per-world sequence is not supported by measurement of the files §7 actually edits.

§7 sequences the per-world passes **Albina → Marius → Theon → Papnoute → Chloe → Yausep**, justified as *"highest-register-shift and least-validated worlds first."* §5 treats Albina throughout as *"the world this brief treats throughout as the elaborate, register-heavy exception."*

That premise rests on §5(D)'s 23.6 words/sentence — which is Albina's **output** in the pilot's current arm, a legitimate measurement. But §7's per-world pass edits the **permanent prompt and the World Capsule Core**, and on those artifacts the picture is different. FK/FRE computed locally (standard formulas; `textstat` is not installed here, so treat these as indicative of the gate's verdict, not as its output):

| File | FK | FRE | words/sent | syll/word |
|---|---|---|---|---|
| Theon prompt | 6.3 | 77.9 | 15.8 | 1.34 |
| Chloe prompt | 7.0 | 73.1 | 16.0 | 1.39 |
| **Albina prompt** | **9.3** | **64.9** | **20.7** | **1.43** |
| Papnoute prompt | 9.9 | 61.4 | 20.8 | 1.47 |
| Yausep prompt | 10.2 | 63.5 | 23.4 | 1.41 |
| **Marius prompt** | **11.7** | **59.2** | **26.8** | **1.42** |
| Syriac capsule | 7.7 | 70.5 | 17.4 | 1.40 |
| Alexandria capsule | 8.1 | 72.3 | 19.8 | 1.35 |
| Desert capsule | 9.8 | 65.1 | 22.5 | 1.41 |
| **Hieronymian capsule** | **11.8** | **57.6** | **26.3** | **1.45** |
| **IJC capsule** | **12.8** | **55.2** | **29.0** | **1.44** |
| **PAHC capsule** | **13.6** | **54.2** | **31.6** | **1.43** |

Three things follow that the brief does not say:

1. **Albina's prompt is the third *most* accessible of the six.** Marius's is the least, and by a clear margin. §5(A)'s comparative reading already half-noticed this — *"his SECTION 3 register block is longer than Papnoute's"* — but the brief never connects it to the "elaborate exception" framing.
2. **The capsules are systematically worse than the prompts, and the relationship is not uniform.** Four of six capsules sit outside the band. **Chloe's capsule is the worst of all twelve files at FK 13.6 / 31.6 words per sentence** — while her prompt is the second plainest. §7 makes her the *pilot* world on the reasoning that she is *"the plainest file, lowest blast radius."* That is true of her prompt and false of her capsule, and §7's per-world pass covers both.
3. **§9 task (c)'s open question is narrower than it needs to be.** The brief correctly refuses to guess whether the gate has been run against the six *builds*. But it could have measured the twelve *files* §7 rewrites, and did not — which would have surfaced all of the above for free.

This is not a source-verification failure; the brief makes no false claim here. It is a premise that orders the entire build sequence and was never tested against the artifacts the sequence operates on.

**Fix.** Run `readability_check` against all six prompts and all six capsules before the thread starts, put the twelve numbers in §5, and let §7's risk ordering answer to them rather than to a single output measurement of one world.

### P1-5. §9's Research stage still frames doc 09's question as "ephemeral-vs-permanent" — the exact framing §3 was rewritten to remove.

Brief §9, lines 825-827:

> *"...and the Persona Framework Survey's **ephemeral-vs-permanent example-dialogue question** (bearing directly on §7 Part A's worked-example plan)."*

§3 was rewritten in this commit to delete precisely that framing and replace it with *"mixed, not industry-wide either direction."* §9 was not touched. This is round 2's P0-5 pattern exactly — one instance corrected, a second instance four sections later missed — and §9's Research stage is the primary consumer of §3's doc-09 bullet.

It also sends Research at a question that partly does not apply. The permanence/eviction split is a prompt-economics rule for systems under context pressure (doc 09's own verdict at line 95: *"TRANSFERS CLEANLY. Pure prompt economics"*), and `10_..._Realness_Study.md:42` records that CiC runs full-history-in-context with prompt caching and *"is already doing this correctly"* — so there is no truncation stage for an ephemeral field to be evicted from.

**Fix.** Replace with doc 09's own framing of the real open question: whether worked examples are load-bearing for CiC's case, given that vendor practice splits and that what is unanimous (doc 09 line 311) is the *relationship* — the trait rubric is fixed first and dialogue is written and judged against it.

### P1-6. §5(B) credits the Lenses Audit with a measurement it did not make, and puts the concentration in the wrong world.

Brief §5(B), lines 307-310:

> *"**The Lenses Audit (§3) independently measured this same leak across the corpus** and found it **concentrated exactly where the risk-ordered build sequence starts — Albina's own Hieronymian set.**"*

**The count itself is real and defensible.** I re-measured the body of every `## Ecological Function` section against a build-process vocabulary set (`Doc_0N`, `G<n>` gravity codes, Primary/Supporting/Tensional gravity, the `hal_lex11` audit phrasing): **29 of 107** EF-bearing chunks, **27%** — so "at least a quarter" and "roughly a quarter" both hold. Round 2's 29 reproduces. Good.

**The sourcing does not.** `07_RepresentativeVoice_Lenses_Audit.md` measured EF **quality**, not this leak. Line 141: *"41 chunks read in full across five worlds, plus a 90-file structural sweep. **26 GENUINE / 10 PARTIAL / 2 RESTATES / 3 absent**."* Line 155 names the builder-facing failure mode in exactly **four** chunks — `syrlex007`, `hal_lex12`, `hal_lex11`, and one implied — not a corpus-wide leak measurement. Doc 07 never counts build-process vocabulary across 118 chunks; this review and round 2 did.

**And the concentration claim inverts the distribution.** By absolute count the leak is **Alexandria's**, not Albina's:

| World | EF chunks carrying build-process vocabulary | of that world's total |
|---|---|---|
| **Alexandria (Theon)** | **17** | of 50 |
| Hieronymian (Albina) | 8 | of 15 |
| Syriac (Yausep) | 4 | of 10 |
| PAHC, Desert, IJC | 0 | — |

Alexandria carries **59% of every instance in the corpus**, and the brief never mentions it in this connection. HAL does have the highest *rate* (8 of 15), and doc 07's HAL 3-of-9 quality figure plus its diagnosis of HAL's *"noun-shaped"* entries (*"anchors G3," "the organizational bedrock"*) supports a rate-based reading — so the sentence is not baseless, just imprecise in a way that matters. §8's own Theon bullet already flags Alexandria as *"the world most exposed to §7 Part A's lead-with-insight instruction silently no-op'ing"* — for the 5 chunks that lack the field. It also holds 17 of the 29 that have the field filled with build-process prose, and the brief connects neither fact to the other.

**Fix.** Attribute the 29-chunk measurement to this review round (or re-derive it and cite the method), keep doc 07 for what it actually found — the 26/10/2 quality split, HAL 3-of-9, and the four named builder-facing chunks including `hal_lex11` — and state the distribution as Alexandria 17 / HAL 8 / Syriac 4, with HAL highest by rate and Alexandria highest by count.

### P1-7. §6's new tier structure gives no cut rule, and §9's two named stopping points both sacrifice the objective §6 holds apart.

§6's whole purpose is to establish what matters most: two non-negotiables, an enabling mechanism, a Tier 2, and Objective 5 *"held apart, not ranked among the others at all."*

§9's closing paragraph then asks Fable to make exactly the trade-off a ranking exists for:

> *"If partway through this genuinely doesn't fit in the available Fable budget, say so plainly and **stop at a clean boundary (e.g., after the pilot, or after the two highest-risk worlds)** rather than compressing quality to finish."*

Both named boundaries are Part A boundaries. Both drop Part B entirely — which is Objective 5, the *"not optional scope"* whose absence §7's own heading calls out (*"two parts, both required"*) and which §6 declines to rank. So the document's stated fallback plan sacrifices, by default, the one objective §6 refuses to place in the ordering, while preserving Tier 2 work.

That is not a contradiction, but it is an unstated decision. §6 was restructured to make priority explicit; §9 makes the one priority call that matters in practice and does it without reference to §6.

**Fix.** Either add Objective 5 to the tier framing with an explicit position, or add a sentence to §9's fallback naming which boundaries preserve which objectives — e.g. that the Part Five/Part Eight edits are the cheapest half of the mandate and should survive any truncation, since a shipped Part A with no framework change reproduces exactly the gap this brief exists to close.

### P1-8. Round 2's P1-2 through P1-8 remain unapplied.

Listed for completeness, not re-argued — all seven were verified in round 2 and none was touched by `b20005c4`. Two have become more consequential since:

- **P1-3 (the assistant register).** `assistant register` and `brevity` still appear **zero** times in the brief. Doc 10's own executive summary leads with it: *"the 'assistant register' — long, over-polite, over-explaining, agreement-prone replies — is the primary tell that breaks perceived conversational realness"*, with *"response-length restraint... nearly double the next-highest trait."* Every §7 Part A addition pushes length up, §8 still names no turn-length instrument, and P0-1 above shows the one existing brake sits inside the block §7 rewrites. This has moved from "omission worth fixing" to "the specific risk P0-1 creates."
- **P1-5 (continuity-regression pass criterion).** Still no threshold, and now the tension is sharper: §6's new tier framing makes register change a Tier-1 success condition, while §8's continuity-regression pass treats voice change as the alarm.

Also still open: P1-2 (the 16-trait rubric required in §7 Part B and absent from §8's instrument list), P1-4 (first-sentence-uptake tally — see P1-1 above), P1-6 (the pilot results file `mark_voice_simulation_results.json` still uncommitted, still carrying four of §5(C)'s claims, still not covered by §8's commit-a-durable-copy action), P1-7 ("measurably stronger weight" — the wording survives verbatim in §3 line 118 despite the commit reworking the sentence around it), and P1-8 (the doc-07 build-time/runtime clause).

---

## P2 — polish

1. **`wrs/parameters.yaml:101-114` should be `:102-114`**, in both §7 Part B and §8. Line 101 is blank; `reading_floor:` is at 102. Round 2's P2-1, unapplied, third round running.
2. **`wrs/parameters.yaml:116-121` is short of what §4 cites it for.** `drift_signal_count_emitted: value: 20` is at 116-117 and the range 118-123 is the `source:` block, but *"its own history — an earlier 'ten' or 'seventeen' count is stale, flagged FLAG-016"* lives in `notes:` at **124-130**, outside the cited range. Also, "seventeen" is what the file flags as stale; "ten" is described there as a component of the 17 (*"10 monitor signals + anachronism alias + over_settling + 5 table-level checks"*), not as a stale count in its own right.
3. **§3's "the two lines its own note marks" is wrong; the log's note marks three.** `Decision-Log.md:19` supersedes bullet 1 (the 100% claim), bullet 4 (worked examples), **and bullet 5** (*"It also found 'the gap is enforcement, not philosophy' (bullet 5 above) is contradicted by Part Five's own text"*). Round 2's P0-6 stated this explicitly (*"the log's own note covers three"*) and the fix pass wrote two. The brief's own list of superseded bullets (1, 2, 4, 6) also omits bullet 5. Net effect is safe — the header instruction is *"treat that entry's entire findings list as superseded"* — so this is a nit rather than a repeat P0, but the miscount is in the sentence round 2 was correcting. The Decision Log itself was not updated by this commit (`b20005c4` touched one file); lines 13 and 17 still read as code-verified fact for anyone who opens it directly, which §3's blanket warning does now cover.
4. **The `hal_lex11` quote truncates mid-clause without marking it.** Brief: *"...found insufficient to establish a difference in kind."* Actual: *"...found insufficient to establish a difference in kind **from the community's dominant authority mode, only a difference in position**."* Both fragments are exact and in forward order, and the substantive claim ("Tensional gravity" and "candidate... tested" are internal build vocabulary sitting before Key Sources) is fully verified. Same class as round 2's P2-4.
5. **§7 Part B still says "the exact guidance §6/§7 believed they were inventing for Albina"** (line 638). After the §6 rewrite this is no longer a contradiction — §6 now quotes that Part Five sentence directly and endorses it — but it is a stale historical statement about a section that no longer believes any such thing. Round 2's P0-7 named the phrase; it survived.
6. **§4 retains *"all content- or posture-based, not register-based"*** for all twenty drift signals. Round 2 flagged this as unsupported for `length_ceiling` and `question_stacking`. `length_ceiling` is a declared `DriftSignal.signal_type` (`state.py:40`) and is never named in the brief.
7. **§8's per-signal drift breakdown drops the turn-over-turn point.** The brief's replacement framing — *"the actual gap isn't missing signal types, it's visibility: nothing today captures **which** of the twenty signals fired"* — is true, but the Realness Study's three signals are *trends* (length **growth**, **declining** initiative, agreement-rate **drift**). A per-signal firing count is not a rate over a conversation. Round 2's stated honest claim (*"none is tracked as a turn-over-turn rate"*) was the sharper one and did not survive.
8. **Objective 4's open placement question is misrendered.** Brief: *"per-turn marker vs. something closer to per-story."* `CitationMarker.tsx:10-13`: per-turn vs. **per-sentence**.
9. **§8 line 730 attributes to §4 a framing §4 does not carry.** §8: *"the raw `over_settling_adjudication` firing count **§4 already names as expensive-but-expected**."* §4 lists it under *"Two adjacent, already-diagnosed **defects**"* and says *"not a rare safety net in practice."* Round 1's P1-9 (the screen is deliberately tuned to over-flag; a high rate is the architecture working) was never applied to §4, and §8 now describes §4 as though it had been.
10. **Round 2's P2-3, P2-4, P2-5, P2-6, P2-7, and P2-8 all remain unapplied** — the reversed-order Marius composite in §5(A), the silently truncated Theon quote, the "four separate points" followed by "a fifth," §7 Part B's four-instrument list against §8's six (now seven, with the sustained-disagreement probe), §3's narrow description of doc 09's scope, and the Theon fabrication-guard kinship claim.

---

## What verified clean

Stated plainly, because four of round 2's seven P0 fixes are exactly right and two of the four are the ones this dispatch asked me to re-derive independently.

**Round-2 P0-1 (story `Tier`) — re-derived from scratch, correct in every particular.**

- 60 story chunks total; **35** carry `## Retrieval Front-Matter`, the same fenced block lexicon chunks use — so the brief's *"35 of the 60 story files carry the identical `## Retrieval Front-Matter` block lexicon files do"* is exact.
- `app/rag/story_retriever.py:148` — `context_parts.append(f"### {title} (Tier {tier})\n")`, exactly as quoted, with `tier = doc.metadata.get("tier", "")` at `:144`. Fed from `story_indexer.py:119` (`tier=int(front_matter.get("tier", "0") or "0")`) and `:145`.
- `app/rag/retriever.py:194` — `context_parts.append(f"### {term}\n")`, no tier. Confirmed: the string `tier` appears **nowhere** in `retriever.py`, while `doc.metadata["tier"]` is constructed at `indexer.py:227` one call away.
- The brief's causal claim — *"a deliberate code behavior, not an accident of file layout"* — is the correct mechanism, and the walked-back claim (*"it is not that story front matter escapes the stripping lexicon front matter gets"*) is correctly walked back.

**Round-2 P0-2 (drift-signal count) — re-derived from scratch, correct.**

- `app/graph/state.py:21-42` declares `DriftSignal.signal_type` as a Literal of exactly **20** members. Its own comment records the history: *"17 at S4.3; S4.7 adds the three §6.5 re-founding types... 20 total."*
- `agreeing` is the **third** member; `over_producing` the **fourth** — matching both the ordinal the brief uses and the monitor prompt's own numbering (`facilitator_prompts.py:135-175`, AGREEING #3, OVER_PRODUCING #4). The monitor's closing line confirms the length coverage: *"check shape and length as their own question."*
- `wrs/parameters.yaml:116-117` — `drift_signal_count_emitted: value: 20`, with `notes:` at 124-130 recording *"state.py's DriftSignal.signal_type Literal declares exactly these 20 (counted, S5.5). Stale 17 caught by the S5.5 pointer pre-check (FLAG-016...)."*
- *"Declining initiative has no existing equivalent and is the one genuinely new signal to add"* — verified against all twenty. Nothing in the set covers it; `question_stacking` runs the opposite direction and `dominance` is table-scoped.

**Round-2 P0-5 (§5 D transcript claim) — fixed.** §5(D) now reads *"the Decision Log entry named in §3 carries the real quotes and cost data this finding rests on, not the full transcripts themselves,"* consistent with §3 and §8. The off-by-two line reference (`Decision-Log.md:57` → `:59`) was corrected too; line 59 is indeed *"Full transcripts, cost tables, and citation excerpts: rendered as a styled Artifact... not reproduced in full here."*

**Round-2 P0-7 (Part Five vs. Albina) — the contradiction is genuinely resolved, and resolved faithfully.** Paragraphs 85 and 86 extracted fresh from `word/document.xml`; the quoted sentence is verbatim exact, the *"two independent checks and must not be conflated"* reading is faithful, and choosing Part Five's side (no exemption) is the right call. The problem is what §6 then says to do about it (P0-3), not the reading itself.

**New material that checks out.**

- **The `hal_lex11` Ecological Function quote is real.** Read at `data/hieronymian_world/lexicon_chunks/hal_lex11_exegesis-practiced-authority.md`: *"The evidentiary core of this world's one Tensional gravity — a genuine counter-current within the ecology... this candidate was tested directly and found insufficient..."* Both flagged phrases are present verbatim. Section order confirmed in-file (Quick Meaning → World Meaning → **Ecological Function** → Distortion Risk → Key Sources → Reported-Experience Status), so the brief's *"this field sits before Key Sources"* is correct for this chunk and for the 112 chunks that have a Key Sources marker.
- **"Roughly a quarter" is a real, defensible count, not an extrapolation from one example.** Re-measured independently: **29 of 107** EF-bearing chunks (27%), 29 of 118 overall (25%). Round 2's figure reproduces. The provenance is what needs fixing (P1-6), not the number.
- **Objective 4's Article 30 claim.** `CitationMarker.tsx:6-8` confirms the three-level mechanism and the Article 30 attribution in its own words. `LexiconHighlight.tsx` and `GlossHighlight.tsx` both exist and reference it as the shared pattern.
- **§4's `OPENING_TURN_LARGE_TABLE_GUIDANCE` clause.** Verified at `table_discourse.py:69`: *"it can run somewhat fuller than a later reactive beat — but that is a little more room for the one idea you are developing"*, and *"at a table this size, even the opening turn has to stay readable."* The brief's *"a crowded table has to stay readable one idea per turn"* is a fair reading of this block specifically. (The rest of the bullet is P0-1.)
- **Story-chunk field measurements.** Re-measured: 60/60 carry `Formation Ecology Connection`, **0/60** carry `Distortion Risk`. Every number in that half of §5(B) exact.
- **Structural health.** Balance ratio **53.3 / 46.7** (§1 296, §2 122, §3 811, §4 928, §5 2,306; §6 901, §7 1,283, §8 838, §9 881 — diagnosis 4,463, ask 3,903, total 8,366). Round 1's 68/32 failure mode remains absent across three rounds. **67 of 68** `§N` pointers resolve; round 2's single break (Objective 6 → §8) is genuinely closed and the one remaining break is new (P1-1).

---

## Why round 3 still found what it found

The dispatch asked, if the document turned out ready, that I explain why this round found less than rounds 1 and 2 — and if not, that I not soften. It is the second case, and the reason is structural rather than a matter of how hard I looked.

**The fixes held.** Every round-2 P0 that was a *pure repair against a written finding* landed correctly, and the two hardest — the story-`Tier` mechanism and the drift-signal count — survived independent re-derivation against source with nothing to correct. Round 2's warning about fix passes introducing new citation errors mostly did not come true for the repair half of the commit.

**The new material did not.** Of this round's five P0s, three are in prose that has never been reviewed by anyone (§4's turn-length bullet, §6's Objective 3 resolution, §6's tier framing colliding with §8), and two are in the two round-2 fixes that required *writing new claims* rather than deleting old ones (§3's persona-survey replacement, §5(B)'s leak paragraph). The pattern across three rounds is now consistent enough to state as a rule: **repairs that delete or re-point survive; repairs that require new positive claims introduce new errors at roughly the same rate as the original prose did.** Round 1 caught eight defects in original prose. Round 2 caught four in 24-hour-old prose that had never been checked. Round 3 caught three in prose that was hours old and had never been checked, plus two in the new claims written to fix round 2.

The one genuinely different finding this round is **P0-4**, which is not a brief error at all in origin — it is a data-and-code fact (six chunks with no `Key Sources` marker; two IJC chunks whose absence is invisible to a string grep) that all three rounds' measurement methods missed because all three grepped for a string rather than locating a section. That one was found by executing the serialisation path instead of reading it, which is what the Standard Practice's point 1 asks for and what "measured programmatically" in rounds 1 and 2 stopped one step short of.

**What this means for round 4.** Items P0-1, P0-2, P0-5, P1-1, P1-2, P1-3, P1-5, and P1-6 are corrections to identified sentences with the evidence already in this document — deletions and re-pointings, not research. P0-3 and P0-4 are the two that need an actual decision (what happens when Albina fails the gate; whether the six markerless chunks get a code-side fix under a §4 content freeze). A targeted re-check of P0-3 and P0-4 after editing is proportionate; a fourth full pass is not, **unless the fix pass again folds in unreviewed restructuring alongside the repairs.** If it does, the same thing will happen again, for the third commit running.

---

## Recommended fix list, in order

1. **§4's interview-vs-table bullet** — the ceiling is `_HOW_YOU_ENGAGE`'s "A Turn Has a Measure" (`representative_prompts.py:59-60`), inside §7 Part A's own edit target; `REACTIVE_TURN_GUIDANCE` is a non-homogenisation rule, not a ceiling; drop "per-world reasoning." **(P0-1)** — the highest-consequence fix, because it protects the one paragraph most likely to be deleted by accident.
2. **§6 Objective 3's Albina levers + a §9 decision gate** — FK sees only sentence length and syllables per word; state which lever actually moves and add the pass/fail decision before world #1. **(P0-3)**
3. **§5(B) + §7 Part A's filter scope** — 107/118 not 109/118, two IJC chunks named, six markerless chunks named, filter rescoped from "the EF field" to "any build-process language from a retrieved chunk." **(P0-4)**
4. **§3's doc-09 bullet** — attribute 32,000/500 to Character.AI, state the Character Card spec's own pruning rule separately, name Google/Alexa/Salesforce, carry Anthropic's 3–5. **(P0-2)**
5. **§8 line 725** — "one of the two non-negotiable priorities." **(P0-5)**
6. **Objective 1's circular half** — a §7 Part A bullet, a §8 callback tally, a §9 task (e), and repoint the citation to `10_..._Realness_Study.md:47`. **(P1-1)**
7. **Objective 6's §7 deliverable and Objective 4's transparency check.** **(P1-2, P1-3)**
8. **§9's "ephemeral-vs-permanent"** — align with the rewritten §3. **(P1-5)**
9. **§5(B)'s Lenses Audit attribution and the Alexandria 17 / HAL 8 / Syriac 4 distribution.** **(P1-6)**
10. **Measure the twelve files** (six prompts, six capsules) with `readability_check` before the thread starts and let §7's risk order answer to the numbers. **(P1-4)**
11. **Round 2's unapplied P1s** — the assistant-register finding and a turn-length metric first (P1-3), then the 16-trait rubric, the uptake tally, the pilot-results commit, "measurably," and the doc-07 clause. **(P1-8)**
12. **Sweep the P2s** — including round 2's five that survived a second fix pass.
