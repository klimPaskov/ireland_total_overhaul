# Veteran settlement and UN admission authority tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

Status: source-level implementation complete for this tranche; live engine, foreign-reaction, mission, AI, and cleanup scenarios remain not-run.

## Scope

This tranche closes two canonical admission gaps found while reviewing the 140-row action map:

1. `Demobilise and Settle Veterans` must be a real housing, labour, and equipment-recovery programme rather than a manpower-only removal.
2. `Apply for United Nations Membership` must require a recorded external/world-organisation position rather than opening from a date and generic postwar review alone.

## Veteran settlement

`ireland_veteran_settlement_capacity` in `common/scripted_triggers/ireland_triggers.txt` requires:

- Administrative Reach at least the shared political gate minimum (`60`);
- Labour Organisation at least the shared constitutional-route minimum (`35`); and
- one named capacity: Emergency Housing, Reconstruction Portfolio, the Reconstruction Mandate focus handoff, or the O'Duffy veteran-employer base.

The action in `common/decisions/ireland_decisions.txt` additionally requires full-control Dublin, two available civilian factories, more than 99 Infantry Equipment, and more than 999 manpower. Launch commits exactly 100 Infantry Equipment and 1,000 manpower, reserves two civilian factories for 300 days, and starts the existing dated settlement mission. No units, equipment, factories, housing, employment, or political power are created as a political victory reward.

The cancellation path uses the existing one-time capped refund helper. Code `19` now returns at most 70 Infantry Equipment and 700 manpower, with no factory-time or political-cost refund. The constants live in `common/script_constants/ireland_constants.txt`, and the action and refund effects are documented in `docs/ireland_dynamic_effects.md`.

## United Nations admission

`ireland_un_admission_authority` requires the postwar foreign review, a resolved FR11 admission-reaction record or a closed H17 United Nations chain, and Diplomatic Recognition at least 50. Both the decision admission gate and the `Build Support For United Nations Admission` map objective consume this trigger. The mission retains its naval-base, control, Neutrality Integrity, foreign-posture, deadline, full, partial, failure, escalation, and cleanup behavior.

The gate accepts the authored FR11 event 425 resolution or the named H17 closure flags (`followup_un_application_closed`, `followup_un_recognition_and_delay_closed`, or `followup_un_neutral_contribution_closed`). It does not treat a date, generic posture, foreign country tag, or action completion as a world-organisation position. The action and map-objective tooltips expose the recognition and external-position requirements and state that membership does not grant free recognition, territory, cores, alignment, industry, equipment, units, fuel, shipping, offices, or membership.

## Static evidence

- The source still contains exactly 140 action blocks and 54 mission blocks.
- The veteran action has a named equipment gate/charge, manpower charge, two-factory native reservation, 300-day removal timer, and one-time cancellation refund branch.
- The UN authority trigger is referenced by both the action and its map objective.
- Localisation keys exist for the veteran material commitment, veteran requirements, UN requirements, and UN map objective.
- No HOI4 process was launched and no live scenario is being presented as passed.

## Remaining boundary

This tranche does not close the remaining canonical 140-row material/safeguard mapping, source-clearance states, staged achievement visibility, live engine/reference checks, or the 22 required scenario families. Those remain explicitly incomplete in the project status and source-of-truth ledgers.
