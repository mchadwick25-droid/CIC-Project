---
id: gallic.quote.three-lentils-and-the-lords-things
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted for the tradition as Cassian transmits it - he offers it as "one instance which I
    will give as an example," typical rather than dated, with no house, brother, steward, or abbot
    named. The wording is Documented as Cassian's own text (Institutes IV.20, read at its locus for
    this record). Contested for the specific attribution: Cassian does not claim to have witnessed the
    episode, and it is set in the East, not in any Gallic house.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes IV.20 (npnf211 div iv.iii.iv.xx, file lines 19227-19248): the three lentil beans, the Abbot's judgment, suspension from prayer and public penance, and the reason given"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how strict the monastery was, what counted as a fault, or how small offenses were punished"
  - "participant uses 'penance', 'sacred property', 'consecrated', or asks what 'poverty' meant in practice"
  - "conversation reaches the interior road at the level of a single lentil, or the reasoning behind graded sanction"
  prefer_instead:
  - "participant wants the general custom this incident illustrates - retrieve gallic.quote.weekly-service-and-sacred-vessels instead, or alongside"
  - "participant is asking about Marmoutier's common property specifically - a different, northern, descriptive text (retrieve gallic.term.monastery-coenobium)"
text: >-
  During the week of a certain brother the steward passing by saw lying on the ground three lentil
  beans which had slipped out of the hand of the monk on duty for the week as he was hastily preparing
  them for cooking, together with the water in which he was washing them; and immediately he consulted
  the Abbot on the subject; and by him the monk was adjudged a pilferer and careless about sacred
  property, and so was suspended from prayer. And the offence of his negligence was only pardoned when
  he had atoned for it by public penance. For they believe not only that they themselves are not their
  own, but also that everything that they possess is consecrated to the Lord. Wherefore if anything
  whatever has once been brought into the monastery they hold that it ought to be treated with the
  utmost reverence as an holy thing. And they attend to and arrange everything with great fidelity,
  even in the case of things which are considered unimportant or regarded as common and paltry, so that
  if they change their position and put them in a better place, or if they fill a bottle with water, or
  give anybody something to drink out of it, or if they remove a little dust from the oratory or from
  their cell they believe with implicit faith that they will receive a reward from the Lord.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  A modern reader hears cruelty over three beans, and a rule that reads as pettiness. But the brother is
  not punished for waste; he is judged careless "about sacred property," because "everything that they
  possess is consecrated to the Lord" - the same reasoning that suspends him from prayer also explains
  why dusting a cell earns a reward. The severity and the small reward sit on the same scale: both
  measure how the monk treats what is not his own.
modern_rendering: >-
  During one brother's week of duty, the steward was passing by. He saw three lentil beans lying on
  the ground. They had slipped from the hand of the monk on duty that week, as he hurried to get them
  ready for cooking. They slipped out along with the water he was washing them in. At once the steward
  asked the Abbot about it. The Abbot judged the monk a petty thief, and careless with sacred
  property. So he was barred from prayer. His careless fault was forgiven only after he had made up
  for it by public penance. For they believe that they do not belong to themselves. They believe, too,
  that everything they have is dedicated to the Lord. So once anything at all is brought into the
  monastery, they hold it must be treated with the deepest reverence, as a holy thing. They look after
  and arrange everything with great faithfulness. They do this even with things thought unimportant,
  or seen as common and trivial. Suppose they move such things and put them in a better place, or fill
  a bottle with water, or give someone a drink from it. Or suppose they sweep a little dust from the
  chapel or from their cell. They believe without doubting that they will receive a reward from the
  Lord.
relations:
- type: associated-with
  target: gallic.story.the-three-lentil-beans
use_note:
  means: "Cassian, in Institutes IV, tells of a monk suspended from prayer for spilling three lentils, because monks treat all monastery goods as consecrated to the Lord."
  not_for:
    - "a Gallic incident, when Cassian sets it in the East without names"
    - "the weekly rotation and handover of vessels, which sits in gallic.quote.weekly-service-and-sacred-vessels"
    - "routine cruelty rather than one example Cassian offers of reverence for sacred property"
  years: {from: 415, to: 426}
  status: reviewed
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml.
`grep -n "three$"` and a read of the surrounding lines locate the passage at the chapter div `<div4
title="Chapter XX. Of the three lentil beans which the Steward found." ... id="iv.iii.iv.xx">` (line
19221), paragraph `iv.iii.iv.xx-p2` (lines 19227-19248). The excerpt is the whole paragraph, verbatim
and unbroken from "During the week of a certain brother" through "receive a reward from the Lord.",
with one editorial endnote reference (n. 777, glossing "Hebdomadarius") falling inside the phrase "for
the week" and "as he was" and dropped as apparatus, not prose.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
No word was added, dropped, substituted, or reordered.

speaker_or_author is gallic.figure.cassian: this is Cassian's own narration, offered, in his own words,
as "one instance which I will give as an example" of the custom described in the previous chapter.
