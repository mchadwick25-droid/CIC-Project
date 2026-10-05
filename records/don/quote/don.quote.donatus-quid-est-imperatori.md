---
id: don.quote.donatus-quid-est-imperatori
world_id: donatism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    The quoted words are the Vassall-Phillips English translation, verbatim from the vendored Optatus, where
    Optatus puts them in Donatus's mouth. The Latin original stands in the Ziwsa critical edition, but the scan
    reads "qnid est imperatori cuni ecelesia?" at that line, so the Latin is not quoted here.
sources:
- source_id: don.source.optatus-against-donatists
  locus: "Book III, chapter 3 (The pride of Donatus); the Vassall-Phillips English translation, cic/texts/optatus_against-the-donatists.txt, line 1904"
  license: public-domain
- source_id: don.source.ziwsa-critical-edition-optatus
  locus: "Book III, the Latin original, whose scan is corrupted at this line (qnid est imperatori cuni ecelesia?); cic/texts/optatus_libri-vii-critical_ziwsa1893.txt, line 6557"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks whether this movement believed the state had any standing to decide who the true
    church was
  - conversation reaches the Principled-Refusal-vs-Pragmatic-Recourse tension and needs the founding quotation
    it is built on
  prefer_instead:
  - participant is asking about the Council of Cirta as an example of this movement's own rigor or resolve
    -- Cirta is a real complication in this movement's own early history, not a confirming example, and
    this quote should not be offered as if it resolved that different, harder question
relations:
- type: associated-with
  target: don.figure.donatus
- type: associated-with
  target: don.figure.optatus
- type: associated-with
  target: don.witness.refusal-and-recourse
- type: associated-with
  target: don.dw.the-emperor-and-the-church
text: "What has the Emperor to do with the Church?"
speaker_or_author: don.figure.donatus
license: verbatim
modern_lens_note: 'A modern reader may hear this as a general church-state-separation principle, the kind
  any modern secular democracy might affirm. Donatus''s own context is narrower and more pointed: he said
  it specifically to reject the emperor''s own claim to arbitrate which church was the true one, in the
  moment an imperial almoner arrived offering material aid -- and this same movement petitioned that identical
  emperor''s machinery for its own advantage at three other named points across its own history, a qualification
  this record does not smooth away.'
modern_rendering: What business does the emperor have with the church?
use_note:
  means: "Donatus, as reported by his opponent Optatus, denied the emperor any business in the church when imperial almoners came to Carthage."
  not_for:
    - "a claim that Donatus affirmed a general modern principle of church-state separation"
    - "a claim that the Donatists never sought imperial help or judgment; their three recourses sit in don.witness.refusal-and-recourse"
    - "a claim that these words survive in Donatus's own hand or in a Donatist text"
    - "a claim that the Council of Cirta shows Donatist rigor or resolve"
  years: {from: 346, to: 348}
  status: reviewed
---
Optatus addresses the passage to Parmenian directly ("when they came to Donatus, your father"). The retort therefore survives inside Optatus's polemic against Donatus's own successor, not in Donatus's hand. The modern rendering lightly modernizes the 1917 translation, which is already close to plain English.
