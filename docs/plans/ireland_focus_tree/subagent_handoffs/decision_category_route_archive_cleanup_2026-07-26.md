# Decision category route-archive cleanup

Date: 2026-07-26

## Scope

This handoff repairs only category visibility after the existing Ireland route-archive cleanup. It does not alter actions, missions, scripted GUI definitions, localisation, assets, event flow, costs, AI weights, or the canonical 13/140/54 inventory.

## Changed file and identifiers

- `common/decisions/categories/ireland_categories.txt`
  - `ireland_settlement_government`
  - `ireland_elections`
  - `ireland_organised_society`
  - `ireland_cultural_archival`
  - `ireland_radical_underground`
  - `ireland_provision`
  - `ireland_readiness`
  - `ireland_neutrality_incidents`
  - `ireland_foreign`
  - `ireland_northern`
  - `ireland_occupation_integration`
  - `ireland_regional_external`
  - `ireland_postwar`

## Before and after

Before, all 140 Ireland actions hid when `ireland_route_archived` was set, but all thirteen `visible_when_empty = yes` category headers remained visible. This left empty Ireland decision panels after route cleanup.

After, every category uses the same `NOT = { has_country_flag = ireland_route_archived }` gate as its actions. Active route categories remain unchanged. Route archival hides the empty category surface while durable history remains available to script, events, and achievements.

## Why this is bounded

The canonical Part 5 lifecycle defines an archived category as zero active objectives with the header hidden. The repair only aligns the category-level visibility with the already-universal action-level gate.

## Validation

- Static inventory confirmed 13 category wrappers and 140 action-level `ireland_route_archived` visibility gates before the patch.
- After the patch, all 13 category wrappers carry the matching route-archive visibility gate.
- No localisation change was needed because no visible wording or identifier changed.

## Skipped validation

- No HOI4 launch or live GUI scenario was run, per the sidecar-audit scope.
- GUI rendering was not run because this is a predicate-only category visibility repair and the available MCP workspace did not resolve the current repository's decision source.

## Remaining issues

- The broader 140-action material and capacity safeguard audit remains unresolved.
- The Radical and Underground category currently has ten actions and no timed mission family even though the canonical category roster reserves organisational and constituent/seizure mission capacity. This requires a design decision and a broader plan, not a local cleanup patch.
