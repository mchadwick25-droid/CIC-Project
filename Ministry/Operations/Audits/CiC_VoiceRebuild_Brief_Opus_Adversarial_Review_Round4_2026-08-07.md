# Adversarial review (round 4): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus review, dispatched 2026-08-07 — the fourth adversarial pass on this document, run immediately before its Fable thread. Rounds 1 (`..._Round1_2026-08-06.md`), 2 (`..._Round2_2026-08-07.md`) and 3 (`..._Round3_2026-08-07.md`) were read in full first, per the Standard Practice's point 4, before any new hunting began.*

*Named failure mode hunted, per point 5: **a second substantial restructuring, deliberately un-bundled from the fix commit, that nothing has ever checked — plus the one thing three rounds of "measured programmatically" never did, which is ask what the cited instruments are actually wired to.** `0b4d19d2` was a disciplined corrections-only commit against round 3's five P0s. `fa10bdf3` and `6fcb15bc` then landed 1,400+ new words of Mark-directed restructuring across §6, §7 Part A, §8 and §9 — a clean-rebuild mandate, a cost/complexity license, a Research-owns-its-own-gaps clause, a Mark-approval gate, and a new positive framing for Objective 3. Round 3's closing sentence named the condition precisely: "a targeted re-check... is proportionate; a fourth full pass is not, **unless the fix pass again folds in unreviewed restructuring alongside the repairs.** If it does, the same thing will happen again, for the third commit running." It did, and it has.*

*Verification method: round 3's P0-1 (§4's interview-vs-table bullet), P0-3 (the Albina/Flesch-Kincaid arithmetic), P0-4 (the §5(B) chunk measurements) and P0-2 (the Persona Survey citation) re-derived from scratch against source, not against round 3's account of them. All 118 lexicon chunks re-measured by executing the real serialisation path (`content.split("---", 2)[2]` → `truncate_at(body, KEY_SOURCES_MARKERS)` → `excise_section(body, QUICK_MEANING_MARKERS)`), with `sections.py` loaded directly by `importlib` rather than through the package, and with a section-aware scan that handles **both** of the codebase's section conventions (`## Heading` and blank-line-preceded `**Label:**`) rather than only the first. Flesch-Kincaid and Flesch Reading Ease computed independently on all six permanent prompts with a local implementation of the standard formulas (`textstat` is installed in `venv/` but the figures below are my own, computed with my own syllable heuristic, so they are indicative of the gate's verdict rather than the gate's own output). `representative_prompts.py`, `table_discourse.py`, `nodes.py`, `retriever.py`, `sections.py`, `wrs/gates/core.py`, `wrs/gates/run_gates.py`, `wrs/views/plain_explanation.py`, `wrs/views/probe_parity.py`, `wrs/views/s62_hal_probe_parity.py`, `wrs/views/permanent_prompt.py`, `wrs/migrate/s27_voice_records.py`, `wrs/parameters.yaml` read at the cited symbols and line-numbered. **Every caller of `readability_check` in the repository enumerated.** All six worlds' `wrs/views/staging/*probe_parity_result.json` opened and read. `09_External_AIPersona_Framework_Survey.md` and `10_Fable_Conversational_Realness_Study_2026-07-24.md` read at the cited sections. `Decision-Log.md` read line-numbered. All 88 internal `§N` pointers extracted programmatically and resolved by hand against what the target section actually says.*

---

## Bottom line

**Not ready to send.**

The corrections-only commit was the most successful fix pass this document has had. **Both of round 3's fixes I re-derived from scratch are exactly right, and a third checks out too.** §4's interview-vs-table bullet now verifies verbatim at every cited symbol (`table_discourse.py:75`, `representative_prompts.py:59-60`, `nodes.py:1140`, `CROSS_WORLD_VOCABULARY_GUIDANCE` at `:57`). §5(B)'s chunk measurements reproduce exactly on independent re-measurement: **118 lexicon chunks, 107 with a real `Ecological Function` section, 11 without (5 Alexandria / 2 IJC / 2 PAHC / 2 Syriac), 6 with no `Key Sources` marker at all**, and `ijclex011_basilica.md`'s `## Final Assembly Instruction` tail reaches generation verbatim exactly as quoted. §8's "one of the two parallel non-negotiable priorities" repair is clean. Structural health improved on the axis round 3 complained about: the document grew 23.7% (8,366 → **10,350** words), and this time **§7 absorbed more of that growth than §6 did** (+651 vs +504 words), reversing round 3's "priority prose at the top of the stack without execution paths underneath it." Balance ratio is now **48.3 / 51.7** — the ask half has, for the first time, overtaken the diagnosis half.

But **seven send-blocking defects remain**, and they split into two groups the same way every round has:

**Introduced by the two unreviewed post-round-3 commits (4):**

- **The cost/complexity license grants permission to delete the only instruments for both of §6's declared non-negotiables**, names as droppable a mechanism whose only referent in this document is Article 30's already-shipped three-level transparency (which §6 Objective 4 declares "not separable" from no-fabrication and which the same paragraph claims to protect), attributes to §4 a cost ranking §4 does not make, and within one paragraph both closes and re-opens `over_settling`'s scope.
- **§7 Part A's clean-rebuild mandate contradicts §4's freeze list, §7 Part A's own bullets, and itself.** It instructs Design to write "identity, era, vocabulary... content fresh" — the exact three categories §4 lists under *What NOT to rebuild*. It is written entirely in per-world source terms while claiming to govern a shared, world-independent block that has no world sources. Its "no comparative diffing" rule collides with §4's instruction to deliberately preserve one named paragraph of the current block. Its source list omits the record layer the project's own prompt generator actually builds from, and names a Source Registry that does not exist in `data/` for worlds #1 and #2.
- **§6 Objective 3's new positive paragraph and §8 now contradict each other on whether `readability_check` tests Objective 3** — §6 says a conversation "can hit every readability number and still fail this objective completely"; §8 says it "is the instrument that actually tests Objective 3." Objective 3 is now half the program and its stated goal has no instrument anywhere. The paragraph's opening sentence is also grammatically broken and ambiguous on the one axis §1 says both failure directions are real on.
- **§7 Part A's leak filter, rescoped from round 3's general rule into a two-item enumeration, misses 17 chunks.** Measured on the real serialisation path with a scan that handles both section conventions: 46 of 118 chunks leak build-process metalanguage into generation context; the two enumerated patterns cover 33; **17 are caught by neither** — Desert 9 (half of Papnoute's entire corpus), Alexandria 5, IJC 3, including the verbatim string *"This is a lexicon-organization device for construction and runtime-retrieval purposes only"* on Marius's *primatus*.

**Never checked by any round, because no round asked what the cited instruments are wired to (3):**

- **`readability_check` is not connected to Representative voice at all.** Its only production caller renders Level-2 lexicon plain-explanations (`wrs/views/plain_explanation.py:174-175`); `run_gates.py:139-141` runs it against three test fixtures. Every world's `voice_profile` record states the floor is *"inherits reading_floor from wrs/parameters.yaml — a pointer, not a restatement."* §7 Part B's "Both ends are real and wired" and §8's "already built, already wired" are false as applied to voice, and Part Five's real gap **does** include enforcement for voice — which is precisely what round 1's P0-4 talked this brief out of saying.
- **§7 Part B's "New: a continuity-regression-testing step" already exists, for all six worlds, and has already been run, with committed results.** `wrs/views/probe_parity.py` plus five `s62_*_probe_parity.py` siblings are blind, two-trial, A/B-graded voice-continuity regressions — deployed prompt vs. record-assembled prompt, graded on register / measure / refusal / vocabulary, with a stated parity rule. The committed results read **Desert PASS, PAHC PASS, Alexandria FAIL, Hieronymian FAIL, IJC FAIL, Syriac FAIL.** Four of six worlds already fail voice parity, including Albina and Marius. Third instance of round 1's P0-4 shape.
- **§8 and §9 still tell Fable that one review round has happened and a second is "still warranted,"** while §7 says three. §8 sends Fable to the round-1 review "for the full account of what changed and why" — a document rounds 2 and 3 falsified in several places, including one of its own "verified clean" items. This is the identical defect §3 fixes for the Decision Log, unfixed for the review record itself.

**Cross-reference integrity: 88 internal `§N` pointers, up from 68. 82 resolve cleanly. One does not resolve at all** — Objective 1's *"proactive memory surfacing finding (§3)"*, round 3's break, unapplied. **Five more resolve to a section that does not say what they cite it for**, four of them new in the post-round-3 commits.

**Completeness map, run fresh.** `callback`, `memory`, `uptake`, `assistant register`, `brevity` and `word count` still appear **zero** times in §7, §8 and §9. `transparen` still appears zero times in §7 and §8. `16-trait` still appears once, in §7, and never in §8. The single occurrence of `disagree` anywhere in §7 is inside the list of apparatus Design is licensed to drop. Objectives 1 (circular half), 4 (transparency half) and 6 (licensing text) remain the three holes round 3 counted; two of them are now *worse*, because §7's only mention of each is a licence to remove its instrument.

None of the seven is a writing problem. All seven would propagate. Three of them would send a capped pass to build something that exists, or to trust an enforcement mechanism that isn't attached to the thing it is cited as enforcing.

---

## P0 — fix before sending

### P0-1. §7 Part B's "New: continuity-regression testing" already exists for all six worlds, has already been run, and its committed results show four of six worlds — including both lead acceptance worlds — already failing voice parity.

Brief §7 Part B, lines 857-866:

> *"**New: a continuity-regression-testing step, required before any future voice-affecting prompt change reaches a built world — including this rebuild's own output before it ships.**... Same probes, old prompt vs. new prompt, diff the actual voice — before merge, not after a complaint. This is the concrete mechanism Objective 5's 'self-sufficient' standard needs for voice specifically, the same way Part Eight's validation battery already exists for content."*

And §8, lines 919-928: *"**A continuity-regression pass on all six voices**, per §7 Part B's new requirement — same probes run against the current, unrebuilt prompt and the rebuilt one, diffed directly."*

`wrs/views/probe_parity.py`, opening docstring, verbatim:

> *"S2.8 probe-parity (P): **deployed prompt vs. generated prompt - same voice?** Pass 1 SS5.2's **continuity regression, run for real for the first time**... the world's validation probe set against both prompts, two independent trials, blind grading. Probes are held-out by construction... grading: per probe and trial, the two responses are presented as A/B in a seeded-shuffled order (grader never told which is deployed); grader must answer SAME-VOICE / DIFFERENT-VOICE on **register, measure, refusal behavior, and vocabulary**... verdict: parity holds if no probe gets DIFFERENT-VOICE on both trials."*

Its grader prompt states the criterion in the brief's own terms: *"the question is whether **a returning participant would experience the same person**."*

This is not one script for one world. Six are committed:

| Script | World | Committed result |
|---|---|---|
| `wrs/views/probe_parity.py` | Desert (Papnoute) | `probe_parity_result.json` → **PASS** |
| `wrs/views/s62_pahc_probe_parity.py` | PAHC (Chloe) | **PASS** |
| `wrs/views/s62_alx_probe_parity.py` | Alexandria (Theon) | **FAIL** |
| `wrs/views/s62_hal_probe_parity.py` | Hieronymian (Albina) | **FAIL** |
| `wrs/views/s62_ijc_probe_parity.py` | Imperial-Juridical (Marius) | **FAIL** |
| `wrs/views/s62_syr_probe_parity.py` | Syriac (Yausep) | **FAIL** |

Raw transcripts (`*_probe_parity_raw.jsonl`) and result JSON are both tracked in git. The HAL harness's own docstring: *"S6.2/HAL S2.8-equivalent probe-parity (P): **deployed Albina prompt vs the temporary record-assembled prompt - same voice?**... Probes are the HAL Phase-5 live-test participant questions VERBATIM (**eight of the Part Eight categories**: source-awareness, anachronism, confidence-under-thinness, frame-break, scholarly-framework, claim-laundering, naming-collision, relational-safety)."*

**Why this blocks.** Four separate things follow, all of them things Fable would otherwise spend capped budget re-deriving:

1. **The mechanism is not new.** §7 Part B asks Fable to add to the Construction Framework a step the project has already built, run, and committed results for. This is the third instance of the exact shape round 1's P0-4 caught (Part Five's readability floor already existed) and round 2's P0-2 caught (`AGREEING`/`OVER_PRODUCING` already existed). The brief cites `probe_parity.py` **twice** — §4 line 228 and §7 line 790 — both times only as a reason to keep `wrs/records/` in lockstep, never as the implementation of the thing §7 Part B calls new.
2. **Round 2's P1-5 is answered in the file, and the answer is bad for this rebuild.** Round 2 asked what a continuity-regression pass is *checking for*, since a successful rebuild must change the voice. `probe_parity`'s stated verdict rule — *"parity holds if no probe gets DIFFERENT-VOICE on both trials"* — **fails a successful register rebuild by construction.** The existing instrument's criterion is inverted for this use. That is a real decision Design has to make, and it is discoverable only by opening a file the brief already cites.
3. **The pre-rebuild baseline already exists and is already failing.** Four of six worlds' deployed prompts do not read as the same voice as their own record-assembled prompts. Albina is world #1 in §7's sequence and Marius world #2; both FAIL. §4's lockstep bullet (lines 226-234) presents record/deploy desync as a hazard the rebuild must avoid creating. It has already happened, it has been measured, and the measurement is in the repository.
4. **It is also the naturalness/register instrument §7 Part B says Part Eight lacks.** §7 Part B correctly notes Part Eight has no naturalness category and asks for one, then says *"'naturalness' needs to be more than a probe category name; §8 below names the actual instruments."* `probe_parity`'s grader is a four-axis register rubric (register / measure / refusal / vocabulary) built on Part Eight's own probe categories. That is closer to the instrument being asked for than anything §8 names.

**Fix.** Rewrite §7 Part B's continuity-regression bullet: the mechanism exists (`wrs/views/probe_parity.py` and its five `s62_*` siblings), it has been run on all six worlds, and the committed verdicts are 2 PASS / 4 FAIL. What Part B should require of the Framework is not the step but its *promotion* — from a migration-era staging tool to a standing pre-merge gate — plus the pass criterion this rebuild needs, which is not `probe_parity`'s current one. Give §8's bullet the same correction and cite the existing result files as the baseline. Add the 2-PASS/4-FAIL finding to §5 as a measured fact about the six builds, and reconcile it with §4's lockstep bullet, which currently describes as a future risk something that has already occurred in four worlds.

---

### P0-2. `readability_check` is not wired to Representative voice anywhere in the codebase. §7 Part B's "both ends are real and wired" and §8's "already built, already wired" are false as applied to voice, and Part Five's real gap therefore *does* include enforcement — the thing round 1's P0-4 talked this brief out of.

Brief §7 Part B, lines 816-821:

> *"Both ends are real and wired: `wrs/parameters.yaml:101-114` (the canonical numbers, sourced to this exact Part Five passage) and `wrs/gates/core.py:211` (`readability_check`), which hard-fails rather than silently passing when it can't check. **The open question this brief cannot answer and must not guess at: has this gate actually been run against the six current builds.**"*

Brief §8, lines 890-894: *"**`readability_check` (`wrs/gates/core.py:211`)** — already built, **already wired to Part Five's own numbers**."*

Every caller of `readability_check` in the repository, enumerated:

| Caller | What it measures |
|---|---|
| `wrs/views/plain_explanation.py:174-175` | the **Level-2 plain-explanation render for a lexicon term** — Article 30's transparency surface, not a Representative turn |
| `wrs/gates/run_gates.py:139-141` | three **test fixtures** (`READABLE_TEXT`, `UNREADABLE_LONG`, `UNREADABLE_JARGON`) — a self-test that the gate works |
| `wrs/gates/core.py:244` | internal, inside the module |

There is **no code path anywhere** that runs it against a permanent prompt, a World Capsule Core, a `voice_profile` record, or Representative output. And the record layer says so in its own words. Every world's `voice_profile` record carries a `reading_level_check` field whose entire content is (`wrs/migrate/s27_voice_records.py:208-210`, and identically in `s62_hal_s27.py:400-402`, `s62_alx_s27.py:308`, `s62_pahc_s27.py:447`, `s62_syr_s27.py:371`):

> *"inherits reading_floor from wrs/parameters.yaml (Flesch-Kincaid grade band 8-10, Reading Ease >= 60; CO-015) — **a pointer, not a restatement**"*

`plain_explanation.py`'s own docstring is equally explicit about the gate's scope: *"the machine check verifies **the authoring** [of the plain_explanation field], it never manufactures plainness... computed at render time on every render, always."*

**Why this blocks.** Four consequences:

1. **§9 task (c)'s question is answerable in one grep, and the brief forbids answering it.** *"Confirm whether `readability_check` has ever actually been run against the six current builds — a fact this brief could not establish and must not be guessed at"* (lines 1023-1025). It is not a guess: nothing wires the gate to a voice artifact, and `run_gates.py` exercises it only against fixtures. The honest answer is "no, and it cannot be without new code." That converts §9's cheapest Research task from *go find out* into *wire it*, and it frees the Research budget the brief spends on it.
2. **§7 Part B's central argument inverts.** Round 1's P0-4 blocked on *"give Part Five concrete operational teeth"* because the teeth existed. They exist — for Level-2 lexicon plain-explanations. For the Representative voice, which is what this entire brief is about, there is no enforcement at all: only a parameter file and a record field that points at it. §7 Part B currently tells Fable *"Part Five's real gap is narrower than 'no operational teeth'"* and lists four content additions. The gap is wider than that, and the missing piece is exactly the one round 1 removed.
3. **Two cross-references misresolve on the strength of this.** §4 line 233 (*"the record layer the gates (**including the readability gate in §7 Part B**) read"*) and §7 line 790-792 (*"`wrs/views/probe_parity.py` and **the readability gate (§7 Part B)** compare against the record layer, and a `data/`-only edit desyncs the two"*). `probe_parity` genuinely does compare deployed against record-assembled. The readability gate does not compare anything against the record layer, never touches `voice_profile` records, and never reads a permanent prompt — so a `data/`-only edit desyncs nothing it reads. §4's lockstep argument is correct for one of the two gates it names and wrong for the other.
4. **§6 Objective 3's whole "real, unresolved tension" rests on an artifact the brief never specifies.** The tension is derived from Albina's **23.6 words/sentence**, which is her *pilot output*. Measured independently, her **permanent prompt** runs 20.6 words/sentence at 1.444 syllables/word → **FK 9.5 / FRE 63.7 — inside the band, passing.** §8 says run the gate on "baseline and rebuilt **output**"; §9(c) says run it "against the six current **builds**... and specifically against Albina's"; §7 Part B and §4 tie the gate to the **record layer**. Three different artifacts, three different verdicts. If Research runs it on her prompt she passes and §6's declared values-level decision evaporates; if on her output she fails. The brief's own decision gate is ambiguous on the single input that decides its outcome.

**Fix.** Replace *"both ends are real and wired"* with what is actually wired: the numbers are canonical in `parameters.yaml:102-114`, and the gate is live — on the Level-2 plain-explanation render, not on Representative voice, where the record layer carries a pointer rather than a check. State that no code path measures a permanent prompt, a capsule, or a Representative turn. Move §9(c) from "find out whether it's been run" to "wire it and run it," and say explicitly which artifact §8's Objective-3 instrument measures — prompt, capsule, or output — because §6's Albina decision hangs on the answer. Then restore enforcement-for-voice to Part Five's list of real gaps in §7 Part B.

---

### P0-3. §7 Part A's clean-rebuild mandate contradicts §4's freeze list, its own bullets, and its own scope.

The governing paragraph, lines 674-686, is new and has never been checked. Read against the rest of §7 Part A start to finish, and against §4, it collides in five places.

**(a) It instructs Design to rewrite the three things §4 puts on the do-not-rebuild list, by name.**

> §7 Part A, lines 756-757: *"**Write each world's identity, era, vocabulary, register, and reasoning-mode content fresh** from its actual sources."*
>
> §4 (*"What NOT to rebuild"*), lines 189-192: *"**Historical identity, era, and vocabulary content** in every permanent prompt — who each Representative is, what span they speak from, their world's real terms. This rebuild changes how something is said and what gets reached for, never the facts being spoken."*

Same three categories, same noun (*content*), opposite instructions. The pre-`fa10bdf3` wording was compatible with §4 — *"Full diction/rhythm audit of both files... identity, era, and vocabulary paragraphs carry the same stylization"* — a rhythm pass over paragraphs whose facts are frozen. The rewrite converts that into writing the content itself, which is a scope expansion into §4's freeze list. The rest of the sentence still gestures at the old intent (*"not an audit of the existing paragraph labeled 'how you speak'"*), so a Fable reader gets both readings in one bullet and no rule for choosing.

**(b) The paragraph is written entirely in per-world terms but claims to govern two bullets that have no world.**

> *"read this before writing anything, **it governs every bullet below**... **It starts from the world's actual sources** — lexicon chunks, story chunks, the World Capsule Core's own content, the Source Registry."*

The first bullet below it is *"**Pilot first, isolated.** Rewrite the shared `_HOW_YOU_ENGAGE` block (`representative_prompts.py:5-76`)"* — a **shared, world-independent** block with no world sources to be derived from. The third is the Facilitator's three "distinct from period diction" occurrences — also world-independent. The governing paragraph cannot govern two of §7 Part A's three top-level bullets, and it is the pilot bullet that ships first.

**(c) "No comparative diffing" collides with two live preservation instructions.**

> §7 Part A, lines 682-684: *"**No comparative diffing against the current prompt is part of the design process itself.**"*
>
> §4, lines 256-260: *"the one real length instruction *is* inside the block being rewritten, so **§7 Part A's edit has to preserve 'A Turn Has a Measure' deliberately**."*
>
> §7 Part A, lines 736-738: *"the shape repertoire from objective 2 **folded into the existing 'Let the Question Set the Shape, Not a Habit' section** as one option among several."*

Deliberately preserving a named paragraph from the current block, and folding new material into a named existing section, are both edit operations that require reading and matching the current text. §4's instruction was round 3's highest-consequence fix — it exists precisely to stop "A Turn Has a Measure" being deleted by accident — and the new mandate's phrasing works against it. The brief added a §8 note distinguishing verification comparatives from design comparatives (lines 923-928), which is a good and necessary note, but it does not reach these two, which are inside the design process.

**(d) "Re-included as given, not rebuilt" is stricter than §4 and works against Objective 3.**

> §7 Part A, lines 763-765: *"Content, fabrication-guard, and witness-not-recruitment blocks untouched — **these are re-included as given, not rebuilt**."*
>
> §4, lines 185-188: *"leave its content alone; **it's fine if register work touches its sentence rhythm** the same way it touches surrounding prose."*

§4 explicitly permits register work on the witness-not-recruitment block's rhythm; §7 Part A now forbids it. Measured, those blocks run roughly 190-400 words per file — **6 to 12 percent of each permanent prompt** — and they are written in each file's existing elevated register (Albina's, at `:21`: *"Our fierceness, where we have it, is directed at a wrong word in a sacred text and at a wealth that will not open its hand"*). Under a clean rebuild, that means every freshly written, plain-register file carries a verbatim block of the old register, in six of six files. §5(A)'s entire diagnosis is that the register problem runs through more surface than the "how you speak" paragraph; freezing 6-12% of that surface verbatim reinstalls the thing the rebuild is removing.

**(e) The source list omits the layer the project's own generator builds from, and names one artifact that does not exist for worlds #1 and #2.**

`wrs/views/permanent_prompt.py`'s own docstring: *"S5.2 - **the real §5.1 Permanent Prompt assembly**... Every part named, **sourced from records**, carrying eviction_priority and cache_stability... **Deterministic: same records -> byte-identical outputs.**"* It also declares, in its own words, exactly the leak class §5(B) is about: *"What never enters generation context (§5.1): world_meaning scholarly bodies, key_sources apparatus, **Author-Gravity notes, gravity codes**, Modern Hearing analysis — the segment renders read voice-register fields only, **through the shared apparatus-stripping helper**."*

So the project already has a record-sourced, deterministic, apparatus-stripping prompt builder — the literal implementation of "build fresh from sources rather than edit the current prompt" — and §7 Part A's mandate does not mention it. Its source list names four `data/`-side artifacts and omits `wrs/records/<world>/` entirely, even though every world has a full record set (`term`, `story`, `figure`, `quote`, `source`, `force`, `gravity`, `contested_claim`, `demonstration`, `voice_profile`, `world_core`).

This matters for direction, not just completeness. §4's lockstep bullet resolved round 1's P1-1 with "records follow the deployed prompt, update after" — a decision made for an **edit pass**. Under a clean rebuild from sources, the project's own tooling runs the other way: records → generated prompt → parity check against deployed. §4's decision and §7's new mandate now pull opposite directions on the same files, and nothing reconciles them.

And one of the four named sources is missing where it is needed first. Checked directly, `data/` carries a source registry for **three** worlds only — `desert_world/sources.json`, `pahc_world/source_registry.json`, `syriac_world/source_registry.json`. **Alexandria, Hieronymian and Imperial-Juridical have none.** They have `wrs/records/<world>/source/` records (37, 26, 41 respectively) — in the layer the mandate omits. So Design, following the mandate literally against the tree §7 points at throughout, begins world #1 (Albina) and world #2 (Marius) with one of its four named inputs absent.

**Fix.** Five edits, all small. Scope the governing paragraph explicitly to the per-world passes and say what governs the shared-block and Facilitator bullets instead. Reconcile "write identity/era/vocabulary content fresh" with §4 — the honest form is "re-derive the *prose* that carries these facts from sources; the facts themselves are frozen (§4)." Carve the two named preservation instructions out of the no-comparatives rule the way §8's continuity note already carves out verification. Align "re-included as given" with §4's actual allowance on witness-not-recruitment rhythm, or change §4. Add `wrs/records/<world>/` and `wrs/views/permanent_prompt.py` to the source list, note that the source registry lives in the record layer for three of six worlds, and re-decide §4's lockstep direction now that Part A is a rebuild rather than an edit.

---

### P0-4. The cost/complexity license is incoherent against §4 and §6: it licenses dropping the only instrument for each of the two declared non-negotiables, names a shipped and protected mechanism as droppable, and both closes and re-opens `over_settling`'s scope inside one paragraph.

Brief §7 Part A, lines 704-723, entirely new in `fa10bdf3`:

> *"This brief's own three adversarial-review rounds added real apparatus this week: **readability enforcement, fabrication-rate tracking, per-signal drift telemetry, three-level-sourcing checks, sustained-disagreement probes, continuity-regression testing.** None of it is fixed by default just because this document names it — **Design has explicit license to question, simplify, or drop any of it** if it doesn't earn its cost and complexity... This does **not** extend to the no-fabrication apparatus, the witness-not-recruitment block (§4, untouchable under any framing), or the existing governance layer (`over_settling`, `citation_grounding`, `drift_detection` — §4, already justified as content-based, **not up for reconsideration here**). One real, already-measured tension worth naming rather than silently resolving either way: `over_settling_adjudication`'s second-stage check is **the single largest invisible cost line item after the main response itself (§4, 10-of-12-turns finding)**, and §4 currently treats fixing the check itself as out of scope. **Now that lowering cost and complexity is an explicit goal of this rebuild, Design should raise this tension with Mark directly** rather than assume either 'still out of scope' or 'now in scope.'"*

Six distinct problems, all in one paragraph.

**1. It licenses dropping the only instrument for each of §6's two non-negotiables — by name.** §6 lines 535-539: *"Two parallel, non-negotiable priorities — neither one waits on the other, and **either one failing fails the whole program**: Objective 3... and Objective 4."* §8 line 899-900 says the fabrication rate *"is the actual instrument for Objective 4, one of the two parallel non-negotiable priorities named in §6, **which had no metric at all before this revision**."* §8 line 893-894 says `readability_check` *"is the instrument that actually tests Objective 3, **which no metric named here tested before this revision**."* The licence's first two items are "readability enforcement" and "fabrication-rate tracking." Round 1's P0-8 and P1-7 existed because Objective 4 had no metric; this paragraph re-opens that hole by name, and opens the same one on Objective 3.

**2. §6 describes this licence as an Objective-3 protection; it is a symmetric deregulation of everything.** §6 lines 553-554, new in `6fcb15bc`: *"see Part A's cost/complexity license (§7), **which exists precisely so this tradeoff doesn't happen by default**."* The licence as written does not protect Objective 3 — its first named droppable item is Objective 3's only instrument, and it applies equally to Objectives 4, 5 and 6's instruments. The pointer resolves to a section that does not say what it is cited for.

**3. "Three-level-sourcing checks" has no referent except the shipped mechanism the brief protects.** The string `three-level` appears exactly twice in the document: here, and in §6 Objective 4 (lines 647-655) — *"the existing three-level transparency mechanism (Article 30: inline in the text, hover for a summary, click for full detail — **already built**, `CitationMarker`/`LexiconHighlight`) has to keep working honestly through this rebuild... **both are this thread's job not to make worse**."* No new "sourcing check" is proposed anywhere in §7, §8 or §9 (round 3's P1-3 asked for one; it was not added — `transparen` still appears zero times in §7 and §8). So the only thing in this document that answers to the name is a built, shipped, Article-30-derived mechanism that §6 Objective 4 declares **"not separable from"** no-fabrication and that this same paragraph claims to protect two sentences later. The licence's most natural reading is a permission to simplify or drop the transparency half of a non-negotiable.

**4. The list's own premise is false for at least one item.** *"This brief's own three adversarial-review rounds added real apparatus this week"* — the Article 30 three-level mechanism was not added this week by a review round; it predates the brief and is already in the frontend. (And per P0-1 and P0-2, continuity-regression testing and readability enforcement were not added by the review rounds either; they were *found* by them, already built.)

**5. The paragraph closes and re-opens `over_settling` in three sentences.** *"not up for reconsideration here"* → *"Design should raise this tension with Mark directly rather than assume either 'still out of scope' or 'now in scope.'"* One of those two sentences has to go.

**6. It attributes a cost ranking to §4 that §4 does not make.** §4's entire statement on this (lines 270-275) is: *"`over_settling_adjudication` fired on 10 of 12 turns in this session's live test — not a rare safety net in practice. Worth watching (§8)... but fixing the check itself is out of scope here."* **§4 contains no cost claim at all.** "The single largest invisible cost line item after the main response itself" traces to the Decision Log's own cost table, not to §4. This is a fresh instance of exactly the defect round 3 logged as P2-9 (§8 attributing to §4 a framing §4 doesn't carry), which is itself still unapplied — so the document now misattributes to §4 twice, in two different sections, on the same subject.

**7. "Lowering cost and complexity is an explicit goal of this rebuild" is not established anywhere.** §6 enumerates six objectives and a priority structure; none of them is cost. §1 and §2 do not mention it. The claim is introduced by this paragraph and then used as the premise for reopening §4's scope decision. If cost reduction is genuinely a goal of this rebuild — and Mark's own Decision Log framing ("it costs too much") suggests it may be — it belongs in §6 with a stated rank, not asserted mid-§7 as already settled.

**Fix.** Rewrite the licence with three lists instead of two: (i) genuinely droppable — per-signal drift telemetry, the term-reclarification tally, the 16-trait rubric adaptation, the sustained-disagreement probe's *form*; (ii) not droppable, because §6 makes them program-ending — the fabrication rate and whatever instrument ends up testing Objective 3, though *which* instrument is open; (iii) untouched and out of scope — the no-fabrication apparatus, the governance layer, and Article 30's three-level transparency, which is not a review-round addition and does not belong in a droppable list under any name. Delete "three-level-sourcing checks" or rename it to whatever new check is meant, and say where in §8 that check lives. Resolve the `over_settling` sentence one way. Re-source the cost claim to the Decision Log. And if cost is a goal, put it in §6.

---

### P0-5. §7 Part A's leak filter was rescoped from round 3's general rule into a two-item enumeration, and the enumeration misses 17 chunks — including half of Papnoute's entire lexicon corpus and verbatim builder-facing text in an acceptance world.

Round 3's P0-4 fix instruction was explicit about the scope: *"Reword §7 Part A's filter from 'Ecological Function fields carrying build-process vocabulary' to '**any build-process, template, or lexicon-bookkeeping language reaching generation from a retrieved chunk, wherever it sits in the file**.'"*

What `0b4d19d2` wrote instead, §7 Part A lines 729-735:

> *"**filtered for the two real risks finding B names — roughly a quarter of Ecological Function fields carrying internal build-process vocabulary ("Tensional gravity," "candidate... tested"), and a handful of chunks with no Key Sources marker at all whose entire body, internal notes included, passes through unfiltered — neither is topical material safe to lead with**"*

Two enumerated patterns, in place of the general rule. Measured against what actually reaches the model — real serialisation path executed, section scan handling **both** of the codebase's conventions (`## Heading` and blank-line-preceded `**Label:**`, per `sections.py:42`), build vocabulary defined tightly as `Doc_NN` references, gravity codes and names, `L4-Templates`/`Deployment_Lexicon` paths, template-instruction language, claim IDs, and the `hal_lex11` audit phrasing:

| | chunks |
|---|---|
| lexicon chunks total | 118 |
| **leaking build-process metalanguage into generation context** | **46** |
| covered by pattern 1 (leak sits inside the `Ecological Function` field) | 27 |
| covered by pattern 2 (no `Key Sources` marker, whole tail passes) | 6 |
| **covered by neither** | **17** |

Where the 17 sit, and in whose worlds:

| World | Representative | Chunks | Section carrying the leak |
|---|---|---|---|
| **Desert** | **Papnoute** | **9 of his 18** | `World Meaning` (7), `Distortion Risk` (2) |
| Alexandria | Theon | 5 of 50 | `World Meaning` |
| **Imperial-Juridical** | **Marius** | 3 of 12 | `Plural-Voices Note` |

Verbatim, reaching generation on Marius's *primatus* — one of that world's most central terms, in a world §8 names as primary acceptance evidence (`ijclex001_primatus.md`, `## Plural-Voices Note`, confirmed by executing the path):

> *"This entry is written from Strand A's own voice specifically... per **Doc_01's three-strand finding**... **This is a lexicon-organization device for construction and runtime-retrieval purposes only — it is not, and does not pre-decide, a Representative voice or identity decision.** Which strand (if any) an eventual Representative speaks primarily from... is **Step 10's own decision, not settled by this document (see Doc_06 §5, Open Item 4)**."*

The same text is in `ijclex002_presbeia.md` and `ijclex005_imperator_intra_ecclesiam.md`. And on Papnoute's side, `desertlex011_apatheia.md`'s `World Meaning`, verbatim: *"Strand-C-bound in this technical sense (**Doc_06 §2.2; Doc_04 gravity 9, Supporting on Persistence grounds**)."*

**Why this blocks.** §7 Part A's filter is the only defence the brief builds against this, and §4 freezes the chunks so nobody in the thread may fix them at source. A filter written to two enumerated patterns is a filter that will be *implemented* to two enumerated patterns. Executed as written, it catches `hal_lex11`, catches the six markerless tails, and leaves a Representative free to speak from a `World Meaning` section that says "Doc_04 gravity 9" — in half of Papnoute's corpus, and in the three IJC entries carrying the most explicit builder-facing sentence in the whole lexicon. §4's own carve-out defect #1 already names participant-visible build-process leakage as a real, logged defect; this is the same defect on the generation path, wider than the brief states.

Note also that the project already holds the correct general rule. `wrs/views/permanent_prompt.py`'s docstring names the exclusion set for the prompt-assembly path — *"world_meaning scholarly bodies, key_sources apparatus, Author-Gravity notes, gravity codes, Modern Hearing analysis... through the shared apparatus-stripping helper"* — and `gravity codes` is exactly the class leaking through the *retrieval* path. The concept exists, is named, and is implemented on one path and not the other.

**Fix.** Restore round 3's general rule: filter for any build-process, template, gravity-code or lexicon-bookkeeping language reaching generation from a retrieved chunk, **wherever in the file it sits**, and keep the two enumerated patterns as worked examples of it rather than as the scope. Add the 46/17 measurement and the three-world distribution to §5(B). Name Papnoute — currently the only world the brief never associates with this leak, and the one with the highest rate. And give the Research stage the question round 3 asked for and this commit did not carry: whether the right fix is a retrieval-side apparatus strip modelled on `permanent_prompt.py`'s existing helper, rather than a prompt-side instruction to the voice, since §4 freezes the chunk content.

---

### P0-6. §6 Objective 3's new positive paragraph and §8 now contradict each other on whether `readability_check` tests Objective 3; the objective's stated goal has no instrument anywhere; and the paragraph's opening sentence is broken exactly where ambiguity is most expensive.

The insertion, §6 lines 589-599, new in `6fcb15bc`, read as a builder or participant would meet it — mid-list, ahead of the existing constraint text:

> *"3. **Stated positively first, because the constraints below exist to serve this, not to replace it:** the conversation itself has to read and engage the participant as a real modern person, with genuine insight and connection — honest, drawing out the truth and the participant's own perspective, carrying the world's actual uniqueness, natural and deep and authentic, not a performance of any of those things. **Plainness and readability (below) are what make that possible, not the goal itself — a conversation can hit every readability number and still fail this objective completely** if it isn't actually insightful, connected, or honest company. Sentences read as plain, real, everyday spoken English — not costume diction — while keeping each world's genuine imagery, vocabulary, and actual distinctiveness as seasoning, not performance."*

**The direct contradiction with §8.** §8 lines 890-894: *"Run it against baseline and rebuilt output for all six worlds; **this is the instrument that actually tests Objective 3**, which no metric named here tested before this revision."* §6 now states, in its own words, that hitting every readability number is compatible with failing Objective 3 completely. Both cannot be true. This is precisely the shape round 3 rated P0-5 — §6 restructured, §8 left carrying the pre-restructuring version — and round 3's fix note said in terms: *"Then re-read §8's `readability_check` bullet in the same light."* `0b4d19d2` fixed the fabrication bullet and left the readability bullet, and `6fcb15bc` then made the contradiction explicit rather than latent.

**The instrument hole this opens on half the program.** Objective 3 now carries a stated goal — insight, connection, drawing out the participant's own perspective, depth, authenticity — and §6 says it is exactly as program-ending as Objective 4. Nothing in §8 measures any of it. §8's instruments are readability (which §6 has just disclaimed as a test of the goal), the fabrication rate, the over-settling confirmed rate, a per-signal drift breakdown, a term-reclarification tally, a continuity-regression pass, a sustained-disagreement probe, and two Part Eight categories. Not one bears on insight, connection, or depth. And §7's cost/complexity licence (P0-4) permits dropping the one instrument that at least measures the constraint. Half the program, declared non-negotiable, is now unfalsifiable by §8's own standard — *"Every prediction this brief or its Research stage makes needs to be falsifiable by an instrument actually named here"* (lines 881-882).

**§6's new rule condemns §6's own floor.** The tier paragraph, lines 549-553: *"Every governance or verification instrument named in §7/§8 is answerable to this: **if a check or a rule is making conversation *more* restrictive without making it more honest, that's an Objective-3 failure the apparatus itself caused**."* Apply that to the FK 8-10 floor Objective 3 itself mandates nine lines later "as an access requirement, not a style suggestion": the floor makes conversation more restrictive and does not make it more honest — its justification is *access*, not honesty. Under §6's own new test, §6's own floor fails. The rule needs "without making it more honest **or more accessible**," or it reads as a standing licence to drop the readability floor, which is the item the §7 licence lists first.

**The sentence itself does not work.** *"the conversation itself has to read and engage the participant as a real modern person"* is a zeugma: *"engage the participant as a real modern person"* parses with the phrase modifying *the participant*; *"read... as a real modern person"* requires it to modify *the conversation*, which is not a person. The two verbs are yoked to an object phrase only one of them fits. Worse, the salvageable reading — the conversation should *read as* a real modern person — says the Representative should sound modern, which contradicts the same objective's next clause (*"keeping each world's genuine imagery, vocabulary, and actual distinctiveness"*), §1's *"real adaptation, not translation-as-dilution"*, and §1's explicit statement that *"the Representative is speaking to a person who lives now, not to someone from its own world."* The ambiguity sits on exactly the axis §1 identifies as having two real failure directions, at the head of one of the two objectives §6 says either one of which failing fails the program.

Three smaller problems in the same insertion: the numbered list loses parallelism (items 1, 2, 4, 5, 6 open with the requirement; item 3 now opens with an editorial note about the ordering of its own sentences); *"not a performance of any of those things"* and *"as seasoning, not performance"* say the same thing four lines apart; and *"the constraints below"* is ambiguous between the rest of objective 3 and objectives 4-6.

**Fix.** Rewrite the opening sentence so the subject and the comparison agree — e.g. *"the conversation has to land for a participant who lives now: genuinely insightful, connected, honest company, drawing out their own perspective while carrying the world's actual uniqueness."* Correct §8's readability bullet to say what it actually is — the instrument for Objective 3's *readability floor*, a necessary condition, not a test of the objective — and either name an instrument for the positive half (a rated transcript rubric is the obvious candidate, and §7 Part B's 16-trait rubric is the one already in the document) or state plainly that the positive half is judged, not measured, and say by whom. Repair the tier paragraph's rule to include accessibility. Drop the duplicated "performance" clause.

---

### P0-7. §8 and §9 still tell Fable one review round has happened and a second is warranted; §7 says three; and §8 sends Fable to the round-1 review as the account of record, a document rounds 2 and 3 falsified.

Three statements, all in the current text:

> §7 Part A, line 706: *"This brief's own **three** adversarial-review rounds added real apparatus this week."*
>
> §8, lines 967-973: *"this brief's own **round-1** Opus adversarial review found and corrected eight send-blocking errors in the draft that preceded this one; **read it directly** (`...Round1_2026-08-06.md`) **for the full account of what changed and why**, not just this revised text."*
>
> §9, lines 1073-1083: *"**Round 1** of this brief's own required Opus adversarial pass ran on 2026-08-06... verdict: not ready, eight send-blocking defects, all applied directly to this document... **a round 2 pass checking this fix itself is still warranted before Friday** — a rewrite this size is exactly the kind of pass most likely to introduce a new citation error while correcting the old ones, and round 2 exists to catch that."*

Rounds 2 and 3 are committed files (`.../Round2_2026-08-07.md`, `.../Round3_2026-08-07.md`). Neither is cited anywhere in the brief. Round 4 is this document. Grepped: the only round references in the brief are to round 1, plus the unrelated System Redesign round-3 precedent, plus §7's bare "three."

**Why this blocks.** §8's pointer is an instruction to Fable to read a superseded document as the record. Round 1's *"What verified clean"* section states, as verified: *"`## CT Contest Type` and `## Related-Terms Reciprocity Note` sit after `## Key Sources` in the chunk files, **so they are stripped from generation context**."* Round 3's P0-4 falsified that for six chunks and this brief's own §5(B) now carries the correction. Round 1's P0-6 states 109 of 118; §5(B) now says 107. Round 1's P0-4 argues Part Five's readability enforcement already exists; P0-2 above shows it does not exist for voice. A Fable pass following §8's instruction reads three claims the brief itself has since corrected, with no superseding note — which is exactly the failure §3 spent two rounds fixing for the Decision Log, and fixed well: *"**Treat that entry's entire findings list as superseded**, not just the two lines its own note marks."* The discipline was applied to the Decision Log and not to the review record, and §9 then compounds it by telling Fable a review that has already happened twice over is still to come.

There is a second-order cost. §9's paragraph is the brief's own statement of how much scrutiny it has survived. Understating it by three rounds undersells the document to the reader who most needs to know — and overstating what round 1 settled is the same class of error as the Decision Log's original "verified directly against the code rather than guessed" header.

**Fix.** Replace §9's round-1 paragraph with the real sequence: four Opus adversarial rounds, 2026-08-06 to 2026-08-07, findings applied in `e2eb7f7a`, `f60a112b`, `b20005c4`, `0b4d19d2`; cite all four audit files. Change §8's pointer to the most recent round, or to all four with a note that earlier rounds' "verified clean" items were themselves corrected by later ones — the same superseding language §3 already uses. Align §7's "three" with whatever the count becomes.

---

## P1 — materially improves, not disqualifying

### P1-1. The Albina arithmetic fix is right in its conclusion and overclaims in its illustration — the comparison it offers is false for two of the five prompts it compares against.

Brief §6, lines 619-624:

> *"`readability_check` computes Flesch-Kincaid from exactly two variables — words per sentence and syllables per word. At Albina's measured 23.6 words/sentence, passing the grade-10 ceiling requires roughly 1.39 or fewer syllables per word on average — ***simpler* vocabulary than any of the other five prompts currently run** (they measure 1.34-1.47), not richer."*

**The load-bearing half is exactly right and re-derives cleanly.** FK = 0.39·(w/s) + 11.8·(syl/w) − 15.59 is a function of two variables; at 23.6 w/s, FK ≤ 10 requires syl/w ≤ **1.3886** — "roughly 1.39" is exact. Richer vocabulary raises FK and lowers FRE; clause structure is invisible to both formulas; sentence length is the only lever that helps. The withdrawal of the incoherent "clause richness and vocabulary" fix, and its replacement with an explicit unresolved-tension statement plus a §9 decision gate, is the right call and the best single repair in `0b4d19d2`.

**The illustration is wrong.** Measured independently (my own syllable heuristic, hence small differences from round 3's figures):

| Prompt | words/sent | **syl/word** | FK | FRE |
|---|---|---|---|---|
| **Theon** | 16.4 | **1.348** | 6.7 | 76.1 |
| Chloe | 16.0 | 1.406 | 7.2 | 71.7 |
| Yausep | 23.8 | 1.429 | 10.6 | 61.8 |
| Marius | 27.4 | 1.436 | 12.0 | 57.5 |
| *Albina* | *20.6* | *1.444* | *9.5* | *63.7* |
| Papnoute | 20.8 | 1.491 | 10.1 | 59.6 |

Theon's prompt runs at **1.348** — below the 1.389 Albina would need. On round 3's own table (Theon 1.34, Chloe 1.39) it is false for two of the five. Round 3's careful wording was *"simpler than the project's current average"*, which is true (average ≈ 1.42); the fix commit upgraded it to *"simpler than any of the other five,"* which is not. In a paragraph whose entire authority rests on being arithmetically careful, and which a Design reader can check in five minutes, the overclaim costs more than its size.

Two further things the same table shows, both of which round 3 raised as P1-4 and neither of which was applied: **Albina's prompt is the third *most* accessible of the six and passes the band at FK 9.5**, while Marius's fails it worst at FK 12.0; and the 23.6 w/s the whole tension is built on is her *output*, not the artifact §7 edits (see P0-2, consequence 4).

**Fix.** *"...requires roughly 1.39 or fewer syllables per word — below the average the six prompts currently run (≈1.42) and below four of the other five, i.e. simpler vocabulary, not richer."* And add the twelve-file measurement round 3 asked for, so §7's risk ordering answers to numbers rather than to one world's output.

### P1-2. §3's Persona Survey rewrite fixes the attribution and drops three things that cut against §7 Part A's now-expanded worked-example mandate.

The core repair is right and re-derives: doc 09's table at lines 299-307 is **5 required / 2 secondary**, and the brief's tally matches it source for source; *"So it is not unanimous"* is verbatim at line 309; the `mes_example` pruning quote is faithful at line 20; Microsoft's *"relegated to 'SCRATCH PAD'"* and IBM's *"Absent"* are exact; Anthropic's *"3–5 examples"* is exact at line 315. Round 3's P0-2 misattribution is genuinely gone from the load-bearing sentence.

Four residues, all pointing the same way:

- **The conflation survives in the tally sentence.** The brief counts Character.AI and the character-card ecosystem as *"two facts about **the character-card ecosystem itself**."* Doc 09 surveys them in different sections as different systems (§1 the hobbyist spec + SillyTavern; §2 Character.AI, a commercial product), and the brief itself distinguishes them correctly eight lines later (*"the Character Card *spec itself*, as distinct from Character.AI's own field limits"*). Corrected where it matters, uncorrected where it counts.
- **"One clean, single-direction, directly relevant data point" is doc 09's own complication.** Doc 09 files the 3-5 figure under *"Complications worth holding,"* item 2, verbatim: *"**Anthropic's own recommendation is 3–5**, and BlendedSkillTalk runs on two persona sentences. **More demonstration is not monotonically better.**"* The brief upgrades a stated ceiling into clean support.
- **Doc 09's most CiC-specific caveat is dropped, and §7 Part A just got bigger without it.** Complication 1, verbatim: *"**Examples can be copied rather than generalized from.** PersonaChat's revised-persona condition exists precisely because models 'unwittingly repeat profile information either verbatim or with significant word overlap'... **For a tradition with distinctive vocabulary, this is the live risk.**"* Six worlds with distinctive vocabulary is the entire subject of §5(A). `fa10bdf3` expanded the worked-example mandate from five files to all six, written fresh, and this caveat is nowhere in the brief.
- **The pruning rule is presented as a live complication for CiC when the project's own research says it doesn't bind.** `10_Fable_Conversational_Realness_Study_2026-07-24.md:42`: *"Long-context models with the full conversation in the prompt substantially outperform fact-extraction memory systems... **CiC is already doing this correctly.**"* There is no truncation stage for an ephemeral field to be evicted from. Round 2's P0-3 fix instruction and round 3's P0-2 fix instruction both asked for this clause; neither commit carried it. §9's Research stage is sent to doc 09 for this exact question.

And one thing this bullet states that nothing implements: *"What's actually unanimous across every source, for or against: **description or trait-adjectives come first, as the rubric**, and dialogue — where used — gets written and judged against them, never the reverse."* §7 Part A mandates six sets of worked example dialogues and contains no trait-rubric-first deliverable. §7 Part B's 16-trait rubric is the only candidate and is still absent from §8's instrument list (round 2's P1-2, third round unapplied). The brief carries the unanimous finding and builds the reverse of it.

*(Also unapplied, third round: doc 09:38 says instructions after history carry **"much"** stronger weight — a community spec's stated design rationale. §3 line 137 still says "measurably," and now adds "this one *is* a clean, single-direction finding, and independent, external confirmation.")*

### P1-3. §5(B) files four of its six named leak examples under the wrong mechanism, in the paragraph whose whole purpose is to distinguish the two mechanisms.

Brief §5(B), lines 342-353, first leak paragraph: *"First: at least a quarter of the **107 Ecological-Function chunks** carry internal build-process language... **Same pattern, different fields, in other worlds: `Related-Terms Reciprocity Note` in Yausep's `syrlex005`/`syrlex008`, `Confidence: Inferential-Thin` in Chloe's `pahclex012`/`pahclex013`.**"*

All four of those chunks are among the **11 with no `Ecological Function` field at all** — they are not in the 107 — and all four are among the **6 with no `Key Sources` marker**, which is the second mechanism, described in the next paragraph without naming them. The substance is right (that material does reach the model — I confirmed it by executing the path), but the mechanism attribution is wrong for four of six named examples, inside a paragraph headed *"Two distinct leaks, not one."* A reader checking `syrlex005` for a build-contaminated Ecological Function field will find no such field.

One smaller precision point in the same paragraph: *"their **entire body**... reaches the model verbatim"* — `excise_section(body, QUICK_MEANING_MARKERS)` still runs for all six migrated worlds, so Quick Meaning is removed. "Everything after the last content section" is the accurate form. And `Confidence: Inferential-Thin` is arguably not build-process language at all — *"asserted, not confirmed, by this world's own evidentiary base"* is exactly the epistemic honesty Objective 4 wants a Representative to have. The Syriac two are unambiguous bookkeeping; the PAHC two are not.

### P1-4. Objective 6's §7 gap is unclosed and now inverted: the only occurrence of "disagree" anywhere in §7 is in the list of apparatus Design may drop.

Counted fresh: `disagree` at lines 99 and 125 (§3), 668 (§6), **708 (§7 — the cost/complexity licence's "sustained-disagreement probes")**, 956 (§8), 1005 (§9). `pushback` at 507 (§5) and 662 (§6). `licens` at 45 (§2), 553 and 666 (§6), **and at 704 and 710 in §7 — both times meaning permission to *remove* apparatus, not the permission Objective 6 asks for.**

Objective 6 still demands prompt text — *"**Explicitly licensed**, not just permitted by omission"* (line 666) — and §7 is still where prompt text gets written and still writes none. This is round 2's P1-1 and round 3's P1-2, third round unapplied, with a new wrinkle: §8 will run a multi-turn agreement-pressure probe against six rebuilt voices, no build step was assigned to produce the behaviour, and §7's single mention of the probe is a licence to drop it. The word "license" now carries opposite meanings in §6 and §7, on the same objective.

### P1-5. Objective 1's circular/callback half still has no deliverable, no instrument and no Research task, and its §3 pointer is still the document's one unresolvable cross-reference.

`callback` appears once (line 575, §6). `memory` once (line 578, §6). `uptake` **zero times in the document**. All zero in §7, §8, §9. Round 3's P1-1, unapplied in full.

The pointer still does not resolve: §6 line 578 cites *"The Realness Study's 'proactive memory surfacing' finding (§3)"*, and §3's Realness Study bullet (lines 94-105) names persona-enactment, sustained disagreement, and three naturalness-collapse signals — nothing about memory or callbacks. The finding is real and sits at `10_Fable_Conversational_Realness_Study_2026-07-24.md:47`, which also supplies the mechanism and the cost: *"surfacing a callback ('you asked earlier about suffering — what we're saying now touches that') **needs zero new infrastructure, just prompt guidance.** This also directly serves comprehension: callbacks are how a human teacher builds understanding across a conversation."*

That last sentence now matters more than it did in round 3, because `6fcb15bc` made Objective 3's positive goal *"genuine insight and connection... drawing out the truth and the participant's own perspective"* — and doc 10's callback finding is the cheapest named mechanism in the entire research base for exactly that, in a brief whose §6 says Objective 1 is *"the mechanism that makes Objective 3 achievable."* It costs one bullet in §7 Part A and a counted tally in §8.

### P1-6. Objective 4's transparency half still has no deliverable and no instrument; its only §7 presence is a licence to drop it.

`transparen` appears at line 54 (§3) and 540/648/649 (§6) — **zero times in §7 and §8**. Round 3's P1-3, unapplied. §6 Objective 4 says transparent sourcing is *"not separable from"* no-fabrication and that both are *"this thread's job not to make worse by changing what citations actually carry."* Nothing checks that nothing got worse. §8's own harness already captures citations (*"every citation shown are real"*, line 938), so a before/after diff of what citations carry is nearly free. See P0-4(3) for why the licence makes this worse rather than merely unfixed.

*(Unapplied nit in the same objective, third round: the open placement question is rendered "per-turn marker vs. something closer to per-story"; `CitationMarker.tsx:10-13` says per-turn vs. **per-sentence**.)*

### P1-7. The fail-open `truncate_at` defect is documented in §5(B) and assigned to nobody, in a brief that also freezes the chunks it affects.

§5(B) lines 364-366 name it plainly: *"This is a real gap in what the project could otherwise treat as settled about how Key Sources stripping works — it only strips when it finds something to strip at."* Verified: `sections.py:159-160`, `return body if section is None else body[:section.start].rstrip()` — a fail-open on six chunks. §4 freezes chunk content, so no one in this thread may fix the six files; §4's *"two adjacent, already-diagnosed defects, deliberately not bundled here — log them for Mark's own separate triage"* list is the exact mechanism for this and was not used; §9's Research tasks (a)-(d) do not include it. Round 3's P0-4 fix instruction asked for precisely this assignment (*"whether the six chunks need a code-side fix (a general trailing-apparatus strip) rather than a prompt-side filter"*). A live code-level defect that puts internal build notes into generation context is now documented and owned by no one. With P0-5, the honest scope is a retrieval-side apparatus strip, and §4's defect list is where it belongs.

### P1-8. The record/deployment divergence §4 warns about has already happened, is already measured, and the measurement is in the repository.

§4 lines 226-234 present record/`data/` desync as a risk this rebuild must avoid creating. The committed `probe_parity` results (P0-1) show it has already occurred in four of six worlds — Alexandria, Hieronymian, Imperial-Juridical and Syriac all return `parity: FAIL` between the deployed prompt and the record-assembled one. Two of those four are §7's first two worlds and §8's two lead acceptance worlds. This bears directly on §7 Part A's clean-rebuild premise: a source-grounded rebuild's distance from the deployed voice is not a matter of speculation for these four worlds; it has been graded, blind, twice per probe, and written down.

### P1-9. Round 2's and round 3's unapplied P1s, listed for completeness — the two that matter most have become sharper.

- **The assistant register (round 2 P1-3, round 3 P1-8).** `assistant register`, `brevity` and `word count` still appear **zero** times. Doc 10's executive summary leads with it. §7 Part A's additions now include worked examples for **all six** worlds (up from five), a shape repertoire, bridge-first openings, and a callback mechanism if P1-5 is taken — all length-adding — against `_HOW_YOU_ENGAGE`'s "A Turn Has a Measure," which §4 now correctly identifies as the only brake and as sitting inside the block being rewritten. §8 still names no turn-length instrument.
- **The continuity-regression pass criterion (round 2 P1-5).** Now answered by the code (P0-1) and the answer is that the existing criterion fails a successful rebuild.
- Also still open: the 16-trait rubric required by §7 Part B and absent from §8 (round 2 P1-2); a first-sentence-uptake tally (round 2 P1-4); `mark_voice_simulation_results.json` still uncommitted while §5(C) rests four claims on it and §8's commit-a-durable-copy action still covers only the baselines (round 2 P1-6); the doc-07 build-time/runtime clause (round 2 P1-8); §9's fallback boundaries both sacrificing Part B / Objective 5 (round 3 P1-7).
- *Applied and confirmed:* round 3's P1-5 — §9 line 1006 now reads *"the Persona Framework Survey's genuinely mixed evidence on worked examples,"* aligned with the rewritten §3. Good catch by `fa10bdf3`.

---

## P2 — polish

1. **`wrs/parameters.yaml:101-114` should be `:102-114`**, in both §7 Part B (line 816) and §8 (line 891). Line 101 is blank; `reading_floor:` is at 102, and the block runs to 114. **Fourth round running.**
2. **§4's `wrs/parameters.yaml:116-121` is short of what it cites it for.** `drift_signal_count_emitted: value: 20` is at 116-117 and `source:` runs 118-123; the FLAG-016 history §4 cites lives in `notes:` at **124-130**. And "ten" is not flagged there as stale — the file describes it as a component of the 17 (*"10 monitor signals + anachronism alias + over_settling + 5 table-level checks"*). Round 3's P2-2, unapplied.
3. **§3's "the two lines its own note marks" is wrong; the log's note marks three.** `Decision-Log.md:31` supersedes bullet 1, bullet 4, **and bullet 5** (*"It also found 'the gap is enforcement, not philosophy' (bullet 5 above) is contradicted by Part Five's own text"*). §3's own list of superseded bullets (1, 2, 4, 6) also omits 5. Net effect is safe because §3's header instruction is "treat that entry's entire findings list as superseded." Round 3's P2-3, third round unapplied. *(Note the same log entry's open question — "whether that gate has ever been run against the six builds is still an open question" — is answered by P0-2 and should be updated with it.)*
4. **§7 Part B line 812 still says "the exact guidance §6/§7 believed they were inventing for Albina."** After `0b4d19d2` this is doubly stale: §6 no longer believes it, and §6 now says the operational reading of that guidance does not work. Round 2's P0-7, round 3's P2-5, unapplied.
5. **§8 line 904 attributes to §4 a framing §4 does not carry** — *"the raw `over_settling_adjudication` firing count §4 already names as expensive-but-expected."* §4 lists it under *"already-diagnosed defects"* and *"not a rare safety net in practice."* Round 3's P2-9, unapplied — and now duplicated in §7's licence paragraph (P0-4(6)).
6. **§4 line 203 retains "all content- or posture-based, not register-based"** for all twenty drift signals. `length_ceiling` is a declared `DriftSignal.signal_type` and is never named in the brief. Round 2's, third round unapplied.
7. **§8's parenthetical (lines 876-879) describing §9's gates names only the adversarial half**, not Mark's approval gate, which `fa10bdf3` made a co-equal requirement.
8. **§5(A)'s Marius quote is still a reversed-order composite.** Brief: *"one short sentence for the first fact. A full stop... Each one short enough to stand alone."* At `ijc_..._Marius.txt:117`, *"Each one short enough to stand alone"* comes **before** *"one short sentence for the first fact."* Verified again this round. Round 2's P2-3, third round unapplied — worth naming because composite quoting is a P0-class failure in this project's own history.
9. **§5(A)'s Theon quote still truncates silently.** Brief: *"You land one thing, and stop."* Actual (`:37`, verified): *"You land one thing, and stop, **and begin the next fresh**."*
10. **§5(C) still says "four separate points," then names a fifth** (lines 410, 430); §7 Part A line 740 repeats "four." Round 2's P2-5, unapplied.
11. **§3 still describes doc 09 as "(Character Card V1-V3, SillyTavern)"** (line 107) — the narrowest of the nine systems it surveys, and the slice both prior misattributions came from. Round 2's P2-7, unapplied.
12. **§6 Objective 3 says "not a performance of any of those things" and, four lines later, "as seasoning, not performance."**
13. **§9's Mark-gate paragraph and §7 Part A's clean-rebuild paragraph both claim primacy** ("the single most important process fact in this brief"; "read this before writing anything, it governs every bullet below"), alongside §1's "read this first, it governs everything below." Different scopes, so not a contradiction, but three governing claims in one document dilute each other.

---

## What verified clean

Stated plainly, because `0b4d19d2` is the most successful fix commit this document has had and the two restructuring commits get several things right.

**Round-3 P0-1 (§4's interview-vs-table bullet) — re-derived from scratch, correct in every particular.**

- `REACTIVE_TURN_GUIDANCE` is declared at `app/prompts/table_discourse.py:75`. **Exact.**
- Its refusal of a ceiling is quoted accurately: *"a real engagement is usually shorter than an opening statement, **but does not need to be brief for its own sake if there is a real view to add. And do not match your length to the turns around you**... **Speak at your own formation's measure even when it is conspicuously shorter or longer than what the last voice gave**."* **Verbatim.**
- `table_discourse.py` carries no per-world reasoning — its only world-specific content is `CROSS_WORLD_VOCABULARY_GUIDANCE` at `:57`, a terminology-borrowing prohibition. **Confirmed by reading the whole file.**
- *"A Turn Has a Measure"* sits at `representative_prompts.py:59-60`, inside `_HOW_YOU_ENGAGE` (declared at `:5`, closing at `:76`), and the quoted text is verbatim: *"default short: most turns are one to two short paragraphs, and a turn should almost never exceed three."* **Exact, including the line range.**
- `reactive_turn_guidance = ""` is at `nodes.py:1140`. **Exact.** Its own comment records the fold: *"Previously received its own PRIMARY_TURN_GUIDANCE block here; **folded into representative_prompts.py's always-present _HOW_YOU_ENGAGE instead** (Mark's own call, 2026-07-24/25)."* The asymmetry claim — solo turns get *less* injected guidance — is correct.

This was round 3's highest-consequence fix and it is now the single best-sourced bullet in §4.

**Round-3 P0-4 (§5(B)'s chunk measurements) — re-measured from scratch by executing the real serialisation path, exact.**

- **118** lexicon chunks; **107** carry a real `Ecological Function` section, located structurally rather than by string match; **11** do not. The brief's correction from 109 to 107, and its identification of `ijclex011_basilica.md` and `ijclex012_martyrium.md` as string-match false positives that mention the field only to record its omission, are both **exactly right**.
- **6** chunks return `None` from `find_section(body, KEY_SOURCES_MARKERS)` — `ijclex011`, `ijclex012`, `pahclex012`, `pahclex013`, `syrlex005`, `syrlex008`. **Reproduces exactly.**
- `truncate_at`'s fail-open is at `sections.py:159-160` as cited, and `ijclex011_basilica.md`'s serialised tail is verbatim what the brief quotes: *"## Final Assembly Instruction — Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0 (Tier 3: World Meaning brief, Ecological Function and Key Sources omitted per Template instruction). No brackets or builder notes remain. CT tag not applied."* **Confirmed by executing the path, not by reading it.**
- §8's corrected Theon figure — *"5 of 11 project-wide"* — is **exact** (Alexandria 5 of the 11).

**Round-3 P0-3 (the Albina arithmetic) — the withdrawal is right and the core derivation re-derives exactly.** FK is a two-variable function; 1.3886 is the true threshold at 23.6 w/s; vocabulary moves it the wrong way; clause structure is invisible to it. Withdrawing an incoherent resolution and replacing it with a stated tension plus a §9 decision gate — rather than writing a second fix that also doesn't work — is the single most disciplined judgement call in the whole fix commit, and it is the right one. (Its illustration overclaims; see P1-1.)

**Round-3 P0-2 (§3's Persona Survey) — the misattribution is genuinely gone.** The 32,000/500 figures are now correctly attributed to Character.AI's own field limits (doc 09:122-123); the Character Card spec's `mes_example` pruning rule is quoted faithfully from doc 09:20 and stated separately; the 5-for/2-against tally matches doc 09's table source for source; Google, Alexa and Salesforce are now named; Anthropic's 3-5 is carried. (Residues at P1-2.)

**Round-3 P0-5 (§8's non-negotiable) — fixed.** §8 line 899-900 now reads *"one of the two parallel non-negotiable priorities named in §6."* Clean.

**New material that checks out.**

- **The §8 note distinguishing verification comparatives from design comparatives** (lines 923-928) is a genuinely necessary addition and correctly reasoned — the continuity-regression pass really is a different activity from the design process, and without this note the two would read as contradicting. It is the best paragraph in `fa10bdf3`.
- **The Mark-approval gate** (§9 lines 1062-1071) does not conflict with anything in §9's stage descriptions or its adversarial-gates paragraph. Order is stated ("adversarial review first, so factual and logical errors are caught before Mark spends time on it"), sufficiency is stated correctly (*"an adversarial pass finding 'ready' is a necessary condition for moving on, not a sufficient one"*), and it names the same three transitions the gates paragraph names. Nothing is made redundant. Checked specifically per the dispatch; **clean.**
- **Research owning its own gaps** (§9 lines 1010-1015) is a real improvement and does not collide with the four named tasks, which are correctly framed as "at minimum."
- **§6's Objective-3 weighting paragraph is right in its substance** — the failure it names (apparatus quietly outweighing readability) is real, it is grounded in actual prior feedback, and making it explicit rather than implicit was the correct call. The defects at P0-6 are in how it is worded and in what §8 was not updated to match, not in the judgement.
- **Structural health.** Balance ratio **48.3 / 51.7** — §1 296, §2 122, §3 1,079, §4 1,065, §5 2,439 (diagnosis 5,001); §6 1,405, §7 1,934, §8 902, §9 1,108 (ask 5,349); total **10,350**. Round 1's 68/32 failure mode has been absent for four rounds and the ratio has now crossed to the ask side. Round 3's specific structural complaint — §6 growing +198% while §7 grew +7.5% — is genuinely fixed: this time §7 grew **+50.7%** (+651 words) against §6's **+56%** (+504 words), so the priority prose finally has more execution path under it than it did.
- **Cross-references: 88 pointers, 82 resolve cleanly.** The failures are one unresolvable (P1-5) and five that resolve to a section not saying what they cite it for (§7 line 713 "witness-not-recruitment block (§4, untouchable under any framing)"; §7 lines 719-720 the cost claim; §6 line 553 the licence's purpose; §4 line 233 and §7 line 790 the readability gate reading the record layer; §8 line 904 "expensive-but-expected"). Four of the five are new in the post-round-3 commits.

---

## Why round 4 still found what it found

The dispatch asked for a plain answer either way, and asked specifically not to soften toward approval because four rounds is a lot. It is still the "not ready" case, and the reason is the same structural one round 3 named — with one genuinely new component.

**The corrections held, and the discipline that produced them is now proven.** Every one of round 3's five P0 fixes that was a *pure repair against a written finding* landed correctly, and the three I re-derived independently — the interview-vs-table bullet, the 107/118 chunk measurement, and the FK two-variable derivation — survived with nothing substantive to correct. The commit message's own stated intention ("corrections only, no new restructuring bundled in") was honoured, and it worked. The one place `0b4d19d2` slipped is the one place it wrote a *new comparative claim* rather than a correction ("simpler than any of the other five"), which is the pattern round 3 predicted, holding for a fourth round.

**The new material did not hold, for the third commit running.** `fa10bdf3` and `6fcb15bc` landed 1,400+ words of unreviewed restructuring after round 3, and four of this round's seven P0s are in that prose. This is now a four-round pattern with no exceptions: round 1 caught eight defects in original prose; round 2 caught four in 24-hour-old unreviewed prose; round 3 caught three in hours-old unreviewed prose plus two in round-2 fixes that required new positive claims; round 4 caught four in the newest unreviewed prose plus one in the enumeration that replaced round 3's general rule. **The rule holds and should now be treated as a standing project fact: any commit that adds new positive prose to this document creates roughly one P0 per 350 words of it, regardless of who writes it or how carefully.**

**The genuinely new component is a method gap, not a diligence gap.** Three P0s this round (P0-1, P0-2, and half of P0-5) were found by asking a question no prior round asked: *what are the cited instruments actually connected to?* Rounds 1-3 all verified that `readability_check` exists, that it hard-fails without `textstat`, that its numbers trace to `parameters.yaml` and Part Five. All of that is true. **None of them enumerated its callers.** The moment you do, the gate turns out to guard the Level-2 lexicon plain-explanation render and nothing else, and the voice records say so in their own words. Similarly, `probe_parity.py` was cited in this brief twice across three rounds and opened by nobody — and inside it is the continuity-regression harness §7 Part B calls new, built for six worlds, already run, with four failures sitting in committed JSON. Round 3's own lesson was that "measured programmatically" stopped one step short of executing the serialisation path; round 4's is the same lesson one level up — **verifying that a cited symbol exists and does what its docstring says is not the same as verifying it is wired to the thing the brief credits it with enforcing.** That check belongs in the Standard Practice's point 1, and it is the single highest-yield addition this process could make.

**What this means for round 5.** P0-3, P0-4, P0-6 and P0-7 are edits to identified paragraphs with the evidence in this document — deletions, re-scopings and one rewrite. P0-1, P0-2 and P0-5 change what Fable is told exists and what the filter must cover; they are paragraph-level rewrites informed by facts now measured here, not new research. **A fifth full pass is not proportionate if the fix commit is corrections-only.** A targeted re-check of P0-1, P0-2 and P0-4 — three paragraphs — is. If the fix commit again folds in unreviewed restructuring, the four-round pattern says roughly one new P0 per 350 words of it, and a full pass will be warranted again.

---

## Recommended fix list, in order

1. **§7 Part B's continuity-regression bullet and §8's continuity-regression pass** — the mechanism exists for all six worlds, has been run, and reads 2 PASS / 4 FAIL with Albina and Marius among the failures; cite `probe_parity.py` and its five siblings, state that its current parity rule fails a deliberate register change, and require the criterion rather than the step. **(P0-1, P1-8)** — the largest single correction, and the third instance of this brief being told to build something the project already built.
2. **§7 Part B's "both ends are real and wired" and §8's "already wired"** — enumerate the gate's real callers, quote the `voice_profile` records' *"a pointer, not a restatement,"* restore enforcement-for-voice to Part Five's gap list, convert §9(c) from "find out" to "wire it," and say which artifact Objective 3's instrument measures. **(P0-2)**
3. **§7 Part A's clean-rebuild mandate** — scope it to the per-world passes, reconcile "identity/era/vocabulary content fresh" with §4's freeze, carve the two preservation instructions out of "no comparatives," align "re-included as given" with §4 on witness-not-recruitment, add `wrs/records/` and `permanent_prompt.py` to the source list, and re-decide §4's lockstep direction now that Part A is a rebuild. **(P0-3)**
4. **The cost/complexity licence** — three lists instead of two; remove "three-level-sourcing checks" or give it a real referent; protect the instruments for both non-negotiables; resolve the `over_settling` sentence; re-source the cost claim to the Decision Log; put cost in §6 if it is a goal. **(P0-4)**
5. **§7 Part A's leak filter** — restore round 3's general rule, add the 46/17 measurement and the Desert 9 / Alexandria 5 / IJC 3 distribution to §5(B), name Papnoute, and give Research the retrieval-side-strip question. **(P0-5, P1-7)**
6. **§6 Objective 3 and §8's readability bullet** — fix the opening sentence's grammar and its adapt-vs-dilute ambiguity, correct §8 to call `readability_check` the floor's instrument rather than the objective's, name an instrument for the positive half or say plainly it is judged not measured, and add "or more accessible" to the tier paragraph's rule. **(P0-6)**
7. **§8's and §9's review-round record** — four rounds, four audit files, superseding language on round 1 the way §3 already does for the Decision Log. **(P0-7)**
8. **§6 Objective 1's callback half** — a §7 Part A bullet (doc 10:47 says it is prompt guidance, zero infrastructure), a §8 tally, a §9 task (e), and repoint the citation. **(P1-5)** — cheapest real win in the document, and it now serves Objective 3's new positive framing directly.
9. **Objective 6's §7 licensing text and Objective 4's transparency check.** **(P1-4, P1-6)**
10. **§3's doc-09 residues** — the tally sentence's conflation, the "clean single-direction" upgrade, doc 09's copying complication, the prompt-economics clause, and "measurably." **(P1-2)** Then implement the unanimous relationship: a trait rubric fixed before dialogue, in §7, with the 16-trait rubric added to §8.
11. **§6's Albina arithmetic illustration** and the twelve-file readability measurement §7's risk ordering should answer to. **(P1-1)**
12. **§5(B)'s "same pattern, different fields" mechanism attribution.** **(P1-3)**
13. **Round 2's and round 3's remaining unapplied P1s** — the assistant register and a turn-length instrument first. **(P1-9)**
14. **Sweep the P2s** — including `parameters.yaml:102`, now in its fourth round, and the Marius composite, now in its third.
