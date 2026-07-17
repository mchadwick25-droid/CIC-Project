# CiC Backend / Runtime — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning —
including the heart reasoning, not just the engineering one — and the specific next
action. A decision that only lives in conversation history is a decision that gets
re-litigated by accident later.

**Scope:** `cic-poc`'s backend runtime — the Facilitator graph, the drift monitor, the
classifiers, prompt assembly, retrieval. Work happens on exploration branches; merge
decisions belong to the front-end thread with the pilot schedule in view.

**Why this log starts on 2026-07-16:** backend work has been happening on
`claude/cic-poc-backend-facilitator-upgrade` without a log of its own — decisions were
being recorded in the front-end log or in commit messages only. The first entry below
is a defect fix serious enough that its reasoning should not live in a commit message.

---

## 2026-07-16 — FIXED (exploration branch): the FABRICATION drift signal was blind, and it acted

**Branch:** `claude/drift-monitor-fabrication-eyes`, cut from
`claude/cic-poc-backend-facilitator-upgrade`. Commit `2a102ee`. **Nothing merges before
Prototype Testing 1 without Mark's call.**

**Origin:** found during Guided Questions calibration (see
`CiC_Guided_Questions_Calibration_Results_V0_1.md` §3 and
`CiC_Guided_Questions_Decision_Log.md`, 2026-07-16), confirmed in code by the map
thread, handed here as a brief. Diagnosis arrived done; it was re-verified in code
before anything was built on it, and one part of it was corrected (below).

### The defect, verified

`nodes.py:1291` — `FACILITATOR_MONITORING_PROMPT.format(response=response_text)`. **The
monitor receives the response text and nothing else.** `facilitator_prompts.py:150`
defines FABRICATION as content *"not grounded in the permanent prompt, world capsule,
or retrieved context."*

Of the nine single-representative signals, **eight are properties of the text** —
smoothing, generating, agreeing, over_producing, temporal_bleed, flattening,
apologetics, first_person — and are judgeable from the response alone. **FABRICATION is
the only one that requires external sources, and it was the only one denied them.** It
also fires at HIGH severity, which at `nodes.py:1417` sets `requires_reroot`, which
`main.py:390` (non-streaming) and `main.py:768` (streaming, via
`pending_guidance[world_id]`) turn into correction guidance injected into that
representative's **next** turn. **It does not merely mislabel. It acts.**

### The reproduction — and what it corrected in the diagnosis

Five turns, live, single-world (Papnoute), all three questions Antony-adjacent and
answerable from `desertlex001_anachoresis`:

| Turn | Named Antony / cited Athanasius | Flag |
|---|---|---|
| T1 | **yes** | clean |
| T2 | no — bare "he" | **fabrication/high** |
| T3 | no, but *"the tradition remembers him"* | clean |
| T4 | no — bare "he" | **fabrication/high** |
| T5 | **yes** — *"Athanasius gives us Antony's own word"* | clean |

**The mechanism is attribution, not naming.** Denied sources, the monitor has exactly
one available proxy for groundedness: whether the text *sounds* attributed. Cite, and
it reads as grounded. Narrate, and it reads as invented. Neither has anything to do
with whether the content is true.

**Two corrections to the record, both against the brief and against my own earlier
report:**
1. **"Fires 2× high-severity" was wrong.** It fires **once**; `facilitator_reroots`
   (`nodes.py:1437`) appends a second copy of the same signal with `Correction:` added.
   Verified: the two descriptions are byte-identical up to the appended correction. One
   detection, recorded twice. The Guided Questions results doc has been corrected.
2. **The predicted harm — that correction steers toward genericness, i.e. toward
   SMOOTHING and FLATTENING — was NOT observed.** What was observed at T3 was the
   representative adding attribution hedging (*"the tradition remembers him,"* *"he is
   remembered as"*) after T2's flag. That is arguably *more* calibrated, not less. **The
   "anti-drift guard induces drift" claim is not supported by this reproduction and is
   not being carried forward as established.** The real harm is different, and worse.

### The real harm: the false negative

**This is the finding that justified the change, and it was not in the brief.**

A monitor without sources can detect *unattributed specificity*. It cannot detect
*misattributed specificity* — and misattribution is precisely the one fabrication this
project has actually recorded (the leaking-jug saying, which belongs to Abba Moses,
attributed in live testing to Macarius).

Tested directly against stage 1 as production calls it today. Input: the jug story,
misattributed to Macarius, carrying an attribution phrase. **Stage 1's verdict:**

> **NO_DRIFT** — *"The response demonstrates genuine formation… The citation of Abba
> Macarius is not decorative but carries the weight of the community's actual moral
> pedagogy."*

**It does not merely miss the project's one recorded failure mode. It commends it.**

So the guard is inverted: **it penalizes truth narrated plainly and clears falsehood
that is well dressed.** Any fabrication that remembers to say "Athanasius tells us"
passes. That is not a noise problem; it is the signal pointing the wrong way.

### The fix

Two-stage, following the codebase's own classify-then-route idiom (the same shape as
the frame-breaker and relational-safety classifiers):

- **Stage 1** — unchanged, every turn, cheap, text-only. Flags *candidates*.
- **Stage 2** (`_adjudicate_fabrication`) — fires **only** on fabrication candidates
  with a `world_id`. Loads that world's capsule via `settings.get_world_config()` and
  re-retrieves lexicon + story context against the response text, then adjudicates
  against `FABRICATION_ADJUDICATION_PROMPT`. **GROUNDED** drops the signal;
  **FABRICATED** keeps it.

**It fails toward keeping the signal, deliberately.** Capsule unreadable, retrievers
erroring, or an unparseable verdict all return `None`, and stage 1's finding stands. A
guard that silently disappears on error is worse than a noisy one — the noise is at
least visible.

**Cost:** near zero. Most turns produce no fabrication candidate and never reach stage
2. The one signal that matters became the only one informed.

**Explicitly not done:** loosening the FABRICATION definition to reduce noise. The
noise is real, but the signal guards the project's one recorded live failure. **Give it
eyes; don't quiet it.** The adjudication prompt is written to that instruction — it
tells the second pass that attribution language is a style, not evidence, and that
thin material is not automatically fabrication, and to answer GROUNDED when genuinely
uncertain, because a false FABRICATION finding corrects a representative away from its
own true material.

### Verification

| Test | Result |
|---|---|
| Exact text that fired `fabrication/high` twice pre-fix | **`None` — cleared**; adjudicator returns GROUNDED |
| Misattributed Macarius jug (**the real failure mode**) | **FABRICATED** — caught, where stage 1 alone says NO_DRIFT |
| Invented named scene ("Abba Theodoros of Kellia" + the forty-year lamp) | **FABRICATED** |
| Attested material narrated plainly, no attribution phrase | **GROUNDED** |
| Five-turn live repro, post-fix | clean at T2/T4 where it previously flagged |
| `py_compile`, imports, stage-2 gating assertions | clean |

**Known limits, named rather than buried.** Stage 2 sees the capsule and freshly
retrieved chunks — **not the permanent prompt**, and not the chunks this turn actually
used (it re-retrieves against the response rather than threading the turn's own
retrieval through). So it adjudicates against *what evidence exists for this world*,
not *what evidence this answer drew on*. That is arguably the better question for
groundedness, but it is a different question and should be said out loud. **n is small**
— three adversarial cases and two five-turn runs, one model, one day. This needs a real
probe battery before it is trusted at production scale.

**Heart reasoning:** the cardinal sin, in this project's own governance, is *"a real
author cited for something they did not say."* The system's guard against it was
structurally incapable of seeing it, and was instead punishing representatives for
telling their own worlds' true stories in their own voice. Of everything this fix
touches, that is what mattered: a Representative narrating attested material plainly is
doing exactly what it was built to do, and it was being corrected for it — while the
one thing it must never do would have sailed through.

**Next action:** Mark's call on merge. Recommendation: this belongs in before the pilot
— a guard that cries wolf on the Desert world's founding story and commends its own
recorded failure mode will either be ignored or will suppress good material, and both
are worse than the current noise suggests. But it needs a probe battery first, and that
costs live API calls.

---

## 2026-07-16 — CHECKED, NOT A LIVE BUG: the `world_id`-less gate at `main.py:744` is a latent trap with a named future occupant

**The concern (from the brief):** `main.py:744` gates the multi-world checks on
`if signal.world_id and signal.severity in ("medium", "high")` — a signal without a
`world_id` would be recorded in `drift_signals` but **silently never corrected**.

**Audited every `DriftSignal` construction in `nodes.py`** (7 sites). All seven set
`world_id`. The five that reach this gate — dominance, convergence,
cross_world_vocabulary, length_ceiling, question_stacking — take it from a loop
variable over `world_ids` or from a `round_turns` dict key, and **cannot be `None`
today**. The dataclass default is `world_id: Optional[str] = None`, documented as
"None for the original single-representative signals… which apply to whoever spoke
last" — and those single-rep signals don't pass through this gate. **Not a live bug.**

**But it is a trap, and Governance §10 already names its occupant.** The gate fails
*silently*: a signal with no `world_id` is recorded and never acted on, with nothing
logged. §10's **mode-dominance drift** is, by its own definition, a table-level signal
about *the table's collective register* rather than any single voice — *"no existing
signal catches this, because no existing signal reads the participant's wound against
the table's register"* — i.e. exactly the signal that would legitimately carry no
`world_id`. **If mode-dominance is ever implemented into that loop, it will be recorded
and silently dropped**, and the failure will look like the feature simply not working.

**Not fixed here** — changing the gate without a signal that needs it is speculative,
and this branch is scoped to the FABRICATION defect. **Logged so it is found by whoever
implements mode-dominance**, rather than discovered as a mystery.

---

## 2026-07-16 — FLAGGED FOR GOVERNANCE, NOT EDITED: two gaps between Facilitator Governance V3.6 and the implementation

Per the brief's item 4, and per this project's standing rule that governing documents
are not edited unilaterally. **Both are flags for Mark, not changes.**

**1. The cardinal sin is specified; its detection was not possible.** Governance §9
names the cardinal sin as *"a fabricated citation — a specific claim dressed in false
scholarly grounding, an invented source, **a real author cited for something they did
not say**"*, and §13 makes the Facilitator *"protective"* of exactly this in Mode One:
*"You ensure that Representatives do not fabricate citations."* **The implementation
could not do this** — as proven above, stage 1 clears a misattributed real author with
a commendation. After this fix it can, **partially**: stage 2 checks against the
capsule and retrieved chunks, not the full corpus and not the permanent prompt.

**§15 (Known Limits) does not name this.** It names self-narration detection under
adversarial pressure, cross-world contamination detection, convergence-drift detection,
coherence across three-plus Representatives, and the decontextualization trigger's
judgment-call nature. **The limit that the groundedness guard cannot see the ground is
absent** — and it was the most consequential of them. Whatever Mark decides about the
fix, **§15 should name what fabrication detection can and cannot verify**, because a
governance document that specifies a duty the runtime cannot perform is the kind of
gap this project's own discipline exists to prevent.

**2. The signal sets have drifted apart.** Governance §10 names **seven**
single-Representative signals: Smoothing, Generating, Agreeing, Over-producing,
Temporal bleed, Flattening, Self-narration. `FACILITATOR_MONITORING_PROMPT` implements
**nine**: smoothing, generating, agreeing, over_producing, temporal_bleed, flattening,
**fabrication, apologetics, first_person** — and does **not** implement self-narration
(deliberately and correctly: governance itself routes self-narration to the
frame-breaker classifier rather than the monitor).

So the code carries three signals governance never names, and governance names one the
monitor doesn't implement. **Neither is necessarily wrong** — first_person is plausibly
Article 28's anti-fabrication discipline expressed as a monitor signal, and
fabrication is the cardinal sin itself. But the project describes "the twelve
fidelity-drift signals" as a fixed set across many documents, and **the number is no
longer accurate against the code**. This is precisely the hand-synced-list drift the
`world_manifest.py` refactor eliminated once already, in a place where it matters more.

**Not this thread's to resolve.** Flagged with the specific mismatch so the correction
is a decision rather than a discovery.

---
