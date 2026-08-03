# Ireland 140-action material and safeguard ledger

Feature slug: `ireland_focus_tree`
Audit date: 2026-07-29
Status: static source audit; HOI4 was not launched.

## Audit contract

This is the row-level ledger for the canonical 140 action IDs. Each row was checked against the current decision source for its native PP cost, named-ledger surcharge text and surcharge driver, action burden, AI block, cleanup/removal, named state/helper or linked mission objective, and any physical input named by the action contract. `none` in the material column means the row is a political, administrative, legitimacy, leverage, or route-state contract; it is not an assertion that every action needs a stockpile charge.

The bounded review found 140/140 actions, 13 categories, and 54 mission families. Every action has a native cost, dynamic-cost key, burden variable, AI block, and cleanup/removal path. All 54 missions have a named map-objective helper, a 45–365 day timeout, full/partial completion, timeout failure/escalation, cancellation result, cleanup, and AI. The source-level check found no unambiguous missing physical admission gate among the canonical material rows.

The review repaired 77 player-facing `custom_cost_text` labels whose displayed ledger differed from the ledger used by the action's PP/CP surcharge. After repair, the action-level comparison reports 140/140 aligned labels. `license_protected_workshops` remains the accepted factory-project pattern (factory reservation plus industrial-site mission, without an invented stockpile material), while `integrate_a_voluntary_member_contribution` is helper-backed and requires a paid class-specific troop/ship/finance/intelligence/infrastructure choice.

## Row ledger

| # | Exact action ID | Category | Surcharge driver shown | Material admission disposition | Map evidence | Mission/deadline | AI / cleanup |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 001 | `slopx_ireland_action_convene_a_cabinet_cohesion_review` | Settlement | aligned: social_consent | decision-only political/administrative/legitimacy contract | named mission objective | maintain_cabinet_discipline/90d | yes/yes |
| 002 | `slopx_ireland_action_request_a_confidence_vote` | Settlement | aligned: dail_mandate | decision-only political/administrative/legitimacy contract | named mission objective | assemble_seventy_routine_votes/45d | yes/yes |
| 003 | `slopx_ireland_action_negotiate_confidence_and_supply` | Settlement | aligned: social_consent | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 004 | `slopx_ireland_action_nominate_an_alternative_taoiseach` | Settlement | aligned: dail_mandate | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 005 | `slopx_ireland_action_ask_the_president_for_dissolution` | Settlement | aligned: national_settlement | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 006 | `slopx_ireland_action_invoke_the_council_of_state` | Settlement | aligned: administrative_reach | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 007 | `slopx_ireland_action_publish_a_government_programme` | Settlement | aligned: dail_mandate | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 008 | `slopx_ireland_action_establish_a_caretaker_cabinet` | Settlement | aligned: administrative_reach | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 009 | `slopx_ireland_action_review_the_six_month_settlement` | Settlement | aligned: national_settlement | decision-only political/administrative/legitimacy contract | named mission objective | complete_six_month_settlement_review/180d | yes/yes |
| 010 | `slopx_ireland_action_restore_ordinary_constitutional_procedure` | Settlement | aligned: social_consent | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 011 | `slopx_ireland_action_update_the_electoral_register` | Elections | aligned: administrative_reach | manpower; paired gate/charge source row | named mission objective | conduct_a_free_general_election/105d | yes/yes |
| 012 | `slopx_ireland_action_protect_campaign_freedom` | Elections | aligned: social_consent | manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 013 | `slopx_ireland_action_organise_county_candidates` | Elections | aligned: dail_mandate | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 014 | `slopx_ireland_action_negotiate_transfer_pacts` | Elections | aligned: social_consent | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 015 | `slopx_ireland_action_secure_polling_stations` | Elections | aligned: security_loyalty | equipment, manpower, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 016 | `slopx_ireland_action_count_formal_and_routine_votes` | Elections | aligned: dail_mandate | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 017 | `slopx_ireland_action_open_coalition_negotiations` | Elections | aligned: social_consent | decision-only political/administrative/legitimacy contract | named mission objective | form_a_government_after_the_poll/60d | yes/yes |
| 018 | `slopx_ireland_action_assign_cabinet_portfolios` | Elections | aligned: administrative_reach | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 019 | `slopx_ireland_action_ratify_the_coalition_charter` | Elections | aligned: social_consent | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 020 | `slopx_ireland_action_prepare_a_by_election` | Elections | aligned: dail_mandate | decision-only political/administrative/legitimacy contract | named mission objective | protect_a_by_election/100d | yes/yes |
| 021 | `slopx_ireland_action_negotiate_an_education_compact` | Organised Society | aligned: minority_confidence | decision-only political/administrative/legitimacy contract | named mission objective | deliver_the_education_settlement/150d | yes/yes |
| 022 | `slopx_ireland_action_contract_parish_welfare_services` | Organised Society | aligned: church_institutional_influence | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 023 | `slopx_ireland_action_create_a_public_health_board` | Organised Society | aligned: administrative_reach | manpower, factory/platform; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 024 | `slopx_ireland_action_charter_collective_bargaining` | Organised Society | aligned: labour_organisation | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 025 | `slopx_ireland_action_set_agricultural_prices` | Organised Society | aligned: rural_organisation | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 026 | `slopx_ireland_action_recognise_an_agrarian_support_bloc` | Organised Society | aligned: dail_mandate | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 027 | `slopx_ireland_action_convene_a_vocational_council` | Organised Society | aligned: federal_cohesion | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 028 | `slopx_ireland_action_audit_church_service_dependency` | Organised Society | aligned: church_institutional_influence | decision-only political/administrative/legitimacy contract | named mission objective | audit_parish_service_contracts/120d | yes/yes |
| 029 | `slopx_ireland_action_protect_minority_institutions` | Organised Society | aligned: minority_confidence | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 030 | `slopx_ireland_action_mediate_an_essential_service_dispute` | Organised Society | aligned: labour_organisation | decision-only political/administrative/legitimacy contract | named mission objective | keep_essential_services_running/60d | yes/yes |
| 031 | `slopx_ireland_action_fund_gaeltacht_administration` | Cultural | aligned: cultural_capacity | equipment, manpower, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 032 | `slopx_ireland_action_expand_folklore_collection` | Cultural | aligned: cultural_capacity | equipment, manpower, transport; paired gate/charge source row | named mission objective | collect_a_national_folklore_cycle/180d | yes/yes |
| 033 | `slopx_ireland_action_survey_provincial_archives` | Cultural | aligned: cultural_capacity | manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 034 | `slopx_ireland_action_hold_a_provincial_cultural_congress` | Cultural | aligned: cultural_capacity | equipment, transport; paired gate/charge source row | named mission objective | hold_a_five_region_cultural_congress/210d | yes/yes |
| 035 | `slopx_ireland_action_protect_a_historic_site` | Cultural | aligned: cultural_capacity | equipment, manpower, transport; paired gate/charge source row | named helper/region contract | decision-only | yes/yes |
| 036 | `slopx_ireland_action_standardise_irish_language_services` | Cultural | aligned: cultural_capacity | manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 037 | `slopx_ireland_action_test_a_restoration_claim` | Cultural | aligned: hidden_evidence | decision-only political/administrative/legitimacy contract | named mission objective | verify_the_restoration_evidence/270d | yes/yes |
| 038 | `slopx_ireland_action_contain_a_public_folklore_panic` | Cultural | aligned: public_knowledge | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 039 | `slopx_ireland_action_convene_a_hidden_evidence_council` | Cultural | aligned: hidden_evidence | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 040 | `slopx_ireland_action_archive_the_failed_restoration` | Cultural | aligned: cultural_capacity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 041 | `slopx_ireland_action_audit_the_republican_commands` | Radical | aligned: republican_network_strength | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 042 | `slopx_ireland_action_convene_the_convention_of_commands` | Radical | aligned: army_council_cohesion | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 043 | `slopx_ireland_action_create_a_civil_republican_directorate` | Radical | aligned: civil_republican_authority | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 044 | `slopx_ireland_action_rebuild_the_republican_congress` | Radical | aligned: congress_coalition_cohesion | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 045 | `slopx_ireland_action_ratify_the_common_programme` | Radical | aligned: social_consent | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 046 | `slopx_ireland_action_reassemble_the_national_corporate_party` | Radical | aligned: corporate_network_strength | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 047 | `slopx_ireland_action_impose_compulsory_estates` | Radical | aligned: minority_confidence | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 048 | `slopx_ireland_action_organise_ailtiri_cells` | Radical | aligned: ailtiri_cell_strength | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 049 | `slopx_ireland_action_launch_the_ailtiri_party_state` | Radical | aligned: national_settlement | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 050 | `slopx_ireland_action_dissolve_the_failed_underground` | Radical | aligned: security_loyalty | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 051 | `slopx_ireland_action_set_county_tillage_quotas` | Provision | aligned: provision_food | equipment, manpower, transport; paired gate/charge source row | named mission objective | meet_the_county_tillage_schedule/150d | yes/yes |
| 052 | `slopx_ireland_action_distribute_seed_and_fertiliser` | Provision | aligned: provision_food | equipment, manpower, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 053 | `slopx_ireland_action_repair_mills_and_storage` | Provision | aligned: provision_food | equipment, fuel, transport, factory/platform; paired gate/charge source row | named mission objective | bring_the_harvest_to_market/120d | yes/yes |
| 054 | `slopx_ireland_action_purchase_emergency_livestock` | Provision | aligned: provision_food | equipment, manpower, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 055 | `slopx_ireland_action_license_protected_workshops` | Provision | aligned: industrial_capacity | accepted factory-project pattern | named mission objective | commission_the_protected_workshop_network/180d | yes/yes |
| 056 | `slopx_ireland_action_commission_a_developmental_plant` | Provision | aligned: industrial_capacity | equipment, convoy, transport; paired gate/charge source row | named mission objective | complete_a_developmental_plant/270d | yes/yes |
| 057 | `slopx_ireland_action_issue_ration_books` | Provision | aligned: provision_food | manpower, transport; paired gate/charge source row | named mission objective | supply_the_capital_through_winter/120d | yes/yes |
| 058 | `slopx_ireland_action_rebalance_fuel_allocation` | Provision | aligned: provision_energy | fuel, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 059 | `slopx_ireland_action_mobilise_emergency_turf` | Provision | aligned: provision_energy | equipment, manpower, transport; paired gate/charge source row | named mission objective | cut_and_dry_the_turf/120d | yes/yes |
| 060 | `slopx_ireland_action_repair_a_named_rail_corridor` | Provision | aligned: provision_transport | equipment, manpower, fuel, transport, factory/platform; paired gate/charge source row | named mission objective | restore_the_dublin_to_cork_corridor/180d | yes/yes |
| 061 | `slopx_ireland_action_establish_a_strategic_depot` | Provision | aligned: readiness_supply | equipment, manpower, fuel, transport, factory/platform; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 062 | `slopx_ireland_action_charter_foreign_tonnage` | Provision | aligned: provision_maritime | equipment, manpower, convoy, transport; paired gate/charge source row | named mission objective | keep_an_essential_cargo_route_open/120d | yes/yes |
| 063 | `slopx_ireland_action_purchase_a_merchant_vessel` | Provision | aligned: provision_maritime | equipment, manpower, convoy, transport; paired gate/charge source row | named mission objective | replace_a_lost_merchant_vessel/270d | yes/yes |
| 064 | `slopx_ireland_action_reroute_an_essential_cargo` | Provision | aligned: provision_maritime | equipment, fuel, convoy, transport; paired gate/charge source row | named mission objective | keep_an_essential_cargo_route_open/120d | yes/yes |
| 065 | `slopx_ireland_action_launch_an_emergency_housing_scheme` | Provision | aligned: regional_capacity | manpower, transport, factory/platform; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 066 | `slopx_ireland_action_fund_a_western_regional_portfolio` | Provision | aligned: regional_capacity | equipment, transport, factory/platform; paired gate/charge source row | named mission objective | deliver_a_western_regional_portfolio/300d | yes/yes |
| 067 | `slopx_ireland_action_run_a_command_district_exercise` | Readiness | aligned: readiness_command | equipment, fuel; paired gate/charge source row | named mission objective | prove_the_command_district/105d | yes/yes |
| 068 | `slopx_ireland_action_standardise_infantry_equipment` | Readiness | aligned: readiness_equipment | equipment, factory/platform, experience; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 069 | `slopx_ireland_action_procure_rifles_and_support_equipment` | Readiness | aligned: readiness_equipment | equipment, convoy, factory/platform; paired gate/charge source row | named mission objective | deliver_a_british_supply_agreement/150d;complete_an_american_procurement_mission/240d;test_a_german_arms_promise/150d;keep_an_essential_cargo_route_open/120d | yes/yes |
| 070 | `slopx_ireland_action_activate_a_cadre_reserve` | Readiness | aligned: readiness_mobilisation | equipment, manpower; paired gate/charge source row | named mission objective | equip_a_reserve_brigade/150d | yes/yes |
| 071 | `slopx_ireland_action_expand_the_local_security_force` | Readiness | aligned: security_loyalty | equipment, manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 072 | `slopx_ireland_action_expand_the_local_defence_force` | Readiness | aligned: readiness_mobilisation | equipment, manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 073 | `slopx_ireland_action_motorise_a_strategic_route` | Readiness | aligned: readiness_supply | equipment, fuel, transport; paired gate/charge source row | named mission objective | secure_the_dublin_to_belfast_corridor/120d | yes/yes |
| 074 | `slopx_ireland_action_build_a_coastwatch_sector_network` | Readiness | aligned: readiness_warning | equipment, manpower; paired gate/charge source row | named mission objective | complete_a_coastwatch_sector/120d | yes/yes |
| 075 | `slopx_ireland_action_install_harbour_defences` | Readiness | aligned: readiness_maritime_protection | equipment, manpower, factory/platform; paired gate/charge source row | named mission objective | defend_a_treaty_port/210d | yes/yes |
| 076 | `slopx_ireland_action_organise_marine_patrols` | Readiness | aligned: readiness_maritime_protection | equipment, manpower, fuel, convoy, experience; paired gate/charge source row | named mission objective | patrol_the_neutral_approaches/105d | yes/yes |
| 077 | `slopx_ireland_action_open_a_g2_liaison_channel` | Readiness | aligned: readiness_intelligence | equipment; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 078 | `slopx_ireland_action_turn_or_intern_a_foreign_agent` | Readiness | aligned: readiness_intelligence | equipment, manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 079 | `slopx_ireland_action_protect_an_operational_plan` | Readiness | aligned: readiness_intelligence | decision-only political/administrative/legitimacy contract | named mission objective | protect_plan_w/120d | yes/yes |
| 080 | `slopx_ireland_action_demobilise_a_force_tier` | Readiness | aligned: readiness_display | decision-only political/administrative/legitimacy contract | named mission objective | demobilise_without_losing_the_cadre/210d | yes/yes |
| 081 | `slopx_ireland_action_intercept_an_airspace_violation` | Neutrality | aligned: neutrality_integrity | equipment, fuel; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 082 | `slopx_ireland_action_intern_a_belligerent_crew` | Neutrality | aligned: neutrality_integrity | manpower; paired gate/charge source row | named mission objective | resolve_an_aircrew_internment_case/90d | yes/yes |
| 083 | `slopx_ireland_action_release_or_exchange_internees` | Neutrality | aligned: neutrality_integrity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 084 | `slopx_ireland_action_investigate_a_neutral_shipping_loss` | Neutrality | aligned: neutrality_integrity | decision-only political/administrative/legitimacy contract | named mission objective | investigate_a_merchant_sinking/120d | yes/yes |
| 085 | `slopx_ireland_action_mark_and_publicise_neutral_shipping` | Neutrality | aligned: neutrality_integrity | equipment; paired gate/charge source row | named mission objective | maintain_equal_belligerent_rules/150d | yes/yes |
| 086 | `slopx_ireland_action_share_a_controlled_weather_report` | Neutrality | aligned: neutrality_integrity | equipment, manpower; paired gate/charge source row | named mission objective | keep_the_blacksod_station_reporting/105d | yes/yes |
| 087 | `slopx_ireland_action_answer_a_foreign_access_request` | Neutrality | aligned: neutrality_integrity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 088 | `slopx_ireland_action_tighten_or_narrow_censorship` | Neutrality | aligned: neutrality_integrity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 089 | `slopx_ireland_action_open_a_border_corridor` | Neutrality | aligned: neutrality_integrity | equipment, manpower, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 090 | `slopx_ireland_action_restore_neutrality_integrity` | Neutrality | aligned: neutrality_integrity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 091 | `slopx_ireland_action_renegotiate_a_british_supply_contract` | Foreign | aligned: british_leverage | equipment, convoy; paired gate/charge source row | named mission objective | deliver_a_british_supply_agreement/150d | yes/yes |
| 092 | `slopx_ireland_action_formalise_plan_w_liaison` | Foreign | aligned: british_leverage | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 093 | `slopx_ireland_action_send_an_american_procurement_mission` | Foreign | aligned: american_leverage | equipment, convoy; paired gate/charge source row | named mission objective | complete_an_american_procurement_mission/240d | yes/yes |
| 094 | `slopx_ireland_action_mobilise_diaspora_relief` | Foreign | aligned: diaspora_support | equipment, convoy; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 095 | `slopx_ireland_action_receive_a_german_emissary` | Foreign | aligned: german_leverage | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 096 | `slopx_ireland_action_demand_proof_of_german_delivery` | Foreign | aligned: foreign_exposure | decision-only political/administrative/legitimacy contract | named mission objective | test_a_german_arms_promise/150d | yes/yes |
| 097 | `slopx_ireland_action_seek_vatican_humanitarian_mediation` | Foreign | aligned: vatican_leverage | decision-only political/administrative/legitimacy contract | named mission objective | conclude_a_vatican_relief_mediation/120d | yes/yes |
| 098 | `slopx_ireland_action_convene_a_neutral_states_consultation` | Foreign | aligned: neutrality_integrity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 099 | `slopx_ireland_action_write_anti_dependency_clauses` | Foreign | aligned: sovereignty_safeguards | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 100 | `slopx_ireland_action_terminate_a_failed_sponsor_agreement` | Foreign | aligned: foreign_exposure | equipment, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 101 | `slopx_ireland_action_open_cross_border_confidence_measures` | Northern | aligned: northern_integration_capacity | manpower; paired gate/charge source row | named mission objective | open_the_cross_border_health_service/150d | yes/yes |
| 102 | `slopx_ireland_action_invite_northern_delegations` | Northern | aligned: unionist_consent | decision-only political/administrative/legitimacy contract | named mission objective | secure_a_representative_northern_convention/210d | yes/yes |
| 103 | `slopx_ireland_action_negotiate_british_flexibility` | Northern | aligned: northern_british_flexibility | equipment, manpower, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 104 | `slopx_ireland_action_protect_northern_campaign_freedom` | Northern | aligned: social_consent | equipment; paired gate/charge source row | named mission objective | conduct_a_supervised_plebiscite/240d | yes/yes |
| 105 | `slopx_ireland_action_convene_a_federal_powers_conference` | Northern | aligned: federal_cohesion | decision-only political/administrative/legitimacy contract | named mission objective | ratify_the_federal_settlement/300d | yes/yes |
| 106 | `slopx_ireland_action_draft_a_unitary_safeguards_charter` | Northern | aligned: northern_integration_capacity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 107 | `slopx_ireland_action_build_a_labour_industrial_settlement` | Northern | aligned: northern_labour_cooperation | equipment, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 108 | `slopx_ireland_action_prepare_a_wartime_unity_bargain` | Northern | aligned: northern_security_stability | equipment, transport; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 109 | `slopx_ireland_action_plan_a_coercive_northern_campaign` | Northern | aligned: northern_security_stability | equipment, manpower, fuel, transport; paired gate/charge source row | named mission objective | take_and_hold_belfast/150d | yes/yes |
| 110 | `slopx_ireland_action_defer_the_constitutional_claim_lawfully` | Northern | aligned: northern_integration_capacity | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 111 | `slopx_ireland_action_establish_a_transitional_authority` | Occupation | aligned: administrative_reach | manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 112 | `slopx_ireland_action_vet_and_rebuild_policing` | Occupation | aligned: northern_security_stability | equipment, transport; paired gate/charge source row | named mission objective | restore_ordinary_policing/240d | yes/yes |
| 113 | `slopx_ireland_action_disarm_paramilitary_organisations` | Occupation | aligned: security_loyalty | manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 114 | `slopx_ireland_action_maintain_welfare_and_pensions` | Occupation | aligned: social_consent | manpower; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 115 | `slopx_ireland_action_restore_belfast_industrial_contracts` | Occupation | aligned: industrial_capacity | equipment, fuel, transport, factory/platform; paired gate/charge source row | named mission objective | reopen_belfast_industry/300d | yes/yes |
| 116 | `slopx_ireland_action_settle_education_and_religious_safeguards` | Occupation | aligned: minority_confidence | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 117 | `slopx_ireland_action_merge_tax_and_debt_administration` | Occupation | aligned: administrative_reach | equipment, convoy; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 118 | `slopx_ireland_action_integrate_or_devolve_military_command` | Occupation | aligned: readiness_command | equipment, experience; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 119 | `slopx_ireland_action_review_foreign_guarantees` | Occupation | aligned: northern_british_flexibility | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 120 | `slopx_ireland_action_conduct_the_core_eligibility_review` | Occupation | aligned: northern_integration_capacity | decision-only political/administrative/legitimacy contract | named mission objective | complete_the_stage_five_integration_review/365d | yes/yes |
| 121 | `slopx_ireland_action_invite_a_celtic_cultural_partner` | Regional | aligned: cultural_capacity | decision-only political/administrative/legitimacy contract | named mission objective | ratify_a_regional_charter/240d | yes/yes |
| 122 | `slopx_ireland_action_draft_an_atlantic_consultation_charter` | Regional | aligned: provision_maritime | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 123 | `slopx_ireland_action_propose_a_regional_defence_league` | Regional | aligned: readiness_display | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 124 | `slopx_ireland_action_recognise_a_liberated_authority` | Regional | aligned: diplomatic_recognition | equipment, convoy; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 125 | `slopx_ireland_action_offer_a_protectorate_treaty` | Regional | aligned: northern_british_flexibility | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 126 | `slopx_ireland_action_convene_a_crown_association` | Regional | aligned: royal_legitimacy | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 127 | `slopx_ireland_action_renew_the_fivefold_compact` | Regional | aligned: federal_cohesion | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 128 | `slopx_ireland_action_fulfil_a_compact_obligation` | Regional | aligned: compact_trust | equipment, manpower; paired gate/charge source row | named mission objective | fulfil_the_compact_at_five_sites/300d | yes/yes |
| 129 | `slopx_ireland_action_dissolve_a_failed_regional_order` | Regional | aligned: foreign_exposure | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 130 | `slopx_ireland_action_integrate_a_voluntary_member_contribution` | Regional | aligned: northern_integration_capacity | helper-backed paid choice | named mission objective | meet_the_member_contribution_schedule/180d | yes/yes |
| 131 | `slopx_ireland_action_review_the_emergency_declaration` | Postwar | aligned: national_settlement | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 132 | `slopx_ireland_action_replace_emergency_supply_orders` | Postwar | aligned: provision_display | decision-only political/administrative/legitimacy contract | named mission objective | end_wartime_rationing_safely/240d | yes/yes |
| 133 | `slopx_ireland_action_demobilise_and_settle_veterans` | Postwar | aligned: social_consent | equipment, manpower, factory/platform; paired gate/charge source row | named mission objective | settle_the_demobilised_forces/300d | yes/yes |
| 134 | `slopx_ireland_action_renew_the_merchant_fleet` | Postwar | aligned: provision_maritime | equipment, manpower, convoy; paired gate/charge source row | named state gate | decision-only | yes/yes |
| 135 | `slopx_ireland_action_launch_a_reconstruction_portfolio` | Postwar | aligned: regional_capacity | equipment, transport, factory/platform; paired gate/charge source row | named mission objective | complete_national_reconstruction/365d | yes/yes |
| 136 | `slopx_ireland_action_settle_the_republic_question` | Postwar | aligned: national_settlement | factory/platform; paired gate/charge source row | named mission objective | bring_the_republic_settlement_into_force/150d | yes/yes |
| 137 | `slopx_ireland_action_review_commonwealth_relations` | Postwar | aligned: british_leverage | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 138 | `slopx_ireland_action_apply_for_united_nations_membership` | Postwar | aligned: diplomatic_recognition | decision-only political/administrative/legitimacy contract | named mission objective | build_support_for_united_nations_admission/300d | yes/yes |
| 139 | `slopx_ireland_action_accept_or_refuse_reconstruction_aid` | Postwar | aligned: foreign_exposure | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |
| 140 | `slopx_ireland_action_complete_the_route_conclusion_review` | Postwar | aligned: national_settlement | decision-only political/administrative/legitimacy contract | named state gate | decision-only | yes/yes |

## Evidence and exceptions

- The exact 77 repaired action IDs and displayed→actual ledger pairs are recorded in `docs/plans/ireland_focus_tree/decision_mission_lifecycle_cost_tranche_2026-07-28.md`; the repair is applied in `common/decisions/slopx_ireland_decisions.txt`.
- The static source sweep reports 140/140 actions with native cost, custom cost text, burden, AI, and cleanup; 54/54 missions with timeout, result writes, map-objective helper, AI, and cancellation/timeout cleanup.
- Eight actions intentionally use named helper/region contracts rather than a numeric `state =` line: `protect_a_historic_site`, `repair_a_named_rail_corridor`, `reroute_an_essential_cargo`, `run_a_command_district_exercise`, `build_a_coastwatch_sector_network`, `install_harbour_defences`, `plan_a_coercive_northern_campaign`, and `restore_belfast_industrial_contracts`.
- `slopx_ireland_action_integrate_a_voluntary_member_contribution` is not a missing material gate: the helper-backed selection requires a paid class-specific payload and safeguard before commitment, and the linked mission evaluates the selected class.
- `slopx_ireland_action_license_protected_workshops` remains a documented accepted factory-project pattern; no extra material charge was invented without a canonical value.

## Remaining gates

This ledger closes the row-level source audit and the 77 cost-text mismatches. At
the time of this tranche it did not clear restricted/blocked source-manifest
rows, settle the then-pending Radical/Underground wording question, add engine
support for staged achievement visibility, or substitute live gameplay for the
required local engine-reference checks. The accepted M2/A2 ruling later closed
the Radical/Underground and achievement-schema decisions; the current source
clearance remainder is the 37 blocked manifest rows.

No live HOI4 session, save, or log was used.

## Current authority addendum (2026-08-02)

The former native-cost wording and the earlier Radical/Underground and staged-achievement
open notes are superseded by the accepted M2/A2 ruling and the current source-of-truth
map. The 140 actions now use custom-cost-only presentation, manual base Political Power
deduction, named-ledger surcharge deduction, and per-action ai_hint_pp_cost values.
The current static contract is 140/140 for AI hints, base deductions, action-specific
cost localisation, and zero regular cost fields. The remaining source-side blocker
is the current 37-row blocked clearance queue; no blocked row is promoted or
replaced by generated or fallback historical art.
