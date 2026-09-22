---
id: gallic.term.brethren
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
    Two voices, both nodes (Sulpitius at Tours, Cassian at Marseilles). Vincent's one use - "the
    holy brethren" of Comm. ch. 11 - names the faithful at large, a different referent, held apart.
    Latin fratres is corpus-supported only in Gibson's editorial prolegomena.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. X ("Many also of the brethren"; "the brethren of younger years"); ch. XXI ("Martin assembled the brethren")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'IV.5 ("in the council of the brethren"; "the body of the brethren, with whom Christ was not ashamed to be numbered"); IV.7 ("the congregation of the brethren")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'Preface II ("holy brothers Honoratus and Eucherius")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'X.1 ("holy brother Helladius")'
  license: public-domain
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 11 [29] ("greatly beloved by the holy brethren") - a different referent'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - what monks called each other; who "the brethren" are
  - why Cassian addresses bishops as "holy brothers"
  - participant uses "brother," "brethren," "the community," "fellow monks"
  - Vita X; Inst. IV.5; the dedications
  prefer_instead:
  - the question is about the monk as such (retrieve monk / solitary)
  - the participant means Vincent's "holy brethren" of Comm. ch. 11 - the faithful at large
relations:
- type: associated-with
  target: gallic.term.communion
- type: associated-with
  target: gallic.term.penance-satisfaction
- type: associated-with
  target: gallic.term.the-religious
- type: associated-with
  target: gallic.term.monk-solitary
- type: associated-with
  target: gallic.term.monastery-coenobium
- type: associated-with
  target: gallic.term.junior-novice
- type: associated-with
  target: gallic.term.elder-senior-abbot
- type: associated-with
  target: gallic.term.humility
- type: associated-with
  target: gallic.term.conference
- type: associated-with
  target: gallic.term.disciple-master
plain_meaning: >-
  The monks of a house or circle as one body, and the address between named friends - "holy
  brother Helladius."
world_word: brethren (fratres) / brother
gloss_forms:
- form: brethren
  kind: ordinary
false_friend: []
senses:
  informational: >-
    At Marmoutier "many also of the brethren" hollow caves, "the brethren of younger years" copy
    while the elders pray, and Martin "assembled the brethren." In Cassian's house the new monk is
    stripped "in the council of the brethren" and told to be "on a level with the poor, that is with
    the body of the brethren, with whom Christ was not ashamed to be numbered." The word runs up the
    letters: "holy brothers Honoratus and Eucherius," "holy brother Helladius."
  evidential: >-
    Attested at Tours (Vita X, XXI) and Marseilles (Inst. IV.5, IV.7; Conf. Prefaces). Vincent's
    "holy brethren" (Comm. 11) is the faithful at large - the same word, another body.
  personal: >-
    A specific bond - the body of our house, with whom Christ was not ashamed to be numbered - not
    a general churchy address.
  translational: >-
    Close to the modern "brothers" of a religious community; the one thing to keep in view is
    that Vincent's "holy brethren" means the faithful at large, and we do not treat the two bodies
    as one.
quick_meaning: >-
  The monks of a house as one body, and how named friends address each other. Not Vincent's
  "holy brethren," which means all the faithful.
distortion_risk: low
---
Built from Doc_06 entry 070 (`galliclex070_brethren.md`, Tier 3, tags SC RT; Doc_03 1.6). Kept
thin at the Tier-3 floor; the chunk's only Distortion Risk is "generic churchy address," which
the translational sense already answers, so false_friend is [].

Related-Terms also names monk / solitary, monastery / coenobium, junior / novice, elder / senior /
abbot, humility, and conference - cross-batch at authoring time, added as relations (typed
associated-with) at the reconciliation pass once all 81 term records existed.
