# Recheck (story): Cyril of Alexandria

An independent recheck of `cyril-of-alexandria.brief.txt` against `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md` and the old draft `cyril-of-alexandria.brief.v1.txt`. I did not write, review or revise this story.

## Verdict: PASS

## 1. Review findings

- **B1. Fixed.** The brief now says "approved the letter he had written to Nestorius about Mary". That ties back to paragraph 5 ("He wrote of Mary, the holy Virgin:"), which is Q1's second letter. That is the letter Ephesus approved (E6, ACTS 15816–15829: "the Epistle of the most holy Archbishop Cyril to Nestorius"). The listener no longer hears the twelve curses as the approved letter. The Do not say line is in the outline at line 130.
- **B2. Fixed.** It adds one more act, Chalcedon's bishop reading Cyril's name. It comes in time order, credited to "a chronicle", and given by role, not as Timothy Aelurus.
- **M1 to M5. Fixed.** M1: both essence clauses are in. M2 and M4: "In 433 he made peace … Afterward one bishop on his side feared …". M3: "more than two centuries later". M5: "who had come to fight for Cyril", split at "under torture".
- Nothing is listed as unfixable.

## 2. New wording

A word-level diff against v1 shows changes only in the places the revision lists. Each change is held by its source:

- "which had him removed from office in 431": outline essence (E6).
- "that later broke with the council of 451, a meeting of bishops": outline essence ("later refused the Council of Chalcedon"). It uses the Words to explain glosses for council and Chalcedon. Armenia rests on the census text, as I4 says.
- "A monk who had come to fight for Cyril struck the emperor's governor with a stone and died under torture": SOC 19484–19500 (the monks "resolved to fight in behalf of Cyril"; Ammonius's stone struck Orestes). His death under torture is from E2.
- "approved the letter he had written to Nestorius about Mary": E6, Q1, and the outline's new Do not say line.
- "In 433 he made peace with the bishop of Antioch. Afterward one bishop on his side feared …": beat 6 and E8 (HEF 7870–7890, Succensus's fear; CIO 19832–19848).
- "A chronicle tells how even the bishop the emperor set up … put Cyril's name among the church's dead fathers read aloud in worship. He hoped to win the people, but they still would not follow him." ZAC 5720–5746: Salophaciolus returned "by the command of King Zeno". He "exerted himself … to keep the people on his side … wrote in the diptych the names of Cyril and Dioscorus, and read them out … and yet he was unable to draw the people to himself". These sentences say no more than the chronicle, and they credit it.

The quotes are unchanged from v1. I re-checked each one, word for word, in `cic/texts/`:
- Q2: CIO 19876–19882.
- Q1: EP3 954–957, in Greek.
- Q3: SEV1 2105–2108.
- "no commingling, no confusion": CIO 19847.
- "the gold of iniquity": BH.

## 3. The kit lines

- **Hook:** paragraph 1, three sentences around the quote. Within the line.
- **Essence:** complete at "bishops.", the end of paragraph 2, at **word 146**.
- **Also told:**
  - (1) the teaching, Q1, two sons and the bush: present.
  - (2) the riot, the Novatians, the Jews, Ammonius and Hypatia: present.
  - (3) Ephesus, the gifts, and "one nature" after 433: present.
  - (4) the refusal of Chalcedon, Chalcedon's bishop and Severus: present.
- **Church words:** each one the story uses is glossed when it is first heard. Council gets "a meeting of bishops" in paragraph 2. Chalcedon gets "the council of 451". Martyr becomes "one who died for Christ". Diptychs becomes "dead fathers read aloud in worship". The glosses the review listed are unchanged.
- **Sentence length:** the longest sentence is 28 words. None runs past 30.
- **Length (ruling 8):** 719 words by plain count, 710 by the profiler. Every added sentence answers a finding, and nothing the story does not need was added. There is nothing to list.
- **Setting:** it comes in a clause at a time and is not stacked in one sentence.
- **Ending:** on the person, with his death in the Coptic book's voice.

## 4. Score

`python -m engine.m1.profile_readability …/cyril-of-alexandria/cyril-of-alexandria.brief.txt`:
- 710 words
- grade 7.9 (names out 6.9)
- reading ease, names out: 77.0
- 17.8 words a sentence
- longest sentence 28 words
- **pass**

The grade is under 8, so I read it as a listener. It is not flat: the narration is adult, the force is told in full, and nothing talks down.
