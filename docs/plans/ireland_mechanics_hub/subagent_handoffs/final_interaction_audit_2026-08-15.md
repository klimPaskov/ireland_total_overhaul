# National Situation Ledger: final interaction audit

Date: 2026-08-15
Scope: decision category, scripted GUI, shared mechanic-hub adapters, and focus inlay
Status: one bounded interaction-safety patch applied; no commit created

## Changed files and identifiers

- `common/scripted_triggers/ireland_mechanics_hub.txt`
  - `ireland_mechanics_hub_row_one_visible`
  - `ireland_mechanics_hub_row_two_visible` (inherits row one)
  - `ireland_mechanics_hub_row_three_visible`
  - `ireland_mechanics_hub_row_four_visible`
  - `ireland_mechanics_hub_row_five_visible`
  - `ireland_mechanics_hub_row_six_visible`

Each Northern branch now requires `ireland_mechanics_hub_northern_visible = yes` in addition to its pre-existing tab and focus predicate.

Before this patch, completed Northern focuses could leave their hub rows visible and selectable after the parent National Question surface had ceased to be public, including the archived-route state. The row click gates reuse these visibility triggers, so the rows also retained selection hit regions. The context action itself was already disabled while archived, but those selectors could still reveal values that the hub-level contract had closed.

After this patch, the overall public Northern contract is required before any Northern row appears or can be clicked. The dedicated focus progression remains exact:

| Hub row | Dedicated predicate retained |
| --- | --- |
| Unionist Consent / Nationalist Consent | `ireland_northern_settlement_ledger` |
| Labour Cooperation | `ireland_northern_labour_social_bridge` |
| British Flexibility | `ireland_northern_trade_corridor` |
| Security Stability | `ireland_northern_local_authorities` |
| Integration Capacity | `ireland_northern_federal_preparation` or `ireland_northern_unitary_preparation` |

The extra shared gate adds initialization, the existing `ireland_reveal_category_northern` contract, and its non-archived route state. It neither changes a Northern cost, reward, threshold, focus requirement, nor review result.

## Findings, ordered by severity

### P0 fixed — Northern row reveal/click parity outside the public ledger lifecycle

The generic Northern row branches did not require `ireland_mechanics_hub_northern_visible`. This was inconsistent with the declared top-level ledger visibility and the P0-02 archival/reveal contract. The patch above closes that path; GUI element visibility and `_click_enabled` both derive from the corrected row predicates.

### P1 remaining, out of this audit's permitted edit scope — inlay North/Culture state phrasing

The corrective addendum requires public state or bottleneck phrases, but the current dynamic localisation still selects:

- `ireland_focus_inlay_northern_open`: `North Stage [?ireland_northern_integration_stage|0]/5`;
- `ireland_focus_inlay_culture_revealed`: raw Cultural Capacity plus a credible-evidence count.

`GetIrelandMechanicsHubInlayCulture` does not prioritize a revealed public disqualifier or accepted obligation, and `GetIrelandMechanicsHubInlayNorthern` has no failure/locked/bottleneck/ready priority. This is the existing P1-01 item, not a new decision-system design issue. It needs the localisation-owned surfaces `common/scripted_localisation/ireland_localisation.txt` and `localisation/english/ireland_l_english.yml`, which were explicitly outside this subtask's editable file list.

### P1 remaining, out of scope — archived Northern summary wording

`GetIrelandMechanicsHubSummary` locks Northern only when `ireland_northern_settlement_ledger` is incomplete. Once that focus is complete, an archived player can select the tab and receive the historical stage summary while its status marker and rows are locked. The category is intended to retain readable historical values after archival, so this does not leave an executable action; however, the localisation should deliberately label that summary as archival/closed if the parent wants the marker and text to agree. This is a presentation follow-up in the same localisation-owned surface.

### P1 validation gap — no deterministic scenario fixture or GUI MCP endpoint available

The named scenario matrix exists only in `docs/plans/ireland_mechanics_hub/improvement_loop/national_situation_ledger_corrective_addendum_2026-08-15.md`; no runnable scenario manifest was present. No `hoi4.gui_inspect` or `hoi4.gui_render` endpoint was registered in this agent session, so visual state rendering at the two required resolutions was not possible here. The parent should retain the addendum's scenario/render requirement before final feature closure.

## Decision category lifecycle notes

- `ireland_national_situation` is visible for original-tag Ireland after `ireland_initialized`, including when its decision list is empty. It does not disappear on archive so the record can remain readable.
- `ireland_mechanics_hub_open` centralizes active-state eligibility as initialized Ireland plus `NOT = { has_country_flag = ireland_route_archived }`.
- Full GUI refresh and context controls use that open trigger. The focus-inlay refresh directly uses it; its State action uses `ireland_next_state_action_available`, which also requires it.
- Initialization sets the selected tab to State and selected row to none. `ireland_cleanup_route_state` restores that presentation-only state and dirties the panel; it does not clear gameplay ledgers.
- Tabs are intentionally selectable when a family is locked, which is required so their unlock explanation stays available. Row selection is only enabled when the corresponding visible row exists.

## Click, cost, and canonical-path audit

| Surface/control | Availability and result | Audit result |
| --- | --- | --- |
| Six hub tabs | Initialized original Ireland; set only presentation tab/row state and dirty the panel | Safe selector actions; no cost or reward path. |
| Seven hub rows | Family/row visibility; set only selected row and dirty the panel | Safe selectors. Northern now exactly mirrors public + focus reveal predicates. |
| Hub Refresh | `ireland_mechanics_hub_open` → `ireland_refresh_national_situation` | Idempotent display recomputation only; no reward, progress, cost, or hidden reveal. Disabled after archive. |
| Hub State context | `ireland_next_state_action_available` → the four canonical Parliament executors | Preserves each native decision's current stage, PP, ownership, majority, completion, and archival gates. |
| Hub Provision / Readiness context | Open revealed family → canonical recompute then deterministic lowest-component selection | No capacity/readiness grant; only recomputes derived display/caps and changes selection. |
| Hub Foreign context | Open revealed family → selects higher of Exposure/Dependence | Informational only; no leverage, foreign access, or agreement state is granted. |
| Hub Northern context | Open + public Northern tab + visible selection → existing review-request/synchronizer path | Projects the selected public row into the dedicated ledger and invokes the same request consumer. No cloned review effect. |
| Hub Culture context | Open public Culture → public review; a revealed Evidence Record uses the existing inspection request/synchronizer | Concealed evidence has no inspection action and no value exposure. |
| Inlay Refresh / State action | Same `ireland_refresh_national_situation` / `ireland_execute_next_state_action` helpers with the same availability | Canonical parity with the dashboard; both unavailable after archive. |

The native Parliament decisions retain their own `ai_will_do` path and each uses the same executor called by the hub and inlay. The full scripted GUI has `ai_enabled = { always = no }` and `ai_check = { always = no }`; focus-inlay buttons have no AI scripting surface in the documented vanilla inlay schema. No GUI-only AI action was introduced.

## Mission quality notes

No mission is created, activated, cancelled, timed, or rewarded in this scoped ledger adapter. The only review-like interaction is owned by the existing Northern and Evidence ledgers: it passes their selection/request flags to their established synchronizers. Consequently there is no new owner/category/region/duration/success/failure/duplicate mission risk in this patch.

## Localisation and tooltip notes

Every clickable full-ledger control has a named tooltip. State-action tooltips resolve the same live Parliament requirement localisation used by the native path; Refresh reports its archival unavailability. The remaining P1 inlay phrase and archived-summary issues above must be resolved in the localisation-owned files before declaring the corrective addendum complete.

## Cleanup and exploit-risk notes

- No new resource, unit, equipment, factory, claim, core, war-goal, or mission reward is introduced; no farming loop is created.
- Every active action checks the open-state contract directly or through its canonical availability trigger, so archived buttons cannot execute a no-op helper.
- The Northern patch removes a stale post-archive selector path. Selection remains reset to State/none during route cleanup.
- The Northern core review remains behind its existing final-review, threshold, controlled-state, resistance, failure, and once-only guards; the hub does not weaken them.

## Meaningful validation performed

- Mapped all 15 full-ledger button names in `interface/ireland_national_situation.gui`; each has a matching scripted GUI click effect and `_click_enabled` trigger.
- Mapped both inlay button names in `interface/ireland_national_situation_inlay.gui`; each has a declared `available` block and canonical `click_effect` in `common/focus_inlay_windows/ireland_national_situation_inlay.txt`.
- Traced all hub/inlay action call sites to `ireland_refresh_national_situation`, `ireland_execute_next_state_action`, `ireland_execute_mechanics_hub_context_action`, and the existing Northern/Evidence request consumers.
- Compared each Northern hub row to the dedicated `ireland_northern_settlement_ledger_scripted_gui` focus predicates, then confirmed `_click_enabled` derives from the same corrected hub row trigger.
- Confirmed the route-archived path fails `ireland_mechanics_hub_open`, disabling refresh, context action, and inlay State action without clearing historical variables.

## Skipped meaningful validation

- Scenario-driven render/inspection at 1920x1080 and 2560x1440: no scenario fixture was present and no HOI4 GUI MCP endpoint was available in this session.
- In-game execution: not run from this audit environment; the static call-path review is not a substitute for the addendum's required visual scenario evidence.

## Simplifications, blockers, and parent follow-up

No gameplay simplification was made. The only patch is the local public-reveal/click-parity fix above. The current corrective addendum already owns the outstanding P1 presentation and scenario-render requirements; no new improvement plan was written.

## Documentation reconciliation closure appended 2026-08-15

The findings above remain the historical audit snapshot. Subsequent parent implementation evidence and source review supersede the prior P1 presentation and render-gap wording for documentation status:

- current scripted localisation exposes the National Question and Culture inlay through public locked, failure, bottleneck, ready, warning, archived, and evidence-state phrase dispatch;
- current source keeps archived controls unavailable through `ireland_mechanics_hub_open`, preserves progressive Northern row visibility/click parity, and renders persistent tab/row selection markers;
- focus inspection revision `90beeec44304c287` and GUI inspection revisions `5cfb9c81e35e17db` / `7f7b1126f87a3ebc` are the frozen evidence references for the reconciled feature status;
- the corrective addendum is now marked implemented, with only the explicitly queued cross-category navigation question remaining open.
