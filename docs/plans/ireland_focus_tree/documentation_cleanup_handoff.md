# Ireland Documentation Cleanup Handoff

Feature slug: `ireland_focus_tree`
Reconciled: 2026-07-22
Scope: documentation only; HOI4 was not launched.

Current-status addendum (2026-08-02): this handoff remains a historical
documentation-cleanup record. The current authority is
`source_of_truth_map.md` and `project_status.md`: 132 of 169 source-manifest
rows are complete and 37 are blocked (15 portraits, 7 symbols/documents, and
15 event/news records), with no remaining user-review rows. Five cleared FRUS
event/news packages are now consumed by the four H04 emergency-news nodes and
the F15 neutral-markings node. The exact sourced event/news budget is still
short 15 blocked slots; no fallback or substitute asset is used.

## Outcome

The current-state ledger is [source_of_truth_map.md](source_of_truth_map.md). It is the resume packet for the next implementation pass. Canonical specifications under `docs/specs/ireland_focus_tree/` were preserved. No gameplay, localisation, interface, GFX, history, common, event, or asset source was edited.

The cleanup distinguishes structural implementation evidence from live proof. The feature remains incomplete: source clearance is blocked, live engine/reference and scenario validation are not-run, global MCP diagnostics are not clean repository proof, and two decision-system follow-ups remain queued.

## Files changed

- `docs/plans/ireland_focus_tree/source_of_truth_map.md` — new authority map, status ledger, disposition table, contradiction list, stale-document list, and parent decision queue.
- `docs/plans/ireland_focus_tree/documentation_cleanup_handoff.md` — this handoff.
- `docs/plans/ireland_focus_tree/00_project_plan.md` — points the working program at the normalized status map.
- `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_finding_disposition.md` — normalized `integrated` to `implemented`, corrected the event/news clearance count to 48, and added exact evidence paths.
- `docs/plans/ireland_focus_tree/project_status.md` — points current status to the authority map and separates historical planning measurements.
- `docs/plans/ireland_focus_tree/part_7_validation_report.md` — clarifies that its single blocker count is historical planning-gate scope.
- `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md` — corrected 68 to the manifest-backed 48 and added status authority.
- `docs/plans/ireland_focus_tree/audits/focus_tree_audit_2026-07-18.md` — marked old missing-setter/AI/icon claims as historical while retaining layout evidence.
- `docs/plans/ireland_focus_tree/audits/ireland_country_package_audit_2026-07-18.md` — marked superseded route/identity/icon claims.
- `docs/plans/ireland_focus_tree/audits/ireland_decisions_missions_gui_audit_2026-07-18.md` — marked superseded lifecycle claims and retained open escalation/tooltip gates.
- `docs/plans/ireland_focus_tree/audits/ireland_decisions_missions_gui_reaudit_2026-07-18.md` — recorded structural counter/GUI status and queued telemetry/tooltips.
- `docs/plans/ireland_focus_tree/audits/ireland_feature_completion_audit_2026-07-18.md` — expanded its historical supersession note.
- `docs/plans/ireland_focus_tree/audits/ireland_localisation_audit_2026-07-18.md` — separated direct coverage evidence from stale runtime findings.
- `docs/plans/ireland_focus_tree/localisation/localisation_handoff.md` — marked the 3,015-key worker snapshot superseded.
- `docs/plans/ireland_focus_tree/repo_explorer_handoff.md` — marked the stale empty-checkout exploration superseded.
- `docs/plans/ireland_focus_tree/assets/ireland_generated_gfx_handoff.md` and `docs/plans/ireland_focus_tree/assets/gfx_handoff.md` — clarified worker scope versus current registration evidence.
- `docs/plans/ireland_focus_tree/ireland_decision_mission_gui_reaudit_followup.md` — added a resume/status note so completed structural work is not repeated.
- `docs/slopx_ireland_systems.md` — added the current status and evidence boundary.

## Disposition summary

| Disposition | Current meaning | Evidence |
| --- | --- | --- |
| Implemented | Planning worker gate and the listed structural source surfaces have current evidence. | `docs/plans/ireland_focus_tree/source_of_truth_map.md` sections “Current status ledger” and “Static inventory and source-clearance ledger” |
| Partial | Structural repairs exist, but live behavior, route proof, visual review, or another accepted surface remains open. | Source-of-truth map; completion follow-up |
| Blocked | Source clearance and final implementation validation cannot be closed from the current evidence. | `docs/plans/ireland_focus_tree/assets/source_manifest.json`; `docs/plans/ireland_focus_tree/assets/clearance_audit.md`; completion follow-up |
| Queued | Shared escalation telemetry, dynamic requirement/cost presentation, and any optional audio selection remain owner decisions/implementation work. | `docs/plans/ireland_focus_tree/audits/ireland_decisions_missions_gui_reaudit_2026-07-18.md`; `docs/plans/ireland_focus_tree/ireland_decision_mission_gui_reaudit_followup.md`; source-of-truth map |
| Not-run | Live engine, fresh-save, scenario, AI, GUI, achievement, and final global-diagnostic checks were intentionally not run. | Completion follow-up; source-of-truth map |

No plan was promoted into the canonical spec, rejected, or deleted. Historical documents were marked in place rather than removed.

## Contradictions resolved

- The stale 68 blocked event/news count was corrected to 48 from the authoritative source manifest and clearance audit.
- Older missing-wiring claims for setters, AI plans, focus icons, route identity, mission counters, event gates, GUI consumers, and scripted localisation are now explicitly treated as historical where current source evidence contradicts them.
- The historical 3,015-key/no-scripted-localisation handoff and empty-checkout repo exploration are marked superseded.
- The historical Part 7 single-blocker count is explicitly scoped to its planning gate.

## Contradictions still open

- Source clearance remains open for the blocked canonical rows; Daniel Morrissey is now conditional C3 local-mod complete with credits retained, while the Father Edward Cahill portrait extension remains blocked.
- Shared escalation telemetry is not aligned with the per-family escalation flags; the parent must choose the accepted result model.
- Reusable dynamic cost/availability presentation is still queued.
- Live engine, scenario, AI, GUI, achievement, and final global-diagnostic proof is absent.
- Older audit bodies retain their original counts and findings by design; their supersession notes must remain visible if later documents are copied or archived.

## Validation and skipped checks

Read-only checks included current identifier inventories, source-manifest JSON status grouping, targeted stale-term searches, and path checks for the new documentation references. The curator did not launch HOI4, inspect binary assets, run live parsing, or execute scenarios. Those omissions are intentional and remain blockers rather than passes.

Remaining documentation risk: future implementation edits must update this map and the completion follow-up when a queued or blocked item changes. Do not mark the feature complete based only on the structural counts listed here.
