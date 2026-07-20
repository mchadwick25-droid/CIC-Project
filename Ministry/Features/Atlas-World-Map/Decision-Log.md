# CiC World Orientation & Selection Map — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning —
including the "heart" reasoning, not just the design logic — and the specific next
action. A decision that only lives in conversation history is one that gets
re-litigated or lost by accident later.

Scope: the interactive World Orientation and Selection Map — a currently out-of-system
product concept for visually orienting a participant across all of Christian history
(built, in-progress, and not-yet-built worlds alike) before they choose who to enter
conversation with. This thread does not touch live `cic-poc` code; integration into the
actual world-selection flow is a future decision for the front-end thread, not this one.

---

## 2026-07-20 (addendum) — Choose-a-Tradition's hover-glimpse dropped as redundant (Mark caught it live)

**Mark's observation, testing Prototype B directly:** "the scroll over didn't offer
any further information than the tile, why not just click on tile for this."

**Verified in the code, not just accepted on report:** the `mouseover` handler built
the glimpse from `name / dates+region / status word` — but every live-world card
(`.wcard`) already prints name, dates, region, status, and a description line at
rest, and every search result row (`.rrow`) already prints name, dates, region,
status word, and the living-tradition tag at rest. The glimpse was a near-strict
subset of what the tile already showed. Confirmed this is **specific to Prototype
B**, not a general flaw in the redesign's grammar: Prototype A's compact 48px status
rows genuinely show less than their Level-2 sheet (which adds the relationship
preview and actions), so that surface's tap-to-glimpse step earns its keep and is
unchanged.

**Applied:** removed the hover-glimpse mechanic from Prototype B entirely (CSS,
markup, and the `mouseover`/`mouseout` listeners) — clicking a card or row already
opened the full panel directly regardless of hover, so nothing about the actual
interaction changed; only the redundant intermediate affordance is gone. Re-verified
no orphaned references remain. Artifact republished at its same URL.

**Heart of it:** the two-level hover/click grammar exists to let someone see *more*
before committing to a full read — it is not decoration to apply everywhere by
habit. Where a surface already prints the short form at rest, adding a hover step
in front of it is pure friction with no payoff, and the fix is to drop the step, not
defend it.

**Next action:** none pending — carry this rule forward into Phase 2 (the in-app
build of Choose a Tradition, once budget allows): only build a hover/glimpse layer
where the tile face actually shows less than the glimpse would.

---

## 2026-07-20 — Fable usability study delivered; five design-decision rulings made

**Mark's direction:** the live map was "way too hard to use, especially on the
phone... the concepts are right but the scale and interaction is way too complex."
Directed a dedicated Fable-model research-and-design thread to study the whole map,
survey comparable scrolling atlas/timeline tools, and propose a more usable
interaction model in the existing brand register — before resuming feature-by-feature
UX testing.

**Produced:** `Design/CiC_World_Map_Usability_Redesign_Study_2026-07-20.md` plus two
working HTML prototypes (`Design/CiC_World_Map_Redesign_Prototype_A_Phone_Story_2026-07-20.html`,
`Design/CiC_World_Map_Redesign_Prototype_B_Choose_A_Tradition_2026-07-20.html`).

**Diagnosis (verified in the shipped code, not inferred):** `world-map.html`'s own
`<title>` reads "Concept Demo V0.3" — a design instrument promoted straight to
production with its stated production punch list (real pinch-zoom, touch glimpse,
era-accordion, 44px targets, real-device testing) never completed. Confirmed zero
touch event handlers in the file; 69% of entries (123/178) render as 9px unlabeled
slivers at phone zoom; a four-deep nested-scroll trap (page → 85vh iframe → two-axis
map → panel); the official phone fallback (the list view) has zero launch actions.
Root cause beneath the individual bugs: one surface asked to be a thesis statement, a
178-entry reference census, and a world-picker at once, when under 3% of entries are
actionable doors.

**Comparative research (5 examples, each examined live):** TimelineJS (separate the
reading surface from the nav surface); The Pudding's scrollytelling epidemic piece
(one verb — vertical scroll — paces density better than pan/zoom); xkcd's temperature
timeline (time-as-scroll communicates scale without any legend to learn first);
Native Land (search-first beats browse-first when the map is a means to an answer;
point-of-reading disclosure is compatible with grace); the Met's Heilbrunn Timeline
(at census scale, retrieval-first-with-chart-optional is the proven production
answer, not a concession).

**Proposed model — three linked surfaces, one shared data source, never deleting the
wall chart:** **The Story** (a vertical era-spine, one verb: scroll) for open
exploration; **Choose a Tradition** (search-first, live worlds land first, non-live
results answer with recorded grounds + a nearest-open-neighbor redirect) for in-app
world selection; **The Wall Chart** (today's canvas) kept as an opt-in desktop/print
view, never the landing surface again.

**Five decisions Mark made against the study's open questions, all DECIDED:**
1. **Pre-survey expander:** counted expander, default-closed ("+11 more this era,
   not yet assessed").
2. **Desktop scope:** the Story replaces the canvas as the landing surface on *all*
   devices, not just phone; the wall chart moves to an opt-in "View as wall chart"
   link.
3. **Tier A/B:** Mark's own framing — "maybe we need two versions, one for
   exploration on the website and another that is for choosing in the conversation
   system" — confirms the study's own two-surface split rather than picking either
   surface as sole primary: **the Story is the website's exploration surface; Choose
   a Tradition is the in-app selection surface.** This is the Tier A/B question's
   actual resolution.
4. **List view's fate:** retire it as the phone fallback; reframe as the scholar's
   research browser it already functions as, linked from the Story's footer.
5. **Era-rail labels:** numeral + short era title revealed on tap/hold, not numerals
   alone at rest.

**Heart reasoning:** none of these five trade away the confidence-calibration or
honest build-status transparency that is the map's reason to exist — every mechanic
audited in the study (its §3.4) lands somewhere in the new surfaces, several of them
(the confidence word, the honest redirect) made *more* visible on touch than they are
on the current desktop-only hover grammar.

**Next action:** this is now a build-ready design — same discipline as the rest of
the front-end backlog: nothing merges before/during a pilot window. Whoever picks up
the build should start from the migration sketch in the study's §3.6 (extract the
census to one JSON asset first — it kills the four-vs-five live-world drift class in
the same motion).

---

## 2026-07-16 (twenty-sixth pass) — Cross-reference: Representative Modes thread launched

**Noted for this thread's record:** Mark launched a new thread (launch prompt
authored this session) to build role-tailored conversation modes — same
Representative, same sources, same governance; register/examples/depth tailored
to the four participant roles (general, pastor/teacher, academic,
deconstructing/reconstructing). Two touch-points with this thread's work:
(1) the `role=` parameter is specified to ride the map-handoff URL contract
established on `claude/world-map-integration-exploration`
(`/?worlds=<id,id>&mode=<interview|table>&role=<...>`), so mode and world
selection arrive at session start together; (2) that thread inherits this
thread's exploration-branch discipline (no changes to running branches, live
verification, assessment doc, merges held through Prototype Testing 1). Its
decisions log to `CiC_Representative_Modes_Decision_Log.md`, rooted in the
front-end log's 2026-07-07 role-shaping entry.

**Next action:** none for this thread; the handoff-contract extension gets
reconciled at whichever merge lands second.

---

## 2026-07-16 (twenty-fifth pass) — Integration exploration built and VERIFIED on its own branch; running program untouched; assessment written

**Mark's direction:** assess what integrating the map (and eventually tours) with
the main program would take for prototype testing — no changes to the running
program, but real work on a new branch we can integrate later. **Boundary note,
made consciously:** the launch prompt reserved integration for the front-end
thread; Mark, as project lead, directed this exploration here. The exploration
happened; the merge decision and its timing stay with the front-end thread.

**Built and verified — branch `claude/world-map-integration-exploration`**
(commit de11233; pilot branch and main untouched, source files confirmed
reverted on checkout): spec Part 4's middle step, working in both directions
against the real dev servers. App → map: one link on the world-selection screen
opens the full map at `/world-map/` (static asset, 281 KB, self-contained). Map
→ app (`?app=1`): "Have an interview with {Rep}" and the tray's "Sit down at the
Table" hand the selection back via `/?worlds=<id,id>&mode=<interview|table>`;
the app preselects on the existing selector, flips the Single/Multiple toggle,
and scrubs the URL. **Verified live:** two-world table handoff (badges 1/2,
"Begin Conversation with 2 Representatives") and the full circle app → map →
Chloe interview → app preselected. `tsc --noEmit` clean. **Design point held:
the map suggests, never starts — the participant confirms with the existing
Begin button, and the backend is unaware anything changed.**

**Engineering lesson recorded:** one-shot URL params parsed in a useState
initializer break under React StrictMode's dev double-mount when the same code
scrubs the URL (second mount reads an already-scrubbed URL). Parse at module
scope; scrub in an effect. Cost an hour; on record so it never costs another.

**Assessment produced** (`CiC_World_Map_Integration_Assessment_V0_1.md`,
committed on the branch and kept as a working-tree copy for reading): the whole
diff is ~40 lines across two components plus one static asset — no backend
changes, no new dependencies. Tiers: A (this branch — merge ≈ one evening);
B (map as primary selector — 2–4 evenings, needs front-end-thread decisions:
tiles' fate, onboarding placement, era-accordion mobile mode); C (Take-a-tour
activation — hours once the hospitality thread delivers, same static-asset
pattern); D (census honesty layer via Ask-the-Facilitator — 1–2 evenings,
independent of the map UI, and arguably the piece worth doing soonest since
testers will ask "why only ancient worlds?"). Cautions: never merge mid-pilot
(standing ops rule); map copy is design-frozen, not externally reviewed; the
WID ref→world-id mapping is hand-synced and should be generated at Tier B.

**Recommendation:** hold the branch through Prototype Testing 1; the front-end
thread takes the merge decision with the pilot schedule in front of it.

**Next action:** Mark reads the assessment; if he wants testers to see the map,
the merge happens BEFORE invitations go out, never mid-pilot.

---

## 2026-07-16 (twenty-fourth pass) — Coordination note: hospitality/tour thread producing a parallel demo; joint assembly session planned

**Mark's direction:** the hospitality tour thread is being asked to produce the
same kind of deliverable (guided walkthrough + recording), and Mark will work
across threads to put it all together into one package.

**What this thread has ready to contribute to that assembly, all in
`Ministry/Technology/World-Orientation-Map/`:** the interactive demo with the
built-in ▶ Watch-the-flow tour (`CiC_World_Map_Interactive_Demo.html`,
self-contained single file); the flow recording (`CiC_World_Map_Demo_Flow.gif`)
and 12-frame slideshow (`CiC_World_Map_Flow_Slideshow.html`); the email pack zip;
the census browser; plus the governing documents (spec, atlas, census V0.12,
visual architecture with the practicality review).

**Reusable machinery the other thread may want, to keep the combined package
feeling like ONE product:** the visual tokens (parchment/ink/gold palette, Cinzel
display + Georgia body — all in the demo template's CSS variables); the
self-contained single-file pattern (assets inlined as data URIs, no server); the
PD-art-with-source-credits discipline; the tour-engine pattern (caption strip
BELOW the screen per Mark's correction, moving pointer, skippable, `?tour=1`
autostart); and the `?pose=N` + headless-Chrome + Pillow recording pipeline
(the reliable method — the extension GIF recorder only captures on tool
actions). Asset pipeline scripts live in this session's scratchpad
(`gen_map_demo.py`, `build_atlas_xlsx.py`); the templates are the durable source.

**Next action:** assembly session with Mark, both threads' deliverables in hand.
This thread's suggestion for that session: agree the shared visual tokens and the
caption-below convention first, then merge content — so the package reads as one
crafted thing rather than two demos stapled together.

---

## 2026-07-16 (twenty-third pass) — Tour narration moved below the screen (Mark's correction); recordings rebuilt

**Mark's correction:** the tour's floating description card covered the action —
move it to a strip across the bottom, below the map, so all clicks can be seen.

**Applied:** the caption is now a full-width docked strip between the map frame
and the seat tray; the map frame shrinks to make room (sizeWrap accounts for the
caption's height), so nothing overlaps the chart, the tooltips, the lineage
edges, or the panel's action buttons. The strip sits above the panel's empty
bottom padding so its text stays fully readable even with a world open. Applied
identically to the live tour, pose mode, and both recordings — the GIF
(CiC_World_Map_Demo_Flow.gif, rebuilt) and the 12-frame slideshow artifact
(rebuilt) — all frames recaptured and visually verified.

**Next action:** unchanged — Mark plays the tour, shows a first viewer, and marks
up caption wording.

---

## 2026-07-16 (twenty-second pass) — The demo simulation built, run live, and recorded

**Mark's direction:** build a simulation — start at the world map, select the Early
Church era, choose a world, then select the next era and choose a second world for
a conversation — recorded, for showing people what this will do functionally.

**Built — a guided tour engine inside the demo itself** (demo → V0.5): a "▶ Watch
the flow" button (era bar + welcome card; also `?tour=1` auto-start) plays a
12-step scripted walkthrough with caption cards, a moving gold pointer, and pulse
highlights: the landscape → Era 1, The Early Church → the House-Churches band →
its panel → **Chloe seats (tray reads Deep Interview)** → cross to Era 2, The
Imperial Church → the Desert band → its panel → **Papnoute seats (tray reads
Compare Worlds)** → "Sit down at the Table" → the honest stub ("this is a design
demo — it ends here, honestly") → outro. Skippable at any moment; reduced-motion
respected. This is better than a fixed video for live showings: it replays
identically, inside the real interactive artifact.

**Run and verified live in real Chrome** (via the local demo server): the full
click-through was exercised and screenshotted end-to-end; every scripted state
landed (Chloe seated → Deep Interview label; both seated → Compare Worlds; the
Table modal listing both worlds).

**Recorded — two artifacts:** (1) `CiC_World_Map_Demo_Flow.gif` (~1.6 MB, 12
frames, ~49s loop) saved to the World-Orientation-Map folder — captured
deterministically via a new `?pose=N` mode (renders the exact state of tour step
N instantly) + headless Chrome frame capture + Pillow assembly; (2) a
slideshow artifact ("The Flow, in 12 Frames") — auto-playing with manual arrows
for hand-presenting, each frame captioned.

**Technical notes for the record:** the Chrome extension's GIF recorder captures
frames on tool *actions* only (4 frames from a 12-step tour) — the pose-mode +
headless-capture pipeline is the reliable recording method for self-animating
pages, and `?pose=N` is now a permanent testing/screenshot affordance;
`save_to_disk` on extension screenshots produced no file.

**Next action:** Mark plays "Watch the flow" himself, shows it to a first viewer,
and marks up any caption wording; the GIF is ready to drop into decks or messages
as-is.

---

## 2026-07-16 (twenty-first pass) — Practicality review: tested in a live browser at desktop and phone sizes; critical fixes applied (demo → V0.4)

**Mark's direction:** deep review on user practicality — the functions are there,
but can it be accessed on a phone, or even on a computer screen, in an engaging
way?

**Method:** not speculation — the demo was served locally (loopback-only, via the
project's launch.json) and exercised in the live browser pane at 1280×800 and
375×812, with layout measured and the full interaction chain driven
programmatically (band → panel → interview → modal; tray modes; zoom levels;
era jumps). In-pane screenshots proved broken at the tool level (hung even on a
plain text file), so verification was metric- and interaction-based throughout.

**Headline findings (measured):** desktop — the header block consumed 452px of a
720px viewport, leaving the map a 268px letterbox; phone — the header ran to
829px on an 812px screen, i.e. **map visible height was NEGATIVE: a phone user
saw zero map.** Also: no charset/viewport meta (glyphs garbled when served raw;
phones would have rendered at ~980px virtual width — mobile silently broken at
the HTML level); the 9500×2166px canvas rendered unframed with most lanes below
the fold; parchment noise painted across the whole canvas (performance risk);
phone opened at 100% zoom (Era 1 alone ≈ 2.5 screens); no orientation cue across
9,500px of scroll; zoom buttons under touch size.

**Fixes applied same session (all re-measured after):** charset + viewport meta;
header collapsed to a one-line invitation with legend/reading-notes in a
collapsible; the canvas is now a viewport-framed window scrolling both axes
inside itself (map top 452→~200px desktop; phone map −91px → **377px in frame**);
noise off the canvas surface; device-aware initial zoom (<700px opens at the 50%
landscape view, whole chart ≈ 13 swipes); active-era highlight verified across
the scroll range; era nav a single scrollable row with ≥38px buttons; visible
small-screen note linking the census browser as the list-form fallback; footer
clearance for the fixed tray.

**Recorded in the architecture doc (§9)** as a findings table plus the honest
remaining-for-production list: real pinch-zoom, tap-and-hold glimpse on touch,
the era-accordion as a first-class mobile mode, 24px band heights vs. the 44px
touch guideline, and real-device testing (a resized viewport approximates a
phone; it isn't one).

**Answer to Mark's question, plainly:** on a computer, yes — engaging now: the
chart opens as a stable framed window with the four live worlds glowing, and the
era buttons track where you are. On a phone, honestly: *usable* now (it was
literally invisible before this pass), best at the landscape view plus the
census-list fallback — but a phone-first participant experience still needs the
production items above, and that remains the front-end thread's build.

**Next action:** Mark tries the updated demo on his own machine and, ideally, his
own phone — real-device feel is the one thing this pass could not measure.

---

## 2026-07-16 (twentieth pass) — DECIDED: the Wet Ink Horizon (Amendment G) — how the atlas holds still-forming currents

**Mark's insight, in his own words:** current movements "are still forming and
tend to overlay other more established movements"; building them rigorously is
far future, "but we need to capture it creatively on this atlas."

**The named principle (atlas, Amendment G):** the last half-century sits inside
the **historiographical horizon** — nothing has settled. Entries there differ in
kind from historical worlds in three marked ways: (1) **overlays, not
territories** — a person may stand in a megachurch, the narrative-kingdom
current, and deconstruction simultaneously, so bands-in-lanes structurally
misrepresents them; (2) **the source problem is inverted** — recovery-from-
scarcity becomes selection-from-abundance, plus platform-fragility preservation
and living-person consent; (3) **membership is non-exclusive and self-described**
— interplay is a first-class feature, not noise.

**The creative device — wet ink:** six Era-10 entries carry the new **Overlay
Current** form (≈): Lausanne-era evangelicalism, the Emerging Church,
Dispensational Prophecy Culture, the Megachurch/Seeker movement, Deconstruction
communities, the Narrative–Kingdom Renewal. On the map they render as wet ink —
translucent, soft-edged, fading unfinished at the right — where historical worlds
are engraved. The chart's engraving runs out at its right edge *on purpose*; the
legend says so. Briefs carry the overlay line participants need: "you may stand
in several at once — that's not confusion, that's what a forming era looks like."

**Future-methodology flag (handoff, not this thread's work):** building inside
the horizon will someday need a *Current Ecology* variant of Doc_02 — magnitude
(selection from abundance), preservation, consent/safety, overlay membership,
bounded windows as requirement. Named in the atlas for the methodology thread
when that day comes.

**Applied:** census V0.13 ("Form" column: World / Overlay Current; `cur` field in
the data contract); demo republished (wet-ink band styling, ≈ marks, tooltip and
brief badges, legend line); browser republished (badges); atlas Amendment G
section added. All verified by execution.

**Next action:** Mark eyeballs the wet-ink rendering at the map's right edge.
The atlas now holds three registers of honesty about time: engraved (settled
history), question-marked (unrun assessments), and wet (still forming).

---

## 2026-07-16 (nineteenth pass) — IX.32 added: The Narrative–Kingdom Renewal (Wright/McKnight/Mackie's current), census → 178

**Mark's identification:** Tim Mackie, N.T. Wright, Scot McKnight and the
grand-narrative / Jesus-as-fulfillment / Kingdom-of-God current — "I think that is
a current movement."

**Agreed and added — IX.32, The Narrative–Kingdom Renewal (c. 1990–present),**
with the worlds-not-persons rule applied to the named individuals (they render as
figure lifelines within the band, not as map objects — the same honest answer as
"why can't I talk to Augustine"). Lineage carried in the entry: Newbigin's
missional vision → Willard's kingdom discipleship → Wright's popularization →
McKnight's King Jesus Gospel → BibleProject reaching tens of millions. Notably
creed-affirming across its voices (no floor note); no founder-prophet mark
(plural teachers, no revelation-based authority).

**The design insight worth keeping:** IX.32 is **the counter-reading-culture to
IX.29's dispensational hermeneutic** — story against chart, two rival ways the
present generation learns to read Scripture — and a frequent re-rooting place for
IX.31's deconstructors. The three rows added this evening (IX.29, IX.31, IX.32)
form a genuine relational triangle on the map, which is exactly the kind of
visible relationship structure the map exists to show. Honest Step 0 question
carried in the brief: teaching current or formation community? The formation
texture (classroom cohorts, curricula, reading practices) is real; the
bounded-window rule applies.

**Census V0.12 (178 entries);** demo, browser, atlas republished and verified.

**Next action:** Mark reviews IX.32's brief. Era 10's contemporary section now
carries 32 entries — at some point a Step 0 for a modern phase will thank this
thread for the pool, which is exactly what the pre-Step-0 survey was for.

---

## 2026-07-16 (eighteenth pass) — Progressive Christianity relabeled (the status miscommunicated, not the judgment); four contemporary-movement rows added (Amendment F; census → 177)

**Mark's challenge:** why is Progressive Christianity "outside the scope" — it's a
real faith many are turning to; and what about dispensationalism and other current
movements?

**The finding:** the judgment was right, the label failed. IX.18's "Outside
Article 4 Scope" status was carrying the Methodology's own A3 rule — which is
*protective*, not exclusionary: "this methodology does not rule on 'progressive
Christianity' as a category, because the category spans both sides of the floor;
eligibility is assessed against the specific confession of the specific candidate
community — never against a label." Some progressive bodies pass the floor
plainly; judging the label either way would wrong somebody. But if Mark read
"outside scope" as exclusion, participants will too.

**Applied — a new status and a rewritten brief:** IX.18 reclassified to **"Label —
Assessed Per Body (A3)"** (its own rendering, double-bordered, distinct from
excluded styling), retitled "Progressive Christianity (a broad label, not one
movement)," with a warmer brief that leads with "a real and fast-growing current"
and explains that the per-body rule exists to *protect* it from category judgment.

**Applied — four contemporary candidate rows (Amendment F), all Pre-Survey
Candidates in the Protestant & Evangelical lane:** IX.28 The Emerging Church &
Post-Evangelical Movement (the progressive current's most documented movement
expression; A3 per-body note; platform-decay preservation note); IX.29
Dispensational Prophecy Culture (a lived formation culture, not just a doctrine —
Niagara → Scofield → Left Behind; child of VIII.23/VIII.24; bounded-window rule);
IX.30 The Megachurch & Seeker Movement (bounded windows only); IX.31
Deconstruction & Ex-vangelical Communities — with two notes the project cannot
ignore: its own named audiences include deconstructing Christians (this entry
partly maps the map's own visitors), and a Step 0 here would face a genuinely new
ecology question (formation community or dispersal-in-progress?).

**Census V0.11 (177 entries)**; demo, browser, and atlas republished and verified.

**Heart reasoning:** the participant Mark is describing — someone moving toward
progressive Christianity, or deconstructing out of the megachurch world — is not
an edge case for this project; they are a named audience of it. The map they open
must meet them as real, not as a footnote marked "outside scope."

**Next action:** Mark reviews the four new briefs and the relabeled IX.18.

---

## 2026-07-16 (seventeenth pass) — DECIDED: the founder-prophet (✦/✧) designation

**Decided by Mark** (accepting the sixteenth pass's middle path and its closing
offer): a founder-prophet designation on the map — visible wherever a movement's
authority structure rests on a named individual's revelation or personal standing
(the Step 0 record's person-defined / Criterion 2 ground), orthogonal to lane and
creedal status.

**Designed and applied — two tiers, never flattened:** **✦ ground on record**
(the C2 ground is on the Phase One record or stated in the movement's own
confession): Montanism, Novatianism, Shakers, Swedenborgians, LDS, Jehovah's
Witnesses, Christian Science, Oneida, the INC/Way/Unification/Luz cluster, Branch
Davidians — 10 entries. **✧ question to run** (a C2 check a future Step 0 must
run, which may well clear): the Joachimite current, Savonarola's Observance,
Family of Love, Kimpa Vita's Antonians, the Haugeans, Adventism (Ellen White),
Catholic Apostolic, Plymouth Brethren, the AICs' founder-succession cases, the
Chinese founder-defined branches, the Catholic founder-charism movements, Taizé &
Iona — 12 entries. The two-tier split preserves exactly the nuance the Adventism
decision protected: Taizé and the Haugeans would almost certainly clear the check;
flattening them into one mark with Branch Davidians would be its own dishonesty.

**Why orthogonality is the point (heart):** the mark says what *kind of authority
question* exists — never where a movement stands on the floor. Montanism carries ✦
while being creedally sound; Adventism carries ✧ while being trinitarian; LDS
carries ✦ in the Beyond-the-Floor stream. Three different situations, one honest
vocabulary, no conflation.

**Applied:** census V0.10 (new "Founder-Prophet / Person-Defined (C2)" column;
`c2` field in the data contract); demo republished (marks on bands, tooltips,
panel badges, legend line); census browser republished (badges + searchable);
spec 3.3 gains the designation section. All verified by execution.

**Next action:** Mark reviews the 22-entry sort — the record tier is drawn from
stated grounds, but the question tier reflects this thread's reading of the census
notes and is his to amend.

---

## 2026-07-16 (sixteenth pass) — LDS/SDA question: LDS confirmed already in the stream; Adventism reclassified to Floor Question status, kept in the Protestant lane, with the reasoning stated

**Mark's expectation:** LDS and Seventh-day Adventism should be in the
Beyond-the-Floor row.

**LDS:** already there (VIII.14, moved in the fifteenth pass alongside JW,
Christian Science, Christadelphians, Oneness, and the rest).

**Adventism — deliberately NOT moved, with pushback given and a middle path
applied.** The stream's defensibility rests on its definition: movements whose
*own confessions* place them outside the Nicene base. That is factually true of
LDS/JW (the Methodology's own named A1 examples) and factually NOT true of the
SDA church today — its official 28 Fundamental Beliefs are explicitly
trinitarian, and mainstream scholarship treats it as trinitarian Protestantism
with distinctive doctrines. What Mark's instinct correctly detects: the
founder-prophet authority structure (Ellen White — a live Criterion 2 question)
and the movement's early window, whose leadership genuinely included
anti-trinitarians before the confession consolidated. Per the Methodology's own
window- and confession-specific rule, which window is assessed decides
everything. Placing today's SDA in an "own-confession-outside" stream would
misstate their confession — the kind of error an Adventist participant or
scholarly reviewer would rightly call out, and the kind the map cannot afford.

**Applied (the middle path):** VIII.10 reclassified Pre-Survey Candidate →
**Floor Question (register)** — it now renders in the dashed question-styling,
visibly not just another unassessed Protestant band, while staying in the
Protestant lane where its current confession places it; its brief carries both
named questions in full. Census V0.9; demo and browser republished (verified).

**Standing offer recorded:** if Mark still wants the full move after this
reasoning, it is a one-line change — but it should be made knowing it asserts
something about SDA's own confession that their confession does not say.

**Next action:** Mark confirms the middle path or overrides it.

---

## 2026-07-16 (fifteenth pass) — DECIDED: the eighth stream — "Beyond the Floor (researched & explained)"

**Mark's direction:** for worlds outside "the base or proximity" — a separate
stream, recognizing the research was done and a brief is readable: not conversation
worlds, but transparency made visible.

**Decided and applied:** an eighth stream at the map's bottom, **"Beyond the Floor
(researched & explained)"**, holding only movements whose *own confessions* place
them outside both the Nicene base (A1) and the bounded-exception proximity (A4) —
19 census entries moved: Marcion, Valentinian/Gnostic Christianities, Manichaeism,
the Homoian family (both entries), Bogomils, Cathars, the anti-trinitarian
Reformation currents, Shakers, Swedenborgians, LDS, Jehovah's Witnesses, Christian
Science, Christadelphians, Oneida, Spiritualism/New Thought, Oneness
Pentecostalism, INC/Way/Unification/Luz del Mundo, Branch Davidians. Their click
panels now read as **research briefs** ("Research brief — not a conversation
world, and why").

**The three guardrails that keep this honest rather than a stigma row:**
(1) *question-cases stay in their historical lanes* — contested-evidentiary
(Ebionites, Paulicians, Free Spirit: the record cannot say they were outside),
A4-proximity (Schwenckfelders), person-defined-with-sound-theology (Montanism,
Novatianism, Catholic Apostolic), and pending per-body assessments (Ratana);
moving them would overclaim. (2) Stream entries keep true time positions and
relationship edges — Marcion still sits beside the second-century church he argued
with. (3) The copy carries the Step 0 record's own framing: a design effect, never
a judgment of unimportance. Mark's "base or proximity" phrase is the razor the
whole sort ran on.

**Governance flag raised, not resolved (needs Mark / a governance pass):** the
Step 0 Conclusion holds Homoian Christianity's A4 question open, but the Step 0
Methodology's A4 clause says the hand-selected path "may never waive Christ's full
divinity" — the very commitment Homoian confession diverges on. The two records
are in tension; flagged in the spec (1.5) and here. Until reconciled, the map
carries Homoian in the stream with its open question stated.

**Applied:** census V0.8 (Lane column updated; Read Me documents the stream and
the stay-in-lane rule); demo and census browser republished at their same URLs
(both verified by execution; demo adds the stream lane, a legend line, and the
research-brief panel header); spec 1.5 gains the stream section.

**Heart reasoning:** the participant most likely to click these entries is
someone *from* one of these communities, or someone who loves someone in one. The
brief they read must be the same posture as everything else on the map — factual
confessional description, stated grounds, no sneer — which is exactly what the
Methodology's own A1 text models ("stated as a factual description of the
confessional difference, not a value judgment about the movement or its
adherents").

**Next action:** Mark reviews the stream's rendering and the 19-entry sort;
the Homoian A4/Methodology tension goes to governance when he's ready.

---

## 2026-07-16 (fourteenth pass) — DECIDED: eras numbered plainly 1–10 (Amendment E)

**Decided by Mark:** drop the 1a/1b sub-numbering — the map's eras are simply
1 through 10: 1 The Early Church Era (70–312) · 2 The Imperial Church Era
(312–451) · 3 The Age of Monks and Empires (451–622) · 4 The Early Medieval Era
(622–1054) · 5 The High Medieval Era (1054–1300) · 6 The Late Medieval Era
(1300–1517) · 7 The Reformation Era (1517–1650) · 8 The Enlightenment & Awakening
Era (1650–1815) · 9 The Missionary Era (1815–1906) · 10 The Global Church Era
(1906–present). Phase One spans map eras 1–2, unchanged.

**Stability decision made alongside it:** Atlas IDs (I.1, II.5, …, IX.27) do NOT
renumber — they are stable record keys, with the Roman numeral now explicitly
defined as the *atlas survey part* (Part I spans map eras 1–2; Parts II–IX map to
eras 3–10). The census column was retitled "Atlas ID," and the mapping is stated in
the atlas intro, the spreadsheet Read Me, and the census browser subtitle. This
avoids silently rewriting ~173 record keys across every document and keeps older
amendment notes historically accurate.

**Applied everywhere:** census V0.7 (era counts 11/15/12/14/16/13/21/17/27/27);
census browser and demo republished at their same URLs with eras 1–10 (both
verified by script execution; demo medallion keys remapped — Fayum→1, Rabbula→3,
Kells→4, Cranach→7); atlas headers now read "Era N (Atlas Part R)" with the
confirmed-list paragraph updated as Amendment E.

**Next action:** none pending on numbering. Standing forward work unchanged
(medallions for the remaining eras, Figma design-of-record, asset folder to repo).

---

## 2026-07-16 (thirteenth pass) — Wall-chart styling pass built (Demo V0.3); the sourced-art discipline proven in miniature

**Decided by Mark:** go on the styling pass (the zero-cost proof-of-direction step
from the twelfth pass's sequencing).

**Built — Demo V0.3** (same artifact URL; execution verified; ~260KB fully
self-contained): parchment ground via inline SVG turbulence noise (light = aged
paper, dark = old leather); **Cinzel** display face inlined as a data-URI (Google
Fonts, OFL license) for the title, era headers, lane cartouches, and panel
headings, body remaining Georgia; engraved band treatment (inset bevels,
letterpress shadows; hatched fill for excluded entries, dotted for contested);
lane labels as gold-bordered cartouches; double-ruled legend cartouche and a
diamond-ornament title rule; drop caps on the panel's "why" copy; gold-ruled
buttons and leather tray.

**The heart of the pass — four public-domain era medallions with visible
sourcing:** Fayum mummy portrait (Roman Egypt, 2nd c.) on Era 1a; the Rabbula
Gospels fol. 13v Ascension (Syriac, 586, Biblioteca Medicea Laurenziana) on Era 2;
the Book of Kells Chi-Rho folio (c. 800, Trinity College Dublin) on Era 3; Cranach's
1528 Luther (Veste Coburg) on Era 6 — all fetched from Wikimedia Commons,
duotone-treated for visual unity, each carrying its full source on hover, with a
credits line in the footer stating the principle: "the map's honesty extends to its
own artwork." This is the twelfth-pass recommendation (PD period art as primary
asset source, source-on-hover as extended transparency) proven working, not just
proposed.

**Technical notes for the record:** assets pipeline is
scratchpad/assets → duotone/resize via Pillow → base64 → injected by
gen_map_demo.py with graceful degradation if absent; Rabbula's Commons filename
required an API search (Special:FilePath + the file's real title) — worth
remembering for future asset pulls; total inline asset weight ~126KB (font 60KB,
four vignettes ~66KB).

**Next action:** Mark judges the direction with his eyes. If it lands: Figma
design-of-record built from these tokens, medallions extended to all ten eras
(candidates: a Cluny/Hildegard manuscript for Era 4, a Book of Hours for Era 5, a
Rembrandt or Wesley portrait for Era 7, a mission-era or revival photograph for
Eras 8–9 — photography enters the record), and the curated-asset folder moves into
the repo with per-image source metadata.

---

## 2026-07-16 (twelfth pass) — Graphic-design tooling recommendation given; awaiting Mark's pick

**Mark's verdict on V0.2:** structure great, concept "amazing" — but the front-end
graphics need real work to look like a wall chart. Question: what to use for the
graphic design.

**Recommendation given (three jobs, three answers):** (1) **Figma** as the
design-of-record (free tier now; the artifact a future designer/engineer inherits);
Affinity Designer only if Mark wants to draw ornaments himself; no Adobe
subscription at this stage. (2) **Public-domain period art as the primary asset
source** — Met/Rijksmuseum/British Library/Wikimedia open access; Fayum portraits,
Rabbula Gospels, Book of Kells, Cranach woodcuts per lane/era; Adams' 1871
Synchronological Chart is itself PD and sampleable. **Heart move: every vignette
carries its real source on hover — the map's transparency mechanic extended to its
own artwork.** AI generation (Firefly for indemnified commercial use) reserved for
style-unification (textures, borders, duotone), NOT for depicting representatives
or historical people — the front-end log's existing evidentiary-imagery discipline
(ethnicity/dress from the world's own evidence) applies to any depicted person.
(3) **CSS/SVG within the existing demo architecture** for application — parchment
ground, engraved borders, open-license display faces (Cormorant/Cinzel/EB
Garamond), PD vignettes as era medallions; the demo's CSS tokens map onto a Figma
system nearly one-to-one.

**Sequencing recommended (solo-founder budget):** buy nothing yet → wall-chart
styling pass on the demo in CSS/SVG first (zero cost, proves the direction) → Figma
design-of-record built from what worked → curated PD asset folder in the repo with
per-image source metadata → human designer at Phase 1 polish, inheriting a working
visual language rather than a blank brief.

**Next action:** Mark's go/no-go on the styling pass as the next working step.

---

## 2026-07-16 (eleventh pass) — Visual architecture answered and specified; demo upgraded to V0.2 (zoom, figures, edges, status-driven actions)

**Mark's question:** the best way to build the interactive visual — scroll, zoom
in/out, hover per world, click options varying by status (description-only for
unbuilt; join a conversation / have an interview / tour with the Representative /
academic sources for built worlds) — in the style of the interactive Bible-timeline
charts (his named reference: the Amazing Bible Timeline with World History).

**Produced — `CiC_World_Map_Visual_Architecture_V0_1.md`** (artifact published).
The one-sentence answer: a single continuous canvas in era-normalized coordinates,
lightweight DOM/SVG, **semantic zoom** (three detail tiers — landscape / era view /
world view — that add content as you zoom rather than scaling pixels), native
horizontal scroll + drag, hover-for-glimpse / click-for-panel, and a click panel
whose actions are driven entirely by `build_status` in the census. Staged tech:
dependency-free demos now; React + SVG (d3-zoom or equivalent) at integration —
**the census JSON is the contract**, so the front-end thread can swap renderers
without touching content. Covers mobile (tap-tap, pinch, era-accordion fallback),
accessibility (focusable bands, keyboard lanes, reduced-motion), and a print/poster
render as a near-free by-product — the wall-chart heritage honored.

**Decided — the click-menu refinement Mark introduced:** built worlds now carry
**"Have an interview" (launches Deep Interview solo) and "Join a conversation"
(adds to the table tray) as two explicit actions**, reconciled with the existing
tray model: interview = the tray's one-seat state reached one click sooner; the
tray remains the single source of truth for what launches. Tour-with-Representative
and academic-sources remain visible placeholders per the standing world-click-menu
discipline.

**Built and verified — Concept Demo V0.2** (same artifact URL; script execution
verified at both default and maximum zoom): five zoom steps (50%–240%) with
re-layout-not-pixel-scaling so text stays crisp; Ctrl+wheel / double-click /
buttons, zoom preserved around the cursor point; tier-1 landscape collapses
unbuilt bands to thin (still hoverable) strips; tier-3 world view reveals **figure
lifelines** for the four built worlds (Ignatius→Hermas; Jacob→Ephrem;
Antony→Evagrius incl. Amma Sarah; Marcella→Eustochium) and finer gridlines;
**relationship edges draw on demand** (hover/selection only, never all at once)
from the spec's seed-edge set, confidence-styled — solid documented/widely-accepted,
dotted contested — with the honest note as the line's tooltip; expanded two-register
context strip (church events in gold, world history muted: Temple falls →
Vatican II); drag-to-pan; status-driven panels as specified.

**Next action:** Mark plays with V0.2. Named V0.3 items already in the architecture
doc's build sequence: full figure roster for Live + Selected worlds, edges extended
from the census relations column, true between-lanes bridge rendering, poster print
CSS. Production rendering choices remain the front-end thread's, made against the
architecture document.

---

## 2026-07-16 (tenth pass) — Armenian row added (verified first); the last three open questions resolved; interactive demo V0.1 built

**Decided by Mark:** "yes if that is true, include it, and run the last three."

**Verified, then included — IX.27, The Armenian Church after the Genocide (Medz
Yeghern, 1915–present).** Web-verified before adding, per Mark's conditional: the
April 23, 2015 centenary canonization of the ~1.5 million victims at Etchmiadzin is
on record as believed to be the largest canonization service in history and the
Armenian church's first new saints in four centuries (France 24; armenianchurch.us;
HuffPost — links in conversation record). The 1938 claim about Catholicos Khoren I's
death was NOT confirmed by the check and was soften-worded in the entry ("the
catholicosate itself almost extinguished in the 1938 purges") rather than asserted.
Census V0.6: 173 entries; the Caucasus lane now runs I.10 → II.4 → IV.15 → IX.27,
completed the way IX.19 completed the Syriac lane.

**Resolved — un-run-era register rendering (spec Q4):** ships at V1 with
question-framed copy. The map's thesis is that honesty about the unresolved is
itself trustworthy; hiding real movements until their Step 0 runs would be the
silent omission the Historical Responsibility value forbids. The guardrail is the
standing copy discipline: the Methodology's own vocabulary, questions never
verdicts.

**Resolved — "Notify me when this changes" (spec Q5): cut.** No notification
infrastructure exists or is planned, and the button would quietly force the
unresolved accounts/identity question (it needs an address to notify). A "planned"
label with no plan is a soft over-promise. May return as a real feature via the
front-end thread if accounts ever exist. Spec §3.5 action list updated.

**Resolved and BUILT — standalone demo (spec Q6): yes, as a design artifact owned
by this thread.** Interactive concept demo V0.1 published (artifact `map_demo`,
script execution verified: 173 rows, 10 eras, all spans valid): horizontally
scrolling era-scaled canvas (equal room per era, distortion disclosed on-page);
eight lane rows (Origin zone + the seven lanes); status-honest rendering (live
worlds in their manifest colors, everything else in the census palette with dashed/
dotted exclusion borders); context markers (Nicaea → Azusa); hover cards; a click
panel carrying each entry's real census copy (why-not-open, sourcing, floor,
relations) with per-lane nearest-live-neighbor redirects; the selection tray where
Deep Interview (1) / Compare Worlds (2–3) emerge from seat count; and an honest
launch stub ("this is a design demo — it ends here, honestly"). Demo
simplifications noted on-page (bridge entries seat in one lane with a ↔ badge;
figure lifelines and edge-drawing not yet in V0.1). **Pilot exposure is the
pilot/front-end thread's call; this thread's recommendation stands: after
testers' sittings, not before.**

**Heart reasoning across all three:** the same rule as everywhere — show what is
real, say what isn't, promise nothing without a plan behind it.

**Next action:** Mark plays with the demo and marks it up. This thread's open-
question list is now EMPTY — remaining forward work is census maintenance, demo
iteration on feedback, and (when Mark says the design is mature) the formal handoff
to the front-end thread per spec Part 4.

---

## 2026-07-16 (ninth pass) — DECIDED: Lane 4 resolved — seven-lane architecture; census carries per-entry lanes

**Mark's direction:** work Lane 4 ("Africa & the Oriental churches" — Armenia isn't
African; geography and communion-family mixed in one label).

**Decided and applied — seven lanes** (spec 1.5 rewritten): 1 Syriac East & Asia ·
2 **Caucasus** (new: Armenia + Georgia together — the lane's own internal story,
their 607 parting over Chalcedon, teaches; Georgia's Chalcedonian alignment is
drawn as edges to the adjacent Greek East lane rather than by moving it out) ·
3 Greek East & Orthodoxy · 4 **Africa** (plainly named: the Nile
spine — Alexandria, Desert, Coptic, Nubia, Ethiopia — plus Kongo, the AICs (moved
from the modern catch-all lane; their lineage is African initiative), and the
diaspora/reverse-mission churches: one continuous 16-entry lane from Era Ia to the
present, the map's visual proof of its longest-testimony claim) · 5 Latin West &
Catholicism · 6 Protestant & Evangelical (from 1517) · 7 Global Revival &
Pentecostal (from ~1900).

**Two honesty devices attached:** (1) the legend states the Latin-North-Africa
tie-break plainly — Donatism/Cyprian/Augustine read in Lane 5 by formation language
and downstream flow, while the Africa lane's continuity story is Nile-based;
geography loses that tie-break and the map says so. (2) *Bridge* labels exist for
entries whose identity IS the bridge (Union of Brest and the Ukrainian underground
"3↔5"; Mar Thoma "1↔6"; Taizé/Iona "5↔6"; the Homoian and Imperial worlds span
3↔5) — rendered between their lanes rather than forced into one.

**Applied:** census V0.5 generated with a Lane column — all 172 entries assigned,
zero gaps (lane counts: Latin West 49, Protestant 46, Greek East 21, Africa 16,
Global 11, Syriac 10, Origin-zone 6, Caucasus 5, bridges 7, out-of-scope 1);
census browser republished at the same URL with a lane filter added (script
execution verified); spec open question 3 marked resolved.

**Gap noticed while working the lane, recommended but NOT added (needs Mark's
yes):** the Caucasus lane has no modern anchor — the census carries no
Armenian-genocide-era church entry (1915, the same catastrophe as the approved
Sayfo row IX.19, plus the Soviet-era Armenian church and diaspora). A one-row
addition ("Medz Yeghern and the Armenian diaspora church, 1915–present") would
complete the lane the same way IX.19 completed the Syriac one.

**Next action:** Mark's yes/no on the Armenian modern row. Remaining open:
un-run-era register rendering at V1; "notify me" placeholder; standalone demo.

---

## 2026-07-16 (eighth pass) — DECIDED: all era boundaries confirmed

**Decided by Mark:** the full era structure is confirmed as the map's pickable
eras — Ia The Early Church Era (70–312) · Ib The Imperial Church Era (312–451) ·
II The Age of Monks and Empires (451–622) · III The Early Medieval Era (622–1054) ·
IV The High Medieval Era (1054–1300) · V The Late Medieval Era (1300–1517) ·
VI The Reformation Era (1517–1650) · VII The Enlightenment & Awakening Era
(1650–1815) · VIII The Missionary Era (1815–1906) · IX The Global Church Era
(1906–present).

**Standing caveat preserved with the confirmation:** map eras organize *reading*;
the window of any future release phase remains that phase's own Step 0 decision and
need not coincide with a map era (Phase One itself spans Eras Ia–Ib).

**Applied:** Atlas intro updated from proposal-language to confirmed-language; spec
open question #2 marked resolved. No census regeneration needed — the spreadsheet's
era table already carries exactly these boundaries.

**Remaining open questions on this thread:** Lane 4's grouping/label ("Africa & the
Oriental churches"); whether un-run eras' adjacent-register entries ship at V1 with
question-framed copy or wait for their Step 0s; whether "Notify me when this
changes" stays as a placeholder or gets cut; whether the map ships as a standalone
demo before front-end integration.

---

## 2026-07-16 (seventh pass) — DECIDED: map-Era I splits at Constantine (Option A); positioning only; description lines deferred to after Prototype Testing 1

**Decided by Mark:** Option A. The map presents **Era Ia — The Early Church Era
(70–312)** and **Era Ib — The Imperial Church Era (312–451)**. Phase One is
unchanged and deliberately spans both (its Step 0 creed-to-council window). Mark's
own framing of the boundary: this changes nothing about the built worlds, "just how
we position them" — plus possibly one era-positioning line in each live world's
description, **implemented only after Prototype Testing 1**.

**Heart reasoning:** the credibility Mark wants is with the first-time participant,
for whom "the Early Church ends at Constantine" is the shelf they already know —
and the launch story gets *stronger*, not weaker: "Phase 1 deliberately spans both
eras, so a voice formed before Constantine's revolution can sit beside one formed
after it." That is already true of the live set (Chloe before; Papnoute and Albina
after; Mar Yausep spanning it from outside Rome's empire entirely) — no
re-selection, no overstatement.

**Applied (Amendment C):** Atlas Era I section split with assignment lists and the
Persian nuance stated (for the Syriac world the divide ran backwards — Constantine's
conversion intensified Persian persecution; the divide is a Roman story and the map
must not imply it was everyone's);
`CiC_World_Atlas_Census_V0_4.xlsx` generated (Era 1a: 11 rows incl. straddlers
Syriac and Latin Pastoral keyed by start date; Era 1b: 15 rows; Eras 2–9 unchanged;
V0_3 superseded); census browser republished at the same URL with eras 1a–9
(script execution verified); spec open-question #2 marked partially resolved.

**Drafted, parked for handoff — four era-positioning description lines** (spec
§2.4a, copy-paste ready): Chloe "formed before Constantine — a church with no
empire behind it"; Mar Yausep "spans the divide — and from the other side of it";
Papnoute "formed in the empire's first Christian century — when the harder question
had become what faithfulness costs once it is safe"; Albina "formed in the imperial
church's high noon — and walked away from what it offered." **These touch
`cic-poc`'s manifest descriptions and are therefore the front-end thread's to
implement, after Prototype Testing 1 — a note was added to that thread's decision
log.** Nothing in the live app changes now.

**Next action:** none on this thread for the split. Remaining open: the other era
boundaries' confirmation, Lane 4 label, un-run-era register rendering,
standalone-demo question.

---

## 2026-07-16 (sixth pass) — Raised, not decided: split map-Era I at Constantine? Recommendation given

**Mark's question:** should the early-church era parallel the Constantine dating for
credibility, with Phase 1's launch framed as early-church worlds plus "one world
from the next era" included to demonstrate cross-era conversation?

**Fact-check that shapes the answer:** the nine Phase One worlds distribute around
Constantine as 2 cleanly before (House-Churches, Alexandrian), 2 straddling
(Syriac, Latin Pastoral), 5 after (Desert, Donatism, Cappadocian, Imperial,
Hieronymian) — and two of the four live worlds are fully post-Constantine. The
"one world from the next era" framing would therefore be untrue as stated; flagged
plainly rather than adopted.

**Recommendation given (Option A): split the MAP era, keep the PHASE.** Era Ia
"The Early Church Era, 70–312" (matches Cambridge Vol 1, Origins to Constantine —
the field's most recognizable break) and Era Ib "The Imperial Church Era, 312–451"
(González's own 'imperial church' language). Phase One remains 70–451 per its Step
0 record (creed-to-council rationale untouched — re-opening the phase window is
not this thread's call). Launch framing becomes: "Phase 1 deliberately spans both
eras, so a voice formed before Constantine's revolution can sit beside one formed
after it" — the cross-era demonstration Mark wants, already true of the existing
live set (Chloe before; Papnoute and Albina after), no re-selection needed.
Alternatives named: heavy in-era Constantine divider (Option B, lighter but loses
the textbook-match claim); re-dating the era with the one-demo-world framing
(Option C, fails honesty and re-litigates Step 0).

**Heart question posed with it:** whose credibility is being protected — the
Article 31 scholarly reviewer (already served by the record's stated rationale) or
the first-time participant (for whom "Early Church ends at Constantine" is the
shelf they know)? Option A serves the second without disturbing the first.

**Next action:** Mark decides. If Option A: era table and titles update (Ia/Ib),
census re-keys Era 1 rows across the two eras by span, atlas Era I section gains
the split, spreadsheet/browser regenerate — statuses and the Step 0 record
untouched throughout.

---

## 2026-07-16 (fifth pass) — Mark approved the full gap list; census V0.3 built (147 → 172)

**Decided by Mark:** "include all" — every Tier A and Tier B recommendation from the
external review, plus the register addition. Applied in full as **Amendment B** to
the Atlas and as **census V0.3**.

**What was added (25 entries):** Tier A — the Baptists (VII.16); Ottoman-era
Orthodoxy/millet/neomartyrs (VI.17); Korean Catholic origins (VIII.21); St. Thomas
Christians at Diamper/Coonan Cross (VI.18); the Sayfo and Syriac diaspora (IX.19);
modern Ethiopian & Eritrean Christianity (IX.20); Philippine Catholicism (VI.19);
Union of Brest (VI.20) and the Ukrainian Greek Catholic underground (IX.21); the
Russian new martyrs and catacomb church (IX.22); colonial Latin American devotional
Catholicism (VII.17). Tier B — Scandinavian conversion (III.14); Georgian golden age
(IV.15); Serbian/Bulgarian monasticism (IV.16); Kyiv-Mohyla (VI.21); Laestadianism
(VIII.22); Plymouth Brethren (VIII.23); Sunday School/Bible-institute movement
(VIII.24); SVM/Edinburgh 1910 (VIII.25); Indonesian Christianity (VIII.26);
NE-India revivals & Mar Thoma (VIII.27); post-Vatican-II parish world (IX.23);
Lausanne-era evangelicalism (IX.24); African diaspora/reverse-mission churches
(IX.25). Register — Ratana & Pacific adjustment movements (IX.26, floor-question
status with question-framed copy). Tier C applied as two stated scope rules
(formation communities, not schools of thought; events/councils are context except
where a lived world expresses them) plus the Bible-translation cross-era theme
thread, all added to the Atlas's cross-era observations.

**Artifacts and files updated:** Atlas (Amendment B header note; all entries marked;
counts updated to ~135 within-floor + ~26 register); `CiC_World_Atlas_Census_V0_3.xlsx`
generated (172 rows; Era counts 26/12/14/16/13/21/17/27/26; V0_2 file retained as
record but superseded); census browser artifact republished at the same URL with all
172 entries (script execution verified). **All four lane-silence problems the review
found are now fixed** — Syriac, Ethiopian, St. Thomas India, and Latin American lanes
now run to the present or their true ends.

**Next action:** none pending on the census. The standing open questions (era
titles/boundaries confirmation, Lane 4 label, un-run-era register rendering,
standalone-demo question) remain with Mark; the atlas and census are now the stable
content spine for any future map visual-design pass or Step 0 run.

---

## 2026-07-16 (fourth pass) — External review: the Atlas against the field; gap list produced

**Mark's direction:** deep review against other church/Christian history sources and
maps — how do we fit, what is missing.

**Produced:** `Ministry/Technology/World-Orientation-Map/CiC_World_Atlas_External_Review_V0_1.md`
(artifact published), checked against the Cambridge History of Christianity's
nine-volume periodization (web-verified volume boundaries), Noll's *Turning Points*
(web-verified 14-moment list), González, Latourette's "Great Century," MacCulloch's
braided-strands structure, the World Christian Encyclopedia bloc taxonomy, and the
participant-visible products (Rose timelines, UsefulCharts/ARDA denominational
family trees).

**Finding — fit is strong and the divergences are deliberate:** era boundaries track
Cambridge within a decade nearly everywhere (1815 exact; 1650 vs 1660; 622 vs c.600;
1054 vs c.1100); our start (70 CE) and Era I/II hinge (Chalcedon 451) are two of
Noll's canonical turning points; the lanes are MacCulloch's braided-strands
architecture; the adjacent register independently reproduces — with stated grounds
instead of a bare label — a category the WCE also found necessary ("marginal
Christians"). Three knowing divergences, each one-sentence-explainable: no
Constantine break (the Step 0 record put that rupture inside Era I as a selected
world); Azusa 1906 over Cambridge's 1914 (church-internal hinge over geopolitical
one); splitting the late Middle Ages (where our women's/ordinary-voice candidates
cluster). **Heart:** recognizable to anyone who knows the standard shelf, honest
about where and why it differs — the same posture as everything else.

**Finding — what's missing, prioritized (recommendations only; census unchanged
pending Mark's yes):** Tier A (~10 rows): the Baptists (the census's most
conspicuous omission); Ottoman-era Orthodox parish life and neomartyrs (a
three-century Orthodox hole); Korean Catholic origins; St. Thomas Christians at
Diamper/Coonan Cross; the Syriac lane's modern chapter (Sayfo + diaspora — the
'longest lane' currently goes silent after ~1300, which reads as erasure); modern
Ethiopian/Eritrean Christianity; Philippine Catholicism (currently present only via
an adjacent-register entry — an inversion); Eastern Catholic/Uniate worlds incl. the
Ukrainian underground church; the Russian new martyrs/catacomb church; colonial
Latin American devotional Catholicism (a 250-year lane hole). Tier B (~12 rows,
selective): Scandinavian conversion + Laestadianism; medieval Georgia;
Serbian/Bulgarian monasticism; Kyiv-Mohyla; Plymouth Brethren; Sunday
School/Bible-institute formation; SVM/Edinburgh 1910; the post-Vatican-II parish;
Lausanne evangelicalism; Indonesian Christianity; NE-India revivals + Mar Thoma;
diaspora/reverse-mission churches. Tier C: scope-rule notes (schools of thought are
not formation communities; only bounded windows for unbounded '-isms') plus a
Bible-translation cross-era theme thread borrowed from the Rose-chart tradition.
Approving A+B grows the census 147 → ~170 and fixes four lane-goes-silent problems.

**Next action:** Mark approves/edits the gap list; V0.3 of the census (spreadsheet +
browser + atlas) folds in the approved rows.

---

## 2026-07-16 (third pass) — User-facing era titles; the census becomes a spreadsheet; Step-0-identified-but-unbuilt worlds made first-class with their reasons

**Mark's direction:** dates alone aren't enough — eras need clear titles a user
recognizes ("Reformation Era," "Enlightenment Era"); the census should live in a
spreadsheet; and the worlds Step 0 identified for the early church but did not build
must be included with the explanation of why the world ecology wasn't built for
conversation.

**Decided — nine user-facing era titles (proposals, dates kept visible):** The Early
Church Era (70–451, fixed by record) · The Age of Monks and Empires (451–622) · The
Early Medieval Era (622–1054) · The High Medieval Era (1054–1300) · The Late Medieval
Era (1300–1517) · The Reformation Era (1517–1650) · The Enlightenment & Awakening Era
(1650–1815) · The Missionary Era (1815–1906) · The Global Church Era (1906–present).
Applied to the Atlas's own headers; the old evocative names survive as taglines.
**Heart:** the era title is the first orientation a participant gets — it should
land on words they already half-know, with the honest dates right beside them.

**Produced — `CiC_World_Atlas_Census_V0_2.xlsx`** (same folder): four sheets — Read
Me (status legend + reading discipline), Eras (the nine titles), World Census (147
entries, filterable, status-color-coded, with columns for sourcing signal,
floor/eligibility note, key relations, and a participant-facing "Why it isn't open
for conversation" for every row), Status Summary (counts: 4 Live, 5 Selected-Not-
Yet-Built, 4 Deferred, 7 Possible-Future on record, 96 Pre-Survey Candidates, 17
Floor-Question register, 4 C1-excluded, 2 C2-excluded, 4 Contested-Evidentiary, 6
Within-Another-World, 2 Outside-Scope). Deliberately formula-free — a data snapshot,
not a calculating model, counts computed at generation and labeled as such. A
matching filterable HTML census browser was published as an artifact so the full
content is readable in the side panel, and verified by executing its script
(9 eras / 147 rows / render clean).

**Decided — every Step-0-identified-but-unbuilt world is a first-class census row
with its recorded reason:** the five Selected-Not-Yet-Built worlds; the deferred
(Armenia, Aksum, Persian Church of the East, Antiochene, Cyrilline Egypt, Jerusalem
pilgrimage); the possible-future entries including Tertullian's "dropped voice" and
Pelagianism's eligible-but-too-thin proof case; and the exclusions with their
distinguishable grounds (C1 floor, C2 person-defined, contested-evidentiary), each
carrying participant-facing draft copy. Era I's 26 rows are the Phase One record
verbatim, not new judgments.

**Next action:** Mark reviews the spreadsheet and census browser alongside the
Atlas. Standing open questions unchanged (era titles now added to the list for his
confirmation).

---

## 2026-07-16 (later) — Reframe: the map is a pre-Step-0 instrument; World Atlas V0.1 produced; spec corrected against the real Step 0 record

**Mark's redirection, in substance:** the map is a "pre-0 step / Step 0" layer, not a
downstream product of the build pipeline. The only nine identified worlds are Phase
One's own Step 0 output for the early church era; what this thread should produce is
a full research pass of all academically identified candidate worlds across Christian
history sitting within or next to the Nicene-creed principles — content that (a)
fills the map's entry screen so users can pick eras or individual movement worlds,
and (b) becomes the standing candidate pool each future phase's Step 0 draws from.
Explicit instruction: don't be bound by the documents governing what happens *after*
a world is built.

**Read for the first time this session, and it corrected real errors:**
`CiC_Step0_Conclusion_FINAL_v2.docx` (Phase One World Selection, merged final) and
`CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`. Corrections forced into the
spec (logged as Amendment A there): Phase One's window is 70–451 (Chalcedon), not
70–430; Step 0 selected NINE worlds of which five are Selected-Not-Yet-Built
(Alexandrian Catechetical, Donatism, Cappadocian, Imperial-Juridical, Latin
Pastoral-Congregational) — the V0.1 spec had missed Donatism, Imperial-Juridical,
and Latin Pastoral entirely and understated Alexandria and the Cappadocians as mere
"candidates" when they are selected worlds with recorded reasoning. **Lesson worth
keeping: the spec's first census was drafted from the front-end log plus repo
inspection without finding the Step 0 Conclusion — the project's own prior decisions
must be searched for harder than that before content is invented in their place.**

**Produced:** `Ministry/Technology/World-Orientation-Map/CiC_World_Atlas_PreStep0_Survey_V0_1.md`
— the broad-survey layer (Step 0 Methodology, procedure item 1) run across all of
Christian history in advance: nine proposed eras, ~110 within-floor candidate worlds
plus ~25 adjacent-register entries, each with sourcing/ecology *signals* and floor
*notes* in the Methodology's own vocabulary (A1 plain-reading, A2 continuity, A3
interpretive fidelity, A4 hand-selected adjacency, Criterion 2 person-defined),
never verdicts. Era I reproduces the Phase One record verbatim as ground truth —
selections, deferrals, and exclusions with their recorded grounds, including the
open structural questions (Homoian Christianity via A4; Montanism's Phrygian
epigraphy vs. Criterion 2).

**Decided — status taxonomy corrected to process-truth:** Live / In Construction /
Selected-Not-Yet-Built / Deferred-by-Step-0 / Pre-Survey Candidate /
Excluded-with-grounds-on-record. "Selected" and "Deferred" exist only where a real
Step 0 ran; everything in Eras II–IX is a Pre-Survey Candidate regardless of how
strong its signals look. Exclusion grounds stay distinguishable (Criterion 1 vs.
Criterion 2 vs. contested-evidentiary) per the Step 0 Conclusion's own discipline.

**Decided — the atlas renders floor-question movements honestly rather than hiding
them:** the earlier open question ("should floor-excluded movements appear at V1?")
is now half-answered by the record itself — Phase One's exclusions have recorded
grounds and full honest copy is possible today; for un-run eras the adjacent
registers carry question-framed copy. Whether un-run eras' registers ship at V1 or
wait for their Step 0s is the remaining half, still Mark's call.

**Heart reasoning:** the map's deepest claim on a participant is "we will tell you
the truth about the whole landscape, including what we haven't done and who isn't
here." That promise is only keepable if the map's content layer is built from the
project's own real decisions (the Step 0 record) and real method (the Methodology's
own tests as questions) — not from a designer's plausible guesses. Today's
correction is that principle applied to this thread's own earlier work.

**Also drafted (Amendment A additions to the spec):** participant-facing copy for
all five Selected-Not-Yet-Built worlds — including Donatism ("known mainly through
hostile pens... deserves to speak as itself") and Imperial-Juridical ("the era's
least comfortable world"), which will be the map's first real tests of
honest-tension copy.

**Open questions for Mark (carried in the spec, updated):** Atlas review (what's
missing that would grieve him); era-boundary proposals (nine eras; only 70–451 is
fixed by record); Lane 4's grouping/label; adjacent-register rendering for un-run
eras; "notify me" placeholder; standalone-demo question.

**Next action:** Mark reviews the Atlas (primary) and the amended spec. After his
pass, V0.2 folds his census/era corrections in; any actual Step 0 run for a new era
remains a phase-level project decision, not this thread's to start.

---

## 2026-07-16 — Spec V0.1 produced: data model, honest not-yet content, five-step flow, handoff note

**Produced:** `Ministry/Technology/World-Orientation-Map/CiC_World_Orientation_Map_Spec_V0_1.md`
— all four launch-prompt deliverables in one document, published in full to an artifact
for Mark's review. New subfolder follows the existing pattern of this workstream's
documents living under Ministry/Technology.

**Continuity, not invention:** this spec matures the "World Map (Ultimate Vision)"
entry already in the Front-End Decision Log (2026-07-07) — dimmed unbuilt worlds, the
hover/click honesty mechanic, two distinct exclusion reasons — rather than starting
fresh. Where that entry sketched, this spec specifies; nothing in it contradicts that
entry.

**Decided — the map's own elements carry confidence calibration.** Every influence
line drawn between two movements is itself a historical claim, so relationship edges
carry the Constitution Article 17 five-level vocabulary, rendered visibly (solid /
dashed / dotted) with the uncertainty named in words on hover. An edge the evidence
can't support isn't drawn — the map has no Tier-5 arrows, just as worlds have no
Tier-5 stories. **Heart:** the map is the first thing a participant sees; if its
arrows overclaim, the project's honesty posture is broken before any conversation
begins. The landscape view exists because of Conviction 1 (the vast testimony must be
visible as a testimony), and a testimony drawn with invented connections isn't one.

**Decided — build-status taxonomy defined by what has actually happened, not
intention:** Live / In Construction / Identified Candidate / Not Yet Assessed.
Consequences applied honestly: Nicene-Cappadocian is an *Identified Candidate*, not
"In Construction" — its folder exists and is empty, and a map that calls an empty
folder in-construction has broken its own rule on entry #6. "In Construction" is
earned by documents, not folders. Alexandria is an Identified Candidate with real
prior work (V6/V7 track, in Former Versions), named as such in its copy. No informal
fifth status like "probably unbuildable" exists — Source Ecology verdicts come from
running the methodology, never from map-content guessing (coordination boundary held).

**Decided — the eligibility (Movement Scope) field is reserved, not exercised.** The
schema carries it because the 2026-07-07 World Map entry requires the two exclusion
reasons be distinguishable; this thread fills in `affirmed` only for the four Live
worlds and `not_yet_reviewed` for everything else. Gothic Homoian ("Arian")
Christianity — the clearest test case — was deliberately left OFF the V0.1 census
rather than shown with a guessed verdict; whether floor-excluded movements appear at
all is logged as an open question for Mark, since rendering `outside_floor` is a
governance determination this thread has no authority to make.

**Decided — the honest "not yet" copy discipline:** every non-live explanation carries
a three-part frame — (1) real and important, named concretely; (2) the true reason:
one world at a time, four built, and the Source Ecology assessment for this movement
*hasn't happened yet* (never "the sources are too thin," a claim no assessment has
earned); (3) the nearest built neighbor by lineage, as a live suggestion. Copy is
held to the already-decided 10th-grade Level 2 readability floor and the manifest's
own "Richest in… thinner on…" tone. Nine full drafts written (Alexandria,
Nicene-Cappadocian, Byzantine monasticism, Coptic, Benedictine, Anabaptist, Azusa
Street, Black Church in America, Chinese house-church) plus the template; no entry
ships as bare template. **Heart:** the launch prompt's own requirement — absence must
never read as a judgment of unimportance. The unbuilt map is the project's future,
not its discard pile, and the copy's warmth is what makes that true rather than
asserted.

**Decided — interaction grammar inherited, extended to one new content type:** hover
= short honest explanation, click = full depth (the existing lexicon/story/sourcing
mechanic), applied to movements and not-yet explanations as the 2026-07-07 entry
anticipated — plus *figures* (Priestley-style lifespan lines inside bands): clicking
Ephrem or Augustine surfaces the already-decided Facilitator answer (a single
person's exact voice can't be honestly reconstructed; the world that formed people
like them can be) and points to the movement band. The most predictable
disappointment becomes the map's own teaching moment. The click panel aligns with the
already-decided four-option world-click menu (Description / Tour / Choose for Table /
Academic Documents) with the same placeholder discipline.

**Decided — census and lanes are explicitly provisional:** 37 movements spanning
30 CE–present across six lanes plus a non-interactive context strip; every non-Live
row carries `census_confidence: provisional` until Mark reviews it, and the map
itself discloses its era-stretched time scale and that lanes are reading aids, not a
taxonomy of the Church. Visual lineage grounded concretely: Priestley's Chart of
Biography (1765) for figure lifespans, Adams' Synchronological Chart (1871) for
parallel era-dense streams, Histomap (1931) noted but its width-as-importance
encoding deliberately rejected as an unearned historical claim.

**Handoff note written, nothing asked of the front-end thread now:** three take-or-
leave increments — (1) adopt the landscape data + not-yet copy through Ask-the-
Facilitator with zero new UI; (2) map as supplementary "see these worlds in history"
view feeding existing selection; (3) map as the selection surface, with Deep
Interview / Compare Worlds emerging from tray count rather than an upfront toggle.
Integration decision and timing stay with the front-end thread.

**Open questions for Mark (blocking V0.2):** census review (what's missing that would
grieve him); Lane 4's grouping/label ("Africa & the Oriental churches" holds Egypt,
Ethiopia, and Armenia together — defensible, contestable, and Armenia isn't African);
whether floor-excluded movements appear dimmed-with-honest-copy at V1 or wait for a
real eligibility review process; whether "Notify me when this changes" is a real
future feature or an over-promise to cut; whether the map ships as any kind of
standalone demo before integration or stays a design artifact.

**Next action:** Mark reviews the spec (artifact + repo file). No construction, no
code, no census expansion until the open questions above are answered.

---
