# C14 coverage map: suffering, doubt, failure, hypocrisy, leaving

Date 2026-10-25. Read-only. Twelve worlds with records (`fix` excluded as synthetic; seven other codes have no records). Method: nine `coverage_search.py --whole-words` runs (`search/C14/S1..S9-*.json`), every record hit read against `retrieve_when` and `use_note.means`, then judged by hand; vendored files from `cic/corpus-map/`; registries from `records/<code>/source`, Doc_02, WANTS-REGISTER, download-queue-seed. Per-cell detail in `C14-coverage.json`.

Layers: **R** rendered in `records/<code>/` (R\* = rendered as an honest limit or contested claim, not an answer); **L** loaded in a mapped vendored text but in no record; **I** identified in a registry only; **O** outside the repo; **N** nothing. Suffix h/m/l = confidence.

## Sub-questions

| id | question | items | canon |
|---|---|---|---|
| S1 | Why God allows suffering; where was God (a sick child; healing prayed for and refused) | C14-01, 14, 19, 23; R-04, R-31 | F6-P-02 |
| S2 | Unanswered prayer, God's silence, grief that does not lift | C14-04; R-19 | F4-P-03 |
| S3 | Anger at God; lament out loud | C14-25; R-18 | none |
| S4 | Doubt and room for it; not believing the church; losing faith and saying so; deconstructing and keeping something | C14-02, 03, 13, 20, 26; R-12 | F1-P-01/02 |
| S5 | Hypocrisy and a judgmental community; belonging; forgiving the unrepentant | C14-07, 11; R-13, R-14 | F6-P-05, F4-P-02 |
| S6 | Leaders who did harm, cover-up, bullying bishops, accountability; the hardest true thing | C14-08, 09, 10, 17, 18 | F3-P-01, F6-I-03 |
| S7 | Leaving, drifting, the lapsed; what was said to those who left; shunned for questions | C14-05, 06, 13; R-07, 10, 11 | F6-P-03/04 |
| S8 | Despair and depression in the world's words; a mind that will not quiet; tired of being good; people the life broke | C14-12, 21, 22, 24; R-08 | F4-P-01 |

**FAC items** C14-15 and C14-16 are Facilitator ground. For them the search asked only what the voice can say warmly and truthfully after the redirect. Results are in the FAC section below and under S8 in the JSON (`fac_followup`, run S9).

## Layer table

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R:h | R:l | L:l | R:h | R:m | R:h | R:h | R:l |
| cappadocian | R:h | R:m | R:l | R:h | R:m | R:h | R:m | R:h |
| desert | R:m | R:m | R:l | R:h | R:h | R\*:m | R:m | R:h |
| don | R:m | R:m | L:l | R:h | R:h | R:h | R:h | N:l |
| gallic | R:m | R:h | R:l | R:m | R:h | R:h | R:h | R:h |
| hal | R:h | R:h | R:m | R:h | R:h | R:h | R:m | R:h |
| ijc | L:m | R\*:m | L:l | R:h | R:h | R:h | R:m | R\*:l |
| lpc | R:m | R:h | L:h | R:m | R:h | R:h | R:h | R:h |
| pahc | R:m | R:h | L:l | R:h | R:m | R:m | R:m | R:m |
| rzg | L:m | R:l | L:m | R:m | R\*:l | R\*:m | R\*:l | R:m |
| syr | R:h | R:h | R:h | R:h | R:m | R:m | R:m | R:h |
| witt | R:m | R:m | R:l | R:m | R:m | R:m | R:l | R:m |

Forcing demos exist for F6-P-02 (cappadocian, desert, hal, pahc, syr), F1-P-01 (syr), F1-P-02 (alx), F4-P-01 (desert, gallic), F6-P-03 (gallic), F6-P-05 (don, ijc), F6-I-03 (cappadocian). **None exists for F4-P-03 (unanswered prayer), F6-P-04 (what to say to one who left), F4-P-02 (forgiving the unrepentant) or F3-P-01 (failing to hold your own accountable).**

Verification: 121 quote-record citations (about 70 distinct quotes) were matched verbatim against the vendored file named in their source record; **all MATCH**. 38 have an inline footnote, gloss or section numeral interrupting the run (each point recorded in `verified[].detail`); none diverged in wording.

## World by world

**alx.** Can say: suffering has three answers from inside it, the physician's pain, presence in the plague, honest silence (`alx.dw.suffering`, `alx.quote.dionysius-plague` MATCH npnf201 L41084); doubt aimed at understanding is hunger, not sin (`alx.quote.to-believe-or-disbelieve` MATCH anf02 L40327); Demetrius against Origen kept visible; John riding out after the robber, the fleet's best "what we said to one who left" (`alx.story.john-young-robber`). Thin: S2, S3, S8; no record on unanswered prayer, lament or despair; Origen's De oratione is vendored Greek only. Add: an honest_limit for S3/S8; a quote from Philocalia on providence (`origen_philocalia_lewis1911.txt`); Peter of Alexandria's canons on the lapsed (anf06) for S7.

**cappadocian.** Can say: where God was in the famine and on the pond (`demo.where-was-god`, `story.forty-sebaste`); tears allowed, despair refused, hope argued (`term.penthos-paraklesis`); overconfidence, not doubt, was the danger (`quote.basil-against-eunomius-ant` MATCH npnf208 L24124); graded penance and the 381 law owned (`quote.basil-canon-to-amphilochius` MATCH L36336); teachers who wanted stillness and rarely kept it (`quote.basil-on-his-retreat` MATCH L24024). Thin: S1 has no quote; S3; wanting to leave. Add: Nazianzen Oration 16 "On his Father's Silence, because of the Plague of Hail" (`npnf207` L27542), the world's one direct theodicy sermon, no record; Nyssa On Infants' Early Deaths (`npnf205`), the only patristic text on a dead child, whose source record has 0 citing records; Basil's Longer Rules on brothers who leave (`basil_ascetic-works-longer-shorter-rules_clarke1925.txt`).

**desert.** Can say: the noonday demon in the world's own words (`quote.the-noonday-demon` MATCH evagrius_praktikos L216); the sand running out of the basket (`quote.moses-sins-run-out` MATCH Budge v2 L1160); monks like hyenas (`quote.monks-like-hyenas`); Sarapion's "they have taken away my God" (`quote.they-have-taken-away-my-god` MATCH npnf211 L36051); and two honest limits, no first-person confession of doubt and no story of a community that harmed someone and made it right (`limit.doubt-and-doctrine`, `limit.communal-wrong-unrepaired`). Thin: S1 and S3 rest on a Contested demo. Add: Lausiac History 25-27 (Valens, Heron, Ptolemy: monks who fell or went back, `palladius_lausiac-history_clarke1918.txt`) for S7; Macarian Homilies on dryness for S2.

**don.** Can say: cover-up is in the court record, bishops writing "settle it quietly" while admitting the charge was true (`dw.hypocrites-and-those-who-left`); two rooms for doubt, Cirta and Tyconius (`dw.room-for-dissent`, `story.tyconius-condemnation`); Bagai violence is a named limit (`limit.bagai-violence-no-account`); the quiet drift back to the rival church is named as unrecorded (`limit.doubt-and-reception`). Thin: S3 (nothing in English; the passions are Latin, Tilley's translation in copyright). **S8 is NOTHING**: no record on despair, a restless mind or anyone the way of life broke. Add: an honest_limit for F4-P-01 in Donatist voice.

**gallic.** Can say: wanting to leave (`demo.want-to-leave`, the fleet's only F6-P-03 demo), cooling and the deserter (`quote.deserter-from-his-service` MATCH npnf211 L23521); accidie; Martin bearing with Brictio, "if Christ bore with Judas" (MATCH L5330); grief at a deathbed (`quote.martin-disciples-plea-and-his-reply`); Trier and the secular judge. Thin: S3, S4 (no F1-P demo; doubt is scruple or a teacher's error). Add: Cassian Conference VI "On the slaughter of some holy persons" (`npnf211`), the pastoral theodicy, no record; Conference IX.34-36 on prayers delayed or refused; Institutes IX "Of the spirit of dejection", named inside a term and nothing more.

**hal.** Strongest world for this cluster. Can say: Rome fell and the scholar's voice stuck in his throat (`quote.city-taken` MATCH npnf206 L26320); the crowd at Blaesilla's funeral calling the monks killers (`quote.detestable-monks` L8111); grief without limit rebuked as unbelief (`dw.doubt`); Marcella arguing back (`quote.dispute-to-learn`); "those of my own order"; Jerome's envy reported by Palladius; the attack of 416 with the attacker unnamed. Thin: S7 (leaving is only Fabiola's way back). Add: Ep. 14 to Heliodorus who left the desert (`npnf206` L4634, no source record); Ep. 60 and 123 (consolation; no source records); Ep. 125 (source record, 0 citing records) for S8.

**ijc.** Can say: hesitation at Nicaea itself (`quote.he-held-aloof-for-a-short-time` MATCH npnf202 L2972); Callinicum and Thessalonica, a bishop's arson and an emperor's penance (`demo.hypocrisy`, `quote.ambrose-dare-not-offer` L44181); forgiveness follows shown repentance (`quote.sin-is-not-done-away-but-by-tears`); the vigil "lest the people pine away in the tediousness of sorrow" (`quote.augustine-vigil-hymns` MATCH npnf101 L13765). **S1 is LOADED only**: no theodicy witness; the F6-P-02 cell is unforced here. S2 and S8 are honest limits (`limit.inner-life`). Add: Chrysostom's Letters to Olympias (`npnf109`, the era's great text on despondency, no source record); Homilies on the Statues (same file); Palladius' Dialogue (`palladius_dialogue-life-of-chrysostom_moore1921.txt`), a bishop bullied out of office, for S6.

**lpc.** Can say: Paul heard for salvation, not according to his wish (`witness.heard-for-salvation-not-for-wish`), the fleet's clearest unanswered-prayer teaching; apart in heart, united in body (`quote.apart-in-heart-united-in-body` MATCH npnf106 L15138); pardon through a wicked clergyman (L13008); the road back examined by name (`demo.road-back-examined`); the lapsed left nothing in their own words (`limit.the-lapsed-own-account`). **S3 is LOADED at high value**: Augustine's Enarrationes in Psalmos (`npnf108`, source record `lpc.source.augustine-expositions-on-the-psalms`, 0 citing records) is the richest lament text in the corpus and no record touches it. Add: a lament quote from Enarr. Ps. 21/41/87; Cyprian De mortalitate (English "On the Mortality" in `anf05`) for S1; Ep. 130 to Proba and Confessions IV/IX for S2.

**pahc.** Can say: put away doubting (`quote.put-away-doubting-from-you` MATCH anf02 L2386); a slow answer is not refusal (`witness.prayer-and-struggle`); Quintus lost his nerve (`story.quintus-recantation`); Pliny's lapsed of twenty years before (`story.pliny-interrogation`); Rome rebuking Corinth with Corinth's side lost (`witness.our-own-failures`). Thin: S1 rests on a Contested demo; S3; S6 has nothing on harm to children. Add: Hermas Mandate X (sadness "the sister of doubt and anger", `anf02`) for S3/S8; Similitudes VIII-IX (classes of apostates) for S7; an honest_limit on abuse, with Didache 2.2 as the one adjacent text.

**rzg.** Can say: Christ the mirror of election against dread (`quote.christ-the-mirror-of-election` MATCH schaff L667, `demo.predestination-and-dread`); and four honest limits (doubt-and-assurance, consistory-case-narrative, Marburg/Bolsec/Perrinist). Thin almost everywhere: **S1 and S3 are LOADED**, S5-S7 are limits with no case and no recorded words, grief has no record. **Servetus, the hardest true thing about Geneva, appears in no witness, limit or demo** though `rilliet_calvin-and-servetus_tweedie1846.txt` is vendored and mapped. Add: Institutes III.viii (bearing the cross) and I.xvi-xviii; Beza's Job Expounded (`beza_job-expounded_legatt1589.txt`, source record, 0 citing); Calvin's consolation letters (`calvin_letters-vol1/2/4_bonnet1858.txt`); a Servetus record. Identified only: the Consistory registers (copyright).

**syr.** Can say: the Jewish sage's taunt kept verbatim, "not one wise man whose prayer is heard" (`quote.a-man-called-wise-amongst-the-jews` MATCH npnf213 L27421), answered by the roll-call of the persecuted (`quote.aphrahat-persecuted-litany` L27954); faith as a building raised course by course (`quote.as-a-stonecutter` L27084); the Physician who is not scandalized by wounds (`dw.physician`, `quote.aphrahat-one-innocent` MATCH hallock L28); penitence as medicine (`quote.aphrahat-medicine-penitence` L29). Thin: S6 (nothing on cover-up, honestly). Add: Nisibene Hymns I-III, the city pleading with God under siege (`npnf213`), for S3; Demonstration VII On Penitents in full for S7.

**witt.** Can say: the terrified and comforted conscience (`gravity.terrified-and-comforted-conscience`); "in the old way we were never sure we were heard" (`term.assurance`); the cross as suffering sent, not chosen (`term.the-cross`); pastors negligent and people cold (`dw.cold-and-careless-among-us`, Contested); the 1543 treatise as the hardest true thing (`contested.1543-treatise-later-effect`). Thin: everything is terms and gravities; no quote on suffering or doubt; no F1-P demo. **Luther's Fourteen of Consolation (1520), the one text written for a suffering person, is vendored (`luther_works-v1-selected_jacobs-spaeth1915.txt` L59), has a source record and 0 citing records.** Add it; Table Talk on temptation and tribulation (`luther_table-talk_bell1886.txt`); "Aus tiefer Not" (`luther_hymns_bacon-allen.txt`). Identified only: Saxon visitation protocols and Melanchthon's Instructions for the Visitors (unvendored; German PD in Sehling and WA 26).

## FAC follow-up material per world

What the voice can say warmly and truthfully after the redirect. None of it is an answer to a crisis or advice.

- **alx**: plague nursing as presence (`story.plague-nursing`); honest silence over particular griefs. No grief vocabulary.
- **cappadocian**: strong. Tears allowed, despair refused (`term.penthos-paraklesis`); a brother weeping openly at his sister's deathbed (`story.macrina-deathbed`).
- **desert**: judgment refused (`quote.moses-sins-run-out`); a rule made for the weak; the heart as a deep gulf where grace and sin coexist.
- **don**: thin. Grief kept in the commemorative sermon (`dw.what-belonging-cost`); nothing on despair.
- **gallic**: Christ met in the beggar and the wounded Christ (`dw.the-christ-who-bears-the-wounds`); grief spoken aloud at Martin's death; the guest received (`quote.receiving-christ-in-you`).
- **hal**: grief allowed and consolation given (`dw.suffering`); Fabiola's hospital. For C14-16, hal alone renders a woman who left a violent husband (`quote.she-put-on-sackcloth`, Ep. 77.3, MATCH npnf206 L17449): history, never counsel.
- **ijc**: "let the sinner be glad in that he is invited to pardon" (`quote.leo-sinner-be-glad` MATCH npnf212 L14508); singing so sorrow would not wear them down.
- **lpc**: the shepherd wounded in the flock (`quote.shepherd-wounded-in-the-flock` MATCH anf05 L43724); Peter the sick man and the physician.
- **pahc**: "the multitude of His tender mercies" (`quote.put-away-doubting-from-you`).
- **rzg**: dread answered by looking away from the self to Christ (`demo.predestination-and-dread`). Nothing on grief.
- **syr**: the warmest in the fleet. The Physician exists for wounds; hiding the wound is the only fatal mistake (`dw.physician`, `quote.aphrahat-one-innocent`).
- **witt**: comfort as the rest of an accused conscience (`term.comfort`); death called a sweet sleep (`term.death`). Luther's own account of Anfechtung is loaded and unused.

No record in any world addresses a husband's violence directly. The vendored texts that do (Augustine Conf. IX.9, Basil Ep. 188 can. 9, Chrysostom Hom. 20 Eph. in `npnf113`) counsel endurance; they belong, if anywhere, in a Facilitator-governed note, not in a Representative's mouth.

## Other sources (public domain or open; not downloaded)

- Calvin, Commentary on the Psalms, tr. James Anderson, Calvin Translation Society 1845-49: PD, CCEL and archive.org. The Reformed lament text (rzg S3).
- Calvin, Sermons on Job, tr. Arthur Golding, 1574: PD (rzg S1).
- Bonnet, Letters of John Calvin vol. 3 (1858): PD, archive.org; vols 1, 2, 4 are vendored, vol. 3 is not.
- Zwingli, Pestlied (1519), English in S. M. Jackson, Huldreich Zwingli (1901): PD, archive.org.
- Luther's letters of consolation: Currie, Letters of Martin Luther (1908) and Smith and Jacobs, Luther's Correspondence, 2 vols (1913, 1918): PD, archive.org. Tappert's LCC 18 (1955) in copyright.
- Sehling, Evangelische Kirchenordnungen Bd. 1 (1902) and Unterricht der Visitatoren (WA 26): German, PD, archive.org (witt S6/S7); LW 40 in copyright.
- No PD English found for Chrysostom's To Stagirius and On Providence (French in Bareille 1865-73, PD; Greek vendored), Basil's "That God is not the author of evils" (PG 31), or Nazianzen's poems on his own life.
- Consistory registers (Kingdon 2000) and Tilley's Donatist Martyr Stories (1996): copyright; in WANTS.

Much of what the cluster needs is already vendored and unrecorded: Nazianzen Or. 16, Nyssa On Infants, Cassian Conf. VI and IX, Enarrationes, Letters to Olympias, Fourteen of Consolation, Beza's Job, Rilliet on Servetus.

## Not checked

- Record bodies below the front matter were not read in full; judgments rest on `statement`/`text`, `retrieve_when` and `use_note.means`.
- Vendored files were scanned by term; LOADED works were confirmed present by grep, not re-read for content.
- `canon/sealed_probes/` was not opened; C14-10's curriculum source was not traced.
- Rights in the "Other" list rest on edition dates and hosts, not re-checked page by page.
- Non-English vendored files were counted as loaded, not judged passage by passage.
