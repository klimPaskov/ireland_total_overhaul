# Ireland P0 family-band layout final handoff

Status: superseded by
`ireland_country_package_family_lane_reflow_completion_2026-08-14.md`.
This file preserves the reversible pre-reflow coordinate table and is not the
current layout contract. Keep it for rollback and audit evidence.

Historical snapshot state: in progress; this file preserves the reversible baseline table before any source edit.

## Scope

Only `common/national_focus/ireland_focus_tree.txt` layout/prerequisite fields are in scope. Rewards, availability gates, `allow_branch` locks, identifiers, localisation, icons, and AI logic must remain unchanged except for the explicitly required visible prerequisite fields.

## Reversible baseline coordinate table

The committed source baseline contains 218 focus IDs and 226 prerequisite connectors. Coordinates and visible prerequisite edges below are the complete five-family programme graph plus the five public commitments and named P0 detour nodes.

| family / focus | baseline `(x,y)` | visible prerequisite(s) |
| --- | ---: | --- |
| `ireland_republican_government` | `(-16,4)` | `ireland_constitutional_draft` |
| `ireland_de_valera_stewardship` | `(-16,5)` | `ireland_republican_government` |
| `ireland_constitutional_stewardship` | `(-16,6)` | `ireland_de_valera_stewardship` |
| `ireland_de_valera_reconciliation` | `(-14,5)` | `ireland_republican_government` |
| `ireland_de_valera_reconciliation_capstone` | `(-14,6)` | `ireland_de_valera_reconciliation` |
| `ireland_emergency_direction` | `(-20,10)` | `ireland_emergency_opening` |
| `ireland_statutory_emergency` | `(-20,11)` | `ireland_emergency_direction` |
| `ireland_emergency_review` | `(-20,12)` | `ireland_statutory_emergency` |
| `ireland_emergency_repeal` | `(-20,13)` | `ireland_emergency_review` |
| `ireland_de_valera_emergency_capstone` | `(-20,14)` | `ireland_emergency_repeal` |
| `ireland_lemass_developmental` | `(-18,9)` | `ireland_active_neutrality` |
| `ireland_dail_nomination` | `(-18,10)` | `ireland_lemass_developmental` |
| `ireland_lemass_developmental_capstone` | `(-18,11)` | `ireland_dail_nomination` |
| `ireland_constitutional_opposition` | `(-14,8)` | `ireland_treaty_port_transfer` |
| `ireland_close_oduffy_chapter` | `(-14,9)` | `ireland_constitutional_opposition` |
| `ireland_cosgrave_institutional` | `(-16,10)` | `ireland_close_oduffy_chapter` |
| `ireland_security_under_law` | `(-16,11)` | `ireland_cosgrave_institutional` |
| `ireland_cosgrave_capstone` | `(-16,12)` | `ireland_security_under_law` |
| `ireland_mulcahy_succession` | `(-14,10)` | `ireland_close_oduffy_chapter` |
| `ireland_mulcahy_capstone` | `(-14,11)` | `ireland_mulcahy_succession` |
| `ireland_costello_coalition` | `(-12,10)` | `ireland_close_oduffy_chapter` |
| `ireland_written_coalition_charter` | `(-12,11)` | `ireland_costello_coalition` |
| `ireland_costello_capstone` | `(-12,12)` | `ireland_written_coalition_charter` |
| `ireland_dillon_public_dissent` | `(-10,10)` | `ireland_close_oduffy_chapter` |
| `ireland_dillon_intervention_caucus` | `(-10,11)` | `ireland_dillon_public_dissent` |
| `ireland_dillon_war_assent` | `(-10,12)` | `ireland_dillon_intervention_caucus` |
| `ireland_congress_reform_bridge` | `(-12,3)` | `ireland_church_labour_consultation` |
| `ireland_organise_congress` | `(-12,4)` | `ireland_congress_reform_bridge` |
| `ireland_congress_plural_republic` | `(-12,5)` | `ireland_organise_congress` |
| `ireland_congress_vanguard_cell` | `(-10,5)` | `ireland_organise_congress` |
| `ireland_congress_plural_capstone` | `(-12,6)` | `ireland_congress_plural_republic` |
| `ireland_congress_vanguard_capstone` | `(-10,6)` | `ireland_congress_vanguard_cell` |
| `ireland_vocational_constitution` | `(-8,7)` | *(none; availability carries route gates)* |
| `ireland_vocational_constitution_capstone` | `(-8,8)` | `ireland_vocational_constitution` |
| `ireland_oduffy_network_revival` | `(-6,10)` | `ireland_close_oduffy_chapter` |
| `ireland_oduffy_personal_command` | `(-8,11)` | `ireland_oduffy_network_revival` |
| `ireland_army_acceptance` | `(-6,11)` | `ireland_oduffy_network_revival` |
| `ireland_corporate_order` | `(-6,12)` | `ireland_army_acceptance` |
| `ireland_oduffy_personal_capstone` | `(-8,12)` | `ireland_oduffy_personal_command` |
| `ireland_oduffy_corporate_capstone` | `(-6,13)` | `ireland_corporate_order` |
| `ireland_clerical_failure_bridge` | `(-10,3)` | `ireland_church_labour_consultation` |
| `ireland_clerical_guardianship` | `(-8,4)` | `ireland_clerical_failure_bridge` |
| `ireland_producer_constitution` | `(-8,5)` | `ireland_clerical_guardianship` |
| `ireland_clerical_route_capstone` | `(-8,6)` | `ireland_producer_constitution` |
| `ireland_high_king_evidence_gate` | `(-4,4)` | `ireland_cultural_evidence_ledger` |
| `ireland_elective_crown` | `(-4,5)` | `ireland_high_king_evidence_gate` |
| `ireland_guardian_crown` | `(-2,5)` | `ireland_high_king_evidence_gate` |
| `ireland_crown_powers_charter` | `(-2,6)` | `ireland_elective_crown`, `ireland_guardian_crown` |
| `ireland_high_king_capstone` | `(-2,7)` | `ireland_crown_powers_charter` |
| `ireland_otherworld_investigation` | `(-6,4)` | `ireland_cultural_evidence_ledger` |
| `ireland_otherworld_evidence_ledger` | `(-6,5)` | `ireland_otherworld_investigation` |
| `ireland_compact_with_otherworld` | `(-6,6)` | `ireland_otherworld_evidence_ledger` |
| `ireland_containment_protocol` | `(-4,6)` | `ireland_otherworld_evidence_ledger` |
| `ireland_dominion_claim` | `(-6,7)` | `ireland_compact_with_otherworld`, `ireland_containment_protocol` |
| `ireland_otherworld_capstone` | `(-6,8)` | `ireland_dominion_claim` |
| `ireland_republican_ministries` | `(-40,0)` | *(none; family flag only)* |
| `ireland_rights_under_emergency` | `(-42,1)` | `ireland_republican_ministries` |
| `ireland_local_government_compact` | `(-40,1)` | `ireland_republican_ministries` |
| `ireland_democratic_security_league` | `(-38,1)` | `ireland_republican_ministries` |
| `ireland_democratic_reconstruction` | `(-41,2)` | `ireland_rights_under_emergency`, `ireland_local_government_compact` |
| `ireland_constitutional_service_cabinet` | `(-41,3)` | `ireland_democratic_reconstruction` |
| `ireland_vanguard_organisers` | `(-34,0)` | *(none; family flag only)* |
| `ireland_trade_union_congress` | `(-36,1)` | `ireland_vanguard_organisers` |
| `ireland_workers_smallholders_programme` | `(-34,1)` | `ireland_vanguard_organisers` |
| `ireland_republican_self_defence` | `(-32,1)` | `ireland_vanguard_organisers` |
| `ireland_workers_reconstruction_board` | `(-34,2)` | `ireland_trade_union_congress`, `ireland_republican_self_defence` |
| `ireland_congress_workers_cabinet` | `(-34,3)` | `ireland_workers_reconstruction_board` |
| `ireland_veterans_command_council` | `(-40,5)` | *(none; family flag only)* |
| `ireland_veteran_employment_corps` | `(-42,6)` | `ireland_veterans_command_council` |
| `ireland_national_corporate_chamber` | `(-40,6)` | `ireland_veterans_command_council` |
| `ireland_motorised_command_contracts` | `(-38,6)` | `ireland_veterans_command_council` |
| `ireland_personal_command_or_corporate_state` | `(-39,7)` | `ireland_national_corporate_chamber`, `ireland_motorised_command_contracts` |
| `ireland_emergency_directorate` | `(-39,8)` | `ireland_personal_command_or_corporate_state` |
| `ireland_creditor_cabinet` | `(-34,5)` | *(none; family flag only)* |
| `ireland_restricted_estate_franchise` | `(-36,6)` | `ireland_creditor_cabinet` |
| `ireland_industrial_syndicates` | `(-34,6)` | `ireland_creditor_cabinet` |
| `ireland_rural_producer_boards` | `(-32,6)` | `ireland_creditor_cabinet` |
| `ireland_executive_estates` | `(-35,7)` | `ireland_restricted_estate_franchise`, `ireland_industrial_syndicates` |
| `ireland_producer_directorate` | `(-33,7)` | `ireland_industrial_syndicates`, `ireland_rural_producer_boards` |
| `ireland_managed_social_peace` | `(-34,8)` | `ireland_executive_estates`, `ireland_producer_directorate` |
| `ireland_estates_and_professions_council` | `(-34,9)` | `ireland_managed_social_peace` |
| `ireland_claimants_convention` | `(-40,11)` | *(none; family flag only)* |
| `ireland_provincial_compact` | `(-42,12)` | `ireland_claimants_convention` |
| `ireland_brehon_law_commission` | `(-38,12)` | `ireland_claimants_convention` |
| `ireland_crown_defence_council` | `(-40,13)` | `ireland_provincial_compact`, `ireland_brehon_law_commission` |
| `ireland_household_council` | `(-40,14)` | `ireland_crown_defence_council` |

The table is intentionally written before the source reflow. If the candidate cannot meet the zero-defect inspection contract, restore the source byte-for-byte from the committed revision and retain this baseline evidence.
