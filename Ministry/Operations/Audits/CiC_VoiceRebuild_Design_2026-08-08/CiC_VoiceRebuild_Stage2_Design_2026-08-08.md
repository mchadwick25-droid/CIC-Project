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

Two recon facts this stage adds to Research's record, both verified and
both two-sided: **the record layer is fleet-wide in structure but not in
readiness.** All six worlds carry demonstration records (Desert 6, the
other five 4 each) in `{{random_user}}` dialogue form, plus a
`voice_profile` (SPEAKING-model speaking situation +
situation-conditioned trait intensities, all six carrying a
`native_measure` — though not all measured: PAHC's is marked "DESIGNED,
NOT MEASURED", IJC's "PROVISIONAL PLANNING FIGURE", and Desert's equals
the runtime ceiling; treat the fleet's numbers as mixed-provenance data
the rebuild re-derives) and a `world_core`. But the demonstration records are
NOT assembly-ready as they stand (this design's Round-1 review ran the
selector): IJC's four records carry no `trait_scores` at all — Marius
would assemble with zero demonstrations; the selector's no-"weak" filter
is currently a no-op because no record fleet-wide uses the score
vocabulary it filters on; three worlds score in a different vocabulary
entirely; and PAHC's four demonstrations belong to a predecessor persona
and carry bracketed apparatus that `segments/_common.py:voice` — a
field-render helper matching parenthesised citations at assembly time,
not a general apparatus stripper — does not remove (one more reason the
demonstrations are written fresh rather than routed through).
This does not weaken the architecture case — the brief already mandates
writing worked examples fresh for all six worlds — but it means the
demonstration layer is a per-world *build* deliverable with a schema
normalization in front of it, not existing content to route through a
selector (§2 Layer 2, §4).

The S52 assembly machinery itself (`wrs/views/permanent_prompt.py` +
`wrs/views/segments/`) is real and, for Desert, verified deterministic
end-to-end: the Round-1 review re-ran it and its output is
**byte-identical to both the committed staging file and the deployed
Desert prompt** — the assembly-identity check this design proposes
already holds for world one. What exists is one world's prompt assembled
and five worlds' records waiting on `DELIBERATELY TEMPORARY` assemblers —
The capsule side, stated precisely (this design's first draft got it
wrong in both directions): capsule *emitters* exist for all six worlds
(`capsule_prompt_views.py` + the five `s62_*` variants) and all six have
staged `*_World_Capsule_Core_generated.md` output — but that generated
output does not match the hand-authored deployed capsules
(`capsule_prompt_views.py`'s own note: hand-authored capsule prose
"will not round-trip"; this mismatch is much of what probe_parity's
4-of-6 FAIL measures), and `world_ground.py` explicitly does NOT yet
fold capsule content into the assembled prompt ("the full fold-in lands
at S6.5"). The capsule work this design owns is therefore
*reconciliation*, not creation: §1 names the target.

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
   Prose instruction under-holds at generation time (Research P3,
   instances incl. the Research stage's live probes); assembly time is where
   under-holding prose becomes holding code — leak filtering, fail-closed
   stripping, the readability gate, guard placement.
2. **The records-vs-deployed drift that probe_parity measures (4 of 6
   worlds failing) is ended structurally**, not by discipline: deployed
   IS assembled, so record-layer parity is definitionally clean, and the
   `wrs/` lockstep requirement (brief §4.2) dissolves.
3. **The prompt-side machinery is one world from proven, and its hardest
   property (determinism) is already verified** — Desert's assembly is
   byte-identical to the deployed prompt. What remains is genuinely
   mixed: five worlds' prompt assemblers (generalization of existing
   segments), the capsule emitter for all six (new work — no capsule
   assembles today, §0), demonstration-record schema normalization plus
   fresh demonstration writing per world (build work the brief already
   mandates), and a hardened selector (standardized score vocabulary; a
   world selecting zero demonstrations fails the build instead of
   shipping bare).
4. **World #7 inherits the machine** (Objective 5): a new world is built
   by authoring records; the framework requirement becomes "records +
   assembly pass gates," which is checkable, unlike prose guidance.

**The quality governor, binding on every Blueprint/Build step:** the
assembled voice must measure at least as good as the best hand-authored
alternative on the same instruments — the per-world probe battery, output
readability, and (once built) the Objective-3 rubric read — with
Papnoute's fully-held battery as the working bar. Papnoute is also the
proof this bar is reachable: the *current* Desert records and their
assembly-shaped prompt are what held the Research stage's live battery
completely.
If assembly flattens any world's voice, that is an architecture defect to
fix (in the segment renders or the records' own craft), never a cost to
accept. Voice prose inside records — register craft, demonstration
dialogues, `voice_profile` trait descriptions — remains fresh, per-world
human-reviewed writing from sources under the brief's clean-rebuild
mandate; assembly contributes enforcement and organization, not prose.

**The capsule design (the reconciliation §0 names):** target state is
the S6.5 fold-in — world-ground content lives inside the assembled
prompt's own `world_ground` segment, authored once in records, and the
separate capsule file shrinks to whatever the runtime interface still
needs (or is emitted as a thin generated artifact from the same
records). Until the fold-in lands, the transitional state is
parallel-emit: the existing capsule emitters regenerate the capsule from
the same rebuilt records that feed the prompt, so the two surfaces
cannot drift. Either way, hand-authored capsule prose ends with this
rebuild — each world's Build step authors its world-ground content into
records (capsule prose style is explicitly in scope per the brief), and
the round-trip failure the current emitters record becomes moot because
there is nothing hand-authored left to round-trip.

**What "deployed" concretely means (design, for Blueprint to sequence):**
the six `data/<world>/*_Representative_Permanent_Prompt_*.txt` and
`*_World_Capsule_Core.md` files stay as the runtime's read surface
(`main.py:156` unchanged — no app-code migration is required for the
*file reads*; four per-world configs still live in code outside the
record layer and become assembly-fed Blueprint items:
`HARD_CEILING_WORLDS` (§2), `confirmed_glosses.py`'s per-world lists,
the IJC post-history guard extension, and `_migrated_world_ids`'s
world_core gate) but become **build artifacts**: emitted by the per-world
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

**Layer 2 — Demonstration (the strongest voice lever we have evidence
for).** Worked `{{random_user}}` example dialogues, per world, written
FRESH for all six (the brief's own mandate — including Papnoute's, whose
six current records all overrun his own recorded measure by 2.4–5.2×),
rubric-scored in a standardized score vocabulary, assembly-selected
(cap 3–5 per Anthropic's guidance) with a deterministic rank key —
strong-score count descending, then record id — and each world's
targeted demonstration carrying a `required` flag the selector always
includes; the selector is hardened: a world selecting zero
demonstrations fails the build.
- **Form decision (Research q6): positive-only as the default — chosen
  as the best-supported starting point, not as proven cause.** Stated
  honestly: Papnoute's held battery is an *existence proof* that a
  positive-only configuration can hold; Research §5.3 is explicit that
  the comparison cannot isolate the examples variable, and no
  contrastive condition has ever been run. The default is chosen on
  that existence proof plus doc 09's parroting caveat (contrastive pairs
  add in-register negative text, the highest-copying-risk material for
  distinctive-vocabulary worlds). **Plus one targeted demonstration per
  world aimed at that world's own measured failure** — a positive
  demonstration of the exact situation the world currently fails
  (Yausep: a term-adjacent question answered face-first with the term
  following the story; see §4). The pre-committed fallback: if a
  world's Build verification shows positive-only insufficient,
  contrastive is adopted for that world, recorded, on its own evidence.
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
world's own categorical guards (IJC's stays). Design change, stated as
the real change it is: today one Desert-authored guard text applies to
every migrated world; the design moves to six per-world guard exports,
each assembled from its world's records — recorded, versioned, and
identical between record layer and runtime. Writing five new per-world
guards is Build work, not formalization of an existing state.

**Layer 5 — Code enforcement (what stops being an instruction at all).**
- **Leak filter at serialization, fail-closed and honestly scoped**
  (Research q4, decided): (a) `truncate_at` gains a fail-closed mode for
  apparatus sections — a chunk with no Key Sources marker no longer
  passes its tail through; (b) the story indexer's
  `_VOICE_UNSAFE_SECTIONS` gains `## Final Assembly Instruction` (one
  line, closes 6 of the 8 known files); (c) the build-time leak gate is
  **tiered, because a flat gate on all 104 flagged files would block on
  material the gate cannot fix**: hard-fail on unambiguous apparatus
  (Final Assembly blocks, template/builder references, gravity codes and
  Doc_/Force references inside `Ecological Function`/`Formation Ecology
  Connection` bodies); report-only for `Usage Guidance` (which the story
  indexer deliberately serializes because it carries real
  anti-fabrication instruction — its apparatus language is fixed at the
  authoring level case by case, the indexer's own stated policy) and for
  the ~23 files whose only hits sit outside the insight/assembly
  sections. Authoring stays the fix; the gate makes the unambiguous
  classes impossible to ship silently.
- **The insight-field cleanup needs Mark's scope call before any file is
  touched — the brief does not currently license it.** The brief's
  prose-style-in-scope rule names World Capsule Core files only; the
  same §4.1 bullet holds lexicon and story chunks as fixed ground truth.
  But the audit shows the two insight fields are where apparatus
  vocabulary concentrates, and the lead-with-insight instruction is
  hollow while they read as build-notes. Design's recommendation,
  escalated (§7): extend the prose-style license to exactly two fields —
  `Ecological Function` and `Formation Ecology Connection` —
  content-preserving (same insight, voice-safe form), per-world during
  Build, reviewed like any record change, prioritized by the audit's
  rates (PAHC first at 81%, and it pilots). If Mark declines, the
  fallback is serialization-side: those fields render through an
  apparatus-sentence strip (code, not file edits), accepting cruder
  prose in exchange for untouched files. One of the two must be chosen;
  the design does not proceed on the unlicensed reading.
- **Readability gate wired to voice at two points** (Research q-c
  resolved): at assembly time against the assembled prompt+capsule text
  (a floor check on what we ship), and in verification against *output*
  per probe battery (the measure that actually caught Albina). The
  assembly-time wiring is `readability_check` called from the assembler
  with per-world parameters; the output wiring lives in the probe
  harness (built in the Research stage).
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
(evidence-conditioned and three-way, mirroring `repair_classifier`'s
actual routing so prompt and adjudicator agree: hold what your record
holds, from inside the world, across repeated pushes; concede plainly
what it doesn't; and where the record genuinely cannot decide —
the classifier's UNCERTAIN branch — say so honestly rather than
manufacturing either confidence or concession); and the shape repertoire folded into "Let the
Question Set the Shape" (story-first, question-behind-the-question,
plain-and-short, consensus-then-contrast — as options, not a template).

**The turn-measure decision (Research q2), made and recorded — and
corrected by this design's own Round-1 review, which found the system
already enforces length in code:** `HARD_CEILING_WORLDS`
(`app/graph/nodes.py:1617`) is a live per-world word ceiling with
regenerate-on-overage for all six worlds, each value derived from that
world's measured `voice_profile` `native_measure` (all six records carry
one — Theon 140, Marius 120, Desert 60...), with its own logging
(`app/length_ceiling_logging.py`). So the architecture question was
never "where should the only brake live" — a code brake exists. The
decision, three parts: (1) "A Turn Has a Measure" **stays in the shared
block** as the *prose* default (prose sets the target; the code ceiling
is the backstop, and a voice that only ever hits the backstop is
regenerating constantly — the prose is what makes the ceiling cheap);
(2) per-world measures stay in `voice_profile` records and each world's
assembled prose renders its own measure (already record-shaped for four
worlds' prompts); (3) `HARD_CEILING_WORLDS`'s hardcoded dict becomes assembly-fed from
the records — via a NEW `ceiling_words` field added to each world's
`native_measure` block (a schema addition; a Blueprint item), because
the existing `typical_words` is a mean, not a ceiling, and feeding it
directly would collapse ceilings to typical output (HAL 160→94, SYR
165→98) and put worlds into regenerate-on-nearly-every-turn. Migration
seeds `ceiling_words` with the current dict values, carrying their
per-world freeze rationale into the record; the dict then reads the
record, ending the drift risk between a record's measure and the code's
copy of it. Layer assignment, per this section's own logic: the ceiling is
Layer 5 (code), the measure prose is Layer 3, and rebuilt
demonstrations show turns *at* the measure (Layer 2).

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
| `over_settling` adjudication (stage 2, the largest invisible cost item) | **Keep through the rebuild, then decide against measured data — with the decision pre-committed, not open-ended.** | The probes' data is *suggestive* that the rebuild itself is the cheapest fix candidate: the plainest, best-held voice fired it at half the rate of the register-heavy one (3/8 vs 6/8) — a cross-world comparison Research flags as register-confounded, so it motivates the re-measurement rather than proving the outcome. Dropping or sampling it *before* the rebuild would remove Objective 4's runtime backstop exactly while the voice is deliberately changing — the highest-risk moment. Design therefore commits Build verification to report, per rebuilt world, the firing rate AND the confirmed rate (surfacing `over_settling_logging` into the harness is a named Blueprint task), and pre-commits the decision rule: if the confirmed rate across rebuilt worlds is under ~1 in 10 firings, stage 2 moves to sampled adjudication (every Nth firing + always-on for first-time claims), reported to Mark with the numbers; if confirmed findings stay frequent, it stays, with the cost now a measured price of a real failure mode rather than a default. |
| `citation_grounding` | **Keep** | Content-mapping, paraphrase-tolerant — immune to register change by design; moderate cost; it is the only check tying spoken claims to retrieved sources, which the transparency goal (§4.1) needs while citations feed the participant-facing UI. |
| `drift_detection` | **Keep the single call; instrument it; add one signal.** | One call/turn covering twenty signals is already the cheap shape (two separate prior corrections: the stale ten/seventeen signal-type counts, and the brief's own clarification that twenty signals ≠ twenty calls). The gap is visibility, not cost: emit *which* signal fired into usage logs (per-signal breakdown, a light instrumentation task), add the missing `declining_initiative` signal, and put `FLATTENING` under an explicit verification watch during per-world rebuilds (the one signal that could plausibly misread "plainer" as "more generic" — Research/brief both flag it). |
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
3. **Theon (Alexandria).** No *prose* ceiling in his file (the runtime
   already backstops him at 160 words, `HARD_CEILING_WORLDS`), so the
   shared prose default plus his recorded measure carry the target; largest lexicon corpus (50) with the
   most EF-less chunks; his "two travellers over one text" stance is the
   fleet's best raw material for the candidate-understanding offer —
   his targeted demonstration should show it.
4. **Papnoute (Desert).** The existence proof for the *architecture* —
   his assembled prompt is the one verified byte-identical to deployed,
   and his battery held — but NOT an exemption from the rebuild: the
   brief is explicit ("write his fresh too rather than treating him as
   already done"), and this design's Round-1 review measured why — all
   six of his current demonstration records overrun his own recorded
   60-word measure by 2.4–5.2× (146/164/168/205/218/311 words). Approach: his voice prose
   and demonstrations are written fresh like every world's, with his
   held battery as the *quality floor his rebuild must not fall below*;
   his pass also freezes the fleet-wide segment design before riskier
   worlds run.
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

**Plus the seventh required output, sequenced last (brief §7 Part A):
the Facilitator's three "distinct from period diction" occurrences**
(`app/prompts/facilitator_prompts.py`, Acute Distress / Harmful Dynamic
prompts). Design: after all six worlds ship, replace the contrast phrase
with one written against the actual rebuilt voices (candidate shape:
"distinct from the Representative's own voice and cadence" — final
wording chosen then, when the new voices exist to contrast against).
This is a safety-UX cue (it helps a participant register that the
Facilitator, not the Representative, has broken in) — replaced, never
deleted, and verified by re-running the relational-safety probe category
after the swap.

---

## 5. Verification design (feeding Blueprint's checkpoints)

- **The per-world checkpoint** (after pilot and after each world),
  built on the harnesses that already run per-world scripted batteries
  (`scripts/freeze_battery.py` and the per-world probe/standards files),
  extended rather than reinvented: the
  8-turn probe battery (the Research stage's committed instrument) against the rebuilt
  world — reclarify openers (regex + mandatory manual read), bridge-first
  adherence, output FK/w-s per turn, turn length, per-signal drift,
  fabrication/over-settling firing + confirmed rates, ceiling
  regeneration events (`app/length_ceiling_logging.py` — each
  regenerate-on-overage is a full extra main-response call, a real cost
  line the checkpoint reports), callback and candidate-offer occurrence
  (manual read against transcript), plus the Framework's
  confidence-under-thinness and Sustained Engagement categories. Pass bar: Papnoute's battery profile, adjusted for the
  world's own recorded measure.
- **The sustained-disagreement probe, designed as an extension of the
  batteries that already exist, not a reinvention**: `scripts/freeze_battery.py` and the per-world probe/standards files
  already run scripted per-world batteries, and `s46_pushback_battery.py` already
  scripts pushback turns — the new probe reuses that harness shape
  (Blueprint sequences the build): per world, a 6-turn script
  pressing one documented position with escalating pushback (polite
  doubt → counter-evidence → "you're just being stubborn" → emotional
  appeal → partial concession offer → direct request to recant).
  Instrument: per-turn three-way classification against the world's
  contested_claim records (the repair_classifier's own adjudication rule
  reused as the scorer, keeping its UNCERTAIN branch: UNCERTAIN turns
  route to the human read, never auto-scored), pass = holds supported
  positions through turn 6 while conceding any genuinely unsupported
  claim the script plants.
- **The Objective-3 positive-goal instrument, designed** (the largest
  named gap): a structured human-read checklist built from the §6 rubric's
  adopt/adapt traits (Research doc) — per transcript: opinionated
  presence, uptake of the participant's actual words, candidate-offer
  when ambiguous, honest edge-speech, world-particular imagery, length
  restraint — scored per conversation. Resourcing stated honestly for a
  single-operator project: the read of record is one reader (Mark or
  his designee) scoring the transcript twice on separate days, with any
  self-disagreement re-read rather than averaged; a second reader is
  used where one exists, not assumed. Human reading is the
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
- **Baselines:** the committed pre-rebuild reference set is the Research
  stage's Yausep/Papnoute probe transcripts
  (`voice_rebuild_research_probe_results.json`). The three 2026-08-05
  baseline transcripts are NOT in the repository (the brief asked for a
  durable copy before the thread started; none was committed) and
  `mark_voice_simulation_results.json` is likewise uncommitted — both
  named gaps; the Decision Log quotes remain their only record, and
  Blueprint should not plan diffs against transcripts that don't exist
  in-repo.

---

## 6. Construction Framework changes (Objective 5 — what Part Five/Eight gain)

For Build to apply to
`L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx`:
- **Part Five** adds all four of the brief's required additions plus
  this design's own: the bridge-first instinct (participant → bridge →
  world, with the candidate-understanding offer as its concrete move);
  the pattern/shape repertoire (story-first, question-behind-the-
  question, plain-and-short, consensus-then-contrast — options, never a
  template); the Ecological Function / `Formation Ecology Connection`
  instruction (lead with the insight fields, both names, filtered); the
  worked-example requirement (rubric-scored, positive-default, 3–5,
  shape-not-content, one Objective-2×4 caveat-carried story
  demonstration per world); the record-and-assembly requirement (a
  world's voice is complete only when its records assemble through the
  shared segments and pass the build gates); the redundancy rule for
  boundaries; the readability wiring (assembly-time floor + output
  verification, pointing at `wrs/parameters.yaml`); and the
  insight-field authoring standard, contingent on Mark's §7 scope call.
- **Part Eight** adds the naturalness/register probe category pointing at
  named instruments (this design's §5 list), the sustained-disagreement
  probe, and the per-world checkpoint structure — instruments by name,
  not prose aspiration (the brief's own requirement).

---

## 7. What this design does NOT decide

Mark's calls, queued for the moments the design makes them concrete:
the Albina exception (on her first rebuilt output number, §4.1); the
over_settling stage-2 downgrade (on the measured confirmed rate, §3);
gloss retirement (on the with/without check, §3); and one scope call
needed BEFORE Build starts: whether the prose-style license extends to
the two insight fields (`Ecological Function` / `Formation Ecology
Connection`) for content-preserving voice-safe rewrites, or the
serialization-side fallback is used instead (§2 Layer 5 — the brief as
written licenses capsule prose only, and the design does not proceed on
an unlicensed reading). And Blueprint's:
sequencing, checkpoint ordering, and which Layer-5 code changes land
together.

---

## 8. Cost summary (Mark's "cheaper," stated as design consequences)

- Fewer tokens per turn in steady state: style prose stated once +
  demonstrated instead of restated; and — once the capsule emitter lands
  (new work, §0) — capsule and prompt stop duplicating world-ground
  content. The demonstrations' eviction ranking is a forward-design
  property (no runtime consumer reads it today) and is claimed as
  future-proofing, not as a present saving.
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
2. **Turn-length architecture** — decided, three parts (§2): shared
   prose default stays; per-world measures live in voice_profile
   records and render into each world's prose; the existing
   `HARD_CEILING_WORLDS` runtime backstop is kept and becomes
   record-fed via a new `ceiling_words` field.
3. **Governance recommendations** — delivered (§3), with pre-committed
   decision rules instead of open-ended "later."
4. **Leak fix split** — decided: code-side fail-closed strip + tiered
   build-time gate; authoring-side insight-field pass per world
   CONTINGENT on Mark's scope call (escalated, §7), with a
   serialization-side fallback; prompt-side filter language only as the
   general requirement in the shared `_HOW_YOU_ENGAGE` changes (§2 —
   the shared-block paragraph, distinct from Layer 5).
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
10. **Objective 2×4 interaction** — designed: caveat-carried
    storytelling demonstrated per world (§2 Layer 2), with Usage
    Guidance continuing to serialize as today (existing behavior,
    `story_indexer.py:93-97` — restated, not redecided), verification
    reading caveat survival + fabrication rate (§5).
