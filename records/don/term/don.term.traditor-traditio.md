---
id: don.term.traditor-traditio
world_id: donatism
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- C-E
- F4-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Doc_04 SS3.1''s own Confidence/Gravity Cross-Check splits this term in two and this record
    keeps the split. The doctrine''s existence and centrality are Documented: Petilian of Constantina''s own quoted
    proposition -- ''Conscientia namque dantis attenditur, quae abluat accipientis'' -- was re-verified directly
    against the vendored npnf104 file (Doc_05 SS1, line 10280), and the Maximianist affair''s own logic presupposes
    the doctrine as settled Donatist teaching rather than a hostile invention. The specific argumentative texture
    -- exactly how the Donatist side reasoned from traditio to invalid ordination to invalid sacrament -- survives
    substantially inside Augustine''s refutation of it, and the Acta Purgationis Felicis reaches this record through
    Optatus''s own selection and framing of his Appendix, court-acts character notwithstanding (Doc_02 SS1, Doc_03
    Cluster 1).'
sources:
- source_id: don.source.optatus-appendix-of-documents
  locus: the Acta Purgationis Felicis (314) -- the founding accusation against Felix of Aptungi
  license: public-domain
- source_id: don.source.augustine-answer-to-petilian
  locus: Petilian's own quoted proposition on the conscience of the giver (verified against npnf104)
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: Books I-II on the 311/312 consecration of Caecilian
  license: public-domain
- source_id: don.source.cyprian-epistles
  locus: the third-century North African purity theology this doctrine sharpens
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - a participant uses 'traditor' or 'traditio', or asks why a minister's conduct under a past persecution mattered
    so much
  - a participant asks why one bishop's consecration split a whole church
  - the conversation reaches the origin of the schism, or who has the right to ordain or baptize
  prefer_instead:
  - the question is about persecution or martyrdom generally, with no reference to the surrender of scripture
relations:
- type: presupposes
  target: don.term.purity-ministerial
- type: presupposed-by
  target: don.term.rebaptism
- type: presupposed-by
  target: don.term.caecilianist
- type: associated-with
  target: don.term.episcopus
- type: associated-with
  target: don.term.reception-without-reordination
plain_meaning: When the persecutor came, some clergy handed the scriptures over to be burned. We call such a man
  a traditor. His hand is no longer clean. He cannot ordain, baptize, or bless. What flows from that hand is nothing
  at all.
world_word: traditor / traditio
false_friend:
- traitor in the modern political sense -- a spy, a turncoat, a betrayer of a nation
- an old grudge over past cowardice that reasonable people would have let go of
- a procedural technicality about who signed what, rather than a claim about the sacrament itself
- handing on the faith (the ordinary, positive sense of tradere) -- here the word names the opposite act
senses:
  informational: Diocletian's edict of 303 demanded the surrender of scriptures and sacred vessels. Some African
    clergy complied and some refused and suffered. When Caecilian was consecrated bishop of Carthage in 311/312,
    the objection was that his consecrator, Felix of Aptungi, had been a traditor -- so the whole line running
    out of that consecration was held defective at its root. The Acta Purgationis Felicis (314), Felix's own hearing,
    is the founding documentary record of the charge.
  evidential: 'Documented at its core on cross-voice grounds, not on Augustine''s characterisation alone: Petilian
    of Constantina argues the doctrine in his own quoted words, and the Maximianist affair presupposes it independently.
    What is Augustine-mediated is the argumentative texture -- the step-by-step reasoning as this record can now
    reconstruct it. Optatus''s Appendix supplies the Felix documents, and Doc_02 SS1 places even those inside
    the Author-Gravity concentration, since Optatus chose what to include and how to frame it.'
  personal: 'This is not vindictiveness toward one long-dead man. It is the ordinary believer''s own question
    at the font, asked in public: whose hands are these, and what stands behind them? A man who gave up the scriptures
    to save himself showed, in the one moment that tested him, what his hand was worth.'
  translational: A modern hearer asks, 'why not just forgive him and move on?' -- but forgiveness of the man was
    never the question here. The question was whether his hand could still give what he claimed to give, and a
    whole century of baptisms and ordinations hangs on the answer. To waive the charge would concede that a sacrament
    is valid whatever the minister is, which is precisely the claim this communion was founded to refuse.
quick_meaning: The one who handed over. A hand that failed then can give nothing now.
distortion_risk: high
prior_sense: 'In ordinary Latin, tradere is simply to hand over or hand on, and traditio is the handing on --
  the same root the wider church uses for the faith delivered from the apostles. The persecution narrowed it to
  one act: handing the scriptures to the man who came to burn them.'
---
Built from Doc_06 SS1 entry 001 (Tier 1, confirmed) and the deployment chunk `Lexicon-Chunks/donlex001_traditor-traditio.md`. Confidence split (core Documented / argumentative texture Augustine-mediated) carried from Doc_04 SS3.1 rather than flattened. Tags AS/DR/TC/RT per `Lexicon_Deployment_Index.xlsx`.
