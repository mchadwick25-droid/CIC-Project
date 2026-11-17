# Card check: Marcion of Pontus

New card `marcion-of-pontus.card.json` compared with `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era1/batch1/marcion-of-pontus.card.json`. Every changed or added claim was checked against `Source_Sheet.md` and the cited lines. All four quotations were re-read in their files.

**Verdict: FIX** (one blocking finding)

## Quotations

| # | Modern (matches brief) | Printed wording re-read | Result |
|---|---|---|---|
| 1 | "Do you know me?" | ANF 39883, "Dost thou know me?" | Verbatim |
| 2 | "I do know you: the firstborn of Satan." | ANF 39884, "I do know thee, the first-born of Satan." | Verbatim. Lines 39883–39884 are right. The hostile words are left as Polycarp's, in Irenaeus's report |
| 3 | "Even now he is still teaching ... greater than the Creator." | JG 730–731, "ὃς καὶ νῦν ἔτι ἐστὶ διδάσκων τοὺς πειθομένους, ἄλλον τινὰ νομίζειν μείζονα τοῦ δημιουργοῦ θεόν" | Verbatim. The ANF English given in the note matches ANF 14943–14945. The rendering is faithful |
| 4 | "Separating the law from the gospel is Marcion's own work, and his chief one." | OEH 4337–4338, "Separatio legis et evangelii pro-/prium et principale opus est Marcionis" | Verbatim, with the line-break hyphen joined. The ANF English matches T 23734–23736 |

Each modern wording matches the brief exactly.

## Changed claims

The following are supported: otherNames, and uncertain line 9 on Sinope (Holl's note at EPI 7496–7497 names Filastrius as dependent on Epiphanius); dates (S2); place (S1); role; knownFor (S5, S3, M1, M4, I1); legacy traces and remembered (I1, I2, I3, I4, I6, M8); all nine uncertain lines (N2, M3, S5, M1, M2, M10, M9, M5, M6, D1, D3, S1); sources; briefReferences, whose line numbers match the sheet. A brief of 374 words gives about 2 minutes 30 seconds. The opponents' charges stay theirs, and the claimed Marcionite martyrs keep Eusebius's hedges ("appears to have been", "it is reported").

## BLOCKING

1. **keyWorks[0].about: "known only through Tertullian" is unsupported.** The writer added "only". The sheet does not support it, and the Library holds another answer to the Antitheses: the anonymous verse *Five Books in Reply to Marcion*, Book IV, headed "Of Marcion's Antitheses" (`cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, lines 15683–15685; the sheet lists it as held but not used, N4). Exact correction:
   - Replace: `"contradictory propositions" setting the gospel against the law. It is lost and known only through Tertullian of Carthage's answer, as is a letter of his that Tertullian cites`
   - With: `"contradictory propositions" setting the gospel against the law. It is lost and known chiefly through Tertullian of Carthage's answer; a letter of his is known only because Tertullian cites it`

## Non-blocking

- otherNames says Sinope is "named only by Epiphanius". uncertain line 9 adds that Filastrius, who depends on him, also names it. The two lines agree in substance and the card already carries the fuller qualification.

**Recheck (2026-11-17): PASS.** keyWorks[0] now carries the correction word for word, and no other field changed; the only other difference is a newline at the end of the file.
