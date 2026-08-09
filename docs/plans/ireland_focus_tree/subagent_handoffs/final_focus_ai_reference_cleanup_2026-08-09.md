# Focus AI reference cleanup handoff

Date: 2026-08-09

Feature: `ireland_focus_tree`
Scope: bounded AI focus-selection cleanup for the 150-focus consolidation

## Changed file and identifiers

- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`
- Removed absorbed queue entries `ireland_plebiscite_campaign` and
  `ireland_plebiscite_mandate` from `IRE_ireland_historical`.
- Retired the obsolete `IRE_ireland_route_convergence` plan, whose three
  ordered/factor references no longer exist as focus blocks after the
  consolidation: `ireland_fivefold_obligation`,
  `ireland_otherworld_convergence`, and
  `ireland_convergence_order_capstone`.

## Route behavior before and after

Before, the historical AI queue attempted to select two deleted plebiscite
focuses between `ireland_constitutional_draft` and
`ireland_election_mandate`. The convergence plan also became eligible from
convergence flags and then pointed at three deleted focus IDs.

After, the historical queue proceeds directly from
`ireland_constitutional_draft` to `ireland_election_mandate`. The absorbed
plebiscite state is still written by the constitutional-draft survivor. The
stale convergence plan is no longer registered. The parent focus owner is
retaining the convergence runtime/profile compatibility through
`ireland_high_king_capstone`.

## Validation

- Parsed the 150 authored focus blocks and the AI plan source with a bounded
  read-only parser.
- Confirmed all ordered and factor focus references resolve to current focus
  IDs. Result: zero unknown references.
- Confirmed the retired convergence plan is absent and the plan registry now
  contains 30 `IRE_ireland_*` plans.
- MCP `hoi4.focus_inspect` on the current source returned 150 focuses and
  no focus-reference diagnostics. Layout warnings are recorded separately in
  the parent audit because this patch does not own coordinates.

## Skipped meaningful validation

- No live AI campaign or fresh-save scenario was run. The workspace is not
  being launched by this subagent.
- No focus layout rewrite was attempted because the parent is actively
  normalizing coordinates and explicitly reserved layout edits.

## Remaining risks and parent follow-up

- The parent must finish the compatibility flags on
  `ireland_high_king_capstone` so runtime/profile/achievement consumers of the
  absorbed convergence IDs remain reachable.
- MCP currently reports connector crossings, through-node intersections, and
  linear detours in the authored layout. Those are intentionally handed back
  to the parent layout pass.
