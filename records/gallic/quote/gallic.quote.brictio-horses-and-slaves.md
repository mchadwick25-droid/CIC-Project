---
id: gallic.quote.brictio-horses-and-slaves
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted and Documented at its locus (Dialogues III.15). This is a non-miraculous, historically
    credible accusation against a named, living contemporary - the report's own weight for the story's
    documentary character, per the host record's own narrative-tier finding.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.15 (npnf211 div ii.iv.iii.xv, file lines 5299-5305): the previous day's reproof
    of Brictio for keeping horses and purchasing slaves, including barbarian boys and comely girls"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks what Martin actually reproved Brictio for"
  - "participant asks about slave-owning, property, or wealth inside a monastery-turned-clergy household"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.brictio-in-the-courtyard"
text: >-
  For he had been reproved by him on the previous day, because he who had possessed nothing before he
  entered the clerical office, having, in fact, been brought up in the monastery by Martin himself, was
  now keeping horses and purchasing slaves. For at that time, he was accused by many of not only having
  bought boys belonging to barbarous nations, but girls also of a comely appearance.
speaker_or_author: "Gallus, as Sulpitius Severus records his account in the Dialogues"
license: verbatim
modern_lens_note: >-
  The charge is stated plainly and without supernatural framing: a man raised owning nothing was now
  buying horses and slaves, including children bought from beyond the frontier. This is the one part of
  the whole episode that rests on no vision, no demon, no possession - an accusation any contemporary
  could have checked, which is exactly why the story records it as the reproof's real cause.
relations:
- type: associated-with
  target: gallic.story.brictio-in-the-courtyard
modern_rendering: PENDING_OPUS_RENDERING
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "For he
had been reproved"` returns line 5299; `grep -n "comely$"` returns line 5304, continuing "appearance." on
line 5305. Read with `sed -n '5299,5305p'`.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
