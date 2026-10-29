# Open Gaps — The Latin Apologists

Append-only ledger for this world's build. Entries are numbered and dated; a merged entry's number never changes. Cross-references cite subject and date, not a bare number. The world's file-code is `latap`.

---

## OG-23 — Step 0 quotation findings fixed by change order; one finding stays flagged (2026-10-29)

**Source:** `Build/Ministry/Operations/Audits/latap_Step0_QuoteFixes_ChangeOrder_2026-10-29.md`; handoff check 8 for `latap`.
**Status:** Open until the targeted review is filed. Owner: the coordination thread for the System Hub entry; a different worker for the review.

Handoff check 8 reported 24 quotation findings, all in Step 0. By Mark's ruling of 2026-10-29 they are fixed by the change order named above, with nothing else in Step 0 touched. The order classifies each finding, gives the file and lines checked by hand, and lists 21 exact edits. Two quotations whose origin could not be found anywhere in the tree lose their quotation marks. One finding stays flagged on purpose: the Arnobius passage in Step 0 §4 item 2, where the words are right and the checker cannot read the line-number tag inside them. A targeted Opus review follows, in the review file the change order names. By the same ruling it does not count toward the cap of three; the System Hub Decision Log entry that says so is filed by the coordination thread.

## OG-24 — Step 0 cap-ruling targeted review paused in progress (2026-10-29)

**Source:** `Build/worlds/latap/Review-Artifacts/Step0_CapRuling_Review.md`; Mark's ruling of 2026-10-29 on the Step 0 quotation change order.
**Status:** Open. Owner: the cap-ruling review worker on resume.

The targeted Opus review of the Step 0 quotation change order stopped at a usage checkpoint. It has no verdict, and Step 0 is not yet cleared under it. Done: the diff check (only the 21 listed spans changed, by two methods) and 20 of the 24 rows. Not done: rows 1, 6, 9 and 17, the history claim in row 16, finding 9's unchecked claim, the quotation-mark pass, and the remaining check-8 flags. First thing on resume: the handoff gate run for this review reported 31 check-8 findings in Step 0, not the 7 the change-order worker reported. Rerun it in a full checkout of `main` and find out whether the higher count is real or comes from the sparse checkout.
