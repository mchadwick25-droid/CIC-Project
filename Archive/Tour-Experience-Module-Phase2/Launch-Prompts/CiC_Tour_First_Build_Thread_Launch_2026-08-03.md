# Launch prompt — Build the first Tour, Tier 3 visual quality (Fable)
## A hands-on build-and-learning thread, not a planning thread

Paste this into a fresh thread, run on Claude Fable 5.

**This is a BUILD thread, distinct from the planning-only redesign thread
launched earlier the same day** (`CiC_Tour_Redesign_Thread_Launch_2026-08-03.md`).
That thread's job was strategy and design; this thread's job is to actually
produce the first real, experienceable tour — text, a photorealistic 3D
visual layer, and audio — not another planning document.

**Read this before anything else: this is explicitly a learning project for
Mark, not just a deliverable.** He's said directly that using new tools is
part of the value here. That means this thread's job includes teaching as it
builds — explain what each tool does and why a choice was made, walk through
setup step by step, don't silently produce a finished asset and hand it
over. If a step can be done two ways (a faster one that hides the mechanics,
a slower one that teaches them), default to explaining, and ask which Mark
wants for that step if it's not obvious.

---

## What already exists — read all of it, in this order, before touching anything

1. **`Ministry/Features/Front-End-Integration-Strategy/Decision-Log.md`**,
   all nine 2026-08-03 entries — the full reasoning behind every design
   decision below (the restart; Facilitator-narration correction; three-voice
   refinement; two-threshold refinement; fill-density refinement; visual-
   policy refinement; the Williamsburg correction; the shape-proof +
   observer-not-participant rule; the voice/audio cost clarification; and
   this build thread's own launch entry, naming the Tier 3 scope).
2. **`Tour-Experience-Module-Phase2/Launch-Prompts/
   CiC_Tour_Redesign_Thread_Launch_2026-08-03.md`** — the full design brief.
   This build thread inherits every rule in it; do not re-derive or
   re-litigate the design, execute it.
3. **`Tour-Experience-Module-Phase2/
   CiC_Tour_PAHC_Worship_Service_Shape_Proof_2026-08-03.md`** — **the actual
   content to build from.** This is not a starting sketch to redesign — it's
   a tested draft (all seven beats scripted, the three-voice structure
   applied, the observer rule applied, the Corinth/Rome meal diversity
   spoken honestly, the room-description image placed at Beat 1). Build
   *this*, resolving its three named open questions along the way (the
   letter candidate between Ignatius and 1 Clement; verifying every
   quotation against a real citable edition; pacing).
4. **`Tour-Experience-Module-Phase2/CiC_Tour_Comparator_Research_2026-08-03.md`**
   — read Section 2 (Rome Reborn) closely. **This is the template for how
   Tier 3 visual work has to be sourced** — tiered evidence discipline
   applied to geometry and materials, not just prose.
5. **Superseded folders** (`Tour-Experience-Module-Phase2/CiC_Tour_
   Experience_Module_Strategy_V0_3.md`, `Hosted-Tour/`) — historical
   research only. Do not inherit their live-hosted architecture.

---

## The mandate

### 1. Produce the finished text and audio layers

Resolve the shape-proof's three open questions (pick the letter — Ignatius's
Romans 4 or 1 Clement, verify the exact wording against a real critical
edition/translation, don't invent or misquote either), finalize pacing, and
record or synthesize audio for the one scoped performative moment (the
letter reading, Beat 3), per the standing audio policy: **produced once,
reviewed, cached as a static file — never generated live per session.** If
using text-to-speech, generate once and save the output; if using a voice
actor, this is where that gets arranged.

### 2. Produce the visual layer at Tier 3 — disciplined 3D reconstruction, photorealistically rendered

**This is the core new-skills work, and it has to follow the same
evidentiary discipline as everything else in this project, applied to
geometry instead of prose.** The target is Beat 1 (the room-description
scene) at minimum — a 3D reconstruction of an ordinary Roman domus interior
of the right region and era, built and rendered the way Rome Reborn builds
its models:

- **No generative AI imagery, anywhere, at any stage.** This is the
  bright line that makes Tier 3 legitimate under this project's own rules —
  a diffusion model outputting a picture from a text prompt has no auditable
  source for any single pixel. A 3D model built element by element from
  named, real evidence does. If a tool under consideration works by
  generating pixels from a prompt, it's out of scope here, full stop.
- **Every modeled element needs a named, real source, tracked the same way
  a text citation is tracked** — wall construction and room proportions from
  excavated domus/insula plans (Pompeii, Herculaneum, or comparable
  published archaeological data), furnishings from actual period finds or
  museum collections, materials and lighting from documented Roman
  domestic-architecture scholarship. Keep a running source list per element,
  the 3D equivalent of the exemplar-vs-claim caption already designed for
  the flat-photo version of this beat.
- **Tooling to set up, taught as it's set up, not just installed silently:**
  Blender is the recommended starting point — free, capable of
  photorealistic rendering (Cycles), with a large ecosystem of tutorials,
  which matters directly for the learning goal. Confirm what's actually
  available in this session's environment first (local install access,
  compute for rendering) before assuming a workflow; name any environment
  gap plainly rather than working around it silently.
- **Scope realistically for a first build.** A single room, modeled well
  and honestly sourced, beats an ambitious multi-scene reconstruction built
  on guesses. If time or tooling runs out, a well-sourced still render of
  the room is a complete, honest deliverable on its own — do not pad it
  with unsourced detail to make it feel more finished.

### 3. Assemble a real, experienceable first tour

Bring text, the rendered visual, and any audio together into something that
can actually be walked through start to finish — a simple presentable
format is fine (a web page, a slideshow, whatever's practical); polish of
the presentation layer is secondary to getting one real, honestly-built tour
to exist. This is the first concrete proof the whole redesign actually
works, not just reads well on paper.

---

## Absolute rules, restated so nothing drifts mid-build

- **The Facilitator hosts; Chloe only ever speaks within exactly her live-
  conversation bound; primary sources are quoted in their own name.** The
  three-voice structure, unchanged.
- **The participant observes — never a participant in what's depicted.**
  Hard rule from the shape-proof, applies to how the visual scene is framed
  too (the camera/viewpoint is a witness's position, not a first-person
  hand reaching for anything).
- **Two thresholds, not one:** the Facilitator welcomes to the experience;
  Chloe (in bound voice) welcomes into the scene.
- **Honesty is Williamsburg-shaped:** narrated framing happens once, at the
  threshold; visual/source honesty is a quiet, always-discoverable label,
  never a repeated interruption.
- **Nothing generates live, anywhere, at runtime, once this ships** — not
  narration, not audio, not the render. Everything a participant experiences
  is a static, pre-produced asset.

---

## Coordination boundary

This thread produces real production assets — the finished script, rendered
visuals, audio files, and an assembled first-tour artifact — and touches new
files/tooling within this project's own repository (a production/assets
location for the redesign thread's judgment to place sensibly). It does
**not** integrate anything into `cic-poc`'s live application or touch its
production code — that remains a future handoff, named plainly if this
thread's work implies one, not started here.

## Logging

Log real decisions, tool choices, and open questions in a decision log under
this feature folder (continuing `Tour-Experience-Module-Phase2/Decision-Log.md`
with a clearly dated new section, or a fresh log — thread's judgment), same
dated-entry discipline as every other thread in this project. Given the
learning-project framing, also log **what Mark actually learned or decided
about the tools themselves** — which parts of the Blender/rendering workflow
he wants to keep doing by hand versus hand off, since that shapes how the
*next* tour gets built, not just this one.
