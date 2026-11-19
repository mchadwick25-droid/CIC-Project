# Batch 6: ruling on originals, and one Ignatius sentence

Independent checker, 2026-11-19. I wrote none of these cards or checks. I read each folder's `<slug>.card.json` and `Card_Check.md` as they stand, then opened every cited file at its lines.

**The rule** (from `ignatius-of-antioch/Card_Check.md`). An original stands only as the page prints it. A scan fault in it is allowed only in two cases. Either a reading resolves it, and a held print confirms that reading (another held edition, the editor's own note, or a parallel held text). Or the fault is a stray mark that is plainly no part of the text, such as a margin number or a running head. Otherwise the original is left out, and the English printed wording stands alone.

**Mark's guidance** (2026-11-19). The aim is high scholarly acceptance, not perfection. Where two held sources disagree, record both. I applied that guidance in two ways. Case, and two forms of one Greek letter (θ and ϑ), are not counted as readings. And in one place (Pliny, FIX 4) a digit zero standing for the capital letter O is treated as a character-code fault, not a reading. Every other correction still needs a held print. The validator drops Greek letters, so every Greek item below was checked by hand.

## Part 1. Originals, card by card

### polycarp-of-smyrna (Gebhardt, `acta-martyrum-selecta_gebhardt1902.txt`)

- **[0] eighty-six years (742-746): LEAVE OUT.** "8&0" and "μὲ ἠδίχησεν" are faults. ἓξ and ἠδίκησεν come from knowing the text, not from a held print.
- **[1] "Away with the atheists" (622-623): LEAVE OUT.** "Alps" is a fault. The page's two other copies of the cry are also garbled ("Aloe" at 733, "dios" at 738), so they confirm nothing.
- **[2] will of God (680): KEEP as it stands.** "Τὸ ϑέλημα τοῦ ϑεοῦ γενέσθω." has no fault. The θ/ϑ mix is two forms of one letter.
- **[3] fire (779-781): LEAVE OUT.** "xci" is a fault, and no held print confirms the reading.
- **[4] birthday (950-951): LEAVE OUT.** "γενόέϑλιον" is a fault, and no held print confirms the reading.
- **[5] those who competed (951-952): LEAVE OUT.** "εἴς τὸ τὴν" is a fault. The τε comes from grammar, not from a print.
- **[6] those to come (952-953): KEEP as it stands.** "καὶ τῶν μελλόντων ἄσκησίν τε καὶ ἑτοιμασίαν." is clean.

So the card check's six readings (FIX 1.1 to 1.5) are not added. Entries [0], [1], [3], [4] and [5] lose `original`, `originalFile` and `originalLines`. Gebhardt stays in `sources`. No other held print has this Greek. Eusebius's Greek of Book IV is not held: the Schwartz file covers Books VI to X only. The second Gebhardt file (`gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt`, the Claremont copy) is another scan of the same print. But its Greek comes out as Latin letters ("Oydonzovra za &£", "eis TE Tmv"), and its own header says the Greek is "not recoverable". Reading that noise as Greek would mean supplying the text from knowledge, so it does not confirm anything.

### josephus (Origen, `origen_commentarii-in-evangelium-matthaei-tomus3-grc-lat_lommatzsch1834.txt`)

- **[6] Origen's Greek `printed` (3731-3733): LEAVE OUT.** The marker "4)" is a stray mark and could be allowed. The other faults have no confirming print: "ἔστιν;", "Ἴη-σοῦν", "ἣτ-τον" and "᾿Ιαχώβῳ". Lommatzsch's note 4 (3753-3755) is about τὸ / τοῦτο and confirms none of them. No other held print has the sentence.
- What stands: `printed` becomes the ANF English, "And the wonderful thing is, that, though he did not accept Jesus as Christ, he yet gave testimony that the righteousness of James was so great" (`anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` 30627-30629). The `englishPrinted`, `englishFile` and `englishLines` keys then go.

### irenaeus-of-lyon (Holl's Epiphanius, `epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt`)

- **[0] the king's portrait (31907-31911): LEAVE OUT.** It is copied from the OCR with its faults: χ for κ throughout (εἰχόνος, χαλῆς, ἐχ, χυνὸς), "Ψηφίδων", "ἀγϑρώπου" and "ἀλῴπεχος".
- **[1] the one house (32715-32719): LEAVE OUT.** χ for κ throughout (χήρυγμα, ἐχχλησία, χαρδίαν), and "προἔφαμεν".
- No other held print has this Greek. The other Epiphanius files cover other books, and no Irenaeus Greek is held. In both entries `printed` becomes the ANF English (anf01 30994-30998 and 31419-31425).

### tatian

- **[0] Q1 (Otto 1851, 12199-12201): KEEP, with FIX 2's wording.** The corrected wording is "χαίρειν εἰπὼν καὶ τῇ Ῥωμαίων μεγαλαυχίᾳ καὶ τῇ Ἀθηναίων ψυχρολογίᾳ, δόγμασιν ἀσυναρτήτοις, τῆς καϑ᾽ ἡμᾶς βαρβάρου φιλοσοφίας ἀντεποιησάμην". The editor's own note at 1686-1689 confirms it: it prints "τῇ Ῥωμαίων / μεγαλαυχίᾳ καὶ τῇ ᾿Αθηναίων ψυ- / χρολογία... τῆς καϑ᾽ ἡμᾶς βαρ- / βάρου φιλοσοφίας ἀντεποιησάμην". The words the note skips ("δόγμασιν ἀσυναρτήτοις") are clean in the text.
- **[3] Q2 (Otto 1851, 14236-14241): KEEP, with FIX 3's wording.** The corrected wording is "Γινώσκων δὲ λοιπὸν τίς ὁ ϑεὸς καὶ τίς ἡ κατ᾽ αὐτὸν ποίησις, ἕτοιμον ἐμαυτὸν ὑμῖν πρὸς τὴν ἀνάκρισιν τῶν δογμάτων παρίστημι, μενούσης μοι τῆς κατὰ ϑεὸν πολιτείας ἀνεξαρνήτου." The lone "Δ" and "δ" are stray margin marks. Neither has an elision mark, and neither can be a word. The same page also sets such marks into its lines ("Ξτὰ", "Ξ κηρύττειν", "10 κατὰ"). The rest of the sentence is clean.
- **[2] Q3, Theodoret's Greek `printed` (Otto 1872, 14984-14987): LEAVE OUT.** "Evgov" for Εὗρον has no confirming print, because Haereticarum fabulae is not held in Greek. This entry has no English. The only other held wording is Maran's Latin on the same page (14994-14997): "Nactus sum etiam ipse libros huiusmodi supra ducentos in honore habitos in ecclesiis nostris, quos Omnes in unum congestos seposui, et pro his quatuor evangelistarum evangelia introduxi." It is clean apart from the case of "Omnes", and it matches the modern span clause by clause. Coordinator's choice: make that Latin the `printed` wording, with `work` relabelled as Maran's Latin, or take the quotation marks off the brief's span.

### valentinus

- **[1] FIX 2, Kroymann's Latin (`tertullian_opera-pars3-lat_kroymann-csel47.txt` 9633-9653): KEEP, with FIX 2's wording.** The wording is "sperauerat episcopatum Valentinus, quia et ingenio poterat et eloquio, sed alium ex martyrii praerogatiua loci potitum indignatus de ecclesia authenticae regulae abrupit".
  - The margin "25", and the notes, apparatus and running head at 9635-9651, are stray marks.
  - "Yalentinus" reads Valentinus. Oehler's edition prints "Valen-" (`tertullian_quae-supersunt-t2-polemica-lat_oehler1853.txt` 21632, scanned "Valenlinus"). The ANF English of this same sentence prints the name "Valentinus" (anf03 43109).
  - "aliura" reads alium. Oehler prints "alium" cleanly (21634).
- The card has no other originals.

### hippolytus-of-rome (Duchesne, `liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt`)

- **[4] "Yppolitus presbyter" (66807) and [5] "in insula nociva" (66808): KEEP as they stand.** Both are clean.
- **[6] Damasus, lines 1-2 (109159-109160): KEEP, with FIX 2 and its two readings.** Benson's *Cyprian* (1897), a held book, confirms both readings. It prints the verse "Hippolytus fertur premerent cum jussa tyranni / Presbyter in scisma semper mansisse Novati" (`benson_cyprian-his-life-his-times-his-work_1897.txt` 11083-11087, where the two-column OCR interleaves the lines). That gives "scisma" for "scismk" and "Novati" for "XOvali". The scan shows a capital O, so in Duchesne's capitals the word is most likely "NOvati". Since case is not counted as a reading, FIX 2's "Novati" is acceptable.
- **[7] Damasus, last line (109166): KEEP, with the page's case.** Duchesne prints "Haec audita rEFERT DAMasus, probat omnia Christus." The card's lower-case form passes the census check, because it folds case. But FIX 2 gives line 1 in Duchesne's capitals, so [7] should match it. The letters are right either way.

### hermas

- **[4] Muratorian Latin (Routh, `apologists-fragmentary_reliquiae-sacrae-vol1-lat-grc_routh1846.txt` 22081-22084): KEEP, with FIX 4.** For "publieari", read "publicari". Routh's own note prints it at 23680: "se publieare vero] For. sed publicari vero." The rest is clean. FIX 4's new `uncertain` keeps both the manuscript's "se publicare" and the editors' "sed publicari", as Mark's guidance asks.
- **[5] FIX 5, "illo apocrypho Pastore moechorum" (Oehler t1 74596-74597): KEEP.** For "moecbomm", read "moechorum". Reifferscheid-Wissowa prints "illo apocrypho Pastore moechorum" cleanly (`tertullian_opera-pars1-lat_reifferscheid-wissowa-csel20.txt` 15056). An alternative with no reading needed is to cite that file and line as the `original` directly, adding that file to `sources` instead of Oehler.

### pliny-the-younger

- **[2] "nostri saeculi" (Mirbt 2819), [4] "Negat inquirendos ... animadvertit." (Oehler t1 11728-11730) and [6] "plurimos Christianorum interfecisset" (Jerome, Fotheringham 42247-42248): KEEP as they stand.** In [4], the carets ("^mandat") are stray marks. In [6], "plu-rimos" is a hyphen join.
- **FIX 2, [0] (Mirbt 2777-2779): KEEP.** The margin "15" is a stray mark, and the rest is clean.
- **FIX 3, [1] "Conquirendi non sunt: si deferantur et arguantur, puniendi sunt" (Mirbt 2811-2816): KEEP.** The running head at 2814 is a stray mark. For "argiiantur", read "arguantur". Schanz-Hosius-Krüger prints Trajan's rescript with "si deferantur et arguantur, puniendi sunt" (`schanz-hosius-krueger_geschichte-der-roemischen-litteratur-teil3-deu_3e-aufl1922.txt` 24554).
- **FIX 4, [3] "O sententiam necessitate confusam!" (Oehler t1 11728): KEEP.** No other held print has this line. The scan's "0" is the same printed shape as the capital O, which the OCR coded as a digit. That is a character-code fault, not a choice between readings. Nothing else could stand there, and the "^" after "necessitate" is a stray mark. This is the one place where I let Mark's guidance decide. The coordinator may overrule it and leave this one out.

### suetonius

- **[0] Claudius 25 (Rolfe 25843-25844), [2] Nero 16 (28458-28460) and [3] Nero 19 `original` (28653-28654): KEEP as they stand.** All three are clean.
- **FIX 3, [5] Tertullian, Apology 3 (Oehler t1 12454-12456): LEAVE OUT.** Some of the faults can be resolved:
  - "*Chrestia •" and "Dus*" read "Chrestianus". The ANF English prints the word "Chrestianus" (anf03 1713-1716), and the bullet is a stray mark.
  - The asterisks, quote marks, carets and "»" are stray marks.
  - But "pcnes" for penes has no confirming print. The Apology is not held in any other edition.
- The card's English stands alone.

## Part 2. "the blessed Ignatius"

**The sentence misplaces the phrase.** The ANF English of Polycarp's Philippians (anf01):

- Ch. 9, line 3487: "to exercise all patience, such as ye have seen [set] before your eyes, not only in the case of the blessed Ignatius, and Zosimus, and Rufus". This is about patience. There is no request here.
- Ch. 13, lines 3619-3625: "Any more certain information you may have obtained respecting both Ignatius himself, and those that were with him, have the goodness to make known to us." Here is the request, and it says "Ignatius himself", not "the blessed Ignatius". The editor's note 414 (3619-3620) says this part survives only in Latin.

**Replacement** for `Polycarp, writing soon after to the church at Philippi, which Paul had once written to, asked for news of "the blessed Ignatius".`:

> Polycarp, writing soon after to the church at Philippi, which Paul had once written to, held up "the blessed Ignatius" as a model of patience. He also asked for any news of him.

The next sentence ("He sent on the letters he held, as Philippi had asked.") follows on unchanged.

## Where two held sources differ and the card states only one

1. **Polycarp [0], [4], [5], once the Greek is left out.** The modern spans follow Gebhardt's Greek where the ANF English says something different:
   - "who saved me": the Greek is τὸν σώσαντά με (GEB 746, clean); ANF has "my Saviour".
   - "birthday": the Greek word means birthday; ANF has "anniversary".
   - "already competed": the Greek is προηϑληκότων, an athlete's word; ANF has "finished their course".

   Without the Greek, the card shows only ANF. Each entry's `uncertain` should say, in English, that the rendering follows Gebhardt's Greek and give ANF's word. This is the same as the Ignatius "I am ground" point.
2. **Josephus [6].** "Our Jesus" follows Origen's τὸν Ἰησοῦν ἡμῶν (OMG 3732). ANF has no "our". An `uncertain` note should say so.
3. **Irenaeus [0].** "Choice small stones" follows the Greek ψηφῖδες (mosaic stones). ANF has "precious jewels". An `uncertain` note should say so.
4. **Hippolytus [6] and [7].** Duchesne prints the stone's letters in capitals, with V for U ("IVSSA"). Benson prints the verse in plain type, with "jussa". This is a difference of printing convention only, and the card follows Duchesne. Nothing more is needed if [7] matches [6], as ruled above.
5. **Polycarp, Philippians 13** (outside the cards' fields, but it bears on Part 2). ANF prints "those that were with him". Its note 415 (3622-3623) says the Latin reads "are", and the editors corrected it. The Ignatius card and brief state neither form, so nothing on the card is wrong. Any later wording about whether Polycarp knew Ignatius was dead should credit both forms: ch. 9 implies he had died, while the Latin of ch. 13 has "are".

Already recorded on the cards, so nothing is needed: Polycarp's date (McGiffert 155/156 against ANF's "about 167", in `datesNote`); Hermas's "se publicare" against "sed publicari"; Hippolytus's place of death (McGiffert against Harnack, in FIX 1); Valentinus's "martyrii" against ANF's "confessorship".
