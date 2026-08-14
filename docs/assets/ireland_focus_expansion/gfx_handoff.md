# Ireland expansion focus icon GFX handoff

Status: wired by the parent implementation. All 42 sprite names in this
handoff are registered in `interface/ireland_icons.gfx`; the snippets below
are retained as the asset crosswalk and provenance record. The separate final
family-lane focus layout is accepted at `89ff719` in
`docs/plans/ireland_country_package/subagent_handoffs/ireland_country_package_family_lane_reflow_completion_2026-08-14.md`.

Scope: 38 focus icons plus one territorial decision category and three territorial route decision icons. This worker produced source/processed PNG, runtime DDS, manifest, and contact sheet only; no `.gfx`, gameplay, or localisation files were edited.

## Focus sprites

Registered target: existing focus sprite surface `interface/ireland_icons.gfx`:

```text
spriteType = { name = GFX_focus_ireland_aer_lingus_air_link texturefile = "gfx/interface/goals/ireland_aer_lingus_air_link.dds" }
spriteType = { name = GFX_focus_ireland_all_island_workers_republic texturefile = "gfx/interface/goals/ireland_all_island_workers_republic.dds" }
spriteType = { name = GFX_focus_ireland_atlantic_ambition texturefile = "gfx/interface/goals/ireland_atlantic_ambition.dds" }
spriteType = { name = GFX_focus_ireland_atlantic_concessions texturefile = "gfx/interface/goals/ireland_atlantic_concessions.dds" }
spriteType = { name = GFX_focus_ireland_atlantic_security_compacts texturefile = "gfx/interface/goals/ireland_atlantic_security_compacts.dds" }
spriteType = { name = GFX_focus_ireland_atlantic_settlement_concluded texturefile = "gfx/interface/goals/ireland_atlantic_settlement_concluded.dds" }
spriteType = { name = GFX_focus_ireland_authorise_reunification_instruments texturefile = "gfx/interface/goals/ireland_authorise_reunification_instruments.dds" }
spriteType = { name = GFX_focus_ireland_belfast_compact texturefile = "gfx/interface/goals/ireland_belfast_compact.dds" }
spriteType = { name = GFX_focus_ireland_blueshirt_patronage_board texturefile = "gfx/interface/goals/ireland_blueshirt_patronage_board.dds" }
spriteType = { name = GFX_focus_ireland_congress_workers_cabinet texturefile = "gfx/interface/goals/ireland_congress_workers_cabinet.dds" }
spriteType = { name = GFX_focus_ireland_constitutional_service_cabinet texturefile = "gfx/interface/goals/ireland_constitutional_service_cabinet.dds" }
spriteType = { name = GFX_focus_ireland_crown_and_province_mandate texturefile = "gfx/interface/goals/ireland_crown_and_province_mandate.dds" }
spriteType = { name = GFX_focus_ireland_customs_union_leverage texturefile = "gfx/interface/goals/ireland_customs_union_leverage.dds" }
spriteType = { name = GFX_focus_ireland_dal_riata_claim texturefile = "gfx/interface/goals/ireland_dal_riata_claim.dds" }
spriteType = { name = GFX_focus_ireland_define_the_national_question texturefile = "gfx/interface/goals/ireland_define_the_national_question.dds" }
spriteType = { name = GFX_focus_ireland_enforce_atlantic_claims texturefile = "gfx/interface/goals/ireland_enforce_atlantic_claims.dds" }
spriteType = { name = GFX_focus_ireland_esb_supply_contracts texturefile = "gfx/interface/goals/ireland_esb_supply_contracts.dds" }
spriteType = { name = GFX_focus_ireland_estates_and_professions_council texturefile = "gfx/interface/goals/ireland_estates_and_professions_council.dds" }
spriteType = { name = GFX_focus_ireland_force_the_border_question texturefile = "gfx/interface/goals/ireland_force_the_border_question.dds" }
spriteType = { name = GFX_focus_ireland_ford_cork_works_agreement texturefile = "gfx/interface/goals/ireland_ford_cork_works_agreement.dds" }
spriteType = { name = GFX_focus_ireland_gaelic_marches texturefile = "gfx/interface/goals/ireland_gaelic_marches.dds" }
spriteType = { name = GFX_focus_ireland_great_southern_railways_contract texturefile = "gfx/interface/goals/ireland_great_southern_railways_contract.dds" }
spriteType = { name = GFX_focus_ireland_harland_and_wolff_access texturefile = "gfx/interface/goals/ireland_harland_and_wolff_access.dds" }
spriteType = { name = GFX_focus_ireland_household_council texturefile = "gfx/interface/goals/ireland_household_council.dds" }
spriteType = { name = GFX_focus_ireland_integration_review_commission texturefile = "gfx/interface/goals/ireland_integration_review_commission.dds" }
spriteType = { name = GFX_focus_ireland_irish_shipping_registry texturefile = "gfx/interface/goals/ireland_irish_shipping_registry.dds" }
spriteType = { name = GFX_focus_ireland_irish_sugar_company_charter texturefile = "gfx/interface/goals/ireland_irish_sugar_company_charter.dds" }
spriteType = { name = GFX_focus_ireland_local_rights_charter texturefile = "gfx/interface/goals/ireland_local_rights_charter.dds" }
spriteType = { name = GFX_focus_ireland_northern_plebiscite_guarantees texturefile = "gfx/interface/goals/ireland_northern_plebiscite_guarantees.dds" }
spriteType = { name = GFX_focus_ireland_postwar_settlement_office texturefile = "gfx/interface/goals/ireland_postwar_settlement_office.dds" }
spriteType = { name = GFX_focus_ireland_protectorate_statutes texturefile = "gfx/interface/goals/ireland_protectorate_statutes.dds" }
spriteType = { name = GFX_focus_ireland_republics_across_the_channel texturefile = "gfx/interface/goals/ireland_republics_across_the_channel.dds" }
spriteType = { name = GFX_focus_ireland_restore_ulsters_place texturefile = "gfx/interface/goals/ireland_restore_ulsters_place.dds" }
spriteType = { name = GFX_focus_ireland_settlement_under_law texturefile = "gfx/interface/goals/ireland_settlement_under_law.dds" }
spriteType = { name = GFX_focus_ireland_steel_holdings_programme texturefile = "gfx/interface/goals/ireland_steel_holdings_programme.dds" }
spriteType = { name = GFX_focus_ireland_turf_development_board_programme texturefile = "gfx/interface/goals/ireland_turf_development_board_programme.dds" }
spriteType = { name = GFX_focus_ireland_ulster_ultimatum texturefile = "gfx/interface/goals/ireland_ulster_ultimatum.dds" }
spriteType = { name = GFX_focus_ireland_workers_reunification_campaign texturefile = "gfx/interface/goals/ireland_workers_reunification_campaign.dds" }
```

All focus sprites are 94x86. Apply the shared focus shine layer `gfx/interface/goals/shine_overlay.dds` through the existing focus-button shine mechanism; no per-icon shine texture is included.

## Territorial decisions and category

Registered decision surface: `interface/ireland_icons.gfx`.

```text
spriteType = { name = GFX_decision_category_ireland_territorial_policy texturefile = "gfx/interface/decisions/categories/ireland/ireland_territorial_policy.dds" }
spriteType = { name = GFX_decision_ireland_claim_scottish_highlands texturefile = "gfx/interface/decisions/ireland/ireland_claim_scottish_highlands.dds" }
spriteType = { name = GFX_decision_ireland_claim_wales texturefile = "gfx/interface/decisions/ireland/ireland_claim_wales.dds" }
spriteType = { name = GFX_decision_ireland_claim_cornwall texturefile = "gfx/interface/decisions/ireland/ireland_claim_cornwall.dds" }
```

- Category texture: 52x40, exact canonical decision-category native canvas.
- Route decision textures: 32x32, exact canonical decision-icon canvas.
- Decisions use their own generated source panels and are not resized focus art.

## Review evidence

- Contact sheet: `docs/assets/ireland_focus_expansion/contact_sheet.png`
- Manifest: `docs/assets/ireland_focus_expansion/manifest.md`
- Prompt log: `docs/assets/ireland_focus_expansion/prompts.md`
- All 42 records are marked `complete` and wired; no blocked or needs-review
  icons remain. The current parent registration was matched against every
  sprite name in this handoff.
