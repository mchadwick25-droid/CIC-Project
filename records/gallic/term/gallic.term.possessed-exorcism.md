---
id: gallic.term.possessed-exorcism
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Weighted to Sulpitius - the organizing sense is the north's (the bishop's ministry as exorcism
    and healing). The south's counter-teaching (Nesteros, Conf. XV.7: good monks do not profess
    themselves exorcists) is Egypt's and never addresses Martin; the two texts do not meet. The
    possessed are the ministry's object and never its subject (Article 20). Whether a given
    exorcism "really happened" is carried by virtus / power's Reported-Experience Status, not
    here. "Energumens" is Doc_03's gloss; no Latin lemma was supplied against the text.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. V ("appointed him to be an exorcist"); ch. XVII (Tetradius''s servant "laid hold of by a demon")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'III.2 ("he utters the formula of exorcism"); III.6 ("the possessed roaring through the whole church"; the man suspended in the air; "he touched no one with his hands, and reproached no one in words"); III.13-14 (cures "more slowly and with less grace")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'XV.7 ("professed themselves exorcists among men"; "nor should we ask whether the devils are subject to him"); XIV.7 (the layman "living in the world")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.15 ("the special grace of the Presbyter Isidore"; "possessed by a most fierce demon")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - how Martin cast out demons
  - what an exorcist was
  - whether Cassian's monks did exorcisms
  - why a good monk should not "profess himself an exorcist"
  - participant uses "exorcism," "exorcist," "possessed," "possession," "deliverance"
  - Martin's appointment by Hilary; the possessed hanging in the air; the formula over the oil; Nesteros on exorcists; the married layman's power
  prefer_instead:
  - the question is about the devil as such (retrieve the devil / demons)
  - the question is about the saint's power generally (retrieve virtus / power)
  - later rites of exorcism
  - whether a given exorcism "really happened" (virtus / power carries the Reported-Experience Status)
relations:
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.sign-of-the-cross
- type: associated-with
  target: gallic.term.humility
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.the-world-secular
- type: presupposes
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.grace-as-charism
- type: associated-with
  target: gallic.term.blessing
- type: associated-with
  target: gallic.term.heathen-rustics
- type: associated-with
  target: gallic.term.sackcloth-and-ashes
- type: associated-with
  target: gallic.term.catechumen
plain_meaning: >-
  The possessed are people "laid hold of by a demon." Exorcism was Martin's first church office
  and his daily ministry - done without touch or words, until the demon named itself.
world_word: the possessed / exorcism
false_friend:
- exorcism as a rite performed by a licensed priest under a later ritual
- possession as mental illness misdescribed
- the exorcist as a horror-film figure
senses:
  informational: >-
    Martin's first Church office was this one: Hilary, unable to bind him any other way, "appointed
    him to be an exorcist," an office with a kind of injury in it, and "Martin did not refuse." The
    possessed are the north's most visible congregation - "one could perceive the possessed roaring
    through the whole church" at his approach, a man "snatched up into the air" and hung there. His
    method, as Gallus tells it: "he touched no one with his hands, and reproached no one in words,"
    but sent everyone out, prayed on the ground in sackcloth and ashes, and questioned the demons,
    who confessed their crimes and "revealed their names, too, of their own accord." At Marseilles
    Nesteros teaches what not to be: "our predecessors never reckoned those as good monks or free
    from the fault of vainglory, who professed themselves exorcists among men"; a man is commended
    for the beauty of his life, "nor should we ask whether the devils are subject to him." A married
    layman casts out a demon by a word; the special grace of Presbyter Isidore could not free a
    brother whom his own envy had delivered up.
  evidential: >-
    Dominant at Tours (Vita V, XVII; Dial. III.2, III.6, III.13-14) and incidental, cautionary at
    Marseilles (Conf. XIV.7, XV.7, XVIII.15). The south's warning is Egyptian counter-teaching, not
    a reply to Tours. The possessed themselves never speak in any source.
  personal: >-
    At Tours our saint is known by the demons that flee him. At Marseilles our teachers would not
    have him praised for it. Both are ours, and we do not let either speak for the other.
  translational: >-
    A modern hearer pictures a licensed priest with a book, or a horror film, or a misdiagnosed
    illness. For us exorcism was a minor Church office Martin held before he was a priest, and the
    bishop's daily work with people who roared and hung in the air - and, in the south, the one fame
    a good monk must never claim.
quick_meaning: >-
  People "laid hold of by a demon," and the office of freeing them. Martin's first church office
  and his daily work, done in silence and sackcloth. In the south, a fame a good monk must not seek.
distortion_risk: medium
---
Built from Doc_06 entry 051 (`galliclex051_possessed-exorcism.md`, Tier 2, tags SC TC RT; Doc_03
6.5). The Article 20 note (the possessed are the ministry's object, never its subject) is
carried in divergence_note and senses.evidential.

Relation typing: `presupposes` gallic.term.the-devil-demons (no exorcism without the adversary).

Related-Terms also names virtus / power, sign of the cross, humility, bishop / the monk-bishop, and
the world / secular - cross-batch at authoring time, added as relations (typed associated-with) at
the reconciliation pass once all 81 term records existed.
