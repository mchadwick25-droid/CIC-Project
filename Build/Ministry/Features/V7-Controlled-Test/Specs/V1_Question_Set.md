# V1: the question set, frozen

**Owner:** question thread, a fresh Opus session. It never sees B's code or any reading card. **Model:** Opus writes the questions; code freezes them.

**Purpose.** 120 visitor questions (40 each for alx, pahc and syr) covering Mark's nine hard cases, as `../Test_Plan.md` §4 lays out. Each authored question has a trap note.

**Outputs.** In `../Set/`:
- `<world>_questions.yaml`, with these fields: id, text, case (1–9 or ordinary), origin (d3 or authored).
- `<world>_trap_notes.yaml`, with these fields: id; what a faithful answer must not do; the source and lines that show it.
- `SHA256SUMS`, covering both files for every world.
- `draw.json`: the seed for the D3 draw, written before the draw.

**Process.**
1. A helper that has seen no answers labels the D3 questions for alx, pahc and syr with the case each fits.
2. Code draws the needed counts with the seed.
3. The question thread writes the rest. It reads the world's shelf list, construction documents (Doc_01–Doc_09) and contested-claim records to find real traps, and words each question as a visitor would.
4. A trap the thread cannot tie to named lines is dropped. It is never invented.

**May touch.** `../Set/` only. **Must not touch.** Records, the D3 files, sealed probes, the engine.

**Tests written first.**
1. The count is 40 per world, with 4 for each hard case and 4 ordinary.
2. Every authored question has a trap note that names a source and lines.
3. No question overlaps a sealed probe, a sub-question wording, a CP.9 question or the 106 lpc questions beyond the D3 overlap limit. Sealed probes are compared by the hash of their normalized text only and never printed.
4. `SHA256SUMS` matches the files.

**Done when.** The tests pass, the set is frozen, and the V7 lead has the hashes. From then on, any change is a change order.

**Cost.** None metered.
