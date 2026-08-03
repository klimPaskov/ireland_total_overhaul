# Ireland focus tree sourced report/news audit

> Historical bounded research snapshot. The assigned-row evidence remains
> useful, but package-wide status and paths are governed by the authoritative
> 2026-07-29 `source_manifest.json` and the later blocked-queue handoffs under
> `assets/source_research_handoffs/`. The current manifest contains 47 complete,
> 31 review-gated, and 91 blocked entries.

Date: 2026-07-22
Scope: EV-SRC-002, EV-SRC-003, EV-SRC-004, EV-SRC-005, EV-SRC-006, EV-SRC-007, EV-SRC-008, EV-SRC-009, EV-SRC-010, EV-SRC-014, EV-SRC-016, EV-SRC-019
Feature: `ireland_focus_tree`

This is a source-side handoff only. No gameplay, event, localisation, GUI or `.gfx` file was edited. Final DDS files, where cleared, are under `gfx/event_pictures/ireland/`.

## Manifest audit and repair

The pre-final audit found the reported inconsistency: `EV-SRC-004` carried the Constitution Bill source, processed PNG and final DDS fields belonging to `EV-SRC-019`, while `EV-SRC-019` was marked complete with `final_dds_path = not_created`. The assigned rows were repaired as complete JSON objects rather than by field-wise substitutions.

The audit also removed a borrowed Blacksod source package from `EV-SRC-009`. The final assigned-row invariants are:

- Complete C3 rows: EV-SRC-002, EV-SRC-003, EV-SRC-005, EV-SRC-014 and EV-SRC-019. Each has its own existing source, processed PNG, runtime DDS and matching DDS SHA-256.
- Blocked C1/C2 rows: EV-SRC-004, EV-SRC-006, EV-SRC-007, EV-SRC-008, EV-SRC-009, EV-SRC-010 and EV-SRC-016. Each has `source_path`, `processed_png_path` and `final_dds_path` set to `not_created`, with null final/dimension/processing fields in the manifest. No blocked row borrows another slot's source or hash.
- The five clearance states remain intact. No row was promoted without object-level evidence and a recorded rights basis.

The existing local review files for EV-SRC-010 and EV-SRC-016 remain available for rights review, but are intentionally not referenced as created assets in their blocked manifest rows.

## Complete packages

### EV-SRC-002 — 1938 trade/finance implementing enactment

- Object: *Finance (Agreement With United Kingdom) Act, 1938*, Number 12 of 1938; agreement dated 25 April 1938, Act enacted 16 May 1938.
- Source/holding: Irish Statute Book / Government of Ireland; browser-rendered official page.
- Source URL: https://www.irishstatutebook.ie/eli/1938/act/12/enacted/en/print.html
- Context lead: https://www.difp.ie/volume-5/1938/british-irish-tripartite-agreement-on-trade-finance-and-defence/2321/
- Rights: C3, Oireachtas Open Data PSI Licence incorporating CC BY 4.0. Retain the Houses/Government credit, licence reference and disclaimer. Rights reference: https://www.irishstatutebook.ie/eli/open-data.html and https://www.oireachtas.ie/en/open-data/license/
- Attribution: Government of Ireland / Houses of the Oireachtas; *Finance (Agreement With United Kingdom) Act, 1938*; Oireachtas Open Data PSI Licence / CC BY 4.0.
- Crop: first-page title and arrangement of sections from the official page; report-card cover crop at 210x176. This is the exact statutory trade/finance component, not a signing photograph and not a claim that the DIFP diplomatic page itself was republished.
- Files: source original `assets/ireland_focus_tree/sourced/source_originals/event_ev_src_002_finance_agreement_with_united_kingdom_act_1938.html`; rendered source preview `..._page1.png`; processed `assets/ireland_focus_tree/sourced/processed_png/event_ev_src_002_report.png`; final `gfx/event_pictures/ireland/event_ev_src_002_report.dds`.
- SHA-256: source `582452A5B5BAA9A45A8A7ECD121CCF82FB92E0AD9789E2067BC6F1345F12EF45`; source preview `B3B8A754224A494066508946852999E9B38428B849E14D5858ADDC5F54BCF705`; processed `E96FC2CDAAB35F675E4A166CB76F10B9A1DBB5A0C06B5C297C06E71BF2CC06C2`; DDS `DCAC93E7818DB601D422597A4DD4DE294AD918C287FF336F9A7A184D923EA752`.
- Sprite: `ireland_report_historical_chain_report_02`.
- Uncertainty: the cleared object is the Irish implementing enactment for the trade/finance component; the wider tripartite diplomatic record remains a separate DIFP research lead.

### EV-SRC-003 — Treaty Port transfer statute

- Object: *Eire (Confirmation of Agreements) Act 1938*, 1 & 2 Geo. 6 c.25, First Schedule, “Agreement regarding Articles 6 and 7,” PDF page 5. Paragraph 2 records transfer of Admiralty property and harbour defences at Berehaven, Cobh (Queenstown) and Lough Swilly.
- Source/holding: legislation.gov.uk / UK Parliament; official legislation scan.
- Source URL: https://www.legislation.gov.uk/ukpga/Geo6/1-2/25/pdfs/ukpga_19380025_en.pdf
- Related record: https://www.difp.ie/volume-5/1938/transfer-of-treaty-ports/2338/
- Rights: C3, Open Government Licence v3.0. Suggested attribution: “© Crown and database right. Derived from content available under the Open Government Licence v3.0 from legislation.gov.uk.” Rights reference: https://legislation.github.io/data-documentation/reuse-licence.html
- Attribution: Crown and database right; legislation.gov.uk; OGL v3.0 attribution above.
- Crop: full official PDF page 5, including the First Schedule heading and transfer paragraph; report-card cover crop at 210x176. This is the legal transfer record, not a handover photograph.
- Files: source original `assets/ireland_focus_tree/sourced/source_originals/event_ev_src_003_eire_confirmation_of_agreements_act_1938.pdf`; rendered page `..._page5.png`; processed `assets/ireland_focus_tree/sourced/processed_png/event_ev_src_003_report.png`; final `gfx/event_pictures/ireland/event_ev_src_003_report.dds`.
- SHA-256: source `4BE2B5C4A437C598851ED9D8C9F1B87612AB29159C46434764C9E031C0895286`; source preview `FFDB38073554E44ABC60E14EBFD93331A6D458367F744C3AD2CC193B6BE5F585`; processed `30BFB4A655B20B0635FDF27259BFD5613795A5065F3FE013ACB320B9F8F36ABC`; DDS `A01C9668BA5BA6D8920A7DC3C25FADC003A92C4B3BA2A3027FAADAC2EE208F8D`.
- Sprite: `ireland_report_historical_chain_report_03`.
- Uncertainty: no individual image author is recorded because the source is an official document scan; OGL conditions are carried.

### EV-SRC-005 — 1941 British Treaty Port claims record

- Object: Historic Hansard, Commons, 18 June 1941, HC Deb vol. 372 cc645-6, “Eire (Ports and Air Bases).” The exact question and answer concern handing over Eire ports and air bases to Britain.
- Source/holding: UK Parliament / Historic Hansard.
- Source URL: https://api.parliament.uk/historic-hansard/commons/1941/jun/18/eire-ports-and-air-bases
- Related page: https://hansard.parliament.uk/Commons/1941-06-18
- Rights: C3, Open Parliament Licence v3.0. Attribution: “Contains Parliamentary information licensed under the Open Parliament Licence v3.0.” Rights reference: https://www.parliament.uk/site-information/copyright/open-parliament-licence/
- Attribution: UK Parliament / Historic Hansard; Open Parliament Licence v3.0 attribution above.
- Crop: browser-rendered transcript heading and question/answer lines; report-card cover crop at 210x176. Text transcript only; no excluded photograph or third-party media is used.
- Files: source original `assets/ireland_focus_tree/sourced/source_originals/event_ev_src_005_hansard_eire_ports_air_bases_1941.html`; rendered preview `..._page1.png`; processed `assets/ireland_focus_tree/sourced/processed_png/event_ev_src_005_report.png`; final `gfx/event_pictures/ireland/event_ev_src_005_report.dds`.
- SHA-256: source `D6A252E3B6672D84CC23DE2CBD95BCCA267C60F8BE5068FEA290E14E2533DB14`; source preview `F8362941628CD92175D4C620A7A194934C991681A6E0E03CB797D02119D31D31`; processed `279144F65181311228FE41E0921765E5EB8F8A4FCC1D36EF4924C4B1F315BE65`; DDS `2EF57A1249BE6CAE91AA72565AD8FF35C49FDCF60571E6441043CB449A4794D6`.
- Sprite: `ireland_report_historical_chain_report_05`.
- Uncertainty: exact contemporary record, but not a photograph.

### EV-SRC-014 — Irish merchant ship *Irish Poplar*

- Object: Imperial War Museums A13398, “An Irish merchant ship, IRISH POPLAR, with large markings on the sides to warn U-boats that she was a neutral.”
- Creator/date: Royal Navy official photographer H.W. Tomlin (Lt.); IWM/Commons date range 1939-1945.
- Source URL: https://commons.wikimedia.org/wiki/File:The_Royal_Navy_during_the_Second_World_War_A13398.jpg
- Identity support: https://www.oireachtas.ie/en/debates/debate/seanad/1994-04-27/4/
- Rights: C3, conservative basis. Commons records an IWM Non Commercial Licence and a UK-government public-domain basis; retain IWM/photographer credit and treat the object as noncommercial until any wider redistribution is separately confirmed.
- Attribution: Imperial War Museums A13398; Royal Navy official photographer H.W. Tomlin (Lt.); Wikimedia Commons file record; IWM noncommercial condition.
- Crop: full 800x592 source, preserving *Irish Poplar* hull and neutral markings; report-card cover crop at 210x176.
- Files: `assets/ireland_focus_tree/sourced/source_originals/event_ev_src_014_irish_poplar_iwm_a13398.jpg`; processed `assets/ireland_focus_tree/sourced/processed_png/event_ev_src_014_report.png`; final `gfx/event_pictures/ireland/event_ev_src_014_report.dds`.
- SHA-256: source `65BAFEF46DCA821D9AEE4C1D3FB6D7EBA012553F2CD161EF6D7A54A2422E4A08`; processed `94E9FFC18A158609A1846664322C60615BF13E94EB63BE963417752581BA85AB`; DDS `6F937F3506F22B61B90D9EE4872BCEDE62B73B6E3C8CD4679E8CFD5FCD7F7802`.
- Sprite: `ireland_report_historical_chain_report_14`.
- Uncertainty: exact vessel identity, but the IWM date is a range rather than a day-specific event. This is a distinct object from the already packaged Tregothnan/*Irish Larch* source.

### EV-SRC-019 — 1937 Constitution Bill

- Object: *Constitution (Consequential Provisions) Bill 1937*, Bill 41 of 1937, official Oireachtas PDF, page 1.
- Source/holding: Houses of the Oireachtas / data.oireachtas.ie.
- Source URL: https://data.oireachtas.ie/ie/oireachtas/bill/1937/41/eng/ver_a/bills1936-37-1pp-02.pdf
- Rights: C3, Oireachtas Open Data PSI Licence incorporating CC BY 4.0. Retain Houses creator credit, copyright notice, licence reference and disclaimer. Rights references: https://www.oireachtas.ie/en/copyright-and-reuse/ and https://www.oireachtas.ie/en/open-data/license/
- Attribution: Houses of the Oireachtas; *Constitution (Consequential Provisions) Bill 1937*, Bill 41 of 1937; Oireachtas Open Data PSI Licence / CC BY 4.0.
- Crop: official bill scan page 1, Arrangement of Sections; report-card cover crop at 210x176. This is the 1937 bill object, not the current consolidated Constitution page and not EV-SRC-001's separate constitution symbol object.
- Files: `assets/ireland_focus_tree/sourced/source_originals/event_ev_src_019_constitution_consequential_provisions_bill_1937.pdf`; rendered page `..._page1.png`; processed `assets/ireland_focus_tree/sourced/processed_png/event_ev_src_019_report.png`; final `gfx/event_pictures/ireland/event_ev_src_019_report.dds`.
- SHA-256: source `5AA66E208FEC55EB47E60726202278027FD6B8D681EFB1D5318EF2DE87046BF7`; source preview `48E54B5691A4AFEF73200C6544BA97D0F47899CCBEF09B46E05938EE58E84C66`; processed `22F2E4D37F2910919B5994FF2598BBC3BB0799515247A52CF79024ED96D07857`; DDS `ECCA1DF1790CAF3FAF41595D46CC0CE7DD3CE72482D3A7AAD37ABFB3EFFBDEA3`.
- Sprite: `ireland_report_constitutional_crisis_report_01`.
- Uncertainty: exact original-era bill scan, not the enrolled instrument; Oireachtas conditions remain attached.

## Blocked and review-gated slots

### EV-SRC-004 — C1 provenance identified

The exact 12 August 1940 DIFP neutrality memorandum is identified at https://www.difp.ie/volume-6/1940/synopsis-of-rationale-for-irelands-neutrality/3260/, with related 1939 neutrality material at https://www.difp.ie/volume-6/1939/memorandum-entitled-irelands-neutrality-in-practice/3001/. No exact downloadable image/document object with compatible project-use terms was found. The existing 1939 de Valera portrait is a contextual identity image, not the neutrality record, and was rejected. Manifest source, processed and final paths remain `not_created`; no hash is assigned.

### EV-SRC-006 — C1 provenance identified

The exact 1940 British unity proposal / Irish reply record is identified through https://www.difp.ie/volume-6/1940/irish-reply-to-british-proposals-for-a-united-ireland/3213/ and https://www.difp.ie/viewdoc.php?DocID=3208. The DIFP pages do not provide an exact downloadable image/document object with a compatible project-use basis. Related official debates were not the exact proposal and were not substituted. Manifest paths remain `not_created`; no hash is assigned.

### EV-SRC-007 — C1 provenance identified

Military Archives identifies the 1939-1945 Lookout Post Logbooks and coast-watching fonds at https://www.militaryarchives.ie/en/reading-room-collections/lookout-post-logbooks, but no exact period logbook/page/image with documented project-use rights was downloadable. Modern Geograph lookout-post photographs, including https://commons.wikimedia.org/wiki/File:Coast_Watching_Service_Lookout_Post_at_Brandon_Point,_Kerry_-_geograph.org.uk_-_5876660.jpg, were rejected as modern substitutes. Manifest paths remain `not_created`; no hash is assigned.

### EV-SRC-008 — C1 provenance identified

Military Archives identifies the 1939-1946 Emergency Defence Plans fonds at https://www.militaryarchives.ie/en/reading-room-collections/emergency-defence-plans, but the exact historical plan/map object and a compatible rights statement were not available. The 2019 archive catalogue/finding aid at https://www.militaryarchives.ie/uploads/documents/DFPP_769_19_2019_archives_Calendar_2020_correct_order.pdf is not the historical object. Manifest paths remain `not_created`; no hash is assigned.

### EV-SRC-009 — C1 provenance identified

Military Archives identifies the Air Defence Command fonds at https://www.militaryarchives.ie/en/reading-room-collections/air-defence-command; the related PDF finding aid at https://www.militaryarchives.ie/uploads/images/Air-Defence-Command.pdf is a modern archival aid, not a wartime object, and has no reusable-object clearance. Foreign or modern air-defence imagery would be substitution. Manifest paths remain `not_created`; no hash is assigned.

### EV-SRC-010 — C2 restricted or review pending

Exact source objects were identified on Met Éireann's Blacksod page: F.E. Dixon's 1942 Blacksod weather-station photograph and the 3 June 1944 observation sheet, https://www.met.ie/blacksod-point-and-the-d-day-forecast. Local review package files are `assets/ireland_focus_tree/sourced/source_originals/event_ev_src_010_blacksod_weather_station_1942_met_eireann.png` (SHA-256 `A92C4F4AC9CA17BEB9A73B1D78B26695589A7AAE7C19A6E9B486B1421A6A0D24`) and `...event_ev_src_010_blacksod_observation_sheet_1944_met_eireann.jpg` (SHA-256 `6BDFBBEAD50F0A1E3A7B59B1619CEF0431860004A4E0AE332BAAA8B716F5F6E4`), with review PNGs `event_ev_src_010_review_station.png` (SHA-256 `EA299B8B9079B4AEAC16DB0C0C1FE490DD0E8D571317FC4951292733DF961992`) and `event_ev_src_010_review_observation.png` (SHA-256 `0BA695B695E4CD27D189A00FA6742151E3B6E55FD83D4B42FD14C9F857A929D0`). Met Éireann's copyright notice, https://www.met.ie/index.php/about-us/copyright-notice, permits limited credited private/noncommercial teaching/research use but says protected images may not be altered and otherwise require written permission. The report-card transformation and internet mod redistribution therefore remain review-gated. Manifest paths and hashes are intentionally `not_created`/null; no DDS exists.

### EV-SRC-016 — C2 restricted or review pending

Exact object: Dúchas Schools Collection CBÉ 0689 p.078, dated 23 September 1938, https://www.duchas.ie/en/cbe/9002797/7355941/9132750. The local review source is `assets/ireland_focus_tree/sourced/source_originals/event_ev_src_016_schools_collection_cbe_0689_078.jpg` (SHA-256 `1CC11DE183661F2992C7BD7C2FA1CC1E9CCFC404701D4AB50069309A7FCEFEB9`) and review PNG `event_ev_src_016_review.png` (SHA-256 `380D223B56AFF2BFE5EC4D2A02D8E49385B3F6A7A007D7306B3146DFFEB78B50`). Dúchas contact/rights guidance is https://www.duchas.ie/en/info/contact; UCD reproduction guidance is https://www.ucd.ie/irishfolklore/en/t4media/NFC_reprod_rights_2017.pdf and https://www.ucd.ie/irishfolklore/en/t4media/Citing%20the%20NFC_2017.pdf. CC BY-NC 4.0 is not treated as sufficient because written permission for publication/reproduction and the derivative internet use is not recorded. Manifest paths and hashes are intentionally `not_created`/null; no DDS exists.

## Contact sheet

The five completed report-card previews are assembled in `assets/ireland_focus_tree/sourced/processed_png/contact_sheet_EV_SRC_002_019_2026-07-22.png` for visual review.

## No-reuse and handoff notes

The cleared EV-SRC-014 *Irish Poplar* photograph is not the previously packaged Tregothnan/*Irish Larch* object. EV-SRC-019 is the separate 1937 Constitution Bill package and is not EV-SRC-001's constitution symbol. The complete rows are ready for main-agent `.gfx` registration; unresolved rows remain blocked without fallback or substitution.
