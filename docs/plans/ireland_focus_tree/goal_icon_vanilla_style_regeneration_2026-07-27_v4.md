# Ireland focus-goal icons — fresh vanilla-style regeneration — 2026-07-27 v4

Feature slug: `ireland_focus_tree`
Namespace: `slopx`

## Current package

The v3 package was rejected after review because it read as a generated
miniature-object/medallion set rather than a consistent HOI4 national-focus
emblem family. The current v4 package is a complete fresh regeneration from
fourteen new built-in image-generation source atlases. It does not reuse v3
source, processed, or DDS imagery.

Source and review evidence:

```text
assets/ireland_focus_tree/icons/regenerated_goal_icons_vanilla_focus_emblems_fresh_2026-07-27_v4/
```

Runtime final DDS:

```text
gfx/interface/goals/slopx_ireland/
```

The runtime sprite names and registration file remain stable:
`interface/slopx_ireland_icons.gfx` → `GFX_focus_slopx_ireland_*`.

## Visual contract

- One compact painted 2D focus emblem per goal, with a strong central
  silhouette and readable 1930s strategy-game detail.
- Shared target canvas: 100×88, with transparent corners and consistent
  centered breathing room.
- Flat hand-painted planes, aged matte brush texture, dark painted contours,
  restrained bronze/cream/steel/deep-green/oxblood palette, and varied open
  compositions.
- Wreaths, ribbons, flags, books, buildings, tools, equipment, people, and
  institutional symbols are used only when they serve the focus subject; no
  universal ring, plaque, box, card, tile, or medallion template.
- No generated text, UI frames, full-field backgrounds, visible green-screen,
  opaque corners, mixed canvas alignment, or icon-family outliers.

## Evidence

- `manifest.json`: 216 focus rows, atlas/cell provenance, source and processed
  hashes, final runtime DDS paths/hashes, and stable sprite names.
- `audit.json`: 216/216 processed rows, 216 unique processed hashes, zero
  visible key-green, opaque corners, empty rows, off-center rows, or edge
  contact; 216 runtime DDS files with valid 100×88 readback; zero source or
  processed hash overlap with v3.
- `contact_sheets/goal_icons_complete_contact_sheet.png`: complete 216-row
  visual review at the actual runtime footprint.
- `prompts/atlas_prompts.md`: shared generation contract and complete atlas
  subject order.

The `assets/` package is temporary source, alpha, processed, manifest, prompt,
and review evidence. Final game-facing DDS files are under the mod’s standard
`gfx/` tree only.

## Validation boundary

Static source, alpha, processed-PNG, DDS, filename, GFX-reference, and runtime
path checks are complete. HOI4 was not launched, so engine rendering,
focus-hover readability, and the larger Ireland runtime scenario programme
remain open in the parent completion audit.
