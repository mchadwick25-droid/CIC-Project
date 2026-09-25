---
id: gallic.quote.salvian-on-the-demand-for-circuses
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted: Salvian's own direct address to the city, in the same section (VI.15) as the
    unburied-dead material. The petitioners are named only as "the few men of rank who had survived
    destruction" - the story's own actors are the city's remaining elite, not its ordinary population,
    and this record does not extend the claim beyond that (the host record's own divergence_note draws
    the same line against gallic.term.church-or-circus's broader, different claim). The moral verdict is
    Salvian's own framing, carried as his.
sources:
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: "On the Government of God, Book VI.15 (Sanford 1930, pp. 183-184; file lines 8263-8306): the petition for circuses and Salvian's direct rebuke of the citizens of Trier"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Salvian actually said to the citizens who wanted circuses restored"
  - "participant asks who asked for the games, and how Salvian answered them"
  - "Representative needs Salvian's own direct address, not a summary of his outrage"
  prefer_instead:
  - "participant wants the surviving elite's moral ruin - retrieve gallic.quote.salvian-on-treves-ruined-elite"
  - "participant wants the corpses and the aftermath - retrieve gallic.quote.salvian-on-the-unburied-dead"
  - "participant wants the whole episode told as a story - retrieve gallic.story.circuses-amid-the-ruins, which this record is drawn from"
text: >-
  The few men of rank who had survived destruction demanded of the emperors ... circuses as the sovereign
  remedy for a ruined city. ... Do you, O citizens of Tréves, long for circuses when you have been
  plundered and captured, after slaughter and bloodshed, after stripes and captivity, and the repeated
  destruction of your ruined city? What is more lamentable than this stupidity, more grievous than this
  folly? I confess I thought you most miserable when you were suffering destruction, but I see that you
  are now more miserable when you demand public shows.
speaker_or_author: "Salvian of Marseilles"
license: verbatim
modern_lens_note: >-
  A modern reader may expect an indictment of "bread and circuses" to target rulers, not survivors.
  Salvian's target is the opposite: he addresses the citizens directly, in the second person, and his
  sharpest line reverses what a reader expects sympathy to sound like - "I thought you most miserable
  when you were suffering destruction, but I see that you are now more miserable when you demand public
  shows." Losing the city, for Salvian, was a lesser loss than this request.
modern_rendering: >-
  The few men of rank who survived the destruction asked the emperors for circus games, as the best
  cure of all for a ruined city. ... Citizens of Trier, do you long for circus games? You have been
  plundered and captured. You have lived through slaughter and bloodshed, floggings and captivity, and
  the destruction of your ruined city again and again. What is more pitiful than this stupidity? What
  is more painful than this folly? I admit I thought you most miserable when you were suffering
  destruction. But I see that you are more miserable now, when you demand public shows.
relations:
- type: associated-with
  target: gallic.story.circuses-amid-the-ruins
- type: associated-with
  target: gallic.source.salvian-on-the-government-of-god
- type: associated-with
  target: gallic.quote.salvian-on-treves-ruined-elite
- type: associated-with
  target: gallic.quote.salvian-on-the-unburied-dead
---
Verified against cic/texts/salvian_on-the-government-of-god_sanford1930.txt. `grep -n "survived
destruction demanded"` returns one hit, line 8264; `grep -n "citizens of Tr"` returns hits at lines
8299 (this quote, plural "citizens") and 8319 (singular "citizen," a later, separate address not part
of this record). Read lines 8263-8306 directly.

The ellipsis marks the omission of Salvian's own extended reflection between the two flagged phrases -
"O that I might here and now be gifted with eloquence..." through "...though sane, they acted
senselessly" (roughly 35 lines) - his commentary on why the petition itself is shocking, not part of
either flagged span.

Normalization: line breaks and page-break hyphenation joined; footnote markers dropped; "Tréves" kept
as the translation spells it (the source's own form of "Trier"). No word was added, dropped,
substituted, or reordered within either quoted phrase.
