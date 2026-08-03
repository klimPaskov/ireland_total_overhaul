# Coercive Northern Campaign gate tranche — 2026-07-25

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`

## Scope

This tranche closes the canonical gate for `Plan a Coercive Northern Campaign`. It does not award Northern control, occupation, settlement, integration, or cores. The action only commits the operation's launch materials and activates `Take and Hold Belfast`; that mission must still satisfy its named Belfast map objective.

## Canonical gate

The decision now requires all of the following before it can be taken:

- route-valid command legitimacy from a revolutionary or militarist route;
- separate border or corridor support proof;
- a valid cause: the Northern war plan, the wartime bargain, a failed settlement requiring recovery, or an active/wider war;
- National Readiness at least 60;
- Supply and Mobility at least 45, read from the existing `slopx_ireland_supply_mobility` alias synchronized from the Readiness supply component;
- National Provision at least 55;
- an available critical mission slot and a staged division in the Southern operational districts `{ 113 134 135 }`;
- the existing equipment, manpower, train, fuel, political-power, command-power, security, and scarcity checks.

Belfast is deliberately not required to be controlled before launch. The `Take and Hold Belfast` mission owns that control proof through `slopx_ireland_map_objective_take_and_hold_belfast_met`, which requires full control of state 119 plus its naval base and arms factory. This preserves the separation between claim, control, occupation, settlement, integration, and core review.

## Script surfaces

Constants in `common/script_constants/slopx_ireland_constants.txt` centralize the three numeric floors:

- `northern_campaign_readiness_floor = 60`
- `northern_campaign_mobility_floor = 45`
- `northern_campaign_provision_floor = 55`

Reusable triggers in `common/scripted_triggers/slopx_ireland_triggers.txt` are deliberately split so later audits can identify which proof is missing:

- `slopx_ireland_coercive_northern_route_legitimacy` checks IRA, Republican Congress, O'Duffy, Ailtirí, and Dillon command-route evidence;
- `slopx_ireland_coercive_northern_border_support` checks Northern command contact, local authorities, corridor work, wartime bargaining, or the later stage review;
- `slopx_ireland_coercive_northern_military_cause` checks the recorded Northern war plan, Northern wartime bargain, a produced settlement-failure signal, or an active war;
- `slopx_ireland_coercive_northern_campaign_cause_valid` requires all three proof classes.

The decision in `common/decisions/slopx_ireland_decisions.txt` consumes the combined cause trigger, the three centralized resource floors, and Southern staging districts. Its existing material charge remains concrete and bounded; its cancellation refund path and mission cleanup remain unchanged.

Localisation in `localisation/english/slopx_ireland_l_english.yml` exposes the live Readiness, Mobility, and Provision values and explains that Belfast control is earned by the linked mission rather than granted by the political action.

## Validation evidence

- Static reference checks confirm every new trigger and constant is referenced by the decision or by another new trigger.
- The Belfast objective remains the only source of the full-control/naval-base/arms-factory proof for the mission.
- No focus, decision, or effect in this tranche adds Northern territory, a core, equipment, fuel, shipping, units, or recognition as a political reward.
- HOI4 was not launched, per the task instruction; live engine loading, map-objective execution, and scenario playthrough remain part of the final audit programme.

## Follow-up

The full completion audit still needs to exercise the blocked, launch, cancellation, partial-success, full-success, escalation, and cleanup branches with the threshold values above. Any future expansion of the cause model must add a real producer and cleanup path for new crisis flags rather than relying on an unconnected condition.
