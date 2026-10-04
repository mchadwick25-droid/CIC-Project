---
id: gallic.quote.humility-mistress-of-virtues-not-exorcism
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
  formation_confidence: Widely Accepted
  divergence_note: >-
    Documented as Cassian's own text (Conference XV.7, read at its locus for this record); Widely
    Accepted as Cassian's report of Abbot Nesteros's teaching, the same caveat this world's other
    Cassian-reported-teaching records carry (its doctrinal content is not independently
    corroborated outside Cassian's own corpus).
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conference XV.7 (npnf211 div iv.v.vi.vii, file lines 39875-39904): Nesteros's teaching
    that humility, not miracle-working, is the mistress of the virtues, and his judgment against
    self-professed exorcists"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why this world's southern house distrusted miracle-working monks"
  - "participant asks what counted as real spiritual achievement at Marseilles"
  prefer_instead:
  - "participant wants Cassian's own stated refusal to narrate miracles at all - retrieve gallic.quote.cassian-refuses-to-weave-a-tale-of-miracles"
text: >-
  Humility therefore is the mistress of all virtues, it is the surest
  foundation of the heavenly building, it is the special and splendid
  gift of the Saviour. For he can perform all the miracles which Christ
  wrought, without danger of being puffed up, who follows the gentle
  Lord not in the grandeur of His miracles, but in the virtues of
  patience and humility. But he who aims at commanding unclean spirits,
  or bestowing gifts of healing, or showing some wonderful miracle to
  the people, even though when he is showing off he invokes the name of
  Christ, yet he is far from Christ, because in his pride of heart he
  does not follow his humble Teacher. For when He was returning to the
  Father, He prepared, so to speak, His will and left this to His
  disciples: "A new commandment," said He, "give I unto you that ye
  love one another; as I have loved you, so do ye also love one
  another:" and at once He subjoined: "By this shall all men know that
  ye are My disciples, if ye have love to one another." He says not:
  "if ye do signs and miracles in the same way," but "if ye have love
  to one another;" and this it is certain that none but the meek and
  humble can keep. Wherefore our predecessors never reckoned those as
  good monks or free from the fault of vainglory, who professed
  themselves exorcists among men, and proclaimed with boastful
  ostentation among admiring crowds the grace which they had either
  obtained or which they claimed.
speaker_or_author: "Abbot Nesteros, as Cassian records him (Conference XV.7)"
license: verbatim
modern_lens_note: >-
  Nesteros does not deny that a humble monk could work every miracle Christ worked - he grants it
  directly. What he denies is that miracle-working is the sign of a good monk at all; that sign is
  humility and love, quoting Christ's own words to that effect. Self-declared exorcism before a
  crowd is, on this teaching, evidence against a monk, not for one.
modern_rendering: >-
  So humility is the mistress of all virtues. It is the surest foundation of the heavenly
  building. It is the special and splendid gift of the Saviour. For the one who can perform all
  the miracles Christ worked, without danger of being puffed up, is the one who follows the
  gentle Lord. He follows Him not in the grandeur of His miracles, but in the virtues of patience
  and humility. But someone may aim to command unclean spirits, or to give gifts of healing, or
  to show the people some wonderful miracle. Even if he calls on the name of Christ while he is
  showing off, he is far from Christ. For in his pride of heart he does not follow his humble
  Teacher. For when Christ was returning to the Father, He drew up His will, so to speak, and
  left this to His disciples. "A new commandment I give you," He said, "that you love one
  another. As I have loved you, so you also must love one another." And at once He added: "By
  this everyone will know that you are My disciples, if you have love for one another." He does
  not say, "if you do signs and miracles in the same way." He says, "if you have love for one
  another." And it is certain that no one but the meek and humble can keep this. That is why our
  predecessors never counted certain men as good monks, or as free from the fault of vainglory.
  These were the men who declared themselves exorcists in public. With boastful display before
  admiring crowds, they proclaimed the grace they had either obtained or claimed to have.
relations:
- type: associated-with
  target: gallic.force.power-displayed-disowned
- type: associated-with
  target: gallic.gravity.virtus
use_note:
  means: "Cassian reports Abbot Nesteros teaching that humility is the mistress of virtues and that one who shows off exorcisms or healings is far from Christ."
  not_for:
    - "a denial that a humble monk could work miracles"
    - "Cassian's refusal to narrate miracles, which sits in gallic.quote.cassian-refuses-to-weave-a-tale-of-miracles"
    - "a direct criticism of Martin, whose private exorcisms sit in gallic.quote.martin-exorcism-without-touch-or-reproach"
  years: {from: 426, to: 426}
  status: reviewed
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"Humility therefore"` returns line 39884; `grep -n "which they had either obtained"` returns a hit
in the surrounding sentence, read with `sed -n '39875,39904p'`, inside `<div4 ...
id="iv.v.vi.vii">` (Conference XV, chapter 7). The two clauses are one unbroken paragraph in the
source; this record carries the whole paragraph rather than splicing fragments.

Normalization: line breaks joined with single spaces. The source's curly quotation marks around
the nested sayings of Christ are rendered here as straight double quotes, the same marks in a
different Unicode form - Christ's own two sayings are nested quotations inside Nesteros's
teaching, not this record's own added structure. No word was added, dropped, substituted, or
reordered.

speaker_or_author follows this world's own established convention for reported-abbot teaching (the
Chaeremon quote records): Conference XV is titled, in this edition's own division heading, "The
Second Conference of Abbot Nesteros. On Divine Gifts."