# Recheck: Polycrates of Ephesus (story)

Batch 6 independent checker, 2026-11-19. Read against `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `polycrates-of-ephesus.brief.txt` and `polycrates-of-ephesus.brief.v1.txt`.

**Verdict: FIX** (one kit line, brought in by the revision).

## 1. Review findings

All six MINOR findings are handled as the review gave them. MINOR 1 to 5 are made word for word. MINOR 6 needed no change. The review gave no Do not say line, and the outline is unchanged.

## 2. New wording

The diff against v1 touches five places, and each one is the review's own wording. Each is held:
- "the apostles and saints buried there": the essence, "the apostles and martyrs buried in Asia" (Outline l.5), and Words to explain, "great lights" (l.29). "He meant" keeps it as his. "Buried" gives "fallen asleep" its plain sense (l.28).
- "bishop of Ephesus in the Roman province of Asia, in today's Turkey": Words to explain, Asia (l.21), and Setting, Place (l.15).
- "the bishops of the province": the essence (l.5).
- "refusing to share the Lord's Supper": Words to explain, communion (l.27). It also keeps D1 open (l.123).
- "the historian Eusebius": Who tells it (l.101).
- "John … buried at Ephesus" and "other bishops and martyrs": beat 3 (l.51). The sheet's L2 has "He fell asleep at Ephesus", and that line is verbatim at EUS 31335–31336 in `npnf201_eusebius-church-history-life-of-constantine.xml`. I1 gives his "burial place".

The quotes are unchanged from v1 and match the outline's renderings.

## 3. Kit lines

- Hook: the quote's two sentences and the gloss. That is within about three.
- Essence complete at word 135, "…refusing to share the Lord's Supper with its churches."
- Every "also told" part is present.
- Every listed word gets its plain sense when first heard outside the quote.
- No sentence runs past about 30 words. Paragraph 5's 30/31 is the review's allowed one.
- Length is 535 words. Nothing is listed as unneeded.
- The story ends on the person.
- **Setting stacked: fails.** The revised turn sentence now stacks the time, the city, the province and today's country in one sentence: "Near the end of the second century, Polycrates, bishop of Ephesus in the Roman province of Asia, in today's Turkey, wrote this to Victor, bishop of Rome." The kit says "never stacked in one sentence".

## FIX

Move the gloss into the sentence right after the quote, which is also where "Asia" is first heard outside the quote. The turn sentence then goes back to its v1 wording. Replace

"By great lights he meant the apostles and saints buried there. Near the end of the second century, Polycrates, bishop of Ephesus in the Roman province of Asia, in today's Turkey, wrote this to Victor, bishop of Rome."

with

"By great lights he meant the apostles and saints buried there, in the Roman province of Asia, in today's Turkey. Near the end of the second century, Polycrates, bishop of Ephesus, wrote this to Victor, bishop of Rome."

This uses the outline's own gloss (l.21). The total length moves by one word, and the essence still ends at about word 136.

## 4. Score

`python -m engine.m1.profile_readability …/polycrates-of-ephesus.brief.txt`: 535 words, grade 8.6 (names out 7.5), reading ease names out 74.2, 18.4 words a sentence, longest sentence 31 words. **Pass.**
