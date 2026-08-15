# Mechanics-hub documentation reconciliation handoff — 2026-08-15

> Historical reconciliation only. The six-tab ledger it documented was superseded by the compact Cabinet Briefing correction later on 2026-08-15.

Feature: Ireland National Situation Ledger and focus-tree inlay
Role: `hoi4_documentation_curator`
Scope: documentation surfaces only; no gameplay, localisation, assets, spreadsheets, or `thumbnail.png` edits

## Source-of-truth map

| Surface | Current authority | Status and evidence |
| --- | --- | --- |
| Accepted feature design | `docs/specs/ireland_mechanics_hub/ireland_mechanics_hub_spec.md` | Implemented. Durable presentation, archive, progressive-reveal, selection, and canonical-action rules are promoted from the corrective addendum. |
| Player-facing value contract | `docs/specs/ireland_mechanics_hub/value_purpose_matrix.md` | Implemented. Numeric values remain the full-ledger source of truth; hidden implementation state stays excluded. |
| Feature package index | `docs/specs/ireland_mechanics_hub/index.md` | Implemented on 2026-08-15; links the accepted source files and frozen evidence. |
| Runtime feature explanation | `docs/ireland_national_situation_ledger.md` | Implemented. Describes six tabs, guarded actions, inlay, asset wiring, archive behavior, and future extension boundary. |
| Broader runtime inventory | `docs/ireland_systems.md` | Updated current focus revision and GUI evidence without converting the document into a whole-repository completion claim. |
| Corrective plan | `docs/plans/ireland_mechanics_hub/improvement_loop/national_situation_ledger_corrective_addendum_2026-08-15.md` | Implemented; P0/P1 dispositions are closed, `NSL-Q-01` remains queued, and `NSL-Q-02` is superseded by existing selection markers. |
| Focus structural evidence | Frozen parent artifact: revision `90beeec44304c287` | 256 focuses, 234 connectors; zero crossings, node intersections, long connectors, and too-close pairs. Inlay declaration is `x = -600, y = 10`. |
| GUI evidence | Final parent artifacts: dashboard `f8fc5fbe5ea0d72c`, inlay `33f76c15e0ae8ae6` | No blockers after active/archive/state-matrix review at 1920x1080 and 2560x1440. |

## Plan and handoff disposition

| Document | Disposition | Reconciliation note |
| --- | --- | --- |
| `subagent_handoffs/repo_map_2026-08-14.md` | Historical / superseded for current counts and surfaces | It records the pre-ledger three-GUI state and older 218/226 focus evidence. It was not rewritten; use current source and this map for present status. |
| `subagent_handoffs/scripted_system_handoff_2026-08-14.md` | Implemented evidence retained | Shared constants, triggers, effects, lifecycle, and canonical adapters remain the implementation evidence; its statement that GUI/focus files were outside that subtask remains historically accurate. |
| `subagent_handoffs/inlay_asset_handoff_2026-08-14.md` | Asset production complete; integration closure appended | The former pending-registration statement is historical. The current `.gfx`, GUI, inlay definition, focus declaration, and frozen review evidence are recorded in the appended closure. |
| `subagent_handoffs/category_icon_and_selection_markers_handoff_2026-08-15.md` | Asset production complete; integration closure appended | The former pending-wiring statement is historical. Category and selection sprites are now registered and consumed. |
| `subagent_handoffs/improvement_loop_handoff_2026-08-15.md` | Historical plan; corrective addendum implemented | The old unresolved-P0 recommendation and old revision remain intact; an appended closure records current source support and superseding evidence. |
| `subagent_handoffs/final_interaction_audit_2026-08-15.md` | Historical audit; current closure appended | Earlier P1/render-gap notes are preserved as the audit snapshot and followed by the current source/evidence closure. |

## Contradictions and remaining limitations

Resolved in this pass:

- The source-spec index no longer says “accepted for implementation”; it now says implemented.
- `docs/ireland_systems.md` now uses focus revision `90beeec44304c287` while retaining the current 256/234 counts.
- Historical asset handoffs no longer leave the parent with an unqualified pending-registration instruction; their original wording is preserved and followed by integration closure.
- The corrective addendum now has explicit P0/P1/queued/superseded/rejected dispositions.

Remaining items for the parent to know:

1. No checked-in scenario manifest was found under the mechanics-hub plan directory. Current closure relies on the frozen parent GUI inspection artifacts named above. Do not invent a manifest or claim a reproducible fixture was added.
2. `NSL-Q-01` remains intentionally queued: no cross-category navigation control was added because a proven engine-safe pattern was not supplied.

## Duplicate or superseded documentation

- The dated `repo_map_2026-08-14.md` is historical exploration, not a current implementation ledger.
- The dated improvement-loop handoff is historical planning material; its appended closure supersedes its old “unresolved” status for current documentation use.
- The dated final interaction audit is historical audit evidence; its appended closure supersedes its old “P1 remaining” status for current documentation use.
- The implementation and asset prompts remain in the accepted spec package as acceptance records, but their new status lines make clear that they are not open work requests.

## Stale prompts or instructions found

- `docs/specs/ireland_mechanics_hub/implementation_prompt.md` previously read as an unstarted imperative; it is now marked implemented and retained as a checklist.
- `docs/specs/ireland_mechanics_hub/asset_prompt.md` previously read as an open asset gate; it is now marked implemented and points to the registered static package.
- The old `repo_map` and improvement-loop handoff contain dated pre-integration instructions. They were not silently rewritten; current status is supplied by their disposition here and appended closures where appropriate.

## Recommended parent decisions

- Keep `NSL-Q-01` queued until a category-navigation precedent proves that visibility, cost, and reveal gates remain intact.
- If final feature closure requires deterministic in-repo scenario fixtures, add them through the appropriate GUI/audit owner; this documentation pass records the supplied MCP evidence but does not manufacture fixtures.
- Keep the current single `ireland_focus_inlay_culture_critical_evidence` localisation key aligned with `GetIrelandMechanicsHubInlayCulture`; a targeted search found one current definition after the concurrent parent localisation pass.
- Preserve the frozen revision/artifact references in the parent completion report. They are the current evidence boundary for this documentation reconciliation.

## Files changed

- `docs/specs/ireland_mechanics_hub/index.md`
- `docs/specs/ireland_mechanics_hub/ireland_mechanics_hub_spec.md`
- `docs/specs/ireland_mechanics_hub/value_purpose_matrix.md`
- `docs/specs/ireland_mechanics_hub/implementation_prompt.md`
- `docs/specs/ireland_mechanics_hub/asset_prompt.md`
- `docs/ireland_national_situation_ledger.md`
- `docs/ireland_systems.md`
- `docs/plans/ireland_mechanics_hub/improvement_loop/national_situation_ledger_corrective_addendum_2026-08-15.md`
- `docs/plans/ireland_mechanics_hub/subagent_handoffs/inlay_asset_handoff_2026-08-14.md`
- `docs/plans/ireland_mechanics_hub/subagent_handoffs/category_icon_and_selection_markers_handoff_2026-08-15.md`
- `docs/plans/ireland_mechanics_hub/subagent_handoffs/improvement_loop_handoff_2026-08-15.md`
- `docs/plans/ireland_mechanics_hub/subagent_handoffs/final_interaction_audit_2026-08-15.md`
- this handoff

## Validation and skipped checks

Meaningful documentation checks run:

- targeted `rg` checks confirmed the current `x = -600, y = 10` focus declaration, 256/234 counts, current frozen revision references, category/selection sprite registrations, and the mechanics-hub scripted-GUI/inlay call sites;
- targeted source review confirmed the Northern row predicates feed both visibility and click eligibility, archive state gates refresh/context controls, and inlay localisation dispatch includes public state phrases;
- targeted status review confirmed the source spec, corrective addendum, prompts, and historical handoffs now each have an explicit current disposition or appended closure.

Skipped meaningful checks:

- no gameplay, live engine, binary-asset, or localisation validation was run because those surfaces are explicitly outside this documentation-only scope and the parent supplied the frozen MCP evidence;
- no file deletion, archival move, commit, or `thumbnail.png` edit was performed.

## Handoff result

The mechanics-hub documentation set now identifies the implemented source spec, current structural/GUI evidence, promoted corrective rules, queued navigation question, historical handoffs, and remaining source-level risks. No gameplay completion claim is made by this handoff.
