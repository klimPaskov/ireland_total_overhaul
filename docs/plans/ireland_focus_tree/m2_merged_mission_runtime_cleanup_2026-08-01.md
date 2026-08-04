# Ireland M2 merged-mission runtime cleanup

Date: 2026-08-01
Feature: `ireland_focus_tree`
Namespace: `ireland`

## Scope

This tranche closes the runtime follow-through for the approved M2 merge. It
does not add actions or missions and does not change the approved inventory of
13 decision categories, 140 actions, or 54 mission families.

The two merged missions retain distinct mode ledgers:

| Merged mission | Mode flag | Mode result namespace |
| --- | --- | --- |
| Conduct a Free General Election | `ireland_election_mission_by_election_mode` | `ireland_mission_conduct_a_free_general_election_by_election_*` |
| Keep Essential Services Running | `ireland_service_mission_parish_audit_mode` | `ireland_mission_keep_essential_services_running_parish_audit_*` |

The by-election remains the 100-day mode through the existing `-5` timeout
adjustment from the 105-day base mission. The parish audit remains the
120-day mode through the existing `+60` adjustment from the 60-day base
mission.

## Changed runtime surfaces

- `common/scripted_effects/ireland_runtime.txt` now uses the merged
  mode namespaces for cancellation, timeout, full and partial completion,
  escalation, failure history, preemption, partial-marker reset, objective
  evaluation, and route cleanup.
- `common/scripted_effects/ireland_effects.txt` clears the merged mode
  ledgers during route cleanup.
- `common/scripted_effects/ireland_achievement_history.txt` reads the
  merged by-election full-success record.
- `common/scripted_triggers/ireland_triggers.txt` exposes the two
  mode-specific map-objective triggers under merged mission names.
- `common/decisions/ireland_decisions.txt` consumes the merged
  mode-specific objective keys and result flags without changing action or
  mission ownership.
- `localisation/english/ireland_l_english.yml` keeps readable,
  mode-specific requirement text and names the 100-day and 120-day deadlines.

## Static evidence

- No retired `protect_a_by_election` or `audit_parish_service_contracts`
  mission identifiers remain in active `common`, `events`, `localisation`, or
  `interface` runtime surfaces.
- The two new mode trigger keys have matching decision consumers and the two
  mode result namespaces have producers, consumers, reset paths, and cleanup
  paths.
- The source inventory remains 13 categories, 140 actions, and 54 missions;
  the Radical/Underground replacement families remain the only added mission
  families in the approved M2 ruling.
- Live HOI4 testing was not run, per owner direction; this tranche uses static
  source and local-reference checks only.

## Remaining work

This tranche does not clear the separate source-rights review queue, portrait
review rows, or other non-live completion blockers recorded in the Ireland
source-of-truth map.
