# National Situation Ledger implementation prompt

Status: implemented on 2026-08-15; retained as the historical acceptance checklist. It is not an open implementation request.

Implement the accepted Ireland mechanics-hub specification without changing the underlying balance or route logic.

## Ordered work

1. Add shared mechanic-hub triggers and effects using existing recompute/review/executor helpers.
2. Initialize and clean up selection-only variables; ensure displayed-value producers dirty the shared GUI counter.
3. Add the `ireland_national_situation` decision category and `ireland_national_situation_scripted_gui`.
4. Build `interface/ireland_national_situation.gui` on the existing 510 by 590 background.
5. Add dynamic localisation for tabs, rows, statuses, selection explanations, purposes, and exact action requirements.
6. Add the vanilla focus-inlay definition, compact GUI, scripted images/buttons, and focus-tree declaration.
7. Wire existing assets; create new art only if the explicit asset gate fails.
8. Inspect and render the dashboard at 1920 by 1080 and 2560 by 1440 across opening, locked, warning, critical, revealed Northern, concealed evidence, revealed evidence, and long-text states.
9. Inspect/render/raster the focus tree and confirm the inlay overlaps no node or connector.
10. Run the improvement loop, implement or explicitly disposition its findings, then run focus, decision/mission, localisation, and completion audits.

## Non-negotiable constraints

- No displayed value lacks a named purpose and gameplay consumer.
- No button duplicates an executor, bypasses a cost, or grants a free outcome.
- No internal cursor/cache/preview value is exposed as a player mechanic.
- No hidden evidence is leaked before its reveal gate.
- No focus prerequisite, reward, search filter, coordinate, AI weight, or route gate changes merely to place the inlay.
- No placeholder or fallback art.
- `thumbnail.png` remains untouched.
