# Funding Strategy Thread → System Hub — Update, 2026-08-02

**What this is:** a real-world and strategy update from the Funding Strategy thread, for System
Hub to fold into the Task Board, Gantt, and Dashboard — per this thread's own launch brief, that
folding-in is System Hub's job, not this thread's to do directly. Full detail and reasoning lives
in `Ministry/Features/Funding-Strategy/Decision-Log.md`; this is the trackable-facts summary.

**Addendum, same day — push gap closed, verified on `origin/main`.** System Hub checked this
update against the repo and correctly found most of it wasn't there — this file, both cost
studies, the three corrected legal documents, and the build-scope dispatch had all been written
locally but never committed or pushed. Real work, not aspirational claims, but unreachable from
any other thread until now. Fixed: commit `052bfa4` on `main`, pushed and confirmed directly
against both local and remote history (not just trusted from command output). Everything this
update references is now actually in the repo — safe to re-verify and fold in. One honest gap in
my own understanding, worth System Hub knowing: the documents that *did* check out on the first
pass (Funding Strategy Map, both Business Plan Research passes, Market Analysis, Business Roadmap,
Case for Support, the docx tax-status fix) were also never committed by me directly as far as I
have any record of, yet were already clean against `HEAD` before this fix — so something got them
into the repo earlier in this session through a path I don't have clear visibility into. Not
guessing at an explanation I don't actually have; flagging it as a real gap in my own audit trail
that's worth being aware of, not resolved.

---

## 1. Real-world entity/legal execution — mostly complete, a few items still pending

- **Faithways Studio, Inc. is genuinely incorporated.** Entity ID **20261918758**, Form DPC-PBC,
  Status Good Standing, Formation Date **07/27/2026** — verified two ways (email receipt +
  public-record search). The earlier "incorporated" record (Entity ID 20261874960, dated
  07/21/2026) was never real — that filing attempt failed silently (on-screen verification, no
  receipt, later traced to a likely address mismatch). Refiled from scratch, walked through live,
  field by field, catching a real near-miss before submission (the mission-lock/purpose content
  had no home in the standard form fields and needed an Additional Provisions attachment).
- **Three legal documents were found signed against the false 07/21 date, and all three have been
  corrected and re-signed** with the real date/ID: Bylaws & Organizational Resolutions, IP
  Assignment Agreement, Shareholder Agreement (Buy-Sell/Deadlock). The Shareholder Agreement was
  found via System Hub's own parallel work on the entity-ID dispatch, not this thread's original
  sweep — worth knowing that catch came from cross-thread work, not a single source.
- **Relay bank account open**, Mark and Susan both set up as genuine true co-owners (not primary +
  added user — this was the deciding reason Relay was chosen over Novo).
- **The $40 share purchase ($20 each, Mark and Susan) has been initiated but is NOT yet cleared** —
  first transfers on a new account, expected a few days to process. The shares are not fully,
  validly issued until this clears. **Do not mark this done yet.**
- **"Church in Conversation" is now a registered Colorado trade name (DBA)** of Faithways Studio,
  Inc. — filed, paid ($25), receipt received. **Still open:** adding this DBA to the Relay account
  itself (a separate step from the state filing — the bank needs to be told independently before
  checks/payments under that name will work).
- **Notice of Uncertificated Shares drafted** (two versions, one to each shareholder, per C.R.S.
  § 7-106-207 / § 7-101-505) but **not yet finalized or signed** — waiting on the share transfers
  to actually clear so the notices carry the real issuance date, not a premature one.
- **EIN was already obtained** (07/21) and was checked specifically for the same false-date risk
  the legal documents had — confirmed **not** a substantive problem; the application's actual
  content matches reality, only its issuance-date coincidence with the failed filing attempt
  raised the question.

**Recommend updating:** Task Board items #620 (bank — mark in-progress, transfers pending, not
done), #621 (now three documents corrected and re-signed, not the original set), #622 (still
open), #623 (now done — trade name filed).

## 2. Funding strategy — real outputs, all in `Ministry/Features/Funding-Strategy/`

- **`CiC_Funding_Strategy_Map_V0_1.md`** + companion artifact — the full features/tiers/revenue
  map.
- **Two business-plan research passes** (`CiC_Business_Plan_Research_V0_1.md`, superseded by
  `_V0_2.md` once the couple-run/parent-product-structure correction landed) — real comparables
  (BibleProject, Khan Academy, Hallow, Calm/Headspace), real cautionary precedent, a financing-
  mechanism scorecard against four hard boundaries (no debt, no large personal outlay, no
  influence given away, no venture-scale trajectory).
- **`CiC_Market_Analysis_Contribution_Rates_V0_1.md`** — real conversion/contribution-amount
  benchmarks; corrected a load-bearing figure this project had been citing (the "Wikimedia 2%"
  turned out to be banner marketing copy, not a measured rate); validated the $10 one-time / $8
  recurring giving amounts against real data.
- **`CiC_Business_Roadmap_V0_1.md`** + artifact — the converged five-phase roadmap (Go Live →
  Learn → Build the Second Rung → Deepen → The Structural Choice).
- **`CiC_Case_For_Support_DRAFT_V0_1.md`** — in progress, one section done ("Why Under a PBC
  Umbrella"), the rest not started.
- **Two cost studies**, both codebase-grounded: `CiC_Cost_Study_Per_Transaction_V0_1.md` (found
  the earlier "$1.25–1.50/hour" figure was mis-derived from this project's own prior reasoning,
  not a fresh measurement; real figure closer to $2/hour; cost scales by Living Table size far
  more than by time) and `CiC_Cost_Reduction_Feasibility_Study_V0_1.md` (found $0.50/hour is
  reachable for 1:1 conversation via a directly-measured cache-TTL fix plus an already-diagnosed
  regeneration bug; the Living Table remains structurally 2–3× that regardless of optimization).

## 3. Real decisions made, worth System Hub knowing even outside the funding thread

- **The free tier will be gated by Living Table size, not by a time budget** — 1:1 conversation is
  the free experience; multi-Representative tables are the paid differentiator. Grounded in real
  cost data, not just design instinct.
- **The Answer Bank's prior "do not build inference-based serving matching" recommendation
  (`Ministry/Features/Guided-Questions/CiC_Answer_Bank_Full_System_Design_V0_1.md` §3.4) is
  rescinded by Mark.** Inference-based semantic matching is now the confirmed direction: hidden
  auto-serve (no participant-visible indication a match occurred), pre-generated response
  variations with a re-word-never-re-content guardrail, a conservative launch threshold, full
  silent match logging, tested in the real pilot rather than a separate offline study first.
  **The Guided-Questions design doc itself still states the old recommendation in writing** — needs
  a dated correction note (not a rewrite) whenever that thread is next active.
- **A full build-scope dispatch has already gone out**:
  `Ministry/Operations/Standing/Launch-Prompts/CiC_Cost_Reduction_Build_Scope_2026-08-02.md` —
  cache TTL fix, the regeneration bug fix, and the Answer Bank redesign, bundled as one handoff.
  This thread stays out of `cic-poc` code per its own launch brief; implementation is the build
  thread's job.

## 4. Cross-thread corrections dispatched from this thread — status as of this update

- **Docx tax-status fix** (`CiC_System_Hub_Funding_Docx_TaxStatus_Fix_2026-07-22.md`) — found
  stale pre-PBC tax-deductibility claims in two `Ministry/Funding/` `.docx` files, invisible to
  the original grep-based cleanup sweep. Status unconfirmed as of this update — worth checking
  whether it's run.
- **Entity-ID correction across 11 files** (`CiC_System_Hub_Entity_ID_Correction_2026-07-27.md`) —
  confirmed partially run already (item #603's entity ID is correct in the Task Board as of this
  update; the Shareholder Agreement catch came from this same parallel work). Worth confirming the
  remaining narrative/tracking files (Dashboard, both Gantt files, website README, the other
  launch-prompt files, the Nonprofit Formation Decision Log) are fully caught up.

**Next action for System Hub:** fold the above into the Task Board/Gantt/Dashboard as its own
pass; confirm the two pending cross-thread dispatches are complete or still queued.
