---
id: gallic.quote.salvian-ever-present-judgment-gallic-provinces
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Salvian's own text (Gov. VII.12, read at its locus for this record) - the one
    place this world's own gravity of imminent/present judgment shifts, in the source's own words,
    from future expectation to a claim about the present. Named Tension as to scale/hyperbole
    carried per gallic.force.barbarian-fiscal-ruin's own divergence_note; not resolved here.
sources:
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: "VII.12 (Sanford pp. 203-204): the barbarian sweep through Germany, the Belgae, Aquitaine,
    and the whole of the Gallic provinces, read as the ever-present judgment of God"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how this world's southern voice made sense of the barbarian collapse"
  - "participant asks whether judgment, for this world, was only a future expectation"
  prefer_instead:
  - "participant wants the shorter, single-sentence version of the same claim - retrieve gallic.quote.salvian-present-judgment-clearly-shown"
text: >-
  We are judged by the ever-present judgment of God, and thus a most
  slothful race has been aroused to accomplish our destruction and
  shame. They go from place to place, from city to city, and destroy
  everything. First they poured out from their native land into
  Germany, which lay nearest them, a country called barbarous, but
  under Roman control. After its destruction, the country of the
  Belgae burst into flames, then the rich estates of the luxurious
  Aquitanians, and after these the whole body of the Gallic provinces.
speaker_or_author: Salvian of Marseilles, On the Government of God
license: verbatim
modern_lens_note: >-
  Salvian names the geography in order, region by region, as the barbarian advance actually moved
  through it - this is not rhetorical vagueness but a specific claim about where the ruin went and
  in what sequence, offered as proof that the judgment is real and ongoing, not a thing to fear
  someday.
modern_rendering: >-
  We are judged by the ever-present judgment of God. And so a most sluggish people has been
  stirred up to bring about our destruction and shame. They go from place to place, from city to
  city, and destroy everything. First they poured out of their native land into Germany, which
  lay nearest to them. It was a country called barbarous, but it was under Roman control. After
  it was destroyed, the country of the Belgae burst into flames. Then the rich estates of the
  luxurious Aquitanians burned. After these, the whole body of the Gallic provinces went up in
  flames.
relations:
- type: associated-with
  target: gallic.force.barbarian-fiscal-ruin
- type: associated-with
  target: gallic.gravity.judgment-imminent-present
use_note:
  means: "Salvian, in On the Government of God, reads the barbarian sweep from Germany through the Belgae and Aquitaine into all Gaul as God's present judgment."
  not_for:
    - "an exact chronicle of the invasions rather than a preacher's indictment"
    - "the captured general read as judgment, which sits in gallic.quote.salvian-present-judgment-clearly-shown"
    - "a date for each invasion, which the passage does not give"
  years: {from: 439, to: 450}
  status: provisional
---
Verified directly against cic/texts/salvian_on-the-government-of-god_sanford1930.txt. `grep -n
"ever-present judgment of God"` returns line 9144; `grep -n "country of the Belgae"` returns line
9150. Read with `sed -n '9135,9153p'`. The quoted span runs from "We are judged..." through
"...whole body of the Gallic provinces.", ending at the paragraph's own period, before "This ruin
spread gradually..." begins a new thought - the full, unedited continuous passage (numbered
section 12 of Book VII in this edition), not an ellipsis joining separated fragments. This one
record carries the whole, unedited paragraph rather than splitting it into narrower excerpts,
avoiding a bare, unfinished ellipsis; both gallic.force.barbarian-fiscal-ruin and
gallic.gravity.judgment-imminent-present point here for the verbatim wording of their own
citations to this same passage.

Normalization: hard line-wraps rejoined with single spaces, including a hyphenated line-break word
("de-\nstruction"). No word was added, dropped, substituted, or reordered.