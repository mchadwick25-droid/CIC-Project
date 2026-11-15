## Council profiles, era 7 batch 2, round 2: Part B (Council of Trent 1545-1563)

**Council.** `council-of-trent`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/council-of-trent.brief.txt`, `audio/council-of-trent.audio.txt`, `council-of-trent.entry.json`, `records.json` key `council-of-trent` (equal to `working/records_council-of-trent.json`, checked by script; 144 claims, 10 contested claims, 9 absent details), and the README line "Council of Trent (about 2:30)". The scope is `git diff f6c9d034 HEAD` for these files, against round 1 Part B (`R1_review.md` l.134-282) and `R1_changes.md` Part B (l.75-150).
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the cap). `grade_text`: FK 7.61, Flesch 61.99. 32 sentences. Longest sentence 22 words ("The council ruled that Scripture and the unwritten traditions, ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff` after stripping the two tags.
**Entry.** No sentence in any entry string is over 25 words (script check). The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file was edited. No model, network or paid calls were made.

Abbreviations as in round 1 (W, S, P1, P2, P3, C1, BOC, ABD, GIUS). Also: BENSOW = `bensow_svenska-kyrkans-bekannelseskrifter-swe_bensow1912.txt`; REUSCH = `reusch_indices-librorum-prohibitorum-sechzehnten-jahrhunderts-deu-lat_1886.txt`.

## Verdict: REVISE (no blocking, one substantial, six minor)

The blocking point B-B1 is closed. The false absence is gone from every profile string. The Smalcald Articles, the Formula of Concord and Pallavicino's account of the envoys are now in the entry and records, each with its own witness and year. Every new quote is verbatim. The new, narrower absence (no Württemberg or Saxon confession held) survives a wide search. Sarpi and Pallavicino are each given as theirs in every changed string.

The one substantial point is the new Formula of Concord sentence in the brief. It says the Formula rejected "the council's decree on good works". The acts have no decree of that name: the Formula's target is the Decree on Justification (canon XXIV, by Jacobs's note). The sentence also gives the condemned side no words of its own, which was the reason for B-S1. The Formula's own words fit in two more words (B2-S1).

The six minor findings are:
- in `uncertain[7]`, Pallavicino's pope is turned into "the cardinals" as the ones who approved, and "held back" overstates what the officials did;
- the records' absent detail still says both confessions were "handed in", against the fixer's own correction;
- the new Book of Concord `record` witness reads as if Luther wrote the Formula;
- the README line now runs the Formula of Concord into "four decrees";
- two small length cuts (3 words and 1 word) that keep every witness tag.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| B-B1 | CLOSED, with a new point | Entry `issue[6]`, `issue[7]`, `uncertain[11]`, `outcome` (Lutherans), `traditions` (Lutheran note), `record[6]`, `people` (Maurice), the new BOC `record` and source; records `absent_details[1]` note and claims 137-140. Checked in context: BOC l.15748-15792 (Smalcald title "WRITTEN BY DR. MARTIN LUTHER IN THE YEAR MDXXXVII"; "a truly free Christian Council", l.15784; "the Romish court is so dreadfully afraid of a free Christian Council", l.15791-15792); W l.11719-11738, 11976-11990 (Mantua 1537, "the city of Mantua was refused us", Vicenza, Trent); BOC l.30993-30999 ("the decree of the Council of Trent, ... should by right be rejected, viz. that our good works support salvation"), l.31038 (Jacobs's "Sess. vi., Can. xxiv."), l.27925 ("Bergen May 29th, 1577", closing "this Epitome"); P2 l.22382-22430 (Württemberg envoys in the morning, "la lor Confessione in mano del Segretario"; the Saxons "verso la sera", "Oratori di Maurizio Elettor di Sassonia"; "à cinque capi"), l.22530-22540 (the fourth head, "innanzi à tutto"). The entry's correction that only the Württemberg confession is said to be handed in is right; the records' `detail` line was left stale (B2-M2). The brief sentence is B2-S1. |
| B-S1 | CLOSED, with a new point | The brief line is in place and the offsetting cuts are applied. The residence sentence now reads "bound bishops to reside, grounding their duties in divine precept, but did not call residence divine right", which matches W l.19388-19422 ("by divine precept, enjoined on all to whom the cure of souls is committed"; "obliged to personal residence in their own church or diocese"). The new Formula line misnames the decree and carries no Lutheran words (B2-S1). |
| B-S2 | CLOSED | `decided[10]` and claim 67 now follow W l.19909-19938: the poor chosen first, then the bishop assigns some, keeps the rest, and "shall supply the place of those who have been withdrawn by others, that so this college may be a perpetual seminary". The fixer's correction of the review's "fills their places" is right. |
| B-S3 | CLOSED, with a new point | Contested claim 5 and claim 141 are in place and cite P3 l.57848-57867, 58030-58039. The entry's new wording has two small slips against those lines (B2-M1). |
| B-S4 | CLOSED | Claims 93, 106, 107, 111 and 132 are "modern reconstruction". The source title, the new `writtenLater` row and the `record[0]` note are in place (W l.24415, "From Le Plat's edition ... 1779"). |
| B-M1 | CLOSED | "In a letter Jules Bonnet's edition dates to 1545" (C1 l.120, 20043, 20050). |
| B-M2 | CLOSED | "Two rival histories tell the debates." |
| B-M3 | CLOSED | "Abdisho, a patriarch from Assyria" in the brief; the numeral is also gone from `traditions`, `record[2]` and the source author. `people` keeps the census name. |
| B-M4 | CLOSED | "In 1562 the fathers split ..." |
| B-M5 | CLOSED | Teaser: "for a time at Bologna" (W l.14722, 14779-14783). |
| B-M6 | CLOSED | Claim 53 note: "OCR 'deterred' and '2.2.' (S l.8790)". S l.8788-8790 re-read. |
| B-M7 | CLOSED | `uncertain[2]` and contested claim 9 now say the two agree "if Sarpi's 25 leaves the legates out". S l.18406 and P1 l.35131-35135 as in round 1. The conditional is fairer than round 1's "plainer reading". |
| B-M8 | CLOSED | `attended[2]` and claims 142-143: W l.7182-7184 ("one hundred and six bishops, four mitred abbots, and four generals"); GIUS l.3650. Giussano's figure tagged Inferential-Thin as a round number. |
| B-M9 | CLOSED, with a new point | The README line now names Calvin, Jewel and the Saxon envoys "as Sarpi gives them". The added Formula clause makes the list misread (B2-M4). |
| B-M10 | CLOSED | `record[2]` kind "participant", with "read at the session of 17 September 1562 (Sarpi, Pallavicino)"; source moved to `fromThoseThere`; claims 123-126 "participant". |
| Sarpi label | CLOSED | Brief: "The Venetian friar Paolo Sarpi was hostile to the papal court." Rests on his own frame against the "exorbitant power" of the See of Rome (S l.8826-8836) and "Father Paul the Venetian, of the Order of the Servi" (S l.677-678). Pallavicino stays "The Jesuit ... wrote to refute him" (P1 l.25-33). |

## New findings

### Blocking

None.

### Substantial

**B2-S1. Substantial (the new Formula of Concord sentence misnames the decree it answers and gives the condemned side no words of its own).**

Location: brief, paragraph 5: "In 1577 the Lutheran Formula of Concord rejected the council's decree on good works."

- The acts have no "decree on good works". The decree in question is titled "DECREE ON JUSTIFICATION" (W l.12960). Its canon XXIV condemns anyone who says "the justice received is not preserved and also increased before God through good works" (W l.13781-13785). Jacobs's footnote ties the Formula's rejection to "Sess. vi., Can. xxiv." (BOC l.31038). A listener hearing "the council's decree on good works" will take it as a separate decree.
- What the Formula rejects is a teaching it reads in that decree: "the decree of the Council of Trent ... viz. that our good works support salvation" (BOC l.30994-30999). The Swedish text agrees independently: "Tridentinska mötets beslut ... nämligen att våra goda gärningar bevara saligheten" (BENSOW l.26802-26807).
- B-S1 asked for the condemned party in its own words (pattern rule 3, C3). The narrator's paraphrase gives none. The Formula's own clause fits in two more words. The paragraph's subject is already the council, so "the decree" is clear.
- Fix, brief paragraph 5: `In 1577 the Lutheran Formula of Concord rejected the decree "that our good works support salvation."` (16 words, +2).
- Same wording in the entry, fix to match: `traditions` Lutheran note, `The Formula of Concord of 1577 rejects 'the decree of the Council of Trent' on good works.` becomes `The Formula of Concord of 1577 rejects 'the decree of the Council of Trent' that 'our good works support salvation'.` (19 words).
- The year holds. The only dated line is the Epitome's "Bergen May 29th, 1577" (BOC l.27925). Bensow says the Epitome and the Solid Declaration were finished together at Bergen as one book and then signed (BENSOW l.31604-31617). So "In 1577" for the Formula as a whole rests on two held lines. The entry's "Its first part is signed at Bergen, 29 May 1577" is exact and should stay.
- With the length cuts below, the brief is 398 words (scratch copy `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/trent_r2_all.txt`). Regenerate the audio from the fixed brief.

### Minor

**B2-M1. Minor (a fix in `uncertain[7]` moves Pallavicino's act from the pope to the cardinals, and "held back" overstates the officials).**

Location: entry `uncertain[7]`: "Both historians say some in Rome first held back from confirming outright. ... The cardinals then approved by common consent."
- Pallavicino's subject is Pius IV: "addomandate secondo il rito le sentenze de' cardinali, di comune consentimento l'approvò e 'l confermò per Bolla da tutti loro segnata" (P3 l.58034-58040). The pope asked the cardinals' votes, then approved and confirmed by common consent.
- The officials did not hold back. They "disconsigliarono il papa dell'assoluta confermazione" (P3 l.57848-57850), advised the pope against it. Sarpi's eight cardinals "were almost all of opinions that it was fit they should be moderated before the Confirmation" (S l.70324-70326). Both are advice against confirming outright.
- Fix: `Both historians say some in Rome first argued against confirming outright.` and `In the consistory, he says, the pope asked the cardinals' votes and confirmed by common consent.` (11 and 16 words).

**B2-M2. Minor (a records line left stale by the fixer's own correction).**

Location: records `absent_details[1]` `detail`: "The Württemberg and Saxon confessions handed in at Trent, 1551-52".
- The fixer corrected the entry because "P2 l.22388-22390 attests only the Württemberg confession handed in; no read line has the Saxons hand one in". Sarpi's lines say the same: the Saxon speech was "presented ... in Writing" (S l.36653-36654), and the second embassy "were to tender the Confession of their Doctrine", in the future (S l.36658-36660).
- Fix: `"detail": "The Württemberg Confession handed in at Trent in 1552, and any Saxon confession"`.

**B2-M3. Minor (a witness string that reads as if Luther wrote the Formula).**

Location: entry, new `record` item, `witness`: "Martin Luther, Smalcald Articles (1537), and the Formula of Concord (1577), in Jacobs's English Book of Concord". Luther died before Trent's first period ended. The Formula is not his.
- Fix: `"witness": "Martin Luther's Smalcald Articles (1537), and the Lutherans' Formula of Concord (1577), in Jacobs's English Book of Concord"`.

**B2-M4. Minor (README list misreads).**

Location: README, "Council of Trent (about 2:30)": "... the Protestant refusal, in Calvin's and Jewel's own words and the Saxon envoys' as Sarpi gives them, with the Lutherans' later answer in the Formula of Concord, four decrees, ..."
- The Formula clause runs straight into "four decrees", so it reads as part of the refusal list. In the brief it sits with the decrees it answers.
- Fix: `The brief keeps only the closing scene, the calling, the Protestant refusal (Calvin's and Jewel's own words, the Saxon envoys' as Sarpi gives them), four decrees with the Lutherans' later answer in the Formula of Concord, the two disputes the historians fight over, and the reach of the close.`
- The length "about 2:30" stays true after the cuts below (398 words, 2:29).

**B2-M5 and B2-M6.** Two small length cuts. See the Length test.

## Length test

The brief runs 400 words, the cap. I tested every sentence. The council ran eighteen years. The brief carries one scene, the calling, three refusing voices, four decrees with the Lutheran answer, the two disputes the historians fight over, and the reach of the close. Each carries a decision, a side or a source. Every attribution is a witness tag. These include "wrote Servanzio, as Waterworth quotes his diary", "Jules Bonnet's edition dates", "by Sarpi's count" and "Each historian counts the votes his own way", which keeps the residence vote with both historians. Two sentences carry a few words of slack:

| # | Sentence | Verdict |
|---|---|---|
| 1-4 | Lorraine, the acclamations, the anathemas, Servanzio | Keep. Scene, the acts, the condemnation, a witness chain. |
| 5-9 | The acts in Waterworth; two histories; Sarpi; Pallavicino | Keep. Sources and their sides. |
| 10-11 | "Pope Paul III called the council in 1542. His bull chose Trent because ..." | Trim 1 word (B2-M6). |
| 12 | Opening, 25 prelates by Sarpi's count | Keep. A count with its witness. |
| 13-14 | Calvin | Keep. |
| 15-16 | "In 1552 envoys from Saxony came. Before anything else, Sarpi says, they asked ..." | Trim 3 words (B2-M5). |
| 17 | Jewel | Keep. |
| 18-21 | Four decrees and the Formula | Keep; B2-S1 adds 2 words. |
| 22-27 | Bologna and residence, each historian as his own | Keep. |
| 28-30 | 255 and 168, the confirmation, Abdisho | Keep. |
| 31-32 | The two rival judgments | Keep. |

**B2-M5. Minor (length, 3 words).** `Before anything else, Sarpi says, they asked the council to affirm that it stood above the pope.` becomes `Sarpi says they first asked the council to affirm it stood above the pope.` (17 to 14 words). "First" is Sarpi's own word: "prayeth the Assembly, That they would first repeat, approve, and ratifie the Article of the Superiority of the Council above the Pope" (S l.36638-36640). The witness tag stays.

**B2-M6. Minor (length, 1 word).** `Pope Paul III called the council in 1542. His bull chose Trent because the Germans "wished for the city of Trent."` becomes `Pope Paul III's bull of 1542 called the council to Trent, because the Germans "wished for the city of Trent."` (21 to 20 words). The bull stays as the witness to the reason (W l.11976-11986, "we have chosen the city of Trent").

**Counts.**
- Before: 400 words, 2:30 at 160 wpm. FK 7.61, Flesch 61.99. Longest sentence 22 words.
- With B2-S1 alone: 402 words, over the cap. FK 7.66, Flesch 61.74.
- With B2-S1, B2-M5 and B2-M6: 398 words, 2:29 at 160 wpm. FK 7.74, Flesch 61.63. Longest sentence 22 words. No sentence over 25. Scratch copy: `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/trent_r2_all.txt`.
- I found no Substantial length cut. The README's "about 2:30" stays true at 398 words. Its list wording needs B2-M4.

## Verified

- **Every new quote, verbatim.** "the Romish court is so dreadfully afraid of a free Christian Council" (BOC l.15791-15792); "a truly free Christian Council" (l.15784); "the decree of the Council of Trent ... should by right be rejected" and "that our good works support salvation" (l.30994-30999, ellipsis over "and whatever elsewhere is set forth in the same sense"); "that so this college may be a perpetual seminary of ministers of God" (W l.19937-19938); "two hundred and fifty Bishops" (GIUS l.3650); "with all the Prelates, in number 25" (S l.18406); "advice and assent" (W l.24172-24175).
- **Translations.** "la lor Confessione in mano del Segretario" is rendered "handed their Confession to the secretary" (P2 l.22388-22390). "disconsigliarono il papa dell'assoluta confermazione ... per le disposizioni onde a lei diminuiva e l'entrata, e l'autorità" is rendered "advised the pope against an absolute confirmation, since it cut the court's revenue and authority" (claim 141; P3 l.57848-57852). "s'opposero" is rendered "opposed them" (l.57862). All faithful; nothing added.
- **Smalcald dating.** "which the edition dates to 1537" is exact: the date is the edition's heading (BOC l.15762-15764). The preface's "convoked a Council last year to assemble at Mantua" (l.15767) fits the bull's Mantua date of 23 May 1537 (W l.11722-11723). "Before Trent met" holds.
- **Pallavicino on the Saxons.** The Saxons "ripetevano le medesime colorite ragioni onde i Protestanti havevan sempre rigettato ogni Concilio" (P2 l.22416-22419). This supports the `traditions` note "refused its terms, by Sarpi's and Pallavicino's accounts". "Colorite" is his hostile word and is not given as fact.
- **Sarpi and Pallavicino, each as his own, in every changed string.** Brief: "by Sarpi's count", "Sarpi says" (twice), "Pallavicino cites", "Each historian counts", "Sarpi judged", "Pallavicino writes". Entry `issue[7]`, `uncertain[2]`, `uncertain[7]`, `uncertain[11]`, `record[6]`, contested claims 5 and 9: each claim carries its historian. Waterworth's leaning to Pallavicino is given as his (`uncertain[0]`).
- **Residence decree.** W l.19384-19422, as above. "Assistunt" footnote (l.19413-19414) unchanged.
- **The bull of 1542.** Claim 139 against W l.11719-11738 (Mantua "on the tenth of the calends of June, in the year 1537"; "the city of Mantua was refused us") and l.11976-11986 (Vicenza; "they (the Germans) wished for the city of Trent").
- **Brief and entry agree.** The brief's Formula, Saxon, Calvin, Jewel, Bologna and residence lines match the entry and records. Audio equals brief plus two tags.

## Searches run

- **Württemberg and Saxon confessions (the new absence in `uncertain[11]` and `absent_details[1]`).** Over all `cic/texts`: `confessio\s*(virt|wirt|wurt|würt|vuirt|vvirt)|(wirt|wurt|würt|virt)[a-z]*\s+confession|w(ü|ue|u)rttembergische[sn]?\s+bekenntnis|wirtembergische[sn]?\s+bekenntnis|confessio\s+saxonica|saxon\s+confession|repetitio\s+(augustanae\s+)?confessionis|confessio\s+doctrinae\s+saxonicarum|s(ä|ae)chsische[sn]?\s+(konfession|confession|bekenntnis)|confession\s+(de\s+)?(saxe|wurtemberg|wirtemberg)|confessione\s+(sassonica|virtemberg)`, case-insensitive. Hits: six false hits on "virtutis/virtute confessionis" (Abelard, Dunstan, Gérard de Frachet, Origen, PL 11, Étienne de Bourbon), and REUSCH l.16571-16573, the Index's titles "(Confeflsio Sazonica.)" and "(Confessio Wirtembergensis.)". Those are mentions, not the texts. File names with `melanch|brenz|brentz|wirtemb|wurtt|wuertt|saxon|sachs` give no confession of 1551-52. The absence holds.
- **Sarpi on a confession handed in.** `conf[eſ][sſ]` in S l.35900-36900: only l.36660, "were to tender the Confession of their Doctrine" (future). Hence B2-M2.
- **The Formula's date.** `1577|1580|MDLXXVII|MDLXXX` in BOC: only the header (l.2, 8) and l.27925. `signing|subscri|bergen|torgau` in BOC: the Preface's Torgau "in the year '76" (l.648) and its seals (l.1026), with no year for the Solid Declaration. Over all `cic/texts`, `formula\s+(of\s+)?concord|concordiae|konkordieformel|concordienformel|solida\s+declaratio`: 19 files. Among them, BENSOW l.31604-31617 (Bergen, epitome with solida declaratio, signed) and `arndt_true-christianity_boehm-schaeffer1868.txt` l.318, 628 ("published in 1580"). So "In 1577" holds on BOC l.27925 with BENSOW.
- **The Formula's target in the acts.** `CANON\s+XXIV|preserved\s+and\s+also\s+increased|on\s+justification` in W: "DECREE ON JUSTIFICATION" (l.12960), canon XXIV (l.13781-13785). No "decree on good works" title. Hence B2-S1.
- **Trent in the Formula, independently.** `trident|tridentin` in BENSOW: l.26805, "Tridentinska mötets beslut", the same passage.

## Counts

Blocking 0, Substantial 1, Minor 6.
