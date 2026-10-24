# Handoff — Library pass, Era VIII (1650–1815) — 2026-10-23

From session: https://claude.ai/code/session_01BUceehKZ2ebKsTF1J1LXc7 · World or workstream: Library thread, Era VIII (census worlds VII.1–VII.29) · Branch / PR: `library/era-viii-2026-10`, https://github.com/mchadwick25-droid/CIC-Project/pull/1085

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Source Readiness Dossier for each of the 29 Era VIII worlds, at `Build/worlds/_cross-world/dossiers/<census-id>_Source_Readiness_Dossier.md` (the Methodist and Old Believer dossiers refreshed as library-completion passes) | 29 files present; each has sections 1–6 filled; `tools/check_live_commentary.py --base origin/main --enforce` exit 0 |
| 376 public-domain texts vendored into `cic/texts/` (1,173 in all), each with an INTAKE header, a `REGISTRY.yaml` entry carrying the reader trailer (sections, credit line, republication), a seed row in `download-queue-seed.yaml`, and corpus-map staging and bucket rows | Every entry re-verified against live host metadata by the intake dry run before download (rights, access flag, date, identity from the body); `cic/engine/texts_registry.py` OK; `corpus_map_merge.py --check` and `corpus_map.py` valid; `works_registry.py --check`, `author_ids.py --check` OK |
| Generated indexes regenerated after the merge of `origin/main` (36 commits, including the Era VII PR and Mark's Era VII rulings): `README.md`, `AUTHORS.md`, `STRUCTURE.md`, `DOWNLOAD-QUEUE.md`, `corpus-coverage.json`, buckets; full-text index rebuilt (1,211 files, 279,362 passages; gitignored) | Regeneration chain exit 0; `tools/check_paths.py` 0 new unresolved citations |
| Closure records for the two worlds with an existing Doc_02: `Build/worlds/meth/Open_Gaps_Tracking.md` entry 36, `Build/worlds/obel/Open_Gaps_Tracking.md` entry 26 | Entries present and numbered; Doc_02 of neither world edited |
| Decision log entry "Era VIII library pass" in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`: scope widening (Mark, 16 October 2026), one registry trailer format, corpus size, slugs, placements left to Mark | Entry present; the corpus-size line corrected to the plan's real trigger (4 GB) in the merge commit |
| The 140 early registry entries rewritten to the Era VII trailer form before merge, so the registry carries one format | Parsed `REGISTRY.yaml` and checked every one of the 376 entries added on this branch: 0 lack the `READER: sections` trailer; no merged entry touched (the diff against `origin/main` adds entries only) |
| PR #1085 opened as a draft after local checks, then marked ready; not merged | Live-surface commentary, cited paths, world gates, M9 confinement, staleness sweeps, needs-ruling tests and the Cloudflare build green on head `51749a37`; "Library validators" was still running when this handoff was written |

## 2. Not done

- Leads that were found but not vendored, with the reason, sit in each dossier's section 3. The main causes: garbled OCR (many Greek, Slavonic and Armenian scans), rights not settled (1931–63 printings, modern uploads with no edition statement), lending-only items, and two size trims (Likowski vol. I for VII.28; Arnauld's *Fréquente communion* for VII.9).
- Kongo Antonians (VII.11): sources vendored, but no public-domain text of the movement's own voice exists. Recommended atlas only.
- Melkites (VII.23) and Utrecht (VII.25) are thin; a Dutch source pass would change the Utrecht answer.
- Doc_02 for `meth` and `obel` still states gaps that are now closed by vendored files; revising it is for those worlds' own threads.
- The two Wesley slug conventions in the Methodist bucket (`wesley-john`/`wesley-charles` and `wesley-j`/`wesley-c`) are flagged, not reconciled.

## 3. Re-check before you trust it

- "Quotes verified" is never claimed by this pass: no text was quoted into a record. Any build thread that quotes from these files re-verifies against the vendored file, per the working rules.
- Title-page years where the host date differed: each is explained in the registry notes (`date_mismatch_explained` in the specs). Spot-check a few against the file body, as `Dobrotolyubie1793` (Philokalia vol. 2) and Humphreys's SPG history (host "1718", known 1728).
- OCR measures in the dossiers (share of non-blank lines with four or more words of three or more letters) were computed once per file. Files near the 0.6 line deserve a second look before quotation.
- Corpus size: 1.34 GB of texts, about 1.5 GB tracked in `cic/texts/`. `PLAN-texts-store-scaling.md` re-opens at 4 GB. The Era VII decision-log entries say 1.5 GB is the action point; the plan says 4 GB. Not this thread's content; flagged, not edited.
- The Cavazzi and Lopes cross-link rows (and nine Era VII rows merged from `main`) point at the old combined VI.13 id `mission-born-christianities-kirishitan-japan-kon`; they validate only because the census still carries that id beside the four split ids.

## 4. Waiting on Mark

- Build / atlas only / part of another world per world — the table in PR #1085 and each dossier's section 6. Open calls: Kongo (atlas only), Melkites (open question), Utrecht (thin build or hold).
- Remap of the eleven VI.13 rows to `kongo-christianity-afonso-to-1650` and the Philippine ids (Era VII ruling 2) — named in the PR body, item 2.
- One pass over this era's `transmission` and post-window `context` rows against the ruling 6 placement principle (35 of this pass's staging files carry a `transmission` row) — PR body, item 3.
- The cross-world placements staged `provisional`: Whitefield (VII.5, VII.6, VII.10); the middle and southern colonies and VII.6; the AME edge of VII.5; the Czech succession claim of VII.4; missions with no census home (Danish West Indies, Greenland, Tranquebar) — each dossier's section 5.
- Whether to merge PR #1085 once "Library validators" is green; the launch brief said not to merge from this thread.

## 5. Next step

Mark reads PR #1085 and rules on the table; if "Library validators" goes red before then, this session (still subscribed to the PR) fixes it on the branch. No new Library batch starts until Mark restarts Library work.

## 6. Spend

Allowance share used: not measured from inside the session; read it from `/usage`. Metered: none (no model API call was made by this thread; decisions 54 and 56).
