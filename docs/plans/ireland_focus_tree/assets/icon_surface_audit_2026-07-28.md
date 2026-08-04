# Ireland Icon Surface Audit

Feature slug: `ireland_focus_tree`
Namespace: `ireland`
Audit date: 2026-07-28
Expanded edge review: 2026-07-29

This is a static visual and raster audit of every Ireland-owned icon family. It
covers the final runtime DDS files and their staging evidence. `assets/` is
temporary source, processing, manifest, and review space; final runtime art is
under the standard mod `gfx/` tree. Live in-game testing is intentionally not
part of this audit, per the implementation instruction.

## Runtime inventory

| Family | Runtime count | Footprint | Result |
| --- | ---: | --- | --- |
| Focus goals | 216 | 100x88 | Freshly regenerated v12; passed edge, corner, alpha, centering, uniqueness, and runtime-hash checks |
| Decision categories | 13 | 52x40 | Detached atlas-edge fragments removed from row 010; row 006 independently regenerated after enlarged review exposed a surviving grey sliver |
| Decision actions | 70 textures / 140 named registrations | 33x32 | Detached atlas-edge fragments removed from 18 rows; controlled reuse remains intentional |
| Mission families | 54 | 33x32 | Six visibly contaminated rows regenerated individually; three minute edge fragments removed |
| Laws | 51 | 60x68 | Freshly regenerated v1 after the old horizontal-alignment defect |
| Spirits | 63 | 60x68 | No true boundary bleed or visible chroma-key defect |
| Mechanic ledger | 45 | 64x64 | No true boundary bleed or visible chroma-key defect |
| Temporary overlays | 27 | 32x32 | No true boundary bleed or visible chroma-key defect |
| Route emblems | 16 | 128x128 and 32x32 | Full-frame emblem composition is intentional |
| Sourced symbols | 9 | Source-specific | Variable framing is intentional; source clearance remains separate |
| Achievements | 96 canonical DDS variants (32 achievements × normal/grey/not-eligible) | 64x64 | Canonical framed square presentation is intentional; 96 unregistered numeric legacy files were removed from the runtime tree and retained only in staging cleanup evidence |
| Animation packages | 7 packages / 14 static and sheet assets | Package-specific | Full-frame sheets and static fallbacks are intentional |

## Goal icons

The current package is:

`assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/`

All 216 goal subjects were regenerated from fresh built-in image-generation
output. The package contains 14 source atlases, 216 source rows, 216 alpha
previews, 216 processed 100x88 previews, a contact sheet, and a row manifest.
The final runtime directory is:

`gfx/interface/goals/ireland/`

The v12 audit found:

- 216 source, alpha, processed, and DDS rows with no missing or extra IDs;
- no source-cell boundary contact or neighboring-atlas bleed;
- no empty icons, opaque corners, off-center subjects, or processed edge contact;
- no fuchsia or greenscreen matte in the processed or DDS rows;
- 216 unique processed hashes and 216 unique DDS hashes;
- exact 100x88 DDS readback dimensions; and
- zero staging-to-runtime hash mismatches.

The stable registrations remain in `interface/ireland_icons.gfx`.

## Law icons

The previous law family was not rejected for a key-color failure; its concrete
defect was inconsistent optical placement. The same 60x68 canvas held visible
bounds centered at approximately x=23 through x=33, so adjacent law states
appeared to jump horizontally in the UI. Reprocessing those old sprites would
have preserved their inconsistent composition, so the family was regenerated.

The current package is:

`assets/ireland_focus_tree/icons/regenerated_law_icons_hoi4_idea_emblems_fresh_2026-07-28_v1/`

Seventeen fresh state-matched triptychs were generated, one for each law
family. Each triptych contains entry, reviewed, and failure columns. The 51
canonical rows were cropped from isolated cells, chroma-key removed, softly
matted, edge-contracted, and normalized around a shared visible center of
`(29.5, 33.5)` in the 60x68 canvas. Pixel-grid quantization leaves no more
than 0.5 pixels of visible-bounds drift. The final runtime directory is:

`gfx/interface/ideas/ireland/laws/`

The v1 audit found:

- 51 processed and 51 DDS rows with exact canonical names;
- exact 60x68 dimensions for every processed and DDS row;
- no source-cell boundary contact in the promoted triptych cells;
- no fuchsia or greenscreen pixels;
- no opaque corners or processed edge contact;
- no visible-center outliers beyond the 0.5-pixel raster quantization allowance; and
- zero staging-to-runtime hash mismatches.

The stable registrations remain in
`interface/ireland_secondary_assets.gfx`. The generated law sources and
processed evidence are symbolic/generated art and do not assert historical
source clearance.

## Decision and mission edge correction

The first contact-sheet pass was not sufficient to expose every small atlas
artifact. A second review enlarged every isolated raster against a checkerboard
field. It found detached fragments close to the cell edge in decision category
010, decision-action rows 009-012, 023, 025-027, 031, 041, 043-044, 054-055,
and 057-060, plus mission rows 003, 007, and 011. Those detached components
were removed without moving, scaling, or repainting the principal subject.

A final enlarged review then caught a separate grey sliver to the right of
decision category 006's compass. That row was regenerated independently as a
single centered antique compass rather than masking the old atlas crop. Its
accepted source, transparent extraction, processed row, DDS, hashes, and
review sheet are retained at:

`assets/ireland_focus_tree/icons/regenerated_decision_category_006_2026-07-29_v1/`

Mission rows 013-015 and 045-047 contained a more serious defect: a substantial
piece of the neighbouring atlas subject intruded into the cell. Those six rows
were not masked or recropped. They were regenerated individually as their
canonical mission subjects and promoted from:

`assets/ireland_focus_tree/icons/regenerated_mission_icons_individual_2026-07-29_v1/`

The regenerated mission rows are centered 33x32 emblems with at least two transparent
pixels of visible clearance, no box or frame, no edge contact, and no chroma
residue. The canonical decision-category, decision-action, and mission contact
sheets were rebuilt after the repair.

The final direct scan compared every processed row to its runtime DDS. Focus,
decision category, decision action, mission, spirit, temporary-overlay, law,
mechanic-ledger, and achievement families have no missing or extra runtime
rows, no processed-to-runtime pixel mismatches, and no surviving strong green
or magenta chroma pixels. Non-full-frame families have transparent corners and
zero edge contact. Achievement icons intentionally use their complete square
frame.

A final runtime-only rerun after the source-research commits opened the actual
DDS files beneath `gfx/`, independent of temporary staging. It inspected 539
transparent icon surfaces: 216 goals, 13 categories, 70 action textures, 54
missions, 51 laws, 63 spirits, 45 mechanic-ledger icons, and 27 temporary
overlays. The scan found zero opaque edge contacts, zero saturated
green-screen candidates, and zero detached secondary components touching any
edge. A separate pass opened all 96 registered 64x64 achievement variants and
found zero dimension errors and zero saturated green-screen candidates.

## Other icon families

Spirits, mechanic-ledger symbols, and temporary overlays were inspected as
isolated runtime rasters and enlarged contact sheets. Apparent pale squares in
their review sheets are the checkerboard transparency field, not baked UI
boxes. Their detached details were compared visually against the complete
subject before being accepted; legitimate bases, shadows, radio waves, chains,
and heraldic parts were not erased. They have transparent framing, no
neighbouring-cell subject, no opaque-corner contamination, and no visible
chroma-key matte. Broad color heuristics were not treated as defects when they
matched legitimate olive, green, or teal painted content.

Route emblems, sourced symbols, achievement variants, and animation sheets
were also reviewed. Their opaque or full-frame areas are part of their intended
asset type: emblem marks use full-frame composition, sourced symbols retain
source-specific framing, achievements use their square presentation, and
animation sheets are frame-packed surfaces. They were not altered because
normalizing those surfaces would damage their registered framing rather than
fix an alignment defect.

The sweep also found 96 ordinal `achievement_ireland_###` DDS files in the
runtime directory that had no `.gfx` registration or gameplay reference. They
were not part of the canonical achievement package. They are retained at
`assets/ireland_focus_tree/icons/runtime_cleanup/legacy_numeric_achievements_2026-07-28/`
as staging-only cleanup evidence; the runtime tree now contains only the 96
registered `ireland_*` variants.

## Wiring and staging boundary

The final DDS paths are:

- `gfx/interface/goals/ireland/`
- `gfx/interface/decisions/categories/ireland/`
- `gfx/interface/decisions/ireland/actions/`
- `gfx/interface/decisions/ireland/missions/`
- `gfx/interface/ideas/ireland/laws/`
- `gfx/interface/ideas/ireland/spirits/`
- `gfx/interface/ireland/mechanic_ledger/`
- `gfx/interface/ireland/temporary_overlays/`
- `gfx/interface/ireland/emblems/`
- `gfx/interface/ireland/sourced/`
- `gfx/achievements/`
- `gfx/interface/animated/ireland/`

The goal registrations remain in `interface/ireland_icons.gfx`; the law,
spirit, mission, overlay, ledger, and achievement registrations remain in
`interface/ireland_secondary_assets.gfx`; animation registrations remain
in `interface/ireland_animation_assets.gfx`. No runtime texture path
points into `assets/`.

## Remaining non-asset gates

This audit closes the visual alignment/chroma issue found in the icon families,
but it does not close source clearance, unresolved canonical design rulings,
engine-reference checks, gameplay scenarios, or the wider Ireland overhaul
completion audit. Those remain recorded in the project status and source-of-
truth documents.
