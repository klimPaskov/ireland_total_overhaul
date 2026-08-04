# Member contribution choice tranche — 2026-07-28

## Canonical gap addressed

The decision and mission map requires `Integrate a Voluntary Member Contribution` to accept troops, ships, finance, intelligence, or infrastructure under agreed command, and requires `Meet the Member Contribution Schedule` to deliver one of those classes within 180 days with full, partial, failure, escalation, and cleanup outcomes. The prior implementation charged Support Equipment unconditionally, so it did not implement the mapped choice.

## Source changes

- Added shared member-contribution charges, class floors, and cancellation recovery values to `common/script_constants/ireland_constants.txt`.
- Added class admission, action-cost reserve, class result, and map-objective triggers to `common/scripted_triggers/ireland_triggers.txt`.
- Added five payload effects, class history, ephemeral cleanup, and class-specific cancellation refunds to `common/scripted_effects/ireland_effects.txt`.
- Replaced the hard-coded Support Equipment charge in `common/decisions/ireland_decisions.txt` with event 431 selection and class cleanup in every terminal mission path.
- Replaced generic mission evaluation thresholds in `common/scripted_effects/ireland_runtime.txt` with class-specific full/partial triggers.
- Added the player/AI selection event to `events/ireland_member_contribution_events.txt` and its complete localisation to `localisation/english/ireland_l_english.yml`.

## Static evidence

- Decision inventory remains 140 actions and 54 missions.
- New event payloads have five distinct scripted effects and five distinct option triggers; no option grants units, territory, cores, equipment, fuel, supply, administration, alignment, offices, or recognition.
- The action's maximum command-power path remains 50 (30 base, up to 10 scarcity surcharge, and up to 10 intelligence payload), below the canonical 60 ceiling.
- Touched Clausewitz files have balanced braces; new trigger/effect identifiers and all new localisation keys resolve locally; the localisation file retains UTF-8 BOM.
- The event MCP inspect/render pass remains unavailable because the configured transport closed; no HOI4 runtime was launched per the task instruction. Live event choice, mission timer, AI option weighting, and refund scenarios remain engine-validation work.
