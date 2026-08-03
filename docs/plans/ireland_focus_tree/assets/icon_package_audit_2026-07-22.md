# Ireland icon package audit - 2026-07-22

> The non-focus allocation audit is retained from 2026-07-22. Focus-goal
> visual acceptance is superseded by
> `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/audit_v12.md`.
> The v12 package is the current 216-row visual and runtime source of truth.

Feature slug: `ireland_focus_tree`
Namespace: `slopx`

This is a static asset-package audit. HOI4 was not launched. Its current-state
registration and path assertions were rechecked on 2026-07-29. Live gameplay
testing is outside the completion gate by user instruction; source clearance
remains independently governed by `source_manifest.json`.

## Static icon package

Each allocated row has a source PNG, processed PNG, and final DDS with matching basenames:

| Family | Rows |
| --- | ---: |
| Focus | 216 |
| Decision categories | 13 |
| Decision actions | 70 |
| Missions | 54 |
| Persistent route spirits | 63 |
| Temporary overlays | 27 |
| Laws | 51 |
| Mechanic and ledger values | 45 |
| Achievement states | 96 |
| **Total** | **635** |

The source and processed staging roots contain 635 allocated files; the canonical runtime DDS set is shipped under the matching `gfx/` roots and contains 635 registered allocations. The source, processed, and runtime DDS sets match one-to-one after the documented `_source` suffix is removed from source PNG names, with no duplicate canonical DDS basenames. The 140 named decision actions intentionally resolve to 70 controlled-reuse textures; no visible decision category repeats a texture. Achievement runtime DDS uses the exact `slopx_ireland_*` IDs; byte-identical ordinal achievement DDS variants retained in `gfx/achievements/` are unreferenced legacy copies outside this allocation count.

The earlier focus packages were rejected for HOI4 focus-icon style and are
retained under
`assets/ireland_focus_tree/icons/rejected_normalized_2026-07-23/` for
technical comparison only. The v12 replacement contains 216 independently
generated focus emblems, 216 processed previews, and 216 DDS rows at 100x88.
Its staging DDS and runtime DDS hashes match one-to-one under
`gfx/interface/goals/slopx_ireland/`.

The row-level evidence is in
`docs/plans/ireland_focus_tree/assets/goal_icon_visual_qa_2026-07-23.md`.

The 70 superseded action rows are retained outside the runtime package at `docs/plans/ireland_focus_tree/assets/retired_icon_candidates/decision_actions/` for recoverability and are not registered or counted in the canonical allocation.

## Registration

- `interface/slopx_ireland_icons.gfx` registers the 216 focus, 13 category, and 140 named action sprites; those action aliases use exactly 70 unique DDS paths.
- `interface/slopx_ireland_secondary_assets.gfx` registers the 54 mission, 63 spirit, 27 overlay, 51 law, 45 mechanic/ledger, and 96 achievement-state sprites.
- The twelve Ireland-owned interface files contain 1,535 texture references to 815 unique paths. Every path resolves, and none points into `assets/`.

## Animation package

All seven approved animations have independent source and processed frames, a horizontal sheet, a static PNG/DDS fallback, a contact sheet, and a GIF review preview. The registered frame counts are 6, 8, 8, 8, 10, 6, and 12, matching the canonical ledger.

## Remaining gates

- The generated icon package is not the blocked source package. The authoritative sourced manifest still contains blocked or review-gated portraits, historical symbol/document packages, and event/news images.
- Source-backed candidate DDS files remain separately marked and are not silently treated as unrestricted clearance.
- The static v12 raster, registration, animation, flag, and path checks are complete. No claim of live gameplay testing is made or required.
