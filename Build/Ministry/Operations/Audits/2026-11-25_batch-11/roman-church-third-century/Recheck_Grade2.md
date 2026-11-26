# Recheck of the second-grade fixes: roman-church-third-century

Checked: `Fixes_Grade2.md`, against the live brief, `Outline.md`, `Source_Sheet.md`, `Grades2/Held_Findings.json` and `Grades2/listener.md`. I did not write the fixes. Every cited line below was opened in `cic/texts/`.

## Verdict: FIX (one sheet citation only)

The brief changes and the cuts pass as written. One line number in the new sheet row N7a is wrong. Apply everything in `Fixes_Grade2.md` with the one correction below.

## The two new sentences

1. "A writer of his day says he ignored warning visions, so holy angels whipped him all night." E 32252-32256 (warned "oftentimes by the Lord through visions"), E 32258-32262 ("as he paid little regard to the visions ... he was scourged by holy angels, and punished severely through the entire night"), E 32267-32268 (sackcloth and ashes in the morning). The writer is the anonymous Little Labyrinth, "in our own day" (E 32223-32224): contemporary, so "a writer of his day" holds. "So" holds: the source makes the scourging follow from his ignoring the visions. The wonder stays in the writer's voice, as Z3 and the Do not say row ("Angels scourged Natalius, as fact") require. Order matches the source. 17 words, one thought, clear on one hearing.
2. "That year, the confessors who had sided with Novatian came back, saying they had been deceived." CyL 6748 and 6776 ("circumuentos se esse / adfirmarunt"), CyL 6831-6832 ("circumuenti sumus perfidia et loquacitate captiosa"), H 32980-32981 and 33018-33019 (ANF's English agrees), E 38451-38458 (Eusebius quoting Cornelius). Own words reported by Cornelius, a hostile party: Documented as their account. It names no deceiver, so Cornelius's charge against Novatian is not carried forward as narration. 16 words.

Both answer the held "why" findings. Nothing reaches past the source. No gap-only tell.

## The mines clause (cut a)

The cut stands. The clause is Callistus's sentence to the mines for disturbing a synagogue, not the 235 exile of Pontian and Hippolytus; that exile was already out (Cut first 4). Judged on four tests:
- **Never cut** (`Outline.md` line 250): not listed. The list keeps Hippolytus's reason for cutting off Sabellius, Callistus's rule, the marriage rule with its charge and the rest. All stay in the brief.
- **The heart**: the essence needs a mixed church that "held slaves". "Who had been a slave" keeps that, and the Do not say row allows it alone ("or 'who had been a slave' alone (C1)").
- **The record's force** (Kit Part 1): the force here is the quarrel between Callistus and Hippolytus. It stays whole: Hippolytus's motive charge, his laxity charge and his "adultery and murder" charge. The mines are Callistus's life before this church's story. The Kit lets a punishment go out whole when the story will not explain it. It forbids only telling the act without its reason.
- **Why it goes**: the slate gives this story Callistus's side, "not Hippolytus's charges again". Leave out gives Callistus's early life "beyond one clause" to `hippolytus-of-rome`, which tells the synagogue in narration (sheet C1a). The cut is made for that reason, not because only an enemy says it.

## The other cuts

b ("Christian"): the brief's context is the church's own argument, so the sense holds; the outline's heart keeps the word. c, e, f and g: wording only. d: "a later historian" keeps the later witness kind, and "the same historian" still points back. None touches a credit, a quote, a Never-cut line or a Part 1 explanation.

## Count and readability

All eight old strings occur exactly once in the live brief. Scratch copy with all changes applied (`/tmp/claude-0/-home-user-CIC-Project/39d92526-11f8-5688-9d05-41b4a8cf62d5/scratchpad/rc2_rct_brief.txt`): **675** by `wc -w`, at the cap. `python3 -m engine.m1.profile_readability --report`: 673, grade 8.3 (names out 7.3), reading ease 75.7, 18.7 words a sentence, longest 35 (an old sentence), pass. The outline and sheet old strings each occur once.

## Correction

In `Fixes_Grade2.md`, "Outline and sheet lines to change", the new `Source_Sheet.md` row N7a:

- Old: `| N7a | Why the confessors came back: they said they had been deceived; Cornelius says they found Novatian out | CyL 6750, 6776;`
- New: `| N7a | Why the confessors came back: they said they had been deceived; Cornelius says they found Novatian out | CyL 6748, 6776;`

("circumuentos se esse" stands at CyL 6748, not 6750.) Nothing else changes.
