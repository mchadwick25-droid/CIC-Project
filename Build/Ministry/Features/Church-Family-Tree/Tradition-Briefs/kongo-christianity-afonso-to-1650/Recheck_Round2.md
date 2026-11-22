# Recheck, round 2: kongo-christianity-afonso-to-1650

Rechecker: Opus, targeted recheck. I wrote neither the brief nor the review. I compared `kongo-christianity-afonso-to-1650.v1.txt` with `kongo-christianity-afonso-to-1650.brief.txt` and opened the source lines myself. PM is `cic/texts/paiva-manso_historia-do-congo-documentos-por_1877.txt`. Lopes is `cic/texts/lopes_report-of-the-kingdom-of-congo_hutchinson1881.txt`.

## Verdict: PASS (after one edit by the rechecker, listed below)

## 1. Findings answered as worded

The diff changes only paragraphs 1, 3, 5, 7, 9 and 11, and every change matches a finding. B1, B2, B3, M1, M2, M3 and M4 each use the reviewer's wording. The one exception is the M1 split, which the reviser declared. No other sentence changed. The quote in paragraph 5 is unchanged, character for character.

## 2. B3 opening

- "who were being carried off to be sold": holds. PM 2399-2403 says merchants "leuam cada dia nossos naturaes", and thieves "os furtam e lhos trazem a vender" (steal them and bring them to be sold). The 1526 heading (PM 2339-2345) says the merchants were "fazendo-os escravos".
- "Contact with Portugal had brought Kongo both the faith and this trade": holds, and it does not overstate. For the faith, see the 1512 letter (PM 533-545): the kings of Portugal sent religious men, and through them Kongo left its idols. Lopes 3510-3530 has the ships of 1491 bringing what was needed for baptism. For the trade, see PM 2390-2405: the merchants came because Portugal's factors gave them free rein, and they carried off his people. The claim is about "this trade", the selling of people to the Portuguese. It does not say slavery began with Portugal. It matches the Sheet's Connection to carry.
- "in his letters Afonso set the one against the other": holds. PM 2405-2411 asks for priests and teachers and no merchants.

## 3. B2 sentence

"Then, it says, Pango brought a great army against him, and Afonso defeated it and kept the throne." This holds against Lopes.
- Lopes 3804-3806: "collected a great force, and came armed against his brother". Lopes 3817: "the great army Pango brought".
- "defeated it": Lopes 3998-4005 and 4019-4036. Pango was routed twice and then died in his own trap.
- "kept the throne": Lopes 4038-4039, "the king was freed from farther opposition". Lopes 3803 already has him "on the throne".
- The sentence leaves out the numbers (200,000 and 10,000) and the vision of the lady in white and the knight (Lopes 4019-4027), as the Sheet asks. "It says" credits the report.

## 4. Own wording (M1 split): corrected

The source is PM 1935-1937: "por alumiar os cegos que sam em meus Reynos pêra que depois de minha morte posam sostentar ha fé". In English: to bring light to the blind in my kingdoms, so that after my death they could uphold the faith.

The split "After his death, he said, they could uphold it." had two problems:
- It lost the purpose ("pêra que", so that). It reads as a claim about what they were able to do.
- Heard once, "it" sits right after "his kingdom", so it can be heard as the kingdom rather than the faith.

Edit applied to the brief:
- Old: "After his death, he said, they could uphold it."
- New: "He wanted them to uphold the faith after his death."

This keeps the purpose and names the faith. The previous sentence already credits the letter ("In 1517 he wrote").

## 5. One fresh hearing

- **Essence in the first minute:** yes. Paragraph 1 (about 65 words) carries the faith, the trade and Afonso setting the one against the other.
- **Told twice:** the 1526 letter opens the brief and comes back in full in paragraph 5. The carrying-off of his people is named in both places. This is the frame that B3 asked for, and paragraph 5 adds new facts: the nobles' sons and his kin, the schools, and the quote. I hear it as a return, not a repeat. One sentence could be tighter: "By 1526, the letters turn to a harm that came with Portugal." It restates paragraph 1 and is not wrong. I make no change.
- **Long sentences:** the longest is 30 words, and none goes past about 30.

## 6. Scorer

`python -m engine.m1.profile_readability .../kongo-christianity-afonso-to-1650.brief.txt`, after the edit: 449 words, grade 6.8 (names out 5.6), reading ease names out 84.2, 16.6 words a sentence, longest sentence 30 words: pass. The grade is under 8, so I judged it by ear. It is not flat.
