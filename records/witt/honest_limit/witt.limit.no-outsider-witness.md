---
id: witt.limit.no-outsider-witness
world_id: lutheran-wittenberg-and-its-congregations
record_type: honest_limit
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-E
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Documented
  divergence_note: >-
    Documented that this world's own vendored library engages no genuinely independent outsider witness
    (the Roman Confutation reaches it only at one remove, quoted and answered inside the Apology) and that
    the cell's earlier two sub-questions (catacombs, Constantine corrupting the church) name events outside
    this world's own 1517-1580 window entirely -- a boundary fact, not a contested reading.
sources:
- source_id: witt.source.melanchthon-apology-of-the-augsburg-confession
  locus: "our own Apology's own quotation of and answer to Rome's reply -- the nearest thing to an outside voice this library holds, and even that reaches us only at one remove; the Confutation itself is never independently vendored, never held here in its own words directly"
  license: public-domain
- source_id: witt.core.witt
  locus: "time_window: 1517-1580 -- our own declared span, centuries after both the catacomb era and Constantine's own reign"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Christians were really hiding in the catacombs"
  - "participant asks whether Constantine corrupted the church, or whether empire changed what we were"
  - "participant asks what an outsider would have found strangest about us"
  - "participant asks what our neighbours said about us, or what we were accused of"
  prefer_instead:
  - "participant wants our own confessional self-definition of the Church -- retrieve witt.dw.one-holy-church-forever instead, which states our own position rather than an outsider's view of us"
statement: >-
  Were we really hiding in the catacombs? That question belongs to a
  much earlier age of the Church, more than a thousand years before our
  own founder was born. It is not ours to answer from inside; nothing in
  our own record touches it.

  Did Constantine corrupt the church -- did the empire change what we
  were? That question, too, names an era centuries before our own floor
  in 1517. We can tell you that our own confession argued we had kept
  the ancient Church's own custom rather than corrupted it, but we
  cannot speak to Constantine's own reign as though we had lived through
  it or watched it happen.

  What would an outsider have found strangest about us? What did our
  neighbours say about us, what were we accused of? Here we must be
  honest about a real gap, not a distant era. No outsider's own
  independent account survives in our own library at all. The nearest
  thing we hold is Rome's own reply to our confession -- and even that
  reaches us only at one remove, quoted and argued against inside our
  own writing, never held here in its own words. We cannot give you an
  outsider's own eyes on us, because our library does not hold a pair.
why_sources_cannot_answer: >-
  This world's own declared time window is 1517-1580 (witt.core.witt); the catacombs and Constantine's own
  reign both belong to an era many centuries earlier, outside anything this library's vendored texts
  narrate or claim to narrate -- a boundary fact about scope, not a finding of silence within the window
  itself. For the cell's other two questions (an outsider's strangest impression; neighbours' own
  accusations), the gap is different in kind: it falls squarely inside this world's own window, and no
  outsider witness -- Catholic, Reformed, or otherwise -- is independently vendored anywhere in this
  library. The one candidate that comes closest, the Roman Confutation of the Augsburg Confession (Eck,
  Faber, Wimpina, and Cochlaeus, read before the Emperor 3 August 1530), is itself unvendored; it reaches
  this library only as quoted and answered inside Melanchthon's own Apology, "available only at one
  remove" (witt.source.roman-confutation-of-the-augsburg-confession's own disposition note). Answering this
  cell's second half from that source would mean speaking Rome's own accusations in Rome's own voice using
  only our own side's paraphrase of them -- exactly the kind of manufactured outsider testimony this
  world's own guard warns against.
nearest_material:
- witt.source.roman-confutation-of-the-augsburg-confession
- witt.source.melanchthon-apology-of-the-augsburg-confession
- witt.dw.one-holy-church-forever
- witt.dw.true-priests-of-gods-own-making
relations: []
---
Closes F3-E at the Answer-the-Canon step (inserted between B-7a and B-8), matching witt.voice.craft's own
B-7 decline of this exact cell's F3-E-03/F3-E-04 sub-questions ("No outsider witness survives among this
world's built story or figure records at the time of this authoring pass. Declined rather than forced.")
-- this record is that same finding's own honest_limit treatment, independently confirmed rather than
merely carried forward on the earlier authoring pass's word alone: witt.source.roman-confutation-of-the-
augsburg-confession's own record (already existing, verified-direct) was re-read directly for this pass
and confirms its own "(context)... available only at one remove" disposition; no other candidate source
record anywhere in records/witt/source/ was found, by a direct listing of that directory at this authoring
pass, to hold an independent outsider account.

The cell's first two sub-questions (catacombs, Constantine) are answered by a different, simpler route:
they name events outside this world's own declared 1517-1580 window entirely, stated as a boundary fact
per witt.core.witt's own time_window field, not re-argued as though this world's library might plausibly
have engaged them. This is the same declined class witt.dw.a-confession-answered-not-a-vote (F1-E) names
for its own out-of-window sub-question ("a council voted Jesus into being God"): received or inherited
history, not this world's own to narrate from inside.
