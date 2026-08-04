# Ireland Cleared Portrait Consumer Repair — 2026-08-01

## Scope

This tranche closes the five cleared portrait rows that had final DDS files and
registered sprites but no non-interface source consumer. It does not change the
source-clearance state, create new portraits, or move source material out of
`docs/portraits/`.

The runtime textures remain in the standard mod tree:

```text
gfx/leaders/ireland/leader_eamon_de_valera.dds
gfx/leaders/ireland/leader_james_larkin.dds
gfx/leaders/ireland/leader_eoin_oduffy.dds
gfx/leaders/ireland/leader_p_37.dds
gfx/leaders/ireland/leader_j_j_walsh.dds
```

## Consumer map

| manifest row | source sprite | consumer | gate and cleanup |
|---|---|---|---|
| P-01 — Éamon de Valera | `GFX_ireland_leader_eamon_de_valera` | `common/scripted_effects/ireland_effects.txt` assigns the sprite to vanilla `IRE_Éamon_de_valera` during one-time campaign initialization | Existing route leader promotion and retirement rules remain authoritative. |
| P-21 — James Larkin | `GFX_ireland_portrait_james_larkin` | Campaign initialization assigns the sprite to vanilla `IRE_james_larkin` | Existing route commitment retirement removes the character when the route lifecycle requires it. |
| P-52 — Eoin O’Duffy | `GFX_ireland_portrait_eoin_oduffy` | Campaign initialization assigns the sprite to vanilla `IRE_eoin_oduffy` | Existing O’Duffy route promotion and post-route retirement remain authoritative. |
| P-37 — Seán Russell | `GFX_ireland_portrait_p_37` | `ireland_sean_russell_advisor` in `common/characters/ireland_route_characters.txt` | Recruited only for the IRA command route after 1938-04-01 and before 1940-08-15, with `ireland_ira_command_ready`; lifecycle cleanup retires or deactivates it on route closure, command collapse, or after the date boundary. |
| P-59 — J. J. Walsh | `GFX_ireland_portrait_p_59` | `ireland_j_j_walsh_patron` in `common/characters/ireland_route_characters.txt` | Recruited for the Ailtirí route after 1942-06-01; lifecycle cleanup deactivates and retires it when that route closes or is no longer active. |

## Static evidence

- The five sprite names are registered in `interface/ireland_sourced_assets.gfx`.
- All five final DDS files exist below `gfx/leaders/ireland/`.
- The two recovered originals remain under `docs/portraits/research_2026-07-29/blocked_queue/`.
- The non-interface consumer scan finds one or more source references for each
  sprite in `common/` or `history/`.
- The touched Clausewitz files have balanced braces after the repair.
- Live HOI4 loading is intentionally outside this completion gate by user
  direction; this record is a source and static-wiring audit, not an in-game
  claim.

## Remaining source-status boundary

These five rows were already cleared by their manifest records. This repair
does not promote blocked or review-gated portraits. P-60 Oliver J. Flanagan is
outside this repair because its separate dated Ailtirí advisor consumer and
runtime registration already exist; its C3 attribution conditions remain in
the manifest.
