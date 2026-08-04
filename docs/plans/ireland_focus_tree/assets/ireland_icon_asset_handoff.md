# Ireland focus-tree icon asset handoff

Status: complete for the bounded asset-production scope on 2026-07-18.

Current implementation reconciliation (2026-07-29): the canonical package
includes 216 v12 focus rows, 13 category rows, and 70 allocated decision-action
texture rows. All 140 named action aliases are wired to those 70 textures with
no within-category duplicate; the 70 superseded ordinal rows are retained
outside the runtime package under
`docs/plans/ireland_focus_tree/assets/retired_icon_candidates/decision_actions/`.
See `docs/plans/ireland_focus_tree/assets/icon_package_audit_2026-07-22.md`
for the reconciled counts and registration evidence.

Canonical ledger: [ireland_icon_animation_manifest.md](../../../../assets/ireland_focus_tree/icons/ireland_icon_animation_manifest.md)

## Completed package

| Family | Completed |
| --- | ---: |
| Focus icons | 216 source PNG + 216 processed PNG + 216 DDS |
| Decision category icons | 13 source PNG + 13 processed PNG + 13 DDS |
| Decision action textures | 70 source PNG + 70 processed PNG + 70 DDS; 140 named aliases with controlled cross-category reuse |
| Mission icons | 54 source PNG + 54 processed PNG + 54 DDS |
| Persistent route-spirit icons | 63 source PNG + 63 processed PNG + 63 DDS |
| Temporary-overlay icons | 27 source PNG + 27 processed PNG + 27 DDS |
| Law icons | 51 source PNG + 51 processed PNG + 51 DDS |
| Mechanic/ledger icons | 45 source PNG + 45 processed PNG + 45 DDS |
| Achievement states | 96 source PNG + 96 processed PNG + 96 DDS; 32 concepts x completed/grey/not-eligible |
| Independent animations | exactly 7; 58 source frames + 58 processed frames, 7 sheets, 7 static fallbacks, 7 GIF previews, 7 contact sheets |

Every focus icon also has a paired animated shine registration in `interface/ireland_focus_shine.gfx`. The masks use the final focus DDS files under `gfx/interface/goals/ireland/`, and the standard shine effect surface is present at `gfx/interface/goals/shine_overlay.dds`.

Source and processed assets remain under `assets/ireland_focus_tree/icons/{source_png,processed_png}/`; final runtime DDS files are shipped under the corresponding `gfx/` roots. The six class contact sheets are under `assets/ireland_focus_tree/icons/contact_sheets/`. The exact row patterns, ranges, spirit runtime-name mapping, and dimensions are in the canonical manifest.

Animations are under `assets/ireland_focus_tree/animations/` using the exact requested slugs and frame counts:

- `hidden_evidence_seal_reveal` — 6 frames, 64x64, 6 FPS, no loop
- `ailtiri_takeover_seal` — 8 frames, 96x96, 8 FPS, no loop
- `high_kingship_crown_selection` — 8 frames, 96x96, 8 FPS, no loop
- `five_provinces_compact` — 8 frames, 96x96, 8 FPS, no loop
- `verified_otherworld_entry` — 10 frames, 128x128, 8 FPS, no loop
- `compact_breach_warning` — 6 frames, 64x64, 6 FPS, loop
- `convergence_conclusion_seal` — 12 frames, 128x128, 8 FPS, no loop

Each animation contains independently generated `source_frames/`, processed `processed_frames/`, `<slug>_static.png`/`.dds`, `sheets/<slug>_sheet.png`/`.dds`, `previews/<slug>_preview.gif`, and `<slug>_contact.png`.

## Provenance and checks

- Official image generation was used for symbolic/alternate/institutional/supernatural art only. No real leaders, real-person likenesses, historical documents/symbols, vanilla substitutions, or placeholders were used.
- Atlas/source evidence remains under `assets/ireland_focus_tree/icons/source_atlases/`. Laws `025..032` were individually regenerated and reprocessed to remove cross-cell leakage; law `026` was restored after a cleanup filter incorrectly removed its valid subject.
- Alpha was processed through the repository chroma-key workflow. Static contact sheets were reviewed over checkerboard transparency; animation contacts were reviewed over the key-color field. The animation frames show frame-to-frame subject changes and were not made by moving, scaling, rotating, blurring, recoloring, or filtering one still.
- DDS conversion used `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py`. Readback checks confirmed every static DDS, animation fallback DDS, and animation sheet DDS has the documented dimensions. File-count checks confirmed all requested static ranges and all seven animation frame ranges.

## Remaining blockers / owning-agent actions

1. The `ireland_NNN` package basenames are mapped to the canonical mission, overlay, law, mechanic/ledger, and achievement runtime IDs in `interface/ireland_secondary_assets.gfx`.
2. Spirits use the ordered `GFX_ireland_spirit_*` mapping in the canonical manifest and implementation registration.
3. Static DDS paths, animation sheet frame counts/rates, static fallbacks, and achievement state variants are registered in the Ireland-owned `.gfx` files. All seven animated and seven static sprites are assigned across the three Ireland GUI surfaces.
4. The documented 60x68 spirit/law and 64x64 mechanic/ledger dimensions are registered against the current UI surfaces. Live gameplay testing is outside the completion gate by user instruction.

No production asset-count or conversion blocker remains within this worker's allowed paths. No gameplay, GFX, GUI, localisation, specs, or unrelated files were changed by this handoff.
