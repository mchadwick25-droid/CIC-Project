# Spec 3: the A seam, the before-drafting test (shadow only)

**Model: Opus.** It is the rule that decides when search is used at all, and it is measured, not assumed.

**Purpose.** Decide before drafting whether a sub-question has no reviewed record, or only a partial fit, and if so let the offer add searched passages (offer design A, widened). B (a check after drafting) stays a measure only, never a gate.

**Inputs.** The offer's records for the turn; the existing fit step's result (`engine/m4/fit_step.py`) and the reader's verdict on whether the records answer the question; the searched passages from Spec 2.

**Outputs.** In `offer_contents`, a decision recorded in the turn's report: `records_sufficient` or `search_added`, with the reason (no record, partial fit). Shadow only: the flag is off, so the offer the voice sees is unchanged; the report shows what the offer would have held.

**May touch.** `engine/m4/passage_offer.py` (the seam), a report writer under `engine/m4/reports/`, tests.
**Must not touch.** The directive, the answer check, the gates, any record, the fit step's own logic.

**Test written first.** (1) A turn with a fully fitting record: `records_sufficient`, offer unchanged. (2) No record for the sub-question: `search_added`. (3) A record marked partial by the fit step: `search_added`. (4) Flag off: the offer is byte-equal to today's in all three. (5) The report names which of the three held.

**Measures (on the held-out set, Spec 5), in two kinds. Counts with the case total.**
- *Code only, free, no drafted answer:* for each question, whether the decision was `records_sufficient` or `search_added`, and why (no record, partial fit); the share of questions in each; how many searched passages the offer would add; how many of those are voiceable and how many outside the voice. These run from the offer alone.
- *Needs a drafted answer:* the share of drafts that cite an added passage; the share of added passages cited; B (a check after drafting), reported beside A and never used as a gate. These run with in-plan helpers that write the drafts, which costs nothing, and every such figure is labelled helper-written. A live test is proposed to Mark only afterwards, with a name and a cap, as already ruled; nothing here starts one.

**Done when.** The tests pass, the code-only counts are reported for every held-out question, and the helper-written counts are reported labelled as such. **Cost:** none. A live test, if one is ever proposed, is a separate step for Mark's named approval and a cap.
