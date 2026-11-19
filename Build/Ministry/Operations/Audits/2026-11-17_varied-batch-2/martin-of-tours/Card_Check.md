# Card check: Martin of Tours

New card: `martin-of-tours.card.json` (this folder). Old card: `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch3/martin-of-tours.card.json`. Checked against `Source_Sheet.md` and the cited source files. Bar: `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Process.md`.

**Verdict: FIX**

## BLOCKING

B1. **Quotation 1 (Life 4), `originalLines` is wrong.** The card gives `6336-6337`. In `cic/texts/sulpicius-severus_libri-qui-supersunt-chronica-vita-martini-lat_halm1866-csel1.txt`, "Christi ego" stands at the end of line 6335; line 6336 is blank; "miles snm: pugnare mihi non licet." is line 6337. The cited range does not hold the start of the quoted Latin.
Correction: `"originalLines": "6335-6337"`.

B2. **Quotation 2 (Chronicle II.50), `originalLines` is wrong.** The card gives `5905-5906`. In the same Halm file, "saeunm esse et inauditum nefas, nt cansam eccle-" is line 5905; line 5906 is blank; "aosiae iudex saeculi iudicaret." is line 5907. The cited range stops before the end of the quoted Latin.
Correction: `"originalLines": "5905-5907"`.

## Checked and sound

- Quotation 1 printed wording, NP11 841–842: "I am the soldier of Christ: it is not lawful for me to fight." Verbatim. Latin reading (OCR "snm" = sum) as the card notes. Modern wording matches the brief exactly.
- Quotation 2 printed wording, NP11 11658–11660: "it was, besides, a foul and unheard-of indignity, that a secular ruler should be judge in an ecclesiastical cause." Verbatim (the cited 11657–11660 includes it). Latin reading *saeuum* and the apparatus "Beanm P, nonum b" (HALM 5924) confirmed. Modern wording matches the brief exactly, and is a fair rendering of the Latin.
- Dialogue III.13 (NP11 5193–5219): communion "of that day", refusal to sign, "He lived sixteen years after this, but never again did he attend a synod". Verbatim.
- Dates: Brehaut "November 8, 397" (GT 595); burial "the third day before the Ides of November" (GT 2213); the Gregory/Sulpicius age conflict (sheet D1). Supported.
- Place: Pannonia "In Hungary" (Brehaut), Ticinum = Pavia (Roberts), Candes "a village of his diocese" (GT). Supported.
- Legacy: Perpetuus and the feast (GT 2194–2213); Brehaut "chief point of Christian pilgrimage in Gaul" (GT 128–129); Clovis's edict, gifts and consul's purple (GT 2608–2611, 2705–2711); Gregory at the Paris council, bishops silent, Maximus (GT 5790–5818); the Life sold in Rome, read in Carthage, Alexandria, Egypt (NP11 3638–3650); many monks made bishops (NP11 1152–1158); about two thousand monks "said" (NP11 2493); Fortunatus "militis alba chlamys plus est quam purpura regis" (VF 25051). All verbatim or faithful.
- Uncertainties: Sulpicius published the Life in Martin's lifetime (sheet D2); the Roberts mistranslation (D3); the three Trier accounts (D5); Condate/Candes (D6). All match the sheet.
- Card agrees with the brief; every brief claim has a reference line.

## Not blocking

- The `dates` field has no closing full stop.

## Recheck

B1: quotation 1 `originalLines` is now "6335-6337". HALM 6335 holds "Christi ego" and 6337 holds "miles snm: pugnare mihi non licet."
B2: quotation 2 `originalLines` is now "5905-5907". HALM 5905 holds "saeunm esse ... nt cansam eccle-" and 5907 holds "aosiae iudex saeculi iudicaret."
Both ranges now hold the full quoted Latin.

**Recheck: PASS**
