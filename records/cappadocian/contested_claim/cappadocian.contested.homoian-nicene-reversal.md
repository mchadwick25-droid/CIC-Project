---
id: cappadocian.contested.homoian-nicene-reversal
world_id: cappadocian-trinitarian
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: cappadocian.source.church-historians-socrates-sozomen-theodoret
  locus: "the reign-by-reign policy arc, e.g. Socrates HE 2.41 for Constantinople 360 - fifth-century
    external narrative sources outside this world's own c. 394 horizon, used only as secondary
    narrative per Doc_02 §1.6, never as the world's own voice"
  license: public-domain
- source_id: cappadocian.source.imperial-communion-law-of-381
  locus: "the settlement naming eleven eastern bishops whose communion is the test of catholicity, four
    of them this world's own (Amphilochius of Iconium; Helladius of Caesarea, Otreius of Melitene,
    Gregory of Nyssa) - Latin verified directly, though the text is still not vendored into
    this repository's own cic/texts/ on the default branch, per that source record's own rights_status"
- source_id: cappadocian.source.gregory-nazianzus-invectives-against-julian
  locus: "Orations 4 and 5 - one of the only episodes in this whole reversal where both sides' own
    words survive (Julian's own edict and letters alongside Gregory's reply)"
  license: public-domain
- source_id: cappadocian.source.photius-epitome-philostorgius
  locus: "the one surviving Eunomian narrative frame in this world's record, via Photius' hostile
    epitome - the closest thing to an insider account for a defeated theological position, though a
    Eunomian one specifically, not the Homoian court church's own voice"
  license: public-domain
claim: >-
  The Nicene minority's reign-by-reign endurance under the Homoian court church of Constantius and
  Valens, and its sudden establishment under Theodosius, is fairly told by the surviving Nicene
  sources' own account of that reversal - persecution and exile under a hostile establishment,
  vindication under a friendly one.
held_against:
- The Homoian establishment's own voice does not survive - per this world's own source ecology, its
  Cappadocian face "survives almost solely in its opponents' accounts and in imperial acts"; the court
  church of Constantius and Valens is known here through the party it eventually lost to, not through
  any surviving self-description of its own theology, aims, or reasons
- The one surviving narrative frame for a defeated theological position in this world's own record -
  Philostorgius, recovered only through Photius' hostile epitome - is a Eunomian history specifically,
  not a Homoian one; even this partial exception does not give the Homoian court church proper its own
  voice, and should not be mistaken for one
- The church historians whose reign-by-reign narrative supplies most of this account (Socrates,
  Sozomen, Theodoret) are fifth-century, writing after the Nicene side's own victory was settled,
  outside this world's own horizon, and used in this build only as secondary narrative, never as the
  world's own voice - their own retrospective shaping of the story is a real distorting factor this
  claim's telling has to carry
- The invectives against Julian are a genuine exception - one of the only episodes in this whole
  reversal where both sides' own words survive - but a single episode's two-sidedness does not extend
  to the whole reign-by-reign arc that surrounds it
concedes: >-
  That the imperial religious policy really did reverse reign by reign - Constantius' Homoian pressure,
  Julian's pagan interlude, Valens' renewed Homoian pressure and Nyssa's own exile, Theodosius' Nicene
  establishment and the 381 communion law naming this world's own bishops among the East's touchstones -
  is Documented and not contested by any side; the sequence of exiles, depositions, and reversals is
  independently attested across imperial acts and ecclesiastical narrative alike. What cannot be
  settled from this record is how the Homoian establishment itself understood what it was doing across
  those same decades, since almost nothing of that understanding survives in its own words.
divergence_partners:
- This is the in-world content dispute over the reign-by-reign contest itself, and is deliberately
  distinct from the standing build-level classification question already carried on
  cappadocian.gravity.contested-church's own divergence_note (Doc_04 §9 item 1 - whether that gravity is
  best classified Primary-with-situational-annotation or Supporting) - that question is about this
  build's own classification choice, not about what happened in the world, and is not restated here.
  The structural problem named above - a defeated establishment's own voice surviving only in its
  opponents' record - is the same shape of Author Gravity constraint this fleet already discloses for
  the Homoian church's more radical Eunomian wing (this record's own sibling,
  cappadocian.contested.agennetos-transmission) and, elsewhere in the fleet, for HAL's Marcella
  (hal.contested.marcella-agency).
relations:
- type: associated-with
  target: cappadocian.gravity.contested-church
use_note:
  means: "This record holds that the Nicene account of long persecution and sudden vindication is contested, because the Homoian establishment's own voice does not survive."
  not_for:
    - "the Homoian court church's own reasons, which survive nowhere in its own words"
    - "Philostorgius as a Homoian voice, when he is a Eunomian historian known only through a hostile epitome"
    - "the fifth-century church historians as this world's own witnesses"
    - "the classification of the contested church as a primary gravity, which sits in cappadocian.gravity.contested-church"
  years: {from: 360, to: 381}
  status: reviewed
---
Unparked from Doc_02 §1.5 ("The Homoian establishment... its Cappadocian face survives almost solely
in its opponents' accounts and in imperial acts... Adversarial transmission") and §9's Confidence Map
(Documented: "the major public events... Julian's legislation and measures against Caesarea; the 372
division; Nyssa's exile; Constantinople 381; the communion law and its named bishops"). Held for
cappadocian.gravity.contested-church per this step's Primary-gravity minimum; associated-with recorded
reciprocally on the gravity record in the same pass.

Deliberately distinct from the classification question already carried on the gravity record's own
divergence_note (Doc_04 §9 item 1, Primary-with-situational-annotation vs. Supporting): that is a
question about this build's own classification choice, not about the world's own content, and per this
step's own instruction is not duplicated here as a separate contested_claim.

Philostorgius (via Photius) is flagged carefully in held_against and again here: he supplies the
fleet's one surviving defeated-theological-position narrative frame in this world, but he is a
Eunomian historian, not a Homoian-establishment one - a real but partial exception, not a full answer
to the Homoian court church's own silence, and this record does not conflate the two positions.
cappadocian.source.imperial-communion-law-of-381 is cited above without a license value because it was
not independently acquired this session (its own rights_status: the Pharr English translation is
copyrighted and excluded; the Mommsen-Meyer Latin text is public domain but unacquired) - the named
bishops it grounds are independently attested via Van Dam and the secondary literature per that
source's own body note, not resting solely on this citation. canon_cells left empty, matching this
world's own deferral of fleet canon-cell tagging to a later build step.
