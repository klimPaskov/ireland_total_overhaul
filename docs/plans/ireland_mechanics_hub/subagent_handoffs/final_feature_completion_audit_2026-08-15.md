# Ireland National Situation Ledger: final feature-completion audit

> Historical audit only. Its six-tab/34-record scope was rejected by player review and superseded by the compact Cabinet Briefing correction and its successor completion evidence.

Date: 2026-08-15
Feature slug: `ireland_mechanics_hub`
Audit mode: read-only source, plan, asset, documentation, and frozen-evidence comparison
Verdict: **COMPLETE**

## Completion verdict

The accepted Ireland National Situation Ledger scope is complete. The current source provides one comprehensible six-family decision-category ledger, 34 purposeful public records, selected-value purpose and significance, current state-dependent consequence/gate text, guarded canonical actions, and a compact interactive focus-tree inlay. It does not introduce a second reward, cost, route, or AI system.

No accepted requirement, accepted corrective item, asset, localisation surface, AI contract, documentation disposition, or task-specific validation blocker remains. No fallback or undisclosed simplification remains.

`NSL-Q-01`, engine-safe navigation to another decision category, remains explicitly queued and was never accepted. It is not a completion blocker.

## Audit basis

The audit compared current source against:

- `docs/specs/ireland_mechanics_hub/`;
- `docs/ireland_national_situation_ledger.md`;
- `docs/plans/ireland_mechanics_hub/improvement_loop/national_situation_ledger_corrective_addendum_2026-08-15.md`;
- every handoff under `docs/plans/ireland_mechanics_hub/subagent_handoffs/`;
- `docs/plans/ireland_mechanics_hub/completion_report_2026-08-15.md`;
- the feature asset manifest, prompts, contact-sheet records, and GFX handoff under `docs/assets/ireland_mechanics_hub/`.

The repository completion route used `hoi4-subagents`, `hoi4-feature-planning`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `hoi4-improvement-loop`, and `hoi4-feature-assets`. The scripted-GUI and focus-inlay checks also used the offline core, Interface Modding, Scripted GUI Modding, and National Focus/Focus Inlay wiki material; official vanilla scripted-GUI, focus-inlay, decision, script-concept, and script-constant documentation; and the AST, CZE, GER, JAP, and SIA vanilla inlay precedents.

## Completion by surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Decision category and dashboard | Complete | `ireland_national_situation` is visible after `ireland_initialized`, remains readable when empty, owns `ireland_national_situation_scripted_gui`, and renders the 510x590 `ireland_national_situation_window`. |
| Public value coverage | Complete | The live row dispatch exposes 5 State, 4 Provision, 7 Readiness, 6 Foreign, 6 National Question, and 6 Culture/Evidence records: 34 distinct public records. The locked/revealed Evidence strings are two presentations of one record, not a thirty-fifth value. |
| Purpose and significance | Complete | The GUI has separate `GetIrelandMechanicsHubSelection`, `GetIrelandMechanicsHubFamilyPurpose`, `GetIrelandMechanicsHubSelectedStatus`, `GetIrelandMechanicsHubConsequence`, and `GetIrelandMechanicsHubAction` slots. There are 34 row-specific consequence/consumer/route branches, 32 state-driven selected-status branches, and a neutral first branch for `row_none`. |
| Internal-value concealment | Complete | Event cursors, preview deltas, AI caches, dirty counters, temporary comparisons, frame indices, selection variables, and one-use helper flags remain outside the 34-record matrix and GUI rows. |
| Canonical interactions | Complete | State delegates to the four guarded Parliament executors; Provision and Readiness recompute then select a deterministic minimum; Foreign selects the greater autonomy risk; Northern and Evidence use their existing request/synchronizer paths; Culture recomputes/selects public capacity; Refresh updates bounded projections only. |
| Reward and exploit safety | Complete | The hub adds no PP, CP, equipment, factories, claims, cores, route progress, leverage, Provision, or Readiness. Selectors change presentation state only; the two review paths retain their canonical guards and consumers. |
| Reveal and archive lifecycle | Complete | Northern rows mirror their exact focus predicates for visibility and click eligibility. Evidence shows `Sealed` until the canonical reveal flag. `ireland_mechanics_hub_open` disables dashboard and inlay actions after `ireland_route_archived` while leaving the historical record readable. |
| Focus-tree inlay | Complete | `ireland_national_situation_inlay` is internal, visible to initialized original-tag Ireland, placed at `x = -600, y = 10`, shows six public summaries, and exposes only the shared Refresh and next-Parliament-step helpers. |
| AI contract | Complete | The decision-category scripted GUI has `ai_enabled = { always = no }` and `ai_check = { always = no }`. The documented focus-inlay schema has no AI-click surface. Native decisions, focuses, missions, and canonical executors remain the AI paths. |
| Localisation | Complete | Every mechanics-hub and inlay scripted-localisation/GUI reference resolves. The final static audit found 250 distinct feature-facing references and no missing English key. |
| Sprites and assets | Complete | All four feature assets have final DDS files, registered sprites, source and processed PNGs, prompts, contact-sheet records, and current wired manifest status. No placeholder or fallback asset is active. |
| Documentation and tracking | Complete | The source spec, value matrix, player/maintainer guide, corrective-plan closure table, completion report, asset manifest, and integration handoffs agree with current source and frozen evidence. |

## Value-purpose and selected-state evidence

The authoritative value matrix and live row dispatch agree on all 34 public records. Each selected record exposes:

- its live value or accountable sealed/revealed state;
- a definition and named consumers/sources;
- a family-purpose line;
- a current selected-state line;
- a row-specific consequence, gameplay gate/consumer, and canonical improvement or review route;
- the family action and its live requirements.

The selected-state helpers use current gameplay rather than a presentation cache:

- `ireland_mechanics_hub_selected_provision_is_lowest` mirrors the four-row deterministic minimum and tie order;
- `ireland_mechanics_hub_selected_readiness_is_lowest` mirrors the seven-row minimum and tie order;
- `ireland_mechanics_hub_selected_foreign_is_greater_risk` mirrors Exposure-versus-Dependence selection, with Exposure winning ties;
- `ireland_mechanics_hub_selected_culture_is_lowest` mirrors the five public Culture rows;
- State dispatches the opening Parliament gate or current family state;
- Northern names the current integration stage and retains failure overrides;
- revealed Evidence reports credible, disqualifying, and obligation counts, while sealed Evidence overrides all value-bearing branches.

The `row_none` branch is first, so switching tabs cannot print an “other component” comparison before the player selects a row.

## Canonical action and disclosure evidence

The full dashboard's 15 clickable controls all have matching scripted-GUI effects and click-enabled triggers. The inlay's two buttons have matching `available` blocks and `click_effect` blocks.

- The State action uses `ireland_next_state_action_available` and calls exactly one of the four existing Parliament executors in native programme order. The same executors remain called by their native decisions and Parliament GUI.
- Provision, Readiness, Foreign, and public Culture actions only recompute or select. They do not mutate their gameplay values.
- Northern projects the visible hub row into the dedicated selection and calls the existing Northern request consumer. Its progressive rows remain: 1-2 Settlement Ledger; 3 Labour Social Bridge; 4 Trade Corridor; 5 Local Authorities; 6 Federal or Unitary Preparation.
- A sealed Evidence row contains no credible/disqualifier/obligation value and cannot invoke Evidence inspection. Once revealed, inspection delegates to the existing request/synchronizer path.
- Refresh calls existing Provision, Readiness, operational, visible Northern, and visible cultural projection helpers. It has no reward or route-advance path.
- Dashboard Refresh/Context and both inlay buttons share the archived/open availability contract, preventing enabled no-op controls.

## Accepted-plan disposition

The corrective addendum is fully disposed:

| Item | Final disposition |
| --- | --- |
| `NSL-P0-01` | Implemented: safe inlay position and focus evidence. |
| `NSL-P0-02` | Implemented: exact Northern progressive reveal/click parity. |
| `NSL-P0-03` | Implemented: persistent brass tab and visible-row selectors. |
| `NSL-P0-04` | Implemented: separate definition, family purpose, current selected state, row-specific consequence/gate/consumer, and canonical next route. |
| `NSL-P0-05` | Implemented: shared archive/open action contract. |
| `NSL-P0-06` | Implemented: deterministic dashboard/inlay state and resolution evidence. |
| `NSL-P1-01` | Implemented: truthful public North and Culture/Evidence state phrases. |
| `NSL-P1-02` | Implemented: bounded Refresh wording. |
| `NSL-Q-01` | Queued, not accepted: cross-category navigation lacks a proven safe precedent. |
| `NSL-Q-02` | Superseded: existing static selection assets satisfy the requirement. |
| `NSL-R-01` through `NSL-R-05` | Rejected with recorded reasons; no cloned executor, animation family, AI GUI path, unrelated route redesign, or concealed-value exposure was added. |

The repository-map, scripted-system, asset-production, improvement-loop, interaction, focus-inlay, localisation, and documentation handoffs all have implemented, integrated, superseded, queued, or rejected dispositions. No subagent patch lacks a handoff.

## Meaningful validation and tool-fidelity limits

- Focus inspection revision `90beeec44304c287` resolves 256 focuses and 234 connectors with zero connector crossings, node intersections, long connectors, or cramped same-row pairs. The 460x248 inlay footprint contains no focus anchor and ends before focus row two.
- Dashboard inspection revision `f8fc5fbe5ea0d72c` covered six value-driven family scenarios plus the archived state at 1920x1080 and 2560x1440. `blockers=[]`. The only visible-overlap notices are intended co-located mutually exclusive ready/warning/critical status sprites. Inspect artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/2a7fb0bdc67faddfa4f26d7094b4efdaeba2fbdd0a7f674ba25dfae7e6bd7455/0531066c8f2c19074e69199ddd6c6c8db748496cc26131e886884a9e9e69744d/gui-inspect.f8fc5fbe5ea0d72c.json`. Render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8dd465e12d245fa8690535233c9c8d1e34972b5aea4f1eb74e7bf382605f907e/5903631abedac6364165f2b1b2ce31066b87355b302a3baf63d0f5573127b64b/ireland_national_situation_window-full.svg`.
- Inlay inspection revision `33f76c15e0ae8ae6` reports no blocker. Inspect artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/21971c03a44004835faf0800bda8ce7df13f47ba4eb0201f08c4fc8519f2cd62/c68c93f749b8d82905445e9821274e9c07bf106ce640b5299b3f31fba249c93b/gui-inspect.33f76c15e0ae8ae6.json`. State matrix: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5d211a9b8cef6d836d52bc11167a64043d6e7be0f7757becdc9ea963361cc2da/e70c67b075f460c6167c8c75eb2aa6cfa2c2f562d77ac94176d9e7f4e1c7a2b6/ireland_national_situation_inlay_window-state-matrix.png`.
- Final source audit confirmed 34 row-specific consequence branches, four state-comparison helpers, 32 selected-status branches plus the first neutral no-row branch, and no missing feature localisation reference.
- The four final DDS dimensions match their contracts: category `52x40`, inlay background `460x248`, tab marker `48x8`, and row marker `14x14`.

The GUI scenario schema cannot model completed focuses, so the Northern focus-completion matrix is proven by source predicates rather than simulated focus state. The offline renderer also cannot execute `defined_text`, text-sprite state dispatch, or `buttonstate.lua`; those bindings and localisation branches were audited directly. These are tool-fidelity limits, not unresolved source defects.

## Assets, documentation, simplifications, and blockers

- Asset gaps: none.
- Localisation gaps: none.
- AI gaps: none.
- Documentation/tracking gaps: none.
- Accepted-plan gaps: none.
- Remaining blockers: none.
- Fallbacks or simplifications: none. The static inlay and selectors are the accepted design; animation was explicitly rejected because it would not communicate additional state.
- External record gaps: none were scoped. No sourced quote, historical image, spreadsheet, or audio package is required by this feature.

## Recommended next action

The parent may make the feature-completion claim using the current completion report and frozen artifacts. No further implementation or improvement-loop planner pass is recommended: the existing corrective addendum is resolved, the six-family architecture has the intended depth, and its own closure guidance says further family expansion would be bloat.

Keep `NSL-Q-01` queued unless a later, separately accepted plan identifies a proven engine-safe category-navigation precedent.

## Audit write boundary

This audit created only this handoff. It did not edit gameplay, localisation, assets, specs, other documentation, or `thumbnail.png`. No commit was created.
