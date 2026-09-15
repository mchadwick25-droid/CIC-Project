---
id: gallic.quote.martin-on-the-christ-with-wounds
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- C-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own text (Vita ch. XXIV, read at its locus for this
    record). The event is a Tier-3-shaped wonder - the devil appearing as Christ in Martin's cell -
    told by an author who was not present and who says he had it "from the lips of Martin himself";
    Roberts's endnote 40 at the same locus records the editor's own doubt about the narrative. What
    this record carries as load-bearing is the formation ideal the words state (the Christ this world
    would own is the one who suffered), not the event; the words are Martin's as the tradition of
    Tours attributed them to him, never independently corroborated.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. XXIV (npnf211 div ii.ii.xxv, file lines 1809-1813): Martin's reply to the devil appearing as a purple-robed, crowned Christ"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks who Jesus was to this world, or what kind of Christ its people believed in"
  - "participant asks about visions of Christ, false visions, or how this world tested what it was shown"
  - "participant asks whether Christ was pictured as a king or as the crucified one"
  do_not_retrieve_when:
  - "participant is asking whether the devil's appearance 'really happened' - this record carries the words, not an assessment of the event"
text: >-
  The Lord Jesus did not predict that he would come clothed in purple,
  and with a glittering crown upon his head. I will not believe that
  Christ has come, unless he appears with that appearance and form in
  which he suffered, and openly displaying the marks of his wounds upon
  the cross.
speaker_or_author: gallic.figure.martin
license: verbatim
modern_lens_note: >-
  A modern reader may hear this as a test for telling a true vision from
  a false one - and it is that. But the test itself is the point: the
  only Christ Martin will own is the one who was crucified, still bearing
  the wounds. A Christ in an emperor's purple and a jewelled crown is, by
  that fact alone, not the Lord. For a man who had left Caesar's own
  service to become "the soldier of Christ," and who stood alone before
  the court at Treves when the bishops bowed, the image of Christ as a
  glittering king was exactly what he had walked away from. The sentence
  is not a doctrine of the two natures; it is a picture of whom this world
  was following.
modern_rendering: >-
  The Lord Jesus never said he would come back dressed in purple, with a
  glittering crown on his head. I will not believe Christ has come unless
  he comes looking the way he did when he suffered, and openly shows the
  marks of his wounds from the cross.
relations:
- type: associated-with
  target: gallic.dw.the-christ-who-bears-the-wounds
- type: associated-with
  target: gallic.dw.christ-in-the-beggar-and-the-guest
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between
B-7 and B-8) directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"marks of his wounds"` returns one hit, line 1813; `grep -n "I am
Christ"` returns hits at lines 1803 and 1807 (the devil's two
declarations) in the same chapter; `grep -n "replied as follows"` puts
Martin's reply opening at line 1809, and "from the lips of Martin
himself" at line 1818. The chapter div is `<div3 title="Chapter
XXIV. Martin is tempted by the Wiles of the Devil." ... id="ii.ii.xxv">`
(line 1769; printed heading "Chapter XXIV.", div id one Roman numeral
higher, the same id-vs-printed-number offset the cloak story's own record
notes for chs. II-III). The quoted span is Martin's reply, `sed -n
'1809,1813p'`, from "The Lord Jesus did not predict..." through "...the
marks of his wounds upon the cross." Sulpitius's own framing sentence
before it ("Then Martin, the Spirit revealing the truth to him, that he
might understand it was the devil, and not God, replied as follows:") and
his attestation after it ("my information regarding it was derived from
the lips of Martin himself; therefore let no one regard it as fabulous")
are left outside the `text` field because they are the narrator's, not
the speaker's; both are disclosed here because the second is the whole
basis for attributing the words to Martin at all. Roberts's endnote 40,
attached to that attestation ("few will have any doubts as to the real
character of the narrative"), is editorial and is not part of the quoted
prose.

Normalization: the source hard-wraps prose at fixed widths; line breaks
were joined with single spaces. The source wraps the speech in curly
double quotation marks; those are the edition's own punctuation marking
speech and are dropped, exactly as a quotation is lifted from a printed
page. No word was added, dropped, substituted, or reordered.

This passage was already carried, at Doc_06 verification, in
gallic.term.illusion (sources[].locus and the informational sense) and
gallic.gravity.interior-road (sources[].locus) - so it is not new material
reached for at this step, but already-built material given its own quote
record for the first time, re-verified at its own line rather than
inherited. It is the ground for gallic.dw.the-christ-who-bears-the-wounds'
first position and for gallic.dw.christ-in-the-beggar-and-the-guest's one
surviving private word; reciprocal associated-with declared on both.

speaker_or_author is gallic.figure.martin: the words are attributed to
Martin by Sulpitius, who claims Martin as his direct source for this
episode. The fleet's self-reference rule applies: these are a named
figure's own attributed words, cited as such, never converted to the
we-voice.
