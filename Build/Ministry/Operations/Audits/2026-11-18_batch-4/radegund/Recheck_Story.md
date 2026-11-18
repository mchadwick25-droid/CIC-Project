# Recheck: Radegund

Independent recheck, batch 4, 2026-11-18. Read against `CLAUDE.md` (Trust and source fidelity), the Brief-Kit `Standard.md`, `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `radegund.brief.txt` and `radegund.brief.v1.txt`.

## Verdict: FIX

## 1. Review findings

- Finding 1 (heart late): asked only for "also told" parts to come earlier. Superseded; not checked.
- Finding 2 ("the king" heard as Lothar): fixed. Sigibert is named twice: "With the letters of King Sigibert" and "So Sigibert sent the bishop of Tours" (L16; DAL 19601–19610, 19620–19625).
- Finding 3 (revolt abbess heard as Agnes): fixed at the cause. The Agnes sentence is cut, so "the abbess" in the revolt no longer reads as her.
- Finding 4 (length): 452 words, under the 460 cap.

## 2. New wording

Each new sentence in `Revision.md`, and every other sentence that differs from v1, traces to the outline or sheet:

- "Radegund had come to the Franks as a captive": S2 (DAL 4379–4381), Essence.
- "founded a house for women at Poitiers, in what is now France": L11; Setting line.
- "She gave it a written Rule and a relic of the Cross, and wrote this letter to guard it after she was gone": Essence; L13, L16, L19.
- "It tells what she had built": beat 1 (L19).
- "With King Lothar's backing ... gave it everything the king had given her": L11, her own letter (DAL 19846–19850).
- "The Rule was one that Caesarius, bishop of Arles, had made for his sister's convent ... for life": L13 (DAL 19851–19855, 19543–19545).
- "With the letters of King Sigibert, she sent to the emperor in the East": L16 (Gregory for the letters; Baudonivia for the emperor); beat 3.
- "The house came to be called Holy Cross": I3, in the outline's required wording.
- "So Sigibert sent the bishop of Tours ...": L16; "Gregory says" is kept (D5).
- "Gregory later copied the whole letter into his History, which is how we still have it": I1; Connection.

Quotes: Q2 is in Gregory's Latin at `cic/texts/gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` 31516–31517. Q1 is in Fortunatus's Latin at `cic/texts/fredegar-liber-historiae-francorum-vitae-mgh-srm-2-lat_krusch1888.txt` 28806, 28808. Both renderings match the outline word for word.

**One fault, made by the revision.** v1 read: "She sent to the emperor in the East for a piece of the wood of the Cross, and the house came to be called Holy Cross. Gregory ... says the bishop of Poitiers would not receive it." The revision split off "The house came to be called Holy Cross." as its own sentence. Now the nearest thing "it" can refer to is the house. A listener hears that the bishop refused to receive the house. The record says he refused the relics (DAL 19601–19610; D5). That is a wrong fact, so the wording must change.

Replace:
> Gregory, a bishop who knew her, says the bishop of Poitiers would not receive it.

with:
> Gregory, a bishop who knew her, says the bishop of Poitiers would not receive the relic.

The next sentence's "brought it in" then refers to the relic, as it should.

## 3. Kit lines

- Hook: two sentences, her letter in her own words (Q2). Pass.
- Essence: complete at word 99 ("...after she was gone"), inside about 150. Pass.
- Also told, all present: all the king had given her (w117); Holy Cross (w189); the bishop of Poitiers refusing (w202, in Gregory's voice); about two hundred (w404); the letter read in the revolt (w425). Pass.
- Setting: "In the sixth century" and "at Poitiers, in what is now France" come in separate sentences, one clause each. Pass.
- Ending: on the abbess, at the hearing, defending "only what was done under the lady Radegund". The story ends on the person. Pass.

## 4. Score

`python -m engine.m1.profile_readability radegund/radegund.brief.txt`: 452 words, grade 6.7 (names out 6.0), reading ease names out 80.8, 16.1 words a sentence, longest sentence 30 words: pass. Grade under 8 is left to the listening review. The fix above adds one word.
