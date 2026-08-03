# Ireland physical action-input tranche

## Scope

This narrow decision pass replaces seven abstract political-power and command-power actions with visible, nonrecoverable physical commitments. It preserves the thirteen categories, the 140 mapped action IDs, all 54 mission families, active caps, route gates, core rules, and existing cleanup ownership.

## Changed files

- `common/decisions/slopx_ireland_decisions.txt`
- `localisation/english/slopx_ireland_l_english.yml`

## Changed actions

| Action ID | New availability gate | Completion charge | Lifecycle rationale |
| --- | --- | --- | --- |
| `slopx_ireland_action_commission_a_developmental_plant` | 50 Support Equipment and 5 Convoys | 50 Support Equipment and 5 Convoys | Imported machinery is a one-time project commitment. |
| `slopx_ireland_action_open_a_g2_liaison_channel` | 20 Support Equipment | 20 Support Equipment | Secure communications are consumed in establishing the channel. |
| `slopx_ireland_action_intercept_an_airspace_violation` | 5 Fighters and 100 Fuel | 5 Fighters and 100 Fuel | The interception spends aircraft readiness and fuel. |
| `slopx_ireland_action_send_an_american_procurement_mission` | 5 Convoys | 5 Convoys | The acquisition route commits carrying capacity before delivery resolves. |
| `slopx_ireland_action_prepare_a_wartime_unity_bargain` | 50 Infantry Equipment and 25 Trucks | 50 Infantry Equipment and 25 Trucks | The proposed defence contribution must be materially credible. |
| `slopx_ireland_action_restore_belfast_industrial_contracts` | 100 Support Equipment and 50 Trucks | 100 Support Equipment and 50 Trucks | Repair and delivery work begins before the Belfast mission can resolve. |
| `slopx_ireland_action_launch_a_reconstruction_portfolio` | 50 Support Equipment and 25 Trucks | 50 Support Equipment and 25 Trucks | First reconstruction works require equipment and transport at launch. |

## Behaviour

Before this patch, every listed action could pass its state, route, capacity, political-power, and command-power checks without a stockpile or fuel commitment. They now remain unavailable until their named physical inputs are present, charge those inputs in `complete_effect`, then follow the existing mission or direct-result lifecycle.

The existing ledger-driven Action Burden remains dynamic. Physical charges are deliberately fixed at launch, rather than scaled after the availability check, so scarcity cannot make an otherwise valid action silently fail its stockpile deduction. None of these inputs are refunded because their linked cleanup routines do not own a recoverable-input ledger and the source spec treats fuel, used equipment, shipping, and completed work as nonrecoverable.

## Validation run

- Targeted structural check reports `action_count = 140`, `mission_count = 54`, and `brace_balance = 0` for `common/decisions/slopx_ireland_decisions.txt`.
- The check found 24 input macros (gate and charge values for the seven actions). Each action has the expected gate-to-charge pair count, the same resource and magnitude at both ends, and exactly one updated requirement tooltip.
- Apart from the four file-header declarations, the wartime-unity macro family occurs only inside `slopx_ireland_action_prepare_a_wartime_unity_bargain`; this specifically catches the initially misplaced British-flexibility insertion.
- The touched decision blocks contain no unsupported `<=` or `>=` operators. The localisation file retains a UTF-8 BOM.

## Skipped validation

- No engine parser or live game session was run. The parent should validate this together with the integrated Ireland package because the decision source file was already untracked in the shared worktree before this tranche.

## Remaining risks

- Other abstract actions remain in Neutrality, Foreign, Northern, Occupation, and Postwar. They were not changed because their physical commitment needs either a dedicated recovery ledger, partner-side delivery accounting, or a broader balance pass.
- The action cost surface continues to show the native political-power price while the detailed requirement tooltip names the new physical charges. A future shared custom-cost presentation would require a broader UI/localisation pass and should not be added in this narrow tranche.
