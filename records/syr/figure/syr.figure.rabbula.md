---
id: syr.figure.rabbula
world_id: syriac-edessa-nisibis
record_type: figure
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: syr.source.petersen-diatessaron
  locus: the displacement discussion
  license: in-copyright-consultation
names:
- name: Rabbula
  tag: in-world
- name: Rabbula, bishop of Edessa (411-435)
  tag: scholarly
dates:
  floruit: 'bishop of Edessa 411-435: the generation after this world''s window closes; traditionally
    credited with the Diatessaron-to-Peshitta shift and the suppression of the remaining Bardaisanite
    and Marcionite communities'
  died: '435'
narratable: false
bridge_line: the bishop just past this world's horizon, under whom its one woven Gospel gave way to the
  four
relations:
- type: associated-with
  target: syr.force.transmission-ending
- type: associated-with
  target: syr.contested.rabbula-peshitta
---
OUT-OF-WINDOW boundary figure, included so the closing transition can
be named without being smeared into the window: his episcopate
(411-435) begins after 410. His personal causal role in the
Diatessaron-to-Peshitta shift is Contested (Voobus argued the
Peshitta predates him - Doc_01 Round 3 cosmetic fix;
syr.contested.rabbula-peshitta). The voice speaks of him only as
what came after its own horizon.

FIXED 2026-08-26 (cross-world transparency audit): names[].scholarly
used to read "Rabbula, bishop of Edessa 411-435 - JUST PAST this
world's own boundary" - a build-team editorial aside that
engine.m4.name_bridge and FigureBridgeMark.tsx render verbatim to the
participant as this figure's "known to scholars as" line, in violation
of gate_no_build_attribution's own purpose (participant-facing fields
carry no build commentary). The same fact - that Rabbula sits just
past this world's own window - is already stated cleanly in
`bridge_line` and `dates.floruit` above, and in this note; the
scholarly name field itself now just names him, matching every other
syr figure's names[] convention (e.g. syr.figure.ephrem's "Ephrem the
Syrian (Ephraem Syrus, c. 306-373)").
