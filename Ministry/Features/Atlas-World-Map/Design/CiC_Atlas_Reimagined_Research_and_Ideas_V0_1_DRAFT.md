# Atlas Reimagined — Research & Ideas (game-grade, animated, connected)

**Status: RESEARCH / IDEATION THREAD. Does not build.** No code changed, no census
edited. Everything below is for Mark's read; nothing here is authorized to ship.

**Date:** 2026-08-31. **Governing chain:** Vision V1.1 → Constitution → Brand
Foundations → `CiC_Full_UX_Design_V1_0.md` → this thread proposes; it decides
nothing. Where an idea would touch a locked visual or motion decision, that is
named as a trade-off, never assumed.

**Mark's brief, his own words:** *"the atlas/map we have is good, but i want to
explore the idea of better graphics, linking and sourcing as a way to help
people see the big picture and not get overwhelmed... i am thinking updated
age of empire details, or even other games that have these interactive worlds
that each have features and connect with eachother."*

**The heart of it, as this thread reads it:** church history is huge. The map
is how a person should be able to *see* the whole story at once — eras,
worlds, and the real connections between them — and then step into any one of
them without feeling lost. Game-grade visual richness in service of
comprehension and invitation. Not a game.

---

## 0. How to read this document

Four parts:

1. **§1–2** — the honest baseline. What the Atlas already does (more than it
   might look like from the outside) and the two disciplines every idea below
   has to survive.
2. **§3** — what the corpus itself actually attests about worlds touching each
   other, checked against real files, not assumed.
3. **§4** — the research survey: games, interactive worlds, and non-game craft,
   each read for mechanism, not aesthetics.
4. **§5–7** — the idea portfolio, organized by zoom level, each idea scored on
   what it costs and what it trades against.

---

## 1. The baseline — what `atlas-v3.html` already does

Before imagining past the current Atlas, its actual sophistication, read
directly from `cic-website/atlas-v3.html` and `cic-website/data/world-census.json`
(schema V0.20+, 292 entries, 69 sourced relationship edges):

- **It is already a connected map, not a decorated timeline.** Every
  relationship line ("thread") the map draws comes from a reviewed edge record
  carrying a `type` (`formed` · `transmitted to` · `contemporary with` · `in
  tension with` · `argued against`), a `confidence` (`Documented` ·
  `Widely Accepted` · `Contested`, contested also rendered dashed), and a
  sourced `note`. The code's own comment states the rule plainly: *"the map
  never draws a thread it can't defend."* Where no edge exists, the click
  panel says so in words rather than showing an empty map.
- **Hover already traces a lineage.** Hovering or tapping a world dims
  everything else and highlights every thread touching it, with the edge's
  *type* printed as a label along the line itself — this is, mechanically,
  the same "focus-and-dim" interaction Crusader Kings III and a tech tree use
  (§4 below), already built.
- **Click already opens a full relational dossier.** The click-sheet groups a
  world's connections into *Influenced by*, *Influenced*, *In tension with*,
  *Contemporary with*, plus continuity chains (`continuesAs` — "the same
  ongoing church, next era") derived live from the census, never hand-kept.
- **Ten eras, each with an approved ground color** (`CiC_Full_UX_Design_V1_0.md`
  §2.5c) that the Atlas is slated to adopt "when next edited — the map→brand
  palette convergence." That convergence has not happened yet; it is real,
  approved, waiting work, not a new idea.
- **Two axes of filtering already exist independently:** tradition
  family/lane (13 hues) and geographic region (Mark, 2026-08-04: *"use actual
  regions... if they show up in more than one they are included"*). A list
  view mirrors the same live filters as a scannable table.
- **The launch grammar is already decided and built** (Decision Log,
  2026-08-28): the Atlas is a *discovery* surface that never creates a
  session itself. Clicking through hands off via `?worlds=<id>&mode=interview`
  (straight into conversation, frictionless, cheap) or `?worlds=a,b&mode=table`
  (seats chosen, one deliberate "Convene the Table" action, more expensive,
  more intentional). **Any idea below that inserts a screen between "click a
  world" and "begin talking" has to answer to this ruling** — Mark's words:
  *"if you launch an interview from the atlas it should go straight into the
  conversation, not to a waiting place."*
- **Prior visual-history research already happened in this exact workstream**
  (`Decision-Log.md`, 2026-07-16): Priestley's *Chart of Biography* (1765) for
  figure lifespans, Adams' *Synchronological Chart* (1871) for parallel
  streams — both real precedent, already adopted in spirit (the vertical
  time-flow, the lane structure). Susan Histomap (1931) was **considered and
  rejected** because its width-as-importance encoding is "an unearned
  historical claim." This thread does not redo that survey; it extends it
  into game and interactive-world mechanisms specifically, which that pass
  did not cover.

**What this means for the brief:** the gap Mark is naming is not "we have no
connections" or "nothing is sourced" — both exist and are handled with more
rigor than most professional history-viz products bother with. The gap is
**scale and legibility at a glance**: 292 entries and 69 edges, plus everything
a world *contains* once you're inside it (its gravities, figures, sources,
stories), rendered as a single dense vertical scroll of small boxes. "Better
graphics, linking and sourcing... to help people see the big picture and not
get overwhelmed" is a comprehension problem at scale, not a trust or
data-sourcing problem. That reframes what "game-grade" should actually buy:
not more content, but a *navigable hierarchy* over content that already
exists — which is exactly what strategy-game campaign maps are built to solve
(§4).

---

## 2. Two disciplines every idea below has to survive

The launch brief names these explicitly and asks that any idea bending either
one say so out loud rather than quietly drift. Both are read directly from
`CiC_Full_UX_Design_V1_0.md`.

### The anti-ghost principle

Mark's rule, quoted in the design doc verbatim: *"these must feel like real
people at a table, not spirits or ghosts… no lighting or glow."* It governs
**everything visual with a figure in it** — the five locked world icons, the
Living Table composition. Enforced by: figures solid and opaque, present the
whole time; a speaker shown by nameplate inversion, never glow/fade/dim/
vignette/transparency.

**Scope check, important for this thread:** the rule is scoped to *figures*.
The Atlas's boxes, threads, and era grounds are not figures — they are
already-abstract cartographic marks (same register as a map's ink, not a
person's portrait). A glowing connection-line or a particle-trail effect on
the *map itself* does not violate anti-ghost by the letter of the rule. It
can still violate the *spirit* of "no lighting or glow" as a house style, and
it collides harder with the stillness posture below. Every idea that adds
shine, glow, or motion to map chrome is flagged so Mark can rule on it
directly rather than this thread assuming the figure-scoped rule clears it.

### The stillness / reduced-motion posture

This design treats motion as **rare and meaningful, not ambient**. The
clearest evidence: the Living Table's camera was built, tested, and then
*removed* (Mark, 2026-07-18, on seeing the real thing): "the composed scene
does not pan, zoom, or move at all... no glow, no vignette, and NO dimming of
the others." `atlas-v3.html` itself already honors
`prefers-reduced-motion: reduce` by killing every transition and animation
outright. The default posture across this whole product is: **the page is a
printed thing that responds to your attention, not a screen that performs at
you.**

**What this rules out by default:** ambient parallax, idle pulsing "look here"
affordances, auto-panning cameras, particle/shimmer effects that play without
being asked for, anything that runs *while the participant is reading* rather
than *because they acted*. What it does not rule out: a state change that
happens once, on a deliberate participant action (a click, a hover, a filter
toggle) and then holds still — which is exactly the register the Atlas's
existing hover-trace and click-sheet already use, and the register every idea
below is written in unless flagged otherwise.

---

## 3. What the corpus actually attests — checked, not assumed

The brief asked this be checked against real files in two worlds' records,
with one question in mind: what real cross-world connections does the corpus
already attest, sourced like everything else? Four findings, all verified
against files under `records/`:

1. **A sourced council record already exists and is stronger than the census
   edge that stands in for it.** `records/alx/doctrinal_witness/alx.dw.councils.md`
   sources Nicaea to Athanasius's *De Decretis* (whole work) and Eusebius's
   *Historia Ecclesiastica* (VII.24), with a real tension preserved in the
   record itself: *"I've heard a council voted Jesus into being God"* —
   answered by the council's own participant, that the vote fenced existing
   worship. This is richer than a one-line edge note; a map-level "click
   Nicaea, see who was actually there and what each world's own record says
   about it" view has primary material to draw on today, in one world at
   least. It does not yet exist in the other five built worlds' records —
   real, bounded work, not a rendering problem.

2. **Two worlds already cite the same primary source independently.** Both
   `records/alx/source/alx.source.eusebius-historia-ecclesiastica.md` and
   `records/pahc/source/pahc.source.eusebius-historia-ecclesiastica.md` exist
   as separate, independently-built citations of the same ancient text. The
   census's edge schema has no vocabulary for this today — its five `type`
   values are all about one world acting on another (`formed`, `transmitted
   to`, `contemporary with`, `in tension with`, `argued against`). "Both
   worlds are known to us through the same eyewitness" is a different, real,
   and legitimately interesting kind of connection with no current home. See
   §6.

3. **A genuine cross-world "handoff" is already modeled, deliberately without
   invented connective tissue.** `records/pahc/force/pahc.force.alexandria-emergence.md`
   records that Alexandria (World #2) emerges independently around 190–254 CE,
   overlapping only the final decade of the House-Churches world, and states
   outright that this world's *own* sources never register Alexandria's
   emergence as a felt pressure. The record's own discipline: *"a genuine,
   evidence-supported handoff rather than a contradiction requiring
   resolution... not a claim this world's own evidentiary base can itself
   ground."* This is the corpus's most honest possible statement of a
   connection — two worlds meeting at an edge, without either one's record
   overclaiming contact it never had. Any visual for "connection" needs a
   way to draw *this* — proximity without asserted mutual awareness — as
   distinct from "documented influence." The census's `contemporary with`
   type currently collapses both into one thread style.

4. **A figure's authority already crosses worlds without the worlds ever
   "meeting."** Athanasius belongs to Alexandria (`records/alx/figure/
   alx.figure.athanasius.md`) — yet his *Festal Letter 39* is independently
   cited as a source inside the House-Churches world's own record
   (`records/pahc/source/pahc.source.athanasius-festal-39.md`), because it is
   the earliest list of the New Testament canon and pahc's canon-formation
   thread needs it. One person, cited by two worlds' own construction
   records, for two different reasons. This is a third connection shape —
   *shared figure, independent relevance* — again with no current edge type.

**Read together:** the corpus already supports a richer connection grammar
than the map currently exposes — not because sourcing is thin, but because
the census's edge model was built for "who formed/influenced whom" and the
real record also contains "known through the same witness," "adjacent without
contact," and "cited by, for unrelated reasons." Surfacing these as
*visually distinct* connection kinds (never collapsed into one generic line)
is itself a legibility win with no new invented content — the sourcing to
support it already exists in at least these four cases, and the discipline
that produced `pahc.force.alexandria-emergence.md` (silence stated as
silence, nothing inferred to fill a gap) is exactly the discipline a bigger
connection grammar has to keep.

**Also worth naming — a second, different meaning of "connect" already lives
in this project, and must never be visually confused with the above.**
`Ministry/Technology/CiC_Table_Pairings_V1_2026-08-28.md` (the C6 record)
recommends which worlds sit well together *at the Table* — and its own
"no-foreknowledge rule" states plainly that *historical acquaintance between
traditions no longer matters to the mechanics — what matters is contrast of
formation, which is what the participant came to witness.* Alexandria+Desert
is offered first because the intellectual-textual and ascetic-embodied modes
contrast productively in conversation, not because the map draws a thick
line between them (though it happens to, on real historical grounds — they
share a `formed`/`Widely Accepted` edge). Hal+Desert is deliberately *harder*
to offer well because the two are nearly historically simultaneous and
similar, which is a reason for caution at the Table, not a reason for a
strong map connection. **A "these worlds connect" map idea must keep these
two axes — sourced historical relationship, and Facilitator-curated
conversational contrast — visually and linguistically separate.** Conflating
them would let a real historical claim quietly become a matchmaking
recommendation, or vice versa; the Vision document's own warning against
"interchangeable paths to a generic Jesus" is exactly the failure mode this
guards against.

---

## 4. The research survey — mechanism, not aesthetics

Read for what each does to make something huge legible, what it would map to
in *our* data, and what it costs. Runtime constraint carried through every
row: **$0 generative — static/client-side only**, so "cost" below means build
effort, never a per-use runtime bill.

### Strategy-game campaign maps

| Reference | Mechanism | Maps to, in our data | Cost / trade-off |
|---|---|---|---|
| **Crusader Kings III** — map modes (Realms / de jure Empire / Kingdom / Duchy, toggled from one control) plus character-relation webs, opened from a person, dimming everyone not connected | One dataset, several *lenses* over it, switched with one click; a focus-and-dim interaction identical in spirit to the Atlas's existing hover-trace | The Atlas already has two lenses (lane, region). A third lens — **connection density**, or **"what's sourced vs. contested"** — is the same mechanism at zero new interaction cost; the toggle control already exists | Cheap: new coloring rule over data already in `world-census.json`, no new UI grammar |
| **Civilization**'s tech tree | A dependency graph rendered as a legible tree: what unlocks what, one line per real dependency, zoomable from "the whole tree" to "one tech's detail card" | The `formed`/`transmitted to` edges are already a dependency graph (`parentsOf`/`childrenOf` are already built in the Atlas's own JS, in memory, unused as a *tree layout* — currently only used for hover highlighting) | Real but bounded: a tree/DAG layout algorithm over an already-existing graph; no new data |
| **Age of Empires IV**'s "Hands-on History" — short documentary interstitials between missions, cutting to footage of the real historical site behind the next campaign | Bridges the game's abstraction back to the real, physical, checkable world at exactly the moment interest peaks | We already have this content, unused as a *bridge* — `world-census.json`'s `experienceToday` field (e.g., the House-Churches entry links the real Dura-Europos house-church excavation and its surviving paintings at Yale) sits inert at the bottom of a click-sheet | Free-to-cheap: surfacing already-authored, already-sourced content more prominently is a layout change, not new research |
| **Slay the Spire / Hades** — a branching path map where the *next* few nodes are visible and their *kind* is previewable (a fight, a rest, a shop) before you commit, but the far map stays a silhouette | "There is more here" signaled by shape and icon, never by blocking or teasing unearned content | The Atlas's own existing icon system (house/plans/question/closed-door) already does exactly this — a "Plans" or "Question" world is a previewable, honestly-labeled not-yet. The *shape* of "more lies beyond what's built" is already solved; only the zoomed-out framing is not | None — this is a naming exercise, not a build |

### Non-game, closer to CiC's own register

| Reference | Mechanism | Maps to, in our data | Cost / trade-off |
|---|---|---|---|
| **Stanford ORBIS** (`orbis.stanford.edu`) — a scholarly, sourced network model of Roman-world travel: 632 real sites, routes costed by time/money/season, built by a Digital Humanities grant, zero game framing anywhere | Proof that "interactive, connected, and computed" can sit entirely inside an academic register with no games vocabulary at all — closest existing analogue to what this project is | Its "compute a route between two points, show the real cost" mechanic maps directly to §6's proposed "path between two selected worlds" feature | Real if attempted at ORBIS's own rigor (route costing); cheap if attempted as pure graph adjacency (which is what our data actually supports today) |
| **Pelagios / Peripleo** — a linked-open-data map where places are the connective tissue between independently-curated resources (texts, museum objects, images) from different institutions, filterable by time/source/type | The exact shape of finding #2 and #4 above: the same *thing* (a place, a text, a person) cited independently by separate curated resources, made explorable through that shared reference point rather than a hand-drawn line | A "click Eusebius's *Historia Ecclesiastica*, see every world whose own record cites it" view is Peripleo's mechanism, applied to our sources instead of their places | Real: needs a reverse index from `source_id` → worlds citing it, buildable from existing `records/*/source/*.md` frontmatter with no new research |
| **Museum interactive timeline walls** — large touch surfaces, tap-a-node reveals layered depth (text → image → video), explicitly designed to "highlight turning points and connections between events" rather than list every event with equal weight | Depth-on-demand at exactly two or three tiers, matching the design system's own hover=short/click=full grammar already | Nothing new mechanically — the Atlas already does this. Worth naming because it confirms the *hierarchy of attention* (a few turning points foregrounded, the rest reachable but quiet) is the professional museum answer to "don't overwhelm," not more visual density | None — validates staying the current course on information hierarchy rather than adding graphic weight everywhere at once |
| **NYT / The Pudding-style scrollytelling** — a guided, authored path through a dataset, where the same map recomposes itself as the reader scrolls, before handing them back to free exploration | A single authored "walk" through the same underlying data, distinct from open exploration of it | This is, structurally, the same shape as the app's already-designed **role's five walks** (`CiC_Full_UX_Design_V1_0.md` §4.1, the question sheet) — a curated path through the same material a participant could otherwise browse freely. A "guided walk through the Atlas" (e.g., "the arc of the church," matching C6's own P2 pairing language) is this mechanism, reusing a pattern the UX design has already legitimized elsewhere | Moderate: authoring effort (a handful of curated sequences through existing, already-sourced entries), no new visual system |

---

## 5. The idea portfolio, by zoom level

Ordered whole story → era → world → a world's own features, per the brief.
Every idea names its mechanism-source from §4, what it costs, and whether it
touches §2's disciplines.

### L1 — The whole story (all ten eras at once)

- **A second map mode: "Connections" view**, toggled the same way lane/region
  filters already toggle (CK3 mechanism). Instead of coloring by family, dim
  every box to a neutral tone and let *edge density* carry the color —
  worlds with many sourced connections read visually "thicker," worlds with
  few read quiet. Answers "where is there more to find" honestly, since
  density is a real property of the reviewed record, not a decoration.
  *Cost: cheap — a coloring function over `DATA.edges`, no new data, no new
  interaction.* *Disciplines: clean on both — no figures, no motion added.*
- **A connection-type legend, always visible, not just discoverable on
  hover.** Right now a participant learns `formed` vs. `contemporary with`
  vs. `in tension with` only by hovering a specific thread. A short legend
  (the map already builds one for categories/regions) would let someone
  read the *kind* of every line at a glance before touching anything —
  directly serving "help people see the big picture," since right now the
  big picture's connective tissue is illegible until you've already
  zoomed in. *Cost: cheap — the glossary-generation pattern already exists
  in code for two other axes.*
- **Orbit/constellation overview as an alternate whole-map mode**, not a
  replacement — think a single screen showing ten era-clusters as
  constellations with only their *strongest* (Documented, high-degree)
  connections drawn between clusters, deep-linking down into the existing
  vertical timeline for any era clicked. This is the museum-wall "turning
  points foregrounded" mechanism (§4) applied at the whole-map level, and
  the direct answer to "not get overwhelmed" — a legible summary that
  *earns* the detailed view rather than starting there. *Cost: real — a
  second, hand-tuned layout and a new top-level state, though it can reuse
  every existing data structure and click-sheet.* *Disciplines: clean if
  static; would need a deliberate, once-only transition (not an idle
  animation) if the two views cross-fade, which is the kind of "rare and
  meaningful" motion the stillness posture explicitly allows — flagged
  because it is still a real motion decision Mark should rule on, not
  default into.

### L2 — An era

- **Ship the already-approved era-ground palette convergence** named in
  `CiC_Full_UX_Design_V1_0.md` §2.5c ("the atlas adopts them when next
  edited"). Not a new idea — the single highest-leverage, lowest-risk visual
  upgrade available, since it is already decided and only waiting for this
  page's next edit. Any "game-grade" pass that skips this first is choosing
  new graphics over a shipped decision. *Cost: near-free — ten approved hex
  values already exist per era.*
- **Era transition as one deliberate beat**, not ambient scroll-linked
  motion — e.g., the era header (already sticky, already carries dates and
  key events) gets a single, non-looping visual settle the first time an era
  scrolls into primary view, then goes fully still. This is the "alone ·
  built · seated · breathing, once per arrival, then stillness" pattern the
  logo's own approved motion brief already uses (`CiC_Logo_and_Motion_Brief
  _V1_0.md`), reapplied to era arrival instead of page arrival. *Cost:
  moderate — a real animation to design and gate correctly against
  `prefers-reduced-motion` (already wired). Disciplines: this is the
  clearest place in the whole portfolio where "rare and meaningful" motion
  is defensible on the design system's own precedent — but it is new motion
  on a surface that currently has none, and should be named to Mark as
  exactly that, not folded in quietly.*

### L3 — A world

- **The click-sheet becomes a dossier, not a new screen.** The 2026-08-28
  ruling (§1) forbids inserting a waiting place between "click a world" and
  "begin talking" — so this idea deliberately does not propose a new
  interstitial. It proposes making the *existing* Level-3 click-sheet (which
  already carries `longDescription`, `voices`, `legacy`, and relations)
  visually richer within itself: the world's locked icon given real
  presence at the top of its own sheet (it is already built, already
  anti-ghost-cleared, currently used only as a small emblem), its `voices`
  list rendered as named citations rather than a bullet list, its relations
  visually split into the three kinds §3 surfaced — sourced historical
  connection, "known through the same witness," and Table-pairing contrast
  — each in its own labeled section so a participant can tell which kind of
  "connection" they're looking at. *Cost: moderate — layout work on an
  existing surface, one new data join (source → world reverse-index, §6),
  no new interaction grammar, no new screen to reconcile against the
  launch ruling.*
- **Name the Table-pairing invitation where a historical edge already
  exists**, distinctly. Where two worlds share a real `formed` or
  `transmitted to` edge *and* appear together in the C6 launch set (e.g.
  Alexandria+Desert), the dossier can honestly say both things in two
  separate lines — "the reviewed record shows X" and, separately, "the
  Facilitator's own judgment offers these two together, for contrast" —
  without merging them into one claim. Where a C6 pairing exists *without*
  a historical edge (contrast pairings don't require one, per the
  no-foreknowledge rule), the dossier says only the second thing. *Cost:
  cheap — a lookup against the small C6 table; the discipline is in the
  copy, not the code.*

### L4 — A world's own features (its people, its gravities, its sources, its stories)

The corpus already organizes each world into exactly these facets —
`records/<world>/figure/`, `gravity/`, `source/`, `story/` — so this zoom
level is not invented; it is the corpus's own ontology, currently
unexposed on the map (the click-sheet surfaces `voices` and
`longDescription`, a flattened prose version of some of this, but not the
structure itself).

- **A per-world "constellation" sub-view**: the world's icon at center
  (static, locked, anti-ghost-clean already), its figures as satellite
  points around it. Clicking a figure surfaces exactly the already-decided
  answer from the 2026-07-16 map spec: *a single person's exact voice can't
  be honestly reconstructed; the world that formed people like them can be*
  — the map's own existing teaching moment, given a real home instead of
  living only in a hover tooltip. *Cost: real — new sub-view, new
  micro-layout (a handful of points around a center, not a force-directed
  graph — deliberately simple), but zero new research: every figure file
  already exists and is already sourced.*
- **Its gravities, shown as the world's own stated center(s) of gravity**,
  not as game "stats." `records/<world>/gravity/*.md` already names each
  world's real theological/formational tensions (e.g., alx's
  `teacher-bishop-tension`, `learning-community-tension`). Rendering these
  as short, sourced statements anchored to the world's dossier — never as a
  bar, meter, or score, which would read as a game mechanic quantifying
  faith — is a direct, honest answer to "features that connect with each
  other": two worlds sharing a named tension (e.g., authority migrating
  from teacher to bishop) is a real, comparable, sourceable thing, and
  currently invisible anywhere on the map. *Cost: moderate — this is a real
  authoring/mapping pass over existing gravity records into
  participant-facing language, not a rendering problem.*
- **Sources as a visible citation trail out to the real world**, reusing the
  `experienceToday` field already authored and already linked (Dura-Europos,
  Yale's baptistery paintings, etc.) — the AoE4 "Hands-on History" mechanism
  (§4), at zero new research cost, currently under-surfaced at the bottom of
  a click-sheet most participants never scroll to.
- **Stories, tiered honestly** — if a world's story repository (Doc_09
  discipline: tiered narrative material, hagiographic content clearly
  labeled) is exposed at all on the map, it must carry the same tier
  labeling the repository itself requires, never presented as flat fact.
  *Flagged as the one L4 idea genuinely gated on separate, in-progress work
  (the story-repository build for each world), not on map design.*

---

## 6. The bigger swing — a real connection-legibility upgrade

Two ideas above L1–L4 in ambition, named separately because each is a real
build, not a styling pass, and each is squarely what "linking... to help
people see the big picture" is actually asking for.

**A. Path-finding between any two selected worlds.** The Atlas's own code
already builds `parentsOf`/`childrenOf` graphs and a `continuesAs` chain in
memory at boot — currently used only to answer "what touches this one world."
Extending that to "show me the path between world A and world B" (a short
breadth-first search over a graph that already exists, capped at a small
number of hops so a "no meaningful path" answer stays honest rather than
reaching) is the ORBIS mechanism (§4) applied to lineage instead of travel
time. It directly serves comprehension at scale: instead of scanning 69 edges
by eye, a participant asks the map a question and gets a sourced, traceable
answer. *Cost: real but bounded — pure client-side graph search over data
already loaded, no server, no new sourcing; the interaction (pick two worlds,
see the chain) is new UI, not a new visual system.*

**B. A richer connection grammar, sourced from the corpus, not invented.**
§3 found three connection shapes the current five edge `type`s can't express:
*shared source* (two worlds independently cite the same text), *shared
figure* (one person cited by two worlds' own records for unrelated reasons),
and *adjacency without asserted contact* (the `pahc.force.alexandria-
emergence` shape — overlap the record itself refuses to claim as influence).
Adding these as real, visually distinct line/mark styles is bounded,
honest work: the two Eusebius citations and the Athanasius Festal 39
citation already exist as sourced facts today; nothing new needs to be
researched to draw at least those. Extending it further (checking whether
the same shared-source pattern holds across all six built worlds) is a real,
scoped research pass this thread flags for a future thread, not an
assumption this document is making. *Cost: moderate for the schema and the
three cases already found; real and open-ended if extended to all six
worlds' full source lists — a scope decision for Mark, not a default.*

---

## 7. What this thread recommends leaving alone

Named because "game-grade" as a brief invites these, and each would cut
against a decision already on record:

- **No XP, unlocks, achievements, or progress bars.** The map's existing
  icon vocabulary (house/plans/question/closed-door) already signals "there
  is more here" honestly; framing unbuilt worlds as things to be "unlocked"
  reframes witness as a game reward, which is precisely the encounter-vs-
  persuasion line the Vision document draws (`Encounter Over Persuasion`:
  *"the goal is not agreement... not validation"*) — an unlock mechanic
  implies a designed sense of accomplishment the project has no business
  manufacturing around faith content.
- **No AI-generated "scene" art for eras or worlds**, however tempting for a
  "game-grade" visual pass. Already explicitly ruled out in the brand brief:
  *"never AI-generated scenes presented as the world"* — period art or
  plainly labeled reconstructions only.
- **No ambient/idle motion on the map as a baseline** — pulsing "look here"
  cues, auto-panning, or looping shimmer on connection lines. Every motion
  idea in this document is gated to "once, on a real action, then still,"
  matching the stillness posture; anything that runs *while nobody has
  acted* should be treated as a rejected default, not a missing feature.
- **No collapsing the historical-edge axis and the Table-pairing axis into
  one visual language.** §3's closing finding — keep doing the work to keep
  these separate as the connection grammar grows, or "linking" quietly
  becomes "recommending," which the Vision document's warning against
  "interchangeable paths to a generic Jesus" rules out.

---

## 8. If Mark wants to prototype one thing first

Not a build plan — this thread doesn't build — but three candidates worth
naming as genuinely different bets, since they cost differently and answer
different parts of the brief:

1. **Cheapest, ships the fastest, already decided:** the era-ground palette
   convergence (§5, L2) plus the always-visible connection-type legend (§5,
   L1). Both are near-free, both are pure "help people see the big picture,"
   neither touches motion or figures at all.
2. **Best single answer to "game-grade... interactive worlds that connect":**
   the L4 per-world constellation sub-view (§5), because it is the one idea
   that most directly matches Mark's own reference point — a world with its
   own features, reachable without leaving the map, built entirely from
   sourced material that already exists.
3. **Best long-term structural bet:** the path-finding feature (§6.A),
   because every other connection idea in this document (the richer grammar,
   the always-visible legend, the constellation view) becomes more valuable
   once a participant can *ask* the map a question instead of only scanning
   it — and it is pure client-side graph work over data already loaded, at
   $0 marginal runtime cost either way.

---

## Document log

- **V0.1 (2026-08-31):** First draft. Produced by a research/ideation thread
  per Mark's launch prompt; reads `cic-website/atlas-v3.html`,
  `cic-website/data/world-census.json`, `CiC_Full_UX_Design_V1_0.md`,
  `CiC_UX_Design_Brand_Brief_V1_0.md`, the Vision/Mission/Convictions
  document, `CiC_FrontEnd_Decision_Log.md`, this workstream's own
  `Decision-Log.md` and `README.md`, `CiC_Table_Pairings_V1_2026-08-28.md`,
  and source records under `records/alx/` and `records/pahc/`. External
  research: Crusader Kings III, Age of Empires IV, Civilization's tech tree,
  Slay the Spire/Hades branching maps, Stanford ORBIS, Pelagios/Peripleo,
  museum interactive-timeline design writing, NYT/Pudding-style
  scrollytelling. Nothing in this document is decided; everything is for
  Mark's read.
