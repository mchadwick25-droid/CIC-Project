# Brief: eras 8 and 9 global completeness sweep (P2-G89), one region, every river

Repo: /home/user/CIC-Project, branch claude/p2-g89-sweep. Read only. Write ONLY in your own scratch
folder, given in your prompt. Read CLAUDE.md first. Trust is everything: invent no source, date,
name or fact. No metered model API calls.

## Why
Mark ruled on 2026-11-09 that the global completeness sweep covers "eras 8 - 10 for now". Era 10's
sweep is done (data release 25). Eras 8 and 9 lean on Europe and North America:
- Era 8 (1650-1815) has 30 entries. 18 are tagged North Europe, and Africa, Latin America and
  Greater Asia have one each.
- Era 9 (1815-1906) has 51 entries. 45 region tags are North Europe or North America; Africa has 5,
  Greater Asia 7 and Latin America 1.

Find what the roster misses in YOUR region, river by river, 1650-1906. Eras 8 and 9 are frozen, so
anything you propose comes to Mark's gate as a change order.

## Read first
- The roster: `cic-website/data/world-census.json`, movements with era 8 or 9. Read name, lane or
  laneLabel (the "river"), regions, modernCountries, dates, relationsSummary and longDescription.
  Also read era 7 rows (to 1650) and era 10 rows (from 1906) in your region: a story may run across
  without an entry for these years. Do not propose what an existing row already carries; say which
  row carries it.
- **Timeline breaks Mark had logged** (`Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`,
  entries 135 and 142). Each one in your region and period MUST be assessed:
  - Ethiopian church 1650-1855;
  - Coptic church to 1854;
  - Church of the East 1650-1815;
  - St Thomas Christians 1665-1815;
  - Catholic missions in China 1650-1793 with the Chinese Rites controversy. Mark: "check that
    they are unique and not tied to other movements, like jesuites moving around the world, that is
    a single movement". The Society of Jesus row VI.11 ends at 1650, so test whether a Jesuit or
    Propaganda continuation row is the right home.
  - Japan's hidden Christians 1650-1865;
  - Maronites 1517-1900;
  - Georgian church (none after 1245);
  - Melkites 1009-1724 and the Syriac Orthodox church after 1300 (both held for sources);
  - Old Believers after 1815;
  - Latin America, thin for 1492-1900.
- The standard: `Build/reference/L3B-World-Build-Methodology/CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`
  (python-docx is installed). It covers the Section A floor, B1-B5 and the tiers.
- A movement outside church bodies needs the four marks: a beginning, carriers, a name, and
  recognition as a movement in a study. It must be "a defined movement, not just a trend".
- The method in practice: `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_GlobalSweep_V1_0.md`.
  Read §0 and one region section, and copy its shape.

## Rivers to cover in your region
Catholic, Orthodox (Eastern and Oriental), Protestant and Evangelical (including Anglican), Syriac
and other Eastern churches, Eastern Catholic (uniate) churches, and independent, indigenous or
slave-born Christianity where present.

For each river: what existed 1650-1906 in your region that a historian of world Christianity would
expect on a family tree, and is it on the roster?

## Sources
These eras fall before about 1930, so the Library rule applies as in eras 1-9:
- **Primary texts.** Look first in `cic/texts/` and `cic/corpus-map/` (grep, rg). Public-domain
  editions online (archive.org, HathiTrust and the like) count when opened raw and read. Use curl
  for the raw text; WebFetch output is a model's summary and never counts as read.
- **Studies.** Use regional histories, ideally by scholars from or of the region. The repo-cited
  studies come first (grep the repo).
- **Non-English sources.** Use them as other eras did: Ge'ez/Amharic chronicles in translation,
  Arabic, Syriac, Armenian, Georgian, Russian, Chinese, Japanese, Portuguese and Spanish. Use the
  original where it is held or online, with a published translation beside it.
- **Verification states.**
  - V: you opened the item and confirmed the detail.
  - V-s: a study's details only.
  - [S]: snippet, summary or unopened.
  - Only V carries a sentence.
- Nothing after 1906 enters an era 9 history. The living mark means alive today, and needs dated
  evidence graded CD or CR.

## Output (in your scratch folder)
- `candidates.md`: a river-by-river table for your region (river | roster has | gap | candidate).
  Then one section per candidate, giving:
  - kind (church body or cross-church movement) and era (8 or 9; or the span);
  - dates, region, countries and lane;
  - Section A, on a dated statement, or "not yet assessable";
  - B1-B5 and the tier;
  - the four marks, for movements;
  - the evidence list with verification states;
  - living today;
  - overlap with existing rows;
  - a recommendation: enter, named line in <row>, hold for sources, or out of scope;
  - one gate question with options and a recommendation.

  Rank candidates by importance to the eras' global story. Answer each logged break explicitly.
- `candidates.json`: the same, structured.
- `summary.md`: the river table, the ranked list with recommendations, how each logged break was
  answered, and at most 10 notes.

Do NOT draft census copy. Return the summary only.
