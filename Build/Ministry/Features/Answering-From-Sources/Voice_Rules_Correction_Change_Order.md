# Voice Rules Correction: change order (2026-11-03)

Named change order, Decision-Log entry 69. It restores four voice rules to what Mark ruled and brings each world's records and phase documents back to them. Engine makes the one shared-rule change (the fleet voice record); this order covers the records and the phase documents only. The proposal page is the Artifact "Voice Rules Correction"; Mark's answer was "follow all your recommendations" (relayed 2026-11-03).

## The four rules, as restored

A. **"We" is for the tradition's perspective.** The voice says "we" when it gives the tradition's own perspective, where it is not a person. In the present conversation it says "I". "Never explain the we" is removed, and so is Donatist-world Fidelis's ban on "I think". Asked why it says "we", the voice answers plainly. The identity line ("I am a representative of ...") stays at most once per turn.

B. **Names.** Datus names any person, see, council, community, city or other name that the sources contain. The Representative does not claim to be the bishop, or any person, in its answers.

C. **Absence.** The voice does not volunteer what is missing. Asked about something the world does not hold, it says so plainly in the world's own words, and adds nothing that does not bear on the question and no filler. (Settled Items Register row 13 already holds the first half.)

D. **Answer the question as asked.** The first sentence answers it. The world's lens shapes how it answers, not what. A source may be applied to the visitor's situation when a reviewed record frames that use (Decision-Log 30). No voice speaks for any church after 430.

## What changed

| Rule | File | Change |
|---|---|---|
| A | `records/{alx,cappadocian,desert,don,gallic,hal,ijc,pahc,rzg,syr,witt}/voice_craft` | The `self-reference` flavor note says "we" for the tradition's perspective, "I" in the conversation, names people and places the sources name, keeps the identity line and the placed-quote citation rule. The "strict we-voice" phrases in the identity text of alx, cappadocian, gallic, hal and ijc follow. gallic loses the rationale paragraph for the zero-"I" rule and the "we is never defended" sentence. |
| A | `Build/worlds/{lpc,cappadocian,don,gallic,ijc,rzg,syr,witt}` Permanent Prompts | The "one more disguise" paragraph (do not explain "we") is replaced by a short plain-answer paragraph. |
| A | `records/lpc/world_core`, caution 15 | Now says the voice answers a question about "we" plainly. |
| A | don Permanent Prompt | The ban on "I think" is replaced by the A rule. |
| B | `Build/worlds/lpc/lpc_Voice_Configuration_Datus.md` | Scope note replaced; the false "zero occurrences" claim and the withdrawn label "Bishop of the Kept Flock" are removed; the register note drops the excluded-name sentence. |
| B | `records/lpc/voice_craft/lpc.craft.datus-voice.md` | The source-anchor fallback names the Scillitan martyrs and Perpetua, Tertullian and the Donatists. The explanatory paragraph follows. |
| B | lpc Phase 3 | The self-identification paragraph says "I" in the conversation and that the voice names what the sources name. |
| C | lpc Permanent Prompt (two passages), Phase 2, Phase 3 example, Phase 4, Doc_10 section 2; don and gallic Permanent Prompts | The gap is not volunteered; asked, it is stated plainly. |
| D | lpc Permanent Prompt (two passages), Phase 4, Doc_10 section 2 | The first sentence answers the question as asked. `records/lpc/world_core` caution 16 keeps its second sentence and drops the "listener's own day" clause. |

Ten world packages are rebuilt and repinned by this order.

## Not in this order

- The fleet voice record (`engine/shape/records/fleet_voice/_fleet.voice.fleet.md` line 33), the answer-path rules in `engine/m4/turn_prep.py`, and the length wording at `turn_prep.py:222` (Engine's).
- Succinctness without a cutoff length replaces any word-range wording in the phase documents. A search of the Representative phase documents, Permanent Prompts and voice_craft records found no word or sentence range in them; the ranges the Artifact lists (P5, P7, P9) sit in the engine files and the Writing Standard.
- The 11 worlds not named above, and the rest of the Permanent Prompts, keep their text.
