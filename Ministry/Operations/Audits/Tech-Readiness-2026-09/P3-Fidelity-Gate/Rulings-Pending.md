# Rulings Pending — Tech-Readiness Package 3 (Fidelity Gate)

Open questions the verbatim quote gate (`engine/m1/quote_verbatim.py`) has
surfaced and flagged, rather than resolved by guessing. Append-only; a
ruling moves the entry to `Decision-Log.md` with a strike-through note
here, it does not get deleted.

---

**Pending 1 — bare, unwrapped footnote digit or symbol (opened 2026-09-23,
PR #422; scoped to item 2, edition-level apparatus, 2026-09-23).** Six
records fail only because a source edition inserts a footnote/endnote
marker inline with no wrapper character of its own to distinguish it from
real quoted content:

- `cappadocian.quote.basil-on-common-life`: `"...in common 1 is more
  useful..."` (digit flanked by plain spaces)
- `cappadocian.quote.basil-on-work-and-prayer`: `"...everything.” ®
  But..."` (a footnote-glyph symbol)
- `hal.quote.hindered-by-jerome`: `"Paula,276 mother..."` (digit glued
  directly to a comma, no space)
- `ijc.quote.ammianus-sicininus-massacre`: `"...Christian church.1\n
  And..."` (digit glued directly to a period)
- `desert.quote.good-good-i-dont-mind`: `"...from work 163 and found..."`
  (digit flanked by plain spaces)

Unlike the pipe/bracket/tilde apparatus forms PR #422 handled, none of
these has a marker character that unambiguously distinguishes it from a
real number that might appear as actual quoted content elsewhere in the
same source file (e.g. "5000 monks" elsewhere in the Lausiac History). No
narrow, evidence-backed rule for telling the two apart was found as a
gate-level character pattern.

**Status: reframed, not resolved, by R33 (2026-09-23).** R33 ruled that
this gate's tolerances are set as principles at the gate, edition, or world
level — never a per-record field or per-quote instruction. Item 2 of the
registration brief takes a different approach than a global character
pattern: footnote-marker apparatus is treated as a property of the
*vendored edition* itself. A closed, named, evidenced list of marker
patterns per edition (stated with the real break each was taken from) lets
the gate apply a pattern to every quote from that edition and no other —
narrower than a fleet-wide rule, and grounded in what a specific edition's
own apparatus actually looks like rather than a guessed general shape. That
work is item 2's, not this entry's; this entry stays open until item 2's PR
lands and these six records are re-checked against it.
