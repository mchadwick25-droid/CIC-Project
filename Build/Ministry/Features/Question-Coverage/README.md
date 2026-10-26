# Question-Coverage

Anticipate what visitors will ask, find what each world's records and the Library actually hold on it, and close the gap from sources, never by invention. Started 25 October 2026 by the design thread "Questions design: anticipate what people ask and make the worlds ready to answer honestly". Nothing here changes a build, a record, the corpus map or the method. Every output is a proposal or a worklist for the thread that owns the thing it names.

## What is here

| Folder | What it holds |
|---|---|
| `Repository/` | The visitor-side question repository: twelve kinds of visitor, seventeen clusters, 129 sub-questions (the coverage unit), 465 wordings. YAML source plus `render.py`. Each wording is tagged EXISTS (already in the repo), PREDICTED, REAL (pilot or Mark, dated) or RESEARCH (from the Opus review, study named). Ids are append only. |
| `Review/` | The independent Opus review of the repository against Pew, PRRI, Gallup, Barna, Lifeway, Springtide, Theos and peer-reviewed grief work. Sources table with weights, stereotyping risks, 40 sourced additions. Its limits are stated in it: mostly US and Protestant, much of it commissioned. |
| `Coverage-Maps/` | Sixteen cluster reports (`C1` to `C16`, markdown and JSON) and `00-summary-all.md`. For each world and sub-question: RENDERED (a record speaks to it), LOADED (vendored and mapped, no record), IDENTIFIED (registered, not vendored), OTHER (public-domain source outside the repo), NOTHING. Every quote record cited as rendered was re-checked against its vendored file. |
| `Worklists/` | `acquire.*`: works to acquire for the Library thread, scored by cells unlocked. `commentaries-eras-*`: Bible commentaries for all ten eras, led by Origen on Romans. `records-by-world.*`: what each world should add or fix. `chrysostom-mapping-change-list.*`: the corpus-map change Mark approved on 2026-10-26. |
| `Tools/` | `coverage_search.py`, a read-only search of records and vendored texts that classifies each world against a topic. See its README. It makes no model calls. |

## Findings in one place

Read `Coverage-Maps/00-summary-all.md`. In short: the main gap is text the Library already holds and no record carries; the canon forces almost no demonstrations per world; five existing honest limits are contradicted by vendored text; three records are unsafe for a Jewish visitor and the Library holds no Jewish voice; eight of nine "what are you" questions fall through to the Representative.

## Rules this work follows

- No model calls, no live tests, no paid services. Search and verification are by code and reading only.
- Facilitator ground stays the Facilitator's. Questions marked FAC list what a voice can say truthfully after the template-anchored redirect, never an answer to the distress.
- A change to the build method is a governance change and goes to Mark as a change order with the old and new text. None is proposed or applied here. Mark's instruction on 2026-10-26: make no quiet change; the priority is answering from sources, which means widening access to the Library and the accuracy of the context.

## Owners of the next steps

| Item | Owner |
|---|---|
| Corpus-map change for Chrysostom, acquisitions, registry drift | Library thread (see `Library-Thread-Launch-Prompt.md`) |
| Records, limits and fixes in a world | That world's build thread, through the world's `Open_Gaps_Tracking.md` |
| Latin pastoral records and Augustine's commentaries | The LPC thread |
| Method change, if any | Mark, by change order |
