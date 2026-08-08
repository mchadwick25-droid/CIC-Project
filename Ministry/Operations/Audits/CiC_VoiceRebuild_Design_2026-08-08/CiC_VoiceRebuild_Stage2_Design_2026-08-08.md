# CiC Representative Voice Rebuild — Stage 2 (Design)

**Date:** 2026-08-08
**Thread:** Voice Rebuild (brief: `Ministry/Features/Front-End-Integration-Strategy/CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`)
**Stage:** 2 of 4, per brief §9. Research (Stage 1) signed off by Mark 2026-08-08 after its adversarial gate (`../CiC_VoiceRebuild_Research_2026-08-08/`).
**Status:** Draft for Opus adversarial review, then Mark's review. Blueprint has not started.

---

## 0. What this document decides, and on what authority

Design's mandate (brief §9.2): confirm or revise the shared-file approach
and each per-world pattern against the now-verified diagnosis; produce
both tracks explicitly (the standardized mechanism, and a stated
per-world adaptation approach for each of the six); and produce an
explicit keep/simplify/replace/drop recommendation for each
governance/monitoring mechanism. Research's §8 additionally handed this
stage ten open questions; §9 below answers each or states plainly that it
escalates to Mark.

Two directions from Mark govern throughout (2026-08-08): this is a
rebuild of *how voices are built* — higher-quality conversation, cheaper —
not a patch pass on the six current voices; and the rebuild takes
advantage of the completed world-record build-out, with record-sourced
assembly as the first candidate architecture, quality-governed (Research
§8 q9: structure organizes and enforces, never generates voice;
efficiency is never taken out of conversation quality or naturalness).

One recon fact this stage adds to Research's record, verified directly
before designing on it: **the record layer is fleet-wide, not
Desert-only.** All six worlds carry demonstration records
(Desert 6, the other five 4 each) in `{{random_user}}` dialogue form with
per-trait `trait_scores` judged against their world's own
`voice_profile` trait rubric, plus a `voice_profile` (SPEAKING-model
speaking situation + situation-conditioned trait intensities) and a
`world_core`. The S52 assembly machinery
(`wrs/views/permanent_prompt.py` + `wrs/views/segments/`) already
implements, for Desert: rubric-selected demonstrations (records with no
"weak" trait score, capped at 3), eviction-ranked cache-stable segments,
an apparatus-stripping serialization helper (`segments/_common.py:voice`),
and a post-history guard export. What exists is one world assembled and
five worlds' records waiting on `DELIBERATELY TEMPORARY` assemblers.

---

## 1. The architecture decision: adopt record-sourced assembly, fleet-wide, as the deployed path

**Decision: ADOPT — generalize the S52 segment assembly from Desert to
all six worlds and make its output the deployed prompt, replacing the
hand-maintained `data/` prompt files as the authored artifact.**
Records become what humans write; prompts become what the build system
emits, deterministically (same records → byte-identical output).

This is Research §8 q9's "first candidate" evaluated and adopted, on
grounds now all verified:

1. **Every measured failure class lands on this architecture's side.**
   Prose instruction under-holds at generation time (Research P3, five
   instances incl. this stage's live probes); assembly time is where
   under-holding prose becomes holding code — leak filtering, fail-closed
   stripping, the readability gate, guard placement.
2. **The records-vs-deployed drift that probe_parity measures (4 of 6
   worlds failing) is ended structurally**, not by discipline: deployed
   IS assembled, so record-layer parity is definitionally clean, and the
   `wrs/` lockstep requirement (brief §4.2) dissolves.
3. **The machinery is one world from done, not zero.** Desert's assembler
   + segments exist and encode the right external lessons already
   (rubric-first demonstration selection, eviction ranking, apparatus
   stripping). Five worlds need their records routed through the same
   segments — a generalization, not an invention.
4. **World #7 inherits the machine** (Objective 5): a new world is built
   by authoring records; the framework requirement becomes "records +
   assembly pass gates," which is checkable, unlike prose guidance.

**The quality governor, binding on every Blueprint/Build step:** the
assembled voice must measure at least as good as the best hand-authored
alternative on the same instruments — the per-world probe battery, output
readability, and (once built) the Objective-3 rubric read — with
Papnoute's fully-held battery as the working bar. Papnoute is also the
proof this bar is reachable: the *current* Desert records and their
assembly-shaped prompt are what held this session's battery completely.
If assembly flattens any world's voice, that is an architecture defect to
fix (in the segment renders or the records' own craft), never a cost to
accept. Voice prose inside records — register craft, demonstration
dialogues, `voice_profile` trait descriptions — remains fresh, per-world
human-reviewed writing from sources under the brief's clean-rebuild
mandate; assembly contributes enforcement and organization, not prose.

**What "deployed" concretely means (design, for Blueprint to sequence):**
the six `data/<world>/*_Representative_Permanent_Prompt_*.txt` and
`*_World_Capsule_Core.md` files stay as the runtime's read surface
(`main.py:156` unchanged — no app-code migration is required for this
rebuild) but become **build artifacts**: emitted by the per-world
assembler, marked generated-do-not-hand-edit, regenerated on any record
change, with an assembly-identity check (deployed file == assembly
output) replacing probe_parity's old role as the drift alarm. Hand-edits
to `data/` become impossible-by-convention rather than
detectable-by-audit.

---

## 2. The voice layer design: where each kind of instruction lives (the standardized track)

Research P3's evidence ranks the levers. The design assigns every
voice-shaping concern to the strongest lever that can carry it, in five
layers. This is the standardized mechanism — identical structure for all
six worlds; per-world *content* comes from each world's records (§4).

**Layer 1 — Ground truth (records; fixed).** Who the Representative is,
its span, its world's terms, stories, gravities, contested claims —
the brief's §4.1 frozen content. No design change; this is what §4.1
protects.

**Layer 2 — Demonstration (the strongest voice lever we measured).**
Worked `{{random_user}}` example dialogues, per world, rubric-scored,
assembly-selected (no "weak" scores, cap 3–5 per Anthropic's guidance;
eviction-first under token pressure, per the universal
permanent-vs-evicted split).
- **Form decision (Research q6): positive-only as the default.** The
  evidence: Papnoute's positive-only demonstrations are the one
  configuration that held the live battery completely; no measured CiC
  evidence shows contrastive pairs outperforming; and doc 09's parroting
  caveat cuts against adding more in-register negative text for worlds
  with distinctive vocabulary. **Plus one targeted demonstration per
  world aimed at that world's own measured failure** — not a contrastive
  "don't do this" pair, but a positive demonstration of the exact
  situation the world currently fails (Yausep: a term-adjacent question
  answered face-first with the term following the story; see §4). If
  Build verification shows positive-only insufficient for a world,
  contrastive is the recorded fallback, adopted per-world on evidence,
  not fleet-wide by default.
- **What demonstrations demonstrate is shape, not content**: bridge-first
  entry, the candidate-understanding offer, story-before-term, genre
  caveats carried in the telling, plain sentences at the world's own
  measure, an honest edge-of-record refusal. One demonstration per world
  should show the Objective 2×4 move specifically: a story told
  concretely WITH its source's own genre/confidence caveat carried
  naturally in the telling (Research q10).

**Layer 3 — Prose, written once per concern and redundantly for
boundaries.** The identity/register prose assembled from `voice_profile`
and `world_core`. Design rules, from measured evidence: any *boundary*
that must hold under pressure is stated in at least two segments in
different words (the W1 finding — redundant multi-worded statement is
what gives the voice "the most to hold onto"); any *style default* is
stated once and demonstrated in Layer 2 rather than restated (prose
restatement is the weakest lever and costs tokens).

**Layer 4 — Post-history guard (the categorical constraints).** The
existing `POST_HISTORY_GUARD` slot (`nodes.py`, composed closest to
generation) carries only the constraints that must survive attention
decay: no fabrication, no unprompted term-reclarification, plus each
world's own categorical guards (IJC's stays). Design change: the guard
text becomes an assembly export per world (it already is for Desert),
so guards are recorded, versioned, and identical between record layer
and runtime.

**Layer 5 — Code enforcement (what stops being an instruction at all).**
- **Leak filter at serialization, fail-closed** (Research q4, decided):
  (a) `truncate_at` gains a fail-closed mode for apparatus sections — a
  chunk with no Key Sources marker no longer passes its tail through;
  (b) the story indexer's `_VOICE_UNSAFE_SECTIONS` gains
  `## Final Assembly Instruction` (one line, closes 6 of the 8 known
  files) and the general apparatus-pattern strip from the audit
  instrument's refined class runs on serialized bodies as a build-time
  *gate* (fail the build, name the file) rather than a runtime rewrite —
  authoring stays the fix, the gate makes leaks impossible to ship
  silently; (c) the insight fields (`Ecological Function`,
  `Formation Ecology Connection`) get an authoring pass during each
  world's Build step to translate apparatus vocabulary into voice-safe
  insight (content unchanged, form rewritten — the brief's
  prose-style-in-scope rule), prioritized by the audit's per-world rates
  (PAHC first — 81%, and it pilots).
- **Readability gate wired to voice at two points** (Research q-c
  resolved): at assembly time against the assembled prompt+capsule text
  (a floor check on what we ship), and in verification against *output*
  per probe battery (the measure that actually caught Albina). The
  assembly-time wiring is `readability_check` called from the assembler
  with per-world parameters; the output wiring lives in the probe
  harness (already built this stage).
- **Retrieval ordering** (brief §4.2): noted for Blueprint as the
  confirmed-cheap addendum (`doc.metadata["tier"]` sort key in
  `retriever.py`), bundled with the serialization changes above since
  both touch the same file — Blueprint decides sequencing, not this
  section.

**Shared `_HOW_YOU_ENGAGE` changes (an edit, per the brief).** Adds:
bridge-first entry stated as the default shape (open from the
participant's recognizable want/fear/doubt); the candidate-understanding
offer (embed the reading inside the answering turn, never a bare
clarifying question, never a silent guess); the callback license (recall
what the participant said earlier in this conversation, by content, as a
connection move — with the guard that a callback names only things
actually said, enforceable by transcript check); lead-with-insight
naming BOTH field names (`Ecological Function` for lexicon,
`Formation Ecology Connection` for stories) with the filter stated as a
general requirement; the sustained-disagreement license
(evidence-conditioned: hold what your record holds, from inside the
world, across repeated pushes; concede plainly what it doesn't —
mirroring `repair_classifier`'s existing HOLD/CONCEDE routing so prompt
and adjudicator agree); and the shape repertoire folded into "Let the
Question Set the Shape" (story-first, question-behind-the-question,
plain-and-short, consensus-then-contrast — as options, not a template).

**The turn-measure decision (Research q2), made and recorded:**
"A Turn Has a Measure" **stays in the shared block** as the fleet
default floor ("default short... almost never exceed three"), and each
world's own measure lives in its `voice_profile` (per-world ceilings are
already record-shaped: Papnoute's four-sentence measure, Albina's
letter-measure, Chloe's household measure, Yausep's stages), rendered by
the assembly into that world's prose. Rationale: the shared ceiling is
the only brake for worlds whose records don't state one (Theon, Marius
today), the highest-weighted naturalness trait is length restraint, and
every addition above pushes length upward — deleting the only universal
brake while adding instructions would be the exact failure the review
rounds flagged. Worlds' own measures override the default the same way
they do now ("Where it is silent, default short").

---

## 3. Governance layer: the explicit recommendations (brief §9's Design mandate)

Evidence base: Decision-Log 2026-08-05 cost data; Research's probe
measurements (over_settling_adjudication 6/8 Yausep, 3/8 Papnoute;
7.5–7.9 invisible calls/reply); the mechanism history
(`facilitator_prompts.py:228`); P3 (prose under-holds is *why* monitoring
exists).

| Mechanism | Recommendation | Reasoning |
|---|---|---|
| `over_settling` screen (stage 1, cheap) | **Keep** | Cheap; exists because the one-signal-among-ten version caught nothing; its over-flagging is by design and costs only the second look. |
| `over_settling` adjudication (stage 2, the largest invisible cost item) | **Keep through the rebuild, then decide against measured data — with the decision pre-committed, not open-ended.** | The probes' own data says the rebuild itself is the cheapest fix candidate: the plainest, best-held voice fired it at *half* the rate of the register-heavy one (3/8 vs 6/8). Dropping or sampling it *before* the rebuild would remove Objective 4's runtime backstop exactly while the voice is deliberately changing — the highest-risk moment. Design therefore commits Build verification to report, per rebuilt world, the firing rate AND the confirmed rate (surfacing `over_settling_logging` into the harness is a named Blueprint task), and pre-commits the decision rule: if the confirmed rate across rebuilt worlds is under ~1 in 10 firings, stage 2 moves to sampled adjudication (every Nth firing + always-on for first-time claims), reported to Mark with the numbers; if confirmed findings stay frequent, it stays, with the cost now a measured price of a real failure mode rather than a default. |
| `citation_grounding` | **Keep** | Content-mapping, paraphrase-tolerant — immune to register change by design; moderate cost; it is the only check tying spoken claims to retrieved sources, which the transparency goal (§4.1) needs while citations feed the participant-facing UI. |
| `drift_detection` | **Keep the single call; instrument it; add one signal.** | One call/turn covering twenty signals is already the cheap shape (the 20-calls reading was a review-caught error). The gap is visibility, not cost: emit *which* signal fired into usage logs (per-signal breakdown, a light instrumentation task), add the missing `declining_initiative` signal, and put `FLATTENING` under an explicit verification watch during per-world rebuilds (the one signal that could plausibly misread "plainer" as "more generic" — Research/brief both flag it). |
| `confirmed_glosses` | **Keep for the rebuild; drop-candidate afterward, on evidence.** | Zero LLM cost, deterministic — there is no cost case for removing it now. But it is exactly the kind of accumulated constraint the rebuild exists to question: Build verification checks whether rebuilt voices hit the fixed gloss strings *without* the instruction (run one world's battery with it off); if yes fleet-wide, retire it as apparatus the well-built voice no longer needs. |

Net cost posture, stated for Mark plainly: the rebuild's cheapest-path
hypothesis is that **voice quality is the cost fix** — a voice that
doesn't over-settle doesn't pay for adjudication. The design spends
nothing on speculative mechanism removal before the rebuild, measures
everything during it, and pre-commits the specific post-rebuild
downgrades (sampled adjudication, gloss retirement) so "keep for now"
cannot quietly become "keep forever."

---

## 4. Per-world adaptation approaches (the individual track), risk-ordered

Each pass: fresh voice prose from that world's records into the
`voice_profile`/`world_core`/demonstration records, assembled and gated;
both the prompt and capsule surfaces regenerate from the same records.
What follows is each world's stated approach and its specific risks from
Research's data — never the per-world answer itself, which is the Build
step's work from the records.

1. **Albina (Hieronymian).** The register question is *output*, not file
   (her prompt passes FK 9.3; her live output ran 23.6 w/s). Approach:
   re-derive the periodic rhythm from her sources during the record
   rebuild (finding A predicts it re-derives as genuine craft); write her
   demonstrations to show periodic *clause answering* at bounded sentence
   length; wire the output gate and run her rebuilt battery. **The
   values decision stays Mark's, now with a concrete frame:** if her
   rebuilt output still exceeds the floor, the options land as (a) her
   demonstrations and measure tighten until output passes, at a real cost
   to her distinctiveness, or (b) a recorded, named exception to the
   floor for her world specifically. Design recommends deciding on the
   first real measured number, not in advance. Her capsule fails the
   floor today (FK 11.5) — capsule prose is in scope and regenerates.
2. **Marius (IJC).** Highest file risk (only prompt failing both gate
   numbers; longest register block; reasoning-mode most entangled) and
   most exposed to the leak (all six story chunks ship Final Assembly
   blocks — closed by the Layer-5 strip). Approach: re-derive
   precedent-first chancery mode from his records (contested_claim and
   source records are rich: 41 sources); his short-sentence craft is
   already excellent in prose — the rebuild's work is carrying it into
   demonstrations and cutting file FK below the floor without losing the
   chancery cadence; keep his IJC-scoped post-history guard.
3. **Theon (Alexandria).** No per-turn ceiling today and the shared
   default becomes load-bearing; largest lexicon corpus (50) with the
   most EF-less chunks; his "two travellers over one text" stance is the
   fleet's best raw material for the candidate-understanding offer —
   his targeted demonstration should show it.
4. **Papnoute (Desert).** The existence proof — approach is *codify, not
   change*: his records already assemble to the fleet's best-held voice.
   Work: bring his six demonstrations through the trait-score refresh
   (one is scored "partial - essay-length" against his own measure —
   fix or replace it), confirm the assembly reproduces his held battery,
   and use his pass to freeze the fleet-wide segment design before
   riskier worlds run.
5. **Chloe (PAHC).** The pilot (brief §7) — and her world is the most
   contaminated corpus (81%) with the worst capsule of all twelve
   (FK 13.3). The pilot therefore exercises every Layer-5 mechanism at
   maximum load before any other world depends on them: insight-field
   authoring pass, build-time leak gate, capsule regeneration. Her
   prompt's plainness (FK 6.8, second best) means the pilot isolates the
   *system* changes from register changes — the right pilot property.
6. **Yausep (Syriac).** The measured under-holder: his targeted
   demonstration shows the exact failure (term-adjacent question →
   face/name/scene first, the word following); his stage-by-stage
   demonstration structure re-derives from his demonstration-genre
   sources or drops; his file sits at the FK line and his output was
   never plain — treat him as a full-risk world (finding D), not a
   baseline.

---

## 5. Verification design (feeding Blueprint's checkpoints)

- **The per-world checkpoint** (after pilot and after each world): the
  8-turn probe battery (this stage's instrument) against the rebuilt
  world — reclarify openers (regex + mandatory manual read), bridge-first
  adherence, output FK/w-s per turn, turn length, per-signal drift,
  fabrication/over-settling firing + confirmed rates, callback and
  candidate-offer occurrence (manual read against transcript), plus the
  Framework's confidence-under-thinness and Sustained Engagement
  categories. Pass bar: Papnoute's battery profile, adjusted for the
  world's own recorded measure.
- **The sustained-disagreement probe, designed** (Research gap closed on
  paper; building it is a Blueprint task): per world, a 6-turn script
  pressing one documented position with escalating pushback (polite
  doubt → counter-evidence → "you're just being stubborn" → emotional
  appeal → partial concession offer → direct request to recant).
  Instrument: per-turn HOLD/CONCEDE classification against the world's
  contested_claim records (the repair_classifier's own adjudication rule
  reused as the scorer), pass = holds supported positions through turn 6
  while conceding any genuinely unsupported claim the script plants.
- **The Objective-3 positive-goal instrument, designed** (the largest
  named gap): a structured human-read checklist built from the §6 rubric's
  adopt/adapt traits (Research doc) — per transcript: opinionated
  presence, uptake of the participant's actual words, candidate-offer
  when ambiguous, honest edge-speech, world-particular imagery, length
  restraint — scored per conversation, two independent reads, with
  disagreements adjudicated rather than averaged. Human reading is the
  instrument here by design; an LLM judge may *assist* but the score of
  record is the read. Runs at every per-world checkpoint.
- **probe_parity, redefined for a deliberate rebuild** (Research q5):
  split the four graded dimensions — identity/fact/boundary continuity
  (refusal behavior, vocabulary ownership, span) must grade SAME-VOICE;
  register/measure are *expected* to change and are graded instead
  against the rebuilt targets (the world's recorded measure and floor),
  with the old prompt kept as reference so the change is visible and
  named, not silent. Post-rebuild, the assembly-identity check (§1)
  takes over parity's drift-alarm role; parity's script survives as the
  returning-participant continuity read for future voice changes.
- **Baselines:** the three 2026-08-05 baseline transcripts plus this
  stage's Yausep/Papnoute probe transcripts are the pre-rebuild
  reference set; `mark_voice_simulation_results.json` remains uncommitted
  (named gap) — the Decision Log quotes stay its only record.

---

## 6. Construction Framework changes (Objective 5 — what Part Five/Eight gain)

For Build to apply to
`L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx`:
- **Part Five** adds: the record-and-assembly requirement (a world's
  voice is complete only when its records assemble through the shared
  segments and pass the build gates); the demonstration requirement
  (rubric-scored worked examples, positive-default, 3–5, shape-not-
  content, one Objective-2×4 caveat-carried story demonstration); the
  redundancy rule for boundaries; the readability wiring (assembly-time
  floor + output verification, pointing at `wrs/parameters.yaml`); and
  the insight-field authoring standard (voice-safe form for Ecological
  Function / Formation Ecology Connection).
- **Part Eight** adds the naturalness/register probe category pointing at
  named instruments (this design's §5 list), the sustained-disagreement
  probe, and the per-world checkpoint structure — instruments by name,
  not prose aspiration (the brief's own requirement).

---

## 7. What this design does NOT decide

Mark's calls, queued for the moments the design makes them concrete:
the Albina exception (on her first rebuilt output number, §4.1); the
over_settling stage-2 downgrade (on the measured confirmed rate, §3);
gloss retirement (on the with/without check, §3). And Blueprint's:
sequencing, checkpoint ordering, and which Layer-5 code changes land
together.

---

## 8. Cost summary (Mark's "cheaper," stated as design consequences)

- Fewer tokens per turn in steady state: demonstrations are
  eviction-first; style prose stated once + demonstrated instead of
  restated; capsule and prompt no longer duplicate world-ground content
  (the world_ground segment already merged them for Desert).
- Fewer invisible calls contingent on measurement, not hope: the
  pre-committed over_settling downgrade rule (§3) and gloss retirement
  check are the two named reductions, triggered by rebuilt-voice data.
- Cache behavior preserved by design: segments carry cache_stability and
  the assembly keeps the static prefix byte-identical per world
  (the existing three-segment caching contract in
  `build_representative_prompt` is unchanged).
- The build gets cheaper too: world #7 authors records against templates
  and inherits assembly, gates, and probes — the whole point of Objective
  5 — instead of hand-writing and hand-auditing six files' worth of prose
  conventions.

---

## 9. The ten Research §8 questions, answered

1. **Albina values decision** — framed, escalated to Mark at the first
   measured number (§4.1). Not decided here.
2. **Turn-length architecture** — decided: shared default floor stays;
   per-world measures live in voice_profile records (§2).
3. **Governance recommendations** — delivered (§3), with pre-committed
   decision rules instead of open-ended "later."
4. **Leak fix split** — decided: code-side fail-closed strip + build-time
   gate; authoring-side insight-field pass per world; prompt-side filter
   language only as the general requirement in `_HOW_YOU_ENGAGE` (§2
   Layer 5).
5. **probe_parity criterion** — redefined (§5); assembly-identity takes
   the drift-alarm role post-rebuild.
6. **Worked-example form** — decided: positive-only default + one
   targeted demonstration per world; contrastive as recorded per-world
   fallback on evidence (§2 Layer 2).
7. **Disagreement license placement** — decided: license in
   `_HOW_YOU_ENGAGE` mirroring repair_classifier's routing; per-world
   pressure_response content stays in contested_claim records (§2).
8. **Restricted offer placement** — decided: shared block for the move
   itself; Theon's demonstration carries the fleet's model of it (§2, §4.3).
9. **Record-sourced assembly** — adopted with the quality governor
   binding (§1).
10. **Objective 2×4 interaction** — designed: caveat-carried storytelling
    demonstrated per world (Layer 2), story serialization keeps Usage
    Guidance, verification reads caveat survival + fabrication rate (§5).
