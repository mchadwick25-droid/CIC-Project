# Review file rules

The header contract is `Review_File_Header_Template.md`. `python -m engine.m10.cli reviewfile <path>` checks it.

- File name: Step 0 is `Step0_Review_Round<n>.md` (world folder or `Review-Artifacts/`). Step 1 and Step 2 are `Doc01_Round<n>_Review.md` and `Doc02_Round<n>_Review.md` in `Review-Artifacts/`, one file per document per round. A combined review of two documents is filed as identical copies under both names.
- The round number in the file name equals the `Round` field.
- Optional field `- **Cycle reset:** <text>`, placed with the header fields, on the first review file after significant new material. The gate honours it only when both conditions hold:
  - the text cites, by its exact title, an entry that exists in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` (the ruling "The three-round cap counts from significant new material") or in a decision log under `Build/Ministry/`;
  - the round immediately before this file cleared review (`Approved to proceed`).

  Otherwise the reset is ignored, the full count stands, and the cap finding routes to the project lead. When honoured, the three-round cap counts from this file, which is the first round of the new cycle. Every file stays on record. A present field must not be empty or a placeholder.
- A bounded spot-check that closes a round's directed correction is filed under the same round number, not a new one.
- The latest round's file carries a `Disposition: Approved to proceed` line. A reviewer's "Clear" is not the disposition: the drafter records it after a clear review.
