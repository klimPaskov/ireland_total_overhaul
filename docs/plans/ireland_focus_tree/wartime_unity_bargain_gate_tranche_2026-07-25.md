# Wartime Unity Bargain Gate Tranche — 2026-07-25

## Scope

This tranche closes the documented admission gap for `Prepare a Wartime Unity Bargain` in feature slug `ireland_focus_tree`. It does not resolve the full source-clearance or live-engine validation programme.

## Canonical contract

The Part 4 wartime-bargain threshold requires:

- the June 1940 crisis or a comparable war state;
- Unionist Consent at least `20`, or enforceable guarantees preserving local authority and rights;
- Nationalist Consent at least `50`;
- British Flexibility at least `45`;
- National Readiness at least `35`;
- a defined defence scope, command, transition timetable, finance, and ratification method.

The decision-and-mission map also requires the action to define the unity principle, interim bodies, defence contribution, ports, arms, guarantees, and ratification, and to open the multi-actor proposal chain. Acceptance never transfers Northern control, occupation, settlement, integration, or cores.

Canonical references:

- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_4_statecraft_and_war.md:2123-2164`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md:362`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md:343`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_economy_and_defence_routes_map.md:329-335`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_diplomacy_northern_and_late_game_map.md:268-273`

## Runtime implementation

`common/decisions/slopx_ireland_decisions.txt` now requires:

- the 1940 window, `slopx_ireland_invasion_danger`, or an active war;
- the Dublin-to-Belfast Northern operating context and available category capacity;
- completed defence estimates, completed command audit, and the derived ready Irish command structure;
- an open British channel with a valid, non-capitulated GBR partner;
- Readiness `35`, British Flexibility `45`, Nationalist Consent `50`, and Unionist Consent `20` or `slopx_ireland_northern_safeguard_enforceable`;
- the existing 50 Infantry Equipment and 25 Truck stock gates and dynamic PP/CP burden gates.

Completion consumes the authored equipment and truck charges, records the action, sets `slopx_ireland_northern_wartime_bargain_ready` for the separate focus handoff, and sets `slopx_ireland_h14_gateway` for the dated proposal dispatcher. It does not set `slopx_ireland_northern_wartime_bargain_complete`, `slopx_ireland_northern_war_plan`, a control flag, an occupation flag, an integration stage, a core, a subject, equipment replacement, or any Northern state ownership.

The focus route remains a separate decision surface: `slopx_ireland_northern_wartime_bargain` must still be completed before the durable `slopx_ireland_northern_wartime_bargain_complete` and `slopx_ireland_northern_war_plan` flags exist. The H14 event family is dated and multi-node; its explicit gateway is now authoritative and its resolved full-unity result is required before the focus handoff can be consumed. See `docs/plans/ireland_focus_tree/wartime_unity_lifecycle_tranche_2026-07-25.md` for the outcome and cleanup contract.

## Localisation and tuning

The action description and requirements tooltip expose the live Readiness, British Flexibility, Nationalist Consent, and Unionist Consent values, the exact floors, the crisis/war gate, the command and British-channel proofs, the material charges, and the no-control/no-core boundary.

The fixed thresholds are centralized in `common/script_constants/slopx_ireland_constants.txt` under the `northern_wartime_bargain_*` keys. No new passive political-power store or free material reward was added.

## Validation and open work

Static checks covered the touched Clausewitz blocks, localization BOM, constant references, named gate references, and the no-free-territory boundary. HOI4 was not launched, so live decision admission, focus availability, H14 dispatch, AI choice, deadline, foreign reaction, route cleanup, and fresh-save behavior remain open in the project audit.
