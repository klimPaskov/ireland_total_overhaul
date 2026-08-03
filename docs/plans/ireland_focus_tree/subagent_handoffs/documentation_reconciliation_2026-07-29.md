# Ireland documentation reconciliation handoff - 2026-07-29

Feature: `ireland_focus_tree`
Role: documentation curator
Scope: the five parent-granted documentation files plus this handoff. No
gameplay, localisation, GFX, asset, spec, manifest, or clearance source file
was edited.

## Parent reconciliation addendum

After this subagent returned, the parent finished merging the round-3A and
round-3B source packages and reconciled the files in this handoff. The settled
machine-manifest baseline is 47 complete / 55 `needs_user_review` / 67 blocked;
families are portraits 11/32/17, symbols 7/11/22, and event/news 29/12/28.
Clearance is C1/C2/C3/C4 = 40/30/74/25 and tiers T1..T11 =
45/18/29/24/7/9/19/9/7/0/2. All twenty-three round-3 candidates remain
staging-only. The NR07 early-admission defect is source-fixed and bounded
verification passed. The older in-flight counts and “parent patching NR07”
statements retained below describe the subagent's handoff-time observation and
are superseded by this addendum and `source_of_truth_map.md`.

## Handoff-time source-of-truth ledger

The latest parent-supplied audit baseline for the read-only
`docs/plans/ireland_focus_tree/assets/source_manifest.json` is authoritative for
this reconciliation. It specifies 169 entries:

- Overall: 47 complete / 46 `needs_user_review` / 76 blocked.
- Families: portraits 11/32/17, symbols 7/11/22, event/news 29/3/37
  (complete/review/blocked).
- Clearance: C1 52, C2 28, C3 64, C4 25.
- Tiers: T1 50, T2 15, T3 29, T4 27, T5 4, T6 9, T7 17, T8 9, T9 7,
  T10 0, T11 2.

The ten exact NLI/UCD leads that advanced from C1 to C2 while remaining
blocked are S-06, S-07, S-08, S-09, S-12, S-13, S-15, S-18, S-19, and S-20.
The new symbol review IDs are S-04, S-11, S-14, and S-21. The previously
integrated round3A event and round3B symbol review candidates remain review
only. None of these source-status changes promotes a runtime asset.

Current static event-source mappings are EV-SRC-003 -> event .109,
EV-SRC-021 -> .110, EV-SRC-039 -> .111, and EV-SRC-057 -> .254. Runtime
consumed budget assets are 80/80 complete; the overall 120-image budget is
80/120 complete. Exactly three GUI windows inspect as 58/40/36 elements, but
local validation remains `false` with source-graph diagnostics and predicted
overlaps. The runtime inventory is 878 DDS files total and 877 Ireland-owned;
the Ireland GFX audit records 1,106 texture references and 346 unique sprite
names. FG-001 through FG-007 remain implemented.

The parent-owned manifest was changing concurrently and was not in this
subagent's write set. A read-only parse during the pass observed 47 complete /
49 review / 73 blocked, and a later read was still changing; this conflicts
with the supplied 47/46/76 baseline. Current-status surfaces intentionally use
the supplied baseline. The parent must settle the manifest and rerun the
ledger before closing this conflict.

Live testing, playthroughs, and fresh-save language remain excluded from the
completion gate by user direction. The seven-live-review-portrait defect and
NR07 early-admission defect remain unresolved. Current source reads contain
direct NR07 final-review-open gates in the four event blocks and dispatcher
limits, but the parent is patching NR07 and this handoff does not claim a fix.

## Source-of-truth and disposition order

1. Accepted feature specifications under `docs/specs/ireland_focus_tree/`.
2. Current implementation files as evidence of what is present.
3. The read-only canonical source manifest for source status and clearance.
4. The latest parent-supplied completion-audit facts recorded above.
5. Historical audits, reports, and worker handoffs, used only where their
   claims are explicitly marked historical or superseded.

## Plan and handoff disposition

| Surface | Disposition | Current state |
| --- | --- | --- |
| `source_of_truth_map.md` | updated/current | Latest manifest, family, clearance, tier, event-consumer, budget, GUI, portrait, and NR07 evidence is normalized here. |
| `project_status.md` | updated/current status surface | Parent-reconciled 47/55/67 ledger and unresolved non-live gates are current; older dated implementation notes remain historical. |
| `audits/ireland_gui_surface_reaudit_2026-07-29.md` | updated/current audit with historical evidence retained | 58/40/36 is current; local validation is `false`; the prior zero-element observation is explicitly superseded. |
| `audits/ireland_country_package_reaudit_2026-07-29.md` | updated/current structural audit | Latest family/status/clearance/tier facts, source consumers, budget, the unresolved portrait finding, and the fixed NR07 gate are current; prior measurements remain historical. |
| `improvement_loop/ireland_focus_tree_finding_disposition.md` | updated planning ledger | ILR-02/ILR-08 use the latest source queue; CA-004 moved from queued to implemented at static wiring level; CA-005 queues the new symbol/review disposition. FG-001..FG-007 remain implemented. |
| `assets/source_manifest.json` | canonical, read-only, unchanged | No manifest edit was authorized or made. |
| `assets/clearance_audit.md` | parent-reconciled after handoff | Current totals match the settled machine manifest. |
| Round3A/round3B source-research handoffs | evidence/queued, not promoted | Staged review candidates remain non-runtime; the symbols round3A handoff documents S-04/S-11/S-14/S-21 and the ten blocked NLI/UCD leads. |

No plan was promoted to a gameplay-complete claim. No plan or handoff was
deleted, merged into a new design, or silently rejected. No resume packet was
created; this handoff and the source-of-truth map are the resume surfaces.

## Contradictions and unresolved conflicts

Resolved on current-status surfaces:

- The earlier 47/42/80, 47/32/90, and handoff-time 47/46/76 asset snapshots
  are superseded by 47/55/67, with the latest family, clearance, and tier
  distributions.
- The earlier claim that EV-SRC-021, EV-SRC-039, and EV-SRC-057 were registered
  but unconsumed is superseded by the current .110/.111/.254 mappings; EV-SRC-003
  is mapped to .109. This is static source wiring, not a live firing claim.
- The GUI audit's old zero-element/missing-window observation is retained as
  historical evidence and superseded for current counts by 58/40/36. The
  validation result remains `false`, so no GUI completion claim is made.

Still open or outside this write set:

- `docs/plans/ireland_focus_tree/assets/clearance_audit.md` was outside the
  subagent's write set but was subsequently reconciled by the parent.
- Same-day supporting clearance audits and older source-research documents may
  still repeat earlier numeric totals or the unconsumed event claim. The latest
  manifest and current status surfaces supersede those statements, but those
  files were not in the granted write set.
- Seven review-gated portrait references remain live in route-character/GFX
  sources: P-05, P-06, P-27, P-43, P-46, P-56, and RC-PORTRAIT-01 Daniel
  Morrissey. No clearance or generated likeness substitution is claimed.
- The GUI source-graph diagnostics and predicted overlaps remain unresolved.
- The NR07 defect is source-fixed; the full comparison timeout remains a
  tooling limitation.
- The Radical/Underground capacity wording conflict and the unsupported
  staged-achievement visibility contract remain canonical/schema conflicts.
- All twenty-three round-3 review candidates remain pending later clearance or
  rejection decisions; the ten exact blocked NLI/UCD leads remain blocked
  after their C1 -> C2 move.

## Duplicate, superseded, and stale-document risks

- The old GUI inspector result is preserved inside
  `audits/ireland_gui_surface_reaudit_2026-07-29.md`, not deleted.
- The old country-package measurements are preserved inside
  `audits/ireland_country_package_reaudit_2026-07-29.md`, not rewritten as
  current facts.
- `assets/clearance_audit.md` and the older same-day source-clearance reports
  remain historical/supporting evidence where they disagree with the latest
  manifest.
- `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_report.md`
  remains an explicit alias, not a second planner report. The execution report
  and normalized finding ledger remain the planning evidence.
- `docs/plans/ireland_focus_tree/repo_explorer_handoff.md` retains stale
  empty-checkout/rebuild instructions and must not drive new work.
- `docs/plans/ireland_focus_tree/localisation/localisation_handoff.md` retains
  an old 3,015-key worker snapshot and is not current coverage authority.
- `docs/plans/ireland_focus_tree/assets/ireland_generated_gfx_handoff.md` and
  `assets/gfx_handoff.md` contain worker-scope statements that must not be read
  as proof that current interface registrations are absent.
- Canonical coding and goal prompts under `docs/specs/ireland_focus_tree/`
  were not changed; no stale canonical prompt was identified in this pass.

## Parent decisions and recommended next actions

1. Resolve the seven live review-gated portrait references without a generated
   likeness fallback.
2. Decide clearance/rejection for all twenty-three round-3 review entries;
   keep all review DDS files out of runtime until their row-specific rights and
   semantic gates are accepted.
3. Track the ten blocked NLI/UCD leads as blocked despite their C1 -> C2
   advance; do not interpret the clearance promotion as runtime approval.
4. Review the GUI source-graph diagnostics and predicted overlaps while
   retaining 58/40/36 as the current inspected element counts.
5. Retain the NR07 full-comparison timeout as a tooling limitation; no further
   source patch is required for the early-admission gate.

## Changed files and validation

Changed by this reconciliation:

- `docs/plans/ireland_focus_tree/source_of_truth_map.md`
- `docs/plans/ireland_focus_tree/project_status.md`
- `docs/plans/ireland_focus_tree/audits/ireland_gui_surface_reaudit_2026-07-29.md`
- `docs/plans/ireland_focus_tree/audits/ireland_country_package_reaudit_2026-07-29.md`
- `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_finding_disposition.md`
- `docs/plans/ireland_focus_tree/subagent_handoffs/documentation_reconciliation_2026-07-29.md`

The finding-disposition file contained parent work before this reconciliation;
those changes were preserved. No file outside this list was modified by this
subagent.

Meaningful read-only checks:

- Parsed the manifest shape and confirmed 169 entries. The parent subsequently
  settled it at 47/55/67 overall, 11/32/17 portraits, 7/11/22 symbols,
  29/12/28 event/news, C1/C2/C3/C4 40/30/74/25, and T1..T11
  45/18/29/24/7/9/19/9/7/0/2.
- Confirmed the exact review IDs and the ten blocked NLI/UCD leads listed above.
- Inspected event source and GFX registration evidence for EV-SRC-003/.109,
  EV-SRC-021/.110, EV-SRC-039/.111, and EV-SRC-057/.254.
- Confirmed the source-level NR07 direct gates; the parent subsequently closed
  the source defect with bounded verification.
- Recorded the supplied static-audit metrics for 878 DDS files, 1,106 texture
  references, 346 unique sprite names, 58/40/36 GUI elements, and the 80/80
  consumed versus 80/120 overall image budgets. Parent-owned GFX/runtime
  surfaces were outside scope and were not used to override those supplied
  audit metrics.
- A final `git diff --check` and write-scope diff review are required before
  the parent integrates this work.

Skipped by design: HOI4 launch, live engine parsing, live GUI interaction,
playthroughs, fresh saves, AI simulation, binary visual inspection, and
achievement scenarios. User direction excludes live testing/playthrough/fresh-
save language from completion gates. No completion claim is made here.
