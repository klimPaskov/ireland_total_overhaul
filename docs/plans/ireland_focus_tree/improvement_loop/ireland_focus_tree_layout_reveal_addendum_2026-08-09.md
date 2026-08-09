# Ireland focus tree semantic layout and reveal addendum

Date: 2026-08-09  
Feature slug: `ireland_focus_tree`  
Pass type: implementation-ready layout and progressive-reveal correction  
Status: implemented; accepted coordinate and reveal contract reconciled to the final source revision

This began as a plan-only handoff. The gameplay owner implemented it, reviewed the connector routing, and accepted the narrow prerequisite corrections recorded in section 6.5 where the original graph itself made the subject families read incorrectly.

## 1. Why another improvement pass is valid

The 2026-08-05 Parliament/focus-tree addendum is explicitly marked superseded and implemented. The 2026-08-06 reduction plan was fulfilled by the authoritative 2026-08-09 completion report, which records the consolidated 150-focus tree. Neither is an unresolved competing addendum.

The new defect is narrower and was only visible after that implementation: the tree was structurally connected, but its authored coordinates did not communicate its subject families. The player could not identify politics, industry, army/air, navy, diplomacy, Northern policy, and culture at first glance, and the naval family read as an interior lane instead of a maritime edge. The implementation changes layout and reveal presentation, plus narrow prerequisite geometry where an unrelated family was acting as a visual parent. It does not add focuses, routes, or generic rewards.

## 2. Evidence and engine constraints

The baseline read used `common/national_focus/ireland_focus_tree.txt`, the current source-of-truth map, the 2026-08-09 completion report, the earlier layout/MCP reports, the offline National Focus, Data Structures, Triggers, Effects, Localisation, Scopes, and AI wiki pages, the official game documentation, and vanilla focus-tree precedents.

The latest complete read-only MCP snapshot taken for this addendum reported 150 focuses, one root, 158 connectors, bounds x -23 through 13 and y 0 through 25, 26 connector crossings, 20 connector-through-node intersections, four long connectors, and an `initial_show_position` expressed as coordinates rather than a focus. That snapshot is evidence for the defect, not an immutable source hash: the gameplay owner was already editing the focus file in parallel.

The engine rules that govern implementation are:

- `initial_show_position = { focus = <id> }` should identify the camera anchor by focus ID.
- Every prerequisite parent must be above its child. Downward or same-row parent-child relationships risk broken connector turns.
- `allow_branch` is evaluated when the focus layout is loaded and is refreshed by `mark_focus_tree_layout_dirty = yes`.
- When a hidden root's `allow_branch` is false, its descendants inherit that hidden state unless they override it.
- Multiple `prerequisite` blocks are AND groups; multiple focus IDs inside one block are OR alternatives. Coordinate work must not change that structure.
- The table below uses absolute `x` and `y` values. Do not introduce a long `relative_position_id` chain merely to encode these coordinates; a missing or cyclic relative anchor is a crash and maintenance risk.

The current source already refreshes the layout after `ireland_cultural_evidence_ledger` and during the country-scoped `on_daily_IRE` synchronization pass. Therefore the current answer to “is visibility progressive?” is **yes, but only for the eight authored hidden families**: they become visible after their gates are true and the layout refreshes, normally no later than the next daily Ireland synchronization. All ordinary branches are visible from the opening screen and merely unavailable until prerequisites are met.

## 3. Player-facing spatial grammar

The tree should read from left to right as follows:

| Band | Primary x range | Player-visible meaning |
| --- | ---: | --- |
| radical and emergency politics | -24 to -18 | armed republican, emergency, O'Duffy, and recovery offshoots; conditionally hidden routes remain tucked against their political parent |
| constitutional politics | -16 to -8 | election, government, Fianna Fáil, Fine Gael, Labour-adjacent, and parliamentary succession routes |
| Northern policy | -6 to -2 | border institutions and federal/unitary/wartime settlement proof; adjacent to constitutional politics rather than treated as a naval reward |
| culture and society | 0 to 8 | cultural survey, archival stewardship, parliamentary social alternatives, and evidence-gated conclusions |
| industry and provision | 10 to 20 | food, energy, transport, domestic production, cooperatives, and the development authority |
| diplomacy and neutrality | 20 to 26 | armed/strict neutrality, British, American, Vatican, and interoperability safeguards |
| army and air readiness | 24 to 34 | command, professional army, air warning, mobilisation, coastwatch, and port defence |
| navy and Marine Service | 32 to 38 | naval staff, dockyard, patrol flotilla, reserve, and Atlantic office; this is the far-right terminal family |

The bands overlap only at authored handoffs. The overlap between diplomacy and readiness shows that neutrality must be defended; the overlap between port defence and the naval staff shows the institutional handoff from coastal protection to an actual Marine Service. It must not be used to scatter unrelated focuses into the same space.

The historical/regional logic follows the accepted source specification rather than inventing a new route history: the Economic War/1938 settlement feeds material provision; the Treaty Port settlement feeds constitutional, Northern, and later coastal questions; Northern Ireland remains a political and administrative society rather than a free territorial naval result; emergency neutrality, foreign safeguards, coastwatch, and the Marine Service remain connected but visually distinguishable; Ailtirí stays dated and concealed rather than appearing as a normal 1936 party choice.

## 4. Opening visibility and camera

Replace the coordinate camera declaration with:

```txt
initial_show_position = { focus = ireland_state_still_defined }
```

The opening camera must show the common root and the three immediately legible gateway directions:

- `ireland_national_settlement` leading to politics, Northern policy, and culture;
- `ireland_economic_war_review` leading to industry and provision;
- `ireland_defence_estimates` leading to diplomacy, army/air readiness, coast defence, and the far-right navy.

The following ordinary families remain visible at game start, including their grey/unavailable descendants:

- constitutional and emergency politics, including all ordinary Fianna Fáil, Fine Gael, Labour, Clann, vocational, and recovery branches;
- industry and National Provision;
- army and air readiness;
- diplomacy and neutrality;
- Northern policy;
- culture and evidence stewardship;
- the full Marine Service/naval family on the far-right edge.

Do not add `allow_branch` to an ordinary family in order to reduce visual width. Progressive disclosure must not erase the seven subject headings the player is trying to recognize.

## 5. Existing progressive hidden families

Preserve exactly these eight hidden roots and their inherited descendants. Do not make their descendants independently visible and do not invent replacement reveal flags.

| Hidden family root | Existing reveal condition | Why it remains hidden |
| --- | --- | --- |
| `ireland_ira_republican_bridge` | `ireland_ira_organization_ready` and `ireland_ira_transition_ready` | armed-republican state transition must arise from organisation plus constitutional/security breakdown, not look like an ordinary election choice |
| `ireland_congress_reform_bridge` | `ireland_congress_organization_ready` and `ireland_congress_transition_ready` | Congress transformation is a crisis/failure development rather than the ordinary Labour-parliamentary lane |
| `ireland_oduffy_network_revival` | `ireland_oduffy_network_ready` and `ireland_oduffy_crisis_ready` | a revived personal/corporate movement contradicts the ordinary closure of the O'Duffy chapter unless its network and crisis return |
| `ireland_clerical_failure_bridge` | `ireland_clerical_failure_ready` and `ireland_service_state_ready` | the guardianship/producer-state route is a failure conversion of ordinary vocational consultation |
| `ireland_ailtiri_cell_network` | date after 1940-09-01, `ireland_ailtiri_cells_ready`, and one of the hidden-content/game-rule/rare-AI permissions | the real movement is a dated wartime emergence and must not advertise itself in the 1936 opening |
| `ireland_high_king_evidence_gate` | `ireland_high_king_evidence_verified` and `ireland_high_king_convention_ready` | the crown conclusion requires earned evidence and a convention, not an unexplained visible monarchy branch |
| `ireland_five_province_mandates` | `ireland_five_provinces_mandates_ready` and `ireland_five_provinces_convention_ready` | the provincial/federal conclusion requires Northern policy proof and actual regional mandates |
| `ireland_otherworld_investigation` | hidden-content permission, hidden-content game rule, `ireland_otherworld_investigation_ready`, and `ireland_otherworld_evidence_verified` | explicitly impossible content should exist only after deliberate opt-in and an earned investigation |

Implementation must preserve the country-scoped refresh after the gate synchronizers. The acceptance scenario is not merely that the flags are set: each root must appear without closing/reopening the focus window once the next existing refresh occurs, and unrevealed roots must leave no orphan connector or empty connector stub.

## 6. Exact coordinate contract for all 150 existing focuses

These are absolute coordinates. The table is the implementation source for this pass. It contains every current focus ID exactly once.

### 6.1 Opening and ordinary political families

| Focus ID | x | y |
| --- | ---: | ---: |
| `ireland_state_still_defined` | 6 | 0 |
| `ireland_national_settlement` | -2 | 1 |
| `ireland_economic_war_review` | 12 | 1 |
| `ireland_defence_estimates` | 14 | 1 |
| `ireland_public_order_review` | -10 | 2 |
| `ireland_church_labour_consultation` | 2 | 2 |
| `ireland_election_timetable` | -4 | 2 |
| `ireland_rural_price_board` | 12 | 2 |
| `ireland_command_audit` | 14 | 2 |
| `ireland_constitutional_draft` | -4 | 3 |
| `ireland_election_mandate` | -12 | 4 |
| `ireland_government_formation` | -12 | 5 |
| `ireland_1938_trade_settlement` | -12 | 6 |
| `ireland_treaty_port_transfer` | -12 | 7 |
| `ireland_republican_government` | -8 | 4 |
| `ireland_de_valera_stewardship` | -8 | 5 |
| `ireland_constitutional_stewardship` | -8 | 6 |
| `ireland_de_valera_reconciliation` | -6 | 5 |
| `ireland_de_valera_reconciliation_capstone` | -6 | 6 |
| `ireland_active_neutrality` | -16 | 8 |
| `ireland_emergency_opening` | -24 | 9 |
| `ireland_emergency_direction` | -24 | 10 |
| `ireland_statutory_emergency` | -24 | 11 |
| `ireland_emergency_review` | -24 | 12 |
| `ireland_emergency_repeal` | -24 | 13 |
| `ireland_de_valera_emergency_capstone` | -24 | 14 |
| `ireland_recovery_bridge` | -22 | 14 |
| `ireland_restore_constitutional_calendar` | -22 | 15 |
| `ireland_material_conclusion_proof` | -22 | 16 |
| `ireland_lemass_developmental` | -20 | 9 |
| `ireland_dail_nomination` | -20 | 10 |
| `ireland_constitutional_opposition` | -10 | 8 |
| `ireland_close_oduffy_chapter` | -10 | 9 |
| `ireland_cosgrave_institutional` | -16 | 10 |
| `ireland_security_under_law` | -16 | 11 |
| `ireland_cosgrave_capstone` | -16 | 12 |
| `ireland_mulcahy_succession` | -12 | 10 |
| `ireland_mulcahy_capstone` | -12 | 11 |
| `ireland_costello_coalition` | -10 | 10 |
| `ireland_written_coalition_charter` | -10 | 11 |
| `ireland_costello_capstone` | -10 | 12 |
| `ireland_dillon_public_dissent` | -8 | 10 |
| `ireland_dillon_intervention_caucus` | -8 | 11 |
| `ireland_dillon_war_assent` | -8 | 12 |

### 6.2 Culture, industry, Northern policy, and diplomacy

| Focus ID | x | y |
| --- | ---: | ---: |
| `ireland_replacement_charter` | 4 | 4 |
| `ireland_cultural_survey` | 4 | 5 |
| `ireland_norton_parliamentary` | 0 | 6 |
| `ireland_labour_as_conscience` | 0 | 7 |
| `ireland_norton_parliamentary_capstone` | 0 | 8 |
| `ireland_clann_founding` | 2 | 6 |
| `ireland_clann_by_election` | 2 | 7 |
| `ireland_archival_record` | 4 | 6 |
| `ireland_serious_cultural_stewardship` | 4 | 7 |
| `ireland_cultural_evidence_ledger` | 4 | 8 |
| `ireland_vocational_constitution` | 6 | 6 |
| `ireland_vocational_constitution_capstone` | 6 | 7 |
| `ireland_provision_baseline` | 12 | 3 |
| `ireland_food_ledger` | 14 | 4 |
| `ireland_energy_board` | 16 | 4 |
| `ireland_transport_priority` | 18 | 4 |
| `ireland_maritime_reserve` | 18 | 6 |
| `ireland_domestic_manufacturing` | 16 | 5 |
| `ireland_rural_credit` | 14 | 5 |
| `ireland_emergency_stockpiles` | 18 | 5 |
| `ireland_development_authority` | 16 | 6 |
| `ireland_social_cooperatives` | 14 | 6 |
| `ireland_producer_accounting` | 14 | 7 |
| `ireland_provision_conclusion` | 14 | 8 |
| `ireland_lemass_developmental_capstone` | 16 | 7 |
| `ireland_northern_settlement_ledger` | -4 | 8 |
| `ireland_northern_local_authorities` | -4 | 9 |
| `ireland_northern_trade_corridor` | -6 | 10 |
| `ireland_northern_labour_social_bridge` | -4 | 10 |
| `ireland_northern_federal_preparation` | -2 | 10 |
| `ireland_northern_unitary_preparation` | -6 | 11 |
| `ireland_northern_wartime_bargain` | -4 | 11 |
| `ireland_northern_policy_proof` | -2 | 12 |
| `ireland_strict_neutrality` | 22 | 3 |
| `ireland_armed_neutrality` | 20 | 4 |
| `ireland_treaty_port_diplomacy` | 24 | 4 |
| `ireland_british_leverage_management` | 24 | 5 |
| `ireland_american_diaspora_mission` | 22 | 4 |
| `ireland_vatican_small_state_mediation` | 26 | 4 |
| `ireland_foreign_safeguards` | 22 | 6 |
| `ireland_neutrality_posture` | 22 | 7 |
| `ireland_interoperability` | 26 | 7 |

### 6.3 Army, air, and the far-right naval family

| Focus ID | x | y |
| --- | ---: | ---: |
| `ireland_readiness_baseline` | 22 | 2 |
| `ireland_readiness_command` | 28 | 3 |
| `ireland_coastwatch` | 30 | 3 |
| `ireland_professional_army` | 28 | 4 |
| `ireland_civilian_oversight` | 28 | 5 |
| `ireland_air_warning` | 30 | 4 |
| `ireland_emergency_mobilisation` | 30 | 5 |
| `ireland_port_defence_project` | 32 | 4 |
| `ireland_maritime_protection` | 32 | 5 |
| `ireland_readiness_conclusion` | 32 | 6 |
| `ireland_establish_naval_staff` | 36 | 5 |
| `ireland_rebuild_marine_service` | 36 | 6 |
| `ireland_requisition_trawler_hulls` | 36 | 7 |
| `ireland_coastal_patrol_flotilla` | 36 | 8 |
| `ireland_marine_service_reserve` | 36 | 9 |
| `ireland_harbour_defence_board` | 38 | 6 |
| `ireland_cobh_dockyard_programme` | 38 | 7 |
| `ireland_lough_swilly_watch` | 38 | 8 |
| `ireland_atlantic_convoy_office` | 38 | 9 |
| `ireland_regional_maritime_defence_pact` | 32 | 10 |

### 6.4 Conditional political and cultural families

| Focus ID | x | y |
| --- | ---: | ---: |
| `ireland_ira_republican_bridge` | -18 | 3 |
| `ireland_reassemble_ghq` | -18 | 4 |
| `ireland_arms_before_authority` | -20 | 5 |
| `ireland_authority_before_arms` | -18 | 5 |
| `ireland_german_channel` | -22 | 6 |
| `ireland_northern_question_in_arms` | -20 | 6 |
| `ireland_ira_civil_authority` | -18 | 6 |
| `ireland_ira_army_council` | -22 | 7 |
| `ireland_ira_route_capstone` | -20 | 8 |
| `ireland_ailtiri_cell_network` | -14 | 3 |
| `ireland_june_1942_public_launch` | -14 | 4 |
| `ireland_ceannaire_state` | -14 | 5 |
| `ireland_ailtiri_total_state_capstone` | -14 | 6 |
| `ireland_congress_reform_bridge` | 10 | 3 |
| `ireland_organise_congress` | 10 | 4 |
| `ireland_congress_plural_republic` | 10 | 5 |
| `ireland_congress_vanguard_cell` | 12 | 5 |
| `ireland_congress_plural_capstone` | 10 | 6 |
| `ireland_congress_vanguard_capstone` | 12 | 6 |
| `ireland_clerical_failure_bridge` | 8 | 3 |
| `ireland_clerical_guardianship` | 8 | 4 |
| `ireland_producer_constitution` | 8 | 5 |
| `ireland_clerical_route_capstone` | 8 | 6 |
| `ireland_oduffy_network_revival` | -18 | 10 |
| `ireland_oduffy_personal_command` | -20 | 11 |
| `ireland_army_acceptance` | -18 | 11 |
| `ireland_corporate_order` | -18 | 12 |
| `ireland_oduffy_personal_capstone` | -20 | 12 |
| `ireland_oduffy_corporate_capstone` | -18 | 13 |
| `ireland_high_king_evidence_gate` | 8 | 9 |
| `ireland_elective_crown` | 8 | 10 |
| `ireland_guardian_crown` | 10 | 10 |
| `ireland_crown_powers_charter` | 10 | 11 |
| `ireland_high_king_capstone` | 10 | 12 |
| `ireland_five_province_mandates` | -2 | 13 |
| `ireland_federal_republic` | -4 | 14 |
| `ireland_pentarchy_guardians` | 0 | 14 |
| `ireland_five_provinces_capstone` | -2 | 15 |
| `ireland_otherworld_investigation` | 2 | 9 |
| `ireland_otherworld_evidence_ledger` | 2 | 10 |
| `ireland_compact_with_otherworld` | 2 | 11 |
| `ireland_containment_protocol` | 4 | 11 |
| `ireland_dominion_claim` | 2 | 12 |
| `ireland_otherworld_capstone` | 2 | 13 |

### 6.5 Implemented dependency corrections

The exact coordinate table above is the final authored layout. During engine routing review, the gameplay owner also accepted these dependency corrections so the visible graph describes the actual subject architecture:

- `ireland_defence_estimates` opens from `ireland_state_still_defined`, separating defence planning from the Economic War lane.
- `ireland_provision_baseline` opens from `ireland_rural_price_board`; its existing availability requirements retain the 1938 settlement gate.
- `ireland_readiness_baseline` visually branches from `ireland_defence_estimates` beside `ireland_command_audit`; its availability block still requires Command Audit, so eligibility is unchanged while the false staircase connector is removed.
- `ireland_northern_settlement_ledger` opens from `ireland_treaty_port_transfer`, placing Northern policy under the sovereignty settlement rather than under neutrality diplomacy.
- `ireland_recovery_bridge` opens from `ireland_emergency_repeal`, so constitutional recovery no longer appears to require completion of the optional regional naval pact.
- `ireland_transport_priority` and `ireland_energy_board` jointly feed `ireland_emergency_stockpiles`, which then feeds `ireland_maritime_reserve`. This gives the transport focus a visible consumer and removes the former crossing/through-node convergence.

These are authored graph corrections, not fallbacks. Existing `available` gates preserve every cross-system state requirement that remains meaningful.

## 7. Connector-risk rules

The table was preflighted against the current 150-ID prerequisite graph. It has 150 unique IDs, 150 unique coordinate pairs, no parent at or below its child, no edge with horizontal span greater than eight, no edge with Manhattan span greater than ten, and no straight-segment crossing or straight-segment connector-through-node case.

Those static properties are necessary but are not a completion claim. HOI4 draws elbowed focus connectors, and the MCP inspector's routing result is authoritative for implementation. The gameplay owner must obey all of these rules during any engine-specific adjustment:

1. Keep every focus inside its named semantic band. A connector fix may move a focus by one or two columns inside the band; it may not put naval content back inside politics or industry.
2. Keep every prerequisite parent on a smaller y row than every child. Do not solve a crossing by putting siblings above their gateway.
3. Keep a minimum same-row centre spacing of two columns and forbid duplicate coordinate pairs.
4. Permit no connector crossing and no connector-through-unrelated-node diagnostic.
5. Permit no long connector: horizontal span must remain at most eight and Manhattan span at most ten for every edge, including `ireland_treaty_port_transfer` to `ireland_northern_settlement_ledger` and both parents of `ireland_regional_maritime_defence_pact`.
6. Route the two multi-system handoffs through empty lower space: Northern policy leaves the Treaty Port political row into x -4; the regional maritime pact converges at x 32/y 10 from interoperability and the Atlantic office.
7. A shared parent may fan to siblings, but sibling connectors may not share an unrelated child's node cell.
8. Do not alter prerequisites merely to make a line shorter. The prerequisite changes in section 6.5 were accepted because the old connectors asserted the wrong subject dependency; all other mutual exclusions, route flags, and reward contracts remain authoritative.

## 8. Implementation order and affected surfaces

1. Re-read the current focus source because it was being edited in parallel when this plan was written.
2. Confirm the current roster is still exactly the 150 IDs in section 6 and apply the dependency corrections in section 6.5.
3. Change `initial_show_position`, authored coordinates, and only the reviewed prerequisite blocks named in section 6.5 in `common/national_focus/ireland_focus_tree.txt`.
4. Preserve the eight `allow_branch` blocks and the existing country-scoped layout refresh behavior.
5. Run focus inspect, render, and raster review. Use a normal opening state and each of the eight revealed states.
6. Correct only bounded coordinate defects, maintaining the band and edge-span rules above.
7. Update `docs/plans/ireland_focus_tree/focus_tree_parliament_completion_2026-08-09.md`, `project_status.md`, and `source_of_truth_map.md` with the new authoritative revision and rendered evidence.

No localisation change is expected because no player-facing name changes. No new icon, report image, animated sprite, portrait, GUI, quote, remark, or audio research package is required. Existing icons should help distinguish families, but icon production is not a substitute for spatial grouping.

## 9. Acceptance scenarios

Implementation is accepted only when all of the following are true:

- the source contains exactly 150 focuses, preserves every mutual exclusion, and matches the reviewed dependency corrections in section 6.5;
- the opening camera centers on `ireland_state_still_defined` and shows the national, economic, and defence gateways;
- a full-tree raster makes the seven ordinary subject families identifiable without reading individual prerequisite lines;
- the Marine Service is the far-right family and is not visually embedded inside politics, culture, industry, or the Northern lane;
- ordinary culture, industry, army/air, navy, diplomacy, Northern, and political focuses are visible at start;
- each hidden root stays absent before its exact gate and appears after its gate plus the existing layout refresh;
- unrevealed branches leave no orphan lines or unexplained holes in an ordinary branch;
- focus inspection reports zero connector crossings, zero connector-through-node intersections, zero long connectors, zero parent-below-child cases, zero duplicate coordinates, and zero spacing defects;
- review at the normal UI scale confirms focus cards and connector turns do not visually collide even if the structural inspector is clean;
- no route eligibility, mutual exclusion, localisation, asset, or GUI behavior changes as an accidental side effect of the layout pass.

## 10. Scope boundary and promotion

Do not add branch-label GUI, new focuses, new hidden routes, new national spirits, route rewiring, or new assets in this pass. The defect is spatial architecture, not missing content. Adding a custom GUI legend would be bloat while the native focus coordinates remain unclear.

This addendum remains under `docs/plans/ireland_focus_tree/improvement_loop/` as the implementation record. The accepted spatial grammar, reveal policy, and reviewed dependency corrections are promoted into the architecture map and completion/source-of-truth reports. The historical defective MCP snapshot remains evidence only.
