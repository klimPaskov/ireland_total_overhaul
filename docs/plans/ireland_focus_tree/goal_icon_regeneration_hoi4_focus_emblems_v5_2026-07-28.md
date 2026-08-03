# Ireland goal-icon regeneration — fresh HOI4 focus-emblem v5

Feature: `ireland_focus_tree`  
Date: 2026-07-28  
Runtime root: `gfx/interface/goals/slopx_ireland/`  
Source package: `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v5/`

## User correction applied

The prior v4 package was not reused, recoloured, or reprocessed. Fourteen new 4×4 source atlases were generated with the built-in image-generation workflow. The new prompt was tightened around the native HOI4 national-focus emblem language: substantial centered painted symbols, dark ink contours, aged matte shading, compact heraldic framing, and varied wreath/ribbon/pennant accents. It explicitly excludes cards, plaques, tiles, square frames, universal medallions, text, green painted subjects, fake checkerboards, glossy CGI, and photorealistic rendering.

The v4 and earlier packages remain staging/review history only. Their artwork is not an input to v5. Cell extraction, chroma-key removal, centering, resizing, and DDS conversion are build processing of the new v5 source art; they do not create the artwork.

## Package and runtime evidence

- 14 new source atlases.
- 216 source PNG rows, one per focus.
- 216 real alpha PNG rows with chroma spill removed.
- 216 processed PNG rows at 100×88.
- 216 runtime DDS rows at 100×88 under the standard `gfx/` tree.
- 216 stable focus sprite registrations remain in `interface/slopx_ireland_icons.gfx`.
- 216 paired focus-shine definitions remain in `interface/slopx_ireland_focus_shine.gfx`.
- `manifest.json` records each focus id, atlas/cell, source/alpha/processed paths, runtime DDS path, sprite name, and hashes.
- `manifest.md`, `gfx_handoff.md`, and `prompts/atlas_prompts.md` retain the per-package handoff and generation brief.
- `contact_sheets/goal_icons_complete_contact_sheet.png` is the review sheet for alignment and visual-family inspection.

The v5 audit reports:

```text
expected                         216
processed                        216
missing                           0
bad_dimensions                    0
green_visible                     0
opaque_corners                    0
empty                             0
off_center                        0
edge_contact                      0
unique_processed_sha256         216
runtime_dds_count               216
runtime_dds_unique_hashes        216
source/processed/runtime overlap with v4  0
```

The offline runtime readback opened a final DDS as 100×88 RGBA and visually confirmed the transparent emblem treatment. No HOI4 process was launched.

## Boundary

This tranche only replaces the 216 Ireland focus-goal visuals and preserves their existing ids and `.gfx` wiring. It does not claim the whole Ireland feature is complete: source clearance, live engine/reference checks, scenario validation, AI playthroughs, and the other asset families remain separate gates recorded in the source-of-truth map.

