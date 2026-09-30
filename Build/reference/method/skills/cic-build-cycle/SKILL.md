---
name: cic-build-cycle
description: Use whenever building, continuing, reviewing, or approving a construction document for a "Church in Conversation" (CiC) formation-world build. Trigger on "build the next document," "run the build cycle," "continue the CiC build," "do Doc_01/Doc_02/World Identification/Source Ecology," or any reference to a formation world's construction sequence. Also trigger the moment a construction document has just been drafted, or a review result has come back and a decision is needed. Enforces one document at a time, review-gated, with a cap of three review files.
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

The Representative speaks only from the world's perspective, as the world, in the first person plural ("we," "our"), never "this world" or "it" about its own community; the `voice-perspective` gate in `engine/m1/gates.py` checks it. Right answers first, generated correctly: the first generated answer is the one graded, a regenerated or revised answer never counts as a pass, and a defect is fixed at its source (the record, the prompt, the guard or the retrieval), never by a later rewriting step.

Zero fabrication anywhere: records, voice, probe documents, review files. The review bar is what a church history scholar would call good. It is not perfection.

## Model routing

- **Sonnet 5.5** drafts every document except Doc_04 and Doc_10. It also orchestrates and does mechanical work.
- **Fable** drafts only Doc_04 (Gravity Discovery) and Doc_10 (Representative Construction Notes, Permanent Prompt, voice, demonstrations). Fable also diagnoses failures in Phase D.
- **Opus 5.5** reviews every round, grades blind, and authors every `modern_rendering`. A separate Opus pass checks each rendering.
- The reviewer is never the drafter.
- The first review file is Opus at high effort. The second and third are targeted rechecks at medium effort.

## Where you are in the cycle

0. **Before the first document.** Fetch `origin/main` and read the current repository state before judging what exists. Look for a prior partial build of this world (unmerged branches, `Archive/`, older folders such as `Build/World-Builds/`). If one exists, recover and audit it. Do not start fresh over it. Run one live thread per world.
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
- Before drafting or revising, check whether this exact document already exists in the canonical folder marked "Approved to proceed" or "Frozen." If it does, and there is no linked review file plus a disposition log entry (for Frozen, a decision Mark recorded himself), stop. Flag the conflict and wait.
- All output goes in the world's canonical folder, `Build/worlds/<code>/`. Never write to a thread-local or scratch path. If output landed elsewhere, move it before continuing.
- Doc_04 follows the template at `Build/reference/L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md`.
- Use the M4 lens spine (Completion Standard section F) in Doc_05 and Doc_07.
- Keep a claims register for any document that makes or restates claims other documents rely on, including one that restates claims from several sources. Register every absence or exclusivity claim ("no source says...") with its confidence level, its source and whether it has been verified. `python -m engine.m10.cli claims <code>` derives those claims from the deliverables and halts on an unregistered claim or a stale register entry. Registration is the control. Verification is separate work. The register is `Build/worlds/<code>/<code>_Claims_Register.md`, made from `Build/reference/L4-Templates/Claims_Register_Template.md`; `claims <code> --bootstrap` prints rows to paste. The command finds a closed set of claim patterns, so a clean run does not show the documents hold no other absence claim.
- Indexes are record-native. Do not create `.xlsx` workbooks or master-index spreadsheets. Indexes come from the record store and its generated views, or from plain markdown or yaml lookup tables kept in the document itself.

## Gate layer

Run these before Opus sees the work. Fix every failure first.

```
python -m engine.m10.cli prereview <code> --doc N    # build, bar screen, cross-world, holdings;
                                                     # saves the review brief; a missing document fails
python -m engine.m10.cli citations <code>   # every record id and citation resolves, right type
python -m engine.m10.cli claims <code>      # every absence or exclusivity claim registered; no stale entry
python -m engine.m10.cli gaps <code>        # every open item has an Open_Gaps_Tracking.md entry
python -m engine.m10.cli roundcount <code> N --check-new   # before any new review file is written;
                                                           # with 3 review files on record it exits
                                                           # non-zero and routes to Mark
python -m engine.m10.cli reviewfile <path>  # reviewer differs from drafter, model is Opus 5.5,
                                            # simulated-review label, two-method truncation check
python -m engine.m10.cli records <code>     # required record types built, not waived
python -m engine.m10.cli regate <code>      # after any edit: readability and word budget re-run
```

`N` is the document number (`0` for Step 0, for `prereview` and `roundcount` alike). `prereview` saves its output at `Build/worlds/<code>/build/<code>_Prereview_Doc<N>.txt`, and that file goes to the reviewer as the review brief. Without `--check-new`, `roundcount` fails only once a fourth file exists, so run it with `--check-new` first. The full file-name table is in Section 3 of the Process document.

At handoff, `python -m engine.m10.cli handoff <code>` runs the 12 handoff checks and confirms Steps 0-2 exist and cleared review. Check 1 fails a new world until `safety_adjacent` on its registry entry is `true` or `false`. Mark sets it at handoff. At freeze, `python -m engine.m10.cli records <code> --freeze` requires the record types whatever the world's state. `python -m engine.m10.cli integrity <code>` checks open items, unmarked superseded files, stated record counts, and that `deployed` passes at the pinned package, stale-package check included (`--no-stale` skips it). The reviewer checks the three parts no script reads, and that each fix a document calls applied is found in the deployed artifact. At the deployed stage, `deployed` and `probes` check the compiled prompt (see the validation skill).

Readability (FK 8-10, FRE 60 or higher) is a mechanical gate on every public-facing field, re-run on every edited field. AI tells are a judgment read in the Opus review, against the approved sample record `records/syr/demonstration/syr.demo.room-for-doubt.md`. There is no banned-word list. Do not add one.

## Review

An adversarial review, specific to the document, runs in an isolated session. It is saved as its own file beside the document, for example `Doc_05_Review_Round1.md`. A revision-log line that says what a review "found" is a summary, not the review. If the review file is not in the folder, the review did not happen.

**Review-file names.** A review file is a `.md` file in the world folder or its `Review-Artifacts/` folder. Its name begins with the document's label (`Doc_NN`, or `Step0` for Step 0) and holds `Review`, `Recheck`, `SpotCheck`, `Check` or `Verification` as a whole name part. Name it `Doc_NN_<Topic>_<Kind>_Round<N>.md`, or `Step0_<Topic>_<Kind>_Round<N>.md` for Step 0. `<Kind>` is `Review`, `Recheck` or `SpotCheck`, and the topic words are optional. `N` is the file's place in the document's series: the first review file is 1, the next is 2, the last allowed is 3. The header's `Round:` field carries the same number, and `reviewfile` fails a mismatch. A file counts toward the cap even if its name has no `Round<N>` part.

**Every review file counts toward the cap of three.** A Review, a Recheck, a SpotCheck or any other review-type file is one file, whatever its verdict. A recheck of a fix is not a free extra round. Run `roundcount <code> N --check-new` before writing any of them.

- The first line of every agent-run review file is: "Simulated review — informational only, not an Article 31 substitute."
- Record a truncation check using two independent methods in every review round.
- The review checks: factual and historical accuracy of every substantive claim; consistency with earlier decisions; source-attribution discipline; whether the document does the job this stage requires; and, for the six forces-integration steps, whether the requirement is present and substantive.
- A finding is never dismissed as a tooling or environment artifact (stale cache, mount discrepancy) without independent re-verification that confirms the dismissal. A blocking finding cannot be dismissed by self-certification. It needs independent re-confirmation.
- Content described to anyone as "shown" or "posted" must be included verbatim in what they receive.
- Every open item in a review or phase document gets an `Open_Gaps_Tracking.md` entry.
- Make no structural edit to a tree while a review of that tree is running. A review reads one state.

## Revision decision

A revision is **substantial** if it changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary. It is **not substantial** if it is wording, tone, formatting, or a typo.

- If substantial: revise, then review again. A substantial revision needs a new review file, and **a document gets at most three review files in all.** A finding that the document could be stronger, with nothing wrong, unsupported, or misleading, is not substantial and starts no new review.
- If the document has not cleared after its third review file, that is an unresolved tension the pipeline cannot close alone. Stop and escalate to Mark with the third file's findings. Never write a fourth file. A revision made after the third file is not reviewed by a fourth file. `python -m engine.m10.cli roundcount <code> N --check-new` counts every review file (Review, Recheck or SpotCheck), whatever its verdict, and exits non-zero when a fourth would be written.
- The second and third review files are targeted rechecks of the prior findings and the diff, at medium effort.
- If cosmetic only: apply it, note that it was applied, and move on.
- If two reviews of the same document disagree, log the disagreement. Do not quietly side with the later one.

## Escalation categories

Check these before any disposition. If one applies, stop and escalate to Mark, however clean the review.

- **Representative identity, name, or title.** Every decision, including a later change. Use the grounded-options format: 2-4 named candidates (identity and image decided together), an explicit trade-off for each, a recommendation, and a dedicated decision file. Discuss with Mark before the decision is used anywhere else.
- **Portfolio-level or cross-world decisions.** Anything decided for a reason outside this world's own ecology. Label it portfolio-level in whatever records it.
- **Governance or methodology decisions.** Anything that changes how the build process works.
- **Unresolved tensions.** Two reviews disagreeing, a contradiction between two cleared documents, a finding that cuts against an earlier decision, or a document that has not cleared after three rounds. A defect class that keeps returning across rounds is named in the review file and escalated. Do not chase it one instance at a time.

Also escalate a missing input, the metered-spend ceiling for the validation set, and any change to a settled decision. A change to a frozen or settled item is a named, reasoned change order, never a quiet edit.

## Naming and term propagation

When a name or term changes, check every file it appears in: narrative document, record, lexicon chunk, index or lookup table. A fix in one file without the others is not complete.

A correction that changes a claim is verified by a separate agent, against the source, before the document proceeds. That agent sweeps outward from every site the correction names, through every copy of the claim, and not only the named sites. Confirm every cited passage by its structural marker in the vendored file (a `div` title or a chapter heading). A single search hit is a lead and never a confirmation.

## Disposition

A document is eligible only after an independent review that calls for no substantial revision, with no escalation category applying. The author's own judgment never counts.

- **Cleared review.** Passed independent review, not yet disposed of.
- **Approved to proceed.** A lightweight go-ahead that unblocks the next document. If no escalation category applies, the build thread applies it without waiting for Mark. It claims nothing about completeness. Use these words only. Nothing closes until Phase Five boundary testing and full-system review are both complete. That whole-system gate is separate from a single document's approval.
- **Frozen.** Mark has read the complete document and its review files and closed it on purpose. It can be reopened later. A build thread never assigns Frozen, and never on an ambiguous reply. If in doubt, the document stays at "Approved to proceed" and the doubt goes to Mark.

Review rounds exist as files. A status line inside a document is not evidence. Nothing is attributed to Mark in any document without a verifiable record that he said or wrote it.

Once a document is at least "Approved to proceed," log it: name, review outcome, rounds taken, where each review file lives, and the disposition. Record every decision with the real alternatives considered and why the chosen one is the most defensible, not only the conclusion. Then begin the next.

## Cross-document fact consistency

When two documents state the same claim (a fact, number, quoted phrase, term) from the same source, check that they match, or that the difference is deliberate and disclosed. Two real defects came from this: one world's Doc_02 and Doc_03 contradicted each other on whether a term was attested; and one world's Permanent Prompt and Capsule Core restated the same fact in different words, and a later review misattributed a quote between them. Where a claim must appear twice, carry the exact wording across or say why it differs. Rule counts in the compiled prompt (for example `[quotation]`) must match the records.

## Budget and pacing

- One world at a time by default. A second concurrent session runs only when the cost ledger shows the weekly allowance allows it.
- Keep two ledgers per world. (1) Weekly allowance share: note the /usage percent at world start and at freeze, plus tokens by model tier, review rounds, and hours. (2) Metered API spend in dollars: live interview, blind probes, any TTS. The paid-bulk-run gate in CLAUDE.md applies.
- Read /usage before starting a world. Start only if the remaining build allocation covers a typical world plus reserve.
- Heavy steps (Opus review rounds, Fable drafts) go early in the weekly window. Pause only at document boundaries. Keep a compact state file so the world can resume after the weekly reset.
- The process version is stamped on each world at start. A change after that is a named change order.
- Budget targets plan the work and never thin it. If staying inside a number would mean shipping work below the bar, stop at the last green checkpoint and put the choice to Mark in allowance and dollars. Running out is never a licence to rush.
- The state file, the commits and the checkpoint artifacts tell one story. File any mismatch in `Open_Gaps_Tracking.md`.

## Coach verification

A coach thread checks in across a batch of already-disposed work, not per document. It runs after every five worlds (Process V2.0, Section 11) and across any batch Mark names. It verifies that review files exist and support what cites them, that escalation triggers were not missed, that the decision log matches disk, and that decisions match the governing designs. It reports to Mark and does not draft or revise world documents.

Editing authority over non-world files (Construction Framework, Representative Construction Framework, build process and completion standard, change-order register, L3B and L4 templates) belongs to a coach thread. A build thread writes only inside its own world's folder.

A coach may make small technical corrections inside a world file (a citation misattribution, a broken cross-reference, a propagation fix) if the correction changes no claim, finding, or decision and is logged with its date in the Build/Ministry decision log, never as a note inside the world file. Anything touching substance stays with the build thread or goes through escalation.

## If something does not fit

If a stage needs more than one review round by design, or does not map to one document, say so plainly to Mark instead of forcing the cycle.
