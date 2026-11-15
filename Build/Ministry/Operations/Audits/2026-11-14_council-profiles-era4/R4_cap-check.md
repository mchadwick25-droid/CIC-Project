# Era 4 council profiles: targeted check of round 3 minors

- **Date.** 2026-11-15.
- **Scope.** Under Mark's standing cap ruling of 2026-11-14 ("Minor round 3 fixes to reader-facing text get one targeted check without asking Mark", Church Family Tree Decision Log), this checks only the four strings changed from R3_recheck.md findings R3-CP3-1, R3-NIC-1, R3-NIC-2 and R3-QUI-1. It does not count toward the review cap.
- **Reviewer.** A fresh reviewer, who did not see the drafting or the earlier rounds.
- **Method.** Each string was read in its file against the vendored source lines named below. No model calls, no network, no paid services. Nothing was edited except this report.

## Summary

| # | Finding | File | Verdict |
|---|---|---|---|
| 1 | R3-CP3-1 | third-council-of-constantinople-680.brief.txt, paragraph 2, and its audio script | CLEAR |
| 2 | R3-NIC-1 | second-council-of-nicaea-787.entry.json, `people`, Theophanes | CLEAR |
| 3 | R3-NIC-2 | second-council-of-nicaea-787.entry.json, `issue[0]` | CLEAR |
| 4 | R3-QUI-1 | quinisext-council-692.entry.json, `outcome[2]` | CLEAR |

There are no minors.

## 1. R3-CP3-1: CLEAR

- **Text.** "Michael the Syrian, a Syriac Orthodox patriarch of the 1100s, writes from the side of the condemned."
- **Source.** Michael, Chronique, tome 2 (Chabot 1901), l.34484-34523. Michael says Macarius "montra clairement que c'est une hérésie d'admettre deux volontés ou opérations dans le Christ". He says the bishops "malgré eux, ils signèrent de force la définition", and that Macarius stayed "emprisonné jusqu'à la fin de sa vie". He ends: "C'est ainsi que s'introduisit l'hérésie pernicieuse de Maximus." He writes for the one-will side that the council condemned, so "from the side of the condemned" is true. The words "writes from" also make him the witness.
- **Read aloud in context.** Paragraph 2 now runs: the acts are "the record of the side that won"; "The condemned reach us mostly through their opponents' records"; then Michael is the exception. The contrast is clear and does not use "one will" before paragraph 3 explains it. Paragraph 3 then starts on the envoys' "forty-six years or so" without a jolt. The last paragraph ("Michael says the bishops signed under force ...") pays off the setup.
- **Tells and vocabulary.** No hedging filler, no assistant cadence and no project terms.
- **Audio.** When the two tags are removed, `audio/third-council-of-constantinople-680.audio.txt` matches the brief exactly (checked with diff). It has exactly two tags: "[calmly] " at the start and "[warmly] " before the last paragraph.
- **Score.** 398 words, FK 7.66, FRE 66.88. This matches round 3's scratch copy and meets the target (FRE 60 or above, grade 8 floor treated as a guide).

## 2. R3-NIC-1: CLEAR

- **Text.** "The Life printed with his Chronicle says he was called to the council and came in a hair shirt, riding a donkey; chronicler of the broken meeting of the year before and of the council"
- **Source.** Theophanes, Chronographia, PG 108 (Migne 1863), l.1703-1716, the Life: "Cum enim Nicaeae synodus secundo coacta esset, ad eam ipse quoque cum aliis Patribus vocatus est. Cumque omnes equis praestantibus ... venirent, ipse solito cilicino sacco indutus, asinae insidens, laetus iter suscepit. Sed cum omnes viderent eum ...".
  - "Called" is "vocatus est".
  - "In a hair shirt" is "cilicino sacco indutus", a garment of goat's hair.
  - "Riding a donkey" is "asinae insidens".
  - "Came" rests on "iter suscepit" and "cum omnes viderent eum", and is fair.
- **Witness.** The credit now comes first ("The Life ... says"), so a hagiographer's report is not told as settled fact. The misparse of "riding a donkey, by the Life" is gone.
- **Read aloud.** Clear. The clause after the semicolon is a role fragment, as in the other `people` lines.

## 3. R3-NIC-2: CLEAR

- **Text.** "We draw on Percival's English summary of it, which mostly follows Hefele."
- **Source.** NPNF 2.14, l.39206-39211. The heading is "Epitome of the Definition of the Iconoclastic Conciliabulum held in Constantinople, A.D. 754". Percival's note 530 says: "In this epitome of the verbose definition of the council, I have followed for the most part Hefele."
  - "Summary" is a fair plain word for "epitome".
  - "Mostly follows" matches "followed for the most part".
- **In context.** "It" refers to the Hieria decree in the sentence before it. The word "draw ... drawn" is no longer repeated. "We" is the profile's established voice for its own sources.
- **Tells.** None.

## 4. R3-QUI-1: CLEAR

- **Text.** "Later popes, as the Book of the Popes tells it: the emperor sent John VII the volumes again, and he returned them uncorrected, \"humana fragilitate timidus\", fearful in human weakness; ..."
- **Source.** Liber Pontificalis t.1 (Duchesne 1886).
  - At l.174285-174291, Justinian II, restored, sent the tomes "quos antea sub domno Sergio ... Romam direxerat" back to Rome by two metropolitan bishops. "Again" is right.
  - At l.174584-174586, John VII, "humana fragilitate timidus, hos nequaquam emendans per suprafatos metropolites direxit ad principem". "Returned them uncorrected" is right, and so is the gloss.
- **Witness and sense.** The emperor is now plainly the one who sends and John VII the one who returns, which agrees with the corrected `people` line. The Book of the Popes is credited at the start.
- **Read aloud.** "He" can only mean John VII, the one person named before it. No tells, and no project vocabulary.
- **Outside scope, noted only.** `uncertain[...]` l.233 ("John VII sent them back uncorrected") is a different field. It is consistent and was not checked as a changed string.

## Result

All four strings are CLEAR. Nothing remains open from R3-CP3-1, R3-NIC-1, R3-NIC-2 or R3-QUI-1.
