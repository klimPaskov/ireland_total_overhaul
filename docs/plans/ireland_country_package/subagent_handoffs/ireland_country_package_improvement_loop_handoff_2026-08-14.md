# Ireland Country Package Improvement-Loop Handoff

Date: 2026-08-14

Subagent: `hoi4_improvement_loop_planner`

Mode: plan only

## Design problem

The latest implementation tranches closed the largest mechanical gaps, but the country package still has three player-facing discontinuities. The five family commitments are scattered across four rows, Atlantic settlement forces all three policy focuses, and the shared conclusion helper archives failed and blocked outcomes before recovery or a family-specific postwar settlement.

The broad postwar decision system already exists. The recommended work extends its conclusion contract instead of duplicating it.

## Recommendation

Implement P0 from `docs/plans/ireland_country_package/improvement_loop/ireland_country_package_post_tranche_addendum_2026-08-14.md` as the next bounded tranche:

1. reflow the five existing public family commitments into a centered two-row band
2. correct `ireland_atlantic_settlement_concluded` to use an OR prerequisite block
3. separate route evaluation from successful archival
4. add five family settlement actions, five family recovery actions, and five terminal reports
5. keep historical AI non-coercive and make recovery critical for blocked AI

Then implement P1 territorial recovery and P2 payoff cleanup only after P0 is implemented, promoted, or explicitly rejected.

## Research basis

The addendum uses the accepted country-package research on:

- 1946 rural electrification
- the 1948 inter-party government
- the Republic of Ireland Act 1948
- immediate postwar United Nations applications
- Irish Shipping from March 1941
- emergency rollback, demobilisation, housing, migration, welfare, and export policy
- Northern consent, provincial institutions, and British flexibility

Alternate family conclusions are marked as alternate-history extrapolation. No uncertain historical claim was promoted as fact.

## Engine and implementation basis

Consulted sources include the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, focuses, and country creation. Official vanilla documentation was consulted for Script Constants, effects, and triggers. Current vanilla decision and event structures remain the required implementation precedent.

Read-only focus inspection found:

- 218 focuses
- 226 connectors
- no crossings or intersections
- bounds x = -42 to x = 21
- one detour at `ireland_clerical_failure_bridge -> ireland_clerical_guardianship`

## Files written

- `docs/plans/ireland_country_package/improvement_loop/ireland_country_package_post_tranche_addendum_2026-08-14.md`
- `docs/plans/ireland_country_package/subagent_handoffs/ireland_country_package_improvement_loop_handoff_2026-08-14.md`

No gameplay, localisation, interface, or asset file was edited. `thumbnail.png` was not touched. No commit was created.

## Skills applied

- `hoi4-improvement-loop`
- `hoi4-feature-planning`
- `hoi4-focus-trees`
- `hoi4-events`
- `hoi4-decisions-missions`
- `hoi4-feature-assets`
- `hoi4-text-audio-research`
- `hoi4-subagents`

The asset pass concluded that animation and new audio would add clutter, so no animated or audio package is proposed.

## Future implementation surfaces

Primary:

- `common/national_focus/ireland_focus_tree.txt`
- `common/decisions/ireland_decisions.txt`
- `common/decisions/ireland_expansion_decisions.txt`
- `common/scripted_effects/ireland_effects.txt`
- `common/scripted_effects/ireland_runtime.txt`
- `common/scripted_triggers/ireland_triggers.txt`
- `common/script_constants/ireland_constants.txt`
- `common/ai_strategy/ireland_ai_strategy.txt`
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`
- `events/ireland_country_conclusion_events.txt`
- `events/ireland_territorial_diplomacy_events.txt`

Supporting:

- English localisation and scripted localisation files
- `interface/ireland_decision_icons.gfx`
- country-package asset manifest
- the five country-package source specs named in the addendum

## Existing work that must be preserved

- the connected National Question focus chain
- Wales and Cornwall response events and report art
- material enforcement reserve consumption
- O'Duffy late-game AI continuation
- nine industrial contracts with real civilian factory use
- democratic plebiscite outcome gate
- Congress workers-campaign gate
- fascist refusal and counteroffer gate
- producer-estate Belfast Compact gate and `ireland_territorial_reopen_belfast_compact`
- restoration Provincial Assent gate
- per-holding rights, protectorate, reconstruction, and integration logic

## Open questions for parent review

1. The layout contract specifies a centered two-row band and diagnostic limits rather than hardcoding collision-prone x positions. The implementation agent should accept the renderer's collision-free coordinates only if every numerical acceptance condition passes.
2. United Nations admission needs an explicit alternate-order completion flag when the organisation is unavailable. The current postwar action set should be inspected for an existing durable flag before adding one.
3. Full and partial family reports can share one report image per family. Recovery options should use the same family report image, not a generic fallback.

## Prior addendum status

No prior country-package improvement addendum remains unresolved. This is the sole open addendum for the current gap.

## Promotion status

Keep the addendum in `docs/plans` until accepted and implemented. After implementation and audits, promote its accepted contracts into the five `docs/specs/ireland_country_package/` files listed in the addendum and record the disposition in `implementation_matrix.md`.

## Completion position

This is not a closure handoff. P0 remains a real player-visible gap. After P0, P1, and P2 are resolved, the parent should rerun focus, decision, country-package, localisation, and feature-completion audits. A later improvement-loop pass should produce closure only if those audits find no fallback, simplification, missing AI, missing assets, unresolved plan, or shallow conclusion.

## Simplifications and omissions

None. The addendum gives exact future identifiers, file surfaces, lifecycle rules, AI behavior, assets, tuning, and acceptance tests. Items in the scope-stop section are rejected as bloat rather than deferred substitutes.
