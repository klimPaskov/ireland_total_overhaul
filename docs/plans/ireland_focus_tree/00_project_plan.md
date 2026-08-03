# Ireland Focus Tree Planning Program

Feature slug: `ireland_focus_tree`

Status at this planning checkpoint: Parts 1 through 6 complete and Part 7 canonical candidate assembled. The mandatory improvement-loop worker has since completed with `fork_context=false`; implementation follow-up remains incomplete because source clearance, engine-reference checks, and required runtime scenarios are still open. See `docs/plans/ireland_focus_tree/source_of_truth_map.md` for the normalized status ledger and `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md` for the current implementation evidence snapshot.

This file is a working program plan. It is not part of the final player-facing design and it contains no final localisation.

## Planning objective

Create one canonical, research-grounded planning package for a complete Ireland gameplay overhaul in Ireland Total Overhaul. The package must give the implementation agent enough design direction to build a large non-linear national focus tree, a living internal political struggle, route-linked decision and mission systems, extensive event chains, route-aware AI, distinct country identities, achievement tracking, and a complete asset and research handoff.

The final source of truth will live under:

```text
docs/specs/ireland_focus_tree/
```

Working notes, continuation state, improvement-loop addenda, and implementation handoffs will live under:

```text
docs/plans/ireland_focus_tree/
```

## Design rules carried through every part

1. The design begins from Ireland's real political, economic, military, religious, labour, and diplomatic problems between 1936 and 1945.
2. Every major claim is tagged as documented history, plausible speculation, or deliberate absurdity.
3. Alternate-history routes grow from real factions, institutions, personalities, tensions, and strategic choices.
4. The focus tree is non-linear. Support branches can interact with several political routes, and route commitments alter the content of military, economic, diplomatic, internal, and expansion branches.
5. Every major route must create active gameplay, route-specific decisions, events, AI behavior, tradeoffs, failure states, country identity changes, and a meaningful conclusion.
6. The internal struggle mechanic must connect to leaders, parties, laws, focuses, decisions, missions, events, crises, AI, and route access.
7. Decisions and missions must represent concrete action. They will use equipment, manpower, convoys, trains, factories, stability, war support, local political support, unit placement, state control, deadlines, diplomatic access, and other fitting costs instead of relying mainly on political power.
8. Events are a required gameplay layer. Flavour events will carry historical and cultural context, offer meaningful choices, and affect visible systems.
9. Northern Ireland will be treated as a populated and politically divided society. It will never be a free territorial reward or an instant core package.
10. Neutrality will be active policy that requires diplomatic management, military preparation, intelligence choices, maritime control, emergency legislation, and responses to violations.
11. Historical routes will be playable without becoming guaranteed success paths. Alternate routes will remain difficult in proportion to their historical marginality.
12. Hidden absurd routes will be culturally grounded, hard to discover, mechanically complete, and integrated with the normal systems. They will not be detached meme branches.
13. Real leaders, historical flags, and attested symbols will be assigned to sourced asset research. Fictional, alternate, symbolic, or supernatural identities will be assigned to generated asset work.
14. The planning files will define localisation direction only. They will not provide final focus names, event prose, option text, achievement titles, or other pasteable localisation.
15. The final package will contain no unresolved placeholders, shortened substitute routes, fallback designs, or undeclared simplifications.
16. The final goal prompt will point to the canonical files and stay below 4,000 characters.
17. The mandatory improvement-loop pass runs only after the full package is assembled. Its completed report and finding disposition are recorded under `docs/plans/ireland_focus_tree/improvement_loop/`; implementation findings remain subject to the separate completion audit.

## Part sequence

### Part 1: Historical research and overall gameplay architecture

Deliverables:

- research notes with confidence and classification rules
- historical timeline and actor map
- strategic constraints and design red lines
- overall gameplay promise
- starting situation
- high-level internal struggle model
- full macro focus-tree architecture
- route family overview
- pacing and failure philosophy
- architecture map

Part 1 must stop before detailed focus-by-focus route drafting.

### Part 2: Constitutional politics and the adaptive internal struggle

Deliverables:

- full adaptive balance-of-power or equivalent mechanic
- thresholds, states, components, crisis behavior, and route transformations
- Fianna Fáil route family
- Fine Gael route family
- James Dillon and pro-Allied constitutional route
- Labour parliamentary route
- church influence and vocational politics as cross-route systems
- elections, coalition crises, leader changes, party changes, laws, advisors, and political failure states
- political focus architecture and route interaction map

### Part 3: Revolutionary, corporatist, and hidden cultural routes

Deliverables:

- IRA Army Council route
- Republican Congress and social-republican route
- Eoin O'Duffy and National Corporate Party route
- Ailtirí na hAiséirghe hidden wartime route
- language, Gaelic revival, folklore, regional identity, and old-institution systems
- hidden mythic and absurd restoration route families
- reveal conditions, disqualifiers, AI restrictions, country identity changes, extreme rewards, and failure states
- culturally grounded secret route map

### Part 4: Economy, defence, diplomacy, Northern Ireland, expansion, and late game

Deliverables:

- agrarian, protectionist, industrial, emergency supply, shipping, fuel, and infrastructure routes
- army, reserves, local defence, coast watching, coastal artillery, air defence, marine service, intelligence, and operational planning routes
- active neutrality, Allied alignment, Axis opportunism, Atlantic diplomacy, Vatican and small-state diplomacy, and diaspora routes
- Northern Ireland negotiation, wartime bargain, federal settlement, coercive reunification, and postwar integration systems
- external expansion and Celtic-order routes where justified
- late-game branches and route conclusions
- full support-branch and convergence map

### Part 5: Decisions, missions, events, ideas, and country identity lifecycles

Deliverables:

- decision category families
- timed mission families
- dynamic cost and scaling model
- map objectives and target regions
- success, partial success, failure, escalation, and cleanup rules
- historical event chains
- political crisis chains
- foreign reaction chains
- route event families
- extensive route-specific flavour event plans
- idea and national spirit lifecycle tables
- leader, advisor, party, law, flag, cosmetic name, and country identity matrices

### Part 6: AI, achievements, assets, research prompts, and localisation direction

Deliverables:

- route-specific AI strategy matrix
- AI decision and mission behavior
- foreign actor reaction matrix
- achievement set and tracking matrix
- asset family ledger
- portrait, flag, symbol, icon, event image, GUI, and animation requirements
- sourced asset research list
- generated asset list
- text, quote, cultural remark, and audio research directions
- localisation tone and dynamic text direction
- decision and mission prompt
- asset prompt
- text and audio research prompt
- achievement prompt

### Part 7: Canonical cleanup, improvement loop, and implementation handoff

Deliverables:

- complete coding prompt
- complete goal prompt
- source-of-truth index
- route coverage table
- mechanic and event maps
- contradiction and repetition cleanup
- mandatory improvement-loop pass
- resolution of every accepted finding
- final canonical package under `docs/specs/ireland_focus_tree/`
- final zip containing every specification part, map, matrix, research note, and prompt

## Working file map

```text
docs/plans/ireland_focus_tree/
  00_project_plan.md
  project_status.md
  improvement_loop/
  subagent_handoffs/

docs/specs/ireland_focus_tree/
  ireland_focus_tree_index.md
  ireland_focus_tree_spec_part_1_research_and_architecture.md
  ireland_focus_tree_spec_part_2_constitutional_politics.md
  ireland_focus_tree_spec_part_3_radical_and_hidden_routes.md
  ireland_focus_tree_spec_part_4_statecraft_and_war.md
  ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md
  ireland_focus_tree_spec_part_6_ai_assets_achievements_and_text.md
  research/
  maps/
  matrices/
  prompts/
```

Only files completed in the current part should exist. Future file names above are reserved to prevent later path drift.

## Accepted starting design decisions

1. The central political mechanic uses the working label `The National Settlement`. This is not final localisation.
2. Its initial visible conflict is between constitutional state authority and the unfinished revolutionary mandate.
3. The mechanic adapts after route commitment. Its labels, stakeholders, effects, and crisis states change to reflect the route that took control.
4. A small number of companion values will support the central struggle. The current working set is Social Consent, National Readiness, and source-specific External Leverage. Part 2 will decide exact presentation and whether any value is merged.
5. Fianna Fáil, Fine Gael, Labour, republican, corporatist, and hidden cultural route families all begin from the same national problems. No route receives an isolated alternate-history tree detached from the shared opening.
6. James Dillon's opposition to neutrality becomes a difficult constitutional pro-Allied route, not a generic Fine Gael default.
7. Eoin O'Duffy provides the historically earlier corporatist opening. Ailtirí na hAiséirghe is an emergent wartime route and cannot appear as an ordinary 1936 party choice.
8. Church influence is a cross-route power centre and policy system. A clerical or vocational state must emerge through escalating constitutional and social choices rather than a sudden theocratic switch.
9. Labour begins as a parliamentary force that broadly supports neutrality. A workers' republic requires a merger or alliance with radical republican and labour currents, not a default Labour election outcome.
10. Northern Ireland routes require negotiation, consent, coercion, or war, followed by administration and integration. Full cores are never granted automatically.
11. Neutrality can include covert Allied assistance, weather reporting, operational liaison, maritime arrangements, and humanitarian action while still creating political risk.
12. A German or Axis alignment route is possible only through marginal actors, major crisis, and deliberate escalation. It must carry severe diplomatic and domestic consequences.
13. The hidden absurd layer will use Irish mythology, the Gaelic revival, provincial identity, language politics, folklore, and old institutions. Full supernatural or impossible outcomes will be labelled deliberate absurdity.
14. Important route identities can change the country name, flag, leader, ruling party, advisor roster, law package, and available decisions. These changes must be visible and asset-backed.

## Historical constraints that later parts cannot ignore

- Neutrality had broad public and cross-party support during the Emergency.
- Ireland's sovereignty was strengthened by the 1938 agreements and return of the Treaty Ports, but coastal defence capacity remained weak.
- The state was prepared to resist invasion by either belligerent and also maintained secret military contacts with Britain and the United States for an Axis invasion contingency.
- The army expanded rapidly during the Emergency but remained under-equipped.
- The economy was heavily rural and dependent on vulnerable external trade and shipping.
- The 1937 Constitution strengthened the state, embedded a Catholic social context, and created a legal basis that wartime emergency government could expand.
- The Civil War split remained embedded in the party system and security politics.
- The IRA was capable of violence and subversion but was not close to normal electoral power in 1936.
- Fascist movements were marginal. O'Duffy's movement had declined, and Ailtirí emerged during the war.
- Labour politics included parliamentary trade unionism and more radical socialist republican currents that were distinct from one another.
- Northern Ireland had a unionist government, a nationalist minority, intense political discrimination disputes, strategic industry, and its own wartime pressures.
- A reunification settlement must address unionist resistance, nationalist expectations, policing, institutions, industry, debt, defence, and foreign guarantees.
- Mythic kingship, supernatural restoration, and impossible Celtic expansion are not documented political programmes of the period. They must remain deliberately absurd branches with culturally grounded prerequisites.

## Questions reserved for later parts

1. Whether the internal struggle is presented through the native balance-of-power interface, a decision category with dynamic scripted localisation, or a hybrid scripted GUI.
2. The exact number and labels of mechanic thresholds.
3. The exact focus count and focus durations.
4. Whether a Fine Gael constitutional route begins with W. T. Cosgrave throughout the 1936 start or creates an earlier leadership contest that can accelerate Richard Mulcahy or John A. Costello.
5. The exact leader and advisor roster for every route.
6. The precise relationship between parliamentary Labour, the Republican Congress legacy, and other radical left actors.
7. The exact map requirements and settlement forms for every Northern Ireland outcome.
8. The number and structure of hidden absurd route families.
9. Which major route reveals merit scripted GUI animation and which should remain static for clarity.
10. Which moments justify sourced quotes, cultural remarks, or audio.

## Tooling and repository state

The active workspace is the Ireland Total Overhaul Git repository. Implementation files, source-side assets, manifests, and current audit records are present in the worktree; no commit is being created by this status update because the worktree also contains unrelated user changes. Local structural validation and the required read-only audit roles have run, but source clearance and the fresh-1936/live engine/scenario programme remain explicit completion gates. The current status authority is `docs/plans/ireland_focus_tree/source_of_truth_map.md`.
