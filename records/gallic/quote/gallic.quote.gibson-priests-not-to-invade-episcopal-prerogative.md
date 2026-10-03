---
id: gallic.quote.gibson-priests-not-to-invade-episcopal-prerogative
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as editorial transmission history, not this world's own primary-source voice -
    the NPNF volume's own editorial prolegomena (read at its locus for this record), reporting
    Celestine's warning and reading it as an allusion to Cassian. The allusion itself is the
    editor's own inference, disclosed as such in the sentence.
sources:
- source_id: gallic.source.npnf-editorial-apparatus
  locus: "Gibson's Prolegomena (npnf211 div iv.i.i, file lines 15760-15766): the editor's own
    account of Celestine's warning and its possible target"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks what Celestine's letter actually warned against"
  - "participant wants the editor's own reasoning for reading the letter as aimed at Cassian"
  prefer_instead:
  - "participant wants Vincent's own quotation of a different Celestine letter and his own reading of it - retrieve gallic.quote.vincent-celestines-letter-and-its-reading"
text: >-
  Celestine speaks strongly of their negligence in not having
  suppressed what he regarded as a public scandal, and says that
  "priests ought not to teach so as to invade the episcopal
  prerogative," an expression in which we may well see an allusion to
  Cassian, the leading presbyter, of the diocese of Marseilles, whose
  Bishop is named first in the opening salutation;
speaker_or_author: "Edgar C. S. Gibson, editorial prolegomena"
license: verbatim
modern_lens_note: >-
  This is Gibson's own reasoning, not a fact the world's own text states - he reports what Celestine
  wrote, then offers his own inference ("we may well see an allusion to Cassian") that the warning
  was aimed at Cassian specifically. Both the report and the inference are the editor's own voice.
modern_rendering: >-
  Celestine speaks strongly about their negligence in failing to suppress what he saw as a public
  scandal. He says that "priests should not teach in a way that invades the special rights of
  bishops." We may well see this phrase as an indirect reference to Cassian. Cassian was the leading
  priest of the diocese of Marseilles, and its bishop is named first in the letter's opening
  greeting.
relations:
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
- type: associated-with
  target: gallic.gravity.monk-bishop
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"speaks strongly of their negligence"` returns line 15761; read with `sed -n '15758,15767p'`, inside
Gibson's own Prolegomena to the Conferences (div id iv.i.i). The quoted span is one complete clause,
"Celestine speaks strongly..." through "...opening salutation;", ending at the source's own
semicolon - the same sentence continues past this point ("and the letter concludes with some words
of eulogium on Augustine..."), not carried here; no terminal punctuation is invented where the
source has none.

Normalization: line breaks joined with single spaces; the source's own curly quotation marks around
Celestine's quoted clause are rendered here as straight double quotes, the same marks in a different
Unicode form. No word was added, dropped, substituted, or reordered.
