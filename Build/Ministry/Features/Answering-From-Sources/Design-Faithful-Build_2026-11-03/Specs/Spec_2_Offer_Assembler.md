# Spec 2: the offer assembler (search wired into the offer)

**Model: Opus.** This is core code: it decides what the voice is allowed to say from. A mistake here is a fidelity failure, not a style one.

**Purpose.** Replace the seed-only passage source with live search inside the world's lens, so the offer can hold any passage on the shelf, not only reviewed seeds. Seeds and records only help rank and route.

**Inputs.** The visitor's own words; the world; the world's built index and vectors (`Sandbox/answering-library/search`); the sub-question's reviewed seeds (rank help); the offer budget (6 passages, 1,800 words).

**Outputs.** A list of offer passages in the shape `engine/m4/passage_offer.py` already uses (tag, passage_id, text, work, author_name, voiceable flag, locus, role, date), in rank order, each cited as "[author], in [work], writes", never "we". Voiceable or outside-the-voice is set by the rules in `engine/m4/reports/passage_offer_build.py` (seed says voiceable, row role own/tradition, speaker known, window inside); a searched passage with no seed is outside the voice.

**Shape.** One function in `passage_offer.py`, `search_passages(world, query, seeds, budget)`, called only from the `offer_contents` seam. Keyword and meaning rank inside the lens, fused, reranked (as in `search/engine.py`); a seed outranks a searched passage of equal score; a passage with no named author or work is never offered; the budget is applied last.

**May touch.** `engine/m4/passage_offer.py`, `engine/m4/turn_prep.py` (the one call), tests, and a new loader for the vectors under `Sandbox/answering-library/search/`.
**Must not touch.** `Sandbox/answering-library/index/` (hashed); the gate on the offer (not decided); the directive text; records.

**Paths are parameters.** The built index, the vectors and the corpus-map rows are passed in; the assembler hardcodes no location. Where they live in a deployment is an open item for Mark (see the README).

**Test written first.**
- Two-world test through the assembler: a query that matches a passage only on world B's shelf yields no passages for world A.
- A reviewed seed and a searched passage at equal score: the seed comes first.
- The budget: never more than 6 passages or 1,800 words; a passage with no author or work is dropped.
- Every offered passage carries the voiceable flag and a citation label; no passage outside the lens appears.
- The flag-off path returns exactly what the offer returns today.

**Done when.** The tests pass, flag off changes nothing in an existing offer (byte-equal on the Passage-Offer-Smoke fixtures), and the part runs with no model call. **Cost:** none.
