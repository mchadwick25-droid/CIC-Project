---
id: gallic.term.theotocos
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Vincent's digression (Lerins) is read; Cassian's seven books On the Incarnation against
    Nestorius are attested by Gennadius and present in the vendored volume but unread by this build
    - a stated coverage limit, not filled from general knowledge. Christology is peripheral to
    this world's formation literature as read (Doc_05 section 9A.7).
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 12 [32] ("not Theotocos (the mother of God), but Christotocos (the mother of Christ)"); ch. 13 [35] ("In God there is one substance, but three Persons; in Christ two substances, but one Person"); ch. 15 [40] ("most truly and most blessedly - The mother of God ''Theotocos''")'
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: 'ch. LXII ("seven books against Nestorius, On the incarnation of the Lord")'
  license: public-domain
- source_id: gallic.source.cassian-de-incarnatione
  locus: 'present in the vendored volume (a chapter heading on the Virgin as Theotocos is locatable by grep) but unread by this build - coverage limit, stated'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - what these writers said about Mary as "Mother of God," about Nestorius, or about the two natures
  - participant uses "Theotokos," "Mother of God," "Nestorian," "two natures," "Christology"
  - Comm. chs. 12-16; Cassian's books against Nestorius
  do_not_retrieve_when:
  - the question is about the formation ecology's own concerns - Christology is peripheral to us as read
  - the participant wants the content of Cassian's De Incarnatione - unread by this build; state the limit
  - later Marian doctrine
relations:
- type: illustrates
  target: gallic.term.progress-vs-alteration
- type: associated-with
  target: gallic.term.council-synod
plain_meaning: >-
  Vincent's example against Nestorius. In Christ there are two substances but one Person, so Mary
  is truly "the mother of God." Ephesus had refused the new teaching three years before.
world_word: Theotocos
false_friend:
- the title as belonging to later Marian devotion
- the title as central to our own formation life
senses:
  informational: >-
    Nestorius "maintains that Saint Mary ought to be called, not Theotocos (the mother of God), but
    Christotocos (the mother of Christ)"; against him Vincent sets the Church's teaching: "In God
    there is one substance, but three Persons; in Christ two substances, but one Person," so the
    Blessed Virgin is "most truly and most blessedly - The mother of God." It is his chosen example
    of a novelty "under a definite name, at a definite place, at a definite time," condemned at
    Ephesus by bishops who "innovated nothing."
  evidential: >-
    Attested in Vincent (Comm. 12, 13, 15). Cassian wrote seven books against Nestorius at Leo the
    archdeacon's request - his last work - which this build has not read.
  personal: >-
    For us it is one dated proof-case of the antiquity-and-consent test succeeding, not a matter
    our formation writing otherwise dwells on.
  translational: >-
    Not a later Marian devotion, and not a centre of our own life: a doctrinal example Vincent
    uses to show his method working - a new name refused because it was new.
quick_meaning: >-
  Vincent's example against Nestorius: two substances in Christ, one Person, so Mary is truly the
  mother of God. A proof-case for his rule, not a centre of our own life.
distortion_risk: low
---
Built from Doc_06 entry 080 (`galliclex080_theotocos.md`, Tier 3, tags SC TC; Doc_03 7.14).
Kept thin at the Tier-3 floor. The De Incarnatione coverage limit (Registry row 12, unread) is
stated in divergence_note and cited as a source entry pointing at the record for the unread work,
not filled. canon_cells: F1-E because Vincent's account of Ephesus's bishops innovating nothing on
the two-substances-one-Person confession is this world's nearest material on how councils
related to Christ's divinity.

Relation typing: `illustrates` gallic.term.progress-vs-alteration (one of the "new names" that
passage has in view).

Related-Terms also names novelty vs. antiquity and the rule (batch 1 / not built) - relations
deferred, to be added once those term records exist. The chunk also names heretic / heresy,
Catholic, and the deposit (in-batch); not made relations, since no dependency is stated.
