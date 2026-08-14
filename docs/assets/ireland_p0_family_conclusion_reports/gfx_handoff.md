# GFX handoff — Ireland P0 family conclusion report art

The main agent should add the following five `spriteType` definitions to the appropriate existing event-picture `.gfx` file. If no suitable shared file exists, `interface/ireland_country_conclusion.gfx` is the suggested feature-owned target. Do not change the sprite IDs.

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

All five DDS files are final `210x176` report-event card textures with transparent corners and soft shadows. The democratic asset is the sourced archival frame documented in `manifest.md`; the other four are generated alternate-history documentary scenes. The event implementation should reference the exact sprite IDs above.
