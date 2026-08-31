---
id: cappadocian.story.famine-open-barns
world_id: nicene-cappadocian
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: unverified
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: "The event and its broad shape (drought, hoarding, preaching, granaries opened, relief organized) are Widely Accepted; the exact year is Contested within a year or two of c. 368/9. The homily text itself (cappadocian.source.basil-moral-famine-homilies) is verification_state unverified in this world's own Source Registry - genuinely named and classified, but never independently checked against an acquired edition - so this record uses no direct quotation from the homilies. Oration 43's narrative frame corroborates from within Basil's own circle but is an encomium, and its scene-level dramatization is not treated as independent attestation."
sources:
- source_id: cappadocian.source.basil-moral-famine-homilies
  locus: "the homilies on famine and drought; on the rich fool's barns; against usury"
- source_id: cappadocian.source.gregory-nazianzus-oration-43-funeral-encomium-basil
  locus: "the famine-leadership narrative frame"
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what this world believed wealth was for, or how it treated the poor"
  - "participant asks about famine, drought, hoarding, or usury in this world"
  do_not_retrieve_when:
  - "participant asks about the poorhouse-hospital complex specifically - that is a later, separate institution (retrieve cappadocian.story.poorhouse-famine-month instead)"
relations:
- type: associated-with
  target: cappadocian.figure.basil
- type: associated-with
  target: cappadocian.story.poorhouse-famine-month
narrative_tier: 1
narrative_tier_justification: "Tier 1: the preaching is the preacher's own homiletic record, delivered at the time of the crisis, not a later retelling. Oration 43's narrative frame corroborates from a documented eyewitness within Basil's own circle, but it is an encomium with a case to make, and its scene-level detail is flagged rather than treated as independent record. Widely Accepted rather than Documented at full strength: the homily text itself has not been independently checked against an acquired edition (see divergence_note); the event's broad shape is not in serious doubt."
tellable_as: "A famine strikes Caesarea, and a young priest's preaching shames the rich into opening their granaries."
text: >-
  In the years before Basil became bishop, drought struck Caesarea and its
  countryside. The harvest failed, and grain grew scarce and dear. Those who
  had storehouses full held their grain back, waiting for the price to climb
  higher before they would sell. Basil, then a priest, preached against them
  without softening the charge: to hoard a neighbor's bread while the
  neighbor starves is theft, whatever the law calls it, and the man who tore
  down his barns to build bigger ones, in the Gospel's own parable, learned
  that lesson too late to matter. He preached against lending at interest for
  the same reason - profiting from another's desperate need is no different
  in kind. The preaching did not stay preaching. Granaries opened. Relief was
  organized for the hungry, funded and distributed for as long as the crisis
  lasted. When his own funeral oration recalled it years later, it was named
  as proof of the kind of bishop this world already knew he would be, before
  he ever held the office.
absent_detail: "The homilies' own exact wording is not verified against a checked edition, so no phrase from them is quoted here. No account survives from any one household actually fed during the famine - only the preacher's own record of the preaching and its effect."
modern_contrast: >-
  A modern reader might picture organized disaster relief - a charity with a
  name, a budget, and volunteers. This world's own record is narrower: one
  priest's preaching, aimed at named local landowners hoarding grain in a
  single regional drought, converted their storehouses into relief through
  public shame and personal appeal - not a standing institution, and not
  (yet) the purpose-built poorhouse-hospital complex that came later under
  his own episcopate.
---
Derived from Doc_09 entry #1 (Tier 1). SOURCING HONESTY CARRIED FORWARD:
cappadocian.source.basil-moral-famine-homilies is one of the three sources
this build already caught as falsely-claimed-verified and corrected to
verification_state: unverified (alongside the martyr homilies and Against
Eunomius). This record's own confidence block and text discipline (no
quotation marks around any homiletic phrase) carry that same honesty
forward rather than repeating the earlier overclaim a fourth time.

FEC / GRAVITY LINKAGE (parked for B-5, per this project's own migration
precedent for exactly this timing problem - see pahc.story.mutual-aid-
prisoner's own body note, and the S6.2/IJC checkpoint's "FEC parked in
bodies" note): cappadocian's own gravity and force records do not exist
yet at this step, so no gravity/force target is put in relations[] above.
This story is the touchstone illustration of Gravity 2 (the ascetic
reordering of life toward koinōnia and the poor, Doc_04 §4) - specifically
its "wealth arraigned in famine" clause - and background for Gravity 7
(the bishop as public patron, Doc_04 §4), since Basil acts here as a public
patron of relief before he ever holds the episcopal office Gravity 7
otherwise centers on. Both connections are to be converted into real
relations[] entries once cappadocian's own gravity records exist (B-5).

Relations to cappadocian.figure.basil and cappadocian.story.poorhouse-
famine-month are declared directly above since both records exist in this
same authoring batch (B-4) and the reciprocal edge is set on each.
