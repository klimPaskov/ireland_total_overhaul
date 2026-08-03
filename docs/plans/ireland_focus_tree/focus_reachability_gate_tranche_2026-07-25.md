# Ireland focus reachability gate tranche — 2026-07-25

## Purpose

The focus audit found eleven dead focuses whose `available` blocks required a
`*_ready` flag written only by that same focus. Those gates could never be
true in a fresh game, blocking the shared readiness chain and every dependent
route conclusion. This tranche replaces only the circular positive gate with
an already-owned prerequisite, route milestone, or live partner check.

## Reachability repairs

| Focus | Circular gate removed | Authoritative gate used |
| --- | --- | --- |
| `slopx_ireland_air_warning` | `slopx_ireland_air_warning_ready` | `slopx_ireland_civilian_defence_review_ready` plus completed readiness command |
| `slopx_ireland_maritime_protection` | `slopx_ireland_maritime_protection_ready` | `slopx_ireland_port_defence_authority_ready` plus completed maritime reserve |
| `slopx_ireland_emergency_mobilisation` | `slopx_ireland_emergency_mobilisation_ready` | `slopx_ireland_emergency_review_started` plus completed emergency opening |
| `slopx_ireland_american_diaspora_mission` | `slopx_ireland_american_mission_ready` | `slopx_ireland_american_partner_valid` plus completed minority guarantees |
| `slopx_ireland_vatican_small_state_mediation` | `slopx_ireland_vatican_mediation_ready` | `slopx_ireland_vatican_partner_valid` plus neutrality and minority guarantees |
| `slopx_ireland_foreign_safeguards` | `slopx_ireland_foreign_safeguards_ready` | British, American, and Vatican channel-open flags |
| `slopx_ireland_northern_local_authorities` | `slopx_ireland_northern_local_authority_ready` | `slopx_ireland_northern_ledger_open` plus public-order review |
| `slopx_ireland_northern_trade_corridor` | `slopx_ireland_northern_trade_corridor_ready` | completed Northern local authorities plus 1938 trade settlement |
| `slopx_ireland_northern_labour_social_bridge` | `slopx_ireland_northern_labour_bridge_ready` | completed Northern local authorities plus church-labour consultation |
| `slopx_ireland_convention_of_commands` | `slopx_ireland_ira_command_convention_ready` | `slopx_ireland_security_exposure_ready` plus Northern contacts |
| `slopx_ireland_language_cells` | `slopx_ireland_ailtiri_language_network_ready` | `slopx_ireland_ailtiri_cells_ready` |

The completion rewards retain the historical `*_ready` and `*_complete`
markers where they are used by downstream runtime systems. They are no longer
used as the target focus's own entry ticket.

## Visible route gates

The 1938 Treaty Port transfer now has visible focus prerequisites for the 1938
trade settlement and port-and-coast audit. The sovereignty mandate now visibly
requires the Treaty Port transfer and presidential settlement. The existing
`available` blocks remain in place, so the visible links do not remove date,
flag, or completion requirements.

## Boundary checks

- No Northern state control, occupation, settlement, integration stage, or
  core is granted by these repairs.
- No route is unlocked by deleting its other requirements.
- Partner checks remain live checks and do not create a foreign actor.
- The audit target is source reachability; live engine/scenario validation is
  still an open completion gate because HOI4 is not launched in this task.

## Static result

The post-edit source scan found 216 unique focus IDs, zero unknown focus
prerequisite references, and no remaining self-written `*_ready` entry gate
among the eleven audited focuses. Four unrelated route milestones still use
their own ready markers alongside externally established route state; those
are not part of the dead chain identified by the auditor.

## Files

- `common/national_focus/slopx_ireland_focus_tree.txt`
- `docs/plans/ireland_focus_tree/project_status.md`
