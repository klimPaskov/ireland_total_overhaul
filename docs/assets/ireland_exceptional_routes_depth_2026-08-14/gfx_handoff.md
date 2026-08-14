# Copy-ready GFX and event-picture handoff

Parent-owned wiring only: this package deliberately does not edit any `.gfx`, event, focus, decision, mission, localisation, or thumbnail file. All texture paths below are final and all sprite identifiers marked `PROPOSED` are stable suggestions where the accepted plan supplied an ID but no existing registration.

## Focus sprite registrations — 38 wired

Add these `spriteType` entries to the project’s focus sprite `.gfx` file. Every entry is `PROPOSED` as a sprite name; the exact focus ID and DDS filename are plan-owned.

```text
spriteType = { name = GFX_focus_ireland_crown_in_party_hands texturefile = "gfx/interface/goals/ireland/goal_ireland_crown_in_party_hands.dds" }
spriteType = { name = GFX_focus_ireland_break_the_captive_crown texturefile = "gfx/interface/goals/ireland/goal_ireland_break_the_captive_crown.dds" }
spriteType = { name = GFX_focus_ireland_the_captive_throne texturefile = "gfx/interface/goals/ireland/goal_ireland_the_captive_throne.dds" }
spriteType = { name = GFX_focus_ireland_the_stone_gives_its_answer texturefile = "gfx/interface/goals/ireland/goal_ireland_the_stone_gives_its_answer.dds" }
spriteType = { name = GFX_focus_ireland_geasa_of_the_crown texturefile = "gfx/interface/goals/ireland/goal_ireland_geasa_of_the_crown.dds" }
spriteType = { name = GFX_focus_ireland_high_kingdom_of_the_living_land texturefile = "gfx/interface/goals/ireland/goal_ireland_high_kingdom_of_the_living_land.dds" }
spriteType = { name = GFX_focus_ireland_unbounded_sacred_rule texturefile = "gfx/interface/goals/ireland/goal_ireland_unbounded_sacred_rule.dds" }
spriteType = { name = GFX_focus_ireland_provincial_powers_convention texturefile = "gfx/interface/goals/ireland/goal_ireland_provincial_powers_convention.dds" }
spriteType = { name = GFX_focus_ireland_fund_the_federal_compact texturefile = "gfx/interface/goals/ireland/goal_ireland_fund_the_federal_compact.dds" }
spriteType = { name = GFX_focus_ireland_four_provinces_and_an_empty_chair texturefile = "gfx/interface/goals/ireland/goal_ireland_four_provinces_and_an_empty_chair.dds" }
spriteType = { name = GFX_focus_ireland_council_by_provincial_mandate texturefile = "gfx/interface/goals/ireland/goal_ireland_council_by_provincial_mandate.dds" }
spriteType = { name = GFX_focus_ireland_irish_confederation texturefile = "gfx/interface/goals/ireland/goal_ireland_irish_confederation.dds" }
spriteType = { name = GFX_focus_ireland_five_sovereign_orders texturefile = "gfx/interface/goals/ireland/goal_ireland_five_sovereign_orders.dds" }
spriteType = { name = GFX_focus_ireland_pentarchy_of_ireland texturefile = "gfx/interface/goals/ireland/goal_ireland_pentarchy_of_ireland.dds" }
spriteType = { name = GFX_focus_ireland_the_fifth_province texturefile = "gfx/interface/goals/ireland/goal_ireland_the_fifth_province.dds" }
spriteType = { name = GFX_focus_ireland_rival_irelands texturefile = "gfx/interface/goals/ireland/goal_ireland_rival_irelands.dds" }
spriteType = { name = GFX_focus_ireland_turn_contact_into_power texturefile = "gfx/interface/goals/ireland/goal_ireland_turn_contact_into_power.dds" }
spriteType = { name = GFX_focus_ireland_compel_an_answer texturefile = "gfx/interface/goals/ireland/goal_ireland_compel_an_answer.dds" }
spriteType = { name = GFX_focus_ireland_the_state_owns_the_mounds texturefile = "gfx/interface/goals/ireland/goal_ireland_the_state_owns_the_mounds.dds" }
spriteType = { name = GFX_focus_ireland_a_breach_made_deliberately texturefile = "gfx/interface/goals/ireland/goal_ireland_a_breach_made_deliberately.dds" }
spriteType = { name = GFX_focus_ireland_the_rights_of_local_guardians texturefile = "gfx/interface/goals/ireland/goal_ireland_the_rights_of_local_guardians.dds" }
spriteType = { name = GFX_focus_ireland_a_law_for_two_orders texturefile = "gfx/interface/goals/ireland/goal_ireland_a_law_for_two_orders.dds" }
spriteType = { name = GFX_focus_ireland_recognise_the_elder_claim texturefile = "gfx/interface/goals/ireland/goal_ireland_recognise_the_elder_claim.dds" }
spriteType = { name = GFX_focus_ireland_the_courts_beneath_the_hills texturefile = "gfx/interface/goals/ireland/goal_ireland_the_courts_beneath_the_hills.dds" }
spriteType = { name = GFX_focus_ireland_a_government_under_the_mounds texturefile = "gfx/interface/goals/ireland/goal_ireland_a_government_under_the_mounds.dds" }
spriteType = { name = GFX_focus_ireland_the_hounds_are_heard_again texturefile = "gfx/interface/goals/ireland/goal_ireland_the_hounds_are_heard_again.dds" }
spriteType = { name = GFX_focus_ireland_muster_a_modern_fian texturefile = "gfx/interface/goals/ireland/goal_ireland_muster_a_modern_fian.dds" }
spriteType = { name = GFX_focus_ireland_no_host_without_equipment texturefile = "gfx/interface/goals/ireland/goal_ireland_no_host_without_equipment.dds" }
spriteType = { name = GFX_focus_ireland_guardians_of_two_irelands texturefile = "gfx/interface/goals/ireland/goal_ireland_guardians_of_two_irelands.dds" }
spriteType = { name = GFX_focus_ireland_regional_otherworld_courts texturefile = "gfx/interface/goals/ireland/goal_ireland_regional_otherworld_courts.dds" }
spriteType = { name = GFX_focus_ireland_no_single_story_rules_them_all texturefile = "gfx/interface/goals/ireland/goal_ireland_no_single_story_rules_them_all.dds" }
spriteType = { name = GFX_focus_ireland_the_emergency_must_end texturefile = "gfx/interface/goals/ireland/goal_ireland_the_emergency_must_end.dds" }
spriteType = { name = GFX_focus_ireland_human_sovereignty_restored texturefile = "gfx/interface/goals/ireland/goal_ireland_human_sovereignty_restored.dds" }
spriteType = { name = GFX_focus_ireland_the_sealed_state texturefile = "gfx/interface/goals/ireland/goal_ireland_the_sealed_state.dds" }
spriteType = { name = GFX_focus_ireland_high_king_of_two_irelands texturefile = "gfx/interface/goals/ireland/goal_ireland_high_king_of_two_irelands.dds" }
spriteType = { name = GFX_focus_ireland_crown_and_five_provinces texturefile = "gfx/interface/goals/ireland/goal_ireland_crown_and_five_provinces.dds" }
spriteType = { name = GFX_focus_ireland_five_courts_of_the_otherworld texturefile = "gfx/interface/goals/ireland/goal_ireland_five_courts_of_the_otherworld.dds" }
spriteType = { name = GFX_focus_ireland_fivefold_high_kingdom_of_two_irelands texturefile = "gfx/interface/goals/ireland/goal_ireland_fivefold_high_kingdom_of_two_irelands.dds" }
```

Use the repository’s existing focus shine/disabled-state convention with these icons; no per-focus shine or animated frame package was required by the accepted plan.

## Decision and mission sprite registrations — 22 wired

The following paths are registered in `interface/ireland_icons.gfx` and used by the matching decision and mission definitions.

```text
spriteType = { name = GFX_decision_ireland_action_audit_the_royal_household texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_audit_the_royal_household.dds" }
spriteType = { name = GFX_decision_ireland_action_break_the_party_crown texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_break_the_party_crown.dds" }
spriteType = { name = GFX_decision_ireland_action_accept_a_royal_geis texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_accept_a_royal_geis.dds" }
spriteType = { name = GFX_decision_ireland_action_negotiate_a_provincial_budget texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_negotiate_a_provincial_budget.dds" }
spriteType = { name = GFX_decision_ireland_action_reserve_the_ulster_chair texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_reserve_the_ulster_chair.dds" }
spriteType = { name = GFX_decision_ireland_action_call_a_confederal_council texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_call_a_confederal_council.dds" }
spriteType = { name = GFX_decision_ireland_action_arbitrate_a_provincial_veto texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_arbitrate_a_provincial_veto.dds" }
spriteType = { name = GFX_decision_ireland_action_record_an_otherworld_obligation texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_record_an_otherworld_obligation.dds" }
spriteType = { name = GFX_decision_ireland_action_hear_a_regional_court texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_hear_a_regional_court.dds" }
spriteType = { name = GFX_decision_ireland_action_restitute_a_seized_site texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_restitute_a_seized_site.dds" }
spriteType = { name = GFX_decision_ireland_action_narrow_the_containment_perimeter texturefile = "gfx/interface/decisions/ireland/exceptional_routes/decision_ireland_action_narrow_the_containment_perimeter.dds" }
spriteType = { name = GFX_mission_ireland_mission_complete_the_royal_circuit texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_complete_the_royal_circuit.dds" }
spriteType = { name = GFX_mission_ireland_mission_break_the_party_crown texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_break_the_party_crown.dds" }
spriteType = { name = GFX_mission_ireland_mission_fund_the_common_compact texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_fund_the_common_compact.dds" }
spriteType = { name = GFX_mission_ireland_mission_keep_the_fifth_seat_open texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_keep_the_fifth_seat_open.dds" }
spriteType = { name = GFX_mission_ireland_mission_prevent_rival_irelands texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_prevent_rival_irelands.dds" }
spriteType = { name = GFX_mission_ireland_mission_equip_a_fian_company texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_equip_a_fian_company.dds" }
spriteType = { name = GFX_mission_ireland_mission_keep_the_veil_at_five_sites texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_keep_the_veil_at_five_sites.dds" }
spriteType = { name = GFX_mission_ireland_mission_repair_the_broken_compact texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_repair_the_broken_compact.dds" }
spriteType = { name = GFX_mission_ireland_mission_reconcile_regional_compacts texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_reconcile_regional_compacts.dds" }
spriteType = { name = GFX_mission_ireland_mission_extract_from_a_protected_site texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_extract_from_a_protected_site.dds" }
spriteType = { name = GFX_mission_ireland_mission_survive_the_first_convergence_review texturefile = "gfx/interface/decisions/ireland/exceptional_routes/mission_ireland_mission_survive_the_first_convergence_review.dds" }
```

Decision-category registrations are not needed for this package. Reuse the five existing category sprites named by the plan: `ireland_settlement_government`, `ireland_cultural_archival`, `ireland_readiness`, `ireland_occupation_integration`, and `ireland_regional_external`.

## Event picture registrations and routing — 438 through 460

Add one picture sprite per event, then route each event’s `picture =` key to the matching sprite below. Every row is a distinct DDS; none is a fallback alias.

```text
spriteType = { name = GFX_report_event_ireland_exceptional_438 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_438.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_439 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_439.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_440 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_440.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_441 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_441.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_442 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_442.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_443 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_443.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_444 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_444.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_445 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_445.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_446 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_446.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_447 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_447.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_448 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_448.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_449 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_449.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_450 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_450.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_451 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_451.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_452 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_452.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_453 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_453.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_454 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_454.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_455 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_455.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_456 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_456.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_457 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_457.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_458 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_458.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_459 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_459.dds" }
spriteType = { name = GFX_report_event_ireland_exceptional_460 texturefile = "gfx/event_pictures/ireland_exceptional_routes/report_event_ireland_exceptional_460.dds" }
```

Event routing map:

```text
438 -> GFX_report_event_ireland_exceptional_438
439 -> GFX_report_event_ireland_exceptional_439
440 -> GFX_report_event_ireland_exceptional_440
441 -> GFX_report_event_ireland_exceptional_441
442 -> GFX_report_event_ireland_exceptional_442
443 -> GFX_report_event_ireland_exceptional_443
444 -> GFX_report_event_ireland_exceptional_444
445 -> GFX_report_event_ireland_exceptional_445
446 -> GFX_report_event_ireland_exceptional_446
447 -> GFX_report_event_ireland_exceptional_447
448 -> GFX_report_event_ireland_exceptional_448
449 -> GFX_report_event_ireland_exceptional_449
450 -> GFX_report_event_ireland_exceptional_450
451 -> GFX_report_event_ireland_exceptional_451
452 -> GFX_report_event_ireland_exceptional_452
453 -> GFX_report_event_ireland_exceptional_453
454 -> GFX_report_event_ireland_exceptional_454
455 -> GFX_report_event_ireland_exceptional_455
456 -> GFX_report_event_ireland_exceptional_456
457 -> GFX_report_event_ireland_exceptional_457
458 -> GFX_report_event_ireland_exceptional_458
459 -> GFX_report_event_ireland_exceptional_459
460 -> GFX_report_event_ireland_exceptional_460
```

## Cosmetic flag filenames

The plan’s exact identity tokens are already present as final files; no `.gfx` sprite registration is required for flag texture discovery. Country flags use uncompressed 32-bit TGA files. Parent wiring must connect each cosmetic identity to these normal/medium/small files:

```text
IRE_IRELAND_CAPTIVE_THRONE.tga
IRE_IRELAND_CONFEDERATION.tga
IRE_IRELAND_FIFTH_PROVINCE.tga
IRE_IRELAND_RIVAL_PROVINCES.tga
IRE_IRELAND_TUATHA_SOVEREIGNTY.tga
IRE_IRELAND_FIANNA_GUARDIANSHIP.tga
IRE_IRELAND_SEALED_STATE.tga
IRE_IRELAND_CROWN_AND_PROVINCES.tga
IRE_IRELAND_HIGH_KING_TWO_IRELANDS.tga
IRE_IRELAND_FIVE_COURTS_OTHERWORLD.tga
```

Normal: `gfx/flags/<identity>.tga`; medium: `gfx/flags/medium/<identity>.tga`; small: `gfx/flags/small/<identity>.tga`.

## Validation and remaining wiring

- 38 focus source/processed/final DDS files: 94x86, transparent.
- 11 decision source/processed/final DDS files: 32x32, transparent.
- 11 mission source/processed/final DDS files: 32x32, transparent.
- 23 report source/processed/final DDS files: 210x176, with the processor-prescribed transparent tilted-card corners.
- 10 flag sources, 30 processed PNGs, and 30 final uncompressed 32-bit TGA files: 82x52 normal, 41x26 medium, 10x7 small, opaque.
- Contact sheets exist for focus, decisions, missions, reports, and normal flags.
- No item is blocked, missing, or a placeholder/fallback. No new category icon or animation was required by the accepted plan. Parent still needs to register the 38 focus sprites, 22 decision/mission sprites, 23 report sprites, route event `picture` keys, and connect cosmetic flag identities.
