---
id: gallic.term.communion
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    No Author Gravity - all three founding voices, both nodes: ecclesial fellowship with
    consequences in the saint's body at Tours; suspension from prayer at Marseilles; "the unity of
    communion and of the faith" at Lerins. The one thing this term cannot state from a Native text
    as read is the sacrament's frequency in Gaul: Gibson's footnote claiming daily communion in Gaul
    cites a chapter of the book his own edition omits entirely (Inst. VI.viii) - an editor's claim
    resting on an unread Latin text, carried as editorial and Inferential/Thin, not as our own
    statement. Latin communionis is attested only in Heurtley's editorial appendix.
sources:
- source_id: gallic.source.sulpitius-sacred-history
  locus: 'II.47 ("if any one should admit the condemned persons to communion")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'III.12 ("those bishops with whom Martin would not hold communion"); III.13 ("a diminution of his power on account of the evil of that communion"; "never again did he attend a synod")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'II.16 ("suspended from prayer"; "no one has any liberty of praying with him"; "delivered unto Satan"; "dares to hold communion with him in prayer"); III.2 (Saturday and Sunday "for the purpose of Holy Communion"); III.11 ("the Lord''s communion")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.15 ("receive the Holy Communion") - Gibson''s footnote there on daily communion in Gaul is editorial and cites an omitted book'
  license: public-domain
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 3 [7] ("the communion of the universal faith"); ch. 29 [77] ("the unity of communion and of the faith")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what "communion" meant, or whether it means the sacrament
  - why Martin's power was lessened by one communion
  - what it meant to be "suspended from prayer"
  - participant uses "communion," "eucharist," "fellowship," "excommunicate," "in communion with"
  - the Saragossa decree; the Ithacian bishops; Inst. II.16; Vincent's "unity of communion"
  do_not_retrieve_when:
  - the question is only about the eucharistic rite and its frequency - the Gallic evidence for that is an editor's footnote citing an omitted book
  - the question is about penance as such (retrieve penance / satisfaction)
relations:
- type: associated-with
  target: gallic.term.grace-as-charism
- type: associated-with
  target: gallic.term.catholic
- type: associated-with
  target: gallic.term.council-synod
- type: associated-with
  target: gallic.term.heretic-heresy
- type: associated-with
  target: gallic.term.penance-satisfaction
- type: associated-with
  target: gallic.term.brethren
- type: associated-with
  target: gallic.term.anathema
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.unceasing-prayer
- type: associated-with
  target: gallic.term.compunction
- type: associated-with
  target: gallic.term.monastery-coenobium
plain_meaning: >-
  Chiefly the bond of fellowship. To withhold it is the Church's sharpest sanction; to extend it
  wrongly defiles. Martin's one forced communion cost him power. A monk at fault loses his place
  at prayer.
world_word: communion (communio)
false_friend:
- '"communion" as the sacrament only - the eucharist, "taking communion"'
- a denominational body ("the Anglican Communion")
- excommunication as a legal penalty
senses:
  informational: >-
    At Tours communion is a thing one refuses, is forced into, and pays for. The synod at
    Saragossa decreed that whoever "should admit the condemned persons to communion" fell under the
    same sentence. At Trier the bishops "with whom Martin would not hold communion" went in terror
    to the king. To save lives Martin at last held communion with them for a moment - and
    afterwards, curing the possessed "more slowly and with less grace than usual," he confessed with
    tears "a diminution of his power on account of the evil of that communion." At Marseilles it is
    the right to pray with the brethren, and its loss is the house's sharpest sanction short of
    expulsion: "if one of them has been suspended from prayer for some fault ... no one has any
    liberty of praying with him before he performs his penance on the ground," for he is "delivered
    unto Satan." The Egyptians meet on Saturday and Sunday "for the purpose of Holy Communion." At
    Lerins the approved masters are those "remaining in the unity of communion and of the faith."
  evidential: >-
    Attested in all three founding voices: Sulpitius (Sacred History II.47; Dial. III.12-13),
    Cassian (Inst. II.16, III.2, III.11; Conf. XVIII.15), Vincent (Comm. 3, 29). What Gaul did
    about the sacrament's frequency, no Native text as read says; the editor's claim rests on an
    omitted book.
  personal: >-
    One communion could cost a saint his power and one fault a monk his place at prayer. The
    sacrament sits inside this bond; it is not the whole of it.
  translational: >-
    A modern hearer thinks first of the eucharistic rite, or of a denominational "communion," or of
    excommunication as a legal penalty. For us communion is fellowship with spiritual weight -
    refused to bishops who urged the sword, forced once and paid for in diminished power, lost by a
    fault and restored by penance on the ground.
quick_meaning: >-
  The bond of fellowship, with real weight. Withheld from bishops who urged the sword; forced
  once on Martin and paid for in lost power; lost by a monk at fault until he does penance. The
  sacrament sits inside it.
distortion_risk: high
---
Built from Doc_06 entry 061 (`galliclex061_communion.md`, Tier 2, tags SC DR TC RT; Doc_03
7.11). The chunk's name-the-layer note on Gibson's daily-communion footnote (citing the omitted
Inst. VI) is carried in divergence_note and senses.evidential, not smoothed. canon_cells: F3-P
because the Saragossa decree and the Ithacian communion are this world's own record of communion
used as a sanction among bishops.

Related-Terms also names bishop / the monk-bishop, virtus / power, unceasing prayer / the canonical
system, compunction, and monastery / coenobium - cross-batch at authoring time, added as relations
(typed associated-with) at the reconciliation pass once all 81 term records existed.
