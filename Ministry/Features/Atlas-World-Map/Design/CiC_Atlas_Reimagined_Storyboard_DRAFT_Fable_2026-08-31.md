# CiC Atlas Reimagined — Creative Storyboard (DRAFT for review)

**Status: FIRST CREATIVE DRAFT. Nothing here is decided, built, or authorized to
build.** This is the creative/artistic pass Mark asked for — a Fable-model draft,
produced 2026-08-31, in the sandbox posture the brainstorm capture locked
(`CiC_Atlas_Reimagined_Divergent_Capture_V1_2026-08-31.md`, §10.1: the live Atlas
keeps serving participants untouched until a replacement exists **and** is judged
clearly better). This document proposes no tools, no architecture, no build plan
— those are explicitly out of scope. It draws scenes: what the reimagined Atlas
could look and feel like, made concrete enough for Mark to say *yes, that* or
*no, not that* about specific pictures rather than abstractions.

**Built from real material, not invention.** Every named world, era, date, edge,
and confidence grade below is taken directly from `cic-website/data/world-census.json`
(292 movements, 10 eras, 69 sourced edges as of V0.20). Every piece of period art
or architecture described is a real, citable object or place — most of them
already cited in the census's own `experienceToday` fields — framed the way a
museum wall label would frame them, per the standing rule against AI-generated
scene art presented as history. Where this draft takes a creative swing on an
open question, the swing is marked **[PROPOSED — this draft]** so it can be
weighed, not mistaken for something already settled.

**The constraints this draft works inside, stated once:** the locked manuscript
palette (parchment `#F7F3EB`, iron-gall `#2A2521`, madder `#A13E2B` — muted,
never brightened toward alert-red — gold-leaf, lapis, Tyrian, graphite; Full UX
Design V1.0 §2.1); Alegreya for reading, Alegreya Sans for chrome, Cinzel
confined to the map's own engraved artifacts (§2.2); the anti-ghost principle
(§2.5a — *"these must feel like real people at a table, not spirits or ghosts…
no lighting or glow"*); hover = short, click = full, and no new interaction verb;
**no motion on the board at all** — the only motion in the whole experience is
the participant's own panning and zooming (capture §11, Mark's correcting pass:
*"the actual board doesn't need motion, the visuals don't need motion, the art
does need to capture alive"*).

---

## 0. The board, stated once — so the scenes don't have to keep explaining it

**Time flows down.** The sheet reads like a page, and like the era-accordion the
project already ships: 70 CE at the top edge, the present at the bottom. Ten era
bands cross the sheet horizontally, each on its own approved ground from the
census (`eras[].ground`): Era I on warm aged parchment `#EFDDB3`, Era II on pale
vellum-green `#E3E0CB`, Era III on cool pale blue-grey `#D8E4E5`, and the three
tones alternating in that quiet cadence down all ten bands to the Global Church
Era at the bottom, back on warm `#EFDDB3`. The alternation is soft enough that
you feel the descent more than you see the seams — like the gathering-marks in a
codex. **[PROPOSED — this draft]:** the compass instinct: lanes are placed with
`laneOrder` ascending **right to left**, so the Syriac East & Asia river rises
at the sheet's eastern edge, the Caucasus and Greek East beside it, Africa
toward the center, the Latin West further west, and the Protestant and Global
Revival lanes opening toward the sheet's western margin. A loose compass
feeling, not a geographic claim — a swim-lane chart wearing a map's manners.

**Each tradition family is a river.** The census's own `lane`/`laneOrder` fields
are the riverbeds; nothing structural is invented. A tributary joining the main
channel is a real `formed`/`transmitted to` edge. The same river continuing
under a new name is a real `continuesAs` chain. A river ending is a movement's
own recorded end date. Rivers are drawn the way the old mapmakers drew them:
**two fine iron-gall bank lines with a muted pigment wash between** — each
lane's wash its own quiet pigment from the palette's family (exact lane-pigment
assignments deliberately left for the next pass). The one thing a river never
does is move. No shimmer, no animated current, no drifting texture. Ever.

**Honesty is rendered, not asserted.** Built & Live worlds sit on the landscape
at full pigment. Everything else is drawn in **graphite underdrawing** — the
palette's own one unpigmented color (`--graphite #8A837C`), the uninked ruling
every real manuscript carries under its ink. "Dimmed is an honest state, not a
disabled state" is already decided language in this project; here it becomes a
craft fact: the not-yet-built parts of the map look like what they are — the
survey a scribe has ruled but not yet inked. Nothing is hover-dead. Confidence
keeps its existing honest line-language everywhere a course is drawn:
**Documented = solid, Widely Accepted = dashed, Contested = dotted** — the map
never inks a stream it can't defend.

**What makes still art alive — the creative swing.** This is the one open
question the capture names twice (§11, §14) and never resolves. This draft's
proposed answer, applied in every scene below, is three-fold
**[PROPOSED — this draft]**:

1. **Evidence of use.** The still-life painter's oldest trick: things shown
   mid-use, just set down. Bread broken, not whole. A letter unfolded, creases
   showing. A stylus laid across a half-written tablet. A cup pushed slightly
   off-center, the way a real hand leaves it. No figures needed — the warmth of
   people is in the room they just stepped out of. (This is also the anti-ghost
   principle's safest ground: where a figure would risk reading spectral, show
   the implements of a practice and the space built for it instead.)
2. **Light with a time of day.** Not glow — *weather*. Lamplight low on a
   plaster wall in Era I; white desert noon in Egypt; candle-dark gold in
   Byzantium. Light falling on stone and bread and ink is an event that
   happened to real matter; a glow is an effect that happens to nothing.
   Anti-ghost stays absolute: light lands on objects and architecture, never
   as an aura on a person.
3. **The mark of the hand in the rendering itself.** Visible ink texture,
   pigment pooling at the edge of a wash, the graphite underdrawing showing
   at a river's bank. A manuscript feels alive because someone's hand made it
   and you can see that they did. The Atlas should feel like the largest page
   this scriptorium ever ruled — a made object, not a rendered surface.

---

## Scene 1 — The whole landscape at rest

*Zoomed all the way out. The participant has just arrived and touched nothing.*

**What the participant just did:** clicked through from wherever they were —
the homepage, the end of a conversation — and the Atlas opened at full extent.
The camera is still. Nothing on the board moves, and nothing ever will; the
first impression is the deep quiet of a large map on a library table.

**On screen:** the whole sheet at once — ten era bands descending through their
warm→cool→warm cadence, and across them the river systems: seven family lanes
plus the headwater. At the very top, on Era I's aged-parchment ground, a single
spring: **Post-Apostolic House-Church Christianity** (70–200 CE), the census's
own `laneOrder 0`, labeled in the data itself *"Origin — before the lanes
divide."* Its `relationsSummary` reads, verbatim, *"Parent of nearly everything
on the map"* — and at this zoom that is simply what the picture shows: one
spring, and below it the lanes fanning out — Syriac East & Asia at the eastern
edge, then Caucasus, Greek East & Orthodoxy, Africa, Latin West & Catholicism,
and further down the sheet the Protestant & Evangelical and Global Revival &
Pentecostal lanes opening where their real start-dates put them. At the far
margin, set off by a ruled border like a mapmaker's marginal table, the
Beyond-the-Floor terrain (the census's lane 80, "Non-Nicene Traditions,"
researched and explained) — present, labeled, never hidden, never center.

At this height no movement names are legible and none try to be. What reads is
**shape**: where rivers thicken with tributaries, where a lane runs thin and
alone for centuries (the Caucasus), where the Latin West braids into many
channels after 1517. Six worlds sit on the landscape at full pigment — the six
Built & Live entries — small illuminated places on an otherwise graphite-ruled
survey. The eye finds them the way it finds the gilded initials on a page.

**The art, and where it's drawn from:** at full extent the period-art layer is
almost subliminal — each era band carries its texture at whisper strength, like
watermarks. The Era I band's texture is drawn from the **Dura-Europos
house-church** (Syria, an ordinary home converted for worship c. 233–256, the
earliest identified Christian church building — census `experienceToday`, House-
Churches entry); Era V's from the ashlar coursing of **Fontenay Abbey**
(Burgundy, founded from Clairvaux in 1118 — census, Cistercians entry); Era X's
from the weatherboard and plain brick of the **Apostolic Faith Mission at 312
Azusa Street, Los Angeles**, as it survives in the movement's own archival
photographs — the building where the era's first recorded key event (census:
*"Azusa Street Revival begins (1906)"*) took place. Each texture is sourced and
creditable — at this zoom you feel them as *grain*, not pictures.

**Text and data on screen:** the era names only, engraved in Cinzel small caps
along each band's left margin — the map's own artifact register — with dates
beneath in Alegreya Sans. One quiet line of chrome. Nothing else. The census's
scale (292 movements, 69 sourced connections) is *felt* as landscape, not
printed as a statistic.

**Alive, without moving:** entirely principle 3 at this height — the hand of
the maker. The bank lines waver by a hair's width the way ruled ink does; the
era grounds are washes with real pooling, not flat fills; the graphite
underdrawing of unbuilt rivers is visibly *drawing*. The felt promise, from the
capture's own diagnosis (§7): you can finally see the whole picture **and**
tell that there is somewhere to dive.

**Grounding:** census `meta` (292/69), `eras[].ground`, `movements[]`
lane/laneOrder fields, `post-apostolic-house-church.relationsSummary`; capture
§7 (scope diagnosis), §8 (rivers/lanes), §11 (stillness).

---

## Scene 2 — The descent into an era

*The participant pans north and zooms into the top of the sheet: Era I,
"The Early Church Era," 70–312 CE.*

**What the participant just did:** two slow pinches (or scroll-wheel steps),
both theirs. The camera never glides on its own — it goes exactly where the
hand sends it, at the speed the hand sends it, the way the current Atlas
already pans on mobile. The whole descent is the participant's own gesture;
the board holds still beneath it.

**On screen:** Era I now fills the view — the aged-parchment ground `#EFDDB3`
edge to edge. What was grain at full extent resolves into picture: the band's
background texture is now readable as what it is, and labeled as what it is.
The spring of the House-Churches sits upper center, and from it two watercourses
leave — and here the honest line-language does quiet, visible work:

- The course running east toward **Syriac Christianity (Edessa/Nisibis)**
  (200–410 CE) is drawn **dotted** — the census grades this `formed` edge
  *Contested*, with the note: *"Aramaic-speaking Christianity reached Edessa
  early, but by what route and hands scholars genuinely disagree."* The map
  draws a stream whose upper reach is dotted like a surveyed-but-unproven
  course. It does not pretend to know what scholars don't.
- The course running south toward **Alexandrian Catechetical / Christian-
  Platonist Tradition** (c. 150–400 CE) is drawn **dashed** — *Widely
  Accepted*: *"Egyptian Christianity's origins are obscure in detail, but its
  second-century emergence out of the same scattered network is broadly
  accepted."*

Lower in the band, at the seam where Era I gives way to Era II's cooler
vellum-green, a different kind of channel appears: **Imperial and Juridical
Christianity** (c. 312–451), which the census itself files not in a lane but on
the *bridge* between two (`laneOrder 3.5`, "Greek East / Latin West — bridge").
The art honors the data's own oddity: not a natural stream but an **engineered
channel** — straight banks, cut stone — running between the Greek East and
Latin West rivers. Empire building waterworks between watersheds. Nothing
dramatic; just a visibly different kind of line, because it *was* a different
kind of thing.

**The art, and where it's drawn from:** the era's backdrop, now legible, is
built from two real survivals, credited on hover like a wall label:

> *Baptistery wall paintings, Dura-Europos house-church, Syria, c. 233–256 —
> probably the oldest surviving Christian paintings anywhere; preserved because
> a Roman defensive rampart buried the building. On display at the Yale
> University Art Gallery.*

The texture takes the Dura paintings' own qualities — dry fresco on rough
plaster, terracotta and olive earth tones sitting naturally inside the muted
palette — and lets them ghost the band's ground at perhaps a tenth strength.
(One word policed hard in the art direction: the *paintings* may be faded — they
really are — but any human form inside the sourced art is presented as the
solid painted figure it is, never re-rendered translucent. Fidelity to the
artifact and anti-ghost turn out to be the same rule.)

**Text and data on screen:** the era's engraved title, its dates, and — set in
Alegreya italic beneath, like an argument-summary in a chapter head — the
census's own era tag: *"The apostles' children, under an empire that could turn
on them."* Movement names begin appearing along their courses at this depth,
lettered in italic along the rivers the way real maps letter real rivers.

**Alive, without moving:** principle 2 arrives — light with a time of day. The
Era I band reads as **lamplit interior**: the Dura texture behind the rivers
sits in a warm, low key, as if the whole era were seen by the oil lamps its
gatherings actually met by. The era doesn't glow. It is simply *lit the way its
rooms were lit* — which a participant feels before reading a single date, which
is exactly the "immediate visual cue" the capture's §11 resolved "richer" to
mean.

**Grounding:** census era 1 record (title, dates, tag, ground); edges
`post-apostolic-house-church → syriac-edessa-nisibis` (formed, Contested) and
`→ alexandria-catechetical` (formed, Widely Accepted), notes verbatim;
`imperial-juridical-christianity` lane 3.5 bridge record; House-Churches
`experienceToday` (Dura-Europos, Yale); capture §11 ("richer" resolved).

---

## Scene 3 — Arriving at a world: the Desert

*The participant follows the Africa river south out of Alexandria and zooms to
a single world: Desert Monasticism, c. 320–430 CE.*

**What the participant just did:** dragged the sheet upward (the camera runs
south along the Africa lane, but only because their finger pulled it), then
zoomed once more. The Nile-fed green of Alexandria's reach thins; the ground
under the river warms from parchment toward bare ochre. They have crossed from
Era I into Era II, and from a city into a desert, and both crossings happened
in the art before any label said so.

**On screen:** the tributary they followed is the census's own `formed` edge,
dashed for *Widely Accepted*, its note available at a touch: *"The desert
movement grew in Alexandria's shadow; Athanasius of Alexandria wrote the Life
of Antony that carried it to the world."* Where the tributary arrives, the
world itself sits on the landscape — and here is this draft's proposed answer
to the capture's open question of *what a world looks like sitting on the
terrain* **[PROPOSED — this draft]**: a world is drawn the way the old mappae
mundi drew cities — a **small architectural vignette at the riverbank**, an
illuminated site-mark, unmistakably a *place made for people*. For the Desert,
the vignette is drawn from the real place the census already cites:

> *The Monastery of Saint Anthony, Eastern Desert, Egypt — a Coptic Orthodox
> monastery grown up around Antony's own cave, still inhabited, open to
> visitors.* (census `experienceToday`)

Walled enclosure, cave mouth in the cliff behind, drawn solid in iron-gall
with an ochre wash. Beside the vignette, at full pigment because this world is
Built & Live, sits Papnoute's locked world emblem — the cracked jug.

**The hinted presence (anti-ghost, kept):** no monk is depicted. At the cave
mouth: a woven rope basket, mid-weave, set down. A water jug in the shade. A
worn footpath from the enclosure gate to the river, drawn as real desert paths
look — made by decades of feet. The path is the boldest single stroke in the
vignette. People are everywhere in this picture; none of them are shown, and
none of them are ghosts.

**Text and data on screen:** hover gives the glimpse card the product already
knows everywhere: name, dates (*c. 320–430 CE*), region (*Nile Valley &
Desert, Egypt*), status (*Open for conversation*), and — because the census
flags `living: true` — the living-tradition chip. Click gives the full panel:
the world's real tile text (*"communities who left settled village life to
wage a lifelong combat against the thoughts that trouble a person from
within"*), the real voices (Antony the Great, Pachomius, Amma Syncletica,
Evagrius Ponticus, John Cassian), and the honest sourcing line the census
already discloses on its tile: *"Small corpus, deep on inner combat."* Also on
the panel, drawn as small downstream course-lines: where this river goes —
`transmitted to` the Bethlehem Circle (*"Jerome and Paula toured the Egyptian
ascetic settlements"* — Documented, solid) and `formed` Byzantine monasticism
(*"Basil visited Egypt; the whole Greek monastic tradition claims the desert
as its root"* — Documented, solid). One tributary in; all later monasticism
out. The picture says it before the prose does.

**Alive, without moving:** principle 1 at full strength — evidence of use.
The basket mid-weave, the path worn deep, the jug in the shade at what is
plainly the hot hour. And principle 2: this vignette lives at **white noon**,
the one era-scene on the sheet lit mercilessly from above, because that is the
desert's true weather and it makes the cave's shade legible as mercy. Stillness
here is not a compromise — it *is* the content. This is the one world whose
whole discipline was learning to sit still in a cell, rendered by a map that
has, itself, learned the same.

**Grounding:** `desert-monasticism` full record (tile, voices, sourcing,
living flag, experienceToday); edges `alexandria-catechetical →
desert-monasticism`, `desert-monasticism → hieronymian-ascetic-literary`,
`desert-monasticism → iconophile-byzantine-monasticism`, notes verbatim;
world-icon spec (Papnoute · cracked jug, locked); capture §8 (open question:
what a world looks like on the landscape).

---

## Scene 4 — The quiet mark: hovering a real tension, then opening it

*Era V, "The High Medieval Era," 1054–1300. The participant notices a small
mark between two rivers and pauses on it.*

**What the participant just did:** panned down the sheet three era bands —
their own long, satisfying drag through five centuries — and stopped where the
Greek East & Orthodoxy river and the Latin West & Catholicism river run close.
In the band's pale vellum-green ground (`#E3E0CB`), between **The Byzantine
Church after the Schism** (1054–1300) and **The Latin Papal Church (Gregorian
Reform to Innocent III)** (c. 1049–1300), something small sits in the space
between the two courses.

**The mark itself [PROPOSED — this draft]:** the interaction mark, everywhere
on the sheet, is a **footbridge** — a tiny iron-gall bridge glyph at the point
where two rivers' stories actually touched, because a bridge is where people
cross, and interaction, in Mark's own words, *"would be key."* The mark's
modifiers are honest and quiet:

- **Contemporary contact** (`contemporary with`): the bridge whole.
- **Tension** (`in tension with`): the same bridge drawn **open at the
  center** — a span with a gap. Still a bridge. Still small.
- **Argument** (`argued against`): the open bridge with a small book-glyph at
  one end — because in this census, nearly every argument *is* a book (Against
  Eunomius, Against Praxeas, the Prose Refutations), and the full panel will
  name it.
- **Confidence**: the bridge's linework goes solid/dashed/dotted exactly as
  every other line on the map does.
- **Weight**: the mark grows only by an honest, computed property — how many
  sourced edges meet at that crossing — never by an editorial judgment of
  importance. (Off-screen but real: the census's Anomoean/Eunomian entry is
  argued against by the Cappadocians *and* the imperial church, and in tension
  with the Homoians — three sourced edges, so its crossing carries a visibly
  heavier mark than a single-edge crossing. Computed fact, not opinion.)

No rapids. No storm. No red. The mark between Rome and Constantinople — the
largest estrangement on the entire sheet — is a broken footbridge a few pixels
wide, drawn solid because the record is *Documented*. Humble transparency,
not front and center, exactly as the instinct recurs through the capture
(§3, §8).

**Hover (short):** a glimpse card, three lines —

> **The Great Schism** · in tension · Documented
> The Roman Church of the Reform Popes ↔ The Orthodox Church of Constantinople
> 1054 — *and it was not as simple as one date. Click for the record.*

**Click (full):** the panel opens with the census's own sourced note, whole and
unsoftened, museum-label register:

> *"The Great Schism, in each side's own documents: Humbert's bull of
> excommunication laid on the altar of Hagia Sophia (16 July 1054);
> Cerularius's synodal condemnation of the legates the following week. Process
> honesty: 1054 was symbolic and legate-to-patriarch, not church-to-church;
> the 1204 sack of Constantinople sealed the estrangement (scholars dating the
> real rupture there — that reading Contested); the anathemas were mutually
> lifted in 1965."*

The panel renders that note's own internal honesty visually: the 1054 line
solid, the "real rupture at 1204" reading dotted — the map keeps its
line-language even inside a single record. And the last clause sits at the
bottom of the panel in the smallest honest type: *the anathemas were mutually
lifted in 1965.* Nine hundred years wide, and the record's own final word is a
quiet un-saying. The design does nothing to amplify any of this. It doesn't
need to.

**The counterweight, one band up:** so that the bridge-mark never reads as
"the conflict symbol," the same mark appears in Era II between the Cappadocian
and Bethlehem-Circle courses — **whole**, solid, Documented — for the census
edge whose note is simply: *"Jerome heard Gregory of Nazianzus teach in
Constantinople and calls him his teacher."* Most bridges on this sheet are
whole. That is itself an honest, findable fact about the data: of 69 edges,
47 are formation and transmission, 6 are contact, 16 are tension or argument.
The landscape's own arithmetic is mostly gift.

**Alive, without moving:** the mark's aliveness is principle 3 — it is
*inscribed*, a deliberate small act of the mapmaker's hand at a real crossing,
with the slight press-weight of a nib start and stop. And the restraint itself
reads as life: a still, small mark over a nine-century wound is the visual
grammar of a witness who was actually there and does not need to raise their
voice.

**Grounding:** edge `latin-papal-church-gregorian ↔ byzantine-church-after-1054`
(in tension with, Documented, note verbatim); edge
`cappadocian-nicene-pastoral-monastic-tradition ↔ hieronymian-ascetic-literary`
(contemporary with, Documented, note verbatim); Eunomian edge-count from census
edges; type/confidence counts computed from `edges[]`; capture §3 & §8
("humble, not front-and-center," mark carries scale by honest property only);
existing hover/click grammar (Full UX Design §2.4).

---

## Scene 5 — The river that keeps its bed: one lineage, Edessa to Xi'an

*The participant follows the easternmost river down the whole sheet.*

**What the participant just did:** zoomed part-way back out — their choice,
their hands — until three era bands fit the frame, then panned slowly down the
Syriac East & Asia lane at the sheet's eastern edge, riding one river across
six centuries.

**On screen:** the longest single demonstration on the map of what `continuesAs`
means. The river never forks here and never ends here — it **keeps its bed and
changes its name**, four times, exactly as the census records:

1. **Syriac Christianity (Edessa/Nisibis)**, 200–410 — the name lettered in
   italic along the course, as maps letter rivers.
2. At the reach where the record turns, a **boundary stone on the bank** —
   this draft's proposed rendering of a `continuesAs` seam **[PROPOSED — this
   draft]**: a small inscribed stone, dated, at the waterline; the old
   lettering ends, and downstream the same river carries a new name:
   **Persian Church of the East (early)**, to 451. The `formed` edge's note is
   on the stone's hover: *"The School of Nisibis and the Persian church carry
   this tradition's teaching directly onward after 410"* — Documented, solid.
3. A second stone at 424 — the year the bishops of Persia declared their
   catholicos answered to no bishop beyond their frontier — and the name
   becomes **The Church of the East under Persia**, 424–651.
4. A third stone, and the name becomes **The Church of the East on the Silk
   Road**, c. 635–845 — the reach the census itself calls *"the map's longest
   single lineage line (Edessa to Xi'an)."*

The model for those boundary stones is not invented. It is the artifact this
very river ends at, credited like the wall label it deserves:

> *The Xi'an Stele, erected 781, inscribed in Chinese and Syriac, narrating a
> century and a half of what it calls the Luminous Religion in China — the
> monument recording Christianity's first arrival in China. On display in the
> Beilin Museum (the Forest of Steles), Xi'an.* (census `experienceToday`)

So the map's own seam-marker glyph is quietly *derived from a real stone this
tradition actually carved to mark its own continuity* — the kind of rhyme
between rendering and record this whole draft is reaching for.

**The honest fade:** the census grades this reach's sourcing plainly —
*"spectacular fragments (Xi'an stele, Dunhuang/Turfan texts) over long silent
stretches"* — and the art obeys: between the bright, solidly-drawn points, the
course's line relaxes toward the dashed and dotted registers. The river is
confident where the record is confident and candid where it is not. In 845 —
the imperial edict against foreign religions, the movement's own recorded end
date for this window — the drawn course stops. Not a dramatized drying-up; the
inked line simply ends at the year the record ends, with the stone that
explains why.

**Text and data on screen:** hovering any reach gives the glimpse card for
that window's movement (name, dates, region, status); hovering a stone gives
the `continuesAs` line and the edge note; clicking opens the full record. The
one long ride tells a participant, wordlessly, something the current
spreadsheet-shaped view could never make felt: that four entries in a table
are **one river**, and that a church whose bishops sat in Persia once watered
ground at the Tang court of Chang'an.

**Alive, without moving:** this is the treasure-hunt scene (capture §3 —
*"the wow of discovery… finding what you didn't know was there"*). The
aliveness is the *arrival*: after two quiet, honest, dashed centuries of
eastward course, the backdrop texture at the river's end resolves into the
stele's own carved surface — cross rising above cloud and lotus, rendered as
rubbing-texture in iron-gall, the way Chinese steles have actually been read
for centuries: by hand, with paper and ink. Principle 3 again — the mark of
real hands, this time hands from 781.

**Grounding:** `syriac-edessa-nisibis` → `persian-church-of-the-east-early` →
`the-church-of-the-east-under-persia` → `the-church-of-the-east-on-the-silk-road`
`continuesAs` chain, all four records' dates/regions verbatim; edge
`syriac-edessa-nisibis → the-church-of-the-east-under-persia` note; Silk Road
entry's sourcing line and 845 end; Xi'an Stele from `experienceToday`; capture
§8 (continuesAs = same river, new name).

---

## Scene 6 — Inside one world: the House-Churches, at deepest zoom

*The participant returns to the spring at the top of the map and zooms all the
way in — deeper than any scene so far — until one world becomes its own small
terrain.*

**What the participant just did:** the final zoom depth. Out at full extent the
Atlas was a landscape of rivers; at era depth it was a band with courses and
marks; at world depth it was a site-vignette by a river. One deliberate pinch
further, on a Built & Live world only, and the vignette **opens** — the world
becomes the whole frame, standing on its own ground, with its own features.
Everything shown at this depth comes from the world's own construction record,
because for the six live worlds that record actually exists.

**On screen — the world's own terrain [PROPOSED — this draft]:** for
Post-Apostolic House-Church Christianity, the deepest view is a quarter — a
few streets of a Roman-era neighborhood seen at rooftop height, drawn solid in
the manuscript register on the Era I ground. Its features are the world's own
**gravities**, as its finalized Gravity Discovery (Doc_04) actually classified
them — the two Primary gravities drawn as the terrain's two organizing
features, the Supporting ones present and smaller, exactly mirroring the
record's own proportions:

- **The table (G07 — Liturgical Practice, Primary).** At the quarter's heart,
  an ordinary dining room with the fourth wall open, drawn from the only kind
  of building this world had — a house. A table laid: bread broken, the shared
  cup (Chloe's locked emblem, here at last in its native size), a lamp. The
  benches pushed back, not tucked in. Someone was just here.
- **The letter-roads (G02 — Translocal Correspondence Network, Primary).**
  From the quarter's edges, roads lettered with real destinations — Antioch,
  Smyrna, Corinth, Rome — and on the table by the door, the network made
  object: letters, unfolded, creases showing. The record's proudest small
  fact sits on hover: Polycarp bundling Ignatius's letters for Philippi is
  *"a specific, directly attested transmission event, named by the person who
  performed it, in his own surviving letter"* (Doc_09, Tier 1).
- **The smaller features, honestly scaled.** A workshop back-room fitted with
  benches (the census: gatherings met in *"a member's dining room or the back
  of a workshop"*); above a bathhouse, a rented upper room with writing
  materials — Justin Martyr's school, straight out of the census's own
  description. And present, but deliberately small and unspotlit, the
  Supporting gravity of state pressure: a street door, solid, closed, with a
  lamp burning behind its crack. That is the whole rendering. The record
  underneath is one click away and does not flinch — Pliny's interrogation,
  and the fact the world's own story inventory states plainly: its single
  most granular detail of worship *"was extracted from two enslaved women,
  called ministrae, under torture."* Present, honestly findable, never a hook.
  This is §3 of the capture, kept: *"honest accessibility for those who are
  searching for truth, not hype."*

**The art, and where it's drawn from:** the backdrop at this depth is the
world's own real room — the Dura-Europos house-church again, now at full
legibility and full credit (converted home, c. 233–256; baptistery paintings
at Yale — both already in this world's census record). The rendering keeps
Dura's plaster texture and earth palette; the label says what is artifact and
what is this project's own drawing, the way the world-icons already flag
DOCUMENTED / INFERENCE / SILENT.

**Text and data on screen:** the full panel at this depth is the world's front
door: the tile text, the real voices (Ignatius, Clement of Rome, Polycarp,
Justin Martyr — and the census's own fifth line, kept verbatim because it is
the most house-church sentence ever written: *"the gatherings met in the homes
of people history did not bother to write down"*), the sourcing disclosure
(*"communal voice rich, individual interior voice thin"*), and the world's
existing actions — **Have an interview / Join a conversation** — the same
deep-link contract the product already keeps, so the Atlas stays what the
capture's §13 requires: a door that opens both ways, never a dead end.

**Alive, without moving:** all three principles converge. Evidence of use
everywhere (the pushed-back bench, the broken bread, the unfolded letters);
lamplight as real weather (this world met at night and before dawn, and its
deepest view is lit accordingly — light on walls and bread, never an aura);
and the maker's hand in every line. No person depicted, and yet the whole
frame is warm with people — which was Mark's stated heart for "alive" in the
first place: *"not experiencing old dead worlds, but getting a glimpse of
life, theology and practices lived."*

**Grounding:** `post-apostolic-house-church` full census record (tile, voices,
longDescription details, sourcing, experienceToday); World-Builds/01 Doc_04
FINAL (G02 and G07 Primary; G01/G03/G04 Supporting; G05 Tensional); Doc_09
Story Inventory (Polycarp transmission, Tier 1; Pliny interrogation disclosure);
locked icon spec (Chloe · shared cup); capture §3 (hardship posture), §13
(plug-and-play door).

---

## Scene 7 — The bottom edge: where the rivers leave the map

*The participant pans all the way down. The sheet ends. Some rivers don't.*

**What the participant just did:** one long pull downward, through the
Missionary Era's cool band into the Global Church Era's warm ground
(`#EFDDB3` again — the sheet ends on the same warmth it began on, which is not
an accident anyone needs explained to them). Then the pan stops, because the
parchment stops.

**On screen:** the bottom edge of the map, Era X, *"The center of gravity
moves south and east"* (the census's own era tag). And the one place on the
whole sheet where the rendering makes a distinction the data has been carrying
all along: the `living` flag. Rivers whose windows closed in the past have
ended, honestly, at their recorded end-years upstream. But rivers the census
marks living reach the parchment's edge **still inked at full confidence — and
run off it**. The bank lines go to the deckle edge and stop only because the
paper does. A map can end; it would be a lie for the river to.

Along that edge, small and credited, the proof the census already carries in
its `experienceToday` fields — the places where a participant could stand,
this year, in the current of something that entered the map's top edge:

> *The Monastery of Saint Anthony, Eastern Desert, Egypt — grown up around
> Antony's own cave, still inhabited.* (The Desert's river: entered the map
> c. 320.)
> *Mor Gabriel Monastery, Tur Abdin — founded 397, still a working monastery.*
> (The Syriac river: entered c. 200.)

**Text and data on screen:** hover on any river at the edge gives the
living-tradition chip and the world's *experience today* line — the same
honest register as everywhere else. Click gives the full record. Nothing new
is invented at the edge; the edge just lets the data's own `living: true`
finally *look like something*.

**Alive, without moving:** this scene is the thesis. Nothing here animates —
and the stillness is what makes the claim serious. A shimmering river says
"an app is running." A still river inked clean off the edge of a
two-thousand-year map, next to a label naming the real monastery where its
water can be visited today, says what the project actually believes: this is
a *visual way to see Jesus at work across history and today* (capture §1,
Mark's own words) — and *today* is not a special effect.

**Grounding:** era 10 record (dates, tag, ground); `living` flags and
`experienceToday` entries for `desert-monasticism` and `syriac-edessa-nisibis`;
capture §1 (the heart of it), §11 (stillness).

---

## Closing — five headlines, offered for the open question

The capture (§8, §14) leaves open what a "headline" would actually say — a
punchier, more human framing than a formal name, for a world or an era. These
five are offered as concrete candidates, each derived from a real census line
(cited), none inventing a fact. They would live where the formal name lives
now, with the formal name one breath beneath — headline in Alegreya italic,
formal name in small caps under it.

1. **"The church before it had buildings."** — Post-Apostolic House-Church
   Christianity. *Derived from its own longDescription: "Christianity had no
   buildings of its own… it had houses."*
2. **"They went out to fight what was inside."** — Desert Monasticism.
   *Derived from its tile: "left settled village life to wage a lifelong
   combat against the thoughts that trouble a person from within."*
3. **"One river, Edessa to Xi'an."** — The Church of the East on the Silk
   Road. *Derived from its relationsSummary: "the map's longest single lineage
   line (Edessa to Xi'an)."*
4. **"An empire that could turn on them."** — Era I, The Early Church Era.
   *Trimmed directly from the era's own census tag.*
5. **"The church moves south."** — Era X, The Global Church Era. *Derived from
   its tag: "The center of gravity moves south and east."*

A rule worth adopting if any of these survive review **[PROPOSED — this
draft]**: every headline must be derivable from a line already in the census
or the world's own construction record, the way all five above are — so the
punchier register never becomes a side door for unsourced claims.

---

## What this draft deliberately does not do

No tool is named, no architecture sketched, no build increment proposed — per
the brief. The scenes above are pictures for Mark to react to. Where a scene
answers a question the capture left open (what a world looks like on the
terrain; what a `continuesAs` seam looks like; what makes still art alive; the
footbridge mark; the compass placement of lanes; the headline rule), the answer
is marked **[PROPOSED — this draft]** and stands ready to be kept, bent, or
struck in the convergent phase.

---

## Document log

- **DRAFT (2026-08-31):** First creative pass, produced by a Fable-model
  session at Mark's request, same day as the divergent-capture it builds on.
  Sources read in full before drafting: the Divergent Capture V1.1, the live
  `world-census.json` (V0.20), Full UX Design V1.0 §2 (palette, typography,
  anti-ghost) — plus the Full UX Storyboard V1.0 for voice precedent, and the
  House-Churches world's own Doc_04/Doc_09 finals for Scene 6's features.
  Sandbox only; touches nothing live; decides nothing.
