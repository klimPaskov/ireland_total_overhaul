# Ireland mission-icon replacement handoff: 006 and 009

Date: 2026-07-29  
Feature: `ireland_focus_tree`  
Asset type: HOI4 mission icons  
Status: complete; no user review blocker

## Scope

Two independent replacement mission icons were generated for the radical /
underground mission rows:

| Asset | Visual brief | Existing runtime sprite | Related mission |
| --- | --- | --- | --- |
| `mission_ireland_006` | centered dark command hub with three linked underground cell nodes and taut network cords | `GFX_mission_ireland_consolidate_the_movement_network` | `mission_ireland_consolidate_the_movement_network` |
| `mission_ireland_009` | broad constituent charter claimed by a dark leather-gloved hand, central brass civic seal, deep-red ribbon | `GFX_mission_ireland_secure_constituent_authority` | `mission_ireland_secure_constituent_authority` |

The canonical replacement sprite definitions are expected in
`interface/ireland_secondary_assets.gfx`; no `.gfx` file was edited by
this subagent.

## Changed files

- `assets/ireland_focus_tree/icons/source_png/missions/mission_ireland_006.png`
- `assets/ireland_focus_tree/icons/source_png/missions/mission_ireland_009.png`
- `assets/ireland_focus_tree/icons/processed_png/missions/mission_ireland_006.png`
- `assets/ireland_focus_tree/icons/processed_png/missions/mission_ireland_009.png`
- `gfx/interface/decisions/ireland/missions/mission_ireland_006.dds`
- `gfx/interface/decisions/ireland/missions/mission_ireland_009.dds`
- `assets/ireland_focus_tree/icons/contact_sheets/mission_ireland_006_009_replacement_contact_sheet.png`
- `assets/ireland_focus_tree/icons/regenerated_mission_icons_individual_2026-07-29_v1/manifest.md`
- `assets/ireland_focus_tree/icons/regenerated_mission_icons_individual_2026-07-29_v1/gfx_handoff.md`
- `docs/plans/ireland_focus_tree/subagent_handoffs/mission_icon_replacements_006_009_handoff.md`

No `.gfx`, gameplay script, localisation, GUI, focus, decision, event, or
achievement file was changed.

## Generation and processing approach

1. Inspected the canonical mission reference family at
   `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/missions/`,
   including its contact sheet and individual 33x32 references.
2. Generated 006 and 009 separately with the built-in `$imagegen` workflow.
   Each source used a uniform `#ff00ff` removable key, an isolated centered
   painted HOI4-style silhouette, dark contours, warm muted materials, no text,
   no frame, and no sheet layout.
3. Regenerated 009 once with a broader charter-and-hand silhouette because the
   first fresh generation was too narrow at native mission size. The final
   009 source is the broader independent generation, not a crop or salvage of
   the earlier sprite.
4. Removed the chroma key with the installed image-generation helper, fit the
   fresh alpha subject to the canonical 33x32 mission canvas, and retained
   transparent unused pixels.
5. Converted each processed PNG with
   `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py` directly to
   the standard runtime DDS folder. No final DDS was left under `assets/`.

## Validation

- Processed PNGs: exact `33x32`, RGBA, transparent corners, no edge contact.
- Visible alpha bounds: 006 = `(2, 3, 31, 28)`; 009 = `(6, 1, 27, 30)`.
- No green fringe, magenta fringe, or key-colored partially transparent edge
  pixels were found.
- Runtime DDS files exist at the requested paths, are uncompressed 32-bit
  BGRA textures, are exactly `33x32`, and are 4,352 bytes each.
- DDS pixel payloads are identical to the processed PNG pixels after the
  expected BGRA channel packing.
- Contact sheet includes each icon at literal native size and full 8x enlarged
  size over a checkerboard review background. The checkerboard is not in the
  runtime art.

## Runtime handoff

Canonical M2 runtime handoff:

- `GFX_mission_ireland_consolidate_the_movement_network` ->
  `gfx/interface/decisions/ireland/missions/mission_ireland_006.dds`
- `GFX_mission_ireland_secure_constituent_authority` ->
  `gfx/interface/decisions/ireland/missions/mission_ireland_009.dds`

The following two names are retained only as historical pre-M2 handoff text;
the canonical implementation uses the merged/new names above:

- `GFX_mission_ireland_protect_a_by_election` →
  `gfx/interface/decisions/ireland/missions/mission_ireland_006.dds`
- `GFX_mission_ireland_audit_parish_service_contracts` →
  `gfx/interface/decisions/ireland/missions/mission_ireland_009.dds`

The user-requested source paths intentionally omit the older `_source` suffix:

- `assets/ireland_focus_tree/icons/source_png/missions/mission_ireland_006.png`
- `assets/ireland_focus_tree/icons/source_png/missions/mission_ireland_009.png`

## Risks and follow-up

- The package has not been visually rendered inside a live HOI4 session by this
  subagent; the existing sprite names and `.gfx` location should be checked by
  the main wiring agent.
- The older asset crosswalk records `_source`-suffixed source names for these
  ordinals. This handoff follows the newer exact paths requested for this
  replacement and does not edit the crosswalk because gameplay/wiring files
  were outside scope.
- No remaining asset blocker or simplification is known.
