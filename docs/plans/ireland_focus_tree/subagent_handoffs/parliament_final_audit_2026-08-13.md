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

## Closure re-audit | 2026-08-13

### Scope and patch

Re-audited the live industrial-contract and territorial-policy package alongside the Parliament decision surface. The only new patch is in `localisation/english/ireland_l_english.yml`:

| Key | Before | After |
| --- | --- | --- |
| `ireland_parliament_seanad_button_tt` | The live checklist omitted the `ireland_settlement_open` condition used by the GUI and native action gate. | It now includes `[ROOT.GetIrelandParliamentSettlementOpenStatus]` between the Dáil-stage and National Settlement rows. |

No thumbnail, focus, event, asset, GUI layout, decision, or scripted-helper source was changed in this closure pass.

### Expansion decision contract

| Required surface | Current evidence |
| --- | --- |
| Nine company-specific contracts | `ireland_contract_esb_grid_works`, `ireland_contract_transport_fleet`, `ireland_contract_merchant_tonnage`, `ireland_contract_state_materials`, `ireland_contract_ford_motor_works`, `ireland_contract_aer_lingus_transport`, `ireland_contract_turf_fuel_reserve`, `ireland_contract_steel_foundry`, and `ireland_contract_belfast_refit` each have their own unlock flag, one-use action, effect, AI block, and localisation. |
| Five Northern methods | The democratic plebiscite, communist workers' campaign, fascist ultimatum, oligarchic Belfast compact, and restoration provincial assent are individually route-gated. The plebiscite delegates to the existing supervised-plebiscite mission. |
| Three noncoercive Atlantic actions | Welsh and Scottish support actions provide an equipment delivery when the recipient exists and always record their political support. The basing action grants access from the current controller of State 120. None grants an Irish core or claim. |
| Coercive State 119, 120, 122, and 123 actions | The fascist State 119 ultimatum leads to the State 119 enforcement action; State 120 precedes 122, which precedes 123. Each is one-use, is priced and timed, refunds 25 PP when its target becomes invalid, revalidates the live owner/controller and faction relation at completion, and uses the live controller as the war-goal target. |
| Readiness and strength safeguards | `ireland_atlantic_claim_enforcement_ready` requires peace, the route and Readiness conclusion, Dublin control, Dáil majority, manpower, infantry equipment, support equipment, convoys, fuel, command power, and `alliance_strength_ratio > 0.74`. Each target also checks that its controller remains below the 1.25 direct strength-ratio limit. |
| Postwar outcomes | State 120, 122, and 123 receive separate local-rights outcomes; States 120 and 122 have Scottish or Welsh protectorate outcomes; State 120 alone has the bounded integration review. All record `ireland_atlantic_state_settlement_recorded`; the conclusion focus sets `ireland_atlantic_settlement_concluded` and clears the review-start flag. |

### Parliament lifecycle and checklist result

The settlement category and scripted GUI become visible once original Ireland has initialized, use `visible_when_empty = yes`, and retain the free opening Dáil action at stage one while Ireland owns Dublin. All four GUI buttons and native actions still call the same guarded executors, with 0, 25, 25, and 35 PP debits respectively.

The complete grey-button checklists now match their canonical availability helpers. The panel itself is hidden when Parliament is not open, so the omitted open-state condition is not a visible grey-button cause. The Dáil checklist names stage, Dublin, and incomplete status. Seanad now names stage, settlement open, National Settlement, Dublin, incomplete status, below-majority status, and 25 PP. Confidence and budget continue to name every stage, focus, settlement, chamber, Dublin, completion, and PP condition relevant to their action.

### Mission quality and cleanup findings

| Mission | Owner | Category | Region | Duration | Success / failure / cleanup | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `ireland_mission_conduct_a_supervised_plebiscite` | IRE | existing Northern category | State 119 and Dublin evidence | 240 days | Reuses established full, partial, failure, cancellation, material-refund, and capacity cleanup. | Guarded by its active flag. |
| `ireland_mission_complete_atlantic_settlement` | IRE | `ireland_territorial_policy` | States 120, 122, 123, SCO, and WLS | 365 days | Cancels on `ireland_atlantic_settlement_concluded`; timeout applies the stated penalty only when no settlement was recorded, clears the start flag, and records expiry. | Its one review-start flag prevents a second review action. |

### Remaining parent review items

1. **Medium:** The Atlantic settlement mission is not presently counted by `ireland_update_mission_capacity`, and `ireland_territorial_open_postwar_review` does not check `ireland_can_launch_postwar_mission` before activating it. This can bypass the postwar mission-capacity model.
2. **Medium:** The Atlantic mission's `cancel_trigger` only watches the conclusion flag. If Ireland loses every relevant State 120, 122, and 123 control position and both subject relationships before conclusion, the stale mission remains until timeout. No per-state reservation flag currently exists to clean on transfer, release, or peace as described in the accepted addendum.
3. **Low:** The coercive completion blocks revalidate target ownership, control, and faction relation. They do not repeat the readiness or strength checks at the final tick. This is not contrary to the implemented player-facing contract, which promises target revalidation, but it remains the boundary of the present safeguard.

The expansion sources were being actively amended during this audit, so the three items above were reported to the parent rather than patched from this worker.

### Validation evidence

- Confirmed the nine company, five Northern, three noncoercive Atlantic, and staged coercive IDs directly from `common/decisions/ireland_expansion_decisions.txt`.
- Confirmed the readiness and alliance-ratio trigger against the offline trigger reference and vanilla POR/SWI strength-ratio precedents.
- Confirmed company, territorial, mission, and Parliament localisation references and the patched English file's UTF-8 BOM.
- Fresh full `hoi4.gui_inspect` completed without blockers: revision `b13cbfa44bde350de6cbc5442c9acb47c8e8ee2447151f707f9cd14311478c60`, artifact `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/836f41f25c887929c6d73301c7c6b07f9487cdae19502a20144061c71e754560/5001161d5d6325d39ab8015600553acc861da53c1d545adc1a570c4458b5949d/gui-inspect.b13cbfa44bde350d.json`.

### Parent closure of adjacent expansion findings

The three parent-review items above were subsequently closed. The Atlantic
mission now uses the canonical launch gate, participates in both global and
postwar capacity counts, and clears its active marker on conclusion, timeout,
route cleanup, or loss of every relevant controlled-state/subject relation.
The State 119, 120, 122, and 123 coercive completion blocks repeat the complete
readiness and exact controller-strength/faction/control contracts before
issuing an outcome, with the stated Political Power refund if conditions have
changed. The earlier alliance-ratio note was removed because the action is
peace-gated; the live target-controller ratio is the meaningful comparison.
