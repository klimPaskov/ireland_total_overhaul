# Ireland National Situation Ledger completion report

Date: 2026-08-15
Feature slug: `ireland_mechanics_hub`
Status: implemented

## Outcome

Ireland now has one player-facing National Situation Ledger in the decision view and one compact National Situation inlay in the focus view. They explain the existing State, Provision, Readiness, Foreign Pressure, National Question, and Culture and Evidence systems without adding another balance layer.

The full ledger presents 34 purposeful public records. Every row has a live value or accountable state, a selected-row explanation, a separate family-purpose line, a current consequence or binding gate, a next canonical action, and colour-coded ready, warning, critical, or locked status. Event cursors, preview variables, dirty counters, AI caches, frame indices, and other implementation-only values remain hidden.

## Interaction and authority

- State actions delegate to the guarded Parliament executors.
- Provision and Readiness refresh their canonical aggregates and select the weakest component; they grant no value.
- Foreign Pressure selects the greater autonomy risk between Foreign Exposure and Sponsor Dependence.
- National Question delegates to the existing Northern review request and synchronizer. Its six rows retain their authored progressive focus reveal.
- Culture selects the weakest public capacity; a revealed Evidence row delegates to the existing evidence review.
- Refresh recomputes public projections through existing helpers and grants no reward or route progress.
- The focus inlay provides the same summaries plus guarded Refresh and next-Parliament-step actions.
- Route archival disables the action and refresh controls. AI continues to use native focuses, decisions, missions, and executors and never clicks the GUI.

## Presentation and assets

The full ledger is a 510 by 590 decision-category panel with persistent tab and row selection, distinct family icons, consequence text, exact requirement tooltips, and active/archive states. The 460 by 248 focus inlay is placed at `x = -600, y = 10`, inside the empty upper corridor between the cultural and economic lanes and above focus row two.

The category icon, inlay background, selected-tab marker, and selected-row marker have final DDS files, registered sprites, source/processed PNGs, prompt records, contact sheets, and manifests under `docs/assets/ireland_mechanics_hub/`. No placeholder or fallback asset is used.

## Files and systems

- Feature source of truth: `docs/specs/ireland_mechanics_hub/`
- Player and maintainer guide: `docs/ireland_national_situation_ledger.md`
- Decision category: `common/decisions/categories/ireland_categories.txt`
- Scripted GUI binding: `common/scripted_guis/ireland_scripted_guis.txt`
- Focus inlay declaration: `common/focus_inlay_windows/ireland_national_situation_inlay.txt`
- Shared tuning, triggers, and effects: `common/script_constants/ireland_mechanics_hub.txt`, `common/scripted_triggers/ireland_mechanics_hub.txt`, and `common/scripted_effects/ireland_mechanics_hub.txt`
- Dynamic text: `common/scripted_localisation/ireland_localisation.txt`
- Layouts: `interface/ireland_national_situation.gui` and `interface/ireland_national_situation_inlay.gui`
- Sprites and English text: `interface/ireland_gui_assets.gfx`, `interface/ireland_icons.gfx`, and `localisation/english/ireland_l_english.yml`

## Meaningful validation evidence

- Focus inspection revision `90beeec44304c287`: 256 focuses and 234 connectors, with zero connector crossings, node intersections, long connectors, or cramped same-row pairs. The inlay footprint contains no focus anchor and ends before row two.
- Dashboard inspection revision `f8fc5fbe5ea0d72c`: six value-driven family scenarios plus the archived state linked the source graph with no blockers. The only overlap notices are the intentional shared status slot and click-transparent selected-tab overlays; the header, tabs, values, prose, and controls do not collide. A final source audit also confirms the neutral no-row-selected fallback before any bottleneck comparison is printed.
- Inlay inspection revision `33f76c15e0ae8ae6`: source graph linked with no blockers or visible-overlap defect.
- Active and archived scenarios were reviewed at 1920x1080 and 2560x1440 across normal, hover, selected, locked, disabled, warning, active, completed, empty/full-list, minimum/maximum-value, long-text, and missing-localisation states.
- Scripted localisation resolves every mechanics-hub output key. The offline renderer cannot execute two defined-text projections and engine text-sprite state code; their source triggers and localisation branches were checked directly.

Current artifacts:

- Dashboard inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/2a7fb0bdc67faddfa4f26d7094b4efdaeba2fbdd0a7f674ba25dfae7e6bd7455/0531066c8f2c19074e69199ddd6c6c8db748496cc26131e886884a9e9e69744d/gui-inspect.f8fc5fbe5ea0d72c.json`
- Dashboard render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8dd465e12d245fa8690535233c9c8d1e34972b5aea4f1eb74e7bf382605f907e/5903631abedac6364165f2b1b2ce31066b87355b302a3baf63d0f5573127b64b/ireland_national_situation_window-full.svg`
- Inlay inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/21971c03a44004835faf0800bda8ce7df13f47ba4eb0201f08c4fc8519f2cd62/c68c93f749b8d82905445e9821274e9c07bf106ce640b5299b3f31fba249c93b/gui-inspect.33f76c15e0ae8ae6.json`
- Inlay state matrix: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5d211a9b8cef6d836d52bc11167a64043d6e7be0f7757becdc9ea963361cc2da/e70c67b075f460c6167c8c75eb2aa6cfa2c2f562d77ac94176d9e7f4e1c7a2b6/ireland_national_situation_inlay_window-state-matrix.png`

## Simplifications, omissions, and blockers

No simplifications, omissions, fallback assets, duplicate mechanics, or feature blockers remain in the accepted National Situation Ledger scope. The optional cross-category navigation experiment `NSL-Q-01` remains deliberately queued rather than accepted; the implemented contextual actions already route through the canonical systems.
