# Uncited-claim source diagnostic (v1, 2026-10-03)

Each item is one sentence a CiC Representative (Bedrock Sonnet 4.5, speaking as a historical Christian tradition) said with no citation, which an earlier review judged to make a specific claim. You did not write it; do not rewrite it. Question: does anything the voice was given about its world carry this claim?

Evidence: the world's compiled prompt (path at the top of your file; read it in full first, it is what the voice saw) and, to confirm, the world's raw records under records/<world>/. Your own historical knowledge does not count, even when the claim is true.

Label each item with exactly one:
- `in_world`: a specific record (or prompt section) carries the claim; the voice just did not tag it. Give the record id (as written in the prompt's "cite as [[...]]" or the record file's id).
- `partly`: a record carries the core but the sentence adds a specific detail, degree, name, date or cause the world does not carry. Give the record id and name what is added.
- `outside`: nothing in the prompt or records carries the main claim; it comes from outside the world.
- `framing`: on reflection the sentence makes no checkable specific claim (transition, restatement of an earlier cited sentence, honest limit).

When unsure between two labels, choose the less favourable (outside < partly < in_world) and say why.

Output: a JSON file (path in your task), nothing else in it:
{"world": "<world>", "items": [{"id": "U01", "label": "in_world", "record_id": "hal.story.x or null", "note": "<=25 words"}, ...]}
Every item in your file must appear exactly once.
