# What makes AI conversation feel real — and what it means for CiC

*Deep research report, 2026-07-24. Run on Fable. 105 agents, 5 search angles, 23 sources fetched, 115 claims extracted, 25 put through 3-vote adversarial verification — 22 confirmed, 3 refuted and dropped, 0 unverified.*

*Copied here 2026-07-25 from this session's original scratchpad location so it lives alongside the rest of the redesign research, in one durable place within the project.*

## Executive summary

The strongest convergent result across 2024–2026 research is that the **"assistant register"** — long, over-polite, over-explaining, agreement-prone replies — is the primary tell that breaks perceived conversational realness. This directly validates the response-length-cap review already underway as the highest-leverage naturalness change on the table.

Human-likeness is now a measurable, optimizable target, but it **collapses over long dialogues** (GPT-4: 51.9% pass at 3 turns → 13.3% at ~110 turns), through three concrete, instrumentable failure modes: declining initiative, drift into agreement/sycophancy, and verbosity drift. The deepest persona failure found: models *state* their assigned character but fail to *enact* it — especially by refusing to sustain disagreement.

Techniques that transfer to CiC's actual architecture (Sonnet 5 + RAG, prompt-only, no fine-tuning): Chain-of-Persona self-questioning, Character.AI's cache-aware truncation playbook (which maps directly onto CiC's already-confirmed-working caching), and full-history-in-context over compressed memory for within-session recall. The counterintuitive memory finding: selective, emotionally-weighted forgetting beats retain-everything RAG — but only matters for a *future* cross-session memory build, not today's within-session design. The open frontier — flagged by Replika's founder as the single missing capability in the whole industry — is **proactive memory surfacing**, which CiC can get almost for free within a session, since full history already sits in the cached context.

Replika's hardest product lesson adds a real governance warning directly relevant to yesterday's `PRIMARY_TURN_GUIDANCE` change: **personality continuity trumps objective model quality** — voice-altering prompt changes need continuity regression-testing before they reach returning participants.

---

## What makes conversation feel real

**1. The "assistant register" is the most-documented killer of naturalness.** *(High confidence — 3 independent primary sources agree.)*
Response-length restraint is the single highest-weighted trait predicting human-likeness in one recent alignment study (nearly double the next-highest trait). Growing verbosity is a measurable drift signal as conversations lengthen. Replika's founder independently reports that instruction-tuned models converge toward overly polite, over-explaining patterns unless a product deliberately counters it.
*For CiC:* proceeds with the length-cap work already in motion — but the underlying principle is per-turn restraint with content **paced across turns**, not shallowness. The source data behind this finding is short, texting-style exchanges, so this needs care in CiC's substantive, sourced dialogue.

**2. Human-likeness can now be measured and directly optimized.** *(Medium confidence — one un-replicated 2026 preprint, real code and weights.)*
A 16-trait model derived from contrastive human-vs-AI dialogue was compressed into a training signal; the aligned model was judged human-like far more often in blind evaluation (61.78% vs. 34.29% for a comparison model). CiC can't fine-tune Sonnet 5, but the 16-trait checklist is directly usable as a rubric for sharpening `PRIMARY_TURN_GUIDANCE` and as an evaluation checklist in the Representative validation suite — with some traits (informal grammar, typos) consciously excluded as incompatible with CiC's brand and historical fidelity.

**3. Realness collapses over long conversations, through three specific, measurable failure modes.** *(High confidence — peer-reviewed, ACL 2025.)*
Human-judged pass rates for "is this human" fall sharply as dialogue length grows (GPT-4: 51.9% → 38.9% → 13.3%; Claude-3-Sonnet: 51.8% → 32.1% → 7.1%, across roughly 3/10/100+ turns). The paper names exactly what degrades: declining initiative, defaulting to agreement instead of driving discussion, and word-count/style drift.
*For CiC (new idea):* instrument drift telemetry — average response length, initiative rate, agreement rate — across a session's turns. The existing safety-classifier pipeline is a natural home for a drift detector; these are exactly the signals that degrade before a conversation starts feeling canned. (Note: these numbers are 2024-era models — Sonnet 5 almost certainly does better in absolute terms, but the *direction* of decline is well-attested.)

**4. The deepest persona failure: models state a character but don't enact it — especially by refusing to disagree.** *(High confidence — three independent studies converge.)*
LLM agents rarely sustain real disagreement even when explicitly assigned maximally opposed preferences. Agents that look socially coherent overall still fail more demanding checks of actually behaving like their assigned persona. Agreement-drift is the specific mechanism undermining persona realism.
*For CiC, this is the standout finding:* a Representative that stops pushing back theologically stops feeling real **and** stops being faithful to its own world — the naturalness fix and CiC's own fidelity conviction are the same fix. Concretely: `PRIMARY_TURN_GUIDANCE` should explicitly license sustained, respectful disagreement, and the validation suite should include probes that pressure a Representative toward agreement across many turns and confirm it holds its world's actual position.

---

## Techniques that transfer to CiC's architecture

**Chain-of-Persona self-questioning** *(High confidence, peer-reviewed.)* A prompt-only technique — 5 rounds of persona-aware self-questioning before the model responds — measurably improved role consistency and conversational quality on a black-box model, no fine-tuning required. Costs tokens and latency, though, which is in direct tension with yesterday's decision to defer non-blocking safety checks for speed. Worth piloting as a *compressed* version (1–2 questions, not 5) at high-risk moments specifically — topic shifts, modern-term bridges — rather than every turn.

**Full history in context beats memory-compression, at CiC's session lengths.** *(Medium confidence, one strong preprint.)* Long-context models with the full conversation in the prompt substantially outperform fact-extraction memory systems on recall accuracy, and with prompt caching's ~90% discount, full-context is actually *cheaper* for shorter sessions — memory-compression only wins after roughly 10+ turns of accumulated history. **CiC is already doing this correctly.** One thing worth watching: Anthropic's cache TTL is 5 minutes by default — if participants pause mid-session for longer than that (real, contemplative pacing), the cache advantage erodes and becomes a real cost variable.

**Character.AI's production playbook — the most detailed public account from a leading companion product.** *(High confidence, two first-party engineering posts.)* Character.AI reports a ~95% prompt-cache hit rate, achieved substantially by holding the truncation point in the conversation history fixed for several turns rather than re-truncating every turn — so the cached prefix from the previous turn survives.
*For CiC (preventive, not urgent):* caching works today, confirmed. But the moment response length or session length changes force any kind of history truncation, a naive sliding window would silently destroy the caching win just confirmed. Adopt the rule now, before it's needed: stable prefix, move the truncation point in blocks.

**Proactive memory surfacing is the industry's hardest unsolved problem — and CiC can get it almost for free.** *(Medium confidence — one strong practitioner account, corroborated by academic literature.)* Replika's founder names this as the single missing capability for real-feeling companion AI: retrieval only answers what's asked, it never spontaneously surfaces a relevant memory at the right moment. Academic work treats this as a genuinely open problem for cross-session memory. But *within* a CiC session, the full history is already sitting in the cached context — surfacing a callback ("you asked earlier about suffering — what we're saying now touches that") needs zero new infrastructure, just prompt guidance. This also directly serves comprehension: callbacks are how a human teacher builds understanding across a conversation.

**Selective, emotionally-weighted forgetting beats retain-everything memory — but only for a future cross-session build.** *(High confidence, peer-reviewed.)* One system that keeps under 10% of a conversation, weighted by emotional salience, significantly increased user satisfaction and *improved* retrieval precision over naive retain-everything RAG. CiC doesn't need this today (full history is already in context within a session) — but if cross-session Representative memory is ever built, the evidence says prioritizing emotionally salient participant moments over transcript completeness is what actually works.

---

## Product governance lesson: personality is versioned

*(High confidence, first-person founder account, independently corroborated as a recurring pattern into 2026.)*

Replika's own upgrades to a better underlying language model *damaged* the user experience — users rejected the improved model because their relationship was with the specific personality, not with "a better AI." The company had to build multi-week gradual transitions and a permanent legacy-model option. The exact same pattern recurred independently in a 2026 model rollout: community backlash, "keep the legacy model" petitions, a shipped legacy toggle.

*For CiC:* treat each Representative's voice as a versioned artifact. Yesterday's `PRIMARY_TURN_GUIDANCE` change alters personality, not just formatting. Before it — and any future prompt change — reaches returning participants, run continuity regression tests: same probes, old prompt vs. new prompt, diff the actual voice. This matters more every week the pilot builds a base of people who've talked to a Representative more than once.

---

## What CiC should try next, in priority order

*(This is the research's own direct synthesis — what's already right, versus what's genuinely new.)*

**Already aligned with the evidence, no change needed:**
- End-to-end prompt caching (matches Character.AI's own economics)
- Full-history-in-context rather than compressed memory
- The length-cap review already underway
- `PRIMARY_TURN_GUIDANCE` as the vehicle for turn-level conversational quality

**New, evidence-backed next steps:**
1. Finalize length caps with content deliberately paced *across* turns, not just shortened
2. Explicitly license and validation-probe **sustained, respectful disagreement** — fixes the best-documented persona failure and serves CiC's own fidelity conviction at the same time
3. Prompt for within-session proactive callbacks — a free win given the current architecture
4. Add drift telemetry (length, initiative, agreement rate across turns) to the classifier pipeline
5. Adopt a cache-aware block-truncation policy *before* any history-window change is made
6. Version Representative voice with continuity regression tests before prompt changes reach returning participants
7. Pilot a compressed (1–2 question) hidden Chain-of-Persona self-check at specifically high-risk moments, latency budget permitting
8. Adopt "refuses to fabricate about undisclosed facts" as a formal validation metric
9. Reserve emotionally-weighted selective memory for a future cross-session memory build — not needed today

**One important reframe:** almost all of this "human-likeness" evidence measures *passing as human* — which is not CiC's goal (a Representative voices a world and never blurs what it actually is). Read every finding above as evidence about conversational naturalness and presence, not deception. The underlying levers — brevity, initiative, sustained disagreement, callbacks, continuity — transfer directly. The Turing-test framing itself does not.

---

## Honest caveat: what did *not* survive verification

Three claims were checked and refuted — worth knowing specifically because one of them cuts against yesterday's own work:

- A claimed breakdown of what judges say tips them off to AI (naturalness, brevity, em-dashes, over-politeness) — refuted, unsupported by its own source on close check.
- A claim that conversational *consistency* overtakes per-turn quality as conversations get longer — refuted.
- **A claim that delayed response timing is a directly detected, measurable driver of perceived unnaturalness in conversation — refuted (0-3 vote).** This means **no verified evidence in this research supports response latency as a first-order naturalness driver.** Yesterday's decision to defer non-blocking safety checks for latency currently rests on product intuition, not on anything confirmed here — worth knowing plainly, not as a reason to reverse it, but so it isn't oversold as evidence-backed when it isn't.

## Domain-transfer caveat

The human-likeness evidence above comes from casual texting-style test games, TV-drama roleplay benchmarks, and companion-chat products — none of it tested long-form, sourced, formation-oriented dialogue like CiC's specifically. The *direction* of every finding likely transfers; the exact *magnitude* is genuinely unproven for CiC's domain. Model era matters too: the long-conversation collapse numbers are from 2024-era models — Sonnet 5 almost certainly does better in absolute terms, though the directional decline is well-attested across multiple studies.

## Open questions this research surfaced but couldn't answer

- Does brevity's naturalness advantage survive in *substantive, educational* dialogue, or is there a real depth-vs-brevity tradeoff CiC has to resolve by pacing content across turns? No study tested this directly — it's the single most decision-relevant gap for the length-cap work.
- What's the real latency-perception relationship for *text* conversation specifically? The one quantitative source on this was refuted, leaving the question genuinely open in either direction.
- Can proactive memory surfacing actually be reliably prompt-engineered, and does it measurably help engagement and comprehension? Well-documented as a gap, but nothing measured the *effect* — CiC could generate this evidence itself, cheaply.
- Which of the 16 human-likeness traits survive CiC's own non-negotiables (anti-fabrication, Representative-voices-the-world, no personalizing)? Nobody has mapped which naturalness levers remain once historical fidelity and transparency-about-being-AI are treated as hard constraints.

## Sources (primary/high-quality, cited above)

- [HAL: Inducing Human-likeness in LLMs with Alignment](https://arxiv.org/html/2601.02813v3) — arXiv 2026 preprint
- [X-Turing: long-conversation naturalness collapse](https://arxiv.org/html/2408.09853) — ACL 2025
- [Persona-Aware Contrastive Learning / Chain of Persona](https://aclanthology.org/2025.findings-acl.1344.pdf) — ACL Findings 2025
- [Agreement-drift / persona-enactment failure](https://arxiv.org/pdf/2509.03736)
- [LUFY — psychologically-grounded selective memory](https://arxiv.org/pdf/2409.12524) — Dialogue & Discourse 2025
- [Long-context vs. memory-extraction cost/accuracy analysis](https://arxiv.org/html/2603.04814v1)
- [Prompt Design at Character.AI](https://blog.character.ai/prompt-design-at-character-ai/) — first-party engineering
- [Optimizing AI Inference at Character.AI](https://blog.character.ai/optimizing-ai-inference-at-character-ai/) — first-party engineering
- [Replika founder interview — personality continuity, proactive memory](https://www.cognitiverevolution.ai/ai-friends-real-relationships-with-eugenia-kuyda-replikas-founder-ceo/)
- [Anthropic prompt-caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Anthropic latency-reduction guardrails documentation](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)
