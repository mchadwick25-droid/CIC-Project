# Launch prompt — Tour / Hosted Experience Module thread (Fable)

Paste this into a fresh thread, run on Claude Fable 5. This is a **Phase Two** product
concept — a hosted "tour" or "experience" mode where a Representative doesn't just
answer questions, but actively invites the participant into a reconstructed moment
(a worship service, a shared meal, a specific rite) and walks them through it using
period art, artifacts, and description, stepping in to explain, translate, and answer
questions along the way.

**Scope note, read this first:** this thread does **not** touch `cic-poc` code, does
**not** change anything about the current prototype or Phase One testing, and does
**not** integrate this feature into the live app. It produces strategy, a per-world
evidentiary analysis, and an architecture design — all as planning artifacts for a
future build phase. Where this thread's work implies a build item, name it plainly as
a future handoff, the same discipline every other thread in this project follows.

---

## The idea, stated exactly as given

Instead of only interviewing the Representative, the Representative can **host** the
participant through a reconstructed experience of their world — a worship service, a
meal, a specific communal rite — using period art and illustration to set the scene,
while the Representative is present throughout to answer questions, fill in gaps, and
translate. This is explicitly **not** invented content: the tour only covers what the
sources actually support. If a world has no real sourced example of a communal
experience (e.g. no textual basis for reconstructing a worship service), **no tour is
offered for that world** — the absence is itself an honest finding, not a gap to
paper over with invention.

**Product framing:** an add-on module — if the project ever moves to a tiered service,
this is a plausible "Level 2" offering, not part of the base conversational encounter.
Not integrated now; kept as a real, buildable-later capability.

## What already governs this, read in this order

1. **`Ministry/Communication/Vision, Mission, Convictions, and Foundational
   Commitments V1.1.docx`** — the Why. Two commitments bind this concept tightly:
   - **Conviction 4** (authentic encounter requires trustworthy transparency — nothing
     essential hidden, nothing invented to smooth over a gap) is the entire reason the
     "only tour what the sources allow" constraint exists. A tour built past its
     evidentiary base is not a richer encounter — it's exactly the kind of confident
     overreach the whole project is built to refuse.
   - **Foundational Value: Historical Responsibility** — a tour is, structurally, a
     *higher-stakes* claim than a conversational answer: it says "this is what a
     morning gathering looked like," not just "here is what I can tell you about it."
     That claim requires more evidentiary weight, not less, than an ordinary reply.

2. **`L1-Foundation/CiC_L1_Constitution_V2_2.docx`** — the What. Article 6's
   Encounter-Success Standard (did the encounter present the world honestly with its
   tensions held, not oversold) applies with extra force here — a beautifully
   illustrated tour of a fabricated scene would technically "keep the Representative
   itself" while still violating the honesty the Standard actually protects.

3. **`L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.3.docx`**
   — the How. Two existing pipeline concepts are directly reusable here, not
   duplicative to invent fresh:
   - **Source Ecology assessment (Doc_02)** already asks, per world, what kind of
     material exists and at what density — this is the same judgment a tour needs, at
     a stricter bar (a tourable *scene* needs more than a lexicon term or a doctrinal
     position; it needs an actual narrated or liturgical description of an event).
   - **Story Repository / Doc_09** (see `anthropic-skills:cic-story-repository`) already
     tiers narrative material by evidentiary strength (Tier 1 founding scenes vs.
     thinner material) and has already, in at least one live world, done exactly this
     kind of judgment call — e.g. Papnoute's world licensed only three Tier-1 founding
     scenes told in full. **Read each live world's actual Doc_09 Story Repository before
     doing any fresh evidentiary analysis for this thread** — the sourced-scene inventory
     this thread needs may already exist there in large part.

4. **`cic-poc/backend/app/world_manifest.py`** and each world's own
   `*_World_Capsule_Core.md` / lexicon and story chunks — the actual current content
   for the four live worlds (The House-Churches, Syriac Christianity, Desert Fathers and
   Mothers, The Bethlehem Circle). This thread's per-world evidentiary analysis (item 2
   below) must be grounded in what these files actually contain, not assumed.

## What to produce

Work through these in order — do not skip to architecture before the evidentiary
analysis is done, since the architecture's scope depends entirely on which worlds
actually qualify.

### 1. Strategy

Draft the actual product strategy for this module: what "hosted through an experience"
means concretely as a participant-facing flow (how it differs from the existing
conversational encounter, where it starts and ends, how the Representative's voice
discipline — never modernizing, never inventing — carries into a scene-narration mode
rather than just a Q&A mode). Address explicitly: does illustrated/visual content
require a new kind of asset (period art, commissioned or sourced) that the project
doesn't currently have any pipeline for, and if so name that as a real, separate
production question, not something this thread can casually assume exists.

### 2. Per-world evidentiary analysis — do this exhaustively, one world at a time

For **every** live and in-progress world (The House-Churches, Syriac Christianity,
Desert Fathers and Mothers, The Bethlehem Circle, and Nicene-Cappadocian if its
construction has progressed by the time this thread runs), answer honestly:

- Does a real, sourced example of a communal/liturgical/shared-life scene exist in this
  world's own construction record (Doc_09 Story Repository, the Permanent Prompt, the
  World Capsule Core)? Name the specific scene if so (e.g. "a sourced example of a PAHC
  worship service" per the user's own example) and its evidentiary tier.
- If no such scene exists, **say so plainly and do not offer a tour for that world.**
  This is itself the required output for that world — not a placeholder to fill in
  later, an honest finding.
- If a scene exists but is thin (a single mention, not a narrated description), name
  that distinction explicitly — a tour built on a thin mention is a different, weaker
  claim than one built on a fully narrated source, and the architecture (item 3) needs
  to know which case it's building for.

Produce this as a real table or per-world section, not a summary paragraph — a future
builder needs to be able to look up "is a tour possible for World X, and on what basis"
without re-deriving this analysis.

### 3. Architecture

Only after item 2 is complete, design the module's architecture:
- How a tour is triggered from within an existing conversational encounter (the
  Representative "invites" the participant — what UI/UX signal represents that
  invitation, and does the participant have to accept it, matching the project's
  standing Participant Agency value — nothing forced, always an open door the
  participant chooses to walk through).
- How period art/illustration is sourced, licensed, or generated, and how that content
  is bounded by the same evidentiary discipline as the text (an illustration implying a
  detail the sources don't support is the same violation as an invented sentence).
- How the Representative's role shifts during a tour (host/narrator/interpreter) versus
  its role in ordinary conversation, and what guardrails keep it from drifting into
  inventing texture to fill visual or narrative gaps.
- Where this would technically integrate into `cic-poc`'s existing structure *if* it
  were ever built (which components it would touch — frontend, backend RAG/story
  retrieval, world_manifest) — as a forward-looking technical note only, not a build
  task for this thread.

## Coordination boundary, stated plainly

This thread produces strategy, evidentiary analysis, and architecture design only. It
does not:
- Touch `cic-poc` frontend or backend code, now or as part of this thread's own work.
- Integrate anything into the current prototype or Phase One testing — explicitly out
  of scope per the user's own framing.
- Invent sourced scenes for worlds that don't have them, under any framing ("we could
  imagine a plausible service based on general Christian custom of the era" is
  precisely the move this module exists to refuse).

## Logging

Log real decisions and open questions in
`Ministry/Technology/CiC_Tour_Experience_Module_Decision_Log.md` as they happen — same
dated-entry discipline (what was decided, the reasoning including the heart of it, the
next action) already in use in the other threads. Don't let a real decision live only
in this thread's own conversation history.
