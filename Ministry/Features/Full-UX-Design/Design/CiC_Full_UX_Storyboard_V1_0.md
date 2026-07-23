# CiC Complete Experience Storyboard — V1.0

**What this is:** every path a participant can take through Church in Conversation, from
the entry page (S0) through every branch to a completed conversation and close — drawn as
one continuous storyboard. Almost all of it is **already decided**; this document's job is
to show the decided design as a single journey, cite where each piece is governed, and
design **only** the two gaps that had never been designed (the Guided-onboarding door, §G;
the Question-First Tier-3 routing UI, §R). A companion visual artifact renders the five
highest-value frames (§Mockups); everything else is descriptive on purpose.

**Reading this document — the flags:**
- **[DECIDED — cite]** designed and approved; the cite is the governing doc/section.
- **[NEW DESIGN]** designed first in this storyboard (only §G and §R).
- **[BUILT · NOT MERGED · NOT VALIDATED]** exists on an exploration branch; storyboarded as
  *intended* behavior — **the running app does not do this today.**
- **[PLACEHOLDER]** an honest visible placeholder in the design; no content behind it yet.
- **[OPEN]** a decision that belongs to someone else; rendered at its current default,
  foreclosed nowhere.

**The two corrections this storyboard is built on (trust these over stale body text):**
1. **The Living Table is fully static.** Composition set once at conversation creation;
   **nothing moves — no camera, no pan, no zoom, and no corner speaker-chip** (both
   superseded). The only state change anywhere in the scene is the speaking
   Representative's **nameplate inverting** vellum/ink → dark-ground/light-text, and back
   (on phone, a top row of nameplates does the same). Governing truth:
   `Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md` §1/§1a/§1b and the V1.0
   Document Log (V1.0.1 entry). The V1.0 body prose still carries camera/chip language in
   ~20 places — flagged to the System Hub as a spec-text bug (see the Hub update).
2. **Five live worlds, not four.** Alexandria/Theon went live 2026-07-17; the Coverage
   Cards carry five cards. Older surfaces still say "four" (map legend, first-visit
   overlay) — flagged, not silently fixed here.

**Terminology used throughout (current):** doors = **Start with your question · Build your
own table · Guided onboarding** (co-equal, never ranked). Modes = **Regular visitor ·
Pastor or teacher · Academic or scholar · Reevaluation** (code identifier is now
`reevaluation` too — the rename was executed in code and approved by Mark 2026-07-18,
commit `9774447`, corrected here 2026-07-19; this document originally described it as
still open, which was stale within a day).
Seating is **emergent**: worlds are added one at a time to a tray; the framing text and the
rendered 1/2/3-seat table template update silently. Hard ceiling: **3 Representatives**;
4th/5th-seat templates deferred.

**Governing documents:** `CiC_Full_UX_Design_V1_0.md` (the backbone) ·
`Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md` (Living Table truth) ·
`CiC_FrontEnd_Integration_Strategy_V0_1_DRAFT.md` (IA: stages, tiers, budget) ·
`CiC_QuestionFirst_Entry_Design_V0_1.md` · `CiC_Guided_Questions_Curriculum_V1_0.md` ·
`Representative-Modes/CiC_Representative_Modes_Design_Spec_V0_1.md` ·
`World-Orientation-Map/` · `Hosted-Tour/` · `CiC_World_Coverage_Cards_V0_1.md` ·
`CiC_Feature_Integration_Readiness_2026-07-17.md`.

---

## Part 1 · The whole tree at a glance

```
S0 THRESHOLD — three co-equal doors (+ 2 quiet chrome: Ask the Facilitator · menu overlay)
│
├─ Door 1 "Start with your question"  → S3 typed question (or theme chip)
│     → R1 considering → R2a proposal | R2b clarify-once [NEW] | R2c honest null
│     → proposal card → Begin  ─────────────────────────────┐
│
├─ Door 2 "Build your own table"  → S2 picker + tray        │
│     ├─ (optional loop) S1 World Map — desktop atlas        │
│     │      / phone era-accordion → tray handoff → S2       │
│     ├─ world-click menu (Description·Tour·Choose·Academic) │
│     ├─ role selector (4 modes + no-role default)           │
│     └─ Begin (Deep Interview ⇄ Compare Worlds, emergent) ──┤
│                                                            │
├─ Door 3 "Guided onboarding" [NEW DESIGN §G]                │
│     G1 where you're starting from → G2 what draws you      │
│     → G3 a prepared table (proposal grammar) → Begin ──────┤
│                                                            ▼
│                                    S4 THE TABLE (the permanent center)
│                                    static composed Living Table · long-form transcript
│                                    nameplate inversion = who's speaking
│                                    ├─ lexicon / citations (hover→popover→panel)
│                                    ├─ "Don't know what to ask?" → question sheet
│                                    ├─ T3 slot: safety(∅) ▸ tour invite ▸ next-questions
│                                    ├─ S4-tour (a mode of S4, Chloe only today)
│                                    └─ safety / status / error states
│                                                            │
│                                                            ▼
│                                    S5 THE CLOSE — gracious close → anything else?
│                                    → reflection beat → resources → the door outward
│
└─ (X) Onboarding/consent — once, before any door; loading & error states
```

Every arrow above is one-directional consent: **Begin is the only thing that seats a
table**, everywhere — the map preselects, proposals propose, guided onboarding prepares;
none of them starts a session [DECIDED — MapInt §1: "The map never auto-starts a session";
QF §1: "the Facilitator proposes, never seats"].

---

## Part 2 · The storyboard, screen by screen

### S0 — Threshold [DECIDED — V1.0 §5.1]

**0.1 Resting.** Hero: the waiting Table in warm light, the Facilitator present as the one
figure; headline = the protected hook — *"Twenty centuries of the church. One table. A
chair pulled out for you."* — CTA register beneath: *"Come and join us at the Table."*
Below, **three co-equal doors** — identical cards, identical weight, no default, no
"recommended": **Start with your question · Build your own table · Guided onboarding**.
Quiet chrome (cap 2): *Ask the Facilitator* (same voice as the encounter's host; absorbs
"why isn't world X here?" — IS §3.7) and the menu (About · Features · FAQ). Cards: 0.
Three doors is a **ceiling** [OPEN — IS §5: map-as-door-form proposal awaits Mark].

**0.2 Menu overlay open.** About/Features/FAQ as a temporary overlay *on top of* the page
— never a navigation-away; participant-opened, dismissed in one action. **0.3 Ask the
Facilitator open.** Pre-threshold Q&A in the Facilitator's own "I" voice; full-sheet on
phone. Five-count: 1 (door set) · 2 chrome · 0 cards · 0 modals · n/a ✓.

*Phone:* doors stack vertically as identical cards — co-equality survives the stack.

*Alpha honesty:* the running app is Bypass-shaped (onboarding → picker → Table); the
three-door threshold is the Phase-1 target the screen grows into [DECIDED — IS §5.1].

### S1 — Orientation: the World Map (an optional loop off S2, never a gate)

**Entry** [DECIDED — IS §1 S1]: one quiet line at S2 — *"See these worlds across two
thousand years — open the World Orientation Map."* On explicit request only; never
auto-opened; **not reachable from S4** ("Orientation is a between-conversations activity").
Also reachable from R2c (the null case points here) and G3 ("see the whole map").

**1.1 The atlas (desktop)** [DECIDED — MapSpec/MapVis; BUILT · NOT MERGED — branch
`claude/world-map-integration-exploration`, Tier A verified live]:
- **First visit:** three-sentence overlay (two thousand years… worlds open today… "The
  whole map is real — and honest about what's built and what isn't"), one action *Look
  around*; opens scrolled to the ancient era, live worlds at full manifest color amid the
  dimmed landscape. *(Overlay copy still says "Four… open" — stale, five now; flagged.)*
- **The census:** ten eras (1 The Early Church … 10 The Global Church), engraved register
  (Cinzel display, parchment/leather grounds, era medallions with their own source
  credits); ~178 bands across six honesty statuses — Live · In Construction · Selected ·
  Deferred (grounds on record) · Pre-Survey · Excluded (grounds one click away) — "dimmed
  is an honest state, not a disabled state"; nothing hover-dead, ever.
- **Disclosure grammar:** hover = glimpse card (name, dates, region, status,
  living-tradition chip; Live worlds add *Add to conversation · Learn more · Take a tour*
  [PLACEHOLDER]); click = full panel (description, prose edges with confidence-styled
  lines — solid/dashed/dotted, drawn on demand, "never an arrow it can't defend" —
  sourcing status, actions: **Have an interview** / **Join a conversation**). Non-live
  panels: honest not-yet copy + *Add nearest built neighbor*.
- **The tray** (persistent, bottom): seats accumulate; 1 = Deep Interview framing, 2–3 =
  Compare Worlds — emergent, no mode switch; one action, **Sit down at the Table**.
- **Handoff contract:** returns `/?worlds=<id,id>&mode=<interview|table>` (+`role=`,
  +`q=` when Tier 3 lands); app preselects, scrubs the URL, **Begin stays the only
  consent** [DECIDED — MapInt §1].
- **Era grounds:** when the atlas is next edited it adopts the approved ten-era
  warm→cool palette (icon spec §7) [DECIDED, hand-off open — IC-10].

**1.2 The era-accordion (phone, <640px)** [DECIDED as the production answer — MapVis §7;
not yet built first-class]: full-screen list — search + era/status filter chips; ten era
accordion rows (name, dates, count line); expanding lists bands as tappable rows
(status-dot · name · dates · one line); tap = glimpse as bottom sheet; "Full entry" = the
panel; same persistent tray + handoff contract. A different form, not a shrink.

**1.3 Handoff return.** Worlds preselected at S2, URL scrubbed, Begin armed.

**Scope honesty** [OPEN]: Tier A (supplementary view + handoff) is the built, decided
scope; **Tier B** (map as primary selection surface) is deliberately undecided, gated on
observing real participants. Storyboarded here as secondary/linked — the current default.

### S2 — Table setup [DECIDED — V1.0 §5.3]

**2.1 Resting.** Primary: the picker ("Choose a Tradition" — five live world tiles now),
the tray/seat state, and **Begin** (madder). Quiet chrome (cap 3): the map line; the
**role selector**, collapsed to one line — *"Optional: tell us where you're starting from —
it shapes where the conversation starts, never what you can ask or see"*; per-tile
sourcing-richness disclosures.

**2.2–2.3 Seating is emergent.** One world in the tray → Begin reads *"Begin a Deep
Interview with Chloe"*; two–three → *"Begin — Compare Worlds: Chloe, Yausep"*. The
1/2/3-seat table template renders silently to match the count (the participant is watching
their table get set); the Single/Multiple toggle is retired. Ceiling: 3 seats — the tray
simply stops adding, with a quiet line naming the table's limit; no 4/5 templates exist
[DECIDED — V1.0 §5.3; icon spec §1b].

**2.4 Role selector expanded** [BUILT · NOT MERGED · NOT VALIDATED — Battery A is the
gate]: four modes as pills — **Regular visitor · Pastor or teacher · Academic or scholar ·
Reevaluation** — plus **no role, the visual resting state** (never framed as lesser;
producing today's exact behavior byte-for-byte). One truth, four registers: mode changes
what's offered first, never what's reachable, never the propositional content ["One truth,
four registers" — Modes spec §2]. Role never appears again after S2 — no badge, no mention.
*(Code identifier is now `reevaluation` too — RESOLVED, executed in code 2026-07-18.)* Phone: bottom sheet.

**2.5 World-click menu** (tap a tile's name area): **Description · Tour · Choose for
Table · Academic Documents**. Tour + Academic Documents are honest visible placeholders
*here and nowhere else*. For a tour-qualifying world the Tour row is live; for a
non-qualifying world **the row itself answers plainly** — *"this world's own surviving
record does not preserve such a scene, and this project does not invent one"* — a
first-class mission surface, never an error [DECIDED — TourStrat §2.2]. Phone: bottom sheet.

**2.6 Proposed-table card** (question-first and guided flows only — the one T3 card): see
§R. **2.7 Proposal null case:** see §R2c.

### S3 — First question [DECIDED — V1.0 §5.4] + the routing states [NEW DESIGN — §R]

**3.1 Typed.** One input box; beneath it **theme chips, not question chips** — *An
ordinary day · How you looked from outside · What you never settled* — because no world is
seated yet to phrase a question at. A tapped theme runs the same router as a typed
question. **3.2 Silent begin.** Beginning without asking gets the Facilitator's ordinary
welcome; nothing is pushed. The data-layer invariant everywhere a starter is clickable:
**world-framed, never participant-framed** — enforced in the curriculum JSON ("None opens
with 'I'") because the relational-safety classifier has no transcript at turn zero; this
fired live [DECIDED — Curriculum header].

**3.3–3.6 What the participant sees while the Facilitator routes:** §R below [NEW DESIGN].

### S4 — The Table [DECIDED — V1.0 §4 as corrected; icon spec §1/§1a/§1b]

**4.0a The composed Living Table.** Composed once at conversation creation: the seated
worlds' **locked icons** (Chloe/cup · Papnoute/jug · Theon/scroll · Yausep/Gospel book ·
Albina/wax tablet) in the 1/2/3-seat template on the era ground — wooden table-edge arc
(solid, no dashed near edge), figures seated at Mark's tuned geometry (1: `50/8` · 2:
`40/8 & 60/8` · 3: `26/10 · 50/8 · 74/10`), nameplates on the table. **Fully static.**
Anti-ghost law: solid, opaque, connected figures; nothing glows, fades, dims, or moves.

**4.0b Who's speaking.** The speaking Representative's **nameplate inverts** (vellum/ink →
dark ground/light text) and reverts when they stop — the whole cue. Participant's and
Facilitator's turns leave every plate at rest (the Facilitator is not pictured; it
represents no one).

**4.1 The conversation (desktop).** One table bar (seats left as colored dots + names;
one consolidated status line right — refresh caution → session-cap notice, never
stacked). The transcript is **long-form, not texting**: a name above flowing prose — never
message bubbles ("we are not texting the R. voices, we are talking with them" — Mark,
2026-07-18). Facilitator centered-register italic graphite; Representative = gold
small-caps label (name · world) above full-width prose; participant = lapis "You" label,
italic. Left-justified column below the greeting, which pins just under the lowest
nameplate. Streaming pins scroll only when already near the bottom. Reading surface: the
warm-cream brand ground (`--gold-wash #FBF2E2`, current draft; era tint scoped to the
atlas) [DECIDED this session — icon spec §1b; V1.0 §4.1].

**4.2 Streaming turn.** The latest Representative turn owns visual priority; their
nameplate stays inverted while they speak.

**4.3–4.5 Depth on request (the one grammar).** Tyrian dotted-underline lexicon terms
(first occurrence only) and the ✲ citation marker at turn end. Hover = Level-2 card; click
= Level-3 **side panel** alongside the column (desktop) / **bottom sheet over the input
area** (phone, ~55% max, transcript visible). Zero modals; the panel is the no-modal
rule's own sanctioned exception ("cover the input area or open alongside") [DECIDED — IS
§2.2 r5]. Confidence language always behind the same hover/click.

**4.6 "Don't know what to ask?" → the question sheet** [content DECIDED — Curriculum
V1.0; UI BUILT NOWHERE — zero code in cic-poc; Increment 3, hard-gated on role selection
landing first]: a few motionless graphite words above the input's corner; the sheet slides
up **over the input area only**. The participant's role surfaces **their five walks
first** as tabs (e.g., Reevaluation: *Did any of you ever want to leave? · When it went
wrong among you · Doubt, and whether there was room for it · What you never settled · Say
the hardest thing first*); each walk is five questions in a deliberate order — a walk, not
a menu; jump anywhere. **"Show me everything"** is one tap away and exposes all twenty
sets to every role. No role = the General five first, same sheet, nothing missing.
Dismisses on typing or any transcript interaction.

**4.7 Suggested next-questions** (T3 default occupant) [OPEN — no validation owner; ships
nowhere until someone owns that]: 2–3 Facilitator-voiced chips, in-flow, quieter than any
turn; typing dismisses instantly; one-action "Stop suggesting for this conversation."

**4.8 Tour invitation** (T3, rare — outranks next-questions when it fires): one card,
consent explicit, "Not now" final for the session. Today this can only ever fire for
**Chloe** (see 4.T).

**4.9 Bridge turns** (anachronism bridge) [BUILT, merge-gated only]: ordinary Facilitator
(+ Representative) turns in the transcript grammar; no new UI.

**4.10 Safety posture active.** Conversational turns in a separate labeled governance
voice (Article 33); the T3 slot renders nothing; nothing else changes on screen.

**4.11–4.12 Status & errors.** One quiet status line in the table bar (phone: truncates,
tap-to-expand); errors inline beneath the bar, dismissible — never a toast, never a modal.

**Five-count (S4):** 1 primary (transcript+input; scene is ground) · 2 chrome · ≤1 card ·
0 modals · hover/click ✓ — both breakpoints [V1.0 §4.3, as corrected: nothing about the
scene moves or freezes; it is simply still].

*Phone (4.x):* the composed table appears **once as a load greeting** (welcome pinned just
under it) → the conversation takes the whole screen, long-form; **a top row of nameplates
(names only)** carries who's speaking by the same inversion. No camera, no chip. The seat
dots stay in the bar [DECIDED — icon spec §1a-phone; phone mockup approved 2026-07-18].

### S4-tour — a mode of S4, not a surface [DECIDED — TourStrat V0.3; BUILT as a
self-contained Chloe demo only; TR-14 integration NOT built]

> **DEFERRED TO PHASE 2 — not part of the current build cycle (2026-07-22).** Mark
> decided Hosted Tour is a second-tier (Phase 2+) feature, not something this launch
> builds, and directed that all Tour-related content be taken out of the current build
> cycle across documents, UX, and code planning. **This storyboarded design stays
> documented as-approved below** — not removed, since it's still the right design for
> when Phase 2 takes this mode up. **The world-click menu's Tour row (2.5, above)
> already degrades gracefully for the current build**: "honest visible placeholders,"
> and for a non-qualifying/unavailable world "the row itself answers plainly" with the
> refusal rather than opening anything — so it should currently render in that
> not-yet-available/refusal state, not as a live entry point, until Phase 2 actually
> builds this mode. No design change needed; it already assumed Tour might not be
> available.

Entry only by consent (the S2 Tour row, or the 4.8 invitation). Acceptance passes the
**threshold stop** — *what this is / what it's built from / what it will not claim* — with
the source cartouche, before any mode shift. Chrome = exactly three: the **register
strip** (Class A: *"A witness's own account — Justin Martyr, writing c. 155"* / Class B:
*"A reconstruction of typical practice…"*), the **beat tracker**, the **Exit door** (one
action, every beat, never framed as abandonment).

**The Chloe tour** (the only one that exists): *A Sunday Gathering in Rome, As Justin
Describes It* — The Door → The Day → The Reading → The Word → The Prayers → The Bread and
the Cup → The Collection → **"What We Cannot Show You"** (penultimate, first-class, four
documented declines: the room, the prayers' words, the people, the singing — Pliny's
report quoted with its cost named) → The Way Out (handback). A participant question at any
beat drops to ordinary conversational mode — full retrieval, all guardrails — and the tour
resumes only if wanted. Exit hands back to open conversation; never left "in a scene."

**The other live worlds, honestly:** Syriac — qualified yes (Class B, `syrstory009`),
needs a pronunciation pass; Desert — partial (daily-rhythm yes, **worship-service no** —
the synaxis is one attested sentence; that decline is a required feature); Bethlehem —
partial/thin, **no liturgical tour possible**, produce last; **Alexandria/Theon — tour
eligibility never assessed** (went live after the tour verdicts; the TR-5 checklist must
run before any Tour row goes live for it) [gap — flagged]. Until manifests exist, all
non-Chloe Tour rows render the honest refusal (2.5), not an error.

### S5 — The close [DECIDED — V1.0 §5.6]

Sequential beats, one on screen at a time, each skippable in one action; the T3 slot
renders nothing throughout. **Gracious close** (a Facilitator turn) → **"anything
else?"** (an open pause; a real new question evaporates the sequence back to normal flow)
→ **the reflection beat** — *"What stayed with you?"*, one optional question, private by
default, never a form; part of the closing sequence, shipping with the closing-sequence
build → **closing resources** — ask, never push; the offer names what was actually
discussed and lists nothing; a yes shows 2–3 genuine, checkable external pointers
(role-shaped register [BUILT world-agnostic, merge-gated]); a decline is a complete path →
**the door outward** — a comma, not a period; no claim on what comes after. *(When
accounts exist someday the pilgrim's-map return-marking lives here — [OPEN], gated on the
unmade accounts decision; noted as the connection point only, per instruction.)*

### X — Outside the stages

**X.1 Onboarding/consent** — the existing screen, brand-corrected copy, shown once before
any door; logging honesty verified live (Article 36). Open content item: one paragraph
mentioning role selection [OPEN — Modes status]. **X.2 Loading / pre-session errors** —
existing states restyled to the system.

---

## Part 3 · The two new designs, in full

### §G — Guided onboarding (the third door) [NEW DESIGN]

**Who it's for.** The participant who wants to be *walked in* — not asked to choose yet.
"Build your own table" assumes some starting confidence (a picker, a map, a tray);
"Start with your question" assumes a question. This door assumes only willingness.

**The design in one line:** the Facilitator walks you in with **three small beats — where
you're starting from, what draws you, and a table prepared for you** — then the standard
Begin. It reuses only decided machinery: the role pills (2.4), the theme chips (3.1), the
coverage-card routing (§R/Tier 1), the proposal grammar (§R2a), and Begin-as-consent.
Nothing new is invented below the surface; what is new is the *sequence and the register*.

**Register.** Hosted, first-person Facilitator ("I"), one beat at a time — the S5 grammar
(one thing on screen, everything skippable) applied to arrival. The hero's warm table
ground persists behind the beats. Quiet chrome (cap 2): a beat-position mark ("1 of 3")
and one standing escape line — *"You can just look around instead"* → the map (S1), or
*"I already have a question"* → the question door (S3). Cards 0 · modals 0.

**G1 — "Where are you starting from?"** Facilitator, two lines: *"Welcome. I'll walk you
in — three small questions, nothing binding. First: where are you starting from? It
shapes where we start — never what you can ask or see."* Five plain-language options
(the four modes + **"Just curious"** = no-role, the visual resting state, never lesser):
Regular visitor · Pastor or teacher · Academic or scholar · Reevaluation (rendered in its
plain participant-facing phrasing, e.g. *"I'm re-examining faith I once held"*) · Just
curious. Selecting sets the same session-constant role as 2.4 — one mechanism, two
surfaces. Skippable ("skip this" = Just curious).

**G2 — "What draws you?"** One line: *"What kind of thing would you want to sit with
first?"* The three theme chips (3.1's exact set — same router): *An ordinary day · How you
looked from outside · What you never settled* — plus **"Surprise me"** (the router treats
it as the role's first-walk theme). One tap; skippable (skip = Surprise me).

**G3 — The prepared table.** The Facilitator proposes **one world** (guided starts small
by design — a first sitting is a Deep Interview; more voices live one tap away) chosen by
the same Tier-1 coverage-card routing on theme × role — richest documented coverage wins,
reasons are sourcing reasons, never steering. Rendered in the decided proposal grammar
(§R2a): the world named with its sourcing reason; *one* prepared first question drawn from
the guided curriculum (the role's matching set, question 1 — world-framed by the hard
rule); who is *not* seated, with the real reason, when the theme touched a world's silence.
Actions: primary = the standard Begin line verbatim (*"Begin a Deep Interview with
Chloe"* — consent stays where it always is); secondary, quiet: *"Show me other tables"* →
S2 with the proposal in the tray, fully editable · *"See the whole map"* → S1. The
prepared question arrives at S4 pre-filled in the input — **editable, deletable, never
auto-sent** (agency: the participant sends their first word, always).

**Five-count (each G beat):** 1 primary (the beat) · 2 chrome (position + escape) · 0
cards (G3's proposal *is* the beat's primary surface, not a card over another) · 0 modals ·
hover/click on any confidence language ✓. Phone: identical beats, full-screen, options
stack; no divergence beyond stacking.

**What this door never does:** never shows the picker grid or the census (that's what the
other doors are for); never asks a fourth question; never re-presses a skipped beat; never
frames "Just curious" or skipping as lesser; never seats anything — Begin does.

**Build status:** [NEW DESIGN — no code anywhere; sequenced with the S0 three-door
threshold build (Phase 1); depends on role selection (Increment 2) for G1's persistence
and on Tier-1 routing for G3.]

### §R — Question-First entry: the Tier-3 routing UI [NEW DESIGN]

**What existed:** the three-tier routing backend (coverage cards → retrieval-probe
scoring → full pathway) and the proposal-turn copy grammar [QF §1–2]. **What didn't:** any
screen/state design for what the participant sees between pressing Send on their question
and having a proposed table. These are those states.

**R0 — The question, held.** On submit, the input collapses and the question re-renders as
a held line at the top of the column — label *"Your question, held:"* over the
participant's own words (lapis label, italic text — the same grammar as a "You" turn). It
stays visible through every following state: the participant never wonders what the system
is working from, and can tap it to edit — editing restarts routing.

**R1 — Considering (the honest interval).** One Facilitator line, its ordinary register:
*"Give me a moment — I'm looking at who can speak to this from their own record."* Below
it, a printed working-mark: three graphite dots that step (·· → ···), reduced-motion = a
still em-dash. **No spinner, no progress bar, no percentage** — nothing tech-forward. If
routing runs long (~6s), the line updates once, honestly: *"Still looking — the worlds'
records are uneven, and I'd rather check than guess."* If routing fails outright, an
ordinary inline error (4.12 grammar) with one action: *Try again* — never a dead end.

**R2a — The proposal (the common case).** The decided proposed-table card [QF §1 verbatim
model], now given its screen form: a single T3 card in the S2 stage. Anatomy, top to
bottom — (1) the Facilitator's proposal prose: which worlds can speak to this *from their
own sources*, one sourcing reason each; (2) **who is not seated, and the real reason**
(*"Syriac Christianity's sources don't document this — I won't seat a voice that would
have to invent an answer"*), with the world's name tappable → its panel (Level-2/3
grammar); (3) the proposed seats as tray chips — removable, reorderable, addable (the full
picker sits directly beneath: self-selection always visible, never behind a click); (4)
the primary action = the standard Begin line for the proposed count (*"Begin — Compare
Worlds: Chloe, Papnoute"*). One tap accepts; everything is editable; silence framing
follows the cards' rule — *"a silence is a proposal, not a refusal"*: a thin world the
participant insists on is seated with its thinness named, never silently dropped.

**R2b — Clarify-once (the ambiguous case).** When Tier-2 scoring is genuinely split, the
Facilitator may ask **exactly one** clarifying question — one line, 2–4 plain options +
free-type + a standing escape: *"Or I can simply propose something."* Hard rule: **never a
second clarifying beat** — one question in, one question back, then a proposal. (An
interview here would invert the product: the participant came to ask, not to be asked.)
Then → R2a.

**R2c — The honest null (the thesis case).** No world carries the question → a designed
moment, never an error [QF §1]: the Facilitator says so plainly; names **the nearest true
thing each world *could* speak to** as 2–3 tappable alternates (each re-runs routing as
that question, participant's words preserved above); points at the map with the real
reason (*"your question lives in the sixteenth century — that world isn't open yet, and
here's why"* → S1, the era in view); and offers Ask-the-Facilitator for the why-not
conversation. The held question (R0) stays on screen the whole time — the participant's
words are never discarded.

**Budget:** all R states live in the S3→S2 stages; the proposal is the stage's one T3
card; 0 modals; every confidence word behind hover/click. **Routing governance rendered,
not re-decided:** reasons are sourcing reasons; proposes, never seats; no theological
steering — a loaded framing routes on sources, not on the framing's politics [QF §4].

**Build status:** [NEW DESIGN over a designed-but-unbuilt backend — Tier 1 is
"prototype-ready" content + prompt work; no build started; exploration-branch discipline;
nothing merges before/during PT1.]

---

## Part 4 · Build-status honesty (what the app does TODAY vs. this storyboard)

The running `cic-poc` today: onboarding → world picker → Table (bubble transcript,
citations inline, anachronism bridge and closing sequence built but merge-gated).
Everything else in this storyboard is design, content, or branch work:

| Piece | Status |
|---|---|
| Three-door threshold (S0) · Guided onboarding (§G) · Tier-3 routing UI (§R) | designed (this doc + V1.0); **zero code** |
| Living Table scene + templates | assets locked, geometry specified (icon spec §1b); its own later increment |
| Long-form transcript, table bar, Level-3 panels, token/typeface swap | Increment 1 handoff, implementation-ready, **not merged** |
| World Map Tier A | **built & verified on branch**, closest to ready; Tier B open |
| Representative Modes (role) | built on branch, mock-verified only; **Battery A never run — the gate**; rename RESOLVED (2026-07-18) |
| Guided Questions | content V1.0 complete; **zero UI code**; Increment 3, hard-depends on role |
| Hosted Tour | Chloe demo built (self-contained); TR-4..15 pipeline + integration not built. **DEFERRED TO PHASE 2 (2026-07-22) — not part of the current build cycle; see §S4-tour above.** |
| Question-First backend | design note only; no build |
| Anachronism bridge · Sensed closing sequence | built world-agnostic, live-tested; **merge-gated only** (P1 rule) |

**Standing rule over all of it:** nothing merges before or during Prototype Testing 1;
merges land before invitation waves, never mid-pilot.

## Part 5 · Open questions preserved (rendered at current defaults, foreclosed nowhere)

1. Three-doors ceiling / map-as-door-form — Mark. 2. ~~`deconstructing → reevaluation`
identifier rename~~ — **RESOLVED 2026-07-18**, executed in code, no longer open. 3. T3
slot priority order — confirm/reorder. 4.
Validation owner for generated next-questions — unowned; feature ships nowhere until
owned. 5. Map Tier B (primary-surface) — observation-gated. 6. Accounts (gates
pilgrim's map, session memory) — the next structural decision after the increments. 7.
Mode One/Two transparency toggle — **designed nowhere** [placeholder note only, per
instruction]. 8. Reading-surface warm cream vs. era tint — settled direction this session
(reading = brand warm cream; era tint = atlas), owed a formal palette note.

## Part 6 · Gaps discovered while storyboarding (new, reported to the Hub)

1. **V1.0 stale camera/chip text** — ~20 spots. **FIXED (SB-4 closed, 2026-07-18
   overnight):** the body prose now reads the static/nameplate truth consistently
   (V1.0.2); every remaining "camera" mention is a negation or a historical log entry.
2. **"Four live worlds" is stale everywhere it appears** — five since 2026-07-17 (map
   legend "4 worlds open", first-visit overlay, several doc headers).
3. **Alexandria/Theon has no tour-eligibility assessment** — the TR-5 checklist must run
   before its Tour row can be anything but a placeholder.
4. **Tour stop numbering is inconsistent** across TourDesign (0–8) / TourLog / TourHub
   ("nine stops") / the demo (13 steps) — harmless but worth one reconciliation line.
5. **Naming gap on record:** Chloe's own voice won't use "house church" as a category,
   but the Facilitator's introduction names the world "The House-Churches" aloud — a live
   inconsistency at the S4 greeting, owner: world/facilitator threads.
6. **Map first-visit overlay + legend counts** predate the five Selected worlds
   (Amendment A) — "2 named for the future" is stale.

## Mockups

Companion artifact (five frames only, everything else stays descriptive): **S0 three
doors · the atlas as an entry surface · S2 tray at 1/2/3 (emergent template swap) · the
composed Living Table mid-conversation, one nameplate inverted · the Guided Questions
sheet open.** Each frame carries its build-status flag so nothing reads as "the app does
this today."

---

## Document log

- **Correction (2026-07-19):** this document described the `deconstructing → reevaluation`
  identifier rename as open in four places (terminology note, role-selector state 2.4, the
  build-status table, and the open-questions list). It was actually **resolved the day
  this storyboard was written** — executed in code 2026-07-18 on the Representative Modes
  branch (commit `9774447`), approved by Mark — the storyboard just hadn't caught up.
  Corrected in place per `CiC_Guided_Questions_Decision_Log.md`'s 2026-07-18 entry, which
  names this document's governing counterpart (`CiC_Full_UX_Design_V1_0.md` §10) explicitly
  as one of the things it closes. Found while compiling the Bedrock/pilot readiness report;
  see `CiC_Full_UX_Design_Decision_Log.md` for the full note.
- **V1.0 approvals (2026-07-18, morning after):** **§G and §R are APPROVED** (Mark: "both
  are approved to move forward") — the [NEW DESIGN] flag on both now reads as approved
  design, recorded in V1.0 (states G.1–G.3 / R.0–R.2c). The **side "other choices" are
  DROPPED** per the review recommendation (Mark: "drop the side choices") — icon spec §1b
  and V1.0 §4.1 carry the ruling.
- **V1.0 (2026-07-18):** First complete storyboard. Sources read in full via two
  extraction passes (entry/questions/modes; map/tour/IA/readiness) + the V1.0 backbone,
  icon/table spec, and this thread's decision log directly. New design: §G (Guided
  onboarding) and §R (Tier-3 routing UI) — everything else cited to its governing record.
  Corrections honored: static Living Table (no camera/chip; nameplate inversion only);
  five live worlds. Logged in `CiC_Full_UX_Design_Decision_Log.md`; Hub hand-off:
  `CiC_UX_Storyboard_System_Hub_Update_2026-07-18.md`.
