---
id: desert.quote.they-have-taken-away-my-god
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F6-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: "Contested for incident-level attribution, matching desert.story.sarapion-anthropomorphite's own basis: this is Cassian's own literary reconstruction of a scene he says he witnessed, composed in Latin for a Gallic audience decades after the event, not a transcript. The words themselves are quoted verbatim from the vendored text."
sources:
- source_id: desert.source.cassian-conferences
  locus: "Conference X (On the Method of Prayer), ch. III - Abbot Sarapion's own outcry on realizing, in the middle of communal prayer, that the bodily image of God he had always held before his mind was gone from his heart"
  license: public-domain
text: "Alas! wretched man that I am! they have taken away my God from me, and I have now none to lay hold of; and whom to worship and address I know not."
speaker_or_author: "Abbot Sarapion of Scete, as Cassian records him - a different named elder from the Abbot Serapion of Conference V (the eight-principal-faults teaching); the surviving text marks the two with different spellings"
license: verbatim
modern_rendering: >-
  Alas! I am a wretched man! They have taken my God away from me. Now I
  have no one to hold on to. I do not know whom to worship, or whom to
  address.
modern_lens_note: >-
  A modern reader may hear this as simple attachment to a comforting mental
  picture, easy to set aside once a truer idea arrives. Read in context, the
  loss is not sentimental: the picture Sarapion always held before his mind
  in prayer was, for him, how he reached God at all. Losing it felt like
  losing access to God himself, not like giving up a habit.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether correction from an outside authority ever cost someone something real"
  - "participant asks how a simple, deeply devoted person experienced being corrected by someone more educated"
  - "participant asks whether losing a comforting picture of God can feel like losing God"
relations:
- type: associated-with
  target: desert.story.sarapion-anthropomorphite
---
Verified verbatim against the vendored file
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, line
36051 ("Alas! wretched man that I am! they have taken away my God from
me, and I have now none to lay hold of; and whom to worship and address
I know not."), inside Conference X ch. III (file lines 36005-36058,
within the Conferences I-X division desert.source.cassian-conferences
registers at line 25863).

This is not the same Abbot Serapion whose teaching on the eight
principal faults desert.quote.eight-principal-faults already carries
(Conference V, file line 30091 onward). The vendored translation marks
the two with different spellings - "Serapion" for the Conference V
elder, "Sarapion" for this one - and its own editorial footnote at
Conference V ch. I (line 30105) raises, without resolving, a separate
identity question about a third possible Serapion (of Arsinöe, per
Rufinus and Palladius ch. LXXVI). This record does not conflate any of
the three.

This quote record supplies the verbatim line that
desert.story.sarapion-anthropomorphite's own `text` field paraphrases
rather than quotes directly, per the standing rule that a story record
embedding verbatim quotation must point at a real quote record instead.

The modern_rendering is a modern-English translation of the text
field, not a summary; the original wording stays as the text field,
shown at Level 3, matching this record set's register-bar convention
(desert.quote.sarah-man-among-you, desert.quote.eight-principal-faults):
short sentences, everyday words, translation fidelity kept.
