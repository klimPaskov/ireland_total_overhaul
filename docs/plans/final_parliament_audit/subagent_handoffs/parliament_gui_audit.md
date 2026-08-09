# Parliament scripted-GUI audit handoff

## Scope and changed files

- `interface/ireland_parliament_scripted_gui.gui`
  - Repacked `ireland_parliament_decision_ui_window` into the fixed 510 x 198 decision-category description host.
  - Kept the Dáil and Seanad summaries, four equal 125 px power columns, and their existing tooltip ids.
  - Marked all summary and state icons `alwaystransparent = yes`; these are status indicators, not alternate decision buttons.
- `common/scripted_guis/ireland_scripted_guis.txt`
  - Hid `ireland_parliament_decision_ui` after `ireland_route_archived` so an archived route cannot retain a stale read-only Parliament header.
- `localisation/english/ireland_l_english.yml`
  - Added `ireland_parliament_power_status_tt`, used only by the four state icons to explain their red-pending/green-complete meaning. The label tooltips still describe each action.

`common/scripted_effects/ireland_parliament.txt` was audited but not changed by this pass. Its four status-frame variables already implement the required contract.

## Identifiers and behavior

The affected displayed ids are:

- `dail_icon`, `seanad_icon`
- `ireland_parliament_power_dail_state`
- `ireland_parliament_power_seanad_state`
- `ireland_parliament_power_confidence_state`
- `ireland_parliament_power_budget_state`
- `ireland_parliament_decision_ui`
- `ireland_parliament_power_status_tt`

Before: the 510 px host contained child controls placed as far right as x=1,082, causing the Seanad summary and later power columns to overflow the decision category. Status icons also sat on ordinary click regions despite having no effects. The GUI could remain visible after the route's decisions were removed by archival.

After: all visible bounds are inside x=0..510 and y=0..198. The two chamber sprites retain their live 21-frame properties; the four 31 x 31 red/green state icons are centered beneath equal-width labels and pass clicks through to the native decision surface. Route archival hides the header.

## State and decision audit

`ireland_update_parliament` sets each power variable to `constant:ireland.one` (pending) and switches it to `constant:ireland.two` when its matching completion flag is present. The scripted GUI maps every one of those variables to the matching icon property. Vanilla `GFX_checkbox_small_red_green` has two frames; vanilla USA Congress uses the same one-based frame convention for its chamber properties.

The four native decisions are still the sole interaction path, are `fire_only_once`, and each calls its corresponding record effect. Their AI remains on the decisions, which is appropriate because this header has no GUI effects or click-enabled controls.

No missions belong to this surface. The category lifecycle is: reveal and initialization make the header visible; the four one-time decisions advance completion flags and frame values; route archival hides the header and removes the actions.

## Validation evidence

- Static host check used the vanilla `decision_category_desc` size of 510 x 8 and the Parliament GUI height of 198. All 17 controls are in-bounds; the furthest edges are the Seanad chamber sprite at x=500/y=128, the final label at x=508/y=164, and every checkbox at y=196.
- Asset headers verified frame geometry: Dáil 94 x 50 per frame, Seanad 132 x 73 per frame, and red/green status 31 x 31 per frame.
- Parsed vanilla font metrics: all four status labels fit the 125 px columns, including `Confidence compact` at 118 px; the longest numeric chamber strings fit their text bounds.
- Property/frame contract check passed for all four indicators: GUI element, GUI property, pending frame assignment, completion flag, and complete frame assignment all exist.

`hoi4.gui_inspect` and `hoi4.gui_render` were not registered in the audit
subagent session. The parent subsequently closed this handoff: the combined
source graph has no non-information diagnostics, and the final render covers
1280 x 720 and 1920 x 1080 across fourteen states with no visible overlap.
The authoritative artifact links are recorded in
`docs/plans/ireland_focus_tree/focus_tree_parliament_completion_2026-08-09.md`.

## Remaining risks

None within the Parliament header. The decision category owns other historical
actions and may remain visible independently; the scripted Parliament header
correctly hides when its route is archived.
