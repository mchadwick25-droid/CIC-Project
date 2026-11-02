# Passage offer smoke test, 2026-11-02 (no tuning)

Six lpc questions whose reader-named sub-question has a seeded passage in Library's Phase 1 seed file (q029, q030, q083, q084, q085, q093; q083's sub-question C5.S2 has no seed, so it is the control). Same reader and safety replies for both conditions (made once). Voice drafts and reads by helper agents, one run each, no ratings. Offer file: `lpc_offer_phase1.json` (index b7511f92). Code: branch engine/passage-offer.

- `off`: offer without passages.
- `on-1`: first offer-on run. Passage ids were `cic:...#01`, which the citation grammar cannot read, so every passage-bound sentence was struck by the net as having no citation tag. Fixed at the source: passages are cited under `lpc.passage.<hash>`.
- `on-2`: offer-on after the id fix. The bound and read steps were first run without the passage records (they load only the world's records), so every passage sentence was struck as unbound: fixed (`--passage-offer` on `test100_bound` and `test100_check`). Its first reads then struck passage sentences because the read's record pack named no author: fixed in `verify_step.record_pack`. The final reads in `on-2/check/read` are after both fixes (`check/read-packnoauthor` is the earlier read).

Counts (after the fixes), 6 questions:
| | off | on-2 |
|---|---|---|
| questions with a passage offered | 0 | 5 |
| questions where a passage was bound | 0 | 4 |
| passage-bound sentences | 0 | 22 |
| of them struck by the read | 0 | 1 (dropped scope) |
| answers-the-question verdict yes/partly/no | 0/4/2 | 0/4/2 (q030 partly to no, q093 no to partly) |

Offered but not used: q085 (1 passage). Before the fixes, 25 passage-bound sentences were struck for the id grammar and the missing records and 17 for the read not being shown the author; none for a reason in the offer line itself.
Gaps found: seeds carry no work title for many passages, so the voice names the author only or "a writing we hold"; in on-1 a source label fell back to a file name.
