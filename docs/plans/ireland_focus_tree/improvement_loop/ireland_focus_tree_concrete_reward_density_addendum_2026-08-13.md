# Ireland Focus Tree Concrete Reward Density Addendum

Feature slug: `ireland_focus_tree`

Date: 2026-08-13

Status: implemented and promoted on 2026-08-13

Implementation disposition: the stable source meets the target bands with 32
material/construction/fuel focus IDs, 24 capability focus IDs, 59 focus IDs
with named decision or mission unlocks, and a usable opening Dáil action. The
canonical outcome is recorded in the focus-tree index, Part 2, the reward
contract, source-of-truth map, and 2026-08-13 completion report.

## Decision and prior-plan disposition

Another broad route or another focus batch would be bloat. Keep the existing
150 focus IDs, exactly three opening roots, and the current hidden-route reveal
model. The remaining problem is reward semantics: a unique tooltip can explain
a ledger change, but explanation alone does not turn that change into
equipment, industrial capacity, military preparation, a usable decision, or a
new capability.

The 2026-08-11 Parliament correction addendum was implemented and promoted
before the user reopened this issue under a stricter standard. It is therefore
not an unresolved duplicate. The concurrent 2026-08-13 tranche already:

- gives all 150 focuses focus-specific reward tooltips;
- compresses the authored tree from x `-30..52` to a 41-column x span, retaining
  y `0..16` and exactly three opening roots;
- retains 150 connectors with zero crossings, connector-through-node
  intersections, or long connectors; and
- shows the Parliament powers panel and four locked controls from campaign
  initialization.

Those changes are the baseline for this addendum and must not be redone.

## Evidence and the remaining gap

The implemented source has 150 focus-specific `custom_effect_tooltip` calls.
The accepted reward pass expanded the direct and playable inventory to:

| Direct effect in focus rewards | Current calls |
| --- | ---: |
| focus IDs with material, construction, or fuel | 32 |
| focus IDs with research, doctrine, agency, or event capabilities | 24 |
| focus IDs with named decision or mission unlocks | 59 |
| `create_intelligence_agency` | 1 |
| `country_event` | 1 |
| named unlock calls / existing decision and mission IDs | 60 / 58 |
| `create_unit` | 0 |
| `set_technology` | 0 |

The material pass is documented in `docs/ireland_material_focus_rewards.md`.
It covers trucks, trains, convoys, factories, infrastructure, fuel, rifles,
support equipment, radar, anti-air, and the Marine Service. Political,
cultural, foreign, Northern, and exceptional-route focuses use named playable
procedures, branch commitments, institutional profiles, and conclusion reviews
instead of receiving arbitrary factories or equipment.

Final focus inspection evidence is maintained in
`docs/plans/ireland_focus_tree/focus_parliament_reward_density_completion_2026-08-13.md`.

The final compact layout preserves the three opening trunks and has no
crossing, connector-through-node, long-connector, or same-row spacing defect.

## Design rule: a focus must deliver or enable something

Every focus keeps its route flags, ledgers, recompute calls, and conclusion
records as backend state. At least one player-facing primary consequence must
also satisfy one of these classes:

1. **Material delivery:** equipment, fuel, convoys, trains, or aircraft.
2. **Physical capacity:** factory, dockyard, infrastructure, air base, radar,
   anti-air, fortification, railway, supply node, or state resource.
3. **Military capability:** technology bonus, doctrine bonus, XP, template,
   unit-training decision, agency/branch, advisor, manufacturer, or equipment
   subsidy.
4. **Playable programme:** a named decision or mission becomes visible and
   usable, with a real cost, executor, AI path, result, and cleanup lifecycle.
5. **Institutional capability:** a named law, office, advisor, route-specific
   idea, diplomacy action, settlement procedure, or conclusion review becomes
   usable. A flag is not the visible reward; it is only the implementation gate
   behind the named capability.

No focus may use a flag, variable, recompute helper, reveal helper, review
helper, generic political power, stability, or war support as its only primary
payoff. Route and proof focuses are not exempt: they must visibly unlock the
next playable procedure or install a named institution.

## Target reward mix

The categories overlap; a project focus may deliver equipment and unlock a
mission.

| Measure | Acceptance target |
| --- | ---: |
| 150-ID reward manifest with one primary class per focus | 150 / 150 |
| focus IDs with direct material or physical-capacity effects | 32–40 |
| focus IDs with named decision or mission unlocks | 45–60 |
| focus IDs with technology, doctrine, advisor, agency, template, or manufacturer capabilities | 24–36 |
| free unit creation | 0 in focuses; maximum 3 route-exclusive trained units through paid decisions |
| focuses whose only payoff is a flag/variable/helper | 0 |
| simultaneous focus-created national spirits | no more than 3 |

This density is deliberately below one factory or equipment bundle per focus.
Political, cultural, diplomatic, Northern, and concealed routes should mostly
open procedures and capabilities; the development and defence trunks carry the
physical deliveries.

## Exact balance bands

All values below include current 2026-08-13 deliveries. Use shared script
constants where the effect field supports `constant:`; otherwise use a
file-local `@` tuning table. Do not duplicate the same number in focus,
tooltip, decision, and AI sources.

### Material delivery bands

| Reward | Minor | Standard | Major / capstone ceiling |
| --- | ---: | ---: | ---: |
| infantry equipment | 250 | 500 | 750 |
| support equipment | 25 | 50 | 100 |
| artillery | 15 | 25 | 50 |
| motorized equipment | 25 | 50 | 100 |
| trains | 2 | 5 | 10 |
| convoys | 5 | 10 | 15 |
| early aircraft or airframes | 5 | 10 | 15 |
| fuel | 250 | 500 | 1,000 |

- One focus may contain one standard bundle or two complementary minor
  deliveries. Reserve major bundles for a 70-day route milestone.
- A normal historical/plausible path should receive no more than 1,500 rifles,
  200 support equipment, 100 artillery, 150 trucks, 10 trains, 30 convoys, and
  20 aircraft from focuses before 1941, excluding paid procurement decisions.
- Aircraft and tank deliveries must use the vanilla DLC-aware archetype split
  and identify a producer. Do not grant advanced equipment without its
  technology or a historically intelligible foreign source.

### Industrial and defence caps

Across all mutually compatible common focuses, including current Marine
rewards, cap instant focus construction at:

- 3 civilian factories;
- 2 military factories;
- 2 dockyards;
- 2 infrastructure levels outside later paid projects;
- 1 air-base level;
- 2 radar levels total;
- 2 state anti-air levels total; and
- one coastal-fort level in each named Irish coastal state.

Alternative ideological routes may replace, relocate, or convert capacity but
must not stack another complete industrial package. Always test free slots and
owned/control state. Prefer Leinster (`113`) for government/armament capacity,
Connaught (`134`) for western transport and turf projects, and Munster (`135`)
for food, Cork, Cobh, shipping, and Marine projects. Northern Ireland (`119`)
receives no free Irish construction until its settlement/administration
lifecycle has lawfully transferred control.

### Training and research bands

- XP: 5 minor, 10 standard, 15 major, 25 absolute capstone ceiling.
- Technology bonuses: one 50% use for an ordinary focus; two 50% uses only on
  a late 70-day programme. Do not use a research speed value as a substitute.
- Instant technology: none by default. Permit one foundational technology only
  where the route would otherwise unlock an unusable template or building, and
  record the reason in the reward manifest.
- Paid unit decisions consume the exact manpower and equipment used by their
  `create_unit` result. No free divisions from a focus and no repeatable unit
  loop.
- Decision PP bands: 15 minor, 25 standard, 35 major, 50 exceptional.
- Mission duration bands: 35 days emergency, 70–90 days ordinary project,
  120–180 days strategic programme.

## Implementation-critical reward map

These are required representatives, not optional examples. The implementer
should assign the remaining IDs in each family the same class discipline in
the 150-row manifest.

### Three opening trunks and Parliament

| Focus / phase | Required primary consequence |
| --- | --- |
| campaign initialization | Show all four Parliament controls; stage one is current, not merely hidden or inert. `ireland_parliament_dail_action_current` must not require `ireland_settlement_open`. Keep Dublin control, completion, archive, and PP gates. |
| `ireland_state_still_defined` | Gateway exception: visibly unlock the constitutional-government programme and its named action family. No generic PP bundle. |
| `ireland_national_settlement` | Require the completed opening Dáil sitting and unlock the six-month settlement review/programme actions through real decision visibility plus `unlock_decision_tooltip`. Do not remain the gate that makes the first Parliament control exist. |
| `ireland_constitutional_draft` | Unlock the constitutional drafting/plebiscite lifecycle and release the confidence-compact Parliament stage. |
| `ireland_government_formation` | Unlock government-formation actions and release the joint-budget Parliament stage. |
| `ireland_election_timetable` | Activate or unlock `ireland_mission_conduct_a_free_general_election`; show duration and success/failure consequences. |
| `ireland_economic_war_review` | Unlock the 1938 trade-negotiation programme and give one 50% industry research bonus. |
| `ireland_rural_price_board` | Unlock `ireland_action_set_agricultural_prices` and the county tillage programme; use a named board capability, not a price-ledger delta alone. |
| `ireland_defence_estimates` | Deliver 250 rifles and 25 support equipment, 5 army XP, and unlock the first command/procurement action family. |
| `ireland_command_audit` | Keep bounded XP, add one 50% land-doctrine or support-technology bonus, and unlock `ireland_action_run_a_command_district_exercise`. |

Parliament keeps the existing shared executors, native AI decisions, costs
`15/25/25/35`, and four-state seals. The complete lifecycle is:

1. initialization: Dáil action current and usable if Ireland controls Dublin
   and has 15 PP;
2. completed Dáil sitting: `ireland_settlement_open` is recorded and
   `ireland_national_settlement` can proceed;
3. National Settlement focus: Seanad support stage becomes current;
4. Constitutional Draft focus plus prior stages: confidence compact becomes
   current;
5. Government Formation focus plus chamber majorities: joint budget becomes
   current; and
6. final completion/archival: controls retain green historical state until the
   category is lawfully archived.

The native decisions must use the same gates as their GUI controls. The opening
Dáil decision is human-visible; later native steps remain AI-facing. Do not
create a fifth button, another Parliament category, a parallel executor, or a
preview-only decision.

### Development and provision

| Focus | Required concrete payoff |
| --- | --- |
| `ireland_provision_baseline` | Unlock the four provision project groups—food, energy, transport, maritime—with decision tooltips. |
| `ireland_food_ledger` | Unlock tillage, seed distribution, mills/storage, and livestock actions; one 50% agriculture/industry bonus if the relevant category exists. |
| `ireland_energy_board` | 500 fuel plus one Connaught infrastructure level, or a one-use 50% synthetic-resource bonus if the infrastructure cap is already reached. |
| `ireland_transport_priority` | Retain 25 trucks and 2 trains; unlock the named Dublin–Cork corridor mission. |
| `ireland_maritime_reserve` | Raise the current delivery to the standard 10-convoy band only if the route-wide 30-convoy cap remains respected; unlock charter/purchase vessel actions. |
| `ireland_domestic_manufacturing` | Retain one civilian factory; add one 50% production/industry bonus and unlock the protected-workshop/developmental-plant programme. |
| `ireland_rural_credit` | Unlock western portfolio, emergency housing, and cooperative project decisions; do not add another flat ledger increment as the primary reward. |
| `ireland_emergency_stockpiles` | Raise the current 300 rifles/50 support equipment to 500/50, or add 25 artillery instead of extra rifles after balance simulation. |
| `ireland_development_authority` | Retain one infrastructure level and unlock `ireland_action_fund_a_western_regional_portfolio`. |
| `ireland_social_cooperatives` | Unlock emergency housing and the cooperative programme; on successful mission completion, construct the capacity rather than granting it immediately. |
| `ireland_producer_accounting` | One 50% industry bonus and a visible producer-accounting institution/decision, not only a proof flag. |
| `ireland_provision_conclusion` | Retain one civilian factory, permanently unlock the conclusion/recovery review, and stop; do not add another universal capstone bundle. |

### Defence, Coastwatch, air warning, and Marine Service

| Focus | Required concrete payoff |
| --- | --- |
| `ireland_readiness_baseline` | Unlock command, equipment, reserve, local-force, Coastwatch, harbour, patrol, and G2 action groups. |
| `ireland_readiness_command` | Retain 200 rifles/25 support equipment; add one 50% land-doctrine bonus or the command exercise unlock. |
| `ireland_coastwatch` | Keep Navy XP and unlock the Coastwatch sector-network mission. Agency creation remains with Naval Staff so it is not duplicated. |
| `ireland_air_warning` | Retain Dublin anti-air; add one 50% radar/electronics bonus and unlock the airspace-violation response. |
| `ireland_port_defence_project` | Add one named coastal-fort or harbour anti-air project through a paid decision; do not duplicate the Marine Board's current forts. |
| `ireland_maritime_protection` | Unlock marine patrol and neutral-shipping actions; XP alone is not the primary consequence. |
| `ireland_professional_army` | Raise the current 200/25 delivery to 500 rifles and 50 support equipment; add one 50% infantry/support bonus. |
| `ireland_interoperability` | Retain 25 trucks/25 support equipment; add a foreign equipment subsidy or one 50% radio/support bonus. |
| `ireland_emergency_mobilisation` | Retain 300 rifles; unlock cadre reserve, Local Security Force, and Local Defence Force decisions. Those decisions consume manpower/equipment for any created units. |
| `ireland_readiness_conclusion` | Retain one military factory and unlock the conclusion/recovery review. |
| Marine Service sequence | Keep the current trawler, convoy, dockyard, radar, coastal-defence, agency, and XP package. Add no capital ships. The only allowed trained Marine unit remains a paid, one-shot decision consuming manpower, rifles, and support equipment. |

### Politics, culture, diplomacy, Northern policy, and exceptional routes

These families should gain capability density rather than copied equipment.

| Family / representative IDs | Required payoff pattern |
| --- | --- |
| de Valera and constitutional stewardship — `ireland_de_valera_stewardship`, `ireland_constitutional_stewardship`, `ireland_de_valera_reconciliation_capstone` | Unlock named cabinet, constitutional review, reconciliation, and emergency-law actions; one route-specific advisor/institution at the capstone, not three stacked spirits. |
| Lemass — `ireland_lemass_developmental`, `ireland_dail_nomination`, `ireland_lemass_developmental_capstone` | Unlock developmental-plant and western-portfolio missions, one 50% industry bonus, and an industrial concern/advisor capability. Physical factories still count against common caps. |
| Fine Gael / coalition / Labour / Clann — `ireland_cosgrave_institutional`, `ireland_costello_coalition`, `ireland_norton_parliamentary`, `ireland_clann_founding` | Unlock their distinct cabinet, confidence, collective-bargaining, agricultural-price, by-election, and coalition-charter actions. Do not copy a generic mandate bundle across leaders. |
| culture — `ireland_cultural_survey`, `ireland_archival_record`, `ireland_serious_cultural_stewardship`, `ireland_cultural_evidence_ledger` | Unlock Gaeltacht administration, Folklore Commission collection, provincial archive survey, cultural congress, and historic-site protection missions. The 1935 Irish Folklore Commission is an archival/capability anchor, not justification for a factory. |
| neutrality — `ireland_strict_neutrality`, `ireland_armed_neutrality`, `ireland_treaty_port_diplomacy`, `ireland_foreign_safeguards` | Unlock internment, neutral-shipping, weather-report, access-request, Treaty Port, and anti-dependency actions. Armed Neutrality may add one standard rifle/support bundle; other diplomacy focuses should not. |
| Northern policy — `ireland_northern_settlement_ledger`, `ireland_northern_trade_corridor`, `ireland_northern_federal_preparation`, `ireland_northern_wartime_bargain` | Unlock the existing convention, cross-border health, plebiscite, federal/unitary safeguards, labour settlement, and wartime bargain lifecycles with explicit tooltips. No territory/core/control is a focus reward. |
| IRA / Congress / O'Duffy / clerical / Ailtirí routes | Route roots unlock their named organization or constituent-authority missions. Military escalations unlock paid recruitment/procurement decisions; no free army. Civil or plural branches unlock institutions and coalition/constitutional procedures. Capstones call the conclusion review and install at most one route identity. |
| High King / Five Provinces / Otherworld | Evidence gates unlock the existing verification or investigation missions. Constitutional variants unlock offices/charters; absurd escalation remains concealed. No supernatural equipment bundle, free cores, or generic industry is allowed. `ireland_high_king_capstone` may retain its event. |

## Tooltip and implementation contract

The current 150 unique tooltips are retained, but each must be reconciled to
the completed reward manifest.

- The first tooltip line names the primary consequence: exact equipment and
  amount, state and building level, exact research bonus, or exact named
  decisions/missions unlocked.
- Secondary lines may describe Provision, Readiness, mandate, consent,
  leverage, evidence, or route records.
- `custom_effect_tooltip` never substitutes for the actual effect.
- Use native effect output when it is clear. Put actual effects in
  `hidden_effect` only when a manually composed tooltip prevents duplication.
- Every decision unlock appears through `unlock_decision_tooltip` (with
  `show_effect_tooltip` / `show_modifiers` where supported) and the decision's
  own `visible` gate consumes the same focus flag or `has_completed_focus`.
- Dynamic state selection must tell the player which state received the
  building. If no eligible state exists, use an explicit non-material branch
  defined in the tooltip; do not silently fall back to a different reward.
- Every equipment tooltip is DLC-aware and matches the actual archetype and
  producer branch.
- Maintain a 150-row table with: focus ID, primary class, visible text key,
  actual effect/helper, tuning constant, state/equipment target,
  decision/mission consumer, AI consequence, and route-wide cap contribution.

## Layout contract after the concurrent compaction

No reward work may widen the tree or add nodes. Preserve:

- 150 focus IDs and exactly three opening roots:
  `ireland_state_still_defined`, `ireland_economic_war_review`, and
  `ireland_defence_estimates`;
- authored bounds no wider than 41 columns at y `0..16`;
- zero connector crossings, connector-through-node intersections, and long
  connectors; and
- existing `allow_branch` concealment and exactly three opening shortcuts.

Optional detour cleanup may align purely linear chains, especially the
election/government, Norton, Provision, and Marine sequences reported by the
current inspection. It is accepted only if the MCP metrics above remain zero
and the three trunks are still legible at default zoom. Do not run a blanket
focus rewrite during reward implementation.

## Historical and regional basis

- Houses of the Oireachtas records show that the 1937 Constitution replaced
  the heavily amended Free State constitution, created the presidency and a
  renewed Seanad, and that the Dáil was already sitting in 1936. This supports
  an immediately usable Dáil control followed by focus-gated constitutional
  stages, not a legislature that appears to begin only after a focus.
- The official 1938 agreements and Oireachtas history connect the end of the
  Economic War with tariff settlement and return of Berehaven, Spike Island,
  and Lough Swilly. Trade, port administration, and defence projects should
  therefore be linked but remain distinct capabilities.
- ESB archival history ties the Shannon Scheme and the 1927 Electricity
  Supply Board to national distribution; the Turf Development Board was
  established in 1934. Energy rewards should be infrastructure, fuel/resource
  programmes, and technology—not an abstract energy number alone.
- Military Archives catalogues proposals for a Coast Watching Service in
  1938–39 and its lookout-post instructions from 1940. The Coastwatch and air
  warning focuses should unlock sector networks, reporting, radar/electronics,
  and response missions.
- UCD's National Folklore Collection inherits the Irish Folklore Commission's
  1935–71 collections. Culture should unlock surveys, collections, archives,
  congresses, and evidence procedures rather than receive military or factory
  bundles.

These anchors are inspiration for playable projects. They do not authorize
anachronistic heavy industry, capital fleets, large air forces, or automatic
Northern annexation.

## Implementation order

1. Freeze the current 150 IDs, compact coordinates, unique tooltips, and
   Parliament four-control presentation.
2. Create the 150-row reward manifest and mark current material effects/caps.
3. Implement the opening Parliament lifecycle and the three root capability
   unlocks using existing executors and decisions.
4. Implement Provision and Readiness material/capability rewards, enforcing
   route-wide caps before adding each building or stockpile.
5. Add decision/mission unlock tooltips and matching visibility gates for
   politics, culture, neutrality, Northern, and exceptional routes.
6. Add bounded research/advisor/manufacturer/template capabilities; keep the
   three-spirit ceiling.
7. Reconcile all 150 reward tooltips with actual effects and update the
   material reward document and dynamic-effect documentation.
8. Re-run focus, decision/mission, Parliament, AI, localisation, country
   package, and feature-completion audits.

## Acceptance scenarios

- On 1 January 1936, Parliament shows all four controls; Convene Dáil is the
  current action and is clickable when Dublin and 15 PP requirements are met.
- Human and AI Parliament paths charge exactly once and advance the same
  focus-integrated stages without parallel executors.
- The three opening roots remain the only opening roots and communicate three
  different capabilities within their completion tooltips.
- A player following the development trunk receives named factory,
  infrastructure, transport, stockpile, and project outcomes within the caps.
- A player following the defence trunk receives equipment, training,
  technology, Coastwatch/air-warning, procurement, reserve, and Marine
  capabilities without a free army or capital fleet.
- Politics, culture, diplomacy, Northern, and concealed routes unlock distinct
  playable procedures; none uses a generic copied equipment bundle to satisfy
  the reward rule.
- All 150 focuses have a manifest row and a primary payoff beyond backend
  flags/variables/helpers.
- Every tooltip's amounts, target state, named unlocks, and conditional branch
  match the executable effect.
- A full compatible historical route stays within every material, industry,
  XP, spirit, and unit cap.
- Focus inspection preserves a 41-column span at y `0..16`, zero crossings, zero node
  intersections, zero long connectors, and exactly three opening roots.

## Assets, text/audio research, and scope limits

No new focus icon, GUI asset, animated sprite, quote package, or audio package
is required. The reward changes use existing focus art, decision icons, engine
text icons, and the existing Parliament controls. Request new art only if the
main implementation introduces a genuinely new named decision family after
review; this addendum does not authorize one.

Do not add focuses, routes, formables, country packages, GUI surfaces,
achievements, or supernatural systems. Do not solve density with universal
reward profiles or a generic completion bundle. Once this reward manifest and
the listed audits pass, broad expansion should stop.

## Promotion and open questions

If accepted, promote:

- the three-trunk and layout invariants into spec Part 1/index;
- the starting Parliament lifecycle into spec Part 2 and Part 5;
- the reward-class, balance-band, and 150-row manifest contract into the
  gameplay/reward specification and `docs/ireland_material_focus_rewards.md`;
  and
- the AI and audit requirements into the implementation/validation spec.

Until accepted and implemented, this file remains in `docs/plans`. There is no
historical research blocker. The only design question for the parent is
whether `ireland_energy_board` should spend its physical budget on one
Connaught infrastructure level plus 500 fuel, or preserve the infrastructure
cap for `ireland_development_authority` and use a synthetic-resource research
bonus. The plan recommends the first option because it is immediately visible
and regionally grounded.
