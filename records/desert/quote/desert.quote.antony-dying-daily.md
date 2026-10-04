---
id: desert.quote.antony-dying-daily
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: "Contested for incident-level attribution, matching desert.story.antony-call's own basis for material from the same Vita: this is reported speech within Athanasius's own narrative, not an independently attested document in Antony's own hand. The words themselves are quoted verbatim from the vendored text."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS19 - from Antony's extended discourse to the gathered brothers"
  license: public-domain
text: "...let us hold fast our discipline, and let us not be careless... But to avoid being heedless, it is good to consider the word of the Apostle, \"I die daily .\" For if we too live as though dying daily, we shall not sin... For our life is naturally uncertain, and Providence allots it to us daily."
modern_rendering: >-
  Let us hold on to our discipline. Let us not grow careless. ... To avoid carelessness, it helps to
  remember the Apostle's words: "I die daily." If we too live each day as if we were dying, we will
  not sin. ... Our life is uncertain by nature. Providence gives it to us one day at a time.
speaker_or_author: desert.figure.antony
license: verbatim
modern_lens_note: "\"I die daily\" risks a modern misreading as describing depression, chronic suffering, or a wish for death - the phrase's most available modern register. The quote's own words guard against exactly that reading in the same breath (\"if we too live as though dying daily, we shall not sin\"): this names a daily readiness for mortality as fuel for discipline, not a description of despair."
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how anyone kept going day after day at something this hard"
  - "participant asks whether they thought about dying, and whether that thought helped or frightened"
  - "participant asks what kept the practice from going stale"
relations:
- type: associated-with
  target: desert.gravity.withdrawal
- type: associated-with
  target: desert.figure.antony
- type: associated-with
  target: desert.dw.judgment-and-resurrection
use_note:
  means: "In the Life of Antony, Athanasius has Antony urge the brothers to live as though dying daily, citing Paul, as a guard against carelessness and sin."
  not_for:
    - "\"dying daily\" as despair, depression, or a wish for death"
    - "the discourse as a transcript of Antony's own words rather than speech composed within Athanasius's narrative"
  years: {from: 356, to: 362}
  status: reviewed
---
Verified verbatim against the vendored file, from the
extended discourse (traditional SSSS16-43) Athanasius attributes to
Antony teaching the gathered brothers. The "Apostle" cited within the
quotation is Paul (1 Corinthians 15:31, per the vendored file's own
endnote); this record does not resolve that citation further, matching
this build's own practice of not over-annotating a quoted passage
beyond what the Representative would need.

The text field marks two internal elisions from SS19 with ellipses:
between "let us not be careless" and "to avoid being heedless" the
vendored text has "For in it the Lord is our fellow-worker, as it is
written, 'to all that choose the good, God worketh with them for
good'"; between "we shall not sin" and "our life is naturally uncertain"
it has "And the meaning of that saying is, that as we rise day by day
we should think that we shall not abide till evening; and again, when
about to lie down to sleep, we should think that we shall not rise up."
The excerpt's own opening also marks the vendored text's vocative
"Wherefore, children," with a leading ellipsis - the vendored sentence
is "Wherefore, children, let us hold fast our discipline..." - matching
the convention this record uses for its two internal elisions
(desert.quote.arsenius-flee-tace-quiesce).

The nested quotation around "I die daily" uses double quote marks,
matching the source's own mark and its own space before the closing
period ("daily .").
