---
id: desert.limit.f1-t-original-sin-eucharist-faith
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
statement: "Were people born already guilty, carrying Adam's sin? Was the bread and cup at communion the very body and blood of Christ, in the way later theology called transubstantiation? Were people saved by faith alone, apart from works? We have no answer to give. No letter and no story we kept speaks to these questions in so many words."
why_sources_cannot_answer: "desert.gravity.scriptural-engagement's own registered evidence is practical and occasion-bound, not systematic - a verse taken up as counsel for one struggle, not a doctrine argued through. Original sin, eucharistic theology, and faith-versus-works are exactly the kind of systematic, school-level questions this world's own surviving voice does not engage; the one place this corpus does show doctrinal boundary-drawing (desert.dw.f1-i-god, on the Trinity) answers a different question, forced on Antony by outside controversy rather than raised from within. This is a genuine gap in what survives in the Vita, checked directly by full-text search rather than asserted; the Apophthegmata carries no vendored edition, so this record cannot make the same check there and does not claim to. Neither gap is evidence that these questions had no answer among desert participants."
nearest_material:
- desert.dw.f1-i-god
- desert.dw.c-e-writings
- desert.gravity.scriptural-engagement
relations:
- type: associated-with
  target: desert.dw.f1-i-god
- type: associated-with
  target: desert.dw.c-e-writings
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
