# Council profiles, era 3: review round 2, targeted recheck (2026-11-14)

**Scope.** What changed in commit `001eef53` under `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era3/`, set against `R1_review.md` and the author's answer `R1_changes.md`. The three councils are the same as in round 1: `second-council-of-constantinople-553`, `third-council-of-toledo-589`, `council-of-dvin-609`. Text that did not change was not reviewed again.

**Method.**
- Read the word diff of every brief, entry and `records.json` against `HEAD~1`, then read each changed brief in full for broken first mentions, ambiguous antecedents and lost sense.
- Checked every new quotation in its vendored file: Michael the Syrian IX (`michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.19002-19095, 6755-6769), Labourt (`labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` l.15582-15589, 15699-15719), the council's sentence on Vigilius's consent (`npnf214` l.23342-23354), Hefele's "without the assent of the Pope" (l.22876-22878), Evagrius on Vigilius's assent (`evagrius…walford1846.txt` l.9556-9557), John of Biclaro's "nostram catholicam fidem" (`john-biclaro-leander-pl72-lat_migne1878.txt` l.64853-64854), the booklet's doxology (`collectio-canonum…toledo-iii-lat_1808.txt` l.36969), Reccared's letter and Barmby's note (`npnf213` l.2245-2262), Gregory to Constantius and Letter I.25 (`npnf212` l.40140-40151, 31921-31922), Samuel of Ani in Brosset's note (`zakaria…brosset1876.txt` l.22666-22672), Brosset 1849 (`kartlis-tskhovreba…brosset1849.txt` l.9688-9697), Register XI.52 and its editors (`gregory-great_registrum…ewald-hartmann1895.txt` l.12138-12182), Barmby on Phocas (`npnf212` l.23779-23781), Issaverdens (`issaverdens…1875.txt` header, l.3650-3654, 3686-3690, 3712-3718), Ormanian on Mekhitar (`ormanian_church-of-armenia_gregory1912.txt` l.4468-4512), and Stephen of Taron (`stepanos-taron…gelzer-burckhardt1907.txt` l.3100-3105).
- Checked the new people verdicts (Pelagius II, Euphemius of Toledo) against the Who scans, and the new tradition id `syriac-orthodox-west-syriac-christianity` against `cic-website/data/world-census.json`.
- Counted words, ran `engine.m1.gates.grade_text`, counted sentence lengths, and compared each audio script with its brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph.
- No model calls, no network calls, no paid calls. No draft was edited.

## Gates

| Council | Words | FK | FRE | Audio = brief | Sentences over 25 words |
|---|---|---|---|---|---|
| second-council-of-constantinople-553 | 400 | 8.15 | 60.22 | yes | none (longest 24) |
| third-council-of-toledo-589 | 400 | 7.01 | 68.71 | yes | none |
| council-of-dvin-609 | 371 | 7.67 | 61.77 | yes | none (longest 24) |

All three pass: 400 words or fewer, FK 10 or under, FRE 60 or over. The scores match `R1_changes.md`. Constantinople and Toledo are at the word cap. Constantinople stays just over the reading-ease floor, so any further brief change there needs a rescore. Each audio script carries only the two tags, in the right places.

## Round 1 findings

| Finding | Severity (R1) | Status | Evidence |
|---|---|---|---|
| CON-1 | substantial | RESOLVED | Brief: "Jérôme Labourt, a French historian of the Persian church, reads the creed of its synod of 585 as an answer to the council's backers." Labourt: "Le patriarche argumente contre tous les partisans byzantins ou persans du cinquième concile œcuménique" (l.15587-15589). The church is now Affected. The note, `outcome` and `record` say the Theodore canon names no council and that Labourt aims it at Henana's followers (l.15715-15717). Labourt is in `record` and `sources`. The contested claim is tagged Inferential-Thin, which fits a link that rests on one modern reading. |
| CON-2 | substantial | RESOLVED | The false absent detail is gone. Michael the Syrian is in `record`, `sources.writtenLater`, `attended`, `outcome`, `uncertain` and both contested claims. Each claim matches Chabot: the 26th year of Justinian, 864 of the Greeks (l.19002-19004); three patriarchs, Vigilius in the city but absent "sous prétexte de ne pas être méprisé en étant compté avec ces trois; ce qui est le comble de l'arrogance" (l.19066-19075); the anathema on Origen "qu'avait porté Justinianus lui-même", and on Theodore, Theodoret and the letter of Ibas (l.19089-19094). Michael gives no count ("beaucoup de métropolitains", l.19078-19079), so `attended[0]`'s "No ancient witness held gives a count" still holds. `syriac-orthodox-west-syriac-christianity` is in the census (era 3, 451-636). |
| CON-3 | minor | RESOLVED | No quotation marks: "Vigilius was in the city, but refused the emperor's repeated calls to come." The claim is now told flat. It rests on the digest's "In vain we sent several commands to him" (l.23128-23130) and on the council's sentence, "we besought his reverence to fulfil his written promises" (l.23351-23352), with Evagrius and Michael. The records tag it Widely Accepted with Victor as the dissent, so a flat telling is fair. |
| CON-4 | minor | RESOLVED | Widely Accepted; Victor of Tunnuna "alone" lists Vigilius as present. |
| CON-5 | minor | RESOLVED | "Vigilius died in Sicily, going home." |
| CON-6 | minor | RESOLVED | "The council's final sentence curses the Chapters: 'We therefore anathematize the Three Chapters.'" "Curses" glosses the new word before it is heard. "Manuscript" is used in both places. |
| CON-7 | minor | RESOLVED; the Theodelinda part left, with the reason accepted | "Gregory the Great of Rome said he honoured a fifth council. But writing to Milan …" The listener no longer hears Gregory's Milan line as Rome's whole verdict. The cap reason for leaving out the queen holds, and the entry's `outcome` and the new claim (l.40141-40144) carry her. See R2-5 on "a fifth council". |
| CON-8 | minor | RESOLVED | "The council's acts survive, the record of the side that won, and are told here from English extracts." "Library" is gone from all three briefs. |
| CON-9 | minor | RESOLVED | `calledBy` gives Hefele ("without the assent of the Pope", l.22877-22878) and Evagrius (l.9556-9557) verbatim. The new contested claim adds the sentence's "he gave his consent in writing to be present at the Council" (l.23345-23346). It is tagged Contested. |
| CON-10 | minor | PARTLY | `informalName` is "The Fifth Council". `uncertain[3]` now says Justinian wrote and sent his quaestor. Pelagius II is added as LISTED, which matches the era 3 scan. Gregory the Great is left out under the new TOL-6 rule, but that rule's own terms take him in (R2-4). |
| TOL-1 | minor | RESOLVED | The Latin is quoted as Latin, with the English after it outside the marks: "nostram catholicam fidem" (PL72 l.64853-64854) and "gloria Patri per Filium in Spiritu Sancto" (acts l.36969). "not many days", "the faith and communion that came from Arius" and "all the elders of the Goths" have no marks. |
| TOL-2 | minor | RESOLVED | `decided[0]`, `record`, `uncertain[3]` and the contested claim now apply Dalton to "the king's speech at the council". The claim quotes him verbatim. |
| TOL-3 | minor | RESOLVED | "Masona, bishop of Mérida"; "Eutropius, abbot of Servitanum". |
| TOL-4 | minor | RESOLVED | "The signed list has sixty-two bishops in person and five who signed through deputies … Two places in the printed text are damaged." |
| TOL-5 | minor | RESOLVED | The letter is in `record` (participant), `sources.fromThoseThere` and a claim. Barmby's note is quoted verbatim: "The genuineness of this letter is considered doubtful" (`npnf213` l.2251-2252). The letter is in Book IX as Epistle LXI (l.2248-2249), so "Book IX, no. 61" is right. |
| TOL-6 | minor | RESOLVED for Toledo | The rule is set out and applied: Gregory the Great is off Toledo's click, and Euphemius is on as NOT SCORED. He is in no Who scan. He signs second as "ecclesiae catholicae Toletanae metropolitanus episcopus" (acts l.38049-38053). "Bishop of the royal city" is true; "metropolitan of Toledo" would be closer to his own subscription, but this is not a finding. For Constantinople, see R2-4. |
| TOL-7 | minor | RESOLVED | "in twenty-three articles" in the brief; the entry and records say the twenty-third is the closing subscription. |
| DVN-1 | substantial | RESOLVED, with one note to correct (R2-3) | Brief: "Kyrion's own words reach us only through James Issaverdens, a priest of the Armenian Catholic monastery of San Lazzaro in Venice, writing in 1875. He praises Kyrion's learning and piety." Issaverdens has "a most learned tiod [and] pious man" (l.3653-3654). The title page has "Rd. Dr. James Issaverdens … Academy of St. Lazaro" (header). Ormanian places Mekhitar's house among the Catholic cases, "had to yield to the demands of the Roman Curia" (l.4482-4493). The wrong-side sentence is gone, and `record` gives his side. Every "He" in paragraph 4 falls on Issaverdens. |
| DVN-2 | substantial | RESOLVED in the brief; the entry overreaches (R2-1) | Brief: "Stephen names no council and gives no year" closes paragraph 1. Paragraph 3 says "Of the writers drawn on here, only modern ones tell of a synod at Dvin." That is true of the held writers. Sebeos tells only the debate before the king. Samuel of Ani, in Brosset's note, says only that the Iberians "se séparèrent" after adopting Chalcedon (l.22668-22669). "Then called" is now "called". |
| DVN-3 | substantial | RESOLVED, with a kind to fix (R2-2) | `uncertain[4]`, the contested claim and the new `record` row match the editors: 601 (l.12142); "Utrum in Hiberniam an in Hiberiam Ponticam an in Hispaniam … Equidem puto de Hiberia Pontica agi" (l.12165-12170); Kyrion not named. The reason for keeping the letter out of the brief holds. It concerns receiving Nestorians (l.12138-12140), not the break. |
| DVN-4 | minor | RESOLVED | Teaser and `shortName`: "Dvin, between 596 and 609". The brief adds Stephen and Issaverdens setting Abraham's quarrel under Maurice. Stephen has "Der Kaiser Maurikios aber setzte …" (l.3103-3105). Issaverdens has Kyrion complain "to the Emperor Maurice" (l.3714-3716). `datesNote` gives Issaverdens's damaged year, "A. D. 59 ^j" (l.3690), and Barmby's "November, a.d. 602" (`npnf212` l.23780-23781). |
| DVN-5 | minor | RESOLVED | "Kyrion came to doubt what Stephen calls the orthodox faith." |
| DVN-6 | minor | RESOLVED | "No writer names the bishops or counts them"; "No other writer tells of that meeting"; "No record of the council survives among the books this account draws on". |
| DVN-7 | minor | RESOLVED | The brief closes on Ormanian's "became part of the Greek Church" (verbatim in round 1). `outcome` gives Brosset's 580 and Chamich. Brosset adds the 580 line ("Je me hâte d'ajouter") and then writes "Tous ces témoignages sont tirés de Tchamitch (… p. 225, 490 sqq.)" (l.9695-9697). Reading the 580 statement as drawn from Chamich is fair, and it was round 1's own suggestion. |
| DVN-8 | minor | RESOLVED | `informalName` is left out. |
| DVN-9 | minor | RESOLVED | Samuel of Ani is in `record` (later narrative, Armenian side) and in a claim. "Les Ibériens, ayant adopté l'hérésie de Chalcédoine, se séparèrent" and "entièrement fausse" are verbatim (l.22668-22670). He is LISTED in the supplement scan. Writers who only report are off the click under the TOL-6 rule, which is consistent. |

All five substantial findings are resolved.

## New findings

**R2-1. Substantial (Dvin entry; false absence; C1, item 7).** The new `uncertain[0]` reads: "The synod at Dvin is told only by modern writers: Issaverdens in 1875, Brosset in 1876 and Ormanian in 1912." The brief scopes this ("Of the writers drawn on here"), but the entry does not. Brosset's held note gives two medieval Armenian writers as his authority for the council: "v. Kiracos tr. fr. p. 24, Oukhtanès, tr. fr. p.284 sqq. La sécession eut lieu lors du concile de Dovin, tenu en 596" (`zakaria…brosset1876.txt` l.22669-22671). Kirakos and Ukhtanes are not held, but they are named in a held line as witnesses to the council. Told without scope, the sentence says no older writer tells of the synod, and the Library's own evidence says otherwise. This is the false-absence fault of CON-2 in round 1. Fix: "Among the writers held here, only modern ones tell of the synod at Dvin: Issaverdens in 1875, Brosset in 1876 and Ormanian in 1912. Brosset cites the medieval Armenian historians Kirakos and Ukhtanes for it, which are not held." Add the Kirakos and Ukhtanes citation to the date's contested claim in `records.json`. The brief need not change, so no rescore is needed.

**R2-2. Minor (Dvin `record`; witness kind).** Gregory's letter to Quiricus (Register XI.52) is given `"kind": "later narrative"`. It is not a history. Under the 609 date that gives the profile its id, it is also earlier than the council. The other Gregory letters in era 3 are "later narrative" because they were written after their councils. That is not true here. Its note also says the letter "shows Rome in touch with a Catholic bishop of Iberia in Kyrion's time". That is the profile's own inference, and the editors do not draw it. Fix: take the letter out of `record`, since it is not a witness to the council, and keep it in `uncertain[4]`, the contested claim and `sources`. If it stays, say in the note that it predates Ormanian's date and bears on the council only through the census's identification.

**R2-3. Minor (Dvin `record` and `records.json`; wording against the source).** The new Issaverdens note says his house was "founded, Ormanian says, under the auspices of Catholicism; his book is a sketch for visitors". The records claim repeats the first part: "Mekhitar founded his house at San Lazzaro under the auspices of Catholicism".
- In Ormanian, "under the auspices of Catholicism" belongs to Mekhitar's earlier attempt in the Morea in 1712, which he gave up. For San Lazzaro (1717) Ormanian says "Mekhitar had to yield to the demands of the Roman Curia" (l.4486-4495). The substance, a Catholic house, stands. The phrase is attached to the wrong foundation.
- "For visitors" rests only on the Library thread's content note in the file header (l.8), not on any line of the book. The records claim cites "file header l.8" as a witness. The title page says only "being a sketch of its geography, history, church and literature".

Fix: "a Mekhitarist house which, Ormanian says, had to yield to the demands of the Roman Curia"; drop "for visitors", or cite a line of the book that says so; cite Ormanian l.4492-4495 in the claim; and remove the header as a witness.

**R2-4. Minor (Constantinople `people`; the TOL-6 rule applied).** `R1_changes.md` sets the rule: the Who click lists "those who acted on the council's decisions (summoned, exiled, confirmed or pressed them)". Under it, Pelagius II is added because he "pressed the Istrian bishops". Gregory the Great did the same. Barmby writes of "his ineffectual attempts, though apparently supported by the Emperor, to bring the Istrian bishops to submission in the matter of the 'Three Chapters'" (`npnf212` l.23069-23071). He also says Gregory "in vain endeavoured … to bring back the Istrian bishops to conformity" (l.22460-22462). Leaving Gregory off breaks the profile's own rule. Fix: add Gregory the Great (WHO, `gregory-the-great`) with "Not present; pressed the Istrian bishops to accept the council, and defended it to Milan". The alternative is to narrow the rule, but then Pelagius II comes off too.

**R2-5. Minor (Constantinople brief; wording).** "Gregory the Great of Rome said he honoured a fifth council." Gregory writes "The fifth council also I equally venerate" (`npnf212` l.31921-31922). He means this council. With "a", a listener can hear some other fifth council, and that weakens the "But …" that follows. Fix: "said he honoured the fifth council". The word count is unchanged; rescore.

No other new quotation was found outside its file. The new text has no paraphrase or translation in quotation marks, no first mention without a role, no sentence over 25 words, no AI tells, no "not X but Y" contrasts and no project vocabulary ("Library", "held") in the briefs. The Dvin brief says "drawn on" twice in two sentences: "among the books this account draws on" and "Of the writers drawn on here". This is clumsy but not a finding.

## Counts (new findings)

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| second-council-of-constantinople-553 | 0 | 0 | 2 (R2-4, R2-5) |
| third-council-of-toledo-589 | 0 | 0 | 0 |
| council-of-dvin-609 | 0 | 1 (R2-1) | 2 (R2-2, R2-3) |

## Verdict

| Council | Verdict |
|---|---|
| second-council-of-constantinople-553 | CLEARS (R2-4 and R2-5 recommended) |
| third-council-of-toledo-589 | CLEARS |
| council-of-dvin-609 | NEEDS FIX (R2-1; R2-2 and R2-3 with it) |

This is the second review file on each of these documents. The Dvin fixes are in the entry and `records.json` only. They need a recheck of those lines, with no rescore and no new audio. If R2-5 is taken, Constantinople needs a rescore and a regenerated audio script.
