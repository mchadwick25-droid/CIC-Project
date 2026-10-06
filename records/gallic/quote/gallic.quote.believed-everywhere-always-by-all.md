---
id: gallic.quote.believed-everywhere-always-by-all
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
    Documented as Vincent's own formulation in the Commonitory (ch. 2 [6]), the single most quoted
    statement of his method, internally dated to 434 (Doc_01 §2.3).
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 2 [6] (npnf211 div iii.iii, file lines 12185-12190): Vincent's rule for distinguishing true Catholic faith from heresy"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks for Vincent's own definition of what makes a belief truly Catholic"
  - "participant asks about universality, antiquity, and consent as a test of doctrine"
  prefer_instead:
  - "participant asks how this rule was actually applied to a specific heresy - this record carries the rule itself, stated in general form"
text: >-
  Moreover, in the Catholic Church itself, all possible care must be
  taken, that we hold that faith which has been believed everywhere,
  always, by all. For that is truly and in the strictest sense
  "Catholic," which, as the name itself and the reason of the thing
  declare, comprehends all universally. This rule we shall observe if
  we follow universality, antiquity, consent.
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  This is Vincent's most famous formulation, later known by the Latin tag "quod ubique, quod semper,
  quod ab omnibus" - what has been believed everywhere, always, by all. He states it here as a
  working test, not an abstract slogan, and immediately breaks it into three named parts - place,
  time, and consent - that his following chapters apply one at a time.
modern_rendering: >-
  Within the Catholic Church, we must take great care to hold only what
  has been believed everywhere, always, by everyone. That is what
  "Catholic" truly means: it takes in everyone. The word itself says
  so, and so does plain logic. We follow this rule by holding to
  universality, antiquity, and agreement.
relations:
- type: associated-with
  target: gallic.gravity.received-not-invented
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"believed everywhere, always, by all"` returns one hit, line 12187, inside `<div2 title="Chapter II. A
General Rule for distinguishing the Truth of the Catholic Faith from the Falsehood of Heretical
Pravity." ... id="iii.iii">`. The passage runs lines 12185-12190: "Moreover, in the Catholic Church
itself, all possible care must be taken, that we hold that faith which has been believed everywhere,
always, by all. For that is truly and in the strictest sense 'Catholic,' which, as the name itself and
the reason of the thing declare, comprehends all universally. This rule we shall observe if we follow
universality, antiquity, consent."

Normalization: the source wraps "Catholic" in curly double quotation marks as the edition's own
emphasis punctuation; retained here as part of the printed text, distinct from a spoken quotation.
Line breaks joined with single spaces. No word added, dropped, substituted, or reordered.
