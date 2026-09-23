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

~~**Status: reframed, not resolved, by R33 (2026-09-23).**~~ **Resolved by
item 2's PR (2026-09-23) — see Decision-Log Entry 9.** Five of the six
records above now verify via a closed, named, per-edition apparatus list in
`cic/texts/REGISTRY.yaml`. The sixth, `cappadocian.quote.basil-on-common-
life`, has its own footnote-digit marker cleared by the same mechanism but
still does not verify — a separate, newly-discovered defect in the same
span. See Pending 2 below; this entry itself is closed.

---

**Pending 2 — cappadocian.quote.basil-on-common-life: compounding defects
beyond the footnote-digit marker (opened 2026-09-23, item 2's PR).** Once
`endnote-num-after-in-common` (Decision-Log Entry 9) clears the "in common
1 is more" digit, the record still fails. The same span
(`basil_ascetic-works-longer-shorter-rules_clarke1925.txt`) has at least
four more anomalies this PR does not touch:

- `"in many ways. 'To begin with"` — a stray curly opening single quote
  inserted before "To", with nothing corresponding in the record's own
  `text`. Not a punctuation-variant difference (nothing in the quote's own
  text needs to match a mark here at all) — a plain, uncaptioned addition.
- `"Tor just as the foot"` where the record's own `text` (and, by every
  ordinary reading, what Basil actually wrote) has "For" — a genuine
  single-character OCR misread in this DOCX-extracted scan, not a footnote
  marker of any kind.
- `"but D \n\nlacks others"` — a second stray bare capital letter, the same
  Migne column-continuation shape as `stray-column-letter-after-work-with`
  (Decision-Log Entry 9) but not yet confirmed against that convention or
  added as its own evidenced entry.
- `"unprocurable,?"` and `"as it is written,® in"` — two more bare
  footnote-glyph occurrences ("?" and a second "®") in the same span,
  beyond the two already handled in `cappadocian.quote.basil-on-work-and-
  prayer`.

The "Tor"/"For" defect in particular is a word-level corruption, not an
apparatus question — the kind of thing PR #413's own record-fix pass
(Entry 4) resolved by either restoring the word or lowering
`verification_state`, never by stretching the verbatim gate's own
tolerances to cover it. **Status: with Mark.** Options named, not decided
here: (a) restore "For" as a record content correction and add the
remaining three apparatus entries once each is independently confirmed
against this file's own real breaks, or (b) lower this record's
`verification_state` below `verified-direct`, the same as the OCR-damaged
residue Decision-Log Entry 5 (Rulings-Pending's own predecessor entry)
already tracks for `don.quote.donatus-quid-est-imperatori` and its two
neighbors.
