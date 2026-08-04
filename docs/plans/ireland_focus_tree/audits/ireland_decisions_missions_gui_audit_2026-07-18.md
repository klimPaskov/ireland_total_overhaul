# Ireland decisions, missions, and GUI audit — 2026-07-18

Historical snapshot note (reconciled 2026-07-22): this audit preserves the original lifecycle findings. The category counters, critical-slot reservation, and GUI request/row projection work are structurally present in `common/scripted_effects/ireland_runtime.txt`, `common/scripted_effects/ireland_culture.txt`, and `common/scripted_localisation/ireland_localisation.txt`; the re-audit and current follow-up supersede the corresponding missing-wiring claims. Shared escalation telemetry, dynamic cost/requirement presentation, and live scenario validation remain open. Use `docs/plans/ireland_focus_tree/source_of_truth_map.md` for disposition.

## Scope and conclusion

Audited the Ireland decision implementation, its category definitions, mission lifecycle helpers, AI registry, focus/event-facing route gates, localisation, and all three decision-owned scripted GUIs.

The inventory target is present: **13 categories, 140 actions, and 54 mission families**. The action command-power ceiling is **45**, below the required 60. All 54 mission definitions contain an `available` objective, a deadline, cancellation, timeout, completion, and AI blocks.

Do **not** treat the system as lifecycle-complete. Two shared-state omissions make the stated 8/10/conditional-12 mission caps and all category caps inert; a third semantic issue conflates cancellation with escalation. These require a coordinated lifecycle patch across mission activation, result recording, category-cap recalculation, and cleanup. They are not safe small local edits.

No gameplay or GUI source was changed by this audit.

## Inventory and lifecycle coverage

| Category | Required category cap | Actions | Mission families | Deadline range (days) | Mission quality / regional anchor |
| --- | ---: | ---: | ---: | ---: | --- |
| `ireland_settlement_government` | 2 | 10 | 3 | 45–180 | IRE; Dublin Metropolitan Region; cabinet, confidence, and settlement objectives. |
| `ireland_elections` | 2 | 10 | 3 | 60–105 | IRE; Dublin Metropolitan Region; electoral and government-formation objectives. |
| `ireland_organised_society` | 2 | 10 | 3 | 60–150 | IRE; Dublin Metropolitan Region; welfare, service, and social-consent objectives. |
| `ireland_cultural_archival` | 2 | 10 | 3 | 180–270 | IRE; cultural/archival objectives with named regional evidence. |
| `ireland_radical_underground` | 2 | 10 | 0 | — | IRE; action-only category, so no mission duplicate risk. |
| `ireland_provision` | 3 / 4 emergency | 16 | 10 | 120–300 | IRE; material objectives in Dublin and Connacht/Western Seaboard. |
| `ireland_readiness` | 3 / 4 invasion or war | 14 | 8 | 105–210 | IRE; readiness, reserve, equipment, and security objectives. |
| `ireland_neutrality_incidents` | 2 / 3 direct incident | 10 | 4 | 90–150 | IRE; shipping, internees, censorship, and belligerent-rule objectives. |
| `ireland_foreign` | 2 | 10 | 4 | 120–240 | IRE; named sponsor and diplomatic counterpart objectives. |
| `ireland_northern` | 3 | 10 | 4 | 150–300 | IRE; Belfast, Lower Lagan/Lisburn, Border Belt, and Dublin–Belfast objectives. |
| `ireland_occupation_integration` | 3 | 10 | 4 | 150–365 | IRE; named occupied-region/integration objectives. |
| `ireland_regional_external` | 2 | 10 | 3 | 180–300 | IRE; regional-partner objectives. |
| `ireland_postwar` | 3 | 10 | 5 | 150–365 | IRE; national reconstruction, including the Dublin–Galway Corridor. |

The 54 mission descriptions cover explicit place names: Dublin Metropolitan (20), Belfast Urban and Harbour (5), Cork and Southwest (5), Connacht and Western Seaboard (3), plus the Border Belt, Shannon network, Northern corridors, Gaeltacht/islands, and other named regions. Every family has `available`, `cancel_trigger`, `timeout_effect`, and `complete_effect`; completion and timeout use full/partial/failure custom effect tooltips. The individual ids are distinct, so there is no duplicate-id finding. The shared lifecycle defect below is the material duplicate/concurrency risk.

## Issues by severity

### Critical — global mission capacity never increases and result recording never runs

`ireland_has_active_mission_capacity` compares `ireland_active_mission_count` against the 8, 10, and 12 constants in [common/scripted_triggers/ireland_triggers.txt](../../../../common/scripted_triggers/ireland_triggers.txt). Campaign initialization sets the count to zero, and `ireland_record_mission_result` subtracts one, but the workspace contains no increment.

The same helper is guarded by `has_country_flag = ireland_mission_active` in [common/scripted_effects/ireland_effects.txt](../../../../common/scripted_effects/ireland_effects.txt). No source sets that generic flag. All 54 actions do set their individual mission active flag and call `activate_mission`, so missions can start, but the shared result accounting, completion counters, capacity decrement, global target cleanup, and capacity refresh are skipped.

Affected identifiers:

- `ireland_active_mission_count`
- `ireland_has_active_mission_capacity`
- `ireland_record_mission_result`
- `ireland_cleanup_mission_state`
- `ireland_mission_active`

Player effect: the normal cap of 8, emergency/war cap of 10, and emergency Northern-occupation cap of 12 do not limit concurrent mission starts; the dynamic “Active missions remaining” outcome tooltip also reports the wrong value.

### Critical — all 13 category-cap gates and the critical-slot reservation are read-only conditions

Every action checks a category `*_at_capacity` flag, and critical actions additionally check `ireland_critical_slot_reserved`. A repository-wide setter/clearer search found no `set_country_flag` or `clr_country_flag` for any of those flags in `common/`, `events/`, `history/`, or `interface/`.

Affected identifiers include all `ireland_category_<category>_at_capacity` flags and `ireland_critical_slot_reserved` in [common/decisions/ireland_decisions.txt](../../../../common/decisions/ireland_decisions.txt).

Player effect: the intended category caps and reserved critical capacity never engage, enabling parallel action/mission starts that the design explicitly disallows.

### High — cancellation is counted as escalation

The decision-file header defines result value 4 as cancellation, while `constant:ireland.mission_result_escalated = 4` in [common/script_constants/ireland_constants.txt](../../../../common/script_constants/ireland_constants.txt). Each mission cancellation sets result 4; the shared recorder therefore increments `ireland_missions_escalated` for ordinary cancellation.

This prevents analytics, AI follow-ups, or future dynamic localisation from distinguishing a cancelled mission from one that actually escalated. Mission-specific failure branches do set their own `*_escalated` flags, so the two concepts should remain separate.

### High — all three scripted GUI action buttons are no-ops despite action wording

The three review/inspect button clicks only set an otherwise unconsumed country flag and increment a GUI-dirty variable:

- `ireland_conditions_review_button_click` → `ireland_conditions_review_requested`
- `ireland_northern_review_button_click` → `ireland_northern_review_requested`
- `ireland_concealed_evidence_inspect_button_click` → `ireland_concealed_evidence_inspection_requested`

Their row clicks similarly set `*_selected_row` variables that have no reader outside [common/scripted_guis/ireland_scripted_guis.txt](../../../../common/scripted_guis/ireland_scripted_guis.txt). Yet their localised tooltips promise to open a review or evidence record. There is no matching decision/event, cost, availability, AI alternative, result, or cleanup path.

This is not a cosmetic fix: wiring a review to gameplay needs an explicit owner, cost, availability, and AI policy. Until then, make the buttons genuinely informational or wire each to a specified existing action; do not leave action language on a no-op click.

### Medium — three short missions need an explicit urgency rationale

The decision-mission guidance expects normal mission deadlines to be at least 90 days unless they are clearly emergency work. The following are shorter:

- `ireland_mission_assemble_seventy_routine_votes` — 45 days
- `ireland_mission_form_a_government_after_the_poll` — 60 days
- `ireland_mission_keep_essential_services_running` — 60 days

The latter two can plausibly be urgent; “routine votes” does not make that urgency clear. Either mark the appropriate families as emergency in their player-facing text/design matrix or adjust the deadlines.

### Medium — action base costs remain scattered magic numbers

All 140 actions have engine PP costs of 13–19 and manual CP base costs of 20–35, with correctly mutually-exclusive scarcity surcharges of 5 or 10. The maximum actual CP charge is 45. Material checks/effects also occur in the action catalogue, so this is not a passive PP-only store.

The ceiling and dynamic burden tooltip pass, but most base cost tuning remains duplicated in [common/decisions/ireland_decisions.txt](../../../../common/decisions/ireland_decisions.txt), rather than centralized script constants. Consolidate only when doing the lifecycle architecture work; a blind mechanical rewrite is not warranted by this audit.

### Low — decision-level AI priorities are shallow

The AI registry has 30 durable profiles and 10 temporary overlays, all constrained to `original_tag = IRE`; inspected profiles use route/eligibility gates, and the decision file contains no literal country target assignments to audit as dead targets. This is a sound validity baseline.

However, action and mission `ai_will_do` blocks are largely a fixed base plus a zero-weight `*_blocked` flag. The registry guides national posture, not which available mission the AI should prefer when several compete. Run route scenarios after the lifecycle fix and add only the specific priority modifiers that prove necessary.

## Cost, requirement, localisation, and cleanup notes

- Cost clarity passes structurally: each action exposes `ireland_action_burden_tt` with current burden, PP, and CP values. The generated availability checks mirror the highest possible scarcity cost, preventing unaffordable starts. CP is never above 45.
- Mission requirement clarity is generally good: descriptions identify the named objective and region, built-in timers supply the deadline, and full/partial/failure tooltips are present. The global active-count text is unreliable because of the critical lifecycle defect.
- Escalation is present as a family-level `*_escalated` flag in all 54 mission families, but the shared numeric outcome mislabels cancellation as escalation.
- `ireland_cleanup_mission_state` clears shared global event targets `ireland_mission_target` and `ireland_mission_region`. It is currently skipped; if the generic guard is simply enabled, one concurrent mission could erase another mission’s target. Cleanup must be made mission-instance-safe before the guard is enabled.
- Category visibility and route locks have direct flag gates. The Northern category is gated by Northern contact/negotiation/war/review flags, and no invalid literal country target was found in the decision source.

## Scripted GUI evidence

The three intended surfaces are attached to the expected categories:

- `ireland_conditions_panel_scripted_gui` — settlement/government
- `ireland_concealed_evidence_ledger_scripted_gui` — cultural/archival
- `ireland_northern_settlement_ledger_scripted_gui` — Northern

`hoi4.gui_inspect` and `hoi4.gui_render` were run read-only with scenario `ireland_audit`, at 1920×1080 and 1280×720 across normal, warning, locked, and long-text states. The render comparison changed zero pixels between those synthetic states because the scenario has no live country values; it is layout evidence only, not gameplay evidence.

| Surface | Inspect fidelity | Render artifact |
| --- | --- | --- |
| Conditions panel | 401 modelled, 22 approximated, 31 ignored, 26 missing, 50 unsupported, 1 unresolved | `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/41d8d8af19864a287581248709cd6c69438505d4670573a84b454ed943c575c8/2cf3e19c9e7696ac145eb11eed4ca277bdfd6477f7070c6ad2a3cf6254345aae/ireland_conditions_panel_window-full.png` |
| Northern ledger | 264 modelled, 11 approximated, 24 ignored, 15 missing, 39 unsupported, 0 unresolved | `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/ef23984e451fb33db4d1676fef6e226ecdf56d37e322db343e9671a68a9aaa2f/305cee31fa5bb5b2d0365e644a3d514db462a8be62121a59275576af8edc4259/ireland_northern_settlement_ledger_window-full.png` |
| Concealed-evidence ledger | 234 modelled, 10 approximated, 21 ignored, 14 missing, 33 unsupported, 0 unresolved | `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/b8f7ad4aedbf3ac46595142fdefb66c56e7babf5b5c3a56bbef2ad1d7362163f/c9ac5711508c82c599de08a9e48c750d09d8b09dce70bee076f6a21573ea3783/ireland_concealed_evidence_ledger_window-full.png` |

The renderer reported no source-controlled visible overlap. Its shared game index has 2,000 unrelated blocking diagnostics from vanilla/game files, so fidelity figures are partial rather than a clean GUI validation pass.

## Required follow-up design

1. Define a single mission-instance lifecycle contract in [common/scripted_effects/ireland_effects.txt](../../../../common/scripted_effects/ireland_effects.txt): increment once on activation; record/decrement exactly once on complete, timeout, or cancellation; and use instance-safe target cleanup.
2. Route all 54 `activate_mission` call sites in [common/decisions/ireland_decisions.txt](../../../../common/decisions/ireland_decisions.txt) through that contract. Retain each family’s own active/completion/partial flags, but do not use one generic country flag as a concurrency guard.
3. Add one category-cap recalculation helper that owns the 13 `*_at_capacity` flags and `ireland_critical_slot_reserved`; call it on activation and every terminal path. Test exactly 8 normal, 10 emergency/war, and 12 emergency Northern-occupation starts.
4. Give cancellation its own result constant/counter, or redefine result 4 and all consumers consistently; do not count a cancellation as escalation.
5. Decide whether each GUI review/inspect click is informational or mechanical. For mechanical clicks, explicitly map it to an existing decision/mission with matching availability, costs, tooltip, AI behaviour, outcome, and cleanup. For informational clicks, remove the action claim and make selection variables drive visible detail.
6. After implementation, exercise normal, emergency/war, and emergency+Northern occupation capacity scenarios; concurrent terminals; route cleanup; a dead/invalid partner; closed foreign route; and each GUI click/close pair.

## Validation evidence and limits

- Parsed the decision tree: 13 categories, 140 actions, 54 missions; category-level counts and duration ranges are in the table above.
- Confirmed 54 occurrences each of `activate_mission`, `days_mission_timeout`, completion, timeout, and cancellation blocks; full-success tooltips occur 54 times, partial-success 108 times, failure 54 times, and family escalation flags 54 times.
- Confirmed no active-mission increment and no category-cap/reserved-slot flag setters in the searched implementation surfaces.
- Confirmed all GUI click-state flags and row selections are only written by their own scripted-GUI file.
- Read the Ireland spec/matrices, the offline Paradox pages for decisions, triggers, effects, localisation, scopes, events, AI, interface, and scripted GUIs; read the relevant vanilla decision and scripted-GUI documentation and a vanilla mission-bearing decision file.
- Used `hoi4.event_inspect` for the shared mission-active flag’s state flow. It returned partial linked evidence because the global event graph has unrelated skipped sources; source inspection above remains the authoritative evidence for the missing setter.

No live HOI4 mission scenario was launched during this audit, and no gameplay patch was applied. The audit is deliberately incomplete as an implementation proof until the lifecycle redesign above is made and exercised.
