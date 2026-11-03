# Step 2: the harness fix, 2026-11-03

Four faults in the CP.9 re-test harness, and what now guards each. No model call, no spend.

| Fault in CP.9 | What changed | How it is checked |
|---|---|---|
| Helpers read only part of their ground (lpc: "directive and first ground record only") | Each voice request's prompt file and system files are measured against what one read returns whole (2000 lines, 2000 characters a line, 80000 bytes). | `engine/m3/shown_check.py voice --work DIR` fails any request with a file over a limit. The lpc prompt (94007 bytes over 616 lines) is caught by the byte limit; the compiled rzg and syr prompts have single lines over 2000 characters. |
| The prompt file a helper is given could lose records the request holds | The record ids in each request are compared with the ids in the prompt file written from it. | The same command fails any request with an id missing from its prompt file. This is a regression check on the prompt writer; it cannot catch a record the engine never put in the request. |
| Passages sat last in the offer (positions 12 to 14 of 13 to 15) | The offer takes records and passages in turn, each in its own rank order (`interleave` in `engine/m4/passage_offer.py`, used where the offer is assembled in `engine/m4/evidence.py`). | A test pins the order; the same command reports each passage's position in the offer. |
| Raters saw the first 170 words of a passage | The rater's item list is compared with the passage in the index. | `engine/m3/shown_check.py items --items ITEMS.json --db INDEX.sqlite` fails any item shorter than its passage. |

Limit. The check proves the helper's files hold what the engine offered and can be read whole. It cannot prove a helper read them. A helper that reports it read only part of its ground voids that run, as the CP.9 notes already treated it.

Run on the three alx requests of the stopped live sample: 3 voice requests, 0 failed, 12 records offered in q001, no file over either limit. That sample offered no passages, so the passage positions were not exercised on a real run; the unit tests exercise them.
