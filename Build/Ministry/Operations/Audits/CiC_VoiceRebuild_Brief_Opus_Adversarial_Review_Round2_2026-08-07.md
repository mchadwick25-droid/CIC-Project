# Adversarial review (round 2): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus review, dispatched 2026-08-07 — the second adversarial pass on this document, run immediately before its Fable thread. Round 1 (`CiC_VoiceRebuild_Brief_Opus_Adversarial_Review_Round1_2026-08-06.md`) was read in full first, per the Standard Practice's point 4. Calibration for the failure class this round exists to catch was taken from `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/19_Opus_Adversarial_Review_Round4_of_Brief.md` (a different document — skimmed for the class only): that round-4 pass was dispatched because the System Redesign brief's round-3 fix pass introduced two new errors while correcting old ones.*

*Named failure mode hunted, per point 5: **the fix pass itself.** Round 1's eight P0s and ten P1s were applied in `e2eb7f7a`; a separate research-grounding pass followed in `f60a112b`. Two full rewrite passes over a 7,000-word document is exactly the condition under which a corrected claim gets half-corrected, a correct citation gets nudged off by a line, and brand-new prose arrives carrying brand-new unchecked claims. Everything introduced by `f60a112b` had never been checked by anything before this review.*

*Verification method: round 1's eight P0s and eight of its ten P1s re-derived against their own sources from scratch, not against round 1's summary of them. All six permanent prompts read at every cited line; `representative_prompts.py`, `nodes.py`, `state.py`, `facilitator_prompts.py`, `retriever.py`, `indexer.py`, `story_retriever.py`, `story_indexer.py`, `over_settling_logging.py`, `wrs/parameters.yaml`, `wrs/gates/core.py`, `scripts/mark_voice_simulation.py`, `scripts/mark_conversation_test.py` read at the cited lines; both `.docx` files extracted fresh from `word/document.xml`; all 118 lexicon chunks and all 60 story chunks re-measured programmatically, including a new content-level sweep of the `Ecological Function` section body; `Decision-Log.md` read line-numbered. `10_Fable_Conversational_Realness_Study`, `09_External_AIPersona_Framework_Survey`, and `07_RepresentativeVoice_Lenses_Audit` read directly — the first in full — since `f60a112b` made all three required reading and nothing had verified the brief's characterization of any of them.*

---

## Bottom line

**Not ready to send.**

The round-1 fix pass largely landed. Of round 1's eighteen P0/P1 findings I re-derived, **fifteen are correctly and durably fixed** — including all four of the hardest ones (the FLAG-018 four-layer relocation, the Part Five readability-gate reversal, the §5(A) five-of-six rewrite, the §5(B) measured chunk counts, which I re-measured and confirmed exact to the chunk). The structural health held: balance ratio **54.2 / 45.8** (§1–§5 = 3,776 words; §6–§9 = 3,190), still nowhere near the 68/32 failure mode. Several new citations introduced by the fix pass are exact on first check (`nodes.py:2101`, `gates/core.py:211`, `indexer.py:227`, `retriever.py:192`, `retriever.py:224`, `facilitator_prompts.py:241`, all three facilitator diction lines, Marius's SECTION 3 measured at 787 words against Papnoute's 340).

But **seven send-blocking defects remain**, and they split cleanly into the two categories this round was dispatched to find:

**Introduced or left behind by the round-1 fix pass (3):**
- **§5(B)'s story-`Tier` mechanism is a new misattribution.** The fix pass answered round 1's open question ("does Tier need to reach generation") with a file-layout explanation that is false: 35 of 60 story chunks carry the identical `## Retrieval Front-Matter` block lexicon chunks do, and Tier reaches the model because `story_retriever.py:148` writes it from metadata — a one-line retriever choice, not a layout difference. This is the same class as round 1's own P0-1.
- **§5(D) still says the full transcripts are in the Decision Log entry.** That is verbatim the claim round 1's P0-7 blocked on. §3 was corrected; §5(D), four sections later, was not — and now contradicts both §3 and §8 on the evidentiary base of finding D.
- **The Decision Log's superseding note covers three falsified bullets; §3 points at two; two more are falsified and flagged by neither** — including line 13, the direct evidentiary basis for finding B, which still states round 1's P0-6 claim as verified fact in the document Fable reads *before* §5.

**Never checked by anything until now — all four of these are `f60a112b` material (4):**
- **§7 Part B and §8 both assert the Realness Study's three drift signals "are not among `drift_detection`'s existing ten."** `AGREEING` is signal **#3** of the ten. `OVER_PRODUCING` is #4 and explicitly covers length and quantity. `length_ceiling` is a declared `DriftSignal.signal_type`. Two of three are relabelings; the brief's own wording explicitly denies the relabeling reading. This is round 1's P0-4 recurring — telling Fable to build telemetry that already exists.
- **§3's characterization of the Persona Framework Survey is refuted by that survey's own §6.** "Example dialogue is treated industry-wide as ephemeral... never permanent" — doc 09 says in a bolded line, "So it is not unanimous," and documents Google, Alexa, and Salesforce requiring sample dialogue as a first-class deliverable, Character.AI allocating 32,000 characters to demonstration against 500 to description, and Anthropic's own guidance recommending 3–5 examples. The brief pre-loads the one question §7 Part A explicitly defers to Research with a false industry consensus pointing the wrong way.
- **§7 Part A's central instruction points at build-process metalanguage in 25% of the corpus.** Measured: **29 of 118** lexicon chunks carry `Doc_04`, `Primary gravity`, `Tensional gravity`, `G3`, or "this candidate was tested directly and found insufficient" *inside* the `## Ecological Function` section — which sits before `Key Sources` and therefore reaches generation on every retrieval. Sixteen are Theon's; **nine are Albina's** — the world §7 sequences first and §8 names as primary acceptance evidence. Doc 07, which this brief made required reading, already measured the quality problem (26 GENUINE / 10 PARTIAL / 2 RESTATES; HAL 3-of-9 genuine; four chunks using the slot for builder-facing content). The brief cites doc 07 for its placement-vs-absence precedent and carries none of this.
- **Part Five's accessibility band forecloses the Albina exception §6 objective 3 grants**, and §7 Part B calls the two "the exact guidance." They are not the same guidance; one denies the other. §8 then mandates `readability_check` against all six worlds with no rule for what happens when world #1 in the build order fails it.

**Cross-reference integrity: 47 of 48 internal `§N` pointers resolve. One does not** — Objective 6's "validation-probed (§8)" points at a section containing no disagreement probe of any kind. Objective 6 is the only one of six objectives with **no deliverable in §7 and no instrument in §8**: the fix pass closed round 1's Objective-4 completeness hole and the grounding pass opened an identical one on Objective 6.

None of the seven is a writing problem. All seven would propagate into what Fable builds, and four of them would send a capped pass to build something that exists or to lead a voice at material that shouldn't reach a participant. The fixes are again mostly deletion and re-pointing — the largest is deciding what §7 Part A should actually say about the `Ecological Function` slot, which is a paragraph, not a research programme.

---

## P0 — fix before sending

### P0-1. §5(B)'s explanation of why story `Tier` reaches the model is a mechanism misattribution introduced by the fix pass. 35 of 60 story chunks have the exact front-matter block the brief says they don't.

Brief §5(B) (lines 253–256):

> *"Story `Tier` is different again: it sits as a plain header line, not inside a stripped front-matter block, so — unlike lexicon `Tier` — it does reach the model as text on every retrieval."*

Measured across all 60 story chunks: **35 of 60 carry `## Retrieval Front-Matter`**, a fenced block containing `Story-Title:`, `World-Code:`, `Tier:`, `Confidence:`, `Source:`, `Retrieve-When:`, `Do-Not-Retrieve-When:` — structurally identical to the lexicon chunks' own front-matter block, terminated the same way. `data/alexandria_world/story_chunks/alexstory001_gregory-address-origen.md:1-12` is the pattern. Only the remaining 25 (the HAL set among them) put those fields as bare lines at the top of the file.

More importantly, the causal clause — *"so ... it does reach the model"* — attributes the outcome to the wrong thing. Tier reaches the model because the story retriever explicitly writes it:

- `app/rag/story_indexer.py:119` — `tier=int(front_matter.get("tier", "0") or "0")`, parsed into metadata regardless of which layout the file uses
- `app/rag/story_retriever.py:144,148` — `tier = doc.metadata.get("tier", "")` then `context_parts.append(f"### {title} (Tier {tier})\n")`

And the lexicon retriever does not, from the same metadata it also has:

- `app/rag/retriever.py:194` — `context_parts.append(f"### {term}\n")`, with `doc.metadata["tier"]` (constructed at `indexer.py:227`) sitting unused one line away.

**Why this blocks.** Round 1's P0-6 fix instruction was *"Decide whether Tier needs to become visible to generation."* The fix pass answered it with a false mechanism, and the false mechanism changes what the fix is. As written, §5(B) tells a Design stage that lexicon `Tier` is invisible because of where it sits in the file — implying a corpus-wide file-layout migration across 118 chunks. The actual fix is one line in `retriever.py`, copying what `story_retriever.py` already does. §6 objective 2's *"built in a defensible order: most sure first"* and §4's deferred retrieval-ordering note both hang on this. A Fable reader who opens two chunk files to check the claim will find them structurally identical and will not know which half of §5(B) to trust.

**Fix.** Replace the clause with the real mechanism: both chunk types keep Tier in parsed front matter; `story_retriever.py:148` serialises it into the context header and `retriever.py:194` does not; making lexicon Tier visible is a one-line retriever change, not a chunk-file change. Drop the "plain header line" claim entirely — it is false for 35 of 60 story chunks.

---

### P0-2. §7 Part B and §8 both claim the Realness Study's three drift signals are new telemetry. `AGREEING` is drift signal #3 of the ten; `OVER_PRODUCING` is #4 and covers length by name.

Brief §7 Part B (lines 535–541), introduced by `f60a112b`:

> *"**New: drift telemetry, instrumented, not just described.** The Realness Study (§3) names three specific, measurable signals that degrade over a long conversation — response-length growth, declining initiative, and agreement-rate drift. **These are not among `drift_detection`'s existing ten content/posture-based signals (§4) — a genuinely new telemetry category, not a relabeling of what already exists.**"*

Repeated in §8 (lines 598–600): *"...which are new telemetry, not among the existing ten."*

The ten signals, read directly from the monitor prompt at `app/prompts/facilitator_prompts.py:135-175`:

| # | Signal | Bears on |
|---|---|---|
| 3 | **AGREEING** — *"Validating participant's existing views rather than engaging from own formation. Mirror problem... Agreement requiring no encounter with genuine otherness is not formation."* | **agreement-rate drift, directly** |
| 4 | **OVER_PRODUCING** — *"Providing too much... Also covers over-producing by SHAPE rather than stance... the failure is completeness and quantity, not borrowed posture."* | **response length, directly** |
| 6 | FLATTENING | — |

The monitor's own closing instruction (`facilitator_prompts.py:175`) makes the length coverage explicit: *"check shape and length as their own question, separate from whether the voice sounds authentic."*

And the emitted-signal set is larger than ten and already contains a length signal by name. `app/graph/state.py:21-41` declares `DriftSignal.signal_type` as a 20-member `Literal` including **`"agreeing"`**, **`"over_producing"`**, and **`"length_ceiling"`**. `wrs/parameters.yaml:116-130` records `drift_signal_count_emitted: value: 20`, with its own note warning: *"Stale 17 caught by the S5.5 pointer pre-check (FLAG-016)... where they differ, this file is current."* This project has already had one incident of a stale drift-signal count, tracked under its own flag.

**Why this blocks.** Two of the three "genuinely new" signals are existing per-turn flags. The honest claim — that the existing ten are per-turn judgments and none is tracked as a **turn-over-turn rate** — is a real and useful gap, and it is a completely different instruction: instrument the *rate* on signals that already fire, rather than build a new telemetry category. Written as-is, Fable spends capped budget re-deriving `AGREEING`, the signal that Objective 6 and the Realness Study's own standout finding both rest on. This is round 1's P0-4 recurring in new prose: *"give that principle concrete operational teeth"* → *"a genuinely new telemetry category."*

Secondary, same defect: §4 and §8's "ten signals" is right for the monitor prompt and wrong for the emitted set. §8's per-signal drift breakdown, built to ten, would silently drop half the declared `signal_type` space. §4's *"all content- or posture-based, not register-based"* is also unsupported for `length_ceiling` and `question_stacking`.

**Fix.** Rewrite the bullet: `AGREEING` (#3) and `OVER_PRODUCING` (#4) already flag agreement and length per turn; `length_ceiling` is already a declared signal type; what does not exist is turn-over-turn rate tracking for any of them, and declining initiative has no analogue at all. State that the emitted set is 20 (`state.py:21-41`, `parameters.yaml:116`), not 10, and scope §8's breakdown to it.

---

### P0-3. §3's characterization of the Persona Framework Survey is contradicted by that survey's own §6, and drops the survey's positive evidence for exactly the thing §7 Part A proposes.

Brief §3 (lines 87–97), introduced by `f60a112b`:

> *"example dialogue is treated **industry-wide** as *ephemeral*, pruned first under context pressure, **never permanent** — worth weighing against §7 Part A's plan to add worked examples straight into the permanent prompt"*

`09_External_AIPersona_Framework_Survey.md` supports this **only for the character-card ecosystem** — lines 20–22 (V1's `mes_example` "SHOULD... be pruned"; SillyTavern's permanent-vs-non-permanent split). Its own §6, headed *"Show-don't-tell for voice: what the evidence actually supports,"* is a direct refutation of the generalization (lines 299–309):

| Source | Status of example utterances |
|---|---|
| Google Conversation Design | *"Required, produced before flows and before code; one of only two high-level deliverables"* |
| Amazon Alexa | *"Required — terminal step of the persona procedure... and a mandatory storyboard component"* |
| Salesforce | *"Required Design-phase deliverable"* |
| Character.AI | *"32,000 chars for Definition vs. 500 for Long Description"* |
| Microsoft | Not required — scratch pad |
| IBM | Absent |

Followed, in the source's own bolded words at line 309: **"So it is not unanimous."**

Three further omissions, all of which cut toward §7 Part A rather than against it:

- Doc 09 line 95's own verdict on the split the brief cites: *"**TRANSFERS CLEANLY.** Pure prompt economics."* It is an eviction-order rule for systems under context pressure, not a claim that examples are ineffective or belong outside the permanent prompt.
- Doc 09 line 315 quotes Anthropic's own guidance verbatim: *"Examples are one of the most reliable ways to steer Claude's output format, tone, and structure"*, with *"Include 3–5 examples for best results."* That is direct model-side evidence about the exact model CiC runs, on the exact question, and the brief cites this document without it.
- The eviction mechanism does not currently apply to CiC. `10_Fable_Conversational_Realness_Study.md:42` records that CiC runs full-history-in-context with prompt caching and *"is already doing this correctly"* — there is no truncation stage for an ephemeral field to be evicted from.

**Why this blocks.** §7 Part A explicitly defers the worked-example question: *"The exact form these examples take... is a Design-stage decision, made only after the Research stage resolves the open question in finding (C) — not prescribed here."* §9's Research stage then sends Fable to doc 09 for *"the ephemeral-vs-permanent example-dialogue question."* Handing Fable a false industry consensus against permanence, on the one question the brief most deliberately leaves open, is the most consequential steering error in the new material. Doc 09's actual finding — that vendors split, and that what is unanimous is the *relationship* (fix the adjective set first, then write and judge dialogue against it, line 311) — is more useful to §7 Part A than the version the brief carries.

**Fix.** Rewrite the bullet: the character-card ecosystem treats example dialogue as evictable under context pressure (a prompt-economics rule CiC's full-context caching does not currently trigger); the wider survey is explicitly split, with three vendors requiring sample dialogue as a first-class deliverable and Character.AI allocating 98.5% of its persona budget to it; Anthropic's own guidance recommends 3–5 examples; what is unanimous is that the trait rubric is fixed first and the dialogue judged against it.

---

### P0-4. §7 Part A's "lead with Ecological Function material" points at build-process metalanguage in 29 of 118 chunks — nine of them Albina's, the world sequenced first and named as primary acceptance evidence.

§7 Part A instructs Fable to write an *"explicit instruction to lead with Ecological Function material (and its story-chunk equivalent, `Formation Ecology Connection`)."* §6 objective 2 makes it a stated objective.

Measured across every lexicon chunk, scanning only the body of the `## Ecological Function` section: **29 of 118 (25%)** contain internal build-process vocabulary — `Doc_04`, `Doc_05`, `Primary gravity`, `Supporting gravity`, `Tensional Gravity`, `G3`, or explicit audit-log phrasing. By world: **Alexandria 16, Hieronymian 9, Syriac 4.**

Section order confirmed in-file (`hal_lex11`: Quick Meaning → World Meaning → **Ecological Function** → Distortion Risk → Key Sources → Reported-Experience Status), so this material sits *before* `truncate_at(body, KEY_SOURCES_MARKERS)` and reaches generation context on every retrieval that surfaces the chunk.

Three verbatim examples, all in worlds §7 rewrites:

- `hieronymian_world/lexicon_chunks/hal_lex11_exegesis-practiced-authority.md`, `## Ecological Function` in full: *"The evidentiary core of this world's one **Tensional gravity** — a genuine counter-current within the ecology that does not organize as broadly as the **Primary gravities** but cannot be honestly omitted. Directly relevant to whether this world contains distinct internal strands (it does not, on current evidence — **this candidate was tested directly and found insufficient** to establish a difference in kind...)."*
- `hal_lex06_patrocinium.md`: *"**Anchors G3 (Primary gravity, the strongest bipolar-holding candidate in this world's ecology)**; the organizational bedrock..."*
- `alexlex001_logos.md`, `alexlex002`, `alexlex003`, and thirteen more Alexandria chunks carry `Doc_04` / `supporting gravity` references directly in the slot.

The brief's own required reading measured this and the brief carries none of it. `07_RepresentativeVoice_Lenses_Audit.md:141`: **"26 GENUINE / 10 PARTIAL / 2 RESTATES / 3 absent"** across 41 chunks read in full. Line 145: *"Quality varies by world... Desert 9/9 genuine, Alexandria 6/8, IJC 4/5, Syriac 4/7, **HAL 3/9**."* Line 155 names the exact defect: *"four chunks use the slot for **builder-facing content** rather than ecology — lexicon bookkeeping... evidentiary calibration... and **build-process audit log** (`hal_lex11`: 'this candidate was tested directly and found insufficient')."* Line 172: *"No review in any world asks whether an Ecological Function delivers dependency insight or restates the Quick Meaning."*

HAL is Albina's world. Albina is **first** in §7's risk-ordered per-world sequence and one of §8's primary acceptance worlds. Alexandria is Theon's, which §8 already flags as *"the world most exposed to §7 Part A's lead-with-insight instruction silently no-op'ing"* — for the 5 chunks that lack the field. It also holds 16 of the 29 that have the field filled with build-process prose.

**Why this blocks.** Round 1's P0-6 caught the *presence* half and the fix landed exactly (I re-measured: 109/118, missing 5 Alexandria / 2 PAHC / 2 Syriac — brief exact). The *content* half is worse and was sitting in the project's own audit the whole time. §4's own carve-out defect #1 already flags participant-facing build-process leakage through `CitationModal`'s `key_sources` — *"a dangling reference to an internal document no participant can see."* §7 Part A's new instruction opens a second door to the same defect, through the generation path rather than the citation path, and the brief does not connect them. A Representative told to *lead* with Ecological Function material, on an Albina turn that retrieves `hal_lex11`, is being told to open on *"the evidentiary core of this world's one Tensional gravity."*

**Fix.** Add the measured content finding to §5(B) (29 of 118 carry build-process language; doc 07's 26/10/2 quality split; HAL 3-of-9). Reword §7 Part A's instruction so it names the *substance* — the dependency the term participates in — rather than the field, and add an explicit exclusion for build-process vocabulary, cross-referenced to §4's carve-out defect #1. Give the Research stage the task of deciding whether the 29 need cleaning before the instruction ships, since that is a content edit and §4 freezes chunk content.

---

### P0-5. §5(D) still asserts the full transcripts are in the Decision Log entry — verbatim the claim round 1's P0-7 blocked on, now contradicting the corrected §3 and §8.

Brief §5(D), lines 380–381:

> *"...that part holds; **full transcripts and cost data are in the Decision Log entry named in §3.**"*

Brief §3, lines 50–53, as corrected by the fix pass:

> *"**The full transcripts themselves are not in this entry** (its own line 57 says so directly) — they were rendered as a claude.ai Artifact, not a repository file this thread can read. Treat the entry's own quotes and findings as the evidentiary record, **not an 'actual transcripts' claim this brief can't back up.**"*

Brief §8, line 625:

> *"...transcripts referenced in the Decision Log entry in §3, **not currently committed to this repository** — only a session-scratchpad copy exists..."*

And the source, `Decision-Log.md:59`: *"**Full transcripts, cost tables, and citation excerpts:** rendered as a styled Artifact... **not reproduced in full here** to keep this log scannable."*

**Why this blocks.** Finding D is the argument for which worlds supply acceptance evidence — it drives §8's entire live-test list. Its evidentiary base is stated three different ways in three sections of one document: present in the log (§5), not present in the log (§3), not present anywhere in the repo (§8). Fable is instructed by §3 and §9 to *"verify it against the file/line it cites."* Following §5(D) to the Decision Log entry returns nothing, and the brief gives no signal which of its own three statements to believe. Round 1 rated this exact claim P0; the fix pass corrected the instance in §3 and missed the instance in §5.

**Fix.** Delete the clause from §5(D) or replace it with §8's formulation. One statement, in one place.

---

### P0-6. §3's superseding pointer names two Decision Log lines; four are falsified, the log's own note covers three, and §3 thereby certifies two false bullets as still good.

Brief §3, lines 53–56:

> *"That entry's own findings list (**its lines 12 and 15**) predates this brief's finding (A) and (C) corrections below and now carries a superseding note pointing here — read this brief's §5 for the current diagnosis, not that list."*

`Decision-Log.md`, the "What this session found, **verified directly against the code rather than guessed**" list, read line-numbered:

| Line | Claim | Status |
|---|---|---|
| 12 | *"archaic/formal register is 100% sourced from the six per-world permanent prompt files"* | Falsified (R1 P0-5). **Superseded by the log's own note; §3 flags it.** ✓ |
| **13** | *"**Every** retrieved chunk already carries `Ecological Function`... and `Distortion Risk`... and **both already reach the model's generation context** — confirmed via `app/rag/sections.py`/`retriever.py`"* | **Falsified (R1 P0-6): 109/118, 0/60 stories, and `sections.py` cannot confirm it. Not superseded. Not flagged by §3.** |
| 14 | governance confirmed content-based | Holds |
| 15 | *"worked example dialogues... carry real enforcement weight prose alone doesn't"* | Falsified (R1 P0-3). **Superseded; §3 flags it.** ✓ |
| 16 | *"the gap across six builds is enforcement, not philosophy"* | Falsified (R1 P0-4). **Superseded by the log's note — but §3's "lines 12 and 15" excludes it.** |
| **17** | *"the three plainest worlds of the six already"* | **Falsified by this brief's own finding (D) — Yausep 23.0 vs Albina 23.6. Not superseded. Not flagged by §3.** |

**Why this blocks.** §3 orders the Decision Log entry read *before* §5 and calls the entry's own findings the evidentiary record. Naming exactly two superseded lines is a positive assertion that the other four survived. Line 13 is the direct evidentiary basis for finding B and for §7 Part A's central instruction, and it states the round-1 P0-6 claim as code-verified fact. Line 17 states the claim §5(D)'s own headline says *"shouldn't be repeated as written."* A precise pointer that undercounts is worse than no pointer, because it looks like it was checked.

**Fix.** Extend the Decision Log's superseding note to lines 13 and 17, and change §3's parenthetical to name all four (12, 13, 15, 16) plus 17, or simply say "several of that list's findings were falsified by the round-1 review; read §5, not the list."

---

### P0-7. Part Five's accessibility band forecloses the Albina exception §6 objective 3 grants. §7 Part B calls them "the exact guidance"; §8 mandates the gate on all six; nothing resolves the conflict for the first world in the build order.

The three statements, all in the current text:

- **§6 objective 3**: *"Sentences read as plain, real, everyday spoken English... **Albina's periodic rhythm is the one deliberate, formation-accurate exception, kept substantively.**"*
- **§7 Part B**: *"...and, immediately after it, **the exact guidance §6/§7 believed they were inventing for Albina**: 'A world whose own sources are rhetorically trained and elaborate should still keep its sentences within the accessibility band — elaboration belongs in vocabulary, imagery, and clause content, not in unbroken sentence length.'"*
- **§8**: *"**`readability_check`**... Run it against baseline and rebuilt output for all six worlds; this is the instrument that actually tests Objective 3."*

Both quoted passages verified verbatim from `CiC_L3C_Representative_Construction_Framework_V3.2.docx`, paragraphs 85 and 86 — including *"this standard is independent of vocabulary"* and the parameters-file pointer. The gate is real: `wrs/parameters.yaml:102-114` (`flesch_kincaid_grade_band: [8, 10]`, `flesch_reading_ease_min: 60`) and `wrs/gates/core.py:211 readability_check(text, fk_max=10.0, fre_min=60.0)`.

But Part Five's passage is not the guidance §6 thought it was inventing — it is the guidance §6 **contradicts**. Part Five's construction note says elaborate worlds get **no exception** on sentence length; elaboration is confined to "vocabulary, imagery, and clause content." §6 objective 3 grants Albina exactly the exception Part Five withholds, and grants it on precisely the axis Part Five governs: *"periodic/hypotactic... one clause answering to another"* is clause-chaining and sentence length. §5(D)'s own measurement makes it concrete — Albina's baseline runs **23.6 words per sentence**, which will not sit inside an FK 8–10 band.

**Why this blocks.** Albina is **first** in §7's risk-ordered sequence and a primary acceptance world. Fable executing §7's first per-world pass faces three instructions from three sections and no resolution rule: §6 says keep the periodic rhythm substantively; Part Five (which §7 Part B endorses) says bring the sentences inside the band; §8 says run the gate and treat it as Objective 3's instrument. If Albina fails `readability_check` — which the numbers say she will — the brief does not say whether that is a defect to fix or the deliberate exception working as designed. Nothing in §9's Research stage asks the question either; task (c) asks only *whether the gate has ever been run*, not what to do with a failure.

Note this is not a fix-pass error alone — round 1's own P0-4 used the same "guidance they believe they are inventing" framing, and the fix pass carried it faithfully. It is wrong in both.

**Fix.** Replace *"the exact guidance §6/§7 believed they were inventing"* with the real relationship: Part Five already denies elaborate worlds an exception on sentence length, which is in direct tension with §6 objective 3's Albina carve-out. Then add the decision to §9's Research stage explicitly — run `readability_check` against Albina's current output first, and decide whether Part Five's band binds her, whether her exception is a documented deviation, or whether Part Five needs amending. That decision gates §7's first per-world pass and cannot be discovered mid-build.

---

## P1 — materially improves, not disqualifying

### P1-1. Objective 6 has no deliverable in §7 and no probe in §8. Its own "validation-probed (§8)" pointer is the single broken cross-reference in the document.

Brief §6, objective 6 (lines 421–428), introduced by `f60a112b`:

> *"A Representative holds its world's actual position under real, sustained pushback across a conversation... **Explicitly licensed**, not just permitted by omission, and **validation-probed (§8) across multiple turns of real disagreement**, not read off a single turn's tone."*

Counted across the whole brief: `disagree` appears at lines 80 (§3), 422/428 (§6), 679 (§9); `pushback` at 378 (§5 D) and 422 (§6). **Zero occurrences in §7. Zero in §8.**

- **"Explicitly licensed"** requires prompt text. §7 Part A's shared-file bullet list (bridge-first entry, Ecological Function instruction, shape repertoire, FLAG-018 disambiguation) does not include it; neither does any per-world bullet. The Realness Study's own recommendation (line 34, line 75) is that this belongs in the turn-guidance layer — `PRIMARY_TURN_GUIDANCE` in its wording, which appears **nowhere** in this brief.
- **"Validation-probed (§8)"** does not resolve. §8's two named Part Eight categories are *confidence-under-thinness* and *Sustained Engagement Testing*. I read Part Eight's category list directly from the docx: `Source-Awareness Probes`, `Confidence-Under-Thinness Probes`, `Self-Referential Probes`, `Claim-Laundering & Decontextualization Probes`, `Sustained Engagement Testing`. Sustained Engagement Testing tests *"whether the engagement deepens over time, whether the Representative responds to conversational trajectory"* — trajectory, not disagreement. **Part Eight has no disagreement/pushback category at all**, which the brief does not say, even though it correctly says Part Eight has no naturalness category.

The only §8 coverage is indirect: the per-signal drift breakdown's "agreement rate." That is telemetry, not the multi-turn probe Objective 6 demands.

This is round 1's P1-7 recurring on a different objective. The completeness map now reads:

| Objective | §7 deliverable | §8 instrument |
|---|---|---|
| 1 — bridge-first | Part A bullet 1; Part B ✓ | **none** (see P1-4) |
| 2 — EF/DR + shape repertoire | Part A bullets 1 & 3; Part B ✓ | over_settling confirmed rate (partial) |
| 3 — plain English, Albina exception | Part A audit + Albina bullet ✓ | `readability_check` ✓ (but see P0-7) |
| 4 — no fabrication | §4 carve-out ✓ | fabrication rate ✓ — **round 1's gap, now closed** |
| 5 — Framework self-sufficiency | Part B ✓ | continuity-regression pass ✓ |
| **6 — sustained disagreement** | **none** | **none** |

**Fix.** Either add a §7 Part A bullet giving disagreement its licensing text and a §8 probe (a multi-turn agreement-pressure sequence, which Part Eight would need as a new category alongside the naturalness one §7 Part B already requires), or demote Objective 6 to a Research-stage question and say so.

### P1-2. §7 Part B requires the 16-trait rubric as "a named validation instrument"; §8 never names it, and no project document reproduces the traits.

Brief §7 Part B (lines 552–557): *"**New: adapt the Realness Study's 16-trait human-likeness rubric as a named validation instrument**, keeping the study's own caveat intact — some traits (informal grammar, typos) are excluded..."*

The characterization is accurate to the source. `10_Fable_Conversational_Realness_Study.md:26`: *"the 16-trait checklist is directly usable as a rubric... with some traits (informal grammar, typos) consciously excluded as incompatible with CiC's brand and historical fidelity."* Two problems the brief does not carry:

- **§8 never names it.** `16-trait` appears exactly once in the brief, in §7 Part B. §8 opens with *"Every prediction... needs to be falsifiable by an instrument actually named here"* and lists six instruments; the rubric is not among them. §7 Part B's own Part Eight bullet enumerates the instrument set — *"readability_check, a term-reclarification count, the fabrication rate, a per-signal drift breakdown"* — and omits the rubric it requires two bullets later. §7 Part B is inconsistent with itself as well as with §8.
- **The traits are not in the corpus.** Doc 10 names 2 of the 16, both as exclusions. The rubric lives in the HAL preprint (arXiv 2601.02813v3), and doc 10 rates the finding *"(Medium confidence — one un-replicated 2026 preprint)"* — a caveat the brief drops while upgrading the item to a requirement. Doc 10's own open question (line 105) is *"Which of the 16 human-likeness traits survive CiC's own non-negotiables? Nobody has mapped which naturalness levers remain..."* — so the adaptation §7 requires is a genuinely open research task, which §7's "this brief only requires that it happen" wording understates.

**Fix.** Add it to §8's instrument list or move it to §9's Research stage; carry the medium-confidence caveat; note that the traits themselves must be recovered from the cited preprint.

### P1-3. The Realness Study's own headline finding — the "assistant register," with response-length restraint as the single highest-weighted human-likeness trait — appears nowhere in the brief, while every §7 addition pushes length up.

`10_Fable_Conversational_Realness_Study.md:9`, executive summary, first sentence: *"The strongest convergent result across 2024–2026 research is that the **'assistant register'** — long, over-polite, over-explaining, agreement-prone replies — is the primary tell that breaks perceived conversational realness."* Line 22: *"Response-length restraint is the single highest-weighted trait predicting human-likeness in one recent alignment study (**nearly double the next-highest trait**)."*

Counted: `assistant register` = 0 occurrences in the brief. `brevity` = 0. §3 cites this study for three things and omits the one it leads with.

This is not a neutral omission. §7 Part A adds worked example dialogues to five permanent prompts, a four-shape answer repertoire, and a bridge-first opening move that names the participant's assumption before answering — all length-adding. Round 1's own prediction section forecast Papnoute's turn length rising above his 138-word baseline and named his file's own hard ceiling (*"four sentences is already long for you"*, `desert_..._Papnoute.txt:13`, verified). §8 names no turn-length instrument: `readability_check` measures per-sentence FK/FRE, not turn or response length.

The study's own caveats belong with the finding and are also absent — line 23 (*"The source data behind this finding is short, texting-style exchanges, so this needs care in CiC's substantive, sourced dialogue"*), line 98 (domain transfer), and line 102's open question (*"Does brevity's naturalness advantage survive in substantive, educational dialogue... the single most decision-relevant gap"*).

**Fix.** Add the assistant-register finding and its caveats to §3's doc-10 bullet; add a per-turn word-count metric to §8 with Papnoute's existing ceiling as the reference point.

### P1-4. Objective 1 — the brief's first objective — has no instrument in §8.

§8's own standard: *"Every prediction this brief or its Research stage makes needs to be falsifiable by an instrument actually named here."* Its six instruments are `readability_check`, the fabrication rate, the over-settling confirmed rate, the per-signal drift breakdown, the term-reclarification tally, and the continuity-regression pass.

None measures whether a turn opens from where the participant stands. The term-reclarification tally counts a *defect* (finding C's unprompted "when I said X"), not bridge-first uptake. Round 1's prediction section made first-sentence uptake the central falsifiable claim for both worlds it had real transcripts for — Albina falsification condition (b), *"her three first sentences still open on the question's wording rather than the participant's assumption"* — and that remains unmeasurable. The fix pass closed Objective 4's instrument gap and left Objective 1's open.

**Fix.** Add a counted first-sentence-uptake classification (does turn 1's opening sentence name the participant's own question/assumption, or the world's framing) — the same shape as the term-reclarification tally already specified, and derivable from the same transcripts.

### P1-5. The continuity-regression instrument has no pass criterion and, read literally, is failed by a successful rebuild.

§7 Part B requires it *"before any future voice-affecting prompt change reaches a built world — **including this rebuild's own output before it ships**."* §8 operationalizes it: *"same probes run against the current, unrebuilt prompt and the rebuilt one, diffed directly, before this thread's output is treated as ready to ship."*

The source characterization is accurate (`10_...Realness_Study.md:53-59`, near-verbatim on *"same probes, old prompt vs. new prompt, diff the actual voice"*). But two things do not transfer without a stated rule:

- **No threshold.** Every other §8 instrument produces a number with a direction. This one produces a diff, and the brief's entire mandate is that the diff should be large. Applied to this rebuild, "the voice changed" is simultaneously the success condition (§6 objectives 1–3) and the alarm.
- **The source's stated precondition does not hold.** Doc 10 line 59: *"This matters more every week the pilot builds a base of people who've talked to a Representative more than once."* CiC is pre-launch; there are no returning participants for a continuity break to injure. The discipline is worth establishing — but as a standing rule for post-launch changes, not as a ship-gate on the rebuild that has to break continuity on purpose.

**Fix.** State what a continuity-regression pass is checking *for* on this rebuild — presumably that world-identity markers (Marius's precedent-first ordering, Yausep's stage-by-stage demonstration, Albina's periodic rhythm, Theon's surface-then-depth) survive, while register changes — and scope the ship-gate version to post-launch changes.

### P1-6. §5(C)'s four pilot-derived claims rest on a results file that is not in the repository, and §8's commit-a-durable-copy action item does not cover it.

§5(C) now carries four measured claims from the same-day pilot: the guarded behaviour appearing in both arms; the `PROTOTYPE_ADDITIONS` confound; the Chloe turn-1 false conversational memory; and the Albina `fabrication_adjudication` firing. All four were added by the round-1 fix pass. All four trace to `mark_voice_simulation_results.json`, which I confirmed is in no commit on any branch and nowhere on disk in the repo. §5(C) says so honestly (*"results not committed to the repo"*), and the fix commit's own message flags P1-2 as unapplied for the baselines.

But §8's remediation covers only the *baseline* transcripts: *"transcripts referenced in the Decision Log entry in §3, not currently committed to this repository... commit a durable copy before this thread starts."* The pilot results — which now carry more of §5's evidentiary weight than the baselines do, including the Albina fabrication signal that §9 task (d) makes a Research-stage assignment — get no equivalent action item. §3 and §9 both instruct Fable to verify every §5 finding against the file/line it cites; none of finding C's pilot claims can be verified.

**Fix.** Extend §8's commit action to `mark_voice_simulation_results.json` alongside `mark_conversation_test_results.json`.

### P1-7. "Measurably stronger weight" upgrades a community spec's design rationale into a measurement, and calls it independent confirmation.

Brief §3: *"`post_history_instructions` exists because instructions placed after conversation history carry **measurably** stronger weight than instructions before it — **independent, external confirmation** of the exact principle behind FLAG-018 layer 3."*

`09_External_AIPersona_Framework_Survey.md:38` quotes the V2 spec: instructions after the conversation have *"**much** stronger weight on current models' generations than instructions written before the conversation history."* "Much" → "measurably" changes the epistemic status of the claim: the character-card V2 spec is a community specification stating a design rationale, not a measurement, and doc 09 presents it as such.

The corroboration is real and worth keeping — but the actual measurement is CiC's own, and §5(C) already cites it correctly (`nodes.py:1156-1163`, *"one false 'I meant X earlier' opener remained in 16 turns"*, verified verbatim). The external item is convergent design practice, not independent data.

**Fix.** *"...carry much stronger weight — the spec's own stated rationale, converging on the principle behind FLAG-018 layer 3, whose measurement is CiC's own."*

### P1-8. The doc-07 precedent is cited without disambiguating build-time from runtime, and reads as contradicting finding B.

§3's doc-07 bullet is accurate on its own terms — I verified the Abba Moses account at `07_...Lenses_Audit.md:77-79` including the *"Same information, different placement and form"* quote verbatim, the *"organization failures, not evidence failures"* framing at line 244, and confirmed the fix landed live in the deployed prompt (`desert_..._Papnoute.txt:78`: *"The jug that leaked was Moses's own... and when we tell it, we tell it as his."*).

But doc 07's Ecological Function headline (lines 159–161) is: *"The string 'Ecological Function' appears in exactly two Representative-side documents across all six worlds... **Zero Permanent Prompts. Zero World Capsule Cores.** Zero Representative Construction Notes."* Finding B says the opposite-sounding thing: 109 of 118 chunks carry it and it reaches generation context. Both are true — doc 07 is about *build-time* Representative documents, finding B about *runtime* retrieved context — but the brief sends Fable to read doc 07 *before* §5 without saying so. A reader taking doc 07's bolded zeros at face value will read finding B as contradicted by required reading.

**Fix.** One clause in §3's doc-07 bullet: doc 07's zeros are about build-time Representative-side documents; finding B is about runtime retrieval, and the two are compatible.

---

## P2 — polish

1. **`wrs/parameters.yaml:101-114` should be `:102-114`**, in both §7 Part B and §8. Line 101 is blank; `reading_floor:` is at 102. Round 1 cited 102 correctly; the fix pass moved it. The block content is right.
2. **§3's "(its own line 57 says so directly)" is off by two.** `Decision-Log.md:57` is *"Where the original complaint does NOT reproduce..."*; the transcripts sentence is line **59**. Round 1 made the same error and the fix pass inherited it.
3. **§5(A)'s Marius quote is a reversed-order composite.** Brief: *"one short sentence for the first fact. A full stop... Each one short enough to stand alone."* In `ijc_..._Marius.txt:117`, *"Each one short enough to stand alone"* comes **before** *"one short sentence for the first fact. A full stop."* An ellipsis reads as forward omission. Both fragments are real and the substance is fully supported; the ordering is not. Worth naming because composite quoting is a P0-class failure in this project's own history.
4. **§5(A)'s Theon quote truncates silently.** Brief: *"You land one thing, and stop."* Actual (`:37`): *"You land one thing, and stop, and begin the next fresh."*
5. **§5(C) says "four separate points," then names a fifth.** The four mix three shared-code layers with one per-world copy (Chloe's `:29`) while excluding the other per-world copy (Marius's `:119`), which is then introduced as *"a fifth, per-world instance."* §7 Part A repeats "four separate points." Either count both per-world copies or neither.
6. **§7 Part B's Part Eight bullet enumerates four instruments; §8 lists six.** Omits the over-settling confirmed rate, the continuity-regression pass, and the 16-trait rubric §7 Part B itself requires (P1-2).
7. **§3 describes doc 09 as covering "Character Card V1-V3, SillyTavern."** It surveys nine systems across five topics, including Character.AI, Google, Alexa, Microsoft, IBM, Salesforce, and the academic persona-dialogue literature. The two named are the hobbyist ecosystem — the narrowest slice, and the one P0-3's overgeneralization comes from.
8. **§4's claim that Theon's fabrication guard is "closer in kind to Papnoute's own differently-worded version" is arguable.** Theon's (`alex_..._Theon.txt:7`) carries the same three-failure-mode scaffold as the museum-guide near-copies — a figure asked a personal-memory question, then invention / self-explanation / limit-as-subject — just with a different figure. Papnoute's anti-fabrication material (`:78`, `:84`, `:86`) is a different mechanism: attribution ownership plus honest-thinness rules, with no scaffold. Theon is closer to Yausep's and Marius's than to Papnoute's. The carve-out instruction ("do not edit... any of the four") is right either way.

---

## What verified clean

Stated plainly, because the fix pass mostly worked and the document is substantially better than it was on 2026-08-06.

**Round-1 P0s re-derived and confirmed fixed:**

- **P0-1 (FLAG-018).** All four layers verified at their stated locations: `representative_prompts.py:168-181` inside `dynamic_parts` behind `if retrieved_context:` (line 164) — confirmed; `nodes.py:1155-1167` layer 3 at the wiring site, with the *"one false 'I meant X earlier' opener remained in 16 turns"* comment quoted **verbatim** and correctly attributed; `nodes.py:3871` / `modern_term_bridge.py:237` layer 4; Chloe `:29` and Marius `:119` per-world copies both verified; the IJC-scoped extension confirmed at `nodes.py:1174` ff. §7 Part A's redirect (*"don't word anything here as an 'extension' of a guard that lives elsewhere"*) is correct and is the sharpest single repair in the document.
- **P0-2 / P0-3 (pilot).** The `PROTOTYPE_ADDITIONS` confound quoted **verbatim** from `scripts/mark_voice_simulation.py`; the non-discriminating-matched-pair framing, the false-conversational-memory defect, and the Albina `fabrication_adjudication` firing with its `hal_story05_marcella-death` genre caveat all now correctly reported and correctly hedged.
- **P0-4 (Part Five).** Both quotations verified verbatim from the docx, including *"this standard is independent of vocabulary"*; the gate confirmed at `wrs/gates/core.py:211`; the open question (*"has this gate actually been run against the six current builds"*) is the right question and is correctly marked as one the brief must not guess at. (Its Albina consequence is P0-7.)
- **P0-5 (§5 A).** All six per-world quotations re-read at their cited lines and verified: Papnoute `:7` (now exact, with the semicolon restored), Chloe `:23`, Yausep `:41`, Marius `:117`, Albina `:29` including her anti-stacking limiter. The new claim that Marius's SECTION 3 outweighs Papnoute's register material is **measured true**: SECTION 3 runs lines 108–122, 787 words, against Papnoute's `:7`+`:13` at 340.
- **P0-6 (§5 B).** Re-measured from scratch against every chunk: **109/118** lexicon chunks carry `Ecological Function`, **118/118** carry `Distortion Risk`, missing set exactly Alexandria 5 / PAHC 2 / Syriac 2; **60/60** story chunks carry `Formation Ecology Connection`, **0/60** carry `Distortion Risk`. Every number in §5(B) is exact. The Quick Meaning excision confirmed at `retriever.py:224`, and the `sections.py` mis-citation properly walked back.
- **P0-7 (Decision Log).** Superseding note added and dated; §3's line references 12 and 15 are **exact** (line 12 = the 100% claim, line 15 = the worked-examples claim); the values/convictions category conflation fixed — the Vision docx carries exactly four Foundational Values (Participant Agency, Historical Responsibility, Intellectual Humility, Encounter Over Persuasion) and §3 now names all four with the two Convictions correctly numbered.
- **P0-8 (§8 instruments).** All five replacement instruments exist and are cited correctly: `gates/core.py:211`, `nodes.py:2101` (`log_llm_usage("fabrication_adjudication", ...)` — exact), `app/over_settling_logging.py:41`, the drift-breakdown gap, the term-reclarification tally. `UsageCapture` (`mark_conversation_test.py:88-98`) confirmed to key on `[llm_usage]` lines and split `k=v` fields, so the fabrication label is genuinely capturable. `SCENARIOS` confirmed hardcoded to desert / pahc / syriac at `:111-142`.

**Round-1 P1s re-derived and confirmed fixed:** the `wrs/` record layer added to §4 with an explicit lockstep decision (P1-1); Yausep added as a third acceptance world with the 23.0 measurement (P1-3); Yausep's `:45` bridge-first instruction quoted verbatim and promoted to run *first* in §9's Research stage (P1-4); §4's block lists corrected — `museum guide` confirmed by string match in **Yausep and Marius only**, `witness-not-recruitment` confirmed present in **all six** including Papnoute `:17`, Chloe `:43`, Yausep `:65-67`, and Marius's literal `SECTION 6 — WITNESS-NOT-RECRUITMENT` at `:139` (P1-5); Marius's `:119` analogue added (P1-6); Objective 4 now has a §8 metric (P1-7); the Chloe pilot correctly re-labelled a safety pilot (P1-8); Theon added to §8's live-test list (P1-10).

**P2 sweeps confirmed applied:** `indexer.py:227` (exact — `"tier": entry.tier`); the Papnoute quote; the over-settling quote with *"this claim needs"* restored (`facilitator_prompts.py:241`, exact); Article 6 correctly attributed to the Constitution with the Vision doc's *"Note: Constitution Article 6 refines..."* relationship stated accurately; `sections.py` no longer cited for what it can't confirm; **`Sustained Engagement Testing`** confirmed as Part Eight's actual category name, read from the docx; the `SCENARIOS` extension flagged.

**New material that checks out:**

- **The Realness Study's provenance and its two central findings.** *"105 agents... 25 put through 3-vote adversarial verification — 22 confirmed, 3 refuted and dropped"* — exact to line 3. The persona-enactment finding is quoted verbatim from line 34 and is genuinely the source's own *"standout finding"* in its own words. The three drift signals are correctly named from line 29. The continuity-regression characterization is near-verbatim from lines 53–59. (The problems are what surrounds them — P0-2, P1-3, P1-5.)
- **The Lenses Audit's Abba Moses precedent** — verified verbatim at `07_...:77-79`, and independently confirmed live: the fix text is sitting in `desert_..._Papnoute.txt:78` exactly as doc 07 describes it. The *"placement or form, not absence"* framing is doc 07's own conclusion (line 244).
- **Part Eight genuinely has no naturalness/register category.** Confirmed by full-text search of the docx: the string "naturalness" does not appear anywhere in the Construction Framework. §7 Part B's claim is correct.
- **Structural health.** Balance ratio **54.2 / 45.8** (§1 156, §2 129, §3 695, §4 736, §5 2,060, §6 302, §7 1,193, §8 799, §9 896 words). **47 of 48** `§N` cross-references resolve. §9's reframing of the Research stage onto "what makes a conversation good," with §5 demoted to supporting evidence, is a real improvement and reads as Mark's redirect landing correctly.

---

## Recommended fix list, in order

1. **§7 Part A's Ecological Function instruction** — add the measured content finding (29 of 118 carry build-process language; doc 07's 26/10/2 and HAL 3-of-9), reword the instruction to name the substance rather than the field, add the build-process exclusion cross-referenced to §4's carve-out defect #1. **(P0-4)** — largest single edit, and the only one that changes what gets built.
2. **§7 Part B + §8 drift telemetry** — `AGREEING` is #3 and `OVER_PRODUCING` is #4; `length_ceiling` is a declared type; the emitted set is 20, not 10; the real gap is turn-over-turn rates. **(P0-2)**
3. **§3's doc-09 bullet** — replace "industry-wide... never permanent" with doc 09's actual split, including Anthropic's 3–5 and Character.AI's 32,000-vs-500. **(P0-3)**
4. **§7 Part B's Albina clause + a §9 Research task** — Part Five denies the exception §6 grants; decide who wins before world #1 is rewritten. **(P0-7)**
5. **§5(B)'s story-Tier sentence** — delete the file-layout claim; state the `story_retriever.py:148` / `retriever.py:194` asymmetry. **(P0-1)**
6. **§5(D)'s transcript clause** — delete or align with §8. **(P0-5)**
7. **Decision Log lines 13 and 17 + §3's pointer** — supersede all four falsified bullets, not two. **(P0-6)**
8. **Objective 6** — give it a §7 deliverable and a §8 probe, or demote it to Research. **(P1-1)**
9. **§8 additions** — the 16-trait rubric, a per-turn word count, a first-sentence-uptake tally; extend the commit action to the pilot results file. **(P1-2, P1-3, P1-4, P1-6)**
10. **§3's assistant-register omission and the doc-07 build-time/runtime clause; §7 Part B's continuity-regression criterion.** **(P1-3, P1-5, P1-8)**
11. **Sweep the P2s** — parameters.yaml `:102`, Decision-Log `:59`, the Marius composite, the Theon truncation, the four-vs-five layer count.

**Do not re-run a full round 3.** Items 1–7 are corrections to identified sentences with the evidence already in this document, not new research; items 8–11 are additive. A targeted re-check of items 1, 2, 3, and 4 after editing — four paragraphs — is proportionate. What earned this round its keep was checking `f60a112b`'s brand-new material against sources nothing had opened yet: **four of the seven P0s are in prose that was 24 hours old and had never been verified once.**
