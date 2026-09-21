---
id: gallic.term.sarabaite
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Single-voice (Cassian), Marseilles only, framed as Egypt's own name ("rightly named in the
    Egyptian language Sarabaites"). No one at Tours uses the word, though Anatolius wears the
    profession falsely there. Gibson's footnote on the name's etymology is editorial.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.4, 7 ("the reprehensible"; "rightly named in the Egyptian language Sarabaites"; "renunciation only as a public profession"; "their own masters"; "two or three together"; "the lukewarmness of their purpose"); XVIII.8 (the fourth kind)'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - what a "Sarabaite" is; whether there were false monks
  - what Cassian's third kind of monk was
  - participant uses "Sarabaite," "fake monk," "monks who live on their own," "no abbot"
  - Conf. XVIII.7
  prefer_instead:
  - the question is about monks in general (retrieve monk / solitary)
  - the question is about the house as such (retrieve monastery / coenobium)
  - Tours, where the word is not used
relations:
- type: associated-with
  target: gallic.term.anchorite-hermit
- type: associated-with
  target: gallic.term.customs-of-the-monasteries
- type: associated-with
  target: gallic.term.lukewarmness
- type: associated-with
  target: gallic.term.monastery-coenobium
- type: associated-with
  target: gallic.term.monk-solitary
- type: associated-with
  target: gallic.term.profession
- type: associated-with
  target: gallic.term.renunciation
- type: associated-with
  target: gallic.term.elder-senior-abbot
- type: associated-with
  target: gallic.term.tradition
- type: associated-with
  target: gallic.term.bloodless-martyrdom-confessor
plain_meaning: >-
  Egypt's name, kept by Cassian, for the false third kind of monk. He renounces the world only
  before men's eyes, lives two or three together, and stays his own master under no elder.
world_word: Sarabaite
false_friend: []
senses:
  informational: >-
    Abbot Piamun's name for the "reprehensible" third kind of monk, "rightly named in the Egyptian
    language Sarabaites" - those who make "their renunciation only as a public profession, i.e.,
    before the face of men," build cells "and calling them monasteries remain in them perfectly free
    and their own masters," never submitting to the will of the Elders. A fourth kind, the false
    anchorite, takes the name of the desert without its training.
  evidential: >-
    Attested in Cassian alone (Conf. XVIII.4, 7, 8), as Piamun's received Egyptian category.
    Gaul hears it as Egypt's name; Tours never uses it.
  personal: >-
    Our name for a monk without a boundary - the category exists to be avoided, not classified.
  translational: >-
    Not a recognized order or a later rule's judgment on small communities, but Egypt's own name,
    used inside our houses, for a specific failure: renunciation performed in public and never
    submitted to an elder.
quick_meaning: >-
  Cassian's third kind of monk, "rightly named" by Egypt. He renounces the world for show, lives
  two or three together, and answers to no elder. A monk without a boundary.
distortion_risk: low
---
Built from Doc_06 entry 069 (`galliclex069_sarabaite.md`, Tier 3, tags SC TC; Doc_03 1.4). Kept
intentionally thin at the Tier-3 floor: the chunk's own Distortion Risk section names only a
mild "recognized order / Benedictine-era judgment" hearing, so false_friend is [] and
distortion_risk: low.

Every one of the chunk's Related-Terms (monk / solitary, monastery / coenobium, anchorite / hermit,
renunciation, profession, lukewarmness, elder / senior / abbot, tradition, the customs of the
monasteries / Institutes, bloodless martyrdom / confessor) was batch 1 / not built when this record
was authored, so relations[] was left empty by decision; all ten were added as associated-with
relations at the cross-batch reconciliation pass once all 81 term records existed.
