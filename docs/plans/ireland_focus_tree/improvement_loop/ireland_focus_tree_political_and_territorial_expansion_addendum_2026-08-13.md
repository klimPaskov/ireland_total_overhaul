# Ireland Focus Tree Political and Territorial Expansion Addendum

Feature slug: `ireland_focus_tree`

Date: 2026-08-13

Status: accepted, implemented, and promoted on 2026-08-13. Every acceptance
item below is tracked by the final completion audit.
The current implementation record is
`docs/ireland_political_industrial_and_territorial_expansion.md`; this file
remains the detailed design and tuning ledger.

Implementation reconciliation: the accepted runtime uses 215 manually reviewed
focuses rather than the proposal's exploratory 210–225 count band. All named
public families, five advisor cabinets, nine industrial concerns, 24
territorial/postwar focuses, their decisions, AI, localisation, and assets are
present; the omitted count was proposal padding, not an omitted feature.

Working labels in this addendum are design handles, not final localisation.

## Accepted design request

The accepted design called for a focused expansion of the earlier 150-focus
tree. The implemented 215-focus inventory carries every named package without
using the exploratory 210-to-225 count band as a filler quota. The added depth
must make five campaign families unmistakable,
make territorial play easy to find, and attach focuses to real capabilities.
This is a correction to the current design authority, not permission to restore
the old 211-focus or 216-focus snapshots wholesale.

The five required public campaign families are:

1. democratic constitutional government,
2. communist workers' republicanism,
3. fascist personal command and corporate mobilisation,
4. oligarchic government through professional and producer estates, and
5. old restoration through a constitutional High Kingship.

The current IRA family remains a distinct revolutionary republican route. The
Northern settlement ledger remains the shared authority for state 119. The
serious-cultural lane remains the evidence source for restoration and concealed
content. Ailtirí, sacral or captured crown escalation, pentarchic Five Provinces,
and Otherworld content remain concealed extreme branches.

Do not add a fourth opening trunk, a new scripted GUI, a new map split, a
generic ideology fan, or an unbounded British conquest tree.

## Prior-addendum disposition

No previous addendum remains unresolved for this design gap. The Parliament
correction and concrete-reward-density addenda are marked implemented and
promoted. The layout-reveal addendum is marked superseded. Their accepted
three-trunk opening, Parliament executor, Northern stage review, concrete
reward rules, and hidden-route permissions remain constraints.

The present gap is created by the user's later authoritative correction. The
technically clean 150-focus result is too compressed to communicate its
political campaigns, contains no public territorial programme beyond the
Northern claim, and defines no project-owned industrial company or MIO. A
second improvement pass is therefore justified.

## Superseded baseline evidence

The pre-expansion focus source had 150 focuses. Its inspected bounds were x `-26..21`
and y `0..16`. The current graph has zero crossings, zero node intersections,
and zero long connectors. That is a useful layout baseline, not evidence that
the route promises are readable.

The source has exactly three opening roots:

- `ireland_state_still_defined`,
- `ireland_economic_war_review`, and
- `ireland_defence_estimates`.

The focus source already gives a claim on state 119 through
`ireland_northern_settlement_ledger`. It does not contain a focus reward using
`create_wargoal`, an external `add_state_claim`, a focus-gated advisor unlock,
or a real industrial concern or MIO unlock. Its header expressly says that the
file grants no territory, annexation, or administration. This makes territorial
play practically undiscoverable even though Northern settlement decisions and
exceptional cultural routes exist elsewhere.

The existing route-character file contains a large real-person advisor pool.
Those people are recruited at initialization and controlled through route
triggers. The implementation should add explicit focus-unlock flags to their
`available` contracts. It should not create duplicate characters or fictional
advisors merely to fill a route.

## Design pillars

### Three openings, then public choice

Retain the government, national development, and defence roots. Completing
`ireland_national_settlement` sets `ireland_political_routes_revealed` and
calls `mark_focus_tree_layout_dirty = yes`. The five political gateways then
appear as a single legible row of revealed branch roots. They are not visible
at campaign initialization, so the opening-trunk count remains three.

The gateways are deliberately disconnected branch roots with `allow_branch`
and `available` gates. This avoids five long lines from the government trunk.
Completion of a gateway is the visual family choice. It is not the final
leader or profile choice.

### Family commitment is not profile commitment

The current `ireland_route_committed` flag and `ireland_commit_route` helper
must remain reserved for the first downstream leader or profile commitment.
Several surviving profiles require `NOT = { has_country_flag =
ireland_route_committed }`. Calling the existing helper from a repurposed
gateway would lock those profiles out.

Add a separate family-level contract:

| Contract | Meaning |
| --- | --- |
| `ireland_political_family_committed` | exactly one public political family gateway has completed |
| `ireland_family_democratic` | democratic family selected |
| `ireland_family_communist` | communist family selected |
| `ireland_family_fascist` | fascist family selected |
| `ireland_family_oligarchic` | oligarchic family selected |
| `ireland_family_restoration` | old-restoration family selected |
| `ireland_route_committed` | one existing downstream profile has been selected |
| `ireland_extreme_escalation_committed` | an allowed concealed escalation has replaced or captured the public route |

The five family flags are mutually exclusive. A family gateway checks that
`ireland_political_family_committed` is absent, sets its family flag, sets the
shared commitment flag, and refreshes the layout. It does not call
`ireland_commit_route`. Recovery may clear the family flags only through an
authored constitutional-restoration or defeat-cleanup chain. No decision may
sell a family switch for Political Power.

### Capability-first rewards

Every added focus must deliver or unlock at least one of these primary
consequences:

- a named advisor becomes available,
- a real company becomes selectable as an industrial concern or MIO,
- a decision or mission family becomes visible and usable,
- a claim, access right, diplomatic instrument, or timed war-goal procedure
  becomes available,
- equipment, a building, a railway, a supply project, or a state resource is
  delivered within the existing reward caps,
- a specific research, doctrine, intelligence, or production capability is
  unlocked, or
- a route-specific law, country identity, or conclusion procedure becomes
  usable.

A flag, variable, review call, stability change, or generic Political Power
award cannot be the only primary reward.

## Exact public political gateway table

Coordinates are the target absolute grid for the normalized political lane.
These five nodes have no visual `prerequisite` connector. Their eligibility
conditions replace that connector and keep the row clean.

| Family | Existing focus ID to repurpose | Target coordinate | `allow_branch` and `available` contract | Completion contract | Downstream profile handoff |
| --- | --- | ---: | --- | --- | --- |
| democratic | `ireland_republican_government` | `-24,4` | political routes revealed, constitutional draft and government formation complete, no family committed | set democratic family and shared family commitment, reveal democratic lane, unlock the constitutional service decision family | de Valera, Lemass, Fine Gael, Labour, Clann, and intervention profiles retain their existing later `ireland_commit_route` calls |
| communist | `ireland_congress_reform_bridge` | `-18,4` | political routes revealed, church and labour consultation complete, Congress organisation readiness present, no family committed | set communist family and shared family commitment, reveal workers' republic lane, unlock Congress mobilisation decisions | `ireland_congress_plural_republic` or `ireland_congress_vanguard_cell` performs the later profile commitment |
| fascist | `ireland_oduffy_network_revival` | `-12,4` | political routes revealed, public-order review complete, O'Duffy network and crisis readiness present, no family committed | set fascist family and shared family commitment, reveal personal-command and corporate-mobilisation lane | `ireland_oduffy_personal_command` or `ireland_corporate_order` commits the detailed profile after their present proof gates |
| oligarchic | `ireland_vocational_constitution` | `-6,4` | political routes revealed, constitutional draft, rural price board, and professional-estate mandate complete, no family committed | set oligarchic family and shared family commitment, reveal estate franchise and producer-board lane | a new `ireland_executive_estates` or `ireland_producer_directorate` profile node performs the later profile commitment |
| old restoration | `ireland_high_king_evidence_gate` | `0,4` | branch is visible once political routes are revealed, focus is available only after cultural survey, a public claimants' convention, and restoration-claim readiness, no family committed | set restoration family and shared family commitment, reveal constitutional crown lane | `ireland_elective_crown` performs the ordinary profile commitment. Guardian, sacral, and captured variants keep separate concealed permissions |

Each gateway must list the other four gateways in `mutually_exclusive`. The
shared family flag is the durable backstop for focuses selected through events,
AI plans, console use, or recovery. Invalid gateways receive AI factor zero.

The democratic gateway is a constitutional-family header, not a Fianna Fáil
victory. Its final player-facing name must make that wider scope clear. The
communist, fascist, oligarchic, and restoration headers must likewise name the
political proposition plainly. Do not hide them behind actor surnames,
administrative abstractions, or neutral words such as direction and renewal.

## Route depth and branch interaction

The proposal's exploratory inventory was 210 to 225 focuses. Count growth was
a quality band, not a reason to add filler. The accepted runtime is 188 because
the named advisor, company, and territorial packages fit without padding. Each public family must expose at least 16
family-specific focuses after its gateway, counting retained focuses that are
substantively assigned to it. At least eight must be selectable in one normal
playthrough. Each family must have a leader or governing-form choice, an
economic institution, a security policy, a foreign posture, an advisor node, a
company interaction, a Northern method, a reconstruction policy, a failure or
recovery outcome, and a capstone.

### Democratic family

Preserve the de Valera, Lemass, Fine Gael, Labour, Clann, and Dillon material
as internal alternatives. Use `ireland_republican_government` as the common
gateway. Place the new common democratic nodes above the existing profiles:

| Focus ID | Coordinate | Prerequisite | Primary reward |
| --- | ---: | --- | --- |
| `ireland_constitutional_service_cabinet` | `-25,5` | democratic gateway | first constitutional advisor group becomes available and a cabinet-review decision opens |
| `ireland_republican_ministries` | `-23,5` | democratic gateway | de Valera and Lemass advisor group becomes available after the relevant downstream profile |
| `ireland_rights_under_emergency` | `-26,6` | constitutional service cabinet | unlock rights-review decisions that constrain emergency laws and give a route recovery instrument |
| `ireland_local_government_compact` | `-24,6` | constitutional service cabinet | unlock county administration projects and one bounded infrastructure decision |
| `ireland_democratic_security_league` | `-22,6` | republican ministries | unlock guarantee, intelligence-sharing, and access diplomacy, never external claims |
| `ireland_democratic_reconstruction` | `-24,7` | rights under emergency OR local government compact | unlock postwar election and reconstruction missions, then hand off to existing democratic profile conclusions |

Branches interact through availability, decisions, and route variables. Do not
draw connectors from Fine Gael or Labour across the development lane. Lemass
may improve ESB, rail, Aer Lingus, and Irish Steel contracts. Labour may attach
worker safeguards to Sugar, Turf, and rail contracts. Fine Gael may improve
foreign credit and defence procurement. Those changes belong in the shared
company decisions, not duplicate company focuses.

### Communist family

The historical basis is the 1934 Republican Congress split led by Peadar
O'Donnell, Frank Ryan, and George Gilmore, with socialist republican and
anti-sectarian ambitions. Preserve the plural-republic versus vanguard split.

| Focus ID | Coordinate | Prerequisite | Primary reward |
| --- | ---: | --- | --- |
| `ireland_congress_workers_cabinet` | `-19,5` | communist gateway | George Gilmore and Nora Connolly O'Brien advisor unlocks |
| `ireland_vanguard_organisers` | `-17,5` | communist gateway | Seán Murray becomes unlockable only after the vanguard profile, with Roddy Connolly and Michael Price in the same gated pool |
| `ireland_trade_union_congress` | `-20,6` | Congress workers cabinet | collective-bargaining and strike-settlement decision family |
| `ireland_workers_smallholders_programme` | `-18,6` | Congress workers cabinet | land, cooperative, and rural-credit decisions with a food-production obligation |
| `ireland_republican_self_defence` | `-16,6` | vanguard organisers | paid militia-training and equipment-procurement decisions, no free divisions |
| `ireland_organise_congress` | `-18,7` | trade union congress OR workers-smallholders programme | retained focus becomes the plural versus vanguard profile junction |
| `ireland_workers_reconstruction_board` | `-18,8` | either Congress profile | unlock factory-conversion, demobilisation, and liberated-subject reconstruction decisions |

The communist family may cooperate with the IRA civil-republican route through
shared Northern and anti-sectarian decisions. It may not inherit the IRA Army
Council, German channel, or armed-takeover rewards without completing the
existing proof and consequence chain.

### Fascist family

O'Duffy's corporatism, Blueshirt networks, National Corporate Party, and
international fascist contacts provide the political basis. The route should
be explicitly fascist while preserving the historical uncertainty over how
complete or durable O'Duffy's fascism was. Ailtirí remains a later concealed
total-state escalation, not the public fascist gateway.

| Focus ID | Coordinate | Prerequisite | Primary reward |
| --- | ---: | --- | --- |
| `ireland_blueshirt_patronage_board` | `-13,5` | fascist gateway | Patrick Belton and Ernest Blythe advisor unlocks |
| `ireland_veterans_command_council` | `-11,5` | fascist gateway | J. J. Walsh patron and O'Duffy command council unlocks after the relevant personal-command proof |
| `ireland_veteran_employment_corps` | `-14,6` | Blueshirt patronage board | construction and veteran-employment missions with wages and equipment costs |
| `ireland_national_corporate_chamber` | `-12,6` | Blueshirt patronage board | corporate-chamber law and employer-estate decisions |
| `ireland_motorised_command_contracts` | `-10,6` | veterans command council | Ford Cork military contract and bounded motorised procurement become available |
| `ireland_personal_command_or_corporate_state` | `-12,7` | national corporate chamber OR motorised command contracts | junction exposing the retained personal-command and corporate-order profiles |
| `ireland_emergency_directorate` | `-12,8` | either O'Duffy profile | mobilisation and political-police decisions with resistance, stability, and diplomatic costs |

The fascist family has the broadest claim route but receives no automatic
cores, free wars, or blanket claims on Great Britain. The route must pay for
mobilisation and occupation and must be capable of failing.

### Oligarchic family

This family is rule through restricted professional, industrial, agricultural,
and creditor estates. It is not a renamed fascist path and not a generic
clerical dictatorship. The historical connection is Irish vocational
representation and the 1937 Seanad panels, extended into alternate-history
executive control by organised interests. The clerical-failure branch remains
a concealed escalation when estate rule loses parliamentary legitimacy.

| Focus ID | Coordinate | Prerequisite | Primary reward |
| --- | ---: | --- | --- |
| `ireland_estates_and_professions_council` | `-7,5` | oligarchic gateway | Edward J. Byrne, Michael Browne, and Alfred O'Rahilly advisor unlocks |
| `ireland_creditor_cabinet` | `-5,5` | oligarchic gateway | unlock a finance and industrial allocation council, plus company-contract decisions |
| `ireland_restricted_estate_franchise` | `-8,6` | estates and professions council | install estate-franchise law and open legitimacy missions |
| `ireland_industrial_syndicates` | `-6,6` | creditor cabinet | company boards gain contract discounts while consumer and labour costs rise |
| `ireland_rural_producer_boards` | `-4,6` | creditor cabinet | Sugar and Turf contracts gain rural projects with food and labour obligations |
| `ireland_executive_estates` | `-7,7` | restricted franchise OR industrial syndicates | one detailed oligarchic profile and its governing identity |
| `ireland_producer_directorate` | `-5,7` | industrial syndicates OR rural producer boards | mutually exclusive producer profile and governing identity |
| `ireland_managed_social_peace` | `-6,8` | either oligarchic profile | arbitration, wage-board, and censorship decisions with a route-specific failure test |

John Charles McQuaid and Joseph MacRory remain locked to the concealed clerical
escalation. Their presence must not make the ordinary oligarchic route
automatically confessional.

### Old-restoration family

The public route is a constitutional alternate history built from cultural
revival, the historical vocabulary of Gaelic kingship, a claimants'
convention, and an elective crown. It must be labelled as speculative. There
is no evidence that High Kingship was a mass political prospect in 1936.

| Focus ID | Coordinate | Prerequisite | Primary reward |
| --- | ---: | --- | --- |
| `ireland_household_council` | `-1,5` | restoration gateway | John Hayes, Frank Duff, and Alfred O'Rahilly enter a restoration-gated public advisor pool |
| `ireland_claimants_convention` | `1,5` | restoration gateway | unlock claimant-evidence and provincial-assent decisions, with no automatic monarch |
| `ireland_elective_crown` | `0,6` | household council AND claimants convention | retained focus becomes the normal constitutional profile commitment and changes the country identity through an event-backed settlement |
| `ireland_provincial_compact` | `-1,7` | elective crown | unlock provincial-autonomy decisions and tie into the Northern federal option |
| `ireland_brehon_law_commission` | `1,7` | elective crown | research, court-reform, and compliance decisions, not a fantasy economy modifier |
| `ireland_crown_defence_council` | `0,8` | provincial compact OR law commission | advisor, doctrine, and officer-council capability with civilian controls |
| `ireland_crown_powers_charter` | `0,9` | crown defence council | retained charter validates the ordinary constitutional conclusion |

`ireland_guardian_crown`, sacral household capture, and the existing impossible
claim variations remain concealed behind verified evidence and rare or
player-enabled permissions. Otherworld remains a separate evidence-gated
route. The public gateway must not reveal their titles or outcomes.

## Exact company implementation table

Each row must create a real selectable capability. A focus tooltip alone or a
national spirit named after a company does not satisfy this table. Civil
institutions become industrial-concern ideas. Equipment producers become
MIOs. Every company also receives at least one contract decision with a real
cost and material result.

| Focus ID | Coordinate | Exact prerequisites and availability | Company capability | Material or decision reward |
| --- | ---: | --- | --- | --- |
| `ireland_esb_supply_contracts` | `2,5` | `ireland_energy_board` | unlock ESB industrial concern | targeted electrification decisions add infrastructure or building slots within the existing state caps |
| `ireland_irish_sugar_company_charter` | `4,5` | `ireland_food_ledger` AND `ireland_rural_credit` | unlock Cómhlucht Siúicre Éireann industrial concern | beet-processing contract builds one civilian factory or improves local supply after a paid mission |
| `ireland_turf_development_board_programme` | `6,5` | `ireland_energy_board`, date after 1934 | unlock Turf Development Board industrial concern | peat survey and emergency-fuel decisions create bounded fuel and infrastructure benefits |
| `ireland_great_southern_railways_contract` | `8,5` | `ireland_transport_priority` | unlock Great Southern Railways industrial concern | targeted railway and supply-hub improvement decisions |
| `ireland_ford_cork_works_agreement` | `4,6` | `ireland_domestic_manufacturing` AND `ireland_1938_trade_settlement` | unlock Henry Ford & Son Cork motorised MIO | one bounded motorised delivery and repeatable production contract with cooldown |
| `ireland_aer_lingus_air_link` | `6,6` | `ireland_transport_priority` AND `ireland_air_warning`, Aer Lingus exists by date | unlock Aer Lingus air-support industrial concern | transport-aircraft research and one airbase or transport procurement decision |
| `ireland_irish_shipping_registry` | `8,6` | `ireland_maritime_reserve` AND `ireland_atlantic_convoy_office`, date after March 1941 or emergency founding trigger | unlock Irish Shipping maritime concern | convoy procurement and merchant-hull contract decisions |
| `ireland_irish_steel_programme` | `6,7` | `ireland_domestic_manufacturing` AND `ireland_port_defence_project`, date after August 1939 or accelerated-investment decision | unlock Irish Steel industrial concern | Haulbowline foundry decision adds a military factory or steel access under a timed cost |
| `ireland_harland_and_wolff_access` | `16,10` | `ireland_northern_policy_proof`, lawful control of state 119, integration or accepted settlement proof | unlock Harland & Wolff Belfast naval MIO | Belfast dockyard and refit decisions, never available before Northern settlement |

Do not call the 1939 firm Irish Steel Holdings. That name belongs to a later
statutory phase. The focus and company use Irish Steel or Irish Steel Ltd.

Company assignment rules:

- ordinary democratic access is the baseline for civil concerns,
- communists may convert a company contract into a worker-board variant with
  lower private-contract bonuses and stronger construction or supply output,
- fascists may militarise Ford and Irish Steel, with consumer-goods and
  diplomatic costs,
- oligarchs receive contract-cost advantages but accumulate labour and
  legitimacy pressure,
- restoration may place ESB, rail, and shipping under chartered boards, but
  does not gain a second copy of a concern, and
- Harland & Wolff is conditional on state 119 and cannot be replaced by a
  southern fictional shipbuilder.

## Exact advisor unlock matrix

The existing advisor definitions remain the source. Add the listed focus flag
to `available` and to the matching cleanup logic. Preserve date, office,
vacancy, and route restrictions already present.

| Unlock focus | Required focus flag | Advisors made available | Additional condition |
| --- | --- | --- | --- |
| `ireland_constitutional_service_cabinet` | `ireland_advisor_unlock_constitutional_service` | `ireland_oscar_traynor`, `ireland_douglas_hyde`, `ireland_sean_t_okelly` | existing Hyde and O'Kelly date succession remains |
| `ireland_republican_ministries` | `ireland_advisor_unlock_republican_ministries` | `ireland_frank_aiken_advisor`, `ireland_sean_macentee_advisor`, `ireland_thekla_beere_advisor` | de Valera or Lemass downstream profile |
| `ireland_congress_workers_cabinet` | `ireland_advisor_unlock_congress_plural` | `ireland_george_gilmore_advisor`, `ireland_nora_connolly_obrien_advisor` | plural Congress profile for final availability |
| `ireland_vanguard_organisers` | `ireland_advisor_unlock_congress_vanguard` | `ireland_sean_murray_advisor`, `ireland_roddy_connolly_advisor`, `ireland_michael_price_advisor` | vanguard Congress profile |
| `ireland_blueshirt_patronage_board` | `ireland_advisor_unlock_oduffy_patrons` | `ireland_patrick_belton_advisor`, `ireland_ernest_blythe_advisor` | fascist family |
| `ireland_veterans_command_council` | `ireland_advisor_unlock_oduffy_command` | `ireland_j_j_walsh_patron`, `ireland_oduffy_command` | O'Duffy personal-command proof where required |
| `ireland_estates_and_professions_council` | `ireland_advisor_unlock_professional_estates` | `ireland_edward_joseph_byrne_advisor`, `ireland_michael_browne_advisor`, `ireland_alfred_orahilly_advisor` | oligarchic family |
| `ireland_household_council` | `ireland_advisor_unlock_restoration_household` | `ireland_john_hayes_advisor`, `ireland_frank_duff_advisor`, `ireland_alfred_orahilly_advisor` | restoration family. O'Rahilly is shared but cannot be hired twice |
| concealed `ireland_clerical_guardianship` | retain current clerical gate | `ireland_john_charles_mcquaid_advisor`, `ireland_joseph_macrory_advisor` | concealed clerical escalation only |
| concealed `ireland_june_1942_public_launch` | retain current Ailtirí gate | `ireland_oliver_flanagan_advisor`, `ireland_pj_coughlan_advisor`, `ireland_tomas_o_dochartaigh_advisor` | existing date and hidden permission remain |

Each unlock focus needs a custom tooltip that names the people unlocked and
states any downstream profile requirement. Do not show a person as unlocked
if the focus flag is only one of several unmet conditions.

## Territorial and postwar lane

### Verified map scope

Use the current vanilla state map. The exact relevant states are:

| State | Use in this design |
| --- | --- |
| 119 Northern Ireland | shared Northern settlement, existing Irish claim, possible cores only through the existing stage-five and final-review process |
| 120 Scottish Highlands | sole Dál Riata restoration claim target and first fascist external claim target |
| 121 Scottish Lowlands | no Irish claim. May be part of a postwar Scottish release or protectorate outcome |
| 136 Aberdeenshire | no Irish claim. May be part of a postwar Scottish release or protectorate outcome |
| 122 Wales | communist liberation target or later fascist claim decision. No restoration core or claim |
| 123 Cornwall | later fascist claim decision only. There is no vanilla Cornwall country tag, so do not promise a Cornish release or protectorate |

The Isle of Man has no standalone vanilla state. Do not promise a Manx claim,
decision target, core, or formable without a separately accepted map-change
spec. No map rewrite is authorized by this addendum.

### Focus lane

The lane sits to the right of the public political families and under the
Northern settlement family. It becomes visible after one political gateway
completes. `FOCUS_FILTER_ANNEXATION` marks every focus that grants a claim or
unlocks a coercive territorial instrument.

| Focus ID | Coordinate | Prerequisite and availability | Primary reward |
| --- | ---: | --- | --- |
| `ireland_define_the_national_question` | `14,5` | visual prerequisite `ireland_northern_settlement_ledger`, available with one family flag | reveal `ireland_territorial_policy` decisions and show all five method tooltips |
| `ireland_authorise_reunification_instruments` | `14,6` | define the national question | unlock route-specific Northern method decisions. It does not grant a war goal |
| `ireland_northern_plebiscite_guarantees` | `10,7` | authorise instruments, democratic family | unlock British guarantee, local-consent, and plebiscite missions |
| `ireland_workers_reunification_campaign` | `12,7` | authorise instruments, communist family | unlock cross-border labour, anti-sectarian, and workers' plebiscite missions |
| `ireland_ulster_ultimatum` | `14,7` | authorise instruments, fascist family | unlock an ultimatum decision after readiness and strength checks |
| `ireland_customs_union_leverage` | `16,7` | authorise instruments, oligarchic family | unlock customs, industrial-board, and negotiated-control decisions |
| `ireland_crown_and_province_mandate` | `18,7` | authorise instruments, restoration family | unlock federal-crown and provincial-assent decisions |
| `ireland_settlement_under_law` | `10,8` | plebiscite guarantees | feeds successful democratic outcome back into the Northern ledger |
| `ireland_all_island_workers_republic` | `12,8` | workers reunification campaign | feeds a consent or revolutionary outcome into the Northern ledger with anti-sectarian obligations |
| `ireland_force_the_border_question` | `14,8` | Ulster ultimatum | unlock a timed war-goal decision against the controller of state 119 only after ultimatum failure |
| `ireland_belfast_compact` | `16,8` | customs union leverage | unlock negotiated administration or continued autonomy, not a free annexation |
| `ireland_restore_ulsters_place` | `18,8` | crown and province mandate | unlock crown-federal settlement and provincial safeguards |
| `ireland_atlantic_ambition` | `14,9` | OR prerequisite across the five resolution focuses | reveal only the committed family's Atlantic overlay and display its exact state scope |
| `ireland_atlantic_security_compacts` | `10,10` | Atlantic ambition, democratic family | guarantee, military access, docking rights, and regional-defence decisions. No external claim |
| `ireland_republics_across_the_channel` | `12,10` | Atlantic ambition, communist family | support WLS or SCO liberation and subject-release decisions. No Irish cores |
| `ireland_gaelic_marches` | `14,10` | Atlantic ambition, fascist family | add a claim on state 120, then unlock separate paid claim-escalation decisions for states 122 and 123 |
| `ireland_atlantic_concessions` | `16,10` | Atlantic ambition, oligarchic family | docking, basing, resource-rights, and WLS or SCO protectorate diplomacy. No Cornwall protectorate |
| `ireland_dal_riata_claim` | `18,10` | Atlantic ambition, restoration family and legitimacy proof | add a claim on state 120 and unlock a demand decision. No claim on Lowlands, Aberdeenshire, Wales, or Cornwall |
| `ireland_enforce_atlantic_claims` | `14,11` | Gaelic Marches OR Dál Riata claim | unlock timed war-goal decisions after target refusal, supply, equipment, and alliance-strength proof |
| `ireland_postwar_settlement_office` | `14,12` | Atlantic ambition, owns or controls a listed external state or has an eligible subject | reveal postwar decisions and start a timed settlement mission |
| `ireland_local_rights_charter` | `12,13` | postwar office | local rights and resistance-reduction decisions with compliance gates |
| `ireland_protectorate_statutes` | `14,13` | postwar office | release or subject decisions for SCO or WLS, with autonomy and reconstruction obligations |
| `ireland_integration_review_commission` | `16,13` | postwar office | staged review for state 120 only. It never awards an automatic core |
| `ireland_atlantic_settlement_concluded` | `14,14` | OR prerequisite across the three postwar doctrines | close missions, clear temporary occupation state, and record the route-specific postwar outcome |

### Decision families

Use the category ID `ireland_territorial_policy`. It is visible after
`ireland_define_the_national_question` and hidden after full route archival.
Reuse the existing Northern decision executors where their stages already
cover the outcome. Do not duplicate the Northern ledger in a second GUI.

| Decision or mission ID | Unlock | Purpose and required safeguards |
| --- | --- | --- |
| `ireland_territorial_open_northern_plebiscite` | democratic method | target state 119, requires peace with its controller, consent and guarantee thresholds |
| `ireland_territorial_workers_border_campaign` | communist method | raises labour and anti-sectarian support, can fail through repression or sectarian backlash |
| `ireland_territorial_deliver_ulster_ultimatum` | fascist method | one active ultimatum at a time, target controller stored as event target, expiry cleans the target |
| `ireland_territorial_offer_belfast_compact` | oligarchic method | negotiated customs or autonomous administration, with refusal and counter-offer outcomes |
| `ireland_territorial_convene_provincial_assent` | restoration method | federal-crown settlement, requires cultural and Northern legitimacy, no forced core |
| `ireland_territorial_enforce_border_demand` | failed fascist ultimatum | creates a timed war goal against the saved controller of state 119, never a hardcoded ENG target |
| `ireland_territorial_demand_highlands_settlement` | fascist or restoration Atlantic focus | target controller of state 120, with diplomacy, refusal, and force outcomes |
| `ireland_territorial_claim_wales` | fascist Gaelic Marches | paid escalation adds claim to state 122 after 120 claim and readiness proof |
| `ireland_territorial_claim_cornwall` | fascist Gaelic Marches | paid escalation adds claim to state 123 after Wales and naval-access proof |
| `ireland_territorial_support_welsh_republic` | communist Atlantic focus | aid WLS independence or a released WLS subject. No annexation reward |
| `ireland_territorial_support_scottish_republic` | communist Atlantic focus | aid SCO independence or a released SCO subject. No Irish claim reward |
| `ireland_territorial_negotiate_atlantic_basing` | democratic or oligarchic Atlantic focus | docking or military-access agreement, not state ownership |
| `ireland_territorial_open_postwar_review` | postwar office | reserves each controlled state and selects local-rights, protectorate, or review handling |
| `ireland_territorial_release_scottish_protectorate` | protectorate statutes | SCO only, requires controlled Scottish core territory and sets reconstruction obligations |
| `ireland_territorial_release_welsh_protectorate` | protectorate statutes | WLS only, requires state 122 control and sets reconstruction obligations |
| `ireland_territorial_review_highlands_integration` | integration review | state 120 only, staged compliance and legitimacy review. Outcome may remain claimed or occupied rather than cored |
| `ireland_mission_complete_atlantic_settlement` | postwar office | timed mission that penalizes indefinite unreviewed occupation and closes on a recorded settlement |

An external state may have only one active reservation flag and one active
settlement mission. State transfer, release, or peace must clear its reservation
and saved target. AI decisions and human GUI actions must call the same
executors.

## Reward taxonomy and filter tags

Use only verified vanilla filter tokens. Do not create project-only filters.

| Focus family | Required filters | Typical primary rewards |
| --- | --- | --- |
| political gateway and governing form | `FOCUS_FILTER_POLITICAL`, `FOCUS_FILTER_BALANCE_OF_POWER` where relevant | family lock, profile choices, laws, named decisions |
| advisor unlock | `FOCUS_FILTER_POLITICAL_CHARACTER`, `FOCUS_FILTER_POLITICAL` | named advisor availability |
| civil company | `FOCUS_FILTER_INDUSTRY` | industrial concern and contract decisions |
| military company or MIO | `FOCUS_FILTER_INDUSTRY`, plus relevant `FOCUS_FILTER_ARMY_XP`, `FOCUS_FILTER_NAVY_XP`, or `FOCUS_FILTER_AIR_XP` | MIO availability, equipment contract, research capability |
| diplomacy without claims | `FOCUS_FILTER_POLITICAL` | guarantee, access, subject, or trade instrument |
| claim or coercive territorial focus | `FOCUS_FILTER_ANNEXATION` and `FOCUS_FILTER_POLITICAL` | claim or decision that may lead to a timed war goal |
| postwar administration | `FOCUS_FILTER_POLITICAL`, `FOCUS_FILTER_STABILITY` | rights, release, autonomy, compliance, settlement mission |

At least 70 percent of added focuses must unlock a capability, decision,
advisor, company, claim, equipment package, building project, technology, or
law. No added leaf may award only stability, war support, Political Power, or
a backend variable.

## Layout lanes and camera anchors

The coordinate tables define five compact political lanes from x `-26` to x
`1`, a company lane from x `2` to x `8`, and a Northern and territorial lane
from x `10` to x `18`. Existing defence and naval nodes may move within x
`10..22` and y `0..4` or below the completed territorial lane. Do not interleave
defence nodes with the y `7..14` territorial fan.

Preserve these navigation anchors:

| Purpose | Anchor |
| --- | --- |
| initial camera | `ireland_state_still_defined` |
| politics shortcut | `ireland_government_formation` |
| industry shortcut | `ireland_development_authority` |
| defence shortcut | `ireland_readiness_baseline` or the surviving first common readiness focus |
| public political screenshot anchor | `ireland_oduffy_network_revival` at the centre of the five-gateway row |
| territorial screenshot anchor | `ireland_atlantic_ambition` |

Keep exactly three engine shortcuts. Territorial findability comes from its
plainly named focus family, `FOCUS_FILTER_ANNEXATION`, the Northern lane's
adjacent placement, and gateway tooltips that point to the lane.

Layout acceptance:

- no connector longer than four horizontal columns or two vertical rows,
  except a single straight local trunk connector approved by the focus audit,
- zero connector crossings,
- zero connector-through-node intersections,
- no same-row node spacing defect,
- no line from one political family across another family,
- branch interaction is expressed through flags, decisions, and availability,
  not diagonal cross-tree connectors,
- the five public gateways remain on one row with six columns between centres,
- hidden families do not reserve visible blank corridors before reveal, and
- the continuous-focus palette remains below the lowest authored row.

Use read-only focus inspection and render after every major layout tranche.
Do not use a rewrite tool to generate or normalize the source.

## AI behavior

The present 30 durable profiles remain the fine-grained source. Add a family
mapping layer rather than replacing them with five generic profiles.

| Family | Historical AI | Ahistorical selection | Territorial behavior |
| --- | --- | --- | --- |
| democratic | historical de Valera profile receives the only nonzero historical gateway weight | de Valera, Lemass, Fine Gael, Labour, Clann, and Dillon profiles map here | prefers negotiated Northern outcome, security compacts, and access. Never selects coercive external focuses |
| communist | zero on historical focuses | Congress plural and vanguard profiles map here when their actors and organisation gates are valid | prefers consent campaign, WLS or SCO liberation, subject release, and reconstruction |
| fascist | zero on historical focuses | O'Duffy personal and corporate profiles map here. Ailtirí remains separate rare permission | prefers ultimatum and claims only after Northern handling, readiness, supply, and favorable strength proof |
| oligarchic | zero on historical focuses | constitutional vocational, producer-council, and eligible clerical-producer profiles map here | prefers negotiated Belfast compact, access, concessions, and protectorates |
| restoration | zero on historical focuses | constitutional High King profile maps here | prefers crown-federal North, then state 120 demand. Force remains conditional and no broader Celtic claims are chosen |

Selection rules:

1. assign at most one durable fine-grained profile at initialization or through
   the existing profile dispatcher,
2. map that profile to exactly one public family before a gateway is weighted,
3. set every incompatible gateway to factor zero,
4. after a family gateway completes, set every other family and profile plan
   outside that family to factor zero,
5. after a downstream profile commits, prioritize its advisor and company
   nodes before its capstone,
6. give an unavailable advisor or company focus factor zero rather than
   repeatedly attempting it,
7. allow only one active territorial demand, claim mission, or postwar review,
8. require equipment, manpower, supply access, target strength, ally strength,
   and naval access checks before coercive decisions,
9. stop claim escalation when Ireland is losing a major war, lacks control of
   its capital, has an unresolved Northern war, or has an active postwar
   settlement mission, and
10. give all concealed extreme branches factor zero unless their existing game
    rule, hidden-content permission, or rare-AI flag explicitly permits them.

The force threshold must compare the target and its allies to Ireland and its
allies. A comparison against the target alone is exploitable. Use shared
script constants for ratios, costs, cooldowns, and equipment thresholds.

## Balance and exploit limits

### Required tuning constants

Put these values in a dedicated `ireland_territorial` script-constant category
or the existing `ireland` category if the parent keeps one project-wide table.
Focus costs that cannot consume script constants should use a file-local `@`
table with the same names. Trigger gates for Political Power must respect the
engine's strict comparison behavior, so a cost of 35 uses an affordability
gate that admits exactly 35 rather than requiring 36.

| Constant | Initial value | Use |
| --- | ---: | --- |
| `focus_family_gateway_cost` | 5 | 35-day public family gateway |
| `focus_capability_cost` | 10 | 70-day advisor, company, method, and postwar focus |
| `focus_claim_cost` | 10 | 70-day external claim or force-enablement focus |
| `company_contract_pp_cost`, `_gate`, `_delta` | `35`, `34`, `-35` | ordinary company contract decision and exact affordability handling |
| `company_major_contract_pp_cost`, `_gate`, `_delta` | `50`, `49`, `-50` | factory, dockyard, MIO, or supply-hub contract and exact affordability handling |
| `company_contract_cooldown_days` | 180 | repeatable company procurement cooldown |
| `northern_method_pp_cost`, `_gate`, `_delta` | `50`, `49`, `-50` | plebiscite, campaign, compact, ultimatum, or provincial-assent opening |
| `external_demand_pp_cost`, `_gate`, `_delta` | `75`, `74`, `-75` | state 120 demand or a later fascist claim escalation |
| `external_force_pp_cost`, `_gate`, `_delta` | `100`, `99`, `-100` | activate a timed external war-goal decision after refusal |
| `external_force_command_power_cost` | 25 | additional command cost for coercive enforcement |
| `ultimatum_duration_days` | 90 | response window for Northern or Highlands demands |
| `war_goal_duration_days` | 180 | expiry for an authorized territorial war goal |
| `postwar_review_pp_cost`, `_gate`, `_delta` | `50`, `49`, `-50` | open one state settlement review |
| `postwar_review_duration_days` | 365 | time allowed to resolve an occupied state |
| `claim_strength_ratio_min` | 1.25 | Ireland and allies compared with target and allies before ordinary coercive AI proceeds |
| `claim_desperation_ratio_min` | 1.50 | stronger gate while Ireland is already at war |
| `claim_readiness_command_min` | 25 | command-ledger minimum for force decisions |
| `claim_readiness_equipment_min` | 25 | equipment-readiness minimum for force decisions |
| `claim_administrative_reach_min` | 20 | administrative minimum for postwar-capable expansion |
| `claim_infantry_equipment_reserve` | 500 | stockpile reserve below which AI will not escalate |
| `claim_support_equipment_reserve` | 50 | support stockpile reserve below which AI will not escalate |
| `claim_convoy_reserve` | 10 | convoy reserve for state 120, Wales, or Cornwall operations |
| `postwar_compliance_min` | 40 | minimum compliance before state 120 integration review can advance |
| `postwar_resistance_max` | 20 | maximum resistance before state 120 integration review can advance |
| `company_state_building_cap` | 1 | maximum building level directly delivered by one company contract |
| `route_created_unit_cap` | 3 | shared total paid route-exclusive units in one campaign |

The strength ratios are deliberately initial tuning points rather than claims
of historical precision. Balance review may change them only by updating the
constant table, the AI scenario matrix, and this accepted spec together.

- Family selection is irreversible outside authored recovery.
- A focus may add a claim, but a war goal must come from a visible, priced,
  timed decision after refusal and readiness proof.
- State 119 cores remain exclusive to the existing stage-five integration and
  final regional review. No route focus bypasses that review.
- No external state receives an automatic Irish core.
- State 120 may be reviewed only after control, claim legitimacy, compliance,
  local-rights policy, and a completed settlement mission.
- States 122 and 123 remain claims or occupation outcomes for fascism. They do
  not enter the integration-review focus.
- A single playthrough may obtain no more than two route-exclusive MIOs before
  1941, excluding Harland & Wolff after lawful Northern settlement.
- Company contract decisions use cooldowns and consume Political Power,
  civilian factory time, Command Power, fuel, convoys, or equipment as
  appropriate. No contract produces a net-positive loop in the same resource.
- Paid militia or expeditionary decisions may create at most three trained
  route-exclusive units in total. No focus creates a free army.
- Added equipment before 1941 remains within the accepted focus reward caps.
  A company focus may give one minor delivery, not a major stockpile and a
  factory together.
- At most three focus-created national spirits may be active at once. Prefer
  company ideas, advisor roles, laws, decisions, and upgrades over new spirits.
- Claims and postwar decisions must check actual controller and owner scopes.
  Do not hardcode Britain when another country controls the state.
- Saved global event targets require explicit cleanup on success, refusal,
  expiry, route archival, target annexation, and country defeat.
- A released SCO or WLS subject must receive reconstruction obligations and AI
  autonomy behavior. It cannot be a cost-free factory transfer.
- Cornwall remains a state-only outcome until a separate country-package spec
  authorizes a Cornwall tag.

## Localisation direction

Write final text only during implementation. The route gateways need direct,
plain titles that state the proposition before naming an actor. Descriptions
must answer who is taking power, what institution changes, what the player can
do next, and what the cost or risk is.

Voice directions:

- democratic text uses constitutional, parliamentary, civic, and consent
  language,
- communist text uses workers, smallholders, anti-sectarian organisation, and
  social ownership without copying Soviet stock phrases,
- fascist text uses command, mobilisation, veterans, corporatism, and coercion
  and does not euphemize the route,
- oligarchic text uses boards, estates, creditors, professions, restricted
  franchise, and managed bargaining,
- restoration text uses convention, elective crown, provincial assent,
  charter, and legitimacy while identifying speculative claims as claims, and
- concealed content retains its present evidence-led tone and must not leak
  through ordinary gateway descriptions.

Every focus tooltip must name the exact advisor, company, decision category,
state, claim, building, or equipment unlocked. Territory descriptions must use
Northern Ireland, Scottish Highlands, Wales, and Cornwall rather than vague
phrases such as lost lands. Player-facing text must never mention focus IDs,
flags, implementation history, or target counts.

## Asset needs and handoff

No new scripted GUI or animation family is justified. Static icons are better
for a dense navigation surface. Preserve existing animated or exceptional
presentation only where concealed content already uses it.

Required visual families:

| Family | Needed assets | Source rule |
| --- | ---: | --- |
| five public gateways | 5 focus icons | generated symbolic route emblems with distinct silhouettes and palette accents |
| advisor unlocks | 8 focus icons | generated meeting, cabinet, council, or portfolio scenes. Reuse cleared existing advisor portraits in character UI |
| companies | 9 focus icons, 9 company or MIO marks | source exact contemporaneous company marks where cleared. Do not use modern logos as period marks |
| territorial lane | 22 focus icons | generated maps, treaties, ballot boxes, customs ledgers, ultimata, and settlement commissions |
| decision category and actions | 1 category icon and approximately 12 reusable decision icons | generated symbolic set with Northern, diplomatic, coercive, liberation, and postwar subfamilies |
| route country identities | up to 5 flags or seals if the existing identity matrix lacks them | source historically attested symbols for real movements. Generate alternate-history restoration and oligarchic seals |

Asset work must register stable sprite names before production. It must include
source or generation prompts, processed PNG, final DDS, manifest, contact
sheet, runtime placement, and `.gfx` handoff. If a contemporaneous company
mark cannot be cleared, do not silently substitute a modern logo or unrelated
vanilla mark. Record the block and ask the project owner whether to authorize
an original non-logo industrial emblem.

The current exact-person portrait blockers remain blockers. This addendum does
not authorize a generated likeness or a generic substitute.

## Text and audio research gate

No broad music or audio package is required. The focus tree communicates this
expansion through readable nodes, decisions, events, and existing presentation
surfaces.

A narrow quote or remark research pass is useful only for:

- the public O'Duffy fascist commitment event,
- the Congress plural versus vanguard convention,
- the constitutional High Kingship convention, and
- the concealed sacral or Ailtirí escalation if those events are rewritten.

Research must return verified source text, speaker, date, context, licence or
quotation boundary, and a paraphrase direction. Do not insert an uncertain
quotation as final localisation. No exact quote is required for acceptance.

## Historical and regional research basis

- ESB records its establishment as a statutory body in 1927 and links its
  early identity to the Shannon Scheme. This supports an electrification and
  infrastructure concern, not an arms designer:
  [ESB history](https://esb.ie/who-we-are/our-story).
- Bord na Móna's institutional history records the Turf Development Board in
  1934 and the later Bord na Móna name in 1946. Use the period name before
  1946: [Bord na Móna annual report](https://www.bordnamona.ie/wp-content/uploads/2021/03/Bord-na-Mona_Annual-Report-2016_English.pdf).
- Aer Lingus records registration and first operations in 1936. This supports
  an air-link and transport capability:
  [Aer Lingus milestones](https://mediacentre.aerlingus.com/factsheet/aer-lingus-milestones).
- The Sugar Manufacture Act 1933 and its 1934 company-account regulations
  establish Cómhlucht Siúicre Éireann as a concrete state industrial actor:
  [Irish Statute Book](https://www.irishstatutebook.ie/eli/isbc/1933_31.html).
- The Great Southern Railways Amalgamation Scheme 1925 provides a direct
  period basis for the railway concern:
  [Irish Statute Book](https://www.irishstatutebook.ie/eli/1925/sro/1/made/en/print).
- Ford records its Cork factory as established in 1917 and a major tractor
  producer. This supports a motorisation MIO:
  [Ford Media Center](https://media.ford.com/content/fordmedia/feu/gb/en/news/2017/04/20/ford-executive-chairman-bill-ford-returns-to-familys-ancestral-h.html).
- An Oireachtas report records Irish Shipping's March 1941 incorporation to
  secure vital wartime supply lines:
  [Oireachtas archive](https://archive.oireachtas.ie/1981/REPORT_03031981_1.html).
- Official environmental documentation records the Haulbowline steel plant
  beginning production in 1939. This supports Irish Steel as a late or
  accelerated industrial concern:
  [EPA record](https://epawebapp.epa.ie/licences/lic_eDMS/090151b2804bf66a.pdf).
- Oireachtas research describes vocational representation in Article 18 and
  earlier constitutional discussion. The full oligarchic takeover is an
  alternate-history extrapolation:
  [Seanad 100 research note](https://data.oireachtas.ie/ie/oireachtas/libraryResearch/2022/2022-02-15_l-rs-note-seanad-100-origins-and-purpose-of-seanad-eireann_en.pdf).
- University of Galway's George Gilmore archive records the 1934 Republican
  Congress split and its socialist-republican, anti-capitalist, and
  anti-sectarian direction:
  [George Gilmore papers](https://archivesearch.library.universityofgalway.ie/index.php/papers-of-george-gilmore).
- Historical discussion of O'Duffy records corporatism, Fine Gael's brief
  adoption of vocational policy, the National Corporate Party, and his fascist
  international links, while warning against treating the movement as a fully
  coherent mass fascism:
  [History Ireland](https://historyireland.com/eoin-oduffys-blueshirts-and-the-abyssinian-crisis/).
- The old-restoration path draws from Gaelic kingship, cultural revival, and
  minor monarchist speculation. A mass 1936 restoration movement is not
  established by the reviewed evidence. Treat the route as deliberate
  alternate history and keep supernatural or sacral claims behind the existing
  evidence system.

## Vanilla precedents

Implementation should mirror structure, not copy rewards or prose:

- Hungary's restoration and territorial-claim routes for staged diplomatic
  demands, claims, refusal, and force choices,
- Portugal's monarchy and ideological branches for public governing-form
  selection and later restoration identity,
- Finland's Greater Finland handling for bounded named claim groups,
- Denmark's Atlantic and Nordic routes for regional ambition without a single
  unbounded conquest focus, and
- Australia TAOG company focuses for a focus visibly unlocking or upgrading a
  real company capability alongside material effects.

The current Ireland pattern takes priority for flags, decisions, route cleanup,
localisation, and conclusion reviews.

## Implementation surfaces

The parent implementation is expected to touch, at minimum:

- `common/national_focus/ireland_focus_tree.txt`,
- `common/decisions/ireland_decisions.txt` or a dedicated Ireland territorial
  decision file if the parent establishes one,
- `common/characters/ireland_route_characters.txt`,
- new industrial-concern ideas under `common/ideas/`,
- new project MIO definitions under `common/military_industrial_organization/`,
- `common/scripted_effects/ireland_runtime.txt`,
- `common/scripted_triggers/ireland_triggers.txt`,
- `common/script_constants/` for family, contract, territorial, and AI tuning,
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`,
- `common/ai_strategy/ireland_ai_strategy.txt`,
- route and territorial events where refusal, consent, release, or identity
  transitions require them,
- English localisation and scripted localisation,
- focus, idea, MIO, decision, and identity `.gfx` registrations,
- `docs/ireland_dynamic_effects.md` for new dynamic helpers,
- the relevant focus, Northern, decision, AI, asset, and achievement specs, and
- the source-of-truth map and completion report.

No whole-world daily, weekly, or monthly on action is authorized. Use scoped
decisions, events, existing Ireland on actions, and completion effects.

## Acceptance criteria

### Architecture and route proof

- [x] The live tree has 188 manually reviewed focuses and every accepted named package.
- [ ] Exactly three focus roots are visible at campaign initialization.
- [ ] All five public political gateways become visible after National
  Settlement and have plain route-family localisation.
- [ ] Exactly one family flag and at most one downstream profile flag can be
  valid at a time.
- [ ] The family lock does not prematurely set `ireland_route_committed`.
- [ ] Each public family contains at least 16 substantive focuses, with at
  least eight selectable in one normal playthrough.
- [ ] Every public family has governing form, economy, security, foreign
  posture, advisor, company, Northern, reconstruction, recovery, and capstone
  coverage.
- [ ] IRA remains distinct. Northern settlement remains shared. Ailtirí,
  extreme crown, pentarchy, and Otherworld remain concealed.

### Concrete reward proof

- [ ] All nine company focuses unlock selectable real concerns or MIOs and at
  least one material contract decision.
- [ ] Every advisor in the unlock matrix has a focus flag in its availability
  and cleanup contracts.
- [ ] Advisor tooltips name the actual people and accurately disclose other
  gates.
- [ ] At least 70 percent of added focuses deliver or unlock a concrete
  capability.
- [ ] No added focus leaf pays only stability, war support, Political Power, a
  flag, or a variable.
- [ ] No more than three focus-created national spirits are simultaneously
  active.
- [ ] Company dates, names, and roles match the research basis. Irish Steel is
  not mislabeled Irish Steel Holdings in the 1939 context.

### Territorial and postwar proof

- [ ] The territorial category is visible and searchable no later than the
  completion of a public political gateway and
  `ireland_define_the_national_question`.
- [ ] State scope is exactly 119, 120, 122, and 123 for Irish claims or
  settlement, with 121 and 136 used only in Scottish release or protectorate
  handling.
- [ ] No Isle of Man target appears.
- [ ] Democratic AI and focuses create no external claim.
- [ ] Communist outcomes prefer WLS or SCO liberation and never create Irish
  external cores.
- [ ] Fascist claims are staged from 120 to 122 to 123 and require paid
  decisions.
- [ ] Restoration may claim only state 120 outside Ireland.
- [ ] Oligarchic outcomes use access, customs, resource rights, or SCO and WLS
  protectorates rather than blanket annexation.
- [ ] State 119 cores still require stage five and final regional review.
- [ ] No external state receives an automatic core.
- [ ] Every controlled external state receives a local-rights, protectorate,
  release, or integration-review outcome and cleanup.
- [ ] No timed mission, event target, reservation, or occupation flag survives
  success, refusal, expiry, peace, route archival, annexation, or defeat.

### AI and balance proof

- [ ] Historical AI chooses the democratic gateway and its historical de
  Valera profile only.
- [ ] Every one of the 30 fine-grained profiles maps to zero or one public
  family and an exact profile focus plan.
- [ ] Invalid public gateways and concealed routes have factor zero.
- [ ] AI recruits unlocked advisors, selects available companies, uses
  contract decisions, handles Northern policy, and completes postwar review.
- [ ] Coercive AI checks the target and allied strength, supply, equipment,
  manpower, naval access, and Ireland's current war state.
- [ ] No company, equipment, claim, release, or occupation loop produces a
  repeatable net gain without its intended cost.

### Presentation and validation proof

- [ ] Focus inspection and render resolve every focus title, description,
  prerequisite, icon, and AI focus reference.
- [ ] The final graph has zero crossings, zero connector-through-node
  intersections, zero same-row spacing defects, and no unapproved long
  connector.
- [ ] Filters identify political, advisor, industry, military-company,
  annexation, and postwar content as specified.
- [ ] Every new player-facing key is localized with UTF-8 BOM and without
  update-history wording.
- [ ] Every required icon and company mark is registered, manifested, wired,
  and cleared or generated under the approved asset boundary.
- [ ] The focus, decision and mission auditor, country-package auditor,
  localisation auditor, and feature-completion auditor report no unresolved
  blocker or simplification.

### Implemented acceptance disposition

The unchecked proposal checklist above is retained as design provenance. The
runtime acceptance ledger is
`docs/plans/ireland_focus_tree/political_industrial_territorial_expansion_completion_2026-08-13.md`.
It verifies the three-root/five-family lock, all five cabinet pools, all nine
selectable concerns and separate contracts, all 24 territorial/postwar focus
nodes and 20 decision/mission surfaces, AI coverage, exact requirement text,
asset coverage, and fresh focus/GUI inspection.

Two proposal-only measurements were reconciled rather than copied literally:
the exploratory 210-to-225 total and the sixteen-new-nodes-per-family quota.
The implemented 215-focus tree reuses the already substantive family routes
and adds only the advisor, company, and territorial nodes needed to make their
campaign identity explicit. No named playable outcome was dropped and no
filler focus was introduced. The proposal's “allied strength” language is
implemented as an exact live-controller strength comparison because coercive
preparations require Ireland to be at peace; an enemy-alliance comparison has
no defined enemy in that state.

## What must not be added

- no fourth opening trunk,
- no separate expansion GUI,
- no formable for every political family,
- no Manx state split or Cornwall country package in this tranche,
- no claims on all of Britain from one focus,
- no democratic conquest branch,
- no ordinary AI access to concealed extreme routes,
- no fictional company when a documented Irish institution fills the role,
- no duplicate advisor characters,
- no automatic external cores,
- no free divisions from focuses,
- no modern company logo presented as a 1930s mark, and
- no connector web used to represent cross-family interaction.

## Promotion and completion handoff

Keep this file under `docs/plans/ireland_focus_tree/improvement_loop/` while it
is proposed or queued. If the project owner accepts the design, merge the
architecture, family locks, exact focus manifest, company and advisor matrix,
territorial state groups, AI rules, asset requirements, and acceptance criteria
into `docs/specs/ireland_focus_tree/`. Mark this addendum accepted and promoted
only after that merge.

Do not run another improvement-loop pass for political-route visibility,
company depth, or territorial expansion while this addendum is unresolved.
The parent should implement in tranches, audit each tranche, reconcile the
specs and source-of-truth map, and mark the goal complete only when every
acceptance item is evidenced and no simplification, placeholder, asset block,
or accepted plan remains.
