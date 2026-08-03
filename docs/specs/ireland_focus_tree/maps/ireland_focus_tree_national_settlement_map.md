# Ireland Focus Tree National Settlement Map

Feature slug: `ireland_focus_tree`

Part: 2 of 7

Map status: accepted Part 2 mechanic map

Planning status: design only, no implementation code, no final localisation

Every label in this map is a working label unless it is a historical proper name.

Historical classification:

- `[H]` documented history
- `[P]` plausible speculation
- `[A]` deliberate absurdity, reserved for later parts

## Map purpose

This file is the source of truth for the structure, tuning anchors, route transformations, crisis rules, AI targets, and cleanup of `The National Settlement`.

The main Part 2 specification owns the historical explanation and full route design. This map owns the mechanic relationships that must remain consistent across focuses, decisions, missions, events, ideas, leaders, parties, laws, AI, and later route transformations.

## System overview

```text
                           ELECTIONS AND PLEBISCITES
                                      |
                                      v
                           DÁIL SEATS AND MANDATE
                                      |
                                      v
 STAKEHOLDER VALUES ----> THE NATIONAL SETTLEMENT <---- LAWS AND LEADERS
       0 to 100                 -100 to +100                    |
            |                        |                          |
            |                        v                          |
            |               route-specific poles               |
            |                        |                          |
            +------------+-----------+-------------+------------+
                         |                         |
                         v                         v
                  SOCIAL CONSENT           ROUTE AVAILABILITY
                      0 to 100                    |
                         |                         v
                         +----------------> CRISIS MISSIONS

 NATIONAL READINESS and source-specific EXTERNAL LEVERAGE act as feasibility
 and dependency gates. Church relationship domains act as policy states rather
 than replacing the domestic Church stakeholder value.
```

## Presentation map

### Primary surface

Use the native balance-of-power interface.

```text
UNFINISHED REVOLUTIONARY MANDATE  <---- 0 ---->  CONSTITUTIONAL STATE AUTHORITY
              -100                                      +100
```

The bar shows:

- current numeric position
- current seven-stage band
- route-specific pole labels after commitment
- active signed contributors
- next threshold in each direction
- current route-optimal band

### Supporting decision category

Use one evolving decision category.

```text
CURRENT GOVERNMENT
  Taoiseach or caretaker head
  ruling party or coalition
  Dáil seats and majority threshold
  Cabinet Cohesion
  Dáil Mandate

THE NATIONAL SETTLEMENT
  current value
  current band
  current Settlement Momentum
  active temporary contributors
  route-specific pole names
  crisis warning and deadline

COMPANION VALUES
  Social Consent
  National Readiness
  British Leverage
  Vatican Leverage
  American Leverage
  German Leverage

RELEVANT STAKEHOLDERS
  only the values and tiers that matter to the current route, decision, or crisis

ACTIVE CONSTITUTIONAL WORK
  election actions
  government-formation work
  leadership contest
  route decisions
  crisis mission
```

The category hides obsolete actions. It does not become a permanent store of every possible political decision.

### Presentation rejected for normal play

Do not create a bespoke scripted GUI for normal constitutional politics.

Reasons:

- the native balance already communicates direction and thresholds
- seats, contributors, and costs fit the decision category
- a second full interface would duplicate information
- constitutional politics needs clarity over spectacle
- later hidden or broken-settlement content can receive special presentation when justified

## Variable and status ledger

| Working value or status | Range or forms | Persistence | Visibility | Owner |
| --- | --- | --- | --- | --- |
| National Settlement | `-100` to `+100` | full campaign | always visible | Part 2 core |
| Settlement Momentum | `-5` to `+5` | rolling 90-day sources | visible in breakdown | Part 2 core |
| Social Consent | `0` to `100` | full campaign | always visible | shared national value |
| National Readiness | `0` to `100` | full campaign | always visible | shared value, completed in Part 4 |
| British Leverage | `0` to `100` | full campaign | always visible | foreign relationship |
| Vatican Leverage | `0` to `100` | full campaign | always visible | foreign relationship |
| American Leverage | `0` to `100` | full campaign | always visible | foreign relationship |
| German Leverage | `0` to `100` | full campaign | always visible | foreign relationship and later route gate |
| Cabinet Cohesion | `0` to `100` | current cabinet | visible when government exists | government system |
| Dáil Mandate | `0` to `100` | current election and confidence cycle | visible | parliamentary system |
| Administrative Confidence | `0` to `100` | full campaign | shown when relevant | administration |
| Security Loyalty | `0` to `100` | full campaign | shown when relevant | Garda and Defence Forces |
| Republican Network Strength | `0` to `100` | full campaign | shown when relevant | republican challenger system |
| Labour Organisation | `0` to `100` | full campaign | shown when relevant | labour system |
| Church Institutional Influence | `0` to `100` | full campaign | shown when relevant | domestic Church stakeholder |
| Rural Organisational Support | `0` to `100` | full campaign | shown when relevant | rural and local system |
| Minority Confidence | `0` to `100` | full campaign | shown when relevant | constitutional pluralism |
| Dáil seat blocs | integers summing to current chamber size | election cycle | visible | parliamentary system |
| Coalition Cohesion | `0` to `100` | coalition lifetime | visible for coalitions | coalition system |
| party unity profiles | route-specific named states | leadership cycle | visible when relevant | party system |
| Church relationship domains | named policy states | until replaced | visible in Church category | education, welfare, information, vocational policy |
| Crisis Pressure | `0` to `100` | one named crisis | visible during crisis | crisis system |
| coalition promises | finite commitments | government lifetime with election memory | visible | coalition system |
| temporary contributor | signed momentum source with expiry | normally 90 days | visible in breakdown | source action or event |

Only the core balance, three companion systems, and current parliamentary summary are always visible. Stakeholder values appear contextually to avoid interface overload.

## Opening state on 1 January 1936

| Value or status | Opening value | Interpretation |
| --- | ---: | --- |
| National Settlement | `+25` | the state has a functioning constitutional advantage, while partition and revolutionary legitimacy remain unresolved |
| Settlement Momentum | `-1` | the unratified constitutional project and organised republican networks create mild pressure toward the challenger side |
| Social Consent | `55` | the political system has a working majority of acceptance under serious economic and social division |
| National Readiness | `15` | routine order exists, while modern defence and strategic supply remain weak |
| British Leverage | `45` | trade, geography, Commonwealth residue, security, ports, and Northern Ireland create high influence |
| Vatican Leverage | `25` | diplomatic and transnational religious authority matter without controlling the Irish state or hierarchy |
| American Leverage | `5` | diaspora and diplomatic potential exist before major wartime engagement |
| German Leverage | `5` | diplomatic presence and possible clandestine contact exist without broad material access |
| Cabinet Cohesion | `65` | Fianna Fáil is experienced and disciplined with real policy and succession differences |
| Dáil Mandate | `55` | government is strong and still lacks the intended new constitutional mandate |
| Administrative Confidence | `70` | ordinary civil administration functions reliably |
| Security Loyalty | `65` | Garda and Defence Forces obey the state while Civil War memory remains politically relevant |
| Republican Network Strength | `35` | militant republicanism is organised and dangerous without mass electoral power |
| Labour Organisation | `35` | Labour and unions can affect confidence, wages, arbitration, and public order |
| Church Institutional Influence | `65` | Catholic institutions possess extensive educational, service, associational, and moral authority |
| Rural Organisational Support | `55` | farming, county, cooperative, and local organisations can reward or punish policy |
| Minority Confidence | `45` | minority citizens possess legal standing and watch the constitutional and religious settlement closely |

These are tuning anchors. Implementation balance testing may adjust numbers without changing the route logic, value ownership, or stage relationships.

## Core stage map

```text
-100        -75         -45         -15        +15         +45        +75       +100
 |-----------|-----------|-----------|-----------|-----------|----------|----------|
 REVOLUTIONARY  ARMED DUAL  REVOLUTIONARY  NEGOTIATED   CONSTITUTIONAL  EXECUTIVE  STATE
 COMMAND        AUTHORITY   ASCENDANCY     SETTLEMENT   ASCENDANCY      CONSOLIDATION MONOPOLY
```

| Range | Working stage | State of play | Constitutional opportunities | Failure pressure |
| --- | --- | --- | --- | --- |
| `-100` to `-76` | Revolutionary Command | extra-state authority directs political obedience | surrender settlement, protected election, constitutional convention after disarmament | Part 3 revolutionary takeover and civil conflict |
| `-75` to `-46` | Armed Dual Authority | government and organised challengers compete for compliance | amnesty, mediation, lawful local containment, national cabinet | divided security forces, foreign sponsorship, local command |
| `-45` to `-16` | Revolutionary Ascendancy | extra-state legitimacy shapes government choices | reconciliation, social compact, targeted prosecution, public mandate campaign | martyrdom, raids, government fall |
| `-15` to `+15` | Negotiated Settlement | neither pole owns the state | coalition, constitutional convention, broad plebiscite, labour or service compact | paralysis and contradictory commitments |
| `+16` to `+45` | Constitutional Ascendancy | state institutions govern with credible contested legitimacy | normal election, administration, law, and institutional reform | complacency and hidden challenger growth |
| `+46` to `+75` | Executive Consolidation | government can direct administration and emergency action | mobilisation, strong neutrality, major reform | overreach, minority distrust, party-state merger |
| `+76` to `+100` | State Monopoly | executive authority has displaced normal counterweights | rapid administration only under severe scrutiny | authoritarian failure, presidential conflict, mass opposition |

### Stage persistence

- `Seven-day confirmation`: a normal stage change confirms after seven consecutive days beyond the threshold
- `Five-point return margin`: return to the prior stage requires movement five points back into its band
- `Immediate crisis entry`: a regime-defining event can force immediate stage entry
- `Route conversion`: route transformation preserves the numeric value and applies the new route description

Example:

- movement from `+45` to `+46` begins confirmation
- after seven days the stage becomes `Executive Consolidation`
- return requires `+40` or lower

## Settlement Momentum map

### Thirty-day update

Every thirty days:

```text
periodic Settlement movement = Momentum x 2
```

Range:

- Momentum minimum `-5`
- Momentum maximum `+5`
- periodic movement maximum `10` points in either direction

Momentum has no unconditional drift.

### Opening momentum sources

| Source | Momentum | Duration or review | Meaning |
| --- | ---: | --- | --- |
| government control of administration | `+2` | reviewed every 180 days | the state commands ordinary government machinery |
| Fianna Fáil revolutionary inheritance | `-1` | transformed by the constitutional settlement | the governing party still claims unfinished republican legitimacy |
| organised republican networks | `-1` | recalculated after security and amnesty results | extra-state organisation remains active |
| Civil War institutional memory | `0` | activated by policy | memory becomes directional through coercion or reconciliation |
| pending constitutional mandate | `-1` | removed after plebiscite or replacement settlement | the state lacks the intended renewed popular mandate |

Opening net Momentum: `-1`

### Normal direct movement

| Outcome | Direct Settlement movement |
| --- | ---: |
| minor local or parliamentary result | `2` to `4` |
| substantial policy or stakeholder result | `5` to `8` |
| major election, law, leadership, or crisis result | `9` to `14` |
| regime-defining success or failure | `15` to `20` |

An ordinary focus does not move the Settlement by more than `8` without a connected election, event, law, or mission result.

### Contributor lifecycle

Each momentum source records:

- signed value
- source action or event
- route owner
- expiry or review date
- stacking group
- reversal condition

Normal temporary duration: `90` days

Longer memory is allowed for:

- election mandate
- constitutional rejection
- leadership transition
- coalition promise
- foreign access scandal
- major Church, Labour, or security confrontation

The same action cannot stack while its contributor remains active.

## Stakeholder tier map

All nine stakeholder values use the same tier thresholds.

| Value | Tier | Mechanical meaning |
| --- | --- | --- |
| `0` to `19` | Marginal | cannot independently alter national policy |
| `20` to `39` | Limited | can affect local outcomes or reinforce another actor |
| `40` to `59` | Organised | can demand concessions and influence national missions |
| `60` to `79` | Decisive | can determine a government, referendum, strike, service, or security outcome |
| `80` to `100` | Dominant | can veto ordinary policy or trigger route transformation |

### Stakeholder influence graph

```text
CABINET COHESION ----------> government speed, ministerial survival, succession
DÁIL MANDATE --------------> law, confidence, war assent, coalition legitimacy
ADMINISTRATIVE CONFIDENCE -> supply, services, courts, lawful transition
SECURITY LOYALTY ----------> Garda and Defence Forces obedience
REPUBLICAN NETWORKS -------> armed pressure, anti-partition legitimacy, Part 3 gates
LABOUR ORGANISATION -------> strikes, coalition support, social reform, Part 3 bridge
CHURCH INSTITUTIONAL ------> schools, hospitals, charities, morality, mobilisation
RURAL ORGANISATION --------> farm policy, local government, regional cooperation
MINORITY CONFIDENCE -------> constitutional legitimacy, service access, foreign concern
```

### Main movement causes

| Stakeholder | Rises through | Falls through |
| --- | --- | --- |
| Cabinet Cohesion | credible portfolios, collective victories, managed succession, valid coalition | unilateral leadership, resignations, failed administration, ignored promises |
| Dáil Mandate | elections, confidence agreements, major legislation, transparent war vote | confidence defeat, unconstitutional extension, party defection, improper dissolution |
| Administrative Confidence | supply delivery, public services, court compliance, clear responsibility | conflicting orders, corruption, failed prices, local obstruction, cabinet collapse |
| Security Loyalty | professional command, lawful orders, equipment, reconciliation, civilian oversight | purge, shortages, rival chains, militia, abusive internment |
| Republican Network Strength | partition crisis, failed amnesty, repression, foreign contact, grievance | reintegration, arms loss, public rejection of violence, visible constitutional progress |
| Labour Organisation | union coordination, successful strike, price crisis, electoral gain, workplace organisation | split, failed strike, repression, co-option without delivery, disorganisation |
| Church Institutional Influence | service compacts, recognition, public campaign, service dependency | internal division, scandal, state replacement, failed intervention, public backlash |
| Rural Organisational Support | prices, credit, cooperative development, roads, representation | trade shock, requisition, urban-first supply, exclusion, local-government conflict |
| Minority Confidence | enforceable guarantees, consultation, equal administration, protected schools | confessional capture, discriminatory censorship, coercive policy, unpunished attacks |

## Companion value map

### Social Consent

Opening value: `55`

| Range | Working band | Effect |
| --- | --- | --- |
| `0` to `19` | Social Fracture | mass non-compliance and combined crisis risk |
| `20` to `39` | Hostile Consent | orders require coercion or major concession |
| `40` to `59` | Contested Consent | normal opening condition, delivery and bargaining required |
| `60` to `79` | Broad Consent | reform and emergency policy can be sustained |
| `80` to `100` | Mobilised Consent | society actively supports the programme, abuse creates large backlash |

Key gates:

- constitutional campaign actions
- emergency-law breadth
- Labour-government durability
- mobilisation
- Dillon war mandate
- postwar restoration
- Northern settlement acceptance

### National Readiness

Opening value: `15`

| Range | Working band | Effect |
| --- | --- | --- |
| `0` to `19` | Exposed | no credible war entry or comprehensive defence |
| `20` to `39` | Improvised | basic emergency administration and limited territorial defence |
| `40` to `59` | Defensible | key ports, cities, communications, and approaches can be guarded |
| `60` to `79` | Prepared | extended mobilisation and selected foreign commitments become viable |
| `80` to `100` | Mobilised | full wartime capacity for Ireland's scale with severe burden |

Part 4 owns most Readiness-building actions.

### External Leverage

Opening values:

| Source | Value |
| --- | ---: |
| British | `45` |
| Vatican | `25` |
| American | `5` |
| German | `5` |

All sources use these bands:

| Range | Working band | Effect |
| --- | --- | --- |
| `0` to `19` | Marginal Access | contact without meaningful constraint |
| `20` to `39` | Negotiated Access | support and limited concessions |
| `40` to `59` | Dependence Risk | policy narrowed by trade, aid, intelligence, or security need |
| `60` to `79` | Strategic Leverage | major access or alignment demands become possible |
| `80` to `100` | Client Pressure | sovereignty compromised unless Ireland accepts loss or renegotiates |

Domestic Church influence and Vatican Leverage remain separate.

## Route transformation map

### Transformation sequence

```text
valid government or route commitment
            |
            v
preserve current Settlement value
            |
            v
clamp only beyond -60 or +60
            |
            v
remove obsolete opening momentum
            |
            v
replace pole labels and stage descriptions
            |
            v
expose route stakeholders, decisions, missions, and crises
            |
            v
start six-month settlement review
```

### Route-specific pole labels

| Route | Positive pole | Negative pole | Route question |
| --- | --- | --- | --- |
| de Valera | Constitutional Republican Government | Unfinished Republican Claim | has constitutional republicanism completed the revolution without abandoning partition? |
| Lemass | Developmental State Capacity | Traditional and Revolutionary Constraint | can administrative delivery modernise the state without losing party and national legitimacy? |
| Cosgrave | Constitutional Continuity | Civil War Grievance | can legality govern without reopening punitive pro-Treaty rule? |
| Mulcahy | Civilian Constitutional Authority | Security Command | can a military founder serve parliament without command dominating politics? |
| Costello | Government by Agreement | Party and Interest Vetoes | can a coalition act without dissolving into bargains? |
| Dillon | Parliamentary War Mandate | Neutrality Consensus | can belligerency gain democratic authority against broad neutrality? |
| Norton | Parliamentary Social Mandate | Extra-Parliamentary Labour Power | can elected reform govern with an independent labour movement? |
| constitutional vocational | Dáil Sovereignty | Vocational Social Authority | can functional representation strengthen policy without replacing parliament? |

Part 3 must define the full transformed poles for the IRA, Republican Congress, O'Duffy, Ailtirí, and hidden cultural routes.

### Six-month route review

Common requirements:

- valid majority, coalition, or confidence agreement
- Cabinet Cohesion at least `45`
- Dáil Mandate at least `45`
- Social Consent at least `40`
- no unresolved constitutional crisis

Outcomes:

| Outcome | Result |
| --- | --- |
| success | opens route middle game and durable institutional actions |
| partial success | imposes coalition, reform, review, or delivery condition |
| failure | starts first route instability branch and strengthens challengers |

## Parliamentary interaction map

### Chamber sizes

| Date or condition | Dáil size | Majority threshold |
| --- | ---: | ---: |
| 1936 opening abstraction | `153` | `77` |
| post-1937 election | `138` | `70` |
| alternate later boundary change | defined by event and electoral law | recalculated dynamically |

### Opening seat and vote ledger

| Bloc | Formal seats | Routine votes | Settlement use |
| --- | ---: | ---: | --- |
| Fianna Fáil | `77` | `76` | government seat ledger includes the outgoing Ceann Comhairle, whose vote remains reserved |
| Fine Gael inheritance | `59` | `59` | Cumann na nGaedheal and National Centre Party inheritance after party merger |
| Labour | `8` | `8` | independent parliamentary and movement actor |
| independents and minor deputies | `9` | `9` | local, farmer, Independent Labour, and other non-party interests |
| total | `153` | `152` | formal seats and routine votes remain separate |

The `Ceann Comhairle Reserve` cannot be spent as a coalition vote or counted in ordinary confidence calculations. A tied division invokes a short parliamentary resolution event and does not silently grant the government an extra vote.

Formal party membership and issue caucuses also remain separate. From 1943, Clann na Talmhan can hold `10` formal seats while five farmer independents cooperate through the temporary `Agrarian Support Bloc`. The 1944 formal anchor is `9` party seats. Coalition, confidence, and agrarian-bill calculations can read the broader caucus without rewriting independent party identity.

### Election result relationship

```text
PLEBISCITE RESULT --------------------------> constitutional legitimacy and Settlement
GENERAL ELECTION RESULT --------------------> Dáil seats and government formation
TRANSFER AFFINITY AND ELECTORAL BLOCS ------> result calculation
CAMPAIGN PROMISES --------------------------> later delivery missions
```

The 1937 plebiscite and election share a campaign period and remain separate results.

### Government forms

| Form | Seat condition | Settlement effect | Main risk |
| --- | --- | --- | --- |
| single-party majority | at least majority threshold | strong movement toward route government | overreach and broken promises |
| minority government | plurality plus written support | modest authority with active promise ledger | confidence withdrawal |
| formal coalition | combined majority plus charter | strong consent opportunity | Coalition Cohesion and vetoes |
| national cabinet | crisis-only combined mandate | strong temporary administration | expiry and route conflict |
| caretaker | no accepted nomination | limited administration | formation deadline and constitutional rupture |

## Crisis trigger map

### Major triggers

Any one can start a primary Settlement crisis.

- National Settlement at `-76` or lower
- National Settlement at `+76` or higher while Social Consent is below `35`
- Cabinet Cohesion below `20`
- Dáil Mandate below `20`
- Security Loyalty below `20`
- government-formation deadline expires
- President refuses dissolution
- constitutional plebiscite fails
- public war commitment followed by failed Dáil vote
- route leader removed without a valid successor

### Minor trigger bundle

Three lasting at least thirty days can start a crisis.

- Social Consent below `30`
- Minority Confidence below `25`
- Republican Network Strength above `75`
- Labour Organisation above `75` during unresolved industrial conflict
- Church Institutional Influence above `80` during active Church-state confrontation
- two foreign leverage sources above `60`
- emergency governance at maximum breadth without review
- Cabinet Cohesion below `35`
- Dáil Mandate below `35`

### Crisis package

Every crisis creates:

- one named Crisis Pressure value
- one timed mission
- two to four concrete response decisions
- one initiating event
- one partial-success event
- one failure event
- one cleanup event or handoff effect

Only one primary Settlement crisis runs at once. Linked secondary missions can exist when their objectives are distinct.

## Crisis family map

| Crisis | Normal trigger | Core objective | Partial success | Failure handoff |
| --- | --- | --- | --- | --- |
| rejected constitutional draft | plebiscite defeat or draft collapse | revise, campaign, or obtain lawful replacement mandate | temporary framework and later vote | emergency Constitution, government fall, Part 3 pressure |
| government-formation deadlock | no Taoiseach nominated | form majority, confidence agreement, or lawful dissolution | fixed-term caretaker | disputed authority and executive breach |
| no-confidence and dissolution | government loses Dáil | form alternative or obtain election | temporary support agreement | presidential conflict or unlawful continuation |
| presidential refusal | Taoiseach seeks dissolution without majority | nominate alternative or accept constitutional ruling | second vote | executive bypass and State Monopoly crisis |
| emergency-powers bill defeat | threat exists and Dáil rejects bill | narrow bill, coalition agreement, or emergency election | limited powers | unprepared state or executive bypass |
| cabinet collapse | resignations and low cohesion | replace ministers or reconstruct government | reduced programme | government fall and leadership route rupture |
| public-order crisis | armed incident, court dispute, abusive crackdown | secure named sites and lawful chain of command | local containment | armed dual authority or state repression |
| labour arbitration and strike | wage, civil-service, or transport dispute | negotiated settlement and essential-service continuity | sector settlement | general strike, Labour split, Congress bridge |
| Church-state confrontation | service, education, welfare, or censorship dispute | maintain services and settle lawful standards | regional compromise | service veto or authoritarian capture interface |
| leadership succession rupture | party and Dáil cannot accept successor | resolve party, cabinet, and parliamentary roles | divided leadership | party split, caretaker, or route collapse |

## Broken Settlement gate

A constitutional settlement becomes broken only when all are true:

- National Settlement is at `-76` or lower, or `+76` or higher
- Social Consent is below `30`
- government is defeated, caretaker, or bypassing constitutional authority
- at least one coercive institution or organised challenger is `Dominant`
- a relevant crisis mission fails

Possible outcomes:

- protected election
- constitutional convention
- fixed-term national cabinet
- military intervention
- revolutionary rising
- corporate seizure
- state repression

Part 3 owns full radical takeovers. Part 2 owns lawful recovery.

## Constitutional recovery map

```text
BROKEN OR NEAR-BROKEN SETTLEMENT
             |
             +-- accepted general election
             +-- cross-party cabinet with fixed expiry
             +-- presidential mediation and Dáil confidence
             +-- amnesty, surrender, or integration agreement
             +-- repeal or review of emergency powers
             +-- Labour and employer settlement
             +-- Church and state service settlement
             +-- defence command accord
```

Recovery carries a durable cost.

Possible costs:

- weaker executive law
- coalition promise
- public inquiry
- amnesty
- dismissed advisor or commander
- foreign guarantee
- delayed focus capstone
- permanent review procedure

## Decision and mission interaction map

### Normal decision roles

| Action type | Use |
| --- | --- |
| political decision | begin negotiation, choose programme, accept risk, appoint mediator |
| timed mission | meet parliamentary, map, service, security, or supply objective by deadline |
| goal-style mission | auto-complete after seat, state, service, or readiness condition is met |
| crisis decision | choose one of a small set of active responses with concrete costs |

### Cost families

- budget and civilian-factory burden
- equipment and tied-down units
- convoys, fuel, trains, and supply access
- political concessions and coalition promises
- Social Consent
- stakeholder support
- foreign leverage and intelligence exposure
- named state or port control
- deadline and delayed focus access

Political power can be one cost and is not the default whole cost.

## Law and idea interaction

### Law requirements

Every emergency or exceptional law has:

- legal trigger
- named scope
- capability
- review date
- renewal, narrowing, repeal, or failure result

Law families:

- constitutional framework
- executive and parliamentary relationship
- emergency governance
- public order
- labour relations
- Church-state settlement
- information and censorship
- vocational delegation

### Political spirit ceiling

No constitutional route carries more than three route-created persistent spirits.

Normal slots:

1. national political settlement
2. institutional capacity
3. social, coalition, Church, labour, or emergency relationship

Election, crisis, scandal, and leadership effects remain timed or transform an existing slot.

## AI strategy map

### Shared AI inputs

- route legality
- current Settlement stage
- route target band
- Social Consent
- National Readiness
- Cabinet Cohesion
- Dáil Mandate
- relevant stakeholder values
- active crisis deadline
- foreign leverage
- election timing
- war and external threat

AI cannot select an action solely because it moves the balance toward its preferred pole.

### Route target bands

| AI profile | Settlement target | Consent floor | Main retreat trigger |
| --- | --- | ---: | --- |
| de Valera steward | `+30` to `+65` | `50` | State Monopoly with low consent |
| de Valera reconciler | `+10` to `+50` | `55` | republican networks rise after failed bargain |
| de Valera emergency | `+45` to `+70` | `40` | review failure or postwar continuation |
| Lemass developmental | `+20` to `+60` | `55` | two social foundations become hostile |
| Cosgrave institutional | `+20` to `+55` | `50` | punitive policy revives Civil War grievance |
| Mulcahy professional | `+15` to `+50` | `45` | Security Command grows faster than Dáil authority |
| Costello coalition | `+10` to `+45` | `50` | Coalition Cohesion below `35` |
| Dillon intervention | `+10` to `+45` | `45` | war vote lacks readiness or safeguards |
| Norton parliamentary | `0` to `+45` | `55` | Labour unity or affiliate support collapses |
| constitutional vocational | `-10` to `+45` | `50` | council power exceeds Dáil review |

### Crisis priorities

1. prevent government disappearance
2. satisfy the named mission objective
3. prevent Security Loyalty below `20`
4. prevent Social Consent entering Social Fracture
5. avoid Client Pressure
6. restore route target band
7. resume normal route programme

Historical AI:

- avoids forced early Lemass succession
- avoids Dillon belligerency without severe Axis threat or direct violation
- avoids binding Article 19 structures beyond safe constitutional tiers
- keeps O'Duffy and Ailtirí unavailable through normal constitutional choices
- prefers lawful election, review, and sunset outcomes

## Cleanup map

| Transition | Required cleanup |
| --- | --- |
| plebiscite result | remove drafting campaign, retain result and promised concessions |
| election result | remove campaign actions, create seat ledger and delivery missions |
| government formation | remove invalid coalition targets and caretaker actions |
| route commitment | hide rival routes, transform pole labels, start six-month review |
| leadership transfer | remove contest actions and incompatible leader roles |
| party split | reassign seats, advisors, party unity, and coalition clauses |
| crisis success | remove crisis decisions, apply one durable settlement or upgrade |
| crisis partial success | remove crisis interface, create limited follow-up mission |
| crisis failure | remove invalid constitutional controls and open named failure handoff |
| emergency end | cancel wartime-only powers and start repeal or accounting mission |
| route conclusion | merge temporary route spirits and retain final lifecycle forms |

## Exploit controls

- the same contributor cannot stack while active
- repeated small actions cannot cross outer stages without a named settlement result
- elections cannot erase broken promises
- coalition dissolution cannot erase coalition liabilities
- foreign aid always creates leverage, obligation, or a concrete reciprocal cost
- amnesty requires a new surrender condition before repetition
- internment, censorship, and special courts require valid law and review
- route transformation clamps extremes and removes obsolete controls
- crisis failure cannot be avoided by hiding the decision category
- AI and player use the same eligibility and cost rules

## Part 3 transformation interfaces

| Part 2 state | Part 3 use |
| --- | --- |
| Revolutionary Command | IRA or revolutionary takeover eligibility |
| Armed Dual Authority | civil conflict, local command, and counter-state preparation |
| Republican Network Strength `75+` | Army Council escalation strength |
| Labour Organisation `75+` plus failed parliamentary bridge | Republican Congress access |
| Army Shadow failure | O'Duffy, military, or corporate crisis input |
| Compulsory Corporate Estates | authoritarian vocational interface |
| Clerical Veto State | clerical-corporate or Ailtirí pressure input |
| Council Government Without a Dáil | corporate transformation input |
| serious cultural policy milestones | hidden cultural reveal inputs without automatic absurdity |

Part 3 must transform this mechanic rather than create an unrelated replacement meter.

## Acceptance tests

Implementation must demonstrate all of the following.

1. The 1937 plebiscite succeeds narrowly while Fianna Fáil loses seats, producing separate constitutional and parliamentary effects.
2. A majority government reaches State Monopoly with low Social Consent and receives an overreach crisis instead of a pure bonus.
3. Government reaches Armed Dual Authority and recovers through lawful security and reconciliation.
4. A Fine Gael coalition forms below a single-party majority and survives its six-month review.
5. Mulcahy becomes party leader while Costello becomes Taoiseach without invalid party state.
6. Dillon obtains a Dáil war mandate and still fails when Readiness or sovereignty safeguards are inadequate.
7. Norton reaches government and preserves Labour unity through strike and coalition missions.
8. A Labour split creates National Labour seats, advisors, and coalition effects without duplicate controls.
9. A vocational council remains subordinate to Dáil authority and still changes policy gameplay.
10. Church-service reform can maintain services while reducing institutional dependency.
11. Minority Confidence collapse can create a constitutional crisis even when Church support is high.
12. Two leverage sources above `60` create competing obligations.
13. Emergency powers expire through review, accounting, and cleanup after war pressure ends.
14. Every crisis has success, partial success, failure, and cleanup.
15. Every route transformation preserves value, clamps extremes, changes labels, and starts the six-month review.
16. No route exceeds three route-created persistent spirits after cleanup.
17. Historical AI remains constitutional, neutral, and cautious while lawful alternate profiles remain possible.
18. Every Part 3 handoff consumes a named Part 2 state.
19. No constitutional action directly grants Northern Ireland, war entry, government office, or permanent alignment without the required political and strategic process.
20. Opening formal seats sum to `153`, routine votes sum to `152`, and the Ceann Comhairle Reserve is never an ordinary party vote.
21. Clann na Talmhan formal seats and aligned farmer independents can cooperate through an issue caucus without being merged into one party ledger.
