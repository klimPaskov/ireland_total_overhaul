# Ireland source-clearance researcher handoff — 2026-08-01

Feature slug: `ireland_focus_tree`  
Role: bounded sourced-visual source-clearance research  
Scope: source objects, provenance, processing, DDS review, manifest and handoff only. No gameplay, localisation, GUI, `.gfx`, or live-game edits.

## Outcome

One exact-period symbol/document alternate was defensibly promoted:

- `S-07` — a 1937 Fine Gael constitutional-referendum poster, promoted to `C3 cleared with conditions` and `complete` in the authoritative manifest. The selected object is the exact 1937 poster recorded by Wikimedia Commons, sourced there to Irish Election Literature. It is an alternate to the NLI-controlled 1938 `EPH B1012` object, not a claim that the NLI scan is licensed.

The 15 priority `EV-SRC` rows remain blocked. No exact event/news source object with compatible project-use clearance was found, so the canonical 120-image sourced event/news budget remains short by those 15 rows. No portrait row was cleared. The remaining blocked symbol rows are unchanged except for `S-07`.

Manifest counts after the single promotion: 125 complete, 44 blocked; 54 complete and 15 blocked event/news rows; 45 complete and 15 blocked portrait rows; 26 complete and 14 blocked symbol/document rows.

## Authority and research boundaries

Reviewed the repo-local `hoi4-feature-assets` skill, the current `source_of_truth_map.md`, the authoritative `source_manifest.json`, the canonical vanilla-reference README/CATALOG, and the existing dated event/news and symbol blocked-source handoffs. The source pass used only exact-period or historically attested source leads. Modern redraws, AI material, unrelated period substitutes, generic maps, modern contextual articles, and restricted/unclear objects were not promoted.

## Cleared package — S-07

| Field | Record |
|---|---|
| Status | `complete`; `C3 cleared with conditions` |
| Exact object | Wikimedia Commons, `Fine Gael "Say No" Poster used in the Irish constitutional referendum of 1937.jpg` |
| Object URL | https://commons.wikimedia.org/wiki/File:Fine_Gael_%22Say_No%22_Poster_used_in_the_Irish_constitutional_referendum_of_1937.jpg |
| Original source | http://irishelectionliterature.com/tag/1937-referendum-on-the-constitution/ |
| Creator/date | Fine Gael; 1937 |
| Clearance | Commons records the exact object as Public domain under its PD-shape/no-copyright determination. This is recorded conservatively as C3, not unrestricted C4; preserve the source credit and alternate-object boundary. |
| Source object | `assets/ireland_focus_tree/sourced/research_2026-08-01/source_clearance_researcher/S-07_fine_gael/fine_gael_say_no_1937_commons_original.jpg` |
| Source dimensions/hash | 528x652; SHA-256 `e3a588282a644561041f0462bf88876d561df851dd26bbde731e675c18bee7ce` |
| Provenance evidence | `source_pages/S-07_commons_file_page.html`, `source_pages/S-07_irish_election_literature_source_page.html`, `research_evidence/S-07_commons_imageinfo.json` |
| Processed preview | `assets/ireland_focus_tree/sourced/research_2026-08-01/source_clearance_researcher/processed_png/symbol_document_s_07_fine_gael_1937_397x153.png` |
| Processing | Exact source crop `[0,442,528,646]`, resized to 397x153, RGBA; no generated or unrelated pixels. SHA-256 `1a7474b2e49eb320f0e458628e4e5077570e20bf41676c8a63ed5ed7f925e337` |
| DDS review | `dds_review/symbol_document_s_07_fine_gael_1937.dds`; SHA-256 `4a984a506cbb1bc29f4e5551cbd5b6f4924c422570c5863f6f37ab8dd397de06` |
| Runtime DDS | `gfx/interface/ireland/sourced/symbol_document_s_07.dds`; copied only after the manifest promotion; no existing file was overwritten |
| Sprite | `ireland_symbol_document_s_07`; target size 397x153 |
| Required credit | Fine Gael, 1937 referendum poster; original source Irish Election Literature; Wikimedia Commons file URL |

The staged candidate contact sheet is `contact_sheet/S-07_fine_gael_crop_candidates.jpg`. The staged `gfx_handoff.md` gives the proposed sprite and a ready-to-copy body; the parent agent owns the actual `.gfx` wiring.

## Priority event/news rows — all still blocked

All rows below have `status=blocked`, `clearance_state=C1 provenance identified`, `source_path=not_created`, and no source/processed/DDS hash because no cleared image object was promoted. The listed page is an exact historical lead or holding-institution page, not a clearance grant.

| Row | Exact source URL | Licence/clearance | Exact remaining blocker | Hashes |
|---|---|---|---|---|
| `EV-SRC-006` | https://www.difp.ie/volume-6/1940/irish-reply-to-british-proposals-for-a-united-ireland/3207/ | DIFP/RIA page rights; no project-use image/document licence | The 4 July 1940 reply and related correspondence are text records on the identified page; no exact downloadable image/document object with compatible reuse terms was found. | None — not created |
| `EV-SRC-008` | https://www.militaryarchives.ie/en/reading-room-collections/emergency-defence-plans | Military Archives; exact object rights not established | The 1939-46 fonds/finding aid and contextual `EDP_01.jpg` do not establish an exact plan/map object, object-level date/creator, or project-use reproduction permission. | None — not created |
| `EV-SRC-009` | https://www.militaryarchives.ie/en/reading-room-collections/air-defence-command | Military Archives; exact object rights not established | The Air Defence Command fonds/finding aid and contextual searchlight image do not provide a cleared exact wartime report/map/photo object or project-use permission. | None — not created |
| `EV-SRC-024` | https://www.difp.ie/volume-6/1940/irish-reply-to-british-proposals-for-a-united-ireland/3207/ | Historical source family identified; no image-object permission | Same exact unity-proposal/reply blocker as `EV-SRC-006`; no separate image object or compatible licence. | None — not created |
| `EV-SRC-026` | https://www.militaryarchives.ie/en/reading-room-collections/emergency-defence-plans | Historical source family identified; no image-object permission | Same exact Emergency Defence Plans blocker as `EV-SRC-008`; finding aid/context image is not a cleared period plan object. | None — not created |
| `EV-SRC-027` | https://www.militaryarchives.ie/en/reading-room-collections/air-defence-command | Historical source family identified; no image-object permission | Same exact Air Defence Command blocker as `EV-SRC-009`; no object-level rights statement. | None — not created |
| `EV-SRC-028` | https://www.met.ie/blacksod-point-and-the-d-day-forecast | Met Eireann page identifies copyrighted historical images; no project permission | The exact Blacksod page identifies the 1942 station photo as Copyright Met Eireann and the observation/wedding material carries reserved or family rights. The copyright notice does not grant derivative game-asset use. | None — not created |
| `EV-SRC-042` | https://www.difp.ie/volume-6/1940/irish-reply-to-british-proposals-for-a-united-ireland/3207/ | Historical source family identified; no image-object permission | Same exact unity-proposal/reply blocker as `EV-SRC-006`; no cleared image/document object. | None — not created |
| `EV-SRC-044` | https://www.militaryarchives.ie/en/reading-room-collections/emergency-defence-plans | Historical source family identified; no image-object permission | Same exact Emergency Defence Plans blocker as `EV-SRC-008`; no cleared period object. | None — not created |
| `EV-SRC-045` | https://www.militaryarchives.ie/en/reading-room-collections/air-defence-command | Historical source family identified; no image-object permission | Same exact Air Defence Command blocker as `EV-SRC-009`; no cleared period object. | None — not created |
| `EV-SRC-046` | https://www.met.ie/blacksod-point-and-the-d-day-forecast | Met Eireann page identifies copyrighted historical images; no project permission | Same exact Blacksod image/rights blocker as `EV-SRC-028`; no derivative-use permission. | None — not created |
| `EV-SRC-060` | https://www.difp.ie/volume-6/1940/irish-reply-to-british-proposals-for-a-united-ireland/3207/ | Historical source family identified; no image-object permission | Same exact unity-proposal/reply blocker as `EV-SRC-006`; no cleared image/document object. | None — not created |
| `EV-SRC-062` | https://www.militaryarchives.ie/en/reading-room-collections/emergency-defence-plans | Historical source family identified; no image-object permission | Same exact Emergency Defence Plans blocker as `EV-SRC-008`; no cleared period object. | None — not created |
| `EV-SRC-063` | https://www.militaryarchives.ie/en/reading-room-collections/air-defence-command | Historical source family identified; no image-object permission | Same exact Air Defence Command blocker as `EV-SRC-009`; no cleared period object. | None — not created |
| `EV-SRC-064` | https://www.met.ie/blacksod-point-and-the-d-day-forecast | Met Eireann page identifies copyrighted historical images; no project permission | Same exact Blacksod image/rights blocker as `EV-SRC-028`; no derivative-use permission. | None — not created |

The prior evidence and rejection trail for these families is retained in `docs/plans/ireland_focus_tree/assets/source_research_handoffs/blocked_event_news_round8_2026-08-01.md` and `blocked_event_news_round9_official_antecedents_2026-08-01.md`. The exact UCD P150/2548 proposal/reply lead, official FRUS text, Military Archives contextual images, and Met Eireann historical page were not silently promoted as substitutes.

## Canonical real portraits — all still blocked

The hashes below are hashes of preserved documentary leads where a source file already exists; they are not clearance hashes. The parent preservation pass archives available source originals under `docs/portraits`; that archive does not change any clearance state or promote a blocked portrait to runtime.

| Row | Source URL | Status / clearance | Exact remaining blocker | Preserved source hash |
|---|---|---|---|---|
| `P-15` John Leydon | https://en.wikipedia.org/wiki/File:John_Leydon_in_1979.png | Blocked, C2 | Explicitly non-free, late (1979), photographer/rights holder unknown; no mod reuse permission. | `d982f2f1e6f8c5213d9d149311157f1a3fd58965d3359a242ede03422c624347` |
| `P-16` Thekla Beere | https://www.irishexaminer.com/opinion/columnists/arid-41079389.html | Blocked, C2 | Department of Justice credit but no photographer, date, archive ID, open licence, or project permission. | `c0613f02a984eafcc7d22dfb666d128cdfc70ba788df9155623e0cf2cc130dd7` |
| `P-24` Luke Duffy | https://ballymoteheritage.com/wp-content/uploads/2022/04/The-Corran-Herald-issue-53-2020-2021.pdf | Blocked, C2 | Publication/courtesy lead only; no direct archive object, photographer, image licence, or project permission. | `9698c61e8eecf32e968dfc21361da14754970d070c8b946da4aff50f85003f8b` |
| `P-26` Patrick Cogan | https://historyireland.com/clann-na-talmhan-irelands-last-farmers-party/ | Blocked, C1 | Group image does not identify Cogan at face level; date, photographer, holding, rights, and licence unresolved. | `c305bcf8ac19d0b2ab1d9588f9c11c2b8e8f2b86aa99cfc57fb2c29555cb4b55` |
| `P-31` Michael Browne | https://en.wikipedia.org/wiki/File:Bishop_Michael_Browne.jpg | Blocked, C2 | Explicitly non-free 1973 image, late for the feature period, and no project-compatible permission. | `77c400dcc711a323eb371ac7d3b4ab033b158b2e3f5f95f4d5e98d0249504220` |
| `P-32` Alfred O'Rahilly | https://www.ucc.ie/en/heritage/collections/portrait-james-sinton-sleator-prha-1885-1950-alfred-orahilly.html | Blocked, C2 | Exact 1949 painting object but UCC copyright/reproduction rights are reserved; no project permission. | `e18d730b7a899ded636c17406e4afa04e66ff0a4b8479cc5eeb3d29a58d4f42a` |
| `P-38` Stephen Hayes | https://erenow.org/ww/ireland-secret-war-dan-bryan-g2-lost-tapes-reveal-hunt-ireland-nazi-spies/13.php | Blocked, C2 | Exact captioned scene is Topfoto copyright; photographer, object/date and project permission unresolved. | `119ae60087a314f109e14a273398f510c7bded8e32c3452cf9ee8135a565bbec` |
| `P-39` Hugh McAteer | https://treasonfelony.wordpress.com/2020/07/01/hugh-mcateer-1916-1970/ | Blocked, C2 | Open-web access copy of a multi-person RUC poster; archive, photographer, rights holder and permission unresolved. | `d1e10ffb3c969c97c62a6e89798916bb5c3b0e2cddf5962559357fa8c65b8df5` |
| `P-41` Harry White | https://www.militaryarchives.ie/en/reading-room-collections/uinseann-mac-eoin-collection | Blocked, C2 | Official archive series lead but no image-level licence, capture date, photographer or project permission. | `10c7f24ba755a23260b62898d00f7cc10ffd8ea56363451f4962acff98e5ce1c` |
| `P-45` Mick Fitzpatrick | https://www.oireachtas.ie/en/members/member/Michael-Fitzpatrick.D.1948-02-18/ | Blocked, C1 | Identity page exposes no exact portrait; no subject-labelled object, date, photographer, rights or permission. | None — no portrait object created |
| `P-48` Roddy Connolly | https://www.opendemocracy.net/en/easter-rising-and-soviet-union-untold-chapter-in-ireland-s-great-rebellion/ | Blocked, C2 | Article notice does not independently license the embedded historical photo; group identification, original holding and image rights unresolved. | `86d366015e35853dcbaf9582b999e19648c5cacb24ba8dc05da9fbeab2606c27` |
| `P-50` Michael Price | https://www.dib.ie/biography/price-michael-mick-a7501 | Blocked, C1 | DIB is an identity lead only; no exact portrait object, photographer or reuse terms. | None — no portrait object created |
| `P-54` P. J. Coughlan | https://www.dib.ie/biographies | Blocked, C1 | Identity lead only; no exact portrait object, photographer or reuse terms. | None — no portrait object created |
| `P-55` Liam D. Walsh | https://www.dib.ie/biographies | Blocked, C1 | Identity lead only; no exact portrait object, photographer or reuse terms. | None — no portrait object created |
| `P-57` Tomas O Dochartaigh | https://historyireland.com/ailtiri-na-haiseirghe-irelands-fascist-new-order/ | Blocked, C2 | Exact captioned Military Archives portrait lead, but accession, photographer/date, image rights and permission unresolved. | `8a7dd4c68884318c79985bacd5a64e1bb29c2b9e666c380f26c46c1108b82f44` |

No exact portrait source met the required provenance and clearance threshold. No generated likenesses were made.

## Remaining symbol/document rows

`S-07` is cleared above. The following 14 rows remain blocked; each has `source_path=not_created`, no source/processed/DDS hash, and no exact cleared image object staged.

| Row | Source URL | Status / clearance | Exact remaining blocker | Hashes |
|---|---|---|---|---|
| `S-06` Fianna Fail | https://catalogue.nli.ie/Record/vtls000277076 | Blocked, C2 restricted/review | Exact NLI objects exist, but NLI reproduction rights are controlled; no project permission. | None — not created |
| `S-08` Labour Party | https://catalogue.nli.ie/Record/vtls000544507 | Blocked, C2 restricted/review | Exact 1930 object exists, but NLI-controlled reproduction rights are unresolved. | None — not created |
| `S-09` National Labour | https://catalogue.nli.ie/Record/vtls000768688 | Blocked, C2 restricted/review | Object metadata is strong but principal object is undated and NLI reproduction rights are unresolved. | None — not created |
| `S-10` Clann na Talmhan | https://www.nli.ie/collections | Blocked, C1 provenance | Collection direction only; no exact object, photography terms or permission. | None — not created |
| `S-12` Easter lily/commemorative material | https://catalogue.nli.ie/Record/vtls000506667 | Blocked, C2 restricted/review | Exact NLI notice is controlled; it must not be conflated with a proclamation or generic symbol. | None — not created |
| `S-15` Republican Congress / Starry Plough | https://catalogue.nli.ie/Record/vtls000507859 | Blocked, C2 restricted/review | Exact handbill is controlled and is not itself a cleared Starry Plough image; contextual sources do not grant image reuse. | None — not created |
| `S-17` National Corporate Party | https://www.nli.ie/collections | Blocked, C1 provenance | Research direction only; no exact object, rights holder or permission. | None — not created |
| `S-18` Ailtiri na hAiseirghe | https://catalogue.nli.ie/Record/vtls000263764/StaffViewMARC | Blocked, C2 restricted/review | Exact period objects are identified, but scan/image rights are not project-compatible; modern emblem reconstructions rejected. | None — not created |
| `S-20` Fainne | https://catalogue.nli.ie/Record/vtls000517326/StaffViewMARC | Blocked, C2 restricted/review | Exact period handbill lead, but NLI rights are controlled and date is a range. | None — not created |
| `S-23` Muintir na Tire | https://www.nli.ie/collections | Blocked, C1 provenance | Collection/research direction only; no exact object photography terms or permission. | None — not created |
| `S-26` Local Security Force | https://www.nli.ie/collections | Blocked, C1 provenance | No exact LSF armband/form/photo with compatible rights. The public-domain LDF photograph is a different organisation and was not substituted. | None — not created |
| `S-28` Coast Watching Service / EIRE markers | https://www.militaryarchives.ie/en/reading-room-collections/lookout-post-logbooks | Blocked, C1 provenance | Exact collection lead, but no cleared logbook/page/marker object or image permission. | None — not created |
| `S-30` Marine Service | https://www.nli.ie/collections | Blocked, C1 provenance | No exact reusable insignia/vessel/admin object or permission. | None — not created |
| `S-33` Treaty Port transfer | https://www.difp.ie/volume-5/1938/transfer-of-treaty-ports/2338/ | Blocked, C1 provenance | Exact record family lead, but no cleared document/map/photo object or reproduction terms. | None — not created |

## Files changed

Created the new researcher staging package under:

`assets/ireland_focus_tree/sourced/research_2026-08-01/source_clearance_researcher/`

It contains the exact S-07 source object, two source-page captures, Commons metadata evidence, a Maynooth contextual research PDF retained only as a rejection record for the Blacksod pass, crop candidates/contact sheet, processed preview, DDS review copy, runtime DDS promotion, and `gfx_handoff.md`.

Updated:

- `docs/plans/ireland_focus_tree/assets/source_manifest.json` — S-07 only, preserving the existing schema and recording the alternate object, C3 condition, provenance, paths, crop, dimensions and hashes.
- `docs/plans/ireland_focus_tree/subagent_handoffs/ireland_source_clearance_researcher_2026-08-01.md` — this per-row status and blocker handoff.

No portrait was cleared or added by this source-clearance pass; S-07 is not a portrait source. The parent preservation archive under `docs/portraits` remains intact and separate from this package. No unrelated files were reverted or overwritten.

## Validation performed

- Parsed `source_manifest.json` as JSON and confirmed 169 entries.
- Confirmed the post-promotion counts: 125 complete and 44 blocked; 15 blocked event/news rows remain; 15 blocked portraits remain; 14 blocked symbols remain.
- Verified the exact S-07 source object is 528x652 and the selected processed preview is 397x153 RGBA.
- Ran the mandated `convert_to_dds.py` workflow for the 397x153 processed preview and verified the staging and runtime DDS SHA-256 values.
- Verified the runtime DDS was copied only after manifest promotion and that no prior target file was overwritten.
- Computed/recorded documentary-source hashes for existing blocked portrait leads for audit identity; these hashes do not imply clearance.
- No live in-game test was run, as requested.

## Remaining safe next action

Only an exact object-level licence/permission or an exact public-domain/compatible source record can clear the remaining rows. In particular, the event/news families need written project-compatible permission from the relevant archive/rights holder or a newly located exact object with documented reuse terms. Do not fill the 15 event/news gaps with generated, duplicate, generic, modern, or adjacent diplomatic imagery.
