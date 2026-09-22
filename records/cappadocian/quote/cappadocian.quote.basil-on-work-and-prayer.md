---
id: cappadocian.quote.basil-on-work-and-prayer
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: cappadocian.source.basil-asketikon-longer-shorter-rules
  locus: "The Longer Rules (Regulae Fusius Tractatae), Rule/Question XXXVII (\"Whether
    We Must Neglect Work for the Sake of the Prayers and Psalmody, and What Times
    Are Suitable for Prayer, and First of All Whether We Should Work at All\"), p.
    206 (basil_ascetic-works-longer-shorter-rules_clarke1925.txt)"
  license: public-domain
text: >-
  Now since some get off work under pretext of prayers and psalmody, you
  must know that for each separate task there is a special time, as
  Ecclesiastes says: "' There is a time for everything." But for prayer and
  psalmody, as for many other things, every time is suitable; so that we
  praise God with psalms and hymns and spiritual songs while we move our
  hands in work with the tongue if it is possible, and conducive to the
  edification of the faith,—but if not, then in the heart, giving thanks
  to Him Who gave both strength of hand to work and wisdom of brain to
  know how to work, and also bestowed means by which to work both in the
  tools we use and the arts we practise, whatever the work be. We pray
  moreover that the works of our hands may be directed towards the mark
  of pleasing God.
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  A modern reader may assume manual labor and prayer were rivals for the
  same hours - either the hands are working or the lips are praying, and
  a busy workday must have crowded devotion out. Basil's own answer here
  refuses that split: psalms are sung aloud while the hands keep working,
  when the task allows it without distracting anyone else's attention
  from the faith, and silently in the heart when it does not. The work
  itself is not a break from prayer or a lesser interval between real
  devotions - it is named alongside the tools used and the trade
  practised as itself something to give thanks for and to aim at
  pleasing God, the same "hands busy both ways" this world's own account
  of an ordinary day already claims of it.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what an ordinary workday actually looked like, hour by hour, among this world's ascetics"
  - "participant asks whether manual labor and prayer competed with each other or how the two actually fit together"
relations:
- type: associated-with
  target: cappadocian.dw.ordinary-day
modern_rendering: >-
  Some of you try to get out of work by claiming prayer or
  psalm-singing needs the time instead. But understand: every task has
  its own proper hour, just as Ecclesiastes says, "There is a time for
  everything." Prayer and psalm-singing are different. Any hour at all
  will do for those.


  So we can praise God with psalms, hymns, and spiritual songs while
  our hands stay busy at work. Aloud, if the task allows it, and it
  won't pull anyone else's mind off the faith. Silently in the heart,
  if it won't. Either way, we give thanks to the God who gave us the
  strength to work with our hands, and the sense to know how. He also
  supplied the tools we use and the trade we practice, whatever that
  work may be. And we pray, too, that what our hands make will be
  aimed at pleasing him.
---
Verified verbatim 2026-09-02 directly against the vendored
basil_ascetic-works-longer-shorter-rules_clarke1925.txt, Longer Rules,
Rule/Question XXXVII ("Whether We Must Neglect Work for the Sake of the
Prayers and Psalmody..."), lines 17072-17096 (grep -n -i "get off work
under pretext" and grep -n "the mark of pleasing God" both confirm the
span; the page header "206 THE ASCETIC WORKS OF ST. BASIL" at line 17026
and the next header "THE LONGER RULES 207" at line 17118 bracket the
whole excerpt on p. 206). This is a scanned/OCR'd edition: two
superscript footnote-marker artifacts ("everything.\"®" and "other
things, »") and two stray mid-line marginal column-locators ("E" before
"the tongue" and "383A" before "how to work") were dropped as print
apparatus, not text; the line-end hyphenation "every-\nthing" was
rejoined as "everything". No wording was added, dropped, or reordered;
the source's own em dash ("faith,—but") is kept as printed.

Quote-verbatim gate fix (2026-09-22, supersedes the 2026-09-02
"normalized to a single straight double quote" call above): the source's
opening "“‘" before "There is a time for everything" is a genuine nested
quotation mark, not print noise - Basil is quoting Ecclesiastes 3:1
inside his own reported speech, exactly the construction a nested mark
exists to punctuate. Per Mark's ruling that a nested mark must be
corrected to match the source, not normalized away, restored as a
straight apostrophe after the opening straight double-quote ('"' '
There...'). The record still cannot verify past this point: the source
also carries the "®" footnote-marker artifact directly between
"everything.\"" and "But" (no whitespace-only gap can skip a literal
character), which is the same footnote/column-apparatus gate gap named
above, not a content problem in the record - flagged for Mark alongside
cappadocian.quote.basil-on-common-life and
cappadocian.quote.gregory-nyssa-on-becoming-god (same root cause, this
vendored edition's own footnote/column-letter apparatus).

Chosen for F5-I specifically because this is Basil's own reasoning for
why manual labor and fixed prayer do not compete for the same hours in
an ordinary day - the rule's own answer is that psalmody rides alongside
the hands rather than waiting for a gap between tasks - which is exactly
the practical rhythm cappadocian.dw.ordinary-day states in its own
words ("Work followed - training for the soul as much as support for
the house, our own rule called it, hands busy both ways"). This is
deliberately about the shape of an ordinary working day, not about
communal life itself: it says nothing about goods held in common,
obedience to a leader, or hospitality at the door, which is the separate
ground cappadocian.quote.basil-on-common-life already covers (Longer
Rule VII, F4-I) from the same Asketikon, so the two records draw on the
same book without overlapping in what they actually witness to.

MODERN RENDERING AUTHORED (2026-09-02, matching this build's own
standing quote discipline: the spoken form is a modern-English
translation, never the archaic original; the original stays as the
record's own text field, shown at Level 3).
