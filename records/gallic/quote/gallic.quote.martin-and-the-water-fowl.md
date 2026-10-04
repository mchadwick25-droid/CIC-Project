---
id: gallic.quote.martin-and-the-water-fowl
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Contested
  divergence_note: >-
    The wording is Documented as Sulpitius's own text. The event - Martin commanding a flock of
    water-fowl off a river on the road to Condate - is a Tier-3-shaped wonder, reported by an author who
    says himself he was not present at the death these same days led to, and carried here at the same
    strength as the letter's other reported wonders. What this record carries as load-bearing for the
    fleet is not the event but the equivalence Sulpitius draws in words: the same authority Martin used
    against demons, used here on birds.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2400-2406): Martin commanding water-fowl off a river on the road to Condate'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - participant asks about Martin's power over demons, or whether that same power showed up in smaller, odder ways
  - participant asks for a story that shows what "virtus" meant day to day, not only at moments of high stakes
  prefer_instead:
  - participant wants the deathbed scene, where the letter's real weight sits - retrieve gallic.quote.martin-disciples-plea-and-his-reply or gallic.quote.martin-rebukes-the-devil-and-dies
  - participant is asking whether the episode "really happened" - this record carries the words, not an assessment of the event
text: >-
  Then Martin, with a miraculous power in his words, commands the birds to leave the pool in which
  they were swimming, and to betake themselves to dry and desert regions; using with respect to those
  birds that very same authority with which he had been accustomed to put demons to flight.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  A modern reader may find a bird story an odd thing to record on the road to a deathbed. Sulpitius
  means it as continuity, not distraction: the same power Martin turned on demons all his life, he
  still carried in these last days, and turned on whatever was in front of him - a river full of
  fish-eating birds included.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.figure.martin
modern_rendering: >-
  Then Martin, with miraculous power in his words, commands the birds to leave the pool where they
  were swimming. He orders them to go off to dry and deserted lands. He used on those birds the very
  same authority he had long used to drive demons away.
use_note:
  means: "Sulpitius writes that on the road to Condate Martin commanded water birds to leave a pool, using the authority he used against demons."
  not_for:
    - "an eyewitness report, when Sulpitius says he was not present at Martin's death"
    - "the foreknowledge of death and journey to Condate, which sits in gallic.quote.martin-foreknows-death-and-goes-to-condate"
  years: {from: 397, to: 397}
  status: reviewed
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"put demons to flight"` returns line 2406. Read in context at lines 2400-2406: the sentence opens
"Then Martin, with a miraculous power in his words, commands the birds..." and closes on the clause
originally flagged, "using with respect to those birds that very same authority with which he had been
accustomed to put demons to flight." Carried as one sentence rather than the clause alone, since the
clause is grammatically incomplete without its subject and verb.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single
spaces. No word was added, dropped, substituted, or reordered.

speaker_or_author is given as "Sulpitius Severus, narrating," not a figure id: this is the letter's
own authorial narration, not a saying attributed to Martin himself. (Martin's own words at this
episode - "This is a picture of how the demons act..." - are not part of the host record's text field
and are not carried here.)
