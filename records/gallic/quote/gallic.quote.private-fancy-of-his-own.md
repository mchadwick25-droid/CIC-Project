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
    Documented as Vincent's own rule in the Commonitory (ch. 28 [72]), the climax of his argument
    on testing novel doctrine against consentient authority.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 28 [72] (npnf211 div iii.xxix, file lines 14271-14278): Vincent's rule for a teacher whose view stands against the consentient testimony of all"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Vincent exempted anyone - even a bishop or a martyr - from his rule of consent"
  - "participant asks how Vincent's method treats a single teacher's dissenting opinion"
  - "participant wants Vincent's own most direct statement that office does not settle a doctrinal question"
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
modern_rendering: >-
  But a teacher may hold something apart from all the rest, or against
  all the rest. He may be holy and learned. He may be a bishop, a
  Confessor, a martyr. Even so, whatever he holds this way must be
  counted as his own private notion. It must be set apart from the
  authority of the common, public, general belief. Otherwise, like
  heretics and schismatics in their sacrilegious custom, we would reject
  the ancient truth of the universal Creed. We would follow the newly
  invented error of one man, at the gravest risk to our eternal
  salvation.
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
- type: associated-with
  target: gallic.force.legitimacy-by-reception
use_note:
  means: "Vincent, in chapter 28 of the Commonitory, rules that a lone teacher's view against all, whatever his rank, is a private fancy, lest the Church follow one man's error."
  not_for:
    - "hostility to bishops as such, when the rule weighs every rank alike"
    - "Vincent's threefold test, which sits in gallic.quote.believed-everywhere-always-by-all"
  years: {from: 434, to: 434}
  status: reviewed
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
