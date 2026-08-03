# Ireland event/news source-clearance handoff — 2026-07-22

This is a static sourced-asset handoff for the Ireland overhaul. It covers only archival/public-domain source research, source originals, processed previews, DDS outputs, metadata, and contact sheets under `assets/ireland_focus_tree/sourced`.

Reconciliation note (2026-07-22): the authoritative manifest now marks `EV-SRC-002`, `EV-SRC-003`, `EV-SRC-005`, `EV-SRC-014`, and `EV-SRC-019` complete, with their runtime final DDS files under `gfx/event_pictures/ireland/`. `EV-SRC-004`, `EV-SRC-032`, `EV-SRC-039`, and `EV-SRC-040` remain blocked despite retained review-package files; those candidates are not registered as runtime art. The slot table below is retained as historical research evidence and does not override `source_manifest.json`.

The authoritative manifest and clearance audit were not edited. All existing C1/C2/C3/C4 states are preserved; “candidate” below means that this package contains evidence for the main agent to review, not that a manifest state has been promoted. No gameplay, GFX, localisation, existing handoff, or HOI4 installation was touched.

## Result

- At handoff generation, six slot-aligned packages had source originals, processed PNGs, and final DDS files: `EV-SRC-003`, `EV-SRC-004`, `EV-SRC-019`, `EV-SRC-032`, `EV-SRC-039`, and `EV-SRC-040`. The reconciliation note above supersedes their runtime-clearance interpretation.
- `EV-SRC-010` and `EV-SRC-016` have exact source originals and processed previews only. Both remain rights-restricted review packages while their authoritative manifest entries stay C1; no final DDS is provided for them.
- `EV-SRC-008`, `EV-SRC-009`, and `EV-SRC-027` were not presented as substitutes: the available LDF and Northern Ireland ARP material does not match their manifest subjects. `EV-SRC-036` is an exact duplicate of the already packaged `EV-SRC-018` source.
- The current blocked event/news count is 43; the authoritative list is recorded in `source_manifest.json` and the full historical list below remains evidence only.

The review sheets are [the six slot-aligned candidates](../../../../assets/ireland_focus_tree/sourced/contact_sheet_event_source_clearance_2026-07-22.png) and [the review-only candidates](../../../../assets/ireland_focus_tree/sourced/contact_sheet_event_source_review_2026-07-22.png).

## Slot-aligned packages

All report outputs are `210x176` RGBA PNG/DDS targets. All news outputs are `397x153` RGB PNG/DDS targets.

| Slot | Exact source and evidence | Package state (manifest unchanged) | Source → processed PNG → DDS | Intended sprite |
|---|---|---|---|---|
| `EV-SRC-003` | [Admiralty House, Cobh, NLI L_CAB_02581 / Robert French](https://commons.wikimedia.org/wiki/File:Admiralty_House_Cobh_(27775479161).jpg), circa 1885. NLI record reports no known copyright restrictions. | Conditional archival candidate. Exact treaty-port site context, but not the 1938 transfer record itself. | `source_originals/event_ev_src_003_admiralty_house_cobh_1885.jpg` (2000×1359) → `processed_png/event_ev_src_003_report.png` (210×176) → `gfx/event_pictures/ireland/event_ev_src_003_report.dds` (210×176). | `ireland_report_historical_chain_report_03` |
| `EV-SRC-004` | [Éamon de Valera, 1939](https://commons.wikimedia.org/wiki/File:De_Valera,_1939.jpg), UCD object `ivrla:31220`; unknown Irish Press photographer. Commons reports PD in Ireland, but UCD reproduction terms need confirmation. | Conditional archival candidate. Exact neutrality-period political portrait, not the neutrality policy record. | `source_originals/event_ev_src_004_de_valera_1939.jpg` (838×634) → `processed_png/event_ev_src_004_report.png` (210×176) → `gfx/event_pictures/ireland/event_ev_src_004_report.dds` (210×176). | `ireland_report_historical_chain_report_04` |
| `EV-SRC-019` | [Constitution (Consequential Provisions) Bill 1937](https://data.oireachtas.ie/ie/oireachtas/bill/1937/41/eng/ver_a/bills1936-37-1pp-02.pdf), Oireachtas Bill 1937/41, version a. | Conditional official-document candidate. Exact 1937 constitutional source; reuse terms for the scan were not separately established. | `source_originals/event_ev_src_019_constitution_consequential_provisions_bill_1937.pdf` plus page-1 render (1730×2790) → `processed_png/event_ev_src_019_report.png` (210×176) → `gfx/event_pictures/ireland/event_ev_src_019_report.dds` (210×176). | `ireland_report_constitutional_crisis_report_01` |
| `EV-SRC-032` | [Tregothnan, MAS asset nKWUWYcJI9AinIVWSSzVTZjc](https://commons.wikimedia.org/wiki/File:Tregothnan,_asset_nKWUWYcJI9AinIVWSSzVTZjc.jpg), [MAS object](https://dams.antwerpen.be/asset/nKWUWYcJI9AinIVWSSzVTZjc), Louis Claes, date unknown. Record supports historical old-work/US-expiry public-domain rationale. | Conditional archival candidate. Vessel was renamed Irish Larch in 1941, but this photograph is under the earlier name and its date is unknown. | `source_originals/event_ev_src_014_irish_larch_tregothnan_unknown_date.jpg` (1200×749) → `processed_png/event_ev_src_032_news.png` (397×153) → `gfx/event_pictures/ireland/event_ev_src_032_news.dds` (397×153). | `ireland_news_historical_news_02` |
| `EV-SRC-039` | [HMS Warspite at Queenstown/Cobh](https://commons.wikimedia.org/wiki/File:H.M.S._Warspite_at_Queenstown,_now_Cobh_(7836986082).jpg), NLI on The Commons, circa 1894; record reports no known copyright restrictions. | Conditional archival candidate. Exact Queenstown treaty-port naval context, but predates the 1938 transfer and is not the transfer document. | `source_originals/event_ev_src_005_hms_warspite_queenstown_1894.jpg` (1023×779) → `processed_png/event_ev_src_039_news.png` (397×153) → `gfx/event_pictures/ireland/event_ev_src_039_news.dds` (397×153). | `ireland_news_historical_news_09` |
| `EV-SRC-040` | [Fianna Fáil Cabinet, circa 1940–1944](https://commons.wikimedia.org/wiki/File:Fianna_F%C3%A1il_Cabinet_circa_1940_to_1944.jpg), UCD object `ivrla:31226`; unknown Irish Press photographer. Commons reports PD in Ireland, but UCD reproduction terms need confirmation. | Conditional archival candidate. Exact circa-1944 government context, not a scan of the neutrality record. | `source_originals/event_ev_src_022_fianna_fail_cabinet_1944.jpg` (1200×893) → `processed_png/event_ev_src_040_news.png` (397×153) → `gfx/event_pictures/ireland/event_ev_src_040_news.dds` (397×153). | `ireland_news_historical_news_10` |

The full per-item provenance, rights notes, uncertainty, hashes, processing, and reuse limits are in [event_source_clearance_metadata_2026-07-22.json](../../../../assets/ireland_focus_tree/sourced/event_source_clearance_metadata_2026-07-22.json).

### Processing record

- Report cards were processed with `.agents/skills/hoi4-feature-assets/tools/process_report_event_image.py`, preserving the required 210×176 report-card treatment and transparent edge/card styling.
- News banners were cropped with PIL `ImageOps.fit` to 397×153, converted to grayscale with autocontrast, and saved as RGB PNGs.
- The Oireachtas PDF and Northern Ireland PDF were rendered to page previews with `pdftoppm`; the Northern Ireland result is review/not-allocated and is not a final package.
- The six final DDS files were produced with `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py`. C2 review material has no final DDS assignment.

## Review-only and not-allocated material

### Rights-restricted exact sources

- `EV-SRC-010`: [Met Éireann Blacksod page](https://www.met.ie/blacksod-point-and-the-d-day-forecast) identifies the 1942 station image as “Photo: F.E. Dixon. Copyright: Met Éireann” and gives the 3 June 1944 observation sheet. Originals and processed previews exist under `source_originals/` and `processed_png/`; rights review remains open and no DDS is assigned.
- `EV-SRC-016`: [Dúchas CBÉ 0689 page 078](https://www.duchas.ie/en/cbe/9002797/7355941/9132750) is dated 23 September 1938 and identifies the material as © National Folklore Collection, UCD. The [Dúchas licensing guide](https://bba.duchas.ie/assets/pdf/2023.01.04-bba-licensing-guidelines.pdf) is retained as the licensing reference. Originals and a processed preview exist; rights review remains open and no DDS is assigned.

### Authentic but wrong-subject or duplicate sources

- `EV-SRC-008`: [LDF 01](https://commons.wikimedia.org/wiki/File:Two_volunteers_for_the_Irish_Local_Defence_Force_aka_LDF_01.jpg) is the reverse of the photograph with handwritten identification/stamp. It is rejected for use.
- `EV-SRC-009`: [LDF 02](https://commons.wikimedia.org/wiki/File:Two_volunteers_for_the_Irish_Local_Defence_Force_aka_LDF_02.jpg) is authentic circa-1940 public-domain material by Roe McMahon, but it depicts Local Defence Force volunteers, not the manifest's Air Defence Command subject. It is retained under `sourced/review/not_allocated_*` and must not be wired to `EV-SRC-009` without parent approval.
- `EV-SRC-027`: [Northern Ireland Air Raid Precautions Regulations 1938](https://www.legislation.gov.uk/nisro/1938/137/pdfs/nisro_19380137_en.pdf) is an official period source under OGL 3.0 conditions, but it is not the manifest's Irish Air Defence Command record. It is retained under `sourced/review/not_allocated_*` and must not be wired to `EV-SRC-027`.
- `EV-SRC-036`: [Romantic Ireland (1905), Stone of the Divisions](https://commons.wikimedia.org/wiki/File:Romantic_Ireland_(1905)_(14769773905).jpg) is byte-for-byte identical to the existing `EV-SRC-018` source. It is retained as a duplicate review file, with no new processed or DDS output.
- At handoff generation, the Warspite original was downloaded under an `EV-SRC-005` filename but was packaged once as `EV-SRC-039`; the Tregothnan original was downloaded under `EV-SRC-014` but was packaged once as `EV-SRC-032`; the Cabinet original was downloaded under `EV-SRC-022` but was packaged once as `EV-SRC-040`. This avoided violating the distinct-image allocation rule at that time. The reconciliation note above supersedes the old slot-status wording.

## Blocked slot audit and source-package gaps

The historical handoff listed these 48 blocked EV-SRC slots; the current authoritative manifest has reconciled the five newly cleared tranche rows above:

```text
EV-SRC-002, EV-SRC-003, EV-SRC-004, EV-SRC-005, EV-SRC-006,
EV-SRC-007, EV-SRC-008, EV-SRC-009, EV-SRC-010, EV-SRC-014,
EV-SRC-016, EV-SRC-019, EV-SRC-020, EV-SRC-021, EV-SRC-022,
EV-SRC-023, EV-SRC-024, EV-SRC-025, EV-SRC-026, EV-SRC-027,
EV-SRC-028, EV-SRC-032, EV-SRC-034, EV-SRC-036, EV-SRC-037,
EV-SRC-038, EV-SRC-039, EV-SRC-040, EV-SRC-041, EV-SRC-042,
EV-SRC-043, EV-SRC-044, EV-SRC-045, EV-SRC-046, EV-SRC-050,
EV-SRC-052, EV-SRC-054, EV-SRC-055, EV-SRC-056, EV-SRC-057,
EV-SRC-058, EV-SRC-059, EV-SRC-060, EV-SRC-061, EV-SRC-062,
EV-SRC-063, EV-SRC-064, EV-SRC-068
```

The remaining gaps are source-object and rights gaps, not image-generation gaps:

| Source family | Affected slots | Gap |
|---|---|---|
| DIFP diplomatic records | `EV-SRC-002`, `005`, `006`, `020`–`024`, `038`, `041`, `042`, `055`–`060` | [DIFP's 1938 tripartite agreement](https://www.difp.ie/volume-5/1938/british-irish-tripartite-agreement-on-trade-finance-and-defence/2321/), [Treaty Port transfer page](https://www.difp.ie/volume-5/1938/transfer-of-treaty-ports/2338/), [neutrality record](https://www.difp.ie/volume-6/1939/irish-neutrality/2496/), [1940 unity reply](https://www.difp.ie/volume-6/1940/irish-reply-to-british-proposals-for-a-united-ireland/3207/), and [1941 Treaty Port claims](https://www.difp.ie/volume-7/1941/the-treaty-ports-and-the-battle-of-the-atlantic-britains-claims/3437/) establish exact documents and dates, but no reusable image object and rights statement were found on the pages. No document scans were invented.
| Military Archives | `EV-SRC-007`–`009`, `025`–`027`, `043`–`045`, `061`–`063` | The [Lookout Post Logbooks](https://www.militaryarchives.ie/en/reading-room-collections/lookout-post-logbooks), [Emergency Defence Plans](https://www.militaryarchives.ie/en/reading-room-collections/emergency-defence-plans), and [Air Defence Command](https://www.militaryarchives.ie/en/reading-room-collections/air-defence-command) pages establish the 1939–1945 fonds, but no exact downloadable image object with reuse terms was found. Wrong-subject LDF/ARP material remains review only.
| Blacksod and Schools Collection | `EV-SRC-010`, `016`, `028`, `034`, `046`, `052`, `064` | Exact objects exist, but Met Éireann and National Folklore Collection/UCD rights require restricted/review treatment. The manifest entries remain C1 and no DDS was made for those objects.
| Uisneach | `EV-SRC-036`, `054` | The exact 1905 Stone of the Divisions source duplicates `EV-SRC-018`; modern tourism/event photos were rejected. A distinct archival source is still missing.
| News/flavour-family breadth | `EV-SRC-032`, `034`, `036`–`043`, `050`, `052`, `054`–`064`, `068` | Six slot-aligned packages are staged, but the remaining news/flavour allocations need distinct source objects. Controlled reuse cannot become one generic image across the family.

## GFX handoff

The main agent owns `.gfx` edits. Proposed target is the event/news picture GFX file selected by the main agent; `interface/slopx_ireland_event_art.gfx` is a suggested grouping name only. The snippets below are ready to copy after the target file is confirmed:

```text
spriteType = {
	name = "GFX_ireland_report_historical_chain_report_03"
	texturefile = "gfx/event_pictures/ireland/event_ev_src_003_report.dds"
}

spriteType = {
	name = "GFX_ireland_report_historical_chain_report_04"
	texturefile = "gfx/event_pictures/ireland/event_ev_src_004_report.dds"
}

spriteType = {
	name = "GFX_ireland_report_constitutional_crisis_report_01"
	texturefile = "gfx/event_pictures/ireland/event_ev_src_019_report.dds"
}

spriteType = {
	name = "GFX_ireland_news_historical_news_02"
	texturefile = "gfx/event_pictures/ireland/event_ev_src_032_news.dds"
}

spriteType = {
	name = "GFX_ireland_news_historical_news_09"
	texturefile = "gfx/event_pictures/ireland/event_ev_src_039_news.dds"
}

spriteType = {
	name = "GFX_ireland_news_historical_news_10"
	texturefile = "gfx/event_pictures/ireland/event_ev_src_040_news.dds"
}
```

Do not wire the `sourced/review/` files. Before release, the main agent should decide whether each conditional candidate has sufficient rights evidence, record any approved clearance transition in the authoritative manifest, and keep the source credit/semantic caveat with the asset documentation.
