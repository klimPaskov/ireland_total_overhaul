# National Situation Ledger Corrective Addendum

> Superseded on 2026-08-15 by `natural_cabinet_briefing_correction_2026-08-15.md` after player review rejected the six-tab and selectable-row presentation.

Date: 2026-08-15
Status: historical and superseded
Feature: Ireland National Situation Ledger and focus-tree inlay
Source specification: `docs/specs/ireland_mechanics_hub/`

## Decision

The feature should receive one corrective pass before closure. The six-family information architecture, canonical action adapters, static inlay art, and public-value policy are sound. The remaining defects are access, selection clarity, consequence clarity, and deterministic review coverage. This addendum does not authorize another mechanic family, another currency, another event chain, a focus-route rewrite, or duplicated gameplay actions.

The accepted feature promise remains unchanged. Every visible value must identify what it measures, what consequence follows from its current state, what changes it, and what the player can do next. The focus inlay remains a compact status surface. The decision-category ledger remains the explanatory and interactive surface.

## Priority and disposition ledger

| ID | Classification | Finding | Required disposition |
| --- | --- | --- | --- |
| NSL-P0-01 | P0 | The current 460 by 248 inlay at `x = -720, y = 10` occupies the same upper-tree footprint as `ireland_cultural_survey` and `ireland_archival_record`. | Move only the inlay declaration to the exact safe position in this addendum, then render the whole tree and prove that nodes, connectors, shortcuts, and the initial camera remain usable. |
| NSL-P0-02 | P0 | Once the National Question tab opens, the hub exposes and enables all six Northern rows. This bypasses the dedicated ledger's focus-by-focus reveal contract. | Make each hub row's visibility and click eligibility mirror the dedicated Northern ledger predicate exactly. A concealed row must not expose its live value or allow selection. |
| NSL-P0-03 | P0 | The interface changes selected tab and row variables but has no persistent selected-tab or selected-row presentation. The player cannot reliably see what will control the explanation or context action. | Add a persistent selected state for the active tab and active row using existing GUI assets or text treatment. Selection must remain visible in normal state, not only on hover. |
| NSL-P0-04 | P0 | Selected-row prose explains general purpose and sources, but it does not consistently identify the current consequence, the currently binding gate, and the next canonical consumer or action. | Add a compact dynamic consequence contract below the selected-row explanation. It must use existing thresholds, flags, focus gates, decisions, missions, and canonical executors only. |
| NSL-P0-05 | P0 | After `ireland_route_archived`, refresh controls remain available in the full hub and focus inlay, while `ireland_refresh_national_situation` intentionally does nothing because `ireland_mechanics_hub_open` fails. | Apply the same open or archived predicate to refresh availability. Archived presentation may stay readable, but the control must be disabled or hidden and explain that the record is closed. |
| NSL-P0-06 | P0 | Current GUI renders do not provide deterministic state evidence. Mutually exclusive status sprites render together when the scenario lacks flags, and selected, disabled, partial-reveal, archive, sealed-evidence, and long-text states are not proven. | Add the named scenario matrix in this addendum and require clean renders at both target resolutions before completion. This is validation data, not new gameplay. |
| NSL-P1-01 | P1 | The inlay's North number is only Integration Capacity, while its status includes consent, British flexibility, security, route preparation, and failure flags. The Culture number is only Cultural Capacity, while its status may be critical because of a revealed evidence disqualifier. | Replace both lone-number summaries with short dynamic public state or bottleneck phrases. Do not invent an aggregate. Keep the individual numbers in the full ledger. |
| NSL-P1-02 | P1 | The refresh wording claims to recalculate every ledger, while the helper deliberately refreshes only the derived public displays and review state in its bounded adapter. | Narrow the player-facing promise to refreshing the displayed national report. Do not broaden the helper into unrelated or side-effecting systems. |
| NSL-Q-01 | Queued | A future engine-safe navigation control could open the already existing dedicated Northern or Evidence review from the corresponding selected row. | Queue only after all P0 items. Adopt only if an existing vanilla or repository pattern can open the exact category without bypassing visibility, cost, or reveal gates. Otherwise leave the explanatory reference in text. |
| NSL-Q-02 | Queued | A small static selector strip may be useful if existing tab and row assets cannot express persistent selection accessibly. | Queue behind an explicit asset-reuse check. If required, route one static asset through `hoi4-feature-assets`. Do not request a new background family. |
| NSL-R-01 | Rejected | Add direct spending buttons, new meter actions, new decision stores, or cloned Parliament, Northern, Provision, Readiness, Foreign, or Evidence executors to make the hub feel more interactive. | Reject. Interactivity must route to the canonical actions and selectors already implemented. |
| NSL-R-02 | Rejected | Add animated tabs, an animated portrait, an animated background, or status loops. | Reject. Static state changes already carry the information and animation would add production cost without resolving a missing state. |
| NSL-R-03 | Rejected | Teach AI to click the dashboard or inlay. | Reject. Both surfaces are human explanation layers. AI must continue using the native focuses, decisions, missions, and scripted effects. |
| NSL-R-04 | Rejected | Repair isolated focus warnings or redesign unrelated focus routes in this pass. | Reject as out of scope. Route those findings to the separate focus-tree audit. |
| NSL-R-05 | Rejected | Expose concealed Evidence values or unrevealed Northern values as a convenience. | Reject. The hub must preserve the dedicated ledgers' public knowledge and progressive disclosure contracts. |

## P0 implementation contract

### NSL-P0-01: safe inlay placement

Change the inlay declaration to:

```txt
position = { x = -600 y = 10 }
```

This is the exact safe replacement for the current authored tree. The current focus layout contains 256 resolved focus positions with horizontal spacing of 96 pixels and vertical spacing of 130 pixels. The replacement footprint is:

- horizontal: `-600` through `-140`
- vertical: `10` through `258`

It occupies the empty upper corridor between:

- the cultural lane at absolute grid `x = -8`, pixel anchor `-768`, containing `ireland_cultural_survey` at row 0 and `ireland_archival_record` at row 1
- the economic lane at absolute grid `x = 0`, pixel anchor `0`, containing `ireland_economic_war_review` at row 0 and `ireland_rural_price_board` at row 1

The footprint ends before row 2 begins at pixel `y = 260`. The neighboring top-row and row-one connectors remain outside the horizontal footprint. Do not move focus nodes to accommodate the inlay. If the tree layout changes after this addendum, re-run the collision review rather than treating `-600, 10` as a permanent universal coordinate.

Acceptance evidence:

- full-tree structural render at the current 96 by 130 spacing
- high-fidelity focus raster or equivalent full focus-view review showing the inlay and decoded focus nodes together
- no overlap with a node, connector, tooltip-critical focus area, shortcut target, or continuous-focus palette
- the `initial_show_position` remains useful at 1920 by 1080 and 2560 by 1440

### NSL-P0-02: Northern progressive disclosure

The hub must reuse or exactly mirror these dedicated-ledger predicates for both row visibility and row click eligibility:

| Hub row | Public value | Exact reveal predicate |
| --- | --- | --- |
| 1 | Unionist Consent | `has_completed_focus = ireland_northern_settlement_ledger` |
| 2 | Nationalist Consent | `has_completed_focus = ireland_northern_settlement_ledger` |
| 3 | Labour Cooperation | `has_completed_focus = ireland_northern_labour_social_bridge` |
| 4 | British Flexibility | `has_completed_focus = ireland_northern_trade_corridor` |
| 5 | Security Stability | `has_completed_focus = ireland_northern_local_authorities` |
| 6 | Integration Capacity | `OR = { has_completed_focus = ireland_northern_federal_preparation has_completed_focus = ireland_northern_unitary_preparation }` |

Overall tab access remains governed by `ireland_mechanics_hub_northern_visible`. That trigger already requires initialization, `ireland_reveal_category_northern`, and completion of `ireland_northern_settlement_ledger`. Do not replace it with a looser flag.

When a later row is concealed, use one of two consistent treatments:

1. Hide the row completely and leave the remaining revealed rows contiguous.
2. Show a locked placeholder that names the exact focus which opens the row, but never includes the live variable or permits selection.

Use the same treatment for all four later rows. Hiding is preferred if rearranging rows does not create misleading blank hit regions. If a previously selected Northern row becomes invalid because a route state closes, reset the hub selection to the first currently visible row or `row_none` before dispatching an action.

### NSL-P0-03: persistent selection hierarchy

The full ledger needs two persistent state cues:

- Active tab: one visible selected treatment on exactly one of the six fixed tabs.
- Active row: one visible selected treatment on the current row when `selected_row` is not `row_none`.

The selected state must not rely on color alone. Pair a color or brightness difference with at least one shape, border, underline, label prefix, or marker. Reuse existing sprites and fonts first. Keep all six tabs present even while a family is locked so the player can learn the feature map. A locked tab may be selected for explanation, but it must display the locked summary and exact unlock condition.

Click regions must match their visible elements. Hidden Northern rows and absent family rows must not retain invisible clickable areas.

### NSL-P0-04: selected-row purpose and consequence contract

Retain the existing descriptive paragraph. Add one dynamic block that answers these three state-dependent questions without repeating the family-wide purpose line:

1. Current consequence: what is enabled, constrained, capped, at risk, or institutionally locked right now.
2. Binding gate: the named threshold, bottleneck, focus, flag-backed review, failure state, or public reveal which currently matters.
3. Next canonical route: the existing focus, decision family, mission, review, or guarded hub action which can change or use the value.

The block must follow these family rules:

| Family | Current consequence rule | Binding gate rule | Next-route rule |
| --- | --- | --- | --- |
| State | Name the active Parliament stage while the opening programme remains incomplete. After it completes, identify the selected value's nearest currently active political, crisis, territorial, or conclusion consumer. | Use existing Parliament stage flags, political gate constants, crisis flags, and route gates. Do not imply that every high value is universally good. | Point to the existing Parliament action during the opening sequence, then name the relevant focus, decision, mission, or review. Do not add a generic resource grant. |
| Provision | State whether the selected component is the lowest component or is causing an aggregate cap. | Use the existing public baseline, aggregate, bottleneck, and cap helpers. | Name the existing Provision decision or focus family which changes that component. The hub action remains recompute and select, not a grant. |
| Readiness | State whether the component is the lowest value, an equipment bottleneck, a supply bottleneck, or another authored operational bottleneck. | Use the existing readiness bottleneck triggers and public thresholds. | Name the existing readiness, defence, procurement, command, warning, maritime, or intelligence route which changes the selected component. |
| Foreign | Keep British, American, German, and Vatican leverage neutral unless a concrete current gate consumes them. Apply warning or critical language to Exposure, Sponsor Dependence, active incidents, and failure flags. | Use documented channel visibility, neutrality incidents, exposure, dependence, and sponsor failure checks. | Name the existing diplomatic focus, agreement, incident response, or safeguard action. The hub action may select the greater autonomy risk, but must not award leverage. |
| National Question | Only evaluate revealed rows. State the selected value's role in the current settlement stage and whether a settlement or occupation failure overrides it. | Use the exact progressive-reveal focus predicate plus the dedicated ledger's readiness thresholds and failure flags. | Route through the canonical Northern review executor and name the currently relevant focus, decision, mission, or convention step. |
| Culture | Distinguish public capacity rows from the Evidence Record. Before evidence reveal, state that the evidence row is sealed. After reveal, name a public disqualifier or accepted obligation only when the dedicated Evidence system makes it public. | Use Cultural Survey, archive and evidence visibility, public component values, credible evidence, disqualifier state, and accepted obligation state. | Route public rows to existing cultural decisions and focuses. Route revealed evidence to the canonical Evidence Review. Never reveal evidence through the hub. |

The text direction is administrative, specific, and present-tense. It should name institutions and consequences, not implementation details. Final localisation must fit the current detail area at both target resolutions. If a state has no current consumer, say that the record is stable and identify the next authored unlock rather than inventing urgency.

### NSL-P0-05: archived action contract

All hub and inlay controls that call `ireland_refresh_national_situation`, `ireland_execute_next_state_action`, or the tab context dispatcher must require the same open-state contract as the helper they call. At minimum this includes `NOT = { has_country_flag = ireland_route_archived }` through `ireland_mechanics_hub_open` or a shared equivalent.

Archived values may remain visible as a closed record if the existing category visibility permits it. In that state:

- no control may look available and then do nothing
- refresh must be hidden or disabled
- State action must be hidden or disabled
- tab context action must be hidden or disabled
- the explanation must state that the national record is closed and read-only

Do not remove history variables or clear the selected tab merely to create the archived view.

### NSL-P0-06: deterministic scenario matrix

Add review scenarios that supply enough variables, flags, completed focuses, and scripted visibility state for the renderer to resolve mutually exclusive sprites and dynamic text. The scenario data is test evidence only.

| Scenario | Required state proof |
| --- | --- |
| `ireland_mechanics_hub_opening_locked` | Six permanent tabs, locked family summaries, no invisible row hit regions, exact unlock wording. |
| `ireland_mechanics_hub_provision_bottleneck` | Provision selected, one weakest component, aggregate cap explanation, persistent selected tab and row. |
| `ireland_mechanics_hub_readiness_bottleneck` | Readiness selected, equipment or supply bottleneck, correct status and next route. |
| `ireland_mechanics_hub_foreign_imbalance` | Bilateral leverage remains neutral, Exposure or Dependence receives risk language, only one family status sprite is visible. |
| `ireland_mechanics_hub_northern_partial` | Settlement Ledger complete, rows 1 and 2 visible, rows 3 through 6 concealed and not clickable. |
| `ireland_mechanics_hub_northern_midroute` | Labour, British, and Security rows appear only as their exact focuses complete. Integration remains concealed until federal or unitary preparation. |
| `ireland_mechanics_hub_evidence_sealed` | Cultural family public, Evidence row sealed, no hidden evidence count or action. |
| `ireland_mechanics_hub_evidence_revealed` | Evidence public, public disqualifier or obligation affects status and consequence text without changing Cultural Capacity by implication. |
| `ireland_mechanics_hub_archived` | Values readable where intended, all action and refresh controls disabled or hidden, no no-op affordance. |
| `ireland_mechanics_hub_long_text` | Long consequence, gate, requirements, and tooltip content stays within its intended scroll or text bounds. |
| `ireland_focus_inlay_operational` | Six summaries resolve to one status icon each, North and Culture use public state phrases, both controls match availability. |
| `ireland_focus_inlay_archived` | No refresh or State action no-op and no misleading current-action promise. |

Render the full ledger and inlay at 1920 by 1080 and 2560 by 1440. Include normal, hover, selected, locked, disabled, warning, active, completed, minimum-value, maximum-value, long-text, and missing-localisation review states where they apply. A generic state render without scenario variables is not sufficient evidence for the mutually exclusive status contract.

## P1 presentation corrections

### NSL-P1-01: truthful North and Culture summaries

The focus inlay must not present Integration Capacity as if it explains the full National Question status. Use a short public state phrase derived from the most important currently visible condition. Priority order is failure state, unrevealed or locked state, current settlement bottleneck, then ready state. The phrase may name Security, British flexibility, consent, preparation, or failure, but it must not expose a concealed row.

The Culture summary must not present Cultural Capacity as if it explains a status driven by public evidence disqualification. Before Evidence reveal, show the public capacity or a sealed-evidence state. After reveal, prioritize a public evidence disqualifier, accepted obligation, or evidence-readiness state over the raw capacity number when that condition controls the status.

Do not create a North aggregate or Culture aggregate. The full ledger remains the numeric source of truth.

### NSL-P1-02: bounded refresh promise

Use player-facing wording that describes refreshing the displayed report and its derived public summaries. Avoid a claim that every ledger or every system is recalculated. The helper should remain idempotent and must not trigger costs, rewards, hidden evidence reveal, mission progress, foreign agreement changes, Parliament spending, or Northern settlement progress.

## Historical and regional design basis

This corrective pass does not add new historical claims. It preserves the feature's existing Irish institutional anchors:

- Dáil and Seanad procedure for State authority
- provisioning, transport, maritime access, and administrative reach for the material capacity of a small island state
- neutrality enforcement and bilateral channels for foreign pressure
- distinct unionist, nationalist, labour, British, security, and administrative conditions for the National Question
- language service, archives, regional participation, and site stewardship for cultural administration

The design value of these connections is that each number belongs to an institution or contested public process. The corrective pass should make that relationship visible rather than adding lore text or another abstract meter. Repository implementation and localisation are the source of truth for these anchors. Vanilla focus-inlay and scripted-GUI precedents provide the presentation model. No external quote, slogan, cultural remark, or audio research package is needed.

## Implementation surfaces

The main implementation pass is expected to inspect and may need to update:

- `common/national_focus/ireland_focus_tree.txt`
- `common/scripted_guis/ireland_scripted_guis.txt`
- `common/scripted_triggers/ireland_mechanics_hub.txt`
- `common/scripted_effects/ireland_mechanics_hub.txt`
- `common/scripted_localisation/ireland_localisation.txt`
- `common/focus_inlay_windows/ireland_national_situation_inlay.txt`
- `interface/ireland_national_situation.gui`
- `interface/ireland_national_situation_inlay.gui`
- `localisation/english/ireland_l_english.yml`
- `docs/ireland_national_situation_ledger.md`
- `docs/specs/ireland_mechanics_hub/value_purpose_matrix.md`
- feature GUI scenario or review manifests used by `hoi4.gui_inspect` and `hoi4.gui_render`

No gameplay balance constants need to change for this addendum. If new shared triggers are introduced solely to mirror row visibility or open-state availability, prefer one reusable trigger per contract over duplicating predicates across GUI surfaces. Do not alter the underlying values, thresholds, costs, rewards, or AI weights unless a separate audit proves an existing defect.

## Acceptance criteria

The corrective pass is complete only when all of the following are true:

- The inlay uses `x = -600, y = 10` and full focus-view evidence proves that its 460 by 248 footprint is clear.
- Every Northern hub row uses the exact dedicated-ledger reveal predicate for both visibility and click eligibility.
- Exactly one tab has a persistent selected presentation, and at most one visible row has a persistent selected presentation.
- Every selected row can present its current consequence, binding gate, and next canonical route without exposing hidden state.
- Archived controls never remain clickable when their helper will do nothing.
- North and Culture inlay summaries do not imply that a lone variable explains a multi-factor status.
- Refresh wording matches the bounded idempotent helper.
- Each status group resolves to exactly one ready, warning, critical, or locked icon in every named scenario.
- The full ledger and inlay pass the named scenario matrix at both target resolutions.
- Existing canonical costs, reveal gates, mission progress, decision availability, and AI behavior remain unchanged.
- No new mechanic family, currency, duplicated executor, animation package, or direct hidden-value exposure has been added.

## Stop condition and promotion

After the P0 and P1 items are implemented and the named scenario evidence is clean, stop the improvement loop for this feature. Additional meters, actions, routes, art families, or lore layers would add bloat rather than clarify the existing six-family system.

This file remains in `docs/plans/ireland_mechanics_hub/improvement_loop/` while any P0 or P1 item is unresolved. Once accepted and implemented, merge the durable contracts into:

- `docs/specs/ireland_mechanics_hub/ireland_mechanics_hub_spec.md`
- `docs/specs/ireland_mechanics_hub/value_purpose_matrix.md`
- `docs/ireland_national_situation_ledger.md`

Then mark this addendum implemented or superseded in the documentation handoff. Do not write another improvement addendum for the National Situation Ledger until this one is implemented, explicitly queued with a reason, or rejected with a reason.

## Closure disposition (2026-08-15)

The corrective pass is implemented in the current source and frozen review evidence. Durable rules are promoted into `docs/specs/ireland_mechanics_hub/ireland_mechanics_hub_spec.md`, `docs/specs/ireland_mechanics_hub/value_purpose_matrix.md`, and `docs/ireland_national_situation_ledger.md`.

| Item | Disposition | Current evidence |
| --- | --- | --- |
| NSL-P0-01 | Implemented | `common/national_focus/ireland_focus_tree.txt` uses `x = -600, y = 10`; focus inspection revision `90beeec44304c287` resolves 256 focuses and 234 connectors with zero crossings, node intersections, long connectors, and too-close pairs. |
| NSL-P0-02 | Implemented | `common/scripted_triggers/ireland_mechanics_hub.txt` mirrors the dedicated Northern focus predicates for row visibility, and scripted-GUI click eligibility derives from those row predicates. |
| NSL-P0-03 | Implemented | The six tabs and visible-row selectors use persistent state conditions and the registered static tab/row marker sprites. |
| NSL-P0-04 | Implemented | The selected-row detail, consequence, binding-gate, next-route, purpose, and live-requirement text is wired through the mechanics-hub scripted localisation and dashboard layout. |
| NSL-P0-05 | Implemented | `ireland_mechanics_hub_open` gates dashboard refresh/context controls and the inlay buttons; archived presentation remains readable while active actions are disabled. |
| NSL-P0-06 | Implemented | Final GUI inspection revisions `f8fc5fbe5ea0d72c` (dashboard) and `33f76c15e0ae8ae6` (inlay) report no blockers after the deterministic state and resolution review. |
| NSL-P1-01 | Implemented | `GetIrelandMechanicsHubInlayNorthern` and `GetIrelandMechanicsHubInlayCulture` select public locked, failure, bottleneck, ready, warning, archived, or evidence-state phrases rather than treating one raw component as the full status. |
| NSL-P1-02 | Implemented | Refresh localisation promises only the displayed Provision, Readiness, operational, Northern, and cultural projections and explicitly states that it grants no value, reward, or progress. |
| NSL-Q-01 | Queued | No cross-category navigation control was added; retain explanatory routing until a proven engine-safe pattern can preserve category, cost, and reveal gates. |
| NSL-Q-02 | Superseded by existing assets | The registered static tab underline and row marker satisfy persistent selection; no selector strip is needed. |
| NSL-R-01 through NSL-R-05 | Rejected | No cloned executors, animation family, AI GUI path, unrelated route redesign, or concealed-value exposure was introduced. |

This file remains as the historical corrective plan and closure record. The queued navigation question is the only active design follow-up; it does not reopen the implemented six-family feature.
