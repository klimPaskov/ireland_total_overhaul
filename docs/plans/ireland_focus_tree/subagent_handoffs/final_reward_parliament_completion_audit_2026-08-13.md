# Final reward and Parliament completion audit — 2026-08-13

## Verdict

**COMPLETE.** No blocker, omission, fallback, or undisclosed simplification
remains in the requested focus-tree reward/layout and Parliament scripted-GUI
surfaces.

## Source-backed closure

- `common/national_focus/ireland_focus_tree.txt` contains 150 unique focuses,
  150 unique coordinates, exactly three ungated opening roots, and three
  opening shortcuts. Authored bounds are `x = -20..21`, `y = 0..16`.
  Focus-inspect revision `b1c47582375c4bad` reports zero crossings, zero
  connector-through-node intersections, zero long connectors, and zero
  same-row spacing defects.
- Every focus calls its exact `ireland_<focus>_reward_tt` key. All 150 keys
  resolve, are non-empty, and have distinct focus-specific text. The seven
  previously identified omissions now name their actual research, claim,
  equipment, building, convoy, and experience effects.
- Direct source classification confirms 32 material/construction/fuel focus
  IDs, 24 capability focus IDs, one legal-claim focus, and 59 focus IDs with
  60 named unlock calls covering 58 existing decisions or missions. Political,
  cultural, diplomatic, Northern, institutional, and capstone focuses use
  named route, Parliament, decision, mission, ledger, proof, institution, or
  conclusion outcomes rather than arbitrary material padding.
- `interface/ireland_parliament_scripted_gui.gui` implements the lowered white
  title, two `247x126` chamber cards, large `126x70` seat strips, and four
  visible `204x32` programme buttons. GUI revision `3afccc6805fec771` reports
  no visible overlap.
- `common/scripted_guis/ireland_scripted_guis.txt`,
  `common/scripted_effects/ireland_parliament.txt`,
  `common/scripted_triggers/ireland_parliament.txt`, and
  `common/decisions/ireland_decisions.txt` give all four human controls and
  native AI actions the same guarded executors. Costs remain 15/25/25/35
  Political Power. The starting Dáil decision is human-visible and actionable
  from initialization when its Political Power and Dublin requirements are
  met. Completion flags and executor-side checks prevent duplicate or free
  execution.
- Parliament titles, coloured values, action labels, focus prerequisites, and
  action tooltips resolve in `localisation/english/ireland_l_english.yml` and
  match the stable lifecycle.

The GUI analyzer's inability to follow click wrappers into the shared
Political Power executors, resolve live chamber variables, or fully model
`buttonstate.lua` is an analyzer limitation. Direct source resolves each of
those contracts, so none is a defect.

## Plans, assets, documentation, and validation

The current reward-density and Parliament completion report, source-of-truth
map, specs, improvement-loop disposition, and specialist closure handoffs agree
with the final source. No accepted plan remains unresolved in these surfaces.
Existing Parliament background, chamber, button, and four-state seal assets
are present and wired; no new asset is required. The task-specific focus and
GUI inspections above are current. No additional improvement-loop planner pass
is recommended because the accepted depth and correction work is implemented
and another expansion would add scope rather than close a gap.

No gameplay file was edited by this audit. This report is the only file added.
