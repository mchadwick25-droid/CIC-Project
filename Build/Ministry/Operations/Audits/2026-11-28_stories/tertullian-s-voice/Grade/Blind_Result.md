# Blind comparison: Tertullian (final brief, commit 564562a8)

Judge prompt: `Build/Ministry/Operations/Audits/2026-11-28_era1-blind-check/x3/pairs/p01/prompt.txt` on `claude/cft-blind-check-14`, word for word, only the paths changed (`blind_pairs_inputs/pairs/p0N/prompt.txt`). One fresh Opus judge per pair; X and Y drawn at random (`blind_pairs_inputs/key.txt`).

| Pair | Reference | Tertullian was | Verdict | Tertullian | Reference |
|---|---|---|---|---|---|
| p01 | Basil of Caesarea | Y | Tertullian better, "by a fair margin but not a wide one" | B | C+ |
| p02 | Epiphanius of Salamis | X | reference somewhat better | C+ | B |
| p03 | John Chrysostom | X | reference somewhat better | B− | B+ |

Pass rule: 2 of 3 at B− or better and none "clearly worse". Result: **passes** (B, B−; no judge said clearly worse).

Faults the judges found in the Tertullian brief (each to be fixed before release or ruled by Mark):
1. "There he answered them": unclear which book (p01, p02, p03).
2. Augustine on second marriage told twice, paragraph 5 and "For that teaching on marriage" (p01, p03).
3. The turn told twice: the essence's "later in life he joined" and "Then he came to believe the New Prophecy" (p02).
4. The opening revisited: "That letter was his Apology" (p02, p03).
5. "about the year 197" and "around the year 200" both given (p01, p03).
6. "the foremost early writer of the faith in Latin" read as the narrator's praise (all three). This is Mark's approved essence (2026-11-20).
7. Ends on a later writer, Augustine; "still being read" heard as a summing-up (all three).
8. The Cyprian chain is clumsy (p01); the essence's run-on list (p02).
