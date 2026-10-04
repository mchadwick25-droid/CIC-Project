---
id: desert.quote.sarah-man-among-you
world_id: desert-monasticism
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
relations:
- type: associated-with
  target: desert.story.sarah-answer
- type: associated-with
  target: desert.gravity.elder-authority
use_note:
  means: "Budge's Syriac sayings collection preserves Mother Sarah telling her brethren that she is the man and they are the women."
  not_for:
    - "Quoting the fuller Greek form about being a woman by nature but not by thought, which this recension lacks"
    - "Reading man and woman here as modern gender-identity claims rather than this world's virtue categories"
    - "Dating the saying precisely, since nothing dates Sarah individually and the collection was compiled after 430"
  years: {from: 350, to: 430}
  status: provisional
---
Verified character for character against the vendored Budge at line
2429, §525.

The fuller form of the saying - "By nature I am a woman, but not by my
own thoughts. It is I who am the man here, and you who are the women" -
belongs to the Greek alphabetical collection (Sarah 4), whose only
English translations are in copyright and which this world therefore
cannot vendor - see desert.search.greek-alphabetical-pd-english. This
recension carries only the second sentence.

The loss is real and is not smoothed over. The dropped sentence is the
half that most clearly frames the saying as Sarah's own comment on her
sex, rather than only a rebuke to the brothers. Without it the line is
blunter and more ambiguous. That is what the Syriac says.

The modern_lens_note stands unchanged: "man" and "women" are this world's
gendered virtue-categories, not a claim about gender identity.

Paraphrase, not verbatim quotation - desert.source.apophthegmata-patrum
carries no vendored edition, and this build's own hard rule bars any
verbatim-quote claim against it. The wording restates the saying's
substance rather than reproducing a specific published translation's
own English, consistent with desert.figure.sarah's own identical
discipline for the same saying.

divergence_note carries both halves of desert.source.apophthegmata-patrum's own confidence pairing,
the "Widely Accepted" half and the unconditional Inferential-Thin bound, matching desert.figure.sarah's
own full statement of it.

`sources[].locus` compiles into `quotes.json` (`build_quotes_json()` emits `sources` verbatim), so it
is written as a plain description: it does not name a sibling record id, use build-process language,
or carry a licence-mechanics gloss.

The modern_rendering is a modern-English translation of the text field, not a summary; the original wording stays as the text field, shown at Level 3. This desert pass is quotes-only: the world's dw prose and limits already carry the plain register.
