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

## 2026-08-31 (still later) — Founding principle stated: the base program is the whole ecology, not the built worlds

**Origin.** After the storyboard's ten-scene revision, Mark stated the
principle underneath it plainly: *"we are building for all the worlds, build
and not, just the built worlds are marked so they can dive deeper. as we
build more worlds we mark those and deepen their content as they come online,
but the base program is about the entire ecology, not the build worlds."*

**Decided.** The Atlas's scope is the full census (292 movements, all ten
eras) as it stands today — not a map of the six built worlds with
placeholders around them. "Built" is one honest attribute a movement can
carry (it unlocks deeper content and a live conversation), never the
organizing principle of what the map shows or how much of it is real. As more
worlds are built, they get marked and deepened in place; the map's own scope
does not grow to catch up with the build — it was already whole.

**Applied immediately.** This ratifies, rather than changes, the same-day
ten-scene restructuring: the earlier seven-scene draft implicitly organized
around the six built worlds, and the fix already moved to organizing around
the real ecology instead. Foregrounded as the storyboard's own leading thesis
(REV 3, both the `.md` and the published artifact) and logged as a captured
decision in `Design/CiC_Atlas_Reimagined_Divergent_Capture_V1_2026-08-31.md`
§10.4, so the reasoning survives independent of this one document's own
revisions.

### Next action

None yet — carries forward as a standing principle for any future work on
this thread, including whichever tool or build eventually gets chosen.

---

## 2026-08-31 (later same day) — Divergent-phase interview, session 1: captured, paused at Mark's request

**Origin.** Following the research thread below, Mark asked to work the same
territory as a live interview instead — his framing, explicit: Sam Kaner's
diamond (divergent → groan zone → convergent), currently in the **divergent**
zone, Claude interviewing him rather than presenting findings. Also set two
governing frames for this whole line of work: (1) sandbox only, the live
system stays untouched until a full replacement exists and is judged clearly
better; (2) this thread is the Atlas/map's own visual and engagement quality
built on what's live — not the surrounding modules (sermon prep, a
curriculum, direct interview/Table access, the separately-scoped
living-movements-today program).

**Output:** `Design/CiC_Atlas_Reimagined_Divergent_Capture_V1_2026-08-31.md`
— a full, theme-organized capture of the session, produced at Mark's request
to pause and hold what had accumulated before continuing. Covers: the felt
qualities wanted (discovery energy, deep engagement, hardships held humbly
not sensationally); organizing lenses (geography, tradition family,
theological distinctives, practices); the core diagnosis (access is solved,
the failure is overview-vs-detail — "a spreadsheet that doesn't fit on the
page, but to get it on the page it's too small"); and an emerging core visual
concept — **a living landscape of time × swim lanes, realized as rivers**
(mapping cleanly onto the existing `formed`/`transmitted to`/`continuesAs`
edges, resonant with this exact build's own internal "Ongoing Streams"
design name), with interaction/tension carried by a small, quiet, scalable
mark rather than a dramatic effect. Nothing in it is decided except three
real rulings, also logged in `CiC_FrontEnd_Decision_Log.md`'s own
2026-08-31 entry: the sandbox constraint, the Hosted Tour staying Phase 2
("don't box the door shut"), and the thread-scope boundary above.

**Heart of it, unchanged from the research thread:** the gap is comprehension
at scale, not missing sourcing — confirmed directly by Mark this session,
independently of the earlier document's own finding.

### Next action

None yet — divergent phase paused, not closed, at Mark's own request. Several
open threads named in the capture's §11 (what a "headline" says, what
"pictures" means in practice, the terrain around the rivers, which tool gets
chosen) are explicitly left for a later continuation of this same interview,
not for this thread to resolve alone.

---

## 2026-08-31 — Research/ideation thread: "Atlas reimagined" (game-grade visuals, linking, sourcing) — explores, does not build

**Origin.** Mark's own words: *"the atlas/map we have is good, but i want to
explore the idea of better graphics, linking and sourcing as a way to help
people see the big picture and not get overwhelmed... i am thinking updated
age of empire details, or even other games that have these interactive worlds
that each have features and connect with eachother."* A pure research/ideation
launch — no code changed, no census edited, nothing decided.

**Output:** `Design/CiC_Atlas_Reimagined_Research_and_Ideas_V0_1_DRAFT.md`.
Reads `atlas-v3.html`/`world-census.json` as they actually stand (already a
sourced connection map with hover-trace lineage, typed/confidence-coded edges,
and a full relational click-sheet — richer than the brief's framing implied),
checks `records/alx/` and `records/pahc/` for real, sourced cross-world
connections the current five edge types can't yet express (a shared source
both worlds cite independently — Eusebius's *Historia Ecclesiastica*; a shared
figure cited for unrelated reasons — Athanasius's Festal Letter 39 inside
pahc's own canon record; a documented "adjacency without asserted contact" —
`pahc.force.alexandria-emergence`), surveys strategy-game campaign maps
(Crusader Kings III, Age of Empires IV, Civilization's tech tree, branching
roguelike maps) and closer non-game analogues (Stanford ORBIS, Pelagios/
Peripleo, museum interactive-timeline design, NYT/Pudding-style
scrollytelling) for mechanism rather than aesthetics, and returns an idea
portfolio organized whole-story → era → world → a world's own features
(gravities/figures/sources/stories, the corpus's own ontology under
`records/<world>/`).

**Two things flagged for Mark's own read, not settled here:** (1) every idea
is checked against the anti-ghost principle (scoped to figures, not map
chrome) and the stillness/reduced-motion posture (motion rare and meaningful,
never ambient) named in `CiC_Full_UX_Design_V1_0.md`, with any idea that would
add real motion or bend either rule named explicitly rather than assumed
clear; (2) the document is explicit that a "these worlds connect" map feature
must never visually merge two different things this project already keeps
distinct — a *sourced historical relationship* (the census edge) and the
Facilitator's own *conversational-contrast* judgment for Table seating
(`CiC_Table_Pairings_V1_2026-08-28.md`'s C6 record, whose own no-foreknowledge
rule states historical acquaintance "no longer matters to the mechanics").

**Heart of it:** the brief's own gap is comprehension at scale, not missing
sourcing or missing connections — both already exist in more depth than the
brief's framing assumed. "Game-grade" should buy a navigable hierarchy over
what's already sourced, not more content or ambient visual motion.

### Next action

Mark's read of the document. Nothing here is authorized to build; any idea
that moves forward needs its own launch thread.

---

## 2026-08-27 (Pass 6) — census 274→292, added by the CORPUS rather than by a Step 0 gate; the pile bar, Mark's override of it, and the Lactantius split

**This entry exists because eighteen movements entered the census without one
of these entries being written, which is exactly the failure this log is for.**
The additions were made across 2026-08-26 and 08-27 by the cross-world corpus
assignment thread (`world-build-docs/_cross-world/`, `cic/corpus-map/`), whose
own records are complete; what was missing until now was any trace of them
here, in the Atlas's own decision record. Census **274 → 287 → 292**, edges
**54 → 69**.

**The mechanism was new and is worth naming.** Every previous addition came
from a Step 0 era gate: a survey ran, candidates were assessed, entries
entered. These eighteen came from the opposite direction. Ten parallel workers
assigning 467 vendored works to Atlas entries kept filing the same complaint,
independently and without being able to see each other: *this material is real
and the census has nowhere accurate to put it.* Eighty-seven works were flagged
`needs-ruling` rather than forced onto a wrong shelf, and the dominant reason
was never doubt about a text — it was a hole in the map. **The corpus audited
the census.** That is a check no Step 0 gate performs, because a survey asks
what movements there were and this asks what survives and where it can honestly
sit.

**Thirteen entries, 2026-08-26.** Seven formation-world candidates
(`gallic-monastic-ascetic-christianity`, `roman-church-third-century`,
`palestinian-ascetic-monasticism-early`, `palestinian-church-pre-constantinian`,
`anatolian-church-third-century`, `gallic-nicene-episcopate`,
`greek-apologists-second-century`); one explicit shelf that says so on its face
(`apocryphal-and-pseudepigraphal-literature`); five **Floor Question
(register)** entries for material the corpus carries *about* a movement
(`anomoean-eunomian-christianity`, `pneumatomachian-current`,
`apollinarian-christianity`, `modalist-monarchianism`, `bardaisanite-current`)
— registered as questions, not as exclusions, because no Phase One record rules
on any of them by name and these entries do not invent one.

**THE BAR WAS A PILE, AND MARK OVERRODE IT ON 2026-08-27.** Those thirteen were
each added for a *pile* of misplaced works — eight for Gaul, seven for Anatolia,
fifteen for the Greek apologists — and five further regional gaps were
DECLINED on that same ground, with the declines written down rather than
quietly dropped. Mark's ruling: *mint the thin entries for all five.* The
reasoning is one line and it is the whole of Pass 6's heart — **an accurate thin
entry beats an inaccurate thick one.** A world nobody has built yet is still
better served by a bucket that names it than by being shelved under a
tradition it does not belong to; the map's job is to be honest about what the
church has been, and a wrong shelf is a quiet lie about a real body of people.
So: `latin-apologists` (I.43), `roman-church-gregorian` (II.18),
`danubian-latin-christianity` (I.40), `aquileian-christianity` (I.41),
`antiochene-church-third-century` (I.42). Each carries its own thinness in its
`why` field — I.42 holds **one work, three thousand words**, and says so.

**What the override did NOT do.** It did not settle anything a worker had
refused to settle. Lactantius was held back deliberately, so that a ruling he
was owed would not arrive as a side effect of one about somewhere else; Mark
ruled him separately the same day, into `latin-apologists`. **That ruling splits
the author, which is what *per work* means.** The *Divine Institutes* and its
three companions move — about three hundred thousand words, quadrupling the new
entry's corpus. *Of the Manner in Which the Persecutors Died* does not: written
c. 314–15 from inside the Constantinian settlement, it is **load-bearing for a
built world** (`ijc.source.lactantius-de-mortibus`, cited by
`ijc.figure.constantine` and `ijc.gravity.church-state-alliance`, and recorded
in `ijc.search.f6-e-negative-sweep` as that world's only licensed source
reaching back before 312). Following the author would have stripped a live world
of a source it depends on, which is what the non-exclusivity rule exists to
prevent.

The two attribution questions (the *Passion of St. Symphorosa* under Julius
Africanus' name, the Maximus of Jerusalem fragment) are untouched by any new
entry, because a new shelf does not answer a doubt about who wrote something.
Flagged works fleet-wide: **87 → 2**.

**Verification:** census validator clean at 292 movements / 69 edges / 10 eras;
`cic/engine/corpus_map.py` valid at 718 assignments across 56 entries; 14/14
corpus-map tests; `engine.m1.cross_world` 0 new defects.

**Next action:** two flagged works remain and both are Mark's, and both are
**attribution** questions rather than shelving ones — no further entry can
answer either. Nothing is blocked on them; the map is valid and usable as it
stands.

---

## 2026-08-14 (Pass 5) — ERA 10 FROZEN by Mark; census 257→274; the Living-Era Protocol ratified; the ten-era Step-0 build COMPLETE

**Decided (Mark): "freeze what is there"** — which under this project's
standing convention means apply each gate question's stated lead lean, every
question carrying one precisely so the ruling is unambiguous. Applied across
all twelve questions of `CiC_Step0_Era10_V1_0.md` §6, after two review rounds
(R1: 8 substantial; R2: 9 substantial, its central lesson being that two R1
fixes had landed in the era doc's prose while the identical defect stayed live
in the candidate JSON that actually enters the census).

**Q1 — the Living-Era Protocol Addendum V1.0 RATIFIED AND FROZEN**, all six of
its own §5 sub-questions per their stated leans (the frame and merits-based
living definition; R1–R2 per-entry A3 with dated own-voice citation; R3's
CD/CR grades with the validator's confidence vocabulary untouched; R4–R6
humility, safety, ends and the verified-anchor bar; R7's recency floor; R8–R10
boundaries and review teeth). Its own header is stamped ratified. The A1.E10
run had operated under it; ratification at its own gate makes that
retroactively lawful, and it now governs every Step 0 assessment touching a
living movement — the census has no successor era to keep era 10 honest, so
the regime does.

**Q3 — SEVENTEEN candidates entered, IX.33–IX.49; census 257→274.** The
Mark-mandated fundamentalist–modernist cluster (IX.33 Fundamentalism, IX.34
the Social Gospel, IX.35 the Mainline Century — the three pieces of Mark's own
Era-9-gate hesitation, one connected story); the live-session mandates (IX.36
New Calvinism with R7's recency stated in the open, IX.48 American Orthodoxy,
IX.49 Hebrew Roots as the weakest of the seventeen, drafted so declining it
would have been on the record); the banked-flag executions (IX.37 Indonesia
and IX.38 NE India/Mar Thoma per the Frozen E9 Q3 fork, IX.39 Malankara
completing the scope note written into Frozen VIII.27, IX.40 Georgia answering
the E9 gap ruling's own condition, IX.41/IX.42 the two Stone-Campbell wings
with the third stream disclosed in-row, IX.44 completing Frozen VIII.10's
charged case); the completeness finds (IX.43 the Black Church in the twentieth
century — the roster's largest single hole, IX.45 the charismatic renewal,
IX.46 the WCC, IX.47 the Catholic 1906–1962 segment). **IX.50 (the Christian
Right / Christian Nationalism current) was HELD — deliberately excluded from
this pass, pending a separate direct ruling from Mark.** Nothing was pre-wired
for it: no row, no relations lines, and neither of the IX.24 or IX.33
disclosure clauses that ride its own question (Q12 held in full). The two
structural boundary leans were applied: the Frozen-era-9 register rows'
era-10 segments (LDS/JW/Christian Science/Christadelphians) deferred to
one-line disclosures at a later gate rather than given rows now, and
MacArthur/Grace to You placed as named lines in IX.33's continuation lane
rather than packed into IX.36.

**Q2/Q4/Q5/Q6 — the era's own record.** Tier list and statusWords frozen, with
the living-era clause the addendum requires: every frozen status on a living
row now says on its face that it is a dated reading. Dates: the
era-boundary-is-present reading of the Frozen register-cap convention; the
eleven-row living/end mismatch classification (3 documented-terminus, 6
episode-end, 2 unsupported artifact) with its nine rationale writes; IX.15's
1993 end → present (no such event exists in either research run — the
addendum's own predicted first case, confirmed); IX.16 start → 1914; IX.17 →
1929–1993, both ends of a window-fill band replaced; IX.3's end → 1977 on
Luwum's martyrdom, the one case where a documented event could replace a soft
decade-end; IX.4's start deepened to the 1880s; IX.10 kept at the 1940s with
the Girgis material disclosed rather than absorbed; IX.28's end kept with its
rationale saying plainly that it is a judgment, not a terminus; IX.29's
31-year overlap acknowledged and kept. Every changed date carries its
`dateRationale` with the "(Era 10 Freeze, Mark, 2026-08-14)" stamp. Register
dispositions RECORDED — IX.15 the era's one record-mandated case, staged per
body, with UPCI's Articles cited by Manual year and **PAW's and ALJC's gaps
recorded OPEN and named rather than filled**, and its argued `c2:null` counted
as the criterion's fourteenth live application (a clear by inapplicability).
The criterion's TENTH through SIXTEENTH live applications recorded in
ascending roster order — IX.4, IX.5, IX.7, IX.14, IX.15, IX.16, IX.26 — with
IX.17 the one stated exclusion, and the Frozen VIII.10 completion recorded
both ways (the finding on IX.44, a one-line closure note on the Frozen row).

**Q7/Q8 — successions and edges.** VIII.11→IX.22, found in the file but
unlisted in the Frozen E9 record, RATIFIED. Five Frozen-era writes riding
adoption: VIII.26→IX.37, VIII.27→IX.38, VIII.1→IX.43, VIII.25→IX.46, and the
VIII.29 re-point (VIII.29→IX.47→IX.23 replacing VIII.29→IX.23 — a Frozen-write
amendment, named rather than made silently), plus the era-10-internal
IX.9→IX.48. Both named NOT-writes honored: no VIII.3 chain write (identity
cannot split two ways), and no VIII.32→IX.27 write — that relation stands as
kin with its nine-year 1906–1915 seam DISCLOSED, the census-corrected finding
that overturned the survey's "seamless" reading. Three edges written, census
21→24: the census's second "in tension with" edge, IX.33↔IX.35, graded
Documented on both sides' own dated rupture texts (1910 / 1922 / 1923 / 1924),
with the Social Gospel named inside the note rather than given a second edge;
and the two VIII.3 'formed' edges to IX.41 and IX.42, both graded Documented
on the verified 1906 federal-census listing — a grade the Round 2 review
supplied because the validator requires one on every edge and "left to Mark's
call" would have written two edges it rejects.

**Q9/Q10/Q11 — the row-level work.** IX.31 (Deconstruction) is the recency
floor's first live case and it fails the marker's time prong; it is RETAINED
by Mark's hand-selection with the recency named on the row's own record and
logged here, on institutionalization legible across independent sources, a
survived founder-adjacent transition, and this row's unique stake — the map
here maps its own visitors. The R4 prose sweep's words applied to all thirteen
flagged rows, including IX.24's `regions[]` coding fix; **the IX.20 stale-line
replacement text was BANKED and NOT written, exactly as the question
required** — a Frozen-adjacent touch for whenever that row is next opened. The
sources[] landing confirmed in its true split shape: the 167 row-keyed items
onto this era's 32 existing rows, the 44 extra-topic items riding their
candidates as inline anchors, with X.10's base banked to the MacArthur forward
flag.

**The one item stopped rather than guessed at: IX.16's row-split lean.** Q5's
mild lean was to split Iglesia ni Cristo out to its own register row. That is
not executable as written at this gate — no draft entry for the new row exists
anywhere in the era's inputs, so applying it would mean inventing a whole
field set rather than copying one; it would take the census to 275 against
this gate's own stated 257→274 arithmetic; and it would need an atlasId out of
the same numbering space IX.50 is being held in. Everything else in Q5 is
applied, including the per-body floorNote clauses that question says land
either way. The split is banked forward as a live, un-executed question needing
a drafted row.

**Verification:** validator 274 movements, 24 edges, 10 eras — 0 errors, 0
warnings. Counts re-derived directly from the census rather than taken from
the era doc, whose arithmetic two review rounds had already caught out
repeatedly.

**This completes the ten-era Step-0 build.** Eras 3–10 are Frozen; the census
has run 178→274 across this sequence of gates. Era 10 has no successor era to
bank flags to, which is exactly why the Living-Era Protocol was ratified with
it: the regime, not a future era run, is what keeps a Frozen reading of a
living story honest.

**Next action:** Mark's direct ruling on IX.50 (adopt as a Tier-3 row with its
B2 thinness in its own copy and the IX.33/IX.24 disclosure lines, or no row at
all with those lines only) → A1.R12 (Eras 1–2 revalidation, carrying the five
pre-gate chain writes and the Augustine→Geneva edge) → the standing
maintenance lanes (the seven-era draft-base queue, the CHC9 TOC verification
debt, the A3 statusWord harmonization backlog, the IX.16 split's drafted row).

---

## 2026-08-05 (Pass 7, UI 29) — Same-family movements clustered into proportional zones instead of interleaved across the canvas

**Mark:** "can we do a better job of having the same lanes (catholic,
orthodox, etc.) nearer each other and not all mixed in with each other."
The heart of it: color is how this map says *family*. A family whose
boxes are sprayed across the full width doesn't read as a family at all
-- a participant can't see a tradition holding together through an era,
which is one of the few things a picture of history can do that a list
can't.

**Measured before diagnosing anything:** Era 9 has 51 movements across 9
families but 32 left-to-right family transitions when its rows are
sorted by x, against a theoretical minimum of 8 -- same-family members
were roughly 4x more scattered than they needed to be. The complaint was
real and quantified before a line was written.

**Two compounding causes, traced against real named cases rather than
guessed at:**

1. `tryPack` gave every family present in an era exactly ONE anchor
point, regardless of how many members that family actually had that era.
Era 9's oversubscribed Protestant & Evangelical block (~20 members) and
its single-member Caucasus entry got equally-sized shares of the anchor
row. Traced live: `armenian-christianity-zartonk`, Era 9's only Caucasus
entry, wanted x=362 and landed at x=2047 -- the pitch grid near the
shared anchor row was already claimed by the oversubscribed families
packed into the same evenly-spaced points, so its free-gap search fell
through to whatever slot was left, deep inside unrelated families.

2. The parent-position blend weights the parent 0.55 against the
family's 0.45, so a movement whose parent belongs to a DIFFERENT family
-- common and entirely legitimate (`alexandria-catechetical`/Africa
descends from `post-apostolic-house-church`/Origin) -- can be dragged
clean out of its own family's territory. Traced: without a clamp its
want came out at 332 instead of its own Africa zone's ~583–697, landing
it inside Origin's cluster and taking Era 1 from its achievable
4-transition minimum up to 6.

**Fix, both halves at once.** Each family now gets a ZONE sized in
proportion to its actual era-native member count (stacked-bar style, in
`FAM`'s own k-order, so a family tends to occupy the same relative
stripe from one era to the next), with each member targeting a point
spread across ITS family's zone by birth order instead of every member
converging on one shared point -- so the free-gap search seats
same-family boxes next to each other rather than scattering the overflow
into whoever's anchor happened to be nearby. And the parent-blended
`want` is re-clamped back into the movement's own family zone: a
foreign-family parent still biases where WITHIN the zone a child lands
(still nearer the parent's side of it) without breaking the family block
apart. Identity succession still overrides the clamp -- it has the
stronger, more specific claim on a column.

**The costs, disclosed rather than buried.** Family transitions across
all ten eras at 1280px dropped from ~161 to 150, with the wins
concentrated exactly where the scattering was worst (era 7: 18→14, era
8: 16→14, era 9: 32→29, era 10: 24→23) -- but eras 1 and 2 each
REGRESSED by one. Small eras are highly sensitive to the residual
tension between the parent pull and the zone clamp, and that is stated
here rather than averaged out of sight. Canvas width: 1280px desktop
unchanged at 2840px; 390px mobile grew 2010 → 2250px (+11.9%). Giving
every family real proportional room costs width -- that's the honest
trade, made two commits after UI 27 spent its whole effort winning width
back, and taken deliberately because the eras where scattering was worst
are the eras where legibility was worst.

**Verified independently, not by trusting the implementing agent's own
report:** the family-transitions measurement was re-run directly and
returned identical numbers; `git diff` was read to confirm the
foreign-tail exclusion computation has no reintroduced same-family
exemption (the exact defect Wave 4 fixed and UI 27 tuned) and that none
of the List view, hover-tip, sticky-header or era-banner code from UI
23–28 was touched; visual spot-check on Era 9 shows same-hue tails now
grouped in contiguous bands instead of scattered. `shoot.mjs` unaffected
(foreignTailOverlaps 0, overlapGroups 0, jsErrors none, 257 nodes);
`validate-census.mjs` 0/0.

**Next action:** none pending. The eras 1–2 one-transition regression is
the live loose end -- worth revisiting only if the residual parent-pull/
zone-clamp tension shows up somewhere a participant would notice, since
on eras that small the difference is one box.

---

## 2026-08-05 (Pass 7, UI 28) — Controls bar, era header and orientation line pinned while scrolling right; a sticky element as wide as its container is just `static`

**Mark:** "can we have the header and era dividers slide to over the
open screen so we don't lose the information if we scroll right." A
direct consequence of the desktop canvas legitimately running wider than
one screen -- UI 27 brought the width back down, but back down to
2840px, not to viewport width. Scroll right into a crowded era and you
lost the search box, every filter, and the era label at the same time:
no way to tell which era you were in, what its dates were, or to search
your way out. Losing your bearings is the specific failure this whole
map exists to prevent.

**Confirmed before touching anything:** a real wheel-scroll test put
`#controls` and `#orientText` at `left:-1560px` at max scroll -- fully
gone, not merely drifting. `position:sticky` only tracks scroll within
an element's own containing block, and both were ordinary
viewport-width page-flow siblings even though `#wrap` (nested several
levels down) is what makes the whole page scrollable to the canvas's
real width. Era headers already worked, since `.erahead` genuinely spans
the full canvas (`left:0;right:0`) -- but `.bar`, the visible
title/tag/dates box inside it, sat at the far-left edge of that span
with nothing holding it in view, so it got `position:sticky;left:.8rem`
on the horizontal axis only (vertical position still comes from
`.erahead`'s own `top:${y}px`, set once per era in JS).

**The wrong turn, recorded because it is the instructive part.** The
first attempt widened the sticky element itself -- `#controls` set to
the canvas width. That made it WORSE, not better: zero sticky effect,
computed `position` still reporting "sticky" while it tracked scroll 1:1
exactly like a static element. The rule that fell out of it: **a sticky
element needs SLACK -- room between its own width and its containing
block's width -- or it has nowhere to travel; one exactly as wide as its
containing block is `position:static` in all but name.** `#orientText`
had been working all along for precisely that reason: its PARENT
(`#orient`) is what gets widened while the paragraph itself stays
narrow. So `#controls` now sits inside a new dedicated `#controlsWrap`,
widened to canvas width `W` in `layout()`, with `#controls` itself
capped near viewport width (`max-width:100vw`, plus matching caps on
`.row1` and `#filterPanel`) so the actual buttons and search stay
compact instead of stretching into a mostly-empty wide wrapper.
Widening `<main>` would have given the same slack and was rejected: it
would also have stretched the footer and glossary prose to an
unreadable line length.

**How the wrong turn ended: an isolated minimal-HTML reproduction** -- a
sticky div inside a container of exactly its own width -- rather than
another round of reasoning against the full page. That settled the
"sticky needs slack" question in one shot, where reasoning about the
real file had already produced one confident wrong answer. Worth
reaching for earlier next time: this file is large enough that arguing
about it from the inside is slower than building a five-line copy of the
thing in question.

**A testing-method note worth carrying forward:** `window.scrollTo()`
gave unreliable, truncated scroll positions while checking this -- far
enough short of the true maximum to make a broken state look partly
working. `page.mouse.wheel()` produced realistic, full-range results,
and the final verification used it out to the true max `scrollX` of
1560px. On this page, drive horizontal scroll with the wheel, not
`scrollTo`.

**Desktop only, by design.** Mobile never needed it: since UI 22 the
wide content lives inside `#mapViewport`'s own contained pinch-zoom
pane, not the page's own scroll. Confirmed unaffected --
`#controlsWrap` and `#controls` both report 390px on a 390px viewport.

**Verified:** `shoot.mjs` unaffected (foreignTailOverlaps 0,
overlapGroups 0, jsErrors none, 257 nodes, mobilePinchChangedScale
true); `validate-census.mjs` 0/0; wheel-scroll to the true max scrollX
confirms `#controls`, `#orientText` and the era header all stay pinned
at left:0/12.8px throughout the scroll, not just partway into it.

---

## 2026-08-05 (Pass 7, UI 27) — Canvas-width regression: one spacing constant had been doing two different jobs

**Mark:** "on the desktop the width is no longer fitting on one page." A
real regression, and one this session caused: the Wave 4 box-vs-foreign-
tail overlap fix (44 → 0 overlaps) correctly stopped exempting
same-family ribbons from each other's box-clearance zones, and the
canvas paid for it.

**Root cause:** the exclusion-zone formula was reusing `GAPb` -- the
12px tail-to-tail PITCH constant -- as the box-clearance buffer too, on
top of a full `NW/2` box half-width. One constant serving two
conceptually different purposes, so every excluded ribbon was
double-charged for clearance. With same-family exemptions gone, each of
the ~23 concurrent movements in the densest era paid that extra 12px on
both sides; the canvas ballooned from 2600px to 4640px at a 1280px
viewport, nearly double. `GAPb`'s job is tail-to-tail spacing on the
pitch grid. It was never the right number for "a box must not visually
touch a foreign tail."

**Fix:** split the two purposes into two constants. `boxClear=4` now
carries box-vs-foreign-tail clearance on its own, empirically tuned as
the smallest value that still holds `foreignTailOverlaps` at 0 -- 2px
was tried and reintroduced 2 real overlaps, so the floor was measured
rather than assumed. The canvas came back to 2840px/2010px at 1280/390px
-- close to the pre-fix baseline instead of nearly double it -- with the
overlap fix itself completely untouched. Which was the whole point:
overlapping boxes and tails are a correctness failure and a
double-width canvas is a usability failure, and the fix had to keep the
first solved while undoing the second.

**Worth keeping:** neither number is derivable from first principles;
both were found by measuring. The durable part of this entry is that the
two costs are now independently tunable, so the next time either one
needs to move it can move without silently paying for the other.

**Verified:** `shoot.mjs` unaffected (foreignTailOverlaps 0,
overlapGroups 0, jsErrors none, 257 nodes); `validate-census.mjs` 0/0;
`#wrap` width measured at both 1280px and 390px before and after.

---

## 2026-08-05 (Pass 7, UI 26) — Hover tip stuck open and following the cursor: paired enter/leave replaced with state re-derived on every move

**The report:** "it sticks open and follows the arrow around and i cant
get it to close." That is two failures in one sentence, and the second
is the serious one -- a tooltip you cannot dismiss stops being a hint
and becomes an obstruction that trails the cursor across the whole map,
with a page reload as the only exit. Everything this map asks a
participant to do is pointing at things; a mode where pointing makes it
worse is disqualifying.

**Root cause, found rather than guessed.** The tip's hide logic lived in
a `pointerout` listener that only fired when its event target was inside
a `.node`. But `layout()`/`relayout()` -- triggered by resize, the
filter toggle, and the list/map toggle -- fully REMOVES and rebuilds
every `.node` element on every call, a behavior already documented in
`relayout()`'s own comment for an unrelated opacity bug. If that rebuild
happens while a node is hovered, the DOM element is destroyed without
ever dispatching a leave event, orphaning `tip.style.display="block"`
permanently; and the old `pointermove` handler had no check that the
pointer was still over anything at all, so it dutifully kept
repositioning whatever was left showing -- which is exactly the "follows
the arrow around" half of the report. The same gap existed for thread
hover: `#art`'s `pointerover` had no hide path whatsoever.

**The shape of the fix matters more than the fix.** The tempting move
was to add another leave path to the paired enter/leave state machine.
Instead the pairing was removed: a single `pointermove` handler now
re-derives hover state fresh on every move via `ev.target.closest()` --
node, thread, or neither -- with one `__hoverKey` recording what the tip
currently shows, and a `pointerleave` safety net for leaving the canvas
outright. This is self-healing rather than stateful: even if a relayout
silently destroys the hovered element mid-gesture, the very next move
(which always fires, because it depends on no paired event) correctly
detects that the pointer is no longer over anything and closes the tip.
A state machine that can desynchronise from a DOM that rebuilds itself
underneath it was the bug; not having one is the fix, and that
generalizes past this one handler.

**Verified:** `shoot.mjs` unaffected (hoverTipVisible true,
foreignTailOverlaps 0, overlapGroups 0, jsErrors none);
`validate-census.mjs` 0/0; and a targeted Playwright reproduction of the
exact mechanism rather than of the symptom -- hover a node, destroy and
replace its element with no leave event (what a relayout does
mid-hover), then move off it -- confirms the tip now hides on the very
next move, precisely where the old code left it stuck, and that hovering
a fresh node afterwards still works normally.

---

## 2026-08-05 (Pass 7, UI 25) — Era banners to two lines on desktop; the tag joins the title line

**Mark's follow-up:** on desktop the era banner -- era number, title,
tag, dates, key events -- was wrapping to three lines even though there
was plenty of horizontal room going unused. The era banners are the
map's ruler: they're what tells a participant where in history they
currently are, and three lines of banner per era is three lines of
history not on screen, repeated ten times down the page.

**The fix, and the near-miss inside it.** The forced flex line-break
lived on `.tag` (`flex-basis:100%`) -- needed on mobile, where that line
is genuinely tight. The obvious move, putting `flex-basis:100%` on
`.dates` instead, would have claimed the whole row for `.dates` alone
and pushed `.events` onto a third line, arriving at the same three-line
result by a different route. So the break is carried by a dedicated
zero-height `.linebreak` spacer placed before `.dates`: it consumes the
remainder of the tag's row, and `.dates`/`.events` keep their natural
widths and share the fresh row after it. Result on desktop: era + title
+ tag on line one, dates + events on line two.

**Gated at the 700px threshold `layout()` already uses** for its own
mobile/desktop box sizing, deliberately, so this page has one
mobile/desktop boundary rather than a second one that could drift out of
step with the first. Mobile keeps the original three-line wrap -- the
`.linebreak` spacer stays `display:none` there, because title and tag
together overflow a narrow screen.

**Verified:** `shoot.mjs` unaffected (foreignTailOverlaps 0,
overlapGroups 0, jsErrors none, 257 nodes); `validate-census.mjs` 0/0;
manual Playwright check at 1280px and at the 700px threshold edge
confirms two clean lines even on the longest title/tag pair (Era III);
mobile at 390px unchanged.

---

## 2026-08-05 (Pass 7, UI 24) — "Reading the marks" icon key moved back down to the footer, ten minutes after UI 23

**Mark's follow-up to UI 23, same session.** The icon-by-icon key ("what
every icon means") had been pulled UP above the fold for the same
Accessibility P0-1 finding, auto-opening once per browser on first
visit, because before that the map's only explanation sat in the footer
below the entire ten-era canvas. With UI 23's always-visible
`#orientText` line now carrying first-visit orientation on its own, the
fuller key was doing that job a second time and charging permanent space
at the top for it.

**Decided:** the `<details>` block moved back down beside the existing
footer paragraph -- where it originally lived -- and the
auto-open-on-first-visit behavior was dropped along with it. That
behavior was scoped entirely to being above the fold; in a footer it
means nothing, so the key is now an ordinary closed-by-default
disclosure like everything else down there. The heart of the call: a
first-time participant needs one sentence telling them how to read the
picture, not a full glossary before they've seen anything; the glossary
is what you go looking for once you're curious, and the footer is where
people go looking.

**Named plainly, because it partly reverses a Wave 1 accessibility fix
and should not be read later as a regression of it.** P0-1's actual
finding was that the map had no explanation above the fold at all; the
`#orientText` line answers that and stays. What moved is the
supplementary depth, not the orientation. The commit left a comment in
the file recording the full round trip -- footer → top for P0-1 → footer
again the same day -- so the next reader doesn't "fix" it back without
knowing why it travelled.

**Verified:** `shoot.mjs` unaffected (foreignTailOverlaps 0,
overlapGroups 0, jsErrors none, 257 nodes); `validate-census.mjs` 0/0;
manual Playwright check confirms it renders closed in the footer and
opens on click.

---

## 2026-08-05 (Pass 7, UI 23) — The always-visible orientation line made closeable, remembered per browser

**Where this and UI 24 sit.** The above-the-fold orientation line
("Time runs downward — each box marks a tradition at its birth, and its
tail traces its lifetime below it…") is Accessibility P0-1 from the
2026-08-05 full-system review, Wave 1. It and the "Reading the marks"
icon key were on the page again as part of re-implementing that work
FORWARD rather than recovering it: a landing-page/hosting versioning
problem had left the live site missing a batch of prior Atlas work --
Mark's own words, recorded at UI 2: *"everytime we make a change it
reverts back to an old version of the landing page."* Reverting the page
to an older version would have dragged the rest of the site backwards
with it, so the lost work was rebuilt going forward instead. The commits
themselves record only the P0-1 provenance; the incident is written down
here so the run of UI 23–29 reads correctly later.

**The problem with an always-visible orientation line:** it is exactly
right on the first visit and steadily wrong after that. It is screen
space the map should have, charged again on every return, to explain
something the participant has already learned. Orientation is a gift you
give once; after that it's furniture.

**Fix:** a small `×` close control on the line itself, with the
dismissal remembered per browser in `localStorage`
(`cic_atlas_orient_text_dismissed`) -- the same once-per-browser pattern
already used for the "Reading the marks" auto-open. First-time visitors
lose nothing at all; returning visitors get the space back permanently,
by their own choice rather than by a guess about how many visits count
as "learned it."

**Verified:** `shoot.mjs` unaffected (foreignTailOverlaps 0,
overlapGroups 0, jsErrors none, 257 nodes); `validate-census.mjs` 0/0;
manual Playwright check confirms the line is visible by default, hides
on click, and stays hidden across a reload.

---

## 2026-08-05 (Pass 7, UI 22) — Mobile pinch-zoom rebuilt map-only, ending six rounds on the whole-page-zoom approach

**The report that closed out the whole-page-zoom line:** "the x works
again [confirming UI 21's stuck-modal fix held], when fully zoomed out
the box is in the right place but too small to read, when i start to
zoom in it starts to expand, but after a little bit of zooming it jumps
off the page partially left and down, then i can get to it, but its
still rough and unpredictable." At that point `#sheet` was PURE static
CSS -- zero app JS touching its position -- yet it still jumped
specifically DURING an active pinch gesture. That's diagnostic on its
own: the roughness was never this page's bug to fix. `position:fixed`
elements are not reliably glued to the visual viewport WHILE a native
pinch gesture is in progress on real mobile browsers -- a genuine,
long-documented web platform rough edge, not something more CSS or JS
cleverness was going to tame, because the whole-page-zoom approach (UI
16's original design) put the header AND the click-document sheet
inside the SAME zoomable surface as the map, so anything the browser
did to that surface mid-gesture reached them too.

**Asked Mark to choose, with the real tradeoff now concrete rather than
theoretical:** live with the roughness, drop pinch-zoom and go back to
plain scroll (losing the capability this whole six-round effort was
for), or rebuild zoom scoped to just the map -- real new engineering on
the most fragile part of this codebase, the exact risk avoided by
picking the native/whole-page approach back in UI 16. He chose the
rebuild.

**Architecture:** `#mapViewport` is a new, bounded-height,
self-contained scrolling "map pane" (like an embedded map) sized to the
screen space below `#controls`. Inside it, `#mapScaler` is a plain
block sized to the CURRENT scaled content dimensions
(`contentSize * mapScale`) purely so `#mapViewport`'s native
`overflow:auto` has the correct scrollable range at any zoom level.
`#wrap` itself never changes size -- only `transform:scale()`, with
`transform-origin` pinned top-left to keep the math simple. The page's
own `<meta name=viewport>` is NEVER touched again (stays exactly
`width=device-width, initial-scale=1` always), so native browser zoom
for accessibility remains fully available everywhere on the page.
`#sheet`, `#scrim`, `#controls`, and `#railWrap` are structural
SIBLINGS of `#mapViewport`, never descendants of it -- no zoom state of
any kind, from the map or otherwise, can reach them anymore. This is
the property that actually closes out all six prior rounds at once,
structurally, rather than chasing the next real-device edge case: the
click-document sheet doesn't need ANY mobile-specific sizing logic
anymore, because there is no longer a page-level zoom for it to be
downstream of.

**Gesture handling:** single-finger pan is NOT custom code --
`touch-action:pan-x pan-y` (CSS) leaves native browser scrolling on
`#mapViewport` completely alone, exactly the same native mechanism this
whole feature has relied on since UI 16. Only a genuine 2-finger touch
is intercepted (`touchstart`/`touchmove` on `#mapViewport`, only when
`ev.touches.length===2`): the distance between the two touch points
drives the scale change, and the pinch's midpoint drives a
"zoom-to-point" correction (`zoomMapAtPoint`) that recomputes
`scrollLeft`/`scrollTop` so the content under the user's fingers stays
visually stationary as the scale changes -- without this correction,
zooming anywhere but the top-left corner would visibly drift, which
would just be a smaller-scale version of the exact bug this rebuild
exists to eliminate.

**Two smaller migrations this required:** (1) the era-jump rail and the
scroll-driven rail-highlight/year-badge, which used to read
`window.scrollY` directly, now read `#mapViewport`'s own scroll state
on mobile (multiplying/dividing by `mapScale` to convert between the
unscaled content coordinates `layout()` computes and the scaled scroll
coordinates `#mapViewport` actually uses) -- desktop's original
`window.scrollY` logic is untouched, gated by `isMobileDevice`. (2)
`#mapViewport`'s own height, sized against `#controls`' current height,
is recomputed when the filter panel opens/closes (its `max-height`
transition changes `#controls`' own height over ~0.2s, so the recompute
runs on a matching delay, not at the click itself).

**A real bug caught and fixed before any of this shipped, unrelated to
zoom:** the WINDOW resize listener still had UI 16's `selfTriggeredResize`
guard, built specifically to suppress `layout()` re-running in response
to THIS page's own now-removed viewport-meta rewrites. With nothing left
to self-trigger, the guard was dead weight -- removed along with the
`setViewportMeta`/`setMobileMapZoom`/`metaVp` machinery it protected.

**A test-methodology false alarm, caught before it became a wasted
round:** a `fullPage:true` Playwright screenshot at 390px initially
looked like it showed map content duplicated below the "Reading the
marks" footer -- alarming, since nothing in the new structure should
produce that. Measuring `#mapViewport`'s and `<footer>`'s actual
`getBoundingClientRect()`s showed them ending/starting within ~16px of
each other, contradicting the visual read; cropping the SAME screenshot
at full pixel resolution (rather than judging the AI-downscaled preview
by eye) confirmed a completely clean transition from map to footer,
with no gap or duplication. Recorded here because it's a real trap: a
compressed preview image is not a substitute for measuring the actual
DOM, and the instinct to chase a phantom bug was strong enough to be
worth naming so it doesn't happen again on this file.

**Verified, using real multi-touch gesture simulation for the first
time this whole feature (previous rounds could only fake single
properties, never a genuine gesture) via raw CDP
`Input.dispatchTouchEvent` with two synthetic touch points:** a
simulated pinch-out from `(20px gap)` to `(100px gap)` around a fixed
midpoint scaled `mapScale` from 0.317 to 1.585 -- exactly 5x, matching
the 5x gap growth precisely; `scrollLeft`/`scrollTop` updated to keep
that midpoint visually anchored. Pinch-zoomed directly onto a specific
node (House-Churches), confirmed it was still correctly tap-openable at
its new, larger, moved position with ZERO changes needed to the
existing tap-to-open code (`getBoundingClientRect()` and DOM hit-testing
are both transform-aware by default) -- and confirmed the resulting
sheet rendered at `transform:none`, full native `390px` width, completely
independent of the map's `1.33x` zoom at the moment it opened. Single-
finger touch-drag (separately simulated, since mouse-drag and touch-
drag are different input paths and only one is native-scroll-eligible)
correctly scrolled `#mapViewport`. Era-rail jump correctly moved
`#mapViewport.scrollTop` and highlighted the right button; search still
filtered correctly; filter-panel toggle correctly resized
`#mapViewport`. Full Playwright harness clean (0 overlaps, 0 JS
errors); `validate-census.mjs` clean. Desktop re-verified completely
unchanged at every level checked: viewport meta, node width, sheet
layout, AND (new checks for this pass) `#mapViewport` computed
`overflow:visible` with no inline height, `#wrap` with no transform and
its original natural width -- confirming the new elements are
functionally invisible/inert on desktop, not just visually absent.

**Honest framing for what's still unverified:** this is the sixth
attempt at mobile pinch-zoom and the first built around a genuinely
different mechanism (scoped custom gesture handling instead of native
whole-page zoom) rather than a refinement of the same one. Multi-touch
CDP simulation is a real gesture, more convincing evidence than any
prior round had, but it is still not a real finger on real glass. This
should be checked on an actual phone before being treated as fully
settled.

---

## 2026-08-05 (Pass 7, UI 21) — Mobile sheet: reverted to static sizing after a genuine regression, five rounds in

**The report:** "still not working, their is not dark screen so it must
be behind the page, it performed worse that time it would get stuck and
I couldnt close it." A different kind of report than the four before
it. UI 18-20 each described a sizing or positioning imperfection --
readable but wrong-shaped, small, off-center. This one describes the
sheet failing at the one thing it absolutely cannot fail at: opening
and closing. Stuck and unclosable is a worse outcome than anything the
original "crammed to the right" complaint (UI 16) started from.

**Not chasing a sixth fix.** UI 18, 19, and 20 each correctly diagnosed
and fixed exactly what the previous real-device report described --
and each time, the NEXT real-device test found a different failure
underneath, none of which had reproduced in headless Chromium testing
at any point. Four straight rounds of "clean in emulation, broken in a
new way on the actual phone" is a signal about the STRATEGY, not about
any single implementation being slightly wrong: dynamically deriving
the sheet's live geometry from browser viewport state (first
`visualViewport` properties, then `#scrim`'s measured rect, both
re-evaluated on every `visualViewport` resize/scroll event, each firing
writing several style properties plus a forced layout reflow via
`offsetHeight`) kept finding real-device edge cases this session has no
way to reproduce or verify directly. The live-listener version is also
a real, if unconfirmed, candidate for the specific "stuck" failure --
a feedback loop between the geometry writes and further viewport events
is a plausible mechanism, though it couldn't be reproduced or
disproven in headless testing either.

**Reverted entirely, not patched further.** No live listeners, no
measuring `#scrim` or `window.visualViewport`, no per-open
recomputation, no `offsetHeight` reflow. `#sheet`'s `max-width` and
`max-height` are set ONCE, statically, from the stable
`screen.width`/`screen.height` (the same target VALUES UI 18
established were correct, just without any of the dynamic machinery
around them) -- and the show/hide animation reverts to the ORIGINAL
`bottom:-105% -> bottom:0` transition, which was never implicated in
any of the five reports; only the dynamically-computed JS geometry ever
was.

**What this trades away, said plainly:** the sheet will not be
perfectly sized or positioned at every possible zoom/pan state -- opened
while the map is significantly zoomed out or panned off-center, it may
still appear smaller than the physical screen or not perfectly
centered on whatever's currently visible, the same class of cosmetic
imperfection UI 18 first reported. That trade is deliberate: after five
rounds, the property that matters more than exact correctness at every
zoom state is that the sheet reliably opens and reliably closes, every
time, with zero risk of hanging the page. If real-world use finds the
static sizing genuinely too small to be usable (not just imperfect),
that's a real open problem worth returning to -- but with a DIFFERENT
strategy than live-tracking browser viewport state, which this session
has now spent five rounds failing to make reliable on a real device.

**Verified:** close/reopen cycle with a different entry re-tested
clean, no errors. Full Playwright harness clean (0 overlaps, 0 JS
errors); `validate-census.mjs` clean. Desktop re-verified unchanged.
Real-device confirmation that the "stuck, can't close" failure is
actually gone is the one thing this session cannot do itself -- flagged
here rather than claimed.

---

## 2026-08-05 (Pass 7, UI 20) — Mobile pinch-zoom, round five: measure what's already correct instead of recomputing it

**The report:** "it isn't perfect, but better, when zoomed out its
small and still goes to the lower left, but you can expand and read it
ok." Progress -- the "jumps mostly off screen" failure from UI 19 is
gone, and the sheet is at least usable once expanded -- but the resting
(zoomed-out) case is still off. Third straight round where headless
Chromium testing gave a clean result and a real phone found the next
layer underneath it.

**The tell that pointed to the actual fix:** nothing was reported wrong
with `#scrim`, the dark backdrop directly behind the sheet. It's also
`position:fixed`, also meant to cover the whole visible screen
(`inset:0`), and evidently does -- a backdrop only covering part of the
screen, leaving map visible around its edges, would have been the more
obvious complaint by far. So `position:fixed` itself was never the
unreliable part on this device. What UI 19 actually did was derive the
SHEET's geometry independently, from `window.visualViewport`'s
`offsetLeft/offsetTop/width/height` properties -- a separate calculation
that had to independently arrive at the same answer `#scrim` was
already visibly getting right, and evidently didn't, at least not at
the very first (zoomed-out, no gesture yet) render.

**Fix:** stopped computing the sheet's geometry from `visualViewport`
properties at all. `updateSheetGeometry()` now measures `#scrim`'s own
`getBoundingClientRect()` -- whatever rectangle it is ACTUALLY, visibly
covering, which by definition is the true current screen -- and sizes/
positions the sheet to match that measured rectangle directly. No
independent math left to drift out of sync with what's already known to
be correct. Required reordering `openSheet()` slightly: `scrim` needs
its `.on` class (display:block, not display:none) added BEFORE its rect
is measured, or the measurement is all zero -- scrim now goes visible
first, sheet's geometry is computed second, sheet goes visible third.
Live tracking while the sheet stays open is unchanged in mechanism
(still triggered by `visualViewport` resize/scroll events) -- only what
happens INSIDE the handler changed, from reading `visualViewport`
numbers to re-measuring `#scrim`.

**Verified:** re-confirmed the resting-zoom case still matches UI 19's
result (`scrim` and `sheet` both measure `left:0, width:1230` at the
canvas's ~0.317x rest zoom -- consistent, since at rest nothing should
have changed). Directly tested the NEW re-measurement path (the OLD
test, which faked `visualViewport` properties, no longer exercises
anything real now that those properties aren't read) by moving
`#scrim`'s actual rendered rect via its own inline style to a specific
simulated "pinched to (300,500), 390×844" position and firing the same
trigger event a real gesture produces -- the sheet moved to
`left:300, top:686, width:390, bottom:1344`, exactly matching scrim's
new rect. Close/reopen cycle with a different entry re-tested clean.
Full Playwright harness clean (0 overlaps, 0 JS errors);
`validate-census.mjs` clean. Desktop re-verified unchanged.

**Named honestly:** this is the third consecutive round on this one
element where a fix that tested clean in headless Chromium needed a
real phone to find what was still wrong. This round's fix rests on one
fact that so far hasn't been contradicted by any report -- that
`#scrim`'s plain `inset:0` is correct -- rather than on reasoning about
viewport APIs in the abstract, which is what the last two rounds did and
both turned out to be short in a way only a real device surfaced. If
this is STILL off, "does the dark backdrop itself look correctly
full-screen when zoomed out" is the next fact worth checking before
writing any more code.

---

## 2026-08-05 (Pass 7, UI 19) — Mobile pinch-zoom, round four: the sheet needed to track the LIVE visual viewport, not a snapshot of it

**The report, on a real phone this time:** "no it is square but small,
and when you zoom in it jumps to the left and down mostly off the
screen." UI 18's fix computed the sheet's size from
`screen.width|height / visualViewport.scale` -- correct math, verified
three ways in testing -- but only ONCE, at the moment `openSheet()` ran.
Confirms two things at once: the scale-math approach was fundamentally
the wrong shape of fix (a live gesture happening AFTER open was never
going to be caught by a one-time calculation, however correct that
calculation was in the instant it ran), and `position:fixed`'s
`left:0`/`bottom:0` are NOT reliably tracking the visual viewport on a
real device -- confirmed now, not just flagged as a theoretical risk in
UI 16's original note.

**Fix, a different shape entirely:** stopped trusting `position:fixed`
to track anything on its own. `updateSheetGeometry()` reads
`window.visualViewport.offsetLeft/offsetTop/width/height` directly --
the live, authoritative description of exactly where the physical
screen currently sits within the page -- and writes `left`/`width`/
`max-width`/`max-height`/`top` in JS pixels explicitly, every time.
`top` instead of `bottom`, deliberately: `top` only needs an OFFSET from
the layout viewport's top edge, which `visualViewport.offsetTop` gives
directly, while `bottom` would need the layout viewport's TOTAL height
-- the exact same inflated, unreliable value that caused UI 18's
original `max-height:78vh` bug in the first place. Height is measured
via `sh.offsetHeight` AFTER `max-height` is applied and BEFORE `top` is
computed, so a short entry still sits flush at the screen's bottom
instead of leaving a gap. Called once on open, then live on every
`visualViewport` `resize`/`scroll` event for as long as the sheet stays
open (registered in `openSheet`, unregistered in `closeSheet`) -- so a
pinch or pan that happens mid-read keeps the sheet correctly sized and
positioned instead of freezing it to whatever the scale happened to be
at the moment of the tap. The show/hide slide animation moved from
animating `bottom` to animating `transform:translateY`, specifically so
it composes on top of whatever `top`/`left` this function just computed
instead of needing its own correct `bottom` value (which was the
un-fixable dependency this whole redesign exists to avoid).

**Verified:** opened the sheet at the map's resting zoom (~0.317x) and
confirmed correct full-width geometry, matching UI 18's prior result;
then, with the sheet still open, directly overrode
`visualViewport.offsetLeft/offsetTop/width/height` to a specific
simulated "pinched in and panned to (300,500), 390×844" state and fired
the same `resize` event a real gesture produces -- the sheet moved and
resized to `left:300, top:686, width:390, height:658`, exactly matching
that simulated viewport's bounds (`686 = 500+844-658`, `1344 = 500+844`
bottom edge). This is the first round of this feature where the FULL
failure mode reported live-updating during an open sheet, not just
sizing at open time -- could be directly reproduced and confirmed fixed
in testing, not just reasoned about. Close/reopen cycle with a different
entry re-tested clean, no stray state from the previous open. Full
Playwright harness clean (0 overlaps, 0 JS errors); `validate-census.mjs`
clean. Desktop re-verified completely unchanged (`updateSheetGeometry`
and `sheetVvListen` both return immediately when `!isMobileDevice`).

---

## 2026-08-05 (Pass 7, UI 18) — Mobile pinch-zoom, round three: the click-document sheet was "a thin long field"

**The report:** "it is a thin long field, on the desktop it works ok,
but on the phone it is to small to read, we need to expand it to the
full width of the screen, and that should solve where it shows up
also." Measured the actual rendered box rather than guessing why, since
this is the second time a plausible-looking fix to this exact element
(the click-document sheet, `#sheet`) turned out to need real numbers to
diagnose correctly (UI 16 tried the same territory and found a worse bug
by testing before shipping).

**Two real, separate causes, both confirmed by measuring the live DOM:**
1. `max-height:78vh` in `#sheet`'s CSS is relative to the LAYOUT
   viewport height, which UI 16's own pinch-zoom widen also inflates on
   mobile (the wide canvas needs a proportionally taller layout viewport
   to keep the zoom math internally consistent). Measured: max-height
   resolved to 1633px against a 390px-wide sheet -- correctly narrow,
   absurdly tall. That's the "thin long field."
2. Pinning the sheet's width to the true `screen.width` (390px, UI 16's
   own fix) isn't enough on its own, because the sheet is ordinary page
   content -- it's zoomed out right along with the map. At the canvas's
   resting "fit to screen" zoom (~0.317x on a typical packed width), a
   390px-wide box renders at roughly a third of the physical screen:
   still thin. What actually fills the screen at the CURRENT zoom is
   `screen.width / visualViewport.scale` of CSS px -- which equals the
   full canvas width W at the map's resting zoom, shrinking toward
   literal `screen.width` only once the user has pinched all the way in
   to native 1:1 reading scale.

**Fix:** `sizeMobileSheet()`, called fresh every time `openSheet()` runs
(not once at page load -- the user's zoom level can differ each time
they tap a box), computes width and max-height from
`screen.width|height / visualViewport.scale` and sets them directly,
overriding the vw/vh-relative CSS the wide viewport now skews. `left:0`,
`right:auto`, `margin:0` are set once (position doesn't depend on zoom)
so width alone determines the box instead of the old left+right+
margin:auto centering, which had also been landing the sheet centered
on the wide canvas (x=420) rather than pinned to the screen's true left
edge -- Mark's own instinct ("expand to full width... should solve
where it shows up") was right: a sheet sized to actually fill the
current screen doesn't have room to appear anywhere but pinned to it.

**Verified:** re-measured the live sheet after the fix at the map's
resting zoom -- width/maxHeight now resolve to exactly `screen.width`
and `screen.height*0.78` in PHYSICAL terms (1230px/2077px in CSS terms
at the 0.317x resting zoom, which is precisely W and 78% of the
inflated height -- the same numbers scaled back to native size).
Directly tested the scale-dependent FORMULA (not just the resting-zoom
case) by mocking `visualViewport.scale` to 1, 0.5, and 0.317 before
opening the sheet each time: computed width/height matched the expected
`screen.width/scale` and `screen.height*0.78/scale` in all three cases
exactly. A genuine live pinch gesture's effect on `visualViewport.scale`
could not be simulated in headless Chromium (confirmed unreliable when
tried, consistent with UI 16's finding that dynamic viewport mutation
doesn't fully propagate in this test environment) -- the three-scale
formula test is the closest verification available short of a real
device, and the formula itself is simple, direct division with no
hidden assumption that would only hold at one particular scale. Full
Playwright harness clean (0 overlaps, 0 JS errors); `validate-census.mjs`
clean (census untouched). Desktop re-verified completely unchanged
(`sizeMobileSheet` and the left/right/margin override both return
immediately when `!isMobileDevice`).

---

## 2026-08-05 (Pass 7, UI 17) — Mobile pinch-zoom, round two: families were clustering in the left third of the canvas, zoomed out

**The report, immediately after UI 16 shipped:** "we can double the
width on the phone, when zoomed out fully everything is on the left
side of the canvas." True, and once pinch-zoom made the WHOLE canvas
visible at once for the first time, it exposed a design decision that
had been sitting quietly in `tryPack` all along, never really testable
until now.

**Root cause:** `tryPack`'s anchor-spread line --
`const AW=Math.min(W,viewW);` -- deliberately spreads each era's family
anchors across the SCREEN width, not the full packed canvas width, with
its own comment explaining why: "extra canvas width is pure spill room
to the right ... never an excuse to scatter the families wider." On
desktop and on mobile before UI 16, that reasoning held -- the canvas's
extra width past the screen was mostly invisible, something you'd only
find by actively scrolling right into overflow, so keeping the families
themselves clustered near what was actually on screen made sense. UI 16
changed that premise for mobile specifically: the packed canvas is now
routinely shown in FULL, zoomed out, in one glance. With anchors still
capped at the original ~390px screen width while the canvas itself
packed out to 1170-1230px, every family's "home" position sat in the
left third of a canvas the viewer could now see whole -- exactly "on the
left side," with the right two-thirds sitting mostly empty except for
whatever individual boxes had to spill there to avoid collisions.

**Fix:** on mobile only, `AW` now equals the full packed width `W`
instead of `Math.min(W,viewW)` -- anchors spread across the whole
canvas, the same canvas the whole-page pinch-zoom now shows at once.
Desktop's line is untouched (`isMobileDevice?W:Math.min(W,viewW)`),
preserving the original screen-clustered behavior there, where the
original reasoning still applies unchanged.

**Verified against real Chromium mobile emulation:** zoomed-out
screenshots at Eras I-II and the Reformation era (VII, the busiest
stretch on the map) both light and dark -- families now spread evenly
across the full width instead of bunching left, in both color schemes;
re-ran the full mobile interaction suite (node sizing, mobile-only CSS,
bottom-sheet layout, tap-to-open, era-rail jump, search) with no
regressions from the wider anchor spread. Full Playwright harness clean
(0 overlaps, 0 JS errors) -- confirms the wider spread didn't introduce
any new collisions, only relocated where boxes prefer to sit before
collision-avoidance kicks in. `validate-census.mjs` clean (census
untouched). Desktop re-verified completely unchanged (viewport meta,
node width, sheet layout all identical to before this pass).

---

## 2026-08-05 (Pass 7, UI 16) — Mobile pinch-zoom/pan: the packed canvas is routinely wider than the phone screen, so let the browser's native gesture handle it

**The report:** "on the phone it feels like everything is crammed to the
right, we can expand to a width that when we scroll it fills the width,
but pinch in and be able to slide right and left." Mobile's packed
canvas has been wider than the screen since the very first mobile pass
this project did (the whole reason the "less text" mobile CSS and the
mobile dark-mode ring exist) -- until now that extra width just sat past
the right edge of a fixed device-width viewport with no visual cue it
was even there.

**Two ways to build this, asked before writing any code:** (1) the whole
page zooms together, native pinch-zoom on a viewport sized to fit the
canvas at rest -- simple, standard, but the header/search shrink too
until you pinch in; or (2) a custom pinch/pan built just for the map,
header always full-size, but real new code layered onto the single most
fragile part of this codebase (node placement, tooltips, and the
tap-to-open sheet all depend on exact positions). Mark picked (1),
explicitly on the lower-risk tradeoff.

**Mechanism:** on mobile only, `layout()` now widens the page's own
`<meta name=viewport>` to `width=${W}` (the packed canvas width already
computed by `tryPack`) with `initial-scale` set so the whole canvas fits
the screen at rest -- native pinch-zoom and native touch-pan take it from
there, no custom gesture code. Desktop's viewport meta is never touched.

**A real correctness trap this surfaced, fixed before it shipped:** every
piece of mobile-specific behavior on this page -- the "less text" CSS,
the responsive `HEAD`/`RH` era-header sizing, the mobile-vs-desktop
`#sheet` layout -- was keyed off live `innerWidth`/`clientWidth` or
`@media (max-width)`/`(min-width)` queries. Deliberately widening the
layout viewport would have silently flipped every one of those the
moment the canvas crossed 700px, making the page misclassify itself as
desktop mid-session. Fixed by capturing an `is-mobile` class on `<html>`
synchronously in `<head>` from `screen.width` (which the viewport widen
never touches, unlike `innerWidth`/`clientWidth`) before boot() even
runs, converting both `@media` blocks to `html.is-mobile`/
`html:not(.is-mobile)` selectors, and switching every JS mobile check
(`RH`, `HEAD`, the `viewW` used for box/thread density in `layout()`) to
read that same frozen flag instead of a live viewport measurement.

**A second trap, caught by testing against real Chromium mobile
emulation, not assumed:** writing the viewport meta tag fires a native
`resize` event, which the existing resize listener treated as a real
window resize and answered by calling `layout()` again -- which ends its
own run by writing the viewport meta, firing another resize. It
converges rather than looping forever (the second pass computes the same
width and writes the same content), but it's real wasted work every
`layout()` call, so it's suppressed with a one-shot
`selfTriggeredResize` flag: armed immediately before any write to the
tag, consumed by the resize listener instead of re-running layout for
that one event. A genuine window resize or orientation change never sets
the flag, so it's never suppressed.

**A design idea tried and deliberately dropped:** the first draft also
flipped the viewport back to plain `device-width` while the click-document
sheet (`#sheet`) was open, so it would read at native 1:1 scale
regardless of whatever zoom the map was left at, then restored the wide
state on close. Testing that against real mobile emulation found the
sheet's own `left:0/right:0/max-width:640px` math resolving against a
stale, inflated viewport HEIGHT after the toggle -- the sheet rendered
anchored below the actual visible screen, unreachable. That's a worse
bug than the one this feature set out to fix, so the toggle was dropped
entirely rather than patched further. What shipped instead: the sheet's
`max-width` is pinned once to the true `screen.width` (never wider than
the physical screen at any zoom level), and its exact on-screen position
while the user has actively pinched/panned away from the top of the page
is named here as a known, accepted limitation -- `position:fixed` versus
the visual viewport is genuinely inconsistent across real mobile
browsers, and this pass doesn't claim to have solved that, only to have
avoided making it worse.

**Verified against real Chromium mobile emulation (iPhone 13 profile,
`isMobile`/`hasTouch` on, the only way the viewport-meta scaling
actually takes visual effect in testing):** initial load shows the full
packed width fit to the screen at Eras I, IV, and VII with nothing cut
off; `screen.width`-derived `is-mobile` class and every downstream mobile
check (node width ~101px not desktop's 150px, `.node .nm` at .62rem,
`#sheet` in bottom-sheet layout not the desktop side panel) held correct
throughout, including after a simulated resize event, confirming no
feedback loop and no misclassification; the sheet opens and reads
correctly at the common case (tapped before any zooming); search, the
era-rail jump, and the two-tap mobile preview-then-open interaction all
still work. Desktop re-verified completely untouched -- viewport meta
stays exactly `width=device-width, initial-scale=1`, node width stays
150px, sheet stays the right-side panel. Full Playwright harness clean
(0 overlaps, 0 JS errors); `validate-census.mjs` clean (census untouched).

---

## 2026-08-04 (Pass 7, UI 15) — Dark mode round two, mobile: the fix worked but was too thin to read at small size

**The report, on the phone, same day as UI 14:** "we have the same
problem on the phone, tertullian is an example." A real regression in
scope, not a repeat of the same bug -- UI 14 was verified on desktop
(1280px) before shipping and genuinely fixed desktop's contrast, but was
never separately checked at mobile's smaller box size.

**Diagnosis, by pixel-sampling the actual rendered screenshot** (not
just computed-style values, since a box-shadow's real visibility depends
on how it anti-aliases at actual size) at Tertullian's real position on
a 390px viewport: the UI 14 fix (a 1px, 9%-opacity light ring) was
*technically* present and *technically* passed a strict luminance check
against the ribbon behind it (~3.4:1 at the single border pixel) -- but
it rendered as one barely-there transition pixel between the box and a
same-family-hue ribbon (Tertullian's own "Latin West" red family tint,
both box fill and thread deriving from the same hue in dark mode). A
1px edge that only technically clears a contrast minimum is still, in
practice, too thin to read as a box outline at mobile's smaller size --
this is the gap a computed-style check alone can't catch, only a real
pixel-sampled render can.

**Fix:** widened the ring from 1px to 1.5px and raised its opacity from
9% to 22% (`0 0 0 1.5px rgba(255,255,255,.22)`), same `--node-shadow`
custom property, no new mechanism. Re-sampled the same pixel row after
the change: the edge is now a 2-3px graduated brightening before the
border color hits, instead of one isolated pixel -- a real, perceptible
outline rather than a value that only passes on paper.

**Verified against the real site:** re-sampled Tertullian's exact pixel
row (clear multi-pixel edge now, was one faint pixel before); mobile dark
screenshots at Era IV, VII, and X (the three most crowded stretches, the
same ones checked for the earlier mobile "less text" work) all show every
box clearly separated from its ribbon; desktop dark re-checked at Era IV
to confirm no regression there -- unchanged, if anything crisper; text
contrast re-scan still 0 failures below 3.0 across all 257 nodes (that
was never the actual problem). Full Playwright harness clean (0
overlaps, 0 JS errors); `validate-census.mjs` clean (census untouched).

---

## 2026-08-04 (Pass 7, UI 14) — Dark mode "dark on dark": boxes were disappearing into their era's background band

**The report:** "As i go through it some of the worlds don't show up well
on the dark mode, the its dark on dard." True on the actual site, and
worth finding the real mechanism before touching anything, since the
site's whole dark-mode strategy is a single set of CSS custom properties
redefined per theme — no ad hoc dark-mode selectors anywhere else in the
file, and this fix needed to keep that pattern intact rather than add a
new one.

**Root cause, measured, not guessed:** computed WCAG contrast ratios
between the box fill (`--panel`) and the 3-shade era background cycle in
both themes. Light mode: ~1.2–1.23. Dark mode: ~1.06–1.09. Low in *both*
themes at the raw color level — but light mode was being rescued by the
box's existing `box-shadow:0 1px 2px rgba(0,0,0,.08)`, a dark shadow that
reads clearly against a light era band. That same dark shadow is nearly
invisible against an already-dark era band, so only dark mode actually
manifested the symptom even though the underlying color problem exists
in light mode too.

**Fix:** a new `--node-shadow` custom property added to all four
existing `:root` theme blocks (base, `prefers-color-scheme: dark`,
`[data-theme="dark"]`, `[data-theme="light"]`) — the same mechanism
already used for every other theme difference in the file. Light mode
keeps the original shadow value unchanged. Dark mode gets a light-rgba
1px ring plus a slightly stronger dark shadow
(`0 1px 3px rgba(0,0,0,.45), 0 0 0 1px rgba(255,255,255,.09)`), so
separation no longer depends on the era band happening to be lighter
than the box. `.node{box-shadow:...}` now reads `var(--node-shadow)`.
Live-status boxes (`.node.live`) were untouched — they already carry
their own family-hue background and shadow, and were never part of this
report, confirmed by checking status classes on rendered nodes: every
non-live status (def/sel/psc/exc/cev) is plain `.node` with no
background override, so this one property covers all of them.

**Verified against the real site, dark mode:** contrast-ratio scan
across all 257 rendered nodes' text-vs-box color (0 failures below 3.0,
confirming this was never a text-contrast issue); `getComputedStyle`
confirms the new shadow value resolves correctly; screenshots at Era I,
IV, VII, and X (the most crowded, multi-ribbon era) all show every box
clearly separated from its era band, including where boxes sit against
a busy stretch of overlapping colored ribbons. Full Playwright harness
(`shoot.mjs`) clean — 0 overlaps, 0 JS errors, all interactions pass;
`validate-census.mjs` clean (257 movements, 21 edges, 10 eras, 0
errors/warnings — census untouched by this fix).

---

## 2026-08-04 (Pass 7, UI 13) — Mobile bundling reverted: "you lose the continuity and ability to find what you're looking for"

**The verdict, after seeing it live, not a mockup:** "the grouping them
doesn't work, you loose the continuity and ability to find what your
looking for. go back to what we had before for the phone, just less
text." Direct, unambiguous -- the tradeoff a prior mobile-bundling pass
made (fewer boxes, narrower canvas, in exchange for folding crowded
traditions behind a tap) cost more than it saved. Losing each
tradition's own visible ribbon broke the thing that makes this a MAP
rather than a list -- you can't trace a lineage through a bundle, and
scanning for one specific tradition by eye no longer works once it's
behind "14 active."

**Reverted with `git revert`** (the bundling commit, on both the working
branch and main) rather than hand-reconstructing the prior state --
clean, single-commit, no conflicts, and confirmed byte-identical to the
pre-bundling file by diff before moving on. Every ribbon, every
individual box, the exact same packing `tryPack` produces on desktop --
nothing about placement, continuity, or search changed from before the
bundling attempt ever started. (That attempt's own decision-log entry
reverted along with its code, since the two were committed together --
recorded here instead: it was tried, shown on the real running site,
and explicitly rejected for continuity and findability, which is worth
knowing before anyone proposes grouping again.)

**"Just less text" implemented as a plain CSS-only change**, deliberately
NOT touching `NW` (box width) or anything inside `layout()`/`tryPack` --
smaller font on `.node .nm`/`.node .dt` and tighter box padding, mobile
only (`max-width:699.9px`). Doesn't reduce the underlying canvas
overflow (the whole point of reverting was to accept that overflow
rather than the bundling tradeoff), just makes each box's own text take
up less visual space at the same position the packer already gave it.
Zero risk to placement/continuity/search since it touches none of the
code that computes them.

**Verified against the real site:** 257/257 individual boxes rendered,
0 bundle boxes, 0 JS errors; Era VII screenshot confirms every
tradition has its own ribbon again, text visibly smaller and more
compact at the same layout as before; a normal box click still opens
its own real sheet correctly. Full Playwright harness (`shoot.mjs`)
clean (0 JS errors, 0 overlaps, all interactions pass).

---

## 2026-08-04 (Pass 7, UI 11) — Era header bar, round two: bigger text, full width, richer events, and two real layout bugs the bigger content exposed

**The feedback:** "it is a great improvement, but the text is to small and
hard to read, also we can streatch the era bars accros the entire width
and add some era information and world events... make them global or
regional events that directly impacted the worlds. they can be church
specific like 'the great schism' or world 'Fall of Rome'."

**Content**: events expanded from 2 to 3 per era, deliberately mixing
church-specific (Great Schism, Western Schism, Council of Trent) with
broader world-historical events that had real, direct church impact —
Justinian's Plague (541), the Sack of Rome (410) and Fall of Rome (476,
matching Mark's own example phrasing), the Sack of Constantinople (1204),
American Civil War, World War I (matching Mark's other example). Kept
every event within its own era's actual date range rather than reaching
outside it for a more famous date.

**Sizing/width**: title 1.25rem (was .7rem), academic/dates/events all
~1rem (was .64-.66rem), no (era number) label .95rem. Width changed from
the first pass's `max-width:min(92vw,640px)` — which capped the bar at
640px even on wide desktop screens, the opposite of "stretch across the
entire width" — to `width:calc(96vw - 64px)` (the -64px reserves room for
the fixed year-badge/rail column at the right edge; see below for why
that reservation had to be measured, not assumed).

**Two more real layout bugs, found by measuring rendered geometry before
shipping, not by eye:**
- **Bigger content needs more vertical clearance, and the geometry didn't
  have any.** The old `HEAD=8` constant (a fixed 8px) was sized for the
  original one-line corner pill. Measured actual rendered bar heights on
  the new content: up to 82px on desktop, 195px on mobile (more events
  wrap onto more lines at narrower widths). Made `HEAD` responsive like
  `RH` already is (`innerWidth<700?230:110`, real headroom above the
  measured worst case, not an exact fit that breaks the next time an
  era's content gets one line longer).
- **Even after that, 12 real node/bar overlaps remained on desktop (9 on
  mobile)** — found by a Playwright bounding-box intersection check
  across every era-bar × every movement-box pair, not by scrolling and
  looking. Root cause: the formula computing each era's own vertical
  start position (`y = s.r0*rh + ERA_PAD*index`) never accumulated the
  PRECEDING eras' own header-clearance space — it only added a flat 34px
  `ERA_PAD` per era boundary, regardless of how tall that era's own
  `HEAD` reservation actually was. Harmless at `HEAD=8`; compounds badly
  once `HEAD` is 110-230px, because each era's start position drifts
  further ahead of where its predecessor's content actually ends.
  Rewritten as a running accumulator (`cursorY += h` each era, using
  each era's own real rendered height) instead of recomputing position
  from row-count alone — structurally can't drift out of sync with the
  height formula again, because both now come from the same accumulator.
- **A third, smaller one**: the widened bar (now up to 96vw) started
  rendering UNDER the fixed year-badge/rail column on mobile — same
  visible-viewport width, different z-index, so the rail (z-index:35)
  painted over the bar's text (z-index:20) wherever their x-ranges
  overlapped. `pointer-events:none` meant nothing was unclickable, but
  real text was genuinely hidden. Fixed by reserving 64px in the bar's
  own width for the rail's known footprint.

**Verified via Playwright**: zero node/bar overlaps confirmed via
bounding-box math on both desktop and mobile (was 12/9 before the
accumulator fix); zero bar/rail overlap confirmed the same way (was a
real x-range collision before the width fix); dark mode 3-shade cycle
still exact-match; census validator clean (257/21/10, 0 errors); full
Playwright harness (`shoot.mjs`) clean (0 JS errors, 0 overlaps across
all 4 breakpoint/scheme combinations, all interactions pass).

---

## 2026-08-04 (Pass 7, UI 10) — Accessibility feedback pass: richer era header bar, 3-shade alternating backgrounds, scrolling year badge

**Three asks from real user feedback**, all landing in one pass: (1) a
full-width era header bar carrying friendly name, academic name where a
real distinct one exists, dates, and 1-2 major events, staying semi-
transparent so "you can see the printing underneath"; (2) alternating
background shades so adjacent eras are unmistakably different, not the
existing 10-step gradient where neighbors are deliberately close in tone;
(3) a scrolling year readout so participants always know what period
they're looking at, spelled out ("70 CE to 312 CE"), not compressed.

**Design decisions confirmed with Mark before building** (both would have
been expensive to redo across 10 eras if guessed wrong): 3 shades, not 2;
flatten to alternating rather than layering onto the existing gradient.

**New era content (census, additive fields `academicName`/`keyEvents` on
each of the 10 eras)** — grounded, uncontroversial historiographical
terms, several literally the field's own vocabulary (Late Antiquity;
"The Great Century of Missions" is Kenneth Scott Latourette's own term).
No academic name shown where the existing title already IS the standard
term (Era VII, "The Reformation Era") rather than inventing a redundant
second label.

**3-shade background**: replaced the 10-step warm-to-cool gradient with a
3-color cycle ((era.num-1)%3) — Eras I/IV/VII/X share a warm gold-tan,
II/V/VIII a neutral straw, III/VI/IX a cool blue-grey, in both light and
dark mode. Same `--eraN` custom-property mechanism as before, just fed a
repeating 3-value census instead of 10 unique ones — no new CSS plumbing.

**Two real bugs found and fixed before shipping, not after:**
- The year badge, first built as its own fixed-position element with
  hand-computed pixel offsets to sit above the rail, silently overlapped
  the rail's top buttons and ate their clicks — caught by Playwright
  ("element intercepts pointer events"), not visually. Fixed by wrapping
  both in one `#railWrap` flex column instead of separately-computed
  pixel math — a flex column can't overlap itself regardless of how long
  the year text gets. Also switched the badge from vertical-rl (sideways)
  text to horizontal — a badge built to make the page MORE accessible
  shouldn't require tilting your head to read it.
- The new full-width `.erahead .bar` had no `max-width`, so it grew to
  fill the CANVAS's width (deliberately wider than the viewport on narrow
  screens — that's the whole point of the timeline's horizontal scroll),
  not the viewport's width. `flex-wrap` had nothing to wrap against.
  Result: the bar's right edge landed at 1157px on a 390px mobile
  viewport — invisible without scrolling right first, defeating the
  entire point of making this content harder to miss. Fixed with
  `max-width:min(92vw,640px)`.
- (Investigated, not a bug): scrolling to the very bottom of the page
  briefly appeared to leave the rail highlight and year badge stuck on
  Era VI/IX instead of X. Root cause was test methodology, not the site —
  clicking "jump to era" uses smooth-scroll, and checking the result
  before the animation settles reads a mid-flight scroll position. With
  proper settle-polling, the rail and badge were correct at every era,
  including the boundary case. Logged so a future check doesn't re-chase
  the same false lead.

**Verified via Playwright**: era bar content correct for all 10 eras;
3-shade cycle confirmed exact-match across the I/IV/VII/X, II/V/VIII,
III/VI/IX groups in both light and dark mode; badge/rail zero pixel
overlap confirmed via bounding-box math, not just visually; clicking
rail buttons 0/4/9 correctly settles both `.on` state and badge text in
sync (I · 70 CE to 312 CE, V · 1054 CE to 1300 CE, X · 1906 CE to
present); no horizontal overflow on mobile (390px) for either the era
bar or the rail/badge column; census validator clean (257/21/10, 0
errors); full Playwright harness (`shoot.mjs`) clean (0 JS errors, 0
overlaps, all interactions pass).

---

## 2026-08-04 (Pass 7, UI 9) — Search stays a name/period lookup; made that honest instead of trying to fake understanding

**The question that surfaced this:** Mark asked what traditions "allowed
women to serve in leadership," and got back what the search box's actual
matching logic would have found instead — traditions a woman personally
*led* (Christian Science, Shakers). Different question. When Mark then
asked whether the search bar could be made "dynamic" enough to tell those
apart, the honest answer: not without either a live LLM call per keystroke
(breaks the entire point of a static, token-free atlas — same cost
argument that drove the whole Tours redesign this project already went
through) or a synonym-expansion hack that just relocates the "you have to
know the exact word" problem one level up and *still* can't distinguish
"founded by a woman" from "included women in some leadership role" — that
needs an actual read of the text, not a keyword match.

**Mark's resolution:** don't fake it — tell the participant plainly when
what they typed isn't in the data, instead of a bare, easy-to-misread
"0 of 257 movements." Two changes:
- Placeholder reframed to set the right expectation up front: "Have a
  movement or period in mind? Search by name — e.g. Coptic, Reformation,
  Pentecostal" (was: "Search all 257 movements — including the ones that
  aren't open, and why," which read as broader than the search actually
  is).
- `applyFilter()`: when there's a typed query and zero matches, the
  `#cnt` readout (already `aria-live="polite"`, so this is announced to
  screen readers the same as the ordinary count) now echoes the literal
  typed text back: `"<query>" doesn't match anything documented in this
  timeline.` Via `.textContent`, not built into a template that reaches
  `innerHTML` — confirmed via Playwright that a typed `<b>test</b>` shows
  up as literal escaped text, not executable markup.

**What this deliberately doesn't do:** it doesn't make the search
smarter. It's still the same literal substring match over `name`,
`shortName`, `informalName`, `region`, `why`, `relationsSummary`,
`floorNote` — NOT `longDescription`/`voices`/`legacy`/`experienceToday`,
where thematic content like "women in leadership" actually lives. If a
theme like that needs to be browsable from the page itself rather than
askable in conversation, the fit with this project's own pattern is a
curated tag (built the way Region was — a real editorial pass, reviewed
once, added as its own honest toggle), not a cleverer guess at the
search box. Not built this pass; flagged as a live open question, not
started.

**Verified via Playwright:** placeholder text confirmed; "Coptic" still
returns 8/257 as before; "women in leadership" and a raw `<b>test</b>`
both produce the honest no-match message with the text properly escaped;
clearing the box and the built-only-toggle-with-no-query edge case both
still show the ordinary count, not a false no-match. Full harness
(`shoot.mjs`) re-ran clean: 0 JS errors, 0 overlaps, all interactions
(search, live-filter chip, hover, sheet, era rail) pass.

---

## 2026-08-04 (Pass 7, UI 8) — Streams retired entirely; "Global" region tag retired for real origin/spread tagging

**Two asks, in one turn.** (1) "lets remove the streams completely and
global it is very inconsistant." (2) "if we have an all for the regional
that should cover the global and we use the start of the movement as the
primary place or if it became big in another region then it is in both."

**Streams removed outright**, not folded into anything — the whole
`#streamlegend` feature (10 buttons: Oriental Orthodox, Hesychast/
Philokalia, Eastern Catholic/Uniate, Reformed/Calvinist, Wesleyan/
Holiness/Pentecostal, Baptist, Anabaptist/Believers-Church, Anglican/
Church of England, Dispensational/Bible-Institute, Post-Evangelical
Ferment), its CSS (`.stream-on`, `body.streamfiltering`), its URL state
(`?streams=`), its glossary section, and its line in the click-doc sheet.
The census's own `streams[]` field on each movement was left untouched
(harmless unused data, not worth 257-entry churn to strip) — only the UI
that read it is gone. The click-doc sheet's old streams line now shows
the entry's `regions[]` instead, filling the same slot with something
still live.

**"Global" region retired.** It was applied inconsistently — some
transnational/diaspora entries got it, some plainly-just-as-transnational
ones didn't — and Mark's own point: the Region toggle's All button
already covers "everywhere," so a dedicated Global tag was redundant with
a mechanism that already exists. Re-tagged all 16 formerly-Global entries
by hand using the rule Mark gave — start place as the primary region, a
second region added only if the movement became substantial somewhere
else identifiable, nothing invented for the sake of filling a field:
- Most (11 of 16) already carried a real region alongside Global (e.g.
  Azusa Street: `[Global, North America]` → `[North America]`) — just
  dropped the redundant tag.
- 4 entries had ONLY "Global" as their region string, needing real
  research instead of a keyword match: Catholic Lay Renewal Traditions
  (a bundle of Catholic Worker/NY, Focolare/Italy, L'Arche/France) →
  `[North America, Mediterranean, North Europe]`; Progressive
  Christianity → `[North America, North Europe]` (mainline Protestant
  roots on both sides of the Atlantic); The Post-Vatican-II Parish
  Tradition → `[Mediterranean]` (Rome, where the Council convened and
  its documents were promulgated, even though its lived effect is every
  parish everywhere); Lausanne-Era Global Evangelicalism →
  `[North America, North Europe]` (Billy Graham's American leadership,
  hosted in Lausanne, Switzerland).
- 1 entry (the Armenian Church after the Genocide) already had two real
  regions (Asia Minor, Caucasus) and just lost the redundant third.

**Verified:** census validator clean (257/21/10, 0 errors); full
Playwright harness (`shoot.mjs`) clean (0 JS errors, 0 overlaps, all
interactions pass); confirmed `#streamlegend` fully gone from the DOM;
confirmed no entry carries "Global" anymore; confirmed region solo/add/
All still works with 10 regions (not 11); opened a formerly-Global entry's
sheet and confirmed it renders its real region with no crash.

---

## 2026-08-04 (Pass 7, UI 7) — African Christianity band retired, right after being created: checked overlap with Region instead of assuming

**The question:** "do we need both the syriac and african plus the same
regional" — right after UI 6 gave both Syriac East and Africa their own
confession bands, Mark asked whether that duplicated the Region toggle
(UI 5) rather than accepting the symmetry at face value.

**Checked, not assumed — the two aren't the same case:**
- **African Christianity band vs. Africa region:** 25 entries in the lane,
  23 of them (92%) also region-tagged Africa (22 Africa-only, 2
  Africa+Mediterranean); 1 outlier is North Europe (diaspora). Clicking
  either control produces almost the identical set of boxes. Genuinely
  redundant.
- **Syriac Christianity band vs. Middle East region:** 17 entries, only 8
  (47%) are Middle-East-only. The rest: 4 Greater Asia only (the Church of
  the East's Silk Road expansion into Persia/Central Asia/China), 2
  Mediterranean+Middle East, 1 each of Greater Asia+Middle East,
  Africa+Middle East, Global+Middle East. Less than half the lane is even
  Middle East — this band captures a single lineage spread across several
  regions, which Region alone can't reach. Not redundant.

**Change:** "African Christianity" retired as its own top-level band —
lane 4 folded back into the residual band (renamed from "Ancient &
Cross-Family" to **"No Single Confession"**, alongside Origin and
Cross-Family), with its description explaining exactly why it's there
("23 of its 25 entries are already the Region toggle's Africa almost
one-for-one... use Region to isolate it") rather than silently
disappearing. Syriac Christianity kept its own band unchanged.

**Final seven categories:** Catholic · Orthodox · Protestant & Evangelical
· Pentecostal & Global Revival · Syriac Christianity · No Single Confession
(Origin, Africa, Cross-Family) · Outside.

**Verified via Playwright:** soloing "No Single Confession" turns on lanes
0, 4, and 50 together; soloing "Syriac Christianity" turns on lane 1 alone.
Zero JS errors.

---

## 2026-08-04 (Pass 7, UI 6) — Confession-band relabeling, closing the loop the Region toggle opened

**What this finishes.** UI 5's Region toggle solved the original "isolate
Africa" complaint through a cleaner, independent axis, which is why the
confession-band relabeling got left open rather than folded into that
pass. Mark: "yes, do the confession-band relabeling too."

**Change, in `CATS`:**
- **Protestant split into two full siblings.** The old single "Protestant"
  band silently combined lane 6 (Reformation-era Protestant & Evangelical)
  and lane 7 (20th-century Global Revival & Pentecostal). UI 3's edge check
  found only one connection between them in the census's own data —
  "Holiness Movement formed Azusa Street" — and every lane-7 entry starts
  1904 or later: a wave that grew OUT of Protestant, not a parallel
  confession. Mark's resolution mid-conversation: don't force a
  parent/child nesting either — give Pentecostal & Global Revival its own
  full band, same standing as Catholic or Orthodox, and let the lineage
  live in the description text ("grew out of the Protestant & Evangelical
  line, but its own family here, not a subheading under it").
- **"Other" retired outright**, not just renamed. It was doing two jobs at
  once: naming a real leftover (Origin, Cross-Family — genuinely don't
  reduce to one confession) AND smuggling in the "isolate Africa" and
  "isolate Syriac East" use cases the lane/category axis was never built
  to carry cleanly — which is exactly why Africa read as dumped in a
  grab-bag next to a bridge lane and an ecumenical single-entry category.
  Now that Region (UI 5) carries geography honestly and independently,
  the lane axis doesn't need to also pretend to. Syriac East and Africa
  are each real families in their own right — the Church of the East /
  Syriac Orthodoxy, and Coptic/Ethiopian/Nubian Orthodoxy plus the
  African-founded movements that followed — so each got its own named
  band instead of hiding in "Other." Only Origin (pre-lane, before any of
  these families existed) and Cross-Family (genuinely spans more than
  one) had no honest single-confession label to give; they share one
  small, plainly-named "Ancient & Cross-Family" band rather than a forced
  one.

**Final eight categories:** Catholic · Orthodox · Protestant & Evangelical
· Pentecostal & Global Revival · Syriac Christianity · African Christianity
· Ancient & Cross-Family · Outside. Same 10 lanes underneath, same
solo-then-add-then-All mechanic (UI 4) — this is a relabeling of which
category button each lane sits under, not a new mechanism.

**Verified via Playwright:** soloing "Protestant & Evangelical" turns on
lane 6 only, not 7; adding "Pentecostal & Global Revival" adds lane 7
without re-soloing; "Syriac Christianity" solos lane 1 alone; "African
Christianity" solos lane 4 alone; "Ancient & Cross-Family" solos lanes 0
and 50 together; All resets to all 10 lanes on. Zero real JS errors (same
pre-existing offline Google Fonts failure as UI 5, unrelated).

---

## 2026-08-04 (Pass 7, UI 5) — New Region toggle: real geography, built from the census's own `region` field, independent of the lane/confession axis

**The ask, across several turns:** after the solo-click fix (UI 4) and a design
conversation about cleaning up the lane/category grouping, Mark redirected —
rather than reshuffling which lane-derived "category" Africa/Syriac
East/Cross-Family sit under, "what if we just use actual regions... and if
they show up in more than one they are included." A genuinely new axis, not
a relabel of the existing one.

**Built from real data, not invented.** Every movement already carries a
free-text `region` field (210 unique values across 257 entries) — that's
the ground truth this classification worked from, not a guess. Classified
by word-boundary keyword match (an early naive substring pass false-
positived "USA" inside "Jer**usa**lem" and "Ani" inside "Rom**ani**a" —
caught by spot-checking multi-region entries before writing anything to
the census, not left in). Iterated with Mark through several rounds:
Balkans folded into the Byzantine-zone "Asia Minor" bucket rather than
Mediterranean, except the specifically Greek places (Greece, the Greek
islands, Mount Athos), which carry Mediterranean AND Asia Minor both;
Haiti moved out of "Latin America" ("its not latin") into North America;
New Zealand/the Pacific started as a fold into Global, then — once a
check turned up three OTHER entries also touching Australia/the Pacific
(the Missionary Movement's Native Churches, the Confessional Lutheran
Revival's emigration, the Emerging Church) — got its own real "Pacific"
region instead, per Mark's own rule: fold only if genuinely alone, give a
real region if there's real company.

**Final taxonomy, 10 regions, added as `regions[]` on every one of 257
movements** (additive-only census change — 843 insertions, 0 deletions,
verified valid JSON): Africa · Middle East · Asia Minor · Caucasus ·
Mediterranean · North Europe · Greater Asia · Pacific · North America ·
Latin America — plus a lightweight `Global` tag for explicitly
transnational/diaspora entries. An entry can carry more than one; per
Mark's rule, it shows if ANY of its tags is active, not just the first.

**UI**: new `#regionlegend` row in the filter panel, same solo-then-add-
then-All mechanic already shipped for lanes (UI 4) — click one to solo it,
click more to add them, All resets. Independent axis from lane/confession
and from streams — composes via its own `region-on` class and
`regionfiltering` body class, same fade convention as the other two.
Glossary section added explaining all ten in plain words.

**Verified via Playwright** against a local static server (`file://` still
CORS-blocked): solo Africa → 34/257 visible; adding Mediterranean → 90
visible; a real Africa+Mediterranean dual-tagged entry (Alexandrian
Catechetical Tradition) stays visible through both states; a North-
Europe-only entry (Insular Irish Monastic Christianity) stays hidden
throughout; All resets to 257/257; combined with a lane solo (Africa lane
AND Africa region together) correctly ANDs down to 24 entries. Zero real
JS errors (the one console error was Google Fonts failing to resolve in
the offline sandbox, unrelated to this change).

**Not done in this pass:** the earlier-discussed confession-band
relabeling (pulling Pentecostal & Global Revival out from under the
"Protestant" category as a full sibling, retiring the "Other" catch-all)
— that conversation got superseded by the region work before Mark
confirmed it, since the new Region toggle already solves the original
complaint (isolating Africa) through a cleaner mechanism. Still open,
not committed to.

---

## 2026-08-04 (Pass 7, UI 4) — Lane/category toggle switched to solo-click: "if i want to look at Africa, i have to turn all the others off"

**The complaint:** with 10 individually-toggleable lanes grouped under 5
categories, isolating one lane meant manually turning off every other
category and every stray lane not covered by those categories — many
clicks to get to "just Africa." Mark: "so what i want is all on, when
someone clicks on a toggle it turns them all off except the one selected.
then i can click on others to turn them on. and then have an all button if
i want to turn all of them back on."

**Fixed — solo-then-add semantics, same `laneOff` state, no new data
model:** `toggleLaneTarget(memberKeys)` replaces the old independent
lane-click / category-click handlers. Rule: while nothing is filtered
(`laneOff.size===0`), clicking any target — a single lane button or a
whole category button — SOLOS it, turning everything else off. Once
something is filtered, further clicks are additive/subtractive against
the current active set (click an on target to drop it, an off target to
add it back) rather than re-soloing — so a participant builds up exactly
the set they want one click at a time. A new "All" button (`#laneAll`,
first item in `#legend`) clears `laneOff` back to empty in one click;
dims itself (`.current`) when already all-on so it doesn't read as a
live, clickable action with nothing to do.

Applies uniformly to both the 10 individual lane buttons and the 5
category buttons — clicking a category solos/adds/drops its whole member
set in one action, same rule, no special-casing.

Verified via Playwright against a local static server (`file://` fails —
the census fetch hits CORS with `origin: null`): solo on first Africa
click (`on:[4]`), additive on Latin West click (`on:[5,4]`), subtractive
on second Africa click (`on:[5]`), All button resets to all 10 lanes on,
category solo confirmed on Protestant (`on:[6,7]`). Zero JS errors.

**Left as-is, not part of this fix:** the Streams row (`#streamlegend`) —
default-off, opt-in spotlight highlighting rather than an
inclusion/exclusion filter, a genuinely different interaction already
simple (multi-select, nothing to "solo" against). Mark separately asked
for a from-scratch review of what the toggle *choices themselves* should
be, independent of today's lane/category/stream organization — that's a
distinct, larger question, tracked separately, not resolved by this
mechanical fix.

---

## 2026-08-04 (Pass 7, UI 3) — Checking the scroll-reset fix on mobile surfaced a second, real bug: the close button scrolled away with the content

**Asked to check Pass 7/UI 2 on mobile.** The scroll-reset itself checked
out fine at 390px width (same Playwright method as desktop: scroll to
600px, close, open a different entry, confirm `scrollTop` reads 0).

**But the check surfaced a second, separate, real bug while measuring the
close button's on-screen position:** `#sheet` is both the fixed panel and
its own `overflow-y:auto` scroll container, and `.close` was
`position:absolute` — positioned relative to `#sheet`'s content box, which
means it scrolled away with everything else. Reading any entry longer than
one screen (most of them) made the × disappear off the top of the panel
entirely — confirmed by measuring its `getBoundingClientRect()` before and
after scrolling 600px: it moved to -406px (mobile) / -594px (desktop/
tablet), well outside the visible area, on every breakpoint, not just
mobile.

**Not a hard dead-end** — Escape and clicking the scrim both still close
the sheet — but tapping "somewhere outside the panel" isn't an obvious
gesture on a touch device with no keyboard, and the visible affordance
disappearing while reading is a real rough edge regardless.

**Fixed:** `.close` switched from `position:absolute` to `position:sticky`,
kept in normal flow with a negative bottom margin so it doesn't push
`.grab`/`#sheetBody` down, background matched to the panel so it stays
legible over scrolled text, `z-index:1` so it stays on top.

**Verified, not assumed:** bounding-box position confirmed identical before
and after a 600px scroll (truly pinned, not just visually close);
`elementFromPoint` at its own coordinates confirmed it's genuinely on top
and not obscured; an actual click after scrolling confirmed it still closes
the sheet, on both mobile (390px) and desktop (1280px) — zero JS errors.
Screenshots taken with the sheet open and scrolled confirm it reads cleanly
in the corner, not floating oddly over text. Full harness re-run clean
after (257/0/0).

**Heart of it:** this is exactly the kind of bug that only shows up once
someone actually goes looking with real content and a real scroll depth,
not a fresh-open screenshot — worth remembering that "checked on mobile"
should mean interacting with it in a realistic state, not just confirming
the layout renders.

---

## 2026-08-04 (Pass 7, UI 2) — Click-doc sheet no longer opens mid-scroll on a fresh entry

**The bug:** `#sheet` (the click-doc panel that slides in from the right) is
its own `overflow-y:auto` scroll container, and `openSheet()` never reset
`scrollTop` when swapping in a new entry's content. Scroll down reading a
long entry, click a different world, and the new entry opened already
scrolled past its own header — most noticeable going from a long entry
straight into a short one.

**Fixed:** `sheet.scrollTop=0` added right after the new content is written
in, before the sheet becomes visible (`sheetBody.innerHTML=h` → `scrollTop=0`
→ `removeAttribute('inert')` → `.on` class) — no flash of the wrong
position. Verified with a targeted Playwright check: scrolled a sheet to
800px, closed it, opened a different entry, confirmed `scrollTop` reads 0.
Full harness re-run clean after (257/0/0).

**Shipped straight from `main`'s current copy, not the feature branch's** —
Mark's own instruction: *"we have updated other parts of the sight so don't
use an old version of the website... everytime we make a change it reverts
back to an old version of the landing page."* Confirmed first that this
branch's `atlas-v3.html` differs from `main`'s by exactly one stale line
(the footer's self-link), applied the one-line scroll fix directly against
`main`'s actual current file rather than risk reintroducing that or any
other drift, then backported the identical fix here for consistency going
forward.

---

## 2026-08-04 (Pass 7, UI 1) — Filters collapsed behind a single toggle: controls went from most of the mobile screen to one compact row

**The problem, confirmed by screenshot before touching anything:** on mobile
(390px), `#controls` — the sticky search/toggle header, the 18-button lane/
category legend, and the 10-button streams row — ran to roughly two-thirds
of the viewport, leaving only about two map boxes visible before a
participant had to scroll. On desktop it was closer to half. Mark's own
framing: *"the choices at the top is to thick... when it takes up the top
half of the screen it is a problem, also the phone it takes up the top two
thirds and scrolls, so you cant see the worlds on the screen very well."*
Cropped the actual mobile-fold screenshot to verify before diagnosing —
confirmed the legend + streams stack, not the search row, was the real bulk.

**Fixed:** `#legend` and `#streamlegend` now live inside a collapsible
`#filterPanel`, hidden by default (`max-height:0`), opened by a single new
"Filters" chip in row1. Row1 itself — search, Built worlds, Filters, Copy
link, count, theme — is the only piece that's always visible, and it's
compact: one line on desktop, two on mobile. Sticky positioning is
unchanged, so the win holds at any scroll depth, not just at the top of the
page.

**Two things kept it honest rather than just smaller:** a small badge on the
Filters chip shows the actual count of active lane/category + stream
filters, and it stays visible even while the panel is collapsed — collapsing
never hides *that* a filter is on, only the full grid of options. And if a
participant arrives via a shared link that already carries active filters
(`?laneoff=...` or `?streams=...`), the panel auto-opens once at boot so
they aren't left looking at a thinned map with no visible reason why.

**Verified functionally, not just visually:** a targeted Playwright check
(not the full harness, which predates this feature) confirmed open/close via
the toggle, the count badge updating live and persisting through collapse,
and auto-expand firing correctly from a URL carrying `laneoff` params —
zero JS errors in every case. Full harness re-run clean after (257/0/0).
Before/after mobile-fold crop: controls dropped from ~560px to ~150px in the
same viewport, with roughly 20 map boxes now visible where 2 were before.

**Next action:** none pending — this was a self-contained fix. Worth
watching whether "Built worlds" and "Copy link" also deserve moving behind
the Filters panel later if row1 itself ever starts feeling crowded again,
but they're single chips, not groups, so leaving them inline was the right
call for now.

---

## 2026-08-03 (Pass 6, scale-up 3) — All 9 planned Opus reviews returned; a systemic template bug found and fixed; ~50 per-entry fact fixes applied

All 8 remaining review agents (Eras 2 through 9, one per era, Era 9 covering
both a+b batches together) reported. Combined with Era 1's earlier review,
this closes out Mark's "9 reviews, not 221" instruction.

**The single biggest finding wasn't in any individual entry — it was in the
template.** Every one of the 8 reviewers, working independently on
different eras, converged on the same discovery: two fields the writer
agents were never asked to touch — `statusDescription` and
`sources[].note` — render verbatim on the public click-sheet (`atlas-v3
.html`, under "Status" and "Sources to research") and are saturated with
internal Step 0 methodology language. `statusDescription` carried things
like "Reviewed at the Era 4 Step 0 run and tiered Strong (Tier 1)...
Added at the Era 4 gate (Mark, 2026-08-02)" — Mark's name and internal
dates, live on a public page, on roughly 200 of 257 entries.
`sources[].note` was worse: `[S]` markers, "the census flags," "LOAD-
BEARING for the floor register," "tier care," "verified this session" —
on roughly 500 of 693 source notes. Neither field was part of this pass's
brief (writer agents were scoped to 6 other fields), so this bug predates
the content-writing pass entirely; the reviews simply exposed it because
they read the whole rendered sheet rather than just the JSON diff.

**Fixed at the template level, not per-entry** — cheaper and impossible to
regress by a future edit. `statusDescription` rendering was swapped for
`statusMeta[status].description`, the one-line, already-clean, plain-
English text that exists once per status category (12 categories, not
257 entries) and was already used nowhere else on the page. `sources[]
.note` stopped rendering entirely — visitors now see the linked/unlinked
work title only, which was always the useful part; the research notes
were internal reading aids, never written for a visitor. Also folded in:
the `eraState` fallback string (used when `longDescription`/`voices`/
`legacy`/sources are empty) still said "Phase One Step 0 record" and
"Frozen by Mark" — rewritten in plain language.

**Per-entry fixes.** Beyond the systemic bug, the 8 reviews surfaced
~50 CONFIRMED factual errors across Eras 2-9 (Era 1's 9 already applied
and committed separately) — wrong dates, reversed causation, overstated
superlatives contradicted by an entry's own neighbor or its own linked
source, a couple of straightforwardly wrong facts (the Chaldean/Assyrian
patriarchal lines were swapped in VI.30; VIII.1 had Allen rather than
Absalom Jones pulled from the segregated gallery; VII.4's "before anyone
else" claim was flatly contradicted by VII.2's own "first" claim three
paragraphs earlier in the same file). Also fixed: three floorNotes on
VIII.14/15/44 that had literally spliced two draft sentences together
mid-word with the internal apparatus left in ("FORMAL DISPOSITION
recorded at the Era 9 gate... the Methodology's own named A1 example");
a run of bare atlasId cross-references in several floorNotes ("as II.4",
"precedent II.4") rewritten to state the actual fact instead of pointing
at another entry's internal ID; several duplicate "continued into the
next era" sentences in `legacy` fields that repeated, almost verbatim,
a line the UI already renders automatically from `continuesAs`. All
applied via targeted scripts (exact string match, verified non-silent),
re-validated (0/0) and harness-tested (257/0/0) after every batch.

**Left for later, logged so it isn't lost:** each review also filed a
long MINOR/JUDGEMENT-CALL list (soft superlatives, contested attributions,
weak experienceToday link quality, coverage gaps, bare "No question"
floorNotes read as a checkbox rather than a sentence) — not applied this
pass, kept in the review transcripts for a future editorial pass. Also
queued: a second look at whether `floorNote`'s common "No question" bare
stub (136 uses file-wide, pre-existing) should become a full sentence
per the house style the rewritten ones now model.

Committing this as one checkpoint: the template fix, all per-entry
CONFIRMED corrections, and the three broken Era-9 floorNotes.

---

## 2026-08-03 (Pass 6, scale-up 2) — Eras 4, 5, 8, 9a, 9b merged (127 entries); Era 1's adversarial review returned — 9 confirmed findings, all fixed

The remaining five writer batches all reported. Unlike Era 1/2/6/7 (which
wrote directly to the live file after finding their assigned worktree stale
— see Pass 6/1 below), these five each self-corrected by resyncing their
OWN worktree copy from the live branch tip before writing, then stayed
inside worktree isolation and left the shared checkout untouched. That
meant a different merge step: a targeted script read each worktree's copy,
copied only the six content fields (`longDescription`/`teaser`/`voices`/
`legacy`/`experienceToday`/`floorNote`/`sources`) for that batch's specific
`atlasId`s into the live file, and left everything else — including the
other batches' already-landed work — untouched. Applied Era 4 (22), Era 5
(26), Era 8 (29), Era 9a (25), Era 9b (25) = 127 entries in one pass.
Verified: exact expected count (225 = 4 pilots + 221 of Eras 1-9, with
Era 10's 32 still correctly deferred), validator 0/0, harness clean
(257 nodes, 0 overlaps, 0 JS errors).

**Era 1's Opus adversarial review landed in the same window** — the first
of the 9 planned per-era reviews. It confirmed the content is honest and
well-hedged throughout (explicitly checked for internal-process leakage
across all 11 entries and found none), but surfaced 9 real, fixable
findings, all applied directly to the live file:

- I.1 `legacy` claimed the Didache had been "continuously read for
  nineteen centuries" — false; it was lost and recovered from a single
  manuscript only in the 1870s. Reworded to state that honestly.
- I.1 `voices` said Polycarp was "burned alive" — the *Martyrdom of
  Polycarp* itself says the fire didn't consume him and he was killed by
  the sword. Corrected to "put to death at Smyrna."
- I.22 `teaser`/`experienceToday` called Cao'an "the world's only
  surviving Manichaean temple" — the linked source itself notes at least
  one other (Xuanzhen Temple) survives intact. Hedged to "long regarded as
  the only intact surviving" one.
- I.25 `longDescription` dated the Pepuza/Tymion identification to 2001;
  Tabbernee's actual find was July 2000. Corrected.
- I.26 `longDescription` called Novatian's rival consecration "the first
  such... in the city's history" — contested (Hippolytus and Natalius have
  earlier claims). Softened to "one of the earliest."
- I.25/I.26 `why`: both parentheticals restated the person-defined concern
  they were disclaiming ("its authority claim rests on three named
  prophets" / "defined by one man's rigorist stance") instead of stating
  the actual sourcing concern. Rewritten to name what survives in the
  record, not who's in charge of it.
- I.25 `statusDescription` said evidence "centers on three named prophets'
  own claims," dropping the hostile-source half that `legacy` and `voices`
  both already state is the larger share of what survives. Added it back.
- I.25/I.26 `statusWord` had drifted to "Still investigating," diverging
  from `statusMeta`'s own `shortWord` ("Contested evidence") and from
  sibling entry I.24 under the same status — an inconsistency visible on
  the hover card. Restored to "Contested evidence" on both.

All 9 fixes applied, re-validated (0/0), harness re-run clean. Committing
this alongside the 5-batch merge as one checkpoint.

Addressed both remaining self-flagged issues: I.12's `floorNote` ("Heresio-
logical 'Nestorian' label is not its own confession...") rewritten in plain
language; V.16's `experienceToday` link (a regional tourism portal) swapped
for the Waldensian Cultural Centre Foundation's own domain, already
independently verified elsewhere in the census on IV.8. Left the Era 2
agent's Priscillian/Compostela omission as-is — the tomb-identification
theory is itself a contested, speculative academic claim, and omitting a
speculative claim under search-budget pressure is the correct call under
the brief's hedge-or-omit rule, not a gap to fill.

Next: launch Opus reviews for Eras 2, 3, 4, 5, 6, 7, 8, and one combined
review for Era 9 (a+b together) — 9 reviews total, per Mark's instruction,
not 221.

---

## 2026-08-03 (Pass 6, scale-up 1) — Era 1 content batch complete, committed as safety checkpoint ahead of formal review

Scaling the click-doc content pattern (longDescription/teaser/voices/legacy/
experienceToday) from the 4 pilots to the remaining 221 Eras 1-9 entries.
Launched 10 parallel background agents (one per era, Era 9 split into two
25-entry batches) in isolated git worktrees, from a shared written brief
(`Design/CiC_Atlas_ContentPass_TaskBrief_2026-08-03.md`) carrying the exact
voice/honesty rules already proven on the pilots.

**A real risk surfaced immediately**: the Era 1 agent's own worktree copy of
the census was stale (out of date vs. the live file by the time it started),
so it made its own call to write directly to the live main-tree file instead
of its isolated copy — bypassing the isolation this was set up to provide.
With 9 more agents running concurrently and several likely to hit the same
staleness, this is a real concurrent-write race: two agents both reading an
old snapshot before either saves could silently clobber each other's output.
Mark's ask (a full Opus review per era, not per-entry) compounds the timing
question — reviewing takes time, widening the window a later agent's write
could land badly.

**Mitigation**: commit each verified era batch immediately as a checkpoint
BEFORE running its formal review, rather than holding it uncommitted while
reviewing — a committed state is safe from being silently overwritten by a
later agent's stale write (git history preserves it even if a later write
does clobber the live file; worst case is a diff to reconcile, not lost
work). Review happens against the committed state; any review findings get
fixed in a follow-up commit. This trades a small process deviation (review
technically happens after, not before, commit) for closing the actual
vulnerability faster.

Era 1 (11 entries: I.1, I.2, I.7, I.8, I.17, I.20, I.21, I.22, I.24, I.25,
I.26) verified directly — spot-read full content on 4 of them (House-
Churches, Marcion, Montanism, Novatianism), confirmed real narrative voice,
honest omission of experienceToday where nothing verifiable exists (Marcion,
Montanism, Novatianism correctly have none — the agent's report explicitly
named and rejected a tempting-but-unconfirmable candidate, Pepuza/Tymion for
Montanism, rather than guess). Two real data-consistency bugs the agent
itself flagged and I fixed before committing: I.25/I.26's `chip`/`glyph`
fields still read "exc" (closed-door) instead of "cev" matching their
Contested-Evidentiary status (confirmed dead/unused in the live template —
icon selection reads `status` fresh, not these fields — but still wrong
data); and both entries' `why` field still said "Excluded on the person-
defined ground," contradicting the corrected Criterion 2 framing already
applied to their `statusDescription`/`legacy`. Rewrote both `why` fields to
state the actual concern (limited primary sourcing) consistently. Full
harness clean (257/0/0), validator 0/0. Committed.

Opus review agent for Era 1 launching next; remaining 9 agents (Eras 2-9)
still running.

---

## 2026-08-03 (Pass 5, click-doc review 12) — Status line moved to the end and rewritten as 4 plain categories; MAJOR: Criterion 2 (person-defined exclusion) clarified by Mark — corrects a real methodological misapplication risk, 2 entries reclassified

Two things happened in one exchange: the last structural piece of the
click-doc reorder (Section 2, deferred since the very first review pass),
and a genuine correction to how Criterion 2 of the Step 0 methodology has
been described and applied.

**The status line rewrite**: Mark wanted it in plain English, four
categories only — "yes built, identified as a future build, still
investigating, currently out of scope because..." — dropping the
single-voice jargon wording entirely. Implemented by computing the plain
label from the SAME house/plans/question/door classification that already
drives the status icon (`st`), not the raw per-entry `statusWord` field —
which sometimes carries its own process phrasing (VIII.10's statusWord was
"Creedal question — two window-specific findings recorded (Era 9 Step
0)..."). `statusDescription` is kept as the supporting detail sentence,
since it's already in plain words for most entries. Moved from position 2
(right after the header) to the very last block in the document, per the
standing decision from the start of this review ("not sure people want to
know our internal decision making criteria" up front).

**The methodology clarification — the more important part**: while reading
through what "currently out of scope" would actually say for excluded
entries, Mark caught that the current Criterion 2 language ("authority
rests on one person's revelation or standing") risks being read as
excluding any tradition centered on or initiated by a leader. That was
never the intent. His own words: **the actual target is traditions with
"limited or singular primary sourcing (so the sources only speak from one
voice)"** — a sourcing/evidence question, not a leadership-structure
question. A tradition that started with one person but grew a real,
independently-documented community — "significant breadth in primary
sourcing to build a living ecology around the theology and teachings and
practices" — is NOT what Criterion 2 is meant to catch. Leader-initiated is
fine; single-voice-sourced-forever is the actual concern.

Checked this against the only two entries currently carrying "Excluded -
Person-Defined (C2)" status, and the ambiguity turned out to be real, not
hypothetical:
- **I.25 Montanism**: its own `why` field already carried a live, unresolved
  question — "Phrygian inscriptions may document a wider communal ecology -
  the test might yield here" — meaning the original analysis itself wasn't
  fully confident this was single-voice-only.
- **I.26 Novatianism**: reasoning cited "defined by one man's rigorist
  stance... rather than a broader communal tradition" — already gesturing
  at the sourcing-breadth question, just phrased ambiguously enough to read
  as leader-based exclusion.

Mark's explicit call, mid-conversation: reclassify both from "Excluded -
Person-Defined (C2)" to **"Contested - Evidentiary"** — "still investigating,
but limited primary sources are a concern" — rather than leave them marked
as settled exclusions under a criterion that may have been misapplied.
Rewrote both `statusDescription` fields to state the corrected concern
plainly (limited primary sourcing, explicitly NOT "a leader was involved"),
updated `meta.statusCounts` (Excluded-Person-Defined 2→0, removed the key
entirely since it's now empty; Contested-Evidentiary 4→6), verified 0
errors/warnings. Visually confirmed Montanism's icon on the live chart
changed from closed-door to question-mark as a direct consequence.

**What this is NOT**: a full Step 0 re-adjudication. This was Mark
exercising his own gate authority directly, on two specific, already-flagged
edge cases, in real-time conversation — not an autonomous reclassification.
The underlying evidentiary question (does either tradition actually have
independent community-voice sourcing beyond its central figure?) is still
open and unresolved; "Contested - Evidentiary" says exactly that, no more.

**Queued, not done**: the Criterion 2 language itself lives in
`Design/CiC_Step0_Criteria_Relook_V1_0.md` and related Round 1/2 review
docs — those should get updated to carry this clarified definition
verbatim, so future Step 0 runs (Era 10 and beyond, whenever Fable resumes
that work) apply the corrected criterion rather than rediscovering this
ambiguity per-entry. Not done in this pass — flagged here so it isn't lost.
Also worth a future sweep: are there OTHER entries anywhere in the census
(Pre-Survey Candidates, Deferred, etc.) whose reasoning leans on the old
"centered around a leader" framing rather than the corrected "single-voice
sourcing" framing? Not checked here — this pass only touched the 2 entries
already carrying a live C2 exclusion.

Verified end-to-end: full harness clean (257/0/0, no JS errors), census
validator 0/0, visually confirmed all four plain-language status categories
render correctly (Alexandria "Yes, built," Donatism "Identified as a future
build," Montanism "Still investigating" with no redundant phrasing, Marcion
"Currently out of scope") and Montanism's chart icon updated live.

---

## 2026-08-03 (Pass 5, click-doc review 11) — Section 11 ("Relations, in brief") cut — same internal-voice bug as `why`/`sourcing`, worse in one case

Checked `relationsSummary` against Section 7's structured edges before
recommending anything: for VII.5 Methodists, it substantially restates in
prose what the structured edges already show with better sourcing
(confidence tags, jump links) — genuinely redundant when edges exist. When
they don't (all 4 pilots have zero structured edges), it's not safely
neutral either — found real internal-process leaks sitting inside it: VI.24's
`relationsSummary` includes "Lane note: drafted lane 6... the lane change is
disclosed, not silent" (us talking to ourselves about our own census-
construction choices), and VII.5's includes "Named at the Era 9 Freeze
(Mark)" mid-sentence — a literal internal meeting reference. Same category
of bug as `why` and `sourcing`, not a new one. Mark: "yes cut it, keep going."

Removed the section entirely. Any genuine relational fact buried in
`relationsSummary` that isn't already captured structurally (Section 7) or
narratively (Sections 3/5) is now the content pass's job to fold into real
prose, not something displayed raw. `relationsSummary` stays in the search
haystack (backend matching, not display) — untouched. Full harness clean,
census validator 0/0.

---

## 2026-08-03 (Pass 5, click-doc review 10) — Section 10 ("Status report") cut

Mark: "cut it, keep going." Removed — it was `statusReport||statusDescription`,
almost always resolving to a near-verbatim repeat of Section 2's status
line since `statusReport` is essentially never populated. Section 2 is
already queued to move to the end of the document and will carry this job
alone. Full harness clean, census validator 0/0 (template-only change).

---

## 2026-08-03 (Pass 5, click-doc review 9) — Legacy widened to cultural/experiential influence, with verified "Visit today" links

Mark: widen "What it left behind" beyond formal denominational/doctrinal
succession to include art, distinctive spiritual practices, stories, sermon
illustrations, and architecture that influenced or were adopted by other
Christian movements — even without a clean, direct, formally-traceable
line — and where something can genuinely still be experienced today, link
to it.

Researched all four pilots via WebSearch before writing anything, same
discipline as every content addition this pass:
- Donatism: Timgad, Algeria — a UNESCO World Heritage Roman city that was
  a real Donatist stronghold, its excavated basilica ruins still standing.
  Added to the legacy paragraph and as an experienceToday link.
- Adventism: the William Miller Farm in Low Hampton, NY — his restored
  home, the chapel he built, and Ascension Rock, actively preserved and
  open for tours by Adventist Heritage Ministries.
- Czech Churches: two real, verified links — Herrnhut, Germany (the
  Moravian Church's founding town, a living community, newly UNESCO-listed
  in 2024) and the Comenius Mausoleum in Naarden, Netherlands (his actual
  tomb, rediscovered 1929, open to the public).
- Humiliati: checked specifically for a surviving building — found one
  candidate (Santa Maria di Cantalupo, Milan) but no stable citable page
  for it, and the other known Humiliati church (Santa Maria in Brera) was
  demolished in 1808-09. Left this one without a forced link rather than
  attach an unverifiable one — the honest "no clear record" legacy text
  already says the true thing.

New `experienceToday` field: array of `{text, url}`, rendered as "Visit
today: [link]" paragraphs after the legacy prose and continuesAs lines,
visually distinguished from the "Sources to research" bibliography (verified
by checking actual rendered hrefs, not just that the markup looked right).

Verified visually on the Czech Churches entry: both new links render
correctly, AND a previously-invisible chain surfaced automatically —
"Continues from Hussites" now appears, a real consequence of the
continuesAs bug fixed two entries ago (V.6 → VI.24 was one of the 60
missing pairs). Full harness clean, census validator 0/0.

---

## 2026-08-03 (Pass 5, click-doc review 8) — Section 8 merged into "What it left behind"; found and fixed a major stale-data bug along the way (chart was silently missing 60 of 71 real succession chains)

Mark: "can this be merged into the legacy section as a specific piece" —
Section 8 ("Ongoing church," the continuesAs prev/next links) folded into
Section 5 ("What it left behind") as an unlabeled continuation right after
the legacy paragraph, rather than its own heading. Both sections answer the
same underlying question — what became of this tradition — one in prose,
one as a structured identity-succession fact.

**Real bug found while verifying the merge, not by going looking for one**:
tested against VI.6 Huguenots, which I knew from earlier stream research
has a real `continuesAs` chain to VII.22 Church of the Desert — and it
didn't render. Traced it to `CONTINUES`, a hardcoded 11-pair array in
`atlas-v3.html`, still carrying its own comment calling itself "PROVISIONAL
DEMO DATA... needs a census `continuesAs` field" — written before the
census had that field at all. The census has carried real `continuesAs` on
71 movements for most of this session (used directly, repeatedly, in the
A4 succession-spine work and the streams batches) — the atlas page never
picked it up. **The chart's own visual continuity rendering (which
pairs get a flowing tail into their successor vs. a closing seal), the
hover/click trace highlighting, and the click doc were all silently running
on 11 of 71 real pairs** — 60 real identity-succession chains were
invisible on the live page this whole time, this session's own work
included.

Fixed at the root: `CONTINUES` and its hand-maintained array deleted;
`contNext`/`contPrev` now built by iterating `DATA.movements` and reading
each entry's own `continuesAs` field directly — the same single-source-of-
truth discipline every other part of this page already follows. Also
caught and fixed an adjacent inconsistency spotted during verification: the
"Lineage" empty-state note ("No relationship is drawn for this entry")
only checked influence edges, so an entry with a real continuesAs chain but
no influence edges (like the Huguenots) showed a technically-true-but-
misleading "no relationship" note directly beneath its own continuation
line. Now suppressed when either kind of relationship exists.

Verified thoroughly given the blast radius (this touches chart geometry,
not just text): full harness clean (257/0/0, no JS errors, no overlaps)
both before and after; visually confirmed the Huguenots entry now shows
"Continues as Church of the Desert" under "What it left behind" with the
misleading Lineage note correctly suppressed; spot-checked the full-page
render for layout coherence. No census changes — this was purely a stale
duplicate-data bug in `atlas-v3.html`, not a data problem.

---

## 2026-08-03 (Pass 5, click-doc review 7) — Section 7 relations reviewed, kept as-is structurally; found and fixed the naming-hierarchy bug in 3 places

Section 7 (structured relation edges: shaped-it/shaped-by/tension/
contemporaries, confidence tags, jump links) was already good — Mark's call:
keep the structure, no redesign needed. But close reading turned up a real
regression from Section 1's naming-hierarchy decision: `edgeRow()` linked to
related entries using their academic `name`, not `shortName||name` — every
relation link on the page was quietly bypassing the hierarchy set two
sections ago. Swept the whole file for the pattern rather than assuming this
was the only instance, and found two more: the "Continues from/as" links
(Section 8) and the thread-hover tooltip (`a.name → b.name` when hovering a
lineage line on the chart itself) had the identical bug. All three fixed
together. Confirmed via grep that every remaining `.name` reference in the
file is now either the correct `shortName||name` form or the deliberate
secondary/academic-name line — not just the one spot that was reported.

Full harness clean, census validator 0/0 (no data changes this pass, purely
a template fix).

---

## 2026-08-03 (Pass 5, click-doc review 6) — "Where it stands on the Creed" rewritten in plain language (same bug as `why`, found by the same instinct)

Checked `floorNote` before recommending anything, same discipline as every
section so far — found the identical bug `why` had: dense internal Step 0
methodology language ("A1 pass," "C2 RUN at the Era 9 gate," "FORMAL
DISPOSITION," "register status," "window-specificity") sitting under a
plain-English heading. Two of the four pilots (Humiliati, Czech Churches)
correctly show nothing here — genuine "no question" cases, confirming this
isn't a universal leak, just this specific field's habit when there IS a
real creedal question on record.

Unlike Sections 3/4/5, this wasn't a wrong-field problem — `floorNote` is
the right field, just written in methodology voice instead of visitor
voice. Rewrote the two pilots' content directly (no template change needed,
the display logic was already correct):
- Donatism: "Cleared Step 0 (A1 pass on record)" → a plain statement that
  the dispute was disciplinary (who could validly serve as clergy), not
  doctrinal — Donatists held the same Nicene content as their rivals.
- Adventism: the dense paragraph → the same underlying facts in plain
  language — the 1872 Declaration's non-trinitarian wording, the 1931
  trinitarian confession, and the unresolved question about Ellen White's
  prophetic authority relative to Scripture — stated as facts, not
  methodology jargon.

Verified visually: Adventism's full document now reads as one coherent,
plain-language whole — story, voices, legacy, creed-standing all in the
same accessible voice. (The status line above it still shows old jargon —
Section 2, already queued to move to the end, not touched this pass.) Full
harness clean, census validator 0/0.

---

## 2026-08-03 (Pass 5, click-doc review 5) — "What survives" (evidence-richness) replaced by "What it left behind" (legacy)

Section 5 had the same mismatch as Section 3's original bug: `sourcing`
under a heading ("What survives") that promises one thing (living
descendants, surviving institutions/practices) while the field actually
answers a different one (how well-documented the tradition is for our own
research purposes). Also overlapped functionally with Section 9's source
bibliography.

Mark reframed it as its own real question, distinct from both the
narrative and the structured relation edges already in the template: "how
did it influence the ongoing story" — did it become an ongoing
denomination, leave a legacy of influence without institutional
continuation, or hand something down that outlived it — and if genuinely
none of those, say so plainly rather than force a claim.

New `legacy` field, heading "What it left behind," `sourcing` fully retired
from the visitor template (confirmed no remaining references) — same fate
as `why`, both were internal researcher bookkeeping, not visitor content.
Wrote real, differentiated legacy content for all four pilots, each a
genuinely different case:
- Donatism: no continuing church, but real doctrinal influence — Augustine's
  mixed-body ecclesiology and ex opere operato sacramental theology both
  developed directly out of arguing against it.
- Adventism: became an ongoing denomination (Seventh-day Adventist Church).
- Humiliati: genuinely nothing recorded — said as an honest "no clear
  record," not padded.
- Czech Churches: a real "gift that lived on" already cross-referenced
  elsewhere in the census — VII.4 Moravian Church at Herrnhut's own
  relationsSummary explicitly names receiving this exact entry "across the
  1627-1722 hidden-seed century." Confirms this new section can draw on
  connections the census already carries, not just fresh research.

Verified visually: the Czech Churches entry now reads as a complete arc —
story, voices, legacy, creed-standing — in one coherent flow. Full harness
clean, census validator 0/0.

---

## 2026-08-03 (Pass 5, click-doc review 4) — "Major voices": found genuinely dead since launch, populated for real rather than cut

Checked Section 4 before recommending anything: `voices` is empty for
**all 257 entries, including all 6 built worlds** — not "mostly empty for
unbuilt worlds" like the earlier sections, never populated once, anywhere.
Every visitor has been seeing "Not yet gathered" 100% of the time since this
shipped. Also noticed the four pilot narratives already name their key
figures inline (Augustine, Miller, Comenius) — a bare separate name-list
risked just repeating the story in flatter form. Recommended cutting the
section. Mark: "we should be able to build this out at this point also" —
build it, don't cut it.

Verified four more names before writing anything (same discipline as the
source links): Petilian of Cirta (a real Donatist bishop Augustine wrote
against, his own words lost except as Augustine quotes them) and Tyconius
(a Donatist theologian whose ecclesiology shaped Augustine despite his own
party's suspicion of him) for Donatism; Hiram Edson and Joseph Bates'
specific roles alongside Miller and White for Adventism; Jan Blahoslav's
role starting the Kralice Bible translation for the Czech Churches.

The Humiliati entry surfaced a real distinction worth keeping visible: no
individual founder is named anywhere in the record — this is a lay
collective, organized by trade and locality, not around a founding
figure. Used a one-line explanatory entry instead of the "Not yet
gathered" fallback for it, because "not yet gathered" would be dishonest
here — it's not that the research hasn't happened, it's that there isn't a
prominent name to report. Different honest state, said as such.

Rewrote the render from one middot-joined line to one paragraph per voice,
since each entry now carries real context ("Name — role/significance") that
reads better as a short list than crammed onto one line. Verified visually
in a real browser (Donatism's four voices, one per line, readable). Full
harness clean, census validator 0/0.

---

## 2026-08-03 (Pass 5, click-doc review 3) — Hover teaser + clickable sources shipped; 4 pilot entries fully written and verified end-to-end

Mark, reacting to the four sample `longDescription` drafts: "yes this
combined with the ability to investigate listed sources and a brief
contextual overview in the previous section seems to work well." Clarified
two things before building: the "brief contextual overview" meant a
genuinely distinct hover-card teaser (not today's mechanical truncation of
the full paragraph), and "investigate listed sources" meant real clickable
links where a source actually has one online — confirmed both directly
rather than guess and build the wrong thing.

**Schema**: new `teaser` field (a hand-written sentence, same shape as the
six built worlds' existing `entry.tile` — hover already fell back to
`entry.tile` for those, so nothing duplicated) and an optional `sources[].url`
field, both additive/backwards-compatible like every schema change this
project has made.

**Sourced for real, not guessed**: before attaching any link, used WebSearch
to verify four real, stable sources exist and confirm exact facts along the
way — this is also where IV.27's suppression date firmed up from a vague
"sixteenth century" placeholder to the actual 1571 papal bull, confirmed by
the Catholic Encyclopedia entry itself:
- I.4 Donatism → Augustine's own "On Baptism, Against the Donatists" (New
  Advent) — fitting, since the entry's own point is that Donatist voices
  survive mostly through their opponent's pen.
- VIII.10 Adventism → William Miller's 1836 "Evidence from Scripture and
  History" (Internet Archive, the actual primary text already cited in the
  entry's existing `sources[]`).
- IV.27 Humiliati → Catholic Encyclopedia's Humiliati entry (New Advent).
- VI.24 Czech Churches → Wikipedia's Bible of Kralice entry, for the
  Unity of the Brethren's lasting literary work.

**Template**: hover tooltip now shows `teaser||entry.tile` instead of a
truncated slice of `longDescription` — absent rather than faked when a
teaser doesn't exist yet, matching every other honest-gap pattern already
in this template. "Sources to research" now renders `x.work` as a link
(gold, matching the site's existing link-adjacent styling) when `x.url` is
present, plain text otherwise.

Wrote real `longDescription`/`teaser`/sourced-`sources[]` for all four pilot
entries (I.4, VIII.10, IV.27, VI.24) — not placeholders, the actual content
Mark reacted to. Verified end-to-end in a real browser: Donatism's hover
card shows its teaser distinct from the full paragraph, its click doc shows
the full narrative under "About this world" plus a working clickable link
(confirmed the actual `href`/`target` on the rendered anchor, not just that
markup looked right) to Augustine's text. Full harness clean (257/0/0).

**Not yet decided**: how to scale this from 4 piloted entries to the
remaining ~221 (m.era 1-9, still no longDescription) — batch size, whether
via a managed background agent per the streams/status-description pattern,
and what review gate catches errors before they ship. That conversation is
next, now that the shape and sourcing discipline are proven on real
examples rather than a plan.

---

## 2026-08-03 (Pass 5, click-doc review 2) — "About this world" stops leaking Step 0 methodology text; content-writing pass scoped correctly to Eras 1-9

Continuing the click-doc section-by-section review. Two decisions:

**Section 2 (status line) reordering**: Mark — "if we keep 2, this should
be at the end, not the second... not sure people want to know our internal
decision making criteria." Decided: final order will be Header → About this
world → [sections TBD] → Status line, last. Not yet implemented in code —
holding the actual reorder until all 12 sections are through review, so it
happens once instead of being re-shuffled section by section.

**Section 3 ("About this world")**: confirmed the diagnosis from the prior
entry — `longDescription||why` was showing Step 0 methodology reasoning
("why this counts as its own tradition") under a heading promising a
description of the tradition itself, for all 251 non-built entries. Mark:
"this should be tell me about this tradition, we dont need to reveal our
system thinking here." Dropped the `why` fallback from both the click doc
and the hover-card preview (which had the identical bug via the same
`rawDesc` fallback chain) — no content, no leak; falls through to an honest
"Not yet written" placeholder instead, same pattern as the existing "Major
voices" fallback.

Discussed structure and content plan for actually writing that missing
content rather than leaving the placeholder long-term. Decided: one
unified narrative paragraph per entry (not split into rigid sub-fields like
"Beliefs"/"Fate" — those don't apply cleanly to every tradition, e.g. a
still-living one has no past-tense "what happened to them"), drawing on
material the census already has (`why`, `relationsSummary`, `sourcing`,
`floorNote` — real historical content, just written in methodology voice)
plus the project's standing six reference works and reliable web sources
for gaps. Explicitly NOT required to go through full Step 0 build-cycle
discipline — that discipline decides whether something belongs on the map;
these entries already cleared it, so writing their story is separate,
lighter work.

**Scope correction, caught before drafting anything**: Mark asked directly
whether Step 0 had already run for all eras but 10 — checked the census
directly rather than assume: Eras 1-2 are Phase One COMPLETE, Eras 3-9 are
Frozen by Mark, Era 10 is "Step 0 not yet run — pre-survey signals only."
Real trap found in the same check: atlasId roman-numeral prefixes do NOT
reliably track `m.era` — e.g. "IX.1 Azusa Street"'s atlasId reads as Era 9
but its actual `m.era` is 10 (historical ID drift). Scoping the
content-writing pass by atlasId prefix would have silently pulled in Era 10
entries whose own inclusion isn't decided yet — used `m.era` instead. Exact
count: 225 entries (m.era 1-9, no longDescription yet) are fair game now;
32 entries (m.era===10) wait for the Fable Era 10 Step 0 run already queued
from earlier this session. Zero entries currently have longDescription at
all — even the 6 Built & Live worlds carry their description in a separate
`entry.tile` field, so this pass doesn't touch or duplicate that.

**Next**: draft `longDescription` for 3-4 sample entries (varied era/amount
of existing material) before committing to any batch/agent approach, so
Mark can react to real prose rather than a plan.

---

## 2026-08-03 (Pass 5, click-doc review 1) — Naming hierarchy flipped: relatable name leads everywhere, academic name demoted

Starting a section-by-section review of the click-through document (Mark:
"i don't think some of the information is clear or accurate on worlds we
have not built out yet... I want to adjust the template"), working through
all 12 sections one at a time before touching code on any of them.

Section 1 (the header) produced an immediate, decided change rather than
just a review note. Mark's example: "Bethlehem Circle" — checked directly,
this is I.9's actual `shortName`, for an entry whose academic `name` is
"Hieronymian Ascetic-Literary Christianity." The shortName evokes a real
place and circle of people; the academic name doesn't. Mark's ruling: the
relatable name belongs on the box AND at the top of the click document,
with the academic name demoted to something you get by looking closer —
"this is something that tells the story."

Checked how consistently the existing `shortName` field actually clears that
bar before assuming it was ready to lead everywhere: pulled a sample and
found it's mixed. "Bethlehem Circle" and "Azusa Street" (a place) earn it;
"Latin Pastoral," "Zurich & Geneva," "Plymouth Brethren," "Baptists" are
just compressed academic titles wearing a shortName's clothes — no
story/place/circle feel. This splits into two separable pieces: the
**display hierarchy** (mechanical, safe to do now) and the **content
quality** of shortName across up to 257 entries (real per-entry judgment
work, same shape as the A2.a shortName spot-check already closed out this
session, just against a stricter bar this time). Mark's call: make the
template change now, queue the renaming pass as its own follow-up.

**Applied**: the box already led with `shortName||name` (no change needed
there — B2/schema-v2 already had this half right). Flipped the other two
surfaces to match: the hover tooltip's primary line now reads
`shortName||name` with the academic `name` demoted to the secondary line
(recolored from gold/quoted — which read as "nickname, worth noticing" — to
muted italic, which reads as "reference info, secondary"); the click
document's `<h2>` now does the same, replacing the old `informalName`-in-
quotes secondary line (which was often just "The " + shortName, genuinely
redundant against the new hierarchy) with the academic name in the same
muted-italic treatment. `informalName` itself wasn't touched at the data
level and still feeds search.

Verified directly on two contrasting real entries, not just code-read: I.9
Bethlehem Circle (Built & Live, rich content) shows "Bethlehem Circle" bold
atop both the hover card and the click doc, "Hieronymian Ascetic-Literary
Christianity" italic/muted beneath in both places; a Pre-Survey Candidate
entry (Cyrilline/Miaphysite Egyptian Christianity, shortName "Miaphysite
Egypt") shows the identical hierarchy with no live content, confirming the
change holds for the 251-of-257 not-yet-built case Mark specifically raised,
not just the six built showcase entries. `#sheetTitle`'s id (load-bearing
for the sheet's `aria-labelledby` from the accessibility pass) is untouched.
Full harness clean (257/0/0). No census changes — `atlas-v3.html` only.

**Queued, not started**: a full-census pass rewriting `shortName` wherever
it's currently just a truncated academic title rather than a genuinely
relatable name — real per-entry work, its own future session.

Sections 2–12 of the click-doc walkthrough are still ahead.

---

## 2026-08-03 (Pass 4, accessibility 4) — Systematic accessibility audit: 2 real WCAG failures, several keyboard/screen-reader gaps, all fixed

Mark: "let's do the accessibility audit next" (the last of the four
candidates offered). Previous a11y work was per-feature and incidental
(`.node` focus-visible, reduced-motion, a stray `aria-live` here and there);
this pass read the whole page systematically — semantic structure, keyboard
reachability, screen-reader labeling, modal/dialog behavior, and measured
color contrast rather than eyeballing it — and fixed everything it found.

**Real WCAG contrast failures (measured, not guessed):**
- Light-mode `--muted` on `--bg`/`--panel`: 3.56–3.85:1, fails the 4.5:1
  normal-text minimum. This is small italic text used everywhere — dates,
  hover-card meta, sheet notes, the movement count, footer prose. Darkened
  to `#77694f` (was `#8a7a5c`): 4.55–4.93:1, passes on both backgrounds.
- Light-mode `--gold` on `--bg`: 3.29:1, same failure — used for small-caps
  section labels and every `h4` in the sheet. Darkened to `#83662a` (was
  `#a07c33`): 4.58–4.95:1. Dark mode's `--muted`/`--gold` were already
  passing (5.55–7.72:1) and left untouched.
- **The more serious one**: `.node.live{color:#fff}` was hardcoded white
  regardless of theme, but dark mode's family-color palette (`FAM[].cd`) is
  deliberately light/pastel — built for thread-stroke legibility against a
  dark canvas, not as a solid fill with white text on top. Measured white
  text against all 13 dark-mode family hues: 1.77–2.36:1, nowhere close to
  passing, and confirmed visually (screenshotted a live node in dark mode —
  genuinely hard to read). This hits the SIX "Built & Live" nodes
  specifically — the ones a visitor can actually enter conversation with,
  arguably the most important boxes on the whole map. Added a `--live-text`
  custom property (white in light mode, the dark theme's own `--bg` value
  in dark mode) and a matching `liveTextColor()` JS helper for the SVG
  status-icon fill drawn in `drawArt()`, which had the identical hardcoded-
  white bug. Verified: 7.1–9.9:1 across all 13 hues both ways.

**Keyboard / screen-reader gaps found and fixed:**
- No `<h1>` anywhere on the page — added one (visually hidden via `.sr-only`,
  doesn't touch the deliberately tight header layout).
- No `<main>` landmark — wrapped the controls+map+atlas-footer (the page's
  actual unique content) in `<main id="main">`; the site chrome header/
  global-footer stay outside it.
- No skip link. First attempt at one used a local inline `.skip-link` CSS
  rule — then discovered `assets/style.css` **already defines this exact
  pattern site-wide** (`href="#main"` + `<main id="main">`, present on
  index.html and about.html) and my local rule was conflicting with it in
  the cascade (caught by testing the actual computed position, not assuming
  the CSS I wrote was the CSS that rendered). Deleted the local override,
  matched the established `<main id="main">` + "Skip to content" wording
  instead of inventing a one-off variant.
- `#legend`/`#streamlegend` had no group-level label for screen readers
  tabbing through ~20 unlabeled buttons — added `role="group"
  aria-label="..."` to each.
- `#cnt` (the "N of 257 movements" count) had no `aria-live` — filtering
  changed it silently for screen-reader users even though sighted users see
  it update. Added `aria-live="polite"`.
- `#rail` era-jump buttons relied on `title` alone (unreliable for screen
  readers, invisible until hover) for a numeral-only button label ("III") —
  added a full `aria-label` ("Jump to Era III: ...").
- Decorative SVG icons in the header controls and the "Reading the marks"
  footer box weren't marked `aria-hidden="true"` — inconsistent behavior
  across screen readers when redundant icons sit next to their own text
  label. Marked all of them.
- The `#tray` "Remove" buttons had a generic `aria-label="Remove"` with no
  indication of what — made it name-specific.
- **The sheet (`#sheet`, the full-entry document) had no modal semantics at
  all**: no `role="dialog"`/`aria-modal`, no `aria-labelledby`, focus never
  moved into it on open or back to the trigger on close, no Escape key, no
  focus trap, and — worse — it stayed in the normal Tab order even while
  visually closed and off-screen, so keyboard users tabbing through the page
  would hit an invisible close button and act buttons that did nothing
  visible. Fixed with the `inert` attribute (toggled on open/close — removes
  the closed sheet from both the tab order and the accessibility tree in one
  step), `role="dialog" aria-modal="true" aria-labelledby="sheetTitle"
  tabindex="-1"`, focus moved to the sheet container on open and back to the
  triggering node on close, Escape-to-close, and a basic Tab/Shift+Tab focus
  trap cycling through the sheet's own buttons and links.
- The "Continues from/as" and "Traditions that shaped it" links inside the
  sheet (`<b data-jump="...">`) looked clickable (underlined, cursor:pointer)
  but had no `tabindex` — keyboard users literally could not reach them, a
  mouse-only dead end for real content. Added `tabindex="0" role="link"`
  plus a matching keydown handler (Enter/Space), reusing the same jump logic
  as the click handler instead of duplicating it.
- Added explicit `:focus-visible` outlines (matching `.node`'s own treatment)
  to legend/stream/rail/control buttons and the sheet's interactive elements,
  rather than relying on each browser's unstyled default outline against
  this theme's custom button chrome.

**Deliberately left alone:** the hover tooltip (`#tip`) still only triggers
on mouse pointerover, not keyboard focus — considered adding `aria-live` to
announce it, but that solves nothing for keyboard users (it still never
fires on focus) and would add noise for anyone using a mouse alongside a
screen reader. Keyboard users get the FULL entry directly via Enter/Space
without the lighter preview step, which is a reasonable, honest tradeoff,
not a blocking gap — left as documented, not silently accepted.

Every fix verified directly in a real browser, not assumed from reading the
code: computed contrast ratios recalculated post-fix, a live node
screenshotted in dark mode before/after (visibly the difference), the sheet
opened/closed via simulated keyboard interaction confirming inert toggling,
focus-in/focus-out/focus-trap-wrap all in the correct place, Escape closing
it, and the jump links' tabindex/role. Full harness clean (257/0/0, no JS
errors). No census changes — `atlas-v3.html` only.

This closes out all four accessibility candidates from the original offer
(search aliases, glossary, deep-links, audit) — the Church in History map
now has real keyboard/screen-reader coverage for its core interaction paths,
not just its newest features.

---

## 2026-08-03 (Pass 4, accessibility 3) — Shareable deep-links: search + built + lanes + streams now round-trip through the URL

Mark: "let's do the shareable deep-links next" (the third of the four
accessibility candidates offered). A specific view — a search term, the
built-worlds toggle, particular lanes off, particular streams spotlighted —
previously lived only in page state; closing the tab lost it, and there was
no way to hand someone else the exact same view.

Read the four state variables (`QF`/`QRaw`, `builtOnly`, `laneOff`,
`streamOn`) from `location.search` once at boot, before any of them take
their normal empty defaults, then write them back via `history.replaceState`
(not `pushState` — a filter tweak shouldn't spam browser back-button history)
after every state-changing action: search input, built-toggle click, a lane
button, a category button, a stream button. Empty state produces a bare URL
with no stray `?` — verified directly, not assumed. Added a "Copy link"
button next to Built worlds for discoverability, since otherwise the only
signal is the address bar quietly changing, which most people won't notice
enough to think to copy it.

Deliberately scoped to the four things this offer named: search, lanes,
streams, built-toggle. Theme and scroll position are NOT part of the URL —
display preference, not "what is this view showing," and out of scope for
what was asked. Search is stored as the raw typed text (`QRaw`, e.g.
preserves "LDS" casing) rather than the normalized/lowercased matching
string, so a shared link reads naturally in the address bar and re-normalizes
on load the same way fresh typing does.

Verified end-to-end in a real browser, not just unit-style: set a compound
state (search "coptic" + built-toggle on + Non-Nicene lane off + Oriental
Orthodox and Baptist streams both on), confirmed the generated URL encodes
all four correctly, confirmed the Copy-link button actually writes that URL
to the clipboard, then loaded a FRESH page directly from that URL and
confirmed every piece restored exactly — search box text, built-toggle
visual state, the lane button's off state, both stream buttons' on state,
and the resulting match count. Full harness clean (257/0/0, no JS errors on
either the state-setting page or the fresh reload). No census changes —
`atlas-v3.html` only.

---

## 2026-08-03 (Pass 4, accessibility 2) — Categories & streams glossary added to the footer

Mark: "let's do the streams/categories glossary next" (the second of the four
accessibility candidates offered). The toggle labels use real vocabulary a
first-time visitor won't already know — "Dispensational / Bible-Institute,"
"Post-Evangelical Ferment" — so the toggles themselves weren't
self-explanatory the way the icon marks already were (the existing "Reading
the marks" footer box).

Added a `desc` field to every entry in the existing `CATS` (5) and `STREAMS`
(10) arrays — one plain sentence each, matching the site's own voice — then
generate a new footer glossary block FROM those arrays at load time, rather
than writing a second, hand-kept copy of the same 15 labels. Same
single-source-of-truth discipline the whole atlas already runs on (it reads
the census live; this reads its own in-page definition arrays live) — a
future stream or category addition only needs its `desc` written once, in
the array that already drives the toggle button itself, and the glossary
picks it up automatically with no separate edit.

Category descriptions clarify the two vaguest groupings specifically: "Other"
(what it actually bundles — pre-lane origins, Syriac East & Asia, Africa,
Cross-Family) and "Outside" (states plainly that Non-Nicene traditions are
included on the map, marked as outside the floor, not hidden). Stream
descriptions are one sentence each, written to be readable without already
knowing the term (e.g. Hesychast/Philokalia: "The contemplative prayer
tradition running from Byzantine monasticism through Mount Athos to the
Russian startsy" rather than assuming the reader already knows what
hesychasm is).

Verified in a real browser at both breakpoints: desktop renders as a clean
two-column definition list; the existing mobile media query pattern (matched
to the lane-legend wrap fix from earlier this pass) collapses it to single-
column term-over-definition under 700px, confirmed by screenshot rather than
assumed. Full harness clean (257/0/0, no JS errors). No census changes —
`atlas-v3.html` only.

---

## 2026-08-03 (Pass 4, accessibility 1) — Plain-language search aliases shipped; two real bugs caught and fixed before shipping

Mark, after agreeing to hold Era 10 for Fable next week: "what else can we do
to make the Church in History map more accessible (easy to use, various forms
of searchability, easy categorizations, etc.)." Offered four candidate
directions (search aliases, streams/category glossary, shareable deep-links,
a11y audit); picked plain-language search aliases — the map still spoke in
academic census vocabulary, so someone who only knows "I grew up Baptist" or
"I'm non-denominational" had to already know the map's own naming to find
themselves. The same problem named at the very start of this build ("the
challenge is the participant has to know what it is they are entering to
choose it"), now showing up in search specifically.

Two honest, grounded fixes rather than one big rewrite:

1. **Widened the search haystack** to include `relationsSummary` and
   `floorNote` — fields the live page's search wasn't reading at all. A lot
   of real denominational language already lives there (e.g. "Book of
   Mormon" only appears in VIII.14's floorNote, nowhere else) — this
   surfaces already-written content, invents nothing. Verified directly:
   searching "coptic" went from 5 to 6 matches, a real entry the old search
   was blind to.
2. **A small curated alias table**, each target checked by direct census
   query before being added, not guessed: LDS/Mormon → VIII.14; JW →
   VIII.15; Adventist → VIII.10 (the census's own shortName is "Adventism" —
   "adventist" doesn't substring-match "adventism", a real naming-suffix
   gap); Amish/Mennonite/Hutterite → VI.3 (confirmed zero hits anywhere in
   the census's own text despite VI.3 being the right entry); Episcopal(ian)
   → the Anglican/C of E chain (VI.4, VII.20, VIII.30, VIII.5); Trappist →
   IV.1 Cistercian Monasticism; non-denominational → IX.30 Megachurch &
   Seeker Movement; "born again" → the revivalist/evangelical-identity
   cluster (VII.6, VIII.2, IX.24). Deliberately did NOT alias fundamentalist,
   liberal/mainline Protestant, or social gospel to some nearby entry — those
   genuinely have no row yet (the already-logged Era 10 gap), and pointing
   the alias at the nearest unrelated thing would misrepresent what the map
   actually says, the same honesty rule that's governed streams since batch 1.

**Two real bugs found by testing before shipping, not after:**
- "lds" initially returned 23 unrelated matches — a 3-letter alias term is
  also a plain substring of ordinary words in the widened haystack ("worlds,"
  "molds," etc.), so the generic text search drowned the alias out. Fixed by
  making an EXACT match to a short alias term exclusive (alias results only,
  bypassing the generic substring search for that query) while a partial/
  still-typing match keeps the normal OR-with-text-search behavior — so
  results still widen naturally as someone keeps typing.
- "born again" was first built as a query-expansion ("search as if this said
  evangelical") rather than a fixed entry list — but `_fam.lbl` ("Protestant
  & Evangelical") sits in every lane-6 entry's own haystack, so the
  expansion inherited that whole lane's noise: 60 matches, not a real
  "find yourself" result. Replaced with a specific, curated 3-entry id list
  instead of a text expansion — same lesson as the first bug: an alias
  should point at verified content, not at a search term whose own breadth
  hasn't been checked.

Verified all eight aliases return exact, correct, tightly-scoped results
after the fixes; re-ran the full harness clean (257/0/0, no JS errors, no
overlaps). No census changes this pass — search-only, `atlas-v3.html`.

---

## 2026-08-03 (Pass 4, streams build 4) — Mark's real objection: modern expressions were being left standalone. Three more streams found and shipped by tracing existing chains forward, not by adding rows

Mark, on the previous entry's conclusion: "so this is a real problem, because
the modern expressions are deeply influenced by historical streams, they are
not stand alone." Correct, and it exposed a gap in HOW the previous batches
were built, not just a missing-data gap: batch 2's sweep checked each entry's
own relationsSummary for a named parent, but stopped at single-hop lookups —
it never asked "does anything ELSE explicitly cite an entry I've already
tagged?" the way batch 1 traced continuesAs chains multi-hop. That missed
real, explicit, already-written connective tissue.

Re-swept by building a citation graph from every `(atlasId)` reference inside
relationsSummary/why text (the census's own way of naming a specific
ancestor, distinct from vague self-description like "evangelical dissent" or
"evangelical pragmatism" that doesn't name one), then walking it forward from
what was already tagged. Found three more genuine streams, all with the same
explicit-citation discipline as the first two batches:

- **Anglican / Church of England** (5: VI.4, VII.20, VIII.30, VIII.5, IX.32) —
  a clean continuesAs institutional spine (VI.4 → VII.20 → VIII.30, the same
  identity-succession kind already used in batch 2's Waldensian chain) plus
  VIII.5 Oxford Movement's explicit two-way "renewal-inside" relation with
  VIII.30, plus IX.32 Narrative-Kingdom Renewal's own stated heritage
  ("heirs of Anglican scholarship (VIII.5 line)"). This is the stream VI.4 was
  excluded FROM Reformed/Calvinist for in batch 2 (its continuesAs identity is
  Anglican, Reformed was only formative influence) — that exclusion is what
  made this its own stream rather than folding into Reformed.
- **Dispensational / Bible-Institute** (3: VIII.23, VIII.24, IX.29) — IX.29's
  own text names both ancestors by ID directly: "Child of Plymouth Brethren
  teaching (VIII.23) carried through the Bible-institute tradition (VIII.24)."
- **Post-Evangelical Ferment** (3: IX.28, IX.30, IX.31) — IX.31's own text
  names both siblings by ID: "Child of IX.30's and broader evangelicalism's
  crises; kin of IX.28's questions a generation later." All-modern (no
  pre-1900 entry), which is fine — a stream doesn't need ancient roots, just
  genuine textual connection; this one directly answers "not standalone" for
  its own era even though it doesn't reach back further.

**What this does NOT fix, and said plainly rather than papered over:** several
modern entries genuinely have no traceable ancestor in the census's own text —
IX.24 Lausanne-Era Global Evangelicalism cites nothing and is cited by
nothing; VIII.23's own origin is "evangelical dissent" with no ID attached;
VIII.25's only citation (from IX.32) is real but singular, one link short of
its own 2-box bar, so it stays untagged rather than forced into Anglican
where it doesn't really belong (VIII.25 isn't Anglican-specific). This is the
SAME underlying problem as the previously-logged Fundamentalism/Social-Gospel/
liberal-theology gap, just one layer further downstream: not only are some
whole traditions missing rows, some existing rows' own relationsSummary text
doesn't yet name a specific historical ancestor even where a real one likely
exists. Both are Track A writing gaps, not something the streams feature can
manufacture without inventing a link the census doesn't actually make — doing
that would violate the same honesty bar ("checked against actual content, not
just name-matching") this whole feature has run on since batch 1.

11 new entries tagged (0 overlap with prior batches, confirmed before
writing); 91 unique entries now carry at least one stream tag across 10
streams total. Verified: each new stream's solo count matches exactly (5/3/3),
and — specifically re-testing the exact failure mode from batch 2's toggle
bug — all 10 streams active simultaneously gives exactly 91 (the true
union), full reset returns cleanly to 257/no-filtering. Full harness clean
(257/0/0). Same append pattern, same 1-space JSON indent, `STREAMS` array in
atlas-v3.html extended from 7 to 10 — no UI logic changes needed, confirming
the spotlight/composition mechanics built in batch 1 continue to generalize
without modification.

---

## 2026-08-03 (Pass 4, streams build 3) — Two remaining candidates checked, neither built: Fundamentalist/Liberal/Evangelical (no data yet) and Pentecostal/Charismatic (already covered)

Mark: "let's do those next too" (the two remaining named candidates from the
original scoping conversation). Checked both against the live census before
writing anything, same discipline as the first two batches — both turned out
to be non-starters, for two different reasons, and nothing was built:

- **Fundamentalist vs. Liberal/Mainline vs. Evangelical**: this isn't a
  streams-tagging gap, it's a data gap already on record. The Era 9 gate
  conversation (2026-08-03, logged in `Design/StepZero-Eras/
  CiC_Step0_Era9_V1_0.md`) found and Mark-mandated three connected E10
  candidates — Fundamentalism, the Social Gospel, and liberal/neo-orthodox
  academic theology (Schleiermacher through Barth/neo-orthodoxy to Tillich/
  Bultmann) — **none of which have a row anywhere in the census**. A stream
  needs at least two existing entries to connect; there's nothing to tag
  until those entries exist. Building them is real Track A work (source
  survey, Section A/B screening, adversarial review, Mark gate) that belongs
  to the Era 10 Step 0 run already queued, not to the streams feature. Asked
  Mark whether to start that Era 10 mini-run now or hold; no answer came
  back, so left it untouched rather than guess at scope for a bigger,
  separate body of work — this stays open for a future session.
- **Pentecostal/Charismatic as its own stream, distinct from the
  Wesleyan/Holiness/Pentecostal stream already shipped**: checked and it
  doesn't hold up as separate. The only "Charismatic" content in the census
  is IX.7 (Catholic Lay Renewal Traditions, which bundles Catholic Worker,
  Focolare, Charismatic Renewal, and L'Arche together), and its own
  relationsSummary says "Children of the long Catholic renewal line" — no
  textual link to IX.1 Azusa or the Pentecostal family at all. Tagging it in
  would have been a name-match ("Charismatic Renewal" is literally in its
  title) rather than a content-match, exactly what Mark's bar rules out.
  Nothing else in the census names the 1960s-70s charismatic movement
  distinctly from classical Pentecostalism. Not built; the existing
  Wesleyan/Holiness/Pentecostal stream already covers everything the census
  actually connects.

No census or UI changes this pass — a negative result is still worth
recording so this doesn't get re-researched from scratch later.

---

## 2026-08-03 (Pass 4, streams build 2) — Next batch shipped: Reformed/Calvinist, Wesleyan/Holiness/Pentecostal, Baptist, Anabaptist/Believers-Church — plus a real multi-select toggle bug found and fixed

Mark: "let's do the next batch of streams." No saved research-agent report to
work from this round (the earlier candidate list — Calvinist/Reformed,
Arminian/Wesleyan, Anabaptist/believers-church, Pentecostal/Charismatic,
Fundamentalist/Liberal/Evangelical — only ever lived in conversation), so
went straight to the census: pulled every Protestant & Evangelical / Global
Revival & Pentecostal lane entry plus targeted keyword sweeps, read each
candidate's actual relationsSummary/why/floorNote text, and built four lists
from what the census itself explicitly claims (parent-of/child-of language,
continuesAs chains, explicit self-naming) rather than genre/name matching.

**Real findings that changed the shape of the streams from the naive
candidate list:**
- The proposed "Arminian/Wesleyan" pairing doesn't hold up — nothing in the
  census textually links the Remonstrants (VI.26) to Wesley/Methodism (VII.5);
  that would have been theology-matching, not lineage, so it was dropped.
  VI.26 stays tagged Reformed instead (explicitly "the era's sharpest
  intra-Reformed contest" — an argument inside the Reformed world, not a
  separate lineage).
- VII.16 Baptists' own relationsSummary explicitly denies Anabaptist descent
  ("Anabaptist-resembling convictions arrived at largely independently —
  contested scholarly line"), so Baptist and Anabaptist/Believers-Church were
  built as two separate, non-overlapping streams rather than one.
- Traced the Waldensian identity chain forward through continuesAs (IV.8 → V.16
  → VI.10) to confirm all three belong in Reformed together — VI.10's own text
  ("joins the Reformed tradition in 1532") is where the merger actually
  happens; IV.8 and V.16 are the same continuing institution before that point.
- VI.4 English Reformation named "Reformed influences" as formative but its own
  continuesAs chain runs to the Anglican line (VII.20), not the Puritan/
  dissenting one — kept out of Reformed on the project's own influence-vs-
  identity distinction (edges/prose describe influence; continuesAs describes
  identity; this project already draws that line for succession spines, and
  it applies here too).
- VIII.7 (the multi-nation missions entry, Serampore/Carey included) is
  explicitly parented by FOUR traditions at once (Pietist, Moravian, Methodist,
  Catholic) plus a named Baptist/Carey connection from VII.16's own text — too
  diffuse to honestly belong to any single stream; left untagged rather than
  force-fit.
- VII.4 Moravian Church at Herrnhut demonstrably shaped Methodism ("decisive
  influence on Wesley," confirmed both directions) but that's influence, not
  membership in the same lineage cluster — excluded on the same principle as
  the VIII.7 call.
- Two genuine dual-memberships, same pattern as VII.24 in the first batch:
  VIII.3 Stone-Campbell Restoration (explicit "Child of the Awakening +
  Presbyterian line" — tagged both Reformed and Wesleyan/Holiness/Pentecostal)
  and VIII.1 Black Church in America (explicit triple-named parentage
  including both VII.16's Baptist line and VII.5's Methodist line — tagged
  both Baptist and Wesleyan/Holiness/Pentecostal).
- Anabaptist/Believers-Church is a thin, honestly-flagged case: only 2 entries
  clear the bar (VI.3 The Anabaptist Movements; VII.3 Radical Pietism & the
  Brethren, whose own text says it sits "between Pietism and Anabaptism").
  Included because it does meet Mark's stated bar (2+ boxes, genuine content,
  not name-matching) — but it's the thinnest stream shipped so far, worth
  revisiting if more entries surface later.

**Final counts** (32 unique entries, 34 tag-assignments counting the two
duals): Reformed/Calvinist 14 (IV.8, V.16, VI.2, VI.5, VI.6, VI.8, VI.10,
VI.26, VII.6, VII.22, VII.26, VIII.3, VIII.50, IX.6 — IX.6 kept despite being
partly Lutheran too, since "Reformed" is one of its two explicitly named
constituent lines and no Lutheran stream exists yet to hold it instead);
Wesleyan/Holiness/Pentecostal 13 (VII.5, VII.10, VIII.1, VIII.2, VIII.3,
VIII.4, VIII.6, VIII.34, IX.1, IX.2, IX.4, IX.11, IX.15); Baptist 5 (VII.16,
VIII.1, VIII.35, VIII.51, IX.12); Anabaptist/Believers-Church 2 (VI.3, VII.3).

**A real bug found and fixed during verification, not before shipping:**
testing single-stream toggles gave correct counts (14/13/5/2, matching the
census tags exactly), but activating a SECOND stream at the same time blew
the count up to 203 nodes instead of the expected union (26). Root cause:
`streamActive()` used an `&&`-chain that can short-circuit to `undefined`
rather than `false` for untagged entries, and `Element.classList.toggle(cls,
force)` treats an explicit `undefined` `force` as "argument omitted" — i.e.
a genuine flip — not as `force=false`. So the first toggle call (from the
all-on default) happened to look right by coincidence, but the second call
flipped every already-correct node back the wrong way. Traced by comparing a
direct in-browser evaluation of `streamActive()` (which read correctly, 26)
against the actual DOM class state (203) to isolate the mismatch to specific
untagged nodes, then instrumented `applyStreamToggle()` directly to catch the
`act===undefined` case and its inconsistent effect depending on the class's
prior state — that inconsistency (same falsy input, opposite class-state
outcome depending on what was already there) is the signature of a flip bug,
not a logic bug in the streamActive predicate itself. Fixed by forcing a real
boolean at the source (`!!(...)`) rather than patching every call site.
Re-verified: single counts unchanged (14/13/5/2), two-stream union correct
(26 = 14+13−1 shared), three-stream union correct (30 = 14+13+5−2 shared),
full reset returns to 257/no-filtering cleanly. This bug would not have been
caught by the first batch's testing, since batch 1's three streams never
overlapped and nothing there ever exercised two-active-streams-at-once.

Full harness clean (257/0/0) before and after the fix. Same `streams[]`
append pattern as batch 1 (no existing tags touched, `JSON.stringify(...,
null, 1)` preserving the census's 1-space indent), same UI (`STREAMS` array
in atlas-v3.html extended from 3 to 7 entries, no other UI changes needed —
the spotlight/composition mechanics built in batch 1 already generalized).

---

## 2026-08-03 (Pass 4, streams build) — First three lineage streams shipped: Oriental Orthodox, Hesychast/Philokalia, Eastern Catholic/Uniate

Mark's call after seeing the research agent's full candidate report: "start with
those three." Before writing any code, independently re-derived the exact entry
list for each stream directly against the live census (not the agent's prose),
resolving three edge cases the agent's report didn't settle cleanly:

- **Included II.14 Caucasian Albania in Oriental Orthodox** despite the agent
  grouping it as peripheral — its own relationsSummary states it was "absorbed
  into the Armenian catholicosate after 705," an unambiguous lineage link.
- **Excluded II.11 / III.18 / V.18 Nubia** from Oriental Orthodox — II.11's own
  relationsSummary explicitly says Nubia sat under "both rival communions'
  missions at once," i.e. deliberately ambiguous per the census's own record,
  not a clean membership.
- **VII.24 tagged with BOTH `oriental-orthodox` and `eastern-catholic-uniate`**
  — its own floorNote states a genuinely dual identity ("miaphysite communion +
  the 1742 Catholic line inside one story"), not a transcription error.

Final counts, all independently verified against relationsSummary/floorNote text
before tagging: Oriental Orthodox 28 entries, Hesychast/Philokalia 11 entries
(no exclusions — every candidate had strong explicit chain language), Eastern
Catholic/Uniate 9 entries + VII.24's dual tag. 48 unique census entries touched.

**Schema**: new `streams: [...]` array field on qualifying movement records in
`world-census.json` (schemaVersion untouched — additive, backwards-compatible,
same pattern as `laneOrder` already driving lanes). Re-wrote the file with
`JSON.stringify(..., null, 1)` to match the census's existing 1-space-per-level
indent convention — first attempt used 2-space indent and produced a 23,000-line
noise diff; caught before committing, reverted, redone to a clean ~220-line diff.

**UI**: a third independent toggle tier in `atlas-v3.html`, `#streamlegend`, below
the lane/category legend. Opt-in spotlight model per Mark's own framing
("highlighting a stream of boxes") — default OFF, multi-select, activating any
stream fades every node/thread/tail not in an active stream. Reuses the lane
toggle's fade-value convention (opacity .13 nodes / .05 art / .08 threads / 0
labels) so streams compose with lane filtering, search, and the built-worlds
toggle by simple independent dimming — no new combination logic needed, any
active filter can dim a box, none un-dims one. Also surfaced stream membership
in the click-through document (a small labeled line next to the tradition-family
line) so the connection is legible in words, not just the highlight.

Verified via the Playwright harness (0 overlap groups, 0 JS errors, all existing
smoke checks pass) plus new targeted checks: Oriental-Orthodox-only toggle lights
exactly 28 nodes, adding Hesychast/Philokalia brings it to 39 (28+11, confirming
the two sets are disjoint as designed), toggling both off clears `streamfiltering`
cleanly. Screenshots confirm the spotlight reads as connected chains threading
down through the eras, at both 1280px desktop and 390px mobile (legend wraps to
its own row, same touch-target sizing as the lane legend).

Doctrinal-practice filters (women-in-leadership fully/mostly/not, elder
plurality, governance structure) remain explicitly out of scope — a separate
future feature per Mark's own scoping call, not touched here.

---

## 2026-08-03 (Pass 4, post-category-toggle) — Streams tier scoped: lineage now, doctrinal-practice filters deferred as a separate future feature

Working through what a third UI tier ("streams," under the new
Theme→Lane structure) should actually contain, Mark identified that
Catholic's internal diversity is mostly institutional (religious orders
under one hierarchy) while Protestant's is mostly theological (positions
cutting across denominational lines) — a uniform streams model would be
dishonest to how these traditions actually work. Working through
candidates surfaced a real distinction between two different kinds of
category:

- **Lineage streams** — historically-connected clusters that grew from
  shared roots (Calvinist/Reformed vs. Arminian/Wesleyan; Fundamentalist
  vs. Liberal/Mainline vs. Evangelical; Anabaptist/believers-church;
  Pentecostal/Charismatic; the Oriental Orthodox/non-Chalcedonian family).
  Bar for inclusion (Mark): "if its highlighting a single box then its
  not helping, if it is highlighting a stream of boxes then it is
  valuable" — must genuinely connect 2+ existing entries, checked against
  actual content, not just name-matching. A first name-pattern check
  already shows Calvinist/Reformed connecting 4 entries and Arminian/
  Wesleyan connecting 2; most named Catholic religious orders (Dominican,
  Carthusian, Humiliati, Benedictine) are each currently just ONE entry
  and would NOT clear this bar — only Franciscan and Carmelite (2 entries
  each) currently would. Also surfaced: no Jesuit entry exists at all —
  a real gap, same shape as the fundamentalism/Social Gospel misses found
  earlier this session.
- **Doctrinal-practice filters** — cross-cutting practice attributes that
  could apply to almost any entry regardless of historical connection
  (women in leadership — refined from a blunt complementarian/egalitarian
  label, which is American-evangelical vocabulary most traditions
  wouldn't self-apply, to an observable three-level practice scale:
  fully/mostly/not; plurality-of-elders vs. single-pastor governance;
  congregational vs. hierarchical/institutional polity). Different
  research bar than lineage streams (honest-assessment confidence per
  entry, not box-count) and different architecture (a filterable
  attribute, not a lineage cluster).

**Scope decision**: build lineage streams now (next: a proper content
survey, not name-matching, checking all 257 entries for genuine 2+-box
clusters). **Doctrinal-practice filters are deferred as their own,
separate future feature** — not mixed into this pass.

---

## 2026-08-03 (Pass 4, post-lane-toggle 3) — Legend organized into 5 major categories over the existing 13 lanes

Mark: "organize the lanes into major lanes (catholic, orthodox,
protestant, other, outside, then lanes under those catagories. most users
will think in those terms." Clarified scope first (legend/toggle UI only,
vs. restructuring the chart's actual 13-lane rendering) — Mark confirmed
the former: "the chart itself keeps its current 13 colors and toggle,
its just an organizing meta category."

**Mapping** (judgment calls named, not silently decided): Catholic =
Latin West; Orthodox = Greek East + Caucasus (Armenian is technically
Oriental not Eastern Orthodox, grouped here for general-audience
legibility); Protestant = Protestant & Evangelical + Global Revival &
Pentecostal (Pentecostalism sometimes treated as its own branch,
grouped under Protestant here); Other = Origin, Syriac East & Asia,
Africa, Cross-Family; Outside = Non-Nicene Traditions. The three bridge
lanes attach to their first-listed parent's category (Latin/Prot→
Catholic, Greek/Latin→Orthodox, Syriac/Prot→Other) rather than being
duplicated under both parents.

Built a `CATS` array (5 groups, each listing member lane keys + attached
bridges) driving the legend's HTML structure (`.lanegroup` divs, each with
a bold `catbtn` header + its member/bridge lane buttons) and a
category-level click handler: clicking a header toggles ALL its member
lanes together (all-on → all off; anything off → all on), with a genuine
tri-state visual (fully on / `.mixed` / fully off) reflecting the actual
aggregate state of its members. Verified directly in a real browser:
clicking "Orthodox" correctly toggles both Greek East and Caucasus
together; the attached Greek/Latin bridge correctly stays on via its OR
logic (Latin West, its other parent, still on); re-enabling just Greek
East individually correctly flips the category header to the mixed state
rather than falsely showing fully-on or fully-off. Full harness clean
(257/0/0) both before and after.

Chart rendering, colors, and the underlying 13-lane data model are
completely untouched — this is purely a legend/controls reorganization.

---

## 2026-08-03 (Pass 4, post-lane-toggle 2) — Status chip row replaced with one "Built worlds" toggle

Mark: "remove the toggle and search function of the build status... leave
just one toggle, built worlds - This would fade everything not currently
built." Removed the four-way status chip group (Open/Planned/Under
review/Outside the base, plus the "All" reset) and `m.statusWord` from
the search haystack — replaced with a single toggle button using the same
on/off mechanism the search box already had (folded into the existing
`applyFilter()` as a boolean rather than building a third parallel
system, since search-text and built-only are the same kind of filter
dimension; lanes stayed their own independent system since that's a
genuinely orthogonal axis).

Verified directly: default off shows all 257 with no dimming; toggled on
correctly isolates exactly the 6 Built & Live entries (matches
`meta.liveCount`); composes correctly with search (searching "coptic"
while Built-worlds is on correctly returns 0 — none of the 6 live worlds,
all Phase-One entries, are Coptic-related, confirmed by checking the live
roster directly rather than assuming); real mobile touch tap confirmed
working (30px target, no layout issues, the earlier lane-legend wrap fix
left this row uncrowded). `Design/tools/shoot.mjs` updated to test the new
`#builtToggle` instead of the removed chip selector. Full harness clean
(257/0/0).

---

## 2026-08-03 (Pass 4, post-lane-toggle) — Mobile check found and fixed a real gap: 8 of 13 lanes were unreachable

Mark: "try it out on mobile." Tested with real touch emulation (Playwright
mobile context: 390×844, `hasTouch`, iOS Safari UA), not just a narrow
desktop viewport. Found a genuine problem: the legend's existing
`overflow-x:auto` (fine when it was a passive color key) left only ~5 of
13 lane buttons visible before running off the right edge of the screen —
the rest were reachable only by scrolling a thin, easy-to-miss strip
sideways. Touch targets also measured just 16px tall, well under normal
touch-target guidance. The dim/highlight rendering itself was correct
where reachable; discoverability was the real gap.

**Fixed**, not just reported: added a `max-width:699.9px` rule (matching
the existing mobile breakpoint already used elsewhere in this file) that
wraps the legend into multiple rows instead of horizontal scroll, and
raises button height to 30px. Verified directly: legend no longer
overflows (`scrollWidth === clientWidth`), wraps to 4 rows, all 13 buttons
now 30px tall, and a real touch tap on the previously-unreachable LAST
button (Non-Nicene) correctly toggled it and dimmed its two entries on the
chart. Full harness re-run clean (257/0/0) after the fix.

---

## 2026-08-03 (Pass 4, post-A4) — New feature: lane toggles on the legend

Mark: "add a toggle feature to the lanes... default toggled on... multiple
on/off at the same time... keep 1/2 lanes connected to both, so if either
or both are on the 1/2 is on." Built directly in `atlas-v3.html` (not a
Blueprint increment — a new post-B5 feature):

- The 13 legend swatches became real `<button>` elements (keyboard-
  focusable, `aria-pressed`), click-toggling a `laneOff` Set. Default empty
  — all 13 on, zero visual change until something's actually toggled
  (matches the existing calm-at-rest pattern from B4).
- Multi-select confirmed: independent lanes toggle on/off in any
  combination, verified directly (Syriac East + Africa off together,
  Latin West untouched).
- **Bridge lanes (the three `.5` families) are not independently
  clickable — their state is COMPUTED as OR of their two named parents**,
  exactly as asked: on if either or both parents are on, off only when
  both are off. Verified directly in a real browser: toggling one parent
  off leaves the bridge on; toggling both off turns the bridge off; toggling
  either parent back on restores it. Bridge buttons carry a `title`
  explaining which two families they follow, since they're visually
  present but not independently interactive.
- Reused the existing dim/highlight visual language (the same opacity
  values B4's search/status filtering already established) via a new,
  independent `lanefiltering`/`lane-on` class pair — composes with the
  existing search/status-chip filter system rather than colliding with it
  (different marker classes, different body class).
- **Incidental fix, same edit**: the window-resize handler only ever
  called `layout()`, silently dropping any active search/status filter on
  resize (pre-existing, unrelated to this feature, found while touching
  the same line). Now calls `layout(); applyLaneToggle(); applyFilter();`
  together — lane-toggle state confirmed surviving a resize directly.

Self-verified: full harness clean (257/0/0), plus targeted interactive
tests for default state, single-toggle, both-bridge-logic branches,
multi-select, and resize survival — all confirmed in a real headless
browser, not just asserted.

---

## 2026-08-03 (Pass 4, post-A4) — Lane rename: "General" → "Cross-Family"

Mark asked how many color-coded lanes exist (13; broken down by count),
then what the single-entry "General" lane was (IX.18, Progressive
Christianity — the census's only entry deliberately not assigned to one
family, per its own why-text: "the project's own methodology refuses to
judge it as a category"). "General" read as a leftover bucket ("didn't fit
anywhere") when the truth is closer to "assigning it anywhere would have
been dishonest." Mark: "cross-family, apply it" — mirrors the existing
bridge-lane naming logic (a bridge spans two families; this spans all of
them). Updated both the atlas's `FAM` array label and the census entry's
own `laneLabel` field. Validator 0/0, harness clean (257/0/0).

---

## 2026-08-03 (Pass 4) — A4 CLOSED: the succession-spine walk complete, four chains standing

Walked the refreshed candidate list pair by pair with Mark (recommended
lean + reasoning each time, per his established format). Six new
`continuesAs` writes landed, all validated 0/0 as applied, full harness
clean throughout (257/0/0):

- **II.7 → III.5** (Merovingian → Carolingian: dynastic transition, no
  rupture)
- **III.5 → IV.18** (Carolingian → Gregorian Reform: the post-Carolingian
  "iron century" disclosed as a gap, not a break)
- **III.6 → IV.6** (Iconophile → Athonite/Comnenian monasticism: post-
  Iconoclasm reorganization, not a rupture)
- **VIII.11 → IX.22** (Optina → the Russian New Martyrs/Catacomb Church:
  1917 drove the same tradition underground, didn't replace it)
- **VIII.29 → IX.23** (the Catholic institutional spine's live end: Vatican
  II is a council of the church, not a break from it)

The last two are written early into not-yet-run Era 10, same shape as the
already-standing VIII.13→IX.10 precedent — to be ratified (or revisited)
when Era 10's own Step 0 run happens.

**Three pairs walked and deliberately left unlinked**, each for a
distinct, real reason under the institutional-continuity convention: I.8
→ II.7 and I.6 → II.5 (different KIND of thing, not the same institution
narrowing — empire-wide pastoral tradition vs. one region; imperial
church vs. a monastic movement); V.4 → VI.17 (a monastic-theological
current absorbed into a much larger, differently-constituted governing
structure at a real rupture point, the 1453 conquest).

**Four complete chains now stand**, spanning up to eight straight eras:
- Catholic institutional: `II.7 → III.5 → IV.18 → V.14 → VI.22 → VII.19 →
  VIII.29 → IX.23` (Merovingian Gaul to the post-Vatican-II parish, seven
  links, c.480 to present)
- Orthodox monastic: `III.6 → IV.6 → V.4` (Iconophile to Hesychast/
  Palamite, three links)
- Orthodox parish/millet: `VI.17 → VII.18 → VIII.28` (Ottoman-era to the
  national churches, three links — already standing before this walk)
- Orthodox renewal: `VII.8 → VIII.11 → IX.22` (Paisius/Philokalia to the
  Catacomb Church, three links)

Prep doc (`CiC_Atlas_Succession_Spines_Candidates_2026-08-02.md`) and the
Blueprint's A4 row both updated to CLOSED.

---

## 2026-08-03 (Pass 4, A4 walk interlude 2) — NEW BACKLOG ITEM: the influence-edge sweep; one concrete edge added now (Augustine → Calvin)

Mid-A4-walk, Mark reframed the underlying question: "did the first
theology and approach directly influence the second, then it's a line
connection even if it's not a direct flow. i think calvinism was directly
influenced by augustine." Correct and important, and distinct from A4's
own question — `continuesAs` means identity (the same institution
continuing); real, documented, direct theological influence with NO
institutional continuity is what edges (type "transmitted to"/"formed")
already exist for. Checked the specific example: **zero edges existed
anywhere from I.8 (Latin Pastoral-Congregational Christianity, Augustine's
own world) — a real, well-documented, currently-invisible gap.**

**Scope decision**: this is a different, larger task than A4 (not bounded
to a succession spine — any two entries could in principle have a missing
influence line) and could be substantial. Mark: "a) keep A4 narrow, log
the edge sweep for later." **The Augustine → Calvin edge itself added now**
(census: 20 → 21 edges) since it was already confirmed and concrete —
`transmitted to`, Documented confidence, citing Calvin's explicit
dependence on Augustine's anti-Pelagian writings for total depravity,
unconditional election, and irresistible grace. Validator 0/0, harness
clean (257/0/0).

**Next action, queued**: a systematic influence-edge completeness sweep —
likely its own task brief (same pattern as the A3 status/why-field
backlogs) given the potential scope, probably a Fable/Track-A job given
it requires real historical judgment about what counts as "direct," not
mechanical writing.

---

## 2026-08-03 (Pass 4, A4 walk interlude) — González completeness check confirms and sharpens the fundamentalism/Social Gospel gap: liberal/neo-orthodox academic theology is the same cluster's third piece

Mark, mid-A4-walk: "as a check, take our list of movements and compare it
to j gonzolasas list" (Justo González's *The Story of Christianity*, one
of the six reference works this whole program cites). WebFetch was blocked
(403) on both archive.org and Google Books, so the sweep ran on a real,
partial search-verified chapter list for Volume 1 plus general reference
knowledge for Volume 2, clearly held to that standard rather than
overclaimed as a verbatim scrape — then checked systematically against
all 257 census entries.

**Result: the census holds up well against González, often more granular
than his own single-narrative text** — Donatism, Arianism/Homoian,
Cappadocians, Crusades, Avignon, Anabaptists, the English Reformation,
Puritans, Methodism, 19th-c. missions, Pentecostalism, Pietism, the
Confessing Church, Vatican II (IX.23), and liberation theology (IX.8,
under its lived name — base communities — not its academic one) are all
covered. Deism and the Thirty Years War checked and correctly absent (not
Christian traditions in the census's own sense — an event and a
philosophical current, not a row).

**One real, significant finding**: the academic liberal-Protestant
theological tradition has no row anywhere — Schleiermacher, historical-
critical scholarship as a movement, Barth/neo-orthodoxy, Tillich and
Bultmann's existentialist theology. Checked carefully, zero hits.
**Folded into the Era 9 doc's existing fundamentalism/Social Gospel
forward-flag rather than logged as a new, separate gap** — Mark: "yes,
fold it in." All three are one story: the institutional (fundamentalism,
Social Gospel) and intellectual (liberal/neo-orthodox theology) sides of
the same fundamentalist-modernist rupture, currently invisible in the
census between 1906 and 1974, feeding directly into what IX.18
"Progressive Christianity" now calls itself contemporary-only. Updated
directly in `CiC_Step0_Era9_V1_0.md` (header + the post-gate forward-flags
section) so the A1.E10 sweep surveys the cluster as one connected
question, not three independent candidates.

---

## 2026-08-03 (Pass 4 cont'd 9) — NEW STANDING RULE: the institutional-continuity convention (A4 prep refresh)

Opened the A4 succession-spine walk (Mark: "let's work on A4") using the
prepared candidate doc (`CiC_Atlas_Succession_Spines_Candidates_2026-08-02.md`)
— found it five eras stale (written before Eras 5–9 froze) and refreshed it
against the live census before presenting anything. That refresh surfaced a
real pattern across every succession decision this program has made so
far, consistent without anyone naming it as a rule until now. **Mark:
"yes, log it as a standing rule."**

**The institutional-continuity convention**: identity `continuesAs` chains
follow a communion's own governing institution — the church-proper,
parish, or see that carries formal continuity — even across large gaps,
renamings, or region shifts, AS LONG AS the identity argument itself holds
(same governing body, same communion, no rupture). Devotional, lay-piety,
and monastic-renewal CURRENTS inside that same tradition — real,
often deeply connected, but not the institution itself — stay prose-only
(relationsSummary / exemplar-succession language), never identity, even
when the family resemblance is close.

**This wasn't invented today — it's what every prior gate has actually
done, independently, without being named:**
- **REMOVED, at the Era 6 gate**: V.10 (Late-Medieval Lay Parish Piety) →
  VI.12 (Tridentine Parish Renewal) — Mark's own record states the
  identity link was pulled ("43-year gap and region jump") and replaced
  with prose exemplar-succession. V.10 is a lay-devotional current;
  VI.12 sits on the institutional line instead.
- **RULED, at the Era 8/9 seam**: VIII.12 (Kollyvades) ↔ VIII.28 — sibling/
  renewal relation, explicitly not identity, carried forward unchanged.
  VIII.12 is a monastic-renewal current, not the millet church itself.
- **BUILT, gate by gate, without anyone stepping back to see it as one
  spine**: the Catholic institutional line now runs unbroken IV.18 (Greg-
  orian Reform) → V.14 (Avignon–Lateran V) → VI.22 (Tridentine Church) →
  VII.19 (Ancien Régime) → VIII.29 (Long 19th Century) — five straight
  eras, each link written at its own era's gate for its own reasons, that
  turn out to form one continuous governing-church spine. Likewise the
  Orthodox parish/millet line: VI.17 (Ottomans) → VII.18 (Second Act) →
  VIII.28 (National Churches).
- Meanwhile the RENEWAL currents inside these same traditions stay
  correctly un-chained to each other across time (Optina, Paisius/
  Philokalia, the Kollyvades, Hesychasm) — real kinship, prose only.

**Applies going forward**: A1.E10 and A1.R12 both use this rule without
re-litigating it; A4's remaining walk (below) applies it to the pairs
still genuinely open.

---

## 2026-08-03 (Pass 4 cont'd 8) — A2.a CLOSED: all 8 shortName spot-check calls resolved one at a time

Mark: "let work on 2a" — worked the review table's 8 flagged judgment
calls one at a time (recommended option + real alternatives + why for
each, per Mark's own established format from the B4/B5.g naming rounds).
Discovered along the way that the table's own header was stale — it said
"awaiting spot-check before these enter world-census.json," but the
Blueprint's own A2.a row already said "applied to census 2026-08-02"; all
257 entries already carry live shortName/informalName values. So this
was a genuine spot-check of already-live public data, not a pre-launch
review.

**Outcomes — 2 changed, 6 confirmed as originally proposed:**
- **IX.11**: "World Pentecostalism" → **"Global Pentecostal"** — keeps the
  geographic specificity that distinguishes this entry (the Global
  South's Pentecostal growth specifically) rather than the broader, less
  precise original.
- **VIII.27**: "Indian Revivals" → **"Kerala & NE India"** — Mark caught a
  real ambiguity risk ("could be understood as American indian") that
  this thread's own first-pass alternatives had missed; the region-explicit
  fix also turned out more geographically accurate than a "South Asia"
  option floated in discussion (the entry's region is entirely within
  India — Kerala and the NE hills — not South Asia broadly, which would
  have overclaimed territory the entry doesn't cover).
- **IX.16, IX.18, IX.21, II.4, IX.10, VIII.15**: confirmed as-is, each
  with a stated reason on the record (see the review table's per-item
  resolution notes).

Each change applied directly, validated (0/0), committed and pushed
individually as it was decided — not batched. Review table and Blueprint
A2.a row both updated to CLOSED.

---

## 2026-08-03 (Pass 4 cont'd 7) — why-field backlog CLOSED (97/97); a self-caused formatting bug found and fixed; one finding re-confirmed with a sharper citation

Second managed Opus agent, same pattern as the statusDescription pass: task
brief (`CiC_Atlas_V3_A3_WhyField_Backlog_Task_2026-08-03.md`) written first
(the `why` field is a different register than `statusDescription` — makes
the case for inclusion, not a status report; split 69 pure-boilerplate /
28-with-real-content-needing-surgical-edit), agent ran it, this thread
independently re-verified before committing.

**97/97 written.** Diff exactly 97/97 line changes; a mechanical check
confirmed 0 non-`why` lines touched. Validator 0/0 (re-checked
independently). Detection query re-run independently: 0 remaining
stale-and-Frozen; Era 10's 27 correctly untouched (genuinely still true
there). Harness re-run independently: 257/0/0. Spot-read five entries the
agent flagged as its least-confident cases (III.11, VII.11, II.4, IV.15,
VIII.10) directly — all specific, honest about thin evidence rather than
padded, and the two previously-flagged stale claims (IV.15's "silent
since 622," "Continuation of II.10") are correctly not repeated anywhere
in the new text.

**Anti-duplication check, independently re-run**: max shared word-run
between any entry's `why` and its own `statusDescription`, across all 257
— **0**. (The agent's self-report claimed the same; verified rather than
trusted.)

**IV.15's stale relationsSummary — same finding as the prior pass, now
with a sharper citation.** Independently confirmed: `III.20` (Georgian
Revival — Tao-Klarjeti and Athos, 780–1000, era 4) carries
`continuesAs: "the-georgian-golden-age"` — i.e. **III.20 is IV.15's actual
identity predecessor by the census's own chain**, not II.10. Still not
fixed (Frozen-adjacent text touch, Mark's call whenever this entry is next
opened — same posture as before).

**A real bug found in MY OWN work from earlier today, fixed directly.**
The agent flagged missing sentence separators in several `relationsSummary`
fields (e.g. VI.10: "...without losing its own memory Named line (Era 9
Freeze)..." — no period between the original text and my appended clause).
Traced to the Era 9 Freeze application script run earlier this session
(Q7/Q8 ripple appends) — I concatenated `relationsSummary + ' ...'`
without checking the original text ended in punctuation. **10 entries
affected: VI.10, VII.5, VII.6, VII.7, VII.16, VIII.5, VIII.11, VIII.12,
VIII.22, VIII.27.** Fixed directly in this pass (inserted the missing
period at each junction, content otherwise unchanged) rather than deferred
— mechanical, no judgment call, own mistake. Validator 0/0 after the fix;
0 remaining instances on re-scan.

**Harness baseline note**: `searchCopticMatches` moved 4→5 — IV.9's new
`why` accurately mentions "the Coptic patriarchate" (matches its own
`relationsSummary`'s "formal dependence on the Coptic patriarchate"), so
the search now correctly surfaces it. A correct consequence of real
content, not a regression — noting it since it's a changed recorded
number in this program's own verification baseline.

**Also flagged, not fixed** — VIII.10's `statusDescription` is notably
thinner than its Era 9 siblings (a one-clause register note rather than
the full "Reviewed at the gate, tiered..." paragraph the rest got); may be
deliberate given its contested register status, may not be. Left for
inspection, not resolved either way.

---

## 2026-08-03 (Pass 4 cont'd 6) — A3 status-description backlog CLOSED (96/96); two new findings logged, not fixed

Mark: "you can launch this in your own thread and manage it" — an Opus
agent ran the task brief (`CiC_Atlas_V3_A3_StatusDescription_Backlog_Task_
2026-08-03.md`) against the live census, era by era; this thread reviewed
its work independently before committing (diff scope, validator, harness,
and direct spot-reads of five written entries) rather than trusting its
self-report blind.

**96 of 96 `statusDescription` fields written**, each grounded in that
entry's own statusWord/floorNote/relationsSummary/dateRationale plus its
era's Frozen Step 0 doc — Era 3 (11), 4 (12), 5 (13), 6 (10), 7 (18), 8
(13), 9 (19). Diff is exactly 96 insertions/96 deletions, one line each —
no incidental reformatting. Validator 0/0 (re-checked independently);
detection query re-run independently: zero stale-and-Frozen remain; the 27
in genuinely-unrun Era 10 correctly untouched. Full harness independently
re-run: 257 nodes, 0 overlaps, 0 JS errors. Spot-read five entries directly
(II.5, IV.5, IV.15, VIII.8, VIII.12) — specific, grounded, correct register,
no padding on thin records (IV.5 stayed one honest sentence rather than
being inflated).

**Two genuine findings surfaced and deliberately left untouched, per the
brief's own discipline (flag, don't silently resolve):**

1. **The `why` field carries the identical staleness bug — 97 entries**
   (the same 96, minus none, plus VIII.10 Adventism, whose
   `statusDescription` was already fine but whose `why` still says "This
   era's Step 0 hasn't run"). This is the MORE visible half of the original
   bug — the click-document prints `why` immediately below
   `statusDescription`, under "About this world," so right now a viewer
   reads a correct paragraph followed by a contradictory one on 97
   entries. **Same shape, same fix pattern, not yet started.**
2. **IV.15 (Georgian Golden Age) carries a stale `relationsSummary`**:
   "Continuation of II.10 - restores the Georgian lane, silent since 622"
   — both halves are now wrong. The Era 4 gate seated **III.20 Georgian
   Revival — Tao-Klarjeti and Athos (780–1000)** directly between II.10 and
   IV.15 (1000–1245); the lane was not silent, and III.20 is the actual
   intervening link. Verified independently (III.20 confirmed on file at
   those exact dates). The new `statusDescription` was written without
   repeating either stale claim. This is the same shape as the IX.20
   stale-relations flag already on record from the Era 9 gate (Decision-
   Log, Era 9 entry) — a single Frozen-adjacent text touch, Mark's to make
   whenever this entry is next opened, not urgent.

**Next action, Mark's call**: launch the `why`-field twin fix the same
way (new Opus agent, same discipline) — the task brief pattern is proven
and reusable; would need only a short addendum swapping the target field
and its detection string.

Mark asked why entries showed "Step 0 hasn't run yet" and got a real answer,
not a design one. Root cause: `atlas-v3.html`'s click-document template
computed its `eraState` note from a hardcoded `m.era<=2` cutoff — any era
above 2 always said "has not yet run," regardless of the census's own
`eras[]` array correctly recording eras 3–9 as Frozen. A dead giveaway was
sitting in the code itself: `const deepDone=false; /* flips per era as A1
Freezes land */` — a hook that was clearly meant to be wired up and never
was. **Fixed**: `eraState` now reads the era's actual `stepStatus` text
(`/FROZEN/` match) instead of a hardcoded number. Verified directly in a
real browser against three cases — a Frozen Era 8 entry, a Phase-One Era 1
entry, and a genuinely-not-yet-run Era 10 entry — all three now read
correctly.

**Fixing it surfaced a bigger, previously-vague item, now precisely
quantified**: 96 of 257 entries (37%) carry a `statusDescription` field
that is *entirely* the boilerplate sentence "The survey for this era has
not yet run. No verdict exists — and none is implied." — even in Frozen
eras, where it now sits directly beside the corrected note and visibly
contradicts it. This isn't new scope; it matches "the A3 status-field
harmonization backlog" already logged repeatedly as "now six eras deep"
without a number attached — this is that number. NOT touched (real census
content, not a template bug; the census-content discipline this whole
program runs on applies here too). Presented to Mark as two honest paths —
(1) a fast template-level mitigation that suppresses the boilerplate line
when its era is Frozen, changing no census data, or (2) writing real
per-entry status prose across the 96, which is Track A content work at the
same weight as a Step 0 run — **awaiting his call, logged as open.**

---

## 2026-08-03 (Pass 4 cont'd 4) — B5.g SHIPPED: the public name is "Church in History," nav label "Map"

The naming arrived through a real one-at-a-time process with Mark, not a
single pick — worth recording the path since the reasoning is as much the
decision as the final words:

1. Started from "Atlas" (already the working name) — Mark: doesn't quite
   fit, "invokes pages of maps."
2. Tried visual-metaphor names (Tapestry, River, Scroll, Chart) — Mark:
   Tapestry "isn't bad but not descriptive enough."
3. Mark reframed the whole brief: **"its the story of the church, gods
   faithfulness, christian movements, moving through time"** — a
   theological claim, not a visual one. Explored Story/Ebenezer/His
   Story/Witnesses/salvation-history language against this.
4. Mark raised the real constraint that cut through the poetry: **"the
   challenge is the participant has to know what it is they are entering
   to choose it."** Resolved by splitting the job — a plain, legible NAV
   label vs. a fuller PAGE TITLE — rather than picking one word to do both.
5. Landed on "Interactive Timeline of the Church," then narrowed the
   adjective (interactive over scrolling/dynamic, per Mark's own legibility
   test — "dynamic" is the vaguest, "scrolling" carries "doomscrolling"
   baggage and only names one of several interactions).
6. **A real correction from Mark mid-stream**: my "7 movements excluded"
   answer undercounted — recomputed and the honest number is **39 of 257
   (register + contested + excluded + outside-scope)**, including exactly
   what Mark named from memory (LDS, and I.23 Homoian/"Arian"
   Christianity — the Creed's own historical target). This didn't break
   "Church" as the word; Mark's "Church" already meant the fuller story,
   arguments and all — the glossary/icons carry the honesty regardless.
7. "Church" confirmed BECAUSE it echoes **Church in Conversation** (the
   org name) — not a separate metaphor.
8. "Through" → **"in"** — completes the echo with "Church *in*
   Conversation" (same preposition) and is the more accurate theological
   word: God's faithfulness enacted *in* real history, not the church
   passing *through* a neutral corridor. (Also independently the title of
   a well-known church-history textbook, Kuiper's — Mark confirmed that
   wasn't the reference, the org-name echo was.)
9. **Branding rule applied**: no "The" before "Church," matching how
   "Church in Conversation" itself takes no article.
10. Nav label: **"Map"** over "Scrolling Map" — matches the single-word
    nav register, and is more accurate than "Timeline" ever was (the
    visualization has two real axes: time running down, region/family
    lanes running across) — plus real precedent already sitting in the
    project's own naming (this folder has been "Atlas-World-Map" since
    before the rebuild).

**Locked: page title "Church in History"; nav label "Map."** Shipped this
pass — see the SHIPPED entry below for the execution record.

---

## 2026-08-03 (Pass 4 cont'd 3.5) — B5.g EXECUTED: ship flip complete

- `cic-website/atlas.html` and `cic-website/world-atlas.html` rewritten as
  minimal redirect stubs (`<meta http-equiv="refresh">` + `rel="canonical"`
  + a plain fallback link) into `atlas-v3.html` — the old Story and Wall
  Chart/Research Table content is retired from live traffic but preserved
  in git history, not deleted.
- `atlas-v3.html`: `<title>`, meta description, self-nav label/href, and
  the stale "178 movements" search placeholder (→ 257) all updated.
- All 6 outer pages (`index`, `about`, `whats-next`, `tour`,
  `pilot-feedback`, `support` — the last one found only in this pass's own
  sweep, missed by the earlier B5.g inventory) — nav label "Atlas" → "Map",
  every `href="atlas.html"` → `href="atlas-v3.html"`.
- Stale body-copy mentions of the retired name fixed for real accuracy,
  not just cosmetics: `index.html`'s "Explore the Timeline" button →
  "Explore the Map"; "Read more in the Atlas" → "Read more in Church in
  History"; three explanatory paragraphs in `whats-next.html` that named
  "the Atlas" directly; two internal code comments in `index.html`.
- **Self-verified**: full harness clean (257 nodes, 0 overlaps, 0 JS
  errors); both redirects confirmed firing correctly in a real headless
  browser (final URL + title both land on the new page); all 6 outer
  pages' nav confirmed pointing at `atlas-v3.html` with the "Map" label.
- Blueprint B5.g row marked SHIPPED.

---

## 2026-08-03 (Pass 4 cont'd 3) — B4 BUILT FOR REAL: arrival ticks + label-on-trace live in atlas-v3.html

Presented B4 one-at-a-time (Mark: "lets go one at a time with recomended
option and alternatives and why") via a real choice with a stated lead lean
(ship baseline) plus a fourth path ("build the real thing instead" —
arrival-ticks/label-on-trace, what B4's own recipe actually asked for, which
the three cosmetic variants didn't attempt). **Mark chose to build the real
thing.**

Implemented directly in `atlas-v3.html` (not a scratch variant this time —
this is the shipped decision):
- Landing dot → landing crossbar (`.tdot` circle → line), calm at rest,
  bolder on trace; same class name kept so `trace()`/`untrace()` needed no
  rework.
- New `.thread-label` text element per edge: the relationship type in words
  (`e.type`), invisible at rest, appears on trace, with a stroke-halo for
  legibility over crossing lines in both themes. Directly serves the
  honesty invariant (confidence/relationship always in words).
- Base thread weight/color unchanged (baseline, not variant B or C).

Self-verified: full 257-entry harness (0 overlaps, 0 JS errors) + a
targeted screenshot on a real edge (Wittenberg → Anabaptists, "argued
against") confirming both elements render and toggle correctly. B4 CLOSED.

---

## 2026-08-03 (Pass 4 cont'd 2) — A3 CONFIRMED; B5.g naming resolved as a low-risk default, ready to execute

Mark asked "what's next" without yet answering B4's lean or B5.g's name.
Closed one more genuinely automatic item and de-risked the other:

- **A3 CONFIRMED.** The icon SVGs were already Mark-approved (B1/R11); the
  only thing actually pending was formalizing the status→icon mapping table
  as a paper trail. Checked it against all three places `atlas-v3.html`
  computes it (`ST()`, the click-document logic, `stGroupOf()` for
  search/filter) — all three agree. Written as
  `Design/CiC_Atlas_V3_A3_StatusTaxonomy_Mapping_2026-08-03.md` and closed;
  nothing in the running app changes.
- **B5.g naming, checked against the record.** The Design Plan's phrase
  "resolves the 'Choose a Tradition' collision" turned out to name a
  DIFFERENT, already-tracked open item: that collision is between the live
  `cic-poc` app's `WorldSelector.tsx` heading and the unbuilt Prototype B
  search-first selector (Decision-Log, 2026-08-02 entry, item 2) — a
  `cic-poc`/in-app naming question, not the public website atlas page. B5.g
  only needs a name that doesn't ALSO collide with "Choose a Tradition,"
  which is a much lower bar. The nav already says "Atlas" everywhere
  (`index.html`, `tour.html`, etc.) and `atlas-v3.html`'s own `<title>` is
  already "The Atlas — Church in Conversation." Proposed as a B0-style
  default: **keep "Atlas"** as the public name — no collision, no new
  decision required, ready to execute the moment Mark confirms (or doesn't
  object).

---

## 2026-08-03 (Pass 4 cont'd) — B0 CONFIRMED; B4 real variant package sent; B5.g prep drafted

Mark: "follow your recommendations," delegating the B0/B4 read from the prior
turn.

- **B0 CONFIRMED.** Closed directly — all three residuals (screen-anchored
  families, accepted peak-density spill, live-hue-off-map) are already the
  live `atlas-v3.html` behavior, just verified clean against the 257-entry
  census. Freeze doc updated.
- **B4**: rather than unilaterally rubber-stamp a visual-taste gate that's
  explicitly Mark's, built the missing piece — R12 turned out to be one
  resolved treatment, not the variant-comparison sheet B4's recipe calls
  for. Built THREE real, working variants (not static mockups): baseline,
  bolder stroke (2.5→3.1 resting / 3.6→4.4 hot), family-tinted thread color
  (uniform gold → `famColor` of the edge's origin family). Filed as R14.
  Self-verified: zero JS errors, identical resting/tracing mechanics across
  all three. Honest finding: the deltas are subtle in a static screenshot —
  consistent with the "calm at rest" brief, not a mockup failure. Arrival
  ticks and label-on-trace flagged as NOT built (real per-edge SVG work,
  not a CSS variant) rather than faked. **Stated lead lean: ship the
  baseline (A) — a thread's "family" is ambiguous for edges spanning two
  families, and tinting by origin-side-only would render a distinction the
  census data doesn't actually assert (the honesty invariant).** Package at
  `Design/CiC_Atlas_V3_R14_B4_LineWeight_Gate_2026-08-03.md`; gate queued
  for Mark's pick (A/B/C, or request real arrival-ticks/label-on-trace).
- **B5.g prep drafted** (not executed — ship flip is explicitly Mark-only
  and public-facing/hard-to-reverse): inventoried every file needing a
  link/redirect touch (`index.html`, `tour.html`, `whats-next.html`,
  `about.html`, `pilot-feedback.html` all link `atlas.html`; `atlas.html`
  and `world-atlas.html` become redirects to the new public path). Held
  for Mark's naming call (the Design Plan's own flagged "Choose a
  Tradition" collision) before any file touches.

---

## 2026-08-03 (Pass 4, model switch to Sonnet) — Track B self-verify loop closed against the 257-entry census; B0/B4 gates queued for Mark

Mark switched this thread's model to Sonnet for template/implementation work
("switch this thread to sonnet ... continue with building templates") and
asked what's next on the Blueprint for eras 1–9. Findings: `atlas-v3.html`
(B5) reads the census live (no inlined data) — the newly Frozen 257-entry,
20-edge census (eras 3–9) required NO rebuild to render; it had simply never
been verified past the 178-entry baseline. Built
`Design/tools/shoot.mjs` (the harness the Blueprint named but hadn't been
created yet: screenshots at 390/1280 × light/dark, geometric no-overlap
check on `.node` boxes, interaction smoke) and ran it:

- **257 nodes render, zero geometric overlaps across all four
  viewport/scheme combinations, zero JS errors.**
- Search "coptic" → 4 matches (was 3 at 178 entries; the Era 9 rename of
  VIII.13 plus new entries account for the growth) — verified against the
  page's real filter model (a non-hiding `.match`-class highlight + the
  `#cnt` counter text, corrected after the harness's first draft wrongly
  assumed a hide-based filter and mis-read it as "all 257 visible" — caught
  and fixed before reporting).
- "Open" chip → exactly 6 (the live-world count, unchanged, matches
  `meta.liveCount`).
- Hover card, click-document (sheet), and the 10-era jump rail all fire
  correctly.

**Two Track B gates were already built and are queued for Mark, surfaced
now rather than left silent:**
- **B0** (design base freeze) — one three-line confirmation
  (`Design/CiC_Atlas_V3_Design_Base_R10_Freeze.md`): screen-anchored
  families, accepted peak-density spill, live worlds' hue confined to
  hover/click/app.
- **B4** (line prominence) — R12 (`CiC_Atlas_V3_R12_Hover_Lines_2026-08-02.html`)
  is a SINGLE resolved treatment (stroke-width 2.5/3.6 hot, already live in
  `atlas-v3.html`), not the variant-comparison sheet the Blueprint's B4
  recipe describes (stroke weight range / family-tint vs gold / arrival
  ticks / label-on-trace) — flagged honestly rather than claimed as
  satisfied; Mark can approve the resolved treatment as-is or ask for true
  variants.

Screenshots + `report.json` on disk at `Design/tools/shots/`.

**Next action:** Mark's B0 + B4 gate decisions; then B5.g (ship flip)
becomes live; A2.a spot-check (8 flagged calls) and A3's formal taxonomy-
mapping gate remain small queued items.

---

## 2026-08-03 (Pass 3) — ERA 9 FROZEN by Mark; census 233→257; the register field's climax gate held

**Decided (Mark): "approved/yes for the era nine rulings"** — the full package
per the stated leans, after two review rounds (R1: 6 substantial incl. the
living-flag defect caught at scale across the drafts; R2: 11/12 clean, one
arithmetic residue fixed). Applied: all 24 candidates entered (the four
big-church receivers VIII.28–31, the global-South block, the U&U register
segment, the Taiping register row — its shelf ruled register over Outside-A4);
ALL FIVE register dispositions RECORDED at own-text strength (VIII.16
record-mandated and the register's FIRST A3-LED case — the machinery era 10's
register rows inherit); the criterion's sixth–ninth live applications (VIII.10
two window-specific findings, question stays on the register for era 10;
VIII.18 the first OFFICE-DEFINED c2 run, question stays genuinely open;
VIII.8 and VIII.23 CLEARED on the community limb); the register-cap convention
RULED (living register rows cap at the era boundary; story-own ends keep —
era 10's kin inherit a clean rule); VIII.17's phantom 1928 → 1906; VIII.20's
window-fill start → 1848; the VIII.26/VIII.27 present-tails segmented at 1906
(era-10 segments at the E10 gate); the VIII.13 rename; VIII.13→IX.10
RATIFIED + twelve Frozen-Era-8 continuesAs writes + VIII.49→IX.20 + four
deliberate NOT-writes (165/205/171-year gaps disclosed, not bridged); the
Black Church's three parent lines named (incl. the Methodist parent the flag
missed) + the census's 19th and 20th edges; the VII.23 and VI.25 living-flag
fixes; the 149-item sources[] landed (139-[S] debt named). Validator 0/0;
Playwright smoke 257 nodes, zero JS errors.

**Mark's hesitation, recorded with the freeze (the heart of it):** "i think
the research missed some significant movement beginnings. dispensationalism,
fundamentalism and social gospel beginnings reshaped the evangelical
landscape more than any other factors and to not have them recognized is a
problem (even if they were developing in the late 1800s)." Checked against
the census: dispensationalism IS carried (VIII.23 + IX.29 + the IX.32
counter-culture); fundamentalism and the Social Gospel are NOT — nor is the
mainline/liberal Protestant lane they jointly imply (IX.18 is contemporary-
only). All three are now **MARK-MANDATED A1.E10 candidates** (era doc
forward-flags, post-gate addition): their late-1800s beginnings (Niagara
1876/1878, Princeton inerrancy 1881; Gladden 1886, Rauschenbusch, Sheldon
1896) named as in-scope reach-backs; WWJD rides as inside content; the two
sides of the fundamentalist–modernist rupture are natural candidates for the
census's second "in tension with" edge.

**Also decided this session (usage strategy):** Fable at 97% of the weekly
window, two days in. Ruled path: freeze Era 9 on Fable now (done); interim
week's work (Track B visuals, A3 harmonization, draft-base queue) may run on
Opus/Sonnet; **Era 10 waits for next week's reset on the strongest model** —
it is the living era, the hardest, and the Mark-gated living-era protocol
addendum precedes its run. A handoff brief accompanies this freeze.

**Next action:** living-era protocol addendum (Mark-gated) → A1.E10 → A1.R12.

## 2026-08-03 (Pass 3) — ERA 8 FROZEN by Mark; census 221→233; six eras Frozen

Mark's ruling, verbatim: **"yes to all, move forward."** Applied per the
leans: all 12 candidates entered (the mandated Ottoman segment + the four
structural receivers + the bridges + the U&U register entry with its two
separate findings); the round-1800 artifact cluster replaced with honest
1815 caps; the register-cap ruling made (VII.12 →1815); **both floor
dispositions RECORDED** (VII.13 record-mandated, VII.12 proposed — the
1808 Testimony anchor); **the Antonian c2 CONTESTED-ON-RECORD** (two
limbs, Salve Antoniana cited, transmission condition named — the question
stays open with its record); nine succession writes incl. **VI.24→VII.4
identity across the hidden-seed century**; VII.8→VIII.11 ratified;
VIII.13→IX.10 banked for E9's ratification sweep; the Kollyvades seam as
proposed; the 98-item sources[] landed. Validator 233 movements, 0
errors; atlas renders 233 nodes, zero JS errors.

**Eras 3–8 are now Frozen. Census 178→233 across this run of gates.**
Next: A1.E9 (1815–1906) — the census's densest register field (the ✦/✧
remap's hardest ground), with the banked forward flags. Then the
living-era protocol gate before A1.E10, and the Eras 1–2 revalidation.

---

## 2026-08-03 (Pass 3) — A1.E8 CLEARED FOR GATE after two review rounds; Era 8 gate package presented to Mark

The Enlightenment & Awakening run (17 entries + 12 drafts) completed the
loop: Round 1 (13 substantial — the heaviest round yet: a manufactured
mandate, a mis-anchored floor disposition, a one-sided c2 run repeating
the E7 defect, a misattributed-Frozen fork, two failed recomputations, a
thrice-asserted analysis that didn't exist — + 12 cosmetic, all applied),
Round 2 (four residues fixed at close; gate-eligible per the reviewer).

- Section A: **VII.13's RECORD-MANDATED floor disposition** (its own why
  assigns it; own-confession strength; the IV.13 Joachim-precedent named
  on its c2 side) + **VII.12's PROPOSED sibling disposition** (anchored on
  the 1808 *Testimony*, honestly un-mandated) + **the Antonian c2 run
  two-limbed** (the *Salve Antoniana* cited; person-shaped vs
  community-shaped; GENUINELY CONTESTED lean; Montanism cited only as the
  un-ruled sibling) + the U&U two-thread analyses + the Quaker
  off-register-on-purpose line.
- 12 drafts (VII.18–VII.29): the mandated Ottoman segment (Jerusalem 1672
  to Gregory V's 1821 hanging), the Ancien Régime church, the Georgian
  C of E, the Synodal Russian church (Old Believers re-scoped as dissent),
  the Church of the Desert, Melkite + Utrecht + Uniate bridges, Old
  Dissent, the U&U register draft, Armenia, the Philippines segment.
- Data finds: the round-1800 six-entry artifact cluster; the four-way
  register-cap inconsistency; the second pre-gate chain write
  (VIII.13→IX.10) banked for E9's ratification sweep.
- **Nothing decided; census untouched (221, validator clean).** Nine
  questions at Mark's gate.

---

## 2026-08-02 (Pass 3) — ERA 7 FROZEN by Mark; census 212→221; five eras Frozen in one day

Mark's ruling, verbatim: **"go with recommendations on all and move
forward."** Applied per the stated leans:

- **Q2**: all 9 candidates entered — Tridentine Church (the big-church
  gap's third fix), Russian patriarchate century, Czech last century (to
  c. 1627), Ethiopia Gragn-to-Fasilides, Remonstrants/Dort, Scandinavian
  kingdoms, New Julfa, Carmelite reform ([S]-conditioned), Sulaqa schism.
  **The VI.13 split HELD** (A5-now stands; Japan's arc confirmed inside).
  Census 212→221.
- **Q3**: all dates applied — Kongo **1491** back-extension landed; VI.4
  extended to 1650 (the Stuart century absorbed); VI.6→1559; VI.16→c.
  1540; string fixes; **both straddle violations SEGMENTED at 1650**
  (VI.17, VI.19 — era-8+ receivers created at those gates); every
  alternative branch was on the record.
- **Q4 — VI.14 floor divergence FORMALLY RECORDED** (own-confession
  strength; the register's cleanest case; recension caveat carried; the
  victim-honesty line newly written into its record).
- **Q5 — VI.16 c2 recorded as GENUINELY CONTESTED** (the criterion's
  first two-limb case; question stays open with its record; Franck → A3).
- **Q6**: eight succession writes onto Frozen Era 6, named-approved, incl.
  **V.23→VI.18 direct** (same community/place/name; 82-year gap
  disclosed). NOT written: VI.24→VII.4, VI.23→VII.7 (era 8's).
- **Q7** ripples applied (Lucaris + Peć + interregnum on VI.17;
  Augustinian seedbed on VI.1; Dort named twice with VI.9's scope line).
- **Q8**: 122-item sources[] landed — the [S] verification debt (109
  items) named and carried. Draft-base queue now 5+11+10+9 across four
  eras.
- Verification: validator 221 movements, 0 errors · atlas renders 221
  nodes, zero JS errors.
- **Eras 3–7 are now Frozen. Census 178→221 in one day.** Next: A1.E8
  (1650–1815) with its banked forward flags (Roman + Anglican holes,
  VII.7/VII.4 receivers, VI.17's era-8 segment, VI.19's segments,
  VII.17/VI.13 scope seam, Old Believers at era 8, Armenian fallback
  n/a — VI.28 entered).

---

## 2026-08-02 (Pass 3) — A1.E7 CLEARED FOR GATE after two review rounds; Era 7 gate package presented to Mark

The Reformation-era run (21 entries — the largest pre-run roster yet — + 9
drafts) completed the loop: Round 1 (6 substantial — a false census-content
claim in the mandatory floor disposition, a one-sided c2 run corrected to
two-limb contested, collapsed forks, dropped [S] hedges — + 12 cosmetic,
all applied), Round 2 (three one-line residues fixed at close;
gate-eligible per the reviewer's ruling).

- Section A carries the era's two register runs, both Mark-gated: the
  **VI.14 mandatory floor disposition** (own-confession strength — the
  register's cleanest case; victim-honesty line proposed as a NEW
  addition, recension caveat carried) and the **VI.16 c2 contest** (the
  criterion's fourth live run and its first genuinely two-limb case:
  person-defined origin-shape vs real transferability counter-evidence).
- 9 drafts (VI.22–VI.30): Tridentine church (the big-church gap's third
  fix), Russian patriarchate century, Czech last century, Ethiopia's
  ordeal, Remonstrants/Dort, Scandinavian kingdoms, New Julfa, Carmelite
  reform (Teresa), the 1552 Sulaqa schism. The VI.17/VI.19
  straddle-violation segment forks and the VI.13 1491 back-extension land
  at this gate; the VI.13 split question goes to Mark.
- **Nothing decided; census untouched (212, validator clean).** Eight
  questions at Mark's gate.

---

## 2026-08-02 (Pass 3) — Open note banked for A1.E10: Mark's caution on the living era

Mark, verbatim in substance: **"we need to be careful with 10 to present. the
dynamics of a current tradition gets much more complicated. it may be ok for
the atlas, but historical rigor may be hard to define."** No decision taken;
banked so the A1.E10 run inherits it.

- Proposal on record [E]: A1.E10 runs under a **living-era protocol
  addendum**, drafted + adversarially reviewed + MARK-GATED before the run
  begins. Likely contents: A3 (interpretive fidelity) run for every entry —
  the subtest built for contemporary movements, N/A in every era so far;
  self-descriptions sourced from each tradition's own current statements,
  dated; a B1 vocabulary extension for contemporary attestation (the
  Documented/Widely Accepted ladder assumes a weathered record that does
  not exist for the living); floor/register findings phrased with
  present-tense humility (claims about living neighbors, not the dead);
  ends stay honestly open (the unsealed-tail grammar already encodes this).
- The conversation system is the era's unique methodological asset: for
  living worlds, "internal voice" can include the tradition's own present
  answer — properly framed, via the Construction Framework, never
  informal (the standing scope discipline holds).
- Era 9 (1815–1906) remains fully historical; the seam is living memory,
  not the century mark.

---

## 2026-08-02 (Pass 3) — ERA 6 FROZEN by Mark; census 202→212; four eras Frozen in one day

Mark's ruling, verbatim: **"apply your recommendations and freeze era 6."**
Applied per the stated leans, with two disclosure notes given in the same
reply, open to correction: the **III.18→V.18 succession field is WITHHELD**
(validator-forbidden under the chosen era-6 slot; the relation is V.18's
named register line), and the **IV.8→VI.10 edge is KEPT** (the retire
branch carried no lean — still open to Mark).

- **Q2**: all 10 candidates entered — the Avignon–Schism–Constance papal
  church + the Palaiologan church (both Schism-principal receivers, the
  latter with continuesAs into VI.17's 1453 start), Alpine Waldensians,
  CoE after Timur, terminal Nubia (era-6 slot), Franciscan Order era-6,
  Bosnian Church (plain candidate, debate in floorNote, c. 1230s
  standing-rule start as drafted), Armenia-to-Etchmiadzin, Maronite union
  segment, pre-Portuguese Malabar. **Kongo resolved on the E7-scope-flag
  branch — the era-6-entry branch knowingly foreclosed by this Freeze.**
  Census 202→212.
- **Q3**: dates applied w/ dateRationale (V.1 c. 1440; V.3/V.7/V.9 →1517;
  V.9 start 1368; V.11/V.12 string+1466 fixes; V.6 origin note).
- **Q4 — Lollardy person-defined check CLEARED** (its floorNote ordered
  the run); **Q5 — Observant c2 CLEARED** (third live application;
  "Savonarola alone would fail" kept verbatim in the floorNote).
- **Q6**: V.10→VI.12 reclassified exemplar-succession (field removed,
  prose carries it). **Q7**: V.6's Moravians-era error corrected in the
  census text; era-7 Unitas hole flagged.
- **Q8**: seven continuesAs writes onto Frozen Era-5 entries + V.15→VI.17
  + the Hospitallers-on-Rhodes note on IV.11 — all named-approved.
- **Q9** ripples applied (converso context on V.9 and inside V.14's
  drafted text; Georgian/Syriac named-gap registers live in the era doc).
- **Q10**: 76-item sources[] landed. Draft bases join the follow-up queue
  (now Era 3's five + Era 5's eleven + Era 6's ten).
- Verification: validator 212 movements, 0 errors · atlas renders 212
  nodes, zero JS errors · meta + era stepStatus refreshed.
- **Eras 3, 4, 5, and 6 are now Frozen. Census 178→212 in one day**, every
  ruling Mark's, every date rationaled, eight adversarial review rounds on
  file across four eras. Next: A1.E7 (1517–1650 — the Reformation era),
  research pre-staging, with its banked forward flags.

---

## 2026-08-02 (Pass 3) — A1.E6 CLEARED FOR GATE after two review rounds; Era 6 gate package presented to Mark

The Era 6 Step 0 run completed the loop: Round 1 (8 substantial — headlined
by a validator-illegal Frozen succession write caught before it could reach
the gate, plus a misattributed Freeze-record claim, five collapsed forks,
the Kongo foreclosure, and the same three dropped Era-5 flags Era 5's own
round had restored once — + 8 cosmetic, all applied), Round 2 (independent
recompute; two one-line residues fixed at close, gate-eligible per the
reviewer's ruling).

- The era carries TWO criterion runs, both drafted lean-clear and
  Mark-gated: Lollardy's person-defined check (its own floorNote ordered
  it run) and the Observant c2 question (the criterion's third live
  application; the Savonarola-alone boundary kept verbatim).
- 10 candidate drafts (V.14–V.23): the Avignon–Schism–Constance papal
  church + the Palaiologan church (both Schism principals' receivers),
  Alpine Waldensians, the Franciscan order's own era-6 story, the Bosnian
  Church with the identification debate honest, terminal Nubia (era-slot
  fork with its write-legality interaction disclosed), and four thin
  spine segments. Kongo 1491 goes to the gate as a three-branch fork with
  the dies-at-Freeze branch named.
- **Nothing decided; census untouched (202, validator clean).** Ten
  questions at Mark's gate, incl. the consolidated Frozen-writes list.

---

## 2026-08-02 (Pass 3) — ERA 5 FROZEN by Mark; census 191→202; the Schism rendered; the C2 criterion's first live clearing

Mark's ruling, verbatim: **"apply your recommendations and freeze era 5"** —
after the ten questions were presented with stated leans. All ten applied per
the recommendations; one item deliberately NOT applied: **III.1→IV.22
succession (the 375-year Church of the East gap) stays OPEN** — it was
presented as "your call" with no lean, so the recommendations ruling does not
cover it.

- **Q2**: all 11 candidates entered — both **Great Schism principals**
  (IV.17 Byzantine post-1054, IV.18 Latin Papal Church with the c. 1049
  standing-rule extension granted), Kievan Rus' to 1240, Armenian Cilicia,
  Syriac Renaissance, CoE under the Mongols (end 1317), Carmelites, Bogomil
  register continuation, Outremer, Coptic golden age ([S]-conditioned —
  named verification before any build), Humiliati. Census 191→202.
- **Q3**: the census's **first "in tension with" edge** — the Schism itself,
  IV.18→IV.17, Documented, both sides' own documents in the note, 1204
  reading carried, 1965 lifting [S]. Edges 17→18.
- **Q4**: dates applied with dateRationale (Victorines 1108–1246, Cathars
  c. 1143–1321, Joachimites 1202, Georgia 1245); **IV.9 ended 1270 and
  RENAMED "Zagwe Ethiopian Christianity"** (overlap fixed, name honest);
  IV.16 keeps 1396 — the straddle rule's letter stands.
- **Q5**: Cathar register retained; per-text finding recorded (dualism =
  Liber only; coherence debate disclosed; non-endorsement language kept).
- **Q6 — the Frozen C2 criterion's first live clearing**: Joachimite
  c2:"question" → null; the finding on the record (communally carried;
  Joachim the pen, not the resting-point). A5 status untouched.
- **Q7**: Maronites keep 1100 + origin note. **Q8**: ripples applied incl.
  the named Cluny-peak touch on Frozen III.10 (Mark's approval explicit in
  the ruling). **Q9 — succession convention ADOPTED**: continuesAs is the
  single identity carrier; six pairs landed (III.22→IV.17 · III.8→IV.19 ·
  III.16→IV.20 · III.17→IV.21 · III.13→IV.24 · III.3→IV.26); IV.8→VI.10 and
  IV.6→V.4 regularize at the A1.E6 gate. **Q10**: 96-item sources[] landed.
- Verification: validator 202 movements, 18 edges, 0 errors · atlas renders
  202 nodes, zero JS errors · meta refreshed (enforced).
- **Eras 3, 4, and 5 are now Frozen.** Census 178→202 today, all
  Mark-ruled, every date with a written rationale, every era
  double-reviewed on file. Next: A1.E6 (research pre-staging), with its
  inherited flag list (Waldensian hole, Franciscan shape, Nubia's end,
  Bosnian question, III.1→IV.22, IV.8/IV.6 regularization).

---

## 2026-08-02 (Pass 3) — A1.E5 CLEARED FOR GATE after two review rounds; Era 5 gate package presented to Mark

The Era 5 Step 0 run completed the loop: Round 1 (5 substantial — Cathar
per-text overstatement, a collapsed IV.9 fork, V.7 sweep omission, IV.24
silent window choice, 3 dropped survey flags — + 7 cosmetic, all applied),
Round 2 (independent recompute; **CLEARED FOR GATE**, one cosmetic
harmonized at close).

- The era carries the census's two heaviest standing assignments, both
  drafted and Mark-gated: the **Cathar floor disposition** (two-layer,
  per-text: dualism text-established in the Liber only; coherence debate
  disclosed) and the **first live run of the Frozen C2 criterion**
  (Joachimites — draft finding: clears, communally carried).
- 11 candidate drafts (IV.17–IV.27) headlined by both **Great Schism
  principals** + the census's **first "in tension with" edge**; register
  draft carries the Bogomils forward; [S]-conditioned Coptic golden age.
- **Nothing decided; census untouched (191, validator clean).** Ten
  questions at Mark's gate.

---

## 2026-08-02 (Pass 3) — ERA 3 FROZEN by Mark; census 187→191; the first fully closed era run

Mark's ruling, verbatim: **"apply your recommendations and freeze era 3"** —
given after a source-grounded walkthrough of the open questions (the
recommendations and their evidence are in the conversation record and the
era doc's gate block).

- **Q5**: Najran martyrs (523) routed inside II.9's story (Kaleb's
  intervention is the connection; the event is richly attested, the ongoing
  community is not) — **"pre-Islamic Arabian Christianity" flagged as a
  future completeness question** (Najran + Ghassanids + al-Hirah together).
- **Q8**: all four A5 ripples applied — II.5 region + Sinai; II.2 +
  Ghassanid patronage line; II.3 + India-inside-communion line; II.10
  "(607)"→"(609)" harmonized with the gated Dvin III end.
- **Candidates II.14–II.17 ALL entered** (Caucasian Albania T3 · Latin
  Africa under Byzantium T2 · Visigothic Iberia T2 · British-Welsh T3), each
  with gate statusWord + dateRationale. **II.16→III.9 continuesAs applied**
  per the recommendation (Mozarabic's relationsSummary already named
  post-589 Iberia as its parent).
- **FREEZE**: the 70-item sources[] landed on the 12 researched era-3
  worlds. Follow-up flagged: the five gate-added entries (II.13–II.17) have
  no source bases yet — queued as an A1.E3 addendum or A2.d item.
- Q6 (Homoian A4) stands untouched — Mark-only, no deadline.
- Verification: validator 191 movements, 0 errors · atlas-v3 renders 191
  nodes, zero JS errors.
- **Eras 3 and 4 are now both Frozen.** The atlas's census has grown
  178→191 in one day's gates, every change Mark-ruled, every date carrying
  a written rationale, every era run double-reviewed on file.

---

## 2026-08-02 (Pass 3) — ERA 4 GATE: Mark rules "yes to all" (all eight questions); census 179→187; treated as the Era 4 Freeze

Mark's ruling, verbatim: **"yes to all."** Three interpretation calls were
stated to Mark in the same reply, open to his correction: the Cluny fork
lands on the stated lead lean (**1109**); Bogomil Q4 lands on option (a);
complete-gate approval incl. Q8 is treated as the **Era 4 Freeze** (sources
landed accordingly).

- **Q1** tier statusWords applied to the 14 entries.
- **Q2** all EIGHT candidates entered: III.15 (622–843) + III.22 (843–1054)
  Byzantine split, Bagratid Armenia, Syriac under Islam, Makurian Nubia,
  Late Anglo-Saxon (793 via the approved Q3 coupling), Georgian Revival,
  post-Aksumite Ethiopia. Census 179→187.
- **Q3** all §5 dates applied with dateRationale: data-class III.7→916,
  III.8→1054 (+string), III.12→c. 650–878; III.1→845, III.2→1009,
  III.3→1013, III.4→793, III.5→751–888, III.9→1031, III.10→**1109**,
  III.11 start→849.
- **Q4** Bogomils: register retained; statusWord records the [S]-qualified
  finding (one verified witness, two from-knowledge).
- **Q5** A5/scope ripples as routed (all already carried in the entered
  drafts; Maronite origin note stays era-record-only; no-receiver flags to
  A1.E5).
- **Q6 — STANDING RULE ADOPTED**: "an entry sits in the era where its
  defining gravity-window lies, even when its start precedes the boundary."
  Covers II.3 (424), Georgia (330), IX.2 (1904), III.4 (597), III.21 (615),
  IV.6 (963), IV.15 (1000). **Closes Era 3's open Q7 and the A0-routed IX.2
  anomaly** — no date edits required; it is a placement doctrine.
- **Q7** eleven succession pairs land as continuesAs (validator allows
  same-era): imperial spine II.13→III.15→III.22; II.2→III.17; II.4→III.16;
  II.11→III.18; II.9→III.21→IV.9; II.10→III.20→IV.15; III.4→III.19;
  III.7→III.8.
- **Q8** the 79-item sources[] bases landed on the 14 era-4 entries — the
  census's first sources[] landing (Era 3's 70 still await its own Freeze).
- Verification: validator 187 movements, 0 errors · atlas-v3 renders 187
  nodes, zero JS errors.
- **Still open after this gate:** Era 3's Q5 (Najran/Himyar), Q8 (A5
  ripples), candidates II.14–II.17, Era 3 whole-era Freeze + its sources
  landing; the Homoian A4 standing question; A0.5 micro-rulings; the other
  standing gate queue (B0, B4, A2.a spot-check, B5.g, A3).

---

## 2026-08-02 (Pass 3) — A1.E4 CLEARED FOR GATE after two review rounds; Era 4 gate package presented to Mark

The Era 4 Step 0 run (`Design/StepZero-Eras/CiC_Step0_Era4_V1_0.md` + 8-draft
candidate appendix) completed the loop: Round 1 (5 substantial — false
III.7→III.8 edge claim, Bogomil evidence overstated, III.19 silent 793 start,
IV.6 sweep omission, Q3 start-anchor mislabel — + 4 cosmetic, all applied),
Round 2 (independent recompute incl. the split; **CLEARED FOR GATE**).

- **Mark's two-world steer applied mid-review** (conversation, 2026-08-02:
  "are there two worlds we can form"): the Byzantine imperial candidate split
  at 843 (Triumph of Orthodoxy) into III.15 (622–843, Heraclian &
  Iconoclast) + III.22 (843–1054, Macedonian); single-entry alternative
  preserved at the gate; imperial spine II.13→III.15→III.22 to the A4 walk.
- Headline Section A work: Bogomil floor disposition drafted at honest
  [S]-qualified strength (one verified witness, two from-knowledge) with a
  hold-for-verification option; Paulician Contested-Evidentiary stands.
- **Nothing decided; census untouched (179, validator clean).** Eight
  questions go to Mark: tier list · candidates (III.15+III.22 split headline,
  III.16–III.21) · §5 dates (3 data-class + 2 start anchors + Cluny
  1109/1049 fork) · Bogomil disposition · A5/scope ripples · start-before-era
  instances → open Q7 rule · A4 spine list · sources[] landing.

---

## 2026-08-02 (Pass 3) — Open notes banked for A1.E5: the Great Schism's principals + a live demand signal

From conversation with Mark (no decision taken; nothing changes now):

- **Completeness note for the A1.E5 run:** Era 5 carries no Byzantine
  patriarchal church entry (IV.6 is monastic only) and no Latin papal/
  Gregorian Reform entry — the two principals of the 1054 schism are both
  missing in the era that begins with it. The E5 run should propose both as
  candidate entries, plus the census's **first "in tension with" edge**
  between them (Documented; each side's own documents — Humbert's bull,
  Cerularius's synodal response), with process honesty in the entry text
  (1054 the symbolic break; 1204 what made it unhealable).
- **B4 audiences signal, real demand:** a participant asked Mark (2026-08-01)
  about the Great Schism and each side's perspective — unprompted live
  interest in exactly these two worlds and in perspective-answering as a
  feature. Carried as a B4 signal into the E5 run's Section B; also a
  future-phase world-selection signal for building the two representatives
  (representative construction stays with the Construction Framework
  methodology, never informal).
- Interim honesty: the atlas renders the schism today only as the frozen
  1054 era boundary; as a relationship it appears only when census edges
  carry it. Per-world perspectives reach participants through click-document
  sources now, and through built representatives only when those worlds are
  built.
- **Mark's scope discipline (2026-08-02, verbatim in substance):** sources
  matter because the schism's worlds must carry "not just the theological
  driver … but the lived ecosystem, internal and external" — but that depth
  is the conversation system's world-building concern (Construction
  Framework), "not for us to worry about as this is a map." The atlas thread
  stays on its task: entries, dates, edges, honest source pointers — no
  world-building, no bias toward the theological headline in source-base
  composition (B2's eight-lens ecology already encodes this).

---

## 2026-08-02 (Pass 3) — ERA 3 GATE: Mark rules Q1–Q4 YES; census updated to 179 movements

Mark's ruling, verbatim: **"1 yes, 2 yes to the byzantine church, 3 yes, 4 yes."**

- **Q1 — tier list FROZEN as proposed.** Census statusWords applied: Tier 1
  (II.1, II.2, II.3, II.5, II.6, II.7) "Researched — strong candidate"; Tier 2
  (II.4, II.8) "viable, secondary"; Tier 3 (II.9, II.10, II.11) "deferred,
  richer window later". `status` field harmonization deferred to the A3
  taxonomy gate, as the era doc proposed.
- **Q2 — the Byzantine Imperial Church (Justinianic) ENTERS the census**
  (II.13, `byzantine-imperial-church-justinianic`, 451–622, Tier 1). The
  headline completeness gap closed. **Candidates II.14–II.17 were not named:
  open, neither approved nor rejected.**
- **Q3 — Lombard extension ADOPTED**: II.12 is now "Gothic, Vandal & Lombard
  Homoian Christianity", end c. 680; floor-register status unchanged.
- **Q4 — §5 date corrections APPLIED**, each with a `dateRationale` string
  (A2.c rolling in per the blueprint): Armenia end 554 · Nubia end 652 ·
  Syriac 636 · Judean Desert 614 · Aksum 451–615 (start corrected) ·
  Georgia end 609. II.7 stays 620 (614 was noted as an alternative only).
- Verification: validator 179 movements, 0 errors · atlas-v3 renders 179
  nodes, Imperial Byzantium present, counter self-updates, zero JS errors.
- **Still open, unnamed at the gate (Frozen discipline):** Q5 Najran/Himyar ·
  Q6 Homoian A4 · Q7 start-before-era standing rule (II.3/Georgia/IX.2) ·
  Q8 A5-ripple edits · candidates II.14–II.17 · the era's whole-Freeze
  declaration (and with it §4's sources[] landing). Era 4 assembly (A1.E4)
  is unblocked and next.

---

## 2026-08-02 (Pass 3) — A1.E3 CLEARED FOR GATE after three review rounds; Era 3 gate package presented to Mark

The Era 3 Step 0 run (`Design/StepZero-Eras/CiC_Step0_Era3_V1_0.md` + candidate
appendix) completed the build-cycle loop: Round 1 (6 substantial + 6 cosmetic,
all applied), Round 2 (caught the applied sweep was still not arithmetic, the
falsified Lombard 652 surviving in Q3/§1, and a borrowed Whitby 664 on the
British-Welsh draft — all applied), Round 3 (independent recompute; **CLEARED
FOR GATE**). All three review rounds exist as files beside the document.

- Notable review-driven corrections: straddle sweep now enumerates all six
  622-boundary crossings + the c. 450 boundary-rounding exemption + all five
  candidates; Lombard extension proposes **c. 680** everywhere; British-Welsh
  candidate re-dated **c. 451–768** (Elfoddw, Welsh Roman-Easter adoption —
  Whitby 664 disowned on record as II.8's hinge, not this church's).
- Also this pass: Era 4 research fully banked ([E]) — survey (9 candidates)
  + source bases (79 items, 14 worlds, 28 [S] sub-flags); era 3+4 source-base
  JSONs moved in-repo. Era 4 assembly waits behind this gate.
- **Nothing decided; nothing touches the census.** Eight questions go to Mark:
  tier list · candidate additions (II.13–II.17) · Lombard extension c. 680 ·
  §5 date corrections (3 data-class incl. Aksum start 451) · Najran/Himyar
  routing · Homoian A4 (standing) · start-before-era standing rule (II.3 /
  Georgia / IX.2) · A5-ripple census edits. Era 3 Freezes only by Mark's
  explicit ruling.

---

## 2026-08-02 (Pass 3) — FROZEN by Mark: the ten eras (A0) and the clean Criterion 2 text (A0.5) — the era runs are unblocked

Mark's rulings, verbatim in substance: **"eras affirmed, keep 1906, freeze the
criteria as written."**

- **A0 CLOSED — all ten eras FROZEN as they stand**, 1650 and 1906 included
  (the memo's two open questions resolved by affirmation; 1906 keeps Azusa as
  the Global Church era's hinge, with the memo's checked numbers on record).
  Residual not ruled at this gate: the IX.2 anomaly (start=1904, era=10) —
  routed to the A1.E10 era run.
- **A0.5 — the §1 Criterion 2 text FROZEN as written**, including the three
  flagged drafter operationalizations ("small named set"; the own-claim
  citation rule; the Contested-Evidentiary reroute), which "as written"
  covers. Per the Frozen discipline, the reply does not freeze what it
  doesn't name: §2 placement (a/b/c), Montanism's (a)/(b) fork, and
  Novatianism's proposed reclassification remain open micro-rulings — the
  I.25/I.26 census statuses change only when Mark rules them explicitly.
- **Consequence: A1.E3–E10 are UNBLOCKED.** The per-era Step 0 runs begin
  with Era 3 (The Age of Monks and Empires, 451–622), under the Frozen
  criterion text and the affirmed era frame, per the Blueprint recipe.

---

## 2026-08-02 (Pass 3, full autonomy) — Blueprint executed through B5: the one atlas exists as a working page

Mark granted full autonomy to execute the Blueprint ("move on with full
autonomy to B5 and beyond"). Landed this stretch, each per its recipe with
the Loop Protocol:

- **A2.b** validator (`Design/tools/validate-census.mjs`) — green on every
  census edit since.
- **A2.a** shortName + informalName for all 178 (census, schemaVersion 2);
  review table with 8 flagged judgment calls queued for Mark's spot-check.
- **A0** era re-affirmation memo through TWO adversarial review rounds (both
  on disk): Round 1 found 4 substantial defects (incl. a false census-impact
  claim — 1906→1910 in fact moves 3 entries, Azusa itself among them;
  1650→1648 moves zero) — revised; Round 2 independently re-verified every
  number and CLEARED FOR GATE. Gate carries: 8 affirms, 2 questions (1650,
  1906), and the IX.2 anomaly (start=1904, era=10) for Mark's ruling.
- **A4 prep**: Catholic + Orthodox spine candidate walks with gap routing;
  framing question on record (communion vs liveliest-thread).
- **Census id fixed at source**: `imperial-and-juridical-christianity` →
  `imperial-juridical-christianity` (validator green; the two page-level fix
  maps become harmless no-ops).
- **B0** freeze doc, **B3** click document (R13) — delivered earlier in the
  stretch; **B5 BUILT**: `cic-website/atlas-v3.html` — the one atlas,
  reading the census live (no inlined data), with search + four-icon status
  chips + count, era jump rail, touch model (tap = hover card, second tap =
  document), keyboard traversal + aria labels + reduced-motion + print
  styles, tray + app hand-off generated from census ids. Verified [M]: zero
  JS errors; 178 nodes/icons; search "coptic" → 3; Open chip → exactly the
  6 live worlds; interview hand-off URL carries the corrected id. Page is
  deliberately UNLINKED — B5.g (redirects, old pages retired, public name)
  remains Mark's ship-flip gate.

---

## 2026-08-02 (Pass 2 close) — APPROVED by Mark: Rebuild Design Plan V1.0 + Build Blueprint V1.0; three scope rulings

Mark moved the thread from struggle to build-planning ("re-build design plan
first, then a blueprint for you to follow autonomously through an entire
build") with six improvement areas: (1) era re-affirmation + Step 0 per era
with deeper sourcing and a source base per world; (2) minimal box template +
four status icons; (3) standard hover template; (4) standard click document
with a revised status taxonomy; (5) more prominent influence lines; (6) the
standing design-review-modify loop. Plan drafted in plan mode, grounded in a
methodology sweep (Step 0 Methodology V1.0's Section A/B structure; the
build-cycle review discipline — review rounds as files, Frozen only by Mark;
Criterion 2's absence from codified Section A), and **approved**.

**Three scope rulings by Mark during planning:**
1. **Per-era Step 0 runs are era-level and AUTHORITATIVE** — a deliberate
   amendment of the methodology's phase-level application. Each era's run
   becomes the standing disposition record the atlas renders; release phases
   still run their own Step 0 for build selection, starting from these.
2. **Eras 1–2 revalidate only** — the Phase One Conclusion stays
   authoritative; deeper sourcing enriches and flags, never re-decides
   without his gate.
3. **Exactly 4 status icons** (house · plans · question mark · closed door)
   **in the tile, plus a page-bottom glossary in words**; finer distinctions
   (willing-to-look-deeper; border vs clearly-out Nicene) carried in words on
   hover/click, never by icon alone.

**Standing documents produced (both Approved):**
`CiC_Atlas_V3_Rebuild_Design_Plan_V1_0.md` and
`CiC_Atlas_V3_Build_Blueprint_V1_0.md` — the blueprint carries the increment
table (A0…A4, B0…B5.g), per-increment recipes, gates, the Loop Protocol, and
autonomy boundaries. Future sessions execute from the blueprint; its status
column is the build's ground truth.

**Sync-ready for System Hub:** two new Gantt tracks (Atlas V3 Data &
Methodology; Atlas V3 Product), first gates A0 era memo + B0/B1; the
era-level-authoritative amendment for the Hub's methodology record; noted
in passing [M]: L2D-System-Operations V1.2 is stale (five-world table vs the
nine-world Phase One record) — Hub's queue, not this thread's.

---

## 2026-08-02 (Pass 2, in-session) — DECIDED by Mark: founder-prophet marks come off the map; C2 pair re-evaluated under clean criteria; Step 0 criteria re-look and remap opened

Made live in conversation during the Pass 2 divergent/groan-zone session, on
Mark's own words — logged immediately so it doesn't live only in chat. Context
that prompted it: the census carries the ✦/✧ founder-prophet mark on **22 of
178 entries**, but only **2** (Montanism I.25, Novatianism I.26) carry the hard
"Excluded — Person-Defined (C2)" status; the ✧ "question to run" mark had
spread to ten ordinary Pre-Survey Candidates (Taizé & Iona, Catholic Worker,
the Chinese indigenous church, African-Initiated Churches, and more). Mark:
"they are real movements... [the single-voice screen] needs to be a part of
the explanation of why a world wasn't chosen to be built, but it's not a lane
of division... we have overdone that — it can be a primarily
single-influenced tradition but have multiple sources from other people that
could qualify, and the Bethlehem Circle could be an example of that."

**1. DECIDED — map presentation.** The ✦/✧ glyphs and "founder-prophet"
language come off every front-facing surface: legends, rows, bands, cards,
tooltips, on all three live views and in any v3 direction. The single-voice
screening survives as **point-of-reading disclosure only** — inside each
entry's click-through "why it isn't open" explanation, where the census's
`why`/`floorNote` prose already carries it. (Note for implementers: there is
no single-influence *lane* to remove — C2 entries already sit in their true
historical lanes; this is a mark-system removal, not a lane change.)
**Implementation waits for Pass 3** — Pass 2 is planning-only by Mark's
instruction; nothing on the live surfaces changes yet.

**2. DECIDED — the two hard C2 exclusions get re-evaluated under clean
criteria.** Montanism and Novatianism's "Excluded — Person-Defined (C2)"
status is not carried forward as settled; both go through the re-assessment
below. (Montanism's own census entry already records a live question in its
favor: Phrygian inscriptions may document a wider communal ecology.)

**3. DECIDED — Step 0 criteria re-look and remap.** Mark: "we are going to
re-look at the step 0 criteria and remap." The distinction that motivated it,
recorded as the seed for that re-look (draft language, not yet the criterion):
**authority resting on one person** (a movement whose own claim to legitimacy
*is* a person's revelation or standing — what C2 was written for) is a
different thing from **sourcing flowing through one pen** (a disclosed
sourcing signal, never disqualifying — the Bethlehem Circle is the built,
live precedent: primarily Jerome's pen, with Paula/Marcella/Eustochium as
multiple real qualifying voices). A movement primarily shaped by one
influence but carried by multiple qualifying communal voices, qualifies.
**Boundary honored:** the criteria revision and the per-entry remap of all 22
marked entries are Construction Framework / Step 0 methodology work — they
happen under that discipline (with the re-assessment recorded per entry), not
as a bulk edit to the census from this design thread. Until the remap runs,
the census's c2 fields stay as data (historical record of the old flagging);
they simply stop being rendered.

**Sync-ready for System Hub:** a new methodology work item exists — "Step 0
criteria re-look + 22-entry founder-prophet remap (incl. Montanism/Novatianism
re-evaluation)" — decided by Mark 2026-08-02, not yet scheduled, owner TBD
(Construction Framework side, not this thread).

**Addendum, same session — DECIDED by Mark: the v3 design parameters (the
five-property trade resolved).** Against the groan-zone statement that
one-axis scrolling + all lanes on one screen + all individuals visible +
legible names + true-scale time cannot all hold, Mark's calls, verbatim in
substance: **true-scale time goes first** (sacrificed); **lineage legibility
is untouchable**; **vertical scroll** is the one axis (lanes share the width,
all on one screen, including phone — no second scroll axis, per his earlier
in-session rule); and **the permanent screen is minimalist** — very little
text at rest, **hover reveals more, click opens a standard description
template for every world, built or not** (one uniform template skeleton for
all 178 entries: name · dates · region · lane · status word + plain
description · why open / why not · what survives · where it stands on the
Creed · relations with confidence in words · actions where live). Design
consequence recorded: with position ordering events rather than measuring
years, movements render as compact nodes rather than lifespan-length bars —
which dissolves most of the concurrency-width problem that drove Direction
1's ~4,000px and Direction 3's 10px capsules, and gives lineage threads clean
node-to-node anchors. A synthesis mockup embodying these four parameters
(vertical braid geometry + ordinal time + minimal chrome + uniform template)
was built for Mark's reaction in the same session — **convergence is checked
back with Mark before anything is treated as the final direction**; build
work remains Pass 3.

**Second addendum, same session — Mark's correction: NOT at convergence;
"still in struggle that will have some convergence and then some more
divergence." Round 1 synthesis reactions, all his words in substance:**
- **Box-and-tail wanted back.** The Round-1 synthesis reduced movements to
  compact nodes; Mark misses Prototype C / Direction 1's grammar — a box at
  the birth date with a descending tail marking the lifespan. Returns in
  Round 2 (tail placed ordinally, since true-scale time stays sacrificed).
- **Physical lanes go; color carries tradition.** "Not locked into physical
  lanes but allow horizontal overlap, staying more true to the influence
  vertical relationship than the major tradition lane… we use color to
  distinguish the high-level tradition instead of physical bound lanes."
  Layout should hug lineage (children pulled toward their influence
  parents), which also kills the empty-lane whitespace ("a huge space in the
  flow until the Reformation happens").
- **Confirmed within the struggle:** the working line itself (Braided &
  Minimal as base, yes); a `shortName` field added to the census for all 178
  entries (yes — a Pass 3 data task, one pass over the census); and **"only
  one atlas, done right"** — not Story + Wall Chart + Research Table as
  parallel surfaces; the one atlas absorbs their jobs. (What of the Research
  Table's scholar-filter role survives inside the one atlas is an open
  struggle point, not yet asked or answered.)
- **New tension this opens, deliberately unresolved:** color previously
  carried STATUS (open/chosen/deferred/excluded…); if hue now carries
  tradition family, status needs a different visual channel (fill/border
  treatment within the family hue) — and the six live worlds' personal
  representative colors (Chloe's violet, Theon's blue…) either yield to
  family hue or break the rule. Round 2 renders family-hue-for-all to make
  the tension visible; Mark has not ruled.

**Third addendum, same session — two data-model principles DECIDED by Mark
during the Rounds 5–7 layout struggle:**
- **Entries are era-scoped; a tail straddles at most ONE era boundary.**
  Mark: "worlds may straddle an era, but shouldn't be crossing three. We are
  looking at specific movements and eras, not a forever… Eras 3–5 are all
  pieces of a Catholic stream that is unbroken, but we are looking
  specifically at what is happening inside those different eras — it
  wouldn't be one Representative to cover 1,500 years." This matches the
  census's own design (continuity carried by successor entries + recorded
  edges, not by one entry's span). Visual consequence: a tail that reaches
  its straddle limit fades with a "continues" cap and the next era's own
  entry carries the stream; entries like Manichaeism (216–650, spanning four
  map eras as one bar today) render era-scoped.
- **Every tradition gets clear start AND end dates, bounded by
  gravity-force shifts.** Mark: "all traditions should have clear starting
  and ending dates and shift when significant gravity forces shift." Entry
  windows close where the movement's significant gravities/forces shift (the
  Construction Framework's own Doc_04/Doc_08 vocabulary), not at vague
  century edges. Data consequence [M]: the census carries soft ends
  ("3rd–7th c.", "400s", "1st–4th c.") that are now data debt — each needs a
  definite year with a gravity-shift rationale. This folds into the already-
  opened Step 0 re-look / remap workstream (this log, earlier today) — the
  remap now covers founder-prophet re-marking AND date-boundary
  rationalization, per entry, under methodology discipline. Visual
  consequence: every tail eventually earns a definite closing seal at a real
  gravity shift; unsealed fades should exist only at the present edge.

**Full-census scale test (Round 9), measured [M]:** the R8 design carries
all 178 movements / 10 eras at 1,760px canvas on a 1,280px desktop (990px on
a 390px phone), ~11,000px tall, zero JS errors, 152 closing seals + 26
unsealed streams (24 living traditions + 2 straddle-capped) running to the
present edge. Families extended to the full 13-lane set (Protestant, Global
Revival, three bridges, General). Visible data debt at scale: entries
without a shortName ellipsize ("Recusant English Cathol…") — the approved
shortName field is now demonstrably needed, not speculative.

**Fourth addendum — DECIDED by Mark: identity succession renders as an
unbroken stream.** "If you are looking at different tradition worlds within
an ongoing stream by identity, like the Catholic church or Orthodox church,
have the tail of the previous bounded world go into the top of the next
era's tradition world without an ending block — it continues as a new world
but ongoing church." Implemented in Round 10: the successor inherits the
predecessor's exact slot, is born on its own tail, and no seal is drawn
between them; the entry template gains "Continues from / Continues as"
lines. **New census field required: `continuesAs`** — identity succession
is a distinct relation from influence and must be carried in the data, not
hand-drawn. Round 10 shipped eleven demo pairs (Church of the East chain
×3, Coptic chain ×2 + the modern revival pair, Armenian, Aksumite,
Ethiopian, the parish stream into Trent, Paisius→Optina) — **CONFIRMED by
Mark in-session and written into `world-census.json` as `continuesAs` on
the eleven predecessor entries** (11-line diff, same minimal-edit
discipline as groundDark). The Catholic and Orthodox full spines remain
open for Mark's pair-by-pair calls. Same session, Mark caught a date
artifact the chart surfaced: Persian Church of the East (early) displays
"to 451" with no start (reading like a one-year world); data carries
start=300/end=451, with 300 an unconfirmed era-boundary estimate per the
2026-07-22 log. Candidates under the gravity rule: c. 300 (attested
communities) vs 410 (Synod of Seleucia-Ctesiphon — formal organization;
seamless with Syriac Edessa's own 410 close). Mark's call, queued for the
dates-rationalization pass. Chain gaps the exercise exposed are census-coverage findings
in their own right [M]: e.g., no Syriac-lane entry between the Silk Road
era (to c. 1000) and the Sayfo (1915), and no Latin parish entry between
Trent (to 1610) and Vatican II (1962) that carries the parish identity —
candidates for the completeness re-check already on the open list.

**Layout finding from the same struggle, on record so it isn't re-derived:**
straight never-overlapped tails with box-and-tail as one centered body have
a hard geometric floor (~contemporaries × half-a-box ≈ 1,900px+ at Era-2
density). Three of Mark's own moves dissolve it: era-scoped tails free
their space every generation; boxes may lean over a gap with an ASYMMETRIC
shoulder ("a moving to the tail") while the tail drops into a tight slot;
and a box crossing its OWN family's ribbon is not an overlap — it's the
family's river running behind its newest member (only other families'
tails must stay clear). Round 7 embodies all three: 0 cross-family
overlaps by geometric check, ~630px canvas on a 390px phone, ~1,520px on a
1,280px desktop at the slice's peak (year ~397, 20 concurrent tails) —
near one-screen, with residual spill only at peak-density rows. [M
throughout; one known 1-overlap tuning bug on record for the build phase.]

---

## 2026-08-02 — Atlas v3 first build pass: IC-10 completed across all three views; two live defects fixed; three questions held open for Mark

First construction pass of the v3 rebuild thread (branch
`claude/christian-traditions-atlas-v3-x2egp6`). Everything below was verified
against the running pages (local serve + light/dark screenshots of the Story,
Wall Chart, and Research Table), not just written. [M] throughout unless marked.

**APPLIED — IC-10 (approved era-ground palette) is now fully live, light and
dark, on every Atlas surface.** The census (`world-census.json`) gained a
`groundDark` field per era, carrying the canonical dark values from the
Brand-Assets spec (`CiC_World_Icon_and_Table_Template_Spec_V0_1.md`
§"Era-ground values", approved 2026-07-18); the existing light values were
verified byte-for-byte against that spec before touching anything. `atlas.html`
(Story) — which already had the light palette — now switches to the dark
grounds in dark mode (its dark-mode CSS previously never touched `.st-era`, so
dark readers saw the unadjusted light hex). `world-atlas.html` now renders the
per-era grounds for the first time: as full-height era columns under the Wall
Chart's timeline (lowest stacking layer, bands/edges/labels unchanged above
them) and as tinted era-header bars in the Research Table. Both read
`ground`/`groundDark` from the census — no hex value is duplicated into either
page. Verified: warm-parchment Era I → cool blue-grey Era X progression is
visibly legible at both ends of the chart, light and dark.

**FIXED — the Story view's app hand-off silently failed for one world.** The
census id `imperial-and-juridical-christianity` doesn't match the app's real
world id `imperial-juridical-christianity` (no "and"). `index.html` already
carried a `CENSUS_ID_FIX` map for exactly this; `atlas.html`'s `launch()` did
not, so interviewing/adding Marius's world from the Story view launched the app
without pre-selecting it. The same fix map is now applied in `atlas.html`'s
`launch()`. Verified: the hand-off URL now carries
`?worlds=imperial-juridical-christianity`. (Fixing the id at the source — the
census/spreadsheet — remains the better long-term fix, but touches the census
build chain; left on record rather than done quietly here.)

**FIXED — the Wall Chart's relationship lines had already drifted from the
census.** Its `EDGES` array was a second, hand-maintained copy of the edge set,
and an audit found 4 of its 17 lines no longer matched the census's reviewed
`edges` field (which the Story view renders live). The chart now derives its
edges from the census at init (id → atlasId) and the hand array is deleted.
Concretely, the chart **stopped drawing** four lines the census does not carry —
I.3→II.5 (Desert → Chalcedonian Monasticism, Judean Desert & Gaza), I.3→II.1
and I.2→II.1 (Desert/Alexandria → Cyrilline Miaphysite Egypt), IV.8→VI.2
(Waldensians → Reformed Cities) — and **started drawing** the four the census
does: I.3→III.6 (→ Iconophile Byzantine Monasticism), I.3→III.3 and I.2→III.3
(→ Coptic Christianity under Early Islam), IV.8→VI.10 (→ the
Waldensian-Reformed Union). Both versions of each claim are historically
defensible prose; the decision here is only about source of truth — the map's
own stated rule ("no relationship is drawn that the census does not carry")
now actually holds on all surfaces. **If Mark wants any of the four dropped
claims back, the move is to add them to the census `edges` field, once, not to
any page.** Note for later: Prototype C embeds a *third* hand copy of the old
6-edge Era 1–2 slice — fine for a frozen prototype, but the same drift class if
it's ever promoted.

**Small craft additions in the same pass:** desktop hover states on Story-view
rows/cards (`@media (hover:hover)` — the rows were click-only with no hover
affordance); the chart's edge-tooltip notes are now HTML-escaped.

**NOT decided here — three questions carried to Mark, per his instruction that
this thread raises them rather than resolves them:**

1. **What "messy" means / Prototype C.** Prototype C
   (`Design/CiC_World_Map_Redesign_Prototype_C_Unified_Grid_Timeline_2026-07-23.html`)
   is now actually read and describable: a single unified canvas — no
   lane-rows-by-era-columns grid — where each movement is a box pinned at its
   start date with a status-colored span bar, influence lines flow from a bar's
   underside into the influenced box, eras are full-width horizontal ground
   bands, and detail opens in a right-side sheet. Built as a 26-entry Era 1–2
   slice "proving the mechanic, not the full census." It has never been
   reviewed or ruled on. The genuine v3 question for Mark: is C's unified-grid
   mechanic the direction for the Wall Chart's replacement, a source of ideas
   to merge (its start-date-box + span-bar reading is arguably clearer than the
   current band-packing), or a dead end? [E: my read — worth a verdict before
   any wholesale chart redesign, since "messy" most plausibly names the current
   chart's band crowding at low zoom, which C's mechanic directly addresses.]
2. **The "Choose a Tradition" name collision.** The live `cic-poc` app's plain
   tile-grid heading (`WorldSelector.tsx`) and Prototype B's unbuilt
   search-first selector share the name. Any v3 work touching either needs
   Mark to pick disambiguated names first.
3. **Tier A / Tier B scope.** The record disagrees with itself: the 2026-07-22
   decision says Tiers A+B jointly ("two linked surfaces, not either/or"); the
   Gantt only ever scheduled Tier A (task 463), and the 2026-08-01 framing
   treats Tier B as unscoped. Both readings go to Mark; nothing in this pass
   touched `cic-poc`. Related dead code, on record for that decision:
   `world-atlas.html`'s `APPMODE` branch targets a `/world-map/` route that
   exists nowhere in the app — left in place, since removing or wiring it is a
   Tier B call.

**Also open (rigor):** the only external completeness review on file ran
against Census V0.2 (147 entries), not the current 178 — if "every identified
Christian tradition" is meant as a checked claim, a second pass against the
same reference works is still owed. [M: review-file coverage; the gap is a
fact, whether to spend the pass is Mark's call.]

---

## 2026-07-22 (later) — DECIDED: Story-view entries sort by start date within each lane; census gains real numeric start/end years

**Mark's observation, looking at the Story view:** the order entries appear in within
an era didn't look right; his call — "i think it should be by movement start date."
Checked the actual code first rather than assuming: entries were rendering in
whatever order they sat in the census JSON array (Atlas-ID/spreadsheet row order),
not chronologically, within each lane group.

**One real choice underneath the ask, put to Mark rather than assumed: sort within
each lane, or interleave the whole era by date regardless of lane?** Chose **within
each lane** — keeps the seven-lane architecture's deliberate grouping (ninth pass,
2026-07-16) intact and just fixes the ordering inside it, rather than dissolving lane
blocks into one date-sorted list.

**Applied:** `world-census.json` movements gained real numeric `start`/`end` year
fields (added right after the existing `dates` display string, all 178 entries,
sourced from the Wall Chart's already-verified per-entry timeline data — the exact
numbers `world-atlas.html` was already using, not a fresh guess) — so any surface can
sort or compute chronologically without parsing the display string. `atlas.html` and
`index.html` (the Story's two copies, see Integration-Notes) both updated: within
`renderLaneGroups()`, each lane's entries now sort by `start` ascending before
rendering; the "Beyond the Floor" stream (rendered separately, not through
`renderLaneGroups`) sorts the same way. Verified live for Era 2: Greek East
(325→350→360), Africa (320→330→451), and Latin West (312→370→374→382→390) all now
render in ascending chronological order within their lanes.

**Also simplified in the same motion:** `world-atlas.html`'s Wall Chart had its own
local `POS_YEARS` lookup (extracted from the old pre-consolidation embedded data,
used only because the census didn't carry numeric years yet) — now that the census
does, `POS_YEARS` was deleted and the chart reads `m.start`/`m.end` straight from the
fetched census, same as the Story. One less locally-duplicated table, not a new one.

**Next action:** none pending on this. Worth remembering if a future world's dates
get revised (e.g. a Step 0 narrows a window): the census's `start`/`end` fields now
drive both sort order and chart timeline placement, so a dates edit should update
both the display string and these two numbers together.

**Addendum, same day — Mark caught it live: "era one is not in order."** Checked
rather than assumed. Not a sort-logic bug — two of the just-added `start`/`end`
fields were themselves wrong, carried forward uncritically from the old Wall
Chart's data without checking them against each entry's own `dates` display
string. **I.1 (The House-Churches)** — display reads "70–200 CE"; the field said
start=200, end=280 (should be 70/200), which pushed the project's earliest
movement to sort *after* Ebionite and Montanism instead of first. **I.2
(Alexandrian Christianity)** — display reads "c. 150–400 CE"; the field said
190/254 (should be 150/400). Both corrected directly in `world-census.json`. A
broader audit (parsing every entry's display string for an explicit year and
diffing against the `start` field) found no other confirmed mismatches — two
remaining borderline cases, **I.12 (Persian Church of the East, "to 451")** and
**II.12 (Gothic &amp; Vandal Homoian, "to 589 / 534")**, give no explicit start year
in their own display string at all, so their current field values (era-boundary
estimates) can't be confirmed wrong either — left as-is rather than guessed at.
Re-verified live: Era 1's Origin lane now reads House-Churches (70) → Ebionite
(70) → Montanism (165) → Novatianism (251); the Wall Chart's I.1/I.2 bands now
start at the timeline's year-70 origin instead of mid-chart. **Lesson for next
time a `start`/`end` field gets touched: check it against the entry's own `dates`
string before trusting an inherited number, even one that was "already verified"
for a different purpose (positional rendering tolerates a wrong number more
quietly than a sort does).**

**Second addendum, same day — Mark checked again after the fix above and House-Churches still wasn't first.** A real, separate, pre-existing bug, not
related to the date fields at all: `renderLaneGroups()`'s lane-ordering sort used
`laneOrder||60` as its fallback for lanes with no assigned order — but the Origin
lane's own `laneOrder` is `0`, and `0` is falsy in JavaScript, so `0||60` silently
evaluated to `60`, sorting Origin as if it were near the bottom instead of first.
This shoved the whole Origin lane (House-Churches, Ebionite, Montanism,
Novatianism) down after Syriac/Africa/Latin West every time, on every era that
has an Origin-lane entry — present since this sort was first written, unrelated
to today's start/end work, just never noticed. Fixed in both `atlas.html` and
`index.html` (the Story's two copies) by switching `||60` to `??60` (nullish
coalescing, which only falls back on `null`/`undefined`, not on a legitimate
`0`). Re-verified live: Era 1 now renders Origin lane first, House-Churches
first within it.

**Third addendum, same day — DECIDED: the ordering source of truth is the Step 0
Conclusion, not each world's own later Doc_01 refinement.** Mark's correction,
precisely stated: order by "start date as stated by step 0," not "by the world's
[own] definition." The distinction is real, not pedantic — for the nine worlds
Phase One's Step 0 Conclusion (`CiC_Step0_Conclusion_FINAL_v2.docx`) originally
selected as a single comparative batch, several later got their own individual
**Doc_01 (World Identification)** document, which is free to narrow or widen
that window with world-specific research done well after Step 0 and independent
of the other eight worlds. Using each world's own Doc_01 figure for ordering
means every entry's precision (and thus its sort position) depends on how much
individual attention that one world happened to get afterward — not a fair,
consistent comparison. Read the Step 0 Conclusion's own nine-world list directly
(`.docx`, extracted via its `word/document.xml`) rather than trusting any
document that merely cites it:

| World | Step 0's own stated window |
|---|---|
| House-Churches | c. 70–200 CE |
| Alexandria | c. 190–254 CE |
| Desert Monasticism | c. 320s onward |
| Donatism | c. 312–430s |
| Cappadocian | c. 360–380s |
| Church and Empire | c. 312–451 |
| Syriac | c. 2nd–4th century |
| Latin Pastoral-Congregational | c. 240s–430 CE |
| Bethlehem Circle | c. 380s–420 CE |

Checked all nine against the census's `start`/`end` fields: seven already
matched (the old Wall Chart data these were sourced from had, for most entries,
already used Step 0's own figures — decade markers like "380s" read as their
decade's first year, e.g. 380, consistently). Two did not, both because
today's earlier fixes had reached for a Doc_01-level number instead: **Alexandria**
was at 150/400 (Doc_01's later, wider "candidate horizon" per its own Doc_01,
not Step 0's 190/254 — reverted); **Syriac** was at 200/410 (Doc_01's
specific, well-reasoned refinement anchored to the Synod of Seleucia-Ctesiphon,
not Step 0's vaguer "2nd–4th century" — reset to 100/400, the century range read
literally). **Deliberately left the displayed `dates` text unchanged for both**
— it stays the more informative Doc_01-level wording; only the invisible
`start`/`end` sort/position numbers now trace to Step 0. This means for these
two specific entries the shown date text and the internal ordering number carry
different precision on purpose, not a bug — flagging it here so it isn't
mistaken for one later. This Step 0 rule applies only to these nine Phase-One
worlds (the ones Step 0 actually ranked); eras 3–10 have no Step 0 record at
all (pre-survey signals only), so their `start`/`end` fields still come from
their own `dates` display string, which remains the best available source
there.

**Fourth addendum, same day — DECIDED: the Story view flattens by date across
lanes; the Wall Chart keeps lanes.** Mark's own worked example (House 70 →
Ebionite 1st c. → Alexandria 150 → Montanism 165 → Tertullian 197 → Syriac 200
→ Latin Pastoral 240s → Novatianism 251...) interleaves entries from four
different lanes into one sequence — a real reversal of the "within each lane"
answer from earlier today. Flagged the conflict rather than guessing which one
he meant; his answer, plainly stated: **the two surfaces get different rules on
purpose.** The Story ("this tile driven scrolling") flattens by date, full
stop, lane no longer a grouping or sort key. The Wall Chart ("the map... small
tiles without the information") keeps lane-grouping, because its bands are too
compact to carry the same information a Story row/card does, so the lane
structure is load-bearing there in a way it isn't here. Applied in `atlas.html`
and `index.html`: `renderLaneGroups()` (grouped-by-lane, sorted by date only
within each group) replaced by `renderFlat()` (one date-sort across the whole
list, no grouping) — used for both the normal entries and the pre-survey
expander's contents. Per Mark's explicit "don't lose the information": each
row/card now names its lane inline (appended to the existing dates · region
line) rather than in a group header — the lane is still visible, just not a
structural axis on this surface. The "Beyond the Floor" stream is untouched by
this — it was never lane-grouped to begin with, already renders as its own
box, already date-sorted from an earlier pass today. Wall Chart
(`world-atlas.html`) needs no change: its `laneRow()`/`LANE_ORDER` lane
structure was never touched by any of today's Story-view work and stays as-is,
per Mark's own reasoning for why it should.

**Fifth addendum, same day — DECIDED: the "Beyond the Floor" stream renamed
"Non-Nicene Traditions"; its description sentence rewritten.** Mark's
complaint, once he saw the box on the live page: not just the explanatory
sentence, but the section's own title — "Beyond the Floor" leans on this
project's internal eligibility-floor jargon (the same word used in status
labels like "Excluded - Doctrinal Floor (C1)" and "Floor Question (register)")
without explaining itself to a first-time reader; he didn't find it clear.
This reopens a title decided in the fifteenth pass (2026-07-16) — reopened
because Mark said so directly, not overridden unilaterally.

Three title options offered (all naming the Nicene Creed directly rather than
the internal "floor" metaphor, to read on its own without prior context):
"Outside the Nicene Creed," "Beyond the Floor (Outside the Nicene Creed)," "A
Different Confession." **Mark's pick, his own wording, not one of the three
as-is: "Non-Nicene Traditions."** Reads clean, states the actual dividing
line by name, no internal jargon a first-time visitor would need to already
know. The "— researched & explained" subtitle carries over unchanged — never
in question, still doing the job of signaling "explained, not hidden."

Description sentence (separately decided, same session): "Movements whose own
confessions diverge from the Nicene Creed, the shared conviction this project
builds from. They keep their true time and place; each carries a research
brief, not a chair." — replaces "Movements whose own confessions sit outside
this project's Nicene base," which named the Creed only via the internal
"base" shorthand.

**Applied in both `atlas.html` and `index.html`** (the Story's two copies);
verified live. **Not touched, deliberately out of scope for this pass:** the
same "Beyond the Floor" term as it appears in `world-map.html`'s Wall-Chart
predecessor content, the census spreadsheet, the spec, or anywhere outside
these two Story files — those weren't part of what Mark was looking at when he
raised this, and renaming a term that's referenced across multiple documents
and the census's own lane vocabulary is a bigger, cross-document consistency
question than "fix what's on this page." Worth a deliberate look later if Mark
wants the rename to propagate everywhere the term appears.

**Sixth addendum, same day — the retired term was still surfacing inside the
box itself.** Mark caught it again, precisely: "the saying beyond the floor is
in some of the tile descriptions also Cathars and others." Cause: today's
flatten-by-date change (fourth addendum) made every row print its own
`laneLabel` field inline so lane information wouldn't be lost — and for these
entries specifically, `laneLabel` in `world-census.json` was itself still the
literal string "Beyond the Floor" (19 entries carry this lane; `lane`, the
separate Wall-Chart routing key with its "8 " prefix, is a different field and
wasn't touched). Renaming the section header text didn't touch the underlying
data each row was quoting from — two different things that happened to say the
same words. **Fixed at the source:** all 19 movements' `laneLabel` field
changed from "Beyond the Floor" to "Non-Nicene Traditions" in
`world-census.json` directly (Marcion, Valentinian, Manichaeism, Homoian x2,
Bogomils, **Cathars/Albigensians**, Anti-Trinitarian Currents, Shakers,
Swedenborgian New Church, LDS, Jehovah's Witnesses, Christian Science,
Christadelphians, Oneida, Spiritualism/New Thought, Oneness Pentecostalism,
INC/Way/Unification/Luz cluster, Branch Davidians) — since this is the shared
census, not a Story-only file, and every row's inline tag reads directly from
it, one data fix corrects every tile at once rather than needing a per-row
patch. Verified live: Era 1's three Non-Nicene tiles (Valentinian, Marcion,
Manichaeism) each now show "Non-Nicene Traditions" in their own row instead of
the retired term. The `lane` field (Wall-Chart routing key) still reads "8
Beyond the Floor (researched & explained)" — left alone per the standing
scope note above; if that's ever addressed, `world-atlas.html`'s own
`LANE_ORDER` array needs the matching update since it hardcodes that exact
string for lane routing.

**Seventh addendum, same day — the rest of the "floor" jargon traced across
every surface it touched, including the Wall Chart, per Mark's explicit
yes.** Mark kept finding it in places a single fix didn't reach — each one
real, each one traced to its actual source rather than patched where he
happened to be looking:

1. *"there is also the floor verbage on the click tile for most of them"* —
   the click-through "full entry" sheet's `<h4>Floor / eligibility
   signal</h4>` heading, shown for any entry with a `floorNote` (all 178 of
   them, not just the 19 Non-Nicene ones). Renamed **"Where it stands on the
   Creed"** — matches the plain-English register of its sibling headings
   ("What survives," "Key relations, in brief") that "Floor / eligibility
   signal" never did.
2. Two more found in the same sweep before Mark had to point them out again:
   the top-of-page filter chip ("Beyond the floor" → **"Non-Nicene"**) and the
   per-era summary tally's catch-all clause ("...or beyond the floor" →
   **"...or a different confession"**). Plus one more once actually looking:
   the footer's "every floor question in one searchable table" → **"every
   creedal question"**.
3. *A genuinely bigger one, found while verifying #1 above:* the two status
   categories' own **`statusMeta` label and description** —
   `"Floor Question (register)"` (shortWord "Floor question — not yet
   resolved") and `"Excluded - Doctrinal Floor (C1)"` (shortWord "Excluded —
   doctrinal floor, grounds stated"). This lives in the **shared census**, not
   just the Story files — surfaces on the Wall Chart and Research Table too.
   Mark confirmed extending the fix there rather than leaving surfaces
   inconsistent. Renamed to "Creedal question — not yet resolved" and
   "Excluded — creedal grounds stated" (descriptions updated to match). The 23
   affected movements' own duplicated `statusWord`/`statusDescription` copies
   were resynced from the corrected `statusMeta` in the same pass — the
   census keeps a per-movement copy of these, not just a shared reference,
   worth remembering next time either field changes. **Deliberately left
   alone: the status *keys* themselves** (e.g. "Excluded - Doctrinal Floor
   (C1)," with its Methodology-defined "C1" criterion code) — internal
   taxonomy, not display text; renaming a formal Step 0 Methodology category
   is a different, bigger decision than fixing what a reader sees.

**Applied to `world-atlas.html` in parallel, all per Mark's explicit yes:**
the "About" legend's stream description; the footer's "floor and eligibility
notes" → "creedal and eligibility notes"; the honest-redirect copy for lane 8
("the base the floor measures from" → "the base every measure starts from");
the `STLABEL` legend entry ("Excluded or floor question" → "Excluded or
creedal question"); the click-panel's own "FLOOR / ELIGIBILITY NOTE" heading →
"WHERE IT STANDS ON THE CREED" (matching the Story's new wording); the
Research Table's "Floor / eligibility note" field label → "Where it stands on
the Creed". The lane-8 header needed a structural fix, not just a string
swap: `LANE_ORDER` is also the *matching* key against each movement's `lane`
field (still "8 Beyond the Floor..." on purpose, per the sixth addendum) —
renaming it in place would have broken lane routing. Added a separate
`LANE_DISPLAY` lookup so the rendered header reads "NON-NICENE TRADITIONS"
without touching what it matches against.

**One more real distinction surfaced and resolved, not just a wording
question:** both the Wall Chart's click panel and the Research Table's cards
were showing the **raw internal status key** as their badge (literally
"Excluded - Doctrinal Floor (C1)"), not the friendly `statusWord` just fixed
above — a display-source choice, not a jargon question. Flagged it rather
than deciding alone: the Research Table's whole purpose is exposing every
field for scholarly reference, so the precise formal key there may be
intentional, not a bug; the Wall Chart's panel is a general-audience surface
where it read as an oversight. **Mark's answer: fix the Wall Chart's badge,
leave the Research Table's as the raw key.** `chartRowsFrom()`'s adapter
gained a `statusWord` field (it only carried raw `status` before) and the
chart panel's badge now reads `r.statusWord`; the table's badge is untouched,
still `r.status`. Verified live, side by side: Marcion now shows "Excluded —
creedal grounds stated" on the Wall Chart and "Excluded - Doctrinal Floor
(C1)" on the Research Table — different by design, not by accident.

Verified live across all three surfaces after every step in this addendum; no
console errors; a repo-wide case-insensitive sweep for "floor" in both Story
files and the Wall Chart found nothing further user-visible left unaddressed
(remaining hits are internal: `Math.floor`, variable names like `r.floor`,
and the status keys deliberately kept as-is).

---

## 2026-07-23 — Found and fixed a real relaunch-day gap: two of three Atlas surfaces had no real hand-off wiring at all

**Context:** Mark, relaunch morning: "i want the atlas fully working." Checked
rather than assumed what that actually requires, since "the Atlas" is now
three files. Found `cic-website/index.html` (the homepage) already had a real,
working hand-off pattern — an `isLocal`/`LIVE_APP_URL` gate that does a real
`window.location.href` redirect to `/?worlds=<id,id>&mode=<interview|table>`
when a live app URL exists, and an honest "hosting is still being finished"
fallback otherwise (never a permanent fake-demo claim). Presumably added by
whoever did the Brand-Messaging-Rework/deploy-config work.

**But `atlas.html` (the standalone page linked from every nav bar) and
`world-atlas.html` (the Wall Chart) had never gotten the same fix** — both
still carried a permanent, unconditional "This is a design sketch/demo — it
ends here, honestly" stub with no escape hatch. Meaning: right now, a visitor
landing on the homepage would get a real conversation hand-off the moment
hosting exists, but a visitor who clicked "Atlas" in the nav, or "View as a
wall chart," would hit a dead-end demo message regardless of whether the app
was actually live. A real, silent inconsistency between the three surfaces —
exactly the kind of thing that would only surface when a real visitor hit it
on relaunch day itself.

**Fixed in both files, mirroring `index.html`'s exact pattern:** added the
same `isLocal`/`LIVE_APP_URL` gate; `atlas.html`'s `launch()` now redirects
for real when `LIVE_APP_URL` is set, falling back to the honest message
otherwise. `world-atlas.html`'s two hand-off points (the panel's "Interview"
button, the tray's "Sit down at the Table" button) got the same treatment,
layered alongside its existing `APPMODE` check (a separate, still-valid
mechanism for when the chart is embedded *inside* the app itself at
`/world-map/` — untouched). Verified live: clicking through on both files
correctly attempted `localhost:8199/?worlds=post-apostolic-house-church&mode=
interview` — the right world ID, the right mode — failing only because
nothing is listening on that port in the test environment, which is the
expected result of a correct attempt, not a bug.

**The actual remaining blockers, confirmed by reading the deploy-config
commit (`d994b22`, this morning) rather than assumed:** two account-level
actions, neither performable by Claude —
1. **GitHub Pages:** repo Settings → Pages → Source: GitHub Actions. This
   makes the static site (all three Atlas surfaces) live.
2. **Render:** dashboard → New → Blueprint → connect this repo (`render.yaml`
   is already at the repo root and will be found automatically). After the
   first deploy assigns cic-poc a URL, set `ANTHROPIC_API_KEY` and
   `CORS_ORIGINS` in Render's own Settings → Environment (deliberately never
   committed to the repo).

**Once Render assigns a real URL, one more small code step:** replace the
`''` production branch of `LIVE_APP_URL` in `atlas.html`, `index.html`,
`world-atlas.html`, and `pilot.html` (four copies of the same three-line
pattern, small enough that a shared include isn't worth the complexity on a
plain static site with no build step) with that real URL, and set
`CORS_ORIGINS` on Render to match the Pages domain so the app's own CORS
check allows the hand-off. Give me the URL once Render assigns one and this
is a five-minute fix, not a rebuild.

**Next action:** Mark does the two account-level steps; reports the Render
URL back here for the final wiring.

---

## 2026-07-22 — Wall Chart and Research Table consolidated into one document, reading the shared census; both stale-status pages archived

**What prompted this:** while confirming Phase 1 (the Story) was already built and
live — the front-end rebuild thread's actual starting state, ahead of its own launch
prompt — a check of `world_manifest.py` against the Story's census found Church and
Empire/Marius (installed 2026-07-18/22, the sixth live world) still showing "Chosen —
not yet built." Fixed in `data/world-census.json` (status, color `#7A2E2E`, icon
copied from Brand-Assets) and verified live. Checking the two other Atlas pages for
the same drift found it there too, plus a second instance already present:
Alexandria/Theon was ALSO still stale in both `world-map.html`'s and
`world-atlas-list.html`'s own embedded census copies (each of the two pages
carried its own full, independently-hand-maintained copy of the 178-entry census —
never migrated to the shared JSON when the Story was built). Asked Mark whether to
patch both copies again or fix the duplication itself; **Mark's direction: build one
document that serves both purposes and archive the stale ones.**

**Built — `cic-website/world-atlas.html`**, one file, a view toggle (`#chart` /
`#table`, default chart) between the Wall Chart and the Research Table. Both views
fetch `data/world-census.json` once at runtime; the Wall Chart keeps only what is
genuinely presentation-only and doesn't drift — per-entry start/end years for
timeline placement (extracted from the old embedded data, verified against all 178
entries with zero position gaps), era medallions, figure lifelines, relationship
edges, neighbor-redirect map — while every census-truth field (status, living, name,
why, sourcing, floor note, relations, lane) is joined in from the shared JSON by
Atlas ID at render time, never duplicated. The two original stylesheets and nearly
all original interaction logic (zoom/pan, tray, panel, guided tour, search/filter)
carried over verbatim inside their own view containers; each view's CSS is a
separate `<style>` element the other view's activation disables via the DOM
`.disabled` property, so the two original palettes never collide despite sharing a
page. View state uses a URL **hash** (`#chart`/`#table`), not a query parameter — a
local test server was found to silently drop query strings on a clean-URL redirect,
and a hash is immune to that class of problem since it never reaches the server.

**Verified live** (both via direct `file://` and via the project's own `serve`-based
local static server): all 178 entries render in both views; Marius and Theon both
show `Built & Live` with correct colors/actions in the chart and correct status in
the table; search/filter on the table view works; the chart's click/tray/panel flow
and guided tour run without console errors; view-toggle round-trips correctly
including on a direct `#table`/`#chart` deep link.

**Archived, not deleted** (`Drafts-Archive/CiC_World_Map_html_Superseded_2026-07-22.html`,
`Drafts-Archive/CiC_World_Atlas_List_html_Superseded_2026-07-22.html`, moved with
`git mv` so history follows): the two pages `world-atlas.html` replaces. All in-site
links (`atlas.html`, `index.html` — both carry their own copy of the Story view) and
the census's own `meta.notes` repointed to the new document. Full detail kept current
in `Integration-Notes.md`, this file's single-source-of-truth companion.

**Also found and corrected in passing, not a new decision:** the sibling worktree
directory this feature's own notes named for the `world-map-merge-into-main` branch
(`C:\Users\mchad\Documents\CiC-Project-worldmap-merge`) no longer exists — the branch
lives only in this repo now, 2 commits behind `main`.

**Heart of it:** the live-status drift bug had already been fixed once (Alexandria)
and had already recurred once more (Marius) before this thread even started looking —
two instances in two months, both silent until someone happened to check. Patching a
third stale copy would have made the count three-for-three; consolidating the data
source is the only fix that changes those odds going forward, and it cost the same
afternoon a third patch would have.

**Next action:** the front-end rebuild thread's real remaining work is Choose a
Tradition — the in-app selector — built against `claude/world-map-merge-into-main`'s
existing handoff contract, per `Integration-Notes.md`.

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

## 2026-09-17 — Era break band replaced with a thin divider line

**Mark's report, from the live site:** the white horizontal bars marking the
boundary between eras were "thick," "block[ed] the whole map under it," and
looked "overwelming." He asked for them deleted and replaced with "just a
white line starting under the text tha[t] has a very subtle background to
stand out."

**Confirmed the actual defect before touching anything:** screenshotted
`atlas-v3.html` locally first. Each era's own "break band" (`gBreakBand`, in
`render()`'s `eras.forEach` loop) was a `BLEED_W`-wide, 120px-tall rect at
~92% opacity in dark mode (the site's default register) — composited to
~#E5E4E0, essentially opaque near-white, painted behind the rivers but
re-painted again on top of them via a fade gradient (`gBandFade`/
`#bandFade`) that kept a bright, always-visible ~22px stripe at the band's
own top and bottom edges regardless of what was underneath. In practice this
read exactly as reported: a wide, heavy, near-opaque block at every era
boundary, cutting the map into segments rather than dividing it cleanly.

**Fix:** removed the break band and its fade gradient entirely (`gBreakBand`
group, the `#bandFade` `linearGradient` and its per-render stop-color
update, both ~120px rects). Replaced with, per era: a single thin line
(1.5px, near-white in dark mode) plus a slim, low-opacity wash (18px tall,
~0.1 opacity) directly behind it only so the line has enough to sit on
against a busy stretch of river — not a return of the old block. Both are
drawn on top of the rivers (the old fade layer's position) so the line
stays crisp regardless of what color river crosses under it.

**Positioned under the text, not at a fixed offset:** the era label/tag/
context text was untouched (it already has its own 5px stroke-halo for
legibility against the map, unrelated to the band) — but the divider's own Y
position is now computed from where that specific era's text actually ends
(reusing the same `wrapText()` call the context text itself uses, so a
one-line vs. three-line context wrap each get a correctly-placed line)
rather than the old fixed 120px height that left a lot of dead, blocked
space under short headers.

**Verified:** screenshotted before/after locally — the rivers now run
unbroken through the header gutter instead of disappearing under a block;
the line and its wash are visible without re-creating the "wall" effect;
no JS console errors from the change (`gBreakBand`/`bandFade` fully removed,
no dangling references).

## 2026-09-17 (cont.) — Era header text made theme-aware; the halo was blurry because its light card was gone

**Mark's report:** the new divider line is good, but the era header text
("1. The Early Church Era" and the lines under it) reads blurry with its
current halo — asked for it crisp.

**Root cause found in the file's own comment, not guessed:** `.era-label`/
`.era-tag`/`.era-context` carried a comment explaining they were
deliberately given fixed (non-theme-variable) dark-ink fill colors and a
thick 5px near-white stroke halo, because they always sat on the old break
band — "its own small light card in both themes," so the text was
dark-ink-on-light-card regardless of the page's own light/dark tokens. That
card is exactly what the previous entry just removed (it blocked the map).
With no card left, the same fixed dark fill + thick light halo now had to
carry all the legibility work directly against the busy map, and a 5px
round-joined halo at 13-22px font sizes reads as a blurry white smear
rather than a crisp edge — the effect got worse, not better, once the
premise it was built for (a card always behind it) was gone.

**Fix:** switched `.era-label`/`.era-tag`/`.era-context` from fixed hex
colors to the same `var()` theme tokens the map's own node/movement labels
(`.lbl`, already correct) use, and matched `.lbl`'s already-tuned 3px halo
width instead of 5px:
- `stroke:#F6F6F2` (fixed) → `stroke:var(--parchment)` — dark in dark mode
  (`#1d1811`), giving light text a thin *dark* backdrop instead of dark
  text a thick *light* one.
- `era-label` fill `#B45309` → `var(--gold-leaf)` — this file's own dark
  register already has a lightened, dark-safe gold-leaf value (`#cfa55c`)
  defined and unused here until now.
- `era-tag` fill `#6C6257` → `var(--ink-faded)` (dark-safe `#a4967a`).
- `era-context` fill `#2A2521` → `var(--iron-gall)` (dark-safe `#e9dfc7`,
  light cream — the description paragraph is now light text, not
  near-black text trying to show through a thick white halo).

Stroke width 5px → 3px, matching `.lbl`.

**Verified:** re-screenshotted the same era boundaries — text reads as
clean, distinctly-colored (gold title / tan dates-and-count / cream
description), with a thin dark edge for legibility rather than a soft
white smear, at both the "1. The Early Church Era" and "2. The Imperial
Church Era" headers.

## 2026-09-17 (cont. 2) — Era header text enlarged; context wrap narrowed so it fits on screen when zoomed

**Mark's report, once the crisp-text fix landed:** the text reads well now,
but it's too small to read comfortably, and zooming in to read it runs the
text off the screen.

**Diagnosed, not guessed, with an actual zoomed screenshot:** the era
context paragraph was wrapped at 200 characters per line — at 13-15px
font, that's a line roughly as wide as the entire map. At the default,
fully-zoomed-out view this isn't obvious (the whole map fits on screen,
so the line does too), but the moment someone zooms in far enough to read
the now-larger text comfortably, that same line spans far more screen
pixels than any browser viewport holds. Tested directly: at a middling
zoom level, a 100-char wrap still ran the description well past the right
edge of a 1400px viewport.

**Fix, in two parts:**
1. **Bigger text:** `.era-label` 22px→26px, `.era-tag` 14px→16px,
   `.era-context` 13px→15px.
2. **Narrower context wrap**, so a line stays short enough to actually
   fit on screen once zoomed in to read it, not just at maximum zoom-out:
   the fixed `200` inlined at two call sites replaced with one named
   constant, `ERA_CONTEXT_WRAP`, tuned empirically against real zoomed
   screenshots (100 chars still overflowed; 55 fit with room to spare but
   produced up to 7 lines for the longest entries; **65** landed as the
   fit-on-screen floor with the fewest lines, confirmed at three different
   zoom levels including a middling and a fairly deep zoom, both well
   within a 1400px viewport).

**A second-order effect caught and fixed in the same pass:** taller
headers (up to 5 context lines at the new sizing, for the two longest
`WORLD_CONTEXT` entries) pushed the divider line drawn in the prior entry
past `HEADER_GUTTER` (190, sized for the *old* 2-3-line-max wrapping) —
the first movement's portrait and label started overlapping the last line
of description text. Computed the actual worst case (7 lines at the
now-superseded 55-char wrap; 5 lines at the shipped 65-char wrap ≈ 184px
to the divider) and raised `HEADER_GUTTER` to 230, restoring the clean
gap between the header text and the first movement below it.

**Verified:** re-screenshotted at the default view and three zoom levels
(via synthetic wheel events on `#stage`, matching the real zoom handler) —
text fits within the viewport at every level tested, and the
"Scattered Households" portrait no longer overlaps the era 1 description.

## 2026-09-25 — Open question for Mark: `statusWord` still carries public-facing process vocabulary

Found while fixing `world-census.json`'s `statusDescription` field for the
Live-Surface-Cleanup program (`Ministry/Operations/Audits/Tech-Readiness-
2026-09/Live-Surface-Cleanup/Decision-Log.md` Entry 8): the sibling field
`statusWord` — rendered directly on the public Atlas, once per movement,
in `atlas-v3.html` — still names the survey's own internal process on 233
of 292 rows (80%). The dominant pattern is `"Researched — [tier] (Era N
Step 0)"`; rarer ones carry raw internal shorthand into visitor-facing
text — `[S]`, `c2`, `A3`, `A4`, `register`, `WINDOW-SPECIFIED`,
`RETAINED`, `BANKED`, `beyondFloor`.

**Not changed here.** This is a public-status-vocabulary decision, not a
commentary cleanup: `statusDescription` (the paragraph) could be rewritten
without inventing anything because the underlying facts were always
there to restate in plain language. `statusWord` (the short label) is a
design choice about what a visitor should see at a glance, and "Era N
Step 0" is doing real, compact work there (signalling roughly how
thoroughly-vetted a not-yet-built entry is) that a plain rewrite can't
just drop without deciding what replaces it. That's Mark's call, not a
rewrite call.

**Next action:** Mark decides the public vocabulary — keep it, or replace
"Researched — [tier] (Era N Step 0)" and the raw-shorthand outliers with
plain-language equivalents (a natural pairing with `statusDescription`'s
new register: "Reviewed, strong candidate" / "Reviewed, one of several
candidates" / etc.) — then whoever implements it re-runs
`tools/check_live_commentary.py --surface cic-website` to confirm the
fix and update this entry.

## 2026-09-25 (same day) — Decision 7 ruled: the "(Era N Step 0)" tag dropped from `statusWord`; the raw-shorthand outliers stay open

**Mark's ruling on Decision 7 (2026-09-25), verbatim: "a."** Option A -
plain words at the source: drop the "(Era N Step 0)" build tag from
every `statusWord` value that carried it, keep the plain assessment.
This resolves the "(Era N Step 0)" half of the open question above; the
other raw-shorthand outliers it also names (`[S]`, `c2`, `A3`, `A4`,
`register`, `WINDOW-SPECIFIED`, `RETAINED`, `BANKED`, `beyondFloor`) are
**not** touched by this ruling and stay open for a separate decision.

**Fixed at the source, not just the output.** `world-census.json`'s own
`statusWord` field has no further upstream generator for non-built
movements - `engine/m6/census_sync.py` only ever writes `statusWord` for
`status === "Built & Live"` movements (from `statusMeta[status].
shortWord`), so for the 212 (now 221, see below) non-built movements
this field was always hand-authored directly in `world-census.json`
itself; census.json *is* the source for it, confirmed by reading
`census_sync.py`'s own sync logic rather than assumed. Fixed there, then
`atlas-v3.html` re-synced from it via the existing generator
(`engine.m6.census_atlas_sync.sync_atlas` + `engine.m6.atlas_html.
apply_movement_updates`) - never hand-edited into the Atlas directly.

**220 movements' own `statusWord` carried the tag as originally counted,
plus one more the fix itself surfaced.** Checked exhaustively (not
estimated): 212 carried the tag as a whole, standalone parenthetical
("Researched — strong candidate (Era 3 Step 0)" → "Researched — strong
candidate"); 8 carried the tag *inside* a parenthetical alongside other
real content after a "; " separator ("...(Era 7 Step 0; corpus
verification follow-up named)" → "...(corpus verification follow-up
named)" - the substantive clause preserved, only the tag itself
dropped). Adding the new `tools/validate-census.mjs` check below (run
before considering this done, not after) caught one further case outside
either pattern: `early-american-unitarians-universalists`'s own
`statusWord` carried `"(Era 8 gate)"` - the same build-stage reference in
different words, not literally "Step 0" - fixed the same way (the
parenthetical dropped, the surrounding clause kept intact). 221
movements' `statusWord` values changed in total.

**Regression check added**, per this ruling's own instruction:
`tools/validate-census.mjs` now fails any `statusWord` containing
`"Step 0"` or `"(Era "` - the same pattern that caught the
`early-american-unitarians-universalists` case above, so it stays caught
if either phrasing is ever reintroduced.

**No visitor-visible change.** Confirmed directly: nothing in
`atlas-v3.html`'s own rendering JavaScript displays `statusWord` at all
today (the earlier open-question entry's own framing, "rendered directly
on the public Atlas," was itself imprecise about this - `statusWord`
lives in the embedded `DATA` object but is not read by any property
access in the page's own render code, the same structural gap this
program's own D2 work found for `statusDescription`).

Verified: `node tools/validate-census.mjs` 0 errors; `engine.m6.
census_atlas_sync.sync_atlas` reports 0 remaining drift against
`atlas-v3.html`; `engine.m2.cli staleness-check` and `engine.m2.
site_cli staleness-check` both pass; `node --check` on the regenerated
`DATA` script block; `tools/check_paths.py --baseline` 0 new unresolved
citations; `tools/check_live_commentary.py --surface cic-website` hit
count unchanged before/after (130 either way - nothing new introduced).

## 2026-09-25 (later) — Cleanup item filed: `statusWord` confirmed dead code, reads nothing on the live Atlas

**Origin.** While fixing the 7 `statusWord` labels this earlier entry's own
Decision 7 pattern-match had missed (their era number sits inside a longer
parenthetical - "the record-mandated Era N disposition," "proposed and
recorded, Era N" - rather than the standalone `(Era N Step 0)` tag Decision
7 fixed fleet-wide), the question came up directly: does the "no
visitor-visible change" note on Decision 7's own entry mean this field
needs wiring up, not just cleaning?

**Traced exhaustively, not assumed.** Both places `atlas-v3.html` renders a
movement's status:

- The hover tooltip (`tipFor()` → `statusLabel()`) reads
  `DATA.statusMeta[m.status].shortWord` - one generic string per `status`
  enum value (e.g. every "Floor Question (register)" movement gets the same
  "An open theological question", regardless of its own `statusWord`). The
  comment directly above `statusLabel()` explains why this indirection
  exists: `status` itself "still carries internal process language...
  never meant for a participant to read as-is," and `statusMeta` is the
  fix for that - a different, working fix than `statusWord`.
- The click panel (`openPanel()`, ~130 lines) never references
  `m.statusWord` anywhere. Its own "Where this tradition stands" section
  reads `m.why` instead - checked directly for all 7 movements this entry's
  own fix touched; all seven are clean, plain narrative prose already, no
  era or build-process language.

A repo-wide grep for `.statusWord` property access (not just the JSON
literal) confirms zero matches in `atlas-v3.html` or `cic-poc/frontend`.

**Conclusion: not a bug, nothing to wire up.** `statusWord` is a third,
orphaned field alongside the two mechanisms (`statusMeta.shortWord`,
`why`) that already do this job correctly. Every one of the 292 movements
carries a copy of it in `world-census.json` and `atlas-v3.html`'s embedded
`DATA`, synced automatically (`engine/m6/census_sync.py:43`'s
`shortWord`→`statusWord` mapping for built worlds;
`engine/m6/census_atlas_sync.py:50`'s `STRUCTURAL_FIELDS` for the
census→Atlas sync) and guarded by `tools/validate-census.mjs` (required key
at line 34; Decision 7's own regression check at lines 41-46) and by
`engine/m6/tests/test_census_sync.py`'s assertions - all real, working
machinery keeping a field alive that nothing downstream reads.

**Not fixed here.** Deleting it is a bigger, structural change than this
entry's own scope (a 7-label wording fix): it touches the sync module, the
Atlas generator's field list, the validator, and the test suite, not just
`world-census.json` content. It's also not a pure mechanical deletion -
someone should confirm first whether `statusWord` was ever meant to show a
per-movement detail beyond `statusMeta`'s generic label (in which case the
fix is wiring it up, not deleting it), which is a design read, not a code
read.

**Next action:** filed as a cleanup item, not acted on. A future pass
decides fleet-wide whether to (a) delete `statusWord` from
`world-census.json`, `atlas-v3.html`'s `DATA`, `census_sync.py`,
`census_atlas_sync.py`'s `STRUCTURAL_FIELDS`, `validate-census.mjs`, and
`test_census_sync.py` since nothing reads it, or (b) wire it into
`openPanel()` or `tipFor()` as the per-movement detail it looks like it was
meant to be. Either way, `tools/validate-census.mjs` and
`engine/m6/tests/test_census_sync.py` need updating alongside whichever
choice is made.

## 2026-10-09 - Family tree: design record reconciled, edge model drawn, 21 rulings made (two Fable sessions)

The project lead asked to explore upgrades to the Church Family Tree (`cic-website/atlas-v3.html`) after an outside tool's inventory reading of the page proposed a list of improvements. Two Fable sessions ran overnight, design and research only: no repo edit, no model call, no live file touched. Session 1 reconciled the report against the design record. Session 2 modelled what each line type asserts and how identity seams, merges and gaps are drawn. The project lead then ruled on every open decision in one sitting, one at a time.

**What the sessions found.**
- The live page is the river map, shipped 2026-09-03 in four merges, not the August canvas. This log has no entry for that launch. Search, the lane, region and built-worlds toggles, the theme chip and the filter deep-links ruled in August lapsed in that replacement.
- "The Story replaces the canvas" (2026-07-20) was overtaken on 2026-08-02 by "only one atlas, done right". The Atlas README and Integration Notes still describe the Story as live and Tier A/B as undecided.
- Of the report's 19 suggestions: 8 already decided (5 lapsed in September), 4 already proposed, 5 new, 2 in conflict with the 2026-08-03 accessibility pass. Several factual claims were wrong in kind: the dead keyboard code is pointer pan buttons; the page has about 443 Tab stops; the "10 drifted movements" are built worlds whose prose the sync leaves null by design; real drift is 4 of 69 edge notes, and `atlas-check` runs nowhere in CI.
- The edge model: only `formed` asserts descent, and only as "came out of". The river map births the Greek East river from a `transmitted to` edge, and four more rivers from a hand-coded parent table with no census edge. Of the 77 `continuesAs` links, 50 are clean; 14 span gaps of 35 to 330 years with no confidence word; 4 overlap (one by 110 years); 7 join renewal currents the 2026-08-03 standing rule says are never identity. The two cross-lane bridges are one real act (Chanforan, 1532) and one era-boundary artefact (Hussites at 1517), and a keyboard user cannot reach either.

**Rulings, 9 October 2026.**
1. **Freeze rule (E1).** The September practice governs; the July pilot-window rule is superseded. System Hub decision 62.
2. **The Story (E2).** Recorded as superseded. The two-surface split survives: the website explores, Choose a Tradition selects in the app.
3. **Data seam (E3).** The page keeps embedding the census for now. `atlas-check` is added to CI and the sync is extended to compare edges. The redesign fetches the census at runtime and retires the m6 atlas tooling then.
4. **Keyboard (E4).** Roving focus: the map is one Tab stop; arrows walk time inside a river and cross rivers; every mark shows its tip on focus; Enter opens the panel; plus and minus zoom; Home resets. This reverses the 2026-08-03 thread decision that keyboard users skip the preview.
5. **Lapsed features and title (E6).** Search and the theme chip return. The lane, region and built-worlds toggles and the filter deep-links are retired. The page is titled "Church Family Tree"; the 2026-08-03 title "Church in History" is superseded.
6. **Small scope (E5, E7, E8).** Permanent bank inscriptions plus a retune of the weakest colour-blind lane pairs. Self-hosting the typefaces goes to the Website-V2 and brand track as a site-wide decision. The module split happens inside the redesign only, after E3.
7. **Edge types (D1).** `formed` asserts origin, `transmitted to` asserts influence only, the other three assert no lineage, `continuesAs` alone asserts identity. No sixth type until a real pair of entries needs one.
8. **River births (D2).** Only a `formed` edge births a river. The four hand-coded parents become census edges, by the 2026-08-02 rule that a claim the census does not carry comes back as an edge, or become springs.
9. **Overlap (D4).** Overlapping continuity windows are a defect. The validator warning becomes an error and the four pairs are re-dated or re-linked at the next Step 0 pass for Eras 1 to 4.
10. **Unions, gaps, graphite (D5, D6, D8, D9).** The panel shows a "Union" line, in the entry's own words, for the seven union entries; no merger is drawn. A gap is drawn only where an identity link spans it and carries a confidence word; otherwise nothing is drawn and the panel says no continuation is recorded. A river's birth and a gap bed take the dash of the claim they rest on. Graphite keeps its meaning, "not yet built"; a gap bed is iron-gall bank lines without water.
11. **Glyphs (D7, D10).** Filled dot for `formed`, open dot for `transmitted to`, the storyboard's footbridge with three modifiers for the other three types; no arrowheads. The identity bridge is iron-gall with a dated stone, not gold. Words stay the first channel.
12. **Renewal chains (D3).** The 2026-08-03 rule stands. The seven chains are removed from `continuesAs` and recorded as graded `transmitted to` edges, with the kinship in prose. This reverses the Optina to Catacomb Church link ratified at the Era 10 freeze.
13. **Confidence vocabulary (D11).** A five-level field is added beside the three-value edge confidence now; the three-value field retires at a later pass once all 69 edges are re-graded.
14. **Hussite bridge (D12).** The 1517 bridge is a segmentation artefact; the lane is re-ruled at an Era 7 pass unless that gate can name the act. The Waldensian bridge stands (Synod of Chanforan, 1532).
15. **Edge notes (D13).** One-pass rewrite of the 69 edge notes to the readability target by the Step 0 thread, with the process commentary in four of them moved to the log.

**Next action.** Nothing is built. The redesign is sandbox work, held to the sandbox rule: it replaces the live page only when judged clearly, significantly better. Items that need no design work and can go ahead as mechanical fixes: `atlas-check` in CI with edge comparison (ruling 3), and removing the process commentary from the four edge notes (ruling 15, which the live-commentary rule also requires). Rulings 8, 9, 12, 13 and 14 change census data or its schema and route to the Step 0 and validator work; they are not made here. Still to do from this entry: correct the Atlas README and Integration Notes (the river-map launch, Tier A/B decided, the Story superseded); register the lapsed-feature retirements; and re-run the colour-vision check on the retuned lane pairs. Not done by any session: contrast measured on the river map's text, a screen-reader test, a real-phone test.

## 2026-10-09 - Follow-up to the family tree rulings: edge comparison built, stale notes corrected, census notes held

Three of the next actions from the entry above are done. (1) Edge comparison: `engine/m6/census_atlas_sync.py` gains `compare_edges`, and `atlas-check` and `atlas-sync` now report edge differences between `world-census.json` and the Atlas's embedded edges, keyed by from, to and type. Edges are compared, never written. Tests are added in `engine/m6/tests/test_census_atlas_sync.py`; the m6 suite passes (38). Run against the committed files, `atlas-check` reports exactly the four edge notes found earlier (Baptists and Methodist Revival into the Black Church; Fundamentalism into the Mainline Century; the Stone-Campbell split). (2) The Atlas README and Integration Notes are corrected: the river map's 2026-09-03 launch, Tier A/B decided, the Story superseded, the census embed and its sync, and the two integration branches gone from the remote. (3) The lapsed August features are recorded as retired or restored in ruling 5 of the entry above.

**Resolved the same day.** With the project lead's approval of the census edit, the four edge notes in `world-census.json` were brought to the Atlas page's cleaner text (four lines changed, nothing else), and `python -m engine.m6.cli atlas-check` was added to `.github/workflows/ci.yml` beside the existing `check`. `atlas-check`, `check` and `tools/validate-census.mjs` all pass (0 errors; the 2 shortName warnings were already there). Two of the four notes carried process commentary ("The census's second 'in tension with' edge", "No continuesAs write"); both now read clean in the census, as they already did on the page. A third note still carries commentary in both files ("Process honesty:" in the Great Schism edge, identical in census and page, so the drift check cannot see it); it was outside the four approved strings and is left for ruling 15's rewrite. The remaining 53 notes that fail the readability gate are ruling 15's one-pass rewrite, not done here.
