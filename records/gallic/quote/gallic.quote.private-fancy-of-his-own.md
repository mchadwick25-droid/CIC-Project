---
id: gallic.quote.private-fancy-of-his-own
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
    Documented as Vincent's own rule in the Commonitory (ch. 28 [71-72]), the climax of his argument
    on testing novel doctrine against consentient authority.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 28 [71-72] (npnf211 div iii.xxix, file lines 14271-14278): Vincent's rule for a teacher whose view stands against the consentient testimony of all"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Vincent exempted anyone - even a bishop or a martyr - from his rule of consent"
  - "participant asks how Vincent's method treats a single teacher's dissenting opinion"
  prefer_instead:
  - "participant asks about a specific dissenting teacher Vincent has in mind - this record carries only his general rule, not a named case"
text: >-
  But whatsoever a teacher holds, other than all, or contrary to all, be
  he holy and learned, be he a bishop, be he a Confessor, be he a
  martyr, let that be regarded as a private fancy of his own, and be
  separated from the authority of common, public, general persuasion,
  lest, after the sacrilegious custom of heretics and schismatics,
  rejecting the ancient truth of the universal Creed, we follow, at the
  utmost peril of our eternal salvation, the newly devised error of one
  man.
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  Vincent names the offices in an ascending order of prestige - holy and learned, bishop, Confessor,
  martyr - precisely to rule out every exemption in turn: no rank, however honored, buys a teacher's
  solitary opinion any authority against the consent of all. Read against this world's own uneasy
  relationship with bishops and synods elsewhere, the rule cuts both ways - it distrusts the lone
  voice exactly as much whether that voice sits on a see or not.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"be he a bishop"` returns one hit, line 14272, inside `<div2 title="Chapter XXVIII. In what Way, on
collating the consentient opinions of the Ancient Masters, the Novelties of Heretics may be detected
and condemned." ... id="iii.xxix">` (printed heading "Chapter XXVIII.", div id one higher, the same
offset noted elsewhere in this corpus's own records). The full sentence runs lines 14271-14278: "But
whatsoever a teacher holds, other than all, or contrary to all, be he holy and learned, be he a
bishop, be he a Confessor, be he a martyr, let that be regarded as a private fancy of his own, and be
separated from the authority of common, public, general persuasion, lest, after the sacrilegious
custom of heretics and schismatics, rejecting the ancient truth of the universal Creed, we follow, at
the utmost peril of our eternal salvation, the newly devised error of one man."

The host record's prior wording quoted this passage out of the source's own order ("a private fancy
of his own ... be he a bishop, be he a Confessor, be he a martyr"), reversing the two clauses. The
source's actual order is "be he a bishop, be he a Confessor, be he a martyr, let that be regarded as
a private fancy of his own" - the office-list comes first, "private fancy" second. This record
carries the sentence in its actual, verified order.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
