# Recheck of Fixes_Grade3: The Roman Church in the Third Century

**Verdict: FIX** (one MINOR item: one of the four cuts blurs, on one hearing, who called the rule adultery and murder. The new sentence itself holds.)

Checked on a scratch copy outside the repository. Each of the five old strings in `Fixes_Grade3.md` occurs exactly once in `roman-church-third-century.brief.txt`. As written, the brief is 675 by `wc -w`. With the replacement below, it is still **675** (cap 675). Scorer, `python -m engine.m1.profile_readability <scratch>`, with the replacement: 673 words, grade 8.1 (names out 7.1), ease 76.2, 18.2 words a sentence, longest 35 (existing), pass.

## The new sentences against the source

**"Almost all that is told of its first decades comes from Hippolytus, a writer of that time. He withstood two of Rome's bishops, but the church sided with them."** (17 + 12)
- `anf05_hippolytus-cyprian-caius-novatian.xml`, read at the file. 13632-13640: "did not give place to him, but reproved and withstood him for the truth's sake. And he hurried headlong into folly, from the fact that all consented to his hypocrisy—we, however, did not do so". 13816-13818: after Zephyrinus died, Callistus, having got what he sought, "excommunicated Sabellius". 13951-13958: "they ... attempt to call themselves a Catholic Church! And some ... concur with them"; "Callistus established, whose school continues". My rendering: everyone went along with the bishop except Hippolytus's own party, and Callistus's following went on, as the church. "The church sided with them" says no more. Witness: contemporary, an enemy, and the losing side, admitting it against his own interest. Confidence: Documented as Hippolytus says. Right as the fix gives it.
- "Lost what?" is answered: the church went with the bishops, not with him. The slate's "the losing side, once, early" is kept. The one-witness sentence still names him once, early. "He" is Hippolytus and "them" is the two bishops, which is clear on one hearing. No reason for the church's choice is added; the "prosperity" sneer stays out. No barred quote ("worshippers of two gods") is used.

## The cuts, on one hearing

- **"In his words, as his enemy reports them"**: Q1 is still marked as Callistus's words reported by an enemy. Fine.
- **"and some Hippolytus's side had thrown out"**: same claim, and it matches "people other groups had refused" just before. Fine.
- **"He let a woman of rank"**: the new paragraph marks a further rule, and "He" is still Callistus. Fine.
- **"and called the rule a teaching of adultery and murder"**: MINOR 1, below.

## Findings

**MINOR 1. Cutting "he" from "and he called the rule" blurs who calls it.** The sentence would run: "Hippolytus charged that such women took drugs to avoid or end a pregnancy, not wanting a child by a slave, and called the rule a teaching of adultery and murder." Heard aloud, "and called" joins most readily to "such women took", inside the "that" clause. That makes the women the ones who called the rule adultery and murder. The charge is Hippolytus's (13949-13950, "inculcating adultery and murder at the same time"), and it is on the Never-cut list (Outline 251, the marriage rule with Hippolytus's charge). Keep "he". Take the word from paragraph 1 instead: "Then" after the whipping. The order of the sentences still tells the sequence, as Outline beat 1 gives it ("In the morning he put on sackcloth"), and no claim is lost. No sentence changes length past 25.

## Exact replacements

Drop the fix's fourth cut (`and he called the rule` → `and called the rule`). In its place:

- Old: `whipped him all night. Then he put on sackcloth`
- New: `whipped him all night. He put on sackcloth`

(The old string occurs once.) Apply the other four changes as written.

In the `Outline.md` item 34 text, replace `"He also let" to "He let" and "and he called" to "and called" (beat 4)` with `"He also let" to "He let" (beat 4); "Then he put on" to "He put on" (beat 1)`.

The outline line 9 and sheet line 51 edits are accurate: each old string occurs once, and the cited lines (13638-13640, 13957-13958) hold the words quoted.
