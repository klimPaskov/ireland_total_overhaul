# Parliament final audit | 2026-08-13

## Scope

Audited the Ireland Parliament decision category, its four native actions, the shared scripted GUI executors, presentation assets, and their localisation. This audit did not change focuses, events, or unrelated localisation.

## Changed files

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `interface/ireland_parliament_scripted_gui.gui` | `ireland_parliament_title` | The parchment-top title used the light `hoi_16mbs` font. | The title remains at `@TITLE_Y = 7`, but uses `vic_18_black` at 18 px for readable dark contrast without crossing into either chamber panel. |
| `localisation/english/ireland_l_english.yml` | `ireland_parliament_*_button_tt`, `ireland_action_*_requirements_tt` | The four GUI and four native requirements tooltips said “control of Dublin”. | They say “Irish ownership of Dublin”, matching `any_owned_state = { state = 113 }`. |

No decision, mission, scripted-effect, scripted-trigger, asset, or GFX identifier was added or renamed.

## Issues, ordered by severity

1. **Medium, fixed:** `ireland_parliament_title` was low contrast against the supplied light parchment background. The prescribed black Victoria font is now used at its 18 px native height.
2. **Low, fixed:** The player-facing Dublin requirement implied a control test while the actual guard is ownership. All eight action tooltips now describe the actual rule.
3. **Low, no gameplay defect:** GUI inspection reports three `GUI_COST_MISMATCH` findings. The inspector does not follow a GUI effect into the shared executor in `common/scripted_effects/ireland_parliament.txt`, where the Political Power deltas are applied. Adding a second direct cost to appease the inspector would double-charge the player and violate the shared-executor contract.

## Decision category lifecycle

`ireland_settlement_government` appears for initialized original Ireland until the route is archived. Its Parliament surface is visible through `ireland_parliament_open`.

| Stage | Native human action | Current requirement | Cost | Completion and next state |
| --- | --- | --- | --- | --- |
| 1 | `ireland_action_convene_the_dail` | initialized Ireland owns Dublin | 0 PP | `ireland_record_parliament_dail_session` sets the Dáil completion flag and opens the settlement, advancing the stage. |
| 2 | `ireland_action_negotiate_seanad_support` | National Settlement focus complete, settlement open, Dublin owned, 25 PP | 25 PP | Sets the Seanad completion flag and advances the stage. |
| 3 | `ireland_action_secure_a_confidence_compact` | Constitutional Draft focus complete, settlement open, Dublin owned, 25 PP | 25 PP | Sets the confidence completion flag and advances the stage. |
| 4 | `ireland_action_pass_a_joint_budget` | Government Formation focus complete, both chamber majorities, Dublin owned, 35 PP | 35 PP | Sets the joint-budget completion flag and advances to the completed summary state. |

All four GUI buttons and native actions call `ireland_execute_parliament_dail_action`, `ireland_execute_parliament_seanad_action`, `ireland_execute_parliament_confidence_action`, or `ireland_execute_parliament_budget_action`. Each executor repeats its canonical availability guard before recording results. The four `fire_only_once` native actions and their matching completion flags prevent duplicate rewards through either surface.

## Mission quality notes

There are no Parliament missions or timed objectives in this package. The owner is IRE, the category is `ireland_settlement_government`, and each decision’s regional condition is ownership of Dublin. Duration, timed success or failure, and duplicate-mission risk are not applicable. Immediate success is defined by the guarded record helper; unavailable or completed actions have no effect.

## Cost and requirement clarity

The configured costs are centralised in `common/script_constants/ireland_constants.txt`: 0, 25, 25, and 35 PP. The paid actions use strict PP gates of 24, 24, and 34 because `has_political_power` is a strict comparison. The free opening action has no PP gate, so it can be clicked immediately after initialization whenever Ireland owns Dublin.

The four visual states are distinct GFX assets and use the central frame values: locked 1, unaffordable 2, current 3, complete 4. Four separate sprite identifiers are wired in `interface/ireland_gui_assets.gfx` to their own DDS files.

## AI validity and route locks

The GUI is explicitly human-only. Native decisions retain AI weights of 10, 9, 8, and 7, and have no unsafe country target. All actions require the original Irish tag and are removed when `ireland_route_archived` is set. Later actions are focus and stage gated, so the AI cannot reach a closed escalation step. Dublin ownership is checked both in the canonical action triggers and in the player-facing requirements text.

## GUI evidence

Fresh scripted-GUI inspection found no visible control overlap in either the initial or later state. The title ends at the chamber-panel boundary, and the native 18 px black font is legible on the light top band. The action buttons remain four separate 204 by 32 regions with their icon regions outside the buttons.

- Initial-state render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/b7a19282e7a667721df351321fe926be5695f4d8b77fc549eab3e8fb2c76418e/764fa6b835d3bdcce9afbf3c354ca19ee28382c2a7d20f28e7f513eb6ec61ba2/ireland_parliament_decision_ui_window-full.svg`
- Later-state render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/718dd78e6ba28b1d774230cf0668c814177e9f75c32153916a2c233f43f70fcc/a4db2d217e24a36e01445dcca08a464c1a51ea4f49f95a93215ce924855410d1/ireland_parliament_decision_ui_window-full.svg`
- Initial-state inspection: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/dd70fc84de544c027805ad6c665a1b9f27e3b49f76b6e7973176964d92758bf8/a2f239320eea25f8dc46bedcb1b9f50499bd3b865a80ae2e9f26c0c643a99862/gui-inspect.d505a6cac93d69c7.json`
- Later-state inspection: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8cd93c6377bb1a1d753b45f66873d5442f16ce43770f828e942ce8fd412be953/906bfad1e1d5d8446cf2ed3d870381487aa900af9f114c9843cb38661e33dc50/gui-inspect.d505a6cac93d69c7.json`

The offline renderer reports partial sprite fidelity because its button-state and glyph support are incomplete. This does not indicate a missing project sprite: all four state DDS files and their GFX declarations are present.

## Validation

- Reviewed the native decision `complete_effect` calls against the GUI effects and confirmed that each reaches the same guarded executor.
- Confirmed the opening Dáil executor has no Political Power debit or gate, while the later executors debit the matching central constants.
- Rendered and inspected the initial and later GUI states after the font change. No visible overlap was reported.
- A fresh full `hoi4.gui_inspect` pass returned no malformed-localisation diagnostic. The earlier targeted warning was not reproducible and is not treated as a project issue.
- Checked the two patched files for whitespace errors and confirmed the localisation file retains a UTF-8 BOM.

## Remaining issues and risks

- The GUI inspector continues to emit the cross-file cost false positives noted above. Treat them as a tooling limitation unless a runtime test shows a missing debit.
- No active Parliament missions, event targets, timed flags, or country targets exist, so there is no additional stale-target cleanup path to patch.

## Plan handoff

No broader mechanic was identified. This audit file is the required handoff: `docs/plans/ireland_focus_tree/subagent_handoffs/parliament_final_audit_2026-08-13.md`.

## Skills used

Applied `hoi4-decisions-missions`, `hoi4-events`, and `hoi4-subagents`. No skill was created or changed.
