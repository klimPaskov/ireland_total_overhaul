# Ireland neutrality incident lifecycle tranche — 2026-07-25

Feature slug: `ireland_focus_tree`

Status: implemented source tranche; live engine and scenario validation remain open.

## Scope

This tranche closes two canonical lifecycle gaps in the Neutrality and Incidents category. The decision layer now distinguishes an active incident from a generic wartime date or unrelated neutrality pressure, and the relevant law must be in force before the state can dispose of the case.

## Implemented behavior

- `Intern a Belligerent Crew` requires both `slopx_ireland_internment_incident_active` and `slopx_ireland_law_internment_active` before it can commit the 250-guard-manpower mission.
- The `Resolve an Aircrew Internment Case` map objective repeats those incident and law gates, in addition to the named Leinster control, air-base, naval-base, and Neutrality Integrity tests.
- `Release or Exchange Internees` is available only for the active internment incident under the active internment law. Completion records the disposition and closes the neutrality incident, preventing repeated releases against a closed case.
- `Answer a Foreign Access Request` is available only for the active access incident under the active foreign-access law. Completion records the response and closes the incident; the access request remains a response decision rather than a generic wartime action.
- Localisation now exposes the incident-specific, law-specific, and closure requirements in the action descriptions and requirement tooltips.

## Cleanup and boundaries

The existing `slopx_ireland_close_neutrality_incident` helper owns source-flag cleanup, severity history, and incident closure. No territory, core, office, equipment, unit, fuel, shipping, recognition, or foreign alignment is granted by these response actions. The existing category-capacity, political-power, command-power, and route-cleanup paths remain in force.

## Evidence

- `common/decisions/slopx_ireland_decisions.txt`
- `common/scripted_triggers/slopx_ireland_triggers.txt`
- `localisation/english/slopx_ireland_l_english.yml`
- `common/scripted_effects/slopx_ireland_effects.txt` (`slopx_ireland_close_neutrality_incident`)

Static checks for this tranche must confirm the 140-action/54-mission inventory, balanced touched script blocks, absence of unsupported comparison operators, and UTF-8 BOM preservation for the localisation file. Live parser, incident response, law-transition, and cleanup scenarios remain not-run because HOI4 is not being launched.

## Remaining work

The overhaul still has the explicit canonical blockers recorded in `docs/plans/ireland_focus_tree/source_of_truth_map.md`: further action-specific leverage, aircraft, ship, tied-unit, local-support, and foreign-channel mappings where the source map requires them; source-clearance decisions; live engine/reference checks; and the required fresh-1936, route, failure/recovery, Northern, hidden-route, AI, and achievement scenarios.
