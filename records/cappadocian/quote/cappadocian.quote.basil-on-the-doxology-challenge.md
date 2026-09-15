---
id: cappadocian.quote.basil-on-the-doxology-challenge
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: cappadocian.source.basil-on-the-holy-spirit
  locus: "On the Holy Spirit, ch. 1, sec. 3 (npnf208_basil-letters-select-works.xml)"
  license: public-domain
text: >-
  Lately when praying with the people, and using the full doxology to
  God the Father in both forms, at one time "with the Son together
  with the Holy Ghost," and at another "through the Son in the Holy
  Ghost," I was attacked by some of those present on the ground that I
  was introducing novel and at the same time mutually contradictory
  terms. You, however, chiefly with the view of benefiting them, or,
  if they are wholly incurable, for the security of such as may fall
  in with them, have expressed the opinion that some clear instruction
  ought to be published concerning the force underlying the syllables
  employed. I will therefore write as concisely as possible, in the
  endeavour to lay down some admitted principle for the discussion.
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  A modern reader might expect a treatise on the Holy Spirit to open
  with abstract argument or scripture exegesis. Basil opens instead
  with a concrete pastoral incident: mid-service, praying the doxology
  aloud, he used two different prepositional phrasings for giving God
  glory and was attacked on the spot for "introducing novel and...
  contradictory terms." The entire treatise exists because of that one
  liturgical challenge, written at Amphilochius's own urging that
  Basil answer it - not because Basil set out to settle an abstract
  question no one had raised.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what actually triggered Basil's treatise on the Holy Spirit"
  - "participant asks whether changing a word in a prayer was really enough to get a bishop accused of heresy"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: cappadocian.dw.confession-not-a-vote
modern_rendering: >-
  Not long ago, praying with the congregation, I used the full
  doxology to God the Father in both of its forms. At one point, "with
  the Son, together with the Holy Spirit." At another, "through the
  Son, in the Holy Spirit." Some of those present attacked me for it.
  They said I was introducing new and self-contradictory language.


  You, though, suggested something better - mainly to help them, or,
  if they can't be helped, to protect anyone who might be taken in by
  them. You suggested that some clear teaching ought to be put out,
  explaining what these words actually mean. So I will write as
  briefly as I can. I will try to lay down some starting points we can
  agree on for the discussion.
---
Verified verbatim 2026-09-02 directly against the vendored
npnf208_basil-letters-select-works.xml. Located via `grep -n 'div1'
cic/texts/npnf208_basil-letters-select-works.xml`, which surfaces the
treatise's own top-level boundary at line 8580 ("De Spiritu Sancto.",
id="vii"); then `grep -n 'div2' cic/texts/npnf208_basil-letters-select-works.xml
| awk -F: '$1>=8580 && $1<=9500'`, which surfaces the treatise's own
"Preface." (id="vii.i", lines 8582-8675 - the NPNF editor's third-person
historical introduction, not Basil's own words, so not usable as a
verbatim quote from Basil) followed immediately by "Chapter I" (id="vii.ii",
title "Prefatory remarks on the need of exact investigation of the most
minute portions of theology", lines 8677-8823). A direct read of
Chapter I in full located the passage at id="vii.ii-p15", Basil's own
sec. "3.", lines 8793-8822 (confirmed again via `grep -n 'Lately when
praying' cic/texts/npnf208_basil-letters-select-works.xml` -> line
8793), immediately following Basil's opening remarks to Amphilochius on
why small words matter and immediately before Chapter II's discussion
of the heretics' close observation of syllables.

Normalization disclosed: the leading paragraph numeral ("3.") was
dropped, matching this build's standing convention of quoting running
prose rather than section numbering (cf. spirit-numbered-with-father-and-son,
which drops its own "25."). The typesetter's double-spacing after
terminal punctuation ("terms.  You" / "employed.  I will") was
normalized to single spaces. The source's typographic curly quotation
marks ("with the Son...") were rendered as straight ASCII double
quotes, matching this build's own precedent in
cappadocian.quote.ousia-and-hypostasis. The <i> emphasis tags the
source places around the four prepositions (with / together with /
through / in) were dropped along with all other markup; no emphasis
was added in its place. One editorial endnote (n. 712, the translator's
own explanation of the underlying Greek prepositions mu/sun/dia/en)
interrupts the source's own text directly after "contradictory terms."
and before "You, however" - this is translator's apparatus, not
Basil's own sentence, and was excised at that clean sentence boundary.
No wording of Basil's own text was added, dropped, or reordered.

Non-overlap confirmed: this passage is drawn from Chapter I (id="vii.ii"),
which precedes by nine chapters the ch. 10 (id="vii.xi") passage quoted
in cappadocian.quote.spirit-numbered-with-father-and-son and by
twenty-six chapters the ch. 27 (id="vii.xxviii" region) passages quoted
in cappadocian.quote.we-look-to-the-east (sec. 66) and
cappadocian.quote.what-is-the-written-source (sec. 67). No sentence,
clause, or section number is shared with any of the three; this is the
treatise's own opening statement of occasion, not part of its later
argument from either scripture (ch. 10) or unwritten custom (ch. 27).

This passage backs cappadocian.dw.confession-not-a-vote directly and
narrows the association to a single specific claim within that dw: the
dw states that when Basil "changed one small word in a familiar prayer
... he was accused of going too far" - and this is Basil's own,
first-person account of exactly that accusation and exactly that
occasion, in his own opening words to Amphilochius, rather than a later
retelling. Where the dw's own cited story record and the already-quoted
ch. 27 material (we-look-to-the-east, what-is-the-written-source) carry
Basil's ANSWER to the charge (pointing to existing unwritten custom -
the water, the standing at prayer, the words already sung), this quote
supplies the missing other half: the charge itself, and the reason the
treatise was written down at all, at Amphilochius's urging, rather than
left as a spoken defense.

MODERN RENDERING AUTHORED (2026-09-02): the spoken form is a modern-English
translation, never the archaic original; the original stays as the
record's own text field, shown at Level 3.
