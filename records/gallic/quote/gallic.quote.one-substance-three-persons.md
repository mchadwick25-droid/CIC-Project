---
id: gallic.quote.one-substance-three-persons
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- C-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Vincent's own text (Commonitory ch. 13 [37], read at its locus for this record),
    and datable to 434 by the work's own internal dating. Documented as this world's confession,
    not as its preoccupation: Vincent gives the formula as his chosen proof-case for the rule of
    antiquity and consent - a novelty refused at Ephesus - and Christology is peripheral to this
    world's formation literature as read (gallic.term.theotocos). Cassian's own seven books against
    Nestorius are present in the vendored volume but unread by this build
    (gallic.source.cassian-de-incarnatione); nothing here is drawn from them.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 13 [37] (npnf211 div iii.xiv, file lines 13059-13060): the one-sentence summary Vincent gives 'to unfold this same doctrine more distinctly and explicitly again and again'"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether this world believed Jesus was God, or believed in the Trinity"
  - "participant asks what this world confessed about Christ's two natures, or about Nestorius and Ephesus"
  - "participant uses 'Trinity', 'two natures', 'one Person', 'Theotokos', 'Nestorian'"
  prefer_instead:
  - "participant wants the content of Cassian's books against Nestorius - unread by this build; state the limit"
  - "the question is about this world's own formation concerns, where Christology is peripheral"
text: >-
  In God there is one substance, but three Persons; in Christ two
  substances, but one Person.
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  A modern reader may hear this as a technical formula, the kind of thing
  argued at councils. Vincent means it as a plain statement of what the
  Church already believes, set down so a monk on an island can remember
  it - and his reason for giving it is not to argue Christology but to
  show his rule at work: a new teaching (that Mary bore the man Christ but
  not God) had been refused three years earlier by bishops who, he says,
  innovated nothing. "Substance" here is what a thing is; "Person" is who.
  One what and three whos in God; two whats and one who in Christ. The
  sentence just before it gives the two reasons: two substances, because
  the Word of God does not change into flesh; one Person, because two sons
  would make a Quaternity, not a Trinity.
modern_rendering: >-
  In God there is one substance but three Persons. In Christ there are two
  substances but one Person.
relations:
- type: associated-with
  target: gallic.dw.one-person-two-substances
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between
B-7 and B-8) directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"two substances, but one Person"` returns one hit, line 13060 ("in Christ
two substances, but one Person. In the Trinity, another and"); the quoted
sentence begins on the line before, `<p id="iii.xiv-p5">In God there is
one substance, but three Persons;` (line 13059). The chapter div id is
iii.xiv (printed as ch. 13; the same id-vs-printed offset the theotocos
term record's own loci already carry for chs. 12-15). The paragraph
immediately before, [36] (lines 13050-13054), read at the same time and
cited in
gallic.dw.one-person-two-substances but not quoted here: "One Person
indeed she believes in Him, but two substances; two substances but one
Person: Two substances, because the Word of God is not mutable, so as to
be convertible into flesh; one Person, lest by acknowledging two sons she
should seem to worship not a Trinity, but a Quaternity." - "she" being the
Catholic Church. The sentences after the quoted one (the alius/aliud
distinction, "In the Trinity, another and another Person, not another and
another substance...") carry Heurtley's parenthetical glosses and endnotes
469-470 inline and were left out to keep the excerpt one clean,
self-standing sentence.

Normalization: the source hard-wraps the sentence across two lines; joined
with a single space. The paragraph number "[37.]" and the sentence
introducing it ("But it will be well to unfold this same doctrine more
distinctly and explicitly again and again.", its own paragraph at line
13056) precede the quoted sentence and are left out as apparatus and
framing respectively. No word was added, dropped, substituted, or reordered.

This passage was already carried, at Doc_06 verification, in
gallic.term.theotocos (sources[].locus for ch. 13 [35] and the
informational sense); this record gives the [37] summary sentence its own
quote record, re-verified at its own line. Ground for
gallic.dw.one-person-two-substances' first position; reciprocal
associated-with declared there.
