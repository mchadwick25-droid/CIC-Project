---
id: lpc.witness.communion-over-separation
world_id: latin-pastoral-congregational-christianity
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-T
use_note:
  means: "In 256 Cyprian's council said it would cast out no one for a different view, and Augustine called it wrong but never cast Cyprian out."
  not_for:
    - "a claim that the church never broke communion"
    - "a claim that any source states a link between the early separations and the rule, since that link is our own reading"
    - "a claim that Cyprian and Augustine reached the same ruling"
    - "a claim that Carthage and Rome stayed in communion through the 256 dispute"
  years: {from: 246, to: 430}
  status: reviewed
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: The 256 preface, the De Unitate formula, Augustine's argument, and the Felicissimus
    and Novatian separations are each read at source at the loci below. That the rule against separation
    was held because of those separations is Doc_07 SS2H's synthesis; the fields give both side by side
    and do not state that causal link as fact.
sources:
- source_id: lpc.source.cyprian-seventh-council-of-carthage
  locus: 'the 256 preface: "judging no man, nor rejecting any one from the right of communion, if he should
    think differently from us," and no one "a bishop of bishops" -- verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml,
    lines 56864-56878'
  license: public-domain
- source_id: lpc.source.cyprian-de-unitate
  locus: On the Unity of the Church, "The episcopate is one, each part of which is held by each one for
    the whole" -- verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines
    42286-42291
  license: public-domain
- source_id: lpc.source.cyprian-epistles
  locus: Epistle XXXVII, Felicissimus tried "to divide with the bishop a portion of the people" while
    Cyprian acted through substitutes in his absence -- verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml,
    lines 32236-32306
  license: public-domain
- source_id: lpc.source.cyprian-epistles
  locus: 'Epistle XXXIX, on the faction of Felicissimus: "Whosoever gathereth elsewhere, scattereth" --
    verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 32476-32483'
  license: public-domain
- source_id: lpc.source.cyprian-epistles
  locus: Epistle XLVIII, Novatus "appointed his attendant Felicissimus a deacon" -- verified directly
    against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 33214-33219
  license: public-domain
- source_id: lpc.source.cyprian-epistles
  locus: Epistle XLI, the Novatian party at Rome "has appointed a bishop for itself" against Cornelius
    -- verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 32654-32690
  license: public-domain
- source_id: lpc.source.augustine-on-baptism-against-the-donatists
  locus: Book V, Chapter 17, SS23, Augustine argues against Cyprian's ruling while Cyprian "remained"
    in the Church's entirety -- verified directly against cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml,
    lines 12993-12999
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how this world handles sharp disagreement among its own leaders
  - participant asks whether disagreeing with a church's own past ruling means leaving it
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: lpc.gravity.collegial-communion-preserved
positions:
- We can argue that a colleague's ruling was wrong, at length, and still keep him at our table. One of
  us said so when he opened the council that would settle the hardest question in the room. No bishop,
  he said, sets himself up as a bishop of bishops. None forces a colleague to obey, since each has his
  own proper right of judgment. He added that we judge no one, and reject no one from communion, for thinking
  differently from us. A century and a half later, another of us argued at book length that the ruling
  made that day was wrong. He never once suggested that the man who made it stood outside our communion.
  Disagreement with a colleague, in our own life, is not a reason to separate.
- Underneath the disagreement sits a belief our earlier bishop wrote down plainly. "The episcopate is
  one, each part of which is held by each one for the whole." We read that as the reason a bishop can
  differ from a colleague without breaking communion.
tensions:
- We do not hold this rule because we have never broken it. In our own first years, we watched what breaking
  it costs. A deacon's faction gathered apart in Carthage while our bishop was away in hiding. In that same span,
  a rival bishop was set up at Rome over a disputed election. Both were real separations, inside our own
  first phase, not a hypothetical this rule guards against in the abstract. We hold the rule that disagreement
  must not become separation knowing, from the inside, what separation actually does.
claim_guards:
- The record puts the deacon's faction in Carthage and the rival bishop in Rome; the speaker must not call the deacon a bishop or place the rival bishop in Carthage.
- The record does not say our rule against separation was held because of those two separations; the speaker must not state that link.
text: We can argue that a colleague's ruling was wrong, at length, and still keep him at our table. One
  of our bishops said so when he opened the council that would settle the hardest question in the room.
  No bishop, he said, sets himself up as a bishop of bishops. None forces a colleague to obey. Every bishop
  has his own proper right of judgment. At that same council, he said we judge no one, and reject no one
  from communion, for thinking differently from us. A century and a half later, another of our bishops
  argued at book length that the ruling made that day was wrong. He never once put the man who made it
  outside our communion. In our own first years, we had seen separation from the inside. A deacon's faction
  gathered apart in Carthage while our bishop was away in hiding. In those same years, a rival bishop was set up at Rome over a disputed election. We do not pretend those separations never happened. We hold our rule
  against separation knowing, from our own record, what it costs when it breaks.
---
Taken from Doc_07_Integrated_Ecology_Analysis.md §2H (Boundary Structures), read in full, including its own Forces integration paragraph naming the Felicissimus schism and the roughly contemporaneous Novatianist rival consecration at Rome as 'both boundary failures of exactly the kind G3 exists to prevent, and both inside Cyprian's own phase.' Doc_06_Full_Lexicon_Development.md's own note that De Unitate was written 'amid the Felicissimus and Novatianist crises' grounds this record's own source citation directly. relations[] carries one gravity edge (G3, lpc.gravity.collegial-communion-preserved).
