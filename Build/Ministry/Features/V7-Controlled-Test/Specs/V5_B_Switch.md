# V5: B behind a switch

**Owner:** engine thread. **Model:** Opus. This is core code on the turn path, and it sits behind a switch that is off.

**Purpose.** Build B exactly as `../Test_Plan.md` §2 defines it.

**Design.**
- **The switch.** A frame flag, `reading_context`. No world record sets it, and the compiler never writes it. Only V2's `--arm b` sets it in memory.
- **When it is on, `engine/m4/evidence.py` `render_evidence_block`:**
  - adds each offered quote's reviewed modern rendering to its line;
  - adds "Reads differently today" from the lens note, or from the card's `reads_differently_today` where there is a card;
  - adds the card's lines under the record, where there is a card;
  - adds the `fit_step.context_blocks` window for the top two offered quotes or stories.
- **Budget.** Additions stop at 12,000 characters. Context windows are dropped first, then card lines, and the quote renderings are kept.
- **Directive.** When the flag is on, `engine/m4/turn_prep.py` adds these lines:
  > Answer what the visitor asked, first and plainly.
  > Draw the offered sources and our ground together: connect them, explain how belief and practice fit, and say what we understand them to mean.
  > Keep apart what a source says, what we understand it to mean, and what was disputed or uncertain, in plain words.
  > Say whose view a source gives, and how widely it was shared, only as far as its card or record says.
  > Read the surrounding text to understand a passage; cite the record, not the text around it.
- **Report-only signal.** A whole-world sentence whose only cited record has a single-author `whose_view` is counted in the turn's report. Nothing is withheld for it.
- **Unchanged.** Selection, the net, placement and every gate.

**May touch.** `engine/m4/evidence.py` (rendering only), `engine/m4/turn_prep.py` (the flag-gated lines), a report counter, tests. **Must not touch.** Evidence selection, `grounding_net.py`, placement, `render.yaml`, any world record's flags.

**Tests written first.**
1. With the flag off, the evidence block and directive are byte-equal to today's for every question in the frozen set's alx file, run in dry mode.
2. With the flag on, the offered record ids equal those with the flag off.
3. With the flag on, additions never exceed 12,000 characters. Context windows are dropped first.
4. A quote with no card still shows its rendering and lens note.
5. Context ids cannot be cited: a sentence tagged with one is treated as today.
6. The signal counts a fixture "we held" sentence bound only to a single-author card, and withholds nothing.

**Done when.** The tests pass, the full engine suite passes, and `live` is untouched.

**Cost.** None.
