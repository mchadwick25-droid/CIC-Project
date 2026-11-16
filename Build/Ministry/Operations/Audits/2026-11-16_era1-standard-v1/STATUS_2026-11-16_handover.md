# Era 1 Standard v1: where things stand (2026-11-16, Opus takeover)

The Fable session stopped at its usage limit at 11:39 UTC without a handover. This note is rebuilt from the branch `claude/cft-era1-standard-v1` at commit 012f04ce.

## Done

- **Drafts.** All 20 Who briefs and the council brief are written, each with a references record in `drafts/`.
- **Renderings.** All 39 quoted spans went through the two-rendering check (`renderings/`). Two keep their joined forms (E15 Ignatius, E34 Pontius) to hold the grade floor; `renderings/README.md` gives the reason.
- **Round 1 review.** Five groups in `reviews/` (Opus). Bardaisan and Dionysius of Alexandria clear. Nineteen briefs are blocked; by the review files' own tables the count is 34 blocking findings (the coordinator's 33 is one fewer, probably a count of Tatian's four as three).
- **Round 1 revision, 4 of 19 done:** Tacitus, Suetonius, Pliny the Younger, Pontius the Deacon. The fixes are in the briefs, and each references record has a "Round 1 revision" section. Pontius B1 was answered with no change, citing the renderings README. That answer is the writer's own, so round 2 has to confirm it independently.

## Left

1. **Round 1 revision, 15 briefs:** Hermas (3), Ignatius (2), Polycrates (1), Josephus (2), Peter of Alexandria (1), Anatolius (2), Eusebius (2), the 251 councils (1), Justin (2), Tatian (4), Clement (1), Marcion (2), Valentinus (3), Hippolytus (1), Novatian (2).
2. **Round 2:** a targeted Opus recheck of the changes only, against the round 1 findings, for all 19. Round 2 is the second of three.
3. **Cards, records, audio scripts and the census for era 1.** Release 48 carries `quotationOriginals` and `briefReferences`. The live errors, the three sample flags and Mark's logged rulings all go in here.
4. **Mark's page:** every brief with its length, and one brief picked at random. That one is recorded only on the coordinator's word, and the rest only after Mark's yes.
5. **One pull request.** The data release and Open-Gaps numbers come from the coordinator.

## Update, 14:30 UTC (Opus session)

Done since the note above:
- Round 1 revision of all 19 blocked briefs; round 2 (`reviews/round2-g1.md` to `-g5.md`); round 3 for Justin, Clement, Hermas and group 5. All 21 clear inside the cap.
- Cards, the council entry and records rewritten for all 21 (live errors listed in Open-Gaps 309). The census was built as data release 50 on main's release 49, with the Bardaisanite card's baptism attributed to Michael the Syrian. Open-Gaps 309 to 312 written.
- Mark's page: https://claude.ai/artifact/LMVXJyiG72yTaAgr9anEEm (random pick: Tatian).
- Mark's two rulings on Tatian are logged in `Decision-Log.md` and are checklist items 19 and 20 of `Who_Profile_Pattern.md`: "To much he said and he rights" (speech tags) and "Just tell the story, not everything has to be a quote or testimony" (one or two quotations a brief).

In progress: the story pass over all 21 briefs (three Opus writers, using the instructions in the session scratchpad; each writes a "Mark's ruling: tell the story" section in its references record and removes dropped quotations from the card's `quotationOriginals`).

Left, in order:
1. One targeted Opus recheck of the story pass (outside the cap, ordered by Mark): claims traced, trust-bearing witnesses kept, one story, length and readability. Write `reviews/story-recheck.md`. Report per brief the quotation and tag counts before and after. Before: 44 quotations; 187 tag verbs by the session's counter (a regex on says/said/writes/wrote/tells/told/reports/adds/records/notes/claims/charges, which also catches plain acts such as "wrote to protest").
2. Rebuild the census: start from `git checkout origin/main -- cic-website/data/world-census.json tools/quote_renderings.json`, then for each era 1 entry set `longDescription` to the brief text, map card.json to the census card (dates to datesNote, place to placeNote; name, tradition and briefLength stay off the census card), map the council entry into `council` and `people` (with an id as {person, part}, otherwise {name, verdict, part}), list in `tools/quote_renderings.json` every brief quotation whose words differ from the printed wording (original = the card's quotationOriginals file and lines, language "English", second_reading = `renderings/comparison.md` and its verdict), set `meta.release` to 50 / 2026-11-16, and apply the Bardaisanite attribution. Then run `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json`, which is slow (over two minutes).
3. Regenerate the audio scripts with `requestTextFor` from `Build/tools/generate_tree_narration.mjs` ([calmly] at the start, [warmly] before the last sentence).
4. Republish Mark's page with the revised Tatian at the top.
5. Wait for Mark's yes through the coordinator. Record Tatian first, with the printed Jon v4 settings and the balance check, only on the coordinator's word; the rest only after Mark's yes. Then one pull request.
