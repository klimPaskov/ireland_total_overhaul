# Parliament start-visibility handoff

Date: 2026-08-09

Feature: `ireland_focus_tree`

Scope: bounded start-of-campaign visibility repair for the Settlement and
Government decision category and its Parliament summary.

## Issue list, sorted by severity

### High — no Parliament summary at campaign start

`ireland_settlement_government` required
`ireland_reveal_category_settlement`, which requires the
`ireland_settlement_open` flag. The only writer for that flag is the later
`ireland_state_still_defined` focus. The normal initializer had already set
the Dáil/Seanad variables, `ireland_parliament_gui_dirty`, and
`ireland_initialized`, but neither the decision category nor its embedded GUI
could appear before that focus.

`visible_when_empty = yes` was already present, so the empty-category rule was
not the blocker. The actual lifecycle gate was the shared action-family reveal.

### Low — summary and interaction reveal were coupled

`ireland_parliament_open` inherited `ireland_reveal_settlement_open`. That
made a read-only chamber summary depend on the same later focus reveal as the
native actions below it.

## Changed files and identifiers

- `common/decisions/categories/ireland_categories.txt`
  - `ireland_settlement_government`
  - Its `visible` block now calls `ireland_parliament_open = yes`.
- `common/scripted_triggers/ireland_parliament.txt`
  - `ireland_parliament_open`
  - Requires `original_tag = IRE`, `ireland_initialized`, and no
    `ireland_route_archived` flag.

No initialization, decision, GUI, interface, or localisation file changed.

## Lifecycle behavior before and after

Before, campaign initialization populated the Parliament ledger, then the
category and GUI remained hidden until `ireland_state_still_defined` set
`ireland_settlement_open`. If no native Parliament action was visible, the
category stayed absent despite its `visible_when_empty` setting.

After normal `ireland_initialize_campaign` execution, original-tag `IRE` sees
the Settlement and Government category and `ireland_parliament_decision_ui`
as soon as `ireland_initialized` exists. The category remains visible with no
native action because it retains `visible_when_empty = yes`. Native actions
remain separately gated by `ireland_reveal_settlement_open` and their existing
stage, cost, capital-control, and completion checks. The summary closes when
`ireland_route_archived` is set, preserving the existing route-cleanup intent.

## Decision-category lifecycle notes

- Owner/category: `IRE` / `ireland_settlement_government`.
- Start state: initialization creates the chamber variables and
  `ireland_initialized`; the category and summary now reveal at that point.
- Action state: the four Parliament actions still open only through the later
  `ireland_settlement_open` route gate.
- Terminal state: `ireland_route_archived` hides the category through
  `ireland_parliament_open`, hides the GUI through its existing visible block,
  and removes native Parliament actions through their existing triggers.

## Mission quality notes

No mission is owned by this patch. The visible surface is a read-only
decision-category summary; it starts no timer and adds no duplicate mission
path. The native Parliament actions and their existing progress stages were
not changed.

## Cost, requirement, AI, and route-lock notes

- Costs and requirement tooltips are unchanged. This patch does not make a
  native decision available: each action still requires
  `ireland_settlement_open` in addition to its prior conditions.
- The summary has no scripted-GUI clicks or AI effect path. Existing native
  `ai_will_do` values remain untouched.
- The new summary gate is valid only for the original IRE tag after
  initialization. It retains the `ireland_route_archived` route lock, so it
  cannot persist after route archival.

## Localisation, tooltip, cleanup, and exploit-risk notes

- No player-facing key changed and no localisation gap was introduced.
- No trigger tooltip changed because the patch changes category visibility,
  not action availability.
- No stale target, variable, mission, or GUI-button cleanup is introduced.
  The existing archival flag remains the single cleanup gate for the summary.
- No equipment, unit, political-power, or mission-success loop changes; the
  patch exposes existing ledger information only.

## Validation

- Read the required offline decision and scripted-GUI references, official
  trigger/effect documentation, and vanilla `USA_congress` / `MTG_congress`
  precedent. The category uses the documented `visible_when_empty = yes`
  pattern for an informational summary.
- Confirmed source lifecycle: `ireland_initialize_campaign` sets the opening
  chamber data and `ireland_initialized`; `ireland_settlement_open` is written
  only by `ireland_state_still_defined`.
- Ran scoped static assertions for the category gate, empty-category setting,
  initialized original-IRE gate, archival closure, removed action-reveal
  dependency, and retained native Dáil action reveal. All passed.
- Ran `hoi4.gui_inspect` and `hoi4.gui_render` for
  `ireland_parliament_decision_ui_window` in the
  `ire_start_after_initialization` / `empty-list` scenario. Artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/eb78129198cf989c3c23d5ed0d991477ed8ebf670dcb23cbc0998b0e598afbc1/f7b9ce3ba41f11f3f545e20b37d36e93143a9b7ea8eeab52bbb50571e2118a21/ireland_parliament_decision_ui_window-full.png`.
  The source graph parsed with no blocking GUI diagnostic and the render
  produced the empty-list variant. Its offline fidelity report was 171
  modelled, 3 approximated, 34 ignored, 2 missing, and 5 unresolved values;
  the unresolved values are live chamber variables that the offline scenario
  cannot inject, not layout or gate failures.

## Skipped meaningful validation

- No live game session was launched by this subagent.
- The GUI renderer is an offline source/render check and cannot execute the
  Clausewitz initializer or inject its resulting country variables, so the
  start-state assertion is established from the initializer-to-trigger path
  rather than a simulated save.

## Remaining risks and parent follow-up

No further implementation is required for this bounded visibility repair.
The parent can verify the initial IRE decision screen in its normal campaign
validation pass. No expansion plan was written.
