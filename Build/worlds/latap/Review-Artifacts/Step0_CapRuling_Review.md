Simulated review — informational only, not an Article 31 substitute.

# Step 0 Movement-Scope Confirmation, latap — Cap-ruling targeted review (IN PROGRESS, NOT A VERDICT)

**Reviewer model:** Opus 5.5
**Drafter model:** Sonnet 5.5
**Reviewer agent:** cap-ruling review worker, latap Step 0 (isolated; no part in the change order or PR #1304)
**Drafter agent:** latap Step 0 quote-fixes worker (PR #1304)
**Round:** 8 (cap-ruling targeted review; by Mark's ruling of 2026-10-29 it does not count toward the cap of three)
**Truncation check, method 1:** replay of the 21 change-order edits on the pre-PR file, compared byte for byte with the merged file
**Truncation check, method 2:** character-level difflib opcodes of the pre-PR and merged files, each changed region tested for containment inside one edit's old span

**Ruling.** Mark ruled on 2026-10-29 that the 24 check-8 quotation findings in Step 0 are fixed by a named change order (`Build/Ministry/Operations/Audits/latap_Step0_QuoteFixes_ChangeOrder_2026-10-29.md`), nothing else in Step 0 is touched, and one targeted Opus review follows that does not count toward the cap. If it clears, Step 0 is approved to proceed.

**Status: in progress, not a verdict.** Work stopped at a usage checkpoint. Step 0 has not cleared under this review yet, and it is not approved to proceed by this file.

## Verified so far

### Diff against the "nothing else touched" rule — verified

Document: `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md`, `d5ef04a8d^1` against `d5ef04a8d` (PR #1304). The pre-PR file is identical to the file at `987e9c147` that the change order's line numbers use, and `main` has not changed the file since.

- Method 1: all 21 old strings occur exactly once; applying the 21 edits to the pre-PR file reproduces the merged file byte for byte.
- Method 2: 83 changed character regions, none outside an edit's old span. The 14 changed lines (16, 43, 59, 61, 71, 75, 83, 98, 106, 110, 140, 167, 182, 197) are exactly the lines the table names.

Result: only the 21 listed spans changed.

One note, not blocking: E18 adds a comma inside the quotation ("deinde fecit alterom,"). The source has that comma (TEI line 7395), so the quotation is now closer to the source. The change order's wording "leaves the Latin words unchanged" is true of the words; the comma is new.

### The 24 rows

| # | Status | Note |
|---|---|---|
| 1 | not yet | tree and history search for the phrase still running when work stopped |
| 2 | verified | Round1 review line 248 holds all three phrases; line 253 repeats the third |
| 3 | verified | Hub log line 5569 heading, verbatim |
| 4 | verified | lpc `Source_Registry.md` line 42, verbatim |
| 5 | verified | line 42; ellipsis omits "(Doc_01 §2, §6) —"; source has *forging* in italics |
| 6 | not yet | `.docx` Section B paragraph not yet opened |
| 7 | verified | corpus map lines 96–97, verbatim |
| 8 | verified | lines 164–166; ellipsis omits the parenthesis and dash |
| 9 | not yet | absence search and the claim on the evidence (task 3) still open |
| 10 | verified | line 848 and staging line 392; [t] shown correctly |
| 11 | verified | lines 954–955, verbatim |
| 12 | verified | pahc Apology record; the quoted words sit at lines 29–30, inside the note at 27–30 |
| 13 | verified | same file line 16 |
| 14 | verified | pahc `world_core` lines 91–93; ellipses also omit "are" before "unknown"; meaning kept |
| 15 | verified | ijc record lines 40–41 |
| 16 | verified (new text) | current map lines 398–405 and staging lines 60–69 match the new text; the claim that the old capitalised wording was a superseded version is not yet checked against history |
| 17 | not yet | archive.org text not yet checked |
| 18 | verified | Arnobius TEI lines 7436–7437; correct once `<lb n="10"/>` is removed |
| 19 | verified | npnf203 lines 39881–39885 print "Irenæus" |
| 20 | verified | npnf203 lines 41051–41053 print "Cæsar" |
| 21 | verified | Lactantius TEI lines 7395–7396 "alterom,"; apparatus line 7423 "deinde fecit alterum]" |
| 22 | verified | `_fleet` record line 32 |
| 23 | verified | Round1 review line 359 |
| 24 | verified | corpus map lines 874–875 |

Verified 20 of 24 (row 16 for its new text only). Not yet: 1, 6, 9, 17, and the history claim in 16.

## Not yet done

- Task 3: whether finding 9's claim (the four original authors' texts do not mainly describe worship practice) stands on the document's own evidence.
- Task 4: a full pass over every single-marked quotation for a named file and lines, and over every double-marked quotation for a vendored source.
- Task 6: the remaining check-8 flags. **Discrepancy to resolve first on resume.** `python -m engine.m10.cli handoff latap`, run in a sparse worktree of `main` at `59692b7a5` with `cic/texts` linked to the main checkout (whose `cic/texts` matches `main`), reported 31 check-8 findings, not the 7 the change-order worker reported. Among them are English phrases such as 'opened the whole enterprise in 197' and 'his surviving work totals just under half a million words', German ('Also kann er nicht vor c. 260 geschrieben haben', 'Der Montanismus des Redaktors ist m. E. unverkennbar') and French ('ne sont pas antérieurs à 260', "C'est donc entre 260 et 313"). It is not yet known whether this count comes from the sparse checkout (missing project-text pool files such as `cic-website/data/world-census.json`) or is real. Until that is settled, this review cannot say whether Step 0 has quotation defects left.

## Verdict

None yet. In progress.
