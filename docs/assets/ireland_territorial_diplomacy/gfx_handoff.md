# Territorial diplomacy report-event GFX handoff

Scope: source/processed PNG, final 210x176 DDS, manifest, prompts, and contact sheet only. No `.gfx`, event, gameplay, localisation, or GUI files were edited by the asset worker.

Suggested target: existing `interface/ireland_event_art.gfx` (or the project's established event-art sprite surface). Add these stable sprite definitions:

```text
spriteType = { name = "GFX_report_event_ireland_territorial_ulster_ultimatum" texturefile = "gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_ulster_ultimatum.dds" }
spriteType = { name = "GFX_report_event_ireland_territorial_belfast_compact" texturefile = "gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_belfast_compact.dds" }
spriteType = { name = "GFX_report_event_ireland_territorial_highlands_claim" texturefile = "gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_highlands_claim.dds" }
spriteType = { name = "GFX_report_event_ireland_territorial_highlands_negotiation" texturefile = "gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_highlands_negotiation.dds" }
spriteType = { name = "GFX_report_event_ireland_territorial_ulster_enforcement" texturefile = "gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_ulster_enforcement.dds" }
```

Suggested event picture routing (main agent owns the event edit):

- `.1`–`.4`: `GFX_report_event_ireland_territorial_ulster_ultimatum`.
- `.5`–`.8`: `GFX_report_event_ireland_territorial_belfast_compact`.
- `.9`–`.10`: `GFX_report_event_ireland_territorial_highlands_claim`.
- `.11`–`.12`: `GFX_report_event_ireland_territorial_highlands_negotiation`.
- `.13`–`.16`: `GFX_report_event_ireland_territorial_ulster_enforcement`.

Additional Wales/Cornwall demand sprites:

```text
spriteType = { name = "GFX_report_event_ireland_territorial_wales_demand" texturefile = "gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_wales_demand.dds" }
spriteType = { name = "GFX_report_event_ireland_territorial_cornwall_demand" texturefile = "gfx/event_pictures/ireland_territorial_diplomacy/report_event_ireland_cornwall_demand.dds" }
```

Suggested event picture routing for the new demand chains:

- `.17`–`.20`: `GFX_report_event_ireland_territorial_wales_demand` (wet Welsh slate-and-coal harbour memorandum exchange).
- `.21`–`.24`: `GFX_report_event_ireland_territorial_cornwall_demand` (granite Atlantic headland, lookout, and small harbour delegation).

Both assets are generated final-source art, not placeholders. The processed PNGs and DDS files are 210x176 report-card assets with the existing package's black-and-white/sepia, transparent-corner, tilt, and soft-shadow treatment. Suggested target remains `interface/ireland_event_art.gfx`; no `.gfx` file was edited by the asset worker.

The existing `GFX_report_event_ireland_report_flavour_northern_bridge` is not a replacement for this package; it may remain for unrelated flavour events. The Highlands events currently have no `picture` field and should receive the proposed Highlands sprite assignments when wired.
