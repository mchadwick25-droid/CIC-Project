---
id: gallic.term.angels
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
    Weighted to Sulpitius (Tours) - angels are Martin's visitors and messengers; at Marseilles the
    angel chiefly spoken of is the devil's counterfeit, plus the two angels of the Shepherd. The
    historicity of the northern visitations is carried by virtus / power's Reported-Experience
    Status, not here.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. XIV ("two angels, with spears and shields after the manner of heavenly warriors"); ch. XXI ("spoke in turns with him in set speech")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'II.13 (the synod at Nemausus; "Agnes, Thecla, and Mary were there with me"); III.13 ("an angel stood by him")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'II.5 ("an angel of Satan as an angel of light")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'XIII.12 ("the book termed the Pastor," two angels)'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - whether Martin saw angels; who visited him in his cell
  - whether Cassian's monks expected angelic visions
  - participant uses "angel," "vision," "apparition," "saints appearing"
  - the two warriors at the temple; the angel at Nemausus; Agnes and Thecla; the angel after the Ithacian communion
  do_not_retrieve_when:
  - the question is about the devil's counterfeit angel (retrieve illusion, the devil / demons)
  - the angel who sang the twelve psalms (retrieve unceasing prayer / the canonical system)
  - angelology as doctrine - not our subject
relations:
- type: associated-with
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.illusion
- type: associated-with
  target: gallic.term.council-synod
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.cell
- type: associated-with
  target: gallic.term.unceasing-prayer
- type: associated-with
  target: gallic.term.compunction
- type: associated-with
  target: gallic.term.sign-of-the-cross
plain_meaning: >-
  At Tours, Martin's visitors - seen "very often," speaking with him "in set speech," clearing a
  temple, reporting a synod. At Marseilles, chiefly the devil's counterfeit angel of light.
world_word: angels (as visitors and messengers)
false_friend:
- angelic visitation as generic pious legend
- a symmetrical convention shared by both nodes
senses:
  informational: >-
    "It is also well known that angels were very often seen by him, so that they spoke in turns
    with him in set speech." Two angels "with spears and shields after the manner of heavenly
    warriors" clear a temple; one tells Martin at sea what a synod at Nemausus decided; Agnes,
    Thecla, and Mary are in his cell; after the coerced communion an angel says, "Justly, O Martin,
    do you feel compunction ... Renew your virtue." At Marseilles our fathers speak of the two
    angels of the Shepherd, and of the angel of Satan Heron obeyed into the well.
  evidential: >-
    Dominant at Tours (Vita XIV, XXI; Dial. II.13, III.13); at Marseilles only Conf. II.5 and
    XIII.12. Whether the visitations happened is not what this record asserts.
  personal: >-
    At Tours the angels are part of what the disciple sees, and part of what Brictio sneers at. At
    Marseilles the same category is the shape of a counterfeit the monk must learn to tell from the
    true.
  translational: >-
    Not generic legend, and not a shared convention: at Tours angelic visits are reported in the
    register of eyewitness testimony, alongside Martin's power; at Marseilles the angel most spoken
    of is the devil's disguise.
quick_meaning: >-
  At Tours, Martin's visitors - warriors at a temple, a messenger at sea, Agnes and Thecla in his
  cell. At Marseilles, mostly the devil's false angel of light.
distortion_risk: medium
---
Built from Doc_06 entry 075 (`galliclex075_angels.md`, Tier 3, tags SC DR RT; Doc_03 6.6). Kept
thin at the Tier-3 floor; the DR tag carried as distortion_risk: medium with the chunk's own two
hearings as false_friend. The Round-1 C3 fix (the angel's full sentence after the Ithacian
communion) is honoured by quoting it as the chunk now has it.

Related-Terms also names virtus / power, cell, unceasing prayer / the canonical system, and
compunction - cross-batch at authoring time, added as relations (typed associated-with) at the
reconciliation pass once all 81 term records existed. The chunk also names sackcloth and ashes and
communion (in-batch); not made relations, since no dependency is stated.
