Simulated review — informational only, not an Article 31 substitute.
Review round 2 (targeted recheck), cappadocian record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Round: 2
Reviewer model: Opus
Reviewer agent: independent subagent, fresh context, read-only, not the round 1 reviewer
Drafter model: Opus
Drafter agent: the session's own Opus thread made the record edits; this reviewer did not draft them
Truncation check, method 1: the file ends on the "Files:" list, whose last line names engine/m9/enforce.py
Truncation check, method 2: the body below this header is 6006 characters, the same length as the reviewer's returned message, counted separately before saving
Scope: commit ca5ddb1, the four blocking items of round 1 and the non-blocking fixes applied with them.

Round-2 verdict: **not cleared.** Two of the four blocking items are still blocking (1 and 4); 2 and 3 are cleared. Everything else in the diff is clean, and every changed field passes readability.

## Blocking items

**1. `dw.not-a-death-wish`: STILL BLOCKING.**
- **The text drops Sozomen's hedge.** Sozomen V.11 (npnf202 ~36054) says: "*I believe* that Eupsychius was condemned in consequence of the demolition of the temple of Fortune… all the actors in this transaction were condemned." The record says "A later church writer **says** he was condemned for helping to pull down…". That turns Sozomen's opinion into a report. "Helping to pull down" is a fair reading of "all the actors… were condemned", but the "says" needs to become "believed", or similar.
- **The round-1 claim is still in the record's metadata.** The source line for the Eupsychius figure still reads "executed under Julian for refusing to deny the faith". The usage note still describes the record as "citing the Forty of Sebaste and Eupsychius" for refusing to deny. The second position still says martyrdom was "consistently framed as refusal under threat", and Eupsychius's own case is no longer an example of that. The figure record supports none of this, and it carries no narrative of how he died.
- **The new temple claim has no source entry.** Sozomen is not cited in `sources`. The figure record's bridge line ("A later church historian tells it.") does give precedent for voicing Sozomen.
- **Closing sentence:** on its own text it now reads as a general statement, not as a claim about Eupsychius. But with the metadata above still pairing him with "refusing to deny", it will be read as covering him. It reads cleanly once the metadata is fixed. Optionally, tie the closing back to the Forty.

**2. `term.panegyris`: CLEARED.**
- Longer Rule 39 (~17525–40) has the brothers carrying their goods to "functions designated fairs" (Clarke's note: πανηγύρεσι). That supports "Buying and selling went on there too."
- Longer Rule 40 (~17550): "buying and selling conducted at martyrs' tombs is not fitting for us". That supports "Basil's rule told the brothers not to trade at the martyrs' tombs."
- The quick meaning ("vigil, preaching, and a market") now agrees with the record's usage note.

**3. `dw.psalms-teach-the-singer`: CLEARED (text only).**
- "We cannot give you our teachers' answer…" sets a limit on what the record can give. It does not claim no answer exists.
- **Residual defect in the same record:** the `tensions` field still says "we have no record of this world's own reaction to the violence in scripture". The usage note's not-for line says the record "lacks" it. Both make the stronger claim that the text fix removed. That claim is doubtful in substance: Gregory of Nyssa's *Life of Moses* (II.91–92, on the Egyptian firstborn) is an in-world answer, though it isn't vendored. Both fields should be bounded the same way as the text.

**4. `dw.catholic-and-its-rivals`: STILL BLOCKING (judgment call).**
- The removed sentence is gone.
- The remaining sentence is the same kind of claim in more scholarly words: "The teachers who formed us became curriculum, liturgy, and law for the traditions that trace themselves back through the councils." It is the world, in its own voice, describing its reception after 394. The horizon gate can't catch it only because it names no date or event.
- That the sentence predates the audit is not a defense. Live records don't get grandfathered.
- The fleet precedent for cell F3-T, `alx.dw.one-church`, answers the same question from inside its window: "Whether any present-day church is 'our church' reaches past what we can see. We speak from before the splits that made today's map, and we say so." A bounded sentence like that would serve the cell without breaking the horizon.
- The third `positions` entry repeats the reception claim.
- **Waiver count matches:** the horizon gate returns **4** findings. They are `core.living_traditions` (Speyer 1529), `not-later-formulas` text and positions (Lateran IV), and `canonization-sieve` (398). The waiver for the horizon gate on cappadocian in `engine/m9/enforce.py:188` is set to 4, so it matches.

## Non-blocking fixes
I found no new errors in these:
- **`was-jesus-god`:** the second doxology form, "through the Son, in the Spirit", is accurate to Basil's *On the Holy Spirit* 1.3.
- **`marriage-ending`:**
  - "could take another wife and be pardoned" fits npnf208 ~35221: "the man who has been abandoned is pardonable, and the woman who lives with such a man is not condemned."
  - "(some said two)" matches the canon on second marriage.
- **`no-stones-to-show`:** the switch to "Basil's mother, Emmelia" is correct. *Life of Macrina* names Emmelia and places the parents' bodies at the shrine of the martyrs. "Is said to" keeps the hedge.
- **The rest** (doxologia, mysterion, woman-authority, akatalepsia, not-later-formulas, doubt-and-unfinished-growth, never-settled) are clean.

**Readability:** every changed field passes. Scores ranged from grade 4.5 to 8.8 (limit 10) and reading ease 64.7 to 83.4 (minimum 60).

## New defects
- The leftover metadata in `not-a-death-wish`: the source line, the usage note, the "consistently" position, and the missing Sozomen source entry.
- The `tensions` field and usage-note overclaim in `psalms-teach-the-singer`.

## Verdict
Not cleared. Items 2 and 3 are cleared (3 needs its metadata aligned). Items 1 and 4 are still blocking: fix the hedge and metadata in `not-a-death-wish`, and replace the reception sentence and matching position in `catholic-and-its-rivals` with a bounded alx-style line.

Files:
- /home/user/CIC-Project/records/cappadocian/doctrinal_witness/cappadocian.dw.not-a-death-wish.md
- /home/user/CIC-Project/records/cappadocian/doctrinal_witness/cappadocian.dw.catholic-and-its-rivals.md
- /home/user/CIC-Project/records/cappadocian/doctrinal_witness/cappadocian.dw.psalms-teach-the-singer.md
- /home/user/CIC-Project/engine/m9/enforce.py
