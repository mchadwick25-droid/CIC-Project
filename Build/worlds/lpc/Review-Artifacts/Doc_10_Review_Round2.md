Simulated review — informational only, not an Article 31 substitute.

# Doc_10 Representative Construction (Datus): targeted recheck, round 2

- **World:** `lpc`, Latin Pastoral-Congregational Christianity, c. 246–430
- **Document:** `Build/worlds/lpc/lpc_Doc_10_Representative_Construction.md` and its companions, revision `2a4e2df6`, checked against round 1 (`Doc_10_Review_Round1.md`, at `e8b90693`)
- **Round:** 2
- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Reviewer agent:** Opus round-1/round-2 review subagent (isolated session, no drafting role)
- **Drafter agent:** lpc build thread, Sonnet revision pass and coordinator additions
- **Effort:** medium (targeted recheck of the round-1 findings and the diff `d517491b..2a4e2df6`)
- **Round count before this file:** `roundcount lpc 10 --check-new`: 1 file on record, PASS
- **Truncation check, method 1:** git object integrity at `2a4e2df6`. `git hash-object` equals `git rev-parse 2a4e2df6:<path>` for Doc_10 (80,980 bytes), the Permanent Prompt (24,407), the voice record (10,651) and the four demonstrations. The world_core record also matches after the restoration noted below.
- **Truncation check, method 2:** a content-terminal read and regeneration. Doc_10 ends on its "What follows this draft" line. `wb_lpc_s27.py`, run into a scratch directory, reproduces the voice record and the four demonstrations byte for byte. `wb_lpc_s21.py` reproduces the world_core record and all 207 source records with identical YAML content; only the serialization style differs, so no content drift.
- **Scope:** only what changed. The Decision 8B quote edits in the same diff range (commits `69dcfcfe` and `b740cf16`) belong to their own review and are not re-reviewed here. No model API was called.

**Reviewer's disclosure.** My `wb_lpc_s21.py` regeneration run wrote into the working tree as well as the scratch directory. It touched `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md` and five `records/lpc/source/` files. I restored all six with `git checkout --` at once. `git status` is clean apart from this review file, and nothing was committed. The semantic comparison above was made against the restored files.

## Mechanical checks

| Check | Result |
|---|---|
| `records lpc` | PASS |
| Voice-craft budget | 836 of 900. Doc_10 §2 and the record body both say 836, which is correct |
| FK / FRE, 10 compiled fields and 8 representative turns | FK 3.9–7.6, FRE 61.1–90.1. All within the ceiling and the floor |
| `source_anchor` = Prompt §2A; distress lines = Prompt Witness section | Identical; all 9 entries named verbatim |
| Leftover circumlocutions ("our first/later bishop", "one of your voices", "your later self") in Prompt, voice fields and demonstrations | None |
| Stray first person in voice fields and demonstrations | None. Only the sanctioned sentence and the anchor's quoted "a prayer for me" |
| Change-history phrases in Doc_10, demonstration bodies and the voice record | None |

## Source re-verification

- **"You will give the account to the Lord."** The source is *Ep.* LIV §14 (`anf05_hippolytus-cyprian-caius-novatian.xml`, lines 35009–35011): "a portion of the flock has been assigned to each individual pastor, which he is to rule and govern, having to give account of his doing to the Lord". The prompt line is faithful and adds nothing. Doc_10 §5 holds it at Documented and holds the joining with Sermon 88 at Inferential-Thin. That is correct.
- **The branch clause ("…loses its life, though the washing is not repeated for those baptized outside").** The source is Sermon 21 §32 (`npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml`, line 12932): "when they come to the Catholic Church… the washing of the flesh is not repeated in their case. For 'this form of godliness' was not wanting to them even when they were without; but there is added to them 'the Unity of the Spirit…,' which cannot be given but within." The clause meets the quote record's pairing guard. The font demonstration's new sentences ("…since the form was not missing even while they were outside. What is added when they come in is the unity of the Spirit, and that can be given only within.") follow the source closely.
- **The telos physician sentence.** Sermon 87 §3, as the quote record gives it. Doc_10 §5 now states the record's claim guard and holds the road-back reading at Inferential-Thin, as the build's own, with external review pointed at it. Labelled that way, it is acceptable in the provisional telos.
- **Caution 13 and the Prompt line.** They carry the 2026-10-25 ruling ("The pointer to `rzg` is given by Datus in his own voice") and D3's horizon statement. Both match each other, and caution 13's "does not answer… from later reception of Augustine" matches D3's own "answers only what Augustine's own text says". One wording overreach: see N1.
- **Caution 12.** The simulated-test sentence is gone, and the paragraph now says plainly that the point is untested.

## Round-1 findings

| ID | Round-1 sev | Status | Evidence at `2a4e2df6` |
|---|---|---|---|
| F1 | P1 | **Fixed** | The who-is-jesus turn 4 causal sentences are gone. The turn tells Sermon 87 §3 alone and ends on the passage. |
| F2 | P1 | **Fixed** | No closing question. The turn answers "Yes" and ends on Peter's three confessions. Only the compel demonstration now closes on a question back. |
| F3 | P1 | **Fixed** | "Went looking" is removed from the Prompt. §5 holds each element at its own level, says the reading as a whole is Inferential-Thin, and says no record carries the lost sheep. Leftover wording: see N4. |
| F4 | P1 | **Fixed (by ruling)** | The D3 misattribution is gone. Doc_10 §3, §6 and §7 cite D3 and the project lead's 2026-10-25 ruling. The pointer is now Datus's, in the Prompt and in caution 13. |
| F5 | P2 | Fixed | The guard and Prompt end at "…must clear", and Doc_10 §2 explains why. |
| F6 | P2 | **Fixed (by ruling)** | Plain names, as the 2026-10-25 ruling directs. Names are consistent across the Prompt, the demonstrations and Doc_10, and the "we" voice survives them ("In our later years the Donatists… stood in our own towns"; "We keep both answers"; "we cannot say from inside him"). The museum-guide paragraph now allows named people from the record and still keeps Datus off the list. |
| F7 | P2 | Fixed | The four sentences in which the voice announced how it would speak are gone. |
| F8 | P2 | Fixed | The font turn ends on the distance between the two answers. The tricolon, the door/Master aphorism and the "road with a door" line are gone. |
| F9 | P2 | Fixed | "Cyprian's answer stands as it was: nothing valid is given outside." |
| F10 | P2 | Fixed | Ep. X is told once. The G8 tension is audible ("The confessors held that their suffering gave them standing… Lucian's own letter still sent every case to the bishop"). New detail: see N3. |
| F11 | P2 | Fixed | The `divergence_note` now names the first turn, and turn 4 reads "plainly right". |
| F12 | P2 | Fixed | The count is 4/3/2. G8 is touched by the certificate but not carried in its own words. |
| F13 | P2 | Fixed | The branch clause is verified at source (above). |
| F14 | P2 | Fixed | 836 words, stated correctly in both places. The thin-topics sentence is corrected. |
| F15 | P2 | Fixed | File names are restored, no bare open-gap numbers remain, and the dates read correctly. |
| F16 | P2 | Fixed | Change history is gone from the demonstration bodies and Doc_10. |
| F17 | P2 | Fixed | "The flock that keeps its own" is removed. Augustine's stages are now in the third person. |
| F18 | P2 | Fixed | "Worked out in an ordinary life." |

## New findings

| ID | Sev | File : location | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| N1 | P2 | world_core caution 13; Permanent Prompt horizon paragraph | The pointer says `rzg` "speaks for those years". `rzg` speaks for the Reformed cities, Zurich and Geneva, 1519–1650. The fleet also has `witt` (Lutheran Wittenberg), which covers the same years. Neither D3 nor the 2026-10-25 ruling says `rzg` speaks for the Reformation as a whole. As written, the line overstates the scope the ruling gave and would mislead someone asking about a Lutheran reading of grace. | `records/worlds/rzg.yaml` (`display_name`, `time_window` 1519–1650); `records/worlds/witt.yaml`; D3 text. | Drop "which speaks for those years", or replace it with the world's own scope ("which speaks from inside those cities' own reform"). Change caution 13 (in `wb_lpc_s21.py`) and the Prompt together. |
| N2 | P2 | `lpc.demo.road-back-examined` turn 2 | "A certificate asking us to take in some man together with his own people, **he said**, opens a wide door." This gives Cyprian's own words ("opens a wide door") as his speech, with no placed quote. Now that names are plain, the fleet citation contract applies directly. A compiled exemplar teaches the form. | `_fleet.voice.fleet.md` `citation_contract`: "we write no words after a name and 'said', 'wrote', 'put it' or a colon: those are quotes too… What a person did or taught we tell in our own words, never as their words." | Tell it as what he did ("Cyprian warned the confessors that a certificate naming one man with his household would let in a crowd no one had examined"), or leave it to a placed quote. |
| N3 | P2 | `lpc.demo.road-back-examined` turn 2 | "Cyprian wrote to the confessors, **the men** who had suffered for the faith." No record gives the confessors' sex. Ep. X is addressed to "the martyrs and confessors". | `lpc.quote.such-a-one-with-his-friends`, its locus and text. | "…the confessors, those who had suffered for the faith." |
| N4 | P2 | Doc_10 §5, "What Was Rejected as Overlay", juridical bullet | The bullet still says "the telos must carry the shepherd who goes looking", which is the image F3 removed. | Doc_10 §5. | "…must carry the physician's recovery of the sick man, not the court", or similar. |

All four are small corrections of wording. None is substantial in the build-cycle sense, and none reopens a ruling.

**Note, not a finding (outside this diff's change).** Caution 12 still offers wording for the Facilitator's crisis redirect ("you are held, and this needs more than this conversation can give"). The crisis and dependency turns are template turns in code (`engine/m4/turn.py`, `safety_route_facilitator_events`; `stream_text=None`), so this caution cannot become a freely generated redirect on those routes. It is recorded so the safety owner knows the suggestion sits in a world record and not in the template.

## Items for the project lead

None. F4 and F6 were resolved by the project lead's 2026-10-25 rulings, and the revision applies both faithfully. N1 corrects wording inside that ruling; it does not change it.

## Open items to log

The build thread logs N1–N4 in `Open_Gaps_Tracking.md`, by subject and date, and closes them when applied.

## Verdict

**Approved to proceed.** All four P1 findings from round 1 are fixed, and the 14 P2 findings are fixed. The new findings are four P2 wording corrections. They do not call for substantial revision, so the build thread applies N1–N4 directly, mirroring each into its generator (`wb_lpc_s21.py` for N1, `wb_lpc_s27.py` for N2 and N3), with no third review file. No escalation category applies to this recheck.
