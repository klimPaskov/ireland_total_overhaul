# Focus tree and scripted GUI cleanup — 2026-08-04

## Scope

- Rebuild the Ireland focus-tree presentation into one connected progression.
- Remove route-entry exclusion cliques and overlong prerequisite lines.
- Replace the three oversized decision-category interfaces with compact, staged panels.
- Make custom action costs readable and verify advisor, idea, BoP, category, and report-event assets.

## Implemented

- Connected all 226 focuses through prerequisites already represented by their availability or by an adjacent progression gateway.
- Preserved the historical route lock while treating High Kingship, Five Provinces, and Otherworld content as late optional overlays.
- Added missing local ancestry for the corporate, IRA, cultural, readiness, naval, neutrality, Northern, recovery, and convergence sections.
- Reduced the tree to a 57 by 57 coordinate footprint with 250 connectors and no crossings, node intersections, overlong connectors, coordinate conflicts, or spacing violations in the HOI4 MCP inspection.
- Rebuilt National Conditions, Northern Settlement, and Concealed Evidence as 510-pixel decision-category panels with staged visibility, selectable rows, explanatory detail text, and explicit working review actions.
- Hid the evidence inspection action until evidence is revealed and a row is selected.
- Replaced long action-cost prose with compact `£pol_power` and `£command_power` texticon labels, retained named-ledger values, and shortened the repeated scarcity explanation.
- Added value scales and warning bands to the conditions panel and a five-stage scale to the Northern panel.
- Restored the Chaos Redux advisor conversion script and template under `assets/ireland_focus_tree/advisor_workflow/`.

## Validation

- HOI4 MCP focus inspection: 226 focuses, one connected component, 250 connectors, 0 crossings, 0 node intersections, 0 long connectors, maximum Manhattan span 10, and 0 mod-local diagnostics.
- HOI4 MCP GUI inspection: source graph linked; no visible-overlap diagnostics for any of the three windows. Dynamic-text size warnings are offline-renderer limitations for `context_aware_text`.
- Static checks: balanced Clausewitz braces, no duplicate English localisation keys, UTF-8 BOM retained, no empty directories, no legacy-prefix or mojibake references.
- GUI entries use separate click-region, inset label, and right-aligned value layers so text respects the row ornaments and action-button endcaps.
- Historical AI bypasses (rather than pursues) the alternate emergency route, the recovery/repeal cycle is broken, and succession bridge routes no longer reject their committed source route.
- Asset audit: every mod-owned referenced focus, idea, advisor, BoP, decision-category, decision, and report-event sprite resolves to an existing texture.
- Latest `logs/error.log`: zero bytes at the final audit.

## External diagnostics

The focus renderer still reports fourteen missing continuous-focus sprites from Paradox's base-game `common/continuous_focus/generic.txt`. None are referenced by this mod and no mod-local focus diagnostic remains.
