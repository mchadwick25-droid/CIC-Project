# hugo-grotius notes

Files (all in /home/user/CIC-Project/cic/texts/): G = grotius_defence-of-the-catholic-faith-satisfaction-of-christ_foster1889.txt; C = calder_memoirs-of-simon-episcopius_1838.txt; D = synod-of-dort_articles-with-history-of-events_scott1831.txt. Found by grepping "Grotius" across the Remonstrant files; G itself holds no biography of Grotius (no prison, escape, or England), so the life comes from C and D.

## Claim table
| Claim | File : line | Support |
|---|---|---|
| Jurist; writing on the law of nations prized in England | G:1270-1274 | "Grotius's work upon international law and his defence of the Christian religion were highly prized in England" |
| Stood with the Remonstrants (the Arminian party headed by Barneveldt and Grotius) | C:9777-9778, C:9525-9528 | "the Arminian party, at the head of which were Barneveldt and Grotius"; quarrel was on "grace and predestination" at C:6222-6225 |
| Calder wrote the life of Episcopius | C:title (Memoirs of Episcopius; running heads) | |
| King James told him he would think better of Remonstrants if sure they had no Socinian leaning | C:6235-6238 | "'if ye would have me to entertain a better opinion of Uitenbogaerdt and the Remonstrants, ye must first persuade me that these people have no inclination to Socinianism.'" (Calder is quoting Le Vassor/Brandt, C:6217-6224) |
| 1617, Leiden | G:364 | "probably the first edition, Leyden, 1617" |
| Socinus: God forgives like a creditor, no payment | G:654 (Foster); G:4611-4616 (Grotius on Socinus) | "A man can forgive a debt without payment: so can God"; "an offended party, ... a creditor, ... a lord" |
| Punishing/pardoning belongs to the ruler as ruler; God acts here as ruler | G:4546-4553; G:4768-4770 | chapter II title "...HE SHOULD BE CONSIDERED AS A RULER"; "this right belongs to the ruler as, ruler" |
| Christ's death a real penalty paid for believers | G:2517-2526 | "pay the penalty for our sins, in order that without prejudice to the exhibition of the divine justice, we might be liberated, upon the intervention of a true faith, from the punishment of eternal death" |
| Showed God's hatred of sin | G:6850-6858 | "God not only testified his own hatred of sin by this act, and so deterred us from sin" |
| Arrested with Barneveldt on the nineteenth of August by an officer of Prince Maurice's guard | C:15480-15486; C:15555-15557 | "layed hold on by the Lieutenant of the Princes guard on the nineteenth of August"; "Grotius and Hoogerbeets were likewise arrested by an officer of the prince's guard" |
| Condemned to prison for life (Mosheim) | D:4581-4582 | "Grotius and Hoogerberts were condemned to perpetual imprisonment" |
| Escape: wife sent him out of prison in a book chest | C:16625-16627 (footnote) | "his wife, who sent him out of prison locked up in a chest, which was accustomed to be filled with books" |
| Foster: Dutch Remonstrant leaders rejected it | G:913-914 | "it was rejected by all the great leaders of the school" (Episcopius, Limborch, Curcellaeus discussed G:1000-1160) |
| English Arminians largely adopted it | G:1281-1282 | "The English Arminians read, and, as we shall see, largely adopted the Grotian theory" |
| Foster calls it the governmental theory; Hopkins in New England | G:1931-1933, G:1947-1949, G:2017-2021 | "the governmental theory of the atonement makes its first appearance in New England"; "Samuel Hopkins (1721-1803) seems... to have adopted the governmental idea completely" |

## The quote
G:6853-6855, Grotius's own sentence as Foster renders it, printed across lines: "that sin should not be thought of less importance, if so many great sins should be remitted without an example." Trimmed at the front only (it continues a sentence that begins "God ... had sufficient, just, and great reasons for exacting of the willing Christ the punishment of our sins"). The brief marks it with "Grotius writes". Checked character for character after joining lines. I avoided the treatise's opening sentence because its OCR carries a footnote asterisk ("penalty*").

## Contested points and how marked
- The escape rests on a Calder footnote that calls the story "too well known to be repeated here"; Calder is an openly Remonstrant partisan. The brief gives it as "Calder adds".
- The imprisonment is Mosheim's statement as printed in Scott's edition, which also says the grounds are unknown to Mosheim. The brief gives it as "Mosheim says".
- The reading as "governmental" is Foster's, named as Foster's. I did not present it as the settled meaning of the treatise. Foster elsewhere says Grotius's theory of the ruler was misread by Turretin and Heidegger (G:810-860); not used.
- King James's remark is Calder's report via Brandt/Le Vassor, not a primary record; marked "reports".

## Dropped (checklist items not sourced)
- Date of arrest year, sentence date, and escape date: no file states the year in my passages; the brief gives only "nineteenth of August" and no year.
- Rector of Rotterdam/office: used nothing beyond what Calder prints ("Pensionary of Rotterdam", C:9382, C:9832); not in the brief.
- The England trip date and his role there: no year in file; brief mentions only the King James remark.
- Later life (Paris, Sweden) and "turned Papist" charge: not sourced beyond Baxter, and not in my passes.

## Uncertain
- 242 words, slightly over the 240 top of range.
- "stood with the Remonstrants in the Dutch quarrel over grace and predestination": joined from Calder pages, not one sentence.

## score.py
hugo-grotius.txt {'words': 242, 'secs': 97, 'fk': 9.3, 'fre': 61.6, 'fails': [], 'below': False}

## Round-1 changes (supersedes the first claim table where they differ)
- Witnesses fixed: King James's remark is Le Vassor's account, quoted by Calder (C:6215-6238); it is now told as "Le Vassor says", with "King James told him" (Grotius) so the "him" is clear. The arrest day (Cross's account, C:15464-15486) is dropped, as the reviewer suggested.
- Opening replaced by the England scene: in England on East India Company business, chosen by the Remonstrants (Brandt, C:6208-6216), received well by English divines except Canterbury, the king's "very harsh" and "author of sin" remarks, and his demand for proof against Socinianism (C:6226-6238).
- Imprisonment: "condemned to prison for life, though Mosheim says he does not know on what charge" (D:4581-4583). Escape told directly (source C:16625-16628, a Calder footnote, noted on the card as Calder's, "too well known to repeat").
- Foster no longer a witness in the audio: reception told directly (G:913-914, 1281-1282, 2017-2021); "governmental theory" label is attributed to Foster only on the card.
- Quote unchanged, verified (G:6853-6855).
- Score: words 241, FK 8.8, FRE 62.5, no failures.
- Card sources: Heidegger/Turretin G:795-860; Episcopius/Limborch G:1000-1160; Tillotson G:1285; Edwards/Zaleucus G:1962-1966; Hopkins G:2017-2021; Burnet 1692 (burnet_discourse-of-the-pastoral-care_1692.txt:7262-7265, printed "almoft got by heart", paraphrased not quoted); Baxter (baxter_reliquiae-baxterianae_sylvester1696.txt:10548-10550, "The Grotian Religion Discovered"); Foster G:755-757 (ban). Titles "On the Law of War and Peace" and "On the Truth of the Christian Religion" translate the Latin titles in an editor's note in baxter_autobiography...lloyd-thomas1925.txt:16330; Foster G:1270-1272 names the subjects.

## Round-2 changes
- Card claim that the name "governmental theory" came from Foster was wrong: Foster quotes Crawford, 1874, already using it (G:14062-14066). uncertain now says Grotius himself never calls his view that, and speaks of God acting as ruler (his chapters G:2471-12478 do not use the word, per the reviewer; I confirmed the chapter II wording at G:4546-4553).
- Baxter: now "in answer to Thomas Pierce, whose chief aim was to defend Grotius" (baxter_reliquiae-baxterianae_sylvester1696.txt:10548-10552).
- Audio: "Remonstrants" explained ("the Arminian side in the Dutch quarrel over grace and predestination", C:6222-6225, C:9777); Grotius "a law officer of Holland" (Calder via Brandt: "advocate-fiscal of Holland", C:6216; I used "law officer" instead of the reviewer's "lawyer" as the closer rendering). The fall of the Remonstrants told through Mosheim's words as Maclaine quotes them in Scott: the prince's party prevailed, those at the helm were imprisoned, Barneveldt "grown grey in the service of his country" died on the scaffold (D:4574-4582).
- Card uncertain item 1: Mosheim's admission and Hoogerbeets imprisoned with him (D:4581-4583; C:9831). Edwards claim now says the pastor at New Haven "may have read him" because of the Zaleucus illustration (G:1954-1966); Tillotson "stood first among the Arminians" (G:1285). Ban and prejudice told directly (G:754-760). Limborch/Episcopius line now "Episcopius, Curcellaeus and Limborch" (G:1000-1160).
- Titles: the Latin titles still come from the editor's note in baxter_autobiography...lloyd-thomas1925.txt:16330; "On the Truth of the Christian Religion" is also near Burnet's 1692 wording (burnet_discourse...:7262-7264).
- Score: words 282, FK 9.4, FRE 60.8, no failures (kept within the 300 ceiling; FRE just above the floor, so nothing was added).
- Quote re-verified: G:6853-6855.
