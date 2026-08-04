# Integrated Maritime Service

## Overview

The naval lane is a compact cross-tree support branch rather than a detached
fleet programme. Naval Staff splits into a patrol/service lane and a
harbour/technical lane. Those lanes merge at the Atlantic Convoy Office, then
join Interoperability at the regional pact capstone.

Short additional links make maritime policy depend on the wider campaign:

- Marine Service reconstruction requires Maritime Protection.
- The Marine Service Reserve requires Emergency Mobilisation.
- Lough Swilly Watch requires the Neutrality Posture.
- The capstone requires Interoperability.

## Reward progression

The visible `ireland_integrated_maritime_service` dynamic modifier accumulates
rewards across the branch. At full completion it provides +8% factory output,
+5% dockyard output, +3% factory-efficiency growth, +3% research speed, -5%
supply consumption, +2% stability, +6% Army defence, +15% convoy escort
efficiency, and +10% repair speed.

Focuses also improve named provision and readiness components. Direct rewards
include a civilian factory and dockyard at Cobh, coastal forts, radar, a naval
base, support equipment, convoys, political and command power, research bonuses,
an intelligence agency, and experience for all three services.

## Runtime structure

- `common/dynamic_modifiers/ireland_maritime_modifiers.txt` owns the visible
  cumulative modifier.
- `common/script_constants/ireland_maritime_constants.txt` owns balance values.
- `common/scripted_effects/ireland_effects.txt` initializes backing variables
  and idempotently adds the modifier.
- `common/national_focus/ireland_focus_tree.txt` owns graph links and rewards.
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` keeps the historical
  AI moving through the integrated branch.

## Visual assets

No new asset is required. The dynamic modifier reuses the registered vanilla
`GFX_idea_generic_coastal_navy` national-spirit sprite from `interface/ideas.gfx`.
The ten focus icons remain project-owned sprites registered in
`interface/ireland_icons.gfx` and stored under
`gfx/interface/goals/ireland/`.

## Future extensions

- A later balance pass could make neutral shipping pressure scale the value of
  convoy protection, provided it remains legible and does not add another daily
  world iteration.
- Named maritime exercises could connect the existing agency and reserve
  formation to limited events without adding a separate UI panel.
