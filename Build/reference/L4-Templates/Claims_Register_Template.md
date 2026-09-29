# Claims Register: [world-code]

**File name:** `Build/worlds/[world-code]/[world-code]_Claims_Register.md`
**Made under:** Build Process V2.0, Section 4 (claim register control).
**Read by:** `python -m engine.m10.cli claims [world-code]`.
**Pattern:** `Build/worlds/lpc/Doc09_Claims_Register.md`.

## What the register holds

One row for every absence or exclusivity claim the world's deliverables and record files make about the record: "no source says", "the only", "never", "no other", "the sole", "is not attested", "is silent on", "nowhere", "exclusively", "absent from". The command derives the claims. It does not decide whether any of them is true.

The command reads the world's `Doc_NN` files, its chunk folders (`*-Chunks/`), its World Profile and Capsule Core files, and the prose fields and bodies of its record files. It skips review files, superseded material, this register, the gaps ledger and the decision log.

## Columns

The register is one markdown table with these columns, in any order.

| Column | Meaning |
|---|---|
| `id` | Eight hex digits derived from the claim's normalised text (markup removed, spaces collapsed, lowercased). Rewording a claim gives it a new id, so a reworded absence is a new claim and starts unregistered. |
| `status` | `VERIFIED`: checked at source, with the check named. `UNVERIFIED`: listed, not yet checked. `JUDGEMENT`: not decidable by a string search; rests on a named reading. |
| `confidence` | One of the five `formation_confidence` levels: Documented, Widely Accepted, Dominant Modern Reconstruction, Contested, Inferential-Thin. Required for `VERIFIED` and `JUDGEMENT`. Empty (`-`) is allowed for `UNVERIFIED`. |
| `source` | Where the claim's evidence sits: a Source Registry row, a `cic/texts/` path, a record id. `-` when unverified. |
| `check` | What was done and what it found. Required for `VERIFIED` and `JUDGEMENT`. `-` when unverified. |
| `file` | The base name of the deliverable or record file that carries the claim. |
| `claim` | The claim's normalised text, as `claims --bootstrap` prints it. |

## What the command halts on

- **Unregistered.** A claim in the deliverables has no row. This is the defect's only entry point.
- **Stale.** A row's id matches no claim in the deliverables any more. The text was reworded or removed.
- **Evidence does not resolve.** A row's `file` is not one of the world's deliverables, or a repository path (`cic/texts/...`, `Build/...`, `records/...`) or record id in its `source` or `check` cell does not exist.
- **Malformed.** A status outside the three, a `VERIFIED` or `JUDGEMENT` row with no check or with a confidence outside the five levels, a duplicate id, or a missing column.

`UNVERIFIED` rows do not fail the command. They are the honest state of a claim nobody has tested. The command reports how many there are.

## Working with it

1. Run `python -m engine.m10.cli claims [world-code] --bootstrap` to print an `UNVERIFIED` row for each claim not yet registered.
2. Paste the rows into the table below.
3. A reviewer who checks a claim at source changes its row to `VERIFIED`, fills `confidence`, `source` and `check`, and leaves the id alone.
4. A claim that changes in one document changes here, and every document that carries it is checked.

## Register

| id | status | confidence | source | check | file | claim |
|---|---|---|---|---|---|---|
| | | | | | | |
