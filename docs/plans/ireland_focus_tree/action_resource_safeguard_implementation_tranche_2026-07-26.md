# Ireland Action-Resource Safeguard Implementation Tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

Status: source-level implementation complete; live validation open

## Scope

This tranche implements the accepted bounded addendum in `action_resource_safeguard_improvement_addendum_2026-07-26.md`. It repairs four existing action/mission pairs without adding actions, missions, events, focuses, routes, categories, laws, ideas, GUI surfaces, or assets. The inventory remains exactly 140 actions and 54 mission families.

## Shared contracts

Twelve side-effect-free country-scope scripted triggers in `common/scripted_triggers/slopx_ireland_triggers.txt` are the shared source of truth:

- `slopx_ireland_rail_corridor_admission_valid`, `slopx_ireland_rail_corridor_full_valid`, and `slopx_ireland_rail_corridor_partial_valid`.
- `slopx_ireland_essential_cargo_route_capacity_valid`, `slopx_ireland_essential_cargo_full_valid`, and `slopx_ireland_essential_cargo_partial_valid`.
- `slopx_ireland_command_district_force_commitment_valid`, `slopx_ireland_command_district_exercise_full_valid`, and `slopx_ireland_command_district_exercise_partial_valid`.
- `slopx_ireland_belfast_contract_admission_valid`, `slopx_ireland_belfast_industry_full_valid`, and `slopx_ireland_belfast_industry_partial_valid`.

The actions call the admission contracts. AI safety uses the same physical contracts plus post-charge floors and collision/emergency exclusions. Mission availability and `slopx_ireland_evaluate_mission_objectives` use the full contract before the partial contract. Map-objective aliases use those same live contracts.

## Pair-by-pair implementation

### Dublin-to-Cork rail

`slopx_ireland_action_repair_a_named_rail_corridor` now requires full control and infrastructure in states `113` and `135`, five Trains, more than 250 manpower, more than 200 Fuel, one available civilian factory, and the existing Provision/route/category/mission/cost gates. It charges 200 Fuel beside the existing five Trains and 250 manpower, reserves one civilian factory for 180 days, and never grants a route connection or railway level by itself.

`slopx_ireland_mission_restore_the_dublin_to_cork_corridor` records full only with the live action and mission, full endpoint control, a 113-to-135 railway connection, level 1 at both endpoints, and Transport Serviceability at least 50. Partial requires both endpoints, Transport Serviceability at least 35, and either the connection or both endpoint levels. Cancellation returns no more than three Trains, 175 manpower, and 140 Fuel through the existing duplicate-refund guard.

### Essential cargo

`slopx_ireland_action_reroute_an_essential_cargo` now uses state `135` as the receiving port and requires its industrial complex, full control, a live Irish/chartered/foreign/neutral merchant route, the 135-to-113 railway, five Convoys, two Trains, 200 Fuel, and the dynamic naval-base tier. Level 1 is required with neither `Patrol the Neutral Approaches` nor `Replace a Lost Merchant Vessel` active; level 2 with one active; and level 3 with both active. No global port-capacity variable is introduced.

Full mission success requires the live action/mission provenance, the capacity contract, and Maritime Access at least 50. Partial requires the active provenance, state-135 port, Maritime Access at least 35, and either a valid merchant route or the railway. Cancellation clears the charter and neutral-procurement origin flags through the existing lifecycle and returns at most three Convoys, one Train, and 140 Fuel.

### Command district exercise

`slopx_ireland_action_run_a_command_district_exercise` now requires full control of state `113`, an arms factory and infrastructure there, at least one division there, Supply Readiness at least 20, 50 Infantry Equipment, 250 Fuel, and its existing readiness/route/category/mission/cost gates. AI launch is suppressed during war, invasion danger, an active coercive Northern campaign, the declared-war/home-defence overlay, or a national emergency, and requires two divisions plus post-charge equipment and fuel floors.

Full success requires two divisions, Command at least 50, and Supply at least 35. Partial success requires one division, Command at least 35, and Supply at least 20. No division is spawned, deleted, moved, renamed, or mutated. Cancellation retains the existing capped return of 35 Infantry Equipment and 175 Fuel.

### Belfast industrial contracts

`slopx_ireland_action_restore_belfast_industrial_contracts` now requires full control of state `119`, an industrial complex and infrastructure there, Northern Labour Cooperation at least 30, two available civilian factories, 100 Support Equipment, 50 Trucks, 250 Fuel, and the existing occupation/integration/route/category/mission/cost gates. It reserves two civilian factories for 300 days through `civilian_factory_use = 2`; factory capacity is released rather than refunded.

Full success requires Labour Cooperation at least 45 and Industrial Capacity at least 55. Partial success requires Labour Cooperation at least 30 and Industrial Capacity at least 40. AI is suppressed for queue collision, contested/invalid endpoint proof, low labour, or a post-charge material-floor breach. Cancellation returns at most 70 Support Equipment, 35 Trucks, and 175 Fuel and clears the owned flags and reservation through the existing cleanup path.

## Documentation and validation evidence

The canonical decision/mission map, `docs/slopx_ireland_systems.md`, `docs/slopx_dynamic_effects.md`, project status, source-of-truth map, and all eight player-facing action/map-objective localisation keys were synchronized in this tranche. Shared numeric tuning lives in `common/script_constants/slopx_ireland_constants.txt`; the rail Fuel charge remains a decision-file macro because the stockpile field uses that documented macro form.

Static evidence to run after the final diff review: action count `140`, mission count `54`, twelve helper identifiers present, full-before-partial ordering for all four runtime pairs, no state-134 admission reference in the essential-cargo pair, the rail cancellation macro present, and the Belfast reservation count updated from eight projects/thirteen reservations to nine projects/fifteen reservations.

No live HOI4 launch was performed, per the task direction. Live parser/reference checks, fresh-1936 action admission, mission ticking, full/partial/failure/escalation, cancellation/refund, route cleanup, AI selection, and GUI/achievement scenario validation remain open. The separate historic-site local-support and patrol-craft objective findings in `decision_requirement_risk_audit_2026-07-26_sidecar_01.md` are not silently folded into this tranche.
