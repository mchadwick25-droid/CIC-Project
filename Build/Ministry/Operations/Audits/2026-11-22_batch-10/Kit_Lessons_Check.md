# Kit lessons, batch 10: independent check of the ten edits

Scope: the ten edits in `git diff -- Build/Ministry/Features/Church-Family-Tree/Brief-Kit/`, each against its section under "Durable gaps" in `Kit_Lessons.md`, read with the sentences on either side, against all of `Kit.md` and every file in `roles/`. Each new text matches its gap's "With" wording verbatim.

Commands and files named, confirmed present: `Build/tools/align_tree_narration.py` (`--only` takes comma-separated entry ids; `--check` prints "no stale paragraph times" or the stale ids and exits 1), `tools/check_open_gaps_numbers.py` (defaults to `Open-Gaps.md`), `tools/check_live_commentary.py` (`--base`, and `--enforce`, which needs `--base`), `tools/validate-census.mjs` (`checkQuotes` scans every quoted span in card prose against the cited files or `tools/quote_renderings.json`), `cic/texts/`.

## Verdict: FIX

Two BLOCKING findings, both on workability: the hand told to do the new thing is not given what it needs.

## Per edit

### 1. Kit, The batch header: no hand is sent anything after its prompt. PASS

Fits the header's "nothing else" rule and step 1's "A change goes back to the researcher before the outline check". No conflict with the reviser or fresh read, which work from files their prompts name.

### 2. reviewer.md step 3: a sentence the outline does not hold is BLOCKING and cut. PASS

Consistent with Kit Part 1 Rigor ("Tell only what the outline holds"), reviewer step 1 (a cut that leaves a named thing unexplained is caught there), and reviser.md step 3 ("using only what the outline holds ... Make the review's cuts"). The Do not say line the reviewer may add guards wording; it does not write story content into the outline, so the two do not clash. Content the story should carry goes back through edit 1's path.

### 3. Kit step 2: the recheck's replacements applied to `Outline.md` word for word before the writer starts. PASS

The hand is covered by Part 4's "Sonnet only to ... apply changes word for word", and "Keeping the kit clean" exempts a fix applied as a checker worded it from a further check. The writer reads only `Outline.md`, so this is the right file.

### 4. card.md census paragraph: quotation marks only around a source's own words. PASS

Matches `checkQuotes`: every double-quoted span in card prose must stand in a cited file or be a listed rendering, which release step 3 lists for the brief's quotations. "There" reads as "in card prose", which is accurate. The old `briefReferences`-only rule is fully replaced, not left beside it.

### 5. card.md: scratch outside the repository, per story, no other hand's script. PASS

### 6. card.md check pass item 1: each "to the card" item is on the card, a modern view credited by name. BLOCKING

The check now asks whether every item the outline, review or fresh read sends to the card is on it, but the check pass's reading list does not include `Outline.md`, `Review.md` or `Fresh_Read.md`. The checker cannot confirm the items without the files that send them. (Separately, `Kit_Lessons.md` gap 6 notes this edit is Mark's call; that is for the coordinator to confirm, not a text finding.)

Old:
> then the brief, the card, `Card_Edits.md`, the starting card if there is one, and the entry if there is one.

New:
> then the brief, `{FOLDER}/Outline.md`, `{FOLDER}/Review.md`, `{FOLDER}/Fresh_Read.md`, the card, `Card_Edits.md`, the starting card if there is one, and the entry if there is one.

### 7. checker.md item 7: each "not held" item searched in `cic/texts/` by its name forms. PASS

Fits the spot-check list grammatically and matches researcher.md's sweep ("a search of `cic/texts/` for every name form"). Supports "Explain it or leave it out" without narrowing it.

### 8. Kit step 0: a pre-kit story first gets a source sheet. BLOCKING

The edit makes a sheet but no outline. Every later step for that story works from `Outline.md`: reviewer step 3 traces every sentence to it, the reviser uses "only what the outline holds", and edit 2 now makes every sentence the outline does not hold BLOCKING and cut. With no outline, the whole pre-kit brief fails and the reviser has nothing to fix from, which is the failure the gap's own evidence names (Ephrem: "No outline"; both stories "later needed an `Outline.md` made from nothing"). Nothing says the sheet is checked before review either.

Old:
> The researcher first makes its source sheet, with the Library sweep, giving what each charge, teaching, book, quarrel or decision it names was about.

New:
> The researcher first makes its source sheet, with the Library sweep, and its outline, giving what each charge, teaching, book, quarrel or decision it names was about, and both pass the outline check before review.

### 9. Kit step 9: paragraph times remade, `--check` clean, changed recordings come off the branch. PASS

Flags exist and behave as the line says. `--only` places only ids whose recording hash matches the current text, so it runs correctly after the release rebuild, which step 9 already follows.

### 10. release.md step 5: `check_live_commentary.py --base origin/main --enforce` and `check_open_gaps_numbers.py`. PASS

Both run as written; `--enforce` has the `--base` it needs.

## Style

All ten: plain short sentences, American spelling, no process history or commentary in kit text.
