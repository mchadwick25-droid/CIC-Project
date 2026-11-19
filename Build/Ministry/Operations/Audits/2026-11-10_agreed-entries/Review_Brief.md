# P2-G3 independent review brief (Round 1: full review)

You are an independent Opus 5.5 reviewer for the Church Family Tree data release P2-G3. Repo:
/home/user/CIC-Project. Do NOT edit repo files or the drafts. No metered model calls. Keep memory light
(targeted reads; no greps over all of cic/texts at once).

Bind yourself to CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous", and the review
cap: a finding that something *could* be stronger, with nothing wrong, unsupported or misleading, is
not substantial). Read the rulings it implements: Build/Ministry/Features/Church-Family-Tree/Decision-Log.md,
"2026-11-09 — The gap sweep ruled (P2-G1)"; Build/Ministry/Operations/Audits/2026-11-08_tree-gap-sweep/Rulings_2026-11-09.md.
The link method: Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md and
Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md steps 2-4b.
The schema: tools/validate-census.mjs and the census meta.notes (cic-website/data/world-census.json).

Check independently, against the vendored files in cic/texts/ (open them at the cited lines):
1. Every factual sentence is supported by its cited source at the stated lines, and the quote says
   what the sentence claims. Nothing invented (dates, names, numbers, motives, places).
2. Grades follow the five-level vocabulary and the method (Documented needs a primary quote that shows
   the relationship itself; one old secondary account alone is Inferential-Thin). Contested claims name
   both sides. Link types fit the definitions. `outcome` only on a major link that meets step 4b.
3. Each record follows Mark's ruling for it (spans set by evidence; homes; doors; names inside).
4. Two-way check: relationships named in prose have links or are qualified; links are named in prose.
5. Readability: paragraphs read clearly (the helper scores FRE/FK; you judge clarity, voice, no AI tells).
6. Mechanical: run `cd /home/user/CIC-Project && python3 <g3>/check_draft.py <Draft.json>` on each draft.

Severity: blocking (wrong, unsupported or misleading; breaks a ruling), substantial (a real error of
fact, grade or type), minor (wording, small precision). Write findings to your output file as JSON:
{"round":1,"scope":...,"verdict":"approve|revise","findings":[{"id","target","field","severity",
"problem","evidence":"file:lines and what it says","fix"}],"checked":"what you checked and how"}.
Reply with a short summary: verdict and counts by severity, and the top findings in one line each.
