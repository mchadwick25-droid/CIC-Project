# constantine-the-great notes

Files (all in /home/user/CIC-Project/cic/texts/): E = npnf201_eusebius-church-history-life-of-constantine.xml; S = npnf202_socrates-sozomen-ecclesiastical-histories.xml; L = anf07_lactantius-apostolic-constitutions-didache-liturgies.xml. Line numbers are file lines (XML lines break mid-sentence; quotes below were checked after stripping tags and joining lines).

## Claim table
| Claim | File : line | Support |
|---|---|---|
| Battle at the Milvian Bridge | L:10616 | "encamped them opposite to the Milvian bridge" |
| Lactantius: directed in a dream to put the heavenly sign (cipher of Christ) on the shields | L:10620 | "Constantine was directed in a dream to cause the heavenly sign to be delineated on the shields of his soldiers... the cipher of Christ" |
| Eusebius: Constantine told him himself, long afterward, and confirmed by oath | E:61197-61201 | "the victorious emperor himself long afterwards declared it to the writer of this history... and confirmed his statement by an oath" |
| Cross of light above the sun about midday, "Conquer by this" | E:61202-61206 | "about noon... he saw with his own eyes the trophy of a cross of light in the heavens, above the sun, and bearing the inscription, Conquer by this" |
| That night Christ appeared in sleep | E:61274 | "night suddenly came on; then in his sleep the Christ of God appeared to him with the same sign" |
| Wrote to Alexander and Arius that the cause was trifling | E:63875 | "intrinsically trifling and of little moment"; E:63870-63872 "truly insignificant character" |
| Such questions should stay in private thought | E:63910 | "ought certainly to be confined to the region of our own thoughts, and not hastily produced in the popular assemblies" |
| He had the council called at Nicaea | E:64275-64278 | chapter "How he ordered a Council to be held at Nicæa" |
| Sat among the bishops, "your fellow-servant" | E:64593-64594 | "at which I myself was present, as one among yourselves (... that I am your fellow-servant)" |
| Eusebius of Caesarea to his church: his statement of faith read before the emperor; emperor first to approve it | S:2988-2992, 3046-3049 | "which when read in the presence of our most pious emperor"; "our most pious emperor himself was the first to admit that they were perfectly correct" |
| Emperor urged the single added word homoousios | S:3049-3052 | "exhorting all present to give them their assent... with the insertion, however, of that single word 'homoousios'" |
| "of the same essence" | S:2951-2952 | Socrates's gloss: "homoousios, 'of the same essence,' or consubstantial" |
| Emperor explained it as no division | S:3052-3056 | "the Son did not subsist from the Father either by division or abscission" |
| Told churches Easter on one day everywhere | E:64607-64609 | "that this feast ought to be kept by all and in every place on one and the same day" |
| Language hostile to the Jews | E:64620 | "nothing in common with the detestable Jewish crowd" (letter at E:64577-64640) |
| Illness; knelt in the martyrs' church at Helenopolis | E:67750-67760 | "Here he passed some time in the church of the martyrs... kneeling on the pavement in the church itself"; Helenopolis from the chapter heading at E:67742 |
| Then asked bishops near Nicomedia for baptism | E:67782-67792 | "proceeded as far as the suburbs of Nicomedia, and there, having summoned the bishops... addressed them"; chapter title "requesting them to confer upon him the Rite of Baptism" |
| Eusebius names no bishop | E:67817-67819 | "the prelates performed the sacred ceremonies" |
| Sozomen: pagan story of remorse over Crispus, called an invention | S:26631-26651 | "it is reported by the pagans that Constantine... after assenting to the murder of his own son Crispus, repented... It appears to me that this story was the invention of persons who desired to vilify the Christian religion" |

## The quote
E:67792-67794 (printed across lines; chapter "Constantine's Appeal to the Bishops"): "The time is arrived which I have long hoped for, with an earnest desire and prayer that I might obtain the salvation of God." No trimming. "Conquer by this", "your fellow-servant" and "of the same essence," are also verbatim.

## Contested points and how marked
- Vision at the bridge: told as two accounts that differ (Lactantius dream only, shields; Eusebius sky-sign at noon plus dream, on Constantine's own word years later). Eusebius's own hesitation ("hard to believe") is in the file but I cut it for length.
- Baptism: Eusebius is the source; he names no baptizer. I did not name one. The editor of the Socrates file guesses Eusebius of Nicomedia (S:5592), which is a modern guess, so left out.
- Crispus: told as a pagan story that Sozomen rejects. His reasoning (Crispus lived until the twentieth year of the reign and laws favoring Christians date earlier) is in the file but not used. The file does not say how Crispus died, so the brief does not either.

## Dropped (checklist items not sourced or not usable)
- The Syriac chronicle under Zachariah's name (in the entry's sourcing field) is not in the files I used; dropped.
- Conversion by Silvester at Rome: not asserted.
- Donatists/Optatus quote and the Edict of Milan: not used (length).
- "Not a theologian": no source states it in the file's own voice (only a translator's footnote opinion at E:63940); expressed instead through his own letter that such questions belong in private thought.
- The year 312 and the date of the battle: not used in the brief; the file gives only "sixth of the kalends of November" with an editor's gloss.

## Uncertain
- "Eusebius of Caesarea told his own church" rests on the letter as quoted by Socrates (S:2980-3110), not on a standalone Eusebius text.
- 262 words, a few above the 230-260 aim.

## score.py
constantine-the-great.txt {'words': 262, 'secs': 105, 'fk': 9.6, 'fre': 62.5, 'fails': [], 'below': False}

## Round-1 changes (supersedes the first claim table where they differ)
- Opening: no longer states shields as shared fact. Eusebius: prayed to learn who God was (E:61185-61190), cross of light at midday, then sleep vision commanding a likeness of the sign (E:61202-61206, 61274-61277); Lactantius alone has the shields (L:10620). The vision happened "on this expedition" (E:61206-61207), so the brief says "Marching on Rome". The gold-and-jewels standard (E:61280-61290) went to the card side/cut for length. Eusebius's "hard to believe" line kept (E:61193-61195); the first notes wrongly said it was cut.
- Stray comma typo fixed.
- Outcome and edict added: Maxentius driven into the Tiber after the bridge was broken (L:10625-10628); Milan edict, "the Christians and all others should have liberty to follow that mode of religion which to each of them appeared best" (L:10684-10690), paraphrased not quoted.
- Arius: "If the Father begat the Son, he that was begotten had a beginning of existence: and from this it is evident, that there was a time when the Son was not" (S:2085-2095, Socrates I.5); creed anathematizes "There was a time when he was not" (S:3085); quote not used in the brief now (cut for length), kept in notes.
- "Eusebius, the bishop of Caesarea" named once; the pagan Crispus story moved to the conversion part, before Nicaea, and Sozomen named as the one who calls it an invention (S:26631-26651). Baptism paragraph now runs straight to his words and says he put baptism off and hoped for the Jordan (E:67794-67796).
- Cut for length: Easter letter (E:64607-64620, now on the card), Helenopolis kneeling (E:67750-67760, now on the card), goldsmiths.
- New claims: he divided the empire, buried in the Church of the Apostles with later emperors (S:30670-30700); letter asking for fifty copies of the scriptures (E:5587-5592, Life IV.36); five bishops refused homoousios (S:2949-2955); Eusebius of Caesarea accepted "having regard to peace" (S:3104); "first of the emperors who began to be zealous for the Church" (S:30668). The card's "Eusebius honors him as the first sovereign baptized in a church of the martyrs" rests on E:67823-67826.
- Score: words 292, FK 8.1, FRE 67.5, no failures. Over the 270 guide; two items cut already and the sources carry a lot of material.
- Quotes ("Conquer by this", "your fellow-servant", "of the same essence,", the baptism sentence) re-verified.

## Round-2 changes
- Baptism told as settled on the card (blocking): known_for no longer says "baptized near his death"; uncertain now carries the Zachariah chronicle (zachariah-rhetor_chronicle_hamiltonbrooks1899.txt:950-976, "Eusebius has failed to give an accurate account and Socrates has missed the truth (for the king was not baptized at the end of his life... the story of his conversion by Silvester is also preserved in writing and in pictures at Rome") and the Crispus story with Sozomen's verdict (S:26628-26651). Zachariah added to written_about. My earlier note that the chronicle was not in the files was wrong.
- "Put off baptism" removed: audio now "Only when he knew he was dying, Eusebius says, did he seek baptism. He had hoped to receive it in the Jordan." (E:67748-67752; E:67794-67796). The "postponement" wording was an editor's bracket (E:67762-67764).
- Homoousios: now "explained that the Son did not come from the Father by division or cutting off" (S:3052-3056, "did not subsist from the Father either by division or abscission"; verified).
- Legacy beat: Crispus story cut from the audio (now on the card); audio ends on burial: body carried to Constantinople, laid in the Church of the Apostles (S:30689-30695), later Christian emperors and bishops buried there too (S:30696-30700; checked as "it became the custom to deposit the remains of subsequent Christian emperors... bishops, likewise, were buried"). Colon sentence split. Card legacy_traces item 3 now the Easter letter (E:64607-64609, 64645-64652) so it does not repeat the burial. Card uncertain item 1 rewritten with the standard made at dawn (E:61280-61290).
- Length: the reviewer's text was 316 words. To reach 299 I cut the "churches' meeting places be given back" clause from the edict sentence (L:10690-10700; true, but dropped), the opening "Constantine wanted the church united" sentence, and trimmed the burial sentence and the homoousios gloss wording. Kept: Eusebius's "hard to believe" line.
- Score: words 299, FK 8.6, FRE 67.1, no failures. Quotes re-verified: "Conquer by this", "your fellow-servant", "of the same essence,", the baptism sentence.
