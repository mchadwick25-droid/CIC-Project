# Why three stories hold a Supporting bare statement, Grades3

Rule applied (`../2026-11-25_tradition-grades/README.md`, Rigor): one Supporting bare statement (weight 2) caps rigor at C; only Passing (weight 1) allows B. Weights are defined in `../2026-11-23_what-and-why-rank/Reader_Prompt.md` (2 Supporting: "sits in a part the piece spends real time on, or a main scene, while the heart still comes through"; 1 Passing: "mentioned on the way"). Where the two readers agree on a finding and their weights are one step apart, `Grades3/merge.py` keeps the higher weight, with no third read.

Nothing outside this file was changed.

## 1. antiochene-church-third-century

Sentence (live brief, paragraph 9): "That bishop set Lucian in a line from Paul to Arius: Lucian, he wrote, kept out of communion with the bishops for many years, and Arius and his party were shoots of the same root." Finding: missing why, weights [2, 2].

**(a) Held before?** Yes. It is the same gap, word for word. Grades2 held it at [2, 2] ("Why was Lucian out of communion with the bishops?"). `Fixes_Grade2.md` fix 2 added "but his letter does not say why". `Recheck_Grade2.md` BLOCKING 1 withdrew that change under Kit Part 1 ("tell it as they give it, with no reason added and no word on the missing one"; "do not announce it unless the gap is itself the story"). The sentence was therefore left as it was, and this round's readers found the same gap again.

**(b) Does a held source answer it?** No. The one old witness is Alexander of Alexandria's letter (c. 320s, Arius's enemy). It gives the act and how long it lasted, and no reason:
- `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` 5759-5770 (Jackson 1892): "Lucianus, his successor, withdrew himself from communion with these bishops during a period of many years."
- `cic/texts/anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml` 28778-28779 (ANF 1886): "To whom Lucian succeeding, remained for many years separate from the communion of three bishops."
- The Greek, `cic/texts/theodoret_opera-omnia-t3-historia-religiosa-pg82-grc-lat_migne1864.txt` 69674-69677 (OCR is damaged): "δεξάμενος Λουχιανὸς, ἀποσυνάγωγος ἔμεινε τριῶν ... ἐπισχόπων πολυετεῖς χρόνους", "remained separated from [the communion of] three bishops for many years". It gives no reason either.
- The next sentence (Thdt 5772-5775), "men who have greedily sucked down the dregs of this impiety, offsets of the same stock", ties Arius to Paul and Lucian. It is Alexander's charge of a shared impiety, but he never gives it as the reason for the break. Writing "for the same teaching" would add a cause that he does not state.
- The only line that gives a reason is modern: Hefele, `cic/texts/hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt` 15709-15711: "Lucian, priest of Antioch, defended for some time this heretical doctrine of the Trinity, and for that reason was excommunicated for a time." This is a nineteenth-century reconstruction. Telling it would be a modern-opinion finding, which costs more than the bare statement does. The editors' notes (Thdt note 295; ANF6 note 2429) are also modern, and they give no reason.
- I searched again myself. Only the ANF6 line and one unrelated Mansi line (42863) fall within a line of Lucian plus communion, separation or withdrawal. Of the Greek hits for ἀποσυνάγωγ-, only the Migne Theodoret line concerns Lucian.

This is the record's limit. Under the kit it cannot be named in the brief, and the recheck has already ruled on that.

**(c) Weight.** Supporting is fair. The Lucian section runs three paragraphs and carries the story's connection and ending (Outline "Connection", line 109: the listener "must hear it as" a charge), so the break sits in a main beat. The heart, Paul's judging, still comes through without it.

**(d) Verdict: source limit the rule penalizes.** The kit requires this act to be told bare. The scan counts it as a fault. No held old text can fill it, and the brief may not say the reason is missing. The only way to lift the cap is to cut the clause. That would be a change order against the outline's Never cut ("Alexander's charge as a charge") and against Kit Part 1's rule that a break is never cut, so the decision is Mark's.

## 2. roman-church-third-century

Sentence (live brief, paragraph 2): "Almost all that is told of its first decades comes from Hippolytus, a writer of that time who withstood two of Rome's bishops and lost." Finding: missing what ("Lost what?"), weights [2, 1]: reader A gave 2, reader B gave 1. The merge kept 2 because the weights are one step apart.

**(a) Held before?** No. This gap was newly sampled by this round's readers, and nothing changed it. The sentence has read the same since `brief.v3.txt`, and the second-grade fixes did not touch it. In Grades and in Grades2 only reader B flagged it, both times at weight 1 ("Lost what, and over what?"; "Withstood them over what, and lost what?"). Both times the third read struck it (Grades `third_read.md` S005; Grades2 `third_read.md` S002), because the later paragraphs explain what the quarrel was about. Grades2 held two other Roman gaps instead (Natalius's repentance and the confessors' return). This round both readers flagged the sentence, so it went to a merge rather than a third read. The narrowed question, "lost what?", is not answered by the later paragraphs the third reads relied on. Paragraph 3 says that Callistus became bishop, but it never says that Hippolytus lost the church to him.

**(b) Does a held source answer it?** Yes. Hippolytus's own account (Refutation IX, ANF 5, `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`) shows that the church went with the bishops and not with him:
- 13632-13640: "did not give place to him, but reproved and withstood him for the truth's sake. And he hurried headlong into folly, from the fact that all consented to his hypocrisy—we, however, did not do so—and called us worshippers of two gods".
- 13816-13818: "Thus, after the death of Zephyrinus, supposing that he had obtained (the position) after which he so eagerly pursued, he excommunicated Sabellius".
- 13951-13952: "they, lost to all shame, attempt to call themselves a Catholic Church!"; 13957-13958: "that most astonishing Callistus established, whose school continues".

The fewest words, replacing "and lost": "a writer of that time who withstood two of Rome's bishops, but the church sided with them." That is four words more. The witness is contemporary and hostile: Hippolytus himself, the losing side, admitting it against his own interest. Confidence: Documented as Hippolytus says (sheet Z9, C14; `Source_Sheet.md` line 20 already reads "lost" from 13957-13958).

**(c) Weight.** Passing is the fairer weight. The sentence is a note on the witness in the framing paragraph, not an event the piece spends time on. The quarrel itself is told at length in the next three paragraphs, and the heart (Rome's public arguments up to the split of 251) comes through whole. Reader B's 1 fits the Reader_Prompt's own example of something "mentioned on the way" better than A's 2.

**(d) Verdict: weight disputed.** The readers split 2 and 1, and only the merge's keep-the-higher rule makes it Supporting. It is also a real gap that held text can close cheaply (four words, from a contemporary source). Making that fix would remove the finding whatever weight it carries.

## 3. syriac-edessa-nisibis

Sentence (live brief, paragraph 9): "A Roman envoy, a bishop, came to a later Persian king. Through his work, the king ordered the churches his fathers had torn down to be rebuilt." Finding: missing both ("What did the envoy do, and why did the king change course?"), weights [2, 2]. Reader B asked only "What did the envoy do?"

**(a) Held before?** Partly. Grades2 held "a later king ordered the churches his fathers had torn down to be rebuilt", missing why, at weights [2, 1]. `Fixes_Grade2.md` answered that why with the envoy ("Through his work"), and `Recheck_Grade2.md` MINOR 1 reworded it into the present two sentences. The fix brought in "his work" without saying what the work was. So this is mainly a gap the second-grade fix created: a new "what". Reader A's "why did the king change course" carries the old gap forward, only half answered. Both readers now weigh it at 2.

**(b) Does a held source answer it?** Yes, for what the envoy did. For the king's reason, only in a later witness, and not in his own words.
- The acts of 410 (contemporary, the synod's own account; Chabot's French), `cic/texts/synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt` 16227-16231: "par la diligence et par les soins de l'apôtre, messager de paix, que Dieu dans ses miséricordes envoya en Orient, ... Mar Marouta, évèque, qui fut le médiateur de la paix et de la concorde entre l'Orient et l'Occident, qui s'appliqua à consolider les églises du Seigneur Christ". The grant itself (16155-16166) is dated "après que la paix et la tranquillité furent rétablies pour les églises du Seigneur" (16155-16156). The acts also credit Isaac's election (16168-16169) and the Roman bishops (16236-16237).
- Socrates, Church History VII.8 (later, c. 440, about 30 years after), `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` 19135-19142: "Necessity brought it about at that time that the Roman emperor thought proper to send Maruthas bishop of Mesopotamia ... on a mission to the king of the Persians. The king discovering great piety in the man treated him with great honor, and gave heed to him as one who was indeed beloved of God." 19174-19175: "he permitted Maruthas to erect churches wherever he wished"; 19186-19187: "For the Romans as a nation he had much regard". Socrates ties the permission directly to the wonders: the headache cured (19151-19153) and the magi's trick exposed (19153-19174). The sheet marks those wonders Contested and Leave out (sheet line 131).

The fewest words, answering what the envoy did from the contemporary witness: "A Roman envoy, a bishop who made peace between East and West, came to a later Persian king." That adds seven words. The witness is contemporary, and the confidence is Documented as the synod's account. Keep "East and West" exactly as the acts give it. The acts do not settle whether they mean the two empires or the two churches, since the same clause goes on to Western canons. The narrator must not turn it into "the two empires".

For the king's side, if the cap requires it: ", who honored him as a holy man, a later historian says". This adds eleven words, credited, from Socrates 19141-19142. The witness is later, and the confidence is Documented as Socrates's account. The wonders stay out. The king's reason in his own words is not held (sheet line 130). That part is the record's limit, and the brief does not mention it.

**(c) Weight.** Supporting is fair. The sentence is the turn of the closing paragraph. It answers the persecution scene that paragraph 6 spends real time on, and the ending ("like seeing the dead rise") rests on it. Even so, the outline plans beat 6 as a "hand-off, a clause or two", and the heart (hymns and vowed life, 201 to 410) still comes through without it.

**(d) Verdict: real fault we can fix.** The second-grade fix named "his work" and left it empty. The contemporary acts say what that work was, in seven words.
