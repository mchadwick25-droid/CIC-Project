# Corrections to Specs 1 to 5, and the chunk map

The delivery lead read Specs 1 to 5 against the proposal, the Settled Items register and Decision-Log 69 to 71. Each chunk starts from its spec as corrected here.

| Chunk | Spec |
|---|---|
| D2 revert and voice rules | Spec 1 |
| D3 held-out set | Spec 5 |
| D4 offer assembler and diversity rule | Spec 2 with Spec 4, one pull request |
| D5 before-drafting test, design A | Spec 3 |
| D6 conformance removals | Spec 6 |
| D7 lens share | Spec 7 |
| D9 to D13 measurement | Spec 8 |

**Spec 1.** Model: Opus (it changes the instructions the voice drafts from). Add: the three-round figure line in `engine/m4/turn_prep.py` (`NO_NEW_FIGURE_LINE`) gives way where the visitor's question or the offered sources name the person (P8 as approved with the voice-rules correction, Decision-Log 69). Drop the handoff note for Library: only `engine/shape/records/fleet_voice/_fleet.voice.fleet.md` still carries "Strict we-voice"; the world records were corrected in #1464 and #1466. Add to "Done when": every touched file passes `tools/check_live_commentary.py --base origin/main --enforce`.

**Spec 2 and Spec 4.** One chunk. The diversity rule covers records and passages together and replaces the record-only source spread in `engine/m4/evidence.py` (Decision-Log 70). The caps are set, not put to Mark: at most 3 of the passages from one author and at most 2 from one work, relaxed when the lens holds too few authors or works; applied after ranking and before the budget. The deployment location of the index and vectors is not needed while the flag is off; it is raised when a live switch-on is proposed.

**Spec 3.** No change. The decision uses only the reader's sub-question, the record map and the existing fit step; it adds no model call.

**Spec 5.** The count per world rounds 20 + shelf tokens / 2 million to the nearest whole question: 360 in all, as Mark approved (lpc 44, ijc 39, cappadocian 35, alx 34, pahc 30, don 29, rzg 28, syr 27, desert 25, hal 24, witt 23, gallic 22). Rounding down gives 355; 360 stands. The overlap check also covers the 106 lpc questions, the CP.9 questions and the sealed probes; the sealed probes are compared by hash of normalized text only and never printed.
