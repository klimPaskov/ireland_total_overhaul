# Ireland Focus Tree Improvement-Loop Execution Report

Feature slug: `ireland_focus_tree`

Review role: mandatory improvement-loop planning gate

Report status: design review complete, gameplay implementation not proven

Recommendation: stop broad design expansion and proceed to implementation integration. Do not close the feature yet.

## Executive judgment

The canonical Ireland pack already specifies the promised depth. It contains a shared opening crisis, a non-linear focus architecture, constitutional politics, the National Settlement, National Provision, National Readiness, active neutrality, foreign leverage, Northern settlement, revolutionary and corporate routes, concealed cultural routes, route-specific conclusions, decisions, missions, events, lifecycle cleanup, AI, achievements, assets, GUI, animation, and research gates.

Adding another route family, decision category, country package, formable, GUI surface, or mechanic would duplicate existing design and increase implementation risk. The correct improvement-loop result is therefore a stop on broad expansion, with a bounded integration handoff before coding.

The repository implementation does not yet deliver the playable promise. The current runtime surface contains one empty event namespace and 13 All-Island flag files. There are no Ireland focus, decision, mission, event, idea, country setup, history, AI, localisation, GUI, GFX registration, achievement, audio, or scripted-system files. This is an implementation gap, not evidence that the canonical design is shallow.

## Playable promise to preserve

Ireland begins as a materially weak sovereign constitutional state whose Civil War memory, partition, economic dependence, Church influence, parliamentary competition, republican networks, labour and rural politics, and wartime strategic exposure remain active problems.

The player must repeatedly answer three linked questions:

1. Who owns the republic and what authority can govern it?
2. How can independence and the island be defended with limited material capacity?
3. What national project justifies the sacrifices made to survive?

The National Settlement is the central adaptive struggle. It opens at `+25` with momentum `-1`, uses the fixed `-100` to `+100` range, seven opening stages, seven-day confirmation, a five-point return margin, a `-60` to `+60` route clamp, and a six-month review. Social Consent opens at `55`, National Readiness at `15`, and source-specific leverage opens at British `45`, Vatican `25`, American `5`, and German `5`.

Material systems must remain coupled to politics. National Provision uses Food `55`, Energy `25`, Transport `40`, Maritime `30`, and displayed opening value `38`. National Readiness uses Command `25`, Equipment `8`, Mobilisation `20`, Supply `12`, Warning `5`, Maritime Protection `5`, Intelligence `30`, and displayed opening value `15`. Neutrality Integrity opens at `72` and represents active policy, enforcement, intelligence, maritime decisions, humanitarian conduct, and diplomatic risk.

Northern claims, control, occupation, settlement, integration, and cores remain separate states of play. Northern cores are permitted only after integration stage `5` and final regional review. No route may turn a political victory into free territory, free cores, free alignment, or free military power.

The H/P/A boundary remains binding. H covers documented history and institutions. P covers grounded alternate leadership, political, revolutionary, federal, corporate, royal, investigative, and containment outcomes. A begins only after verified impossible sovereignty, sacral obligation, impossible pentarchy, Otherworld authority, or the final convergence. Cultural work must remain valuable when it produces no concealed route.

## Current depth and integration gaps

| ID | Severity | Finding | Evidence | Disposition |
| --- | --- | --- | --- | --- |
| ILR-01 | Critical | The runtime implementation is absent. The only gameplay script is `events/ireland_events.txt`, which contains only `add_namespace = ireland`. | Current repository file inventory under `common/`, `history/`, `localisation/`, `interface/`, `music/`, and `sound/` is empty. | Implement the canonical package in the dependency order already defined by `ireland_focus_tree_coding_prompt.md`. This is not a new design route. |
| ILR-02 | High | Existing All-Island flags are not a country package. They have no tag registration, country history, cosmetic identity, party lifecycle, leader, units, focus loading, or route trigger. | `gfx/flags/IRE_ALL_ISLAND*.tga` and their medium and small variants are the only Ireland-specific runtime assets. | Treat them as an asset lead requiring source and identity verification. Do not expose a formation or transformed country until the country package and map checks exist. |
| ILR-03 | Critical | The central mechanic can become a disconnected reward ladder if the National Settlement and companion values are implemented after route content. | Canonical Part 2, the National Settlement map, the mechanic reconciliation map, and the Part 5 lifecycle matrix require shared values to gate leaders, laws, offices, decisions, missions, events, AI, and conclusions. | Build identifiers, constants, scopes, flags, variables, cleanup helpers, and value presentation before focus rewards and route branches. |
| ILR-04 | Critical | Northern content is especially vulnerable to shortcut implementation. Claims, control, occupation, settlement, integration, and core review are distinct canonical surfaces. | Statecraft matrix, Northern Settlement map, lifecycle matrix, and route coverage matrix. | Require a separate state ledger and separate decision, mission, event, AI, and cleanup hooks for each stage. Cores remain post-integration only. |
| ILR-05 | High | Active neutrality can collapse into a passive modifier or a free political-victory route. | Part 1, Part 4, the diplomacy map, foreign reaction matrix, and AI matrix define incidents, access, weather cooperation, internment, shipping, intelligence, public legitimacy, and sovereignty safeguards. | Keep neutrality actions material, time-bound, and politically costly. Formal belligerency remains behind the complete Dillon intervention gate. |
| ILR-06 | High | The canonical event, decision, and mission volumes create lifecycle and clutter risk. | Part 5 requires 13 decision categories, 140 actions, 54 mission families, 18 historical event families, 18 crisis families, 12 foreign reaction families, at least 236 flavour events, and at least 484 player-facing events. | Use the fixed category caps of `8`, `10`, and conditional `12`, route and crisis filters, active mission caps, target cleanup, and family-level reuse. Do not reduce the counts by substituting generic filler. |
| ILR-07 | High | AI parity is unimplemented and hidden routes are unsafe if treated as ordinary focus choices. | AI matrix defines exactly 30 durable profiles and 10 overlays. AI-29 preserves the `P/A` containment transition. | Implement route validity, resource floors, foreign and Northern posture, overlay activation and exit, recovery behavior, and hard prohibitions on concealed A-route discovery by ordinary AI. |
| ILR-08 | High | Visual and text surfaces are only planned. The current repository has no `.gfx`, `.gui`, localisation, portrait, icon, event-image, sound, or music wiring. | Part 6, asset ledger, asset prompt, frame-animation prompt, and text/audio prompt. | Treat source clearance, real-person sourcing, generated-art boundaries, static fallbacks, frame sheets, and optional audio research as gates. Do not use placeholders or invented researched text. |
| ILR-09 | High | Documentation validation is not gameplay validation. | Part 7 validation reports 366 passed checks and one blocked gate for the missing returned planner report. | Run engine-facing syntax, focus layout, decision, event, GUI, asset, localisation, AI, and scenario audits after implementation. Keep the planning pass separate from completion claims. |
| ILR-10 | Medium | Supporting records state that the required worker report was unavailable and name `ireland_focus_tree_improvement_loop_report.md`, while this user-directed artifact uses `ireland_focus_tree_improvement_loop_execution_report.md`. | `improvement_loop_execution_record.md`, `improvement_loop_execution_prompt.md`, and this report path. | Parent must reconcile the expected report filename and record whether this artifact is the accepted worker output. Do not silently create a second competing report. |

## Accepted pre-coding addenda

These are integration addenda, not new mechanics. They operationalise the canonical pack so the implementer does not invent a smaller substitute or silently change ownership. They should remain in `docs/plans/ireland_focus_tree/` unless they alter the canonical design. The present review finds no reason to promote them into a new spec part.

### IL-A01: canonical runtime contract

Use the index, Part 7 reconciliation maps, fixed matrices, and coding prompt as one source-of-truth chain. The six numbered parts own substantive design. Matrices own exact counts, thresholds, rosters, and lifecycle checks. Maps own interfaces. Prompts own workflow. Plans provide evidence and disposition only.

Before route implementation, establish stable identifiers for the Ireland country package, the shared opening, every fixed mechanic value, route flags, conclusion families, decision categories, mission families, event families, AI profiles, overlays, achievements, and asset references. Centralise shared tuning in the appropriate script-constant or documented tuning surface. Avoid magic values and duplicate formation, cleanup, Northern, or route-transition effects.

Affected surfaces: `common/script_constants/`, country and history setup, focus tree files, decisions and categories, events and on-actions, ideas, scripted effects and triggers, scripted localisation, AI strategy, achievements, interface, GFX, localisation, and documentation.

Acceptance: the implementation can trace each canonical fixed count and constant to one owning source, and no route is added merely because an identifier was missing.

### IL-A02: shared opening before route branching

The first playable tranche must establish the sovereign Ireland package, the shared opening, National Settlement, Social Consent, National Provision, National Readiness, active neutrality, the starting army and material assumptions, and the opening event and decision surfaces. Political routes then transform the shared system rather than replacing it with isolated trees.

The focus architecture must retain early, middle, and late pacing. Support lanes such as economy, defence, diplomacy, culture, and organised society must interact with several political routes. Route rewards should unlock institutions, decisions, missions, laws, advisors, units, map work, diplomacy, or identity changes. Flat political power, stability, war support, or repeated spirit rewards cannot substitute for these systems.

Acceptance: a fresh 1936 scenario can enter the shared loop and make a meaningful policy choice before any historical or alternate route is complete. This is a vertical integration criterion, not permission to reduce the final route count.

### IL-A03: route, lifecycle, and conclusion contract

Implement route commitment, leader and office lifecycle, party and law lifecycle, persistent three-family spirit ceiling, temporary crisis states, failure, recovery, and conclusion review as one connected system. Every one of the 30 AI profiles must map to a separate conclusion or lawful host conclusion. The composite convergence remains the highest variant of the existing Otherworld and convergence family and does not create a sixteenth standard conclusion family.

Every route must have visible identity, a tradeoff, a failure state, a recovery path where the matrix requires one, an AI profile, route-specific event and decision behavior, and a material conclusion. No route may be implemented as a cosmetic name change or an isolated modifier stack.

Acceptance: route coverage can be audited against the 30-row matrix, the fifteen standard conclusion families, and the convergence entry without adding unbudgeted routes or spirits.

### IL-A04: Northern and neutrality separation contract

Northern actions must progress through the canonical ledger. A claim can open a diplomatic or military objective. It cannot grant control. Control can open occupation or settlement. Occupation can open integration work. Integration can qualify a final regional review. Only then can the core review occur.

Neutrality must remain active while Northern work, foreign leverage, maritime access, weather cooperation, intelligence, internment, and emergency law change its integrity and public legitimacy. Dillon's intervention route must require the complete material, parliamentary, sovereignty, home-reserve, and contribution gates from Part 4. No formal war, Allied alignment, or political conclusion may bypass these gates.

Acceptance: validation scenarios show partial Northern success, failed settlement, occupation strain, delayed cores, sponsor pressure, and neutrality backlash without granting free political victory material.

### IL-A05: AI, asset, and researched-text parity

AI must have an equivalent action path for every AI-usable decision and mission family. The ten temporary overlays must pause or reprioritise normal work, retain route history, and clean their temporary targets. Hidden A routes require verified evidence and must not be discovered by ordinary AI merely because a decision is technically visible.

The asset ledger remains exact: 60 sourced real-person portrait slots, 40 historical symbol and document packages, five clearance states, eleven source tiers, one historical base flag set, 18 alternate route flag sets, at least 216 focus icons, 120 event and news images split 69 sourced and 51 generated, three GUI surfaces, seven frame-based animations with independent source frames and static fallbacks, and three optional audio briefs. Source clearance C0 through C4 is a production gate. Research prompts provide direction, not final localisation.

Acceptance: no generated real-person portrait, fabricated historical symbol, unlicensed audio, invented quote, placeholder animation, or uncatalogued final DDS can be treated as complete.

### IL-A06: completion evidence contract

After implementation, the parent must run the canonical route-coverage, decision and mission, country package, localisation, asset, AI, focus-tree, event, GUI, and feature-completion audits. The implementation report must identify every simplification, omission, missing asset, missing AI path, queued plan, rejected finding, and blocker.

Required scenario coverage includes:

- January 1936 shared opening and National Settlement movement.
- 1937 constitutional drafting, campaign, plebiscite, election, and government formation.
- 1938 Treaty Port transfer, trade, finance, and defence consequences.
- September 1939 neutrality, Emergency law, supply, internment, intelligence, and maritime incidents.
- Provision and Readiness bottlenecks, recovery, and national-emergency overlay behavior.
- ordinary constitutional, Labour, agrarian, Church, republican, corporate, Ailtirí, and serious cultural routes.
- Dillon's complete intervention gate and failure outcomes.
- Northern confidence measures, settlement, control, occupation, integration, failed settlement, and delayed core review.
- concealed evidence, false leads, verified P/A transition, containment, and convergence disqualifiers.
- postwar demobilisation, reconstruction, conclusion review, and cleanup.
- AI profile validity, overlay priority, sponsor collapse, recovery, and hidden-route restrictions.

## Route and system interaction handoff

The shared political mechanic is the spine. Constitutional decisions, elections, confidence, offices, laws, organised society, and route commitments move the National Settlement and Social Consent. The values must in turn alter focus availability, decision visibility, mission priorities, event variants, AI queues, leader succession, and conclusion eligibility.

Economy and defence are support lanes with strategic consequences. Provision controls whether food, energy, transport, maritime access, housing, industry, and regional projects can sustain a route. Readiness controls command, equipment, mobilisation, supply, warning, maritime protection, and intelligence. A political route that ignores those values should fail or become dependent, not receive a free victory.

Active neutrality is a policy system shared by historical and alternate routes. It connects foreign leverage, shipping, weather, airspace, internment, intelligence, censorship, treaty-port access, humanitarian relief, public legitimacy, and the possibility of war. Foreign reaction families must change leverage, dependency, access, recognition, guarantees, debt, or sovereignty safeguards rather than appear as disconnected flavour.

Northern work interacts with diplomacy, Readiness, Provision, local consent, security, occupation administration, services, industry, labour, rights, British position, and postwar reconstruction. It must retain the separate Northern ledger values `U5 N40 L30 B10 S45 I10` at opening and must not collapse all-island politics into a single ownership trigger.

Serious cultural work connects language, archives, folklore, sites, regional identity, public institutions, and organised society to the current host government. It can open concealed evidence, but it must not automatically replace the host government's AI profile or create an A route. Verified impossibility is the only entry to A. The final convergence is a gated composite outcome, not a normal early-game branch.

Events, decisions, missions, focus rewards, ideas, AI, assets, and localisation are one lifecycle. Every active system needs entry, visible state, action, consequence, failure or partial success, follow-up, and cleanup. Obsolete decisions, missions, flags, event targets, temporary ideas, and GUI states must close when a route, war, occupation, sponsor, target, or conclusion ends.

## AI handoff

Use the exact 30 durable profiles and 10 temporary overlays from the AI matrix. Profiles must evaluate route validity, war state, stability, war support, industry, manpower, equipment, supply, foreign dependency, faction position, local support, territory, and conclusion requirements. They must refuse actions that lack material inputs, valid targets, valid sponsors, required states, required offices, or route permissions.

The historical profiles should prefer survival, constitutional authority, active neutrality, Provision, Readiness, and bounded foreign cooperation. Radical and corporate profiles may accept lower consent or higher exposure only within their mapped floors and costs. Concealed profiles remain locked behind evidence and route state. AI-08 Dillon cannot enter war without every fixed intervention gate. AI-29 must preserve the canonical `P/A` containment transition.

Overlays OV-01 through OV-10 take temporary priority during elections, constitutional crises, provision breakdown, invasion danger, declared war, Northern occupation and integration, sponsor collapse, office vacancy, postwar demobilisation, and conclusion review. Each overlay must retain history and clean only temporary targets when it ends. AI should not click a hidden GUI action simply because it is visible to the human player.

## Assets, GUI, animation, text, and audio

The current 13 TGA files are not evidence of a complete asset package. The implementer must verify whether they are the canonical historical base or route assets, document provenance and source clearance, and register them through the correct flag and cosmetic-tag surfaces. The asset ledger's one historical base flag set and 18 alternate route flag sets remain fixed.

The three GUI surfaces are the National Conditions Panel, Northern Settlement Ledger, and Concealed Evidence Ledger. Each needs readable state, costs, requirements, warnings, selected and locked states where relevant, and cleanup. GUI decoration cannot compensate for weak decisions or tiny rewards.

The seven animations require independent source frames, frame sheets, static fallbacks, manifests, and verified HOI4 sprite wiring. Transform-only motion is not acceptable. Animation should clarify availability, danger, progression, route reveal, or major identity change. Static surfaces should remain static when motion would add clutter.

Text and audio remain research-gated. Final player-facing wording must be written from the route direction in Part 6. Quotes, cultural remarks, slogans, title-like references, and optional audio require source, attribution, copyright or licence notes, and fit justification. No unresearched phrase should be promoted from a working label into localisation.

## Validation and audit plan

The Part 7 documentation validation is useful evidence for source completeness, with 366 passed checks, 0 failed checks, 0 warnings, and one blocked completion gate. It does not prove that the game loads or that a focus, decision, event, GUI, asset, AI, or localisation reference works.

The implementation owner should validate in this order:

1. Use the offline wiki pages and vanilla documentation already present in this workspace. Compare against the inspected vanilla focus, decision, event, GUI, GFX, and AI examples before writing each surface.
2. Validate the Ireland country package, starting forces, equipment and manpower assumptions, tag and identity lifecycle, focus loading, and flag registration.
3. Inspect and render the focus tree. Confirm non-linear layout, route locks, convergence, focus filters, varied rewards, and no dead-end reward spurs.
4. Inspect decisions and missions for caps, dynamic costs, named targets, active objectives, AI behavior, partial success, failure, and cleanup.
5. Inspect event roots and descendants, scope flow, dated hooks, crisis variants, foreign reactions, route events, Northern events, and conclusion cleanup.
6. Audit localisation keys, dynamic values, scripted localisation, source-researched text, asset references, GUI labels, achievement text, and UTF-8 BOM requirements.
7. Verify all sourced and generated assets, DDS dimensions, flag orientation, portraits, icons, event images, GUI sprites, frame sheets, static fallbacks, manifests, and optional audio licences.
8. Run the scenario matrix in IL-A06, including failed and partial outcomes, AI profiles, overlays, Northern integration, Dillon, concealed-route evidence, and postwar cleanup.
9. Reconcile the route coverage, achievement, asset, AI, foreign reaction, lifecycle, and decision matrices against the final implementation and report every variance.

## Prior addendum and blocker disposition

No prior accepted improvement addendum remains unresolved. The parent review findings IL-001 through IL-012 were recorded as integrated, queued, or blocked in `ireland_focus_tree_finding_disposition.md`. They are not new route requirements.

The supporting execution record says that no earlier custom worker report existed. This report is the requested current execution artifact, but the parent must resolve the filename mismatch between the canonical expected `ireland_focus_tree_improvement_loop_report.md` and the user-requested `ireland_focus_tree_improvement_loop_execution_report.md` before marking the gate satisfied.

The old supporting records also say the offline wiki and local game installation were unavailable. A current read-only probe found the offline wiki pages, the local vanilla documentation, and the local vanilla installation. The implementation owner should reclassify the old environment note as stale for this workspace, while still following the required local reference audit.

## Closure and stop recommendation

Stop the improvement loop for broad design expansion. The canonical pack already has enough route depth, connected mechanics, AI, consequences, assets, research gates, and conclusions. More content would create duplicate branches, more maintenance burden, and more opportunities for lifecycle drift.

Do not mark the feature complete. Runtime implementation is absent, the current flags are not a country package, the mandatory report filename must be reconciled, and all implementation-facing validation remains open. The parent may close the design loop after accepting this stop recommendation, then proceed through the existing coding prompt and final audits. Completion requires no unresolved accepted addenda, no fallback or placeholder content, no missing AI for AI-usable systems, no free Northern cores or political-victory material, and no remaining blocker.

## Source files read

Repository and skills:

- `AGENTS.md`
- `.agents/skills/hoi4-improvement-loop/SKILL.md`
- `.agents/skills/hoi4-feature-planning/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/hoi4-events/SKILL.md`
- `.agents/skills/hoi4-feature-assets/SKILL.md`
- `.agents/skills/hoi4-frame-animation/SKILL.md`
- `.agents/skills/hoi4-text-audio-research/SKILL.md`
- `.agents/skills/hoi4-subagents/SKILL.md`

Offline wiki pages read:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`

Vanilla documentation and precedents read:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_formatter_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_objects_documentation.md`
- Vanilla focus, decision, event, AI, GUI, and GFX precedents in `common/national_focus/uk.txt`, `common/national_focus/portugal.txt`, `common/national_focus/iceland.txt`, `common/decisions/political_decisions.txt`, `common/decisions/formable_nation_decisions.txt`, `common/decisions/categories/ICE_decision_categories.txt`, `events/Decisions_Events.txt`, `interface/countrydecisionview.gui`, `interface/countrydecisionview.gfx`, `interface/nationalfocusview.gui`, `interface/nationalfocusview.gfx`, `common/ai_strategy/ENG.txt`, and `common/ai_strategy/ICE.txt`.

Canonical specifications, maps, matrices, research, prompts, and supporting plan records:

- `docs/specs/ireland_focus_tree/ireland_focus_tree_index.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_1_research_and_architecture.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_2_constitutional_politics.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_3_radical_and_hidden_routes.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_4_statecraft_and_war.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_6_ai_assets_achievements_and_text.md`
- All twelve maps under `docs/specs/ireland_focus_tree/maps/`: `ireland_focus_tree_architecture_map.md`, `ireland_focus_tree_canonical_reconciliation_map.md`, `ireland_focus_tree_constitutional_routes_map.md`, `ireland_focus_tree_cross_surface_reconciliation_map.md`, `ireland_focus_tree_decision_and_mission_map.md`, `ireland_focus_tree_diplomacy_northern_and_late_game_map.md`, `ireland_focus_tree_economy_and_defence_routes_map.md`, `ireland_focus_tree_event_family_map.md`, `ireland_focus_tree_hidden_cultural_routes_map.md`, `ireland_focus_tree_mechanic_reconciliation_map.md`, `ireland_focus_tree_national_settlement_map.md`, and `ireland_focus_tree_revolutionary_and_corporate_routes_map.md`.
- All nine matrices under `docs/specs/ireland_focus_tree/matrices/`: `ireland_focus_tree_achievement_matrix.md`, `ireland_focus_tree_ai_strategy_matrix.md`, `ireland_focus_tree_asset_ledger.md`, `ireland_focus_tree_constitutional_politics_matrix.md`, `ireland_focus_tree_foreign_reaction_matrix.md`, `ireland_focus_tree_lifecycle_matrix.md`, `ireland_focus_tree_radical_and_hidden_routes_matrix.md`, `ireland_focus_tree_route_coverage_matrix.md`, and `ireland_focus_tree_statecraft_and_war_matrix.md`.
- `docs/specs/ireland_focus_tree/research/ireland_focus_tree_historical_research_notes.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_achievement_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_asset_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_coding_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_decision_mission_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_goal_prompt.md`
- `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_text_audio_research_prompt.md`
- `docs/plans/ireland_focus_tree/00_project_plan.md`
- `docs/plans/ireland_focus_tree/project_status.md`
- `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_execution_prompt.md`
- `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_execution_record.md`
- `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_parent_review.md`
- `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_finding_disposition.md`
- `docs/plans/ireland_focus_tree/part_7_final_gate_attempt_report.md`
- `docs/plans/ireland_focus_tree/part_7_package_manifest.md`
- `docs/plans/ireland_focus_tree/part_7_source_processing_report.md`
- `docs/plans/ireland_focus_tree/part_7_validation_report.md`

Current implementation surfaces inspected:

- `events/ireland_events.txt`
- `gfx/flags/IRE_ALL_ISLAND_communism.tga`
- `gfx/flags/IRE_ALL_ISLAND_democratic.tga`
- `gfx/flags/IRE_ALL_ISLAND_fascism.tga`
- `gfx/flags/IRE_ALL_ISLAND_neutrality.tga`
- corresponding medium and small All-Island flag files under `gfx/flags/medium/` and `gfx/flags/small/`
- empty runtime directories under `common/`, `history/`, `localisation/`, `interface/`, `music/`, and `sound/`

## Promotion note

This report should remain under `docs/plans/ireland_focus_tree/improvement_loop/`. It does not change the canonical feature design. If the parent later changes a route, fixed constant, count, H/P/A rule, Northern lifecycle, or conclusion family, that accepted change must be folded into the relevant canonical specification and reconciliation map before implementation continues.

This report is a gate artifact and planning handoff. It does not prove gameplay implementation, runtime loading, asset completion, AI completion, localisation completion, or final feature completion.
