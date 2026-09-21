---
id: gallic.term.anathema
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
    Weighted to Vincent (Lerins), with one ironic northern use (Sulpitius: a bad priest who would
    have anathematized a virgin). The Greek anathema is the apostle's word in Heurtley's editorial
    brackets; not sought further.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 8 [22-23] ("Tremendous severity!"; "separated, segregated, excluded, lest the dire contagion of a single sheep"); ch. 9 [25] ("to anathematize those who preach anything other than what has once been received, always was a duty"); ch. 16 [41] ("Accursed then be Photinus")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'II.12 ("laid under an anathema")'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - what "anathema" means; how Vincent reads Galatians 1:8
  - whether excommunication was practised
  - participant uses "anathema," "accursed," "excommunicate," "cast out"
  - Comm. chs. 8-9, ch. 16's list; the priest who would have anathematized a virgin
  prefer_instead:
  - the question is about who is a heretic (retrieve heretic / heresy)
  - the withholding of fellowship as such (retrieve communion)
  - later canonical procedure
relations:
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.monk-bishop
- type: presupposes
  target: gallic.term.heretic-heresy
- type: associated-with
  target: gallic.term.catholic
- type: associated-with
  target: gallic.term.communion
- type: associated-with
  target: gallic.term.virgin-virginity
plain_meaning: >-
  Paul's "let him be accursed," as Vincent reads it - separated, excluded, lest one sick sheep
  infect the flock. A standing duty against any who preach other than what was received.
world_word: anathema ("let him be accursed")
false_friend:
- '"anathema" as a loose synonym for strong disapproval'
senses:
  informational: >-
    Vincent lingers on the apostle's "though we, or an angel from heaven": "Tremendous severity!"
    The word's force is exclusion - "let him be accursed, i.e., separated, segregated, excluded,
    lest the dire contagion of a single sheep contaminate the guiltless flock of Christ." And its
    permanence is the rule's: "to anathematize those who preach anything other than what has once
    been received, always was a duty, always is a duty, always will be a duty." At Tours the word
    appears once, in a bad priest's mouth, turned wrongly on a virgin who kept herself apart.
  evidential: >-
    Attested in Vincent (Comm. 8, 9, 16) and once in Sulpitius (Dial. II.12).
  personal: >-
    A formula of exclusion bound to the apostle's own severity, applied even to an apostle or an
    angel who preaches otherwise.
  translational: >-
    Not a word for strong disapproval, but a specific, permanent formula of exclusion - and, in its
    one northern use, a warning of the sanction turned wrongly.
quick_meaning: >-
  "Let him be accursed" - cut off, lest one sick sheep infect the flock. A permanent duty toward
  any who preach other than what was received.
distortion_risk: low
---
Built from Doc_06 entry 078 (`galliclex078_anathema.md`, Tier 3, tags SC TC; Doc_03 7.9). Kept
thin at the Tier-3 floor.

Relation typing: `presupposes` gallic.term.heretic-heresy (the sanction presupposes the
category it falls on).

Related-Terms also names the rule, novelty vs. antiquity, and bishop / the monk-bishop - cross-batch
at authoring time, added as relations (typed associated-with) at the reconciliation pass once all 81
term records existed. The chunk also names council / synod (in-batch); not made a relation, since no
dependency is stated.
