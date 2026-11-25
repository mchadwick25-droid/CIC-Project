# Craft pass (story-shape rebuild): The Second-Century Greek Apologists

Under Mark's ruling "a" (Decision-Log, "Batch 11: the two rebuilt stories ship"). Backup before any change: `greek-apologists-second-century.brief.v5.txt` (675 by `wc -w`, never edited). Live file: `greek-apologists-second-century.brief.txt`. Fixes taken from `Trust_Shape.md` (BLOCKING), `Listen_Shape_FirstTime.md` and `Listen_Shape_Skeptic.md` (BLOCKING, and MINOR where a plain word does it). No other sentence reopened.

## Record files

- `Outline.md`, Do not say: the line `"his petition survives" → "only the passages Eusebius copied survive"` is replaced, as `Trust_Shape.md` directs, by its line word for word: `"only the passages Eusebius copied survive" / "nothing else of it survives" → "Eusebius copied passages from his petition" (anf08 71060–71070 holds a further fragment from the *Chronicon Alexandrinum*).`
- `Source_Sheet.md`, Set aside, anf08 Melito line: "fragments of his Apology that repeat Eusebius's extracts" now reads "fragments of his Apology: Fragment II repeats Eusebius's extracts (anf08 70962–71058); Fragment III, "From the Same Apology", comes from the *Chronicon Alexandrinum*, not Eusebius (anf08 71060–71070)." Checked in the file: Fragment II's note cites Eusebius, *Hist. Eccl.*; Fragment III's note gives the *Chronicon Alexandrinum*. Fragment I is from the Passover work, not the Apology, so "two repeat" would be wrong.
- Not touched, for the caller: `Outline.md` still carries the barred wording "only the passages Eusebius copied from his petition survive" in Story beat 4, What came of it 1 and Cut first 9. The brief does not.

## Changed sentences

| # | Finding | Old | New | Source line |
|---|---|---|---|---|
| 1 | Trust BLOCKING; both listeners' tell (B3) | Only the passages Eusebius copied from his petition survive. | Eusebius copied passages from his petition. | `Trust_Shape.md` exact wording; npnf201 25826 ("a little further on he says"); Outline Do not say (new line) |
| 2 | Quadratus bare (FirstTime 4; what his defense argued) | So Quadratus, a Christian, addressed a defense to the emperor, and Eusebius, a church historian, still had the book in the early 300s. | So Quadratus, a Christian, addressed a defense to the emperor. Christ's works were real, he wrote: some Christ healed lived to Quadratus's day. Eusebius, a church historian, still had the book in the early 300s. | Source_Sheet line 42 (npnf201 21056–21068: "the works of our Saviour were always present, for they were genuine:—those that were healed … some of them lived even to our day"). Do not say: no "had seen" (Outline line 134). The Eusebius clause is kept, now its own sentence (Outline Never cut; Who tells it) |
| 3 | Theophilus: why the books' age would count (Skeptic B2) | Theophilus wrote to him, counting back the years to show that the books of Moses, the first in the Bible, were older than the Greeks' own. | Theophilus wrote to him, counting back the years to show that the books of Moses, the first in the Bible, were older than the Greeks' own, and so their teaching true. | Source_Sheet line 97 (anf02 11091–11095: "the antiquity of the prophetical writings and the divinity of our doctrine, that the doctrine is not recent, nor our tenets mythical and false … but very ancient and true"). Held inside "to show that", so it stays Theophilus's claim |
| 4 | Valentinians: what the quarrel was about, and that it was a second task (FirstTime 4; Skeptic B1) | He wrote against the followers of a teacher, Valentinus. | He also wrote against the followers of a teacher, Valentinus. | Outline line 69, 75 (beat 7; What came of it 2) |
| 5 | Same; and why the connection matters (FirstTime 1; Skeptic 1, thin) | They stacked heaven on heaven for their gods, he scoffed, and he named Justin first among the earlier writers who had refuted them. | They stacked heaven on heaven for their many gods, he scoffed, and he drew on earlier writers against them, Justin first. | "many gods": anf03 43237 ("a dwelling for each several god of theirs"), Outline lines 69, 153. "drew on earlier writers … Justin first": Outline lines 75, 100 ("He said he drew on earlier Christian writers, and named Justin first"; "Tertullian used Justin's work"), placed after the Valentinians, against them, per Outline line 160. Credited scorn kept ("he scoffed", Outline line 155) |
| 6 | MINOR (both): "one" heard as "one God" | Yet one stood against Christians, who said the same. | Yet a law stood against Christians, who said the same. | FirstTime's exact change; athen-grc 316 (ἐφ᾿ ἡμῖν δὲ κεῖσθαι νόμον), Outline line 67 |
| 7 | MINOR (both): "the godly", "driven about" | …in today's western Turkey, the godly were driven about by new decrees, new written orders, as Melito… | …in today's western Turkey, Christians were hounded by new decrees, new written orders, as Melito… | npnf201 25818–25821 ("the race of the pious is now suffering persecution, being driven about"), Source_Sheet line 69 |
| 8 | Cut for the 675 cap | They worshipped God alone, and gladly served the emperors in all else. | (cut) | 1apol-grc 512–513. Also the Skeptic's short-run MINOR (b). The loyalty theme stays in the essence ("prayed for the emperors") and in Athenagoras ("lives, teaching and loyalty"); the taxes line stays. Outline's Never cut names "his taxes and loyalty": this is a named loss, the caller's to weigh |

## Cuts named

- Sentence 8 above, 12 words.
- In fix 2, Quadratus's passage is told at its shortest: "raised from the dead" and "even" left out (card keeps the full passage, Cut first 4).
- In fix 5, "who had refuted them" gives way to "against them".

## MINOR items left

- "atheists of such gods": the Outline's Do not say prescribes this wording (line 166). Left.
- "the honour of such a death": inside Quote 1, word for word. Left.
- "Long before" (whose before?), "certain wicked men": no plain-word fix the outline holds. Left.
- "Carthage" unplaced: no held line gives its region. Left.
- "Eusebius, a church historian, still had the book in the early 300s" read as a citation: kept, since Who tells it needs the 300s gap and fix 1's Eusebius needs this gloss.
- Para 7 run of short sentences: the outline's planned three-sentence form. Left.

## Count and scorer

`wc -w`: 675 (v5: 675).

`python -m engine.m1.profile_readability …/greek-apologists-second-century.brief.txt`:
`675 words, grade 7.9 (names out 7.1), reading ease names out 73.6, 16.5 words a sentence, 0.7 joining words per 100, 10% short sentences, longest sentence 38 words - pass (note: grade 7.9 is under 8: the listener read checks it is not flat)`
