# Ireland public-family focus icon GFX handoff

Scope: 27 static national-focus icons. This asset worker produced source PNGs, processed PNGs, final DDS, manifest, prompt log, and contact sheet only. No `.gfx`, focus, gameplay, localisation, GUI, or existing documentation files were edited.

Suggested target: the existing Ireland focus sprite surface (for example `interface/ireland_icons.gfx`). Add one sprite per row using the stable names and texture paths below:

```text
spriteType = { name = GFX_focus_ireland_republican_ministries texturefile = "gfx/interface/goals/ireland_republican_ministries.dds" }
spriteType = { name = GFX_focus_ireland_rights_under_emergency texturefile = "gfx/interface/goals/ireland_rights_under_emergency.dds" }
spriteType = { name = GFX_focus_ireland_local_government_compact texturefile = "gfx/interface/goals/ireland_local_government_compact.dds" }
spriteType = { name = GFX_focus_ireland_democratic_security_league texturefile = "gfx/interface/goals/ireland_democratic_security_league.dds" }
spriteType = { name = GFX_focus_ireland_democratic_reconstruction texturefile = "gfx/interface/goals/ireland_democratic_reconstruction.dds" }
spriteType = { name = GFX_focus_ireland_vanguard_organisers texturefile = "gfx/interface/goals/ireland_vanguard_organisers.dds" }
spriteType = { name = GFX_focus_ireland_trade_union_congress texturefile = "gfx/interface/goals/ireland_trade_union_congress.dds" }
spriteType = { name = GFX_focus_ireland_workers_smallholders_programme texturefile = "gfx/interface/goals/ireland_workers_smallholders_programme.dds" }
spriteType = { name = GFX_focus_ireland_republican_self_defence texturefile = "gfx/interface/goals/ireland_republican_self_defence.dds" }
spriteType = { name = GFX_focus_ireland_workers_reconstruction_board texturefile = "gfx/interface/goals/ireland_workers_reconstruction_board.dds" }
spriteType = { name = GFX_focus_ireland_veterans_command_council texturefile = "gfx/interface/goals/ireland_veterans_command_council.dds" }
spriteType = { name = GFX_focus_ireland_veteran_employment_corps texturefile = "gfx/interface/goals/ireland_veteran_employment_corps.dds" }
spriteType = { name = GFX_focus_ireland_national_corporate_chamber texturefile = "gfx/interface/goals/ireland_national_corporate_chamber.dds" }
spriteType = { name = GFX_focus_ireland_motorised_command_contracts texturefile = "gfx/interface/goals/ireland_motorised_command_contracts.dds" }
spriteType = { name = GFX_focus_ireland_personal_command_or_corporate_state texturefile = "gfx/interface/goals/ireland_personal_command_or_corporate_state.dds" }
spriteType = { name = GFX_focus_ireland_emergency_directorate texturefile = "gfx/interface/goals/ireland_emergency_directorate.dds" }
spriteType = { name = GFX_focus_ireland_creditor_cabinet texturefile = "gfx/interface/goals/ireland_creditor_cabinet.dds" }
spriteType = { name = GFX_focus_ireland_restricted_estate_franchise texturefile = "gfx/interface/goals/ireland_restricted_estate_franchise.dds" }
spriteType = { name = GFX_focus_ireland_industrial_syndicates texturefile = "gfx/interface/goals/ireland_industrial_syndicates.dds" }
spriteType = { name = GFX_focus_ireland_rural_producer_boards texturefile = "gfx/interface/goals/ireland_rural_producer_boards.dds" }
spriteType = { name = GFX_focus_ireland_executive_estates texturefile = "gfx/interface/goals/ireland_executive_estates.dds" }
spriteType = { name = GFX_focus_ireland_producer_directorate texturefile = "gfx/interface/goals/ireland_producer_directorate.dds" }
spriteType = { name = GFX_focus_ireland_managed_social_peace texturefile = "gfx/interface/goals/ireland_managed_social_peace.dds" }
spriteType = { name = GFX_focus_ireland_claimants_convention texturefile = "gfx/interface/goals/ireland_claimants_convention.dds" }
spriteType = { name = GFX_focus_ireland_provincial_compact texturefile = "gfx/interface/goals/ireland_provincial_compact.dds" }
spriteType = { name = GFX_focus_ireland_brehon_law_commission texturefile = "gfx/interface/goals/ireland_brehon_law_commission.dds" }
spriteType = { name = GFX_focus_ireland_crown_defence_council texturefile = "gfx/interface/goals/ireland_crown_defence_council.dds" }
```

All textures are 94x86 RGBA/BGRA DDS with transparent corners. Apply the existing shared focus shine layer `gfx/interface/goals/shine_overlay.dds` through the normal focus-button shine mechanism; no per-icon shine texture is supplied.

Runtime texture folder: `gfx/interface/goals/`.
