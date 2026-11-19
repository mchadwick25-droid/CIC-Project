# Research brief (common to all four councils): era 7 council dossiers (batch 2)

You are a research agent for the Church Family Tree, CIC-Project repo at /home/user/CIC-Project (branch claude/cft-councils-era7-batch2, which equals origin/main). You gather a sourced dossier for ONE major council. A separate drafter will write the profile from your dossier, and a separate reviewer will check every line, so accuracy matters more than anything. Do not write any file in the repo. Write only your dossier file in the scratchpad path you are given. No paid calls, no network.

## Read first (briefly)
- /home/user/CIC-Project/CLAUDE.md, the "Trust and source fidelity" section.
- Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md (the whole thing; it defines the fields your dossier feeds).
- The model profile: Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1530.entry.json and its key in era7/records.json (look at its shape; don't copy its facts). Batch 1's dossier for it, Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/working/dossier_augsburg.md, shows the dossier shape wanted (skim it).

## The rules that the last reviews caught (do not repeat them)
1. FALSE ABSENCES were most blocking findings in eras 5 and 6 (a council's own documents in Mansi missed; an editor's name missed; a held history missed). Never write "no held source gives X" unless you have searched every plausible held file with whitespace-tolerant, OCR-tolerant patterns (Latin, Greek, German, French, Czech, English spellings; OCR often double-spaces letters or names, and breaks words with hyphens at line ends; long-s is often "f": "fessio" for "sessio"). For each absence you report, list the files and the patterns you searched.
2. Keep every claim with its own witness. Say who says it (and in what kind of text). A modern editor's date or count is that editor's, by name.
3. "Widely Accepted" only after looking for a held editor or writer who disagrees. Where held sources disagree, give both with file:line.
4. A source line must be read in context: give enough surrounding lines to be sure what it says (who is speaking, which council, which year). A preface or note by an editor is the editor's, not the author's.
5. Never count an editor's omissions unless you have counted every one.
6. A contested point is told as contested; never settle it.
7. Read the WHOLE source sentence before reporting what it says, including its concessive and exception clauses ("although", "except that", "bien que", "si ce n'est", "quanquam", "se non"). Batch 1's worst blocking point was a historian overstated by a clipped sentence.
8. Names: give a first name or title only where a held line gives it; note which line. A partisan label ("Jesuit", "Protestant", "Catholic historian") needs a held line too.
9. Tell each side from its OWN held sources where they exist; where a side reaches us only through opponents, say so and name them.
10. Quotes must be verbatim. Give the exact text as in the file with file and line numbers, and an English translation marked as yours.

## How to search
- Held sources are in cic/texts/ (filenames are descriptive; `ls cic/texts | grep -i ...`). Use grep -n with line ranges and `sed -n 'a,bp'`; never read whole files (they are huge). Use the Grep tool or grep -n -i -E.
- Search broadly: all of cic/texts for the council's name in its languages (German, Latin, French, Italian, English; old spellings, e.g. Regensburg/Ratisbon/Ratisbona/Ratispona/Reinspurg; Trent/Trento/Tridentum/Trident/Concilium Tridentinum; Augsburg/Augspurg/Augusta Vindelicorum/Auguste/Augusta, Religionsfriede/pax religionis/recès; Poissy/Poissi/Pissiacum/colloque), not just the obvious files.
- File abbreviations: give the full filename once, then you may use a short tag.

## Census check
- The census excerpt (every census entry field and edge that mentions Regensburg/Ratisbon, Trent/Tridentine, 1555 or Poissy) is at Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch2/working/census_era7_batch2_councils.json (large: grep it, don't read it whole); the list of era 7 census traditions (id | dates) is era7_census_ids.txt beside it. The full census is `git show origin/main:cic-website/data/world-census.json` (query it with python; never print it whole).
- For every statement the census makes about this council, say whether the held sources agree, with file:line, or where they differ. Don't change the census.
- List census gaps: parties at the council that have no census tradition entry at the date.

## People
- Era 7 Who scan verdicts: Build/Ministry/Operations/Audits/2026-11-12_who-scan-era7/Who_Scan_Era7.md (grep for names; its "Leads for the councils list" is at about l.358) and Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md. Check Build/Ministry/Features/Church-Family-Tree/Who-Profiles/ on origin/main for any era 7 Who profile (ls; don't edit). Live census person entries in era 7 include martin-luther, john-calvin, ignatius-of-loyola (check ids in the census). Batch 1's entries (era7/*.entry.json, `people`) show how the Who click is filled, including NOT SCORED.
- For each person who took part (called, attended, spoke, was tried, condemned, signed, refused, or was the direct subject of an act), give: name, verdict from the scan (WHO, STORY, LISTED, WANTED) or NOT SCORED, the part played with file:line, and an id only if a census person entry exists. Writers who only report the council are witnesses, not people on the click.

## Dossier shape (write it as Markdown)
1. Held sources: every held file that bears on the council, with what it holds (line ranges), the author, the date of writing where a held line gives it, and the witness kind (acts / participant / later narrative / modern reconstruction) and side.
2. Candidate opening scenes (2-4): a sourced moment in or just before the room, with the verbatim lines and a translation.
3. Issue: what brought them together, each side with its witness.
4. Called by, with witness.
5. Attended: counts (each with its witness; a round number in a history vs a signed list kept apart), names, where from; whether a list of names is held.
6. Dates: opening, key sessions, close, each with witness; modern editors' dates by name.
7. Decided: item by item, from the acts where held (quote the key lines).
8. Outcome: what came of it, through events, with witnesses, including reach beyond one tradition.
9. The condemned or refusing party's own voice, in its own words where held (quote), or say whose hostile account carries it.
10. Short quotable lines (6-12), verbatim, from acts first, then participants, each with file:line and translation.
11. Contested points, each side with file:line.
12. Absences (honest limits), each with the searches run.
13. Close candidates: how later memory held it, from a held source.
14. Census check (statement by statement) and census gaps.
15. People list (as above).
16. Traditions touched (census ids at the date), grouped Gathered / Condemned / Refused / Affected, each with one sourced line.

Also: 17. Length. Say how much the held sources can carry (a 1:30 profile or the full 2:30 ceiling, about 400 words) and why. Never pad: if the record is thin, say so; if no held text can carry a profile at all (no account of what happened in the room), say that plainly and name the wanted text.

Be complete but tight: verbatim quotes short (a line or two), with line numbers. Aim for a dossier the drafter can trust without reopening files, and flag anything you are unsure of as unsure. When done, reply with only: the dossier path, and a 10-line summary of the strongest scene, the biggest contested points and any absence that might make the profile thin.
