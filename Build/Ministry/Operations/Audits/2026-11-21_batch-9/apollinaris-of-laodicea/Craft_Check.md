# Craft check: Apollinaris of Laodicea (`apollinaris-of-laodicea`)

**FIX** (one sentence)

File note: the pass reversed the two files. `apollinaris-of-laodicea.brief.txt` still holds the pre-pass text (it matches the wording `Fresh_Read.md` quotes). The edited text is in `apollinaris-of-laodicea.brief.v2.txt`. This check reads `brief.txt` as before and `.v2` as after. When the edits are applied, the after text belongs in `brief.txt` and the before text in `.v2`.

1. Nothing is added or dropped. All three quotes are word for word. "and the creed of Nicaea" leaves the hook, but the essence still carries it. "One of them" and "There Apollinaris gave his reason" are gone. "To refute it" and the new "So, he held" still carry both points. The holy Fathers gloss is folded into Justinian's lead-in. Lietzmann and Hefele are now given by role, as the outline's Names list directs. **One credit is now unclear (see the fix).** The dissent ("one thought it might be Athanasius's", Pusey) and the watchword ("what one editor calls", Hefele) are both "one" in back-to-back sentences. A listener can hear the watchword as the dissenting editor's.
2. "So, he held, the Word replaced the human mind" stays inside beat 4. The outline gives Quote 1 as his reason for that teaching. Gregory's "without a human mind Christ could not heal ours" goes past the outline's line. It is held, though, by the letter itself (`npnf207` 44689-44691, "a Man without a human mind ... that which He has not assumed He has not healed"). The fresh read cites the same lines. Acceptable.
3. The essence is complete by about word 145. The life is told once, in order. It ends on him.
4. The hook repeat, the stakes and the "Cyril's side" points are all better. The name trim is better on load. Its credit is worse, as point 1 says.
5. 671 words before and 671 after. `python -m engine.m1.profile_readability` passes on `.v2`: grade 8.1, reading ease 77.2, longest sentence 30.

## Fix

Replace:
> Modern editors give it to Apollinaris himself; one thought it might be Athanasius's. If they are right, the man condemned in 381 gave Cyril's followers, unseen, what one editor calls a watchword of orthodoxy.

With:
> Modern editors give it to Apollinaris; one thought it might be Athanasius's. If they are right, the man condemned in 381 gave Cyril's followers, unseen, what one of them calls a watchword of orthodoxy.

"Them" refers to the editors who give it to Apollinaris, and Hefele is one of them. Dropping "himself" pays for the added word, so the count stays at 671.

## Applied (coordinator, 2026-11-22)
The craft pass had written the edited text to `.v2` and left the pre-pass text in `apollinaris-of-laodicea.brief.txt`; the two were swapped, so `.v2` now holds the pre-pass text as the prompt intended, and the fix above was applied word for word to the brief.
