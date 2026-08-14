# Ireland user portrait replacement GFX handoff

This package contains five user-provided full leader portrait textures and three regenerated native advisor cards. The producer did not edit `.gfx` files. The main agent should preserve any existing registrations and use the stable names and paths below.

## Full leader textures

The supplied DDS bytes were copied unchanged to these runtime paths:

| Identity | Runtime DDS | Sprite name |
| --- | --- | --- |
| Maurice Twomey | `gfx/leaders/ireland/leader_maurice_twomey.dds` | Not supplied; preserve the existing registration |
| Éamon de Valera | `gfx/leaders/ireland/leader_eamon_de_valera.dds` | Not supplied; preserve the existing registration |
| Seán Lemass | `gfx/leaders/ireland/leader_sean_lemass.dds` | Not supplied; preserve the existing registration |
| W. T. Cosgrave | `gfx/leaders/ireland/leader_w_t_cosgrave.dds` | Not supplied; preserve the existing registration |
| Douglas Hyde | `gfx/leaders/ireland/leader_douglas_hyde.dds` | Not supplied; preserve the existing registration |

All five are validated `156x210` RGBA DDS files with fully opaque alpha. No external source or rights claim is made.

## Advisor cards

Only these three existing advisor cards were regenerated. Do not create cards for Éamon de Valera or W. T. Cosgrave.

| Sprite name | Runtime DDS | Suggested target definition |
| --- | --- | --- |
| `GFX_ireland_advisor_maurice_twomey` | `gfx/interface/ideas/ireland/advisors/advisor_maurice_twomey.dds` | Existing Ireland advisor `.gfx` definition |
| `GFX_ireland_advisor_sean_lemass` | `gfx/interface/ideas/ireland/advisors/advisor_sean_lemass.dds` | Existing Ireland advisor `.gfx` definition |
| `GFX_ireland_advisor_douglas_hyde` | `gfx/interface/ideas/ireland/advisors/advisor_douglas_hyde.dds` | Existing Ireland advisor `.gfx` definition |

Ready-to-copy texture entries, only if a parent-owned definition is missing:

```text
spriteType = {
	name = GFX_ireland_advisor_maurice_twomey
	texturefile = "gfx/interface/ideas/ireland/advisors/advisor_maurice_twomey.dds"
}

spriteType = {
	name = GFX_ireland_advisor_sean_lemass
	texturefile = "gfx/interface/ideas/ireland/advisors/advisor_sean_lemass.dds"
}

spriteType = {
	name = GFX_ireland_advisor_douglas_hyde
	texturefile = "gfx/interface/ideas/ireland/advisors/advisor_douglas_hyde.dds"
}
```

The cards are native `65x67` output from the current Chaos Redux `create_advisor_icon.py` workflow. Their source, placement studies, 4x reviews, 8x overlays, metadata, hashes, and alpha evidence are recorded in `docs/plans/ireland_focus_tree/assets/advisors/manifest_current_chaos_redux_2026-08-13.json` and the adjacent advisor artifact folders.

Independent visual approval was granted on 2026-08-14. The review covered identity pairing, full-portrait fidelity, advisor crop and dossier geometry, stable sprite consumers, DDS round-trip fidelity, and alpha coverage.
