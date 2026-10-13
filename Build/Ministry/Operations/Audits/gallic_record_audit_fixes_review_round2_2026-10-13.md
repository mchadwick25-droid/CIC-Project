Review round 2 (targeted recheck), gallic record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS

## Blocking findings from round 1

1. **gallic.quote.the-fathers-and-the-angels-twelve: RESOLVED.** Each of the three cut clauses is now a whole sentence, finished in the edition's own words. "They feared that some dispute might send out a poisonous root ..." matches npnf211:17181-17184. "Each man ... thought that what was easy for him should be fixed" matches 17184-17187, and "fix" is also the edition's word at 17190. "There was such a holy difference of opinion ..." matches 17192-17193. Every "..." is kept. The ending "the two lessons they added, they added simply as extras, and by their own appointment" matches 17225-17227. Nothing is added, and the result meets method V2.0, l.862.
2. **gallic.demo.someone-like-me: RESOLVED.** "Could not recall anyone ... keeping it up unbroken even a year" matches npnf211:18557-18559. Both "cannot recollect" and "unbroken" are back. "In the same book" is true, because the Institutes is the book named in the line before (IV.2). The new sentence is 21 words.
3. **gallic.term.customs-of-the-monasteries: RESOLVED.** Practice is no longer stated as fact. The text is now Cassian's stated plan ("he said he would balance it"), which is true to npnf211:16526-16534 ("severity of the climate ... diversity of habits ... I shall to some extent balance it"). "A new house in Gaul" matches "a new establishment in the West, in the parts of Gaul" (16522-16523). It no longer clashes with the record's own not_for.

## Non-blocking items

- **4. apostolic-authority-in-martin-alone:** applied correctly, yes. It reads "priesthood" and "royal court".
- **5. vincent-awful-expectation-of-judgment:** applied correctly, yes. "Urgently demands" is in. See New issue 1 for a side effect.
- **6. christ-in-the-beggar-and-the-guest positions[3]:** applied correctly, yes.
- **7. the-three-lentil-beans:** applied correctly, yes. "Judges him a pilferer, careless with sacred things" matches npnf211:19233.
- **8. Small wording points:** all applied correctly.
  - virgin-virginity: yes.
  - sarabaite: yes.
  - apostolic-see-pope: yes. Pope Stephen is Vincent's own example.
  - no-one-who-saw-him: yes. "For those who wished" matches "only for those who liked" (17227).
  - never-settled: a locus is added, but see New issue 2.
- **The "unbroken" follow-ons:** only-on-paper, want-to-leave and record-thinnest now all carry "unbroken". Yes.
- **9. Out-of-scope logging:** this commit touched no Open_Gaps_Tracking.md file, so I could not confirm that the items were logged.

## New issues

1. **gallic.quote.vincent-awful-expectation-of-judgment (NON-BLOCKING).** Splitting the sentence dropped the causal link. The source says "especially since a certain awful expectation ... demands" (npnf211:12088-12090). The new text "This is all the more needed. A certain fearful expectation ..." no longer says that the second sentence is the reason for the first. Fix: "This is all the more needed, since a certain fearful expectation ..." or "... needed. For a certain fearful expectation ...".
2. **gallic.demo.never-settled, new locus (NON-BLOCKING).** The locus is mostly true of the source. Augustine is replying to letters from Prosper and Hilary about "those brethren". This is in ch. 1 ("write again from here") and ch. 2 ("on consideration of your letters", what they "have attained to"), and ch. 3 answers "those who say". Two points are off:
   - The edition never says "Africa". It says only "from here". Africa (Hippo) is common knowledge, but it is not true "of that source" as the locus claims.
   - The report itself is in ch. 1-2, not ch. 2-3.
   
   Fix: "ch. 1-2 (xxi.ii.i-ii): Augustine answers Prosper's and Hilary's letters about what the brethren held". Leave Africa out of the locus.
3. **Same "unbroken" gap in fields outside this commit (NON-BLOCKING, needs logging).**
   - voice_craft carries "none of us keeping the fathers' perseverance a year". It feeds the voice, so this one matters most.
   - gallic.gravity.received-not-invented l.147 carries "none kept Egypt's perseverance a year".
   - gallic.gravity.egypt-as-measure l.156 has "even for a year" without "unbroken".
   - Cassian's figure record, the egypt-two-measures contested claim and only-on-paper's own locus do the same.
   
   None of these was edited here, so this is not a regression. They belong in the Open_Gaps entry from finding 9.

No added words, dropped clauses, AI-voice phrasing, or rendering words missing from the edition turned up in the 15 changed files beyond the points above.

## Resolution

New issues 1 and 2 were applied before the package was rebuilt: "For a certain fearful expectation" restores the causal link, and the never-settled locus now reads "ch. 1-2 (xxi.ii.i-ii): Augustine answers Prosper's and Hilary's letters about what the brethren held". The only-on-paper locus now carries "unbroken" as well. New issue 3 is logged in Build/worlds/gallic/Open_Gaps_Tracking.md, OG-33.
