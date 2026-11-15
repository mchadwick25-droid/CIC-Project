# Round 2: targeted recheck of the "How it connects" lines

You are a fresh, independent reviewer. This is round 2 of a capped review cycle (three rounds at most). Do a targeted recheck: check that each round 1 finding was fixed without new error, and check every changed line's fidelity afresh. Do not re-review unchanged PASS lines from scratch.

Read first: scratch/BRIEF.md (rules), the rulings in scratch/REVISE_BRIEF.md (they apply), and the round 1 review file(s) for your stories in scratch/rev/R1_<batch>.md (A = 01-16, B = 17-32, C = 33-47, D = 48-62).

For each story in your range: the revised line and its notes are in scratch/draft2/NN_<id>.json; the round 1 line is scratch/draft/NN_<id>.json; card and linked census in scratch/pk/NN_<id>.json; other census at scratch/mov/<id>.json.
Check:
1. Each round 1 finding: fixed, or declined with a sound reason?
2. Fidelity of the revised line (blocking): every claim said by the card or census, verbatim support present, hedges kept, no new overstatement, causation or descent the source doesn't state. A fix is new text and needs the same check.
3. Form (blocking): two sentences; first gives the connection, second what it shows; no data or builder talk (this includes "their regions", "tied only by time" read as site talk: judge whether a reader hears the story or the website).
4. Named witnesses: no role standing in for a named witness ("one historian", "a modern scholar", "the translator") where the card names the person; either name them with a few words of who they are, or leave the point out.
5. Craft, judged across the whole set as a reader would read many cards: the coordinator notes that many second sentences hinge on "so" with a payoff clause. Name any lines where the cadence is formulaic or the payoff is a tag line, and suggest a plainer join. Minor unless clearly bad.
Coordinator's specific questions: line 08 ("strip Church and Empire of the privileges" reads oddly with a tradition name as object); line 29 ("One historian"); line 60 ("though Burma lies outside their regions"); line 05 ("His epitaph says he found the same faith everywhere", given no held text of the epitaph: is the claim supported by the card, and is it properly attributed).

Output: scratch/rev/R2_<your batch letters>.md. Per story: `### NN id`, verdict CLEAR / MINOR / BLOCKING, numbered findings with the exact words, why, and a full replacement line with support quotes where you can. End with counts and a short pattern summary. Read, Write, Glob, Grep only. Touch nothing else. Reply with counts and the blocking ids.
