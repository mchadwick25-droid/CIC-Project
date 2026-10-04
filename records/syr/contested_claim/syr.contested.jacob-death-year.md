---
id: syr.contested.jacob-death-year
world_id: syriac-edessa-nisibis
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
- source_id: syr.source.theodoret-historia-ecclesiastica
  locus: II.26 (the siege chapter; it gives no year - cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml, lines 11125-11185)
  license: public-domain
- source_id: syr.source.chronicle-of-edessa
  locus: 'entry 17: "died Mar Jacob, bishop of Nisibis," year 649 of the Greeks (337/338 CE) (cic/texts/chronicle-of-edessa_cowper.txt, line 77)'
  license: public-domain
relations:
- type: associated-with
  target: syr.figure.jacob-of-nisibis
claim: Jacob of Nisibis died in 338. The Chronicle of Edessa dates his death then, in the first Persian siege.
held_against:
- the Chronicon Paschale is reported to have him defending Nisibis in 350, which cannot be squared with a 338 death - this text is not vendored, so the report is not rechecked here
- Theodoret's account of Jacob on the wall gives no year, and the tradition blends the city's three sieges, so it cannot confirm 338 or settle on 350
concedes: Jacob's episcopate from c. 309, his presence at Nicaea in 325, and his standing as the city's
  remembered intercessor are solid. The Chronicle of Edessa, which is vendored, records his death in the
  year 649 of the Greeks (337/338 CE). The Chronicon Paschale, which is not vendored, is reported to place
  him at the siege of 350. The two dates are the only positions, and the question stays open on that
  ground alone - neither date is to be silently adopted.
divergence_partners: []
use_note:
  means: "The claim that Jacob of Nisibis died in 338 is contested, since the Chronicle of Edessa gives 337/338 and the Chronicon Paschale is reported to place him defending the city in 350."
  not_for:
    - "a claim that Jacob died in 338"
    - "a claim that Jacob died in 350"
    - "a claim that Theodoret's blended siege tradition fixes the date"
  years: {from: 338, to: 350}
  status: reviewed
---
This date stays genuinely open (a closer critical-edition pass on
Theodoret's Historia Religiosa is the path to resolution if it ever
becomes load-bearing). canon_cells is empty: a dating question with no
participant-facing cell; the figure and story records carry the honest
hedge.
