# Fresh check: Tatian (targeted check of the fresh-read fixes)

Batch 12, 2026-11-27. Checked only what `Fixes_Fresh.md` changed in `Outline.md`, against `Fresh_Read.md` and the cited lines in `cic/texts/`. The brief and the outline were not edited.

## 1. New and changed outline lines: PASS

- **Words to explain, *David's line*.** TH 4157 (Latin, "Dominus autem Deus, non solum Davidis semen in aeternum servaturum, sed ejus etiam regnum sine fine conservaturum promisit") and TH 4232-4240 (Greek, "σπέρμα τοῦ Δαβὶδ εἰς τὸν αἰῶνα τηρήσειν, ἀλλὰ καὶ τὴν βασιλείαν ἀκατάλυτον φυλάξειν ... τὸν θρόνον σου ... τὸ γένος φροῦδον ... τὴν βασιλείαν δεξαμένην τὸ πέρας") hold the outline's English. The passage is in *Eranistes* Dialogue I (headers at TH 1675, 3980, 4646; Dialogue II starts at 7571), and it is spoken by ORTH., the orthodox speaker who carries Theodoret's own view (speaker label before TH 4166-4172, the same argument). "Documented as his own words" is right.
- **"King David's family".** The summary holds. Theodoret gives David a kingdom (βασιλεία, "regnum") and a throne (θρόνος) promised by God, and in the same exchange the promised son is "excelsior futurus regibus terrae" (TH 4186-4187). One who holds a kingdom and a throne is a king; "King" adds a title, not a claim. "Family" is Theodoret's own γένος / "genus" (TH 4239, 4160).
- **"As a man".** "κατὰ σάρκα" holds at TH 29729-29730 (Compendium), Latin "secundum carnem" at TH 29713-29714; Dialogue I TH 4635 ("ἐκ σπέρματος Δαβὶδ κατὰ σάρκα βεβλάστηκεν") and 4652-4655 ("οὐ σάρκα μόνον, ἀλλὰ καὶ ψυχὴν εἶχεν"), Latin 4561. "As a man" is a fair plain sense of "according to the flesh", with the soul line showing full manhood is meant. Documented.
- **What came of him 2** and the **Do not say** Say text now match each other and the beat wording.
- **Opening 1, "turned inward".** AG-G 10387 "ἐμαυτὸν γενόμενος", AG-G 10457 "in me ipsum descendens", AG 6970 "retiring by myself": an inward act. Holds. The new Do not say line is word for word as Fresh_Read gives it.

## 2. The four cuts: PASS

- ", explaining it": "Later writers of the Church of the East say Ephrem, a deacon of Nisibis, commented on the Diatessaron." "Commented on" still says what the work was (Do not say, Ephrem line). It does not echo the live text, which has "Ephrem the Syrian wrote a commentary on it." Clear on one hearing.
- "And" in "And on his own": "On his own he taught that Adam, the first man, was not saved." Clear; beat 5 holds "a teaching of his own".
- "also" in "He also wove": "He wove the four Gospels into one book, read in worship by the Syriac-speaking churches of the East." Clear; the essence holds the wording.
- "And" before "Moses is older": "Moses is older than Homer, he argues, citing Greek, Chaldean, Phoenician and Egyptian writers rather than Christian ones." Clear; beat 3 holds it.
- None touches the heart, a quote or a Never cut item.

## 3. Brief changes and count: PASS

For `tatian.brief.txt`, in order:

1. Old: "He went off alone and asked how he might find the truth."
   New: "He turned inward and asked how he might find the truth."
2. Old: "Irenaeus says Tatian spoke of aeons, invisible heavenly powers, like the followers of Valentinus, a teacher at Rome."
   New: "Irenaeus says Tatian invented aeons, invisible heavenly powers, like the followers of Valentinus, a teacher at Rome."
3. Old: "Eusebius, a bishop, makes Tatian the source of the Encratites, about 172."
   New: "Eusebius, a bishop, makes Tatian the source of the Encratites, and places this about 172."
4. Old: "Later writers of the Church of the East say Ephrem, a deacon of Nisibis, wrote a commentary explaining the Diatessaron."
   New: "Later writers of the Church of the East say Ephrem, a deacon of Nisibis, commented on the Diatessaron, explaining it."
5. Old: "A later Roman teacher gives the reason: disobedience began with Adam."
   New: "A later Roman teacher gives Tatian's reason: disobedience began with Adam."
6. Old: "Tatian, he says, had cut out the lists of Jesus's ancestors and other passages showing the Lord born of David's line."
   New: "Tatian, he says, had cut out the lists of Jesus's ancestors and other passages showing the Lord born, as a man, of King David's family."
7. Old: "Later writers of the Church of the East say Ephrem, a deacon of Nisibis, commented on the Diatessaron, explaining it."
   New: "Later writers of the Church of the East say Ephrem, a deacon of Nisibis, commented on the Diatessaron."
8. Old: "And on his own he taught that Adam, the first man, was not saved."
   New: "On his own he taught that Adam, the first man, was not saved."
9. Old: "He also wove the four Gospels into one book, read in worship by the Syriac-speaking churches of the East."
   New: "He wove the four Gospels into one book, read in worship by the Syriac-speaking churches of the East."
10. Old: "And Moses is older than Homer, he argues, citing Greek, Chaldean, Phoenician and Egyptian writers rather than Christian ones."
    New: "Moses is older than Homer, he argues, citing Greek, Chaldean, Phoenician and Egyptian writers rather than Christian ones."

Each old text occurs once at its step. Count on a scratch copy with all ten applied, `python -m engine.m1.profile_readability --report`: 675 words, grade 8.4 (names out 7.5), reading ease 72.2, 17.3 words a sentence, longest 31 words, pass. At the 675 ceiling.

Note: Fresh_Read gives change 1 as "Words: 0"; it is -1, as `Fixes_Fresh.md` says. The count above is the measured one.
