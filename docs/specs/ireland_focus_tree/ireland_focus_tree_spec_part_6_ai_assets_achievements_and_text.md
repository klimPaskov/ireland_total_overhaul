# Ireland Gameplay Overhaul and Focus Tree

## Part 6: AI, foreign reactions, achievements, assets and text direction

Feature slug: `ireland_focus_tree`

Status: Part 6 source specification

Planning only. This file contains no implementation code and no final localisation. Structural names are working labels. Historical classification remains `H`, plausible divergence remains `P`, and deliberate absurdity remains `A`.

# Part 6 design result

Part 6 completes the behaviour and presentation contract for the Ireland overhaul. It gives every route an executable AI identity, preserves the thirteen action categories and mission limits, resolves simultaneous foreign reactions, fixes a 32-entry achievement set, defines a complete source-mode asset programme, limits scripted GUI and animation to clear state-management needs, and provides self-contained implementation prompts.

Part 6 does not change the National Settlement, companion values, parliamentary arithmetic, Provision, Readiness, Neutrality Integrity, Northern ledger, decision categories, mission caps, event floors, lifecycle rules or conclusion gates.

# Fixed inherited limits

- Thirteen decision categories retain their Part 5 ownership and category caps.
- Global active missions remain 8 in normal peace, 10 during the Emergency or war, and 12 only during simultaneous national emergency and Northern occupation.
- Component collapse, invasion, constitutional collapse, occupation security and route review reserve critical slots.
- Action Burden remains 1 to 10, command power remains capped at 60, goal missions auto-complete and cancellation returns at most 70 percent of recoverable physical inputs.
- The event programme retains eighteen historical chains, eighteen political crisis families, twelve foreign reaction families and at least 236 consequential flavour events.
- The package retains three persistent route-spirit families and seventeen law ladders.
- Northern cores remain unavailable before integration stage 5 and final review.

# AI architecture

## Exact profile count

The overhaul uses exactly 30 route profiles and exactly ten temporary state overlays. A profile is a durable strategic identity. The overlays handle election, constitutional crisis, shortage, invasion, war, Northern occupation, sponsor collapse, office vacancy, postwar transition, and conclusion review. This prevents one generic AI and also prevents a maintenance burden of near-duplicate profiles.

Profile activation is separate from focus choice. An AI cannot become radical, corporate, royal, provincial or Otherworld merely because a weighted focus is available. The political, organisational, legal, material and reveal gates must already be valid.

## Historical and nonhistorical selection

Historical mode assigns Historical de Valera as the starting government profile. It preserves the historical Constitution, 1938 settlement, active neutrality, Emergency mobilisation, limited Allied liaison, IRA suppression, dated leadership transitions and postwar review unless the campaign forces a lawful change.

Nonhistorical mode uses the Part 2 constitutional base weights before campaign modifiers. Radical and hidden profiles remain at zero until their named transition. An explicit hidden-content game rule is necessary for every `A` commitment.

## Profile memory

AI records route commitments, failed governments, offices, laws, foreign agreements, sponsor dependence, Northern status, hidden evidence and conclusion eligibility. Recovery changes the active profile without erasing history. This preserves achievement disqualifiers and prevents a failed dictatorship from becoming a clean constitutional state through one event.

## Mission queue and reserved slots

The AI queue starts with the Part 5 priority score, then adds profile priority, route dependency, recovery value, feasibility and deadline pressure. It subtracts burden, dependency, consent loss, exposure, repetition and regional collision. Critical objectives may pre-empt routine work. A paused routine objective does not fail during valid pre-emption.

AI leaves the correct number of critical slots available. It does not fill the global cap with routine construction while a component, invasion, constitutional, occupation or route-review crisis is pending.

## Dynamic cost behaviour

AI evaluates the full cost package. Political power is never treated as the only price. It considers factories, equipment, manpower, transport, fuel, convoys, XP, leverage, exposure, legitimacy, consent, tied units and time. It blocks actions whose indispensable physical input falls below a safety floor.

## Partial success, failure and recovery

AI can deliberately accept a mapped partial success when full completion becomes impossible. It cannot relabel failure as success. Named failures open recovery objectives, change profile priorities and preserve campaign memory. The AI does not endlessly restart a recently failed family.

## Government, office and law behaviour

AI forms a valid majority, confidence agreement or 70-seat coalition before seeking a new election. It keeps party, parliamentary and state offices separate. It fills command and constitutional vacancies before routine programmes. Emergency laws are chosen with review and expiry, not as permanent modifier upgrades.

## Material statecraft

Every profile has Provision and Readiness targets. No profile receives free industry, troops, shipping, supply or administration from a political victory. Authoritarian and impossible profiles can accept harsher burdens, but their population, economy, logistics and command still constrain them.

## Neutrality, diplomacy and war

AI understands neutrality as a sequence of incidents, laws, access, internment, intelligence, weather, trade, rescue and public legitimacy. Formal war requires the route-specific political and material gate. Foreign agreements record source-specific leverage, obligations, command limits, withdrawal and dependency.

## Northern Ireland

AI chooses negotiation, lawful deferment, confidence measures, federalism, unitary settlement, labour settlement or coercive war only when its profile permits that family. It plans policing, services, finance, representation, rights, demobilisation and foreign guarantees after control. It never grants cores at occupation.

## Postwar and conclusion behaviour

AI reviews emergency powers, mobilisation, access, debt, reconstruction, constitutional identity, Northern status and foreign alignment after the war. It begins a route conclusion only after all mandatory offices, laws, obligations, occupation states and critical missions are resolved.

## Concealed route behaviour

Historical AI investigates folklore, archives and sites as public culture. It never interprets them as proof of sovereignty or supernatural contact. Rare hidden AI requires explicit permission, full public prerequisites, valid evidence, no disqualifier and a named profile. Once committed, it understands the full route rather than relying on human-only decisions.

The authoritative profile roster and queue rules are in `matrices/ireland_focus_tree_ai_strategy_matrix.md`.

# Foreign reaction architecture

## Twelve separate actor families

The reaction layer contains exactly twelve actor families and exactly twelve primary reaction action classes. Britain, Northern institutions, the United States, diaspora organisations, Germany, Vatican diplomacy, Commonwealth states, neutral states, Allied powers, Axis powers, postwar organisations and Celtic regional actors each keep their own state. Action classes range from observation and private diplomacy through recognition, material aid, guarantees, covert action, coercion, and intervention. They never merge actor state.

## Fourteen-day reaction window

A major Irish action opens a 14-day window. Direct local actors resolve first, obligations and security resolve next, economic and diplomatic responses follow, and symbolic reactions resolve last. Four major responses may receive separate events. Additional valid responses enter a digest without losing their individual effects.

## Response scoring

Response tier depends on severity, strategic stake, existing leverage, legal exposure, domestic constituency, opportunity, saturation and capability. Scores range from observation through private and public diplomacy to material response, coercion and international crisis.

## Conflict rules

Northern and British reactions remain separate. Allied and Axis actors may both respond when both channels remain viable. Vatican Leverage remains separate from domestic Church power. Diaspora support does not automatically change American Leverage. Celtic cultural actors cannot grant sovereignty.

The authoritative actor and weighting ledger is `matrices/ireland_focus_tree_foreign_reaction_matrix.md`.

# Achievement architecture

## Set size and distribution

The final planning set contains 32 achievements: 8 Hard, 12 Very Hard, 8 Campaign and 4 Hidden Mastery. The set covers historical administration, neutrality, defence, economy, constitutional alternatives, agrarian politics, radical routes, restoration, authoritarian survival, Northern settlement, regional orders and concealed conclusions.

## Tracking philosophy

Achievements use campaign history rather than end-state snapshots. No-dependency conditions track maximum leverage. Rights conditions track every disqualifying action. Office conditions track lawful entry and simultaneous roles. Northern conditions track the settlement process and every integration stage. Hidden conditions track evidence provenance and accepted obligations.

## Visibility

Public achievements can show visible system requirements. Hidden achievements reveal only after the route appears. The convergence achievement remains secret until completion. Progress text cannot expose an unrevealed route or secret variable.

## Ethical direction

Authoritarian-route achievements test survival, succession, independence or restoration. They do not require atrocities, antisemitic escalation, mass repression or foreign-client status. Their writing direction remains clinical or self-condemning rather than celebratory.

The exact conditions, working IDs, disqualifiers and icon directions are in `matrices/ireland_focus_tree_achievement_matrix.md`.

# Asset architecture

## Source separation

Real people, historical flags, attested symbols, documents, sites and photographed events use sourced mode with provenance and licence notes. Generated art is reserved for alternate flags, fictional councils, route emblems, impossible actors, alternate documentary scenes, icons and hidden presentation.

## Portraits

The sourced roster contains 60 real people. Primary leaders are P0. Recurring advisors and event figures are P1. A small number of optional local actors are P2 and are used only when their mapped event or office appears. No generated historical likeness is accepted.

## Flags and identity

Constitutional routes normally retain the tricolour. Eighteen alternate identity flag sets cover radical, corporate, Ailtirí, royal, provincial, Otherworld and convergence conclusions. Each generated flag begins after the recorded divergence.

## Icons

The minimum budget covers 216 focus icons, 13 category icons, 70 decision icons, 54 mission icons, 63 persistent spirit icons, 27 temporary state icons, 51 law icons, 45 mechanic icons and 32 achievement concepts with three achievement states. Controlled reuse is allowed only where one action class is genuinely shared.

## Event images

The event plan uses 120 unique images, split into 69 sourced and 51 generated assets. Major chains and conclusions receive anchor images. The 236-event flavour programme uses documented family reuse instead of 236 near-duplicate pictures.

## GUI and animation

Three scripted GUI surfaces pass the clarity test: National Conditions Panel, Northern Settlement Ledger and Concealed Evidence Ledger. Seven animations pass the state-change test. National Settlement remains native balance of power and mostly static. No animated portrait is approved.

The full counts, rosters, source modes and production order are in `matrices/ireland_focus_tree_asset_ledger.md`.

# Localisation and dynamic text direction

## Information hierarchy

Every visible system shows current value, band, trend, main positive causes, main negative causes, active objective, reserved slot state and next review when relevant. Complex requirements use short summaries and detailed named-place tooltips.

## Colour identity

| System | Colour direction | Warning rule |
| --- | --- | --- |
| National Settlement | revolutionary ochre, negotiated cream, constitutional teal | either extreme gains a red crisis frame when failure is active |
| Social Consent | civic green | amber below 45, red below 25 |
| National Provision | agricultural green and supply brown | amber strain, orange severe, red collapse |
| National Readiness | steel blue | amber bottleneck, red operational failure |
| Neutrality Integrity | neutral white and sea blue | amber compromised, red breakdown |
| Unionist Consent | orange | red only for active refusal or violence |
| Nationalist Consent | green | red only for active refusal or violence |
| Labour Cooperation | burgundy | red only for strike, exclusion or coercion crisis |
| British Flexibility | blue | red only for ultimatum or intervention |
| Security Stability | slate | red for insurgency, reprisal or command collapse |
| Integration Capacity | gold | red for insolvency or administrative failure |
| foreign leverage | actor-specific icon and colour | red outline at client pressure, never one merged colour |
| hidden evidence | parchment, stone and muted violet | no route colour before credible partial reveal |

Colour never replaces a label or icon. Accessibility requires named bands, arrows and textual cause summaries.

## Route voices

- De Valera is formal, sovereign, patient and legal.
- Lemass is administrative, material and impatient with non-delivery.
- Fine Gael and Costello are institutional, legal and coalition-conscious.
- Dillon is morally urgent but constitutionally exact.
- Labour and Congress use work, housing, wages, services, unions and smallholders rather than generic imported slogans.
- IRA routes distinguish civil republican authority from Army Council command.
- O'Duffy, corporate and Ailtirí writing shows coercion, hierarchy, exclusion, antisemitism and anti-democratic law directly.
- Church and vocational writing distinguishes institutions, services, lay actors, bishops, minorities and Vatican diplomacy.
- Northern writing uses local government, industry, housing, policing, religion, labour and representation.
- Hidden writing begins with records, testimony, material anomalies and uncertainty. It does not announce the route.

## Dynamic references

Final text should name the active office-holder, party, coalition, law, region, sponsor, value, deadline, incident, settlement model, integration stage and obligation where the player needs that information. It should not expose internal IDs, hidden weights or unrevealed branches.

# Route presentation coverage

Every AI profile has a linked achievement challenge, asset family, text voice and failure presentation. The achievement hook can be a direct mastery goal, a recovery goal, or a difficult shared conclusion. It does not mean every profile receives a separate automatic achievement.

| AI profile | Achievement hooks | Main asset family | Localisation direction | Failure and recovery presentation |
| --- | --- | --- | --- | --- |
| AI-01 Historical de Valera | A-02, A-03, A-04, A-05 | de Valera portrait, Constitution, tricolour, coastwatch and merchant-shipping images | measured state papers, sovereignty, legal restraint and practical wartime administration | loss of trust appears through parliamentary criticism, shortages and dated review, not sudden regime collapse |
| AI-02 De Valera reconciliation | A-01, A-02 | veteran, amnesty, Garda, republican and county-meeting assets | formal republican language with clear distinctions among pardon, compliance and surrender | a breached amnesty names victims, security costs and the surviving lawful alternatives |
| AI-03 De Valera emergency | A-02, A-06, A-21 | Emergency statute, cabinet, army, rationing and warning assets | controlled official language that shows the widening reach and expiry date of each power | permanent rule is shown through missing reviews, silenced institutions and growing administrative dependence |
| AI-04 Lemass developmental | A-08 | Lemass portrait, turbines, factories, roads, ports and regional plans | delivery, output, bottlenecks, contracts and named regions | failed development shows debt, idle plant, import exposure and coalition blame |
| AI-05 Cosgrave institutional | A-09, A-15 | Cosgrave portrait, Dáil, courts, ballots and reconciliation assets | constitutional continuity, fiscal limits and coalition duty | failure uses electoral defeat, exhausted partners and unresolved Civil War memory |
| AI-06 Mulcahy civilian defence | A-09, A-10 | Mulcahy portrait, officer training, depots and civilian-review assets | professional command vocabulary under explicit elected authority | Army Shadow is shown through command intrusion, political distrust and civilian corrective action |
| AI-07 Costello coalition | A-10, A-14, A-15 | Costello portrait, coalition charter, courts and presidential assets | precise legal and coalition language with named clauses and offices | collapse identifies the broken charter clause, responsible partner and lawful next step |
| AI-08 Dillon intervention | A-11 | Dillon portrait, Dáil division, protected access, convoy and contribution assets | morally urgent foreign-policy language paired with exact constitutional safeguards | defeat remains principled opposition, while dependency failure shows surrendered command and leverage |
| AI-09 Norton parliamentary | A-12 | Norton portrait, union cards, housing, wages and parliamentary assets | practical labour language rooted in affiliates, services, work and democratic procedure | split and defeat show affiliate choices, lost mandates and repair options without assuming revolution |
| AI-10 Clann agrarian broker | A-16 | Donnellan, Cogan and Blowick portraits, farms, roads, markets and rural power | county, smallholder, price and local-service language | failure shows regional fracture, expired caucuses and unmet rural clauses |
| AI-11 Constitutional vocational | A-13 | council seals, delegate credentials, courts and association assets | institutional and social language that names who elected or appointed every delegate | capture is shown through closed associations, coerced labour and loss of Dáil review |
| AI-12 Serious cultural stewardship | A-27, A-28, A-30 prerequisite tracking | teachers, archives, folklore notebooks, Gaeltacht and protected-site assets | public cultural work, evidence quality, regional access and scholarly caution | false leads and damaged sites are corrected openly, with no automatic path to hidden sovereignty |
| AI-13 IRA civil republican | A-17, A-21 | civil executive, county committees, republican charters and disarmament assets | republican legitimacy, constituent law and civilian responsibility | failure distinguishes renewed military command, local defection and a protected return to elections |
| AI-14 IRA GHQ command | A-17 recovery, A-21 | Army Council, arms stores, dispatches, safe houses and command-map assets | terse military orders and contested command claims | fragmentation shows lost districts, supply, public protection and the terms of a civil compact |
| AI-15 Congress plural | A-18 | Congress leaders, union halls, tenant and smallholder meetings, cooperative assets | plural social-republican language that names unions, committees and rural mandates | breakdown identifies which coalition promise, affiliate or armed safeguard failed |
| AI-16 Congress vanguard | A-18 recovery, A-21 | directorate, planning office, militia and compulsory-production assets | centralised ideological language whose coercive terms remain visible | purges and committee capture show labour resistance, administrative loss and a route back to congress authority |
| AI-17 O'Duffy personal command | A-19 | O'Duffy portrait, rallies, veterans, blue-shirt material and patronage assets | personal command, martial hierarchy and imported authoritarian language | illness, succession, army refusal and sponsor exposure are presented as structural weaknesses |
| AI-18 O'Duffy corporate state | A-20 | estate chambers, corporate councils, army and industrial-delegate assets | formal corporate language that identifies coercive representation and excluded groups | institutional failure shows captive estates, military veto and foreign dependency |
| AI-19 Clerical guardianship | A-21, A-07 | collective guardianship, hospitals, schools, welfare and episcopal assets | institutional Catholic and lay-service language, separate from Vatican diplomacy | failure names minority exclusion, service coercion, episcopal division and constitutional restoration |
| AI-20 Producer council state | A-13 recovery, A-21 | producer congress, union, employer, rural and professional-delegate assets | sector bargaining and production language with visible labour freedom | capture shows compulsory membership, closed unions and the route to balanced councils or elections |
| AI-21 Emergency administrative restoration | A-21 | caretaker cabinet, courts, electoral registers and demobilisation assets | restrained administrative repair, legality and dated restoration | renewed capture is shown as failure to restore offices, ordinary law or a valid election |
| AI-22 Ailtirí total state | A-22 | sourced movement material, generated party-state seals, cells and directorate images | Irish-language total-state vocabulary with explicit antisemitism, coercion and exclusion | sponsor collapse, regional fracture and constitutional restoration remain distinct outcomes |
| AI-23 Constitutional High King | A-27 | crown-in-council, convention, provincial and ratification assets | legal antiquarian language translated into modern constitutional offices and limits | captive claimant, failed ratification and abdication are shown without divine claims |
| AI-24 Sacral High King | A-29 | generated sacral crown, mound, obligation and household assets | ritual and obligation language clearly marked as deliberate absurdity after reveal | broken obligations produce named restitution, abdication, conflict or collapse |
| AI-25 Five Provinces federation | A-28 | provincial arms, assemblies, equalisation, transport and compact assets | federal finance, mandates, rights and regional administration | failure identifies unfunded powers, invalid Ulster status and rival mandates |
| AI-26 Five Provinces pentarchy | A-28, A-29 | generated fivefold standards, Uisneach convention and provincial-host assets | ceremonial provincial language with clear practical budgets and command duties | compact breach shows which province, duty, right or common institution failed |
| AI-27 Otherworld compact | A-29, A-30, A-31 | generated compact, witnesses, sites, records and joint-council assets | evidence-led uncertainty followed by exact obligations and human-law safeguards | failure uses restitution, broken trust, witness harm and containment, not vague magical punishment |
| AI-28 Otherworld dominion | A-29 | generated dominion authority, human administration and resistance assets | impossible sovereignty presented after verified reveal, with ordinary supply and rights costs still visible | collapse shows resistance, administrative failure, broken obligations and possible return to compact |
| AI-29 Otherworld containment | A-30 | perimeter, archive, witness, Garda, military and site-safety assets | cautious public-safety and evidence language with explicit review and expiry | police-state failure, uncontrolled disclosure and lawful stewardship are separate outcomes |
| AI-30 Convergence order | A-32 | final crown, fivefold, compact, Northern and common-law asset families | composite language that names each component institution and avoids one vague mystical register | failure separates crown, provinces and compact, preserving every breach and restoration path |

# Quote and cultural remark research

Direct quotations, slogans, prayers, proverbs, traditional sayings, programme phrases, literary echoes and period remarks require source research. The research package must record exact wording, author or speaker, source work or archive, date, source URL, attribution confidence and copyright status. Unsourced quote-site material is rejected.

Research packages cover constitutional and parliamentary language, neutrality and emergency law, Labour and agrarian language, republican and Congress terminology, corporate and Ailtirí programmes, Church and minority language, Northern political vocabulary, Gaelic and folklore terminology, royal and provincial institutions, military and maritime language, and foreign diplomatic reporting.

# Audio threshold

Audio remains optional and has only three briefs: coastwatch and Atlantic ambience, constitutional or sacral High Kingship ceremony, and verified Otherworld entry. Each requires a real gameplay surface, separate composition and recording rights, a manifest and a static silent fallback. No achievement or route depends on audio.

# Prompt boundaries

## Decision and mission prompt

Owns implementation of the thirteen categories, 140 actions, 54 mission families, caps, queue, costs, AI selection, tooltips, map objectives, outcomes and cleanup. It does not own final asset creation or historical quote research.

## Asset prompt

Owns sourcing or generation, processing, DDS conversion, placement, manifests and GFX handoff for the ledger. It does not invent gameplay, edit events, or generate real portraits.

## Text and audio research prompt

Owns source verification and research notes for quotes, remarks and optional audio. It does not write final localisation or wire sound.

## Achievement prompt

Owns implementation of the 32-entry matrix, tracking, icons, localisation direction and validation. It does not weaken route or lifecycle conditions.

# Part 6 acceptance criteria

1. Exactly 30 AI profiles and exactly ten temporary state overlays cover every constitutional, radical, corporate, clerical, public cultural, royal, provincial and Otherworld route and campaign state.
2. Historical AI has zero concealed-route commitment weight.
3. AI obeys the thirteen category caps, global caps, reserved slots, queue, dynamic cost, partial result and cleanup rules.
4. The foreign reaction matrix contains exactly twelve actor families and exactly twelve primary reaction action classes with separate actor states, capability limits, delivery records and cleanup.
5. The achievement matrix contains exactly 32 nontrivial achievements with tracking and disqualifiers.
6. The sourced portrait roster contains exactly 60 real people and forbids generated likenesses.
7. The source-research roster contains exactly 40 historical symbol and document packages, exactly five source-clearance states, an eleven-tier archive hierarchy and a per-item source manifest contract.
8. The asset ledger fixes one historical base flag, 18 alternate flag sets, 120 event images, three GUI surfaces and seven animations.
9. Localisation direction distinguishes routes, shows dynamic causes and hides unrevealed content.
10. Quote, remark and audio work has explicit thresholds and source requirements.
11. Four implementation prompts have non-overlapping ownership.
12. No Part 1 through Part 5 constant, route gate, event floor, mission cap, law state or conclusion is changed.
13. Part 7 receives a clean source-of-truth and improvement-loop handoff.

# Part 7 interface ledger

| Part 6 surface | Part 7 receives | Part 7 must complete | Part 7 cannot change without explicit contradiction repair |
| --- | --- | --- | --- |
| AI | 30 profiles, ten temporary state overlays, queue formula, gates, recovery and validation scenarios | reconcile with route maps and final coding prompt | replacing route AI with generic focus weights |
| foreign reactions | 12 actor families, 12 primary action classes, score bands, reaction window, capability limits and conflict rules | reconcile event map and coding handoff | merging leverage, deleting valid reactions or allowing an undeliverable action |
| achievements | 32 exact entries, tracking, disqualifiers, visibility and icon directions | final index, prompt reconciliation and completion checks | automatic route-start unlocks or weakened conditions |
| assets | exact portrait, flag, icon, event image, GUI and animation budgets, five clearance states, eleven-tier source hierarchy and per-item manifest contract | source-of-truth index and final package inventory | generated historical likenesses, unverified rights or placeholder completion |
| localisation | route voices, dynamic value hierarchy, colour direction and hidden-text rules | coding prompt and final documentation cleanup | writing final localisation inside the planning package |
| text and audio | research packages and three optional audio briefs | index and implementation handoff | unsourced quotations or required audio dependency |
| prompts | decision and mission, asset, text and audio, and achievement prompts | reconcile with the final coding prompt | duplicate ownership or fallback instructions |
| project status | exact Part 6 stopping point and fixed counts | mandatory improvement-loop pass, finding disposition, final validation and canonical ZIP | claiming the required subagent pass ran when no execution evidence exists |
