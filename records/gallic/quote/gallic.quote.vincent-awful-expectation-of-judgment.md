---
id: gallic.quote.vincent-awful-expectation-of-judgment
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Vincent's own text (Commonitory ch. 1 [2], read at its locus for this record) -
    his own stated occasion for writing, load-bearing for this world's Lérins-side instance of the
    judgment gravity.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 1 [2] (npnf211 div iii.ii, file lines 12086-12093): Vincent's own stated
    reasons for writing - the nearness of time, the approach of judgment, and the danger of new
    heresies"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why Vincent wrote the Commonitory at all"
  - "participant asks whether Lérins shared the same sense of urgency as Tours"
  prefer_instead:
  - "participant wants Vincent's own interpretive rule itself, rather than his stated occasion for writing it - retrieve the Commonitory's own rule material"
text: >-
  By the consideration of time,—for seeing that time seizes upon all
  things human, we also in turn ought to snatch from it something
  which may profit us to eternal life, especially since a certain awful
  expectation of the approach of the divine judgment importunately
  demands increased earnestness in religion, while the subtle
  craftiness of new heretics calls for no ordinary care and attention.
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  Vincent gives two reasons for writing, side by side, as if they were of a piece: the nearness of
  judgment, and the danger of new heretical teaching. For Vincent, urgency about the end and
  urgency about doctrinal error are not two separate concerns - they are the same concern.
modern_rendering: >-
  By considering time. Time takes hold of everything human. So we, in turn, should grab something
  from it - something that will help us reach eternal life. This matters even more for one reason:
  a certain fearful sense that God's judgment is coming presses us to take our faith more
  seriously. It matters for a second reason too: the sly cunning of new heretics calls for real
  care and attention.
relations:
- type: associated-with
  target: gallic.gravity.judgment-imminent-present
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"By the consideration of time"` returns line 12086; `grep -n "no ordinary care"` returns a hit at
line 12091 in the same paragraph (a second, unrelated occurrence of the phrase exists later in the
Conferences, at line 45607, not part of this quote). Read with `sed -n '12084,12093p'`, inside
`<div2 ... id="iii.ii">` (Commonitory, chapter 1, numbered section [2]). The quoted span is one
complete sentence, "By the consideration of time..." through "...no ordinary care and attention.",
ending at its own period.

Normalization: line breaks joined with single spaces; the source's own em dash after "time" is
preserved as written. No word was added, dropped, substituted, or reordered.