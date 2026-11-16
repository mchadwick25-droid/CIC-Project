# Comparison of renderings A and B, G1 to G12

Independent Opus comparison. No model or API calls; no repo file changed.

Latin sources checked (OCR normalised here; line numbers are in the vendored files):
- Gregory of Tours: `cic/texts/gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt`
- The Rule: `cic/texts/benedict_rule-of-st-benedict-lat-eng_hunter-blair1907.txt`
- Dialogues II: `cic/texts/acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt`
- Paul the Deacon: **no Latin text of the Historia Langobardorum is held** in `cic/texts`. Only Foulke's English (1907) is vendored. Searched for the Latin title, "Langobard", "reverendi viri Gregorii" and "Gregorii Turonensis episcopi"; the only hits are other works. AASS Maii t.5 (St Hospitius, l.57387) mentions Paul but does not quote this line.

Neither renderer had the Dialogues Latin; both recalled it from memory. It is now checked: their recall was right for G8 and G12.

---

## G1 (Gregory of Tours, cathedral)

- Printed (Dalton 1927, l.22653-22660): "all ruined and destroyed by the fire."
- A: "all ruined and destroyed by the fire." (unchanged)
- B: "all in ruins, wrecked by the fire."
- Latin (HF X.31, l.35057): "ab incendio dissolutam dirutamque nanctus sum" = "I found it broken apart and torn down by fire." No word for "all". "The fire" is fair: a few lines earlier (l.35046) the Latin tells how in Eufronius' time "civitas Turonica cum omnibus ecclesiis magno incendio concremata est", so this points back to that great fire.
- Verdict: **same**.
- FINAL: "ruined and destroyed by the fire."
- Brief fit: When he arrived, he found his cathedral "ruined and destroyed by the fire."
- Note: Both A and B keep Dalton's "all", which the Latin lacks; the FINAL drops it to follow the original.

## G2 (Gregory of Tours, lament)

- Printed (Brehaut 1916, l.844-851): "Woe to our day, since the pursuit of letters has perished from among us,"
- A: "Alas for our times, because the study of literature has died out among us,"
- B: "Alas for our times, because the study of letters has died out among us,"
- Latin (HF Pref., l.2548-2549): "Vae diebus nostris, quia periit studium litterarum a nobis" = "Woe to our days, because the study of letters has perished from us."
- Verdict: **minor**. "Literature" narrows "litterae" (literary learning and the skill of writing) toward a body of texts; "letters" keeps the full range but may be misread today as mail. No claim changes.
- FINAL: "Alas for our times, because the study of literature has died out among us,"
- Brief fit: People lamented, he says, "Alas for our times, because the study of literature has died out among us," so he wrote ten books of History himself...
- Card note: "litterae" means literary learning and skill in writing; A reads "literature", B "letters" — both readings kept.

## G3 (Gregory of Tours, creed)

- Printed (Dalton, l.333-340): "that whoso reads may doubt not that I hold the catholic faith,"
- A: "so that anyone who reads this may have no doubt that I hold the catholic faith,"
- B: "so that no reader may doubt that I hold the catholic faith,"
- Latin (HF I Pref., l.2736-2739): "prius fidem meam proferre cupio, ut qui legerit me non dubitet esse catholicum" = "so that whoever reads may not doubt that I am catholic." Dalton's "hold the catholic faith" fairly renders "esse catholicum" next to "fidem meam"; a bare "am catholic" would mislead a modern reader toward a denomination or toward "broad-minded".
- Verdict: **same**. (A's "this" adds an object the Latin leaves implied; no change of sense.)
- FINAL: "so that anyone who reads may have no doubt that I hold the catholic faith,"
- Brief fit: He opened them with his creed, "so that anyone who reads may have no doubt that I hold the catholic faith," and a king put that faith to the test.

## G4 (Gregory of Tours, Chilperic's demand)

- Printed (Dalton, l.10364-10371): "This is my will, that such be thy faith, and that of the other doctors of the Church."
- A: "It is my will that this be your faith, and the faith of the other teachers of the Church."
- B: "This is what I want: that you believe this, and so do the other teachers of the Church."
- Latin (HF V.44, l.18773-18774): "'Sic', inquid, 'volo, ut tu vel reliqui doctores ecclesiarum credatis'" = "This is how I want you and the other teachers of the churches to believe." "Credatis" is a verb (believe), not a noun; "ecclesiarum" is plural.
- Verdict: **same**.
- FINAL: "I want you and the other teachers of the churches to believe this."
- Brief fit: ...and told Gregory, "I want you and the other teachers of the churches to believe this." Gregory refused.
- Note: The FINAL follows the Latin in two points both A and B passed over: the verb "believe" (B has it, A keeps Dalton's noun) and the plural "churches" (both kept Dalton's singular).

## G5 (Gregory of Tours, Hilary and Eusebius)

- Printed (Dalton, l.10368-10375): "that which Hilary and Eusebius taught."
- A: "what Hilary and Eusebius taught."
- B: "what Hilary and Eusebius taught."
- Latin (HF V.44, l.18776-18777): "quod Elarius Eusebiusque docuerunt" = "what Hilary and Eusebius taught."
- Verdict: **same** (identical).
- FINAL: "what Hilary and Eusebius taught."
- Brief fit: The king must hold to "what Hilary and Eusebius taught."

## G6 (Gregory of Tours, the king gives up)

- Printed (Dalton, l.10398-10405): "So the king desisted from his purpose,"
- A: "So the king gave up his plan,"
- B: "So the king gave up his plan."
- Latin (HF V.44, l.18797): "Et sic rex ab hac intentione quievit" = "And so the king rested from this intention." The edition's own index (l.83992) glosses "quiescere = abstinere" here.
- Verdict: **same**.
- FINAL: "So the king gave up this plan,"
- Brief fit: "So the king gave up this plan," Gregory writes.
- Note: "hac" is "this"; Dalton's "his" is a fair gloss but the FINAL follows the Latin.

## G7 (Paul the Deacon on Gregory)

- Printed (Foulke 1907, l.5068-5075): "the books of the reverend man Gregory, bishop of Tours."
- A: "the books of that revered man, Gregory, bishop of Tours."
- B: "the books of that revered man Gregory, bishop of Tours."
- Latin: **not held.** No Latin Historia Langobardorum is in `cic/texts`, so the Latin could not be checked. Both renderers' guess "reverendi viri" is unverified.
- Verdict: **same** (A's extra comma only).
- FINAL: "the books of that revered man Gregory, bishop of Tours."
- Brief fit: Two centuries later the historian Paul the Deacon sent readers to "the books of that revered man Gregory, bishop of Tours."
- Note: Checked against Foulke's English only. "Reverend" is rendered "revered" so it does not read as the modern clergy title; confirm against a Latin edition (MGH SRL, 1878) once one is vendored.

## G8 (Benedict to Totila)

- Printed (Gardner 1911, l.4466-4473): "Much wickedness do you daily commit."
- A: "Every day you do much evil."
- B: "You do much evil every day."
- Latin (Dial. II.15, AASS Mart. III l.79157-79162): "Multa mala facis, multa mala fecisti" = "You do many evil things; you have done many evil things." **No word for "daily".** The span covers only the first clause, "Multa mala facis".
- Verdict: **same** between A and B. Both keep "daily", which the Latin lacks.
- FINAL: "You do many evil things."
- Brief fit: When the Gothic king Totila came to him, Benedict told him, "You do many evil things." From then on, Gregory says, the king was less cruel.
- Note: "daily" is the 1608 English translator's word; both renderers flagged it from memory, and the Latin now confirms it is absent, so the FINAL drops it.

## G9 (The Rule, Prologue)

- Printed (Gasquet 1925, l.763-770): "a school for the service of God, in which we hope nothing harsh nor burdensome will be ordained."
- A: "a school for the service of God, in which we hope to set down nothing harsh or hard to bear."
- B: "a school for the service of the Lord. In setting it up, we hope to lay down nothing harsh and nothing heavy." (B's one-sentence option: "a school for the service of the Lord, and in setting it up we hope to lay down nothing harsh and nothing heavy.")
- Latin (Prol., l.1242-1245): "Constituenda est ergo nobis dominici schola servitii; in qua institutione nihil asperum, nihil grave nos constituturos speramus." = "We must therefore found a school of the Lord's service; in founding it we hope to lay down nothing harsh, nothing heavy."
- Verdict: **minor**. A ties "in which" to the school (as Gasquet does); B follows "in qua institutione", the act of founding it. A has "God", B has "the Lord" ("dominici"). No claim changes.
- FINAL: "a school for the Lord's service, and in setting it up we hope to lay down nothing harsh and nothing heavy."
- Brief fit: In it he founds "a school for the Lord's service, and in setting it up we hope to lay down nothing harsh and nothing heavy."
- Card note: A reads "in which" as the school and says "God"; B reads it as the founding ("institutione") and says "the Lord" ("dominici") — both readings kept.

## G10 (The Rule, ch. 58, the promise)

- Printed (Gasquet, l.3589-3596): "stability, amendment of manners and obedience,"
- A: "stability, a change of his way of life, and obedience,"
- B: "stability, a reformed way of life, and obedience,"
- Latin (ch. 58, l.8568 ff.): "promittat de stabilitate sua, et conversione morum suorum, et obedientia" = "let him promise his stability, the turning of his ways, and obedience." This edition reads "conversione"; many manuscripts read "conversatione" (faithfulness to the monastic way of life). Which reading is original is contested.
- Verdict: **minor**. A's "change" is neutral, close to "conversio" (a turning). B's "reformed" leans to moral improvement, as Gasquet's "amendment" does, and "reformed" can carry a denominational echo today. Both follow the "conversio" reading; neither takes up "conversatio". No claim changes.
- FINAL: "stability, a changed way of life, and obedience,"
- Brief fit: His monks promise "stability, a changed way of life, and obedience," and divide their days... (A's "his" would clash with "His monks" in the brief and could be read as Benedict's; the FINAL leaves the possessive implicit, as Gasquet does.)
- Card note: "conversio morum" is a turning of one's way of life (A: "a change", B: "reformed"); some manuscripts read "conversatio", the monastic way of life itself — both renderings kept, and the variant is contested.

## G11 (The Rule, ch. 64, the abbot's measure)

- Printed (Gasquet, l.3954-3961): "that the strong may have their scope and the weak be not scared."
- A: "that the strong have something to strive for and the weak are not frightened away."
- B: "that the strong have something to reach for and the weak are not driven away."
- Latin (ch. 64, l.9526-9528): "sic omnia temperet, ut et sit quod fortes cupiant, et infirmi non refugiant" = "let him so balance all things that there is something the strong long for and the weak do not run from."
- Verdict: **minor**. "Refugiant" is something the weak do themselves (flee, shrink back). A's "frightened away" keeps that; B's "driven away" makes them pushed by someone. Both "strive for" and "reach for" add a sense of effort to "cupiant" (desire, long for). No claim changes.
- FINAL: "that the strong have something to long for and the weak do not run away."
- Brief fit: The abbot must so temper all things "that the strong have something to long for and the weak do not run away."
- Card note: "refugiant" = the weak flee of themselves (A: "frightened away"); B's "driven away" implies an outside push — both readings kept.

## G12 (Gregory the Great on the Rule)

- Printed (Gardner, l.5561-5568): "excellent for discretion and also eloquent for the style,"
- A: "outstanding for its sound judgement and also eloquent in its style,"
- B: "outstanding for its wise moderation and fine and clear in its language,"
- Latin (Dial. II.36, AASS Mart. III l.80435-80436): "scripsit monachorum Regulam, discretione praecipuam, sermone luculentam" = "he wrote a Rule for monks, outstanding in discretion, clear in its language." No word for "also".
- Verdict: **minor**. "Discretio" covers both discernment and a sense of measure: A picks "sound judgement", B "wise moderation". "Luculentus" is clear, bright, well expressed: A's "eloquent" leans toward fine speaking, B's "fine and clear" uses two words for one. No claim changes.
- FINAL: "outstanding for its sound judgment and clear in its language,"
- Brief fit: Gregory, by then pope, praised the Rule as "outstanding for its sound judgment and clear in its language," though by the time he wrote...
- Card note: "discretio" is judgment and a sense of measure (A: "sound judgement", B: "wise moderation"); "luculentus" is clear rather than eloquent — both readings kept. The FINAL drops Gardner's "also", which the Latin lacks.

---

## Summary

| G | Verdict | FINAL |
|---|---|---|
| G1 | same | "ruined and destroyed by the fire." |
| G2 | minor | "Alas for our times, because the study of literature has died out among us," |
| G3 | same | "so that anyone who reads may have no doubt that I hold the catholic faith," |
| G4 | same | "I want you and the other teachers of the churches to believe this." |
| G5 | same | "what Hilary and Eusebius taught." |
| G6 | same | "So the king gave up this plan," |
| G7 | same (Latin not held) | "the books of that revered man Gregory, bishop of Tours." |
| G8 | same | "You do many evil things." |
| G9 | minor | "a school for the Lord's service, and in setting it up we hope to lay down nothing harsh and nothing heavy." |
| G10 | minor | "stability, a changed way of life, and obedience," |
| G11 | minor | "that the strong have something to long for and the weak do not run away." |
| G12 | minor | "outstanding for its sound judgment and clear in its language," |

No G was judged "changes meaning".
