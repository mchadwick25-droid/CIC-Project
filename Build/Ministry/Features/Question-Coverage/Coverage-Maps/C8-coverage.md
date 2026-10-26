# C8 coverage map: women, children, the enslaved, marriage, sex

Read-only pass, 26 October 2026; nothing in the repo was edited. Eight `coverage_search.py --whole-words --regex` runs (`search/C8/S1..S8-*.json`) plus an independent front-matter grep of every record; each cited record was read and each LOADED claim checked in the vendored context. Lines, ids and verification are in `search/C8/C8-coverage.json`.

## The sub-questions

| id | sub-question | items |
|---|---|---|
| S1 | Women's lives in their own words; writing by women; nuns | C8-01, 19, 23 |
| S2 | Women leading, preaching, deacons, priests; "wives, submit"; were women lesser | C8-05, 08, 21, 26, 27 |
| S3 | The enslaved: owned, freed, thought wrong, "slaves obey", one table, the tortured witnesses | C8-03, 07, 09, 24, 28 |
| S4 | Marriage: age, consent, mixed, widows, divorce, adultery | C8-04, 06, 15, 16, 17, 25, 30 |
| S5 | Sex in marriage, virginity ranked, contraception, abortion, exposure, castration | C8-10, 12, 13, 14, 18, 29 |
| S6 | Gay people and same-sex relations (never faced as asked) | C8-11, R-06 |
| S7 | Children: raised, taught, treated | C8-02, 22 |
| S8 | A wife beaten and the church's word (Facilitator ground) | C8-20 |

Ids are C8.S1 to C8.S8. S1 and S2 are the best covered; S6 has no record anywhere; S8 is deliberately minimal.

## Layer table

R = RENDERED (a record speaks), R* = only an honest_limit or guard, L = LOADED (vendored, mapped, read in context, no record), N = nothing found. No cell is I or O alone; those are listed below.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R | R | R* | R* | R | L | R | N |
| cappadocian | R | R | R | R | R | L | R | L |
| desert | R | R | L | R | R | L | L | L |
| don | R* | R | L | R* | L | L | R* | L |
| gallic | R | L | R | R | R | L | L | N |
| hal | R | R | R* | R | R | L | R | R* |
| ijc | R* | R | R* | R | R | L | L | L |
| lpc | R* | L | L | R | R | L | R | L |
| pahc | R* | R | R | R | R | L | L | N |
| rzg | R* | R* | L | R* | R* | L | R | N |
| syr | R* | R | R* | R* | R | L | L | L |
| witt | R | L | L | R | R | N | R | N |

lpc and some don and pahc records are status draft. Worlds without records (aec, hus, jes, meth, obel, rcg, wsyr) and `fix` were not graded.

## Demonstrations in the canon cells

Counts by canon_cells: F5-I 5 (alx, gallic, hal, ijc, witt: one each); F5-T 0; F6-P 26; F6-T 7 (alx 2, hal 2, desert, pahc, syr); F6-E 2 (don, witt, both the martyr-wish question). Per world F6-P: cappadocian, desert, don, hal, ijc, pahc, syr 3 each; alx, gallic 2; witt 1; lpc, rzg 0. The women's-authority question has 8 (not gallic, lpc, rzg, witt). Divorce has 5 (alx, desert, hal, pahc, syr); cappadocian has the best witness and no demo. The question about the two tortured enslaved women (f6-e-01) has no demonstration anywhere; no demo exists for children or the enslaved (f5-i-04, 05).

## Verification

26 quote records cited as RENDERED were matched to their vendored files; all MATCH. Five needed an editorial artifact allowed for (Migne column and page markers in Macrina, footnote numbers in Palladius, a footnote marker in Aphrahat, a ligature inside an editor's note for Pliny, spacing in Timothy). None is a wording change.

## World by world

**alx.** Can say: no woman held office and none speaks (`demo.woman-authority`, `demo.women-own-words`); Origen's act, Contested (`story.origen-daring-deed`); divorce honestly unanswered (`demo.marriage-ending`). Thin: the enslaved are only a guard in `term.oikos`; abortion, rearing. Vendored in English and unused: Clement, Strom. IV.8, "Women as Well as Men, Slaves as Well as Freemen" (anf02 L38538) and "women are therefore to philosophize equally with men, though the males are preferable" (L38643); Strom. II.23 On Marriage (L34787). The limit is right that Strom. III is Latin only.

**cappadocian.** Macrina, digamy and the Gangra radicals are rendered. Vendored and unrecorded: Life of Macrina L120 (a girl raised on Wisdom and the Psalter) and L138, L158 (slave girls "as if they were sisters"); Nazianzen Or. 37, "They who made the Law were men" (npnf207 L35864); Basil's canons on abortion (npnf208 L34979), a hatchet raised at a wife (L35123), marriage without a master's consent (L36510); Gangra can. 3 (npnf214 L8641). The anti-slavery story rests on Nyssa's Ecclesiastes homily, which is unvendored.

**desert.** Rendered: Sarah ("It is I who am a man"), Talida, Pachomius's sister, Paul and the unfaithful wife. Egeria's Marthana (L3790) is loaded. Nothing on slaves (Antony "an owner of slaves", paradise-v1 L617) or children.

**don.** Limits and guards. The only vendored word on the enslaved is hostile: Augustine, Ep. 185 (npnf104 L19482), says Donatist protection let slaves destroy their debt papers and "depart in freedom". Needs a contested_claim, not a witness.

**gallic.** Brictio "purchasing slaves" and the women's houses are rendered and verified. No record on women's authority; Martin and the queen (npnf211 L4187) and Salvian on slaves and concubines (L4048, L4930) are loaded.

**hal.** Fullest. Unrecorded: Jerome Ep. 55 (npnf206 L12992-13029), where the question is a wife who left a husband "an adulterer and sodomite" and remarried; his answer: "he is still her husband". That is stricter than the Fabiola story. Ep. 22 on potions for barrenness (L5787) is also unrecorded.

**ijc.** Women: Justina only. Marriage ranked is rendered. Vendored, unrecorded: CTh 3.7.2 (no Jew to take a Christian woman; "adulterii vicem", codex L942), 3.7.1 (young widows remarry by their fathers' choice, L940), 4.7.1 (freedom given in church, L1182), 5.10.1 (a bought foundling may be kept in servitude, L1496); Sozomen's deaconess (npnf202 L43214).

**lpc.** Draft records only on marriage, chastity, infants. Loaded: City of God XIX.15, "the condition of slavery is the result of sin" (npnf102 L38914); Cyprian to Fidus on infants (anf05 L35860-35947); Ep. 211 to the nuns (npnf101 L54738). Perpetua's own prison account (anf03 L59560) is vendored and mapped but excluded as pre-246.

**pahc.** The only world that renders Pliny's two women with the source, and the only one with Thecla mapped ("Go, and teach the word of God", anf08 L48096). Unrecorded: Justin 1 Apol. 27 and 29 (exposed children; a petition to a surgeon, anf01 L14973, L15045); Athenagoras 35 (abortion is murder, anf02 L13350).

**rzg.** `limit.no-teaching-on-wealth-or-marriage` says the teaching cannot be given, yet Calvin Inst. (vol1 L25853, vol3 L11100) and Second Helvetic ch. XXIX (L1525) are vendored. Dentiere is registered and unvendored.

**syr.** Limits say no woman's line and no ruling on divorce survive. Loaded against that: Egeria on Edessa (L3339-3403); Aphrahat Dem. VI.4-7, celibate men and women under one roof (npnf213 L25834-25951); the Book of the Laws of Countries, where Christians "in Edessa" do not kill an unchaste wife or sister "but they withdraw from them" (anf08 L68966-68985).

**witt.** Women: one sentence. Luther's "the men, priests, the women, priestesses" (luther_works-v1 L11754) is loaded for S2. Marriage and chastity are rendered as terms, not quotes. Children rest on the catechism prescription, rated Inferential-Thin.

## S6: what the sources say and where they are silent

No record in any world treats it. The ten "someone like me" demos (all but lpc and rzg) answer entry and belonging in general terms and do not mention it. In `pahc.story.two-ways-catechumen` the Didache list carries the word "pederasty" and no more. `alx.quote.clement-instructor` concerns disordered passions of the soul (its not_for says so).

What vendored sources say, read in context: Clement, Paed. III.3 and III.8 (anf02 L24945-24986, L25559-25570): practices "contrary to nature"; the Sodomites "burning with insane love for boys", Sodom burned as an example. Basil Ep. 188 can. 7 (npnf208 L35084): "Abusers of themselves with mankind, and with beasts" fall under the same penalty as murderers and adulterers. Augustine, Conf. III.8 (npnf101 L6021): offences "contrary to nature" are "to be held in detestation and punished". Jerome Ep. 55 (above). Salvian (L9528) quotes Romans 1:26-27 of Africa. Barnabas 10 (anf01 L12629) and Justin 1 Apol. 27 (L14973). The Book of the Laws of Countries (anf08 L68980): "The brethren who are in Gaul do not take males for wives."

Silent, as far as read: no Desert Sayings, Donatist, Aphrahat or Ephrem, or Wittenberg passage was found; no passage read speaks in the voice of a person describing their own attraction or partnership. Not read in context: Chrysostom on Romans (npnf111), Calvin on Genesis 19.

## S8: after the redirect

Facilitator ground. A voice could truthfully say only: Basil's canon names a man who raises a hatchet against his wife in rage a murderer, with intent weighed (cappadocian); Jerome writes that what is forbidden to women is forbidden to men, and that Fabiola left a husband whose vices a whole neighbourhood knew and was received back (hal); Augustine records that wives in Monica's town "carried the marks of blows" and that she blamed their tongues (npnf101 L13983; lpc, don, ijc, hal). That last is history, not counsel, and should not be spoken as advice. No record names a husband's blows; no world can say what a church did in a particular case.

## Other sources (outside the repo; working knowledge, not fetched)

Didascalia Apostolorum (Gibson 1903, PD) for syr, alx and pahc; Nyssa Hom. Eccl. 4 (Greek PD; Hall 1993 in copyright); Dentiere's 1539 Epistre (French PD); Argula von Grumbach's letters (German PD; Matheson in copyright); Luther's Estate of Marriage (WA PD); Rabbula's Rules (Overbeck 1865). Chrysostom Hom. 20 on Ephesians is vendored (npnf113) but mapped to none of the twelve worlds. Per-world detail in the JSON.

## Not checked

- Grep covered front matter only; record bodies were read only for cited records.
- Vendored hits marked "not read" are leads; many S5 and S7 hits are noise.
- Non-English files were counted, not read. `canon/sealed_probes/` was not read; no model call, no network.
- Which draft records are in the compiled package was not checked.
