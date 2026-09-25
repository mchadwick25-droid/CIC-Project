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

Step 1 PR A built the classifier only and edited nothing in a live
surface. The first entries below land with Step 2, per surface: `engine/`
(Step 2 PR C) first, then `cic-website/`, `cic-poc/frontend/`, and
`cic/corpus-map/` (a separate parallel thread's own numbering, each
surface starting its own "Entry 1"). PR D (identifier renames, originally
planned for `engine/`) was dropped from scope entirely after PR C merged
- working code stays as-is rather than renaming for cosmetics - see the
program's own closing disposition below.

---

**Entry 1 — `engine/m1/rendering_fidelity.py`, `engine/m1/tests/test_rendering_fidelity.py` (Step 2 PR C).** Removed: a ruling-number citation to R34 ("Mark, 2026-09-23 P3 relaunch thread") attached to the translate-not-summarize standard the module docstring quotes; a citation to R35 ("R35's build-quality principle") attached to the reason this gate is report-only, not yet registered in `gates.GATES`; a "(reviewer verdict on item 4, 2026-09-23)" attribution on the birth-condition explanation; a "Per R33," citation on the no-per-record-scope-carve-out statement; the specific date on the Bedrock-rate-limit incident that motivates the module's own retry logic; and, in the test file, an "(R33/R35: ...)" citation on a comment explaining the same no-carve-out rule. In every case the underlying reason stayed, rewritten in plain present tense; only the ruling number, attribution, and/or date moved here. `REPORT_PATH`'s own dated filename (line 75, `rendering-fidelity-report-2026-09-23.json`) is untouched — a real, functional output path the program writes to, not commentary, so it isn't a REWRITE case even though the classifier's `iso-date` pattern matches it.

**Entry 2 — `engine/m4/grounding_net.py`, `engine/m4/tests/test_grounding_net.py` (Step 2 PR C).** Removed: the specific sign-off date on the Live-Generation Design promotion in the module docstring; the specific date on when the "residual `[[...]]`" comment was last updated (the underlying observed fact — one unclosed `don.dw.room-for-diss` tag left by a cut generation stream — stays); a "M-1 (witt go-live adversarial review, 2026-09-20)" finding-ID citation on the scaffold-exemption fix, in both the module and its test (the bug description and fix stay, fully self-contained without it); an "R27-A item 1 (Decision-Log.md Entry 55, 2026-09-23)" citation and a "moved here per item 2's own build order" note on the paragraph-split regex; an "(R27-A item 2, Decision-Log Entry 55)" citation on the `paragraph_coverage` layer's docstring; an "(Entry 55's own recommendation - coverage only...)" citation on the preceding-paragraph inheritance rule (kept "coverage only; see inherited_from_preceding below" — a real code cross-reference, not provenance); and, in the test file, three dated section-header comments ("the three narrowings (2026-08-23)", "truncation (2026-09-19)", a "2026-09-19 rzg+don Table round" date on a real-case citation) and the same "R27-A item 2 (Decision-Log.md Entry 55, 2026-09-23)" citation on the paragraph-coverage test section header. `engine/m4/grounding_net.py:152` ("the opening quotation mark's own offset") is untouched — a false positive of the classifier's `marks-word` pattern (a literal quotation mark, not "Mark" the project lead), not a REWRITE case.

**Entry 3 — `engine/m1/quote_verbatim.py`, `engine/m1/tests/test_quote_verbatim.py` (Step 2 PR C).** Removed throughout both files: "RULED (Mark, 2026-09-22, ...)" attributions on the module's core editorial-tolerant/no-fuzzy-score rule and on each of its three sequential rulings (verse_number allowed, a nested-mark case not allowed, two #403-triage patterns folded into existing classes); "FOURTH ROUND"/"FIFTH ROUND"/"FIFTH ROUND, REVIEW ROUND 1" round labels and their dates on the apparatus-class and edition-level-apparatus design history; "R33"/"R28"/"R35" ruling-number citations throughout (the gate-level note-body fallback superseding an earlier per-record `source_note_id` field; the `_REQUIRED_VERIFICATION_STATE` gate; the endnote-sequence apparatus kind; the gate registration section header); dated section-header comments in the test file ("apparatus (fourth round, 2026-09-23)", "note-body fallback (R33, 2026-09-23)", "gate registration (item 3, R33/R35)"); and "Mark's second/third ruling" attributions on three test docstrings. In every case the underlying rule or reason stayed, including the two places (lines ~11 and ~150 of the module) that quote the project lead's own words directly on the no-per-record-field principle — kept as "stated directly by the project lead," since a direct quotation needs to say whose words they are; only the ruling number, round label, and date moved here.

Two deliberate non-edits in `quote_verbatim.py`: lines 141-142, a "(see Rulings-Pending Pending 2 / Decision-Log)" cross-reference — kept, because it points a reader to a genuinely different, still-open tracking item (why one specific record is downgraded to `verified-via-authority`), not to this design's own decision history; and `REPORT_PATH` (line 625, `quote-verbatim-report-2026-09-22.json`) — a real, functional output path, not commentary, same reasoning as Entry 1's `rendering_fidelity.py` case.

**Entry 4 — `engine/m1/gates.py` (Step 2 PR C).** Removed: dates on the world_front-referential-gate addition, the voice-craft-prompt-budget gallic/witt trims and gallic's earlier partial fix, the gate's own admission-from-experimental date and its corpus-check date, the ATTRIBUTION_FIELDS/PERSPECTIVE_FIELDS relocation dates, the Form-1/3 measurement date and hand-check date, the CiC_Cross_System_Analysis_Tracking.md and CiC_Register_Bar entry dates, the world_front-gates-design approval date, the quote-mark-fidelity and quote-verbatim gate registration dates, and the two already-shipped-defect commit dates (kept the commit hashes themselves - `fbb6557`, `763c48d` - as real, findable references, only dropping the date attached to them). Removed attribution framing: "R11 (Rulings-Pending.md, ruled (a) 2026-09-21; Decision-Log.md Entries 21-24)" on the retrieval-negatives-structured split (also fixed the matching runtime finding-message string, `"...R11's split retired this field"` → `"...this field is retired"` - a builder-facing diagnostic, not participant-facing, but the same leaked-citation problem); "Mark's standing quote ruling" on the world_front quote-mark-fidelity design note; "Mark's own direct decision" on the mode-3-claim-fidelity design note (kept as "a direct decision from the project lead," since the paragraph needs to say whose decision it records); "R35 (Mark, in his own words)" on the quote-verbatim gate-registration comment (kept the quote itself, attributed to "the project lead").

Five deliberate non-edits, all illustrative rather than decorative: lines 644/646/650, three real quoted examples of the exact leaked build-attribution text (`"the project lead's 2026-08-21 ruling accepts this"`, a raw `"2026-08-21"` next to an attribution, `"(RULED by [name], 2026-08-21: ...)"`) that motivated writing `gate_no_build_attribution` in the first place — these are historical evidence of what the gate exists to catch, not narration about this code's own history, so removing the dates would misrepresent the actual defect instances documented here (the same distinction Entry 1's Council-of-Carthage/`donatism.html` protection in `tools/check_live_commentary.py` draws, applied by hand here since this file isn't on that tool's protected-file list); line 683, a generic `"RULED by [name]"` placeholder describing a defect *class*, not a specific ruling; line 1270, "reviewer" used generically ("only useful to a reviewer alongside WHERE it drifted") to mean whoever reads this function's output, not a project review-process reference — the same false-positive class PR #498's own body already documented for this pattern.

**Entry 5 — `engine/api/table_wiring.py` (Step 2 PR C).** Removed throughout: dates and "independent review"/"reviewer thread" timestamps on the per-session advance lock's hard-stop rationale, the 2-3-seat re-validation, the `_own_world_named` design note, `_context_prefix`'s thinness rationale, `_scoped_pending`'s docstring, and the whole `_table_engagement_directive` docstring's five design/bug-fix passes (DESIGN ENHANCEMENT, THE ROUND-DESIGN FIX, BUG FIX, STRUCTURAL FIX) and their in-body "Independent review"/"SECOND independent review" section notes; "Mark's ruling 2026-09-17" on the `door_turn` card_name cross-reference; `selector_reason`'s and `get_round_close_reasons`'s "Mark's own question" attributions; the presentation-order shuffle's "Mark's report" attribution; the SEAT-IDENTITY GUARD's two "(Decision-Log.md Entry 47, 2026-09-22)" citations (both occurrences - opening comment and the continued-logging comment); the OTHER-TRADITION PARITY block's "(reviewer thread, 2026-09-23, round 1 fixes applied)" framing and its "R26/R37/R38"/"R37"/"R37-A"/"R37-B" ruling-number citations (three places); "round 2"/"Round 1"/"round-2" review-round labels in FIX 2's two paragraphs (reworded as "corrected after the first version got it wrong" / "The first version assumed..."); its closing "Decision-Log.md, Entry 68's round-2 addendum" citation (kept as a bare "see the Decision-Log" pointer - no entry number or date, the same kind of open cross-reference Entry 3 kept for `quote_verbatim.py`'s Rulings-Pending pointer); the uncited-claims check's "R27 (Decision-Log.md Entry 51, 2026-09-22)" citation; and the seat-correction fallback's "R27 build item 5 (Decision-Log.md Entry 56/Rulings-Pending.md R36, 2026-09-23)" citation and "the reviewer thread's own item 5 message asked for" framing. Every direct quotation of the project lead's own words (on shortening pressure, the round-design fix, the fabricated-Facilitator-line bug, and the "i dont want fix on fix" structural fix) stayed verbatim, attributed to "the project lead" rather than "Mark" with a date. The underlying design reasoning - what each fix does and why - stayed in full in every case; only the ruling numbers, review-round labels, reviewer-thread citations, and dates moved here.

Eight occurrences of `r27_enforce`/`r27_enforcement_exhausted` (lines 672, 952-953, 1013, 1054, 1160, 1178, 1204) are real code identifiers (a parameter name, dict keys, a call-site kwarg) — out of scope for this comment/docstring pass; they belong to Step 2 PR D's identifier-rename work, where `CIC_R27_ENFORCE`/`r27_enforce` is registered as an `ACCEPTED_OPEN` waiver rather than renamed, per the launch brief's own exception for this live server env var.

**Entry 6 — `engine/m4/uncited_claims.py`, `engine/m4/tests/test_uncited_claims.py` (Step 2 PR C).** Removed throughout both files: the module's own opening "(Decision-Log.md Entry 51, 2026-09-22)" citation and the "(Rulings-Pending.md R27)" restatement of the same rule it already names; a "(Decision-Log.md Entry 51)" citation on the claim_markers-cannot-be-the-gate finding; a "(Rulings-Pending.md R26, Decision-Log.md Entry 50)" citation on `R26_HONEST_LIMIT_SENTENCE`'s own comment; a "(reviewer thread fix list, 2026-09-22, after the item-4 live battery)" citation on fix F1 (three occurrences across the module and the test file); a "R27-A item 1 (Decision-Log.md Entry 55, 2026-09-23), PASS-verdicted in PR #421... as built in PR #420" build-history citation on `classify_other_tradition_turn`'s own docstring comment, reworded to state the same over-flagging finding without the PR numbers, entry number, or date; an "(R27-A item 2, Decision-Log.md Entry 55)" citation on the paragraph-offense docstring; an "Entry 55's own recommendation" citation on the inherited-paragraph rule; a "R36's own hand-sort (Decision-Log.md Entry 56, 2026-09-23)" citation (both the module comment and its Rulings-Pending.md R36 restatement, and the test file's matching comment); a "(reviewer thread's own instruction, PR #421's verdict)" citation on the two-failure-kinds comment; an "F5 (reviewer thread fix list, 2026-09-22, after PR #419's own re-run)" citation (module and test file, two occurrences each); an "R39's own reviewer-ordered fix (relayed 2026-09-23, "...")" citation and its quoted reviewer imperative, on the false-fixed-sentence fix (module and test file); a "(Decision-Log.md Entry 71, first PR #438)" citation on the restricted-prose-field-allowlist note (module and test file); an "(Rulings-Pending.md R37, ruled 2026-09-23; R37-A the same day; R37-B 2026-09-24)" citation opening the R37 design comment, and the matching test-file "(Rulings-Pending.md R37, R37-A, R37-B)" citation; two "Mark's words name..." attributions (module and test file), reattributed to "The ruling names..."; "R27-A item 1 (Entry 55/PR #421)"/"per PR #420's own live finding" and "R27 build item 3's own... named directly by the reviewer thread's build order" citations in the test file; and a "PR #420's own live report" attribution on the alx conflict-turn fixture comment. In every case the underlying design reasoning, and any real finding it recorded (the 24/24 over-flagging rate, the hand-sort catch, the demonym gap), stayed in full - only the Decision-Log/Rulings-Pending/PR citations, reviewer-thread framing, and dates moved here.

Bare `R26`/`R27`/`R37`/`R37-A`/`R37-B` mentions throughout both files are deliberate non-edits, not REWRITE cases: unlike the R33/R35/R28-style ruling citations removed elsewhere in this program, these are the module's own stable rule names, structurally tied to real code - `R26_HONEST_LIMIT_SENTENCE` (the constant), this module's own R27 report-only check, and `engine/m4/reports/r37_build_battery.py` (a real, findable report path R37 is named after) - the same reasoning already applied to `table_wiring.py`'s R27/`r27_enforce` in Entry 5. Removing the bare rule name would disconnect the prose from the identifiers it describes; only the decorative citation wrapper (dates, entry numbers, PR numbers, "reviewer thread") came out.

**Entry 7 — `engine/m4/live_uncited_claims_battery.py` (Step 2 PR C).** Removed from the module's opening docstring: the "(Decision-Log.md Entry 51)" citation on R27 build item 4; the "(reviewer thread \"CiC — Tech Review & Funding Readiness Prep\", 2026-09-22, after item 4's first run)" citation on fix list F3; "Mark can set" reworded to "the threshold can be set" (no participant/project-lead attribution needed - it's simply who reads the report); the "(Decision-Log.md Entry 54's own build order, item 2's module merged in #424)" citation on the R27-A item 4 paragraph-unit numbers (also dropped the bare "R27-A item 4"/"R27-A item 2" labels here, since - unlike R27/R26/R37 - "R27-A" names no real code identifier anywhere in this file or the module it measures); "Entry 55's option (a)" reworded to "the paragraph-check's option (a)"; the "(reviewer thread fix list, 2026-09-22, after PR #419's own report, SUPERSEDED above)" citation on F6, kept as plain "(SUPERSEDED above)"; and the "(Decision-Log.md Entry 56/Rulings-Pending.md R36, 2026-09-23)" citation on R27 build item 5. Removed from the function bodies and the two runtime report "note" strings (builder-facing JSON output, not source comments, but the same leaked-citation defect the f-string fix in gates.py's Entry 4 already established as in scope): the "(R27-A item 2)" citation on `_paragraph_check`'s docstring; the "(Entry 54 item 4's own ask)" citation (three occurrences: `_one_sentence_wholly_uncited_paragraphs`'s docstring, the paragraph-unit-simulation comment, and the sentence-level-numbers comment in `run`'s per-world dict); the "(Entry 55's own point 4: ...)" citation on `_inherited_verdict_counts`'s docstring; the "now (Entry 56)" citation on the correction-wording comment; the "(R27-A item 2)" citation on the paragraph-unit-numbers comment; and, in `run`'s report "note" string, "R27-A item 4 asks Mark's enforcement threshold to be set against (Decision-Log Entry 54)" reworded to "the enforcement threshold is meant to be set against", "Entry 55's own option (a) vs (b) question" reworded to "the option (a) vs (b) question", and "the reviewer's own ask names alx on the Donatists probe first" reworded to "alx on the Donatists probe is reported first"; and in `run_enforced`'s report "note" string, "Mark's own staging-look numbers" reworded to "a staging look at the numbers" and the trailing "(that was #427's own job)" citation dropped. In every case the underlying design reasoning and every real finding (the 24/24 over-flagging rate this module measures, the denominator discipline, what each number is for) stayed in full - only the Decision-Log/Rulings-Pending/PR/reviewer-thread citations and dates moved here.

Bare `R26`/`R27` mentions (module docstring items 4 and 5, the `--enforce` help text, the `run_enforced` print statement) are deliberate non-edits for the same reason as Entry 6: `r27_enforce`, `R27_ENFORCEMENT_EXHAUSTED`-shaped dict keys, and `CIC_R27_ENFORCE` are real, currently-running identifiers this file calls directly. The `r27_enforce`/`r27_enforcement_exhausted`/`attempts_meta["r27_regenerated"]` occurrences flagged as `ruling-identifier` (lines 68, 74-76, 532, 534, 577, 581-582, 602, 614, 624-625, 636, 654, 676, 686 in the cleaned file) are real code identifiers - parameter names, dict/field keys, an f-string interpolation - out of scope for this comment/docstring pass, deferred to PR D per the same `CIC_R27_ENFORCE` exception as Entries 5 and 6.

**Entry 8 — `engine/m4/turn.py`, `engine/m4/tests/test_turn.py` (Step 2 PR C).** Removed throughout both files: dates on the routing-actions scope note, the LIVE-GENERATION-DESIGN two-call-shape signoff, the `UnhandledRoutingAction` unreachable-as-of note, the `GateRun` extraction, the two-pass term-resolution measurement, the portfolio decision that silences the voice on `ACUTE_DISTRESS` (three occurrences - the module docstring and two test docstrings), the Program-Spec SS8 Track-B-silencing amendment, the invented-term-id live measurement, the pre-fix gate-payload build date, the "Run 2 turn 2" bridge-non-fire measurement, and the `apply_net` foundation-audit finding; "Mark's own words"/"Mark's words" attributions on the two direct quotations of the project lead's own ruling text (the R26 no-invented-sources rule and the R37(b) seated-tradition scope rule, each quoted twice across the two files) reattributed to "the project lead's own words," quotes kept verbatim; "Mark flips the flag"/"until Mark flips CIC_R27_ENFORCE" reworded to "until the flag is flipped on"; "the new line Mark chose 2026-09-23" (the `voice_turn_rejected_turn` fallback note) dropped entirely, the design reason (a Facilitator turn substitutes when enforcement exhausts) already stated without it. Removed review-round/reviewer-thread framing: "Round 1 returned None... the round-2 review caught..." (the `_other_tradition_directive`/`_build_turn_directive` Table-parity history) reworded to "The first version of this fix returned None... and catching it exposed..."; "(Decision-Log.md, Entry 68's round-2 addendum)" dropped from the OT3-probe finding, the finding itself kept in full; "reviewer thread"/"reviewer-ordered"/"the reviewer's own ask"/"per the reviewer's own explicit instruction" framing on R27 fix F3/F4/F6 and the R39 evidence-record fix, in both files, reworded to state the fix plainly (e.g. "R27 fix F3" alone, "the R39 fix that corrects a false honest-limit statement"). Removed Decision-Log/Rulings-Pending entry-number citations throughout (Entries 47, 50, 51, 55, 56, 61, 68; Rulings-Pending R36) on the seat-identity guard, `_append_r27_correction`, the R27/R27-A enforcement docstrings and comments, the R26/R37 build docstrings, and the R38 self-revision block - the design reasoning stayed in full in every case, reworded only to drop the who/when/which-entry wrapper.

Bare `R27-A` and `R36` labels are REMOVED throughout both files, not just their date/citation wrappers: unlike `R27`/`R26`/`R37`/`R38`/`R39` (below), neither names a real code identifier anywhere in `turn.py`, `test_turn.py`, or `uncited_claims.py` (the module their content describes) - "R27-A item 2 (Entry 55)" becomes plain prose ("paragraph_coverage now rides on THIS SAME net_result..."), "R27 build item 5 (Entry 56/Rulings-Pending.md R36)" becomes "R27's flag-gated enforcement," and "R36's own scope decision" becomes "This enforcement's own scope decision." Bare `R39` mentions are KEPT, correcting a first pass of this entry that stripped them: `engine/m4/reports/r39_generation_side_measure.py` and `engine/m4/reports/r39_d1_d2_measure.py` are real, committed file paths named after R39, the same shape of evidence Entries 6/7 used to justify keeping bare `R37`/`R38` - a check this entry's own initial instructions missed (the grep behind that instruction searched for `R39` as a code identifier/constant, not as a report-file naming convention). Reworded to name the rule while dropping the reviewer-thread wrapper: "R39's own reviewer-ordered fix, relayed 2026-09-23" becomes "the R39 fix" at all three occurrences (`evidence_record_ids`'s and `other_tradition_evidence_ids`'s docstrings in `turn.py`, and the section comment above `test_other_tradition_directive_keeps_the_fixed_sentence_when_there_is_no_evidence` in `test_turn.py`).

**Entry 9 — PR #504 round 1 FAIL, corrected across all 9 target files (Step 2 PR C).** The managing thread's round-1 verdict on PR #504 corrected a standing misreading of the launch brief that Entries 5-8 each applied: "it ties to a real identifier or filename" was read as license to keep a BARE ruling-number label (`R26`, `R27`, `R37`/`R37-A`/`R37-B`, `R38`, `R39`) in comment/docstring PROSE whenever the number also names a real running code identifier or a real committed file (`r27_enforce`, `R26_HONEST_LIMIT_SENTENCE`, `engine/m4/reports/r37_build_battery.py`, etc.). The actual rule, per the verdict: that exception covers the identifier or filename ITSELF staying unrenamed (PR D's own scope) - it does not license a comment or docstring to keep naming the rule BY NUMBER. Every bare `R26`/`R27`/`R37`/`R37-A`/`R37-B`/`R38`/`R30` mention this program's own comments and docstrings still carried was reworded to name the rule in words instead - "the honest-limit rule" (R26), "the uncited-claims rule" (R27), "the tradition-pivot rule" and its "condition (a)"/"condition (b)"/"third source" (R37/R37-A/R37-B), "the self-revision pass" (R38) - across `engine/m1/rendering_fidelity.py`, `engine/m1/quote_verbatim.py` (+ test), `engine/m1/gates.py`, `engine/api/table_wiring.py`, `engine/m4/uncited_claims.py` (+ test), `engine/m4/live_uncited_claims_battery.py`, and `engine/m4/turn.py` (+ test). This supersedes the specific "kept because it ties to a real identifier/filename" claims in Entries 5, 6, 7, and 8 for `R26`/`R27`/`R37`/`R37-A`/`R37-B`/`R38`/`R39` bare mentions - those mentions are now all reworded to plain words too. Real code identifiers (`r27_enforce`, `r27_enforcement_exhausted`, `r27_regenerated`, `R26_HONEST_LIMIT_SENTENCE` the constant) and real filenames (`engine/m4/reports/r37_build_battery.py`, `r38_self_revision_measure.py`, `r39_generation_side_measure.py`, `r39_d1_d2_measure.py`) are untouched, exactly as before - only the prose citing them by ruling number changed. `R30` (a section heading inside `engine/m4/self_revision.py`'s own docstring, that file out of this PR's scope) is named in words in `turn.py`'s one cross-reference to it ("its pre-stream compatibility note") rather than repeating "7b/R30."

Also fixed per the verdict's remaining items, all now REMOVED (not reworded to a bare label) since none ties to a real identifier: "F1"/"F2"/"F3"/"F4"/"F5"/"F6", "fix list", "build item N", and "item N" labels throughout `uncited_claims.py` (+ test), `quote_verbatim.py` (+ test), `rendering_fidelity.py`, `live_uncited_claims_battery.py`, and `turn.py` (+ test) - restated as plain prose in every case, the underlying fix/finding kept. `rendering_fidelity.py:28` ("blocking check unless Mark rules otherwise") restated as a plain report-only statement. `gates.py`'s two Mark/project-lead attributions on named decisions (the quote-mark-fidelity rule at two call sites, one inside an f-string that reaches gate-finding output; the mode-3-claim-fidelity design note; the quote-verbatim registration note) restated without naming who decided; `gates.py:644-650`'s three detector-pattern examples, which quoted real leaked text from an actual past incident, replaced with synthetic examples of the identical shape (an ISO date beside a build-attribution phrase, a `RULED by [name]` construction, a `WORKING SCOPE, NOT A RULING` marker) so the live file carries no real past ruling text - the design reasoning for each pattern is unchanged. `live_uncited_claims_battery.py:31`'s "F3(b)'s own words: 'That post-regeneration number is what Mark sets the threshold on'" restated as "the threshold is meant to be set against that post-regeneration number." `quote_verbatim.py:142` and `table_wiring.py:880`'s Decision-Log pointers replaced with the actual reason stated inline (respectively: the specific compounding OCR/scan anomalies in one vendored source file; the specific live-battery finding, without the pointer). `turn.py:922`'s "(R38, measured 0/20 real leaks)" measurement snapshot dropped entirely, per the verdict - a measured result belongs in a report or this log, not the source comment; the pass's own description (what self-revision does, why) stays.

A second pass across all 9 target files (13 code files), asked as the verdict's own closing question - does any comment name a ruling, a person, a date, a fix-list item, or a Decision-Log entry - caught several instances the classifier's own patterns had missed (a gap parallel to, but distinct from, the checker refinements the managing thread separately relayed for a future tools-only PR): `test_quote_verbatim.py:79`'s `"""Mark's third ruling: ..."""` (the classifier's `marks-word` pattern requires `Mark's` immediately followed by ruling/call/word/own; "Mark's third ruling" has "third" between them); `test_quote_verbatim.py:379`'s "the regression this round caught" and `turn.py:581`'s "(round-2 review fix - see..." (review-round labels with no attached date); `gates.py:776`'s "flagged again in this implementation's own report to the project lead"; `gates.py:1229`'s "a direct decision from the project lead" (Entry 4 had explicitly kept this one; the round-1 verdict's broader rule against naming decision-makers supersedes that specific call); `gates.py:1333`'s "in the project lead's own words" plus "per item 3 of the P3 registration brief"; `quote_verbatim.py:596`'s "(item 3)"; `test_quote_verbatim.py:381,519`'s two "item 2" labels; `rendering_fidelity.py:1`'s "Item 4 of the P3 registration brief"; `live_uncited_claims_battery.py:311,422,494`'s three "Item 4's own" labels. All reworded the same way as the rest of this entry - rule/finding restated in plain words, no ruling number, person, date, fix-list item, or Decision-Log entry attached. PR numbers with no surrounding review-round/reviewer-thread framing (`PR #413`, `PR #415`, `PR #422`, `PR #427`) were left as-is at this point, on the reasoning that a bare, undated, unattributed reference a reader can still look up is not provenance narration, the same class as Entry 4's kept commit hashes - corrected in Entry 10 below.

**Entry 10 — PR #504 round 2 FAIL, PR numbers and commit hashes removed (Step 2 PR C, last round under the cap).** The managing thread's round-2 verdict corrected Entry 9's closing call: a bare PR number or commit hash is provenance in the same class as a ruling number - it answers "who changed what, when," not "what does this do and why" - regardless of whether a date or reviewer-thread label rides along with it. Named example: "PR #432." Removed, restating the current fact in each case rather than its history: `quote_verbatim.py:27`'s "report-only through PR #422;" (the surrounding sentence already states the current fact - registered in `gates.GATES` - so the clause was dropped outright, nothing to restate); `quote_verbatim.py:90`'s "After PR #413's record-fix pass left 13 non-escalated failures" became "Of the apparatus the gate didn't yet strip, 13 non-escalated failures remain"; `live_uncited_claims_battery.py:86,440`'s two "(PR #415...)" citations on the table-caller-path note dropped, the finding ("already proven correct there") kept; `test_turn.py:1199`'s "(PR #427's own report: uncited_in_cited_paragraph)" became "(a real report's own uncited_in_cited_paragraph finding)"; `gates.py`'s four "commit fbb6557"/"commit 763c48d" citations (the quote-mark-fidelity docstring, the cross-record-consistency-flag design note and its own commit-message quotation, the mode-3-claim-fidelity counterexample intro, and its companion-defect paragraph) all dropped, each restated as "a real, already-shipped defect" or "the same already-shipped incident" without the hash - the concrete defect each one describes (what broke, why a mechanical check couldn't have caught it) stays in full in every case.

Also fixed: `test_turn.py:1224`'s "The R39 fix that corrects a false honest-limit statement:" - "fix" framing on a section comment above four pinning tests - restated as what those tests actually check ("`_other_tradition_directive`'s own honest-limit sentence must never fire unconditionally..."), dropping both "R39" and the historical "fix" frame; this is narrower than Entry 9's R39 policy (turn.py's own two `R39`-tied docstring mentions, on `evidence_record_ids` and `other_tradition_evidence_ids`, are untouched and still correctly KEPT bare per Entry 9 - the managing thread's round-2 verdict named only this one test comment, not a reversal of the R39-stays-bare policy itself).

KEPT, confirmed by name in the verdict and re-checked here: `gates.py:866`'s `CiC_Register_Bar_2026-08-29.md` and `turn.py:1057`'s `VR_1A_Transparency_Gap_2026-08-09.md` (real filenames that happen to contain a date, not dated commentary); `gates.py`'s synthetic `2026-01-01` detector examples (Entry 9's own synthetic replacements, illustrative of a pattern shape, not a real incident); `test_grounding_net.py:256`'s "don's round-1 turn-1 of an rzg+don Table round" (a live Table session's own round/turn index, a runtime concept this codebase actually uses - `state.round_no` - never a code-review round).

Verification after this round: full `engine` test suite and `check_paths.py` re-run clean; a fresh grep for `PR #[0-9]+`, `commit [0-9a-f]{7}`, and bare `R[0-9]{2}` across all 13 touched files confirms zero remaining PR-number or commit-hash citations anywhere, and the only remaining bare `R[0-9]{2}` hits are `turn.py`'s two intentionally-kept `R39` mentions addressed above.

**Entry 11 — PR #504 PASS with one pre-merge correction (Step 2 PR C, merged).** The managing thread's PASS verdict corrected the one open question from Entry 10: `turn.py:360`'s "the R39 fix that lets a world's own records stand in..." and `:810`'s "the R39 fix that corrects a false..." are prose naming a rule by number and framing it as a fix - the same class of defect Entry 9's policy removes everywhere else, not an exception the R39-stays-bare policy covers. That policy (Entry 9, confirmed in Entry 10) only ever covered the two real filenames `engine/m4/reports/r39_generation_side_measure.py` and `r39_d1_d2_measure.py` staying named - it never extended to naming the rule itself "R39" in prose, exactly as R26/R27/R37/R37-A/R37-B/R38 already didn't. Both docstring parentheticals reworded to describe what the parameter does with no "R39" and no "fix" framing: `evidence_record_ids` is now "(lets a world's own records stand in for the honest limit when they already speak to the question)"; `other_tradition_evidence_ids` is now "(corrects a false honest-limit statement, unconditional - never gated behind r27_enforce...)". A fresh grep for `R39` across the whole repository (not just the 13 touched files) confirms zero remaining prose mentions inside this PR's own 9 target files; it also surfaces the same defect still live in three files genuinely outside this PR's scope - `engine/api/wiring.py`, `engine/m1/sentence_completeness.py`, and two files under `engine/m4/reports/` (`g1_citation_contract_battery.py` plus the R39 report scripts' own opening docstrings) - `engine/*/reports/` is explicitly out of scope per the launch brief, and the other two are not among the 9 files this program named; flagged here rather than fixed, since expanding this PR's own scope was not asked for. Full `engine` suite and `check_paths.py` re-verified clean. PASS - no further round.

Verification after this round: `engine` test suite (1150 tests, all passing), `tools/check_paths.py` (0 new unresolved citations, 775/775 accepted), and `check_live_commentary.py --surface engine` confirm every remaining REWRITE hit across the 9 target files is either a real code identifier/filename (`ruling-identifier`, or bare `R39` per its own real-file exception) or one of the deliberate non-edits already itemized in Entries 1-4 (the quotation-mark false positive, `REPORT_PATH`'s dated filename x3, the synthetic detector examples above, the generic "RULED by [name]"/"reviewer" placeholders).

Bare `R26`, `R27`, `R37`/`R37-A`/`R37-B`, and `R38` mentions throughout both files are deliberate non-edits, the same reasoning as Entries 5-7: `R26_HONEST_LIMIT_SENTENCE` is a real constant `turn.py` itself defines and `uncited_claims.py` matches against; `r27_enforce`/`r27_enforcement_exhausted`/`attempts_meta["r27_regenerated"]` are real parameters/dict keys this module and its tests call and assert on directly; `engine/m4/reports/r37_build_battery.py` and `r37_live_battery.py` are real, findable report paths R37 is named after, and the pivot logic they battery-test (`_other_tradition_directive`, `_pivot_scope_clause`, `_revealed_excerpts_block`) lives in `turn.py` itself; `engine/m4/self_revision.py` (the module `turn.py`'s SELF-REVISION block calls into) opens its own docstring "R38," and `engine/m4/reports/r38_self_revision_measure.py` is a matching real report path. Every direct quotation of the project lead's own words (the R26 ruling and the R37(b) seated-tradition rule, each appearing twice) stayed verbatim, reattributed rather than removed. The underlying design reasoning - what each fix does, why the Table-parity round found a real failure, what R27/R27-A/R36 enforcement actually enforces - stayed in full throughout; only the ruling-round labels, reviewer-thread framing, Decision-Log/Rulings-Pending entry citations, dates, and the two labels (`R27-A`, `R36`, alongside `R39`) with no real code identifier moved here or came out.
---

## Entry 1 — cic-website/ (Step 2, surface 1 of 6)

`tools/check_live_commentary.py --surface cic-website` read 260 hits
before this PR (0 KEEP, 256 REWRITE, 4 PROTECTED) and 1 after (see "Left
open" below). Every REWRITE line's functional reason was kept, rewritten
in plain present tense, in place; the provenance below is what moved out.
Regenerated `cic-website/tree/*.html` (`tools/generate_tree_pages.mjs`)
and `cic-website/traditions/*.html` (`tools/generate_tradition_pages.py`)
after editing their sources so generated output matches.

**Removed, by file (see this PR's diff for exact before/after text):**

- `cic-website/index.html`, `table.html`, `assets/style.css`,
  `traditions/*.html` (shared header/nav chrome) — ~18 CSS/HTML comments
  citing "Mark, 2026-09-18/19" with direct quotes ("can you center them",
  "add a fade at the bottom", "add a peek of the next card", etc.) behind
  the site header/menu, chairs gallery, feature-card, and video-loop
  design decisions. Reason kept (why the CSS is shaped this way); the
  attribution and date removed.
- `cic-website/support.html` — the largest single removal: a ~167-line
  top-of-file comment logging five-plus revision passes on the cost
  section and Payment Link setup ("Replaced 2026-08-06", "SUPERSEDED
  2026-08-25", "CORRECTED 2026-08-26", "Revised... second/third/fourth
  pass", direct Mark quotes throughout), plus a second ~30-line inline
  revision comment in the cost `<section>`. Condensed to the current
  state and reasoning only (what the two Stripe Payment Links are, why
  the cost section deliberately carries no dollar figure). Full passes
  already lived in `Ministry/Features/Funding-Strategy/` — this removal
  stops duplicating that history in the live file, not deletes it.
- `cic-website/README.md` — "Removed from nav again 2026-09-19 (Mark,
  direct instruction)", "Academic Review Fund dropped 2026-08-25 (Mark,
  direct instruction)", and a "Resolved, 2026-07-21" bullet documenting a
  since-settled contact-email decision (removed outright as a stale
  "known follow-up," not moved — the current mailbox is already visible
  in every page's own contact link).
- `cic-website/data/world-census.json` (and the identical strings
  duplicated in `atlas-v3.html`'s own embedded `DATA` copy — see "Flagged,
  not fixed" below) — one `meta.generated` timestamp; a dated clause in
  `meta.notes`; 8 `stepStatus` era fields reading "era FROZEN by Mark
  <date>"; and a repeating `statusDescription`/edge-`note` trailer,
  "Added/ADOPTED/Edge written at the Era N gate/Freeze (Mark, <date>)",
  on ~50 movement and edge records across Eras 3, 4, 6, 9, and 10. Two
  records also had "per Mark's two-world steer" / "per Mark's mandate"
  reworded inline (`split at 843, treated as two separate worlds`; `per
  the grading mandate`). Every instance dropped only the `(Mark,
  <date>)` parenthetical or personal-attribution phrase; the surrounding
  status sentence (e.g. "Added at the Era 4 gate") is untouched.
- `cic-website/atlas-v3.html` — beyond the census-mirrored fields above:
  one CSS comment citing "2026-09-17... see the Decision-Log"; a
  three-round revision narrative on the era-divider line ("Mark,
  2026-09-17: the old break band...", two further "Mark's next report"
  passes) condensed to one paragraph describing the current design; and
  five further single-line date/quote removals (HEADER_GUTTER,
  ERA_CONTEXT_WRAP, the Part 3 cutover note, the source-registry note,
  pointer-capture and manual-pan-controls comments, and
  `positionScopeNote`'s feature-bar note).
- `cic-website/templates/tradition.html` — "project owner's ruling
  2026-09-19" / "2026-09-21" from the header comment and the two inline
  comments this template splices into all 11 built worlds' own
  `traditions/*.html` pages (the safety-disclosure note and the
  glossary/pull-quotes placement note); fixed once here rather than
  per-page, then regenerated.
- `cic-website/assets/world-icons/{alexandria,bethlehem,desert,empire,
  house-churches,syriac}.svg`, `assets/logo-arriving.svg` — version-
  history logs (V0.1 DRAFT → V1.8 LOCKED iteration notes), "Mark
  approved 2026-07-18" / "Mark's call" attributions, and direct quotes
  ("this actually looks great, lets lock this for now"). All DOCUMENTED/
  INFERENCE grounding notes (what's attested vs. inferred, and why) were
  kept verbatim — only version-iteration and approval narrative moved.
  Outside `check_live_commentary.py`'s scope (it skips `.svg`), fixed
  per the launch brief's own naming of these files.
- `cic-website/assets/orientation-render.mjs`, `story.html`,
  `pilot-feedback.html`, `talk.html`, `atlas.html`, `world-atlas.html` —
  one dated clause each (design-approval date, a page-migration date, a
  dark-mode-fix date, a form-reliability fix date, an iframe-bug date, a
  page-redirect date).

**Left open (1 remaining hit):** `support.html:127` — "external
reviewer" in "If you know a seminary, professor, or scholar who might
serve as an external reviewer, introduce us." This is participant-facing
copy about wanting an academic reviewer for the project's own scholarship,
not narration of this project's internal review process; the checker's
`reviewer` pattern has no carve-out for that context (unlike its `round`
and `iso-date` patterns, which do exclude non-review "round" usages and
bare-date fields). Left unchanged rather than reworded, since this PR
does not touch participant-facing wording without real review. Flagged
for Cleanup 1 as a candidate pattern refinement, and for Mark as a
"Words for Mark" item if a rewording is wanted instead.

**Flagged, not fixed (outside this program's scope):**
- `atlas-v3.html` embeds its own `const DATA = {...}` copy of
  `world-census.json` (`tools/check_no_embedded_world_data.py`'s own
  documented, already-baselined anti-pattern — its migration to fetching
  at runtime is a separate, later Website V2 stage). That embedded copy
  is measurably **stale**: `liveCount: 7` vs. `world-census.json`'s
  `liveCount: 11`, and different `statusCounts` — the live map may be
  under-representing built worlds. This is a data-accuracy defect, not
  commentary, so it's out of scope for this cleanup PR; both copies
  received the identical provenance-removal treatment (independently,
  since they already diverge) so neither carries stale REWRITE hits, but
  the underlying staleness is unresolved and worth its own fix.
- `tools/tests/test_check_live_commentary.py`'s hand-labelled sample
  cites specific `cic-website` line numbers (and `cic-poc/frontend` ones,
  untouched by this PR) as known REWRITE examples; cleaning those exact
  lines makes 10 of those hand-labels stale (`python3 -m pytest
  tools/tests/test_check_live_commentary.py` now fails). Not currently
  wired into CI (`.github/workflows/ci.yml` runs the checker itself,
  report-only, but not its pytest suite), so this does not block CI on
  this PR's head. Left for Cleanup 1 to refresh alongside each surface
  PR landing, per the checker's own docstring ("measures it before
  anything downstream... touches a single line").

Validated: `check_live_commentary.py --surface cic-website` → 1 hit (was
260); `check_no_embedded_world_data.py` → exit 0; `check_paths.py
--baseline tools/check_paths_baseline.txt` → 0 new/retired; `node
tools/validate-census.mjs` → 0 errors; `engine/m6/tests`,
`engine/m2/tests/test_site_{compiler,staleness}.py` → all green.
`cic-poc/frontend` untouched by this PR.

**Round 2 (managing-thread verdict, FAIL round 1, 2026-09-24):**

1. Round 1 only stripped the `(Mark, <date>)` parenthetical, leaving the
   surrounding process sentence itself on the live site: "Edge written at
   the Era 9 Freeze.", "Added at the Era 4 gate.", "ADOPTED at the Era 10
   Freeze.", and several mid-sentence variants ("banked at the Era 9
   gate", "written at the Era 9 gate", "made at the Era 9 gate", "ruled
   REGISTER over Outside-A4 at the Era 9 Freeze") — 105 occurrences
   across `world-census.json` and its 1 mirrored occurrence in
   `atlas-v3.html`'s embedded copy, plus the 7 already-regenerated
   `tree/*.html` pages. Removed the whole clause in every case, keeping
   the sourcing sentence before it (e.g. "Added at the Era 3 gate —
   proposed by the Era 3 Step 0 run..." → "Proposed by the Era 3 Step 0
   run..."). Four `statusDescription` fields carried nothing but the
   process clause itself, with the real status already stated in the
   sibling `statusWord` field — emptied to `""` rather than left
   half-sentence. `stepStatus` fields ("Step 0 run complete — era
   frozen") were left as-is per the verdict: they state current status,
   not process history. Regenerated `tree/*.html` from the fixed data.
2. Refreshed `tools/tests/test_check_live_commentary.py`'s 6 stale
   cic-website `HAND_LABELS` entries (all 6 pointed at lines this PR's
   round 1 had already cleaned). cic-website now has only one real
   remaining hit — hand-labelled `KEEP` (`support.html:127`, "external
   reviewer" — a checker false positive on real body copy about an
   academic reviewer, per the managing thread's own explicit ruling that
   this is not a Words-for-Mark item) — so the other 5 slots moved to
   fresh `cic/corpus-map` examples (untouched, stable) to keep the table
   at its required ≥60 real, currently-matching samples.
   `cic-poc/frontend`'s 3 stale entries are PR #503's own fix, not this
   PR's.
3. Registered `atlas-v3.html`'s stale embedded-census finding (liveCount
   7 vs. `world-census.json`'s 11) as a comment on its
   `tools/embedded-world-data-baseline.txt` entry — the baseline format
   supports `#`-prefixed comment lines (skipped by the loader, so the
   exclusion itself is unaffected). Not fixed here, per the verdict's own
   instruction ("Don't fix the migration here").

Re-validated: `check_live_commentary.py --surface cic-website` → 1 hit
(the documented KEEP false positive); `check_no_embedded_world_data.py`
→ exit 0; `check_paths.py` → 0 new/retired; `node
tools/validate-census.mjs` → 0 errors; `pytest
tools/tests/test_check_live_commentary.py` → 4 failures remaining, all
`cic-poc/frontend` (PR #503's own stale entries, not this PR's).

**Round 3 (managing-thread verdict, FAIL round 2, one round left under the
three-round cap):**

Round 2 only removed the tokens the checker patterns themselves catch
(dates, ruling numbers); a comment could still narrate what used to be
true, in plain prose the checker has no pattern for. Round 3 is a full
manual second pass, file by file, on that question - not just the seven
spots the verdict's own (non-exhaustive) grep found.

1. `templates/tradition.html`: the "was cut in the card redesign" history
   on the safety-disclosure comment (spliced into all 11
   `traditions/*.html`); "Two sections that used to run here are gone
   outright" in the header comment; "not the old 3-section page" in the
   opening line; and "no section of their own in the old hand-built
   pages" on the glossary/pull-quotes comment. All four restated as
   present-tense fact; template fixed once, `traditions/*.html`
   regenerated.
2. `index.html`, `assets/style.css`: "was width:100%;aspect-ratio:16/7",
   "was min(60vh,480px)", "now part of the single header row" (both
   copies), "that was tried with equal flex-grow..." (the menu-centering
   comment), and "the card was as wide as or wider than its own mobile
   scroll container... nothing... ever showed" (the chair-peek comment,
   rewritten to the hypothetical it's guarding against, not a past
   state).
3. `atlas-v3.html`: by far the largest share of this round - roughly 25
   separate comments narrating a prior layout, a rejected alternative, or
   a fixed bug, on the header-gutter sizing, the era-divider block (a
   second location round 2 missed, plus a still-remaining "not the old
   thick bar" phrase in the one round 2 did fix), the per-river research
   note ("Mark asked for" attribution), the FAM color array's dated
   addition note, the dark-mode default-detection comment, the
   width-floor/merge-window/smoothstep river-rendering trio, the built-
   world label-collision trio (a first-attempt-and-revert narrative
   condensed to just the one surviving correction), the seam-mark-dot
   fix, the orientation-fetch race-condition note (dropped the specific
   "found by loading X in a browser, it threw Y" debugging story, kept
   the mechanism), the panel-content and status-pill removal notes, the
   focus-management note, the initial-zoom-floor note, the pointer-
   capture rationale, and the scope-note positioning note. Every one
   restated as the current design plus the (hypothetical, present-tense)
   problem it avoids, not a past-tense account of what broke or what an
   earlier version did. Three color-derivation methodology paragraphs
   (how the FAM hues and the dark-mode edge-opacity constant are
   computed, using "was" as part of describing a still-true derivation
   method, not a superseded value) were read closely and left alone -
   they don't say what used to be true, they say how the current value is
   derived, which remains true.
4. `talk.html`: "used to fall back to its pre-redesign Launch screen"
   rewritten to the current behavior only.
5. `pilot-feedback.html`: two spots from round 2's own re-reading (the
   mailto-vs-form-POST comment's own "Was action=... ALONE" opening, and
   "the mailto rebuild above was written to fix") - both restated as
   current behavior and reason.
6. `support.html`: "Text only for now" removed outright (stale - real
   checkout is live, stated in the very next sentence); ".fine-print...
   the fix that was already sitting right there" restated as present
   tense.
7. `assets/logo-arriving.svg`: "Opening widened to +/-50deg (was
   +/-40)" restated as the current angle alone.

Checked and left alone as real content, not commentary: the "chair" tile
descriptions on `index.html` and every `traditions/*.html`/`tree/*.html`
page (real historical prose - Alexandria's teachers, Donatism's rival
bishops, Wittenberg's theses - which legitimately narrates past events
in past tense); `support.html`'s "Pending review before this is treated
as final" (a real, still-open item, not settled history);
`README.md`'s "before this goes fully public" (a genuine forward-looking
TODO); `empire.svg`'s "was considered and held in reserve" and
`syriac.svg`'s "the old 'girdle'" (a rejected design alternative and a
historical garment term, neither project history).

Re-validated: `check_live_commentary.py --surface cic-website` → 1 hit
(unchanged, the documented KEEP false positive); `check_no_embedded_world_data.py`
→ exit 0; `check_paths.py` → 0 new/retired; `node tools/validate-census.mjs`
→ 0 errors, 292/69/10 unchanged; both JSON payloads (`world-census.json`,
`atlas-v3.html`'s embedded copy) parse; `pytest
tools/tests/test_check_live_commentary.py` → 81/85 passed, the 4
failures all `cic-poc/frontend` (PR #503's own surface, not this PR's -
full output:

```
FAILED tools/tests/test_check_live_commentary.py::test_hand_label_present[cic-poc/frontend/src/components/VoiceTurnBody.test.tsx-170-REWRITE]
FAILED tools/tests/test_check_live_commentary.py::test_hand_label_present[cic-poc/frontend/src/components/StoryMark.tsx-15-REWRITE]
FAILED tools/tests/test_check_live_commentary.py::test_hand_label_present[cic-poc/frontend/src/components/StoryMark.tsx-16-REWRITE]
FAILED tools/tests/test_check_live_commentary.py::test_precision_and_recall_on_hand_labelled_sample
4 failed, 81 passed in 0.87s
```
).

**Round 3 verdict: PASS**, with one remaining line flagged: `atlas-v3.html`
line ~40695, "0.55 (Mark, live-site review) blended graphite down to
within a few steps..." carried an attribution the checker's own regexes
don't catch (no ISO date, no ruling number). Fixed: dropped the
attribution and restated the rejected 0.55 alternative in the
conditional ("would blend...") alongside the kept reasoning for 0.78,
matching the same rejected-alternative pattern already used and kept
elsewhere in this file (e.g. `empire.svg`'s dalmatic alternative).
Re-validated: `check_live_commentary.py --surface cic-website` → 1 hit
(unchanged, the documented KEEP false positive); `check_no_embedded_world_data.py`
→ exit 0; `check_paths.py` → 0 new/retired; `node tools/validate-census.mjs`
→ 0 errors, 292/69/10 unchanged.

---

## Entry 2 — cic-poc/frontend/ (Step 2, surface 2 of 6)

`tools/check_live_commentary.py
--surface cic-poc-frontend` read 48 hits before this PR (0 KEEP, 48
REWRITE) and 1 after (a checker false positive left open, see below). No
UI-facing string content was changed anywhere in this PR — every edit is
to a `/**...*/` or `//` code comment; every rendered string in
`src/data/worlds.ts`, `src/lib/confidence.ts`, `src/components/
Arrival.tsx`, and the citation-mark copy is untouched.

**Removed, by file (see this PR's diff for exact before/after text):**

- `src/app.css` — a "2026-09-17 dark-mode change order" date on the
  `:root` token comment and the a11y-sweep comment above it; `R9 (RULED
  a, 2026-09-21)` and `R10 (RULED c, 2026-09-21)` ruling numbers/dates on
  the citation-mark comments; `R16/R9`'s ruling-number cross-reference on
  the confidence-phrase comment; three further dated change-order
  comments (`2026-08-26` transparency audit, `2026-09-17` dark-mode
  error-background change, `2026-08-28` "Trust package"). Reason kept in
  every case (why the token/color/rule is shaped this way).
- `src/components/Arrival.tsx`, `Arrival.test.tsx` — `Stage 6e
  (Ministry/Features/Conversation-Transparency-Engine/Decision-Log.md)`,
  `R10`'s "label copy" citation, and "per Mark's own direction" removed
  from the header comment explaining why one sentence in the disclosure
  block is new prose rather than relocated. **The comment's open-status
  flag was kept, reworded from "DRAFT COPY, not yet Mark's own word" to
  "DRAFT COPY, not yet approved as final wording"** — this is a real,
  still-open item (the ✲-mark explainer sentence in `arrival__disclosure`
  is unconfirmed copy), not settled history, so it stays flagged in the
  file rather than being treated as resolved provenance to remove.
- `src/lib/confidence.ts` — same pattern: `Stage 6b (...Decision-Log.md,
  Entry 35 family)`, `R16 (RULED c, Decision-Log.md Entry 29)` removed;
  "DRAFT COPY - not yet worded by Mark... until Decision-Log.md records
  his own word on it" reworded to "DRAFT COPY - not yet approved as
  final wording... until it is confirmed" — same reasoning: `
  CONFIDENCE_PHRASES`' values are still-unapproved copy, a live open
  item, not history.
- `src/components/StoryMark.tsx`, `WitnessMark.tsx`,
  `VoiceTurnBody.tsx`, `VoiceTurnBody.legacy-default.test.tsx` — `R9`/
  `R10`/`R17` ruling-number cross-references, one `RULED c, 2026-09-21`
  date, one `Rulings-Pending.md, Decision-Log.md Entry 29` pointer, and
  `Decision-Log.md Entry 49`/`R10 and label copy both ruled, Mark's own
  read-through passed` removed from header/inline comments. Reason kept
  throughout (why a mark sits where it sits, why the drop-cap and
  tie-break rules are shaped as they are).
- `src/lib/flags.ts` — `R10`, `Rulings-Pending.md`, `Decision-Log.md
  Entry 41`, `Mark's own seeker read-through`, `Entries 46, 48, 49`
  removed from the header comment explaining why the flag now defaults
  ON; the functional explanation (what the flag does, why "off" is the
  only string that reverts it) is untouched.
- `src/screens/TableRoom.tsx`, `TableRoom.test.tsx` — `Decision-Log.md
  Entry 47 (2026-09-22)` removed from both comments describing the
  seat-identity guard's empty-text case.
- `src/data/worlds.ts` — nine separate dated comments (`2026-08-24`
  design-review date, `as of 2026-09-20`, `2026-09-17` dark-mode-order
  date x3, and four "world N, added/admitted/re-admitted `<date>`"
  per-world comments) — every one kept the "which world, in what order,
  why this color" reasoning and dropped only the calendar date.
- `src/hooks/useConversation.ts`, `src/lib/api.ts` — one dated
  parenthetical each (`2026-08-28 audit fix`, `2026-09-04` bug-fix
  date).

**Left open (1 remaining hit):** `src/components/FigureBridgeMark.tsx:3`
— cites `VR_1A_Transparency_Gap_2026-08-09.md`, a real file at
`Ministry/Operations/Audits/CiC_VoiceRebuild_Blueprint_2026-08-08/
decisions/` whose date is part of its actual filename, not a change-date
attached to prose. Rewording or dropping the date would break the
citation. Left unchanged; flagged for Cleanup 1 as a second candidate for
a bare-filename-citation carve-out (alongside the `reviewer`-pattern gap
already flagged in Entry 1).

One further false-positive fixed rather than left open: `src/app.css`'s
padded-hit-area comment read "the mark's own position:relative" —
`marks-word`'s pattern is case-insensitive and fired on the CSS term
"mark" (as in citation mark), nothing to do with Mark. Reworded to "the
citation mark's position:relative" — same meaning, no provenance to
preserve, so fixed outright rather than documented as an exception.

Validated: `check_live_commentary.py --surface cic-poc-frontend` → 1 hit
(was 48); `check_paths.py --baseline tools/check_paths_baseline.txt` → 0
new/retired; `check_no_embedded_world_data.py` → exit 0; `npx tsc
--noEmit` → 0 errors; `npm test` (vitest) → 31/31 passed, 6/6 files.
`npm run lint` fails on this branch with a pre-existing "ESLint couldn't
find a configuration file" error, unrelated to this PR's changes
(comment-only edits) — not fixed here, flagged for whoever owns
`cic-poc/frontend`'s tooling config.

**Round 2 (managing-thread verdict, FAIL round 1, 2026-09-24):**

1. Round 1 only removed the ruling number/date token from each comment,
   leaving the surrounding sentence stating what USED to be true or
   naming a stage/ruling as the reason. Fixed throughout the PR's diff:
   - `Arrival.tsx` and `lib/confidence.ts`'s "DRAFT COPY, not yet
     approved" flags removed entirely (not reworded) - both are stale as
     of the Transparency Engine Decision-Log's own 2026-09-22 entries
     (Entry 39, Entry 41/the Arrival test's own PR #398 note): the
     Stage 6b confidence phrases and the ✲-mark explainer sentence were
     both "confirmed as Mark's own word without change." Status belongs
     in Ministry, never restated in a code comment.
   - `app.css`: "(supersedes CiC_Full_UX_Design_V1_0.md §2.1's 'Dark
     mode: deferred')", "was #8A837C - 3.38:1", "was #FBEAEA (light
     pink)", the "Cross-world transparency audit:" and "Trust package:"
     stage/feature-name labels, and one remaining "Stage 6b:" label —
     rewritten as present-tense facts (what the current color measures
     and why), not as "was X" comparisons.
   - `data/worlds.ts`: the file's own "used to be a hand-copied second
     version of the registry... nothing here is invented copy... The
     endpoint exists now" history paragraph, "Stage 7.5" cited twice as
     the source of a design decision, every "Nth world, added/admitted/
     re-admitted once X was locked in" ordinal-history framing (6
     instances), and every remaining "Light-mode color was X" comparison
     — all rewritten to state the current accent color's own grounding
     and contrast math directly, with no addition-order or stage
     narrative.
   - `useConversation.ts`, `lib/api.ts`: "(an audit fix)" and
     "recoverable: true - was false, which left a live bug..." rewritten
     to state what the code guarantees now.
   - `lib/flags.ts`: "Both are ruled now, and the seeker read-through...
     passed - the flag defaults ON" reduced to "Defaults ON."; the
     ruling/rollout history moved here.
   - `VoiceTurnBody.tsx`: "below are the confirmed answer, not invented
     here" and "a documented default, not an implicit accident" (process
     voice from round 1's own rewrite) restated as the rule itself; "the
     approach Build-Plan.md Stage 3c replaces" (still framing the legacy
     renderer by what it's superseded by) restated as its own
     completeness gap, stated directly.
   - `VoiceTurnBody.legacy-default.test.tsx`, `screens/TableRoom.tsx`:
     "turn from before Stage 3b" and "Stage 0c, Build-Plan.md" — the
     stage label dropped, the technical condition it named stated
     directly instead.
2. Refreshed `tools/tests/test_check_live_commentary.py`'s
   cic-poc/frontend `HAND_LABELS` entries a second time: round 1 fixed 3
   of the 6 original entries' staleness in its own PR body but round 2's
   further cleanup made 2 more (`Arrival.test.tsx:2`, `Arrival.tsx:14`)
   stop matching too. Only `FigureBridgeMark.tsx:3` (the real
   filename-citation false positive) is still valid; the other 5 slots
   moved to fresh `cic/corpus-map` examples, distinct from the 5 Entry 1
   already claimed there, to avoid a duplicate sample.

Re-validated: `check_live_commentary.py --surface cic-poc-frontend` → 1
hit (the documented `FigureBridgeMark.tsx:3` false positive); `pytest
tools/tests/test_check_live_commentary.py` → **85/85 passed** (0
failures - both PRs' stale-hand-label fixes are now mutually
consistent, pending whichever merges first renumbering the other's
Decision-Log entry per Entry 1's own note); `npx tsc --noEmit` → 0
errors; `npm test` (vitest) → 31/31 passed; `check_paths.py` → 0
new/retired.

**Round 3 (FAIL round 2 fixes, four leftovers the checker's own patterns
don't catch):**
1. `VoiceTurnBody.legacy-default.test.tsx:2-4`: "The flag now defaults
   ON - this file's own title predates that flip..." restated as the
   file's present-tense purpose - it tests the legacy renderer, which
   stays reachable whenever a turn has no `transparency` plan,
   regardless of the flag's own default.
2. `data/worlds.ts:24-26`: "per site-portrait/witt's own now-closed
   cross_world entry" dropped; kept only where the portrait lives
   (GitHub, as `nikolaus.jpg`).
3. `types/conversation.ts:35`: "every fixture/test predating Stage 6b
   built a SourceCard without it" restated as the contract itself - the
   field is optional because a caller may omit it; a real API response
   always includes the key (possibly null).
4. `lib/confidence.test.ts:4`: dropped "(Stage 6b)" from the `describe`
   block title.

Not touched: the several other `Stage N (Build-Plan.md)`/`PHASE-1-
LAUNCH.md Stage N` citations elsewhere in this surface
(`conversation.ts`, `app.css`, `ChatInput.tsx`/`.test.tsx`,
`useWorlds.ts`, `useTable.ts`) - these cite the governing spec document
by name as the source of a still-current technical rule (a round-cap
value, a disabled-prop contract), not a ruling/decision date or
attribution; the round-2 verdict named exactly the four items above as
the remainder, and these weren't among them.

Re-validated: `check_live_commentary.py --surface cic-poc-frontend` → 1
hit (unchanged, the documented `FigureBridgeMark.tsx:3` false
positive); `npx vitest run` → 31/31 passed; `pytest
tools/tests/test_check_live_commentary.py` → 85/85 passed; `check_paths.py`
→ 0 new/retired.

---

## Entry 3 — cic/corpus-map/ (Step 2, surface 3 of 6)

`tools/check_live_commentary.py --surface cic-corpus-map` read 761 hits
before this PR (0 KEEP, 761 REWRITE, 0 ROUTE — the checker's own
ROUTE_CUES limitation reads a ROUTE line as REWRITE; see Entry 1/2's
same note) and 0 after. This is the largest surface so far: 133
`_staging/<volume>.yaml` source files (the only files a worker ever
hand-edits), 58 generated per-tradition bucket files plus
`UNATTRIBUTED.yaml` (regenerated from staging via
`cic/engine/corpus_map_merge.py`, never hand-edited), and a handful of
top-level docs/scripts.

**Never touched anywhere in this PR:** `work:`, `author:`, `locus:`
(except the two boundary cases below), `atlas_ids:` (which tradition a
work maps to), `role:`, or `confidence:` field values. Every edit is to
`note:`/`evidence:` prose or `#` comments.

### What changed, by category

1. **46 "header-only" `_staging/` files** (all their hits confined to
   the file's own leading `#` header block) — a single-pass script
   dropped "Worker notes, `<date>`.", "Worker: `<thread>`, `<date>`.",
   "Vendored `<date>`[, supplied by Mark].", "Written `<date>` by `<X>`
   sweep.", "RULED, Mark, `<date>`:", and "SEEDED WORKED EXAMPLE,
   `<date>` -"/"EXTENDED `<date>` by..." framing from each header,
   keeping every still-true reason (Pearse-file/ThML notes, why a
   volume was proactively vendored, the Cyprian granularity rule,
   Morison's own scholarly-framing methodology, npnf204's own
   worked-example shape) restated in present tense. Diff spot-checked
   file by file before running; re-verified 0 remaining hits across all
   46 afterward.
2. **87 further `_staging/` files** with hits inside per-work `note:`
   fields (not just the header) — done via six parallel workers, each
   given the same litmus test, worked examples, and the CRITICAL
   boundary list above, then reconciled by hand. The dominant pattern,
   repeated hundreds of times: `"<date>: <atlas_id> added alongside -
   the entry the corpus assignment showed was missing, for <reason>.
   <X> is kept: <reason>."` → `"<atlas_id> holds this work for
   <reason>; <X> is kept because <reason>."` Also fixed throughout:
   "RULED BY MARK", "Re-pointed `<date>`", "Cross-linked `<date>` from a
   Source Readiness Dossier finding", "NOTE, corrected `<date>` (OG-N)",
   "Split `<date>` on Mark's ruling", review-round citations
   ("independent review Round N", "lpc Round 28/29"), and several
   multi-sentence "this note previously said X, that was withdrawn,
   corrected here" self-correction paragraphs (codex-theodosianus'
   Donatism-bucket note, perpetua-scillitan's Tertullian-voice note) —
   each condensed to the current true state only, with the withdrawn
   history dropped rather than narrated.
3. **Two boundary cases the parallel workers correctly declined to
   touch**, fixed by hand afterward: `cyprian_opera-spuria-vita-pontius-
   lat_hartel-csel3-pars3.yaml` and `didymus-alexandria_de-trinitate-
   lat-grc_mingarelli1769.yaml` each had review/date narration sitting
   inside a `locus:` field's own string value rather than in `note:`.
   For the Cyprian one, the real reasoning (why the work stays under
   Cyprian's name — the transmitted-author shelf, not re-attributed)
   was moved into `note:`, restated in present tense, and `locus:`
   trimmed back to a physical description. For the Didymus one, the
   locus's current line number was already correct; only the "corrected
   `<date>`, Round 2 Opus review, from a stale reference the Round 1
   header fix itself invalidated" narrative was dropped, since it
   carried no standing information the corrected locus doesn't already
   state.
4. **Top-level docs, hand-edited directly** (not generated):
   `README.md` (7 spots — a Mark quote/date explaining why this sits
   outside `records/`, a stale count-snapshot date, "both were added
   `<date>`", two stale seeded-count-as-of-date table cells, a code
   comment's dated usage note, a coverage-feed sign-off date, a
   Mark-sign-off parenthetical on the `address` field's own semantics);
   `AUTHOR-IDS.yaml` (dropped the verification date, kept "verified via
   WebSearch"); `PAIRS.yaml` (dropped a bare "Decision-Log entry 4"
   pointer, kept the still-live CM-3/D3§3 spec references);
   `WORKS.yaml` (5 spots — a Mark-sign-off date on the `work_id` field's
   own contract, three "verified via WebSearch, `<date>`" tags, one
   "confirmed by direct read ..., `<date>`" tag — all restated dropping
   only the date); `work_coverage_diff.py` (a dated worked-example
   citation, and "fooled a human reviewer" restated as "found").
   `fixture-synthetic.yaml` (the one HAND-AUTHORED bucket file — see
   its own header) had one "Decision-Log entry 10" pointer dropped the
   same way as `PAIRS.yaml`'s.
5. **`ATLAS-TARGETS.md`** is generated by `cic/engine/atlas_targets.py`
   from `cic-website/data/world-census.json`; the committed file was
   also measurably stale (7 vs. 11 `Built & Live` entries, an old
   tradition name) — the same shape as item 1's `atlas-v3.html` embedded
   census. Fixed the one hardcoded process-narration string still in the
   generator's own `render()` (a "hand-typed... caught `<date>`" clause;
   the rest of the generator was already clean) and regenerated the
   file — the drifted count and name fixed themselves as a byproduct.
6. **`CELL-VOICE-WORKLIST.md`** and **`RETRIEVAL-HINTS.md`** were the
   two densest cases in this surface: both read as full engineering
   retrospectives (specific probes run, specific bugs found and fixed,
   "Measured/Recorded/FIXED `<date>`" narration) rather than the
   reference documents their own titles promise ("the standing check",
   "the discipline"). The checker caught only one or two lines in each
   (bare dates); a full manual pass, per the litmus test, restructured
   both down to durable rules/architecture facts stated in present
   tense (the locator-token discriminator and ruling table in
   `CELL-VOICE-WORKLIST.md`; the seven hint-writing rules, the two
   honest remedies, and the scorer's known weighting/follow-up behavior
   in `RETRIEVAL-HINTS.md`), dropping the day-by-day investigation
   narrative and specific probe-by-probe journal entries. Nothing
   asserted in the trimmed versions is invented — every kept sentence
   restates a finding the original text already stated, without the
   who/when wrapper.

### Regenerated (not hand-edited)

Ran `python3 cic/engine/corpus_map_merge.py` once all 133 staging files
were clean: writes all 58 generated per-tradition bucket files plus
`UNATTRIBUTED.yaml` from the now-clean `_staging/` sources. `--check`
first (clean); the real run reported `877 work assignment(s) across 58
Atlas entry(ies)... valid.` and one pre-existing, unrelated finding
(`fixture-synthetic.yaml` is hand-written and not staging-derived — as
documented, expected, left alone).

### Left open — genuinely unresolved editorial questions (ROUTE)

None of these were resolved by this program, per its own scope (never
alter which work maps to which tradition; a ROUTE item's job here is to
stop attributing the question to "Mark"/"a reviewer" and state it
plainly, not to answer it). All were already open before this PR;
several already carry `confidence: needs-ruling` in their own
`_staging/` entry. Listed here rather than filed into a world's own
`Open_Gaps_Tracking.md`, because most of the atlas_ids below are not
built worlds (no per-world gaps file exists to receive them), and
because attempting to regenerate `worlds/_cross-world/NEEDS-RULING.md`
myself surfaced a real defect (below) that made hand-filing safer than
mechanical regeneration this round. Recommend the corpus-map thread (or
whoever owns that cross-world file) do the actual filing/regeneration
with the full context these items need.

- `anf01`, *Epistle of Barnabas* (`post-apostolic-house-church`):
  whether to also add `alexandria-catechetical`, given argued
  Alexandrian provenance vs. that entry's c.150 window start.
- `anf01`, *Against Heresies* `ebionite-nazoraean-current` context row:
  whether a locus-level extract, not the whole work, is the better fit.
- `anf03`, *Apology* (Tertullian) `post-apostolic-house-church` row:
  whether pahc should reach this work through `latin-apologists`
  instead of citing it directly.
- `anf03`, *The Prescription Against Heretics* context row
  (`valentinian-and-other-gnostic-christianities`,
  `marcion-marcionism`): whether its thinner heresiological description
  still justifies the context assignment.
- `anf03`, *Passion of Perpetua and Felicitas* (`latin-apologists`):
  whether `montanism-the-new-prophecy` should also be added, given real
  but not-yet-chosen New Prophecy affinity scholarship.
- `anf03`, *Against Praxeas* (`montanism-the-new-prophecy`) row: still
  literally reads "a ruling for Mark, not a parsing fact" — not caught
  by the checker (no date/ruling-keyword match), flagged here as a
  gap in the checker's own patterns as well as a genuinely open item.
- `anf05` header and several Hippolytus-of-Rome rows (Refutation,
  Christ and Antichrist, Against Noetus, Exegetical/Dogmatical/
  historical fragments, Appendix) plus the Caius row: Hippolytus has no
  census entry at all; every row sits provisionally under
  `roman-church-third-century` pending a ruling on a proper shelf.
- `anf06`, *The Passion of St. Symphorosa and Her Seven Sons*
  (`post-apostolic-house-church`, `confidence: needs-ruling`): both the
  attribution to Julius Africanus and the shelf assignment are open.
- `anf06`, *Of the Manichaeans* (Alexander of Lycopolis)
  (`manichaeism`): whether the author is an orthodox bishop or a pagan
  Platonist is unresolved, which affects whether `role: context` is
  even the right call.
- `npnf214`, *The Canons of the Council of Ancyra* and five sibling
  provincial-canon entries (Neocaesarea, Gangra, Antioch-in-Encaeniis,
  Laodicea, Constantinople-394) (`imperial-juridical-christianity`):
  whether a finer/more specific home should exist for provincial
  disciplinary canons.
- `npnf214`, *The Apostolical Canons* (`imperial-juridical-christianity`,
  `apocryphal-and-pseudepigraphal-literature`): whether this should be
  placed with its sibling text, the Apostolic Constitutions (assigned
  separately in `anf07`), under one unified ruling.
- Duplicate census entries `cyrilline-miaphysite-egyptian-tradition`
  and `cyrilline-miaphysite-egyptian-christianity`: which should carry
  corpus assignments generally (affects `npnf214`'s Council of Ephesus
  431 tradition row and `npnf212`'s Letters of Leo the Great).
- `anf02`, *Address to the Greeks*/*Oratio ad Graecos* (Tatian): whether
  his later Encratite branding and eastern/Syriac career mean his voice
  belongs with pahc or the Syriac tradition instead.
- `anf02`, *Plea for the Christians*/*Resurrection of the Dead*
  (Athenagoras): whether a better home than the era-1 mainstream entry
  may turn up in a later survey.
- `anf02`, *The Stromata* context row (Clement of Alexandria)
  (`valentinian-and-other-gnostic-christianities`): whether
  locus-level extracts should be added for the Valentinus/Basilides/
  Isidore/Carpocrates material, and whether the Marcion material
  should ground a separate `marcion-marcionism` context assignment.
- `codex-theodosianus`, second assignment (`donatism`, `confidence:
  needs-ruling`): whether/how CTh belongs in Donatism's bucket —
  context, antecedent, or narrower (CTh 16.5/16.6).
- `codex-theodosianus`, third assignment
  (`imperial-juridical-christianity`, `confidence: needs-ruling`):
  whether CTh is that entry's own context or tradition, pending that
  world's Doc_01/Doc_02.
- `npnf210`, *On the Holy Spirit* (Ambrose): a `homoian-arian-
  christianity` id could be added by analogy with *De Fide*.
- `npnf203`, Rufinus' translation prefaces (`alexandria-catechetical`):
  may be worth dropping to sub-work-level instead of a grouped context
  row.
- `npnf209`, *De Fide Orthodoxa* (John of Damascus)
  (`melkite-arabic-christianity`): a Byzantine-imperial-church id could
  be argued for instead of or alongside.
- `npnf101`, Manichaeism context row (Confessions Books III-V)
  (`manichaeism`): `npnf104`'s dedicated refutations could carry that
  bucket alone instead.
- `ephraim_prose-refutations`, *Against Bardaisan's "Domnus"* and
  *Against Bardaisan (A Discourse Against Bardaisan)*
  (`bardaisanite-current`): whether a dedicated Bardaisan/Daisanite
  entry, or folding into the Syriac world alone, fits better than the
  current floor entry.
- `chronicle-of-edessa`, *The Chronicle of Edessa*
  (`syriac-orthodox-west-syriac-christianity`): whether a
  composition-era (c. 540s) placement is wanted for this entry at all.
- `npnf104`, *The Correction of the Donatists* (Letter 185)
  (`imperial-juridical-christianity`): whether ijc should instead be
  reached through the imperial laws themselves rather than through
  Augustine as North African advocate.
- `npnf107`, *Soliloquies* (`latin-pastoral-congregational-
  christianity`): whether the Cassiciacum period should also touch
  `ambrosian-milan-standalone`.
- `anf08`, *Excerpts of Theodotus* context row
  (`valentinian-and-other-gnostic-christianities`): now that the text
  is confirmed to be the Eclogae Propheticae rather than genuine
  Valentinian material, whether it belongs in this context entry at
  all.
- `anf08`, Fragment of Maximus of Jerusalem
  (`palestinian-church-pre-constantinian`): attribution disputed (the
  fragment circulates with Methodius' material).

### Flagged, not fixed (out of scope here)

- **`worlds/_cross-world/NEEDS-RULING.md` / `gen_needs_ruling.py` has a
  real data-loss bug.** The file's own header claims it is fully
  "Generated by `gen_needs_ruling.py`", but its committed copy carries
  a fourth, hand-appended "question that is not per-work" (a
  multi-paragraph methodology finding about the census `era` field)
  that does not exist anywhere in the generator's own source. Running
  `gen_needs_ruling.py` after this PR's corpus-map fixes (to pick up
  the reworded `needs-ruling` notes and the corrected 5→6 work count)
  silently dropped that fourth question and relabeled the section
  "Three questions". Reverted that regeneration rather than ship the
  loss (`git checkout -- worlds/_cross-world/NEEDS-RULING.md`);
  `worlds/_cross-world/` is untouched by this PR. Flagged for whoever
  owns that file: either the generator needs to actually incorporate
  that fourth finding as data, or the file needs a documented
  hand-maintained section the generator preserves on rewrite — right
  now, running it as-is is destructive.
- The ROUTE items above are not filed into any per-world
  `Open_Gaps_Tracking.md` or `WANTS-REGISTER.md`, for the reasons
  stated in that section.

### Validation

- `python3 -c "..."` YAML parse check across all 133 `_staging/*.yaml`
  files → 0 bad.
- `python3 cic/engine/corpus_map_merge.py --check` → clean, then the
  real run → `877 work assignment(s) across 58 Atlas entry(ies)...
  valid.`
- `tools/check_live_commentary.py --surface cic-corpus-map` → **0 hits**
  (was 761).
- `tools/check_live_commentary.py` (full repo) → every other surface's
  count unchanged from before this PR (cic-website 1, cic-poc-frontend
  1, cic-engine 19, engine 1229, records 2841, reference 261, worlds
  16541, fixtures 8, canon 28, packages 0).
- `tools/check_paths.py --baseline tools/check_paths_baseline.txt` → 0
  new/retired.
- `tools/check_no_embedded_world_data.py` → exit 0.
- `cic/engine/works_registry.py --check` → OK, 4 works, all external_ids
  and item addresses valid.
- `cic/engine/author_ids.py --check` → OK, 5 authors, all well-formed.
- `pytest tools/tests/test_check_live_commentary.py` → **88/88 passed**
  (refreshed 17 stale `HAND_LABELS` entries this cleanup itself made
  stop matching, moving them to fresh `worlds/` examples — item 4, not
  yet touched by this program; table grew from 85 to 88 entries in the
  process, still well above the ≥60 floor).

---

## Entry 4 — `worlds/_cross-world/gen_needs_ruling.py` data-loss fix (PR #510)

Fixes the data-loss bug flagged in Entry 3's "Flagged, not fixed" note
above. `gen_needs_ruling.py` regenerates `NEEDS-RULING.md` from
`cic/corpus-map/`; the committed file also carried a hand-appended
fourth "question that is not per-work" the generator's own source
never produced. A regeneration after Entry 3's corpus-map fixes
silently overwrote that section.

**2026-09-24, Mark (via the managing thread, delegated verdict
authority).** Round 1: FAIL. The marker-preserving design (everything
below `HAND_MAINTAINED_MARKER` in the output file is read back from
the existing file and reproduced verbatim, rather than regenerated)
was confirmed correct, but the fix was still in the same data-loss
class — `extract_hand_maintained()` fell back to a placeholder,
silently discarding real content, whenever an *existing* file's marker
was missing, rather than only doing that on a genuine first run (file
absent). Required before round 2: (1) make a missing marker on an
existing file a refusal to write, not a placeholder; (2) remove this
bug's own "found 2026-09-24" story from the live script's and test's
docstrings/comments, since `worlds/` is itself a live surface this
program governs — the story belongs here instead; (3) cut
`NEEDS-RULING.md`'s new "Placement questions" section intro down to
one present-tense line describing what the section holds, not a
narration of the cleanup program that produced it; (4) wire the new
test file into somewhere CI actually collects it.

Round 2 (this entry): `extract_hand_maintained()` now raises
`MissingMarkerError` when given a non-`None` existing text with no
marker, and `main()` catches it, prints an error, and returns without
writing — a first run (no file at all) still gets the placeholder.
`worlds/_cross-world/tests_gen_needs_ruling.py`'s fallback test now
asserts the raise, and a new end-to-end test drives `main()` itself
against a scratch file with no marker and asserts the file is left
byte-for-byte unchanged. The script's docstring, its
`HAND_MAINTAINED_MARKER` comment, and the test file's own docstring
were rewritten present-tense (the guarantee, not the story of finding
the bug). `NEEDS-RULING.md`'s "Placement questions" intro is now one
line. `.github/workflows/ci.yml` gained a `crossworld` path-filter
output (`worlds/_cross-world/**`, `cic/corpus-map/**`) and a new
`cross-world-tests` job that installs `pyyaml`+`pytest` and runs
`tests_gen_needs_ruling.py` — this suite had nowhere in CI before this
PR.

### Validation

- `python3 -m pytest worlds/_cross-world/tests_gen_needs_ruling.py -q`
  → 7 passed (the original 6, plus a new
  `test_main_refuses_to_write_when_an_existing_file_lacks_the_marker`).
- Three consecutive `python3 worlds/_cross-world/gen_needs_ruling.py`
  runs against the real file → idempotent, hand-maintained tail
  byte-for-byte unchanged each time.
- CI run on this PR's branch, `cross-world-tests` job → green (linked
  in the PR).

---

## Entry 5 — Program stopped: worlds/, fixtures/, and reference/ cleanup dropped

**2026-09-24, Mark (via the managing thread, delegated verdict and
sequencing authority).** Scope change, delivered after PR #510 merged
and desert (item 4, the smallest world) was underway: stop the
`worlds/` construction-document cleanup now, including the in-progress
desert work, and drop the remaining program items — `fixtures/`
(item 5) and `reference/` (item 6) — entirely. Reason given: those
three surfaces are not participant-facing, and the cost of continuing
the pass across them (twelve worlds' construction documents, at up to
79 files for the largest) is not justified once weighed against that.
`tools/check_live_commentary.py` stays in place as a report-only scan
— it keeps whatever commentary remains in these surfaces visible on
every CI run, without gating anything, so the count is not lost even
though the pass to bring it to zero does not continue.

Items 1–3 (`cic-website/`, `cic-poc/frontend/`, `cic/corpus-map/` —
PRs #501, #503, #508) and the `gen_needs_ruling.py` data-loss fix
(PR #510) are unaffected and stand as completed, merged work.

**In-progress desert work at the time of the stop, for the record:**
a branch (`step4-desert-live-surface-cleanup`, pushed but no PR
opened) held two pieces of work, abandoned per this stop directive
rather than merged:

- A `tools/check_live_commentary.py` fix protecting per-world
  `worlds/<code>/*_Decision_Log.md` files from being flagged
  (ruling 2 for item 4: these are the legitimate audit-trail
  destination this program routes provenance *to*, not a construction
  document leaking it — the checker did not yet know that when item 4
  began).
- `worlds/desert/CiC_W3_Doc01_World_Identification.md` and
  `CiC_W3_Doc02_Source_Ecology.md`, cleaned of inline "per Round N
  review, Finding X" provenance and a duplicated "Document log"
  section (already fully carried by `CiC_W3_Decision_Log.md` and the
  still-protected `Doc_0N_Review_RoundN.md` files), as the worked
  model for the other eight canonical Doc files. Doc_03 was in
  progress, unverified, when work stopped; its edit was discarded.

None of this is merged, none of it is lost — the branch remains on
the remote, unreferenced by any open PR, should this program resume
later.

**Process-note move candidates identified, for the record** (per
item 4 ruling 4(b): these were never in scope to strip, only to list
as candidates for a later, separate structural move to
`worlds/<code>/build/` or `Ministry/`, a move this stop directive also
does not authorize):

- **Desert-specific**, confirmed directly: `CiC_W3_Guided_Starters_V0_1_DRAFT.md`
  and `CiC_W3_Phase6_Facilitation_Brief_DRAFT.md`.
- **The general shape**, named in the original item-4 ruling but not
  re-enumerated per world before the stop (most worlds' own file lists
  were never individually surveyed): `STATUS-FOR-SOURCE-THREAD.md`;
  `G0`/`G1`/`B1a`/`B8`/`B9`/`PhaseC` scoping/coverage notes;
  `Phase*_DRAFT.md`; dated Step 0 confirmations; a world's own
  `Source_Acquisition_Manifest` where it is a working log rather than
  a settled record.
- **`worlds/_cross-world/`**, per item-4 ruling 5 (that surface's own
  PR, never started): dated audit/brief documents —
  `CiC_Cross_System_Consistency_Audit_2026-08-26.md`, `BRIEF-*`,
  `CASE-*`, `CORPUS-PARTITION-BRIEF`, `PLAN-*` — were identified as
  candidates to move to `Ministry/`, distinct from that surface's
  registers (`NEEDS-RULING.md`, `WANTS-REGISTER.md`,
  `SOURCE-READINESS`, `DOWNLOAD-QUEUE.md`, dossiers), which were
  ruled to stay and keep their ROUTE hits as their own function.

**Disposition:** the Live-Surface-Cleanup program closes here. Items 1–3
and the `gen_needs_ruling.py` fix are the program's completed scope;
items 4–6 are stopped, not deferred to a later phase of this same
program — any future work on `worlds/`, `fixtures/`, or `reference/`
commentary is a new decision, not a resumption of this one.

---

## Entry 6 — witt: REWRITE removals, PR #506 (branch `step1-live-surface-cleanup-pr-witt`)

**Note on Entry 5, above.** This entry's own program — cleaning `records/<world>/*.md` per world, one PR per world initially, batched into three PRs from alx onward per the managing thread's own 2026-09-24 scope-change directive — is a separate, ongoing track from the "Live-Surface-Cleanup program" Entry 5 closes. Entry 5's items 1–6 never enumerated the `records/` per-world track; its "the Live-Surface-Cleanup program closes here" refers only to its own four items. This program continues under its own separate authorization.

**What was removed.** Every line `tools/check_live_commentary.py` classified REWRITE across `records/witt/*.md` (252 line-hits, roughly 150 distinct files), resolved by pure word/token/sentence deletion — no wording invented. Two shapes:

1. **Internal citation/ruling leaks** (the large majority): a "Source Registry R##" row citation, a bare `R\d\d` ruling number, or (inside a record type's own SPOKEN field per `engine/m1/spoken_fields.py`) a `Doc_0N`/`§N` citation or a formation_confidence-taxonomy word used as a spoken predicate ("is Documented"). Removed in place; the surrounding sentence's substantive claim is unchanged. Full file:line list is in PR #506's own body, not duplicated here.
2. **Settled correction narrative**, removed whole rather than token-trimmed, once re-reading confirmed the record's own current fields already state the corrected fact and the narrative explaining how it got there carried nothing else:
   - `witt.figure.brussels-martyrs-john-and-henry`, `witt.story.brussels-martyrs` (`confidence.divergence_note`): "the Registry's own technical correction fixed an earlier, unverified 'Augustinian friars' wording to what the text actually supports."
   - `witt.core.witt` (world_core body): three "CORRECTION:" paragraphs on how `.thinness`/`.cautions`/`.thin_topics` reached their current 1525/1543 treatment (the Doc_10-review reversal logged there as OG-15; a follow-on `.thin_topics` fix; a two-part overclaim fix).
   - `witt.voice.craft` (voice_craft body): a "QUOTE / DOCTRINAL_WITNESS GAP" passage (self-labeled "kept as the historical record... not a description of this world's current store") and two "CORRECTION:" paragraphs on the `guard` field's 1525/1543 wording.

**Where it moved from.** `records/witt/*.md` — bodies and front-matter free-text fields, per the file:line list in PR #506's own body.

**Where the settled-history detail lives.** `worlds/witt/build/BUILD-LOG.md` (created; witt had no build log before this PR) carries the fuller account of the five whole-paragraph removals in item 2, including what each record's own current fields say and how that was confirmed before deleting the narrative. This entry is the pointer; that file has the reasoning.

**One open item ROUTE'd, not REWRITE'd.** `witt.source.marburg-articles`'s inline "Doc_01 open item 1 / §7" note moved to `worlds/witt/Open_Gaps_Tracking.md` OG-33 (the Marburg Articles remain unvendored) — a still-open acquisition gap, not settled history, so it belongs there rather than here. (Renumbered three times during rebase past concurrently-merged PRs from other threads: originally filed as OG-32/Entry 1, then OG-33/Entry 4 once `Entry 3`'s own corpus-map PR claimed OG-32 for witt first, then Entry 5 once PR #510 claimed Entry 4, then Entry 6 once PR #511 claimed Entry 5 — see `worlds/witt/Open_Gaps_Tracking.md`.)

**Eighteen items left unedited**, flagged Words-for-Mark in PR #506's own body: pure deletion would break grammar or destroy real content (most commonly a formation_confidence word fused as a sentence's own verb — "is Documented", "is Contested" — with no way to remove it without either inventing a replacement or losing the clause's only content). Awaiting Mark's wording, not resolved here.

**Known gap, not addressed by this PR.** `tools/check_live_commentary.py` is a line-based scan and does not reliably catch a multi-paragraph narrative block where only one line independently matches a pattern while the surrounding sentences carry the same process narrative without their own trigger word — found in this PR only by re-reading the paragraph around an already-flagged line, not by the tool. Both `witt.core.witt` (world_core) and `witt.voice.craft` (voice_craft) turned out to carry this shape. Other worlds' `world_core`/`voice_craft`/`world_front` records likely do too and have not been checked here — flagged in `worlds/witt/build/BUILD-LOG.md` and PR #506's own body for whoever runs the next world's pass.

---

## Entry 7 — alx: REWRITE removals, PR #509 (branch `step1-live-surface-cleanup-pr-alx`)

**Note on numbering:** this branch forked from `main` before witt's PR #506 merged, so it
originally claimed "Entry 1," then renumbered twice more on rebase past concurrently-merged
threads (Entry 6, then this final renumbering to Entry 7 once witt's own PR #506 merged and its
entry landed on `main` as Entry 6 first).

**What was removed.** Every line `tools/check_live_commentary.py` classified REWRITE across
`records/alx/*.md` (145 line-hits at scan time, across ~90 files), resolved by pure word/token/
whole-clause/whole-paragraph deletion — no wording invented, except two cases restated in present
tense per witt's own round-1 verdict. Two shapes, same as witt's own entry:

1. **Internal citation/ruling leaks** — a ruling number, a dated "Rights verified" opener, a
   "REVISED"/"BAR SWEEP"/"LEXICON LABEL PASS"/"REGISTER TRANSLATION" boilerplate line. Removed in
   place. Full file:line list is in PR #509's own body.
2. **Settled correction/build narrative**, removed whole once the record's own current fields
   were confirmed to already state the corrected fact: two "RULING RECORD (Mark, 2026-08-21...)"
   blocks and a dated readability-fix narrative in `alx.voice.craft`'s body; the entire
   builder-addressed body of `alx.front.alexandria-catechetical` (a `world_front` record — its
   body is never read by the compiler, confirmed against `engine/m2/site_compiler.py`); and
   roughly a dozen "CORRECTED"/"BAR SWEEP"/"Reciprocal relation added" paragraphs across
   `doctrinal_witness`, `demonstration`, `story`, `force`, `gravity`, and `source` records.

**Two lines restated in present tense rather than deleted or left broken**, per witt's own
round-1 verdict ("if it records a still-true fact about the record, state that fact in present
tense"): `alx.quote.athanasius-made-god`'s ellipsis-justification note and
`alx.demo.someone-like-me`'s sanctioned-alternative note — both kept their real, still-true
reasoning; only the dated/"Mark's own" attribution framing was dropped.

**Where it moved from.** `records/alx/*.md` — bodies and free-text fields, per the file:line
list in PR #509's own body.

**Where the settled-history detail lives.** `worlds/alx/build/BUILD-LOG.md` (created; alx had no
build log before this PR) carries the `world_front` record's own build narrative in full,
including the now-resolved `modern_rendering` coverage finding (1/26 at build time, 26/26 now,
per commit `da3f1a77` and two follow-ups) — recorded as settled history, not filed as a fresh gap.

**Two open items ROUTE'd, not REWRITE'd:** `worlds/alx/Open_Gaps_Tracking.md` OG-9 (Didymus's
Tura material has no public-domain English translation) and OG-10 (`alx.source.origen-on-
prayer-curtis`'s unresolved chain-of-custody caution) — both still-open, not settled, so they
belong there rather than here. (Renumbered from this entry's original OG-8/OG-9 once PR #508's
own corpus-map pass claimed OG-8 for alx first — see `worlds/alx/Open_Gaps_Tracking.md`.)

**Nothing left as an unresolved Words-for-Mark item.** Every candidate either resolved by
deletion, resolved by present-tense restatement (above), or was confirmed KEEP
(`alx.quote.timothy-ordinary-questions`'s "RULED ON" — the in-world bishop Timothy's own
ruling, not this project's review process).

---

## Entry 8 — Website/app re-check (`cic-website/` and `cic-poc/frontend/`), and a standing rule change order

**Trigger.** PR #512 refined `tools/check_live_commentary.py` (five precision/recall additions,
including the `era-gate` and `route-cue` patterns), and a re-scan of the two participant-facing
surfaces under the refined tool reported 145 hits in `cic-website` (58 REWRITE, 86 ROUTE, 1 KEEP)
and 28 in `cic-poc/frontend` (24 REWRITE, 4 ROUTE). Every hit was classified by hand; only real
commentary was fixed. The full per-hit classification, with reasons, is in this entry's own PR
body rather than restated here.

**What was actually commentary, and got fixed:**

1. **`cic-website/data/world-census.json`'s `statusDescription` field, 255 not-yet-built
   entries — corrected from an initial undercount of 43.** This field is the census's own
   hand-authored status line — confirmed by checking its value on the six built-and-live entries,
   which all read a single plain sentence ("You can sit down with this tradition now."), and by
   `engine/m6/census_sync.py`'s own scope: it only syncs `statusDescription` from the registry for
   `status == "Built & Live"` rows, so every flagged row here (`"Pre-Survey Candidate"`, `"Floor
   Question (register)"` and `"Label - Assessed Per Body (A3)"`) is hand-authored in this file
   directly, not a generated mirror of something else. 255 of these entries had drifted into full
   internal-review paragraphs — "Reviewed at the Era N Step 0 run and tiered X (Tier N)...",
   "corrected/routed/decided/named/ratified at the gate/Freeze", "flagged forward", "Named in the
   Step 0 record...", "Carries a named creedal question for a future Step 0..." — the survey
   pipeline's own review vocabulary, not content about the historical movement each row
   describes. **The first pass's 43 came from filtering to `tools/check_live_commentary.py`'s own
   `era-gate`/`route-cue` hits**, which only match lines containing "at the gate/Freeze" or an
   open-item phrase; most of the drifted paragraphs don't contain either — they just open
   "Reviewed at the Era N Step 0 run" and never mention a gate or an open question by name, so the
   checker never flagged them at all. Re-verified with a direct scan for `"Reviewed at`/`"Proposed
   by`/`"Named in the Step 0 record`/`"Carries a named creedal question` openers across every
   movement regardless of checker output: 255 found, all rewritten, 0 remaining, confirmed by a
   final regex sweep for `Step 0|Era \d+|Freeze|ratified|at the gate|RETAINED|BANKED|floorNote|
   continuesAs|dateRationale|statusWord` across the whole file. Rewritten to plain status language,
   keeping every substantive fact (sourcing quality, access limits, window dates, real editorial
   judgment calls about scope, disclosed uncertainty) and dropping only the process framing. Two
   entries (the Templar-trial and Old Believers rows) also leaked the internal field name
   `floorNote` into their own rewritten text on the first pass — caught on review and fixed to
   "its note on the doctrinal floor." `engine/m6/tests/` (census/atlas sync) and the site
   `staleness-check` both still pass — this field isn't synced or compiled into anything, so
   nothing downstream depended on its old wording.
   **Open item, not fixed here:** `statusWord`, this field's sibling and also visitor-facing,
   still carries the same process vocabulary on 233 of 292 rows — a public-vocabulary design
   decision, not a commentary cleanup, so it's logged for Mark's ruling rather than rewritten:
   `Ministry/Features/Atlas-World-Map/Decision-Log.md`, entry "2026-09-25 — Open question for
   Mark: `statusWord` still carries public-facing process vocabulary."
2. **The Atlas census's own `"notes"` field** (identical text duplicated at
   `cic-website/atlas-v3.html:428` and `cic-website/data/world-census.json:21`) — trimmed to keep
   the load-bearing "single source of truth, read by these surfaces" statement and the schema
   note about numeric date fields, and drop the reconciliation narrative (a named xlsx version
   disagreeing with `world_manifest.py`, "bringing the live count to 6") that belongs in this
   Decision Log's own history, not in a live data file's own notes field.
3. **`cic-poc/frontend/src/data/pairings.ts`'s docstring** claimed the C6 pairing record
   (`Ministry/Technology/CiC_Table_Pairings_V1_2026-08-28.md`) was "still pending approval."
   Checked against `Ministry/Technology/CiC_FrontEnd_Decision_Log.md`'s own 2026-08-28 entry:
   Mark's "ok it works for me. make this a go." on the same day signed off the C6 launch set as
   the tray's offered seatings. The DRAFT/pending-approval claim was stale by a month; removed.

**Fidelity re-check on the `statusDescription` rewrites: a ruling stays a ruling, not a fact.**
Where the original text said something was ruled or decided on stated grounds — not just a
scope/filing choice (which row a topic sits in) but a substantive claim about the historical
subject itself — the rewrite keeps the grounds visible rather than flattening it into a plain
assertion. Checked systematically after the managing thread flagged the risk with the Moravian
succession entry (kept correctly: "on the strength of a literal-renewal claim and refugee-carried
continuity across that 95-year gap"). Two entries had dropped the grounds entirely on the first
pass and were corrected: the Athonite-succession entry (Hesychasm/Palamite Synthesis) now reads
"it succeeds from the Athonite entry as a direct continuation" with the classification kept
visibly a classification, not an unqualified historical claim; the Optina-succession entry
(Paisius/Philokalia) similarly. The clearest case is the recency-exception entry (a 2016-onward
movement kept on the map despite failing this survey's own age bar): rewritten as "kept anyway,
on record as a deliberate exception," not as if inclusion were simply the neutral, obvious
outcome. "This status is a dated reading of a living tradition,
not a permanent verdict" — the Living-Era Protocol's own hedge — was kept verbatim everywhere it
appeared, rather than dropped as process framing, because it is itself a fidelity safeguard, not
narration about how the safeguard was adopted.

**What was flagged but is not commentary, and was left as-is (KEEP):**

- **17 `era-gate` hits, all literal historical gates**, not the project's own "Freeze" gate: a
  monastery's tower gate, a palace gate a bishop walks past, a convent gate, the satirical
  *Julius Excluded from Heaven*'s gate of the afterlife, and (repeated across `atlas-v3.html`,
  `world-census.json`, and the compiled `tree/` and `traditions/` pages that carry the same
  underlying text) Patriarch Gregory V hanged at the gate of the Constantinople patriarchate in
  1821. The `era-gate` pattern matches "at the gate" regardless of which gate; these are all the
  wrong kind.
- **`route-cue` hits, almost all genuine emic/etic scholarly hedge language about the
  historical subject matter** (86 at scan time, before this entry's own `statusDescription`
  rewrites; several of those rewrites deliberately kept or introduced plain "a real, open
  question" phrasing to preserve fidelity — see above — which the checker now also reads as
  `route-cue`, bringing the live count to 95; all still the same kind of legitimate content),
  not the project's own open items: "Creedal question — not yet
  resolved" status labels, `floorNote`/`legacy`/`why` fields naming a real unresolved historical
  or doctrinal question (Paul of Samosata's teaching, the Testaments of the Twelve Patriarchs'
  authorship, Kyrion II's 1918 death, the filioque-adjacent Consensus Tigurinus question), and
  the seven compiled per-world JSON files' own `_generated_by` provenance header (build/commit
  metadata, not narrative). This is exactly the "uncertainty stated plainly" register this
  project's own accessible-and-rigorous standard asks for — fixing it would mean flattening real
  scholarly caution into false certainty, the opposite of the rule's intent.
- `cic-website/support.html:127` — already correctly marked KEEP by the checker itself
  (visitor-facing fundraising copy naming "external reviewer", not project review narration).
- `cic-poc/frontend`'s remaining 24 REWRITE + 3 ROUTE hits are all legitimate engineering
  documentation: a CSS-positioning bug write-up (`Level2Card.tsx`, flagged only on the phrase
  "caught by"), a real spec-document filename (`FigureBridgeMark.tsx`), a `sessionStorage`
  edge-case comment (`App.tsx`, flagged on "was still open"), a regression test's own name
  describing an intentional legacy-path limitation (`VoiceTurnBody.legacy-default.test.tsx`), and
  a server error-string comparison (`api.ts`, flagged on the literal string `'round still open'`
  it matches against).

**Rebuild/repin.** Not needed — every edit landed in a field neither `engine/m2/site_cli.py`'s
compiler nor `engine/m6`'s census/atlas sync reads or mirrors; `staleness-check` confirms all ten
built worlds' pins are unchanged.

**Change order — standing rule added to `CLAUDE.md`.** Per Mark's 2026-09-24 approval: added one
sentence to "Keep the live/canonical surfaces clean," directly after the paragraph ending "treat
that as corruption: remove it, don't add to it.": *"Any PR that edits a live or canonical file
also removes the commentary already in that file; the check in `tools/check_live_commentary.py`
shows what is there."* This replaces the dedicated Live-Surface-Cleanup campaign (this program)
going forward: the remaining known commentary in `engine/`, records-body/notes/locus text,
`reference/`, and `worlds/` construction documents is cleaned file by file, as real work already
touches each file, rather than swept in its own dedicated pass. This entry is that change order's
record.

---

**Entry 12 — 2026-09-25, "yes, widen the fleet checks" (Mark's ruling) and "yes, merge verified
PRs" (Mark's ruling), same session.**

Root cause this ruling answers: every re-voicing and rendering PR up to this point carried build
vocabulary and readability slips into spoken text that neither `tools/check_live_commentary.py`
nor `gate_readability` (`engine/m1/gates.py`) caught on their own — only a per-PR Opus adversarial
review did. Mark's ruling: *"yes, widen the fleet checks."*

Widened, both mechanically:

- `tools/check_live_commentary.py`'s `SPOKEN_VOCAB_PATTERNS` gained six new patterns, scoped (like
  the five already there) to a record's own declared SPOKEN fields only: `six-test-vocabulary`
  (Doc_04's Repetition/Dependency/Formation/Explanatory Power/Persistence/Interaction test names,
  PASS/FAIL grading, `SIX-TEST`/`N/6 tests`, `AUTHOR-GRAVITY RISK`), `cross-check-label`,
  `gravity-classification-label` (Primary/Supporting/Tensional as a gravity class, `Tier N`),
  `all-caps-section-header` (literal build-template headers — `LAYER 1/2/3`, `SIX-TEST SUMMARY`,
  `CROSS-CELL CONNECTION`, `WHY PRIMARY RATHER THAN SUPPORTING` — not a generic
  "2+ capitalised words" rule: that generic version was tried first and dropped after it flagged
  `pahc.core.house-church.md`'s own clean `cautions` field, which numbers its points with
  invented editorial labels, not copied build-template headers), `matrix-cell-code` (Doc_08's
  `Cell 2B`/`Force 2B-1`/`[2B - ongoing/internal]` notation), and `build-history-language`
  (`Finding S4`, "an earlier version," "this build's own," "original assessment" — "Round N" was
  already caught fleet-wide by the existing `review-round` pattern and is not re-declared). Still
  report-only (never fails CI — `.github/workflows/ci.yml`'s "Live-surface commentary scan
  (report-only)" job, unchanged). Fleet hit count from the new patterns alone, current main (PR
  #547 already merged, desert's own count below is post-merge): 741 across 12 worlds (don 195,
  lpc 148, witt 128, gallic 81, cappadocian 74, alx 28, desert 22, pahc 20, hal 17, ijc 16, rzg 6,
  syr 6) — every one pre-existing content the narrower pattern set never saw, not new drift. A
  widespread, previously-invisible finding among these: gravity/force
  `name` fields fleet-wide (found even on alx and hal, the fleet's own exemplar worlds) carry a
  bracketed build-taxonomy tag (`"Divine Pedagogy [SUPPORTING - explanatory framework]"`) that
  `engine/m4/citation_cards.py`'s own `_short_name` already strips before a citation card shows
  it, but `engine/m2/builders.py` `build_prompt()`'s own Gravities-list line (`g.get('name')`)
  does not — the raw tag reaches the model's own prompt context, unstripped, every turn, for
  every gravity in the fleet. Flagged here as a recommended follow-up (a `build_prompt()` fix, not
  a per-record rewrite) rather than fixed in this PR, which was scoped to the checks themselves.
- `gate_readability` (`engine/m1/gates.py`, registered in `gates.GATES`, CI-blocking via
  `engine.m9.cli check`) widened from four hand-listed fields (`term.quick_meaning`/
  `plain_meaning`, `honest_limit.statement`, `quote.modern_rendering`, `voice_craft.identity`/
  `guard`/`flavor_notes[].note`/`characteristic_concerns[]`) to every field
  `engine/m1/spoken_fields.py`'s own `SPOKEN_FIELDS` registry declares under an
  `instruction`/`voice-diet`/`evidence-head` role (`fields_with_role`, already built for exactly
  this reuse) — `gravity.description` and `force.description` by name, plus `world_core`'s four
  fields, `fleet_voice`'s six, `story.tellable_as`, `demonstration.exchange`,
  `doctrinal_witness.text`/`positions`, `contested_claim.claim`, `figure.bridge_line`, and
  `ambient.detail`. `participant-label` fields (a term's `world_word`, a figure's `names`, a
  quote's `speaker_or_author`/`sources`, a source's `work`, and gravity/force's own `name`) stay
  ungraded by design — short labels and proper nouns, not composed prose. `quote.text` and
  `story.text` stay excluded by the same design already in force for `modern_rendering`/
  `tellable_as`: each is the record's own verbatim/archaic original, never pressured toward a
  grade level. Second scored threshold added: Flesch Reading Ease, `FRE_FLOOR = 60` — the North
  Star decision's own already-ruled number (`reference/method/Pass2-decisions/
  VR_1A_NorthStar_Readability_Target_2026-08-09.md`, "RULED — hard edge": "Any single emitted turn
  breaching FK <= 10 / FRE >= 60 fails the world"), not an invented one; `engine/m1/fk.py` gained
  `fre_score` using the identical word/sentence/syllable counts `fk_grade` already computes. The
  North Star decision's FK-8 band floor stays report-only, not gated, exactly as that decision
  itself rules ("reported, not failed... FLATTENING, not FK, guards against emptiness"); a
  sentence-length ceiling (CLAUDE.md's "practical shape" guidance, ~25 words) was considered and
  NOT added — `engine.m1.cross_world.observe_register_profile` already measures sentence length
  per spoken field and stays deliberately OBSERVATION-only pending Ruling R6
  (`Ministry/Features/Conversation-Transparency-Engine/Rulings-Pending.md`), which has not yet
  been made; gating on it here would pre-empt that open ruling, not honor "don't invent new
  thresholds."

  Full-fleet run (11 built/admitted/open worlds; `lpc` is not yet in the registry and is not
  checked by this gate; `fix`, the fixture world, must stay 100% clean and was — six of its own
  clean fixture records scored over the new ceiling/under the new floor purely because the wider
  gate now grades fields they were never checked against before; each was shortened in place,
  meaning unchanged, `fix.craft.vera-voice.md`'s own pre-existing "REVISED 2026-09-19" commentary
  removed in the same edit per `CLAUDE.md`'s "any PR that edits a live file also removes the
  commentary already in it," `fix` now scores 0 findings on every registered gate; desert's own
  count below is measured post-merge of PR #547, which landed while this PR was in progress):
  alx 149, cappadocian 322, desert 163, don 368, gallic 135, hal 165, ijc 163, pahc 162, rzg 137,
  syr 155, witt 235 — 2,154 total, none of it new drift, all of it pre-existing content the
  narrower field set never graded. No record text in a real world was rewritten in this PR — every one of these
  11 counts is registered as its own dated `ACCEPTED_OPEN` waiver in `engine/m9/enforce.py`
  (deadline 2026-12-14, the same deadline convention already used for this fleet's other live
  content-fix waivers), so `engine.m9.cli check` stays clean and CI is not broken by the widening
  itself. Three worlds' waivers name a re-voicing PR narrowing part of their count for
  gravity/force description: desert's own PR #547 merged while this PR was in progress and its
  count above is already measured post-merge; witt's (#545) and don's (#551) are still open and
  their counts above are still pre-merge. None of the three closes its world's waiver outright,
  since every other newly-covered field (positions, exchange, claim, bridge_line, detail, the
  world_core/fleet_voice fields) is still outstanding regardless. The other eight worlds' waivers
  have no PR narrowing them yet.

  Mark and the managing thread decide, from these counts, when either check moves from report-only
  toward enforcement narrower than "everything is waived" — nothing here pre-empts that decision.

Second ruling, same session: *"yes, merge verified PRs."* The managing thread may merge a PR
itself, without asking Mark first, once an independent review has passed, CI is green on the
current head, and there is no merge conflict. Mark still personally approves: a promotion from
`main` to `live`, any change to `CLAUDE.md` or `reference/method`, any participant-visible app
change, and anything a review or the managing thread flags for him directly. This does not change
who owns driving a PR to green in the first place (`babysit`/`steward` discipline, unchanged) —
only who clicks merge once it is there.

**Entry 13 — PR #561 round 1 FAIL, corrected.** The managing thread's independent review found:

1. **CI red, root cause.** `gate_readability`'s own output changed (new fields, new FRE
   threshold), but no world's compiled package was rebuilt against it - `validation/gates-
   report.json` mismatched the pinned manifest in all 11 worlds, plus `fix`'s own compiled
   output (six records edited directly). Fixed: every world rebuilt (`engine.m2.cli build`) and
   repinned (`records/worlds/<code>.yaml`), `engine.m2.cli restore`/`staleness-check` and
   `engine.m2.site_cli staleness-check` all green.
2. **Sequencing with PR #548 (not yet merged, will land after #561).** #548's own draft declares
   `modern_term.modern_sense` as `participant-label` - a role `spoken_fields.py` defines as short
   display text ("a citation card, mark, or index entry shows directly"), not composed prose,
   despite `modern_sense` being spoken verbatim by the Facilitator's own `bridge_turn()`. #561
   now owns this cleanly instead of #548 hand-listing it: a fifth role, `facilitator-spoken`
   (`engine/m1/spoken_fields.py`) - composed, multi-sentence prose the Facilitator's own
   apparatus puts in front of a participant, spoken or read on an expanded card, never routed
   through the world's own Representative voice. `modern_term.modern_sense` and
   `.distinguishing_claim` (also multi-sentence card prose, also mis-declared `participant-label`
   in #548's draft) both take this role; `.underlying_subject` stays `voice-diet`.
   `gate_readability`'s own `_READABILITY_ROLES` now includes it. A second, real bug found while
   doing this: `gate_readability` had only ever walked a world's own `records` - `fleet_voice`
   and `modern_term` both live under `records/_fleet/`, never inside any world's own records, so
   every field this PR's own earlier pass "added" for `fleet_voice` was dead code, never actually
   graded. Fixed with a dedicated `gate_readability_fleet(fleet)` function, checked once (not
   once per world - `engine/m9/enforce.py`'s own per-world loop hands the identical `fleet` dict
   to every world's battery, so a naive per-world fleet walk would have scored the same fleet
   content once per world and multiplied its count by eleven). Reported under a new
   `FLEET_PSEUDO_WORLD = "_fleet"` pseudo-world key, exempted from the grandfathering-is-closed
   check for the reason its own code comment gives (never admitted as a world, so grandfathering
   was never a live question for it) - 9 real findings (`_fleet.voice.fleet`,
   `_fleet.contested.theophilus-triad-referent`, and the pre-#548 wording of
   `_fleet.modern.trinity`'s own `modern_sense`), waived the same way every world's count already
   is. #548's own exact adaptation once it rebases onto this PR's main: drop the hand-written
   `for rid, rec in fleet.items(): if rec.get("record_type") == "modern_term": ...` block its own
   diff adds inside `gate_readability` (its own patch header: `gates.py` around line 506-515) and
   the `participant-label` role on `modern_sense`/`distinguishing_claim` in its own
   `spoken_fields.py` diff - both already exist as of this PR, done the registry-driven way. Its
   `modern_sense` rewrite (already inside its own diff, not touched here) clears the ceiling on
   its own; `_fleet.modern.trinity`'s current, pre-#548 wording is untouched by this PR and stays
   the fleet-pseudo-world waiver's problem until #548 lands.
3. **Commentary this PR's own edits had introduced into live code**, caught by the checker
   against its own touched files: `gates.py`'s "Widened 2026-09-25 (Mark's ruling..." framing and
   its per-world waiver comment's "(see the owning Decision-Log..." pointer, both reworded to
   plain present-tense design reasoning with no date/ruling/Decision-Log citation; `enforce.py`'s
   per-world waiver `owner=` strings stripped of PR-number narration ("#547 merged and already
   narrowed...") down to what each waiver actually is (a finding and an owning thread, not a
   change history) - this file's own docstring already names exactly that distinction. Both files
   also had their pre-existing commentary removed in the same pass, per `CLAUDE.md`'s "any PR
   that edits a live file also removes the commentary already in it": `enforce.py` lost two
   admission dates in its own "two named exceptions" paragraph, an "increment 4 (date)" phrase, a
   `Decision-Log.md entry 22` citation (kept `tools/set_source_kind.py`'s own real filename
   reference), and a whole paragraph of pure change-history narration ("the five ... waivers
   registered ... were removed the same day") that carried no design reason once its provenance
   was stripped, so it was deleted outright rather than reworded; `gates.py` lost two synthetic
   illustrative dates (already using a fictional placeholder specifically so the file never quotes
   real leaked text - reworded to a non-ISO `YYYY-MM-DD` placeholder so the pattern no longer
   fires at all) and one literal `"RULED by [name]"` example (reworded to lowercase, matching what
   its own `_RULED_BY` pattern actually matches case-insensitively). `gates.py`'s FRE_FLOOR
   comment, which only cites the North Star ruling by name and number (no date, no "Mark," no
   Decision-Log pointer), was confirmed a real KEEP and left as-is.
4. **Pattern precision and recall**, `tools/check_live_commentary.py`'s `six-test-vocabulary`
   made case-sensitive on the test name itself (Title-case or ALL-CAPS, the two real forms found
   live; a bare case-insensitive match had fired on "Formation tests the soul" - "tests" as an
   ordinary plural verb - and on an unrelated, lowercase "the interaction test") and narrowed to
   label-position anchors only (an immediate colon, a singular "test" noun, PASS/FAIL, a grading
   adverb immediately before the name, a relational "is with", or the battery-completion
   phrases); `build-history-language`'s "an earlier version/draft/assessment" narrowed to require
   self-reference ("of this/the record/field/...") so it no longer fires on legitimate
   textual-tradition prose about a historical text's own earlier version. Recall added, each with
   a real fleet example and a test: "Six of six"/"all six tests" (battery-completion phrasing
   without a name attached), a grading adjective directly before a test name with no "on"/"for"
   between them, a test name followed by "is with" (a cross-reference relation), "Explanatory"
   used bare without "Power", a parenthetical `(gravity N)` cross-reference
   (`gravity-classification-label`), and a world's own "Strand A"/"Strand A-B" source-pool label
   (`matrix-cell-code`).
5. **Fixture wording** - three of the six fixture records shortened in the first pass had lost
   real content the reviewer flagged, restored while keeping every field under the FK/FRE
   ceiling: `fix.force.social-cost-pressure.md`'s description keeps "an ongoing force, not a
   start or an end" (the original's parenthetical, not the flattened "did not start or end
   anything"); `fix.story.the-long-road.md`'s `tellable_as` keeps the causal "after" and the word
   "standing"; `fix.gravity.witness-under-pressure.md`'s description keeps "organizes its
   identity" rather than the flattened "knows itself". `fix.craft.vera-voice.md`'s own added
   process sentence ("stays under `gate_readability`'s FK/FRE ceiling, the same as...") was
   dropped outright - it was itself exactly the kind of process narration this whole effort exists
   to keep out of a live record's body.
6. **Desert waiver recount.** PR #547 (gravity/force description re-voicing) and PR #560 (a
   post-merge scope-fix on top of #547) both merged onto `main` while this PR was in flight. The
   desert count is measured fresh against `main` post-both-merges: 163 (was 172 at the first
   measurement), all in fields #547/#560 never touched (`positions`, `world_core`, `bridge_line`,
   and the remaining `description`/`tellable_as` instances the re-voicing pass didn't reach).

Updated fleet hit counts, current `main`: `check_live_commentary`'s new patterns, 800 across 12
worlds (don 226, lpc 156, witt 127, cappadocian 81, gallic 81, desert 30, pahc 26, alx 25, ijc 19,
hal 17, rzg 6, syr 6) - up from 741 at the first measurement, entirely from the recall additions
finding real, previously-unmatched content, none of it new drift. `gate_readability`: 2,154
across the 11 real worlds (unchanged - the `facilitator-spoken` role and the fleet walk added no
world-level findings, since neither role change touches any field a world's own records declare)
plus 9 fleet-level findings under the new `FLEET_PSEUDO_WORLD` waiver - 2,163 total. Full test
suite, `engine.m1.selftest`, `engine.m9.cli check`, `engine.m2.cli`/`site_cli staleness-check`,
and `check_paths.py` all re-verified clean before pushing the correction.

**PR #545 (witt re-voicing) merged onto `main` while this correction was still open**, alongside
#559/#568 (unrelated). Merged into this branch (a merge commit, not a rebase, per the drive-to-
green rules for CI red on a branch already pushed) and both counts recounted fresh against the
merged state: `check_live_commentary`'s new patterns, witt 127 -> 28 (701 total across 12 worlds);
`gate_readability`, witt 235 -> 194 (2,113 world-level + 9 fleet-level = 2,122 total). Both waiver
entries updated to match. Every world's package rebuilt and repinned again against the merged
state; `engine.m2.cli staleness-check`/`restore`, `engine.m2.site_cli staleness-check`, and
`engine.m9.cli check` all re-verified clean before pushing.

A hard-coded test also broke and was fixed in the same push:
`engine/api/tests/test_wiring.py` asserted `fix.figure.the-elder.md`'s own `bridge_line` text
verbatim; the fixture-restoration pass above changed that field's wording (for FK/FRE, "who came
after" -> "who came later"). The test's own substance (figures-used tracking flows through a turn
and does not re-fire on the next message) is unaffected; only the literal expected string needed
updating to match the fixture's current wording. Confirmed no other hardcoded reference to any of
the six edited fixture fields exists elsewhere in the repo (grepped every `.py` file for each
field's prior wording).

---

**Entry 14 — PR #561 round 3 (head `e8dcc5a1`) independent re-review, three small items.** The
Opus re-review confirmed every round-1 item fixed clean: the new `check_live_commentary` patterns
(701 hits, spot-checked across 5 worlds, no false positives), `gate_readability`'s registry-driven
field coverage, and every `ACCEPTED_OPEN` waiver correct - `engine.m9.cli check` clean, merge tree
clean, tests passing. Three items left, all fixed in the same push (head `b7c551d6`):

1. **The FK-8 band floor was documented as "reported, not failed" but nothing reported it.**
   `gates.py`'s own comment on `FRE_FLOOR` had said so since round 1, with no code behind the
   claim. Added `gate_readability_floor(records, fleet, registry)` and its fleet-scoped twin
   `gate_readability_floor_fleet(fleet)`: the identical spoken-field set `gate_readability` grades
   (via the same `_readability_checks` registry lookup), checked against `FK_FLOOR = 8` instead of
   `FK_CEILING`/`FRE_FLOOR`. Neither function is registered in `GATES` - `engine.m2.validation`'s
   `build_gates_report` (and therefore every world's committed `validation/gates-report.json` and
   package pin) is untouched by this addition, no rebuild needed. `engine/m9/enforce.py` collects
   both under a `"m1:readability-floor"` key (per-world in `collect_findings`'s own loop, plus the
   fleet's own key alongside `"m1:readability-fleet"`), `hygiene_problems()` permanently skips that
   key (unlike the R-4 voicing-pair carve-out, which is conditional and ends itself once
   corpus-map lands a real pair, this one never ends - a sub-8 field is never a defect), and
   `report_only()` now surfaces every `m1:readability-floor` finding fleet-wide rather than only
   the R-4 case it used to be scoped to. Full-fleet run: 1,135 report-only observations, `engine.m9.cli
   check` still exits clean. New tests: `engine/m1/tests/test_gate_readability.py` (a sub-8 field
   is reported while `gate_readability` itself stays clean on the same record) and
   `engine/m9/tests/test_enforce.py` (`hygiene_problems` never blocks on it, `report_only` surfaces
   it).
2. **Two build-vocabulary leaks this PR itself introduced.** `gates.py`'s own `FRE_FLOOR` comment
   and `fk.py`'s `fre_score` docstring each quoted the North Star decision's own section heading,
   "RULED - hard edge," verbatim - tripping `check_live_commentary`'s generic `ruled` pattern
   (`\bRULED\b`) on the `engine` surface, the same pattern class Entry 9-11 above already spent
   several rounds clearing out of this codebase's other comments. `_readability_checks`'s own
   docstring separately cited this project's own history ("`story.tellable_as` and `voice_craft.*`
   going ungraded for a real stretch of this project's life") rather than stating what the function
   does. All three reworded to describe the code's own behavior and design reasoning directly, no
   quoted ruling language, no project-history narration. Confirmed via `check_live_commentary
   --surface engine`, diffed against `origin/main`'s own copies of both files: zero new hits on
   either touched file (the two REWRITE hits this round's diff removes were not present on `main`
   before this PR existed - genuinely new, not pre-existing debt this PR happened to touch).
3. **PR body numbers.** Already corrected to the current, accurate figures (head `e8dcc5a1`, witt
   194, 2,122 total, 701 hits) in a body update that landed before this review's findings were
   relayed back - the review's own citation of stale numbers (`ea90c7e8`, witt 235, 2,154/2,163,
   800) reflects the body's state at whatever moment the review actually ran, not its current
   content. The body update accompanying this entry only advances the head SHA to `b7c551d6` and
   adds this round's own section.

Full local suite (829 passed), `engine.m1.selftest` (`overall_pass: true`), `engine.m9.cli check`
(clean - 0 blocking problems, 1,135 report-only observations), and `check_paths.py` (0 new
unresolved) all re-verified before pushing.
