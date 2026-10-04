---
id: don.quote.the-shores-are-covered
world_id: donatism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Verified word for word against the vendored NPNF volume, where Augustine introduces it as the language
    of "that Council of theirs" and quotes it to be used against them. This is a conciliar decree of this
    communion's own largest recorded council, so the words are ours; the reason they survive is that an
    opponent found them devastating. Augustine quotes the same decree more than once, in slightly different
    English renderings within the same volume, and the form carried here is the fuller of the two. Nothing
    independent of Augustine preserves the decree, so what is verified is the wording he quotes rather
    than the wording that was voted.
sources:
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: Book III (the Bagai decree quoted, followed immediately by Optatus Gildonianus advancing with
    a military force to bring Felicianus and Praetextatus back)
  license: public-domain
- source_id: don.source.augustine-contra-cresconium
  locus: the same decree quoted again in the later work, pressing the same contradiction
  license: public-domain
text: >-
  Seeing that the shipwrecked members of certain men have been dashed by
  the waves of truth upon the sharp rocks, and after the fashion of the
  Egyptians, the shores are covered with the bodies of the dying; whose
  punishment is intensified in death itself, since after their life has
  been wrung from them by the avenging waters, they fail to find so much
  as burial.
speaker_or_author: The council of Bagai, 394 - three hundred and ten bishops of this communion, condemning
  the Maximianist party
license: verbatim
modern_lens_note: >-
  This is not a description of anything that happened. Nobody drowned.
  It is figurative conciliar rhetoric: the "waves of truth" are the
  council's own sentence, and the unburied bodies on the shore are the
  condemned bishops' spiritual standing after it. A modern reader who
  takes it as a report of violence will misread the document entirely.
  What makes the passage matter is what came next. Within a few years
  two of the very men covered by this sentence, Felicianus of Musti and
  Praetextatus of Assuris, were restored to office by the same
  communion - with neither their baptism nor their ordination repeated,
  and with a general's troops enforcing the reconciliation. The
  ferocity of the language and the quietness of the reversal sit in the
  same record, unreconciled, and that is precisely why the decree
  survives: the man quoting it built his central case on the gap.
  Hearing it read aloud, remember also that it was drafted to be
  acclaimed, and was: the same source records that it "formerly called
  forth shouts of unreserved applause."
retrieval:
  tier: 2
  retrieve_when:
  - participant asks what we never settled, or what troubled us about ourselves
  - participant asks how we treated a group that broke away from us
  - participant asks whether we lived up to our own rule
  prefer_instead:
  - participant is asking about an actual shipwreck, drowning, or violent death - the imagery is figurative
relations:
- type: associated-with
  target: don.dw.what-we-never-settled
modern_rendering: >-
  For the waves of truth have hurled the shipwrecked limbs of certain
  men against the sharp rocks. And, as happened to the Egyptians, the
  shores are covered with the bodies of the dying. Their punishment
  grows heavier in death itself. This is because, after the avenging
  waters have squeezed the life out of them, they do not even find
  burial.
use_note:
  means: "The Bagai council of 394 condemned the Maximianist party in figurative language of shipwrecked, unburied bodies, as Augustine quotes it."
  not_for:
    - "a claim that anyone actually drowned or was physically killed"
    - "a claim that the voted wording of the decree is attested independently of Augustine"
    - "a claim that the condemned Maximianist bishops were never received back"
  years: {from: 394, to: 394}
  status: provisional
---
Verified verbatim against the vendored
`npnf104_augustine-anti-manichaean-anti-donatist.xml`, in the passage
where Augustine introduces the words as coming from "the noble decree of
that Council of theirs which formerly called forth shouts of unreserved
applause when it was recited among them for the purpose of being
decreed." No wording added, dropped, or reordered.

The same volume quotes the decree a second time in a shorter and slightly
differently worded rendering ("Even after the manner of the Egyptians,
the shores are full of the bodies of the dying, on whom the weightier
punishment falls in death itself, in that, after their life has been
wrung from them by the avenging waters, they have not found so much as
burial"). The fuller of the two is carried here; the existence of the
second is recorded in `divergence_note` rather than left for a reader to
discover as a discrepancy.

Register `emic`: the speaker is a council of this communion's own
bishops, and the words are its own decree, even though the only channel
by which they reach us is the opponent who quoted them to destroy the
argument they came from. `don.story.bagai-reconciliation` already carries
the same passage as narrative; this record carries it as attributable
speech with the transmission stated.

MODERN RENDERING re-authored: see `worlds/don/Open_Gaps_Tracking.md`
OG-18 for what changed and why. Reciprocal relation declared on
`don.dw.what-we-never-settled`.
