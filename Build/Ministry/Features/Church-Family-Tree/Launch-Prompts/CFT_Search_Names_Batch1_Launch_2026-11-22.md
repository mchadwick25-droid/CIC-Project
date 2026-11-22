# Church Family Tree, search names batch 1 (common, older and outsider names): launch

Paste this as the first message of a new Sonnet session. The review is a separate short Opus session, launched with the last section.

---

Draft the first batch of sourced names for Church Family Tree search. Read `CLAUDE.md`, then the Decision-Log entry "Search: three levels, and the level 1 design converged" (2026-11-22) and the Open-Gaps entry "Search level 1: the sourced common names" (2026-11-22) in `Build/Ministry/Features/Church-Family-Tree/`. No model calls beyond this session and no metered spend.

**What a row is.** One name a visitor might type that the census does not already hold for that entry. Each row: the name; the entry's id, or a country or region the census uses; its kind (other name, older name, spelling, name given by opponents); and its basis. A basis is either a line in the tree's own checked text (entry id, field, the sentence, verbatim) or a source held in `cic/texts/` (file, lines, the words, verbatim). A name with no basis you can quote is left out and listed as wanted. Never invent a name, and never record a name from memory alone. A name its bearers reject is kind "name given by opponents", whatever its fame.

**Scope of batch 1.** Living traditions (the census's `living` field) and the best-known older and outsider names, for entries and for places: for example Nestorian, Quakers, Mormons, Copts, Abyssinia, Persia, Asia Minor, Mesopotamia. Start with what the tree's own text already says (search the census text for each candidate), then the Library. Skip anything code rules already cover (accents, plurals, "St" and "Saint", date forms) and anything already in the census's short, everyday or other names.

**Where it goes.** `cic-website/data/search-names.json`, data only, no commentary. Extend `tools/validate-census.mjs` so a row with no real entry, no kind or no basis fails. Add the file to the data page's list and stamp the next data release number in the census meta and wherever release 52 was stamped (Decision-Log, "Data release 52: a catch-up stamp"). The batch folder is `Build/Ministry/Operations/Audits/<date>_search-names-1/`, with a README, the draft table, the wanted list and the review records.

**Stop for Mark.** Before the review, show the table as an Artifact: each name, its entry, its kind and its basis in one line, with the opponents' names grouped first. Any name whose kind is in doubt is his call.

**Review (a fresh Opus session).** Re-read every basis against its file and lines; a row marked verified is a claim to re-check. Check each kind, above all the opponents' names. Findings are things wrong, unsupported or misleading; "could be fuller" is not one. From round 2, recheck only what changed. Three rounds at most, then escalate to Mark.

**Finish.** Merge your own pull request when CI is green; never promote `main` to `live`. Append dated lines to the Open-Gaps entry and log the batch in the Decision-Log.
