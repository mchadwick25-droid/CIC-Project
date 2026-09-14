# The World Orientation & Selection Map — Design Specification V0.1

**Status:** Draft for Mark's review. Nothing here is built, and nothing here builds into
`cic-poc` — integration is a future decision belonging to the front-end thread.

> **Amendment A (2026-07-16).** After this draft was first written, the map was
> reframed as a **pre-Step-0 instrument**, and the Phase One Step 0 Conclusion
> (`reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx`) and Step 0 Methodology V1.0 were read
> directly. Three corrections follow: (1) Phase One's window is **70–451 CE**
> (Chalcedon), not 70–430; (2) Step 0 selected **nine worlds** — four are built,
> and **five are Selected-Not-Yet-Built** (Alexandrian Catechetical, Donatism,
> Cappadocian, Imperial-Juridical, Latin Pastoral-Congregational) — this spec's
> original census had missed three of them and understated the other two;
> (3) the census in Part 1.8 is **superseded** by the full-history survey in
> `CiC_World_Atlas_PreStep0_Survey_V0_1.md`, which is now the map's content spine.
> Edits marked ⟦A⟧ below apply the corrections; unrevised passages should be read
> against the Atlas where they conflict.

**What this document is:** the four deliverables of the World Orientation Map thread in
one place — (1) the landscape data model, (2) the honest "not yet" content, (3) the
five-step interaction flow, (4) the future-integration handoff note. It matures the
"World Map (Ultimate Vision)" idea already logged in the Front-End Decision Log
(2026-07-07) into a full specification; it does not replace or contradict that entry.

**What governs it:** Vision Conviction 1 (no single movement exhausts the richness of
Christ — the map's reason to exist), Conviction 4 (trustworthy transparency — the
reason unbuilt worlds appear honestly), the Historical Responsibility value (the map
itself must not oversell thin coverage or silently omit movements), and Constitution
Article 6 (the map succeeds when a participant arrives at a world with honest
expectations, holding its tensions as the world held them).

---

## Part 1 — The Landscape Data Model

### 1.1 The one rule, applied to the map itself

The project already has one rule expressed everywhere: **only what the evidence
supports is shown; where evidence runs out, the system says so plainly.** Applied to
the map, this rule has a consequence that shapes the whole data model:

> **Every visual element of the map is itself a historical claim, and therefore
> carries confidence calibration.** A band's date range, a lane assignment, and —
> especially — every influence line drawn between two movements is an assertion about
> history. The map does not get to draw arrows more confidently than the evidence
> warrants just because arrows look good. Relationship edges carry the same five-level
> confidence vocabulary (Constitution Article 17) as everything else, and the visual
> rendering encodes it (see Part 3).

### 1.2 Entity: Movement

One record per movement/era band on the map. Field names are illustrative, not code.

| Field | Type | Notes |
|---|---|---|
| `id` | slug | Stable identifier, e.g. `desert-monasticism` |
| `name` | string | Participant-facing name, e.g. "Desert Fathers and Mothers" |
| `subtitle` | string? | Scholarly label where the plain name needs one (mirrors `world_subtitle` in the live manifest) |
| `time_span` | {start, end, approx flags} | Years CE; either bound may be marked approximate; `end` may be `present` for living movements |
| `regions` | list | Plain-language places, modern-location gloss included ("Edessa & Nisibis — in what is now southeastern Turkey") |
| `lane` | enum | Presentational lane assignment (see 1.5) — explicitly *not* a historical claim; a movement may carry `cross_lane_links` |
| `build_status` | enum | See 1.3 — the field the transparency layer runs on |
| `status_detail` | string | Participant-facing one-liner qualifying the status honestly |
| `eligibility` | enum | Movement Scope doctrinal-floor status: `affirmed` / `not_yet_reviewed` / `outside_floor` — **never auto-filled; see 1.4** |
| `description` | text | Tile copy. For Live worlds: verbatim from `world_manifest.py`, including its sourcing-richness disclosure. For others: drafted per Part 2 |
| `not_yet_explanation` | text? | The clickable honest explanation (Part 2). Required for every non-Live entry |
| `relationships` | list of Edge | See 1.6 |
| `notable_figures` | list of Figure | See 1.7 |
| `living_tradition` | {descends_into: list, note}? | Which present-day communities descend from this movement; grounds the map's care with living traditions (Vision, "Living Traditions") |
| `nearest_live_neighbor` | id + note | The built world a curious participant should be pointed toward — by lineage, not just by date (see Part 3, step 4) |
| `entry` | {representative_id, launch}? | Live worlds only — the actual door into conversation |
| `census_confidence` | enum | Whether this entry's *presence and framing on the map* has been reviewed (`reviewed` / `provisional`) — the census itself must not pretend completeness |

### 1.3 The build-status taxonomy ⟦A — corrected against the Step 0 record⟧

Six values, defined by what has *actually happened* in the project's own process,
not by intention:

| Status | Definition | Current members |
|---|---|---|
| **Live** | Built through the full Construction Framework pipeline, deployed, open for conversation now | The House-Churches (#1); Syriac Christianity (#7); Desert Fathers and Mothers (#3); The Bethlehem Circle (#9) |
| **In Construction** | Doc_01 or later construction documents actually exist and work is active | *(none today)* |
| **Selected, Not Yet Built** | Chosen by a completed phase-level Step 0, with recorded reasoning; construction not begun | The five remaining Phase One worlds: Alexandrian Catechetical (#2 — substantial V6/V7-track prior construction exists); Donatism (#4); Cappadocian Nicene Pastoral-Monastic (#5 — folder exists, **no documents, deliberately not called "In Construction"**); Imperial & Juridical Christianity (#6); Latin Pastoral-Congregational (#8) |
| **Deferred by Step 0** | Named and reasoned about by a completed Step 0, held for a later phase — deferred, not dropped | Armenia; Aksum/Ethiopia; Persian Church of the East; Antiochene (Chrysostom-centered); Cyrilline/miaphysite Egypt; Jerusalem liturgical-pilgrimage; and the rest of the Phase One record's deferred list |
| **Pre-Survey Candidate** | Named in the Atlas's broad-survey layer for an era whose Step 0 has not run | All Era II–IX Atlas entries |
| **Excluded by Step 0 (grounds on record)** | Excluded by a completed Step 0 on a named ground — Criterion 1 (doctrinal floor), Criterion 2 (person-defined movement), or contested-evidentiary | Phase One's recorded exclusions (Marcion, Gnostic Christianities, Manichaeism, Homoian Christianity, Montanism, Novatianism; Ebionite/Nazoraean as contested-evidentiary) |

Decisions inside this table worth naming:

- **"In Construction" is earned by documents, not folders** — the Cappadocian world's
  empty folder stays Selected-Not-Yet-Built.
- **"Selected" and "Deferred" statuses exist only where a real Step 0 ran.** For
  Eras II–IX everything is a Pre-Survey Candidate, however strong its signals look,
  until that era's phase-level Step 0 actually runs.
- **There is no informal status like "probably unbuildable."** Source Ecology and
  floor verdicts come from running the actual methodology. The Atlas carries
  *signals* (sourcing, ecology, floor notes as questions); the map's copy says
  exactly that.
- **Exclusion grounds stay distinguishable** (the Step 0 Conclusion's own
  discipline): a Criterion 1 floor exclusion, a Criterion 2 person-defined
  exclusion, and a contested-evidentiary case are three different honest sentences,
  never smoothed into one "not included."

### 1.4 The eligibility field (Movement Scope) — reserved, not exercised

The Constitution's Movement Scope section (present in the V2.3 branch copies, not yet
in the frozen V2.2 main tree) sets a doctrinal floor for which movements are eligible
for construction at all. The Front-End Decision Log (2026-07-07, World Map entry)
already decided the map surfaces **two distinct exclusion reasons honestly rather than
smoothed together**: insufficient evidence, or falling outside the doctrinal floor.

The data model therefore carries `eligibility`, but with a hard discipline: **this
thread fills in `affirmed` only for the four Live worlds (whose builds already
established it) and `not_yet_reviewed` for everyone else.** Rendering a movement
`outside_floor` is a governance determination. Where the plain reading of the floor
suggests a movement would not pass (e.g., Gothic Homoian ["Arian"] Christianity under
the full-divinity affirmation), the census may *note* that the question exists — it
does not answer it. The map's copy for such a movement says the review hasn't been
conducted, which is the truth.

### 1.5 Lanes — presentational, and labeled as such ⟦revised 2026-07-16, Lane 4 resolved⟧

Seven persistent horizontal lanes, top to bottom, chosen so lineage lines mostly
flow within or between adjacent lanes. A lane is a reading aid, not a taxonomy of
the Church; the map says this in its own legend. The census (V0.5+) carries every
entry's lane assignment; a handful of entries carry *bridge* labels ("Greek East ↔
Latin West") because bridging IS their identity (the Uniate worlds, Taizé) — the
map renders those between their two lanes.

1. **Syriac East & Asia** — Edessa/Nisibis onward; Church of the East to Tang
   China; St. Thomas India; Maronites; the Sayfo and the modern diaspora.
2. **Caucasus** — Armenia and Georgia: two ancient national churches whose lane
   holds their shared conversions *and* their 607 parting over Chalcedon — the
   lane's own story teaches the era. *(New — resolves the old Lane 4's "Armenia
   isn't African" defect.)*
3. **Greek East & Orthodoxy** — Asia Minor, Constantinople, Byzantine monasticism,
   the Slavic and Russian worlds, Ottoman-era Orthodoxy, Optina, the émigrés.
4. **Africa** — the Nile spine and beyond: Alexandria, the Desert, Coptic Egypt,
   Nubia, Ethiopia/Eritrea, Kongo, the African-Initiated Churches, and the
   diaspora/reverse-mission churches — one continuous lane from Era Ia to the
   present, the map's visual proof of its longest-testimony claim. *(AICs move
   here from the old Lane 6; their lineage is African initiative, not a footnote
   to global Pentecostalism.)*
5. **Latin West & Catholicism** — Rome, the medieval West, Catholic reform and
   missions, Latin America, the Philippines, the post-conciliar world. **Honest
   note carried in the legend:** Latin North Africa (Donatism, Cyprian, Augustine)
   reads in *this* lane, not the Africa lane — its formation language and its
   downstream flow (Augustine → the whole medieval West) run here, while the
   Africa lane's continuity story is Nile-based. Geography loses that tie-break;
   the map says so rather than hiding it.
6. **Protestant & Evangelical** — appears at 1517; Lutheran, Reformed, Anabaptist,
   Anglican, Baptist, Methodist, Holiness, and their mission-born children.
7. **Global Revival & Pentecostal** — appears ~1900; Azusa and its family, the
   1904–07 revival cluster, the Chinese church, global South Pentecostalism,
   Messianic Judaism, Lausanne-era evangelicalism.

Adjacency is deliberate: Caucasus sits between the Syriac and Greek lanes (its two
formation lines), Africa between Greek and Latin (Alexandria's and Carthage's
respective conversation partners), Protestant below Latin (its birth line), Global
near the bottom (born of Protestant and African lines both). Entries older than
c. 300 render in the merged "Origin" zone that visually splits into lanes across
the fourth century, as before.

**The eighth stream — "Beyond the Floor (researched & explained)" ⟦added
2026-07-16, Mark's decision⟧:** a visually set-apart stream at the map's bottom
holding only movements whose *own confessions* place them outside both the Nicene
base and the bounded-exception (A4) proximity — Marcion, the Gnostic
Christianities, Manichaeism, the Homoian family, Bogomils, Cathars, the
anti-trinitarian Reformation currents, Shakers, Swedenborgians, LDS, Jehovah's
Witnesses, Christian Science, Christadelphians, Oneida, Spiritualism/New Thought,
Oneness Pentecostalism, INC/Way/Unification/Luz del Mundo, and the apocalyptic
splinters (19 census entries). They are not conversation worlds; they carry full
**research briefs** (grounds, sourcing, relations) — recognized, researched, and
explained, never hidden. Three honesty guardrails: (1) entries carrying *questions*
rather than verdicts — contested-evidentiary cases (Ebionites, Paulicians, Free
Spirit), A4-proximity cases (Schwenckfelders), person-defined exclusions with
sound theology (Montanism, Novatianism, Catholic Apostolic), and pending per-body
assessments (Ratana) — **stay in their historical lanes**, because moving them
would overclaim what the record can say; (2) stream entries keep their true time
positions and relationship edges (Marcion still sits beside the second-century
church he argued with); (3) the stream's copy states the Step 0 Conclusion's own
framing — a design effect, never a judgment of unimportance. **Governance flag
raised while sorting (not resolved here):** the Step 0 Conclusion holds Homoian
Christianity's A4 question open, but the Methodology's A4 clause says the
exception path "may never waive Christ's full divinity" — the very commitment at
issue; the two records are in tension and need a governance reconciliation.

A seventh strip, **Context**, runs beneath all lanes: empires, persecutions, councils,
the Great Schism, 1517, dates a participant can anchor to. Context entries are not
selectable worlds; they exist for step 2 of the five-step flow (orientation).

**Time scale:** piecewise era segmentation rather than linear years — 30–500 CE gets
roughly as much horizontal room as 1500–today, because that is where the project's
built density currently lives and where the formative story is thickest. The
distortion is disclosed on the map ("the map stretches time where the story is
dense"), with real date gridlines so no one is misled. This mirrors how the classic
synchronological charts (see Part 3) handle the same problem.

### 1.6 Entity: Relationship Edge

| Field | Type | Notes |
|---|---|---|
| `from`, `to` | movement ids | Direction matters for `formed` and `transmitted_to` |
| `type` | enum | `formed` (parent→child lineage) / `transmitted_to` (practices, texts, or institutions carried onward) / `reacted_against` (defined itself in opposition) / `diverged_from` (shared lineage that split) / `contemporary_with` (no dependency claimed, but the participant should see the simultaneity) |
| `confidence` | enum | The five-level vocabulary: Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin |
| `note` | string | One participant-readable sentence, hover-surfaced ("John Cassian carried the desert's teaching to Gaul; Benedict's Rule commends his writings by name") |

Edges below Contested confidence render differently than Documented ones (Part 3.3);
an edge the evidence cannot support at all is simply not drawn — the map has no
Tier-5 arrows, just as the worlds have no Tier-5 stories.

### 1.7 Entity: Figure

The interlinear "who lived in relationship to whom" texture — thin lifespan lines
within a movement's band, in the style of Priestley's Chart of Biography.

| Field | Notes |
|---|---|
| `name`, `lifespan` | e.g. Ephrem, c. 306–373 |
| `role` | one line: "hymn-writer whose madrashe carried this world's teaching" |
| `single_figure_note` | the honest handling of "can I talk to *him*?" — see Part 3.2. Figures are never conversation entry points; the map says why, in the Facilitator's already-decided words |

### 1.8 The census ⟦A — superseded by the World Atlas⟧

**The census that originally sat here (37 provisional entries) is superseded in
full by `CiC_World_Atlas_PreStep0_Survey_V0_1.md`** — the era-by-era pre-Step-0
survey of roughly 110 within-floor candidate worlds and ~25 adjacent-register
entries across nine eras, anchored at Era I to the Phase One Step 0 Conclusion's
actual nine-world record. The Atlas is the map's content spine; this spec keeps
only the Era I anchor here for orientation:

| # | Phase One world (Step 0 Conclusion, 70–451 CE) | Status |
|---|---|---|
| 1 | Post-Apostolic House-Church Christianity | **Live** (Chloe) |
| 2 | Alexandrian Catechetical / Christian-Platonist | Selected, not yet built |
| 3 | Desert Monasticism | **Live** (Papnoute) |
| 4 | Donatism | Selected, not yet built |
| 5 | Cappadocian Nicene Pastoral-Monastic | Selected, not yet built |
| 6 | Imperial and Juridical Christianity | Selected, not yet built |
| 7 | Syriac Christianity (Edessa/Nisibis) | **Live** (Mar Yausep) |
| 8 | Latin Pastoral-Congregational Christianity | Selected, not yet built |
| 9 | Hieronymian Ascetic-Literary Christianity | **Live** (Albina) |

Carried over from the superseded census, still governing the map build:
- **Pre-lane rendering for the earliest era** — before roughly 300 CE the lanes
  haven't diverged; the earliest bands render across a merged zone that visually
  splits into lanes across the fourth century.
- **Living movements never render as "ended"** because the project's likely build
  window for them is historical; the Vision's living-traditions distinction is
  carried in copy (the Atlas marks these ⚑).
- **Floor-question movements** (Homoian Christianity and the rest of the adjacent
  registers) now *do* appear — the Step 0 record itself names them with recorded
  grounds, which is exactly the honest basis the original census lacked. For eras
  whose Step 0 hasn't run, adjacent-register entries carry questions, not verdicts.
- The lane and era-scale design (1.5) now applies over the Atlas's nine proposed
  eras; the era structure itself is one of the open questions for Mark.

### 1.9 Seed relationship edges (V0.1, confidence-marked)

A non-exhaustive starter set — enough to prove the edge model carries real content.
Every edge below is participant-visible via hover.

| From → To | Type | Confidence | Note (hover text) |
|---|---|---|---|
| House-Churches → Syriac | formed | Contested | Aramaic-speaking Christianity reached Edessa early, but by what route and hands scholars genuinely disagree |
| House-Churches → Alexandria | formed | Widely Accepted | Egyptian Christianity's origins are obscure in detail, but its second-century emergence out of the same scattered network is broadly accepted |
| Alexandria → Desert | formed | Widely Accepted | The desert movement grew in Alexandria's shadow; Athanasius of Alexandria wrote the Life of Antony that carried it to the world |
| Desert → Bethlehem Circle | transmitted_to | Documented | Jerome and Paula toured the Egyptian ascetic settlements; the circle's practice consciously imported the desert's renunciation |
| Alexandria → Bethlehem Circle | transmitted_to | Documented | Origen's textual scholarship (the Hexapla) is the direct ancestor of Jerome's Hebrew-testing project — even as Jerome turned publicly against Origen's theology |
| Nicene-Cappadocian ↔ Bethlehem Circle | contemporary_with | Documented | Jerome heard Gregory of Nazianzus teach in Constantinople and calls him his teacher |
| Syriac → Church of the East | formed | Documented | The School of Nisibis and the Persian church carry this world's teaching directly onward after 410 |
| Desert → Byzantine monasticism | formed | Documented | Basil visited Egypt; the whole Greek monastic tradition claims the desert as its root |
| Desert → Benedictine | transmitted_to | Documented | John Cassian carried the desert's teaching to Gaul; Benedict's Rule commends his Conferences by name |
| Desert → Celtic monasticism | transmitted_to | Widely Accepted | Via Gaul (Lérins, Martin of Tours); the route is secure in outline, thinner in specifics |
| Coptic Christianity ← Desert + Alexandria | formed | Documented | Post-Chalcedon Egyptian Christianity is the direct continuation of both |
| Waldensians → Reformed | transmitted_to | Contested | The Waldensians adhered to the Reformation in 1532; how much earlier "proto-Protestant" continuity is real vs. retrospective is a live scholarly argument |
| Lutheran ↔ Anabaptist | reacted_against | Documented | The Radical Reformation defined itself against the magisterial reformers' church-state settlement as much as against Rome |
| Holiness → Pentecostal origins | formed | Documented | Azusa Street's leaders and vocabulary came directly out of the Holiness movement |
| Pentecostal origins → African-Initiated Churches | transmitted_to | Widely Accepted | Aladura and Zionist movements drew on Pentecostal currents while being genuinely African-initiated — the balance is actively studied |
| Methodist → Holiness | formed | Documented | The Holiness movement understood itself as recovering Wesley's own doctrine of sanctification |

---

## Part 2 — The Honest "Not Yet" Content

### 2.1 The discipline

Three constraints, all already established elsewhere in the project, govern every word
of this copy:

1. **No invented verdicts.** ⟦A⟧ Where a real Step 0 has run (Era I / Phase One),
   the copy states its recorded dispositions and grounds — selection, deferral, and
   exclusion reasoning are all on the record and may be quoted. Where no Step 0 has
   run (Eras II–IX), the copy must say "the assessment hasn't happened yet," never
   "the sources are too thin" — that claim hasn't been earned. What the copy *may*
   do is describe, accurately, what the assessment would have to weigh (the Atlas's
   sourcing/ecology/floor *signals*) — statements about the method and the evidence
   landscape, never pre-judgments of the result.
2. **The manifest's tone.** The live worlds' own tile copy already discloses
   sourcing-richness honestly ("Richest in… — thinner on…, since…"). The not-yet copy
   is the same voice pointed at absence instead of thinness.
3. **The readability floor.** 10th-grade reading level, per the already-decided
   Level 2 standard. A curious teenager should be able to read why a world isn't here
   and understand the answer.

### 2.2 The three-part honest frame (every not-yet explanation carries all three)

1. **Real and important.** Named plainly, without hedging, with one concrete line of
   what this movement carried.
2. **Why it isn't here.** The true general reason first: this project builds one world
   at a time, through a slow and demanding process, and has built four. Then the
   specific gate: before any world is built, we assess whether the right kind of
   sources survive — not just histories *about* a movement, but enough of its own
   inner voice (its prayers, letters, teaching, arguments, daily texture) to let an
   ordinary member of it speak honestly. For this movement, that assessment hasn't
   happened yet.
3. **Where to go meanwhile.** The nearest built neighbor, by lineage — turning a
   closed door into an open one.

### 2.3 Status-line copy (the short badge text, hover-level)

⟦A — updated to the corrected taxonomy⟧
- **Live:** "Open for conversation."
- **In Construction:** "Being built now — the construction records are real and we can show them."
- **Selected, Not Yet Built:** "Chosen — one of the nine worlds selected for this era. Construction hasn't begun." *(Alexandria variant adds: "Earlier construction work exists and is being re-grounded in the project's current method.")*
- **Deferred by Step 0:** "Considered for this era and held for a later one — the reasons are on record, click to read them."
- **Pre-Survey Candidate:** "Real history we haven't built yet — click to see why, honestly."
- **Excluded (grounds on record):** "Not in the conversation set — for a stated reason you can read in full. Exclusion is not a judgment of unimportance."

### 2.4 Full drafts

**Alexandria (Selected, Not Yet Built — the special case, real prior work): ⟦A⟧**

> This world has already been chosen. Alexandria — the catechetical tradition that
> read all of Scripture through the Logos, the Word who became flesh — is one of the
> nine worlds selected for this era after a real survey of the whole period, and it
> was one of the first worlds this project ever tried to build: a substantial body of
> construction work exists from an earlier version of our method, and that earlier
> work taught us most of what our current method knows. We hold every world to the
> standard of the method as it now stands, including the worlds we love most — so
> Alexandria waits until that earlier work is re-grounded and re-tested, rather than
> opening on the strength of documents we've since learned to improve. Chosen,
> wanted, not yet open. Meanwhile: the Desert Fathers and Mothers grew up in
> Alexandria's shadow, and the Bethlehem Circle inherited its scholarship — both are
> open now.

**Cappadocian world (Selected, Not Yet Built): ⟦A⟧**

> This world has already been chosen — one of the nine selected for this era: the
> communities around Basil of Caesarea, Gregory of Nazianzus, Gregory of Nyssa, and
> Macrina, where the words Christians still confess about the Trinity were being
> forged in real congregations, real letters, real grief. Nothing about it was judged
> too hard or too thin — it was selected on the strength of its sources; construction
> simply has not begun. This project builds one world at a time, slowly, because each
> one is checked against its actual surviving sources at every step. Meanwhile: the
> Bethlehem Circle is open, and its founder sat under Gregory of Nazianzus's teaching
> — you can hear that century from inside it now.

**Donatism (Selected, Not Yet Built — new in Amendment A): ⟦A⟧**

> This world has already been chosen — and it may surprise you that it's here: the
> churches of Roman North Africa that broke communion with their neighbors over what
> faithfulness under persecution required, kept their own bishops for a century, and
> built their identity on the memory of the martyrs. History mostly remembers them
> through their opponents — Augustine wrote against them, and the label "Donatist"
> was never their own name for themselves. That is exactly why this project chose
> them: a whole communion of real Christians, serious about holiness, known mainly
> through hostile pens, deserves to speak as itself. Construction has not yet begun.
> Meanwhile: the House-Churches are open — an earlier era's communities also holding
> costly convictions under pressure.

**Imperial and Juridical Christianity (Selected, Not Yet Built — new in Amendment A): ⟦A⟧**

> This world has already been chosen: the church that woke up one morning allied to
> the empire that had been killing it — Constantine's alliance, Ambrose facing down
> an emperor at the church door, popes building the machinery of a church that could
> outlast Rome itself. It is the era's least comfortable world and one of its most
> consequential: power, and what power does to a community formed by a crucified
> Lord, held honestly as the sources hold it. Construction has not yet begun.
> Meanwhile: the Bethlehem Circle is open — aristocrats of that same imperial world
> who gave its wealth and rank away.

**Latin Pastoral-Congregational Christianity (Selected, Not Yet Built — new in Amendment A): ⟦A⟧**

> This world has already been chosen: the ordinary congregational life of Latin
> North Africa — Cyprian steering his flock through plague and persecution,
> Augustine preaching to his own people at Hippo week after week, baptisms and
> penance and the daily care of souls under a bishop's office. Not the councils, not
> the controversies — the parish, long before that word existed. Construction has
> not yet begun. Meanwhile: the House-Churches are open — the same ordinary-assembly
> life, two centuries earlier and one sea away.

**Byzantine monasticism (Not Yet Assessed):**

> This is real and important: a thousand years of Greek-speaking monastic life, from
> the great houses of Constantinople to Mount Athos, carrying practices of prayer —
> including the continual prayer of the heart — that are still alive today. It isn't
> here yet, and the honest reason is ordinary: this project has built four worlds,
> one at a time, and hasn't reached this one. Before any world is built, we assess
> whether the right kind of sources survive — not just histories about the movement,
> but enough of its own inner voice to let an ordinary member speak honestly, at a
> level of evidence we can show you. For this movement that assessment hasn't happened
> yet. What it would weigh: rich monastic rules, hymns, and spiritual writings survive
> across many centuries — the question a real assessment would ask is which specific
> community and window of time could speak as *one* world, rather than a thousand
> years flattened into one voice. Meanwhile: the Desert Fathers and Mothers are open —
> the root this whole tradition claims.

**Coptic Christianity after Chalcedon (Not Yet Assessed, living tradition):**

> This is real and important: the church of Egypt after the council of Chalcedon in
> 451 — a communion that took the costlier road at that council's parting of ways, and
> has carried an unbroken witness through fifteen centuries, much of it under
> pressure, to this day. It isn't here yet. This project builds one world at a time
> and hasn't reached this one; the assessment of its sources hasn't yet been done. One
> more thing matters here: this is a living church. If this world is ever built, it
> would be a reconstruction of one historical window, bounded and evidence-checked —
> never a claim to speak for Coptic Christians today, whose own voice is theirs, not
> ours. Meanwhile: the Desert Fathers and Mothers are open — Antony and Pachomius,
> whom the Coptic church venerates, are that world's own teachers.

**Benedictine monasticism (Not Yet Assessed):**

> This is real and important: the Rule of Benedict quietly organized Western
> monastic life for a thousand years — a school for the Lord's service built on
> stability, obedience, and a daily rhythm of prayer and work. It isn't here yet, for
> the ordinary reason: four worlds are built, one at a time, and this one hasn't been
> reached. Before building, we assess whether enough of a community's own inner voice
> survives — for this movement that assessment hasn't happened yet. What it would
> weigh: the Rule itself survives, and so do customaries and chronicles, but a real
> assessment would ask which century and which houses could speak honestly as one
> lived world — sixth-century Monte Cassino, Carolingian reform houses, and Cluny at
> its height are three quite different worlds sharing one Rule. Meanwhile: the Desert
> Fathers and Mothers are open — Benedict's Rule itself commends their teachers by
> name.

**Anabaptist / Radical Reformation (Not Yet Assessed, living tradition):**

> This is real and important: the communities of the Radical Reformation — Swiss
> Brethren, Hutterites, Mennonites — who concluded that following Jesus meant baptism
> as a chosen allegiance, refusal of the sword, and a church free of state power, and
> who paid for those convictions in martyrdom recorded by their own hand. It isn't
> here yet: this project builds one world at a time and hasn't reached this one, and
> the assessment of its sources hasn't yet been done. What that assessment would
> weigh: this movement is unusually rich in ordinary members' own words — court
> testimonies, hymns written in prison, the Martyrs Mirror — exactly the kind of
> inside-voice evidence our method looks for; and it is a living tradition, whose
> present-day communities' self-understanding would be held distinct from any
> historical reconstruction. Meanwhile: the House-Churches are open — small
> assemblies holding costly convictions under pressure is where the whole story
> begins.

**Pentecostal origins — Azusa Street (Not Yet Assessed, living tradition):**

> This is real and important: the revival at 312 Azusa Street in Los Angeles,
> 1906 — an interracial congregation led by William J. Seymour, the son of freed
> slaves, from which the fastest-growing Christian movement on earth traces its
> descent. Perhaps a third of a billion people today worship in ways this small
> mission shaped. It isn't here yet: this project builds one world at a time, has
> built four — all ancient so far — and hasn't reached the modern era. The assessment
> of this movement's sources hasn't yet been done. What it would weigh: newspapers,
> the mission's own periodical, and participants' memoirs survive in quantity — a
> real assessment would test how directly those let an ordinary participant speak,
> and how to hold a story that several living traditions tell differently. Meanwhile:
> the Desert Fathers and Mothers are open — an earlier movement convinced that the
> Spirit's power was present and transforming now, not only in the past.

**The Black Church in America (Not Yet Assessed, living tradition):**

> This is real and important: the church forged by enslaved Africans in America —
> praying in secret in "hush harbors," hearing Exodus as their own story, building
> after emancipation the institutions that carried a people — a tradition whose
> preaching, music, and endurance have marked the whole church since. It isn't here
> yet: this project builds one world at a time and hasn't reached this one, and the
> assessment of its sources hasn't yet been done. What that assessment would weigh:
> spirituals, slave narratives, sermons, and church records survive — powerful
> inside-voice evidence, gathered under conditions that silenced much more, and a
> real assessment would name whose voices the record structurally suppressed, as our
> method requires of every world. This is a living tradition; any historical window
> built here would never claim to speak for the Black church today. Meanwhile: the
> House-Churches are open — assemblies holding faith and freedom together under
> powers that permitted neither.

**Chinese house-church movement (Not Yet Assessed, living tradition, near-present):**

> This is real and important: the unregistered congregations of China, which carried
> faith through decades when every public church was closed, and grew — nobody knows
> exactly how much, which is itself part of the story — into one of the largest bodies
> of Christians in the world. It isn't here yet, and this one carries an extra
> honesty: beyond the ordinary reason (four worlds built, one at a time, none modern
> yet), a movement this recent and this exposed raises questions our method takes
> seriously — much of its inside voice is unpublished, oral, or unsafe to publish, and
> real people could be affected by how their story is told. No assessment has been
> done; if one ever is, those questions come first. Meanwhile: the House-Churches of
> the second century are open — the resemblance is not an accident, and they would
> recognize much.

**Template for remaining Not Yet Assessed entries** (every entry still gets its own
movement-specific first and last paragraphs before shipping — no entry ships as bare
template):

> This is real and important: [one concrete sentence of what this movement carried].
> It isn't here yet, and the honest reason is ordinary: this project has built four
> worlds, one at a time, and hasn't reached this one. Before any world is built, we
> assess whether the right kind of sources survive — not just histories about a
> movement, but enough of its own inner voice to let an ordinary member of it speak
> honestly, at a level of evidence we can show you. For this movement, that
> assessment hasn't happened yet. [Where known and accurate: one sentence on what the
> assessment would weigh.] Meanwhile: [nearest built neighbor, by lineage, with the
> connecting thread named].

### 2.4a Era-positioning lines for the live worlds — future `cic-poc` handoff, NOT for now

Per Mark (2026-07-16): with the map's Constantine split adopted (Era Ia / Era Ib),
each live world's tile description *may* eventually gain one era-positioning line —
**to be implemented in `cic-poc` only after Prototype Testing 1**, by the front-end
thread, not by this one. Drafted here so the handoff is copy-paste ready:

- **The House-Churches (Chloe):** "Formed before Constantine — a church with no
  empire behind it, and sometimes one against it."
- **Syriac Christianity (Mar Yausep):** "Spans the divide — and from the other side
  of it: beyond Rome's border, Constantine's conversion made things harder, not
  easier." *(The divide is a Roman story; this world's copy must not imply it was
  everyone's story.)*
- **Desert Fathers and Mothers (Papnoute):** "Formed in the empire's first Christian
  century — when the harder question had become what faithfulness costs once it is
  safe."
- **The Bethlehem Circle (Albina):** "Formed in the imperial church's high noon —
  and walked away from what it offered."

These lines change *positioning only*; no world's build, boundaries, or description
substance changes. The manifest's existing sourcing-richness disclosures stay
untouched.

### 2.5 What this copy never does

- Never says or implies a movement was judged unimportant.
- Never fabricates a Source Ecology verdict, positive or negative.
- Never lets "not yet assessed" read as a euphemism for "rejected" — the census's
  whole tone treats the unbuilt map as the project's future, not its discard pile.
- Never implies a living communion is a historical artifact.
- Never promises a build date or sequence not actually decided.

---

## Part 3 — The Five-Step Interaction Flow

### 3.1 Visual grounding — the pattern this map belongs to

Mark's reference point — "who lived in relationship to whom," Bible-history style —
belongs to a real, old visual tradition worth naming so the concept stays concrete:

- **Priestley's *Chart of Biography* (1765)** — the origin of the horizontal lifespan
  bar: time flows left to right, each life is a line, and simultaneity becomes
  *visible* instead of computed. Our Figure lines (1.7) are exactly this, nested
  inside movement bands.
- **Adams' *Synchronological Chart of Universal History* (1871)** — the wall-chart
  ancestor of every "Bible timeline" poster: parallel civilizational streams flowing
  left to right, widening and narrowing, with era-dense regions given more room. Our
  lanes and piecewise time scale are this pattern.
- **Sparks' *Histomap* (1931)** — streams whose *width* encodes relative presence;
  useful precedent if the map ever wants band thickness to mean anything (V0.1
  deliberately keeps thickness uniform — width-as-importance is a historical claim we
  haven't earned).
- **Modern interactive equivalents** — horizontally scrolled, zoomable timelines
  (TimelineJS-style) and relationship-stream charts. The interaction budget below
  assumes only: horizontal scroll, hover, click, and a selection tray. No zoom, no
  drag-rearrange, no physics — V0.1 is a *scrolling chart that answers questions*,
  not a simulation.

### 3.2 The two-level grammar (hover vs. click) — inherited, not invented

The project already has one interaction grammar: **hover for the short honest
explanation, click for the full depth** — built for lexicon terms, extended to
stories, quotes, sourcing, and closing resources. The map extends it to two further
content types (as the 2026-07-07 World Map log entry anticipated):

- **A world/movement** — hover: identity card + quick actions; click: the full panel.
- **"Why isn't this here"** — hover: the status line (2.3); click: the full honest
  explanation (2.4).

And one new content type this spec adds:

- **A figure** (Ephrem, Benedict, Seymour…) — hover: name, dates, one-line role;
  click: a short panel that includes the honest single-figure boundary, in the
  Facilitator's already-decided framing: *a single historical person's exact voice
  can't be reconstructed at the confidence this project requires — but the world that
  formed people like them can be, and here it is on the map.* Every figure panel
  points back to its movement band. This turns the most predictable disappointment
  ("let me talk to Augustine") into the map's own teaching moment.

### 3.3 Rendering the transparency layer

- **Build status is the brightness of the map.** Live worlds render in full saturated
  color (each world's existing manifest color: violet, amber, teal, magenta).
  Identified Candidates render outlined with a light fill. Not Yet Assessed renders
  dimmed but *fully readable and fully interactive* — dimmed is an honest state, not
  a disabled state. Nothing on the map is hover-dead.
- **A persistent legend** states the counts plainly: "4 worlds open for conversation ·
  2 named for the future · the rest: real history we haven't built yet — every band
  is clickable." The legend is the map's thesis statement.
- **Edges render by confidence:** Documented/Widely Accepted as solid lines;
  Dominant Modern Reconstruction as long dashes; Contested/Inferential-Thin as dotted,
  with the hover note always naming the uncertainty in words. The map never draws an
  arrow it can't defend on hover.
- **The context strip** (councils, persecutions, empires, 1054, 1517) is muted and
  non-interactive except for plain hover labels — it orients, it doesn't compete.
- **The founder-prophet designation ⟦added 2026-07-16, Mark's decision⟧:** entries
  whose authority structure rests on a named individual's revelation or personal
  standing (the Step 0 record's person-defined / Criterion 2 ground) carry a
  visible mark, two tiers never flattened: **✦** where the ground is on record or
  stated in the movement's own confession (10 entries: Montanism, Novatianism,
  Shakers, Swedenborgians, LDS, JW, Christian Science, Oneida, the
  INC/Way/Unification/Luz cluster, Branch Davidians); **✧** where the check is a
  question a future Step 0 must run and may well clear (12 entries: the
  Joachimites, Savonarola's Observance, Family of Love, Kimpa Vita's movement,
  Haugeans, Adventism/Ellen White, Catholic Apostolic, Plymouth Brethren, the
  AICs' founder-succession cases, the Chinese founder-defined branches, the
  Catholic founder-charism movements, Taizé & Iona). The mark is orthogonal to
  lane and creedal status — that orthogonality is the point: it says what kind of
  authority question exists, never where a movement stands on the floor. Carried
  as a census field (`c2`), rendered on bands, tooltips, and panel badges.

### 3.4 The five steps, as a participant actually moves through them

**Step 1 — Introduce the world.**
Entry state: the map opens scrolled to wherever the participant's attention should
start — default, the ancient era where the four Live worlds cluster, with all four
glowing at full color amid the dimmed landscape. First-visit only: a three-sentence
overlay in the project's own voice ("Two thousand years of Christians have known
Jesus from inside very different worlds. Four of those worlds are open for
conversation today. The whole map is real — and honest about what's built and what
isn't.") with one action: *Look around.* Hovering any Live band shows the identity
card: name, dates, region, the manifest description's first clause, status badge, and
quick actions — **Add to conversation · Learn more · Take a tour** *(tour renders as
a visible placeholder marked "coming later," consistent with the world-click menu's
already-decided placeholder discipline)*.

**Step 2 — Orient the user within Christian history.**
The scrolling itself is the orientation instrument: lanes make communion families
visible, the context strip anchors dates to events a participant may half-know
(Nicaea, the Schism, 1517), and the era-segmented scale keeps the ancient world from
vanishing into a sliver. Figure lifespan lines inside bands answer "who lived when,
in relationship to whom" at a glance — Priestley's trick, unchanged in 260 years.
Hovering empty lane space in any era surfaces a quiet affordance: "What was happening
here?" → one-line era summary from the context strip.

**Step 3 — Show relationships to other worlds.**
Hovering any band highlights its edge neighborhood: incoming lineage, outgoing
transmission, contemporaries — everything else drops back slightly. Edge hover shows
the one-sentence note with its confidence in words ("Documented: Cassian carried the
desert's teaching to Gaul…"). Clicking a band opens the full panel (3.5), whose
**Relationships** section lists the same edges as prose with links that pan the map
to the related band. This is where Conviction 1 becomes visible mechanics: no world
is an island on this map, and the participant *sees* the vast testimony as a
connected whole before choosing a voice within it.

**Step 4 — Help them decide where to go.**
Two mechanics, both already grounded in decided design:
- **The selection tray** (bottom edge, persistent): "Add to conversation" from any
  Live band's hover card or click panel places it in the tray. One world in the tray
  reads as a **Deep Interview** ("a long conversation with one voice"); two or three
  read as **Compare Worlds** ("hear how different worlds answer the same question") —
  the same two entry modes already raised in the front-end thread, surfaced here as a
  natural consequence of how many worlds you picked rather than an upfront mode
  switch. The tray enforces the ceiling (the five-Representative limit; within
  current `cic-poc` reality, effectively "up to 3–4 for a readable table" — final cap
  is the front-end thread's call at integration time).
- **The honest redirect.** Every non-Live panel ends with its `nearest_live_neighbor`
  as a live suggestion: "You can't enter this world yet — but the Desert Fathers and
  Mothers are its direct ancestors, and they're at the table now. [Add them]." A
  participant who came looking for Athos leaves with Papnoute instead of leaving
  empty-handed — and knows exactly why, having been told the truth.

**Step 5 — Launch them into conversation.**
The tray's single action: **Sit down at the Table.** Confirmation shows who will be
seated (name, world, dates — the same introduction framing the Facilitator will
speak), and hands off to the existing conversation entry. The map does not reimplement
onboarding, role selection, or the Facilitator's greeting — it delivers a
world-selection payload (list of world ids + implied mode) to the door of the
existing flow and steps aside. *(In the standalone V0.1 concept demo, this step
terminates at a plain screen stating what would happen — honest even about its own
unbuilt edges.)*

### 3.5 The click panel — one structure for every band

Aligned with the already-decided four-option world-click menu (Description / Tour /
Choose for Table / Academic Documents), extended with the map's own honesty section:

1. **Identity header** — name, subtitle, dates, region, status badge, lane.
2. **Description** — Live: the manifest copy verbatim, richness disclosure included.
   Non-Live: the Part 2 explanation.
3. **Relationships** — prose edges with confidence words and pan-to links.
4. **Sourcing status** — Live: the world's sourcing-richness line plus a pointer
   toward the future Academic Documents feature (placeholder). Non-Live: what
   assessment has and hasn't happened, in exactly the Part 2 language.
5. **Actions** — Live: *Choose for Table* (functional) · *Tour* (placeholder) ·
   *Academic Documents* (placeholder). Non-Live: *Add nearest built neighbor* only.
   ⟦"Notify me when this changes" was cut 2026-07-16 — no notification
   infrastructure exists or is planned, and the button would quietly force the
   unresolved accounts question; it may return as a real feature via the front-end
   thread if accounts ever exist.⟧

---

## Part 4 — Future-Integration Note (Handoff Proposal, Not a Build Task)

*Addressed to the front-end thread, to evaluate on its own timeline.*

**What exists when this thread's work matures:** a specified data model (Part 1), a
reviewed census with participant-facing honest copy (Parts 1–2), and a concrete
interaction design (Part 3) — none of it in `cic-poc`.

**Where it could connect, in increments the front-end thread can take or leave:**

1. **Cheapest first step — the data, not the map.** The census schema deliberately
   extends the existing `WorldManifestEntry` pattern (same tone, same fields where
   they overlap). `cic-poc` could adopt the landscape data file as a static asset and
   surface *only* the "why isn't X here?" content through the existing Ask-the-
   Facilitator surface — honest not-yet answers, zero new UI. This alone discharges a
   real transparency gap (a tester who asks "why only ancient worlds?" today gets an
   improvised answer).
2. **Middle step — map as supplementary view.** Keep the current selection tiles as
   the default; add "See these worlds in history" opening the map as an orientation
   layer. The map's tray then feeds the existing selection state. This tests whether
   the map actually helps decisions before it owns them, at low regret.
3. **Full step — map as the selection surface.** The map replaces the tile list; the
   Deep Interview / Compare Worlds distinction becomes emergent from tray count
   (this map's step 4) rather than an upfront toggle — which dovetails with that
   thread's own still-open entry-point question. Only worth deciding after the middle
   step has been observed with real participants.

**What this thread asks of the front-end thread now:** nothing. When the census and
copy have been through Mark's review, this note becomes the handoff; the integration
decision, its timing, and the tray-ceiling question belong there.

**One seam worth naming early** (echoing the Engineering Considerations Catalog's
world-data-schema entry): if any new world metadata gets added to `cic-poc` before
this map integrates, adding it in the manifest's single-source-of-truth pattern —
and keeping tile copy, sourcing disclosures, and colors in that one place — keeps the
eventual map integration a data-plumbing task instead of a migration.

---

## Open questions for Mark (V0.1 → V0.2) ⟦A — updated⟧

1. **Atlas review.** The Atlas (~110 within-floor candidates + ~25 adjacent-register
   entries across nine eras) supersedes the old census question. What's missing that
   would grieve you to see missing? Which era intros or signals read wrong to you?
2. **Era boundaries.** ⟦RESOLVED 2026-07-16 — Mark confirmed all ten eras as the
   entry screen's pickable objects: Ia 70–312 (The Early Church Era) · Ib 312–451
   (The Imperial Church Era) · 451–622 · 622–1054 · 1054–1300 · 1300–1517 ·
   1517–1650 · 1650–1815 · 1815–1906 · 1906–present. Phase One spans Eras Ia–Ib
   deliberately. Map eras organize reading; future release-phase windows remain
   each phase's own Step 0 decision.⟧
3. **Lane 4's grouping and label.** ⟦RESOLVED 2026-07-16 — seven-lane architecture
   (1.5): Lane 4 is plainly **Africa** (Nile spine → AICs → diaspora, one
   continuous lane); Armenia and Georgia get their own **Caucasus** lane (whose
   internal 607 split teaches); Georgia leaves the old grouping for good reason
   (it is Chalcedonian); Latin North Africa stays in the Latin lane with the
   tie-break stated honestly in the legend. Census carries per-entry lane
   assignments from V0.5.⟧
4. **Adjacent-register rendering.** ⟦RESOLVED 2026-07-16 — un-run eras' register
   entries ship at V1 with question-framed copy. The map's thesis is that honesty
   about the unresolved is itself trustworthy; hiding real movements until their
   Step 0 runs would be the silent omission the Historical Responsibility value
   forbids. The copy discipline (questions in the Methodology's own vocabulary,
   never verdicts) is the guardrail that makes this safe.⟧
5. **"Notify me when this changes."** ⟦RESOLVED 2026-07-16 — **cut.** No
   notification infrastructure exists or is planned, and the button would quietly
   force the unresolved accounts/identity question (it needs an address to notify).
   A "planned" label for something with no plan is a soft over-promise — against
   the project's own posture. If accounts ever exist, this can return as a real
   feature via the front-end thread. Section 3.5's action list updated
   accordingly.⟧
6. **Standalone demo.** ⟦RESOLVED 2026-07-16 — **yes, as a design artifact owned by
   this thread**: an interactive V0.1 concept demo (built; see
   `map_demo` artifact) implementing the five-step flow against the real census —
   scrolling era-scaled lanes, status-honest rendering, hover/click, the selection
   tray with Deep Interview / Compare Worlds emerging from seat count, and an
   honest launch stub. It exists to let Mark and reviewers *feel* the design.
   Whether pilot testers ever see it is the pilot/front-end thread's call — this
   thread's recommendation: after their sittings, not before (the pilot tests
   conversation quality; a map shown first would reframe expectations mid-test).⟧
