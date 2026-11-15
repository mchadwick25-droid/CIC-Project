# Live-surfaces sweep — independent review, round 2

Reviewer model: Opus
Round 2, targeted recheck
Scope: `git diff HEAD~1 HEAD` (e8064a6e) against the twelve findings in `R1_review.md`, with `R1_changes.md` section 6 read as claims. Read and grep only.

## Verdict: PASS

All twelve findings are fixed. The fixes introduce no substantial new problem. One minor note is below; it needs no change before merge.

## Findings 1-12

1. **FIXED.** Cyprian Pars III line 9 now reads "three indices: a scriptural index ..., a word/phrase index (..., the largest of the three)". Only the word index is called largest.
2. **FIXED.** ijc Source_Registry row 30 now reads "Title confirmed; publisher, series and year added at that check; not independently re-collated ..., so B, not A". Moved_Notes' "after" block matches it.
3. **FIXED.** `_library_header_end` now finds a boxed header's closing rule at any depth and never falls back to the first blank line. The new test puts a hit on line 134 of a header longer than 120 lines.
4. **FIXED.** The vonsoden_prosopographie Content note now points to `vonsoden_ketzertaufstreit-rom-karthago-deu_1909.txt`. ROUTE_CUES now include `not yet ... vendored` and `flagged for a future round`, and a test covers them. The stale REGISTRY.yaml note is carried in Open-Gaps 280. (Section 6 item 4 says it is "listed below". It is not listed below in that section, but Open-Gaps 280 tracks it, and that is what counts.)
5. **FIXED.** A grep of the first 60 lines of every `cic/texts/*.txt` finds exactly the thirteen files named in section 6 and in Open-Gaps 280.
6. **FIXED.** Open-Gaps 280 now has the bullet "support.html needs a content refresh before it is linked again". Moved_Notes points to it.
7. **FIXED.** New tests cover: the OCR exclusion, the "Mark's own" + gospel exclusion, Source-line `pr-ref` and `builder-thread`, REGISTRY `evidence`/`date_added`/`supplied_by` protection, and the one-line change-history rule (`rights: CORRECTION per Mark` gives REWRITE). The `- date_added:` test does tell the fixed code from the bug: under the old code, line 8 would have been PROTECTED. The "each tested" claim now holds.
8. **FIXED.** Links, `[ ]`/`[x]`, code spans and `\[` are stripped before brackets are counted. Depth resets at a heading, a blank line and `---`. A test is added.
9. **FIXED.** For the `- key:` form, `key_indent` is now indent + 2, so an entry's other fields are scanned again.
10. **FIXED.** (a) `_CODE_SPAN_WITH_DATE` now requires a non-digit, non-hyphen character in the span, and a test shows that a bare `` `2026-09-25` `` is still flagged. (b) `builder-thread` now counts as data on the Source line only. The new `dated-fix` pattern matches `evagrius_praktikos_dysinger.txt:7` ("(Fixed" at the end of the line).
11. **FIXED.** The cue is now `has not yet been (?:\w+ly )?(?:re-)?(assessed|opened|...)`, and a test uses the witt phrasing.
12. **FIXED.** (a) quote_verbatim.py:110 now reads "Two of the three patterns (the source-side ones)". (b) Didymus now reads "No Greek characters survive in / this file's OCR", which fits the Unicode-census sentence after it. (c) Pars III keeps the plain fact: "Closely related material from the same edition is vendored separately". Keeping session ids in the other headers' Source and Provenance lines, as INTAKE.md asks, is a fair answer to the "treat them the same" choice.

Line counts: every `cic/texts/` hunk in this commit keeps its size (-4,9 +4,9; -42,8 +42,8; -6,7 +6,7). No body line is touched.

## New problems from the fixes

None substantial.

**Minor note (no change needed now): a boxed header with no closing rule now runs to the end of the read.** `chronica-minora-liber-genealogus_mommsen1892.txt` opens with a rule and has no second one. Its real header ends before line 60. Under the new `_library_header_end`, the whole 256 KB read counts as header. Before the fix, the header was one line long, so this is not a regression. But it means the header rules are now applied to the edition's own OCR body. A grep of that range today finds no cue or date matches, so the reported count holds, but a future body hit would look like a header defect. If this file is touched later, stop at the first blank line after the header block when no closing rule follows, or give the header its closing rule.

The new global `dated-fix` pattern also matches a few existing non-Library lines (for example cic/texts/README.md:2483, cappadocian BUILD_LEDGER:811, don_Decision_Log:425). Each of those lines already carries a `round N` match, so section 4's counts are not visibly moved. It is report-only for files this change does not edit.
