# Ireland portrait/symbol GFX handoff — 2026-07-19

Historical handoff. The authoritative implemented registrations are in
`interface/ireland_sourced_assets.gfx`; the snippets below preserve the
original proposed sprite stems, while the runtime file owns the exact `GFX_`
names. Every final texture path is under `gfx/`, never `assets/`.

No `.gfx` file was edited. These are proposed sprite names and copy-ready snippets for the parent implementation agent.

Suggested target file: `interface/ireland_sourced_assets.gfx` (or the parent’s existing Ireland asset GFX file).

## Portrait sprites

```text
spriteTypes = {
	spriteType = { name = ireland_portrait_william_norton texturefile = "gfx/leaders/ireland/leader_william_norton.dds" }
	spriteType = { name = ireland_portrait_douglas_hyde texturefile = "gfx/leaders/ireland/leader_douglas_hyde.dds" }
	spriteType = { name = ireland_portrait_sean_t_okelly texturefile = "gfx/leaders/ireland/leader_sean_t_okelly.dds" }
	spriteType = { name = ireland_portrait_sean_mac_eoin texturefile = "gfx/leaders/ireland/leader_sean_mac_eoin.dds" }
	spriteType = { name = ireland_portrait_frank_aiken texturefile = "gfx/leaders/ireland/leader_frank_aiken.dds" }
	spriteType = { name = ireland_portrait_sean_macentee texturefile = "gfx/leaders/ireland/leader_sean_macentee.dds" }
	spriteType = { name = ireland_portrait_oscar_traynor texturefile = "gfx/leaders/ireland/leader_oscar_traynor.dds" }
	spriteType = { name = ireland_portrait_james_larkin texturefile = "gfx/leaders/ireland/leader_james_larkin.dds" }
	spriteType = { name = ireland_portrait_william_davin texturefile = "gfx/leaders/ireland/leader_william_davin.dds" }
	spriteType = { name = ireland_portrait_john_charles_mcquaid texturefile = "gfx/leaders/ireland/leader_john_charles_mcquaid.dds" }
	spriteType = { name = ireland_portrait_frank_duff texturefile = "gfx/leaders/ireland/leader_frank_duff.dds" }
	spriteType = { name = ireland_portrait_sean_macbride texturefile = "gfx/leaders/ireland/leader_sean_macbride.dds" }
	spriteType = { name = ireland_portrait_george_gilmore texturefile = "gfx/leaders/ireland/leader_george_gilmore.dds" }
	spriteType = { name = ireland_portrait_nora_connolly_obrien texturefile = "gfx/leaders/ireland/leader_nora_connolly_obrien.dds" }
	spriteType = { name = ireland_portrait_eoin_oduffy texturefile = "gfx/leaders/ireland/leader_eoin_oduffy.dds" }
	spriteType = { name = ireland_portrait_ernest_blythe texturefile = "gfx/leaders/ireland/leader_ernest_blythe.dds" }
}
```

## Symbol sprites

```text
spriteTypes = {
	spriteType = { name = ireland_symbol_oglaigh_na_heireann texturefile = "gfx/interface/ireland/sourced/symbol_oglaigh_na_heireann.dds" }
	spriteType = { name = ireland_symbol_starry_plough_1914 texturefile = "gfx/interface/ireland/sourced/symbol_starry_plough_1914.dds" }
	spriteType = { name = ireland_symbol_legion_of_mary_vexillum texturefile = "gfx/interface/ireland/sourced/symbol_legion_of_mary_vexillum.dds" }
	spriteType = { name = ireland_symbol_irish_air_corps_roundel_1939_1954 texturefile = "gfx/interface/ireland/sourced/symbol_irish_air_corps_roundel_1939_1954.dds" }
	spriteType = { name = ireland_symbol_belfast_coat_of_arms texturefile = "gfx/interface/ireland/sourced/symbol_belfast_coat_of_arms.dds" }
}
```

All new sprites are conditional review exports. The source/rights conditions and unresolved IDs are recorded in `portrait_symbol_source_handoff_2026-07-19.md`; do not wire them as unrestricted assets without parent review.
