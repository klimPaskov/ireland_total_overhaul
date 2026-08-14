# Ireland territorial diplomacy report-event art manifest

Feature slug: `ireland_territorial_diplomacy`  
Asset type: generated HOI4 report-event imagery  
Source mode: `$imagegen` built-in generation; generation is appropriate because the chain is fictional/alternate-history and needs specific diplomatic scenes rather than a real historical photograph.  
Reference inspected: canonical `event_art/report/` reference family and its contact sheet under the shared vanilla reference library.  
Processing: `.agents/skills/hoi4-feature-assets/tools/process_report_event_image.py` followed by `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py`.  
Report-card target: 210x176 RGBA PNG/DDS, black-and-white source with sepia applied by the report-card processor, transparent corners, subtle tilt and soft shadow.

| Asset | Narrative surface / event IDs | Source PNG | Processed PNG | Runtime DDS | Registered sprite | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Ulster ultimatum | `ireland_territorial_diplomacy.1`–`.4` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_ulster_ultimatum.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_ulster_ultimatum.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_ulster_ultimatum.dds` | `GFX_report_event_ireland_territorial_ulster_ultimatum` | complete / wired |
| Belfast commercial compact | `.5`–`.8` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_belfast_compact.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_belfast_compact.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_belfast_compact.dds` | `GFX_report_event_ireland_territorial_belfast_compact` | complete / wired |
| Scottish Highlands claim | `.9`–`.10` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_highlands_claim.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_highlands_claim.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_highlands_claim.dds` | `GFX_report_event_ireland_territorial_highlands_claim` | complete / wired |
| Scottish Highlands negotiation | `.11`–`.12` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_highlands_negotiation.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_highlands_negotiation.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_highlands_negotiation.dds` | `GFX_report_event_ireland_territorial_highlands_negotiation` | complete / wired |
| Ulster enforcement/refusal | `.13`–`.16` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_ulster_enforcement.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_ulster_enforcement.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_ulster_enforcement.dds` | `GFX_report_event_ireland_territorial_ulster_enforcement` | complete / wired |
| Wales demand | `.17`–`.20` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_wales_demand.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_wales_demand.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_wales_demand.dds` | `GFX_report_event_ireland_territorial_wales_demand` | complete / wired |
| Cornwall demand | `.21`–`.24` | `docs/assets/ireland_territorial_diplomacy/source_png/report_event_ireland_cornwall_demand.png` | `docs/assets/ireland_territorial_diplomacy/processed_png/report_event_ireland_cornwall_demand.png` | `gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_cornwall_demand.dds` | `GFX_report_event_ireland_territorial_cornwall_demand` | complete / wired |

Runtime wiring status: the seven sprites above are registered in
`interface/ireland_event_art.gfx`. They cover the picture-bearing diplomatic
chain events `.1`–`.24`; Provincial Assent record/confirmation events `.25`–`.27`
are event-led records without a picture field. The separate family-lane focus
layout is accepted at `89ff719`; this manifest does not replace the parent
completion audit.

All source and processed images are generated for this feature and do not depict recognizable real people. No asset is a placeholder or reused generic image. The contact sheet for review is `docs/assets/ireland_territorial_diplomacy/contact_sheet.png` (duplicate review copy: `contact_sheets/territorial_diplomacy_report_event_contact_sheet.png`). The Wales and Cornwall sources were generated on 2026-08-14 with the built-in `$imagegen` workflow, then processed through the repository report-card processor and converted with the repository DDS converter. Wales uses a slate-and-coal harbour memorandum exchange; Cornwall uses a granite Atlantic headland and lookout delegation so the two demand chains have distinct visual identities.
