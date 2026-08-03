# Commonwealth Status Gate Tranche

Feature: `ireland_focus_tree`  
Namespace: `slopx`  
Date: 2026-07-25

## Closed source gap

The canonical Part 5 decision map defines `Review Commonwealth Relations` as a postwar legal action available after a republic or constitutional status change. The previous decision source checked only the postwar window, Dublin ownership, British leverage, partner validity, and dynamic costs. A calendar date could therefore expose a Commonwealth review before any constitutional or republican status had actually been recorded.

## Implementation

`common/decisions/slopx_ireland_decisions.txt` now requires one of the following recorded transitions:

- the standard postwar republic-status event closed;
- the standard postwar Commonwealth-choice event closed;
- a full `Bring the Republic Settlement into Force` mission result;
- a partial `Bring the Republic Settlement into Force` mission result.

The gate is placed only inside `slopx_ireland_action_review_commonwealth_relations`. It does not grant recognition, territory, Northern control, cores, industry, equipment, units, shipping, fuel, administration, offices, alignment, or passive Political Power. The action still records its own British-Leverage and Command-Power consequences.

The requirement tooltip names the status-transition prerequisite so a locked action is readable in the decision surface.

## Lifecycle and cleanup

The gate consumes no persistent material and creates no new persistent flag. Existing event and mission result flags remain the authoritative records and are cleared by their existing route cleanup paths. This keeps the Commonwealth review separate from the Republic Settlement mission and from Northern claims, control, occupation, settlement, integration, and core review.

## Validation boundary

Static source checks are required for the decision brace balance, exact gate placement, localisation BOM, and unique occurrence of each status-result flag. Live engine/reference inspection, event timing, decision rendering, AI selection, and cleanup scenarios remain not-run because the offline HOI4 MCP transport is closed and HOI4 is not being launched.
