# Expansion Decision and Parliament Final Audit

**Scope:** Current working tree audit of `common/decisions/ireland_expansion_decisions.txt`, the `ireland_territorial_policy` category, related focus/trigger/AI/localisation/GFX surfaces, and the four Parliament GUI actions.

**Verdict at first pass:** The first inspected implementation was materially narrower than the accepted expansion addendum. The dated closure below supersedes that interim finding against the final expanded source.

## Small patches made

| File | IDs | Before | After |
| --- | --- | --- | --- |
| `common/national_focus/ireland_focus_tree.txt` | `ireland_enforce_atlantic_claims` | The focus required `ireland_atlantic_force_authorised`, a flag set only by fascist `ireland_force_the_border_question`; the restoration `ireland_dal_riata_claim` branch could never reach its State 120 claim decision. | Its availability accepts either the fascist authorisation or `ireland_atlantic_claims_restoration`, while retaining the readiness-conclusion gate. Restoration can now reach its intended Highlands-only claim decision. |
| `common/decisions/ireland_expansion_decisions.txt` | `ireland_territorial_claim_scottish_highlands`, `ireland_territorial_claim_wales`, `ireland_territorial_claim_cornwall` | A claim could be begun when the state was Irish-controlled or controlled by an Irish faction partner. Raw readiness conditions were presented directly. | Each decision requires an externally controlled, non-Irish-owned target outside Ireland's faction and renders that condition through `ireland_territorial_claim_foreign_controller_requirement_tt`. The readiness trigger is wrapped in `ireland_atlantic_claim_enforcement_ready_tt`. |
| `common/scripted_localisation/ireland_localisation.txt`, `localisation/english/ireland_l_english.yml` | `GetIrelandParliamentSettlementOpenStatus`, `ireland_parliament_confidence_button_tt`, `ireland_parliament_budget_button_tt` | Confidence and budget tooltips did not show the canonical `ireland_settlement_open` gate. | Both tooltips include a live green/red settlement-open row, exactly matching their shared click trigger. |

No changes were made to `thumbnail.png`.

## Severity-sorted issues remaining

1. **High — the territorial category is not the promised five-family, Northern, and postwar decision surface.** `ireland_territorial_policy` opens after `ireland_define_the_national_question`, but its only children are the three coercive external claims. Democratic, communist, oligarchic, and restoration Northern methods are absent; the democratic/communist/oligarchic Atlantic alternatives are absent; no State 119 action exists in this category. With `visible_when_empty = no`, those route families see no territorial category at all.

   The accepted addendum requires the family decisions listed in its `Decision families` table, beginning at `ireland_territorial_open_northern_plebiscite`, and requires a visible lifecycle after the national-question focus. This is a feature gap, not a safe local tweak. Plan it as a cohesive decision/event/missions implementation under `docs/plans/ireland_focus_tree/`.

2. **High — postwar administration is focus flags without decision or mission ownership.** The focus tree sets `ireland_atlantic_postwar_review_open`, `ireland_atlantic_rights_charter`, `ireland_atlantic_protectorate_statutes`, `ireland_atlantic_integration_review_open`, and `ireland_atlantic_settlement_concluded`; no decision, mission, event, effect, or cleanup handler consumes them. The addendum instead requires one reservation and settlement mission per external state, success/failure handling, release/review choices, and cleanup on peace or transfer. The visible focus text therefore promises a postwar system that does not exist.

3. **High — company contract coverage does not match the nine-company commitment.** `ireland_company_aer_lingus_unlocked` appears only in its focus and industrial-concern idea; no decision consumes it. The other eight companies collapse into four one-shot generic decisions. Once a shared `fire_only_once` decision is taken, a later partner company unlock supplies no material contract. In particular, Railways/Ford Cork, Shipping/Harland & Wolff, and Sugar/Turf/Steel are mutually consumed by the first unlock. This needs company-specific or company-stateful actions; attaching Aer Lingus to an unrelated truck/train action would not be a safe correction.

4. **High — coercive escalation has no strength, supply, convoy, command-power, naval-access, target-allies, Northern-war, or postwar-review safeguards.** `ireland_atlantic_claim_enforcement_ready` only demands peace, the two route/readiness flags, Dublin, 750 available manpower, and 100 Infantry Equipment. Those reserves are disproportionately low for a 70-day preparation leading to a 180-day war goal against the live controller of States 120, 122, or 123. AI has only base `1` and a historical-zero modifier. The addendum calls for shared strength and stockpile gates, including comparison of both sides' allies, and stop conditions. This is balance/design work, not a local scalar edit.

5. **Medium — controller changes during the 70-day timer are not revalidated at completion.** The new availability guard prevents an invalid target when clicked, but `complete_effect` creates the war goal against whichever country controls the state when the timer finishes. If the state becomes Irish-controlled or an allied-faction occupation during the timer, the effect can attempt an invalid/self/friendly target. A follow-up must add a documented cancellation or completion safeguard with an explicit player-facing cancellation outcome; do not silently consume 50 PP and 70 days.

6. **Medium — all four company contracts use the same 25 PP / 35-day exchange and Political Power is their only cost.** `fire_only_once` prevents repeat farming, and State Materials safely adds a building slot before a civilian factory, but the costs are flat and do not use the factory time, equipment, fuel, convoys, manpower, or route conditions called for by their differing narratives. The local `@` table is syntactically appropriate for native fields, but the values and duplicated localisation text can drift from each other.

7. **Medium — the three external claims skip the addendum's demand/refusal/partial-success phase.** They directly add a claim and an expiring `take_claimed_state` goal. There is no diplomatic response, failure, cooldown after refusal, or route-specific postwar obligation. This is an explicit simplification that has not been recorded as accepted.

8. **Low — category text overstates its present contents.** The category comment/localisation describes Northern settlement, external claims, and postwar handling; it currently contains only the three external claim decisions. Correct the text only alongside the fuller decision implementation so it does not normalize an empty category.

## Decision-category lifecycle

| Category / decision family | Owner and visibility | Current lifecycle | Quality notes |
| --- | --- | --- | --- |
| `ireland_provision` company contracts | IRE; company flags reveal a contract | 25 PP starts 35-day one-shot decision; effect completes once and the decision disappears. | No passive store or repeat farm. Shared one-shot visibility suppresses later company rewards; costs/timers are mechanically identical. |
| `ireland_territorial_policy` | `original_tag = IRE`, `ireland_territorial_policy_open`, not `ireland_route_archived` | Category hides when it has no visible child. The three claim decisions use route flags and issued flags to stage 120 → 122 → 123. | Correct archive gate and no stale target variable. It disappears for non-coercive families and after the restoration Highlands claim, contrary to the planned policy lifecycle. |
| Atlantic claim decisions | Fascist: 120 then 122 then 123. Restoration: 120 only. | 50 PP, 70 days, one issued flag per state, current-controller goal for 180 days. | Claim additions and issued flags prevent duplicate war-goal loops. Goal expiry is present. Completion race and inadequate coercion/readiness policy remain. |

### Mission quality

No new mission IDs exist in the audited expansion decision file. Therefore there is no active decision-owned mission with an owner/category/region/duration/success/failure table to validate. This itself is material: the planned Atlantic postwar settlement mission, its State 120/122 reservation, failure penalty, target cleanup, and duplicate-active prevention are absent.

## State scope, costs, AI, and exploit notes

- **State scope:** State IDs are correct: 120 Scottish Highlands, 122 Wales, 123 Cornwall. The pattern `state -> controller -> ROOT -> create_wargoal { target = PREV }` correctly targets the live controller, matching the vanilla Argentina scope precedent. No automatic external core is granted.
- **New target guard:** Availability now rejects Irish ownership, Irish control, and an Irish faction partner, with a custom tooltip. It does not resolve the timer-completion race above.
- **Cost/timer clarity:** Descriptions correctly state 25/35 for contracts and 50/70/180 for claims. The readiness tooltip now explains peace, readiness, Dublin, manpower, and rifle conditions rather than exposing raw flags. Political Power availability uses strict thresholds correctly (`> 24` for 25, `> 49` for 50).
- **AI validity:** Historical AI is prevented from territorial claims. Non-historical AI can select them with static base `1`, but receives no live target-strength, enemy-faction, naval/supply, reserve, or losing-war evaluation. Company AI has static bases 8/8/8/6; ESB and State Materials are zeroed at war, while transport and merchant procurement are not.
- **Exploit risk:** One-shot company and issued-state flags stop direct repetition; the 180-day goal expires. There is no free-unit loop. The remaining risk is a very cheap early coercion against a stronger controller and a state-controller change during the preparation timer.

## Parliament four-button click/tooltip audit

All four GUI effects invoke exactly one shared executor. Each executor repeats its canonical availability helper before any debit/record effect, so a disabled GUI control cannot bypass the native decision path. The GUI is hidden rather than grey when `ireland_parliament_open` is false (not original IRE, not initialized, or route archived).

| Button | Exact canonical availability | Every reason a visible button is grey/disabled | Tooltip result |
| --- | --- | --- | --- |
| Dáil | Parliament open; stage 1; no `ireland_parliament_dail_session_complete`; Ireland owns State 113. | Wrong stage; Dáil already convened; Dublin not owned. | Existing live rows are exact. It is free. |
| Seanad | Parliament open; `ireland_settlement_open`; `ireland_national_settlement` complete; stage 2+; not completed; government Seanad seats below majority; Dublin owned; PP > 24. | Any failed condition at left, including already holding the Seanad majority or fewer than 25 PP. | Existing live rows are exact. |
| Confidence | Parliament open; `ireland_settlement_open`; `ireland_constitutional_draft` complete; stage 3+; not completed; Dublin owned; PP > 24. | Settlement not open; Constitutional Draft incomplete; early stage; already completed; Dublin lost; fewer than 25 PP. | Corrected: tooltip now contains `GetIrelandParliamentSettlementOpenStatus` as well as all other live conditions. |
| Joint Budget | Parliament open; `ireland_settlement_open`; `ireland_government_formation` complete; stage 4+; not completed; Dáil majority; Seanad majority; Dublin owned; PP > 34. | Settlement not open; Government Formation incomplete; early stage; either chamber lacks majority; already completed; Dublin lost; fewer than 35 PP. | Corrected: tooltip now contains `GetIrelandParliamentSettlementOpenStatus` as well as all other live conditions. |

The prior GUI inspector reports of `GUI_COST_MISMATCH` are a fidelity limitation: it does not follow the GUI wrapper into `ireland_execute_parliament_{seanad,confidence,budget}_action`, where the sole Political Power debit occurs. Do not add direct GUI costs; that would double-charge the action.

## Localisation, UI, and assets

- `GFX_decision_category_ireland_territorial_policy` and all three claim sprites resolve in `interface/ireland_icons.gfx`.
- All audited company/territorial title and description keys exist in BOM-encoded `localisation/english/ireland_l_english.yml`.
- Added: `ireland_atlantic_claim_enforcement_ready_tt`, `ireland_territorial_claim_foreign_controller_requirement_tt`, and the two Parliament settlement-open status keys.
- The Parliament render graph already had no reported button overlap. Its synthetic scenario cannot model Dublin ownership or execute the engine's `buttonstate.lua`, so the visual artifact is layout evidence rather than live click proof.

## Meaningful validation

- Re-read the required offline Paradox wiki pages and vanilla decision/scripted-GUI documentation; used vanilla Argentina's state-controller war-goal scope and vanilla decision cancellation documentation as references.
- `hoi4.focus_inspect` after the restoration patch: `FOCUS_INSPECTED`, validation passed, no blocking focus diagnostic. Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/7e0eabfdfa18c893e4e54a6b6d55a7dda467ae7a4fa5b1fc0ac9625a41aa5e70/53965252c49eeee61ff1554c77c41e7383a50dc4b4f84c34d5062dcce80f1a96/focus-inspect.8ec972db8f4d46b9.json`.
- Map inspection of States 119/120/122/123 passed map membership/adjacency/supply validation. Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/f143143d913f97e09493f9d4cde70e10b36577820e4f079d63404556856a3bc6/168cad3b6244edf0d3d026f6511d3854a80321fcceee58486717c5438198aeb2/map-inspect.2110dd2afe69880a.json`.
- Existing Parliament GUI inspect/render evidence remains useful for the unchanged layout: inspect artifact `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/835292af4eda500db3384eb076c1319b894fc224f753e9c0212358023d2ad109/58245c328e8916e0a5218bfab06e13461faa50a3bf388f3ea9fb76d968721423/gui-inspect.aaf366c6e477c3ec.json`; render artifact `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/164ff927e976510637fb105951264d0a5fb67b5f66108e4a1535f200e6018666/0d9a2fbfc5bc68df48f31fa84d5e6f0ad68e15d5f20c44f31df772354880d9a1/ireland_parliament_decision_ui_window-full.svg`.
- Confirmed each added tooltip/localisation reference is defined exactly once, the English localisation retains UTF-8 BOM, the touched scripted files have balanced braces, and `git diff --check` on the tracked touched sources reports no error.

**Skipped meaningful validation:** No HOI4 runtime session was available for a live timer/controller-change test or a click-state render that injects owned-state data. The audit does not claim those runtime cases are proven.

## Recommended next work

1. Use the accepted addendum's `Decision families`, `AI behavior`, and `Balance and exploit limits` sections as the source for one full territorial implementation plan, including all five family methods, postwar mission/cleanup ownership, target reservations, and state-specific exit paths.
2. Add a completion-time/cancellation contract for each 70-day external claim, with clear cancellation/refund policy before implementation; it must re-check the live controller and faction relation.
3. Replace generic shared one-shot company actions with company-specific results or per-company completion state, beginning with an Aer Lingus aviation action and preserving one bounded result per unlocked concern.
4. Move the external/coercive and company tuning table into shared script constants where fields support them, then update descriptions and AI scenario evidence together.

## Skills used

Applied `hoi4-decisions-missions`, `hoi4-focus-trees` (the restoration focus unlock), and `hoi4-subagents` guidance. No skill was created or changed.

## Final closure — 2026-08-13

The interim omissions above are superseded by the completed implementation:

- all nine company flags own separate one-shot contracts, including Aer Lingus;
- the territorial category owns five Northern instruments, three non-coercive
  Atlantic actions, staged State 119/120/122/123 coercive preparations, and
  route-specific restrictions;
- coercive completion effects re-check the shared readiness contract, the live
  controller, faction relation, and target-controller strength, refunding the
  preparation cost when those conditions change;
- postwar handling includes local-rights, Scottish/Welsh protectorate, and
  Highlands integration outcomes plus a 365-day settlement mission;
- that mission reserves and releases global and postwar mission capacity and
  clears on conclusion, expiry, route cleanup, or loss of every relevant
  controlled-state/subject relation; and
- all four Parliament tooltips expose every canonical availability gate.

Current source closes the eight interim issues and the four recommended
follow-ups. The original sections remain as the evidence trail for the
corrections, not as the current completion verdict.
