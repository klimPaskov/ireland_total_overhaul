# Ireland decision, mission, and GUI re-audit follow-up

Status reconciliation (2026-07-22): the category counters/critical reservations and GUI selected-row request projections described as required decisions below are structurally present in the current source, but have not had live engine or scenario proof. The 54-family result path now uses exclusive escalation result 5 with shared telemetry, and all 140 actions use the reusable dynamic-cost presentation with the current highest scarcity band; named map-objective gates and partner-locked foreign channels are also wired. The current evidence ledger is `docs/plans/ireland_focus_tree/source_of_truth_map.md`; do not redo the completed structural checks unless new source changes invalidate them.

## Purpose

This is a parent-owned implementation handoff from the 2026-07-18 decision/mission/GUI re-audit. It deliberately does not alter routes, action families, mission count, or category ownership.

## Required design decisions before implementation

1. **Category concurrency and critical slots**
   - Preserve the current global capacity contract: 8 normal, 10 during national emergency or war, and 12 only during simultaneous national emergency and Northern occupation.
   - Add a separate derived active counter for each of the thirteen categories and use the map’s specified category caps.
   - Classify the existing mission families eligible for the one/two/three reserved critical slots. Routine work must stop before the global limit; eligible critical work may occupy the reserved capacity.
   - Keep the counter rebuild derived from the existing 54 active flags. Do not introduce a parallel mission system.

2. **Result and escalation telemetry**
   - Choose one model: (a) escalation is a second telemetry flag counted alongside failure, or (b) escalation is an exclusive terminal result with its own player-facing outcome.
   - Align all 54 timeout paths, `slopx_ireland_record_mission_result`, and localisation with that model. The current per-family `_escalated` flags must not disagree with a permanently-zero shared escalation counter.

3. **Player-facing requirements and dynamic costs**
   - Create one reusable decision availability/cost presentation pattern rather than hand-writing 194 custom blocks.
   - It must show the actionable named objective, regional requirement, active category/global capacity, and current Political/Command Power scarcity surcharge before confirmation.

4. **GUI interaction contract**
   - Either add a selected-row detail output for Conditions, Northern, and Evidence ledgers, or remove row click affordances and their unused state.
   - Keep Northern core review derived by its canonical trigger and daily runtime path. A GUI click must not become the only way for the AI to receive a core.

5. **Asset diagnostics**
   - Confirm whether `mechanic_ledger_ireland_001.dds` and `_002.dds` are intentionally registered under two sprite names. If intentional, document/suppress the inspector collision; otherwise assign distinct art.
   - Add explicit animation fallback metadata only if the asset workflow requires it; current GUI source already contains paired static elements with state predicates.

## Suggested implementation order

1. Category counters and critical-slot admission.
2. Result/escalation model and terminal cleanup ordering.
3. Reusable dynamic requirement/cost tooltip helper plus localisation.
4. GUI interaction decision and asset ownership follow-up.

## Audit source

See [`ireland_decisions_missions_gui_reaudit_2026-07-18.md`](audits/ireland_decisions_missions_gui_reaudit_2026-07-18.md) for exact counts, source identifiers, validation evidence, and the two narrow patches already applied.
