---
id: gallic.term.kingdom-within
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Single-voice (Cassian), Marseilles only - Abbot Moses's and Abbot Piamun's readings of Luke
    17:21, received from Egypt. The reading is not used at Tours.
sources:
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'I.13 ("the kingdom of God is within you"; "knowledge or ignorance of truth, and delight either in vice or in virtue"; "a kingdom for the devil or for Christ in our heart")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.16 ("the doors of our cell or the recesses of the desert"; "no one is more my enemy than my own heart")'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - how Cassian reads "the kingdom of God is within you"
  - whether the kingdom is a place
  - why walls and deserts cannot protect an impatient heart
  - participant uses "kingdom within," "Luke 17:21," "interior kingdom"
  - Conf. I.13 or XVIII.16
  prefer_instead:
  - the question is about the goal/end pair (retrieve goal and end)
  - the kingdom as eschatological end only
  - Tours, where the reading is not used
relations:
- type: associated-with
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.contemplation
- type: associated-with
  target: gallic.term.goal-and-end
- type: associated-with
  target: gallic.term.purity-of-heart
- type: associated-with
  target: gallic.term.thoughts
- type: associated-with
  target: gallic.term.cell
- type: associated-with
  target: gallic.term.anchorite-hermit
- type: associated-with
  target: gallic.term.humility
plain_meaning: >-
  Abbot Moses's reading of "the kingdom of God is within you." The heart is a land under one of
  two kings, and no cell wall or desert can guard it for us.
world_word: the kingdom within / the kingdom of the devil
false_friend:
- '"the kingdom of God is within you" as a comforting platitude about spirituality residing inside a person'
senses:
  informational: >-
    Since the Lord says "the kingdom of God is within you," Moses tells the two Gauls, "nothing
    else can be 'within you,' but knowledge or ignorance of truth, and delight either in vice or in
    virtue, through which we prepare a kingdom for the devil or for Christ in our heart." Piamun
    turns the same verse against the monk who trusts his surroundings: if patience rests "in the
    doors of our cell or the recesses of the desert," we hope in vain, for "no one is more my enemy
    than my own heart."
  evidential: >-
    Attested in Cassian alone (Conf. I.13; XVIII.16), received as Moses's and Piamun's teaching.
  personal: >-
    The cell keeps the body still; it cannot keep the kingdom. Our whole interior discipline is the
    taking of the heart for Christ.
  translational: >-
    Not a soothing word about inner spirituality. For us the heart is contested ground, actively
    ruled by one of two kings, and the verse is a warning that walls and distance cannot secure a
    heart that remains its own worst enemy.
quick_meaning: >-
  Moses's reading of "the kingdom of God is within you." The heart belongs to the devil or to
  Christ, and no cell wall or desert can hold it for us. "No one is more my enemy than my own
  heart."
distortion_risk: low
use_note:
  means: "The kingdom within meant Abbot Moses's reading that the kingdom of God is within you: a heart ruled by the devil or Christ, which no cell wall can guard."
  not_for:
    - "a comforting platitude that spirituality lives inside a person"
    - "the pair of goal and end, which sits in gallic.term.goal-and-end"
    - "the kingdom as the eschatological end only"
    - "a Tours teaching, where the reading is not used"
  years: {from: 426, to: 435}
  status: reviewed
---
Built from Doc_06 entry 073 (`galliclex073_kingdom-within.md`, Tier 3, tags SC TC; Doc_03 4.12).
Kept thin at the Tier-3 floor. canon_cells: F4-P because Piamun's "no one is more my enemy than
my own heart" is a direct answer to someone who cannot quiet their own mind.

Related-Terms also names goal and end, purity of heart, thoughts, cell, anchorite / hermit,
contemplation, and humility - cross-batch at authoring time, added as relations (typed
associated-with) at the reconciliation pass once all 81 term records existed.
