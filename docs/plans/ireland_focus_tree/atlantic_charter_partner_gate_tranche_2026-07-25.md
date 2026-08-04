# Atlantic consultation charter partner gate tranche — 2026-07-25

Feature slug: `ireland_focus_tree`  
Namespace: `ireland`

## Canonical requirement

The regional/external decision map defines `Draft an Atlantic Consultation Charter` as a political action requiring two or more willing states and adequate diplomacy. A regional route flag and a maritime value are not substitutes for participating states.

## Implementation

The action now consumes `ireland_atlantic_charter_partners_valid`. The trigger enumerates every valid pair among the five state-level channel families used by the Ireland package:

- British and American;
- British and German;
- British and Vatican;
- British and neutral states;
- American and German;
- American and Vatican;
- American and neutral states;
- German and Vatican;
- German and neutral states; or
- Vatican and neutral states.

British, American, German, and Vatican pairs also require the named country to exist and not be capitulated. Neutral states require the separate neutral forum channel. The gate is deliberately explicit instead of reading the foreign-reaction actor counter, which is rebuilt for a reaction window and is not a durable diplomatic-capacity measure.

The action retains its Dublin map, route, Maritime Access, category, and dynamic cost gates. Completion remains a consultation charter only; it creates no faction entry, alignment, recognition, territory, core, industry, equipment, unit, fuel, shipping, administration, office, or free-supply result.

## Evidence

- Trigger: `common/scripted_triggers/ireland_triggers.txt`
- Action admission: `common/decisions/ireland_decisions.txt`
- Player-facing requirements: `localisation/english/ireland_l_english.yml`
- Reusable-helper contract: `docs/ireland_dynamic_effects.md`
- Canonical row: `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`

## Remaining proof

Static script and localisation checks are required after the edit. A live scenario still needs to prove one-channel rejection, two-channel admission, sponsor-capitulation invalidation, foreign reaction, and route cleanup.
