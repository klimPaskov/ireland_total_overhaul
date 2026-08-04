# Ireland focus icon source handoff — ordinals 204–216

Scope is exactly the 13 missing focus rows 204–216 from
`assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/generation_plan.json`.

All 13 source images were independently generated with the official built-in
`$imagegen` workflow using the exact row prompts in `generation_plan.json`.
The source mode is `built_in_imagegen_chroma_key` with the requested flat
`#ff00ff` magenta source field. No prior Ireland goal icon was used as an edit
target. The generated source canvas is `1254x1254`, matching the existing
source-PNG convention in this package; the parent-owned focus target size is
`100x88`.

This is a source-only handoff. Alpha removal, processed PNGs, DDS conversion,
GFX edits, gameplay edits, localisation edits, and changes to other plan rows
were intentionally not performed.

| Row | Related id | Sprite name | Exact source PNG | Planned runtime DDS | Status |
| ---: | --- | --- | --- | --- | --- |
| 204 | `ireland_otherworld_witnesses` | `goal_ireland_otherworld_witnesses` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_otherworld_witnesses.png` | `gfx/interface/goals/ireland/goal_ireland_otherworld_witnesses.dds` | source complete; processing parent-owned |
| 205 | `ireland_otherworld_evidence_ledger` | `goal_ireland_otherworld_evidence_ledger` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_otherworld_evidence_ledger.png` | `gfx/interface/goals/ireland/goal_ireland_otherworld_evidence_ledger.dds` | source complete; processing parent-owned |
| 206 | `ireland_compact_with_otherworld` | `goal_ireland_compact_with_otherworld` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_compact_with_otherworld.png` | `gfx/interface/goals/ireland/goal_ireland_compact_with_otherworld.dds` | source complete; processing parent-owned |
| 207 | `ireland_containment_protocol` | `goal_ireland_containment_protocol` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_containment_protocol.png` | `gfx/interface/goals/ireland/goal_ireland_containment_protocol.dds` | source complete; processing parent-owned |
| 208 | `ireland_dominion_claim` | `goal_ireland_dominion_claim` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_dominion_claim.png` | `gfx/interface/goals/ireland/goal_ireland_dominion_claim.dds` | source complete; processing parent-owned |
| 209 | `ireland_otherworld_guardians` | `goal_ireland_otherworld_guardians` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_otherworld_guardians.png` | `gfx/interface/goals/ireland/goal_ireland_otherworld_guardians.dds` | source complete; processing parent-owned |
| 210 | `ireland_regional_thresholds` | `goal_ireland_regional_thresholds` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_regional_thresholds.png` | `gfx/interface/goals/ireland/goal_ireland_regional_thresholds.dds` | source complete; processing parent-owned |
| 211 | `ireland_otherworld_statecraft` | `goal_ireland_otherworld_statecraft` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_otherworld_statecraft.png` | `gfx/interface/goals/ireland/goal_ireland_otherworld_statecraft.dds` | source complete; processing parent-owned |
| 212 | `ireland_otherworld_capstone` | `goal_ireland_otherworld_capstone` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_otherworld_capstone.png` | `gfx/interface/goals/ireland/goal_ireland_otherworld_capstone.dds` | source complete; processing parent-owned |
| 213 | `ireland_crown_province_convergence` | `goal_ireland_crown_province_convergence` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_crown_province_convergence.png` | `gfx/interface/goals/ireland/goal_ireland_crown_province_convergence.dds` | source complete; processing parent-owned |
| 214 | `ireland_fivefold_obligation` | `goal_ireland_fivefold_obligation` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_fivefold_obligation.png` | `gfx/interface/goals/ireland/goal_ireland_fivefold_obligation.dds` | source complete; processing parent-owned |
| 215 | `ireland_otherworld_convergence` | `goal_ireland_otherworld_convergence` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_otherworld_convergence.png` | `gfx/interface/goals/ireland/goal_ireland_otherworld_convergence.dds` | source complete; processing parent-owned |
| 216 | `ireland_convergence_order_capstone` | `goal_ireland_convergence_order_capstone` | `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/source_png/focus/goal_ireland_convergence_order_capstone.png` | `gfx/interface/goals/ireland/goal_ireland_convergence_order_capstone.dds` | source complete; processing parent-owned |

The parent should process each source to the planned `100x88` transparent
focus texture, convert it to the listed DDS path, and wire the exact sprite
names on the existing goal `.gfx` surface. The owning `.gfx` filename was not
specified in the parent plan, so none is proposed here.
