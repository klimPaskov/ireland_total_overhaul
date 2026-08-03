# Treaty Port and Neutral Approaches Objective Truth Tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

## Scope

This tranche closes the source-level gap between the canonical decision-and-mission map rows and the live Treaty Port and neutral-approaches missions. It does not claim live engine execution, foreign reaction, AI behavior, or cleanup proof.

## Canonical rows preserved

- `Defend A Treaty Port` remains the Cork/Munster operation for Cobh, Berehaven, or Lough Swilly. The objective now requires control of the named Munster state, a receiving industrial complex and naval base, an active port-defence project, a harbour-defence action and mission, a connected Coastwatch/coastwatch-sector/Air Warning network, and command and warning readiness above their operational floors.
- `Patrol The Neutral Approaches` remains the coastal-sector and port operation. The objective now requires the active Marine Patrol action and mission, full control of the Munster port and Leinster naval base, Munster industry, an Irish or named chartered/purchased/renewed/publicly marked shipping route, a warning/rescue service, Neutrality Integrity above the authored approaches floor, and maritime-protection readiness above its operational floor.

## Source changes

- `common/script_constants/slopx_ireland_constants.txt` adds `neutral_approaches_integrity_floor = 25` so the patrol objective does not duplicate a magic threshold.
- `common/scripted_triggers/slopx_ireland_triggers.txt` adds `slopx_ireland_treaty_port_operational_authority` and `slopx_ireland_neutral_approaches_operational_authority`.
- The two named map-objective triggers now require live action and mission records and call the reusable authority proofs. They retain separate state control, building, command, warning, Neutrality Integrity, and maritime-readiness checks.
- `localisation/english/slopx_ireland_l_english.yml` explains the named state, platform, route, warning, action, mission, and dynamic current-value requirements without exposing implementation history.
- `docs/slopx_dynamic_effects.md` records both trigger contracts, their defaults, side effects, and caller usage.

## Boundaries

These triggers do not transfer or core Northern territory, create equipment, ships, fuel, units, crews, rescue capacity, access, or recognition. The existing decision charges and mission deadlines remain authoritative. Existing full/partial/failure/escalation results and route cleanup remain separate and were not collapsed into the map objective.

## Validation evidence

- Static source inspection confirms the two helpers are defined once and each named mission objective calls the intended helper plus its active action/mission flags.
- The new constant is referenced through `constant:slopx_ireland.neutral_approaches_integrity_floor`.
- Localisation remains UTF-8 with BOM and the touched source contains no unsupported `<=` or `>=` operators.
- HOI4 was not launched, so parser behavior, mission ticking, map control/building checks, deadline outcomes, AI selection, foreign reaction, and cleanup scenarios remain not-run.
