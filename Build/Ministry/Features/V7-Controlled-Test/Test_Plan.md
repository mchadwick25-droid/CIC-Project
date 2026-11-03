# V7 controlled test: plan

Written 2026-11-03 under Mark's authorization (Answering-From-Sources Decision-Log 75). Revised the same day on his direction: "we have plenty of test data on the engine that is currently running, use that, then what we need is to compare it to something".

Every claim carries one of three labels:
- **Verified**: read in code, a run file or a report, with the source named.
- **Assumption**: taken as given, not checked.
- **Hypothesis**: a claim the test exists to check.

## 1. The two arms

| Arm | What it is | Paid? |
|---|---|---|
| **A** | The saved answers of **fleet graded run 1** for alx, pahc and syr: 28 sealed probes per world, 84 answers. Not re-run. | Already spent |
| **B** | The same 84 questions, through the same harness, on the same code and records, with the B switch on | Yes; the only paid arm |

**A: fleet graded run 1** (Verified)

The run:
- Approved 2026-10-28; $16.55 spent across the fleet (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, entries of 2026-10-28 and 2026-10-29).
- Ran 2026-10-28 23:16Z to 2026-10-29 00:24Z.
- Voice: Sonnet 4.5, `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, on Bedrock us-east-1, max_tokens 2048.
- Harness: `engine.m3.live_admission_run`.

The code it ran:
- `main` at `ddabd865` plus commits that change only the run driver. The per-world commits are alx `c7a64ffd`, pahc `3c69d7bf` and syr `045a70b9`; the shape hash is `sha256:4b285d56…`.
- `git diff ddabd865 c869dd86 -- engine records` is empty. So the engine and records that produced A are byte-identical to the `live` head now in production (c869dd86, promotion #1264, 2026-10-28).

Where its files are: on branch `claude/fleet-run-1-analysis` only (not on `main`), in the run's report folder `fleet-graded-run-1/` under the engine's m3 reports.
- `<world>.json` holds, for each probe: the draft, the shipped `answer_text`, citations, token usage, `seconds_to_first_text`, `seconds_total` and the stop reason.
- `ledger-<world>.jsonl` holds the priced cost of each call. By world: alx $0.686, pahc $0.659, syr $0.655, about $0.024 per answer.

Nothing is missing for the three worlds:
- all 84 answers;
- the second-pass Opus reviews (`analysis-2026-10-29/second-pass/<world>.json`, rubric in `analysis-2026-10-29/RUBRIC.md`);
- the outside-referee reviews (`analysis-2026-10-29/outside-referees/`).

Cappadocian is the only world in the run whose report was lost, and it is not in this test.

**Use `answer_text` from the run files.** The A answers in CP.9 and the cross-world test leave out the code-placed quote words in 9 of the 28 alx answers. Rebuilding from the run's gate replay reproduces the shipped text in 28 of 28 for each world.

**What A is, and is not** (Verified)

The admission harness runs:
- the production evidence assembly;
- the cached world prompt;
- one voice call;
- the production net, with quote placement (`engine/m3/generation.py`, `LiveModelAnswerer`, at `ddabd865`).

It skips the live turn directive, the safety and reader gate, the recitation retry and self-revision (`analysis-2026-10-29/DIGEST.md`, "The test"). So A is production's answering core, not the full live turn. B is run the same way, so the comparison is like for like.

**B**
- **The code.** A test branch cut from `live` at c869dd86, which is A's exact code. It carries only the B switch (Spec V5) and the reading-card loader (Spec V4a).
  - The branch is never merged into `live` or `main`.
  - The same switch code also lands on `main`, behind the off flag, for later.
- **The run.** B runs through the same `LiveModelAnswerer` harness, with the same model id, region and max tokens. It uses the same packages, matched by the manifest hashes in A's `run_settings`.
- **The only difference from A** is the switch, plus the alx cards, which the loader reads from `main`'s alx records.

**What still differs between A and B**
- **Records.** None on the test branch: B uses A's records. Since A, `main` has changed alx, pahc and syr only lightly:
  - corpus-map pointers;
  - one voice-rule file per world;
  - two small alx fixes.

  The rendering fixes RD1 and RD2 touched other worlds (`git log` on `records/alx`, `records/pahc`, `records/syr` since 2026-10-28). B does not use any of these changes, so none can be mistaken for a B effect.
- **Time.** B runs about a week later, on the same pinned model id. **Assumption:** the provider serves the same model behind that id.
- **Run-to-run variance.** Two runs of the same engine always differ somewhat. §2 measures this.

C is not in scope. If B leaves a problem that selective correction could address, C goes back to Mark for a new approval.

## 2. The noise floor

**B.** B answers 42 of the 84 questions a second time: 14 per world, stratified by the canon cell's family and register, drawn by a seed written in advance. The spread between B's two runs on those 42 is B's run-to-run variance.

**A.** A has no repeat on this code. The nearest measure is `engine/m3/reports/baseline-2026-10-02/`:
- three runs (r1, r2, r3) of the same 28 probes per world for alx, pahc and syr, on Sonnet 4.5, made to measure a noise band;
- run on the 2026-10-02 packages, an older engine.

That spread is reported as an indication only, labelled "older engine". A's own run-to-run variance on this code is **unmeasured**, and the report says so.

**The rule.** A difference between A and B counts only where it is larger than B's own spread. Where the older-engine band is wider than that spread, the difference must clear the band too.

## 3. B, exactly

B changes what each offered item carries. It does not change which items are offered.

1. **Same records.** Evidence selection is unchanged. With the same question, B offers the same record ids as A did. A's `request` field in the run files holds the offered set, and a test checks against it.
2. **The quote in view.** Each offered quote also shows its reviewed modern rendering. Today the voice sees only the speaker and gist (`engine/m4/evidence.py:1518-1539`). Code still places the quote in the answer.
3. **The surrounding text, for the top two items.** For the two highest-ranked offered quotes or stories, B adds the context window from `engine/m4/fit_step.py`: the cited lines plus up to 450 words around them. Context ids cannot be cited, so the voice cites the record.
4. **The modern-lens note.** Every quote in the three worlds has one: alx 26 of 26, pahc 25 of 25, syr 34 of 34. It is stripped at compile (`engine/m2/builders.py:719`). B shows it as "Reads differently today". The test loader reads it from the record, so the package stays byte-equal.
5. **The reading card (alx only).** Where a record has a card (§4), its lines are shown under it.
6. **Guidance lines, at the head of the evidence block.** They go there because the harness, like A, sends no turn directive. Spec V5 holds the text. In short:
   - answer the question first;
   - connect and interpret across the offered sources and our ground;
   - keep "the source says", "we understand it to mean" and "this was disputed" distinct, in plain speech;
   - say whose view a source gives, and how widely it was shared, only as far as the card or record says.

   They add no citation rules. The net and every check after drafting are A's.
7. **Budget.** The additions are capped at 8,000 characters (about 2,000 tokens). Context windows are dropped first.
8. **A report-only signal.** A sentence speaking for the whole world ("we held", "our churches") whose only cited record has a single-author card is counted for the readers. Nothing is removed.

**pahc and syr run B without cards.** Mark authorized cards for alx only. In those two worlds B adds items 2, 3, 4, 6 and 7, all built from existing material.

**What the comparison can show** (Hypothesis):
- If B helps in alx but not in pahc and syr, the authored cards matter.
- If it helps equally in all three, delivering existing material is most of the gain.
- If it helps nowhere, contextual preparation is not the lever with this voice model.

alx also differs from the other two worlds in other ways, so a cross-world difference is suggestive, not proof.

## 4. The reading card (alx)

A card is short world-construction material, written once per quote and per story. It keeps Mark's four distinctions apart (his §3). Each line is one or two sentences, and the whole card is at most 120 words.

| Line | Holds | Must come from |
|---|---|---|
| `setting` | Who wrote or said it, to whom, on what occasion. The schema field already exists and is empty in every world counted. | The source and its edition apparatus |
| `source_says` | What the passage says at this point in the author's argument | The vendored text around the cited lines |
| `historians_conclude` | What historians understand or conclude about it, with a confidence tag from the five-level vocabulary | The world's construction documents (Doc_01–Doc_09) or a shelved scholarly work, named |
| `contributes` | What it adds to understanding the world: belief, practice, or how the community lived its faith | The world's gravities, forces and terms, by id |
| `whose_view` | Whose position this is, and how widely it was shared, with the reason. Prose, never a rank. An influential author is not the community, and a common practice is not universal agreement. | Construction documents or contested-claim records |
| `open` | What is disputed, uncertain or unrepresentative | Contested-claim, honest-limit or divergence notes, by id |
| `reads_differently_today` | The modern-lens note, rewritten so the voice can say it | The record's existing `modern_lens_note` |
| `complicated_by` | Ids of the records that qualify it, only where they exist | Records |

- **Never invent.** A line that cannot be traced to its named source is left out. Every line names its source, and review checks each one.
- **How many.** alx has 26 quotes and 9 stories, so 35 cards. Opus authors them, and an Opus review checks them under the build cycle's capped rounds.
- **The author works blind.** Cards are written for every alx quote and story, never chosen by question. The card author does not read A's or B's answers, or the reviews of fleet graded run 1.
- **Where cards live.** An optional `reading_card` field on quote and story records, filed as a schema change order (Spec V4a). The field is stripped at compile, so production cannot see it.

## 5. The questions, and Mark's nine hard cases

The core run uses A's 84 questions exactly: the 28 sealed probes per world, one per canon cell. Probe texts are read through the existing sealed loader and are never written into this folder.

How the 28 probes per world bear on Mark's nine cases:

| Hard case | Covered by the 84? |
|---|---|
| Modern assumptions projected backward | **Yes.** 7 probes per world are in the T register, "modern terms and anachronisms" (`Build/reference/Redesign-Spec/CiC-Program-Spec.md:114`). |
| Historical uncertainty | **Partly.** 7 probes per world are in the E register, "did it happen, how do you know". |
| The evidence does not give an answer | **Partly.** The E-register probes. Fleet graded run 1 also found that 13 of 28 pahc turns had no record written for the question (`DIGEST.md`, family 3). |
| Wants a direct, simple answer | **Partly.** 7 probes per world are in the I (informational) register. |
| Accurate quote, incorrect interpretation | **As a failure, not a question type.** Readers look for it in every answer that places a quote. |
| Accurate quote, wrong historical context | As a failure, as above. |
| Relevant evidence, wrong answer | As a failure, as above. |
| One author generalized to the tradition | As a failure, as above, with the report-only signal (§3, item 8). |
| Contradictory sources | **Not targeted.** It can appear only by chance. |

**Option for Mark, priced apart from the core run**
- **What it adds.** At most 15 fresh questions, 5 per world, aimed at the cases the probes do not target: two contradictory-sources questions, one one-author-generalized question, and two accurate-quote traps (interpretation or context).
- **How they are written.** By an Opus thread that does not see B's code or the cards. Each question has a sealed trap note tied to named source lines, and the set is frozen by SHA-256 before the cards are written.
- **Cost.** These questions need fresh A and B answers: 30 turns, about $0.80 (§7).
- **Status.** Not part of the core run unless Mark says so.

**Limit.** Every question is a single first turn, so conversational quality across several turns is not measured.

## 6. Readers and human review

**Model readers**
- Both A's and B's answers are scored fresh, by the same readers, on all ten dimensions in `Rubric.md`.
- Two blind, independent `judge-reader` helpers read each answer. Answers are shuffled with a seed written in advance, and arm labels are hidden.
- Agreement between the two readers is reported per dimension.
- Reading draws on the weekly allowance, not metered spend.

**The October reviews of A are reported beside the fresh scores, not mixed in**
- **Why they are not reused as A's scores.** They used a different rubric (rigor; readable, understandable and succinct; ship, fix or block) and different readers. Scoring A with old readers and B with new ones would tie the reader to the arm. CP.9's corrections showed that one-reader ratings "cannot be compared between runs" (`../Answering-From-Sources/CP9-Retest_2026-11-02/README.md`, Corrections).
- **What they are used for.**
  - As a check on the fresh readers: on A, do the fresh scores for dimensions 1–3 and 10 agree with the October rigor and access grades?
  - As a list of known A errors, from the second-pass and outside-referee findings. The report says, for each one, whether B repeats it.

**Human historical review**
- **No independent human historian is available to this project today.**
  - None is named in the repository, and every label so far is a model's (`../Answering-From-Sources/Decision-Log.md` entry 17).
  - The only reviewer brief is a draft (`Build/Ministry/Scholarly-Review/CiC_Article31_Reviewer_Brief_V0_2_DRAFT.docx`).
  - The fleet run's external-reviewer packets were prepared (`analysis-2026-10-29/external-reviewer-packets/`), but no human review of them is on record.
- **The sample.**
  - 12 questions per world, the same 12 in both arms, so 72 answers.
  - Each comes with a source packet: the question, the answer, the cited records, and the source lines with their context.
  - About 10 minutes per answer, about 12 hours in all (**Assumption**).
  - Reviewers record errors: the count, severity tier, type, and how sure they are.
- **What Mark can do, in order of strength:**
  1. Recruit one or two patristics scholars, paid or volunteer. Any fee is outside the $12 model cap and is Mark's decision.
  2. Ask an existing seminary or university contact.
  3. If neither happens before the decision report, the report says plainly that it has no human historical review, and reports serious-error rates as unknown.
- **What the sample can show.** It can find problems. It cannot show that serious errors are gone.

## 7. The paid run and its cap

- **Name:** `v7-b-alx-pahc-syr`. Only B is paid.
- **Cap:** $12, set by Mark 2026-11-03, lowered from $30. It is a ceiling. The guard stops any call that would cross it (`engine/provider/guard.py:258-282`).
- **Order.**
  1. **Sample:** 2 probes per world, 6 turns, with a $1 cap. The run prints the model id, route, settings, token counts and cost. The coordination thread checks it, and Mark confirms it, before the rest runs.
  2. **Main:** B on the remaining 78 probes.
  3. **Repeat:** B on the 42 repeat probes.

| Part | Turns | Per turn (Hypothesis) | Total |
|---|---|---|---|
| Sample | 6 | $0.025–0.047 | $0.15–0.28 |
| Main | 78 | $0.025–0.047 | $1.95–3.67 |
| Repeat | 42 | $0.025–0.047 | $1.05–1.97 |
| **Core run** | 126 | | **$3.15–5.92** |
| Option: 15 hard-case questions, A and B | 30 | $0.018–0.047 | about $0.80 |

How the per-turn figure is estimated:
- The base is A's own cost: about $0.024 per answer in fleet graded run 1, inside the measured $0.018–0.040 (`../Answering-From-Sources/Stage1_Ledger.md:15`).
- B adds up to 2,000 fresh input tokens at Sonnet 4.5's $3.00 per million, times the 1.10 Bedrock regional rate (`engine/m8/price_tables.py:27-33`, `:116`). That is at most $0.007 per turn.

**Stop rules**
- After the sample, code scales its actual cost per turn to the remaining 120 turns. If the core run would pass $11, the repeat is cut to fit, and the coordination thread is told before any further call.
- A run that stops on the cap reports what it completed. It is not resumed without Mark.

## 8. Logging

For each B turn:
- the call's model id;
- input, output, cache-write and cache-read tokens;
- seconds to first text and total seconds;
- the priced cost;
- the offered record ids;
- the size in characters of B's additions.

The fields match A's `run_settings`, `usage` and ledger, so the two arms compare directly. The run also files the guard's ledger and summary, the test branch's commit, and the package hashes.

Latency and tokens for the full live turn (gate plus voice) are not measured here, because neither arm runs the gate. The gate's two Haiku calls are the same in both arms (**Verified**: `engine/m4/turn.py:138-143` on `live`), so they add the same cost and time to each.

## 9. What the decision report answers

Mark's eight questions (his response, §8), with verified findings, assumptions and hypotheses kept separate:
1. Does B improve contextual integrity and interpretive fidelity?
2. Does it keep or improve responsiveness, depth and conversational quality?
3. Does it keep the Representative speaking from within its world?
4. Is the experience better for an ordinary user?
5. What errors remain?
6. What are the actual cost and latency?
7. What did human reviewers find that automation missed?
8. What is the smallest next change the evidence justifies?

**Success rules for B**, written before the run:
- Better than A beyond the noise floor on contextual integrity and on interpretive fidelity.
- On every other dimension, no worse than A beyond the noise floor. Depth, responsiveness and world embodiment are named here because of Mark's §4.
- No more tier 1 errors than A.
- Cost per answer no more than 1.3 times A's.
- Of the known A errors from the October reviews, B repeats fewer than it fixes.
