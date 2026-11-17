# Review: Marcion of Pontus

Reviewer: independent brief review, 2026-11-17. Brief: `marcion-of-pontus.brief.txt` (343 words). I did not read the v1 brief or any earlier review.

## Verdict: REVISE

Two blocking findings, both single-sentence fixes. The brief is sound, well grounded and in an adult register, and every quote is verbatim. It handles the hostile record well: "firstborn of Satan" stays in Polycarp's mouth, the cutting of Luke and Paul is "his opponents say", and Tertullian's reading of Marcion's motives is credited and marked uncertain. One sentence lets Marcion's own charge against "the defenders of Judaism" slip into the narrator's voice. Another loses the listener at the expulsion.

## 1. Listener read (one pass, written before the other steps)

**Where I got lost or drifted**
- Paragraph 5, last sentence: "Yet Marcion claimed the reverse, Tertullian reports, because the defenders of Judaism had added to the Gospel, and he was restoring it." I stumbled on "the reverse": the reverse of cutting would be adding, yet he says others added. "Because" then sounds like the narrator giving his reason, not reporting his claim. I had to stop and work it out.
- Paragraph 6: "Rome expelled him more than once, Tertullian says of him and another teacher, Valentinus, and his gift was cast out along with him." The attribution breaks the sentence in two. After it, "his gift ... along with him" lands nearest to Valentinus, and the gift was mentioned three paragraphs back. I lost whose gift it was. The expulsion also passes with no sense of why it happened or what it meant.
- Paragraph 2 asks a lot of the opening sentence: three placing phrases stack up before the verb. I followed it, but only just.

**Where it sounds like a children's book or talks down**
- No stretch does. There are no runs of short one-act sentences (the profiler reports 0% short sentences), and no definitions are tacked on after a comma.
- Paragraph 7 comes nearest: "Irenaeus defended four Gospels against him, and Tertullian wrote five books against him." It reads as a list of acts, but it is not a children's-book run. Not a finding.

## 2. Trace against the outline

| Brief | Outline | Result |
|---|---|---|
| Polycarp opening, Irenaeus "who had seen Polycarp in his early youth" | Opening 1, Q2, Who tells it | Matches. Marcion asks and Polycarp answers. No place and no "old". |
| "how hard the church set itself against this man" | Q2 job | Matches. |
| Setting sentence; "gave the church money in the warmth of new faith" | Setting; beat 1 (M1, M2) | Matches. No wealth, no sum, no Sinope. |
| "Everything we know of Marcion comes from the men who wrote against him." | Who tells it, line to say aloud | Verbatim. |
| Tertullian: first faith, brooding, good tree, Isaiah; "his real reasons remain uncertain" | Beats 1–2, Inferential-Thin | Matches and is credited. "Until" links the two beats in time. This is fair to Tertullian's account (T 22621–22639), which presents the brooding as the start of the break. |
| Justin quote | Q1 rendering | The last two of the rendering's three sentences, word for word. Dropping "And there is a certain Marcion, from Pontus" changes nothing. |
| Antitheses, "now lost"; Q3 | Beat 4, Q3 | Matches. Q3 is word for word. |
| "His opponents say he cut down Luke's Gospel and Paul's letters." | Beat 5 | Matches. |
| "Yet Marcion claimed the reverse ... because the defenders of Judaism had added ..." | Beat 5 | The content matches, but the grammar moves his claim outside "claimed". See Finding 1. |
| Expelled more than once, with Valentinus, gift cast out | Beat 6 (M9, M1) | Content matches. See Finding 2. |
| "book after book ... one God made the world and sent Jesus"; Irenaeus four Gospels; Tertullian five books | Impact 3, 4 | Matches. |
| "his churches spread, and claimed martyrs of their own" | Impact 1, 2 | Matches. "Claimed" keeps the hedge, and no date is given. |
| Epiphanius: Rome and Italy, Egypt, Syria, Cyprus, Persia | Impact 1 | A selection. "As far away as" marks it as reach, not a full list. See Finding 4. |

Nothing in the brief falls outside the outline. It adds no feelings, weather or thoughts. The baptism detail, Cerdo and the repentance story are left out, which is allowed. The brief does not follow Polycarp's arc of arrest, trial, death and legacy; it follows the teacher shape.

**Quotes re-checked word for word in `cic/texts/`:**
- Q1 Greek, JG 729–731: "ὃς καὶ νῦν ἔτι ἐστὶ διδάσκων τοὺς πειθομένους, ἄλλον τινὰ νομίζειν μείζονα τοῦ δημιουργοῦ θεόν". Verbatim. The rendering is faithful.
- Q1 English, ANF 14943–14945. Verbatim.
- Q2, ANF 39882–39884: "Dost thou know me?" / "I do know thee, the first-born of Satan." Verbatim. Irenaeus "saw" Polycarp "in my early youth" (ANF 39860). Verbatim.
- Q3 Latin, OEH 4337–4338: "Separatio legis et evangelii pro-prium et principale opus est Marcionis". Verbatim. English at T 23734–23736. Verbatim.
- Supporting lines re-read: T 22613–22639 (the tree, brooding, "I am He that createth evil"); T 29248–29255 ("interpolated by the defenders of Judaism"); T 21335–21341 ("more than once expelled", the two hundred sesterces).

## 3. Readability

`python -m engine.m1.profile_readability` reports 343 words, grade 8.7 (7.2 with names out), reading ease 75.4 with names out, 18.1 words a sentence, 0% short sentences, longest sentence 30 words. **Pass.** The grade sits inside the 8–9 aim, and reading ease is well above 60.

## 4. Scores

- **Voice: 4.** The register is adult throughout. Cause and contrast are carried inside sentences ("until he began to brood", "yet in Isaiah", "Yet his churches spread"). It never talks down. One sentence (Finding 1) uses "because" in a way that shifts whose voice is speaking.
- **Craft: 3.** It opens on a strong hook and gives the setting early. The thread (law against gospel, one God answered back) is clear. Two things hold it back. The expulsion is told with no stake (Finding 2). What came of him takes about 70 of 343 words (about a fifth), not a third (Finding 3). It ends well, on how far his churches reached.
- **Rigor: 4.** Every sentence traces to the outline, and the quotes are exact and few. Witnesses are named where the listener needs them. Hostile charges are credited, and uncertainty is stated plainly: "his real reasons remain uncertain", and the martyrs are "claimed". One sentence lets a charge escape its credit (Finding 1).
- **Accessibility: 4.** It scores well within the limits. Two sentences do not survive one hearing (Findings 1 and 2).

## 5. Findings

**1. BLOCKING: Marcion's charge slips into the narrator's voice, and the sentence loses the listener.** "Yet Marcion claimed the reverse, Tertullian reports, because the defenders of Judaism had added to the Gospel, and he was restoring it." As written, "because ..." gives the narrator's reason for his claim. It is not part of what he claimed. So the narrator asserts as fact that "the defenders of Judaism had added to the Gospel". That is Marcion's charge against other Christians, which Tertullian reports (T 29252–29253). Under Mark's rule it must be credited, not carried forward. "The reverse" also confuses on one hearing, because the reverse of cutting sounds like adding.
*Change to:* "Marcion claimed the opposite, Tertullian reports: the defenders of Judaism had added to the Gospel, and he was restoring it." Any form works if the claim sits inside "claimed" or "said".
**Do not say** (add to outline): WRONG "because the defenders of Judaism had added to the Gospel", or any wording that gives his claim as the narrator's cause or fact. RIGHT "Marcion claimed, Tertullian reports, that the defenders of Judaism had added to the Gospel".

**2. BLOCKING: the expulsion sentence loses the listener.** "Rome expelled him more than once, Tertullian says of him and another teacher, Valentinus, and his gift was cast out along with him." The attribution splits the sentence. When "his gift ... along with him" comes, the nearest man is Valentinus, and the gift was last mentioned three paragraphs earlier. On one hearing it is unclear whose gift was cast out, and why the expulsion mattered.
*Change to:* two sentences that put Marcion back as the subject and tie the gift to its meaning. For example: "Tertullian says Rome expelled Marcion more than once, together with another teacher, Valentinus. The money Marcion had given in his first faith was cast out with him." The outline allows the reason, credited: Tertullian blames "their ever restless curiosity" (M9). If it is used, it must stay in Tertullian's voice.

**3. MINOR: the impact share runs short.** "What came of him" is about 70 of 343 words, against the standard's "about a third". There is room for one more clause of what the outline already ranks. Examples: Justin's "many of every nation", or Tertullian's "Even wasps make combs; so also these Marcionites make churches", credited. The aim is that his churches' reach gets its weight. Do not add a moral.

**4. MINOR: the Epiphanius list.** The brief gives a selection. That is acceptable, because "as far away as Persia" signals reach. The outline check (finding 7) asked that the list not sound complete. Ending it "... and as far away as Persia, and elsewhere" would honour that at no cost.
