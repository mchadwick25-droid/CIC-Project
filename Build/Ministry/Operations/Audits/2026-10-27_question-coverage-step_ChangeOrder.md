# Change order: Question Coverage report at step B-7c — 2026-10-27

## 1. Name

A step is added to the world build, B-7c, Question Coverage report, after the Answer-the-Canon pass (B-7b) and before the four parities (B-8). The report must be filed and every finding dispositioned before the world freezes. This changes the build process, so it is a named change order and not a quiet edit (Build Process V2.0, Section 12).

It binds every world that has not started Phase B on 2026-10-27. Worlds already in Phase B or frozen are not bound and may run the report on request.

Approved by Mark on 2026-10-27: "Approve as drafted", on the draft shown to him as an Artifact. The step itself was chosen the same day as "New step B-7c, report-only."

## 2. Reasoning

- B-7b closes the blank cells of the canon. The Question Coverage design starts from visitors' own wording instead: 129 sub-questions with about 465 wordings, mapped against each world's records and the vendored Library (`Build/Ministry/Features/Question-Coverage/README.md`).
- Its first run found real gaps after the worlds were built: five honest limits that vendored text contradicts, three Jewish-visitor records with unguarded edges, and safety-adjacent records in don, witt and alx.
- The tool is read-only and needs no network and no model call: `Build/Ministry/Features/Question-Coverage/Tools/coverage_search.py`. It reads the world's records, so it cannot run before they exist.
- Findings already land in each world's `Open_Gaps_Tracking.md` by practice (alx OG-37 to 39, don OG-49 to 51). The process had no written rule for it.
- The design says a method change comes to Mark as a change order. A Library launch prompt once added a per-sub-question duty to Doc_02; that was a method change and was struck. This order adds nothing to Doc_02.

## 3. Before and after, verbatim

**Build Process V2.0, Section 6 step table, after B-7b.**

Before: no B-7c row; B-7b is followed directly by B-8.

After, new row: see the B-7c row in `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`.

**Completion Standard V1.4, Section B.**

Before: no requirement for a coverage report.

After, new paragraph at the end of Section B: "The Question Coverage report is saved for the world, with every finding dispositioned in its `Open_Gaps_Tracking.md`: closed by a grounded record, closed by an `honest_limit` record, or accepted with its reason. An undispositioned finding blocks the freeze. The report has no pass mark of its own. This binds every world that has not started Phase B on 2026-10-27."

**Build Process V2.0, Section 12, list of change orders.**

Before: the list ends with the Step 0 to 2 process and gate fixes entry.

After, new entry: "Question Coverage report at B-7c," with its source, reason and whom it binds.

Files touched: `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`, `Build/reference/method/CiC_World_Build_Completion_Standard_V1.4.md`, and the System Hub Decision Log.

## 4. What this change order does not do

- It adds no gate, no threshold and no engine command, and changes no record, schema or probe.
- It changes nothing in Doc_01 to Doc_10, including Doc_02. Library threads gain no new duty.
- It leaves B-7b and `gate_canon_coverage` as they are.
- It makes no model call and spends no money. Re-testing how a reader class responds still needs a named, capped live test from Mark.
- It does not touch worlds already in Phase B or frozen.
- It makes no edit to the build-cycle skill (`Build/reference/method/skills/cic-build-cycle/SKILL.md`). That skill sequences Doc_01 to Doc_10 and does not list the Phase B steps, so it carries no line to change. The draft shown to Mark named the skill as a file to edit; that was an error in the draft, and the order is narrower than the draft as a result.

## 5. Related files

- Form followed: `Build/Ministry/Operations/Audits/2026-10-27_canon-visitor-wording_ChangeOrder.md`.
- Feature: `Build/Ministry/Features/Question-Coverage/`.
