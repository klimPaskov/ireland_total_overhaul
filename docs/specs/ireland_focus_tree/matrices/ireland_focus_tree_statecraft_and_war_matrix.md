# Ireland Focus Tree Statecraft and War Matrix

Feature slug: `ireland_focus_tree`

Part: 4 of 7

Document role: cross-surface acceptance ledger for economy, defence, neutrality, diplomacy, Northern Ireland, expansion, late game, and the Part 5 handoff. All structural names are working labels unless they are historical proper names.

# Classification and fidelity matrix

| Surface | `H` requirement | `P` permission | `A` permission | Rejection condition |
| --- | --- | --- | --- | --- |
| economy | real dependence, policy, industry, transport, shortages, and institutions remain recognisable | acceleration, different ownership, or alternate planning grows from real capacity | impossible obligations can alter selected outcomes | political victory creates goods, factories, fuel, or ships without delivery |
| defence | small army, equipment weakness, Emergency mobilisation, coastwatch, ports, Air Corps, Marine Service, G2, and LDF anchor the system | stronger reform, procurement, war entry, and Northern operations require capacity | royal, provincial, and Otherworld forces still use command and supply | focus or flag grants modern armed force |
| neutrality | legal neutrality, broad support, active enforcement, covert cooperation, internment, rescue, intelligence, and trade remain central | deeper cooperation, belligerency, Axis opportunism, or recovery follows explicit gates | impossible governments still face foreign access and public policy | neutrality is one focus or a passive modifier |
| Northern Ireland | institutions, communities, industry, labour, security, British authority, and consent remain separate | federation, plebiscite, unitary settlement, or coercive reunification has full process | hidden systems may add crown, provincial, or site obligations | territory or cores are free rewards |
| regional order | cultural and diplomatic contacts precede institutions | consenting Atlantic, Celtic, neutral, reconstruction, or defence structures | impossible order requires extreme route and material capacity | generic claims or annexations lack local authority |
| postwar | emergency expiry, demobilisation, reconstruction, republic status, UN, trade, and alignment require action | alternate constitutional or ideological order is fully developed | hidden regimes still resolve ordinary governance | route ends with a cosmetic name and no statecraft conclusion |

# Fixed inherited constants

| Item | Value | Acceptance test |
| --- | --- | --- |
| National Settlement range | `-100` to `+100` | no Part 4 file changes it |
| opening Settlement value | `+25` | preserved in all opening references |
| opening Momentum | `-1` | preserved |
| Momentum range | `-5` to `+5` | preserved |
| monthly movement | `2` per point, maximum `10` | preserved |
| boundary confirmation | `7` days | preserved |
| return margin | `5` points | preserved |
| route commitment | preserve, clamp `-60` to `+60`, relabel, clean contributors, six-month review | every route conclusion consumes current state |
| Social Consent | opening `55` | never replaced by Provision or Northern consent |
| National Readiness | opening `15` | decomposed through the fixed seven components |
| British Leverage | opening `45` | remains source-specific |
| Vatican Leverage | opening `25` | remains separate from domestic Church influence |
| American Leverage | opening `5` | remains source-specific |
| German Leverage | opening `5` | remains source-specific |

# National Provision constants

| Item | Fixed value | Meaning | Validation |
| --- | --- | --- | --- |
| Food Security opening | `55` | output, inputs, storage, prices, distribution | all files agree |
| Energy Continuity opening | `25` | coal, oil, turf, peat, electricity, allocation | all files agree |
| Transport Serviceability opening | `40` | rail, road, rolling stock, depots, maintenance | all files agree |
| Maritime Access opening | `30` | tonnage, crews, ports, charters, routes | all files agree |
| displayed opening Provision | `38` | rounded mean | arithmetic correct |
| severe bottleneck | any component below `20` caps Provision at `35` | prevents compensation by unrelated strength | mapped in spec and economy map |
| dual bottleneck | two components below `30` cap Provision at `45` | models broad scarcity | mapped in spec and economy map |
| zero component | begins national emergency | systemic failure | Part 5 must create event and mission response |

## Provision bands

| Range | State | Mandatory gameplay |
| --- | --- | --- |
| `0` to `19` | systemic breakdown | essential-service failures, emergency allocation, consent and readiness loss |
| `20` to `34` | acute scarcity | rationing, stoppages, black market, regional inequality, leverage |
| `35` to `49` | strained provision | limited shock absorption and constrained major projects |
| `50` to `64` | managed supply | reliable ordinary projects and mobilisation support |
| `65` to `79` | resilient provision | sustained mobilisation or reconstruction |
| `80` to `100` | strategic capacity | ambitious regional or war programmes with continued costs |

# Economic lane acceptance matrix

| Lane | Required focus groups | Required projects or missions | Required tradeoff | Required failure | Route conclusion link |
| --- | --- | --- | --- | --- | --- |
| agrarian recovery | rural survey, price settlement, inputs, machinery, tillage, storage, fisheries | county input delivery, tillage compliance, storage, milling, fisheries | producers versus consumers, livestock versus food, coercion versus compliance | poor yields, producer capture, county revolt, distribution failure | food and rural settlement |
| protected industry | census, licensing, consumer goods, materials, state capital, training, tariff review, war conversion | factory and workshop projects, skill missions, import replacement | price and efficiency, patronage, foreign retaliation | stagnation, machine trap, labour flight, consumer crisis | protected or corporate economy |
| developmental industry | power, technical labour, industrial sites, export standards | portfolio delivery and regional sites | capital, leverage, urban concentration, rural displacement | dependent or uneven modernisation | developmental conclusion |
| emergency supply | import priorities, rationing, prices, stocks, allocation, enforcement | dynamic shortage responses by good and region | fairness, coercion, black market, stakeholder burden | distribution collapse, corruption, consent crisis | wartime survival and emergency expiry |
| energy and peat | surveys, emergency turf, bog works, generation, transmission, storage | fuel campaigns, drainage, machinery, grid and storage projects | labour, weather, land, foreign machinery | wet turf, grid bottleneck, urban fuel riot, import dependency | Energy Continuity and reconstruction |
| transport and depots | rail, road, bridge, bus, port, depot, regional access | named route repair, rolling stock, loading and depot missions | civilian versus military priority, regional equity versus efficiency | coal stoppage, congestion, route failure, sabotage | Provision, mobility, Northern integration |
| merchant shipping | markings, purchase, charter, Irish Shipping, crews, routes, rescue, loss replacement | tonnage tiers, route missions, port repair, rescue and investigation | capital and crew loss, foreign pressure, escort dependency | blockade, sinking cascade, seizure, port loss | neutral lifeline or aligned supply |
| housing and works | municipal, rural, sanitation, training, regional workshops, demobilisation | named local projects | materials versus defence, patronage versus need | abandoned works, local capture, urban unrest | consent and reconstruction |
| regional development | western, border, Gaeltacht, island, provincial, and Northern interfaces | regional project portfolios | cost versus territorial equality | persistent imbalance, provincial resentment | route legitimacy and integration capacity |

# Route economic transformation matrix

| Route | Project authority | Labour form | Rural form | Foreign capital rule | Corruption or coercion risk | Final form |
| --- | --- | --- | --- | --- | --- | --- |
| de Valera | cabinet and state boards | regulated bargaining | producer settlement | diversified and guarded | party patronage and slow delivery | sovereign protected economy |
| Lemass | developmental cabinet and technical boards | training and productivity bargain | processing and transition | selective, standards and anti-dependency clauses | technocratic capture and uneven growth | developmental republic |
| Fine Gael | legal boards and coalition ministries | conventional bargaining | cooperative credit | reviewed private and state finance | coalition delay and elite capture | accountable mixed economy |
| Dillon | war cabinet under Dáil mandate | wartime bargain | Allied supply contracts | extensive Allied access with safeguards | dependency and neutrality backlash | co-belligerent supply state |
| Norton | parliament, public boards, municipalities | union participation and rights | labour and consumer safeguards | balanced reconstruction finance | coalition and affiliate fracture | democratic social economy |
| IRA civil | civil republican directorate | republican unions and public boards | land commission and committees | balanced, recognition dependent | dual authority and expropriation dispute | civil republican reconstruction |
| IRA command | GHQ and military districts | military allocation | requisition | sponsor and clandestine | local corruption, evasion, client status | command economy |
| Congress plural | common programme and committees | union and worker control | cooperative and agrarian compact | labour and anti-colonial partners | committee delay and coalition fracture | plural workers' economy |
| Congress vanguard | central directorate | compulsory labour direction | compulsory delivery | ideological sponsor | purges and resistance | directed socialist state |
| O'Duffy | leader and compulsory estates | restricted corporate membership | agricultural corporations | foreign patrons and contracts | oligarchic capture and forced membership | estate economy |
| clerical | guardianship or producer commission | mediated vocation | parish and producer networks | humanitarian and selected capital | Service Dependency and veto | guardianship or producer economy |
| Ailtirí | party state | compulsory national service | autarkic settlement | Axis or isolated | exclusion, antisemitism, surveillance, false autarky | total state economy |
| High King | crown in council or household | chartered associations | crown land commission | treaty and charter | household capture and obligation abuse | crown economy |
| Five Provinces | provincial and federal boards | provincial settlements | provincial programmes | multiple partners under federal rules | veto, unequal capacity, foreign penetration | federal economy |
| Otherworld | human institutions plus compact bodies | human labour with obligations | site and seasonal compact | exceptional and ordinary channels | compact breach and public fear | compact, containment, or dominion economy |

# National Readiness constants

| Component | Opening | Required content |
| --- | --- | --- |
| Command and Training | `25` | command districts, staff work, exercises, civil control, signals |
| Equipment Sufficiency | `8` | inventory, standards, repair, domestic production, procurement |
| Mobilisation Depth | `20` | regulars, cadres, LSF, LDF, replacements, demobilisation |
| Supply and Mobility | `12` | depots, rail, roads, trucks, fuel, medical, engineering |
| Coastal and Air Warning | `5` | posts, observers, communications, recognition, weather, Air Corps liaison |
| Maritime Protection | `5` | Marine Service, harbours, batteries, mines, rescue, shipping liaison |
| Intelligence Coordination | `30` | G2, Garda, censorship, liaison, agents, Northern and weather intelligence |
| opening Readiness | `15` | exact rounded mean |

## Readiness bands and gates

| Range or threshold | Capability | Additional requirements |
| --- | --- | --- |
| `0` to `14` | nominal sovereignty | no coordinated defence claim |
| `15` to `29` | improvised defence | opening state |
| `30` | stable armed neutrality floor | Provision, warning, port and law requirements |
| `35` | wartime Northern bargain floor | ledger and British conditions |
| `45` | credible national defence and Dillon Readiness floor | fixed Part 2 conditions plus National Provision `50` with no component below `30`, Maritime Access `40`, Transport Serviceability `40`, Equipment Sufficiency `40`, Command and Training `40`, Supply and Mobility `40`, protected home-defence reserve, defined military contribution, and enforceable safeguards |
| `50` | normal constitutional voluntary war-entry floor | consent, supermajority, Provision, Northern policy |
| `55` | independent offensive planning | command, equipment, mobility and legitimacy |
| `60` | sustained Northern campaign | mobility `45`, Provision `55`, occupation plan |
| `65` | expeditionary intervention | shipping and replacement capacity |
| `75` | credible regional defence league | members, contributions, common threat |
| `85` | impossible multi-front ambition | extreme route gates and Provision `70` |

## Readiness bottlenecks

| Condition | Effect | Required Part 5 response |
| --- | --- | --- |
| Equipment below `15` | Readiness cap `35` | procurement, repair, standardisation, force reduction |
| Supply and Mobility below `20` | Readiness cap `45` | named route, depot, fuel, truck, rail missions |
| Command below `25` | no sustained offensive | exercises, appointments, civil-control crisis |
| Intelligence below `25` | penetration and plan compromise | agent and liaison chains |
| Warning below `20` | no credible armed-neutrality conclusion | sector post and communications missions |
| Maritime Protection below `20` | no secure port conclusion | harbour and Marine Service programme |
| Provision below `35` | prolonged mobilisation cap | demobilise, ration, import, or coerce with consequences |

# Defence lane matrix

| Lane | Required early work | Required active objectives | Required late payoff | Failure state |
| --- | --- | --- | --- | --- |
| command and training | command review, authority law, staff school | exercises, signals, regional plans | lawful integrated command | dual command, officer revolt, political army |
| equipment and repair | inventory and standards | workshop output, procurement, ammunition and spare routes | sustainable force standard | incompatible stocks or sponsor dependence |
| mobilisation | registers and cadres | LSF, LDF, coastwatch, replacement and training | general or sustained mobilisation | unarmed mass or politicised local force |
| supply and mobility | route surveys | depots, rail loading, bridges, fuel, medical | operational endurance | stranded units and provision collapse |
| coastwatch and warning | posts and recruitment | sector coverage, recognition, communication, weather, rescue | integrated picture | blind sector, false report, compromise |
| harbour and maritime | inventory transferred works | batteries, mines, Marine Service, repair, inspection | secure ports or controlled access | foreign seizure, unusable port, mine crisis |
| air defence | observation and civil warning | airfields, fuel, training, AA, searchlights | national air defence or rare expedition | aircraft and fuel dependency |
| intelligence | G2, Garda, legal authority | agents, liaison, censorship, Northern and weather work | protected plans and bargaining | repression, penetration, scandal |
| operational planning | plan selection and authority | unit placement, supply test, exercise, communications | valid war or neutrality plan | bottleneck exposure and AI reprioritisation |

# Neutrality Integrity constants

| Item | Fixed design | Validation |
| --- | --- | --- |
| range | `0` to `100` | all files agree |
| normal September 1939 opening | `72` before route and law adjustments | Part 5 implements adjustment helper |
| credible armed neutrality | `80` to `100` | requires material enforcement |
| practised neutrality | `60` to `79` | normal historical space |
| selective neutrality | `40` to `59` | uneven enforcement and leverage visible |
| compromised neutrality | `20` to `39` | dependency or covert war crisis |
| breakdown | `0` to `19` | forced choice, restoration, or intervention |

# Neutrality incident acceptance matrix

| Family | Mandatory variables and states | Minimum choices | Required visible effects | Failure escalation |
| --- | --- | --- | --- | --- |
| airspace | warning, Air Corps, crew, aircraft, origin, intent, law | intercept, protest, intern, release, conceal, cooperate | Integrity, leverage, equipment or intelligence | repeated violation, bombing, foreign access scandal |
| shipping | route, vessel tier, cargo, crew, threat, port | rescue, investigate, protest, reroute, escort choice, restrict | Maritime Access, losses, Provision, diplomacy | blockade, sinking cascade, crew crisis |
| internment | nationality, camp, law, escape, treatment | equal rules, parole, exchange, prosecution, discreet tolerance | Integrity, camp cost, intelligence, consent | escape scandal, unequal treatment, foreign retaliation |
| intelligence | agent identity, sponsor, exposure, domestic contact | watch, turn, intern, expel, prosecute, protect | Intelligence, Security Loyalty, leverage, route cohesion | network growth, false arrest, sponsor retaliation |
| weather | station, report type, operation, public safety | public, equal, controlled Allied, restrict, deceive | rescue, aviation, Integrity, liaison | exposed bias, accident, compact breach |
| trade | named good, supplier, route, stocks, sponsor demand | ration, diversify, bargain, concede, borrow | Provision components, leverage, consent | dependency, shortage, black market |
| access | facility, duration, command, force, withdrawal rule | refuse, time-limit, Irish command, share, foreign command | Readiness, Integrity, leverage, sovereignty safeguard | occupation or access dependency |
| censorship | target information, law, duration, review | narrow, broaden, publish, investigate, suppress | consent, cabinet, National Settlement, intelligence | permanent emergency, scandal, opposition radicalisation |
| border | named corridor, refugees, smuggling, forces, Northern actor | close, regulate, cooperate, permit, deploy | Northern ledger, supply, Integrity, leverage | communal violence, British incursion, route overload |

# Diplomacy and dependency matrix

| Partner | Main benefits | Main costs | Dependency warning | Route-specific crisis |
| --- | --- | --- | --- | --- |
| Britain | trade, coal, equipment, Plan W, shipping, recognition, Northern flexibility | access, leverage, policy pressure, Commonwealth and port questions | exclusive supply plus command or irreversible access | British ultimatum, exposed liaison, Northern guarantee conflict |
| United States | procurement, credit, diaspora, shipping, reconstruction, UN support | access pressure, neutrality criticism, economic leverage | debt, market, base, or recognition control | Aiken mission failure, diaspora split, access dispute |
| Germany | agents, anti-British leverage, arms promise, ideology, recognition | exposure, blockade, faction conflict, client status | sponsor controls regime or security | failed delivery, captured agent, Axis defeat |
| Vatican | recognition, humanitarian channels, moral and anti-communist support | external ecclesiastical influence and regime scrutiny | guardianship relies on diplomatic protection | minority, authoritarian, antisemitic, or mythic criticism |
| neutral and small states | diversification, legal consultation, shipping and reconstruction | low hard power and coordination cost | forum cannot replace supply or defence | member defection and major-power pressure |
| diaspora | lobbying, relief, investment, remittances, recognition | divided agendas and foreign domestic politics | government depends on one organisation or patron | neutrality, partition, labour, fascism, or violence split |

A dependency conclusion requires three or more of the fixed dependency indicators in the Part 4 specification.

# Northern Settlement Ledger constants

| Value | Opening | Acceptance rule |
| --- | --- | --- |
| Unionist Consent | `5` | never inferred from British agreement alone |
| Nationalist Consent | `40` | never inferred from Dublin claim alone |
| Labour Cooperation | `30` | never treated as automatic class unity |
| British Flexibility | `10` | moves through war, bargaining, politics, guarantees, and leverage |
| Security Stability | `45` | separate from consent and military control |
| Integration Capacity | `10` | requires services, finance, administration, transport, and law |

# Northern settlement threshold matrix

| Model | Unionist | Nationalist | Labour | British | Security | Integration | Additional gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lawful deferment | none fixed | public mandate for policy | optional | none | no active collapse | none | explicit law and review |
| functional cooperation | target-specific | target-specific | target-specific | target-specific | usually `45` | usually `20` | named joint body and competence |
| wartime bargain | `20` or enforceable guarantees | `50` | context | `45` | context | context | Readiness `35` and defined defence scope |
| plebiscite | campaign result, not opening threshold | campaign result | context | `55` | `60` | `30` preferred | supervision, registers, district rules, no occupation |
| federal | `45` | `60` | `45` | `50` | `55` | `40` | powers, finance, rights, policing and ratification |
| negotiated unitary | `60` | `65` | `50` | `60` | `65` | `55` | new constitution and local safeguards |
| labour social | `35` | `55` | `65` | `45` | `55` preferred | `40` | union freedom and industrial programme |
| coercive | consent not required for invasion | route legitimacy still matters | not required | may be hostile | occupation begins unstable | occupation begins low | Readiness `60`, mobility `45`, Provision `55`, occupation plan |

## Federal settlement threshold

Unionist Consent `45`, Nationalist Consent `60`, Labour Cooperation `45`, British Flexibility `50`, Security Stability `55`, and Integration Capacity `40`, plus powers, finance, rights, policing, and ratification.

## Negotiated unitary settlement threshold

Unionist Consent `60`, Nationalist Consent `65`, Labour Cooperation `50`, British Flexibility `60`, Security Stability `65`, and Integration Capacity `55`, plus a new constitution, local safeguards, and accepted withdrawal terms.

## Coercive reunification threshold

National Readiness `60`, Supply and Mobility `45`, National Provision `55`, valid cause and command, a Belfast and occupation plan, and long resistance, rights, finance, and integration gameplay.

# Northern process and integration acceptance

| Stage | Mandatory surfaces | Invalid shortcut |
| --- | --- | --- |
| claim and contact | legal policy, diplomatic channels, local actors | claim grants compliance |
| confidence measures | prisoners, policing, propaganda, trade, services, incidents | one opinion event completes trust |
| proposal mandate | Dáil, cabinet, movement, crown, province, or compact authority | focus provides mandate |
| Northern representation | unionist, nationalist, labour, local and institutional delegates | Dublin selects all representatives |
| British settlement | sovereignty, finance, defence, guarantees, recognition | Britain ignored or auto-accepts |
| ratification | election, plebiscite, convention, or route-valid consent | control substitutes for public consent |
| implementation | administration, security, services, debt, industry, rights | cosmetic tag or ownership completes unity |

## Integration stages

| Stage | Required proof | Core status |
| --- | --- | --- |
| 0 claim only | policy and diplomacy | impossible |
| 1 functional bodies | at least one functioning joint competence | impossible |
| 2 provisional settlement | recognised authority, timetable, guarantees | impossible |
| 3 shared administration | selected services, finance, policing, infrastructure | impossible |
| 4 integrated administration | common standards, budgets, institutions, coordinated security | still not automatic |
| 5 stable constitutional integration | durable consent, rights, services, no major resistance, settled guarantee | eligible after final test |

# Northern post-settlement matrix

| Surface | Must define | Success measure | Failure |
| --- | --- | --- | --- |
| Stormont or successor | executive, legislature, powers, confidence, review | stable valid government | institutional vacuum or imposed shell |
| local government | boundaries, finance, representation, services | legitimate functioning councils | gerrymander, boycott, service collapse |
| policing | command, recruitment, oversight, vetting, law | ordinary civil policing accepted across communities | sectarian force, purge, military policing |
| security | paramilitary disarmament, British withdrawal, army role | no major armed control outside law | insurgency, reprisals, foreign intervention |
| industry | ownership, contracts, fuel, labour, market, damage | sustained output with workforce participation | requisition collapse, capital flight, sabotage |
| labour | unions, bargaining, wages, discrimination | cross-community cooperation survives disputes | union split, employer lockout, political purge |
| welfare and housing | benefit continuity, finance, construction | comparable service access | regional collapse and migration |
| education and religion | school control, funding, safeguards | Minority Confidence and stable access | forced assimilation or denominational crisis |
| language and culture | voluntary rights, institutions, service | accepted framework | coercive language conflict |
| debt and finance | pensions, liabilities, tax, transfers, guarantees | stable budget and clear obligations | insolvency or external financial control |
| military | bases, personnel, equipment, command, pensions | loyal integrated or devolved structure | mutiny, duplicate command, foreign occupation |
| guarantees | monitor, duration, withdrawal and review | guarantee normalised or resolved | permanent foreign veto |

# Expansion and regional order matrix

| Structure | Class | Required members or territory rule | Material gate | Political gate | Failure |
| --- | --- | --- | --- | --- | --- |
| Celtic Cultural Congress | `H` to `P` | organisations and consenting partners | cultural capacity and travel or broadcasting | no sovereignty claim required | empty symbolism or domination |
| Atlantic Small-State Forum | `P` | at least two sovereign partners | Maritime Access `50` preferred | diplomatic preparation | major-power pressure and weak delivery |
| Atlantic Neutrality Compact | `P` | compatible neutral states | Integrity `65`, Readiness `40` preferred | common legal rules | member belligerency or defection |
| Celtic Reconstruction Council | `P` | consenting postwar governments | Provision `55` and finance plan | reconstruction treaty | unequal burden and foreign opposition |
| Irish-led Defence League | `P` | credible members and contributions | Readiness `75`, Provision `65` | common threat and ratification | empty guarantee and dependency |
| anti-colonial support network | `P` | recognised movements or states | shipping, training, finance | route legitimacy and foreign reaction | proxy conflict and overreach |
| High Kingship of Western Isles | `A` | consent, valid authority, or explicit conquest | Provision `70`, Readiness `75` or route-specific higher gate | Royal Legitimacy and cultural preparation | rebellion, succession, foreign war |
| Five Provinces Beyond Ireland | `A` | local mandates required for federal form | Provision `70`, federal logistics | Federal Cohesion and valid provinces | occupation and federal fracture |
| Atlantic Threshold Compact | `A` | valid human and Otherworld partners | Provision `70`, Readiness `65`, stable sites | Veil Stability and Compact Trust | Veil collapse and resistance |

# Postwar and conclusion acceptance matrix

| Route | Emergency authority | Economy resolution | Defence resolution | Alignment | Northern direction | Identity resolution | Failure alternative |
| --- | --- | --- | --- | --- | --- | --- | --- |
| de Valera | expire or review | managed protected economy | armed neutrality | neutral or discreet Western | defer, cooperate, negotiate | republic or external relation settled | permanent emergency |
| Lemass | technical emergency bodies normalised | development portfolios | integrated small-state defence | balanced Western and European | functional to federal or unity | developmental republic | dependent or uneven modernisation |
| Fine Gael | parliamentary restoration | accountable mixed economy | professional constitutional force | British agreement or non-aligned | lawful settlement | coalition republic | coalition or command crisis |
| Dillon | war cabinet reviewed | Allied supply to reconstruction | defined military contribution and demobilisation | Allied or Atlantic | settle or defer lawfully | co-belligerent republic | dependency |
| Norton | civil-liberty review | social economy and housing | citizen defence | democratic neutral or cooperative | labour settlement | social republic or coalition state | movement fracture |
| IRA civil | civil authority established | republican reconstruction | Army Council subordinated or integrated | balanced, aligned, or neutral | convention or legitimate war | civil republic | dual authority or failed state |
| IRA command | military law reviewed or entrenched | command economy | GHQ state | patron or isolation | coercive campaign | Army Council republic | fragmentation or client state |
| Congress plural | committee law constitutionalised | cooperative public economy | armed wing subordinated | labour, anti-colonial, non-aligned | social federation | plural workers' republic | coalition collapse |
| Congress vanguard | directorate entrenched | directed economy | central revolutionary force | ideological sponsor or isolation | imposed settlement | vanguard state | resistance and succession |
| O'Duffy | personal emergency entrenched or estate succession | corporate economy | personal and corporate security | Axis, Vatican, or isolation | corporate or coercive | corporate state | Axis defeat and collapse |
| clerical | guardianship returns authority or persists | service or producer economy | lawful force and service mobilisation | Vatican and neutral | safeguarded settlement | constitutional guardianship or veto state | captured council |
| Ailtirí | party emergency permanent | coercive autarky | ideological army | Axis or isolation | reconquest | total Gaelic state | underground or collapse |
| High King | crown emergency bounded by law or geis | charter economy | guard plus national force | crown diplomacy | autonomous, federal, or conquest | constitutional or sacral crown | empty crown or household capture |
| Five Provinces | federal emergency apportioned | equalisation and provincial economies | federal staff and guards | federal and Celtic | federal Ulster | federation or confederation | provincial fracture |
| Otherworld | compact or containment law | obligation-sensitive provision | human and site defence | compact diplomacy | human and site settlement | compact, containment, dominion | breach or restored stewardship |
| full convergence | all emergency systems reconciled | high-capacity federal crown compact | integrated obligation-bound defence | rare regional order | deepest valid settlement | convergence identity | cascading multi-system failure |

# Three-spirit lifecycle acceptance

The three persistent families are Governing Order, Organised Society, and Security and External Position.

| Family | Allowed Part 4 transformations | Prohibited outcome |
| --- | --- | --- |
| governing order | project authority, emergency form, reconstruction, federal, crown, revolutionary, corporate, or compact conclusion | separate permanent idea for every board and project |
| organised society | labour, rural, Church, cultural, provincial, corporate, republican, integration, resistance, or compact form | overlapping permanent labour, rural, Church, and culture stacks |
| security and external position | armed neutrality, alliance, dependency, occupation, federal defence, intelligence, compact security | fourth permanent route spirit for Readiness or neutrality |

Temporary shortages, mobilisation, projects, foreign missions, occupations, and integration stages must expire, transform, or clean up.

# AI acceptance matrix

| AI requirement | Historical profile | Alternate profile | Invalidation rule |
| --- | --- | --- | --- |
| provision | solve worst component, prioritise 1941 shipping and coal crisis | follow route ownership and distribution | no project without inputs and capacity |
| readiness | coastwatch, local defence, supply, modest procurement | pursue route force and capability gates | no offensive plan below required components |
| neutrality | maintain Integrity, discreet Allied bias, avoid formal war | follow valid alignment route | hidden or marginal route cannot select invalid stance |
| foreign leverage | diversify and protect sovereignty | accept route sponsor with dependency awareness | dead sponsor or inaccessible route weight zero |
| Northern | defer, cooperate, avoid reckless war | pursue route threshold and capacity | settlement unavailable when any mandatory actor or threshold missing |
| expansion | low historical priority | pursue only valid regional or hidden order | no independent members, consent, capacity, or route gate means zero weight |
| postwar | demobilise, review emergency, reconstruct | complete route conclusion | conclusion unavailable until government, law, economy, defence, Northern, and identity are resolved |

# Part 5 reservation matrix

| Part 4 design | Part 5 must create | Part 5 must not invent or change |
| --- | --- | --- |
| National Provision | decision header, component updates, projects, shocks, dynamic costs, failure and cleanup | components, opening values, bottlenecks, bands |
| economic lanes | categories, missions, event chains, law and idea stages, regional targets | route institutions and payoff logic |
| National Readiness | component display, procurement, training, mobilisation, plans, incidents | components, opening values, gates, bottlenecks |
| active neutrality | incident pools, choices, timers, foreign reactions, restoration | Integrity opening, bands, stance architecture |
| source leverage | partner-specific events, agreements, access, debt, dependency lifecycle | merging partners into one meter |
| Northern Ledger | actor events, targeted decisions, local missions, negotiations, war and integration | six opening values, settlement thresholds, process, integration stages |
| expansion | treaty, recognition, membership, contribution, war and integration chains | classifications and capacity gates |
| postwar | emergency expiry, demobilisation, republic, UN, aid, party and office lifecycles | route conclusion requirements |
| spirits | exact idea forms, upgrades, replacements, corruption and cleanup | three-family ceiling |
| identity | leader, party, law, flag, cosmetic name, claim, core, occupation and conclusion rows | cosmetic change as substitute for political or material result |

# Cross-file consistency tests

| Test | Required result |
| --- | --- |
| Provision arithmetic | `55 + 25 + 40 + 30 = 150`, mean `37.5`, displayed `38` |
| Readiness arithmetic | `25 + 8 + 20 + 12 + 5 + 5 + 30 = 105`, mean `15` |
| Dillon gate | Part 2 conditions remain exact. Part 4 also requires National Provision `50` with no component below `30`, Maritime Access `40`, Transport Serviceability `40`, Equipment Sufficiency `40`, Command and Training `40`, Supply and Mobility `40`, a protected home-defence reserve, a defined military contribution, and enforceable access, command, customs, finance, Northern, withdrawal, and review safeguards. |
| Northern federal threshold | `U45 N60 L45 B50 S55 I40` everywhere |
| Northern unitary threshold | `U60 N65 L50 B60 S65 I55` everywhere |
| Northern labour threshold | `U35 N55 L65 B45`, with security and integration work |
| coercive campaign | Readiness `60`, Supply and Mobility `45`, Provision `55`, occupation plan, no free cores |
| core eligibility | only after integration stage `5` and final rights, service, resistance, policing, and guarantee test |
| armed neutrality | Readiness `30` floor plus Integrity and warning, port, and law conditions |
| three spirits | no fourth persistent focus-created route spirit |
| H/P/A | hidden or impossible content never described as documented history |
| no free capacity | focus completion alone never provides unsupported material output |

# Part 5 interface ledger

This table is the exact stopping point for Part 4. Part 5 must consume these states without redesigning the statecraft architecture.

| Part 4 state | Part 5 receives | Part 5 must implement | Part 5 cannot assume |
| --- | --- | --- | --- |
| National Provision | four components at current values, bottleneck state, active projects, shortages, regional delivery, sponsor and law state | complete decision categories, missions, shocks, dynamic costs, event chains, partial success, failure, maintenance, and cleanup | that the mean alone proves food, fuel, transport, or shipping capacity |
| agrarian system | price doctrine, tillage law, fertiliser and seed access, storage, machinery, fisheries, rural and labour response | county and regional decisions, harvest and input events, compliance missions, idea lifecycle | that acreage equals yield or farmers form one bloc |
| industrial system | ownership model, licences, boards, training, portfolios, factories and workshops delivered | project tiers, construction and production missions, labour and patronage events, law and advisor lifecycles | that protection or nationalisation creates output without energy, skills, inputs, and markets |
| energy system | turf, peat, generation, transmission, storage, fuel imports, regional allocation | seasonal and project missions, weather and machinery events, grid and fuel ideas | that turf, peat, hydro, coal, oil, and electricity are interchangeable |
| transport system | route groups, rolling stock, depots, roads, bridges, ports, fuel allocation | named map missions, repair decisions, route failure, military priority, cleanup | that national control means serviceable transport |
| merchant shipping | tonnage tier, vessel and crew losses, routes, ports, charters, Irish Shipping state | purchase, charter, route, rescue, investigation, loss replacement, family and crew events | that neutral markings guarantee safety or one ship grant solves imports |
| National Readiness | seven components, bottlenecks, mobilisation tier, command law, foreign standards, operational plans | component-linked decisions, missions, exercises, procurement, force growth, incidents, demobilisation | that manpower creates equipped and trained formations |
| coastwatch and warning | six sectors, coverage, training, communications, weather, rescue, exposure | sector missions, incident events, post and service lifecycle, foreign reaction | that 83 posts are 83 passive buttons or ownership means functioning warning |
| harbour and Marine Service | port policy, batteries, mines, patrol, repair, rescue, access and command | harbour projects, port incidents, mine and rescue missions, service ideas and leaders | that port transfer means effective defence or blue-water navy |
| intelligence | G2, Garda, censorship, agents, liaison, weather, Northern portfolio, legal model | agent chains, counter-intelligence missions, exposure, scandals, office and law lifecycles | that high coordination proves legality or loyalty |
| Neutrality Integrity | current value, stance, incident history, access, internment, covert cooperation, public exposure | continuous incident pools, choice consequences, restoration or belligerency chain, cleanup | that neutrality is equal sympathy, isolation, or one focus |
| British relationship | leverage, trade, equipment, Plan W, access, Northern talks, safeguards | agreements, demands, events, aid, corridor, dependency and postwar lifecycle | that British aid is free or British flexibility equals unionist consent |
| American and diaspora relationship | leverage, organisations, procurement, credit, access, recognition and internal divisions | targeted diaspora and US events, investment, lobbying, mission and dependency lifecycle | that diaspora is one bloc or American support guarantees unity |
| German relationship | leverage, contacts, delivery, exposure, sponsor and Axis war state | agent, procurement, ideological, client, defeat and document-exposure chains | that promises arrive or Axis alignment survives defeat unchanged |
| Vatican relationship | leverage, representation, humanitarian, moral, anti-communist and regime state | diplomatic and Church-linked event chains with separate domestic influence | that domestic Church control equals Vatican approval |
| Northern Settlement Ledger | six values, local actor states, proposal, representation, British position, security, integration | negotiations, confidence measures, plebiscite, conventions, war, occupation, services, rights, policing, debt, industry, guarantees | that one consent value, British agreement, or military control completes settlement |
| Northern integration | stage `0` through `5`, administration, policing, industry, labour, welfare, education, language, finance, military, guarantees | full lifecycle, events, decisions, missions, claims, resistance, occupation, core test and cleanup | that state ownership grants cores or stable administration |
| regional order | organisation class, members, contributions, consent, route and capacity gates | membership, refusal, exit, contribution, cohesion, foreign reaction, war and conclusion events | that cultural contact grants sovereignty or faction membership |
| postwar transition | emergency law, demobilisation, Provision, Readiness, debt, reconstruction, recognition, republic and alignment questions | complete event and lifecycle package for laws, ideas, leaders, parties, offices, identities, aid, UN and Northern review | that victory ends emergency systems or cosmetic identity resolves constitutional law |
| route conclusion | final government, economy, defence, alignment, Northern, emergency and identity requirements | route-specific completion chains and flavour events with clear failure and recovery | that any route can conclude while a required surface is unresolved |
| three-spirit architecture | current governing order, organised society, security and external position forms | exact idea upgrades, replacements, mergers, corruption, failure and cleanup | that projects, shortages, occupations, or incidents become permanent extra spirits |
