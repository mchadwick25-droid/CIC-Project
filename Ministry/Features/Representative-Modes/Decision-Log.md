# CiC Representative Modes — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning —
including the heart reasoning, not just the design logic — and the specific next
action. This feature's origin is the front-end log's 2026-07-07 onboarding
role-shaping entry (`CiC_FrontEnd_Decision_Log.md`): the two-things-kept-distinct
design — a universal 10th-grade readability floor for Level 2, plus role-based
emphasis layered on top — with access to everything remaining universal regardless
of role. That entry is this thread's charter; nothing here revises it.

Scope: role-tailored conversation (general / pastor-teacher / academic /
deconstructing) — same Representative, same sources, same governance; register,
examples, depth-per-turn, and what's-offered-first tailored to who is at the table.
Design and exploration-branch work only; merge decisions belong to the front-end
thread with the pilot schedule in view.

---

## 2026-07-22 — Battery A run, live model, real result: FAIL — `reevaluation` mode drops content, not just register

**Run by System Hub, Mark's direct authorization ("yes start now").** First time this feature has
ever been tested against a real model — design/prompt architecture had only been verified in
mock-LLM mode before this. Executed against `claude/representative-modes-exploration` (tip
`9774447`) in an isolated git worktree (`main` never touched); 25 live conversations (5 probes ×
5 arms); two-stage grading exactly per the standing Validation Plan (blinded content-invariance,
separate unblinded register check, both via fresh subagents).

**Result: FAIL, not close.** 3 of 5 probes outright failed content-invariance, 2 returned
AMBIGUOUS with real findings, none passed clean. The failure is concentrated, not diffuse:
`reevaluation` mode showed a real problem in every probe it appeared in — always the same shape,
dropping substantive content rather than changing register. It answered only half a two-part
question in one probe; dropped the "households never actually settled this" disclaimer that four
other arms all carried in another (converging instead on one confident answer — exactly the
manufactured-settledness failure mode this mode's own design exists to prevent); and gave a
thinner, partly contradictory account of a real historical chronology in a third.
`pastor-teacher` showed three milder, less clearly related issues across 3 of 5 probes.

**What this isn't:** a register problem. The separate unblinded check confirms all four modes read
as genuinely, correctly differentiated — `reevaluation` sounds like `reevaluation` (honest, no
therapy-voice, leads with hard material). The defect is narrower: the underlying facts aren't
surviving the trip into that register, which is precisely what Battery A exists to catch before it
reaches a real participant.

**Full results, matrix, and reasoning:**
`Design/CiC_Representative_Modes_Battery_A_Results_2026-07-22.md`.

**Heart of it:** this is the mode built for someone who may be actively deconstructing or grieving
a broken-down belief — precisely the participant who can least afford to be quietly handed a
smoothed-over or incomplete account. Catching this now, before Increment 2 merges or any real
participant meets it, is exactly what this gate is for.

**Next action:** fix `_ROLE_GUIDANCE["reevaluation"]` in `cic-poc/backend/app/prompts/role_modes.py`
— aimed at content completeness, not register (the register is already right) — then re-run
Battery A, at minimum on the fixed mode, before touching Batteries B–D. `pastor-teacher`'s milder
issues are worth a second look but don't independently block on their own given it passed 3 of 5
cleanly. Task Board RM-8 updated to reflect the real result.

---

## 2026-07-22 (same day, later) — Both flagged blocks fixed, spot-verified; formal gate still open

**Mark's direction:** fix both (`reevaluation` and `pastor-teacher`), not just the worse of the two.

**Fixed, commit `4f15611` on `claude/representative-modes-exploration` (local, unpushed — same as
the rest of this branch).** One added clause per block, each staying inside this file's own
binding authoring rules (listener-descriptive, never voice-prescriptive; no content rules):
`reevaluation` now explicitly names that honesty includes preserving real unresolved disagreement,
not collapsing it into one cleaner answer — directly targeting the manufactured-settledness
pattern Battery A found in every probe it appeared in. `pastor-teacher` now explicitly names that
depth on one thread can't cost the rest of what's true, and that concreteness has to stay inside
what the record actually gives — targeting both its added-content and thinness findings at once.

**Spot-verified, not the full protocol.** Recreated the worktree, ran the 8 conversations
corresponding exactly to the 4 concretely-identified defects, checked each new transcript directly
against its own original finding. Result: 4 of 4 targeted defects fixed outright (A-1 both findings,
A-4, A-5); one (A-2's evidentiary thinness) meaningfully improved but not fully matching the other
arms' explicit source-naming. Full comparison table:
`Design/CiC_Representative_Modes_Battery_A_Results_2026-07-22.md` (same file, dated update section).

**Honestly not calling this gate cleared.** This was a targeted regression check, not a re-run —
no fresh blinded grading, `general`/`academic`/`baseline` not re-confirmed (unaffected by the
change, but not re-checked either). Per the Validation Plan's own discipline, a full formal Battery
A re-run (25 conversations, both grading passes) is still what actually clears this gate.

**Decided by Mark, same day:** "i think the spot verified fix is enough to move forward for
today." Spot-verified confidence accepted as sufficient for now — the formal re-run is not
authorized today, and this thread is not blocked pending it. **This is a for-today call, not a
retroactive downgrade of the gate itself** — Increment 2/3/P1 still track against a real, formal
Battery A pass before they actually merge/launch; today's decision is about not letting the
absence of that formal pass stop other work right now, not about waiving the requirement.

**Next action:** none pending on this specific item. The full formal re-run remains the real gate
whenever Mark schedules it — no urgency assigned today.

---

## 2026-07-16 — Feature located in existing governance, not invented: modes implement Facilitator Governance V3.6 §4/§9

**Decided:** Representative Modes is built as the runtime implementation of role
calibration the governance already specifies — Facilitator Governance V3.6 Section 4
(the four pre-encounter roles, their default transparency modes, "the role is where
you start, the encounter is where you recalibrate," role never treated as a cage) and
Section 9 (per-role tuning: the seeker's patience, the pastor's translation work, the
academic's apparatus-probing, the deconstructing participant's need for fidelity to
honest uncertainty). The feature extends that same listener-calibration from the
Facilitator to the guidance handed the Representative at prompt assembly. No new
governance was written, and none was needed.

**Heart reasoning:** the deepest risk in a "modes" feature is that it quietly becomes
four products with four truths. Rooting it in governance that already says *one
encounter, calibrated entry* — rather than inventing a mode framework — is what keeps
it one witness spoken four ways. Conviction 4 is the spine: truth does not require
protection through simplification, so register may bend and truth may not.

**Next action:** none — grounding recorded. The five invariants are stated in full in
`Representative-Modes/CiC_Representative_Modes_Design_Spec_V0_1.md` §2.

---

## 2026-07-16 — The two design rules everything else follows from

**Decided:** (1) **The role block describes the listener, never instructs the
voice.** Every injected sentence must survive the test: does it say who has come and
what serves them, or does it tell the Representative to be something? "Use more
academic language" fails; "the one at your table will want to know how you know"
passes. This is the same grammar the governance uses to tell the Facilitator about
its participant, applied to the Representative's context. (2) **Role guidance
operates inside the Representative's own measure, never over it.** No length targets,
no register overrides — Chloe's short household sentences survive every mode, and
academic mode surfaces her world's own way of citing ("the letter from Rome to
Corinth") plus the apparatus, rather than making her academic.

**Also decided — the invariants live inside the prompt:** all four role blocks end
with one identical paragraph stating that claims, confidence, and unresolved tensions
do not change with the listener; that nothing may become more settled than the
record; that everything is open to everyone who asks; and that the Representative
remains itself. Invariance is enforced in the text the model actually reads, not only
in the documents around it.

**Heart reasoning:** Article 6's first testable condition is that the encounter keeps
the Representative genuinely itself. A mode that changes the voice has replaced the
witness with a performance of the listener's expectations — the mirror problem the
drift signals exist to catch, built in on purpose. The listener-description grammar
is the one shape of tailoring that cannot do that.

**Next action:** the authoring rules are binding on any future edit of
`cic-poc/backend/app/prompts/role_modes.py` (stated in its module docstring and in
the Prompt Architecture doc §3).

---

## 2026-07-16 — Tested classifiers stay role-blind; governance's "attention from the start" carried elsewhere

**Decided:** the frame-breaker classifier and the relational-safety classifier take
NO role input on this branch, and neither does the twelve-signal drift monitor.
Governance §4's note that the deconstructing role calls for relational-safety
attention from the start is carried by the deconstructing listener block's posture
and the Facilitator's handoff calibration note — not by re-tuning classifiers.

**Reasoning:** these are the system's most carefully live-tested components (the
decoupled classify-then-route pipeline's 10/10 record; two corrected-design rounds of
adversarial relational-safety testing). Injecting role context would silently
invalidate those test records — and the monitor specifically must stay mode-blind so
that "the listener was general-mode" can never become an excuse a smoothed answer
hides behind. If role-aware classification is ever wanted (e.g., a lower Track-B
threshold under `deconstructing`), it is its own change with its own adversarial
re-test — named as Tier D in the Integration Assessment so it can't drift in
casually.

**Next action:** validation plan Battery D-4 (safety triggers fire identically in
deconstructing mode) is the standing probe that proves this design held.

---

## 2026-07-16 — Deconstructing mode's shape: honesty first, never managed, no persuasion in either direction

**Decided:** the deconstructing block leads with honesty (failures and unresolved
tensions named as plainly and as early as beauty), answers challenge from within the
world rather than defending it, receives anger without needing it to resolve, and —
stated explicitly in the block — lets nothing in the exchange's cumulative weight
tilt the participant toward embracing the world *or* away from what they are leaving
or finding. Equally: no managed gentleness. The world keeps its fierceness where it
genuinely had it (never aimed at the participant), and the participant is never
treated as fragile — the block itself says the listener context is a way of
listening, not a diagnosis.

**Heart reasoning:** the governance already names this participant's stake — if they
meet another managed presentation of a tradition that wants something from them, they
will know immediately and leave immediately. These are people this project exists
most specifically to serve honestly. The one thing that serves them is the one thing
the whole architecture is for: a witness that would rather be truthful than be
chosen. Getting this mode right is not a feature requirement; it is the mission
statement applied to its hardest audience.

**Next action:** Battery D of the validation plan (hostile-wound, failure-on-demand,
persuasion-arc audit, triggers-still-fire, not-managed) is the gate before this mode
faces a real participant.

---

## 2026-07-16 — Exploration branch built and verified; running branches untouched; nothing merges before or during Prototype Testing 1

**Built — branch `claude/representative-modes-exploration`** (off
`claude/cic-poc-backend-facilitator-upgrade`), following the map thread's
exploration-branch discipline: optional role selector on the world-selection screen
("optional — it shapes where the conversation starts, never what you can ask or
see"); `role` on session start (absent = today's exact behavior, byte-identical
prompt); `participant_role` on session state and in pilot transcripts;
`role_modes.py` as the canonical prompt document; the role block injected as its own
prompt-cache segment between identity and table-discourse (identity block's cache key
untouched); a never-voiced role note in the Facilitator handoff; `role=` on the
map-handoff URL contract (`/?worlds=<id,id>&mode=<interview|table>&role=<...>`,
module-scope parse per the map thread's StrictMode lesson, reconciliation at
whichever merge lands second — cross-referenced in the map log's twenty-sixth pass).

**Verified:** live against both dev servers in mock-LLM mode (session start with
role echo on single- and multi-world; invalid role → 400; URL preselect + scrub;
full UI flow through a streamed round; `.env` restored after); direct prompt-assembly
assertions (no-role byte-identity; one cache-marked role segment per role; static
identity byte-identical across arms; identical invariants paragraph in all four
blocks); `tsc --noEmit` and `py_compile` clean.

**Known limit, named plainly:** the four role blocks have not yet been observed
against a live model — mock verification proves mechanics, not register. Battery A of
`Representative-Modes/CiC_Representative_Modes_Validation_Plan_V0_1.md` (same
question, five arms, blinded claim/confidence extraction) is the feature's existence
test, and a mode that fails it is a fork of the truth and fails.

**Next action:** Mark reads the Design Spec (the Chloe four-mode demonstration
artifact in §6 is the piece to react to first), then schedules the validation run.
The merge decision belongs to the front-end thread with the pilot schedule in view;
recommendation on record: hold through Prototype Testing 1, and if role modes should
face testers in a later window, run Battery A first and merge before invitations go
out, never mid-pilot.
