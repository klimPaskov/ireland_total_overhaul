# Material Focus Rewards

## Purpose

Ireland focuses use immediate effects sparingly. Route flags, decision
unlocks, proof records, ledger updates, ideas, and bespoke branch effects are
the primary rewards. Shared material profiles are now reserved for 16 named
route-opening milestones and 24 route capstones; ordinary review, service,
military, cultural, and economic nodes do not repeat a generic reward bundle.

## Profiles

- Economic: political power, support equipment, and railway equipment from
  procurement capacity, used only at named route milestones.
- Military: Army experience, command power, and infantry equipment, used only
  at named route milestones.
- Maritime: naval experience and convoys at maritime route milestones.
- Air: air experience and command power at the air-warning milestone.
- Technical: political power and one 15% industry research bonus at evidence
  gates.
- Diplomatic: political power, stability, and convoys at foreign-policy
  milestones.
- Cultural, radical, and recovery profiles remain available to authored
  route milestones only; ordinary branch nodes rely on their flags, ideas,
  decisions, events, and ledgers.
- Capstone: political power, stability, and limited command power. Route
  capstones keep their authored conclusion, idea, and review effects instead
  of receiving an all-service reward bundle.

Material quantities are centralized in
`common/script_constants/ireland_focus_reward_constants.txt`; the technical
profile keeps its engine-native one-use 15% industry bonus in the scripted
effect. Implementations live in `common/scripted_effects/ireland_focus_rewards.txt`.

## Visual assets

The reward profiles use vanilla political power, stability, war support,
experience, command power, manpower, research, convoy, and equipment texticons.
They require no custom sprite or texture reference.

## Future extension

If a focus later gains a bespoke building, unit, idea, event reward, or unique
research package, remove its standard profile call after confirming the bespoke
reward remains immediate and visible.
