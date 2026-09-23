# Rulings Pending — Tech-Readiness Package 3 (Fidelity Gate)

Open questions the verbatim quote gate (`engine/m1/quote_verbatim.py`) has
surfaced and flagged, rather than resolved by guessing. Append-only; a
ruling moves the entry to `Decision-Log.md` with a strike-through note
here, it does not get deleted.

---

**Pending 1 — bare, unwrapped footnote digit or symbol (opened 2026-09-23,
PR #422).** Six records fail only because a source edition inserts a
footnote/endnote marker inline with no wrapper character of its own to
distinguish it from real quoted content:

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
narrow, evidence-backed rule for telling the two apart was found. Two
paths named in the registration brief: (a) a narrow rule for this shape, if
one can be found, or (b) `verification_state` downgraded on these six
records (a record edit, reserved like every other record-fix decision).
**Status: with Mark.** Gate registration in `gates.GATES` is blocked on
this — registering now would go red on all six, since they remain
`verified-direct`.
