# Liturgical Evidence Read — Augustine Phase (391–430)

**World:** Latin Pastoral-Congregational Christianity (lpc), Roman North Africa, *c.* 246–430
**Scope of this read:** the Augustine phase (391–430) half of the liturgical-evidence task named at `Doc_07` §8 item 8 and `Doc_02` §9 item 9. The parallel Cyprian-phase read is being conducted by another thread.
**Method:** per `Doc_05` §3, this world wrote no order of service. The rite is recovered from what preaching, catechesis, and controversy presuppose about it. Throughout, a claim that a text *states* is marked **STATEMENT**; a claim recoverable only because a passage *would not make sense unless* a practice existed is marked **PRESUPPOSITION**. Every quotation is character-exact from the vendored file, with editorial `<note>` spans identified and excluded from anything attributed to Augustine's own voice.

---

## 1. What was read, and how

### Texts opened (all under `/home/user/cic-project/cic/texts/`)

| File | What was read within it |
|---|---|
| `npnf101_augustine-confessions-letters.xml` | *Confessions* Book I (chs. XI–XII), Book IX (ch. VI); *Letters* LIV–LV (to Januarius), XCVIII (to Boniface), CXXVI (to Albina), CCXXVIII (to Honoratus); full-text keyword survey of the entire letters corpus |
| `npnf104_augustine-anti-manichaean-anti-donatist.xml` | *On Baptism, Against the Donatists*, Books I, III, V (targeted); *Answer to the Letters of Petilian*, Book II ch. 23; full-text keyword survey of both anti-Donatist works and the Council-of-Carthage speeches Augustine quotes within them |
| `npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml` | *On the Catechising of the Uninstructed* (De Catechizandis Rudibus) in full; *On the Creed: A Sermon to the Catechumens* (De Symbolo Ad Catechumenos) in full; the Introductory Notice to *A Treatise on Faith and the Creed* (which quotes *Retractationes* I.17); *The Enchiridion* ch. 82; full-text keyword survey of the volume |
| `npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml` | Sermon VI [LVI Ben.] and Sermon VII [LVII Ben.] ("to the Competentes," on the Lord's Prayer) in full; Sermon LXXXII [CXXXII Ben.] (on John 6:55) in full; full-text keyword survey of the whole volume (Harmony of the Gospels + Sermons on Selected Lessons) |
| `npnf107_augustine-homilies-john-soliloquies.xml` | Full-text keyword survey only (competentes, catechumen, exorcism, scrutiny, dismissal, reconciliation, laying-on-of-hands, kiss of peace, milk and honey) — no passage in this file yielded material beyond what the other five files already supplied; read less exhaustively line-by-line than the other files given time constraints |
| `npnf108_augustine-exposition-psalms.xml` | Expositions on Psalms XLII, LXVI, LXXXI, and CXXXIII in full; full-text keyword survey of the whole volume |
| `augustine_confessiones-lat_knoll-csel33.txt` | Used to verify the Latin behind *Confessions* I.11.17 |
| `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt` | Used to verify the Latin behind *De Baptismo* III.16.21 |
| `augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt` | Used to verify the Latin behind the Psalm LXXXI renunciation dialogue and the Psalm CXXXIII *Sursum corda* reference |

**Corpus-discipline notes applied:** all English-text loci below were resolved by `title=`/`n=` attributes on the governing `<div2>`/`<div3>`/`<div4>`, never by line position; every `<note place="end">...</note>` span was located and excluded from quotations attributed to Augustine — where an editorial note supplies a Latin gloss (e.g. "*Sacramentis*", "*Agere pœnitentiam*", "*Characterem*"), that gloss is reported separately and labeled as the 19th-century editor's/translator's voice, not Augustine's; hyphenated line-breaks were rejoined before searching.

**OCR artifacts in the vendored Latin plain-text files, disclosed here so a later string search doesn't mistake a corrected quotation for a fabricated one:**
- `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt`, at the locus for *De Baptismo* III.16.21: **the vendored file reads `hominera`**, not `hominem` — "*quid est enim aliud nisi oratio super hominera?*" This is an OCR misread of `hominem` (no other word fits the grammar or the sense). The quotation given in §1j/§3 below is silently corrected to the obvious reading, `hominem`; this note records that correction openly rather than leaving it silent.
- `augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt`, at the Psalm CXXXIII/CXXXII locus (§2e below): the vendored file reads "*Sursum cor habe , ct nemo te angustabit in coelo '.*" — `ct` is an OCR misread of `et`, and there is a stray closing mark after `coelo` that is apparatus/typesetting noise, not part of the sentence. The quotation given below corrects `ct` to `et` and drops the stray mark; the spacing before punctuation (`habe , ct`) is the print edition's own convention and was silently tightened to modern spacing (`habe, et`) purely for readability, with no effect on wording.
- `augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt`, at the Psalm LXXXI locus (§1e below): the vendored file reads "*Renuntias ? Renuntio : et redit ad qnod renuntiat..*" — `qnod` is an apparent OCR misread of `quod`, left **unaltered** in the quotation below because it does not touch the words being cited as evidence (the renunciation exchange itself, `Renuntias? Renuntio?`, is unaffected either way); only the pre-punctuation spacing was tightened and the doubled final stop reduced to one, again for readability with no effect on wording.
- `augustine_confessiones-lat_knoll-csel33.txt`, at *Confessions* I.11.17 (§1a below): the vendored plain-text file interleaves the CSEL print edition's own marginal line-numbers into the running text — a bare "15" sits between `condiebar` and `eius sale` in the file. This is the edition's line-counter, not part of Augustine's Latin, and was removed for legibility when the sentence was quoted across that line break.

### What I searched for and found nothing (reported as absence, not silence)

- **"energumen"** (any spelling) — zero hits in all six English NPNF files searched (npnf101, 103, 104, 106, 107, 108). No evidence for or against a distinct liturgical category of demoniac/energumen in this reading; the term simply did not surface.
- **"milk and honey" as an administered ritual element** — the phrase occurs repeatedly (npnf101, npnf107, npnf108) but in every located instance it is scriptural-exegetical ("a land flowing with milk and honey"), never a description of milk and honey given to the newly baptized. I found no locus describing this practice in these texts, though it is attested elsewhere in the wider North African tradition (Tertullian).
- **"viaticum" / explicit single-person deathbed communion terminology** — zero hits. The closest material found is *Confessions* I.11 (postponement of a sick child's baptism) and *Letter* CCXXVIII.8 (baptism, reconciliation, and penance urgently sought during a mass civil emergency) — both about baptism/reconciliation under threat of death, not a named "viaticum" rite for the dying specifically.
- **Explicit description of a Holy Thursday reconciliation-of-penitents ceremony** — *Letter* LV to Januarius (the letter most likely to contain it, given its extended treatment of Lent, the Paschal Triduum, and the neophyte octave) was read through its discussion of the forty days' fast and the eight days of the neophytes (§32) without turning up a description of a specific Thursday reconciliation rite in the portion read. I did not locate *Letter* CLIII (to Macedonius, known from other transmissions to discuss penance) in this file at all — the NPNF letter selection here jumps from Letter CL to Letter CLVIII, so CLIII is simply not present in this vendored file.
- **Specific bodily postures of public penance (sackcloth, ashes, kneeling "stations")** — searched across all six files; the only prostration material found (*On Care to Be Had for the Dead*, npnf103) concerns prayer posture generally, not penitential status specifically. No named grade-system of penitents (weepers/kneelers/etc.) was found.
- **"competentes" in Augustine's own spoken sermon text** — the word appears repeatedly as an editorial/manuscript-tradition sermon *heading* ("to the Competentes") and in translators' endnotes, but I did not find Augustine using the untranslated Latin word *competentes* inside the body of a sermon in these NPNF translations (the translators render it into English or leave it only in headings).

---

## 2. Findings by domain

### Domain 1 — Baptism as administered

**1a. Admission to the catechumenate: signing with the cross and salt.**
> "Even as a boy I had heard of eternal life promised to us through the humility of the Lord our God condescending to our pride, and I was signed with the sign of the cross, and was seasoned with His salt even from the womb of my mother, who greatly trusted in Thee."
— *Confessions* I.11.17 (npnf101). **STATEMENT.** Confidence: **Widely Accepted**.
Latin verified at `augustine_confessiones-lat_knoll-csel33.txt`: "et signabar iam signo crucis eius et condiebar eius sale iam inde ab utero matris meae." The rite behind this — signing with the cross plus a blessed portion of salt given to a new catechumen — is independently corroborated (as a live practice, not just autobiography) in *On the Catechising of the Uninstructed* 26.50 (npnf103): "he is to be solemnly signed and dealt with in accordance with the custom of the Church. On the subject of the sacrament, indeed, which he receives... that species, which is then sanctified by the blessing, is therefore not to be regarded merely in the way in which it is regarded in any common use." **STATEMENT** (Augustine instructing a catechist what to do). The identification of the "species" as salt is the *editor's* endnote gloss ("*Speciem* = kind, in reference to the outward and sensible sign of the *salt*"), not Augustine's own wording in this locus — flagged accordingly; the Confessions parallel independently supplies "salt" in Augustine's own voice.

**1b. "Giving in the name" (enrollment as a competens) tied to the approach of Easter.**
> "Thence, when the time had arrived at which I was to give in my name... we returned to Milan... and we were baptized."
— *Confessions* IX.6.14 (npnf101). **STATEMENT.**
> "I plead, I do not discuss it. Lo, Easter is at hand, give in thy name for baptism."
— Sermon LXXXII [CXXXII Ben.], §1, on John 6:55 (npnf106). **STATEMENT**, addressed live to catechumens ("Hearers") in the congregation. Confidence: **Widely Accepted** (the practice of *nomen dare* before Lent is one of the best-attested North African customs, and here it is attested twice, independently, in Augustine's own voice).

**1c. Exorcism and exsufflation of infant candidates, witnessed the same day as the sermon.**
> "This is the reason why, as ye have seen to-day, as ye know, even little children undergo exsufflation, exorcism; to drive away from them the power of the devil their enemy, which deceived man that it might possess mankind. It is not then the creature of God that in infants undergoes exorcism or exsufflation: but he under whom are all that are born with sin."
— *On the Creed: A Sermon to the Catechumens* §2 (npnf103). **STATEMENT**, and moreover an eyewitness cross-reference ("as ye have seen to-day") — Augustine is preaching on the same liturgical occasion at which the audience had just watched infants exorcised. Confidence: **Widely Accepted**.

**1d. Exorcism-then-baptism as a fixed sequence, described in fire/water imagery.**
> "Therefore also in the mystic rites and in catechising and in exorcising, there is first used fire. For whence ofttimes do the unclean spirits cry out, 'I burn,' if that is not fire? But after the fire of Exorcism we come to Baptism: so that from fire to water, from water unto refreshment."
— Exposition on Psalm LXVI, §15 (npnf108). **STATEMENT.** Confidence: **Dominant Modern Reconstruction** (the sequence itself is uncontroversial in scholarship; this locus supplies primary confirmation from this world's own texts).

**1e. The renunciation dialogue.**
> "Dost thou renounce? I renounce. And he returns to what he renounced. In fact, what things dost thou renounce, except bad deeds, diabolical deeds, deeds to be condemned of God, thefts, plunderings, perjuries, manslayings, adulteries, sacrileges, abominable rites, curious arts."
— Exposition on Psalm LXXXI, §18 (npnf108). **STATEMENT** — Augustine is directly re-enacting a liturgical Q&A for his hearers. The NPNF translator's own note reads: "He alludes to the form of interrogatory at Baptism" (editor's voice, given for context, not Augustine's wording). Latin verified at `augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt`: "Inimici Domini mentiti sunt ei. Renuntias? Renuntio: et redit ad qnod renuntiat." Confidence: **Widely Accepted**.

**1f. The Creed handed over and given back (traditio/redditio symboli).**
> "Receive, my children, the Rule of Faith, which is called the Symbol (or Creed). And when ye have received it, write it in your heart, and be daily saying it to yourselves... what ye are about to hear, that are ye to believe; and what ye shall have believed, that are about to give back with your tongue... For this is the Creed which ye are to rehearse and to repeat in answer."
— *On the Creed: A Sermon to the Catechumens* §1 (npnf103). **STATEMENT.**
Cross-confirmed by Augustine's own *Retractationes* I.17, quoted in the Introductory Notice to *A Treatise on Faith and the Creed* (npnf103): "I threw into the form of a book... although not in a method involving the adoption of the particular connection of words which is given to the *competentes* to be committed to memory." **STATEMENT** (Augustine's own retrospective account of his practice). Confidence: **Widely Accepted**.

**1g. Postponement of baptism, including for the dying, and the social commonplace this produced.**
> "...being at the point of death... with what emotion of mind and with what faith I solicited from the piety of my mother, and of Thy Church, the mother of us all, the baptism of Thy Christ... So my cleansing was deferred, as if I must needs, should I live, be further polluted."
— *Confessions* I.11.17 (npnf101). **STATEMENT.**
> "whence comes it that it is still dinned into our ears on all sides, 'Let him alone, let him act as he likes, for he is not yet baptized'?"
— *Confessions* I.11.18 (npnf101). **PRESUPPOSITION/reported social commonplace** — Augustine is quoting a proverb-like popular saying as evidence of how normalized deferred baptism was; this is stronger than a bare inference because he explicitly reports it as something "dinned into our ears on all sides," but it is not itself a description of the rite. Confidence: **Widely Accepted**.

**1h. Emergency ministrations, including for the dying, during civil catastrophe.**
> "an extraordinary crowd of persons, of both sexes and of all ages, is wont to assemble in the church,—some urgently asking baptism, others reconciliation, others even the doing of penance, and all calling for consolation and strengthening through the administration of sacraments... how great perdition overtakes those who depart from this life either not regenerated or not loosed from their sins!... if the ministers be at their posts... all are aided,—some are baptized, others reconciled to the Church. None are defrauded of the communion of the Lord's body."
— *Letter* CCXXVIII (to Honoratus), §8 (npnf101). **STATEMENT.** This is the single richest locus in the whole read: it names baptism, reconciliation (of penitents/schismatics), penance-entry, and eucharistic communion as four distinct, regularly performed pastoral actions, each sought by name by ordinary people in crisis. Confidence: **Widely Accepted**.

**1i. Infant baptism: presented by another's will, not the infant's.**
> "the possibility of regeneration through the office rendered by the will of another, when the child is presented to receive the sacred rite, is the work exclusively of the Spirit... Now the regenerating Spirit is possessed in common both by the parents who present the child, and by the infant that is presented and is born again; wherefore, in virtue of this participation in the same Spirit, the will of those who present the infant is useful to the child."
— *Letter* XCVIII (to Boniface), §2 (npnf101). **STATEMENT.** Confidence: **Widely Accepted**.

**1j. What is *not* repeated for a convert from heresy/schism, and what is done instead.**
> "the laying on of hands in reconciliation to the Church is not, like baptism, incapable of repetition; for what is it more than a prayer offered over a man?"
— *On Baptism, Against the Donatists*, Book III, ch. 16, §21 (npnf104). **STATEMENT** — this is Augustine's own doctrinal ruling, not a report of someone else's practice. Latin verified at `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt`: "manus autem inpositio non sicut baptismus repeti non potest. quid est enim aliud nisi oratio super hominem?"
Corroborated in Augustine's own voice again at Book V, ch. 23, §33: "hands are laid on heretics when they are brought to a knowledge of the truth." **STATEMENT.**
(For context only, *not* attributed to Augustine's own era: within the same Book III, Augustine quotes bishops' speeches from the mid-3rd-century Council of Carthage under Cyprian, e.g. Crescens of Cirta — "these being reconciled and admitted to the penance of the Church by the imposition of hands" — as historical testimony he is arguing *with*, from a period a different reading thread is covering; it is reported here only to show it is the same rite-name Augustine's own ruling continues to use a century and a half later.) Confidence: **Widely Accepted** — this is one of the most secure findings in the whole read.

**1k. Paschal baptism and the eight-day octave of the neophytes.**
> "The celebration of Easter and Pentecost is therefore most firmly based on Scripture. As to the observance of the forty days before Easter, this has been confirmed by the practice of the Church; as also the separation of the eight days of the neophytes, in such order that the eighth of these coincides with the first."
— *Letter* LV (to Januarius), §32 (npnf101). **STATEMENT.** Confidence: **Widely Accepted / Dominant Modern Reconstruction** — this letter is one of the classic sources historians already use for this calendar; the read confirms it verbatim in this vendored text.

**1l. A specific psalm ritually associated with candidates approaching the font.**
> "it is not ill understood as the cry of those, who being as yet Catechumens, are hastening to the grace of the holy Font. On which account too this Psalm is ordinarily chanted on those occasions, that they may long for the Fountain of remission of sins, even 'as the hart for the water-brooks.' Let this be allowed; and this meaning retain its place in the Church; a place both truthful and sanctioned by usage."
— Exposition on Psalm XLII, §1 (npnf108). **STATEMENT.** Confidence: **Widely Accepted**.

### Domain 2 — The Eucharist

**2a. Catechumens excluded from understanding the Eucharistic teaching; the discipline of the secret presupposed and named.**
> "As we heard when the Holy Gospel was being read, the Lord Jesus Christ exhorted us by the promise of eternal life to eat His Flesh and drink His Blood. Ye that heard these words, have not all as yet understood them. For those of you who have been baptized and the faithful do know what He meant. But those among you who are yet called Catechumens, or Hearers, could be hearers, when it was being read, could they be understanders too?... Come to the profession, and thou hast resolved the difficulty. For what the Lord Jesus said, the faithful know well already. But thou art called a Catechumen, art called a Hearer, and art deaf."
— Sermon LXXXII, §1 (npnf106). **STATEMENT.** Confidence: **Widely Accepted**.

**2b. What competentes are told they will soon receive "at the altar."**
> "There is a spiritual food also which the faithful know, which ye too will know, when ye shall receive it at the altar of God... So then the Eucharist is our daily bread."
— Sermon VII [LVII Ben.], "to the Competentes," §7 (npnf106). **STATEMENT**, direct address to candidates.
> "if by this our daily bread thou understand what the faithful receive, what ye shall receive, when ye have been baptized... that we may live in such sort, as that we be not separated from the Holy Altar."
— Sermon VI [LVI Ben.], "to the Competentes," §10 (npnf106). **STATEMENT.** Confidence: **Widely Accepted**.

**2c. Reception of the Eucharist hand to hand, reciprocally, between clergy.**
> "with whom you joined in the kiss of peace in the sacraments, in whose hands you placed the Eucharist, to whom in turn you extended your hands to receive it from his ministering."
— *Answer to the Letters of Petilian*, Book II, ch. 23, §53 (npnf104). **STATEMENT.** Confidence: **Widely Accepted** (communion in the hand is well attested generally in this period; this locus supplies this world's own primary confirmation).

**2d. Dismissal of catechumens as a standing structural feature of the assembly, even outside a Eucharistic celebration.**
> "We dismissed the catechumens, and he adhibited his signature to the document at once."
— *Letter* CXXVI (to Albina), §5 (npnf101). **STATEMENT.** This shows the dismissal was routine enough to be performed even during an ad-hoc parish business meeting unrelated to the liturgy proper — good evidence that "dismiss the catechumens" was a reflexive procedural marker of what kind of gathering could continue. Confidence: **Widely Accepted**.

**2e. The *Sursum corda* dialogue presupposed as familiar to the whole congregation.**
> "Do not hear, 'Lift up your hearts,' with a deaf ear. Keep thy heart lifted up, and no one will straiten thee in heaven."
— Exposition on Psalm CXXXIII, §9 (npnf108). **PRESUPPOSITION**, strengthened toward statement by direct naming of the phrase as something the congregation "hears." Latin verified at `augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt` (at the corresponding Vulgate-numbered Psalm CXXXII): "Noli surdus audire, Sursum corda. Sursum cor habe, et nemo te angustabit in coelo." The same formula recurs, used the same presupposing way, at Psalm XXXIV/³⁶ and Psalm CXLVIII expositions (npnf108). Confidence: **Widely Accepted**.

**2f. Exclusion from the altar for grave public sin, and its reversal.**
> "for which it is necessary that the sinner be cut off from the altar, and be so bound in earth, as to be bound in heaven, to his great and deadly danger, unless again he be so loosed in earth, as to be loosed in heaven."
— Sermon VI, "to the Competentes," §12 (npnf106). **STATEMENT.** This belongs equally to Domain 3 (penance/reconciliation) — cross-referenced there.

### Domain 3 — Penance and reconciliation

**3a. Penance as a publicly visible status, distinct from ordinary daily prayer for venial sin.**
> "For those whom ye have seen doing penance, have committed heinous things, either adulteries or some enormous crimes: for these they do penance. Because if theirs had been light sins, to blot out these daily prayer would suffice."
— *On the Creed*, §15 (npnf103). **STATEMENT**, and "whom ye have seen" again marks this as something the congregation visibly witnesses. The editor's endnote glosses "doing penance" as "*Agere pœnitentiam*" (Latin gloss, editor's voice, given for the term only).
> "In three ways then are sins remitted in the Church; by Baptism, by prayer, by the greater humility of penance; yet God doth not remit sins but to the baptized... The Catechumens, so long as they be such, have upon them all their sins."
— *On the Creed*, §16 (npnf103). **STATEMENT.** Confidence: **Widely Accepted**.

**3b. Three named pastoral acts sought together in crisis: baptism, reconciliation, and "the doing of penance."**
> "some urgently asking baptism, others reconciliation, others even the doing of penance."
— *Letter* CCXXVIII.8 (npnf101), already quoted at 1h. This locus is the clearest evidence in the whole read that *reconciliation* and *entering penance* were understood as two distinct, nameable acts, not one — precisely the kind of distinction `Doc_06` §5 asks this read to test for. **STATEMENT.** Confidence: **Widely Accepted**.

**3c. The rite-name and theological minimum for reconciling one baptized outside the Church: the imposition of hands as "a prayer offered over a man."**
See 1j above (*On Baptism* III.16.21 and V.23.33). This is the strongest single lexicon candidate from the whole read (see §3 below).

**3d. Shame as the deterrent to entering the canonically required penance.**
> "Now even penance itself, when by the law of the Church there is sufficient reason for its being gone through, is frequently evaded through infirmity; for shame is the fear of losing pleasure when the good opinion of men gives more pleasure than the righteousness which leads a man to humble himself in penitence."
— *Enchiridion*, ch. 82 (npnf103). **STATEMENT.** This directly supports `Doc_07`'s finding that this world's crises are rite disputes turning on cost: Augustine names public shame, not merely doctrine, as the reason penance is "evaded." Confidence: **Widely Accepted**.

**3e. Excommunication from the altar and its reversal by "loosing."**
See 2f above (Sermon VI.12, npnf106) — "cut off from the altar... bound in earth... loosed in earth, as to be loosed in heaven." **STATEMENT.**

### Domain 4 — The catechumenate

**4a. Teaching order: Creed first, then the Lord's Prayer, in immediate sequence over consecutive sessions.**
> "The order established for your edification requires that ye learn first what to believe, and afterwards what to ask... Therefore have ye first learned what to believe: and to-day have learnt to call on Him in whom ye have believed."
— Sermon VII, "to the Competentes," §1 (npnf106). **STATEMENT**, and it dates itself relative to a prior session ("to-day").
> "The Son of God, our Lord Jesus Christ, hath taught us a Prayer; and though He be the Lord Himself, as ye have heard and repeated in the Creed..."
— same sermon, §2. **STATEMENT**, confirming the *redditio symboli* (they had "repeated" the Creed) preceded this teaching of the Lord's Prayer. Confidence: **Widely Accepted**.

**4b. The Creed given to be memorized, in a fixed verbal form, specifically to the competentes.**
See 1f above. Cross-domain with Domain 1.

**4c. Exorcism/exsufflation and signing with the cross and salt as entry markers of the catechumenate.**
See 1a and 1c above. Cross-domain with Domain 1.

**4d. What the *Confessions* records of Augustine's own catechumen status.**
Augustine was signed and salted as an infant catechumen (I.11.17); his baptism was deferred in childhood illness and again through young adulthood while he was a Manichaean "Hearer" and later a philosophically convinced but unbaptized inquirer; he finally "gave in his name" before his baptism at Milan at Easter, administered by Ambrose, together with Alypius and his son Adeodatus (IX.6.14): "we were baptized, and solicitude about our past life left us." **STATEMENT** (autobiographical). Confidence: **Widely Accepted**.

**4e. The competentes told directly what awaits them at the altar.**
See 2b above — cross-domain with Domain 2, and itself a strong indicator of catechetical content and order (Creed → Lord's Prayer → what the Eucharist will be once baptized).

---

## 3. Proposed lexicon-term candidates

Per `Doc_06` §5 item 3, these are **proposed only** — nothing has been added to any lexicon.

**Candidate 1 — the rite of reconciling a baptized convert from heresy/schism: *manus impositio* / "imposition of hands as reconciliation."**
- Latin form: *manus impositio* (also *impositio manuum*); Augustine's own gloss for what the rite *is*: "*oratio super hominem*" ("a prayer offered over a man").
- English rendering in this vendored translation: "the laying on of hands in reconciliation."
- Exact locus: *On Baptism, Against the Donatists*, Book III, ch. 16, §21 (npnf104), Latin confirmed at `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt`.
- What it denotes: the sole rite performed on a person validly baptized outside the Catholic communion (heretic or schismatic) who comes to unity — explicitly *not* a second baptism, and explicitly repeatable (unlike baptism), because Augustine defines its content minimally as prayer, not as a second sacramental washing. This is a strong candidate because it is precisely the kind of technical distinction (not-baptism-but-something) that a keyword-frequency-based candidate discovery pass (Doc_03's method) would be unlikely to isolate — it requires reading the theological argument to see that Augustine deliberately holds apart two different kinds of rite: baptism, and the laying on of hands in reconciliation (the NPNF104 wording, not a second, differently-worded phrase).
- Confidence: **Widely Accepted**.

**Candidate 2 — the baptismal renunciation formula: *renuntiatio* / "Renuntias? Renuntio."**
- Latin form, confirmed at source: "Renuntias? Renuntio" (Enarrationes in Psalmos, on Ps. 80/81, at `augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt`).
- English rendering: "Dost thou renounce? I renounce."
- Exact locus: Exposition on Psalm LXXXI, §18 (npnf108).
- What it denotes: the interrogatory renunciation-of-the-devil exchange performed at baptism, preserved here not as a rubric but as Augustine re-performing it rhetorically mid-sermon for a general congregation — evidence that the exact wording was current enough to be recognizable outside the baptismal rite itself. This is a good second candidate because a term-frequency pass over "renounce" language would very likely miss that this specific two-line exchange is a fixed liturgical formula rather than ordinary vocabulary, since nothing in the surrounding prose flags it as a quotation — only the editor's separately placed endnote does, and Doc_03's method (per the brief) works from the primary running text.
- Confidence: **Widely Accepted**.

**Candidate 3 (weaker, offered for completeness) — *sacramentum salis*, "the sacrament of salt," as the name for the catechumenal admission rite.**
- I did not find Augustine himself using the phrase "*sacramentum salis*" in the vendored primary text (it is the *editor's* endnote gloss to *On the Catechising of the Uninstructed* 26.50, reconstructing what "sacrament" and "species" refer to). Augustine's own words in Confessions I.11.17 name the two elements ("signed with the sign of the cross, and seasoned with His salt") but do not supply a single technical name for the combined rite in this vendored corpus.
- I flag this only as a candidate for the parallel Cyprian-phase or Doc_03 threads to verify independently, since the practice itself is solidly attested twice in Augustine's own voice (1a above) even though the *name* "sacramentum salis" is not attested in his own words here — this is exactly the kind of distinction (practice attested, technical Latin label not attested in this corpus) the "propose only" instruction is meant to protect against overclaiming.
- Confidence for the *practice*: **Widely Accepted**. Confidence for the *name* "sacramentum salis" as Augustine's own term: **Not Attested** in the texts read.

---

## 4. What I could not establish

- **A named, described ceremony of Holy Thursday reconciliation of penitents.** I read the letter most likely to contain it (*Letter* LV to Januarius, on the Paschal calendar) through its treatment of Lent and the neophyte octave and did not find it there; *Letter* CLIII, known in the wider Augustine corpus to discuss penance and reconciliation at length, is simply absent from this vendored NPNF selection (the file jumps from Letter CL to Letter CLVIII). I cannot say whether Augustine describes this ceremony elsewhere in his corpus — only that it is not present in the texts I was given to read.
- **Grades or stages of public penitents** (e.g., a formal sequence of "weepers," "hearers," "kneelers," "standers" as in some Eastern sources). Not found; the African material read here treats penance as a single publicly visible status ("whom ye have seen doing penance") rather than a graded system, but I cannot rule out a graded system existing in texts outside this read.
- **A named single-person rite for the dying (viaticum) as distinct from general "reconciliation."** The evidence found (Confessions I.11; Letter CCXXVIII.8) is about baptism and reconciliation sought under threat of death, but I found no locus naming or describing a specific rite for the dying as such.
- **The technical Latin name for the catechumenal admission rite** (see Candidate 3 above) — the practice is attested; a single fixed technical name for it, in Augustine's own words in this corpus, is not.
- **Whether "competentes" was a word Augustine himself spoke aloud in these sermons**, versus a manuscript/editorial heading applied to them afterward — the headings ("Sermon VI... to the Competentes") are consistent across the collection but I did not find the word inside the transcribed sermon text itself in the files read.
- **npnf107** (Tractates on John, Homilies on 1 John, Soliloquies) was surveyed by keyword search across its full text but not read exhaustively section-by-section the way the other five files were; a closer read of it might surface material this pass missed, particularly given its size (11,900+ lines cleaned) and the number of generic keyword hits (catechumen: 21, font: 33, reconcil: 39) that were not individually opened.
