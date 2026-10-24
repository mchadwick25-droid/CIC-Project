# Cappadocia: records citing the five unvendored sources, assessment, 2026-10-24

Independent Opus assessment (read only, no model calls) of the 19 records that cite the five Cappadocian sources that are not in the English Library: `basil-against-eunomius`, `gregory-nyssa-in-xl-martyres-ii`, `gregory-nazianzus-de-vita-sua`, `gregory-nazianzus-on-the-mamas-festival`, `gregory-nyssa-de-pauperibus-amandis`. The fixing session spot-checked the decisive passages (Letter CCXXXIV, Sasima letter, Life of Macrina 212, the PG36 and PG37 headers).

Path keys: N205 = `cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt`; N207 = `cic/texts/npnf207_cyril-jerusalem-gregory-nazianzen.xml`; N208 = `cic/texts/npnf208_basil-letters-select-works.xml`; N202 = `cic/texts/npnf202_*` (Socrates, Sozomen, Theodoret); LM = `cic/texts/gregory-nyssa_life-of-macrina_clarke1916.txt`; BR = `cic/texts/basil_ascetic-works-longer-shorter-rules_clarke1925.txt`; PG36 = `cic/texts/gregory-nazianzen_orationes-27-45-pg36-grc-lat_migne1858.txt`; PG37 = `cic/texts/gregory-nazianzen_epistulae-carmina-pg37-grc-lat_migne1857.txt`.

## Method question for the project lead (not decided here)

De vita sua (PG37 file line 85705 onward) and Oration 44 with the Mamas passage (PG36 ~:52123) are held as Migne's Greek. It is OCR, and the file headers say nothing in it is quotable until checked against the scanned page. No source record covers either file. Whether records may rest on these OCR Greek texts is a method decision. Until it is made, claims that rest only on them are hedged or lowered, not deleted.

## Cross-cutting fixes
- `cappadocian.source.sasima-letters`: `kind: unvendored` contradicts its own edition note. The letters are in N207 (e.g. :45796 "because I did not accept your Sasima"). Set `kind: vendored`.
- `cappadocian.source.gregory-nazianzus-on-the-mamas-festival`: "only Epp. 101, 102, 202" undercounts. N207 has a Basil-correspondence division (:45110) and a miscellaneous-letters division (:46022). Correct the edition note.
- `cappadocian.source.gregory-nyssa-in-xl-martyres-ii`: "zero occurrences of 'Forty Martyrs'" is wrong. N205:588-589 reads "in honour of the Forty / Christian Martyrs" (editor's prolegomena, not the homily). Correct the note.
- Remove `license: public-domain` from `sources` entries that point at unvendored sources (akatalepsia, epinoia-energeia, panegyris, philoptochia, hesychia, philotimia).

## Per record

**contested.agennetos-transmission.** Basil's own words survive, quoted by Nyssa: N205:26158-26166 ("We call the Universal Deity … imperishable and ungenerate … and we arrive at these names by Conception"), source `gregory-nyssa-against-eunomius`. Re-ground the Basil content there. The body note calls Basil's treatise vendored; reword it to "has no vendored file; npnf208's Prolegomena summarizes it". Ratings fit.

**term.akatalepsia.** The plain_meaning is supported by Basil, Letter CCXXXIV, N208:40273-40276 ("we know our God from His operations, but do not undertake to approach near to His essence"), source `basil-letters-general-corpus`. Re-ground. The divergence_note leans on Letter XVI, which concerns created things; reword it to cite Letter CCXXXIV.

**term.epinoia-energeia.** Add `gregory-nyssa-against-eunomius` (Nyssa quoting Basil on names "by Conception", N205:26158-26166) and Letter CCXXXIV (N208:40273-40276). Reword the divergence_note away from Letter XVI.

**force.eunomian-movement.** Basil's refutation is attested in editorial text: N205:2829-2831; N208:24107-24109. Separate churches and rebaptism: Sozomen, N202 ~:39114-39117 and ~:39152-39154, source `church-historians-socrates-sozomen-theodoret`. "born in Cappadocia" is not stated outright; N205:3272-3274 says Corniaspa, with "half-Galatian extraction". Soften it. Documented holds only with these sources added. The Against Eunomius locus should say the work is named, not held.

**figure.emmelia.** The relics claim rests on editorial prose: N208:1012-1019. Re-ground as secondary authority. Parentage: LM:44. Add `gregory-nyssa-life-of-macrina`. The divergence_note overclaims Nyssa's own credit; reword to "reported by modern editors; the homily itself is not held". Ratings fit.

**story.forty-sebaste.** The passion details rest on the editor's summary, N208:7755-7768 ("plunged for a whole night into a frozen pond in the city"). Add that locus. "frozen lake" → "frozen pond", or keep it under the record's existing "as our church remembers it" frame. Ratings fit.

**force.persecutions-nearness.** Confessor grandparents: LM:212 ("My father's parents had their goods confiscated for confessing Christ. Our maternal grandfather was slain by the imperial wrath"). Add `gregory-nyssa-life-of-macrina`. The relics on the estate are editorial (N208:1012-1014): rate that element Widely Accepted. Reword the locus that implies the homily was read. Documented holds once the Life of Macrina is added.

**gravity.hesychia-summons.** Every claim is vendored without De vita sua: Basil's Pontus retreat, N208:23988-24003 (Letter XIV); Sasima, N207:45796-45799; the resignation, N207:40838 and :40877 (Or. 42). Replace De vita sua with `basil-letters-general-corpus` and `gregory-nazianzus-orations-general-corpus`. Documented fits.

**figure.gregory-of-nazianzus.** The bridge_line is vendored: N207:45798; :23128-23131; :40877. Re-ground. The locus "his own verse autobiography" treats it as held; drop it pending the method question.

**story.gregory-constantinople.** The Anastasia, the council, the canonical dispute and the resignation are vendored: N207:23122-23124; :23176-23181; :40853. Re-ground. "One Easter, a mob attacked the gathering itself" is found only in De vita sua and could not be checked even in the PG37 Greek. Remove it, or hedge it pending the method question. The text field says the account comes from De vita sua; reword it. Ratings fit.

**story.sasima-wound.** The province split, Anthimus and the new sees are vendored: N207:22975-22984. "for Basil's need": N207:45784-45786. "withdrew to help his father": N207:22994-22997. Re-ground. "a waystation without a people or a spirit of its own" goes past the Greek (PG37 ~:88184-88203: a staging post, waterless, without a crowd, not free, all dust, noise and carts, its people strangers and vagrants; nothing about "spirit"). Hedge it to what the Greek says, or cut it, pending the method question. Reconcile the divergence_note with the sasima-letters record's state.

**story.athens-friendship.** Grounded in Or. 43: N207:41521-41522 ("one soul, inhabiting two bodies"); :41487-41488; :41526-41527. Drop De vita sua. The bee image is used of Basil's schooling (N207:41302-41303), not as Gregory's; reword it.

**term.philotimia.** Grounded in Or. 42: N207:40726-40732 and :40672. Re-ground to `gregory-nazianzus-orations-general-corpus`, Or. 42 §§19, 22. Replace the De vita sua source.

**term.hesychia.** Vendored: N207:45237-45239 ("Your roofless and doorless hut"); N208:23988-24003. Replace De vita sua with the sasima-letters record and Basil Letter XIV.

**force.family-archive-transmission.** Gregory gathering his own letters is Ep. 52, held only in PG37 (~:7560-7561). Rate that element Widely Accepted pending the method question. "Nyssa completes his brother's works" rests on On the Making of Man, N205:34007-34014; re-ground to `gregory-nyssa-on-the-making-of-man`. Fix the locus. Documented holds only after re-grounding.

**force.paideia-ladder.** Caesarea, Byzantium and Athens, and the friendship, are in Or. 43: N207:41303, :41337, :41341-41342, :41521. Replace De vita sua with `gregory-nazianzus-oration-43-funeral-encomium-basil`. Reword the divergence_note. Documented fits.

**story.panegyris-shrine.** The Mamas passage is only in PG36 Greek (~:52123-52126), and the feast date comes from Migne's note (~:51133-51135). Hedge it pending the method question. Add Basil, Longer Rule XL, BR:17554-17558 ("buying and selling conducted at martyrs' tombs is not fitting for us"), source `basil-asketikon-longer-shorter-rules`. "preachers complain" cannot be checked; keep the existing hedge.

**term.panegyris.** "The Mamas festival evidence is verified-via-authority" is false; lower it to named-not-rechecked. Add Rule XL (BR:17554-17558). "preachers worked the crowd" cannot be checked; reword or drop it. Fix the locus. Widely Accepted holds only with Rule XL added; otherwise Inferential-Thin.

**story.poorhouse-famine-month.** The new city, the infirmary and the lepers are vendored: N207:42736-42737; N208:30019-30023; N207:42783. Re-ground. "a direct test of what love of the image of God … meant" → Or. 43's own wording, "sympathy is put to the test", N207:42746-42747.

**term.philoptochia.** "Nazianzen's Oration 14 … which is vendored" is false (only a title at N207:23339). Correct it. All three cited sources are unvendored. Re-ground the supported parts: grain from hoarders, N207:42005-42006; the guest-house, infirmary and leper-house, N208:30019-30023 and N207:42783. "poor bear the image of God" and "beyond their own need … belongs to the hungry" cannot be checked; reword them or rate them Inferential-Thin.
