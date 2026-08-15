# Cabinet Briefing no-further-expansion handoff

Date: 2026-08-15
Feature: Ireland mechanics hub and national-focus inlay
Recommendation: close the design loop after bounded finalization

## Design problem and closure decision

The rejected National Situation Ledger exposed the internal structure of the mod instead of helping the player read Ireland's immediate strategic position. The accepted four-card Cabinet Briefing fixes that problem. No further mechanic or UI expansion is justified.

The final player-facing boundary should remain:

- Government as a qualitative constitutional and parliamentary judgement
- National Supply as the existing Provision aggregate number
- Defence Readiness as the existing Readiness aggregate number
- National Question as the current public settlement or integration stage
- one guarded next-Parliament action when a canonical step is available

Do not restore tabs, row selectors, manual refresh, Foreign Pressure or Culture cards, permanent component lists, diagnostic prose, cross-category navigation, a Northern review button, forced actions, new currencies, new pressures, or new card-specific mechanics. Those additions would recreate the value sprawl and navigation burden the user rejected.

Static presentation is the correct choice for this compact briefing. The existing status seals communicate state without motion. Animation would add noise to a surface meant for a quick cabinet-level reading.

## Current implementation evidence

- `interface/ireland_national_situation.gui` contains four fixed card icons, four labels, four status outputs, one short assessment, and one contextual action. It contains no tab, row, list, selector, or refresh control.
- `common/scripted_guis/ireland_scripted_guis.txt` binds only `ireland_briefing_context_action_click` on this surface, hides it when unavailable, and disables GUI use for AI.
- `common/scripted_effects/ireland_mechanics_hub.txt` delegates that action through `ireland_execute_next_state_action` to the existing guarded Dail, Seanad, confidence, or joint-budget executor. It creates no alternate reward path.
- `common/focus_inlay_windows/ireland_national_situation_inlay.txt` exposes the same four statuses and one guarded action. It has no refresh or secondary navigation.
- `common/scripted_localisation/ireland_localisation.txt` and the active Cabinet Briefing localisation present Government qualitatively, Provision and Readiness as the only aggregate numbers, and the National Question as a public stage or condition.
- The accepted correction at `docs/plans/ireland_mechanics_hub/improvement_loop/natural_cabinet_briefing_correction_2026-08-15.md` explicitly supersedes the six-tab, 34-record interaction model.
- An exact repository reference search found no current consumer for `GFX_ireland_mechanics_hub_tab_selected`, `GFX_ireland_mechanics_hub_row_selected`, or their former GUI element names. Their asset records are stale.

Current read-only `hoi4.gui_inspect` revision `2ec3189185cde94907cf9e57ecd77bd1487e20749f3c94a0c2abcde3f1c643f7` parsed and linked `ireland_national_situation_window` without a blocking source-graph error. Its generic scenario could not size the four context-aware value strings and treated mutually exclusive status sprites as simultaneously visible. The resulting clipping and overlap warnings are not closure evidence. They require a value-driven render before the parent freezes the completion report.

## Research and precedent basis

The offline Scripted GUI and Interface Modding references support a small fixed decision-category window with scripted visibility and one shared action. Vanilla `AST_cabinet_trust_ui` and `usa_congress_decision_ui` demonstrate compact decision-category summaries driven by existing state rather than diagnostic navigation. Vanilla focus-inlay documentation supports the same limited information and button pattern in the focus view.

The four papers also follow Ireland's established campaign institutions. Government belongs to the Dáil and Seanad programme, National Supply to the island's food, power, transport, and maritime constraints, Defence Readiness to neutrality and service preparation, and the National Question to partition and the Northern settlement. These connections are already present in the mod. They do not justify another historical subsystem or a new research package.

## Finalization required before parent completion

1. Promote the accepted four-card correction into `docs/specs/ireland_mechanics_hub/` and reconcile `docs/ireland_national_situation_ledger.md`, the mechanics-hub completion report, asset manifest, and GFX handoff. They still describe six families, 34 records, refresh controls, selected markers, or two inlay actions.
2. Mark the old selected-tab and selected-row assets as retired or unconsumed. Review the category icon because its manifest still describes six coloured ledger tabs. Reuse it only if the rendered 52 by 40 icon reads as a general cabinet paper rather than the rejected six-tab model. This is a bounded asset correction if replacement is necessary, not a new visual system.
3. Run value-driven GUI inspect and render scenarios at 1920x1080 and 2560x1440 for locked, warning, critical, ready, archived, action-available, action-hidden, and long-text states. Confirm one status seal per card, readable aggregate values, no dead click region, and no clipping.
4. Confirm the visible Defence card uses the accepted Defence Readiness terminology and that every card tooltip remains within the six-short-line contract.
5. Recheck the focus inlay against the current focus layout and complete the final localisation, decision interaction, focus-layout, asset-wiring, and feature-completion audits after the documentation promotion.

## Queued and nonblocking cleanup

- Dead compatibility localisation, selected-tab or selected-row helpers, and refresh-only helpers may be removed after an exact reference audit. Their existence is maintenance debt, not a reason to delay the four-card design or expose them again.
- Existing category icons, status seals, and the quiet panel background may remain if current render evidence confirms readability. No new asset family or animation package is recommended.
- The previously queued `NSL-Q-01` cross-category navigation experiment should be rejected for this feature. Native Northern, cultural, foreign, provision, and readiness surfaces already own their detailed interaction.

## Prior addendum and promotion status

`national_situation_ledger_corrective_addendum_2026-08-15.md` records its P0 and P1 corrections as implemented, but its six-tab interaction model is superseded by the accepted Natural Cabinet Briefing correction. The Natural Cabinet Briefing correction remains the only accepted unresolved design record until the parent completes the finalization tasks above and promotes it into the source specification.

This closure handoff should remain under `docs/plans/ireland_mechanics_hub/subagent_handoffs/`. It should not be promoted as a new feature spec. The accepted four-card design itself should be merged into `docs/specs/ireland_mechanics_hub/`, after which the superseded ledger language should be clearly retired.

## Parent handoff

- Proposed expansion: none
- Closure reason: another mechanic, card, action, navigation layer, or visual state family would add bloat and weaken the accepted glanceable briefing
- Implementation surfaces affected by finalization: mechanics-hub specs and docs, asset records, Cabinet Briefing localisation, decision-category GUI validation, focus-inlay validation, and final audit records
- Open design questions: none
- Open implementation evidence: value-driven GUI renders, final focus-inlay placement proof, and documentation plus asset-record reconciliation
- Files written by this planner: `docs/plans/ireland_mechanics_hub/subagent_handoffs/cabinet_briefing_no_further_expansion_2026-08-15.md`
