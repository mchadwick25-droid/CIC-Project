---
id: gallic.quote.private-fancy-be-he-a-bishop
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
    Documented as Vincent's own text (Commonitory ch. 28 [72], read at its locus for this record) -
    his own statement that even high office does not exempt a teacher's own opinion from being
    treated as a private fancy, if it stands against the consent of the fathers.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "ch. 28 [72] (npnf211 div iii.xxix, file lines 14268-14273): Vincent's own statement that
    rank does not exempt a teacher's opinion from being weighed against the fathers' own consent"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Vincent's own rule of antiquity applies even to a bishop or a martyr"
  - "participant wants Vincent's own most direct statement that office does not settle a doctrinal question"
  prefer_instead:
  - "participant wants Vincent's own summary formula instead - retrieve a Comm. ch. 2 [6] record where one exists"
text: >-
  But whatsoever a teacher holds, other than all, or contrary to all,
  be he holy and learned, be he a bishop, be he a Confessor, be he a
  martyr, let that be regarded as a private fancy of his own, and be
  separated from the authority of common, public, general persuasion
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  Vincent names the highest ranks a Christian teacher could hold - bishop, confessor, martyr - and
  says none of them settles the question. What matters is agreement with the consentient fathers,
  not the office or the sanctity of the one teaching. A martyr's own private opinion is still a
  private opinion.
modern_rendering: >-
  But suppose a teacher holds something that differs from what all hold, or goes against it. He may
  be holy and learned. He may be a bishop, a Confessor, or a martyr. Even so, let that be regarded
  as a private notion of his own. And let it be separated from the authority of common, public,
  general belief
relations:
- type: associated-with
  target: gallic.force.legitimacy-by-reception
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"But whatsoever a teacher holds"` returns line 14271; read with `sed -n '14260,14274p'`, inside
`<div2 title="Chapter XXVIII. In what Way, on collating the consentient opinions of the Ancient
Masters, the Novelties of Heretics may be detected and condemned." ... id="iii.xxix">` - the
Commonitory's own Chapter XXVIII, section [72]. The host record's own prior citation of "ch. 22
[53]" for this passage does not match this file's own division structure (`id="iii.xxix"`, div
title "Chapter XXVIII"); this record cites the locus the vendored file itself gives. The quoted span
is one complete clause, "But whatsoever a teacher holds..." through "...common, public, general
persuasion", closing at the clause's own natural boundary rather than continuing into the source's
own next clause ("lest, after the sacrilegious custom of heretics and schismatics..."), a separate
warning about heresy that does not bear on this clause's own point about rank and private opinion.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered; no terminal punctuation is added after "persuasion" - the source's own sentence continues
past this point with a comma, not a period, so this record's `text` field closes without inventing a
period the source does not have at this position.
