# Ireland Focus Tree Improvement Loop Execution Prompt

Feature slug: `ireland_focus_tree`

Subagent: `hoi4_improvement_loop_planner`

Required launch setting: `fork_context=false`

Mode: plan-only final design review

Output path: `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_report.md`

## Task

Review the complete Ireland overhaul planning package after Parts 1 through 6 and the Part 7 canonical reconciliation. Decide whether any broad design expansion is still needed. Use the stop condition and anti-bloat rule from `hoi4-improvement-loop`. Write either a concrete addendum or a closure handoff. Do not patch gameplay files, write implementation code, produce final localisation, or claim implementation completion.

The review must test the full package against its promise:

- large non-linear national focus architecture with political, internal, economic, military, diplomatic, Northern, expansion, cultural, hidden and late-game play
- The National Settlement as an adaptive internal struggle connected to leaders, parties, offices, laws, decisions, missions, events, crises and route access
- meaningful National Provision, National Readiness, active neutrality, foreign leverage and Northern Settlement systems
- complete route gameplay, tradeoffs, failures, recovery, AI, identity, conclusions and cleanup
- continuous historical, political, foreign, route and flavour events
- concealed cultural routes that preserve the documented-history to plausible-speculation to deliberate-absurdity boundary
- route-specific AI, achievements, assets, text direction and implementation handoffs
- no fallback routes, passive stores, tiny reward filler, free territory, free cores, free alignment, idea spam or unresolved placeholder sections

## Required reading

Read `AGENTS.md`, `hoi4-improvement-loop.md`, `hoi4-feature-planning.md`, `hoi4-focus-trees.md`, `hoi4-decisions-missions.md`, `hoi4-events.md`, `hoi4-feature-assets.md`, `hoi4-frame-animation.md`, `hoi4-text-audio-research.md`, `hoi4-mtth.md`, `hoi4-subagents.md`, and `hoi4_improvement_loop_planner.toml`.

Read these project plans:

- `docs/plans/ireland_focus_tree/00_project_plan.md`
- `docs/plans/ireland_focus_tree/project_status.md`

Read every canonical source file below:

- `docs/specs/ireland_focus_tree/ireland_focus_tree_index.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_1_research_and_architecture.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_2_constitutional_politics.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_3_radical_and_hidden_routes.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_4_statecraft_and_war.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_6_ai_assets_achievements_and_text.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_architecture_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_canonical_reconciliation_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_constitutional_routes_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_cross_surface_reconciliation_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_diplomacy_northern_and_late_game_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_economy_and_defence_routes_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_event_family_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_hidden_cultural_routes_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_mechanic_reconciliation_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_national_settlement_map.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_revolutionary_and_corporate_routes_map.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_achievement_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_ai_strategy_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_asset_ledger.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_constitutional_politics_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_foreign_reaction_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_lifecycle_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_radical_and_hidden_routes_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_route_coverage_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_statecraft_and_war_matrix.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_achievement_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_asset_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_coding_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_decision_mission_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_goal_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_text_audio_research_prompt.md`
- `docs/specs/ireland_focus_tree/research/ireland_focus_tree_historical_research_notes.md`

## Fixed constants and counts

Do not recommend changing these unless you find a real contradiction and name every affected file:

- National Settlement range `-100` to `+100`, opening `+25`, opening momentum `-1`, seven stages, seven-day confirmation, five-point return margin, route clamp `-60` to `+60`, six-month review
- Social Consent `55`
- National Readiness `15`
- British, Vatican, American and German Leverage openings `45`, `25`, `5`, `5`
- Dáil `153` formal seats and `152` routine votes, with Fianna Fáil `77` formal and `76` routine, Fine Gael `59`, Labour `8`, and others `9`
- National Provision components `55`, `25`, `40`, `30`, displayed `38`
- Readiness components `25`, `8`, `20`, `12`, `5`, `5`, `30`, displayed `15`
- Neutrality Integrity opening `72`
- Northern opening `U5 N40 L30 B10 S45 I10`
- exactly three persistent route-spirit families
- exactly thirteen decision categories
- global active mission caps `8`, `10`, and conditional `12`
- command power cost ceiling `60`
- exactly eighteen historical event-chain families
- exactly eighteen political crisis families
- exactly twelve foreign reaction families
- at least 236 flavour events and at least 484 player-facing events overall
- exactly 30 durable AI profiles and exactly ten temporary overlays
- exactly twelve foreign actor families and twelve primary reaction action classes
- exactly 32 achievements split 8 Hard, 12 Very Hard, 8 Campaign and 4 Hidden Mastery
- exactly 60 sourced real-person portrait slots
- exactly 40 historical symbol and document packages
- exactly five source-clearance states and an eleven-tier source hierarchy
- one historical base flag set and 18 alternate route flag sets
- minimum 216 focus icons, 13 category icons, 70 decision icons, 54 mission icons, 63 persistent-spirit icons, 27 temporary-state icons, 51 law icons, 45 mechanic icons and 32 achievement concepts
- exactly 120 event and news images, 69 sourced and 51 generated
- exactly three scripted GUI surfaces
- exactly seven animations with independent source frames and static fallbacks
- exactly three optional audio briefs
- Northern cores only after integration stage `5` and final regional review
- the complete canonical Dillon intervention gate from Part 4

## Required review dimensions

1. Route completeness and non-linearity, including every one of the 30 profile roles and the fifteen standard conclusion families plus the composite convergence review.
2. Branch interaction among politics, economy, defence, diplomacy, Northern Ireland, culture and late-game play.
3. Decision and mission pressure, material costs, partial success, failure, cleanup and anti-exploit design.
4. Event continuity, route-specific flavour, historical context and meaningful effects.
5. AI route validity, temporary overlays, hidden-route prohibition, foreign actor capability and recovery.
6. Country identity, offices, laws, leaders, parties, flags, claims, occupation, integration and core lifecycles.
7. Asset sourcing, source clearance, generated-art boundaries, GUI, animation and optional audio.
8. Achievement difficulty, tracking and anti-shortcut rules.
9. Historical grounding and the `H`, `P`, `A` boundary.
10. Repetition, duplicate systems, excessive maintenance burden and further-expansion risk.

## Required output

Write one report with:

- recommendation: `expansion addendum` or `closure handoff`
- reviewed source set
- unresolved prior addenda, if any
- findings with stable IDs, severity, evidence paths and concrete disposition recommendation
- any proposed additions, with affected implementation surfaces and anti-bloat justification
- any proposals rejected as bloat, with reason
- final small tasks required before the parent may close planning
- whether any finding should be promoted into `docs/specs/ireland_focus_tree/`
- explicit statement that the report does not prove gameplay implementation

Do not leave a finding unclassified. Do not repeat accepted design merely to increase report size. Prefer closure when the package already supplies route depth, connected mechanics, AI, consequences, assets and implementation handoffs.
