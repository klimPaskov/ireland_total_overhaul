# Final focus and Parliament localisation audit

Date: 2026-08-09
Feature slug: `ireland_focus_tree`
Scope: current 150-focus source after the semantic layout/visibility pass and
the read-only Parliament decision-category header.

## Result

The current source contains exactly 150 focus IDs. Every focus has a title key
and a matching `_desc` key in
`localisation/english/ireland_l_english.yml`; missing titles: 0, missing
descriptions: 0.

The Parliament panel has 20 unique direct localisation references (23
occurrences across `text` and `pdx_tooltip` fields) in
`interface/ireland_parliament_scripted_gui.gui`. All 20 resolve to non-empty
English keys. The category binding
`ireland_settlement_government` and its `_desc` key also resolve.
`common/scripted_localisation/ireland_localisation.txt` has no missing
`localization_key` outputs (0 missing).

## Changed files and keys

Only `localisation/english/ireland_l_english.yml` was patched. The 226-focus
roster at commit `3902350` was compared with the current 150-focus roster.
Seven retired wrapper IDs had no title/description keys to remove:
`ireland_domestic_industry_review`,
`ireland_port_and_coast_audit`, `ireland_northern_contacts`,
`ireland_govern_through_dail`, `ireland_reconciliation_mandate`,
`ireland_agrarian_support_bloc`, and `ireland_territorial_reserve`.
The remaining 69 deleted IDs had stale title and description pairs; all 138
stale lines were removed:

- `ireland_amnesty_under_law` + `ireland_amnesty_under_law_desc`
- `ireland_army_serves_dail` + `ireland_army_serves_dail_desc`
- `ireland_border_observation` + `ireland_border_observation_desc`
- `ireland_cabinet_compact` + `ireland_cabinet_compact_desc`
- `ireland_cabinet_of_production` + `ireland_cabinet_of_production_desc`
- `ireland_civil_service_and_courts` + `ireland_civil_service_and_courts_desc`
- `ireland_civil_war_memory` + `ireland_civil_war_memory_desc`
- `ireland_convention_of_commands` + `ireland_convention_of_commands_desc`
- `ireland_convergence_order_capstone` + `ireland_convergence_order_capstone_desc`
- `ireland_corporate_estates` + `ireland_corporate_estates_desc`
- `ireland_corporate_gaelic_nation` + `ireland_corporate_gaelic_nation_desc`
- `ireland_council_government_rejected` + `ireland_council_government_rejected_desc`
- `ireland_crown_province_convergence` + `ireland_crown_province_convergence_desc`
- `ireland_cultural_service` + `ireland_cultural_service_desc`
- `ireland_culture_completion` + `ireland_culture_completion_desc`
- `ireland_dail_supremacy_clause` + `ireland_dail_supremacy_clause_desc`
- `ireland_demobilisation_charter` + `ireland_demobilisation_charter_desc`
- `ireland_diaspora_exchange` + `ireland_diaspora_exchange_desc`
- `ireland_distinguish_prisoners` + `ireland_distinguish_prisoners_desc`
- `ireland_emergency_accounting` + `ireland_emergency_accounting_desc`
- `ireland_extra_parliamentary_transition` + `ireland_extra_parliamentary_transition_desc`
- `ireland_face_civil_war_record` + `ireland_face_civil_war_record_desc`
- `ireland_federal_convention` + `ireland_federal_convention_desc`
- `ireland_fivefold_obligation` + `ireland_fivefold_obligation_desc`
- `ireland_foreign_postwar_review` + `ireland_foreign_postwar_review_desc`
- `ireland_general_election_campaign` + `ireland_general_election_campaign_desc`
- `ireland_government_from_opposition` + `ireland_government_from_opposition_desc`
- `ireland_high_king_convention` + `ireland_high_king_convention_desc`
- `ireland_institutional_survey` + `ireland_institutional_survey_desc`
- `ireland_labour_industrial_discipline` + `ireland_labour_industrial_discipline_desc`
- `ireland_labour_social_law` + `ireland_labour_social_law_desc`
- `ireland_language_cells` + `ireland_language_cells_desc`
- `ireland_language_institutions` + `ireland_language_institutions_desc`
- `ireland_language_service` + `ireland_language_service_desc`
- `ireland_minority_guarantees` + `ireland_minority_guarantees_desc`
- `ireland_neutrality_by_irish_decision` + `ireland_neutrality_by_irish_decision_desc`
- `ireland_northern_recovery_bridge` + `ireland_northern_recovery_bridge_desc`
- `ireland_northern_regional_review` + `ireland_northern_regional_review_desc`
- `ireland_otherworld_convergence` + `ireland_otherworld_convergence_desc`
- `ireland_otherworld_guardians` + `ireland_otherworld_guardians_desc`
- `ireland_otherworld_statecraft` + `ireland_otherworld_statecraft_desc`
- `ireland_otherworld_witnesses` + `ireland_otherworld_witnesses_desc`
- `ireland_party_conference` + `ireland_party_conference_desc`
- `ireland_party_of_government` + `ireland_party_of_government_desc`
- `ireland_plebiscite_campaign` + `ireland_plebiscite_campaign_desc`
- `ireland_plebiscite_mandate` + `ireland_plebiscite_mandate_desc`
- `ireland_presidential_settlement` + `ireland_presidential_settlement_desc`
- `ireland_producer_councils` + `ireland_producer_councils_desc`
- `ireland_professional_defence_council` + `ireland_professional_defence_council_desc`
- `ireland_reconstruction_mandate` + `ireland_reconstruction_mandate_desc`
- `ireland_regional_participation` + `ireland_regional_participation_desc`
- `ireland_regional_thresholds` + `ireland_regional_thresholds_desc`
- `ireland_republic_in_districts` + `ireland_republic_in_districts_desc`
- `ireland_republican_legitimacy` + `ireland_republican_legitimacy_desc`
- `ireland_republican_veterans` + `ireland_republican_veterans_desc`
- `ireland_restore_parliamentary_confidence` + `ireland_restore_parliamentary_confidence_desc`
- `ireland_rural_compensation` + `ireland_rural_compensation_desc`
- `ireland_rural_producer_compact` + `ireland_rural_producer_compact_desc`
- `ireland_seanad_panels` + `ireland_seanad_panels_desc`
- `ireland_secure_plebiscite_mandate` + `ireland_secure_plebiscite_mandate_desc`
- `ireland_service_state` + `ireland_service_state_desc`
- `ireland_site_stewardship` + `ireland_site_stewardship_desc`
- `ireland_sovereignty_mandate` + `ireland_sovereignty_mandate_desc`
- `ireland_state_we_built` + `ireland_state_we_built_desc`
- `ireland_support_without_surrender` + `ireland_support_without_surrender_desc`
- `ireland_ulster_rule` + `ireland_ulster_rule_desc`
- `ireland_union_local_mandate` + `ireland_union_local_mandate_desc`
- `ireland_unwind_exceptional_state` + `ireland_unwind_exceptional_state_desc`
- `ireland_veteran_employer_league` + `ireland_veteran_employer_league_desc`

Before removal, these stale keys were not referenced as localisation,
tooltip, scripted-localisation, or GUI text by the current gameplay source.
After removal, no deleted focus ID from the 226-focus baseline has a surviving
title or description key.

## Required audit lists

### Missing keys

None for current focus titles/descriptions, the settlement-government category,
the Parliament GUI, or scripted-localisation output keys.

### Duplicate keys

None across `ireland_l_english.yml` and
`ireland_game_rules_l_english.yml`.

### Scripted-localisation issues

None. Every `localization_key = ...` in
`common/scripted_localisation/ireland_localisation.txt` resolves. The
Parliament panel intentionally uses direct dynamic English keys rather than a
new defined-text contract.

### Dynamic text opportunities

The current Parliament strings already expose live Dáil/Seanad values,
majority thresholds, chamber composition, and red/green power-state meaning.
No additional dynamic localisation is required for this pass. The four power
labels and their tooltips describe the visible result of the corresponding
native decisions; costs remain owned by those decisions.

### Cross-surface mismatch notes

None found. `ireland_settlement_government` binds
`ireland_parliament_decision_ui` to
`ireland_parliament_decision_ui_window`; every GUI text/tooltip key is
present, and the 150 current focus IDs have matching title/description pairs.
The seven retired wrapper IDs documented in the 2026-08-09 completion report
remain compatibility flags/assets only and do not retain focus localisation.

### File encoding concerns

None. Both English localisation files retain a UTF-8 BOM
(`EF BB BF`) and decode as strict UTF-8. No `:0` keys were found.

## Validation

Task-specific checks run after the patch:

- current focus ID extraction: 150 IDs; title gaps 0; description gaps 0;
- Parliament GUI direct references: 20 unique keys / 23 occurrences; missing 0;
- scripted-localisation `localization_key` outputs: missing 0;
- duplicate-key scan across both English yml files: 0;
- stale-focus comparison against the 226-focus `3902350` baseline: 0
  surviving deleted-focus title/description keys;
- BOM and strict UTF-8 checks: both files OK.

Live HOI4 launch, runtime GUI rendering, and engine-log checks were skipped;
the parent completion report already carries the linked offline focus/GUI
inspection artifacts, and this handoff is a static localisation-only pass.

## Unresolved wording decisions

None. No gameplay text, costs, requirements, or route meaning changed.

## Simplifications, omissions, and blockers

None in the localisation/UI audit scope. No fallback text or replacement
mechanic was introduced.
