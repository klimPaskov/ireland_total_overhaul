# Ireland Focus Tree Complete Coding Prompt

Feature slug: `ireland_focus_tree`

Mod: `Ireland Total Overhaul`

Namespace and script prefix: `slopx`

## Objective

Implement the complete Ireland gameplay overhaul and national focus tree described by the canonical package under `docs/specs/ireland_focus_tree/`. Preserve every route, gate, value, lifecycle, failure, recovery, AI profile, achievement, asset requirement, and historical boundary. Do not replace any mapped system with a smaller fallback, one-focus substitute, passive decision store, generic ideology path, free territorial reward, or cosmetic-only conclusion.

No fallbacks, shortened substitutes, unresolved placeholders, or cosmetic-only conclusions are permitted.

This prompt coordinates implementation. The specialised decision and mission, asset, text and audio research, and achievement prompts retain their own ownership.

## Required reading before code

Read in full:

1. `AGENTS.md`
2. the offline Paradox wiki pages and local vanilla documentation required by `AGENTS.md`
3. at least one relevant vanilla precedent for each engine surface
4. existing Ireland Total Overhaul patterns for country history, focus loading, events, decisions, ideas, AI, scripted localisation, GUI, GFX, achievements, flags, and validation
5. `docs/specs/ireland_focus_tree/ireland_focus_tree_index.md`
6. all six numbered specification parts
7. all canonical maps and matrices
8. the historical research notes
9. all six implementation prompts under `docs/specs/ireland_focus_tree/prompts/`

The offline wiki and local game installation were unavailable during planning. They are a hard implementation preflight. Do not infer syntax or engine behaviour from memory when those sources are available.

## Source precedence

Use the precedence rules in `maps/ireland_focus_tree_canonical_reconciliation_map.md`.

- Part 7 index and reconciliation files own canonical inventory, naming registry, explicit repairs, and file precedence.
- Specialised matrices and maps own exact rows, IDs, counts, thresholds, and cross-reference keys.
- Numbered specification parts own route meaning, player experience, historical classification, tradeoffs, failures, recovery, and conclusions.
- Research notes own historical claims and source confidence.
- Prompts own work order and completion gates. They cannot redesign the specifications.

When you find a real contradiction, stop that surface, record the contradiction, repair every affected canonical document, and then implement. Do not silently select the easier version.

## Non-negotiable constants and counts

Preserve all values in the fixed constant registry. In particular:

- National Settlement range `-100` to `+100`, opening `+25`, opening momentum `-1`
- momentum range `-5` to `+5`, two balance points per momentum each monthly update, maximum ten
- seven-day stage confirmation, five-point return margin, route clamp `-60` to `+60`, six-month commitment review
- Social Consent `55`
- National Readiness opening display `15`
- British, Vatican, American, and German Leverage `45`, `25`, `5`, `5`
- Dáil `153` formal seats and `152` routine confidence votes
- Fianna Fáil `77` formal and `76` routine, Fine Gael predecessors `59`, Labour `8`, others `9`
- National Provision components `55`, `25`, `40`, `30`, displayed as `38`
- Readiness components `25`, `8`, `20`, `12`, `5`, `5`, `30`, displayed as `15`
- Neutrality Integrity `72`
- Northern opening `U5 N40 L30 B10 S45 I10`
- exactly three persistent route-spirit families
- exactly thirteen decision categories, 140 decision actions, 54 mission families
- global active mission caps `8`, `10`, and conditional `12`
- command power action cost never above `60`
- eighteen historical chains, eighteen political crises, twelve foreign-reaction families, at least 236 consequential flavour events
- exactly 30 durable AI profiles and ten temporary overlays
- exactly 12 foreign actor families and 12 response action classes
- exactly 32 achievements
- exact Part 6 asset budgets and source-clearance workflow
- Northern cores only after integration stage 5 and final review
- the complete canonical Dillon gate from Part 4

Centralise tunable values in documented constants or helpers. A tuning file can expose a fixed planning value without changing its meaning or default.

## Implementation order

### Phase 1: repository and precedent audit

Before editing gameplay files:

- map existing Ireland tag, history, states, parties, leaders, ideas, focus loading, events, decisions, AI, flags, localisation, GFX, achievements, and scripted helpers
- identify conflicts with existing Ireland Total Overhaul content
- inspect local vanilla examples for balance of power, national focuses, decisions, timed missions, events, AI strategy, dynamic modifiers, scripted localisation, scripted GUI, achievements, cosmetic tags, flags, characters, and occupation or integration systems
- write an implementation touchpoint map under `docs/plans/ireland_focus_tree/`
- decide which existing assets and helpers can be reused only after exact compatibility checks

Do not begin the focus tree until the country package and shared system ownership are known.

### Phase 2: identifiers, constants, regions, variables, flags, and cleanup helpers

Create a stable `slopx` ID registry for:

- focus tree and focus nodes
- event namespaces and event families
- decision categories, actions, and missions
- ideas, dynamic modifiers, laws, advisors, characters, traits, AI strategies, achievements, scripted localisation, GUI sprites, cosmetic tags, flags, variables, event targets, and state flags
- the 30 AI profiles, ten overlays, twelve foreign actor families, twelve reaction action classes, 32 achievements, three persistent spirit families, 17 law ladders, and named route conclusions

Implement reusable scripted effects, triggers, constants, and cleanup helpers where repeated logic exists. Helpers must have documented scope, inputs, outputs, side effects, call sites, and cleanup. Do not create helper scaffolding without call sites.

Register the named regional objective groups from Part 5. State membership must match the current map and be documented. Northern regions remain separate from southern administrative regions until a lawful agreement, war, occupation, or transition state connects them.

### Phase 3: Ireland starting country package

Implement January 1936 starting state:

- correct government, parties, formal Dáil arithmetic, routine vote arithmetic, President, Taoiseach, party leaders, parliamentary leaders, cabinet figures, military command, security figures, and historical actors
- the opening National Settlement at `+25` with momentum `-1`
- opening companion, stakeholder, leverage, Provision, and Readiness values
- starting laws and the three opening persistent spirit families
- starting army, equipment, command, Air Corps, maritime, transport, shipping, intelligence, and industrial limitations described in Parts 1 and 4
- no hidden party or impossible sovereignty at game start
- no free units, factories, shipping, fuel, equipment, command capacity, or Northern control

Real leaders require sourced portraits. Collective offices require institutional identity and must not invent a personal ruler.

### Phase 4: National Settlement, parliament, elections, offices, and organised society

Implement the National Settlement as the central adaptive struggle. Use the seven stages, hysteresis, momentum, stakeholder contributions, route transformations, crisis states, and six-month review from Part 2.

The system must connect to:

- focuses
- decisions and missions
- elections and government formation
- leaders and offices
- parties and Dáil seats
- laws and emergency powers
- Church domains and service dependency
- Labour Organisation and Movement Unity
- Rural Organisation and Agrarian Cohesion
- security loyalty and republican network strength
- events, crises, AI, route access, failures, recovery, and conclusions

Implement formal seats separately from routine confidence votes. Party popularity never substitutes for seats. Party leader, parliamentary leader, Taoiseach, President, cabinet office, military office, movement office, and collective office remain separate.

Implement the 1937 constitutional plebiscite and election as separate calculations in one sequence. Implement valid coalition, confidence and supply, minority government, caretaker, presidential refusal, dissolution, Seanad, cabinet, succession, and election lifecycles.

Church influence remains distributed. Domestic Church domains never merge with Vatican Leverage. Constitutional vocational councils remain subordinate to elections, the Dáil, courts, free associations, labour freedom, and minority safeguards unless a named failure transforms the route.

### Phase 5: focus tree architecture

Build one large, non-linear Ireland focus tree from the architecture maps. Do not create separate disconnected trees for each ideology.

The tree must include:

- shared 1936 opening and national survey
- 1937 constitutional gateway
- 1938 sovereignty, trade, and Treaty Port gateway
- Fianna Fáil, Lemass, Fine Gael, Costello, Dillon, Norton, Clann, and constitutional vocational routes
- IRA civil and Army Council routes
- Republican Congress plural and vanguard routes
- O'Duffy personal and institutional corporate routes
- clerical and producer-state transformations
- dated Ailtirí route
- serious public cultural lane
- High Kingship, Five Provinces, Otherworld, and convergence routes with exact reveal rules
- agrarian, industrial, social, vocational, command, corporate, clerical, Ailtirí, royal, provincial, and compact economic support
- army, reserve, coastwatch, coastal defence, air warning, maritime, intelligence, and operational planning support
- neutrality, Allied, Axis, British, American, Vatican, small-state, Atlantic, diaspora, and Celtic diplomacy
- Northern negotiation, deferment, federation, labour settlement, unitary settlement, wartime bargain, plebiscite, coercive conflict, occupation, and integration
- postwar reconstruction, demobilisation, republic or association, regional order, and route conclusions

Branches must interact. Political commitments change the economy, defence, diplomacy, Northern, internal, and late-game lanes. Support lanes must feed multiple routes and receive route-specific variants.

Every real branch needs several focuses or focus groups, at least one meaningful choice, at least one mechanical unlock, route-specific AI, events, asset direction, and a visible payoff. Avoid one-focus or two-focus fake branches.

Focus rewards must be varied. Use buildings, infrastructure, rail, supply, ports, airbases, anti-air, forts, equipment, production lines, research, units, templates, advisors, leaders, decisions, missions, laws, identities, claims, diplomatic agreements, mechanic changes, and staged idea transformations where appropriate. Do not fill the tree with political power, stability, war support, tiny modifiers, or new ideas.

Stay within the three persistent route-spirit families. Modify, replace, merge, or corrupt those spirits instead of creating route-spirit spam.

Hidden focuses remain invisible until the correct reveal stage. An impossible branch requires the explicit hidden-content game rule and valid evidence. Serious culture remains valuable when no hidden route appears.

### Phase 6: National Provision, National Readiness, neutrality, leverage, and Northern systems

Implement the four-component National Provision system and seven-component National Readiness system. Show components and bottlenecks through the approved National Conditions Panel or readable dynamic localisation.

A high average cannot hide a critical component. Apply every cap and collapse rule from Part 4. Projects require delivery, maintenance, regional capacity, and physical inputs. Political victory does not create material capacity.

Implement Neutrality Integrity and the Neutrality Ledger as active gameplay. Cover airspace, shipping, mines, rescue, internment, intelligence, weather, trade, access, censorship, border activity, public legitimacy, violations, covert cooperation, and escalation. Partner cooperation depth and leverage remain source-specific.

Implement every foreign agreement with actor, delivery path, obligations, command limit, safeguards, exposure, review, withdrawal, dependency, and sponsor-collapse cleanup.

Implement the Northern Settlement Ledger with six separate values. Northern institutions, Britain, unionists, nationalists, labour, industry, local government, religion, education, policing, security, finance, and services remain distinct.

Claims, control, occupation, transition, settlement, integration, and cores remain separate. A focus or event cannot grant Northern cores. Stage 5 and final regional review are mandatory.

### Phase 7: decisions and missions

Follow `prompts/ireland_focus_tree_decision_mission_prompt.md` and the Part 5 decision map.

Implement exactly thirteen evolving categories, 140 mapped actions, and 54 mission families. Categories must hide obsolete actions, enforce route and phase visibility, respect category caps, reserve critical slots, and clean stale targets.

Use dynamic costs across political power, command power, XP, manpower, equipment, trucks, trains, convoys, fuel, factories, consumer-goods burden, local support, legitimacy, leverage, exposure, tied units, map control, and time. Political power is not the default price.

Every mission needs:

- named region or target
- dynamic duration
- visible objective
- automatic completion where the work itself is the objective
- full success
- partial success
- failure
- escalation
- cooldown or repetition control
- cleanup
- route-aware AI

Do not let cancellation refund more than 70 percent of recoverable physical inputs. Do not refund political, exposure, leverage, or reputation costs unless a mapped lifecycle allows it.

### Phase 8: event programme

Implement the event architecture from Part 5 and the event map.

- eighteen historical chain families
- eighteen political crisis families
- twelve foreign reaction families
- at least 236 route, regional, social, cultural, military, economic, Church, labour, agrarian, Northern, and institutional flavour events
- route conclusions and 180-day consolidation sequences

Flavour events are mandatory and continuous. Each one must provide historical or cultural context, a meaningful choice, and a noticeable system effect. Do not reserve events for milestones.

Use event memory to prevent repetition, preserve decisions, alter later options, and support achievements. Severe events must not disappear into a generic digest.

Implement the twelve foreign actor families, twelve response action classes, 14-day window, response score, capability limits, four-event visible maximum, and digest rules. Britain and Northern institutions remain separate. Vatican and domestic Church state remain separate. Diaspora and American state leverage remain separate.

Final player-facing event text belongs to implementation. Follow the route voices and ethical rules. Do not use cheap humour around sectarian conflict, antisemitism, repression, political killing, or mass suffering.

### Phase 9: routes, failures, recovery, and conclusions

Implement every route in the route coverage matrix. A route must have:

- valid political and historical access
- route-specific focus architecture
- decisions and missions
- event families and flavour
- AI profile
- material and foreign policy
- Northern policy
- leader, office, party, law, idea, and identity lifecycle
- failure states
- recovery paths
- conclusion review
- achievement hooks
- asset package

Authoritarian routes must show coercion, repression, antisemitism where historically relevant, exclusion, service capture, foreign dependency, army reliability, and institutional cost directly.

A route conclusion is a process. Test every mandatory system, fire institutional and foreign responses, activate identity, run the 180-day consolidation mission, then resolve success, partial success, or failure. No conclusion can hide an unresolved crisis, occupation, law, vacancy, obligation, or disqualifier.

### Phase 10: AI

Implement the 30 profile roster and ten overlays from the AI matrix.

AI must understand:

- route permission and commitment
- focus path and support lanes
- mission queue, reserved slots, Action Burden, feasibility, partial success, cancellation, recovery, and repetition penalties
- government formation, offices, laws, and elections
- Provision and Readiness targets
- neutrality, partner depth, leverage, obligations, and war gates
- Northern settlement, occupation, integration, rights, and cores
- postwar transition and conclusions
- hidden reveal and game-rule permissions

Historical AI has zero weight for concealed commitments. An AI cannot become O'Duffy, Ailtirí, royal, provincial, Otherworld, or convergence through generic focus weighting. It needs the exact route state.

Use MTTH entries or central weight helpers when they reduce repeated `ai_will_do` logic. Keep weights readable and documented.

### Phase 11: achievements

Follow `prompts/ireland_focus_tree_achievement_prompt.md` and implement the exact 32-entry matrix.

Track campaign history, maxima, minima, continuous periods, offices, laws, misconduct, sponsor dependence, incidents, evidence provenance, Northern stages, route conclusions, and disqualifiers. Do not use end-state snapshots where the matrix requires history.

Implement normal, grey, and not-eligible icon states with filenames matching the full achievement IDs. Hidden progress must not expose unrevealed routes.

### Phase 12: assets, GUI, animation, text research, and localisation

Follow the asset and text-audio prompts.

- source the 60 real-person portraits
- research and clear the 40 historical symbol and document packages
- apply C0 through C4 clearance, eleven source tiers, and per-item manifests
- produce one historical base flag set and 18 alternate sets
- produce the full icon budget and exactly 120 event images with the 69 sourced and 51 generated split
- implement exactly three approved scripted GUI surfaces
- implement exactly seven approved animations with independent source frames and static fallbacks
- keep audio optional and limited to three briefs

Do not generate real leaders, historical flags, or attested historical symbols. Do not use reenactments, film stills, fake documents, or unclear rights as historical substitutes.

Write final localisation only during implementation. Keep costs icon-first, requirements readable, dynamic values explicit, hidden content concealed, and route voices distinct. Final wording must use dynamic actors, states, values, routes, dates, and consequences where useful.

### Phase 13: validation and audits

Before completion, run:

- parser and error-log checks
- focus-tree loading, prerequisite, bypass, mutual exclusion, search-filter, and layout review
- decision and mission visibility, cost, objective, partial result, failure, cleanup, AI, and exploit review
- event namespace, trigger, scope, option, follow-up, picture, localisation, and on-action review
- country package, leader, party, history, state, flag, identity, claim, core, occupation, and integration review
- scripted helper, variable, flag, event-target, and cleanup review
- AI route, queue, hidden permission, sponsor collapse, Northern, war, and conclusion scenarios
- achievement tracking and disqualifier tests
- asset path, sprite, dimensions, transparency, DDS, source, licence, clearance, and fallback review
- localisation key, encoding, duplicate, scripted localisation, dynamic value, and hidden-text review
- historical and nonhistorical playthroughs
- major route, failure, recovery, postwar, Northern, and hidden-route scenarios

Use the project audit subagents when available. Review every subagent patch and handoff. The parent implementation agent remains responsible for integration and completion claims.

## Required validation scenarios

At minimum test:

1. historical de Valera from 1936 through postwar emergency expiry
2. failed and successful 1937 Constitution outcomes
3. hung Dáil and lawful coalition formation
4. early Lemass succession and blocked succession
5. Cosgrave, Mulcahy, Costello, Dillon, Norton, and Clann routes
6. National Provision dual bottleneck and component collapse
7. readiness mobilisation without equipment and with full supply
8. six coastwatch sectors and 83-post historical representation
9. strict neutrality, discreet cooperation, severe incidents, sponsor pressure, and direct attack
10. every Dillon gate failure plus valid war entry and demobilisation
11. Northern negotiation, federation, unitary settlement, lawful deferment, coercive war, occupation, integration stage 5, and final review
12. IRA civil and GHQ outcomes
13. Congress plural and vanguard outcomes
14. O'Duffy failure, succession, corporate order, and restoration
15. clerical, producer, and emergency restoration outcomes
16. Ailtirí dates, exposure, sponsor collapse, and conclusion
17. serious culture with no hidden reveal
18. false lead, constitutional High King, sacral High King, federal provinces, pentarchy, compact, dominion, containment, and convergence
19. historical AI zero hidden commitment
20. sponsor defeat, invalid delivery, debt, exposure, and recovery
21. all 32 achievements, including every disqualifier
22. route change, leader death, election defeat, coalition collapse, war entry, demobilisation, occupation end, cultural false lead, compact breach, and conclusion cleanup

## Completion report

Do not claim completion until:

- every canonical route and support branch is implemented
- every fixed count and constant is preserved
- every required visible asset is final or explicitly blocked in a non-completion report
- no placeholder, fallback, shortened substitute, generic route, or free reward remains
- every major validation scenario passes
- every audit finding is fixed or transparently reported
- documentation matches implementation
- the offline wiki and vanilla precedent audit has been performed

Report exact files changed, systems implemented, assets produced, validation run, skipped validation and reason, known limitations, and any requirement that remains blocked. A blocked requirement means the feature is not complete.
