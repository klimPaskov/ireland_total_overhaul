# P0 family settlement and recovery decision-icon manifest

Feature slug: `ireland_p0_family_settlement_decision_icons`  
Asset type: generated HOI4 decision icons  
Source mode: built-in `$imagegen` generation. These are fictional/alternate-history institutional symbols and do not require real photographs or archival material.  
Generation date: 2026-08-14  
Target: 32x32 RGBA decision icon, transparent background  
Reference inspected: `.agents/skills/hoi4-feature-assets/assets/vanilla_reference/README.md`, `CATALOG.md`, and `icons/decisions/contact_sheet.png`, with individual decision references including `decision_usa_congress.png`, `decision_bra_integralism.png`, `decision_bol_establish_arica_department.png`, and `decision_generic_disband_irregulars.png`.  
Processing: alpha-aware square crop and LANCZOS resize to exact 32x32 RGBA, then `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py` using the repository's 32-bit BGRA DDS workflow.  
Scope note: no `.gfx`, gameplay, localisation, decision, GUI, or thumbnail files were edited by the asset worker.  
Runtime wiring note: the parent registered all ten sprites in
`interface/ireland_icons.gfx` as `GFX_decision_<exact decision ID>`, retaining
the `ireland_action_` segment. The shorter names from the initial draft are
historical and superseded; the DDS paths remain final.

Wiring disposition: the parent registered `GFX_decision_<exact decision ID>` for
all ten actions, retaining the `ireland_action_` segment. All ten runtime DDS
paths and sprite registrations resolve; the separate family-lane layout is
accepted at `89ff719` in the country-package completion handoff and is not
replaced by this asset manifest.

| Family / surface | Exact decision ID | Source PNG | Processed PNG | Runtime DDS | Registered sprite | Target / status |
| --- | --- | --- | --- | --- | --- | --- |
| Democratic settlement | `ireland_action_ratify_the_postwar_republic` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_ratify_the_postwar_republic_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_ratify_the_postwar_republic.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_ratify_the_postwar_republic.dds` | `GFX_decision_ireland_action_ratify_the_postwar_republic` | 32x32 RGBA; wired |
| Congress settlement | `ireland_action_civilianise_the_workers_congress` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_civilianise_the_workers_congress_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_civilianise_the_workers_congress.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_civilianise_the_workers_congress.dds` | `GFX_decision_ireland_action_civilianise_the_workers_congress` | 32x32 RGBA; wired |
| Blueshirt settlement | `ireland_action_place_the_directorate_under_statute` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_place_the_directorate_under_statute_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_place_the_directorate_under_statute.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_place_the_directorate_under_statute.dds` | `GFX_decision_ireland_action_place_the_directorate_under_statute` | 32x32 RGBA; wired |
| Producer-estate settlement | `ireland_action_convert_contracts_to_reconstruction_credit` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_convert_contracts_to_reconstruction_credit_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_convert_contracts_to_reconstruction_credit.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_convert_contracts_to_reconstruction_credit.dds` | `GFX_decision_ireland_action_convert_contracts_to_reconstruction_credit` | 32x32 RGBA; wired |
| Restoration settlement | `ireland_action_define_the_postwar_crown` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_define_the_postwar_crown_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_define_the_postwar_crown.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_define_the_postwar_crown.dds` | `GFX_decision_ireland_action_define_the_postwar_crown` | 32x32 RGBA; wired |
| Democratic recovery | `ireland_action_reconstitute_the_postwar_coalition` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_reconstitute_the_postwar_coalition_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_reconstitute_the_postwar_coalition.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_reconstitute_the_postwar_coalition.dds` | `GFX_decision_ireland_action_reconstitute_the_postwar_coalition` | 32x32 RGBA; wired |
| Congress recovery | `ireland_action_reconvene_the_workers_congress` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_reconvene_the_workers_congress_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_reconvene_the_workers_congress.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_reconvene_the_workers_congress.dds` | `GFX_decision_ireland_action_reconvene_the_workers_congress` | 32x32 RGBA; wired |
| Blueshirt recovery | `ireland_action_demobilise_the_failed_directorate` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_demobilise_the_failed_directorate_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_demobilise_the_failed_directorate.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_demobilise_the_failed_directorate.dds` | `GFX_decision_ireland_action_demobilise_the_failed_directorate` | 32x32 RGBA; wired |
| Producer-estate recovery | `ireland_action_rebalance_the_producer_estates` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_rebalance_the_producer_estates_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_rebalance_the_producer_estates.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_rebalance_the_producer_estates.dds` | `GFX_decision_ireland_action_rebalance_the_producer_estates` | 32x32 RGBA; wired |
| Restoration recovery | `ireland_action_reconvene_the_crown_council` | `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/ireland_action_reconvene_the_crown_council_source.png` | `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/ireland_action_reconvene_the_crown_council.png` | `gfx/interface/decisions/ireland/actions/decision_ireland_reconvene_the_crown_council.dds` | `GFX_decision_ireland_action_reconvene_the_crown_council` | 32x32 RGBA; wired |

## Review and validation artifacts

- Final processed contact sheet: `docs/assets/ireland_p0_family_settlement_decision_icons/contact_sheet.png`.
- Source-art contact sheet with checkerboard transparency preview: `docs/assets/ireland_p0_family_settlement_decision_icons/contact_sheets/source_contact_sheet.png`.
- Processed 32x32 checkerboard review: `docs/assets/ireland_p0_family_settlement_decision_icons/contact_sheets/processed_contact_sheet.png`.
- Prompt log: `docs/assets/ireland_p0_family_settlement_decision_icons/prompts.md`.
- GFX wiring handoff: `docs/assets/ireland_p0_family_settlement_decision_icons/gfx_handoff.md`.
- Required plan handoff: `docs/plans/ireland_country_package/improvement_loop/ireland_p0_family_settlement_decision_icons_handoff.md`.

All ten source PNGs contain real alpha transparency. All ten processed PNGs are exactly 32x32 RGBA with transparent unused pixels. All ten runtime DDS files exist at the listed paths, have DDS headers reporting 32x32, use 32-bit uncompressed BGRA masks, and retain transparent pixels. No placeholder, fallback, recolour-only, or reused decision icon was used.
