# N. America countries: adversarial review, Round 2

Reviewer: independent Opus 5.5 review · 2026-11-10 · Round 2 (targeted recheck)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_NAmerica_Countries_Proposed.json` at `fc524e253`, against the Round 1 version (`4f7212547`) and `cic-website/data/world-census.json`.

**Scope.** Only what changed since Round 1, checked against the Round 1 findings. Rules as in Round 1 (Atlas Decision-Log, 2026-11-10, option c).

**Method.**
- Diffed the normalized JSON of both versions. Each change was matched to a Round 1 finding.
- Resolved every evidence `field` path in the census and counted each quote with my own script (`chk.py`, scratch dir). Read each new quote in its context.
- Applied the 30 `new` lists with the same script and ran `node tools/validate-census.mjs <applied> --atlas cft-website/index.html`: **322 movements, 578 edges, 10 eras — 0 errors, 2 warnings** (the two existing `shortName` warnings, same as the base file).
- No repo file edited. No metered model call.

## Diff against Round 1

| Finding | Change made | Matches Round 1 |
|---|---|---|
| S-1 IX.15 | US evidence now `documentedStories[1].text` "The Pentecostal Assemblies of the World was led from Indianapolis" | Yes (evidence item); see R2-1 |
| S-2 IX.28 | `documentedStories[0].text` "by which time an American conversation had begun to use the same vocabulary" | Yes |
| S-3 IX.29 | `documentedStories[1].text` "He worked in Dallas, in Northfield, Massachusetts" | Yes |
| M-1 VIII.4 | `teaser` "a movement launched from a New York parlor" | Yes |
| M-1 VIII.16 | `teaser` "New England and outward" | Yes |
| M-1 VIII.17 | `documentedStories[0].text` "The brethren of Ogle County, Illinois" | Yes |
| M-1 VIII.34 US | "The General Conference met in New York on 1 May" | Yes |
| M-1 VIII.36 | `documentedStories[0].text` "In April 1827 Philadelphia Yearly Meeting" | Yes |
| M-1 optional IX.33 | Not taken | Allowed |
| M-2 VIII.34 Canada | "emigrated to Ontario, where Loveless helped found a Methodist chapel" | Yes |
| M-3 IX.15, IX.16 | United States now before Mexico in `new`; evidence items reordered to match | Yes |
| — | `rev1` note added at top level | Allowed |

Nothing else changed. No country was added or removed in any row. The optional IX.15 Mexico quote swap was not taken; the `region` "Mexico" evidence stays valid.

## Quote check

All ten new or changed quotes occur exactly once in their stated field. Each places the row's own story in that country:
- IX.15: the PAW is the Oneness body itself, led from Indianapolis.
- IX.28: the emerging-church conversation, with "American" plainly the United States (the clause before names it).
- IX.29: Scofield's work on the Reference Bible, the row's own text.
- VIII.4, VIII.16, VIII.17, VIII.34, VIII.36: each names the movement's own launch, spread, body or meeting at the US place.
- VIII.34 Canada: Methodism's own chapel in Ontario.

## SUBSTANTIAL findings

None.

## MINOR findings

### R2-1 — IX.15 `doubtful` entry is now stale

- **What.** S-1 asked for the IX.15 `doubtful` entry to be updated or dropped. It still cites "Azusa Street" as the evidence and says "order puts Mexico first". Both are now false of the record. The proposal contradicts itself on this row.
- **Fix.** Drop the IX.15 `doubtful` entry (the order point is resolved by M-3, the evidence by S-1). No other change. This completes S-1 as given; it does not need another review round.

## Verdict

**Approved to proceed**, with R2-1 made in the same commit. The census output is correct and validates with 0 errors. Every Round 1 fix was applied as given, and the only gap is the stale IX.15 note, a one-entry deletion that Round 1 already specified. M-4 (IX.48) still goes to the Atlas Open-Gaps, as `rev1` says.
