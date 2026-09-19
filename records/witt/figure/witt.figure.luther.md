---
id: witt.figure.luther
world_id: lutheran-wittenberg-and-its-congregations
record_type: figure
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as to existence, office, and reputation: directly attested across nine of this library's
    own vendored sources, spanning a dated letter (1517), a disputation, sermons, an exposition, a
    ballad, a catechism pair, and a confession his own colleague drafted and signed. No vendored primary
    text in this library gives a birth date. His life is understood, per this world's own already-
    established closing boundary (witt.core.witt.thinness: "the years after our founder's own life
    closed... after 1546"), to run into 1546 - a boundary this record treats as already settled by that
    record, not independently re-derived here. Every individual story below carries its own tier and its
    own, sometimes lower, confidence (Tier 2 for the Table Talk retellings, Contested for the household
    exchange); this record's own Documented rating covers Luther's existence, office, and general
    conduct across the library, not the wording of any one collected reminiscence.
sources:
- source_id: witt.source.luther-disputation-on-the-power-and-efficacy
  locus: Letter to Albrecht of Mainz, 31 October 1517; the Ninety-Five Theses
  license: public-domain
- source_id: witt.source.luther-selections-from-the-table-talk
  locus: >-
    Augsburg before Cajetan (1518), Worms (1521), household conversation with Katharina, the 1532 prayer
    for rain - Luther's own later retellings and sayings, collected by students
  license: public-domain
- source_id: witt.source.luther-ein-neues-lied-wir-heben
  locus: Hymn V, the Brussels martyrs' ballad (1523), written in Luther's own hand
  license: public-domain
- source_id: witt.source.luther-eight-wittenberg-sermons
  locus: The Eight Wittenberg Sermons (March 1522), preached in his own voice to his own congregation
  license: public-domain
- source_id: witt.source.luther-magnificat-translated-and-explained
  locus: The Magnificat exposition (1520-21), composed for the young Duke John Frederick
  license: public-domain
- source_id: witt.source.johann-letter-of-reminiscence-on-luther-as
  locus: Walter's own testimony to Luther's work on the German Mass (1526)
  license: public-domain
- source_id: witt.source.luther-large-catechism
  locus: The Large Catechism (1529), the founder's own reception complaint (G13)
  license: public-domain
- source_id: witt.source.luther-small-catechism
  locus: The Small Catechism (1529), the household program
  license: public-domain
- source_id: witt.source.johann-eyewitness-report-of-luthers-first-invocavit
  locus: Kessler's independent eyewitness corroboration of the first 1522 sermon
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - a participant asks who Luther was, or wants any of the nine stories this library holds him in
  do_not_retrieve_when:
  - a participant wants a biographical detail this library does not attest - no birth date, no physical
    description, no personal anecdote beyond what the nine linked stories themselves state
names:
- name: Doctor Martin Luther
  tag: in-world
- name: Martin Luther (letter dated 1517; no birth or death date attested in this library)
  tag: scholarly
dates:
  display: >-
    Directly attested in this library's own sources from 31 October 1517 (the letter to Albrecht) to 9
    June 1532 (the prayer for rain); no vendored primary text held here gives a birth date. His life is
    understood to run into 1546, per this world's own already-established closing boundary
    (witt.core.witt.thinness) - a boundary this record treats as given, not independently re-derived
    from any source of its own.
narratable: true
bridge_line: >-
  The friar who wrote privately to an archbishop about indulgences in 1517, stood before a cardinal and
  then an emperor rather than take his own words back, came home from hiding to preach his own
  congregation back from its excesses, wrote a ballad for two young monks burned at Brussels, worked out
  a German Mass tone by tone with his own musician, and led his whole town in prayer through a drought.
relations:
- type: associated-with
  target: witt.story.letter-to-albrecht-and-theses-circulation
- type: associated-with
  target: witt.story.augsburg-before-cajetan
- type: associated-with
  target: witt.story.worms-1521
- type: associated-with
  target: witt.story.brussels-martyrs
- type: associated-with
  target: witt.story.return-and-the-eight-sermons
- type: associated-with
  target: witt.story.composing-the-magnificat
- type: associated-with
  target: witt.story.first-german-mass-sung
- type: associated-with
  target: witt.story.household-and-kate-on-prayer
- type: associated-with
  target: witt.story.prayer-for-rain-1532
---
The founder-figure this whole library's own narrative material orbits: subject or author of nine of the
twelve stories in Doc_09's inventory, across every tier this library holds (Tier 1: the letter, the
sermons, the Magnificat composition, the Brussels martyrdom itself; Tier 2: the Table Talk retellings of
Augsburg and Worms, the household exchange, the rain prayer, Walter's testimony to the German Mass).
Narratable: true, argued directly - he is directly, verbatim attested across nine independently-read
vendored sources spanning three decades of this world's own window, in his own written hand (the
letter, the ballad, the catechisms), in his own preached voice (the sermons), and in his own later
retellings (Table Talk). Nothing about whether he can be narrated is in doubt; what varies, story by
story, is the tier and confidence of each particular telling - which each linked story record argues
for itself, and which this record does not re-argue or flatten into one blanket confidence.

What this record does not supply, and what no downstream use should invent: a birth date, a physical
description, any personal history before 1517, or any of the wider Luther corpus this library has not
vendored (his correspondence beyond the Albrecht letter and Walter's, his lectures, his translation
work as a described process, his later controversial writings named but disclosed rather than narrated
per Doc_02 SS12.3-SS12.4 - On the Jews and Their Lies is not a source for any story in this inventory
and this record does not narrate it). The founder's own testimony about his congregations' failings
(G13, Doc_04 - "hearers and repeaters of words") is carried in witt-S05 and witt-S12, but per Doc_04's
own barred-upgrade rule, is never usable as independent evidence that any actual parish was in fact
ignorant or negligent - only that Luther said so, repeatedly, in his own voice.

FEC / GRAVITY LINKAGE (parked for B-5; no gravity/force records exist yet for this world, so no
relations[] entry points at one, the same handling the Gallic and Cappadocian B-4 precedents used for
the identical situation): load-bearing across nearly every gravity this world's Doc_04 names. Directly,
through the nine linked stories: G1 (Primary, witt-S01, witt-S04, witt-S09), G2 (Primary, witt-S02,
witt-S03, witt-S05), G3 (Primary, witt-S05), G4 (Primary, witt-S06, witt-S08), G6 (Supporting,
witt-S03), G7 (Supporting, witt-S04, witt-S05), G8 (Tensional, witt-S08, witt-S12), G9 (Supporting,
witt-S06), G11 (Supporting, witt-S07), and G13 (Tensional, witt-S12, and load-bearing generally - Doc_04
names Luther's own testimony as G13's entire evidentiary basis, "the founder's own testimony... always
as a complaint about others' negligence"). When B-5 runs, this figure record should gain associated-
with edges to most or all of these gravity records, with reciprocal edges declared on each.
