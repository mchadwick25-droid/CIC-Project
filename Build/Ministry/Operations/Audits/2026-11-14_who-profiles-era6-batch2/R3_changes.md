# R3 changes: era 6 batch 2

Applied under Mark's cap ruling of 2026-11-15 ("Fix + one check"), on branch `claude/cft-who-era6-batch2` (uncommitted). Review: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era6-batch2/R3_review.md`.

## Findings

- **D3-B1** (Palamas, 1351 tome): as worded, card `uncertain` and records claim "Combefis's note" with the new witness lines. MANSI26 l.10511-10524, 12063-12070, 12189, 19574, 19592-19597 reopened first.
- **B3-B1** (Clareno, Friday after Pentecost): as worded, card `dates`, card `uncertain` "When he died" and records claim "Ehrle's reckoning of the year". EHRLE1 l.27786-27798 reopened first.
- **B3-M3** (README Clareno line): as worded.
- **A3-M1** (Catherine, Gobelinus and Platina): as worded, brief para 4 and card `uncertain` 1. Also applied the review's records note for it: the claim "Scudder on the return…" gains "Gobelinus Paderbonensis officialis (MANSI26 l.111555-111556); Platina 'in vita ipsius Gregorii' (BIRGL l.98786-98787)", and those lines go into its witness.
- **A3-M2** (Bridget, Gobelinus and Platina): as worded, card `legacy.remembered` 4. Also applied the review's records notes: the same two witnesses go into the claim "Gobelinus, in Mansi's notice of Gregory XI…", and the Rome claim's citation changes from BIRGE l.955-961 to l.956-961 (l.955 is blank, checked).
- **B3-M1** (Clareno, Rader idiom): as worded.
- **B3-M2** (Clareno, Richard): as worded.
- **D3-M1** (Gregory of Sinai, records witnesses): as worded, in "Paisius on the copies…", the Basil claim and "Meyer 1894…". PAISZ l.3987-3994, 14215 and MEYER l.32-48 reopened first.
- **A3-M3** (README ranges): refreshed from `grade_text` after all fixes, to 405 to 407 words, grade 6.8 to 8.6, Flesch 61.4 to 71.5.
- **C3-B1, C3-B2, C3-M1, A3-B1** (Cabasilas), one merged fix as the ruling directs. GASS l.1364-1395, 1765-1800, 1880-1892, 1915-1940, PG150 l.26062-26075 and PO19 l.18200-18222 and 39860-39925 were reopened first. Differences:
  - Brief para 5 uses the ruling's draft wording exactly. That made the brief 412 words, so two cuts were made elsewhere in it. "the emperor's plan to leave the world for a monastery" became "…to leave the world", which also matches Kantakouzenos's ἐκ τοῦ βίου ἀναχώρησιν and the card's "plan to withdraw". "the followers of Gregory Palamas, standing up for them" became "…of Gregory Palamas". The brief is now 405 words. Neither cut adds a claim.
  - Card `role`: "archbishop of Thessalonica, by Fabricius and Gass, though Martin Jugie doubts it". This uses the ruling's "e.g." with "though … doubts it" in place of "which … doubts", because "which" had no clear antecedent.
  - Card `uncertain` 1: built from C3-B2's item text, retitled "Whether and when…", with A3-B1's Jugie sentences put after the Symeon sentence. A3-B1's second Jugie sentence ran to 30 words, so it is split in two: "He says neither … gives him that title. He thinks it came from confusion with Nilus."
  - Card `sources.about`: Jugie's entry is titled "…, in Patrologia Orientalis 19", the form of the Petit entry beside it. Its language is "French", in place of A3-B1's "French and Greek", because the entry is the introduction, which is in French.
  - Records claim "Archbishop": C3-B1's Palamas line and widened GASS lines are applied as worded, and so is C3-B2's note that the Synodikon gives a first name with no surname. The claim is retagged Contested and gains PO19 l.39892-39895, 39907-39908, 39914 in its witness. C3-B2's relabel of "Against or silent" to "Bounds and silence" rested on "no held line argues against the see", which Jugie now does. So the claim has "Against: Martin Jugie …" (his words, with the OCR "soufllent" and "avee Nil" noted, and his note citing Petit's 1918 Synodicon article), then "Bounds and silence:" for Kantakouzenos and Symeon.
  - Records `contested_claims`: the claim is "Whether and when he became archbishop of Thessalonica", with three sides: Fabricius (C3-M1's text); Gass (C3-M1's text, plus his reading of the Synodikon's Nicholas, GASS l.1884-1888, 1919-1938); and Jugie, "No" (A3-B1's text). Kantakouzenos and Symeon stay in the "Archbishop" claim, as C3-M1 directs.
  - Records `absent_details`, "The date he took the see of Thessalonica". This edit follows from the others. "No line … says he never held it" no longer stands beside Jugie, so the note now reads "No line gives the date he took the see; Jugie doubts he held it at all (PO19 l.39892-39895). Searched …".
  - README Cabasilas line: A3-B1's replacement, corrected so that Gass does not have him succeed directly and the Thessalonica record names only a Nicholas, as C3-B2 found.
- **Not changed, for the cap check to note.** The records claim "Gass: 'unter den Anhängern des Palamas genannt…'" still says "the Thessalonica Synodikon praises him". That rests on Gass's same identification of the Synodikon's Nicholas. No finding names this claim, so it was left as it stands.

Audio: `catherine-of-siena` and `nicholas-cabasilas` were rebuilt from their briefs, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Once the tags are stripped, all eight audio files equal their briefs (checked by script). All nine JSON files parse. `tools/check_spelling.py` found 0 issues in the briefs, the cards and the README.

## Strings for the cap check

**catherine-of-siena.brief.txt, para 4, last sentence:**
A life of Gregory in Mansi's collection of church councils says Gobelinus of Paderborn credited his return to Bridget's revelations.

**catherine-of-siena.card.json, `uncertain` 1, the changed sentences:**
A notice of Gregory's life in Mansi's collection of church councils names other causes. Gobelinus of Paderborn credits Bridget's revelations. Platina, in his life of Gregory, tells of a bishop's retort that hastened the return.

**bridget-of-sweden.card.json, `legacy.remembered` 4:**
A notice of Gregory XI's life in Mansi's collection of church councils says Gobelinus of Paderborn credited his return to Rome to her revelations. They reached him through Alphonso. Platina, in his life of Gregory, gave another cause.

**angelo-clareno.card.json, `dates`, last two sentences:**
The year is Ehrle's reckoning, from a note dated to the Friday after Pentecost, which was also the feast of Saint Anthony, 13 June. Daniel Papebroch, a Bollandist, had found the years in which that Friday fell on 13 June.

**angelo-clareno.card.json, `legacy.traces`, the changed sentence:**
Rader grants that Ambrose does not give his name, and says the description makes plain who is meant.

**angelo-clareno.card.json, `uncertain`, authorship item, the changed end:**
… and Ehrle reports doubts from Richard, writing in 1884, and from Professor Felice Tocco.

**angelo-clareno.card.json, `uncertain` "When he died", first two sentences after the heading:**
Ehrle fixed 1337 from a note at the end of the list of his miracles, dated to the Friday after Pentecost and the feast of Saint Anthony, 13 June. Daniel Papebroch, a Bollandist, had already found that in the first half of the fourteenth century the Friday after Pentecost fell on 13 June only in 1317, 1337 and 1348.

**gregory-palamas.card.json, `uncertain`, the changed sentence:**
François Combefis, a Dominican, annotates the tome of 1351 in Mansi and calls it heretical.

**nicholas-cabasilas.brief.txt, para 3, the two cut sentences:**
In 1349 Cabasilas and Demetrios Kydones joined the emperor's plan to leave the world.
Gass finds him named among the followers of Gregory Palamas.

**nicholas-cabasilas.brief.txt, para 5:**
Fabricius says he succeeded his uncle as archbishop of Thessalonica. Gass also makes him archbishop, after Gregory Palamas held the see. Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof and thinks the title came from confusing him with Nilus.

**nicholas-cabasilas.card.json, `role`:**
Layman of the imperial household, by Kantakouzenos's account; envoy; theologian of the sacraments; archbishop of Thessalonica, by Fabricius and Gass, though Martin Jugie doubts it

**nicholas-cabasilas.card.json, `uncertain` 1:**
Whether and when he became archbishop of Thessalonica. Fabricius says he succeeded his uncle Nilus in that office after Nilus died, and Migne heads him as metropolitan of Thessalonica. Gass puts Gregory Palamas in the see between uncle and nephew. Gass presumes Nicholas took it only some years after the synod of 1351, and finds him named archbishop no earlier than 1354. A record of the church of Thessalonica, quoted by Gass, calls a Nicholas its most holy metropolitan, and Gass takes him for Cabasilas. Kantakouzenos calls him still a layman in 1353. Symeon of Thessalonica praises him and names no see. Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof that he succeeded Nilus. He says neither Kantakouzenos, nor the titles in the manuscripts, nor the record of the church of Thessalonica gives him that title. He thinks it came from confusion with Nilus. No witness gives the date or tells how he took office.

**nicholas-cabasilas.card.json, `sources.about`, new entry:**
title "Homélies mariales byzantines II: Nicolas Cabasilas, introduction, in Patrologia Orientalis 19"; author "Martin Jugie (ed.)"; date "1926"; language "French"; file `cic/texts/john-ephesus_lives-eastern-saints-po19-mixed-issue_brooks1926.txt`

**README.md, para 3, the changed sentences:**
The briefs run 405 to 407 words, about 2:30; the 2:30 is a cap, not a target. `grade_text` scores them at grade 6.8 to 8.6 and Flesch Reading Ease 61.4 to 71.5.

**README.md, Clareno bullet, the changed sentence:**
His death year is Ehrle's reckoning, using Papebroch's list of the years in which the Friday after Pentecost fell on 13 June, and the card says so; the Bollandists give 14 June for the day.

**README.md, Cabasilas bullet:**
**Nicholas Cabasilas** opens on the patriarchal election of 1353, where Kantakouzenos calls him still a layman. How he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he, which anti-Latin writings are his, and whether and when he became archbishop of Thessalonica are tagged Contested. Fabricius has him succeed his uncle in the see. Gass makes him archbishop after Gregory Palamas held it, and takes a Nicholas named in a Thessalonica record for him. Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof. No held line gives a date. Gregoras's old friend is Boivin's identification, followed by Gass.

## Grades after all fixes

| Brief | Words (`wc -w`) | FK | Flesch |
|---|---|---|---|
| angelo-clareno | 406 | 8.16 | 62.55 |
| bernardino-of-siena | 405 | 7.21 | 69.87 |
| bridget-of-sweden | 405 | 6.85 | 68.68 |
| catherine-of-siena | 405 | 6.79 | 71.51 |
| gregory-of-sinai | 406 | 8.59 | 63.48 |
| gregory-palamas | 407 | 7.77 | 63.26 |
| nicholas-cabasilas | 405 | 8.00 | 61.37 |
| william-of-ockham | 405 | 8.07 | 63.19 |

- Records, the claim "Gass: unter den Anhängern des Palamas genannt…" (the fixer's open note): "the Thessalonica Synodikon praises him against" now reads "the Thessalonica Synodikon praises a Nicholas, whom Gass takes for him, against", the same identification fix as C3-B2 (GASS l.1884-1888).
