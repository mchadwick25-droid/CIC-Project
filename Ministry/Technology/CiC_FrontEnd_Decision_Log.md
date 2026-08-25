# CiC Front-End & Product — Decision Log

Dated entries: what was decided (or what's still open), the reasoning — including the
"heart" reasoning, not just the operational one — and the specific next action. A
decision that only lives in conversation history is one that gets re-litigated by
accident later.

Scope: the participant-facing product — what a real person sees, clicks, and
experiences. Distinct from the world-build threads (which own construction methodology)
and from the System Hub log (which owns operations and thread dispatch).

---

## 2026-08-14 — The current-day space: scoped as its own program, not started

**Origin.** Raised by Mark immediately after the Era 10 freeze, while looking at what the
frozen map does and doesn't do for a present-day visitor. His framing, in his own words
across the exchange: *"whats happening in the world today, where do i fit, where do i
go"* — and *"we show more of jesus by revealing what jesus is doing and they can find
things they resonate with and reject. and eventually find Jesus in deeper relationship by
finding a place."*

**Status: SCOPED, NOT STARTED.** Mark's explicit sequencing — finish the ten-era Atlas
and get it live first, then the interview and multi-voice Table upgrades in their own
threads, and only then open this. Recorded here so the thinking survives the gap.

### The gap this answers, with the number that grounds it

The census has **one living row starting after 2000, and four starting after 1990**, out
of 257 at the time of the finding. A visitor arrives in the present and the map goes
quiet right around where their own experience begins. That is not a defect in the
historical work — it is the recency floor doing its job for history and failing when
applied to today.

Two structural facts about living movements that the Atlas's grammar does not currently
carry, both surfaced in this conversation:

- **Many living currents are not things you can join.** New Calvinism, deconstruction,
  the Christian Right — these run *through* institutions rather than being institutions
  with boundaries. That distinction is exactly what someone asking "what are my options"
  needs, because the answer differs completely: one is a door you can walk through, the
  other is a mood inside doors you might walk through. The census has no field marking it.
- **There is no alias field at all** (verified: zero rows carry one). People search what
  they have heard — "young restless reformed," not "New Calvinism"; "exvangelical," not
  "deconstruction." Living rows need an also-called list, including labels a movement
  itself rejects, marked as rejected — more findable *and* more honest than implying a
  settled name exists.

### Decisions

1. **It is its own program, not an Atlas feature.** The vision document already carries
   the mandate — the mission says "throughout history **and today**," and Conviction 1
   says "historical **and contemporary** movements." The contemporary half has simply
   never been built. This is the unbuilt half of the stated mission, not an add-on.

2. **Organise by question, not by movement.** The Atlas is organised by movement and by
   birth date, which is right for history. A person exploring faith is not asking "what
   movements exist" — they are asking who Jesus is, what forgiveness means, why
   suffering, what to do with doubt. The current space leads with the question and lets
   living traditions answer it. The Atlas then sits underneath as the "where did this
   come from, and how did it get here" layer — Mark's own "the map can work into it."

3. **Show what is shared, not manufactured contrast — Mark's correction, adopted.**
   An early framing had several traditions answering "visibly differing." Mark rejected
   it: *"we don't need to always put different ideas in contrast or exclusivity."* He is
   right, and the vision backs him — it says outright the project is not for
   denominational comparison. Much of what is alive right now is shared across
   traditions: prayer, scripture, feeding people, people returning after years away.
   Showing that as *one thing happening in many places* is closer to revealing what Jesus
   is doing than staging a debate. Difference still gets shown where it is real and
   load-bearing — just not produced everywhere by the layout.

4. **Seeing more of Jesus and finding a place are one arc, not a fork — Mark's
   correction, adopted.** An earlier framing offered these as alternative product goals.
   Mark: *"its not just a single think we can do both... eventually find Jesus in deeper
   relationship by finding a place."* The operative line is not "never point at a door" —
   it is **don't push anyone through one.** Showing someone that what moved them exists
   in real communities with real doors is service; ranking those communities for them is
   not. A "find your tradition" quiz would violate participant agency even though it
   would be the most clickable thing available.

5. **Rigor moves, it does not loosen — and rule-making must not become the obstacle.**
   An early draft of this thinking treated the vision's Living Traditions clause ("a
   tradition's present-day self-understanding... is not ours to define or represent") as
   a hard constraint requiring an elaborate protocol. Mark corrected this twice, and the
   correction stands: that clause exists because historical source sets are *closed* and
   those communities cannot speak for themselves any more. Living movements are the
   opposite — they publish constantly and are entirely capable of speaking for
   themselves. So we point at what they actually say, dated, and let people read it.
   Mark, verbatim: *"all these added rules that you add cant get in the way."* Recorded
   as a standing caution on this track — the Era 10 rigor regime was right for a frozen
   census and would be wrong here.

   **The whole standard reduces to one honest line to the participant:** this part of the
   map is settled and sourced; this part is alive, it moves, here is when we looked, and
   people inside it disagree about what it even is.

6. **Misconceptions: let the tradition answer, never adjudicate.** Mark asked for a space
   where people can explore "their own and other truths and misconceptions." CiC ruling
   on what is a misconception would make it referee between living communities. The
   working form instead: *here is what you may have heard; here is what they say about
   themselves right now, in their own words* — the participant does the reconciling. This
   preserves participant agency and is more persuasive anyway.

### Related, decided on the census side the same night

An **era 11 emerging band, defined by confidence rather than a date cut** — everything in
it visibly provisional, rows graduating into era 10 as they stabilise. A hard ten-year
line is false precision. This gives currents like deconstruction a home that is not
"retain with a caveat, demote to mentions, or delete." Also named as the largest missing
piece: a **trajectory reading** per living row — what this was twenty years ago, what it
is now, what moved it. Full account in the System Hub Decision Log, 2026-08-14.

### Next action

None yet, by Mark's own sequencing. When this opens: draft a short program brief on the
shape above — question-first surface, shared-before-contrasted, the Atlas underneath as
the provenance layer, and the one transparency line. Not a protocol.

**Open, and deliberately not resolved here:** platform and phase placement (this does not
obviously belong to any rung of the existing Alpha → Beta → Phase 1 → Phase 2+ ladder),
whether it ships inside the existing app or as its own surface, and its cost shape.

---

## 2026-08-25 — Three-level transparency: scoped as its own dedicated build, not a port

**Origin.** Mark used the newly-launched pilot (`cic-engine`) and reported three real
problems: (1) the three-level transparency system (highlight → hover → click) is not
working; (2) the Facilitator gives no greeting at session start, just a prompt at the
bottom; (3) the world-selection cards are too thin to build participant confidence about
"which Christian world" they're entering. All three are real product gaps, not launch bugs.

**Status: SCOPED, NOT STARTED.** A full launch prompt for a new dedicated thread has been
written and handed to Mark. Items 2 and 3 are deliberately deferred — Mark's own
sequencing — to start only once transparency work is underway.

### Decisions

1. **Transparency gets its own thread, not a copy-over.** Mark: *"this is a bigger project
   than importing or copying over what was there... i want it done very well, designed
   well, built well and implemented well."* The old `cic-poc` components
   (`GlossHighlight`, `LexiconModal`, `Level3Panel`, `CitationMarker`, `CitationModal`) are
   reference for what was tried, not a working baseline to port — they were removed from
   the tree and the underlying wiring (glosses, figures, citation depth) was never
   finished even there.

2. **Scope is all three tracks together — highlight, hover, and click** — not a phased
   subset. Mark's answer to the scope question: *"all three."*

3. **The heart of it is discovery, not comprehension-aid or credibility-verification —
   Mark's correction, adopted.** I offered a binary framing (don't let someone get stuck
   on a word / let someone verify a claim); Mark rejected both for something more central:
   *"its discovery, we may think differently or understand words differently. its deeper
   discovery."* The target is a participant noticing where their own assumed meaning
   diverges from the world's own frame — not just glossing an unfamiliar term. This
   reframing governs what content the system should surface, not just how it displays it.

4. **Items 2 (Facilitator greeting) and 3 (richer world cards) wait.** Mark: work on those
   "after we get the work on the 3 level transparency working." Both remain real,
   confirmed problems — greeting text drafts (A/B) are drafted and awaiting his pick;
   richer cards have real unused source material identified (`world_core`'s `horizon`
   field, compiled `frame.frames.general_seeker.starters`) — just not started.

### What the launch prompt carries forward

Grounding so the new thread doesn't have to rediscover it: the *current* gap is
structural (glosses are hardcoded empty, figure records are compiled but never wired to
any API or frontend path, citations render flat with no Level 2/3 depth) and distinct from
the *historical* diagnosis in `VR_1A_Transparency_Gap_2026-08-09.md` (the old system's gap
was mostly unfamiliar names/figures, not generic vocabulary). The interaction design is
already decided and final in `CiC_Full_UX_Design_V1_0.md` §9.1 — side panel / bottom sheet
only, never a centered modal. A real, authored, reviewed content layer already exists
across all six worlds and is currently unused by anything — `modern_contrast` (60 records)
and `senses.translational` (85 records) — that does exactly the "deeper discovery" work
Mark described once he named it, and should be the backbone of what the click level shows.
`transparency_reach.py` is the existing measurement instrument (report-only by design, no
pass/fail bar, to avoid a "gloss everything" pressure that would make the Representative
lecture) and should be used to check the finished build, not just diagnosed as a tool.

**Model choice for the new thread:** recommended Sonnet 5 for the build (compiler wiring,
new API endpoint, frontend components — well-specified engineering, not open-ended
judgment), with Opus 5 called in specifically for the content-selection quality pass
across the six worlds and a design-fidelity check against the UX spec — not as a blanket
reviewer. Fable 5 not recommended: its premium is for resolving ambiguity, and the scope,
framing, and interaction design here are already decided.

### Next action

Mark takes the launch prompt to a new thread and starts the build there. Once transparency
is working, resume items 2 and 3 in this thread per his sequencing.

---

## 2026-08-25 — Richer world cards/doorway built; Facilitator greeting drafted, awaiting pick

**Status.** Transparency (the prior entry) shipped and launched in its own thread. Picked
up items 2 and 3, deferred from the 2026-08-25 pilot feedback per Mark's own sequencing.

### Item 3 (richer cards) — DONE, built and pushed

**Concrete finding, not just a vibe:** the world-list card never rendered the world's own
display name at all — only the Representative's personal name and role (e.g. "Chloe ·
Household Leader"). A participant scanning six cards had no direct way to tell *which
Christian world* a card even was, which is exactly Mark's stated complaint ("clarity of
wth chrsitian world"). Fixed directly: the tradition's display name now leads every card,
in its accent color.

**The doorway went further**, closing real gaps against Program-Spec SS165's own
definition of "the detailed world card" (display name/period/place, thinness statement,
the living-tradition distinction where flagged, self-disclosure, persona provenance,
starter questions) — most of which the doorway had never carried:

- **horizon** — world_core's own scene-setting paragraph, already authored and already
  compiled into the voice's own system prompt, but never surfaced to a participant. Now
  compiled into `compiled/frame.json` too (`engine/m2/builders.py::build_frame_json`) and
  shown as the doorway's lead paragraph.
- **Living-tradition distinction** and **self-disclosure/persona provenance** — both
  quoted verbatim from the spec itself (O0 for "who built this and what it hopes";
  SS165/SS166 for the living-tradition sentence and the persona-provenance line). Verbatim
  quotation of language Mark already approved at the spec level, so this did NOT need a
  fresh draft-and-approve round the way new Facilitator copy does.
- **Starter questions** — sampled from the compiled frame's real per-cell canon
  (identity/personal/critical framings, not an arbitrary first three), so a participant
  can see the actual range of what's askable before committing.

**New surface:** `GET /api/worlds`, reading each formation world's real compiled
frame.json through the same load path a session uses — the frontend's `data/worlds.ts`
had carried its own comment since Stage 4 admitting it hand-copied the registry because
"no /api/worlds endpoint exists yet." That endpoint exists now; the frontend fetches live
and keeps only what the registry never carried (portrait image, accent color, display
order) as local assets. All 7 registry packages (6 formation worlds + the fix fixture)
recompiled to carry `horizon`; determinism and staleness both green; 349 backend tests
pass; verified live in a browser against the no-spend dev server (world list, doorway,
deep link, and full conversation flow all screenshotted and working).

### Item 2 (Facilitator greeting) — DRAFTED, awaiting Mark's pick

The conversation screen still opens with no introduction — confirmed still true, and
still exactly the gap Mark named ("no introduction, do greeting"). `facilitator_turn`'s
`"door"` kind has been declared in the event schema since early in this build but is
still never emitted anywhere in the codebase (confirmed by direct grep, not memory).

Two drafts, same discipline SYSTEM_NATURE/CHECK_IN/DEPENDENCY_CHECK went through
(`engine/m4/facilitator_turns.py`) — plain, honest, no invented warmth the system hasn't
earned, and keeping the SS4.3a convention that the Facilitator names itself plainly while
the Representative is named by its own registry name:

- **Option A (short handoff):** "Welcome — I'm the Facilitator. I don't belong to any
  world; I'm just here to keep this space honest. You're about to speak with
  {representative_name}, {role_label} of {display_name}. Ask anything you like —
  {representative_name} answers only from what's actually known of this world, and will
  tell you plainly when the record runs out."
- **Option B (fuller, door metaphor):** "Welcome. I'm the Facilitator here — not
  {representative_name}, and not any world myself. Think of me as the door: I step aside
  once you're through it.\n\nIn a moment you'll be speaking with {representative_name},
  {role_label} of {display_name}, {place}, {eraStart}–{eraEnd}. Ask anything that's
  actually on your mind. {representative_name} will only answer from what's actually
  known of this world, and will say so plainly whenever it isn't."

Leaning A: the spec's own "witness, not a home" principle (never optimize for engagement)
argues for the Facilitator doing minimal scaffolding at the door, not a warm monologue —
the doorway screen already carried the fuller orientation before the participant ever
clicked "Begin." Not wired into code yet; new participant-facing text waits on Mark's
pick, same as always.

### Next action

Mark picks A, B, or redlines either. Once picked: wire into
`engine/m4/facilitator_turns.py` (a `door_turn()` function, same shape as
`dependency_check_turn`), append it in `engine/api/wiring.py::create_session` right after
`open_session()` (the entrance seal only restricts who may write `session_started`, not
what else `create_session` appends after it), and seed the frontend's `useConversation.begin()`
turns from the session-create response instead of `[]` — all three sites already scoped,
no design work left, just the text.
