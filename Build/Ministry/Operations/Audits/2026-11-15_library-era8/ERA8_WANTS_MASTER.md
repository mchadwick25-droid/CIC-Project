# Era 8 (1650-1815) source wants: master list

Compiled 2026-11-15, read-only, from the repo as it stands. Sources: A = `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (rows 121-162); B = `Build/Ministry/Features/Source-Library/CFT-Wants.md`; C = `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (entries 175-182, 225); D = Eras 8-9 global sweep; E = `2026-11-12_who-scan-era8/`; census = `cic-website/data/world-census.json`; shelf = `ls cic/texts` (1,926 files).

## 1. Counts

- **83 master wants** (de-duplicated), plus **16 council leads** that are not on any wanted list (group 12, listed apart).
- 40 of the 83 come from A (42 rows; rows 122, 153, 154 share one source and are one master row). 43 come from B and C only.
- Major (A): 8 rows (121-128). Open-Gaps 225 lists only 7 as major (it leaves out Occom, row 128).
- Per group: 1 Orthodox 8 | 2 Oriental Orthodox, CoE, Eastern Catholic, India 12 | 3 Africa 5 | 4 Asia 10 | 5 Latin America 6 | 6 Catholic Europe 9 | 7 German-speaking Protestants 7 | 8 Nordic 2 | 9 British Isles 10 | 10 Methodists 1 | 11 North America 9 | 12 councils 0 formal (16 leads) | 13 other 4.
- A's Outside-witness section (rows 1-27) and Council section (rows 1-46) have **no Era 8 rows**: outside-witness rows are eras 5-7, council dates run 377-2010 with none in 1650-1815.
- Count mismatches to know about: A and the Who scan say WANTED 42 (409 rows); Open-Gaps 225 says WANTED 44 (411 rows). The two extra are Herman of Alaska and Philiphe Binh, who A files in era 9 (rows 226, 288). They are included here, flagged. A127 dates Rego 1744; Open-Gaps 178 says 1745.
- Not counted (filled already in B, so no longer wants): Tolstoy, Dukhobors, Haiti (Moreau de Saint-Mery), Cuba/Claret, Bethlemites, Korea, Marsden, Carthusians, Cistercians (Rance), Jesuits (Thwaites 36-40, Lettres edifiantes t19-22), Quebec, Rabinowitz, Unitarians of Transylvania, Waldensians (Arnaud), Remonstrants, Church of Scotland, Delaware Swedes.

Columns: id | person or entry served | named source (as given) | major? | held in cic/texts | earlier search result (B) or Open-Gaps note.
Id key: A### = Wanted_Sources.md row number; OG### = Open-Gaps entry; B2/B3/B5/B6 = CFT-Wants batch; E-lead = Who scan council leads.

## 2. Tables by group

### (1) Orthodox: Greek East, Russia, Romania, Balkans, Georgia

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A149 | Tikhon of Zadonsk; Russian Church (Nikon to Holy Synod) | "A life by a disciple: Ivan Chebotarev (the monk who served him), Life of Tikhon of Zadonsk (late 18th c.) [suggested; to confirm]; and his Of True Christianity [suggested; to confirm]" | no | `tikhon-zadonskii_nastavleniia-dlia-monashestvuiushchikh-rus_kiev1854.txt` (counsels only); no Life | not in B |
| A161 + B2 RV-9 + OG182 | Kosmas Aitolos; Orthodoxy under the Ottomans | "Kosmas, Didachai (Teachings) and a Life, English in Vaporis, Father Kosmas, the Apostle of the Poor (1977) [suggested; to confirm]". Census (VII.18 story) also names Sapfeiros Christodoulides, Life of Kosmas the Aetolian (Venice, 1814) | no | none | B2: not found; all printings found date from 1966 or later. OG182: waits for a pre-1930 text |
| A162 | Athanasios Parios; Kollyvades / Hesychast revival | "Athanasios Parios, Christianike Apologia (1798), and a modern life [suggested; to confirm]" | no | none (Nikodemos's Pedalion and Synaxaristes are held, not his) | not in B |
| A150 | Ioan Inocentiu Klein; Romanian Greek Catholic church (VII.49) | "Augustin Bunea, Episcopul Ioan Inocentiu Klein (1728-1751) (Blaj, 1900) (named by the census) and Nicolaus Nilles, Symbolae ad illustrandam historiam ecclesiae orientalis, vol. 2 (Innsbruck, 1885) [suggested volume; to confirm]" | no | none (Nilles not in cic/texts; census read it online; Open-Gaps says the scan used is damaged) | not in B. OG180: a less damaged Nilles scan wanted |
| OG180 ME-8 (era 8 remainder) | Romanian Greek Catholics 1751-1815 (Sofronie, Supplex Libellus Valachorum, Orthodox resistance after Visarion) | "Bunea's or Iorga's later volumes, or Nilles for the later documents" (no title given) | no | none | not in B |
| OG180 ME-8 (Ruthenian) | Carpathian Ruthenian union after 1652; Ruthenian Uniate (VII.28) | "a nineteenth-century source and Nilles's Munkacs entries re-read"; Nilles's index gives 1771 for first bishop of Munkacs | no | held: `harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt`, `pelesz_geschichte-der-union-bd2-deu_1880.txt`, `basilovits_brevis-notitia-fundationis-koriathovits-pars1-lat_1799.txt`, `wazynski_katechizm-albo-krotkie-zebranie-nauki-chrzescianskiey-pol_1792.txt`; no Nilles | not in B |
| B5 | Ukrainian Orthodoxy after 1700 (no entry; shelved needs-ruling on Russian Church) | later documents after the 1770s | no | `arkhiv-iugo-zapadnoi-rossii_ch1-t2-pravoslavie-v-zapadnoi-ukraine-xviii-rus_1864.txt`; `kiev-academy_akty-i-dokumenty-t1-ch2-1721-1750-rus_petrov.txt` | B5: filled to the 1770s only |
| B3 + B-later + OG179 | Georgian Church 1650-1811 (VII.39) | Brosset, Histoire de la Georgie, first livraison (1856), Additions (1851), part II (1856-57), "modern volumes (1856-58)". Census VII.39 also names P. Ioselian, A Short History of the Georgian Church, tr. S. C. Malan (London, 1866) | no | `brosset_histoire-de-la-georgie-pt2-histoire-moderne-livr2-fra_1857.txt`, `brosset_histoire-de-la-georgie-pt1-fra_1849.txt`, `kartlis-tskhovreba_histoire-de-la-georgie-pt1-histoire-ancienne-fra_brosset1849.txt`; Ioselian none | B3: 1856 first livraison not found; queued: Additions (1851), part II (1856-57) |

### (2) Oriental Orthodox, Church of the East, Maronite / Melkite / Eastern Catholic, India (Thomas Christians)

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A152 | Ibrahim al-Jawhari; Copts under the Ottomans (VII.34) | "al-Jabarti, Aja'ib al-athar (Cairo chronicle, obituary of Ibrahim al-Jawhari) [suggested; to confirm]; Butcher, The Story of the Church of Egypt, vol. 2 (London, 1897) as named in the census" | no | none of either (held Egypt outsiders: `renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt`, `abu-salih_churches-and-monasteries-of-egypt_evetts1895.txt`, `volney_travels-through-syria-and-egypt-v2_1788.txt`, `leo-africanus_*`) | not in B |
| OG175 | Coptic patriarchate and archons under the Ottomans | "the Arabic History of the Patriarchs for the Ottoman patriarchs; Vansleb, Histoire de l'Eglise d'Alexandrie (1677); the archons' letters and waqf deeds, and Magdi Guirguis on the Jawhari brothers" | no | none (no Vansleb) | not in B |
| OG175 AF-7 | Coptic Catholics (patriarchate named 1824, filled 1895; Rome's line from 1741) | "a source for 1824 and 1895" (Butcher's account of 1741 only read) | no | none | not in B. Mostly era 9 |
| A151 | James Bruce of Kinnaird (outside witness if held); Ethiopia Gondar (VII.38); also Copts | "James Bruce, Travels to Discover the Source of the Nile, vols. 2 and 3 (Edinburgh, 1790)" | no | none (Ludolf 1682 and 1691, Lobo, Telles, Alvares held) | not in B. OG175 also wants "a modern study of James Bruce as a witness" |
| OG175 AF-1 | Ethiopia, Zemene Mesafint (start 1769) | "Guidi, Annales (CSCO, 1903-05; lending-only copies on archive.org); Weld Blundell (Cambridge, 1922; not found on archive.org by title)". Census VII.38 also names Samuel Gobat, Journal of a Three Years' Residence in Abyssinia (London, 1834) | no | none (the Guidi files held are other works) | OG175: not found on archive.org |
| OG179 ME-2 | Maronite Church, 1736 Synod of Mount Lebanon (VIII row waits for it) | "Mansi vol. 38, Collectio Lacensis vol. 2 (1876) or another public-domain edition of the acts" | no | none; Collectanea v1 quotes its canons (`propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt`) | B4: not found in a readable printing (Zainati 1926 unreadable); Anaissi's Bullarium not found. Mansi 38 not on archive.org |
| OG179 + B4/B5 | Maronites: a clean Duwayhi | Duwayhi, Tarikh al-ta'ifa al-maruniyya (clean scan) | no | `duwayhi_tarikh-al-ta-ifa-al-maruniyya-ara_shartuni1890.txt`; `duwayhi_tarikh-al-taifa-al-maruniyya-ara_shartuni189x.txt` (both damaged OCR) | B4/B5: clean witness still wanted |
| E (OG225 note) | Melkite Greek Catholics: 1724 split (VII.23) | Charon, Histoire des patriarcats melkites, tome I (tome I tells the 1724 split) | no | `charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt` (t2, t3 only) | a Library defect, not a named want |
| B2 ME-7 + B3 + OG179 | Syriac Orthodox and Syriac Catholic split, c. 1650-1906 | "a Syriac or Arabic chronicle of the patriarchate after 1369, or Parry (1895)"; "Wright's catalogue of Syriac manuscripts (dated colophons) is the next lead" | no | `assemani_bibliotheca-orientalis-tomus1-de-scriptoribus-syris-orthodoxis-lat_1719.txt` and Tomus 3 pars 1 and 2; Badger v1, v2 (outsider) | B2: not found (Rabbath 1910 and Southgate 1856 are outsiders). B3: not found (Bruns-Kirsch 1789 scan unreadable) |
| OG177 AP1 | St Thomas Christians (VII.48) | "Paremmakkal Thoma Kathanar, Varthamanappusthakam (c. 1790; no pre-1930 printing found)" | no | none | OG177: no pre-1930 printing found |
| OG177 AP1 | same: Malankara and Catholic party documents | "the Malayalam originals of the Malankara history (Whitehouse App. D) and the Angamaly document of 1787 (App. E)" | no | English in `whitehouse_lingerings-of-light-in-a-dark-land_1873.txt`; no Malayalam | not in B |
| B5 + OG225 | St Thomas Christians: Puthenkoor (Malankara) own text; Mar Thoma I, Mar Dionysius I, Archdeacon Thomas | "No Puthenkoor text of its own was found." Archdeacon Thomas (Coonan Cross) "suggested WANTED" (OG, era 7 note); Mar Thoma I and Mar Dionysius I WHO "no own text held" | no | `paulinus-a-s-bartholomaeo_india-orientalis-christiana-lat_1794.txt`, `buchanan_christian-researches-in-asia_1811.txt`, `geddes_history-of-the-church-of-malabar-synod-of-diamper_1694.txt`, `raulin_historia-ecclesiae-malabaricae-cum-diamperitana-synodo-lat_1745.txt`, `philipos_syrian-christians-of-malabar_howard1869.txt`, `sebastiani_prima-speditione-indie-orientali-ita_1666.txt` and seconda, `vincenzo-maria_viaggio-indie-orientali-ita_1672.txt` | B5: filled, outsiders only |

### (3) Africa (other than Copts and Ethiopia, which are in group 2)

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A122 + A153 + A154 + OG175 | Dona Beatriz Kimpa Vita (A122); Bernardo da Gallo (A153); Pedro IV of Kongo (A154); Antonian movement (VII.11) | "Bernardo da Gallo, Relatione (Capuchin relation on the interrogation, trial and burning, 1706) and Lorenzo da Lucca's relation, both named in the census; Brasio, Monumenta Missionaria Africana, for the Portuguese-side documents [suggested; to confirm the volume]"; Zucchelli's Italian original of 1712 [suggested; to confirm]; OG175: "the Capuchin manuscripts of Antonio de Teruel and Bernardo da Gallo" | A122 yes | none of da Gallo, da Lucca, Brasio. Held: `zucchelli_missions-und-reise-beschreibung-nach-congo-deu_1715.txt`, `cavazzi_istorica-descrizione-tre-regni-congo-matamba-angola-ita_alamandini1687.txt`, `carli_viaggio-nel-regno-del-congo-ita_guattini1671.txt`, `merolla_breve-e-succinta-relatione-viaggio-congo-ita_piccardo1692.txt`, `paiva-manso_historia-do-congo-documentos-por_1877.txt`, `lopes_report-of-the-kingdom-of-congo_hutchinson1881.txt` | not in B as a row |
| OG175 AF-3 + B5 | Kongo after 1650 (VII.42), about 1720-1879 | "Kongolese letters to Rome and Lisbon"; a read of Merolla, Zucchelli, Proyart (1814) for 1680-1760; a source for 1720-1879 | no | `bentley_pioneering-on-the-congo-v1_1900.txt`, `-v2_`; Proyart not held | B5: filled from held texts plus Bentley; no other Kongolese text found |
| B2 AF-8 + OG175 | West Africa before the mission societies (Quaque, Capitein, Freetown settlers) | "Capitein, Quaque, Thompson" ; "a pre-1930 source for Quaque (SPG) and the Freetown settlers' churches, opened raw"; Capitein only in a 2001 translation | no | none | B2: Thompson 1758 image-only scan, nothing readable; no printing of Capitein or Quaque before 1931 found |
| OG175 AF-4 | Dutch Reformed Church at the Cape (VII.46) | "the Acta Synodi of 1857 in Dutch and a pre-1930 history of the Dutch Reformed Mission Church". Census VII.46 reads McCarter, The Dutch Reformed Church in South Africa (Edinburgh, 1869) | no | none (McCarter not vendored) | not in B. Mostly era 9 (1857, 1881) |
| OG175 AF-5 | Southern African mission churches (Xhosa) | "Ntsikana's hymn in Xhosa from a pre-1930 printing" | no | none | not in B |

### (4) Asia: Catholic missions and local churches (China, Vietnam, Japan, Ceylon, India, VOC world)

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A124 | Charles Maigrot; Chinese Catholicism (VII.36) | "Maigrot's Mandate of 1693 (Fujian) in a contemporary printing; Launay, Histoire generale de la Societe des Missions-Etrangeres, vol. 1 (Paris, 1894), named in the census, for the life [suggested; to confirm the printing of the mandate]" | yes | none of the Mandate or the 1894 Launay. Other Launay: `launay_histoire-des-missions-de-chine-kouy-tcheou-t1-fra_1907.txt`; `propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt`; `lettres-edifiantes_memoires-de-la-chine-t19-fra_1781.txt`, `-t20-`, `-t22-` | not in B as a row |
| A125 | Francois Pallu and Pierre Lambert de la Motte (pair); Chinese and Vietnamese Catholicism | "Pallu's and Lambert's own Relations and letters, and Launay, Histoire generale ... vol. 1 (Paris: Tequi, 1894), named in the census; the Monita of the first vicars [suggested; to confirm the early printing]" | yes | none | not in B |
| A126 | Alexandre de Rhodes; Vietnamese Catholicism to 1815 (VII.45) | "Rhodes, Divers voyages et missions (Paris, 1653), his own life-telling [suggested; to confirm]; the Catechismus of 1651 (Propaganda) as the work". OG178: the Catechismus "the teaching and not only the title page" | yes | none | not in B |
| A127 + OG178 | Joseph Vaz; Catholics of Dutch Ceylon (VII.47) | "Sebastiao do Rego, Vida do veneravel padre Joseph Vaz (Lisbon, 1744) [suggested; to confirm]; the Sketch of the Rise and Progress of the Catholic Church in Ceylon (Colombo, 1848), named in the census". OG178: Rego "(1745)"; "Tamil and Sinhala Catholic texts" | yes | none (1848 Sketch read online, not vendored) | not in B |
| A156 + OG178 | Philippus Baldaeus; Ceylon; VOC world | "Baldaeus, Naauwkeurige beschryvinge van Malabar en Choromandel ... en het machtige eyland Ceylon (Amsterdam, 1672) [suggested; to confirm]". OG178: "the Dutch proclamations of 1658 and 1715 against Catholics in Ceylon and a Dutch Reformed account of the Ceylon church" | no | none | not in B |
| OG178 | Protestant churches of the VOC world (VII.43) | "Valentijn, Oud en Nieuw Oost-Indien (1724-26), the Leijdecker Bible of 1733 and Ambon church records" | no | none | not in B. No A row. OG186: dated record of the Protestant Church of the Moluccas also wanted (not PD) |
| E / OG225 (A288 is era 9) | Philiphe Binh; Vietnamese Catholicism | "Binh's own notebook and writings (Sach so sang chep cac viec) [suggested; to confirm]; George E. Dutton, A Vietnamese Moses (UC Press, 2017), open access, named in the census"; OG178: "Sach so sang chep cac viec (1822; no pre-1930 printing found)" | no | none | OG178: no pre-1930 printing found. Date of work 1822 is era 9 in A |
| B5 + OG177 | Chinese Catholics, a Chinese voice (VII.36) | "Huang Bolu, Zhengjiao fengbao (1883), for the 1692 edict and the 1723 memorial"; "Andreas Ly's Journal, the 1803 Sichuan synod" | no | none | B5: outsider only; Chinese Catholic's own text not found |
| B5 + OG177 | Japan's hidden Christians (VII.41) | "Tenchi hajimari no koto, the hidden Christians' own text"; orasho; "a Japanese source for the village communities"; Urakawa Wasaburo, Kirishitan no fukkatsu (1927-28) | no | `marnas_religion-de-jesus-ressuscitee-au-japon-t1-fra_1897.txt`, `-t2-` (French, mediated) | B5: no orasho or Tenchi hajimari printed before 1931 found |
| OG177 AP11 | Russian mission in Peking and the Albazinians (1685-) | "Widmer (1976) or a pre-1930 work on the mission and the Albazinians" | no | `adoratskii_pravoslavnaia-missiia-v-kitae-vyp1-1685-1745-rus_1887.txt`, `-vyp2-1745-1808-` | B2: filled to 1808; Widmer not found on archive.org |

### (5) Latin America and the Caribbean

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A123 | Antonio Vieira; Colonial Latin American devotional Catholicism (VII.17), Society of Jesus row | "Vieira, Maria Rosa Mystica (Lisbon, 1686), named in the census; a life-bearing source: Andre de Barros, Vida do apostolico padre Antonio Vieira (Lisbon, 1746) and the Cartas [suggested; to confirm]" | yes | none. OG176: Vieira (1686) "read raw online and ready to vendor" | not in B |
| OG176 LA8-4 | Colonial Brazil (strand of VII.17) | "Antonil (1711)" (Cultura e opulencia do Brasil, Lisbon: Officina Real Deslandesiana, 1711, as named in census VII.17) | no | none | not in B. OG176: ready to vendor |
| A155 | Ursula de Jesus; VII.17 | "The Souls of Purgatory: The Spiritual Diary of a Seventeenth-Century Afro-Peruvian Mystic, ed. and trans. Nancy van Deusen (UNM Press, 2004), named in the census. A 2004 translation: the Library must check rights, and the Spanish edition of the diary may be needed." | no | none | not in B |
| OG176 LA8-10 + B2 | Virgin of Cancuc (1712); Talking Cross | "Francisco Ximenez's chronicle for Cancuc, a dated Cruzob text"; no Maya-language source | no | church side only: `juarros_compendio-historia-ciudad-de-guatemala-t2-spa_1809.txt`; `garcia-pelaez_memorias-historia-reyno-de-guatemala-t2-spa_1852.txt` | B2: not found (no Cruzob or Cancuc text before 1931) |
| OG176 LA8-5 | Priests in the wars of independence (Hidalgo, Morelos; 1810-1815) | "Hernandez y Davalos, Coleccion de documentos (1877-82), and Morelos's Sentimientos de la Nacion (1813), not found on archive.org" | no | none | OG176: not found on archive.org |
| OG176 LA8-6 | Haiti before 1804 | "the Code Noir (1685)" | no | `moreau-de-saint-mery_description-partie-francaise-saint-domingue-t1-fra_1797.txt`, `-t2-` (B2: filled) | Code Noir: the B2 row does not say it was found; unclear |

### (6) Catholic Europe: old regime, Jansenism, Jesuits, orders

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A146 | L. A. Muratori; Society of Jesus (Paraguay), old regime (VII.19, VII.44) | "Gian Francesco Soli Muratori, Vita del proposto Lodovico Antonio Muratori (Venice, 1756) [suggested; to confirm]; Il cristianesimo felice (1743) is online at archive.org A118051 (the census link)" | no | `muratori_della-regolata-divozione-de-cristiani-ita_1748.txt`; Cristianesimo felice not held | not in B |
| A147 | Armand-Jean de Rance; old regime | "A life of Rance by Pierre Marsollier (1703) [suggested; to confirm], or Rance's letters [suggested; to confirm]" | no | `rance_de-la-saintete-et-des-devoirs-de-la-vie-monastique-t1-fra_1683.txt`, `-t2-` (host attribution only, unconfirmed) | B4: Rance's treatise filled; Reglements of 1718 not found. A Life not searched |
| A148 | Nicolas Fontaine and Pierre Thomas du Fosse (pair); Port-Royal (VII.9) | "Nicolas Fontaine, Memoires pour servir a l'histoire de Port-Royal (Cologne, 1738) [suggested; to confirm]; Memoires de Pierre Thomas, sieur du Fosse (Utrecht, 1739) [suggested; to confirm]" | no | none (held: `port-royal_divers-actes-lettres-relations-fra_1724.txt`) | not in B |
| OG225 | Pasquier Quesnel (LISTED until vendored) | "the Reflexions morales (1692-94)" | no | none | not in B |
| OG181 RV-1 | Society of Jesus 1650-1814 (VII.44): expulsions, Paraguay | "Dobrizhoffer, Historia de Abiponibus (1784)"; "the Pragmatic Sanction of Charles III (1767)" | no | `clement-xiv_bulls-suppression-and-restoration-of-the-jesuits-lat-eng_1814.txt`; `murillo-velarde_historia-provincia-philipinas-compania-jesus-spa_1749.txt`; none of the two named | not in B |
| OG181 RV-1 | Jesuits in Russia 1773-1800 | "a Polotsk source" | no | none | not in B |
| OG181 RV-1 | Jesuit voice from Paraguay or Russia | "a modern history of the Society's suppression and a Jesuit letter or house history from Paraguay or Russia"; "a Guarani-language or Guarani-written source for the reductions after 1743" | no | none | not in B |
| OG181 RV-3 | Catholics of the Ottoman Balkans (VII.35): Albania, Bulgaria | "the Albanian council of 1703 (Concilium Albanum) and a source on the Bulgarian Catholics before 1815" | no | none | not in B |
| OG181 RV-3 + OG180 ME-10 | Bosnian Franciscans (VII.35); Polish-Lithuanian Commonwealth church 1650-1772 | "a Bosnian Franciscan chronicle in Croatian (Fojnica or Sutjeska)"; "a Polish or Lithuanian source ... and Theiner vol. 4 for the Commonwealth church" | no | `fermendzin_acta-bosnae-potissimum-ecclesiastica-lat_fermendzin1892.txt`; `theiner_vetera-monumenta-poloniae-lithuaniae-v3-lat_1863.txt`, `-v4-lat_1864.txt` (v4 held, not read) | not in B |

### (7) German-speaking Protestants: Pietism, Moravians, Brethren, Mennonite / Amish, Schwenkfelder

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A143 | Johanna Eleonora Petersen; German Pietism (VII.2) | "Lebens-Beschreibung der Frauen Johanna Eleonora Petersen (1718), the census's own source; Becker-Cantarino's English (Chicago 2005) is the modern edition [suggested; to confirm the early German print]" | no | none of hers; her husband's: `petersen-jw_leben-deu_1717.txt` | not in B |
| A144 | Gottfried Arnold; Radical Pietism and the Brethren (VII.3) | "Unparteiische Kirchen- und Ketzer-Historie (1699-1700), the census's own source; the Frankfurt edition of 1729 [suggested; to confirm]" | no | none | not in B |
| A145 | Rebecca Protten; Moravians (VII.4) | "Her letters and Lebenslauf from the Unity Archives (Herrnhut), as printed in a published edition [suggested; to confirm]. Sensbach, Rebecca's Revival (Harvard 2005) is a modern secondary book" | no | none (held Moravian: `oldendorp_geschichte-der-mission-caraibische-inseln-v1-deu_bossart1777.txt`, `moravian-church_periodical-accounts-missions-v1_1790.txt`, `cranz_*`, `loskiel_*`) | not in B |
| A142 | Jakob Ammann; Mennonites and Amish (VII.32) | "Ammann's letters of 1693 and the Amish division sources, in Die Taufer in der Schweiz (Akten) [suggested; to confirm]" | no | none (nearest: `taeuferakten-wuerttemberg_quellen-geschichte-wiedertaeufer-1-deu_bossert1930.txt`, Wurttemberg, not Swiss; `van-braght_martyrs-mirror_sohm1886`) | not in B |
| OG182 RV-5 | Moravian Church other fields (Greenland, Nicaragua, Ladakh, Alaska, Australia, Cape) | "J. Taylor Hamilton (1901) as a vendoring candidate" (A History of the Missions of the Moravian Church during the Eighteenth and Nineteenth Centuries, Bethlehem, Pa., 1901) | no | none (Cranz, La Trobe 1771 held) | not in B |
| B6 | Schwenkfelders after 1650 | `lehre-und-ordnungs-regeln` (sacrament rules); "the 1762 hymnal itself" | no | `kriebel_genealogical-record-of-the-schwenkfelders_1879.txt`; `seipt_schwenkfelder-hymnology_1909.txt` | B6: Lehre held back (CC BY-NC-ND licence unclear), a call for Mark; hymnal not found |
| B6 | Hutterites after 1785 | an insider print before 1931 | no | `wolkan_die-hutterer-deu_1918.txt` (outsider); `hutterite-brethren_geschicht-buch-deu_wolkan1923.txt` | B6: outsider only |

### (8) Nordic

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A160 | Hans Nielsen Hauge; Haugean awakening | "Hauge's own Skrifter and the Testament; a life such as Bang, Hans Nielsen Hauge og hans Samtid (1874) [suggested; to confirm]" | no | none | not in B. Era 9 shelf per E |
| B6 | Nordic state churches after 1650 | "the Church Law of 1686, Pontoppidan's Sandhed, Kingo, Brorson" | no | `cornelius_svenska-kyrkans-historia-efter-reformationen-swe_1886.txt`; `helweg_den-danske-kirkes-historie-efter-reformationen-v1-dan_1851.txt`, `-v2-` | B6: not found |

### (9) British Isles: Church of England, Dissent, Baptists, Scotland, Wales, Ireland

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A121 | Robert Hindmarsh; Swedenborgian New Church (VII.13) | "Hindmarsh, Rise and Progress of the New Jerusalem Church (pub. 1861) (named in census sources)" | yes | `hindmarsh_letters-to-dr-priestley_1792.txt`; `new-jerusalem-church_minutes-of-the-first-general-conference_hindmarsh1789.txt` | not in B |
| A129 | Ann Griffiths; Welsh revival (VII.10) | "The 1806 Welsh memoir of Ann Griffiths and her letters, by John Hughes of Pontrobert [recollection; to confirm]" | no | `griffiths-ann_hymns-in-english-verse_pughe1900.txt` | not in B |
| A135 | Anne Dutton; Baptists (VII.16) | "Dutton, A Brief Account of the Gracious Dealings of God with a Poor, Sinful, Unworthy Creature (1743) [suggested; to confirm]" | no | `dutton-anne_letters-on-spiritual-subjects-v1_1740.txt` | not in B |
| A136 | Isaac Watts; English Old Dissent (VII.26) | "Thomas Gibbons, Memoirs of the Rev. Isaac Watts (1780) [suggested; to confirm]" | no | `watts_hymns-and-spiritual-songs-ninth-edition_1725.txt`, `watts_psalms-of-david-imitated_1719.txt` | not in B |
| A137 | Philip Doddridge; Old Dissent | "Job Orton, Memoirs of the Life, Character and Writings of Philip Doddridge (1766) [suggested; to confirm]" | no | `doddridge_rise-and-progress-of-religion-in-the-soul_1745.txt` | not in B |
| A139 | Hannah More; Georgian C of E, evangelical wing (VII.20) | "William Roberts, Memoirs of the Life and Correspondence of Mrs. Hannah More (1834) [suggested; to confirm]" | no | tracts only (Cheap Repository, per E file key); no Life | not in B |
| A140 | Thomas Bray; Georgian C of E | "Samuel Smith, The Life of the Rev. Thomas Bray (1746) [suggested; to confirm]" | no | none | not in B |
| A141 | William Wilberforce; Georgian C of E (also era 9) | "R. I. and S. Wilberforce, The Life of William Wilberforce (1838) [suggested; to confirm]" | no | `wilberforce_practical-view-of-the-prevailing-religious-system_dublin1797.txt` | not in B |
| A159 | Robert Raikes and Thomas Stock (pair); Sunday School movement | "Gregory, Robert Raikes: Journalist and Philanthropist (1877); Raikes's letters in the Gentleman's Magazine 1784 [suggested; to confirm]" | no | none | not in B |
| B6 | English and Welsh Catholics after 1650 | Kirk's Biographies | no | `milner_end-of-religious-controversy-part2_1818.txt`; `dodd_church-history-of-england-v4_tierney1841.txt`, `-v5_`; `challoner_memoirs-of-missionary-priests_pollen1924.txt` | B6: not found |

### (10) Methodists

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A133 | Sarah Crosby; Methodist Revival (VII.5) | "Zechariah Taft, Biographical Sketches of the Lives and Public Ministry of Various Holy Women (1825-1828) [suggested; to confirm]" | no | none (about 16 Wesley files, Asbury, Coke, Mary Fletcher, Hester Ann Rogers held) | not in B |

### (11) North America

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| A128 | Samson Occom; New England Awakening (VII.6) | "Samson Occom, A Short Narrative of My Life (1768), as printed in W. DeLoss Love, Samson Occom and the Christian Indians of New England (1899) [suggested; to confirm]" | yes | `occom_sermon-at-the-execution-of-moses-paul_1788.txt` | not in B |
| A130 | James Davenport | "James Davenport, The Reverend Mr. James Davenport's Confession and Retractions (Boston, 1744) [suggested; to confirm]" | no | none | not in B |
| A131 | Nathan Cole | "Nathan Cole, Spiritual Travels, as printed in M. J. Crawford, 'The Spiritual Travels of Nathan Cole,' William and Mary Quarterly 33 (1976) [recollection; to confirm]" | no | none (1976 article is likely in copyright; unclear) | not in B |
| A132 | Lemuel Haynes (straddles eras 8-9) | "Timothy Mather Cooley, Sketches of the Life and Character of the Rev. Lemuel Haynes (New York, 1837) [suggested; to confirm]" | no | none | not in B |
| A134 | Samuel Davies; Hanover, Virginia strand | "The first volume of the same edition (Sermons on Important Subjects, 1792) with the funeral sermon and life [recollection; to confirm]" | no | `davies_sermons-on-important-subjects-v3_allen1792.txt` (v3 only) | not in B |
| A138 | Judith Sargent Murray; Early American Unitarians and Universalists (VII.27) | "Judith Sargent Murray, The Gleaner (1798) [suggested; to confirm]; her letter books [suggested; to confirm]" | no | none (`murray-john_*` files are her husband's) | not in B |
| A157 | James McGready; Kentucky revival (era 9 shelf) | "McGready, A Short Narrative of the Revival of Religion in Logan County (1801), or his Posthumous Works (1831-32) [suggested; to confirm]" | no | none (`mcnemar_kentucky-revival-with-the-entrance-of-shakerism_1808.txt`, `asbury_journal-v3_1821.txt`) | not in B |
| A158 | Thomas Campbell; Stone-Campbell | "Campbell, Declaration and Address (1809), and Richardson, Memoirs of Alexander Campbell (1868), vol. 1, which carries Thomas's life [suggested; to confirm]" | no | none | not in B. Era 9 shelf per E |
| OG225 (A226 era 9) | Herman of Alaska; Alaskan mission | "The Valaam mission records and a Life: Little Russian Philokalia vol. 3, Saint Herman: Wonderworker of Alaska (Platina, 1971) [suggested; to confirm]; Hieromonk Gideon, journal of his 1804-07 voyage to Russian America [suggested; ...]" (rest of line cut in the source) | no | none | not in B. A226 gives "Herman's Spruce Island record (census sources note)"; 1971 book is modern |

### (12) Councils and synods of era 8

**Formal wants: none.** A's council table has no row dated 1650-1815 (46 rows, 377-2010). Councils_Scan (era 8, 9 rows): Great Moscow Synod 1666-67, Synod of Jerusalem 1672, Synod of Zamosc 1720, Second Synod of Utrecht 1763, General Baptist Assembly all HELD; Mount Lebanon 1736 is counted in group 2. Partly held, with what is missing: Warsaw 1658, Manila 1771, Pistoia 1786. The rows below are **leads**, from the Councils_Scan and the Who scan (E-lead), not on any wanted list. Mark: the councils owner decides.

| lead | what is missing | held |
|---|---|---|
| Diet of Warsaw 1658 (charge against Polish Unitarians) | the proceedings | `lubieniecki_historia-reformationis-polonicae-lat_1685.txt` only (decree, lines about 14800-14830); not on the shelf by keyword |
| Provincial Council of Manila 1771 | the acts | Blair-Robertson v50 narrative only |
| Synod of Pistoia 1786 | the Atti | `pius-vi_auctorem-fidei-lat_1794.txt` (85 propositions) |
| Synods of Alba Iulia 1701 and 4 June 1728 | the acts | none (Nilles not in cic/texts) |
| Georgian synod 1755 (Antoni I) | the acts | none (Brosset notes only) |
| Synod of Constantinople 1776 (Kollyvades; Athanasios Parios deposed) | text | none identified |
| Synod of Tonkin 1670 (Lambert de la Motte) | text; Launay vol. 1 would carry it | none |
| Canton conference of missionaries 1667-1670 [recollection; to confirm] | text | none known |
| Fourth Mexican Provincial Council 1771 [recollection; to confirm] | text | none known |
| Council of Embrun 1727; French constitutional church councils 1797 and 1801; National Council of Paris 1811 | text | "no file checked" |
| Savoy Assembly 1658; Exeter Assembly 1718-19 | records | not held |
| Protestant Episcopal Convention, Philadelphia 1785-87 | records | not held |
| Winchester Convention (Universalist) 1803 | 1803 printing | later retelling only (`universalist-church_winchester-centennial-with-the-profession-of-belief_1903.txt`) |
| Hungarian diets 1681 (Sopron) and 1790-91; Peace of Szathmar 1711 | text | none (diets, not councils) |
| Council of Ethiopian clergy under David (stoning of Catholic priests) | Bruce | none (Bruce not held) |
| National Synod of Loudun (year not read; about 1659-60 [recollection; to confirm]) | text | named in `leger_histoire-generale-eglises-vaudoises-livre2-fra_1669.txt`; not shelved |

Held and complete or in part, so not leads: Moscow 1654 (Subbotin v1), Moravian synods 1740-1789 (Spangenberg, Cranz, Periodical Accounts), Pennsylvania synods 1742, Angamaly 1787 and Coonan Cross 1653 (Whitehouse), Melkite synods 1730, 1761 (Mansi 46), Pozega 1689 (Fermendzin), Mughan 1736 (Chamich, Zakaria), Christmas Conference 1784 (Coke, Minutes).

### (13) Other

| id | served | named source | major | held | earlier result / note |
|---|---|---|---|---|---|
| OG180 ME-9 | Hungarian and Transylvanian Protestantism 1650-1815 (VII.40): Debrecen, Sarospatak, Upper Hungary Lutherans, galley pastors | "a Hungarian-language source or the narrative of a galley pastor such as Balint Kocsi Csergo" | no | none (census read Bauhofer 1854 and the Catholic Encyclopedia article online; Unitarian files held belong to VII.50) | not in B |
| OG182 RV-8 | Czech lands after 1627; Toleration Patent 1781 (named line in VII.4) | no source named; "waits for a North Europe pass" | no | `lasicki_obraz-jednoty-ceskobratrske-ces_1869.txt`; `comenius_historia-fratrum-bohemorum-lat_1702.txt` (older Unity) | unclear what is wanted |
| OG225 | Outside witnesses 1650-1815 | "No Jewish, Muslim or Asian chronicler of 1650-1906 is held" (no author named) | no | outside witnesses held: Volney v2, Rycaut, Tournefort, Chardin, Ludolf | not in B |
| B-later (OG159) | families the tree does not reach, all eras | the Patriarchate of Alexandria, Cyprus, Polish, Czech-Slovak and Macedonian churches, Eastern Catholic churches never named | no | n/a | queued, not era-specific |

## 3. Census entries with NO want row and a thin shelf

Test: fewer than 2 held files by keyword, `ls cic/texts | grep -i`. Keyword counts are loose (noise like "kleine", "cape"); real subject counts given in brackets. Census has 51 era 8 entries (VII.1-VII.50 plus VII.24a), not the 34 D counted at data release 29; D lists no per-entry sources, so entry data below is from `cic-website/data/world-census.json`.

- **VII.43 Protestant Churches of the VOC World** (1650-1815; Ambon, Java, Jaffna): 0 held [0]. No row in A. Only OG178 (Valentijn, Leijdecker Bible, Ambon records). Census sourcing: "No Dutch or Malay text of the church itself was read."
- **VII.47 Catholics of Dutch Ceylon** (1658-1806): 1 by keyword [0 real]. Rows exist (A127, A156) but nothing held; census rests on an anonymous 1848 sketch read raw.
- **VII.49 Romanian Greek Catholic Church** (1698-1815): [0 real]. Row A150 exists; nothing held; Nilles is not vendored.
- **VII.45 Vietnamese Catholicism** (1650-1815): 1 by keyword [0 Vietnam-specific; Launay Guizhou volume is China]. Rows A125, A126 exist; nothing held.
- **VII.40 Hungarian and Transylvanian Protestantism** (1650-1815): [0 for the Reformed and Lutheran churches]. Only the OG180 ME-9 lead; the Unitarian files held serve VII.50.
- Borderline (1-2 real files): VII.41 Japan's Hidden Christians (2: Marnas t1, t2, French); VII.35 Balkan Catholics (1 Fermendzin, plus Theiner Slavorum meridionalium v1); VII.39 Georgian Church (2-3 Brosset); VII.23 Melkite (Charon t2-t3, Mansi 46, Paul of Aleppo).

## 4. The two Era 8 worlds (`records/worlds/`)

| code (file) | world_id | display name | window | state |
|---|---|---|---|---|
| `meth` (`records/worlds/meth.yaml`) | the-methodist-revival | The Methodist Revival | 1738-1815 | candidate |
| `obel` (`records/worlds/obel.yaml`) | the-old-believers | The Old Believers | 1666-1815 | candidate |

Other worlds in `records/worlds/` end at or before 1650 (`jes` 1540-1650, `rzg` 1519-1650, `witt` 1517-1580, `hus` 1402-1517; the rest earlier).

## 5. Era 8 Who scan by tradition (E)

Totals: 409 rows: WHO 137, STORY 51, LISTED 179, WANTED 42; 51 census entries (50 movements and John Wesley). WHO counts below are keyword tallies on the tradition column; rows naming two traditions count in both, so treat as approximate.

Quakers 6 | Methodist Revival 9 | Evangelical Awakening in New England 4 | Welsh Revival 4 | Shakers 5 | New Sweden 1 | Baptists 5 | English Old Dissent 7 | English Unitarianism 3 | Early American Unitarians and Universalists 4 | Swedenborgian New Church 2 | Restoration and Georgian C of E 2 (nonjuring and others; keyword "Georgian Church") | Mennonites and Amish 1 | German Pietism (Halle) 7 | Radical Pietism and the Brethren 6 | Moravian Church at Herrnhut 9 | Transylvanian Unitarian Church 1 | Church of Utrecht 5 | Church of the Desert 4 | Quietist controversy 4 | Port-Royal and Jansenism 5 | Camisard prophetism 3 | Catholic Church of the old regime 7 | Old Believers 5 | Russian Church (Nikon to Holy Synod) 4 | Hesychast revival 2 | Orthodoxy under the Ottomans 4 | Armenian (Apostolic and Catholic) 5 | Melkite Greek Catholic 2 | St Thomas Christians 3 | Ethiopian Christianity 1 | Kongo 1 | Colonial Latin American devotional Catholicism 5 | Philippine Catholicism 1 | Waldensians 1 | Polish Brethren 1 | Remonstrants 1 | The Black Church in America 1 | Maronite Church 1.

## 6. Census entries, era 8 (id | name | window | region | main named primary works | held-by-keyword)

From the census `sources` fields, entry level, type "primary" only. "sourcing prose only" means the entry has no work list; "-" means none captured.

| id | name | window | region | primary works named | held |
|---|---|---|---|---|---|
| VII.1 | Quakers | 1650s-1815 | England, Atlantic world | Fox Journal; Fell Women's Speaking Justified (1666), Works (1710); Woolman Journal; Besse Sufferings (1753); Evans and Cheevers (1662) | 16 |
| VII.2 | German Pietism | 1675-1750 | Germany | Spener Pia Desideria (1675); Francke Lebenslauf, Segensvolle Fusstapfen; J. E. Petersen Life (1718); Freylinghausen Gesangbuch (1704) | 16 |
| VII.3 | Radical Pietism, Brethren | 1690s-1815 | Germany, then Pennsylvania | Mack Rights and Ordinances (1713); Arnold Ketzer-Historie (1699-1700); Chronicon Ephratense; Turtel-Taube (1747) | 15 |
| VII.4 | Moravian Church at Herrnhut | 1722-1815 | Saxony, then global | Gemein-Diarium, Brotherly Agreement; Lebenslaeufe; Zinzendorf; mission diaries; La Trobe (1771); Periodical Accounts v1 (1790) | 21 |
| VII.5 | Methodist Revival | 1738-1815 | Britain, then America | Wesley Journal and Works; General Rules (1743), Minutes (1744-); Hymns (1780); Crosby, Fletcher, Rogers | 29 |
| VII.6 | Evangelical Awakening, New England | 1734-c. 1760 | New England | Edwards; Cole, Osborn, Wheatley, Haynes, Occom; Chauncy (1743); Davenport (1744) | 23 |
| VII.7 | Old Believers | 1666-1815 | Russian north, Siberia | Avvakum Life; Morozova letters; Solovki petitions; Vyg Pomorskie otvety (1723); 1666-67 council acts | 14 |
| VII.8 | Hesychast Revival | 1746-1815 | (Neamt, Athos) | Philokalia (1782); Paisius autobiography; Nicodemus works | 8 |
| VII.9 | Port-Royal Jansenism | 1640-1710 | France | nuns' records; Pascal; Jansen, Arnauld, Quesnel; Racine Abrege, Fontaine and du Fosse memoirs | 6 |
| VII.10 | Welsh Revival | 1735-1815 | Wales | Harris diaries; Pantycelyn; Ann Griffiths; seiadau records | 16 |
| VII.11 | Antonian Movement, Kongo | 1704-1706 | Kongo | da Gallo and da Lucca relations; Salve Antoniana; court correspondence | 6 |
| VII.12 | Shakers | 1774-1815 | England, then America | Testimonies of Mother Ann Lee (1816); Youngs (1808); Rathbun (1781) | 10 |
| VII.13 | Swedenborgian New Church | 1780s-1815 | England, America | Arcana Coelestia, Heaven and Hell, True Christian Religion; first General Conference minutes (1789); Hindmarsh | 14 |
| VII.14 | Quietists | 1675-1699 | Spain, France | Molinos (1675); Guyon; Fenelon Maximes (1697), Bossuet Relation, Cum alias (1699) | 14 |
| VII.15 | Camisards | 1700-1710 | Cevennes | Theatre sacre (1707); Cavalier Memoirs (1726); intendants' records | 12 |
| VII.16 | Baptists | 1609-1815 | England, then America | London Confessions; Bunyan; Broadmead records; Beaumont (1674); Liele (1791) | 12 |
| VII.17 | Colonial Latin American Devotional Catholicism | c. 1600-1810 | New Spain, Peru, Brazil | cofradia books; Sor Juana (1691); Ursula de Jesus; Vieira Maria Rosa Mystica (1686); Antonil (1711); Benedict XIV Immensa (1741); Moreau de Saint-Mery; Montalvo (1683); Garcia de la Concepcion (1723) | 12 |
| VII.18 | Orthodoxy under the Ottomans, second act | 1650-1821 | Anatolia, Balkans, Greek islands | sourcing prose: Jerusalem 1672 acta, Dositheus (verified); Kosmas Teachings, Christodoulides Life (1814) | 20 |
| VII.19 | Catholic Church of the Ancien Regime | 1650-1815 | Rome, Catholic Europe | sourcing prose only (Unigenitus, 1773 suppression, 1790 Civil Constitution) | 32 |
| VII.20 | Restoration and Georgian C of E | 1660-1815 | England, Wales, Ireland; colonies | sourcing prose only | 16 |
| VII.21 | Russian Church, Nikon to Holy Synod | 1652-1815 | Russia | sourcing prose (1666-67 council, Spiritual Regulation 1721) | 15 |
| VII.22 | Church of the Desert | 1685-1787 | Languedoc, Cevennes | sourcing prose only (Desert synods, Court, Rabaut) | 10 |
| VII.23 | Melkite Greek Catholic Split | 1650-1815 | Damascus, Aleppo, Mount Lebanon | Paul of Aleppo, Travels of Macarius, tr. Belfour (1836) | 5 |
| VII.24a | Armenian Apostolic Church | 1650-1815 | Etchmiadzin, Constantinople, Isfahan | sourcing prose only (a catholicos's story of 1736) | 8 |
| VII.24 | Armenian Mekhitarists and Catholic Patriarchate | c. 1700-1815 | Constantinople, Venice, Lebanon | sourcing prose only | 6 |
| VII.25 | Church of Utrecht | 1723-1815 | Netherlands | sourcing prose only | 5 |
| VII.26 | English Old Dissent | 1662-1815 | England, Wales | sourcing prose only (Watts, academies, Salters' Hall) | 10 |
| VII.27 | Early American Unitarians and Universalists | 1770-1815 | New England, London | sourcing prose only (Murray, Winchester 1803, Ballou) | 18 |
| VII.28 | Ruthenian Uniate Church | 1700-1815 | Ruthenia, Galicia | Nilles Symbolae (Innsbruck, 1885) | 8 |
| VII.29 | Philippine Catholicism, era 8 | 1650-1815 | Philippines | sourcing prose only (pasyon of 1704) | 22 |
| VII.30 | Swedish Lutherans of New Sweden | 1638-1786 | Delaware River | - | 5 |
| VII.31 | English Unitarianism | 1774-1813 | London, Birmingham, Hackney | - | 7 |
| VII.32 | Mennonites and the Amish | 1650-1890 | Netherlands, Pennsylvania, Indiana | Wiebe (1900); Beck Geschichts-Buecher (1883) | 7 |
| VII.33 | John Wesley | 1735-1791 | Britain, Georgia | - | 16 |
| VII.34 | Copts under the Ottomans | 1517-1854 | Egypt | Volney (1788); Lane (1860); Gobat (1834); Bruce v2 (1790) | 9 |
| VII.35 | Catholics of the Ottoman Balkans | 1650-1815 | Bosnia, Slavonia | Fermendzin Acta Bosnae (1892) | 6 |
| VII.36 | Chinese Catholics | 1650-1906 | China | Collectanea Propaganda v1 (1907); Lettres edifiantes | 10 |
| VII.37 | Church of the East, Three Patriarchates | 1650-1815 | Diyarbakir, Mosul, Hakkari | Badger Nestorians and their Rituals v1 (1852) | 10 |
| VII.38 | Ethiopia, Gondar to the Zemene Mesafint | 1650-1855 | Ethiopia, Eritrea | Ludolf (1682); Bruce v2, v3 (1790); Gobat (1834) | 17 |
| VII.39 | Georgian Church | 1650-1811 | Georgia | Ioselian, tr. Malan (1866) | 5 |
| VII.40 | Hungarian and Transylvanian Protestantism | 1650-1815 | Hungary, Transylvania | - (Bauhofer, Catholic Encyclopedia only) | 4 |
| VII.41 | Japan's Hidden Christians | 1650-1865 | Japan | - | 2 |
| VII.42 | Kongo Christianity after 1650 | 1650-1881 | Kingdom of Kongo | Carli (1671); Cavazzi (1687); Lopes and Pigafetta; Bentley (1900) | 9 |
| VII.43 | Protestant Churches of the VOC World | 1650-1815 | Ambon, Java, Jaffna | - | 0 |
| VII.44 | Society of Jesus, 1650-1814 | 1650-1814 | Rome, Paraguay, world | Bulls of Clement XIV and Pius VII (1814); Muratori (1743); Mirbt; Nilles v1; Lettres edifiantes | 50 |
| VII.45 | Vietnamese Catholicism to 1815 | 1650-1815 | Tonkin, Cochinchina | Collectanea v1 (1675 entry); Rhodes Cathechismus (1651) | 1 |
| VII.46 | Dutch Reformed Church at the Cape | 1652-1906 | South Africa | McCarter (1869) | 23 |
| VII.47 | Catholics of Dutch Ceylon | 1658-1806 | Jaffna, Puttalam, Kandy, Goa | - (the 1848 Sketch, anonymous) | 1 |
| VII.48 | St Thomas Christians, Two Obediences | 1665-1815 | Malabar Coast | Philipos, Syrian Christians of Malabar (1869); Buchanan (1811) | 9 |
| VII.49 | Romanian Greek Catholic Church | 1698-1815 | Transylvania, Blaj | Nilles (1886) | 1 |
| VII.50 | Transylvanian Unitarian Church | 1660-1906 | Transylvania, Hungary | Ferencz (1875); Short Account (1907) | 5 |

Held counts are the loose keyword counts from section 3 (VII.44 counts every Jesuit file; VII.46 counts "cape"/"philip" noise; VII.19 counts "pius"/"clement"); use section 3 for the real thin spots.

## 7. Could not read or check

- D lists no per-entry census sources (it holds 68 new candidate rows, not the existing entries); I used the census JSON instead. Its entry-level source lists for VII.19-22, 24-27, 29-33, 40, 41, 43, 47 are absent or prose only.
- Open-Gaps 225 lines for Herman of Alaska are cut off in the source ("[suggested; ..."), and a few B rows cite files by stem only; filenames above were checked with `ls`.
- I did not open any text in cic/texts to confirm contents; "held" means a filename match only.
- One scratch file was created during research: `.../scratchpad/era8.json` (an extract of the census, not used by the repo).
