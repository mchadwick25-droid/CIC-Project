# V7 controlled test

Mark approved a direction for controlled testing on 2026-11-03. This is not approval of an architecture (Answering-From-Sources Decision-Log 75). The question being tested: can better contextual preparation of the Representative improve the first answer, using the same single generation and no new routine model calls?

The reassessment that led here: https://claude.ai/artifact/EuKJQj3kEgvS2kDLkQvjC9

| File | What it holds |
|---|---|
| [Test_Plan.md](Test_Plan.md) | A (the saved answers of fleet graded run 1), B and its definition, the questions, human review, the paid run and its cap, logging |
| [Rubric.md](Rubric.md) | The ten dimensions, the error log, and how the readers work |
| [Specs/](Specs/README.md) | One spec per chunk, in dependency order |

**Worlds:** alx, pahc and syr. Mark chose pahc as the third world.

**Cap:** $12 of metered spend for the whole evaluation, the sample included (Mark, 2026-11-03, lowered from $30). Only B is paid. A is the saved fleet graded run 1 answers, which are not re-run. The core run is estimated at $3.53 to $6.30. If the work cannot finish inside the cap, it stops and goes back to Mark. C is not in this cap.

**Not in scope:** arm C (it is built only if B shows a remaining problem that selective correction could address), pre-verified bundles, new routine model calls, any permanent decision on source-library reach, and any change to production. D4 (pull request #1484) stays paused.

**Status:** V1 done (2026-11-03). Arm A is frozen in [Set/](Set/README.md): 84 answers, 28 per world, each byte-equal to the run file. The gate replay reproduces 84 of 84. The repeat draw holds 42 probes, 14 per world. Priced cost from the ledgers: alx $0.6857, pahc $0.6587, syr $0.6554. The run did not save the offered record ids, so Test Plan §3, item 1 cannot be checked against A's run files as written (Set/README.md, "What did not match"). The optional hard-case questions were not written.
