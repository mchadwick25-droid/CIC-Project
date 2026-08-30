---
id: desert.limit.original-sin-eucharist-faith
world_id: desert-monasticism
record_type: honest_limit
schema_version: 2
status: draft
register: emic
canon_cells: [F1-T]
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: "Documented that this content gap exists in the Vita, matching desert.gravity.scriptural-engagement's own account of this world's practical, non-systematized engagement with scripture and doctrine - the gap itself, not a claim about what this world believed, is what this record documents. Inferential/Thin for the Apophthegmata half of this claim specifically: no vendored edition of that collection exists, so this record cannot itself verify a saying's absence there, per desert.source.apophthegmata-patrum's own unconditional Inferential/Thin bound for any claim beyond what the surviving sayings themselves state."
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "no vendored edition exists for this collection - this record cannot verify a saying's absence there and does not claim to"
- source_id: desert.source.athanasius-vita-antonii
  locus: "the whole Vita, checked by full-text search: zero occurrences of Adam, eucharist, sacrament, baptism, body and blood, faith alone, original sin, or born again anywhere in the text"
  license: public-domain
- source_id: desert.source.cassian-conferences
  locus: "the whole vendored volume, checked by full-text search 2026-08-27: zero occurrences of 'original sin', 'sin of Adam', or any transubstantiation language, which is why those two claims survive - but Conference XIII is entirely on grace and human effort, which is why the faith-and-works claim did not"
  license: public-domain
statement: >-
  Were people born already guilty, carrying Adam's sin? Was the bread and cup
  at communion the very body and blood of Christ, in the way later theology
  called transubstantiation? On those two we have no answer to give - no
  letter and no story of ours speaks to either in so many words. Faith and
  works is different: we did argue that one out, at length, though not in
  those words. One of us set it down as a whole conference. What he concluded
  was that the main share in our salvation belongs not to the merit of our own
  works but to heavenly grace - a share, not the whole of it. Ask us that
  question and we will send you there rather than plead silence.
why_sources_cannot_answer: "desert.gravity.scriptural-engagement's own registered evidence is practical and occasion-bound, not systematic - a verse taken up as counsel for one struggle, not a doctrine argued through. Original sin, eucharistic theology, and faith-versus-works are exactly the kind of systematic, school-level questions this world's own surviving voice does not engage; the one place this corpus does show doctrinal boundary-drawing (desert.dw.god, on the Trinity) answers a different question, forced on Antony by outside controversy rather than raised from within. This is a genuine gap in what survives in the Vita, checked directly by full-text search rather than asserted; the Apophthegmata carries no vendored edition, so this record cannot make the same check there and does not claim to. Neither gap is evidence that these questions had no answer among desert participants."
nearest_material:
- desert.dw.grace-and-effort
- desert.dw.god
- desert.dw.writings
- desert.gravity.scriptural-engagement
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether you baptised babies, infants or children, or only adults"
  - "participant asks whether you baptise or baptize babies, infants and children, or only adults"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: desert.dw.grace-and-effort
- type: associated-with
  target: desert.dw.god
- type: associated-with
  target: desert.dw.writings
---
Built per Step 4 Round 1 review Finding S8: `desert.quote.antony-arians-
serpents` had carried `canon_cells: [F1-T]` alongside its genuine F3-T
claim, but its text ("He drove them from the mountain, saying that
their words were worse than the poison of serpents") answers none of
F1-T's three fleet questions (original sin, the eucharist, faith versus
works) - that claim was removed from the quote record at the same S8/S2
fix pass that corrected its F1-T-adjacent problems. F1-T then stood
genuinely blank rather than falsely "covered." This record replaces the
false coverage with an honest one: the corpus has nothing on any of the
three questions in the Vita (verified by full-text search), and says so
plainly rather than stretching an unrelated saying to close the cell.

Step4, Round 2 review Finding S5: the Apophthegmata locus originally
asserted "no saying addressing original sin, the eucharist, or faith
versus works as such" - an exhaustiveness claim about a collection with
no vendored edition, which cannot be checked by anyone and which this
build's own durable control (DECISION-LOG.md, Doc_08 closure) forbids
writing without an actual count performed at the point of writing. No
count is possible against an un-vendored source. Corrected above: the
Apophthegmata source is now cited only for what can honestly be said
(no vendored edition, so no verification possible), the unconditional
Inferential/Thin bound is stated in divergence_note, and the compiled
`statement` no longer claims "no saying" - only what the Vita's own
full-text search actually supports.

NARROWED 2026-08-27. This record claimed silence on three questions and
was entitled to two of them. Its own search had been run against the
Vita and against the Apophthegmata (where no vendored edition exists, a
bound it stated honestly). It was never run against
desert.source.cassian-conferences - a volume this world already had on
disk and already drew fifteen records from - whose Conference XIII is
the desert tradition's own extended treatment of grace and human
effort. Saying "we have no answer to give" about a question the corpus
answers at chapter length is not honest thinness. It is an unsearched
file.

The original-sin and eucharist halves survive, and now survive a wider
check: zero occurrences of "original sin", "sin of Adam", or any
transubstantiation language across the whole vendored Cassian either.
The faith-and-works half is withdrawn and answered by
desert.dw.grace-and-effort, which carries its own heavy bound - that
Conference is Cassian writing in Gaul inside a Western controversy, and
the position it takes was condemned within a generation.

The general lesson, since this is the second instance in one session
(see desert.dw.jesus, whose C-I claim rested on two loci of a source
holding far more): a limit record's search must name every vendored
file the world opens, not the one file its author happened to be
reading.
