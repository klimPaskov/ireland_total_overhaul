# Final exceptional decisions and events audit

## Scope and verdict

Audited the 22 exceptional Ireland actions and missions, `ireland_events.438` through `.460`, the associated constants, spirits, cosmetic tags, localisation, AI hooks, lifecycle helpers, and wired art. No unresolved defect remains in this bounded surface after the patches listed below.

The three previously uncalled events were wired during this live audit by the parent implementation: `.438` is called from the accepted `.214` convention route, `.439` from `ireland_household_council`, and `.446` from `ireland_action_negotiate_a_provincial_budget`. Every event in `.438` through `.460` now has at least one caller.

## Issues, sorted by severity

### Resolved

- Eleven timed exceptional missions had `activation` and cleanup effects but no `cancel_trigger`. A route closure or removed due marker could leave a stale mission card running until its timeout. Each now cancels when its route or defining marker is no longer valid, allowing the existing `cancel_effect` cleanup to execute.
- `ireland_action_audit_the_royal_household` could repeat indefinitely after its two required audits, farming legitimacy and Household Reach. Availability now caps it at `party_crown_audits_required`.
- The Fian mission described a material commitment but charged none. It now consumes centralised manpower, infantry equipment, support equipment, and command-power commitments on completion.
- Seven exceptional route values could exceed their documented 0 to 100 bounds. The route refresh helper now clamps them using existing tuning constants.
- Event localisation now uses `.desc` for each event description; `.d` is solely option D. The duplicate description and option-key collision no longer exists.
- The Fian proof now requires a player division in Dublin, Cork, or Donegal at more than 90% strength and more than 80% organisation, with both thresholds held in script constants. Its exact requirements tooltip and material and command-power consumption agree with the trigger.

## Decision category lifecycle

| Category | Active-mission handling | Route and cleanup result |
| --- | --- | --- |
| Settlement government | Royal Circuit and Party Crown mission state | Route close clears launch and active markers; new cancellation trigger removes stale cards. |
| Cultural and archival | Veil, Broken Compact, Reconciliation, Extraction | Capacity is checked before launch; category and mission cleanup run on cancel or completion. |
| Readiness | Fian Company | Material readiness gates completion; route closure cancels and clears readiness state. |
| Regional and external | Common Compact, Fifth Seat, Rival Irelands, Convergence Review | Regional counters and critical state are rebuilt or cleared by route helpers and mission cleanup. |

All 11 missions have an owner of `IRE`, an activation rule, a duration macro, timeout or completion effects, cancellation cleanup, and a category capacity path. The defining active or due marker is cleared by the matching helper, avoiding duplicate mission cards.

## Mission quality notes

| Mission | Category and region | Duration | Requirement | Success and failure | Duplicate risk |
| --- | --- | ---: | --- | --- | --- |
| Royal Circuit | Settlement, royal states | 120 days | Circuit materials and crown route | Circuit completion or timeout resolution | Cleared by route and active-state cleanup |
| Break the Party Crown | Settlement, national | 120 days | Reduced Household Reach and consensus | Route event resolution or timeout | Audit cap prevents resource loop |
| Equip a Fian Company | Readiness, Dublin, Cork, or Donegal | 120 days | Material readiness plus a player division above 90% strength and 80% organisation | Commits material then resolves; timeout cleans readiness | Active marker cleared; proof and tooltip agree |
| Keep the Veil at Five Sites | Cultural, site network | 180 days | Veil obligations and cultural route | Success or deterioration result | Active marker cleared |
| Repair Broken Compact | Cultural, compact sites | 120 days | Broken-obligation conditions | Repair or failure result | Active marker cleared |
| Reconcile Regional Compacts | Cultural, regional partners | 150 days | Compact-count conditions | Reconciliation or failure result | Active marker cleared |
| Extract from a Protected Site | Cultural, protected site | 90 days | Dominion route and reversible extraction state | Extraction result or cancellation | Route-state cancellation added |
| Fund the Common Compact | Regional, Ireland | 120 days | Compact funding state | Funding result or failure | Active marker cleared |
| Keep the Fifth Seat Open | Regional, council | 180 days | Fifth-seat conditions | Seat preserved or lost | Active marker cleared |
| Prevent Rival Irelands | Regional, national | 120 days | Rival prevention state | Prevention result or escalation | Critical marker cleared |
| Survive First Convergence Review | Regional, convergence | 180 days | Convergence review state | Review result or escalation | Critical marker cleared |

## Costs, requirements, AI, and presentation

- Related duration, threshold, cooldown, cost, and clamp values resolve through `common/script_constants/ireland_exceptional_routes.txt`, with decision-file macros used where Clausewitz fields require them.
- Fian completion now charges 500 manpower, 500 infantry equipment, 20 support equipment, and 20 command power, matching its material-commitment framing. It does not create a unit or stockpile reward.
- The household audit requires capture of the crown, fewer than two completed audits, and political power. Its localisation states those player-facing requirements.
- Decision AI weights and route-lock checks remain limited to valid Ireland route state, active route markers, and matching availability checks. No dead country target or open-route bypass was found.
- All 23 events are triggered only, with four options each. Their 92 options retain a historical modifier, route match, ledger-pressure modifier, and effect tooltip.
- The seven exceptional spirits and ten cosmetic tags have their intended localisation coverage. All ten cosmetic flags have normal, medium, and small variants.
- All 22 action or mission sprite identifiers are registered and point to existing 32 by 32 DDS files. All 23 report-picture identifiers are registered and point to existing 210 by 176 DDS files.
- No decision-owned scripted GUI surface was found in this scope, so GUI inspection or rendering was not applicable.

## Changes made

| File | Identifiers | Before and after |
| --- | --- | --- |
| `common/decisions/ireland_decisions.txt` | All 11 `ireland_mission_*` entries in this package | Added cancellation guards based on the route and their defining active or due state so stale missions cancel and run existing cleanup. |
| `common/decisions/ireland_decisions.txt` | `ireland_action_audit_the_royal_household` | Added the two-audit availability cap. |
| `common/decisions/ireland_decisions.txt` | `ireland_mission_equip_a_fian_company` | Completion now consumes the stated Fian material and command commitments. |
| `common/script_constants/ireland_exceptional_routes.txt` | `fian_*_cost` | Added the four centralised Fian commitment constants. |
| `common/scripted_effects/ireland_exceptional_routes.txt` | `ireland_refresh_exceptional_route_state` | Clamps seven route values to their existing 0 to 100 bounds. |
| `localisation/english/ireland_exceptional_routes_l_english.yml` | Fian mission and household audit keys | Clarifies implemented Fian requirements and material commitments, and describes the audit cap. |
| `docs/ireland_exceptional_routes.md` | exceptional route reference | Records audit cap and Fian commitment behavior without promising a spawned unit or stockpile reward. |

## Validation evidence

- Static source audit confirmed exactly 22 exceptional actions or missions and 11 timed missions.
- `ireland_events.438` through `.460` contain 23 events and 92 options. Every event has one title, one `.desc`, option keys through `.d`, four effect tooltip keys, and at least one current caller.
- Constant-reference checks found no missing exceptional route constants in the decisions, triggers, effects, events, or ideas surfaces. Touched script brace checks were balanced.
- Asset audit confirmed all 22 decision or mission icons and all 23 report images are both registered and present at their expected dimensions.
- Read-only MCP focus inspection reported no blocking diagnostics and no missing event references from the Ireland focus source. Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/22936b5a8e0e29bcfba258c457dd81468ebf7625cd6cc68d14697fcc817962e7/3fb7ff228281ecd17ddc08e0257b85de1deb4756226c8e994b0c2b6ddbf1f12c/focus-inspect.e9fbbc8b6e26fae7.json`.
- A direct event MCP inspection tool was not exposed in this agent session. Full in-game scenario validation was not run here.

## Remaining issues and follow-up

None in the audited exceptional decision, mission, and event surface. The accepted Fian proof is one player division in Dublin, Cork, or Donegal above the stated readiness thresholds, rather than coverage in every listed state. No fallback was introduced.
