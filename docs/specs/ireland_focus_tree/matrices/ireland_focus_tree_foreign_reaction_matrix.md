# Ireland Focus Tree Foreign Reaction Matrix

Feature slug: `ireland_focus_tree`

Status: Part 6 authoritative foreign reaction ledger

All names are working labels except historical actors and institutions. Foreign actors remain separate. Their reactions can share an event window, but their leverage, obligations, access, consent and recognition states never merge.

# Reaction window and score

Irish actions open a 14-day reaction window. Each valid actor calculates a Reaction Score from six positive inputs and two reductions.

| Input | Range | Meaning |
| --- | ---: | --- |
| trigger severity | 0 to 30 | local event, national policy, war, annexation, atrocity, regime or impossible claim |
| strategic stake | 0 to 20 | trade, security, territory, ideology, citizens or institutional authority |
| existing leverage or commitment | 0 to 15 | current influence, treaty, aid, guarantee or access |
| legal and treaty exposure | 0 to 15 | obligation, neutrality law, guarantee, occupation or recognition question |
| domestic constituency | 0 to 10 | parliament, diaspora, Church, labour, press or regional pressure |
| opportunity or threat | 0 to 10 | ability to gain access, prevent rival influence or shape the settlement |
| response saturation | 0 to -15 | actor already responded to the same trigger class inside 60 days |
| inability or invalidity | 0 to -30 | defeated sponsor, no route, no access, no institution or no legal standing |

| Score | Response tier | Visible response |
| ---: | --- | --- |
| 0 to 14 | observation | intelligence, press or private note, normally no popup |
| 15 to 29 | private diplomacy | request, warning, mediation or inquiry |
| 30 to 44 | public diplomacy | protest, endorsement, recognition debate or public condition |
| 45 to 59 | material response | aid, licence, credit, restriction, guarantee or access bargain |
| 60 to 74 | coercive response | embargo, ultimatum, mobilisation, sabotage, withdrawal or monitoring |
| 75 to 100 | international crisis | coordinated pressure, intervention threat, emergency conference or recognition rupture |

# Twelve primary reaction action classes

Every response selects one primary class. A response may carry secondary effects when the actor has capacity, but the persistent record keeps the primary class, delivery path, duration, obligations, escalation, and expiry. The class does not merge actor states or leverage tracks.

| ID | Action class | Normal score band | Capability and persistence rule |
| --- | --- | --- | --- |
| RC-01 | observation and intelligence collection | 0 to 14 | records concern, target, source confidence, and review date. It cannot create leverage by itself |
| RC-02 | private inquiry or diplomatic démarche | 15 to 34 | requests clarification, protest, reassurance, or confidential terms. Stores the issue and any reply |
| RC-03 | public support, criticism, or condemnation | 15 to 49 | changes public reputation and domestic constituencies. It does not substitute for material delivery |
| RC-04 | mediation, arbitration, or conference offer | 25 to 59 | requires a valid mediator, participants, agenda, and acceptance. Failure can harden positions |
| RC-05 | recognition, legal adjustment, or admission decision | 35 to 100 | changes diplomatic or organisational status only when the actor has legal competence. Conditions and reversals are recorded |
| RC-06 | trade, customs, credit, or financial measure | 35 to 74 | requires a deliverable market, licence, credit line, customs power, or sanction channel. Debt and conditions persist |
| RC-07 | matériel, technical, relief, or reconstruction assistance | 35 to 74 | requires stock, transport, delivery route, recipient capacity, safeguards, and an end state. Undelivered promises do not grant equipment |
| RC-08 | access, intelligence, weather, rescue, or operational coordination | 35 to 74 | requires bounded access, Irish command terms, exposure, review, and withdrawal. It changes cooperation depth where valid |
| RC-09 | guarantee, defence commitment, or security consultation | 50 to 100 | requires a capable sovereign actor, named territory or institution, credible means, obligations, and expiry or withdrawal rules |
| RC-10 | covert influence, propaganda, sabotage, or clandestine liaison | 35 to 74 | requires access, network, target, exposure risk, and sponsor viability. Discovery creates its own reaction and cleanup |
| RC-11 | restriction, embargo, ultimatum, mobilisation, or withdrawal | 55 to 100 | requires legal and material capability. The demand, deadline, enforcement path, compliance, and failure outcome remain explicit |
| RC-12 | intervention, hostilities, recognition rupture, or emergency international action | 75 to 100 | reserved for actors able to act. It cannot be hidden in a digest and must create war, occupation, rupture, or emergency-conference records |

Actors with no capability for the selected class must choose a lower deliverable response. Cultural bodies cannot use RC-05 on behalf of a sovereign state, defeated sponsors cannot use RC-07 or RC-09, and a private diaspora body cannot create American state leverage through its own action.

# Actor roster

| ID | Actor family | Strategic stake | Main triggers | Positive responses | Negative responses | Persistent state |
| --- | --- | --- | --- | --- | --- | --- |
| FR-01 | United Kingdom | Atlantic security, trade, ports, Northern Ireland, Plan W, Commonwealth and republic status | neutrality enforcement, access, war entry, shipping, Northern settlement, republic, hidden strategic claim | trade, aid, intelligence liaison, guarantee, recognition, withdrawal agreement | protest, access demand, customs pressure, guarantee of Northern institutions, ultimatum, intervention | British Leverage, obligations, access, dependency, guarantee and withdrawal |
| FR-02 | Northern Ireland government and unionist institutions | constitutional position, local government, policing, industry, border security and representation | Dublin claims, border action, relief, plebiscite, federation, occupation, integration or royal and provincial proposal | limited cooperation, delegates, relief, representation, confidence measure | refusal, security mobilisation, boycott, appeal to London, local resistance | Unionist Consent and Security Stability, never British Leverage |
| FR-03 | United States government | neutral shipping, Atlantic access, procurement, diaspora pressure, postwar credit and institutions | neutrality, access, Allied cooperation, humanitarian policy, war entry, republic, UN and reconstruction | licence, credit, aid, recognition, support, technical mission | criticism, access pressure, export restriction, conditions, delay | American Leverage, debt, access and recognition |
| FR-04 | Diaspora organisations | partition, republican legitimacy, labour, relief, anti-fascism and public reputation | Northern policy, repression, neutrality, fascist route, humanitarian crisis, republic and hidden cultural claims | fundraising, lobbying, relief, press support, volunteers under lawful rules | split campaign, boycott, denunciation, rival fundraising or exposure | organisation-specific support, domestic legitimacy and exposure, not American Leverage by default |
| FR-05 | Germany and viable Axis channels | Atlantic intelligence, agents, propaganda, Irish neutrality, IRA or Ailtirí contact and access | agents, ports, weather, IRA or Ailtirí liaison, Axis alignment, sponsor crisis and defeat | promise, delivery, training, recognition or propaganda support | pressure, extraction, sabotage, abandonment, exposure or client demand | German Leverage, exposure, sponsor viability and client risk |
| FR-06 | Vatican and transnational Catholic diplomacy | humanitarian cases, Church disputes, communism, authoritarianism, antisemitism, minority treatment and mythic claims | service conflict, repression, anti-clerical law, fascist or communist route, Northern settlement, hidden religious interpretation | mediation, private support, recognition, humanitarian channel | private pressure, criticism, refusal, diplomatic distance | Vatican Leverage, separate from domestic Church domains |
| FR-07 | Commonwealth states | war contribution, citizenship, republic status, trade, defence consultation and regional legitimacy | belligerency, republic, Commonwealth exit or association, Atlantic league, reconstruction | recognition, legal adjustment, aid, consultation, bilateral treaty | concern, delayed recognition, trade condition or defence reservation | bilateral relationships and organisation legitimacy |
| FR-08 | Neutral and small states | shipping law, internment, neutral coordination, humanitarian practice, postwar institutions and diversification | neutrality precedent, forum proposal, shipping crisis, access pressure, postwar order | shared legal position, forum support, trade diversification, mediation | refusal, withdrawal under pressure, neutral condemnation or non-participation | forum cohesion, diversification and bilateral access |
| FR-09 | Allied powers and commands | Atlantic operations, intelligence, weather, access, war contribution, Northern security and occupation risk | deep cooperation, belligerency, access, intelligence, Northern war, liberation and protectorate policy | aid, command coordination, recognition, equipment, guarantee | command demand, occupation concern, access condition, withdrawal pressure | partner cooperation depth, obligations and sovereignty safeguards |
| FR-10 | Axis powers and associated regimes | ideological alignment, intelligence, ports, sabotage, propaganda and strategic denial | O'Duffy, Ailtirí, German liaison, access, anti-Allied action and sponsor collapse | aid promise, recognition, liaison or matériel | coercion, extraction, sabotage, abandonment and succession pressure | sponsor viability, dependency, exposure and route legitimacy |
| FR-11 | Postwar organisations | admission, humanitarian standards, reconstruction, trade, monitoring, sovereignty and regional security | UN application, reconstruction, occupation record, minority law, regional order and republic settlement | admission, aid, recognition, technical programme | delay, conditions, monitoring, rejection or veto | postwar recognition, application state and conclusion legitimacy |
| FR-12 | Celtic regional actors and movements | language, culture, federal ideas, local mandates, liberation, crown, provincial and impossible orders | cultural exchange, Celtic institution, protection claim, league, royal or hidden route | cultural cooperation, delegation, cautious diplomacy or voluntary membership | refusal, local opposition, exposure of overclaim or appeal to parent state | cultural and regional relationships, never sovereignty without mandate |

# Trigger class weighting

| Trigger class | UK | NI govt | US | Diaspora | Germany | Vatican | Commonwealth | Neutrals | Allies | Axis | Postwar | Celtic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| neutrality enforcement or violation | 5 | 2 | 4 | 2 | 4 | 1 | 2 | 5 | 4 | 3 | 1 | 0 |
| foreign access or formal alignment | 5 | 3 | 5 | 2 | 5 | 2 | 3 | 3 | 5 | 5 | 2 | 0 |
| Northern claim, settlement or war | 5 | 5 | 3 | 4 | 2 | 3 | 3 | 2 | 4 | 2 | 3 | 2 |
| constitutional or regime change | 4 | 3 | 3 | 3 | 4 | 4 | 3 | 2 | 3 | 4 | 4 | 1 |
| repression, antisemitism or minority law | 3 | 3 | 4 | 4 | 1 | 5 | 3 | 3 | 4 | 2 | 5 | 2 |
| republic and Commonwealth status | 5 | 2 | 3 | 4 | 1 | 2 | 5 | 2 | 2 | 1 | 4 | 1 |
| Atlantic or regional order | 4 | 2 | 4 | 2 | 2 | 2 | 4 | 4 | 4 | 2 | 4 | 5 |
| concealed royal or impossible claim | 3 | 2 | 3 | 3 | 4 | 4 | 2 | 3 | 3 | 4 | 4 | 5 |

Weights use 5 decisive, 4 strong, 3 material, 2 limited, 1 watch and 0 normally silent. They modify strategic stake. They do not predetermine approval or hostility.

# Conflict resolution and presentation

1. Direct local authority reacts first. Northern institutions resolve their local response before Britain resolves its sovereign and strategic response.
2. Existing treaty, access, guarantee and occupation obligations resolve before new offers.
3. Security actions resolve before economic actions when delay would change control, war or life safety.
4. Economic and diplomatic responses resolve next. Symbolic reactions resolve last.
5. A maximum of four major reactions receive separate visible events in one 14-day window. Other valid reactions enter a diplomatic digest. Their individual state changes still apply.
6. A digest cannot hide an ultimatum, declaration of war, guarantee, recognition rupture, occupation threat, sponsor collapse or postwar admission decision.
7. When Allied and Axis actors both respond, each uses its own viability, access and dependency state. One response does not cancel the other unless the Irish action makes the rival channel impossible.
8. Britain and the United States may coordinate pressure, but British and American Leverage remain separate.
9. Vatican response changes Vatican Leverage and Church-related diplomacy. It does not directly set a domestic Church domain.
10. Celtic cultural support never creates sovereignty, a core, a subject or a faction member without a local mandate and later valid process.

# Regime and rights response rules

- Constitutional actors distinguish lawful emergency measures from permanent executive capture.
- Fascist and authoritarian reactions explicitly evaluate coercion, antisemitism, minority exclusion, one-party law and foreign dependency.
- Communist and social-republican reactions distinguish union autonomy and plural councils from vanguard capture.
- Otherworld and mythic reactions begin with disbelief, evidence and public safety. Foreign actors do not accept Irish sovereignty claims because an impossible event occurred.
- Humanitarian aid can coexist with diplomatic condemnation. The two responses are stored separately.

# Foreign reaction AI

Each foreign actor uses the same score bands with its own strategic stake and capability. A response must be deliverable. An invalid sponsor cannot promise equipment, a defeated government cannot guarantee territory, and a regional cultural body cannot recognise a sovereign state on behalf of a country.

# Acceptance tests

1. All twelve actor families can respond separately to one major Irish action.
2. RC-01 through RC-12 are the complete primary action-class registry.
3. An actor that cannot deliver a selected class must choose a lower valid class rather than invent capacity.
4. No response writes to a merged foreign influence value.
5. Northern government reaction and British reaction remain separate.
6. Vatican response does not command domestic Church institutions.
7. A maximum of four visible reactions avoids popup floods without deleting state changes.
8. Severe responses remain visible and cannot be hidden in a digest.
9. Sponsor defeat, withdrawal and invalid access cancel future delivery while preserving debt and exposure.
10. Hidden routes receive evidence-sensitive reactions and no automatic recognition.
