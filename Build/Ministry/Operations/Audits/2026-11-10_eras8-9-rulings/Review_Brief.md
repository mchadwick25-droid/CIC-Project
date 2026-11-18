# P2-G89b review brief (adversarial, Opus)

You review drafted census rows, named lines and links for the Church Family Tree. You did not
draft them. Read only; write only your review file, at the path your task names. No metered model
calls. Repo root `/home/user/CIC-Project`.

## What binds the drafts

- `CLAUDE.md` ("Trust and source fidelity", "Accessible and rigorous").
- Mark's ruling (2026-11-10): "take every recommendation" on the P2-G89 gate. Each item's
  recommendation is in the sweep record,
  `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`
  (§8 holds the gate questions G89-1 to G89-55).
- `Drafting_Brief.md` and `Slices.md` in this folder (what each slice was asked to do).

## Review from the sources, not from the drafter's conclusions

For each slice you are given:
1. **Ruling fidelity.** Does each new row, named line, re-route and hold do what its G89
   recommendation says, no more and no less? A frozen row changed beyond what the ruling names is
   a substantial finding. A ruled item missing is substantial.
2. **Fabrication and support.** Every factual sentence rests on an item the record marks V, on a
   Library file, or on a raw public-domain text the drafter opened (listed in `raw/SOURCES.json`).
   Re-open sources yourself: for Library quotes, read the file at the lines; for raw texts, fetch
   the URL with `curl` yourself and search for the quote (a second, independent check of the
   drafter's saved copy). Check at least every quote in `voices`, every link quote, and every date
   and name in `why` and `teaser`. An unsupported or overstated sentence is substantial; an
   invented one is blocking.
3. **Contested claims** tagged and both sides named; nothing disputed stated as settled.
4. **Links.** Type, grade and state fit the evidence (Documented only on a Library primary quote
   checked `verified-direct`; raw online quotes `verified-online`, Widely Accepted at most). Major
   links: lineage and breaks by type; others only with an `outcome` resting on an institutional act
   in the link's own quotes. Two-way check: each relationship the prose names has a link or a
   qualified sentence.
5. **Living.** `living: true` only with R2 to R4 evidence (Living-Era Protocol Addendum V1.0),
   alive today.
6. **Prose.** Run `python3 Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/check_draft.py
   <Draft.json> <raw dir>`. Read for AI tells, generic voice, hedging filler, flattened imagery.
   The bar is acceptable scholarly rigor, not perfection: "could be stronger" with nothing wrong is
   not a finding.

## Output

JSON at the path given: `{"slice", "round", "verdict": "approve" | "revise", "blocking": [...],
"substantial": [...], "minor": [...], "quotes_checked": n, "quotes_failed": [...],
"notes"}`. Each finding: `{"id", "where" (entry/link/field), "problem", "evidence",
"fix"}` (a concrete fix, with replacement text where you can). Approve only with no blocking and
no substantial findings.
