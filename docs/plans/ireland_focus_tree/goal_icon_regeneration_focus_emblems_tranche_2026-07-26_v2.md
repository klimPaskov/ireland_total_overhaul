# Ireland focus-goal icon regeneration — superseded compact emblems — 2026-07-26 v2

> Historical evidence only. This package was replaced after review because
> its shared round/oval plaque treatment did not match the vanilla HOI4
> national-focus goal-icon style. The current package is documented in
> `docs/plans/ireland_focus_tree/goal_icon_vanilla_style_regeneration_2026-07-26.md`.

## Outcome

The previous loose-object goal-icon batch was rejected because it did not read
as a coherent HOI4 national-focus icon family. This tranche generates a new
216-icon package from fourteen brand-new 4x4 image-generation atlases. Every
retained cell uses the same compact painted focus-emblem treatment: one
centered subject on a small round or oval bronze-and-dark-iron plaque, with a
shared safe area, muted aged palette, and no square tile, box, full-field
background, or visible key-green.

The runtime files are promoted to the standard game path:

```text
gfx/interface/goals/ireland/
```

`assets/` remains temporary source, processing, provenance, and review space.
Sprite names and focus references remain unchanged.

## Evidence

- Package: `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-26_v2/`
- Source: fourteen fresh `source_atlases/atlas_01.png` through `atlas_14.png`
  files; atlas 14 contributes its first eight cells.
- Per-item outputs: 216 source crops, 216 chroma-key alpha outputs, 216
  centered 100x88 RGBA previews, and 216 final DDS files.
- Prompt record: `prompts/atlas_prompts.md`.
- Per-item manifest: `manifest.json`; package contract:
  `manifest.md`.
- Visual review: `contact_sheets/goal_icons_complete_contact_sheet.png`.
- Static PNG audit: `audits/processed_png_audit.json`.
- DDS/runtime parity audit: `audits/dds_runtime_audit.json`.

The processed audit records 216/216 files, 100x88 dimensions, no empty icons,
no opaque corners, no visible key-green, no edge contact, and no off-center
rows. The DDS/runtime audit records 216 staged files, 216 runtime files, 216
unique hashes on each side, 100x88 dimensions throughout, and zero parity
mismatches.

## Build boundary

The generation step created new source atlases. The subsequent build steps only
performed standard atlas cropping, chroma-key removal with the installed
imagegen helper, shared-canvas fitting, contact-sheet generation, and the
repository DDS conversion. No older Ireland icon package was used as a source,
and no game launch was performed.

## Remaining validation

The asset-source and runtime-parity checks are complete. Live HOI4 loading,
focus-tree rendering, hover readability, and shine-mask presentation remain
open with the larger Ireland completion audit; HOI4 was not launched per the
user's instruction.
