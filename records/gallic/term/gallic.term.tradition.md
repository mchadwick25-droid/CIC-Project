---
id: gallic.term.tradition
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F2-T
- F4-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Three voices, both nodes, in three registers - doctrinal (Vincent), monastic (Cassian), cultic
    (Martin); among the safest shared vocabulary. An asymmetry of weight: one Tours episode against the
    south's systematic statement. The Latin traditio is not attested in the vendored translation.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 2 [4] ("by the Tradition of the Catholic Church"); ch. 6 [16] ("Let there be no innovation - nothing but what has been handed down"); ch. 22 [53] ("not of private adoption, but of public tradition")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes Preface ("according to their traditions"); II.3 ("a succession of fathers and their traditions")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'Conferences II.10 ("by their traditions"); II.13 ("the tradition of the Elders"); II.24 ("relied on his own judgment rather than on the traditions of the Elders")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'Conferences XVIII.7 (not "taught by their traditions")'
  license: public-domain
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'Life of St. Martin ch. XI ("no steady tradition respecting them had come down from antiquity"; "a mere superstition")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what "tradition" meant, or whether the monks valued tradition over Scripture
  - why Cassian would not invent a rule, or why Martin refused to venerate a tomb
  - participant uses "tradition," "handed down," "custom," "innovation," or "Scripture alone"
  - Pope Stephen's "no innovation," Vincent's second criterion, the "traditions of the Elders," or the unattested martyr
  do_not_retrieve_when:
  - the persons who hand down (retrieve the Fathers / elders)
  - the formulated test (retrieve the rule)
  - the value-axis itself (retrieve novelty vs. antiquity)
  - Tradition as a later confessional counter-term to Scripture
relations:
- type: associated-with
  target: gallic.term.example-imitation
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.customs-of-the-monasteries
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.disciple-master
- type: associated-with
  target: gallic.term.discretion
- type: associated-with
  target: gallic.term.eight-principal-faults
- type: associated-with
  target: gallic.term.catholic
- type: associated-with
  target: gallic.term.commonitory-peregrinus
- type: associated-with
  target: gallic.term.progress-vs-alteration
- type: associated-with
  target: gallic.term.sarabaite
- type: associated-with
  target: gallic.term.the-deposit
plain_meaning: >-
  For us tradition is what has been received from predecessors and must be passed on unchanged.
  Vincent's second criterion of truth after Scripture, "the Tradition of the Catholic Church." Pope
  Stephen's rule, "nothing but what has been handed down." Cassian's "traditions of the Elders" by
  which thoughts are judged. And the "steady tradition ... from antiquity" without which Martin will
  not honour a tomb.
world_word: tradition / "handed down"
false_friend:
- a rival authority to Scripture in a confessional debate
- custom and folkways
- conservatism
senses:
  informational: >-
    Vincent puts the word second and makes it decisive: Catholic truth is guarded "first, by the
    authority of the Divine Law, and then, by the Tradition of the Catholic Church" - the second needed
    because heretics quote Scripture too. What Timothy is to keep is "not of private adoption, but of
    public tradition; a matter brought to thee, not put forth by thee." Cassian's monks live by the
    same word in a smaller room: faults are treated "according to their traditions," the junior learns
    "what ought to be considered good or bad by their traditions," the monk who "relied on his own
    judgment rather than on the traditions of the Elders ... forsook the desert," and monasteries stand
    at all only "through a succession of fathers and their traditions." At Tours the word governs a
    cult: shown a tomb the crowd revered, Martin asks his elders for the martyr's name and date,
    because "no steady tradition respecting them had come down from antiquity," and rather than lend
    his authority "lest a mere superstition should obtain a firmer footing," he asks the dead man
    himself - who confesses he was a robber.
  evidential: >-
    Vincent (Commonitory chs. 2, 6, 22), Cassian (Institutes Preface, II.3; Conferences II.10, II.13,
    II.24, XVIII.7), Sulpitius (Life ch. XI). The Latin lemma is not attested in the vendored
    translation.
  personal: >-
    Tradition for us is not a body of doctrine but a handed-down way of judging - a thought, a fast, a
    garment, a grave. The same test Vincent applies to a doctrine and Cassian to a custom, Martin
    applies to a tomb: nothing is honoured that was not handed down. Our most authoritative writers all
    insist that they are inventing nothing.
  translational: >-
    'Tradition versus Scripture - which did you put first?' - the question is not ours: Vincent needed
    tradition second, after Scripture, only because heretics quote Scripture too; and "tradition" for
    us was tested by whether it could be traced - a doctrine to the Fathers, a custom to the Elders, a
    cult to antiquity - and passed on by a keeper who is "not an author."
quick_meaning: >-
  What was handed down and must be passed on unchanged. The ground on which a Pope's letter, a monk's
  fast and a bishop's refusal of a tomb are all judged.
distortion_risk: medium
---
Built from Doc_06 entry 027 (Tier 2; chunk galliclex027_tradition.md; Doc_03 3.4). Register emic.
Quotations verified at locus by the build's own Doc_06 pass; not re-read here. Canon cells F2-T and
F4-E: Vincent's two-way guard and the traced-to-antiquity test are this world's own material on
whether the Bible was the only authority and whether its practices were later inventions.

Related-Terms also names the deposit, Catholic and progress vs. alteration - cross-batch at
authoring time, added as relations (typed associated-with) at the reconciliation pass once all 81
term records existed.
