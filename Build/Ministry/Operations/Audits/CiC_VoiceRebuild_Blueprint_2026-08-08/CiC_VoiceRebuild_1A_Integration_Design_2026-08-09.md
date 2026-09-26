# CiC Voice Rebuild — 1A Integration Design (2026-08-09)

**Mark's question, verbatim:** "we have gone deeper in the design of 1A
that should change the entire build process… rethink the design process
and ensure our goals for 1A are deeply embedded in it. do we need to
start over or can we shape the design process to fully integrate and
improve what we have designed for 1A without compromising 1B?"

**Verdict: reshape, not restart — and the reshape is precise, not
vague.** The 1A corpus does not fight the architecture; it lands on
levers the architecture already has. What it exposes is an *ordering*
defect: 1A criteria enter the process only at checkpoint time, after
authoring, so checkpoints *discover* engagement failures instead of
*confirming* engagement work. The reshape moves 1A upstream into
authoring and keeps every 1B gate exactly where it is.

This document is a design amendment. Per the project's own discipline it
does not edit the settled Blueprint in place; it defines the revised
per-world pass and the fleet work, and it should take an adversarial
review before it governs, like every design before it.

---

## 1. Why not start over — three lines of evidence

**First: the 1A corpus itself says the foundation is right.** Its
governing sentence — "the world is already doing the scholarly work; the
Representative's craft is selection + voice + conversational judgment" —
*presupposes* deep, trustworthy, record-shaped worlds. That is exactly
what the six Phase-2 records passes built. Starting over would discard
the one layer 1A depends on most.

**Second: every element of the corpus maps onto an existing lever.** Not
one requires a mechanism the architecture lacks:

| 1A corpus element | existing lever it lands on |
|---|---|
| depth behind the voice | records + retrieval (the record holds everything; the turn selects) |
| perception before vocabulary | `voice_profile.speaking_model` — `act_sequence` IS what the world notices, `key` what it worries about, `norms` what it values |
| intent layer ("what is this question really about") | the Doc_04 gravities, already per world |
| witnesses as characters | the source registry with confidence/boundary tags |
| the palette | Layer 3 prose + Layer 2 demonstrations (where Design §2 always put engagement shapes) |
| we-voice, emic honesty | the block's How-You-Speak passage, drift signals 9/10, per-world guards |
| accessible-but-rigorous | the readability gates (assembly-time floors → now per-turn hard edge) |
| record-carried quotes/stories | the anti-fabrication absolute, *extended* — supply, never permission |

When a new design maps this cleanly onto an old architecture, the
architecture was aimed right and under-instructed — the cheapest kind of
wrong.

**Third: the process absorbed a brand-new 1A requirement live, today.**
The B2 hard edge went from nonexistent to scored in hours; it failed
Marius; diagnosis → record fix → guard fix → fleet rule (mid-band) →
pressed-register clause ran through *four checkpoints in one day*
without touching `data/`, without weakening one 1B gate, and with every
step committed. A process that metabolizes a new hard requirement that
fast does not need replacing.

**What would have had to be true for a restart:** if 1A had demanded
per-persona intimacy or biographical texture (breaking the we-voice), or
etic explanation ("historians say…") in Representative speech (breaking
emic containment), or engagement material invented at generation time
(breaking record-groundedness) — those would contradict load-bearing
walls, and rebuilding would be on the table. Every insight instead
strengthened those walls. That is the strongest evidence available that
the original architecture and the deepened 1A goal are the same project.

## 2. Where the process structurally fought 1A — the five defects the reshape fixes

1. **Fidelity-first authoring.** The per-world records pass targeted each
   world's *measured* failure — and every measured failure was a fidelity
   failure, because fidelity was all that was measured. Demonstrations
   were authored to model constraint-keeping (measure, containment), not
   conversation. The circle closed on itself; engagement pooled at the
   end as "the 1A task."
2. **Gates only in prose don't gate.** "Both 1A and 1B must pass before
   Phase 2" existed as a sentence; 1B ran, 1A didn't, nothing noticed.
   (Same class as the wrong-prompt bug: unverified assumptions about
   what's loaded/what's gated.)
3. **Instrument attrition.** Objective-3 cancelled without a successor;
   bridge-first narrowed to a proxy; uptake never built; candidate-offer
   left with zero test cases. The engagement half of the checkpoint
   decayed into dangling references while the fidelity half grew teeth.
4. **The batteries are fidelity-shaped.** All direct questions, scripted,
   never re-asked, never branching — so clarify/candidate-offer,
   emergence, and vary-the-evidence are structurally untestable by them.
5. **The shared block is defensive.** Fifteen sections of don'ts, two
   constructive rules. The voice was told what not to be and left to
   guess what to reach for; today's measurements show the result — 0
   stories, 1 quote, 0 question-backs in 16 turns.

## 3. The reshaped process

### 3a. Fleet work, once (the 1A foundation — before remaining checkpoints)

- **F1. The shared block rewrite** — mission statement = Voice Design's
  closing instruction verbatim; priority order (answer the question well
  is THE job); the palette as availability ("Choose what helps. Don't
  demonstrate the repertoire."); Writing Standard prose rules; the
  we-voice sentence; the "what would people today think" pattern fix.
  Defensive sections stand.
- **F2. The Facilitator rewrite** to the Writing Standard (breaches the
  floor in 4 of 4 measured runs; the one voice in every conversation).
- **F3. Instruments** — done today: B2 hard edge, sentence discipline,
  vocab reach, first-use, evidence surfacing, facilitator report. To
  add: opening/ending-type distributions, build-on (emergence proxy),
  repetition report, first-sentence-uptake, 2 ambiguous probes per
  world, the within-world variance probe, the cross-world probe.
  **Standing Goodhart rule: diversity metrics are observational, never
  targets.**
- **F4. The read protocol** — the six-dimension grid (clear / deep /
  on-point / distinctly-this-world / transparent / conversation) +
  one-memorable-thing + emergence/surprise questions + the two-audience
  questions (newcomer, scholar). Score of record stays human.
- **F5. Runtime** — session flavor ledger (stories/quotes/figures used;
  re-use takes callback framing) and witness-variety in retrieval's
  served set.

### 3b. The per-world pass, v2 (what changes in authoring — incremental "1A pass," far smaller than a Phase-2 pass)

The Phase-2 pass structure stands (records → staging assembly → gates →
checkpoint → read → swap). Its **authoring checklist gains 1A items**,
so checkpoints confirm rather than discover:

1. `key_line` authored per story/source record where the source
   genuinely yields one — sourced, R-reviewed, never invented. (Schema
   addition; the `ceiling_words` migration is the exact precedent.)
2. Witness/signature tagging: each world's 3–5 most distinctive stories
   marked; themes checked for witness *variety* (can this question be
   answered from more than one witness?).
3. **Demonstration set models different palette moves** — one story-led,
   one plain-truth-led, one ending on a genuine question back — variety
   demonstrated, never described. At least one demo is the world's
   hardest conviction said plainly (accessible-rigor as worked example).
4. Capsule/world-ground verified to give the voice its "we believed X"
   landings in plain sentences (Chloe's capsule pass is the model:
   FK 14.88 → 9.95 with nothing conceded).
5. Register aimed **mid-band** (the fleet rule), never at the ceiling.

### 3c. The dual bar (how 1B is structurally uncompromised)

Nothing ships unless **both** columns are green; the right column never
loosens the left:

| 1B — scored, hard, unchanged | 1A — scored where ruled, observed elsewhere |
|---|---|
| leak gate hard-fail 0 | B2/FK 8–10 per emitted turn — HARD (ruled) |
| fabrication 0 confirmed | sentence/vocab/first-use/evidence — reported |
| sustained-disagreement bar (§5) | palette/witness/structural diversity — observed, Goodhart-guarded |
| containment, we-voice, emic gates | six-dimension grid — human, score of record |
| assembly identity, no regression vs baseline | cross-world: accessibility converges, witness diverges |

Every 1A mechanism is additive at layers that never touch ground truth
(block, guards, runtime, instruments) or is a record *addition* under
full review (key_line). Anti-fabrication is extended by the supply-side
approach, not negotiated with.

### 3d. Sequencing

1. Fleet work F1–F4 now (F5 can trail). 2. Marius closes out under the
current bar (checkpoint 4 in flight at this writing). 3. Chloe's and
Marius's completed runs become the **pre-1A arm** of the paired read.
4. Remaining four worlds checkpoint **once**, against the post-1A block,
with the v2 authoring checklist applied as a light 1A pass first.
5. World #7, whenever it comes, inherits the v2 pass whole — this
document is part of Phase 4's "what world #7 inherits."

## 4. What this changes in the governing documents

- The Blueprint's Phase-1A task is subsumed by F1–F5 (recorded here, not
  edited there; a FLAGS entry points here).
- The Design's §2 layer assignments stand; this document adds the 1A
  authoring checklist to §4's per-world approaches.
- The five decision docs of 2026-08-09 (north star, Writing Standard,
  Palette, Composition addendum, Voice Design + we-voice pin) are the
  content sources; this document is the process integration.
- Per discipline: adversarial review before this governs; Mark's
  remaining open rulings (worklist items 3, 4, 4b, 5, 6, 7, 10) are
  unchanged by it, though 3, 4 and 10 are answered in substance by F3,
  F4 and §3d if he adopts this design.
