# Scripted-system handoff: National Situation Ledger

## Scope and ownership

- Parent task: implement the shared scripted-system layer for the accepted
  Ireland National Situation Ledger specification.
- Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/ireland_total_overhaul`.
- Files changed by this handoff:
  - `common/script_constants/ireland_mechanics_hub.txt`
  - `common/scripted_triggers/ireland_mechanics_hub.txt`
  - `common/scripted_effects/ireland_mechanics_hub.txt`
  - `docs/ireland_dynamic_effects.md`
  - this handoff file
- GUI, focus, decision-category, localisation, existing lifecycle
  initialization/cleanup, and assets were not edited. `thumbnail.png` was not
  edited.
- No commit was created. The working tree also contains concurrent parent
  changes in GUI, focus, localisation, category, and lifecycle files. They
  remain outside this handoff.

## Helper map

| Identifier | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `ireland_mechanics_hub_state/provision/readiness/foreign/northern/culture_visible` | country | `ireland_initialized`, existing reveal predicates | visibility truth | none | hub status dispatch and parent GUI/localisation surfaces |
| `ireland_mechanics_hub_state_ready/warning/critical` | country | National Settlement, crisis flags, existing stage constants | family status truth | none | focus inlay and overall status dispatch |
| `ireland_mechanics_hub_provision_ready/warning/critical` | country | Provision display and existing bottleneck triggers | family status truth | none | focus inlay and overall status dispatch |
| `ireland_mechanics_hub_readiness_ready/warning/critical` | country | Readiness display and existing material bottleneck triggers | family status truth | none | focus inlay and overall status dispatch |
| `ireland_mechanics_hub_neutrality_ready/warning/critical` | country | Neutrality Integrity and active incident trigger | family status truth | none | focus inlay |
| `ireland_mechanics_hub_northern_locked/ready/warning/critical` | country | Northern reveal including completed `ireland_northern_settlement_ledger` focus, failure flags, consent-state values, and existing GUI thresholds | family status truth | none | focus inlay and overall status dispatch |
| `ireland_mechanics_hub_culture_locked/ready/warning/critical` | country | Culture reveal, Cultural Capacity, public Evidence disqualifier state | family status truth | none | focus inlay and overall status dispatch |
| `ireland_mechanics_hub_status_ready/warning/critical/locked` | country | selected tab plus family status triggers | selected-tab status truth | none | parent scripted GUI |
| `ireland_next_state_action_available` | country | canonical Parliament availability triggers | action availability truth | none | focus-inlay button and State context gate |
| `ireland_mechanics_hub_context_action_available` | country | selected tab, visibility, and action gates | context-button truth | none | parent scripted GUI |
| `ireland_refresh_national_situation` | country | live Provision, Readiness, operational, named Northern, and public Culture inputs | refreshed existing displays and dirty counter | calls existing recomputers and safe named/public syncs | parent dashboard and focus-inlay refresh buttons |
| `ireland_execute_next_state_action` | country | `ireland_next_state_action_available` | at most one Parliament step | delegates to canonical guarded Parliament executor, dirties hub | State context action and focus-inlay next-state button |
| `ireland_select_weakest_provision_component` | country | four Provision component values | selected hub row | temporary comparison only, dirties hub | Provision context branch |
| `ireland_select_weakest_readiness_component` | country | seven Readiness component values | selected hub row | temporary comparison only, dirties hub | Readiness context branch |
| `ireland_select_weakest_culture_component` | country | public Cultural Capacity and four named public culture components | selected hub row one through five | temporary comparison only, dirties hub | Culture context branch before Evidence review |
| `ireland_review_national_situation_northern` | country | Northern tab visibility and selected-row review gate | request flag consumed by shared GUI sync | delegates to `ireland_sync_gui_requests`; no duplicate reward | Northern context branch |
| `ireland_review_national_situation_evidence` | country | Culture/Evidence reveal and Evidence row selection | request flag consumed by shared GUI sync | delegates to canonical Evidence inspection path | Culture context branch |
| `ireland_review_national_situation_culture` | country | public Culture reveal | public cultural components | calls `ireland_sync_cultural_evidence` only | Culture context branch before Evidence review |
| `ireland_review_national_situation_foreign` | country | Foreign tab visibility, Exposure, Sponsor Dependence | selected row five or six | refreshes existing report and selects the higher risk, no leverage mutation | Foreign context branch |
| `ireland_execute_mechanics_hub_context_action` | country | selected tab and context availability | dispatch result | routes only to helpers listed above | parent dashboard context button |

## Constants and tuning table

`common/script_constants/ireland_mechanics_hub.txt` adds one integer category:

| Key family | Values | Purpose |
| --- | --- | --- |
| `tab_state`, `tab_provision`, `tab_readiness`, `tab_foreign`, `tab_northern`, `tab_culture` | `1..6` | stable selected-tab IDs used by GUI effects, scripted localisation, status dispatch, and context dispatch |
| `row_none`, `row_one` through `row_seven` | `0..7` | stable row IDs used by GUI effects and weakest-component selection |

No status thresholds were duplicated. Status triggers reuse settlement stage
bands, Provision and Readiness GUI thresholds, Neutrality GUI thresholds,
Northern GUI thresholds, Culture evidence floors, and existing Foreign reveal
and leverage ceilings from `constant:ireland`.

## Lifecycle and cleanup plan

- The existing `ireland_initialize_campaign` and cleanup helpers already own
  `ireland_mechanics_hub_selected_tab` and `ireland_mechanics_hub_selected_row`.
  They now resolve the shared IDs from the new constants category.
- No new event targets were needed. The helper layer only uses existing
  country-scoped request flags for Northern and Evidence review.
- `ireland_sync_gui_requests` clears
  `ireland_northern_review_requested` and
  `ireland_concealed_evidence_inspection_requested` after delegating to their
  canonical synchronisers.
- Refresh intentionally calls named Northern objective sync rather than the
  full Northern ledger. The full ledger advances review-derived state and can
  reach core review, so it remains behind the explicit dedicated review path.

## Migration and call-site plan

1. Parent GUI and focus-inlay call the new public context and status identifiers.
2. Existing Parliament GUI and native decisions continue to call the four
   original Parliament executors. The hub only selects the next one and calls
   that executor.
3. Existing Northern and Evidence panels remain canonical. The hub writes the
   same request flags and invokes `ireland_sync_gui_requests` rather than
   copying their ledger mutations.
4. Existing Provision and Readiness recomputers remain authoritative for
   displays and bottleneck flags. The hub selectors read the raw canonical
   components to identify the first minimum without changing the aggregate
   implementation or balance.
5. Existing lifecycle initialization and cleanup remain authoritative for
   selection-only variables. No GUI or localisation migration is required in
   this subtask.

## Risks and unsupported fields

- The existing Provision and Readiness recomputers expose rounded average
  display values with bottleneck caps. The new selectors use raw components as
  required by the accepted weakest-component contract, while status triggers
  retain the existing authored thresholds and bottleneck triggers.
- The Northern full synchroniser includes review-derived state and the guarded
  core-review call. The refresh helper therefore uses only named objective
  records. Explicit Northern context review still delegates to the canonical
  request flow and its existing gates.
- The Evidence request path may call the existing hidden-permission
  synchroniser. The hub only reaches it after the public Evidence reveal and
  Evidence row selection gate, so concealed content is not exposed by ordinary
  Culture review or report refresh.
- Foreign review is deliberately visible without being a diplomacy action. It
  refreshes and selects Exposure or Sponsor Dependence, with Exposure winning
  ties. Culture review selects the weakest public row one through five unless
  the revealed Evidence row is selected.
- No dynamic threshold injection or event-target persistence was necessary.
  This layer does not add unsupported GUI fields, balance aliases, or new
  on-actions.
- The Northern context action mirrors the dedicated ledger's selected-row
  requirement. A tab-wide Northern action remains disabled until a row is
  selected, matching the canonical review button contract.

## Validation

- Inspected the accepted mechanics-hub spec, value-purpose matrix, and
  implementation prompt.
- Inspected the existing Parliament availability/executor pair, Provision and
  Readiness recomputers, operational-state sync, named Northern objective and
  full Northern ledger helpers, cultural Evidence synchroniser, and shared GUI
  request delegator.
- Inspected the parent GUI and focus-inlay call sites to match every requested
  public trigger/effect name.
- Read the required offline wiki pages and vanilla script constants, effects,
  triggers, scopes, GUI, and focus-inlay documentation before implementation.
- Performed repository checks for every new identifier's definition and for
  balanced Clausewitz braces in the three new script files. No game executable
  or live save validation was run in this subtask because the parent owns the
  concurrent GUI, focus, category, localisation, and render validation pass.

## Simplifications and follow-up

No balance changes, free effects, fallback rewards, new assets, localisation
changes, or gameplay redesigns were introduced. The parent should include the
new files in the final scripted-GUI, focus-inlay, localisation, and completion
audits and verify the selected-row Northern/Evidence action states in the live
panels.
