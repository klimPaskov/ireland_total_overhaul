# Ireland goal icons — superseded vanilla-style regeneration — 2026-07-26

> Superseded on 2026-07-27 by
> `docs/plans/ireland_focus_tree/goal_icon_vanilla_style_regeneration_2026-07-27_v4.md`.
> The current runtime package is
> `assets/ireland_focus_tree/icons/regenerated_goal_icons_vanilla_focus_emblems_fresh_2026-07-27_v4/`.

## Current package

The earlier Ireland goal-icon package was rejected because its icons shared a
medallion treatment that did not match the vanilla HOI4 national-focus emblem
language. The current package was generated again from new built-in
image-generation source atlases; it was not produced by reprocessing the old
source or processed images.

Current staging and provenance package:

```text
assets/ireland_focus_tree/icons/regenerated_goal_icons_vanilla_focus_emblems_fresh_2026-07-26_v3/
```

The package contains fourteen fresh 4x4 source atlases, 216 source cells, 216
alpha-clean PNGs, 216 processed 100x88 PNGs, 216 staged DDS files, a prompt
record, a machine-readable manifest, a complete contact sheet, and the static
audit. The final game-facing DDS files are in:

```text
gfx/interface/goals/slopx_ireland/
```

`interface/slopx_ireland_icons.gfx` keeps the existing stable sprite names and
references all 216 runtime DDS files. `assets/` is staging and provenance only;
the runtime art is not loaded from there.

## Style contract

The source prompt required the vanilla HOI4 focus-emblem language: compact,
aged matte painted symbols with readable silhouettes, restrained bronze/steel/
cream/deep-green tones, and dark painted outlines. Subjects use varied open
compositions—wreaths, ribbons, banners, flags, books, tools, buildings,
equipment, and heraldic or institutional symbols—chosen for the focus rather
than a shared circular mount. The source atlases use flat `#00ff00` only as a
temporary chroma-key field; the runtime files have transparent corners and no
visible key-green.

## Evidence

- `manifest.json` records the 216 per-focus source, processed, and runtime
  paths plus final DDS hashes.
- `audit.json` records 216 processed icons with no visible key-green, opaque
  corners, empty cells, off-center bounds, edge contact, or duplicate processed
  hashes.
- `contact_sheets/goal_icons_complete_contact_sheet.png` is the complete visual
  review of the regenerated set.
- Runtime parity is exact: 216 staged DDS files match 216 files under
  `gfx/interface/goals/slopx_ireland/`, with 100x88 DDS headers and 216 `.gfx`
  texture references.
- The new source and processed hashes have zero overlap with the superseded
  package, confirming that the current set was regenerated rather than
  reprocessed.

## Validation boundary

Static source, image, DDS, filename, and runtime-parity checks are complete.
HOI4 was not launched, as requested; engine rendering, focus-hover readability,
and full feature scenario validation remain open in the larger Ireland audit.
