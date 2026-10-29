# Open Gaps — The Latin Apologists

Append-only ledger for this world's build. Entries are numbered and dated; a merged entry's number never changes. Cross-references cite subject and date, not a bare number. The world's file-code is `latap`.

---

## OG-23 — Step 0 quotation findings fixed by change order; one finding stays flagged (2026-10-29)

**Source:** `Build/Ministry/Operations/Audits/latap_Step0_QuoteFixes_ChangeOrder_2026-10-29.md`; handoff check 8 for `latap`.
**Status:** Open until the targeted review is filed. Owner: the coordination thread for the System Hub entry; a different worker for the review.

Handoff check 8 reported 24 quotation findings, all in Step 0. By Mark's ruling of 2026-10-29 they are fixed by the change order named above, with nothing else in Step 0 touched. The order classifies each finding, gives the file and lines checked by hand, and lists 21 exact edits. Two quotations whose origin could not be found anywhere in the tree lose their quotation marks. One finding stays flagged on purpose: the Arnobius passage in Step 0 §4 item 2, where the words are right and the checker cannot read the line-number tag inside them. A targeted Opus review follows, in the review file the change order names. By the same ruling it does not count toward the cap of three; the System Hub Decision Log entry that says so is filed by the coordination thread.

## OG-26 — Step 0 cap-ruling targeted review: Approved to proceed (2026-10-29)

**Source:** `Build/worlds/latap/Review-Artifacts/Step0_CapRuling_Review.md`; Mark's ruling of 2026-10-29 on the Step 0 quotation change order.
**Status:** Review closed with its verdict. Two items are left for Mark's call. Owner: Mark.

The targeted Opus review checked all 24 rows of the change order against the real files and found no defect. A diff by two methods confirmed that only the 21 listed spans changed. The claim in finding 9 stands on the document's own evidence. By Mark's ruling the review does not count toward the cap. Its verdict is Approved to proceed (Step 0 only; not Frozen).

On a full checkout of `main`, handoff check 8 reports 7 findings. One is the Arnobius flag the order keeps. Six are genuine quotations that the checker cannot reach: four from Harnack's *Chronologie* II, which is not yet vendored on `main`, and two from Monceaux III, which Step 0 cites without the file path. These six are pre-existing and not defects of the order.

For Mark: whether a later change order adds the Monceaux path, and whether to bring all of Step 0's project-file quotations onto the single-mark convention.
