# Witt generator scripts retired, 2026-10-27

Two build scripts for the Witt records moved to `Archive/Superseded-Engine-Code/Build/worlds/witt/scripts/`:

- `wb_witt_s21.py` wrote `records/witt/world_core/`.
- `wb_witt_s22_s23.py` wrote the term records, including `witt.term.insurrection`.

## Why

Both scripts still hold the wording of the 1525 and 1543 rule that was in force before the witness change order (Open Gaps OG-86 and OG-88). Running either one would overwrite the hand-edited records with that old wording.

- `wb_witt_s21.py` holds the old `thinness`, `cautions` and keyword notes for 1525 and 1543 in `witt.core.witt`.
- `wb_witt_s22_s23.py` holds the old `divergence_note`, `false_friend`, `translational` sense and retrieval lines in `witt.term.insurrection`, which said the 1525 tract is not in the library.

The records are now edited by hand and checked by the record gates. Keeping the scripts live would leave a one-command way to undo the ruling.

## Checked before the move

- Nothing in `tools/`, `.github/` or `engine/` imports or calls either script.
- `wb_witt_s25.py` has no 1525 or 1543 text and stays in `Build/worlds/witt/scripts/`.
- Review files that name the scripts by path (for example `Build/worlds/witt/witt_GoLive_Adversarial_Review_Round1.md`) are history and were not edited.
