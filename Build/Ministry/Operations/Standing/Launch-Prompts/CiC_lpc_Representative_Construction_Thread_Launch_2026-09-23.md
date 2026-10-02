# Launch prompt — lpc Representative Construction (Datus), 2026-09-23

**What this thread does.** Continue Representative construction for lpc (Latin
Pastoral-Congregational Christianity, Representative **Datus, Bishop of the
Kept Flock**, card_name "The Ordinary Church") end-to-end, from Phase Two
through world-freeze gates, under the `cic-build-cycle` and
`cic-validation-suite` skills' own discipline — self-governing exactly as
those skills specify, escalating only where they require it.

**Why a separate thread.** The Go-Live Pipeline Coordinator thread (this
launch prompt's author) reconciled lpc's branches, ran Phase One's review
round to Approved to proceed, and tracked the full remaining sequence — but
running the rest of Representative construction turn-by-turn inside that
same thread would burn its own context and usage on drafting/review work
that belongs to a dedicated build thread, exactly the split
`CLAUDE.md`'s "Scaling the build" section describes ("Run multiple worlds
concurrently as separate sessions... rather than serially in one thread").

## Read in full, before any work

1. This document.
2. The `cic-build-cycle` skill (one-document-at-a-time discipline, CO-022
   self-disposition, the four escalation categories, capped review rounds).
3. The `cic-validation-suite` skill (Part Three / Part Eight bar).
4. `reference/L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx`
   in full — it's a .docx; extract it directly (e.g. read `word/document.xml`
   out of the zip) rather than working from any summary, including this one.
5. `reference/L4-Templates/Representative_Construction_Notes_Template.md` and
   `reference/L4-Templates/World_Facilitation_Brief_Template.md`.
6. `reference/method/CiC_World_Build_Completion_Standard_V1.3.md` (the actual
   current version may be later — read what's on disk, not this number).
7. lpc's own record: `worlds/lpc/lpc_Decision_Log.md` in full (identity,
   portrait, Article 29, the 2026-09-21 reconciliation, the 2026-09-23 Phase
   One round), `worlds/lpc/lpc_World_Profile.md`, `worlds/lpc/Doc_01`
   through `Doc_09`, and `worlds/lpc/Representative/lpc_Rep_Phase1_Ecology_Assessment.md`
   (Approved to proceed — read it as the actual handoff into Phase Two, not
   a formality).
8. A worked comparison from a sibling world already through this pipeline —
   `worlds/rzg/` (Theophilus) has the fullest documented Representative
   construction and validation arc in the fleet; `worlds/don/Representative/`
   is the naming-convention precedent lpc's own Phase One file already
   follows.

## What "end-to-end" covers here

In order, each its own document, each through the build-cycle's own Draft →
Review → Revision decision → Disposition cycle:

1. Phase Two — Formation Calibration
2. Phase Three — Voice Construction
3. Phase Four — Engagement Architecture
4. Phase Five — Boundary Testing (= RCF Part Eight validation: the eight
   probe categories, parroting/pushback, Sustained Engagement, Dynamic
   Encounter Validation, the Table Readiness Round)
5. Phase Six — Facilitator Coordination
6. Phase Seven — Encounter Ecology Mapping
7. The Permanent Prompt and the full 8-section Representative Construction
   Notes (RCN template v2.3)
8. The remaining deployment outputs: World Capsule Core, World Context
   Layer, Voice Configuration, Deployment Lexicon, Story Repository
9. The World Facilitation Brief
10. lpc's world-freeze gates per the Completion Standard's §B (machine
    gates, content review rounds, retrieval golden set, the Register-Bar /
    Transparency-Ground / File-Discipline reads)

## Self-governance — run this the same way the coordinator thread already
## did for Phase One, not a lighter version of it

- **One document at a time.** Don't start drafting the next phase before
  the current one has reached at least Approved to proceed.
- **Independent review, genuinely isolated.** Delegate each adversarial
  review to a fresh subagent (the `Agent` tool) that reads the governing
  framework and this world's own prior documents directly rather than
  trusting a summary — the same method that caught two fabrication-class
  HIGH findings in Phase One's own Round 1 review. Re-verify any HIGH
  finding yourself against source before applying a fix; don't take a
  review's word for a fabrication claim without checking it, and don't
  dismiss one as a tooling artifact without independent re-verification either.
- **Targeted recheck from round 2 on**, not a full re-review — same
  discipline, same reason (cost, and because a full re-review re-litigates
  ground the first round already covered).
- **Review rounds are capped.** Three rounds of substantial revision on the
  same document without it clearing is itself an unresolved tension — stop
  and escalate rather than run a fourth round.
- **No invented content.** No family, age, personal history, or anecdote
  for Datus beyond what Doc_01–09/World Profile/Decision Log actually
  establish. Every quote re-verified verbatim against the vendored source
  file before a record passes review — a "quotes verified" note is a claim
  to recheck, not a fact to trust.
- **git/PR workflow, matching the coordinator thread's own precedent
  (PRs #353, #355, #443, all merged under this project's CO-022
  self-disposition without a per-PR ask):** one branch and one PR per
  document/unit of work, off current `main`. Verify CI green and
  `mergeable_state: clean`, then merge it yourself once the document has
  actually cleared review and no escalation category applies — this is the
  same authority CO-022 already gives a build thread over its own
  documents; merging the PR is the mechanical last step of that
  self-disposition, not a separate ask. Log every disposition in
  `worlds/lpc/lpc_Decision_Log.md`, in the same style as its existing
  entries (dated, what was found, what was fixed, the disposition and why).

## Escalate — stop and report back, don't self-resolve

The four standing categories, exactly as `cic-build-cycle` defines them:

- **Representative identity/title.** Datus's identity is already decided
  (2026-09-15) and is not reopened by this thread. If something in Phases
  Two–Seven surfaces real tension with that decision (not just a stylistic
  quibble), that is exactly this category — escalate, don't quietly
  reinterpret the identity to fit.
- **Portfolio-level or cross-world decisions.** Anything decided for a
  reason external to lpc's own ecology.
- **Governance or methodology changes.** Anything that would change how
  the build process itself works — including any Framework or template gap
  this thread finds along the way (route it as a flagged finding, the way
  Phase One's own coach-handoff file routed portfolio-level methodology
  defects, not as a silent workaround).
- **Unresolved tensions the pipeline can't close on its own** — including
  the capped-review-round case above.

**Also always stop for, regardless of escalation category:**

- **Anything requiring real billed spend** — AWS Bedrock calls for live
  validation batteries (Part Eight's actual generation trials, the Table
  Readiness Round, M3 admission). Prepare the battery/protocol and ask
  first; do not run it unauthorized.
- **The registry entry and go-live.** `records/worlds/` registration and
  anything past it is explicitly the project lead's own act (lpc's own
  Decision Log already states this twice) — not this thread's to do, and
  not something to prepare a "just needs a state field" stub for either,
  per the reconciliation thread's own finding that no fleet precedent
  exists for an entry without one. Stop at world-freeze gates. Hand back.

## When done, or when stopped on an escalation

Report back to Mark (or to the Go-Live Pipeline Coordinator thread, which
watches for this) with: what reached Approved to proceed and where its
review artifacts live, what's still open, any escalation raised and why,
and real costs if any billed spend was authorized and run. Update
`worlds/lpc/lpc_Decision_Log.md` as the durable record — don't let this
thread's own conversation be the only place state lives.
