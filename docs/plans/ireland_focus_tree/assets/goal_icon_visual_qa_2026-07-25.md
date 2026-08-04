# Ireland goal-icon visual QA — v4 direct regeneration

Feature slug: ireland_focus_tree  
Namespace: ireland  
Review date: 2026-07-25  
Runtime target: gfx/interface/goals/ireland/

> Superseded historical QA. The v4 direct-regeneration package is no longer
> the runtime package. Use the fresh vanilla-emblem tranche dated 2026-07-26
> and its manifest/audits for current goal-icon evidence.

## Disposition

The earlier v3 package is rejected for the runtime style. Its source package relied on large composite atlas imagery with bulky outlined objects and was not a consistent compact national-focus emblem family. It remains in the workspace as historical evidence only.

The v4 package is historical evidence only. Every one of the 216 focus IDs received a separate fresh built-in image-generation call from the shared v4 prompt and an explicit semantic subject brief. No earlier icon, atlas, DDS, contact sheet, vanilla icon, or other supplied image was passed as an image-generation input. The only common processing step was build-time chroma-key removal, alpha decontamination, and fitting to the shared target canvas.

## Style contract

- One compact hand-painted HOI4 focus-goal emblem per focus, or one inseparable symbolic pair.
- Target canvas is 94x86 RGBA PNG with a centered visible silhouette and transparent corners.
- Shallow painted relief and restrained brass, bronze, iron, cream, olive, deep-red, and desaturated-blue materials.
- No text, letters, numbers, maps, flags, UI, cards, panels, plaques, boxes, frames, ribbons, badges, medals, shields, coats of arms, circular medallion templates, oversized wreaths, people, or faces.
- Green is used only as the temporary source chroma key. It is removed before processing and never appears as an opaque background in the runtime DDS.

## Package evidence

| Layer | Expected | Measured | Location |
|---|---:|---:|---|
| Focus IDs | 216 | 216 | common/national_focus/ireland_focus_tree.txt |
| Fresh direct source PNGs | 216 | 216 | assets/ireland_focus_tree/icons/regenerated_goal_icons_v4_2026-07-25/source_png/focus |
| Processed RGBA PNGs | 216 | 216 | assets/ireland_focus_tree/icons/regenerated_goal_icons_v4_2026-07-25/processed_png/focus |
| Historical staging DDS files | 216 | 216 | assets/ireland_focus_tree/icons/regenerated_goal_icons_v4_2026-07-25/final_dds |
| Promoted runtime DDS files | 216 | 216 | gfx/interface/goals/ireland |
| Runtime sprite registrations | 216 | 216 | interface/ireland_icons.gfx |

## Static checks

- Every focus ID has exactly one matching source PNG, processed PNG, staged DDS, and runtime DDS.
- Processed PNGs are 94x86; all four corners are transparent; no silhouette is empty, oversized, or outside the centering tolerance.
- The processed set has 216 unique image hashes; no duplicate row was accepted.
- DDS readback opened all 216 files as DDS at 94x86 with no conversion failures.
- Runtime DDS hashes match the staged v4 DDS hashes for all 216 names.
- The complete processed contact sheet is `assets/ireland_focus_tree/icons/regenerated_goal_icons_v4_2026-07-25/v4_goal_icons_contact_sheet.png`.
- The per-item manifest is `assets/ireland_focus_tree/icons/regenerated_goal_icons_v4_2026-07-25/manifest.md`.

## Visual corrections made during review

The first direct source assignment was corrected so the church-bell source belongs to clerical guardianship and the gear-and-seal source belongs to producer constitution. Costello, clerical route, IRA route, O'Duffy personal, and O'Duffy corporate capstones were regenerated after review because their first versions read as a shield, plaque, medal, or trophy. The replacement symbols are direct object emblems and were included in the final contact-sheet review.

HOI4 was not launched for this package. In-engine texture loading, focus-tree rendering, zoom/readability, and live save scenarios remain separate validation gates for the overall Ireland feature.
