# Final Ireland focus-tree audit — 2026-08-14

## Verdict

**Superseded by the corrective closure below.** This section records the read-only audit of `89ff719`; it is not the final source verdict.

The stable commit `89ff719` is structurally healthy and its reflowed programme
lanes are layout-clean, but the five public family gateways do not satisfy the
committed “one row directly below National Settlement” contract. There are also
strict filter-parity and helper-only reward findings that should be resolved or
explicitly waived before calling the tree complete. No gameplay source, asset,
or thumbnail was changed by this audit.

## Scope and references

- Audited commit: `89ff719` (`Compact Ireland political family lanes`).
- Focus source: `common/national_focus/ireland_focus_tree.txt`.
- Read `AGENTS.md`, `hoi4-focus-trees`, `hoi4-subagents`,
  `hoi4-decisions-missions`, `hoi4-feature-assets`, `hoi4-events`, and
  `hoi4-improvement-loop` skills.
- Consulted the required offline wiki pages for data structures, triggers,
  effects, modifiers, localisation, scopes, on actions, events, decisions,
  ideas, AI, and national focuses, plus the relevant vanilla script and
  focus/documentation references.

## Fresh MCP evidence

Fresh `hoi4.focus_inspect` (`ireland_focus_tree`, `nodeSpacing = 2`,
`laneSpacing = 2`) reported:

| Metric | Result |
| --- | ---: |
| focuses | 218 |
| connectors | 226 |
| bounds | x = -26..21, y = 0..22 |
| connector crossings | 0 |
| connector-through-node intersections | 0 |
| long connectors | 0 |
| duplicate coordinates | 0 |
| same-row pairs / cramped pairs | 195 / 0 |
| minimum same-row spacing / required | 2 / 2 |
| max horizontal / vertical connector span | 8 / 2 |
| total horizontal / vertical span | 248 / 230 |
| sibling cohort asymmetry | 0 / 0 |
| local linear detours | 1 warning |

The one nonblocking detour is
`ireland_clerical_failure_bridge` -> `ireland_clerical_guardianship`
(source lines 3829–3848, span 2 horizontally and 1 vertically). Straightening
it forces a crossing with the adjacent Congress corridor, so the committed
zero-crossing geometry is preferable. The other MCP warning is the unrelated
vanilla localisation reference `continuous_restrict_freedom_desc`.

Inspect artifact:

`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/85dbe6e42347983c81724e69887fc612cc2c93f8e6a99d996e2a56a0a7a41e30/c3be345607e9046da94518ce45eaaf230c3be8dc4d72ad05de771273e55f7056/focus-inspect.ea067e4f28da98eb.json`

Fresh `hoi4.focus_render` (`horizontalSpacing = 96`, `verticalSpacing = 130`,
`padding = 2`, `reviewScale = 1`) rendered 4660 x 2940. Review artifacts:

- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/05cd7aa34cf3665992d21be1e785a8272a18cd80b33a7cd54e1e54fef5f4daec/be66a133d40333619eea6ca579e2d0d1fcc8280aebe87e174d27012bdc95a6ae/ireland_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/777367dd9e9d8260b3b654518fa10f08b17133808821523092a89e546c4cf1e3/8621011f857d7060ba6ecb1b3222ebd83c07f4132889a751736c46b1c3a6e9fb/ireland_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/27037a9e95893b46c47f7fd61e43e08dfa13005ab9ccf64adf58769f27da231f/f967d18082f2fa3f556b9685cd042e7d6e278fa843de13aee4f508bb313a6727/ireland_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/edc16fc3d9c5fd55eb2183c63e76c22a0f2dcab205a6995ee5941215a50d90ea/a06edbecfada465617173e324809bc1da8568b832db8e9d8135c22b19e6e8e43/ireland_focus_tree.focus.source-map.json`

## Route coverage

| Contract surface | Source coverage | Audit result |
| --- | --- | --- |
| Three visible opening roots | `ireland_state_still_defined` (-12,0), `ireland_economic_war_review` (0,0), `ireland_defence_estimates` (12,0) | **PASS**; exactly 3 roots without a reveal gate. |
| Shared settlement/reveal | `ireland_national_settlement` sets `ireland_political_routes_revealed` and `ireland_territorial_lane_revealed`, then refreshes layout | **PASS**. |
| Five public families | Democratic `ireland_republican_government`; Congress `ireland_congress_reform_bridge`; Blueshirt `ireland_oduffy_network_revival`; producer-estate `ireland_vocational_constitution`; restoration `ireland_high_king_evidence_gate` | **PASS** for flags, pairwise exclusions, and route-specific availability; **FAIL** for the required common gateway row (see blocker). |
| Family programme islands | `ireland_republican_ministries`, `ireland_vanguard_organisers`, `ireland_veterans_command_council`, `ireland_creditor_cabinet`, `ireland_claimants_convention` at (-24,-18,-12,-6,0; y=18), with descendants on y=19..22 | **PASS** for clean parallel lanes and centered spacing. |
| Northern/Atlantic campaign | `ireland_unfinished_national_question` -> `ireland_border_and_atlantic_dossier` -> `ireland_test_the_state_instruments` -> `ireland_define_the_national_question` -> `ireland_authorise_reunification_instruments`; five methods, five outcomes, Atlantic policy, enforcement, postwar review, conclusion | **PASS** for visible depth and connected source path. |
| Territorial scope | Northern state 119; Highland 120; Wales 122; Cornwall 123 | **PASS**; no automatic external cores or full-army grant found. |
| Atlantic settlement gate | `ireland_atlantic_settlement_concluded` has an OR prerequisite over the three policy cards but `ireland_atlantic_settlement_all_relevant_resolved = yes` in `common/scripted_triggers/ireland_triggers.txt:4778` enforces every relevant holding/subject obligation | **PASS**; OR is convergence, not a bypass. |
| Hidden/extreme routes | 28 `allow_branch` blocks, including family reveal, territorial reveal, and permission-gated Ailtirí/five-province/otherworld branches | **PASS**; no hidden route is exposed as an ordinary opening root. |

## Required blocker: public gateway band and branch centering

The committed architecture requires all five public gateways on one centered row
directly below Settlement. The actual gateway coordinates are:

| Family | Focus | Source line | Actual coordinate |
| --- | --- | ---: | ---: |
| Democratic | `ireland_republican_government` | 461 | (-16,4) |
| Congress | `ireland_congress_reform_bridge` | 3450 | (-12,3) |
| Producer-estate | `ireland_vocational_constitution` | 1361 | (-8,7) |
| Blueshirt | `ireland_oduffy_network_revival` | 3618 | (-6,10) |
| Restoration | `ireland_high_king_evidence_gate` | 4033 | (-4,4) |

They are mutually exclusive and reveal correctly, but they are not a single
post-Settlement band. This is a contract-level visual/navigation failure even
though MCP reports zero geometric crossings. The reflowed programme roots are
clean; they do not repair the gateway band. In addition,
`ireland_blueshirt_patronage_board` (line 4957, (-4,11)) remains in the old
O'Duffy corridor instead of the fascist programme lane rooted at (-12,18), so
the family advisor branch is visually detached from the otherwise centered
programme island.

## Territorial route and reward audit

The territorial lane is substantially implemented and localized:

- evidence/preparation: `ireland_unfinished_national_question`,
  `ireland_border_and_atlantic_dossier`, `ireland_test_the_state_instruments`;
- gateway/authorization: `ireland_define_the_national_question`,
  `ireland_authorise_reunification_instruments`;
- methods: `ireland_northern_plebiscite_guarantees`,
  `ireland_workers_reunification_campaign`, `ireland_ulster_ultimatum`,
  `ireland_customs_union_leverage`, `ireland_crown_and_province_mandate`;
- outcomes: `ireland_settlement_under_law`,
  `ireland_all_island_workers_republic`, `ireland_force_the_border_question`,
  `ireland_belfast_compact`, `ireland_restore_ulsters_place`;
- Atlantic policies: `ireland_atlantic_security_compacts`,
  `ireland_republics_across_the_channel`, `ireland_gaelic_marches`,
  `ireland_atlantic_concessions`, `ireland_dal_riata_claim`;
- enforcement/postwar: `ireland_enforce_atlantic_claims`,
  `ireland_postwar_settlement_office`, `ireland_local_rights_charter`,
  `ireland_protectorate_statutes`, `ireland_integration_review_commission`,
  `ireland_atlantic_settlement_concluded`.

Direct route payoffs are present for the evidence, method, policy, enforcement,
and postwar stages: XP, command power, support-tech bonus, equipment, named
decision unlocks, state-120 claims for the two bounded claim routes, staged
Wales/Cornwall/Highlands decisions, and per-holding settlement decisions.
Relevant tooltips explicitly describe refusal, no automatic core, and paid or
staged operations.

The following outcome/reveal cards are helper-heavy and should be reviewed
against the concrete-payoff rule in `territorial_campaign.md`:

- `ireland_settlement_under_law` (line 5332; custom tooltip plus two ledger flags);
- `ireland_all_island_workers_republic` (custom tooltip plus two ledger flags);
- `ireland_belfast_compact` (custom tooltip plus two ledger flags);
- `ireland_restore_ulsters_place` (custom tooltip plus two ledger flags); and
- `ireland_atlantic_ambition` (custom tooltip plus the Atlantic reveal flag).

These are meaningful persistent resolution/reveal markers and their tooltips
name the ledger or policy they feed, but they do not themselves grant a new
operation, material grant, or institution. Treat them as P1 reward-depth
follow-ups unless the source-of-truth spec explicitly accepts convergence cards
as a capability handoff.

## Strict filter parity findings

XP and research metadata are internally consistent: every Army/Navy/Air XP
filter has a corresponding direct XP effect, and every Research filter has a
direct technology, doctrine, or research-speed effect. The following are
verified strict-direct-effect risks because their completion rewards contain no
literal construction, production, company/MIO, infrastructure, or industrial
contract effect despite `FOCUS_FILTER_INDUSTRY`:

`ireland_economic_war_review` (129), `ireland_rural_price_board` (153),
`ireland_1938_trade_settlement` (363), `ireland_lemass_developmental` (735),
`ireland_lemass_developmental_capstone` (801), `ireland_provision_baseline`
(1543), `ireland_food_ledger` (1570), `ireland_transport_priority` (1631),
`ireland_maritime_reserve` (1654), `ireland_rural_credit` (1712),
`ireland_emergency_stockpiles` (1741), `ireland_producer_accounting` (1837),
`ireland_northern_trade_corridor` (2961), `ireland_material_conclusion_proof`
(3190), `ireland_producer_constitution` (3849),
`ireland_motorised_command_contracts` (4696), `ireland_industrial_syndicates`
(4769), `ireland_rural_producer_boards` (4788),
`ireland_customs_union_leverage` (5309), and `ireland_belfast_compact` (5391).

Several unlock downstream operations or grant equipment/fuel/research, but the
committed filter rule is direct-effect metadata; a downstream decision unlock
does not automatically make the focus an Industry card. Two focuses likewise
carry `FOCUS_FILTER_ANNEXATION` without a direct claim, war goal, transfer, or
territorial operation in their completion reward:

- `ireland_define_the_national_question` (5241); and
- `ireland_authorise_reunification_instruments` (5263).

`ireland_creditor_cabinet` (4742) carries `FOCUS_FILTER_POLITICAL_CHARACTER`
but only sets `ireland_industrial_contracts_open` and political power; it does
not set an advisor-pool flag. Remove that filter or add the intended character
capability. These are source-level parity findings, not MCP layout errors.

## Advisor, company, and MIO crosswalk

The unlock chain is wired, primarily through flags and scripted triggers:

- family programme/advisor flags are set in focus lines 4478, 4571, 4659,
  4937, 4953, 4967, 4983, and 4999;
- advisor availability/cleanup consumes these in
  `common/scripted_triggers/ireland_triggers.txt:4562–4664` and
  `common/characters/ireland_route_characters.txt`;
- company flags set at focus lines 5016, 5037, 5054, 5071, 5090, 5109, 5133,
  5151, and 5175 are consumed by
  `common/ideas/ireland_industrial_concerns.txt` and
  `common/decisions/ireland_expansion_decisions.txt`;
- Ford Cork and Harland & Wolff use `show_mio_tooltip` and `mio:` blocks at
  focus lines 5090–5092 and 5175–5179, with organizations defined in
  `common/military_industrial_organization/organizations/ireland_organizations.txt`.

No missing advisor/company/MIO identifier was found in this crosswalk. The
indirect flag-based design is consistent with the existing runtime, but it is
why character/company capability effects must remain documented in tooltips.

## Localisation and icon coverage

| Surface | Result |
| --- | ---: |
| focus IDs | 218, unique |
| focus title keys | 218 / 218 |
| focus description keys | 218 / 218 |
| custom focus tooltip references | 218 / 218 resolved |
| regular focus icons | 218 / 218 registered |
| shine icons | 218 / 218 registered in `interface/ireland_focus_shine.gfx` |
| duplicate Ireland localisation keys | 0 |

No icon, shine, title, description, or Ireland tooltip localisation blocker was
found. The unrelated vanilla continuous-focus warning is recorded above.

## AI, reachability, and terminals

- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` contains all 218
  focus IDs, with 36 Ireland plans including historical, reactive, five family
  programme profiles, route profiles, and postwar conclusion handling.
- Direct focus-local `ai_will_do` exists on 28 focuses; the remaining 190 are
  plan-driven. This is not a missing-reference failure, but any future gateway
  reflow must preserve the plan IDs and profile flags because route behavior is
  not encoded locally on every focus.
- The historical plan explicitly zeros Atlantic/extreme focus factors, while
  family plans provide route-specific factors for the territorial method and
  Atlantic policy cards. No missing AI focus reference was found.
- The source parser reports 16 structural no-prerequisite roots, but only the
  three opening roots are visible without `allow_branch`; the other roots are
  reveal-gated family, hidden, territorial, or postwar branches. This is
  expected progressive disclosure, not 13 additional opening trunks.
- There are 60 structural leaves. They are mostly named route capstones,
  conclusion/support projects, or policy terminals. No orphan focus ID was
  found; the unresolved issue is visual family-gateway placement, not a dead
  source reference.

## Priority follow-up

1. Resolve the public gateway band: reflow the five gateway cards and their
   direct descendant corridors as one authored pass, keeping the clean MCP
   geometry; bring `ireland_blueshirt_patronage_board` into the fascist lane or
   document why it is intentionally shared/legacy.
2. Decide strict filter policy and correct the 20 Industry candidates, the two
   Annexation gateway filters, and the `ireland_creditor_cabinet` character
   filter. Downstream decision unlocks should only count if the source contract
   explicitly defines them as direct capability metadata.
3. Give the four Northern outcome cards and `ireland_atlantic_ambition` a named
   persistent capability/operation or explicitly mark them as accepted ledger
   convergence cards in the source spec.
4. Re-run focus inspect/render after any coordinate change and preserve the
   current zero-crossing result.

## Files and validation

Only this handoff file was added. No gameplay file, interface file, localisation
file, asset, or `thumbnail.png` was edited; no commit was created. Validation
was limited to fresh `hoi4.focus_inspect`, fresh `hoi4.focus_render`, source
parsing/crosswalk checks, and read-only `rg` inspections. A live game session,
AI simulation, and raster thumbnail comparison were not run; running them was
outside this read-only audit and the existing user thumbnail was preserved.

## Corrective closure after the audit

The findings were resolved in the subsequent authored pass:

- all five public family gateways now share row `y = 14`, ordered and centered at x `-24, -18, -12, -6, 0` for democratic, communist, oligarchic, fascist, and restoration;
- four redundant visible prerequisite connectors were removed because every former prerequisite remains an explicit `available` requirement and the Settlement reveal flag remains authoritative;
- each gateway's profile corridor was moved beneath it, the substantive programme roots remain aligned on row `y = 18`, and `ireland_blueshirt_patronage_board` is inside the fascist corridor at `(-4,15)`;
- 20 unsupported Industry filters, two unsupported Annexation filters, and the unsupported `ireland_creditor_cabinet` character filter were removed; XP and Research parity remains intact; and
- the four Northern settlement cards and `ireland_atlantic_ambition` are explicitly accepted in the source spec as persistent settlement/policy capability handoffs, avoiding arbitrary material gifts on constitutional resolution cards.

Fresh inspection revision `97013150a7474f29` reports 218 focuses, 222 connectors, bounds x `-26..21` / y `0..22`, zero crossings, node intersections, long connectors, duplicate coordinates, or spacing defects, and maximum connector span 6 columns / 2 rows. The remaining detour/staircase advisories are nonblocking concealed corridors outside the five public family band.

Artifact:

`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/cef93413019260f758c5bd8c1d6cd3ba02f4105da571f2ecf98b759c39ce3e00/ff8b072165eb89950c5dcac511e230c7e1ee962b90a7b2a985ec6e815fd8eb5a/focus-inspect.97013150a7474f29.json`

Final verdict after correction: **COMPLETE for the static focus-tree contract.**
