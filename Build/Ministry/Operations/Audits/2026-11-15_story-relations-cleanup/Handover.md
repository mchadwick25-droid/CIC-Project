# Handover: story "How it connects" rewrite, new voice (2026-11-15)

The previous worker (session_01JMNsS9pAu8gHF18tfNX1Fs) stopped at a clean break when its context passed 400k. Nothing in the new voice has been written to the repository. Coordinator: session_01JMNsSAmN1HUCBWPQWS4gro.

## State

- Branch `claude/cft-story-relations-cleanup`, PR #1679, open, not merged. Mark ordered it held (2026-11-15). Head `bdbd62e2` plus this handover commit.
- On the branch: the first rewrite of all 62 lines (three review rounds plus two cap-ruling checks, all in this folder), the validator check `checkStoryText` in `tools/validate-census.mjs` and its test `tools/tests/validate_census_story_text.test.mjs` (wired into CI), the Scillitan story-text fix, census release 45, the data page, the Decision-Log entries and the Open-Gaps entry (numbered 280 on the branch).
- Mark then read the 62 lines and ruled them "too factual, no color". The new voice below replaces them.

## Converged with Mark (2026-11-15, "converged, auto mode"), his words in quotes

Worked through divergent, groan and convergent phases in this session.
- "these read too factual, no color". Story-style rewrites (a scene carrying the link) were rejected: "these are not story peices they are technical inforamtion".
- Voice: option 1, "yes 1". Each line gives the connection, then says what the connection shows (why it matters). Not narrative, not scene-setting.
- Sample first: "sample first". Eight samples were approved: "much better". They are in `Voice_Samples_Approved.json` (id, line, support). Note that those samples run 2-4 sentences; the length rule below came after them.
- Length: "yes, two sentences", then "two sentences, no exceptions". Every line is exactly two sentences, about 35-45 words. An honest limit or correction is folded into the two sentences, never a third. Cut the scaffolding: don't restate the card's "Nearby on the map" list, and don't put setup clauses before the point.
- "How it connects" is one small section of a story card (10-15 seconds to read). It is not a Who brief; the 2-minute target does not apply.
- Fidelity: every claim, including each "what it shows" sentence, must be supported by the card's own text, teaser, caveat or sources, or by the census. Hedges stay ("reportedly"). Nothing invented. CLAUDE.md reading target; no AI tells.
- Review: "yes, fresh cycle". A fresh review cycle with its own three-round cap, as a change order. Log it in the Decision-Log as a "Cap ruling" entry naming the review files, so the roundcount gate counts only the new files.
- Drafter: "opus drafts". Opus drafts all 62 (a fresh Opus session is fine; Sonnet does not draft this).

## Plan (auto mode)

1. Draft all 62 lines in the new voice. For each story, read its card (`DATA.stories` in `cft-website/index.html`) and the census movements it links or names. Use the approved samples as the voice, cut to two sentences (the two-sentence cuts of Lay, Abitinae, Nickel Mines and As'ad, below, were shown to Mark).
2. Self-check: the validator (`node tools/validate-census.mjs --skip-quotes --atlas cft-website/index.html cic-website/data/world-census.json`), an exact count of two sentences per line, and readability (`engine.m7.turn_readability.score_turn`).
3. Review: fresh Opus agents at full effort, every line checked against card and census. Files go in a new subfolder, e.g. `voice2/` here (V2_R1_review.md, V2_R1_changes.md, rechecks). Three rounds at most; a blocking point open after round 3 goes to Mark. Mark's standing cap ruling of 2026-11-14 covers minor round 3 fixes to reader text (apply as worded, then one targeted check).
4. Put the final 62 on an Artifact page for Mark to read before merging.
5. Merge origin/main. PR #1680 takes Open-Gaps 280, so renumber this entry to the next free number and fix every reference (the Decision-Log cites it). Remove the waiver "relations-summary-release-45" that #1680 adds, or the stale-waiver check fails. Update the Decision-Log entries for the new voice and the cap ruling, the PR body, and rerun every check #1669 ran. Send the coordinator one line before merging and wait for the go. After the merge, check that www.churchfamilytree.com serves release 45 and a cleaned card.

## Two-sentence cuts shown to Mark

- Lay: "Lay is where Quaker opposition to slavery starts, as one man's protest. A generation later John Woolman made it the Quakers' own position, and Woolman owned and read Lay's book."
- Abitinae: "Donatism's story begins here. The Abitinians reportedly refused communion with a bishop who had handed over the Scriptures, and that refusal grew into the Donatist conviction that a sacrament is only as valid as the purity of the one who gives it."
- Nickel Mines: "The Amish are a branch of the Anabaptist family, and their response shows how deep its teaching runs. Scholars trace it to the Lord's Prayer said every day and to a memory of martyrdom reaching back to the Radical Reformation."
- As'ad: "The American missionaries in Beirut called As'ad their first convert and first martyr, so the Arab Evangelical churches begin with him. The Maronite church, which held him at Qannubin until he died, remembered the same events as discipline, not martyrdom."

## Carry forward from the first rewrite

- Known traps: Abercius's 'the same faith' cannot be quoted (no held text); Anatolia is not Pliny's province; four home traditions exist in the census (Hungary Protestants, Catholics of Ceylon, Arab Evangelicals, Maronites 1815-1906); the Amish split is within the Anabaptist family; Olympias was an ordained deaconess; Abitinae's break is "reportedly"; "towns of Lombardy" on great-alleluia-1233 has no support (the card says "cities of northern Italy").
- Old-line claims: Mark kept the old-line convention for release 45, and the 84 claims are listed in `Old_Line_Claims.md`. The new voice requires card-or-census support for every claim, so the redraft should not carry those forward unsupported; update the Open-Gaps entry to match what the new lines keep.
- Process slip to avoid: unquoted shell heredocs ate backticked text three times in this job. Write briefs and logs with quoted heredocs (`<<'EOF'`) or from files.
