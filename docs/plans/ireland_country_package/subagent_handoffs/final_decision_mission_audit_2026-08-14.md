# Final decision, mission, and territorial-recovery audit — 2026-08-14

## Audit boundary

Read-only audit of committed `317ce37` (*Implement Ireland territorial recovery paths*) and `f7e5e64` (*Implement Ireland family postwar conclusions*). I did not inspect the concurrent uncommitted focus-tree, thumbnail, or handoff changes as implementation evidence, and made no gameplay edits or commit.

Required offline wiki pages, vanilla documentation (including Script Constants, Effects, and Triggers), vanilla decision precedents, and the decisions/missions, events, focus-tree, and subagent skills were consulted. Vanilla `common/decisions/SIA.txt` supplies a direct precedent for `days_remove = constant:...`; those P0 duration constants are parser-safe.

MCP evidence: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d2fe31cd16f5e00f1ed7153a5d0c05770e6e2eda337e743c64aeac3a0a6ba462/fb761fe04cf8576305ff383d1587ac0d377066316e7ef874656eae2e4e4854d5/event-state_flow-03121b7ede8d.json` (`hoi4.event_inspect`, `state_flow`, `ireland_territorial_diplomacy.25`). Fidelity is partial: it confirmed the source-linked event artifact but deferred workspace-wide helper/lifecycle projection. The findings below are source-traced rather than inferred from that partial artifact. There is no decision-owned scripted-GUI surface in scope, so GUI inspection/rendering was not applicable.

## Issues, highest severity first

1. **Critical — parser-unsafe territorial cooldown durations.**
   - `common/decisions/ireland_expansion_decisions.txt`, `ireland_territorial_reopen_supervised_plebiscite`, sets a temporary variable from `constant:ireland.territorial_plebiscite_relaunch_cooldown_days`, then supplies that variable to `set_country_flag = { ... days = ... }` (lines 335–336).
   - `events/ireland_territorial_diplomacy_events.txt` repeats the same variable-in-`set_country_flag days` shape **29 times** (lines 85–86 through 791–792) for the diplomatic cooldown.
   - The events skill documents `set_country_flag` duration as a sensitive field which accepts a file-scoped `@` literal, not a normal/temp variable or `constant:` token. This is a load/save parser risk, not a balance concern.
   - **Fix:** add a file-scoped cooldown macro in each owning file, mirroring the shared script constant, and use it directly in `days = @...`. Remove the temporary-variable setup. Keep `common/script_constants/ireland_constants.txt` as the cross-file tuning source.

2. **High — the player can record Provincial Assent without meeting any consent, legitimacy, or administration requirement.**
   - `events/ireland_territorial_diplomacy_events.txt`, event `ireland_territorial_diplomacy.25`, option `ireland_territorial_diplomacy.provincial_assent.record`, has the four intended thresholds only as `ai_chance` modifiers. They do not constrain a human option.
   - Selecting it at any values leads to `.26`, which sets `ireland_territorial_provincial_assent_complete`, `ireland_territorial_provincial_assent_recorded`, and `ireland_northern_policy_selected` (lines 862–879). It bypasses the intended adjournment/reconvene loop and its one-factory recovery gate.
   - **Fix:** put all four threshold checks in the record option's `trigger`, wrapped in a custom trigger tooltip whose localisation reports the actual consent, legitimacy, and administrative requirements. Keep adjourn available as the failure/partial path.

3. **High — timed P0 settlement/recovery projects record success immediately, and route cleanup cannot retract it.**
   - All five settlement actions and all five family recoveries in `common/decisions/ireland_decisions.txt` use `complete_effect` to set their durable result flags and call `ireland_begin_conclusion_review`, while their 180/120-day factory reservation is still active. Per Decision modding, `complete_effect` runs when the player selects the decision; it is not the end-of-`days_remove` hook.
   - A route cleanup/archival removes the decision through `remove_trigger`, but these ten decisions have no matching `remove_effect`/`cancel_effect`. `ireland_cleanup_route_state` in `common/scripted_effects/ireland_effects.txt` contains **zero** clears for `ireland_family_postwar_settlement_complete` or the five settlement-record flags. A cancelled project therefore survives as a completed constitutional settlement/recovery and may start the 180-day review without its 180/120-day work being completed.
   - The current player text is contradicted by code: `ireland_postwar_family_settlement_requirements_tt` and `ireland_postwar_family_recovery_requirements_tt` promise cleanup “without a ... record,” while every result is recorded at selection.
   - The auxiliary `ireland_action_record_an_alternate_postwar_order` has the same immediate-record/no-cleanup pattern, although it does not begin a conclusion review.
   - **Fix:** reserve the factory at launch, then perform durable settlement/recovery records and `ireland_begin_conclusion_review` only on normal terminal expiry. If `remove_effect` is used, guard it against route cleanup/archival; add explicit cancellation/remove cleanup for launch-only state. If design instead intentionally records at launch, revise the timing/tooltips and remove the claim that cancellation has no record; the present mixed contract is unsafe.

4. **High — the P1 factory recoveries also claim to complete after 120 days but start their result immediately.**
   - `ireland_territorial_rebuild_workers_border_campaign` immediately adds its three ledger increments and activates the 180-day Congress mission. `ireland_territorial_reconvene_provincial_assent` immediately sets pending and fires `.25`. Both only *display* a 120-day one-factory project; neither has terminal or cancellation cleanup.
   - Their localisation explicitly says the campaign/convention resumes *after* the 120-day factory commitment. The current code lets the mission/event resolve on day zero, so a player can obtain a conclusion while the nominal recovery project later remains merely as a factory lock.
   - **Fix:** move ledger increase/mission activation and provincial-event dispatch to terminal expiry; add cancellation cleanup so neither pending flag nor mission is orphaned. If launch-time resolution is intended, change duration/wording and remove the faux recovery-project framing.

5. **High, pending design confirmation — Fascist withdrawal is advertised as a partial conclusion but cannot clear the final Northern blocker.**
   - `ireland_territorial_withdraw_border_enforcement` correctly requires the safe/invalid-target/refusal cases through `ireland_territorial_border_enforcement_withdrawal_required`, clears all pending diplomacy flags and global targets, leaves consumed reserves unreimbursed, and opens `ireland_territorial_atlantic_security_exit_open`.
   - It sets `ireland_territorial_fascist_partial_recorded` but neither `ireland_northern_policy_selected` nor `ireland_northern_deferment_accepted`. `ireland_finalize_route_conclusion` in `common/scripted_effects/ireland_effects.txt` treats absence of precisely those latter two flags as `ireland_route_conclusion_blocked_northern`.
   - Thus the advertised “partial territorial conclusion” cannot actually conclude a fascist route; it only opens Atlantic follow-up and forces P0 recovery. This may be intended as an unresolved-Northern design, but conflicts with its decision tooltip and P1 handoff description.
   - **Fix:** either make withdrawal explicitly record a lawful/partial Northern policy, or teach the conclusion evaluator to recognise the withdrawal record as a partial rather than unresolved outcome. Update the decision text to match the selected design.

6. **Medium — stale-target refunds are exact full PP refunds after the diplomatic action consumes its material reserve.**
   - Five stale-result branches in `events/ireland_territorial_diplomacy_events.txt` grant `@IRELAND_TERRITORIAL_DIPLOMACY_STALE_REFUND = 50` PP (for example lines 98, 339, 473, 602, and 726) after an underlying 50-PP demand/enforcement decision has consumed Atlantic reserves.
   - This is not a free PP loop in the reviewed paths: the refund equals the initiating 50 PP cost, the material reserve remains spent, target pointers are cleared, and the relevant claims are `fire_only_once`. It does, however, exceed the stated “only unspent administrative portion” cancellation rule unless a stale target is intentionally a full administrative refund.
   - **Recommendation:** retain only with an explicit design decision and player tooltip. Otherwise change the refund to the documented unspent amount. Do not refund the material reserve or erase the foreign outcome.

## P0 five-family settlement and recovery lifecycle

All five families have the intended visible/capstone/factory gates, one 180-day settlement card, a family report (`ireland_country_conclusion.1` through `.5`), and a 120-day one-factory repair card when `ireland_conclusion_recovery_open` is raised. The report options correctly archive only full/partial outcomes; recovery leaves the route open. No P0 settlement, report, or recovery grants cores, equipment, units, factories, manpower, or Political Power.

| Family | Settlement -> repair | Current repair surface | Lifecycle assessment |
| --- | --- | --- | --- |
| Democratic | `ireland_action_ratify_the_postwar_republic` -> `ireland_action_reconstitute_the_postwar_coalition` | clears government/law blockers | Correct family pairing and report dispatch; affected by issue 3. |
| Communist | `ireland_action_civilianise_the_workers_congress` -> `ireland_action_reconvene_the_workers_congress` | clears government/defence blockers | Correct pairing; affected by issue 3. |
| Fascist | `ireland_action_place_the_directorate_under_statute` -> `ireland_action_demobilise_the_failed_directorate` | clears defence blocker | Correct pairing; affected by issue 3 and territorial issue 5. |
| Oligarchic | `ireland_action_convert_contracts_to_reconstruction_credit` -> `ireland_action_rebalance_the_producer_estates` | clears economy blocker | Correct pairing; affected by issue 3. |
| Restoration | `ireland_action_define_the_postwar_crown` -> `ireland_action_reconvene_the_crown_council` | clears government/identity blockers | Correct pairing; affected by issue 3 and Provincial Assent issue 2. |

`ireland_begin_conclusion_review` correctly centralises the 180-day review counter, and `ireland_tick_reviews_and_windows` decrements it to `ireland_conclusion_review_due`. The timing flaw is the decision terminal boundary, not the review counter itself.

## P1 recovery and mission quality

### Democratic plebiscite relaunch

`ireland_territorial_reopen_supervised_plebiscite` is correctly visible only after a recorded failed/cancelled democratic plebiscite, refuses to run while the mission/diplomacy is active, costs 15 PP, preserves the original outcome record, clears only the prior launcher lock, and sets the existing material-refund guard before directly activating the old mission. That guard prevents a duplicate manpower/equipment refund from the original launcher. The remaining blocker is the parser-unsafe 180-day cooldown flag (issue 1), plus the generic launch-time timing mismatch in issue 4.

### Congress mission, rebuild, and capacity accounting

| Field | Evidence |
| --- | --- |
| Owner/category/region | IRE; `ireland_territorial`; Northern national-question campaign. |
| Launch | `ireland_territorial_workers_border_campaign`: 25 PP/35 days, one-use; only ledger inputs (+5 nationalist, +2 unionist, +3 social), then activates the existing mission. |
| Duration/requirements | `ireland_mission_sustain_the_workers_border_campaign`: 180 days. Full = Social Consent 60 and Nationalist Consent 60; partial = 45 and 50 respectively, exposed by `ireland_territorial_workers_campaign_objective_tt`. |
| Success | Records full or partial mission result and `ireland_northern_policy_selected`; no core, territory, PP, stockpile, or unit reward. |
| Failure/cancel | Both record an outcome, clear active/temporary flags, and call `ireland_update_mission_capacity`. Timeout exposes the one-factory rebuild; cancellation does not award a refund. |
| Rebuild | `ireland_territorial_rebuild_workers_border_campaign`: intended 120-day factory recovery, adds only +3 nationalist/social/labour ledger inputs and restarts the existing mission; no PP/equipment/core. It has the terminal-boundary problem in issue 4. |
| Duplicate/capacity risk | `ireland_rebuild_mission_counters` includes the mission in the global active counter and Northern category counter. Launch, success, cancellation, timeout, and rebuild all use the active marker and `ireland_update_mission_capacity`; no duplicate active-mission route was found. |

### Restoration Provincial Assent (.25–.27)

`.25` is triggered only by the pending flag; `.26` records assent and clears response/pending; `.27` records adjournment, preserves the first-adjournment flag, and clears its pending markers. `.27` has no material, PP, territory, core, factory, or unit outcome. The reconvene decision is appropriately repeatable after adjournment and checks an improved consent/legitimacy condition. Its player-facing requirements are too broad for the actual desired four-way success gate, and its success can currently be forced by issue 2.

### Fascist withdrawal

The route-lock and AI safety requirements are good: original IRE/fascist method, enforcement open, no issued war goal/active diplomacy, a refusal or rejected counteroffer, then invalid readiness/target/controller conditions. Cleanup is complete for the direct diplomacy pointers and pending flags; no PP, material, manpower, equipment, core, or war goal is created. Final conclusion integration remains blocked as described in issue 5.

## Costs, tooltip, AI, cleanup, and exploit notes

- P0 costs are varied appropriately as one-factory institutional work rather than flat PP exchanges. P1 uses 15/25 PP for political launch work, a one-factory recovery when work must be rebuilt, and the existing Atlantic reserve sink for coercive enforcement.
- Player-facing mission objective text is present and accurate for Congress. P0 cancellation tooltips and the two P1 delayed-recovery tooltips are inaccurate because their effects fire at selection (issues 3–4). Provincial Assent’s success tooltip has no requirement display despite the event prose claiming these requirements determine the result (issue 2).
- AI has meaningful non-historical zero weights for the relevant territorial paths. The `.25` weighting itself is not a human legality gate and cannot substitute for one. The family settlements/recoveries use distinct critical/recovery AI scores.
- Global territorial pointers are centralised in `ireland_clear_territorial_diplomacy_targets`; the terminal diplomacy branches and `ireland_cleanup_route_state` invoke it. The workers mission is included in both active/global and Northern capacity rebuild paths. Those cleanup/capacity surfaces are sound.
- No free P0/P1 core, equipment, unit, factory, manpower, or net PP reward was found. The only exception requiring design confirmation is the exact 50-PP stale-target reimbursement noted in issue 6; it is not net-positive, but it is a full administrative refund after material has been consumed.
- Static cross-file checks found all 17 audited decision/mission localisation entries, all conclusion `.1`–`.5` and territorial `.25`–`.27` event definitions, and all audited P0/P1 script constants. `localisation/english/ireland_l_english.yml` has UTF-8 BOM (`EF BB BF`). No unsupported `<=`/`>=` operator occurs in the audited source files.

## Recommended parent fixes, in order

1. Fix the 30 timed-flag duration writes in `common/decisions/ireland_expansion_decisions.txt` and `events/ireland_territorial_diplomacy_events.txt` with file-local `@` cooldown literals; preserve matching values in `common/script_constants/ireland_constants.txt`.
2. Gate `ireland_territorial_diplomacy.25`’s record option with all four actual thresholds and add a requirements tooltip/localisation value display.
3. Decide the terminal model for the fourteen timed P0/P1 settlement/recovery/withdrawal cards. For the documented “after N days” model, put success/event/mission effects only on normal terminal expiry, guard any `remove_effect` against cleanup/archival, and add `cancel_effect` cleanup. Apply it consistently to the P0 five settlements, five recoveries, alternate-order record, Congress rebuild, Provincial Assent reconvene, and fascist withdrawal.
4. Decide whether `ireland_territorial_fascist_enforcement_withdrawn` is an intentionally unresolved Northern outcome or a valid partial policy. Patch `ireland_finalize_route_conclusion` or the withdrawal effect and localisation accordingly.
5. Confirm the stale-target PP policy before changing it; it is currently non-exploitable but conflicts with the narrow-refund design wording.

## Validation limits and remaining blockers

This was a static, source-level final audit. I did not run the game, modify gameplay, or commit; live runtime confirmation of the `set_country_flag days` parser restriction and decision terminal semantics remains for the parent’s post-fix validation. Completion is blocked by issues 1–5. No separate plan handoff was written; this audit file is the handoff.
