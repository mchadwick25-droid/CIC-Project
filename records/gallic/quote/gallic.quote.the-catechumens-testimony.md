---
id: gallic.quote.the-catechumens-testimony
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Contested
  divergence_note: >-
    Contested rather than Widely Accepted, unlike the companion record for this locus: the witness is
    named only as "a certain catechumen," and the eyewitness claim is itself the hagiographic
    convention this world's own governing framework flags as "convention risk" (Doc_04 G5). What is
    Widely Accepted is only that Sulpitius records this as the man's own account and as the origin of
    Martin's reputation at Tours; the tribunal, the two angels, and the man's own report of them are
    Inferential-Thin, carried as the tradition's own claim, not this record's finding.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. VII (npnf211 div ii.ii.viii, file lines 1007-1025): the catechumen becomes Martin's first witness, and the growth of Martin's reputation"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why Martin's reputation for power began with this one episode"
  - "participant asks what it meant to be a 'witness' to Martin's virtues in Sulpitius's own sense"
  - "Representative needs the exact wording behind 'powerful and truly apostolical'"
  prefer_instead:
  - "participant wants the raising itself, the prayer and the waiting - retrieve gallic.quote.martin-raises-the-catechumen"
  - "participant is asking whether the miracle 'really happened' - this record carries Tier 3 register and does not assess that"
  - "participant wants the whole episode told as a story - retrieve gallic.story.raising-of-the-catechumen, which this record is drawn from"
text: >-
  Thus being restored to life, and having immediately obtained baptism, he lived for many years
  afterwards; and he was the first who offered himself to us both as a subject that had experienced
  the virtues of Martin, and as a witness to their existence. ... From this time forward, the name of
  the sainted man became illustrious, so that, as being reckoned holy by all, he was also deemed
  powerful and truly apostolical.
speaker_or_author: "Sulpitius Severus, narrating"
license: verbatim
modern_lens_note: >-
  A modern reader may take "witness" here as a legal or evidentiary term - someone who can vouch that
  an event occurred. Sulpitius's own sense is closer to a living demonstration: the man does not just
  report what happened to him, he "offered himself... as a subject" of it, his continuing life the
  evidence. Martin's reputation, in this telling, grows outward from one restored life becoming visible
  proof, not from an argument made on Martin's behalf.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.story.raising-of-the-catechumen
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.figure.sulpitius
- type: associated-with
  target: gallic.quote.martin-raises-the-catechumen
---
Verified against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, same chapter div
`id="ii.ii.viii"` (line 971) as gallic.quote.martin-raises-the-catechumen. `grep -n "witness to their
existence"` returns one hit, line 1013; `grep -n "powerful and truly apostolical"` returns one hit,
line 1024-1025. Read lines 1007-1025 directly.

The ellipsis marks the omission of the catechumen's own report of the tribunal and the two angels
("The same man was wont to relate that... restored to his former life"), which is not part of either
flagged span for this record and is carried, with its own short quoted phrases, in the host record's
own untouched prose.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered within either quoted phrase.
