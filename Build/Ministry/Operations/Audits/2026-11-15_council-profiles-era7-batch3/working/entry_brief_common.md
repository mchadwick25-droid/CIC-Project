# Drafting brief: entry and records for one era 7 council (batch 3, common to all four)

You are an Opus drafting agent for the Church Family Tree, repo /home/user/CIC-Project (branch claude/cft-councils-era7-batch3). You write TWO things for one council:
1. `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/<id>.entry.json`
2. A records block for that id, written as a standalone JSON file at `/home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch3/working/records_<id>.json` (an object with keys `claims`, `contested_claims`, `absent_details`; the worker merges the councils into era7/records.json).

Do not edit any other repo file. Do NOT edit the brief. No paid calls, no network.

## Read first
- `/home/user/CIC-Project/CLAUDE.md`: "Trust and source fidelity" and "Accessible and rigorous" (especially "No AI tells").
- `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md` (whole): it defines every field.
- The model, copy its form exactly: `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1530.entry.json` and that id's block in `era7/records.json` (batch 1; look at claim/witness/witness_kind/formation_confidence shape, and how `witness` cites "file l.a-b"). Read the batch 1 round reviews' lessons in `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/Handover.md`, "Lessons".
- The brief already written for your council (in era7/): your entry's About This Council is that brief; the entry must agree with it in every fact and must not contradict it.
- The research dossier for your council (path given below). It has file:line for everything. Re-open the source lines yourself (grep -n / sed -n with line ranges; never whole files) for anything you put in the entry, and for every quote. Quotes are verbatim; OCR files often double-space words, use long s as f, and break words with hyphens at line ends.

## Rules the earlier reviews enforced (do not repeat the mistakes)
- Every claim sits with its own witness, named in the text ("Fillastre says", "by Mansi's dating"). When you write a sentence of two clauses, check each clause still has its witness. When you split a sentence, re-check the same.
- A month, day or count that no witness of the time gives is the modern editor's, by name.
- No false absences: write "not among our sources" or "no held source gives X" only where the dossier's searches (or your own) back it, and say so in `absent_details` with the searches.
- "Widely Accepted" only where no held editor disagrees; otherwise Contested with a `contested_claims` entry naming both sides with file:line.
- Contested points are told as contested, both sides by name.
- Census: the entry may differ from the live census only where held sources do; such differences go in the coordinator's Open-Gaps list, not here. List them at the end of your reply.
- Writing: plain, precise, CEFR B2; sentences no longer than 25 words (check by script); no AI tells (no "X, not Y" empty contrasts, no "X and never Y", no "a testament to", no summing-up lines, no hedging filler). American spelling in our own prose; quotes keep theirs.
- `people`: name, verdict (WHO / STORY / LISTED / WANTED / NOT SCORED, from the dossier, which took them from the era 7 Who scan), part played. An `id` only where a census person entry already exists (no era 7 Who profiles exist yet; census persons include hugo-grotius, martin-luther, john-calvin: check the census). Writers who only report the council are in `record` and `sources`, not `people`. People who did not attend but acted in the record (sent envoys, were condemned, refused) may be on the click with their part stated, as era 5 Lyon does for Clement IV and Joseph I.
- `traditions`: census ids that exist at the date (see the dossier §16 and working/era7_census_ids.txt in the batch 3 audit folder); `name` copied exactly from the census (`git show origin/main:cic-website/data/world-census.json`, query with python); part Gathered / Condemned / Refused / Affected; one sourced line each.
- `modernCountries`: country and place ids copied from existing census rows (search the census for the country/place you need; if a place id is not in the census, give only what is there and say so in your reply).
- `rivers` exactly as the councils scan row gives them (in the dossier brief).
- `briefLength`: e.g. "about 2 minutes 30 seconds" (compute from the brief's words at 160 words a minute, rounded to the nearest 15 seconds, the way era 6 did).
- `uncertain` opens with the brief's caveat on the record (whose account we have), then each further doubt naming witnesses.
- `sources`: three groups `fromTheCouncil`, `fromThoseThere`, `writtenLater`, each {title, author, language, file} with file under `cic/texts/` (check each file exists with ls).
- records: every fact in the brief and entry has a claim with witness "file l.a-b", witness_kind (acts / participant / later narrative / modern reconstruction) and formation_confidence (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin). Every contested point has a contested_claim. Every honest limit is an absent_detail with the searches named.

- Read every source sentence whole before you report what it says, including its "although" and "except" clauses; a fix or a paraphrase that overstates a historian was batch 1's worst blocking point. A partisan label ("Jesuit", "Lutheran") needs a held line.
- Keep the entry tight. Each field holds what the sources give; no filler, no repeating the brief at length.

## When done
Validate both JSON files with python -m json.tool, run a sentence-length check (no string sentence over 25 words), and reply with: the two file paths; the count of claims / contested / absent; a list of census differences found (for Open-Gaps); any place where you could not confirm a dossier line (and what you did instead); and any fact in the brief you think is wrong or unsupported (do not edit the brief; just report it with file:line).
