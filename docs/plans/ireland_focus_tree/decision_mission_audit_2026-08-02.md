# Ireland decision and mission audit handoff — 2026-08-02

Scope: Ireland decisions, missions, scripted GUI, lifecycle helpers, AI gates, and localisation. Source clearance, assets, and live HOI4 validation were explicitly out of scope.

## Completed local correction

- `common/scripted_triggers/ireland_triggers.txt`
  - `ireland_map_objective_complete_the_stage_five_integration_review_met`
  - Replaced the impossible literal `northern_integration_stage < 4` condition with `northern_stage_core_eligible` or higher.
  - The Core Eligibility Review is revealed only at stage five. Before this correction, its mission could start but could never become completable through its named map objective, and would time out into the failure path. The correction does not weaken `ireland_can_northern_core_review`, which remains the sole gate for `119 = { add_core_of = ROOT }`.

## Mission and category coverage

All 54 mission definitions are Ireland-owned, use a named map-objective tooltip, have a deadline, and expose cancellation, full success, partial success, failure, escalation, and cleanup paths. Active mission flags are present in both the counter rebuild and route cleanup helpers. Durations are varied from 45 to 365 days.

| Category | Missions | Durations (days) | Regional and duplicate-risk contract |
| --- | ---: | --- | --- |
| National Settlement | 3 | 45, 90, 180 | named national/Dublin objectives; active flags prevent duplicate starts |
| Elections and Dáil | 2 | 60, 105 | named electoral objectives; shared election helper owns outcomes |
| Organised Society | 2 | 60, 150 | named civic objectives and one active instance per mission |
| Cultural and Archival | 3 | 180, 210, 270 | named archive/site objectives; concealed route remains separately gated |
| Radical Underground | 2 | 150, 180 | named organisation/constituent objectives; helper cleanup owns route state |
| Provision | 10 | 120, 150, 180, 270, 300 | named production, rail, port, and regional objectives; refund guards prevent repeat recovery |
| Readiness | 8 | 105, 120, 150, 210 | named command, corridor, coastwatch, and port objectives |
| Neutrality Incidents | 4 | 90, 105, 120, 150 | incident authority and neutrality-state gates; no generic wartime action bypass |
| Foreign Leverage | 4 | 120, 150, 240 | live sovereign partner and channel gates; closure cancels stale deliveries |
| Northern Settlement | 4 | 150, 210, 240, 300 | distinct negotiated Northern objectives and route gates |
| Occupation and Integration | 4 | 150, 240, 300, 365 | state 119 objectives; core remains behind final review rather than mission completion |
| Regional External | 3 | 180, 240, 300 | named member/charter/compact objectives |
| Postwar | 5 | 150, 240, 300, 365 | named reconstruction and demobilisation objectives |

Mission capacity is centralised at 8 normal, 10 during emergency or war, and 12 only during emergency plus Northern occupation. Category caps and critical reservations are rebuilt from the same active-flag set. The literal command-power deduction across every action is 35–50, below the 60-point ceiling.

## Audit findings that did not need source changes

- No action grants positive Political Power; the audit found no passive PP-store decision loop.
- Physical commitments are present where actions create delivery, transport, unit, industrial, or security obligations; cancellation refunds are separately guarded and documented as at most 70 percent of recoverable inputs.
- Foreign actions and missions share valid-partner checks for Britain, the United States, Germany, and the Vatican: existence, sovereignty, and non-capitulation; invalidated channels cancel the corresponding mission.
- The only Ireland core writer is `ireland_apply_northern_core_review`, which applies a core only to state 119 after stage-five integration, final regional proof, consent, security, resistance, guarantee, withdrawal, demobilisation, and failure checks.
- The three decision-category GUI ledgers only set selected-row or review-request state. Their effects do not grant PP, territory, cores, equipment, units, or political outcomes; `ai_check = { always = no }` prevents a GUI-only action from becoming an AI-only path.

## Decision-cost contract correction

The 140 Ireland actions now use the documented custom-cost-only model:

- Regular `cost = ...` is removed from all 140 custom-cost actions.
- Each action has `ai_hint_pp_cost` set to its maximum base-plus-scarcity Political Power exposure (23–29 PP).
- Each `complete_effect` manually deducts the action's base Political Power, while the existing named-ledger branches deduct the +10/+5/+0 scarcity surcharge.
- The action-specific custom-cost localisation shows the readable base cost, live named ledger, current value, and all surcharge bands.
- Existing affordability gates, physical commitments, cancellation/refund handling, and the 60-command-power ceiling remain unchanged.

Static contract audit after the correction: 140/140 AI hints, 140/140 base deductions, 140/140 action-specific cost keys, zero regular `cost =` lines, and zero unresolved action-cost localisation keys. Live HOI4 validation remains intentionally excluded.

## Evidence and remaining limits

- Static source checks confirmed the canonical 13 categories, 140 actions, and 54 missions.
- No live or HOI4 validation was run.
- `hoi4.gui_inspect` and `hoi4.gui_render` resolved the unrelated `mod_chaos_redux` workspace, so their Ireland-window-missing result cannot validate this repository's GUI layout. The source-level GUI wiring was reviewed separately.
- Artifact references from that mismatched workspace are retained only to document the limitation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a940b8f2f5e3d6c2f1fa4eeadc74a1251dc32fe77ac204cdfb9ed28fd9aa8e14/8de143e188166d92f3680c3e48b34ee32ab2125a06469499c035ae771129d2cc/gui-inspect.0cebc78d683de23b.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/33dddbb63d1c47bca7f6c217ebe650c60f9998bced2f03133fceb9ab72571f76/04aa5311c8104371199e9e58d19642b3f8eab9cfd4d739419fc7c9e22cd80e6c/ireland_conditions_panel_window-full.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8663d01c70ad0d1f9d2b62e599cf82c16982e3fbbe1889dd063192f731551367/bbd3af373c7fc04d3ebeb63df16600bea052740943123ec2c2d9f488d2658eaf/event-trace-8cb7d9f366af.json`.
