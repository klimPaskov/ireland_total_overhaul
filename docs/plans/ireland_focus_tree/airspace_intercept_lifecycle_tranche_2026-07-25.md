# Airspace Intercept Lifecycle Tranche (2026-07-25)

Feature slug: `ireland_focus_tree`

## Scope

This tranche corrects the neutrality-family wiring for `Intercept an Airspace Violation` and connects a forced landing to the existing internment mission without turning the interception into free equipment, territory, or alignment.

## Current implementation

- The interception now requires `ireland_airspace_active`, the operational family signal derived from the active airspace incident sources.
- The existing Fighter and Fuel gates remain in force, and completion adds the authored Readiness Intelligence delta and opens the foreign-reaction window.
- Completion records `ireland_airspace_forced_landing_pending`.
- `Intern a Belligerent Crew` and `Resolve an Aircrew Internment Case` accept either the named internment incident or the pending forced-landing record, while retaining the internment law, map, manpower, and mission-capacity gates.
- Cancellation, timeout, full success, partial success, route cleanup, and neutrality-incident cleanup all clear the pending handoff flag.

## Boundary

The handoff is not a core, claim, control, occupation, settlement, integration, equipment, unit, fuel, shipping, or recognition reward. The original Fighter and Fuel commitments remain consumed on successful interception; the existing mission cancellation refund remains limited to its authored manpower recovery.

## Validation boundary

Static trigger, decision, effect, constant, and localisation checks are required after this tranche. HOI4 was not launched; live incident-source selection, forced-landing handoff, foreign reactions, mission timeout, and cleanup scenarios remain not-run.
