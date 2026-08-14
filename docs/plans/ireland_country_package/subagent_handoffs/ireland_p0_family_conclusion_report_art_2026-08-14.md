# Handoff: Ireland P0 family conclusion report-event art

Date: 2026-08-14

Status: complete for all five requested static report-event images.

## Deliverables

- Source PNGs: `docs/assets/ireland_p0_family_conclusion_reports/source_png/`
- Processed `210x176` RGBA PNGs: `docs/assets/ireland_p0_family_conclusion_reports/processed_png/`
- Final DDS textures: `gfx/event_pictures/ireland_country_conclusion/`
- Manifest: `docs/assets/ireland_p0_family_conclusion_reports/manifest.md`
- Generation prompts and source notes: `docs/assets/ireland_p0_family_conclusion_reports/prompts.md`
- Review contact sheet: `docs/assets/ireland_p0_family_conclusion_reports/contact_sheet.png`
- GFX handoff: `docs/assets/ireland_p0_family_conclusion_reports/gfx_handoff.md`

## Sprite mapping

| Sprite ID | Final DDS |
| --- | --- |
| `GFX_report_event_ireland_postwar_democratic_settlement` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_democratic_settlement.dds` |
| `GFX_report_event_ireland_postwar_congress_settlement` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_congress_settlement.dds` |
| `GFX_report_event_ireland_postwar_blueshirt_settlement` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_blueshirt_settlement.dds` |
| `GFX_report_event_ireland_postwar_producer_estates_settlement` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_producer_estates_settlement.dds` |
| `GFX_report_event_ireland_postwar_restoration_settlement` | `gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_restoration_settlement.dds` |

## Source decisions

- Democratic settlement uses a verified archival source: an approximately 00:40 frame from the 17 February 1948 British Movietone newsreel **“Ireland's New Premier” – John Costello elected Taoiseach**, downloaded from its Wikimedia Commons file page. Commons records the file as Public domain (`PD-UK`, `PD-1996`). The source crop removes the visible AP corner mark before processing.
- Congress settlement, Blueshirt settlement, producer-estates settlement, and restoration settlement are fictional alternate-history scenes generated with the official built-in `imagegen` workflow. They were generated as period documentary source photographs and then received the deterministic report-event card treatment locally.
- No placeholder, map, title card, contact-sheet tile, or substitute asset was used as a final texture.

## Parent-owned next step

Add the five sprite definitions from `docs/assets/ireland_p0_family_conclusion_reports/gfx_handoff.md` to the appropriate existing `.gfx` file, then wire the event picture references in the parent-owned event implementation.
