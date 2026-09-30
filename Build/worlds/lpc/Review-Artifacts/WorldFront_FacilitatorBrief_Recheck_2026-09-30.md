Simulated review — informational only, not an Article 31 substitute.

# lpc B-7a: round-2 targeted recheck of the world_front and facilitator_brief records

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Drafter note:** revision commit 57326232c ("revise world_front and facilitator_brief after the round-1 review ... log OG-63") carries the Sonnet 5.5 trailer.
- **Reviewer agent:** independent Opus recheck subagent (fresh context, medium effort; did not draft or revise either record)
- **Drafter agent:** B-7a revision session (commit 57326232c)
- **Round:** 2
- **Truncation check, method 1:** line count and closing marker: `wc -l` on this file returns 127 lines, and `tail -n 1` returns "End of recheck.", both run after the last edit.
- **Truncation check, method 2:** set comparison: every finding id in the "Verdicts by finding" table (B1, S1 to S11, O1 to O14, N1 to N4) also appears as a bold lead in the "Notes on findings" section or is marked "no note needed" in the table; checked by reading the table against the notes, id by id.
- **Scope:** only what changed in `git diff HEAD~1 -- records/lpc/world_front records/lpc/facilitator_brief`, checked against the round-1 findings in `WorldFront_FacilitatorBrief_Review_2026-09-30.md`. Both working files hash identical to HEAD (front 994365b84, brief ecc78b883). Nothing in `records/` was edited.
- **Also done:** status set for the two UNVERIFIED rows of `lpc_Claims_Register.md` (`47bbbca6`, `e92de79f`); no other row edited.
- **Cap:** round 2 of 3 for these two records.

## Verdict

**Not yet approved to proceed. Every round-1 finding is resolved. One new substantial finding (N1), three optional.**

The revision applied the round-1 wording faithfully, and each fix holds against its source. N1 is a single sentence the revision added to `formation_limitations[0]` from the round-1 review's own optional proposal (O13). On a closer read it states a cause of survival that no record gives, and it cuts against the world's own preaching record. The fix is one sentence, worded below. A round-3 check would then be N1 only.

## Gates run

| Gate | Result |
|---|---|
| `python -m engine.m10.cli regate lpc` | PASS. 269 public fields checked; no hard failure in either record. |
| Per-field grade, all 69 prose fields in the two records (`engine.m1.gates.grade_text`) | All clear FK 10 and FRE 60. Fragile: brief `cautions[6]` FRE 60.39, brief `world_identity` 60.17 (was 60.57 before the O8 edit), front `voices[3].text` 60.40 (unchanged). |
| `python -m engine.m10.cli citations` on both files | PASS (the three partner-world ids resolve). |
| `python -m engine.m10.cli claims lpc` | PASS: 110 derived, 110 registered, 0 UNVERIFIED after this recheck. |
| `python -m engine.m10.cli records lpc` | PASS |
| `python -m engine.m10.cli reviewfile` on this file | PASS |

## Verdicts by finding

| Id | Round-1 severity | Verdict | Note |
|---|---|---|---|
| B1 | blocking | resolved | see notes |
| S1 | substantial | resolved | see notes |
| S2 | substantial | resolved | see notes |
| S3 | substantial | resolved | no note needed: applied as worded; "ordinary believer" matches claims row `8f060a71`'s reading |
| S4 | substantial | resolved | no note needed: count removed; "by far the most frequent key word" matches the gravity's "by a wide margin, the single highest" |
| S5 | substantial | resolved | see notes |
| S6 | substantial | resolved | see notes |
| S7 | substantial | resolved | see notes |
| S8 | substantial | resolved | see notes (grounding gap is N2) |
| S9 | substantial | resolved | no note needed: "By his own later account" restored |
| S10 | substantial | resolved | see notes |
| S11 | substantial | resolved | see notes |
| O1 | optional | resolved in part | no note needed: all flagged phrases fixed except the `story[2]` split, left by choice (optional) |
| O2 | optional | resolved | no note needed: title now "Love for Enemies in a Time of Plague" |
| O3 | optional | resolved | no note needed: "a few years later" fits the force's c. 249 to 262 and the death in 258 |
| O4 | optional | resolved | no note needed: folded into S11 |
| O5 | optional | resolved | no note needed: `records/worlds/don.yaml` window is 311 to 439 |
| O6 | optional | resolved | see notes and N4 |
| O7 | optional | resolved | no note needed: "the Facilitator's own voice steps in" |
| O8 | optional | resolved | no note needed; FRE fell to 60.17 (still passes) |
| O9 | optional | resolved | no note needed: F4-I now cites `lpc.force.recurring-contest-failed-member` |
| O10 | optional (flag) | carried to record owner | no note needed: logged in OG-63 |
| O11 | optional | no action, correctly | no note needed |
| O12 | optional (engine) | carried to engine owner | no note needed: logged in OG-63 |
| O13 | optional | applied, but see N1 | see N1 |
| O14 | optional | resolved | no note needed: "week after week" |
| N1 | new, substantial | open | brief `formation_limitations[0]`: unsupported cause of survival |
| N2 | new, optional | open | brief `formation_strengths[1]`: `grounded_in` lacks the conciliar gravity |
| N3 | new, optional (flag) | open | brief `formation_limitations[6]`: the rite words live only in context chunks |
| N4 | new, optional | open | brief `cautions[6]`: fragile FRE |

## Notes on findings

**B1.** The false absence claim is gone. Checked at source: the belief question is at ANF05 lines 38062-38063 and 40319 (Cyprian's correspondence), and "Dost thou renounce? I renounce." is at npnf108 line 17698 (Augustine on Psalm 81). That matches `lpcctx002`, and "each is attested in one bishop's years only" is accurate. The laying on of hands matches `lpcctx004`, which gives no words. "The rites have not yet been read as evidence in their own right" is world core line 248. See N3 for the grounding.

**S1.** The front's `story[12]` and `voices[0].hedge` now say "The texts held here do not fix their date or place", with "none has been assessed" and "none is drawn on". That is Doc_02 section 7's wording ("whose date and place the vendored files do not fix; none is assessed, and none is drawn on for a claim") and world core line 273. "Several" replaces "a few". Silence wording across tile, `story[12]` and brief `formation_limitations[5]` still matches Doc_02 section 7 and stays inside this world's own record.

**S2.** The tile now says "No text written by a woman survives", which is the wording of `lpc.limit.womens-own-voice`'s `why_sources_cannot_answer`. The 31-word opener is split. Claims row `e92de79f` is now set (see the register section).

**S5.** "Won every dispute" is gone, and "Most of the English texts ... 1800s" matches the force's "mainly". "The church that copied and kept them honored both men" rests on the force's named agent (the Catholic manuscript tradition) and "the canonized one". It no longer claims a cause for the survival, which is less than the force says, not more.

**S6.** "By this world's own account" restores the force's framing ("the world's own self-understanding ... not assessed"). "Both men expected their writings to outlast them" and "went back over his life's work and corrected it" rest on the force's own lines on Cyprian's dossier and the Retractationes.

**S7.** The hedge now states what the later dating means. It matches Doc_02 section 7's Koch quotation ("a writer living at the end of the third century at the earliest, who plays the eyewitness"). The "cannot separate the facts" overstatement is gone. The date stays Contested in Doc_02 section 8, and the hedge presents both dates.

**S8.** The item now reports Cyprian's view as his and Augustine's as his, and ends "The world keeps that question open", which is world core caution 6 (lines 310-311) and Doc_02 line 126. Grounding: N2.

**S10.** "Datus names the silence as a plain fact. He does not explain it, and he does not fill it." This matches `lpc.limit.the-silent-century` and world core line 244 ("never an occasion for commentary"). The Facilitator steps in only when his answer does not satisfy, as Phase Six section 2 has it.

**S11.** All three partner ids are in `pairing_guidance.grounded_in` and resolve. Each claim was reread against its partner record. The ijc wording ("uses Augustine's own defence ... to show its central concern") fits the gravity's `illustrated-by` edge to `ijc.quote.compelled-to-come-in`. The gallic wording ("can sometimes begin"; "Cassian's own text says both things"; the reply "is disputed") fits `gallic.contested.beginning-of-good-will` (Conf. XIII.9 and the record's own "says both"). Windows match `records/worlds/`: ijc 312 to 451, gallic 360 to 450, don 311 to 439. All three paragraphs now carry the cautions:

- Contemporaries-not-stages: in all three.
- Ending-not-read-back, both ways: in all three ("neither world's later years may be used to judge the other").
- Handoff containment: Donatism and ijc say "Nothing from there may fill this world's silence between 258 and 391". Gallic says "Nothing from there may stand in for Pelagius". That is the right containment for a grace pairing, because the gallic window's part inside the silence (360 to 391) is Gaul, not Africa.

**O6.** The template and otherness sentences are in, and the safety rule holds: Facilitator-only, template-anchored, warm, unconditional, never waiting on the participant saying they are fine, and stern otherness is not distress. The drafter's reword is sound. Its FRE is fragile (N4).

**N1. New, substantial. Brief `formation_limitations[0]`.** The added sentence reads "What survives is what drew a bishop's attention in a crisis, and that is why it survived." It came from the round-1 review's O13 proposal, so this reviewer owns it. No record gives crisis as the reason texts survived. `lpc.force.transmission-institutionally-dominant-side` names the manuscript tradition and the dominant side as the agents, and says the imbalance comes from the near-total absence of any voice but a bishop's. The sentence is also wrong for Augustine's years. His routine sermons and catechesis survive in bulk, and the front calls preaching the main way people were formed, "week after week" (`lpc.gravity.preaching-and-catechesis`). A Facilitator could pass this on as fact. Proposed full text of the item (FK 8.2, FRE 64.0):

> This world cannot give an ordinary believer's own account of an ordinary week. Almost nothing survives that a lay believer wrote about church life. The nearest are two letters between confessors, and Augustine's account of his own baptism, which he wrote years later as a bishop. The church that copied and kept these texts was keeping its bishops' writings. So most of the record is what a bishop saw and decided. It is also a Latin, literate record, so it says little about people who could not read or who spoke Punic or Berber.

Add `lpc.force.transmission-institutionally-dominant-side` to that item's `grounded_in`. The Article 20 "why" is then carried by what the record says, not by a cause it does not give.

**N2. New, optional. Brief `formation_strengths[1]`.** The new sentences on Augustine's correctable councils and the open question are true (world core lines 310-311). But the item's `grounded_in` (acclamation force, `lpc.term.the-people`, `lpc.quote.bishop-of-bishops`, collegial gravity) does not include the record that carries them. Add `lpc.gravity.conciliar-authority-theory`.

**N3. New, optional, flag to the record owner. Brief `formation_limitations[6]`.** The two baptismal exchanges and the laying on of hands are true at source (B1 note). But they live only in the context chunks `lpcctx002` and `lpcctx004`. `grounded_in` cannot cite those, and the cited `lpc.term.catechesis` and `lpc.term.reconciliation-penitential-discipline` do not carry them. Nothing is wrong in the text. This is a record-layer gap, and it belongs in the world's gaps log.

**N4. New, optional. Brief `cautions[6]`.** It grades FRE 60.39, so any later edit may drop it below 60. Splitting one sentence lifts it to 61.2 (FK 7.4) with no change of substance. Replace "This world's warmth is the grief of a shepherd wounded by his flock's wound, and its teaching on the road back stresses being examined and weighed before being received home." with:

> This world's warmth is the grief of a shepherd wounded by his flock's wound. Its teaching on the road back stresses being examined and weighed before being received home.

## AI tells and register (changed text only)

No new tells. The revision removed the round-1 tells: the not-X-but-Y shape, the archaic "for", the nominal chain, and the balanced double negative in `legacy[1]`. The new text is plain and declarative. "The rites are argued over more than they are described" is the one line with a balanced shape. It is kept because it states world core line 248 exactly. The etic "this world" is right for both records.

## Claims register rows set

- **`47bbbca6` (world core, uncompiled Registry rows): VERIFIED, Documented.** A script parsed all 355 numbered Registry rows (1 to 355, no gap, no duplicate). The 142 rows above 213 split into 57 Excluded, 84 Native, and row 222 (Native for the Cyprianic acts, Excluded for Perpetua and the Scillitan Martyrs). All 208 source records carry `lpc_source_registry_row` values within 1 to 213, missing exactly 28, 29, 98, 128 and 204, and none above 213.
- **`e92de79f` (tile, women and the lapsed): JUDGEMENT, Documented.** Both limit records were reread. The two nearest women's cases were checked at source. npnf101 Letters XXV and XXX (lines 24531, 25665) are "from Paulinus and Therasia", and the record reads their voice as his. Knopf-Krueger no. 16, ch. VIII (lines 5771-5775) gives Quartillosa's vision as "Vidi, inquit", inside an act the narrators wrote. For the lapsed, ANF05 lines 31240-31246 show the one letter the lapsed sent Cyprian "is Wanting". The status is JUDGEMENT because the claim turns on reading the joint letters as not written by Therasia.

## Truncation check of the two records (two independent methods)

- **Method A, parsed structure.** Both files parse as YAML front matter. All 69 prose fields of nine words or more end in terminal punctuation (script scan; 0 unterminated).
- **Method B, raw bytes.** Front: 336 lines, 22,988 bytes. Brief: 350 lines, 20,431 bytes. Each has exactly two `---` fences and ends with `---` and a newline. `git hash-object` on each working file equals `git rev-parse HEAD:<path>` (994365b84, ecc78b883).

## What happens next

The drafter applies N1 as worded, and N2 to N4 if it chooses. It logs N3 to the record owner and this recheck's outcome in `Open_Gaps_Tracking.md`, then reruns `regate lpc`, `claims lpc` and `citations`. N1 does not change a registered claim, so no register row moves. Round 3, the last under the cap, would check N1 alone. If N1 lands as worded, nothing blocking or substantial remains in either record.

End of recheck.
