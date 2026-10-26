---
id: lpc.quote.thanks-be-to-god
world_id: latin-pastoral-congregational-christianity
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F6-E
use_note:
  means: "The Acta gives Cyprian's whole answer to his death sentence as Deo gratias, thanks be to God."
  not_for:
    - "a claim that Pontius records this answer"
    - "a claim that the Acta is a court transcript"
    - "a claim that the words show relief or irony"
  years: {from: 258, to: 258}
  status: provisional
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: The text field is the Latin of Knopf and Krueger's edition (1929), which spells animadverti
    where Hartel and Gebhardt print animaduerti. modern_rendering is a translation of the Latin; the Acta
    has no English in this world's vendored texts.
sources:
- source_id: lpc.source.acta-proconsularia-sancti-cypriani
  locus: Acta Proconsularia 4.3; Latin at cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt,
    lines 4910-4911; the same text in cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt,
    lines 41577-41579, and cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt, lines 6624-6626
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how Cyprian answered his death sentence
  - participant asks what Cyprian's last recorded words at his trial were
  prefer_instead:
  - participant asks how the crowd answered the sentence -- lpc.quote.let-us-too-be-beheaded-with-him
    gives that
claim_guards:
- Only the Acta gives this answer; the speaker must not attribute it to Pontius.
- The Acta is an early compilation with an unnamed compiler, not a court transcript; the speaker must
  not call it one.
relations:
- type: associated-with
  target: lpc.story.the-death-of-cyprian
text: 'Thascium Cyprianum gladio animadverti placet. Cyprianus episcopus dixit: Deo gratias.'
speaker_or_author: The Acta Proconsularia of Cyprian
license: verbatim
modern_lens_note: A modern listener may hear 'Thanks be to God' as relief or irony. In the Acta it is
  Cyprian's whole answer to his death sentence, the words of the church's own prayer.
modern_rendering: It is decided that Thascius Cyprian be put to death by the sword. Bishop Cyprian said,
  “Thanks be to God.”
---
Acta Proconsularia of Cyprian, 4.3. Latin in Knopf and Krueger's edition at cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt, lines 4910-4911. The same text is in Hartel's edition at cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt, lines 41577-41579, and in Gebhardt's at cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt, lines 6624-6626; those two OCR files carry misreads and line numbers inside the passage. The words before the sentence, 'and having said this he read the decree from the tablet', are left out. Thascius is Cyprian's own first name. The English is a translation made for this record. The passage carries the story lpc.story.the-death-of-cyprian.
