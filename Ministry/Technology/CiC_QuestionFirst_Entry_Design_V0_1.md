# Question-First Entry — Design Note V0.1
## "Start with your question" as a co-equal door, with the Facilitator proposing the table

**Status:** Design note for Mark, 2026-07-16. Front-end thread's domain to build.

**Continuity, not invention:** the Pre-Encounter Experience Design already
specifies three co-equal entry pathways — Bypass ("straight to question"),
Build Your Own Table (pick worlds), Guided Onboarding — confirmed as a match to
Mark's own phrasing in the front-end log, 2026-07-07. This note gives the
question-first pathway its missing mechanics: how the Facilitator actually
knows which worlds can answer a given question.

---

## 1. The choice architecture (participant-facing)

Two doors at entry, equal visual weight, no default (per the governing design;
the map is a third, orientation-shaped door):

- **"I know who I want to talk to"** → world selection as today (tiles or map).
- **"Start with your question"** → one input box. The participant types what
  they're actually wondering. The Facilitator responds with a **proposed
  table** — and this is the heart of the feature:

> *"Three of the four open worlds can speak to this from their own sources.
> The Desert Fathers and Mothers speak to it most directly — the struggle you're
> describing is nearly their whole surviving literature. The House-Churches
> touch it where community life met suffering. The Bethlehem Circle only at its
> edges. Syriac Christianity's sources don't document this — I won't seat a
> voice that would have to invent an answer. Shall I seat the first two, just
> the Desert, or would you like to choose differently?"*

**The invariant, inherited from the map:** *the Facilitator proposes, never
seats.* One tap accepts the proposal; the proposal is editable; the participant
can always override into full self-selection. Participant agency is untouched —
what the feature removes is the burden of knowing four worlds' source ecologies
before asking a first question.

**The honesty feature inside it:** the proposal names the worlds NOT seated and
the real reason — "no documented sources on this" — the same
transparency-of-absence grammar as everywhere else. And the null case is a
designed moment, not an error: if no open world carries sources for the
question, the Facilitator says so plainly, offers the nearest true thing each
world *could* speak to, and points to the World Map ("your question lives in
the sixteenth century — that world isn't open yet, and here's why").

## 2. The routing mechanics (how the Facilitator knows)

Three tiers, buildable in order, each honest at its own level:

**Tier 1 — World Coverage Cards (prototype-ready now).** A hand-authored,
per-world routing summary derived from materials that already exist: the
manifest's sourcing-richness disclosures ("richest in… thinner on…"), the
Facilitation Briefs' caution zones, and the Story Inventories' own "stories
this world cannot tell" sections. Shape: strengths (themes the world answers
from documented evidence), edges (answerable but thin — flag in the proposal),
silences (decline honestly), cautions (route carefully — e.g., Aphrahat's
polemics). The Facilitator's existing classify-then-route architecture (already
tested, per the constitution-investigation entry) takes the question + four
cards and drafts the proposal. This is prompt-layer work plus four content
cards — no new infrastructure.

**Tier 2 — Retrieval-probe scoring (quantitative honesty).** The per-world
vector stores already exist (pahc, syriac, desert, hal). Run the participant's
question as a retrieval probe against each store; retrieval strength becomes an
evidence-availability signal that grounds and checks the Tier 1 judgment — the
difference between the Facilitator *believing* a world is silent and having
*looked*. Guards against coverage-card staleness as worlds grow.

**Tier 3 — The full pathway UI.** The three-door entry built as designed
(equal weight), the map's handoff contract extended with a question parameter,
and the Guided Questions feature's starter sets wired in: a participant who
doesn't know what to ask taps a starter question and flows straight into this
same routing.

## 3. Synergies already in flight (route these, don't duplicate)

- **Guided Questions thread:** its Deliverable 3 desk-checks every starter
  question against every world's materials — that question × world
  answerability matrix IS Tier 1 routing seed data. One study, two features.
- **Representative Modes thread:** role arrives at the same session start;
  a Reevaluation participant's question may route identically but the
  *proposal's register* adapts.
- **World Map branch:** the null case and the "not seated because" explanations
  link into the map's existing honesty copy; the handoff contract
  (`/?worlds=…&mode=…&role=…`) gains `q=` when Tier 3 lands.
- **Ask-the-Facilitator** (already decided): same voice, adjacent moment —
  pre-threshold Q&A about the project vs. question-first entry INTO an
  encounter. Keep them distinct but voiced identically.

## 4. Governance check (clean, one watch-point)

Serves Article 6 directly (arriving at a world with honest expectations);
Conviction 4 (absence explained); participant agency preserved by
propose-never-seat. **Watch-point:** routing must never become steering —
the Facilitator proposes on *evidence availability*, never on where it thinks
the participant *ought* to land theologically. The proposal's reasons must
always be sourcing reasons. Validation should probe this (a question with
loaded framing should route on sources, not on the framing's politics).

## 5. Build path recommendation

Tier 1 is small enough for the Modes thread's exploration branch or its own:
four coverage cards + one facilitator routing prompt + the proposal turn.
Live-test with the four worlds against a battery of real questions (borrow the
Guided Questions study's sets when they exist). Tiers 2–3 follow the standing
discipline: exploration branch, verified live, merged only after Prototype
Testing 1 on the front-end thread's schedule.
