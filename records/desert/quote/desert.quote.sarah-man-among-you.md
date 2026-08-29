---
id: desert.quote.sarah-man-among-you
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'The saying is secure in this recension. What is NOT secure is the fuller Greek form:
    the clause about being a woman by nature but not by thought is absent here, and no public-domain English
    of the Greek exists to check it against. Anything resting on that clause stays unquotable.'
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: §525 (cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt line 2429) - Budge's Syriac recension
    of 'Anan-Isho', whose numbering and wording differ from the Greek alphabetical collection
  license: public-domain
text: Mother Sarah used to say to her brethren, “It is I who am a man, and ye who are women.”
modern_rendering: >-
  Mother Sarah used to say to her brothers: 'It is I who am the man, and you
  who are the women.'
speaker_or_author: desert.figure.sarah
license: verbatim
modern_lens_note: '"Man" and "women" operate here as this world''s own gendered virtue-categories (courage
  and steadfastness coded "man," weakness coded "woman"), not a claim about gender identity in the modern
  sense. Stated plainly as a vocabulary point; this field does not soften or reframe what Sarah''s own
  words claim.'
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how men in this world spoke to and about a woman"
  - "participant asks whether a woman was ever tested or challenged, and how she answered"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: desert.story.sarah-answer
- type: associated-with
  target: desert.gravity.elder-authority
---
VERBATIM AS OF 2026-08-27, AND SHORTER THAN THE PARAPHRASE IT REPLACES.
Verified character for character against the newly vendored Budge at line
2429, §525.

WHAT CHANGED, AND IT IS NOT A FORMALITY. The paraphrase this record
carried read: "By nature I am a woman, but not by my own thoughts. It is
I who am the man here, and you who are the women." THE FIRST SENTENCE IS
NOT IN THIS RECENSION. It belongs to the Greek alphabetical collection
(Sarah 4), whose only English translations are in copyright and which
this world therefore cannot vendor - see
desert.search.greek-alphabetical-pd-english. The paraphrase had been
carrying a Greek-tradition clause under a licence that could not be
checked against anything.

THE LOSS IS REAL AND IS NOT SMOOTHED. The dropped sentence is the half
that most clearly frames the saying as Sarah's own comment on her sex,
rather than only a rebuke to the brothers. Without it the line is blunter
and more ambiguous. That is what the Syriac says. A world that kept the
fuller wording because it preferred it would be choosing its evidence.

The modern_lens_note stands unchanged: "man" and "women" are this world's
gendered virtue-categories, not a claim about gender identity.

Paraphrase, not verbatim quotation - desert.source.apophthegmata-patrum
carries no vendored edition, and this build's own hard rule bars any
verbatim-quote claim against it. The wording restates the saying's
substance rather than reproducing a specific published translation's
own English, consistent with desert.figure.sarah's own identical
discipline for the same saying.

Step4, Round 1 review Finding S10: divergence_note carried only the
"Widely Accepted" half of desert.source.apophthegmata-patrum's own
confidence pairing - the unconditional Inferential/Thin bound added
above, matching desert.figure.sarah's own full statement of it.

Step4, Round 2 review Finding M8: `sources[].locus` compiles into
`quotes.json` (`build_quotes_json()` emits `sources` verbatim), which
this build's own field map for the record type had not previously
flagged - the locus above previously named two sibling record ids and
described itself in build-process terms ("in this record's own words
rather than a verbatim rendering"); reworded to a plain description
carrying the same information without either.

Step4, Round 3 review Finding M6: the M8 fix still left "vendored" and
a licence-mechanics gloss in this compiled field - reworded above to
plain description with neither.

MODERN RENDERING AUTHORED (2026-08-29, desert register pass; Mark's standing quote ruling: spoken form is a modern-English translation, not a summary - original wording stays as text, shown at Level 3). The desert pass is quotes-only: the world's dw prose and limits already carry the plain register.
