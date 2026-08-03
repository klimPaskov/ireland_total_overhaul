# Ireland historic-site and patrol-craft implementation tranche — 2026-07-26

## Scope

This tranche closes the two medium findings in `decision_requirement_risk_audit_2026-07-26_sidecar_01.md` at source level. It does not claim live engine parsing, gameplay, AI, GUI, or scenario completion.

## Historic-site admission

`slopx_ireland_historic_site_admission_valid` is the shared, side-effect-free admission contract for `slopx_ireland_action_protect_a_historic_site`. It requires:

- a live serious-culture or archive lane and full control of state `135`;
- regional participation through the completed institutional record or the cultural regional floor, plus Social Consent `35`;
- one rights-bearing local constituency at the cultural rights floor, represented by Minority Confidence, Labour Organisation, or Church Institutional Influence;
- 250 manpower, 5 Trucks, and 10 Support Equipment maintenance kits.

The action uses the helper in its visible availability block and calls it again immediately before its direct Cultural Capacity result and completion flag are written. The maintenance requirement is a concrete Support Equipment charge, not a passive political-power store and not the later Site Stewardship result used as a circular prerequisite. AI receives a zero factor when the same admission contract is not valid.

## Patrol-craft commitment

`slopx_ireland_action_organise_marine_patrols` now sets `slopx_ireland_marine_patrol_craft_committed` after charging its 3 Convoys. The flag is the authored representation of one dedicated coastal patrol-craft coverage allocation; it is explicitly not merchant shipping stockpile capacity and does not create a vessel or unit.

`slopx_ireland_map_objective_patrol_the_neutral_approaches_met` now requires `slopx_ireland_marine_patrol_craft_coverage_valid`, in addition to the existing full-control, port, industrial, naval-repair, shipping-authority, warning/rescue, and Maritime Protection checks. The action blocks while the commitment is already live, and AI receives a zero factor in the same collision state.

The commitment is cleared on action removal, mission cancellation, timeout, full success, partial success, route cleanup, and the shared mission-objective cleanup. The mission localisation and canonical map row name the 105-day deadline, craft allocation, crews, fuel, rescue, repair, inspection coverage, failure/escalation, and terminal release.

## Files changed

- `common/scripted_triggers/slopx_ireland_triggers.txt`
- `common/decisions/slopx_ireland_decisions.txt`
- `common/scripted_effects/slopx_ireland_effects.txt`
- `localisation/english/slopx_ireland_l_english.yml`
- `docs/slopx_ireland_systems.md`
- `docs/slopx_dynamic_effects.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`
- `docs/plans/ireland_focus_tree/decision_requirement_risk_audit_2026-07-26_sidecar_01.md`

## Validation boundary

Static validation must confirm that the helper definitions are balanced, the direct action calls the historic-site helper both for admission and result recording, the patrol map objective calls the craft helper, the patrol flag is cleared on every terminal path and route cleanup, the action/mission counts remain `140/54`, and the localisation file retains UTF-8 BOM encoding. Live parsing, mission timing, craft collision, AI queue behavior, and route cleanup remain not-run.
