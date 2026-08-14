# Ireland National Situation Ledger

Feature slug: `ireland_mechanics_hub`.

## Current status and evidence

The National Situation Ledger and its focus-tree inlay are implemented. The frozen structural evidence is focus inspection revision `90beeec44304c287` with 256 focuses and 234 connectors, reporting zero crossings, node intersections, long connectors, and too-close pairs. Final dashboard GUI inspection revision `f8fc5fbe5ea0d72c` and inlay GUI inspection revision `33f76c15e0ae8ae6` report no blockers after active, archived, selected, locked, disabled, warning, completed, extreme-value, and long-text review at 1920x1080 and 2560x1440. This is a feature-surface documentation status, not a whole-repository completion claim.

## Purpose

The National Situation Ledger is the common player-facing explanation and control surface for Ireland's interconnected state values. It is visible in the decision view after campaign initialization and is summarized by a compact inlay inside the national-focus view.

The ledger separates six mechanic families:

1. State: constitutional legitimacy, public consent, neutrality, administrative delivery, and parliamentary mandate.
2. Provision: food, energy, transport, and maritime access.
3. Readiness: command, equipment, mobilisation, supply, warning, maritime protection, and intelligence.
4. Foreign pressure: four bilateral leverage records plus Foreign Exposure and Sponsor Dependence.
5. National Question: unionist and nationalist consent, labour cooperation, British flexibility, security stability, and integration capacity.
6. Culture and evidence: cultural capacity, language service, archives, regional participation, site stewardship, and the accountable evidence record.

Event-preview deltas, dispatcher cursors, temporary calculations, dirty counters, AI caches, and frame indices remain internal. They do not represent choices the player can govern.

## Reading the ledger

Each family has a permanent tab, a summary, selectable rows, a plain-language explanation, a purpose line naming the systems affected, and a guarded action. Selecting a row also reports whether that exact value is the current bottleneck or greater autonomy risk; the Northern record names the active integration stage, while revealed Evidence names credible proof, disqualifiers, and accepted obligations. Grey means that the public record has not been institutionally opened; its summary and action tooltip name the exact opening focus or channel. Green means the governing threshold currently passes, amber means the family is under pressure, and red means an active gate is failing.

Provision is the rounded average of its four components, constrained by severe and multiple-service bottleneck caps. Readiness is the rounded average of seven components, constrained by the operational bottleneck caps for equipment, supply, warning, and maritime protection. The actions select the lowest component so the player can see the most direct improvement target, but the aggregate is not falsely described as a simple minimum.

Bilateral foreign leverage is directional rather than inherently beneficial. The interface uses Foreign Exposure and Sponsor Dependence to communicate autonomy risk. Concealed evidence remains sealed until the existing evidence system reveals it.

## Interactive actions

- State delegates to the next available Parliament executor. The tooltip uses the same live focus, stage, majority, Political Power, ownership, and completion checks as the Parliament surface.
- Provision recomputes the existing aggregate and selects its lowest component. It grants no capacity.
- Readiness recomputes the existing aggregate and selects its lowest component. It grants no readiness.
- Foreign pressure selects the greater current value of Foreign Exposure and Sponsor Dependence. It grants no leverage.
- National Question delegates to the existing Northern review request and synchronizer after a row is selected.
- Culture selects the weakest public cultural component; selecting a revealed Evidence Record delegates to the existing evidence inspection request and synchronizer.
- Refresh report recalculates Provision, Readiness, operational flags, and opened Northern and cultural projections through existing helpers. It grants no value, route progress, resource, or reward, and it is disabled after route archival.

AI continues to use native decisions, missions, focus plans, and their canonical executors. The scripted GUI and focus inlay are human-facing projections, not alternate AI gameplay paths.

## Focus-tree inlay

`ireland_national_situation_inlay` shows Settlement, Provision, Readiness, Neutrality, the National Question, and Culture with the same green/amber/red/locked vocabulary. The National Question displays its integration stage instead of pretending one component represents the whole settlement; Culture distinguishes public capacity from a sealed or revealed Evidence count. It exposes two actions: refresh the report and execute the next available Parliament step. Both use the same helpers as the full ledger.

The inlay is declared in `common/focus_inlay_windows/ireland_national_situation_inlay.txt`, rendered by `interface/ireland_national_situation_inlay.gui`, and placed by the Ireland focus tree. It does not change focus visibility, prerequisites, rewards, filters, AI weights, or route gates.

## Implementation ownership

- Category: `common/decisions/categories/ireland_categories.txt`
- Scripted GUI: `common/scripted_guis/ireland_scripted_guis.txt`
- Focus inlay: `common/focus_inlay_windows/ireland_national_situation_inlay.txt`
- Shared constants: `common/script_constants/ireland_mechanics_hub.txt`
- Shared triggers: `common/scripted_triggers/ireland_mechanics_hub.txt`
- Shared effects: `common/scripted_effects/ireland_mechanics_hub.txt`
- Dynamic text: `common/scripted_localisation/ireland_localisation.txt`
- Full layout: `interface/ireland_national_situation.gui`
- Inlay layout: `interface/ireland_national_situation_inlay.gui`
- Sprite registration: `interface/ireland_gui_assets.gfx`
- English text: `localisation/english/ireland_l_english.yml`

## Assets

- Full ledger background: `gfx/interface/ireland/gui/conditions/background.dds`, sprite `GFX_ireland_gui_conditions_background`.
- Focus inlay background: `gfx/interface/ireland/gui/conditions/focus_inlay_background.dds`, sprite `GFX_ireland_mechanics_hub_inlay_background`.
- Decision category: `gfx/interface/decisions/categories/ireland/ireland_national_situation.dds`, sprite `GFX_decision_category_ireland_national_situation`.
- Persistent selection: `GFX_ireland_mechanics_hub_tab_selected` and `GFX_ireland_mechanics_hub_row_selected`.
- Status vocabulary: `GFX_ireland_gui_status_ready`, `GFX_ireland_gui_status_warning`, `GFX_ireland_gui_status_critical`, and `GFX_ireland_gui_status_locked`.
- Rows and controls: `GFX_ireland_gui_value_row` and `GFX_ireland_gui_parliament_step_button`.
- Tab emblems reuse the six registered Ireland decision-category sprites.

Source, processed, prompt, manifest, and handoff evidence for the inlay background lives under `docs/assets/ireland_mechanics_hub/`.

## Future plans

Future extensions should add new rows only when a value has a distinct player-controlled purpose and named consumers. A new family should not be added merely because another script variable exists. If regional service delivery or postwar reconstruction becomes a genuinely separate player system, it should first be evaluated as a contextual row or dedicated existing-ledger extension before expanding the six-family navigation model.
