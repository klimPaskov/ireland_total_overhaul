# Ireland Action Resource and Safeguard Improvement Addendum

Feature slug: `ireland_focus_tree`

Status: implemented at source level; live validation open

Date: 2026-07-26

## Purpose

This addendum defines one small, high-impact reconciliation tranche for four existing Ireland actions whose canonical physical work or continuing mission proof is still shallower than the decision/mission map promises. It does not add actions, missions, events, routes, GUI surfaces, or assets.

The tranche owns only:

1. fuel and endpoint authority for the Dublin-to-Cork rail repair;
2. port and inland-distribution capacity for essential cargo rerouting;
3. continuing tied-force and supply proof for the command-district exercise;
4. labour agreement and civilian-factory capacity for Belfast industrial contracts.

## Prior-addendum reconciliation

No unresolved Ireland improvement addendum duplicates this work.

- `improvement_loop/ireland_focus_tree_improvement_loop_report.md` is the earlier broad review.
- `improvement_loop/ireland_focus_tree_finding_disposition.md` gives every finding a disposition.
- `improvement_loop/ireland_focus_tree_improvement_loop_execution_record.md` records the accepted closure-oriented planning work.
- `project_status.md` and `source_of_truth_map.md` state that a second broad expansion pass is not required.
- `action_material_gate_reconciliation_tranche_2026-07-26.md` and `action_safeguard_admission_tranche_2026-07-26.md` are source-level implementation evidence, not unresolved design addenda.

This file is therefore a new bounded follow-up to a later implementation tranche, not a repeated plan layer. The accepted design is implemented at source level and folded into the canonical decision/mission map; live engine, AI, and scenario validation remain open below.

## Evidence-based gap disposition

| Case family | Current evidence | Disposition in this tranche |
| --- | --- | --- |
| Fuel | Essential cargo, command exercise, Belfast industry, motorisation, patrols, and interception have paired fuel gates and charges. `Repair a Named Rail Corridor` charges trains, manpower, and factory capacity but no fuel, although the canonical work and linked mission name fuel. | Add a dedicated 200-fuel rail gate, charge, and 140-fuel cancellation return. |
| Trains | Rail repair charges 5 Trains; essential cargo charges 2 Trains. | Keep both amounts. Make the route and inland-distribution proof match those commitments. |
| Trucks | Belfast industry already gates and charges 50 Trucks. Other recently repaired truck rows have paired admission checks. | Keep the Belfast amount; do not invent another truck charge. Tie it to a real Belfast labour/capacity project. |
| Convoys | Essential cargo already gates and charges 5 Convoys, but admission checks state 134 while the mission objective checks state 135 and neither proves an operating port-to-inland route. | Standardise this action/mission on the existing state-135 receiving-port objective and add dynamic port-capacity proof. |
| Aircraft | `ireland_action_intercept_an_airspace_violation` has a 5-Fighter/100-fuel commitment, an air base in state 135, incident-family authority, and a forced-landing handoff after the 2026-07-25 tranches. | Do not reopen source design in this tranche. Live incident, aircraft, AI, reaction, and cleanup validation remains open. |
| Ships | Marine patrols have fuel, Navy XP, manpower, Convoys, a naval base, industry, and a named route authority; merchant-vessel purchase has Convoys, manpower, supplier/leverage logic, dockyard capacity, and crew/route mission proof. | Do not replace the authored Convoy vessel proxy or invent ship deletion without a separate engine-reference decision. Live naval validation remains open. |
| Leverage | The 2026-07-26 foreign-channel and neutrality burden tranches attach source-specific leverage or exposure to the named foreign actions they repaired. | Do not add generic leverage to domestic rail, cargo, command, or Belfast work. Multi-channel priority and partner invalidation remain live-validation work. |
| Tied units | Command-exercise admission checks one division in state 113, but its mission result writers and map objective do not recheck any formation or supply. | Add ongoing one-/two-division and supply proof without spawning, deleting, moving, or permanently locking units. |
| Local support | Belfast's mission objective checks Northern Labour Cooperation, but the action can start without the union agreement named by the canonical map. | Add staged labour-cooperation admission, partial, and full thresholds. |
| Factory/capacity | Rail repair already reserves one civilian factory for 150 days. Belfast industry consumes materials for a 300-day project but reserves no civilian factory. Cargo has no port-capacity collision rule. | Keep the rail reservation; reserve two civilian factories for Belfast for 300 days; make cargo capacity depend on the receiving port and concurrent maritime work. |

## Tranche boundary

Implement exactly these action/mission pairs:

| Action ID | Linked mission ID | Primary gap |
| --- | --- | --- |
| `ireland_action_repair_a_named_rail_corridor` | `ireland_mission_restore_the_dublin_to_cork_corridor` | fuel and route-endpoint authority |
| `ireland_action_reroute_an_essential_cargo` | `ireland_mission_keep_an_essential_cargo_route_open` | receiving-port and inland-distribution capacity |
| `ireland_action_run_a_command_district_exercise` | `ireland_mission_prove_the_command_district` | continuing force and supply commitment |
| `ireland_action_restore_belfast_industrial_contracts` | `ireland_mission_reopen_belfast_industry` | labour agreement and two-factory reservation |

Do not change the fixed inventory of 140 actions or 54 missions.

## Shared implementation contract

Each pair should use three reusable, side-effect-free scripted triggers:

- one admission trigger used by the action requirements and AI material/capacity test;
- one full-result trigger used by the runtime result writer and mission availability;
- one partial-result trigger used by the runtime result writer and mission availability.

The full result must be tested before the partial result. No runtime writer should set a full or partial flag from a ledger threshold alone.

Keep the existing dynamic Political Power and Command Power model. The exact current scarcity bands remain authoritative:

| Action | Normal PP/CP | Watch PP/CP | Severe PP/CP |
| --- | --- | --- | --- |
| Rail corridor | 15 / 30 | 20 / 35 | 25 / 40 |
| Essential cargo | 14 / 25 | 19 / 30 | 24 / 35 |
| Command exercise | 15 / 30 | 20 / 35 | 25 / 40 |
| Belfast contracts | 16 / 35 | 21 / 40 | 26 / 45 |

Physical commitments stay fixed and visible because a Train, Convoy, Fighter, or Truck is not an abstract scarcity score. Dynamic behaviour comes from the existing PP/CP bands, post-charge material-safety checks, competing capacity, and full/partial result conditions.

Put shared thresholds and refund values in `common/script_constants/ireland_constants.txt` when the consuming field accepts script constants. Use dedicated file-local macros only for equipment/fuel admission and charge fields that follow the existing decision-file pattern. Do not borrow another action's macro names.

## Action specification 1: Repair a Named Rail Corridor

### Named contracts

- `ireland_rail_corridor_admission_valid`
- `ireland_rail_corridor_full_valid`
- `ireland_rail_corridor_partial_valid`

### Admission

`ireland_rail_corridor_admission_valid` must require:

- original Ireland ownership and all existing route, category-capacity, repeat, and mission-launch gates;
- full control of states 113 and 135, not only ownership of state 113;
- at least one infrastructure level at each endpoint;
- 5 Trains;
- more than 250 available manpower, retaining the existing 250-manpower charge;
- more than 200 fuel;
- at least one civilian factory available for projects;
- no active copy of the linked mission.

Do not require an already-working Dublin-to-Cork railway connection at admission; that would prevent the repair action from repairing a broken connection.

### Cost and duration

- Keep the dynamic PP/CP bands above.
- Keep 5 Trains, 250 manpower, and one civilian factory.
- Add a dedicated 200-fuel charge.
- Keep the one-factory reservation visible with `ireland_factory_commitment_one_tt`.
- Align the action's timed factory work with the linked mission lifecycle. Preferred implementation: 180 days for both the factory reservation and mission. If the parent retains the current 150-day reservation, document that the final 30 days are inspection rather than active construction.

### Full, partial, failure, and cleanup

`ireland_rail_corridor_full_valid` must require:

- the action and mission active flags;
- full control of states 113 and 135;
- a railway connection from state 113 to state 135;
- railway level 1 or higher at both endpoints;
- Transport Serviceability at least 50.

`ireland_rail_corridor_partial_valid` must require:

- the action and mission active flags;
- full control of both endpoints;
- Transport Serviceability at least 35;
- either the complete state-113-to-state-135 connection or rail-level proof at both endpoints.

At timeout, neither trigger being valid is failure. Loss of either endpoint or route-cleanup escalation must remain an escalated failure under the existing mission-result helper.

Cancellation may return at most:

- 3 Trains;
- 175 manpower;
- 140 fuel.

No PP, CP, or consumed work time is refundable. Add fuel to the existing rail refund branch and retain its duplicate-refund guard. Full success, partial success, timeout, cancellation, route cleanup, and decision removal must clear the active/full/partial flags exactly once; the factory reservation must end with the timed decision or route cleanup.

### AI

The AI may launch only when the post-charge material floor remains valid for Trains and fuel and both endpoints are controlled. Apply factor 0 when either endpoint is contested or when another Provision action already reserves the last available civilian factory. Keep the current recovery bonus when Transport Serviceability is below the watch floor.

## Action specification 2: Reroute an Essential Cargo

### Named contracts

- `ireland_essential_cargo_route_capacity_valid`
- `ireland_essential_cargo_full_valid`
- `ireland_essential_cargo_partial_valid`

### Admission

Replace the current state-134 admission proof with the state-135 receiving-port model already used by the mission objective.

`ireland_essential_cargo_route_capacity_valid` must require:

- full control of state 135;
- an industrial complex and naval base in state 135;
- a live Irish, chartered, purchased, renewed, or otherwise canonically valid merchant route;
- a railway connection between states 135 and 113 for inland distribution;
- the existing 5 Convoys, 2 Trains, and 200 fuel;
- normal mission/category capacity.

Port capacity must scale with concurrent work:

- naval-base level 1 is sufficient when neither `ireland_mission_patrol_the_neutral_approaches` nor `ireland_mission_replace_a_lost_merchant_vessel` is active;
- naval-base level 2 is required when one of those missions is active;
- naval-base level 3 is required when both are active.

This is a read-only capacity gate, not a new global port-capacity ledger. It avoids another permanent variable and needs no separate capacity-cleanup flag.

### Cost

- Keep the dynamic 14/25, 19/30, and 24/35 PP/CP bands.
- Keep 5 Convoys, 2 Trains, and 200 fuel.
- Do not add a civilian-factory charge.

### Full, partial, failure, and cleanup

`ireland_essential_cargo_full_valid` must require:

- action and mission provenance;
- the full route-capacity trigger;
- Maritime Access at least 50.

`ireland_essential_cargo_partial_valid` must require:

- action and mission provenance;
- state-135 control and a naval base;
- Maritime Access at least 35;
- at least one surviving delivery leg: a valid merchant route or the state-135-to-state-113 railway connection.

Neither result being valid at timeout is failure. Port loss, loss of both delivery legs, seizure/sinking evidence, or route cleanup feeds the existing escalation result rather than creating a new event.

Retain the existing cancellation ceiling of 3 Convoys, 1 Train, and 140 fuel. Retain and clear the charter-origin and neutral-procurement-origin flags on every terminal path. Success and failure do not refund physical inputs.

### AI

The AI must evaluate the capacity helper before receiving the material-ready bonus. Apply factor 0 when launch would use the last Convoys or fuel below the shared safety floor, when the receiving port is contested, or when concurrent maritime missions exceed the naval-base tier. Prefer this action under a named Food Security, Energy Continuity, or equipment-delivery deficit; do not run it solely because Maritime Access is below 95.

## Action specification 3: Run a Command District Exercise

### Named contracts

- `ireland_command_district_force_commitment_valid`
- `ireland_command_district_exercise_full_valid`
- `ireland_command_district_exercise_partial_valid`

### Admission

`ireland_command_district_force_commitment_valid` must require:

- full control of state 113;
- at least one division in state 113;
- an arms factory and infrastructure in state 113;
- Supply Readiness at least the existing bottleneck threshold of 20;
- the existing 50 Infantry Equipment and 250 fuel;
- normal action/mission/category-capacity gates.

This is a force commitment, not a transfer of ownership. Do not create, delete, move, rename, damage, or permanently lock a division.

### Cost

- Keep the dynamic 15/30, 20/35, and 25/40 PP/CP bands.
- Keep 50 Infantry Equipment and 250 fuel.
- Do not add manpower or factory costs.

### Full, partial, failure, and cleanup

`ireland_command_district_exercise_full_valid` must require:

- action and mission provenance;
- full control, arms-factory, and infrastructure proof in state 113;
- at least two divisions in state 113;
- Command Readiness at least 50;
- Supply Readiness at least 35.

`ireland_command_district_exercise_partial_valid` must require:

- action and mission provenance;
- the state-113 platform;
- at least one division in state 113;
- Command Readiness at least 35;
- Supply Readiness at least 20.

No committed division, loss of state 113, or Supply Readiness below 20 at timeout is failure. An active invasion or command collapse may use the existing escalated result if the general mission escalation helper already recognises it; do not add a parallel incident system.

Retain the existing cancellation ceiling of 35 Infantry Equipment and 175 fuel. Clear only exercise flags and mission state. Unit state remains untouched on every terminal path.

### AI

Player admission remains one division, but AI launch requires two divisions already present in state 113 and a valid post-charge equipment/fuel floor. Apply factor 0 during `ireland_invasion_danger`, an active coercive Northern campaign, or a home-defence queue emergency. This prevents the AI from turning the only field formation into an exercise commitment during an actual crisis.

## Action specification 4: Restore Belfast Industrial Contracts

### Named contracts

- `ireland_belfast_contract_admission_valid`
- `ireland_belfast_industry_full_valid`
- `ireland_belfast_industry_partial_valid`

### Admission

`ireland_belfast_contract_admission_valid` must require:

- full control of state 119, not only any controlled state;
- an industrial complex and infrastructure in state 119;
- Northern Labour Cooperation at least 30;
- at least two civilian factories available for projects;
- the existing 100 Support Equipment, 50 Trucks, and 250 fuel;
- normal route, mission, action, and Occupation/Integration category-capacity gates.

The labour floor represents the union agreement named in the canonical action map. It is not a generic national Social Consent substitute.

### Cost and capacity

- Keep the dynamic 16/35, 21/40, and 26/45 PP/CP bands.
- Keep 100 Support Equipment, 50 Trucks, and 250 fuel.
- Add a two-civilian-factory reservation for the 300-day action/mission period.
- Reuse `ireland_factory_commitment_two_tt`.

This raises the documented named native reservation total from eight projects / thirteen factories to nine projects / fifteen factories. Update every inventory statement that cites the old count.

### Full, partial, failure, and cleanup

`ireland_belfast_industry_full_valid` must require:

- action and mission provenance;
- full control of state 119;
- the industrial-complex and infrastructure platform;
- Northern Labour Cooperation at least the existing `northern_core_labour_floor` of 45;
- Industrial Capacity at least the existing Belfast full threshold of 55.

`ireland_belfast_industry_partial_valid` must require:

- action and mission provenance;
- full control and the same physical platform;
- Northern Labour Cooperation at least 30;
- Industrial Capacity at least the existing Belfast partial threshold of 40.

Failure occurs when neither result is valid at timeout. Loss of state 119, collapse of the physical platform, labour cooperation below 30, or an existing sabotage/capital-flight escalation state must produce failure/escalation through the current result helper.

Retain the existing cancellation ceiling of 70 Support Equipment, 35 Trucks, and 175 fuel. Civilian factories are capacity reservations and are released, not refunded. Route cleanup, timeout, completion, and cancellation must release the reservation and clear action/mission state once. Emergency managers or ownership outcomes already recorded by other systems must not be silently erased.

### AI

The AI must have two spare civilian factories after other project reservations are counted and must retain the post-charge Truck/fuel/support-equipment floor. Apply factor 0 when state 119 is contested, Northern Labour Cooperation is below 30, or the two-factory reservation would collide with a critical reconstruction or veteran-settlement project. Reward the action when Industrial Capacity is below 55 and a Northern integration route actually needs Belfast output.

## Runtime and cleanup order

The parent should implement in this order:

1. add the twelve side-effect-free admission/full/partial triggers;
2. add dedicated rail-fuel and labour/capacity constants or local macros;
3. update the four action admission blocks and cost presentation;
4. update `ireland_evaluate_mission_objectives` so each pair uses its full helper first and partial helper second;
5. make each mission `available` block consume the same helpers instead of reconstructing weaker conditions;
6. add the 140-fuel rail cancellation return and preserve all duplicate-refund guards;
7. verify route cleanup, decision removal, mission cancellation, timeout, full success, and partial success each clear only their owned flags and reservations;
8. update AI gating and utility;
9. synchronize localisation and documentation.

Do not introduce a daily or weekly all-country on action. These conditions belong in the existing Ireland runtime and decision lifecycle.

## Localisation touchpoints

Update the existing requirement and map-objective keys for all four pairs:

- `ireland_action_repair_a_named_rail_corridor_requirements_tt`
- `ireland_map_objective_restore_the_dublin_to_cork_corridor_tt`
- `ireland_action_reroute_an_essential_cargo_requirements_tt`
- `ireland_map_objective_keep_an_essential_cargo_route_open_tt`
- `ireland_action_run_a_command_district_exercise_requirements_tt`
- `ireland_map_objective_prove_the_command_district_tt`
- `ireland_action_restore_belfast_industrial_contracts_requirements_tt`
- `ireland_map_objective_reopen_belfast_industry_tt`

The text must name the physical commitment, endpoint/port/force/labour proof, and cancellation ceiling where the player can act on it. Keep player-facing prose in world terms. Do not mention implementation history, caps, hardcoding, or this addendum.

No new localisation namespace, event text, GUI text, icon, or asset is required.

## Documentation touchpoints

If implemented, update:

- `docs/ireland_systems.md` for the four action contracts and Belfast reservation count;
- `docs/ireland_dynamic_effects.md` for every new reusable trigger/effect contract;
- `docs/plans/ireland_focus_tree/project_status.md` with source-level evidence and unchanged live-validation blockers;
- `docs/plans/ireland_focus_tree/source_of_truth_map.md` with the four-row disposition;
- the material/safeguard audit or a new dated implementation tranche report covering only these four pairs.

The addendum is accepted. Its exact gates, costs, outcomes, and exclusions are merged into `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`; this file remains as the bounded implementation record under `docs/plans/ireland_focus_tree/`.

## Explicit exclusions

This tranche must not:

- add or remove actions, missions, events, focuses, categories, routes, achievements, laws, ideas, GUI surfaces, sprites, portraits, or audio;
- change action or mission IDs;
- redesign the national Provision, Readiness, Occupation/Integration, or regional-order ledgers;
- add a global port-capacity variable;
- spawn, delete, move, rename, or permanently lock divisions, aircraft, or ships;
- replace the existing Convoy vessel proxy without an engine-reference decision;
- add generic Foreign Exposure or leverage to domestic projects;
- reopen the 2026-07-25 airspace-interception or Marine Patrol platform tranches;
- reopen the 2026-07-26 foreign-leverage and channel-burden tranches;
- implement shipping, finance, intelligence, and infrastructure variants of `ireland_action_integrate_a_voluntary_member_contribution`.

The last exclusion is deliberate. The current regional-contribution source defines only a military contribution and has no player-facing contribution-class selector. Adding ship, finance, intelligence, and infrastructure modes would require a separate bounded design decision about selection, member provenance, command, refunds, and AI. Folding that larger system into these four repairs would weaken reviewability.

## Research and precedent basis

The design follows the canonical Ireland package:

- the decision/mission map names fuel and trains for the Dublin-to-Cork corridor, port and inland distribution for essential cargo, deployed supplied units for the command exercise, and labour/power/inputs/transport/management for Belfast industry;
- the Ireland research architecture treats imported fuel, weak transport, merchant shipping, small defence capacity, Belfast industry, and labour relations as strategic constraints rather than generic PP costs;
- the Emergency-era rail, fuel, shipping, command, and Belfast labour connections are used as gameplay structure, not as claims of source-cleared quotation or asset provenance.

Engine/reference precedent consulted:

- the offline Decision Modding, Triggers, Effects, Data Structures, Scopes, AI Modding, and related core wiki pages;
- vanilla `common/decisions/_documentation.md` for decision and mission lifecycle ownership;
- vanilla `common/decisions/CZE.txt` for paired `num_of_civilian_factories_available_for_projects` and `civilian_factory_use`;
- vanilla `common/decisions/PHI.txt` for state-scoped `has_railway_connection` use;
- vanilla script-constant documentation for centralized tuning.

No external source candidate is promoted or cleared by this addendum.

## Acceptance criteria

The parent may mark this addendum implemented only when:

- all four action admissions use the named authoritative admission triggers;
- all four mission result writers and mission completion gates use the same full/partial contracts;
- rail repair gates and charges exactly 200 fuel and cancellation returns no more than 140;
- essential cargo uses state 135 consistently and respects the named port-capacity tiers;
- command exercise requires continuing one-/two-division and supply proof without mutating units;
- Belfast contracts require labour cooperation and reserve two civilian factories for 300 days;
- the existing dynamic PP/CP bands and authored physical inputs remain synchronized with requirement text;
- cancellation, timeout, partial, full, escalation, route cleanup, and removal paths leave no owned active flag, origin flag, duplicate-refund opportunity, or factory reservation behind;
- AI cannot launch any of the four while its post-charge resource floor or capacity proof is invalid;
- localisation and documentation touchpoints are synchronized;
- the action/mission inventory remains 140/54.

## Open validation and parent handoff

This addendum does not establish feature completion.

The parent still owns:

- implementation and review of every affected gameplay/localisation/docs surface;
- offline engine-documentation and vanilla-precedent confirmation for the final syntax;
- live HOI4 action admission, mission ticking, full/partial/failure/escalation, cancellation, AI, and cleanup scenarios;
- source-clearance validation for the wider Ireland package;
- a separate disposition for the unimplemented non-military member-contribution classes;
- final completion audits.

Live HOI4 validation and source-clearance validation remain open. The Ireland overhaul must not be marked complete from this plan or from source-only implementation evidence.
