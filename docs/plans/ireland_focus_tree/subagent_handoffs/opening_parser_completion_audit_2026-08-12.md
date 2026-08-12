# Opening Visibility and Parliament Parser Completion Audit

Date: 2026-08-12  
Feature slug: `ireland_focus_tree`  
Mode: read-only gameplay audit; this handoff is the only file written

## Verdict

**Complete; the stale final-audit claim identified during review has been superseded and corrected.**

The four Parliament `ai_hint_pp_cost` fields are parser-compatible and retain
the existing executable Political Power costs. The focus source exposes only
three opening trunks and conceals all seven later ordinary families behind
`allow_branch` conditions that match their complete `available` conditions.
Daily Ireland-scoped layout invalidation allows those families to reveal as
their conditions become true. The canonical specification, current completion
report, source-of-truth map, project-status checkpoint, and shortcut
localisation all describe the corrected three-trunk contract.

No gameplay fallback, omission, or simplification was found in this bounded
correction. The older final-audit handoff is explicitly superseded for opening
visibility and now records the current three-shortcut, fifteen-gate,
`c1112c666cadee8b` state.

## Completion status by surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Parliament parser repair | Complete | `common/decisions/ireland_decisions.txt:21-24,214,246,278,310` defines and consumes four file-local numeric macros. No `ai_hint_pp_cost = constant:` token remains under `common/`. Vanilla decision precedents use literal integer values, and the offline Decision Modding reference describes this field as a constant amount. |
| Executable Parliament costs | Complete and unchanged | `common/script_constants/ireland_constants.txt:49-60` remains the executable cost/delta/gate table at `15/25/25/35`; the gameplay diff changes only the hint representation. The matching action labels and custom-cost text remain `15/25/25/35` in `localisation/english/ireland_l_english.yml:3429-3443`. |
| Opening focus visibility | Complete in current source | The only ungated structural opening roots are `ireland_state_still_defined`, `ireland_economic_war_review`, and `ireland_defence_estimates` (`common/national_focus/ireland_focus_tree.txt:36,95,131`). The tree declares exactly three shortcuts at lines 29-31. |
| Progressive later reveal | Complete in current source | Seven ordinary later roots use `allow_branch` at lines 1084, 1169, 1234, 1296, 1989, 2392, and 2580. Normalised source comparison found every gate identical to its root's full `available` block, including the stabilised Cultural Survey, Establish Naval Staff, and Strict Neutrality blocks. The pre-existing eight crisis/radical/evidence gates remain, for fifteen reveal roots total. |
| Layout refresh | Complete at static-source boundary | `common/on_actions/ireland_on_actions.txt:39` invokes `mark_focus_tree_layout_dirty = yes` inside `on_daily_IRE`, so satisfied reveal conditions are re-evaluated without a world-wide on-action scan. |
| Shortcut localisation | Complete | Exactly three shortcut labels remain at `localisation/english/ireland_l_english.yml:4111-4113`; no removed shortcut key is referenced by the current focus source. |
| Canonical/current documentation | Complete | The three-trunk contract is present in `docs/specs/ireland_focus_tree/ireland_focus_tree_index.md:175`, `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_2_constitutional_politics.md:4747-4754`, `docs/plans/ireland_focus_tree/source_of_truth_map.md:28-38`, `docs/plans/ireland_focus_tree/project_status.md:9-18`, and `docs/plans/ireland_focus_tree/focus_tree_parliament_completion_2026-08-09.md:9-32`. |
| Historical/final audit alignment | Complete | `final_feature_completion_audit_2026-08-12.md` is explicitly superseded for opening visibility and its current-state table records three shortcuts, fifteen gates, and revision `c1112c666cadee8b`. |
| Assets | Not applicable | This correction changes parser-safe hint values, focus presentation gates, and text contracts only. It creates no new visual or audio asset requirement. |

## Accepted plans and disposition

- The 2026-08-11 correction addendum is implemented. Its opening-correction
  section explicitly supersedes its earlier seven-simultaneous-lane language
  and requires no more than three opening trunks; the historical paragraphs can
  remain because the supersession boundary is explicit.
- The earlier layout/reveal direction is superseded for opening presentation.
  Its retained historical evidence does not override the later correction.
- The corrected contract has been promoted into canonical Part 2 and the spec
  index, then reflected in the current completion report, project status, and
  source-of-truth map.
- The focused Parliament parser handoff
  `subagent_handoffs/parliament_cost_parser_audit_2026-08-12.md` independently
  reaches the same parser/cost conclusion. No accepted plan remains queued for
  the bounded gameplay correction.

## Meaningful validation

- Direct search found zero malformed `ai_hint_pp_cost = constant:` assignments
  and exactly four corrected macro-backed Parliament hints. Their expanded
  values are `15`, `25`, `25`, and `35`, equal to the executable script-constant
  values and displayed costs.
- Structural parsing of all 150 focus blocks found ten roots without visual
  prerequisites: three opening roots and seven ordinary roots protected by
  false-at-opening `allow_branch` conditions. All other later route families
  retain their existing eight presentation gates.
- A normalised block comparison found exact `allow_branch`/`available` equality
  for all seven newly presentation-gated roots. This prevents a branch from
  appearing before its first focus is actually available.
- Fresh focus inspection revision `c1112c666cadee8b` reports 150 focuses and
  connectors, zero crossings, zero connector-through-node intersections, zero
  long connectors, zero same-row spacing defects, and no Ireland focus
  diagnostics. Artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8e37b3d8fcc978bbf66674414714882544fc5cff8323faf385d1767986d682e9/0b87357b7b1ecce8e9b5ace730122d922763cb6bc052ff602b2eb53bc3219d66/focus-inspect.c1112c666cadee8b.json`.
  The inspector's `branchCount = 0` is not semantic branch evidence, so the
  opening-budget finding is based on direct source structure and gate analysis.
- No live engine-start observation is claimed; confidence is static-source plus
  current MCP inspection. This does not conceal a failed runtime test.

## Missing or simplified requirements

No gameplay or documentation requirement in this correction is missing or
simplified. No fallback was introduced.

## Required next action

None. The documentation-only repair identified by this audit is complete.

## Improvement-loop recommendation

Do not route this correction to `hoi4_improvement_loop_planner`. It is a narrow
parser and opening-presentation repair, the intended design is already explicit
and implemented, and no uncovered depth gap requires a new addendum.
