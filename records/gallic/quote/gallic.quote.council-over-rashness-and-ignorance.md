---
id: gallic.quote.council-over-rashness-and-ignorance
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented as Vincent's own rule in the Commonitory (ch. 3 [8]), part of his method for testing a
    disputed doctrine against conciliar authority.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 3 [8] (npnf211 div iii.iv, file lines 12218-12220): the rule for what to prefer when error appears even in antiquity"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Vincent decided which authority to trust when sources disagreed"
  - "participant asks why councils mattered to Vincent's method"
  prefer_instead:
  - "participant asks about a specific council's decrees - this record carries only Vincent's general rule"
text: >-
  Then it will be his care by all means, to prefer the decrees, if such
  there be, of an ancient General Council to the rashness and ignorance
  of a few.
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  This is one step in Vincent's own procedure for testing a claim: first check whether the whole
  Church agrees; if error appears even among ancient authorities, prefer a General Council's ruling
  over any individual's private judgment. The same instinct - trusting a gathered, collective judgment
  over a lone voice - sits uneasily beside this world's own suspicion of synods and bishops elsewhere
  in its story.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"rashness and ignorance"` returns one hit, line 12220, inside `<div2 title="Chapter III. What is to
be done if one or more dissent from the rest." ... id="iii.iv">`. The sentence runs lines 12218-12220:
"Then it will be his care by all means, to prefer the decrees, if such there be, of an ancient
General Council to the rashness and ignorance of a few."

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
