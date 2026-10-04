---
id: gallic.term.doctor-expositor
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Weighted to Vincent (Lerins) - the technical usage is his; Cassian's "best masters of that work
    or science" is the ordinary sense. Latin tractatores is one of the few lemmas supplied against
    the ancient text by the translator.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 10 [28] ("a Doctor in the Church, who is believed by his disciples or auditors to teach by revelation"); ch. 22 [53] ("O Timothy! O Priest! O Expositor! O Doctor!"); ch. 28 [72-74] ("a private fancy of his own"; "be he a bishop, be he a Confessor, be he a martyr"; "doctors, who are now called Homilists, Expositors"; "a consentient council of doctors")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.2 ("the best masters of that work or science") - the ordinary sense'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - who counted as an authorized teacher
  - what "Doctor" or "Expositor" means in Vincent
  - whether a bishop's or martyr's opinion binds
  - participant uses "doctor of the Church," "theologian," "teacher," "expositor," "commentator"
  - Comm. ch. 22, ch. 28; "a private fancy of his own"
  prefer_instead:
  - the question is about "the Fathers" as received authority in general (retrieve the Fathers / elders)
  - the question is about the monastic master (retrieve disciple / master)
  - the later title "Doctor of the Church" as a formal honour
relations:
- type: associated-with
  target: gallic.term.the-deposit
- type: associated-with
  target: gallic.term.progress-vs-alteration
- type: associated-with
  target: gallic.term.trial
- type: associated-with
  target: gallic.term.heretic-heresy
- type: associated-with
  target: gallic.term.commonitory-peregrinus
- type: associated-with
  target: gallic.term.bloodless-martyrdom-confessor
- type: associated-with
  target: gallic.term.disciple-master
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
plain_meaning: >-
  Vincent's word for an authorized teacher in the Church. What binds is the consent of such
  teachers; one teacher's own view, "be he a bishop, be he a Confessor, be he a martyr," is "a
  private fancy."
world_word: Doctor / Expositor (Tractatores)
false_friend:
- '"Doctor of the Church" as a later formal honorific bestowed on a fixed list of named saints'
senses:
  informational: >-
    God placed in the Church "first Apostles," "secondly Prophets," "then doctors, who are now
    called Homilists, Expositors"; what "all, or the more part, have supported and confirmed
    manifestly, frequently, persistently, in one and the same sense, forming, as it were, a
    consentient council of doctors," is to be held without doubt. But "whatsoever a teacher holds,
    other than all, or contrary to all, be he holy and learned, be he a bishop, be he a Confessor,
    be he a martyr, let that be regarded as a private fancy of his own." The Doctor is addressed as
    the deposit's keeper - "O Timothy! O Priest! O Expositor! O Doctor!"
  evidential: >-
    Attested in Vincent (Comm. 10, 22, 28); Cassian's use (Conf. XVIII.2) is the ordinary
    "master of a craft."
  personal: >-
    Not office, not sanctity, not even martyrdom binds us - only consent among such teachers. A
    Doctor's very gifts make him a trial when he errs.
  translational: >-
    Not the later honorific "Doctor of the Church" given to a short list of saints, but any
    recognized teacher, whose authority lies wholly in agreeing with the rest.
quick_meaning: >-
  Vincent's name for a Church teacher. Their agreement binds; one teacher alone, even a bishop or
  martyr, has only "a private fancy of his own."
distortion_risk: low
use_note:
  means: "Doctor meant Vincent's authorized Church teacher, whose agreement binds, while one teacher alone, be he bishop or martyr, holds only a private fancy."
  not_for:
    - "Doctor of the Church as a later honorific for a fixed list of saints"
    - "the Fathers as received authority in general, which sits in gallic.term.the-fathers-elders"
    - "the monastic master, which sits in gallic.term.disciple-master"
    - "a remark about this record's own coverage, sources or scholarly attribution"
  years: {from: 434, to: 434}
  status: reviewed
---
Built from Doc_06 entry 077 (`galliclex077_doctor-expositor.md`, Tier 3, tags SC TC; Doc_03
7.7). Kept thin at the Tier-3 floor.

Related-Terms also names the Fathers / elders, the rule, disciple / master, bloodless martyrdom /
confessor, and novelty vs. antiquity - cross-batch at authoring time, added as relations (typed
associated-with) at the reconciliation pass once all 81 term records existed. The chunk also names
council / synod (in-batch); not made a relation, since no dependency is stated.
