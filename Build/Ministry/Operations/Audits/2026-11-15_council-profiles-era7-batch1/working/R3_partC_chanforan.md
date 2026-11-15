## Council profiles, era 7 batch 1, round 3: Part C (Synod of Chanforan 1532)

**Council.** `synod-of-chanforan-1532`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/synod-of-chanforan-1532.brief.txt`, `audio/synod-of-chanforan-1532.audio.txt`, `synod-of-chanforan-1532.entry.json`, `records.json` key `synod-of-chanforan-1532` (102 claims, 9 contested claims, 9 absent details; identical to `working/records_synod-of-chanforan-1532.json`), and `README.md` l.11 (unchanged in this round). The scope is `git diff 7e0ce987c HEAD` on those files (branch `claude/cft-councils-era7-batch1`), checked against `R2_recheck.md` Part C and `R2_changes.md` Part C with its preface (the worker's brief edit for C2-B1 and the two word cuts that pay for it).
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.93, Flesch 66.84. Longest sentence 25 words ("The articles survive in printings by the Dauphiné pastor Jean-Paul Perrin, the valleys' historians Pierre Gilles and Jean Léger, and the English envoy Samuel Morland."). No sentence over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag (checked by `diff` after stripping the two tags). The R2_changes preface says only Augsburg's audio changed; Chanforan's changed too, with the worker's brief edit, and it matches.
**Entry.** No sentence in any changed entry string is over 25 words. The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the fixing. No repo file other than this part was written. No model, network or paid calls were made.

Abbreviations as in rounds 1 and 2 (GIL81 = `gilles_histoire-ecclesiastique-eglises-vaudoises-v1-fra_1881.txt`, LEG = `leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt`, PER19 = `perrin_histoire-des-vaudois-fra_1619.txt`, CRESP1 = `crespin_histoire-des-martyrs-t1-fra_benoit-lelievre1885.txt`).

## Verdict: REVISE (one blocking, two minor)

The entry and records now read Léger rightly: the arms view held through 1560 and changed only later. C2-M1, C2-M2 and C2-M3 are closed, and every changed quote is verbatim.

The worker's new brief sentence carries a new error. "Except that later they took up arms" tells the listener the valleys bore no arms until after 1560. Léger says their rule allowed defense "en toute extrémité", and that they kept that rule through Emanuel Philibert's war. Gilles, whom Léger cites there, tells the valleys fighting that war in self-defense under the same rule. What changed later was going beyond defense, not taking up arms (C3-B1).

The two minor findings are "nothing changed in their dealings with the reformers", which can be read as a claim about relations rather than doctrine, and Muston and Montet left with no word on what kind of witness they are, after "the historians" was cut to pay for the C2-B1 sentence.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| C2-B1 | CLOSED in entry and records; OPEN in the brief, with a new point | LEG l.23072-23086 re-read in place (quoted under C3-B1). Entry `outcome[17]` ("He names one exception: they were nearly Anabaptists on arms, holding that only magistrates should wield the sword. They still held this in 1560, in Emanuel Philibert's war, and acted otherwise only later.") is faithful to "presque Anabatistes en ce qui regarde le maniement des armes seulement", "qu'il n'appartenoit qu'aus Magistrats de manier l'épée", "encore là logés l'an 1560 ... pendant la cruelle guerre que leur fit Emanuel Philibert" and "ils en ayent uzé autrement du depuis". Records claim 91 says the same and adds "after the Maccabees' example" ("à l'exemple des anciens Machabées", l.23086); its witness is widened to l.23072-23086. Entry `uncertain[12]` and records contested claim 3 have the right timing; see C3-M1 on their opening clause. Keeping "acted otherwise" rather than round 2's "gave up" is right: "en ayent uzé autrement" says no more. The brief sentence is the worker's, not round 2's proposal, and it misstates the change (C3-B1). The cut "a slight to earlier leaders" is faithful to "deshonoroit la mémoire de ceux qui avoyent tant heureusement conduit ces Eglises jusqu'alors" (GIL81 l.2034-2036). The cut "the historians" is C3-M2. |
| C2-M1 | CLOSED | Entry `attended[6]` ends "Our scan reads 1552, a slip for 1532." CRESP1 l.49905 "En 1552, il vint . avec un autre barbe, inviter Farel et Saunier, qui se trouvaient à Granson, au synode d'An- grogne . qui se tint le 12 septembre." The 1532 reading stands on round 2's evidence (the same note misprints 1526 as "IÇ26", l.49902). |
| C2-M2 | CLOSED | Gonin's `people` row: "Barbe of Angrogna; with another barbe, invited Farel and Saunier to the synod (Crespin's editors); sent to Geneva in 1536 (Perrin)". "Avec un autre barbe" (CRESP1 l.49905); "en l'annee mille cinq cens trente six ils envoyerent à Geneve vn certain Martin Gonin" (PER19 l.12164-12166, OCR). The tag no longer reads as the editors inviting. |
| C2-M3 | CLOSED | Records claim 95 cites PER19 l.14262-14271: "Lettre d'Oecolampade escrite aux Vaudois de Prouence" (l.14262, OCR) and "escripte en l'annee 1530" (l.14271, OCR). The range holds the year. |
| C-S4 (round 1, held) | OPEN, held for the batch's Open-Gaps entry at merge | Unchanged in this round, as R2_changes Part C says. Not rechecked further. |

## New findings

### Blocking

**C3-B1. Blocking (the brief's new Léger sentence misstates what changed: the valleys bore arms in defense before the change).**

Location: brief p.8, sentence 1: "Léger wrote in 1669 that the valleys changed nothing at the Reformation, except that later they took up arms."

Evidence:
- LEG l.23072-23086 (OCR and long s normalised): "Je ne trouve point qu'ils y ayent changé la moindre chose, si ce n'est qu'ils étoient presque Anabatistes en ce qui regarde le maniement des armes seulement, car ils croyoient qu'il n'appartenoit qu'aus Magistrats de manier l'épée, & que quand ils étoient persecutés en un lieu, ils se devoient contenter de fuir en un autre, ou, en toute extrémité, d'être seulement sur la defensive, sans seulement faire un pas pour poursuivre leurs ennemis quand ils prenoient la fuite. Ils en étoient même encore là logés l'an 1560 [OCR "l ait 1 fSo. 8c <f I .", which may add 61] pendant la cruelle guerre que leur fit Emanuel Philibert ... comme le remarque Pierre Gilles ... bien qu'enfin à l'exemple des anciens Machabées, ils en ayent uzé autrement du depuis."
- So the old rule already allowed defense in the last extremity, and it held during the war of 1560-61. Léger points to Gilles for that war.
- GIL81 l.8768-8789: in that war the ministers would not let the people pursue the beaten army, "car ils avoyent conclu dès le commencement de la guerre au mois d'octobre précédent, et puis confirmé au commencement de février dernier, que si l'extrême nécessité les contraignait de se défendre par armes, ... on se contiendroit en la seule défense". GIL81 l.8276-8278 has the people bring in "grande quantité d'armes de toutes sortes, harquebuses, morions, tambours, picques, halebardes, espées, et autres despouilles des ennemis".
- A listener hears that the valleys took no arms until after 1560. Léger and Gilles both have them fighting in self-defense in 1560-61. What changed "du depuis" was going beyond defense, which is what "en ayent uzé autrement" refers back to.

Fix, brief p.8, sentence 1 (17 words for 19): "Léger wrote in 1669 that the valleys changed nothing at the Reformation, but later went beyond self-defense." The brief's spelling is American ("pretense"), so "self-defense". With this fix alone the brief is 398 words, FK 6.94, Flesch 66.77, longest sentence 25 words (scratch copy `/tmp/claude-0/-home-user-CIC-Project/961c4153-8c1b-50d3-a603-34620231affd/scratchpad/R3C/b1only.txt`). The entry and records need no change for this point; they already say "acted otherwise only later".

### Minor

**C3-M1. Minor (an opening clause that can be read as relations, not doctrine).** Entry `uncertain[12]`: "Léger says nothing changed in their dealings with the reformers." Records contested claim 3, Léger's side: "Nothing changed in their dealings with the reformers; ...". Léger's "y" refers back to the deputies' talks "touchant les points de Doctrine, & de Discipline" (LEG l.23071-23074): he finds they changed nothing in doctrine or discipline through those talks. "Nothing changed in their dealings" can be heard as saying the relationship with the reformers did not change, which he does not say. Fix: entry `uncertain[12]`, the Léger sentence: "Léger finds they changed nothing in doctrine or discipline through their talks with the reformers." (15 words.) Records contested claim 3, Léger's side, opening clause: "Nothing changed in doctrine or discipline through the talks with the reformers; ..." (rest unchanged).

**C3-M2. Minor (two main witnesses left with no kind).** Brief p.2, sentence 1: "That manuscript reaches us only in quotations by Alexis Muston and Édouard Montet." Round 2 had "by the historians Alexis Muston and Édouard Montet"; the words were cut to pay for the C2-B1 sentence. Muston and Montet are the only relays of the manuscript, and nothing else in the brief says what kind of witness they are. "All wrote on the Reformed side" follows the printers' sentence, so the listener cannot tell whether it covers them. The pattern (`Council_Profile_Pattern.md` l.15) asks for each main witness's kind. The README (l.11) still says "a manuscript quoted by two historians". Fix: restore "the historians": "That manuscript reaches us only in quotations by the historians Alexis Muston and Édouard Montet." With C3-B1 the brief is back at 400 words, FK 6.99, Flesch 66.50, longest sentence 25 words (scratch copy `/tmp/claude-0/-home-user-CIC-Project/961c4153-8c1b-50d3-a603-34620231affd/scratchpad/R3C/fixed.txt`). The audio follows the brief through `mkaudio.py`.

## Verified

- **Changed or added quotes, verbatim (OCR allowed).** "Je ne trouve point qu'ils y ayent changé la moindre chose" (LEG l.23074-23075); CRESP1 "En 1552" (l.49905); PER19 "escripte en l'annee 1530" (l.14271).
- **Translations and paraphrases of Léger.** "nearly Anabaptists on arms" for "presque Anabatistes en ce qui regarde le maniement des armes seulement"; "only magistrates should wield the sword" for "qu'il n'appartenoit qu'aus Magistrats de manier l'épée"; "still held this in 1560, in Emanuel Philibert's war" for "encore là logés l'an 1560 ... pendant la cruelle guerre que leur fit Emanuel Philibert"; "after the Maccabees' example" for "à l'exemple des anciens Machabées"; "acted otherwise only later" for "en ayent uzé autrement du depuis". None adds anything. The brief's "at the Reformation" follows "au tems de la Reformation" (l.23071).
- **Gilles's dissent sentence after the cut.** "A slight to earlier leaders" (GIL81 l.2034-2036). The claim still sits with "Gilles ... says" in the sentence before.
- **Sentences joined or split.** Entry `outcome[17]` now has three sentences; the two added ones carry "He names" and follow "Léger wrote", so the witness is clear. Entry `uncertain[12]`'s three Léger sentences open with "Léger says" (see C3-M1). Records claim 91 opens "Léger, on the Waldensians' talks with the reformers".
- **Records.** The `records.json` key equals the working copy (Python comparison). Counts: 102 claims, 9 contested claims, 9 absent details.
- **Writing.** In the changed strings: no empty contrast, no "X and never Y", no summing-up line, no filler. Each changed sentence earns its place.

## Searches run

No new or changed absence in this round. Searches made for the points above, all in `cic/texts/` with case-insensitive `grep`, OCR and long s allowed for:
- `anaba|machab` in LEG: the only arms passage is l.23076-23086; the other "Machab" hits are book lists (l.4172, 11939, 12733-12737, 12843). Léger gives no other statement on when the arms view changed.
- `armes` in GIL81 after l.3000, then read in place at l.7284-7294, l.8268-8280 and l.8766-8794 (the 1560-61 war: arms used in defense, pursuit refused under the ministers' rule).
- `(prendre|prindrent|prirent|pris) les armes` in GIL81 v1 and v2: no hit in that form.
- Spelling check: no "defence" in any era 7 brief.

## Counts

Round 2: 4 closed (C2-B1 in entry and records, C2-M1, C2-M2, C2-M3), 1 open with a new point (C2-B1 in the brief), C-S4 still held for merge. New: Blocking 1 (C3-B1). Substantial 0. Minor 2 (C3-M1, C3-M2).
