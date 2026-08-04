# Material Focus Rewards

## Purpose

Every Ireland focus must produce an immediate, visible gameplay consequence in
addition to route flags, decision unlocks, proof records, or ledger updates.
Focuses with bespoke rewards keep them. Other focuses call one of eleven shared
profiles chosen by branch purpose.

## Profiles

- Institutional: political power and stability.
- Economic: political power, support equipment, and railway equipment from
  procurement capacity.
- Military: Army experience, command power, and infantry equipment.
- Maritime: naval experience and convoys.
- Air: air experience and command power.
- Technical: political power and one 25% industry research bonus.
- Diplomatic: political power, stability, and convoys supporting neutral trade.
- Cultural: political power and stability.
- Radical: war support, Army experience, and infantry equipment.
- Recovery: political power, stability, and returned manpower.
- Capstone: political power, stability, command power, all-service experience,
  and support equipment.

Balance values are centralized in
`common/script_constants/ireland_focus_reward_constants.txt`. Implementations
live in `common/scripted_effects/ireland_focus_rewards.txt`.

## Visual assets

The reward profiles use vanilla political power, stability, war support,
experience, command power, manpower, research, convoy, and equipment texticons.
They require no custom sprite or texture reference.

## Future extension

If a focus later gains a bespoke building, unit, idea, event reward, or unique
research package, remove its standard profile call after confirming the bespoke
reward remains immediate and visible.
