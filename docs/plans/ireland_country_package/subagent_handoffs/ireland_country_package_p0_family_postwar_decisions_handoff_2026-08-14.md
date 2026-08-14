# P0 Family Postwar Decisions — Handoff

Disposition: implementation handoff retained for the ten action contracts.
Its initial terminal-event, evaluator, and AI-runtime concerns were resolved by
the parent integration closure and `1984ff0`; the old issue list below is
historical evidence, not an open work queue. The remaining package-level gate
is parent-owned completion audit/live evidence. The separate family-lane layout
is accepted at `89ff719` and recorded in
`ireland_country_package_family_lane_reflow_completion_2026-08-14.md`.

Date: 2026-08-14

Owner: `hoi4_decision_mission_auditor`

Scope: `ireland_postwar` decisions and English localisation only.

## Changed files

- `common/decisions/ireland_decisions.txt`
- `localisation/english/ireland_l_english.yml`
- `docs/plans/ireland_country_package/subagent_handoffs/ireland_country_package_p0_family_postwar_decisions_handoff_2026-08-14.md`

## Verified concurrent interfaces

- The four shared P0 constants now exist in
  `common/script_constants/ireland_constants.txt` and match every decision
  reference.
- `ireland_postwar_foundation_ready` and
  `ireland_family_postwar_settlement_complete` now exist in
  `common/scripted_triggers/ireland_triggers.txt`.
- The shared conclusion layer now supplies
  `ireland_begin_conclusion_review`,
  `ireland_open_family_conclusion_recovery`, and
  `ireland_archive_successful_route` in
  `common/scripted_effects/ireland_effects.txt`.
- All ten final DDS files and their exact future sprite IDs are registered in
  `interface/ireland_icons.gfx`. These are concurrent asset/wiring changes,
  not edits from this decision-surface task.

## Implemented decision ids

### One-time family settlements

- `ireland_action_ratify_the_postwar_republic`
- `ireland_action_civilianise_the_workers_congress`
- `ireland_action_place_the_directorate_under_statute`
- `ireland_action_convert_contracts_to_reconstruction_credit`
- `ireland_action_define_the_postwar_crown`

Each is gated to `IRE`, its active political family, its specified capstone set,
and `ireland_postwar_foundation_ready`. It runs for
`constant:ireland.postwar_family_settlement_days`, reserves
`constant:ireland.postwar_family_factory_use` civilian factories, is one-time,
records `ireland_family_postwar_settlement_complete`, records its family outcome,
and starts or refreshes the conclusion review.

### Repeatable family recoveries

- `ireland_action_reconstitute_the_postwar_coalition`
- `ireland_action_reconvene_the_workers_congress`
- `ireland_action_demobilise_the_failed_directorate`
- `ireland_action_rebalance_the_producer_estates`
- `ireland_action_reconvene_the_crown_council`

Each is visible only to `IRE` when `ireland_conclusion_recovery_open` and the
matching family flag are present. It runs for
`constant:ireland.postwar_family_recovery_days`, reserves one shared factory,
sets `ireland_family_conclusion_recovery_complete`, clears recovery-open, and
calls `ireland_begin_conclusion_review`. Recoveries deliberately do **not** use
`fire_only_once`, so a later failed review can reopen the same family action.

The narrow blocked-surface repair mapping is:

| Recovery | Current blockers cleared |
| --- | --- |
| Postwar Coalition | government, law |
| Workers' Congress | government, defence |
| Failed Directorate | defence |
| Producer Estates | economy |
| Crown Council | government, identity |

No recovery resets `ireland_route_failure`, conclusion result history, or any
other broad live-failure condition. The shared evaluator and conclusion-report
work own those cross-system resets and the route-specific event routing.

## Final-review integration

`ireland_action_complete_the_route_conclusion_review` now requires
`ireland_family_postwar_settlement_complete = yes`. This prevents the existing
route-conclusion AI bonus from being reachable before the family settlement and
gives the existing requirement tooltip a clear player-facing explanation.

## Before and after behavior

Before this patch, postwar statecraft could reach the route-conclusion review
without a family-specific institutional settlement. It had no P0 family recovery
surface in the category.

After this patch, a capstone family must finish its foundation-gated 180-day
settlement before the conclusion review is available. A blocked/failure report
can expose exactly one matching 120-day recovery, which records the repair,
removes only its named current blockers, and begins a new review without erasing
failure history. None of the ten actions grants factories, equipment, cores,
manpower, stability, war support, or map claims.

## Decision category lifecycle notes

1. A family capstone plus the shared postwar foundation reveals its settlement.
2. The settlement reserves one civilian factory and records the route's durable
   institutional form.
3. The shared conclusion review can then be completed and delegated to the
   family report/event logic.
4. A blocked or failed family report opens only its matching recovery action.
5. Recovery clears its current family-relevant blockers, preserves history, and
   starts a fresh review. Archive/route-cleanup removes an in-progress project
   without granting its completion record.

## Mission quality notes

No missions were added or changed in this scope. The P0 surface consists of
timed decisions, not timed objectives; there is therefore no new mission owner,
region, success/failure timeout, or duplicate-mission risk. Existing postwar
foundation missions remain the prerequisite proof owned by
`ireland_postwar_foundation_ready`.

## Cost, AI, and route-lock notes

- All ten decisions use the vanilla one-factory reservation pattern:
  `custom_cost_trigger = { num_of_civilian_factories_available_for_projects > 0 }`,
  `custom_cost_text = decision_cost_civ_factory_1`, and the shared factory-use
  constant. They carry no political-power, equipment, or free-reward exchange.
- Settlement AI receives `constant:ireland.ai_critical_score` once the
  foundation trigger is true. Recovery AI receives
  `constant:ireland.ai_recovery_bonus` while recovery is open.
- Family, capstone, `original_tag = IRE`, and route-archive gates prevent invalid
  AI targets or cross-family actions. These actions have no external country or
  state target.
- The parent-owned AI runtime/strategy work still needs to force a blocked AI to
  prefer recovery over optional postwar actions, as assigned by the P0 addendum.

## Localisation and tooltip coverage

Added 32 English keys: ten titles, ten descriptions, ten completion-effect
tooltips, two shared requirement tooltips, and the updated final-review
requirement text. The requirements explain the postwar foundation, factory
reservation, and cancellation on archival or route cleanup. The English file
retains its UTF-8 BOM.

## Issues, severity order

1. **High — terminal report definitions are still absent:**
   `ireland_dispatch_family_conclusion_event` calls
   `ireland_country_conclusion.1` through `.5`, but no matching definition is
   currently present under `events/` (the prescribed
   `events/ireland_country_conclusion_events.txt` does not exist). This event
   tranche must provide the result-specific reports and call
   `ireland_archive_successful_route` only for full/partial options.
2. **High — recovery records are not yet consumed by the evaluator:** each
   recovery records its family-specific repair flag and clears only its current
   blocked surfaces as required. The current evaluator then clears and rebuilds
   blocked surfaces from live source conditions, but does not yet test the five
   repair records. Consequently, a still-unresolved source condition can repeat
   the same blocker after the next 180-day review. The shared evaluator/event
   tranche must map each repair record to a lawful post-recovery state or partial
   result; this task deliberately did not reset broad failure state.
3. **Medium — AI runtime ownership boundary:** decision weights provide the P0
   critical and recovery scores, but the parent-owned AI runtime/strategy work
   must still force a blocked AI to choose recovery ahead of optional postwar
   actions.

## Validation

Ran a task-specific static contract check against the completed decision and
localisation files. It verified all ten exact ids, five settlement durations,
five recovery durations, shared factory reservation, factory availability cost,
family/foundation or family/recovery gates, settlement and recovery completion
flags, review restart calls, repeatable recovery behavior, the final-review
settlement gate, one unique definition per id, matching localisation, and the
absence of factory/equipment/core/manpower/stability/war-support reward effects.
The contract passed.

Also inspected the vanilla 180-day civilian-factory decision precedent in
`common/decisions/GER.txt` and reused its factory-availability/custom-cost
structure.

Cross-file integration was rechecked after the concurrent shared tranche landed:
all four constants, both triggers, the review/recovery/archive helpers, ten DDS
files, and ten `GFX_decision_<action_id>` registrations match this decision
interface. The remaining integration check found that the five dispatched event
IDs have no definition under `events/` yet, and that the evaluator does not yet
consume the five repair-record flags.

Meaningful validation not run: an engine parse/load is deferred until the five
terminal event definitions and post-recovery evaluator mapping exist. No
decision-owned scripted GUI exists on this surface, so no GUI inspection or
render artifact applies.

## Skills used

- `hoi4-decisions-missions`
- `hoi4-events` for direct conclusion-report integration boundaries
- `hoi4-focus-trees` for capstone and family-gate verification
- `hoi4-subagents` for scoped handoff and ownership rules

No simplification was made within the assigned decision/localisation surface.
The outstanding terminal-event and evaluator-mapping dependencies above must be
completed before the P0 tranche can be considered fully integrated.

## Parent integration closure

The parent subsequently added `events/ireland_country_conclusion_events.txt`
with IDs `.1` through `.5`, registered five distinct report images, and integrated
the architect's family repair-record mappings. The final review is repeatable
after a failed cycle, and the alternate-order decision owns the explicit
non-UN postwar path. The two high dependencies recorded during this subtask are
therefore resolved.
