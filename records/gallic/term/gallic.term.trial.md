---
id: gallic.term.trial
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Cross-voice: the word and the one proof-text (Deuteronomy 13, "the Lord your God trieth you")
    are shared between Vincent and Cassian, but read of two different subjects - the Church's trial
    by an erring teacher (Vincent) and the individual will's trial (Cassian, Conf. XIII.14). The
    ecclesial application is Vincent's own. Sulpitius's "tried by that danger" (Letter I) is a third,
    ordinary use. Latin tentationis periculum is attested only in Gibson's editorial apparatus.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 10 [27-28] ("certain excellent persons, and of position in the Church, are often permitted by God to preach novel doctrines"; "the Lord, your God, trieth you"); ch. 17 [42] ("with the Church to receive Teachers, not with Teachers to desert the faith of the Church"); ch. 18 (Origen and Tertullian)'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'XIII.14 ("How God makes trial of the strength of man''s will"; Job "His well tried athlete")'
  license: public-domain
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter I ("Martin was indeed tried by that danger, but passed through it with true acceptance")'
  license: public-domain
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. XXIV title ("Martin is tempted by the Wiles of the Devil")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - why God lets great teachers fall into error
  - what Vincent says about Origen or Tertullian
  - how Deuteronomy 13 was read
  - whether Martin was "tested"
  - participant uses "trial," "test," "temptation," "why does God allow," "proving"
  - Comm. ch. 10 and ch. 17; Conf. XIII.14 on Job; Martin in the burning sacristy
  prefer_instead:
  - the participant means a court trial (the Priscillianist "trial" before Maximus - retrieve heretic / heresy and council / synod)
  - the question is about the athlete's combat as such (retrieve combat / athlete)
  - temptation by the devil in general (retrieve the devil / demons)
relations:
- type: associated-with
  target: gallic.term.illusion
- type: associated-with
  target: gallic.term.heretic-heresy
- type: associated-with
  target: gallic.term.doctor-expositor
- type: associated-with
  target: gallic.term.combat-athlete
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.free-will
- type: associated-with
  target: gallic.term.grace
- type: associated-with
  target: gallic.term.virtus
plain_meaning: >-
  God's proving of love - "the Lord your God trieth you, to know whether you love Him." A whole
  Church is tried by a learned teacher's novelty; a single will by a permitted assault.
world_word: trial (tentatio)
false_friend:
- a trial as an ordeal or misfortune only
- '"temptation" as enticement to sin'
- a court trial
- the erring teacher as a problem for the Church's credibility
senses:
  informational: >-
    Vincent asks the hard question about Origen and Tertullian: how is it "that certain excellent
    persons, and of position in the Church, are often permitted by God to preach novel doctrines to
    Catholics?" The answer is Moses's: even a teacher believed to teach by revelation may arise with
    signs, and yet "the Lord, your God, trieth you, to know whether you love Him with all your
    heart." The more learned the erring teacher, the greater the trial - "in order that all true
    Catholics may understand that it behoves them with the Church to receive Teachers, not with
    Teachers to desert the faith of the Church." Chaeremon reads the same verse of the single soul:
    God "makes trial of the strength of man's will," as with Job, "His well tried athlete," and
    does not always remove temptation but lets the will fight, helped. At Tours the word is spoken
    of a night in a burning sacristy: "Martin was indeed tried by that danger, but passed through it
    with true acceptance."
  evidential: >-
    Attested in Vincent (Comm. 10, 17, 18), Cassian (Conf. XIII.14), and Sulpitius (Letter I; Vita
    XXIV title). One proof-text, two ecologies; the ecclesial reading is Vincent's alone.
  personal: >-
    A great teacher's fall is not a scandal to be explained away but a test set for us. That is
    how Vincent can honour Origen and refuse him in one breath - and how a monk can be told that
    God let the assault come so that his love could be proved.
  translational: >-
    A modern hearer may take "trial" as misfortune, "temptation" as enticement, or a fallen teacher
    as an embarrassment to the Church. For us a trial is God proving love - through a learned man's
    novelty, a permitted assault, or a night of fire - and the right answer is to hold to the
    Church, fight with help, or return to the cross.
quick_meaning: >-
  God's proving of our love. A Church is tried by a great teacher's error; a monk's will by an
  assault God permits; Martin by fire. The greater the teacher or the danger, the greater the
  proof.
distortion_risk: medium
---
Built from Doc_06 entry 058 (`galliclex058_trial.md`, Tier 2, tags SC TC DR; Doc_03 7.6). The
one-proof-text-two-ecologies finding (Doc_05 section 6C mode 5) is carried in divergence_note.
canon_cells left empty: the term informs no canon question directly enough to claim one.

Related-Terms also names the rule, novelty vs. antiquity, free will, grace (of God), combat /
athlete, the devil / demons, virtus / power, and Catholic. The rule, novelty vs. antiquity, free
will, grace, combat / athlete, and virtus / power were batch 1 / not built when this record was
authored and were added as associated-with relations at the cross-batch reconciliation pass once all
81 term records existed; the devil / demons and Catholic are in-batch but not made relations here,
since the chunk's Ecological Function states no dependency on them.
