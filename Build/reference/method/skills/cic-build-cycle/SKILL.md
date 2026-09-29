---
name: cic-build-cycle
description: Use whenever building, continuing, reviewing, or approving a construction document for a "Church in Conversation" (CiC) formation-world build. Trigger on "build the next document," "run the build cycle," "continue the CiC build," "do Doc_01/Doc_02/World Identification/Source Ecology," or any reference to a formation world's construction sequence. Also trigger the moment a construction document has just been drafted, or a review result has come back and a decision is needed. Enforces one document at a time, review-gated, with a three-round cap.
---

# CiC build cycle (Process V2.0)

This skill governs how one construction document gets built inside a formation-world build. The cycle exists because batching documents or self-certifying quality has caused real defects here: an unmarked borrowing from the wrong tradition, a reasoning error that survived until a later review, a scope decision assumed instead of argued.

The world build starts from the Library handoff, after Step 2. It runs to freeze. Go-live is a separate thread.

## The bar

Every document is held to four criteria. Craft is the keystone.

1. **Rigor.** Every claim traces to a real source. A Contested or Inferential-Thin claim keeps its hedge.
2. **Accessibility.** Plain English first, one idea per sentence, FK grade 8-10, Flesch Reading Ease 60 or higher.
3. **Craft.** A distinct, real voice. The world's own imagery and concerns survive.
4. **Focus.** The answer addresses what was asked, including the hardest questions.

Zero fabrication anywhere: records, voice, probe documents, review files. The review bar is what a church history scholar would call good. It is not perfection.

## Model routing

- **Sonnet 5.5** drafts every document except Doc_04 and Doc_10. It also orchestrates and does mechanical work.
- **Fable** drafts only Doc_04 (Gravity Discovery) and Doc_10 (Representative Construction Notes, Permanent Prompt, voice, demonstrations). Fable also diagnoses failures in Phase D.
- **Opus 5.5** reviews every round, grades blind, and authors every `modern_rendering`. A separate Opus pass checks each rendering.
- The reviewer is never the drafter.
- Round 1 is Opus at high effort. Rounds 2 and 3 are targeted rechecks at medium effort.

## Where you are in the cycle

1. **No document open.** Draft the next one in the confirmed sequence.
2. **Just drafted.** Run the gate layer, then review.
3. **Review came back.** Decide: substantial revision or not.
4. **Cleared review.** Check the four escalation categories. If none applies, apply "Approved to proceed" yourself. If one applies, escalate to Mark and wait.
5. **Approved to proceed.** Only now does the next document begin.

If an earlier document has not reached at least "Approved to proceed," do not draft, outline, or plan a later one.

## Draft

Produce exactly one document, the next in the confirmed sequence. Ground it in this world's earlier documents and the governing methodology. Do not borrow content, sources, or characterizations from another world, even a similar one.

- Address this world's known open issues in the document. Do not defer them silently.
- Check whether the step is one of the Forces Framework's six integration points (Steps 1, 2, 4, 5, 7, 8: Doc_01, 02, 04, 05, 07, 08). Read the Forces Framework's Section 4 entry for the step before drafting.
- Before drafting or revising, check whether this exact document already exists in the canonical folder marked "Approved to proceed" or "Frozen." If it does, and there is no linked review file plus a disposition log entry (for Frozen, Mark's own recorded decision), stop. Flag the conflict and wait.
- All output goes in the world's canonical folder, `Build/worlds/<code>/`. Never write to a thread-local or scratch path. If output landed elsewhere, move it before continuing.
- Doc_04 follows the template at `Build/reference/L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md`.
- Use the M4 lens spine (Completion Standard section F) in Doc_05 and Doc_07.
- Keep a claim register for any document that restates claims from several sources. Every restated claim carries its confidence level and source.
- Indexes are record-native. Do not create `.xlsx` workbooks or master-index spreadsheets. Indexes come from the record store and its generated views, or from plain markdown or yaml lookup tables kept in the document itself.

## Gate layer

Run these before Opus sees the work. Fix every failure first.

```
python -m engine.m10.cli prereview   # build, bar screen, cross-world, holdings
python -m engine.m10.cli citations   # every record id and citation resolves, right type
python -m engine.m10.cli gaps        # every open item has an Open_Gaps_Tracking.md entry
python -m engine.m10.cli roundcount  # blocks a 4th review file, routes to Mark
python -m engine.m10.cli reviewfile  # reviewer differs from drafter, model is Opus 5.5,
                                     # simulated-review label, two-method truncation check
python -m engine.m10.cli records     # required record types built, not waived
python -m engine.m10.cli regate      # after any edit: readability and word budget re-run
```

At handoff, `python -m engine.m10.cli handoff` runs the 12 handoff checks and confirms Steps 0-2 exist and cleared review. At the deployed stage, `deployed` and `probes` check the compiled prompt (see the validation skill).

Readability (FK 8-10, FRE 60 or higher) is a mechanical gate on every public-facing field, re-run on every edited field. AI tells are a judgment read in the Opus review, against the approved sample record `records/syr/demonstration/syr.demo.room-for-doubt.md`. There is no banned-word list. Do not add one.

## Review

An adversarial review, specific to the document, runs in an isolated session. It is saved as its own file beside the document, for example `Doc_05_Review_Round1.md`. A revision-log line that says what a review "found" is a summary, not the review. If the review file is not in the folder, the review did not happen.

- The first line of every agent-run review file is: "Simulated review - informational only, not an Article 31 substitute."
- Record a truncation check using two independent methods in every review round.
- The review checks: factual and historical accuracy of every substantive claim; consistency with earlier decisions; source-attribution discipline; whether the document does the job this stage requires; and, for the six forces-integration steps, whether the requirement is present and substantive.
- A finding is never dismissed as a tooling or environment artifact (stale cache, mount discrepancy) without independent re-verification that confirms the dismissal. A blocking finding cannot be dismissed by self-certification. It needs independent re-confirmation.
- Content described to anyone as "shown" or "posted" must be included verbatim in what they receive.
- Every open item in a review or phase document gets an `Open_Gaps_Tracking.md` entry.

## Revision decision

A revision is **substantial** if it changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary. It is **not substantial** if it is wording, tone, formatting, or a typo.

- If substantial: revise, then review again. **At most three rounds of substantial revision per document.** A finding that the document could be stronger, with nothing wrong, unsupported, or misleading, is not substantial and starts no new round.
- If the document has not cleared after the third round, that is an unresolved tension the pipeline cannot close alone. Stop and escalate to Mark. Never start a fourth round.
- Rounds 2 and 3 are targeted rechecks of the prior findings and the diff, at medium effort.
- If cosmetic only: apply it, note that it was applied, and move on.
- If two reviews of the same document disagree, log the disagreement. Do not quietly side with the later one.

## Escalation categories

Check these before any disposition. If one applies, stop and escalate to Mark, however clean the review.

- **Representative identity, name, or title.** Every decision, including a later change. Use the grounded-options format: 2-4 named candidates (identity and image decided together), an explicit trade-off for each, a recommendation, and a dedicated decision file. Discuss with Mark before the decision is used anywhere else.
- **Portfolio-level or cross-world decisions.** Anything decided for a reason outside this world's own ecology. Label it portfolio-level in whatever records it.
- **Governance or methodology decisions.** Anything that changes how the build process works.
- **Unresolved tensions.** Two reviews disagreeing, a contradiction between two cleared documents, a finding that cuts against an earlier decision, or a document that has not cleared after three rounds.

Also escalate a missing input, the metered-spend ceiling for the validation set, and any change to a settled decision. A change to a frozen or settled item is a named, reasoned change order, never a quiet edit.

## Naming and term propagation

When a name or term changes, check every file it appears in: narrative document, record, lexicon chunk, index or lookup table. A fix in one file without the others is not complete.

## Disposition

A document is eligible only after an independent review that calls for no substantial revision, with no escalation category applying. The author's own judgment never counts.

- **Cleared review.** Passed independent review, not yet disposed of.
- **Approved to proceed.** A lightweight go-ahead that unblocks the next document. If no escalation category applies, the build thread applies it without waiting for Mark. It claims nothing about completeness. Use these words only. Nothing closes until Phase Five boundary testing and full-system review are both complete. That whole-system gate is separate from a single document's approval.
- **Frozen.** Mark has read the complete document and its review files and closed it on purpose. It can be reopened later. A build thread never assigns Frozen, and never on an ambiguous reply. If in doubt, the document stays at "Approved to proceed" and the doubt goes to Mark.

Review rounds exist as files. A status line inside a document is not evidence. Nothing is attributed to Mark in any document without a verifiable record that he said or wrote it.

Once a document is at least "Approved to proceed," log it: name, review outcome, rounds taken, where each review file lives, and the disposition. Then begin the next.

## Cross-document fact consistency

When two documents state the same claim (a fact, number, quoted phrase, term) from the same source, check that they match, or that the difference is deliberate and disclosed. Two real defects came from this: one world's Doc_02 and Doc_03 contradicted each other on whether a term was attested; and one world's Permanent Prompt and Capsule Core restated the same fact in different words, and a later review misattributed a quote between them. Where a claim must appear twice, carry the exact wording across or say why it differs. Rule counts in the compiled prompt (for example `[quotation]`) must match the records.

## Budget and pacing

- One world at a time by default. A second concurrent session runs only when the cost ledger shows the weekly allowance allows it.
- Keep two ledgers per world. (1) Weekly allowance share: note the /usage percent at world start and at freeze, plus tokens by model tier, review rounds, and hours. (2) Metered API spend in dollars: live interview, blind probes, any TTS. The paid-bulk-run gate in CLAUDE.md applies.
- Read /usage before starting a world. Start only if the remaining build allocation covers a typical world plus reserve.
- Heavy steps (Opus review rounds, Fable drafts) go early in the weekly window. Pause only at document boundaries. Keep a compact state file so the world can resume after the weekly reset.
- The process version is stamped on each world at start. A change after that is a named change order.

## Coach verification

A coach thread checks in across a batch of already-disposed work, not per document. It verifies that review files exist and support what cites them, that escalation triggers were not missed, that the decision log matches disk, and that decisions match the governing designs. It reports to Mark and does not draft or revise world documents.

Editing authority over non-world files (Construction Framework, Representative Construction Framework, build process and completion standard, change-order register, L3B and L4 templates) belongs to a coach thread. A build thread writes only inside its own world's folder.

A coach may make small technical corrections inside a world file (a citation misattribution, a broken cross-reference, a propagation fix) if the correction changes no claim, finding, or decision and is logged with its date in the Build/Ministry decision log, never as a note inside the world file. Anything touching substance stays with the build thread or goes through escalation.

## If something does not fit

If a stage needs more than one review round by design, or does not map to one document, say so plainly to Mark instead of forcing the cycle.
