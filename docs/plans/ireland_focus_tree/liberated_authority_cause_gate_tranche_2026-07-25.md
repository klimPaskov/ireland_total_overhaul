# Liberated authority cause gate tranche

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`  
Date: 2026-07-25

## Purpose

The Regional Orders and External Ambitions row for `Recognise a Liberated Authority` requires war or collapse to produce a valid political opening. The action previously had a route-family, Dublin map, equipment, convoy, and recognition ceiling but could appear from a regional route alone. This tranche adds the missing cause admission.

## Implementation

`common/scripted_triggers/slopx_ireland_triggers.txt` defines `slopx_ireland_liberated_authority_cause_valid`. It accepts only the authored war/collapse or local-authority records:

- active Irish war;
- war spillover;
- foreign-sponsor collapse or its active recovery overlay;
- the Northern local-authority mandate;
- a Northern wartime bargain.

`common/decisions/slopx_ireland_decisions.txt` consumes the trigger in `slopx_ireland_action_recognise_a_liberated_authority`. Existing route-family, capacity, state-113, diplomatic-recognition, equipment, convoy, political-power, command-power, mission, AI, and cleanup gates remain in force.

The updated localisation names the cause, bounded aid package, and no-free-status rule. The trigger contract is recorded in `docs/slopx_dynamic_effects.md`.

## Invariants

- A route flag or cultural contact alone cannot open recognition.
- The action still spends 50 Infantry Equipment and 5 Convoys; it does not create a puppet, subject, territory, core, industry, unit, or free recognition.
- Recognition remains separate from protectorate treaty authority, Northern control, occupation, settlement, integration, and core review.
- The foreign reaction window and aid/legitimacy missions remain responsible for their own outcomes and cleanup.

## Validation status

The trigger definition and decision consumer need the targeted static source audit rerun after this edit. Live decision, foreign-reaction, mission, and cleanup scenarios remain not-run; HOI4 is intentionally not launched.
