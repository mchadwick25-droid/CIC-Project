# V7 controlled test

Mark approved a direction for controlled testing on 2026-11-03. This is not approval of an architecture (Answering-From-Sources Decision-Log 75). The question being tested: can better contextual preparation of the Representative improve the first answer, using the same single generation and no new routine model calls?

The reassessment that led here: https://claude.ai/artifact/EuKJQj3kEgvS2kDLkQvjC9

| File | What it holds |
|---|---|
| [Test_Plan.md](Test_Plan.md) | Arms, the definition of B, the question set, human review, the paid run and its cap, logging |
| [Rubric.md](Rubric.md) | The ten dimensions, the error log, and how the readers work |
| [Specs/](Specs/README.md) | One spec per chunk, in dependency order |

**Worlds:** alx, pahc and syr. Mark chose pahc as the third world.

**Cap:** $30 of metered spend for the whole evaluation, the sample included. If the work cannot finish inside it, it stops and goes back to Mark.

**Not in scope:** arm C (it is built only if B shows a remaining problem that selective correction could address), pre-verified bundles, new routine model calls, any permanent decision on source-library reach, and any change to production. D4 (pull request #1484) stays paused.

**Status:** plan written. No chunk has started.
