# Ireland P0 family conclusion report-event art manifest

Feature: `ireland_country_package`

Asset package: `ireland_p0_family_conclusion_reports`

Target surface: HOI4 report-event picture, finished `210x176` RGBA canvas.

Runtime wiring status: all five report sprites are registered in
`interface/ireland_event_art.gfx` and consumed by
`events/ireland_country_conclusion_events.txt` events `.1` through `.5`.
The separate family-lane focus layout is accepted at `89ff719`; this asset
status does not replace the parent completion audit.

Processing: source artwork was passed through `.agents/skills/hoi4-feature-assets/tools/process_report_event_image.py`, which applies the report-event card treatment (cover crop, black-and-white conversion, sepia, grain, paper edge, deterministic tilt, transparent margins, and soft shadow). Each processed PNG was converted with `convert_to_dds.py` using `--width 210 --height 176`.

## Assets

| Status | Sprite ID | Source mode | Source PNG | Processed PNG | Final DDS |
| --- | --- | --- | --- | --- | --- |
| complete | `GFX_report_event_ireland_postwar_democratic_settlement` | archival, public-domain-tagged source | `docs/assets/ireland_p0_family_conclusion_reports/source_png/report_event_ireland_postwar_democratic_settlement_source.png` | `docs/assets/ireland_p0_family_conclusion_reports/processed_png/report_event_ireland_postwar_democratic_settlement.png` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_democratic_settlement.dds` |
| complete | `GFX_report_event_ireland_postwar_congress_settlement` | generated | `docs/assets/ireland_p0_family_conclusion_reports/source_png/report_event_ireland_postwar_congress_settlement_source.png` | `docs/assets/ireland_p0_family_conclusion_reports/processed_png/report_event_ireland_postwar_congress_settlement.png` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_congress_settlement.dds` |
| complete | `GFX_report_event_ireland_postwar_blueshirt_settlement` | generated | `docs/assets/ireland_p0_family_conclusion_reports/source_png/report_event_ireland_postwar_blueshirt_settlement_source.png` | `docs/assets/ireland_p0_family_conclusion_reports/processed_png/report_event_ireland_postwar_blueshirt_settlement.png` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_blueshirt_settlement.dds` |
| complete | `GFX_report_event_ireland_postwar_producer_estates_settlement` | generated | `docs/assets/ireland_p0_family_conclusion_reports/source_png/report_event_ireland_postwar_producer_estates_settlement_source.png` | `docs/assets/ireland_p0_family_conclusion_reports/processed_png/report_event_ireland_postwar_producer_estates_settlement.png` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_producer_estates_settlement.dds` |
| complete | `GFX_report_event_ireland_postwar_restoration_settlement` | generated | `docs/assets/ireland_p0_family_conclusion_reports/source_png/report_event_ireland_postwar_restoration_settlement_source.png` | `docs/assets/ireland_p0_family_conclusion_reports/processed_png/report_event_ireland_postwar_restoration_settlement.png` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_restoration_settlement.dds` |

## Democratic source record

The democratic image is a cropped still taken at approximately 00:40 from the British Movietone newsreel **“Ireland's New Premier” – John Costello elected Taoiseach, February 1948**. The source page identifies the footage as British Movietone, dated 17 February 1948, and records a Public domain / `PD-UK` / `PD-1996` status. The source frame was cropped to the central group to remove the visible AP corner mark before report-card processing; no generated content was added.

- Wikimedia Commons file page: <https://commons.wikimedia.org/wiki/File:%22Ireland%27s_New_Premier%22_-_John_Costello_elected_Taoiseach,_February_1948.webm>
- Direct source media: <https://upload.wikimedia.org/wikipedia/commons/2/2e/%22Ireland%27s_New_Premier%22_-_John_Costello_elected_Taoiseach%2C_February_1948.webm>
- Commons metadata credit: British Movietone; original YouTube source is linked from the file page.
- Rights note: the final asset relies on the public-domain status recorded on the Commons file page; retain this source record with the package if the image is redistributed.

## Generated-source rationale

The congress, Blueshirt, producer-estates, and restoration scenes are fictional alternate-history settlements with no single real archive photograph that could depict the requested event families. They were generated as period documentary source photographs, then processed into the shared HOI4 report-event card treatment. The generated images contain no readable text, labels, watermarks, or modern objects.

## Reference and review

The canonical report-art reference folder and contact sheet were inspected before production:

`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`

The package contact sheet is `docs/assets/ireland_p0_family_conclusion_reports/contact_sheet.png`.
