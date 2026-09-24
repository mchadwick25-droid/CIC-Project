# Decision Log — Live-Surface-Cleanup

Append-only, per `CLAUDE.md`. This log is the destination for provenance
history removed from a live/canonical surface (`CLAUDE.md`, "Keep the
live/canonical surfaces clean") by the Live-Surface-Cleanup program:
ruling numbers, review rounds, reviewer names, "Mark's ruling"/"per Mark"
attributions, and dated change narration that `tools/check_live_commentary.py`
classifies as REWRITE. One entry per removal, citing what was removed,
where it moved from, and the PR that moved it. The fuller reasoning for
each PR lives in that PR's own body; this log is the pointer a removed
line's provenance is still findable from, per the launch brief's own rule
("Every removed line must be findable there, or in a gaps file,
afterwards").

No entries yet: Step 1 PR A builds the classifier only and edits nothing
in a live surface. The first entries land with Step 2 PR C/D.

---

**Entry 1 — `engine/m1/rendering_fidelity.py`, `engine/m1/tests/test_rendering_fidelity.py` (Step 2 PR C).** Removed: a ruling-number citation to R34 ("Mark, 2026-09-23 P3 relaunch thread") attached to the translate-not-summarize standard the module docstring quotes; a citation to R35 ("R35's build-quality principle") attached to the reason this gate is report-only, not yet registered in `gates.GATES`; a "(reviewer verdict on item 4, 2026-09-23)" attribution on the birth-condition explanation; a "Per R33," citation on the no-per-record-scope-carve-out statement; the specific date on the Bedrock-rate-limit incident that motivates the module's own retry logic; and, in the test file, an "(R33/R35: ...)" citation on a comment explaining the same no-carve-out rule. In every case the underlying reason stayed, rewritten in plain present tense; only the ruling number, attribution, and/or date moved here. `REPORT_PATH`'s own dated filename (line 75, `rendering-fidelity-report-2026-09-23.json`) is untouched — a real, functional output path the program writes to, not commentary, so it isn't a REWRITE case even though the classifier's `iso-date` pattern matches it.

**Entry 2 — `engine/m4/grounding_net.py`, `engine/m4/tests/test_grounding_net.py` (Step 2 PR C).** Removed: the specific sign-off date on the Live-Generation Design promotion in the module docstring; the specific date on when the "residual `[[...]]`" comment was last updated (the underlying observed fact — one unclosed `don.dw.room-for-diss` tag left by a cut generation stream — stays); a "M-1 (witt go-live adversarial review, 2026-09-20)" finding-ID citation on the scaffold-exemption fix, in both the module and its test (the bug description and fix stay, fully self-contained without it); an "R27-A item 1 (Decision-Log.md Entry 55, 2026-09-23)" citation and a "moved here per item 2's own build order" note on the paragraph-split regex; an "(R27-A item 2, Decision-Log Entry 55)" citation on the `paragraph_coverage` layer's docstring; an "(Entry 55's own recommendation - coverage only...)" citation on the preceding-paragraph inheritance rule (kept "coverage only; see inherited_from_preceding below" — a real code cross-reference, not provenance); and, in the test file, three dated section-header comments ("the three narrowings (2026-08-23)", "truncation (2026-09-19)", a "2026-09-19 rzg+don Table round" date on a real-case citation) and the same "R27-A item 2 (Decision-Log.md Entry 55, 2026-09-23)" citation on the paragraph-coverage test section header. `engine/m4/grounding_net.py:152` ("the opening quotation mark's own offset") is untouched — a false positive of the classifier's `marks-word` pattern (a literal quotation mark, not "Mark" the project lead), not a REWRITE case.
