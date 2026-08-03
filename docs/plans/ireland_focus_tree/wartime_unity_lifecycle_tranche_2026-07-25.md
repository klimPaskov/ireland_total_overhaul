# Wartime Unity Lifecycle Tranche — 2026-07-25

## Scope

This tranche closes the H14 wartime-unity preparation lifecycle without changing the Northern ownership boundary. It follows the canonical 1940 wartime bargain in `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_4_statecraft_and_war.md`, the decision/event lifecycle rows in Part 5, and the Northern diplomacy map.

## Runtime contract

`Prepare a Wartime Unity Bargain` is now a one-shot action. Its existing Readiness, consent, British-channel, command, equipment, truck, map, category, Political Power, and Command Power gates remain in force. The action records the dated `slopx_ireland_h14_gateway`; it does not grant Northern control, occupation, settlement, integration, cores, units, or free equipment.

The H14 dispatcher treats that gateway as authoritative. Date checks bound the chain to the June 1940–January 1941 proposal window; a date alone no longer opens the chain. The daily lifecycle helper withdraws an unresolved gateway after the deadline, route closure, or loss of a valid British implementing partner. It records `slopx_ireland_h14_unprepared_delay` or `slopx_ireland_h14_crisis_destroyed`, preserves the preparation history, and clears only the unresolved gateway, active event markers, and focus handoff.

## H14 result ledger

The final cabinet event now records distinct outcomes:

- `slopx_ireland_h14_proposal_rejected`
- `slopx_ireland_h14_defence_cooperation`
- `slopx_ireland_h14_postwar_unity_pledge`
- `slopx_ireland_h14_federal_transition`
- `slopx_ireland_h14_stormont_refusal`
- `slopx_ireland_h14_unprepared_delay`
- `slopx_ireland_h14_unitary_transition`
- `slopx_ireland_h14_crisis_destroyed`

The final result requires the live `slopx_ireland_h14_full_terms_met` trigger for a pledge or constitutional transition: valid British implementation, defence estimates, command audit and structure, Readiness 35, British Flexibility 45, Nationalist Consent 50, and Unionist Consent 20 or enforceable safeguards. Federal and unitary outcomes additionally require their respective prepared route. Defence cooperation deliberately remains a non-unity result.

The Northern wartime-bargain focus now requires a resolved full-unity outcome and consumes its ready handoff when completed. It writes only the route’s durable war-plan record; the separate control, occupation, settlement, integration-stage, and final-core systems remain responsible for any later territorial result.

## Files and localisation

- `common/decisions/slopx_ireland_decisions.txt`
- `common/national_focus/slopx_ireland_focus_tree.txt`
- `common/scripted_triggers/slopx_ireland_triggers.txt`
- `common/scripted_effects/slopx_ireland_runtime.txt`
- `common/on_actions/slopx_ireland_on_actions.txt`
- `events/slopx_ireland_events.txt`
- `localisation/english/slopx_ireland_l_english.yml`

The event localisation names the actual agenda and the eight result classes. No new asset is required; the existing regenerated H14/focus goal icon package remains in the runtime `gfx` path.

## Validation and open work

Static validation covers balanced touched blocks, the authoritative gateway references, the one-shot action guard, the full-terms trigger, outcome-key coverage, and UTF-8 BOM localisation. HOI4 remains intentionally unlaunched. Live event choice, AI selection, deadline, sponsor-collapse, focus availability, foreign reaction, route cleanup, and fresh-save scenarios remain open in the project audit.
