# Alexandria identity-and-scaffolding pass: adversarial review, round 2 (2026-10-06)

Scope: targeted recheck of commit `a35fa0b4` ("alx: apply identity-and-scaffolding review round 1") on branch `records/identity-scaffolding-alx`, against the round 1 findings (`alx_identity_scaffolding_review_round1_2026-10-06.md`). Only the changed text, the bodies of the touched records, OG-17 and the package pin were checked. No model or API call was made.

Mechanical checks re-run by the reviewer:
- `python -m engine.m10.cli records alx`: PASS.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0.
- `sha256sum packages/alx/2026-10-06T22-18-30Z/manifest.json` gives `09529d70c139d69a2ea3023652d58057676bdbccd0e8943012f224865ab21594`. That matches `package.manifest_hash` in `records/worlds/alx.yaml`, and `package.location` names the same directory. The superseded `2026-10-06T22-02-26Z` package directory was renamed in the commit, so no orphan package is left.

## Verdict: CLEARED

## (1) Round 1 substantial findings

1. `alx.dw.councils`: FIXED. The text now opens "Who decided disputed belief changed across our own history: first the teachers, then the bishop, and at the end the council." It answers who first, and it is backed by positions[0]. "Our best picture of deciding well" is restored, which is also the origin/main wording. No new claim, and no orphaned reference.
2. `alx.dw.empire`: FIXED. The text now opens "Constantine's empire did not simply corrupt us. We lived both sides of that change inside one lifetime, and what we saw was double." This answers the question and keeps "both sides". "a church's" was dropped, so the close is the origin/main wording again ("The record does not show purity corrupted"). "That change" reads back to Constantine's empire.
3. `alx.dw.suffering`: FIXED. The text now opens "We gave three answers we could stand behind about why God allows suffering." The later duplicate sentence is gone, and "First, the teacher's answer" still follows correctly.
4. `alx.dw.jesus`: FIXED. "Between those two sentences lies the whole answer." became "All we hold about him lies between those two sentences." No answer-talk is left, and no claim is added.
5. Body commentary: FIXED. The REGISTER TRANSLATION, BAR SWEEP and LEXICON LABEL PASS paragraphs are gone from `alx.dw.councils`, `alx.dw.god`, `alx.dw.original-sin` and `alx.dw.suffering`. All 13 touched record bodies were reread. None carries change history or process narration now, apart from the two lines ruled on below.
6. OG-17: FIXED. See (3).

## (2) The two body lines kept by the author

- `alx.dw.church-failure`: "The church-failure cell: answered without defense-lawyering; the identity-collision-adjacent care lives in step-5 demonstrations." RULING: legitimate record note, not commentary. It says what the record is and how it answers, and it points to where the related material lives, the demonstration records. It does not narrate an edit, a review or a decision. It belongs to the same kind as the one-line descriptions round 1 kept, such as `alx.dw.one-church` "answered to the window's edge and honestly no further". This PR does not have to remove it.
- `alx.dw.god`: "Also tagged F1-P: the fixed-vs-open distinction IS the world's answer to 'was there room for doubt?' ... see alx.dw.doubt for the dedicated ground." RULING: legitimate record note, not commentary. It states and explains a fact that is true of the record now: `canon_cells` includes F1-P. It also cross-references the companion witness. It has no history and no process narration.

OG-17 flags both lines "for the project lead". This ruling settles that question, so it needs no further escalation.

## (3) OG-17 accuracy

Every sentence was checked against `git diff origin/main...HEAD`:
- The list of 12 records plus `alx.dw.jesus` matches the diff.
- Councils: the quoted opener, the restored wording and both sentence splits are accurate. "Patient public argument, loving the man while honoring the truth more" did become two sentences with the same content.
- Empire: the quoted opener is accurate. The close is the old wording. Both readability splits are accurate.
- Suffering: the opener is accurate. The duplicate is not repeated. The rhetorical question became a statement, and "answer to the question" became "answer". All are as stated.
- The statements on original-sin, church-failure, doubt, god, apostolic, one-church, record, resurrection and was-jesus-god match the diff word for word.
- `alx.dw.jesus`: accurate.
- The body-commentary paragraph names the right paragraphs in the right four files.
- The quotes paragraph is true: the Origen sentence in `alx.dw.apostolic` is unchanged.
- The known-wrong claims list is unchanged from round 1, where it was checked.
- The gate lines match the reviewer's re-runs where they were repeated. The package name and hash match the manifest and the pin.
- Status OPEN is correct pending this round.

No substantial findings.

## Not substantial

- When the branch merges, the OG-17 line that keeps the two body lines "for the project lead" can cite this ruling. It is accurate as written, so this is not required.
