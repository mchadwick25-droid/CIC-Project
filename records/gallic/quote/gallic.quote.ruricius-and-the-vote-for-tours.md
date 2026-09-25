---
id: gallic.quote.ruricius-and-the-vote-for-tours
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted at the narrative level: Documented as Sulpitius's own text (Vita ch. IX, read at
    its locus for this record), a named author writing within Martin's lifetime or immediately after,
    of a public event in the city he describes. Sulpitius was not present, and his hostility to the
    objecting bishops is his own perspective, disclosed as such.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. IX (npnf211 div ii.ii.x, file lines 1058-1083): Ruricius's pretext, the posted crowd, the vote, and the bishops' resistance"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks how Martin became bishop, or how a monk who did not want the office was made to take it"
  - "participant uses 'election', 'trick', 'ambush', or asks why some bishops objected to Martin"
  prefer_instead:
  - "participant wants the psalm that answered the objectors - retrieve gallic.quote.the-psalm-that-answered-defensor instead, or alongside"
  - "participant wants the southern node's version of the same shape - retrieve gallic.quote.archebius-carried-off-to-panephysis alongside, not instead"
text: >-
  Martin was called upon to undertake the episcopate of the church at Tours; but when he could not
  easily be drawn forth from his monastery, a certain Ruricius, one of the citizens, pretending that
  his wife was ill, and casting himself down at his knees, prevailed on him to go forth. Multitudes of
  the citizens having previously been posted by the road on which he traveled, he is thus under a kind
  of guard escorted to the city. An incredible number of people not only from that town, but also from
  the neighboring cities, had, in a wonderful manner, assembled to give their votes. There was but one
  wish among all, there were the same prayers, and there was the same fixed opinion to the effect that
  Martin was most worthy of the episcopate, and that the church would be happy with such a priest. A few
  persons, however, and among these some of the bishops, who had been summoned to appoint a chief
  priest, were impiously offering resistance, asserting forsooth that Martin's person was contemptible,
  that he was unworthy of the episcopate, that he was a man despicable in countenance, that his clothing
  was mean, and his hair disgusting. This madness of theirs was ridiculed by the people of sounder
  judgment, inasmuch as such objectors only proclaimed the illustrious character of the man, while they
  sought to slander him.
speaker_or_author: gallic.figure.sulpitius
license: verbatim
modern_lens_note: >-
  A modern reader hears an episcopal election as a career move or a procedure. Sulpitius tells it as an
  ambush of kindness: a lie about a sick wife, a crowd posted along the road, "a kind of guard." And the
  charge the objecting bishops bring is the ascetic body itself - mean clothes, disgusting hair - which
  Sulpitius turns back on them: the objection proclaims the very holiness it means to deny.
relations:
- type: associated-with
  target: gallic.story.election-at-tours
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml.
`grep -n "was called upon to undertake the episcopate"` returns one hit, line 1059. The chapter div is
`<div3 title="Chapter IX. High Esteem in which Martin was held." ... id="ii.ii.x">` (line 1052). The
excerpt is one continuous paragraph, verbatim and unbroken, at lines 1058-1083, from "Martin was called
upon to undertake the episcopate" through "while they sought to slander him."; no material internal to
this span was omitted or elided. One editorial endnote (n. 21, on the Turones
and Tours) falls after "at Tours;" and is dropped as apparatus.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
No word was added, dropped, substituted, or reordered.

speaker_or_author is gallic.figure.sulpitius: this is Sulpitius's own narration in the Life of Martin.
