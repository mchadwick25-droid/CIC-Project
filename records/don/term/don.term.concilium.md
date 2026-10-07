---
id: don.term.concilium
world_id: donatism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-E
- F3-I
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: 'The two councils that matter most -- Cebarsussi (393) and Bagai (394) -- are Documented, and
    their sentences are quoted directly in Augustine''s On Baptism and Answer to Petilian (Doc_04 SS3.6). That
    is also the whole of the problem: no Donatist conciliar acta survive in their own right, so this communion''s
    own conciliar life is known through an opponent''s selective quotation of two sentences he needed for an argument.
    Doc_06 SS1 records ''No change'' to the Tier-3 estimate and no chunk was built, so the term''s development
    here is modest by design.'
sources:
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: the Bagai sentence quoted for Augustine's own argument
  license: public-domain
- source_id: don.source.augustine-contra-cresconium
  locus: the Cebarsussi and Bagai proceedings
  license: public-domain
- source_id: don.source.code-of-canons-african-church-419
  locus: the rival African conciliar tradition running in parallel
  license: public-domain
- source_id: don.source.acts-council-of-carthage-under-cyprian-npnf214
  locus: the third-century African conciliar precedent both sides inherit
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - a participant asks how disputes inside this communion were settled
  - a participant asks about Cebarsussi or Bagai
  prefer_instead:
  - the question is about the ecumenical councils of the same century
relations:
- type: enabled-by
  target: don.term.episcopus
- type: associated-with
  target: don.term.primas
- type: precondition-for
  target: don.term.reception-without-reordination
plain_meaning: Our bishops govern by council, as any true church does. That our councils could judge and discipline
  our own dissidents is part of our claim to be one. Cebarsussi elected a rival primate in 393. Bagai condemned
  him the year after.
world_word: concilium
false_friend:
- an ecumenical council of the whole church, like Nicaea
- an advisory body without binding force -- these councils deposed and restored clergy
- a proceeding whose records survive on its own terms; what survives is an opponent's quotation
senses:
  informational: 'A gathering of this communion''s bishops, claiming the same binding authority the rival hierarchy''s
    councils claim. It is the machinery through which the Maximianist crisis was fought and closed: Cebarsussi
    elected Maximian a rival primate in 393, and the much larger council at Bagai condemned that election in 394
    and later received his clergy back.'
  evidential: 'Documented at the level of these two councils and their sentences, because Augustine quotes them.
    Beyond that the conciliar life of this church is invisible: no acta of its own survive, so how often it met,
    how it deliberated, and what else it decided are not recoverable from the vendored corpus.'
  personal: The councils are the proof of being a real church rather than a protest against one. They are also
    where the sharpest internal inconsistency was enacted, which is why the record of them survives at all --
    an opponent found it useful.
  translational: '''Did they have real church government?'' -- yes, with binding sentences and disciplinary force.
    What they did not have, in the end, was custody of their own records.'
quick_meaning: A council of our own bishops, with power to judge and to restore.
distortion_risk: low
use_note:
  means: "Donatist bishops governed by council and judged their own dissidents: Cebarsussi elected a rival primate in 393, and Bagai condemned him in 394."
  not_for:
    - "a claim that these councils were ecumenical councils of the whole church, like Nicaea"
    - "a claim that they were advisory bodies without binding force"
    - "a claim that their records survive on their own terms rather than through an opponent's quotation"
  years: {from: 393, to: 394}
  status: reviewed
---
Built from Doc_06 SS1 entry 017 (Tier 3, 'No change'). Development is modest by design; the Cebarsussi/Bagai material is drawn from Doc_04 SS3.6 and Doc_05 SS4.
