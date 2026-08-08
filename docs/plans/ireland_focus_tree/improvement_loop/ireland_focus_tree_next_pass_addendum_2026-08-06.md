# Ireland focus tree — improvement-loop next-pass addendum

Date: 2026-08-06  
Workspace: Ireland Total Overhaul only  
Feature: ireland_focus_tree  
Pass type: implementation/integration plan for the current 211-focus worktree

This is the single next-pass addendum for the current improvement loop. It is an executable handoff to the gameplay/interface owner. It does not authorize or perform gameplay edits. The authoritative gameplay source remains common/national_focus/ireland_focus_tree.txt; this addendum only records the route reduction, contract, validation, and blocker work required before that source is rewritten.

## 1. Current evidence and hard invariants

The current source and local related sources were read together with the repository instructions, local HOI4 skills, offline wiki pages, and vanilla documentation. The current static inventory is:

- 211 focus blocks, one prerequisite-graph root, 210 prerequisite-bearing nodes, and 38 static graph leaves.
- 14 decision categories, 144 primary actions, 4 Marine Service actions, and 54 missions.
- 40 AI strategy blocks: 30 durable route/profile strategies and 10 overlays.
- 31 AI strategy plans: one historical plan, one reactive plan, and 30 route plans.
- 211 focus IDs have an id and id_desc localization pair in the current English file. The local icon-token scan found one icon assignment per focus and no unresolved icon token in the scanned interface/source files. These are static checks, not proof of in-engine rendering.
- The current scripted-effects/rewards file defines ten shared reward helpers. The focus tree currently calls economic 5 times, technical 2, diplomatic 1, military 1, radical 2, recovery 5, and capstone 24 times. Maritime, air, and cultural helpers are defined but unused.

The fresh HOI4 MCP evidence is the baseline for the next pass:

- workspace id: mod_ireland_total_overhaul_aaca88216c92
- source: common/national_focus/ireland_focus_tree.txt
- tree: ireland_focus_tree
- inspect revision: 457141a831476dfa66ac9622344761cb768ad0cc03329a7a5c55b8119c82c5fa
- focus inspect: 211 nodes, one root, 234 connectors, zero crossings, zero node intersections, zero long connectors, zero same-row overlaps, and 14 blocking focus diagnostics.
- layout bounds: x -24 through 24 and y 0 through 49. The authored graph is structurally connected but visually wide and tall.
- render: FOCUS_RENDERED with HTML, SVG, JSON, source-map, and plan artifacts; rendered dimensions are 8752 × 5920.
- raster at reviewScale 0.5: FOCUS_RASTERIZED and artifact produced, but validation still reports the same 14 blocking diagnostics.
- raster at reviewScale 1: RENDER_PIXELS_BLOCKED because 8752 × 5920 = 51,811,840 pixels, above the 50,331,648 pixel ceiling.

The next pass must preserve these design invariants:

1. One visible shared opening, progressive disclosure, and a clear route commitment. No second root and no branch that appears before its evidence or institutional gate.
2. Historical, plausible constitutional, and concealed absurd routes remain distinct and meaningful. No new route family is added in this pass.
3. No focus grants Northern territory, cores, annexation, administration, alignment, recognition, or free armies. Northern and Treaty Port work remain project/action surfaces.
4. Route capstones require the existing material, readiness, foreign, Northern, identity, objective, and postwar proof contract. Failed or partial routes must have a lawful recovery/review handoff.
5. Do not use a generic PP/stability/XP/equipment bundle as the only reason to take a focus. Preserve at most three durable route-profile spirit families; named failure forms remain ordered lifecycle outcomes, not additional reward piles.
6. Every surviving focus has a visible role, a complete effect description, a localization pair, an icon, an actionable unlock or durable state change, and an owner in the AI/decision/mission matrix.
7. Use HOI4 prerequisite semantics deliberately: entries inside one prerequisite block are OR; multiple prerequisite blocks are AND. Recheck every rewrite against that rule so compacting the graph does not accidentally bypass route gates.

## 2. Disposition of previous improvement-loop records

The previous records are not silently closed. Broad design expansion is closed; the remaining work is bounded implementation integration and evidence.

| Previous record | Disposition carried into this pass |
| --- | --- |
| finding disposition for IL-001 through IL-012 | The broad findings were accepted as implemented or superseded by the current source. IL-010 remains partial only where runtime/parser/scenario evidence was not run. No new design family is authorized. |
| worker findings ILR-01 through ILR-07 | Structurally present in the current source and related systems, but still partial until parser, engine, fresh-save, failure, and AI scenarios pass. The next pass owns those checks. |
| ILR-08 / source clearance | Still blocked. The current source-of-truth map is authoritative: exact-person portrait blockers remain P-26 Patrick Cogan, P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh. No substitute likeness or invented consumer is allowed. |
| ILR-09 / GUI and static focus audit | Structurally present and superseded by the fresh 211-node MCP snapshot. Live GUI interaction, stale-state checks, and save/reload behavior remain unrun. |
| ILR-10 / alias and report hygiene | Resolved. The execution report remains the historical worker report; this file is the only new addendum. |
| accepted IL-A01 through IL-A06 in the execution report | All six are partial-to-queued integration work: runtime contract, shared opening, route/lifecycle/conclusion, Northern/neutrality separation, AI/assets/text parity, and completion evidence. None is marked complete until its acceptance evidence below exists. |
| 2026-08-05 parliament improvement addendum | Its current-source correction is accepted: the worktree is 211 focuses, 14 categories, 144 primary actions plus 4 Marine Service actions, and 54 missions. Its older 13/140/54 registry and 226-focus MCP snapshot are historical. The exact roster reduction, native-decision versus GUI ownership, Seanad presentation, non-Dáil modes, and live validation remain unresolved. |
| parent review and execution recommendation | Broad design expansion is closed. This pass is the closure handoff only after the route map, reward contracts, action phases, validation artifacts, and blockers are dispositioned. |

## 3. Route roster and merge map

The following is the current roster read from the source comments and focus IDs. It is a reconciliation manifest, not permission to delete a route. Every current ID must end as a surviving focus, a named merged survivor, or a named decision/mission handoff in the implementation ledger.

### Current roster by source section

- Shared H/P opening and gateway: ireland_state_still_defined, ireland_national_settlement, ireland_republican_veterans, ireland_public_order_review, ireland_economic_war_review, ireland_rural_price_board, ireland_domestic_industry_review, ireland_defence_estimates, ireland_command_audit, ireland_port_and_coast_audit, ireland_church_labour_consultation, ireland_minority_guarantees, ireland_language_service, ireland_northern_contacts, ireland_election_timetable, ireland_constitutional_draft, ireland_plebiscite_campaign, ireland_general_election_campaign, ireland_plebiscite_mandate, ireland_election_mandate, ireland_government_formation, ireland_replacement_charter, ireland_1938_trade_settlement, ireland_treaty_port_transfer, ireland_sovereignty_mandate, ireland_emergency_opening, ireland_active_neutrality.
- de Valera stewardship, reconciliation, and Emergency: ireland_republican_government, ireland_party_of_government, ireland_republican_legitimacy, ireland_neutrality_by_irish_decision, ireland_de_valera_stewardship, ireland_govern_through_dail, ireland_constitutional_stewardship, ireland_de_valera_reconciliation, ireland_amnesty_under_law, ireland_reconciliation_mandate, ireland_de_valera_reconciliation_capstone, ireland_emergency_direction, ireland_statutory_emergency, ireland_emergency_review, ireland_emergency_repeal, ireland_de_valera_emergency_capstone.
- Fine Gael, Cosgrave, Mulcahy, Costello, and Dillon: ireland_constitutional_opposition, ireland_close_oduffy_chapter, ireland_government_from_opposition, ireland_state_we_built, ireland_cosgrave_institutional, ireland_restore_parliamentary_confidence, ireland_civil_service_and_courts, ireland_security_under_law, ireland_cosgrave_capstone, ireland_mulcahy_succession, ireland_army_serves_dail, ireland_mulcahy_capstone, ireland_costello_coalition, ireland_written_coalition_charter, ireland_unwind_exceptional_state, ireland_costello_capstone, ireland_dillon_public_dissent, ireland_dillon_intervention_caucus, ireland_dillon_war_assent.
- Norton: ireland_norton_parliamentary, ireland_labour_as_conscience, ireland_support_without_surrender, ireland_labour_social_law, ireland_norton_parliamentary_capstone.
- Clann and constitutional vocational: ireland_clann_founding, ireland_agrarian_support_bloc, ireland_clann_by_election, ireland_rural_producer_compact, ireland_vocational_constitution, ireland_council_government_rejected, ireland_vocational_constitution_capstone.
- Serious culture and evidence: ireland_cultural_survey, ireland_language_institutions, ireland_archival_record, ireland_regional_participation, ireland_site_stewardship, ireland_diaspora_exchange, ireland_serious_cultural_stewardship, ireland_cultural_service, ireland_cultural_evidence_ledger, ireland_culture_completion.
- National Provision: ireland_provision_baseline, ireland_food_ledger, ireland_energy_board, ireland_transport_priority, ireland_maritime_reserve, ireland_domestic_manufacturing, ireland_rural_credit, ireland_emergency_stockpiles, ireland_development_authority, ireland_social_cooperatives, ireland_producer_accounting, ireland_provision_conclusion.
- National Readiness and defence: ireland_readiness_baseline, ireland_readiness_command, ireland_territorial_reserve, ireland_coastwatch, ireland_air_warning, ireland_port_defence_project, ireland_maritime_protection, ireland_professional_army, ireland_civilian_oversight, ireland_interoperability, ireland_emergency_mobilisation, ireland_readiness_conclusion.
- Marine Service: ireland_rebuild_marine_service, ireland_requisition_trawler_hulls, ireland_coastal_patrol_flotilla, ireland_marine_service_reserve, ireland_establish_naval_staff, ireland_harbour_defence_board, ireland_cobh_dockyard_programme, ireland_lough_swilly_watch, ireland_atlantic_convoy_office, ireland_regional_maritime_defence_pact.
- Neutrality and foreign safeguards: ireland_strict_neutrality, ireland_armed_neutrality, ireland_treaty_port_diplomacy, ireland_british_leverage_management, ireland_american_diaspora_mission, ireland_vatican_small_state_mediation, ireland_foreign_safeguards, ireland_neutrality_posture.
- Northern Ireland: ireland_northern_settlement_ledger, ireland_northern_local_authorities, ireland_northern_trade_corridor, ireland_northern_labour_social_bridge, ireland_northern_federal_preparation, ireland_northern_unitary_preparation, ireland_northern_wartime_bargain, ireland_northern_recovery_bridge, ireland_northern_regional_review, ireland_northern_policy_proof.
- Recovery and postwar proof: ireland_recovery_bridge, ireland_restore_constitutional_calendar, ireland_emergency_accounting, ireland_demobilisation_charter, ireland_reconstruction_mandate, ireland_foreign_postwar_review, ireland_material_conclusion_proof.
- IRA civil-republican and Army Council: ireland_ira_republican_bridge, ireland_reassemble_ghq, ireland_convention_of_commands, ireland_republic_in_districts, ireland_arms_before_authority, ireland_authority_before_arms, ireland_german_channel, ireland_northern_question_in_arms, ireland_ira_civil_authority, ireland_ira_army_council, ireland_ira_route_capstone.
- Republican Congress: ireland_congress_reform_bridge, ireland_organise_congress, ireland_congress_plural_republic, ireland_congress_vanguard_cell, ireland_extra_parliamentary_transition, ireland_congress_plural_capstone, ireland_congress_vanguard_capstone.
- O'Duffy personal and corporate: ireland_oduffy_network_revival, ireland_oduffy_personal_command, ireland_veteran_employer_league, ireland_corporate_estates, ireland_army_acceptance, ireland_corporate_order, ireland_oduffy_personal_capstone, ireland_oduffy_corporate_capstone.
- Clerical and producer-council: ireland_clerical_failure_bridge, ireland_service_state, ireland_producer_councils, ireland_clerical_guardianship, ireland_producer_constitution, ireland_clerical_route_capstone.
- Ailtirí: ireland_ailtiri_cell_network, ireland_june_1942_public_launch, ireland_ceannaire_state, ireland_corporate_gaelic_nation, ireland_ailtiri_total_state_capstone.
- High Kingship: ireland_high_king_evidence_gate, ireland_high_king_convention, ireland_elective_crown, ireland_crown_powers_charter, ireland_high_king_capstone.
- Five Provinces: ireland_five_province_mandates, ireland_federal_convention, ireland_federal_republic, ireland_ulster_rule, ireland_pentarchy_guardians, ireland_five_provinces_capstone.
- Otherworld: ireland_otherworld_investigation, ireland_otherworld_witnesses, ireland_otherworld_evidence_ledger, ireland_compact_with_otherworld, ireland_containment_protocol, ireland_dominion_claim, ireland_otherworld_guardians, ireland_regional_thresholds, ireland_otherworld_statecraft, ireland_otherworld_capstone.
- Final convergence: ireland_crown_province_convergence, ireland_fivefold_obligation, ireland_otherworld_convergence, ireland_convergence_order_capstone.

### Working survivor envelope

Use the previous compact budget as the accounting envelope. Count a focus once only; a focus cannot be counted in both its source section and a support lane. Target 144 surviving focus blocks. Hard ceiling 156, and anything above the ceiling requires a new explicit planning decision rather than silent carry-forward.

| Envelope | Working budget | Required compact shape |
| --- | ---: | --- |
| Shared opening | 10 | State still defined → National Settlement → a small set of institutional, social, material, and readiness reveals. |
| Constitution, election, and parliament | 16 | Election/plebiscite alternatives converge into one government-formation gate; replacement charter remains a visible recovery choice. |
| Government and coalition routes | 28 | de Valera, Lemass, Cosgrave, Mulcahy, Costello, Dillon, Norton, and Clann remain recognizable through one anchor, one interaction/proof lane, and one capstone or recovery handoff. |
| Society, Church, culture, and vocational | 12 | Preserve minority/service obligations and serious-culture evidence; move repeated audits into actions or missions. |
| Provision and economy | 10 | Keep food, energy, transport, maritime, industry, and rural credit as distinct ledgers, but expose repeated work through the existing decision/mission surface. |
| Readiness, defence, and maritime | 12 | Keep command, reserve, warning, port, professional army, and Marine Service identity; collapse repeated dockyard/procurement review steps into named actions. |
| Neutrality and foreign | 10 | Keep strict/armed neutrality, Treaty Port diplomacy, British/American/Vatican channels, safeguards, and neutrality posture as distinct choices with material exposure. |
| Northern | 12 | Keep settlement, local authority, labour, federal, unitary, wartime, recovery, and policy-proof outcomes; never turn a focus into an automatic territorial reward. |
| Republican, IRA, and Congress | 12 | Preserve civil-authority versus Army Council and plural versus vanguard choices; use action/mission stages for command reassembly and constituent authority. |
| O'Duffy, corporate, and Ailtirí | 8 | Keep personal/corporate and dated Ailtirí identities; route evidence and state-interface failure must remain visible. |
| Hidden, royal, Five Provinces, and Otherworld | 8 | Keep evidence gate, negotiated versus coercive outcomes, containment versus dominion, and obligation accounting. These are compact branches, not extra roots. |
| Recovery and conclusions | 6 | One shared recovery/review spine with route-specific conclusion results and explicit cleanup. |
| Total | 144 | Any survivor outside this envelope must replace another survivor and explain the trade in the ledger. |

### Merge and convergence instructions

The implementation owner must maintain a before/after table with focus_id, source section, survivor or merge target, route role, retained flag/ledger, new decision or mission, lifecycle cleanup, localization/icon disposition, and validation scenario. The following are the first-pass map decisions:

1. Keep ireland_state_still_defined as the only root and ireland_national_settlement as the shared initialization gate.
2. Retain the institutional meaning of ireland_republican_veterans and ireland_public_order_review, but remove review-only spacing and duplicate reward work. If one is merged, move both the veterans ledger opening and security baseline to the named survivor and update every focus, trigger, AI plan, and localization reference.
3. Retain one visible early provision anchor and one readiness anchor. Recast ireland_domestic_industry_review into the later domestic-manufacturing/development-authority output if it has no independent action; recast ireland_command_audit into the readiness-command contract if its audit has no independent decision; retain port/coast evidence through the Coastwatch or Marine Service action surface.
4. Keep church/labour consultation and minority guarantees only as a two-step social obligation if both unlock different stakeholder actions. The old layout intent remains: church/labour consultation should converge into minority guarantees; public-order proof should feed the language-service gate without a long visual detour.
5. Keep election timetable, constitutional draft, plebiscite campaign, general-election campaign, the two mandate outcomes, and government formation only while each produces a distinct ledger or action. Election and plebiscite branches may be parallel choices, but government formation must require the correct mandate arithmetic and must not be an OR bypass accidentally created by multiple prerequisite blocks.
6. Straighten the MCP-identified visual detours: ireland_1938_trade_settlement → ireland_treaty_port_transfer, ireland_close_oduffy_chapter → ireland_government_from_opposition, and ireland_northern_settlement_ledger → ireland_northern_local_authorities. A detour may be kept only when it represents a real cross-branch dependency and the source-map records why.
7. Preserve the de Valera reconciliation and Emergency alternatives, but move repeated stewardship/audit effects into named actions. Reconciliation and emergency capstones must open the conclusion-review/recovery lifecycle rather than terminate as reward-only leaves.
8. Preserve Lemass developmental, Cosgrave institutional, Mulcahy civil-defence, Costello coalition, Dillon intervention, Norton parliamentary, and Clann agrarian identity. Merge only repeated consultation, review, or generic institution focuses; retain each route's leader/office or authority change, stakeholder tradeoff, and actionable support lane.
9. Keep the serious-culture evidence chain only to the point where it opens a real cultural/archive/evidence action or mission. Merge language-institution and repeated archive review where the action surface already represents the work; do not merge away the independent-evidence gate used by hidden routes.
10. Keep the three provision component choices as ledger inputs, but remove standalone tiny rewards and expose their consequences through the existing component decisions/missions. Merge maritime reserve into the transport/maritime contract only if the Marine Service and convoy consequences remain visible.
11. Compact the Marine Service chain around one commissioning/authority focus, one dockyard/patrol proof focus, and one reserve/convoy conclusion. The four Marine Service actions remain owned by the Marine Service category; a focus must not duplicate all four action rewards.
12. Keep neutrality, foreign, and Northern as separate support lanes. A foreign focus opens a named channel or safeguard; a Northern focus opens a representative, federal, unitary, labour, wartime, recovery, or proof action. No foreign or Northern focus may directly grant control, cores, annexation, alignment, or recognition.
13. Compact hidden routes through evidence and obligations: IRA bridge → civil/Army Council choice → Northern question and conclusion; Congress bridge → plural/vanguard choice → constituent authority and conclusion; O'Duffy bridge → personal/corporate choice → Army acceptance/order and conclusion; clerical bridge → service/producer choice → conclusion; Ailtirí keeps the dated 1942 launch; High King keeps evidence/convention/elective or sacral charter; Five Provinces keeps federal or pentarchic choice; Otherworld keeps witnesses/evidence, compact/containment/dominion, and obligation review.
14. All hidden/royal/Otherworld capstones converge only through ireland_crown_province_convergence → ireland_fivefold_obligation → ireland_otherworld_convergence → ireland_convergence_order_capstone, with the existing independent-proof checks. If a hidden route fails, its cleanup and recovery bridge remain available; it must not become a soft-lock.
15. Route capstones that are currently static leaves must hand off to the shared conclusion-review action/mission or a named recovery bridge. A capstone may remain a visual leaf only when the tooltip states the active review/conclusion handoff and the scripted state proves that handoff.

### Static leaf audit to execute

The current prerequisite graph has 38 leaves. Before accepting a rewrite, classify every one in the implementation ledger as a support handoff, route conclusion, recovery bridge, or merged focus. The current list is:

ireland_domestic_industry_review; ireland_port_and_coast_audit; ireland_minority_guarantees; ireland_language_service; ireland_northern_contacts; ireland_neutrality_by_irish_decision; ireland_constitutional_stewardship; ireland_de_valera_reconciliation_capstone; ireland_de_valera_emergency_capstone; ireland_dail_nomination; ireland_cosgrave_capstone; ireland_mulcahy_capstone; ireland_costello_capstone; ireland_dillon_war_assent; ireland_norton_parliamentary_capstone; ireland_rural_producer_compact; ireland_vocational_constitution_capstone; ireland_language_institutions; ireland_culture_completion; ireland_maritime_reserve; ireland_emergency_stockpiles; ireland_territorial_reserve; ireland_marine_service_reserve; ireland_civilian_oversight; ireland_emergency_mobilisation; ireland_armed_neutrality; ireland_northern_policy_proof; ireland_congress_plural_capstone; ireland_congress_vanguard_capstone; ireland_oduffy_personal_command; ireland_oduffy_personal_capstone; ireland_clerical_route_capstone; ireland_ailtiri_total_state_capstone; ireland_elective_crown; ireland_federal_republic; ireland_dominion_claim; ireland_regional_thresholds; ireland_convergence_order_capstone.

Acceptance rule: no unowned leaf, no leaf whose only output is the shared capstone reward helper, and no leaf that leaves an active mission/category/action slot without a success, partial, failure, cancellation, or recovery path.

## 4. Reward contracts and effect descriptions

Create a reward contract ledger before changing any completion_reward. Use these columns:

focus_id; route family; focus role; prerequisite/proof; authoritative flags/variables; exact player-visible output; action or mission unlocked; AI plan/profile; cleanup or reversal; localization keys; icon key; validation scenario.

Apply these role contracts:

- Shared opener: initialize or reveal a ledger/category and state the next real choice. Do not front-load PP, stability, XP, equipment, a spirit, and an institution together.
- Constitutional anchor: set one route/office/law/mandate state and open a named stakeholder action with a real tradeoff.
- Leader/authority anchor: change the leader, office, government, law, cabinet, or accountable authority. The output must be visible in the route/office state and must have vacancy/reversal handling.
- Economic/provision anchor: add or modify a named project, production/trade/provision input, or component mission with material requirements and shortage/failure outcomes.
- Defence/readiness anchor: open a command, template, warning, maritime, lawful military authority, or reserve action. Do not grant free armies or duplicate the readiness ledger.
- Diplomacy/neutrality anchor: open a named sponsor/channel/agreement/access project and record leverage/exposure. Keep neutral posture and foreign burden separate.
- Northern anchor: open a representative, settlement, federal/unitary, labour, wartime, recovery, or integration action. The focus must not directly annex or core territory.
- Society/culture anchor: open a service, archive, language, labour, minority, vocational, or cultural-evidence action/mission with a measurable obligation.
- Hidden evidence anchor: require independent evidence, state-interface failure, and route proof; expose containment/reversal risk and never use hidden status as a substitute for gameplay.
- Capstone/recovery: start or complete the existing conclusion-review/cleanup contract, set a route-specific conclusion result, or open a recovery path. It is not a generic reward bundle.

Specific current reward cleanup:

1. Remove the 24 calls to ireland_grant_capstone_focus_reward from capstones that do not add a unique route result. Replace them with route conclusion/review state, a named action or mission, and cleanup/recovery.
2. Retain a shared reward helper only when the focus also has a unique route-bearing effect and the contract ledger identifies why the helper is not duplicate. No surviving focus may be justified only by PP, stability, war support, XP, or stockpile material.
3. Keep the old shared-profile ceiling of 24 final focus blocks only as an upper audit limit; the target should be lower after merge. Keep institutional reward use at or below 8 unless a new design decision records the replacement.
4. Keep values in the existing constants/helpers. Do not introduce isolated numeric rewards in the focus tree. Every effect must have an accurate player-facing description, including dynamic variables, action costs, mission outcomes, flags, ideas, leader/office changes, and cleanup.
5. Every surviving focus must have a complete id_desc that explains its real completion effect. Every newly exposed action/mission/decision state must have its blocked, cost, active, success, partial, failure, cancellation, and cleanup tooltip coverage. No placeholder, generic “review” text, or hidden-only effect description is accepted.

## 5. Progressive unlock and lifecycle policy

Use the existing ledgers and helpers as the single state machine. The focus tree reveals and routes the state; it must not create a parallel arithmetic system.

| Phase | Entry contract | What may unlock | Exit/cleanup |
| --- | --- | --- | --- |
| 0 — shared opening | ireland_initialize_campaign and ireland_settlement_open complete | One Dáil opening action, constitutional opening, at most two support-lane actions; hidden and leader routes remain closed | obsolete opening prompts close; GUI dirty and derived ledgers update |
| 1 — parliamentary foundation | Dáil session complete and parliament stage advanced | Seanad support, confidence compact, vote-count/election preparation, valid constitutional alternatives | failed vote opens confidence/dissolution/recovery path; no stale action remains active |
| 2 — government formation | valid election or plebiscite mandate, formal/routine vote arithmetic, and government-formation gate | coalition, alternative Taoiseach, cabinet portfolios, programme, charter, minority/caretaker paths | formed/minority/caretaker/dissolution state is exclusive and cleans incompatible options |
| 3 — active government | lawful government and route commitment | route-specific government, society, provision, readiness, neutrality, Northern, and diplomatic actions | collapse, review, emergency, or transformation must set a named result and close obsolete actions |
| 4 — crisis/emergency | emergency, lost vote, invasion danger, shortage, sponsor failure, or route proof failure | only critical crisis/recovery missions and actions; do not reveal every category at once | full/partial/failure/restore outcomes return to lawful review or recovery |
| 5 — review/conclusion | route proof and postwar/review timing | conclusion review, demobilisation, reconstruction, postwar, integration, or hidden obligation actions | conclusion result is archived, transient state is cleaned, and route reopening requires an explicit flag |

Preserve and test the existing staged actions ireland_action_convene_the_dail, ireland_action_negotiate_seanad_support, ireland_action_secure_a_confidence_compact, and ireland_action_pass_a_joint_budget. Preserve ireland_parliament_stage, ireland_update_parliament, the formal/routine seat ledgers, Seanad ledgers, and GUI dirty variables. Any new focus gate must name its phase and the authoritative variable/flag it reads.

Resolve the parliament ownership blocker before implementation:

- Recommended default: native decisions own affordability, effects, completion, failure, and refunds; the scripted GUI displays the same variables, dispatches the same native action/effect, and sets dirty state only.
- If the existing GUI-direct effect path is retained, prove that the GUI and decision path call the same cost, ledger, and cleanup helpers. No duplicate seat count, stage, or action outcome may exist in the GUI.
- Choose and document the non-Dáil roster: ordinary Dáil, minority/confidence, caretaker/crisis, Dáil-sovereign vocational, extra-parliamentary/captured, and archived/replaced. Every mode needs visible status and a legal action path.
- The Seanad must be a real support gate with its own seats, threshold, action, tooltip, failure, and GUI status; it cannot be a decorative second majority.

## 6. AI parity

The current AI package is substantial but static-only. Preserve the 30 durable route/profile strategies, 10 overlays, and 31 plans while reducing focus IDs. Every surviving focus and every newly named action/mission must have one of:

1. a historical or reactive plan entry;
2. a route plan entry with the same prerequisite/proof and cost floors as the player;
3. a documented human-only/hidden disposition with an explicit AI exclusion.

Required parity matrix:

- Historical: IRE_ireland_historical and ireland_historical_de_valera must take the shared opening, constitutional gateway, material/readiness baseline, and de Valera handoff without selecting hidden content.
- Historical alternatives: Lemass, Cosgrave, Mulcahy, Costello, Dillon, Norton, Clann, and vocational routes each need a focus factor, support-lane priority, and conclusion/recovery priority.
- Reactive: election/government formation, constitutional crisis, provision breakdown, invasion/home defence, Northern occupation/integration, foreign sponsor collapse, leadership vacancy, and postwar/review overlays must pre-empt route selection only when their trigger is true.
- Concealed routes: default human-only. Any existing rare non-historical Ailtirí/Otherworld permission must remain explicitly gated by the hidden-content rule or rare permission flag and must be tested as a deliberate exception, never as accidental AI drift.
- AI actions/missions: the AI must be able to pay the same PP/CP/material costs, observe the same National Settlement/Social Consent/Provision/Readiness/Neutrality Integrity floors, complete partial/failure branches, and reach recovery or conclusion. AI must not skip a focus gate because a plan still names an absorbed ID.

Acceptance requires a crosswalk from every surviving focus ID to plan/factor/profile, plus static checks for orphaned plan IDs and runtime scenarios for historical, alternate constitutional, emergency, Northern, and one permitted hidden route.

## 7. Localization and icon acceptance

The current static baseline has 211 focus title/description pairs and no missing focus localization keys. The next pass must regenerate a survivor crosswalk and then verify:

- every surviving focus has exactly one title key, one desc key, and effect text that matches the actual completion_reward;
- merged focus keys are either intentionally retained as compatibility aliases or removed with all references updated; no orphaned name/description keys remain;
- action, mission, category, route-profile, office, leader, idea, conclusion, recovery, blocked, partial, failure, cancellation, and cleanup tooltips have complete English coverage;
- dynamic variable formatting is valid and has a readable fallback; no unresolved variable, missing scripted localization object, or stale stage label remains;
- every surviving focus has a distinct registered icon or a deliberate approved reuse documented in the asset crosswalk; merge operations do not strand icon registrations or point to the three blocked exact-person portraits;
- MCP title resolution equals the post-rewrite focus count and decoded raster output shows the intended icon for every focus. Static token resolution is not enough; the icon/render pass must be recorded.

The three blocked exact-person portraits remain an asset blocker, not a reason to invent replacements. If a gameplay owner removes a blocked consumer during the route merge, record the removal; do not silently substitute a likeness.

## 8. MCP inspect/rewrite/render/raster acceptance

No rewrite was called in this planning pass because gameplay files are read-only. The implementation owner may use the following bounded sequence only after the route/reward/action ledger is approved:

1. Preflight with hoi4_focus_inspect on workspace mod_ireland_total_overhaul_aaca88216c92, relative path common/national_focus/ireland_focus_tree.txt, tree ireland_focus_tree, mode national. Save the revision, layout hash, diagnostics, node IDs, and source-map artifact.
2. Apply the approved plan with hoi4_focus_rewrite, layoutMode compact, and the same workspace/path/tree. The plan must name the survivor IDs, merge targets, route lanes, and convergence rules. No createIfMissing and no unrelated file changes.
3. Re-run hoi4_focus_inspect. Acceptance requires:
   - focus count in the 144–156 envelope and the approved registry count recorded;
   - exactly one root and no orphaned or unknown prerequisite/mutual-exclusion IDs;
   - all route families and shared support lanes have a visible path to a decision/mission or review/conclusion/recovery handoff;
   - zero blocking diagnostics, zero crossings, zero node intersections, zero long connectors, zero same-row overlaps, no unnecessary linear detours, and no sibling-anchor warnings that obscure route meaning;
   - the source-map covers every surviving focus and every merge is traceable to the implementation ledger.
4. Run hoi4_focus_render and save HTML, SVG, JSON, source-map, plan, revision, layout hash, dimensions, and artifact hashes. Acceptance requires FOCUS_RENDERED, resolvedTitleCount equal to focus count, and no missing effect/localization references in the render-side inventory.
5. Run hoi4_focus_raster at reviewScale 1.0. Acceptance requires FOCUS_RASTERIZED, decoded icons, a PNG within 50,331,648 pixels, and validation passed. A lower reviewScale may be an additional inspection artifact, but it cannot be reported as the full raster acceptance. The current 0.5 raster is evidence that the tool can produce an artifact; it is not a clean pass because the 14 diagnostics remain.
6. Review the raster and SVG visually for legible branch labels, route convergence, no apparent dead ends, no detached support lanes, no icon substitution, and no accidental crossing. Record the artifact URI and hash in the follow-up execution report.
7. Run local static validation after the MCP rewrite: focus ID/prerequisite graph, reward-helper crosswalk, localization pairs, icon registrations, decision/mission references, AI plan references, scripted effect/trigger definitions, and changed-file boundary. Then run the engine/scenario suite below.

The MCP baseline warnings must be treated as layout work, not hidden by deleting meaningful nodes. The named warning cohorts include the church/economic/Northern opening trio; defence/rural review; election/veteran review; plebiscite/replacement charter; Costello/Dillon/Mulcahy; energy/food/transport; Coastwatch/readiness/reserve; harbour/rebuild Marine Service; American/Vatican channels; armed neutrality/Northern settlement/Treaty Port diplomacy; Northern labour/trade; Congress/IRA bridge; Army acceptance/clerical bridge; and Dominion/Otherworld statecraft.

## 9. Scenario and runtime evidence required

The current source-of-truth map still records live engine, fresh-save, GUI interaction, and AI simulation evidence as not-run. The next execution report must include pass/fail evidence for:

- fresh 1936 opening: state still defined, National Settlement, exactly the intended early actions, hidden content closed;
- Dáil/Seanad staging: Dáil session, minority 76 versus 77 support, Seanad support, confidence failure, confidence-and-supply, cabinet formation, and joint budget;
- election and plebiscite: both mandate branches, rejected plebiscite/replacement charter, government formation, dissolution/caretaker cleanup;
- support lanes: provision bottleneck and recovery, readiness warning/invasion, Marine Service actions, neutrality incident and foreign sponsor collapse, Northern representative/federal/unitary/recovery paths;
- route lifecycle: one historical route, one plausible constitutional route, IRA civil versus Army Council, Congress plural versus vanguard, O'Duffy personal versus corporate, clerical/producer, dated Ailtirí, High King, Five Provinces, and Otherworld compact/containment;
- conclusion/recovery: full, partial, blocked, failed, cancellation, cleanup, and lawful re-entry after a route review;
- AI: historical route, non-historical constitutional route, crisis overlay, and permitted hidden-content exception. Verify that AI reaches action/mission completion rather than merely selecting focus IDs.

## 10. Remaining blockers and stop condition

These blockers remain open and must be named in the implementation report:

1. Exact survivor/merge roster and the current 14-category / 144+4-action / 54-mission registry versus the older 13/140/54 canonical registry. Resolve the registry decision before changing counts.
2. Native decision versus scripted-GUI ownership for parliament actions, including Seanad presentation and non-Dáil authority modes.
3. The 38-leaf disposition and the 14 MCP blocking layout diagnostics.
4. Full-scale raster pixel ceiling; the current authored layout exceeds it.
5. Runtime parser, engine, fresh-save, GUI, failure/recovery, and AI scenario evidence.
6. Three exact-person portrait source blockers: P-26 Patrick Cogan, P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh. No substitute asset is allowed.
7. Post-merge localization/effect/icon crosswalk and any stale AI, decision, mission, trigger, scripted-effect, or achievement references.

Stop this improvement loop when the route ledger answers every survivor/merge, convergence, reward, action phase, authoritative variable, player/AI owner, cleanup, localization, icon, and validation field; MCP inspect/render/raster pass; static and runtime scenario evidence is recorded; and the only remaining asset disposition is the explicitly blocked portrait set. If any blocker above remains, keep the feature open with its exact disposition rather than adding more route concepts.
