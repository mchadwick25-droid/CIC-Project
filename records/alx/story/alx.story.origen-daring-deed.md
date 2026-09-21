---
id: alx.story.origen-daring-deed
world_id: alexandria-catechetical
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells:
- F6-I
- F3-I
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: "The structural sequence (a drastic youthful act; Demetrius's initial admiration; Demetrius's later use of the same act against Origen) is Widely Accepted as what Eusebius reports. Whether the act itself happened as told - or at all - is Contested: the vendored edition's own translator endnote states plainly that 'some have even gone so far as to believe that he never committed the act, but that the report of it arose from a misunderstanding of certain figurative expressions used by him,' naming three nineteenth-century scholars (Boehringer, Schnitzer, Baur) who held that reading, before concluding in its own voice that there is no reason to doubt the report. This record keeps that live disagreement visible rather than adopting either side."
sources:
- source_id: alx.source.eusebius-historia-ecclesiastica
  locus: 'VI.8 (npnf201 lines 33140-33224: the deed itself, Demetrius''s initial admiration, his later
    reversal, and the ordination by the bishops of Caesarea and Jerusalem; the translator''s own endnote
    recording nineteenth-century scholarly doubt about whether the act happened at all begins at line
    33144)'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - the cost and risk of reading Scripture too literally
  - church conflict and failure, honestly told
  - a hard, self-inflicted act done for the sake of holiness
relations:
- type: associated-with
  target: alx.force.origen-demetrius-conflict
- type: illustrates
  target: alx.gravity.teacher-bishop-tension
- type: associated-with
  target: alx.story.origen-demetrius
narrative_tier: 2
narrative_tier_justification: 'Tier 2 (collected traditional material): Eusebius''s own narrative (HE
  VI.8), written decades after the event from Alexandrian church memory, not a first-person account. The
  structural sequence is Widely Accepted as what Eusebius reports; whether the underlying act is historical
  fact is Contested, per the confidence block above.'
tellable_as: the remembered account of a hard, literal reading Origen once acted on, and how his own bishop
  later turned it against him
text: 'While Origen was still young and teaching the faith in Alexandria, he did something Eusebius calls
  both immature and a proof of unusual faith. He took a hard verse from Matthew - about those who "have
  made themselves eunuchs for the kingdom of heaven''s sake" - in the most literal sense possible, and
  acted on it himself. He taught men and women together, day and night, and wanted no one to accuse him
  of wrongdoing because of it. He tried to keep the act secret. He could not. When his bishop, Demetrius,
  learned of it, he admired the young man''s daring and his faith, and urged him to keep teaching. Years
  later, once Origen had grown famous far beyond Alexandria, the same Demetrius turned that same youthful
  act against him: he wrote to bishops everywhere denouncing it as foolish, at the same time using Origen''s
  ordination by the bishops of Caesarea and Jerusalem - given without Demetrius''s own consent - as fresh
  grounds for attack. Origen himself later judged the verse differently, and wrote against reading it so
  literally.'
absent_detail: 'Eusebius alone reports this; no first-person account from Origen himself describes the
  act, only his later Commentary on Matthew arguing against a literal reading of the same verse. Whether
  the act happened exactly as told, happened at all, or grew out of a misunderstanding of Origen''s own
  words is a real, named disagreement in the source''s own apparatus (see confidence.divergence_note),
  not one this record settles. What exactly changed Demetrius''s mind, and when, the record does not say
  beyond the passing of years and Origen''s growing fame.'
modern_contrast: >
  A modern reader may take this either as proof of extraordinary devotion or
  as evidence of a young man's dangerous self-harm - and Eusebius himself
  already held both readings at once, calling the act "immature" in the same
  breath he called it faithful. This world's own record does not resolve
  that tension into one verdict: it keeps the admiration and the discomfort
  together, and it states plainly, on the strength of Origen's own later
  writing, that he came to judge the verse differently himself.
---
Authored 2026-09-19/20: the alx `world_front` build's own
documented_stories reconciliation. `atlas-v3.html`'s alexandria-catechetical
`documentedStories` array holds three entries; two ("Nursing the
Plague-Stricken While the City Fled", "Three Days of Argument at
Arsinoe") matched existing records directly (`alx.story.plague-nursing`,
`alx.story.arsinoite-conference`). The third, "Origen's Rash Act and the
Bishop Who Turned on Him," covers material - Origen's youthful act on
Matthew 19:12 and Demetrius's later use of it against him - that no
existing alx story record narrates: `alx.story.origen-demetrius` covers
the SAME underlying teacher-bishop rupture but was deliberately built
"structural-only," explicitly refusing motive-level and incident-level
detail per its own body note ("any expansion must come from the sources,
not from filling"). Rather than either inventing detail to match the
site's own telling, or silently dropping a real, sourceable historical
episode, this record was authored fresh, verified directly against the
vendored Eusebius file at the cited lines (not against the site's own
prose, which was read only to identify what needed reconciling).

The site's own version states "modern scholars are divided over whether
the mutilation happened at all," citing Henri Crouzel's 1989 Origen
biography - a work not vendored in this corpus and not independently
checked here. This record does not repeat that specific attribution.
What IS independently verified, directly in the vendored primary
source's own apparatus, is that the 1890 NPNF translator's endnote to
this very passage records nineteenth-century scholarly doubt by name
(Boehringer, Schnitzer, Baur) before arguing against it - a real,
citable disagreement this record grounds `formation_confidence: Contested`
in, without asserting the site's own "modern scholars" framing beyond
what this corpus can independently verify.

Handled with the same restraint this world's other difficult material
uses (compare `alx.story.leonides-martyrdom`'s own modern_contrast on a
teenager's wish to die alongside his father): no graphic elaboration
beyond what Eusebius himself states, and modern_contrast names both a
glorifying and a pathologizing modern misreading rather than endorsing
either.
