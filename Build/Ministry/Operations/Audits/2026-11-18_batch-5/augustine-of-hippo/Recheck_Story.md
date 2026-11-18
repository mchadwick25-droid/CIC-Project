# Recheck: Augustine of Hippo (batch 5)

Checker: an independent hand who did not write, review or revise this story. Read against `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entry "Batch 5 hearts: church words explained, and Luther's job re-set" (2026-11-18), `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, the brief and `augustine-of-hippo.brief.v1.txt`.

## Verdict: FIX

There is one fix: the essence finishes too late. Everything else passes.

## 1. Review findings

- **B1.** Both of the review's sentences are in the brief, word for word, and so is the paragraph 3 trim. The two books and the Western churches are now in the essence. But the essence is still complete too late (see 3).
- **M1 to M5 and M8 to M10.** Each is fixed as the review gave it. M4 now reads "parable", which matches the letter (outline beat 5). M5 now reads "Near the end of his account", which keeps the new Do not say line.
- **M6.** The reviser did not add it, and that is right. The review marked it optional. The outline's beat 2 also has "another teacher", not "another seller of words".
- **M7.** Noted only, and nothing is owed.

## 2. New wording

The diff against v1 holds only the review's sentences, splits and cuts. Each is held:
- the two books and their glosses: outline essence (line 5) and Words to explain ("City of God")
- the churches carrying the teaching on: outline, What came of it
- "a bishop of Milan sent him questions": beat 4
- the M5 line: Ending 1 and its Do not say line

I checked both quotes word for word against the outline's renderings and against `cic/texts/`:
- Q1 matches AUGL 13463–13465. It follows *uicina*, as the outline sets out.
- Q3 matches RET 9059–9064, and stops before "si autem accepisti".

## 3. Kit lines

- **Hook:** three sentences (words 1–51). Pass.
- **Essence:** not within "about 150". The reviser gives word 180, using the review's two sentences. A plain whitespace count gives word 181, "...both shaped and divided them". That is 31 words over, about 72 seconds at 150 words a minute, which is past the kit's "within the first minute". The review sets its own bar here: it put the Confessions at word 175 and counted that as outside the first minute. So 181 cannot count as "about 150". This is a **FIX**, below.
- **Also told:** every part is present. Leaving the teaching post is left out, as the review allowed.
- **Church words:** every listed word the story uses is given its plain sense where it is first heard. The Confessions gloss in the essence and the "owning up to sin" gloss in paragraph 3 do not repeat each other.
- **Sentences past about 30 words:** none outside the quote sentences (see 4).
- **Length:** the story has nothing it does not need beyond the review's cuts, which are made.
- **Setting:** not stacked in one sentence.
- **Ending:** it ends on the person.

### FIX: bring the essence in by about word 150

Make these four replacements. No gloss and no heart part is dropped. The "sold the skill" clause is moved to paragraph 3, where the outline's beat 1 ("The seller of words", E3) puts it. With all four, the essence is complete at about word 160 by a plain count, about 64 seconds. That is "about 150".

1. Paragraph 2. Replace
   "He taught rhetoric, the art of persuasive public speaking, and in his own words he sold the skill of talking to win."
   with
   "He taught rhetoric, the art of persuasive public speaking."
2. Paragraph 2. Replace
   "And he taught that grace, God's free and unearned gift, comes first: no one turns to God, or even begins to believe, unless God gives it."
   with
   "He taught that grace, God's free and unearned gift, comes first: no one even begins to believe unless God gives it."
   (This says less than the outline, which holds "even the beginning of faith is God's gift", E12.)
3. Paragraph 2. Replace
   "The churches of western Europe carried that teaching on, and it both shaped and divided them."
   with
   "The Western churches carried that teaching on, and it both shaped and divided them."
   (The outline's What came of it reads "the churches of the West".)
4. Paragraph 3. Replace
   "Born in Roman Africa, he taught at Carthage and Rome, then Milan, where he heard its bishop, Ambrose, preach."
   with
   "Born in Roman Africa, he taught at Carthage and Rome, then Milan; in his own words, he sold the skill of talking to win. At Milan he heard its bishop, Ambrose, preach."
   (The new first sentence is 24 words. "There, in 386" still follows straight on.)

Scored with all four in place: 827 words, grade 7.4 (6.7 with names out), reading ease 78.0 with names out. That passes, and the grade under 8 goes to the listener read, as now.

## 4. Score

`python -m engine.m1.profile_readability` on the brief as it stands: 834 words, grade 7.6 (6.8 with names out), reading ease 77.6 with names out, 17.7 words a sentence, longest sentence 41 words. **Pass.**

**The 41-word "sentence": the review and the revision name the wrong sentence.** The scorer splits at every "." "?" and "!". That means Q3 is cut at its own question marks, and its last piece is only 9 words ("What do you have that you did not receive"). It is not joined to "Beside his church...", which begins a new paragraph.

The 41 words are the garden sentence: the lead "Then, he writes:" (3 words) plus Q1 (38 words, the outline's rendering word for word). The scorer splits it only after "read".

**Ruling: it stands.** The words past 30 are the quote itself, and its rendering keeps every clause of one Latin sentence (AUGL 13463–13465). It cannot be split without changing a verbatim quote. The review's earlier "(Not a finding)" ruling on this sentence holds. The longest true narrator sentence is 28 words.
