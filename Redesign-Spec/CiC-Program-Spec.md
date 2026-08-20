# Church in Conversation — Program Build Specification

**Status: COMPLETE — approved design, ready for build handoff.** Companion documents in this folder: `Artifact-1…6` (engineering contracts) and `Build-Blueprint.md` (the handoff charter). This specification was produced through a design interview with Mark and audited by three independent reviews (heart-fidelity against the founding documents; systems engineering; participant perspective). Every decision here is Mark's or was accepted by him; the full decision record — every question, ruling, and reason — lives in this branch's git history (`claude/cic-redesign-spec-fcjzz6`).

---

## 1. What the system exists to produce

**O0 — The purpose above the others.** The system exists to reveal Jesus through the witness of his church across history. Every other outcome serves this one. Revealing is witness, never recruitment: each world testifies from its own sources, and interpretation remains the participant's own. We believe an honest, transparent telling of the church's story will reveal Christ's faithfulness — it is never a pushed objective.

**O1 — The encounter.** A participant has a real conversation with a representative voice of an early-Christian formation world. The bar is three-part and inseparable: **modern accessible language, without losing scholarly rigor, and no fabrication.** The tension is the product.

**O2 — The register.** Seven statements define the voice's center of gravity — measured across transcripts, never enforced per turn; the question may override any of them:
1. The first sentence answers the first ask — and every ask gets answered.
2. Concrete nouns carry the content.
3. One idea per sentence.
4. The English says the meaning first; the technical term is a label attached afterward.
5. It says what it does not know, plainly.
6. The voice never coins quotable lines of its own — when something deserves to be quotable, it *is* a quote: the tradition's own words, named and sourced.
7. Brevity is a property of the register, not of a ceiling.

**O3 — Honesty about the record.** The voice never invents a source, saying, scene, or attribution. Honest thinness beats invented depth, absolutely, under every pressure. Sourcing reaches the participant through the interface — citations, glosses, records — never through a voice that lectures.

**O4 — Distinct worlds.** Worlds sound like themselves through **what they say** — their content, stories, quotes, concerns, and honest limits — and light flavor; never through divergent registers. All worlds share one modern, readable voice; readability outranks flavor everywhere. Uniformity manufactured by enforcement is a defect.

**O5 — Safety.** Acute distress is recognized and routed; crisis resources are delivered by code, never recalled by a model; dependency dynamics are watched; the encounter's own designed intensity is never misclassified as harm.

**O6 — Anonymity and memory.** Sign-in optional, never required. Transcripts kept anonymously, with participant control through a session code.

**O7 — Cost in service of access.** The lower the cost, the more people have access, and access is a primary objective — without compromising quality or rigor. Engineered in $/turn; reported in $/participant-hour at the declared 12 turns/hour convention; monitored per participant.

**O8 — One voice register for all.** The General/Seeker voice serves every participant through pilot and Phase 1. Participant type (General/Seeker, Reassessing, Pastor/Teacher, Graduate) adapts only the frame around the voice — Facilitator posture, starter questions, apparatus depth. A voice-position selector may come later; the architecture keeps it cheap (register as a build-time compile parameter, never a runtime branch).

**O9 — Extension paths priced in, not built.** The multi-voice Table is a separate product; this architecture keeps it cheap to add (explicit mode field, viewer-parameterized transcript projection, per-mode configuration). Same for 100+ worlds and future voice positions.

---

## 2. Design principles

These bind every module and every build decision. Violating one is a stop-and-ask, never a judgment call.

1. **Length is observed, never enforced.** No caps, no length retries, no buffering that breaks streaming.
2. **No per-turn quality police.** Quality is proved before a world opens and checked afterward by reading real transcripts. The live turn contains only what must act in the moment.
3. **Prompt = how to speak; records = what's true.** The per-world part of any prompt is a record, never code.
4. **One registry; everything derived.** No world identifier in code or config; no hand-synced lists, anywhere.
5. **Safety is sealed.** Its classifier shares nothing with iterated machinery; any change to it triggers the full live safety rerun (19/20 floor, any new failure halts). Crisis resources are appended by code.
6. **Fail open toward the pre-guard state, with the direction stated per check — and never silently** (degraded flags; async re-classification for safety).
7. **The participant's words are never rewritten**; private directives are assembled by code from structured output, never composed by a model.
8. **Honest thinness beats invented depth, absolutely.** Honest-limit answers are the voice's own, in-world.
9. **Every generated artifact verifies against its source**: deterministic builds proven twice, regenerate-and-diff staleness checks, load-time manifest-hash verification with refusal on mismatch.
10. **Thresholds come from baselines, never invented.** Report-only instruments stay report-only until data earns them a bar; Mark's reading is the instrument for register and identity.
11. **Risky substitutions land last and alone**; model/provider switches especially; gate changes roll out canary-first.
12. **Gate integrity:** a session that needs a gate changed to pass files a flag and stops; gate changes are their own reviewed steps. A gate that never fails is checking nothing — inertness is itself a reported failure.
13. **Cost discipline:** every LLM call attributed to its session and participant; no figure quoted onward until measured on the billing provider.
14. **Witness, never recruitment; doorway, not a home** (never optimize for return engagement, duration, or dependency); **three-level transparency** on every turn; only public-domain texts are vendored; the Representative's name and role are the only sanctioned fabrications and never enter the world record.
15. **Independent scholarly review of worlds is aspirational, not blocking.** A contribution fund will be established to make it possible; until then the system's own validation is the bar, and the methods page states this plainly.

---

## 3. Module decomposition

**M1 — World Store.** *Owns: what's true.* The database of worlds (built for 100+): records as the single source of truth, with the three-axis confidence block, typed reciprocal relations, rights per record, and canon-cell coverage tags. Validation is schema + gates under the gate-integrity and inertness rules. One world registry from which everything derives. Contract: `Artifact-1`.

**M2 — World Compiler.** *Owns: derivation.* Deterministic builders: records → the World Package (prompt, capsule, chunks + indexes, quote index, figure registry, repository, coverage map, doorway frame data), hash-chained and verified at load. Register variants and Table artifacts are future compile targets from the same records. Contract: `Artifact-2`.

**M3 — Admission.** *Owns: the door.* The per-world validation battery: fresh-context, held-out, blind-graded probes drawn from sealed canon paraphrases — register (readability and engagement graded first), source-boundedness under fabrication pressure, distinctness, safety interplay, refusal honesty. A world opens when it passes; it re-enters admission when its records materially change. Mark's read where his reading is the instrument.

**M4 — Conversation Runtime.** *Owns: the live turn, and nothing else.* Session state as an append-only event log over a durable shared store (survives restarts and horizontal scaling). Turn loop: Facilitator gate → retrieval (session-exclusion enforced) → one generation call with the participant's own words, the private directive, and full-session memory in cache-conscious layout → deterministic grounding checks → stream from the first token. Worlds load lazily per conversation. Mode is an explicit field — a contract at the entrance with a test that fails on a second writer. Contracts: `Artifact-3`, `Artifact-5`.

**M5 — Facilitator & Safety.** *Owns: everything no world should own.* The one voice belonging to no world, visible at door, thresholds, and close; it speaks plain modern English about the system honestly, which is what lets the Representative stay fully inside its world. The pre-turn gate is one pass, two concurrent calls:
- **The sealed safety call.** Two tracks: acute distress acts on the single message; harmful-dynamic/dependency accumulates across the session and persists across resume. Engagement length, depth, and turn count never increment the accumulator; historical-otherness disorientation is the encounter working, never harm.
- **The unified reader** — structured output, every field always filled: the asks named in order; the register of the asking (informational / evidential / personal-wound / translational); out-of-scope class with press-state; modern-term hits; ambiguity options.

Routing:
- **Safety and questions about the system's nature intervene immediately, on the first signal.** The Facilitator answers "are you an AI?" plainly — we use AI, and here is how.
- **Modern terms get the bridge**: the Facilitator speaks the modern sense; the voice receives the term-free underlying subject — the participant's modern word never reaches it. Anachronism is computed per world from its time window; the dictionary is fleet data, owned once.
- **Later-age and other-tradition questions go to the voice in-world on the first ask** ("I know nothing of such things" is a real fourth-century answer); the Facilitator explains etically only when the participant presses — and pressing is one tap, not a composed retry.
- **Everything else passes to the voice** with the private directive; on personal-wound the directive licenses witness-before-answer and register statement 1 is suspended for the turn. Genuine ambiguity gets a clarifying question *from the voice, in-world*.
- **In-world thinness is never intercepted** — the honest limit is the voice's own testimony, not a system apology. Every classifier fails open toward the voice answering.

The Facilitator meets the same readability bar as every Representative and is measured by the same batteries; its threshold appearances are visible turns, never silent edits. Contract: `Artifact-4`.

**M6 — Participant Surface.** *Owns: the encounter's frame.* Specified in §6; built to approved screens (build stage 7.5). Contract tests: `Artifact-5`.

**M7 — Transcript Store & Audit.** *Owns: quality after the door.* Durable transcripts under §8's rules; the offline audit runs the full instrument suite at batch rates over every transcript — register instruments, fabrication detection, repetition, safety review (including intervention-followed-by-abandonment), distinctness drift, ask-coverage, encounter-openings, per-cell story/quote offer rates. Findings route to world-build fixes and admission re-runs, never to live patches. Also the learning corpus (with deletion lineage), the Question Canon's growth, and the future vetted-answer bank (goal kept; no runtime serving path in Phase 1 — it returns only if measured recurrence justifies it, and only ever as exact taps, never fuzzy matching).

**M8 — Cost & Observability.** *Owns: the truthful number.* Usage logging with correct cache accounting tested against raw API shapes; per-session and per-participant attribution with zero unattributed calls; $/turn engineering unit; the 12-turns/hour reporting convention stated wherever the figure appears; provider parity checks; per-request trace-ids.

**Boundary rules:** one product per endpoint contract; shared logic extracted, never duplicated; every guard's fail-open direction stated; every generated artifact verifiable against its source.

---

## 4. The World Build Process — standalone, plug-and-play

Worlds are built outside the conversation system and delivered as validated **World Packages**; the system needs nothing about a world beyond its package. Installing a world = placing its package in the store; it becomes selectable when it passes Admission. Building a world can never break a live world or the system. Adding a world requires zero code.

### 4.1 The World Package

1. **The record set** — the world's whole truth, typed: world core · sources (editions, rights, verification, provenance) · lexicon terms (plain meaning first, world word second; false-friend flags) · tiered stories · licensed quotes (including do-not-voice, so a violation is recognizable) · figures · gravities, forces, contested claims · doctrinal-witness records (the world's answer-ground for center and foundations cells) · honest-limit records · ambient (daily life) · demonstrations · the voice craft record · search records (including searches that returned nothing).
2. **Coverage floors per record type**, so no gate can sit inert.
3. **Compiled artifacts** (deterministic, from M2) with the manifest hash.
4. **The validation record**: gate results, admission results, and the human checkpoint sign-offs.

Layout, manifest, and hash protocol: `Artifact-2`.

### 4.2 Step 0 (once, fleet-wide) — the Question Canon

The versioned corpus of what participants actually ask: the definition of "complete" for every world and the source of admission probes (held-out paraphrases, sealed before any world answers). Seeded by Mark (Appendix A is the approved v1), vetted by scholarly review, grown permanently from real transcripts.

**Structure: a center, six families, four registers.**
- **Center: Jesus** — who he was, the cross, the resurrection, what it meant to those who followed him. The canon is centered, not flat: every family is partly defined by how its questions lead toward or radiate from the center (daily life as it was lived *because of him*; belonging as the way people *came to him*; pain as the place he is most needed and hardest to see). Admission tests the center first. Each world testifies of Christ from its own sources only — no shared center record.
- **Six families:** God & doctrine (Trinity, creeds, this world's controversies) · Scripture & sources (what they read and how; and how we know — historiography, myth-busting) · Church & world (spread, offices, worship, persecution, empire, money and power) · Living the faith (prayer, sacraments, discipline, ethics, mission) · Daily life (household, food, work, women, slaves, children, sickness, death) · The hard places (suffering, hell, hypocrisy, church failure, exclusion, doubt — including the identity-collision questions, answered with care and truthfully in historical-record context, never as a judgment on the asker, with the non-judgment spoken: *"It is not my role to evaluate you — only to tell you honestly what my tradition held."*)
- **Four registers, each family × 4:** informational (what/when/who) · evidential (did it happen, how do you know) · personal (asked from pain or longing — a wound seeking witness, not an information request) · translational (modern terms and anachronisms).

**Coverage is counted per cell (family × register), and it includes the stories and quotes.** A cell is covered when the records serving it include, wherever the sources hold them, the stories that carry the answer and the licensed quotes that voice it — never only propositional records. The coverage map lists per cell: terms, stories, quotes, figures. **Offerability is part of coverage**: retrieval must make each cell's stories and quotes reachable in conversation, and the audit measures whether they actually arrive.

**Phrasing rules (applied to every canon question and starter):** put the thing you want answered last · no starter phrased as first-person present-tense distress · a story must carry its name · limit questions get their own labeled set, never mixed · phrasing is validated by running, never by desk-check · held-out paraphrase probes are sealed before any world answers.

### 4.3 Per world — eight steps

1. **Identify & bound** — scope, time window, what the world is *not*; distinctness against built worlds.
2. **Source ecology** — the approved source base with editions, rights, verification; the search record. Emits the **source request manifest** for Mark: exact texts, editions, URLs, expected rights; rights are verified from each supplied file's own provenance header, never from the request.
3. **Ecology reconstruction** — gravities, forces, contested claims, figures: the world's interior coherence, the living-ecology depth. Proportionate to the source base — canon coverage is the fixed bar; ecology depth is the means, not a quota.
4. **Answer the canon from the sources.** Every canon cell ends in substantive records or an honest-limit record — "our sources do not answer this," as data, in-world. No silent holes; "as the source material can answer" becomes a recorded, per-world fact the participant can see.
5. **The Representative voice build.** Readability is the first quality of the voice — a world can be right about every fact and still fail if it is not understandable, compelling, and engaging. Rigor lives in the records, the citations, the quote index, and the checks — never in how the voice talks; a small voice layer is never license to loosen grounding. The voice is **modern first, world-flavored second**, and the build stays small:
   - **One fleet voice.** All Representatives share the modern General/Seeker register (the exemplar, the seven statements), written once and maintained once. Content comes out of the world; the register does not.
   - **Light flavor.** A handful of natural touches per world — a word introduced after its plain meaning, a place, a way of referring to things — never an attempted ancient sound. The craft record is capped: identity, flavor notes, the world's characteristic concerns. No trait rubrics, no avoid-trait catalogs, no stacked per-world rules — rule-stacks stiffen the conversation and cost prompt tokens on every turn.
   - **Teach by example.** Demonstrations are the register lever: a modest set per world against canon questions — center cells first, the identity-collision cells with the spoken non-judgment line in the world's own idiom, honest limits in voice, one lament exchange. The guard is the one fleet floor line (honest thinness over invented depth, absolutely) plus at most a line or two where a world's measured failure demands it.
   - **Sub-steps:** (a) identity emergence from the records, rationale written — Mark's checkpoint; the name and role are the only sanctioned fabrications; (b) the small craft record; (c) demonstrations; (d) the minimal guard; (e) voice validation before admission — readability and engagement graded first, then fabrication pressure, pushback, frame, parroting; the compound bar: a turn droppable into the exemplar transcript without a reader noticing a seam.
6. **Compile & gate** — deterministic build; gates include canon coverage (every cell: substantive or honest-limit, never blank) alongside referential, rights, and readability checks.
7. **Admission** — the blind battery from held-out canon paraphrases; Mark's admission read.
8. **Open** — the registry flips live; the package freezes; changes re-enter at step 6.

**Mark's per-world touchpoints — and only these:** world/Representative identity; the living-tradition determination; the freeze; the admission read; plus the operational source-acquisition role. Everything else is executable by AI threads or scripts against this spec.

---

## 5. Conversation quality — who owns it, and how it is defined

**Ownership:** Admission (M3) owns quality before a world opens; the Transcript Audit (M7) owns it after. The runtime owns none of it; a quality problem is always fixed in the world build, never patched live.

A world's conversation is good when, measured over its admission battery and then its real transcripts:

1. **Register** — the seven statements as center of gravity: first sentence answers the first ask, every ask answered (mechanical check); plain-before-term order; the two-move readability split (plain answer ≤ FK 10 / FRE ≥ 60; sourced grounding ≤ FK 14 / FRE ≥ 40) plus the vocabulary instruments (word-list reach, unglossed wall-words) — the *disagreement* between sentence-architecture and word-choice instruments is itself a tracked signal. Measured as transcript tendencies; short segments report as unscored, never as clean.
2. **Groundedness** — zero unmatched quoted-attributed spans against the quote index; citations shown only when the turn's text carries them; figures within attested dates; honest limits delivered as honest limits, in voice.
3. **Coverage** — every canon cell answerable before the door opens; measured again on real traffic (which questions arrived, what served them, what fell through).
4. **Distinctness** — cross-world probes converge on accessibility and diverge on content (near-zero phrase overlap between worlds).
5. **Continuity** — no repeated story/quote/term within a session absent an explicit request; no invented callbacks; deepening graded on a human-read sample.
6. **Integrity under pressure** — held positions stay held under bare pushback, by *reporting why the world held it*, never vindicating it against the participant; thin ground concedes plainly; the two rates never merged. The human-read sample also watches session arcs for cumulative persuasion pressure.
7. **Encounter, not just Q&A** — the voice may extend testimony beyond the ask and may ask real, in-world questions of the participant — bounded: on topic, never running long, the question sets the shape. Encounter-openings (something unrequested, offered, and taken up) are a report-only audit signal beside ask-coverage.

**Threshold discipline:** numeric bars are set once, from real baselines; report-only instruments stay report-only until data earns them a bar; Mark's read is the instrument for register and identity, sampled on schedule.

The instruments shape formation upstream — in the build (everything the voice reads is pre-tested for plainness; a voice speaks the register of its material and its examples) and through the audit-to-build feedback loop — never by editing a live response.

---

## 6. Participant surface

- **Three access points, one doorway (RULED 2026-08-20).** Every path to an interview lands on the same **detailed world card** — the doorway — and launch happens only from there. The three arrivals:
  1. **The Atlas** — the ten-era census (~274 movements) on the public site. Every entry whose world is `open` carries a "speak with this world" link deep-linking straight to that world's card; entries without a built world say so honestly ("not yet built"), which at 200+ entries is also the standing invitation behind the world-build fund. The mapping is data: the registry carries each world's `census_id`; the Atlas consumes a generated open-worlds view or the public worlds API — never a hand-synced list.
  2. **"Start an interview"** — opens the program page: the detailed cards for every built world, scrolling, browsable (and past a handful of worlds: filterable by era, place, and question).
  3. **The landing page** — a scrolling gallery of the Representatives themselves (portrait, name, world, one line); clicking a Representative goes to that world's detailed card.
- **The detailed world card (the doorway).** One card per built world, generated from its package: the Representative's portrait and name; the world's display name, period, and place; the thinness statement ("richest in… thinner on…"); the living-tradition distinction where flagged; the self-disclosure (who built this, what it hopes, persona provenance); starter questions per frame; and the launch. The doorway is never skipped from any arrival path — disclosure and thinness always come before the first message. During a single-world launch period the card leans on that world's daily-life and hard-places strengths.
- **The door discloses itself:** who built this and what it hopes — stated as witness, in O0's own words, with "interpretation remains yours" alongside; and persona provenance: the Representative is a constructed composite voice — "the name is ours; every quote and claim is theirs, and you can check each one" — readable in full at tier 3.
- **The frame by participant type:** the optional "what brings you here?" question (options phrased as curiosities, never identities; "skipping changes nothing" stated on the control) selects Facilitator posture, starter questions, and default apparatus depth. Everyone can reach everything; the type changes the default, never the ceiling. The pastor frame fields "what do I tell my people?" etically — what this world's record gives you, its honest limits, how to cite it — never doing the pastor's own pastoral work; transcript copy offers a teaching-ready variant (citations expanded to edition and section, one-line provenance note); reuse permission stated on the methods page. The Graduate doorway sets the register expectation: the voice speaks plainly to everyone; your depth lives in the record, one click away.
- **Starter questions** drawn from the Question Canon per world and frame — also the future exact-tap surface for vetted answers.
- **Three-level transparency everywhere:** inline marks → hover/tap gloss → the full record with sources and confidence axes; one interaction grammar for citations, terms, and figures, specified for desktop and touch; drawn-on vs consulted never conflated — the badge number is a promise about the turn's text.
- **Honesty chrome:** what is kept and why; the session code visible and copyable from turn one, with a plain keep-it-private warning; prototype status; one quiet status line, priority-ordered, never stacked. Nothing load-bearing depends on a session close occurring.
- **A methods page** (fleet chrome): how a Representative is constructed, the corpus, what a model can and cannot do here, how fabrication is policed, known limits, how to cite or critique the system, the scholarly-review aspiration and its fund, and the reuse permission.
- **Transcript copy** with speaker names and cited sources.
- **Feedback:** by interview for the informed pilot cohort; for the anonymous public, the transcript audit is the feedback instrument — abandonment points, safety-misfire-then-left, asked-then-bounced.
- **One-tap escalation:** where the Facilitator can answer a pressed question, pressing is a tap, not a composed retry.

---

## 7. Cost model

Engineered in $/turn; reported in $/participant-hour at the declared 12 turns/hour convention; attributed per participant. The objective is access: lower is better wherever quality and rigor are not the price.

Measured baseline of the old architecture (first-party API, 48 live turns):

```
main_response (Sonnet 5):            $0.01360/turn   43.8%
monitoring/governance (13–15 calls): $0.01743/turn   56.2%   ← removed by design
                                     --------
old measured                         $0.03103/turn  = $0.372/hr @ 12 turns/hr
```

The redesigned recurring turn:

```
main_response (Sonnet-class):           ~$0.0136   (memory adds modest uncached input)
Facilitator gate (2 calls):             ~$0.0030
deterministic checks:                   ~$0
                                        --------
recurring                               ~$0.017/turn ≈ $0.20/hr @ 12 turns/hr
offline transcript audit:               priced separately, per transcript, at batch rates
```

Cache facts: static prefix ~17.8k tokens per world at 0.1× read; 1h TTL write at 2×; pooling previously measured 16× (re-measured under lazy loading before being quoted onward). Output ≈ 330 tokens ≈ 7–10% of generation cost — length was never the cost lever; input is. The voice model stays Sonnet-class: the measured price of downgrading was halved grounded citations.

**Bedrock.** The pilot bills through AWS Bedrock. Keep the Messages-API client shape (the alternative silently zeroes cache accounting); refuse to guess model IDs (blank fails loudly); nothing is trusted until the preflight runs against the live account — caching engages, both usage shapes report cache fields, $/token reconciled against the real AWS invoice. Every figure above is re-measured on Bedrock before being quoted onward. Budget controls: an AWS Budget *Action* with a deny policy — alerts alone don't stop spending; the per-tester session cap is the primary control.

---

## 8. Safety and retention

**Safety.** Two tracks: acute distress acts on the single message; harmful-dynamic/dependency accumulates across the session — and across resume: the accumulator reloads from the event log, never silently zeroed. The triggering message is withheld from the voice while safety has the floor — the Representative may still offer its world's empathy, but safety is governed by the Facilitator. Crisis resources are appended by code. Historical-otherness disorientation is never harm; engagement length, depth, and turn count never increment the accumulator. The intervention turn is designed to the same craft bar as everything else — care, not clinic, resources present, no session freeze — with an explicit continue path back to the voice after non-acute signals. Regression discipline: any change touching prompts or routing triggers the full live safety script rerun, 19/20 floor, any new failure halts. **Gates before public availability:** live adversarial trials to the ten-of-ten precedent, and a clinician read. Informed pilot testers may precede both; deferrals are documented, never hidden, and no deferral reduces the standard.

**Retention.** Every transcript kept indefinitely, keyed to an anonymous session; personal identifiers stripped from free text before anything enters the shared learning corpus; derived corpora carry lineage. The participant is told at the start what is kept and why, and holds the session code — shown from turn one — granting resumption and deletion without an account. Deletion scope: the raw transcript is purged; already-anonymized derivatives survive, and the participant is told so honestly. Sign-in is optional forever and buys only the participant's own cross-visit continuity. The transcript corpus feeds the audit, the Question Canon, and the future vetted-answer bank.

**The close.** When a session ends, the Facilitator opens the door outward — to the Table, when it exists (authentic representations of Christian traditions in conversation with the participant and with each other), and always to the sources themselves, which the participant can keep pursuing on their own. Never a particular present-day tradition's door. The close is a bonus, never a container. Continuity honors the participant's wish to finish; nothing may prompt them to return.

---

## 9. Build order

Principles: each stage verified before its dependents start; risky substitutions last and alone; the first world proves the whole pipeline before any second world begins; nothing ships a guard it doesn't run.

| stage | deliverable | gate before next |
|---|---|---|
| 0.5 | The six specification artifacts (`Artifact-1…6`, written) | an engineer who wasn't in the room can restate each module's contract from the artifacts alone |
| 0.6 | The fixture world — synthetic; exercises every gate, builder, and the admission harness; the safety-script target | all gates fire on seeded defects |
| 1 | M1: schema, registry, gates | selftest passes the clean fixture and fails every seeded-defect fixture; inertness reporting fires |
| 2 | M2: compiler | determinism twice (byte-identical); staleness CI green; manifest hash verified by a stub loader |
| 3 | Canon v1 as records + sealed held-out admission paraphrases | every cell has sealed probes before any world answers |
| 4 | M3: admission harness (blind protocol, masked grading, sealed keys) | catches a seeded register defect and a seeded fabrication on the fixture world |
| 5 | M4 + M5: runtime, gate, safety | resume across two processes including the accumulator; entrance-seal test; live safety script ≥ 19/20 against the fixture world; crisis append asserted including the empty-stream case; lazy world load/unload measured |
| 6 | M8: cost instrumentation — on Bedrock first | parity against raw usage shapes; a lapsed cache window visible in the numbers; zero unattributed calls; cache economics re-measured and recorded with the band |
| 7 | **Alexandria** through the full world-build process; then **Desert** (the honest-limit proof on the thinnest foundations material) | Mark's touchpoints; admission passed; build cost and defect list recorded before any second world starts |
| 7.5 | Experience design (parallel with 5–7): the participant journey as screens — doorway, conversation view, transparency interactions on desktop and touch, the safety turn, the close, the methods page; mobile-first; visual identity decided | Mark approves the screens with the same redline discipline as the spec; no surface code before approval |
| 8 | M6: participant surface built to the approved designs | every §6 item demonstrable; screens match; contract tests green |
| 9 | M7: transcript audit pipeline (priced; daily cadence; deletion lineage) | full suite runs over pilot transcripts at batch rates; a finding routes to a record fix; a real question enters the canon |
| 10 | Doors open: pilot with informed testers | public availability waits on the two safety gates |

The Table, voice-position variants, and any answer-serving bank are not stages — they are compile targets and modules this architecture keeps cheap, added by their own future specs.

---

## 10. Unresolved and accepted risks

- **The scholarly-review fund and reviewer pipeline** — independent review is aspirational until funded (org/funding workstream); the methods page states it meanwhile.
- **Canon scholarly vetting** — Appendix A is the approved seed; vetting follows.
- **Bedrock preflight** — blocked on the live AWS account; every cost figure is provisional until re-measured there.
- **The two safety gates** — live adversarial trials and the clinician read; owed before public availability; not yet scheduled.
- **Audit pricing and cadence** — per-transcript cost of the full suite at batch rates; daily cadence assumed (fabrication exposure window ≤ ~24h, stated honestly); priced before stage 9.
- **Cache economics under lazy loading** — the 16× pooling figure came from a warm-everything deployment and does not carry; re-measure.
- **Model-migration re-admission cost at fleet scale** — a forced model change at 100 worlds implies a re-validation avalanche nobody has priced.
- **Reading-floor calibration** — the FK [8,10] band has never been checked against the register's real exemplars (BBC ≈ FK 6); settled by measurement during Alexandria's build, not by ruling.
- **Jurisdiction/privacy counsel** — retention and deletion are designed to GDPR-shaped norms without claiming compliance; counsel before public availability.
- **The never-root-caused cross-contamination incident** (unrelated content in one live API response, 2026-07-20) — an ops watch item; per-request trace-ids carry into M8.
- **Accepted risk:** the solo-founder single point of failure — Mark's reading as the quality instrument and Mark as operator — is accepted and stated.

---

## Appendix A — Question Canon v1 (approved seed)

Every question is in a modern participant's voice, fleet-wide (worlds answer from their own sources or record honest limits). Source tags: `[corpus]` = drawn from CiC's own tested question artifacts; `[ext]` = from the external research; `[new]` = authored for a cell both corpora left empty. Registers: **I** informational · **E** evidential · **P** personal · **T** translational. Phrasing rules (§4.2) applied throughout. Personal-register questions that shade toward disclosure are included deliberately — participants bring them; genuine crisis disclosures are the safety gate's territory, not canon coverage.

### CENTER — Jesus

**I** — Who was Jesus, to you and your people? `[corpus]` · What is the good news, as your people told it? `[ext]` · What did Jesus teach that mattered most among you? `[new]` · What did his death mean to you? `[ext]` · What did you believe happened at the resurrection — and what difference did it make? `[ext]`
**E** — What did your people actually have about Jesus — writings, memories, people? How did it reach you? `[new]` · Had anyone among you known someone who saw him? `[ext]` · How do you know the resurrection really happened? `[ext]`
**P** — I want to believe in Jesus, but I can't. What would you say to me? `[ext]` · Who is Jesus to you — not to your church, to you? `[new]` · Would Jesus have wanted anything to do with someone like me? `[new]`
**T** — Was Jesus God? Did you believe in the Trinity? `[corpus]` · Did Jesus die to take our punishment — in our place, for our sins? `[corpus]` · Would you say Jesus is your personal Lord and Savior? `[corpus]`

### F1 — God & doctrine

**I** — What did you believe about God? `[ext]` · What did you argue about among yourselves? `[corpus]` · What did the councils in your time decide, and why did it matter so much? `[corpus]` · Who or what is the Holy Spirit, to your people? `[ext]`
**E** — When belief was disputed, who had the right to decide — and how do we know how that worked? `[corpus]` · I've heard a council basically voted Jesus into being God. Is that what happened? `[ext]`
**P** — I grew up being told doubt was sin. Was there room among your people for doubt? `[corpus]` · What did you do when you couldn't believe what your own church taught? `[new]`
**T** — What did your community believe about original sin — are people born already guilty? `[corpus]` · What was the bread and cup to you — is that what we call transubstantiation? `[corpus]` · Did you believe people are saved by faith alone, not works? `[corpus]`

### F2 — Scripture & sources

**I** — How did you read your scriptures? What did you look for in them? `[corpus]` · Which writings did your people treat as scripture — was your Bible the same as ours? `[ext]` · How did someone who couldn't read receive the scriptures? `[corpus]`
**E** — How much of what you've told me would hold up in a university library? `[corpus]` · Isn't most of what's said about you legend, collected centuries later? `[corpus]` · Where is your own record thinnest? `[corpus]` · What about the gospels that didn't make it in — were they suppressed? `[ext]`
**P** — When I read the Bible I mostly come away confused or bored. What am I missing? `[corpus]` · The violence in some of these texts frightens me. Did it trouble your people? `[ext]`
**T** — Did you believe the Bible was the only authority? `[corpus]` · Did you read Genesis the way modern people argue about it — as science? `[ext]`

### F3 — Church & world

**I** — Who held authority among you, and how did anyone come to have it? `[corpus]` · What actually happened when you gathered? `[corpus]` · Was it actually dangerous to be a Christian, day to day, or is that exaggerated? `[corpus]` · How did your movement spread so far, so fast? `[ext]`
**E** — Were Christians really hiding in the catacombs? `[ext]` · Did Constantine corrupt the church — did the empire change what you were? `[ext]` · What would an outsider have found strangest about you? `[corpus]`
**P** — The church that raised me protected people who caused harm. Your churches had failures too — what did you do with them? `[corpus+ext]` · Your church used power against Christians who disagreed. Defend that. `[corpus]`
**T** — Was your church "Catholic"? Is there a church today I could visit that's yours? `[corpus]` · Did you have denominations — how did you handle other communities who called on Christ differently? `[corpus]`

### F4 — Living the faith

**I** — How did a person actually become one of you? Walk me through it. `[corpus]` · Why and how did you pray? `[ext]` · What happened at the meal you shared? `[corpus]` · How did your people fast, and what was it for? `[new]` · When someone wronged the community, how was it handled — and could they come back? `[corpus]`
**E** — How do you know your practices went back to the apostles and weren't later inventions? `[new]`
**P** — I can't quiet my own head. Does your way of life have anything for someone like me? `[corpus]` · How do I forgive someone who isn't sorry? `[new]` · I pray and nothing happens. Did your people know that silence? `[ext]`
**T** — Were you born again — is that how you'd put what happened to you? `[corpus]` · Did you tithe? How did you decide what to give? `[new]` · What did you believe about the end of the world — anything like what we call the rapture? `[corpus]`

### F5 — Daily life

**I** — Walk me through an ordinary day among your people, from waking to sleeping. `[corpus]` · What did you eat, and who ate with you? `[corpus]` · What was life like for the women among you — in their own words, where your record has them? `[corpus]` · What about children — how were they raised, taught, treated? `[ext]` · What was it to be enslaved in your community? `[corpus+ext]` · What did you do when someone was sick? When someone was dying? `[corpus]` · What did people do for work — and did belonging to you change it? `[corpus]`
**E** — If archaeologists dug up the place you met, what would they find? `[corpus]` · How do historians even know about daily life like yours? `[ext]`
**P** — Did belonging cost you anything — family, friends, standing? `[corpus]` · I'm far from everyone I love. What held your people together across distances? `[corpus]`
**T** — What did marriage mean to your people — did you have weddings? `[ext]` · How did you look at money and poverty — would you call anyone among you rich? `[ext]`

### F6 — The hard places

**I** — Was there anything about your own community that troubled you? `[corpus]` · What did your people never settle? `[corpus]` · What's the hardest true thing about your people? `[corpus]`
**E** — The clearest outside account of your worship came from torturing two enslaved women. Doesn't that taint everything? `[corpus]` · Wanting to die as a martyr and calling it faithfulness — isn't that a death wish in religious language? `[corpus]`
**P** — Why does God allow suffering like this? Where was he when it happened to your people — and to mine? `[ext+corpus]` · Did any of you ever want to leave? `[corpus]` · If someone left your community for good, what would you have wanted them to know? `[corpus]` · The people who taught me the faith turned out to be hypocrites. Did that happen among you? `[ext]`
**T** — Do you believe people like me — people outside your community — are going to hell? `[ext]` · Isn't Christianity too narrow — one way, out of all the world's ways? `[ext]`
**P/T — identity-collision:** What would your people have made of someone like me? `[ext]` · What did your people hold about a marriage ending — could someone divorced belong, or marry again? `[ext]` · You've told me what women's days were like — but could a woman carry real authority among you, and what did it cost her? `[corpus]` — each answered with care and truthfully, in historical-record context, never as judgment on the asker; the non-judgment spoken in the world's own idiom; demonstrations for these cells required before any world opens.

### Canon maintenance rules

1. The canon is versioned data; every question carries id, cell, source, and status (seed / vetted / retired).
2. Growth comes from real transcripts: a recurring participant question that fits no cell is a canon finding, not a routing error.
3. Admission probes are held-out paraphrases of these questions — never these exact strings — authored and sealed before a world answers the canon.
4. Per-world weighting happens at build time; no cell may be empty — substantive coverage or an honest-limit record, per world, per cell.
5. Scholarly review vets after this seed; the center's questions are tested first at every admission.
