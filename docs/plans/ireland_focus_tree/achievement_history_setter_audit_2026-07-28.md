# Ireland achievement history setter audit — 2026-07-28

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`  
Status: structural audit complete; engine and scenario validation remain open.

## Scope

This audit checks the durable history contract between
`common/achievements/slopx_ireland_achievements.txt` and the Ireland scripted
source. It deliberately does not change achievement conditions or invent an
unsupported staged-visibility key.

## Results

- The achievement source contains exactly 32 definitions.
- The 32 `happened` blocks reference 197 distinct Ireland country flags. Every
  referenced flag has a corresponding `set_country_flag` writer in the
  Ireland `common/` or `events/` source tree.
- The achievement conditions reference 37 distinct Ireland variables. Every
  referenced variable has a corresponding variable writer in the Ireland
  `common/` or `events/` source tree, including the `var = ...` form used by
  the scripted-variable effects.
- The three apparent unresolved names from a naive reference scan —
  `slopx_ireland_achievement_coastwatch_days`,
  `slopx_ireland_achievement_league_members`, and
  `slopx_ireland_achievement_mission_floor` — are file-local `@` constants,
  not gameplay flags or variables.
- `slopx_ireland_update_achievement_trackers` runs from the scoped
  `on_daily_IRE` and `on_monthly_IRE` hooks and calls
  `slopx_ireland_update_achievement_history`; the history writer therefore
  remains attached to the Ireland runtime rather than a world-wide on-action.

## Boundary that remains open

The offline Achievement Modding reference documents static `possible` gating,
`happened`, and optional `ribbon`/icon data, but does not document a dynamic
`visible` trigger. The concealed A-22, A-27, A-28, and A-29–A-32 presentation
requirement therefore remains an engine-reference/validation blocker. This
audit does not add `visible = { ... }` or convert staged concealment into a
static claim of completion.

All 32 positive, negative, disqualifier, route-shortcut, partial-result,
cancellation, and restored-government achievement scenarios remain unrun
because HOI4 was not launched.

