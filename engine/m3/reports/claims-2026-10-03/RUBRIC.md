# Claim-support rubric (v1, 2026-10-03)

You are grading replies written by the CiC engine's voice (Bedrock Sonnet 4.5) speaking as a Representative of a historical Christian tradition. You did not write them and must not rewrite them. Your only job: for every sentence, decide whether what it asserts is carried by the text of the records it cites.

Unit: each numbered sentence (S1, S2, ...). Read the full reply first for context, then each sentence with its cited records' full JSON. The record's own fields are the evidence (text, modern_rendering, tellable_as, definition/gloss, summary, notes, sources). Nothing outside the cited records counts, not even other records of the same world and not your own historical knowledge, even if the claim is true.

Labels (exactly one per sentence):
- `no_claim`: no specific factual or doctrinal content to check: greetings, transitions, invitations, hedges, statements about the Representative's own uncertainty or limits ("we cannot say", "the record is silent"), pure restatement of the question.
- `supported`: every specific claim in the sentence is stated or directly entailed by a cited record. Paraphrase and modern wording are fine. A quotation counts as supported when its words match the record's text or modern_rendering closely enough to be the same saying.
- `stretched`: the cited record carries the core of the sentence but the sentence adds a specific detail, a stronger degree, a cause, a date, a name or a generalisation that the record does not carry.
- `unsupported`: the sentence's main specific claim is not carried by any cited record (wrong record, record says something else, or record contradicts it).
- `uncited`: the sentence makes a specific claim and cites no record at all.

Rules: a sentence with several claims takes the worst applicable label among supported < stretched < unsupported. Judge against the records as given, not the world in general. When unsure between two labels, pick the less favourable and say why in the note.

Output: write a JSON file (path given in your task) of this shape, nothing else in it:
{"grader": "<your label>", "replies": [{"reply": "<world:probe_id>", "sentences": [{"s": 1, "label": "supported", "note": "<=25 words, required for stretched/unsupported/uncited>"}, ...]}]}
Every sentence of every reply you were given must appear exactly once.
