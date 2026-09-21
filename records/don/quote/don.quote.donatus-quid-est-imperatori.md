---
id: don.quote.donatus-quid-est-imperatori
world_id: donatism
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'The Latin clause quoted in `text` was re-located this session to `cic/texts/optatus_libri-vii-critical_ziwsa1893.txt`,
    line 6557 (the Ziwsa critical edition), NOT to the `optatus-against-donatists` locus originally cited
    -- that file''s line 1904 carries only the Vassall-Phillips English translation. The Ziwsa file''s own
    OCR is rough at this line (''qnid est imperatori cuni ecelesia?'' for ''quid est imperatori cum ecclesia?''),
    a known artifact of that scan rather than a textual variant; the Latin above is given in its standard,
    corrected orthography, not the raw OCR string.'
sources:
- source_id: don.source.optatus-against-donatists
  locus: Book III -- the Vassall-Phillips English translation; cic/texts/optatus_against-the-donatists.txt,
    line 1904
  license: public-domain
- source_id: don.source.ziwsa-critical-edition-optatus
  locus: 'Book III -- the Latin original, corrupted by OCR at this line (''qnid est imperatori cuni ecelesia?'');
    cic/texts/optatus_libri-vii-critical_ziwsa1893.txt, line 6557'
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
text: '"Quid est imperatori cum ecclesia?" ("What has the Emperor to do with the Church?")'
speaker_or_author: don.figure.donatus
license: verbatim
modern_lens_note: 'A modern reader may hear this as a general church-state-separation principle, the kind
  any modern secular democracy might affirm. Donatus''s own context is narrower and more pointed: he said
  it specifically to reject the emperor''s own claim to arbitrate which church was the true one, in the
  moment an imperial almoner arrived offering material aid -- and this same movement petitioned that identical
  emperor''s machinery for its own advantage at three other named points across its own history, a qualification
  this record does not smooth away.'
modern_rendering: What business does the emperor have with the church?
---
Named directly in the Permanent Prompt's own Approved Source paragraph ('The retort Donatus himself is remembered to have given the emperor's own claim on the church'). Independently re-located this session at Optatus, Against the Donatists, Book III (line 1904) -- Optatus addresses the passage to Parmenian directly ('when they came to Donatus, your father...'), so the retort survives inside Optatus's own polemic against Donatus's own successor, not in Donatus's own hand. modern_rendering lightly modernizes Vassall-Phillips's own 1917 published translation, already close to plain modern English.
