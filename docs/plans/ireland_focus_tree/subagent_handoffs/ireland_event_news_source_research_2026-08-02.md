# Ireland event/news source research handoff - 2026-08-02

## Status

Incomplete and blocked. This handoff covers only the 15 assigned rows:

`EV-SRC-006`, `EV-SRC-008`, `EV-SRC-009`, `EV-SRC-024`, `EV-SRC-026`,
`EV-SRC-027`, `EV-SRC-028`, `EV-SRC-042`, `EV-SRC-044`, `EV-SRC-045`,
`EV-SRC-046`, `EV-SRC-060`, `EV-SRC-062`, `EV-SRC-063`, and `EV-SRC-064`.

Every row now has a concrete, provenance-traced research source in the repo,
a processed review PNG, a source tier, an explicit clearance state, and a
row-level license/uncertainty note in the package manifest. No row has a
cleared runtime asset: all four UCD rows and all eight Military Archives rows
are C1, and all three Blacksod rows are C2. Consequently, no final DDS was
created.

## Authoritative package files

- [Row manifest](../../../../assets/ireland_focus_tree/sourced/research_2026-08-02_blocked_event_news_ireland/source_manifest_2026-08-02.json)
  contains the source URL, holding, catalogue/object lead, creator/date,
  rights and license note, required credit, crop/use note, uncertainty,
  source path, evidence path, processed path, DDS state, sprite name, and
  controlled-reuse note for every row.
- [Canonical Ireland asset manifest](../assets/source_manifest.json) now points
  all 15 assigned entries to their local source originals and review PNGs while
  preserving `status: blocked` and `final_dds_path: not_created`.
- [Review contact sheet](../../../../assets/ireland_focus_tree/sourced/research_2026-08-02_blocked_event_news_ireland/contact_sheet/blocked_event_news_ireland_2026-08-02.png)
  shows one labeled 210x176/397x153 review card for each assigned row.
- [GFX handoff](../../../../assets/ireland_focus_tree/sourced/research_2026-08-02_blocked_event_news_ireland/gfx_handoff.md)
  records proposed sprite names, target sizes, review paths, and the reason no
  ready-to-copy runtime snippet is supplied.

## Direct provenance and clearance result

### UCD correspondence scans - EV-SRC-006, EV-SRC-024, EV-SRC-042, EV-SRC-060

The source is the UCD Cultural Heritage Collections presentation of UCD
Archives object `P150/2548`, with the related record cross-checked against the
Documents on Irish Foreign Policy page. The pages are exact scans of the 1940
British unity proposal / Irish reply correspondence context, including the
26 June proposal and 4 July reply. The four pages are distinct local source
files, not generated substitutes.

- Primary presentation: [UCD Cultural Heritage Collections](https://ucdculturalheritagecollections.com/2025/05/02/internal-weakness-and-eventual-frustration-eamon-de-valera-neville-chamberlain-and-irish-neutrality/)
- Related text/provenance record: [DIFP, Irish reply to British proposals for a united Ireland](https://www.difp.ie/volume-6/1940/irish-reply-to-british-proposals-for-a-united-ireland/3207/)
- Clearance: C1, provenance identified. The presentation does not state an
  image-level derivative-use or project-use license, and underlying document
  rights are not established for mod redistribution. Written permission or a
  user-approved conditional use decision is required before DDS conversion.

### Irish Defence Forces planning leads - EV-SRC-008, EV-SRC-026, EV-SRC-044, EV-SRC-062

The source holding is the Military Archives. The local files are rendered
pages from the official `18th Military Mission` finding aid, including the
`18th-MM-002` lead for the 26 May 1940 disposition of Defence Forces and the
finding-aid text covering July 1940 invasion planning, the Donegal/Lough
Swilly question, and General Defence Plan No. 2. These are concrete official
archival provenance leads and period-relevant review sources, but they are
finding-aid pages rather than scans of the underlying plan objects.

- Primary finding-aid page: [Military Archives - 18th Military Mission](https://www.militaryarchives.ie/en/reading-room-collections/18th-military-mission)
- Local evidence PDF: `assets/ireland_focus_tree/sourced/research_2026-08-02_blocked_event_news_ireland/evidence/18th-Military-Mission.pdf`
- Clearance: C1, provenance identified. The official finding aid supplies the
  archive and catalogue lead but does not grant republication or derivative
  use of an underlying plan scan. The local page renders are research/review
  evidence only; the main agent must obtain the underlying object scan and
  permission, or record an explicitly approved conditional-use decision.

### Air Defence Command leads - EV-SRC-009, EV-SRC-027, EV-SRC-045, EV-SRC-063

The source holding is the Military Archives Air Defence Command collection.
The official finding aid identifies the relevant object groups, including
`ADC-001`, `ADC-010/012`, `ADC-018/020`, and `ADC-024`. The local files are
rendered pages from that official finding aid and are not presented as scans
of the underlying plan objects.

- Primary collection page: [Military Archives - Air Defence Command](https://www.militaryarchives.ie/en/reading-room-collections/air-defence-command)
- Local evidence PDF: `assets/ireland_focus_tree/sourced/research_2026-08-02_blocked_event_news_ireland/evidence/Air-Defence-Command.pdf`
- Clearance: C1, provenance identified. No object-level historical image and
  no project-use/republication permission was established. The local pages
  are evidence/review files only and must not be wired as cleared runtime art.

### Blacksod observation sheet - EV-SRC-028, EV-SRC-046, EV-SRC-064

All three rows point to the same underlying historical object: the 3 June
1944 Blacksod observation sheet used in the D-Day weather record. The package
keeps three provenance-traced variants for review, but they are not three
independent clearances:

- Primary page: [Met Eireann - Blacksod Point and the D-Day forecast](https://www.met.ie/blacksod-point-and-the-d-day-forecast)
- Local Met image: `source_originals/blacksod_observation_sheet_1333px.jpg`
- Local Met thumbnail: `source_originals/blacksod_observation_sheet_300x190_met.jpg`
- Secondary rehost used only for comparison: [D-Day Overlord weather file](https://www.dday-overlord.com/en/d-day/files/the-d-day-weather-6-june-1944-normandy-landings)
- Clearance: C2, restricted/review pending. Met Eireann's copyright notice
  applies, and neither the Met page nor the rehost grants the mod an explicit
  project-use or derivative-use license. Written permission is required. The
  rehost does not improve clearance and is not treated as a separate source.

## Per-item handoff map

Paths below are relative to the repository root. The full row metadata is in
the package manifest linked above.

| ID | Tier / clearance | Local source file | Local processed review | Proposed sprite | DDS |
| --- | --- | --- | --- | --- | --- |
| EV-SRC-006 | T4 / C1 | `.../source_originals/EV-SRC-006_P150-2548_page-0001.jpg` | `.../processed_png/review_cards/EV-SRC-006_P150-2548_page-0001_report_event.png` | `ireland_report_historical_chain_report_06` | not created |
| EV-SRC-008 | T1 / C1 | `.../source_originals/18th_military_mission_page-03.png` | `.../processed_png/review_cards/18th_military_mission_page-03_report_event.png` | `ireland_report_historical_chain_report_08` | not created |
| EV-SRC-009 | T1 / C1 | `.../source_originals/air_defence_command_finding_aid_page-01.png` | `.../processed_png/review_cards/air_defence_command_finding_aid_page-01_report_event.png` | `ireland_report_historical_chain_report_09` | not created |
| EV-SRC-024 | T4 / C1 | `.../source_originals/EV-SRC-024_P150-2548_page-0002.jpg` | `.../processed_png/review_cards/EV-SRC-024_P150-2548_page-0002_report_event.png` | `ireland_report_constitutional_crisis_report_06` | not created |
| EV-SRC-026 | T1 / C1 | `.../source_originals/18th_military_mission_page-04.png` | `.../processed_png/review_cards/18th_military_mission_page-04_report_event.png` | `ireland_report_constitutional_crisis_report_08` | not created |
| EV-SRC-027 | T1 / C1 | `.../source_originals/air_defence_command_finding_aid_page-04.png` | `.../processed_png/review_cards/air_defence_command_finding_aid_page-04_report_event.png` | `ireland_report_constitutional_crisis_report_09` | not created |
| EV-SRC-028 | T1 / C2 | `.../source_originals/blacksod_observation_sheet_1333px.jpg` | `.../processed_png/review_cards/blacksod_observation_sheet_1333px_report_event.png` | `ireland_report_constitutional_crisis_report_10` | not created |
| EV-SRC-042 | T4 / C1 | `.../source_originals/EV-SRC-042_P150-2548_page-0006.jpg` | `.../processed_png/news_review/EV-SRC-042_news_review.png` | `ireland_news_historical_news_12` | not created |
| EV-SRC-044 | T1 / C1 | `.../source_originals/18th_military_mission_page-05.png` | `.../processed_png/review_cards/18th_military_mission_page-05_report_event.png` | `ireland_report_flavour_family_01` | not created |
| EV-SRC-045 | T1 / C1 | `.../source_originals/air_defence_command_finding_aid_page-05.png` | `.../processed_png/review_cards/air_defence_command_finding_aid_page-05_report_event.png` | `ireland_report_flavour_family_02` | not created |
| EV-SRC-046 | T1 / C2 | `.../source_originals/blacksod_observation_sheet_1024x648_dday_overlord.jpg` | `.../processed_png/review_cards/blacksod_observation_sheet_1024x648_dday_overlord_report_event.png` | `ireland_report_flavour_family_03` | not created |
| EV-SRC-060 | T4 / C1 | `.../source_originals/EV-SRC-060_P150-2548_page-0007.jpg` | `.../processed_png/review_cards/EV-SRC-060_P150-2548_page-0007_report_event.png` | `ireland_report_flavour_family_17` | not created |
| EV-SRC-062 | T1 / C1 | `.../source_originals/18th_military_mission_page-06.png` | `.../processed_png/review_cards/18th_military_mission_page-06_report_event.png` | `ireland_report_flavour_family_19` | not created |
| EV-SRC-063 | T1 / C1 | `.../source_originals/air_defence_command_finding_aid_page-07.png` | `.../processed_png/review_cards/air_defence_command_finding_aid_page-07_report_event.png` | `ireland_report_flavour_family_20` | not created |
| EV-SRC-064 | T1 / C2 | `.../source_originals/blacksod_observation_sheet_300x190_met.jpg` | `.../processed_png/review_cards/blacksod_observation_sheet_300x190_met_report_event.png` | `ireland_report_flavour_family_21` | not created |

The `.../` prefix in the table means:
`assets/ireland_focus_tree/sourced/research_2026-08-02_blocked_event_news_ireland/`.

## Processing and review notes

- All report rows were passed through
  `.agents/skills/hoi4-feature-assets/tools/process_report_event_image.py`
  and have 210x176 RGBA review PNGs.
- EV-SRC-042 has a separate 397x153 RGB news review crop from the exact UCD
  page 0006 source. It was not promoted to DDS because it is C1.
- The contact sheet is review-only and is not a runtime asset.
- No AI-generated or generated-substitute image was used.
- No gameplay file, `.gfx` file, localisation file, or unrelated asset was
  edited by this pass.

## Required next clearance action

The source package is ready for a permission decision, not for runtime wiring.
Obtain written project-use/derivative-use permission from UCD or the relevant
rights holder for the P150/2548 pages, from Military Archives for underlying
EDP/ADC objects, and from Met Eireann for the Blacksod sheet. If the project
owner intentionally accepts conditional local-mod use, record that approval
per row and retain the required archive/credit wording. Only after that review
should the rows advance to C3/C4, be processed again as final art if needed,
and receive DDS files.
