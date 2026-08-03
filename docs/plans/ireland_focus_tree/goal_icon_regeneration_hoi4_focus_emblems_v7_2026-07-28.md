# Ireland goal-icon regeneration tranche - v7

Date: 2026-07-28
Feature slug: `ireland_focus_tree`
Namespace: `slopx`

## Outcome

The previous goal-icon package was rejected for looking too ornamental and
insufficiently like vanilla HOI4 focus emblems. A fresh v7 set was generated
from new prompts. The 216 focus identifiers and stable `.gfx` registrations
were preserved, but the image sources were regenerated rather than
reprocessed from v5 or any earlier package.

## Production record

- Fourteen new 4x4 source atlases were generated with the built-in image
  generation workflow.
- One additional source was generated for `presidential_settlement` after its
  atlas cell failed visual review.
- The shared prompt required one route-specific centered painted object or
  scene per cell, dark contour, matte shading, restrained palette, and small
  focus-tree readability.
- The prompt prohibited universal wreaths or medallions, boxes, plaques,
  text, portraits, glossy rendering, fake checkerboards, and green painted
  subjects.
- A flat green matte was used only as source separation. The installed
  chroma-key cleanup produced real alpha; each visible alpha bound was then
  optically centered on a 100x88 canvas.
- All 216 processed PNGs were converted to DDS and promoted to the standard
  runtime `gfx/interface/goals/slopx_ireland/` folder.

## Evidence

The complete source package is
`assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v7/`.

- `manifest_v7.json` is the per-item source/alpha/processed/DDS manifest with
  dimensions, hashes, atlas cell, prompt reference, and runtime path.
- `prompts_v7.md` records the shared brief, all atlas subject order, and the
  individual presidential replacement prompt.
- `visual_review_v7.md` records the style review against the rejected package.
- `audit_v7.md` records the strict 216-row, alpha, alignment, duplicate,
  DDS-readback, and v5-overlap results.
- `gfx_handoff_v7.md` records the final runtime path and registration contract.
- `contact_sheets/goal_icons_complete_contact_sheet_v7.png` is the visual
  review sheet; its checkerboard is review-only.

The audit result is 216 source rows, 216 processed rows, and 216 DDS files;
zero missing/unexpected rows, duplicate hashes, green residue, opaque corners,
empty icons, off-center icons, edge contact, readback failures, and v5 hash
overlap. After promotion, all 216 runtime DDS SHA-256 hashes match v7 staging.

## Boundary and remaining proof

`assets/` remains temporary staging/evidence. The final DDS files are under the
mod's standard `gfx` tree. No HOI4 process was launched. Offline registration
and raster checks do not replace live engine loading, focus hover, or scenario
validation, which remain open in the overall Ireland overhaul.
