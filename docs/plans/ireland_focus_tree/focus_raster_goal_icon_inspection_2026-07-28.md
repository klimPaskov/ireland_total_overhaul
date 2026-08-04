# Ireland focus raster and goal-icon inspection — 2026-07-28

## Scope

This is an offline MCP raster review of the authored `ireland_focus_tree`
after the fresh v7 focus-goal regeneration. It does not launch Hearts of Iron
IV and does not claim live engine behaviour.

## Result

- Source: `common/national_focus/ireland_focus_tree.txt`
- Tree id: `ireland_focus_tree`
- Raster mode: national focus tree
- Review scale: `0.25`
- Raster spacing: horizontal `80`, vertical `80`, padding `20`
- Raster dimensions: `9046x1009`
- Result: `FOCUS_RASTERIZED`
- Ireland focus goal references loaded: `216`
- Runtime texture root observed: `gfx/interface/goals/ireland/`
- Runtime `assets/` texture references observed: `0`

The raster source scan resolved the Ireland focus references against the fresh
runtime DDS package. The package remains the fourteen newly generated atlases,
the separate presidential replacement, and 216 distinct focus-emblem DDS
outputs documented in
`goal_icon_regeneration_hoi4_focus_emblems_v7_2026-07-28.md`.

## Diagnostics boundary

The raster response reports fourteen blocking icon-reference diagnostics for
unrelated vanilla continuous-focus entries in the game snapshot, plus one
unrelated vanilla localisation warning. No Ireland-local missing goal-icon,
texture-path, or icon-registration diagnostic was returned. Those global game
diagnostics are retained as an engine-tool boundary and are not silently
attributed to the Ireland tree.

## Visual contract

The v7 source package remains the visual authority: each goal uses the same
100x88 transparent HOI4 national-focus canvas, centered painted emblem scale,
dark contour, matte bronze/cream/steel/deep-green/navy/oxblood palette, and a
route-specific object or compact scene. The package contains no universal
wreaths or medallions, painted cards, plaques, fake checkerboards, green matte,
portraits, or text.
