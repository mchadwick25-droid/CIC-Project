# Gloss card FK-18 rewrites: independent review, 2026-10-18

## Scope

Twenty-seven gloss-card fields that scored Flesch-Kincaid grade 18 or more: 21 `senses.translational` fields and 6 `false_friend` lines (gallic 4, hal 4, rzg 3, witt 16). The project lead's rulings govern: (1) the card speaks from outside the world, with no "we/our/us" for the world, though a modern reader's quoted question keeps its own pronouns; (2) the readability gate (FK at most 10, Flesch Reading Ease at least 60) now grades the card; (3) only these 27 cards are rewritten now. A Sonnet drafter produced the rewrites. This review checked each draft. No record file was edited.

## Method

For each of the 27, the draft was compared clause by clause with the old text, looking for any lost or added claim, qualifier or hedge. Each was also read against its term record: sources, loci, other senses, false friends and use note. Where a draft quotes a source, the quotation was checked against the vendored text:
- "after long discussion": Cassian, Institutes III, in `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`
- "in and under": Large Catechism, in `cic/texts/luther_large-catechism_bente-dau1921.txt`
- "with the highest reverence": Augsburg Confession, in `cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`
- the Antichrist condition: Apology, in `cic/texts/melanchthon_apology-augsburg-confession_bente-dau1921.txt`
- "pupil of the Catechism": Large Catechism, in the same file as "in and under"

All of these are verbatim in the vendored texts. Every approved text was re-scored with `engine.m1.gates.grade_text`, checked for world-voice pronouns, and checked for sentences longer than 25 words. Corrected texts were re-scored after correction. All 27 approved texts pass the gate.

## Entries

1. gallic.term.angels, translational: pass. "Told as eyewitness testimony" keeps the old text's point: this is how the visits are reported, and it is no claim that they happened.
2. gallic.term.church-or-circus, translational: corrected. The draft used "this" twice with two different referents ("closer to this" and "renounce exactly this"), so the baptismal vow no longer pointed clearly at the games. It also turned the old denial into "a modern reader may hear". The correction restores the denial ("This is not 'some people skipped church,' a mild modern shrug") and names what was renounced as "these shows".
3. gallic.term.sarabaite, translational: corrected. "Used inside the Gallic houses" read as all Gallic houses. The record says the word is Marseilles-only and that no one at Tours uses it. The correction reads "inside houses in Gaul". The draft's "giving up the world in public" lost the sense of a renunciation that was only performed, for show. The correction reads "as a public show". The record's own phrasing is "before the face of men" and "for show".
4. gallic.term.unceasing-prayer, translational: corrected. "Those later names come from a nineteenth-century editor" implies the editor coined Lauds, Prime and Compline. He only applied those labels in the translation; the record says the names are "the editor's". The correction keeps the old wording: "are a nineteenth-century editor's". The modern reader's quoted question keeps "you", as ruled. The quotation is verified.
5. hal.term.grammaticus, translational: pass. "Language and books" for "language and literature" is an acceptable plain equivalent, since the record's own approved plain_meaning already uses it.
6. hal.term.grammaticus, false_friend[0]: corrected. The draft put "Hebrew skill" in place of both "mastery" and "fluency". That changes the claim: the scholarly dispute is over fluency, not whether Jerome had any Hebrew at all, and the record's use note speaks of "Hebrew fluency". The correction keeps "mastery" in the misreading and "fluent in Hebrew" in the contested claim. It keeps the old hedge ("supposedly") as "the claim that", and "seriously contested".
7. hal.term.matrona, false_friend[0]: corrected. The draft dropped "interchangeable", and "her family" read as lineage rather than "family situations" (widowhood, children, remarriage). The correction is "one type, each the same as the next" and "home lives", with "standing" for "positions". "Genuinely" is kept as "truly".
8. hal.term.monasterium, false_friend[0]: corrected. "That label is from later medieval times" suggests when the word was coined. The old text says the label belongs to later medieval arrangements. The correction is "belongs to later forms from the Middle Ages".
9. rzg.term.catechism, false_friend[0]: pass. "Single type of text, repeated the same way" keeps "single, uniform genre repeated identically", and "several catechism voices, each distinct" is kept.
10. rzg.term.mutual-consent, false_friend[0]: corrected. "A modern call for all Christians to be one" drifts. A statement became an appeal, and "general", the half of the contrast with "specific", was lost. The correction is "a modern statement, in general terms, that all Christians are one", and "negotiated" becomes "worked out by both sides". This also matches the record's "approved on both sides".
11. rzg.term.the-lords-supper-spiritual-presence, false_friend[0]: pass. "Of worship" for "liturgical" is acceptable, and the habit of reading such questions as symbolic by default is kept.
12. witt.term.catechism, translational: corrected. "Every Christian recites it daily for life" turned a prescription into a statement of practice. The record says household practice is unattested, and its use note excludes the weekly examination as attested practice. The draft's "In their own words, they remain its pupils" used the present tense for the dead. The correction is "Every Christian was to recite it daily for life, and be examined on it weekly", and "By their own word, the reformers remained its pupils too". The "pupil" phrase is verified in the Large Catechism preface.
13. witt.term.faith, translational: pass. All clauses are kept, including the 1529 fence against the movement's own radicals.
14. witt.term.household, translational: pass. "A house with ranks" for "stratified" is an acceptable plain equivalent. "Stated as a duty" and "no actual house's practice is attested" keep the old hedge.
15. witt.term.hymn, translational: pass.
16. witt.term.indulgence, translational: pass. "Bought release from penalty" for "purchased remission of penalty" is acceptable, and the guilt/penalty distinction survives.
17. witt.term.law-and-gospel, translational: pass.
18. witt.term.marriage, translational: pass.
19. witt.term.must-and-free, translational: pass.
20. witt.term.pope-and-antichrist, translational: corrected. The draft split "a fixed doctrine about the papal office in general" into two denials. One of them, "a fixed doctrine", is broader than the old text. Its last sentence, "It is the kingdom of Antichrist if...", had no clear subject. The correction restores the single denial ("a fixed doctrine about the pope's office as such"). It names the subject from the Apology, the record's own source ("The papacy belongs to Antichrist's kingdom if..."), and "belongs to" matches the source's "part of the kingdom". "Foe" for "adversary" and "polite words of the confession" for "confessional courtesy" were needed to pass the gate. Both are plain equivalents.
21. witt.term.promise-and-testament, translational: pass.
22. witt.term.repentance, translational: corrected. "Held one word for a lifelong turning" lost the old text's point: after naming both, it says 'repentance' and 'penance' are one word, the single word poenitentia. The record's false friends make the same point about the translators. The correction is "For the Wittenberg reformers these were one word. It named a lifelong turning with two parts."
23. witt.term.sacrament-of-the-altar, translational: pass. The quotation "in and under" is verified.
24. witt.term.the-mass, translational: pass. The quotation "with the highest reverence" is verified.
25. witt.term.the-two-governments, translational: pass.
26. witt.term.the-word, translational: pass.
27. witt.term.we-are-all-priests, translational: pass. "Used" for "exercised" is slightly weaker but does not change the claim.

## Cross-cutting note

All 16 witt drafts put "the Wittenberg reformers" where the old text had the world's "we". This is an outside-voice subject consistent with ruling (1). For these doctrinal and prescriptive statements it is accurate, since the world's own "we" here is the movement's teaching voice. It narrows "we" a little where the world also includes its congregations, but no draft attributes a practice to the congregations that the old text did not.

## Overall verdict

17 pass and 10 are corrected; all 27 approved texts meet the gate (FK at most 10, FRE at least 60), keep the outside voice, have no sentence over 25 words, and keep every quotation verbatim. No entry needs to be held back. The corrections fix meaning drift in the drafts, not readability, and each corrected text was re-scored. The approved texts are in `final27.json` in the session scratchpad.
