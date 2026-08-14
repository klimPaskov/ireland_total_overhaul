# Decision and mission audit fixes — 2026-08-14

## Scope and result

This patch closes blockers 1 through 5 from [the final decision and mission audit](final_decision_mission_audit_2026-08-14.md). It owns only the named Ireland decision, territorial-event, scripted-effect, and English localisation surfaces. Concurrent focus-tree and thumbnail changes were preserved.

Vanilla `ARG.txt` and `AST.txt` decision examples, the offline Decision modding page, and the current vanilla Effects and Triggers documentation confirm the lifecycle model used here: `complete_effect` starts a timed decision, natural `days_remove` expiry runs `remove_effect`, and `cancel_trigger` ends the decision without its `remove_effect` outcome.

## Changed files

- `common/decisions/ireland_decisions.txt`
- `common/decisions/ireland_expansion_decisions.txt`
- `events/ireland_territorial_diplomacy_events.txt`
- `common/scripted_effects/ireland_effects.txt`
- `localisation/english/ireland_l_english.yml`

## Resolved issues, ordered by severity

1. **Critical, resolved — unsupported timed-flag values.**
   - Added `@IRELAND_TERRITORIAL_PLEBISCITE_RELAUNCH_COOLDOWN_DAYS = 180` in `ireland_expansion_decisions.txt`, mirroring `ireland.territorial_plebiscite_relaunch_cooldown_days`.
   - Added `@IRELAND_TERRITORIAL_DIPLOMACY_COOLDOWN_DAYS = 180` in `ireland_territorial_diplomacy_events.txt`, mirroring `ireland.territorial_diplomacy_cooldown_days`.
   - Replaced the 29 event writes and the plebiscite relaunch write so every `set_country_flag = { ... days = ... }` uses the owning file-local literal. Removed the temporary-variable duration bridge.

2. **High, resolved — Provincial Assent could be recorded without consent.**
   - `ireland_territorial_diplomacy.25`, option `ireland_territorial_diplomacy.provincial_assent.record`, now has a player legality `trigger` with all four intended floors: Unionist Consent 25, Nationalist Consent 50, Royal Legitimacy 55, and Administrative Reach 70.
   - The new `ireland_territorial_provincial_assent_record_requirements_tt` names each test and shows the current value. The adjourn option remains the legal incomplete path.

3. **High, resolved — P0 institutional projects recorded before their project time elapsed.**
   - Moved durable records and `ireland_begin_conclusion_review` from `complete_effect` to `remove_effect` for:
     - `ireland_action_ratify_the_postwar_republic`
     - `ireland_action_civilianise_the_workers_congress`
     - `ireland_action_place_the_directorate_under_statute`
     - `ireland_action_convert_contracts_to_reconstruction_credit`
     - `ireland_action_define_the_postwar_crown`
     - `ireland_action_reconstitute_the_postwar_coalition`
     - `ireland_action_reconvene_the_workers_congress`
     - `ireland_action_demobilise_the_failed_directorate`
     - `ireland_action_rebalance_the_producer_estates`
     - `ireland_action_reconvene_the_crown_council`
     - `ireland_action_record_an_alternate_postwar_order`
   - Each now sets only an `_in_progress` launch flag in `complete_effect`, uses `cancel_trigger` rather than `remove_trigger` for route cleanup/archive/tag loss, and clears that launch marker in `cancel_effect`.

4. **High, resolved — P1 rebuild/convention cards resolved on day zero.**
   - `ireland_territorial_rebuild_workers_border_campaign` now grants its three ledger increments and activates `ireland_mission_sustain_the_workers_border_campaign` only from terminal `remove_effect`.
   - `ireland_territorial_reconvene_provincial_assent` now sends `ireland_territorial_diplomacy.25` only from terminal `remove_effect`.
   - Both have explicit launch flags and cleanup cancellation paths.

5. **High, resolved — fascist withdrawal was not a valid partial Northern conclusion.**
   - `ireland_territorial_withdraw_border_enforcement` now performs its durable diplomatic cleanup and partial record only when its 120-day project ends. It also sets `ireland_northern_policy_selected`.
   - `ireland_finalize_route_conclusion` independently recognises `ireland_territorial_fascist_partial_recorded`, so the partial outcome remains valid even if a later narrow system consumes the generic selection flag.

## Category lifecycle notes

`ireland_postwar` now treats settlement and recovery cards as actual factory projects. Selection sets a transient launch flag, natural expiry sets the constitutional or recovery record and begins the 180-day conclusion review, and route cleanup/archive cancellation leaves no durable project record. `ireland_cleanup_route_state` explicitly clears all fourteen new launch flags so the visible category, counters, and cleanup state cannot retain an abandoned project.

`ireland_territorial_policy` keeps the Congress rebuild, Provincial Assent reconvene, and fascist withdrawal as 120-day work cards. They have no result, ledger change, mission activation, or Northern policy selection until natural expiry. Route cleanup/archive cancellation only clears launch state.

## Mission quality notes

| Surface | Owner/category/region | Requirement and duration | Success | Failure/cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `ireland_mission_sustain_the_workers_border_campaign` | IRE / `ireland_territorial` / Northern national-question campaign | 180 days, full at Social 60 and Nationalist 60, partial at Social 45 and Nationalist 50 | Records full or partial Northern policy | Timeout records failure; cancellation records cancellation | Rebuild activates the existing mission only after its own terminal project. Existing active-marker and capacity helper prevent a parallel mission. |
| `ireland_territorial_rebuild_workers_border_campaign` | IRE / `ireland_territorial` / Northern organisers | 120 days, one civilian factory, mission capacity must be available | At expiry adds the documented consent/labour increments and restarts the existing mission | Route cancellation clears only `ireland_territorial_workers_campaign_rebuild_in_progress` | No new mission id or duplicate capacity path. |
| `ireland_territorial_reconvene_provincial_assent` and `.25` | IRE / `ireland_territorial` / Provincial convention | 120-day factory project, then all four record floors must be met | Opens the event after the project and records assent only when the option is legal | Adjournment remains a repeatable partial path; cancellation opens no event and leaves no pending marker | The pending flag gates the event, so an active duplicate convention is not created. |
| `ireland_territorial_withdraw_border_enforcement` | IRE / `ireland_territorial` / Northern enforcement exit | 120 days after refusal/counteroffer and invalid or unsafe enforcement conditions | Closes pending demand state, records partial Northern policy, opens Atlantic security exit | Route cancellation clears only launch state; no PP or material refund | `fire_only_once` and the withdrawn record prevent repetition. |

## Cost, AI, route-lock, and tooltip notes

- The P0 and P1 factory reservations remain the only project cost. No settlement, recovery, reconvene, or withdrawal card now produces a day-zero durable benefit.
- Provincial Assent now shows a single custom requirement tooltip rather than treating AI weights as human legality. AI remains zeroed for historical focus behavior as before.
- Fascist withdrawal retains its original valid-target, refusal/counteroffer, readiness, and route conditions. Its completed partial record is now accepted by the conclusion evaluator.
- Updated P0/P1 localisation says the project reserves a factory and describes the result as occurring when the displayed project finishes. The Provincial Assent threshold text mirrors the authoritative script constants and should be updated in the same change if those four tuning values are retuned.

## Cleanup and exploit-risk notes

- All project launch flags are cleared locally on `cancel_effect` and centrally by `ireland_cleanup_route_state`; no project result flag is set before natural expiry, so archive/cleanup cannot retain a false constitutional, recovery, mission, or Northern-policy record.
- The five stale diplomatic branches retain `@IRELAND_TERRITORIAL_DIPLOMACY_STALE_REFUND = 50`. This is exact repayment of the initiating 50 PP administrative charge, while consumed enforcement manpower, equipment, convoys, fuel, and command effort remain spent. Claims are one-use and stale branches clear flags and targets, so this is not a PP or material farming loop. An event-file comment and all five player tooltips now state that contract explicitly.

## Validation evidence

- Targeted lifecycle source check passed: all eleven P0 and three P1 audited cards have no durable outcome in `complete_effect`, retain it in `remove_effect`, and have `cancel_effect` cleanup. It also confirmed all four Provincial Assent record checks and all 29 diplomatic plus one plebiscite cooldown writes use the file-local literals.
- `hoi4.event_inspect` lint after the patch reported no blocking diagnostics. Evidence: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0191b62b9a303914db052a6e1d3352dd107e5faebdd9e67cb0e572c5174845b6/658a191117de0a5920e2e0c04c108c011598213249074254dcd10e69683cc6d0/event-lint-d3375312c35a.json`.
- `hoi4.event_render` produced the bounded terminal manifest at revision `d3375312c35a`: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/bcb5ef695ff1db2c3806a417d0524012c0c6dabc39c2c86b48dec6220f2426f5/db89117515b5abcffb1de8d920bc1aac23c7678e9d4af85bc4b51329215ff2f2/event-terminals-d3375312c35a-manifest.json`.

## Skipped validation and remaining issues

- An MCP before/after comparison could not be produced. The prior revision was not cached, and the available pre-patch event graph snapshot exceeds the comparison artifact ceiling (105,427,864 bytes versus 67,108,864 bytes). The post-patch lint and bounded terminal render are therefore evidence only for the current graph.
- Live-engine testing of the timed decision expiry and the `set_country_flag days = @literal` parser behavior was not run in this workspace. The source model follows the required wiki and vanilla precedent, but parent live-session confirmation remains useful.
- No decision-owned scripted GUI exists in scope, so GUI inspection/rendering was not applicable.

No plan handoff was needed because every blocker was a local lifecycle, trigger, cooldown, evaluator, or localisation correction rather than a new decision system.
