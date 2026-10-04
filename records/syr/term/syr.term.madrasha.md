---
id: syr.term.madrasha
world_id: syriac-edessa-nisibis
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: syr.source.ephrem-hymns-on-faith-pearl
  locus: the Pearl cycle (the genre performed)
  license: public-domain
- source_id: syr.source.ephrem-nisibene-hymns
  locus: passim (stanzas and refrains)
  license: public-domain
- source_id: syr.source.sozomen-historia-ecclesiastica
  locus: III.16 (the rival hymnody answered in kind)
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how this world's theology was taught or passed on
  - participant asks about Ephrem's hymns
  - sung versus written theology comes up, or Ephrem's answer to Bardaisan and Mani
  prefer_instead:
  - participant asks about Aphrahat's writings - his Demonstrations are prose (see tahwyata)
relations:
- type: associated-with
  target: syr.term.raza-shrara
- type: associated-with
  target: syr.term.memra
plain_meaning: 'The teaching hymn: a sung poem with stanzas and a refrain, made to be performed. Among
  us, doctrine was taught by singing it. The melody and the refrain carry the argument into the body,
  so the congregation learns the faith by keeping the tune.'
world_word: madrasha (pl. madrashe)
false_friend:
- hymn (a decorative worship song beside the real teaching)
- madrasa (the later Islamic school - an unrelated word-echo)
senses:
  informational: The stanzaic teaching hymn with refrain - Ephrem's dominant vehicle for theological argument,
    performed by choirs (including the daughters of the covenant), often acrostic, meant to be sung rather
    than read.
  evidential: 'The genre was not Ephrem''s invention: Bardaisan''s circle had already made sung, stanzaic
    verse the register of popular theology in Edessa, and the church historians record Ephrem deliberately
    answering those songs with his own. Genre-level continuity is attested; claims about matching a specific
    rival''s meter are not made.'
  personal: 'For someone who learns by heart and not by argument: this world taught its deepest convictions
    as songs you could keep - the refrain does the remembering for you.'
  translational: '''Hymn'' undersells it: the madrasha was itself the argument, not the decoration around
    one.'
quick_meaning: 'The madrasha is the teaching hymn: a sung poem with a refrain. Among us, doctrine
  was taught by singing it.'
distortion_risk: low
use_note:
  means: "The madrasha is the stanzaic teaching hymn with refrain, Ephrem's chief vehicle for theological argument, sung by choirs rather than read, in which doctrine was taught as song."
  not_for:
    - "a claim that the hymn was mere decoration beside the real teaching"
    - "a claim that Ephrem matched a specific rival's meter"
    - "a claim that madrasha means the later Islamic school"
  years: {from: 200, to: 373}
  status: reviewed
---
Re-derived from syrlex004 (Tier 1) and Doc_04 C1/C3. The
Bardaisan-first genre point is carried at genre level only, per the
legacy chunk's own Author Gravity note; the vendored attestation is
Sozomen III.16 (Harmonius's songs answered by Ephrem's), cited with
its 5th-century remove understood. Ephrem's personal leadership of the
women's choirs stays excluded (see syr.term.qyama).
