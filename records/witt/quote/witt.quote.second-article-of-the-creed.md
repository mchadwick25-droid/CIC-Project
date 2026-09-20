---
id: witt.quote.second-article-of-the-creed
world_id: lutheran-wittenberg-and-its-congregations
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- C-T
- C-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as the Small Catechism's own Second Article, the household's weekly confession, said by
    every household in the program the Large Catechism prescribes (witt.gravity.household-catechism). No
    biographical or personal claim rides on it -- it is recited text, not a remembered saying, and every
    household under this program said these same words.
sources:
- source_id: witt.source.luther-small-catechism
  locus: "The Second Article, On Redemption, and its own explanation (cic:luther_small-catechism_smith1994.txt lines 186-205): the creed's own confession and the household's own 'I believe that Jesus Christ is truly God... and also truly man'"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether Jesus was God, or asks about the Trinity's own claim about Christ"
  - "participant asks whether Jesus died to pay for sin, in the participant's place"
  - "participant asks whether Jesus is a personal Lord and Savior, or asks what our record actually holds about Jesus"
  - "participant asks how we know the resurrection happened"
  do_not_retrieve_when:
  - "participant wants the whole Apostles' Creed recited in order -- this record holds only the Second Article"
  - "participant wants an eyewitness or historical-critical argument for the resurrection -- this is a confession, not an apologetic argument"
text: >-
  And in Jesus Christ, His only Son, our Lord, Who was conceived by the
  Holy Spirit, born of the Virgin Mary, suffered under Pontius Pilate,
  was crucified, died and was buried, descended to Hell, on the third day
  rose again from the dead, ascended to Heaven and sat down at the right
  hand of God the Almighty Father. From there He will come to judge the
  living and the dead.

  What does this mean?

  I believe that Jesus Christ is truly God, born of the Father in
  eternity and also truly man, born of the Virgin Mary. He is my Lord! He
  redeemed me, a lost and condemned person, bought and won me from all
  sins, death and the authority of the Devil. It did not cost Him gold or
  silver, but His holy, precious blood, His innocent body--His death!
  Because of this, I am His very own, will live under Him in His kingdom
  and serve Him righteously, innocently and blessedly forever, just as He
  is risen from death, lives and reigns forever. Yes, this is true.
speaker_or_author: "the Small Catechism's Second Article -- the creed and its explanation, said by the household itself, in its own first person, as 'I believe'"
license: verbatim
modern_lens_note: >-
  A modern reader may hear "bought and won me" as cold, commercial language -- a transaction. We do not
  mean it that way. The point of naming a price at all is to name what it was not: not gold, not silver,
  nothing we could ourselves have paid. The price was a person, given. And "He is my Lord" can sound to
  a modern ear like the American phrase "personal Lord and Savior," which we do not use and would not
  quite recognize -- we are not describing a private feeling we each produce; we are a household reciting,
  together, what was done for each of us and for all of us at once. The claim that he is "truly God" and
  "truly man" in the same sentence is not a philosophical puzzle to us; it is why the price could be paid
  at all.
modern_rendering: >-
  And I believe in Jesus Christ, God's only Son, our Lord -- conceived by the Holy Spirit, born of the
  Virgin Mary, made to suffer under Pontius Pilate, crucified, died, and buried. He went down to the dead,
  and on the third day he rose again. He went up to heaven and sits at the right hand of God the Father,
  the Almighty. From there he will come to judge the living and the dead.

  What does this mean?

  I believe that Jesus Christ is truly God, born of the Father before time began, and just as truly man,
  born of the Virgin Mary. He is my Lord. He has bought me back -- a lost person, condemned -- and freed
  me from every sin, from death, and from the devil's power. It cost him nothing made of gold or silver.
  It cost him his own holy, precious blood, and his own innocent life and death. Because of this I belong
  to him. I will live under him in his kingdom, and serve him, made right, innocent, and blessed forever
  -- exactly as he himself is risen from death and lives and reigns forever. Yes, this is true.
relations:
- type: associated-with
  target: witt.dw.truly-god-and-truly-man
- type: associated-with
  target: witt.dw.how-the-promise-reached-us
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between B-7a and B-8) directly against
the vendored cic/texts/luther_small-catechism_smith1994.txt. `grep -n "The Second Article\|born of the
Virgin Mary, suffered\|rose again from the dead\|is risen from death, lives and reigns forever. Yes,
this is true."` returns hits at line 186 ("The Second Article"), line 190 ("Holy Spirit, born of the
Virgin Mary, suffered under Pontius Pilate,"), line 192 ("rose again from the dead, ascended to Heaven
and sat down at the right"), and line 205 ("is risen from death, lives and reigns forever. Yes, this is
true."). `sed -n '186,205p'` confirms the whole span read as one continuous unit: heading at 186-187
("The Second Article" / "On Redemption"), the creed's own wording at 189-194 (opening "And in Jesus
Christ" at 189, closing "living and the dead." at 194), "What does this mean?" at 196, and the household's
own explanation at 198-205 (opening "I believe that Jesus Christ is truly God" at 198, closing "Yes, this
is true." at 205). No word added, dropped, substituted, or reordered; blank lines in the source (188,
195, 197) are the file's own paragraph breaks, preserved here as the paragraph breaks in `text`.

This is the same passage witt.core.witt's own formation_logic and witt.voice.craft's own body note (the
"QUOTE / DOCTRINAL_WITNESS GAP" section) named as the natural ground for a future C-cell pass: "His own
word stands behind bread, behind water, behind the sentence of absolution spoken over a frightened
conscience" (witt.core.witt.formation_logic) is this same Second Article's own content, restated there in
the founder's telos language rather than the catechism's own words. It had no term, story, quote, or
doctrinal_witness record behind its own exact wording anywhere in this world's store before this record.
Ground for witt.dw.truly-god-and-truly-man (C-T: was Jesus God, did he die for our sins, is he a personal
Lord) and witt.dw.how-the-promise-reached-us (C-E: what did we have of Jesus, how did it reach us, how do
we know the resurrection happened) -- reciprocal associated-with declared on both.

speaker_or_author names the Small Catechism's own Second Article rather than a person: this is recited,
confessional text, not a remembered individual saying, and per Doc_10's own household-catechism ecology
every household under this program said these same words as its own weekly confession -- the household's
own "I" is deliberately corporate, not an invented individual's biography, matching this world's own
guard against any invented personal history.
