# Historical rejected Ireland goal-icon regeneration tranche — 2026-07-26

> This document describes the rejected medallion package only. It is retained
> for audit history. The current source of truth is
> `goal_icon_regeneration_vanilla_emblems_tranche_2026-07-26.md` and the
> `regenerated_goal_icons_hoi4_vanilla_emblems_fresh_2026-07-26` package.

## Outcome

The earlier 216-icon package was rejected: it used loose object collages rather
than the compact medallion language of vanilla HOI4 focus icons. All 216 goal
icons were therefore regenerated from new `$imagegen` source art. The current
package uses one consistent family treatment: a front-facing circular or shield
medallion, dark charcoal/navy painted center, aged-gold rim, restrained laurel,
and one readable historical symbol. The processed results have transparent
corners only; no white backing, UI box, checkerboard, greenscreen pixels, or
source-art reuse remains in the current runtime set.

The final DDS files are in the standard runtime location:

```text
gfx/interface/goals/ireland/
```

`assets/` contains temporary source atlases, chroma-key source tiles, processed
previews, manifests, contact sheets, and staging DDS files. Stable
`GFX_focus_ireland_*` registrations remain owned by
`interface/ireland_icons.gfx`.

## Rejected medallion package evidence

```text
assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_medallion_fresh_2026-07-26/
```

- Fourteen newly generated source atlases cover all 216 focus ids; the last
  atlas contributes the final eight conclusion icons.
- Every consumed focus has a retained fresh `source_png/focus/*_source.png`, a
  keyed and normalized `processed_png/focus/*.png`, a staged DDS, and one
  row-level manifest entry.
- The target is the vanilla goal-icon footprint of 100x88 pixels, with a
  consistent 94x84 safe box for the medallion silhouette.
- Prompt record: `prompts/goal_icon_generation_prompt_set.md`.
- Per-item manifest: `manifest.md`.

## Historical static evidence

- `audit_static.json`: 216 processed icons, all 100x88; 216 unique hashes; no
  empty icons, bright-green subject pixels, opaque corners, or edge contact.
- `audit_runtime.json`: 216 staged DDS, 216 runtime DDS, exact staged/runtime
  hash matches, successful DDS decoding at 100x88, 216 exact `.gfx` pairs, and
  no missing or extra focus registrations.
- `contact_sheets/fresh_hoi4_medallion_goal_icons_contact_sheet.png` shows the
  complete processed package in one review sheet; the runtime DDS files are
  the same hashes recorded in the manifest.

This is static source/package evidence. HOI4 was not launched, so live engine
rendering and GUI click-path validation remain open for the larger feature
audit.
