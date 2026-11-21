# Card check: Ambrose of Milan

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. I wrote neither the card nor the brief. Read: `ambrose-of-milan.brief.txt` (and `brief.v1.txt`), `ambrose-of-milan.card.json`, `Card_Edits.md`, the census entry `ambrose-of-milan` (no card), and each cited line in its file. New card: every field was checked against its evidence and against the entry's `sourcing`, `voices`, `legacy`, `why`, `floorNote`, `relationsSummary`, `dates` and `placeLabel`. The validator was not run.

**Verdict: FIX** (four changes below).

## 1. Each field against its evidence

Re-read and confirmed: AMB 909-932 (Trèves, probably born there; 333 or 340, the latter most accepted; governor of Liguria and Aemilia about 370); SOC 14243 (the note's "born in 333"); AMB 959-966 (questionable expedients; 7 December 374); PAUL 3322-3328 (a Catholic bishop, the eighth day); AMB 1116-1122 (Good Friday night, 4 to 5 April 397; the rite); PAUL 5757-5782 (Elias; the Easter vigil; the infants and the star); PAUL 3622-3625; AMB 1067-1068, 1082-1084; AMB 1844-1855 and 735-745 (On the Duties, 391 to 392); CONF 13717-13720 (the Te Deum note), 13748-13753, 14346-14363; AUGP 13126-13134; POSS 3765-3775, 3789-3826, 5816-5822; PAUL 7-8, 1171-1177; PAUL 3143-3146, 3197-3200; RUF 30228-30238, 30562-30576; AMB 942-953, 41446-41449, 700-707, 1463-1479; THDT 16506-16530; SOC 42152-42206; CD 11209-11218; PAUL 4276-4290, 4356-4372. Every quoted span in the card's prose (Theodoret's line, Castulus, the boy emperor, Calligonus, the tyrant question, the synagogue) stands verbatim in its file.

One statement misreports its source (FIX 1). `uncertain[4]` says the law of 23 January 386 threatens as authors of sedition "any who think that right theirs alone". The law (`theodosianus-16_mommsen-meyer1905.txt` 83735-83737) threatens those who think the right theirs alone only if they attempt a disturbance against the order ("si turbulentum quippiam contra nostrae tranquillitatis praeceptum faciendum esse temptaverint").

No conflict with the entry's fields. `voices` ("the first churchman to make an emperor do public penance") is not supported by a held line and is rightly not on the card. `floorNote` and `legacy` agree with the card. `sourcing` ("nine of his own works ... including his letters") does not conflict with the card's "no Latin of his letters or sermons is held": the works are held in English.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

Three name what the brief does not tell (FIX 2 to FIX 4): the death of Auxentius, baptism "by a Catholic bishop", and the tradition. Remaining, each naming what the brief tells or the source a told claim rests on: [1] the governor; [3] Letter XX, the court's demand, Castulus's rescue, the fines and prisons, the soldiers, the secretary, the withdrawal, and Justina as mother of the boy emperor (Valentinian II identifies him); [4] the palaces and the hymns charge; [5] the custom begun at Milan; [6] Augustine received like a father and baptized at Easter 387; [7] the synagogue, the bishop ordered to rebuild, the altar and the promise (Callinicum identifies the brief's "town in the East"); [8] Thessalonica; [9] the penance and Theodoret's door scene; [10] the singing still going on; [11] the last reply, Good Friday 397, the arms like a cross. No quotation marks in any.

## 4. Census rules

Only allowed keys; no `briefLength`. Seven quoted spans in the brief, seven entries, each `modern` word for word; none for a span the brief no longer quotes (v1 had the same seven). Each `printed` and `original` stands at its lines by the fold rule (the stray "*" in PAUL 5602 folds away). Every cited file is in `sources`. No audit, review or ruling named. American spelling throughout ("trades-people" is the print's word, not a spelling variant). "I certainly do not deny it." is six words and so is read blind; it rightly has no `secondReading`.

**Checked at card: "Ambrose for bishop!"** PAUL 3145 "Ambrosium episcopum": the accusative names Ambrose as the bishop the people ask for; "Ambrose for bishop" renders it rightly, and Kaniecka prints "Ambrose Bishop" (PAUL 3199). Rufinus has the same two words (RUF 30237).

## 5. Originals

No Latin of Ambrose's letters or sermons is held (searched `cic/texts/`; only `npnf210` in English), so five spans rightly carry English alone. Paulinus's Latin is carried for the two spans taken from him, clean at PAUL 3145 and 5601-5602. Greek: none. Nothing missing.

## 6. Not-found claims

All upheld: "first" to make an emperor do penance; Paulinus's bees and fire and Maximinus at Aquileia (no line cited); On the Duties given as the chronology's 391 to 392, not the Sheet's "about 391".

## FIXes

**FIX 1.** `uncertain[4]`
- Old: `threatening as authors of sedition any who think that right theirs alone, is dated at Milan on 23 January 386.`
- New: `threatening as authors of sedition any who think that right theirs alone and attempt a disturbance against the order, is dated at Milan on 23 January 386.`

**FIX 2.** `briefReferences[0]`
- Old: `the people of Milan after the death of Auxentius, Ambrose going into the church`
- New: `the people of Milan, Ambrose going into the church`
- Why: the brief does not tell Auxentius or his death.

**FIX 3.** `briefReferences[2]`
- Old: `the tortures, the flight at midnight, baptism by a Catholic bishop and consecration on the eighth day.`
- New: `the tortures, the flight at midnight, baptism and consecration on the eighth day.`
- Why: the brief says only that he was baptized and made bishop within eight days.

**FIX 4.** `briefReferences[12]`: remove the entry.
- Old: `World census, Ambrose's Milan: his tradition.`
- Why: the brief does not name his tradition.
