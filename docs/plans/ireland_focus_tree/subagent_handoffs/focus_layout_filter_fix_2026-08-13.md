# Ireland focus layout and search-filter handoff

## Scope

Owned files only: `common/national_focus/ireland_focus_tree.txt` and this handoff. Focus IDs, prerequisites, rewards, branch reveal conditions, and the 150-focus count were preserved.

## Layout changes

- Shortcuts now target visual branch midpoints: politics `ireland_government_formation` (0.66), industry `ireland_development_authority` (0.66), and defence `ireland_maritime_protection` (0.70).
- Politics/core lane was compacted around the authored left lane (constitutional/government/trade chain stays visually grouped).
- Industry lane was straightened into three compact columns: food/rural/social/producer/provision at x=0, energy/domestic/development at x=2, and transport/emergency/maritime at x=4.
- Hidden/reveal lanes were repositioned only to avoid overlaps and connector crossings; no gates or rewards changed.
- Final geometry alignment kept the defence root separated at `ireland_defence_estimates` x=12 and straightened five previously-advised connectors; the clerical bridge remains the one authored detour (see residuals).

Exact coordinate IDs changed by this subagent (64): `ireland_1938_trade_settlement`, `ireland_active_neutrality`, `ireland_ailtiri_cell_network`, `ireland_ailtiri_total_state_capstone`, `ireland_american_diaspora_mission`, `ireland_armed_neutrality`, `ireland_arms_before_authority`, `ireland_authority_before_arms`, `ireland_ceannaire_state`, `ireland_clerical_guardianship`, `ireland_clerical_route_capstone`, `ireland_command_audit`, `ireland_compact_with_otherworld`, `ireland_congress_plural_capstone`, `ireland_congress_plural_republic`, `ireland_congress_vanguard_capstone`, `ireland_congress_vanguard_cell`, `ireland_constitutional_draft`, `ireland_constitutional_stewardship`, `ireland_containment_protocol`, `ireland_crown_powers_charter`, `ireland_de_valera_reconciliation`, `ireland_de_valera_reconciliation_capstone`, `ireland_de_valera_stewardship`, `ireland_development_authority`, `ireland_dominion_claim`, `ireland_economic_war_review`, `ireland_election_mandate`, `ireland_elective_crown`, `ireland_energy_board`, `ireland_food_ledger`, `ireland_foreign_safeguards`, `ireland_german_channel`, `ireland_government_formation`, `ireland_guardian_crown`, `ireland_high_king_capstone`, `ireland_high_king_evidence_gate`, `ireland_ira_army_council`, `ireland_ira_civil_authority`, `ireland_ira_republican_bridge`, `ireland_ira_route_capstone`, `ireland_june_1942_public_launch`, `ireland_maritime_reserve`, `ireland_northern_local_authorities`, `ireland_northern_question_in_arms`, `ireland_northern_unitary_preparation`, `ireland_northern_wartime_bargain`, `ireland_organise_congress`, `ireland_otherworld_capstone`, `ireland_otherworld_evidence_ledger`, `ireland_otherworld_investigation`, `ireland_producer_accounting`, `ireland_producer_constitution`, `ireland_provision_baseline`, `ireland_provision_conclusion`, `ireland_reassemble_ghq`, `ireland_replacement_charter`, `ireland_republican_government`, `ireland_rural_price_board`, `ireland_social_cooperatives`, `ireland_transport_priority`, `ireland_treaty_port_diplomacy`, `ireland_treaty_port_transfer`, `ireland_vatican_small_state_mediation`.

Final parent geometry-only alignment IDs: `ireland_constitutional_draft` restored to x=-14 beside `ireland_election_timetable`; `ireland_interoperability` moved to x=13 beside `ireland_civilian_oversight`; `ireland_british_leverage_management` moved to x=4 beside `ireland_treaty_port_diplomacy`; `ireland_northern_local_authorities` moved to x=10 beside `ireland_northern_settlement_ledger`; `ireland_five_province_mandates` moved to x=11 beside `ireland_northern_policy_proof`; and `ireland_defence_estimates` moved to x=12 for root separation. No prerequisites, rewards, gates, or filters changed in this alignment pass.

Route coverage (all retained):

| Family | Coverage | Notes |
| --- | --- | --- |
| Politics / constitutional | complete | constitutional draft → election mandate → government formation → 1938 settlement → treaty-port transfer |
| Industry / provision | complete | provision baseline → food/energy/transport → rural/domestic/emergency → social/development/maritime → accounting/conclusion |
| Defence / readiness | complete | defence estimates, readiness, naval staff, marine service, army interoperability |
| Diplomacy / Northern | complete | neutrality, foreign safeguards, Northern settlement and federal/unitary branches |
| Revealed families | complete | IRA, Congress, clerical, Ailtiri, high-king, Otherworld, and five-province branches retain authored reveals |

## Search-filter policy and changes

XP filters are strict: `FOCUS_FILTER_ARMY_XP`, `FOCUS_FILTER_NAVY_XP`, and `FOCUS_FILTER_AIR_XP` appear only when the focus has a direct corresponding XP effect in `completion_reward`. A source parser found zero mismatches after the patch.

- Corrected false XP tags: treaty port transfer, security under law, transport priority, maritime reserve, harbour defence board, Cobh dockyard programme, treaty-port diplomacy, arms/authority branches, Northern question in arms, O'Duffy personal command, army acceptance, and Ceannaire state.
- Corrected true XP tags: marine service reserve → Army XP; naval staff → Army + Navy XP; Lough Swilly watch → Air XP; regional maritime defence pact → Army + Navy + Air XP; interoperability → Army + Air XP.
- Added `FOCUS_FILTER_RESEARCH` to focuses with direct research/doctrine/research-speed effects (industry, command audit, treaty-port, readiness, naval/air research, professional army, interoperability, armed neutrality, German channel, Congress vanguard). Existing authored cultural/evidence research markers remain unchanged.
- Industry tags were kept on direct industrial/provision focuses; manpower tags were retained only where existing branch semantics called for them.

Exact search-filter IDs changed (38): `ireland_1938_trade_settlement`, `ireland_air_warning`, `ireland_armed_neutrality`, `ireland_arms_before_authority`, `ireland_army_acceptance`, `ireland_authority_before_arms`, `ireland_ceannaire_state`, `ireland_coastal_patrol_flotilla`, `ireland_coastwatch`, `ireland_cobh_dockyard_programme`, `ireland_command_audit`, `ireland_congress_vanguard_cell`, `ireland_development_authority`, `ireland_domestic_manufacturing`, `ireland_economic_war_review`, `ireland_establish_naval_staff`, `ireland_food_ledger`, `ireland_german_channel`, `ireland_harbour_defence_board`, `ireland_interoperability`, `ireland_lough_swilly_watch`, `ireland_marine_service_reserve`, `ireland_maritime_protection`, `ireland_maritime_reserve`, `ireland_northern_question_in_arms`, `ireland_oduffy_personal_command`, `ireland_port_defence_project`, `ireland_producer_accounting`, `ireland_professional_army`, `ireland_provision_baseline`, `ireland_readiness_baseline`, `ireland_regional_maritime_defence_pact`, `ireland_rural_credit`, `ireland_rural_price_board`, `ireland_security_under_law`, `ireland_transport_priority`, `ireland_treaty_port_diplomacy`, `ireland_treaty_port_transfer`.

## Validation evidence

Final `hoi4_focus_inspect` artifact (revision `ff82977eb9daf44c1d7a2612ea04ba44e48427d9e74c8e58f9026aa748610e27`): `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/68a96e8669db136c298b235364bac3b0a322e5e0bcf7da2fc80f1564f99e8b02/a8868d5f848170cd9643b85cbea02e14693ae0a5ba4aede4cfc3d82378decfa8/focus-inspect.ff82977eb9daf44c.json`.

- 150 focuses, 150 connectors; exactly three no-prerequisite `allow_branch` roots (`ireland_state_still_defined`, `ireland_economic_war_review`, `ireland_defence_estimates`).
- `crossingCount=0`, `nodeIntersectionCount=0`, `longConnectorCount=0`, `tooCloseSameRowPairCount=0`, minimum same-row spacing 2; maximum horizontal span 6; inspect validation passed with one layout advisory.
- Final render artifacts: HTML `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/cbcc0c5f6805d56fb6bc45e4fdc3735d4ddd95c3bd358b6b6e8d16ea57fb778c/ccb7fd3fac863a4e13ab1d405d0c152c73462c64dcafeebb32968a985c185079/ireland_focus_tree.focus.html`; SVG `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/48f72d38181f34356877accc12e866b432595198497fac9d247f870e85995e20/afc77fc5cda82e10dd364a3d3204ff5a4128b5d223679dab9fc79fc67926ffcc/ireland_focus_tree.focus.svg`; JSON `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/024a11cd5652a73ab277e3782ab63e3d6e332a5aee8209f553e672be1891a779/1a5583bdad209e632384ebaa78083bb3cb007a60df801b3ad1f8f5b5d41d7ef3/ireland_focus_tree.focus.json`; source map `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/070a9720a0c7a83bfd6803a7ec893dc63960a299d3d1dcc2bd2df395b5d1ecc5/0b04853eec2e9511d41c98062d75cdceca1439368d9517e560cb18ba9072eabf/ireland_focus_tree.focus.source-map.json`; plan `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/871e694d122163d95452276d4a1907b5bb717eb859f469ba837a1cd26c1f937a/031359b542a855e0de38ef9fc9416ddde095ae16d4aa69dbad2b399e54dfae72/ireland_focus_tree.focus.plan.json`.

## Icons, localisation, rewards, AI

- Icon coverage: unchanged; all 150 existing `GFX_focus_ireland_*` references resolve in the render inventory. No asset files changed.
- Localisation keys and reward bodies were not renamed or removed. No reward/localisation mismatch was introduced.
- AI blocks and route weights were not changed. Existing AI behavior remains the parent agent's responsibility.

## Residuals / skipped work

MCP reports one retained non-blocking linear-detour advisory: `ireland_clerical_failure_bridge` -> `ireland_clerical_guardianship` (horizontal span 2; expected 0). The only other diagnostic is the unrelated vanilla `continuous_restrict_freedom_desc` localisation warning. Five prior detours were aligned while preserving zero crossings/intersections/long connectors/spacing defects. No new route, fallback, or simplification was introduced.
