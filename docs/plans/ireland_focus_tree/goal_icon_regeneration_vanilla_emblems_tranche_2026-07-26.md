# Ireland goal-icon regeneration — fresh vanilla-style emblems — 2026-07-26

> Historical tranche. Its first replacement was itself superseded after
> review by `goal_icon_regeneration_focus_emblems_tranche_2026-07-26_v2.md`,
> which is the current runtime and visual source of truth.

## Outcome

The previous circular-medallion package was rejected after comparison with
the actual vanilla national-focus reference set. This tranche regenerates all
216 goal icons from fresh image-generation source atlases and uses the native
HOI4 treatment: isolated, compact, subject-specific painted emblems on a
transparent 100x88 canvas. No old Ireland source, processed PNG, medallion, or
runtime DDS was used as input.

The runtime DDS files are promoted to:

```text
gfx/interface/goals/ireland/
```

`assets/` is staging/provenance only. Stable sprite names remain in
`interface/ireland_icons.gfx`; no gameplay references were renamed.

## Package evidence

- Package: `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_vanilla_emblems_fresh_2026-07-26/`
- Fourteen fresh 4x4 source atlases; the last contributes eight of its sixteen
  generated cells to the 216-icon package.
- 216 fresh `source_png` cells, 216 processed `100x88` RGBA PNGs, 216 staged
  DDS files, and 216 runtime DDS files.
- `manifest.md` describes the asset contract and stable per-item paths.
- `audits/processed_png_audit.json` is the per-item source/processed/DDS
  manifest with hashes, atlas/cell provenance, and dimensions.
- `audits/dds_runtime_audit.json` records 216/216 counts, 100x88 DDS decode,
  216 unique staged hashes, and exact staged/runtime parity.
- `contact_sheets/goal_icons_complete_contact_sheet.png` is the complete
  visual review on a neutral field. The per-atlas sheets are beside it.
- `prompts/atlas_prompts.md` preserves the common generation constraints and
  all atlas theme lists.

## Style checks

Every visible goal subject is centered inside a shared safe area. The static
audit found transparent corners on every PNG, no visible chroma-key green, no
universal square frame, and no DDS dimension mismatch. Fresh atlas files
retain the original green-key source only as temporary provenance; they are
not referenced by the game.

## Validation boundary

The offline source, image, DDS, filename, and runtime-parity checks are
complete. HOI4 was not launched, as requested; live engine rendering and GUI
hover/click validation remain open in the larger Ireland completion audit.
