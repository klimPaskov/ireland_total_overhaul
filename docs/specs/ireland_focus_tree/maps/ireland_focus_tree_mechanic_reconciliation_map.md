# Ireland Focus Tree Mechanic Reconciliation Map

Feature slug: `ireland_focus_tree`

Status: Part 7 canonical mechanic ownership and interface map

All names are working labels. This map does not create new mechanics. It states which source owns each mechanic, what later files may add, and what must never be merged or bypassed.

# Authority order

| Surface | Authoritative source | Supporting sources | Part 7 rule |
| --- | --- | --- | --- |
| historical classification and source notes | `research/ireland_focus_tree_historical_research_notes.md` | every specification part | research informs design. A later gameplay file may define a plausible route but cannot relabel speculation as documented history |
| macro architecture | Part 1 specification and architecture map | later route maps | later parts add detail without replacing the shared opening or cross-branch design |
| National Settlement, elections, parties, constitutional routes, Church domains and vocational constitutionalism | Part 2 specification, National Settlement map, constitutional route map and constitutional matrix | Parts 3 to 6 | exact constants and political lifecycles remain fixed |
| radical, corporate, clerical, cultural, royal, provincial and Otherworld routes | Part 3 specification, two Part 3 route maps and radical matrix | Parts 4 to 6 | later material and lifecycle rules constrain political victory without deleting the route |
| National Provision, National Readiness, neutrality, foreign policy, Northern settlement, expansion and postwar statecraft | Part 4 specification, two Part 4 maps and statecraft matrix | Parts 5 and 6 | Part 4 owns the canonical Dillon gate and all material and Northern thresholds |
| decisions, missions, event volumes, laws, offices, identities, cleanup and standard conclusions | Part 5 specification, decision map, event map and lifecycle matrix | Part 6 | Part 5 owns category counts, mission caps, event floors and the fifteen standard conclusion families |
| AI, foreign reactions, achievements, assets, GUI, animation, text direction and implementation-prompt ownership | Part 6 specification and four Part 6 matrices | Part 7 route and reconciliation maps | exact counts remain fixed |
| source navigation, label normalisation, route coverage, composite convergence and implementation handoff | Part 7 index, route matrix, reconciliation maps and prompts | all six source parts | Part 7 cannot weaken an accepted gate |

# Fixed constant registry

| System | Fixed value |
| --- | --- |
| National Settlement range | `-100` to `+100` |
| National Settlement opening | `+25` |
| opening Settlement Momentum | `-1` |
| Momentum range and monthly movement | `-5` to `+5`, two balance points per momentum point, maximum ten per monthly update |
| stage confirmation and return | seven days beyond a boundary, five-point return margin |
| route commitment | preserve current value, clamp to `-60` through `+60`, relabel poles, remove obsolete contributors, begin six-month review |
| Social Consent opening | `55` |
| National Readiness opening | `15` |
| British, Vatican, American and German Leverage openings | `45`, `25`, `5`, `5` |
| formal and routine Dáil ledgers | `153` formal seats and `152` routine votes |
| Fianna Fáil opening | `77` formal seats and `76` routine votes |
| Fine Gael, Labour and other deputies | `59`, `8`, `9` formal seats |
| National Provision components | Food `55`, Energy `25`, Transport `40`, Maritime `30` |
| displayed National Provision | mean `37.5`, displayed `38` |
| National Readiness components | Command `25`, Equipment `8`, Mobilisation `20`, Supply `12`, Warning `5`, Maritime Protection `5`, Intelligence `30` |
| displayed National Readiness | mean `15` |
| Neutrality Integrity opening | `72` at the normal September 1939 activation |
| Northern Settlement opening | Unionist `5`, Nationalist `40`, Labour `30`, British `10`, Security `45`, Integration `10` |
| persistent route-spirit ceiling | three families |
| decision categories | thirteen |
| global active mission caps | `8` normal, `10` during the Emergency or war, `12` only during simultaneous national emergency and Northern occupation |
| command power ceiling for one action | `60` |
| event programme | eighteen historical chain families, eighteen political crisis families, twelve foreign reaction families, at least 236 flavour events, minimum 484 player-facing events in total |
| AI | exactly 30 durable profiles and exactly ten temporary state overlays |
| foreign reaction window | fourteen days, at most four separate visible reactions before a digest |
| achievements | exactly 32, split 8 Hard, 12 Very Hard, 8 Campaign, 4 Hidden Mastery |
| Northern cores | only after integration stage `5` and final regional review |

# National Settlement

| Element | Reconciled rule |
| --- | --- |
| opening poles | Unfinished Revolutionary Mandate and Constitutional State Authority |
| stages | Revolutionary Command, Armed Dual Authority, Revolutionary Ascendancy, Negotiated Settlement, Constitutional Ascendancy, Executive Consolidation, State Monopoly |
| support inputs | stakeholders, elections, offices, laws, decisions, missions, events, crises, route actions and foreign pressure |
| companion systems | Social Consent, National Readiness and source-specific External Leverage support the balance but never replace it |
| route transformation | the value persists. Pole labels, contributors, stage effects and crises change to match the government |
| failure rule | extreme authority or revolutionary control can be a route state, a crisis, or a failure. The route specification decides which |
| cleanup | obsolete contributors, missions and labels close. History, damage, offices, laws, leverage and disqualifiers remain |

The National Settlement remains a native balance-of-power presentation supported by an evolving decision category. It is not moved into one of the three scripted GUI surfaces.

# Political and institutional ledgers

| Ledger | Reconciled rule |
| --- | --- |
| formal seats | records legal membership of the Dáil |
| routine votes | records ordinary confidence strength after the Ceann Comhairle reserve and support agreements |
| government formation | requires a majority, confidence agreement, or coalition with at least 70 seats under the mapped process |
| offices | party leader, parliamentary leader, Taoiseach, President, cabinet office, military command, security office and movement command remain separate |
| Church domains | education, health, welfare, morality and information, labour and vocation, service dependency, episcopal confidence and Minority Confidence remain separate from Vatican Leverage |
| Labour and unions | parliamentary Labour, National Labour, affiliates, unions, dissidents and Republican Congress actors retain separate history |
| agrarian politics | formal Clann seats, farmer independents, Agrarian Cohesion and the temporary Agrarian Support Bloc remain separate |

# National Provision

National Provision measures civilian and strategic continuity across four components. Political victory does not grant capacity.

| Component | Opening | Main consumers | Main failure effect |
| --- | ---: | --- | --- |
| Food Security | `55` | population, army, towns, industry, Northern transition | rationing, nutrition, unrest, mobilisation ceiling |
| Energy Continuity | `25` | rail, industry, electricity, transport, defence | production and mobility collapse |
| Transport Serviceability | `40` | food distribution, projects, mobilisation, evacuation, Northern administration | regions and forces cannot receive delivered capacity |
| Maritime Access | `30` | imports, fuel, equipment, trade, rescue, diplomacy | external supply and shipping collapse |

The displayed value is the rounded mean. Bottlenecks and regional delivery caps prevent a high average from hiding a collapsed component. Every project has a region, cost, delivery path, success, partial success, failure, maintenance and cleanup state.

# National Readiness

National Readiness measures usable defence capacity across seven components. Manpower alone does not create readiness.

| Component | Opening | Main proof |
| --- | ---: | --- |
| Command and Training | `25` | lawful authority, staff work, officers, exercises, signals, doctrine and continuity |
| Equipment Sufficiency | `8` | weapons, ammunition, vehicles, aircraft, engineering tools, spares and repair |
| Mobilisation Depth | `20` | regulars, reserves, LSF, LDF, coastwatchers, replacement and medical fitness |
| Supply and Mobility | `12` | food, fuel, rail, roads, depots, trucks, medical support and repair |
| Coastal and Air Warning | `5` | six coastwatch sectors, recognition, weather, communications, plotting and response |
| Maritime Protection | `5` | harbour control, batteries, mines, patrol, inspection, rescue and denial |
| Intelligence Coordination | `30` | G2, Garda, censorship, liaison, agent control, Northern intelligence and protected plans |

National Readiness uses the fixed bottlenecks, overextension rules, operational plans and route gates from Part 4. The Coast Watching Service contains 83 historical posts represented through six gameplay sectors.

# Canonical Dillon gate

Formal belligerency through Dillon requires all of the following:

- Intervention Mandate at least `90`
- National Readiness at least `45`
- Social Consent at least `60`
- a Dáil majority
- British Leverage below `60`
- sovereignty safeguards
- a Northern policy or lawful deferment
- no active constitutional crisis
- National Provision at least `50`, with no component below `30`
- Maritime Access at least `40`
- Transport Serviceability at least `40`
- Equipment Sufficiency at least `40`
- Command and Training at least `40`
- Supply and Mobility at least `40`
- a protected home-defence reserve
- a defined military contribution
- enforceable access, command, customs, finance, Northern, withdrawal and review safeguards

No focus, event, foreign request, AI weight or achievement may bypass this gate.

# Active neutrality and foreign relations

| Surface | Reconciled rule |
| --- | --- |
| Neutrality Integrity | one visible value measuring consistency among declaration, territorial control, public law and conduct |
| incident families | airspace, aircraft, shipping, mines, rescue, internment, intelligence, agents, weather, trade, access, censorship, border, refugees and smuggling |
| cooperation depth | tracked by partner and action. Covert Allied cooperation can coexist with public neutrality |
| External Leverage | British, American, German and Vatican tracks remain separate. Other relationships use their own ledgers |
| obligations | every agreement records delivery, access, command, debt, exposure, safeguards, review, withdrawal and dependency |
| war | route-specific political and material proof is required. War does not close home-defence, demobilisation or sovereignty obligations |
| sponsor collapse | future delivery ends. Debt, exposure, local clients and captured material remain |

# Northern Settlement Ledger

| Value | Opening | What it cannot be inferred from |
| --- | ---: | --- |
| Unionist Consent | `5` | British agreement alone |
| Nationalist Consent | `40` | Dublin claims alone |
| Labour Cooperation | `30` | one party or one union alone |
| British Flexibility | `10` | Allied cooperation or public rhetoric alone |
| Security Stability | `45` | military control alone |
| Integration Capacity | `10` | territorial transfer or a focus reward |

The ledger supports lawful deferment, functional cooperation, wartime bargain, federal settlement, negotiated unitary government, labour settlement, plebiscite, coercive war, royal and provincial arrangements, occupation and postwar review. Local government, policing, security, industry, labour, welfare, housing, education, religion, language, debt, taxation, military command, guarantees, resistance and rights remain active after settlement.

Integration stages remain separate from claims and control. Only stage `5` plus the final regional review can grant a core, and failed regions remain non-core until they later pass a valid review.

# Decision and mission architecture

| Surface | Fixed rule |
| --- | --- |
| categories | thirteen evolving categories owned by Part 5 |
| actions | 140 mapped decisions |
| objective families | 54 mapped mission families |
| costs | political, command, XP, manpower, equipment, vehicles, trains, convoys, fuel, factories, leverage, exposure, consent, local support, tied units and time as appropriate |
| Action Burden | `1` to `10` and used by human presentation and AI utility |
| outcomes | every mission has full success, partial success, failure, escalation and cleanup |
| auto-completion | goal missions complete when the condition is met and do not require a second payment |
| cancellation | physical recovery is at most 70 percent. Political, exposure, leverage and reputation costs normally remain |
| critical slots | constitutional collapse, invasion, component collapse, occupation and route review can pre-empt routine work |

# Events and memory

The minimum 484 player-facing events comprise 72 historical and institutional nodes, 42 political and leadership crises, 48 Provision, Readiness and neutrality incidents, 30 foreign reactions, 32 Northern events, 236 route and regional flavour events, and 24 postwar and conclusion events. Hidden bookkeeping, AI-only routing and debug events do not count.

Events are a continuous gameplay layer. Each player-facing event changes a visible value, starts or modifies an objective, changes a temporary state, affects an office or relationship, or records a lasting choice. Event memory supplies achievement and conclusion disqualifiers.

# Persistent spirits, laws and temporary states

| Surface | Fixed rule |
| --- | --- |
| persistent spirit families | Governing Order, Organised Society, Security and External Position |
| ceiling | no route keeps more than these three focus-created persistent spirit families |
| lifecycle | each family has opening, route, success, corruption, failure, recovery and conclusion forms |
| law ladders | seventeen families with entry, review, abuse, replacement and expiry |
| temporary states | projects, shortages, mobilisation, incidents, occupation, integration and reconstruction remain temporary and use cleanup |

# Concealed evidence and cultural capacity

Serious language, archive, folklore, Gaeltacht, regional and site work remains useful in every valid campaign. It cannot grant sovereignty. Concealed routes require the mapped evidence classes, provenance, public capacities, sites, unusual campaign state, no disqualifier, explicit hidden permission where required, and revalidation after major changes.

The classification boundary is:

- `H` for documented organisations, institutions, sites, records and cultural work
- `P` for constitutional restoration, investigation, containment and alternate political use grounded in those materials
- `A` from the first verified impossible claim, sacral obligation, pentarchy or Otherworld sovereignty onward

A false lead removes false evidence and route access while retaining legitimate archives, teachers, roads, museums, local institutions and site protection.

# Conclusion and convergence

The fifteen standard conclusion families use the Part 5 sequence:

1. eligibility review
2. exact blocked-surface report when needed
3. institutional settlement
4. foreign and domestic reactions
5. identity activation
6. 180-day consolidation mission
7. full, partial, blocked or failed result
8. cleanup and persistent memory

The full crown, provincial and Otherworld convergence is a composite super-conclusion. It requires valid component conclusions, stage `5` Northern integration and final review, material and obligation floors, and no captive crown, warlord province, fabricated evidence, exclusion state, broken compact or patron control. It uses the same consolidation standard without changing the count of fifteen standard families.

# Mechanic acceptance tests

1. Every value has one owner and a visible presentation.
2. No companion value replaces the National Settlement.
3. No political route grants free Provision, Readiness, consent, recognition, units, territory, offices, alignment or cores.
4. Foreign leverage and domestic Church influence remain separate.
5. Northern actors and British actors remain separate.
6. Every mission and agreement has cleanup.
7. Every route conclusion resolves all mandatory surfaces.
8. The three-spirit ceiling, category count, mission caps, event floors, AI counts, achievement count and asset counts remain fixed.
