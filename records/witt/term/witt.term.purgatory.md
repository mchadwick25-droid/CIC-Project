---
id: witt.term.purgatory
world_id: lutheran-wittenberg-and-its-congregations
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: Documented as a real change across our own texts, both voices, rather than a fixed
    position held from the first day -- the entry states the arc rather than flattening it (Doc_03 had
    proposed 'Luther-only'; Doc_06's own reading of Ap 5003-6377 found the confessional voice too, corrected
    this pass).
sources:
- source_id: witt.source.luther-disputation-on-the-power-and-efficacy
  locus: the Ninety-Five Theses, Thesis 1517 reasoning that still allows purgatory's furniture
  license: public-domain
- source_id: witt.source.luther-four-hymnal-prefaces-to-walters-gesangb
  locus: the 1542 funeral preface -- purgatory among the 'popish horrors' abolished
  license: public-domain
- source_id: witt.source.melanchthon-apology-of-the-augsburg-confession
  locus: the Apology, read this pass -- 'Scripture does not teach' purgatory (Ap 5003-5011, 6363-6365)
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - purgatory
  - what happened to the idea of purgatory over our own history
  prefer_instead:
  - the participant means indulgences themselves (retrieve indulgence)
relations:
- type: associated-with
  target: witt.term.indulgence
- type: associated-with
  target: witt.term.the-keys
- type: associated-with
  target: witt.term.death
plain_meaning: In 1517 we still argued about purgatory. By 1531 we said Scripture does not teach it. By
  1542 we buried our dead without it.
world_word: purgatory -- reasoned with, then denied, then buried
false_friend:
- assuming we never used the word, or that our founder denied it from his first day
senses:
  informational: 'In 1517 the word was still furniture: ''Hell, purgatory, and heaven seem to differ as
    do despair, almost-despair, and the assurance of safety,'' and the only dispute was whether the pope''s
    keys reached it. By 1531 we said flatly that eternal punishments commuted ''to the punishments of
    purgatory'' is a scheme Scripture does not teach, and that the keys ''have not the power of binding
    and loosing except upon earth.'' By 1542 our founder''s own funeral preface counted purgatory among
    the things ''abolished, done away, and out-and-out made an end of'' at our burials, against ''our
    doctrine of the resurrection, not that of purgatory with its pains and expiations.'''
  evidential: A real change traced across three periods and two voices, not a single fixed denial.
  personal: 'This is a word whose arc is our own history: reasoned with, then denied, then buried -- and
    we state that change rather than pretend we never held the earlier position.'
  translational: Do not assume we never used the word purgatory or denied it from day one; we reasoned
    inside it in 1517 and had refused it by 1531.
quick_meaning: A belief we reasoned with early on, then denied, then dropped from our own burials.
distortion_risk: high
use_note:
  means: "Purgatory meant a doctrine still reasoned with in 1517, denied as unscriptural by 1531 and buried without by 1542."
  not_for:
    - "a claim that the word was never used, or that Luther denied it from his first day"
    - "indulgences themselves, which sit in witt.term.indulgence"
  years: {from: 1517, to: 1542}
  status: provisional
---
Built from Doc_06 §5 entry 1.5 (purgatory, Tier 2, confirmed at Doc_03's own estimate). Register emic. Doc_06 tags: [SC][RT][DR]. Author Gravity: none -- both voices (Ap 5003-5011, 6363-6365; Doc_03 had proposed 'Luther-only, cross-register'). Quotations carried from Doc_06's own script-verified base (§10), not independently re-opened against the vendored files by this authoring pass.

Relations above are this batch's own reading of Doc_06's own Related Terms line for this entry, closed for structural reciprocity by this script's close_reciprocity() (see module docstring, disclosed-scope item 1) -- not Doc_06's own §7 candidate-return-link reconciliation pass, which was not separately re-run here.
