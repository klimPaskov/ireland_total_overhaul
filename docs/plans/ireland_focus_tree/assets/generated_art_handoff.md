# Ireland generated-art GFX handoff

Owned source package: `assets/ireland_focus_tree/generated/`. Runtime final DDS files are shipped under `gfx/`; route flag TGAs use the standard `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` roots. The generated package remains staging/provenance material.

## Coverage

| Package | Count | Final output | Suggested surface | Static fallback |
| --- | ---: | --- | --- | --- |
| Generated event/news allocations | 51 | `gfx/event_pictures/ireland/` | report/news event-picture `.gfx` slots | own static DDS; no animation dependency |
| Generated route flag identities | 18 × 3 sizes | `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/` | exact `IRE_SLOPX_*` cosmetic-tag filenames | size siblings; historical tricolour when inactive |
| Generated route/faction emblems | 8 × 2 sizes | `gfx/interface/ireland/emblems/` | selected faction/route emblem `.gfx` surface | large/small static siblings |

The ledger split is preserved: 69 sourced + 51 generated = 120 planned event/news images. The 51 generated source PNGs are exact; four retained alternatives are outside the allocation under `contact_sheets/alternatives/`.

## Event/news sprite handoff

| Sprite | Family | Final DDS | Target | Suggested `.gfx` surface | Static fallback |
| --- | --- | --- | --- | --- | --- |
| ireland_news_army_council_broadcast | generated_alternate_news | `gfx/event_pictures/ireland/ireland_news_army_council_broadcast.dds` | 397x153 | news event picture .gfx slot | own static DDS |
| ireland_news_convergence_three_orders | generated_alternate_news | `gfx/event_pictures/ireland/ireland_news_convergence_three_orders.dds` | 397x153 | news event picture .gfx slot | own static DDS |
| ireland_news_five_provinces_compact | generated_alternate_news | `gfx/event_pictures/ireland/ireland_news_five_provinces_compact.dds` | 397x153 | news event picture .gfx slot | own static DDS |
| ireland_news_high_king_crowned_tara | generated_alternate_news | `gfx/event_pictures/ireland/ireland_news_high_king_crowned_tara.dds` | 397x153 | news event picture .gfx slot | own static DDS |
| ireland_news_northern_unity_settlement | generated_alternate_news | `gfx/event_pictures/ireland/ireland_news_northern_unity_settlement.dds` | 397x153 | news event picture .gfx slot | own static DDS |
| ireland_news_otherworld_envoy_dublin | generated_alternate_news | `gfx/event_pictures/ireland/ireland_news_otherworld_envoy_dublin.dds` | 397x153 | news event picture .gfx slot | own static DDS |
| ireland_report_agrarian_producer_settlement | route_conclusion | `gfx/event_pictures/ireland/ireland_report_agrarian_producer_settlement.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_ailtiri_cultural_capture | radical_alternate_crisis_report | `gfx/event_pictures/ireland/ireland_report_ailtiri_cultural_capture.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_ailtiri_exposure | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_ailtiri_exposure.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_ailtiri_state | route_conclusion | `gfx/event_pictures/ireland/ireland_report_ailtiri_state.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_army_council_radio_seizure | radical_alternate_crisis_report | `gfx/event_pictures/ireland/ireland_report_army_council_radio_seizure.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_army_council_state | route_conclusion | `gfx/event_pictures/ireland/ireland_report_army_council_state.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_clerical_guardianship | route_conclusion | `gfx/event_pictures/ireland/ireland_report_clerical_guardianship.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_congress_plural | route_conclusion | `gfx/event_pictures/ireland/ireland_report_congress_plural.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_congress_vanguard | route_conclusion | `gfx/event_pictures/ireland/ireland_report_congress_vanguard.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_constitutional_republic_settlement | route_conclusion | `gfx/event_pictures/ireland/ireland_report_constitutional_republic_settlement.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_convergence_reveal | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_convergence_reveal.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_corporate_estate | route_conclusion | `gfx/event_pictures/ireland/ireland_report_corporate_estate.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_corporate_estate_proclamation | radical_alternate_crisis_report | `gfx/event_pictures/ireland/ireland_report_corporate_estate_proclamation.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_crown_evidence | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_crown_evidence.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_district_courts | radical_alternate_crisis_report | `gfx/event_pictures/ireland/ireland_report_district_courts.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_dominion_failure | route_conclusion | `gfx/event_pictures/ireland/ireland_report_dominion_failure.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_five_provinces_federation | route_conclusion | `gfx/event_pictures/ireland/ireland_report_five_provinces_federation.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_five_provinces_reveal | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_five_provinces_reveal.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_ailtiri_cells | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_ailtiri_cells.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_army_council | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_army_council.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_breach_aftermath | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_breach_aftermath.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_compact_stewards | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_compact_stewards.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_convergence_council | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_convergence_council.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_corporate_council | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_corporate_council.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_crown_guard | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_crown_guard.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_federal_works | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_federal_works.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_guardianship_service | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_guardianship_service.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_northern_bridge | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_northern_bridge.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_otherworld_guardians | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_otherworld_guardians.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_provincial_delegates | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_provincial_delegates.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_public_ritual | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_public_ritual.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_rebel_courier | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_rebel_courier.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_royal_circuit | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_royal_circuit.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_flavour_sealed_archive | shared_flavour_generated | `gfx/event_pictures/ireland/ireland_report_flavour_sealed_archive.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_hidden_fianna_return | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_hidden_fianna_return.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_hidden_living_land | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_hidden_living_land.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_hidden_sealed_sites | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_hidden_sealed_sites.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_high_king_constitutional | route_conclusion | `gfx/event_pictures/ireland/ireland_report_high_king_constitutional.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_ira_civil_republic | route_conclusion | `gfx/event_pictures/ireland/ireland_report_ira_civil_republic.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_oduffy_personal | route_conclusion | `gfx/event_pictures/ireland/ireland_report_oduffy_personal.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_otherworld_compact | route_conclusion | `gfx/event_pictures/ireland/ireland_report_otherworld_compact.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_otherworld_rath_breach | radical_alternate_crisis_report | `gfx/event_pictures/ireland/ireland_report_otherworld_rath_breach.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_otherworld_verification | hidden_reveal | `gfx/event_pictures/ireland/ireland_report_otherworld_verification.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_social_republic | route_conclusion | `gfx/event_pictures/ireland/ireland_report_social_republic.dds` | 210x176 | report event picture .gfx slot | own static DDS |
| ireland_report_workers_smallholders_strike | radical_alternate_crisis_report | `gfx/event_pictures/ireland/ireland_report_workers_smallholders_strike.dds` | 210x176 | report event picture .gfx slot | own static DDS |

## Route flags

The DDS paths below are presentation/review siblings only. Engine flags are
the exact 18 `IRE_SLOPX_*` TGA triplets under the standard `gfx/flags/` roots.
Their cosmetic tags are declared in
`common/countries/slopx_ireland_cosmetic.txt` and applied by the Ireland
runtime identity effect.

| Identity | Review sprite stem | Normal DDS | Medium DDS | Small DDS | Engine note |
| --- | --- | --- | --- | --- | --- |
| Army Council Ireland | `ireland_route_flag_army_council_ireland` | `gfx/interface/ireland/flags/route_flag_army_council_ireland_normal.dds` | `gfx/interface/ireland/flags/route_flag_army_council_ireland_medium.dds` | `gfx/interface/ireland/flags/route_flag_army_council_ireland_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| civil republican republic variant | `ireland_route_flag_civil_republican_republic` | `gfx/interface/ireland/flags/route_flag_civil_republican_republic_normal.dds` | `gfx/interface/ireland/flags/route_flag_civil_republican_republic_medium.dds` | `gfx/interface/ireland/flags/route_flag_civil_republican_republic_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| workers and smallholders republic | `ireland_route_flag_workers_smallholders_republic` | `gfx/interface/ireland/flags/route_flag_workers_smallholders_republic_normal.dds` | `gfx/interface/ireland/flags/route_flag_workers_smallholders_republic_medium.dds` | `gfx/interface/ireland/flags/route_flag_workers_smallholders_republic_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| workers party state | `ireland_route_flag_workers_party_state` | `gfx/interface/ireland/flags/route_flag_workers_party_state_normal.dds` | `gfx/interface/ireland/flags/route_flag_workers_party_state_medium.dds` | `gfx/interface/ireland/flags/route_flag_workers_party_state_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| O'Duffy personal state | `ireland_route_flag_oduffy_personal_state` | `gfx/interface/ireland/flags/route_flag_oduffy_personal_state_normal.dds` | `gfx/interface/ireland/flags/route_flag_oduffy_personal_state_medium.dds` | `gfx/interface/ireland/flags/route_flag_oduffy_personal_state_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| corporate estate state | `ireland_route_flag_corporate_estate_state` | `gfx/interface/ireland/flags/route_flag_corporate_estate_state_normal.dds` | `gfx/interface/ireland/flags/route_flag_corporate_estate_state_medium.dds` | `gfx/interface/ireland/flags/route_flag_corporate_estate_state_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Catholic guardianship state | `ireland_route_flag_catholic_guardianship_state` | `gfx/interface/ireland/flags/route_flag_catholic_guardianship_state_normal.dds` | `gfx/interface/ireland/flags/route_flag_catholic_guardianship_state_medium.dds` | `gfx/interface/ireland/flags/route_flag_catholic_guardianship_state_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Aiséirighe national state | `ireland_route_flag_ais_eirghe_national_state` | `gfx/interface/ireland/flags/route_flag_ais_eirghe_national_state_normal.dds` | `gfx/interface/ireland/flags/route_flag_ais_eirghe_national_state_medium.dds` | `gfx/interface/ireland/flags/route_flag_ais_eirghe_national_state_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Gaelic corporate state | `ireland_route_flag_gaelic_corporate_state` | `gfx/interface/ireland/flags/route_flag_gaelic_corporate_state_normal.dds` | `gfx/interface/ireland/flags/route_flag_gaelic_corporate_state_medium.dds` | `gfx/interface/ireland/flags/route_flag_gaelic_corporate_state_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Christian national state | `ireland_route_flag_christian_national_state` | `gfx/interface/ireland/flags/route_flag_christian_national_state_normal.dds` | `gfx/interface/ireland/flags/route_flag_christian_national_state_medium.dds` | `gfx/interface/ireland/flags/route_flag_christian_national_state_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| regional Aiséirighe directorate | `ireland_route_flag_regional_ais_eirghe_directorate` | `gfx/interface/ireland/flags/route_flag_regional_ais_eirghe_directorate_normal.dds` | `gfx/interface/ireland/flags/route_flag_regional_ais_eirghe_directorate_medium.dds` | `gfx/interface/ireland/flags/route_flag_regional_ais_eirghe_directorate_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| constitutional High Kingdom | `ireland_route_flag_constitutional_high_kingdom` | `gfx/interface/ireland/flags/route_flag_constitutional_high_kingdom_normal.dds` | `gfx/interface/ireland/flags/route_flag_constitutional_high_kingdom_medium.dds` | `gfx/interface/ireland/flags/route_flag_constitutional_high_kingdom_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| sacral High Kingdom | `ireland_route_flag_sacral_high_kingdom` | `gfx/interface/ireland/flags/route_flag_sacral_high_kingdom_normal.dds` | `gfx/interface/ireland/flags/route_flag_sacral_high_kingdom_medium.dds` | `gfx/interface/ireland/flags/route_flag_sacral_high_kingdom_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Fivefold Federation | `ireland_route_flag_fivefold_federation` | `gfx/interface/ireland/flags/route_flag_fivefold_federation_normal.dds` | `gfx/interface/ireland/flags/route_flag_fivefold_federation_medium.dds` | `gfx/interface/ireland/flags/route_flag_fivefold_federation_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Pentarchy of Five Provinces | `ireland_route_flag_pentarchy_five_provinces` | `gfx/interface/ireland/flags/route_flag_pentarchy_five_provinces_normal.dds` | `gfx/interface/ireland/flags/route_flag_pentarchy_five_provinces_medium.dds` | `gfx/interface/ireland/flags/route_flag_pentarchy_five_provinces_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Compact of Two Irelands | `ireland_route_flag_compact_two_irelands` | `gfx/interface/ireland/flags/route_flag_compact_two_irelands_normal.dds` | `gfx/interface/ireland/flags/route_flag_compact_two_irelands_medium.dds` | `gfx/interface/ireland/flags/route_flag_compact_two_irelands_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| Otherworld Dominion or Sealed Sites state | `ireland_route_flag_otherworld_dominion_sealed_sites` | `gfx/interface/ireland/flags/route_flag_otherworld_dominion_sealed_sites_normal.dds` | `gfx/interface/ireland/flags/route_flag_otherworld_dominion_sealed_sites_medium.dds` | `gfx/interface/ireland/flags/route_flag_otherworld_dominion_sealed_sites_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |
| convergence order | `ireland_route_flag_convergence_order` | `gfx/interface/ireland/flags/route_flag_convergence_order_normal.dds` | `gfx/interface/ireland/flags/route_flag_convergence_order_medium.dds` | `gfx/interface/ireland/flags/route_flag_convergence_order_small.dds` | Main agent selects route-specific/cosmetic-tag filename and wires inactive fallback to historical tricolour. |

## Faction/regional-order emblems

| Identity | Proposed sprite | Large DDS | Small DDS | Suggested `.gfx` surface | Static fallback |
| --- | --- | --- | --- | --- | --- |
| Army Council seal | `ireland_faction_emblem_army_council_seal` | `gfx/interface/ireland/emblems/faction_emblem_army_council_seal_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_army_council_seal_small.dds` | faction/route emblem `.gfx` | large/small static siblings |
| Republican Congress cooperative emblem | `ireland_faction_emblem_republican_congress_cooperative` | `gfx/interface/ireland/emblems/faction_emblem_republican_congress_cooperative_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_republican_congress_cooperative_small.dds` | faction/route emblem `.gfx` | large/small static siblings |
| Corporate Estate Order emblem | `ireland_faction_emblem_corporate_estate_order` | `gfx/interface/ireland/emblems/faction_emblem_corporate_estate_order_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_corporate_estate_order_small.dds` | faction/route emblem `.gfx` | large/small static siblings |
| Clerical-Lay Guardianship emblem | `ireland_faction_emblem_clerical_lay_guardianship` | `gfx/interface/ireland/emblems/faction_emblem_clerical_lay_guardianship_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_clerical_lay_guardianship_small.dds` | faction/route emblem `.gfx` | large/small static siblings |
| Aiséirighe Directorate emblem | `ireland_faction_emblem_ais_eirghe_directorate` | `gfx/interface/ireland/emblems/faction_emblem_ais_eirghe_directorate_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_ais_eirghe_directorate_small.dds` | faction/route emblem `.gfx` | large/small static siblings |
| High Kingdom Crown-in-Council emblem | `ireland_faction_emblem_high_kingdom_crown_council` | `gfx/interface/ireland/emblems/faction_emblem_high_kingdom_crown_council_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_high_kingdom_crown_council_small.dds` | faction/route emblem `.gfx` | large/small static siblings |
| Five Provinces federal emblem | `ireland_faction_emblem_five_provinces_federal` | `gfx/interface/ireland/emblems/faction_emblem_five_provinces_federal_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_five_provinces_federal_small.dds` | faction/route emblem `.gfx` | large/small static siblings |
| Otherworld Compact emblem | `ireland_faction_emblem_otherworld_compact` | `gfx/interface/ireland/emblems/faction_emblem_otherworld_compact_large.dds` | `gfx/interface/ireland/emblems/faction_emblem_otherworld_compact_small.dds` | faction/route emblem `.gfx` | large/small static siblings |

## Notes and blockers

- Every event/news image is fictional/alternate/symbolic/supernatural or institutional material generated with the official `$imagegen` workflow; no real person or historical document is fabricated.
- Report previews use the repository report-event processor and are `210x176` sepia-compatible RGBA cards. News previews are `397x153` black-and-white strips.
- Route flags are generated designs and are not claims about attested Irish heraldry. All 18 exact cosmetic-tag triplets are implemented in the standard engine flag roots.
- Each route flag also has a matching `final_tga/` export at normal/medium/small size with TGA image descriptor `0` (bottom-left origin) for the engine flag workflow.
- The source package itself does not edit implementation files. Parent integration registers the event/news and emblem DDS files, installs the TGA triplets, declares the cosmetic tags, and wires route identity changes.
- Retained non-allocation alternatives are under `assets/ireland_focus_tree/generated/contact_sheets/alternatives/` and are not counted in the 51.
