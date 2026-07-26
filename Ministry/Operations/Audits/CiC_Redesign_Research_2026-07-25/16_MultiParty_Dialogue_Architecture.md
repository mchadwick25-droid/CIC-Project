# Multi-Party Dialogue Architecture: What Grounding Theory, Conversation Analysis, and Multi-Party Dialogue Systems Research Say About How CiC Allocates and Manages Turns

Every source below was read on 2026-07-25/26. Where I extracted a PDF myself and read the primary text, findings carry **High** confidence. Where I could only reach a fetch-summary, a secondary rendering, or a search snippet, the finding says so and carries **Medium** or **Low**. Six items I could not verify are listed at the end under "Do not cite" so nobody quotes them later on my authority — including one where a fetch summarizer fabricated a taxonomy that does not exist in the paper.

CiC's actual mechanism was read first, in code, not from documentation: `graph/nodes.py` (`determine_turn_type` 2065–2161, `select_next_speaker` 2187–2322, `build_public_transcript` 830–850, `_select_monitor_finding`/`_MONITOR_SIGNAL_PRIORITY` 1499–1530, `check_dominance` 2325–2384, `check_question_stacking` 2606–2644, `generate_reroot_guidance` 1921–1964, `facilitator_reroots` 1999–2025), `graph/state.py` in full, `main.py` 592–630 and 831–1300, and `prompts/table_discourse.py` in full. All paths are under `C:\Users\mchad\Documents\CiC-Project\cic-poc\backend\app\`.

This document deliberately does **not** re-cover doc 10's ground (declining initiative, agreement-drift, verbosity/style drift, states-but-doesn't-enact). Where a finding here touches agreement-drift, it is because the literature locates it at a specific *sequential position* — which is a structural fact about turn organization, not a fact about how natural a single turn sounds.

---

## Summary — the six findings that matter

**1. CiC's "public-transcript isolation boundary" has a precise name in the literature, and the name comes with a cost ledger CiC has never paid.** Clark & Brennan's *Grounding in Communication* (1991) defines eight **constraints on grounding** that a medium may impose, and eleven **costs of grounding** that shift as constraints are removed. Read against that table, Representative-to-Representative communication at CiC's table has exactly **two** constraints — reviewability and sequentiality — and not copresence, visibility, audibility, cotemporality, or simultaneity. Because the streaming endpoint publishes tokens as they are generated, it does not have revisability either. That is a poorer constraint set than any of the seven media Clark & Brennan tabulate. Two consequences follow directly and neither is currently handled: **speaker change costs** are so high that an acknowledgment consumes a whole turn against a `MAX_MULTI_WORLD_TURNS = 6` ceiling, leaving "initiation of the relevant next turn" as the only affordable form of positive evidence; and **other-repair is structurally impossible**, which is exactly the condition under which Clark & Brennan say speakers must prevent faults before sending rather than rely on others to repair. CiC's fabrication and over-settling adjudicators run *after* sending. **Verdict: PARTIAL — the boundary is a defensible, principled choice, and the literature gives it a better name than "isolation." The missing piece is the cost accounting, not the boundary.** Confidence: High.

**2. Every one of CiC's drift signals is negative evidence, and Clark & Brennan name that exact design and say it is not enough.** They write that if negative evidence were all we looked for, "we would often accept information we had little justification for accepting," and that people "ordinarily reach for a higher criterion... positive evidence of understanding." CiC has seventeen distinct drift signal types (see finding 6) and zero positive-evidence mechanisms — nothing anywhere in the pipeline establishes that a Representative understood another Representative, or that the participant understood a Representative, or that the Facilitator understood the participant. The fix has an evaluated architecture behind it: Roque & Traum's **Degrees of Grounding** model attaches a *per-topic grounding criterion* (sensitive topics get a higher one) and a **Grounding component that runs before response generation** and prepends an explicit repeat-back when the criterion is unmet. In two controlled experiments with a deployed virtual human it improved appropriateness-of-response at p<0.01 and p<0.05 respectively — including against a control that produced grounding statements *at the same frequency* but non-methodically. **Verdict: REAL GAP, and the highest-value structural fix in this document.** Confidence: High.

**3. The single-vs-all routing decision does not exist on the live code path — and a multi-world table therefore cannot produce a single-voice answer.** `determine_turn_type`, with the "when genuinely in doubt between single and all, prefer single" default that both the brief (§3) and doc 02 (§5) cite as CiC's governing conservatism, is called from exactly one place: `main.py:595`, inside the **non-streaming** `/message` endpoint. The streaming endpoint never calls it. Instead every multi-world participant turn enters the `select_next_speaker` loop with `MIN_MULTI_WORLD_TURNS = 2`, and `must_continue = turns_completed < 2` is True for iterations 0 and 1, so `select_next_speaker` is forbidden from returning `None` until two Representative turns have completed. The code comment names this as intentional — "2 still guarantees the multi-world contract (more than one voice heard)." The consequence has not been named: when a participant addresses one world by name, a second world is still structurally compelled to speak. That is a direct violation of Sacks, Schegloff & Jefferson's Rule 1a, under which a party selected by a "current speaker selects next" technique "has the right and is obliged to take next turn to speak; no others have such rights or obligations." So the brief's framing — two engines of differing sophistication — understates it: the two engines differ in *which questions they can ask at all*. **Verdict: REAL GAP.** Confidence: High on the code; High on the rule's substance, Medium on its verbatim wording (see Do not cite).

**4. CiC's turn selector has no adjacency-pair rule, and `check_question_stacking` is a symptom-level patch for that missing rule — while the prompt layer actively licenses the behavior the structural layer penalizes.** The best-measured multi-party LLM turn-taking design in the current literature (Nonomura & Mori, *Frontiers in AI* preprint, 2025) implements the Sacks et al. rule set directly: a `detectDesignation()` step that uses an LLM to detect a **first pair part** of an adjacency pair in the previous turn and identify the addressed agent, with a self-selection mechanism as fallback. The combined condition (CSSN-or-SS) significantly reduced dialogue-breakdown utterances against **both** a fixed equal-turns rotation (p<0.001) **and** pure self-selection (p<0.001). Their named failure mode for equal rotation is that a question addressed to someone "requires waiting until one's turn comes around"; their named failure mode for pure self-selection is one high-importance agent "monopolizing turns." CiC has both engines and neither rule: the plain endpoint is equal rotation, the streaming selector is holistic self-selection-by-proxy, and dominance is patched post-hoc by a 70% cumulative word-share heuristic. Meanwhile `table_discourse.py`'s `REACTIVE_TURN_GUIDANCE` contains a section headed **"Ask, Don't Just Answer"** explicitly licensing a Representative to ask another Representative a direct clarifying question — and `check_question_stacking` (nodes.py 2606–2644) fires a medium-severity correction on *every speaker in the round* when more than two turns end with "?". One layer of the system invites other-initiated repair; the next layer penalizes it and never routes the answer to the addressee. **Verdict: REAL GAP, and an internal contradiction between prompt layer and structural layer.** Confidence: High.

**5. The model CiC actually runs has a measured, position-specific repair failure that CiC has no detector for.** Lachenmaier, Bultmann & Zarrieß (2026) probe five models with three third-position repair initiations ("Are you sure?", "Are you sure that X is correct?", "Shouldn't it be 36?"). Claude-Sonnet-4.5 emerges as the **"second-guesser"**: it revises roughly 25% of previously *correct* answers under repair pressure and was the most susceptible of the five to a misleading candidate answer. CiC's `AGREEING` signal reads only the Representative's own response text (`_detect_drift_signal` passes `FACILITATOR_MONITORING_PROMPT.format(response=response_text)` and nothing else) and has no knowledge of whether the preceding participant turn was a repair initiation. So the single highest-risk sequential position for CiC's core conviction — that a world holds its own position under pressure — is precisely the position CiC's monitors cannot see. This is a distinct structural finding from doc 10's agreement-drift result, not a restatement: doc 10 establishes that agreement-drift happens over long conversations; this establishes *which turn position triggers it* and that CiC's monitor is position-blind by construction. **Verdict: REAL GAP.** Confidence: Medium (fetch-summary of an arXiv preprint, not my own read of the PDF; see Do not cite).

**6. There is a second drift-signal bottleneck, undocumented anywhere, and it is worse than the first — it structurally deprioritizes exactly the multi-party table signals.** The brief (§3) names "only one drift signal survives per turn by design" and points at `_select_monitor_finding`. That function is careful: severity first, then a twelve-entry `_MONITOR_SIGNAL_PRIORITY` ordering built after a measured failure. But `pending_guidance` is `dict[str, str]` (state.py 95) — one string per world — and every writer in `main.py`'s background block does a bare assignment: `new_pending_guidance[signal.world_id] = signal.description` (1257) and then `new_pending_guidance[msg_world_id] = generate_reroot_guidance(signal)` (1284). Last writer wins, with **no priority logic at all**. And the ordering is fixed: the five table-level checks (dominance, convergence, cross-world vocabulary, length ceiling, question stacking) all run at 1248–1254, *before* the per-message drift loop at 1269–1284. So any per-turn drift finding silently overwrites every multi-party finding for that world, and `_MONITOR_SIGNAL_PRIORITY` never governs this second bottleneck. RavenClaw's answer to precisely this problem is a **gating mechanism** that "queues up the actions (if necessary) and executes them one at a time." **Verdict: REAL GAP.** Confidence: High.

---

## 1. Conversational grounding theory — Clark & Brennan, and what the isolation boundary is really called

### 1a. The grounding criterion, and why CiC needs one per record rather than one per system

[Clark & Brennan 1991](https://web.stanford.edu/~clark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf) define the criterion verbatim: "The contributor and his or her partners mutually believe that the partners have understood what the contributor meant to a criterion sufficient for current purposes. This is called the grounding criterion." The load-bearing clause is *sufficient for current purposes* — the criterion is not fixed. They devote a whole section to it ("Grounding changes with purpose") and give the worked case of a father instructing a five-year-old, where "the father may go on testing for understanding long after the son thinks he needs to."

Roque & Traum operationalized exactly this: in their deployed system, "offers or sensitive topics... have higher grounding criteria than less-threatening topics such as general social talk."

CiC has no grounding criterion anywhere, at any granularity. But the brief's §9 already specifies the field that would carry one: `conceptual_distance_note` — "why the senses diverge despite sharing a word." A term whose `period_sense` and `modern_sense` diverge sharply *is* a high-grounding-criterion topic in the exact technical sense, and the redesign is already going to compute that divergence. The criterion is a derived value over a field the schema is already getting.

**Verdict: REAL GAP, but a cheap one — the data to compute a per-record grounding criterion is already in the redesign's own schema.** Confidence: High.

### 1b. The eight constraints, and the honest name for the isolation boundary

Clark & Brennan's eight constraints, verbatim from the paper: **Copresence** ("A and B share the same physical environment"); **Visibility** ("A and B are visible to each other"); **Audibility** ("A and B communicate by speaking"); **Cotemporality** ("B receives at roughly the same time as A produces"); **Simultaneity** ("A and B can send and receive at once and simultaneously"); **Sequentiality** ("A's and B's turns cannot get out of sequence"); **Reviewability** ("B can review A's messages"); **Revisability** ("A can revise messages for B").

Their Table 1 assigns constraint sets to seven media. Face-to-face gets six. Letters and email get two (reviewability, revisability). Now read CiC's Representative-to-Representative channel, which is `build_public_transcript`:

- **Reviewability: yes** — the transcript persists. But only the last ten lines: `return "\n\n".join(transcript_lines[-10:])`.
- **Sequentiality: yes** — turns are appended in order.
- **Copresence, visibility, audibility: no** by construction.
- **Cotemporality: no** — a Representative reads a finished string, never a turn in progress.
- **Simultaneity: no** — one speaker at a time is enforced by the loop.
- **Revisability: no.** This is the one worth dwelling on. Letters and email — the two poorest media in Clark & Brennan's table — at least have revisability. CiC gave it up on purpose, by streaming tokens to the participant as they are generated (`stream_representative_turn`, and `main.py`'s `yield sse({"type": "token", ...})`). So the Representative-to-Representative channel at CiC's table has a *strictly poorer* constraint set than any medium Clark & Brennan tabulate.

This is not a criticism of the boundary. It is the correct name for it. The isolation boundary is a **grounding-constraint specification**, and CiC has selected {reviewability, sequentiality}. That framing is more precise and more defensible than "only spoken words cross," because it makes the downstream cost consequences derivable rather than surprising — which is exactly what the current mechanism cannot do.

**Verdict: PARTIAL — WORTH ADOPTING the vocabulary.** Confidence: High.

### 1c. The eleven costs, and the two that CiC is silently paying

Clark & Brennan enumerate eleven costs that shift as constraints are removed: formulation, production, reception, understanding, start-up, delay, asynchrony, speaker change, display, fault, and repair. Two are directly diagnostic for CiC.

**Speaker change costs.** They observe that "the cost of changing speakers is higher in media with fewer cues for changes in turns," and that "one effect of high speaker change costs is that people try to do more within a turn." That is a mechanistic prediction of CiC's own most-tuned problem. The `_WORLD_LENGTH_CEILINGS` work, the `OVER_PRODUCING` signal, the `OPENING_TURN_LARGE_TABLE_GUIDANCE` block, and doc 10's headline "assistant register" finding are all fighting a pressure that Clark & Brennan predict *from the medium's constraint set*. That doesn't make the length work wrong — it makes it symptomatic. If speaker change is cheap, turns get short by themselves. Concretely: the reason a Representative cannot afford a one-line acknowledgment of another Representative is that it would consume one of six turns. A structural fix (cheap sub-turn acknowledgments that don't count against `MAX_MULTI_WORLD_TURNS`) attacks a cause that prompt-level length discipline can only attack as an effect.

**Repair costs.** Verbatim: "In media that are not cotemporal, repairs initiated or made by others become very costly indeed, so speakers will try hard to avoid relying on others to repair misunderstandings. It is less costly for them to revise what they say before sending." CiC's medium is not cotemporal *and* has no revisability. That is the worst quadrant: prevention-before-sending is the only affordable repair strategy, and streaming forecloses it. The fabrication adjudicator and over-settling adjudicator — the two most expensive quality mechanisms in the system, one of them a ~9,250-token call — both run after the participant has read the text. Clark & Brennan also note that "faults tend to snowball," which is why speakers repair "just as soon as they detect a fault."

**Verdict on the cost ledger: REAL GAP.** Confidence: High.

### 1d. Positive versus negative evidence — the sharpest single finding in this section

Clark & Brennan set up and then reject the negative-evidence-only design explicitly: one might suppose "all we need to look for is negative evidence — evidence that we have been misheard or misunderstood... But if negative evidence is all we looked for, we would often accept information we had little justification for accepting. In fact, people ordinarily reach for a higher criterion... people ultimately seek positive evidence of understanding." They give three forms: **acknowledgments** (continuers — "used by partners... to signal that they are passing up the opportunity to initiate a repair on the turn so far and, by implication, that they think they have understood the turn so far"), **initiation of the relevant next turn** (the second part of an adjacency pair, which "is also evidence that she has understood"), and **displays/demonstrations**.

CiC's entire quality architecture is negative evidence. Ten monitoring signals, two adjudicators, five table-level heuristic checks, five classify-then-route intercepts — all of them detect trouble. Nothing establishes understanding. And per the constraint analysis in 1c, of the three forms of positive evidence available to humans, CiC can currently only afford one: initiation of the relevant next turn. Acknowledgments cost a full turn out of six; displays are impossible without copresence.

There is a strong internal argument here that CiC has already made in a neighbouring domain. Doc 12 §2c observes that CiC's retrieval audit endpoint preserves every candidate the retriever considered, retrieved or skipped, and identifies this as the **positive apparatus** choice — "the more expensive and more trusted of the two options." CiC chose the positive apparatus for its source-retrieval audit. It chose the negative apparatus for grounding. Adopting the same discipline one layer over is a consistency argument, not a new conviction.

**Verdict: REAL GAP.** Confidence: High.

### 1e. What grounding theory says CiC's mechanism does not handle at all: the Facilitator is not in the common ground

`build_public_transcript` contains this:

```python
elif hasattr(msg, "name") and msg.name:
    # Skip facilitator messages in transcript for representatives
    if msg.name == "facilitator":
        continue
```

Every Facilitator turn is excluded from the record Representatives share. So a Facilitator anachronism gloss, a frame-breaker answer, a relational-safety intervention, an epistemology-bridge word — none of it enters the Representatives' common ground. In grounding terms the Facilitator is a full participant who contributes to common ground and whose contributions are erased from the shared record.

The sharpest case is the modern-term bridge. Per doc 02 §6 and the brief §4, the bridge hands the Representative a "term-free reframed question that is never persisted to the transcript." Compose that with the exclusion above and the result is: Representative A answers a question that exists nowhere in the record, and Representative B, reading only the public transcript, sees the answer without the question. B's only available form of positive evidence — initiation of the relevant next turn — is being computed against a first pair part that has been deleted.

Roque & Traum's Figure 6 is this exact failure, observed live in their own experiments: the trainee asks "Who are you working for?", ASR/NLU mis-parse it as an offer to protect the family, the system answers the mis-parsed question, and "the Trainee would not be aware that Hassan expects his family to be protected, and the expectations mentioned by Hassan would make no sense." Their fix is the Grounding component's explicit repeat-back of the *understood* topic before answering, and it is the case they use to demonstrate the model's value.

**Verdict: REAL GAP, and the highest-severity grounding gap found.** Confidence: High.

### 1f. Two code-level findings inside the boundary machinery

- **`exclude_world_id` is a dead parameter.** `build_public_transcript(state, exclude_world_id: str = None)` never references it in the body, and a repo-wide search across all `.py` files returns exactly one hit — the definition itself. Whatever per-Representative filtering it was going to express does not exist. This matters more than a typical dead parameter, because it is the signature of the function that *implements a constitutional line*: it advertises a capability to differentiate what each Representative sees, and does not have it.
- **`transcript_lines[-10:]` is a naive sliding window on the constitutional record.** Doc 10 already established the cache-aware rule (hold the truncation point fixed across several turns; Character.AI's ~95% hit rate depends on it) — that rule applies here and this is exactly the naive sliding window it warns against. But there is a second, independent reason it is wrong, from §2 below: next-speaker prediction is the *one* multi-party task where text LLMs beat humans, and the measured reason is that "LLMs can leverage longer conversational histories." The ten-line window throws away precisely the resource that makes the selector work.

---

## 2. Multi-party dialogue management and addressee selection

This is a real, named subfield. [Multi-Party Conversational Agents: A Survey](https://arxiv.org/html/2505.18845v1) organizes it around the decomposition of what an agent must decide — "when to speak, whom to address, and what to say" — yielding three named subtasks: **turn detection**, **addressee selection**, and **agent response**. Confidence: Medium-High (read via fetch-summary of the HTML, not my own full read).

### 2a. CiC conflates two subtasks that the literature separates — and gets the harder one for free

CiC's `select_next_speaker` answers "whom shall I call on." It never answers "whom is this turn addressed to." There is no addressee field anywhere: `ConversationState` has `current_speaker`, `current_world_id`, and `world_ids`, and nothing else about participant roles. [SI-RNN](https://arxiv.org/abs/1709.04005) (Zhang, Lee, Polymenakos & Radev, AAAI 2018) frames the difficulty exactly: "multiple speakers exchange messages with each other, playing different roles (sender, addressee, observer), and these roles vary across turns." CiC represents the sender only.

That matters because the two subtasks have opposite difficulty profiles for LLMs, and a recent evaluation on the AMI corpus quantifies both. [Fukuda et al., 2026](https://arxiv.org/pdf/2606.17542) report, against a naive baseline and human subjects:

| Task | Naive baseline | Human | Qwen3-14B | Gemini 2.5 Pro |
|---|---|---|---|---|
| Addressee detection (Acc) | 28.4 | 66.6 | 51.5 (sig. worse than human) | 61.4 |
| Turn-change prediction (Acc) | 64.6 | 75.0 | 67.4 | 69.8 |
| Next speaker prediction (F1) | 25.0 | 60.1 | **69.4 (sig. better than human)** | 57.7 |

Their explanation for the one task where LLMs win: "Unlike supervised models, which rely only on features from the immediately preceding utterance as context, LLMs can leverage longer conversational histories, likely contributing to their advantage in this task."

Three concrete consequences for CiC:

1. **CiC's Haiku-based next-speaker selector is operating in the regime where LLMs are genuinely strong** — better than humans, on a task where even humans reach only F1 60 with four candidates. That is real validation of the architecture choice, and it should be stated as such rather than hedged.
2. **The advantage is explicitly attributed to long context, which `build_public_transcript` truncates to ten lines.** This is the same finding as 1f, arriving from a second, independent direction.
3. **CiC should not solve addressee detection with an LLM judgment call.** It is the task where LLMs underperform humans significantly and sit only modestly above a naive baseline. The alternative is structural detection — see 3b.

**Verdict: PARTIAL. Next-speaker selection: ALREADY DOES THIS, and in the right regime. Addressee representation: REAL GAP, and the fix is structural, not a new classifier.** Confidence: High for the numbers (read the paper directly); High for the SI-RNN abstract.

### 2b. Self-selection is where LLMs collapse — and CiC's architecture sidesteps that, deliberately or not

[Inner Thoughts](https://arxiv.org/abs/2501.00383) (Liu et al., 2024/2025) is the strongest recent argument against next-speaker-prediction-from-context, and its critique is specific: "decisions to self-select and participate are largely influenced by covert internal processes — such as a participant's interest, relevance, or motivation to engage — which are not easily observable from explicit conversational data." Their measured result: GPT models reached roughly **12% accuracy in self-selection cases** against a ~12.7% random baseline, versus 70%+ in turn-allocation contexts where explicit cues exist.

CiC's Facilitator-allocates design is squarely in the 70%+ regime. That is a real, non-obvious win, and it is worth knowing that the governance conviction ("not rotation, not equal time, but which voice is most directly positioned") happens to land CiC on the tractable side of the hardest split in this literature.

The tension is also real and worth naming precisely. Inner Thoughts' remedy is a five-stage pipeline — **Trigger → Retrieval → Thought Formation → Thought Evaluation → Participation** — in which each agent maintains "a continuous, covert train of thoughts in parallel to the overt communication process" and an intrinsic-motivation score gates expression. That covert pre-verbal state is exactly what CiC's isolation boundary forbids from crossing between Representatives.

But it does not have to cross. The boundary prohibits *content*, not *the existence of a bid*. A Representative could compute a scalar within its own private context and pass only that scalar to the Facilitator — a **sealed-bid turn allocation**. No world's reasoning reaches another world; the Facilitator gains a self-selection signal it currently has to infer from the transcript alone; and the constitutional line holds exactly as written. Their score's eight heuristic factors are directly reusable as the bid's rubric: relevance, information gap, expected impact, urgency, coherence, originality, **balance**, and dynamics. Note that *balance* is the dominance problem expressed as a positive selection input rather than a post-hoc 70% word-share penalty.

Confidence: Medium (fetch-summary of the HTML for the stage names, score formula, and 12% figure; the abstract I read verbatim).

**Verdict: PARTIAL — WORTH ADOPTING, in a boundary-preserving form.**

### 2c. The moderation literature has a validated taxonomy for the Facilitator's job, and CiC performs two of its six acts

[WHoW](https://arxiv.org/abs/2410.15551) (Zhang et al.) is an evaluation framework for moderator facilitation strategies across domains, built on three dimensions — **Why** (motives), **How** (dialogue acts), **Who** (target speaker) — with 5,657 human-annotated and 15,494 GPT-4o-annotated moderation sentences from TV debates and radio panel discussions. Verbatim from Table 1:

*Motives:* **Informational** — "Provide or acquire relevant information to constructively advance the topic or goal of the conversation." **Coordinative** — "Ensure adherence to rules, plans, and broader contextual constraints." **Social** — "Enhance the social atmosphere and connections among participants."

*Dialogue acts:* **Probing** — "Prompt speaker for responses." **Confronting** — "Prompt one speaker to response or engage with another speaker's statement, question or opinion." **Instruction** — "Explicitly command, influence, halt, or shape the immediate behavior of the recipients." **Interpretation** — "Clarify, reframe, summarize, paraphrase, or make connection to earlier conversation content." **Supplement** — "Enrich the conversation by supplementing details or information without immediately changing the target speaker's behavior." **Utility** — everything else.

Their headline cross-domain finding: "debate moderators emphasise coordination and facilitate interaction through questions and instructions, while panel discussion moderators prioritize information provision and actively participate in discussions."

Mapped onto CiC's Facilitator: **Interpretation** is well developed (the anachronism bridge is a textbook Interpretation act — clarify and reframe). **Instruction** exists but only invisibly, via `pending_guidance`. **Supplement** exists in the frame-breaker and epistemology-bridge responses. **Probing** and **Confronting** are at zero at the table, by explicit governance decision — `main.py` 1174–1182 cites Facilitator Governance V3.6 §12: "most encounters should never require the room to acquire a voice"; "if the Facilitator is present in the middle of a rich encounter, the governance is too loud."

I am not going to argue against that conviction; it is a real one and it is well reasoned in the code comment itself. But the tradeoff should be named, because **Confronting is the one act in the taxonomy that exists specifically to make a multi-party table work** — it is the act that turns parallel monologues into an exchange, and it is the act CiC's `check_convergence` and `check_question_stacking` are both indirectly compensating for.

And there is a middle path that costs nothing in Facilitator voice. `select_next_speaker` already composes a private prompt for the selection decision and discards the `REASON:` line it asks for. A Confronting act can be delivered *there* — as a private directive attached to the selection ("you are being called on because Chloe named X; engage that specifically") rather than as a spoken Facilitator turn. The act happens; the room never acquires a voice. This is strictly cheaper than a spoken turn and it uses a field the selector already generates and throws away.

**Verdict: PARTIAL — WORTH ADOPTING, as a private directive rather than a spoken act.** Confidence: High (read the paper's framework section and appendix directly).

---

## 3. Turn-taking models from conversation analysis

### 3a. What the model actually offers CiC, and what it does not

Sacks, Schegloff & Jefferson (1974), *Language* 50: 696–735, decompose turn-taking into a **turn-constructional component** (turns are built from turn-constructional units, TCUs) and a **turn-allocational component** (a rule set applied at each **transition-relevance place**, the point of possible completion of a TCU where speaker change becomes a possible next action). The rules, in substance: **1a** — if the turn-so-far uses a "current speaker selects next" technique, the selected party has the right and obligation to take the next turn and no others do; **1b** — otherwise any party may self-select, first starter gets the turn; **1c** — otherwise the current speaker may but need not continue; and the rule set reapplies recursively at each next TRP. (Confidence: High on substance, Medium on verbatim wording — I could not retrieve the primary paper; see Do not cite.)

The task asked whether this offers CiC a more principled way to decide "has this speaker naturally finished." **The honest answer is mostly no, and that is worth stating plainly rather than manufacturing a mapping.** Projectability and TRP-detection are answers to a problem CiC does not have: CiC's turns do not have to be *detected* as complete, because generation terminates deterministically. The turn boundary is set by `PRIMARY_TURN_MAX_TOKENS` / `REACTIVE_TURN_MAX_TOKENS` / a stop sequence, not inferred from an incoming stream. Importing TRP machinery here would be borrowing the vocabulary without the problem.

What the model *does* offer CiC is the **allocation** half, and that half is directly actionable.

### 3b. Rule 1a is the missing rule, and implementing it has a measured effect

[Nonomura & Mori, "Who Speaks Next?"](https://arxiv.org/pdf/2412.04937) (arXiv:2412.04937v2, submitted to *Frontiers in Artificial Intelligence*, Feb 2025) built "Murder Mystery Agents," which implements two named mechanisms from Sacks et al. — "Self-Selection" and "Current Speaker Selects Next" — with these modules:

- `think()` — each agent, every turn, generates a thought, chooses "speak" or "listen," and emits an **importance** integer 0–9.
- `selectMostImportant()` — implements self-selection: single speaker wins trivially; multiple speakers resolved by highest importance; ties broken randomly "to represent the uncertainty of turn-taking in actual conversations"; and if all agents choose "listen," the previous speaker continues — which they note implements Rule 1c directly.
- `detectDesignation()` — implements Rule 1a: "uses the LLM to determine if a first pair part of an adjacency pair is present in the previous turn's utterance. When a first pair part is detected, it simultaneously classifies its type (Yes/No question, addressing, etc.) and estimates the agent addressed by the utterance."

Three conditions compared: EQUAL (equal turns/opportunities), SS (self-selection only), CSSN-or-SS (designation first, self-selection as fallback). Result: Kruskal-Wallis χ² = 42.171, p<0.001 across conditions, and Dunn's test with Bonferroni correction showed CSSN-or-SS significantly reduced breakdown utterances against **both** EQUAL (p<0.001) and SS (p<0.001). LLM-as-judge coherence, cooperativeness and diversity all showed significant differences (χ² = 51.784 / 56.718 / 52.973, all p<0.001).

Their two named failure modes are CiC's two engines:

- **EQUAL's failure**, in their words: when a first pair part occurs — "such as addressing someone or asking a specific question" — the second pair part "requires waiting until one's turn comes around, which may result in inefficient conversation." That is the plain endpoint's `multi_representative_engages`, which marches through `responding_worlds` in fixed order.
- **SS's failure**: "an agent with high importance scores monopolizing turns." That is CiC's dominance problem, currently addressed by `check_dominance`'s cumulative-70%-word-share heuristic *after the fact*, delivered as guidance to a later turn that may never come.

CiC's streaming selector implements neither rule. Its prompt reasons holistically over the transcript ("which representative is most directly positioned"), which can *incidentally* honor a direct question, but nothing guarantees it — and nothing in the code notices whether a first pair part is outstanding. `check_question_stacking` notices the *accumulation* of outstanding first pair parts and responds by telling every speaker in the round to stop asking. That is treating the symptom while the cause — no routing rule for the second pair part — goes unaddressed. And it sits in direct contradiction with `REACTIVE_TURN_GUIDANCE`'s "Ask, Don't Just Answer" section, which licenses exactly the act the check penalizes.

One further note on `check_question_stacking`'s detector: it counts only turns where `turn.endswith("?")`. A turn that asks a real question mid-paragraph and closes on substance — which `REACTIVE_TURN_GUIDANCE` explicitly asks for elsewhere — is invisible to it. So the check both over-penalizes the shape it can see and misses the shape the prompt recommends.

**Verdict: REAL GAP. Rule 1a is the single highest-value addition to `select_next_speaker`, and unlike most recommendations in this document it has a controlled measurement behind it.** Confidence: High (read the full paper text).

### 3c. What CA correctly warns CiC away from

CiC should *not* adopt overlap, interruption, or simultaneous-start modeling. Clark & Brennan's own constraint analysis explains why: simultaneity is absent from CiC's medium, and asynchrony costs are described as making timing-dependent grounding techniques "altogether impossible" without cotemporality. Any attempt to simulate overlap in a text medium would be importing surface features of a medium CiC does not inhabit — which is the same error doc 09 flags for emotion sprites and individual-figure reconstruction.

**Verdict: DOESN'T APPLY, and worth recording as a deliberate exclusion.** Confidence: High.

---

## 4. Mixed-initiative dialogue design

[Horvitz, "Principles of Mixed-Initiative User Interfaces," CHI 1999](https://dl.acm.org/doi/pdf/10.1145/302979.303030) gives twelve critical factors. Read against CiC's Facilitator, this literature is largely *validating* — CiC independently arrived at four of the twelve, including two of the subtler ones. Two are real gaps, and one is a genuine, unresolved tension with CiC's own governance.

**Where CiC already does this, and should say so:**

- **(8) Scoping precision of service to match uncertainty** — "a preference for 'doing less' but doing it correctly under uncertainty." This is `determine_turn_type`'s "when genuinely in doubt between single and all, prefer single" verbatim in substance. **ALREADY DOES THIS** — though see finding 3: it does it on the dead code path.
- **(3) Considering the status of a user's attention in the timing of services** — "consider the costs and benefits of deferring action to a time when action will be less distracting." CiC's decision to run all drift checking *after* the `done` event is exactly this principle, and the code comment reasons its way there independently: "it used to run before 'done' was sent, costing several seconds of invisible latency for zero visible benefit." **ALREADY DOES THIS.**
- **(4) Inferring ideal action in light of costs, benefits, and uncertainties** — expected-value-guided invocation. CiC's two adjudicators, deliberately biased in *opposite* fail-open directions ("a missed fabrication is the cardinal sin"; a false OVER_SETTLED "manufactures false uncertainty"), are a qualitative expected-utility calculation with asymmetric loss. This is more sophisticated than most production guardrail design and should be named as such. **ALREADY DOES THIS.**
- **(7) Minimizing the cost of poor guesses about action and timing** — partially. The `must_continue` fallback to `candidates[0]` on an unparseable selector response is a correct application. But `MIN_MULTI_WORLD_TURNS = 2` runs *against* this factor: it locks in a possibly-wrong fan-out for two turns. Given that even human next-speaker F1 is 60.1 (§2a), the base rate of poor guesses here is high by nature, and a floor that forecloses correction raises their cost. **PARTIAL.**

**The real gaps:**

- **(6) Allowing efficient direct invocation and termination** — "efficient means by which users can directly invoke or terminate the automated services." CiC's participant has no control surface over turn allocation at all. They cannot end a round in flight, cannot ask for another voice, cannot ask for one voice only. Direct address by name is honored on the dead endpoint and structurally overridden on the live one (finding 3). **REAL GAP** — and the cheapest possible fix is a single participant-side affordance, not a new model.
- **(11) Maintaining working memory of recent interactions** — "provide mechanisms that allow users to make efficient and natural references to objects and services included in 'shared' short-term experiences." The ten-line window again, from a third independent direction.

**The genuine tension, stated rather than resolved:**

- **(5) Employing dialog to resolve key uncertainties** — "If a system is uncertain about a user's intentions, it should be able to engage in an efficient dialog with the user, considering the costs of potentially bothering a user needlessly." This is in direct tension with Facilitator Governance V3.6 §12's near-silent Facilitator. And the brief §8.5 names a live bug that is precisely a case where one clarifying line would have resolved it: "a term-matching gap that let a universal question misfire as a narrow modern doctrine," plus the known "bare universal question meeting a seated table" pattern.

The resolution is not "make the Facilitator chattier." It is that Horvitz's factor and CiC's governance are answering different questions, and the literature in §6 below supplies the form that satisfies both: not a clarifying question ("what did you mean?") but a **restricted offer** — a candidate understanding embedded in the answer's own opening, which is a grounding act rather than an interruption. Roque & Traum's system does exactly this ("So, you offer me money") and their Grounding component prepends it to the substantive reply rather than taking its own turn.

**Overall verdict for area 4: PARTIAL — mostly validating precedent, with two cheap concrete gaps and one tension that §6 resolves.** Confidence: High (read all twelve factors verbatim from the paper text).

---

## 5. Drift and consistency monitoring architecture in multi-party conversational AI

### 5a. The RavenClaw pattern — the closest architectural match to CiC's problem found anywhere in this research

[Bohus & Rudnicky, "Error Handling in the RavenClaw Dialog Management Architecture," HLT-EMNLP 2005](https://aclanthology.org/H05-1029/) is a twenty-one-year-old spoken-dialogue architecture that solves, structurally, three problems CiC currently has. From the paper directly:

1. **Decoupling.** "The responsibility for handling potential errors is delegated to the Error Handling Process which runs in the Dialog Engine." Developers "focus exclusively on describing the dialog control logic" while error handling is "transparently generated" by the engine. New strategies "can be easily plugged into any existing RavenClaw-based spoken dialog system." — This is the answer to CiC's two-engine problem. The reason CiC's plain endpoint has none of the streaming endpoint's dominance/convergence/cross-world-vocabulary/length/question-stacking checks is that all of it is hand-wired in `main.py`'s endpoint bodies rather than living in a layer both paths pass through. RavenClaw's answer is not "unify the two engines" — it is "extract governance to the engine so the number of engines stops mattering."

2. **Distributed local decision processes instead of one global slot.** "The error handling decision process is implemented in a distributed fashion, as a collection of local decision processes. The Dialog Engine automatically associates a local error handling process with each concept, and with each request agent in the dialog task tree." — This is the direct structural alternative to CiC's "only one drift signal survives per turn." CiC's answer to signal contention was to build a careful priority ordering for a single slot. RavenClaw's answer was to stop having a single slot.

3. **A gating mechanism.** "At every system turn, each concept- and request-agent error handling process computes and forwards its decision to a gating mechanism, which queues up the actions (if necessary) and executes them one at a time." — This is the fix for finding 6, CiC's undocumented second bottleneck. `pending_guidance: dict[str, str]` with bare assignment is a slot; a gate with a queue is the pattern.

4. **Strategies pushed onto a dialog stack, executed, popped, and the dialog resumes.** "Whenever necessary, it will insert an error handling strategy on the dialog stack... The strategy executes and, once completed, it is removed from the stack and the dialog resumes from where it was left off." — This is Clark & Brennan's embedded contribution and CA's insertion sequence, implemented. CiC has no stack anywhere; `closing_stage` is a flat five-state machine, and correction never inserts anything into the flow — it only decorates a hypothetical future turn.

5. **Belief update after repair.** "On completion, the strategy updates the confidence score of the confirmed hypothesis in light of the user response." — CiC never records whether a correction worked. `pending_guidance` is popped and discarded; `facilitator_reroots` sets `requires_reroot: True` and moves on. There is no closed loop.

Their strategy taxonomy is also directly reusable, split by problem type. For **misunderstandings**: Explicit Confirmation, Implicit Confirmation, Rejection. For **non-understandings**: AskRepeat, AskRephrase, Reprompt, DetailedReprompt, Notify, Yield, MoveOn, YouCanSay, FullHelp. Note that CiC's `generate_reroot_guidance` currently generates free-form corrective prose from a Haiku call — and the code documents a real incident where doing so was actively harmful: handed an OVER_SETTLING signal, "the reroot model invented supporting sources and told a ~95-155 AD householder to contrast 'Tertullian's rigorism' with the Shepherd of Hermas." The fix applied was to bypass generation for that one signal and pass the adjudicator's own words through. A closed strategy taxonomy generalizes that fix to all signals: a strategy is selected, not composed.

**Verdict: REAL GAP, and the single most transferable architectural pattern in this document.** Confidence: High (read the paper text directly, including the architecture figures' captions and the strategy list).

### 5b. Event sourcing — the pattern that makes repair structurally possible

[Fowler, "Event Sourcing"](https://martinfowler.com/eaaDev/EventSourcing.html): "Capture all changes to an application state as a sequence of events." The event log is the system of record; current state is derivable from it. The four named benefits are complete rebuild, temporal query, **event replay** — on discovering a past error, reverse the incorrect event and its successors, then replay corrected — and audit trail.

CiC's conversation state is the opposite: a mutable `ConversationState` dataclass held in an in-memory `sessions` dict and overwritten in place. The code already documents the symptom this produces, at `main.py` 1286–1290: "Re-read and merge rather than overwrite wholesale — since 'done' already went out above, the participant's next message may have already been appended to this session by the time this background work finishes, and a blind overwrite here would clobber it." That is a read-modify-write race, hand-patched. It is the canonical problem event sourcing exists to remove.

Two things make this recommendation stronger than a generic architecture suggestion:

- **CiC already chose this discipline one layer down and knows why.** Doc 12 §1d records that the Source Registry protocol is append-only: "never renumber, never delete, a discredited source moves to Confidence E and disposition removed-from-use but stays as a record of what was tried," and identifies this as the same principle PREMIS encodes for digital provenance. CiC applies event-sourcing discipline to source data and mutable-state discipline to conversation state. Adopting the discipline it already chose is a consistency argument.
- **Event replay is the only mechanism found in this entire research that could make CiC's detected errors *correctable*.** Right now, per `main.py` 1204–1208: "Everything below this point — dominance/convergence, monitoring, reroot — is post-hoc by design: none of it can change the turn the participant just read." An event-sourced transcript with a `correction` event type changes what that sentence has to mean. It also gives the audit endpoint temporal query, which it currently approximates by accumulating lists.

**Verdict: REAL GAP — WORTH ADOPTING, and it is a prerequisite for area 6's recommendations rather than an independent improvement.** Confidence: High for the pattern definition (Medium on the verbatim quotes, taken from a fetch-summary of the page); High for the CiC-side code facts.

### 5c. Resolving the drift-signal count, and a live type/runtime mismatch

The brief §3 flags "an unresolved drift-signal count (6→7→9→10→11→12 across documents)." Read against the code, there are four distinct live lists and they resolve cleanly:

| Where | Count | Contents |
|---|---|---|
| `FACILITATOR_MONITORING_PROMPT` (facilitator_prompts.py 132–173) | **10** | SMOOTHING, GENERATING, AGREEING, OVER_PRODUCING, TEMPORAL_BLEED, FLATTENING, FABRICATION, APOLOGETICS, FIRST_PERSON, SELF_NARRATION |
| `_MONITOR_SIGNAL_PRIORITY` (nodes.py 1499–1503) | **12** | the 10 above + `anachronism` (documented legacy alias for temporal_bleed) + `over_settling` |
| `valid_signals` (nodes.py 1604–1608) | **12** | identical set to the priority list |
| `DriftSignal.signal_type` Literal (state.py 14–30) | **15** | 10 monitor signals + `anachronism` + the 5 table-level heuristic signals (dominance, convergence, cross_world_vocabulary, length_ceiling, question_stacking) — but **not** `self_narration` and **not** `over_settling` |

The true number of distinct signal types the system can emit is **17**: the 15 declared, plus `self_narration` and `over_settling`, both of which are accepted by `valid_signals` and both of which are actually constructed — `nodes.py:1780` builds `DriftSignal(signal_type="over_settling", ...)` directly, and `nodes.py:1648` passes a validated `signal_type` through that can be `"self_narration"`.

So the declared type is out of sync with the emitted set for exactly two signals, and they are two of the most governance-critical: `over_settling` is one of the two dedicated screen-then-adjudicate pairs in the system, and `self_narration` is the signal added specifically to close the backstop that doc 02 §6 records as having been "fiction until 2026-07-16." A `@dataclass` does not validate `Literal` annotations at runtime, so nothing breaks today. Any future migration to a validating model, or any type-checked refactor, would silently reject or drop precisely these two.

**Verdict: REAL GAP — and it is a one-line fix that also settles a documentation question the brief lists as open.** Confidence: High.

### 5d. On the persona-drift-detection literature specifically

I looked for a production-grade drift-monitoring pattern beyond doc 10's scope and found the field thinner than the marketing suggests. [Nautilus Compass](https://arxiv.org/html/2605.09863) (Wang, arXiv:2605.09863, May 2026) is the closest match — black-box, prompt-text-layer only, hooked at `UserPromptSubmit` / `PostToolUse` / `Stop`, with cosine similarity between user prompts and "behavioral anchor texts" as the core signal, reporting drift-detection AUC 0.83 and mixed steering results (significant on fabrication-resistance at p<0.05, minimal aggregate effect across vendors). It is a single-author preprint from a company, unreplicated.

The transferable part is not the technique — CiC's LLM-judged signals are considerably more semantically precise than embedding cosine similarity. It is the **hook-point architecture**: drift detection sited at named lifecycle events rather than inline in the request handler. That is the same insight as RavenClaw's decoupling, arrived at 21 years later, and it is worth noting the convergence.

**Verdict: PARTIAL — the hook-point framing transfers; the detection method does not, and CiC's is better.** Confidence: Low-Medium (fetch-summary of a single unreplicated preprint).

---

## 6. Repair and error-correction in conversation

### 6a. CiC has no repair mechanism, in the technical sense — and this is the one place where the gap is total

Repair in conversation analysis is organized along two axes — who initiates and who executes — yielding self-initiated self-repair, self-initiated other-repair, other-initiated self-repair, and other-initiated other-repair. Schegloff, Jefferson & Sacks (1977), *Language* 53: 361–382, established the strong empirical skewing toward self-repair and the operation of a **preference for self-correction**. Schegloff (1992), *American Journal of Sociology* 97(5): 1295–1345, extends this to **third-position repair** — the first speaker's opportunity, after seeing the recipient's response, to accept or repair the understanding that response displayed — and names it "the last structurally provided defense of intersubjectivity in conversation." (Confidence: High on the concepts; Medium on paginations, taken from search results rather than the articles.)

Against that, CiC's full correction inventory:

| Mechanism | Initiated by | Executed by | Visible to participant | Affects the record |
|---|---|---|---|---|
| `pending_guidance` (streaming) | Facilitator | the drifting Representative, on a *later* turn | No | No |
| `facilitator_reroots` (plain endpoint only) | Facilitator | whoever speaks next | No | No |
| Modern-term bridge | Facilitator | Facilitator, pre-emptively | Partially — the gloss is spoken, the reframed question is not persisted | Deletes, does not correct |
| Frame-breaker / epistemology bridge | Facilitator | Facilitator | Yes | Adds, does not correct |

Every row is Facilitator-initiated and prospective. **There is no other-initiated repair anywhere** — no path by which the participant signals trouble with a Representative's turn and gets that turn repaired, and no path by which one Representative's repair initiation is structurally routed to the addressee (§3b). And there is no self-initiated repair either, because streaming removes revisability (§1c). CiC's only defense of intersubjectivity is prevention, and prevention runs after publication.

The literature says this is the normal state of the field and names it as a failure. [Ngo, Rollet, Pelachaud & Clavel, "'Mm, Wat?' Detecting Other-initiated Repair Requests in Dialogue," EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1168.pdf) (pp. 22926–22939), verbatim from the abstract: "Conversational Agents (CAs) still fail to recognize user repair initiation, leading to breakdowns or disengagement." Their detection method is multimodal Dutch spoken dialogue with prosodic features and does **not** transfer to CiC's text-only medium — I want to be explicit about that rather than overclaim.

What does transfer is their coding typology, and one number in it. They classify repair initiation as **open request** ("the least specific, not giving clues of trouble"), **restricted request** (implied trouble-source location), or **restricted offer** (a candidate understanding put forward for confirmation). Their annotated distribution: **10 open requests, 31 restricted requests, 252 restricted offers.** The restricted offer is ~86% of real other-initiated repair.

That is a concrete design number, and it converges with two independent findings above:

- Roque & Traum's Grounding component's chosen act, when a grounding criterion is unmet, is a **Repeat Back** — which is a restricted offer ("So, you offer me money").
- Horvitz's factor (5), employ dialog to resolve uncertainty, in the one form that does not require the Facilitator to acquire a voice.

Three independent literatures converge on the same single mechanism: **a candidate-understanding offer, embedded in the answering turn rather than taking a turn of its own.** That is the highest-confidence concrete recommendation in this document, and it is the direct fix for the modern-term bridge's deleted-question problem (§1e).

**Verdict: REAL GAP — total.** Confidence: High.

### 6b. The model-specific repair vulnerability CiC is exposed to right now

[Lachenmaier, Bultmann & Zarrieß, "Talking to a Know-It-All GPT or a Second-Guesser Claude?"](https://arxiv.org/html/2604.19245v1) (Bielefeld University, arXiv:2604.19245v1, April 2026) probe five models on the Unanswerable Math Word Problems dataset with three third-position repair initiations: an open-ended "Are you sure?", a trouble-source-identifying "Are you sure that [answer] is correct?", and a misleading alternative "Shouldn't it be 36?".

Their result for the model CiC runs: **Claude-Sonnet-4.5 revises approximately 25% of previously correct answers** under repair pressure and shows the highest susceptibility to the misleading alternative of the five models tested. GPT-4o exhibits the mirror failure — "largely impervious to misleading prompts but rarely revises incorrect answers." The paper frames these as "characteristic form[s] of unreliability" rather than a uniform deficiency.

Two things follow for CiC, and they pull in opposite directions, which is why this needs to be handled deliberately rather than with a single instruction:

1. **CiC's core conviction is at structural risk at exactly one turn position.** A participant who pushes back on a Representative — "are you sure the desert fathers really said that?", "shouldn't it be the other way around?" — is issuing a third-position repair initiation, and the model CiC runs is the most likely of five tested to cave. This is not doc 10's general agreement-drift; it is a specific, nameable sequential position with a measured effect size, and CiC's `AGREEING` monitor cannot see it because `_detect_drift_signal` is handed the response text and nothing else.
2. **But the same disposition is load-bearing for CiC's rigor.** A Representative that *never* revises under correction is GPT-4o's failure mode, and it is worse for CiC — a fabrication that survives every challenge is exactly the cardinal sin `_adjudicate_fabrication` exists to prevent. So the recommendation is not "make the Representative resist repair." It is that the two cases must be distinguished, and the distinguishing information is available: **whether the pushback is factually grounded is a question about the world's own record**, which `_gather_world_evidence` already answers for the two adjudicators. A repair-initiation classifier that routes to a *held-position* check for a claim the record supports and to a *concession* path for a claim it does not is a straightforward composition of two mechanisms CiC already has.

**Verdict: REAL GAP, highest urgency of anything in this document, because it is live today on the model in production.** Confidence: Medium (I read a fetch-summary of the HTML, not the paper myself; the numbers are as reported by that summary — see Do not cite).

### 6c. One thing CiC does have, which the repair literature makes legible

`REACTIVE_TURN_GUIDANCE`'s **"Ask, Don't Just Answer"** section — "If something another representative said is genuinely unclear to you... you may ask them directly rather than assuming and responding anyway — 'when you say X, do you mean...'" — is a licence for other-initiated repair in the **restricted offer** format, written in the correct linguistic form, apparently by instinct. And **"Name What They Actually Said"** — "Name the specific thing they said, in your own words, before you agree or differ with it" — is a licence for exactly the Repeat Back that Roque & Traum's Grounding component produces.

So CiC's prompt layer already knows what the right grounding acts are. What is missing is everything structural around them: nothing routes the answer to a restricted offer (§3b), nothing verifies that a "you named X" was *accurate* (there is no misattribution signal in any of the four signal lists in §5c, and `check_convergence` catches nearly the opposite failure — borrowing another's vocabulary, not misreporting it), and `check_question_stacking` penalizes the offer's existence.

**Verdict: PARTIAL — the acts are licensed, the architecture doesn't support them, and one check works against them.** Confidence: High.

---

## Do not cite

Six items I could not verify to the standard the rest of this document holds. Nobody should quote these on my authority.

1. **A "five named dimensions" taxonomy for the Common Ground benchmark** — communication clarity, alignment verification, context awareness, disambiguation handling, feedback integration. **This does not exist in the paper.** A fetch summarizer generated it. I then extracted the PDF and read the actual abstract: [Poelitz, Doshi-Velez & Lindley, "A Benchmark to Assess Common Ground in Human-AI Collaboration"](https://arxiv.org/pdf/2602.21337) (Microsoft Research Cambridge / Harvard, arXiv:2602.21337v1, Feb 2026) is built on "a collaborative puzzle task that requires iterative interaction, joint action, referential coordination, and repair under varying conditions of situation awareness," and its finding is that the benchmark "reproduces established theoretical and empirical findings from human–human collaboration, while also revealing clear divergences in human–AI interaction." Its one directly quotable claim for CiC, citing Wu et al. 2025: "AI models do not show the interaction patterns needed to build common ground in human-AI interaction, and that when models are adapted to perform more of these, human-AI collaboration improves." Flagging this explicitly because it is a live demonstration of the failure mode: a plausible-sounding taxonomy attributed to a real paper. **Confidence in the corrected version: High.**

2. **Traum's grounding-acts list** (initiate, continue, acknowledge, repair, request-repair, request-ack, cancel). Widely reported, and Traum's 1994 Rochester dissertation *A Computational Theory of Grounding in Natural Language Conversation* is real and load-bearing for this whole area — but I could not extract the primary text. Cite Traum 1994 as the origin of computational grounding acts and Common Ground Units; do not quote the act list on my authority. Roque & Traum's own description, which I did read, is that Traum's model "uses common ground units (CGUs) [Nakatani and Traum, 1999] to represent the content being grounded, and grounding acts to describe the utterances that ground the common ground units." That much is safe.

3. **Verbatim wording of the Sacks, Schegloff & Jefferson 1974 rule set.** The primary paper exceeded my fetch size limit. Rule 1a's wording above came from a search snippet; 1b and 1c are paraphrases from secondary renderings including [Wikipedia's TCU page](https://en.wikipedia.org/wiki/Turn_construction_unit). The substance is not in doubt — it is the most-cited paper in conversation analysis and Nonomura & Mori's implementation independently corroborates the rule structure — but quote it from the original before putting it in a governance document. Full citation: *Language* 50(4): 696–735.

4. **Exact numbers from Lachenmaier et al. 2026** — the ~25% revision rate, the 1,127 misleading-answer instances, the 69.7% problem-flagging figure. These come from a fetch-summary of the HTML, not my own read. The directional finding (Claude as "second-guesser," most susceptible to misleading repair among five models tested) is stated in the paper's own framing and is safe; verify the specific numbers before citing them.

5. **Inner Thoughts' score formula and stage-level detail**, including the eight heuristic factors with their mention counts and the 12%-versus-12.7% self-selection figure. Fetch-summary, not my own read. The abstract I did read verbatim, and it supports the core claim ("we demonstrate the limitations of such methods" for next-speaker prediction from preceding context; the covert-thoughts framing; significant improvement on "anthropomorphism, coherence, intelligence, and turn-taking appropriateness"). Also note: arXiv:2501.00383 has no traditional venue listed as of this reading.

6. **The Multi-Party Conversational Agents survey's Table 1 SOTA numbers, and the negative claim that it "does not address moderator roles."** Both come from a fetch-summary. The three-subtask decomposition (turn detection / addressee selection / agent response) and the when/whom/what framing are corroborated by multiple independent sources and are safe. Also: **Nautilus Compass's AUC 0.83** — single-author, unreplicated, company-affiliated preprint, read via summary. Treat as an existence proof of the hook-point pattern, not as a benchmark.

---

## Prioritized recommendations for the facilitator-governance redesign

Ordered by expected value per unit of design and build effort. Each names the pattern, the source, and the specific code it would replace or supplement.

### Tier 1 — do these; they are cheap, load-bearing, and each has a named pattern behind it

**1. Add a third-position repair-initiation classifier, routed to a held-position-versus-concede decision, and put it in the intercept chain.**
*Replaces:* nothing — this is net new, and it is the only Tier-1 item that closes a live risk on the model in production.
*Pattern:* CA third-position repair (Schegloff 1992) + the model-specific vulnerability in Lachenmaier et al. 2026.
*Design:* a sixth classifier alongside frame-breaker / relational-safety / modern-term / epistemology-bridge, on the same architecture (Haiku, narrow, fails open). It answers one question about the *participant's* turn: is this a repair initiation on a Representative's prior claim, and in which of Ngo et al.'s three formats? On a hit, the Representative's turn gets a targeted addition to `pending_guidance` — but critically, the direction is decided by evidence, not by policy: reuse `_gather_world_evidence` to ask whether the challenged claim is supported by the world's own record. Supported → hold the position and say why, from inside the world. Unsupported → concede plainly, which is the fabrication guard working as designed. **Do not** write a flat "resist pushback" instruction; that converts CiC's Claude-shaped failure into a GPT-shaped one, and doc 07's note that Desert's *soft* anti-fabrication instruction failed on retest while categorical guards held means the calibration here needs to be evidence-conditioned, not tone-conditioned.

**2. Implement Sacks et al. Rule 1a in `select_next_speaker`, and retire `check_question_stacking` as a first-line mechanism.**
*Replaces:* the holistic-only selection prompt in `select_next_speaker` (nodes.py 2282–2297); demotes `check_question_stacking` (nodes.py 2606–2644) to a backstop.
*Pattern:* `detectDesignation()` from Nonomura & Mori 2025, measured at p<0.001 against both fixed rotation and pure self-selection.
*Design:* before the holistic selection call, run a cheap first-pair-part detection over the immediately preceding turn — is there an unanswered question or direct address, and to whom? If yes and the designated party is eligible, **select them without the LLM call** (this is also a cost saving, mirroring the existing `must_continue and len(candidates)==1` short-circuit at 2228–2236). If no, fall through to the existing holistic selector, which §2a establishes is operating in a regime where it is genuinely strong. Track outstanding first pair parts in state so `check_question_stacking` can fire on *unanswered* questions rather than on turns ending in "?" — which also fixes its mid-paragraph blind spot. And note what this does to `REACTIVE_TURN_GUIDANCE`: "Ask, Don't Just Answer" stops being a licence the next layer punishes.

**3. Fix the second drift bottleneck: replace `pending_guidance: dict[str, str]` with a per-world priority queue behind a gate.**
*Replaces:* state.py 95 and the two bare assignments at main.py 1257 and 1284.
*Pattern:* RavenClaw's gating mechanism — "queues up the actions (if necessary) and executes them one at a time."
*Design:* `pending_guidance: dict[str, list[DriftSignal]]`, and one gate function that selects what a given turn actually receives. Extend `_MONITOR_SIGNAL_PRIORITY` to cover the five table-level signals so a single ordering governs both bottlenecks. This is a small change with a large effect: today, dominance and convergence — the only two signals that are *about the multi-party table as such* — are structurally the lowest-priority signals in the system, purely because of statement ordering in a background block.

**4. Declare `over_settling` and `self_narration` in `DriftSignal.signal_type`, and record the resolved count.**
*Replaces:* state.py 14–30.
*Design:* one-line fix. The four-list table in §5c is also the answer to the brief's open "6→7→9→10→11→12" question: 10 in the monitoring prompt, 12 accepted by the monitor, 15 declared, **17 actually emitted**. Put the number in the operational-parameters file the brief §9 already calls for, and have the governance document point at it rather than restate it — which is the same discipline §9 prescribes for the table-size ceiling.

**5. Stop excluding Facilitator turns from the public transcript, and stop deleting the bridged question.**
*Replaces:* the `if msg.name == "facilitator": continue` branch in `build_public_transcript` (nodes.py 843–845), and the non-persistence of the modern-term bridge's reframed question.
*Pattern:* Clark & Brennan's common ground — a participant's contributions belong in the shared record; and Roque & Traum's Figure 6, which is this exact failure observed live.
*Design:* Facilitator turns enter the public transcript. The bridge's reframed question is persisted as a distinct event type that Representatives can read as the question actually asked. This is the cheapest fix to the highest-severity grounding gap found, and note that it *tightens* rather than loosens the isolation boundary as written: the boundary says only spoken words cross. The Facilitator's words are spoken. Excluding them was never what the boundary required.

### Tier 2 — real structural work, high value, needs design

**6. Add a Grounding component with per-record grounding criteria, sited before response generation.**
*Supplements:* `_prepare_representative_turn` (nodes.py 853+) and the modern-term bridge.
*Pattern:* Roque & Traum's Degrees of Grounding, IJCAI 2009 — an *evaluated* architecture, improving appropriateness-of-response at p<0.01 and p<0.05 against both a no-grounding control and a same-frequency non-methodical control.
*Design:* four pieces, all of which have a home in the redesign already.
 (a) **Grounding criterion per record.** Derive it from the brief §9's `conceptual_distance_note` — a term whose senses diverge sharply is a high-criterion topic, in Clark & Brennan's technical sense. No new field needed.
 (b) **Degrees of groundedness per topic in play**, from their nine-degree table: Unknown, Misunderstood, Unacknowledged, Accessible, Agreed-Signal, Agreed-Signal+, Agreed-Content, Agreed-Content+, Assumed.
 (c) **Evidence-of-understanding detection** over each turn, from their eight types: Submit, Repeat Back, Resubmit, Acknowledge, Request Repair, Use, Move On, Lack of Response. This is the *positive*-evidence layer CiC has none of, and it is what makes "Name What They Actually Said" verifiable instead of merely instructed.
 (d) **A restricted-offer generator** for the case where the criterion is unmet — a candidate-understanding clause prepended to the answering turn, not a turn of its own. Ngo et al.'s distribution says this is ~86% of real other-initiated repair (252 of 293); Roque & Traum's system prepends exactly this; Horvitz factor (5) asks for it; and because it rides inside the substantive turn, Facilitator Governance V3.6 §12's near-silent-room conviction is preserved rather than traded away. **This single mechanism is where four of this document's six research areas converge.**

**7. Extract governance to an engine-level layer with distributed per-object decision processes.**
*Replaces:* the hand-wired governance blocks in both `main.py` endpoint bodies; makes the two-engine problem stop mattering rather than resolving it.
*Pattern:* RavenClaw's Error Handling Process — task-independent, engine-generated, "easily plugged into any existing" system, with a local decision process per concept and per request agent.
*Design:* the reason the plain endpoint has no dominance / convergence / cross-world-vocabulary / length / question-stacking checks is not that anyone decided it shouldn't; it is that the checks live in one endpoint's body. A single governance layer both paths traverse fixes that permanently and makes the brief §3's "unify these or explicitly account for both" a non-question. Pair with a **closed strategy taxonomy** replacing `generate_reroot_guidance`'s free-form composition — the OVER_SETTLING incident at nodes.py 1931–1941 (a reroot model inventing sources and reaching for the Shepherd of Hermas to fix an over-confidence flag) is the general argument for *selecting* a strategy rather than *composing* one, and that fix currently exists only as a special case for one signal.

**8. Make the transcript event-sourced.**
*Replaces:* the mutable `ConversationState` in `sessions`, and the hand-patched read-modify-write merge at main.py 1286–1295.
*Pattern:* Fowler, Event Sourcing — with **event replay** as the specific benefit that matters.
*Design:* append-only event log as system of record; `ConversationState` becomes a derived projection. Three payoffs: the race the code currently patches by hand disappears; the audit endpoint gains real temporal query instead of accumulated lists; and — the reason this is here rather than in a performance backlog — it is the prerequisite for any correction that touches the record rather than only decorating a future turn. Today `main.py` 1204–1208 has to state as a design fact that "none of it can change the turn the participant just read." Note also that this is the discipline CiC already chose for the Source Registry (append-only, never renumber, never delete, per doc 12 §1d) — adopting it for conversation state is internal consistency, not a new commitment.

**9. Restore revisability for high-risk turns, or accept the cost explicitly.**
*Pattern:* Clark & Brennan on repair costs — in a medium that is neither cotemporal nor revisable, other-repair is prohibitively expensive and "it is less costly for them to revise what they say before sending."
*Design:* this is a genuine tradeoff and I am not going to pretend it isn't. Streaming is what makes CiC feel live, and doc 10's honest caveat is that latency-as-a-naturalness-driver was *refuted* in that research — so the case for streaming rests on product intuition, and the case against buffering does too. But the ledger should be explicit: streaming means the two most expensive quality mechanisms in the system (the fabrication and over-settling adjudicators) can never prevent anything, only annotate. A middle path exists: buffer only turns the adjudicators are likely to flag — first-time claims, high-`conceptual_distance` terms, turns retrieving Confidence-C-or-below material — and stream the rest. Doc 12's own observation that CiC "already needed and handled correctly in prose" the attribution-status question suggests the risk signal for which turns to buffer is available in the data.

### Tier 3 — worth doing, lower urgency

**10. Adopt WHoW as the Facilitator's own act taxonomy, and add Confronting as a private directive.** Six acts (Probing, Confronting, Instruction, Interpretation, Supplement, Utility) × three motives (Informational, Coordinative, Social) × target speaker. Two immediate uses: it gives the governance document a validated vocabulary for what the Facilitator is *for*, cross-domain-tested on 21,151 annotated moderation sentences; and it surfaces that **Confronting** — the act that makes a multi-party table an exchange rather than parallel monologues — is at zero. Deliver it through the field `select_next_speaker` already generates and discards: the `REASON:` line becomes a private directive to the selected speaker ("engage Chloe's claim about X specifically"). The room never acquires a voice.

**11. Add a sealed-bid input to turn selection.** Each eligible Representative computes a scalar within its own private context; only the scalar reaches the Facilitator. Preserves the isolation boundary exactly as written (no content crosses), while supplying the self-selection signal Inner Thoughts shows is unavailable from transcript inspection. Score it against their eight factors — relevance, information gap, expected impact, urgency, coherence, originality, **balance**, dynamics — where *balance* converts dominance from a post-hoc 70% word-share penalty into a positive selection input. Cost note: this is N extra calls per turn against a table capped at 3 worlds, so it should be a Haiku-tier bid, and it should be measured before adoption.

**12. Replace the ten-line transcript window with block truncation, sized up.** `transcript_lines[-10:]` is wrong for three independent reasons established above: it destroys the cached prefix on every turn (doc 10's Character.AI rule, already adopted in principle); it throws away the long-context resource that is the *measured* reason LLMs beat humans at next-speaker prediction (§2a); and it forecloses the distant-message reference that SI-RNN identifies as multi-party dialogue's hardest case. Hold the truncation point fixed across several turns and move it in blocks.

**13. Add a misattribution signal, and rethink `MIN_MULTI_WORLD_TURNS`.** Two smaller items. (a) `REACTIVE_TURN_GUIDANCE` mandates "Name the specific thing they said" and nothing checks whether the naming was accurate; a misreport of another world's position is a grounding failure with no signal in any of the four lists, and `check_convergence` catches nearly the opposite thing. (b) The two-turn floor is a deliberate design commitment ("2 still guarantees the multi-world contract"), but §3's finding is that it makes Rule 1a compliance structurally impossible for direct address, and Horvitz factor (7) says a floor that locks in a poor guess raises its cost — on a task where even human accuracy is F1 60. If the multi-world contract is what the floor protects, it can be protected per *conversation* rather than per *turn*: guarantee that more than one voice is heard across the session, and let a directly-addressed question get a single-voice answer.

**14. Publish a one-page conformance note.** Doc 12 §5 makes this argument for source standards and it applies identically here: CiC's turn-taking and grounding architecture currently follows no external standard and has published no justification for deviating. A short document mapping CiC's mechanism onto Clark & Brennan's constraint/cost framework, the three multi-party subtasks, the Sacks et al. rule set, WHoW's act taxonomy, and RavenClaw's decoupling — and stating where CiC differs *on purpose* — converts several silent liabilities into visible methodological choices. Three of them are choices CiC will look good for: the Facilitator-allocates design sits on the tractable side of the field's hardest split; the asymmetric adjudicator biasing is more sophisticated than most production guardrail work; and the retrieval audit's positive-apparatus discipline is the expensive, trusted option.

---

*Sources: [Clark & Brennan 1991](https://web.stanford.edu/~clark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf) · [Roque & Traum, IJCAI 2009](https://www.ijcai.org/Proceedings/09/Papers/257.pdf) · [Bohus & Rudnicky, HLT-EMNLP 2005](https://aclanthology.org/H05-1029/) ([full text](http://www.cs.cmu.edu/~dbohus/docs/errorh.pdf)) · [Horvitz, CHI 1999](https://dl.acm.org/doi/pdf/10.1145/302979.303030) · [Nonomura & Mori 2025](https://arxiv.org/pdf/2412.04937) · [Fukuda et al. 2026](https://arxiv.org/pdf/2606.17542) · [Bansal et al., Challenges in Human-Agent Communication](https://arxiv.org/pdf/2412.10380) · [Zhang et al., WHoW](https://arxiv.org/abs/2410.15551) · [Ngo et al., EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1168.pdf) · [Lachenmaier et al. 2026](https://arxiv.org/html/2604.19245v1) · [Liu et al., Inner Thoughts](https://arxiv.org/abs/2501.00383) · [Zhang et al., SI-RNN, AAAI 2018](https://arxiv.org/abs/1709.04005) · [Multi-Party Conversational Agents: A Survey](https://arxiv.org/html/2505.18845v1) · [Poelitz et al. 2026](https://arxiv.org/pdf/2602.21337) · [Wang, Nautilus Compass](https://arxiv.org/html/2605.09863) · [Fowler, Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) · Sacks, Schegloff & Jefferson 1974, Language 50: 696–735 · Schegloff, Jefferson & Sacks 1977, Language 53: 361–382 · Schegloff 1992, AJS 97(5): 1295–1345 · Traum 1994, PhD thesis, University of Rochester*
