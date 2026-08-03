# Ireland Focus Tree AI Strategy Matrix

Feature slug: `ireland_focus_tree`

Status: Part 6 authoritative AI ledger

All labels are working labels. `H` means documented historical baseline, `P` means plausible divergence, and `A` means deliberate absurdity after a valid reveal.

# Global AI rules

- Historical mode begins with `AI-01 Historical de Valera`. Other constitutional profiles require a lawful government change. Radical and concealed profiles require their named transition gates.
- Nonhistorical constitutional route selection keeps the Part 2 base distribution of 55, 12, 8, 5, 7, 2, 8 and 3 for de Valera, Lemass, Cosgrave, Mulcahy, Costello, Dillon, Norton and constitutional vocationalism before campaign modifiers.
- Radical, authoritarian and concealed profiles have zero opening weight. Their activation is a consequence of a valid crisis, organisation state, route vote, takeover or reveal.
- A profile stores route history, government, office, law, material, foreign, Northern and conclusion states. A leader replacement does not erase the profile history.
- No AI profile can bypass the global mission caps, category caps, reserved critical slots, Action Burden Score, map objectives, physical inputs, partial success, failure or cleanup.

# Queue and action model

## Objective queue score

AI begins with the inherited Part 5 queue score. It then applies the following profile layer.

| Input | Adjustment | Rule |
| --- | ---: | --- |
| profile primary domain | +30 | one or two categories named by the active profile |
| profile supporting domain | +15 | categories required to sustain the main route |
| route conclusion dependency | +15 | action is required for a valid conclusion and the route remains viable |
| deadline inside 60 days | +15 | only when the objective can still succeed |
| recovery from active failure | +20 | the action closes or contains a named failure |
| all material inputs present | +10 | does not replace the inherited feasibility check |
| one material input below safety floor | -20 | can become zero when the input is indispensable |
| foreign dependency beyond profile ceiling | -25 | ignored only during direct survival emergency |
| Social Consent cost would cross the profile floor | -20 | authoritarian profiles may use a lower floor but still record the cost |
| route or target invalid | set to 0 | no retry until a relevant state changes |

Critical objectives score at least 70 and may use a reserved slot. Normal objectives score 35 to 69. Maintenance objectives score 15 to 34. Objectives below 15 wait. Invalid objectives score zero.

## Burden willingness

| AI stance | Starts normal action when expected net utility is | Starts crisis action when expected net utility is |
| --- | ---: | ---: |
| cautious constitutional | 25 or more | 5 or more |
| pragmatic constitutional | 15 or more | 0 or more |
| radical survival | 10 or more | -10 or more |
| authoritarian command | 5 or more | -15 or more |
| concealed stewardship | 20 or more | 0 or more |
| desperate or self-destructive variant | 0 or more | -25 or more |

Expected net utility includes strategic value, crisis relief, route necessity and completion value, then subtracts eight points per Action Burden level, dependency risk, consent loss, exposure, duplicated regional load and opportunity cost. This is a planning formula for later centralised tuning, not implementation code.

## Cancellation and partial success

- AI cancels only when the target becomes invalid, a critical objective pre-empts the slot, expected utility falls below -20, or completion is impossible.
- After 70 percent progress, AI completes unless the action is invalid or would trigger a named collapse.
- Physical refunds never exceed the Part 5 maximum of 70 percent. Political, exposure, leverage and reputation costs are not refunded unless their lifecycle explicitly says so.
- AI accepts a defined partial result when full success is impossible and the partial result preserves a critical service, lawful office, route bridge or recovery path.
- AI does not immediately restart a failed family. The inherited 90-day repetition penalty and any route-specific review apply.

# Ten temporary state overlays

The system uses exactly ten temporary overlays. An overlay changes queue priority, safety floors, reserved slots, and exit behaviour while preserving the durable route profile and all campaign history. Several overlays can be active together. They never create a new political route. Ordinary cross-route cultural work stays under the current host profile and its normal Culture category priority. AI-12 is reserved for a government whose primary national programme is serious public cultural stewardship.

| ID | Overlay key | Activation | Priority change | Exit and cleanup |
| --- | --- | --- | --- | --- |
| OV-01 | `election_and_government_formation` | scheduled or crisis election, result declared, caretaker period, or unresolved nomination | Government and Election become critical. Routine route projects pause when they consume coalition, office, or campaign capacity. | ends after a valid majority, confidence agreement, or coalition forms, or after the mapped constitutional failure resolves. Clears campaign-only targets and retains seats, promises, debts, and route history. |
| OV-02 | `constitutional_crisis` | lost confidence, presidential refusal, disputed office, unlawful emergency extension, or constitutional breakdown | reserves the constitutional crisis slot. Government, ordinary law, courts, office continuity, and lawful recovery outrank all routine work. | ends after a valid government and law state survive the review period. Retains abuse, refusal, coup, and restoration history. |
| OV-03 | `provision_breakdown` | any Provision component below `20`, a dual bottleneck, or a named national shortage failure | National Provision actions become critical. The AI protects food, energy, transport, and maritime delivery before growth projects. | ends after every collapsed component stays above its recovery floor for 30 days. Converts surviving emergency controls into reviewed law or closes them through cleanup. |
| OV-04 | `invasion_danger` | credible invasion plan, severe territorial incident, enemy staging, or active invasion | Readiness, warning, home defence, operational plans, Neutrality incidents, and protected command become critical. | ends when the invasion state and its immediate threat expire. Retains mobilisation, damage, access, intelligence, and incident memory. |
| OV-05 | `declared_war_and_home_defence` | Ireland enters formal war or is attacked | contribution, home reserve, supply, equipment, command, access safeguards, and war law gain priority. Neutrality restoration actions close where incompatible. | ends through peace and the demobilisation review. It never deletes obligations, casualties, debt, access, or misconduct history. |
| OV-06 | `northern_occupation_and_integration` | Northern occupation, transitional authority, or an active integration stage | reserves security, service, and constitutional capacity. The global cap reaches `12` only when a national emergency is also active. | ends when occupation closes or every active region completes, pauses, or fails its current stage. Consent, rights, service, resistance, guarantee, and core-review history persists. |
| OV-07 | `foreign_sponsor_collapse` | sponsor defeat, loss of sovereignty, blocked delivery route, withdrawal, or invalid guarantee | delivery cleanup, debt, client exposure, access withdrawal, replacement supply, and neutrality or independence recovery outrank new agreements. | ends after all undelivered promises, advisers, access rights, subjects, debts, and dependencies receive a valid disposition. |
| OV-08 | `leadership_and_office_vacancy` | death, retirement, resignation, removal, split, or incompatible office combination | lawful succession and every authority-blocking vacancy become critical. Personal projects pause. | ends after each required office has a valid holder or collective body. Clears personal missions and retains organisational history. |
| OV-09 | `postwar_demobilisation_and_reconstruction` | the major war ends or Ireland leaves belligerency | demobilisation, emergency-law expiry, veterans, shipping, debt, housing, transport, identity, foreign access, and reconstruction gain priority. | ends after the dated postwar review and all remaining controls become ordinary law, a continuing programme, or an explicit failure. |
| OV-10 | `route_conclusion_review_and_consolidation` | a route requests conclusion review or begins its 180-day consolidation | every unresolved government, law, economy, defence, foreign, Northern, emergency, identity, obligation, and cleanup dependency outranks optional work. | ends with full, partial, blocked, or failed conclusion resolution. It archives eligibility evidence and preserves every disqualifier. |

Overlay collision order follows immediate constitutional survival, territorial survival, civilian provision, occupation safety, lawful authority, sponsor cleanup, postwar transition, and conclusion work. The queue still evaluates deadlines and feasibility inside that order.

# Thirty profile roster

| ID | Profile | Class | Activation gate | Strategic targets | Main queue priorities | Foreign and Northern posture | War, occupation and recovery |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI-01 `historical_de_valera` | Historical de Valera | H | Historical game rule, Fianna Fáil government, valid constitutional state | Settlement +30 to +65, Consent 50 to 70, Integrity 65+ | government, Provision, neutrality, coastwatch, reviewed emergency law | bounded Allied liaison, leverage ceilings, no formal war unless attacked. Northern: lawful deferment and functional cooperation | War: home defence and Plan W only under invasion danger. Recovery: selective reconciliation, parliamentary review, postwar expiry |
| AI-02 `de_valera_reconciliation` | De Valera reconciliation | P | Fianna Fáil government, veteran support, manageable armed incidents, valid amnesty record | Settlement +15 to +50, Consent 60+, Security Loyalty 55+ | government, organised society, republican compliance, ordinary law | active neutrality with discreet liaison. Northern: confidence measures and negotiation without a free unity bargain | War: defensive mobilisation only. Recovery: halts repeated amnesty after major breach and returns to targeted security |
| AI-03 `de_valera_emergency` | De Valera emergency stewardship | P | Declared Emergency, invasion danger, severe shortage, or repeated armed incidents | Settlement +35 to +70, Consent 45+, Readiness 45+ | critical Provision, Readiness, incidents, cabinet cohesion, review dates | cooperation short of exposed co-belligerency unless directly attacked. Northern: deferment or wartime bargain under fixed triggers | War: defence first, no indefinite mobilisation after peace. Recovery: retreats from State Monopoly when Consent below 40 and schedules sunset |
| AI-04 `lemass_developmental` | Lemass developmental administration | P | Earned succession, valid Dáil government, Developmental Standing and coalition foundation | Settlement +20 to +60, Consent 55 to 75, Provision 55+ | power, transport, industry, regional delivery, labour or rural compact | balanced British and American technical access, no leverage 60+. Northern: functional integration followed by lawful negotiation | War: wartime administrator stance only when required. Recovery: slows projects after dual bottleneck and restores coalition foundation |
| AI-05 `cosgrave_institutional` | Cosgrave institutional government | P | Fine Gael electoral or coalition mandate, paramilitary legacy resolved | Settlement +20 to +55, Consent 55+, Coalition 50+ | ordinary law, trade, rural relief, fiscal delivery, reconciliation | lawful British and Allied cooperation under sovereignty safeguards. Northern: legal settlement or deferment | War: avoids war without a separate Dillon mandate. Recovery: calls lawful election or coalition renegotiation before executive escalation |
| AI-06 `mulcahy_civil_defence` | Mulcahy civilian defence government | P | Valid Fine Gael succession, defence crisis, Civil War grievance manageable | Settlement +25 to +60, Readiness 55+, Security Loyalty 60+ | command, training, equipment, civilian review, public order | professional cooperation under Irish command. Northern: security planning plus negotiated settlement | War: mobilises within Provision and civilian command limits. Recovery: accepts Costello compromise or parliamentary review when vetoed |
| AI-07 `costello_coalition` | Costello coalition legalism | P | Hung Dáil, coalition at 70+ seats, valid charter, party leader veto resolved | Settlement +10 to +45, Coalition 60+, Minority Confidence 55+ | charter clauses, courts, cabinet balance, legal review, social compact | agreement by coalition mandate and explicit safeguards. Northern: lawful settlement with partner consent | War: partial and slower solutions preferred to unilateral war. Recovery: renegotiates programme, changes Taoiseach lawfully, or calls election |
| AI-08 `dillon_intervention` | Dillon constitutional intervention | P | All fixed political, material, Dáil, sovereignty, home reserve, and contribution gates | Intervention Mandate 90+, Readiness 45+, Provision 50+, Consent 60+ | shipping, equipment, mobility, safeguards, Dáil vote, contribution mission | Allied alignment without client pressure or command surrender. Northern: policy or lawful deferment required before war vote | War: formal belligerency only after every fixed gate. Recovery: accepts constitutional defeat and returns to principled opposition |
| AI-09 `norton_parliamentary` | Norton parliamentary Labour | H/P | Labour government or coalition office with a valid social charter | Settlement -5 to +35, Consent 60+, Movement Unity 55+ | housing, wages, transport, union unity, civil liberties, food | democratic neutrality or controlled Allied cooperation. Northern: labour and civic settlement with minority guarantees | War: avoids revolutionary bridge without explicit collapse conditions. Recovery: protects essential services, repairs affiliates, and prevents avoidable split |
| AI-10 `clann_agrarian_broker` | Clann agrarian broker | H/P | Dated Clann foundation and merger lifecycle, valid seats or issue caucus | Consent 55+, Agrarian Cohesion 55+, Provision food 60+ | roads, prices, small farms, rural power, processing, coalition clauses | cautious trade diversification. Northern: cross-border rural and local cooperation | War: opposes burdens that lack rural delivery or defence necessity. Recovery: expires issue caucuses and resolves regional leadership through party process |
| AI-11 `constitutional_vocational` | Constitutional vocational order | P | Lawful councils, Dáil sovereignty, courts, free associations, minority safeguards | Settlement +5 to +40, Labour Freedom 55+, Minority Confidence 55+ | delegate legitimacy, sector compacts, service capacity, council review | Vatican and small-state contact without domestic command transfer. Northern: rights-guaranteed federal or deferred settlement | War: councils advise, elected government commands. Recovery: closes captured councils and restores elections after crisis |
| AI-12 `serious_cultural_stewardship` | Serious cultural stewardship | H/P | A lawful government makes serious cultural stewardship its primary national programme and accepts the full public cultural conclusion. Ordinary cross-route cultural work retains the current government profile and uses that profile's normal Culture category priority | Language, Archive, Region, and Site values above route bottlenecks | teachers, archives, county participation, site protection, plural access | cultural exchanges without territorial claims. Northern: all-island cultural contact without annexation logic | War: protects sites and staff, yields to critical defence only with recorded damage. Recovery: corrects false leads, preserves serious institutions, and returns to the lawful host-government profile when culture stops being the primary programme |
| AI-13 `ira_civil_republican` | IRA civil republican government | P | Named revolutionary gateway, civil committees, public legitimacy, stable command | Settlement -35 to +10, Public Legitimacy 55+, Command Compliance 55+ | civil executive, constituent law, disarmament, county boards, security exposure | balanced recognition and diaspora, German channel refused at leverage 60+. Northern: civil guarantees, negotiation, or prepared campaign | War: no northern campaign below Readiness 35 and valid occupation plan. Recovery: protected convention, civilian control, amnesty and constituent election |
| AI-14 `ira_ghq_command` | IRA GHQ command state | P | Revolutionary Command, immediate security collapse, strong Army Council and arms network | Settlement -75 to -35, Command Cohesion 65+, Compliance 50+ | command survival, stockpiles, local orders, counter-intelligence, supply | opportunistic supply only when viable, dependency ceiling 55. Northern: coercive campaign only with supply and occupation capacity | War: centralises during survival crisis and avoids symbolic offensives. Recovery: civil compact if legitimacy rises, fragmentation if compliance fails |
| AI-15 `congress_plural` | Congress plural social republic | P | Failed parliamentary bridge, unions, agrarian actors, local mandates, subordinate armed wing | Settlement -20 to +20, Coalition 60+, Union 60+, Armed Wing 60+ | common programme, cooperatives, housing, unions, rural compact, constituent vote | anti-fascist non-alignment and labour contacts. Northern: labour commonwealth or federal settlement | War: citizen defence under elected control. Recovery: federal congress, union arbitration, constituent election |
| AI-16 `congress_vanguard` | Congress vanguard directorate | P | Repeated committee breakdown, cadre dominance, valid high-pressure state | Settlement +35 to +70 in transformed scale, Directorate 65+, Compliance 45+ | central planning, compulsory defence, security, production, party authority | available anti-fascist or socialist sponsor under dependency limits. Northern: revolutionary integration with labour and security costs | War: accepts higher coercion only under survival pressure. Recovery: retreats to congress when capacity or resistance makes purges self-defeating |
| AI-17 `oduffy_personal` | O'Duffy personal command | P | Severe crisis, dormant network, Organisation 40+, Fine Gael legitimacy broken | Personal Command 60+, Army Acceptance 40+, Sponsor Dependence below 55 | veterans, marches, movement discipline, patronage, leader control | Axis or Spanish contacts only when viable, opportunistic patron otherwise. Northern: corporate or coercive claim | War: avoids takeover below Organisation 40 and prepares succession before 1944. Recovery: successor convention, army bargain, or collapse into ghost movement |
| AI-18 `oduffy_corporate` | O'Duffy corporate and military order | P | Rebuilt corporate blocs, estate authority, army or successor settlement | Corporate Cohesion 60+, Army Acceptance 55+, Dependency below 55 | estate compliance, production, army bargain, succession, public order | pragmatic sponsor with explicit ceiling. Northern: corporate settlement or coercive integration | War: material preparation before external adventure. Recovery: institutional succession, military directorate, or lawful defeat |
| AI-19 `clerical_guardianship` | Clerical guardianship state | P | Service dependency and clerical veto failure with valid guardianship institutions | Service Continuity 65+, Minority Security 40+, Labour Freedom 35+ | schools, hospitals, welfare, service law, minority and lay representation | Vatican humanitarian contact, no Vatican command. Northern: rights-guaranteed federalism or deferment | War: regular army remains under state command. Recovery: lay representation, public capacity, judicial review, election calendar |
| AI-20 `producer_council_state` | Producer council state | P | Compulsory estates or council failure with real labour, employer, rural, and professional bodies | Council Compliance 60+, Labour Freedom 45+, Administrative Continuity 55+ | balanced estates, production, arbitration, competence, Dáil or successor review | trade and neutral contacts chosen by material need. Northern: federal or functional settlement | War: council contribution under a defined national command. Recovery: balanced producer congress or constitutional restoration |
| AI-21 `emergency_admin_restoration` | Emergency administrative restoration | P | Council or executive failure plus credible administrators, courts, and election path | Settlement +20 to +55, Continuity 65+, Consent 50+ | services, election calendar, law review, demobilisation, cleanup | temporary technical agreements with expiry. Northern: lawful deferment or caretaker settlement | War: defensive continuity only. Recovery: restores elections when war pressure ends unless impossible |
| AI-22 `ailtiri_total_state` | Ailtirí total state | P | Explicit rare AI permission, post-1940 cells, June 1942 public gate, severe emergency, capture values | Cell and Youth 60+, State Capture 60+, trained language capacity or self-destructive variant | party organisation, autarky, coercive culture, party army, censorship, succession | German alignment while viable, then post-Axis survival and isolation management. Northern: reconquest and assimilation with occupation burden | War: no early public path, no free institution capture, material limits remain. Recovery: 1945 split, regional directorate, suppression, or post-sponsor restructuring |
| AI-23 `high_king_constitutional` | Constitutional High Kingship | P/A | Nonhistorical permission, sites, archives, claimant process, convention, public and provincial ratification | Royal Legitimacy 60+, Settlement +15 to +45, Consent 55+ | convention, civil list, succession, public law, regional assent, recognition | rejects foreign-appointed claimant. Northern: negotiated crown-in-council settlement | War: crown does not replace elected command without emergency law. Recovery: abdication, new election, or abolition after legitimacy failure |
| AI-24 `high_king_sacral` | Sacral High Kingship | A | Hidden permission, credible impossible event, valid crown, obligations within capacity | Royal Legitimacy 65+, Obligation compliance 80+, Site Stewardship 60+ | geasa, sites, household capacity, public order, compact obligations | limited recognition and no sponsor appointment. Northern: ritual or federal claim only after lawful political settlement | War: accepts no conflicting geasa and resources every obligation. Recovery: penance, abdication, renegotiation, or broken kingship |
| AI-25 `five_provinces_federal` | Five Provinces federation | P | Nonhistorical permission, regional mandates, convention, rights, finance, valid Ulster status | Federal Cohesion 60+, Mandates 55+, Settlement -10 to +35 | budgets, rights, transport, equalisation, provincial institutions, guard law | federal observers and cultural contacts. Northern: empty chair or explicit Ulster mandate, never automatic claim | War: common command and funded guards only. Recovery: recentralisation, renewed mandates, or lawful dissolution |
| AI-26 `five_provinces_pentarchy` | Five Provinces pentarchy | A | Hidden permission, completed Uisneach evidence chain, valid fivefold compact | Mandates 60+, Federal Cohesion 55+, obligation compliance | provincial standards, middle balance, hosts, compact, impossible duties | cautious Celtic contact before expansion. Northern: Ulster sovereignty only through the valid route state | War: raises no host without equipment, command, and threat. Recovery: compact renewal, rival sovereignties, or reunified centre |
| AI-27 `otherworld_compact` | Otherworld compact stewardship | A | Hidden permission, verified evidence, valid public law, site and witness protections | Veil 60+, Compact Trust 60+, Settlement -15 to +30 | obligations, witnesses, sites, law, local guardians, controlled disclosure | restricts access without trust and sovereignty safeguards. Northern: compact applies only through lawful territorial settlement | War: human defence and compact obligations remain separately supplied. Recovery: restitution, new steward, renegotiation, or containment |
| AI-28 `otherworld_dominion` | Otherworld dominion | A | Explicit dominion profile, valid reveal, transformed sovereignty, prepared human administration | Otherworld Authority 70+, Veil 55+, resistance below crisis threshold | obligations, supply, human administration, resistance, site authority | rejects weaponisation that threatens sovereignty unless desperate. Northern: no automatic all-island dominion without control and settlement | War: does not delete human supply, law, or resistance problems. Recovery: new compact, uprising, accepted dominion, or collapse |
| AI-29 `otherworld_containment` | Otherworld containment | P/A | Verified or dangerous contact plus lawful or authoritarian containment profile | Veil 65+, public panic below 40, review dates active | narrow perimeters, witnesses, site safety, disclosure review, security cleanup | denies uncontrolled access and intelligence exploitation. Northern: local containment does not settle sovereignty | War: military necessity uses defined perimeters and expiry. Recovery: lawful stewardship, disclosure, continued sealing, or police-state failure |
| AI-30 `convergence_order` | Fivefold High Kingdom of Two Irelands | A | Every component route valid, no disqualifier, full hidden permission, material and Northern handoffs complete | all crown, federal, compact, Provision, Readiness, Consent, and obligation floors | component obligations, common law, federal finance, sites, succession, foreign recognition | no patron may appoint or control the order. Northern: completed lawful settlement and stage 5 integration required | War: no expansion until internal compact and supply are stable. Recovery: component separation, constitutional restoration, or final collapse |

# Category priority by profile family

Priority uses `5` critical, `4` high, `3` normal, `2` maintenance, `1` low and `0` unavailable. A profile row is a default. The queue score and active crisis state still decide the exact action.

| Profile family | Gov | Election | Society | Culture | Radical | Provision | Readiness | Neutrality | Foreign | Northern | Occupation | Regional | Postwar |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| historical constitutional | 4 | 3 | 3 | 2 | 0 | 4 | 4 | 5 after 1939 | 3 | 2 | 0 unless required | 1 | 4 after war |
| alternate constitutional | 4 | 4 | 4 | 2 | 0 | 4 | 4 | 3 | 3 | 3 | 1 | 2 | 4 |
| radical republican or Congress | 4 | 2 | 4 | 2 | 5 during transition | 4 | 4 | 2 | 3 | 4 | 3 after control | 2 | 3 |
| corporate or clerical authoritarian | 5 | 1 | 4 | 2 | 5 during takeover | 4 | 4 | 2 | 4 | 4 | 4 after control | 3 | 3 |
| public cultural stewardship | 2 | 1 | 3 | 5 | 0 | 2 | 2 | 1 | 2 | 1 | 0 | 2 | 2 |
| concealed royal or provincial | 4 | 2 | 4 | 5 | 3 | 4 | 4 | 2 | 3 | 4 | 3 | 5 | 4 |
| Otherworld | 4 | 1 | 4 | 5 | 3 | 4 | 4 | 2 | 4 | 3 | 3 | 5 | 4 |

# Offices, laws and leaders

- AI fills a vacant office before starting a routine programme when the vacancy blocks legal authority, command, diplomacy or a conclusion.
- Party leader, parliamentary leader, Taoiseach, head of state, chief of staff, security chief, movement leader and armed-wing commander remain separate.
- Historical death, retirement, election and split dates trigger a review rather than deleting the organisation.
- AI law choice compares immediate crisis relief, review date, abuse risk, consent floor, route compatibility and restoration path. It never chooses an unreviewed permanent emergency merely because the modifier is stronger.
- A route with a collective office uses an institutional name and portrait. It does not invent a personal ruler for a council.

# Diplomacy and war

- Every foreign agreement requires a valid actor, delivery path, obligations, command limit, exit and dependency ceiling.
- AI never accepts access that crosses its profile ceiling unless direct survival is at risk and a later withdrawal mission exists.
- War planning requires a political gate, Readiness, Provision, home defence, supply and occupation or settlement plan.
- Northern war never grants immediate cores. AI opens occupation and integration work and reserves one security, one service and one constitutional slot.
- AI formation of an Atlantic or Celtic order requires real members and funded contributions. Cultural contacts do not count as sovereign members.

# Concealed route permission matrix

| Route | Historical AI | Nonhistorical AI | Hidden-content rule | Extra activation proof |
| --- | --- | --- | --- | --- |
| O'Duffy | prohibited without severe crisis | rare after severe crisis | not required because route is visible after crisis | Organisation 40+, unresolved network, Fine Gael rupture |
| Ailtirí | hard zero | rare | explicit rare-authoritarian or hidden-content permission | post-1940 cells, June 1942 public gate, severe emergency, capture values |
| High Kingship | cultural study only | constitutional variant possible | required for sacral variant | sites, archives, claimant process, convention and ratification |
| Five Provinces | limited devolution only | federal variant possible | required for pentarchy | regional mandates, convention, rights, finance, valid Ulster rule |
| Otherworld | investigation only | no impossible validation | required for all commitment profiles | verified independent evidence, sites, witnesses, public law and no disqualifier |
| convergence | prohibited | prohibited without full component routes | required | all component conclusions, stage 5 Northern integration and no patron control |

# Anti-stall recovery

If the preferred profile becomes invalid, AI moves to the nearest valid recovery profile. This is not a fallback route. It preserves route history, failures, laws, material damage, leverage, offices and achievement disqualifiers.

| Invalid profile | Recovery order |
| --- | --- |
| de Valera routes | historical or coalition constitutional government, then election |
| Lemass | return to ministerial Fianna Fáil, coalition, or scheduled election |
| Fine Gael or Costello | coalition renegotiation, opposition, then election |
| Dillon | constitutional opposition or deep cooperation short of war |
| Norton | coalition Labour, parliamentary opposition, split or reunion lifecycle |
| IRA | civil compact, protected convention, disarmament and election, then fragmentation only if no authority survives |
| Congress | federal congress, union arbitration, constituent election, then narrow party state only after valid capture |
| O'Duffy | succession, corporate institutions, lawful defeat, or ghost movement |
| clerical and producer states | emergency restoration, balanced council, election or explicit captured-state transition |
| Ailtirí | regional directorate, suppression, post-sponsor restructuring or constitutional restoration |
| crown | new election, regency, abdication or abolition |
| provinces | renewed mandates, legal recentralisation or dissolution |
| Otherworld | restitution, new steward, containment, disclosure or route closure |
| convergence | separate the component orders and revalidate each one |

# AI validation scenarios

1. Historical 1936 to 1948 run keeps hidden commitments at zero and follows the dated constitutional, neutrality, defence and postwar reviews.
2. Hung Dáil run forms only a valid 70-seat government and never duplicates offices.
3. Severe shortage run pre-empts routine projects, respects the global cap and returns the slot after 30 stable days.
4. Dillon run refuses war below any fixed gate and accepts constitutional defeat.
5. Northern occupation run uses the 12-slot cap only while both national emergency and occupation exist.
6. Sponsor collapse run cancels undelivered aid, keeps debt and exposure, and opens recovery.
7. Ailtirí run cannot appear before its date and organisation gates.
8. Hidden route run preserves zero historical weight and requires explicit permission.
9. Partial success run does not restart the same family inside the repetition window.
10. Conclusion run refuses completion while a required law, office, occupation, obligation or critical mission remains unresolved.
