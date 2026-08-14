# Ireland country-package final audit — 2026-08-14

## Disposition

**COMPLETE for the requested read-only source audit at `89ff719` (`Compact Ireland political family lanes`).** No hard Ireland country-package source blocker was found. The gameplay source is unchanged in the worktree after that commit; this handoff is the only audit artifact added by this subagent. No gameplay file was patched and no commit was created.

This is a source-level completion result, not a live-save/gameplay sign-off. HOI4 was not launched, and the full fresh-1936 route/scenario programme, live AI selection, timed decision expiry, and in-game GUI interaction remain parent-owned validation work.

The working tree contains concurrent parent documentation/asset-manifest edits, `thumbnail.png`, and layout handoffs. They were preserved. `89ff719` itself changed only 31 coordinate pairs in `common/national_focus/ireland_focus_tree.txt` plus its layout handoff.

## Coverage checklist

| Surface | Result | Evidence / disposition |
| --- | --- | --- |
| Tag, country history, politics, start setup | PASS | Vanilla `IRE` is intentionally reused; `history/countries/IRE - Ireland.txt` initializes capital 113, OOB, three research slots, 10 convoys, politics, and `ireland_initialize_campaign`. |
| Leaders, 45 Chaos Redux advisor cards, portraits | PASS | `common/characters/ireland_route_characters.txt`: 45 `advisor` blocks and 24 `country_leader` blocks; all referenced character portrait GFX and textures resolve. |
| Parties, cosmetic tags, flags | PASS | 20 party-name assignments resolve; 18 cosmetic tags have definitions, localisation, and normal/medium/small flags. |
| Seven industrial concerns, two MIOs, nine contracts | PASS | Exact requested counts and cross-wiring are present; each contract is one-use and uses the 35-day contract macro. |
| Focus IDs and AI references | PASS | 218 unique focus IDs; 718 AI focus references covering 218 unique IDs; unknown AI focus IDs: 0. |
| Five family locks and depth | PASS | Five gateway locks are mutually exclusive and set one family flag; family AI depths are democratic 18, Congress 23, Blueshirt 25, producer-estate 21, restoration 21. |
| Focus layout | PASS with one nonblocking warning | MCP focus inspection: 218 focuses/226 connectors, zero crossings, node intersections, long connectors, duplicate coordinates, and same-row spacing defects; one retained clerical two-column linear-detour warning. |
| Northern and Atlantic territorial lifecycle | PASS | Five family methods, target-state checks, transfer/refusal/claim/wargoal paths, event-target cleanup, and no automatic cores. |
| Report art, GFX, localisation | PASS | Event picture/GFX/texture crosswalk complete; report/news dimensions and current English localisation audit are complete. |
| Parliament initialization and button semantics | PASS | Day-one Dáil action is free and visible; later Seanad/confidence/budget buttons use matching `_click`/`_click_enabled` scripted-GUI hooks and live ledger gates. |
| Event cadence | PASS | Daily hooks are IRE-scoped state synchronization; the player-facing programme dispatcher runs on the monthly IRE pulse and allows at most one programme event per pulse. |
| Decision/mission lifecycle and cleanup | PASS at source level | `1984ff0` decision fixes are present: terminal outcomes moved to `remove_effect`, launch/cancel cleanup exists, timed flags use file-local literals, and Provincial Assent has four human legality floors. |
| Balance/material rewards | PASS with design caveat | Starting weakness is bounded and recoverable; contracts reserve productive capacity and are distinct/one-use. Five stale territorial branches refund exactly 50 PP while consumed material remains spent; this is documented as an administrative refund, but remains a balance-review caveat. |
| Parser-safe constants and unknown IDs | PASS in source scans | No unresolved project constant references or country-linked event/decision/focus/scripted-call references were found in the audited source set. |

## Country identity, history, map, and starting playability

### Tag and history

Ireland uses the vanilla `IRE` registration rather than inventing a second country tag. This is consistent across `history/countries/IRE - Ireland.txt`, focus `country = { factor = 0 tag = IRE }` gating, `original_tag = IRE` scripted checks, AI plans, decisions, events, MIOs, and cosmetic identity helpers. No missing custom `common/country_tags` registration is a defect here.

`history/countries/IRE - Ireland.txt` has:

- `capital = 113`, `oob = "IRE_1936"`, `set_research_slots = 3`, and `set_convoys = 10`;
- the intended initial technology, democratic politics, 1933 election, 98/1/1 popularity, and one guarded `ireland_initialize_campaign = yes` call;
- a 1939 dated history block with the historical OOB, technologies, doctrines, focuses, and special-project setup.

`history/units/IRE_1936.txt` and `history/units/IRE_1939.txt` define five usable templates (Infantry Division, Coastal Defence Battalion, Marine Service Company, Coastal Watch Brigade, Emergency Reserve Division), but start only one historical infantry division at province `11293`. The start has one infantry-equipment production line and no free navy or air force. This is a deliberately weak but playable island opening, and route systems add later maritime/defence capacity rather than granting a large day-zero army.

Vanilla state references are coherent:

- state `113` Leinster/Ireland: IRE owner/core, Dublin capital and VP `11293`;
- state `119` Northern Ireland: initial ENG owner with the expected ENG/IRE/NIR cores;
- states `120` Scottish Highlands, `122` Wales, and `123` Cornwall: valid vanilla ENG targets for the Atlantic branches.

No Isle of Man target, invalid state ID, invalid capital, or route-owned starting state was found. No territorial focus, event, or decision grants a free core.

## Politics, leaders, advisors, parties, flags, and assets

`common/characters/ireland_route_characters.txt` contains exactly 45 advisor cards and 24 country leaders. The 45 advisor IDs are all recruited from `history/countries/IRE - Ireland.txt` or route lifecycle effects and have corresponding English name keys. The leader set includes the historical/personal route figures and institutional/council figures. Institutional leaders use institutional names rather than personal random-name pools; no opposite-gender generated portrait/name pairing or unsupported female metadata was found.

Portrait evidence:

- 98 character portrait GFX references resolve to `interface/ireland_sourced_assets.gfx` or `interface/ireland_route_assets.gfx`;
- all 98 texture paths exist;
- runtime leader portraits are 156x210 and advisor cards are 65x67;
- sourced historical portraits and generated institutional portraits remain separated in the GFX surfaces.

`common/scripted_effects/ireland_runtime.txt` contains 20 `set_party_name` assignments across democratic, communist, fascist, and neutrality branches. The corresponding `ireland_party_*` name/long-name localisation keys resolve. The neutral IRA branch is unusual but is an explicit authored route choice, not an unknown party token.

`common/countries/ireland_cosmetic.txt` defines these 18 route identities, all matched by `TAG`, `TAG_ADJ`, and `TAG_DEF` localisation and all three flag sizes:

`IRE_IRELAND_ARMY_COUNCIL`, `IRE_IRELAND_CIVIL_REPUBLICAN`, `IRE_IRELAND_WORKERS_PARTY`, `IRE_IRELAND_WORKERS_SMALLHOLDERS`, `IRE_IRELAND_CORPORATE_ESTATE`, `IRE_IRELAND_ODUFFY_PERSONAL`, `IRE_IRELAND_CATHOLIC_GUARDIANS`, `IRE_IRELAND_GAELIC_CORPORATE`, `IRE_IRELAND_CHRISTIAN_NATIONAL`, `IRE_IRELAND_REGIONAL_AIS_EIRGHE`, `IRE_IRELAND_AIS_EIRGHE`, `IRE_IRELAND_HIGH_KING_SACRAL`, `IRE_IRELAND_HIGH_KING_CONSTITUTIONAL`, `IRE_IRELAND_PENTARCHY`, `IRE_IRELAND_FIVEFOLD_FEDERATION`, `IRE_IRELAND_OTHERWORLD_DOMINION`, `IRE_IRELAND_COMPACT_TWO_IRELANDS`, and `IRE_IRELAND_CONVERGENCE_ORDER`.

`ireland_sync_route_identity` clears prior route identity before setting the one selected cosmetic tag. Route cleanup clears the identity flags and cosmetic tag state rather than leaving a stale country name after a failed/archived route.

## Focus tree, family locks, AI, and final layout

`common/national_focus/ireland_focus_tree.txt` has `focus_tree = { id = ireland_focus_tree default = no }`, country gating for IRE, a generic continuous-focus fallback at `(50, 3000)`, and exactly three visible opening trunks:

- `ireland_state_still_defined` at `(-12,0)`;
- `ireland_economic_war_review` at `(0,0)`;
- `ireland_defence_estimates` at `(12,0)`.

The final source-level focus count and AI crosswalk are:

```text
focus_ids=218 focus_unique=218 focus_duplicate_ids=[]
ai_refs=718 ai_unique=218 ai_unknown=[]
```

The five public gateway focuses are:

- `ireland_republican_government` → democratic;
- `ireland_congress_reform_bridge` → Congress/communist;
- `ireland_oduffy_network_revival` → Blueshirt/fascist;
- `ireland_vocational_constitution` → producer-estate/oligarchic;
- `ireland_high_king_evidence_gate` → constitutional restoration.

Each gateway has the existing branch reveal gate, sets one family flag, and mutually excludes all four alternatives. No gateway lock was lost during the `89ff719` coordinate-only reflow. AI family programme depths are 18/23/25/21/21 for democratic/communist/fascist/oligarchic/restoration respectively, and all family-plan focus references resolve.

The read-only MCP focus inspection for `ireland_focus_tree` reports:

| Metric | Result |
| --- | ---: |
| Focuses / connectors | 218 / 226 |
| Bounds | x -26..21, y 0..22 |
| Column / row span | 47 / 22 |
| Connector crossings | 0 |
| Connector-through-node intersections | 0 |
| Long connectors | 0 |
| Duplicate coordinates / visible overlaps | 0 |
| Same-row pairs / too-close pairs | 195 / 0 |
| Minimum same-row spacing | 2 |
| Maximum horizontal / vertical connector span | 8 / 2 |
| Maximum Manhattan span | 9 |

The only Ireland-local focus diagnostic is the documented nonblocking two-column detour `ireland_clerical_failure_bridge -> ireland_clerical_guardianship`. Straightening it would cross the adjacent Congress corridor; the authored zero-crossing geometry was retained. The other MCP localisation warning is vanilla `continuous_restrict_freedom_desc`, outside this package. The final layout handoff is `docs/plans/ireland_country_package/subagent_handoffs/ireland_country_package_family_lane_reflow_completion_2026-08-14.md`.

Focus icons are wired through `interface/ireland_icons.gfx`, `interface/ireland_focus_shine.gfx`, and `interface/ireland_focus_expansion_shine.gfx`; all 218 custom focus icon references resolve to GFX definitions and existing 94x86 goal DDS files.

## Industrial concerns, MIOs, contracts, and material balance

`common/ideas/ireland_industrial_concerns.txt` contains exactly seven industrial concerns:

`ireland_company_electricity_supply_board`, `ireland_company_irish_sugar_company`, `ireland_company_turf_development_board`, `ireland_company_great_southern_railways`, `ireland_company_aer_lingus_air_link`, `ireland_company_irish_shipping_registry`, and `ireland_company_steel_holdings`.

`common/military_industrial_organization/organizations/ireland_organizations.txt` contains exactly two MIOs:

- `ireland_ford_cork_works_organization`;
- `ireland_harland_wolff_belfast_organization`.

Both MIOs use `allowed = { original_tag = IRE }`, route unlock flags, valid MIO `FROM = { ... }` visibility/availability scopes, resolved names/traits, and existing icon assets. The generic MIO trait icons are intentional vanilla fallbacks.

`common/decisions/ireland_expansion_decisions.txt` contains exactly nine one-use, 35-day contracts:

`ireland_contract_esb_grid_works`, `ireland_contract_transport_fleet`, `ireland_contract_merchant_tonnage`, `ireland_contract_state_materials`, `ireland_contract_ford_motor_works`, `ireland_contract_aer_lingus_transport`, `ireland_contract_turf_fuel_reserve`, `ireland_contract_steel_foundry`, and `ireland_contract_belfast_refit`.

Each uses `fire_only_once = yes`, `days_remove = @IRELAND_INDUSTRIAL_CONTRACT_DAYS`, a productive-civilian-factory availability gate, and a one-factory reservation (major contracts use the major reservation macro). Rewards are distinct and bounded: infrastructure/materials, motorized/trains, convoys, a state factory, motorized/army XP, transport aircraft/air XP, fuel, steel capacity, or Belfast dockyard/navy XP. There is no repeatable PP/material loop and no free core/major army reward. The remaining balance caveat is the separately documented 50-PP refund on five stale territorial diplomatic branches; the consumed manpower/equipment/convoy/fuel/command reserves remain spent.

## Territorial expansion, Northern question, Atlantic lifecycle, and cleanup

The territorial lane in `common/national_focus/ireland_focus_tree.txt` requires political-family commitment, Northern policy proof, foreign safeguards, provision conclusion, and readiness conclusion before `ireland_define_the_national_question`. `ireland_authorise_reunification_instruments` then opens exactly one family method:

- democratic `ireland_northern_plebiscite_guarantees` → supervised plebiscite;
- communist `ireland_workers_reunification_campaign` → workers campaign;
- fascist `ireland_ulster_ultimatum` → ultimatum/enforcement;
- oligarchic `ireland_customs_union_leverage` → Belfast Compact;
- restoration `ireland_crown_and_province_mandate` → Provincial Assent.

Settlement records are route-specific (`ireland_settlement_under_law`, `ireland_all_island_workers_republic`, `ireland_force_the_border_question`, `ireland_belfast_compact`, `ireland_restore_ulsters_place`) and do not grant automatic cores. Atlantic follow-up uses `ireland_atlantic_ambition`, the five route outcomes, and `ireland_enforce_atlantic_claims`; the focus prerequisite block for the latter is an intentional OR between `ireland_gaelic_marches` and `ireland_dal_riata_claim`, so no family is made unreachable.

`events/ireland_territorial_diplomacy_events.txt` defines 27 numbered territorial events. Acceptance branches transfer the event-target state; refusal/expiry branches add a claim and create a time-limited `take_claimed_state` wargoal. States 119/120/122/123 are the only target-state set observed. Every terminal branch calls `ireland_clear_territorial_diplomacy_targets` and clears pending flags. The Provincial Assent record option now requires Unionist Consent 25, Nationalist Consent 50, Royal Legitimacy 55, and Administrative Reach 70; adjournment is the legal incomplete path.

The decision lifecycle repairs in `docs/plans/ireland_country_package/subagent_handoffs/decision_audit_fixes_handoff_2026-08-14.md` remain present at `89ff719`:

- all timed country-flag durations use owning-file `@` literals rather than variables/fixed-point constants;
- P0 postwar, recovery, alternate-order, Congress rebuild, Provincial reconvene, and fascist withdrawal records occur from terminal `remove_effect`, not day-zero `complete_effect`;
- launch markers have `cancel_effect` cleanup and central route/archive cleanup;
- the fascist partial withdrawal records `ireland_northern_policy_selected` and is accepted by conclusion evaluation;
- no duplicate active mission/project path was found.

## Parliament initialization and scripted-GUI semantics

`common/scripted_effects/ireland_effects.txt` initializes the Parliament ledger once behind `ireland_initialized`, with:

- Dáil formal seats 153, routine votes 152, majority threshold 77;
- government formal/routine values 77/76, opposition formal 76, external support 0;
- Seanad formal seats 60, majority threshold 31, government 30, opposition 30;
- Parliament stage 1 and GUI-dirty state set at initialization.

`common/decisions/categories/ireland_categories.txt` exposes `scripted_gui = ireland_parliament_decision_ui` with `visible_when_empty = yes`, so the panel is available from the opening settlement category. `interface/ireland_parliament_scripted_gui.gui` defines four buttons whose names exactly match the scripted-GUI convention:

`ireland_parliament_dail_button`, `ireland_parliament_seanad_button`, `ireland_parliament_confidence_button`, and `ireland_parliament_budget_button`.

`common/scripted_guis/ireland_scripted_guis.txt` supplies matching `_click` effects and `_click_enabled` triggers. Dáil is the free day-one action; Seanad, confidence, and joint budget consume 25, 25, and 35 political power respectively, then mutate the corresponding live chamber/settlement ledgers. Trigger gates require the expected stage, focus/settlement state, ownership of state 113, and (where applicable) political power and chamber majorities. No button is a decorative dead click.

## Event cadence, report art, GFX, and localisation

`common/on_actions/ireland_on_actions.txt` uses `on_startup`, `on_daily_IRE`, and `on_monthly_IRE` scoped to IRE. The daily hook performs ledger, GUI, route, leader, mission, and cleanup synchronization; it does not directly fire the public programme. The monthly hook calls `ireland_dispatch_event_programme`, whose cursor, seen flags, route gates, and cooldown permit at most one player-facing programme event per Ireland monthly pulse. The narrow daily `ireland_events.433` conclusion follow-up is gated by the completed High King unity state and a one-shot seen flag. No unscoped whole-world daily/weekly event dispatch was found.

Report/event art crosswalk:

- 524 mod event `picture` references, 133 unique picture names, and no missing custom GFX definitions or textures;
- 134 custom event GFX definitions are wired in `interface/ireland_event_art.gfx` and `interface/ireland_sourced_assets.gfx`;
- 103 report DDS files are 210x176 and 19 news DDS files are 397x153;
- the 27 territorial events, postwar family `.1`–`.5` reports, and public conclusion events `.432`/`.433` have report/news art and localisation consumers.

The current English localisation audit (`docs/plans/ireland_country_package/subagent_handoffs/final_localisation_audit_2026-08-14.md`) reports 5,911 unique non-empty keys across the package English files, BOM-preserved files, complete 218 focus title/description coverage, decision/mission/event/GFX/Parliament coverage, and all 45 advisor plus seven concern/two MIO names. Seven unused defined-text helpers and four old Parliament tooltip copies remain documented future/legacy surfaces; they do not feed missing current references.

## Source-level ID, parser, and constant checks

The final focus/AI pass above was rerun after `89ff719`. The following source scans were performed before the coordinate-only commit and remain valid because that commit did not modify those surfaces:

- event definitions/references: 527/527, unknown event references 0;
- decision IDs/explicit decision references: 250/85, unknown decision references 0;
- scripted boolean effect/trigger definitions and calls: 135/553, unknown calls 0;
- fixed-point script constants: 831 definitions and 728 `constant:ireland.*` references, unknown references 0;
- custom character portrait, focus icon, company/MIO icon, and event picture GFX/texture crosswalks: no missing custom asset path;
- no `set_country_flag`, `set_global_flag`, or `set_state_flag` timed duration uses a variable or `constant:` token; the audited timed flags use file-local `@` literals.

The source checks found no unknown country tag, state, focus, event, decision, scripted helper, MIO, industrial concern, portrait, GFX, texture, or localisation identifier in the Ireland package. No parser-unsafe `<=`/`>=` script operators were introduced by the stable focus commit.

## Findings, blockers, and remaining risks

### Hard blockers

**None found in the requested Ireland country-package source surfaces.** The focus inspector reports no blocking diagnostics, and all exact requested package counts and cross-references pass.

### Nonblocking design/documentation risks

1. **Focus geometry warning:** `ireland_clerical_failure_bridge -> ireland_clerical_guardianship` remains a two-column linear detour. It is intentionally retained to preserve zero crossings; it is not a parser, reachability, or package-wiring blocker.
2. **Stale diplomatic refund policy:** five invalidated/stale territorial branches refund exactly 50 PP while material reserves stay spent. The current code comments/tooltips describe this as repayment of the initiating administrative charge, and one-use/cleanup gates prevent farming. It remains the only material balance policy worth parent review.
3. **Live validation boundary:** no live HOI4 launch, fresh save, timed-expiry playthrough, AI route run, or interactive Parliament click test was performed. The read-only MCP event lint was partial because its large workspace analysis deferred helper/lifecycle projections; it reported zero blocking diagnostics, but the source crosswalk remains authoritative. The focus inspection was complete for its structural checks and passed with the one warning above.
4. **Documentation staleness:** `baseline_completion_gap_audit_2026-08-14.md` and `final_decision_mission_audit_2026-08-14.md` contain historical/superseded gaps. `decision_audit_fixes_handoff_2026-08-14.md`, `final_localisation_audit_2026-08-14.md`, and the family-lane reflow handoff are the current evidence surfaces. This is documentation debt, not a gameplay defect.

## Files inspected

Primary package surfaces:

```text
history/countries/IRE - Ireland.txt
history/units/IRE_1936.txt
history/units/IRE_1939.txt
common/characters/ireland_route_characters.txt
common/countries/ireland_cosmetic.txt
common/national_focus/ireland_focus_tree.txt
common/ai_strategy/ireland_ai_strategy.txt
common/ai_strategy_plans/IRE_ireland_strategy_plans.txt
common/ideas/ireland_industrial_concerns.txt
common/military_industrial_organization/organizations/ireland_organizations.txt
common/decisions/ireland_decisions.txt
common/decisions/ireland_expansion_decisions.txt
common/decisions/categories/ireland_categories.txt
events/ireland_territorial_diplomacy_events.txt
events/ireland_public_conclusion_events.txt
common/on_actions/ireland_on_actions.txt
common/on_actions/ireland_public_conclusion_on_actions.txt
common/scripted_effects/ireland_effects.txt
common/scripted_effects/ireland_parliament.txt
common/scripted_effects/ireland_runtime.txt
common/scripted_triggers/ireland_parliament.txt
common/scripted_guis/ireland_scripted_guis.txt
interface/ireland_parliament_scripted_gui.gui
interface/ireland_event_art.gfx
interface/ireland_sourced_assets.gfx
interface/ireland_industrial_concerns.gfx
localisation/english/ireland_l_english.yml
```

Required offline Paradox wiki pages, repository skills, and relevant vanilla documentation were read before the audit. Vanilla state/history, country, scripted-GUI, event, decision, MIO, and script-constant precedents were consulted where syntax or engine scope mattered.
