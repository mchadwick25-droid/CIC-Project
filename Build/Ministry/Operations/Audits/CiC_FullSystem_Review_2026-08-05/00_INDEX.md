# CiC Full-System Review — Index

Dispatched 2026-08-05 at Mark's direction: four independent Opus review passes, each
from a distinct angle, run in parallel overnight. Each followed
`Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md` (source-level
verification, P0/P1/P2 severity, a genuine bottom-line verdict) and built on the prior
`CiC_Redesign_Research_2026-07-25/` audit series where directly relevant, rather than
re-deriving ground already covered there. All four completed and are read in full below —
this index summarizes; the actual evidence, quotes, and file citations are in the reports
themselves.

| # | File | Angle | Bottom line |
|---|---|---|---|
| 01 | `01_Accessibility_Engagement_Review.md` | Ease of use, clarity, plain language, story vs. dry info | Not yet accessible to a non-academic — but the gap is in the *delivery layer* (unglossed jargon leaking into hover/aria labels, census prose breaching the project's own reading-level floor, 0 of 6 built worlds carry visible sources), not the underlying writing quality, which is genuinely strong where it's been authored with care. |
| 02 | `02_Academic_Rigor_Review.md` | Would a seminary professor trust this | **"I like it, with two specific caveats — and I'd want one thing before I put my own name near it."** Best-verified: ~60 specific historical/bibliographic claims checked, one likely error found. The internal review discipline is real and unusual. Two caveats: a provenance-field data error (50 rows), and uneven depth across worlds (Imperial-Juridical is a first draft next to Post-Apostolic/Hieronymian). The one thing missing: a real outside scholarly reader — the Framework already names this as a freeze gate, open since July 8. |
| 03 | `03_Engineering_Design_Review.md` | Would an engineer call this well-built | The evaluation/testing instruments are real and unusually disciplined (a genuine held-out probe set, deterministic zero-API retrieval harness, replay-parity assertions) — **but none of them is a wired gate**, so real regressions still ship. **One P0 already fixed tonight** (see below); three more P0s open, including a documentation file that's wrong in nearly every particular. |
| 04 | `04_Participant_Readiness_Review.md` | Readiness per persona (General / Re-evaluating / Pastor-Teacher / Academic) | Most ready: **General** — a complete, honest, three-click path. Least ready: **Pastor/Teacher** — no entry point, no takeaway. Highest *risk*: **Re-evaluating** — best design writing in the repo, best shipping content, **weakest safety floor**, and recruited by name in the marketing copy. Single biggest lever: finish the ending screen — it's where the human-support path, per-world reading, and a takeaway artifact all belong, and it's currently one sentence and an email address. |

## Two findings needed same-night action, not morning review

Both surfaced independently, from different angles, within the same review pass.

**1. Security (Engineering review, P0-1) — fixed and shipped tonight.** The frontend
catch-all route (`cic-poc/backend/app/main.py`) joined an attacker-controlled URL path onto
the frontend directory without resolving it, then trusted `.is_file()` — a path traversal.
Verified directly (not just read): `Path("/a/b") / "../../../etc/passwd"` reads straight
through with this exact join pattern. The container runs as root with `ANTHROPIC_API_KEY`
and other secrets as env vars, so an unresolved join here could reach `/proc/self/environ`.
**Fixed**: the candidate path is now resolved and required to stay under the frontend
directory before being served; verified the exploit path now correctly fails and legitimate
files still serve normally. Committed and pushed to `main`
(`cic-poc/backend/app/main.py`). **If cic-poc has been deployed with this code at any
point, rotating `ANTHROPIC_API_KEY` and any other secrets in that environment is worth
doing regardless of whether exploitation can be confirmed** — this was not checked here and
is a decision for Mark, not something taken unilaterally.

**2. Safety (Participant Readiness review, P0-1) — flagged, NOT independently acted on.**
The shipped acute-distress response templates (A1/A2) instruct the Representative: *"Do
NOT: name any resource, hotline, or organization. Do NOT suggest a course of action."* The
governing document, Facilitator Governance V3.6 §12, requires the opposite: *"redirect with
honesty… whatever redirection toward human support is appropriate."* The project's own
internal battery graded this MARGINAL twice, called it "a hard pre-freeze fix item," then
closed it by citing a document — `CiC_W1_Phase5_RelationalSafety_LiveAdversarialTest_
CorrectedDesign_Round1/2.md` — that the reviewer confirmed does not exist anywhere in the
repository or git history. This one was **not** fixed tonight: it's a live policy/prompt
decision about how the system responds to someone in genuine crisis, and that call belongs
to Mark, not to an unattended pass. Full detail, including the exact contradicting text
from both sides, is in report 04 §on this finding.

## Everything else

The four reports carry a combined 15 P0s (2 of which — the two above — got the same-night
treatment described above; the rest are build-quality, consistency, and completeness
findings, not live-risk items), plus roughly 35 P1s and 20 P2s across all four angles, each
with a specific file reference and a concrete fix. Read the individual reports for the full,
verified detail — this index is a map, not a substitute.
