# Compact obligation authority tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

Status: source-level implementation complete for this tranche; live mission, unit-placement, cultural-decay, AI, engine-reference, and cleanup scenarios remain not-run.

## Canonical gap closed

The decision map lists `Fulfil a Compact Obligation` as an A-route action whose costs include resources, units, political limits, and cultural capacity. The action previously consumed manpower and Support Equipment and checked Compact Trust, but it could be offered through unrelated regional flags without a named force or live cultural admission.

## Admission and objective behavior

`slopx_ireland_compact_obligation_authority` now requires the balanced Otherworld compact path, the activated Compact Steward, all four authored Otherworld cultural thresholds (`45` Language Service, `75` Archival Record, `60` Regional Participation, and `70` Site Stewardship), and a division already deployed in state `134` or `135`. The action keeps its existing 500-manpower and 20-Support-Equipment commitments, dynamic Political Power/Command Power costs, Compact Trust limit, full-control map objective, five named sites, deadline, partial result, failure/escalation, and cleanup.

The mission map objective rechecks the named division and cultural components. No division is spawned, moved, supplied, or granted by the action, and no political or supernatural outcome grants free units, equipment, manpower, territory, cores, recognition, or offices.

## Evidence

- `common/scripted_triggers/slopx_ireland_triggers.txt` defines the force, cultural-capacity, and combined authority contracts.
- `common/decisions/slopx_ireland_decisions.txt` uses the combined contract for action admission and rechecks force/culture for the five-site map objective.
- `localisation/english/slopx_ireland_l_english.yml` names the route, office, thresholds, states, physical commitments, and capped refund.
- `docs/slopx_dynamic_effects.md` records the trigger scope, no-free-unit boundary, and recheck behavior.
- Source counts remain 140 actions and 54 missions; no HOI4 process was launched.

## Remaining boundary

This tranche does not close source-clearance states, staged achievement visibility, live engine/reference checks, or the 22 required runtime scenario families. Those remain incomplete in the project status and source-of-truth ledgers.
