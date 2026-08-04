# Failed sponsor termination gate tranche — 2026-07-25

Feature slug: `ireland_focus_tree`  
Namespace: `ireland`

## Canonical requirement

The decision map requires `Terminate a Failed Sponsor Agreement` to follow a sponsor being defeated, inaccessible, defaulting, or violating its terms. The action must close access, settle the exposed arrangement, recover personnel, and create a replacement-supply burden. It must not be a generic foreign-reaction action.

## Source changes

- `common/scripted_triggers/ireland_triggers.txt`
  - Added `ireland_sponsor_agreement_recorded`.
  - Added `ireland_failed_sponsor_agreement_valid`.
  - The composite requires one of the four authored sponsor-agreement action records and concrete evidence from the matching invalidated channel, failed delivery mission, sponsor-collapse history, dependency-failure state, or the named German collapse-refusal record.
- `common/scripted_effects/ireland_runtime.txt`
  - The daily overlay synchronizer now records `ireland_sponsor_dependence_failure` after a sponsor agreement reaches the shared dependency ceiling or the named German sponsor-collapse refusal is recorded. The flag is durable history; the AI overlay remains derived and still clears when its immediate trigger closes.
- `common/decisions/ireland_decisions.txt`
  - Added the composite trigger to the action availability block.
  - On completion, closes only source channels supported by their own agreement/failure evidence, reduces source-specific leverage, applies the bounded Transport/Maritime Provision and Supply/Equipment Readiness shock, records termination history, and opens the existing foreign-reaction window for replacement diplomacy.
- `common/script_constants/ireland_constants.txt`
  - Added centralized termination deltas for source leverage, Provision, and Readiness.
- `localisation/english/ireland_l_english.yml`
  - Rewrote the action description and requirements to expose the agreement-history and failure evidence gates.
  - Added the completion outcome tooltip; no replacement aid or political victory reward is implied.
- `docs/ireland_dynamic_effects.md`
  - Documented both reusable sponsor-admission triggers and their scope, defaults, side effects, and usage.

## Boundary checks

- The action remains H/P foreign-reaction work and retains its existing state-113, category-capacity, exposure, dynamic-cost, and command-power gates.
- British, American, German, and Vatican leverage remain separate. A failed delivery does not close an unrelated live channel.
- Channel invalidation, sponsor collapse, and delivery failure remain durable history; the action only closes the currently open source channel and records termination.
- The completion shock lowers existing ledgers and creates no equipment, units, fuel, shipping, territory, cores, alignment, office, recognition, or free supply.
- No Northern claim, control, occupation, settlement, integration, or core state is touched.

## Validation status

Static trigger/decision/localisation checks are required after this tranche. Offline source inspection can prove the gate and effect wiring, but engine parsing, foreign-reaction timing, partner invalidation, delivery failure, replacement diplomacy, and route cleanup scenarios remain not-run. HOI4 was not launched.
