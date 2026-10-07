---
id: gallic.term.catechumen
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Single-voice (Sulpitius, Tours). The historicity of the raised catechumen falls under virtus /
    power's Reported-Experience Status. Roberts's footnotes on baptismal regeneration are editorial.
    No Latin lemma sought.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. II ("begged that he might become a catechumen"); ch. III ("Martin, who is still but a catechumen, clothed me with this robe"); ch. VII (the catechumen raised)'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'II.4 ("he made them all catechumens, by placing his hand upon the whole of them"; "that plain where the martyrs were wont to be consecrated")'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - whether Martin was baptized as a child; what a catechumen was
  - why the cloak vision matters
  - how a whole crowd could be "made catechumens"
  - participant uses "catechumen," "unbaptized," "baptism," "enrolled"
  - Vita II-III; the raised catechumen of Vita VII; Dial. II.4
  prefer_instead:
  - the question is about the mission in general (retrieve heathen / rustics)
  - the monastic sense of "conversion" (retrieve conversion)
  - later catechumenate rites
relations:
- type: associated-with
  target: gallic.term.possessed-exorcism
- type: associated-with
  target: gallic.term.heathen-rustics
- type: associated-with
  target: gallic.term.conversion
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.soldier-of-christ
- type: associated-with
  target: gallic.term.monk-solitary
plain_meaning: >-
  One enrolled but not yet baptized. Martin was one for years, as a boy and a soldier; Christ
  named him so in the cloak vision; a whole heathen crowd was made catechumens by his one hand.
world_word: catechumen
false_friend:
- a brief administrative waiting period before an expected infant baptism
senses:
  informational: >-
    Martin at ten "begged that he might become a catechumen." Still a catechumen as a soldier, he
    gave half his cloak, and that night heard Christ say, "Martin, who is still but a catechumen,
    clothed me with this robe." At his first monastery a catechumen died "without receiving
    baptism," and Martin restored him to life - the first of his powers made known. On the plain
    outside Tours "he made them all catechumens, by placing his hand upon the whole of them."
  evidential: >-
    Attested in Sulpitius alone (Vita II, III, VII; Dial. II.4).
  personal: >-
    The catechumen is where the north's power and mission meet a single body - the state Martin
    was in when Christ wore his cloak, and the state of the first man he raised.
  translational: >-
    Not a short waiting period before a near-default infant baptism: at Tours the state could last
    years into adult soldiering, and it is where our literature locates the first breaking-through
    of Martin's power.
quick_meaning: >-
  One enrolled but not yet baptized. Martin stayed one for years, into his soldiering. The first
  man he raised was one. He made a whole crowd catechumens with one hand.
distortion_risk: low
use_note:
  means: "A catechumen was one enrolled but not yet baptized, as Martin stayed for years, as the first man he raised was, and as a whole crowd became by his hand."
  not_for:
    - "a brief administrative wait before an expected infant baptism"
    - "the mission to the pagan countryside in general, which sits in gallic.term.heathen-rustics"
    - "the monastic sense of turning, which sits in gallic.term.conversion"
    - "later catechumenate rites"
  years: {from: 397, to: 406}
  status: reviewed
---
Built from Doc_06 entry 081 (`galliclex081_catechumen.md`, Tier 3, tags SC TC RT; Doc_03 8.3).
Kept thin at the Tier-3 floor.

Related-Terms also names conversion, virtus / power, bishop / the monk-bishop, soldier of Christ,
and monk / solitary - cross-batch at authoring time, added as relations (typed associated-with) at
the reconciliation pass once all 81 term records existed. The chunk also names blessing (in-batch);
not made a relation, since no dependency is stated.
