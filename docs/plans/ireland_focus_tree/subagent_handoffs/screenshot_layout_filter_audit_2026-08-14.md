# Screenshot, connector, and search-filter audit

Audit scope: `d0b4f21` (`common/national_focus/ireland_focus_tree.txt`) and its referenced focus icons/localisation. This is a read-only audit; no gameplay, asset, or thumbnail files were changed by this subagent.

The working tree currently contains uncommitted parent-agent edits to the focus file. Baseline facts below are read from `git show d0b4f21:common/national_focus/ireland_focus_tree.txt`; the current-worktree MCP snapshot is called out separately so parent review does not confuse the two states.

## Route coverage

| Route surface | Gateway/anchor IDs | Baseline status |
|---|---|---|
| Shared opening and constitutional/economic/defence trunks | `ireland_state_still_defined`, `ireland_national_settlement`, `ireland_provision_baseline`, `ireland_readiness_baseline` | Present; 17 opening focuses and downstream proof/conclusion gates. |
| Five public political families | `ireland_republican_government`, `ireland_congress_reform_bridge`, `ireland_oduffy_network_revival`, `ireland_vocational_constitution`, `ireland_high_king_evidence_gate` | All five gateways and downstream capstones are present. Their baseline reciprocal gateway mutex lists form the giant screenshot line; route locking is also enforced by `NOT = { has_country_flag = ireland_political_family_committed }` and family flags in each gateway `available`/reward. |
| Culture and exceptional routes | `ireland_cultural_survey`, `ireland_ira_republican_bridge`, `ireland_otherworld_investigation`, `ireland_high_king_capstone` | Present, with proof and conclusion flags. Several conclusion cards are available-gated rather than visibly connected. |
| Five Provinces | `ireland_five_province_mandates` -> federal, empty-chair, confederation, pentarchy, fifth-province, or rival conclusions -> `ireland_five_provinces_capstone` | All six conclusion routes are present. The capstone has a six-focus OR `prerequisite` block plus a repeated six-focus OR `available` block, which creates the large fan in the screenshot. One `prerequisite` block is OR semantics, so this is not an intentional all-six requirement; the visible block is removable if the `available` gate remains. |
| Northern settlement and territorial policy | `ireland_northern_settlement_ledger` -> `ireland_northern_policy_proof` -> `ireland_define_the_national_question` -> five method/resolution lanes -> Atlantic/postwar settlement | Present. The ledger directly claims state 119 and the later focuses unlock territorial decisions. Baseline filters were incomplete (see below); current parent worktree adds ANNEXATION across this lane. |

No whole route family is absent in the baseline. The simplifications are visual/gating presentation: giant reciprocal mutex meshes, long visible prerequisite fan-outs, and several proof-gated cards with no visible incoming connector.

## Mutual-exclusion visual edges

The baseline `d0b4f21` source still contains the old public-gateway mutex mesh. Each of the five gateway cards reciprocally excludes the other four, producing 20 directed declarations/10 unordered lines at `y = 14`:

| Gateway pair family | Coordinates | Maximum span/risk |
|---|---:|---|
| `ireland_republican_government` <-> `ireland_congress_reform_bridge` | `(-24,14)` <-> `(-18,14)` | 6; safe alone, but part of complete mesh |
| `ireland_republican_government` <-> `ireland_vocational_constitution` | `(-24,14)` <-> `(-12,14)` | 12; passes the Congress gateway |
| `ireland_republican_government` <-> `ireland_oduffy_network_revival` | `(-24,14)` <-> `(-6,14)` | 18; passes Congress and vocational gateways |
| `ireland_republican_government` <-> `ireland_high_king_evidence_gate` | `(-24,14)` <-> `(0,14)` | 24; crosses all three intermediate gateway cards |
| `ireland_congress_reform_bridge` <-> `ireland_vocational_constitution` | `(-18,14)` <-> `(-12,14)` | 6; part of complete mesh |
| `ireland_congress_reform_bridge` <-> `ireland_oduffy_network_revival` | `(-18,14)` <-> `(-6,14)` | 12; passes vocational gateway |
| `ireland_congress_reform_bridge` <-> `ireland_high_king_evidence_gate` | `(-18,14)` <-> `(0,14)` | 18; passes vocational and O'Duffy gateways |
| `ireland_vocational_constitution` <-> `ireland_oduffy_network_revival` | `(-12,14)` <-> `(-6,14)` | 6; part of complete mesh |
| `ireland_vocational_constitution` <-> `ireland_high_king_evidence_gate` | `(-12,14)` <-> `(0,14)` | 12; passes O'Duffy gateway |
| `ireland_oduffy_network_revival` <-> `ireland_high_king_evidence_gate` | `(-6,14)` <-> `(0,14)` | 6; part of complete mesh |

Other baseline mutex groups with through-card or long-span risk:

| Group/edge | Coordinates | Risk |
|---|---:|---|
| `ireland_turn_contact_into_power` <-> `ireland_containment_protocol` | `(-44,6)` <-> `(-28,6)` | Span 16; passes `ireland_compact_with_otherworld` at `(-36,6)`. |
| `ireland_federal_republic` <-> `ireland_council_by_provincial_mandate` | `(15,7)` <-> `(25,7)` | Span 10; a long cross-lane line. |
| `ireland_crown_in_party_hands` <-> `ireland_the_stone_gives_its_answer` | `(-4,21)` <-> `(4,21)` | Span 8; passes `ireland_household_council` at `(0,21)` and is part of a three-card exclusion group. |
| `ireland_the_rights_of_local_guardians` <-> `ireland_recognise_the_elder_claim` | `(-34,7)` <-> `(-42,7)` | Span 8; passes `ireland_the_hounds_are_heard_again` at `(-38,7)` and is part of a three-card group. |
| `ireland_pentarchy_of_ireland`, `ireland_the_fifth_province`, `ireland_rival_irelands` | `(27,10)`, `(29,10)`, `(31,10)` | Reciprocal triangle; the 4-span pentarchy/rival line runs through the fifth-province card. |
| `ireland_elective_crown` <-> `ireland_guardian_crown` | `(-2,16)` <-> `(2,16)` | Span 4; `ireland_crown_powers_charter` at `(0,17)` is close enough to be a possible card-intersection risk depending on engine card bounds. |

Short local pairs (span <= 4) are not independently concerning: arms/authority, Congress plural/vanguard, O'Duffy capstones, emergency/sealed state, producer/executive estates, captive crown/throne, and high-king living-land/unbounded rule. The hounds/rights/elder and stone/household/crown groups remain worth checking as groups because a short line can still pass through the third card.

The parent worktree currently removes the public-gateway mesh and several other long mutex declarations, replacing route locks with `available`/`NOT has_completed_focus` checks. That is the correct direction for the screenshot issue, but it leaves isolated-card warnings listed under Remaining route risks.

## Prerequisite visual edges and the Five Provinces fan

Baseline `d0b4f21` has 263 explicit prerequisite connector edges. The most important spans are:

| Source -> destination | Coordinates / span | Source evidence |
|---|---:|---|
| `ireland_fund_the_federal_compact` -> `ireland_five_provinces_capstone` | `(15,10)` -> `(23,12)`, Manhattan 10 | Capstone prerequisite block, around baseline L4514; one OR block containing six focus IDs. |
| `ireland_rival_irelands` -> `ireland_five_provinces_capstone` | `(31,10)` -> `(23,12)`, Manhattan 10 | Same block. |
| `ireland_five_province_mandates` -> `ireland_federal_republic` | `(23,5)` -> `(15,7)`, Manhattan 10 | Baseline L4200. |
| `ireland_dominion_claim` -> `ireland_otherworld_capstone` | `(-44,10)` -> `(-36,12)`, Manhattan 10 | Baseline L5147. |
| `ireland_otherworld_evidence_ledger` -> `ireland_turn_contact_into_power` / `ireland_containment_protocol` | `(-36,5)` -> `(-44,6)` / `(-28,6)`, Manhattan 9 | Baseline L4589/L4669/L4643; long branch fan near the Otherworld row. |
| `ireland_high_king_capstone` -> `ireland_high_king_of_two_irelands` / `ireland_crown_and_five_provinces` | `(0,24)` -> `(-8,25)` / `(8,25)`, Manhattan 9 | Baseline L4128/L5178/L5208. |
| `ireland_a_government_under_the_mounds` -> `ireland_otherworld_capstone` | `(-42,9)` -> `(-36,12)`, Manhattan 9 | Baseline L4875/L5147. |
| `ireland_five_province_mandates` -> `ireland_pentarchy_guardians` | `(23,5)` -> `(29,7)`, Manhattan 8 | Baseline L4166/L4221. |
| `ireland_the_fifth_province` -> `ireland_five_provinces_capstone` | `(29,10)` -> `(23,12)`, Manhattan 8 | Baseline L4447/L4509. |
| `ireland_provincial_powers_convention` -> `ireland_four_provinces_and_an_empty_chair` | `(23,6)` -> `(19,10)`, Manhattan 8 | Baseline L4244/L4301; the clearest ordinary Five Provinces detour. |

Additional baseline M7/M6 edges that are visibly detached from their local lanes: `ireland_strict_neutrality` -> `ireland_vatican_small_state_mediation` (M7), `ireland_public_order_review` -> `ireland_ira_republican_bridge` (M7), `ireland_establish_naval_staff` -> `ireland_harbour_defence_board` (M7), `ireland_compact_with_otherworld` -> `ireland_regional_otherworld_courts`/`ireland_recognise_the_elder_claim` (M7), `ireland_break_the_captive_crown` -> `ireland_high_king_capstone` (M7), `ireland_emergency_repeal` -> `ireland_recovery_bridge` (M6), and `ireland_crown_defence_council` -> `ireland_crown_in_party_hands`/`ireland_the_stone_gives_its_answer` (M6).

The baseline `ireland_five_provinces_capstone` explicitly repeats the same six focus IDs in `available = { OR = { has_completed_focus = ... } }`. The wiki says `available` normally does not draw prerequisite lines, but the user screenshot is authoritative and engine/UI versions can expose or emulate these relations. Keep the OR gate for route semantics; do not replace it with six visible AND-style prerequisites. If a visible anchor is needed, use one local route anchor and retain the OR completion gate in `available`.

`allow_branch`, `bypass`, and the `available` blocks containing only flags/variables do not have authored focus endpoints. The relevant engine-risk type not represented as ordinary prerequisite geometry is `available`/`has_completed_focus`; baseline contains 219 such focus references, including the six-focus Five Provinces OR fan and many cross-lane proof gates. MCP structural connector counts should not be treated as proof that those UI/game lines cannot appear.

## Search-filter audit

Baseline counts: 29 RESEARCH, 22 INDUSTRY, 0 MANPOWER, 5 ANNEXATION, 14 INTERNATIONAL_TRADE, 15 ARMY_XP, 12 NAVY_XP, and 4 AIR_XP filters.

### Missing MANPOWER

There are no direct `add_manpower`, `create_unit`, or leader-recruitment rewards. However, the base filter documentation explicitly includes equipment in MANPOWER’s normal use. The following 31 focuses directly add equipment to stockpile and therefore are candidates for MANPOWER in addition to their existing thematic filters:

`ireland_defence_estimates` (L180), `ireland_transport_priority` (L1608), `ireland_maritime_reserve` (L1631), `ireland_emergency_stockpiles` (L1718), `ireland_readiness_command` (L1921), `ireland_maritime_protection` (L2047), `ireland_requisition_trawler_hulls` (L2122), `ireland_atlantic_convoy_office` (L2439), `ireland_professional_army` (L2522), `ireland_interoperability` (L2579), `ireland_emergency_mobilisation` (L2614), `ireland_armed_neutrality` (L2705), `ireland_arms_before_authority` (L3243), `ireland_northern_question_in_arms` (L3315), `ireland_ira_army_council` (L3360), `ireland_congress_vanguard_cell` (L3500), `ireland_oduffy_personal_command` (L3625), `ireland_army_acceptance` (L3655), `ireland_ailtiri_cell_network` (L3855), `ireland_ceannaire_state` (L3933), `ireland_republican_self_defence` (L5446), `ireland_motorised_command_contracts` (L5535), `ireland_emergency_directorate` (L5563), `ireland_crown_defence_council` (L5766), `ireland_great_southern_railways_contract` (L5939), `ireland_ford_cork_works_agreement` (L5956), `ireland_aer_lingus_air_link` (L5977), `ireland_irish_shipping_registry` (L5994), and `ireland_ulster_ultimatum` (L6382).

The last company/logistics entries are lower-priority UI candidates because their primary purpose is industrial/logistics contracting, but they still directly grant equipment under the documented filter rule.

At the final current-worktree read, the parent had added MANPOWER to most military stockpile focuses. The remaining direct-equipment gaps were `ireland_armed_neutrality` (L2705; infantry/support equipment in the armed-neutrality route) and `ireland_ailtiri_cell_network` (L3855; infantry/support equipment for the paramilitary cell network). Conversely, the parent had added MANPOWER to four industrial/company contract focuses whose primary branch purpose is not recruitment: `ireland_great_southern_railways_contract` (L5939), `ireland_ford_cork_works_agreement` (L5956), `ireland_aer_lingus_air_link` (L5977), and `ireland_irish_shipping_registry` (L5994). Retain INDUSTRY/NAVY_XP on those company focuses and review/remove MANPOWER unless the project intentionally treats their equipment contracts as force-generation rewards.

### Missing INDUSTRY

These focuses directly construct buildings but lack INDUSTRY:

| Focus | Baseline reward | Why the filter is missing |
|---|---|---|
| `ireland_coastwatch` (L1946) | radar station in state 113 | Direct state building construction. |
| `ireland_air_warning` (L1980) | anti-air in state 113 | Direct state building construction. |
| `ireland_port_defence_project` (L2012) | anti-air in state 135 | Direct state building construction. |
| `ireland_coastal_patrol_flotilla` (L2167) | naval base in state 135 | Direct state building construction. |
| `ireland_lough_swilly_watch` (L2396) | radar station in state 134 | Direct state building construction. |
| `ireland_readiness_conclusion` (L2640) | arms factory in a random owned core state | Direct factory construction. |

Existing Industry assignments for `ireland_energy_board`, `ireland_domestic_manufacturing`, `ireland_development_authority`, `ireland_provision_conclusion`, the Naval Service construction board, reconstruction focuses, and company/contract focuses match their building, production, fuel, or industrial-organization rewards. No high-confidence Industry false positive was found.

### ANNEXATION: Northern and territorial lane

Only the five coercive/claim focuses have ANNEXATION in baseline: `ireland_ulster_ultimatum` (L6382), `ireland_force_the_border_question` (L6451), `ireland_gaelic_marches` (L6543), `ireland_dal_riata_claim` (L6565), and `ireland_enforce_atlantic_claims` (L6576).

High-confidence missing ANNEXATION candidates tied to Northern Ireland reclamation/territorial policy are:

`ireland_northern_settlement_ledger` (L2885; direct `119 = { add_claim_by = ROOT }`), `ireland_define_the_national_question` (L6325; opens the territorial policy), `ireland_authorise_reunification_instruments` (L6348; opens the method decisions), `ireland_northern_plebiscite_guarantees` (L6361; unlocks plebiscite protection), `ireland_workers_reunification_campaign` (L6372; unlocks the workers border campaign), `ireland_customs_union_leverage` (L6394; unlocks the Belfast compact offer), `ireland_crown_and_province_mandate` (L6405; unlocks provincial assent), `ireland_settlement_under_law` (L6416), `ireland_all_island_workers_republic` (L6435), `ireland_belfast_compact` (L6476), and `ireland_restore_ulsters_place` (L6495). These focus rewards either open territorial decisions or set a Northern territorial resolution flag.

Broader-lane candidates, depending on whether the project wants every Northern policy card grouped by the territorial filter, are `ireland_northern_local_authorities`, `ireland_northern_trade_corridor`, `ireland_northern_labour_social_bridge`, `ireland_northern_federal_preparation`, `ireland_northern_unitary_preparation`, `ireland_northern_wartime_bargain`, and `ireland_northern_policy_proof` (baseline L2906–L3048). Their rewards are delegations, a border corridor, an industrial settlement, constitutional arrangements, a wartime bargain, and foreign-guarantee review rather than direct claims. The parent worktree currently adds ANNEXATION to this broader group; retain it if the screenshot/search requirement is intentionally lane-wide.

The current-worktree territorial lane still has four likely omissions under the user’s explicit lane-wide requirement: `ireland_northern_question_in_arms` (L3298; requires the Northern ledger and sets `ireland_ira_northern_policy_ready`), `ireland_unfinished_national_question` (L5990; follows the Northern policy proof), `ireland_border_and_atlantic_dossier` (L6006; unlocks `ireland_territorial_commission_border_atlas`), and `ireland_test_the_state_instruments` (L6021; opens `ireland_territorial_policy_open`). Add ANNEXATION to these if “Northern Ireland reclamation/territorial policy content” includes the complete lead-in and IRA-linked Northern policy cards, as the user wording suggests. The parent worktree already covers the ledger, integration cards, policy proof, reunification methods, resolution lanes, Atlantic claims, and postwar settlement cards.

Postwar Atlantic settlement focuses (`ireland_postwar_settlement_office`, `ireland_local_rights_charter`, `ireland_protectorate_statutes`, `ireland_integration_review_commission`, `ireland_atlantic_settlement_concluded`) unlock settlement/protectorate/integration decisions for Scotland, Wales, Cornwall, and the Highlands. They are lower-confidence ANNEXATION candidates because they are postwar administration rather than the Northern reclamation lane.

### INTERNATIONAL_TRADE

High-confidence missing candidates:

- `ireland_1938_trade_settlement` (L363): named trade settlement, sets `ireland_trade_settlement_ready`/`ireland_port_transfer_open`, and currently has only POLITICAL/RESEARCH/BALANCE_OF_POWER.
- `ireland_northern_trade_corridor` (L2927): directly unlocks `ireland_action_open_a_border_corridor`, but currently has only POLITICAL (the parent worktree adds ANNEXATION; INTERNATIONAL_TRADE is still the relevant economic filter).
- `ireland_customs_union_leverage` (L6394): explicitly represents a customs-union lever and unlocks the Belfast compact offer; currently only POLITICAL.

At the final current-worktree read, parent edits had added INTERNATIONAL_TRADE to all three high-confidence candidates above (`ireland_1938_trade_settlement`, `ireland_northern_trade_corridor`, and `ireland_customs_union_leverage`). Recheck the exact line before merge because this audit ran while the parent’s uncommitted focus edits were still moving.

No high-confidence false-positive trade filter was found because vanilla uses INTERNATIONAL_TRADE for foreign supply contracts, procurement, port access, and diplomatic trade channels as well as literal market effects. Review-only candidates under a strict market-only interpretation are `ireland_active_neutrality` (L442), `ireland_strict_neutrality` (L2684), `ireland_treaty_port_diplomacy` (L2724), `ireland_vatican_small_state_mediation` (L2809), `ireland_foreign_safeguards` (L2815), and `ireland_neutrality_posture` (L2844); their rewards are posture/mediation/foreign-access decisions rather than market transactions. `ireland_british_leverage_management`, `ireland_american_diaspora_mission`, `ireland_atlantic_convoy_office`, `ireland_treaty_port_transfer`, and `ireland_atlantic_concessions` have clear supply, procurement, convoy, port, or concession hooks and should retain INTERNATIONAL_TRADE.

### RESEARCH and XP

No missing or false-positive RESEARCH, ARMY_XP, NAVY_XP, or AIR_XP filter was found against direct focus rewards. All 29 RESEARCH focuses grant a tech bonus, doctrine reduction, intelligence/research capability, or a research-speed modifier (`ireland_lough_swilly_watch`); all direct XP focuses carry the corresponding XP filter. In particular, `ireland_regional_maritime_defence_pact` grants all three XP types and has all three XP filters.

## Icon coverage

| Surface | Result |
|---|---|
| Focus icon references | 256/256 focus blocks have a unique `GFX_focus_ireland_*` icon reference. |
| GFX registration | All 256 focus icon names resolve in `interface/ireland_icons.gfx` or the dedicated focus-icon GFX files. |
| Texture files | All referenced focus icon DDS paths exist under `gfx/interface/goals/ireland/`. |
| Duplicate focus icon IDs | None found. |
| Filter icons/localisation | Base filter names are vanilla; no Ireland-owned filter sprite/localisation change is required for the listed filter additions. |

## Localisation and reward mismatch list

- All 256 baseline focus IDs have both `<focus_id>` and `<focus_id>_desc` localisation keys.
- All focus-owned `custom_effect_tooltip` keys resolve. `available_mio_tt` in `ireland_ford_cork_works_agreement` (L5956) and `ireland_harland_and_wolff_access` (L6040) is the vanilla MIO engine key, not a missing Ireland localisation key.
- The actionable reward/filter mismatches are the direct building/Industry, direct equipment/Manpower, Northern claim/Annexation, and trade settlement/International Trade findings above. No focus name/description contradicts a detected direct reward strongly enough to require a text rewrite in this audit.

## AI behavior gaps

`common/national_focus/ireland_focus_tree.txt` baseline has `ai_will_do` on 75/256 focuses, concentrated in public-family route choices, Naval Service, IRA/exceptional routes, and capstones. The Northern settlement and territorial-policy lanes have no focus-level `ai_will_do` on the policy cards (`ireland_northern_settlement_ledger` through `ireland_northern_policy_proof`, baseline L2885–L3048; `ireland_define_the_national_question` through `ireland_atlantic_settlement_concluded`, baseline L6325–L6630).

`common/ai_strategy/ireland_ai_strategy.txt` has profiles and a Northern occupation/integration overlay (around L363), plus a Dillon intervention strategy targeting state 119 (around L82–L92), but no dedicated strategy that chooses the Northern method/resolution branches or Atlantic territorial path after the policy gateway. Add route-aware AI only after preserving the existing country-flag proof gates; do not make AI choose a method before the corresponding decision/method flag is open.

## High-priority fixes

1. Keep the parent’s removal of the five-gateway reciprocal mutex mesh. If route exclusivity must remain visible, use only local pairwise choices; the family-wide lock is already enforced by `ireland_political_family_committed` and family flags.
2. Keep the parent’s removal of the six-focus visible `ireland_five_provinces_capstone` prerequisite fan; retain its one-route OR completion gate in `available` and add at most one local visual anchor if needed.
3. Add/verify ANNEXATION for the complete Northern/territorial lead-in; the parent worktree covers the main ledger, integration, method/resolution, Atlantic, and postwar cards but the four lead-in IDs listed above remained outside the filter at the final read.
4. Review current MANPOWER additions against branch purpose: add it to the two military gaps listed above, but do not leave it on the four company/industrial contract focuses without an explicit force-generation rationale.
5. Add INDUSTRY to the six direct building-construction focuses listed above.
6. Review isolated cards after connector cleanup and restore a local visible anchor where it improves route comprehension without recreating cross-tree fans.

## Current-worktree MCP evidence and remaining risks

Current parent worktree (not baseline) was inspected/rendered read-only:

- [focus inspect JSON](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/e92acf69e7a90f5d3151e4528e8f2f5d98781cdb4787779dd69b7451dcc64d4b/21f02d30f44c39bb208bf179166444f5efc9d2948135a7a59dfb6caec68fdd0a/focus-inspect.bda2be7db9d8f1f4.json)
- [focus HTML render](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4a00731f563b4b7c903fbb67a7588387c7c6074e67fa2914ab77fd899092f45d/787ba45f381b355627b6fa43ebbedb976034d52947fb313473723dc8b086fd86/ireland_focus_tree.focus.html)
- [focus SVG render](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/01912e121cbceae0aeea3564e05ceda8da9ec1d760e0952caea65bd85a0b8ea8/d1a56c3679b6f060604ed6fc5ed54701f7af27fa7fb99d6cb80424423855eaeb/ireland_focus_tree.focus.svg)
- [focus JSON render](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/a30a5cc1d6736545342ffa65886162d33b1c3e3dee7bee1b3075c91223b59d20/6274fab1dd85a8479ea8e8f472bf8bc413d68cb25e28519d309fcfa9f18adc4a/ireland_focus_tree.focus.json)

The current MCP snapshot reports 256 focuses, 234 authored connectors, zero connector crossings/node intersections/long-connector diagnostics, and validation passed. It still reports eight isolated focuses: `ireland_establish_naval_staff`, `ireland_vatican_small_state_mediation`, `ireland_high_king_capstone`, `ireland_federal_republic`, `ireland_fund_the_federal_compact`, `ireland_the_sealed_state`, `ireland_otherworld_capstone`, and `ireland_high_king_of_two_irelands`. These are the main remaining visual/route-comprehension risks after moving proof gates into `available`.

The high-fidelity raster check was not used as a completion gate because it also reports unrelated generic continuous-focus DDS diagnostics; the structural inspect/render evidence above is the meaningful focus-tree validation for this audit.

## Frozen closure verdict (2026-08-14)

The parent’s final read-only worktree pass now has 256 focuses and 234 authored connectors, with zero connector crossings, node intersections, or long-connector diagnostics; maximum horizontal span is 4 and validation passed. The fresh [focus-inspect artifact](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/7560fe95c23c41fc818ab237d997f9acf6f7a6e9e12c9fb2661f50083d9d4b92/d816c31c4f2712613ae2419ca64c2fae86d1c0d4c4b6af6976315b52edd5fc95/focus-inspect.eacefcd9888a83b9.json) still reports only the eight isolated-focus warnings listed above, plus the unrelated vanilla continuous-focus localisation warning.

Filter closure against the current source: all 29 direct equipment-stockpile focus blocks carry MANPOWER; all 22 direct building-construction focus blocks carry INDUSTRY (28 total Industry-tagged focuses); the three high-confidence trade settlement/corridor/customs focuses carry INTERNATIONAL_TRADE; and ANNEXATION is present on 32 current focuses. RESEARCH and all Army/Navy/Air XP tags continue to match their direct rewards.

Parent closure: the four territorial lead-in cards—`ireland_northern_question_in_arms`, `ireland_unfinished_national_question`, `ireland_border_and_atlantic_dossier`, and `ireland_test_the_state_instruments`—now carry ANNEXATION. The lane-wide territorial set is 36 focuses; the strict requirement has no remaining blocker.

Final parent inspection revision `938dd72614e85122` preserves 256 focuses and 234 connectors with zero crossings, node intersections, long connectors, or spacing defects and a maximum horizontal span of four. [Final focus-inspect artifact](hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/b8873cf66c52f21dbf1a1e811c3af8828a7bf97d2692463a678b7b822137e4ad/a9ca1348d760216387a8021d7696273b5be674d89533fc7731187018b106e8d6/focus-inspect.938dd72614e85122.json).
