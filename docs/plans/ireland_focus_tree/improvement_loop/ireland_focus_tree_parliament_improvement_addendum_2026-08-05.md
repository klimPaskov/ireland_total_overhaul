# Ireland focus tree and parliament improvement-loop addendum

Feature slug: `ireland_focus_tree`

Addendum date: 2026-08-05

Status: superseded planning handoff; implemented and reconciled 2026-08-09

This is a historical planning snapshot. Its accepted focus-tree and Parliament
recommendations are implemented and recorded in
`docs/plans/ireland_focus_tree/focus_tree_parliament_completion_2026-08-09.md`.
The current source has 150 focuses, one root, and 158 visual connectors. The
final MCP inspection reports zero crossings, node intersections, long
connectors, spacing defects, or Ireland-local diagnostics. The Parliament
header fits its 510 by 198 host and renders without overlap at both target
resolutions. Historical counts, captures, and recommendations below remain
useful provenance but are not current implementation claims.

Scope of this pass: documentation only. No gameplay, GUI, localisation, focus,
asset, or script file was changed.

## Decision summary

The current worktree needs a consolidation and integration pass, not another
route family. The existing design records describe a deep system, but the
current source does not present that depth coherently:

- The focus source contains 226 unique focus blocks, 37 top-level roots, and no
  formal branch blocks in the MCP projection. This makes most of the tree
  selectable as independent opening material instead of making the shared
  constitutional crisis the player’s first decision.
- The focus inspection at revision
  `40a4b0fc84d2b6007b971b2019927e4cdf695bf196496b8eaf2f4638118ed12f` reports
  257 connectors, one crossing, 14 blocking focus diagnostics, total
  horizontal connector span 450, total vertical span 363, and total Manhattan
  span 813. The renderer reports a 5080 by 3366 output. The raw
  `longConnectorCount` is zero under the tool threshold, but the reported
  linear-detour and zigzag diagnostics still match the user’s “long connector”
  complaint.
- Shared reward profiles are called 216 times for 226 focuses: institutional
  96, economic 20, military 13, maritime 8, air 1, technical 4, diplomatic
  10, cultural 9, radical 25, recovery 6, and capstone 24. This is a strong
  signal of repeated wrapper rewards rather than 226 distinct decisions.
- The current decision source contains 14 category registrations, 144 action
  blocks, and 54 mission blocks. The canonical documents still state 13
  categories and 140 actions. That count drift must be resolved before the
  next implementation commit; it must not be silently accepted as a new
  scope target.
- The parliament backend has real variables and staged decisions, but the
  visible panel is not an interaction surface. `ireland_parliament_panel_window`
  is a 510 by 286 collection of static text and icon rows. Its scripted-GUI
  registration has no `effects`, `triggers`, or `properties`, and its AI check
  is `always = no`.

The recommended implementation target is a single shared spine, 2–4 meaningful
early choices, route commitment before specialised branches, route-specific
reward contracts, progressive action disclosure, and a parliament surface that
projects and advances the same ledgers used by decisions and AI. Do not add a
fallback tree, a parallel seat system, or decorative buttons.

## Current evidence and authority

### Read-only evidence captured for this addendum

| Surface | Current evidence | Planning consequence |
| --- | --- | --- |
| Focus source | `common/national_focus/ireland_focus_tree.txt`, 226 focus blocks, 226 unique IDs, 37 roots, no duplicate coordinates or missing prerequisite references in the local structural scan | Consolidate the graph before tuning its presentation; do not interpret unique IDs as unique gameplay decisions |
| Focus MCP | Revision `40a4b0fc84d2b6007b971b2019927e4cdf695bf196496b8eaf2f4638118ed12f`; validation false with 14 blocking focus diagnostics; crossing count 1; node intersection count 0 | The prior “layout clean” records are stale for this worktree revision |
| Focus MCP render | `FOCUS_RENDERED`; layout hash `b465c75219c59f9268f626b3cc4a17a609918e9a576ed3be5b0b313e33ed8eea`; HTML/SVG/JSON artifacts produced | The current graph is inspectable, but not acceptable as the final layout |
| Shared reward helpers | `common/scripted_effects/ireland_focus_rewards.txt` and `common/script_constants/ireland_focus_reward_constants.txt` | Reward migration must replace generic profile calls with route contracts and centralised round tuning |
| Decisions | `common/decisions/ireland_decisions.txt`; 144 action blocks and 54 mission blocks in the current source | Reconcile the 144/140 drift and use one progressive lifecycle rather than exposing all actions through broad reveal triggers |
| Decision categories | `common/decisions/categories/ireland_categories.txt`; 14 registered categories, including `ireland_marine_service` | Decide whether the empty marine category is a dormant reserved category or a real phase-owned category |
| Parliament GUI | `interface/ireland_conditions.gui`; 22 elements were inspected in scenario `ireland_audit` | Convert the read-only panel into a state-and-action surface without duplicating decision effects |
| Parliament GUI MCP | Shared revision `d8aa657a3a9f6a122d41b9c20132831106c133d2836e4c7adba002b9ba5f374d`; 22 inspected elements; source graph passed; scenario validation false; 8 unresolved dynamic values, 2 missing fidelity items, no visible-overlap diagnostic | The values are wired as text, but current offline inspection does not prove usable interaction or resolved runtime rendering |
| Parliament backend | `common/scripted_effects/ireland_parliament.txt`, `common/scripted_triggers/ireland_parliament.txt`, and the first four settlement actions | Reuse the existing ledgers and stage flags; repair the ownership and presentation contract instead of inventing another mechanic |

The canonical design remains authoritative for fixed values, route identities,
H/P/A boundaries, Northern separation, mission caps, lifecycle rules, and AI
profiles. The current source is authoritative for what is actually present and
therefore exposes the implementation gaps this addendum must address.

The older records claiming 216 focuses, 197 connectors, zero Ireland-local
layout diagnostics, or a completed static improvement loop are historical
records from earlier workspace revisions. They are not evidence against the
current MCP revision and must not be used to close this handoff.

## Non-negotiable design decisions

These are the recommended defaults. Items marked “approval required” cannot be
completed by an implementation agent without the corresponding choice.

| Decision | Recommended default | Approval required because |
| --- | --- | --- |
| Final focus count | Consolidate to a 140–150 node envelope, with a hard ceiling of 156. The working target is 144. | The canonical package names many historical and absurd routes; exact survivor/merge mapping changes route pacing and asset ownership |
| Early tree shape | One visible shared opener, then four early lanes: constitutional authority, material survival, society/culture, and security/neutrality. Leader and hidden routes reveal later. | Keeping all named routes as day-one roots reproduces the reported disconnected tree |
| Seat model | Keep the existing 153 formal-seat / 152 routine-vote Dáil model and the existing 60-seat Seanad ledger. No second or ideology-derived seat model. | The UI choice is whether Seanad arithmetic is a primary visible row or a supporting modifier |
| Parliament authority | Decisions remain the authoritative cost/effect/AI owner. The GUI selects, previews, and invokes only the approved action path; it must not duplicate decision effects. | The local engine reference must confirm how a scripted GUI can route to a native decision or a request-consumer effect |
| Non-Dáil routes | Transform the panel into an explicit institutional mode for vocational, corporate, or extra-parliamentary authority; do not leave stale Dáil labels visible. | The canonical route maps differ on whether Dáil review survives, so a mode roster is required |
| Action count drift | Reconcile current 144 actions against the canonical 140-action registry before implementation. Merge or retire four named actions only after the registry owner identifies them. | Silently changing the count would invalidate the existing crosswalks and mission/category matrices |
| Asset and text work | Keep source clearance, final art, final localisation, and animation outside this addendum. Record blockers; do not substitute placeholders. | Those are separate production decisions and were explicitly excluded from this pass |

## Workstream 1: consolidate the focus graph

### Target topology

The shared spine must carry the player through `ireland_state_still_defined`,
`ireland_institutional_survey`, and `ireland_national_settlement`. The first
meaningful route choice must occur after the settlement is established, within
the first 70 days for normal focus pacing. The opening should expose no more
than four broad lanes and no hidden A-route node.

Use this working node budget for the 144-node target. It is a budget for
decision-bearing focus blocks, not permission to add filler nodes.

| Functional cluster | Working budget | Required payoff |
| --- | ---: | --- |
| Shared opening and National Settlement | 10 | establishes the central state and first cross-system decision |
| Constitutional, election, and parliament spine | 16 | creates the Dáil/Seanad stages, election gates, government formation, and review |
| Government and coalition routes | 28 | preserves Fianna Fáil/de Valera, Lemass, Fine Gael/Cosgrave/Mulcahy/Costello, Dillon, Labour, and Clann identities through shorter trunks |
| Organised society, Church, culture, and vocational route | 12 | keeps public institutions and Dáil-sovereignty tradeoffs valuable without duplicating survey/review nodes |
| Provision and economy | 10 | converts material weaknesses into route choices and action unlocks |
| Readiness, defence, and maritime | 12 | turns command, equipment, warning, and ports into route dependencies and rewards |
| Neutrality and foreign leverage | 10 | gives each sponsor posture a distinct cost, access, and sovereignty consequence |
| Northern settlement | 12 | preserves confidence, local actors, British position, security, occupation, integration, and delayed cores |
| Republican, IRA, and Congress routes | 12 | separates civil authority, army authority, plural Congress, and vanguard capture |
| O’Duffy, corporate, and Ailtirí routes | 8 | retains personal-command, producer/corporate, and cell-state identities without parallel ladders |
| Hidden, royal, five-province, and Otherworld routes | 8 | keeps evidence and H/P/A escalation gated and out of the opening |
| Recovery and conclusions | 6 | gives failure, restoration, route review, and conclusion states one visible endpoint |
| **Total working target** | **144** | **No new route family** |

### Concrete consolidation rules

1. Attach every current day-one root other than
   `ireland_state_still_defined` to the shared spine or to an explicit later
   reveal. The current 37 roots are an audit failure, not a route requirement.
2. Preserve one route anchor per meaningful choice, one interaction node, one
   support-lane dependency, and one conclusion/recovery node. Merge any chain
   that only repeats “review”, “audit”, “consultation”, or generic institution
   language without changing a value, unlocking an action, changing an idea,
   or creating a new dependency.
3. Replace long visual jumps with local parent-child placement. The following
   current diagnostics are mandatory rewrite targets, not cosmetic observations:

   | Current edge or chain | Required action |
   | --- | --- |
   | `ireland_state_still_defined` → `ireland_institutional_survey` | place as a one-row vertical spine edge |
   | `ireland_church_labour_consultation` → `ireland_minority_guarantees` | keep the policy choice adjacent to its parent or merge the consultation into the guarantee node |
   | `ireland_public_order_review` → `ireland_language_service` | remove the horizontal detour; retain the language consequence as a society payoff |
   | `ireland_election_timetable` → `ireland_constitutional_draft` | remove the three-row gap; make the draft a direct constitutional gate |
   | `ireland_1938_trade_settlement` → `ireland_treaty_port_transfer` | merge duplicated trade/port preparation or make the transfer a direct consequence |
   | `ireland_de_valera_stewardship` → `ireland_secure_plebiscite_mandate` → `ireland_govern_through_dail` → `ireland_constitutional_stewardship` | make a straight route trunk; the four nodes must express four distinct commitments, not four visual turns |
   | `ireland_republican_legitimacy` → reconciliation chain | remove the repeated horizontal stepping in `de_valera_reconciliation`, `distinguish_prisoners`, and `amnesty_under_law` |
   | `ireland_dail_supremacy_clause` → `ireland_council_government_rejected` | make the rejection a direct institutional fork with a visible consequence |
   | `ireland_replacement_charter` → `ireland_cultural_survey` | do not route a late charter through a six-column cultural detour; use an explicit cultural reveal edge |
   | `ireland_domestic_manufacturing` → `ireland_development_authority` and `ireland_rural_credit` → `ireland_social_cooperatives` | consolidate each material pair into a preparation/payoff choice |
   | `ireland_air_warning` → `ireland_emergency_mobilisation` and `ireland_maritime_protection` → `ireland_readiness_conclusion` | make emergency readiness and conclusion dependencies direct and readable |
   | `ireland_treaty_port_diplomacy` → `ireland_british_leverage_management` | keep port access and British leverage as adjacent but distinct commitments |

4. Use visible `prerequisite` blocks for route identity and choice locks.
   Use `available` or named scripted triggers for material, date, and evidence
   gates that should not draw a connector. Do not hide the only route parent in
   an availability condition.
5. Keep mutually exclusive choices as true locks. A route is not committed by
   a colour change or a small modifier; it is committed by a visible policy
   choice that changes later focuses, decisions, AI priority, and failure
   consequences.
6. Put every route capstone after the route’s own interaction and at least one
   support-lane proof. A capstone must not be reachable by a generic conclusion
   flag alone.
7. Hidden routes begin behind evidence and route-specific gates. `A` outcomes
   remain impossible to discover through ordinary AI or an uncommitted cultural
   focus.

### Route survival checklist

The consolidation must retain, in shorter form, each of these distinct route
families: constitutional Fianna Fáil/de Valera; Lemass developmental; Fine
Gael/Cosgrave/Mulcahy/Costello; Dillon intervention; Norton parliamentary
Labour; Clann agrarian; constitutional vocational; serious cultural; IRA civil
authority and army authority; Republican Congress plural and vanguard; O’Duffy
personal command and corporate order; clerical/producer-council; Ailtirí; High
King; Five Provinces; and Otherworld/convergence.

Each surviving family must have:

- a visible entry gate and a real route lock;
- at least one route-specific interaction with a support lane;
- a route-specific reward or institution;
- an actionable decision or mission phase;
- one failure or reversal state;
- a conclusion or lawful host-conclusion mapping; and
- an AI profile or explicit host-profile handoff.

If preserving all of those families within the 144-node target is impossible,
stop and request the route-roster decision. Do not silently drop a route or
replace it with a generic branch.

## Workstream 2: replace fairy-dust rewards with reward contracts

### Current defect

The current tree uses 96 institutional profile calls and 24 generic capstone
profile calls. The shared constants include values such as 20 political power,
0.01 stability, 5 command power, 10 service experience, 75 infantry equipment,
and 50 support equipment. Those values are not inherently invalid, but repeated
profile calls make a focus look complete while leaving the route unchanged.

### Reward contract

After consolidation, no focus may have a reward package consisting only of
political power, stability, war support, experience, equipment, or a generic
spirit. A shared profile may remain as a small part of a bridge reward, but no
more than 24 of the final focus blocks may use a shared profile, and no more
than 8 may use the institutional profile. The exact final count is subject to
the route-roster decision above; the anti-fairy-dust rule is not optional.

Use one or more of these concrete reward classes on every route-bearing focus:

| Focus role | Required reward contract |
| --- | --- |
| Shared opener | initialize or reveal one shared system, establish a meaningful baseline, and open the next decision phase; no free stockpile bundle |
| Constitutional anchor | set a constitutional component or route flag, unlock a named parliamentary/election action, and move one or more settlement stakeholders with a visible tradeoff |
| Government/leader anchor | install or transform a leader, office, law, cabinet relationship, or parliamentary authority; expose the next action phase |
| Economic anchor | open a named project, factory/rail/port/resource commitment, production or trade posture, or provision mission; use dynamic material requirements rather than repeated support equipment |
| Defence anchor | unlock a formation/template, command institution, warning or maritime task, readiness mission, or lawful military authority; do not grant a generic army bundle on every node |
| Diplomacy/neutrality anchor | create a sponsor channel, agreement, incident response, access condition, recognition change, or sovereignty safeguard with a measurable exposure cost |
| Northern anchor | advance a named ledger stage, actor relationship, or settlement mission; never grant control or cores as a political reward |
| Society/culture anchor | create an institution, language/service delivery, archive/evidence permission, labour agreement, minority guarantee, or vocational review with a concrete follow-up |
| Hidden route anchor | record evidence quality, source credibility, obligation, or containment risk; no immediate impossible transformation |
| Capstone | replace or conclude route spirits, close obsolete decisions, open the conclusion/recovery review, and deliver a route-specific national consequence; no universal PP/CP/XP/equipment bundle |

Reward migrations must be traceable in a table with columns `focus_id`,
`surviving role`, `specific output`, `shared profile removed`, `new decision or
mission`, `lifecycle cleanup`, and `validation scenario`. The implementation
owner must not tune values directly in 226 individual focus blocks.

Use round values and central constants for meaningful state changes. Small
values may support a larger effect, but a 0.01 stability change cannot be the
only reason to click a focus. Every route anchor should explain its opportunity
cost in terms of National Settlement, Social Consent, Provision, Readiness,
Neutrality Integrity, Dáil support, Northern ledger values, or foreign leverage.

Maintain the three persistent-spirit ceiling and lifecycle replacement rules.
Do not create a new spirit for every focus or leave a route’s preparatory spirit
active after its conclusion.

## Workstream 3: progressive decision and mission disclosure

The current decision source has the correct general ingredients—dynamic costs,
named map objectives, missions, partial results, AI blocks, and cleanup—but the
category and reveal layer has drifted from the canonical 13/140/54 contract.
The next implementation pass must make visibility follow phase and route state,
not merely `ireland_reveal_category_*`.

### Required phase model

| Phase | Entry | Visible settlement/election actions | Exit and cleanup |
| --- | --- | --- | --- |
| 0. Shared opening | `ireland_initialized` through `ireland_national_settlement` | One Dáil opening action, one constitutional/settlement action, and at most two support-lane actions; hidden and leader routes remain closed | Establish the first route choice and clear actions that have become obsolete |
| 1. Parliamentary foundation | Dáil session or equivalent opening complete | `ireland_action_negotiate_seanad_support`, `ireland_action_secure_a_confidence_compact`, `ireland_action_count_formal_and_routine_votes`, plus the currently valid election preparation action | Advance `ireland_parliament_stage`; update the GUI dirty value after each ledger change |
| 2. Government formation | election result, confidence loss, or formation-ready flag | coalition negotiations, alternative Taoiseach, cabinet portfolios, programme and charter actions; only actions eligible for the current seat arithmetic | One formed government, a minority agreement, caretaker state, or dissolution; remove incompatible offers |
| 3. Active government | lawful government and route commitment | confidence-and-supply, cabinet cohesion, ordinary agenda, social and material programmes; route-specific actions appear only after the route lock | successful review, coalition collapse, emergency, or route transformation |
| 4. Crisis/emergency | constitutional crisis, lost vote, emergency, invasion, severe shortage, or sponsor failure | only crisis actions plus the reserved critical mission slot; routine actions are suppressed or deprioritised | failure, partial recovery, restoration of ordinary procedure, or route conclusion |
| 5. Review/conclusion | six-month review, route conclusion, postwar, or integration review | review and cleanup actions; no new routine ladder unless the route explicitly reopens | archive obsolete actions, replace lifecycle spirits, preserve history, and expose the next lawful host |

The native staged actions already present—`ireland_action_convene_the_dail`,
`ireland_action_negotiate_seanad_support`,
`ireland_action_secure_a_confidence_compact`, and
`ireland_action_pass_a_joint_budget`—should become the foundation of Phase 0
and Phase 1 rather than a separate mini-system. They currently advance
`ireland_parliament_stage` and call `ireland_update_parliament`; preserve that
ownership and add the missing phase gates, costs, AI priorities, and visible
outcomes.

The following actions need explicit lifecycle connections:

- `ireland_action_request_a_confidence_vote` starts a named confidence mission
  and must resolve to majority, partial confidence-and-supply, caretaker, or
  dissolution outcomes.
- `ireland_action_negotiate_confidence_and_supply` must add a dated support
  agreement and one working vote without silently adding a government seat.
- `ireland_action_count_formal_and_routine_votes` must be the authoritative
  seat-ledger audit before government formation or a constitutional vote.
- `ireland_action_open_coalition_negotiations`,
  `ireland_action_assign_cabinet_portfolios`, and
  `ireland_action_ratify_the_coalition_charter` must be a sequence, not three
  independent generic actions.
- `ireland_action_ask_the_president_for_dissolution` and
  `ireland_action_establish_a_caretaker_cabinet` must close government-only
  actions and make the caretaker restriction visible.
- The election actions must disappear on polling-day cleanup and transfer
  promises into the resulting government or opposition state.

Use the existing normal/emergency mission capacities of 8/10/conditional 12.
The settlement category should not display a full tray of every possible
government action. A category cap is a clutter-control rule, not just an AI
priority.

## Workstream 4: make parliament a real mechanic

### Existing authority to preserve

The existing backend already defines the central data needed for a real
mechanic:

- formal Dáil party ledgers for Fianna Fáil, Fine Gael, Labour, and other/minor
  deputies;
- `ireland_dail_government_routine_votes` and
  `ireland_dail_majority_threshold` for ordinary working support;
- `ireland_dail_external_support_votes` for confidence-and-supply;
- `ireland_dail_mandate`, `ireland_cabinet_cohesion`, and `ireland_social_consent`;
- Seanad formal/government/opposition ledgers;
- `ireland_parliament_stage` and the four completion flags;
- `ireland_parliament_gui_dirty` and `ireland_update_parliament`.

The panel must be a projection of those values. It must not introduce a second
seat count, a GUI-only vote total, or a value that the AI cannot see.

### Required interaction contract

The future panel should expose three layers:

1. **Arithmetic:** formal seats, routine working votes, support agreements,
   Seanad support where the selected UI contract includes it, and the current
   majority threshold.
2. **Institutional stage:** Dáil convened, Seanad support negotiated, confidence
   compact secured, joint budget passed, or a route-specific institutional mode.
3. **Action state:** the currently available action, its exact cost and
   requirement, active mission/timer, and the visible full/partial/failure
   consequence.

The six existing party/status rows may be retained as the arithmetic summary,
but they must stop implying that every row is an action. Add a clear stage and
action area, or select a party/status row and show the native decision that owns
the next transition. The implementation must not show a clickable control that
only changes a local selection variable.

The four staged chamber actions must produce this observable sequence:

| Stage | Action | Observable state change |
| --- | --- | --- |
| 1 | Convene Dáil | Dáil session history records; stage advances; routine and mandate values update; next action appears |
| 2 | Negotiate Seanad support | Seanad government/opposition values update; stage advances; support requirement is visible |
| 3 | Secure confidence compact | external support and routine working votes update; the agreement is dated and reviewable |
| 4 | Pass joint budget | administrative reach, mandate, and cohesion update; stage reaches the completed state and opens ordinary government work |

The main confidence and coalition actions must then operate on this same state.
Failure is part of the mechanic: a lost vote removes or suspends government-only
actions, opens a caretaker/dissolution path, and leaves a readable historical
record. A successful confidence-and-supply action must not convert minor
deputies into cabinet seats. A coalition must not be considered formed before
portfolio and charter obligations are complete.

### Scripted-GUI ownership choice

The current `ireland_parliament_panel_scripted_gui` registration has no action
effects, trigger table, or properties. Before GUI implementation, the engine
reference audit must answer whether a scripted GUI can safely invoke the native
decision action in the current decision-category context. The implementation
owner must choose one authoritative interaction model and document the proof:

- **Recommended:** the panel’s action control routes to the existing native
  decision entry, while scripted GUI effects only select, preview, dirty, and
  display state. Costs, availability, AI, completion, and cleanup stay in the
  decision block.
- **Alternative requiring explicit approval:** the panel emits a request flag
  and a single shared consumer executes the exact same action contract. This is
  only acceptable if the consumer is demonstrably shared with the native
  decision and cannot double-charge or bypass availability.

Do not implement both models. Do not count the panel as interactive until a
click has been verified to change an authoritative ledger, trigger the correct
mission or flag, dirty the display, and respect costs and failure paths.

### Non-Dáil modes

For `ireland_extra_parliamentary_transition`, corporate/producer-council
routes, and any route that changes the authority of the Dáil, define an explicit
`parliamentary_authority_mode` contract before editing the panel. The panel must
show one of:

- ordinary Dáil government;
- minority/confidence-and-supply government;
- caretaker or constitutional crisis;
- Dáil-sovereign vocational administration;
- extra-parliamentary or captured institutional authority; or
- archived/replaced parliamentary state.

The exact mode roster and whether Seanad support remains a primary interaction
are approval-required choices. Until chosen, no implementation should hide the
panel or reuse stale Fianna Fáil/Fine Gael labels for a changed authority.

## Workstream 5: strengthen AI parity

The four staged parliament actions currently use simple base weights (`10`, `9`,
`8`, and `7`) while the larger action layer uses more elaborate utility
modifiers. This is not sufficient for route-aware parliament play.

Implement AI priorities in the same order as the player contract:

| Profile/scenario | Expected ordering |
| --- | --- |
| Historical Fianna Fáil | Dáil foundation → formal/routine count → confidence support → government programme/budget → material and neutrality actions |
| Fine Gael or coalition | count ledger → open negotiations → portfolios → charter → confidence review; avoid repeating failed offers |
| Labour or Clann support route | secure a named programme/support agreement before treating the government as stable; accept a minority outcome when the ledger cannot reach a majority |
| Dillon intervention | parliament and sovereignty gates before foreign alignment or war; never bypass the named vote and material safeguards |
| Vocational/corporate transition | complete the authority transition, close incompatible Dáil actions, and use the selected institutional mode |
| Emergency/caretaker | resolve the critical review, confidence failure, or supply crisis before starting routine projects |
| Recovery/conclusion | restore ordinary procedure or complete the route review; do not reopen obsolete actions |

AI must use the same costs, action burden, material floors, route flags, and
mission capacity as the player. The AI must never discover a hidden A route from
an action that is only technically visible, and must never click a GUI control
that has no AI-equivalent decision path.

## Validation matrix

All tests below are future implementation checks. This addendum does not claim
that any of them has passed.

### Static source and graph checks

- Re-run `hoi4.focus_inspect` against `ireland_focus_tree` and record the new
  revision. Require no Ireland-local blocking layout diagnostics, no crossings,
  no node intersections, no duplicate IDs, no duplicate coordinates, and no
  orphaned prerequisite references.
- Confirm one shared visible root and 2–4 meaningful first choices. Every
  separate root must be documented as a deliberate later reveal, not an
  accidental root.
- Confirm every linear route edge uses the next row and adjacent column unless
  a cross-lane interaction is explicitly named. The known detour and zigzag
  diagnostics must disappear.
- Reconcile the final focus count, decision category count, action count, and
  mission count against the accepted registry. A source header is not evidence.
- Audit every focus reward. A focus with only a generic shared profile, tiny
  stability, small PP, XP, or stockpile grant fails the reward audit.
- Validate that every route capstone has a route lock, support-lane proof,
  route-specific reward, and cleanup path.

### Parliament interaction scenarios

| Scenario | Setup and expected result |
| --- | --- |
| Fresh 1936 opening | By the first meaningful focus window, the player sees the shared Dáil/settlement state and no hidden route. Only the intended phase actions are visible. |
| Staged chamber sequence | Complete the four existing chamber actions in order. Each action advances the stage, changes the displayed ledger, dirties the panel, and exposes exactly the next approved action. Re-opening an already completed action is impossible. |
| Minority confidence-and-supply | Start at 76 routine votes against a 77 threshold. Negotiate support adds one reliable working vote without adding a government seat. The agreement has an expiry/review and can be breached. |
| Confidence failure | Trigger a failed confidence mission. Government-only actions close; caretaker/dissolution actions open; the panel changes status; no stale coalition action remains. |
| Coalition formation | Run election result → count ledger → coalition negotiation → portfolios → charter. A partial or failed formation produces the documented caretaker or new-election state. |
| Emergency review | Trigger an emergency or severe shortage. A critical action occupies the reserved mission capacity, routine actions are suppressed, and ordinary procedure returns only after review. |
| Dáil-sovereign vocational route | Complete the vocational route while preserving Dáil review. The panel changes mode without erasing the seat history, and council actions cannot silently bypass parliamentary review. |
| Extra-parliamentary/corporate route | Complete the authority transition. The panel displays the approved non-Dáil mode, closes invalid Dáil actions, and records the institutional cost and failure risk. |
| Election cleanup | Complete a general or by-election. Campaign actions close, seat ledgers update once, and government formation opens only after the count phase. |
| AI historical route | AI completes the Dáil opening and formation sequence before spending its first critical action on a route-specific conclusion. No action loop or dead category appears. |
| AI alternate route | At least one coalition, Labour, radical, corporate, vocational, Dillon, and hidden-route profile reaches its legal entry state without bypassing the parliamentary or material gate. |

### GUI inspection checks

Run GUI inspection only for
`ireland_parliament_panel_window` with a scenario that resolves the dynamic
values. Require:

- no unresolved dynamic-value diagnostics for the values shown in the panel;
- no missing action, stage, or status element in the intended interaction
  contract;
- a verified click or native-decision handoff for every advertised action;
- a dirty refresh after every authoritative state change;
- a visible locked, unavailable, active, success, partial, and failure state;
- no GUI-only arithmetic and no stale labels after route transformation.

Do not use GUI inspection of unrelated surfaces as evidence for this addendum.

## Blockers and explicit out-of-scope work

1. **Route roster and exact focus target — approval required.** The 144-node
   target is a recommended envelope, not an approved deletion list. The parent
   must approve the surviving named routes and the exact merge map before any
   focus IDs are removed or repurposed.
2. **13/140/54 versus current 14/144/54 — registry decision required.** Four
   current action blocks and the empty marine category need an owner decision.
   Until reconciled, the implementation cannot claim canonical action coverage.
3. **Parliament action ownership — engine/design decision required.** The
   current GUI has no action effects and the offline scenario left eight dynamic
   values unresolved. The implementer must verify native decision invocation or
   approve one shared request-consumer contract. This handoff does not pretend
   the current panel is a real mechanic.
4. **Seanad presentation — approval required.** The backend tracks a 60-seat
   Seanad, while the current panel’s six rows show only Dáil party arithmetic,
   routine support, public confidence, and cabinet unity. Decide whether Seanad
   support is a primary row, a stage detail, or a decision-only ledger.
5. **Non-Dáil authority roster — approval required.** The panel behavior for
   vocational, corporate, and extra-parliamentary transitions cannot be made
   coherent until the authority modes and Dáil-review rules are selected.
6. **Live engine and scenario validation — still open.** Hearts of Iron IV was
   not launched in this planning pass. Static MCP evidence is not a parser,
   render-at-runtime, or gameplay completion claim.
7. **Assets and final text — out of scope.** Existing source-clearance records
   still contain portrait/source blockers. Do not use generated likenesses,
   placeholder icons, or invented final text to close this addendum.

## Implementation order

1. Approve the route roster, focus budget, action registry, Seanad presentation,
   and authority-mode contract.
2. Build a before/after focus mapping with survivor IDs, absorbed IDs, route
   locks, first-choice timing, and reward ownership. Do not edit source from an
   unreviewed mapping.
3. Rewrite the focus DAG and layout, then run focus inspection before changing
   reward values.
4. Replace generic reward calls with route-specific contracts and lifecycle
   cleanup, using central constants.
5. Reconcile decision categories and actions, then implement phase visibility,
   progressive disclosure, route transformation, and cleanup.
6. Integrate the parliament stage, Dáil/Seanad ledgers, confidence outcomes,
   GUI dirtying, and action ownership. Prove one interaction model before
   expanding the panel.
7. Add route-aware AI ordering and run static probability/AI checks before live
   scenarios.
8. Run the validation matrix, record every failure or unrun test, and only then
   update the project status. Do not reuse the older static-closure language.

## Handoff acceptance

This addendum is accepted only when the next implementation owner can answer,
from a mapping rather than inference:

- which current focus nodes survive, merge, or become decision-only;
- what each surviving route-bearing focus changes;
- which action/mission phase each route unlocks and when obsolete actions close;
- which authoritative variable or flag every parliament row displays;
- how a player and AI perform the same parliament action;
- how lost confidence, caretaker rule, emergency review, route transformation,
  and recovery clean up;
- which design choices remain blocked; and
- which validation scenarios have actually passed.

Until those answers and the live/static checks are recorded, the Ireland focus
tree and parliament feature remain open. This document is a planning handoff,
not a fallback implementation and not a claim that the existing implementation
is complete.

## Proper stopping condition

Stop this improvement loop when the targeted handoff is either accepted for
implementation or explicitly blocked by one of the approval-required choices.
Acceptance requires all of the following to be recorded in the next evidence
pass:

- an approved survivor/merge map within the focus-count envelope, with one
  shared root, 2–4 early choices, no unexplained roots, and no remaining
  detour/zigzag/crossing diagnostics;
- a reward audit showing no duplicate/fairy reward package, no generic-profile-
  only focus, no tiny-value-only focus, and a concrete route-specific output for
  every surviving route-bearing node;
- a reconciled decision/action/category registry and a progressive phase table;
- one authoritative parliament interaction model with verified ledger changes,
  costs, AI parity, dirty refresh, failure cleanup, and explicit non-Dáil mode
  behavior; and
- recorded pass/fail results for the static graph checks and the named
  parliament, route, recovery, and AI scenarios.

When those conditions are met, close this improvement-loop addendum and hand the
approved mapping to implementation. Do not continue expanding routes, actions,
GUI surfaces, or rewards under this addendum. If an approval-required choice or
live-engine limitation remains, stop at that blocker, record the exact missing
decision or test, and leave the feature open. Do not mark the existing feature
complete, substitute a fallback, or silently simplify the scope to obtain a
passing report.
