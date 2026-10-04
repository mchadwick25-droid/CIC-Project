---
id: cappadocian.quote.basil-on-common-life
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    This record's own body documents correcting this passage's `text`
    against two plain OCR misreads in the vendored basil_ascetic-works-longer-shorter-rules_clarke1925.txt
    scan - "Tor just as" for "For just as", and a stray leading curly-quote mark before "To
    begin" - and dropping three inline footnote-marker artifacts as apparatus, not text.
    The gate's own edition-level apparatus (cic/texts/REGISTRY.yaml) strips the recurring,
    evidenced marker conventions this same edition uses elsewhere in this passage (the
    "?" and "®" footnote glyphs, the stray column-continuation letter), but the "Tor"/"For"
    difference is a genuine scan misread, not a marker - the vendored file itself reads
    "Tor", not what Basil wrote. No apparatus mechanism should correct a raw word-level OCR
    error; that stays a fact about the scan, not a fidelity defect in this record. Same
    treatment applies to don.quote.donatus-quid-est-imperatori and its OCR-damaged
    neighbors: verification_state is lowered from verified-direct to verified-via-authority to
    reflect that the corrected text rests on a human correction against the raw
    scan, not a direct character match to the vendored file as it actually reads.
sources:
- source_id: cappadocian.source.basil-asketikon-longer-shorter-rules
  locus: "The Longer Rules (Regulae Fusius Tractatae), Rule/Question VII, opening
    argument, pp. 163-164 (basil_ascetic-works-longer-shorter-rules_clarke1925.txt)"
  license: public-domain
text: >-
  I recognise that the life of a number lived in common is more useful in
  many ways. To begin with, none of us is self-sufficient even as regards
  bodily needs, but we need one another's help in getting necessaries. For
  just as the foot has certain powers but lacks others, and without the
  help of the other limbs neither finds its own strength sufficient for
  endurance nor has the support of what is lacking, so in the solitary
  life both what we have becomes useless and what we lack becomes
  unprocurable, since God the Creator ordained that we need one another,
  as it is written, in order that we may be linked with one another.
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  A modern reader hears "communal living" as a lifestyle preference -
  efficient, or cozy, or countercultural - one option among others. Basil
  is not offering a preference; this passage is his direct answer to a
  direct question (the Longer Rules are framed as question-and-answer)
  asking whether someone who has fled a corrupt setting should live alone
  or with like-minded brothers. His case is anthropological and
  theological before it is practical: no person is self-sufficient even
  for bodily needs, so a solitary life leaves both your own gifts unused
  and your own lack unmet. Mutual need is not a design flaw community
  patches over - he argues God built it in on purpose, "in order that we
  may be linked with one another." Reading this as an argument against
  hermits generally overstates it; reading it as an argument for why
  someone joining this world's brotherhoods was joining goods, needs, and
  strengths in common, not just a household, gets it right.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks why someone would join a brotherhood instead of just being a solitary ascetic on
    their own"
  - "participant asks why the brotherhood held goods and necessities in common rather than each member
    keeping their own"
relations:
- type: associated-with
  target: cappadocian.dw.becoming-one-of-us
modern_rendering: >-
  I've come to see that living together does more good, in more ways,
  than living alone. To start with, none of us is self-sufficient even
  for our basic needs - we need each other's help just to get by. Think
  of a foot: it has certain strengths but lacks others, and cut off from
  the rest of the body, it can neither hold up on its own nor get what
  it's missing. It's the same with the solitary life - what abilities you
  do have go to waste, and what you lack you simply cannot get. God our
  Creator built us to need one another, so that we would be bound
  together.
use_note:
  means: "Basil's Longer Rules argues that no one is self-sufficient, so living in community lets gifts and needs meet as God intended."
  not_for:
    - "a blanket condemnation of every hermit rather than an answer to one question about where an ascetic should live"
    - "an exact character match to the vendored scan, when the text corrects an OCR misreading"
    - "the ordered day of prayer and work, which sits in cappadocian.quote.basil-on-work-and-prayer"
  years: {from: 360, to: 379}
  status: provisional
---
Verified verbatim directly against the vendored
basil_ascetic-works-longer-shorter-rules_clarke1925.txt, Longer Rules,
Question VII ("That it is necessary, with a view to pleasing God, to
live with like-minded persons, and that solitude is difficult and
dangerous"), its opening paragraph, lines 13190-13208 (grep -n "I
recognise that the life of a number lived in common" and grep -n "order
that we may be linked with one another" both confirm the span). This is
a scanned/OCR'd edition: three superscript footnote-marker digits
("common 1", "unprocurable,?", "written,®") and one stray mid-line
marginal column-letter ("D" after "but") were dropped as apparatus, not
text; two plain OCR misreads were corrected against context and the rest
of the sentence's own grammar - "Tor just as" to "For just as", and a
stray leading curly-quote mark before "To begin" removed. No wording was
added, dropped, or reordered.

Chosen for F4-I specifically because cappadocian.dw.becoming-one-of-us
asserts that joining one of this world's brotherhoods meant, among other
things, "goods held in common" - this passage is Basil's own argument
for exactly that, in his own voice, from the same Asketikon the DW
record's adelphotes and askesis term citations already draw from. The
term record cappadocian.term.koinonia already paraphrases "the Longer
Rules' argument against the solitary life" without quoting it; this
record supplies the verbatim passage that paraphrase rests on.

The spoken form is spoken form is a modern-English translation, never the archaic original; the original stays as the record's own text field, shown at Level 3.
