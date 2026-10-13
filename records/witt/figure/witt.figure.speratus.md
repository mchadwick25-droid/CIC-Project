---
id: witt.figure.speratus
world_id: lutheran-wittenberg-and-its-congregations
record_type: figure
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented only as the named author of three of the eight hymns in Wittenberg's first hymn-book (1524),
    per Bacon's own bibliographic account, directly read and verified. Inferential-Thin for everything
    else: the window anecdote itself is Tier 3, related rather than documented, and - on this record's
    own direct re-reading of the vendored text - does not actually name Speratus as the anecdote's own
    wanderer; only the hymn is his. No biographical detail about Speratus survives in this library beyond
    his authorship of the hymns themselves.
sources:
- source_id: witt.source.leonard-introduction-to-the-hymns-of-martin
  locus: Bacon's own bibliographic note naming "not less than three" of the 1524 hymn-book's four hymns
    as Speratus's own, including "Es ist das Heil uns kommen her"; the window anecdote, which names only
    "a wanderer from Prussia," not Speratus by name, as its own singer
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - a participant asks who wrote the hymn sung under Luther's window
  - a participant asks about the authors of Wittenberg's first hymn-book beyond Luther himself
  prefer_instead:
  - claiming Speratus himself was physically present, singing under Luther's window - the vendored text
    names only an unnamed wanderer as the singer, Speratus only as the hymn's author
  - narrating any biographical detail about Speratus beyond his authorship of these hymns - none is attested
    in this library
names:
- name: Paul Speratus, author of the hymn
  tag: in-world
- name: Paul Speratus (named author of hymns in the 1524 Wittenberg hymn-book)
  tag: scholarly
dates:
  display: Documented in this library only as one of the named authors of Wittenberg's first hymn-book,
    printed 1524; no birth or death date, and no other biographical detail, is given by any vendored source
    held here.
narratable: true
bridge_line: >-
  Paul Speratus wrote at least three of the eight hymns in the first Wittenberg hymn-book, in 1524. We
  know almost nothing else about him. One of his hymns is said to have delighted Luther when a traveler
  from Prussia sang it beneath his window.
relations:
- type: associated-with
  target: witt.story.speratus-hymn-under-the-window
- type: associated-with
  target: witt.gravity.german-for-the-people
---
Narratable: true, but at a boundary this record states with unusual care, because the temptation to
overclaim is real and specific here. What is genuinely Documented is narrow and biographical almost not
at all: Speratus is named as the author of at least three of the eight hymns in Wittenberg's earliest hymn-book
(1524), a fact Bacon's Introduction states directly and this record has verified against the vendored
text. Everything else commonly attached to this figure - that he personally sang under Luther's window,
that the encounter is a verified historical meeting between the two men - is not what the vendored text
itself supports. The anecdote names its own singer only as "a wanderer from Prussia," never as Speratus
in person; Speratus is named, throughout this library, only as the hymn's author, never as the
anecdote's protagonist. witt.story.speratus-hymn-under-the-window's own text narrates the anecdote at
exactly this narrower level, and this figure record does the same: narratable as a named hymn-writer
whose work is attested to have reached and moved Luther, by tradition; not narratable as a person who
is shown, by this library's own text, to have stood beneath that window himself. No other biographical
fact about Speratus - birth, death, career, or any other writing - is attested anywhere in this library.

FEC / GRAVITY LINKAGE (closed at B-5): the connection this record's own Doc_09 entry named above is now a real relations[] entry in this file's frontmatter -- associated-with to G11 (German for the people: vernacular teaching and singing, Latin retained for the learned [SUPPORTING]) -- with the reciprocal edge declared on each gravity record itself (witt.gravity.*), exactly as this note said it would when B-5 ran. No longer parked.
