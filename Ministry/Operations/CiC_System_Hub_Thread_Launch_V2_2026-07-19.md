# Launch prompt — System Hub V2: reconciliation and discipline

Paste this into a fresh thread to succeed the current System Hub thread. Its job is narrower
and more disciplined than the thread that produced it: fix the specific consistency gaps a
systematic audit found today, and do it in a way that doesn't repeat today's own near-misses.

## The rule that overrides everything else below

**The build process is untouchable.** The project's level structure (`L1-Foundation`,
`L2A/B/C/D-System-*`, `L3A/B/C/D-*-Methodology`, `L4-Templates`, `World-Builds/`,
`Project-Reference/`) and the construction/review cycle itself (`cic-build-cycle` and its
sibling indexing skills) are never moved, renamed, restructured, or reorganized — not even as
a suggestion. **Fixing a stale citation, a wrong version number, or a missing propagation is
in scope. Reorganizing where anything lives is not**, unless Mark explicitly asks for that
specific change. If you ever discover you've touched, damaged, or altered the structure itself
— even accidentally — say so immediately, before doing anything else.

## Why this thread exists

A 10-agent systematic audit of L1–L4 and all five live world builds ran 2026-07-19
(`Ministry/Operations/CiC_L1-L5_Systematic_Audit_2026-07-19.md` — read this in full before
touching anything). It found real, specific, checkable drift: decisions made but never
propagated to the documents that cite them, deployed code that outran its own build record,
and self-reported compliance numbers that were wrong when independently recounted. This
thread's job is to close those specific gaps — not to re-audit, not to redesign, not to expand
scope beyond what's listed below.

## Discipline this thread must hold that the prior one had to learn mid-session

- **Check `git worktree list` before doing anything.** Multiple sessions may be running
  concurrently against this same repo. Today's file-loss incident happened during exactly that
  condition. Know what's live and locked before you start.
- **Before treating anything as "lost" or "unrecoverable," check git history yourself** —
  `git log --all --full-history` for the filename, and look for orphan/dangling safety-snapshot
  commits (`git log --all --oneline` won't show them; you may need to search commit messages
  directly). A prior thread today declared a real, recoverable trove permanently lost because it
  only checked its own published Artifacts, not git. Don't repeat that.
- **Before trusting a "canonical" document, check whether the actual decision already exists
  somewhere unmerged.** `CiC-L1L3-Foundation` is a live worktree/branch that the Change Orders
  Register says already carries real governance decisions (a nine-world portfolio, Early-Communal
  deprecation, Constitution 2.2→2.3, Facilitator-Governance V3.4→V3.6) "NOT YET PROPAGATED to
  the canonical project folder." **Check that branch's actual content before hand-editing any
  canonical L2 document to match what you believe is current** — the fix may already exist and
  just need reviewing and merging, not re-deriving.
- **Before trusting that a world's build record reflects what's actually deployed, diff them.**
  Today found a live Representative's Permanent Prompt (Bethlehem Circle/Albina) had drifted
  from its own tested, reviewed World-Builds copy, undocumented. Check `cic-poc/backend/data/`
  against `World-Builds/` for any world you touch before assuming either one is current.
- **Any "X/Y compliant" or "N of M pass" claim you write into a decision log, cross-world
  finding, or task board must state how it was checked** — automated script, independent
  recount, or self-report only. Today found three self-reported counts that were wrong when
  actually recounted. Don't add a fourth.
- **Commit in logically separate commits once Mark has confirmed scope**, don't bundle
  unrelated fixes. Ask before pushing to `origin`.

## The specific work, in priority order

### 1. Write the safety-mechanism confirmation back into House-Church's own record
The Acute-Distress/Harmful-Dynamic mechanism (`cic-poc/backend/app/graph/nodes.py`,
`main.py`, `state.py`, `prompts/facilitator_prompts.py`) is real, live-tested, and wired into
both message endpoints — confirmed directly in code, not on claim. It was built and verified
2026-07-13, four days after House-Church's own last safety record (2026-07-09) said this
mechanism didn't exist and the world shouldn't ship without it. **Write a confirmation entry
into `World-Builds/01-Post-Apostolic-House-Church/`'s own testing record** stating the
mechanism now exists, where, and what was verified — so the world's own build history stops
contradicting reality. Fix the stale `state.py` docstring on `relational_safety_deescalation_count`
while you're in that file (one line, matches code that's already correct).

### 2. Check `CiC-L1L3-Foundation`, then reconcile the canonical L2 registry
Read what CO-023/CO-024 and the branch actually contain. If the nine-world portfolio decision,
Early-Communal deprecation, and related governance updates are sitting there complete, bring
them into `CiC_L2C_Phase_Status_V1.2.docx`, `CiC_L2A_System_Level_Map_V1.6.docx`,
`CiC_L2A_Clean_File_Structure_V1.1.docx`, and `CiC_L2D_System_Operations_V1.2.docx` so they
describe the real, current nine-world project instead of the stale five-world one. Confirm with
Mark before merging the branch itself if that's what it takes — this task is about the canonical
documents being accurate, not about resolving whatever else might be on that branch.

### 3. Decide and close the Bethlehem Circle prompt drift
Either bring `World-Builds/Hieronymian-Ascetic-Literary/`'s Permanent Prompt in line with
what's actually deployed and log the change, or revert the deployed version to the tested one.
Whichever way Mark calls it, re-run adversarial testing against the final version before treating
it as settled again.

### 4. Fix the confirmed cross-document citation/version drifts
Each of these was independently confirmed by the audit, not just suspected:
- `L3C-Representative-Methodology`'s Construction Framework still cites the anti-fabrication
  rule as "Article 3; TC-001" — Facilitator-Governance V3.6 already corrected this to "Article
  28, Anti-Fabrication Prohibition." Update L3C to match.
- Forces Framework (L3A) says the construction sequence has eight steps; it has ten. Fix the
  framing sentence; the six integration points it names are individually still correct.
- Ecology lens naming has drifted between Construction Framework/Forces Framework ("Human/
  Community/Boundary Ecology") and the Formation World Template's actual current vocabulary
  ("Formation Ecology," "Boundary Structures," "Organizational & Ministry Ecology"). Reconcile
  to one vocabulary — the Template is supposed to be authoritative here.
- Archive `CiC_L3D_Facilitator_Governance_V3.4.docx` — confirmed fully superseded by V3.6,
  nothing treats it as current.
- `The Table Design Document V2.3` says "has not yet been deployed or tested" — its own
  companion document proves otherwise with a dated fix and a real code reference. Refresh the
  readiness status.
- `Representative_Permanent_Prompt_Template.txt`'s internal header (2.1) is stale against its
  own changelog (2.2) — bump it, and give the file a version number in its filename like every
  sibling template has.
- If/when Mark approves V3.7_PROPOSAL for merge: it fixes Section 10's stale signal count but
  not the dependent count in Section 14, which its own fix makes worse. Fix both together, not
  separately.

### 5. Build the lexicon compliance checker, run it, close the mechanical gaps
A small script (Python or PowerShell) that scans a world's `Lexicon-Chunks/` for the five
Article 17 confidence-vocabulary terms and Author-Gravity/mediation-risk language, and outputs
a per-file pass/fail table. Run it against House-Church, Desert-Monasticism, and Bethlehem
Circle. For Desert-Monasticism specifically, the audit diagnosed the exact root cause (Doc_06's
"Key Sources: Doc_02 §X.X" pointer field gets dropped during chunk extraction, uniformly, on
all 9 chunks) — the grounding citations already exist upstream, this is a copy-forward fix, not
new research. Same likely applies to House-Church and Bethlehem Circle; confirm before assuming.
Log the actual verification method (script name, date run) next to any new compliance number.

## What NOT to do
Don't re-run the audit. Don't expand into Ministry/Branding, Funding, or any other workstream —
that's other threads' territory. Don't reorganize any part of the build-process structure even
if a cleaner layout seems obvious. Don't merge `CiC-L1L3-Foundation` wholesale without checking
with Mark first — read it, confirm what's actually on it, then ask before merging.

## Standing reference
- `Ministry/Operations/CiC_L1-L5_Systematic_Audit_2026-07-19.md` — the full findings this
  thread is closing out.
- `Ministry/Operations/CiC_System_Hub_Decision_Log.md` — this session's full record, including
  the file-recovery incident and the worktree inventory.
- Log every real decision and fix in the same decision log, continuing its dated-entry format.
