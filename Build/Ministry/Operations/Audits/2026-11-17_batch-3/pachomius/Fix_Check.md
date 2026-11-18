# Pachomius: fix check

Targeted check of `pachomius.brief.txt` against `Recheck_2.md`, `Outline.md` and the cited source lines in `cic/texts/`.

## Verdict: PASS

## 1. Birth date (Recheck_2 BLOCKING 1): fixed
Now: "Born to pagan parents, he was taken at about twenty for Constantine's war, early in the fourth century." This is the outline's wording (Setting, line 11; Do not say, lines 78-79). The date now sits on the conscription, not the birth. Sources: Bohairic, Amélineau 5093-5101 (after the persecution, Constantine king, "pris alors qu'il avait vingt ans"); Greek, Acta 80977-80983 ("Cum finem deinde accepisset persecutio regnavit Constantinus ... vigesimum tunc circiter agens aetatis suae annum"). Pagan parents: S1 (Greek 86417). The sentence names no enemy and no year. It says no more than the sources.

## 2. Opening split: clean
"... the great hermit Antony speaks to Pachomius's monks after his death. He tells them: ..." Heard once, it is clear who speaks and who "your father" is. Quote 1 matches Outline quote 1 word for word. It renders Acta 86887-86893 faithfully ("nullum uspiam extabat coenobium ... persecutione jam finita, privatim ... Postea vero Pater vester tantum bonum, Deo adjuvante, effecit"). "The great hermit" is supported by 86884-86886.

## 3. Trims: no fact changed, no must-tell lost
- "Nine monasteries came to form one fellowship": "along the Nile" is cut, and Upper Egypt is already given.
- Esneh: only one attribution is left ("the Greek Life says"). The questioning, the intent to kill and the rescue are all kept, and bishops and sword stay in separate sentences (beat 6; Do not say line 97).
- "Freed and baptized": same facts as "Once free and baptized" (E3).
- "Locked up, he asked who the strangers feeding the recruits were": faithful to Amélineau 5139-5146.
- The split, Theodore's letters, Eustochium's nuns and the order Palladius-then-Jerome are all kept (Do not say lines 90-92).

## 4. Heart in the first 150 words: yes
"Pachomius drew such monks into one shared life under one written rule" ends at word 114. The houses, clothes, table and work follow, and "one fellowship" ends at word 150.

## 5. Score
`python -m engine.m1.profile_readability`: 448 words, grade 7.8 (names out 7.2), reading ease 73.2, 16.6 words a sentence, longest sentence 33 words. Pass. The length is now inside 380-450.

Grade 7.8 is under 8, so it was checked by a listener read. It is not flat: Antony's witness, the prison, the blanket and the Latin chain keep the world's own voice.

## Findings
None blocking. No corrections are required.
