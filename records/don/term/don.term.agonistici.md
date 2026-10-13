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
  locus: 'Augustine, Enarrationes in Psalmos 132.6: ''milites Christi agonistici appellantur''. Monceaux
    quotes this in a footnote and reads it as the group''s own name for itself.'
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
plain_meaning: Augustine says some of us in the country called ourselves agonistici. It means contestants.
  Our opponents called us Circumcellions and said we were violent wanderers. That we existed is beyond
  doubt. What we were like, the record cannot say.
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
  personal: In Numidia, belonging to this communion did not mean belonging to a minority. It meant belonging
    to the church of one's own village. The open question is narrower than it looks. Did the violent character
    our opponents describe fit the whole region? Or did it fit only a small, provocative part that the hostile
    record let stand for the rest?
  translational: '''Weren''t they basically a violent fringe?'' That is the question the evidence will not
    close. The name usually given to them, Circumcellions, was not their own. Almost all of the portrait
    comes from people with every reason to make them look dangerous. The one independent witness, an imperial
    law, shows only that they existed and were legislated against. A fair account leaves the question open
    and does not repeat the portrait as fact.'
quick_meaning: Contestants. Augustine says our side called the country folk this, and their foes had another name.
distortion_risk: high
prior_sense: 'Agonistes is a contender at the games; agonistici carries that sense of one who strives in a contest.
  The opponents'' word runs the other way: circum cellas, those who linger around the shrines.'
use_note:
  means: "Agonistici, 'contestants', is the name Augustine reports for the rural Numidian group opponents called Circumcellions; its existence is certain, its character unsettled."
  not_for:
    - "a claim that 'Circumcellion' was an accepted self-description rather than the opponents' own label"
    - "a claim that the vivid hostile portrait is reliable because it is detailed"
    - "a claim that this group shows what ordinary members were like outside rural Numidia; its Numidian scope is set in don.gravity.circumcellion-agonistici"
    - "a claim that the group was a modern revolutionary or class-war movement"
  years: {from: 311, to: 439}
  status: reviewed
---
Built from Doc_06 SS1 entry 018 and SS2 (the roster's sole [CT] term; contest type Meaning + Historical scope) and `Lexicon-Chunks/donlex018_agonistici.md`. formation_confidence is set to Contested rather than to the Documented existence claim so the record does not read stronger than its weakest load-bearing component; the three-way split is stated in full in divergence_note and senses.evidential, per Doc_03 SS0 and Doc_04 SS3.5.
