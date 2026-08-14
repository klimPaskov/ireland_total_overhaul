# Final Ireland country-package integration audit — 2026-08-14

## Verdict

The active Ireland country package is source-complete across the requested
exceptional tranche and the existing character/company package. No missing
Ireland-owned GFX registration, country identifier, focus localisation,
decision/mission localisation, event-art reference, advisor card, concern/MIO
icon, or exceptional cosmetic localisation was found.

One asset-format defect was corrected locally: the ten exceptional cosmetic
identities had been emitted as DDS flags, but HOI4 country flags require
uncompressed 32-bit TGA files. Thirty valid TGA files now exist at the normal,
medium, and small flag paths. Parent integration removed all 40 obsolete,
unreferenced DDS outputs before staging.

## Coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| National focus tree | PASS | `common/national_focus/ireland_focus_tree.txt`; read-only `hoi4_focus_inspect` reports 256 focuses, 265 connectors, zero blocking diagnostics. |
| Focus icon and localisation coverage | PASS | All 256 focus IDs have registered icons/textures and `<focus_id>` plus `<focus_id>_desc` keys. Exceptional focus sprites/shines are in `interface/ireland_icons.gfx` and `interface/ireland_focus_shine.gfx`. |
| Exceptional ideas | PASS | 7 IDs in `common/ideas/ireland_exceptional_spirits.txt`; all seven `picture` tokens resolve in `interface/ireland_secondary_assets.gfx` to existing 60x68 DDS icons; titles/descriptions resolve. |
| Exceptional events | PASS | `ireland_events.438`–`.460` (23 unique direct events) in `events/ireland_exceptional_route_events.txt`; all report sprites resolve through `interface/ireland_exceptional_route_events.gfx` and are 210x176 DDS; title/description/options/effect keys resolve after the parent’s collision fix. |
| Exceptional decisions/missions | PASS | 11 action IDs and 11 mission IDs in `common/decisions/ireland_decisions.txt`; all 22 icons resolve in `interface/ireland_icons.gfx`, exist as 32x32 DDS, and have title/description keys. |
| Cosmetic identities | PASS after patch | 10 IDs in `common/countries/ireland_exceptional_cosmetic.txt`; all have `TAG`, `TAG_ADJ`, and `TAG_DEF` localisation plus normal/medium/small TGA flags. Flags are filename-discovered; no `.gfx` registration is required. |
| Advisors and leaders | PASS | `common/characters/ireland_route_characters.txt` contains 45 advisors and 24 country leaders. All 112 unique portrait/card references are registered and their textures exist. Large portraits are 156x210; advisor cards are 65x67; collective portraits are institutional names and use collective cards. |
| Industrial concerns and MIOs | PASS | 7 concerns in `common/ideas/ireland_industrial_concerns.txt` and 2 MIOs in `common/military_industrial_organization/organizations/ireland_organizations.txt`; all icons are registered/existing 68x68 DDS, all unlock flags and company-contract consumers are present, and names/traits localise. |
| English localisation | PASS | 3 English YAML files, 6,363 parsed keys, 6,363 unique keys, zero duplicate keys, zero empty values, and UTF-8 BOM on every file. |
| GFX texture references | PASS with vanilla dependencies | 1,277 Ireland interface texture references resolve locally or to the vanilla install. The 15 local misses are existing vanilla continuous-focus/parliament UI dependencies, not Ireland-owned package assets. |
| AI | PASS | `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` keeps the historical constitutional plan at zero for exceptional/convergence route factors and exposes route/profile-specific plans for alternate routes. |

## File surface checklist

- Country and cosmetics: `common/countries/ireland_exceptional_cosmetic.txt`,
  `localisation/english/ireland_exceptional_routes_l_english.yml`, and
  `gfx/flags/{,medium/,small/}`.
- Focus tree and wiring: `common/national_focus/ireland_focus_tree.txt`,
  `interface/ireland_icons.gfx`, and `interface/ireland_focus_shine.gfx`.
- Events and art: `events/ireland_exceptional_route_events.txt`,
  `interface/ireland_exceptional_route_events.gfx`, and
  `gfx/event_pictures/ireland_exceptional_routes/`.
- Decisions, missions, and ideas: `common/decisions/ireland_decisions.txt`,
  `common/ideas/ireland_exceptional_spirits.txt`, and
  `interface/ireland_secondary_assets.gfx`.
- Characters and portraits: `common/characters/ireland_route_characters.txt`,
  `interface/ireland_advisors.gfx`, `interface/ireland_sourced_assets.gfx`,
  `interface/ireland_route_assets.gfx`, `gfx/leaders/ireland/`, and
  `gfx/interface/ideas/ireland/advisors/`.
- Industry and MIO: `common/ideas/ireland_industrial_concerns.txt`,
  `common/military_industrial_organization/organizations/ireland_organizations.txt`,
  `interface/ireland_industrial_concerns.gfx`, and
  `common/decisions/ireland_expansion_decisions.txt`.
- Documentation and provenance: `docs/ireland_exceptional_routes.md`,
  `docs/assets/ireland_exceptional_routes_depth_2026-08-14/`, and the active
  asset handoff under `docs/plans/ireland_country_package/subagent_handoffs/`.

## Exceptional identifiers

The 22 decision/mission IDs audited were:

- Actions: `ireland_action_audit_the_royal_household`,
  `ireland_action_break_the_party_crown`,
  `ireland_action_accept_a_royal_geis`,
  `ireland_action_negotiate_a_provincial_budget`,
  `ireland_action_reserve_the_ulster_chair`,
  `ireland_action_call_a_confederal_council`,
  `ireland_action_record_an_otherworld_obligation`,
  `ireland_action_hear_a_regional_court`,
  `ireland_action_restitute_a_seized_site`,
  `ireland_action_narrow_the_containment_perimeter`,
  `ireland_action_arbitrate_a_provincial_veto`.
- Missions: `ireland_mission_complete_the_royal_circuit`,
  `ireland_mission_break_the_party_crown`,
  `ireland_mission_keep_the_veil_at_five_sites`,
  `ireland_mission_repair_the_broken_compact`,
  `ireland_mission_reconcile_regional_compacts`,
  `ireland_mission_extract_from_a_protected_site`,
  `ireland_mission_equip_a_fian_company`,
  `ireland_mission_fund_the_common_compact`,
  `ireland_mission_keep_the_fifth_seat_open`,
  `ireland_mission_prevent_rival_irelands`,
  `ireland_mission_survive_the_first_convergence_review`.

The 7 industrial concern IDs are
`ireland_company_electricity_supply_board`,
`ireland_company_irish_sugar_company`,
`ireland_company_turf_development_board`,
`ireland_company_great_southern_railways`,
`ireland_company_aer_lingus_air_link`,
`ireland_company_irish_shipping_registry`, and
`ireland_company_steel_holdings`. The MIO IDs are
`ireland_ford_cork_works_organization` and
`ireland_harland_wolff_belfast_organization`.

## Patch made in this audit

Generated 30 uncompressed 32-bit TGA flag files from the accepted processed
PNGs:

- `gfx/flags/IRE_IRELAND_*.tga` — 10 normal flags, 82x52.
- `gfx/flags/medium/IRE_IRELAND_*.tga` — 10 medium flags, 41x26.
- `gfx/flags/small/IRE_IRELAND_*.tga` — 10 small flags, 10x7.

Updated the active asset documentation to use TGA paths and the engine-correct
flag requirements:

- `docs/assets/ireland_exceptional_routes_depth_2026-08-14/manifest.md`
- `docs/assets/ireland_exceptional_routes_depth_2026-08-14/gfx_handoff.md`
- `docs/ireland_exceptional_routes.md`
- `docs/plans/ireland_country_package/subagent_handoffs/ireland_exceptional_routes_asset_handoff_2026-08-14.md`

Before the patch, the package presented DDS files as country flags. After the
patch, all 30 documented runtime flag paths are TGA, with descriptor 8,
image type 2, 32-bit pixels, opaque alpha, and exact expected dimensions.

## Map, state, politics, and lifecycle review

The exceptional tranche adds cosmetic identities, focus/decision/event state,
ideas, and company/MIO unlock state; it does not add states, provinces,
ownership, controllers, cores, claims, capitals, victory points, ports,
railways, supply nodes, or resource/building definitions. Its state references
are existing controlled-state gates in the decision/effect code. The existing
Ireland country setup, party/leader package, character cleanup, and route
cleanup remain parent-owned surfaces and were not redesigned here.

The 45 advisors use explicit historical names and the 14 collective country
leaders use institutional names. No opposite-gender random name pool or
fictional one-person leader generation is used by this package.

## Validation and remaining risk

Meaningful checks completed: read-only focus MCP inspection; balanced-block
coverage scans for focuses, characters, decisions/missions, ideas, and
cosmetic tags; GFX texture existence checks; DDS dimension checks for focus,
idea, advisor, company/MIO, decision/mission, and event assets; TGA header,
dimension, byte-length, opacity, and Pillow decode checks for all 30 corrected
flags; and complete English localisation duplicate/BOM scan.

Not run: live-game loading, save simulation, or map rendering. Parent integration
removed the 40 stale exceptional DDS flag outputs; the valid TGA replacements
and updated docs are ready for review.

No focus-tree redesign, country identity redesign, new package, thumbnail edit,
fallback art, or unrelated gameplay change was made.
