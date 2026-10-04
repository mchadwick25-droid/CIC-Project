---
id: gallic.quote.salvian-on-the-unburied-dead
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
    Widely Accepted: Salvian states this as his own direct experience ("a sight that I myself
    endured"), at the same locus (VI.15) that gives "three times destroyed" against VI.13's "four
    times" for the same city - the host record's own divergence_note names this inconsistency and this
    record keeps it rather than resolving it. The moral reading that follows in the source (increased
    wickedness after destruction) is Salvian's own framing, not carried here as this record's
    independent claim.
sources:
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: "On the Government of God, Book VI.15 (Sanford 1930, pp. 183-184; file lines 8242-8261): the city's repeated destruction and the unburied dead"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks for a specific, vivid description of what the barbarian destruction looked like"
  - "participant asks whether Salvian was an eyewitness"
  - "Representative needs the exact wording behind the story's most graphic image"
  prefer_instead:
  - "participant wants the surviving elite's moral ruin - retrieve gallic.quote.salvian-on-treves-ruined-elite"
  - "participant wants the circus petition and Salvian's rebuke - retrieve gallic.quote.salvian-on-the-demand-for-circuses"
  - "participant wants the whole episode told as a story - retrieve gallic.story.circuses-amid-the-ruins, which this record is drawn from"
text: >-
  This can be quickly tested by the example of the greatest city of Gaul, three times destroyed by
  successive captures, yet when the whole city had been burned to the ground, its wickedness increased
  even after its destruction. ... Some perished of hunger, others of nakedness, some wasting away,
  others paralyzed with cold, and so all alike by diverse deaths hastened to the common goal. ... There lay
  all about the torn and naked bodies of both sexes, a sight that I myself endured. ... lacerated by
  birds and dogs. The stench of the dead brought pestilence on the living: death breathed out death.
speaker_or_author: "Salvian of Marseilles"
license: verbatim
modern_lens_note: >-
  A modern reader may expect a list of causes of death to build toward sympathy for the dead. Salvian's
  own point is the opposite: the dead are evidence against the living. He does not pause to mourn each
  death before moving to the smell of pestilence, and "death breathed out death" reads as an indictment
  of what survived the sack, not an elegy for what did not.
modern_rendering: >-
  This can be tested quickly by the example of the greatest city in Gaul. It was destroyed three
  times, captured again and again. Yet when the whole city had been burned to the ground, its
  wickedness grew even after its destruction. ... Some died of hunger, others from having no clothes.
  Some wasted away, others were frozen stiff with cold. And so all of them, by different deaths,
  hurried to the same end. Torn and naked bodies of men and women lay all around. I myself had to
  endure that sight. ... torn apart by birds and dogs. The stench of the dead brought disease on the
  living. Death breathed out death.
relations:
- type: associated-with
  target: gallic.story.circuses-amid-the-ruins
- type: associated-with
  target: gallic.source.salvian-on-the-government-of-god
- type: associated-with
  target: gallic.quote.salvian-on-treves-ruined-elite
- type: associated-with
  target: gallic.quote.salvian-on-the-demand-for-circuses
use_note:
  means: "Salvian, in On the Government of God, describes the greatest city of Gaul after repeated sacks, its dead lying unburied, a sight he says he himself endured."
  not_for:
    - "a consistent count of the sacks, when Salvian says three here and four in gallic.quote.salvian-on-treves-ruined-elite"
    - "the circus petition, which sits in gallic.quote.salvian-on-the-demand-for-circuses"
    - "a lament for the dead, when Salvian uses them as an indictment of the living"
  years: {from: 439, to: 450}
  status: provisional
---
Verified against cic/texts/salvian_on-the-government-of-god_sanford1930.txt. `grep -n "three times
destroyed"` returns one hit, line 8242; `grep -n "torn and naked"` returns one hit, line 8255-8256;
`grep -n "death breathed out death"` returns one hit, line 8259. Read lines 8226-8261 directly.

The three remaining ellipses mark omitted material within the same numbered section, VI.15: between
"increased even after its destruction" and "Some perished of hunger" the source lists (not flagged for
this record) the causes of death by sack-related disaster generally, which the quoted "so all alike by
diverse deaths" already summarizes; between "hastened to the common goal" and "There lay all about" the
source opens a new paragraph ("Worse than all this, other cities suffered..."); and between "a sight
that I myself endured" and "lacerated by birds and dogs" the source has "These were a pollution to the
eyes of the city, as they lay there," which the flagged span itself already skips with its own
ellipsis - "lacerated by birds and dogs" is retained, exactly as the flagged span has it.

At the point between "successive captures," and "yet when the whole city had been burned to the
ground," the vendored file (line 8242) has "three times destroyed by successive captures,” yet when
the whole city..." - the stray curly close-quote glyph glued directly onto "captures," is Sanford's own
superscript footnote marker (note 52) mangled by OCR, not a quotation mark and not a gap. Read with the
artifact removed, the sentence runs on unbroken: "three times destroyed by successive captures, yet
when the whole city had been burned to the ground, its wickedness increased even after its
destruction." No content is omitted at that point.

Normalization: line breaks and page-break hyphenation joined; footnote markers dropped. No word was
added, dropped, substituted, or reordered within any quoted phrase.
