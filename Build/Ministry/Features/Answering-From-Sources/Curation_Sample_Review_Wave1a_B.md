# Curation sample review, wave 1a, group B

Reviewer: Opus 5.5, 2026-10-29. Brief: the wave 1a Opus sampling brief. Curations merged on main in PR #1302. I ran `check` and `sample` on all eight files, and all eight pass `check` (exit 0). The review stopped early on Mark's pause, because the weekly allowance was nearly spent. Two files were fully sampled. The other six were not, and their status stays `drafted`.

## Verdicts

| Stem | Verdict | What was checked (lines) | Defects / notes |
|---|---|---|---|
| `optatus_against-the-donatists` | needs-redo | All 135 divisions listed against the file. Every book head (25, 761, 1821, 2987, 3484, 4461, 4836) and every chapter head starts its division with the printed roman numeral and title. Appendix heads I to XVI (5467 to 7366) all match. The notes ranges (315-760, 1325-1820, 2322-2986, 3282-3483, 3881-4460, 4578-4835, 5029-5465, 5795-5928, 6862-7083, 7376-7596) each open with "[Footnotes moved to the end and renumbered]" and hold the notes. Appendix II (5929-6861) has no printed inner head apart from its title "GESTA APUD ZENOPHILUM" on 5930, so the `allow_oversize` sentence holds. All evidence quotes are on their lines. | **Defect:** line 2294 `APPENDIX TO BOOK III.309` is declared `ignore` with kind `running-head`. It is not a running head. It is the editor's printed heading over Book III chapters XIII and XIV. Note 309 (line 2966) explains it: Ziwsa and Du Pin print these two chapters as Book VII.6-7, but they "are evidently an appendix (written later) to Book III". Declaring the heading as furniture takes it out of passage text, which the how-to forbids. Fix: drop the `ignore` entry. The heading should stay as printed text, either as a context-only marker (`division: false`) heading ch13 or inside the division. **Note:** Book II goes from XXIV (1233) to XXVI (1307). No `XXV.` heading is printed in Book II anywhere in the file; the only `XXV.` is Book I's (283). The addresses stay correct, but the yaml should not leave this gap unexplained. The `scheme` line should say that Book II prints no chapter XXV heading. |
| `codex-theodosianus_latinlibrary` | needs-redo | All 3,934 lines starting `CTh` classified. Every law line in the body (`CTh.b.t.l`, `...pr.`, the range `CTh.6.2.1-11` at 1650, `CTh.ct.11.22.1` at 4823) starts a division. The 398 `.0.` lines outside the body are the per-book contents lists, and the 16 contents apparatus ranges (for example 398-432, 805-827, 6866-6878) each open with `IMPERATORI THEODOSIANI CODEX` and list titles only. The body title heads `.0.` (400) start divisions. Evidence quotes are on their lines. | **Defect:** `law-pr` gives the locus `cth{b}.{t}.{l}pr` to the whole law, but each of the 285 pr laws runs on through its numbered paragraphs, which the file prints. Example: `cth6.35.3pr` (2167) holds 6.35.3pr and also `CTh.6.35.3.1`, `.2` and `.3` (2169-2173). A passage from 6.35.3.2 would be cited as "pr", which is a wrong address. Dropping `pr` is not enough: law 16.7.3 is printed twice, once as the Breviary text `CTh.16.7.3 [=brev.16.2.1]` (7311) and once as the full text `CTh.16.7.3pr.` (7314), so the two addresses would collide. Fix: add a paragraph rule on the printed `CTh.b.t.l.n` lines (616 lines), with locus `cth{b}.{t}.{l}.{n}`. Then `pr` names only the principium, and every passage carries its printed paragraph address. **Note:** at 4823 the `(?:ct\.)?` in the pattern absorbs a stray `ct.`. The reading 11.22.1 is backed by the title head 11.22.0 (4822) and by 11.22.2 after it. |
| `acta-martyrum-selecta_gebhardt1902` | not sampled | `check` passes | Paused before review |
| `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902` | not sampled | `check` passes | Paused before review |
| `harnack_vita-cypriani-commentary-lat-deu_1913` | not sampled | `check` passes | Paused before review |
| `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929` | not sampled | `check` passes | Paused before review |
| `perpetua-scillitan-martyrs-lat-grc_robinson1891` | not sampled | `check` passes | Paused before review |
| `possidius_vita-augustini_weiskotten1919` | not sampled | `check` passes | Paused before review |

## Recurring patterns

- A printed heading was declared as furniture (Optatus 2294). Furniture should be checked against the notes before a line is called a running head.
- A locus named a finer level than the division actually covers (CTh `pr`). When the edition prints a finer level, that level should be the division.
- `check` passed both files. Neither defect is something the checker can see.

## Tooling observations

- `CDiv.start` in `resolve()` is 0-based, but YAML and evidence lines are 1-based. A reviewer script reading `resolved.divisions` has to add one.
