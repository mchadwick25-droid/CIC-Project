# R4 cap check: era 4 batch 4, round 3 strings only

## Scope

This is the one targeted check that Mark's standing ruling of 2026-11-14 allows ("Minor round 3 fixes to reader-facing text get one targeted check without asking Mark"; `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`). It does not count toward the cap. It covers only the strings changed in round 3, as listed in `R3_changes.md`. The diff checked is `git diff 8cde26e9..b46401f8 -- Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch4/`, which spans the two round 3 commits (92ffff44, b46401f8). The range 8b11d4e0 does not exist; the coordinator confirmed 8cde26e9 as the state before round 3. The diff touches 12 files and matches the R3 table row for row. Nothing outside the diff was reviewed, except where a string's meaning depends on its context.

## Method

- (1) Source check. Each changed string was read against the vendored lines that `records.json` cites in `cic/texts/`: BERT (Waitz 1883) l.98-150, 152-263, 3526-3539; MANSI16 l.66955-67158; PL115 l.79262-79310, 79376-79391, 79618-79632; PL80 l.51995-52062; PL96 l.638, 3640, 3840-3876, 16518, 36013, 36860-36892, 37355-37392; MGH11 header and l.16360-16365, 32605-32626; REES header, l.144, 13450-13463. The OCR was read with the long s as f and the two-column interleave taken into account.
- (2) Clarity. Each string was read once as a listener would hear it. The checks: pronoun and "its" targets, every witness attached to a speaker, and every name given a role or identifier at its first mention in its own field.
- (3) Tells. Each string was checked for AI tells, narrator contrasts and beat lines.
- (4) Length and grading. Card sentence length was checked against about 25 words. Both changed briefs were graded with `engine.m1.gates.grade_text`. Each audio file was compared by script against its brief, with `[calmly] ` added at the start and `[warmly] ` at the start of the last paragraph.

## 1. hincmar-of-reims, brief P4 and audio: PASS

"In his own letter, the uncle wished he had never seen the man, still less ordained him." MANSI16 l.67130-67155 is headed "Epistola Hincmari Rhemorum archiepisc. ad Hadrianum papam" and reads "Quem utinam non vidissem, minime autem illum me ordinare in episcopum contigisset". The string says no more than the source. "The uncle" now settles which Hincmar is meant, and "the man" can only be the nephew. Grade: FK 6.50, Flesch 74.88; 406 words. The audio file matches the brief exactly with both tags in place.

## 2. hincmar-of-reims, legacy.traces 3: PASS, one MINOR

"The annals for 861 give Prudentius's Spanish birth and his turn in the predestination quarrel. G. H. Pertz holds that Hincmar wrote the annals from that year." BERT l.3530-3536 gives "natione Hispanus" and the turn ("Gotescalco ... restiterat, post, felle commotus ... heresis defensor acerrimus"). BERT l.203-205 has Pertz: "annalium inde ab a. 861. auctorem ipsum Hincmarum fuisse, extra dubium venit". The attribution to Pertz is now correct, and "holds" fairly renders "extra dubium venit". MINOR: this is the first mention of Pertz in the `traces` field, and it has no role. Prudentius is also bare here, but that wording predates round 3. Suggested fix: "G. H. Pertz, an earlier editor of the annals, holds…".

## 3. hincmar-of-reims, keyWorks 1: PASS

"Georg Waitz, who edited them, says some have held them to be official annals and others have doubted it." BERT l.66 ("RECENSUIT G. WAITZ") and l.338-357 (signed "G. WAITZ") show that Waitz edited them. At l.250-253 he writes: "ut seriem annalium publica auctoritate susceptorum continuarent, alii contenderunt, alii in dubium vocaverunt". "Official annals" fairly renders "annales publica auctoritate suscepti". The sentence has 19 words.

## 4. prudentius-of-troyes, brief P2 and audio: PASS, one MINOR

"On his death the annals name him Galindo, called Prudentius, a Spaniard by birth." BERT l.3530-3531 reads "Galindo cognomento Prudentius ... natione Hispanus", in the death notice. The source check holds, and removing "Hincmar" as the speaker correctly drops a disputed attribution from the brief. MINOR: "the annals" first appears here, but P3 is the first paragraph to say which annals they are ("He kept the annals of the Frankish kings' deeds, now called the Annals of Saint-Bertin"). A listener hears "the annals" before they have been introduced. Suggested fix: anchor it in P2, for example "In the annals he had kept, the entry on his death names him…". Alternatively, accept it as is, since P3 resolves it within seconds.

## 5. prudentius-of-troyes, brief P4 and audio: PASS

"Prudentius took the side Hincmar of Reims opposed." With the P2 change, this is now Hincmar's first mention in the brief, and "of Reims" identifies him. PL115 lists the sides ("Hinc ... Hincmarus Remensis ... Hinc Prudentius noster"; records claim on sides). Grade: FK 7.81, Flesch 64.23; 342 words. The audio file matches the brief exactly with both tags in place.

## 6. prudentius-of-troyes, dates: PASS

"Died in 861, by the annals' entry for that year." BERT l.3526-3536: the entry for 861 records his death ("moritur"). Pertz l.150 agrees. The string makes no authorship claim, which is correct.

## 7. prudentius-of-troyes, keyWorks 1: PASS

The Waitz sentence is the same as in section 3 and rests on the same source.

## 8. prudentius-of-troyes, legacy.remembered 1: PASS, one MINOR

"The annals' notice of his death, which G. H. Pertz gives to Hincmar, his opponent in the predestination quarrel, calls him learned. It says he turned in bitterness into a fierce defender of Gottschalk's heresy." BERT l.3531-3534 gives "adprime litteris eruditus", "felle commotus" and "heresis defensor acerrimus". Pertz's attribution is at l.203-205. The sentences have 22 and 13 words. "His opponent" reads as Hincmar's role relative to Prudentius, and it is not misheard. MINOR: this is the first mention of Pertz in the `remembered` field, and it has no role. Suggested fix: "which G. H. Pertz, an editor of the annals, gives to Hincmar…". Gottschalk is also bare here, but that wording predates round 3.

## 9. prudentius-of-troyes, uncertain 1: PASS

"The annals' notice of his death says he first resisted him and then took his side." BERT l.3532-3534 says the same. It is accurate, and it no longer treats a disputed attribution as settled. Observation, not counted: the string's untouched sentences use a bare "Gottschalk" and a bare "Antonio" at their first mentions in `uncertain`. That wording predates round 3.

## 10. prudentius-of-troyes, uncertain 2: PASS

"Some comes through defenders who answered them, such as Nicolás Antonio." "Some" corrects the earlier overclaim "The rest". PL115 l.79379-79391 and 79618-79632 show Antonio answering the annals ("calumniose et inique ... Nec verum est Prudentium Gotescalcho obstitisse unquam"). "Them" points back to "Hincmar ... and the annals", which is correct.

## 11. prudentius-of-troyes, uncertain 4: PASS

"The annals' notice of his death calls him Galindo, surnamed Prudentius." BERT l.3530 reads "Galindo cognomento Prudentius", and "surnamed" renders "cognomento".

## 12. hincmar-of-reims and prudentius-of-troyes, records.json (four entries): PASS

- Prudentius quarrel claim, and the Annals 861 claim: each gives the notice to Hincmar on Pertz's authority (BERT l.203-205) and to an anonymous annalist on Antonio's (PL115 l.79267-79271, 79307, 79622-79623). All the cited lines say this. At l.79307 Antonio writes "anonymus idem Bertinianus auctor", and l.79622-79623 has "Bertinianus Anonymus, Hincmari metropolitae ... velificatus partibus".
- The contested side "The annals for 861 ..., Hincmar's by Pertz: yes" is accurate.
- The added parenthesis on the authorship contest, "Antonio's anonymous author is the one who carried the annals to 882", rests on PL115 l.79270-79271 ("auctoris fere aequalis, qui ad annum usque 882 res in Francia gestas persecutus est"). The line numbers are correct.

## 13. braulio-of-zaragoza, uncertain 5: PASS

"A note printed with Nicolás Antonio's notice says Gregorius Mayansius, in his Life of Antonio, denied it." PL80 l.52036-52040 and l.52007-52008 read "Gregorius Mayansius Siscarius: qui in Nicolai Antonii Vita, ... falso eam Praenotationem Braulioni tributam asserit". The note writer is the speaker, as the string says. The sentence has 18 words.

## 14. ildefonsus-of-toledo, legacy.traces 2: PASS

"Cixila, a later bishop of Toledo under Muslim rule, wrote a Life of him. He says Ildefonsus composed Masses, among them one to be sung in Mary's praise on her feast, which he counts as the seventh." For the identifier, the records cite the heading "A Cixilano ejusdem urbis episcopo edita" and Antonio's "sub Maurorum tyrannide". PL96 l.3870-3873 has "missam superscriptam, quae in ejus laude decantaretur, perfecit, quae est septima", on the feast of Mary. "He" now points to Cixila, and "Ildefonsus" removes the earlier ambiguity. The plural "Masses" rests on "quae est septima"; the records tag it Inferential-Thin, and that wording predates round 3. The sentences have 14 and 22 words.

## 15. julian-of-toledo, dates: PASS, one MINOR

- "Felix of Toledo says…" PL96 l.37355-37357 gives "annis decem ..., mense uno, diebus septem".
- "The notes of Cardinal Lorenzana's Toledo edition read this as 6 March 690, with his consecration on 29 January 680." PL96 l.37362-37373 gives "anno ... 690 ... consecratum fuisse anno 680, die 29 Januarii".
- "Nicolás Antonio, in his Bibliotheca Hispana vetus, has Quiricus dying in 681." The notice is headed "(Ex Antonio, Biblioth. vetus Hisp.)" (PL96 l.36013), and l.36887-36889 reads "post Quiricum, qui anno obiit 681".

MINOR: the next sentence, "He signed the councils of Toledo of 681, 683, 684 and 688", now follows a sentence whose subject is Antonio and whose object is Quiricus. Heard once, "He" can attach to Quiricus, and a council of 681 fits his dying that year. The wording predates round 3, but the longer Antonio sentence sits right before it. Suggested fix: "Julian signed the councils…". Observation, not counted: PL96 prints the editor as "Antonio Lorenza" (l.3640, 16518). The title "Cardinal" and the form "Lorenzana" are an outside identification, not held text. The card already used it in two `uncertain` strings, and earlier rounds accepted it there.

## 16. julian-of-toledo, uncertain 2: PASS

"That chronicle runs to 754, says Theodor Mommsen, who edits it, and the name is false." MGH11 l.16362-16363 reads "pervenientis ad a. 754 notae hodie sub nomine ficticio Isidori Pacensis", and the file header names Mommsen as editor. The witness is now named, and his role is given.

## 17. julian-of-toledo, uncertain 5: PASS

"Felix says he and the deacon Gudila wished to be, but God judged otherwise." The records quote Felix: "collegae sui Gudilanis levitae ... Sed quia aliter in superni numinis fuit judicio". Antonio's paraphrase at PL96 l.36873-36877 ("una cum Gudila diacono ... Avebant ambo sese addicere monasticae vitae") agrees. "The deacon" renders "levita".

## 18. beuno, legacy.traces 1: PASS

"A note in W. J. Rees's edition names eleven churches dedicated to him…" REES l.13458-13462 names eleven churches in the five counties. The file header and l.144 name the editor as W. J. Rees. "A note" is right for a first mention.

## 19. beuno, legacy.remembered 1: PASS

"The Latin Life of Saint Winefred, printed by W. J. Rees, makes Beuno her teacher…" The Life is in the same volume (REES l.9203-9372). "Printed by" correctly separates the editor from the Life.

## 20. README, Beuno line and audio line: PASS

"The note in W. J. Rees's edition" matches the card. The audio description ("`[warmly]` at the start of the last paragraph") matches both audio files, as checked by script in sections 1 and 5.

## Findings

No string fails the source check, and none needs a correction to its substance. No AI tells, narrator contrasts or beat lines were found. Every changed card sentence is 25 words or fewer. Both briefs pass the reading-level gate: Hincmar FK 6.50 / Flesch 74.88, Prudentius FK 7.81 / Flesch 64.23. Both match the figures in `R3_changes.md`, and both audio files match their briefs exactly.

Four MINOR points, all on clarity, none blocking:

- **R4-M1** (hincmar-of-reims, traces 3): Pertz has no role at his first mention in the field.
- **R4-M2** (prudentius-of-troyes, brief P2): "the annals" comes one paragraph before the brief says which annals they are.
- **R4-M3** (prudentius-of-troyes, remembered 1): Pertz has no role at his first mention in the field.
- **R4-M4** (julian-of-toledo, dates): "He signed the councils" can be heard as Quiricus. This wording predates round 3 but sits in a changed string.

Observations not counted against round 3: the bare "Gottschalk" and "Antonio" in Prudentius uncertain 1, and "Cardinal Lorenzana" as an outside identification of PL96's "Antonio Lorenza". These belong in the batch's open-gaps record if they are kept.

## Verdict

CLEAR. The round 3 strings are faithful to the vendored sources and read clearly, apart from four non-blocking MINOR clarity points (R4-M1 to R4-M4). Applying those points, or recording them as accepted, is the caller's decision under the cap rules.
