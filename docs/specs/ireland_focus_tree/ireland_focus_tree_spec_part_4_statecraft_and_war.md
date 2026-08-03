# Ireland focus tree Part 4: statecraft and war

Feature slug: `ireland_focus_tree`

Planning part: 4 of 7

Status: source specification

Mode: planning only

All route, focus, decision, mission, idea, law, achievement, interface, and conclusion names in this file are working labels unless they are historical proper names.

Classification key:

- `H`: documented history or direct institutional extension
- `P`: plausible speculation grounded in real institutions, factions, strategic problems, or dated possibilities
- `A`: deliberate absurdity opened through the Part 3 hidden-route rules

# Material promise

Part 4 turns the political victories of Parts 2 and 3 into governments that must feed people, move goods, defend territory, enforce or abandon neutrality, bargain with foreign powers, confront partition, and survive the postwar settlement.

Ireland begins with political sovereignty that exceeds its material capacity. It has land, ports, a national electrical institution, a small regular military, an experienced civil service, major cultural and political networks, and access to British trade. It lacks secure fuel, shipping, modern weapons, large industrial reserves, air defence, naval power, and the ability to absorb Northern Ireland without prolonged negotiation or coercion.

The player must build capacity through projects, organisations, regional bargains, foreign contracts, mobilisation, and institutional reform. A focus may open a programme or change its rules. It cannot grant the finished result without delivery.

The Part 4 gameplay loop is:

1. choose which shortages receive priority
2. build National Provision through regional projects and supply policy
3. convert provision into National Readiness without exhausting the civilian economy
4. operate the Neutrality Ledger under repeated incidents and foreign pressure
5. bargain for trade, arms, information, access, recognition, and sovereignty safeguards
6. decide whether partition is deferred, negotiated, federalised, contested, or fought over
7. integrate any territorial settlement through government, security, industry, services, finance, and rights
8. transform Emergency institutions into a postwar economy, defence policy, and international identity

No government receives a free material package. De Valera's constitutional legitimacy does not create fuel. Lemass's developmental standing does not create machine tools. Dillon's moral case for intervention does not create divisions. An IRA command does not create army obedience. A Congress committee network does not create industrial output. A corporate state does not create efficient production. A crown does not create a treasury. A provincial federation does not create common supply. An Otherworld compact does not remove the need for food, transport, public consent, or command.

# Shared statecraft architecture

Part 4 adds four connected systems.

| System | Function | Opening state | Main outputs |
| --- | --- | ---: | --- |
| `National Provision` | measures whether Ireland can feed the population, keep energy flowing, move goods, and maintain maritime access | `38` | civilian resilience, project delivery, mobilisation ceiling, shortage risk |
| `National Readiness` | measures usable command, equipment, mobilisation, mobility, warning, maritime protection, and intelligence capacity | `15` | deterrence, mobilisation quality, war gates, invasion response |
| `Neutrality Integrity` and the Neutrality Ledger | measures whether declared policy, territorial control, public law, and actual conduct remain coherent | normal September 1939 opening `72` | incident outcomes, access, internment, covert cooperation, alignment pressure |
| `Northern Settlement Ledger` | keeps unionist, nationalist, labour, British, security, and integration conditions separate | six opening values | negotiations, plebiscites, bargains, conflict, transition, integration |

External Leverage remains source-specific. British, American, German, and Vatican Leverage are not merged into one value. Each agreement records obligations, safeguards, exposure, and dependency consequences.

The National Settlement remains the central political balance. Part 4 never resets its value or stages. Provision, readiness, neutrality, and Northern statecraft alter its contributors because material performance changes legitimacy, command authority, public consent, and institutional confidence.

# National Provision

## National Provision purpose

`National Provision` answers one practical question: can the government deliver the food, energy, transport, and maritime access required by its policy?

The range is `0` to `100`. The displayed opening value is `38`, calculated as the rounded arithmetic mean of four components.

| Component | Opening value | Measures |
| --- | ---: | --- |
| Food Security | `55` | output, agricultural inputs, storage, prices, nutrition, imports, and local distribution |
| Energy Continuity | `25` | coal, oil, turf, peat, electricity, generation, storage, and allocation |
| Transport Serviceability | `40` | rail, roads, rolling stock, vehicles, horses, depots, bridges, repair, and local delivery |
| Maritime Access | `30` | merchant tonnage, crews, ports, charters, repair, routes, insurance, and foreign access |

```text
55 + 25 + 40 + 30 = 150
150 / 4 = 37.5
Displayed opening National Provision = 38
```

Industrial output is derived from these four components and the institutions that organise capital, labour, skills, standards, machinery, and contracts. It remains a visible project result and route capability. It is not a fifth Provision component.

## Provision bands

| Range | State | Meaning | Typical gameplay |
| --- | --- | --- | --- |
| `0` to `19` | Systemic Breakdown | national distribution and essential services cannot sustain policy | national emergency, cascading service failure, compulsory prioritisation |
| `20` to `34` | Acute Scarcity | severe rationing and improvisation keep the state functioning | stoppages, black markets, regional inequality, foreign leverage |
| `35` to `49` | Strained Provision | ordinary government functions with little shock capacity | opening priority choices, partial project delivery, mobilisation limits |
| `50` to `64` | Managed Supply | the state can absorb limited shocks and complete ordinary programmes | reliable projects, stable rationing, credible mobilisation support |
| `65` to `79` | Resilient Provision | prolonged mobilisation or reconstruction is sustainable | advanced defence, regional programmes, support to partners |
| `80` to `100` | Strategic Capacity | the economy can sustain exceptional national or regional programmes | total mobilisation, deep reconstruction, highest late-game ambitions |

## Provision bottlenecks

A high mean cannot conceal a critical shortage.

- any component below `20` caps National Provision at `35`
- two or more components below `30` cap National Provision at `45`
- any component at `0` begins a national emergency
- Food Security below `20` creates nutritional, price, and public-order pressure
- Energy Continuity below `20` disrupts rail, industry, electricity, air operations, and military mobility
- Transport Serviceability below `20` prevents national projects from delivering full effects outside their source region
- Maritime Access below `20` makes overseas contracts unreliable and sharply raises foreign leverage
- National Provision below `35` caps prolonged mobilisation gains even when emergency law can produce a temporary surge

## Provision update rhythm

Provision is reviewed monthly and after major shocks. The update reads completed and maintained projects, route laws, stocks, harvest conditions, shipping loss, damaged infrastructure, trade agreements, mobilisation, bombing, occupation, regional compliance, and emergency controls.

Ordinary monthly movement stays limited. Harvest failure, port seizure, major ship loss, bombing, invasion, or completion of a national network can cause a larger immediate change. Part 5 owns exact constants and breakdown tooltips.

Provision cannot be farmed through repeated cheap actions. Projects need one-time completion flags, regional capacity, escalating costs, maintenance, replacement, or a defined higher stage.

## Regional provision model

National Provision is supported by regional delivery records. These are not extra national meters. They are state or regional records used by projects, missions, and events.

| Region | Core material role | Opening pressure | Strategic projects |
| --- | --- | --- | --- |
| Dublin and the eastern approaches | administration, imports, finance, distribution, repair, population | port congestion, housing, fuel dependence, air exposure | port warehouses, rail sorting, emergency depots, air warning, industry standards |
| Cork Harbour and south-west approaches | Treaty Port defence, deep water, repair, food exports, Atlantic access | coastal-defence burden, imported fuel, scattered approaches | harbour defence, ship repair, oil storage, naval examination, rail link |
| Waterford and Rosslare corridor | eastern and southern trade, food exports, cross-channel routes | limited storage, route exposure, rail dependence | port handling, ferry and cargo access, rail and road distribution |
| Limerick and Shannon Estuary | western distribution, river and port access, industry, air potential | weak hinterland links, limited handling, fuel scarcity | Shannon depots, port works, airfield, regional power, rail priority |
| Midlands peat belt | domestic fuel, employment, strategic depth | drainage, machinery, seasonal labour, transport | mechanised turf, briquettes, bog rail, worker housing, postwar Bord na Móna |
| Shannon electricity network | national generation and transmission | uneven distribution, maintenance, demand limits | grid reinforcement, industrial feeders, postwar rural programme |
| western seaboard | fishing, weather, coast watching, small ports, migration | isolation, weak roads, low port capacity, severe weather | weather stations, local harbours, roads, radio, rescue, regional industry |
| north-west and Donegal | Lough Swilly defence, coast watching, border trade, fisheries | border complexity, weak access, British strategic interest | coastal battery, roads, air warning, cross-border supply, local ports |
| south-east agricultural belt | grain, livestock, ports, rail distribution | tillage conflict, fertiliser, price exposure | storage, milling, cooperative machinery, guaranteed transport |
| western and midland smallholder belt | livestock, turf, small farms, rural organisation | low capital, poor roads, tillage resistance, seasonal work | credit, drainage, cooperatives, local electricity, rural roads |

Northern regions enter the southern provision network only through a lawful agreement, war, occupation, or transition authority. Belfast, Belfast Lough, Derry and Lough Foyle, Larne, the linen belt, aircraft sites, and border rail corridors retain separate management, labour, contract, fuel, security, and finance requirements.

# Economic opening branch

## Shared opening sequence

The economy branch begins before route commitment. Its first lane establishes the information and institutions required for later choices.

| Focus group, working label | Class | Role | Unlock |
| --- | --- | --- | --- |
| `Count the National Stores` | H | survey stocks, imports, storage, rail, fuel, and industrial bottlenecks | National Provision display and first shortage missions |
| `Reconcile the County Returns` | H | improve agricultural, transport, and local-government reporting | county delivery records, lower project uncertainty |
| `A Programme of Essential Works` | P | choose first national priority | one of food, fuel, transport, maritime, or industry priority packages |
| `The Price of Sovereignty` | P | connect the 1938 settlement to supply and defence costs | Treaty Port, trade, and provision interaction |
| `A Board for National Provision` | P | create or designate a cross-department coordinating body | monthly provision review and project queue |

The coordinating body is route-neutral at creation. Its later name, composition, and authority depend on government.

- de Valera uses ministerial coordination and emergency cabinet review.
- Lemass strengthens a technical development board.
- Fine Gael uses treasury, law, and departmental responsibility.
- Labour adds unions, municipalities, and cooperatives.
- Clann na Talmhan demands county and farmer representation.
- vocational routes add sector councils.
- Congress uses programme boards and committees.
- IRA governments divide civil supply and military requisition authority.
- O'Duffy and Ailtirí centralise control through corporate or party bodies.
- High Kingship adds a public exchequer and household obligations.
- Five Provinces uses federal equalisation and regional budgets.
- Otherworld routes add site obligations while preserving ordinary human supply administration unless the route reaches dominion.

The shared opening never forces one route. It identifies the constraint and lets political outcomes change the means of delivery.

# Agrarian recovery and protected economy

## Agrarian recovery route identity

The agrarian and protectionist family builds food security, rural income, domestic processing, and bargaining power. It is the normal material foundation for de Valera, Clann na Talmhan, farmer independents, and several coalition or federal governments.

It is compatible with later industrial development. It becomes mutually exclusive only when a government commits to uncompensated collectivisation, estate command, unrestricted foreign dependence, or a route that abolishes private or cooperative farm authority.

## Agrarian recovery focus groups

### `Settle the Agricultural Account` working group

- revise the 1938 trade settlement into predictable cattle, dairy, grain, and input channels
- create export and import schedules tied to British Leverage
- compensate or restructure debts created by the Economic War
- choose whether the government prioritises farm income, cheap urban food, or foreign exchange

Tradeoff:

- farm-price support raises Rural Organisation and can lower urban purchasing power
- cheap-food policy supports urban consent and can weaken farm investment
- export priority brings foreign exchange and can reduce domestic reserves during a poor harvest

### `County Agricultural Programmes` working group

- county soil and crop surveys
- seed and fertiliser allocation
- cooperative machinery pools
- storage and milling
- veterinary and livestock protection
- drainage and land improvement
- rural credit and debt arbitration

Delivery uses county missions. The same policy can succeed in Wexford and fail in a wet western district. Part 5 defines county targets and timers.

### `Protected Food Industries` working group

- sugar processing
- milling and flour extraction
- dairy processing
- textiles and wool
- fertiliser substitution and recovery
- packaging, storage, and cold-chain experiments

Rewards change industrial delivery and Food Security together. Factories require power, transport, inputs, and local labour. A processing plant with no rail or storage creates waste and debt rather than full capacity.

### `The Rural Services Bargain` working group

- roads, clinics, schools, agricultural instruction, housing, local electricity preparation, and communications
- Church, local government, cooperative, Labour, and farmer influence depends on route
- serious cultural routes can add Irish-language service capacity without changing the economic purpose

The bargain is expensive and raises long-term Social Consent. Delaying it can produce higher short-term output and stronger agrarian opposition.

## Agrarian failure states

| Failure | Trigger direction | Consequence | Recovery |
| --- | --- | --- | --- |
| quota revolt | coercive tillage, low prices, weak machinery, high Rural Organisation opposition | food targets miss, inspections resisted, National Settlement pressure | price revision, county compact, targeted enforcement, cooperative equipment |
| livestock collapse | excessive grain conversion, feed shortage, transport loss | export and domestic protein decline | revised crop balance, feed imports, livestock protection |
| merchant capture | storage, milling, or export contracts concentrated without review | high prices, black market, patronage | cooperative marketing, competition inquiry, public board |
| protected stagnation | factories survive behind tariffs without skills or standards | industrial delivery ceiling and fiscal burden | technical standards, merger, export test, or closure |
| regional abandonment | projects concentrate in east and south | low western consent, migration, Clann or radical growth | regional fund, roads, peat, local industry, federal equalisation |

# Lemass developmental state

## Lemass developmental route identity

The Lemass route converts protected development and wartime supply experience into a technical state capable of planned industrial growth. The early route remains grounded in the 1930s and 1940s. It does not copy the policies of the late 1950s without institutional development and world conditions.

The route's central value remains Developmental Standing from Part 2. Part 4 adds material proof. A succession can remain politically valid and still fail as a developmental government if projects are late, indebted, import-dependent, or regionally narrow.

## Developmental pillars

| Pillar | Material purpose | Main projects | Main risk |
| --- | --- | --- | --- |
| technical administration | improve project selection and delivery | standards office, statistics, industrial research, procurement, engineering cadre | technocratic exclusion and cabinet resistance |
| power and fuel | expand reliable energy | grid reinforcement, peat mechanisation, storage, industrial feeders | imported machinery and regional concentration |
| strategic industry | build useful domestic capacity | machine repair, construction materials, chemicals, textiles, food processing | protected inefficiency and foreign input dependence |
| transport integration | connect industry to ports and markets | rail workshops, depots, priority freight, roads, port handling | coal and petrol scarcity, debt |
| labour and training | supply skills and industrial peace | apprenticeships, technical colleges, wage boards, housing | strikes, low pay, union exclusion |
| commercial transition | test whether protected firms can survive | export standards, procurement discipline, selective market opening | unemployment, dependency, political backlash |

## Non-linear developmental choices

The route has three strategic forks.

### Capital source

- domestic savings and gradual projects
- British contracts and trade access
- American credit and technical access
- balanced foreign sourcing
- route-specific state requisition or corporate finance

Each source changes leverage and project speed. Balanced sourcing is slower to negotiate and reduces client risk.

### Regional pattern

- Dublin and eastern industrial concentration
- Cork and southern maritime industry
- Shannon and Limerick development corridor
- Midlands fuel and materials belt
- distributed regional programme

Concentration completes faster. Distributed development raises transport and administrative costs while reducing regional grievance.

### Labour settlement

- managerial authority with minimum standards
- negotiated wage and productivity councils
- worker participation and cooperative supply
- compulsory industrial discipline

The first can deliver quickly and provoke strikes. The second favours Labour or plural Congress cooperation. The third changes ownership and committee power. The fourth belongs to authoritarian or vanguard variants and carries coercion and reporting distortion.

## Developmental conclusions

| Conclusion | Required material state | Identity |
| --- | --- | --- |
| Developmental Republic | Provision at least 60, a completed industrial delivery portfolio and reliable power, transport, skills, and inputs, Transport Serviceability at least `50`, leverage safeguards intact | technical sovereign republic with mixed protected industry |
| Developmental Social Compact | above plus strong Labour Organisation and negotiated labour settlement | industrial republic with welfare, unions, and regional delivery |
| Atlantic Development State | high shipping and American or balanced access, dependency below client pressure | trade-oriented small state with protected strategic sectors |
| Imported Development | high throughput built under leverage above 70 or weak domestic skills | fast growth with foreign contract and sovereignty pressure |
| Plan Without Delivery | high Developmental Standing but Provision below 45 or repeated failed projects | succession remains lawful, government loses material authority |

# Fine Gael fiscal and institutional economy

## Fine Gael economic route identity

Fine Gael's material route stresses solvency, law, administrative responsibility, trade, property security, and professional management. It cannot be a generic austerity bonus path. The government must decide who bears the cost of defence, rural recovery, and industrial modernisation.

## Fine Gael fiscal focus groups

### `Audit the Emergency State` working group

- review supply boards, state companies, contracts, rationing, and departmental powers
- expose or regularise off-budget liabilities
- preserve useful technical bodies under statutory authority
- close or merge captured boards

### `Credit and Confidence` working group

- stabilise public borrowing
- protect savings and farm credit
- negotiate British and American finance with safeguards
- create transparent capital budgets
- decide whether balanced budgets can be relaxed for defence or reconstruction

### `Trade Under Law` working group

- predictable tariffs and licensing
- commercial courts and contract enforcement
- export quality standards
- port and customs reform
- anti-monopoly review

### `Public Works With Accounts` working group

- regional road, rail, port, housing, and utility projects
- parliamentary appropriations and audit
- local-government co-finance
- project cancellation or redesign after failure

## Leadership variants

- Cosgrave prefers gradual solvency, institutional continuity, farm and commercial confidence.
- Mulcahy accepts higher defence expenditure when professional command and civilian audit are protected.
- Costello uses legal settlements, coalition bargains, and statutory boards.
- Dillon can redirect finance toward Allied interoperability and wartime supply after satisfying the intervention mandate.

## Fine Gael failures

- fiscal paralysis when every project is delayed for certainty
- creditor dependency under British or American leverage
- coalition collapse over taxes, rationing, and public works
- professional boards captured by commercial monopolies
- defence modernisation without social consent

# Labour and social economy

## Labour social-economy route identity

Norton's Labour route uses parliamentary authority, unions, municipalities, cooperatives, welfare services, and negotiated neutrality. It begins with reform, not revolutionary command. Congress transition remains separate and requires the Part 3 bridge.

## Labour social-economy focus groups

### `The Cost of Living Compact` working group

- wages, prices, rationing, rent, food distribution, and family allowances
- union, employer, cooperative, Church-service, and municipal participation
- indexed review during major shortages

### `Public Work and Full Employment` working group

- housing
- roads and sanitation
- schools and clinics
- peat and electricity preparation
- rail and port maintenance
- demobilisation employment

### `Cooperative Supply` working group

- consumer cooperatives
- agricultural marketing
- machinery pools
- worker and municipal distribution
- fraud and governance rules

### `Workers in Strategic Industry` working group

- apprenticeships
- safety
- bargaining
- productivity agreements
- worker representation in state enterprises
- emergency strike and arbitration rules

## Labour route forks

- parliamentary social compact with mixed ownership
- municipal and cooperative decentralisation
- state-enterprise development with union boards
- wartime national labour agreement
- Congress bridge after parliamentary breakdown

The 1944 Labour and National Labour split modifies every branch. National Labour can defend anti-communist union autonomy, coalition bargaining, and service reform. It can resist Congress, vanguard control, compulsory producer councils, or Church capture. Reconciliation requires affiliate and union procedures.

## Labour failures

- wage-price spiral under low provision
- union fragmentation and unauthorised strikes
- welfare promises without revenue or supply
- municipal inequality
- state-company patronage
- emergency arbitration becoming permanent coercion

# Clann na Talmhan and regional agrarian economy

## Clann na Talmhan economic route identity

Clann na Talmhan's material route begins only after its dated formation. It represents smallholder, western, regional, and anti-central grievance rather than a generic farmer party. Agrarian Cohesion determines whether regional and class differences can support a national programme.

## Clann na Talmhan programme families

- county credit and debt relief
- drainage, land improvement, and cooperative machinery
- rural roads and market access
- local processing and storage
- peat and regional employment
- housing and electrification preparation
- equalisation grants
- protection against urban and large-farmer capture

Michael Donnellan, Patrick Cogan, Joseph Blowick, farmer independents, and regional organisers have different priorities. Formal Clann seats and temporary farmer support blocs remain separate.

## Agrarian conclusion forms

- regional smallholder republic within constitutional government
- agrarian coalition partner with named programme delivery
- federal equalisation partner in Five Provinces or constitutional federation
- rural corporatist capture under estate government
- fragmented regional protest after Agrarian Cohesion collapses

# Constitutional vocational and producer economy

## Constitutional vocational economic identity

Constitutional vocationalism creates advisory and bargaining institutions under elections, courts, labour freedom, and minority safeguards. Part 4 tests whether councils can coordinate production without replacing parliament or becoming a route to employer, clerical, party, or military capture.

## Council architecture

| Council | Legitimate role | Capture risk | Material responsibilities |
| --- | --- | --- | --- |
| agriculture and food | prices, quotas, inputs, storage, farm labour | large farmer, merchant, or clerical capture | Food Security and county delivery |
| industry and construction | standards, contracts, materials, apprenticeships | employer cartel or party direction | industrial delivery and public works |
| labour and welfare | wages, safety, services, arbitration | union monopoly, clerical veto, or state coercion | Social Consent and labour continuity |
| transport and shipping | freight priority, crews, repairs, ports | company cartel, military capture, foreign access | Transport and Maritime Access |
| energy and peat | peat, coal, electricity, storage | regional patronage or central monopoly | Energy Continuity |

Council advice can improve information and compliance. Executive decree without Dáil review moves the route toward the Part 3 producer state, estate state, clerical guardianship, or council-government failure.

## Constitutional vocational conclusions

- Vocational Republic under parliamentary law
- Emergency Producer Commission with a dated return to elections
- Employer-Captured Council State
- Clerical Veto Economy
- Council Government Without a Dáil

The last three are failures or Part 3 transformations with full material consequences.

# Revolutionary and authoritarian material economies

The political transformations from Part 3 receive their own methods for allocating labour, land, credit, imports, and industrial output. They use the same four Provision components and the same regional project map. A route can change who controls delivery, which costs are accepted, how information is reported, and which foreign contracts are available. It cannot bypass shortages.

# IRA civil republican economy

Classification: `P`

## IRA civil material authority

The civil republican variant places an elected or convention-backed civil authority above the Army Council. Local commands retain influence over security and mobilisation, while civilian departments control taxation, procurement, welfare, courts, and ordinary production.

This route transforms wartime republican networks into public institutions through five connected programmes.

1. county reconstruction boards combine local republican organisers, elected representatives, technical staff, cooperatives, and recognised unions
2. a public procurement office converts clandestine supply channels into audited contracts
3. an armed integration board inventories weapons, vehicles, depots, workshops, and command obligations
4. a republican land and credit settlement handles debt, untenanted land, cooperative machinery, and compensation
5. a recognition and trade office separates lawful diplomacy from private military contact

## Core tradeoff

Local networks deliver quickly where Republican Network Strength and Public Republican Legitimacy are high. They also create uneven authority. Counties with strong local commands can withhold deliveries, protect favoured firms, resist taxation, or preserve private arms stores. Centralisation improves Transport Serviceability and industrial delivery while lowering Local Command Compliance if the process ignores civil guarantees.

## Non-linear route forks

### Public boards or cooperative districts

- public boards favour Administrative Reach, standard contracts, and national planning
- cooperative districts favour Social Consent, local knowledge, and agrarian participation
- a mixed settlement allows regional variation and costs more administrative capacity

### Restitution or accelerated redistribution

- lawful restitution and compensated transfer preserve credit and minority confidence
- accelerated transfer raises rural support and risks capital flight, legal disputes, and retaliatory withholding
- confiscatory command belongs to the IRA command variant and closes the civil route unless reversed through a constitutional recovery

### Foreign procurement

- balanced public contracts reduce dependency and move slowly
- Allied procurement improves equipment compatibility and raises British or American obligations
- German contacts can be disclosed, severed, prosecuted, or converted into a dangerous clandestine channel
- diaspora finance requires transparent civilian control or it strengthens rival armed networks

## IRA civil material conclusions

| Conclusion | Requirements | Outcome |
| --- | --- | --- |
| Civil Republican Reconstruction | Provision at least 55, Administrative Reach at least organised, Army Council Cohesion controlled, Local Command Compliance at least organised, audited procurement | lawful republican state with regional boards and an integrated defence economy |
| Cooperative Republic | strong Labour Organisation, Rural Organisation, county delivery, union and agrarian compact | decentralised social and agrarian economy with slower strategic concentration |
| Armed Dual Economy | Local Command Compliance below 40, private depots, weak tax collection, civil authority still present | uneven provision, repeated requisition disputes, weak national readiness |
| Recognition Without Capacity | foreign recognition or sponsorship with Provision below 40 | diplomatic progress alongside continued material dependence |
| Return to Constitutional Administration | lawful election or convention, disarmament schedule, audited departments | bridge back to a constitutional government without erasing republican history |

# IRA command economy

Classification: `P`

## IRA command material authority

The Army Council and GHQ direct production, transport, food allocation, and foreign procurement through command districts. This can concentrate scarce resources for war faster than a divided civil government. It damages civilian reporting, local trust, trade stability, and the ability to distinguish military need from factional privilege.

## Command districts

Each command district has four records.

- delivery compliance
- civilian hardship
- military priority
- reporting reliability

A district can meet a quota by voluntary delivery, negotiated contract, requisition, smuggling, or foreign supply. The method changes Public Republican Legitimacy, Security Exposure, Social Consent, Food Security, and foreign leverage.

## Command allocation choices

### Arms before consumption

This raises equipment repair and military stockpiles while lowering Food Security, civilian fuel, and Social Consent. It can be justified during direct invasion or an active Northern war. Repeated use outside those conditions creates a warlord economy failure.

### Strategic county requisitions

Requisition targets named depots, mills, vehicles, livestock, fuel stores, and workshops. The action must record the command district, duration, compensation policy, and civilian replacement plan. Failure creates sabotage, desertion, black markets, and local-command defection.

### Foreign military pipeline

A German, Allied, or diaspora pipeline can supply equipment and specialist knowledge. It also creates sponsor conditions, intelligence exposure, incompatible equipment, political demands, and a route-specific client-state risk.

### Command industry

GHQ can convert workshops and protected firms for military use. Industrial output rises only when power, tools, skilled labour, and transport are available. Forced conversion without inputs creates idle plants and false readiness reports.

## Command economy failures

- requisition famine in low-compliance regions
- rival commands retaining supplies
- foreign sponsor control over procurement and strategy
- civilian departments stripped of staff and transport
- arms production that cannot be supplied with energy or imported components
- inflated output records hiding unusable equipment
- local commanders trading exemptions for personal loyalty

## IRA command material conclusions

| Conclusion | Requirements | Outcome |
| --- | --- | --- |
| Integrated Republican War State | Army Council Cohesion at least decisive, Local Command Compliance at least decisive, Provision at least 50, Readiness at least 60, sponsor dependence below client pressure | militarised republic capable of sustained defence with heavy civil cost |
| GHQ Directorate | strong command and weak civil authority | central command economy with recurring legitimacy and succession crises |
| German-Supplied Client | German Leverage or Sponsor Dependence above 84, protected pipeline, weak civil safeguards | foreign-dependent command state with intelligence and strategic subordination |
| Fragmented Commands | Local Command Compliance below 20 or Army Council Cohesion below 20 | rival regional economies, collapsing national provision, civil conflict risk |
| Civil Restoration | negotiated disarmament, public accounts, lawful civil authority, command obligations retired | transition to the civil republican economy |

# Republican Congress plural economy

Classification: `P`

## Congress plural material authority

The plural Congress route builds a common programme among unions, local committees, agrarian organisations, municipal bodies, public enterprises, and a subordinated armed wing. It gains local participation and social consent while facing slow coordination, contested ownership, and sectoral vetoes.

## Economic institutions

- a congress of production and supply sets broad goals
- elected industrial boards manage strategic enterprises
- municipal and county committees deliver housing, food, sanitation, and local transport
- union agreements regulate wages, safety, apprenticeship, and emergency work
- cooperative and public credit supports farms, workshops, and consumer distribution
- a civilian defence council limits the armed wing's claim on output

## Programme choices

### Social ownership settlement

- national ownership for power, rail, ports, shipping, fuel, and selected heavy industry
- municipal ownership for housing, water, local transport, and services
- cooperative ownership for agriculture, retail distribution, fisheries, and small manufacturing
- regulated private operation where capacity cannot be replaced quickly

The player must specify compensation, management, worker representation, technical continuity, and foreign contract treatment. A declaration alone does not raise throughput.

### Union production compact

The compact links wages, prices, food allocation, workplace safety, training, and emergency production. High Union Commitment improves compliance. A compact imposed through the vanguard lowers reporting reliability and raises strike or sabotage risk.

### Agrarian common programme

Peadar O'Donnell's agrarian influence can connect debt relief, land improvement, cooperative machinery, and local processing to the national plan. Urban committees can divert capital toward housing and industry. A failed compromise fractures Coalition Cohesion.

## Plural route failures

- committee duplication across the same factory or county
- union rivalry blocking national standards
- armed wing pressure on civilian allocation
- capital flight and foreign contract withdrawal without replacement
- urban priority causing rural delivery collapse
- democratic procedures unable to respond during immediate invasion

## Congress plural material conclusions

| Conclusion | Requirements | Outcome |
| --- | --- | --- |
| Plural Workers' Commonwealth | Provision at least 60, Coalition Cohesion and Union Commitment at least decisive, Armed Wing Subordination at least organised, functioning public boards | democratic social economy with strong services and negotiated mobilisation |
| Cooperative Social Republic | high rural and municipal participation, moderate industrial concentration | resilient local economy with slower heavy military growth |
| Emergency Common Programme | active war or invasion, dated emergency authority, review mechanism | temporary central coordination that can return to plural rule |
| Committee Paralysis | Coalition Cohesion below 40 and repeated delivery failures | low transport coordination, project delay, political fragmentation |
| Armed Committee Capture | Armed Wing Subordination below 20 | transition toward the vanguard or a renewed armed dual authority |

# Republican Congress vanguard economy

Classification: `P`

## Congress vanguard material authority

The vanguard variant replaces negotiated common programming with a central directorate. It can direct labour, imports, land, production, and transport quickly. It risks purge-driven skill loss, false reporting, local resistance, union revolt, and dependency on an external socialist sponsor if one exists.

## Directorate instruments

- compulsory delivery schedules
- central labour assignment
- nationalised strategic firms
- production tribunals
- controlled wages and prices
- ration hierarchy tied to political and military priority
- centralised foreign trade monopoly

## Capacity rule

Vanguard direction changes the speed and coercion of allocation. It never creates raw inputs. Every compulsory project still needs power, machinery, transport, labour, and maintenance. A high Committee Mandate created through coercion does not substitute for Administrative Reach.

## Failure branches

- skilled workers removed through ideological screening
- union opposition and underground organisation
- agriculture withholding or livestock slaughter
- local committees falsifying delivery records
- military demands overriding civilian survival
- external sponsor demanding political or military control
- directorate succession producing rival security organs

## Congress vanguard material conclusions

- disciplined command-socialist state with high provision and heavy coercion
- foreign-backed revolutionary client
- military-directorate merger
- famine and strike crisis
- plural restoration through a congress and union settlement
- constitutional social republic after lawful elections

# O'Duffy and National Corporate Party economy

Classification: `P`

## O'Duffy material authority

O'Duffy's route reorganises agriculture, industry, labour, professions, veterans, and local government into compulsory estates under executive direction. The route can coordinate contracts and suppress disputes. It also creates cartel capture, patronage, labour coercion, Church conflict, foreign sponsorship, and a persistent gap between ceremonial representation and real control.

## Estate economy structure

| Estate | Public claim | Actual material role | Main capture risk |
| --- | --- | --- | --- |
| agricultural estate | national food and rural order | quotas, prices, credit, labour, land policy | large farmer and merchant dominance |
| industrial estate | national production | licensing, contracts, imports, wages, technical training | employer cartel and foreign investor control |
| labour estate | class peace | compulsory representation, arbitration, labour assignment | party and security domination |
| professional estate | expertise | engineering, medicine, law, finance, administration | elite insulation and patronage |
| veterans' estate | service and defence | mobilisation, procurement, paramilitary employment | personal guard and military rivalry |
| local and charitable estate | social order | welfare, housing, education, relief | clerical or local patron capture |

## Route choices

### Estate arbitration or executive decree

Arbitration improves compliance and slows decisions. Executive decree accelerates mobilisation and shifts the system toward personal dictatorship.

### Domestic corporate capital or foreign patronage

Domestic capital is limited and politically constrained. Italian, German, British, or American contracts create distinct leverage and ideological consequences. The route cannot assume Axis aid remains available or useful after Axis defeat.

### Army partnership or party militia

Army partnership requires Army Acceptance and professional command safeguards. Party militia directs contracts toward loyalists and increases Paramilitary Reliability while reducing equipment standardisation and officer trust.

## Corporate failures

- compulsory estates becoming monopolies
- labour freedom collapsing into forced assignment
- small farmers excluded by large producers
- military procurement captured by veteran networks
- foreign sponsor contracts creating client status
- Church institutions resisting party control or gaining a veto
- O'Duffy succession leaving no accepted material authority

## O'Duffy material conclusions

| Conclusion | Requirements | Outcome |
| --- | --- | --- |
| Corporate State Economy | high Corporate Bloc Cohesion, Provision at least 55, Army Acceptance organised, sponsor dependence below 70 | authoritarian estate economy with controlled labour and concentrated contracts |
| Personal Patronage State | O'Duffy Organisation dominant, institutions weak | unstable allocation through personal networks |
| Military Corporate Directorate | Army Acceptance dominant and O'Duffy weakened | army-led production state with reduced party autonomy |
| Foreign Corporate Client | Sponsor Dependence above 84 | external contracts and strategic subordination |
| Estate Collapse | Corporate Bloc Cohesion below 20 or succession failure | sectoral noncompliance, black markets, labour conflict, constitutional recovery opening |

# Clerical guardianship and producer economy

Classification: `P`

## Clerical material authority

The clerical guardianship variant expands Church-linked education, health, welfare, charity, rural service, and vocational mediation into statecraft. The route gains service reach and moral authority where public administration is thin. It risks clerical veto, minority insecurity, labour exclusion, fragmented accounting, and reliance on institutions that were not designed to run national industry or defence.

## Service network functions

- relief distribution and nutrition
- hospitals, clinics, nursing, and civil defence
- schools, technical education, and apprenticeships
- housing and parish works
- family support and refugee reception
- vocational mediation among employers, labour, farms, and services

## Institutional boundary

Church Institutional Influence can improve delivery through trusted networks. Vatican Leverage remains foreign and separate. Bishops, orders, hospitals, schools, lay bodies, and charities do not act as one command. National projects require contracts, budgets, audits, minority safeguards, and labour rules.

## Route forks

- statutory partnership under elected government
- emergency guardianship commission with a fixed expiry
- producer councils with clerical mediation
- clerical veto over labour, education, information, and social policy
- captured service state controlled by a narrow hierarchy

## Material failures

- minority exclusion from services and public employment
- duplication between public departments and institutions
- medical or educational staff diverted without replacement
- charities used as political patronage
- labour arbitration suppressing free organisation
- Vatican diplomacy treated as domestic command
- emergency guardianship refusing to expire

## Clerical material conclusions

- Social Partnership Republic
- Emergency Guardianship With Return Date
- Vocational Welfare State
- Clerical Veto Economy
- Service Network Collapse
- Constitutional Recovery With Protected Institutional Autonomy

# Ailtirí autarkic economy

Classification: `P`

## Ailtirí material authority

Ailtirí directs land, labour, language institutions, youth, migration, industry, and trade through a total national programme. Its public claim is Gaelic self-sufficiency. Its operating methods include coercive assignment, political screening, forced cultural conformity, exclusion, party patronage, emigration controls, and ideological procurement.

Autarky does not remove dependence. Ireland still needs machinery, fuel, chemicals, specialist equipment, shipping, and technical knowledge. The route converts scarcity into a disciplinary project and can hide failure through propaganda and repression.

## Ailtirí material programme families

- compulsory Gaelic labour service
- youth settlement and construction brigades
- directed peat, power, road, and housing projects
- agricultural quotas and land settlement
- party-controlled strategic firms
- emigration restriction and skilled-personnel retention
- ideological trade with Axis or sympathetic partners
- seizure or exclusion of targeted property and employment

Antisemitism and social exclusion are explicit parts of the movement's politics. They reduce Minority Confidence, remove or endanger skilled citizens, damage foreign relations, and increase coercive enforcement. The route cannot receive a neutral efficiency reward for persecution.

## Wartime and post-Axis crisis

The route can gain short-term German contact or propaganda value. Axis defeat removes the strategic foundation, cuts supply channels, and forces a choice among ideological isolation, tactical diplomatic retreat, internal purge, succession struggle, or regime collapse.

## Ailtirí material conclusions

| Conclusion | Requirements | Outcome |
| --- | --- | --- |
| Coercive Gaelic Autarky | high State Capture and Cultural Capture, Provision at least 50, closed labour and trade regime | authoritarian scarcity economy with heavy repression and weak innovation |
| Party Development State | technical cadres retained, selective foreign trade, party control | stronger throughput with persistent exclusion and surveillance |
| Axis Client Project | German Leverage or sponsor dependence above 84 | externally directed procurement and war policy |
| Post-Axis Isolation | sponsor collapse with regime surviving | severe maritime and technical shortage, diplomatic exclusion |
| Administrative Breakdown | State Capture high and Administrative Reach below 40 | orders without delivery, local evasion, black markets, succession crisis |

# High Kingship material orders

## Constitutional crown economy

Classification: `P`

The constitutional crown operates through a public exchequer, elected government, courts, provincial consultation, and a bounded civil list. Royal Legitimacy can support long projects and symbolic national subscriptions. It cannot replace taxation, borrowing, technical management, or parliamentary appropriation.

### Crown institutions

- crown development commission under statute
- public civil list and household audit
- royal charter for shipping, culture, or regional development
- provincial works conferences
- succession reserve and continuity fund
- public ceremonial employment with strict cost controls

### Risks

- household patronage in contracts and appointments
- an expanding civil list during shortage
- provincial resentment at royal concentration
- foreign recognition tied to dynastic or strategic obligations
- crown guard costs competing with regular defence

### Constitutional High Kingship outcomes

- Crown-in-Council Development State
- Parliamentary High Kingdom With Public Accounts
- Provincial Royal Compact
- Captured Household Economy
- Elective Restoration Failure and Republican Reversion

## Sacral crown obligation economy

Classification: `A`

The hidden sacral variant adds the Obligation Burden to ordinary provision. Ceremonies, sites, seasonal duties, hospitality, legal assemblies, regional journeys, and compact obligations consume labour, transport, food, security, and political time.

A high Royal Legitimacy value can improve voluntary contributions and long-term project consent. Forced obligation raises Household Reach and lowers Social Consent, Minority Confidence, and reporting quality. Sacral claims do not produce factories, weapons, harvests, or foreign recognition.

The material route chooses among:

- bounded public obligations under human law
- regional and seasonal contributions
- hereditary household extraction
- military royal command
- compact obligations shared with an Otherworld route

Failure produces a Captive Throne, household warlordism, provincial refusal, or human constitutional restoration.

# Five Provinces material federation

## Federal equalisation economy

Classification: `P`

The plausible federal variant assigns revenue, works, services, and development responsibilities among the common government and valid provincial authorities. Each province has a budget, contribution, delivery record, and veto exposure.

## Federal fiscal model

| Level | Responsibilities | Revenue | Main failure |
| --- | --- | --- | --- |
| common authority | defence, foreign trade, currency, national rail, major ports, national standards | customs, common tax, provincial contributions | underfunded centre or central overreach |
| provincial authority | roads, housing, local industry, education, health, agriculture, culture | assigned taxes, grants, local borrowing | regional inequality or patronage |
| county and municipal bodies | delivery, local works, relief, policing support | rates, grants, service fees | weak capacity and unequal administration |

The Middle Balance or Mide settlement controls equalisation, shared institutions, and the common capital. A weak centre cannot fund national defence. A dominant centre converts federalism into unitary rule. A provincial veto can protect rights and can block emergency supply.

## Provincial economy variants

- balanced federal equalisation
- competitive provincial development
- provincial sovereignty with a minimal common market
- crown and provinces with a royal arbitration role
- four provinces and an empty Ulster chair
- full five-province settlement after a valid Northern agreement

## Federal conclusions

- Federal Republic of the Five Provinces
- Irish Confederation with a limited centre
- Crown and Five Provinces
- Rival Irelands after fiscal and guard breakdown
- Pentarchy under the hidden route after full `A` gates

# Otherworld material compact

Classification: `A`

## Human state remains primary

A verified compact introduces sites, passages, witnesses, obligations, exceptional actors, and unusual hazards. Human agriculture, power, shipping, transport, industry, taxation, and public administration remain necessary.

## Obligation Ledger interaction

Each compact obligation has:

- human authority responsible for delivery
- site or passage affected
- material cost
- public-knowledge level
- Compact Trust effect
- Veil Stability effect
- failure consequence
- expiry or renewal rule

Possible costs include protected land, seasonal access, transport priority, food, ceremonial materials, security, legal recognition, medical support, archive work, or restrictions on development. Obligations cannot use undefined magical resources.

## Compact economy routes

- stewardship republic protects sites while pursuing ordinary development
- compact of two Irelands creates joint courts and bounded exchange
- sealed state closes passages and funds containment
- dominion economy exploits passages, labour, or territory and creates resistance
- five courts distribute obligations through provincial authorities
- crown compact places the monarch under public law and the Obligation Ledger

## Exceptional benefit rule

An impossible event can create a route-specific capability, such as reliable passage under strict conditions, unusual reconnaissance, or exceptional site protection. Every capability has a maintenance cost, failure state, geographical limit, public risk, and countermeasure. It does not grant universal production or combat bonuses.

## Compact failures

- obligations exceeding National Provision
- public panic after uncontrolled knowledge
- foreign capture of a site or witness network
- human authorities surrendering jurisdiction
- false evidence corrupting the route
- passage exploitation causing resistance and Veil collapse
- Compact Trust collapse producing closure, conflict, or dominion

# Emergency economy overlays

Political routes share several overlays that can appear during war, invasion, blockade, major bombing, Northern conflict, or severe shortage.

## Legal emergency allocation

Classification: `H` and `P`

- cabinet or lawful route authority identifies critical goods
- the Dáil or valid successor approves powers and review
- boards allocate imports, fuel, shipping, labour, and transport
- rationing and price controls protect minimum consumption
- inspectors and courts handle evasion
- sunset dates and demobilisation rules are recorded

This overlay favours constitutional routes and any radical route that has created valid public law.

## Negotiated national production compact

Classification: `P`

- government, unions, farms, employers, cooperatives, services, and local authorities agree quotas and protections
- compliance depends on Social Consent and stakeholder organisation
- disputes use arbitration and public review
- successful delivery raises Provision and preserves institutional legitimacy

This overlay favours Labour, plural Congress, civil republican, and constitutional vocational routes.

## Command requisition

Classification: `P`

- armed or authoritarian authority seizes named resources and transport
- short-term military allocation rises
- civilian provision, local support, and reporting reliability fall unless compensation and replacement are supplied
- repeated use can transform the governing order into a command state

## Foreign supply dependency

Classification: `P`

- one sponsor supplies fuel, shipping, equipment, credit, or food above a defined share
- source-specific leverage and obligation rise
- domestic components can improve while sovereignty safeguards weaken
- interruption creates a sudden component loss

## War damage and recovery

Bombing, invasion, sabotage, mine damage, port seizure, rail disruption, and ship losses change regional delivery and national components. Repairs require construction capacity, labour, machinery, security, and access. A focus can authorise reconstruction. It cannot restore every damaged asset instantly.

# National Provision conclusion gates

| Capability | Provision floor | Component and delivery gates | Political requirement |
| --- | ---: | --- | --- |
| stable peacetime administration | `40` | no component below `20` | valid government and Administrative Reach at least organised |
| resilient Emergency economy | `50` | Food Security, Energy Continuity, and Transport Serviceability at least `35` | lawful emergency authority or route-valid coercive enforcement |
| sustained mobilisation | `55` | Food Security, Energy Continuity, and Transport Serviceability at least `40` | mobilisation authority and Readiness support |
| deep Allied cooperation | `50` | Maritime Access and Transport Serviceability at least `40` | sovereignty safeguards and valid foreign policy |
| formal belligerency | `55` preferred | Maritime Access, Energy Continuity, and Transport Serviceability at least `40` | route war gate and contribution plan |
| Northern transition administration | `50` | Transport Serviceability at least `40` and a delivered administrative portfolio | valid settlement and Integration Capacity |
| prolonged Northern war | `55` | Food Security at least `45`, Energy Continuity at least `40`, Transport Serviceability at least `45`, Maritime Access at least `35` | Readiness `60`, mobility `45`, command and occupation plan |
| Atlantic or Celtic defence order | `65` | Maritime Access and Transport Serviceability at least `50` | real partners and shared obligations |
| highest hidden-route ambition | `70` | no component below `50` | complete concealed-route gates and affordable obligations |

# National Readiness

## National Readiness purpose

`National Readiness` measures usable defence capacity. It asks whether the state can make decisions, train and command forces, equip them, mobilise replacements, move and supply them, detect danger, protect maritime approaches, and use intelligence without losing civil control.

The range is `0` to `100`. The opening value is exactly `15`, calculated as the arithmetic mean of seven components.

| Component | Opening value | Measures |
| --- | ---: | --- |
| Command and Training | `25` | lawful authority, staff work, officers, exercises, doctrine, signals, liaison, and continuity |
| Equipment Sufficiency | `8` | rifles, artillery, vehicles, signals, engineering tools, aircraft, ammunition, spares, and maintenance |
| Mobilisation Depth | `20` | regular strength, reserves, LSF, LDF, coastwatchers, recruitment, replacement, and medical fitness |
| Supply and Mobility | `12` | food, fuel, rail, roads, depots, trucks, medical support, repair, shipping, and replacement flow |
| Coastal and Air Warning | `5` | lookout coverage, air warning, recognition, weather, communications, plotting, and response |
| Maritime Protection | `5` | batteries, mines, harbour control, patrol, inspection, rescue, pilotage, and port denial |
| Intelligence Coordination | `30` | G2, Garda, coastwatch, censorship, foreign liaison, agent control, Northern intelligence, and protected plans |

```text
25 + 8 + 20 + 12 + 5 + 5 + 30 = 105
105 / 7 = National Readiness 15
```

## Readiness bands

| Range | State | Capability |
| --- | --- | --- |
| `0` to `14` | Nominal Sovereignty | forces and installations exist but cannot cover national tasks |
| `15` to `29` | Improvised Defence | limited mobilisation works under severe equipment and mobility limits |
| `30` to `44` | Limited Territorial Defence | selected regions can impose a credible invasion cost and support armed neutrality |
| `45` to `59` | Credible National Defence | several national sectors can be sustained under one command |
| `60` to `74` | Integrated Defence | army, warning, maritime protection, intelligence, supply, and mobilisation operate together |
| `75` to `89` | War-Capable State | home defence and a limited external or regional commitment can coexist |
| `90` to `100` | Exceptional Mobilisation | extraordinary late-game commitments become possible with continuing material and political costs |

## Readiness bottlenecks

- Equipment Sufficiency below `15` caps Readiness at `35`
- Supply and Mobility below `20` caps Readiness at `45`
- Command and Training below `25` blocks sustained offensive operations
- Intelligence Coordination below `25` exposes plans to penetration and disruption
- Coastal and Air Warning below `20` blocks a credible armed-neutrality conclusion
- Maritime Protection below `20` blocks a secure-port conclusion
- National Provision below `35` caps prolonged mobilisation gains

A direct invasion can produce temporary Overextension above a sustainable ceiling. Overextension consumes equipment, fuel, food, transport, officers, and Social Consent until the force returns to a supportable level.

## Readiness gates

| Capability | Readiness floor | Additional fixed gate |
| --- | ---: | --- |
| credible armed neutrality | `30` | Warning at least `20`, Maritime Protection at least `20`, Integrity at least `60` preferred |
| wartime Northern defence bargain | `35` | defined defence scope, Irish command, and British agreement |
| Dillon formal belligerency | `45` | every fixed Part 2 political gate, National Provision `50` with no component below `30`, Maritime Access `40`, Transport Serviceability `40`, Equipment Sufficiency `40`, Command and Training `40`, Supply and Mobility `40`, protected home-defence reserve, defined military contribution, and enforceable safeguards |
| normal constitutional voluntary war entry | `50` | Social Consent at least `65`, lawful supermajority, Provision at least `45`, Northern policy, contribution plan |
| independent offensive planning | `55` | Command at least `35`, Equipment at least `25`, Supply at least `30` |
| sustained Northern campaign | `60` | Supply and Mobility at least `45`, Provision at least `55`, valid cause, command, and occupation plan |
| expeditionary intervention | `65` | protected home-defence reserve, Maritime Access, transport, replacement, and foreign command settlement |
| regional defence league | `75` | real members, common threat, contribution rules, command safeguards, Provision at least `65` |
| impossible multi-front ambition | `85` | full concealed-route gates, high component floors, affordable obligations, aftermath plan |

## Readiness update rhythm

Readiness is reviewed monthly and after mobilisation changes, major equipment loss, port or airfield transfer, war entry, command crisis, or operational-plan failure. Components improve through delivered equipment, staffed installations, completed training, exercises, working communications, route and depot missions, intelligence fusion, and maintained stocks.

Rapid recruitment without equipment and command raises Mobilisation Depth without producing an effective force. Imported equipment without training, spares, compatible ammunition, and communications creates temporary capacity followed by failure.

# Shared defence architecture

## Defence branch crown

The defence support tree has seven interacting lanes.

1. civilian command and general staff
2. regular army reform
3. reserves, Local Security Force, and Local Defence Force
4. coastal defence and harbour command
5. Air Corps, air warning, and anti-air defence
6. Marine Service, shipping protection, and rescue
7. G2 intelligence, Garda Special Branch, counter-intelligence, censorship, and foreign liaison

These lanes normally coexist. A political route changes control, rights, foreign access, and mobilisation method. Mutual exclusion is reserved for incompatible command orders, such as civilian general staff against party military command, integrated national force against independent local commands, or public intelligence law against foreign-directed security.

# Civilian command and general staff

## Command settlement

Every route must define:

- supreme lawful authority
- ministerial or council control
- chief of staff and succession
- relationship between army, Garda, intelligence, militia, guards, and local commands
- emergency delegation
- foreign liaison limits
- review and demobilisation

The command settlement changes the National Settlement contributor map. A professional army under civilian authority supports constitutional or negotiated stages. A party guard, captive crown guard, independent armed wing, or provincial military veto pushes the transformed balance toward coercive authority or fragmentation.

## Staff reform groups

- mobilisation tables and replacement plans
- district and brigade command review
- officer education and staff exercises
- signals, maps, weather, and communications
- engineering, medical, transport, and supply staffs
- civil defence and continuity of government
- lessons from Spain, continental war, and British liaison without copying foreign command wholesale

## Command failures

- competing mobilisation orders
- political screening removing skilled officers
- Civil War memory blocking appointments
- foreign liaison bypassing Irish command
- secret plans unknown to civil authorities
- emergency command becoming permanent rule
- guards or local commands receiving independent strategic authority

# Regular army reform

## Personnel and structure

The regular force provides cadres, specialist services, training, and national command. It cannot cover every port, airfield, border crossing, depot, and coastal sector alone.

Route choices include:

- small professional cadre with strong reserves
- larger territorial army with modest equipment
- mobile defence around capital, ports, and transport nodes
- regional commands tied to local defence
- Allied-compatible expeditionary structure
- route-specific revolutionary, corporate, royal, federal, or party command

## Equipment priorities

The player chooses a sequence among:

- infantry rifles and ammunition
- support weapons and artillery
- signals and field telephones
- engineers and demolition equipment
- trucks, motorcycles, and staff transport
- anti-air weapons and searchlights
- aircraft and airfield support
- coastal artillery ammunition and fire control
- medical and repair equipment

No route can modernise all categories early. Foreign aid can accelerate one sequence and raises leverage, training needs, spare-part dependence, and access demands.

## Training cycle

A force becomes usable through recruitment, individual training, unit training, field exercise, mobilisation rehearsal, and operational-plan validation. Shortening the cycle raises Personnel while reducing Command and Training. Exercises consume fuel, ammunition, equipment life, transport, and civilian access.

# Reserves, Local Security Force, and Local Defence Force

Classification: `H` foundation with route-specific `P` changes

## Layered mobilisation

| Layer | Primary role | Main cost | Failure risk |
| --- | --- | --- | --- |
| regular army | national combat and specialist cadres | permanent manpower and budget | too small to cover national territory |
| first-line reserve | reinforce regular formations | training time and equipment storage | paper units and slow call-up |
| Local Security Force | local guarding and public support tasks | police and local coordination | politicisation and uneven reliability |
| Local Defence Force | territorial defence, observation, infrastructure, local response | rifles, training, officers, transport, Social Consent | militia fragmentation or false readiness |
| general mobilisation | national war expansion | economy, food, fuel, equipment, labour | provision collapse and command overload |

## LDF route design

The LDF can specialise by region.

- coastwatch and rescue support on the Atlantic and southern coasts
- harbour and infrastructure guarding around Cork, Dublin, Waterford, and Shannon
- border observation and refugee support in border counties
- airfield and communications protection in the east and midlands
- transport, medical, and fire response in urban areas
- local knowledge and language support in Gaeltacht and island districts

Political loyalty checks do not replace training or equipment. Heavy ideological screening lowers local participation and can remove valuable knowledge.

## Mobilisation tradeoffs

- volunteers preserve consent and fill slowly
- selective obligation improves numbers and creates exemptions disputes
- general conscription raises personnel and damages neutrality legitimacy unless invasion or formal war justifies it
- party or command recruitment raises loyal formations and fragments national standards
- provincial guards preserve local authority and can block common deployment
- royal guards protect institutions and can compete with the regular army

# Coastal defence and Treaty Port burden

Classification: `H` foundation

## Port defence package

The 1938 transfer gives Ireland sovereignty and responsibility. Each major port defence project requires:

- ownership and lawful command
- survey and inventory
- staffed batteries
- ammunition and fire control
- searchlights and observation
- communications
- harbour patrol and pilotage
- mines or demolition plans where used
- repair, fuel, medical, and supply support
- access and denial doctrine

A harbour can be sovereign and militarily unusable. It can be defended and commercially congested. It can accept Allied technical help while retaining Irish command. It can become a foreign base only through a public or route-valid access settlement with obligations and withdrawal rules.

## Harbour route families

- denial and demolition under strict neutrality
- defended neutral commerce
- controlled Allied access short of basing
- full Allied base after lawful belligerency
- Axis or German liaison harbour under an authoritarian route
- federal all-island harbour command after a Northern settlement
- royal or provincial command under bounded common law
- exceptional compact protection with an ordinary human garrison

## Coastal failure states

- batteries without ammunition
- foreign access overwhelming Irish command
- port denied to everyone and merchant supply collapsing
- sabotage or local-command capture
- bombardment or air attack disabling facilities
- duplicated command among army, Marine Service, port authority, and foreign liaison

# Air warning, Air Corps, and anti-air defence

## Air Defence Command network

The air-defence lane joins observation, reporting, filtering, fighter and anti-air response, weather, civil defence, and incident policy.

### Observation layers

- Coast Watching Service posts
- Garda and LDF local reports
- Air Corps patrols
- weather stations
- port and lighthouse reports
- foreign technical information under liaison agreements
- radar only after a valid project and technical source

### Response layers

- identification and plotting
- civil warning
- interception where aircraft exist
- anti-air defence around Dublin, ports, airfields, power, and industry
- forced landing or internment procedure
- rescue and medical response
- diplomatic protest and investigation

## Air Corps choices

- observation and liaison force
- limited interceptor force
- training and technical school
- maritime patrol role
- Allied interoperability
- route-specific party, federal, or royal air arm

Aircraft require pilots, mechanics, fuel, spares, airfields, communications, and weather. Imported aircraft without spare parts create a short-lived readiness increase and a maintenance crisis.

# Coast Watching Service

Classification: `H`

## Network architecture

The 83 historical lookout posts are grouped into six operational sectors for gameplay.

1. northwest and Donegal
2. Galway and western islands
3. southwest and Berehaven approaches
4. Cork and south coast
5. east coast and Dublin approaches
6. border loughs and Northern interface

Each sector tracks:

- post coverage
- observer training
- communications reliability
- aircraft and vessel recognition
- weather reporting
- rescue access
- security exposure

The player maintains the network through staff rotation, radios and telephones, maps, recognition material, transport, shelter, fuel, local cooperation, and intelligence protection.

## Coastwatch outputs

- Coastal and Air Warning
- neutral incident evidence
- rescue opportunities
- weather and navigation information
- smuggling and agent detection
- foreign liaison value
- hidden cultural support through local knowledge when serious Cultural Capacity is high

Cultural Capacity improves language, local knowledge, archives, and regional participation only when posts, communications, transport, and trained staff exist.

# Marine Service, shipping protection, and rescue

## Marine defence scope

Ireland cannot build a major fleet quickly. The maritime branch focuses on harbour patrol, examination, mines, rescue, coastal communication, merchant protection, small craft, maintenance, and liaison.

## Force development choices

- harbour and coastal patrol craft
- minesweeping and examination service
- rescue and salvage service
- merchant escort coordination short of formal convoying
- maritime patrol aircraft cooperation
- controlled foreign technical assistance
- wartime expansion after belligerency

## Neutral shipping protection

Neutral markings, route planning, weather, crew training, repair, radio procedure, cargo priority, rescue, and diplomatic protest reduce risk without granting immunity. Shipping losses reduce Maritime Access and can trigger replacement, charter, routing, or alignment choices.

## Maritime failures

- merchant ships used for military supply while neutrality remains publicly strict
- foreign naval protection creating hidden basing or command obligations
- crew shortage and refusal
- port repair bottlenecks
- mines and unexploded ordnance closing routes
- rescue obligations overwhelming small services

# Intelligence, counter-intelligence, and censorship

## Institutional division

| Institution | Core role | Political risk |
| --- | --- | --- |
| G2 | military intelligence, foreign agents, operational liaison | foreign penetration or military autonomy |
| Garda Special Branch | domestic security, IRA and subversion investigations | partisan policing, detention abuse, intelligence rivalry |
| ordinary Garda | local information, public order, enforcement | overload and local political pressure |
| Office of Censorship | wartime information control and security | permanent censorship, political suppression, false public confidence |
| Coast Watching and Air Defence | observation and incident evidence | poor coordination or foreign access |
| foreign liaison cells | British, American, German, Vatican, or neutral contacts | sponsor leverage and divided loyalty |

## Intelligence values

Part 4 uses architecture states that Part 5 will turn into decisions and missions.

- Foreign Penetration
- Intelligence Exposure
- Liaison Depth by foreign partner
- Domestic Intelligence Confidence
- Operational Warning
- Civil Liberty Strain

These do not replace Security Loyalty, Security Exposure, Republican Network Strength, or source-specific leverage.

## Intelligence route choices

- statutory civilian review
- military-led liaison
- Garda-centred domestic security
- dual service coordination
- party or command security organ
- clerical or institutional information network
- provincial or royal intelligence compact
- Otherworld site and witness protection under human law

## Intelligence failures

- German agents using republican or authoritarian contacts
- Allied liaison bypassing Irish authority
- false arrests and partisan investigations
- intelligence rivalry hiding threats
- censorship protecting government reputation rather than security
- political police expanding after the Emergency
- foreign access to sites, ports, weather, or communications without safeguards

# Operational planning

Every operational plan requires a command owner, named regions, units, equipment, supply, communications, intelligence, civilian authority, foreign liaison rule, review date, and failure response.

| Operational plan | Main regions | Minimum readiness emphasis | Political and diplomatic gate | Failure state |
| --- | --- | --- | --- | --- |
| continuity of government | Dublin alternatives, broadcasting, archives, transport, secure communications | command and communications, security, logistics | valid cabinet or route authority | government paralysis and succession crisis |
| Dublin and eastern defence | capital, port, eastern airfields, rail approaches | territorial defence, equipment, air warning, logistics | emergency command | loss of capital supply and national command |
| Cork Harbour defence | Cork Harbour, Berehaven approaches, roads, batteries, fuel | coastal defence, awareness, logistics | port policy and access doctrine | foreign seizure, disabled harbour, or maritime collapse |
| Atlantic rescue and denial | western and southwest sectors, rescue ports | awareness, Marine Service, logistics | neutrality doctrine | shipping loss, foreign protest, rescue failure |
| border and refugee plan | border counties, roads, depots, camps, local authorities | mobilisation, logistics, intelligence | Northern policy and civil-rights safeguards | communal violence, uncontrolled armed movement, service overload |
| Plan W liaison | border corridors, airfields, communications, ports | command, intelligence, logistics | Irish command safeguards and British bargain | leverage spike, exposed neutrality, divided command |
| airborne and sabotage response | airfields, depots, power, ports, capital | local defence, awareness, intelligence, mobility | security law | panic, false arrests, infrastructure loss |
| Northern intervention | crossings, Belfast, Derry, ports, industrial corridors | all components, especially logistics and command | valid Northern route, war authority, occupation plan | British war, communal conflict, occupation trap |
| expeditionary contribution | ports, training centres, overseas route | Equipment Sufficiency, Command and Training, Supply and Mobility, Maritime Access | lawful belligerency and home-defence reserve | home defence hollowed out and dependency |

# Route-specific defence orders

## De Valera constitutional stewardship

Classification: `H` baseline with `P` player variation

- civilian cabinet authority
- regular cadres, reserves, LSF, and LDF
- strong coastwatch, intelligence, internment, and operational liaison
- public neutrality with bounded covert cooperation
- priority on warning, supply, capital, ports, and continuity
- failure through permanent emergency power, weak equipment, or liaison exposure

## Lemass developmental defence

Classification: `P`

- professional staff and technical ministries
- signals, transport, air warning, workshops, and standardisation
- balanced procurement and domestic repair
- lower tolerance for militia fragmentation
- risk of technocratic dependency and delayed mass mobilisation

## Fine Gael professional defence

Classification: `P`

- civilian law, professional command, audited procurement
- reserve standards and alliance-compatible planning
- Mulcahy variant emphasises command and training
- Costello variant emphasises legal access agreements and coalition review
- risk of Civil War legitimacy conflict and creditor dependence

## Dillon intervention force

Classification: `P`

- Dáil-mandated war cabinet
- home-defence reserve protected before expeditionary commitment
- Allied equipment, shipping, intelligence, air, and command liaison
- formal belligerency remains gated by the fixed Part 2 mandate plus Part 4 material floors
- risk of unprepared war, British dependency, Northern deferment collapse, and public backlash

## Norton citizen defence

Classification: `P`

- parliamentary command with union, municipal, and cooperative logistics
- LDF, civil defence, medical, transport, and fair rationing
- officer standards protected through law
- risk of union split, officer mistrust, or emergency arbitration becoming coercive

## IRA civil integrated defence

Classification: `P`

- civil authority commands a unified national force
- local commands are integrated through rank, training, depot, and disarmament agreements
- republican legitimacy supports mobilisation where civil safeguards exist
- risk of armed dual authority and private foreign pipelines

## IRA GHQ defence

Classification: `P`

- Army Council and GHQ control mobilisation and war plans
- local commands supply territorial formations
- German or clandestine procurement remains possible and dangerous
- readiness can rise quickly in personnel and fall in command, equipment, and logistics
- risk of command fragmentation, foreign client status, and civilian collapse

## Congress plural citizen army

Classification: `P`

- common-programme civilian authority
- unions and committees support logistics and mobilisation
- armed wing remains subordinated
- local defence and workplace skills strengthen engineering, transport, medical, and civil defence
- risk of committee delay, officer conflict, and armed-wing autonomy

## Congress vanguard force

Classification: `P`

- central directorate and political command
- compulsory mobilisation and production
- political commissar or screening structures
- rapid personnel growth with skill, trust, and reporting losses
- risk of purge-driven collapse and military takeover

## O'Duffy corporate military order

Classification: `P`

- executive, army, veterans, and estates bargain over command
- corporate procurement and paramilitary formations
- Army Acceptance and Paramilitary Reliability remain separate
- sponsor equipment can raise dependency
- risk of personal guard state, rival command, and succession collapse

## Clerical guardianship defence

Classification: `P`

- lawful army command supported by medical, welfare, education, refugee, and local-service networks
- Vatican diplomacy supports humanitarian channels and never commands the army
- risk of clerical veto, minority distrust, and service overreach

## Ailtirí party army

Classification: `P`

- one-party military commission, ideological conscription, youth mobilisation, and cultural screening
- rapid manpower and coercive control
- technical expertise, minority security, foreign recognition, and equipment standardisation suffer
- post-Axis isolation can collapse procurement and officer confidence

## Constitutional royal defence

Classification: `P`

- elected government and general staff command the regular force
- crown guard is small, ceremonial, and legally bounded
- royal legitimacy can support voluntary service and long projects
- risk of household capture and dual command

## Sacral royal command

Classification: `A`

- royal guard, household obligations, and exceptional compact actors operate under or against human law
- ordinary army, provision, equipment, and communications remain required
- captive throne and royal warlordism are explicit failures

## Federal Five Provinces defence

Classification: `P` and `A` for the hidden pentarchy

- common army handles external defence
- provincial guards handle local security and civil defence
- standards, contribution quotas, deployment powers, and vetoes are defined by the compact
- historical Ulster requires a valid Northern settlement
- risk of divided command, unpaid contributions, provincial militia rivalry, and central overreach

## Otherworld compact defence

Classification: `A`

- human command remains responsible for ordinary defence
- site stewards, witnesses, compact courts, and eligible exceptional actors support limited tasks
- every exceptional capability has geographic, obligation, trust, and stability gates
- risk of foreign site capture, public panic, compact failure, and human-jurisdiction collapse

# National Readiness conclusion gates

| Capability | Readiness floor | Component floors | Other requirements |
| --- | ---: | --- | --- |
| functioning armed neutrality | `30` | Warning `20`, Maritime Protection `20` | Neutrality Integrity at least `60` preferred |
| Plan W technical liaison | `35` | Command `30`, Intelligence `30`, Supply `25` | Irish command safeguards and British agreement |
| credible national invasion defence | `45` | Equipment `15`, Supply `20`, Command `25` | Provision at least `40` |
| Dillon formal belligerency | `45` minimum | Equipment `40`, Command `40`, Supply `40` | every fixed Part 2 gate, National Provision `50` with no component below `30`, Maritime Access `40`, Transport Serviceability `40`, protected home-defence reserve, defined military contribution, and enforceable safeguards |
| normal constitutional voluntary war entry | `50` | Equipment `20`, Command `30`, Supply `30` | Consent `65`, lawful supermajority, Provision `45`, Northern policy, contribution plan |
| sustained Northern campaign | `60` | Supply `45`, Command `35`, Equipment `30` | Provision `55`, valid cause and occupation plan |
| limited expeditionary force | `65` | Supply `40`, Equipment `35`, Command `40`, Maritime Protection `30` | protected home-defence reserve and Maritime Access |
| Atlantic defence league | `75` | Warning, Maritime Protection, Command, and Intelligence at least `45` | real partners and shared command rules |
| highest external hidden ambition | `85` | no component below `55` | route gates, Provision `70`, valid obligations and aftermath plan |

# Neutrality Integrity and the Neutrality Ledger

## Neutrality Integrity purpose

`Neutrality Integrity` is the visible national value for active neutrality. It measures whether declared law, territorial control, public legitimacy, administrative capacity, and actual conduct remain coherent under repeated pressure.

The range is `0` to `100`. The normal September 1939 opening is `72` before route, law, and world-state adjustments.

| Integrity | State | Meaning |
| --- | --- | --- |
| `80` to `100` | Credible Armed Neutrality | law and enforcement remain coherent, independent, and materially credible |
| `60` to `79` | Practised Neutrality | discreet exceptions and cooperation remain publicly and institutionally sustainable |
| `40` to `59` | Selective Neutrality | enforcement is uneven, exposure is rising, and sponsor pressure shapes policy |
| `20` to `39` | Compromised Neutrality | patron access, concealed war, or weak territorial control threatens independence |
| `0` to `19` | Neutrality Breakdown | occupation, forced alignment, public restoration, or regime crisis becomes unavoidable |

The Neutrality Ledger records incident history, public stance, legal authority, source-specific leverage, obligations, access terms, internment, exposure, and partner-specific cooperation depth. These records are not averaged into extra national companion meters.

## Partner-specific cooperation depths

A cooperation depth can be tracked from `0` to `4` for each foreign partner and each defined channel. It is a record, not a national `partner-specific cooperation` value.

| Depth | Working state | Typical activity | Main risk |
| ---: | --- | --- | --- |
| `0` | no organised channel | ordinary diplomacy and ad hoc incident contact | slow response and missed intelligence |
| `1` | administrative contact | consular liaison, internment communication, weather, rescue, and routine technical contact | foreign expectation and minor exposure |
| `2` | technical cooperation | maps, equipment advice, communications, observation, discreet procurement | Integrity loss when unequal treatment becomes visible |
| `3` | operational liaison | invasion planning, intelligence fusion, controlled air or maritime support | major constitutional and foreign crisis if exposed |
| `4` | undeclared co-belligerency | sustained access, targeting support, logistics, or operations without public war status | retaliation, dependency, forced war entry, or government collapse |

British operational liaison does not erase a German agent network. German contact does not imply equal access or authority. A partner can have technical cooperation in one domain and no access in another.

## Neutrality policy domains

| Domain | Public rule questions | Operational questions | Typical incidents |
| --- | --- | --- | --- |
| airspace | overflight, pursuit, forced landing, warning, protest | identification, interception, internment, repair, crew handling | navigation error, reconnaissance, bombing, forced landing |
| shipping and waters | territorial waters, inspection, shelter, repair, prize law | route choice, rescue, mines, detention, escort, cargo security | sinking, seizure, submarine report, mine, covert cargo |
| internment | equal legal framework, parole, exchange, prosecution | camps, guards, medical care, escapes, diplomatic access | aircraft crews, sailors, soldiers, agents, escape scandal |
| intelligence | espionage law, service authority, foreign contact | G2, Garda, liaison, agents, codes, surveillance | agent arrest, liaison request, IRA contact, leak, false report |
| weather and navigation | civil and maritime safety, publication, restricted transmission | forecasts, coded reports, station security, rescue | Atlantic storm, aviation request, operational forecast, exposed bias |
| rescue and humanitarian action | duty to save life, relief, burial, refugee and civilian aid | lifeboats, hospitals, ports, transport, notification | shipwreck, aircraft crash, Belfast relief, coastal casualty |
| trade and supply | export control, import priorities, transit, inspection | shipping allocation, customs, fuel, cargo, credit | coal, oil, grain, fertiliser, machinery, smuggling |
| access | ports, airfields, radio, cables, corridors, troop movement | command, duration, customs, finance, withdrawal | base demand, Donegal corridor, shared facility, foreign command |
| censorship and information | military secrecy, political speech, casualty and shortage reporting | press, post, communications, review, investigation | leaked liaison, bombing report, scandal, opposition challenge |
| border policy | refugees, trade, smuggling, security, Plan W | local forces, corridors, policing, intelligence | border violence, refugee flow, arms movement, British incursion |

## Neutrality stance families

- strict legal neutrality uses published rules, strong internment, and restrained technical contact
- armed adaptive neutrality adds credible warning, maritime protection, mobilisation, and denial capacity
- discreet Western cooperation preserves public neutrality while allowing bounded Allied intelligence, weather, rescue, procurement, and invasion-contingency work under Irish command
- deep cooperation short of war permits broader planning and access while retaining a public neutral status that can still fail through exposure or dependency
- Axis opportunism uses German contact for procurement, deception, authoritarian sponsorship, or anti-British strategy and always faces a delivery and sponsor-survival test
- protected dependency retains formal sovereignty while foreign supply, command, access, debt, recognition, or guarantees dominate policy
- open belligerency transforms the ledger into public alliance and war obligations after lawful entry
- neutrality restoration removes or reviews access, repairs law and territorial control, settles incidents, demobilises, and restores public authority

Deep cooperation short of war requires Readiness at least `30`, Neutrality Integrity at least `45`, Social Consent at least `50`, British Leverage below `70`, lawful authority, defined Irish command, and no unresolved foreign-access scandal.

## Integrity movement

Integrity rises through coherent law, Irish command, territorial control, credible incident settlement, public review, lawful humanitarian action, diversified supply, fair legal procedure, and safeguards that limit foreign authority.

Integrity falls through unexplained exceptions, exposed one-sided cooperation, foreign command, unequal or corrupt internment, uncontrolled agents, repeated territorial violations, censorship abuse, direct attack, low readiness, severe shortage, unresolved incidents, and a government whose public stance conflicts with its actual route.

`Neutrality Pressure` can be shown as a derived breakdown of active incidents, shortages, access demands, shipping loss, bombing, intelligence exposure, border crisis, sponsor pressure, and cooperation that exceeds public law. It is a diagnostic summary, not a second national meter.

## Incident severity

| Severity | Definition | Required response |
| ---: | --- | --- |
| `1` | routine violation or uncertain report | record, investigate, local response, possible protest |
| `2` | confirmed violation with limited damage | national review, legal disposition, foreign communication |
| `3` | repeated or politically sensitive breach | cabinet response, mission, public or parliamentary choice |
| `4` | strategic incident | emergency conference, mobilisation option, stance revalidation |
| `5` | attack, invasion, ultimatum, or exposed undeclared war | lawful war, retreat, alliance, client bargain, restoration, or regime crisis |

Every major incident ends through legal and material success, material success with political cost, political success with material cost, partial containment with a timed obligation, or failure that raises exposure, leverage, dependency, or war risk. Opinion changes alone do not resolve an incident.

## War-entry rules

Dillon keeps every fixed Part 2 requirement: Intervention Mandate `90`, National Readiness `45`, Social Consent `60`, a Dáil majority, British Leverage below `60`, sovereignty safeguards, a Northern policy or lawful deferment, and no active constitutional crisis. Part 4 also requires National Provision at least `50` with no component below `30`, Maritime Access at least `40`, Transport Serviceability at least `40`, Equipment Sufficiency at least `40`, Command and Training at least `40`, Supply and Mobility at least `40`, a protected home-defence reserve, a defined military contribution, and enforceable access, command, customs, finance, Northern, withdrawal, and review safeguards.

Other voluntary constitutional war entry without direct attack requires Readiness `50`, Social Consent `65`, a Dáil supermajority or equivalent lawful mandate, National Provision `45`, a Northern policy or lawful deferment, a defined military contribution plan, and no unresolved command or access crisis.

Direct attack can create an emergency war state below these floors. It also creates Overextension, public-law review, foreign-command, civilian-protection, and postwar-restoration obligations.

# Neutrality route families

## De Valera's Emergency neutrality

Classification: `H`

The historical baseline combines public neutrality, Emergency powers, internment, censorship, active trade management, humanitarian action, weather cooperation, intelligence liaison, and preparation against invasion.

### Player choices

- how far Allied liaison develops
- whether internment remains strict, flexible, or politically manipulated
- how much information reaches the public
- which trade and access concessions are accepted
- whether preparedness justifies stronger emergency authority
- when wartime powers begin to expire

### Success conclusion

A stable neutral republic requires Neutrality Integrity at least `60`, Social Consent at least `55`, National Readiness at least `30`, National Provision at least `45`, no unresolved severity `4` or `5` neutrality incident, no partner cooperation depth `4`, and a dated emergency-law exit.

### Failure conclusions

- permanent emergency government
- neutrality without enforcement
- exposed undeclared Allied alignment
- British protected dependency
- internal republican or opposition crisis after repression

## Lemass pragmatic neutrality

Classification: `P`

Lemass treats neutrality as a platform for development, trade diversification, technical cooperation, and postwar access. He favours practical Allied contact without surrendering economic or administrative control.

Tradeoffs include American credit, British markets, domestic industrial protection, and the risk that technical dependence becomes foreign policy dependence.

## Fine Gael lawful neutrality

Classification: `P`

Fine Gael places neutrality under parliamentary review, professional defence, published access rules, and statutory emergency powers. It gains institutional credibility and can lose operational speed. Coalition partners can block secret liaison or foreign concessions.

## Dillon intervention

Classification: `P`

Dillon's path begins as public opposition to neutrality. He must build an Intervention Mandate through speeches, votes, defence delivery, foreign safeguards, and a Northern policy. The fixed Part 2 formal belligerency gate remains unchanged.

Part 4 adds these material gates:

- National Provision at least `50`, with no component below `30`
- Maritime Access at least `40`
- Transport Serviceability at least `40`
- Equipment Sufficiency at least `40`
- Command and Training at least `40`
- Supply and Mobility at least `40`
- home-defence reserve protected
- defined military contribution recorded
- access, command, customs, finance, Northern, withdrawal, and review safeguards recorded and enforceable

A route can enter deep cooperation short of war when the political mandate is insufficient. Formal entry without material floors creates an Unprepared Belligerency failure and severe dependency.

## Norton democratic neutrality

Classification: `P`

Norton connects neutrality to worker protection, fair rationing, citizen defence, anti-fascist sympathy, humanitarian action, and parliamentary control. Labour can support deeper Allied cooperation without accepting automatic war entry.

The route fails when emergency arbitration suppresses independent labour, unequal supply discredits neutrality, or the Labour and National Labour split destroys the mandate.

## IRA neutrality or revolutionary war

Classification: `P`

A civil republican state can claim armed anti-imperial neutrality, seek recognition, and balance foreign contacts. An Army Council state may treat the European war as an opportunity for partition conflict or German supply.

German contact raises Security Exposure and British retaliation. Allied contact creates ideological and command disputes. A revolutionary government that invites one belligerent while claiming strict neutrality loses credibility quickly.

## Congress anti-fascist non-alignment

Classification: `P`

The plural Congress can maintain formal neutrality while supporting refugees, labour solidarity, intelligence against fascist networks, and selected Allied technical cooperation. A vanguard government can align with an available socialist patron or enter war through an anti-fascist mandate.

Labour and committee consent remain real. Anti-fascist purpose does not create ships, weapons, or a public war mandate.

## O'Duffy and Axis opportunism

Classification: `P`

O'Duffy can seek Axis political recognition, arms, training, propaganda, or strategic support. German and Italian capacity, interest, access, and survival are separate. A patron can demand ports, intelligence, war policy, persecution, and military subordination.

Axis alignment can begin through covert cooperation and becomes a public client route when Sponsor Dependence exceeds the safeguard ceiling. Axis defeat creates abandonment, invasion risk, or regime collapse.

## Clerical humanitarian neutrality

Classification: `P`

A guardianship or vocational government emphasises relief, prisoners, refugees, medical networks, mediation, and Vatican channels. Humanitarian credibility can support neutrality. Clerical censorship, minority exclusion, or political policing can destroy it.

## Ailtirí strategic alignment

Classification: `P`

Ailtirí can seek German support for total national transformation and reconquest. The route must portray anti-democratic rule, antisemitism, coercion, and client pressure directly. German support does not create a viable invasion plan without shipping, intelligence, equipment, and local control.

## Royal and provincial neutrality

Classification: `P`

A constitutional High Kingdom can use crown diplomacy and ceremonial continuity under elected authority. A Five Provinces federation requires one common external doctrine. Provincial foreign contacts cannot create separate military commitments without triggering a federal crisis.

## Otherworld secrecy and neutrality

Classification: `A`

A compact route has two distinct questions.

- Ireland's human diplomatic status in the European war
- foreign access to sites, witnesses, passages, and compact knowledge

Neutrality law cannot resolve the second question without new public or secret law. Foreign access raises obligations, Compact Trust risk, public-knowledge risk, and sovereignty conflict. Exceptional actors do not become a free belligerent force.

# Foreign leverage, obligations, and dependency

## Source-specific rule

British, American, German, and Vatican Leverage keep their fixed opening values and remain separate. Additional partners can use relationship and obligation records without creating a new national leverage meter unless Part 5 and implementation evidence justify one.

Every major foreign bargain creates an Obligation Record.

## Obligation Record fields

- foreign partner
- public or secret status
- material received
- Irish contribution
- access granted
- command rights
- intelligence rights
- customs and financial terms
- Northern Ireland clause
- duration and renewal
- withdrawal or termination rule
- exposure risk
- dependency effect
- breach consequences

A focus can open negotiation or change acceptable terms. The bargain completes through decisions, missions, events, delivery, and foreign acceptance.

## Sovereignty safeguards

A stable cooperation agreement normally requires six safeguards.

1. valid Irish authority approves the agreement
2. bases, ports, airfields, routes, or offices have defined duration and expiry
3. Irish command boundaries are written and enforceable
4. customs, taxation, procurement, and finance remain under stated control
5. Northern Ireland has a policy, settlement clause, or lawful deferment
6. postwar withdrawal, demobilisation, or renegotiation is specified

Radical or authoritarian routes can reject safeguards. Doing so raises dependency and creates distinct client or occupation conclusions.

## Dependency stages

| Source-specific leverage or sponsor dependence | Working stage | Meaning |
| ---: | --- | --- |
| 0 to 29 | contact | partner has access and influence without structural control |
| 30 to 49 | influence | Irish policy increasingly accounts for partner expectations |
| 50 to 69 | dependency risk | interruption or refusal has major material cost |
| 70 to 84 | client pressure | partner can demand policy, access, command, or internal concessions |
| 85 to 100 | protected or client order | sovereign choice is severely constrained and route identity changes |

A high relationship is not the same as high leverage. Aid can be friendly and still create structural dependence.

# British bargaining

Classification: `H` foundation and `P` alternatives

## British interests

- western approaches and Atlantic security
- Treaty Ports and denial of hostile access
- Northern Ireland and Stormont
- trade, shipping, fuel, and food
- intelligence, weather, airspace, and Plan W
- preventing German influence
- maintaining imperial and Commonwealth strategic coherence

## Irish bargaining assets

- sovereign control of territory and ports
- trade, food, labour, and shipping cooperation
- weather and coastal observation
- intelligence and counter-agent cooperation
- denial of hostile access
- public legitimacy and neutral mediation
- diaspora and American political effects
- willingness to discuss Northern settlement

## Bargaining packages

- trade and coal arrangement
- equipment and training contract
- coastwatch and air-warning liaison
- Plan W planning under Irish command
- controlled port repair or access
- wartime unity proposal
- formal alliance and basing
- postwar withdrawal and recognition settlement

British Leverage rises when Ireland depends on one trade route, accepts indefinite access, cannot defend ports, or has no alternative supply. It falls through diversified trade, strong readiness, clear command, American counterweight, and credible public authority.

# American access and diaspora politics

Classification: `H` foundation and `P` expansion

## American interests

- Allied war policy and pressure against Axis access
- aviation, shipping, weather, and Atlantic routes
- public presentation of neutrality
- diaspora politics and Irish-American opinion
- postwar trade, credit, aviation, and security

## Diaspora channels

- remittances and family networks
- political lobbying
- public fundraising
- technical and business contacts
- cultural organisations
- military volunteers outside direct state control

Diaspora support does not automatically belong to the government. Rival parties, republican networks, Church bodies, labour groups, and regional associations compete for it.

## Access bargains

- technical missions
- aviation and weather cooperation
- credit and machinery contracts
- merchant shipping and repair support
- humanitarian and refugee support
- postwar airport and Atlantic-service agreement
- military access after lawful alignment

American Leverage rises when credit, machinery, shipping, or diplomatic recognition becomes irreplaceable. A balanced British-American strategy can reduce single-sponsor dependence and can create conflicting obligations.

# German liaison and Axis supply

Classification: `H` contact foundation and `P` route expansion

## German interests

- intelligence on Britain and the Atlantic
- Irish political and republican contacts
- propaganda value
- possible disruption or diversion
- port, weather, air, or radio access

## Irish route interests

- arms and training
- support against partition or Britain
- recognition of an alternative regime
- ideological patronage
- intelligence exchange
- trade or technical supply

German assistance faces severe access, shipping, operational, and trust limits. Agent networks can be penetrated. Promised arms may never arrive. A contact can increase British pressure faster than it increases Irish capability.

Axis opportunism requires:

- a route willing to accept authoritarian or military consequences
- a delivery channel
- security and command control
- a plan for British reaction
- a post-Axis survival strategy

Without those conditions the route produces exposure, arrests, retaliation, or client failure.

# Vatican diplomacy and humanitarian networks

Classification: `H` foundation

Vatican Leverage covers foreign diplomatic and ecclesiastical influence. It does not measure domestic Church command.

Potential channels include:

- diplomatic recognition and mediation
- humanitarian appeals
- prisoner and refugee communication
- protection of institutions and minorities
- moral pressure on war entry, repression, labour, censorship, and education
- postwar international presentation

A clerical government can have high domestic Church influence and low Vatican compliance. A secular or socialist government can retain Vatican diplomacy while restricting domestic institutional power.

# Atlantic and small-state diplomacy

Classification: `P` built from `H` contacts

Ireland can pursue cooperation with neutral, small, or Atlantic-facing states through:

- diplomatic consultation
- shipping and rescue standards
- food, fuel, and procurement exchange
- prisoner and refugee arrangements
- civil aviation and weather
- postwar trade and reconstruction
- cultural and academic exchange
- common opposition to great-power domination

This route requires real partners. A conference with no willing states does not create a faction or guarantee. Members can refuse military obligations while accepting trade or humanitarian cooperation.

# Postwar foreign policy choices

## Independent republic

Classification: `H` foundation and `P` timing

The government can complete a constitutional and external-relations settlement that changes the state's formal identity. It requires lawful authority, head-of-state settlement, diplomatic notification, Commonwealth or British relationship policy, treaty review, defence policy, citizenship and nationality rules, and Northern Ireland policy.

## Continued association

Classification: `P`

Ireland can preserve selected Commonwealth or bilateral ties under a sovereign constitutional arrangement. The route must define head-of-state, defence, trade, citizenship, and diplomatic representation.

## Atlantic security cooperation

Classification: `P`

A postwar Ireland can seek guarantees, intelligence cooperation, air and maritime arrangements, or full alliance. Partition, bases, command, public consent, and dependency remain active.

## European economic cooperation

Classification: `P`

Ireland can pursue postwar trade, reconstruction, standards, transport, and institutional cooperation. This is a late-game economic and diplomatic lane, not an instant modernisation reward.

## Neutral small-state leadership

Classification: `P`

A credible neutral Ireland can organise mediation, humanitarian, shipping, legal, or economic cooperation among small states. It needs credibility, provision, diplomatic reach, and participating states.

# Northern Settlement Ledger

## Northern Settlement purpose

The `Northern Settlement Ledger` models partition as a political, constitutional, industrial, security, labour, religious, and diplomatic problem. It begins before any unity negotiation and continues after deferment, cooperation, federation, occupation, or constitutional integration.

Six values remain separate. They are never averaged into one unity score.

| Value | Opening value | Meaning |
| --- | ---: | --- |
| Unionist Consent | `5` | willingness of unionist communities and institutions to accept a defined relationship with Dublin or constitutional change |
| Nationalist Consent | `40` | organised support among northern nationalists for a specific rights, federal, unity, labour, or autonomy programme |
| Labour Cooperation | `30` | cross-community capacity among unions, municipalities, professional bodies, cooperatives, churches, and civic organisations |
| British Flexibility | `10` | British willingness and capacity to negotiate constitutional, defence, financial, and guarantee changes |
| Security Stability | `45` | degree to which policing, border conditions, communal relations, and armed organisations remain governable without exceptional force |
| Integration Capacity | `10` | practical capacity to finance, administer, police, supply, represent, and protect a changed order |

A high Nationalist Consent value cannot erase low Unionist Consent. British Flexibility cannot substitute for local ratification. Military control does not create Security Stability or Integration Capacity.

## Unionist Consent movement

Unionist Consent rises through credible rights, property and pension safeguards, local government, fair representation, independent courts, policing guarantees, industrial continuity, educational and religious autonomy, reliable implementation, and accepted external guarantees.

It falls through violence, confiscation, cultural compulsion, purge, vague finance, abolition of local institutions without replacement, foreign alignment that threatens local security, and territorial rhetoric without a workable settlement.

## Nationalist Consent movement

Nationalist Consent rises through organisation, elections, civil-rights work, labour cooperation, protection from discrimination, credible Dublin support, and a clear constitutional programme.

It falls through factional rivalry, southern neglect, indiscriminate violence, repression, and settlements that preserve inequality without reform.

## Labour Cooperation movement

Labour Cooperation rises through union coordination, municipal work, housing, welfare, reconstruction, professional and cooperative networks, protected organising, and shared industrial interests.

It falls through communal mobilisation, discriminatory employment, strikebreaking, industrial collapse, armed rivalry, compulsory estates, vanguard control, and imposed southern leadership.

## British Flexibility movement

British Flexibility rises through overextension, wartime bargaining, American pressure, Stormont failure, high subsidy or security cost, Irish defence safeguards, an acceptable guarantee, and postwar constitutional change.

It falls through strategic dependence on Northern bases and industry, fear of hostile access, reliable Stormont mobilisation, strong domestic opposition to change, and an Irish route that threatens British security.

## Security Stability movement

Security Stability rises through ceasefire, verified disarmament, fair policing and courts, representation, economic recovery, relief, credible timetables, external guarantees, and successful integration work.

It falls through IRA or loyalist violence, discriminatory policing, border incidents, conscription crisis, bombing, arms imports, partisan occupation, reprisals, inflammatory policy, and foreign intelligence operations.

## Integration Capacity movement

Integration Capacity rises through joint commissions, tax and currency planning, pension and debt settlement, police and court transition, industry and transport agreements, local-authority participation, rights and education settlements, trained staff, budgets, and demobilisation plans.

It falls through sudden transfer, war damage, purge, fiscal crisis, incompatible law, occupation without local administration, industrial flight, and premature foreign withdrawal.

# Northern regional architecture

Northern policy uses six interface regions. These are design regions for decisions, missions, event targeting, and integration records. They do not presume new state borders.

| Interface region | Political and social profile | Material role | Main settlement problem |
| --- | --- | --- | --- |
| Belfast and Belfast Lough | unionist government centre, dense working class, mixed districts, major municipal institutions | shipbuilding, engineering, aircraft, port, housing, transport, power | government authority, industry, labour, housing, policing, air defence, debt |
| northeast Antrim | strong unionist organisation, rural and industrial links, coastal access | agriculture, ports, roads, coastal defence | consent, local government, security, British access |
| Down and Armagh corridor | mixed communities, border routes, agriculture, military importance | roads, rail, food, airfields, border movement | boundaries, policing, representation, communal security |
| Derry and Lough Foyle | divided city and hinterland, nationalist strength, strategic lough | port, industry, Atlantic access, transport | franchise, local government, port command, cross-border access |
| Tyrone and Fermanagh | nationalist-majority or mixed districts, rural economy, long border | agriculture, roads, local administration, security | county consent, boundary questions, policing, service delivery |
| Mid-Ulster and Lough Neagh | mixed rural and industrial communities, transport centre | food, linen, water, roads, local markets | district boundaries, labour, common services, regional autonomy |

A settlement can treat regions differently when the constitutional process allows it. Regional differentiation requires transparent rules and cannot be a disguise for arbitrary ethnic cleansing or forced expulsion.

# Northern settlement process and integration ladder

## Seven-step settlement process

1. **Claim and contact** establishes public policy, legal authority, named interlocutors, route purpose, and disqualifiers.
2. **Confidence measures** deliver bounded work in trade, transport, rescue, labour, policing, services, refugees, or civil defence.
3. **Proposal mandate** gives the Dublin or route government authority to offer a specific settlement instead of a general claim.
4. **Northern representation** defines who speaks for unionists, nationalists, labour, local authorities, industry, churches, security bodies, and affected districts.
5. **British settlement** resolves constitutional authority, troops, finance, bases, guarantees, debt, and withdrawal or continuing association.
6. **Public ratification** uses an election, plebiscite, convention, parliamentary vote, dual majority, regional mandate, or route-valid public process.
7. **Implementation** creates the transition authority, timetable, rights floor, administration, finance, policing, services, military settlement, review, and failure procedure.

A coercive route replaces Northern representation and public ratification with military control, resistance, foreign reaction, and a later settlement requirement. It does not receive consent through conquest.

## Integration stages

| Stage | Working state | Required evidence | Main failure |
| ---: | --- | --- | --- |
| `0` | claim only | constitutional aspiration, propaganda, diplomatic note, or war aim | rhetoric without local access or capacity |
| `1` | contact and functional bodies | named actors, lawful contacts, targeted boards, routes, or services | capture, boycott, unequal delivery, or security incident |
| `2` | provisional settlement | written proposal, interim authority, guarantees, finance, and timetable | institutional vacuum, rejected mandate, or foreign veto |
| `3` | shared administration | functioning joint or transitional bodies in several domains | divided command, service failure, local obstruction, or fiscal dispute |
| `4` | integrated administration | common law and services operate with protected local authority and settled security | rights crisis, resistance, administrative flight, or regional collapse |
| `5` | stable constitutional integration | durable representation, rights, finance, policing, services, guarantees, demobilisation, and review | constitutional reversal, renewed violence, or foreign occupation |

Partial success can raise one ledger value or one administrative domain without advancing the whole stage. A transport board can function while policing remains contested. An industrial agreement can improve Labour Cooperation and Integration Capacity while Unionist Consent remains low. Part 5 must preserve mixed outcomes.

# Settlement families

# Lawful deferment

Classification: `H` and `P`

The government preserves the constitutional claim or replaces it with a negotiated aspiration, while accepting that immediate unity lacks consent or strategic conditions.

A durable deferment can include:

- formal rights and cross-border commissions
- trade and transport cooperation
- nationalist representation and protection
- a future review date
- security and non-interference commitments
- British and Irish guarantees
- humanitarian and family access

Deferment is a meaningful conclusion when it raises Security Stability, improves rights, and creates functioning cooperation. It is a failure when it becomes passive abandonment or a cover for repression.

# Cross-border functional settlement

Classification: `P`

This route creates shared boards for electricity, transport, disease control, fisheries, trade, labour, tourism, civil defence, or waterways. It can prepare later federal or unitary settlement and can remain a long-term practical arrangement.

The player must prevent boards from becoming empty diplomacy. Each board needs funding, jurisdiction, local participation, and project delivery.

# The 1940 wartime bargain

Classification: `H` opening and `P` full negotiation

The British proposal opens a crisis negotiation among Dublin, London, Stormont, northern political actors, and the Irish public.

## Required agenda

- immediate defence cooperation
- Irish military readiness and command
- British implementation authority
- Stormont and unionist response
- constitutional form of unity
- transition timing
- policing and security
- ports and bases
- finance, debt, pensions, and taxation
- Belfast industry and labour
- minority safeguards
- foreign guarantees
- public ratification

## Wartime bargain threshold

- Unionist Consent at least `20` or enforceable guarantees that preserve local authority and rights
- Nationalist Consent at least `50`
- British Flexibility at least `45`
- National Readiness at least `35`
- the defence scope, command, transition timetable, finance, and ratification method are defined

## Possible outcomes

- proposal rejected with no lasting agreement
- defence cooperation without unity
- postwar unity pledge with interim guarantees
- federal transition
- British proposal collapses after Stormont refusal
- Irish unpreparedness delays implementation
- negotiated unitary transition
- foreign or domestic crisis destroys the bargain

The route cannot bypass Unionist Consent, British implementation, Integration Capacity, or Irish readiness.

# Federal all-Ireland settlement

Classification: `P`

A federal settlement preserves substantial Northern or provincial self-government within a common Irish state.

## Federal subjects

The common authority normally controls:

- foreign affairs
- defence
- currency and customs
- national transport and major ports
- citizenship and national rights floor
- national taxation or agreed contribution

The Northern or provincial authority can control:

- local government
- education and culture
- health and housing
- local policing under national rights standards
- regional economic development
- defined taxes and services

## Federal settlement threshold

- Unionist Consent at least `45`
- Nationalist Consent at least `60` for the specific federal offer
- Labour Cooperation at least `45`
- British Flexibility at least `50`
- Security Stability at least `55`
- Integration Capacity at least `40`
- valid powers, finance, rights, policing, and ratification in the relevant jurisdictions

Higher thresholds reduce transition cost. A route can force a lower-confidence federation after war and will face resistance, veto, and foreign guarantees.

## Federal failures

- centre unable to fund defence or services
- Northern government blocking common law
- Dublin overriding autonomy
- segregated policing surviving under a new flag
- provincial fiscal veto
- competing foreign access agreements
- no accepted capital, court, or representation settlement

# Plebiscite and consent settlement

Classification: `P`

A plebiscite route must define electorate, district, date, campaign rights, security, observation, threshold, appeals, and post-vote guarantees.

## Models

- six-county vote
- county votes
- district or corridor votes
- staged vote after an autonomy period
- dual-majority federal vote
- all-island constitutional ratification with a separate Northern consent rule

## Plebiscite settlement threshold

- British Flexibility at least `55`
- Security Stability at least `60`
- Integration Capacity at least `30` preferred before the vote
- electorate, registers, district rules, campaign rights, supervision, appeals, and post-vote guarantees are defined
- no active military occupation determines the result

## Boundary safeguards

- boundaries cannot be changed after results are known
- local-government and franchise disputes must be reviewed before the vote
- mixed urban and rural areas need explicit treatment
- Belfast cannot be divided through a vague map reward
- minorities on each side receive representation, services, property, and security guarantees
- population transfer is rejected as a routine settlement tool

A close or disputed result opens recount, court, security, and mediation systems. It does not create instant cores.

# Negotiated unitary settlement

Classification: `P`

A unitary settlement abolishes or transforms Stormont and places Northern Ireland under one national constitutional order. It requires stronger consent and preparation than federalism.

## Minimum architecture

- common parliament representation
- local government protection
- police and court transition
- public service continuity
- industry and labour compact
- education and religious settlement
- debt and pension assumption
- British withdrawal and guarantee
- phased security integration
- rights charter and enforcement

## Negotiated unitary settlement threshold

- Unionist Consent at least `60`
- Nationalist Consent at least `65`
- Labour Cooperation at least `50`
- British Flexibility at least `60`
- Security Stability at least `65`
- Integration Capacity at least `55`
- a new constitutional order, local safeguards, and accepted withdrawal terms

A lower-confidence unitary agreement can exist after major external change and will require longer autonomy, guarantee, and integration periods.

# Labour and social commonwealth settlement

Classification: `P`

Labour or plural Congress routes can build unity around housing, employment, unions, welfare, municipal reform, public industry, and civil rights.

The route requires northern labour autonomy. Dublin Labour, National Labour, Congress, Belfast unions, and local socialist or labour organisations do not merge automatically.

## Programme

- non-discrimination in employment and housing
- union rights and cross-border bargaining
- public reconstruction after bombing
- shipyard and engineering conversion
- municipal franchise and representation reform
- integrated welfare and pensions
- public transport, power, and housing boards
- constitutional autonomy and rights

## Labour social settlement threshold

- Unionist Consent at least `35`
- Nationalist Consent at least `55`
- Labour Cooperation at least `65`
- British Flexibility at least `45`
- Security Stability at least `55` preferred
- Integration Capacity at least `40`
- union freedom, industrial delivery, rights, and local autonomy remain enforceable

Failure occurs when class policy ignores national and religious identity, when vanguard actors capture unions, or when southern parties impose candidates and leadership.

# Royal or provincial Northern settlement

Classification: `P` and `A` where hidden forms apply

## Crown settlement

A constitutional crown can offer symbolic continuity, a bounded Northern household, local autonomy, and external recognition. The crown must be elected or otherwise valid under Part 3 rules. Unionists are not assumed to accept a Gaelic crown. British dynastic or Commonwealth associations require explicit negotiation.

## Five Provinces settlement

Historical Ulster can become a valid province only through northern mandates, boundaries, rights, and common-law settlement. Models include:

- federal Ulster within five provinces
- northern province with substantial autonomy
- several regional mandates and a common Ulster council
- four provinces and an empty chair until consent exists
- Crown and Five Provinces after dual ratification

The hidden pentarchy cannot receive Northern territory through cultural symbolism.

# Coercive reunification

Classification: `P` for plausible armed conflict and `A` for impossible expansion methods

Coercive reunification begins through invasion, uprising, British collapse, foreign war, or an authoritarian decision to use force.

## Coercive reunification threshold

- valid command authority and route-valid cause
- National Readiness at least `60`
- Supply and Mobility at least `45`
- National Provision at least `55`
- border, depot, bridge, fuel, medical, and replacement plans
- civilian protection, policing, detention, and rights rules
- Belfast, port, industry, and urban relief plan
- British reaction and foreign sponsor record
- occupation administration and postwar transition budget

A lower-readiness route can attempt war and receives an improvised campaign with severe failure risk.

## Occupation states

| State | Meaning | Core effects |
| --- | --- | --- |
| contested control | active combat and fragmented administration | collapsed Security Stability, no integration credit |
| military occupation | routes and centres held by force | requisition, resistance, foreign reaction, low Unionist Consent |
| provisional civil administration | local services and courts restored under supervision | Integration Capacity can rise, rights and representation tested |
| transitional autonomy | local institutions operate under a settlement timetable | security integration, fiscal and political negotiation |
| integrated non-core territory | national law applies with persistent special measures | compliance, services, rights, and demobilisation determine core progress |
| accepted constitutional territory | long-term settlement and high compliance | core eligibility after every domain passes review |

## Coercive route failures

- British war and blockade
- Belfast urban siege or industrial destruction
- loyalist insurgency
- nationalist disillusion after repression
- sectarian reprisals
- army or militia atrocities
- foreign client occupation
- southern provision collapse
- permanent emergency government
- partition reproduced inside an occupied state

No coercive route receives automatic cores. Cores require a long integration and rights process with higher thresholds than negotiated settlement.

# External collapse and wartime opportunity

Classification: `P`

A major British defeat, invasion of Britain, Axis landing, Allied counteroffensive, or collapse of Stormont can create a rapid Northern crisis.

Ireland can:

- defend the border and preserve neutrality
- implement Plan W liaison
- occupy limited zones by agreement
- support civil authorities and refugees
- negotiate an emergency federation
- enter war for an all-island settlement
- exploit the collapse through coercive occupation
- invite a foreign patron

The crisis does not erase local actors. Unionist, nationalist, labour, police, army, municipal, British, and foreign responses continue.

# Transition authority architecture

## Composition rule

A transition authority must represent enough of the settlement to govern. Its possible seats include:

- Dublin or common government
- Northern elected representatives
- unionist representatives
- nationalist representatives
- labour and civic representatives
- local authorities
- police and judicial administration
- industry and finance
- education and religious bodies
- British or external guarantors without executive control
- provincial authorities
- crown, compact, or other route-specific offices

A one-party, military, or foreign-controlled transition is possible and carries coercion and legitimacy penalties.

## Transition domains

The transition authority maintains a ledger of twelve domains.

1. constitutional representation
2. local government and franchise
3. courts and legal continuity
4. policing and public order
5. armed groups and military command
6. finance, currency, debt, and taxation
7. pensions, welfare, and public employment
8. industry, contracts, power, ports, and transport
9. housing, reconstruction, and municipal services
10. education, religion, language, and culture
11. minority rights, property, and political participation
12. British withdrawal, foreign guarantees, and external relations

Each domain can be unresolved, provisional, functioning, contested, or settled. Core progression requires every domain to reach functioning and most to reach settled.

# Stormont and successor government

## Institutional options

- retained Stormont under federal law
- reformed Northern assembly
- temporary transition council
- provincial Ulster assembly
- direct common-government administration with local councils
- municipal and county federation
- suspended government during military occupation

Retaining Stormont can preserve administrative continuity and old discrimination. Abolition can remove a symbol of partition and destroy local capacity. The player must reform institutions rather than assume either outcome is clean.

## Representation questions

- electoral system
- constituency boundaries
- franchise
- upper or advisory chambers
- executive formation
- minority veto or rights review
- relation to Dublin, federal, provincial, or crown government
- emergency dissolution and judicial review

# Policing, security, and armed integration

## Police models

- reformed Royal Ulster Constabulary under federal or national law
- new Northern civic police
- integrated all-Ireland police with regional command
- dual police transition
- military occupation police
- local or provincial constabularies

Each model must resolve recruitment, command, vetting, weapons, training, complaints, intelligence, local trust, and relation to Garda and military forces.

## Armed organisations

- British forces
- regular Irish forces
- RUC and auxiliary structures
- IRA local and GHQ formations
- loyalist organisations
- local defence and civil defence
- provincial guards
- party militia
- foreign liaison or occupation forces

Disarmament can use amnesty, integration, retirement, prosecution, weapons collection, local security guarantees, and verified demobilisation. Purging every experienced actor creates a capacity gap. Integrating unvetted forces creates infiltration and abuse.

# Northern industrial and economic integration

## Strategic assets

- Belfast port and shipbuilding
- engineering and aircraft production
- linen and textiles
- power and utilities
- rail and road networks
- housing and municipal services
- skills, managers, contracts, unions, and finance
- Derry and Lough Foyle access
- agriculture and food distribution

Control of a factory or shipyard does not produce output. Integration requires inputs, contracts, labour, management, power, transport, repair, security, and market access.

## Industrial settlement models

- protected continuity under local management
- public reconstruction and conversion
- federal industrial board
- Labour and union co-management
- corporate estate absorption
- revolutionary nationalisation
- foreign contract zone
- military requisition

Each model changes Unionist Consent, Labour Cooperation, Provision, British Leverage, and resistance.

## Debt and finance

The settlement must allocate:

- Northern public debt
- pensions and public salaries
- municipal obligations
- industrial loans and guarantees
- currency conversion or continuity
- tax collection
- customs and trade
- British grants or withdrawal payments
- reconstruction cost

Refusing every inherited obligation damages confidence and services. Assuming every obligation without revenue can collapse southern provision.

# Education, religion, language, and minority rights

## Rights floor

Every negotiated settlement requires:

- freedom of worship
- equal citizenship and public employment
- fair access to housing, education, welfare, courts, and policing
- political organisation and press rights within public-order law
- protection of property with lawful compensation rules
- safeguards against cultural compulsion
- language access where demand and capacity exist
- review and enforcement

Authoritarian routes can reject these safeguards and receive resistance, foreign reaction, skill loss, and legitimacy consequences.

## Education models

- preserved regional systems with a common rights floor
- national standards and local administration
- federal education powers
- Church and institutional partnership
- secular public reform
- Gaelic expansion by consent and service capacity
- coercive cultural assimilation under Ailtirí or a corrupted hidden route

Cultural Capacity can provide teachers, terminology, archives, broadcasting, and administration. It cannot compel acceptance or erase existing institutions.

# Foreign guarantees and withdrawal

A Northern settlement can include:

- British guarantee of autonomy and rights
- Irish guarantee of local institutions
- joint guarantee
- American or multilateral observation
- fixed British troop withdrawal
- temporary access for transition security
- neutral commission for disputes
- federal constitutional court
- plebiscite review clause

A guarantee without enforcement rules is symbolic. A guarantee with indefinite foreign troops can become dependency or continued partition.

# Claims and core progression

## Claim progression

1. constitutional aspiration or Article-based claim
2. diplomatic claim with an active policy
3. negotiated provisional authority or wartime control
4. transitional administration
5. integrated non-core status
6. accepted constitutional territory
7. core eligibility after long review

## Core review criteria

Northern core status can be considered only after integration stage `5`, Stable Constitutional Integration.

The final review requires:

- durable lawful authority and accepted constitutional representation
- Security Stability at least `70` for a sustained period
- Unionist Consent or route-valid peaceful compliance above the settlement floor
- Nationalist Consent satisfied or peacefully represented
- Labour Cooperation at least organised
- Integration Capacity at least `70`
- functioning police, courts, finance, services, transport, industry, and local government
- protected education, religion, language, property, pension, and minority rights
- no active mass expulsion, persecution, foreign occupation, or major armed resistance
- settled debt, guarantee, withdrawal, demobilisation, and emergency-law review

Coercive routes require stronger compliance, rights, resistance, finance, and time conditions. Deliberately absurd routes do not bypass human integration.

# Route-specific Northern strategies

## De Valera Northern strategy

- public constitutional claim
- cross-border contact and wartime bargaining
- 1940 proposal decision
- preference for negotiated or deferred unity
- covert defence liaison can support an all-island emergency
- failure through rhetorical claim without preparation or emergency overreach

## Lemass Northern strategy

- functional economic integration
- trade, electricity, transport, industry, and postwar development
- federal or negotiated unitary options after material preparation
- risk that development postpones rights and constitutional settlement indefinitely

## Fine Gael Northern strategy

- legal negotiation, rights, British settlement, and coalition review
- Costello can support a formal republic alongside negotiated Northern policy
- Mulcahy's Civil War and military history affect security talks
- Dillon requires a Northern policy or lawful deferment before war entry

## Norton Labour Northern strategy

- labour, housing, welfare, civil rights, and municipal cooperation
- federal social commonwealth or durable cross-border settlement
- respects northern labour autonomy
- risk of southern union division and sectarian backlash

## IRA civil Northern strategy

- republican claim joined to civil guarantees, northern mandate, and armed subordination
- can negotiate, support nationalist organisation, or enter a constitutional crisis
- failure through local-command violence and dual authority

## IRA command Northern strategy

- border campaign, uprising support, or direct war
- low Unionist Consent and high British reaction by default
- local nationalist support is not automatic
- occupation and command fragmentation are central risks

## Congress plural Northern strategy

- cross-community labour and civil-rights programme
- federal or social commonwealth settlement
- union and committee autonomy
- armed-wing subordination required

## Congress vanguard Northern strategy

- class and national liberation under a central directorate
- compulsory nationalisation and security integration
- strong risk of unionist, nationalist, labour, Church, and foreign resistance

## O'Duffy Northern strategy

- corporate all-Ireland order, military bargain, or Axis-backed coercion
- cannot treat unionists as natural allies or northern nationalists as automatic followers
- estate and personal rule increase resistance and British intervention risk

## Clerical guardianship Northern strategy

- Church and service networks, humanitarian cooperation, and moral guarantee
- must preserve Protestant and minority rights
- clerical veto or confessional compulsion destroys Unionist Consent

## Ailtirí Northern strategy

- reconquest, one-party assimilation, coercive language policy, antisemitism, and party security
- route has very low consent and high occupation burden
- Axis support can raise British war risk and client dependence
- post-Axis settlement crisis is severe

## Constitutional High King

- crown convention can offer a symbolic common head under law
- northern assent and British settlement remain required
- crown household cannot substitute for local government

## Sacral High King

- deliberate absurd route can claim ancient sovereignty
- human rights, public administration, supply, and integration remain active
- coercive sacral command creates captive territories rather than cores

## Five Provinces Northern strategy

- federalism and regional mandates are the strongest natural Northern interface
- historical Ulster must be constructed through consent and local institutions
- four provinces and an empty chair is a valid stable conclusion
- hidden pentarchy requires the same human integration plus concealed gates

## Otherworld compact Northern strategy

- sites and passages on both sides of the border require joint stewardship or strict containment
- foreign access and public knowledge create new Northern disputes
- compact law cannot erase unionist, nationalist, labour, British, or human rights questions

# Northern conclusion families

| Conclusion | Required state | Meaningful end-state |
| --- | --- | --- |
| Managed Partition | rights, cooperation, low security, valid review | durable deferment with active cross-border institutions |
| Functional Island | several shared boards and strong civic cooperation | practical integration without sovereign change |
| Federal Ireland | valid federal ratification and functioning transition | common state with protected Northern autonomy |
| Negotiated United Republic | high consent, British settlement, deep integration | unitary republic with regional safeguards |
| Labour Commonwealth | social and labour mandate, rights, industrial settlement | all-island social state with northern autonomy or strong local government |
| Crowned Union | valid constitutional crown, northern assent, British settlement | crown-in-council all-island order |
| Five Provinces | valid Ulster and other provincial mandates | federal or confederal all-island settlement |
| Military Reunification | war victory and occupation | non-core territory with long resistance and integration gameplay |
| Foreign-Imposed Settlement | sponsor or occupation controls the outcome | client state, bases, dependency, and contested legitimacy |
| Rival Irelands | failed federal, security, or fiscal settlement | renewed partition, competing authorities, or civil conflict |
| Compact of Two Irelands | full hidden gates and human settlement | bounded human and Otherworld constitutional order across the island |

# External expansion and regional orders

## Expansion rule

Ireland receives no generic conquest branch. External ambitions must grow from a completed government, a specific strategic problem, a valid target, National Provision, National Readiness, diplomacy, logistics, foreign reaction, and a postwar settlement.

Every expansion action answers seven questions.

1. what claim or obligation creates the route
2. which government has legal or ideological authority
3. which target states or regions are involved
4. how forces, shipping, supply, intelligence, and access are obtained
5. how local consent and resistance are handled
6. how Britain, the United States, France, Germany, and affected governments react
7. what government and rights system follows success

Cultural contact, mythic memory, and linguistic kinship do not create claims by themselves.

# Serious Celtic cooperation

Classification: `H` contact foundation

The serious cultural lane uses Irish, Scottish Gaelic, Welsh, Manx, Breton, Cornish, and wider Celtic scholarly, language, literary, folklore, labour, religious, maritime, and diaspora links.

## Cooperation families

- language and education exchange
- folklore and archival exchange
- broadcasting and publishing
- university and technical contact
- fisheries and maritime safety
- tourism and transport after the war
- labour and cooperative contact
- diaspora and cultural congresses

This content remains available when every hidden route is closed. It improves Cultural Capacity, diplomacy, regional knowledge, and selected project delivery. It does not grant territorial claims.

# Atlantic small-state compact

Classification: `P`

A credible neutral or postwar Ireland can organise a compact among willing Atlantic or small states.

## Possible compact subjects

- shipping safety and rescue
- weather and civil aviation
- procurement and repair
- food and fuel exchange
- humanitarian and refugee action
- intelligence against piracy, mines, or hostile agents
- postwar reconstruction and trade
- legal consultation on neutrality and sovereignty

## Membership rules

- at least two foreign participants beyond Ireland
- each member accepts a written subject and contribution
- military obligations remain separate from economic or humanitarian membership
- client states cannot provide independent consent without their controlling power's settlement
- members can suspend participation after breach
- leadership rotates or follows a treaty rule

The compact can grow into an Atlantic economic league, a neutral consultation group, or a defensive arrangement. It does not become a faction through one focus.

# Atlantic defence league

Classification: `P`

This late-game route requires a common threat, willing members, Provision at least 65, Readiness at least 75, Coastal and Air Warning plus Maritime Protection, command rules, contribution schedules, and a settlement of British and American relations.

## Shared institutions

- defence council
- maritime and air-warning centre
- joint exercises
- repair and supply arrangements
- common rescue and patrol standards
- intelligence safeguards
- member-confidence and withdrawal rules

Ireland can lead the council, host a secretariat, or remain one equal member. A league that relies wholly on British or American forces becomes a protected order and raises leverage.

# Voluntary Celtic political order

Classification: `P`

A political Celtic order requires independent or constitutionally empowered partners. Scotland, Wales, Brittany, the Isle of Man, Cornwall, and other regions cannot be annexed through cultural affinity.

## Entry conditions

- the target has independent authority, valid self-government, or a campaign-created constitutional opening
- a public movement or government requests negotiation
- Britain or France is absent, consenting, defeated, or part of a settlement
- Ireland has a compatible government and a real economic offer
- membership and exit rules are written
- defence and foreign policy powers are explicit

## Possible forms

- cultural council
- economic and maritime league
- confederation of sovereign governments
- federal order after separate ratifications
- crown association under a valid elected crown
- provincial council linked to Five Provinces

A voluntary order raises obligations. Members require development, defence, representation, and dispute resolution.

# Liberation and protectorate routes

Classification: `P`

A revolutionary, Allied, royal, federal, or authoritarian government can claim to liberate or protect a territory during wider war. The route must identify the local authority and cannot treat occupation as consent.

## Settlement options

- restore an existing government
- create a provisional government with local representatives
- recognise independence
- establish a time-limited protectorate
- admit a consenting member to a league or federation
- return territory through a negotiated settlement
- impose a client regime, with explicit dependency and resistance

## Protectorate rules

A protectorate requires:

- legal instrument or route authority
- local administration
- security and rights policy
- fiscal contribution and development plan
- foreign recognition strategy
- duration and exit rule
- no automatic core status

# Ailtirí reconquest order

Classification: `P` that can grow into `A`

Ailtirí's reconquest doctrine can target Britain and Celtic regions through ideological and historical claims. The route begins as authoritarian expansion and can become deliberately absurd after hidden cultural gates.

## Plausible campaign layer

- exploit a wider British war or collapse
- support selected nationalist or separatist movements
- seek German or other foreign aid
- prepare shipping, air, intelligence, and occupation
- impose party-directed governments
- pursue compulsory cultural and political transformation

The route creates high resistance, foreign war, minority persecution, technical shortages, and sponsor dependence. It cannot receive free compliance from claimed Celtic populations.

## Absurd imperial layer

The hidden layer can claim ancient, legendary, or impossible jurisdictions. Every claim requires the full `A` transition, extreme readiness, route-specific evidence or ideology, and an occupation system. It produces world reaction and does not turn mythology into history.

# High Kingship external order

## Constitutional royal diplomacy

Classification: `P`

A constitutional High King can sponsor cultural congresses, ceremonial alliances, arbitration, or a voluntary crown association. Each partner retains a constitutional ratification process.

## Royal protectorates

Classification: `P`

Protectorates can arise from wartime liberation or treaty. The crown does not hold personal sovereignty without public law, local authority, finance, rights, and exit rules.

## Sacral claims

Classification: `A`

A sacral crown can pursue impossible claims tied to legend, old kingship, or compact law. Human supply, command, resistance, diplomacy, and postwar government remain active. Captive or coercive crowns create a Royal Command State failure.

# Five Provinces external order

## Federal example route

Classification: `P`

A successful Five Provinces federation can offer technical advice, equalisation, autonomy models, and confederal membership to willing partners. It gains diplomatic appeal and carries a risk of veto and overextension.

## Provincial foreign contacts

Provinces can conduct cultural and economic contact within common law. Separate military guarantees, ports, or foreign patrons require federal approval. Rival provincial diplomacy raises Federal Cohesion pressure.

## Pentarchic order

Classification: `A`

The hidden pentarchy can attempt to organise external regions into symbolic courts or provinces after full concealed gates. Local authority, consent, and ordinary administration remain required. A symbolic map does not create control.

# Otherworld external ambitions

Classification: `A`

## Stewardship and containment

A stewardship route cooperates with foreign governments to protect sites, witnesses, and passages. It requires secrecy rules, public-law limits, foreign access records, and compact consent.

## Compact diplomacy

A stable compact can create bounded relations among human and exceptional authorities. Foreign states can observe, negotiate, seek access, exploit, or reject the system. Compact Trust and Veil Stability react to each agreement.

## Dominion

Otherworld Dominion uses passages or exceptional actors for coercive expansion. It creates severe obligation, resistance, public-knowledge, containment, and human-authority failures. No passage carries unlimited supply or armies.

# External-war aftermath

Every external war route has an aftermath branch.

## Mandatory aftermath questions

- ceasefire and treaty
- prisoners and missing persons
- occupation and local government
- claims, borders, and cores
- demobilisation
- veterans and disabled personnel
- shipping and reconstruction
- debt and foreign aid
- resistance and security
- rights and citizenship
- foreign bases and withdrawal
- alliance or neutrality transformation

A war goal without aftermath is incomplete.

# Support-branch convergence

Politics, economy, defence, diplomacy, Northern policy, culture, and hidden systems interact through convergence gates. A player can complete support branches in different orders, though route commitments change cost and availability.

## Early convergence

### `Sovereignty Requires Supply` working convergence

Requires the 1938 settlement, a material survey, and a port-defence inventory. It opens National Provision and links economic projects to readiness.

### `Government Under Pressure` working convergence

Requires a valid government and a National Settlement review. It defines who can authorise emergency allocation, mobilisation, foreign liaison, and Northern policy.

## Middle convergence

### `The Emergency State` working convergence

Requires the European war or equivalent crisis. It opens the Neutrality Ledger, Emergency supply architecture, mobilisation, coast watching, intelligence, censorship, and incident handling.

### `An Island in the Atlantic` working convergence

Links shipping, ports, weather, rescue, diaspora, British and American diplomacy, and coastal and air warning.

### `The Northern Question Becomes Immediate` working convergence

Requires a wartime proposal, security crisis, British collapse, federal convention, plebiscite mandate, or route-specific armed escalation. It opens the active Northern Settlement phases.

## Late convergence

### `The War Has Changed the State` working convergence

Combines Provision, Readiness, emergency law, social consent, veterans, industry, foreign obligations, and political authority. It opens postwar reconstruction and constitutional review.

### `Settlement of the Island` working convergence

Requires a Northern conclusion or durable deferment, security review, and foreign settlement.

### `Ireland's Place in the New Order` working convergence

Requires a postwar foreign policy, defence doctrine, economic model, and country identity. It is the main late-game capstone family.

# Postwar reconstruction

## Demobilisation

Demobilisation is a staged system.

1. release or retain emergency formations
2. return labour and transport to civilian use
3. dispose of or maintain equipment
4. settle veterans, disability, pensions, and training
5. convert barracks, depots, airfields, factories, and shipping
6. review internment, censorship, and emergency law
7. integrate or dissolve route-specific militia, guards, commands, or councils

Rapid demobilisation improves civilian provision and can collapse readiness or public order. Slow demobilisation preserves capacity and prolongs coercion and cost.

## Control expiry

Rationing, price control, import licensing, tillage, fuel allocation, censorship, internment, labour direction, and emergency procurement expire or transform separately. The end of war does not remove them all on one date.

## Reconstruction priorities

- housing and municipal repair
- railways, roads, ports, and rolling stock
- electricity and rural-grid preparation
- peat, fuel, and industrial conversion
- merchant shipping and civil aviation
- schools, health, training, and employment
- regional development and Gaeltacht services
- Northern reconstruction where relevant
- export and trade reorientation

## Postwar social settlement

The player chooses among:

- conservative fiscal recovery
- Lemass-style developmental acceleration
- Labour welfare and public works
- agrarian and regional equalisation
- cooperative and social ownership
- constitutional vocational partnership
- corporate or clerical continuity
- revolutionary command continuation
- federal provincial reconstruction
- royal public works
- compact stewardship obligations

# Late-game government conclusions

Every conclusion resolves eight fields.

1. governing authority
2. constitutional and emergency law
3. economic order and Provision conclusion
4. defence order and Readiness conclusion
5. foreign policy and dependency
6. Northern Ireland status
7. internal reconciliation, coercion, or resistance
8. visible country identity

# Constitutional conclusions

## De Valera late-game conclusion

### Sovereign Neutral Republic

Classification: `H` aligned

- elected constitutional government
- emergency powers reviewed and reduced
- active neutrality preserved
- Provision resilient or better
- Readiness at armed-neutrality level
- Northern claim managed through negotiation or deferment
- covert Allied cooperation remains bounded and recorded
- country identity reflects sovereign republican continuity

### Benevolent Atlantic Neutrality

Classification: `P`

- public neutrality with deep but lawful Allied and American cooperation
- strong shipping, weather, intelligence, and rescue
- dependency below client pressure
- postwar Atlantic access without permanent foreign command

### Permanent Emergency Republic

Failure

- executive authority remains dominant
- censorship and security powers fail to expire
- material delivery can remain competent
- Social Consent, Dáil Mandate, and National Settlement legitimacy erode

## Lemass late-game conclusion

### Developmental Republic

- lawful succession and technical government
- strategic industry, transport, power, and regional programmes
- balanced foreign sourcing
- professional defence and postwar trade
- Northern policy through functional integration or negotiated settlement

### Atlantic Development State

- American and British technical access
- civil aviation, shipping, export, and investment orientation
- sovereignty safeguards intact
- risk of uneven regional growth and external dependence remains managed

### Imported Modernisation

Failure or compromised conclusion

- high output built on leverage, imported management, and weak domestic skills
- foreign interruption can collapse Provision

## Fine Gael late-game conclusion

### Institutional Republic

- parliamentary law, audited boards, professional defence, controlled emergency powers
- solvent reconstruction and protected property
- negotiated or deferred Northern settlement

### Coalition Republic

- Costello or another valid coalition Taoiseach
- party leader and government leader can differ
- social, agrarian, Labour, and Fine Gael programmes are recorded
- instability remains an active political cost

### Security Conservatism

Failure or coercive drift

- anti-IRA and emergency institutions dominate
- professional state survives while consent and civil liberties weaken

## Dillon

### Allied Belligerent Republic

- every political and material war gate passed
- home defence protected
- Irish command and postwar withdrawal safeguarded
- Northern policy settled or lawfully deferred
- dependency below client order

### Deep Cooperation Short of War

- intervention mandate remains below formal threshold or material gates fail
- intelligence, shipping, weather, procurement, and planning deepen
- Neutrality Integrity is redefined and reviewed

### Protected Allied Dependency

Failure

- bases, command, finance, or foreign policy fall under external control
- Irish war participation exists without a sovereign settlement

## Norton Labour late-game conclusion

### Social Democratic Republic

- parliamentary Labour or coalition government
- unions, municipalities, cooperatives, welfare, and public works
- democratic neutrality or lawful Allied cooperation
- citizen defence
- Northern labour and civil-rights policy

### Labour Commonwealth of Ireland

- valid all-island social settlement
- northern labour autonomy and rights
- public industrial and welfare integration

### Movement Fragmentation

Failure

- Labour and National Labour conflict, union division, and emergency coercion prevent delivery

## Clann na Talmhan influence

### Regional Smallholder Settlement

- Clann remains a party or coalition partner after its dated formation
- Agrarian Cohesion high
- regional equalisation, rural infrastructure, credit, processing, and power
- no false conversion into a generic national ruling ideology

### Fragmented Agrarian Protest

Failure

- regional and class conflict defeats the programme

## Constitutional vocationalism

### Vocational Republic

- councils remain advisory or bargaining bodies under elected law
- labour freedom and minority safeguards protected
- producer coordination supports Provision

### Emergency Producer Commission

- wartime powers are effective and dated
- return mechanism exists

### Compulsory Estate or Clerical Veto State

Failure or Part 3 authoritarian conclusion

- representation becomes coercive and emergency authority persists

# Revolutionary conclusions

## IRA civil late-game conclusion

### Civil Republican State

- civil authority commands the armed wing
- audited economy and public law
- foreign contacts regularised
- partition resolved by negotiation, war, or durable policy
- National Settlement review succeeds

### Cooperative Republican Commonwealth

- county and cooperative institutions dominate within a national legal order
- provision is resilient and local command is subordinated

### Armed Dual Republic

Failure

- civil authority and commands maintain parallel finance, depots, courts, and foreign contacts

## IRA command late-game conclusion

### Integrated Republican War State

- command and local compliance high
- Provision and Readiness support sustained defence
- foreign sponsor does not control strategy
- Northern campaign or settlement reaches a defined conclusion

### GHQ Directorate

- central military authority survives with low civil legitimacy
- succession and demobilisation remain unresolved

### Fragmented Commands or Foreign Client

Failure

- national state breaks into local commands or sponsor control

## Congress plural late-game conclusion

### Plural Workers' Commonwealth

- common programme, unions, committees, agrarian actors, and civilian defence remain balanced
- social economy and rights survive the Emergency
- Northern route uses Labour Cooperation and cross-community civic work

### Cooperative Social Republic

- decentralised public and cooperative order
- slower military concentration and high local legitimacy

### Committee Paralysis

Failure

- no institution can allocate national supply or command defence

## Congress vanguard late-game conclusion

### Revolutionary Directorate

- central command economy and military order
- high coercion, surveillance, and political exclusion
- capable state only if Provision and Administrative Reach are real

### Foreign Revolutionary Client

Failure or compromised conclusion

- sponsor directs trade, security, and war policy

### Plural or Constitutional Restoration

- directorate yields to congress, unions, and public ratification

# Authoritarian conclusions

## O'Duffy late-game conclusion

### Corporate State

- estates, army, executive, and sponsor relations stabilised
- labour freedom and opposition remain restricted
- material efficiency depends on real delivery and is not presumed

### Military Corporate Directorate

- army displaces personal leadership and governs through estates

### Personal Guard State

Failure

- party militia and patronage dominate the economy and security

### Foreign Corporate Client

Failure

- sponsor dependence determines foreign and domestic policy

## Clerical guardianship late-game conclusion

### Social Partnership Guardianship

- service networks operate under public law and a dated guardianship
- minorities and labour retain enforceable rights

### Clerical Veto State

Failure

- Church-aligned bodies control policy without public accountability

### Service Collapse and Constitutional Recovery

- state administration resumes after institutional overload or public revolt

## Ailtirí late-game conclusion

### Total Gaelic State

- one-party rule, coercive language policy, antisemitism, political repression, and social exclusion remain explicit
- material capacity depends on forced mobilisation, selective trade, and party control
- Northern and external reconquest create occupation burdens

### Post-Axis Isolation State

- regime survives sponsor defeat with severe technical and diplomatic shortage

### Party Succession Collapse

Failure

- 1945 split, sponsor defeat, exposure, and low administrative reach destroy the regime

# Royal, provincial, and Otherworld conclusions

## Constitutional High Kingdom

### Parliamentary High Kingdom

- elected government, bounded crown, public civil list, professional defence, and lawful succession
- Northern and external crown associations require consent

### Crown and Five Provinces

- every provincial mandate, finance, rights, common command, and crown power is ratified

### Captive Throne

Failure

- household, army, Church, foreign patron, or compact controls the crown

## Sacral High Kingdom

### High Kingdom of the Living Land

Classification: `A`

- human law and public assent bind sacral obligations
- ordinary Provision and Readiness remain functional
- compact or provincial obligations stay within capacity

### Royal Command State

Failure

- sacral claim becomes coercive warlord rule

## Five Provinces late-game conclusion

### Federal Republic of the Five Provinces

- valid provincial mandates, common fiscal and defence authority, rights, and Northern settlement

### Irish Confederation

- limited common authority and strong provincial sovereignty
- foreign and defence obligations remain workable

### Four Provinces and an Empty Chair

- stable deferment of Ulster status without fabrication

### Rival Irelands

Failure

- fiscal veto, guard rivalry, or boundary conflict breaks the federation

## Otherworld compact late-game conclusion

### Stewardship Republic

- human law protects sites and persons
- Compact Trust and Veil Stability remain healthy
- obligations fit National Provision

### Compact of Two Irelands

- bounded joint courts and public authority
- passage and foreign-access rules defined

### Sealed State

- containment succeeds at a high economic and cultural cost

### Otherworld Dominion

Failure or hostile conclusion

- human sovereignty and rights collapse under exceptional rule or exploitation

# Three-spirit lifecycle

The complete overhaul stays within three persistent focus-created route spirits. Ordinary timed modifiers, state modifiers, laws, decisions, missions, and event states do not count as additional route spirits.

## Spirit slot 1: Governing Order

Inherited from Parts 2 and 3. It represents the constitutional, revolutionary, corporate, clerical, party, royal, provincial, or compact governing settlement.

Examples of final forms:

- Constitutional Stewardship
- Developmental Government
- Coalition Legalism
- Parliamentary Labour Settlement
- Civil Republican Authority
- Army Council Command
- Common Programme Authority
- Corporate Estate Order
- Clerical Guardianship
- Total Gaelic Vanguard
- Crown in Council
- Federal Common Authority
- Human Stewardship

Each route upgrades, corrupts, replaces, or removes one governing form. It does not stack several government ideas.

## Spirit slot 2: Organised Society

This spirit represents the mature relationship among labour, rural organisations, churches and service networks, cultural institutions, provincial bodies, economic coordination, and local participation. It carries the social settlement through which projects, rationing, reconstruction, Northern integration, and regional development are delivered. It does not turn every factory, board, project, or shortage into a permanent national spirit.

Possible final forms include:

- Protected Rural Settlement
- Developmental Social Partnership
- Audited Producer Compact
- Parliamentary Social Provision
- Agrarian Cooperative Network
- Republican Reconstruction Boards
- Cooperative Commonwealth
- Mobilised Command Society
- Corporate Estates
- Guardianship Service Network
- Total Gaelic Mobilisation
- Crown Charter Society
- Federal Provincial Compact
- Human Stewardship Networks

Provision projects, labour agreements, rural settlements, Church service arrangements, cultural institutions, provincial compacts, and Northern integration work upgrade or condition this one family. They can corrupt it into Patronage Distribution, Emergency Shortage Order, Captured Estates, Sectarian Administration, Forced Mobilisation, or Broken Public Services. Those forms replace one another. They do not stack as separate permanent ideas.

## Spirit slot 3: Security and External Position

This spirit combines the mature defence order, neutrality or alliance doctrine, intelligence settlement, foreign-dependency state, occupation status, and any valid federal or compact security arrangement.

Possible forms include:

- Armed Neutrality
- Emergency Neutral Defence
- Allied Cooperation Under Irish Command
- Allied Belligerent Republic
- Protected Dependency
- Republican War State
- Citizen Defence Commonwealth
- Corporate Military Order
- Party Army
- Crown and General Staff
- Federal Defence Compact
- Human and Compact Defence

Neutrality incidents, foreign obligations, coastwatch sectors, Northern transition, temporary occupation, mobilisation, and wartime access use variables, laws, decisions, missions, state modifiers, and timed ideas. They may transform this family when a durable strategic order is reached. They do not create a fourth persistent route spirit.

# Route-specific AI statecraft

## AI profile structure

Each government receives a statecraft profile containing:

- Provision priorities
- Readiness target
- neutrality doctrine
- foreign partner preferences and dependency ceiling
- Northern settlement preference
- willingness to use coercion
- expansion validity
- postwar demobilisation policy
- emergency-law expiry policy

Historical AI stays within documented or conservative plausible paths unless campaign conditions open a named divergence. Hidden and absurd routes remain unavailable without their complete reveal and route conditions.

## Constitutional AI profiles

| Route | Provision priority | Readiness target | Foreign policy | Northern policy | Main avoidance rule |
| --- | --- | ---: | --- | --- | --- |
| de Valera historical | food, shipping, fuel, emergency supply | 35 to 50 | benevolent neutrality with bounded Allied liaison | deferment, 1940 bargain only under historical trigger | avoids formal war and exposed level 4 cooperation |
| Lemass | power, transport, industry, regional delivery | 45 to 60 | balanced British and American technical access | functional integration, later negotiation | avoids one-sponsor dependency and premature war |
| Fine Gael | fiscal delivery, trade, professional procurement | 45 to 60 | lawful British and Allied cooperation | legal settlement or deferment | avoids corporate or fascist drift |
| Dillon | shipping, equipment, mobility, home defence | at least 45 before war, seeks 60 | public Allied alignment | policy or lawful deferment required | never enters war below fixed political and material gates |
| Norton | food, housing, transport, public works | 35 to 55 | democratic neutrality or controlled Allied cooperation | labour and civic settlement | avoids revolutionary transition without bridge conditions |
| Clann influence | food, roads, rural power, processing | 30 to 45 | cautious trade diversification | cross-border rural and local cooperation | avoids early national-party behaviour and heavy overseas war |

## Radical AI profiles

| Route | Provision method | Defence method | Foreign preference | Northern preference | Collapse response |
| --- | --- | --- | --- | --- | --- |
| IRA civil | county boards and public procurement | integrated civil command | balanced recognition and diaspora, cautious liaison | civil guarantees, negotiation or prepared war | seeks civil restoration or coalition before fragmentation |
| IRA command | requisition and command districts | GHQ and local commands | German or opportunistic supply when valid | coercive campaign | centralises, then fragments if compliance fails |
| Congress plural | public, cooperative, union compact | citizen defence | anti-fascist non-alignment and labour contacts | labour commonwealth or federalism | calls congress and restores plural mandate |
| Congress vanguard | central directorate | compulsory force | available socialist or anti-fascist sponsor | revolutionary integration | purges or retreats based on capacity and resistance |

## Authoritarian AI profiles

| Route | Provision method | Defence method | Foreign preference | Northern preference | Hard validity rule |
| --- | --- | --- | --- | --- | --- |
| O'Duffy | compulsory estates and patron contracts | army, veterans, paramilitary bargain | Axis if viable, otherwise opportunistic patron | corporate or coercive settlement | route requires severe crisis and real organisation |
| clerical | service networks and vocational mediation | lawful army plus civil services | Vatican humanitarian and Western practical | rights-guaranteed federal or deferred settlement | avoids direct military command by Vatican or Church institutions |
| Ailtirí | coercive autarky and party direction | party army and ideological conscription | German alignment while viable | reconquest and assimilation | no public route before June 1942 and no hidden AI without gates |

## Hidden AI profiles

- constitutional High King AI protects public law, civil list limits, and negotiated Northern settlement
- sacral High King AI acts only after complete `A` reveal and accepts high obligation costs
- Five Provinces AI prioritises mandates, equalisation, federal command, and an empty chair when Ulster consent is absent
- Otherworld stewardship AI prioritises Veil Stability, Compact Trust, obligations, and containment
- Otherworld dominion AI is rare, campaign-state dependent, and does not ignore supply or human resistance
- convergence AI requires every component route to remain valid and never forces a hidden merger after disqualification

## AI material safeguards

AI must not:

- start a major project without inputs and delivery capacity
- mobilise beyond the sustainable readiness ceiling without invasion or route emergency
- enter Dillon's war route below the fixed gate
- accept foreign access above its dependency ceiling without a crisis reason
- pursue Northern war without supply and occupation plans
- grant cores at occupation
- form a league without members
- select a target that lacks the required political opening
- continue obsolete emergency controls after its chosen expiry review without a route reason
- reveal hidden cultural content through ordinary historical AI

# Event architecture reserved for Part 5

Events are continuous across the Part 4 systems. Part 5 owns exact event ids, chains, options, timing, localisation direction, effects, and cleanup.

## Economic event families

- aftermath of the 1938 trade settlement
- port handover inventories and defence discoveries
- harvest, livestock, fertiliser, seed, and tillage disputes
- rationing, price control, queues, smuggling, and black markets
- peat labour, machinery, weather, and transport
- electricity maintenance and rural surveys
- industrial licensing, state-company management, technical failure, and labour conflict
- rail coal shortage, rolling-stock wear, road fuel crisis, and depot bottlenecks
- Irish Shipping formation, charter, purchase, crew, route, loss, rescue, repair, and replacement
- housing, public works, and regional grievance
- postwar conversion, demobilisation employment, and control expiry

## Defence event families

- army expansion and equipment shortage
- reserve and LDF recruitment, training, loyalty, and local service
- Local Security Force and Garda coordination
- Treaty Port batteries, ammunition, staff, and access disputes
- Coast Watching Service daily life, observation, rescue, weather, false report, and security exposure
- Air Defence Command development
- Air Corps procurement, pilots, maintenance, forced landing, and accident
- Marine Service patrol, mine, rescue, and harbour incidents
- G2, Special Branch, foreign agent, IRA, and liaison cases
- Plan W planning and command disputes
- continuity of government and invasion preparations

## Neutrality event families

- declaration and public doctrine
- belligerent aircraft and ships
- internment and escape
- bombing and civilian casualties, including North Strand
- intelligence and weather cooperation
- British pressure and access requests
- American diplomatic pressure and David Gray
- German agents and contacts
- rescue, burial, hospital, and humanitarian action
- censorship, press, rumour, and public challenge
- level 3 and level 4 cooperation exposure
- doctrine review, alignment, or crisis

## Northern event families

- Stormont, unionist, nationalist, labour, local-government, and British reactions
- conscription debate
- Belfast Blitz and southern fire or medical assistance
- industrial production, labour, housing, and air-defence strain
- 1940 unity proposal
- federal and plebiscite campaigns
- border violence, refugees, policing, and arms
- transition-authority formation
- police, court, debt, pension, education, religious, language, and industrial settlements
- resistance, disarmament, guarantees, and core reviews
- postwar constitutional conference

## Expansion and late-game event families

- Celtic congresses and cultural exchange
- small-state and Atlantic conferences
- league membership and refusal
- wartime liberation and protectorate disputes
- foreign occupation and withdrawal
- republic declaration or alternative external-relations settlement
- postwar alliance or neutral leadership
- Ailtirí reconquest and Axis collapse
- royal and provincial recognition
- Otherworld foreign access, stewardship, containment, and dominion reaction

## Flavour requirement

Each major project, service, region, and route needs recurring flavour that explains lived consequences and changes gameplay. Topics include coastwatch shifts, turf cutting, rail overcrowding, ration substitutions, ship crews, harbour workers, LDF training, air-raid response, Gaeltacht communications, border families, Belfast housing, union meetings, provincial budget disputes, royal obligations, and compact stewardship.

Flavour choices must affect a visible value, regional state, stakeholder, relationship, idea stage, mission, or later event. They are not decorative popups.

# Decision and mission architecture reserved for Part 5

Part 5 will build active families from the following Part 4 systems.

## Provision families

- county tillage and agricultural delivery
- fertiliser, seed, machinery, storage, and milling
- peat and fuel production
- electricity, transmission, and regional service
- industrial licensing and conversion
- railway, road, bridge, depot, port, and housing projects
- shipping acquisition, routing, repair, crew, rescue, and replacement
- rationing, price control, allocation, enforcement, and black-market response
- postwar reconstruction and control expiry

## Readiness families

- officer and staff reform
- reserve training and mobilisation rehearsal
- LSF and LDF regional missions
- equipment procurement and standardisation
- Treaty Port defence packages
- coastwatch sector maintenance
- air warning, anti-air, airfield, and Air Corps missions
- Marine Service patrol and rescue
- intelligence, counter-agent, and liaison missions
- operational-plan exercises and validation

## Neutrality families

- doctrine review
- incident response
- internment and escape prevention
- airspace and maritime enforcement
- weather, rescue, and intelligence cooperation
- foreign access and obligation negotiation
- exposure containment
- public legitimacy and censorship review
- war-entry or retreat-from-commitment mission

## Northern families

- political, labour, civic, Church, business, and local-government contact
- cross-border functional boards
- 1940 bargain
- federal convention
- plebiscite preparation
- ceasefire and disarmament
- transition authority
- police, courts, debt, pensions, industry, housing, education, and rights integration
- resistance and security
- foreign guarantee and withdrawal
- core review

## Expansion and order families

- cultural and Atlantic conferences
- member recruitment and contribution
- liberation and provisional government
- protectorate administration
- foreign base withdrawal
- league cohesion and common defence
- royal, provincial, and compact obligations
- postwar treaty and country-identity settlement

# Asset architecture reserved for Part 6

Part 4 identifies asset families and source rules. Part 6 will produce the full ledger and prompts.

## Sourced historical needs

- Irish regular army, LDF, LSF, Air Corps, Marine Service, coastwatch, G2, Garda, and civil-defence material
- Treaty Port batteries and harbour facilities
- Irish Shipping vessels and crews
- railways, peat, ESB, agriculture, rationing, ports, and public works
- Belfast shipbuilding, aircraft, linen, labour, Blitz, housing, Stormont, and local government
- real political, military, labour, business, Church, and administrative figures
- historical flags, seals, documents, maps, and attested symbols

## Generated needs

- fictional alternate-history scenes
- hidden-route report and news images
- fictional flags, emblems, councils, and symbolic leaders
- High Kingship, Five Provinces, and Otherworld interfaces
- route-state panels and exceptional incident art

## Icon families

- Provision components and stages
- Readiness components and stages
- Neutrality Integrity, incident, access, internment, exposure, and partner-cooperation domains
- Northern values, regions, settlement process, integration stages, and domains
- economy, defence, diplomacy, expansion, and late-game focus icons
- route-specific idea and conclusion icons
- achievement hooks

# Achievement hooks reserved for Part 6

Part 4 creates tracking hooks for difficult mastery outcomes.

- maintain credible neutrality through repeated high-severity incidents while avoiding undeclared co-belligerency at partner depth `4`
- enter the Allied war through Dillon after every political and material gate
- complete rural and industrial development without any leverage reaching client pressure
- sustain an Irish merchant service through wartime loss and rescue
- reach integrated national defence without collapsing Provision
- negotiate a valid all-Ireland federal settlement with high Security Stability
- achieve unitary unity through consent and deep integration
- win a coercive Northern war and complete the long rights and integration review without atrocities or foreign client status
- form an Atlantic league with real members and contributions
- complete a constitutional crown and Northern settlement
- form Five Provinces with a valid Ulster mandate
- complete a stable Compact of Two Irelands with obligations inside capacity
- survive Ailtirí's post-Axis crisis while retaining the authoritarian route, marked as a rare and severe outcome
- restore constitutional government after a command, corporate, clerical, or party failure

Part 6 will define exact working keys, descriptions, disqualifiers, visibility, difficulty, tracking, and icon direction.

# Cross-system acceptance criteria

1. National Provision uses four components, opens at `38`, and applies the fixed single and dual bottleneck caps.
2. National Readiness uses seven components, opens at `15`, and applies the fixed equipment, mobility, command, warning, maritime, intelligence, and Provision gates.
3. Neutrality uses one visible `Neutrality Integrity` value, normal September 1939 opening `72`, five bands, incident history, source-specific leverage, and partner-specific cooperation depths `0` to `4`.
4. Every foreign bargain records obligations, command limits, withdrawal terms, and sovereignty safeguards.
5. The Northern Settlement Ledger keeps Unionist Consent, Nationalist Consent, Labour Cooperation, British Flexibility, Security Stability, and Integration Capacity separate.
6. No settlement family grants Northern territory, compliance, administration, or cores through a focus reward.
7. Every government family receives a material economy, defence order, neutrality or alignment policy, Northern policy, and late-game conclusion.
8. Hidden routes retain ordinary human supply, command, rights, diplomacy, occupation, and integration burdens.
9. Serious cultural capacity improves delivery only through institutions, staff, archives, language services, and regional networks.
10. Support branches converge through capability gates and do not become isolated reward columns.
11. Every external order requires real partners or explicit conquest, authority, logistics, foreign reaction, and aftermath.
12. The complete package stays within the three persistent route spirits: Governing Order, Organised Society, and Security and External Position.
13. Events remain continuous across projects, incidents, organisations, regions, crises, wars, settlements, and conclusions.
14. Part 5 receives enough fixed architecture to implement decisions, missions, events, and lifecycles without redesigning Part 4.

# Part 5 interface ledger

| Part 4 system or state | Part 5 receives | Part 5 must implement | Part 5 cannot change silently |
| --- | --- | --- | --- |
| National Provision | range `0` to `100`, opening `38`, Food `55`, Energy `25`, Transport `40`, Maritime `30`, bands, bottleneck caps, regional delivery, project and failure architecture | exact variables, rounded mean, dynamic projects, costs, success, partial success, failure, maintenance, shocks, cleanup, tooltips, events, idea transformations | component count, openings, arithmetic mean, bottleneck caps, or delivery rule |
| National Readiness | range `0` to `100`, opening `15`, seven component openings, bands, bottlenecks, Overextension, mobilisation layers, operational plans, and route gates | exact calculations, training, procurement, mobilisation, LDF, coastwatch, warning, ports, air, maritime, intelligence, plan missions, losses, recovery, demobilisation, cleanup | component count, openings, fixed gates, Dillon gate, or rule that manpower and imported equipment alone do not create readiness |
| Neutrality Integrity | range `0` to `100`, normal September 1939 opening `72`, five bands, partner-specific cooperation depths `0` to `4`, policy domains, incident severity, source leverage, obligations, exposure, and derived pressure | incident chains, doctrine decisions, internment, access, intelligence, weather, rescue, shipping, trade, censorship, exposure, war entry, restoration, foreign reactions, cleanup | opening, bands, level meanings, source separation, or one-visible-value architecture |
| foreign obligation system | source-specific leverage, obligation record, sovereignty safeguards, dependency indicators, access and delivery | negotiation, delivery, breach, exposure, withdrawal, sponsor collapse, postwar revision | source-specific leverage or no-free-aid rule |
| Northern Settlement Ledger | Unionist `5`, Nationalist `40`, Labour `30`, British `10`, Security `45`, Integration `10`, separate thresholds, regions, seven-step process, integration stages, transition domains, occupation states, rights and core tests | actor events, confidence measures, conferences, plebiscites, war, transition authority, policing, industry, services, finance, guarantees, resistance, integration, cleanup | opening values, separate-value rule, exact federal, unitary, labour, plebiscite, wartime, and coercive thresholds, or no-free-territory rule |
| economy route states | final authority, ownership, capital source, labour settlement, rural settlement, regional pattern, project portfolio, derived industrial output | route decision categories, project variants, laws, idea stages, advisors, leaders, stakeholders, failure and recovery | coercion costs, foreign dependency, or ordinary material limits |
| defence route states | command owner, force model, procurement, foreign liaison, mobilisation method, failure, and conclusion for every route | command lifecycles, unit and equipment missions, operational-plan events, laws, idea stages, AI, cleanup | civil-command distinctions, armed-wing autonomy, component gates, or no-free-capacity rule |
| emergency overlays | legal allocation, negotiated compact, command requisition, foreign dependency, war damage and recovery | rationing, requisition, damage, reconstruction, review, expiry and cleanup | temporary nature, material cost, or route transformation risk |
| shipping and port states | merchant capacity, crews, routes, losses, repairs, rescue, markings, harbour packages, access doctrine | tonnage and port decisions, convoy and rescue missions, loss events, replacement, foreign access, cleanup | neutral shipping immunity, ownership as capability, or unrecorded access |
| coastwatch and air defence | `83` historical posts grouped into six operational sectors, coverage, staffing, communication, recognition, weather, rescue, warning and response | sector missions, forced landing chains, procurement, maintenance, incidents, events | free warning or a static national bonus |
| intelligence and censorship | G2, Garda, ordinary policing, censorship, coastwatch, foreign liaison, Northern work, legal division, exposure and civil-liberty pressure | agents, liaison, counter-intelligence, domestic cases, censorship, review, events, cleanup | institutional collapse into one generic security service |
| expansion and regional orders | serious Celtic contact, Atlantic structures, voluntary political order, liberation, protectorate, authoritarian conquest, royal, provincial and Otherworld routes | invitations, refusal, ratification, contributions, cohesion, war, occupation, resistance, dissolution, aftermath, identity | cultural links as claims, empty factions, or protectorates without exit rules |
| postwar settlement | staged demobilisation, control expiry, reconstruction, republic and external-relations settlement, defence, alignment and Northern review | missions, events, law expiry, veterans, industry, identity, flags, cosmetic transitions, foreign reactions | all controls expiring together or republic status as a free focus |
| three-spirit ceiling | Governing Order, Organised Society, Security and External Position | exact idea ids, upgrades, replacements, corruption, failure, mergers, removals, tooltips, icons, cleanup | a fourth persistent focus-created route spirit or dead idea stacks |
| route conclusions | government, law, economy, defence, foreign policy, Northern status, emergency authority, internal settlement and identity | completion and failure chains, idea, law, leader, advisor, party, flag, cosmetic, claim, core, guarantee and cleanup lifecycles | a focus, flag, leader, cosmetic name, claim, or military control alone proving completion |
| Part 4 event architecture | economic, defence, neutrality, Northern, expansion, postwar, foreign-reaction and flavour families | full event maps with continuous route and regional flavour, meaningful choices, noticeable effects, images and text direction | optional events or decorative flavour |
