# Fixes: Benedict of Nursia

Applied from `Outline_Check.md`, findings 1–4 (all MINOR; no BLOCKING).

## Applied verbatim

1. **Finding 1 (the abbot in the first minute).** `Outline.md` line 21, beat 1: "For monks living together under an abbot the community chooses, he wrote a rule (M18, R2, R6)" replaces "For his monks he wrote a rule (M18)". The sentence "He called it 'this little Rule written for beginners' (R8; RBE 4297–4300)" is removed from beat 1 and goes to beat 2 as the wording of finding 2.
2. **Finding 2 (the pointer for "little Rule for beginners").** `Outline.md` line 22, beat 2, after the guest sentence and before "Documented (OWN).": "He called it 'this little Rule written for beginners', and pointed those who wanted more to Basil's Rule and the Collations, Institutes and Lives of the Fathers (R8; RBE 4290–4300)." (RBE 4290–4300 checked: "Co//ations of the Fathers, their Institutes, their Lives, and the Rule of our Holy Father St. Basil ... this little Rule written for beginners".)
3. **Finding 3 (the Connection).** `Outline.md` line 40: "What the listener needs: Benedict wrote a rule for monks, but no source has him make it binding beyond his own houses, and there was no order in his lifetime. Frankish rulers two centuries later took up his book and made it the measure of the monasteries in their lands." replaces the two sentences the check named.

## Worded by me

1. **Finding 4 (Library sweep).** New section "Library sweep", `Source_Sheet.md` lines 223–228. Exact text:

   > ## Library sweep
   >
   > Added 2026-11-18, from the outline check's finding 4. Two held files, both vendored on 2026-11-13, were not in the sheet.
   >
   > - **ARDO** = `cic/texts/benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt`. Migne, PL 103 (1851). It holds Ardo's Life of Benedict of Aniane, "Auctore ARDONE 8eu [seu] SMARAGDO ejus discipulo" (ARDO 28358–28361), and Benedict of Aniane's *Concordia regularum* (from ARDO 58286), which sets the Rule beside other rules. The editor says Ardo wrote while Louis the Pious was still alive (ARDO 28395–28396). **Bears on I1: yes.** Ardo says the emperor set Benedict of Aniane over all the monasteries of his realm (ARDO 30632–30635), gathered the fathers of the monasteries with many monks (ARDO 30640–30642), had the Rule discussed "ab integro" (ARDO 30643), and confirmed a capitulary for "omnibus in regno $u0 [suo] positis monasleriis [monasteriis]" (ARDO 30650–30651), with inspectors sent to each monastery (ARDO 30653–30654); "una cuyctis [cunctis] generaliter posita observatur Regula" (ARDO 30658–30659). LATER. Documented as Ardo's account. The year, 817 at the synod of Aachen, is the editor's note (ARDO 30672). It carries I1 past 802, under Louis; it changes no claim in the outline. Added to the card's sources.
   > - **RC** = `cic/texts/regularis-concordia_de-consuetudine-monachorum-in-anglia-13-lat-ang_logeman1891.txt`. Logeman's edition of the *Regularis Concordia*, the agreement on monks' customs in England, Latin with its Old English gloss (*Anglia* 13, 1891). It says abbots and abbesses received "Regulari itaque sancii [sancti] patris benedicti norma ... honestissime suscepta" (RC 21683–21685). **Bears on I1: no.** I1 is the Frankish councils; this is England. It is a witness to the Rule's later reach and could serve I2 on a later rework. Not added to the card.

   Checked in the files at those lines: ARDO 28358 "VITA S. BENEDICTI ANIANENSIS", 28361 "Auctore ARDONE 8eu SMARAGDO ejus discipulo"; 28395–28396 "superstite Ludovico Augusto"; 30632–30635 "Praefecit eum quoque imperator cunctis in regno suo coenobiis ... Franciam"; 30640–30643 "aggregatis coenobiorum Patribus una cum quampluribus monachis ... Regulam ab integro discutiens"; 30649–30651 the capitulary "imperatori confirmandum ... ut omnibus in regno suo positis monasteriis observare praeciperet"; 30653–30654 "inspectoresque per singula posuit monasteria"; 30658–30659 the "una ... Regula" line; 30672 the editor's "Id factum anno 817, in synodo Aquisgranensi"; 58286 "CONCORDIA REGULARUM". RC 21683–21685: "Regulari itaque sancii patris benedicti | norma ... honestissime suscepta . tarn abbates perplurimi . quam abba[tissae]"; file header names Logeman's *De consuetudine monachorum*, *Anglia* XIII, 1891. "The agreement on monks' customs in England" is my gloss of the title *De consuetudine monachorum in Anglia*.
2. **Finding 4 (card, since ARDO bears on I1).** `benedict-of-nursia.card.json` lines 85–90, a new entry in `sources.about`: `{"title": "Life of Benedict of Aniane, with Benedict of Aniane's Concordia regularum, in Patrologia Latina 103", "author": "Ardo", "language": "Latin", "file": "cic/texts/benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt"}`. No other card field changed.

## Not applied

None.
