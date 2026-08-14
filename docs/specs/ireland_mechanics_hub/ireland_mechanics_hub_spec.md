# Ireland National Situation Ledger specification

## 1. Purpose

Ireland has several connected systems, but their presentation currently forces the player to remember individual values across focuses, decisions, event options, and tooltips. The National Situation Ledger turns those systems into a single readable control surface.

Every displayed value must answer four questions:

1. What does this measure?
2. What does a high or low result change?
3. What improves or damages it?
4. What can the player do next?

If a value cannot answer those questions, it must remain internal or be retired from gameplay rather than displayed as decorative arithmetic.

## 2. Player-facing information architecture

The hub has six tabs. The tab count is fixed so the player can build a stable mental model.

| Tab | Summary | Components | Primary consequence |
| --- | --- | --- | --- |
| State | National Settlement | Social Consent, Neutrality Integrity, Administrative Reach, Dáil Mandate | Government legitimacy, institutional actions, route and conclusion gates |
| Provision | National Provision | Food, Energy, Transport, Maritime Access | Civilian projects, crisis resilience, supply and route-conclusion capacity |
| Readiness | National Readiness | Command, Equipment, Mobilisation, Supply, Warning, Maritime Protection, Intelligence | Security missions, military projects, coercive instruments and wartime resilience |
| Foreign | Foreign Exposure | British, American, German and Vatican Leverage; Sponsor Dependence | Diplomatic options, neutrality pressure, sponsor risk and foreign-response outcomes |
| National Question | Northern settlement state | Unionist Consent, Nationalist Consent, Labour Cooperation, British Flexibility, Security Stability, Integration Capacity | Lawful settlement, territorial instruments, integration and recovery |
| Culture | Cultural Capacity | Language Service, Archival Record, Regional Participation, Site Stewardship, Evidence Status | Cultural programmes, public knowledge and exceptional-route proof |

The dashboard always shows the tab names. Locked systems explain the exact focus or institutional milestone that opens them. Values do not vanish merely because they are currently weak.

## 3. Full dashboard

### 3.1 Entry point

A new decision category, `ireland_national_situation`, is visible after `ireland_initialized`. It has `visible_when_empty = yes`, high priority, and owns `ireland_national_situation_scripted_gui`.

The GUI window is `ireland_national_situation_window`, sized for the existing 510 by 590 conditions background. It uses `context_type = decision_category`, `dirty = ireland_conditions_gui_dirty`, and disables AI GUI clicks. Native decisions and shared executors remain the AI surface.

### 3.2 Layout

The 510 by 590 window contains:

- a title, concise instruction, and current overall warning marker;
- six persistent tab buttons;
- a summary card with the current tab's governing value and status;
- up to eight clickable rows, enough for the Readiness family without scrolling;
- a selected-value explanation panel;
- an exact “purpose” line naming the decisions, missions, routes, or gates affected;
- a guarded context action;
- a refresh action that recomputes derived displays and ledgers without granting a reward.

Rows are selection controls, not disabled reward buttons. Their normal visual state must remain legible. Locked mechanics use a separate lock marker and explanatory text rather than a grey label with no reason.

### 3.3 Colour language

The visual vocabulary is consistent across the dashboard, focus inlay, Parliament, Northern ledger, and Evidence ledger:

- green: the current gate is satisfied or the value is safely above its operational threshold;
- amber: the value is usable but is the current bottleneck or is close to a gate;
- red: an active gate fails, a process is blocked, or a route disqualifier is present;
- grey lock: the mechanic has not been institutionally revealed and the tooltip names the reveal condition;
- white/cream: descriptive text and values that are directional rather than inherently good or bad, especially individual foreign leverage scores.

Foreign leverage is not coloured green merely because it is high. The summary uses Foreign Exposure and Sponsor Dependence to express risk; the four bilateral values remain neutral and explain which actions they enable or constrain.

### 3.4 Selected-value explanation

Each row selection provides:

- definition in plain language;
- current value and important threshold bands;
- direct consumers, expressed as named player-facing focuses, decisions, missions, or conclusions;
- common positive sources;
- common negative sources;
- the current next gate where one exists.

The explanation must describe current gameplay, never implementation history or internal variable names.

## 4. Interactive actions

The hub exposes two action slots.

### 4.1 Refresh national report

`ireland_refresh_national_situation` recomputes Provision, Readiness, operational state, Northern records, cultural evidence, and dirty variables through existing shared helpers. It has no reward, no cost, and no hidden state advance.

### 4.2 Context action

The context action changes by tab and is always backed by an existing canonical trigger/executor:

- State: perform the next available parliamentary programme step through the same four guarded Parliament executors. If none is available, the button is disabled and the tooltip states the missing focus, majority, PP, ownership, or prior step.
- Provision: refresh the capacity report and select the weakest Provision component. It does not add points.
- Readiness: refresh the capacity report and select the weakest Readiness component. It does not add points.
- Foreign: review current exposure and sponsor dependence; this is informational and does not create diplomatic leverage.
- National Question: call the same Northern review helper used by the dedicated ledger, only when its canonical review trigger passes.
- Culture: call the same Evidence inspection helper when revealed; otherwise review ordinary cultural capacity without exposing concealed evidence.

Shared scripted effects own the actions. The dashboard and focus inlay never duplicate rewards, costs, or route logic.

## 5. National-focus inlay

### 5.1 Engine surface

The focus tree declares `ireland_national_situation_inlay` through the vanilla `focus_inlay_windows` system. The definition lives in `common/focus_inlay_windows/ireland_national_situation_inlay.txt`; the rendered window lives in `interface/ireland_national_situation_inlay.gui`.

It is `internal = yes`, visible for the original Ireland tag after initialization, and never conceals focus branches.

### 5.2 Placement

The inlay occupies the deliberately empty upper gap between the opening political trunk and the economic/defence trunks. It must not cover a focus node, connector, shortcut, or the initial camera target. Its final pixel position is accepted only after focus render and raster review.

### 5.3 Information and actions

The compact inlay shows six colour-coded summaries:

- Settlement;
- Provision;
- Readiness;
- Neutrality;
- Northern settlement;
- Cultural capacity/evidence.

It has two scripted buttons:

- Refresh report, calling the same idempotent refresh helper as the full hub;
- Next state action, calling the same next-parliament-step helper and available only when a canonical parliamentary action is available.

Every summary has a tooltip naming its purpose and directing the player to the National Situation decision category for component detail.

## 6. State and lifecycle

The feature adds only presentation state:

- `ireland_mechanics_hub_selected_tab`;
- `ireland_mechanics_hub_selected_row`;
- optional cached row/status frames if required by the GUI renderer.

The first tab is selected during campaign initialization. Existing `ireland_conditions_gui_dirty` is the shared dirty counter. Every effect that changes a displayed value must already or newly dirty this counter. Cleanup removes selection-only state when Ireland is archived or no longer valid, without clearing gameplay ledgers.

## 7. AI contract

The dashboard and inlay use `ai_enabled = no` or the inlay equivalent. AI continues to use native decisions, focus plans, and canonical executors. A human-facing action is acceptable only if an AI-accessible native path already exists or the action is a pure refresh with no gameplay benefit.

## 8. Localisation contract

All visible labels, values, lock reasons, status explanations, action requirements, and tooltips are localised in English with UTF-8 BOM. The hub uses scripted localisation for tab/row-specific detail and status text. It does not expose internal flag or variable identifiers.

## 9. Asset contract

The implementation reuses the existing 510 by 590 National Conditions background and the shared value-row, compact-row, action-button, lock, warning, critical, and ready sprites. New art is created only if the reuse pass cannot express the state vocabulary clearly.

The focus inlay uses vanilla tiled panel framing plus the registered Ireland status sprites. Static state is always readable; animation is optional and may only communicate a real warning or completed-state transition. Transform-only animation is forbidden.

## 10. Acceptance scenarios

1. Opening: State is readable immediately; unrevealed tabs remain present with exact unlock explanations.
2. Weak Provision: the aggregate and weakest component are amber/red, the detail explains affected actions, and refresh does not grant points.
3. Weak Readiness: the governing minimum and failed military gates are named.
4. Foreign imbalance: bilateral leverage remains neutral while exposure/dependence carries risk colour.
5. Northern opening: the summary activates, its six rows match the dedicated ledger, and review uses the same helper.
6. Evidence concealed: the Culture tab shows ordinary cultural capacity and a locked evidence row without leaking hidden content.
7. Evidence revealed: the evidence summary and inspection action match the dedicated ledger.
8. Parliament: the inlay and dashboard next-step button enable under the same trigger as the Parliament button and call the same executor.
9. Archived route: no direct action remains available; values remain readable when the country remains Ireland.
10. Focus layout: the inlay covers no node or connector at normal UI scale and does not change focus prerequisites, rewards, filters, or AI.

## 11. Completion boundary

Completion requires the decision category, scripted GUI, focus inlay, shared triggers/effects, dynamic localisation, asset wiring, focus declaration, initialization, cleanup, AI-equivalent paths, GUI inspection at 1920x1080 and 2560x1440, focus render/raster review, documentation, and independent audits. No placeholder art or unexplained displayed value is accepted.

