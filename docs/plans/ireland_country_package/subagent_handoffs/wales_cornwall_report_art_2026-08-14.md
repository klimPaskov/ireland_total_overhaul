# Wales and Cornwall report-event art handoff

Status: complete / handed off  
Feature slug: `ireland_territorial_diplomacy`  
Asset type: generated HOI4 report-event imagery  
Source mode: built-in `$imagegen` generation  
Target: 210x176 RGBA PNG/DDS report cards  
Date: 2026-08-14

## Completed assets

| Asset | Event IDs | Source PNG | Processed PNG | Runtime DDS | Sprite name |
| --- | --- | --- | --- | --- | --- |
| Wales demand | `ireland_territorial_diplomacy.17`–`.20` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_wales_demand.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_wales_demand.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_wales_demand.dds` | `GFX_report_event_ireland_territorial_wales_demand` |
| Cornwall demand | `ireland_territorial_diplomacy.21`–`.24` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_cornwall_demand.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_cornwall_demand.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_cornwall_demand.dds` | `GFX_report_event_ireland_territorial_cornwall_demand` |

Wales is a wet slate-and-coal harbour memorandum exchange. Cornwall is an exposed granite Atlantic headland with a lookout and small fishing harbour delegation. They are intentionally distinct from one another and from the existing Belfast, Highlands, and Ulster package images. Neither source depicts a recognizable real person. No readable text, flags, logos, UI, modern props, or placeholder art is present.

## Documentation updated

- `docs/assets/ireland_territorial_diplomacy/manifest.md`
- `docs/assets/ireland_territorial_diplomacy/prompts.md`
- `docs/assets/ireland_territorial_diplomacy/gfx_handoff.md`
- `docs/assets/ireland_territorial_diplomacy/contact_sheet.png`
- `docs/assets/ireland_territorial_diplomacy/contact_sheets/territorial_diplomacy_report_event_contact_sheet.png`

The contact sheet contains all seven territorial-diplomacy report images. The prompt record documents the generated scenes and constraints.

## Processing and validation

- Inspected the existing package contact sheet and the canonical `event_art/report/` reference contact sheet before generation.
- Generated both sources with the official built-in imagegen workflow.
- Processed with `.agents/skills/hoi4-feature-assets/tools/process_report_event_image.py` using separate deterministic seeds (`1738` Wales, `1739` Cornwall).
- Converted with `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py --width 210 --height 176`.
- Verified source dimensions (1537x1023 Wales; 1536x1024 Cornwall), processed PNG dimensions/mode (210x176 RGBA), and DDS dimensions/format (210x176, 32-bit uncompressed BGRA masks).

## Main-agent wiring

Add the two sprite definitions to the established event-art `.gfx` surface, proposed in `docs/assets/ireland_territorial_diplomacy/gfx_handoff.md`, and route `.17`–`.20` to the Wales sprite and `.21`–`.24` to the Cornwall sprite. This subagent did not edit `.gfx`, gameplay, events, localisation, GUI, focus, decisions, or `thumbnail.png`.

No known asset blockers or simplifications remain. No commit was created; the parent agent owns final wiring and commit.
