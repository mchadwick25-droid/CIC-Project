# lpc sermon quote batch 1: review, round 2 (targeted recheck)

- Reviewer: Opus 5.5 (`claude-opus-5-5`), independent reviewer. I did not draft, render or revise these records.
- Date: 2026-10-24
- Subject: fixes at `a41940e3` on `claude/lpc-sermon-batch1-2026-10-24`, diffed against `b01ea289`. Prior findings: `Build/worlds/lpc/Review-Artifacts/Sermon_Quotes_Batch1_Review_2026-10-24.md`.
- Sources: `cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt` (PL 38) and `cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml` (NPNF).
- Scope: only what changed. Main working tree untouched; gates run in a detached scratch worktree, removed afterwards.

## Changed files

The diff touches 12 files: the round-1 review file (new), `Build/worlds/lpc/scripts/wb_lpc_s24.py`, and 10 quote records. `stewards-and-future-bishops` and `apart-in-heart-united-in-body` are unchanged, as expected (no findings). No gravity record, no other generator script, and no `text` field changed.

## B-1 (P1): PL 38 ranges

I printed each corrected range with margin and checked the last line.

| Record | New range | Last line of range | Locus | Body | Result |
|---|---|---|---|---|---|
| `bind-him-justly` | 35544-35549 | 35549 "in coelo." | yes | yes | Fixed |
| `reprove-and-forgive-the-surgeons-knife` | 36195-36201 | 36201 "mentum ?" | yes | yes | Fixed |
| `peter-the-sick-man-and-the-physician` | 52934-52947 | 52947 "gationem timoris." (52948 blank, 52949 CAPUT IV) | yes | yes | Fixed |
| `going-out-without-violating-unity` | 38536-38542 | 38542 "plinam ; existi inde." | yes | yes | Fixed |
| `pardon-through-a-wicked-clergyman` | 32485-32492 | 32492 "rum." | yes | yes | Fixed |
| `consider-who-was-there` | 50696-50701 | 50701 "quis ibi fuit." | yes | yes | Fixed |

No range overshoots into the next sentence's own content beyond the line it shares. The generator holds the same ranges.

## P2 findings

| Finding | Applied as proposed | Result |
|---|---|---|
| B-2 locus "lines" to "line" (records 4, 5, 7, 9, 12) | yes, all five | Fixed |
| R1-1 "who are spread" | yes | Fixed |
| R3-1 drop "But" | yes | Fixed |
| R3-2 divergence note | yes, word for word | Fixed |
| R5-1 purpose clause | yes, word for word | Fixed |
| R5-2 lens note and first guard | yes, word for word | Fixed; residual wording in body, see N-1 |
| R5-3 second guard | yes, word for word | Fixed |
| R6-1 "presumed" | yes | Fixed |
| R9-1 "The sentences before the passage" | yes, plus verb agreement | Fixed (see extra fixes) |
| R10-1 "In the same way" | yes | Fixed |
| R10-2 retrieve_when trigger | yes, word for word | Fixed |
| R10-3 "That sentence and the next read:" | yes, plus follow-on sentence | Fixed; new problem in the follow-on, see N-2 |
| R11-1 "He may even come" | yes | Fixed |
| R11-2 guard typo | yes, word for word | Fixed |

### Renderings checked to the bar (every clause, nothing added)

- **ye-belong-to-my-care:** "who are spread over the whole world" matches *diffusorum per orbem terrarum* (agrees with *martyrum*) and NPNF "who are spread". Nothing added.
- **good-works-the-comfort-of-our-dangers:** "Why do we speak to you..." keeps every clause of *Quid autem nos loquimur vobis ... nisi ut de vestris bonis moribus gaudeamus*. Dropping "But" removes a false contrast; *autem* is a link only.
- **reprove-and-forgive-the-surgeons-knife:** "The Lord added 'from your hearts' for this reason: when discipline is given out of love, gentleness must not leave the heart." Carries *Ideo ... subdidit, de cordibus vestris, ut si per charitatem imponitur disciplina, de corde lenitas non recedat*: the addition, its purpose, the condition and the gentleness. Nothing added. 21 words.
- **peter-the-sick-man-and-the-physician:** "presumed" matches *praesumpsit* and NPNF. Nothing else changed.
- **the-branch-cut-from-the-vine:** "In the same way, feeling does not stay..." restores *ita ... quemadmodum* and NPNF "just as". Nothing added. 20 words.
- **pardon-through-a-wicked-clergyman:** "He may even come through a wicked cleric" carries *etiamsi per malum clericum*. Nothing added.

All changed sentences are 21 words or fewer.

### The two extra grammar fixes

- **going-out-without-violating-unity, body:** "The sentences before the passage ... quote ... say ... and define ..." and "Persona, sits inside the last of them." Checked against NPNF 15204-15208. The Isaiah quotation, the "we/they" sentence and the definition are separate sentences, so the plural verbs are right. *Persona* (line 15207) sits inside the last one, the "And what is it to 'go out from thence'..." sentence. Correct.
- **the-branch-cut-from-the-vine, body:** "That sentence and the next read: '...'" is correct; the quote spans the end of the 12926-12932 sentence and the whole "For 'this form of godliness'..." sentence. The follow-on change is not correct; see N-2.

## Regressions

- The record diffs match the generator diff line for line. Only the intended fields changed: `sources[].locus`, body, `modern_rendering`, `divergence_note`, `modern_lens_note`, `claim_guards` and one `retrieve_when` entry. No `text`, `speaker_or_author`, `confidence` level, relation or canon cell changed.
- `reprove-and-forgive-the-surgeons-knife`'s `modern_rendering` is now single-quoted YAML because of the new colon. It parses; the gates load it.
- Gates at `a41940e3`: `records lpc: PASS`; `regate lpc: PASS` (12 new or edited fields; 11 below FK 8, reported, not failed, same as round 1; other notes are unchanged base failures).

## New findings

### N-1 (P2): "household" left in the surgeon's-knife body

R5-2 removed "household" from the lens note and the first guard, because nothing in the text names a household. The body still says: "The household illustration about unruly boys is at lines 14437-14443." NPNF 14437-14443 has unruly boys and "us when we wish to chastise them", with no household. This is the same unsupported detail R5-2 removed, left in one place. It was not in R5-2's proposed fix, so it is a residual, not a drafting error.

**Proposed body text:** "The illustration about unruly boys is at lines 14437-14443."

### N-2 (P2): branch body now says notes break both sentences

The drafter changed "It is not part of the passage because translators' notes break it" to: "They are not part of the passage because translators' notes break them." The first sentence (NPNF 12926-12932) is broken by notes (*Congregationibus vel potius segregationibus*, Gal. iv. 29). The second, "For 'this form of godliness' was not wanting to them ... which cannot be given but within", sits whole on line 12932 with no note inside it. So the statement is now wrong for the second sentence.

**Proposed body text:** "Translators' notes break the first of them, and another sentence and a note stand between them and the passage, so they are not part of it."

Neither finding affects quote text, loci, renderings or guards. Neither blocks.

## Counts

- Prior findings: 15 (B-1 P1; 14 P2). Fixed: 15. Not fixed: 0.
- New findings: P0 0, P1 0, P2 2 (N-1, N-2).
- Regressions: 0.
- Gates: records PASS, regate PASS.

VERDICT: Approved to proceed
