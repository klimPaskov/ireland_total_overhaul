# Ireland Focus Tree Decision and Mission Map

Feature slug: `ireland_focus_tree`

Status: Part 5 source map

All names are working labels unless they are historical proper names.

## M2 authority amendment — 2026-08-01

The approved M2 interpretation preserves exactly 13 decision categories, 140
actions, and 54 mission families. The by-election mode is a named mode of
`Conduct a Free General Election`, and the parish-audit mode is a named mode of
`Keep Essential Services Running`. The two freed inventory rows are the
Radical and Underground families `Consolidate the Movement Network` and
`Secure Constituent Authority`. They remain physically owned by the Radical
and Underground category and retain separate mode-specific objectives,
deadlines, outcomes, AI weights, and cleanup records.

# Control-surface map

```text
National Settlement and Government
  -> Elections and Coalition Formation
  -> Organised Society
  -> Cultural and Archival Work
  -> Radical and Underground Transition

National Provision <-> National Readiness
  -> Neutrality and Incidents
  -> Foreign Leverage and Agreements

Northern Settlement
  -> Occupation and Integration
  -> Regional Orders and External Ambitions
  -> Postwar Settlement

Every route conclusion reads all relevant surfaces.
```

# Category roster and caps

| Category | Visibility | Category cap | Primary state | Reserved capacity |
| --- | --- | --- | --- | --- |
| National Settlement and Government [working] | opening onward | 2 | cabinet, confidence, constitutional review, succession, caretaker government | one constitutional crisis slot is reserved |
| Elections and Coalition Formation [working] | campaign, dissolution, scheduled election, government formation | 2 | registers, candidates, transfers, coalition charter, ministries | one election mission and one formation mission |
| Organised Society [working] | opening onward, route filtered | 2 | Labour, rural organisations, Church domains, vocational councils, minority safeguards | one national negotiation and one regional delivery mission |
| Cultural and Archival Work [working] | opening serious lane, concealed stages after valid evidence | 2 | language, folklore, archives, sites, provincial culture, false leads | one public cultural project and one evidence mission |
| Radical and Underground Transition [working] | only after a valid crisis or movement gate | 2 | IRA, Congress, O'Duffy, Ailtirí, clerical capture, route transition | one organisational mission and one seizure or constituent mission |
| National Provision [working] | opening onward | 3 routine, 4 in national emergency | food, energy, transport, shipping, industry, housing, regional delivery | one slot is reserved for a component below 20 |
| National Readiness [working] | opening onward | 3 routine, 4 during invasion danger or war | training, equipment, mobilisation, mobility, warning, maritime protection, intelligence | one slot is reserved for an exposed frontier or compromised plan |
| Neutrality and Incidents [working] | September 1939 onward or earlier war spillover | 2 routine, 3 during direct incident | airspace, shipping, internment, intelligence, weather, access, censorship, border | an unresolved severe incident occupies one slot |
| Foreign Leverage and Agreements [working] | when a valid partner channel exists | 2 | Britain, United States, diaspora, Germany, Vatican, neutral states | one active mission per sponsor |
| Northern Settlement [working] | contact, negotiation, confidence measure, plebiscite, convention, or war planning | 3 | local actors, British position, consent, security, integration preparation | one political, one local, and one security or economic mission |
| Occupation and Integration [working] | after military control, provisional settlement, or lawful transfer | 3 | administration, policing, services, finance, industry, rights, demobilisation | one security, one service, and one constitutional slot |
| Regional Orders and External Ambitions [working] | after route and capacity gates | 2 | Celtic cooperation, Atlantic structures, protectorates, liberation, royal, provincial, compact orders | one institution mission and one contribution or conflict mission |
| Postwar Settlement [working] | major war end, Emergency review, or 1945 onward | 3 | demobilisation, controls, reconstruction, republic, Commonwealth, UN, alignment, Northern review | one legal, one material, and one diplomatic slot |

# Global objective capacity

| Campaign state | Global active cap | Reserved critical slots | Closure rule |
| --- | ---: | ---: | --- |
| normal peace | `8` | `1` | slot returns after crisis or review closes |
| Emergency or declared war | `10` | `2` | returns to 8 after 30 stable days |
| national emergency plus Northern occupation | `12` | `3` | returns when either condition closes |

Critical slots belong to component collapse, invasion, constitutional collapse, occupation security, and route review. They never host routine construction or lobbying.

# Priority queue

| Input | Priority effect |
| --- | --- |
| component at 0 or active invasion | +50 |
| constitutional or occupation collapse | +40 |
| component below 20 | +30 |
| route conclusion or six-month review | +25 |
| major historical date window | +20 |
| local damage or severe incident | +15 |
| all physical prerequisites present | +10 |
| same region and purpose already active | -20 |
| same family completed inside 90 days | -15 |
| invalid target or dead sponsor | set to zero |

# Dynamic cost map

| Action scale | Typical political cost | Typical physical burden | Typical duration | Typical risk |
| --- | --- | --- | --- | --- |
| local | 10 to 20 political power | staff, 250 to 1,000 manpower, local equipment or one transport pool | 90 to 110 days | local consent or exposure |
| regional | 25 to 40 political power | one to two factories, trucks, trains, fuel, equipment and regional staff | 120 to 180 days | service displacement or regional backlash |
| national | 45 to 65 political power | two to four factories, major stockpile, command and administrative burden | 180 to 270 days | coalition, shortage, or dependency |
| strategic | 70 to 100 political power | four to five factories, forces, shipping, debt, access, leverage and safeguards | 270 to 365 days | constitutional failure, war, occupation, or client status |

Command power never exceeds `60`. Stockpiles use target requirements and scarcity floors. Low stocks can block an action instead of reducing its price.

# Named region map

| Working region | Geography | Objectives |
| --- | --- | --- |
| Dublin Metropolitan Region [working] | Dublin city and county, Dún Laoghaire, port approaches, central government sites | government, housing, censorship, air defence, port, labour |
| Eastern Administrative Corridor [working] | Dublin, Kildare, Meath, Wicklow, eastern rail and road approaches | government dispersal, transport, mobilisation, food distribution |
| Midlands and Central Plain [working] | Laois, Offaly, Westmeath, Longford and connected central routes | tillage, peat, depots, roads, dispersed industry |
| South and Southeast [working] | Wexford, Waterford, Carlow, Kilkenny and southern Tipperary | Rosslare and Waterford routes, tillage, airspace, coastal warning |
| Cork and Southwest [working] | Cork, Kerry, Cobh, Berehaven and southwest approaches | Treaty Port defence, shipping, fisheries, industry, Gaeltacht |
| Shannon and Mid-West [working] | Limerick, Clare, northern Tipperary, Foynes and Shannon crossings | hydro power, aviation, port traffic, rail, regional works |
| Connacht and Western Seaboard [working] | Galway, Mayo, Roscommon, Sligo, Leitrim and western ports | smallholders, fisheries, Gaeltacht, weather, roads, emigration |
| Donegal and Northwest [working] | Donegal, Lough Swilly, northwest coast and approaches | border, coastwatch, port defence, northern contacts, language |
| Border Belt [working] | Donegal, Leitrim, Cavan, Monaghan and Louth border districts | smuggling, refugees, security, rail corridors, Northern confidence |
| Gaeltacht and Atlantic Islands [working overlay] | official and route-recognised Irish-speaking districts and inhabited Atlantic islands | language services, folklore, supply, evacuation, site stewardship |
| Treaty Port Complexes [working overlay] | Cobh, Berehaven and Lough Swilly | inventory, command, batteries, access, mines, repair, foreign demands |
| Dublin to Belfast Corridor [working] | Dublin, Drogheda, Dundalk, Newry, Lisburn and Belfast route | trade, rail, military movement, refugees, plebiscite access |
| Dublin to Cork Corridor [working] | Dublin, Kildare, Portlaoise, Thurles, Mallow and Cork route | food, troops, fuel, industry, reconstruction |
| Dublin to Galway Corridor [working] | Dublin, Midlands, Athlone and Galway route | western access, supply, evacuation, regional development |
| Shannon and Western Port Network [working] | Foynes, Limerick, Galway and connected rail and road systems | Atlantic shipping, fuel, food, relief |
| Belfast Urban and Harbour [working] | Belfast city, docks, shipyards, aircraft works and dense housing districts | industry, labour, blitz relief, policing, integration |
| Lower Lagan and Lisburn [working] | Belfast approaches, Lisburn and the Lagan industrial corridor | transport, housing, security, labour |
| Antrim and Larne [working] | County Antrim, Larne port and northern approaches | ports, unionist institutions, air and sea access |
| Ards and North Down [working] | Bangor, Newtownards, Ards and North Down | airfields, coastal warning, blitz spillover, local government |
| Derry and Foyle [working] | Derry city, Foyle port and northwest approaches | naval access, nationalist representation, Donegal links, industry |
| Tyrone and Mid-Ulster [working] | Tyrone and central Northern districts | agriculture, local government, policing, representation |
| Fermanagh and Erne [working] | Fermanagh, Erne crossings and western border | security, smuggling, waterways, rural consent |
| Armagh and Newry Border [working] | Armagh, Newry and the southeast border districts | rail, policing, nationalist and unionist confidence |

# Family flow maps

## Government and election flow

```text
seat or confidence change
  -> Count Formal and Routine Votes
  -> Request Confidence Vote
      -> government confirmed
      -> Open Coalition Negotiations
      -> Ask the President for Dissolution
          -> election
          -> Nominate an Alternative Taoiseach
  -> Assign Cabinet Portfolios
  -> Ratify Coalition Charter
  -> Publish Government Programme
  -> Six-Month Settlement Review
```

## Provision flow

```text
component shock or authorised programme
  -> choose project or emergency action
  -> commit physical and political inputs
  -> active regional mission
      -> full delivery
      -> partial delivery with debt or bottleneck
      -> failure and escalation
  -> maintenance review
  -> project cleanup or institutional upgrade
```

## Readiness flow

```text
capability audit
  -> training, procurement, mobilisation, route, warning, maritime or intelligence action
  -> deployment or delivery mission
  -> component change
  -> operational plan test
  -> route gate or failure
  -> demobilisation and equipment recovery
```

## Neutrality flow

```text
incident detected
  -> identify actor, law, place and severity
  -> immediate response decision
  -> investigation or enforcement mission
  -> domestic and foreign reaction
  -> Integrity, leverage, exposure and cooperation memory
  -> restoration, selective neutrality, belligerency or breakdown
```

## Northern flow

```text
claim and contact
  -> confidence measure
  -> valid mandate and representation
  -> British settlement
  -> plebiscite, federal, unitary, labour, wartime or coercive route
  -> integration stage 2
  -> shared administration stage 3
  -> integrated administration stage 4
  -> stable constitutional integration stage 5
  -> regional core eligibility review
```

# Decision inventory by family


## Settlement and government

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Convene a Cabinet Cohesion Review [working] | H/P | Cabinet Cohesion below 60 or a route review | test ministers, portfolios, collective responsibility, and emergency commitments | political power, ministerial concessions, seven to twenty-one days | records loyal, conditional, and dissenting ministers and changes Cabinet Cohesion | public resignation, rival mandate, or caretaker transition, then clear temporary portfolio flags |
| Request a Confidence Vote [working] | H/P | government majority is disputed | force the formal and routine seat ledgers to resolve government authority | Dáil preparation, coalition discipline, one parliamentary sitting | confirms government, opens formation talks, or starts dissolution procedure | lost vote starts government collapse and removes government-only actions |
| Negotiate Confidence and Supply [working] | P | minority government and an eligible support bloc | trade a bounded programme for named votes without merging parties | policy concessions, Cabinet Cohesion, support-bloc demands | creates a dated support agreement with review and expiry | breach removes promised support and starts a confidence mission |
| Nominate an Alternative Taoiseach [working] | H/P | a Taoiseach has lost the majority and another coalition can reach 70 routine votes | assemble a valid nomination before presidential dissolution | coalition concessions, office commitments, twenty-one-day deadline | installs a lawful government after presidential appointment | failed nomination permits dissolution or extended caretaker rule |
| Ask the President for Dissolution [working] | H/P | Taoiseach lacks or seeks a renewed mandate | begin the constitutional dissolution sequence | political power, public risk, presidential independence test | opens an election if accepted | refusal starts alternative-government mission and caretaker restrictions |
| Invoke the Council of State [working] | P | presidential or constitutional doubt over emergency, referendum, dissolution, or legislation | seek formal consultation without turning the President into an executive ruler | time, legal staff, public attention | clarifies procedure and modifies legitimacy | divided advice raises constitutional uncertainty |
| Publish a Government Programme [working] | P | new coalition or minority government | convert negotiated promises into dated policy obligations | Cabinet Cohesion, policy concessions, administrative capacity | creates measurable programme missions | unfunded promises damage mandate and coalition trust |
| Establish a Caretaker Cabinet [working] | P | no viable majority and dissolution or convention is pending | limit appointments, emergency escalation, and irreversible agreements | reduced policy freedom, temporary office slate | prevents institutional vacuum | prolonged caretaker rule lowers mandate and opens radical pressure |
| Review the Six-Month Settlement [working] | P/A | route commitment review date | test government, law, society, security, Provision, Readiness, and public authority | no click cost, objective completion across systems | confirms, conditions, or reopens the route settlement | failure opens route-specific recovery or collapse and cleans obsolete route actions |
| Restore Ordinary Constitutional Procedure [working] | P | emergency or failure government has stabilised | return appointments, debate, courts, and review to ordinary rules | administrative time, possible security risk, repeal costs | improves consent and closes permanent-emergency failure | premature restoration can trigger security or supply relapse |

## Elections and coalitions

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Update the Electoral Register [working] | H | scheduled election, referendum, plebiscite, or post-settlement vote | audit voters, displaced persons, contested districts, and duplicate entries | administrative reach, local staff, time | improves vote legitimacy and reduces dispute risk | poor register creates challenge events and lowers minority confidence |
| Protect Campaign Freedom [working] | H/P | election or plebiscite campaign | protect meetings, printing, candidates, and opposition access | Garda deployment, administrative burden, security exposure | raises legitimacy and reduces boycott risk | violence, censorship, or selective policing changes turnout and route access |
| Organise County Candidates [working] | H/P | party contest before an election | balance local organisation, leadership loyalty, social groups, and transfer strategy | party organisation, money, candidate concessions | creates candidate slate and regional strength | rebellious candidacies, split tickets, or weak regions |
| Negotiate Transfer Pacts [working] | P | STV election and compatible parties or independents | coordinate lower preferences without merging programmes | policy promises, local autonomy, party unity | improves coalition prospects in selected regions | exposure can alienate core voters or strengthen rivals |
| Secure Polling Stations [working] | H/P | violence, occupation, radical pressure, or Northern plebiscite | deploy trained civil police and observers to named districts | personnel, transport, command restraint | reduces intimidation and invalid ballots | heavy-handed deployment lowers consent and may not prevent disruption |
| Count Formal and Routine Votes [working] | H/P | election result or party defection | update 153 formal seats, 152 routine votes, Ceann Comhairle reserve, and support agreements | administrative action | produces authoritative Dáil ledger | inconsistent ledger blocks government formation and triggers audit |
| Open Coalition Negotiations [working] | P | no party holds 70 routine votes | invite eligible parties and blocs with red-line records | time, ministries, policy concessions, party cohesion | creates negotiation table and possible charter | expired talks lead to caretaker, minority, or new election |
| Assign Cabinet Portfolios [working] | P | coalition charter reaches 70 votes | separate Taoiseach, party leader, parliamentary leader, Tánaiste, and ministries | office concessions and competence tradeoffs | installs cabinet and advisor availability | incompatible offices or overpromising cause immediate cabinet crisis |
| Ratify the Coalition Charter [working] | P | portfolio slate and programme are complete | secure party, parliamentary, and where relevant union or agrarian approval | party unity and policy concessions | forms a government with dated review | rejection reopens negotiations and clears provisional appointments |
| Prepare a By-Election [working] | H/P | vacancy, leader outside Dáil, death, resignation, or disqualification | select candidate, protect polling, and update seat ledger | local organisation and campaign resources | restores representation or leader eligibility | loss changes succession and government arithmetic |

## Organised society

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Negotiate an Education Compact [working] | H/P | education dispute, constitutional review, or Northern settlement | settle funding, language, denominational management, inspection, and minority safeguards | budget, Church confidence, minority confidence, teacher support | creates reviewed education law and service delivery missions | veto, boycott, or forced assimilation crisis |
| Contract Parish Welfare Services [working] | H/P | state capacity is insufficient and Church service networks are available | fund defined health or welfare services under audit | consumer goods burden, service dependency, oversight | improves delivery with dated review | dependency, exclusion, or financial scandal |
| Create a Public Health Board [working] | P | constitutional or Labour route seeks public provision | build state or mixed administration without instant national capacity | civilian factories, trained staff, local cooperation | opens regional health missions and reduces service dependency | Church dispute, labour shortage, or urban bias |
| Charter Collective Bargaining [working] | P | Labour Organisation and employer bodies are organised | define unions, wages, arbitration, essential services, and strike rights | political concessions, employer confidence, union discipline | creates a stable labour framework | wildcat action, lockout, or coercive labour law |
| Set Agricultural Prices [working] | H/P | harvest, trade, rationing, or agrarian campaign | balance producer income, consumer prices, exports, and state purchasing | budget, food stocks, rural and urban consent | changes Food Security and Agrarian Cohesion | hoarding, urban hardship, or farmer revolt |
| Recognise an Agrarian Support Bloc [working] | P | Clann na Talmhan or aligned independents coordinate on a named issue | record a temporary issue caucus without falsifying party membership | policy concession and expiry date | adds votes for the named measure | bloc expires, fragments, or becomes a formal coalition |
| Convene a Vocational Council [working] | P | constitutional vocational law is active | bring employer, labour, farmer, professional, Church, and minority delegates into a bounded advisory body | administrative cost, representation concessions | advises a named policy and changes stakeholder confidence | capture, compulsory estates, or Dáil bypass starts transformation crisis |
| Audit Church Service Dependency [working] | P | service dependency exceeds 50 or a government changes | measure capacity, access, finance, exclusion, and replacement options | administrative burden and possible episcopal conflict | creates reform schedule or renewed contract | concealment or abrupt withdrawal harms services |
| Protect Minority Institutions [working] | H/P | constitutional, Northern, clerical, corporate, or hidden route pressure | fund and protect schools, worship, associations, and civil access | budget and majority backlash risk | raises Minority Confidence and blocks coercive conclusions | neglect or repression opens domestic and foreign reaction chains |
| Mediate an Essential-Service Dispute [working] | H/P | transport, docks, power, hospitals, or food distribution faces strike or lockout | choose arbitration, wage concession, emergency staffing, or coercion | money, consent, command, union trust | restores service with route-specific settlement | service stoppage, repression, or split union |

## Cultural and archival work

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Fund Gaeltacht Administration [working] | H/P | serious cultural lane active | provide staff, roads, schools, broadcasting, and public service capacity | budget, trained speakers, regional delivery | raises Cultural Capacity and local service quality | symbolic spending without service causes distrust |
| Expand Folklore Collection [working] | H | Irish Folklore Commission and schools network are available | collect oral histories, customs, stories, place knowledge, and material culture | teachers, collectors, travel, archives | adds verified cultural records and route-safe flavour events | poor custody, politicisation, or fabricated evidence |
| Survey Provincial Archives [working] | H/P | provincial or old-institution research is authorised | catalogue charters, legal records, genealogies, maps, and local claims | archivists, legal staff, local access | adds documented or uncertain evidence with provenance | misreading or forgery creates false lead |
| Hold a Provincial Cultural Congress [working] | P | regional organisations and Cultural Capacity are sufficient | bring county, language, labour, Church, artistic, and historical delegates together | regional budget, transport, representation | builds provincial mandate or serious cultural institutions | boycott or central capture lowers Federal Cohesion |
| Protect a Historic Site [working] | H/P | site faces military, development, looting, or route pressure; a regional institution, Social Consent 35, and rights-bearing local constituency can support the work | hold full control of state 135, staff, secure, document, and maintain a named site | 250 manpower for guards, 5 Trucks for transport, 10 Support Equipment maintenance kits, regional participation, Social Consent 35, and one local-support ledger at the cultural rights floor | preserves evidence and public trust; records the direct Cultural Capacity outcome only after the same admission contract is rechecked | militarisation or spectacle creates cultural backlash; missing local support, consent, transport, guards, or maintenance blocks the action and leaves no result flag |
| Standardise Irish-Language Services [working] | P | trained staff and legal support exist | phase bilingual administration by region and service | training, recruitment, documents, delay | improves access without coercion | forced deadlines reduce service and minority confidence |
| Test a Restoration Claim [working] | P/A | concealed evidence threshold reached | submit a crown, provincial, legal, or folklore claim to independent review | archival credibility, legal time, public exposure | classifies evidence as historical, plausible, unresolved, or absurd | false lead closes or changes the route and cleans reveal flags |
| Contain a Public Folklore Panic [working] | P/A | rumours or site incidents become public | use local authorities, clergy, scholars, police, or route institutions | consent, credibility, time, site access | reduces panic while preserving or dismissing evidence | heavy suppression increases hidden interest or compact breach |
| Convene a Hidden Evidence Council [working] | A | all reveal gates and unusual campaign conditions are met | choose secrecy, public inquiry, royal, provincial, or stewardship authority | elite trust, cultural capacity, legal risk | opens the valid concealed route transition | exposure without capacity creates scandal, fraud prosecution, or panic |
| Archive the Failed Restoration [working] | P/A | hidden route is abandoned or disproved | preserve records, compensate institutions, and restore ordinary ownership | budget, public explanation, legal settlement | cleans false leads and preserves serious cultural benefits | destruction or cover-up harms Cultural Capacity and future trust |

## Radical and underground transition

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Audit the Republican Commands [working] | H/P | IRA route gate or security crisis | measure GHQ, local commands, arms, prisoners, civil contacts, and penetration | security exposure, local trust, time | sets Army Council Cohesion and Local Command Compliance | exposure, arrest, or false strength assessment |
| Convene the Convention of Commands [working] | P | valid IRA transition and sufficient networks | choose central command, northern primacy, civil compact, or continued underground | leadership concessions, security risk, local compliance | sets leadership offices and transforms the National Settlement | command split, civil rejection, or state crackdown |
| Create a Civil Republican Directorate [working] | P | IRA civil branch has public and administrative support | separate public executive, finance, courts, and security from GHQ | administrative reach, legitimacy, cadre transfer | raises Civil Republican Authority | dual orders or GHQ displacement |
| Rebuild the Republican Congress [working] | P | failed parliamentary bridge, labour organisation, radical republican partners | reconstruct committees, unions, local groups, and a common programme | union resources, local organisers, ideological concessions | sets Congress Coalition Cohesion | sectarian, communist, agrarian, or party fracture |
| Ratify the Common Programme [working] | P | Congress coalition has valid delegates | settle land, industry, religion, rights, armed wings, and constitutional form | deep concessions and delegate approval | opens constituent transition | one-party capture or armed-wing veto |
| Reassemble the National Corporate Party [working] | P | O'Duffy survives severe crisis gate and dormant networks exist | recruit veterans, employers, organisers, and patrons | money, foreign exposure, public backlash | creates limited movement capacity | infiltration, veteran refusal, or personal collapse |
| Impose Compulsory Estates [working] | P | corporate route controls government and has enough coercive capacity | replace voluntary councils with compulsory representation | security deployment, labour freedom, minority confidence | creates Corporate Estate Order | strikes, evasion, army refusal, or oligarchic capture |
| Organise Ailtirí Cells [working] | H/P | after wartime date gate and valid cultural, youth, clerical, or crisis conditions | build publishing, youth, local, and patron networks | secrecy, funds, exposure, recruitment | raises cell strength and public launch capacity | exposure, faction split, Church rejection, or police suppression |
| Launch the Ailtirí Party State [working] | P | public launch gate and crisis victory | merge party, administration, surveillance, mobilisation, and ideological offices | coercion, exclusion, minority collapse, foreign risk | installs Total Gaelic Vanguard and route laws | bureaucratic capture, Ceannaire rivalry, or broad resistance |
| Dissolve the Failed Underground [working] | P | radical route fails or accepts constitutional recovery | disarm, amnesty, prosecute, exile, or absorb named bodies | security, legitimacy, prison and employment costs | cleans command and movement flags while preserving historical memory | fragmented remnants create later violence or foreign networks |

## National Provision

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Set County Tillage Quotas [working] | H/P | food pressure or tillage law | assign crop obligations by soil, labour, machinery, livestock, and farm scale | inspectors, seed, price guarantees, rural consent | raises planted acreage and creates compliance missions | poorly designed quotas lower yields and legitimacy |
| Distribute Seed and Fertiliser [working] | H/P | planting season and imported or domestic stocks | allocate scarce inputs by county and crop | stocks, trains, trucks, administrative reach | improves harvest potential | diversion, late delivery, regional capture |
| Repair Mills and Storage [working] | H/P | harvest, milling, or storage bottleneck | tie factories, machinery, labour, and transport to named facilities | civilian factories, spare parts, fuel, time | improves usable food and reduces spoilage | delay, breakdown, local shortage |
| Purchase Emergency Livestock [working] | P | urban food or export shock | redirect animals from export or private trade into domestic supply | budget, rural consent, transport, cold storage | short-term food relief | herd depletion, smuggling, long-term rural damage |
| License Protected Workshops [working] | H/P | industrial route and import replacement need | authorise firms that can prove power, machines, labour, and demand | capital, materials, inspection | creates output and training missions | patronage licences, idle plant, price inflation |
| Commission a Developmental Plant [working] | P | Lemass or other developmental institution | select a regional industrial project through a portfolio test | two to five civilian factories, imported machinery, power, skilled labour | creates a construction and commissioning mission | foreign dependency, urban concentration, unfinished plant |
| Issue Ration Books [working] | H/P | acute scarcity or emergency supply law | allocate controlled goods by household and occupational rules | administrative reach, printing, enforcement, stocks | slows consumption and reveals distribution disputes | black market, exclusion, public anger |
| Rebalance Fuel Allocation [working] | H/P | Energy Continuity below 50 or transport competition | choose household, agriculture, rail, industry, military, or shipping priorities | fuel stocks and political consent | moves energy and serviceability with visible losers | stoppage, cold homes, harvest loss, military immobility |
| Mobilise Emergency Turf [working] | H/P | coal shortage and suitable bog regions | recruit labour, drain, cut, dry, move, and store turf | manpower, tools, transport, weather risk | raises seasonal Energy Continuity | wet turf, labour injury, rail congestion, land damage |
| Repair a Named Rail Corridor [working] | H/P | Provision route need with full control of states 113 and 135, endpoint infrastructure, and a launchable mission | reserve one civilian factory for 180 days and commit 5 Trains, 250 manpower, and 200 Fuel to the Dublin-to-Cork corridor | one factory, trains, manpower, fuel, route control, dynamic PP/CP | Transport Serviceability 50 and a connected level-1 railway is full success; 35 with the connection or both endpoint levels is partial success | sabotage, bridge failure, insufficient serviceability, or deadline failure; cancellation returns at most 3 Trains, 175 manpower, and 140 Fuel |
| Establish a Strategic Depot [working] | P | Provision or Readiness plan identifies a gap | build and stock a named depot with access and maintenance | factories, trucks, trains, fuel, guards | improves local delivery and military mobility | empty depot, theft, exposed target |
| Charter Foreign Tonnage [working] | H/P | Maritime Access below 50 and a willing owner or sponsor | lease a vessel under neutral, sponsor, or mixed terms | credit, leverage, insurance, crew, port access | adds temporary tonnage and a route mission | seizure, dependency, loss, diplomatic dispute |
| Purchase a Merchant Vessel [working] | H/P | Irish Shipping or equivalent authority and available market | buy or take over one vessel tier with repair and crew obligations | large finance, leverage, dockyard time, crew | adds durable tonnage after commissioning | unserviceable ship, debt, crew shortage |
| Reroute an Essential Cargo [working] | H/P | full control of state 135 with its receiving port and industrial complex, a live merchant route, the 135-to-113 railway, and a valid naval-base capacity tier | move a named cargo through the state-135 port and inland corridor; reserve no extra global port variable and commit 5 Convoys, 2 Trains, and 200 Fuel | convoys, trains, fuel, industrial/port platform, route, tier 1/2/3 capacity based on the patrol and lost-merchant missions | Maritime Access 50 is full success; Maritime Access 35 with a valid merchant route or railway is partial success | delay, spoilage, sinking, port congestion, or deadline failure; cancellation returns at most 3 Convoys, 1 Train, and 140 Fuel and clears origin flags |
| Launch an Emergency Housing Scheme [working] | P | urban overcrowding, Blitz relief, Northern integration, or postwar need | tie building materials and labour to a named urban region | civilian factories, timber, cement, labour, time | improves social consent and service capacity | unfinished estates, patronage, material diversion |
| Fund a Western Regional Portfolio [working] | P | regional development lane and valid local bodies | select roads, fisheries, power, schools, workshops, or housing as a linked programme | multi-year budget, local co-finance, transport | raises regional capacity and rural organisation | fragmented projects, clientelism, migration |

## National Readiness

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Run a Command District Exercise [working] | H/P | full control of state 113 with arms factory, infrastructure, one division, Supply Readiness 20, and the launchable mission | reserve the named command platform and commit 50 Infantry Equipment and 250 Fuel; no division is spawned, moved, renamed, or mutated | command power, equipment, fuel, one real division, platform, dynamic PP/CP | two divisions with Command 50 and Supply 35 is full success; one division with Command 35 and Supply 20 is partial success | invasion, coercive Northern campaign, home-defence emergency, accident, supply failure, or deadline failure; cancellation returns at most 35 Infantry Equipment and 175 Fuel |
| Standardise Infantry Equipment [working] | P | mixed calibres or foreign aid | select standards, convert stores, and train armourers | army XP, support equipment, factory time | raises usable Equipment Sufficiency | wasted stocks, sponsor dependence, workshop overload |
| Procure Rifles and Support Equipment [working] | H/P | valid domestic, British, American, German, or neutral channel | contract a delivered package with shipping and standards | credit, leverage, convoys, factories, political safeguards | adds equipment only after delivery mission | non-delivery, interdiction, dependency, incompatible equipment |
| Activate a Cadre Reserve [working] | H/P | mobilisation tier 0 and minimum command and equipment | call and train a bounded reserve cadre | manpower, rifles, officers, supply, 90 to 150 days | raises Mobilisation Depth and creates formations | paper units, desertion, civilian labour loss |
| Expand the Local Security Force [working] | H | internal security pressure and mobilisation tier 1 | recruit local part-time security under civil law | manpower, rifles, Garda and army liaison | improves local security with limited military value | politicisation, arms leakage, uneven recruitment |
| Expand the Local Defence Force [working] | H | invasion danger and mobilisation tier 2 | organise local defence, coastwatch, communications, and static tasks | manpower, equipment, training, local support | raises Mobilisation Depth and warning capacity | untrained mass, local faction capture, equipment drain |
| Motorise a Strategic Route [working] | P | Supply and Mobility gap and available trucks or trains | assign vehicles, fuel, repair, and priority to a named corridor | trucks, fuel, mechanics, road or rail service | raises mobility for one plan | civilian transport collapse, breakdown, fuel exhaustion |
| Build a Coastwatch Sector Network [working] | H/P | Marine and Coast Watching Service active | construct, staff, train, communicate, and relieve posts in one sector | manpower, support equipment, radios, roads | raises Coastal and Air Warning | gaps, false reports, exposure, fatigue |
| Install Harbour Defences [working] | H/P | valid port authority and transferred or controlled harbour | repair guns, magazines, searchlights, mines, command, and communications | artillery, support equipment, manpower, construction | raises Maritime Protection at one port | unsafe guns, untrained crews, access conflict |
| Organise Marine Patrols [working] | H/P | Marine Service or route equivalent plus a controlled Munster port with industrial and naval repair capacity | bind one dedicated coastal patrol-craft coverage allocation, assign fuel, crews, rescue, repair, and inspection patrols, and launch the named Neutral Approaches mission | 3 Convoys as the craft allocation (not ordinary merchant shipping), 250 Fuel, 250 manpower, 10 Naval Experience, named port platform, and mission capacity | raises local maritime protection and incident detection; the bound craft flag is rechecked by the map objective and cleared on every terminal result | craft loss, foreign confrontation, rescue failure, or missing repair/craft coverage fails the operation and releases the bound craft flag |
| Open a G2 Liaison Channel [working] | H/P | valid partner or Northern plan | define information class, scope, Irish control, exposure, and review | intelligence exposure, leverage, legal risk | raises Intelligence Coordination | penetration, public scandal, partner overreach |
| Turn or Intern a Foreign Agent [working] | H/P | identified agent and legal authority | choose surveillance, controlled use, internment, expulsion, or prosecution | security staff, exposure, diplomatic cost | disrupts network or yields intelligence | false arrest, escape, retaliation, compromised operation |
| Protect an Operational Plan [working] | P | Plan W, invasion, Northern, expeditionary, or occupation plan exists | vet staff, compartment records, test communications, and secure depots | time, intelligence capacity, trust | reduces plan-compromise risk | leak changes enemy and foreign reactions |
| Demobilise a Force Tier [working] | H/P | war danger falls or postwar review | release personnel, recover equipment, settle pay, and preserve cadres | administrative effort, veteran benefits, security risk | reduces mobilisation burden without erasing readiness | arms leakage, unemployment, mutiny, lost cadre |

## Neutrality and incidents

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Intercept an Airspace Violation [working] | H/P | detected aircraft and available warning or Air Corps response | identify, signal, escort, force landing, or document the flight | fuel, aircraft readiness, diplomatic risk | changes Integrity, leverage, intelligence, and internment state | missed contact, combat, crash, or public exposure |
| Intern a Belligerent Crew [working] | H | forced landing, shipwreck, or border entry | apply equal rules, camp, parole, exchange, or prosecution | camp capacity, guards, diplomacy, public law | supports neutrality when applied consistently | escape, unequal treatment, sponsor pressure |
| Release or Exchange Internees [working] | H/P | valid legal and diplomatic channel | negotiate medical release, exchange, parole, or repatriation | leverage, public trust, security review | reduces camp burden and alters partner relations | exposed favouritism or returned combatants harm Integrity |
| Investigate a Neutral Shipping Loss [working] | H/P | Irish or chartered vessel damaged or sunk | recover survivors, cargo records, navigation, belligerent evidence, and claims | Marine Service, intelligence, port capacity, time | assigns responsibility and opens protest or rerouting | uncertain cause, false accusation, crew unrest |
| Mark and Publicise Neutral Shipping [working] | H | merchant route active | maintain markings, lights, route notices, and diplomatic notification | paint, communications, route discipline | reduces some misidentification risk | does not prevent deliberate or accidental loss and can reveal routes |
| Share a Controlled Weather Report [working] | H/P | station data has strategic value and cooperation depth permits | choose public, equal, controlled Allied, restricted, or deceptive release | exposure, aviation safety, leverage, Integrity | affects operations and liaison without automatic belligerency | bias exposure, accident, foreign retaliation |
| Answer a Foreign Access Request [working] | H/P | partner seeks port, airfield, corridor, repair, weather, or intelligence access | refuse, time-limit, place under Irish command, share, or concede | sovereignty safeguards, leverage, public consent | creates a dated access agreement or refusal | dependency, secret access scandal, retaliation |
| Tighten or Narrow Censorship [working] | H/P | war, security, shortage, or political crisis | define subject, duration, appeal, and review | administrative reach, legitimacy, intelligence protection | changes exposure and public trust | permanent emergency, rumour, opposition radicalisation |
| Open a Border Corridor [working] | P | refugee, trade, relief, Plan W, or Northern settlement need | define persons, cargo, guards, hours, and inspection | units, police, transport, leverage | supports relief or cooperation | smuggling, infiltration, communal violence, foreign incursion |
| Restore Neutrality Integrity [working] | P | Integrity below 60 and no irreversible belligerency | review access, internment, liaison, trade, censorship, and public law | concessions to several stakeholders, partner disappointment | moves toward Practised or Credible Armed Neutrality | failed restoration can end in alignment, breakdown, or government fall |

## Foreign leverage and agreements

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Renegotiate a British Supply Contract [working] | H/P | British trade channel and a named shortage | bargain price, cargo, route, credit, access, and Northern terms separately | British Leverage, finance, shipping, political safeguards | creates delivered supply mission | non-delivery, leverage rise, access demand |
| Formalise Plan W Liaison [working] | H/P | invasion danger, Readiness, and legal cooperation gate | define contacts, maps, command, entry conditions, withdrawal, and secrecy | exposure, British Leverage, Irish command concessions | improves joint contingency planning | exposure or overbroad access damages Integrity |
| Send an American Procurement Mission [working] | H/P | American channel, shipping, credit, and legal authority | seek equipment, credit, machinery, food, or reconstruction aid | American Leverage, dollars or debt, access pressure | opens delivery and lobbying missions | embargo, neutrality criticism, debt dependency |
| Mobilise Diaspora Relief [working] | H/P | diaspora organisations and humanitarian need | coordinate competing organisations, funds, shipping, and public claims | domestic political concessions, foreign lobbying risk | delivers relief and recognition support | partition, neutrality, labour, or violence split |
| Receive a German Emissary [working] | H/P | valid diplomatic or clandestine contact | hear arms, intelligence, recognition, or ideological proposal | exposure, German Leverage, British reaction, movement cohesion | opens a delivery test or controlled channel | captured agent, false promise, client pressure |
| Demand Proof of German Delivery [working] | P | a German promise is active | require route, cargo, date, liaison, and independence safeguards | time, exposure, sponsor displeasure | filters real aid from propaganda | failed delivery weakens sponsor and may expose domestic actors |
| Seek Vatican Humanitarian Mediation [working] | H/P | war, prisoners, refugees, Church network, or international isolation | request mediation without granting domestic veto | Vatican Leverage, domestic Church expectations | supports relief or recognition | authoritarian, antisemitic, minority, or mythic policy invites criticism |
| Convene a Neutral States Consultation [working] | P | two or more valid neutral or small-state partners | share law, shipping, trade, internment, and postwar positions | diplomatic staff, travel, major-power pressure | creates a limited consultation forum | member defection or sponsor retaliation |
| Write Anti-Dependency Clauses [working] | P | any foreign agreement with leverage above 40 | set command, customs, debt, access, ownership, duration, withdrawal, and review limits | slower agreement, reduced immediate aid | lowers dependency indicators | partner refuses or circumvents safeguards |
| Terminate a Failed Sponsor Agreement [working] | P | sponsor defeated, inaccessible, defaulting, or violating terms | close access, settle property, recover personnel, and replace supply | short-term Provision and Readiness loss, diplomatic risk | prevents dead-sponsor logic and client collapse | abrupt termination triggers shortage or security vacuum |

## Northern settlement

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Open Cross-Border Confidence Measures [working] | P | no active major hostilities and at least one local partner | choose trade, health, rail, policing, prisoners, or relief as a named competence | political concessions, local staff, British notification | moves relevant ledger values and creates a joint body | sabotage, boycott, or jurisdiction dispute |
| Invite Northern Delegations [working] | P | proposal mandate and safe travel | invite unionist, nationalist, labour, local government, Church, industry, and civic delegates separately | security, representation concessions, time | creates valid representation ledger | Dublin-selected shell delegation invalidates settlement |
| Negotiate British Flexibility [working] | P | British government is able to bargain | link sovereignty, defence, finance, guarantees, timing, and local consent | British Leverage, access, wartime contribution, diplomacy | raises or lowers British Flexibility with recorded terms | British agreement alone never moves Unionist Consent |
| Protect Northern Campaign Freedom [working] | P | plebiscite or convention campaign | guarantee meetings, press, observers, policing, and dispute procedure | security deployments, external supervision, time | supports a valid result | intimidation, occupation, censorship, or boycott invalidates result |
| Convene a Federal Powers Conference [working] | P | federal threshold work begins | settle executive, legislature, finance, policing, education, religion, language, defence, and review | major concessions across all six ledger values | creates a ratifiable federal text | one missing actor or unfunded power blocks ratification |
| Draft a Unitary Safeguards Charter [working] | P | unitary threshold work begins | write local government, representation, policing, courts, schools, religion, language, finance, and guarantees | high consent and integration costs | creates a valid unitary proposal | majority rule without safeguards collapses confidence |
| Build a Labour Industrial Settlement [working] | P | Labour Cooperation and union freedom are viable | link wages, discrimination, housing, welfare, shipbuilding, linen, and public works | finance, employer concessions, union unity | raises Labour Cooperation and Integration Capacity | sectarian split, lockout, purge, or output collapse |
| Prepare a Wartime Unity Bargain [working] | P | 1940 crisis or comparable war state and fixed thresholds | define unity principle, interim bodies, defence contribution, ports, arms, guarantees, and ratification | Readiness, Provision, British Flexibility, unionist guarantees | opens multi-actor bargain chain | vague principle, absent arms, or imposed settlement fails |
| Plan a Coercive Northern Campaign [working] | P/A | route legitimacy, Readiness 60, mobility 45, Provision 55, valid cause | define command, Belfast, ports, corridors, occupation, rights, supply, and foreign reaction | large forces, equipment, fuel, trains, political legitimacy | opens war plan only after full proof | incomplete plan blocks action or causes catastrophic occupation |
| Defer the Constitutional Claim Lawfully [working] | P | government chooses non-escalation | retain claim policy while setting review, contact, rights, and no-war rules | political cost among republicans | closes reckless actions and preserves future diplomacy | permanent neglect weakens nationalist consent and route legitimacy |

## Occupation and integration

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Establish a Transitional Authority [working] | P/A | military control or recognised provisional settlement | separate military command, civil administration, courts, finance, and local representation | administrators, guards, money, legitimacy | creates integration stage 2 or occupation administration | military government without civil plan raises resistance |
| Vet and Rebuild Policing [working] | P | post-settlement or occupation stage | review command, recruitment, oversight, records, sectarian conduct, and local access | time, trainers, political concessions, security risk | improves Security Stability and ordinary policing | purge, impunity, or militarisation lowers consent |
| Disarm Paramilitary Organisations [working] | P | valid authority and security plan | offer registration, surrender, integration, prosecution, or monitored stand-down | units, intelligence, amnesty, prisons | reduces armed dual authority | unequal disarmament or arms leakage fuels insurgency |
| Maintain Welfare and Pensions [working] | P | transfer or settlement changes administration | continue payments, records, staff, and appeal rights | budget, data, local offices | raises Integration Capacity and confidence | missed payments create immediate legitimacy crisis |
| Restore Belfast Industrial Contracts [working] | P | occupation/provisional/integration authority, full control of state 119 with industrial complex and infrastructure, Labour Cooperation 30, and two available civilian factories | reserve two civilian factories for 300 days and commit 100 Support Equipment, 50 Trucks, and 250 Fuel to the Belfast contract | capital, fuel, trucks, support equipment, labour, two factory reservations, union agreement | Labour Cooperation 45 and Industrial Capacity 55 is full success; Labour 30 and Industrial Capacity 40 is partial success | requisition, capital flight, sabotage, contested platform, low labour, or deadline failure; cancellation releases factories and returns at most 70 Support Equipment, 35 Trucks, and 175 Fuel |
| Settle Education and Religious Safeguards [working] | P | integration stage 2 or higher | protect schools, worship, curricula, funding, language, and inspection | finance, Church and minority negotiations | raises both consent and Minority Confidence | forced assimilation or denominational crisis |
| Merge Tax and Debt Administration [working] | P | integration stage 3 or higher | allocate liabilities, pensions, tax, transfers, guarantees, and audits | finance staff, budget, external creditors | raises Integration Capacity | insolvency, hidden debt, external financial control |
| Integrate or Devolve Military Command [working] | P | security stable enough and British withdrawal terms exist | choose common force, devolved units, demobilisation, pensions, bases, and oath | equipment, training, command concessions | creates loyal structure | mutiny, duplicate command, foreign occupation |
| Review Foreign Guarantees [working] | P | guarantee is active and integration stage changes | renew, narrow, replace, or end monitoring and veto rights | diplomatic concessions and security proof | normalises sovereignty or preserves confidence | permanent foreign veto or premature withdrawal |
| Conduct the Core Eligibility Review [working] | P/A | integration stage 5 and all fixed final tests | review rights, representation, services, policing, resistance, finance, guarantees, and demobilisation | long review with no shortcut | permits cores only where every test passes | failure keeps claims or integrated non-core status and opens remediation |

## Regional orders and external ambitions

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Invite a Celtic Cultural Partner [working] | H/P | serious cultural contact and an eligible partner | offer language, archives, universities, festivals, and broadcasting cooperation | diplomatic staff, cultural budget | creates voluntary cultural institution | refusal has no territorial consequence |
| Draft an Atlantic Consultation Charter [working] | P | two or more willing states and adequate diplomacy | define consultation, shipping, intelligence, rescue, trade, and exit | contributions, neutrality or alliance compatibility | creates a limited organisation | overbroad defence commitment blocks neutral members |
| Propose a Regional Defence League [working] | P | Readiness 75, valid members, common threat, command and supply | set membership, command, contributions, goals, and exit | forces, finance, sovereignty concessions | creates league after ratification | paper league, sponsor capture, or member refusal |
| Recognise a Liberated Authority [working] | P | war or collapse produces a valid local authority | recognise, fund, arm, advise, or withhold support | equipment, convoys, leverage, legal risk | opens aid and legitimacy missions | puppet pressure, faction conflict, dead authority |
| Offer a Protectorate Treaty [working] | P/A | local authority requests protection or route conquest allows treaty | define rights, defence, finance, administration, exit, and recognition | large obligations and foreign reaction | creates subject only after consent or conquest settlement | unfunded or coercive treaty creates resistance and dependency |
| Convene a Crown Association [working] | P/A | valid elected crown and willing partner | offer ceremonial, arbitration, defence, or cultural association under public law | royal legitimacy, partner ratification, finance | creates voluntary association | captured crown or dynastic demand causes rejection |
| Renew the Fivefold Compact [working] | P/A | Five Provinces route and valid mandates | review powers, finances, vetoes, services, command, and middle province | provincial concessions, federal budget | raises Federal Cohesion | veto or unequal capacity opens provincial crisis |
| Fulfil a Compact Obligation [working] | A | Otherworld compact has a due obligation | deliver a named site, season, stewardship, restraint, or public-law duty | resources, units, political limits, cultural capacity | maintains human and compact defence | breach changes territory, legitimacy, and exceptional effects |
| Dissolve a Failed Regional Order [working] | P/A | membership, war goal, sponsor, or cohesion collapses | settle forces, property, debts, guarantees, subjects, and claims | diplomatic time and possible losses | prevents orphaned factions and obligations | unmanaged collapse triggers wars, subjects, or dependency |
| Integrate a Voluntary Member Contribution [working] | P/A | organisation has members and a shared project | accept troops, ships, finance, intelligence, or infrastructure under agreed command | administrative and sovereignty safeguards | raises organisation capacity | free contribution loops and uncommanded units are forbidden |

## Postwar transition

| Action | Class | Availability | Concrete work | Cost | Result | Failure and cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| Review the Emergency Declaration [working] | H/P | major war end or scheduled postwar review | decide continuation, narrowing, replacement, or expiry of emergency authority | cabinet, Dáil, courts, security and supply evidence | starts legal unwinding or bounded continuation | automatic expiry or permanent emergency without review is invalid |
| Replace Emergency Supply Orders [working] | H/P | controls remain after war | move rationing, price, import, transport, and service powers onto temporary postwar law | administrative effort, consumer and producer bargaining | prevents abrupt collapse while setting expiry | black market, inflation, or authoritarian continuity |
| Demobilise and Settle Veterans [working] | H/P | mobilisation tier above 0 after danger falls | release forces, preserve cadres, provide pay, training, housing, land, and employment | budget, housing, equipment recovery, labour absorption | reduces burden and preserves loyalty | unemployment, arms leakage, militant veterans |
| Renew the Merchant Fleet [working] | P | Irish Shipping or equivalent survives | decide debt, ownership, commercial purpose, vessel replacement, and routes | capital, dockyard access, credit, crews | creates a postwar shipping institution | liquidation, debt dependency, obsolete fleet |
| Launch a Reconstruction Portfolio [working] | P | Provision and administration can support it | select housing, transport, power, ports, schools, hospitals, and regional projects | multi-year factories, finance, labour, imported materials | creates phased reconstruction missions | overreach, regional inequality, foreign dependency |
| Settle the Republic Question [working] | H/P | constitutional government and external policy review | choose historical 1948 to 1949 procedure or route-valid alternate settlement | Dáil mandate, President, external law, Commonwealth relations | changes legal and country identity after commencement | cosmetic change without law is blocked |
| Review Commonwealth Relations [working] | H/P | republic or constitutional status changes | negotiate recognition, citizenship, trade, defence, and diplomatic form | British Leverage and economic safeguards | creates stable external relationship | trade retaliation, legal ambiguity, or dependency |
| Apply for United Nations Membership [working] | H/P | recognised postwar state and valid world organisation | build support, answer vetoes, define neutrality and contribution | diplomatic capital, partner positions, recognition | opens multilateral route and possible delayed admission | rejection creates renewed campaign rather than instant success |
| Accept or Refuse Reconstruction Aid [working] | P | valid foreign or multilateral programme | negotiate money, goods, markets, planning, access, and conditions | dependency risk and domestic policy concessions | supports projects under safeguards | aid capture, debt, or policy veto |
| Complete the Route Conclusion Review [working] | P/A | route seeks final conclusion | test government, law, economy, defence, foreign policy, Northern status, emergency, demobilisation, and identity | no direct click reward, all systems must resolve | fires route-specific conclusion and consolidation mission | unresolved surfaces block conclusion and name exact remediation |


# Mission inventory

| Mission | Family | Region | Duration days | Objective | Full success | Partial success | Failure | Cleanup |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Maintain Cabinet Discipline [working] | Settlement | national | 90 to 120 | keep Cabinet Cohesion at 60 or more and resolve every dissenting portfolio | stable cabinet and route review progress | cabinet survives with one conditional minister and a dated concession | resignation cascade, lost confidence, caretaker | remove temporary dissent and portfolio flags |
| Assemble Seventy Routine Votes [working] | Settlement | Dáil | 30 to 60 | secure 70 routine confidence votes through parties and named support agreements | lawful government formation | minority cabinet with a short confidence deadline | dissolution or caretaker | clear provisional coalition promises that were not ratified |
| Complete the Six-Month Settlement Review [working] | Settlement | national | 180 | meet route-specific authority, consent, law, office, security, Provision and Readiness tests | route settlement confirmed | conditional settlement with one recovery mission | route collapse or restoration branch | archive transition flags and replace route spirit form |
| Conduct a Free General Election [working] | Election | national poll or named by-election regions | 100 or 105 | complete the register, campaign freedom, polling security, candidate slate and count in the selected mode | valid seat ledger and mandate | valid result with regional disputes or recount | invalid election, boycott, or violence crisis | clear campaign modifiers, candidate locks, and temporary pacts |
| Form a Government After the Poll [working] | Election | Dáil | 45 to 75 | nominate Taoiseach, reach 70 routine votes, assign portfolios, ratify charter | government installed | caretaker or confidence and supply government | new election or presidential crisis | remove unaccepted office offers and negotiation flags |
| Consolidate the Movement Network [working] | Radical | named platform in Leinster, Munster, or the Western Seaboard | 150 | consolidate the IRA, Congress, corporate, or Ailtirí underground platform in the named region | recognised movement network and route progress | fractured cell structure with a dated repair | exposure, faction split, or escalation | clear temporary command state and retain the movement result |
| Secure Constituent Authority [working] | Radical | Dublin Metropolitan Region or named regional authority | 180 | secure the named constituent authority objective under the active radical mode | recognised constituent authority and route progress | conditional authority with a review obligation | exposed claim, coercive failure, or escalation | clear temporary constitutional state and retain the authority result |
| Deliver the Education Settlement [working] | Organised society | two named regions | 120 to 180 | open schools, appoint staff, fund agreed management, and preserve minority access | education law becomes stable | one region succeeds and one requires review | boycott, closure, or forced-assimilation crisis | replace temporary school dispute state |
| Keep Essential Services Running [working] | Organised society | named service system or three parish service networks | 60 or 120 | restore the named service or audit access, finance, staffing, and oversight in the selected mode | service ledger restored or contract renewed | conditional service or contract review | stoppage, scandal, withdrawal, or dependency increase | end temporary staffing, audit targets, and service flags |
| Collect a National Folklore Cycle [working] | Culture | Gaeltacht and three provincial regions | 180 | complete school, collector, archive and custody objectives | verified records and cultural capacity | partial regional collection with provenance warnings | fabricated, lost, or politicised collection | archive evidence class and remove temporary collector teams |
| Hold a Five-Region Cultural Congress [working] | Culture | Dublin plus four provincial centres | 180 to 270 | secure delegates, transport, programme, rights and regional participation | provincial cultural institutions mature | congress held with one boycott | central capture or regional failure | clear temporary delegations and venue states |
| Verify the Restoration Evidence [working] | Culture | named archives and sites | 180 to 365 | meet provenance, independent review, site custody and unusual-condition requirements | valid H to P or P to A transition | unresolved evidence delays reveal | false lead, fraud, panic, or route closure | clean false lead, evidence, and public-knowledge flags according to result |
| Meet the County Tillage Schedule [working] | Provision | selected rural counties | 120 to 180 | deliver seed, fertiliser, labour and machinery and reach tailored acreage targets | Food Security and Rural Organisation rise | acreage reached with poor yield or consent cost | quota failure, farm resistance, urban shortage | remove seasonal quotas and retain harvest outcome |
| Bring the Harvest to Market [working] | Provision | rural region to named city or port | 90 to 120 | keep road or rail open, provide fuel, storage, milling and fair purchasing | usable food stocks delivered | part delivered with spoilage or price dispute | transport or storage collapse | release tied vehicles and temporary purchasing orders |
| Commission the Protected Workshop Network [working] | Provision | two industrial regions | 150 to 240 | install machines, power, inputs, labour and orders | durable industrial capacity | one site operates and one remains dependent | idle licences, patronage, or power failure | close failed licences and clear tied factories |
| Complete a Developmental Plant [working] | Provision | named industrial site | 240 to 365 | finish construction, import machines, train workers, secure power and market | plant opens with route-specific production | plant opens below capacity and needs follow-up | unfinished project, debt, labour or input failure | release factories, record debt and site status |
| Supply the Capital Through Winter [working] | Provision | Dublin Metropolitan | 90 to 150 | maintain food, fuel, transport and ration distribution above minimum levels | consent and Provision protected | one good remains scarce | urban stoppage, cold, riot, or black market | expire winter orders and retain stock results |
| Cut and Dry the Turf [working] | Provision | Midlands and one western region | 90 to 150 | recruit labour, meet dry-tonnage and transport objectives | seasonal energy reserve | tonnage produced with transport or quality loss | wet season failure or labour crisis | release seasonal labour and vehicles |
| Restore the Dublin to Cork Corridor [working] | Provision | states 113 and 135 under full control with endpoint infrastructure and the active rail action/mission | 180 days | restore the named connection and endpoint level 1 while maintaining Transport Serviceability | Transport Serviceability 50, connection, and both level-1 endpoints | Transport Serviceability 35 with the connection or both endpoint levels | broken route, lost control, low serviceability, sabotage, or deadline failure | clear engineering flags and return only the capped 3 Trains/175 manpower/140 Fuel cancellation share |
| Keep an Essential Cargo Route Open [working] | Provision | state-135 receiving port, industrial complex, live route, 135-to-113 railway, and tiered naval capacity under the active action/mission | 120 days | maintain vessel, crew, port, intelligence and inland distribution with the named capacity tier | Maritime Access 50 and full route capacity | Maritime Access 35 with a valid route or railway | sinking, seizure, port closure, crew refusal, capacity loss, or deadline failure | clear charter/neutral-procurement origin flags and return only the capped 3 Convoys/1 Train/140 Fuel cancellation share |
| Replace a Lost Merchant Vessel [working] | Provision | Irish Shipping fleet | 180 to 365 | secure finance, vessel, repairs, crew and route certification | tonnage restored | temporary charter substitutes for purchase | debt or market failure | close procurement offers and retain financial obligation |
| Deliver a Western Regional Portfolio [working] | Provision | Connacht and Western Seaboard | 240 to 365 | complete at least three linked road, power, fishery, school, workshop or housing projects | regional capacity and consent rise | two projects succeed and one is deferred | fragmentation, patronage or migration | archive completed projects and cancel undelivered promises |
| Prove the Command District [working] | Readiness | state 113 arms/infrastructure platform, active exercise provenance, one real division, and Supply Readiness 20 | 105 days | maintain one or two existing divisions in the named district and complete movement, communication, and defence tasks | two divisions, Command 50, and Supply 35 | one division, Command 35, and Supply 20 | invasion, coercive Northern campaign, home-defence emergency, accident, breakdown, command refusal, or deadline failure | leave unit placement untouched and clear only exercise flags; cancellation recovery is capped at 35 Infantry Equipment/175 Fuel |
| Equip a Reserve Brigade [working] | Readiness | named mobilisation district | 120 to 180 | provide manpower, rifles, support equipment, officers and training | formation becomes deployable | understrength cadre remains | paper unit drains equipment and consent | return unused manpower and remove provisional template |
| Secure the Dublin to Belfast Corridor [working] | Readiness | Dublin to Belfast Corridor | 90 to 150 | place supplied formations, protect bridges and depots, maintain civilian passage | mobility and Northern planning improve | military route secured with civilian disruption | corridor blocked, sabotaged or politically inflamed | stand down units and restore civilian priority |
| Complete a Coastwatch Sector [working] | Readiness | one of six coastwatch sectors | 120 | staff posts, train recognition, connect communications, supply relief and test reporting | warning coverage rises | coverage with communication or staffing gap | blind sector or compromised post | replace temporary construction and training states with sector status |
| Defend a Treaty Port [working] | Readiness | Cobh, Berehaven or Lough Swilly | 180 to 270 | repair guns, train crews, stock magazines, connect warning and define command | Maritime Protection rises | port usable under limited conditions | unsafe defence, access crisis, or foreign demand | archive inventory and clear borrowed crews |
| Patrol the Neutral Approaches [working] | Readiness | one coastal sector and port with the action-specific craft commitment, shipping authority, warning/rescue coverage, and repair platform | 105 days | maintain the committed craft, fuel, crews, rescue, repair, and inspection coverage | full success improves detection and rescue; partial success preserves limited coverage with maintenance cost | craft loss, confrontation, or an uncovered route records failure/escalation | release patrol crews and the craft commitment on cancellation, timeout, full, partial, failure, escalation, and route cleanup |
| Protect Plan W [working] | Readiness | border and command centres | 120 | vet liaison, secure maps, test communications and protect depots | Intelligence Coordination and plan reliability improve | plan survives with limited exposure | documents or contacts compromised | clear temporary event targets and update exposure history |
| Demobilise Without Losing the Cadre [working] | Readiness | national | 180 to 270 | release personnel while preserving officers, equipment, depots and records | burden falls and readiness retains a floor | cadre preserved with unemployment or equipment loss | arms leakage, mutiny, or total capability collapse | close wartime mobilisation decisions and create veteran state |
| Resolve an Aircrew Internment Case [working] | Neutrality | camp and landing site | 60 to 120 | apply law, secure camp, handle diplomacy and prevent escape | Integrity protected | case resolved with sponsor resentment | escape, unequal treatment or violence | clear crew targets, camp modifiers and diplomatic demands |
| Investigate a Merchant Sinking [working] | Neutrality | loss location, home port and foreign channel | 90 to 150 | recover survivors, identify cause, preserve evidence and decide protest | route, claims and foreign reaction updated | cause remains uncertain and route is adjusted | false accusation or no rescue | archive evidence and remove temporary search state |
| Maintain Equal Belligerent Rules [working] | Neutrality | national | 120 to 180 | apply internment, access, censorship and rescue law consistently across incidents | Integrity and consent improve | one exception is publicly defended | pattern of bias creates Selective Neutrality | expire incident comparisons after review |
| Keep the Blacksod Station Reporting [working] | Neutrality | Mayo and Blacksod | 90 to 120 | staff station, maintain equipment, protect communication and choose report policy | weather capability and liaison improve | reports continue with exposure or equipment cost | station failure, accident or exposed bias | clear temporary operation and retain report history |
| Deliver a British Supply Agreement [working] | Foreign | named British port, Irish port and inland corridor | 90 to 180 | load, sail, unload and distribute the contracted goods under safeguards | goods and leverage change after delivery | partial cargo or delayed delivery | non-delivery, seizure, access demand | close contract and retain obligations or dispute |
| Complete an American Procurement Mission [working] | Foreign | Washington, Atlantic route and Irish receiving port | 180 to 270 | secure licence, credit, cargo, shipping and compatible standards | delivered aid and American relationship change | credit or political support without full delivery | embargo, debt or access pressure | close mission and record outstanding debt |
| Test a German Arms Promise [working] | Foreign | German contact route and Irish landing or transfer point | 90 to 180 | prove cargo, route, independence and security | aid arrives only if all steps succeed | intelligence or propaganda value without arms | capture, betrayal, client demand or no delivery | remove promised stock and update exposure |
| Conclude a Vatican Relief Mediation [working] | Foreign | Vatican channel and named humanitarian case | 90 to 150 | secure parties, passage, funds and domestic service delivery | relief and diplomatic standing improve | limited mediation | domestic veto claim or foreign criticism | close temporary delegation and separate Vatican from Church state |
| Open the Cross-Border Health Service [working] | Northern | Border Belt and matched Northern districts | 120 to 180 | agree jurisdiction, staff, funding, transport and patient access | functional cooperation and integration capacity rise | pilot service with limited districts | boycott, funding dispute or security closure | replace pilot body with permanent or closed state |
| Secure a Representative Northern Convention [working] | Northern | Belfast, Derry, border and local delegations | 180 to 270 | seat unionist, nationalist, labour, local, industrial and religious delegates under valid rules | proposal can proceed | one bloc attends conditionally | shell convention or boycott invalidates settlement | clear temporary delegates and record participation history |
| Conduct a Supervised Plebiscite [working] | Northern | defined districts | 180 to 270 | complete registers, boundaries, security, observers, campaign freedom, count and dispute process | valid district results | some districts valid and others require rerun | occupation, intimidation or register failure invalidates result | archive ballots and clear campaign modifiers |
| Ratify the Federal Settlement [working] | Northern | Dáil, Northern bodies and British process | 180 to 365 | ratify powers, finance, rights, policing, defence, guarantee and transition | integration stage 2 begins | conditional ratification with review clauses | one required authority rejects | remove proposal-only bodies and open transition authority |
| Take and Hold Belfast [working] | Northern occupation | Belfast Urban and Harbour plus corridors | 90 to 180 | control city, docks, power, rail, depots and supply while limiting civilian harm | military objective completed and occupation begins | city held with severe damage or isolation | campaign failure, intervention, supply collapse | create occupation zones and clear attack orders |
| Restore Ordinary Policing [working] | Integration | three Northern policing districts | 180 to 270 | recruit, vet, train, oversee and transfer duties from military units | Security Stability and integration stage rise | mixed military and civil policing continues under review | sectarian force, purge or insurgency | withdraw temporary military police where successful |
| Reopen Belfast Industry [working] | Integration | state 119 under full control with industrial/infrastructure platform, active contract provenance, Labour Cooperation 30, and the reserved two-factory project | 300 days | restore power, workers, contracts, inputs, transport, management and security | Labour 45 and Industrial Capacity 55 | Labour 30 and Industrial Capacity 40 | requisition collapse, sabotage, low labour, contested platform, no market, or deadline failure | release the two factories, preserve outcome history, and return only the capped 70 Support Equipment/35 Trucks/175 Fuel cancellation share |
| Complete the Stage Five Integration Review [working] | Integration | all Northern regions | 365 | meet rights, representation, services, policing, resistance, finance, guarantees and demobilisation tests | stable constitutional integration and possible core review | integrated non-core status with remediation | stage falls or settlement reopens | archive transitional bodies and remove obsolete occupation modifiers |
| Ratify a Regional Charter [working] | Regional order | all member capitals | 180 to 270 | secure membership, contribution, command, goals, exit and dispute rules | organisation forms | limited consultative body forms | insufficient members or sponsor capture | clear invitations and provisional offices |
| Meet the Member Contribution Schedule [working] | Regional order | named member contributions | 180 | deliver finance, units, shipping, intelligence or infrastructure under valid command | cohesion and capability rise | partial contribution with renegotiation | free rider, refusal or command dispute | expire contribution mission and record compliance |
| Fulfil the Compact at Five Sites [working] | Otherworld | five named sites | 180 to 365 | hold, service and obey site-specific obligations with human administration intact | compact remains stable | four sites succeed and one requires penance | breach, site loss or supernatural dominion | clear due obligations and create next cycle |
| End Wartime Rationing Safely [working] | Postwar | national and two vulnerable urban regions | 180 to 270 | replace controls only after stocks, imports, prices and transport meet floors | ration law narrows or expires | some goods remain controlled | inflation, shortage, black market or political crisis | remove ended ration categories and keep continuing ones |
| Settle the Demobilised Forces [working] | Postwar | national and veteran concentration regions | 180 to 365 | complete pay, employment, housing, training, land and equipment recovery | veteran settlement and stable demobilisation | cadres settle while unemployment persists | militant veterans, arms leakage or government fall | clear force-tier flags and create long-term veteran outcome |
| Bring the Republic Settlement into Force [working] | Postwar | Dáil, President and external legal channels | 90 to 180 | pass law, set commencement, update external relations, offices and identity | legal country identity changes on the valid date | law passes with delayed external settlement | constitutional or coalition collapse | remove obsolete constitutional names and preserve historical offices |
| Build Support for United Nations Admission [working] | Postwar | eligible member states and Security Council actors | 180 to 365 | secure recognition, answer objections and define contribution | application advances or admission occurs when world state permits | application remains pending with support gained | rejection or veto creates later campaign | close obsolete lobbying targets and retain support ledger |
| Complete National Reconstruction [working] | Postwar | three named project regions | 365 | finish housing, transport, power, ports, schools or hospitals under balanced finance | route conclusion material gate satisfied | two regions complete and one remains under programme | debt, labour, import or regional failure | archive completed projects and retain debt or unfinished works |

# Mission collision rules

- A region cannot host two missions that require the same units, trains, convoys, port capacity, or factories unless the tooltip shows the split and both remain feasible.
- A national emergency mission can pre-empt one routine mission. The routine mission pauses and does not fail during the pause.
- A route transition cancels missions owned only by the defeated authority. Shared public-service and humanitarian missions transfer after an office and funding review.
- A sponsor mission ends immediately when the sponsor is invalid. Delivered goods remain. Promised goods vanish. Debt and exposure remain.
- A Northern settlement mission and an occupation mission cannot apply to the same district under contradictory authority.
- A hidden evidence mission never occupies a critical Provision, invasion, or occupation slot.

# Success, partial success, and failure map

| Outcome | Minimum proof | Reward rule | Follow-up |
| --- | --- | --- | --- |
| full success | all named objectives met inside timer | full value, institution, map or lifecycle effect | maintenance, next tier or conclusion |
| partial success | defined subset met and no disqualifier | limited effect with named debt, gap or risk | repair mission or conditional review |
| failure | timer ends or disqualifier triggers | meaningful loss, crisis, harder follow-up or route change | escalation or recovery |
| cancellation | authority or campaign state makes objective invalid | recoverable inputs capped at 70 percent | explicit cleanup and history record |
| bypass | objective already achieved by a valid external state | only effects supported by that state | reason recorded for audit |

# Cleanup map

| Trigger | Cleanup | Preserved record | New surface |
| --- | --- | --- | --- |
| government replacement | cancel government-only decisions, confidence missions, provisional ministers and private agreements | retain election, party, Dáil and historical office records | new government revalidates laws and foreign agreements |
| election defeat | remove campaign modifiers, candidate promises and temporary popularity actions | retain seats, party organisation, debts and coalition red lines | update opposition and succession access |
| coalition collapse | end charter benefits, return portfolios, clear support votes, start caretaker or election | retain policy concessions already enacted and breach memory | no duplicate cabinet offices |
| leader death or resignation | vacate only held offices, cancel personal missions, start valid succession | retain party, government and movement institutions | historical date pressure applies unless alternate survival was earned |
| route transition | archive old category actions, transform National Settlement labels, clamp value, start six-month review | retain all historical ledgers and material conditions | no reset to ideal values |
| war entry | close incompatible neutrality restoration actions, review internment, access and censorship | retain incident history, obligations and public law | open belligerency, home defence and contribution missions |
| peace and demobilisation | end war-only access, mobilisation, requisition and operational missions | retain veterans, debt, damage, equipment and foreign obligations | start postwar reviews |
| sponsor defeat or withdrawal | cancel deliveries, advisers, access and sponsor-only decisions | retain debt, exposure, local clients and captured equipment | open replacement, neutrality restoration or client-collapse chain |
| Northern settlement | close claim-only, war-only or negotiation-only actions according to model | retain consent, security, representation and guarantee history | open stage-specific integration category |
| occupation end | remove military zones, requisition and occupation offices | retain damage, resistance, collaborators, debt and service records | open withdrawal, restoration or integration review |
| core grant | close integration remediation only for passing regions | retain rights and service review history | no blanket core grant across failed districts |
| false cultural lead | remove evidence and reveal flags tied to the false claim | retain serious archive, language and site benefits | open public explanation, fraud or recovery event |
| hidden route failure | remove exceptional offices, due obligations and impossible actions | retain damage, public knowledge, sites and historical institutions | open constitutional, provincial, crown or stewardship recovery |
| compact breach | suspend exceptional benefits, mark due obligations failed, open containment or penance | retain human law and site state | do not erase ordinary Provision or security burdens |
| regional order dissolution | remove shared decisions, commands, temporary contributions and offices | retain bilateral treaties, debt and war consequences | resolve members and subjects individually |
| postwar conclusion | expire temporary crisis modifiers, close unresolved projects or convert them into dated programmes | retain final three spirits, laws, offices and identity | route conclusion cannot hide an unresolved crisis |

# Part 6 handoff

Part 6 receives category icon families, AI priority inputs, objective state types, map-region names, mission success and disqualifier flags, and achievement hooks. It cannot change category ownership, active caps, critical-slot rules, or the requirement for concrete objectives.
