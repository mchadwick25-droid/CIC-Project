# Church in Conversation: End-to-End System Redesign Brief

**Phase 1 of 2 — this brief is the design ask only.** Phase 1 (this thread) produces the design and holds the full complexity of how every piece interrelates — nothing more. Mark reviews and refines that design before anything else happens. Phase 2 is a separate, later Fable thread, built from the reviewed design, that produces the step-by-step build blueprint. The actual building then happens afterward, incrementally, in Sonnet, one step at a time. See §9.

**Required reading before starting:** the full research behind this brief lives in `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/` — ten documents plus an index (`00_INDEX.md`). Read all of them before beginning the design. Every claim in this brief traces back to specific evidence in that folder; this document only summarizes and organizes it.

**Governing document, resolved 2026-07-25:** two Vision documents exist with different framings of the rigor floor — `L1-Foundation/CiC_L1_Vision_V2_0.docx` ("scholarly rigor... this methodology **requires** of every world build") versus `Ministry/Communication/.../V1.1.docx` ("scholarly rigor... **demonstrated in the two existing world builds**"). V2.0 governs this redesign. V1.1 explicitly scoped itself, in its own text, to authorizing one earlier revision cycle ("the v7 revision") — it was never meant to permanently replace the founding document's language, and its narrower, achievement-anchored framing would work against the point of this redesign, which is closing the gap between what the methodology requires and what's unevenly been demonstrated so far. Treat V2.0's language as the standard throughout.

This is a live draft Mark is actively marking up — treat every section as a proposal, not a locked spec, unless told otherwise.

**None of what follows is a locked specification.** The only true bedrock is the mission, the Five Convictions, and a genuinely safe space for a participant to explore faith and the story of Jesus — without pressure, without distortion, without harm. Everything else in this brief — the seven jobs in §5, the external patterns in §6, the dataset-not-prose shape in §8, even the six items in §3 — is a well-evidenced starting hypothesis from the research, not a requirement. If a genuinely better way to accomplish the same underlying outcomes exists, take it, even if the result looks nothing like what's suggested here.

---

## 1. Mission — read this first, it governs everything below

Church in Conversation exists to help people experience Jesus in new ways through engagement with the living traditions and practices of His Church throughout history and today. Everything below serves that mission through one instrument: a genuinely engaging, natural, and rigorous conversation between a modern participant and Representatives who voice historical Christian worlds — never an invented individual, always the world's own collective "we."

## 2. What this redesign is for

This is not a data-modeling exercise for its own sake. The test of every decision below is: does this make the conversation more engaging, more natural, and more faithful, for a real participant, at the table, right now. A data structure that's elegant but doesn't serve a better conversation is wrong. A shortcut that serves a better conversation but breaks rigor is also wrong. Holding both at once is the actual design problem — conversation dynamics are the ground this whole redesign stands on, not an afterthought once the data model is settled.

A third thing grounds this equally, not as a secondary constraint: **real API/runtime cost has to come down, not just stay acceptable.** This isn't in tension with the two goals above — in at least one place the research found, it's the same fix. Retrieval volume has never once been tuned or measured, and a share of what gets injected into every turn is exactly the scholarly-register material already shown to be leaking into voice as an unwanted "documentation" tone. Organizing that correctly is very plausibly a quality win and a cost win at the same time, not a tradeoff between them. Treat every proposal in this brief through that same lens: where quality and cost pull in the same direction, take it; where they'd genuinely conflict, rigor governs, but don't assume a conflict exists before checking.

**This brief covers the build process, representative-construction methodology, facilitator governance, and table/multi-world dynamics together, as one system — deliberately, not because it's convenient.** The research found the real failures live at the seams between these, not inside any one of them: a lens synthesis explicitly deleted for being "representative-construction work, out of scope for this document"; real relational insight that reaches Doc_04 and never reaches Doc_08, the Permanent Prompt, or the Facilitator's own table-selection logic. Redesigning the data layer without redesigning how representative construction, facilitator governance, and the table consume it would risk producing the exact same disconnection this research diagnosed, one level up. The design should be unified even if the rollout is phased — see §9.

## 3. What NOT to rebuild — this is a redesign, not a restart

None of the items below are mechanisms frozen in place. Fable should feel free to redesign any of them, including moving where in the process they're handled entirely, if a better mechanism serves the same end. What's actually fixed is the **purpose and the outcome** underneath each one — the current mechanism is just today's best attempt at it, not a boundary. Several of these may genuinely be better managed elsewhere in the pipeline than where they live today; that's an improvement, not a violation of scope.

**Purpose (non-negotiable) → current mechanism (open to redesign):**

- **A Representative always voices the world's own collective life, never an invented individual** — independently validated by outside industry practice, not just an internal preference (see research doc 09). Current mechanism: pronoun discipline written into the prompt, checked by adversarial testing.
- **No claim may be spoken without being traceable to an actual source, with honest confidence attached** — this is the outcome, not the specific registry format. Current mechanism: Doc_02's Source Registry checkpoint. This whole redesign is partly about generalizing this pattern; the pattern itself, or something that achieves the same guarantee better, should carry forward.
- **A participant in real crisis, or drifting toward an unhealthy dependency on a Representative, is met deliberately — never left to whatever a Representative happens to improvise.** Current mechanism: a classify-then-route safety pipeline, live-tested to 19/20 clean. The track record is what's worth protecting; the specific pipeline shape isn't sacred if something else holds the same guarantee.
- **Full-model cost is never spent on a decision a cheaper, reliable check could make.** Current mechanism: a hard split between the generation model and a cheaper model for every classifier. Directly relevant to the cost requirement above — this is the one place cost discipline already exists; extend the principle, don't lose it.
- **A real fabrication must never be missed, and a real conviction must never be second-guessed into false hesitation** — two different mistakes, two different acceptable error directions. Current mechanism: two adjudicators, deliberately biased in opposite directions.
- **A modern participant unfamiliar with period vocabulary should never be lost by it.** Current mechanism: a confirmed-gloss whitelist — and unlike the others above, this one's actual execution needs real rework, found broken the same night this research was compiled. Keep the goal; the mechanism is fair game to replace outright.

## 4. The diagnosis — four converging findings, found independently

Three research passes plus live bug-hunting on the night this was compiled arrived at the same underlying cause from four different directions (full evidence in research docs 04, 05, 06, 07, 08):

**a. Build process.** Quality does not improve with build order — the last world built has the worst defect rate of any world (40% of documents needing 3+ review rounds, the only world where zero cleared in one round). The failures cluster in document types that require a prose narrative to stay in sync with a separate structured artifact by hand — a lexicon narrative and its companion chunk files, a forces document and its companion index. Every failure in these types takes the same shape: the fix landed where a reviewer looked, not in the other places the same fact also lives.

**b. Representative construction.** Voice failures are overwhelmingly organization failures, not evidence failures. A story was told with the right content and the wrong occasion, in the same transcript that got it right elsewhere. A fully-built, indexed martyrdom account never reached a Representative because the prompt's own grief list pointed at six different, unnarratable names instead. The material existed. It wasn't reachable at the moment of speaking.

**c. Runtime retrieval.** Generation output length has been tuned with real rigor — measured, revised, re-measured. Retrieval input has never been tuned once since the original scaffold. Concretely: three of six worlds have every lexicon chunk marked Tier 1, so retrieval conditions are never evaluated at all; some conditions are a literal em-dash; the one field built for safe, lightweight surfacing (Quick Meaning) is silently dropped by the parser while heavy scholarly-register content is injected raw into every turn — a live, per-turn source of exactly the "documentation voice" register leaks found across every world's own testing. This is also a real cost lever sitting unexamined: Alexandria alone can push roughly 4,300 words of retrieved context into a single turn against a ~900-word output cap — tokens being paid for that are actively working against voice quality, not for it.

**d. Cross-cutting.** Real, good relational insight already exists and never reaches the Representative. Doc_04's own vocabulary for a force reshaping and being reshaped by the world ("reshaping") self-organized independently across all six worlds before any template asked for it — and appears in zero deployed prompts. The lexicon's "Ecological Function" section genuinely reveals culture, not just definition, about 68% of the time it's used — and is read by nothing downstream. Compare "Related-Terms," the same class of relational information, which was structured and indexed, and became the backbone of a real analytical finding. The difference was never quality. It was whether anything downstream could query it.

## 5. The seven jobs every piece of information must serve

Organize the schema around these explicitly. A field may serve more than one job at once — that's fine. The failure mode is a job with *no* field responsible for it, left to memory, the way "which sources a Representative may draw from" was an unwritten convention until a Representative reached for the wrong world's source and broke it.

- **Rigor/grounding** — is this claim true, how sure are we, per the confidence vocabulary.
- **Repository/reference** — browsable and queryable on its own, for a human to look something up without a conversation happening.
- **Representative voice-construction** — what a Representative may actually draw from, and how, when speaking. Distinct from rigor: a source can be well-attested and still be the wrong one for this Representative to reach for.
- **Runtime retrieval** — findable at the right moment in a live conversation. A timing job, not a truth job.
- **Cross-reference/consistency** — how this relates to other terms, other worlds, other gravities, so a fix in one place doesn't leave three related places stale.
- **Participant-facing translation** — making the same underlying content legible to someone with no background, without touching the underlying claim.
- **Anachronism boundary** — whether this belongs to this world's own era at all.

## 6. Adopt, don't reinvent — what already exists in the wild

Full evidence and verdicts in research doc 09.

- **Keyword/embedding-triggered, budgeted, priority-ranked knowledge entries.** Every AI persona-building tool that solves "give a voice the right fact at the right moment" converges on the same pattern, and every implementation calls it *World* Info, not persona info — trigger keys, a token budget, priority scoring when things compete for space, entries that can require two keys at once, entries that are always-on. This directly targets the retrieval-specificity gap found in §4c.
- **Explicit permanence/eviction ranking on every field.** The most reused persona-building spec in the industry splits fields into "always present" versus "prune first under token pressure," and production systems tag every assembled prompt piece with an explicit priority for exactly this. CiC has no equivalent today.
- **Situation-conditioned trait intensity, not a fixed character.** The most transferable structure found: model voice as named traits whose intensity varies by situation (the same tradition speaks differently about death than about food), scored against a fixed rubric — rather than trying to fully specify a voice through description alone.
- **The SPEAKING model** (Setting, Participants, Ends, Act sequence, Key, Instrumentalities, Norms, Genre) — the one framework surveyed whose theoretical foundation already assumes a *speech community*, not an individual speaker. Worth using directly as an organizing lens for how a world's own "voice" gets specified.
- **Demonstration dialogue as a small, curated, rubric-scored calibration set** — not a bottomless well. The industry's own guidance lands around 3–5 examples, diverse, judged against a fixed trait rubric. More example text is not simply better; the rubric comes first and dialogue is judged against it.
- **Negative constraints work best as an author/reviewer-facing rubric**, not as a direct instruction fed to the model — no framework surveyed has a working "things this voice would never say" field that functions well as model input.

## 7. The concrete objectives this redesign must hit

1. **Build process.** One dataset-first, source-collection-and-rating discipline for primary sources, generalizing Doc_02's Source Registry pattern to every document type that currently fans out (lexicon, forces, gravity discovery) — the highest standard for collecting, organizing, and rating what's primary to the world.
2. **Three-level participant access.** The live conversation itself; an on-request plain explanation at a genuine, checkable reading-level floor; the full scholarly apparatus underneath — all three drawn from one dataset, not three separately-maintained representations that can drift apart.
3. **Full scholarly coverage.** Lexicon, stories, quotes, general referencing — everything a genuine scholarly library of primary and secondary sources would make available — organized from the start to do double duty: a real, browsable repository, *and* the material a Representative can actually speak from naturally, at the table, with other Representatives, not just with the participant.
4. **Representative-construction methodology, redesigned alongside the data it draws from, not left as-is on top of a new schema.** How a Permanent Prompt actually gets assembled from the dataset — what's always-present versus retrieved on demand, how voice examples are selected and how many, how the lens/synthesis work (§4d) actually reaches this step instead of being cut before it. Informed directly by §6's external patterns.
5. **Facilitator governance, redesigned as its own methodology — not just "whatever data the Representatives have, plus a translation layer."** This covers the Facilitator's actual jobs: bridging between a world and a modern participant, translating without flattening, holding safety and rigor, and — for a multi-world table — deciding who speaks next and why. Two live bugs found the same night this research was compiled are direct evidence this needs real design attention, not incremental patching: an anachronism-bridge intercept that silently ended a multi-world round after one speaker regardless of how many worlds were seated, and a term-matching gap that let a universal question misfire as a narrow modern doctrine. Table dynamics — turn selection, cross-world vocabulary distinctness, forces/gravities actually informing how worlds engage each other, not just what each says alone — are part of this, not a separate concern.
6. **Real API/runtime cost, lower than today's, not just "acceptable."** Every part of the design should be checked against this directly — what gets retrieved, how much, in what form, for every turn. Where a fix already found serves both quality and cost at once (§4c), take it as one decision, not two competing ones.

## 8. The shape of the output

Not prose as the source of truth. One structured record per addressable unit — a term, a story, a force, a source, a gravity — each carrying both its structured fields (confidence, tier, retrieval triggers, related-terms, which of the seven jobs it serves) *and* its own prose content as a field inside that same record, not a separately-maintained companion document. Deployment artifacts — Permanent Prompts, lexicon chunks, indexes — are generated views over this dataset, not independently hand-authored documents kept in sync by memory. Nothing is quality-reduced by this. The depth stays, and should grow, because it finally becomes reachable instead of stranded.

## 9. Two phases — this brief is Phase 1 only

Neither phase asks Fable to write final schema files, rewrite the actual templates, migrate real world data, or produce ready-to-ship artifacts. Phase 1 thinks through the whole system's complexity at once — something no single build-process pass, representative-construction pass, or facilitator-governance pass has ever done together. Phase 2, later, turns the result into something buildable.

### Phase 1 (this thread) — the design

Needs to hold the full complexity and interdependency of the system, not treat any piece in isolation:

1. A concrete schema/field specification per record type, explicitly mapped to the seven jobs in §5.
2. A build-process methodology — template plus verification gate — for each document type currently prone to fan-out drift (§4a).
3. A representative-construction methodology — how a Permanent Prompt is actually assembled from the new dataset, replacing today's largely-hand-authored process.
4. A facilitator-governance design — safety/translation/rigor-bridging logic and table/multi-world turn-selection dynamics, built to actually read the new dataset's relational and cross-reference fields rather than working around them.
5. An explicit accounting of what from §3 is being preserved as-is, versus where a listed purpose is now being served by a different, better mechanism — and why.
6. A real, honest cost comparison against today's system — where the redesign is expected to cost less, and by roughly how much, not just an assertion that it will.
7. **A pressure test, not just architecture on paper.** Before calling the design done, run it against 2-3 concrete, realistic multi-world conversation scenarios — including at least one scenario like the "what is faith" case in research doc 08, where a bare universal question meets a seated table of several worlds — and show explicitly how the new design would have produced a better result than today's system did. A schema that hasn't been checked against a real scenario risks looking elegant and still being wrong.

**Stop here.** Mark reviews and refines this design directly before Phase 2 begins — do not proceed to a build sequence in this same pass.

### Phase 2 (a separate, later Fable thread) — the blueprint

Starts from the reviewed, finalized Phase 1 design, not from this brief directly. Produces an ordered, step-by-step build plan a Sonnet-driven process can actually execute — one focused step at a time, potentially across many separate sessions over time, the same way every other piece of work in this project has been built. Each step needs to specify:

- **What it builds**, scoped to what one focused session can complete and verify in a single sitting.
- **What it depends on** from earlier steps, and what it unlocks for later ones — so the sequence itself is legible, not just a flat task list.
- **How to verify it actually integrated correctly** before moving on — a real checkpoint, in the spirit of Doc_02's own Source Registry gate (§3), not a self-report. This is the part that matters most: building incrementally, session by session, is exactly the process shape that produced the original fan-out/drift problem this whole brief exists to fix. The blueprint has to guard against reproducing that failure one level up, not just describe a good end state and trust the path there to hold together.

**Open: anything specific to name here about scope, timeline, or what "done" looks like for either phase — add before sending.**

---

*Compiled from tonight's full research arc — see `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/00_INDEX.md` for the complete source list.*
