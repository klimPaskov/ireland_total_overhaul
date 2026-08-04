# Superseded Ireland goal-icon regeneration - 2026-07-26

> Historical evidence only. The current runtime package is the later
> `assets/ireland_focus_tree/icons/regenerated_goal_icons_vanilla_focus_emblems_fresh_2026-07-26_v3/`
> package documented in `docs/plans/ireland_focus_tree/goal_icon_regeneration_vanilla_emblems_tranche_2026-07-26.md`.

Feature slug: `ireland_focus_tree`  
Namespace: `ireland`

## Reason for regeneration

The earlier v3 atlas package and v4 direct-image package were rejected after visual review because they did not consistently match the compact, painterly, irregular Hearts of Iron IV national-focus goal-icon treatment. This tranche regenerates the complete goal-icon set from new image-generation outputs. No earlier Ireland icon, processed image, DDS, vanilla image, flag, portrait, or repository asset was supplied as an image-generation input.

## Package

- 216/216 focus IDs are covered in source-file order.
- Eighteen fresh 4x3 source atlases cover rows 001-216.
- `ireland_material_conclusion_proof` is a separate fresh direct source for row 151, preserving exact one-to-one focus coverage.
- Every row has a retained source PNG, normalized 94x86 RGBA PNG, and final DDS.
- The shared visual direction is compact painterly emblem art with irregular silhouettes, transparent corners, no UI frame, no hard box, no greenscreen matte, and no accidental source-art reuse.

## Evidence and handoff

- Manifest: `assets/ireland_focus_tree/icons/regenerated_goal_icons_fresh_2026-07-26_final/manifest.md`
- Prompt specification: `assets/ireland_focus_tree/icons/regenerated_goal_icons_fresh_2026-07-26_final/prompts/fresh_goal_icon_prompt_spec.md`
- Complete-sheet review: `assets/ireland_focus_tree/icons/regenerated_goal_icons_fresh_2026-07-26_final/contact_sheets/final_goal_icons_contact_sheet.png`
- Runtime DDS folder: `gfx/interface/goals/ireland/`
- Runtime registration: `interface/ireland_icons.gfx`

The staging package remains under `assets/` for source, processing, manifest, and review evidence. Final DDS files are promoted only under the mod's standard `gfx/` tree.

## Historical static QA

The superseded package contains 216 source PNGs, 216 processed PNGs, and 216 DDS files. Its 94x86 processing and runtime evidence is retained for history only; it is not the current runtime art. The live game was not launched; engine rendering and full feature validation remain separate open gates.
