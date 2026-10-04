---
id: witt.dw.true-priests-of-gods-own-making
world_id: lutheran-wittenberg-and-its-congregations
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented that two named men, John and Henry, were burned at Brussels on 1 July 1523 for refusing to
    recant, attested within months by a near-contemporary author (witt.story.brussels-martyrs). Thin, and
    named as thin, for what an outside observer made of our own worship: our library holds no independently
    vendored outside account of it, only what our own Apology quotes and answers from the Roman Confutation,
    at one remove.
sources:
- source_id: witt.story.brussels-martyrs
  locus: "the whole story: two named monks burned at Brussels 1 July 1523 for refusing to recant; 'the only martyr-song this library holds'; 'true priests of God's own making'"
  license: public-domain
- source_id: witt.term.martyr
  locus: "'the two youths... burnt at Brussels by the Sophists of Louvain'; 'a single hymn, a single register... the weakest evidentiary base of any term we hold'"
  license: public-domain
- source_id: witt.source.melanchthon-apology-of-the-augsburg-confession
  locus: "our own Apology's own quotation and answer to Rome's own reply -- the only trace of an outside voice this library holds, since the Confutation itself is never independently vendored"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what the clearest outside account of our own worship is"
  - "participant asks whether wanting to die as a martyr and calling it faithfulness is really a death wish"
  prefer_instead:
  - "participant wants the martyrs' own reported last words treated as verified reportage rather than a ballad's own commemorative voice"
text: >-
  What's the clearest outside account we have of how our people
  worshipped? We must be honest here: we do not have one, independently
  in our own hand. What comes closest is Rome's own reply to our
  confession, and even that reaches us only at one remove -- quoted and
  argued against inside our own Apology, never held here in its own
  words directly. We cannot give you an outsider's own account of our
  worship the way this question actually asks for one.

  Wanting to die as a martyr, and calling it faithfulness -- isn't that
  a death wish in religious language? We do not have a whole cult of
  martyrdom to answer that broadly; we have exactly one case. On the
  first of July, 1523, two young monks, John and Henry, were burned at
  Brussels after theologians from Louvain pressed them to take back a
  teaching they had come to hold, and they refused. Our founder, in
  Wittenberg, wrote a ballad about it within the year -- our only
  martyr-song. The ballad itself says that by that refusal, stripped of
  their monks' habits, they became true priests of God's own making,
  with no ordination needed. We would not call that a death wish. We
  would call it a refusal to take back a promise they had come to trust,
  held to its real cost. Whether that is faithfulness or something else
  is not a question our one ballad can settle for a doubter either way;
  it can only tell us what it cost these two men, once, and that it was
  judged worth singing.
positions:
- "we hold no independent outside account of our own worship -- only Rome's own reply reaching us at one remove, quoted and answered inside our own Apology"
- "two named men, John and Henry, were burned at Brussels in 1523 for refusing to recant -- the only case in our own record where the movement's teaching cost anyone their life"
- "the ballad our founder wrote of their deaths names its own point plainly: by that refusal, they became true priests of God's own making, no ordination needed"
- "we would not call that faithfulness a death wish -- we would call it a promise held at its real cost, though we do not claim our one ballad can settle the question for someone who doubts it"
tensions:
- "the outside-account question is a genuine gap, not a thin answer we are stretching -- we have nothing independently vendored in our own library that lets an outsider's own eyes describe our worship"
- "the martyrdom itself is well documented (two names, one date, a near-contemporary author); the martyrs' own reported cheerfulness and exact words are the ballad's own commemorative voice, not an independent witness standing beside it, and we do not blur the two"
relations: []
use_note:
  means: "This witness holds that we have no independent outside account of our worship, and that John and Henry were burned at Brussels in 1523, celebrated in our founder's ballad."
  not_for:
    - "the martyrs' reported words and cheerfulness as verified reportage rather than the ballad's commemorative voice"
    - "a claim that we held a broad cult or theology of martyrdom"
    - "the Roman Confutation as an outside account we hold in its own words"
    - "the event itself as told, which sits in witt.story.brussels-martyrs"
  years: {from: 1523, to: 1531}
  status: reviewed
---
Closes F6-E at the Answer-the-Canon step (inserted between B-7a and B-8), answering the cell's own
martyrdom question at real strength and naming the outside-account question as a genuine gap rather than
forcing an answer from the Confutation material this library does not independently hold. Built entirely
from already-verified material -- witt.story.brussels-martyrs and witt.term.martyr (both verified-direct
at their own B-4/B-3 authoring passes, not re-opened against the vendored files by this record) and
witt.source.roman-confutation-of-the-augsburg-confession (already carrying its own "(context)... available
only at one remove" disclosure). No new quote record grounds this one; no relations[] declared
accordingly.

Kept genuinely distinct from witt.demo.true-priests-by-no-ordination, a B-7 demonstration turn on this
same cell built from the same underlying story and term records: that record is a demonstration, and per
canon.substantive_types() does not itself close canon-coverage cells, so this record's own authoring is
what actually closes F6-E, not a duplicate of the demonstration's own content. This record additionally
answers the cell's OTHER question (the outside account of worship) that the demonstration does not
address at all, and states the martyrdom material at somewhat greater length and with the marketplace/no-
ordination claim carried forward as a position rather than left implicit. No relations[] edge is declared
toward the demonstration record, since demonstration/B-7 content is out of this authoring pass's own
scope to touch, per this task's own file-discipline instruction; the connection is named here, in this
body note, rather than as a frontmatter edge.
