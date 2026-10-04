---
id: don.term.rebaptism
world_id: donatism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
- F4-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Doc_04 SS3.2: the practice itself is attested directly and repeatedly inside Augustine''s
    own primary text, and argued FOR in Petilian''s own quoted words rather than merely characterised by an opponent
    -- so the practice is Documented, not inferred. The qualification, carried rather than smoothed away, is that
    this corroboration comes from a Donatist voice quoted inside the hostile corpus rather than from a source
    outside it, so the specific argumentative texture remains Augustine-mediated in the same degree as the purity
    doctrine it enacts.'
sources:
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: seven books devoted substantially to this practice
  license: public-domain
- source_id: don.source.augustine-answer-to-petilian
  locus: Petilian's own argument for the practice, quoted clause by clause
  license: public-domain
- source_id: don.source.cyprian-de-unitate
  locus: the third-century North African rebaptism position this sharpens
  license: public-domain
- source_id: don.source.seventh-council-of-carthage-256-anf05
  locus: the 256 council under Cyprian on baptism outside the church
  license: public-domain
- source_id: don.source.codex-theodosianus-book-16
  locus: the imperial legislation naming rebaptism specifically
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - a participant uses 'rebaptism' or 'baptized again', or asks why anyone would need baptism twice
  - a participant asks what the two rival African churches actually fought over
  - the conversation reaches what makes a baptism real, or how someone crosses from one communion to the other
  prefer_instead:
  - the question is about baptism as a general Christian rite, with no bearing on the boundary-crossing question
relations:
- type: presupposes
  target: don.term.traditor-traditio
- type: presupposes
  target: don.term.purity-ministerial
- type: tension-with
  target: don.term.reception-without-reordination
- type: associated-with
  target: don.term.ecclesia
plain_meaning: We do not think of this as baptizing twice. Nothing happened the first time. A hand from a tainted
  line washes nothing. So when someone comes to us from the other church, we give the first real baptism they
  have had.
world_word: rebaptizare
false_friend:
- a modern adult re-baptism chosen for personal renewal or a fresh start
- a ritual scruple about repeating a sacrament, as though the objection were fussiness
- a denial that the first rite happened at all, rather than a denial that it conferred anything
- a private opinion held by a rigorist minority rather than the communion's own enacted norm
senses:
  informational: Baptism given by a minister descended from a traditor-tainted line was held to confer nothing,
    so someone received from the rival communion was baptized -- not re-baptized, on this reckoning, but baptized.
    Successive imperial edicts name the practice specifically, because rebaptizing a Catholic was the plainest
    public refusal of the settlement the state was trying to impose. Its one recorded internal exception is the
    Maximianist clergy, received back without repeating either rite.
  evidential: Documented. Augustine devotes seven books of On Baptism and three of the Answer to Petilian to it,
    and quotes Petilian arguing for it clause by clause -- a Donatist voice reasoning in its own favour, not merely
    a hostile summary. Doc_04 SS3.2 rates the bare practice Documented; the qualification is that the voice reaches
    this record from inside the hostile corpus that preserved it, and that what a rebaptism actually felt like
    to undergo is nowhere recorded (Doc_05 SS2).
  personal: This is the most concretely lived thing in the whole communion. A believer does not merely agree with
    a teaching about tainted ordination; a believer is washed, bodily, into one church and out of another. The
    doctrine becomes one person's own history on one datable day.
  translational: '''Isn''t baptizing someone twice just excessive?'' -- the answer from inside is that the count
    is wrong. There was no first baptism to repeat. And the cost of stopping is exact: to stop would be to concede
    that the rival''s ministers can baptize validly after all, and if theirs were real, this church never needed
    to exist.'
quick_meaning: Washed again, because the first washing gave nothing. Not a repeat -- the first real one.
distortion_risk: high
prior_sense: 'The word already had a history in Africa before the schism: Cyprian''s mid-third-century councils
  used it for receiving those baptized among heretics, against Rome''s contrary practice. What is new after 312
  is not the rite but its target -- another African church holding the same creed.'
use_note:
  means: "For Donatists it was no second baptism: a hand from a tainted line washes nothing, so those from the other church received their first real one."
  not_for:
    - "a claim that it was a modern adult rebaptism chosen for personal renewal"
    - "a claim that it was a ritual scruple about repeating a sacrament"
    - "a claim that it denied the first rite happened at all, rather than that it conferred anything"
    - "a claim that it was a private opinion of a rigorist minority rather than the communion's enacted norm"
  years: {from: 311, to: 439}
  status: reviewed
---
Built from Doc_06 SS1 entry 002 (Tier 1, confirmed) and `Lexicon-Chunks/donlex002_rebaptism.md`. The one-directional Related-Terms link Doc_06 SS4 flagged (Rebaptism -> Church/Ecclesia, not yet reciprocated) is completed here as a mutual `associated-with` pair, since both records are now built; Doc_06 SS5 names that completion as the open deployment-layer item.
