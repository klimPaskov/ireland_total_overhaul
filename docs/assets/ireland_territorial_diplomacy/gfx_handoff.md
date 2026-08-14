# Territorial diplomacy report-event GFX handoff

Status: wired by the parent implementation. All seven sprite definitions below
are registered in `interface/ireland_event_art.gfx`, and the territorial event
chain consumes the seven report surfaces across events `.1`–`.27`. This handoff
is retained as the asset registration and routing record.

Scope: source/processed PNG, final 210x176 DDS, manifest, prompts, and contact sheet only. No `.gfx`, event, gameplay, localisation, or GUI files were edited by the asset worker.

Registered target: existing `interface/ireland_event_art.gfx`. The stable sprite
definitions are:

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

Both assets are generated final-source art, not placeholders. The processed PNGs
and DDS files are 210x176 report-card assets with the existing package's
black-and-white/sepia, transparent-corner, tilt, and soft-shadow treatment. The
parent adopted the target and wired all seven sprites; no further `.gfx` insertion
is pending for this asset package.

The existing `GFX_report_event_ireland_report_flavour_northern_bridge` is not a
replacement for this package; it may remain for unrelated flavour events. The
Highlands and demand events now have their dedicated picture assignments in the
territorial chain. Layout status is separate; the final family-lane reflow is
accepted at `89ff719` in the country-package completion handoff. Parent
completion audit/live evidence remains separate.
