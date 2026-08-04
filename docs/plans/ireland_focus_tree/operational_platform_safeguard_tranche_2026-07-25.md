# Ireland operational platform safeguard tranche (2026-07-25)

Feature slug: `ireland_focus_tree`

## Scope

This bounded source tranche closes two action-specific cost-map mismatches in National Readiness and Neutrality and Incidents. It does not alter the 13-category, 140-action, 54-mission inventory.

## Implemented safeguards

- `Organise Marine Patrols` now requires full control of state 135, an industrial complex, and a naval base. The naval base is the named repair and dispatch platform described by the action's port requirement; the action still consumes 3 Convoys, 250 Fuel, 250 manpower, and 10 Naval Experience.
- The patrol convoy gate and completion charge are now paired local macros (`MARINE_CONVOY_GATE` and `MARINE_CONVOY_CHARGE`) instead of a hardcoded threshold/charge pair.
- `Intercept an Airspace Violation` now requires an air base in state 135 in addition to the active airspace incident family, Air Corps authority, Fighter stockpile, and Fuel gates already present. This makes the existing air-base requirement localisation truthful and prevents a paper interception from consuming the response commitment without a named operating field.

## Boundaries

These checks do not grant equipment, fuel, ships, aircraft, units, territory, cores, recognition, alignment, or political-power stores. The committed Fighter, Convoy, Fuel, manpower, and Naval Experience costs remain consumed on successful action launch; existing mission cancellation and route-cleanup helpers retain ownership of recovery and cleanup.

## Evidence and remaining gates

Changed source: `common/decisions/ireland_decisions.txt` and `localisation/english/ireland_l_english.yml`.

Static checks must confirm the named platform gates, paired convoy macro usage, balanced Clausewitz blocks, and localisation BOM. HOI4 was not launched. Live state-building, incident dispatch, mission timeout, foreign-reaction, AI queue, and route-cleanup scenarios remain open, as do the broader source-clearance and action-specific cost-map gates.
