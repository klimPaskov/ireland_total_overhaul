# Cabinet Briefing implementation contract

The accepted implementation is the compact four-card Cabinet Briefing described by this spec package and the correction addendum under `docs/plans/ireland_mechanics_hub/improvement_loop/`.

Maintenance rules:

1. Keep exactly Government, National Supply, Defence, and National Question.
2. Do not restore the six-tab or selectable-row ledger.
3. Do not add a manual refresh action.
4. Keep only the next guarded Parliament action, hidden when unavailable.
5. Use the same status triggers and scripted-localisation branches in both the decision panel and focus inlay; keep the inlay informational because its button API cannot hide unavailable controls.
6. Hide internal route/profile reconciliation from focus effect tooltips.
7. Re-run GUI inspection/render and focus inspection/render after any layout or binding change.
8. Reject new permanent cards unless a separate accepted design proves a distinct, player-controlled strategic purpose.
