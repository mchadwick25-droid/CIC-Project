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

**The whole ecology, marked where it's built — the founding principle, stated
plainly.** Mark's own words: *"we are building for all the worlds, build and
not, just the built worlds are marked so they can dive deeper. as we build
more worlds we mark those and deepen their content as they come online, but
the base program is about the entire ecology, not the build worlds."* This
storyboard is not a map of six built worlds with placeholders around them —
it is a map of the real, whole census as it stands today, in which "built" is
one honest attribute a movement can carry (it unlocks deeper content and a
live conversation), never the organizing principle of what the map shows.
That is why this draft walks all ten eras rather than the six worlds that
happen to be built, and why Eras III–X are drawn in full, honest graphite
detail rather than left thin or skipped. As more worlds are built, they get
marked and deepened in place — the map's own scope does not grow to catch up
with the build; it was already whole.

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

**How the scenes walk — the structure, fixed at Mark's direction.** Ten scenes,
Scene I through Scene X: **one for each of the census's ten eras, in order**,
top of the sheet to bottom. Each scene is that era's own — its real title,
dates, tag, ground color, and the real movements and edges the census actually
files in it. One honest fact governs how the ten differ: as of V0.20, **all six
Built & Live worlds sit in Eras I and II; Eras III through X hold none yet.**
So the first two scenes arrive at inhabited, full-pigment worlds, and the
remaining eight are drawn entirely in the graphite-underdrawing register — real
names, real dates, real sourced marks, ruled but not yet inked. That is not
eight lesser scenes. It is the survey rendered honestly, and several of the
strongest pictures below live in the graphite.

---

## Scene I — Era I: The Early Church Era, 70–312 CE

*"The apostles' children, under an empire that could turn on them" (the era's
own census tag). Ground: warm aged parchment `#EFDDB3`. The participant arrives,
and descends to the spring.*

**What the participant just did:** clicked through from wherever they were —
the homepage, the end of a conversation — and the Atlas opened at full extent:
the whole sheet at once, ten bands descending through their warm→cool→warm
cadence, seven family lanes plus the headwater, six small full-pigment worlds
on an otherwise graphite-ruled survey, found by the eye the way it finds gilded
initials on a page. At the far margin, ruled off like a mapmaker's marginal
table, the Beyond-the-Floor terrain (the census's lane 80, "Non-Nicene
Traditions," researched and explained) — present, labeled, never hidden, never
center. Then two slow pinches, both theirs — the camera goes exactly where the
hand sends it, at the speed the hand sends it — and Era I fills the view. The
board holds still beneath the whole descent.

**On screen:** the band's engraved Cinzel title and dates along the left
margin, the tag beneath in Alegreya italic, and the era's own `keyEvents` set
small along the margin rule — *Destruction of the Temple (70) · Decian
persecution (250) · Great Persecution begins (303)*. Upper center, a single
spring: **Post-Apostolic House-Church Christianity** (70–200 CE), the census's
own `laneOrder 0`, its lane labeled in the data itself *"Origin — before the
lanes divide,"* its `relationsSummary` reading, verbatim, *"Parent of nearly
everything on the map."* At this depth that is simply what the picture shows —
one spring, and the watercourses leaving it, each wearing the honest
line-language of its real edge:

- East toward **Syriac Christianity (Edessa/Nisibis)** (200–410 CE, Built &
  Live, full pigment): drawn **dotted** — the census grades this `formed` edge
  *Contested*, note verbatim: *"Aramaic-speaking Christianity reached Edessa
  early, but by what route and hands scholars genuinely disagree."*
- South toward **Alexandrian Catechetical / Christian-Platonist Tradition**
  (c. 150–400 CE, Built & Live, full pigment): drawn **dashed** — *Widely
  Accepted*: *"Egyptian Christianity's origins are obscure in detail, but its
  second-century emergence out of the same scattered network is broadly
  accepted."*
- West toward **The Roman Church of the Third Century** (graphite): dashed —
  *"The Roman congregation of the house-church period is the same community,
  two generations on."*
- And a short solid course to **The Greek Apologists** (graphite, Documented):
  *"The same Christians, turned outward."*

**Arriving at the world [PROPOSED — this draft]:** one deliberate pinch further,
on a Built & Live world only, and the world opens. A world sits on the terrain
the way the old mappae mundi drew cities — a **small architectural vignette at
the riverbank**, an illuminated site-mark, unmistakably a *place made for
people* — and at deepest zoom the vignette becomes the whole frame: the world's
own small terrain, its features drawn from the world's own finalized
construction record. For the House-Churches, a few streets of a Roman-era
neighborhood at rooftop height, organized by the two Primary gravities its
Gravity Discovery (Doc_04) actually classified:

- **The table (G07 — Liturgical Practice, Primary).** An ordinary dining room
  with the fourth wall open — the only kind of building this world had. Bread
  broken, the shared cup (Chloe's locked emblem, here at its native size), a
  lamp, the benches pushed back, not tucked in. Someone was just here.
- **The letter-roads (G02 — Translocal Correspondence Network, Primary).**
  Roads lettered with real destinations — Antioch, Smyrna, Corinth, Rome — and
  by the door, the network made object: letters, unfolded, creases showing.
  On hover, the record's proudest small fact: Polycarp bundling Ignatius's
  letters for Philippi is *"a specific, directly attested transmission event,
  named by the person who performed it, in his own surviving letter"*
  (Doc_09, Tier 1).
- **The smaller features, honestly scaled:** a workshop back-room fitted with
  benches (the census: gatherings met in *"a member's dining room or the back
  of a workshop"*); a rented upper room with writing materials — Justin's
  school; and, small and unspotlit, the Supporting gravity of state pressure:
  a street door, solid, closed, a lamp burning behind its crack. The record
  underneath is one click away and does not flinch — Pliny's interrogation,
  and the story inventory's plain statement that this world's single most
  granular detail of worship *"was extracted from two enslaved women, called
  ministrae, under torture."* Present, honestly findable, never a hook —
  capture §3, kept: *"humble transparency that isn't front and center."*

**The art, and where it's drawn from** — credited on hover like a wall label:

> *Baptistery wall paintings, Dura-Europos house-church, Syria, c. 233–256 —
> an ordinary home converted for worship, the earliest identified Christian
> church building, preserved because a Roman defensive rampart buried it;
> the paintings, probably the oldest surviving Christian paintings anywhere,
> are on display at the Yale University Art Gallery.* (census
> `experienceToday`, both entries)

The band's texture takes the Dura paintings' own qualities — dry fresco on
rough plaster, terracotta and olive earths already inside the muted palette —
at whisper strength behind the rivers, at full legibility and full credit
inside the opened world. One word policed hard: the *paintings* may be faded —
they really are — but any human form inside the sourced art stays the solid
painted figure it is, never re-rendered translucent. Fidelity to the artifact
and anti-ghost turn out to be the same rule.

**Text and data on screen:** hover gives the glimpse card the product already
knows everywhere (name, dates, region, status); click gives the world's front
door — the tile text, the real voices (Ignatius, Clement of Rome, Polycarp,
Justin Martyr, and the census's own fifth line, kept verbatim because it is
the most house-church sentence ever written: *"the gatherings met in the homes
of people history did not bother to write down"*), the sourcing disclosure
(*"communal voice rich, individual interior voice thin"*), and the existing
actions — **Have an interview / Join a conversation** — the same deep-link
contract the product already keeps, so the Atlas stays a door that opens both
ways, never a dead end (capture §13).

**Alive, without moving:** all three principles converge at the spring.
Evidence of use everywhere; lamplight as real weather — this world met at
night and before dawn, and its view is lit accordingly, light on walls and
bread, never an aura; and the maker's hand in every ruled line. No person
depicted, and the whole frame warm with people — Mark's stated heart for
"alive": *"not experiencing old dead worlds, but getting a glimpse of life,
theology and practices lived."*

**Grounding:** census era 1 record (title, dates, tag, ground, keyEvents);
`post-apostolic-house-church` full record (lane/laneLabel, relationsSummary,
tile, voices, longDescription, sourcing, experienceToday); edges
`post-apostolic-house-church → syriac-edessa-nisibis` (Contested),
`→ alexandria-catechetical` (Widely Accepted), `→ roman-church-third-century`
(Widely Accepted), `→ greek-apologists-second-century` (Documented), notes
verbatim; World-Builds/01 Doc_04 FINAL (G02, G07 Primary); Doc_09 Story
Inventory (Polycarp transmission Tier 1; Pliny disclosure); locked icon spec
(Chloe · shared cup); capture §3, §7, §11, §13.

---

## Scene II — Era II: The Imperial Church Era, 312–451 CE

*"From Constantine's revolution to Chalcedon" (the era's tag). Ground: pale
vellum-green `#E3E0CB`. Three Built & Live worlds sit in this one band — the
Desert, Church and Empire, the Bethlehem Circle. The scene arrives at the
Desert and lets the other two stand as real, named, connected neighbors.*

**What the participant just did:** dragged the sheet upward — the camera runs
south along the Africa lane only because their finger pulled it — following
the census's own `formed` edge out of Alexandria, dashed for *Widely Accepted*,
its note at a touch: *"The desert movement grew in Alexandria's shadow;
Athanasius of Alexandria wrote the Life of Antony that carried it to the
world."* The Nile-fed green thins; the ground under the river warms from
parchment toward bare ochre. They crossed an era seam and a city's edge, and
both crossings happened in the art before any label said so. The era's
keyEvents sit small on the margin rule: *Edict of Milan (313) · Council of
Nicaea (325) · Sack of Rome by the Visigoths (410)*.

**On screen — the world at the riverbank:** where the tributary arrives,
**Desert Monasticism** (c. 320–430 CE, Built & Live) sits at full pigment as a
site-vignette drawn from the real place the census already cites:

> *The Monastery of Saint Anthony, Eastern Desert, Egypt — a Coptic Orthodox
> monastery grown up around Antony's own cave, still inhabited and open to
> visitors.* (census `experienceToday`)

Walled enclosure, cave mouth in the cliff behind, drawn solid in iron-gall
with an ochre wash. Beside it, Papnoute's locked world emblem — the cracked
jug.

**The hinted presence (anti-ghost, kept):** no monk is depicted. At the cave
mouth: a woven rope basket, mid-weave, set down. A water jug in the shade. A
worn footpath from the enclosure gate to the river, drawn as real desert paths
look — made by decades of feet. The path is the boldest single stroke in the
vignette. People are everywhere in this picture; none of them are shown, and
none of them are ghosts.

**The era's other two live worlds, real and connected:** lower in the band,
where the Greek East and Latin West rivers run closest, the census's own
oddity is honored — **Imperial and Juridical Christianity** (c. 312–451) is
filed not in a lane but on the *bridge* between two (`laneOrder 3.5`, "Greek
East / Latin West — bridge"), and the art draws it as what it was: not a
natural stream but an **engineered channel** — straight banks, cut stone —
empire building waterworks between watersheds. Its site-mark is its own real
survival: *the Archbasilica of St John Lateran, Rome — founded under
Constantine in the 320s and still the cathedral church of the bishop of Rome*
(census `experienceToday`). And on the Latin West's eastern reach, **the
Bethlehem Circle** (Hieronymian Ascetic-Literary Christianity, c. 382–420),
its site-mark *the Church of the Nativity and the Pilgrimage Route, Bethlehem
— the UNESCO World Heritage site whose underground caves include the one long
shown as Jerome's study* (census `experienceToday`). Two real edges tie the
Desert to it and beyond, both Documented, both solid: *"Jerome and Paula
toured the Egyptian ascetic settlements"* (`transmitted to`), and — flowing
out of the band entirely — *"Basil visited Egypt; the whole Greek monastic
tradition claims the desert as its root"* (`formed`, toward Byzantine
monasticism far downstream). One tributary in; all later monasticism out. The
picture says it before the prose does.

**A small mark, seen here first [PROPOSED — this draft]:** between the
Cappadocian course and the Bethlehem Circle sits a tiny iron-gall
**footbridge** — whole, solid, Documented — for the census edge whose note is
simply: *"Jerome heard Gregory of Nazianzus teach in Constantinople and calls
him his teacher."* A bridge is where people cross. This is the interaction
mark's first appearance on the walk down the sheet, and it appears the way
most of the sheet's bridges are: **whole**. The full mark grammar — including
what tension and argument do to it — is specified where the sheet's largest
crossing demands it, in Scene V.

**Text and data on screen:** hover gives the glimpse card (name, dates,
region *Nile Valley & Desert, Egypt*, status *Open for conversation*, and the
living-tradition chip, because the census flags `living: true`). Click gives
the full panel: the real tile text (*"communities who left settled village
life to wage a lifelong combat against the thoughts that trouble a person from
within"*), the real voices (Antony the Great, Pachomius, Amma Syncletica,
Evagrius Ponticus, John Cassian), and the honest sourcing line: *"Small
corpus, deep on inner combat."*

**Alive, without moving:** principle 1 at full strength — the basket
mid-weave, the path worn deep, the jug in the shade at what is plainly the hot
hour. And principle 2: this vignette lives at **white noon**, the one scene on
the sheet lit mercilessly from above, because that is the desert's true
weather and it makes the cave's shade legible as mercy. Stillness here is not
a compromise — it *is* the content. This is the world whose whole discipline
was learning to sit still in a cell, rendered by a map that has, itself,
learned the same.

**Grounding:** census era 2 record (title, dates, tag, ground, keyEvents);
`desert-monasticism` full record (tile, voices, sourcing, living flag,
experienceToday); `imperial-juridical-christianity` lane 3.5 bridge record and
experienceToday; `hieronymian-ascetic-literary` record and experienceToday;
edges `alexandria-catechetical → desert-monasticism`, `desert-monasticism →
hieronymian-ascetic-literary`, `desert-monasticism →
iconophile-byzantine-monasticism`,
`cappadocian-nicene-pastoral-monastic-tradition → hieronymian-ascetic-literary`,
notes verbatim; world-icon spec (Papnoute · cracked jug, locked); capture §8.

---

## Scene III — Era III: The Age of Monks and Empires, 451–622

*"The communions take their lasting shapes after Chalcedon" (the era's tag).
Ground: cool pale blue-grey `#D8E4E5`. The first band with no Built & Live
world — and the first scene drawn wholly in graphite underdrawing. Nothing
here pretends otherwise; everything here is real.*

**What the participant just did:** one steady pull downward, across the seam
where the vellum-green cools into blue-grey. The pigment washes of the two
inhabited bands give way to the ruled survey: bank lines and course names in
graphite, era title engraved as everywhere else, keyEvents on the margin —
*Fall of Rome (476) · Benedict's Rule (c. 530) · Justinian's Plague begins
(541)*. Nothing is hover-dead. The band simply looks like what it is: ruled,
not yet inked.

**On screen — the row of stones:** the band opens with the most legible single
fact the census records about this era: at its top edge, several rivers change
names at once. A `continuesAs` seam is drawn as a **small inscribed boundary
stone at the waterline [PROPOSED — this draft]** — dated, lettered, the old
name ending upstream and the same bed carrying a new name down. (The glyph's
model is not invented; it is derived from a real stone one band further down
the sheet, credited in full in Scene IV.) Across the band's top, the stones
stand in a quiet row, each one a real census chain: the Armenian river's stone
at 451 (**Armenian Christianity after Avarayr**, 451–554); the Egyptian
river's (**Cyrilline / Miaphysite Egyptian Christianity**, 451–642); and
slightly upstream of the era line, the Church of the East's stone at 424 —
the year, per the census's own longDescription, *"the bishops of the Persian
Empire declared that their catholicos at Seleucia-Ctesiphon answered to no
bishop beyond their own frontier"* (**The Church of the East under Persia**,
424–651, carrying forward the Documented edge from Edessa: *"The School of
Nisibis and the Persian church carry this tradition's teaching directly
onward after 410"*). The era's tag is not asserted anywhere as prose overlay;
the row of stones *is* the tag, drawn.

**The featured course — the desert goes west:** across the band's Latin reach
runs the era's richest sourced chain, every link Documented and solid, every
note the census's own:

1. Out of Era II's Desert: *"John Cassian lived among the Egyptian monks
   before founding his houses at Marseilles; the Institutes and Conferences
   are that transmission in written form"* (→ Gallic monastic-ascetic
   Christianity).
2. Gaul to Italy: *"Benedict's Rule commends Cassian's Conferences by name
   and prescribes them as daily reading"* (→ **Early Benedictine / Italian
   Monasticism**, c. 500–604).
3. Italy to Rome: *"Gregory was a monk of his own foundation on the Caelian
   before he was bishop, and wrote the only life of Benedict there is"*
   (→ **The Roman Church in the Age of Gregory the Great**, c. 560–604).
4. And out of the band's bottom edge, a course already leaving for the next
   era: *"Gregory sent Augustine and forty monks to Kent in 596 and directed
   the mission by letter for the rest of his life"* (→ Anglo-Saxon
   Christianity, Era IV).

One desert, one visitor, one short rule, one monk-bishop — and the whole
Latin monastic line. The census's own teaser for the Benedictine entry sits
on its glimpse card: *"a short, practical rule for a single household of
monks, written while the peninsula was being fought over, that ended up
organizing Western monastic life for fifteen centuries."*

**A quiet mark:** near the band's end, between the Roman course and the
Justinianic Byzantine course, a footbridge drawn **open at the center** — the
census's `in tension with` edge, Documented, its note carried whole: *"Gregory
refused the patriarch of Constantinople's title of universal bishop and
answered it by calling himself servant of the servants of God."* No storm, no
red. A small gap in a small bridge, and a sentence a participant will not
forget.

**The art, and where it's drawn from** — the band's site-marks are graphite
vignettes of real places the census itself cites:

> *The Abbey of Monte Cassino, Italy — Benedict's own foundation of around
> 529, destroyed and rebuilt many times over and again a working monastery.*
> (census `experienceToday`, Early Benedictine entry)

with, standing real and named along the band's other courses, *the Basilica
of San Vitale, Ravenna — completed in 547, with the mosaic portraits of
Justinian and Theodora facing each other across the sanctuary* (Justinianic
entry), *Mar Saba in the Kidron valley — founded by Sabas in 483 and
inhabited by monks almost continuously since* (Judean Desert entry), and
*Iona Abbey, on the site Columba founded in 563* (Insular Irish entry — whose
own dashed course back to the desert reads *"Via Gaul (Lérins, Martin of
Tours); the route is secure in outline, thinner in specifics"*).

**Text and data on screen:** every glimpse card in this band carries its
honest status line from the census's own vocabulary — *"Researched — strong
candidate"* — and the era record's own caution renders as one quiet chrome
line: entries here carry signals, not verdicts. Dimmed is an honest state,
not a disabled state; the cards open, the notes read, the sources stand.

**Alive, without moving:** principle 1, carried by a book — the one object
this era's featured chain keeps handing forward. A rule *prescribed as daily
reading* is evidence of use by definition. And principle 2: the band sits in
**grey first light**, the hour of vigils, the monastic day's true beginning —
cool light on cool ground, which the blue-grey `#D8E4E5` was already waiting
to hold.

**Grounding:** census era 3 record (title, dates, tag, ground, keyEvents,
rec); `continuesAs` chains into `armenian-christianity-after-avarayr`,
`cyrilline-miaphysite-egyptian-christianity`,
`the-church-of-the-east-under-persia` (longDescription, 424, verbatim); edges
`desert-monasticism → gallic-monastic-ascetic-christianity`,
`gallic-monastic-ascetic-christianity → early-benedictine-italian-monasticism`,
`early-benedictine-italian-monasticism → roman-church-gregorian`,
`roman-church-gregorian → anglo-saxon-christianity`,
`roman-church-gregorian ↔ byzantine-imperial-church-justinianic`,
`desert-monasticism → insular-irish-monastic-christianity`, notes verbatim;
experienceToday entries for `early-benedictine-italian-monasticism`,
`byzantine-imperial-church-justinianic`,
`chalcedonian-monasticism-judean-desert-and-gaza`,
`insular-irish-monastic-christianity`; statusWord vocabulary from census.

---

## Scene IV — Era IV: The Early Medieval Era, 622–1054

*"Christianity under new empires, from Ireland to China" (the era's tag).
Ground: warm parchment `#EFDDB3`. The longest band on the sheet — four
hundred and thirty-two years — and the widest picture: the participant rides
one river to the sheet's far eastern edge.*

**What the participant just did:** zoomed part-way back out — their choice,
their hands — until the whole band fits the frame, then panned slowly east
along the Syriac East & Asia lane, riding the river whose boundary stone they
met in Scene III. The keyEvents on the margin say what kind of centuries
these are: *Rise of Islam (622) · Viking raid on Lindisfarne (793) ·
Charlemagne crowned emperor (800)*.

**On screen — the longest single lineage line on the map:** the river keeps
its bed and changes its name — a stone at the era seam, and the course
becomes **The Church of the East on the Silk Road** (c. 635–845), the reach
the census's own relationsSummary calls *"the map's longest single lineage
line (Edessa to Xi'an)."* Its record, carried onto the panel verbatim: in 635
*"a missionary the Chinese records call Alopen reached the Tang capital of
Chang'an and was received at the imperial court."* And here the boundary-stone
glyph pays its debt, because the model for every `continuesAs` stone on the
sheet is the artifact this river ends at, credited like the wall label it
deserves:

> *The Xi'an Stele, Beilin Museum (the Forest of Steles), Xi'an — the 781
> monument recording Christianity's first arrival in China, inscribed in
> Chinese and Syriac, narrating a century and a half of what it calls the
> Luminous Religion, still on display.* (census `experienceToday`)

**The honest fade:** the census grades this reach's sourcing plainly —
*"spectacular fragments (Xi'an stele, Dunhuang/Turfan texts) over long silent
stretches"* — and the graphite obeys: between the firmly-drawn points the
course relaxes toward the dashed and dotted registers. In 845 the drawn
course stops, at the year the census's own dateRationale fixes — *"Huichang
edict laicizes foreign clergy — the Tang church's documented end"* — with the
record's own disclosure beside it: *"the same communion carried on in Persia
and Central Asia."* Not a dramatized drying-up; the line ends where the
record ends, and says where the water went.

**The width, honestly shown:** the same band, panned back west, holds the
tag's other half. At the sheet's western margin, **Anglo-Saxon Christianity**
(597–793) — the river Gregory's forty monks started in Scene III — with its
real site: *Lindisfarne Priory, Holy Island, Northumberland — the site raided
in 793, with its Anglo-Saxon stonework, cared for by English Heritage*
(census `experienceToday`). A carved stone at the sheet's eastern edge, 781;
raided stonework at its western edge, 793. Twelve years apart, at the two
ends of the known world, and the map needs no caption to make the point.
Between them, real and named in graphite: *the Palatine Chapel at Aachen —
Charlemagne's own chapel, consecrated in 805* (Carolingian Reform entry);
*Saint Sophia Cathedral and the Kyiv-Pechersk Lavra* (Kievan Rus', the river
the Cyrillo-Methodian course became in 988, by its own `continuesAs` chain);
and on the Syriac lane's southern reach, *St Mary's Knanaya Church, Kottayam,
Kerala — home to two ancient granite 'Persian crosses' carved with Pahlavi
inscriptions* (St. Thomas Christians of India, 849–1054) — the same
communion's stones, half a world from Edessa.

**Text and data on screen:** hovering any reach gives that window's glimpse
card; hovering a stone gives the `continuesAs` line; clicking opens the full
record. The one long ride tells a participant, wordlessly, what a table of
entries never could: that four rows are **one river**, and that a church
whose bishops sat in Persia once watered ground at the Tang court of
Chang'an.

**Alive, without moving:** this is the treasure-hunt scene (capture §3 —
*"the wow of discovery… finding what you didn't know was there"*). The
aliveness is the *arrival*: after two quiet, dashed centuries of eastward
course, the backdrop texture at the river's end resolves into the stele's own
carved surface — cross rising above cloud and lotus, rendered as
rubbing-texture in iron-gall, the way Chinese steles have actually been read
for centuries: by hand, with paper and ink. Principle 3 — the mark of real
hands, these ones from 781.

**Grounding:** census era 4 record (title, dates, tag, ground, keyEvents);
`the-church-of-the-east-on-the-silk-road` full record (relationsSummary,
longDescription, sourcing, dateRationale, experienceToday); `continuesAs`
chain `the-church-of-the-east-under-persia → …on-the-silk-road`;
`anglo-saxon-christianity`, `carolingian-reform-christianity`,
`kievan-rus-christianity` (+ chain from `cyrillo-methodian-slavic-christianity`),
`st-thomas-christians-of-india` records and experienceToday; edge
`roman-church-gregorian → anglo-saxon-christianity`; capture §3, §8.

---

## Scene V — Era V: The High Medieval Era, 1054–1300

*"Reform, renewal, and the new orders" (the era's tag). Ground: pale
vellum-green `#E3E0CB`. The band opens on the sheet's largest estrangement
and fills with its most concentrated season of new channels — and the design
treats both at the same volume, which is to say quietly.*

**What the participant just did:** panned down one band and stopped where the
Greek East & Orthodoxy river and the Latin West & Catholicism river run
close. Between **The Byzantine Church after the Schism** (1054–1300) and
**The Latin Papal Church (Gregorian Reform to Innocent III)** (c. 1049–1300),
something small sits in the space between the two courses. The keyEvents on
the margin: *The Great Schism (1054) · First Crusade (1096) · Sack of
Constantinople (1204)*.

**The mark, specified [PROPOSED — this draft]:** the interaction mark,
everywhere on the sheet, is the **footbridge** first seen whole in Scene II —
a tiny iron-gall bridge glyph at the point where two rivers' stories actually
touched, because a bridge is where people cross, and interaction, in Mark's
own words, *"would be key."* Its modifiers are honest and quiet:

- **Contemporary contact** (`contemporary with`): the bridge whole.
- **Tension** (`in tension with`): the same bridge drawn **open at the
  center** — a span with a gap. Still a bridge. Still small.
- **Argument** (`argued against`): the open bridge with a small book-glyph at
  one end — because in this census, nearly every argument *is* a book, and
  the full panel will name it.
- **Confidence**: the bridge's linework goes solid/dashed/dotted exactly as
  every other line on the map does.
- **Weight**: the mark grows only by an honest, computed property — how many
  sourced edges meet at that crossing — never by an editorial judgment of
  importance. (Off-screen but real: the census's Anomoean/Eunomian entry is
  argued against by the Cappadocians *and* the imperial church, and in
  tension with the Homoians — three sourced edges, so its crossing carries a
  visibly heavier mark than a single-edge crossing. Computed fact, not
  opinion.)

No rapids. No storm. No red. The mark between Rome and Constantinople — the
largest estrangement on the entire sheet — is a broken footbridge a few
pixels wide, drawn solid because the record is *Documented*.

**Hover (short):** a glimpse card, three lines —

> **The Great Schism** · in tension · Documented
> The Roman Church of the Reform Popes ↔ The Orthodox Church of Constantinople
> 1054 — *and it was not as simple as one date. Click for the record.*

**Click (full):** the panel opens with the census's own sourced note, whole
and unsoftened, museum-label register:

> *"The Great Schism, in each side's own documents: Humbert's bull of
> excommunication laid on the altar of Hagia Sophia (16 July 1054);
> Cerularius's synodal condemnation of the legates the following week.
> Process honesty: 1054 was symbolic and legate-to-patriarch, not
> church-to-church; the 1204 sack of Constantinople sealed the estrangement
> (scholars dating the real rupture there — that reading Contested); the
> anathemas were mutually lifted in 1965."*

The panel renders the note's own internal honesty visually: the 1054 line
solid, the "real rupture at 1204" reading dotted — the map keeps its
line-language even inside a single record. And the last clause sits at the
bottom in the smallest honest type: *the anathemas were mutually lifted in
1965.* Nine hundred years wide, and the record's own final word is a quiet
un-saying. The design does nothing to amplify any of this. It doesn't need
to.

**The counterweight — the band itself:** so the bridge never reads as "the
conflict symbol," the arithmetic of the whole sheet stands behind it: of 69
sourced edges, 47 are formation and transmission, 6 are contact, 16 are
tension or argument. The landscape's own arithmetic is mostly gift — and
this band shows it. West of the mark, the Latin river braids into the
century of new channels the era is named for, every one a real graphite
course with a real site-mark from its own census record: **Cistercian
Monasticism** (1098 — *the Abbey of Fontenay, founded from Clairvaux in
1118, one of the most complete surviving Cistercian abbeys in Europe*, and
this band's whisper-strength ashlar texture); **Carthusian Life** (1084);
**The Franciscan Movement** (1209 — *the Basilica of Saint Francis at
Assisi, built over his tomb from 1228*); **The Dominican Order** (1216);
**The Beguines** (c. 1190 — *the Princely Beguinage Ten Wijngaerde, Bruges,
founded in 1244, still standing around its garden*); **The Waldensians**
(c. 1173 — *Torre Pellice, the Alpine valleys where the community
survived*), a thin course worth marking with the eye, because it is one of
the only rivers in this band that will still be flowing when the sheet
reaches its bottom edge. East of the mark, renewal in the same key: the
Athonite houses (*the Great Lavra, founded 963, still the senior monastery
of the mountain*), Studenica, Rila, Lalibela — *eleven churches cut downward
out of the living rock, still in use for worship* (Zagwe Ethiopian entry).

**Alive, without moving:** the mark's aliveness is principle 3 — it is
*inscribed*, a deliberate small act of the mapmaker's hand at a real
crossing, with the slight press-weight of a nib start and stop. And the
restraint itself reads as life: a still, small mark over a nine-century
wound is the visual grammar of a witness who was actually there and does not
need to raise their voice.

**Grounding:** census era 5 record (title, dates, tag, ground, keyEvents);
edge `latin-papal-church-gregorian ↔ byzantine-church-after-1054` (in
tension with, Documented, note verbatim); Eunomian edge-count and
type/confidence counts computed from `edges[]`; records + experienceToday
for `cistercian-monasticism`, `the-franciscan-movement`, `the-beguines`,
`the-waldensians`, `athonite-and-comnenian-byzantine-monasticism`,
`serbian-and-bulgarian-medieval-monasticism`,
`zagwe-and-early-solomonic-ethiopian-christianity`; capture §3 & §8
("humble, not front-and-center"; mark carries scale by honest property
only); existing hover/click grammar (Full UX Design §2.4).

---

## Scene VI — Era VI: The Late Medieval Era, 1300–1517

*"Crisis and devotion on the eve of reform" (the era's tag). Ground: cool
blue-grey `#D8E4E5`. The scene is built on the tag's own two words, each
given a real building — one very large, one very small.*

**What the participant just did:** panned down across the 1300 seam and
paused, because two site-marks in the same band are drawn at honestly
different scales and the contrast asks to be looked at. The keyEvents on the
margin state the crisis half without commentary: *Avignon Papacy begins
(1309) · Black Death (1347–51) · Western Schism (1378–1417)*.

**On screen — crisis:** the Latin Papal river passes its boundary stone at
1300 and becomes **The Latin Papal Church (Avignon to Fifth Lateran)**
(1300–1517). Its glimpse card carries the census's own summary, which needs
no dramatizing: *"two centuries in which the papacy left Rome, split three
ways, was put on trial by its own councils, and came back as a Renaissance
court."* Its site-mark is the era's largest:

> *The Palais des Papes, Avignon — the popes' fortress-palace, a UNESCO
> World Heritage Site open to visitors year-round.* (census
> `experienceToday`)

A fortress-palace, drawn in graphite at fortress scale. The record beneath
is one click away and carries what the census itself carries — the Western
Schism healed at Constance, the conciliar contest, and the register's own
process-honesty about the hard things it holds as context, never
endorsement.

**On screen — devotion:** on the same band, at the sheet's western margin,
the era's smallest site-mark, drawn with the same care the fortress got:

> *St Julian's Church, Norwich — the rebuilt cell on the site of Julian's
> anchorhold, open daily.* (census `experienceToday`, The English Mystics
> and Devout, c. 1330–1440)

One room against a church wall. The hinted-presence rule has no better
friend on the whole sheet than an anchorhold: the room itself *is* the life,
and no figure is needed or shown — a cell, a window toward the altar, a
lamp. The glimpse card carries the census's teaser: *"hermits, anchoresses
and a weeping townswoman who wrote about God in English, in the first
person, when almost nobody else did"* — and the sourcing line that makes
this thin course one of the richest places on the map: *"RICH,
first-person, vernacular, two women's voices — Julian's Showings; Margery
Kempe's Book may be the atlas's best ordinary-believer document."* The
record's own relations line adds the quiet connection a reader could miss:
*"Carthusians copied and preserved these texts (documented transmission)"*
— the century-old order from Scene V's band, keeping a townswoman's book.

**The third beat — Bohemia:** between the two, the band's most consequential
graphite course: **The Hussite & Bohemian Brethren Movement** (1415–1517),
its census teaser doing all the work: *"a whole country that took communion
in both kinds, was crusaded against five times for it, and kept its own
church anyway."* Its site-mark: *Bethlehem Chapel, Prague — rebuilt on its
medieval foundations and surviving walls, where Hus preached in Czech*
(census `experienceToday`). The census's relationsSummary calls it *"a
functioning non-Roman national church a century before Luther"* — and its
river carries a boundary stone at the band's bottom edge whose far side the
participant will not reach for two more scenes. Worth a margin note the map
itself makes silently: rivers in this band also end — Terminal Christian
Nubia's course stops c. 1484, at its recorded end, with the *Faras Gallery,
National Museum in Warsaw* standing as its real, visitable survival.

**Text and data on screen:** the era's own `rec` line renders once in quiet
chrome — signals, not verdicts — and every card keeps its honest census
status. In the Greek East lane, **Hesychasm & the Palamite Synthesis**
(c. 1300–1400) stands with Athos as its living site; the band is quieter on
its eastern half, and the drawing lets it be quiet rather than filling it.

**Alive, without moving:** principle 2 carries the scene: **the light of one
window**. The band's two named buildings are lit the same way — a high
window's shaft on a stone floor — which is simply how both a papal audience
hall and an anchorhold were actually lit, and the participant feels the
difference in scale precisely because the light is the same. Principle 1
sits in the cell: a book open, ink dry, the lamp trimmed.

**Grounding:** census era 6 record (title, dates, tag, ground, keyEvents,
rec); `latin-papal-church-avignon-to-lateran-v` record (teaser,
relationsSummary, experienceToday) + `continuesAs` chain from
`latin-papal-church-gregorian`; `the-english-mystics-and-devout` record
(teaser, sourcing, relationsSummary, experienceToday);
`the-hussite-and-bohemian-brethren-movement` record (teaser,
relationsSummary, experienceToday); `terminal-christian-nubia` and
`hesychasm-and-the-palamite-synthesis` records; capture §3 (hardship
posture, kept).

---

## Scene VII — Era VII: The Reformation Era, 1517–1650

*"The Western church remade — several ways at once" (the era's tag). Ground:
warm parchment `#EFDDB3`. A new riverbed carries water for the first time,
and the band braids more densely than any before it.*

**What the participant just did:** crossed the 1517 seam — and noticed,
because the sheet's structure makes it noticeable, that a lane which ran
empty down six bands now fills: the **Protestant & Evangelical** riverbed
(`laneOrder 6`) carries its first courses. The keyEvents on the margin:
*Luther's 95 Theses (1517) · Council of Trent (1545–63) · Peace of
Westphalia (1648)*.

**On screen — several ways at once:** the tag is the picture. From the Latin
West's braid, new channels cut west into the new lane, each a real census
course in graphite: **Lutheran Wittenberg & Its Congregations** (1517–1580 —
site-mark: *the Luther museums in Lutherstadt Wittenberg — Luther's own
house and Melanchthon's, a UNESCO World Heritage site*); **The Reformed
Cities — Zurich & Geneva** (1519–1650 — *the International Museum of the
Reformation, Geneva, beside St Peter's Cathedral, in the old cloister where
the city voted for reform*; census relationsSummary: *"Parent of the
Scottish, Huguenot, Dutch, and Puritan traditions"* — and the band shows all
four as real named courses); **The Anabaptist Movements** (1525–1650); the
English and Scottish reformations; the Huguenots. And the Latin river itself
reforms in place: its boundary stone at 1517 reads **The Tridentine Church**,
with *the Museo Diocesano Tridentino, Trento — a gallery devoted to the
Council of Trent itself* as its real site, and the **Society of Jesus**
(1540) beside it — *the Church of the Gesù, Rome, holding Ignatius's tomb
and the rooms where he lived and wrote*.

**Two marks, and a cave:** between the Wittenberg course and the Anabaptist
course sits an open footbridge with the book-glyph — `argued against`,
Documented — its census note carried whole: *"The Radical Reformation
defined itself against the magisterial reformers' church-state settlement as
much as against Rome."* The Anabaptist course's own site-mark is the band's
quietest and most eloquent piece of hinted presence:

> *The Täuferhöhle near Bäretswil, Switzerland — the cave in the hills
> outside Zurich where hunted Anabaptists met to worship, reachable on a
> short marked walk.* (census `experienceToday`)

A cave mouth, a path, daylight at the entrance. No figures, no drama — the
census's own sourcing line says where this world's voice actually lives:
*"court testimonies, prison hymns, the Martyrs Mirror."* Honest
accessibility for those searching, not hype (capture §3).

**Two long rivers arrive:** this band holds the sheet's two great
treasure-hunt confluences. First: a course entering the Reformed cities from
eleven centuries upstream — the census's `transmitted to` edge from
Augustine's own world (Era I's Latin pastoral-congregational Christianity),
Documented, solid, its note carried in full on the panel: *"Calvin's
Institutes draws explicitly and heavily on Augustine's anti-Pelagian
writings… A direct theological line across eleven centuries with no
institutional continuity — influence, not identity."* The longest single
drawn connection on the sheet, and the record itself supplies the honest
caption. Second: the thin Alpine river from Scene V joins the new lane at
1532 — and the junction is drawn **dotted**, because the census grades the
Waldensian-Reformed union's continuity claim *Contested*: *"The Waldensians
adhered to the Reformation in 1532; how much earlier 'proto-Protestant'
continuity is real versus retrospective is a live scholarly argument."* The
map draws the join and declines to overclaim it, in the same stroke.

**Text and data on screen:** glimpse cards throughout, statuses honest; the
Bohemian river from Scene VI runs its last century here (**The Czech
Churches' Last Century**, 1517–c. 1627 — *"a reform church older than
Luther's, living on borrowed legal time"*), and where its ink stops, the
ruled graphite bed visibly continues toward the next band. A participant who
wonders why is one scene from the answer.

**Alive, without moving:** principle 3, sharpened: this is the century the
mark of the hand became the mark of the press, and the band's textures are
drawn from set type and woodcut line — real pages of real printed
confessions rendered as texture the way Dura's plaster textures Era I. The
maker's hand is still everywhere; it is simply holding a composing stick
now.

**Grounding:** census era 7 record (title, dates, tag, ground, keyEvents);
lane 6 first-appearance fact computed from `movements[].lane/era`; records +
experienceToday for `lutheran-wittenberg-and-its-congregations`,
`the-reformed-cities-zurich-and-geneva`, `the-anabaptist-movements`,
`the-society-of-jesus`, `the-tridentine-church`,
`czech-churches-last-century`; edges `lutheran-wittenberg… →
the-anabaptist-movements` (argued against, Documented),
`latin-pastoral-congregational-christianity →
the-reformed-cities-zurich-and-geneva` (Documented), `the-waldensians →
the-waldensian-reformed-union` (Contested), notes verbatim; capture §3, §8.

---

## Scene VIII — Era VIII: The Enlightenment & Awakening Era, 1650–1815

*"Established churches, awakened hearts" (the era's tag). Ground: pale
vellum-green `#E3E0CB`. The scene is the tag rendered as hydrology: broad,
steady, established channels — and small bright springs rising inside them.*

**What the participant just did:** followed the ruled-but-uninked graphite
bed left hanging at the end of Scene VII — the one that kept going after the
Czech river's ink stopped in 1627 — down across the era seam, to see where
it leads. The keyEvents on the margin: *First Great Awakening (1730s) ·
American Revolution & disestablishment (1776) · French Revolution's
dechristianization campaign (1790s)*.

**On screen — the river that resurfaces:** the bed leads to a boundary stone
dated 1722, and the ink resumes: **The Moravian Church at Herrnhut**
(1722–1815). This is the sheet's most striking `continuesAs` seam, because
its two inked reaches do not touch — the census itself names the gap and
crosses it deliberately: the Czech entry's relations line routes *"the
relation to Herrnhut… across the hidden-seed century"*, and the Moravian
entry answers: *"Literal renewal of the Bohemian Brethren"* — an identity
*"ruled at the Era 8 gate"*, refugee-carried, with its supporting
consecration line flagged `[S]` in the record itself. The rendering obeys
the record exactly **[PROPOSED — this draft]:** across the silent
1627–1722 stretch, the riverbed stays visible as pure graphite underdrawing
— ruled, uninked — and the ink resumes at the stone. The sheet's own honesty
grammar turns out to already contain the idea of a hidden seed: the ruling
that waits.

Herrnhut's glimpse card carries the census teaser that earns the scene:
*"a refugee village of a few hundred that wrote down every day of its life,
prayed in shifts around the clock, and sent out missionaries on a scale no
other Protestant church came near"* — and the sourcing line: *"RICH to an
almost unique degree: daily congregational diaries, choir records, thousands
of member memoirs (Lebensläufe), the Losungen since 1731."* Its site is not
a ruin:

> *Herrnhut, Germany — the Moravian Church's founding town, still a living
> community and a UNESCO World Heritage Site.* (census `experienceToday`)

**The awakened springs beside it:** in the English channel of the same lane,
**The Methodist Revival** (1738–1815) — teaser verbatim: *"a priest who
could not get a pulpit preached in fields instead, then organized everyone
who listened into weekly classes that had to give an honest account of
themselves"*; relations line, verbatim: *"Child of Puritan piety + Moravian
influence inside the English church"* — the map draws no invented edge, but
the panel's own census text hands a reader the Herrnhut connection in the
record's words. Its site: *Wesley's Chapel and the Museum of Methodism, City
Road, London — the chapel Wesley opened in 1778, his house next door, and
his grave behind it* (census `experienceToday`). Its outflow leaves the
band's bottom edge already labeled for the next scene: `formed` → the
Holiness movement, Documented — *"The Holiness movement understood itself as
recovering Wesley's own doctrine of sanctification."* And the established
channels these springs rise beside are drawn at their real breadth, named
and unglamorous: the Ancien Régime Catholic river, the Georgian Church of
England, the Russian Church from Nikon to the Holy Synod.

**The eastern counterpart:** the Greek East lane carries its own awakening
in the same decades — **The Hesychast Revival — Paisius & the Philokalia**
(1746–1815), with *Neamț Monastery, Romania — Paisius's community and
translation centre, a working monastery where his relics are kept* (census
`experienceToday`), and the Old Believers' course beside it holding its own
stubborn line. The tag's two words are not a Western story; the band shows
it.

**Alive, without moving:** principle 1, in its purest census-sourced form
this sheet will ever get: **a village that wrote itself down daily.** The
band's texture is drawn from the kinds of objects the record names — diary
pages, watchword slips, class-meeting rolls — and the era sits at **the
first hour of the morning**, the hour a community draws its daily watchword,
light low and level across paper. Nothing moves; everything has just been
written.

**Grounding:** census era 8 record (title, dates, tag, ground, keyEvents);
`continuesAs` chain `czech-churches-last-century →
the-moravian-church-at-herrnhut` with both entries' relationsSummary
verbatim (hidden-seed century, Era 8 gate ruling, [S] flags);
`the-moravian-church-at-herrnhut` record (teaser, sourcing,
experienceToday); `the-methodist-revival` record (teaser, relationsSummary,
experienceToday) and edge `→ the-holiness-movement` (Documented, note
verbatim); `the-hesychast-revival-paisius-and-the-philokalia` and
`the-old-believers` records; `catholic-church-ancien-regime`,
`restoration-georgian-church-of-england`, `russian-church-nikon-to-holy-synod`
records (the established channels).

---

## Scene IX — Era IX: The Missionary Era, 1815–1906

*"Revival, missions, and a globalizing faith" (the era's tag). Ground: cool
blue-grey `#D8E4E5`. The census's fullest band — 51 entries — and the scene
holds its two most remarkable facts: a confluence, and a resurfacing.*

**What the participant just did:** panned down into the band and felt the
density change before counting anything — more courses enter this band than
any other on the sheet, and lanes that hugged one meridian for centuries now
reach shores the top edge never imagined. The keyEvents on the margin:
*Second Great Awakening (1800s–30s) · Abolition of the transatlantic slave
trade (1807/1833) · American Civil War (1861–65)*.

**On screen — the confluence:** in the Protestant lane, two courses the
participant has followed since Scene VIII bend toward each other and a third
river forms: **The Black Church in America** (c. 1770s–1906). Both forming
edges are real, dashed for *Widely Accepted*, their census notes carried
whole: from the Baptists — *"The Black Baptist congregations (Silver Bluff
c. 1773–75, First African Savannah 1788) are the Baptist parent line of the
Black Church"* — and from the Methodist revival — *"Richard Allen's AME
(1816) and AME Zion (1821) are Methodist bodies — the Methodist parent line
of the Black Church."* The glimpse card carries the census's own teaser,
which the design leaves entirely alone, because no rendering could add to
it and any would subtract: *"a church born in praise houses and hush
harbours, whose theology was sung long before it was allowed to be written
down."* The sourcing line beneath, verbatim: *"RICH and inside-voice: slave
narratives (editorial-frame gravity named), spirituals as communal
theology, conversion accounts, Allen's and Jarena Lee's autobiographies."*
The site-mark is a standing building with a census label that is itself a
piece of history:

> *Mother Bethel A.M.E. Church, Philadelphia — Richard Allen's
> congregation, founded 1794, on the oldest parcel of land continuously
> owned by African Americans in the United States.* (census
> `experienceToday`)

At the band's bottom edge, this river's boundary stone is already cut: the
census's own relations line says the entry *"names as its own future"* the
civil-rights church of the next era, carried by `continuesAs`. The
confluence has two rivers in and a century out, and the drawing simply
shows that.

**On screen — the resurfacing:** on the sheet's far eastern reach, a course
begins mid-band with no drawn line arriving from anywhere — and that
absence is the record, honored. **Japanese Christianity — the Hidden
Christians' Emergence & the Meiji Church** (1865–1906): the census dates
its opening *to the day* — 17 March 1865, when, in its teaser's words,
*"villagers… walked into a new church and revealed that their families had
kept the faith for two and a half centuries without a priest"* — roughly
30,000 of them, per the relations line, surfacing at Ōura. The sheet draws
no course across those hidden centuries **because the census records none**;
the map's honesty grammar has no stroke for what the record cannot trace,
and here that restraint becomes the most eloquent line never drawn. The
site-mark:

> *Ōura Church, Nagasaki — the church where the hidden Christians revealed
> themselves in 1865, a National Treasure of Japan and open to visitors.*
> (census `experienceToday`)

**The width, in real places:** the band's reach is shown by its own census
sites, small and credited: *Serampore College, West Bengal — founded in
1818 by Carey, Marshman and Ward, and still teaching* (the Missionary
Movement's Native Churches); *the Basilica of the Uganda Martyrs at
Namugongo*; *the Church of the Holy Ascension, Unalaska, and Spruce Island,
Alaska — Saint Herman's hermitage and grave* (the Alaskan Mission); *Optina
Pustyn — the monastery of the elders, receiving pilgrims again* (the
Russian ascetic renewal). Eight lanes wide and every point on it a real
door someone could walk through this year.

**Alive, without moving:** principle 1 carries the scene, and the census
chose the object: **song as evidence of use** — *"theology… sung long
before it was allowed to be written down."* The board cannot and does not
play a note; it shows the stillness after singing — a meeting-house room,
benches worn smooth, a hymn-book open — and lets the record's sentence do
what no animation could. Quiet register throughout, per the standing rule:
the hardship in this band is neither hidden nor made a spectacle; it is in
the notes, findable, in each record's own words.

**Grounding:** census era 9 record (title, dates, tag, ground, keyEvents);
entry count per era computed from `movements[]`; `the-black-church-in-america`
full record (teaser, sourcing, relationsSummary, experienceToday,
continuesAs); edges `the-baptists → the-black-church-in-america` and
`the-methodist-revival → the-black-church-in-america` (Widely Accepted,
notes verbatim); `japanese-christianity-hidden-emergence-meiji` full record
(teaser, relationsSummary, experienceToday);
`the-missionary-movement-s-native-churches-seramp`,
`east-african-christianity-uganda-martyrs`,
`alaskan-mission-herman-veniaminov`,
`the-optina-elders-and-russian-ascetic-renewal` experienceToday entries;
capture §3 (hardship posture, kept).

---

## Scene X — Era X: The Global Church Era, 1906–present

*"The center of gravity moves south and east" (the era's tag). Ground: warm
parchment `#EFDDB3` — the sheet ends on the same warmth it began on, which
is not an accident anyone needs explained to them. The last lane opens, and
the rivers reach the edge of the paper.*

**What the participant just did:** one long pull downward — their own hands,
through the Missionary band into the last ground — and then the pan stops,
because the parchment stops. The keyEvents on the margin: *Azusa Street
Revival begins (1906) · World War I (1914–18) · Second Vatican Council
(1962–65)*.

**On screen — the last lane opens:** at the band's top, the **Global Revival
& Pentecostal** riverbed (`laneOrder 7`) — empty down nine bands — takes its
first water: **Azusa Street & Early Pentecostalism** (1906–1920s). Its
forming edge arrives solid from Scene IX's Holiness course — Documented:
*"Azusa Street's leaders and vocabulary came directly out of the Holiness
movement"* — and the census's relations line names the fuller parentage in
its own words: *"Child of Holiness + Black Church worship; parent of most of
this era's family."* The confluence the participant watched form in Scene IX
is upstream of this spring, and the sheet lets the eye make that connection
by simply drawing what the records say. One outflow is already inked and
dashed — *Widely Accepted*, reaching the Africa lane: *"Aladura and Zionist
movements drew on Pentecostal currents while being genuinely
African-initiated — the balance is actively studied"* (→ African-Initiated
Churches). The tag's center of gravity is visible as geometry: the lanes
that thicken in this band are Africa, Global Revival, and the eastern
reaches; the census's own arithmetic (49 entries here, most flagged
`living: true`) *is* the picture.

**A mark the participant has seen before:** in the Protestant lane, an open
footbridge — the census's own note introducing it as *"the census's second
'in tension with' edge — the Great Schism pattern run inside Protestantism,
graded on both sides' own dated rupture texts"* (Fundamentalism ↔ the
Mainline Century, Documented, the panel naming the texts and dates the
record names). Same small glyph as Scene V, same size, same silence. The
grammar holds at both ends of the sheet, which is the point of having a
grammar.

**The art, and an honest disclosure:** Era X is the one band whose census
records carry no `experienceToday` fields yet — the survey's own edge, stated
rather than papered over. So this scene's one art anchor is the real object
the census itself names in its Azusa entry's sourcing and teaser fields —
*"documented as it happened in its own newspaper, The Apostolic Faith"* —
framed museum-style:

> *The Apostolic Faith (Los Angeles), the Azusa Street mission's own
> newspaper, 1906 onward — named in the census record itself; its surviving
> issues are held and digitized by the Flower Pentecostal Heritage Center,
> Springfield, Missouri.* (Holding institution identified from outside the
> census and flagged as such — the one such credit on the sheet.)

Set type again, as in Scene VII — a movement that printed its own record as
it happened, rendered as page-texture at whisper strength on the band.

**The bottom edge — where the rivers leave the map:** and then the one place
on the whole sheet where the rendering makes a distinction the data has been
carrying all along: the `living` flag. Rivers whose windows closed have
ended, honestly, at their recorded end-years upstream. But rivers the census
marks living reach the parchment's edge **still inked at full confidence —
and run off it**. The bank lines go to the deckle edge and stop only because
the paper does. A map can end; it would be a lie for the river to. Along
that edge, small and credited, the proof the census already carries — real
places where a participant could stand, this year, in the current of
something that entered the map's top edge:

> *The Monastery of Saint Anthony, Eastern Desert, Egypt — grown up around
> Antony's own cave, still inhabited.* (The Desert's river: entered the map
> c. 320.)
> *Mor Gabriel Monastery, Tur Abdin — founded 397, still a working
> monastery.* (The Syriac river: entered c. 200.)

**Text and data on screen:** hover on any river at the edge gives the
living-tradition chip and the world's *experience today* line where its
record carries one — the same honest register as everywhere else. Click
gives the full record. Nothing new is invented at the edge; the edge just
lets the data's own `living: true` finally *look like something*.

**Alive, without moving:** this scene is the thesis. Nothing here animates —
and the stillness is what makes the claim serious. A shimmering river says
"an app is running." A still river inked clean off the edge of a
two-thousand-year map, next to a label naming the real monastery where its
water can be visited today, says what the project actually believes: this is
a *visual way to see Jesus at work across history and today* (capture §1,
Mark's own words) — and *today* is not a special effect.

**Grounding:** census era 10 record (title, dates, tag, ground, keyEvents);
`azusa-street-and-early-pentecostalism` full record (teaser,
relationsSummary, sourcing); edges `the-holiness-movement →
azusa-street-and-early-pentecostalism` (Documented) and
`azusa-street-and-early-pentecostalism →
african-initiated-churches-harrist-aladura-zioni` (Widely Accepted), notes
verbatim; edge `fundamentalism-1910-1970s ↔
the-mainline-century-liberal-and-neo-orthodox` (in tension with, Documented,
note verbatim); era-10 entry count and living-flag facts computed from
`movements[]`; absence of era-10 `experienceToday` fields verified against
the census; `living` flags and `experienceToday` entries for
`desert-monasticism` and `syriac-edessa-nisibis`; capture §1, §11.

---

## Closing — ten headlines, one per era, offered for the open question

The capture (§8, §14) leaves open what a "headline" would actually say — a
punchier, more human framing than a formal name, for a world or an era. With
the storyboard now walking all ten eras, the candidate list walks with it:
one per era, each derived from a real census line (cited), none inventing a
fact. They would live where the formal name lives now, with the formal name
one breath beneath — headline in Alegreya italic, formal name in small caps
under it.

1. **Era I — "The church before it had buildings."** Post-Apostolic
   House-Church Christianity. *From its longDescription: "Christianity had
   no buildings of its own… it had houses."*
2. **Era II — "They went out to fight what was inside."** Desert
   Monasticism. *From its tile: "left settled village life to wage a
   lifelong combat against the thoughts that trouble a person from within."*
3. **Era III — "A short rule for one household."** Early Benedictine /
   Italian Monasticism. *From its teaser: "a short, practical rule for a
   single household of monks… that ended up organizing Western monastic
   life for fifteen centuries."*
4. **Era IV — "One river, Edessa to Xi'an."** The Church of the East on the
   Silk Road. *From its relationsSummary: "the map's longest single lineage
   line (Edessa to Xi'an)."*
5. **Era V — "They walked out of a rich abbey."** Cistercian Monasticism.
   *From its teaser: "monks who walked out of a rich abbey to keep
   Benedict's Rule plainly."*
6. **Era VI — "She wrote about God in English, in the first person."** The
   English Mystics and Devout. *From its teaser: "…who wrote about God in
   English, in the first person, when almost nobody else did."*
7. **Era VII — "Remade — several ways at once."** The Reformation Era.
   *Trimmed directly from the era's own census tag.*
8. **Era VIII — "A village that wrote down every day of its life."** The
   Moravian Church at Herrnhut. *From its teaser, verbatim.*
9. **Era IX — "Sung long before it was allowed to be written down."** The
   Black Church in America. *From its teaser: "whose theology was sung long
   before it was allowed to be written down."*
10. **Era X — "The church moves south."** The Global Church Era. *From its
    tag: "The center of gravity moves south and east."*

A rule worth adopting if any of these survive review **[PROPOSED — this
draft]**: every headline must be derivable from a line already in the census
or the world's own construction record, the way all ten above are — so the
punchier register never becomes a side door for unsourced claims.

---

## What this draft deliberately does not do

No tool is named, no architecture sketched, no build increment proposed — per
the brief. The scenes above are pictures for Mark to react to. Where a scene
answers a question the capture left open (what a world looks like on the
terrain; what a `continuesAs` seam looks like — including one whose reaches
don't touch; what makes still art alive; the footbridge mark; the compass
placement of lanes; the headline rule), the answer is marked **[PROPOSED —
this draft]** and stands ready to be kept, bent, or struck in the convergent
phase.

---

## Document log

- **REV 3 (2026-08-31, same day):** Added the founding-principle statement to
  the header, at Mark's explicit direction — *"the base program is about the
  entire ecology, not the build worlds."* Ratifies, rather than changes, the
  REV 2 restructuring: the ten-scene/one-per-era shape was already organized
  around the whole census, not the six built worlds, and this revision simply
  states that as the document's own leading thesis instead of leaving it
  implicit in the scene-by-scene execution. Also logged as a decision in
  `CiC_Atlas_Reimagined_Divergent_Capture_V1_2026-08-31.md` §10.4.
- **REV 2 (2026-08-31, same day):** Restructured at Mark's explicit request
  — *"we need 10 eras covered, it should be 10 scenes 1 for each era look at
  the documents and build it as designed."* The first draft's seven scenes
  jumped zoom levels (whole map, Era I twice, Era II, Era V, a cross-era
  river, Era X) and left Eras III, IV, VI, VII, VIII, and IX uncovered.
  This revision replaces them with exactly ten scenes, Scene I through
  Scene X, one per census era, in order. Eras I–II (the only eras holding
  Built & Live worlds — all six of them, re-verified against the census's
  `status` fields) keep the arrival-at-a-world treatment; Eras III–X, which
  hold no Built & Live worlds, are drawn honestly in the graphite
  underdrawing register from each era's own real movements, edges,
  `continuesAs` seams, keyEvents, and `experienceToday` sites — dimmed as an
  honest state, never skipped, never faked. Material from the old scenes
  survives where it truly belonged: the House-Churches deep zoom folded into
  Scene I, the Desert arrival into Scene II, the Edessa–Xi'an ride into
  Scene IV (its movement's own era), the Great Schism mark into Scene V, the
  bottom-edge living rivers into Scene X. New era-scenes built from the
  census for III, IV, VI, VII, VIII, IX. §0 gained a "how the scenes walk"
  paragraph; the headline list grew from five to ten, one per era. Header,
  constraints, board description, and scope boundaries otherwise unchanged.
  Additional census fields re-derived this pass rather than assumed:
  per-era `status` counts, `eras[].keyEvents`, all `continuesAs` chains,
  edge type/confidence arithmetic, era-10's absence of `experienceToday`.
- **DRAFT (2026-08-31):** First creative pass, produced by a Fable-model
  session at Mark's request, same day as the divergent-capture it builds on.
  Sources read in full before drafting: the Divergent Capture V1.1, the live
  `world-census.json` (V0.20), Full UX Design V1.0 §2 (palette, typography,
  anti-ghost) — plus the Full UX Storyboard V1.0 for voice precedent, and the
  House-Churches world's own Doc_04/Doc_09 finals for Scene 6's features.
  Sandbox only; touches nothing live; decides nothing.
