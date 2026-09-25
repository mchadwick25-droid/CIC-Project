---
id: cappadocian.quote.macrina-refuses-remarriage
world_id: cappadocian-trinitarian
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
  formation_confidence: Contested
  divergence_note: "Contested in the same way this world's own sibling records already carry it
    (cappadocian.story.macrina-refusal; cappadocian.figure.macrina): the reasoning quoted here is
    Gregory's own literary rendering of his sister's motive in indirect speech, not a transcript of
    her actual words, and how much of it is recoverable biographical memory versus his hagiographic
    shaping of her is itself argued among the scholars who study her (Doc_02 SS5 debate 2). The TEXT
    itself is verified-direct against the vendored file; what stays open is whose reasoning this
    really is."
sources:
- source_id: cappadocian.source.gregory-nyssa-life-of-macrina
  locus: "\"DEATH OF THE YOUNG MAN\" (Migne PG 46, coll. 964C-964D; gregory-nyssa_life-of-macrina_clarke1916.txt)"
  license: public-domain
text: >-
  But when the plan formed for her was shattered by the young man's death,
  she said her father's intention was equivalent to a marriage, and
  resolved to remain single henceforward, just as if the intention had
  become accomplished fact. And indeed her determination was more
  steadfast than could have been expected from her age. For when her
  parents brought proposals of marriage to her, as often happened owing to
  the number of suitors that came attracted by the fame of her beauty, she
  would say that it was absurd and unlawful not to be faithful to the
  marriage that had been arranged for her by her father, but to be
  compelled to consider another; since in the nature of things there was
  but one marriage, as there is one birth and one death. She persisted
  that the man who had been linked to her by her parents' arrangement was
  not dead, but that she considered him who lived to God, thanks to the
  hope of the resurrection, to be absent only, not dead; it was wrong not
  to keep faith with the bridegroom who was away.
speaker_or_author: "Gregory of Nyssa, narrating Macrina's own reasoning"
license: verbatim
modern_lens_note: >-
  A modern reader may hear "refused to remarry after her fiance died" as
  simple grief, or as old-fashioned spinsterhood, and miss that Gregory
  frames it as a theological argument rather than a sentimental one:
  because Macrina held her father's arrangement as already tantamount to a
  marriage, and because she trusted the resurrection meant her betrothed
  was merely away rather than gone, a later match would have counted, in
  her own reasoning, as unfaithfulness to a still-living husband - not
  loyalty to a memory, but a conclusion drawn from what she believed the
  resurrection itself meant.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks why Macrina never married, or what happened when her betrothed died"
  - "participant asks what reasoning or argument stands behind Macrina's refusal of remarriage, in
    the source's own words"
  prefer_instead:
  - "participant wants a direct first-person quotation from Macrina herself rather than her
    brother's narration of her reasoning"
relations:
- type: associated-with
  target: cappadocian.dw.macrina-and-its-cost
modern_rendering: >-
  When the young man died, the marriage her father had arranged for her was undone. But
  she said the arrangement itself counted as good as an actual marriage. So she resolved
  to stay single from then on, as if the marriage had really taken place. Her resolve held
  firmer than anyone would have expected from someone her age. Her parents kept bringing
  her fresh proposals -- her beauty attracted many suitors. Each time, she said it was
  absurd and unlawful not to keep faith with the marriage her father had arranged for her,
  yet be compelled to consider another. In the nature of things, she said, there is only
  one marriage, just as there is one birth and one death. She insisted that the man bound
  to her by her parents' arrangement was not dead. Because of the hope of the
  resurrection, she believed he was alive with God -- only away, not gone. So it would be
  wrong, she said, not to stay faithful to a husband who was merely absent.
---
Verified verbatim 2026-09-02 directly against the vendored
gregory-nyssa_life-of-macrina_clarke1916.txt, under its own section header
"DEATH OF THE YOUNG MAN" (line 126), the paragraph immediately following
at line 128 (found via `grep -n -i -E "betroth|marriage|espous|widow|marry"`
on that file). Two inline print-apparatus artifacts were stripped as
pagination/column locators, not wording: the Clarke edition's own
page-break marker "|25" (between "could" and "have been expected") and
the Migne column-locator "[964D]" (between "her" and "parents'
arrangement"); both are cited instead in this record's own locus field
(coll. 964C-964D). No wording was added, dropped, or reordered; the
sentence beginning "Now Macrina was not ignorant of her..." was left out
of the excerpt entirely rather than silently repaired, since the print
text carries a stray, unclosed quotation mark there that is plainly an
OCR/typesetting artifact of this edition, not a wording choice to
preserve or fix.

Chosen over the section's earlier "HER BETROTHAL" paragraph (964B-964C)
because that paragraph only sets up the arranged match itself, while this
one is where Gregory gives Macrina's own reasoning for refusing every
later proposal - the exact claim cappadocian.dw.macrina-and-its-cost
states in its own voice ("she declared the bond binding still, reasoning
that if the resurrection is real, he was not lost but only away"). This
quote is that dw's own paraphrase traced back to Gregory's actual
sentences, reinforcing F6-P with the primary text itself rather than a
second restatement of it.

Carried as Gregory's narration of her reasoning, not her direct speech:
the passage is indirect discourse ("she said," "she would say," "she
persisted") rather than words rendered in quotation marks, so
speaker_or_author names Gregory as narrator rather than crediting Macrina
with a first-person quotation the text does not actually give her - the
same mediation this world's cappadocian.figure.macrina and
cappadocian.story.macrina-refusal already carry openly rather than paper
over.

MODERN RENDERING AUTHORED (2026-09-02, matching this build's own standing
quote discipline: the spoken form is a modern-English translation, never
the archaic original; the original stays as the record's own text field,
shown at Level 3).
