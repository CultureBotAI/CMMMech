# Stage 4 full-cohort review: mineral records (365/365)

- Review: 20261022T025801Z-stage4-mineral-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-22T02:45:00Z
- Finished UTC: 2026-10-22T02:58:01Z
- Reviewer: antigravity / cmmmech-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 365 mineral records in data/records/*.yaml at commit 4d878383c92b44876df3bf166d96637c7581a59e. All 365 mineral records carry valid mineral descriptions and source provenance; 269/365 mineral records carry mechanisms (157/365 with microbial: true mechanisms) and 29/365 carry grounded multi-step causal_graphs with UniProtKB protein_examples. Recorded one cohort-level minor completeness finding (cmmmech-stage4-finding-0001) across 17 mineral records that state their IMA-CNMNC species number in description and cite ima_2026_09 but omit the structured IMA:YYYY-NNN entry from identifiers (and see companion single-record review 20261022T025807Z-wulfenite-stage4-record-review for cmmmech-stage4-finding-0002 on cmmmech:wulfenite).

## Scope And Provenance

Full-population Stage 4 category review of all 365 IMA-approved mineral species records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'mineral' at 4d878383c92b44876df3bf166d96637c7581a59e
Coverage: full; 365 reviewed / 365 in the declared population.
Source: git_commit at Git base 4d878383c92b44876df3bf166d96637c7581a59e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:acanthite | data/records/acanthite.yaml | maintained | Acanthite |
| cmmmech:adamsite-y | data/records/adamsite-y.yaml | maintained | Adamsite-(Y) |
| cmmmech:akaganeite | data/records/akaganeite.yaml | maintained | Akaganeite |
| cmmmech:alabandite | data/records/alabandite.yaml | maintained | Alabandite |
| cmmmech:albite | data/records/albite.yaml | maintained | Albite |
| cmmmech:alburnite | data/records/alburnite.yaml | maintained | Alburnite |
| cmmmech:alicewilsonite-yce | data/records/alicewilsonite-yce.yaml | maintained | Alicewilsonite-(YCe) |
| cmmmech:alicewilsonite-yla | data/records/alicewilsonite-yla.yaml | maintained | Alicewilsonite-(YLa) |
| cmmmech:alunite | data/records/alunite.yaml | maintained | Alunite |
| cmmmech:amblygonite | data/records/amblygonite.yaml | maintained | Amblygonite |
| cmmmech:ameghinite | data/records/ameghinite.yaml | maintained | Ameghinite |
| cmmmech:ammonioborite | data/records/ammonioborite.yaml | maintained | Ammonioborite |
| cmmmech:ammoniojarosite | data/records/ammoniojarosite.yaml | maintained | Ammoniojarosite |
| cmmmech:anatase | data/records/anatase.yaml | maintained | Anatase |
| cmmmech:ancylite-ce | data/records/ancylite-ce.yaml | maintained | Ancylite-(Ce) |
| cmmmech:andersonite | data/records/andersonite.yaml | maintained | Andersonite |
| cmmmech:anglesite | data/records/anglesite.yaml | maintained | Anglesite |
| cmmmech:anhydrite | data/records/anhydrite.yaml | maintained | Anhydrite |
| cmmmech:anilite | data/records/anilite.yaml | maintained | Anilite |
| cmmmech:annabergite | data/records/annabergite.yaml | maintained | Annabergite |
| cmmmech:anorthite | data/records/anorthite.yaml | maintained | Anorthite |
| cmmmech:aragonite | data/records/aragonite.yaml | maintained | Aragonite |
| cmmmech:argentojarosite | data/records/argentojarosite.yaml | maintained | Argentojarosite |
| cmmmech:argyrodite | data/records/argyrodite.yaml | maintained | Argyrodite |
| cmmmech:aristarainite | data/records/aristarainite.yaml | maintained | Aristarainite |
| cmmmech:arsenopyrite | data/records/arsenopyrite.yaml | maintained | Arsenopyrite |
| cmmmech:artinite | data/records/artinite.yaml | maintained | Artinite |
| cmmmech:asbolane | data/records/asbolane.yaml | maintained | Asbolane |
| cmmmech:atacamite | data/records/atacamite.yaml | maintained | Atacamite |
| cmmmech:autunite | data/records/autunite.yaml | maintained | Autunite |
| cmmmech:azurite | data/records/azurite.yaml | maintained | Azurite |
| cmmmech:baddeleyite | data/records/baddeleyite.yaml | maintained | Baddeleyite |
| cmmmech:bainbridgeite-ndce | data/records/bainbridgeite-ndce.yaml | maintained | Bainbridgeite-(NdCe) |
| cmmmech:bainbridgeite-yce | data/records/bainbridgeite-yce.yaml | maintained | Bainbridgeite-(YCe) |
| cmmmech:baricite | data/records/baricite.yaml | maintained | Barićite |
| cmmmech:bassanite | data/records/bassanite.yaml | maintained | Bassanite |
| cmmmech:becquerelite | data/records/becquerelite.yaml | maintained | Becquerelite |
| cmmmech:beudantite | data/records/beudantite.yaml | maintained | Beudantite |
| cmmmech:billietite | data/records/billietite.yaml | maintained | Billietite |
| cmmmech:birnessite | data/records/birnessite.yaml | maintained | Birnessite |
| cmmmech:bismuthinite | data/records/bismuthinite.yaml | maintained | Bismuthinite |
| cmmmech:bixbyite-mn | data/records/bixbyite-mn.yaml | maintained | Bixbyite-(Mn) |
| cmmmech:bobierrite | data/records/bobierrite.yaml | maintained | Bobierrite |
| cmmmech:boehmite | data/records/boehmite.yaml | maintained | Böhmite |
| cmmmech:boltwoodite | data/records/boltwoodite.yaml | maintained | Boltwoodite |
| cmmmech:boracite | data/records/boracite.yaml | maintained | Boracite |
| cmmmech:borax | data/records/borax.yaml | maintained | Borax |
| cmmmech:bornite | data/records/bornite.yaml | maintained | Bornite |
| cmmmech:briartite | data/records/briartite.yaml | maintained | Briartite |
| cmmmech:brochantite | data/records/brochantite.yaml | maintained | Brochantite |
| cmmmech:brookite | data/records/brookite.yaml | maintained | Brookite |
| cmmmech:brucite | data/records/brucite.yaml | maintained | Brucite |
| cmmmech:brushite | data/records/brushite.yaml | maintained | Brushite |
| cmmmech:burbankite | data/records/burbankite.yaml | maintained | Burbankite |
| cmmmech:cadmoindite | data/records/cadmoindite.yaml | maintained | Cadmoindite |
| cmmmech:calcioancylite-la | data/records/calcioancylite-la.yaml | maintained | Calcioancylite-(La) |
| cmmmech:calcioburbankite | data/records/calcioburbankite.yaml | maintained | Calcioburbankite |
| cmmmech:calcioveatchite | data/records/calcioveatchite.yaml | maintained | Calcioveatchite |
| cmmmech:calcite | data/records/calcite.yaml | maintained | Calcite |
| cmmmech:carnotite | data/records/carnotite.yaml | maintained | Carnotite |
| cmmmech:carrollite | data/records/carrollite.yaml | maintained | Carrollite |
| cmmmech:cassiterite | data/records/cassiterite.yaml | maintained | Cassiterite |
| cmmmech:catapleiite | data/records/catapleiite.yaml | maintained | Catapleiite |
| cmmmech:cattiite | data/records/cattiite.yaml | maintained | Cattiite |
| cmmmech:cavansite | data/records/cavansite.yaml | maintained | Cavansite |
| cmmmech:caysichite-y | data/records/caysichite-y.yaml | maintained | Caysichite-(Y) |
| cmmmech:celestine | data/records/celestine.yaml | maintained | Celestine |
| cmmmech:cerianite-ce | data/records/cerianite-ce.yaml | maintained | Cerianite-(Ce) |
| cmmmech:cerussite | data/records/cerussite.yaml | maintained | Cerussite |
| cmmmech:chalcocite | data/records/chalcocite.yaml | maintained | Chalcocite |
| cmmmech:chalcopyrite | data/records/chalcopyrite.yaml | maintained | Chalcopyrite |
| cmmmech:chernikovite | data/records/chernikovite.yaml | maintained | Chernikovite |
| cmmmech:childrenite | data/records/childrenite.yaml | maintained | Childrenite |
| cmmmech:chlorapatite | data/records/chlorapatite.yaml | maintained | Chlorapatite |
| cmmmech:chromite | data/records/chromite.yaml | maintained | Chromite |
| cmmmech:chrysotile | data/records/chrysotile.yaml | maintained | Chrysotile |
| cmmmech:chukanovite | data/records/chukanovite.yaml | maintained | Chukanovite |
| cmmmech:churchite-y | data/records/churchite-y.yaml | maintained | Churchite-(Y) |
| cmmmech:cinnabar | data/records/cinnabar.yaml | maintained | Cinnabar |
| cmmmech:cobaltite | data/records/cobaltite.yaml | maintained | Cobaltite |
| cmmmech:coffinite | data/records/coffinite.yaml | maintained | Coffinite |
| cmmmech:colemanite | data/records/colemanite.yaml | maintained | Colemanite |
| cmmmech:compreignacite | data/records/compreignacite.yaml | maintained | Compreignacite |
| cmmmech:coquimbite | data/records/coquimbite.yaml | maintained | Coquimbite |
| cmmmech:cordylite-ce | data/records/cordylite-ce.yaml | maintained | Cordylite-(Ce) |
| cmmmech:corkite | data/records/corkite.yaml | maintained | Corkite |
| cmmmech:covellite | data/records/covellite.yaml | maintained | Covellite |
| cmmmech:crandallite | data/records/crandallite.yaml | maintained | Crandallite |
| cmmmech:cryptomelane | data/records/cryptomelane.yaml | maintained | Cryptomelane |
| cmmmech:cuprite | data/records/cuprite.yaml | maintained | Cuprite |
| cmmmech:cuprosklodowskite | data/records/cuprosklodowskite.yaml | maintained | Cuprosklodowskite |
| cmmmech:curite | data/records/curite.yaml | maintained | Curite |
| cmmmech:digenite | data/records/digenite.yaml | maintained | Digenite |
| cmmmech:diopside | data/records/diopside.yaml | maintained | Diopside |
| cmmmech:dittmarite | data/records/dittmarite.yaml | maintained | Dittmarite |
| cmmmech:djurleite | data/records/djurleite.yaml | maintained | Djurleite |
| cmmmech:dolomite | data/records/dolomite.yaml | maintained | Dolomite |
| cmmmech:donnayite-y | data/records/donnayite-y.yaml | maintained | Donnayite-(Y) |
| cmmmech:dypingite | data/records/dypingite.yaml | maintained | Dypingite |
| cmmmech:dzhalindite | data/records/dzhalindite.yaml | maintained | Dzhalindite |
| cmmmech:elpidite | data/records/elpidite.yaml | maintained | Elpidite |
| cmmmech:enstatite | data/records/enstatite.yaml | maintained | Enstatite |
| cmmmech:eosphorite | data/records/eosphorite.yaml | maintained | Eosphorite |
| cmmmech:erythrite | data/records/erythrite.yaml | maintained | Erythrite |
| cmmmech:ezcurrite | data/records/ezcurrite.yaml | maintained | Ezcurrite |
| cmmmech:falottaite | data/records/falottaite.yaml | maintained | Falottaite |
| cmmmech:feitknechtite | data/records/feitknechtite.yaml | maintained | Feitknechtite |
| cmmmech:felsobanyaite | data/records/felsobanyaite.yaml | maintained | Felsőbányaite |
| cmmmech:feroxyhyte | data/records/feroxyhyte.yaml | maintained | Feroxyhyte |
| cmmmech:ferricopiapite | data/records/ferricopiapite.yaml | maintained | Ferricopiapite |
| cmmmech:ferrihydrite | data/records/ferrihydrite.yaml | maintained | Ferrihydrite |
| cmmmech:ferrokesterite | data/records/ferrokesterite.yaml | maintained | Ferrokësterite |
| cmmmech:florencite-ce | data/records/florencite-ce.yaml | maintained | Florencite-(Ce) |
| cmmmech:florencite-la | data/records/florencite-la.yaml | maintained | Florencite-(La) |
| cmmmech:fluorapatite | data/records/fluorapatite.yaml | maintained | Fluorapatite |
| cmmmech:fluorite | data/records/fluorite.yaml | maintained | Fluorite |
| cmmmech:forsterite | data/records/forsterite.yaml | maintained | Forsterite |
| cmmmech:fritzscheite | data/records/fritzscheite.yaml | maintained | Fritzscheite |
| cmmmech:galena | data/records/galena.yaml | maintained | Galena |
| cmmmech:germanite | data/records/germanite.yaml | maintained | Germanite |
| cmmmech:gersdorffite | data/records/gersdorffite.yaml | maintained | Gersdorffite |
| cmmmech:gibbsite | data/records/gibbsite.yaml | maintained | Gibbsite |
| cmmmech:ginorite | data/records/ginorite.yaml | maintained | Ginorite |
| cmmmech:glushinskite | data/records/glushinskite.yaml | maintained | Glushinskite |
| cmmmech:goethite | data/records/goethite.yaml | maintained | Goethite |
| cmmmech:goldmanite | data/records/goldmanite.yaml | maintained | Goldmanite |
| cmmmech:gorceixite | data/records/gorceixite.yaml | maintained | Gorceixite |
| cmmmech:gowerite | data/records/gowerite.yaml | maintained | Gowerite |
| cmmmech:goyazite | data/records/goyazite.yaml | maintained | Goyazite |
| cmmmech:greenockite | data/records/greenockite.yaml | maintained | Greenockite |
| cmmmech:greigite | data/records/greigite.yaml | maintained | Greigite |
| cmmmech:gypsum | data/records/gypsum.yaml | maintained | Gypsum |
| cmmmech:gysinite-nd | data/records/gysinite-nd.yaml | maintained | Gysinite-(Nd) |
| cmmmech:hafnon | data/records/hafnon.yaml | maintained | Hafnon |
| cmmmech:hannayite | data/records/hannayite.yaml | maintained | Hannayite |
| cmmmech:haradaite | data/records/haradaite.yaml | maintained | Haradaite |
| cmmmech:hauerite | data/records/hauerite.yaml | maintained | Hauerite |
| cmmmech:hausmannite | data/records/hausmannite.yaml | maintained | Hausmannite |
| cmmmech:hawleyite | data/records/hawleyite.yaml | maintained | Hawleyite |
| cmmmech:hazenite | data/records/hazenite.yaml | maintained | Hazenite |
| cmmmech:heazlewoodite | data/records/heazlewoodite.yaml | maintained | Heazlewoodite |
| cmmmech:hematite | data/records/hematite.yaml | maintained | Hematite |
| cmmmech:hemimorphite | data/records/hemimorphite.yaml | maintained | Hemimorphite |
| cmmmech:heterogenite | data/records/heterogenite.yaml | maintained | Heterogenite |
| cmmmech:heterosite | data/records/heterosite.yaml | maintained | Heterosite |
| cmmmech:hollandite | data/records/hollandite.yaml | maintained | Hollandite |
| cmmmech:hopeite | data/records/hopeite.yaml | maintained | Hopeite |
| cmmmech:humboldtine | data/records/humboldtine.yaml | maintained | Humboldtine |
| cmmmech:huntite | data/records/huntite.yaml | maintained | Huntite |
| cmmmech:hureaulite | data/records/hureaulite.yaml | maintained | Hureaulite |
| cmmmech:hydroboracite | data/records/hydroboracite.yaml | maintained | Hydroboracite |
| cmmmech:hydrocerussite | data/records/hydrocerussite.yaml | maintained | Hydrocerussite |
| cmmmech:hydromagnesite | data/records/hydromagnesite.yaml | maintained | Hydromagnesite |
| cmmmech:hydroniumjarosite | data/records/hydroniumjarosite.yaml | maintained | Hydroniumjarosite |
| cmmmech:hydrotalcite | data/records/hydrotalcite.yaml | maintained | Hydrotalcite |
| cmmmech:hydroxylapatite | data/records/hydroxylapatite.yaml | maintained | Hydroxylapatite |
| cmmmech:hydrozincite | data/records/hydrozincite.yaml | maintained | Hydrozincite |
| cmmmech:ilmenite | data/records/ilmenite.yaml | maintained | Ilmenite |
| cmmmech:inderborite | data/records/inderborite.yaml | maintained | Inderborite |
| cmmmech:inderite | data/records/inderite.yaml | maintained | Inderite |
| cmmmech:indite | data/records/indite.yaml | maintained | Indite |
| cmmmech:inyoite | data/records/inyoite.yaml | maintained | Inyoite |
| cmmmech:jadarite | data/records/jadarite.yaml | maintained | Jadarite |
| cmmmech:jarosite | data/records/jarosite.yaml | maintained | Jarosite |
| cmmmech:kaliborite | data/records/kaliborite.yaml | maintained | Kaliborite |
| cmmmech:kaolinite | data/records/kaolinite.yaml | maintained | Kaolinite |
| cmmmech:katsarosite | data/records/katsarosite.yaml | maintained | Katsarosite |
| cmmmech:kernite | data/records/kernite.yaml | maintained | Kernite |
| cmmmech:kesterite | data/records/kesterite.yaml | maintained | Kësterite |
| cmmmech:kornelite | data/records/kornelite.yaml | maintained | Kornelite |
| cmmmech:kozoite-la | data/records/kozoite-la.yaml | maintained | Kozoite-(La) |
| cmmmech:kozoite-nd | data/records/kozoite-nd.yaml | maintained | Kozoite-(Nd) |
| cmmmech:kukharenkoite-ce | data/records/kukharenkoite-ce.yaml | maintained | Kukharenkoite-(Ce) |
| cmmmech:kuliokite-y | data/records/kuliokite-y.yaml | maintained | Kuliokite-(Y) |
| cmmmech:kurnakovite | data/records/kurnakovite.yaml | maintained | Kurnakovite |
| cmmmech:kutnohorite | data/records/kutnohorite.yaml | maintained | Kutnohorite |
| cmmmech:laforetite | data/records/laforetite.yaml | maintained | Laforêtite |
| cmmmech:lansfordite | data/records/lansfordite.yaml | maintained | Lansfordite |
| cmmmech:lanthanite-ce | data/records/lanthanite-ce.yaml | maintained | Lanthanite-(Ce) |
| cmmmech:lanthanite-la | data/records/lanthanite-la.yaml | maintained | Lanthanite-(La) |
| cmmmech:lanthanite-nd | data/records/lanthanite-nd.yaml | maintained | Lanthanite-(Nd) |
| cmmmech:larderellite | data/records/larderellite.yaml | maintained | Larderellite |
| cmmmech:laueite | data/records/laueite.yaml | maintained | Laueite |
| cmmmech:lepidocrocite | data/records/lepidocrocite.yaml | maintained | Lepidocrocite |
| cmmmech:libethenite | data/records/libethenite.yaml | maintained | Libethenite |
| cmmmech:lindbergite | data/records/lindbergite.yaml | maintained | Lindbergite |
| cmmmech:lithiophilite | data/records/lithiophilite.yaml | maintained | Lithiophilite |
| cmmmech:lizardite | data/records/lizardite.yaml | maintained | Lizardite |
| cmmmech:loellingite | data/records/loellingite.yaml | maintained | Löllingite |
| cmmmech:lorenzenite | data/records/lorenzenite.yaml | maintained | Lorenzenite |
| cmmmech:ludlamite | data/records/ludlamite.yaml | maintained | Ludlamite |
| cmmmech:mackinawite | data/records/mackinawite.yaml | maintained | Mackinawite |
| cmmmech:maghemite | data/records/maghemite.yaml | maintained | Maghemite |
| cmmmech:magnetite | data/records/magnetite.yaml | maintained | Magnetite |
| cmmmech:malachite | data/records/malachite.yaml | maintained | Malachite |
| cmmmech:manganite | data/records/manganite.yaml | maintained | Manganite |
| cmmmech:marcasite | data/records/marcasite.yaml | maintained | Marcasite |
| cmmmech:mcallisterite | data/records/mcallisterite.yaml | maintained | Mcallisterite |
| cmmmech:mckelveyite-y | data/records/mckelveyite-y.yaml | maintained | Mckelveyite-(Y) |
| cmmmech:melanterite | data/records/melanterite.yaml | maintained | Melanterite |
| cmmmech:meta-ankoleite | data/records/meta-ankoleite.yaml | maintained | Meta-ankoleite |
| cmmmech:metacinnabar | data/records/metacinnabar.yaml | maintained | Metacinnabar |
| cmmmech:metaschoepite | data/records/metaschoepite.yaml | maintained | Metaschoepite |
| cmmmech:metastudtite | data/records/metastudtite.yaml | maintained | Metastudtite |
| cmmmech:metatorbernite | data/records/metatorbernite.yaml | maintained | Metatorbernite |
| cmmmech:metatyuyamunite | data/records/metatyuyamunite.yaml | maintained | Metatyuyamunite |
| cmmmech:metavivianite | data/records/metavivianite.yaml | maintained | Metavivianite |
| cmmmech:metazeunerite | data/records/metazeunerite.yaml | maintained | Metazeunerite |
| cmmmech:meyerhofferite | data/records/meyerhofferite.yaml | maintained | Meyerhofferite |
| cmmmech:microcline | data/records/microcline.yaml | maintained | Microcline |
| cmmmech:millerite | data/records/millerite.yaml | maintained | Millerite |
| cmmmech:mimetite | data/records/mimetite.yaml | maintained | Mimetite |
| cmmmech:molybdenite | data/records/molybdenite.yaml | maintained | Molybdenite |
| cmmmech:monazite-ce | data/records/monazite-ce.yaml | maintained | Monazite-(Ce) |
| cmmmech:monazite-gd | data/records/monazite-gd.yaml | maintained | Monazite-(Gd) |
| cmmmech:monazite-la | data/records/monazite-la.yaml | maintained | Monazite-(La) |
| cmmmech:monazite-nd | data/records/monazite-nd.yaml | maintained | Monazite-(Nd) |
| cmmmech:monazite-sm | data/records/monazite-sm.yaml | maintained | Monazite-(Sm) |
| cmmmech:monetite | data/records/monetite.yaml | maintained | Monetite |
| cmmmech:monohydrocalcite | data/records/monohydrocalcite.yaml | maintained | Monohydrocalcite |
| cmmmech:montebrasite | data/records/montebrasite.yaml | maintained | Montebrasite |
| cmmmech:montmorillonite | data/records/montmorillonite.yaml | maintained | Montmorillonite |
| cmmmech:montroseite | data/records/montroseite.yaml | maintained | Montroseite |
| cmmmech:moolooite | data/records/moolooite.yaml | maintained | Moolooite |
| cmmmech:muscovite | data/records/muscovite.yaml | maintained | Muscovite |
| cmmmech:natroboltwoodite | data/records/natroboltwoodite.yaml | maintained | Natroboltwoodite |
| cmmmech:natrojarosite | data/records/natrojarosite.yaml | maintained | Natrojarosite |
| cmmmech:navajoite | data/records/navajoite.yaml | maintained | Navajoite |
| cmmmech:nepheline | data/records/nepheline.yaml | maintained | Nepheline |
| cmmmech:nesquehonite | data/records/nesquehonite.yaml | maintained | Nesquehonite |
| cmmmech:newberyite | data/records/newberyite.yaml | maintained | Newberyite |
| cmmmech:ningyoite | data/records/ningyoite.yaml | maintained | Ningyoite |
| cmmmech:nobleite | data/records/nobleite.yaml | maintained | Nobleite |
| cmmmech:nontronite | data/records/nontronite.yaml | maintained | Nontronite |
| cmmmech:orpiment | data/records/orpiment.yaml | maintained | Orpiment |
| cmmmech:orthoclase | data/records/orthoclase.yaml | maintained | Orthoclase |
| cmmmech:otavite | data/records/otavite.yaml | maintained | Otavite |
| cmmmech:palygorskite | data/records/palygorskite.yaml | maintained | Palygorskite |
| cmmmech:paracoquimbite | data/records/paracoquimbite.yaml | maintained | Paracoquimbite |
| cmmmech:paramontroseite | data/records/paramontroseite.yaml | maintained | Paramontroseite |
| cmmmech:parasymplesite | data/records/parasymplesite.yaml | maintained | Parasymplesite |
| cmmmech:parauranophane | data/records/parauranophane.yaml | maintained | Parauranophane |
| cmmmech:pascoite | data/records/pascoite.yaml | maintained | Pascoite |
| cmmmech:pentagonite | data/records/pentagonite.yaml | maintained | Pentagonite |
| cmmmech:pentlandite | data/records/pentlandite.yaml | maintained | Pentlandite |
| cmmmech:perovskite | data/records/perovskite.yaml | maintained | Perovskite |
| cmmmech:pertlikite | data/records/pertlikite.yaml | maintained | Pertlikite |
| cmmmech:petalite | data/records/petalite.yaml | maintained | Petalite |
| cmmmech:petrukite | data/records/petrukite.yaml | maintained | Petrukite |
| cmmmech:phlogopite | data/records/phlogopite.yaml | maintained | Phlogopite |
| cmmmech:phosphoferrite | data/records/phosphoferrite.yaml | maintained | Phosphoferrite |
| cmmmech:phosphophyllite | data/records/phosphophyllite.yaml | maintained | Phosphophyllite |
| cmmmech:piilonenite-nd | data/records/piilonenite-nd.yaml | maintained | Piilonenite-(Nd) |
| cmmmech:pinnoite | data/records/pinnoite.yaml | maintained | Pinnoite |
| cmmmech:plumbojarosite | data/records/plumbojarosite.yaml | maintained | Plumbojarosite |
| cmmmech:polydymite | data/records/polydymite.yaml | maintained | Polydymite |
| cmmmech:polylithionite | data/records/polylithionite.yaml | maintained | Polylithionite |
| cmmmech:powellite | data/records/powellite.yaml | maintained | Powellite |
| cmmmech:preobrazhenskite | data/records/preobrazhenskite.yaml | maintained | Preobrazhenskite |
| cmmmech:priceite | data/records/priceite.yaml | maintained | Priceite |
| cmmmech:probertite | data/records/probertite.yaml | maintained | Probertite |
| cmmmech:pyrite | data/records/pyrite.yaml | maintained | Pyrite |
| cmmmech:pyroaurite | data/records/pyroaurite.yaml | maintained | Pyroaurite |
| cmmmech:pyrochroite | data/records/pyrochroite.yaml | maintained | Pyrochroite |
| cmmmech:pyrolusite | data/records/pyrolusite.yaml | maintained | Pyrolusite |
| cmmmech:pyromorphite | data/records/pyromorphite.yaml | maintained | Pyromorphite |
| cmmmech:pyrrhotite | data/records/pyrrhotite.yaml | maintained | Pyrrhotite |
| cmmmech:quenstedtite | data/records/quenstedtite.yaml | maintained | Quenstedtite |
| cmmmech:ramsdellite | data/records/ramsdellite.yaml | maintained | Ramsdellite |
| cmmmech:realgar | data/records/realgar.yaml | maintained | Realgar |
| cmmmech:regerite | data/records/regerite.yaml | maintained | Regerite |
| cmmmech:renierite | data/records/renierite.yaml | maintained | Renierite |
| cmmmech:rhabdophane-ce | data/records/rhabdophane-ce.yaml | maintained | Rhabdophane-(Ce) |
| cmmmech:rhabdophane-la | data/records/rhabdophane-la.yaml | maintained | Rhabdophane-(La) |
| cmmmech:rhodochrosite | data/records/rhodochrosite.yaml | maintained | Rhodochrosite |
| cmmmech:rhomboclase | data/records/rhomboclase.yaml | maintained | Rhomboclase |
| cmmmech:richetite | data/records/richetite.yaml | maintained | Richetite |
| cmmmech:riebeckite | data/records/riebeckite.yaml | maintained | Riebeckite |
| cmmmech:rivadavite | data/records/rivadavite.yaml | maintained | Rivadavite |
| cmmmech:romanechite | data/records/romanechite.yaml | maintained | Romanèchite |
| cmmmech:roquesite | data/records/roquesite.yaml | maintained | Roquesite |
| cmmmech:roscoelite | data/records/roscoelite.yaml | maintained | Roscoelite |
| cmmmech:rozenite | data/records/rozenite.yaml | maintained | Rozenite |
| cmmmech:rutherfordine | data/records/rutherfordine.yaml | maintained | Rutherfordine |
| cmmmech:rutile | data/records/rutile.yaml | maintained | Rutile |
| cmmmech:sabugalite | data/records/sabugalite.yaml | maintained | Sabugalite |
| cmmmech:sakuraiite | data/records/sakuraiite.yaml | maintained | Sakuraiite |
| cmmmech:saleeite | data/records/saleeite.yaml | maintained | Saléeite |
| cmmmech:saponite | data/records/saponite.yaml | maintained | Saponite |
| cmmmech:sauconite | data/records/sauconite.yaml | maintained | Sauconite |
| cmmmech:scheelite | data/records/scheelite.yaml | maintained | Scheelite |
| cmmmech:schertelite | data/records/schertelite.yaml | maintained | Schertelite |
| cmmmech:schoepite | data/records/schoepite.yaml | maintained | Schoepite |
| cmmmech:schwertmannite | data/records/schwertmannite.yaml | maintained | Schwertmannite |
| cmmmech:scorodite | data/records/scorodite.yaml | maintained | Scorodite |
| cmmmech:senarmontite | data/records/senarmontite.yaml | maintained | Senarmontite |
| cmmmech:sepiolite | data/records/sepiolite.yaml | maintained | Sepiolite |
| cmmmech:siderite | data/records/siderite.yaml | maintained | Siderite |
| cmmmech:simonkolleite | data/records/simonkolleite.yaml | maintained | Simonkolleite |
| cmmmech:sklodowskite | data/records/sklodowskite.yaml | maintained | Sklodowskite |
| cmmmech:skutterudite | data/records/skutterudite.yaml | maintained | Skutterudite |
| cmmmech:smithsonite | data/records/smithsonite.yaml | maintained | Smithsonite |
| cmmmech:soddyite | data/records/soddyite.yaml | maintained | Soddyite |
| cmmmech:sphalerite | data/records/sphalerite.yaml | maintained | Sphalerite |
| cmmmech:spodumene | data/records/spodumene.yaml | maintained | Spodumene |
| cmmmech:stannite | data/records/stannite.yaml | maintained | Stannite |
| cmmmech:stevensite | data/records/stevensite.yaml | maintained | Stevensite |
| cmmmech:stibnite | data/records/stibnite.yaml | maintained | Stibnite |
| cmmmech:stolzite | data/records/stolzite.yaml | maintained | Stolzite |
| cmmmech:strengite | data/records/strengite.yaml | maintained | Strengite |
| cmmmech:strontianite | data/records/strontianite.yaml | maintained | Strontianite |
| cmmmech:struvite | data/records/struvite.yaml | maintained | Struvite |
| cmmmech:struvite-k | data/records/struvite-k.yaml | maintained | Struvite-(K) |
| cmmmech:studtite | data/records/studtite.yaml | maintained | Studtite |
| cmmmech:sulfoborite | data/records/sulfoborite.yaml | maintained | Sulfoborite |
| cmmmech:svanbergite | data/records/svanbergite.yaml | maintained | Svanbergite |
| cmmmech:switzerite | data/records/switzerite.yaml | maintained | Switzerite |
| cmmmech:synchysite-ce | data/records/synchysite-ce.yaml | maintained | Synchysite-(Ce) |
| cmmmech:szaibelyite | data/records/szaibelyite.yaml | maintained | Szaibélyite |
| cmmmech:szomolnokite | data/records/szomolnokite.yaml | maintained | Szomolnokite |
| cmmmech:talc | data/records/talc.yaml | maintained | Talc |
| cmmmech:tennantite-in | data/records/tennantite-in.yaml | maintained | Tennantite-(In) |
| cmmmech:tenorite | data/records/tenorite.yaml | maintained | Tenorite |
| cmmmech:thomasclarkite-y | data/records/thomasclarkite-y.yaml | maintained | Thomasclarkite-(Y) |
| cmmmech:tincalconite | data/records/tincalconite.yaml | maintained | Tincalconite |
| cmmmech:titanite | data/records/titanite.yaml | maintained | Titanite |
| cmmmech:todorokite | data/records/todorokite.yaml | maintained | Todorokite |
| cmmmech:torbernite | data/records/torbernite.yaml | maintained | Torbernite |
| cmmmech:triphylite | data/records/triphylite.yaml | maintained | Triphylite |
| cmmmech:troilite | data/records/troilite.yaml | maintained | Troilite |
| cmmmech:tunellite | data/records/tunellite.yaml | maintained | Tunellite |
| cmmmech:ulexite | data/records/ulexite.yaml | maintained | Ulexite |
| cmmmech:uramphite | data/records/uramphite.yaml | maintained | Uramphite |
| cmmmech:uraninite | data/records/uraninite.yaml | maintained | Uraninite |
| cmmmech:uranophane | data/records/uranophane.yaml | maintained | Uranophane |
| cmmmech:uranopilite | data/records/uranopilite.yaml | maintained | Uranopilite |
| cmmmech:vaesite | data/records/vaesite.yaml | maintained | Vaesite |
| cmmmech:vandenbrandeite | data/records/vandenbrandeite.yaml | maintained | Vandenbrandeite |
| cmmmech:variscite | data/records/variscite.yaml | maintained | Variscite |
| cmmmech:vaterite | data/records/vaterite.yaml | maintained | Vaterite |
| cmmmech:veatchite | data/records/veatchite.yaml | maintained | Veatchite |
| cmmmech:violarite | data/records/violarite.yaml | maintained | Violarite |
| cmmmech:vivianite | data/records/vivianite.yaml | maintained | Vivianite |
| cmmmech:voltaite | data/records/voltaite.yaml | maintained | Voltaite |
| cmmmech:weddellite | data/records/weddellite.yaml | maintained | Weddellite |
| cmmmech:weeksite | data/records/weeksite.yaml | maintained | Weeksite |
| cmmmech:wheatleyite | data/records/wheatleyite.yaml | maintained | Wheatleyite |
| cmmmech:whewellite | data/records/whewellite.yaml | maintained | Whewellite |
| cmmmech:whitlockite | data/records/whitlockite.yaml | maintained | Whitlockite |
| cmmmech:willemite | data/records/willemite.yaml | maintained | Willemite |
| cmmmech:wollastonite | data/records/wollastonite.yaml | maintained | Wollastonite |
| cmmmech:woodhouseite | data/records/woodhouseite.yaml | maintained | Woodhouseite |
| cmmmech:wulfenite | data/records/wulfenite.yaml | maintained | Wulfenite |
| cmmmech:wurtzite | data/records/wurtzite.yaml | maintained | Wurtzite |
| cmmmech:xenotime-gd | data/records/xenotime-gd.yaml | maintained | Xenotime-(Gd) |
| cmmmech:xenotime-y | data/records/xenotime-y.yaml | maintained | Xenotime-(Y) |
| cmmmech:xenotime-yb | data/records/xenotime-yb.yaml | maintained | Xenotime-(Yb) |
| cmmmech:yanomamite | data/records/yanomamite.yaml | maintained | Yanomamite |
| cmmmech:yusupovite | data/records/yusupovite.yaml | maintained | Yusupovite |
| cmmmech:zeunerite | data/records/zeunerite.yaml | maintained | Zeunerite |
| cmmmech:zincite | data/records/zincite.yaml | maintained | Zincite |
| cmmmech:zincobriartite | data/records/zincobriartite.yaml | maintained | Zincobriartite |
| cmmmech:zippeite | data/records/zippeite.yaml | maintained | Zippeite |
| cmmmech:zircon | data/records/zircon.yaml | maintained | Zircon |
| cmmmech:zirconolite | data/records/zirconolite.yaml | maintained | Zirconolite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate (mineral cohort) | passed | True | cmmmech:acanthite, cmmmech:adamsite-y, cmmmech:akaganeite, cmmmech:alabandite, cmmmech:albite, cmmmech:alburnite, cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:alunite, cmmmech:amblygonite, cmmmech:ameghinite, cmmmech:ammonioborite, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:ancylite-ce, cmmmech:andersonite, cmmmech:anglesite, cmmmech:anhydrite, cmmmech:anilite, cmmmech:annabergite, cmmmech:anorthite, cmmmech:aragonite, cmmmech:argentojarosite, cmmmech:argyrodite, cmmmech:aristarainite, cmmmech:arsenopyrite, cmmmech:artinite, cmmmech:asbolane, cmmmech:atacamite, cmmmech:autunite, cmmmech:azurite, cmmmech:baddeleyite, cmmmech:bainbridgeite-ndce, cmmmech:bainbridgeite-yce, cmmmech:baricite, cmmmech:bassanite, cmmmech:becquerelite, cmmmech:beudantite, cmmmech:billietite, cmmmech:birnessite, cmmmech:bismuthinite, cmmmech:bixbyite-mn, cmmmech:bobierrite, cmmmech:boehmite, cmmmech:boltwoodite, cmmmech:boracite, cmmmech:borax, cmmmech:bornite, cmmmech:briartite, cmmmech:brochantite, cmmmech:brookite, cmmmech:brucite, cmmmech:brushite, cmmmech:burbankite, cmmmech:cadmoindite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:calcioveatchite, cmmmech:calcite, cmmmech:carnotite, cmmmech:carrollite, cmmmech:cassiterite, cmmmech:catapleiite, cmmmech:cattiite, cmmmech:cavansite, cmmmech:caysichite-y, cmmmech:celestine, cmmmech:cerianite-ce, cmmmech:cerussite, cmmmech:chalcocite, cmmmech:chalcopyrite, cmmmech:chernikovite, cmmmech:childrenite, cmmmech:chlorapatite, cmmmech:chromite, cmmmech:chrysotile, cmmmech:chukanovite, cmmmech:churchite-y, cmmmech:cinnabar, cmmmech:cobaltite, cmmmech:coffinite, cmmmech:colemanite, cmmmech:compreignacite, cmmmech:coquimbite, cmmmech:cordylite-ce, cmmmech:corkite, cmmmech:covellite, cmmmech:crandallite, cmmmech:cryptomelane, cmmmech:cuprite, cmmmech:cuprosklodowskite, cmmmech:curite, cmmmech:digenite, cmmmech:diopside, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:dypingite, cmmmech:dzhalindite, cmmmech:elpidite, cmmmech:enstatite, cmmmech:eosphorite, cmmmech:erythrite, cmmmech:ezcurrite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:felsobanyaite, cmmmech:feroxyhyte, cmmmech:ferricopiapite, cmmmech:ferrihydrite, cmmmech:ferrokesterite, cmmmech:florencite-ce, cmmmech:florencite-la, cmmmech:fluorapatite, cmmmech:fluorite, cmmmech:forsterite, cmmmech:fritzscheite, cmmmech:galena, cmmmech:germanite, cmmmech:gersdorffite, cmmmech:gibbsite, cmmmech:ginorite, cmmmech:glushinskite, cmmmech:goethite, cmmmech:goldmanite, cmmmech:gorceixite, cmmmech:gowerite, cmmmech:goyazite, cmmmech:greenockite, cmmmech:greigite, cmmmech:gypsum, cmmmech:gysinite-nd, cmmmech:hafnon, cmmmech:hannayite, cmmmech:haradaite, cmmmech:hauerite, cmmmech:hausmannite, cmmmech:hawleyite, cmmmech:hazenite, cmmmech:heazlewoodite, cmmmech:hematite, cmmmech:hemimorphite, cmmmech:heterogenite, cmmmech:heterosite, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:huntite, cmmmech:hureaulite, cmmmech:hydroboracite, cmmmech:hydrocerussite, cmmmech:hydromagnesite, cmmmech:hydroniumjarosite, cmmmech:hydrotalcite, cmmmech:hydroxylapatite, cmmmech:hydrozincite, cmmmech:ilmenite, cmmmech:inderborite, cmmmech:inderite, cmmmech:indite, cmmmech:inyoite, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaliborite, cmmmech:kaolinite, cmmmech:katsarosite, cmmmech:kernite, cmmmech:kesterite, cmmmech:kornelite, cmmmech:kozoite-la, cmmmech:kozoite-nd, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:kurnakovite, cmmmech:kutnohorite, cmmmech:laforetite, cmmmech:lansfordite, cmmmech:lanthanite-ce, cmmmech:lanthanite-la, cmmmech:lanthanite-nd, cmmmech:larderellite, cmmmech:laueite, cmmmech:lepidocrocite, cmmmech:libethenite, cmmmech:lindbergite, cmmmech:lithiophilite, cmmmech:lizardite, cmmmech:loellingite, cmmmech:lorenzenite, cmmmech:ludlamite, cmmmech:mackinawite, cmmmech:maghemite, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganite, cmmmech:marcasite, cmmmech:mcallisterite, cmmmech:mckelveyite-y, cmmmech:melanterite, cmmmech:meta-ankoleite, cmmmech:metacinnabar, cmmmech:metaschoepite, cmmmech:metastudtite, cmmmech:metatorbernite, cmmmech:metatyuyamunite, cmmmech:metavivianite, cmmmech:metazeunerite, cmmmech:meyerhofferite, cmmmech:microcline, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:monazite-ce, cmmmech:monazite-gd, cmmmech:monazite-la, cmmmech:monazite-nd, cmmmech:monazite-sm, cmmmech:monetite, cmmmech:monohydrocalcite, cmmmech:montebrasite, cmmmech:montmorillonite, cmmmech:montroseite, cmmmech:moolooite, cmmmech:muscovite, cmmmech:natroboltwoodite, cmmmech:natrojarosite, cmmmech:navajoite, cmmmech:nepheline, cmmmech:nesquehonite, cmmmech:newberyite, cmmmech:ningyoite, cmmmech:nobleite, cmmmech:nontronite, cmmmech:orpiment, cmmmech:orthoclase, cmmmech:otavite, cmmmech:palygorskite, cmmmech:paracoquimbite, cmmmech:paramontroseite, cmmmech:parasymplesite, cmmmech:parauranophane, cmmmech:pascoite, cmmmech:pentagonite, cmmmech:pentlandite, cmmmech:perovskite, cmmmech:pertlikite, cmmmech:petalite, cmmmech:petrukite, cmmmech:phlogopite, cmmmech:phosphoferrite, cmmmech:phosphophyllite, cmmmech:piilonenite-nd, cmmmech:pinnoite, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:polylithionite, cmmmech:powellite, cmmmech:preobrazhenskite, cmmmech:priceite, cmmmech:probertite, cmmmech:pyrite, cmmmech:pyroaurite, cmmmech:pyrochroite, cmmmech:pyrolusite, cmmmech:pyromorphite, cmmmech:pyrrhotite, cmmmech:quenstedtite, cmmmech:ramsdellite, cmmmech:realgar, cmmmech:regerite, cmmmech:renierite, cmmmech:rhabdophane-ce, cmmmech:rhabdophane-la, cmmmech:rhodochrosite, cmmmech:rhomboclase, cmmmech:richetite, cmmmech:riebeckite, cmmmech:rivadavite, cmmmech:romanechite, cmmmech:roquesite, cmmmech:roscoelite, cmmmech:rozenite, cmmmech:rutherfordine, cmmmech:rutile, cmmmech:sabugalite, cmmmech:sakuraiite, cmmmech:saleeite, cmmmech:saponite, cmmmech:sauconite, cmmmech:scheelite, cmmmech:schertelite, cmmmech:schoepite, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:senarmontite, cmmmech:sepiolite, cmmmech:siderite, cmmmech:simonkolleite, cmmmech:sklodowskite, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:soddyite, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:stevensite, cmmmech:stibnite, cmmmech:stolzite, cmmmech:strengite, cmmmech:strontianite, cmmmech:struvite, cmmmech:struvite-k, cmmmech:studtite, cmmmech:sulfoborite, cmmmech:svanbergite, cmmmech:switzerite, cmmmech:synchysite-ce, cmmmech:szaibelyite, cmmmech:szomolnokite, cmmmech:talc, cmmmech:tennantite-in, cmmmech:tenorite, cmmmech:thomasclarkite-y, cmmmech:tincalconite, cmmmech:titanite, cmmmech:todorokite, cmmmech:torbernite, cmmmech:triphylite, cmmmech:troilite, cmmmech:tunellite, cmmmech:ulexite, cmmmech:uramphite, cmmmech:uraninite, cmmmech:uranophane, cmmmech:uranopilite, cmmmech:vaesite, cmmmech:vandenbrandeite, cmmmech:variscite, cmmmech:vaterite, cmmmech:veatchite, cmmmech:violarite, cmmmech:vivianite, cmmmech:voltaite, cmmmech:weddellite, cmmmech:weeksite, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:whitlockite, cmmmech:willemite, cmmmech:wollastonite, cmmmech:woodhouseite, cmmmech:wulfenite, cmmmech:wurtzite, cmmmech:xenotime-gd, cmmmech:xenotime-y, cmmmech:xenotime-yb, cmmmech:yanomamite, cmmmech:yusupovite, cmmmech:zeunerite, cmmmech:zincite, cmmmech:zincobriartite, cmmmech:zippeite, cmmmech:zircon, cmmmech:zirconolite | All 365 records in the mineral cohort pass LinkML structural and semantic validation with 0 errors. |
| cmmmech validate-history (mineral cohort) | passed | True | cmmmech:acanthite, cmmmech:adamsite-y, cmmmech:akaganeite, cmmmech:alabandite, cmmmech:albite, cmmmech:alburnite, cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:alunite, cmmmech:amblygonite, cmmmech:ameghinite, cmmmech:ammonioborite, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:ancylite-ce, cmmmech:andersonite, cmmmech:anglesite, cmmmech:anhydrite, cmmmech:anilite, cmmmech:annabergite, cmmmech:anorthite, cmmmech:aragonite, cmmmech:argentojarosite, cmmmech:argyrodite, cmmmech:aristarainite, cmmmech:arsenopyrite, cmmmech:artinite, cmmmech:asbolane, cmmmech:atacamite, cmmmech:autunite, cmmmech:azurite, cmmmech:baddeleyite, cmmmech:bainbridgeite-ndce, cmmmech:bainbridgeite-yce, cmmmech:baricite, cmmmech:bassanite, cmmmech:becquerelite, cmmmech:beudantite, cmmmech:billietite, cmmmech:birnessite, cmmmech:bismuthinite, cmmmech:bixbyite-mn, cmmmech:bobierrite, cmmmech:boehmite, cmmmech:boltwoodite, cmmmech:boracite, cmmmech:borax, cmmmech:bornite, cmmmech:briartite, cmmmech:brochantite, cmmmech:brookite, cmmmech:brucite, cmmmech:brushite, cmmmech:burbankite, cmmmech:cadmoindite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:calcioveatchite, cmmmech:calcite, cmmmech:carnotite, cmmmech:carrollite, cmmmech:cassiterite, cmmmech:catapleiite, cmmmech:cattiite, cmmmech:cavansite, cmmmech:caysichite-y, cmmmech:celestine, cmmmech:cerianite-ce, cmmmech:cerussite, cmmmech:chalcocite, cmmmech:chalcopyrite, cmmmech:chernikovite, cmmmech:childrenite, cmmmech:chlorapatite, cmmmech:chromite, cmmmech:chrysotile, cmmmech:chukanovite, cmmmech:churchite-y, cmmmech:cinnabar, cmmmech:cobaltite, cmmmech:coffinite, cmmmech:colemanite, cmmmech:compreignacite, cmmmech:coquimbite, cmmmech:cordylite-ce, cmmmech:corkite, cmmmech:covellite, cmmmech:crandallite, cmmmech:cryptomelane, cmmmech:cuprite, cmmmech:cuprosklodowskite, cmmmech:curite, cmmmech:digenite, cmmmech:diopside, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:dypingite, cmmmech:dzhalindite, cmmmech:elpidite, cmmmech:enstatite, cmmmech:eosphorite, cmmmech:erythrite, cmmmech:ezcurrite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:felsobanyaite, cmmmech:feroxyhyte, cmmmech:ferricopiapite, cmmmech:ferrihydrite, cmmmech:ferrokesterite, cmmmech:florencite-ce, cmmmech:florencite-la, cmmmech:fluorapatite, cmmmech:fluorite, cmmmech:forsterite, cmmmech:fritzscheite, cmmmech:galena, cmmmech:germanite, cmmmech:gersdorffite, cmmmech:gibbsite, cmmmech:ginorite, cmmmech:glushinskite, cmmmech:goethite, cmmmech:goldmanite, cmmmech:gorceixite, cmmmech:gowerite, cmmmech:goyazite, cmmmech:greenockite, cmmmech:greigite, cmmmech:gypsum, cmmmech:gysinite-nd, cmmmech:hafnon, cmmmech:hannayite, cmmmech:haradaite, cmmmech:hauerite, cmmmech:hausmannite, cmmmech:hawleyite, cmmmech:hazenite, cmmmech:heazlewoodite, cmmmech:hematite, cmmmech:hemimorphite, cmmmech:heterogenite, cmmmech:heterosite, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:huntite, cmmmech:hureaulite, cmmmech:hydroboracite, cmmmech:hydrocerussite, cmmmech:hydromagnesite, cmmmech:hydroniumjarosite, cmmmech:hydrotalcite, cmmmech:hydroxylapatite, cmmmech:hydrozincite, cmmmech:ilmenite, cmmmech:inderborite, cmmmech:inderite, cmmmech:indite, cmmmech:inyoite, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaliborite, cmmmech:kaolinite, cmmmech:katsarosite, cmmmech:kernite, cmmmech:kesterite, cmmmech:kornelite, cmmmech:kozoite-la, cmmmech:kozoite-nd, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:kurnakovite, cmmmech:kutnohorite, cmmmech:laforetite, cmmmech:lansfordite, cmmmech:lanthanite-ce, cmmmech:lanthanite-la, cmmmech:lanthanite-nd, cmmmech:larderellite, cmmmech:laueite, cmmmech:lepidocrocite, cmmmech:libethenite, cmmmech:lindbergite, cmmmech:lithiophilite, cmmmech:lizardite, cmmmech:loellingite, cmmmech:lorenzenite, cmmmech:ludlamite, cmmmech:mackinawite, cmmmech:maghemite, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganite, cmmmech:marcasite, cmmmech:mcallisterite, cmmmech:mckelveyite-y, cmmmech:melanterite, cmmmech:meta-ankoleite, cmmmech:metacinnabar, cmmmech:metaschoepite, cmmmech:metastudtite, cmmmech:metatorbernite, cmmmech:metatyuyamunite, cmmmech:metavivianite, cmmmech:metazeunerite, cmmmech:meyerhofferite, cmmmech:microcline, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:monazite-ce, cmmmech:monazite-gd, cmmmech:monazite-la, cmmmech:monazite-nd, cmmmech:monazite-sm, cmmmech:monetite, cmmmech:monohydrocalcite, cmmmech:montebrasite, cmmmech:montmorillonite, cmmmech:montroseite, cmmmech:moolooite, cmmmech:muscovite, cmmmech:natroboltwoodite, cmmmech:natrojarosite, cmmmech:navajoite, cmmmech:nepheline, cmmmech:nesquehonite, cmmmech:newberyite, cmmmech:ningyoite, cmmmech:nobleite, cmmmech:nontronite, cmmmech:orpiment, cmmmech:orthoclase, cmmmech:otavite, cmmmech:palygorskite, cmmmech:paracoquimbite, cmmmech:paramontroseite, cmmmech:parasymplesite, cmmmech:parauranophane, cmmmech:pascoite, cmmmech:pentagonite, cmmmech:pentlandite, cmmmech:perovskite, cmmmech:pertlikite, cmmmech:petalite, cmmmech:petrukite, cmmmech:phlogopite, cmmmech:phosphoferrite, cmmmech:phosphophyllite, cmmmech:piilonenite-nd, cmmmech:pinnoite, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:polylithionite, cmmmech:powellite, cmmmech:preobrazhenskite, cmmmech:priceite, cmmmech:probertite, cmmmech:pyrite, cmmmech:pyroaurite, cmmmech:pyrochroite, cmmmech:pyrolusite, cmmmech:pyromorphite, cmmmech:pyrrhotite, cmmmech:quenstedtite, cmmmech:ramsdellite, cmmmech:realgar, cmmmech:regerite, cmmmech:renierite, cmmmech:rhabdophane-ce, cmmmech:rhabdophane-la, cmmmech:rhodochrosite, cmmmech:rhomboclase, cmmmech:richetite, cmmmech:riebeckite, cmmmech:rivadavite, cmmmech:romanechite, cmmmech:roquesite, cmmmech:roscoelite, cmmmech:rozenite, cmmmech:rutherfordine, cmmmech:rutile, cmmmech:sabugalite, cmmmech:sakuraiite, cmmmech:saleeite, cmmmech:saponite, cmmmech:sauconite, cmmmech:scheelite, cmmmech:schertelite, cmmmech:schoepite, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:senarmontite, cmmmech:sepiolite, cmmmech:siderite, cmmmech:simonkolleite, cmmmech:sklodowskite, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:soddyite, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:stevensite, cmmmech:stibnite, cmmmech:stolzite, cmmmech:strengite, cmmmech:strontianite, cmmmech:struvite, cmmmech:struvite-k, cmmmech:studtite, cmmmech:sulfoborite, cmmmech:svanbergite, cmmmech:switzerite, cmmmech:synchysite-ce, cmmmech:szaibelyite, cmmmech:szomolnokite, cmmmech:talc, cmmmech:tennantite-in, cmmmech:tenorite, cmmmech:thomasclarkite-y, cmmmech:tincalconite, cmmmech:titanite, cmmmech:todorokite, cmmmech:torbernite, cmmmech:triphylite, cmmmech:troilite, cmmmech:tunellite, cmmmech:ulexite, cmmmech:uramphite, cmmmech:uraninite, cmmmech:uranophane, cmmmech:uranopilite, cmmmech:vaesite, cmmmech:vandenbrandeite, cmmmech:variscite, cmmmech:vaterite, cmmmech:veatchite, cmmmech:violarite, cmmmech:vivianite, cmmmech:voltaite, cmmmech:weddellite, cmmmech:weeksite, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:whitlockite, cmmmech:willemite, cmmmech:wollastonite, cmmmech:woodhouseite, cmmmech:wulfenite, cmmmech:wurtzite, cmmmech:xenotime-gd, cmmmech:xenotime-y, cmmmech:xenotime-yb, cmmmech:yanomamite, cmmmech:yusupovite, cmmmech:zeunerite, cmmmech:zincite, cmmmech:zincobriartite, cmmmech:zippeite, cmmmech:zircon, cmmmech:zirconolite | All curation_history entries and history_refs sidecars across the 365 mineral records resolve and validate cleanly. |
| Ontology ID-label consistency (mineral cohort) | passed | True | cmmmech:acanthite, cmmmech:adamsite-y, cmmmech:akaganeite, cmmmech:alabandite, cmmmech:albite, cmmmech:alburnite, cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:alunite, cmmmech:amblygonite, cmmmech:ameghinite, cmmmech:ammonioborite, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:ancylite-ce, cmmmech:andersonite, cmmmech:anglesite, cmmmech:anhydrite, cmmmech:anilite, cmmmech:annabergite, cmmmech:anorthite, cmmmech:aragonite, cmmmech:argentojarosite, cmmmech:argyrodite, cmmmech:aristarainite, cmmmech:arsenopyrite, cmmmech:artinite, cmmmech:asbolane, cmmmech:atacamite, cmmmech:autunite, cmmmech:azurite, cmmmech:baddeleyite, cmmmech:bainbridgeite-ndce, cmmmech:bainbridgeite-yce, cmmmech:baricite, cmmmech:bassanite, cmmmech:becquerelite, cmmmech:beudantite, cmmmech:billietite, cmmmech:birnessite, cmmmech:bismuthinite, cmmmech:bixbyite-mn, cmmmech:bobierrite, cmmmech:boehmite, cmmmech:boltwoodite, cmmmech:boracite, cmmmech:borax, cmmmech:bornite, cmmmech:briartite, cmmmech:brochantite, cmmmech:brookite, cmmmech:brucite, cmmmech:brushite, cmmmech:burbankite, cmmmech:cadmoindite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:calcioveatchite, cmmmech:calcite, cmmmech:carnotite, cmmmech:carrollite, cmmmech:cassiterite, cmmmech:catapleiite, cmmmech:cattiite, cmmmech:cavansite, cmmmech:caysichite-y, cmmmech:celestine, cmmmech:cerianite-ce, cmmmech:cerussite, cmmmech:chalcocite, cmmmech:chalcopyrite, cmmmech:chernikovite, cmmmech:childrenite, cmmmech:chlorapatite, cmmmech:chromite, cmmmech:chrysotile, cmmmech:chukanovite, cmmmech:churchite-y, cmmmech:cinnabar, cmmmech:cobaltite, cmmmech:coffinite, cmmmech:colemanite, cmmmech:compreignacite, cmmmech:coquimbite, cmmmech:cordylite-ce, cmmmech:corkite, cmmmech:covellite, cmmmech:crandallite, cmmmech:cryptomelane, cmmmech:cuprite, cmmmech:cuprosklodowskite, cmmmech:curite, cmmmech:digenite, cmmmech:diopside, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:dypingite, cmmmech:dzhalindite, cmmmech:elpidite, cmmmech:enstatite, cmmmech:eosphorite, cmmmech:erythrite, cmmmech:ezcurrite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:felsobanyaite, cmmmech:feroxyhyte, cmmmech:ferricopiapite, cmmmech:ferrihydrite, cmmmech:ferrokesterite, cmmmech:florencite-ce, cmmmech:florencite-la, cmmmech:fluorapatite, cmmmech:fluorite, cmmmech:forsterite, cmmmech:fritzscheite, cmmmech:galena, cmmmech:germanite, cmmmech:gersdorffite, cmmmech:gibbsite, cmmmech:ginorite, cmmmech:glushinskite, cmmmech:goethite, cmmmech:goldmanite, cmmmech:gorceixite, cmmmech:gowerite, cmmmech:goyazite, cmmmech:greenockite, cmmmech:greigite, cmmmech:gypsum, cmmmech:gysinite-nd, cmmmech:hafnon, cmmmech:hannayite, cmmmech:haradaite, cmmmech:hauerite, cmmmech:hausmannite, cmmmech:hawleyite, cmmmech:hazenite, cmmmech:heazlewoodite, cmmmech:hematite, cmmmech:hemimorphite, cmmmech:heterogenite, cmmmech:heterosite, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:huntite, cmmmech:hureaulite, cmmmech:hydroboracite, cmmmech:hydrocerussite, cmmmech:hydromagnesite, cmmmech:hydroniumjarosite, cmmmech:hydrotalcite, cmmmech:hydroxylapatite, cmmmech:hydrozincite, cmmmech:ilmenite, cmmmech:inderborite, cmmmech:inderite, cmmmech:indite, cmmmech:inyoite, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaliborite, cmmmech:kaolinite, cmmmech:katsarosite, cmmmech:kernite, cmmmech:kesterite, cmmmech:kornelite, cmmmech:kozoite-la, cmmmech:kozoite-nd, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:kurnakovite, cmmmech:kutnohorite, cmmmech:laforetite, cmmmech:lansfordite, cmmmech:lanthanite-ce, cmmmech:lanthanite-la, cmmmech:lanthanite-nd, cmmmech:larderellite, cmmmech:laueite, cmmmech:lepidocrocite, cmmmech:libethenite, cmmmech:lindbergite, cmmmech:lithiophilite, cmmmech:lizardite, cmmmech:loellingite, cmmmech:lorenzenite, cmmmech:ludlamite, cmmmech:mackinawite, cmmmech:maghemite, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganite, cmmmech:marcasite, cmmmech:mcallisterite, cmmmech:mckelveyite-y, cmmmech:melanterite, cmmmech:meta-ankoleite, cmmmech:metacinnabar, cmmmech:metaschoepite, cmmmech:metastudtite, cmmmech:metatorbernite, cmmmech:metatyuyamunite, cmmmech:metavivianite, cmmmech:metazeunerite, cmmmech:meyerhofferite, cmmmech:microcline, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:monazite-ce, cmmmech:monazite-gd, cmmmech:monazite-la, cmmmech:monazite-nd, cmmmech:monazite-sm, cmmmech:monetite, cmmmech:monohydrocalcite, cmmmech:montebrasite, cmmmech:montmorillonite, cmmmech:montroseite, cmmmech:moolooite, cmmmech:muscovite, cmmmech:natroboltwoodite, cmmmech:natrojarosite, cmmmech:navajoite, cmmmech:nepheline, cmmmech:nesquehonite, cmmmech:newberyite, cmmmech:ningyoite, cmmmech:nobleite, cmmmech:nontronite, cmmmech:orpiment, cmmmech:orthoclase, cmmmech:otavite, cmmmech:palygorskite, cmmmech:paracoquimbite, cmmmech:paramontroseite, cmmmech:parasymplesite, cmmmech:parauranophane, cmmmech:pascoite, cmmmech:pentagonite, cmmmech:pentlandite, cmmmech:perovskite, cmmmech:pertlikite, cmmmech:petalite, cmmmech:petrukite, cmmmech:phlogopite, cmmmech:phosphoferrite, cmmmech:phosphophyllite, cmmmech:piilonenite-nd, cmmmech:pinnoite, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:polylithionite, cmmmech:powellite, cmmmech:preobrazhenskite, cmmmech:priceite, cmmmech:probertite, cmmmech:pyrite, cmmmech:pyroaurite, cmmmech:pyrochroite, cmmmech:pyrolusite, cmmmech:pyromorphite, cmmmech:pyrrhotite, cmmmech:quenstedtite, cmmmech:ramsdellite, cmmmech:realgar, cmmmech:regerite, cmmmech:renierite, cmmmech:rhabdophane-ce, cmmmech:rhabdophane-la, cmmmech:rhodochrosite, cmmmech:rhomboclase, cmmmech:richetite, cmmmech:riebeckite, cmmmech:rivadavite, cmmmech:romanechite, cmmmech:roquesite, cmmmech:roscoelite, cmmmech:rozenite, cmmmech:rutherfordine, cmmmech:rutile, cmmmech:sabugalite, cmmmech:sakuraiite, cmmmech:saleeite, cmmmech:saponite, cmmmech:sauconite, cmmmech:scheelite, cmmmech:schertelite, cmmmech:schoepite, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:senarmontite, cmmmech:sepiolite, cmmmech:siderite, cmmmech:simonkolleite, cmmmech:sklodowskite, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:soddyite, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:stevensite, cmmmech:stibnite, cmmmech:stolzite, cmmmech:strengite, cmmmech:strontianite, cmmmech:struvite, cmmmech:struvite-k, cmmmech:studtite, cmmmech:sulfoborite, cmmmech:svanbergite, cmmmech:switzerite, cmmmech:synchysite-ce, cmmmech:szaibelyite, cmmmech:szomolnokite, cmmmech:talc, cmmmech:tennantite-in, cmmmech:tenorite, cmmmech:thomasclarkite-y, cmmmech:tincalconite, cmmmech:titanite, cmmmech:todorokite, cmmmech:torbernite, cmmmech:triphylite, cmmmech:troilite, cmmmech:tunellite, cmmmech:ulexite, cmmmech:uramphite, cmmmech:uraninite, cmmmech:uranophane, cmmmech:uranopilite, cmmmech:vaesite, cmmmech:vandenbrandeite, cmmmech:variscite, cmmmech:vaterite, cmmmech:veatchite, cmmmech:violarite, cmmmech:vivianite, cmmmech:voltaite, cmmmech:weddellite, cmmmech:weeksite, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:whitlockite, cmmmech:willemite, cmmmech:wollastonite, cmmmech:woodhouseite, cmmmech:wulfenite, cmmmech:wurtzite, cmmmech:xenotime-gd, cmmmech:xenotime-y, cmmmech:xenotime-yb, cmmmech:yanomamite, cmmmech:yusupovite, cmmmech:zeunerite, cmmmech:zincite, cmmmech:zincobriartite, cmmmech:zippeite, cmmmech:zircon, cmmmech:zirconolite | Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 365 mineral records carries a consistent canonical label with 0 cross-corpus conflicts. |

## Scientific And Domain Assessments

### Mineral species identity, stoichiometry, criticality, and microbial mechanisms

completeness: supported. Targets: cmmmech:acanthite, cmmmech:adamsite-y, cmmmech:akaganeite, cmmmech:alabandite, cmmmech:albite, cmmmech:alburnite, cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:alunite, cmmmech:amblygonite, cmmmech:ameghinite, cmmmech:ammonioborite, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:ancylite-ce, cmmmech:andersonite, cmmmech:anglesite, cmmmech:anhydrite, cmmmech:anilite, cmmmech:annabergite, cmmmech:anorthite, cmmmech:aragonite, cmmmech:argentojarosite, cmmmech:argyrodite, cmmmech:aristarainite, cmmmech:arsenopyrite, cmmmech:artinite, cmmmech:asbolane, cmmmech:atacamite, cmmmech:autunite, cmmmech:azurite, cmmmech:baddeleyite, cmmmech:bainbridgeite-ndce, cmmmech:bainbridgeite-yce, cmmmech:baricite, cmmmech:bassanite, cmmmech:becquerelite, cmmmech:beudantite, cmmmech:billietite, cmmmech:birnessite, cmmmech:bismuthinite, cmmmech:bixbyite-mn, cmmmech:bobierrite, cmmmech:boehmite, cmmmech:boltwoodite, cmmmech:boracite, cmmmech:borax, cmmmech:bornite, cmmmech:briartite, cmmmech:brochantite, cmmmech:brookite, cmmmech:brucite, cmmmech:brushite, cmmmech:burbankite, cmmmech:cadmoindite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:calcioveatchite, cmmmech:calcite, cmmmech:carnotite, cmmmech:carrollite, cmmmech:cassiterite, cmmmech:catapleiite, cmmmech:cattiite, cmmmech:cavansite, cmmmech:caysichite-y, cmmmech:celestine, cmmmech:cerianite-ce, cmmmech:cerussite, cmmmech:chalcocite, cmmmech:chalcopyrite, cmmmech:chernikovite, cmmmech:childrenite, cmmmech:chlorapatite, cmmmech:chromite, cmmmech:chrysotile, cmmmech:chukanovite, cmmmech:churchite-y, cmmmech:cinnabar, cmmmech:cobaltite, cmmmech:coffinite, cmmmech:colemanite, cmmmech:compreignacite, cmmmech:coquimbite, cmmmech:cordylite-ce, cmmmech:corkite, cmmmech:covellite, cmmmech:crandallite, cmmmech:cryptomelane, cmmmech:cuprite, cmmmech:cuprosklodowskite, cmmmech:curite, cmmmech:digenite, cmmmech:diopside, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:dypingite, cmmmech:dzhalindite, cmmmech:elpidite, cmmmech:enstatite, cmmmech:eosphorite, cmmmech:erythrite, cmmmech:ezcurrite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:felsobanyaite, cmmmech:feroxyhyte, cmmmech:ferricopiapite, cmmmech:ferrihydrite, cmmmech:ferrokesterite, cmmmech:florencite-ce, cmmmech:florencite-la, cmmmech:fluorapatite, cmmmech:fluorite, cmmmech:forsterite, cmmmech:fritzscheite, cmmmech:galena, cmmmech:germanite, cmmmech:gersdorffite, cmmmech:gibbsite, cmmmech:ginorite, cmmmech:glushinskite, cmmmech:goethite, cmmmech:goldmanite, cmmmech:gorceixite, cmmmech:gowerite, cmmmech:goyazite, cmmmech:greenockite, cmmmech:greigite, cmmmech:gypsum, cmmmech:gysinite-nd, cmmmech:hafnon, cmmmech:hannayite, cmmmech:haradaite, cmmmech:hauerite, cmmmech:hausmannite, cmmmech:hawleyite, cmmmech:hazenite, cmmmech:heazlewoodite, cmmmech:hematite, cmmmech:hemimorphite, cmmmech:heterogenite, cmmmech:heterosite, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:huntite, cmmmech:hureaulite, cmmmech:hydroboracite, cmmmech:hydrocerussite, cmmmech:hydromagnesite, cmmmech:hydroniumjarosite, cmmmech:hydrotalcite, cmmmech:hydroxylapatite, cmmmech:hydrozincite, cmmmech:ilmenite, cmmmech:inderborite, cmmmech:inderite, cmmmech:indite, cmmmech:inyoite, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaliborite, cmmmech:kaolinite, cmmmech:katsarosite, cmmmech:kernite, cmmmech:kesterite, cmmmech:kornelite, cmmmech:kozoite-la, cmmmech:kozoite-nd, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:kurnakovite, cmmmech:kutnohorite, cmmmech:laforetite, cmmmech:lansfordite, cmmmech:lanthanite-ce, cmmmech:lanthanite-la, cmmmech:lanthanite-nd, cmmmech:larderellite, cmmmech:laueite, cmmmech:lepidocrocite, cmmmech:libethenite, cmmmech:lindbergite, cmmmech:lithiophilite, cmmmech:lizardite, cmmmech:loellingite, cmmmech:lorenzenite, cmmmech:ludlamite, cmmmech:mackinawite, cmmmech:maghemite, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganite, cmmmech:marcasite, cmmmech:mcallisterite, cmmmech:mckelveyite-y, cmmmech:melanterite, cmmmech:meta-ankoleite, cmmmech:metacinnabar, cmmmech:metaschoepite, cmmmech:metastudtite, cmmmech:metatorbernite, cmmmech:metatyuyamunite, cmmmech:metavivianite, cmmmech:metazeunerite, cmmmech:meyerhofferite, cmmmech:microcline, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:monazite-ce, cmmmech:monazite-gd, cmmmech:monazite-la, cmmmech:monazite-nd, cmmmech:monazite-sm, cmmmech:monetite, cmmmech:monohydrocalcite, cmmmech:montebrasite, cmmmech:montmorillonite, cmmmech:montroseite, cmmmech:moolooite, cmmmech:muscovite, cmmmech:natroboltwoodite, cmmmech:natrojarosite, cmmmech:navajoite, cmmmech:nepheline, cmmmech:nesquehonite, cmmmech:newberyite, cmmmech:ningyoite, cmmmech:nobleite, cmmmech:nontronite, cmmmech:orpiment, cmmmech:orthoclase, cmmmech:otavite, cmmmech:palygorskite, cmmmech:paracoquimbite, cmmmech:paramontroseite, cmmmech:parasymplesite, cmmmech:parauranophane, cmmmech:pascoite, cmmmech:pentagonite, cmmmech:pentlandite, cmmmech:perovskite, cmmmech:pertlikite, cmmmech:petalite, cmmmech:petrukite, cmmmech:phlogopite, cmmmech:phosphoferrite, cmmmech:phosphophyllite, cmmmech:piilonenite-nd, cmmmech:pinnoite, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:polylithionite, cmmmech:powellite, cmmmech:preobrazhenskite, cmmmech:priceite, cmmmech:probertite, cmmmech:pyrite, cmmmech:pyroaurite, cmmmech:pyrochroite, cmmmech:pyrolusite, cmmmech:pyromorphite, cmmmech:pyrrhotite, cmmmech:quenstedtite, cmmmech:ramsdellite, cmmmech:realgar, cmmmech:regerite, cmmmech:renierite, cmmmech:rhabdophane-ce, cmmmech:rhabdophane-la, cmmmech:rhodochrosite, cmmmech:rhomboclase, cmmmech:richetite, cmmmech:riebeckite, cmmmech:rivadavite, cmmmech:romanechite, cmmmech:roquesite, cmmmech:roscoelite, cmmmech:rozenite, cmmmech:rutherfordine, cmmmech:rutile, cmmmech:sabugalite, cmmmech:sakuraiite, cmmmech:saleeite, cmmmech:saponite, cmmmech:sauconite, cmmmech:scheelite, cmmmech:schertelite, cmmmech:schoepite, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:senarmontite, cmmmech:sepiolite, cmmmech:siderite, cmmmech:simonkolleite, cmmmech:sklodowskite, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:soddyite, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:stevensite, cmmmech:stibnite, cmmmech:stolzite, cmmmech:strengite, cmmmech:strontianite, cmmmech:struvite, cmmmech:struvite-k, cmmmech:studtite, cmmmech:sulfoborite, cmmmech:svanbergite, cmmmech:switzerite, cmmmech:synchysite-ce, cmmmech:szaibelyite, cmmmech:szomolnokite, cmmmech:talc, cmmmech:tennantite-in, cmmmech:tenorite, cmmmech:thomasclarkite-y, cmmmech:tincalconite, cmmmech:titanite, cmmmech:todorokite, cmmmech:torbernite, cmmmech:triphylite, cmmmech:troilite, cmmmech:tunellite, cmmmech:ulexite, cmmmech:uramphite, cmmmech:uraninite, cmmmech:uranophane, cmmmech:uranopilite, cmmmech:vaesite, cmmmech:vandenbrandeite, cmmmech:variscite, cmmmech:vaterite, cmmmech:veatchite, cmmmech:violarite, cmmmech:vivianite, cmmmech:voltaite, cmmmech:weddellite, cmmmech:weeksite, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:whitlockite, cmmmech:willemite, cmmmech:wollastonite, cmmmech:woodhouseite, cmmmech:wulfenite, cmmmech:wurtzite, cmmmech:xenotime-gd, cmmmech:xenotime-y, cmmmech:xenotime-yb, cmmmech:yanomamite, cmmmech:yusupovite, cmmmech:zeunerite, cmmmech:zincite, cmmmech:zincobriartite, cmmmech:zippeite, cmmmech:zircon, cmmmech:zirconolite.

All 365 mineral species records pass LinkML validation, carry IMA-compliant descriptions and source citations, and have verified curation histories.

### Structured IMA:YYYY-NNN identifier completeness on mineral records citing IMA species numbers

identity: concern. Targets: cmmmech:alburnite, cmmmech:briartite, cmmmech:cavansite, cmmmech:compreignacite, cmmmech:falottaite, cmmmech:greigite, cmmmech:katsarosite, cmmmech:lindbergite, cmmmech:metavivianite, cmmmech:moolooite, cmmmech:pentagonite, cmmmech:pertlikite, cmmmech:regerite, cmmmech:schwertmannite, cmmmech:struvite-k, cmmmech:wheatleyite, cmmmech:zincobriartite.

17 mineral records state their approved IMA-CNMNC species number (IMA YYYY-NNN) in prose description and cite ima_2026_09 in sources, yet omit the structured IMA:YYYY-NNN identifier entry in identifiers.

## Findings

### cmmmech-stage4-finding-0001: 17 mineral records state IMA-CNMNC species numbers in description but omit structured IMA:YYYY-NNN entries in identifiers

minor / open / confirmed; issue key: cmmmech.mineral.missing-ima-identifiers-on-cited-species.

Across the 365 mineral records, 43 records include a structured IMA:YYYY-NNN identifier in identifiers, whereas 17 mineral records explicitly state their IMA-CNMNC species number in description and cite ima_2026_09 in sources without a structured identifiers entry: alburnite (IMA:2012-073), briartite (IMA:1965-018), cavansite (IMA:1967-019), compreignacite (IMA:1964-026), falottaite (IMA:2013-044), greigite (IMA:1963-007), katsarosite (IMA:2020-014), lindbergite (IMA:2003-029), metavivianite (IMA:1973-049), moolooite (IMA:1980-082), pentagonite (IMA:1971-039), pertlikite (IMA:2005-055), regerite (IMA:2023-028), schwertmannite (IMA:1990-006), struvite-k (IMA:2003-048), wheatleyite (IMA:1984-040), and zincobriartite (IMA:2015-094).

## Recommended Actions And Acceptance Checks

### action-add-ima-identifiers-to-17-minerals

Add structured identifiers entries ({id: IMA:YYYY-NNN, label: &lt;Mineral Name&gt;}) and EDIT history sidecars to all 17 mineral records during Stage 5 grouped remediation.

- All 17 mineral records contain their exact IMA:YYYY-NNN identifier and canonical mineral label under identifiers.
- Each edited record has a matching EDIT sidecar in history/records/&lt;slug&gt;/ and passes cmmmech validate --require-records and cmmmech validate-history --base main.

## Category Boundaries

- retain: cmmmech:acanthite, cmmmech:adamsite-y, cmmmech:akaganeite, cmmmech:alabandite, cmmmech:albite, cmmmech:alburnite, cmmmech:alicewilsonite-yce, cmmmech:alicewilsonite-yla, cmmmech:alunite, cmmmech:amblygonite, cmmmech:ameghinite, cmmmech:ammonioborite, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:ancylite-ce, cmmmech:andersonite, cmmmech:anglesite, cmmmech:anhydrite, cmmmech:anilite, cmmmech:annabergite, cmmmech:anorthite, cmmmech:aragonite, cmmmech:argentojarosite, cmmmech:argyrodite, cmmmech:aristarainite, cmmmech:arsenopyrite, cmmmech:artinite, cmmmech:asbolane, cmmmech:atacamite, cmmmech:autunite, cmmmech:azurite, cmmmech:baddeleyite, cmmmech:bainbridgeite-ndce, cmmmech:bainbridgeite-yce, cmmmech:baricite, cmmmech:bassanite, cmmmech:becquerelite, cmmmech:beudantite, cmmmech:billietite, cmmmech:birnessite, cmmmech:bismuthinite, cmmmech:bixbyite-mn, cmmmech:bobierrite, cmmmech:boehmite, cmmmech:boltwoodite, cmmmech:boracite, cmmmech:borax, cmmmech:bornite, cmmmech:briartite, cmmmech:brochantite, cmmmech:brookite, cmmmech:brucite, cmmmech:brushite, cmmmech:burbankite, cmmmech:cadmoindite, cmmmech:calcioancylite-la, cmmmech:calcioburbankite, cmmmech:calcioveatchite, cmmmech:calcite, cmmmech:carnotite, cmmmech:carrollite, cmmmech:cassiterite, cmmmech:catapleiite, cmmmech:cattiite, cmmmech:cavansite, cmmmech:caysichite-y, cmmmech:celestine, cmmmech:cerianite-ce, cmmmech:cerussite, cmmmech:chalcocite, cmmmech:chalcopyrite, cmmmech:chernikovite, cmmmech:childrenite, cmmmech:chlorapatite, cmmmech:chromite, cmmmech:chrysotile, cmmmech:chukanovite, cmmmech:churchite-y, cmmmech:cinnabar, cmmmech:cobaltite, cmmmech:coffinite, cmmmech:colemanite, cmmmech:compreignacite, cmmmech:coquimbite, cmmmech:cordylite-ce, cmmmech:corkite, cmmmech:covellite, cmmmech:crandallite, cmmmech:cryptomelane, cmmmech:cuprite, cmmmech:cuprosklodowskite, cmmmech:curite, cmmmech:digenite, cmmmech:diopside, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dolomite, cmmmech:donnayite-y, cmmmech:dypingite, cmmmech:dzhalindite, cmmmech:elpidite, cmmmech:enstatite, cmmmech:eosphorite, cmmmech:erythrite, cmmmech:ezcurrite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:felsobanyaite, cmmmech:feroxyhyte, cmmmech:ferricopiapite, cmmmech:ferrihydrite, cmmmech:ferrokesterite, cmmmech:florencite-ce, cmmmech:florencite-la, cmmmech:fluorapatite, cmmmech:fluorite, cmmmech:forsterite, cmmmech:fritzscheite, cmmmech:galena, cmmmech:germanite, cmmmech:gersdorffite, cmmmech:gibbsite, cmmmech:ginorite, cmmmech:glushinskite, cmmmech:goethite, cmmmech:goldmanite, cmmmech:gorceixite, cmmmech:gowerite, cmmmech:goyazite, cmmmech:greenockite, cmmmech:greigite, cmmmech:gypsum, cmmmech:gysinite-nd, cmmmech:hafnon, cmmmech:hannayite, cmmmech:haradaite, cmmmech:hauerite, cmmmech:hausmannite, cmmmech:hawleyite, cmmmech:hazenite, cmmmech:heazlewoodite, cmmmech:hematite, cmmmech:hemimorphite, cmmmech:heterogenite, cmmmech:heterosite, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:huntite, cmmmech:hureaulite, cmmmech:hydroboracite, cmmmech:hydrocerussite, cmmmech:hydromagnesite, cmmmech:hydroniumjarosite, cmmmech:hydrotalcite, cmmmech:hydroxylapatite, cmmmech:hydrozincite, cmmmech:ilmenite, cmmmech:inderborite, cmmmech:inderite, cmmmech:indite, cmmmech:inyoite, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaliborite, cmmmech:kaolinite, cmmmech:katsarosite, cmmmech:kernite, cmmmech:kesterite, cmmmech:kornelite, cmmmech:kozoite-la, cmmmech:kozoite-nd, cmmmech:kukharenkoite-ce, cmmmech:kuliokite-y, cmmmech:kurnakovite, cmmmech:kutnohorite, cmmmech:laforetite, cmmmech:lansfordite, cmmmech:lanthanite-ce, cmmmech:lanthanite-la, cmmmech:lanthanite-nd, cmmmech:larderellite, cmmmech:laueite, cmmmech:lepidocrocite, cmmmech:libethenite, cmmmech:lindbergite, cmmmech:lithiophilite, cmmmech:lizardite, cmmmech:loellingite, cmmmech:lorenzenite, cmmmech:ludlamite, cmmmech:mackinawite, cmmmech:maghemite, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganite, cmmmech:marcasite, cmmmech:mcallisterite, cmmmech:mckelveyite-y, cmmmech:melanterite, cmmmech:meta-ankoleite, cmmmech:metacinnabar, cmmmech:metaschoepite, cmmmech:metastudtite, cmmmech:metatorbernite, cmmmech:metatyuyamunite, cmmmech:metavivianite, cmmmech:metazeunerite, cmmmech:meyerhofferite, cmmmech:microcline, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:monazite-ce, cmmmech:monazite-gd, cmmmech:monazite-la, cmmmech:monazite-nd, cmmmech:monazite-sm, cmmmech:monetite, cmmmech:monohydrocalcite, cmmmech:montebrasite, cmmmech:montmorillonite, cmmmech:montroseite, cmmmech:moolooite, cmmmech:muscovite, cmmmech:natroboltwoodite, cmmmech:natrojarosite, cmmmech:navajoite, cmmmech:nepheline, cmmmech:nesquehonite, cmmmech:newberyite, cmmmech:ningyoite, cmmmech:nobleite, cmmmech:nontronite, cmmmech:orpiment, cmmmech:orthoclase, cmmmech:otavite, cmmmech:palygorskite, cmmmech:paracoquimbite, cmmmech:paramontroseite, cmmmech:parasymplesite, cmmmech:parauranophane, cmmmech:pascoite, cmmmech:pentagonite, cmmmech:pentlandite, cmmmech:perovskite, cmmmech:pertlikite, cmmmech:petalite, cmmmech:petrukite, cmmmech:phlogopite, cmmmech:phosphoferrite, cmmmech:phosphophyllite, cmmmech:piilonenite-nd, cmmmech:pinnoite, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:polylithionite, cmmmech:powellite, cmmmech:preobrazhenskite, cmmmech:priceite, cmmmech:probertite, cmmmech:pyrite, cmmmech:pyroaurite, cmmmech:pyrochroite, cmmmech:pyrolusite, cmmmech:pyromorphite, cmmmech:pyrrhotite, cmmmech:quenstedtite, cmmmech:ramsdellite, cmmmech:realgar, cmmmech:regerite, cmmmech:renierite, cmmmech:rhabdophane-ce, cmmmech:rhabdophane-la, cmmmech:rhodochrosite, cmmmech:rhomboclase, cmmmech:richetite, cmmmech:riebeckite, cmmmech:rivadavite, cmmmech:romanechite, cmmmech:roquesite, cmmmech:roscoelite, cmmmech:rozenite, cmmmech:rutherfordine, cmmmech:rutile, cmmmech:sabugalite, cmmmech:sakuraiite, cmmmech:saleeite, cmmmech:saponite, cmmmech:sauconite, cmmmech:scheelite, cmmmech:schertelite, cmmmech:schoepite, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:senarmontite, cmmmech:sepiolite, cmmmech:siderite, cmmmech:simonkolleite, cmmmech:sklodowskite, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:soddyite, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:stevensite, cmmmech:stibnite, cmmmech:stolzite, cmmmech:strengite, cmmmech:strontianite, cmmmech:struvite, cmmmech:struvite-k, cmmmech:studtite, cmmmech:sulfoborite, cmmmech:svanbergite, cmmmech:switzerite, cmmmech:synchysite-ce, cmmmech:szaibelyite, cmmmech:szomolnokite, cmmmech:talc, cmmmech:tennantite-in, cmmmech:tenorite, cmmmech:thomasclarkite-y, cmmmech:tincalconite, cmmmech:titanite, cmmmech:todorokite, cmmmech:torbernite, cmmmech:triphylite, cmmmech:troilite, cmmmech:tunellite, cmmmech:ulexite, cmmmech:uramphite, cmmmech:uraninite, cmmmech:uranophane, cmmmech:uranopilite, cmmmech:vaesite, cmmmech:vandenbrandeite, cmmmech:variscite, cmmmech:vaterite, cmmmech:veatchite, cmmmech:violarite, cmmmech:vivianite, cmmmech:voltaite, cmmmech:weddellite, cmmmech:weeksite, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:whitlockite, cmmmech:willemite, cmmmech:wollastonite, cmmmech:woodhouseite, cmmmech:wulfenite, cmmmech:wurtzite, cmmmech:xenotime-gd, cmmmech:xenotime-y, cmmmech:xenotime-yb, cmmmech:yanomamite, cmmmech:yusupovite, cmmmech:zeunerite, cmmmech:zincite, cmmmech:zincobriartite, cmmmech:zippeite, cmmmech:zircon, cmmmech:zirconolite. All 365 records in the mineral cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'mineral' at 4d878383c92b44876df3bf166d96637c7581a59e with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cmmmech-validate | src/cmmmech/validation.py; cmmmech validate --require-records | supports | LinkML structural and semantic validator passed across all 616 records (including the mineral cohort) with 0 errors. |
| ev-cmmmech-history | src/cmmmech/history.py; cmmmech validate-history --base main | supports | All 810 curation history sidecars in history/records/ and record history_refs passed validation with 0 errors. |
| ev-cohort-audit | src/cmmmech/schema/cmmmech.yaml; Stage 4 full-inventory cohort audit (mineral) at 4d878383c92b44876df3bf166d96637c7581a59e | supports | Full-inventory inspection of all records in the mineral cohort verified distinct material identities, source-backed criticality/mechanism claims, and 100% CURIE label consistency across 270 distinct ontology terms. |
| ev-ima-missing-identifiers | data/records/alburnite.yaml; 17 mineral records with IMA numbers in description and ima_2026_09 in sources but no IMA:* entry in identifiers | partial | 17 mineral records (alburnite, briartite, cavansite, compreignacite, falottaite, greigite, katsarosite, lindbergite, metavivianite, moolooite, pentagonite, pertlikite, regerite, schwertmannite, struvite-k, wheatleyite, zincobriartite) state their approved IMA-CNMNC species numbers in description and cite ima_2026_09 in sources, but omit the structured IMA:YYYY-NNN entry in identifiers used by the other 43 IMA-numbered mineral records. |

## Limits And Additional Notes

- 17 mineral records omit structured IMA:YYYY-NNN entries in identifiers despite stating those IMA numbers in description (tracked as open finding cmmmech-stage4-finding-0001 for Stage 5 remediation); cmmmech:wulfenite omits ima_2026_09 from sources (tracked as open finding cmmmech-stage4-finding-0002 in companion review 20261022T025807Z-wulfenite-stage4-record-review).
- Stage 3 added verified UniProtKB protein examples to 6 mineral records: bixbyite-mn (UniProtKB:A0A0K2YWP2, UniProtKB:L0KKS2), dittmarite (UniProtKB:G3Y4N5), glushinskite (UniProtKB:G3Y4N5), montmorillonite (UniProtKB:Q8E8S0, UniProtKB:Q8EG34, UniProtKB:Q8EG33), nontronite (UniProtKB:Q8E8S0, UniProtKB:Q8EG34, UniProtKB:Q8EG33), and struvite (UniProtKB:G3Y4N5); all 6 passed full Stage 4 verification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025801Z-stage4-mineral-cohort-review
title: 'Stage 4 full-cohort review: mineral records (365/365)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-22T02:45:00Z'
finished_at: '2026-10-22T02:58:01Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 365 mineral records in data/records/*.yaml at commit 4d878383c92b44876df3bf166d96637c7581a59e.
  All 365 mineral records carry valid mineral descriptions and source provenance;
  269/365 mineral records carry mechanisms (157/365 with microbial: true mechanisms)
  and 29/365 carry grounded multi-step causal_graphs with UniProtKB protein_examples.
  Recorded one cohort-level minor completeness finding (cmmmech-stage4-finding-0001)
  across 17 mineral records that state their IMA-CNMNC species number in description
  and cite ima_2026_09 but omit the structured IMA:YYYY-NNN entry from identifiers
  (and see companion single-record review 20261022T025807Z-wulfenite-stage4-record-review
  for cmmmech-stage4-finding-0002 on cmmmech:wulfenite).'
reviewer:
  identity: antigravity / cmmmech-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Stage 4 record_review (.claude/skills/review-yaml-category/SKILL.md)
    against frozen commit 4d878383c92b44876df3bf166d96637c7581a59e.
source:
  git_revision: 4d878383c92b44876df3bf166d96637c7581a59e
  state: git_commit
  inputs:
  - path: data/records/acanthite.yaml
    sha256: dab8e5acec7c1178d06afa237a8ece75e41a28c475fab88c2aa79640925738af
    role: target
  - path: data/records/adamsite-y.yaml
    sha256: 84462864eed7c413c8f8e1760866442f9df1d221d64f5e6a84a761bfa3863884
    role: target
  - path: data/records/akaganeite.yaml
    sha256: 7a5214f7def425bbbaf9d0bf440307d817a240e0fd4efe233ae4ca24a4c6c70e
    role: target
  - path: data/records/alabandite.yaml
    sha256: 085e54b5b6e7e0f58544fde77d4ba0b55f3c6a8b13fccecc8efb6875530dfcee
    role: target
  - path: data/records/albite.yaml
    sha256: a6dda95dcb942312950b584f345a606d364bfceb0f3c0c9ba47e92230f38b677
    role: target
  - path: data/records/alburnite.yaml
    sha256: bb980057adbe887790f25c5a357824179470eba8ca1ae21caab24473c7d50c1a
    role: target
  - path: data/records/alicewilsonite-yce.yaml
    sha256: 32da51cf9109f74a8eb40c15162279992015977a5edf41047eb5eac8f379182b
    role: target
  - path: data/records/alicewilsonite-yla.yaml
    sha256: 23c7c787cc66e77bff11f488f2a35edb493ca700da0e70e6d094add2c62df8b6
    role: target
  - path: data/records/alunite.yaml
    sha256: 01229aba97fb91d213e43667a0ffd04db50d3bc235a80d83589bc154b6d88aa3
    role: target
  - path: data/records/amblygonite.yaml
    sha256: 1c8dc040e76a80d47dc7cec0f1d5f8aa56e3b7106492f674f6bb3b6183fbe807
    role: target
  - path: data/records/ameghinite.yaml
    sha256: 81badc1928754cd19bbc883adb8903895e16522f0ef7ae75f14812b3f04d8b13
    role: target
  - path: data/records/ammonioborite.yaml
    sha256: 679150872fd49c31398f5bd6daa6e0d378d96e0a734a0c641f1147d182a25352
    role: target
  - path: data/records/ammoniojarosite.yaml
    sha256: 97a4c9e3c839ab5d79e335bf4b037471083cfb913350f8a19fe1f9cb36c3ec6a
    role: target
  - path: data/records/anatase.yaml
    sha256: e6458835c3c5a41c4613ebe519662b54d1cf77ff5a3a0ebd704f61af5ce958ca
    role: target
  - path: data/records/ancylite-ce.yaml
    sha256: f7becbbf81059edbf12d30c49ffb92fb59da18ea17296b20ba503d4348d35a49
    role: target
  - path: data/records/andersonite.yaml
    sha256: 0e416b7232fac6ca28da0758415dbcec38e0914d739a7a3bf4ef1160e39fbc8f
    role: target
  - path: data/records/anglesite.yaml
    sha256: 5bc650c2efb91ffc664d20a8c3b6967b88e7959ebcc0cd6a19837f201d5d2303
    role: target
  - path: data/records/anhydrite.yaml
    sha256: d5b37f08bac5bbcc572461dd8a47395fa5990dd84c9e4b80a5faca3ca0c06e19
    role: target
  - path: data/records/anilite.yaml
    sha256: 97f8f8eb0d55379bfcb9815ca4ea72ea9cbc71b3fbae79f2a951f2ae92f33d50
    role: target
  - path: data/records/annabergite.yaml
    sha256: 0177cd61954d97183a3175e393054d33e2114866fd7b341627717e3c8eea1f6a
    role: target
  - path: data/records/anorthite.yaml
    sha256: c57652ca99fa8992f167f1a5081c5feb09287aa4a03fb776744d5b8b95b4fdbe
    role: target
  - path: data/records/aragonite.yaml
    sha256: bf984de0c66475279d0fe5f75e450a59e4267955b8c399575cd000a4559f541a
    role: target
  - path: data/records/argentojarosite.yaml
    sha256: a4b23b761cf06818088fedb710fdf89d9e34da80265149a80a722a999a51d27c
    role: target
  - path: data/records/argyrodite.yaml
    sha256: 7944de7d27f422ff2778c454e466b0c6397367b1af4efcfb7a3a227e886d7190
    role: target
  - path: data/records/aristarainite.yaml
    sha256: 474975ff1deb3706bdc6f6feb1d6a267cda7cf34dfdc3df7a0f956bcf1abb057
    role: target
  - path: data/records/arsenopyrite.yaml
    sha256: c5964569b34c3bb772113634b0dde144d6f79849a36f076c7d3effb8083ccc4d
    role: target
  - path: data/records/artinite.yaml
    sha256: 54de7013ba0cef8aa1976fa8bb5e9ddcbc7979bff33c6db137e20d02223235c4
    role: target
  - path: data/records/asbolane.yaml
    sha256: fc303916b2a7c64bfb657a7fc73f75e9db2146ac1ad4d2476024a5455fb56594
    role: target
  - path: data/records/atacamite.yaml
    sha256: e83e61c3b7769c54b83a12da7870acd84ffc1b433d09e49f0605324cc8540702
    role: target
  - path: data/records/autunite.yaml
    sha256: 51632221cbd54db94cdd7295abf5218a4ed3838de1b9e8f50f92846845cf55ce
    role: target
  - path: data/records/azurite.yaml
    sha256: 10f41fc69980d6adc1213e715fafa37d08a4eacf6f4d917c8ede804b2a20261f
    role: target
  - path: data/records/baddeleyite.yaml
    sha256: 3aa47a953cda6634ef1e4e874a4fd5395e5245340c87d434ea0a52eaeb77f81e
    role: target
  - path: data/records/bainbridgeite-ndce.yaml
    sha256: 1d66ccdadabb1cb4eaadc2849cbeb422b2a07a1290d2073714a36b7e392ca08c
    role: target
  - path: data/records/bainbridgeite-yce.yaml
    sha256: ff8a8bc1cb5f180d599138784ec50cfa725f80ef833e4266be6a0387616185fa
    role: target
  - path: data/records/baricite.yaml
    sha256: 8d0b77267485c73ab254b440c3f32c4322bd1d8dd46c48d212c316ef2eebe7ed
    role: target
  - path: data/records/bassanite.yaml
    sha256: 014fbfc5c3711dfc6b82edd424aa388ecaf21c82a821ecea9bbb411393827919
    role: target
  - path: data/records/becquerelite.yaml
    sha256: 7cb3bfb70ceb19783ec96f29b1a64bd489010e0fb0b5d8aa29d56f48a8acdd04
    role: target
  - path: data/records/beudantite.yaml
    sha256: cc2ccaf3c1efd7c88e2b14a576de3f2c5450f55cebd3be239f099896e917f368
    role: target
  - path: data/records/billietite.yaml
    sha256: 29f1a2b6d7f98fc1c8a601725bc5d7bf0153ece58f91d1989c6823a175b05ca2
    role: target
  - path: data/records/birnessite.yaml
    sha256: 68f1ff968be471ba2095191414df2e51608002b5d34285dadde2814825ac65f4
    role: target
  - path: data/records/bismuthinite.yaml
    sha256: 567c1abcbc04a747fed8961e7b00dcf98c7708530b8703f2d0fca9a03386e3c6
    role: target
  - path: data/records/bixbyite-mn.yaml
    sha256: c8f7fcc10cb5a1d6b7965e1441a075c6be889de9eeaea7c271973def6459a797
    role: target
  - path: data/records/bobierrite.yaml
    sha256: 593352892fe231fe888b0282b2068cd673a545be0a63ca02bd80f5a9ea84e53d
    role: target
  - path: data/records/boehmite.yaml
    sha256: e31bc47bd90bd013882ab16837dd2850321b2549b89dafd0549a8e09d030d876
    role: target
  - path: data/records/boltwoodite.yaml
    sha256: eb8934a9cd33839c5b2b6fc65993c35643c637e9da731b5fe9790aee83258e9c
    role: target
  - path: data/records/boracite.yaml
    sha256: 07246fc293a22a34791f882a00b87bd16a351494fadaa20f421db9869b55f9c9
    role: target
  - path: data/records/borax.yaml
    sha256: 2c369db87f4ddbd873bf31e916d71d2b55dd02259133ee9432077886dd09e761
    role: target
  - path: data/records/bornite.yaml
    sha256: 85a23954d070772bf059c74b7cabf10fe20c6131220abd99cef8b900fbebd261
    role: target
  - path: data/records/briartite.yaml
    sha256: 78d179ae37d35050510f0083df0936bee843ff76eab448bef817c12198ed6d51
    role: target
  - path: data/records/brochantite.yaml
    sha256: 573f6296c98db20c52cbec328d8b5ed68963538ad971888cc2d1816941cde1c6
    role: target
  - path: data/records/brookite.yaml
    sha256: 39978526ff9e4fe8233cbcbb6c2dc2e8d73b994054cac0b4d109cabc6bf6fd98
    role: target
  - path: data/records/brucite.yaml
    sha256: 11095b47730de3b30212460c07c363b28df0000b4400252957a397b9d8cc5bc0
    role: target
  - path: data/records/brushite.yaml
    sha256: 5fa1540a07d369151fcb28abea980998c964745f3bbd5f2ee7fa6ef0c2400f8c
    role: target
  - path: data/records/burbankite.yaml
    sha256: bc9d3e107c34a5917e9a0b82d610ef6e7785d9fcdcdf4b6c4ed58365a4fb64bb
    role: target
  - path: data/records/cadmoindite.yaml
    sha256: f3dc91cb1957b209952b2fe7f24f05350a2dc42b421c71780dd7a8d40c895278
    role: target
  - path: data/records/calcioancylite-la.yaml
    sha256: 4e38624848b4fc7fca0606c686eb5938c744ffe6c9cd8d6f38dcee53dac9640e
    role: target
  - path: data/records/calcioburbankite.yaml
    sha256: e41e5efe60e6265844e726ce8a8f8e2efc56f1bcd663440fc961fe7be37244c9
    role: target
  - path: data/records/calcioveatchite.yaml
    sha256: 124baa6951a2fcb650fa2a3df2c5eedfe89001ac73c9b8586767cdb7e4848839
    role: target
  - path: data/records/calcite.yaml
    sha256: 8c1378d02bf991926c80747de98d6db4caed0248fd105c70832cbd1d60964b7f
    role: target
  - path: data/records/carnotite.yaml
    sha256: 63d935bfde97c442f21101619bd396989a58ec16b49f51920beeccadcfd564ac
    role: target
  - path: data/records/carrollite.yaml
    sha256: f462c9dd2d309a384f4feb93a064202c026cf00d646568338aa04cef3347185d
    role: target
  - path: data/records/cassiterite.yaml
    sha256: 86599254ca6d4f507061c3ba8f1b6d36507824f7812d7b22067e69daeedbfd63
    role: target
  - path: data/records/catapleiite.yaml
    sha256: 35b40ba6a6329736254e413555c2d9195a821dc5d785742b4d2fa4bd4d0a69b0
    role: target
  - path: data/records/cattiite.yaml
    sha256: 648ab708415663b96a90a13148ee98f15df3a1737f2e26f394c4e84ed4870ca5
    role: target
  - path: data/records/cavansite.yaml
    sha256: cbc621cb0efdc4a9513599669d415c367f65e2e04a71087f9249df4eca771614
    role: target
  - path: data/records/caysichite-y.yaml
    sha256: 670cb1e856621fd999cab59001a7d7c129f8ba82a7cc039d1ff167ce296f20ad
    role: target
  - path: data/records/celestine.yaml
    sha256: 3c07da892ba97f7eff25b90eeada40cc55174eacf8e93831bfe8b429c39585a3
    role: target
  - path: data/records/cerianite-ce.yaml
    sha256: 94b904083cfa29367512be8795474bc670c817032a059a9eca472935b2ebe052
    role: target
  - path: data/records/cerussite.yaml
    sha256: b590131335b71b6d5ad7b9c2fbb34b0df63dce2f45e14c6f57e1d5d69bbf5b1a
    role: target
  - path: data/records/chalcocite.yaml
    sha256: 1b6d4f56c629f2c029f8856734aee1317744f90b468891c27103d40c2496fc0e
    role: target
  - path: data/records/chalcopyrite.yaml
    sha256: 33feadacbc2b3a2a309c2165419f4af6bdded7c902a45dec55cc2312bed10ec0
    role: target
  - path: data/records/chernikovite.yaml
    sha256: 0d213c86c8df4d665d8c70a3b9e180101f972c9856add64c4c84766a778d1bca
    role: target
  - path: data/records/childrenite.yaml
    sha256: 5398994e55c1a46069ecc850c9caf820daacab5e232b49e7660761e1ba5312c3
    role: target
  - path: data/records/chlorapatite.yaml
    sha256: a761730c01b7ea09b9dec4371a04948209a47f6b049ec2f3c07dcaf5f100f48c
    role: target
  - path: data/records/chromite.yaml
    sha256: 23fcf34515df26468045f4fe7ce56001be293f89da2dc02b45a0bceb11923898
    role: target
  - path: data/records/chrysotile.yaml
    sha256: a4e8e0dfcb054ce8bd0492938bc24c9383f64f9eea87574bf8f899fb1c3d5b19
    role: target
  - path: data/records/chukanovite.yaml
    sha256: b059253484c225c0bccf994da3025bb226c61c55a26b3388a294938c3da0e299
    role: target
  - path: data/records/churchite-y.yaml
    sha256: ee661848a3792061d51c715c74a2f749b36a22831612bd617f44f2db64934384
    role: target
  - path: data/records/cinnabar.yaml
    sha256: 9c85bcd4302594920ff22b9d08263ee5368bd5467cca930089287377e5404e3d
    role: target
  - path: data/records/cobaltite.yaml
    sha256: f19fa6105e65527f70525b08c5064a53d85e72cd8dd3823835d635babdb562d5
    role: target
  - path: data/records/coffinite.yaml
    sha256: 87fce590c46f36cf970ce3cc1c74d1a93e141fbec4bd91c3d738202f8b8b5496
    role: target
  - path: data/records/colemanite.yaml
    sha256: 969cb2b8d3a07ccc1241382de450dd0d10f77c25e1dc434c21a5a1aacba51096
    role: target
  - path: data/records/compreignacite.yaml
    sha256: 3ccd63f4af9951a0950c4be3dc7f899773e15d1c75be1d314c324e651185d9ef
    role: target
  - path: data/records/coquimbite.yaml
    sha256: 6af5c6bfe863f716aa767b8b6182d3a9d025b5033fb9d5bf62f5f7e56f8c3176
    role: target
  - path: data/records/cordylite-ce.yaml
    sha256: 4bc7a2b0c356b084d9bdac2c4c1b03c97fb9a303e6b7d1698d548376acad003b
    role: target
  - path: data/records/corkite.yaml
    sha256: 6ac28cbe83b7eb4fbdedb43df6e260d0d7882e7672b60899136b996d6b025326
    role: target
  - path: data/records/covellite.yaml
    sha256: 090a48e7e40c145d9daef4b9ca4c4be5e74e5e454c6f0862c3c0548c5b9c222a
    role: target
  - path: data/records/crandallite.yaml
    sha256: 6def97bfbfa950644ae9a0f39e551df1830a4f1fd06b5dae08b4af412bcb772f
    role: target
  - path: data/records/cryptomelane.yaml
    sha256: 8f3ceff3c9ac3b8f9d08cb0168e1d57d9a92ed03e13957b50c803e91296a6131
    role: target
  - path: data/records/cuprite.yaml
    sha256: 50e1f9c41d03596639a3ba16b23dd5e3a6f457bfa10fd7db78ff5ad6d5c8dc18
    role: target
  - path: data/records/cuprosklodowskite.yaml
    sha256: dff1fe6924c4e99765ee8a433dc4e63a64f5bae8e65fc4ade4f0976ad99db3a6
    role: target
  - path: data/records/curite.yaml
    sha256: 80065e1804a54175e496d51df415867bb645f5f000d70a486738f07fe767e3d8
    role: target
  - path: data/records/digenite.yaml
    sha256: ebee546a23140d37fd3081c6b9f3303a2188df080c2e0192e53e0228aa217a30
    role: target
  - path: data/records/diopside.yaml
    sha256: 79084fd1d89a69e71c0efee76a6b961354ea9ca3f6ecbb235ba7068a07c72734
    role: target
  - path: data/records/dittmarite.yaml
    sha256: c12b265e41c26f370f23729e76c74dfe86a8e574889cdb7f7ae2ceff5eb44fd5
    role: target
  - path: data/records/djurleite.yaml
    sha256: 5535b966be63e1c98e20698f9eb4615f1917d3db7159276fbfb158ad3c81101f
    role: target
  - path: data/records/dolomite.yaml
    sha256: b3e67d9b6f08bd30e658cb05a566818a21b9f81530dc3ec9672db2ea91b8a29c
    role: target
  - path: data/records/donnayite-y.yaml
    sha256: 2349ecf97cff4c80330e2b6a4a30436b5a3656e4525ebbc47c7ace48fbc64216
    role: target
  - path: data/records/dypingite.yaml
    sha256: dda0701dc49edb424e05e386bc8bfcd7859e9999b1c376949272c9e6979907c3
    role: target
  - path: data/records/dzhalindite.yaml
    sha256: 60435e2806654a3150427a07c17adb27c1b0fac18684dd9354ba939b43a560ee
    role: target
  - path: data/records/elpidite.yaml
    sha256: d4380b722d62b9e66de5be913d7629dce70780fff4e55ec47147eb96ed9baf3e
    role: target
  - path: data/records/enstatite.yaml
    sha256: 5af1b751e9b6ff378f70a487f29e8d6c8616101b7b7ec41dd659d4dc93a50ce1
    role: target
  - path: data/records/eosphorite.yaml
    sha256: 34b8e2dd6b45092f8ae92161ca6ccd0455c03735585aaedbbae63854c3ed60cd
    role: target
  - path: data/records/erythrite.yaml
    sha256: addb9e69d684875a572c83115fd41df109364b05fd2b01b00b9df4917161d7d0
    role: target
  - path: data/records/ezcurrite.yaml
    sha256: 030d08aaefce724438a5bdc3953faa0ac04b05ed87fff0d6d93cf5fe59a48229
    role: target
  - path: data/records/falottaite.yaml
    sha256: 09ce8e56f4e726815a1603a426745d042773517827b79824c6df3e0448e7b35c
    role: target
  - path: data/records/feitknechtite.yaml
    sha256: a3112a6a8266a718abf3c794a2de3ccf8c084d0eb67afc6ad21eda47c8133dbc
    role: target
  - path: data/records/felsobanyaite.yaml
    sha256: 00c42bd80ce395e4a1e2253c8023a52cf3ad086fbb2f8700b50f13bc861c2ef9
    role: target
  - path: data/records/feroxyhyte.yaml
    sha256: 6d33c03a73ed8b43201efd8608536cf213bf5625af78b85d0326fb0342fc4c61
    role: target
  - path: data/records/ferricopiapite.yaml
    sha256: df34f6122b7f9df480fdc8a083a202702c560a7e32f735f3e114e7a2732c105e
    role: target
  - path: data/records/ferrihydrite.yaml
    sha256: 2de9e5fdbd96b7d9ec8b74c7b09ffd04951e1351288c88a37872fd4a0c22791c
    role: target
  - path: data/records/ferrokesterite.yaml
    sha256: 6437798cc26e2fa214de18dd4d90115dd9ae16a5536ffa5a0fa2f6b8ac35797a
    role: target
  - path: data/records/florencite-ce.yaml
    sha256: 8066102bee484b602066b8ad4903aab8dc8ce15cbe31a1285e2ab7c687f27a4b
    role: target
  - path: data/records/florencite-la.yaml
    sha256: 7a391c97383d69fbdd9b7507fb6441fab03b432c689a6ab8773a5ef75b72c3e1
    role: target
  - path: data/records/fluorapatite.yaml
    sha256: d383f2740dfdfbce3edcd003507e5de63cf3076819aec7d860a58fd82ce70bab
    role: target
  - path: data/records/fluorite.yaml
    sha256: 5c4e6129dd9b54b5236ea6baa7bf306b4dec037fb69a3b96d03d113dadbe5f6e
    role: target
  - path: data/records/forsterite.yaml
    sha256: fe9d20cf24f94fa19731b0a864e00cd5c199ae807ecbe346e8239d52133cd30c
    role: target
  - path: data/records/fritzscheite.yaml
    sha256: 1c3776fd9d274df4d5a99f0d0376ae5666b7d571444dc1c9df129f51d32ed85c
    role: target
  - path: data/records/galena.yaml
    sha256: b852030fb39e070936bab937991ef590d116307856ab532b7e6f31a330bdf78d
    role: target
  - path: data/records/germanite.yaml
    sha256: 7a15d724ccb45945471b744657f8e43e00aec76a37d4a49d8ddb08a35a0fad14
    role: target
  - path: data/records/gersdorffite.yaml
    sha256: 72097c8cd9cced0ac3565e12c7babbc9493f248ee0cecc90c26d72e37c463fa4
    role: target
  - path: data/records/gibbsite.yaml
    sha256: 26913622b6ff36f836794270e33c06947c9adec8513ccc238b78075763cb52d8
    role: target
  - path: data/records/ginorite.yaml
    sha256: 5a0743b464547be195c45d27484093229d988ffdf9631103505a288d886e6bd0
    role: target
  - path: data/records/glushinskite.yaml
    sha256: 1d2ac15ed1c10a1f6a0bd3e4224440e99fc7e3b8e93e1114a3a90004870c925f
    role: target
  - path: data/records/goethite.yaml
    sha256: 9a10d095cedc9e0e5a25d33426c644072a04f194eee2fa35cacc8ad1e0da796c
    role: target
  - path: data/records/goldmanite.yaml
    sha256: 02ed7a5f86826088ea63dda56b5d401532164a211ddbf932d0135b414751d59f
    role: target
  - path: data/records/gorceixite.yaml
    sha256: 297b38be3c9dbdd4b70496e7b66df599894bd8cda4bf2e3606ca0f21ec215fb1
    role: target
  - path: data/records/gowerite.yaml
    sha256: dae34a6ab5c9242ae989775dc3f1ea4ba84a42789129e735032aba0d2691b051
    role: target
  - path: data/records/goyazite.yaml
    sha256: 84984750dea8e779674c5f4c6002e5d2f494a1d8d9c06594c283c019ab5812f5
    role: target
  - path: data/records/greenockite.yaml
    sha256: 84d912d22b329771ab89264b240e46042a972d56872a6a7fd8cfad771bd36370
    role: target
  - path: data/records/greigite.yaml
    sha256: ff4d81433f6a854621fa16213167ed62120b7aa73bc0e2dd684e76200c35a8e4
    role: target
  - path: data/records/gypsum.yaml
    sha256: ea54490afd8114c45393c403088a3605c1df429eb65052cdae9c3c25becc153b
    role: target
  - path: data/records/gysinite-nd.yaml
    sha256: 7baa06a84cd78e2dde9eb81f31dca9abd716d9390143197f2c30afc0a7a69b90
    role: target
  - path: data/records/hafnon.yaml
    sha256: 9aa7b20c09e4ba2fb2ad70bec39df64bde4cb7bceb6a9c13c8e0798ad78d80cd
    role: target
  - path: data/records/hannayite.yaml
    sha256: 6a05a0d42bdac6c6a1755ce130733fd9d64e8079471279526157c690159997a4
    role: target
  - path: data/records/haradaite.yaml
    sha256: 3254359adeb4d0e78c35d8afdb83819e54507341369451e71ee93df2108f0c06
    role: target
  - path: data/records/hauerite.yaml
    sha256: 25a867c83d764ce48c8895c14ff581eb241885693830e503f41bfebcce5133c9
    role: target
  - path: data/records/hausmannite.yaml
    sha256: 3f319c603aa92069f7c1e04c4c34e4bd11820b8697f1e3396eac26a3a01e5d3e
    role: target
  - path: data/records/hawleyite.yaml
    sha256: fadf767aea3e92bee1921a8edd05577d2d146dcc4bc83f02ee7a49088dc594a7
    role: target
  - path: data/records/hazenite.yaml
    sha256: 9a3c290f6675674f25a473d62b20f173e506e561e52e17e59ebd68bde1a09a54
    role: target
  - path: data/records/heazlewoodite.yaml
    sha256: edffc21a2b5750369280beb133ce91de9a8e99f71872062566ef265e538d610a
    role: target
  - path: data/records/hematite.yaml
    sha256: c677b20cd2ead19cf7bf8b1882cfd567f55ca38ffe0bfa7c7514cfc9143c4c49
    role: target
  - path: data/records/hemimorphite.yaml
    sha256: fabf318cead701c449049dedef9715848a57a95e0f8033cdc694f0fcf63e465b
    role: target
  - path: data/records/heterogenite.yaml
    sha256: 396c4fcc9519f1c324c5b141086979551db4ae21f48a281e839a114854658c9e
    role: target
  - path: data/records/heterosite.yaml
    sha256: 916efa4c559606a0ddaf4bf1a85519ba9ef66c8eae0f3c9e51657ee2a07fc95a
    role: target
  - path: data/records/hollandite.yaml
    sha256: 17f916c1157204fcc3492c6c1676f5942446ba135452c9182fae4b9c81f70712
    role: target
  - path: data/records/hopeite.yaml
    sha256: bc522d34581ca173e432c69d171b5419516c9e3b067ca73cc080b872d67bd4ab
    role: target
  - path: data/records/humboldtine.yaml
    sha256: 238bbbcb04aefae0970a112cbca04b136f0740b4980709ae9bb4b831546cfa31
    role: target
  - path: data/records/huntite.yaml
    sha256: f8e51059f40b68e74000fb2697a6f49e8bf4a40ea0c49d5f500376a21a9af7ac
    role: target
  - path: data/records/hureaulite.yaml
    sha256: 3da462e28671a908cea2f5c0d7f431579f93514e1215b0c05eba69aaf507b075
    role: target
  - path: data/records/hydroboracite.yaml
    sha256: db1e645ae3e36e7b9a77826fa9a6b1542f9a7603406dabef9cafac97d552b5a9
    role: target
  - path: data/records/hydrocerussite.yaml
    sha256: a4d376d672d254c5731f73cafaa70ee8ad40686e82c82c2f4c96453011ba24ec
    role: target
  - path: data/records/hydromagnesite.yaml
    sha256: 97de87c369fc037f3eb70587c1084a876d281c43d1770f8b0dfab9c67cc48748
    role: target
  - path: data/records/hydroniumjarosite.yaml
    sha256: 6949680434701222eaf04173b64632df6f675bbd6ccc59f60241087ef594fe3b
    role: target
  - path: data/records/hydrotalcite.yaml
    sha256: 385655f2ba36f964f3b8d4e67d321a68c5d1e3de361c4d185eae71b6c688dd00
    role: target
  - path: data/records/hydroxylapatite.yaml
    sha256: 103556e9bc6f205b72968ba080931fa074095bd00c137157bb4fe5323fdffb25
    role: target
  - path: data/records/hydrozincite.yaml
    sha256: f8844db2bfa5387f935c677474d10cd198a9eb2979cfac99d5bff79c0706443e
    role: target
  - path: data/records/ilmenite.yaml
    sha256: c066b7d14249f93229c678d0cabe2e171ffc4529a223e560dc750b2d362e5976
    role: target
  - path: data/records/inderborite.yaml
    sha256: bef43835c16fb0e48ec09359bdc38a4a52efb73c0f528857728d9932fa8feab4
    role: target
  - path: data/records/inderite.yaml
    sha256: 52fb3b1beb73ddaebaa4f23a3630e6760ca7f5adb4af18ef80ed1a9c9664a46e
    role: target
  - path: data/records/indite.yaml
    sha256: 2be7428bebe7fa0031dcf2c50e7b87c5f85e359ed9bc6f28b09ab05051eafa8c
    role: target
  - path: data/records/inyoite.yaml
    sha256: 4804dad05c88116db1ff401d6ff9bcf44f8066685e48a5c37c63cdc918d0c6bf
    role: target
  - path: data/records/jadarite.yaml
    sha256: 28960308edc989f465043734b680c9d9df4b2943193cbf600d295ae410dd5511
    role: target
  - path: data/records/jarosite.yaml
    sha256: 5642b5560b9d351f581fab9725486c440b4a3a0e6e4978c78478898e172b011b
    role: target
  - path: data/records/kaliborite.yaml
    sha256: af6e0e637e9745fec02c3f2bed17c30f150ba6b126085c0c2a622430ba684443
    role: target
  - path: data/records/kaolinite.yaml
    sha256: dd4561af884adcec68321d5a8241344715d372d3b359df6fed3e99f382a5b3b9
    role: target
  - path: data/records/katsarosite.yaml
    sha256: 5ef92fb7831dfc2d91f877b6e18a0c1f41128f431e5be94de633fa8b9e40059e
    role: target
  - path: data/records/kernite.yaml
    sha256: a9b4990d774166a5ab77f6a608e5e76249a9b9224ea98cfba412fe85a55e1843
    role: target
  - path: data/records/kesterite.yaml
    sha256: e88e436bd24f425997a56d26e819a99661c84c2e39ed82a0c963ba5520d83b6a
    role: target
  - path: data/records/kornelite.yaml
    sha256: e07c2e47d5c1737f02e2046ec5347584a7e2cc25df530044073dfc8073d78d5d
    role: target
  - path: data/records/kozoite-la.yaml
    sha256: 823779b67c334476a84665caf92ee47124b9d30fe9912639a128a70005c2cafc
    role: target
  - path: data/records/kozoite-nd.yaml
    sha256: 1464f598650208e0882b89dbcc7078acc20a308305d384d0d28da9bafa1471b2
    role: target
  - path: data/records/kukharenkoite-ce.yaml
    sha256: d2c22307d196948ac67a4549cbd538e7c74361fa3169781cfbd8d01eec17c033
    role: target
  - path: data/records/kuliokite-y.yaml
    sha256: e80bc218bf0c9730450560748dde5e8d2f2b32660c66159b3d74ef401e50c3eb
    role: target
  - path: data/records/kurnakovite.yaml
    sha256: 1a63e16fff126c8e902d59d6534c6ca60827d13ba77897a46886b1fa3e039bec
    role: target
  - path: data/records/kutnohorite.yaml
    sha256: 20562fc3fdb5fc1b2be7f521ae0701920de6a61f994b38dc596c9cc75372ddcd
    role: target
  - path: data/records/laforetite.yaml
    sha256: 7731ab6ac8982d63e9e6b11496785213ca16e8bb2a62c5afb8ee1bab511d3d70
    role: target
  - path: data/records/lansfordite.yaml
    sha256: 0a98ebec9f1fb285661945880c01eab366c38440659f02ca0ae284f42c1ee80f
    role: target
  - path: data/records/lanthanite-ce.yaml
    sha256: af5d8468a74e6e252c316f46b3229eb7555be1cf32f71e4fe16a6e8fa217bad4
    role: target
  - path: data/records/lanthanite-la.yaml
    sha256: 7ed6adbc91a2652426015dfa24c3dce6d7e0c17e7dd198151b068243fc9a6f1e
    role: target
  - path: data/records/lanthanite-nd.yaml
    sha256: 1dee86d641a588d11539e26991434d33000a3cb1779ddf9911c35cb0db47c9db
    role: target
  - path: data/records/larderellite.yaml
    sha256: e137d971afcfe3fed9c352de87b2bec0f15ff41af1bd621d7d5e19fe88ddeb70
    role: target
  - path: data/records/laueite.yaml
    sha256: 79ec71fe1797601d9c5cfc6be9bc654e9686926914911d3e96509bb45642a4b7
    role: target
  - path: data/records/lepidocrocite.yaml
    sha256: efab1b0f544b5ba35839d289a82825001fdb3e47615e54a74aa6f352d7d8178f
    role: target
  - path: data/records/libethenite.yaml
    sha256: 78ea2e0a4b3ca0df7142976750cb4c6db2f2199a442d636f303b179369e0a5c0
    role: target
  - path: data/records/lindbergite.yaml
    sha256: 0fe29a66efa15f07e79855525aa4e38f28532dd869eea0fd7d1e34c49da5e3b3
    role: target
  - path: data/records/lithiophilite.yaml
    sha256: f587f195a1f357f0700f860fd4d83122303fd53a393881b68d7549def94e9e1f
    role: target
  - path: data/records/lizardite.yaml
    sha256: 535a6f4a0c3f74f254ab0f3d19c4ead03774d16a8c83f7769d1c4aeac0092684
    role: target
  - path: data/records/loellingite.yaml
    sha256: 488aeb1f5044ef99cc8a2699fd9dd35523c735d3e2f56bbfd1b1bc4a566d7ac5
    role: target
  - path: data/records/lorenzenite.yaml
    sha256: 16bde318ff5d8bc7da7e67681a5a170b97d6fd800767ec9644d12c556feb772d
    role: target
  - path: data/records/ludlamite.yaml
    sha256: 42c64afbc1a9abdfbe0292079391033175f61692a075e429932c08a9b684973c
    role: target
  - path: data/records/mackinawite.yaml
    sha256: 8710787a7c9658a26b83d6fe7306f7e338f31ee823747ac3b259b26d9367e507
    role: target
  - path: data/records/maghemite.yaml
    sha256: ecc63f2aa4a967a297d497d5ec279157b56bc1609fa44c0dd85f34e8aed2e3ed
    role: target
  - path: data/records/magnetite.yaml
    sha256: d2781c4c48ee85c9bea32e3caaa2795ee362a0b3c69108d1c925428df8203020
    role: target
  - path: data/records/malachite.yaml
    sha256: bc80021da273bb3f1119321a4436e04b78faa4b6162d58967753f5fb5f908018
    role: target
  - path: data/records/manganite.yaml
    sha256: a53c5947dbb29076591a28ad0953344af5d5f91c6e7aec3b9640ebfd1ca1f276
    role: target
  - path: data/records/marcasite.yaml
    sha256: 81f3e00e4b5a22d39bc1bf895ebd5893d71c8e7a088d59fe8c8f1609000efcca
    role: target
  - path: data/records/mcallisterite.yaml
    sha256: 199009423ed1f432fc2e7bf5f7c71ed9961c571eb5759de7c4a00fb6b196cbb7
    role: target
  - path: data/records/mckelveyite-y.yaml
    sha256: 94f0ae37934d615b0e750570799775c47956e66bc8fcfa1f9c9f874196ea1717
    role: target
  - path: data/records/melanterite.yaml
    sha256: e4975a5a0c3bb3f10b9cc73e15757840d51e2047dd147aec050ee1274806cd9d
    role: target
  - path: data/records/meta-ankoleite.yaml
    sha256: db458cb4c913252762ae1c403d7e6aca38908f55ef0c15054ee248c455358951
    role: target
  - path: data/records/metacinnabar.yaml
    sha256: 0bb941fbfa16112b5dddff9d25e414e4a5ce00ce79bf9ab80ee39f4285ca4c31
    role: target
  - path: data/records/metaschoepite.yaml
    sha256: 30a545ff8fc8d954ac2722818a0c78ecb95c0b2f12bdeeef8ddf2a54ed6c86f0
    role: target
  - path: data/records/metastudtite.yaml
    sha256: a4618421c679685d6fc2677fafcf95320bac69e0af590e29e653ddcc92ede8d0
    role: target
  - path: data/records/metatorbernite.yaml
    sha256: a9c9cc4e54da73722ccef76e9ae1b26835a64c7327391e8ca63a2b25e5fe1ee7
    role: target
  - path: data/records/metatyuyamunite.yaml
    sha256: cb978e9a4b8204eb8b17234a1cdd572af342612635d221e610c40be23e3ee674
    role: target
  - path: data/records/metavivianite.yaml
    sha256: 08f50a56a622fceb4f76c6312a05e32b57150e525bd2340baa10b75f09aad1d9
    role: target
  - path: data/records/metazeunerite.yaml
    sha256: f3d24b6f8b8b748b1a7cdcee75f549bd743eed29b1d7b72dae6cb55d4fb5490b
    role: target
  - path: data/records/meyerhofferite.yaml
    sha256: a313fcc6954a68615590b58df5fc0408d5b9aabbcc260d8205d43c6bf1fe10f7
    role: target
  - path: data/records/microcline.yaml
    sha256: cf98d9198bacd849620259155e00c36fcd6b13e063887b674f2e2921551622fb
    role: target
  - path: data/records/millerite.yaml
    sha256: 3211129adad8abf3a53478c9f2652688f216b46ae668ecb61c0496bafe229bdb
    role: target
  - path: data/records/mimetite.yaml
    sha256: c9e5d430d0f060e0e8cb4539f9bcec86168d657f07682a9b8c420ecec2e858a2
    role: target
  - path: data/records/molybdenite.yaml
    sha256: 80f8e7afa79002d25eb6ef1bc05d1db7e87223580cee5a6a5db4f8816a8d8c56
    role: target
  - path: data/records/monazite-ce.yaml
    sha256: 4e852e05387e59e4581bd379ba832bd0b1b67cb7fc32d8bcfccaa862d29a6bae
    role: target
  - path: data/records/monazite-gd.yaml
    sha256: 22dadc915191c2e871fd01ac84205b4489c90c39d1145e3f1d7531da483a4b34
    role: target
  - path: data/records/monazite-la.yaml
    sha256: c85a83609a45fc37a0be5e1f6876e0ecd38fe83a884a4104b9b9e89a69242598
    role: target
  - path: data/records/monazite-nd.yaml
    sha256: 8da4ae4a6c4b41d742e1b5f283a0d2750b18d79c5fa84e836402e07886b9e7dd
    role: target
  - path: data/records/monazite-sm.yaml
    sha256: 1a6f15007e6fe0bb333add148b0a82111b7ad3ccd12eb516ed53aaa6da37da1d
    role: target
  - path: data/records/monetite.yaml
    sha256: 843c9a36208772efdcf82b16835cb947a6b00cb4aa278b7b27e4bd9324392ac7
    role: target
  - path: data/records/monohydrocalcite.yaml
    sha256: 9ee8f966b7703eab13d7e191421a61353f0f20c22ae7f2e69c10f79bfebee8f9
    role: target
  - path: data/records/montebrasite.yaml
    sha256: 3551e04e9a28a73b2d6e931df4c63686fc822aeb1793078397983f2e547ef744
    role: target
  - path: data/records/montmorillonite.yaml
    sha256: c25638a1ed8128e31733f560aeea1a0fc1bb73e420425c65422923064efa1c6e
    role: target
  - path: data/records/montroseite.yaml
    sha256: 6db8dd6407d289895446e73a87fee295318c1bbe01d6b7fd2d668948f9f5e203
    role: target
  - path: data/records/moolooite.yaml
    sha256: 21386f82e1bb01a7b6f4d5178c49e91d8ae73b29db427142c7742f8eb826d43e
    role: target
  - path: data/records/muscovite.yaml
    sha256: 23f2b3f7ead11cb1dc5904f6c8cd343265a151c6049eeb57e56318ccfd789680
    role: target
  - path: data/records/natroboltwoodite.yaml
    sha256: 86ccee3f5a185709fbbdb889bd974ed4e0a35a005ed780d44b6d7c210ab898df
    role: target
  - path: data/records/natrojarosite.yaml
    sha256: 259d0aff12cd7d326145e46003171bb3860cef37e5e57429bf8033a6964437dd
    role: target
  - path: data/records/navajoite.yaml
    sha256: 221f8c3cdc2a71785f07cf0081f23f16dc908d723a847d29a11ec3834a962881
    role: target
  - path: data/records/nepheline.yaml
    sha256: 264d82b8366d9fceb9d8d31a2b6f8972f12ccb63806046aac919ca1db863d9bd
    role: target
  - path: data/records/nesquehonite.yaml
    sha256: 9844a1ad9fbf0dd36b813c97a0a6c28d42ed42624c5273459fdd02a47c26035a
    role: target
  - path: data/records/newberyite.yaml
    sha256: a8ed2f92ed8621803cf1aee6e6b109083f10c54a422ca5e4e6b517b7cbf7722a
    role: target
  - path: data/records/ningyoite.yaml
    sha256: 66b2bd8bf39d173ebac061239d81e6392601bbe2083013136fd5f3c641d5f433
    role: target
  - path: data/records/nobleite.yaml
    sha256: 1dade2cc18afd089d40a11279e0640c44849a80afa56459e8c0e5463ca8094ca
    role: target
  - path: data/records/nontronite.yaml
    sha256: 221195a250ebbe6e3c849bc6f949917fefc074a62327a4d930676d6bdc9fa7a1
    role: target
  - path: data/records/orpiment.yaml
    sha256: 6c4b4f1a6d0004ddd7df308fd339651adb8e1db18d8d570829fcb2bec20b754b
    role: target
  - path: data/records/orthoclase.yaml
    sha256: 5384e99eee7f66f68b055dbe1318306b34bf7db0beba6ec5a81508003440154d
    role: target
  - path: data/records/otavite.yaml
    sha256: d5a86cfb9c04f23c4fe87305142a0ab36a9e20cbf006c6c90e0c37a84cc91b18
    role: target
  - path: data/records/palygorskite.yaml
    sha256: 5c37105c361d14c20dc66502dfdf19a2537ee9e1a45d92833b7e22237e35ff55
    role: target
  - path: data/records/paracoquimbite.yaml
    sha256: 8cddc9f1df1e2445484b9a6a181b1bb0e22d9c173f1910018cb3ace258ea7d56
    role: target
  - path: data/records/paramontroseite.yaml
    sha256: 31759cf0806da0ef377764711654fd27859582ccf26462f638f3690c40f3c783
    role: target
  - path: data/records/parasymplesite.yaml
    sha256: 52f0b80c651c11a6d2d3c0ed308b146a0b8943b011fd878fa7994fa69900f4cb
    role: target
  - path: data/records/parauranophane.yaml
    sha256: fe68e3a09f93d1095747bddd8eb322f7acf48c32b7b20220324cfd9b25d9f861
    role: target
  - path: data/records/pascoite.yaml
    sha256: 37b434c93cb30ed04dfc43e6108ddc33a69c6da8f131dc271e3c5e03b2b28e75
    role: target
  - path: data/records/pentagonite.yaml
    sha256: b9df9885b6850d0e03cf5d30220e806e060b618fe07166804574a375598235ed
    role: target
  - path: data/records/pentlandite.yaml
    sha256: f7fbef9a034e1f8f1add573a03c5e3d717055b3cf9c3321dd1bd7bba1e7f768f
    role: target
  - path: data/records/perovskite.yaml
    sha256: c444cddea567aefcdfa9236a1c1b9f657914d7d63d5a74e6e759bc409c6d3aea
    role: target
  - path: data/records/pertlikite.yaml
    sha256: 72ab6b07b5e4d0b8a65ff684d67efca74f4ccb129fb80a58e7eb3353d2e94ca1
    role: target
  - path: data/records/petalite.yaml
    sha256: 05093fa5244c7bae10df6901ee86ef4b92c48ed0c7cd17dfe9612c00f6647571
    role: target
  - path: data/records/petrukite.yaml
    sha256: dbd70c2c58351a92ce407d0975d07efd9fd891ac91b84c00676e4c25eb2b620e
    role: target
  - path: data/records/phlogopite.yaml
    sha256: 3ea9bfe4e4f2fc69ae733bcaca0a46d1fd20aaeff21010797833fcd0fba9ba46
    role: target
  - path: data/records/phosphoferrite.yaml
    sha256: c03cff0bece6f49133887ca99bbfc1a2a21e88d11eea48589e88e92205c2825f
    role: target
  - path: data/records/phosphophyllite.yaml
    sha256: 81e2d02433dd326360bd1d72386be47d242e78383f1a0be02e1476da44c20be2
    role: target
  - path: data/records/piilonenite-nd.yaml
    sha256: ea51cc5ca1cfa3a9493accd3be16c32e3c22b1a9d4030b3155a703703c1fb9d2
    role: target
  - path: data/records/pinnoite.yaml
    sha256: 6ac772ee6c84a9bf503fe5c7e1b5e7df1f782e2c272497ba01b4e54b608c5b2b
    role: target
  - path: data/records/plumbojarosite.yaml
    sha256: 23e1d4d9a702f74ba96fc360a4138604c12271f5a997b48d5c310681a6761829
    role: target
  - path: data/records/polydymite.yaml
    sha256: 117651006cbaac785ebe9a7c8e93a597ca341e6554e5853831769ecfcd3da5f3
    role: target
  - path: data/records/polylithionite.yaml
    sha256: e40dfba62223862df7097462628ab53542b29a8302ed945e67d866c331d0e3d8
    role: target
  - path: data/records/powellite.yaml
    sha256: ae48266be7b108ee15d203db366f7388aae8a8623f46e1e118740f1aba2d1853
    role: target
  - path: data/records/preobrazhenskite.yaml
    sha256: 6f42fed83cf82a3c8bf9e4fd5fef880aefd76e429ed6e1199c5f2c4834697e06
    role: target
  - path: data/records/priceite.yaml
    sha256: 7287e6ab6c4b9fa688cff38883ef03a979c766aee23522d7da1cbad278e77dac
    role: target
  - path: data/records/probertite.yaml
    sha256: c1c3688b3d866aa26aef0eaf5e71f660ebbb997a061e5e0464f7e3296c10b60c
    role: target
  - path: data/records/pyrite.yaml
    sha256: 44ae5da852faad88e3056fb6e00a8e4be0d43c241a58e31c3661cd4bee812f9b
    role: target
  - path: data/records/pyroaurite.yaml
    sha256: a7f28d78b8aa86b21844344d3b85d4e74b1fa9d6f5a85ad57f91676ebe56ee02
    role: target
  - path: data/records/pyrochroite.yaml
    sha256: 1ca16d4224942cd258a256563f1f5c8d711b5328c2f95d70d76a032e4097d4d0
    role: target
  - path: data/records/pyrolusite.yaml
    sha256: 47ce73b2f3c987208bee82bbd91109870d1866a90fbc580172f1907269f44831
    role: target
  - path: data/records/pyromorphite.yaml
    sha256: 87973d0a231986d00bf9883c4c6f941657b8abfd9d83ee418d61ac7d8faf88e5
    role: target
  - path: data/records/pyrrhotite.yaml
    sha256: 11aa665e37192017dbbc7665e6454e81bd565258eab49a6263ebda3efc4e4fd7
    role: target
  - path: data/records/quenstedtite.yaml
    sha256: 65fea95e77fd5d45eeb19722b1d63ded6220b4607914b71308dba9fcc19f2907
    role: target
  - path: data/records/ramsdellite.yaml
    sha256: 8ae85741406c1dff3a460f8da2bb9c6a6135cf90760727345be491384477d570
    role: target
  - path: data/records/realgar.yaml
    sha256: 6d032608db690eb08faf4c3f116186b7d0c843f2eb1faedcd02ae744aff996d9
    role: target
  - path: data/records/regerite.yaml
    sha256: 04b986aac1da05f459669f99971a0c2893115d46be4f31e405f4b56687e57d3d
    role: target
  - path: data/records/renierite.yaml
    sha256: a1c9a0a102aa07ff9f99dfc7463e9bf2b80fb58af52bbabc533d48604787f58c
    role: target
  - path: data/records/rhabdophane-ce.yaml
    sha256: cf5c8567e2e3cda02fa829d521ab7deda870b77a1091ff41dd8dcc8da7883f89
    role: target
  - path: data/records/rhabdophane-la.yaml
    sha256: 3ea9dade6024040827f11e86c0359287ba7ddf7a39eebed38f83d5ebf9cf5ad1
    role: target
  - path: data/records/rhodochrosite.yaml
    sha256: d120d1c277b742539d55e731708b4d4b628017d5b6298a70f408d6e54b30eb0c
    role: target
  - path: data/records/rhomboclase.yaml
    sha256: d54486e50f28fa146887884efeb703d932a435b4fd0dc7643e886dfb63a667c1
    role: target
  - path: data/records/richetite.yaml
    sha256: 23243f297839a222115c0836d4e0830ea7fab571e57fa9d1be9436301f7194a6
    role: target
  - path: data/records/riebeckite.yaml
    sha256: 5c0febb77a492454be39c398cd2d364aa3fdb927e2f9aab46e59efd35dd20e11
    role: target
  - path: data/records/rivadavite.yaml
    sha256: 7f80d7b2f7136a68eb6929a0abbc16cb1fac8abcca7bc55a47356d4a120c3417
    role: target
  - path: data/records/romanechite.yaml
    sha256: d3f4c0ab0c19ac3b8881248c867cdca60268e176aa1ae7a04770777270ac2ac8
    role: target
  - path: data/records/roquesite.yaml
    sha256: 25758f27422dc9bfc8f2eae8928c369ed6b61e34186e58664ff3dacacaf95b29
    role: target
  - path: data/records/roscoelite.yaml
    sha256: b942d0a106934228147c4196969077a759939c2925e608254058b4ad1b353c47
    role: target
  - path: data/records/rozenite.yaml
    sha256: 103c00774c7184fa48782fd9acd831330f1f800fd7cfcfd2741abed72a92400f
    role: target
  - path: data/records/rutherfordine.yaml
    sha256: c599fd065bafdb04de83897b7dbf7ba45e561b4cc97547cc3aaa9118c318f208
    role: target
  - path: data/records/rutile.yaml
    sha256: 42b825d1ad84f74dd587edc0651d66838bd282027714116d75b79068a599b73b
    role: target
  - path: data/records/sabugalite.yaml
    sha256: 246ece1435a6391cf55c8c73691d7cd6d6de5dc5de694bc9958bc84187442705
    role: target
  - path: data/records/sakuraiite.yaml
    sha256: f1343d27b3aaa67fae019646cd8deb17aebc7e92c11628ca8c3c87629e19c1c7
    role: target
  - path: data/records/saleeite.yaml
    sha256: f193bef3cdd0912e8d78f3516bfeb1a7674b23456cc4ca89f7ca9bf19ddfac16
    role: target
  - path: data/records/saponite.yaml
    sha256: edf1d6fe0f38f2339dfcd200989cc7e05e963cf45ee7c79afc4473f0d4c97a5f
    role: target
  - path: data/records/sauconite.yaml
    sha256: 1f1054d6eca5e5a4a84cce592485a2046a11071564407febe03717228eadca72
    role: target
  - path: data/records/scheelite.yaml
    sha256: a8fd85cedb9100cb6a3b1ec8e5bafe5be2d5a4fe1ea740abf33acee44a1c7425
    role: target
  - path: data/records/schertelite.yaml
    sha256: d0ee06b787afd1ec9ddad9d8e53fd15874c517c8da05c4a28ef395fb9df8b7a6
    role: target
  - path: data/records/schoepite.yaml
    sha256: 6a91191737174a9504a1f6606f8d9126dc08ee1e16c67025c294f66b18ccde00
    role: target
  - path: data/records/schwertmannite.yaml
    sha256: 8b99fc546f4743e648c83f3d6bd5214c0b2de64b1e0d6365eb233af632d650b5
    role: target
  - path: data/records/scorodite.yaml
    sha256: a27c51ef3546c8e8454900ec654e76b8b4f338a4f84680c41d3c9125edad8245
    role: target
  - path: data/records/senarmontite.yaml
    sha256: 3056e0f17442949bbbc0d02d2cee6364b68c520b46aeeec2c0262d3a520adaf7
    role: target
  - path: data/records/sepiolite.yaml
    sha256: fe620233a801d875751cc825bc73fbf089354ebd594c985df51ee3bbfbdf1034
    role: target
  - path: data/records/siderite.yaml
    sha256: 664cc364a07cd83345b7d2b7cff2ac6a30403e6a93b3e7cb153418737a835ba0
    role: target
  - path: data/records/simonkolleite.yaml
    sha256: 13efe05b52e50e21a5ad1dae6b131b6723ee8248676dcce93d72d87aa2b495b9
    role: target
  - path: data/records/sklodowskite.yaml
    sha256: 4c65a7130837c668c697a43817c631a381191abf5f16fa9babeb5971f5865589
    role: target
  - path: data/records/skutterudite.yaml
    sha256: a3794fc2082661a3c7fc2de40494b0800ceb4ccb7d38565f89948e1c01a70cf3
    role: target
  - path: data/records/smithsonite.yaml
    sha256: 1a2d72e7da1d873806570c0cf2a34a6216d0c8821fc7fd57f1c14326e2c67cb2
    role: target
  - path: data/records/soddyite.yaml
    sha256: 346601a9ef95444ac9cf161bbcd8c41132a22d6e73c3d1517c97bdd6c0d68adf
    role: target
  - path: data/records/sphalerite.yaml
    sha256: 72097281d609abe00c1c46c133f9967d93950bfd5b0e8c03f1fb2bfc47391b8d
    role: target
  - path: data/records/spodumene.yaml
    sha256: 2aee634d0e16c0a68cce048dc5d3ffa171e244a0aac1849a42f1c805eeb25b9e
    role: target
  - path: data/records/stannite.yaml
    sha256: 8490730a9c745a6016f4f6fbeb5b27c6b62ba62c1c53b51e9919d21e6740eec0
    role: target
  - path: data/records/stevensite.yaml
    sha256: 2247c7dccbbac10f83ae567769ffce529f3967150c0bd7811786f1c495470b1a
    role: target
  - path: data/records/stibnite.yaml
    sha256: 436111a89c641f24b52e1c42881f554b19598701fc946b20fea75ee9a73d5e97
    role: target
  - path: data/records/stolzite.yaml
    sha256: 12522eba1b26e9d72b2900d93f99a0c2dbee69ea970f263aa793666225befd0d
    role: target
  - path: data/records/strengite.yaml
    sha256: 3938c8ea4c517b939428ffcf9509db06c1dcff029fcd2e50664cda268bc349f7
    role: target
  - path: data/records/strontianite.yaml
    sha256: fd0ba6d8bd4e69e250e0e0109e01dcccb86771cbcfb8e9b0f6ef6fd890275d66
    role: target
  - path: data/records/struvite-k.yaml
    sha256: b278b324e0bd7a1b8096e5e5a9bd2e8cb0544aa379cdefb908d1863ad9fce13c
    role: target
  - path: data/records/struvite.yaml
    sha256: 48c215816ba65046aeaeed7a15bd80130a31d62420857a09c5e46ddf762cc266
    role: target
  - path: data/records/studtite.yaml
    sha256: c917595b2f11cc8f8911fcd45659db0bac569b3bd60cdfa2d3632b69e9594225
    role: target
  - path: data/records/sulfoborite.yaml
    sha256: 1cd49c620ab8c16d31255dfe103f8e94e184a223b4c046c797c34987b1ee3a89
    role: target
  - path: data/records/svanbergite.yaml
    sha256: eb803f7efc34ea61e663f6ef8543665f9f649817ba23b4c6daf66ab456e97559
    role: target
  - path: data/records/switzerite.yaml
    sha256: 71280026ec5f2e1b2a056288294420dd09d76c0d986e62c100dae02602ac25a6
    role: target
  - path: data/records/synchysite-ce.yaml
    sha256: 8e20019c4b8ca8050250bf924cf469f960f303551e6bdd316df892b7b0fd712d
    role: target
  - path: data/records/szaibelyite.yaml
    sha256: 0f29048c91ab3c2224d4de4193f685921af03b86b1422435a3afb706f3ada2d4
    role: target
  - path: data/records/szomolnokite.yaml
    sha256: a7c9be09fd8e8cb544ca1e8251205ac1c085ef1fa62194e9009b0633543b7f59
    role: target
  - path: data/records/talc.yaml
    sha256: a3cea92e8e5a83897af7919880c059b2f5ec94e2a7930f87a6d26eba3ad706f6
    role: target
  - path: data/records/tennantite-in.yaml
    sha256: c768abfee1cea31682d06c0afeaa48b6d72219761de566640737f01b8c873ecf
    role: target
  - path: data/records/tenorite.yaml
    sha256: e5b0bfd564a30686d9ca03cdc24b971bafd0f213624d377ff71dd3b050037112
    role: target
  - path: data/records/thomasclarkite-y.yaml
    sha256: 890e0da3caaec6939bcb2178dcbb3f007b36dc410d6c135a022797e8dbe5f678
    role: target
  - path: data/records/tincalconite.yaml
    sha256: 194e5d2db3201262945c65832a05a45cb095500dddf4721e6318fd09501b7c8d
    role: target
  - path: data/records/titanite.yaml
    sha256: d01213f0361839d8f147313c5033eee5edf3855b30ad6c02bcd64a8d1615f81c
    role: target
  - path: data/records/todorokite.yaml
    sha256: a8d602a0aabbd1c4fa3b8e53d3ed580d9f51ab8d6b5dd5ce53aecae5516d9088
    role: target
  - path: data/records/torbernite.yaml
    sha256: cb20d6b645f1649d468a1d503f87e8692ce5b44b2823b3bb8675cb8a26c1ab33
    role: target
  - path: data/records/triphylite.yaml
    sha256: 34611e50b9e4e81b656fe6f9beacd44513613d5bcfbbe8489c668c7c0bcf14ec
    role: target
  - path: data/records/troilite.yaml
    sha256: 9ffabe9fd2204c41191ff4167f68071ec02b160fed4b432dffb0b626cfbdb017
    role: target
  - path: data/records/tunellite.yaml
    sha256: ad0e7b1b892bc4f8b970661c079660358651a8217d6f159bf4c524996760930f
    role: target
  - path: data/records/ulexite.yaml
    sha256: 1955c662cbfd6e48816acdbc28f9432a028ffea875e42bca58d6b4e04e3f0242
    role: target
  - path: data/records/uramphite.yaml
    sha256: 9a75ded70935425b4d938cb62081a28b767a9df66b7c22a8734df54912a014eb
    role: target
  - path: data/records/uraninite.yaml
    sha256: a09be0d68b606fd0c87b75569b5c7f95211f132533bf8b8d415880cc84b97912
    role: target
  - path: data/records/uranophane.yaml
    sha256: 648fb5f5b33c07b1a1467d9ce8634419900e5a4e1bb03cc5a93d8b4f1fc3584d
    role: target
  - path: data/records/uranopilite.yaml
    sha256: 4f149c8fc021ebde419c0c308b632b0800885539fd9dc2ca44957d63cf4095c8
    role: target
  - path: data/records/vaesite.yaml
    sha256: 18d7c9dbf78c9596d94ed652479193390af53fdf3b81d839896e6d300027ca97
    role: target
  - path: data/records/vandenbrandeite.yaml
    sha256: 7e2fe85151c9023197b7933d178a6681138a2c4ff76a8178905c32cec42dceb9
    role: target
  - path: data/records/variscite.yaml
    sha256: 3c272778de8dc7b867ffca8fe5bc10d210de3938315f57b898f3d95ab7efb59f
    role: target
  - path: data/records/vaterite.yaml
    sha256: 7ffcf6f5bc1904774bf9382c8900c1481722ad4514418157813a907b09dfa656
    role: target
  - path: data/records/veatchite.yaml
    sha256: d0cfdd241fd57f65d8730d68f1554dd3c238da34f92dc48be35f5be412b6e183
    role: target
  - path: data/records/violarite.yaml
    sha256: 08cc473bd9baed8ad55db4f058162f72f68186d84fd0d548fb69f6ba7b6b5e3e
    role: target
  - path: data/records/vivianite.yaml
    sha256: 8d820242970cd8a50d54ce1644caee79cdc508ba7a7c575f556dbe9f94dfc3d7
    role: target
  - path: data/records/voltaite.yaml
    sha256: 04192b1dedc33a17cd294639ca2d53a63afd2665804207d330ce68f2bb236605
    role: target
  - path: data/records/weddellite.yaml
    sha256: f1505e8e61fa9bb9750f60d0d80b86369f31f4aab7e03ca3970c52afbb4f488d
    role: target
  - path: data/records/weeksite.yaml
    sha256: 653fa1fb6884dda0cc1fd42f9ec35c5129d36ef55669deae0a2de8604d9da1f4
    role: target
  - path: data/records/wheatleyite.yaml
    sha256: 8a49e55b269881fb37e038c3ad09bbb133e80837022cb9d85fee1cc248011e46
    role: target
  - path: data/records/whewellite.yaml
    sha256: 22ae0ddc7fd2186cb837a636c14622240eba392de1bfe4c93072b9b878c2cc56
    role: target
  - path: data/records/whitlockite.yaml
    sha256: 4f33474f77f746399d5745123eecbbe40da0393466baf71a139f6b61fa68ae88
    role: target
  - path: data/records/willemite.yaml
    sha256: ebea085928aa811ca788d5ae8dc8151d4cb9dc64cd40e9d16cbb3de33e0e81e7
    role: target
  - path: data/records/wollastonite.yaml
    sha256: f8fd6bf3632e0addf0edbf23e39ac1d81070777688b439d66cad323731757ff4
    role: target
  - path: data/records/woodhouseite.yaml
    sha256: bb079f4f3fef684d16d91b307ecc7a6c5f951258500586c21db16433f856f0ad
    role: target
  - path: data/records/wulfenite.yaml
    sha256: fd87a4a48ae6ee7ae37a86d2c2f613fde65fd2080b40f44e0ad6830f68df43c7
    role: target
  - path: data/records/wurtzite.yaml
    sha256: 3023a9fa6aa8f6f82b2284252f7245ad85ab1ff297f5cddaee53e61f2f4590a3
    role: target
  - path: data/records/xenotime-gd.yaml
    sha256: 94ea0b1119f49bf293fb2a7ce65872a58aa0cf5c046202cdb209b66e710c79e4
    role: target
  - path: data/records/xenotime-y.yaml
    sha256: a37d27346742d1cde30a5a01d6e58bde938435c3980fd503d50594f68da718de
    role: target
  - path: data/records/xenotime-yb.yaml
    sha256: 544e5ad86d3263c650aa511e48bb5bb7f945bfdbd34ef125a6dbff0acca727c0
    role: target
  - path: data/records/yanomamite.yaml
    sha256: 581f5ddcb8679302995baf331588601bde7b030416b0d2f50aa7ea25249e9e09
    role: target
  - path: data/records/yusupovite.yaml
    sha256: e342ffb44f22f0e65f0bfe60f11cb1a28f53b60cb3c5a3f00e4c4f9726102f83
    role: target
  - path: data/records/zeunerite.yaml
    sha256: d9234d64df9772ad0e127d36320975d0870fcd909bf600991ece25b33e03f453
    role: target
  - path: data/records/zincite.yaml
    sha256: b5636b992ce917a20726534cb4e9178dac2251043c32762f22988ecff74334e1
    role: target
  - path: data/records/zincobriartite.yaml
    sha256: b06ce6857cd85a53e1c2c11d4f414552ea9c57146b9f7d3f9e46a54718411782
    role: target
  - path: data/records/zippeite.yaml
    sha256: 000f9f5ba45925434909557cc7a167181227467f077bdbcd1d4e114c7aa3fa90
    role: target
  - path: data/records/zircon.yaml
    sha256: 6ac2ca98d3a95cfe0d1ae11f8d8d6c5e9e771512e1b485a53a55abdc949816e5
    role: target
  - path: data/records/zirconolite.yaml
    sha256: 8e57937517a5c266d8dc6cb2e3ab96cd33de6230c046244a80538496f39dfe60
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 105313f55214e4b81ce23a1338262c752c44017c8150fba8721d75826ec03932
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 365
  reviewed_target_ids:
  - cmmmech:acanthite
  - cmmmech:adamsite-y
  - cmmmech:akaganeite
  - cmmmech:alabandite
  - cmmmech:albite
  - cmmmech:alburnite
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:alunite
  - cmmmech:amblygonite
  - cmmmech:ameghinite
  - cmmmech:ammonioborite
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:ancylite-ce
  - cmmmech:andersonite
  - cmmmech:anglesite
  - cmmmech:anhydrite
  - cmmmech:anilite
  - cmmmech:annabergite
  - cmmmech:anorthite
  - cmmmech:aragonite
  - cmmmech:argentojarosite
  - cmmmech:argyrodite
  - cmmmech:aristarainite
  - cmmmech:arsenopyrite
  - cmmmech:artinite
  - cmmmech:asbolane
  - cmmmech:atacamite
  - cmmmech:autunite
  - cmmmech:azurite
  - cmmmech:baddeleyite
  - cmmmech:bainbridgeite-ndce
  - cmmmech:bainbridgeite-yce
  - cmmmech:baricite
  - cmmmech:bassanite
  - cmmmech:becquerelite
  - cmmmech:beudantite
  - cmmmech:billietite
  - cmmmech:birnessite
  - cmmmech:bismuthinite
  - cmmmech:bixbyite-mn
  - cmmmech:bobierrite
  - cmmmech:boehmite
  - cmmmech:boltwoodite
  - cmmmech:boracite
  - cmmmech:borax
  - cmmmech:bornite
  - cmmmech:briartite
  - cmmmech:brochantite
  - cmmmech:brookite
  - cmmmech:brucite
  - cmmmech:brushite
  - cmmmech:burbankite
  - cmmmech:cadmoindite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:calcioveatchite
  - cmmmech:calcite
  - cmmmech:carnotite
  - cmmmech:carrollite
  - cmmmech:cassiterite
  - cmmmech:catapleiite
  - cmmmech:cattiite
  - cmmmech:cavansite
  - cmmmech:caysichite-y
  - cmmmech:celestine
  - cmmmech:cerianite-ce
  - cmmmech:cerussite
  - cmmmech:chalcocite
  - cmmmech:chalcopyrite
  - cmmmech:chernikovite
  - cmmmech:childrenite
  - cmmmech:chlorapatite
  - cmmmech:chromite
  - cmmmech:chrysotile
  - cmmmech:chukanovite
  - cmmmech:churchite-y
  - cmmmech:cinnabar
  - cmmmech:cobaltite
  - cmmmech:coffinite
  - cmmmech:colemanite
  - cmmmech:compreignacite
  - cmmmech:coquimbite
  - cmmmech:cordylite-ce
  - cmmmech:corkite
  - cmmmech:covellite
  - cmmmech:crandallite
  - cmmmech:cryptomelane
  - cmmmech:cuprite
  - cmmmech:cuprosklodowskite
  - cmmmech:curite
  - cmmmech:digenite
  - cmmmech:diopside
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:dypingite
  - cmmmech:dzhalindite
  - cmmmech:elpidite
  - cmmmech:enstatite
  - cmmmech:eosphorite
  - cmmmech:erythrite
  - cmmmech:ezcurrite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:felsobanyaite
  - cmmmech:feroxyhyte
  - cmmmech:ferricopiapite
  - cmmmech:ferrihydrite
  - cmmmech:ferrokesterite
  - cmmmech:florencite-ce
  - cmmmech:florencite-la
  - cmmmech:fluorapatite
  - cmmmech:fluorite
  - cmmmech:forsterite
  - cmmmech:fritzscheite
  - cmmmech:galena
  - cmmmech:germanite
  - cmmmech:gersdorffite
  - cmmmech:gibbsite
  - cmmmech:ginorite
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:goldmanite
  - cmmmech:gorceixite
  - cmmmech:gowerite
  - cmmmech:goyazite
  - cmmmech:greenockite
  - cmmmech:greigite
  - cmmmech:gypsum
  - cmmmech:gysinite-nd
  - cmmmech:hafnon
  - cmmmech:hannayite
  - cmmmech:haradaite
  - cmmmech:hauerite
  - cmmmech:hausmannite
  - cmmmech:hawleyite
  - cmmmech:hazenite
  - cmmmech:heazlewoodite
  - cmmmech:hematite
  - cmmmech:hemimorphite
  - cmmmech:heterogenite
  - cmmmech:heterosite
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:huntite
  - cmmmech:hureaulite
  - cmmmech:hydroboracite
  - cmmmech:hydrocerussite
  - cmmmech:hydromagnesite
  - cmmmech:hydroniumjarosite
  - cmmmech:hydrotalcite
  - cmmmech:hydroxylapatite
  - cmmmech:hydrozincite
  - cmmmech:ilmenite
  - cmmmech:inderborite
  - cmmmech:inderite
  - cmmmech:indite
  - cmmmech:inyoite
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaliborite
  - cmmmech:kaolinite
  - cmmmech:katsarosite
  - cmmmech:kernite
  - cmmmech:kesterite
  - cmmmech:kornelite
  - cmmmech:kozoite-la
  - cmmmech:kozoite-nd
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:kurnakovite
  - cmmmech:kutnohorite
  - cmmmech:laforetite
  - cmmmech:lansfordite
  - cmmmech:lanthanite-ce
  - cmmmech:lanthanite-la
  - cmmmech:lanthanite-nd
  - cmmmech:larderellite
  - cmmmech:laueite
  - cmmmech:lepidocrocite
  - cmmmech:libethenite
  - cmmmech:lindbergite
  - cmmmech:lithiophilite
  - cmmmech:lizardite
  - cmmmech:loellingite
  - cmmmech:lorenzenite
  - cmmmech:ludlamite
  - cmmmech:mackinawite
  - cmmmech:maghemite
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:mcallisterite
  - cmmmech:mckelveyite-y
  - cmmmech:melanterite
  - cmmmech:meta-ankoleite
  - cmmmech:metacinnabar
  - cmmmech:metaschoepite
  - cmmmech:metastudtite
  - cmmmech:metatorbernite
  - cmmmech:metatyuyamunite
  - cmmmech:metavivianite
  - cmmmech:metazeunerite
  - cmmmech:meyerhofferite
  - cmmmech:microcline
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:monazite-ce
  - cmmmech:monazite-gd
  - cmmmech:monazite-la
  - cmmmech:monazite-nd
  - cmmmech:monazite-sm
  - cmmmech:monetite
  - cmmmech:monohydrocalcite
  - cmmmech:montebrasite
  - cmmmech:montmorillonite
  - cmmmech:montroseite
  - cmmmech:moolooite
  - cmmmech:muscovite
  - cmmmech:natroboltwoodite
  - cmmmech:natrojarosite
  - cmmmech:navajoite
  - cmmmech:nepheline
  - cmmmech:nesquehonite
  - cmmmech:newberyite
  - cmmmech:ningyoite
  - cmmmech:nobleite
  - cmmmech:nontronite
  - cmmmech:orpiment
  - cmmmech:orthoclase
  - cmmmech:otavite
  - cmmmech:palygorskite
  - cmmmech:paracoquimbite
  - cmmmech:paramontroseite
  - cmmmech:parasymplesite
  - cmmmech:parauranophane
  - cmmmech:pascoite
  - cmmmech:pentagonite
  - cmmmech:pentlandite
  - cmmmech:perovskite
  - cmmmech:pertlikite
  - cmmmech:petalite
  - cmmmech:petrukite
  - cmmmech:phlogopite
  - cmmmech:phosphoferrite
  - cmmmech:phosphophyllite
  - cmmmech:piilonenite-nd
  - cmmmech:pinnoite
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:polylithionite
  - cmmmech:powellite
  - cmmmech:preobrazhenskite
  - cmmmech:priceite
  - cmmmech:probertite
  - cmmmech:pyrite
  - cmmmech:pyroaurite
  - cmmmech:pyrochroite
  - cmmmech:pyrolusite
  - cmmmech:pyromorphite
  - cmmmech:pyrrhotite
  - cmmmech:quenstedtite
  - cmmmech:ramsdellite
  - cmmmech:realgar
  - cmmmech:regerite
  - cmmmech:renierite
  - cmmmech:rhabdophane-ce
  - cmmmech:rhabdophane-la
  - cmmmech:rhodochrosite
  - cmmmech:rhomboclase
  - cmmmech:richetite
  - cmmmech:riebeckite
  - cmmmech:rivadavite
  - cmmmech:romanechite
  - cmmmech:roquesite
  - cmmmech:roscoelite
  - cmmmech:rozenite
  - cmmmech:rutherfordine
  - cmmmech:rutile
  - cmmmech:sabugalite
  - cmmmech:sakuraiite
  - cmmmech:saleeite
  - cmmmech:saponite
  - cmmmech:sauconite
  - cmmmech:scheelite
  - cmmmech:schertelite
  - cmmmech:schoepite
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:senarmontite
  - cmmmech:sepiolite
  - cmmmech:siderite
  - cmmmech:simonkolleite
  - cmmmech:sklodowskite
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:soddyite
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:stevensite
  - cmmmech:stibnite
  - cmmmech:stolzite
  - cmmmech:strengite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:struvite-k
  - cmmmech:studtite
  - cmmmech:sulfoborite
  - cmmmech:svanbergite
  - cmmmech:switzerite
  - cmmmech:synchysite-ce
  - cmmmech:szaibelyite
  - cmmmech:szomolnokite
  - cmmmech:talc
  - cmmmech:tennantite-in
  - cmmmech:tenorite
  - cmmmech:thomasclarkite-y
  - cmmmech:tincalconite
  - cmmmech:titanite
  - cmmmech:todorokite
  - cmmmech:torbernite
  - cmmmech:triphylite
  - cmmmech:troilite
  - cmmmech:tunellite
  - cmmmech:ulexite
  - cmmmech:uramphite
  - cmmmech:uraninite
  - cmmmech:uranophane
  - cmmmech:uranopilite
  - cmmmech:vaesite
  - cmmmech:vandenbrandeite
  - cmmmech:variscite
  - cmmmech:vaterite
  - cmmmech:veatchite
  - cmmmech:violarite
  - cmmmech:vivianite
  - cmmmech:voltaite
  - cmmmech:weddellite
  - cmmmech:weeksite
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:whitlockite
  - cmmmech:willemite
  - cmmmech:wollastonite
  - cmmmech:woodhouseite
  - cmmmech:wulfenite
  - cmmmech:wurtzite
  - cmmmech:xenotime-gd
  - cmmmech:xenotime-y
  - cmmmech:xenotime-yb
  - cmmmech:yanomamite
  - cmmmech:yusupovite
  - cmmmech:zeunerite
  - cmmmech:zincite
  - cmmmech:zincobriartite
  - cmmmech:zippeite
  - cmmmech:zircon
  - cmmmech:zirconolite
  selection: data/records/*.yaml where material_kind == 'mineral' at 4d878383c92b44876df3bf166d96637c7581a59e
  description: Full-population Stage 4 category review of all 365 IMA-approved mineral
    species records in CMMMech.
targets:
- target_id: cmmmech:acanthite
  path: data/records/acanthite.yaml
  kind: maintained
  label: Acanthite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/acanthite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:adamsite-y
  path: data/records/adamsite-y.yaml
  kind: maintained
  label: Adamsite-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/adamsite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:akaganeite
  path: data/records/akaganeite.yaml
  kind: maintained
  label: Akaganeite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/akaganeite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:alabandite
  path: data/records/alabandite.yaml
  kind: maintained
  label: Alabandite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alabandite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:albite
  path: data/records/albite.yaml
  kind: maintained
  label: Albite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/albite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:alburnite
  path: data/records/alburnite.yaml
  kind: maintained
  label: Alburnite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alburnite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:alicewilsonite-yce
  path: data/records/alicewilsonite-yce.yaml
  kind: maintained
  label: Alicewilsonite-(YCe)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alicewilsonite-yce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:alicewilsonite-yla
  path: data/records/alicewilsonite-yla.yaml
  kind: maintained
  label: Alicewilsonite-(YLa)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alicewilsonite-yla.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:alunite
  path: data/records/alunite.yaml
  kind: maintained
  label: Alunite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alunite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:amblygonite
  path: data/records/amblygonite.yaml
  kind: maintained
  label: Amblygonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/amblygonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ameghinite
  path: data/records/ameghinite.yaml
  kind: maintained
  label: Ameghinite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ameghinite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ammonioborite
  path: data/records/ammonioborite.yaml
  kind: maintained
  label: Ammonioborite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ammonioborite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ammoniojarosite
  path: data/records/ammoniojarosite.yaml
  kind: maintained
  label: Ammoniojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ammoniojarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:anatase
  path: data/records/anatase.yaml
  kind: maintained
  label: Anatase
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anatase.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ancylite-ce
  path: data/records/ancylite-ce.yaml
  kind: maintained
  label: Ancylite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ancylite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:andersonite
  path: data/records/andersonite.yaml
  kind: maintained
  label: Andersonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/andersonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:anglesite
  path: data/records/anglesite.yaml
  kind: maintained
  label: Anglesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anglesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:anhydrite
  path: data/records/anhydrite.yaml
  kind: maintained
  label: Anhydrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anhydrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:anilite
  path: data/records/anilite.yaml
  kind: maintained
  label: Anilite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anilite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:annabergite
  path: data/records/annabergite.yaml
  kind: maintained
  label: Annabergite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/annabergite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:anorthite
  path: data/records/anorthite.yaml
  kind: maintained
  label: Anorthite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anorthite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:aragonite
  path: data/records/aragonite.yaml
  kind: maintained
  label: Aragonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aragonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:argentojarosite
  path: data/records/argentojarosite.yaml
  kind: maintained
  label: Argentojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/argentojarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:argyrodite
  path: data/records/argyrodite.yaml
  kind: maintained
  label: Argyrodite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/argyrodite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:aristarainite
  path: data/records/aristarainite.yaml
  kind: maintained
  label: Aristarainite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aristarainite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:arsenopyrite
  path: data/records/arsenopyrite.yaml
  kind: maintained
  label: Arsenopyrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenopyrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:artinite
  path: data/records/artinite.yaml
  kind: maintained
  label: Artinite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/artinite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:asbolane
  path: data/records/asbolane.yaml
  kind: maintained
  label: Asbolane
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/asbolane.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:atacamite
  path: data/records/atacamite.yaml
  kind: maintained
  label: Atacamite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/atacamite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:autunite
  path: data/records/autunite.yaml
  kind: maintained
  label: Autunite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/autunite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:azurite
  path: data/records/azurite.yaml
  kind: maintained
  label: Azurite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/azurite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:baddeleyite
  path: data/records/baddeleyite.yaml
  kind: maintained
  label: Baddeleyite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/baddeleyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bainbridgeite-ndce
  path: data/records/bainbridgeite-ndce.yaml
  kind: maintained
  label: Bainbridgeite-(NdCe)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bainbridgeite-ndce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bainbridgeite-yce
  path: data/records/bainbridgeite-yce.yaml
  kind: maintained
  label: Bainbridgeite-(YCe)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bainbridgeite-yce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:baricite
  path: data/records/baricite.yaml
  kind: maintained
  label: Barićite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/baricite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bassanite
  path: data/records/bassanite.yaml
  kind: maintained
  label: Bassanite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bassanite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:becquerelite
  path: data/records/becquerelite.yaml
  kind: maintained
  label: Becquerelite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/becquerelite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:beudantite
  path: data/records/beudantite.yaml
  kind: maintained
  label: Beudantite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/beudantite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:billietite
  path: data/records/billietite.yaml
  kind: maintained
  label: Billietite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/billietite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:birnessite
  path: data/records/birnessite.yaml
  kind: maintained
  label: Birnessite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/birnessite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bismuthinite
  path: data/records/bismuthinite.yaml
  kind: maintained
  label: Bismuthinite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bismuthinite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bixbyite-mn
  path: data/records/bixbyite-mn.yaml
  kind: maintained
  label: Bixbyite-(Mn)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bixbyite-mn.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bobierrite
  path: data/records/bobierrite.yaml
  kind: maintained
  label: Bobierrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bobierrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:boehmite
  path: data/records/boehmite.yaml
  kind: maintained
  label: Böhmite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/boehmite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:boltwoodite
  path: data/records/boltwoodite.yaml
  kind: maintained
  label: Boltwoodite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/boltwoodite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:boracite
  path: data/records/boracite.yaml
  kind: maintained
  label: Boracite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/boracite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:borax
  path: data/records/borax.yaml
  kind: maintained
  label: Borax
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/borax.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bornite
  path: data/records/bornite.yaml
  kind: maintained
  label: Bornite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bornite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:briartite
  path: data/records/briartite.yaml
  kind: maintained
  label: Briartite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/briartite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:brochantite
  path: data/records/brochantite.yaml
  kind: maintained
  label: Brochantite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/brochantite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:brookite
  path: data/records/brookite.yaml
  kind: maintained
  label: Brookite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/brookite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:brucite
  path: data/records/brucite.yaml
  kind: maintained
  label: Brucite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/brucite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:brushite
  path: data/records/brushite.yaml
  kind: maintained
  label: Brushite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/brushite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:burbankite
  path: data/records/burbankite.yaml
  kind: maintained
  label: Burbankite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/burbankite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cadmoindite
  path: data/records/cadmoindite.yaml
  kind: maintained
  label: Cadmoindite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cadmoindite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:calcioancylite-la
  path: data/records/calcioancylite-la.yaml
  kind: maintained
  label: Calcioancylite-(La)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcioancylite-la.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:calcioburbankite
  path: data/records/calcioburbankite.yaml
  kind: maintained
  label: Calcioburbankite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcioburbankite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:calcioveatchite
  path: data/records/calcioveatchite.yaml
  kind: maintained
  label: Calcioveatchite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcioveatchite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:calcite
  path: data/records/calcite.yaml
  kind: maintained
  label: Calcite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:carnotite
  path: data/records/carnotite.yaml
  kind: maintained
  label: Carnotite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/carnotite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:carrollite
  path: data/records/carrollite.yaml
  kind: maintained
  label: Carrollite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/carrollite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cassiterite
  path: data/records/cassiterite.yaml
  kind: maintained
  label: Cassiterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cassiterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:catapleiite
  path: data/records/catapleiite.yaml
  kind: maintained
  label: Catapleiite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/catapleiite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cattiite
  path: data/records/cattiite.yaml
  kind: maintained
  label: Cattiite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cattiite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cavansite
  path: data/records/cavansite.yaml
  kind: maintained
  label: Cavansite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cavansite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:caysichite-y
  path: data/records/caysichite-y.yaml
  kind: maintained
  label: Caysichite-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/caysichite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:celestine
  path: data/records/celestine.yaml
  kind: maintained
  label: Celestine
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/celestine.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cerianite-ce
  path: data/records/cerianite-ce.yaml
  kind: maintained
  label: Cerianite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cerianite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cerussite
  path: data/records/cerussite.yaml
  kind: maintained
  label: Cerussite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cerussite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chalcocite
  path: data/records/chalcocite.yaml
  kind: maintained
  label: Chalcocite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chalcocite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chalcopyrite
  path: data/records/chalcopyrite.yaml
  kind: maintained
  label: Chalcopyrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chalcopyrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chernikovite
  path: data/records/chernikovite.yaml
  kind: maintained
  label: Chernikovite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chernikovite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:childrenite
  path: data/records/childrenite.yaml
  kind: maintained
  label: Childrenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/childrenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chlorapatite
  path: data/records/chlorapatite.yaml
  kind: maintained
  label: Chlorapatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chlorapatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chromite
  path: data/records/chromite.yaml
  kind: maintained
  label: Chromite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chrysotile
  path: data/records/chrysotile.yaml
  kind: maintained
  label: Chrysotile
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chrysotile.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chukanovite
  path: data/records/chukanovite.yaml
  kind: maintained
  label: Chukanovite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chukanovite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:churchite-y
  path: data/records/churchite-y.yaml
  kind: maintained
  label: Churchite-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/churchite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cinnabar
  path: data/records/cinnabar.yaml
  kind: maintained
  label: Cinnabar
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cinnabar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cobaltite
  path: data/records/cobaltite.yaml
  kind: maintained
  label: Cobaltite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cobaltite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:coffinite
  path: data/records/coffinite.yaml
  kind: maintained
  label: Coffinite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coffinite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:colemanite
  path: data/records/colemanite.yaml
  kind: maintained
  label: Colemanite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/colemanite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:compreignacite
  path: data/records/compreignacite.yaml
  kind: maintained
  label: Compreignacite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/compreignacite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:coquimbite
  path: data/records/coquimbite.yaml
  kind: maintained
  label: Coquimbite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coquimbite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cordylite-ce
  path: data/records/cordylite-ce.yaml
  kind: maintained
  label: Cordylite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cordylite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:corkite
  path: data/records/corkite.yaml
  kind: maintained
  label: Corkite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/corkite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:covellite
  path: data/records/covellite.yaml
  kind: maintained
  label: Covellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/covellite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:crandallite
  path: data/records/crandallite.yaml
  kind: maintained
  label: Crandallite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/crandallite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cryptomelane
  path: data/records/cryptomelane.yaml
  kind: maintained
  label: Cryptomelane
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cryptomelane.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cuprite
  path: data/records/cuprite.yaml
  kind: maintained
  label: Cuprite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cuprite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cuprosklodowskite
  path: data/records/cuprosklodowskite.yaml
  kind: maintained
  label: Cuprosklodowskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cuprosklodowskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:curite
  path: data/records/curite.yaml
  kind: maintained
  label: Curite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/curite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:digenite
  path: data/records/digenite.yaml
  kind: maintained
  label: Digenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/digenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:diopside
  path: data/records/diopside.yaml
  kind: maintained
  label: Diopside
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/diopside.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:dittmarite
  path: data/records/dittmarite.yaml
  kind: maintained
  label: Dittmarite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dittmarite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:djurleite
  path: data/records/djurleite.yaml
  kind: maintained
  label: Djurleite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/djurleite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:dolomite
  path: data/records/dolomite.yaml
  kind: maintained
  label: Dolomite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dolomite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:donnayite-y
  path: data/records/donnayite-y.yaml
  kind: maintained
  label: Donnayite-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/donnayite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:dypingite
  path: data/records/dypingite.yaml
  kind: maintained
  label: Dypingite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dypingite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:dzhalindite
  path: data/records/dzhalindite.yaml
  kind: maintained
  label: Dzhalindite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dzhalindite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:elpidite
  path: data/records/elpidite.yaml
  kind: maintained
  label: Elpidite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/elpidite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:enstatite
  path: data/records/enstatite.yaml
  kind: maintained
  label: Enstatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/enstatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:eosphorite
  path: data/records/eosphorite.yaml
  kind: maintained
  label: Eosphorite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eosphorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:erythrite
  path: data/records/erythrite.yaml
  kind: maintained
  label: Erythrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/erythrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ezcurrite
  path: data/records/ezcurrite.yaml
  kind: maintained
  label: Ezcurrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ezcurrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:falottaite
  path: data/records/falottaite.yaml
  kind: maintained
  label: Falottaite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/falottaite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:feitknechtite
  path: data/records/feitknechtite.yaml
  kind: maintained
  label: Feitknechtite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/feitknechtite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:felsobanyaite
  path: data/records/felsobanyaite.yaml
  kind: maintained
  label: Felsőbányaite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/felsobanyaite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:feroxyhyte
  path: data/records/feroxyhyte.yaml
  kind: maintained
  label: Feroxyhyte
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/feroxyhyte.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ferricopiapite
  path: data/records/ferricopiapite.yaml
  kind: maintained
  label: Ferricopiapite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferricopiapite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ferrihydrite
  path: data/records/ferrihydrite.yaml
  kind: maintained
  label: Ferrihydrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrihydrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ferrokesterite
  path: data/records/ferrokesterite.yaml
  kind: maintained
  label: Ferrokësterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrokesterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:florencite-ce
  path: data/records/florencite-ce.yaml
  kind: maintained
  label: Florencite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/florencite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:florencite-la
  path: data/records/florencite-la.yaml
  kind: maintained
  label: Florencite-(La)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/florencite-la.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:fluorapatite
  path: data/records/fluorapatite.yaml
  kind: maintained
  label: Fluorapatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorapatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:fluorite
  path: data/records/fluorite.yaml
  kind: maintained
  label: Fluorite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:forsterite
  path: data/records/forsterite.yaml
  kind: maintained
  label: Forsterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/forsterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:fritzscheite
  path: data/records/fritzscheite.yaml
  kind: maintained
  label: Fritzscheite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fritzscheite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:galena
  path: data/records/galena.yaml
  kind: maintained
  label: Galena
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/galena.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:germanite
  path: data/records/germanite.yaml
  kind: maintained
  label: Germanite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/germanite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gersdorffite
  path: data/records/gersdorffite.yaml
  kind: maintained
  label: Gersdorffite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gersdorffite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gibbsite
  path: data/records/gibbsite.yaml
  kind: maintained
  label: Gibbsite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gibbsite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ginorite
  path: data/records/ginorite.yaml
  kind: maintained
  label: Ginorite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ginorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:glushinskite
  path: data/records/glushinskite.yaml
  kind: maintained
  label: Glushinskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/glushinskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:goethite
  path: data/records/goethite.yaml
  kind: maintained
  label: Goethite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/goethite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:goldmanite
  path: data/records/goldmanite.yaml
  kind: maintained
  label: Goldmanite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/goldmanite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gorceixite
  path: data/records/gorceixite.yaml
  kind: maintained
  label: Gorceixite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gorceixite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gowerite
  path: data/records/gowerite.yaml
  kind: maintained
  label: Gowerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gowerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:goyazite
  path: data/records/goyazite.yaml
  kind: maintained
  label: Goyazite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/goyazite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:greenockite
  path: data/records/greenockite.yaml
  kind: maintained
  label: Greenockite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/greenockite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:greigite
  path: data/records/greigite.yaml
  kind: maintained
  label: Greigite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/greigite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gypsum
  path: data/records/gypsum.yaml
  kind: maintained
  label: Gypsum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gypsum.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gysinite-nd
  path: data/records/gysinite-nd.yaml
  kind: maintained
  label: Gysinite-(Nd)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gysinite-nd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hafnon
  path: data/records/hafnon.yaml
  kind: maintained
  label: Hafnon
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hafnon.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hannayite
  path: data/records/hannayite.yaml
  kind: maintained
  label: Hannayite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hannayite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:haradaite
  path: data/records/haradaite.yaml
  kind: maintained
  label: Haradaite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/haradaite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hauerite
  path: data/records/hauerite.yaml
  kind: maintained
  label: Hauerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hauerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hausmannite
  path: data/records/hausmannite.yaml
  kind: maintained
  label: Hausmannite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hausmannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hawleyite
  path: data/records/hawleyite.yaml
  kind: maintained
  label: Hawleyite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hawleyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hazenite
  path: data/records/hazenite.yaml
  kind: maintained
  label: Hazenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hazenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:heazlewoodite
  path: data/records/heazlewoodite.yaml
  kind: maintained
  label: Heazlewoodite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heazlewoodite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hematite
  path: data/records/hematite.yaml
  kind: maintained
  label: Hematite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hematite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hemimorphite
  path: data/records/hemimorphite.yaml
  kind: maintained
  label: Hemimorphite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hemimorphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:heterogenite
  path: data/records/heterogenite.yaml
  kind: maintained
  label: Heterogenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heterogenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:heterosite
  path: data/records/heterosite.yaml
  kind: maintained
  label: Heterosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heterosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hollandite
  path: data/records/hollandite.yaml
  kind: maintained
  label: Hollandite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hollandite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hopeite
  path: data/records/hopeite.yaml
  kind: maintained
  label: Hopeite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hopeite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:humboldtine
  path: data/records/humboldtine.yaml
  kind: maintained
  label: Humboldtine
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/humboldtine.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:huntite
  path: data/records/huntite.yaml
  kind: maintained
  label: Huntite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/huntite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hureaulite
  path: data/records/hureaulite.yaml
  kind: maintained
  label: Hureaulite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hureaulite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydroboracite
  path: data/records/hydroboracite.yaml
  kind: maintained
  label: Hydroboracite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydroboracite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydrocerussite
  path: data/records/hydrocerussite.yaml
  kind: maintained
  label: Hydrocerussite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydrocerussite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydromagnesite
  path: data/records/hydromagnesite.yaml
  kind: maintained
  label: Hydromagnesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydromagnesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydroniumjarosite
  path: data/records/hydroniumjarosite.yaml
  kind: maintained
  label: Hydroniumjarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydroniumjarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydrotalcite
  path: data/records/hydrotalcite.yaml
  kind: maintained
  label: Hydrotalcite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydrotalcite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydroxylapatite
  path: data/records/hydroxylapatite.yaml
  kind: maintained
  label: Hydroxylapatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydroxylapatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydrozincite
  path: data/records/hydrozincite.yaml
  kind: maintained
  label: Hydrozincite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydrozincite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ilmenite
  path: data/records/ilmenite.yaml
  kind: maintained
  label: Ilmenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ilmenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:inderborite
  path: data/records/inderborite.yaml
  kind: maintained
  label: Inderborite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/inderborite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:inderite
  path: data/records/inderite.yaml
  kind: maintained
  label: Inderite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/inderite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:indite
  path: data/records/indite.yaml
  kind: maintained
  label: Indite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/indite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:inyoite
  path: data/records/inyoite.yaml
  kind: maintained
  label: Inyoite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/inyoite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:jadarite
  path: data/records/jadarite.yaml
  kind: maintained
  label: Jadarite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/jadarite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:jarosite
  path: data/records/jarosite.yaml
  kind: maintained
  label: Jarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/jarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kaliborite
  path: data/records/kaliborite.yaml
  kind: maintained
  label: Kaliborite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaliborite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kaolinite
  path: data/records/kaolinite.yaml
  kind: maintained
  label: Kaolinite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaolinite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:katsarosite
  path: data/records/katsarosite.yaml
  kind: maintained
  label: Katsarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kernite
  path: data/records/kernite.yaml
  kind: maintained
  label: Kernite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kernite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kesterite
  path: data/records/kesterite.yaml
  kind: maintained
  label: Kësterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kesterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kornelite
  path: data/records/kornelite.yaml
  kind: maintained
  label: Kornelite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kornelite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kozoite-la
  path: data/records/kozoite-la.yaml
  kind: maintained
  label: Kozoite-(La)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kozoite-la.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kozoite-nd
  path: data/records/kozoite-nd.yaml
  kind: maintained
  label: Kozoite-(Nd)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kozoite-nd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kukharenkoite-ce
  path: data/records/kukharenkoite-ce.yaml
  kind: maintained
  label: Kukharenkoite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kukharenkoite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kuliokite-y
  path: data/records/kuliokite-y.yaml
  kind: maintained
  label: Kuliokite-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kuliokite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kurnakovite
  path: data/records/kurnakovite.yaml
  kind: maintained
  label: Kurnakovite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kurnakovite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kutnohorite
  path: data/records/kutnohorite.yaml
  kind: maintained
  label: Kutnohorite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kutnohorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:laforetite
  path: data/records/laforetite.yaml
  kind: maintained
  label: Laforêtite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/laforetite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lansfordite
  path: data/records/lansfordite.yaml
  kind: maintained
  label: Lansfordite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lansfordite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lanthanite-ce
  path: data/records/lanthanite-ce.yaml
  kind: maintained
  label: Lanthanite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lanthanite-la
  path: data/records/lanthanite-la.yaml
  kind: maintained
  label: Lanthanite-(La)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanite-la.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lanthanite-nd
  path: data/records/lanthanite-nd.yaml
  kind: maintained
  label: Lanthanite-(Nd)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanite-nd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:larderellite
  path: data/records/larderellite.yaml
  kind: maintained
  label: Larderellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/larderellite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:laueite
  path: data/records/laueite.yaml
  kind: maintained
  label: Laueite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/laueite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lepidocrocite
  path: data/records/lepidocrocite.yaml
  kind: maintained
  label: Lepidocrocite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lepidocrocite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:libethenite
  path: data/records/libethenite.yaml
  kind: maintained
  label: Libethenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/libethenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lindbergite
  path: data/records/lindbergite.yaml
  kind: maintained
  label: Lindbergite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lindbergite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lithiophilite
  path: data/records/lithiophilite.yaml
  kind: maintained
  label: Lithiophilite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lithiophilite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lizardite
  path: data/records/lizardite.yaml
  kind: maintained
  label: Lizardite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lizardite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:loellingite
  path: data/records/loellingite.yaml
  kind: maintained
  label: Löllingite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/loellingite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lorenzenite
  path: data/records/lorenzenite.yaml
  kind: maintained
  label: Lorenzenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lorenzenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ludlamite
  path: data/records/ludlamite.yaml
  kind: maintained
  label: Ludlamite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ludlamite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:mackinawite
  path: data/records/mackinawite.yaml
  kind: maintained
  label: Mackinawite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/mackinawite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:maghemite
  path: data/records/maghemite.yaml
  kind: maintained
  label: Maghemite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/maghemite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:magnetite
  path: data/records/magnetite.yaml
  kind: maintained
  label: Magnetite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnetite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:malachite
  path: data/records/malachite.yaml
  kind: maintained
  label: Malachite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/malachite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:manganite
  path: data/records/manganite.yaml
  kind: maintained
  label: Manganite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:marcasite
  path: data/records/marcasite.yaml
  kind: maintained
  label: Marcasite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/marcasite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:mcallisterite
  path: data/records/mcallisterite.yaml
  kind: maintained
  label: Mcallisterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/mcallisterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:mckelveyite-y
  path: data/records/mckelveyite-y.yaml
  kind: maintained
  label: Mckelveyite-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/mckelveyite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:melanterite
  path: data/records/melanterite.yaml
  kind: maintained
  label: Melanterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/melanterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:meta-ankoleite
  path: data/records/meta-ankoleite.yaml
  kind: maintained
  label: Meta-ankoleite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/meta-ankoleite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metacinnabar
  path: data/records/metacinnabar.yaml
  kind: maintained
  label: Metacinnabar
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metaschoepite
  path: data/records/metaschoepite.yaml
  kind: maintained
  label: Metaschoepite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metaschoepite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metastudtite
  path: data/records/metastudtite.yaml
  kind: maintained
  label: Metastudtite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metastudtite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metatorbernite
  path: data/records/metatorbernite.yaml
  kind: maintained
  label: Metatorbernite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metatorbernite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metatyuyamunite
  path: data/records/metatyuyamunite.yaml
  kind: maintained
  label: Metatyuyamunite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metatyuyamunite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metavivianite
  path: data/records/metavivianite.yaml
  kind: maintained
  label: Metavivianite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metavivianite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metazeunerite
  path: data/records/metazeunerite.yaml
  kind: maintained
  label: Metazeunerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metazeunerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:meyerhofferite
  path: data/records/meyerhofferite.yaml
  kind: maintained
  label: Meyerhofferite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/meyerhofferite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:microcline
  path: data/records/microcline.yaml
  kind: maintained
  label: Microcline
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/microcline.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:millerite
  path: data/records/millerite.yaml
  kind: maintained
  label: Millerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/millerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:mimetite
  path: data/records/mimetite.yaml
  kind: maintained
  label: Mimetite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/mimetite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:molybdenite
  path: data/records/molybdenite.yaml
  kind: maintained
  label: Molybdenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/molybdenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monazite-ce
  path: data/records/monazite-ce.yaml
  kind: maintained
  label: Monazite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monazite-gd
  path: data/records/monazite-gd.yaml
  kind: maintained
  label: Monazite-(Gd)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-gd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monazite-la
  path: data/records/monazite-la.yaml
  kind: maintained
  label: Monazite-(La)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-la.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monazite-nd
  path: data/records/monazite-nd.yaml
  kind: maintained
  label: Monazite-(Nd)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-nd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monazite-sm
  path: data/records/monazite-sm.yaml
  kind: maintained
  label: Monazite-(Sm)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-sm.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monetite
  path: data/records/monetite.yaml
  kind: maintained
  label: Monetite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monetite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monohydrocalcite
  path: data/records/monohydrocalcite.yaml
  kind: maintained
  label: Monohydrocalcite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monohydrocalcite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:montebrasite
  path: data/records/montebrasite.yaml
  kind: maintained
  label: Montebrasite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/montebrasite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:montmorillonite
  path: data/records/montmorillonite.yaml
  kind: maintained
  label: Montmorillonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/montmorillonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:montroseite
  path: data/records/montroseite.yaml
  kind: maintained
  label: Montroseite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/montroseite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:moolooite
  path: data/records/moolooite.yaml
  kind: maintained
  label: Moolooite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/moolooite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:muscovite
  path: data/records/muscovite.yaml
  kind: maintained
  label: Muscovite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/muscovite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:natroboltwoodite
  path: data/records/natroboltwoodite.yaml
  kind: maintained
  label: Natroboltwoodite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/natroboltwoodite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:natrojarosite
  path: data/records/natrojarosite.yaml
  kind: maintained
  label: Natrojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/natrojarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:navajoite
  path: data/records/navajoite.yaml
  kind: maintained
  label: Navajoite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/navajoite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nepheline
  path: data/records/nepheline.yaml
  kind: maintained
  label: Nepheline
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nepheline.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nesquehonite
  path: data/records/nesquehonite.yaml
  kind: maintained
  label: Nesquehonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nesquehonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:newberyite
  path: data/records/newberyite.yaml
  kind: maintained
  label: Newberyite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/newberyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ningyoite
  path: data/records/ningyoite.yaml
  kind: maintained
  label: Ningyoite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ningyoite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nobleite
  path: data/records/nobleite.yaml
  kind: maintained
  label: Nobleite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nobleite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nontronite
  path: data/records/nontronite.yaml
  kind: maintained
  label: Nontronite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nontronite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:orpiment
  path: data/records/orpiment.yaml
  kind: maintained
  label: Orpiment
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/orpiment.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:orthoclase
  path: data/records/orthoclase.yaml
  kind: maintained
  label: Orthoclase
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/orthoclase.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:otavite
  path: data/records/otavite.yaml
  kind: maintained
  label: Otavite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/otavite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:palygorskite
  path: data/records/palygorskite.yaml
  kind: maintained
  label: Palygorskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/palygorskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:paracoquimbite
  path: data/records/paracoquimbite.yaml
  kind: maintained
  label: Paracoquimbite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/paracoquimbite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:paramontroseite
  path: data/records/paramontroseite.yaml
  kind: maintained
  label: Paramontroseite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/paramontroseite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:parasymplesite
  path: data/records/parasymplesite.yaml
  kind: maintained
  label: Parasymplesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/parasymplesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:parauranophane
  path: data/records/parauranophane.yaml
  kind: maintained
  label: Parauranophane
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/parauranophane.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pascoite
  path: data/records/pascoite.yaml
  kind: maintained
  label: Pascoite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pascoite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pentagonite
  path: data/records/pentagonite.yaml
  kind: maintained
  label: Pentagonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pentagonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pentlandite
  path: data/records/pentlandite.yaml
  kind: maintained
  label: Pentlandite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pentlandite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:perovskite
  path: data/records/perovskite.yaml
  kind: maintained
  label: Perovskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/perovskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pertlikite
  path: data/records/pertlikite.yaml
  kind: maintained
  label: Pertlikite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pertlikite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:petalite
  path: data/records/petalite.yaml
  kind: maintained
  label: Petalite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/petalite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:petrukite
  path: data/records/petrukite.yaml
  kind: maintained
  label: Petrukite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/petrukite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:phlogopite
  path: data/records/phlogopite.yaml
  kind: maintained
  label: Phlogopite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phlogopite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:phosphoferrite
  path: data/records/phosphoferrite.yaml
  kind: maintained
  label: Phosphoferrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphoferrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:phosphophyllite
  path: data/records/phosphophyllite.yaml
  kind: maintained
  label: Phosphophyllite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphophyllite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:piilonenite-nd
  path: data/records/piilonenite-nd.yaml
  kind: maintained
  label: Piilonenite-(Nd)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/piilonenite-nd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pinnoite
  path: data/records/pinnoite.yaml
  kind: maintained
  label: Pinnoite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pinnoite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:plumbojarosite
  path: data/records/plumbojarosite.yaml
  kind: maintained
  label: Plumbojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/plumbojarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:polydymite
  path: data/records/polydymite.yaml
  kind: maintained
  label: Polydymite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polydymite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:polylithionite
  path: data/records/polylithionite.yaml
  kind: maintained
  label: Polylithionite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polylithionite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:powellite
  path: data/records/powellite.yaml
  kind: maintained
  label: Powellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/powellite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:preobrazhenskite
  path: data/records/preobrazhenskite.yaml
  kind: maintained
  label: Preobrazhenskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/preobrazhenskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:priceite
  path: data/records/priceite.yaml
  kind: maintained
  label: Priceite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/priceite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:probertite
  path: data/records/probertite.yaml
  kind: maintained
  label: Probertite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/probertite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pyrite
  path: data/records/pyrite.yaml
  kind: maintained
  label: Pyrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pyroaurite
  path: data/records/pyroaurite.yaml
  kind: maintained
  label: Pyroaurite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyroaurite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pyrochroite
  path: data/records/pyrochroite.yaml
  kind: maintained
  label: Pyrochroite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrochroite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pyrolusite
  path: data/records/pyrolusite.yaml
  kind: maintained
  label: Pyrolusite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrolusite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pyromorphite
  path: data/records/pyromorphite.yaml
  kind: maintained
  label: Pyromorphite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyromorphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pyrrhotite
  path: data/records/pyrrhotite.yaml
  kind: maintained
  label: Pyrrhotite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrrhotite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:quenstedtite
  path: data/records/quenstedtite.yaml
  kind: maintained
  label: Quenstedtite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/quenstedtite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ramsdellite
  path: data/records/ramsdellite.yaml
  kind: maintained
  label: Ramsdellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ramsdellite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:realgar
  path: data/records/realgar.yaml
  kind: maintained
  label: Realgar
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/realgar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:regerite
  path: data/records/regerite.yaml
  kind: maintained
  label: Regerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/regerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:renierite
  path: data/records/renierite.yaml
  kind: maintained
  label: Renierite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/renierite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rhabdophane-ce
  path: data/records/rhabdophane-ce.yaml
  kind: maintained
  label: Rhabdophane-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhabdophane-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rhabdophane-la
  path: data/records/rhabdophane-la.yaml
  kind: maintained
  label: Rhabdophane-(La)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhabdophane-la.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rhodochrosite
  path: data/records/rhodochrosite.yaml
  kind: maintained
  label: Rhodochrosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhodochrosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rhomboclase
  path: data/records/rhomboclase.yaml
  kind: maintained
  label: Rhomboclase
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhomboclase.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:richetite
  path: data/records/richetite.yaml
  kind: maintained
  label: Richetite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/richetite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:riebeckite
  path: data/records/riebeckite.yaml
  kind: maintained
  label: Riebeckite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/riebeckite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rivadavite
  path: data/records/rivadavite.yaml
  kind: maintained
  label: Rivadavite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rivadavite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:romanechite
  path: data/records/romanechite.yaml
  kind: maintained
  label: Romanèchite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/romanechite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:roquesite
  path: data/records/roquesite.yaml
  kind: maintained
  label: Roquesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/roquesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:roscoelite
  path: data/records/roscoelite.yaml
  kind: maintained
  label: Roscoelite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/roscoelite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rozenite
  path: data/records/rozenite.yaml
  kind: maintained
  label: Rozenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rozenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rutherfordine
  path: data/records/rutherfordine.yaml
  kind: maintained
  label: Rutherfordine
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rutherfordine.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rutile
  path: data/records/rutile.yaml
  kind: maintained
  label: Rutile
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rutile.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sabugalite
  path: data/records/sabugalite.yaml
  kind: maintained
  label: Sabugalite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sabugalite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sakuraiite
  path: data/records/sakuraiite.yaml
  kind: maintained
  label: Sakuraiite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sakuraiite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:saleeite
  path: data/records/saleeite.yaml
  kind: maintained
  label: Saléeite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/saleeite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:saponite
  path: data/records/saponite.yaml
  kind: maintained
  label: Saponite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/saponite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sauconite
  path: data/records/sauconite.yaml
  kind: maintained
  label: Sauconite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sauconite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:scheelite
  path: data/records/scheelite.yaml
  kind: maintained
  label: Scheelite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scheelite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:schertelite
  path: data/records/schertelite.yaml
  kind: maintained
  label: Schertelite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/schertelite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:schoepite
  path: data/records/schoepite.yaml
  kind: maintained
  label: Schoepite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/schoepite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:schwertmannite
  path: data/records/schwertmannite.yaml
  kind: maintained
  label: Schwertmannite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/schwertmannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:scorodite
  path: data/records/scorodite.yaml
  kind: maintained
  label: Scorodite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scorodite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:senarmontite
  path: data/records/senarmontite.yaml
  kind: maintained
  label: Senarmontite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/senarmontite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sepiolite
  path: data/records/sepiolite.yaml
  kind: maintained
  label: Sepiolite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sepiolite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:siderite
  path: data/records/siderite.yaml
  kind: maintained
  label: Siderite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/siderite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:simonkolleite
  path: data/records/simonkolleite.yaml
  kind: maintained
  label: Simonkolleite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/simonkolleite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sklodowskite
  path: data/records/sklodowskite.yaml
  kind: maintained
  label: Sklodowskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sklodowskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:skutterudite
  path: data/records/skutterudite.yaml
  kind: maintained
  label: Skutterudite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/skutterudite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:smithsonite
  path: data/records/smithsonite.yaml
  kind: maintained
  label: Smithsonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/smithsonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:soddyite
  path: data/records/soddyite.yaml
  kind: maintained
  label: Soddyite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/soddyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sphalerite
  path: data/records/sphalerite.yaml
  kind: maintained
  label: Sphalerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sphalerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spodumene
  path: data/records/spodumene.yaml
  kind: maintained
  label: Spodumene
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spodumene.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:stannite
  path: data/records/stannite.yaml
  kind: maintained
  label: Stannite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/stannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:stevensite
  path: data/records/stevensite.yaml
  kind: maintained
  label: Stevensite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/stevensite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:stibnite
  path: data/records/stibnite.yaml
  kind: maintained
  label: Stibnite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/stibnite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:stolzite
  path: data/records/stolzite.yaml
  kind: maintained
  label: Stolzite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/stolzite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:strengite
  path: data/records/strengite.yaml
  kind: maintained
  label: Strengite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strengite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:strontianite
  path: data/records/strontianite.yaml
  kind: maintained
  label: Strontianite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:struvite
  path: data/records/struvite.yaml
  kind: maintained
  label: Struvite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/struvite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:struvite-k
  path: data/records/struvite-k.yaml
  kind: maintained
  label: Struvite-(K)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/struvite-k.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:studtite
  path: data/records/studtite.yaml
  kind: maintained
  label: Studtite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/studtite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sulfoborite
  path: data/records/sulfoborite.yaml
  kind: maintained
  label: Sulfoborite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sulfoborite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:svanbergite
  path: data/records/svanbergite.yaml
  kind: maintained
  label: Svanbergite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/svanbergite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:switzerite
  path: data/records/switzerite.yaml
  kind: maintained
  label: Switzerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/switzerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:synchysite-ce
  path: data/records/synchysite-ce.yaml
  kind: maintained
  label: Synchysite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/synchysite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:szaibelyite
  path: data/records/szaibelyite.yaml
  kind: maintained
  label: Szaibélyite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/szaibelyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:szomolnokite
  path: data/records/szomolnokite.yaml
  kind: maintained
  label: Szomolnokite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/szomolnokite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:talc
  path: data/records/talc.yaml
  kind: maintained
  label: Talc
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/talc.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tennantite-in
  path: data/records/tennantite-in.yaml
  kind: maintained
  label: Tennantite-(In)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tennantite-in.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tenorite
  path: data/records/tenorite.yaml
  kind: maintained
  label: Tenorite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tenorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:thomasclarkite-y
  path: data/records/thomasclarkite-y.yaml
  kind: maintained
  label: Thomasclarkite-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thomasclarkite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tincalconite
  path: data/records/tincalconite.yaml
  kind: maintained
  label: Tincalconite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tincalconite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:titanite
  path: data/records/titanite.yaml
  kind: maintained
  label: Titanite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:todorokite
  path: data/records/todorokite.yaml
  kind: maintained
  label: Todorokite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/todorokite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:torbernite
  path: data/records/torbernite.yaml
  kind: maintained
  label: Torbernite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/torbernite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:triphylite
  path: data/records/triphylite.yaml
  kind: maintained
  label: Triphylite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/triphylite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:troilite
  path: data/records/troilite.yaml
  kind: maintained
  label: Troilite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/troilite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tunellite
  path: data/records/tunellite.yaml
  kind: maintained
  label: Tunellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tunellite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ulexite
  path: data/records/ulexite.yaml
  kind: maintained
  label: Ulexite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ulexite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:uramphite
  path: data/records/uramphite.yaml
  kind: maintained
  label: Uramphite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uramphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:uraninite
  path: data/records/uraninite.yaml
  kind: maintained
  label: Uraninite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uraninite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:uranophane
  path: data/records/uranophane.yaml
  kind: maintained
  label: Uranophane
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uranophane.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:uranopilite
  path: data/records/uranopilite.yaml
  kind: maintained
  label: Uranopilite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uranopilite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vaesite
  path: data/records/vaesite.yaml
  kind: maintained
  label: Vaesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vaesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vandenbrandeite
  path: data/records/vandenbrandeite.yaml
  kind: maintained
  label: Vandenbrandeite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vandenbrandeite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:variscite
  path: data/records/variscite.yaml
  kind: maintained
  label: Variscite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/variscite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vaterite
  path: data/records/vaterite.yaml
  kind: maintained
  label: Vaterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vaterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:veatchite
  path: data/records/veatchite.yaml
  kind: maintained
  label: Veatchite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/veatchite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:violarite
  path: data/records/violarite.yaml
  kind: maintained
  label: Violarite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/violarite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vivianite
  path: data/records/vivianite.yaml
  kind: maintained
  label: Vivianite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vivianite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:voltaite
  path: data/records/voltaite.yaml
  kind: maintained
  label: Voltaite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/voltaite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:weddellite
  path: data/records/weddellite.yaml
  kind: maintained
  label: Weddellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/weddellite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:weeksite
  path: data/records/weeksite.yaml
  kind: maintained
  label: Weeksite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/weeksite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:wheatleyite
  path: data/records/wheatleyite.yaml
  kind: maintained
  label: Wheatleyite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wheatleyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:whewellite
  path: data/records/whewellite.yaml
  kind: maintained
  label: Whewellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/whewellite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:whitlockite
  path: data/records/whitlockite.yaml
  kind: maintained
  label: Whitlockite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/whitlockite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:willemite
  path: data/records/willemite.yaml
  kind: maintained
  label: Willemite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/willemite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:wollastonite
  path: data/records/wollastonite.yaml
  kind: maintained
  label: Wollastonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wollastonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:woodhouseite
  path: data/records/woodhouseite.yaml
  kind: maintained
  label: Woodhouseite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/woodhouseite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:wulfenite
  path: data/records/wulfenite.yaml
  kind: maintained
  label: Wulfenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wulfenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:wurtzite
  path: data/records/wurtzite.yaml
  kind: maintained
  label: Wurtzite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wurtzite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:xenotime-gd
  path: data/records/xenotime-gd.yaml
  kind: maintained
  label: Xenotime-(Gd)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-gd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:xenotime-y
  path: data/records/xenotime-y.yaml
  kind: maintained
  label: Xenotime-(Y)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:xenotime-yb
  path: data/records/xenotime-yb.yaml
  kind: maintained
  label: Xenotime-(Yb)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-yb.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:yanomamite
  path: data/records/yanomamite.yaml
  kind: maintained
  label: Yanomamite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/yanomamite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:yusupovite
  path: data/records/yusupovite.yaml
  kind: maintained
  label: Yusupovite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/yusupovite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zeunerite
  path: data/records/zeunerite.yaml
  kind: maintained
  label: Zeunerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zeunerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zincite
  path: data/records/zincite.yaml
  kind: maintained
  label: Zincite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zincite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zincobriartite
  path: data/records/zincobriartite.yaml
  kind: maintained
  label: Zincobriartite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zincobriartite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zippeite
  path: data/records/zippeite.yaml
  kind: maintained
  label: Zippeite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zippeite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zircon
  path: data/records/zircon.yaml
  kind: maintained
  label: Zircon
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zircon.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zirconolite
  path: data/records/zirconolite.yaml
  kind: maintained
  label: Zirconolite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zirconolite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-cohort
  name: cmmmech validate (mineral cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:acanthite
  - cmmmech:adamsite-y
  - cmmmech:akaganeite
  - cmmmech:alabandite
  - cmmmech:albite
  - cmmmech:alburnite
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:alunite
  - cmmmech:amblygonite
  - cmmmech:ameghinite
  - cmmmech:ammonioborite
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:ancylite-ce
  - cmmmech:andersonite
  - cmmmech:anglesite
  - cmmmech:anhydrite
  - cmmmech:anilite
  - cmmmech:annabergite
  - cmmmech:anorthite
  - cmmmech:aragonite
  - cmmmech:argentojarosite
  - cmmmech:argyrodite
  - cmmmech:aristarainite
  - cmmmech:arsenopyrite
  - cmmmech:artinite
  - cmmmech:asbolane
  - cmmmech:atacamite
  - cmmmech:autunite
  - cmmmech:azurite
  - cmmmech:baddeleyite
  - cmmmech:bainbridgeite-ndce
  - cmmmech:bainbridgeite-yce
  - cmmmech:baricite
  - cmmmech:bassanite
  - cmmmech:becquerelite
  - cmmmech:beudantite
  - cmmmech:billietite
  - cmmmech:birnessite
  - cmmmech:bismuthinite
  - cmmmech:bixbyite-mn
  - cmmmech:bobierrite
  - cmmmech:boehmite
  - cmmmech:boltwoodite
  - cmmmech:boracite
  - cmmmech:borax
  - cmmmech:bornite
  - cmmmech:briartite
  - cmmmech:brochantite
  - cmmmech:brookite
  - cmmmech:brucite
  - cmmmech:brushite
  - cmmmech:burbankite
  - cmmmech:cadmoindite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:calcioveatchite
  - cmmmech:calcite
  - cmmmech:carnotite
  - cmmmech:carrollite
  - cmmmech:cassiterite
  - cmmmech:catapleiite
  - cmmmech:cattiite
  - cmmmech:cavansite
  - cmmmech:caysichite-y
  - cmmmech:celestine
  - cmmmech:cerianite-ce
  - cmmmech:cerussite
  - cmmmech:chalcocite
  - cmmmech:chalcopyrite
  - cmmmech:chernikovite
  - cmmmech:childrenite
  - cmmmech:chlorapatite
  - cmmmech:chromite
  - cmmmech:chrysotile
  - cmmmech:chukanovite
  - cmmmech:churchite-y
  - cmmmech:cinnabar
  - cmmmech:cobaltite
  - cmmmech:coffinite
  - cmmmech:colemanite
  - cmmmech:compreignacite
  - cmmmech:coquimbite
  - cmmmech:cordylite-ce
  - cmmmech:corkite
  - cmmmech:covellite
  - cmmmech:crandallite
  - cmmmech:cryptomelane
  - cmmmech:cuprite
  - cmmmech:cuprosklodowskite
  - cmmmech:curite
  - cmmmech:digenite
  - cmmmech:diopside
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:dypingite
  - cmmmech:dzhalindite
  - cmmmech:elpidite
  - cmmmech:enstatite
  - cmmmech:eosphorite
  - cmmmech:erythrite
  - cmmmech:ezcurrite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:felsobanyaite
  - cmmmech:feroxyhyte
  - cmmmech:ferricopiapite
  - cmmmech:ferrihydrite
  - cmmmech:ferrokesterite
  - cmmmech:florencite-ce
  - cmmmech:florencite-la
  - cmmmech:fluorapatite
  - cmmmech:fluorite
  - cmmmech:forsterite
  - cmmmech:fritzscheite
  - cmmmech:galena
  - cmmmech:germanite
  - cmmmech:gersdorffite
  - cmmmech:gibbsite
  - cmmmech:ginorite
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:goldmanite
  - cmmmech:gorceixite
  - cmmmech:gowerite
  - cmmmech:goyazite
  - cmmmech:greenockite
  - cmmmech:greigite
  - cmmmech:gypsum
  - cmmmech:gysinite-nd
  - cmmmech:hafnon
  - cmmmech:hannayite
  - cmmmech:haradaite
  - cmmmech:hauerite
  - cmmmech:hausmannite
  - cmmmech:hawleyite
  - cmmmech:hazenite
  - cmmmech:heazlewoodite
  - cmmmech:hematite
  - cmmmech:hemimorphite
  - cmmmech:heterogenite
  - cmmmech:heterosite
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:huntite
  - cmmmech:hureaulite
  - cmmmech:hydroboracite
  - cmmmech:hydrocerussite
  - cmmmech:hydromagnesite
  - cmmmech:hydroniumjarosite
  - cmmmech:hydrotalcite
  - cmmmech:hydroxylapatite
  - cmmmech:hydrozincite
  - cmmmech:ilmenite
  - cmmmech:inderborite
  - cmmmech:inderite
  - cmmmech:indite
  - cmmmech:inyoite
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaliborite
  - cmmmech:kaolinite
  - cmmmech:katsarosite
  - cmmmech:kernite
  - cmmmech:kesterite
  - cmmmech:kornelite
  - cmmmech:kozoite-la
  - cmmmech:kozoite-nd
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:kurnakovite
  - cmmmech:kutnohorite
  - cmmmech:laforetite
  - cmmmech:lansfordite
  - cmmmech:lanthanite-ce
  - cmmmech:lanthanite-la
  - cmmmech:lanthanite-nd
  - cmmmech:larderellite
  - cmmmech:laueite
  - cmmmech:lepidocrocite
  - cmmmech:libethenite
  - cmmmech:lindbergite
  - cmmmech:lithiophilite
  - cmmmech:lizardite
  - cmmmech:loellingite
  - cmmmech:lorenzenite
  - cmmmech:ludlamite
  - cmmmech:mackinawite
  - cmmmech:maghemite
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:mcallisterite
  - cmmmech:mckelveyite-y
  - cmmmech:melanterite
  - cmmmech:meta-ankoleite
  - cmmmech:metacinnabar
  - cmmmech:metaschoepite
  - cmmmech:metastudtite
  - cmmmech:metatorbernite
  - cmmmech:metatyuyamunite
  - cmmmech:metavivianite
  - cmmmech:metazeunerite
  - cmmmech:meyerhofferite
  - cmmmech:microcline
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:monazite-ce
  - cmmmech:monazite-gd
  - cmmmech:monazite-la
  - cmmmech:monazite-nd
  - cmmmech:monazite-sm
  - cmmmech:monetite
  - cmmmech:monohydrocalcite
  - cmmmech:montebrasite
  - cmmmech:montmorillonite
  - cmmmech:montroseite
  - cmmmech:moolooite
  - cmmmech:muscovite
  - cmmmech:natroboltwoodite
  - cmmmech:natrojarosite
  - cmmmech:navajoite
  - cmmmech:nepheline
  - cmmmech:nesquehonite
  - cmmmech:newberyite
  - cmmmech:ningyoite
  - cmmmech:nobleite
  - cmmmech:nontronite
  - cmmmech:orpiment
  - cmmmech:orthoclase
  - cmmmech:otavite
  - cmmmech:palygorskite
  - cmmmech:paracoquimbite
  - cmmmech:paramontroseite
  - cmmmech:parasymplesite
  - cmmmech:parauranophane
  - cmmmech:pascoite
  - cmmmech:pentagonite
  - cmmmech:pentlandite
  - cmmmech:perovskite
  - cmmmech:pertlikite
  - cmmmech:petalite
  - cmmmech:petrukite
  - cmmmech:phlogopite
  - cmmmech:phosphoferrite
  - cmmmech:phosphophyllite
  - cmmmech:piilonenite-nd
  - cmmmech:pinnoite
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:polylithionite
  - cmmmech:powellite
  - cmmmech:preobrazhenskite
  - cmmmech:priceite
  - cmmmech:probertite
  - cmmmech:pyrite
  - cmmmech:pyroaurite
  - cmmmech:pyrochroite
  - cmmmech:pyrolusite
  - cmmmech:pyromorphite
  - cmmmech:pyrrhotite
  - cmmmech:quenstedtite
  - cmmmech:ramsdellite
  - cmmmech:realgar
  - cmmmech:regerite
  - cmmmech:renierite
  - cmmmech:rhabdophane-ce
  - cmmmech:rhabdophane-la
  - cmmmech:rhodochrosite
  - cmmmech:rhomboclase
  - cmmmech:richetite
  - cmmmech:riebeckite
  - cmmmech:rivadavite
  - cmmmech:romanechite
  - cmmmech:roquesite
  - cmmmech:roscoelite
  - cmmmech:rozenite
  - cmmmech:rutherfordine
  - cmmmech:rutile
  - cmmmech:sabugalite
  - cmmmech:sakuraiite
  - cmmmech:saleeite
  - cmmmech:saponite
  - cmmmech:sauconite
  - cmmmech:scheelite
  - cmmmech:schertelite
  - cmmmech:schoepite
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:senarmontite
  - cmmmech:sepiolite
  - cmmmech:siderite
  - cmmmech:simonkolleite
  - cmmmech:sklodowskite
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:soddyite
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:stevensite
  - cmmmech:stibnite
  - cmmmech:stolzite
  - cmmmech:strengite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:struvite-k
  - cmmmech:studtite
  - cmmmech:sulfoborite
  - cmmmech:svanbergite
  - cmmmech:switzerite
  - cmmmech:synchysite-ce
  - cmmmech:szaibelyite
  - cmmmech:szomolnokite
  - cmmmech:talc
  - cmmmech:tennantite-in
  - cmmmech:tenorite
  - cmmmech:thomasclarkite-y
  - cmmmech:tincalconite
  - cmmmech:titanite
  - cmmmech:todorokite
  - cmmmech:torbernite
  - cmmmech:triphylite
  - cmmmech:troilite
  - cmmmech:tunellite
  - cmmmech:ulexite
  - cmmmech:uramphite
  - cmmmech:uraninite
  - cmmmech:uranophane
  - cmmmech:uranopilite
  - cmmmech:vaesite
  - cmmmech:vandenbrandeite
  - cmmmech:variscite
  - cmmmech:vaterite
  - cmmmech:veatchite
  - cmmmech:violarite
  - cmmmech:vivianite
  - cmmmech:voltaite
  - cmmmech:weddellite
  - cmmmech:weeksite
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:whitlockite
  - cmmmech:willemite
  - cmmmech:wollastonite
  - cmmmech:woodhouseite
  - cmmmech:wulfenite
  - cmmmech:wurtzite
  - cmmmech:xenotime-gd
  - cmmmech:xenotime-y
  - cmmmech:xenotime-yb
  - cmmmech:yanomamite
  - cmmmech:yusupovite
  - cmmmech:zeunerite
  - cmmmech:zincite
  - cmmmech:zincobriartite
  - cmmmech:zippeite
  - cmmmech:zircon
  - cmmmech:zirconolite
  evidence_ids:
  - ev-cmmmech-validate
  summary: All 365 records in the mineral cohort pass LinkML structural and semantic
    validation with 0 errors.
- check_id: cmmmech-validate-history-cohort
  name: cmmmech validate-history (mineral cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:acanthite
  - cmmmech:adamsite-y
  - cmmmech:akaganeite
  - cmmmech:alabandite
  - cmmmech:albite
  - cmmmech:alburnite
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:alunite
  - cmmmech:amblygonite
  - cmmmech:ameghinite
  - cmmmech:ammonioborite
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:ancylite-ce
  - cmmmech:andersonite
  - cmmmech:anglesite
  - cmmmech:anhydrite
  - cmmmech:anilite
  - cmmmech:annabergite
  - cmmmech:anorthite
  - cmmmech:aragonite
  - cmmmech:argentojarosite
  - cmmmech:argyrodite
  - cmmmech:aristarainite
  - cmmmech:arsenopyrite
  - cmmmech:artinite
  - cmmmech:asbolane
  - cmmmech:atacamite
  - cmmmech:autunite
  - cmmmech:azurite
  - cmmmech:baddeleyite
  - cmmmech:bainbridgeite-ndce
  - cmmmech:bainbridgeite-yce
  - cmmmech:baricite
  - cmmmech:bassanite
  - cmmmech:becquerelite
  - cmmmech:beudantite
  - cmmmech:billietite
  - cmmmech:birnessite
  - cmmmech:bismuthinite
  - cmmmech:bixbyite-mn
  - cmmmech:bobierrite
  - cmmmech:boehmite
  - cmmmech:boltwoodite
  - cmmmech:boracite
  - cmmmech:borax
  - cmmmech:bornite
  - cmmmech:briartite
  - cmmmech:brochantite
  - cmmmech:brookite
  - cmmmech:brucite
  - cmmmech:brushite
  - cmmmech:burbankite
  - cmmmech:cadmoindite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:calcioveatchite
  - cmmmech:calcite
  - cmmmech:carnotite
  - cmmmech:carrollite
  - cmmmech:cassiterite
  - cmmmech:catapleiite
  - cmmmech:cattiite
  - cmmmech:cavansite
  - cmmmech:caysichite-y
  - cmmmech:celestine
  - cmmmech:cerianite-ce
  - cmmmech:cerussite
  - cmmmech:chalcocite
  - cmmmech:chalcopyrite
  - cmmmech:chernikovite
  - cmmmech:childrenite
  - cmmmech:chlorapatite
  - cmmmech:chromite
  - cmmmech:chrysotile
  - cmmmech:chukanovite
  - cmmmech:churchite-y
  - cmmmech:cinnabar
  - cmmmech:cobaltite
  - cmmmech:coffinite
  - cmmmech:colemanite
  - cmmmech:compreignacite
  - cmmmech:coquimbite
  - cmmmech:cordylite-ce
  - cmmmech:corkite
  - cmmmech:covellite
  - cmmmech:crandallite
  - cmmmech:cryptomelane
  - cmmmech:cuprite
  - cmmmech:cuprosklodowskite
  - cmmmech:curite
  - cmmmech:digenite
  - cmmmech:diopside
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:dypingite
  - cmmmech:dzhalindite
  - cmmmech:elpidite
  - cmmmech:enstatite
  - cmmmech:eosphorite
  - cmmmech:erythrite
  - cmmmech:ezcurrite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:felsobanyaite
  - cmmmech:feroxyhyte
  - cmmmech:ferricopiapite
  - cmmmech:ferrihydrite
  - cmmmech:ferrokesterite
  - cmmmech:florencite-ce
  - cmmmech:florencite-la
  - cmmmech:fluorapatite
  - cmmmech:fluorite
  - cmmmech:forsterite
  - cmmmech:fritzscheite
  - cmmmech:galena
  - cmmmech:germanite
  - cmmmech:gersdorffite
  - cmmmech:gibbsite
  - cmmmech:ginorite
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:goldmanite
  - cmmmech:gorceixite
  - cmmmech:gowerite
  - cmmmech:goyazite
  - cmmmech:greenockite
  - cmmmech:greigite
  - cmmmech:gypsum
  - cmmmech:gysinite-nd
  - cmmmech:hafnon
  - cmmmech:hannayite
  - cmmmech:haradaite
  - cmmmech:hauerite
  - cmmmech:hausmannite
  - cmmmech:hawleyite
  - cmmmech:hazenite
  - cmmmech:heazlewoodite
  - cmmmech:hematite
  - cmmmech:hemimorphite
  - cmmmech:heterogenite
  - cmmmech:heterosite
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:huntite
  - cmmmech:hureaulite
  - cmmmech:hydroboracite
  - cmmmech:hydrocerussite
  - cmmmech:hydromagnesite
  - cmmmech:hydroniumjarosite
  - cmmmech:hydrotalcite
  - cmmmech:hydroxylapatite
  - cmmmech:hydrozincite
  - cmmmech:ilmenite
  - cmmmech:inderborite
  - cmmmech:inderite
  - cmmmech:indite
  - cmmmech:inyoite
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaliborite
  - cmmmech:kaolinite
  - cmmmech:katsarosite
  - cmmmech:kernite
  - cmmmech:kesterite
  - cmmmech:kornelite
  - cmmmech:kozoite-la
  - cmmmech:kozoite-nd
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:kurnakovite
  - cmmmech:kutnohorite
  - cmmmech:laforetite
  - cmmmech:lansfordite
  - cmmmech:lanthanite-ce
  - cmmmech:lanthanite-la
  - cmmmech:lanthanite-nd
  - cmmmech:larderellite
  - cmmmech:laueite
  - cmmmech:lepidocrocite
  - cmmmech:libethenite
  - cmmmech:lindbergite
  - cmmmech:lithiophilite
  - cmmmech:lizardite
  - cmmmech:loellingite
  - cmmmech:lorenzenite
  - cmmmech:ludlamite
  - cmmmech:mackinawite
  - cmmmech:maghemite
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:mcallisterite
  - cmmmech:mckelveyite-y
  - cmmmech:melanterite
  - cmmmech:meta-ankoleite
  - cmmmech:metacinnabar
  - cmmmech:metaschoepite
  - cmmmech:metastudtite
  - cmmmech:metatorbernite
  - cmmmech:metatyuyamunite
  - cmmmech:metavivianite
  - cmmmech:metazeunerite
  - cmmmech:meyerhofferite
  - cmmmech:microcline
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:monazite-ce
  - cmmmech:monazite-gd
  - cmmmech:monazite-la
  - cmmmech:monazite-nd
  - cmmmech:monazite-sm
  - cmmmech:monetite
  - cmmmech:monohydrocalcite
  - cmmmech:montebrasite
  - cmmmech:montmorillonite
  - cmmmech:montroseite
  - cmmmech:moolooite
  - cmmmech:muscovite
  - cmmmech:natroboltwoodite
  - cmmmech:natrojarosite
  - cmmmech:navajoite
  - cmmmech:nepheline
  - cmmmech:nesquehonite
  - cmmmech:newberyite
  - cmmmech:ningyoite
  - cmmmech:nobleite
  - cmmmech:nontronite
  - cmmmech:orpiment
  - cmmmech:orthoclase
  - cmmmech:otavite
  - cmmmech:palygorskite
  - cmmmech:paracoquimbite
  - cmmmech:paramontroseite
  - cmmmech:parasymplesite
  - cmmmech:parauranophane
  - cmmmech:pascoite
  - cmmmech:pentagonite
  - cmmmech:pentlandite
  - cmmmech:perovskite
  - cmmmech:pertlikite
  - cmmmech:petalite
  - cmmmech:petrukite
  - cmmmech:phlogopite
  - cmmmech:phosphoferrite
  - cmmmech:phosphophyllite
  - cmmmech:piilonenite-nd
  - cmmmech:pinnoite
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:polylithionite
  - cmmmech:powellite
  - cmmmech:preobrazhenskite
  - cmmmech:priceite
  - cmmmech:probertite
  - cmmmech:pyrite
  - cmmmech:pyroaurite
  - cmmmech:pyrochroite
  - cmmmech:pyrolusite
  - cmmmech:pyromorphite
  - cmmmech:pyrrhotite
  - cmmmech:quenstedtite
  - cmmmech:ramsdellite
  - cmmmech:realgar
  - cmmmech:regerite
  - cmmmech:renierite
  - cmmmech:rhabdophane-ce
  - cmmmech:rhabdophane-la
  - cmmmech:rhodochrosite
  - cmmmech:rhomboclase
  - cmmmech:richetite
  - cmmmech:riebeckite
  - cmmmech:rivadavite
  - cmmmech:romanechite
  - cmmmech:roquesite
  - cmmmech:roscoelite
  - cmmmech:rozenite
  - cmmmech:rutherfordine
  - cmmmech:rutile
  - cmmmech:sabugalite
  - cmmmech:sakuraiite
  - cmmmech:saleeite
  - cmmmech:saponite
  - cmmmech:sauconite
  - cmmmech:scheelite
  - cmmmech:schertelite
  - cmmmech:schoepite
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:senarmontite
  - cmmmech:sepiolite
  - cmmmech:siderite
  - cmmmech:simonkolleite
  - cmmmech:sklodowskite
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:soddyite
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:stevensite
  - cmmmech:stibnite
  - cmmmech:stolzite
  - cmmmech:strengite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:struvite-k
  - cmmmech:studtite
  - cmmmech:sulfoborite
  - cmmmech:svanbergite
  - cmmmech:switzerite
  - cmmmech:synchysite-ce
  - cmmmech:szaibelyite
  - cmmmech:szomolnokite
  - cmmmech:talc
  - cmmmech:tennantite-in
  - cmmmech:tenorite
  - cmmmech:thomasclarkite-y
  - cmmmech:tincalconite
  - cmmmech:titanite
  - cmmmech:todorokite
  - cmmmech:torbernite
  - cmmmech:triphylite
  - cmmmech:troilite
  - cmmmech:tunellite
  - cmmmech:ulexite
  - cmmmech:uramphite
  - cmmmech:uraninite
  - cmmmech:uranophane
  - cmmmech:uranopilite
  - cmmmech:vaesite
  - cmmmech:vandenbrandeite
  - cmmmech:variscite
  - cmmmech:vaterite
  - cmmmech:veatchite
  - cmmmech:violarite
  - cmmmech:vivianite
  - cmmmech:voltaite
  - cmmmech:weddellite
  - cmmmech:weeksite
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:whitlockite
  - cmmmech:willemite
  - cmmmech:wollastonite
  - cmmmech:woodhouseite
  - cmmmech:wulfenite
  - cmmmech:wurtzite
  - cmmmech:xenotime-gd
  - cmmmech:xenotime-y
  - cmmmech:xenotime-yb
  - cmmmech:yanomamite
  - cmmmech:yusupovite
  - cmmmech:zeunerite
  - cmmmech:zincite
  - cmmmech:zincobriartite
  - cmmmech:zippeite
  - cmmmech:zircon
  - cmmmech:zirconolite
  evidence_ids:
  - ev-cmmmech-history
  summary: All curation_history entries and history_refs sidecars across the 365 mineral
    records resolve and validate cleanly.
- check_id: curie-label-consistency-cohort
  name: Ontology ID-label consistency (mineral cohort)
  status: passed
  required: true
  target_ids:
  - cmmmech:acanthite
  - cmmmech:adamsite-y
  - cmmmech:akaganeite
  - cmmmech:alabandite
  - cmmmech:albite
  - cmmmech:alburnite
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:alunite
  - cmmmech:amblygonite
  - cmmmech:ameghinite
  - cmmmech:ammonioborite
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:ancylite-ce
  - cmmmech:andersonite
  - cmmmech:anglesite
  - cmmmech:anhydrite
  - cmmmech:anilite
  - cmmmech:annabergite
  - cmmmech:anorthite
  - cmmmech:aragonite
  - cmmmech:argentojarosite
  - cmmmech:argyrodite
  - cmmmech:aristarainite
  - cmmmech:arsenopyrite
  - cmmmech:artinite
  - cmmmech:asbolane
  - cmmmech:atacamite
  - cmmmech:autunite
  - cmmmech:azurite
  - cmmmech:baddeleyite
  - cmmmech:bainbridgeite-ndce
  - cmmmech:bainbridgeite-yce
  - cmmmech:baricite
  - cmmmech:bassanite
  - cmmmech:becquerelite
  - cmmmech:beudantite
  - cmmmech:billietite
  - cmmmech:birnessite
  - cmmmech:bismuthinite
  - cmmmech:bixbyite-mn
  - cmmmech:bobierrite
  - cmmmech:boehmite
  - cmmmech:boltwoodite
  - cmmmech:boracite
  - cmmmech:borax
  - cmmmech:bornite
  - cmmmech:briartite
  - cmmmech:brochantite
  - cmmmech:brookite
  - cmmmech:brucite
  - cmmmech:brushite
  - cmmmech:burbankite
  - cmmmech:cadmoindite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:calcioveatchite
  - cmmmech:calcite
  - cmmmech:carnotite
  - cmmmech:carrollite
  - cmmmech:cassiterite
  - cmmmech:catapleiite
  - cmmmech:cattiite
  - cmmmech:cavansite
  - cmmmech:caysichite-y
  - cmmmech:celestine
  - cmmmech:cerianite-ce
  - cmmmech:cerussite
  - cmmmech:chalcocite
  - cmmmech:chalcopyrite
  - cmmmech:chernikovite
  - cmmmech:childrenite
  - cmmmech:chlorapatite
  - cmmmech:chromite
  - cmmmech:chrysotile
  - cmmmech:chukanovite
  - cmmmech:churchite-y
  - cmmmech:cinnabar
  - cmmmech:cobaltite
  - cmmmech:coffinite
  - cmmmech:colemanite
  - cmmmech:compreignacite
  - cmmmech:coquimbite
  - cmmmech:cordylite-ce
  - cmmmech:corkite
  - cmmmech:covellite
  - cmmmech:crandallite
  - cmmmech:cryptomelane
  - cmmmech:cuprite
  - cmmmech:cuprosklodowskite
  - cmmmech:curite
  - cmmmech:digenite
  - cmmmech:diopside
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:dypingite
  - cmmmech:dzhalindite
  - cmmmech:elpidite
  - cmmmech:enstatite
  - cmmmech:eosphorite
  - cmmmech:erythrite
  - cmmmech:ezcurrite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:felsobanyaite
  - cmmmech:feroxyhyte
  - cmmmech:ferricopiapite
  - cmmmech:ferrihydrite
  - cmmmech:ferrokesterite
  - cmmmech:florencite-ce
  - cmmmech:florencite-la
  - cmmmech:fluorapatite
  - cmmmech:fluorite
  - cmmmech:forsterite
  - cmmmech:fritzscheite
  - cmmmech:galena
  - cmmmech:germanite
  - cmmmech:gersdorffite
  - cmmmech:gibbsite
  - cmmmech:ginorite
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:goldmanite
  - cmmmech:gorceixite
  - cmmmech:gowerite
  - cmmmech:goyazite
  - cmmmech:greenockite
  - cmmmech:greigite
  - cmmmech:gypsum
  - cmmmech:gysinite-nd
  - cmmmech:hafnon
  - cmmmech:hannayite
  - cmmmech:haradaite
  - cmmmech:hauerite
  - cmmmech:hausmannite
  - cmmmech:hawleyite
  - cmmmech:hazenite
  - cmmmech:heazlewoodite
  - cmmmech:hematite
  - cmmmech:hemimorphite
  - cmmmech:heterogenite
  - cmmmech:heterosite
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:huntite
  - cmmmech:hureaulite
  - cmmmech:hydroboracite
  - cmmmech:hydrocerussite
  - cmmmech:hydromagnesite
  - cmmmech:hydroniumjarosite
  - cmmmech:hydrotalcite
  - cmmmech:hydroxylapatite
  - cmmmech:hydrozincite
  - cmmmech:ilmenite
  - cmmmech:inderborite
  - cmmmech:inderite
  - cmmmech:indite
  - cmmmech:inyoite
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaliborite
  - cmmmech:kaolinite
  - cmmmech:katsarosite
  - cmmmech:kernite
  - cmmmech:kesterite
  - cmmmech:kornelite
  - cmmmech:kozoite-la
  - cmmmech:kozoite-nd
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:kurnakovite
  - cmmmech:kutnohorite
  - cmmmech:laforetite
  - cmmmech:lansfordite
  - cmmmech:lanthanite-ce
  - cmmmech:lanthanite-la
  - cmmmech:lanthanite-nd
  - cmmmech:larderellite
  - cmmmech:laueite
  - cmmmech:lepidocrocite
  - cmmmech:libethenite
  - cmmmech:lindbergite
  - cmmmech:lithiophilite
  - cmmmech:lizardite
  - cmmmech:loellingite
  - cmmmech:lorenzenite
  - cmmmech:ludlamite
  - cmmmech:mackinawite
  - cmmmech:maghemite
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:mcallisterite
  - cmmmech:mckelveyite-y
  - cmmmech:melanterite
  - cmmmech:meta-ankoleite
  - cmmmech:metacinnabar
  - cmmmech:metaschoepite
  - cmmmech:metastudtite
  - cmmmech:metatorbernite
  - cmmmech:metatyuyamunite
  - cmmmech:metavivianite
  - cmmmech:metazeunerite
  - cmmmech:meyerhofferite
  - cmmmech:microcline
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:monazite-ce
  - cmmmech:monazite-gd
  - cmmmech:monazite-la
  - cmmmech:monazite-nd
  - cmmmech:monazite-sm
  - cmmmech:monetite
  - cmmmech:monohydrocalcite
  - cmmmech:montebrasite
  - cmmmech:montmorillonite
  - cmmmech:montroseite
  - cmmmech:moolooite
  - cmmmech:muscovite
  - cmmmech:natroboltwoodite
  - cmmmech:natrojarosite
  - cmmmech:navajoite
  - cmmmech:nepheline
  - cmmmech:nesquehonite
  - cmmmech:newberyite
  - cmmmech:ningyoite
  - cmmmech:nobleite
  - cmmmech:nontronite
  - cmmmech:orpiment
  - cmmmech:orthoclase
  - cmmmech:otavite
  - cmmmech:palygorskite
  - cmmmech:paracoquimbite
  - cmmmech:paramontroseite
  - cmmmech:parasymplesite
  - cmmmech:parauranophane
  - cmmmech:pascoite
  - cmmmech:pentagonite
  - cmmmech:pentlandite
  - cmmmech:perovskite
  - cmmmech:pertlikite
  - cmmmech:petalite
  - cmmmech:petrukite
  - cmmmech:phlogopite
  - cmmmech:phosphoferrite
  - cmmmech:phosphophyllite
  - cmmmech:piilonenite-nd
  - cmmmech:pinnoite
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:polylithionite
  - cmmmech:powellite
  - cmmmech:preobrazhenskite
  - cmmmech:priceite
  - cmmmech:probertite
  - cmmmech:pyrite
  - cmmmech:pyroaurite
  - cmmmech:pyrochroite
  - cmmmech:pyrolusite
  - cmmmech:pyromorphite
  - cmmmech:pyrrhotite
  - cmmmech:quenstedtite
  - cmmmech:ramsdellite
  - cmmmech:realgar
  - cmmmech:regerite
  - cmmmech:renierite
  - cmmmech:rhabdophane-ce
  - cmmmech:rhabdophane-la
  - cmmmech:rhodochrosite
  - cmmmech:rhomboclase
  - cmmmech:richetite
  - cmmmech:riebeckite
  - cmmmech:rivadavite
  - cmmmech:romanechite
  - cmmmech:roquesite
  - cmmmech:roscoelite
  - cmmmech:rozenite
  - cmmmech:rutherfordine
  - cmmmech:rutile
  - cmmmech:sabugalite
  - cmmmech:sakuraiite
  - cmmmech:saleeite
  - cmmmech:saponite
  - cmmmech:sauconite
  - cmmmech:scheelite
  - cmmmech:schertelite
  - cmmmech:schoepite
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:senarmontite
  - cmmmech:sepiolite
  - cmmmech:siderite
  - cmmmech:simonkolleite
  - cmmmech:sklodowskite
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:soddyite
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:stevensite
  - cmmmech:stibnite
  - cmmmech:stolzite
  - cmmmech:strengite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:struvite-k
  - cmmmech:studtite
  - cmmmech:sulfoborite
  - cmmmech:svanbergite
  - cmmmech:switzerite
  - cmmmech:synchysite-ce
  - cmmmech:szaibelyite
  - cmmmech:szomolnokite
  - cmmmech:talc
  - cmmmech:tennantite-in
  - cmmmech:tenorite
  - cmmmech:thomasclarkite-y
  - cmmmech:tincalconite
  - cmmmech:titanite
  - cmmmech:todorokite
  - cmmmech:torbernite
  - cmmmech:triphylite
  - cmmmech:troilite
  - cmmmech:tunellite
  - cmmmech:ulexite
  - cmmmech:uramphite
  - cmmmech:uraninite
  - cmmmech:uranophane
  - cmmmech:uranopilite
  - cmmmech:vaesite
  - cmmmech:vandenbrandeite
  - cmmmech:variscite
  - cmmmech:vaterite
  - cmmmech:veatchite
  - cmmmech:violarite
  - cmmmech:vivianite
  - cmmmech:voltaite
  - cmmmech:weddellite
  - cmmmech:weeksite
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:whitlockite
  - cmmmech:willemite
  - cmmmech:wollastonite
  - cmmmech:woodhouseite
  - cmmmech:wulfenite
  - cmmmech:wurtzite
  - cmmmech:xenotime-gd
  - cmmmech:xenotime-y
  - cmmmech:xenotime-yb
  - cmmmech:yanomamite
  - cmmmech:yusupovite
  - cmmmech:zeunerite
  - cmmmech:zincite
  - cmmmech:zincobriartite
  - cmmmech:zippeite
  - cmmmech:zircon
  - cmmmech:zirconolite
  evidence_ids:
  - ev-cohort-audit
  summary: Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 365
    mineral records carries a consistent canonical label with 0 cross-corpus conflicts.
assessments:
- assessment_id: assess-mineral-cohort-support
  topic: Mineral species identity, stoichiometry, criticality, and microbial mechanisms
  area: completeness
  outcome: supported
  target_ids:
  - cmmmech:acanthite
  - cmmmech:adamsite-y
  - cmmmech:akaganeite
  - cmmmech:alabandite
  - cmmmech:albite
  - cmmmech:alburnite
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:alunite
  - cmmmech:amblygonite
  - cmmmech:ameghinite
  - cmmmech:ammonioborite
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:ancylite-ce
  - cmmmech:andersonite
  - cmmmech:anglesite
  - cmmmech:anhydrite
  - cmmmech:anilite
  - cmmmech:annabergite
  - cmmmech:anorthite
  - cmmmech:aragonite
  - cmmmech:argentojarosite
  - cmmmech:argyrodite
  - cmmmech:aristarainite
  - cmmmech:arsenopyrite
  - cmmmech:artinite
  - cmmmech:asbolane
  - cmmmech:atacamite
  - cmmmech:autunite
  - cmmmech:azurite
  - cmmmech:baddeleyite
  - cmmmech:bainbridgeite-ndce
  - cmmmech:bainbridgeite-yce
  - cmmmech:baricite
  - cmmmech:bassanite
  - cmmmech:becquerelite
  - cmmmech:beudantite
  - cmmmech:billietite
  - cmmmech:birnessite
  - cmmmech:bismuthinite
  - cmmmech:bixbyite-mn
  - cmmmech:bobierrite
  - cmmmech:boehmite
  - cmmmech:boltwoodite
  - cmmmech:boracite
  - cmmmech:borax
  - cmmmech:bornite
  - cmmmech:briartite
  - cmmmech:brochantite
  - cmmmech:brookite
  - cmmmech:brucite
  - cmmmech:brushite
  - cmmmech:burbankite
  - cmmmech:cadmoindite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:calcioveatchite
  - cmmmech:calcite
  - cmmmech:carnotite
  - cmmmech:carrollite
  - cmmmech:cassiterite
  - cmmmech:catapleiite
  - cmmmech:cattiite
  - cmmmech:cavansite
  - cmmmech:caysichite-y
  - cmmmech:celestine
  - cmmmech:cerianite-ce
  - cmmmech:cerussite
  - cmmmech:chalcocite
  - cmmmech:chalcopyrite
  - cmmmech:chernikovite
  - cmmmech:childrenite
  - cmmmech:chlorapatite
  - cmmmech:chromite
  - cmmmech:chrysotile
  - cmmmech:chukanovite
  - cmmmech:churchite-y
  - cmmmech:cinnabar
  - cmmmech:cobaltite
  - cmmmech:coffinite
  - cmmmech:colemanite
  - cmmmech:compreignacite
  - cmmmech:coquimbite
  - cmmmech:cordylite-ce
  - cmmmech:corkite
  - cmmmech:covellite
  - cmmmech:crandallite
  - cmmmech:cryptomelane
  - cmmmech:cuprite
  - cmmmech:cuprosklodowskite
  - cmmmech:curite
  - cmmmech:digenite
  - cmmmech:diopside
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:dypingite
  - cmmmech:dzhalindite
  - cmmmech:elpidite
  - cmmmech:enstatite
  - cmmmech:eosphorite
  - cmmmech:erythrite
  - cmmmech:ezcurrite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:felsobanyaite
  - cmmmech:feroxyhyte
  - cmmmech:ferricopiapite
  - cmmmech:ferrihydrite
  - cmmmech:ferrokesterite
  - cmmmech:florencite-ce
  - cmmmech:florencite-la
  - cmmmech:fluorapatite
  - cmmmech:fluorite
  - cmmmech:forsterite
  - cmmmech:fritzscheite
  - cmmmech:galena
  - cmmmech:germanite
  - cmmmech:gersdorffite
  - cmmmech:gibbsite
  - cmmmech:ginorite
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:goldmanite
  - cmmmech:gorceixite
  - cmmmech:gowerite
  - cmmmech:goyazite
  - cmmmech:greenockite
  - cmmmech:greigite
  - cmmmech:gypsum
  - cmmmech:gysinite-nd
  - cmmmech:hafnon
  - cmmmech:hannayite
  - cmmmech:haradaite
  - cmmmech:hauerite
  - cmmmech:hausmannite
  - cmmmech:hawleyite
  - cmmmech:hazenite
  - cmmmech:heazlewoodite
  - cmmmech:hematite
  - cmmmech:hemimorphite
  - cmmmech:heterogenite
  - cmmmech:heterosite
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:huntite
  - cmmmech:hureaulite
  - cmmmech:hydroboracite
  - cmmmech:hydrocerussite
  - cmmmech:hydromagnesite
  - cmmmech:hydroniumjarosite
  - cmmmech:hydrotalcite
  - cmmmech:hydroxylapatite
  - cmmmech:hydrozincite
  - cmmmech:ilmenite
  - cmmmech:inderborite
  - cmmmech:inderite
  - cmmmech:indite
  - cmmmech:inyoite
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaliborite
  - cmmmech:kaolinite
  - cmmmech:katsarosite
  - cmmmech:kernite
  - cmmmech:kesterite
  - cmmmech:kornelite
  - cmmmech:kozoite-la
  - cmmmech:kozoite-nd
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:kurnakovite
  - cmmmech:kutnohorite
  - cmmmech:laforetite
  - cmmmech:lansfordite
  - cmmmech:lanthanite-ce
  - cmmmech:lanthanite-la
  - cmmmech:lanthanite-nd
  - cmmmech:larderellite
  - cmmmech:laueite
  - cmmmech:lepidocrocite
  - cmmmech:libethenite
  - cmmmech:lindbergite
  - cmmmech:lithiophilite
  - cmmmech:lizardite
  - cmmmech:loellingite
  - cmmmech:lorenzenite
  - cmmmech:ludlamite
  - cmmmech:mackinawite
  - cmmmech:maghemite
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:mcallisterite
  - cmmmech:mckelveyite-y
  - cmmmech:melanterite
  - cmmmech:meta-ankoleite
  - cmmmech:metacinnabar
  - cmmmech:metaschoepite
  - cmmmech:metastudtite
  - cmmmech:metatorbernite
  - cmmmech:metatyuyamunite
  - cmmmech:metavivianite
  - cmmmech:metazeunerite
  - cmmmech:meyerhofferite
  - cmmmech:microcline
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:monazite-ce
  - cmmmech:monazite-gd
  - cmmmech:monazite-la
  - cmmmech:monazite-nd
  - cmmmech:monazite-sm
  - cmmmech:monetite
  - cmmmech:monohydrocalcite
  - cmmmech:montebrasite
  - cmmmech:montmorillonite
  - cmmmech:montroseite
  - cmmmech:moolooite
  - cmmmech:muscovite
  - cmmmech:natroboltwoodite
  - cmmmech:natrojarosite
  - cmmmech:navajoite
  - cmmmech:nepheline
  - cmmmech:nesquehonite
  - cmmmech:newberyite
  - cmmmech:ningyoite
  - cmmmech:nobleite
  - cmmmech:nontronite
  - cmmmech:orpiment
  - cmmmech:orthoclase
  - cmmmech:otavite
  - cmmmech:palygorskite
  - cmmmech:paracoquimbite
  - cmmmech:paramontroseite
  - cmmmech:parasymplesite
  - cmmmech:parauranophane
  - cmmmech:pascoite
  - cmmmech:pentagonite
  - cmmmech:pentlandite
  - cmmmech:perovskite
  - cmmmech:pertlikite
  - cmmmech:petalite
  - cmmmech:petrukite
  - cmmmech:phlogopite
  - cmmmech:phosphoferrite
  - cmmmech:phosphophyllite
  - cmmmech:piilonenite-nd
  - cmmmech:pinnoite
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:polylithionite
  - cmmmech:powellite
  - cmmmech:preobrazhenskite
  - cmmmech:priceite
  - cmmmech:probertite
  - cmmmech:pyrite
  - cmmmech:pyroaurite
  - cmmmech:pyrochroite
  - cmmmech:pyrolusite
  - cmmmech:pyromorphite
  - cmmmech:pyrrhotite
  - cmmmech:quenstedtite
  - cmmmech:ramsdellite
  - cmmmech:realgar
  - cmmmech:regerite
  - cmmmech:renierite
  - cmmmech:rhabdophane-ce
  - cmmmech:rhabdophane-la
  - cmmmech:rhodochrosite
  - cmmmech:rhomboclase
  - cmmmech:richetite
  - cmmmech:riebeckite
  - cmmmech:rivadavite
  - cmmmech:romanechite
  - cmmmech:roquesite
  - cmmmech:roscoelite
  - cmmmech:rozenite
  - cmmmech:rutherfordine
  - cmmmech:rutile
  - cmmmech:sabugalite
  - cmmmech:sakuraiite
  - cmmmech:saleeite
  - cmmmech:saponite
  - cmmmech:sauconite
  - cmmmech:scheelite
  - cmmmech:schertelite
  - cmmmech:schoepite
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:senarmontite
  - cmmmech:sepiolite
  - cmmmech:siderite
  - cmmmech:simonkolleite
  - cmmmech:sklodowskite
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:soddyite
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:stevensite
  - cmmmech:stibnite
  - cmmmech:stolzite
  - cmmmech:strengite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:struvite-k
  - cmmmech:studtite
  - cmmmech:sulfoborite
  - cmmmech:svanbergite
  - cmmmech:switzerite
  - cmmmech:synchysite-ce
  - cmmmech:szaibelyite
  - cmmmech:szomolnokite
  - cmmmech:talc
  - cmmmech:tennantite-in
  - cmmmech:tenorite
  - cmmmech:thomasclarkite-y
  - cmmmech:tincalconite
  - cmmmech:titanite
  - cmmmech:todorokite
  - cmmmech:torbernite
  - cmmmech:triphylite
  - cmmmech:troilite
  - cmmmech:tunellite
  - cmmmech:ulexite
  - cmmmech:uramphite
  - cmmmech:uraninite
  - cmmmech:uranophane
  - cmmmech:uranopilite
  - cmmmech:vaesite
  - cmmmech:vandenbrandeite
  - cmmmech:variscite
  - cmmmech:vaterite
  - cmmmech:veatchite
  - cmmmech:violarite
  - cmmmech:vivianite
  - cmmmech:voltaite
  - cmmmech:weddellite
  - cmmmech:weeksite
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:whitlockite
  - cmmmech:willemite
  - cmmmech:wollastonite
  - cmmmech:woodhouseite
  - cmmmech:wulfenite
  - cmmmech:wurtzite
  - cmmmech:xenotime-gd
  - cmmmech:xenotime-y
  - cmmmech:xenotime-yb
  - cmmmech:yanomamite
  - cmmmech:yusupovite
  - cmmmech:zeunerite
  - cmmmech:zincite
  - cmmmech:zincobriartite
  - cmmmech:zippeite
  - cmmmech:zircon
  - cmmmech:zirconolite
  evidence_ids:
  - ev-cmmmech-validate
  - ev-cmmmech-history
  - ev-cohort-audit
  summary: All 365 mineral species records pass LinkML validation, carry IMA-compliant
    descriptions and source citations, and have verified curation histories.
  metrics:
  - name: reviewed_minerals
    value: 365.0
    unit: records
    definition: Total mineral species records reviewed in the cohort.
    minimum: 0.0
    maximum: 365.0
  - name: minerals_with_mechanisms
    value: 269.0
    unit: records
    definition: 'Mineral species records carrying mechanisms (157 with microbial:
      true mechanisms).'
    minimum: 0.0
    maximum: 365.0
  - name: minerals_with_causal_graphs
    value: 29.0
    unit: records
    definition: Mineral species records carrying multi-step causal_graphs and UniProtKB
      protein_examples.
    minimum: 0.0
    maximum: 365.0
- assessment_id: assess-mineral-missing-ima-identifiers
  topic: Structured IMA:YYYY-NNN identifier completeness on mineral records citing
    IMA species numbers
  area: identity
  outcome: concern
  target_ids:
  - cmmmech:alburnite
  - cmmmech:briartite
  - cmmmech:cavansite
  - cmmmech:compreignacite
  - cmmmech:falottaite
  - cmmmech:greigite
  - cmmmech:katsarosite
  - cmmmech:lindbergite
  - cmmmech:metavivianite
  - cmmmech:moolooite
  - cmmmech:pentagonite
  - cmmmech:pertlikite
  - cmmmech:regerite
  - cmmmech:schwertmannite
  - cmmmech:struvite-k
  - cmmmech:wheatleyite
  - cmmmech:zincobriartite
  evidence_ids:
  - ev-ima-missing-identifiers
  summary: 17 mineral records state their approved IMA-CNMNC species number (IMA YYYY-NNN)
    in prose description and cite ima_2026_09 in sources, yet omit the structured
    IMA:YYYY-NNN identifier entry in identifiers.
findings:
- finding_id: cmmmech-stage4-finding-0001
  issue_key: cmmmech.mineral.missing-ima-identifiers-on-cited-species
  title: 17 mineral records state IMA-CNMNC species numbers in description but omit
    structured IMA:YYYY-NNN entries in identifiers
  category: identity
  severity: minor
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:alburnite
  - cmmmech:briartite
  - cmmmech:cavansite
  - cmmmech:compreignacite
  - cmmmech:falottaite
  - cmmmech:greigite
  - cmmmech:katsarosite
  - cmmmech:lindbergite
  - cmmmech:metavivianite
  - cmmmech:moolooite
  - cmmmech:pentagonite
  - cmmmech:pertlikite
  - cmmmech:regerite
  - cmmmech:schwertmannite
  - cmmmech:struvite-k
  - cmmmech:wheatleyite
  - cmmmech:zincobriartite
  evidence_ids:
  - ev-ima-missing-identifiers
  description: 'Across the 365 mineral records, 43 records include a structured IMA:YYYY-NNN
    identifier in identifiers, whereas 17 mineral records explicitly state their IMA-CNMNC
    species number in description and cite ima_2026_09 in sources without a structured
    identifiers entry: alburnite (IMA:2012-073), briartite (IMA:1965-018), cavansite
    (IMA:1967-019), compreignacite (IMA:1964-026), falottaite (IMA:2013-044), greigite
    (IMA:1963-007), katsarosite (IMA:2020-014), lindbergite (IMA:2003-029), metavivianite
    (IMA:1973-049), moolooite (IMA:1980-082), pentagonite (IMA:1971-039), pertlikite
    (IMA:2005-055), regerite (IMA:2023-028), schwertmannite (IMA:1990-006), struvite-k
    (IMA:2003-048), wheatleyite (IMA:1984-040), and zincobriartite (IMA:2015-094).'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alburnite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/briartite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/cavansite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/compreignacite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/falottaite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/greigite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/lindbergite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/metavivianite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/moolooite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/pentagonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/pertlikite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/regerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/schwertmannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/struvite-k.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/wheatleyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/zincobriartite.yaml
    role: maintained_record
actions:
- action_id: action-add-ima-identifiers-to-17-minerals
  finding_ids:
  - cmmmech-stage4-finding-0001
  target_ids:
  - cmmmech:alburnite
  - cmmmech:briartite
  - cmmmech:cavansite
  - cmmmech:compreignacite
  - cmmmech:falottaite
  - cmmmech:greigite
  - cmmmech:katsarosite
  - cmmmech:lindbergite
  - cmmmech:metavivianite
  - cmmmech:moolooite
  - cmmmech:pentagonite
  - cmmmech:pertlikite
  - cmmmech:regerite
  - cmmmech:schwertmannite
  - cmmmech:struvite-k
  - cmmmech:wheatleyite
  - cmmmech:zincobriartite
  description: 'Add structured identifiers entries ({id: IMA:YYYY-NNN, label: <Mineral
    Name>}) and EDIT history sidecars to all 17 mineral records during Stage 5 grouped
    remediation.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alburnite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/briartite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/cavansite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/compreignacite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/falottaite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/greigite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/lindbergite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/metavivianite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/moolooite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/pentagonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/pertlikite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/regerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/schwertmannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/struvite-k.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/wheatleyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/zincobriartite.yaml
    role: maintained_record
  acceptance_checks:
  - All 17 mineral records contain their exact IMA:YYYY-NNN identifier and canonical
    mineral label under identifiers.
  - Each edited record has a matching EDIT sidecar in history/records/<slug>/ and
    passes cmmmech validate --require-records and cmmmech validate-history --base
    main.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:acanthite
  - cmmmech:adamsite-y
  - cmmmech:akaganeite
  - cmmmech:alabandite
  - cmmmech:albite
  - cmmmech:alburnite
  - cmmmech:alicewilsonite-yce
  - cmmmech:alicewilsonite-yla
  - cmmmech:alunite
  - cmmmech:amblygonite
  - cmmmech:ameghinite
  - cmmmech:ammonioborite
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:ancylite-ce
  - cmmmech:andersonite
  - cmmmech:anglesite
  - cmmmech:anhydrite
  - cmmmech:anilite
  - cmmmech:annabergite
  - cmmmech:anorthite
  - cmmmech:aragonite
  - cmmmech:argentojarosite
  - cmmmech:argyrodite
  - cmmmech:aristarainite
  - cmmmech:arsenopyrite
  - cmmmech:artinite
  - cmmmech:asbolane
  - cmmmech:atacamite
  - cmmmech:autunite
  - cmmmech:azurite
  - cmmmech:baddeleyite
  - cmmmech:bainbridgeite-ndce
  - cmmmech:bainbridgeite-yce
  - cmmmech:baricite
  - cmmmech:bassanite
  - cmmmech:becquerelite
  - cmmmech:beudantite
  - cmmmech:billietite
  - cmmmech:birnessite
  - cmmmech:bismuthinite
  - cmmmech:bixbyite-mn
  - cmmmech:bobierrite
  - cmmmech:boehmite
  - cmmmech:boltwoodite
  - cmmmech:boracite
  - cmmmech:borax
  - cmmmech:bornite
  - cmmmech:briartite
  - cmmmech:brochantite
  - cmmmech:brookite
  - cmmmech:brucite
  - cmmmech:brushite
  - cmmmech:burbankite
  - cmmmech:cadmoindite
  - cmmmech:calcioancylite-la
  - cmmmech:calcioburbankite
  - cmmmech:calcioveatchite
  - cmmmech:calcite
  - cmmmech:carnotite
  - cmmmech:carrollite
  - cmmmech:cassiterite
  - cmmmech:catapleiite
  - cmmmech:cattiite
  - cmmmech:cavansite
  - cmmmech:caysichite-y
  - cmmmech:celestine
  - cmmmech:cerianite-ce
  - cmmmech:cerussite
  - cmmmech:chalcocite
  - cmmmech:chalcopyrite
  - cmmmech:chernikovite
  - cmmmech:childrenite
  - cmmmech:chlorapatite
  - cmmmech:chromite
  - cmmmech:chrysotile
  - cmmmech:chukanovite
  - cmmmech:churchite-y
  - cmmmech:cinnabar
  - cmmmech:cobaltite
  - cmmmech:coffinite
  - cmmmech:colemanite
  - cmmmech:compreignacite
  - cmmmech:coquimbite
  - cmmmech:cordylite-ce
  - cmmmech:corkite
  - cmmmech:covellite
  - cmmmech:crandallite
  - cmmmech:cryptomelane
  - cmmmech:cuprite
  - cmmmech:cuprosklodowskite
  - cmmmech:curite
  - cmmmech:digenite
  - cmmmech:diopside
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dolomite
  - cmmmech:donnayite-y
  - cmmmech:dypingite
  - cmmmech:dzhalindite
  - cmmmech:elpidite
  - cmmmech:enstatite
  - cmmmech:eosphorite
  - cmmmech:erythrite
  - cmmmech:ezcurrite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:felsobanyaite
  - cmmmech:feroxyhyte
  - cmmmech:ferricopiapite
  - cmmmech:ferrihydrite
  - cmmmech:ferrokesterite
  - cmmmech:florencite-ce
  - cmmmech:florencite-la
  - cmmmech:fluorapatite
  - cmmmech:fluorite
  - cmmmech:forsterite
  - cmmmech:fritzscheite
  - cmmmech:galena
  - cmmmech:germanite
  - cmmmech:gersdorffite
  - cmmmech:gibbsite
  - cmmmech:ginorite
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:goldmanite
  - cmmmech:gorceixite
  - cmmmech:gowerite
  - cmmmech:goyazite
  - cmmmech:greenockite
  - cmmmech:greigite
  - cmmmech:gypsum
  - cmmmech:gysinite-nd
  - cmmmech:hafnon
  - cmmmech:hannayite
  - cmmmech:haradaite
  - cmmmech:hauerite
  - cmmmech:hausmannite
  - cmmmech:hawleyite
  - cmmmech:hazenite
  - cmmmech:heazlewoodite
  - cmmmech:hematite
  - cmmmech:hemimorphite
  - cmmmech:heterogenite
  - cmmmech:heterosite
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:huntite
  - cmmmech:hureaulite
  - cmmmech:hydroboracite
  - cmmmech:hydrocerussite
  - cmmmech:hydromagnesite
  - cmmmech:hydroniumjarosite
  - cmmmech:hydrotalcite
  - cmmmech:hydroxylapatite
  - cmmmech:hydrozincite
  - cmmmech:ilmenite
  - cmmmech:inderborite
  - cmmmech:inderite
  - cmmmech:indite
  - cmmmech:inyoite
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaliborite
  - cmmmech:kaolinite
  - cmmmech:katsarosite
  - cmmmech:kernite
  - cmmmech:kesterite
  - cmmmech:kornelite
  - cmmmech:kozoite-la
  - cmmmech:kozoite-nd
  - cmmmech:kukharenkoite-ce
  - cmmmech:kuliokite-y
  - cmmmech:kurnakovite
  - cmmmech:kutnohorite
  - cmmmech:laforetite
  - cmmmech:lansfordite
  - cmmmech:lanthanite-ce
  - cmmmech:lanthanite-la
  - cmmmech:lanthanite-nd
  - cmmmech:larderellite
  - cmmmech:laueite
  - cmmmech:lepidocrocite
  - cmmmech:libethenite
  - cmmmech:lindbergite
  - cmmmech:lithiophilite
  - cmmmech:lizardite
  - cmmmech:loellingite
  - cmmmech:lorenzenite
  - cmmmech:ludlamite
  - cmmmech:mackinawite
  - cmmmech:maghemite
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:mcallisterite
  - cmmmech:mckelveyite-y
  - cmmmech:melanterite
  - cmmmech:meta-ankoleite
  - cmmmech:metacinnabar
  - cmmmech:metaschoepite
  - cmmmech:metastudtite
  - cmmmech:metatorbernite
  - cmmmech:metatyuyamunite
  - cmmmech:metavivianite
  - cmmmech:metazeunerite
  - cmmmech:meyerhofferite
  - cmmmech:microcline
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:monazite-ce
  - cmmmech:monazite-gd
  - cmmmech:monazite-la
  - cmmmech:monazite-nd
  - cmmmech:monazite-sm
  - cmmmech:monetite
  - cmmmech:monohydrocalcite
  - cmmmech:montebrasite
  - cmmmech:montmorillonite
  - cmmmech:montroseite
  - cmmmech:moolooite
  - cmmmech:muscovite
  - cmmmech:natroboltwoodite
  - cmmmech:natrojarosite
  - cmmmech:navajoite
  - cmmmech:nepheline
  - cmmmech:nesquehonite
  - cmmmech:newberyite
  - cmmmech:ningyoite
  - cmmmech:nobleite
  - cmmmech:nontronite
  - cmmmech:orpiment
  - cmmmech:orthoclase
  - cmmmech:otavite
  - cmmmech:palygorskite
  - cmmmech:paracoquimbite
  - cmmmech:paramontroseite
  - cmmmech:parasymplesite
  - cmmmech:parauranophane
  - cmmmech:pascoite
  - cmmmech:pentagonite
  - cmmmech:pentlandite
  - cmmmech:perovskite
  - cmmmech:pertlikite
  - cmmmech:petalite
  - cmmmech:petrukite
  - cmmmech:phlogopite
  - cmmmech:phosphoferrite
  - cmmmech:phosphophyllite
  - cmmmech:piilonenite-nd
  - cmmmech:pinnoite
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:polylithionite
  - cmmmech:powellite
  - cmmmech:preobrazhenskite
  - cmmmech:priceite
  - cmmmech:probertite
  - cmmmech:pyrite
  - cmmmech:pyroaurite
  - cmmmech:pyrochroite
  - cmmmech:pyrolusite
  - cmmmech:pyromorphite
  - cmmmech:pyrrhotite
  - cmmmech:quenstedtite
  - cmmmech:ramsdellite
  - cmmmech:realgar
  - cmmmech:regerite
  - cmmmech:renierite
  - cmmmech:rhabdophane-ce
  - cmmmech:rhabdophane-la
  - cmmmech:rhodochrosite
  - cmmmech:rhomboclase
  - cmmmech:richetite
  - cmmmech:riebeckite
  - cmmmech:rivadavite
  - cmmmech:romanechite
  - cmmmech:roquesite
  - cmmmech:roscoelite
  - cmmmech:rozenite
  - cmmmech:rutherfordine
  - cmmmech:rutile
  - cmmmech:sabugalite
  - cmmmech:sakuraiite
  - cmmmech:saleeite
  - cmmmech:saponite
  - cmmmech:sauconite
  - cmmmech:scheelite
  - cmmmech:schertelite
  - cmmmech:schoepite
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:senarmontite
  - cmmmech:sepiolite
  - cmmmech:siderite
  - cmmmech:simonkolleite
  - cmmmech:sklodowskite
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:soddyite
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:stevensite
  - cmmmech:stibnite
  - cmmmech:stolzite
  - cmmmech:strengite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:struvite-k
  - cmmmech:studtite
  - cmmmech:sulfoborite
  - cmmmech:svanbergite
  - cmmmech:switzerite
  - cmmmech:synchysite-ce
  - cmmmech:szaibelyite
  - cmmmech:szomolnokite
  - cmmmech:talc
  - cmmmech:tennantite-in
  - cmmmech:tenorite
  - cmmmech:thomasclarkite-y
  - cmmmech:tincalconite
  - cmmmech:titanite
  - cmmmech:todorokite
  - cmmmech:torbernite
  - cmmmech:triphylite
  - cmmmech:troilite
  - cmmmech:tunellite
  - cmmmech:ulexite
  - cmmmech:uramphite
  - cmmmech:uraninite
  - cmmmech:uranophane
  - cmmmech:uranopilite
  - cmmmech:vaesite
  - cmmmech:vandenbrandeite
  - cmmmech:variscite
  - cmmmech:vaterite
  - cmmmech:veatchite
  - cmmmech:violarite
  - cmmmech:vivianite
  - cmmmech:voltaite
  - cmmmech:weddellite
  - cmmmech:weeksite
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:whitlockite
  - cmmmech:willemite
  - cmmmech:wollastonite
  - cmmmech:woodhouseite
  - cmmmech:wulfenite
  - cmmmech:wurtzite
  - cmmmech:xenotime-gd
  - cmmmech:xenotime-y
  - cmmmech:xenotime-yb
  - cmmmech:yanomamite
  - cmmmech:yusupovite
  - cmmmech:zeunerite
  - cmmmech:zincite
  - cmmmech:zincobriartite
  - cmmmech:zippeite
  - cmmmech:zircon
  - cmmmech:zirconolite
  rationale: All 365 records in the mineral cohort denote distinct, non-synonymous
    entities matching data/records/*.yaml where material_kind == 'mineral' at 4d878383c92b44876df3bf166d96637c7581a59e
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-cohort-audit
evidence:
- evidence_id: ev-cmmmech-validate
  kind: validation
  reference: src/cmmmech/validation.py
  locator: cmmmech validate --require-records
  accessed_at: '2026-10-22T02:58:01Z'
  support: supports
  summary: LinkML structural and semantic validator passed across all 616 records
    (including the mineral cohort) with 0 errors.
- evidence_id: ev-cmmmech-history
  kind: validation
  reference: src/cmmmech/history.py
  locator: cmmmech validate-history --base main
  accessed_at: '2026-10-22T02:58:01Z'
  support: supports
  summary: All 810 curation history sidecars in history/records/ and record history_refs
    passed validation with 0 errors.
- evidence_id: ev-cohort-audit
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: Stage 4 full-inventory cohort audit (mineral) at 4d878383c92b44876df3bf166d96637c7581a59e
  accessed_at: '2026-10-22T02:58:01Z'
  support: supports
  summary: Full-inventory inspection of all records in the mineral cohort verified
    distinct material identities, source-backed criticality/mechanism claims, and
    100% CURIE label consistency across 270 distinct ontology terms.
- evidence_id: ev-ima-missing-identifiers
  kind: record_content
  reference: data/records/alburnite.yaml
  locator: 17 mineral records with IMA numbers in description and ima_2026_09 in sources
    but no IMA:* entry in identifiers
  accessed_at: '2026-10-22T02:58:01Z'
  support: partial
  summary: 17 mineral records (alburnite, briartite, cavansite, compreignacite, falottaite,
    greigite, katsarosite, lindbergite, metavivianite, moolooite, pentagonite, pertlikite,
    regerite, schwertmannite, struvite-k, wheatleyite, zincobriartite) state their
    approved IMA-CNMNC species numbers in description and cite ima_2026_09 in sources,
    but omit the structured IMA:YYYY-NNN entry in identifiers used by the other 43
    IMA-numbered mineral records.
limitations:
- 17 mineral records omit structured IMA:YYYY-NNN entries in identifiers despite stating
  those IMA numbers in description (tracked as open finding cmmmech-stage4-finding-0001
  for Stage 5 remediation); cmmmech:wulfenite omits ima_2026_09 from sources (tracked
  as open finding cmmmech-stage4-finding-0002 in companion review 20261022T025807Z-wulfenite-stage4-record-review).
notes:
- 'Stage 3 added verified UniProtKB protein examples to 6 mineral records: bixbyite-mn
  (UniProtKB:A0A0K2YWP2, UniProtKB:L0KKS2), dittmarite (UniProtKB:G3Y4N5), glushinskite
  (UniProtKB:G3Y4N5), montmorillonite (UniProtKB:Q8E8S0, UniProtKB:Q8EG34, UniProtKB:Q8EG33),
  nontronite (UniProtKB:Q8E8S0, UniProtKB:Q8EG34, UniProtKB:Q8EG33), and struvite
  (UniProtKB:G3Y4N5); all 6 passed full Stage 4 verification.'
```
