# Ireland AI registry re-audit — 2026-07-29

Feature slug: `ireland_focus_tree`

This is a non-live source audit. Hearts of Iron IV was not launched, and no
in-game scenario or save was used.

## Durable profiles and overlays

`common/ai_strategy/ireland_ai_strategy.txt` contains exactly 40 unique
top-level strategy blocks:

- 30 durable Ireland profiles;
- 10 temporary overlays, each using the `ireland_overlay_*` registry;
- no duplicate top-level IDs.

Every one of the 40 blocks has an Ireland `allowed` scope, an `enable` gate,
`abort_when_not_enabled = yes`, and at least one authored `ai_strategy` entry.
The profile and overlay registry therefore remains separate from the 31
vanilla-style focus-selection plans in
`common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`.

## Focus-plan references

The focus-plan source contains 31 plan blocks, including the shared historical
and route-reactive plans. Across their `ai_national_focuses` lists there are
216 unique Ireland focus references. The authored national focus source
contains 216 focus blocks (excluding the tree declaration), and all 216 plan
references resolve to an authored focus ID.

The checks cover reference presence only; they do not claim live focus
selection balance, engine loading, or scenario behaviour.

## Remaining gates

This closes the current static AI registry and focus-reference check. Live AI
selection remains outside the user-authorized completion gate, while source
clearance, local engine-reference evidence, the documented achievement-schema
limitation, and the Radical/Underground mission-capacity wording contradiction
remain open.
