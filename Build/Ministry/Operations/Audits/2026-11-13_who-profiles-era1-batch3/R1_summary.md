# R1 summary: four Who profiles, era 1 batch 3

Reviewer: independent, first sight. No drafts edited. No paid or model-API calls; local scripts only. Full detail in `R1_review.md`.

## Blocking / minor counts

| Profile | Blocking | Minor |
|---|---|---|
| Peter of Alexandria (MAJOR) | 0 | 3 |
| Anatolius of Alexandria and Laodicea | 0 | 2 |
| Polycrates of Ephesus | 0 | 1 |
| Pliny the Younger (outside witness) | 0 | 1 |
| **Total** | **0** | **7** |

## Blocking findings

None.

## Readability and length

Pattern bar: FK at most 10, Flesch at least 60. Length @162 wpm; Peter capped at 2:30 / about 405 words (major), the others within about 2:00. Word count by `wc -w` and by regex token count. Audio = brief for all four (tags removed); `[calmly]` opens, one `[warmly]` before the closing line; no tags in briefs or cards.

| Profile | Words (wc / regex) | Length @162 | FK | Flesch | Within cap |
|---|---|---|---|---|---|
| Peter of Alexandria (MAJOR) | 405 / 405 | 2:30 | 8.2 | 60.2 | yes (at the 2:30 cap) |
| Anatolius of Alexandria and Laodicea | 325 / 325 | 2:00 | 7.7 | 64.1 | yes |
| Polycrates of Ephesus | 320 / 321 | 1:59 | 7.7 | 63.9 | yes |
| Pliny the Younger (outside witness) | 310 / 310 | 1:55 | 8.0 | 61.6 | yes |

## Minor findings, one line each

- Peter M1: "The quarrel with Meletius is told two ways." is a (mild) dispute-announcing opener; the card uses the same phrasing.
- Peter M2: records.json tags Sozomen's "Peter ordained Arius a deacon and cast him out" Inferential-Thin — a doubted one-witness report, not an inference (Contested, or Documented with a note, fits better).
- Peter M3 (borderline): one narrator sentence of 26 words, about 20 of them outside the embedded quote.
- Anatolius M1: one narrator sentence of 29 words (the deacon Eusebius winning the Roman commander's promise).
- Anatolius M2: two men named Eusebius in the siege scene; distinguished by place vs. role, but a listener could momentarily conflate them.
- Polycrates M1: one narrator sentence of 27 words (the Asian fourteenth-day fast).
- Pliny M1 (report-only): the card `label` "Outside witness" sits above `knownFor`, not literally beside `role`; rendering-dependent, as in batches 1 and 2.

All quotations in all four briefs and cards verified verbatim against the vendored files (file + line in `R1_review.md`). Every contested point is given both named sides and left open; honest limits (Peter's family/birth, Anatolius' dates, Polycrates' death, Pliny's birth/death/Tacitus) are present and nothing of the kind is asserted; no invention, no role standing in for a witness.
