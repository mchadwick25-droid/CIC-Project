# CiC Record-Native World Build Process — V1.0 (2026-08-01)

**What this document is:** the single end-to-end process for building a NEW
formation world, from Step-0 scope confirmation through a frozen, deployed,
live-verified Representative — with every upgrade the S6.2 record-store
migration (2026-07-26 → 2026-08-01) proved on the six existing worlds built
in from the first record, not retrofitted afterward. A new world built under
this document is **born record-native**: authored directly into the
schema-validated WRS record store under the live gates, with the deployed
prompts and chunks *generated from* the records — there is no separate
"migration pass" for a world built this way, because the migration IS the
authoring.

**What governs, in order of authority (this document does not replace any
of them — it sequences them and fills the gaps between them):**

1. `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`
   — the Construction Framework (governing since 2026-07-27; carries the
   Table Readiness Round, the Record Integrity Principle, the Source
   Registry freeze gate, and the Validation Protocol Rigor discipline).
2. `L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx`
   — the RCF (Part Three Ecology Assessment; Part Eight Validation Testing;
   Phase Eight Table Readiness Round).
3. `Ministry/Technology/CiC_World_Build_Completion_Standard_V1.0.md`
   — the freeze-requirements source of truth (the CF's own pointer target).
4. `Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md`
   — the one-document-at-a-time, review-gated build discipline.
5. `Ministry/Technology/Pass2/SESSION_CONTRACT.md`
   — the session rules (adapted here for a new-world build; see §6).
6. This document — the sequence, the record-native additions, and the
   S6.2 upgrade inventory (Appendix A).

**Vision framing note (standing, Mark):** purpose statements and any
participant-facing copy produced during a build lead with making
experiential Christian formation available; the product is the current
means, never the mission's definition. The Brand Kit QuickRef governs all
public wording.

---

## 1. The human checkpoints — exactly three, by design

This process is fully automated EXCEPT where authority genuinely cannot be
delegated. Three stops, no more:

**M1 — Representative identity (mid-build, after Doc_09).** The build
thread prepares the grounded-options artifact per the build-cycle
discipline's own escalation rule: a scored options table for ROLE (each
option grounded in the world's own methodology facts, with named
trade-offs) and for NAME (scored on ecological resonance, authenticity,
collision-with-a-real-figure risk, gender clarity, memorability), plus ONE
recommendation for each. Saved as
`World-Builds/<World>/<code>_Representative_Identity_Options.md`. The
thread STOPS and presents the table to Mark. Precedent to imitate: both
prior executions of this pattern —
`World-Builds/Alexandria-Catechetical-School/Representative/alex_Representative_Identity_Options.md`
(Mark rejected both recommendations and chose "Theon," with reasoning
recorded) and
`World-Builds/Hieronymian-Ascetic-Literary/hal_Representative_Identity_Preliminary_Decision.md`
(Mark adopted a fifth option not among the four presented — the *vidua*
Albina, with the naming-collision risk disclosed and accepted on the
record). The lesson from both: Mark's answer is frequently NOT the
recommendation — present real options with real trade-offs, record his
actual decision verbatim in the same file, and never proceed on the
recommendation alone.

**M2 — Article 29 (Living Traditions) determination (at the freeze).** A
project-lead act by Constitution Article 29 — the build thread drafts the
determination with full history and its own recommendation, carries the
status as `provisional` until Mark confirms, and lists it in the freeze
declaration's RESOLVED-AT-THE-FREEZE section for his explicit word.
(Article 31 telos review is NOT a stop: provisional by design until year
two, per Mark's standing 2026-07-31 ruling.)

**M3 — The freeze itself.** Only the project lead assigns Frozen, under
any circumstance (build-cycle discipline, unchanged). The thread completes
everything, drafts the freeze declaration, and stops with a completion
summary. Mark's "push and make final" (or equivalent) executes it.

Everything else — every document, every review round, every record, every
gate fix, every battery reprobe — the build thread decides and records
autonomously (decisions logged, never silent), per the S6.2 autonomy
addenda: full in-world autonomy, stop only at the checkpoints above and at
the world boundary.

---

## 2. Phase A — World construction (Step 0 → Doc_10)

The document sequence, unchanged from the six built worlds, run under the
one-document-at-a-time cycle (draft → adversarial review → revision →
disposition), with the review loops agentized (§5):

| Step | Document | Notes and per-step quality bars |
|---|---|---|
| 0 | `Step0_Movement_Scope_Confirmation` | Confirm the world against `CiC_Step0_Conclusion_FINAL_v2.docx`'s portfolio entry before anything else. |
| 1 | `Doc_01` World Identification, Boundaries, Orientation | Article-21 strand analysis here if the world is strand-plural (PAHC and IJC precedents: strands ride `world_core`'s body until the strands schema CO lands). |
| 2 | `Doc_02` Source Ecology | **Use the Source Registry Template from the first row** (V7.4 freeze gate) — machine-readable rows, per-row confidence/boundary-status/licensed-for/verification-note. PAHC's 73-row JSON registry is the best-practice model; it made its S2.1 fully mechanical. Every load-bearing caveat (do-not-cite flags, pending-verification lists) written as its OWN row field, not prose — S6.2 spent real effort re-deriving these. |
| 3 | `Doc_03` Lexicon Candidate List | Term front-matter per the lexicon-index discipline (Tier, AS/SC/DR/TC/RT/PV/CT tags). **NEW: run the alias-safety preflight NOW** (§3, B-2) — author aliases against Rules A/B from birth so no retrofit is ever needed. |
| 4 | `Doc_04` Gravity Discovery | Six-test assessment per gravity; Confidence/Gravity Cross-Check on every Primary; forces-connection notation per gravity. No L4 template exists for this step — the gravity-index discipline is the bar. |
| 5 | `Doc_05` Ecological Reconstruction | |
| 6 | `Doc_06` Full Lexicon Development | CT Contest Type completion audit before clearing review. |
| 7 | `Doc_07` Integrated Ecology Analysis | |
| 8 | `Doc_08` Forces Document | Six-cell matrix, three layers per force, Section 4 cross-cell connections, Section 5 forces-and-gravities synthesis, per the forces-index bar: connections must be LOOKUPABLE, not re-read-the-whole-document discoverable. |
| 9 | `Doc_09` Story Inventory (+ 09a-c as needed) | Four-tier rule (no Tier 5 / no invented narrative); the Absent Stories question answered explicitly; per-story tier justifications. |
| — | **M1 STOP — Representative identity** (§1) | |
| 10 | `Doc_10` Representative Construction Notes + Permanent Prompt | Built AFTER M1, on the decided identity. Voice, registers, demonstrations. RCF Part Three Ecology Assessment (4 domains + Thinness Mapping) produced here — it calibrates the Phase-D probes. |

**Index artifacts:** the old per-world `.xlsx` workbooks are RETIRED for
new builds. Their function (filterable indexes for tier/tag/risk-flag/
result review) is served by the record store itself plus its generated
views — S6.2's close-out audits machine-verified the old workbooks as
fully absorbed before retiring them. Do not create new workbooks.

---

## 3. Phase B — Record-store authoring (born under the live gates)

This is where a record-native build departs from the six worlds' history:
instead of finishing Phase A and later migrating, each Phase-A document is
converted into WRS records AS IT CLEARS REVIEW, under the live gates, by a
committed per-step script (the S6.2 `s62_<code>_s2X.py` pattern — write
the same scripts, named `wb_<code>_s2X.py`, each with the dense docstring
discipline: exact source doc/section cited, mechanical-vs-authored
declared, every judgment call named). Hieronymian is the proven template —
the first world authored under the live alias-safety gate, **it opened at
zero and closed at zero; no retrofit was ever needed**. That is the
standard: gates green from the first record.

The step sequence (S6.2's, now canonical):

| Step | What | S6.2-proven quality bars baked in |
|---|---|---|
| B-1 (S2.1) | Source rows from Doc_02's registry + `<code>core001` world_core | Mechanical if the registry followed the template. Registry caveats carried VERBATIM as row licenses. `language` per row (schema requires it — declare judgment calls in the docstring). Article-29 status carried provisional for M2. |
| B-1a (S2.1a) | Discovery sweep | Read every planned citation surface; row every genuine miss with real discovery data; declared non-rows with reasons; `src<CODE>search001` sweep record with saturation statement + coverage limits. |
| B-1b (S2.1b) | Relative recall + PRESS | Ten-item independent recall test (fleet range: 6/10–9/10; a clean sweep is PAHC's 9/10 + zero miss rows). PRESS question asked verbatim; namings routed to the pre-freeze re-sweep. |
| B-2 (S2.2) | Mechanical lexicon split → term records | **Born at alias_safety ZERO**: aliases parsed under the runtime's own `parse_aliases` semantics at authoring; Rule-A generics resolved at birth (gloss-route, drop, or documented `alias_generic_override_note` — the bare-Christ/Prayer class only); Rule-B collisions picked per-term. Coverage assertion: every source sentence lands in exactly one record. |
| B-3 (S2.3) | Term authoring — senses, confidence, voice, typed relations | Confidence EXTRACTED from the doc's own confidence blocks, never re-judged. Relations fully reciprocal (the gate enforces: presupposes↔presupposed-by INVERSE; tension/associated/competing/reshaping SYMMETRIC; back-edges elsewhere). Schema enums are real — see Appendix B's collision list before authoring. Confirmed-gloss entries authored INTO `wrs/glosses/confirmed_glosses.yaml` (schema-validated, term_id set at birth — no backfill debt) and flagged per-entry for Mark's one-at-a-time confirmation. |
| B-4 (S2.4) | Story + figure records | Tier justifications verbatim; composites carry their own element-to-source tables; outsider witnesses own their accounts; boundary figures declared (no-story, preserver-only, no-figure skips); FECs parked verbatim for B-5. |
| B-5 (S2.5) | Gravity + force records | Doc_04/Doc_08 reasoning carried IN FULL, not summarized; interaction matrices mirrored exactly including no-relationship pairs; FEC→gravity_links only where the chunk's own words support it — never force-fit (FLAG-029's lesson: a wording variance gets flagged upstream, not silently converted). |
| B-6 (S2.6) | Contested-claim records | Primary-gravity minimum; CT parkings absorbed; divergence partners mapped LIVE against the frozen fleet's claims (`partner_claim_id` set); non-claims declared with reasons. |
| B-7 (S2.7) | Voice record + demonstrations | Register position warranted by the world's own genre evidence (the fleet holds six distinct positions — a new world earns its own or inherits none). `native_measure` MEASURED from real generations, not designed (PAHC's designed-70w vs measured-246-272w divergence is the cautionary case). Demonstrations grep-clean against the record store. |
| B-7a (S2.7a) | Facilitation guidance onto world_core | Pairings riding LIVE partner claims with built-in cautions (ending-not-read-back both ways; contemporaries-not-stages; the handoff containment class); telos (provisional/Art-31); living_traditions (provisional for M2). |
| B-8 (S2.8) | Generated views + four parities | Chunk views GENERATED from records; render parity (0 unclassified defects); retrieval parity vs the committed production baseline (**the verdict rule:** isolation-harness reproduction is diagnosis only — the production eval against the committed baseline is the verdict; FLAG-033's lesson); prompt coverage (zero GAPs); probe parity (held-out probes, blind, two-trial — deployed-side true-positives become record-derived guard candidates, the FLAG-030/036 class). |
| B-9 (S2.9) | Change-order decisions + chunk swap | The swap makes the record store drive this world's production. Post-swap: render identity, full production eval metric-identical, baseline saved. Prompt guards added ONLY record-derived, deployment-copy-only, cold-verified (the HAL-2/IJC-2 pattern). |

**The re-proof rule (FLAG-037, fleet-level):** any prompt fix proven in an
isolated harness MUST be re-proven under the deployed runtime (RAG +
capsule dilution) before it counts. Depth-of-drilling correlates with
survival; the election-scene seam defeated two guard layers before a
targeted prompt sharpening closed it.

---

## 4. Phase C — Deployment wiring

Everything S6.2 and the go-live day proved can break, as a checklist:

1. `app/world_manifest.py` entry (world_id, name, subtitle, period, region,
   description, representative block, color chosen from rendered swatches).
2. The two hand-synced frontend points (the manifest docstring names them):
   `SpeakerName` union + `MessageBubble.tsx` `REPRESENTATIVE_NAMES`;
   `tsc --noEmit` clean.
3. Vector indices built at Docker build time (`build_indices.py`) — never
   at runtime startup (the OOM lesson).
4. **Dockerfile audit for new runtime dependencies** — the 2026-08-01
   go-live regression: a data move made `wrs/glosses/confirmed_glosses.yaml`
   a runtime dependency the image never copied, breaking every deploy until
   root-caused from the real Render build log. Any new file the app imports
   at runtime must be verified present in the image.
5. `HARD_CEILING_WORLDS` entry (`app/graph/nodes.py`) from the MEASURED
   voice profile + battery evidence, with the retry-trigger multiple;
   `cost_baseline_runner.py`'s `CEILING_WORLDS` kept in sync (the
   observability gate enforces).
6. `POST_HISTORY_GUARD` wiring for the world (`wrs/views/segments/guards.py`
   → `nodes.py`) — the layer that rides closest to generation; add
   world-conditional clauses only on battery evidence.
7. Live smoke test against the REAL deployed site after the deploy — a real
   session, a real message, citations inspected. Freeze batteries validate
   the build environment; only a live conversation validates the deploy
   (the Deep-Interview sweep's reason for existing).

---

## 5. Phase D — Validation and freeze (agents and loops required)

**LEAN VALIDATION IS THE DEFAULT (Mark's cost policy, 2026-08-01, refined
same day):** the freeze bar is content accuracy — "the right things
said" — PLUS single-representative INTERVIEW dynamics (the solo Deep
Interview is the product on limited-table footing; its own dynamics are
not optional). What is deferred is MULTI-REPRESENTATIVE table dynamics
only. Target spend: the interview class (single-digit dollars/world),
not the ~$30 full-battery class. The full V7.4 battery below remains
available ON MARK'S WORD ONLY.

**What costs nothing and is NEVER cut (the content-accuracy floor):** the
seven gates at zero; schema validation fleet-green; render parity and
prompt coverage (both free); grep-clean demonstration checks; the record
store itself — fabrication is a build-time impossibility when every chunk
and prompt is generated from validated records. This floor does the bulk
of "the right things said" before a single API dollar is spent.

**The lean probe set (single-trial, targeted, blind-graded):** ~10–14
probes, ONE trial each, fresh-context, masked, Opus-graded blind
(grading short transcripts costs cents). Not a thinned copy of the full
battery — a concentration of where the batteries actually caught things.
Content-accuracy probes: the world's naming-collision cold probe (the
FLAG-030/HAL class), the post-window/horizon press (FLAG-031), a
fabrication press aimed at the Ecology Assessment's own thinnest
evidence areas (the FLAG-036 class), and every world-specific REQUIRED
probe the build accumulated. **Interview-dynamics probes (in the freeze
bar per Mark's refinement — the solo interview is the product on
limited-table footing):** one parroting probe and one pushback probe
(the S5.6 classes), one over-settling press, one re-gloss/exact-form
check (FLAG-034's tic). Ecology-Assessment thinness calibrates weight;
clean passes in known-hard-to-detect domains stay provisional, not
clean.

**One EXTENDED live Deep Interview against the REAL deployed site**
(~$3–4 at current pricing): 6–8 genuine rounds, follow-ups written off
the actual prior answer — long enough that sustained-length dynamics get
a real test, since that is where interview dynamics actually fail
(FLAG-018's false-referent openers and FLAG-037's dilution family both
surfaced only under sustained context, never in short exchanges). Graded
on: direct-answer opening every round; genuine cross-round memory (late
rounds concretely reusing early material, not re-explaining);
substance-driven register variation; no truncation and clean
length-ceiling behavior; no re-gloss or false-referent openers; citation
grounding inspected per turn. This is also the deploy verification
(Phase C step 7) — one spend, two checks.

**What lean validation honestly gives up, declared in every freeze
package, never silent:** (1) the second independent trial — single-trial
means generation-variance issues can slip (the Chloe "who is Jesus" catch
was exactly a variance draw); the standing mitigation is the cheap live
re-probe pattern the moment any user report lands. (2) Live-pressed
MULTI-REPRESENTATIVE table dynamics ONLY (dominance, convergence,
ending-not-read-back under real cross-world pressure) — interview
dynamics are IN the bar, not given up; the B-7a pairing disciplines are
still AUTHORED in full, just not live-pressed until the table returns. A
world frozen lean is declared "content-and-interview-frozen;
table-dynamics deferred" in its freeze declaration. (3) This is a
recorded project-lead deviation from CF V7.4's own two-trial Validation
Protocol Rigor text — reconciling the Framework wording is on the
coach-thread list (Appendix C).

**The loop discipline ("loop until dry") — unchanged:** every FAIL gets
root-caused (Fable diagnosis per the routing) → fixed record-derived →
COLD-reprobed under the deployed runtime → the failed class re-run until
clean. A probe that fails and gets explained is not a probe that passed.
The lean set makes loops CHEAPER, not optional.

**The TRR under the table's limited-use status: DEFERRED by default.**
When Mark re-opens table work, the cost-capped form applies
(representatives HARD-CAPPED AT 3; sample the 2–3 sharpest B-7a pairings,
never one table per frozen world; graded on available evidence if spend
is interrupted — a declared limit, never a silent gap).

**Cost guardrails (real incidents, not hypotheticals):** API credit
exhaustion killed a TRR table mid-run once — checkpoint probe/battery
state so an interruption resumes instead of restarting; watch spend
during any generation-heavy session; note claude-sonnet-5's intro
pricing ends 2026-08-31 (costs rise ~50% after — measured figures from
before then are optimistic for later runs).

**The freeze package:** gate report + freeze declaration
(`gates/<code>_FREEZE_GATE_REPORT.md`, `<code>_FREEZE_DECLARATION.md`, the
S6.2 shape: what the freeze rests on; RESOLVED-AT-THE-FREEZE listing M2;
resolved-and-standing items; watch items; standing search limits), the
fleet sweep green (records validate, glosses validate, matrix clean, all
gates zero, selftest green, retrieval metric-identical to baseline), and
the world-boundary completion summary for M3.

---

## 6. Session rules (the contract, adapted for a new-world build)

The `SESSION_CONTRACT.md` rules apply with `BUILD_STATE`-equivalent
tracking in the world's own build ledger:

1. Read the build ledger first; resume from its resume point.
2. Re-run the previous checkpoint before new work (kind-specific meaning
   per the contract).
3. One declared step at a time, with `Touches:`.
4. **Gate-integrity rule:** never edit a gate in the session that must
   pass it.
5. Full in-world autonomy; every decision recorded; stops only at
   M1/M2/M3 and the world boundary.
6. Defects → `FLAGS.md`, never silently patched. Upstream wording problems
   are referred, not rewritten (the FLAG-029 discipline).
7. End every session deployable; partial work commits at the last green
   checkpoint.
8. Commits carry step IDs; **push only on Mark's word.**
9. Safety-regression and retrieval-regression rules as in the contract
   (any step touching the intercept chain or retrieval ends with the
   full rerun/diff against the committed baseline).

**Model routing (Mark's policy, 2026-08-01 — pinned, not per-thread
discretion):**

| Lane | Model | Scope |
|---|---|---|
| Main thread | **Sonnet** | Orchestration and ledger discipline; the mechanical Phase-B conversion scripts (B-2 split, B-3/B-4/B-5/B-6 record conversion of the cleared documents); the remaining templated documents (Doc_01, 05, 07); Phase-C wiring; running the TRR tables. The scaffold (ledger, one-step contract, checkpoints) carries the coherence — the main thread's job is discipline, not depth. |
| Review + research | **Opus** | Every adversarial review round (cross-model against BOTH other tiers — Opus reviews Sonnet's drafts and Fable's key components alike); blind battery grading; deep source research (Doc_02 support, the recall/PRESS coverage checks); the M1 identity-options research. |
| Key components | **Fable** (subagent calls) | **Lexicon discovery and development (Doc_03 + Doc_06)**; **story inventory + quote discovery and vetting (Doc_09, incl. the Absent Stories question)** — these demand the deepest, most inclusive searching and building, and discovery misses are invisible to every gate; gravity discovery (Doc_04); forces synthesis (Doc_08); voice construction (Doc_10 + B-7); **Phase-D battery-fail diagnosis loops** (shallow root-causing costs a battery re-run; a Fable diagnosis call is cheaper than the loop it prevents). |

**The brief discipline that makes the routing safe:** a Fable subagent's
brief is POINTERS, NOT SUMMARIES — the file paths and the specific
question; the subagent reads the actual World-Builds documents and records
itself. An under-briefed subagent wastes the tier; a summarized brief
launders the main thread's blind spots into the component that exists to
avoid them.

**Agents and looping (how "the current system was built," now required):**
adversarial reviews run as INDEPENDENT subagent rounds (2–3 per document;
a finding is never dismissed as a tooling artifact without independent
re-verification; fabricated-content checks are explicit — S6.2's history
includes a fabricated inverted methodology quotation caught only by
adversarial review). Battery grading runs blind in an agent that never saw
the build. Gates loop fix-until-green. The review-agent model-routing
commitment (which lapsed twice in one historical build) is checked per
round: graders and reviewers on the tier the task calls for per the
standing model-allocation policy (Sonnet live/compiling, Opus
research/design-evaluation, Fable comprehensive passes).

---

## Appendix A — The S6.2 upgrade inventory (what this document captures)

Every mechanism the migration proved, where it lives, and what it caught —
the ledger of what a new build inherits on day one:

| Mechanism | Lives at | Proved by |
|---|---|---|
| WRS record store (13 record types, JSON-Schema validated) | `cic-poc/backend/wrs/{schema,records}/` | 739/739 fleet-wide; one source of truth, drift impossible by construction |
| Gate battery (7 gates, backfill profile) + selftest | `wrs/gates/{core,run_gates,fixtures}.py` | Zero-violation floor on every frozen world |
| Alias-safety Rules A/B/C + override mechanism | `gate_alias_safety` in `wrs/gates/core.py` | Caught live production over-broad highlighting (Syriac's bare `truth`/`mystery`/`symbol`); HAL born clean under it |
| Confirmed-gloss schema + YAML + term_id + runtime parity | `wrs/{schema/confirmed_gloss.schema.json,glosses/confirmed_glosses.yaml}`, `app/prompts/confirmed_glosses.py` | 88/88 validated; byte-identical runtime guidance; Rule C zero cross-namespace violations fleet-wide |
| Freeze battery V7.4 (two-trial, held-out, fresh-context, blind) | Per-world under `Ministry/Technology/Pass2/batteries/` | Every S6.2 freeze; first ran at S5.6 where it correctly WITHHELD a freeze (FLAG-018) |
| Table Readiness Round (cost-capped, cap-3) | Per-world under `Ministry/Technology/Pass2/trr/` | Cross-world disciplines pressed live; the policy caps per `decisions/S6.2_M_table_cap_and_trr_cost.md` |
| HARD_CEILING_WORLDS + retry + observability | `app/graph/nodes.py`, `app/length_ceiling_logging.py` | PAHC's designed-vs-measured divergence; per-world measured entries |
| POST_HISTORY_GUARD (closest-to-generation layer) | `wrs/views/segments/guards.py` → `nodes.py` | FLAG-018 layer 3; FLAG-037's dilution family |
| Record-derived prompt guards, cold-verified | Per-world deployment prompts | FLAG-030 (4/4), FLAG-031 (6/6), FLAG-036 (10/10), FLAG-037 (8/8) |
| Four-parity release gate (render/retrieval/coverage/probe) | `wrs/views/s62_*_{render,retrieval,prompt_coverage,probe}_parity.py` patterns | Real catches at nearly every world's B-8 |
| The production-eval verdict rule | Baselines under `cic-poc/backend/baselines/` | FLAG-033 resolved by measurement, not argument |
| The re-proof-under-deployment rule | — (a discipline, §3) | FLAG-037's fleet lesson |
| Citation-grounding filter | `filter_grounded_citations()` in `app/graph/nodes.py` | The 2026-08-01 live sweep's Syriac finding; verified on real transcripts |
| Session contract + FLAGS + checkpoint ledger | `Ministry/Technology/Pass2/` | The whole of S6.2's traceability |
| Gloss scope clause + re-gloss guards | `confirmed_glosses.py` guidance + world prompts | FLAG-034's two-layer fix (PAHC-4/4b, IJC-4) |
| Article-29 at-freeze confirmation; Article-31 year-two ruling | Freeze declarations; `Ministry/Technology/Pass2/decisions/` | All six worlds carry settled Article-29 states |

## Appendix B — Schema-enum collisions to author around (S6.2's caught list)

Authoring hits these enums; declare, don't invent: `grounding_criterion`
is enum low/standard/high (free text → `conceptual_distance_note`);
`field_relations` has no `reinforcing` type (→ mechanism-behind +
associated-with mirror); `evidentiary_weight` has no `qualified`;
`trait_rubric` entries require `trait` with intensities as array;
`avoid_traits` are plain strings; gravity `interaction` is a typed edge
array (reinforcing/competing/reshaping); force connections need
reciprocity back-edges; source records require `language`.

## Appendix C — Known gaps this document does NOT fix (flagged for the coach thread / Mark)

1. **The six build skills live OUTSIDE the repo** (the Claude app's local
   skills cache), unversioned, and none of them mention any Appendix-A
   mechanism. Recommendation: commit versioned copies into the repo and
   add a one-line pointer in each to this document. Coach-thread edit
   authority — not done here.
2. **CF V7.4 / RCF V3.2 narrow edits** — the docx frameworks absorbed the
   Table Readiness Round and Validation Protocol Rigor at S6.1 but still
   say nothing of the record store, the alias gate, or the gloss schema.
   Framework wording is Mark's, one edit at a time — a proposed edit list
   is a coach-thread task, not this document's.
3. **The Cappadocian orphan** — a substantially built world (Doc_01–Doc_10,
   Representative Eumathios, deployment package) sits on the unmerged
   branch `origin/CiC-Fable-Cappadocian`, invisible from main. If world
   building ever resumes, recover and audit it under this process before
   building anything new; its Phase A may be largely done.
