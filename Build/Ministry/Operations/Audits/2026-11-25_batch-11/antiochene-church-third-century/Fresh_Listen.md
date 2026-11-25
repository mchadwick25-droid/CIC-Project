# Fresh listen: The Church of Antioch in the Third Century

New first-time listener (no church background, English as a second language), one hearing of the final `antiochene-church-third-century.brief.txt`. Read only the role prompt, Kit Part 1 and the bar, `kinds/tradition.md` and the brief.

**Verdict: PASS.** Nothing BLOCKING. Four MINOR findings, below; each is applied word for word or noted, never the start of another round.

## Counts

| # | What was counted | Count |
|---|---|---|
| 1 | Test lines unfilled | 0 of 4 |
| 2 | Opening gaps after three sentences | 1 (when), not blocking |
| 3 | Sentences that fail on one hearing | 2 (MINOR) |
| 4 | Bare statements | 0 |
| 5 | Citations read aloud that Part 1 does not call for | 0 |
| 6 | Tells Part 1 names | 0 |
| 7 | Unexplained words / short one-act runs / talking down | 2 words, 1 run, 0 talking down (MINOR) |
| 8 | Opening pulls in; drift; listen to end | Yes; drifts at Firmilian; yes |

## 1. The test

- **Who these people were:** filled. "the Christians of Antioch, in Roman Syria, were one church under a bishop, with presbyters, its priests, and deacons, its helpers, bound by letters to churches across the empire."
- **What happened to them:** filled. Their bishop was charged, the bishops met again and again, a debate was taken down, he was cut off, the emperor ruled on the house; later Lucian was killed in a persecution.
- **What their faith was about:** filled. That "the Son of God came down from heaven", against Paul's "Christ was by nature an ordinary man"; psalms sung to Christ; Lucian's "I am a Christian."
- **Why the connection matters:** filled. Arius's bishop "set Lucian in a line from Paul to Arius", Lucian's pupils became bishops, and Arius signs himself "fellow-Lucianist". I can say what passed from this church to Arius's party. (I am not told what Arius's quarrel later grew into; the tree's own Arius page can carry that.)

## 2. The opening

After the first three sentences (the narrator's sentence and the first two of the quote) I know who (Paul of Samosata, bishop of Antioch, and the bishops who judged him), where (Antioch, named) and why there (the charge that he changed the church's psalms). Missing: **when** — it arrives in the next sentence, "In the later third century". Not lost about who or where. Not blocking.

## 3. Sentences that fail on one hearing (MINOR)

- "The emperor Aurelian was petitioned, and he ordered that the house go to the side the bishops of Italy and Rome wrote to." On one hearing I lost who "the side ... wrote to" was. The next sentence ("So those bishops' letters decided it") recovers the thread, so MINOR. Change, noted for the reviser only if a later fix touches the line: none required.
- "... and Eusebius says he alone could catch out a man who hid his mind." "Catch out" and "hid his mind" are idioms; I guessed the meaning (only he could expose a man hiding what he believed). MINOR; no change required.

## 4. Bare statements

0. Each charge, the condemnation ("because, they wrote, he set himself against God and refused to obey"), Arius's expulsion ("because he would not agree"), and the letters of communion are explained. Lucian keeping "out of communion with the bishops for many years" has no reason, but it is told as the bishop gives it, as Part 1 asks.

## 5. Citations read aloud

0 not called for. The single-witness sentence comes once, early, inside a sentence about the letter and Eusebius. Each later "Eusebius says" carries his own judgment of blame or praise ("as against a man ravaging Christ's flock"; "he alone could catch out"), "The bishops also wrote" is an enemy's charge, and "A church historian of the next century, on Arius's side" and "Two generations later, John Chrysostom" mark sources that wrote long after. Arius and his bishop act in the story; they are not citations.

## 6. Tells

0. No "not X but Y", no dash, no question answered by the narrator, no stock word, no moral close. It ends on the community's own name for itself through Arius's words, which is the batch header's planned close on Lucian's circle.

## 7. Words, runs, talking down (MINOR)

- Unexplained words: "magistrate" ("like a magistrate") and "petitioned". I got both from context; no change required.
- Run of short one-act sentences: "That bishop set Lucian in a line from Paul to Arius. Lucian, he wrote, kept out of communion with the bishops for many years. And Arius and his party, he said, were shoots of the same root." Exact change, if applied: "That bishop set Lucian in a line from Paul to Arius: Lucian, he wrote, kept out of communion with the bishops for many years, and Arius and his party were shoots of the same root." (The Chrysostom run, "What is your trade? I am a Christian.", is the quote's own rhythm, not the narrator's; it does not count.)
- Talking down: none. Grade 7.9 does not sound flat; the voice keeps its weight.

## 8. Attention

- **Opening:** pulls me in. A bishop training women to sing to himself at Easter, so that "anyone who heard them would shudder", is a real scene.
- **First drift:** "Firmilian, bishop of Caesarea in Cappadocia, came twice and condemned his new teaching ..." Three new names and places arrive at once for one side figure, and "Caesarea" echoes "Eusebius of Caesarea" from the paragraph before, so I briefly thought they were connected. It recovers on "he died at Tarsus, while the bishops waited for him". For the reviser: noted only; Firmilian acts, so he stays.
- A smaller dip at "Later, in Alexandria, a presbyter named Arius ...": for one sentence it sounds like a new subject, until "That bishop set Lucian in a line from Paul to Arius" ties it back. Noted only.
- **To the end:** yes. Lucian's "I am a Christian" carries me into the last paragraphs.

## The two tools

- `python -m engine.m1.profile_readability`: 675 words, grade 7.9 (names out 7.1), reading ease 74.9, 17.3 words a sentence, 23% short, longest 37 words, pass. Grade under 8 checked: not flat.
- `python tools/check_brief_craft.py`, 7 lines, judged by Part 1:
  - s6, 37 words ("When their own bishop was charged ..."): a chain of events, understood on one hearing. Not a fault.
  - s9, s10, s16 "names a source" (Eusebius): each carries his own judgment; called for (section 5). Not a fault.
  - s28, run of 3 short sentences ("I am a Christian."): inside the Chrysostom quote. Not a fault.
  - s31 "names a source" (Arius said): Arius acts in the story. Not a fault.
  - s36 "modern-scholar word" ("A church historian of the next century"): an ancient historian, credited because he wrote long after and took one side. Not a fault.
