---
id: don.term.agonistici
world_id: donatism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-E
- F3-P
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: 'This is the roster''s one [CT] term, and Doc_03 SS0''s three-way split must stay explicit
    rather than be flattened. (1) The group''s bare EXISTENCE is Documented independently of any hostile literary
    framing: CTh 16.5.52 names it, and the vendored Mommsen-Meyer critical text confirms ''circumcelliones argenti
    pondo decem'' at XVI, 5, 52 (412 Ian. 30) -- verified directly. (2) The self-designation agonistici reaches
    this record only through Augustine''s report of it; the law''s own text never uses the word, confirming neither
    it nor its absence. (3) The group''s CHARACTER, scale and typical conduct are HIGH Author-Gravity risk and
    are live scholarly contest -- Frend''s native-social-protest reading treats more of the hostile portrait as
    evidentiary, Shaw''s Sacred Violence is the standard corrective, and Boyd (1905) restates the hostile portrait
    uncritically and is explicitly not licensed for it (Doc_02 SS3). Doc_04 SS4 rates the character component
    ''DMR at best... the sharpest divergence in this document''. The build does not adjudicate; the record-level
    formation_confidence is set to the contested component, deliberately, rather than to the Documented existence
    claim, so the record does not read stronger than its weakest load.'
sources:
- source_id: don.source.mommsen-meyer-theodosiani-libri-xvi
  locus: XVI, 5, 52 (412 Ian. 30) -- 'circumcelliones argenti pondo decem'
  license: public-domain
- source_id: don.source.codex-theodosianus-book-16
  locus: 16.5.52, the law naming the group
  license: public-domain
- source_id: don.source.monceaux-histoire-litteraire-tome4
  locus: 'row 52''s own footnote, quoting Augustine, Enarr. in Ps. 132.6 verbatim: "Milites
    Christi Agonistici appellantur." The self-designation reaches this record only through Monceaux''s own
    quotation of the Latin; the vendored NPNF English of the Enarrationes (npnf108) does not carry
    the term at all, checked directly.'
  license: in-copyright-consultation
- source_id: don.source.shaw-sacred-violence
  locus: the standard corrective reading of the hostile portrait
  license: in-copyright-consultation
- source_id: don.source.frend-the-donatist-church
  locus: the older native-social-protest reading
  license: in-copyright-consultation
- source_id: don.source.boyd-ecclesiastical-edicts-theodosian-code
  locus: restates the hostile characterisation uncritically; not licensed for it
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - a participant uses 'Circumcellion' or 'agonistici', or asks about the rural itinerant members and their reputation
  - a participant asks whether the violent portrait of this group is accurate
  - the conversation reaches Numidia specifically, or the group's relation to the wider hierarchy
  prefer_instead:
  - ordinary Numidian believers are being asked about generally, with no reference to this specific contested
    group
relations:
- type: associated-with
  target: don.term.refusal-of-imperial-legitimacy
- type: associated-with
  target: don.term.persecutio
plain_meaning: Some of us in the Numidian countryside call ourselves agonistici -- contestants, those who strive.
  Our opponents call us Circumcellions and paint us as violent wanderers. That we exist is beyond doubt. What
  we were actually like is a question the surviving record cannot close.
world_word: agonistici
false_friend:
- '''Circumcellion'' as an accepted self-description rather than the opponents'' own label'
- a vivid hostile portrait treated as reliable because it is detailed
- a proxy for what ordinary members of this communion were like anywhere outside rural Numidia
- a modern revolutionary or class-war movement read back into a fourth-century countryside
senses:
  informational: A rural group concentrated in Numidia, reported by Augustine to have called itself agonistici,
    and called Circumcellions by its opponents. The hostile portrait is itinerancy, social marginality, attacks
    on rival clergy and forced rebaptisms. Imperial legislation takes legal notice of the group by name. Its reported
    involvement in the suppression of the Maximianists ties it to the sharpest internal crisis of the period.
  evidential: 'The one place in this lexicon where three evidentiary tiers must be stated separately. Existence:
    Documented, independently, in imperial law whose critical text is vendored and directly checked. Self-designation:
    reaches this record only through Augustine''s report, which Doc_02 SS6 judges reliable as reportage while
    still judging him a hostile interpreter. Character and scale: Contested, HIGH Author-Gravity risk, Dominant
    Modern Reconstruction at best on Shaw''s reading. Doc_04 SS3.5 also confirms the phenomenon Supporting for
    the Numidian regional sub-ecology only, not ecology-wide -- so any account that lets this group stand for
    the movement as a whole has overreached the evidence.'
  personal: 'In that region, belonging to this communion was not belonging to a minority. It was belonging to
    the ordinary church of one''s own village. The contest is narrower than it looks: whether the vivid, often
    violent character the opponents describe covers that whole regional strength, or only ever described a smaller
    and more provocative element the hostile record chose to make stand for the rest.'
  translational: '''Weren''t they basically a violent fringe?'' -- that is exactly the question the evidence will
    not close. The name they are usually given is not their own; the portrait attached to it comes almost entirely
    from people with every reason to make them look dangerous; and the one piece of independent testimony, an
    imperial law, confirms only that they existed and were legislated against. A fair account names the question
    open rather than repeating the portrait as fact.'
quick_meaning: Contestants -- our own name for the country strivers our opponents call Circumcellions.
distortion_risk: high
prior_sense: 'Agonistes is a contender at the games; agonistici carries that sense of one who strives in a contest.
  The opponents'' word runs the other way: circum cellas, those who linger around the shrines.'
use_note:
  means: "Agonistici, 'contestants', is the name Augustine reports for the rural Numidian group opponents called Circumcellions; its existence is certain, its character unsettled."
  not_for:
    - "a claim that 'Circumcellion' was an accepted self-description rather than the opponents' own label"
    - "a claim that the vivid hostile portrait is reliable because it is detailed"
    - "a claim that this group shows what ordinary members of the communion were like outside rural Numidia"
    - "a claim that the group was a modern revolutionary or class-war movement"
  years: {from: 311, to: 439}
  status: reviewed
---
Built from Doc_06 SS1 entry 018 and SS2 (the roster's sole [CT] term; contest type Meaning + Historical scope) and `Lexicon-Chunks/donlex018_agonistici.md`. formation_confidence is set to Contested rather than to the Documented existence claim so the record does not read stronger than its weakest load-bearing component; the three-way split is stated in full in divergence_note and senses.evidential, per Doc_03 SS0 and Doc_04 SS3.5.
