---
id: witt.figure.melanchthon
world_id: lutheran-wittenberg-and-its-congregations
record_type: figure
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: Documented as the Augsburg Confession's own drafter, directly attested by the document's
    own title page and preface as read in this library's vendored edition. No vendored source in this
    library supplies any biographical detail about Melanchthon beyond this role - no birth or death date,
    no personal history, no direct quotation of his own outside the Confession's own institutional voice
    (Doc_09 witt-S09; Source Registry R37).
sources:
- source_id: witt.source.melanchthon-augsburg-confession
  locus: Title page ("Melanchthon (drafter)") and Preface, addressed to the Emperor at the 1530 Diet of
    Augsburg
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - a participant asks who drafted the Augsburg Confession, or who Melanchthon was
  - a participant asks how the movement's teaching was put into a single institutional document
  do_not_retrieve_when:
  - a participant wants a personal biography, a quotation in Melanchthon's own private voice, or any detail
    this library does not attest - only the Confession's own institutional role is documented here
names:
- name: Melanchthon
  tag: in-world
- name: Philip Melanchthon, drafter of the Augsburg Confession (1530)
  tag: scholarly
dates:
  display: Documented in this library only as the Augsburg Confession's own drafter, 1530; no vendored
    source held here gives any other date for him.
narratable: true
bridge_line: The scholar who drafted the confession that electors, princes, and free cities signed together
  before the Emperor at Augsburg in 1530 - the movement's own teaching, named to the whole Empire in one
  corporate document.
relations:
- type: associated-with
  target: witt.story.diet-of-augsburg-1530
- type: associated-with
  target: witt.gravity.justified-by-faith-alone
- type: associated-with
  target: witt.gravity.two-governments
---
Narratable: true, but narrowly, and the boundary is stated directly rather than left implicit. This
library attests exactly one thing about Melanchthon directly: that he drafted the Augsburg Confession,
the strongest single evidentiary document this world holds. Doc_09 witt-S09's own usage guidance
instructs that this story be told "as an institutional act... not as a personal drama centered on any
one figure" - and that instruction bears directly on how this figure record should be used. Melanchthon
is narratable as the confession's own named drafter, standing behind an institutional, corporate act;
he is not narratable, from this library, as a person with a private biography, a personal conversation,
or any documented relationship to Luther beyond what the shared confessional project itself implies.
No Table Talk entry, letter, or personal reminiscence involving Melanchthon is vendored in this world's
library. A Representative drawing on this figure should introduce him as the Confession's drafter and
go no further than that role without inventing.

FEC / GRAVITY LINKAGE (closed at B-5): the connection this record's own Doc_09 entry named above is now a real relations[] entry in this file's frontmatter -- associated-with to G1 (Justified by faith alone [PRIMARY]), G6 (The two governments: the temporal sword, obedience, and the prince as addressee [SUPPORTING]) -- with the reciprocal edge declared on each gravity record itself (witt.gravity.*), exactly as this note said it would when B-5 ran. No longer parked.
