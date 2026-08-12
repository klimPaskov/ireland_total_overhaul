# Three-opening-trunks focus audit

Date: 2026-08-12  
Feature slug: `ireland_focus_tree`  
Scope: read-only audit of opening visibility, `allow_branch` semantics, route/AI reachability, localisation, icons, and fresh MCP focus diagnostics. No gameplay files were edited.

## Verdict

The source implements the requested opening presentation: exactly three top-level focus roots without structural prerequisites or `allow_branch` visibility gates, three matching navigation shortcuts, and fifteen presentation-gated roots for staged/hidden families. The three roots are `ireland_state_still_defined`, `ireland_economic_war_review`, and `ireland_defence_estimates` (`common/national_focus/ireland_focus_tree.txt:36,95,131`).

The engine distinction is important. `available` controls whether a focus can be selected, while `allow_branch` controls whether the focus and inherited descendants are visible. The offline National Focus wiki states that `allow_branch` is evaluated at tree load and can be refreshed with `mark_focus_tree_layout_dirty`. Therefore the three opening roots remain visible on initial load, with Economic War and Defence Estimates unavailable until their existing `available` checks are satisfied. The seven newly staged ordinary families remain hidden until their exact gate checks become true. Ireland's country-scoped daily hook runs `mark_focus_tree_layout_dirty = yes` after the gate synchronizers (`common/on_actions/ireland_on_actions.txt:39`), so staged branches refresh without a reload on the next `on_daily_IRE` pass.

Fresh MCP evidence is clean for the Ireland national tree:

- `hoi4.focus_inspect` revision `c1112c666cadee8b6c76b13c32fb0be676a913de1fc2ffedc79971acce2bc225` reports 150 focuses, one tree, 150 connectors, zero crossings, zero connector-through-node intersections, zero long connectors, maximum horizontal span 6, maximum vertical span 2, zero spacing defects, and zero Ireland-local diagnostics. Artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8e37b3d8fcc978bbf66674414714882544fc5cff8323faf385d1767986d682e9/0b87357b7b1ecce8e9b5ace730122d922763cb6bc052ff602b2eb53bc3219d66/focus-inspect.c1112c666cadee8b.json`.
- `hoi4.focus_render` produced HTML, SVG, JSON, source-map, and plan artifacts with no Ireland diagnostic. HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ee6a4d45f14e1401fe57da668529551ca9f4c58d36ab67dd51bdcd96579d5dfa/02ae4744bb9e11afeb5d8d3c6b8fc6630ab21663fad312f433562866e0da5b64/ireland_focus_tree.focus.html`.
- `hoi4.focus_raster` produced a high-fidelity raster. Its nine blocking texture diagnostics are limited to vanilla continuous-focus DDS files that the offline decoder reports as truncated. No Ireland focus icon is implicated. Raster: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/45de2b378f88ba965124985864aa6c144e8bd01c7e8e3b49da05fbf74020d161/1743987d3a5ee74a1b84e2620d2408d79dc9aac1ffa692e80c53467159e391ab/ireland_focus_tree.focus.png`.

The MCP adapter reports `branchCount = 0`. This is an adapter limitation, not evidence that the authored shortcuts or `allow_branch` presentation gates are absent. The source and static checks below are the authoritative opening contract.

## Opening and reveal coverage

| Surface | Source evidence | Result |
| --- | --- | --- |
| Initial camera | `initial_show_position = { focus = ireland_state_still_defined }` at `common/national_focus/ireland_focus_tree.txt:22` | Correct opening anchor. |
| Opening shortcuts | `ireland_focus_shortcut_politics`, `ireland_focus_shortcut_industry`, `ireland_focus_shortcut_defence` at lines 29-31 | Exactly three. Localised labels resolve. |
| Ungated structural roots | `ireland_state_still_defined`, `ireland_economic_war_review`, `ireland_defence_estimates` at lines 36, 95, 131 | Exactly three roots without prerequisite or `allow_branch`. Their `available` blocks are selection gates, not visibility gates. |
| Newly staged ordinary roots | `ireland_cultural_survey` line 1290, `ireland_establish_naval_staff` line 1983, `ireland_strict_neutrality` line 2386, `ireland_northern_settlement_ledger` line 2574, `ireland_norton_parliamentary` line 1071, `ireland_clann_founding` line 1156, `ireland_vocational_constitution` line 1221 | All seven have `allow_branch` and are hidden until their own ordinary selection gates are met. |
| Concealed/exception roots | IRA line 2858, Congress line 3071, O'Duffy line 3217, clerical line 3374, Ailtirí line 3475, High King line 3605, Five Provinces line 3762, Otherworld line 3859 | All eight retain authored hidden-route reveal gates. |
| Total presentation gates | Seven newly staged ordinary roots plus eight concealed roots | Exactly fifteen `allow_branch` blocks. |

The initial visibility count is therefore three campaign trunks. No other root is exposed by an unconditional `allow_branch` or a missing prerequisite. Ordinary descendants inherit their root's hidden state, per engine semantics. The eight concealed families intentionally use narrower reveal predicates than their full `available` blocks, preserving hidden-route presentation while retaining the complete selection gate.

## Ordinary `allow_branch` versus `available` audit

The seven newly staged roots have matching presentation and selection predicates. This avoids a branch becoming visible while its selected focus is impossible, or remaining hidden after the complete gate is met.

| Root | `allow_branch` / `available` gate | Match | AI/deadlock check |
| --- | --- | --- | --- |
| `ireland_cultural_survey` | `ireland_replacement_charter`, `ireland_public_order_review`, `ireland_church_labour_consultation` | Exact | All are ordinary completed-focus gates. Cultural evidence descendants remain gated by their own flags. |
| `ireland_establish_naval_staff` | `ireland_port_defence_project`, `ireland_command_audit`, `ireland_readiness_plan` | Exact | Readiness plan is emitted by the readiness baseline contract. Historical AI queue completes port defence and command audit before this focus. |
| `ireland_strict_neutrality` | `ireland_readiness_baseline`, `ireland_treaty_port_transfer`, `ireland_active_neutrality` | Exact | Historical queue and route-reactive plan contain the three required predecessors. |
| `ireland_northern_settlement_ledger` | `ireland_national_settlement`, `ireland_treaty_port_transfer` | Exact | Treaty-port sovereignty is completed before the route-reactive Northern ledger. |
| `ireland_norton_parliamentary` | not route committed, alternate AI allowed, cultural survey, Labour organisation ready, government formation, Church/Labour consultation | Exact | Historical AI is excluded by `ireland_alternate_focus_ai_allowed`; non-historical route plan supplies Norton after government/consultation gates. |
| `ireland_clann_founding` | not route committed, alternate AI allowed, cultural survey, date after 1939-06-29, rural price board, election timetable | Exact | Date and ordinary predecessor gates are represented in the Clann route queue; historical AI is excluded. |
| `ireland_vocational_constitution` | not route committed, alternate AI allowed, cultural survey, vocational mandate ready, Church/Labour consultation, constitutional draft | Exact | Non-historical vocational profile supplies the queue; historical AI is excluded. |

No route deadlock was found in the static source pass. All 150 focus IDs are referenced by at least one Ireland AI focus plan, with no unknown focus IDs in those plans. Ordered `ai_national_focuses` entries are skipped when impossible, as documented by the offline wiki, so a gated root cannot block the AI indefinitely. Route profiles and `ireland_alternate_focus_ai_allowed` keep historical and alternate route selection distinct (`common/scripted_triggers/ireland_triggers.txt:39`, `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`).

The eight concealed roots are deliberately not exact copies of `available`: their `allow_branch` blocks expose only the reveal condition, while `available` adds route-commitment, evidence, date, and state-interface requirements. This is safe for presentation and preserves the full selection gate. Their descendants have no independent `allow_branch` overrides that would leak hidden content.

## Route coverage table

| Route family | Representative focus IDs | Audit result |
| --- | --- | --- |
| Government and constitutional politics | `ireland_state_still_defined`, `ireland_national_settlement`, `ireland_election_timetable`, `ireland_constitutional_draft`, `ireland_government_formation` | Present, visible opening trunk. |
| National development and Provision | `ireland_economic_war_review`, `ireland_rural_price_board`, `ireland_provision_baseline`, `ireland_food_ledger`, `ireland_energy_board`, `ireland_transport_priority`, `ireland_provision_conclusion` | Present, visible opening trunk with staged Provision root. |
| Defence and Readiness | `ireland_defence_estimates`, `ireland_command_audit`, `ireland_readiness_baseline`, `ireland_professional_army`, `ireland_air_warning`, `ireland_readiness_conclusion` | Present, visible opening trunk with staged readiness family. |
| Culture and evidence | `ireland_cultural_survey`, `ireland_archival_record`, `ireland_serious_cultural_stewardship`, `ireland_cultural_evidence_ledger` | Present, staged after constitutional/social prerequisites. |
| Diplomacy and neutrality | `ireland_active_neutrality`, `ireland_strict_neutrality`, `ireland_armed_neutrality`, `ireland_foreign_safeguards`, `ireland_neutrality_posture` | Present, staged strict-neutrality root. |
| Northern settlement | `ireland_northern_settlement_ledger`, `ireland_northern_local_authorities`, `ireland_northern_trade_corridor`, `ireland_northern_policy_proof` | Present, staged after Treaty Port transfer. |
| Marine Service/naval | `ireland_establish_naval_staff`, `ireland_rebuild_marine_service`, `ireland_requisition_trawler_hulls`, `ireland_coastal_patrol_flotilla`, `ireland_regional_maritime_defence_pact` | Present, staged after port/readiness/command authority. |
| Norton, Clann, vocational | `ireland_norton_parliamentary`, `ireland_clann_founding`, `ireland_vocational_constitution` | Present, each separately staged and route-committed on completion. |
| Concealed crisis/evidence routes | IRA, Congress, O'Duffy, clerical, Ailtirí, High King, Five Provinces, Otherworld roots listed above | Present and intentionally hidden until authored reveal conditions. |

## Icon coverage

| Surface | Result | Source |
| --- | --- | --- |
| Focus icon assignments | 150/150 focuses have unique `GFX_focus_ireland_*` assignments | `common/national_focus/ireland_focus_tree.txt` |
| Icon definitions | 150/150 icon names resolve | `interface/ireland_icons.gfx:3` and related definitions |
| Shine definitions | 150/150 matching `_shine` names resolve | `interface/ireland_focus_shine.gfx:6` and related definitions |
| Missing Ireland icon diagnostics | None in `hoi4.focus_inspect` or `hoi4.focus_render`; raster errors are vanilla continuous-focus DDS decode failures | Fresh MCP artifacts above |

## Localisation and reward mismatch list

Static localisation scan found 150/150 title keys and 150/150 description keys in UTF-8 with BOM (`localisation/english/ireland_l_english.yml`). The three shortcut labels resolve at lines 4111-4113. No focus title/description or shortcut mismatch was found.

No ordinary staged root has a name or description that contradicts its gate. The cultural, naval, neutrality, Northern, Norton, Clann, and vocational descriptions match their respective route identities. The Northern focus explicitly states that its claim does not grant control, occupation, integration, or cores, which matches its reward.

The staged roots are mainly gateway/state contracts, so several completion rewards intentionally set flags rather than grant a direct factory or unit. This is not a localisation mismatch, but it is a player-facing reward-depth risk inherited from the broader tree. The strongest concrete staged reward is `ireland_establish_naval_staff`, which creates the Coastwatch intelligence agency when needed, grants naval/army experience, and adds a technology bonus. `ireland_strict_neutrality` has a matching `ireland_strict_neutrality_reward_tt` key. `ireland_northern_settlement_ledger` claims state 119 and its description explicitly explains the non-annexation contract.

No focus-localisation or icon changes are required from this audit.

## AI behavior gaps and remaining risks

- No opening-root AI deadlock found. Historical and route-reactive queues contain the three trunks and all staged routes as ordered candidates, while alternate political roots use `ireland_alternate_focus_ai_allowed` and route-specific profile plans.
- No unknown or orphaned AI focus references found. Static coverage is 150/150 focus IDs referenced by the Ireland AI-plan surface.
- The MCP focus adapter cannot infer semantic branch families and reports `branchCount = 0`. Keep this limitation explicit in future review rather than treating it as a source failure.
- The raster adapter reports nine vanilla continuous-focus texture decode errors and one generic continuous-focus localisation warning (`continuous_restrict_freedom_desc`). These are outside the Ireland tree and should not be fixed in this task.
- `initial_show_position` centers the camera on the shared political root. The three roots are available as shortcuts and visible cards, but the current authored coordinates span `x = -30..52`; a future player-scale camera review may decide whether the three root cards fit in one unzoomed viewport. MCP structural diagnostics are clean, so this is a presentation-risk note, not a route or syntax defect.
- Concealed-root reveal timing depends on the existing daily scoped hook. If a future gate is changed to a non-daily effect, it must retain an explicit `mark_focus_tree_layout_dirty` refresh.

## High-priority fixes

1. **No gameplay fix required for this audit.** The three opening roots, three shortcuts, fifteen presentation gates, ordinary gate matching, route AI coverage, localisation, and icon references are all internally consistent.
2. Keep `common/on_actions/ireland_on_actions.txt:39` layout refresh after hidden/staged gate synchronizers. Removing or moving it would make `allow_branch` visibility stale until reload.
3. Treat the nine raster vanilla DDS errors and generic continuous-focus localisation warning as out of scope. Do not change Ireland assets or localisation to mask them.
4. If the parent wants a separate viewport pass, inspect the three-root camera at target UI scale. Do not alter prerequisites or `allow_branch` gates for a cosmetic camera issue.

## Validation and skipped checks

Meaningful checks completed:

- Offline Paradox National Focus wiki and required core wiki pages read, including `allow_branch`, `available`, prerequisites, focus layout, AI focus plans, localisation, and icon semantics.
- Vanilla `allow_branch` precedents inspected in USA focus files.
- Fresh `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster` runs against the latest source.
- Static parser confirmed exactly 150 focus blocks, exactly three no-prerequisite/no-`allow_branch` roots, exactly fifteen `allow_branch` blocks, and exact matching predicates for all seven newly staged ordinary roots.
- Static localisation check confirmed 150/150 title and description keys plus three shortcut labels, all with UTF-8 BOM.
- Static icon check confirmed 150/150 unique Ireland focus icons, definitions, and shine definitions.
- Static AI-plan check confirmed all 150 focus IDs referenced and no unknown focus IDs.

Skipped: live-game scenario execution and human UI viewport inspection. The parent guidance says live verification is performed by the user, and no game process was available for this read-only audit. The fresh MCP structural and raster evidence is included so the parent can review the non-live result.

## Files changed

Only this handoff was added:

- `docs/plans/ireland_focus_tree/subagent_handoffs/three_opening_trunks_audit_2026-08-12.md`

Gameplay source, AI, localisation, icons, and on-actions were not edited.

