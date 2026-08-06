# Church in Conversation: Representative Voice Rebuild — Design & Build Brief

## 1. Mission — read this first, it governs everything below

A Representative exists to let a real person encounter a real historical
Christian tradition — genuinely, not as a lecture in period costume. Per the
Vision document's own Article 6 test, a real encounter keeps the Representative
itself, protects the participant's authorship, presents the world honestly
with its tensions held, and leaves interpretation to the participant. Mark's
own framing of this rebuild, verbatim: the Representative "has to be rebuilt
(not the name and role) but who they are to have a conversation that engages,
is natural and not distracting and gives truely insightful and accurate
answers." A voice a participant has to work to get into is quietly failing
"protect the participant's authorship" — it's making *them* cross into the
world, when a Representative's whole premise is that it crosses toward them.

## 2. What this rebuild is for

Mark named the actual architectural inversion needed: this system was built
**sources → voice → conversation** — the vetted record dictates the register,
and a participant has to enter through that register to be understood. It
needs to run **participant → bridge → world**, circularly: start from what a
person standing there actually needs to feel oriented and drawn in, reach into
the real record to answer them, and let the world's own flavor arrive as the
conversation deepens rather than as the price of entry.

**One thing does not move, stated by Mark twice, in these exact terms: no
fabrication. This is "our world grounding."** Register, structure, and
entry-point can all change. What a Representative is licensed to claim never
does.

## 3. What governs this — read directly, verify against it, don't design in a vacuum

- `Ministry/Communication/Vision, Mission, Convictions, and Foundational
  Commitments V1.1.docx` — every product decision below answers to it.
  Participant Agency, Trustworthy Transparency, Encounter Over Persuasion,
  Technology Serves Encounter Never Replaces It.
- `Ministry/Features/Front-End-Integration-Strategy/Decision-Log.md`, entry
  dated **2026-08-05 — "Live conversation test run"** — the actual live
  transcripts, real per-call cost data, and the two adjacent defects (§4)
  this brief carves out of scope. Read this before assuming you know the
  starting state; it's the direct evidentiary basis for everything in §5.
- `L3C-Representative-Methodology/
  CiC_L3C_Representative_Construction_Framework_V3.2.docx` — the current
  Construction Framework, Part Five (Voice Construction) and Part Eight (the
  validation probe battery). Read Part Five closely before writing anything:
  it already states the destination — "This does not mean archaic English or
  artificial formality... language should feel natural rather than
  performed" — and this rebuild is as much about closing the gap between that
  stated principle and what six actual builds produced as it is about the
  Representative prompts themselves.
- `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`
  — the discipline this project holds every design claim to. Before treating
  any finding in §5 below as settled, verify it against the file/line it
  cites — this brief was assembled by directly reading the code and prompt
  files named, not by summarizing a summary, but check it anyway.

## 4. What NOT to rebuild — this is a voice rebuild, not a restart

- **The world/source layer's content** — lexicon chunks, story chunks,
  source registries. Confirmed good by Mark directly. Prose *style* inside
  the World Capsule Core files is explicitly in scope (§7); their
  *content/sourcing* is not.
- **The no-fabrication apparatus** — the near-verbatim shared "museum guide"
  fabrication-guard block (present in Yausep's, Theon's, and Marius's
  permanent prompts) and Papnoute's own differently-worded version of the
  same rule. Do not edit, shorten, or soften this under any framing.
- **The near-verbatim "witness not recruitment" block** — present, reworded
  per world, in Chloe's, Albina's, Yausep's, Theon's, and Marius's files
  (Marius's own file names it "SECTION 6 — WITNESS-NOT-RECRUITMENT"). Not
  fabrication-related, but a separate, deliberate, already-shared module —
  leave its content alone; it's fine if register work touches its sentence
  rhythm the same way it touches surrounding prose.
- **Historical identity, era, and vocabulary content** in every permanent
  prompt — who each Representative is, what span they speak from, their
  world's real terms. This rebuild changes how something is said and what
  gets reached for, never the facts being spoken.
- **The governance/monitoring layer.** Confirmed directly, this session, by
  reading the actual prompts: `over_settling` (`app/prompts/
  facilitator_prompts.py`, its own screen prompt states "tone is not a
  limit... the question is whether the specific qualification is present,
  not whether the voice sounds modest"), `citation_grounding`
  (`app/graph/nodes.py`, explicitly tolerant of paraphrase, purely
  content-mapping), and `drift_detection`'s ten signals are all content- or
  posture-based, not register-based. One exception worth empirical
  attention, not redesign: `FLATTENING` ("sounds like educated generic
  Christian voice with historical accent") is a holistic LLM judgment that
  could plausibly read "plainer" as "more generic" — watch it in verification
  (§8), don't design around a hypothetical.
- **Confirmed inline glosses** (`app/prompts/confirmed_glosses.py`) — a
  small per-world whitelist requiring an exact fixed string for specific
  terms, checked deterministically. Explicitly out of scope by its own
  docstring: "the only place... an exact form is asked... everything else
  about how you speak is unchanged."
- **Retrieval ordering.** Tier-based sorting of retrieved documents before
  they reach the model is a real, confirmed-cheap follow-up
  (`doc.metadata["tier"]` already exists per chunk in `app/rag/
  indexer.py:32`; the hook point is a sort key before the per-document loop
  in `app/rag/retriever.py:192`, `get_context_for_response`) — Mark's own
  framing was "we could still add some more codes to prioritize things," a
  minor addendum. Note it, don't build it, unless the blueprint stage finds
  a compelling reason it has to move together with the voice work.
- **Two adjacent, already-diagnosed defects, deliberately not bundled here** —
  log them for Mark's own separate triage rather than fixing them as part of
  this thread:
  1. `CitationModal.tsx` renders a citation's `key_sources` field in full,
     unfiltered, to participants — and some `key_sources` values carry
     build-process language straight from source chunk files (a real example
     surfaced this session: "...is itself the term's own live contest. See
     CT Contest Type below" — a dangling reference to an internal document
     no participant can see).
  2. `over_settling_adjudication` fired on 10 of 12 turns in this session's
     live test — not a rare safety net in practice. Worth watching (§8)
     since a "begin with substance, avoid generic hedging" voice
     instruction pushes toward more unhedged claims, which is exactly what
     this check screens for — but fixing the check itself is out of scope
     here.

## 5. The diagnosis — what's actually broken, and where

Four converging findings, verified directly against the code and prompt
files, not inferred:

**A. The archaic/formal register is 100% sourced from the six per-world
permanent prompt files — not the shared engagement instructions.**
`app/prompts/representative_prompts.py`'s `_HOW_YOU_ENGAGE` block explicitly
defers register to each world's own file: "Your own permanent formation...
specifies how your world characteristically builds an answer... That is your
register." Confirmed by direct comparative reading of all six files:
- **Papnoute** (desert-monasticism) — richest register instruction,
  deliberate archaic parataxis ("sentences stand next to each other, do not
  lean on each other"), explicitly modeled *against* a "scholar's sentence"
  as the wrong example. The only file with worked example dialogues.
- **Chloe** (PAHC) — already the plainest of the six, self-described as
  "closer to the terse teaching handed to catechumens than to the crafted
  urgency of a bishop." Thin register instruction, no worked examples.
- **Mar Yausep** (Syriac) — similar terse rule to Papnoute's, thinner, more
  archaic-leaning surrounding vocabulary. No worked examples.
- **Albina** (Hieronymian) — the one deliberate exception: prescribes
  periodic/hypotactic Latin-scholar sentence rhythm as her genuine,
  formation-accurate voice, the opposite of Papnoute's parataxis, argued with
  comparable craft. No worked examples.
- **Theon** (Alexandria) — thin register instruction, lyrical/devotional
  diction. No worked examples.
- **Marius** (Imperial-Juridical) — richest of the five non-Papnoute files,
  the only one with explicit section headers, register and reasoning-mode
  genuinely entangled in its own "SECTION 3 — VOICE AND REASONING MODE." No
  worked examples.

**B. The raw material for insight and bridging already reaches the model —
nothing tells it to use it.** Every lexicon/story chunk carries `Tier`
(human-curated centrality), `Ecological Function` ("why this matters, what
it connects to" — pre-written insight material), and `Distortion Risk`
(structured as Modern Hearing vs. World Hearing — literally pre-written
bridge-from-participant's-assumption material). Confirmed directly via
`app/rag/sections.py` and `app/rag/retriever.py:get_context_for_response`:
only `Key Sources` is stripped before generation (`truncate_at(body,
KEY_SOURCES_MARKERS)`); Ecological Function and Distortion Risk reach the
model's context on every turn. Nothing in `_HOW_YOU_ENGAGE` or any permanent
prompt instructs the model to lead with this material, which is a large part
of why answers currently "pick random things" rather than building from what's
most sure toward what's genuinely distinctive toward what's honestly
unsettled.

**C. Prose-only guards have already, demonstrably, failed to hold this exact
line — live, in this session's own test.** `_HOW_YOU_ENGAGE` already carries
an explicit guard (labeled FLAG-018 in its own comment, `representative_
prompts.py:174-181`) against unprompted term-reclarification, and Chloe's own
permanent prompt independently carries a second, per-world version of the same
rule. Both were live in this session's own test conversations — and the exact
behavior they guard against still surfaced, twice, back-to-back, in two of
three worlds tested ("When I said 'ekklesia' a moment ago..." then "When I
said 'episkopos' a moment ago..." in consecutive Chloe turns; the equivalent
in Mar Yausep). Two layers of prose instruction, same direction, already
insufficient — that much is settled.

**What is NOT settled: whether worked examples are the fix, and this brief
should not tell Fable they are.** A same-day ad hoc pilot (not a production
change — `cic-poc/backend/scripts/mark_voice_simulation.py`, results not
committed) tested a bridge-first instruction plus positive worked-example
dialogues against Chloe specifically, live through the real backend. The
FLAG-018 behavior still surfaced, on the same turn, with both additions
present. That is one data point, not a verdict — it shows positive-only
worked examples aren't sufficient by themselves for this specific guard, in
this one instance. It does not show worked examples are the wrong tool
generally: Papnoute is the one world that already has worked examples and
has never been probed for this exact failure mode. Whether Papnoute is clean
on it is the single cheapest next check that would actually discriminate
between "worked examples work, mine just weren't built right" and "worked
examples aren't enough alone for this guard, project-wide" — and it hasn't
been run. **This is Fable's Research-stage question to resolve, not this
brief's to answer in advance.** Do not carry a specific fix (e.g., a
contrastive/negative example paired with the positive one) into the Design
stage as a foregone conclusion — treat it as one candidate the Research
stage should test, alongside the Papnoute check, before Design commits to an
approach.

**D. The three baseline transcripts this session captured do NOT actually
reproduce "over formal / distracting" — and they're the three plainest worlds
already.** Full transcripts, cost data, and this exact finding are in the
Decision Log entry named in §3. Read cold, all three (Papnoute, Chloe, Mar
Yausep) handled real pushback substantively and didn't read as generic or
archaic in a way that visibly matches the complaint. This matters concretely
for how this thread verifies its own work (§8): re-testing only these three
worlds and finding they "still read fine" proves nothing, since they weren't
shown to be broken in the first place. **The real acceptance evidence has to
come from Albina and Marius** — the two worlds never live-tested this
session, and, per the comparative read in (A), the two with the most to lose
from a careless rewrite (Albina's deliberate periodic rhythm; Marius's
entangled register-and-reasoning-mode).

## 6. The concrete objectives

1. Every Representative opens from where the participant actually stands —
   a recognizable want, fear, or doubt — before reaching for the world's own
   vocabulary or imagery. Period flavor arrives once the bridge is built, not
   as the price of admission.
2. A substantive answer draws on what's genuinely insightful (Ecological
   Function, Distortion Risk) rather than whatever's topically nearest, and,
   when the question calls for it, is built in a defensible order: most sure
   first, genuinely distinctive second, honestly unsettled last and lightest
   — as **one option among a real repertoire of answer shapes**, not a new
   template replacing the old one. (Mark's own words: "we need to have
   several patterns so it doesn't just repeat the same thin process.")
3. Sentences read as plain, real, everyday spoken English — not costume
   diction — while keeping each world's genuine imagery, vocabulary, and
   actual distinctiveness as seasoning, not performance. Albina's periodic
   rhythm is the one deliberate, formation-accurate exception, kept
   substantively.
4. No fabrication rule moves, anywhere, under any framing.
5. The Construction Framework itself changes so that world #7 doesn't
   reintroduce this exact gap — "self-sufficient... as we have done all
   along," Mark's own words. This is not optional scope; it's the actual
   point of doing this on a dedicated thread instead of hand-patching six
   files.

## 7. The shape of the output — two parts, both required

### Part A — rebuild the six Representative voices

- **Pilot first, isolated.** Rewrite the shared `_HOW_YOU_ENGAGE` block
  (bridge-first entry; explicit instruction to lead with Ecological
  Function/Distortion Risk material, worded as an *extension* of the
  existing FLAG-018 guard rather than a parallel instruction competing with
  it; the shape repertoire from objective 2 folded into the existing "Let
  the Question Set the Shape, Not a Habit" section as one option among
  several — story-first, question-behind-the-question, plain-and-short,
  consensus-then-contrast). Pilot it against Chloe alone, verify in
  isolation (§8) before touching any other file.
- **Per-world passes, risk-ordered — Albina → Marius → Theon → Papnoute →
  Chloe → Yausep.** Not build order, not alphabetical: highest-register-shift
  and least-validated worlds first. Each pass covers **both** that world's
  permanent prompt **and** its World Capsule Core file (Mark confirmed:
  capsule content/sourcing frozen, prose style in scope — the capsule sits
  in the cached prefix at equal weight to the permanent prompt on every
  turn, in the same elevated register, so a register fix that stops at the
  permanent prompt is capped by its own neighbor).
  - Full diction/rhythm audit of both files — the elevated register runs
    through more than the paragraph explicitly labeled "how you speak"
    (confirmed by direct reading: identity, era, and vocabulary paragraphs
    carry the same stylization). Content, fabrication-guard, and
    witness-not-recruitment blocks untouched.
  - Reconcile the new shape repertoire against that world's *own* existing
    reasoning-mode paragraph — Marius's precedent-first chancery mode,
    Yausep's stage-by-stage demonstration, Theon's surface-then-depth
    unfolding, etc. Each may host the repertoire cleanly or need explicit
    adjustment; check per file, don't assume uniformity.
  - Add worked `{{random_user}}`-style example dialogues to the five files
    that lack them, in the *same* pass as the register edit — not a separate
    polish layer. **The exact form these examples take (positive-only, or
    paired with a contrastive/negative demonstration) is a Design-stage
    decision, made only after the Research stage resolves the open question
    in finding (C) — not prescribed here.**
  - Albina keeps her periodic/hypotactic rhythm substantively — genuine
    formation-accurate craft — but gets the same plain-vs-performed
    naturalness audit on surrounding diction as the other five.
- **Facilitator's three "distinct from period diction" occurrences**
  (`app/prompts/facilitator_prompts.py`, Acute Distress/Harmful Dynamic
  prompts, roughly lines 429/449/485) — fixed last, once all six permanent
  prompts are settled, so the replacement contrast phrase is accurate to
  the actual new voice rather than guessed early. This is a real safety-UX
  cue (helps a participant register mid-conversation that the Facilitator,
  not the Representative, has broken in) — don't just delete it, replace it
  with something still true.

### Part B — revise the Construction Framework itself

Update `L3C-Representative-Methodology/
CiC_L3C_Representative_Construction_Framework_V3.2.docx`:
- **Part Five (Voice Construction)** — the framework already states the
  right destination ("not archaic English or artificial formality...
  natural rather than performed"). Give that principle concrete operational
  teeth: the pattern-repertoire concept, the bridge-first instinct, explicit
  instruction to draw on Ecological Function/Distortion Risk during voice
  construction, and a worked-example requirement for every future world
  (not optional, the way it effectively was for five of the current six).
- **Part Eight (the validation probe battery)** — add a naturalness/register
  probe category, checked the same rigorous way confidence-under-thinness
  and self-referential probes already are, so a future build gets caught
  automatically if it drifts from Part Five's own stated principle the way
  these six did. This is the actual "self-sufficient" fix — without it, the
  framework can restate its own good philosophy indefinitely while builds
  keep drifting from it unnoticed until someone runs a live conversation
  test months later.

## 8. Verification — a real checkpoint, not a self-report

(This verifies the rebuilt voices themselves, once built — distinct from
§9's adversarial-review gates below, which verify the thread's own
research/design/blueprint documents at each stage, before the next stage
builds on them.)

- Reuse `cic-poc/backend/scripts/mark_conversation_test.py`, already built
  and proven this session (real conversations through the actual FastAPI
  backend, real Anthropic billing, full transcript + per-call usage
  capture). This environment's network policy blocks huggingface.co, so the
  script's embeddings/cross-encoder are network-free lexical stand-ins —
  documented in the script itself; BM25 and every citation shown are real.
  If this thread runs somewhere with real network access, prefer the real
  embeddings model.
- **Live-test Albina and Marius as the primary acceptance evidence** — not
  an afterthought after "the real three." Per finding (D), the original
  three baselines don't demonstrate the failure being fixed; these two do,
  or are the most likely to.
- Regression-check the original three baselines (transcripts already saved,
  referenced in the Decision Log entry in §3) — confirm nothing about them
  got worse, not that they "still read fine."
- Run at minimum the confidence-under-thinness and sustained-multi-turn-
  coherence probe categories from the Framework's existing Part Eight
  methodology (`cic-validation-suite`) against the rebuilt worlds — a
  stronger, more auditable bar than a transcript read by eye alone.
- Watch two specific metrics in the before/after diff, not just general
  impression: the `FLATTENING` drift-signal rate (per §4's governance note),
  and the `over_settling_adjudication` firing rate (per §4's second scoped
  defect — the new voice instructions push toward more unhedged claims,
  worth knowing if that measurably moves this number even though fixing the
  check itself is out of scope).
- Before treating any finding in this brief as settled, verify it against
  the file/line cited, per §3's standing discipline.

## 9. One thread, staged — research, design, blueprint, build, each gated by adversarial review

Unlike the prior system redesign (which deliberately split design and
blueprint across two separate weekly Fable passes), this brief's scope —
six voice files plus one framework document — is likely small enough to
carry through **research → design → blueprint → build in one thread**,
staged rather than split. Four stages, not three: this brief's own §5
diagnosis was shown mid-session to be incomplete in at least one place (the
worked-examples question in finding C), so Fable needs real room to extend
and verify the diagnosis before designing against it — not to "confirm" a
diagnosis this brief hands over as settled fact.

**What Fable is building, at every stage below: two tracks, not one.**
(1) A standardized mechanism — the shared `_HOW_YOU_ENGAGE` changes, and
whatever the Research stage concludes about worked-example form — applying
to all six worlds alike. (2) Individual adaptation — each world's own
per-file pass, keeping and sharpening what already makes it distinct
(Albina's periodic rhythm, Marius's entangled reasoning-mode, etc.) rather
than flattening toward a template. This brief tells Fable what to research,
design, blueprint, and build toward — never the specific per-world answer;
that's what the individual-adaptation track is for, and deciding it per
world, informed by the standardized track's findings, is Fable's call.

1. **Research** — extend and stress-test §5's diagnosis before treating any
   of it as ground to design on. At minimum: resolve finding (C)'s open
   question (does Papnoute's existing worked-example pattern hold up against
   FLAG-018-style probes; does a contrastive/negative example close the gap
   the same-day pilot found in Chloe). Live-test whatever the Research stage
   still finds underdetermined — don't inherit this brief's diagnosis
   uncritically, per §3's standing discipline.
2. **Design** — confirm or revise the shared-file approach and each
   per-world pattern against the (now Fable-verified, not just
   this-thread-verified) diagnosis and this brief's objectives (§6). Produce
   both tracks explicitly: the standardized mechanism, and a stated
   per-world adaptation approach for each of the six.
3. **Blueprint** — sequence the risk-ordered per-world passes (§7) with a
   real verification checkpoint after the pilot and after each subsequent
   world — not just a final pass at the end.
4. **Build** — execute in order, checkpointing as sequenced.

**Adversarial review gates every transition, per
`Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`
— Opus tier, not Fable, per the model-tier policy that document itself
cites.** Research's findings get an adversarial pass before Design is
allowed to build on them; Design's output gets one before Blueprint
sequences it; Blueprint gets one before Build spends the expensive pass
executing it. Each pass uses the Standard Practice's actual discipline —
source-level verification against the cited file/line, not
plausibility-checking; P0/P1/P2 severity; cross-reference and completeness
checks counted, not eyeballed; read the prior gate's findings first; a
genuine "ready" or "not ready" verdict, not softened toward approval because
a deadline is close. Name the failure mode explicitly in each dispatch, per
the Standard Practice's point 5 — for this thread specifically: **this
brief itself already contained one claim (finding C's original "worked
examples are the fix") that sounded right and didn't survive being tested
live; assume the same risk is present in Research's and Design's own
findings until checked.**

**This brief itself should get one more Opus adversarial pass before
Friday's Fable thread starts** — the same discipline the 2026-07-25 System
Redesign brief got three rounds of before its own Fable pass, and this
document has had enough live edits since §5 was first drafted (this
finding-C revision included) that it hasn't had a full pass since.

If partway through this genuinely doesn't fit in the available Fable budget,
say so plainly and stop at a clean boundary (e.g., after the pilot, or after
the two highest-risk worlds) rather than compressing quality to finish —
matching this project's own standing discipline of honest partial completion
over a rushed full one.
