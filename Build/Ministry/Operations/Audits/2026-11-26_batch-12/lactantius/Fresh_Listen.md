# Fresh listen: Lactantius

A new first-time listener (no church background, English as a second language), hearing the final `lactantius.brief.txt` once. No source, outline, other read, `Revision.md` or earlier draft opened. Judged by the bar in `Brief-Kit/Kit.md` and `kinds/person.md`.

**Verdict: PASS.** Nothing is BLOCKING. Seven MINOR findings, each with its exact change below. Applied together they bring the brief from 673 words to 671, inside the approved 675.

## Counts

| Check | Count |
|---|---|
| Test lines unfilled | 0 of 4 |
| Opening leaves listener lost about who or where | No |
| Sentences that fail on one hearing | 4 (all MINOR, none loses the thread) |
| Bare statements | 0 |
| Citations read aloud that Part 1 does not call for | 0 |
| Tells Part 1 names | 0 |
| Unexplained words | 3 (MINOR) |
| Runs of short one-act sentences | 0 |
| Talks down | 0 |

## 1. The test (person)

- **Who he was:** filled. He was a teacher of Latin public speaking from Africa, working at the emperor's city of Nicomedia. He wrote Christian books, and in old age he taught Constantine's son.
- **What happened:** filled. The persecution began around him in 303. Two writers attacked the Christians in front of him. He answered with the Divine Institutes. Later a bishop turned his sentences against an emperor.
- **What it was about:** filled. Religion cannot be forced because it lives in the will. Argue from the pagans' own authorities. Defend religion "not by killing but by dying."
- **Why the connection matters:** filled. He is the last of the Latin Apologists, and he judged Tertullian and Cyprian. Jerome kept reading him. Lucifer reused his words against an emperor who used the sword.

## 2. The opening

After the first three sentences I have his name, the place (Bithynia, a name I don't yet know) and the scene: a governor rejoicing that a tortured man gave way. Three things are still missing: what Lactantius was (that he was a teacher, or even a Christian), when this happened, and why he was there. Sentence 4 fills all three at once: Nicomedia, north-west Turkey, Diocletian's palace, 303. I am not lost, so this is not a finding. The opening pulls me in: the gloating governor is vivid and strange.

## 3. Sentences that fail on one hearing (MINOR)

**3a.** "He came from Africa, says Jerome, writing later that century, on whom most of his life outside his books rests."
Meaning lost: "on whom … rests" comes too late. On one hearing I can't tell what rests on whom. I also don't know who Jerome is (see 7a).
Change to: "Most of his life outside his books rests on Jerome, a Christian writer later that century, who says he came from Africa." (+2 words)

**3b.** "His own were divine, a full course on hope, life, salvation, immortality and God."
Meaning lost: heard aloud, this sounds as if the narrator is saying his books were divine. It does not come across as the book's title.
Change to: "He called his Divine, a full course on hope, life, salvation, immortality and God." (0 words)

**3c.** "A book on how the persecutors died survives in one copy under the name of a Lucius Caecilius, and whether it is Lactantius's is disputed."
Meaning lost: a new name arrives with nothing to tie it to Lactantius. I can't tell why this man's book belongs in Lactantius's story. This is also where my attention drifts most (see 8).
Change to: "A book on how the persecutors died survives in one copy, and whether Lactantius wrote it is disputed." (−7 words) The trust reader should confirm this still tells the book only as far as the old sources credit it to him. If the outline holds a plain line tying the name "Lucius Caecilius" to Lactantius, say that line instead of cutting the name.

**3d.** "Yet he asked who could forbid him, Jerome, to read the Institutes, written against the pagans with much ability."
Meaning lost: "forbid him, Jerome, to read" is a knot. I have to work out that Jerome is defending his own reading.
Change to: "Yet he asked who could stop him, Jerome, from reading the Institutes, written against the pagans with much ability." (0 words)

## 4. Bare statements

None. The story explains each thing it names: the Divine Institutes, the Great Persecution and its order, the two attacking books, the Latin Apologists, the title "Institutes", the book on the persecutors and the Arian teaching.

## 5. Citations read aloud

None that Part 1 does not call for (see the tool results below for the three the checker lists). "As he tells it" (the philosopher) and "he said" (the judges) credit Lactantius's own judgment of his enemies, which Part 1 calls for.

## 6. Tells

None. There are no dashes, stock words, moral close or questions asked only to answer them. The "not … but" in the quote and in Lucifer's echo of it are the record's own words, and the echo is the point of that paragraph. Neither is a turn in the narrator's voice.

## 7. Unexplained words (MINOR)

**7a. Jerome.** He is named three times and is the main witness, but I am never told what he was. This is fixed by the change in 3a ("a Christian writer later that century").

**7b. Gaul.** I don't know where it is.
Change: "taught Constantine's son Crispus in Gaul." to "taught Constantine's son Crispus in Gaul, now France." (+2 words; the trust reader confirms the gloss against the outline's Setting)

**7c. Cagliari, and the name Lucifer.** Heard cold, "Lucifer" startles a listener, and "Cagliari" is only a sound.
Change: "Lucifer of Cagliari, a bishop, wrote" to "Lucifer, bishop of Cagliari in Sardinia, wrote" (+1 word; the trust reader confirms "Sardinia" against the outline's Setting)

No runs of short one-act sentences. Nothing talks down.

## 8. Attention

- **Opening:** it pulls me in.
- **First drift:** at sentence 9 (3a). After the clear sentence 4, the tangled Jerome clause makes me stop and untangle it.
- **Worst drift:** the Lucius Caecilius sentence (3c). A new, unexplained name in a book whose link to Lactantius I can't see feels like a detour. With the name cut, the paragraph moves straight to Constantine's dream and on to Crispus.
- **Second, smaller dip:** the Lucifer paragraph. I hear the bishop's words before I learn they are Lactantius's. The paragraph's last sentence brings me back.
- **Would I listen to the end?** Yes. The two attacking books, the judgment of Tertullian and Cyprian, and "not by killing but by dying" carry me through. The close on his poverty lands, because it follows the poor-praising philosopher he answered.

## Tools

`python -m engine.m1.profile_readability …/lactantius.brief.txt`:
674 words, grade 9.8 (names out 8.6), reading ease names out 67.4, 19.3 words a sentence, 0.7 joining words per 100, 3% short sentences, longest sentence 33 words: **pass**. This is within grade 10 and ease 60. Grade 9.8 with names in sits near the limit, which is a warning only. Changes 3a and 3c should lower it a little.

`python tools/check_brief_craft.py …/lactantius.brief.txt`: 5 to look at, each judged by Part 1:
- **s6, modern-scholar word** ("their own philosophers and historians"): false positive. These are the pagans' ancient historians, not modern ones. No change.
- **s9, names a source** (Jerome): called for. Most of the life rests on one witness, and Part 1 says to say so once, early, inside a sentence about that witness. Recast for clarity in 3a.
- **s12, names a source** ("Its aim, Lactantius writes"): called for. The motive of the order is told from the persecuted side, in the voice of a witness who is also in the story. No change.
- **s19, names a source** ("Lactantius says"): Lactantius is the subject speaking, which makes him part of the story, not a citation. No change.
- **s33, not X but Y** (Lucifer): this is the record's own reused wording, and showing that reuse is the paragraph's point. It is not a turn in the narrator's voice. No change.
