# Ireland expansion focus final audit — 2026-08-13

## Scope and handoff status

This is a read-through of the current political, industrial, and territorial expansion in `common/national_focus/ireland_focus_tree.txt`, with source checks for localisation, icons, shines, AI plans, industrial concerns, and territorial decisions. The audit used the required offline wiki pages, vanilla documentation, `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster`.

Small, in-scope fixes made by this subagent:

| File | Identifiers changed | Reason |
| --- | --- | --- |
| `common/national_focus/ireland_focus_tree.txt` | `ireland_lough_swilly_watch`; `ireland_ford_cork_works_agreement`; `ireland_aer_lingus_air_link`; `ireland_steel_holdings_programme` | Restore strict research-filter parity: Lough Swilly has a direct maritime research-speed effect; the three company focuses do not have a direct research/doctrine/speed effect. |
| `localisation/english/ireland_l_english.yml` | `ireland_aer_lingus_air_link_reward_tt` | Add the missing reward tooltip for one of the 38 expansion focuses. |

No coordinates, prerequisites, rewards, route gates, icons, or `thumbnail.png` were changed. Concurrent work in the repository was preserved.

## Executive result

- The current source parses as **188 unique focus IDs**, with **no duplicate coordinates**. The new expansion tranche is the final 38 IDs (source order 151–188).
- There are exactly three authored opening trunks: `ireland_state_still_defined`, `ireland_economic_war_review`, and `ireland_defence_estimates`. The latter two use `available` gates for the opening Dáil/settlement sequence. The other nine no-prerequisite roots are hidden branch/reveal roots, not additional initial trunks.
- There are exactly five public political-family gateways. Each is revealed by `ireland_political_routes_revealed`, mutually excludes the other four, and checks `ireland_political_family_committed` before completion.
- Source-level focus inspection passes. The layout has zero connector crossings, node-through-connector intersections, long connectors, and same-row spacing defects. One non-blocking clerical detour advisory remains.
- All 38 expansion focuses have title, description, reward tooltip, icon, shine, and at least one AI plan entry. Research/XP filters now have exact direct-effect parity.
- The raster artefact is useful for visual review but reports unrelated vanilla continuous-focus DDS truncation errors and the same clerical detour; these are outside the Ireland source scope.

## Route coverage

| Surface | Current IDs | Coverage evidence | Status |
| --- | --- | --- | --- |
| Opening trunks | `ireland_state_still_defined`, `ireland_economic_war_review`, `ireland_defence_estimates` | Three no-prerequisite opening anchors; all other no-prerequisite roots have `allow_branch` and/or availability gates. | Pass |
| Public family gates | `ireland_republican_government`, `ireland_congress_reform_bridge`, `ireland_oduffy_network_revival`, `ireland_vocational_constitution`, `ireland_high_king_evidence_gate` | Five pairwise-complete `mutually_exclusive` groups, one shared reveal flag, one family commitment flag. | Structural pass; helper asymmetry below |
| Public family cabinets | `ireland_constitutional_service_cabinet`, `ireland_congress_workers_cabinet`, `ireland_blueshirt_patronage_board`, `ireland_estates_and_professions_council`, `ireland_household_council` | Each follows the selected family/capstone and sets an advisor-pool unlock flag. | Pass |
| Compact industrial concerns | `ireland_irish_sugar_company_charter`, `ireland_esb_supply_contracts`, `ireland_turf_development_board_programme`, `ireland_great_southern_railways_contract`, `ireland_ford_cork_works_agreement`, `ireland_aer_lingus_air_link`, `ireland_irish_shipping_registry`, `ireland_steel_holdings_programme`, `ireland_harland_and_wolff_access` | Nine focuses call `show_ideas_tooltip`, set a concern flag, and map to one-shot contracts in `common/ideas/ireland_industrial_concerns.txt` and `common/decisions/ireland_expansion_decisions.txt`. | Pass |
| Northern/territorial lane | `ireland_define_the_national_question`, `ireland_authorise_reunification_instruments`, five family methods, five Northern resolutions | Dedicated right-hand lane, family-specific method availability, and no automatic core or war goal. | Pass |
| Atlantic/external lane | `ireland_atlantic_ambition`, five external policies, `ireland_enforce_atlantic_claims`, postwar office, three postwar outcomes, conclusion | Atlantic policy is selected after a Northern resolution; claims are staged through paid decisions against states 120/122/123. | Pass |

All prerequisite and mutual-exclusion focus references resolve to one of the 188 IDs. The territorial lane does not use `add_core`, `create_wargoal`, or free external control in focus rewards; the only direct claims are the two state-120 claim focuses, with enforcement delegated to the existing decision category.

The territorial coordinates form the intended compact fan: policy definition/authorisation at x=13/y=8–9; five Northern methods at x=9,11,13,15,17/y=10; five resolutions at the same columns/y=11; Atlantic ambition at x=13/y=12; five external policies at x=9,11,13,15,17/y=13; claim enforcement at x=13/y=14; postwar office at x=19/y=15; three outcome reviews at x=17,19,21/y=16; and the conclusion at x=19/y=17.

## Public family gate audit

| Family | Gateway and visible gate | Key availability proof | Completion markers | Profile-helper finding |
| --- | --- | --- | --- | --- |
| Democratic | `ireland_republican_government` (`ireland_constitutional_draft`) | Democratic government and `ireland_government_formation` | `ireland_political_family_committed`, `ireland_family_democratic` | Does not call `ireland_commit_route`; downstream profiles can still commit. |
| Communist | `ireland_congress_reform_bridge` (`ireland_church_labour_consultation`) | Congress organisation/transition and labour-decisive flags plus public-order/church-labour proof | `ireland_family_communist`, `ireland_route_congress` | Calls `ireland_commit_route` in the family gateway. |
| Fascist | `ireland_oduffy_network_revival` (`ireland_close_oduffy_chapter`) | O'Duffy network/crisis/interface flags plus public-order/close-chapter proof | `ireland_family_fascist`, `ireland_route_oduffy` | Calls `ireland_commit_route` in the family gateway. |
| Oligarchic/vocational | `ireland_vocational_constitution` (reveal/availability only) | Cultural survey, vocational mandate, church-labour consultation, constitutional draft | `ireland_family_oligarchic`, `ireland_route_constitutional_vocational` | Calls `ireland_commit_route` in the family gateway. |
| Restoration | `ireland_high_king_evidence_gate` (`ireland_cultural_evidence_ledger`) | Verified evidence, convention-ready, serious stewardship, and ledger proof | `ireland_family_restoration`, `ireland_route_high_king` | Does not call `ireland_commit_route`; downstream profile can still commit. |

The family flags and reveal are structurally correct. The current source does not fully satisfy the expansion specification's **family commitment versus profile commitment** contract: `ireland_commit_route` is intended for the first downstream profile, but the Congress, O'Duffy, and vocational gateways call it directly. `ireland_commit_route` sets `ireland_route_committed`, clears settlement momentum, and starts route review/profile synchronisation (`common/scripted_effects/ireland_effects.txt:862-888`). This is the highest-priority follow-up; it should be resolved as a coordinated route-system change rather than by this narrow audit patch.

Reachability writers are present: National Settlement sets `ireland_political_routes_revealed` (`common/national_focus/ireland_focus_tree.txt:105`); the runtime refresh writes Congress organisation/transition and labour-decisive flags (`common/scripted_effects/ireland_runtime.txt:2859-2873`), O'Duffy network/crisis/interface flags (`:2915-2917`), vocational mandate (`:2330`), and High-King evidence/convention flags (`:1563`, `:1575`). The five family route-specific AI plans also reference their corresponding gateways. No focus or mutual-exclusion reference points to a missing ID.

## New-focus reward and localisation audit

The 38 expansion focuses all contain their own `custom_effect_tooltip`, and after the Aer Lingus fix all 38 title keys, description keys, and reward-tooltip keys resolve in `localisation/english/ireland_l_english.yml` (UTF-8 with BOM). The bodies match the player-facing outcomes:

- five family cabinets unlock the intended advisor pools and stability/command-power effects;
- nine industrial concerns unlock the corresponding selectable ideas and bounded factory, fuel, train, truck, plane, convoy, or electronics effects;
- Northern methods/resolutions set family-specific policy flags and never grant free territory;
- Atlantic routes set security, liberation, concession, or claim flags, while postwar focuses expose rights/protectorate/integration reviews.

No remaining reward/localisation mismatch was found in the 38-focus tranche. The only mismatch discovered was the missing `ireland_aer_lingus_air_link_reward_tt`, now added.

The compact-company wiring also resolves cleanly: all nine concern IDs in `common/ideas/ireland_industrial_concerns.txt` have `allowed`, `visible`, `available`, cost/removal cost, research/modifier, and AI entries; all nine `picture` names resolve through `interface/ireland_industrial_concerns.gfx` to 68x68 DDS files; and the four bounded one-shot contracts in `common/decisions/ireland_expansion_decisions.txt` are exposed by the concern flags.

## Icon and shine coverage

| Surface | Expected | Found | Validation |
| --- | ---: | ---: | --- |
| Focus source `icon = GFX_focus_<id>` | 38 | 38 | Every new source icon points at its own ID. |
| `interface/ireland_icons.gfx` registrations | 38 | 38 | All 38 `GFX_focus_ireland_*` sprites resolve to `gfx/interface/goals/ireland_*.dds`; existing 226 older registrations remain. |
| Focus shine registrations | 38 | 38 | Every `GFX_focus_<id>_shine` block has the matching texture/mask and `shine_overlay.dds`. |
| New DDS files | 38 | 38 | All are present at `gfx/interface/goals/ireland_<id>.dds`, 94x86, 32,464 bytes. |

The current raster errors are for nine **vanilla** continuous-focus DDS files, not these 38 Ireland icons.

## Strict search-filter parity

Source parser results after the patch:

| Filter | Tagged focuses | Direct-effect focuses | Mismatch |
| --- | ---: | ---: | --- |
| `FOCUS_FILTER_ARMY_XP` | 11 | 11 | none |
| `FOCUS_FILTER_NAVY_XP` | 11 | 11 | none |
| `FOCUS_FILTER_AIR_XP` | 4 | 4 | none |
| `FOCUS_FILTER_RESEARCH` | 25 | 25 | none |

The patch removed `FOCUS_FILTER_RESEARCH` from the Ford Cork, Aer Lingus, and Steel Holdings company focuses, and added it to `ireland_lough_swilly_watch`, which directly changes `ireland_maritime_research_speed_factor`. Industry, annexation, stability, international-trade, and political-character tags on the new focuses remain aligned with their authored concern, claim, stability, trade, or advisor-pool role.

## AI coverage

- `IRE_ireland_route_reactive` lists all 38 new IDs, including every cabinet, company, Northern method/resolution, Atlantic policy, claim-enforcement, postwar, and conclusion focus.
- `IRE_ireland_historical` lists 18 of the 38: the democratic family, peaceful territorial path, and material companies. Its 20 omissions reflect non-democratic or non-historical policy branches (mostly alternate-family/coercive routes); `ireland_harland_and_wolff_access` is also omitted because its state-119 ownership gate is a later Northern outcome. The omitted IDs are `ireland_congress_workers_cabinet`, `ireland_blueshirt_patronage_board`, `ireland_estates_and_professions_council`, `ireland_household_council`, `ireland_workers_reunification_campaign`, `ireland_ulster_ultimatum`, `ireland_customs_union_leverage`, `ireland_crown_and_province_mandate`, `ireland_all_island_workers_republic`, `ireland_force_the_border_question`, `ireland_belfast_compact`, `ireland_restore_ulsters_place`, `ireland_republics_across_the_channel`, `ireland_gaelic_marches`, `ireland_atlantic_concessions`, `ireland_dal_riata_claim`, `ireland_enforce_atlantic_claims`, `ireland_protectorate_statutes`, `ireland_integration_review_commission`, and `ireland_harland_and_wolff_access`.
- Route-specific plans reference all five family gateways. The 38 new focus blocks do not carry individual `ai_will_do` blocks; plan ordering and availability gates are the current AI mechanism. If a future contract requires per-focus weights, that is an additional design pass rather than a missing route entry.
- Historical claim decisions retain `factor = 0` under historical focus mode in `common/decisions/ireland_expansion_decisions.txt`.

## MCP geometry and raster evidence

Current source-inspect artefact (validation passed):

`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/89e89f950699195a24eea2e754dad10d89d57abd5239af017c3ad0f5ec40604a/16b4378bd8427cab4fe5c63acb11254067db85cc4f17be65f81505f987ad9f86/focus-inspect.225d9857e8f1c78f.json`

Inspect metrics: 188 focuses, 195 connectors, bounds x `-26..21`, y `0..17`, `crossingCount=0`, `nodeIntersectionCount=0`, `longConnectorCount=0`, `tooCloseSameRowPairCount=0`, minimum same-row spacing `2`, maximum horizontal connector span `8`, maximum vertical span `2`.

Current render artefacts:

- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/f056ec4fa7e73e49d889919ccfd06db415d5505a47ebc93299abad1eb18a6789/f9d7c5a0ac127f5dde30f6c9480b4d16dd4f005cf3deb431cd3b9fd5e728157f/ireland_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0f8a7b70ccd7112b0668bf7a69e1037920f75821ca15979eb876169156877ede/c521ae135aea3ba0df7a37d299b7b66d53f24ba6b8dea0c71544998b93d1c32a/ireland_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/be2911b5e95333f9d54307cf53c9c049ce185064d429d5769d30a9636424e0c7/ccfa70e04e4695330cace98590466f5cfc413b74719229da2ad45aea1f2128a2/ireland_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/421e29fe7f90157f03cb1f64017aa20b69fbd304e933f15165d9317a677f1d07/32141f8a33d0ed4f82fb9458d0075fb2661196811fb37f3846a25c5d6d243e7a/ireland_focus_tree.focus.source-map.json`

Current raster artefacts:

- PNG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/6568588693db63a53c3b24bb64430a7fffa7eec2b7103a27181e6fb69fea09af/863e324a554f6d865f06e689e30f6979581ecdc2d5512723519790418c9a7117/ireland_focus_tree.focus.png`
- Raster JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/56419b3648ed8ae2599a8ad53ca89e5dafbcdaa58da66624f764c57e00ddedea/c8b1782c1663114623fcd0db27fe739935ae291fff28f51df5b4d141ee15810d/ireland_focus_tree.focus.json`
- Raster HTML/SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/c41939f5e2dc4d8e3ceaee6a28eab12d0ded6881a71f8ccedec4ed4113200022/c19a8e372937f840cdb5b29c2384242d344866f064a735ecde893f8b85693de2/ireland_focus_tree.focus.html`; `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d29226e41f4a35d4e82f776cf937294b51925c385543b83fe19d03572d884f73/9d6c59a949b2ba1e0bba8bc4fc92250924f17cd7c77b429022f55d33365ff030/ireland_focus_tree.focus.svg`

The review render is 8,576x2,208; the padded raster is 4,776x2,406.

Raster validation is false because the analyser cannot load nine vanilla continuous-focus DDS files (`continuous_naval_production`, `continuous_air_production`, `continuous_non_factory_construct`, `continuous_reduce_training_time`, `continuous_suppression`, `continuous_repair`, `continuous_tech_share`, `continuous_boost_freedom`, and `continuous_restrict_freedom`; each reports truncated RGB data). It also repeats the Ireland clerical detour and the unrelated vanilla `continuous_restrict_freedom_desc` localisation warning. The source inspect validation remains passed and reports no Ireland blocking diagnostics.

## High-priority fixes, blockers, and simplifications

1. **Route contract follow-up:** remove the three family-gateway calls to `ireland_commit_route` or introduce the separately specified family-level helper, then verify profile plans and `ireland_route_committed` gates. This is a broader route-system change and was intentionally not patched here.
2. **Layout advisory:** `ireland_clerical_failure_bridge` → `ireland_clerical_guardianship` remains a horizontal-span-2/vertical-span-1 detour (source lines 3827–3846). It does not cross a node or connector, but a future geometry-only pass may align the child x-coordinate.
3. **Raster environment:** the nine vanilla DDS truncation errors and vanilla missing localisation are outside the mod source scope; no vanilla files were changed.

No focus route, industrial concern, territorial lane, icon, shine, or localisation was intentionally omitted by this audit. Full Clausewitz game loading/live campaign verification was not run in this subagent; the source parser and MCP checks above are the meaningful task-scoped evidence. `thumbnail.png` was not touched.

## Closure re-audit - 2026-08-13

This closure re-checks the current source after the family/profile lock corrections. No gameplay source file was changed in this turn; only this handoff was appended. The prior route-contract note above predates these corrections and is superseded for the five public gateways by the evidence below.

### Public family gateway ownership

All five public gateways now have the same structural lock: `allow_branch = { has_country_flag = ireland_political_routes_revealed }`, four-way mutual exclusion against the other public gateways, and `NOT = { has_country_flag = ireland_political_family_committed }` in availability. A source parser found zero `ireland_commit_route = yes` calls and zero direct `ireland_route_committed` writes in every gateway completion body.

| Gateway | Family markers written | Compatibility profile label | Downstream commitment |
| --- | --- | --- | --- |
| `ireland_republican_government` (line 461) | `ireland_political_family_committed`, `ireland_family_democratic` | none at the family gate | Existing democratic profile focuses retain their own route helper. |
| `ireland_congress_reform_bridge` (line 3451) | `ireland_political_family_committed`, `ireland_family_communist` | none; no `ireland_route_congress` at the gate | Plural or vanguard profile focus owns route commitment. |
| `ireland_oduffy_network_revival` (line 3621) | `ireland_political_family_committed`, `ireland_family_fascist` | none; no `ireland_route_oduffy` at the gate | Personal or corporate profile focus owns route commitment. |
| `ireland_vocational_constitution` (line 1360) | `ireland_political_family_committed`, `ireland_family_oligarchic` | `ireland_route_constitutional_vocational` is retained as the existing family/profile compatibility label | `ireland_vocational_constitution_capstone` owns route commitment after proof gates. |
| `ireland_high_king_evidence_gate` (line 4040) | `ireland_political_family_committed`, `ireland_family_restoration` | `ireland_route_high_king` is retained as the existing family/profile compatibility label | High Kingship keeps its authored legacy profile flow; this is outside the Congress/O'Duffy/vocational downstream-helper requirement. |

The two compatibility labels are not route commits: they do not set `ireland_route_committed`, reset settlement momentum, or start route review. They remain because AI plans, runtime profile synchronisation, advisor triggers, and the vocational capstone availability consume them.

### Downstream profile, capstone, advisor, and AI continuity

- Congress: `ireland_congress_plural_republic` (line 3513) and `ireland_congress_vanguard_cell` (line 3541) each set `ireland_route_congress`, populate `ireland_route_commitment_input`, and call `ireland_commit_route`. Their capstones (lines 3573 and 3596) call only `ireland_begin_conclusion_review`; `ireland_congress_workers_cabinet` (line 4488) remains reachable through the two-capstone prerequisite and writes `ireland_advisor_pool_congress_unlocked`.
- O'Duffy: `ireland_oduffy_personal_command` (line 3666) and `ireland_corporate_order` (line 3719) each own `ireland_route_oduffy`, the commitment input, and `ireland_commit_route`. Personal and corporate capstones (lines 3741 and 3769) remain helper-free conclusion reviews. `ireland_blueshirt_patronage_board` (line 4502) remains reachable from the public network gate and writes `ireland_advisor_pool_blueshirt_unlocked`.
- Vocational: `ireland_vocational_constitution_capstone` (line 1408) sets the retained profile label, commitment input, and `ireland_commit_route` before beginning conclusion review. `ireland_estates_and_professions_council` (line 4516) still requires that capstone and writes `ireland_advisor_pool_estates_unlocked`.
- High Kingship: `ireland_high_king_capstone` (line 4170) remains the authored convergence capstone and conclusion review; `ireland_household_council` (line 4530) still requires it and writes `ireland_advisor_pool_household_unlocked`.
- AI route plans remain wired in `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`: profile plans at lines 527, 619, 640, 659, and 683; shared Congress/O'Duffy plans at lines 763 and 801; High Kingship compatibility plan at line 908. Runtime profile selectors continue to consume the retained labels (`common/scripted_effects/ireland_runtime.txt:2011-2054`).

### Fresh inspect evidence

The current `hoi4.focus_inspect` result is:

`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/fffce96d959acb2180aa2d490bf35f765b0de2cbfb04aad4c6eb8e10991a3f29/9f49b4ae96f64c8909d12532a3e1a6fdb3b926fa12e81e2fcb54f2e1e8453257/focus-inspect.89f42fdb66e8591b.json`

Validation passed for the current source: 188 focuses, 195 connectors, bounds `x=-26..21`, `y=0..17`, zero connector crossings, zero node/connector intersections, zero long connectors, zero same-row spacing defects, maximum horizontal span 8, maximum vertical span 2, and minimum same-row spacing 2. The only Ireland layout advisory remains the non-blocking clerical failure bridge detour; the separate continuous-focus localisation warning is vanilla. No coordinates were changed in this re-audit, and `thumbnail.png` was not touched.

### Closure status

No exact defect remains in the requested gateway/profile ownership contract. No new blocker or simplification was introduced. The remaining High Kingship compatibility-label asymmetry and the clerical detour are documented design/geometry risks, not blocking parser findings. Full game loading and live-campaign verification remain outside this subagent's scope.
