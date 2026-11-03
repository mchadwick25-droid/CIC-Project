# V7 controlled test: plan

Written 2026-11-03 under Mark's authorization (Answering-From-Sources Decision-Log 75). Each claim below carries a label:
- **Verified** means read in code or a report; the source is named.
- **Assumption** means taken as given and not checked.
- **Hypothesis** means a claim the test exists to check.

## 1. What is being compared

| Arm | Engine | What it tells us |
|---|---|---|
| **A-live** | Branch `live` at the commit in production when the run starts (today c869dd86), with its own packages and production settings | The production baseline Mark asked for |
| **A-main** | Branch `main` at the frozen run commit, with the new switch off | Whether `main`'s changes since the last promotion matter on their own. These include the absence rule, lead-in support and the D2 and D2b voice rules. |
| **B** | The same `main` commit with the switch on | The effect of contextual preparation alone, because B differs from A-main only by the switch |

Run counts:
- A-live and A-main run once each.
- B runs twice. The spread between B's two runs is the noise floor: a difference between arms counts only if it is larger than that spread, as in CP.9 (`../Answering-From-Sources/CP9-Retest_2026-11-02/README.md`, Noise floor).

**Verified:**
- Production makes three model calls per ordinary turn: two Haiku 4.5 gate calls in parallel, then one Sonnet 4.5 voice call (`engine/m4/turn.py:138-143` and `:770` on `live`; `render.yaml:145-165`).
- The new arms keep that count. B adds no model call.

**C is not built** unless the decision report shows a remaining problem in B that a selective check could fix. That would need a change order and Mark's approval.

## 2. B, exactly

B changes only what each offered item carries. It does not change which items are offered.

1. **Same records.** Evidence selection is unchanged (`engine/m4/evidence.py`). With the same question, B offers the same record ids as A-main, and a test checks this. That keeps the comparison about preparation, not retrieval. It also keeps every connection the cached world prompt already gives the voice (Mark, §4: richness is non-negotiable).
2. **The quote in view.**
   - Today a quote line shows the speaker and the gist but not the words (`evidence.py:1518-1539`).
   - In B, each offered quote also shows its reviewed modern rendering.
   - Code still places the quote in the answer, as now.
3. **The surrounding text, for the top two items.** For the two highest-ranked offered quotes or stories, B adds the context window that `engine/m4/fit_step.py` already builds: the cited lines plus up to 450 words around them (`fit_step.py:32-33`, `:83-100`). Context ids cannot be cited (`verify_step.py:175-176`), so the voice reads them to understand and cites the record.
4. **The modern-lens note.**
   - Every quote in the three worlds has one (alx 26 of 26, pahc 25 of 25, syr 34 of 34). It is stripped at compile (`engine/m2/builders.py:719`).
   - In B it is shown on the quote's line, as "Reads differently today".
   - The test loader reads it from the record, so the compiled package stays byte-equal.
5. **The reading card (alx only).** Where a record has a card (section 3), its lines are shown under the record.
6. **Directive lines.** A few lines on using this material (Spec V5 holds the text). In short:
   - answer the question first;
   - connect and interpret across the offered sources and the world's ground;
   - keep "the source says", "we understand it to mean" and "this was disputed" distinct in plain speech;
   - say whose view a source gives, and how widely it was shared, only as far as the card or record supports.

   These lines do not add citation rules, and B's checks after drafting are the same as A-main's.
7. **Budget.** B's additions are capped at 12,000 characters per turn (about 3,000 tokens). Past the cap, the context windows are dropped first.
8. **A report-only signal, never a gate:**
   - a sentence speaking for the whole world ("we held", "our churches") whose only cited record is a single-author card;
   - counted per answer for the readers, and nothing is removed for it.

**pahc and syr run B without cards.** Mark authorized cards for alx only. In those two worlds B adds items 2, 3, 4, 6 and 7, all built from material that already exists.

What the three-world comparison can show (**Hypothesis**):
- If B helps in alx but not in pahc and syr, the authored cards matter.
- If B helps equally in all three, delivering existing material is most of the gain, and cards may not need to be written for every world.
- If B helps nowhere, contextual preparation is not the lever, at least with this voice model.

One limit: alx differs from the other two worlds in other ways as well (record counts, shelf, catalogue review), so a cross-world difference is suggestive, not proof.

## 3. The reading card (alx)

A card is short world-construction material, written once per quote and per story. It holds Mark's four distinctions apart, plus the setting and the cautions (Mark, §3). Each line is one or two sentences, and the whole card is at most 120 words.

| Line | Holds | Must come from |
|---|---|---|
| `setting` | Who wrote or said it, to whom, on what occasion. The schema field exists and is empty in all four worlds the reassessment counted. | The source and its edition apparatus |
| `source_says` | What the passage says at this point in the author's argument | The vendored text around the cited lines |
| `historians_conclude` | What historians understand or conclude about it, with a confidence tag from the five-level vocabulary | The world's construction documents (Doc_01–Doc_09) or a shelved scholarly work, named |
| `contributes` | What it adds to understanding the world: belief, practice, or how the community lived its faith | The world's gravities, forces and terms, by id |
| `whose_view` | Whose position this is and how widely it was shared, with the reason we think so. Written as prose, never as a rank. An influential author is not the community; a common practice is not universal agreement. | Construction documents or contested-claim records |
| `open` | What is disputed, uncertain or unrepresentative | Contested-claim, honest-limit or divergence notes, by id |
| `reads_differently_today` | The modern-lens note, rewritten so the voice can say it | The record's existing `modern_lens_note` |
| `complicated_by` | Ids of records that qualify it, only where they exist | Records |

- **Never invent.** A line that cannot be traced to its named source is left out. It is not filled with something plausible. Every card names its source for each line, and review checks each one.
- **Scope of work.** alx has 26 quotes and 9 stories, so 35 cards. Opus authors them and an Opus review reads them, under the build cycle's capped rounds.
- **Where cards are stored.** Cards are stored as an optional `reading_card` field on quote and story records. That is a schema change, so it is filed as a change order (Spec V4a). The compiler strips the field, so packages stay byte-equal and production cannot see it. Only the test loader reads it.

## 4. The question set

120 questions, 40 per world. Each world gets four questions for each of Mark's nine hard cases, plus four ordinary questions.

| Hard case | Source of questions |
|---|---|
| 1. Accurate quotation, incorrect interpretation | Authored |
| 2. Accurate quotation, wrong historical context | Authored |
| 3. Relevant evidence, wrong answer | Authored |
| 4. One author generalized to a tradition | Authored |
| 5. Contradictory sources | Authored |
| 6. Historical uncertainty | Authored |
| 7. Modern assumptions projected backward | Authored |
| 8. The evidence does not give an answer | From the D3 held-out set where it fits; otherwise authored |
| 9. Wants a direct, simple answer | From D3 where it fits; otherwise authored |
| Ordinary questions (4) | From D3 |

**D3 questions.**
- D3 holds alx 34, pahc 30 and syr 27, written blind by Sonnet helpers (`../Answering-From-Sources/Design-Faithful-Build_2026-11-03/Specs/Spec_5_Held_Out_Set.md`). It is still being written.
- A helper that has seen no answers labels each D3 question with the hard case it fits, if any.
- Code then draws the needed counts with a seed fixed in advance. The rest stay held out.

**Authored questions.**
- Each authored question is written by Opus in a visitor's own words, with sight of the world's shelf and construction documents.
- Each carries a sealed *trap note*: what a faithful answer must not do, and the source and lines that show it. A question with no traceable trap is rewritten.
- Readers see the trap note after they score blind, as a check.

**Freezing.**
- The set and its trap notes are frozen by SHA-256 before any card is written and before B is built. A change after that is a change order.
- Card authors and B's builders never open the set. Cards are written for every alx quote and story, never selected by question.
- A code check rejects any question that overlaps a sealed probe beyond the D3 overlap limit. The check compares hashes only, so sealed probes are never printed.

**Limit.** Every question is a single first turn. Conversational quality across several turns is not measured; that is a known gap.

## 5. Readers and human review

- **Model readers.** Two blind, independent in-plan readers (agent type `judge-reader`) score every answer on the ten dimensions in `Rubric.md`.
  - Arm labels are hidden and answers are shuffled with a seed written in advance.
  - Agreement between the two readers is reported per dimension.
  - A disagreement goes to a third read, and the report says how many there were.
  - These readers draw on the weekly allowance, not metered spend.
- **Human historical review.**
  - **No independent human historian is available to this project today.** The repository names none. Every label so far has been a model's (`../Answering-From-Sources/Decision-Log.md` entry 17). The only reviewer brief is a draft (`Build/Ministry/Scholarly-Review/CiC_Article31_Reviewer_Brief_V0_2_DRAFT.docx`).
  - **The sample:** 24 questions per arm for A-live and B (run 1), 8 per world, weighted toward hard cases 1–7. That is 48 answers.
  - **Each answer goes with a source packet:** the question, the answer, the cited records, and the source lines with their context. It takes about 10 minutes an answer, so about 8 hours in all (**Assumption**).
  - **Reviewers record errors, not grades:** the count, the severity tier, the type, and how sure they are.
  - **What Mark can do, in order of strength:**
    1. Recruit one or two patristics scholars (a graduate student or faculty member) for about 8 hours, paid or volunteer. Any fee is outside the $30 model cap and is Mark's decision.
    2. Ask an existing contact in a seminary or university department.
    3. If neither is possible before the decision report, the report says plainly that it has no human historical review. Its findings then count as model-read only, and serious-error rates are reported as unknown.
- **What the sample can show.** A sample of 48 can find problems. It cannot show that serious errors are gone (Mark, §6). The report gives counts with that limit stated.

## 6. The paid run

**Name:** `v7-ab-alx-pahc-syr`. **Cap:** $30 in total, as two commands under the same name. The sample has a $2 cap. The main run is capped at $28 minus what the sample spent.

**Sample first** (CLAUDE.md, paid bulk runs):
- 2 questions per world, through A-live and B: 12 turns.
- The run prints the model ids, the route, settings and counts.
- The coordination thread confirms the sample with Mark before the main run.

**Main run:**
- A-live and A-main once, B twice: 480 turns.
- Each question is a fresh first turn.
- Arms are interleaved per question, so they share the warm cache.

**Estimate (Hypothesis until the sample):**

| Arm | Turns | Per turn | Total |
|---|---|---|---|
| A-live | 120 | $0.020–0.044 | $2.40–5.30 |
| A-main | 120 | $0.020–0.044 | $2.40–5.30 |
| B, two runs | 240 | $0.025–0.055 | $6.00–13.20 |
| Sample | 12 | | about $0.60 |
| **All** | | | **about $11–24** |

How the per-turn figures were reached:
- They start from the measured $0.018–0.040 per answer (`../Answering-From-Sources/Stage1_Ledger.md:15`).
- They add the 1.10 Bedrock regional rate (`engine/m8/price_tables.py:116`).
- B adds up to 3,000 fresh input tokens at Sonnet 4.5's $3.00 per million (`price_tables.py:27-33`).

**Stop rules:**
- If the sample's per-turn cost, scaled to the main run, comes to more than $27, the run stops and returns to Mark before any main-run call.
- The guard stops any call that would cross the cap (`engine/provider/guard.py:258-282`).
- A run that stops on the cap reports what it completed. It is not resumed without Mark.

## 7. Logging

**For each turn:**
- each call's kind and model id;
- its input, output, cache-write and cache-read tokens (`engine/m8/usage.py`, `NormalizedUsage`);
- its seconds to first text and total seconds;
- the turn's wall time and its priced cost;
- the offered record ids, and the size in characters of B's additions.

**For the run:**
- the guard's ledger (`CIC_LIVE_TEST_LEDGER`) and summary;
- the commit hashes of `live` and `main`;
- the package manifest hashes.

**Verified:**
- Production already stores token usage per call (`engine/api/wiring.py:145`, `engine/m8/log_store.py`).
- It stores latency only in log lines (`engine/api/app.py:166`, `:801`).
- The runner therefore times calls itself.

## 8. What the decision report answers

These are Mark's eight questions (his response, §8). Each answer separates verified findings, assumptions and hypotheses.
1. Does B improve contextual integrity and interpretive fidelity?
2. Does it keep or improve responsiveness, depth and conversational quality?
3. Does it keep the Representative speaking from within its world?
4. Is the experience better for an ordinary user?
5. What errors remain?
6. What are the actual cost and latency?
7. What did human reviewers find that automation missed?
8. What is the smallest next change the evidence justifies?

**Success rules for B** (written before the run):
- Better than A-main beyond the noise floor on contextual integrity and on interpretive fidelity.
- On every other dimension, no worse than A-main beyond the noise floor. Depth, responsiveness and world embodiment are named here because of Mark's §4.
- No more tier 1 errors than A-main.
- Cost per answer no more than 1.3 times A-main's.

If B misses a rule, the report says which one, and by how much.
