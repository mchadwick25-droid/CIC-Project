# Step 0 — Eras 8 and 9 global sweep (P2-G89) · Review Round 3

**Record:** `CiC_Step0_Eras8-9_GlobalSweep_V1_0.md` (same folder), "Revision log (after Round 2)".
**Scope:** targeted recheck of the Round 2 fixes (`git diff 2626f195`) and of any errors they introduced. Nothing else. Round 3 of 3 under the cap.

## 1. Round 2 findings: closure

| Finding | State | Check |
|---|---|---|
| R2-M1 ME-4 and VIII.52 | **Closed** | Census: VIII.52 "The Melkite Greek Catholic Church after 1815", 1815-1911; VII.23 (1724-1815) has `continuesAs` the VIII.52 entry. ME-4 is restated as the Orthodox Patriarchate of Antioch, 1815-1906, class hold; §2, §2b, §6 and G89-42 agree. G89-42 gives (a)/(b)/(c) with a reasoned recommendation; (c) is rejected for a stated reason. VIII.52's text does not name Gregory II Yūsuf, as the record says. |
| R2-M2 RV-2 and VII.32/VI.32 | **Closed, departure reasoned** | Census: VII.32 "The Mennonites and the Amish", 1650-1890, countries Netherlands and United States; VI.3 continues as VII.32; VI.32 "The Hutterite Brethren", 1528-1785. Both quoted phrases appear in the census verbatim. RV-2 is now "named line", G89-49 gives three options with (a) recommended. The departure is right: RV-2 was "enter once", so rivers enter stays 3, enter once 2 to 1, named line 2 to 3. |
| R2-C1 | Closed | §1 at release 29, with a line that the passes read release 28. |
| R2-C2 | Closed | VII.31 in RV-7's precedents and Overlap. |
| R2-C3 | Closed | §10 logs VIII.52's 1911 end, noticed and not touched. |
| R2-C4 | Closed | ME-2 Section A and §6's list read "held, not read". |
| R2-C5 | Closed | "[I] would rather die ...", marked supplied. |

## 2. Counts

Recomputed from §2's Class column: enter 22, enter once 2, named line 18, hold 19, out of scope / carried 1; 62 counted, 6 not counted, 68 rows. Per region they match the table (Middle East enter 7, hold 6; Rivers enter 3, enter once 1, named line 3, hold 2). The revision log's closing line agrees.

## 3. New errors from the revision

None found. No new name, date or source is invented; the census facts the fixes rest on are as stated.

## Substantial findings

None.

## Moderate findings

None.

## Cosmetic findings

None.

## Clean checks

- `python3 tools/check_spelling.py` on the record: 4 hits (*Neighbours* twice and *Enquiry*, in book titles; "Saint Saviour", a monastery's name). All are proper names, left as written; 0 in enforced trees.
- `python3 tools/check_paths.py --baseline tools/check_paths_baseline.txt`: 0 new unresolved citations.

## Verdict

**Pass.** Both moderate findings are closed, R2-M2's departure on counts is correct, and the cosmetic fixes hold. No review round remains under the cap, and none is needed.
