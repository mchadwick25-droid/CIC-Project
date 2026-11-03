# Spec 4: the diversity rule for the offered passages

**Model: Opus.** It changes the order of what the voice speaks from.

**Purpose.** When several passages bear on a sub-question, order them by rank but keep them different from one another, so no more than a set share comes from one author or one work. No gate, no pass.

**Proposal (for Mark to confirm).** Cap: no more than 3 of the 6 passages from one author, and no more than 2 from one work. Reason: with 6 slots, half from one voice still lets a strong author lead while leaving room for a second view; two from one work stops one book filling the offer. Floor: the cap relaxes when fewer distinct authors (or works) hold passages in the lens for the sub-question than the cap needs, so a world with one author on the topic is offered up to the budget from that author instead of starved. A reviewed seed still outranks a searched passage of equal score. Budget stays 6 passages and 1,800 words. Where passages disagree, the contested-claim records already carry the label; nothing is added.

**Inputs.** The ranked candidate list from Spec 2 with author and work for each. **Outputs.** The same list reordered and cut by the cap, within the budget.

**Where it sits.** Inside `offer_contents`, after ranking and before the budget cut. It is one function (`diversify`) in `engine/m4/passage_offer.py`.

**May touch.** `engine/m4/passage_offer.py` and tests. **Must not touch.** Search ranking, the directive, records, the contested-claim records.

**Test written first.** (1) Eight ranked passages, six from author X: the offer holds at most 3 from X and keeps rank order among the rest. (2) Only one author in the lens: the offer holds up to 6 from that author. (3) A seed and a searched passage at equal score, same author: the seed stays first. (4) The 1,800-word budget still applies. (5) Passages with no named author or work are dropped before the cap.

**Measures (held-out set, Spec 5), in two kinds. Counts with the case total.**
- *Code only, free, no drafted answer:* the share of questions where the offered set holds more than one author or more than one work; the largest share of the offer taken by one author, before and after the rule; how many passages the cap moved or removed; how many questions hit the floor (too few authors in the lens).
- *Needs a drafted answer:* whether the draft binds sentences to more than one passage. This runs with in-plan helpers that write the drafts, which costs nothing, and is labelled helper-written. A live test is proposed to Mark only afterwards, with a name and a cap, as already ruled.

**Done when.** Tests pass, the code-only counts are reported for every held-out question, and the helper-written count is reported labelled as such. **Cost:** none. A live test is a separate step for Mark's named approval and a cap.
