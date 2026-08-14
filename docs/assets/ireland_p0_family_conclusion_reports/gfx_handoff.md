# GFX handoff — Ireland P0 family conclusion report art

Status: wired by the parent implementation. The five sprite definitions below
are registered in `interface/ireland_event_art.gfx` and consumed by
`events/ireland_country_conclusion_events.txt` events `.1`–`.5`. This handoff is
retained as the asset registration and provenance record; no further `.gfx`
insertion is pending for this package.

```text
spriteTypes = {
	 spriteType = {
		 name = GFX_report_event_ireland_postwar_democratic_settlement
		 texturefile = "gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_democratic_settlement.dds"
	 }
	 spriteType = {
		 name = GFX_report_event_ireland_postwar_congress_settlement
		 texturefile = "gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_congress_settlement.dds"
	 }
	 spriteType = {
		 name = GFX_report_event_ireland_postwar_blueshirt_settlement
		 texturefile = "gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_blueshirt_settlement.dds"
	 }
	 spriteType = {
		 name = GFX_report_event_ireland_postwar_producer_estates_settlement
		 texturefile = "gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_producer_estates_settlement.dds"
	 }
	 spriteType = {
		 name = GFX_report_event_ireland_postwar_restoration_settlement
		 texturefile = "gfx/event_pictures/ireland_country_conclusion/report_event_ireland_postwar_restoration_settlement.dds"
	 }
}
```

All five DDS files are final `210x176` report-event card textures with
transparent corners and soft shadows. The democratic asset is the sourced
archival frame documented in `manifest.md`; the other four are generated
alternate-history documentary scenes. The family conclusion event consumers
reference the exact sprite IDs above. Layout status is separate; the final
family-lane reflow is accepted at `89ff719` in the country-package completion
handoff. Parent completion audit/live evidence remains separate.
