# Ireland Focus Tree and Parliament Correction Addendum

Feature slug: `ireland_focus_tree`

Date: 2026-08-11

Status: implementation-ready correction addendum; no new route, focus, decision category, mission family, or country package is authorised

## Outcome

The accepted 2026-08-09 pass is structurally valid but does not meet the
player-facing quality bar. Its 150-focus sheet still presents most content as
one long connector field, the MCP inspection reports `branchCount = 0`, and
the reward source is dominated by bookkeeping. The Parliament panel imitates
an action deck without providing a coherent action-and-state hierarchy.

This addendum corrects those surfaces without expanding the feature:

- keep the existing 150 focus IDs and one-root campaign architecture;
- expose seven named semantic branch families through a compact, progressively
  revealed layout bounded to x `-14..14` and y `0..26`;
- detach only the cross-family prerequisites listed below and preserve their
  gameplay gates as `available` checks with player-facing tooltips;
- deepen existing focuses through existing decisions, missions, ledgers,
  route-spirit lifecycles, buildings, equipment, and XP rather than generic PP;
- make Parliament a real four-step human interaction surface while retaining
  native decisions as the AI-only entry path into the same executors; and
- replace the cramped `510x198` composition with a `510x248` two-chamber,
  two-by-two-action grid using larger seat strips and unambiguous state art.

There is no unresolved earlier addendum for this same gap. The 2026-08-05
Parliament improvement addendum, the 2026-08-06 next-pass addendum, and the
2026-08-09 layout-reveal addendum were marked implemented or superseded before
this user correction reopened the quality decision.

## Evidence behind the correction

The current runtime tree contains 150 focuses. A bounded completion-reward
scan found:

| Current reward shape | Focuses | Planning interpretation |
| --- | ---: | --- |
| flags or variables only | 69 | no visible payoff unless another surface happens to explain the flag |
| only a route/recompute/review helper beyond flags | 67 | potentially meaningful backend state, but still opaque as a focus reward |
| a concrete building, equipment, XP, event, or comparable effect | 14 | the small minority that already reads as tangible work |
| generic PP grant | 3 | `ireland_rebuild_marine_service`, `ireland_atlantic_convoy_office`, and `ireland_regional_maritime_defence_pact` |

The GUI evidence is equally specific. The inherited panel is `510x198`, its
two chamber strips are approximately `90x50`, and its four red/green checkbox
milestones occupy a clipped bottom strip. Vanilla USA Congress is a sound
precedent for live chamber frames, but it is intentionally a passive readout.
Official scripted-GUI documentation instead provides `button_name_click` and
`button_name_click_enabled`, and this repository already uses that contract on
the Northern and Concealed Evidence ledgers. A `checkboxType` has engine-owned
behaviour and is not the correct custom action control.

The historical grouping is already supported by the canonical research:

- the 1937 Constitution, Dail assent, the presidency, Seanad, electoral
  legitimacy, minority guarantees, and emergency law form one institutional
  problem rather than scattered connector lanes;
- the Economic War, rural prices, food, fuel, transport, and shipping form the
  National Provision problem;
- the 1938 Treaty Port transfer creates a sovereignty gain and a concrete
  defence obligation involving coastwatch, port control, air warning, and a
  small Marine Service;
- wartime neutrality is an active legal, diplomatic, intelligence, and
  territorial-control system, not a free stability focus;
- Northern Ireland retains its own institutions, consent blocs, labour,
  security, industry, and British relationship; and
- language, archives, folklore, sites, and regional institutions remain useful
  before any concealed route is proven.

No new quote, cultural-remark, or audio package is required. No animated focus
or Parliament asset is justified. The chamber strips and button sprites are
static presentation derivatives and need an ordinary asset manifest only.

## Superseded and retained decisions

### Superseded

The following decisions in
`ireland_focus_tree_layout_reveal_addendum_2026-08-09.md`, the implemented
spatial grammar in `maps/ireland_focus_tree_architecture_map.md`, and
`focus_tree_parliament_completion_2026-08-09.md` are superseded:

1. Seven simultaneous full-tree horizontal bands spanning x `-24..38`.
2. All ordinary subject families visible from the opening camera.
3. Structural cleanliness alone being sufficient despite semantic
   `branchCount = 0`.
4. The far-left emergency/recovery island and far-right Marine Service island.
5. The `510x198` Parliament host, two `50px` chamber strips, passive
   red/green checkbox milestones, and native human decisions as the sole
   interaction surface.
6. The description of Parliament as a fourth passive overview surface.

### Retained

The following remain authoritative:

- exactly one visible campaign root, `ireland_state_still_defined`;
- the current 150 focus IDs and existing route roster;
- fixed National Settlement, Dail, Seanad, Provision, Readiness, neutrality,
  Northern, route-spirit, mission-cap, and conclusion constants;
- the eight current concealed branch roots and their existing H/P/A evidence
  gates;
- no free Northern control, annexation, cores, armies, or instant integration;
- three persistent route-spirit families and their replacement/cleanup rules;
- existing decisions and missions as the operational content to expose; and
- costs `15/25/25/35` and stages `1..5` for the four opening Parliament acts.

## Exact semantic branch registry

The shared root is not counted as a branch. The implementation plan and MCP
rewrite manifest must register exactly seven semantic branch families. A
post-rewrite semantic `branchCount` of zero is not acceptable.

| Branch | Semantic root and reveal root | Exact authored window | Internal anchors | Meaning |
| --- | --- | --- | --- | --- |
| B1 Government and Constitution | `ireland_national_settlement` at `(-8,2)` | x `-14..-6`, y `2..26` | `ireland_election_timetable` `(-8,4)`; `ireland_constitutional_draft` `(-8,6)`; `ireland_government_formation` `(-8,10)` | Oireachtas, election, constitution, government formation, constitutional party routes, emergency and lawful recovery |
| B2 Society, Culture, and Evidence | `ireland_church_labour_consultation` at `(-4,4)`; operational reveal `ireland_cultural_survey` at `(-4,8)` | x `-6..-2`, y `4..24` | `ireland_archival_record` `(-4,10)`; `ireland_cultural_evidence_ledger` `(-4,14)` | organised society, minority guarantees, language, archives, sites, legitimate cultural capacity, concealed evidence handoff |
| B3 National Provision | `ireland_economic_war_review` at `(0,2)`; operational reveal `ireland_provision_baseline` at `(0,6)` | x `-2..2`, y `2..22` | component fan at x `-2/0/2`; `ireland_provision_conclusion` `(0,18)` | food, energy, transport, maritime access, manufacturing, rural credit, stockpiles, delivery projects |
| B4 National Readiness | `ireland_defence_estimates` at `(8,2)`; operational reveal `ireland_readiness_baseline` at `(8,6)` | x `6..10`, y `2..22` | command/army x `6/8`; coast/air/port x `8/10`; `ireland_readiness_conclusion` `(8,20)` | command, equipment, mobilisation, supply, warning, maritime protection, intelligence, civilian control |
| B5 Active Neutrality and Foreign Relations | `ireland_active_neutrality` at `(4,14)`; operational reveal `ireland_strict_neutrality` at `(4,16)` | x `2..6`, y `14..26` | British x `2`; American x `4`; Vatican x `6`; `ireland_neutrality_posture` `(4,24)` | neutrality law and incidents, source-specific channels, safeguards, leverage, posture |
| B6 Northern Settlement | `ireland_northern_settlement_ledger` at `(-4,16)` | x `-6..-2`, y `16..26` | local/trade/labour at x `-6/-4/-2`; federal/unitary at x `-5/-3`; proof `(-4,26)` | separate Northern institutions, consent, labour, British flexibility, security, models, proof |
| B7 Marine Service | `ireland_establish_naval_staff` at `(12,14)` | x `10..14`, y `14..26` | rebuild/patrol x `10/12`; harbour/dockyard/watch x `12/14`; pact `(12,26)` | small-state naval staff, patrol/rescue, harbour defence, Cobh, Lough Swilly, convoy office, regional pact |

The common sovereignty hinge is deliberately outside the branch count:

| Shared hinge | Exact anchor | Purpose |
| --- | ---: | --- |
| `ireland_state_still_defined` | `(0,0)` | opening camera and only root |
| `ireland_public_order_review` | `(-6,4)` | early security evidence and concealed political handoff |
| `ireland_rural_price_board` | `(0,4)` | Provision handoff |
| `ireland_command_audit` | `(8,4)` | Readiness handoff |
| `ireland_1938_trade_settlement` | `(0,10)` | shared trade/sovereignty convergence |
| `ireland_treaty_port_transfer` | `(0,12)` | central hinge to neutrality, Northern policy, port defence, and Marine Service |

### Political sub-branch roots

These are route roots inside B1, not new day-one macrobranches. They reveal only
after their existing mandate/evidence gates and reuse the B1 window:

- Fianna Fail inheritance: `ireland_republican_government`, then
  `ireland_de_valera_stewardship`, `ireland_de_valera_reconciliation`,
  `ireland_emergency_direction`, or `ireland_lemass_developmental`.
- Constitutional opposition: `ireland_constitutional_opposition`, then
  `ireland_cosgrave_institutional`, `ireland_mulcahy_succession`,
  `ireland_costello_coalition`, or `ireland_dillon_public_dissent`.
- Parliamentary alternatives: `ireland_norton_parliamentary`,
  `ireland_clann_founding`, and `ireland_vocational_constitution`.

Mutually exclusive siblings share one row. Each selected route then descends
vertically in a two- or three-column module. Capstones occupy the same final
row; they do not jump to a material branch merely to show a distant gate.

### Concealed overlays

Keep the existing eight reveal roots, but place them in the nearest semantic
module and show none at the opening camera:

- B1 political overlay: `ireland_ira_republican_bridge`,
  `ireland_congress_reform_bridge`, `ireland_oduffy_network_revival`,
  `ireland_clerical_failure_bridge`, `ireland_ailtiri_cell_network`;
- B2/B6 evidence overlay: `ireland_high_king_evidence_gate`,
  `ireland_five_province_mandates`, `ireland_otherworld_investigation`.

The mutually incompatible hidden modules may reuse the same x columns after
their `allow_branch` gates. They must not expand the authored bounds.

## Progressive reveal contract

The opening viewport, x `-10..10` and y `0..8`, shows the shared root, the
three early problem choices, and their first evidence/audit nodes. It does not
show late political leaders, the Northern settlement model, foreign-channel
capstones, the Marine Service conclusion, or concealed routes.

Add or retain `allow_branch` at these exact ordinary reveal roots:

| Reveal root | Reveal condition; retain the full current `available` block for selection |
| --- | --- |
| `ireland_republican_government` | constitutional draft complete and the republican-government gateway exists |
| `ireland_constitutional_opposition` | government formation complete and a Fine Gael/opposition mandate exists |
| `ireland_norton_parliamentary` | government formation complete and Norton/Labour gateway exists |
| `ireland_clann_founding` | government formation complete and agrarian gateway exists |
| `ireland_vocational_constitution` | government formation complete and vocational gateway exists |
| `ireland_cultural_survey` | replacement charter, public-order review, and church/labour consultation complete |
| `ireland_provision_baseline` | rural price board and 1938 trade settlement complete |
| `ireland_readiness_baseline` | defence estimates and command audit complete |
| `ireland_strict_neutrality` | active neutrality and Treaty Port transfer complete |
| `ireland_northern_settlement_ledger` | Treaty Port transfer complete |
| `ireland_establish_naval_staff` | port-defence authority, readiness plan, and command audit complete |

An `allow_branch` controls presentation only. It must not replace an
`available` gate or make an AI path legal earlier.

## Exact prerequisite detach and reattach list

Only the following connector ownership changes are authorised. Each removed
cross-family prerequisite becomes or remains an `available` check with a
custom tooltip, so gameplay proof is preserved without drawing a misleading
connector.

| Focus | Detach structural prerequisite | New structural parent | Gate retained as availability |
| --- | --- | --- | --- |
| `ireland_lemass_developmental_capstone` | `ireland_development_authority` | `ireland_dail_nomination` | development authority/provision conclusion remains material proof |
| `ireland_constitutional_opposition` | `ireland_treaty_port_transfer` | `ireland_government_formation` | Treaty Port/timeline condition remains if still required by the route contract |
| `ireland_norton_parliamentary` | `ireland_cultural_survey` | `ireland_government_formation` | cultural/social proof remains an availability gate |
| `ireland_clann_founding` | `ireland_cultural_survey` | `ireland_government_formation` | rural/cultural participation proof remains an availability gate |
| `ireland_vocational_constitution` | `ireland_cultural_survey` | `ireland_government_formation` | stakeholder and cultural proof remains an availability gate |
| `ireland_strict_neutrality` | `ireland_readiness_baseline` | `ireland_active_neutrality` | readiness baseline and Treaty Port control remain availability gates |
| `ireland_congress_reform_bridge` | `ireland_church_labour_consultation` | `ireland_public_order_review` | Labour organisation and church/labour consultation remain reveal/availability proof |
| `ireland_clerical_failure_bridge` | `ireland_church_labour_consultation` | `ireland_public_order_review` | clerical failure, producer mandate, producer accounting, and consultation remain reveal/availability proof |
| `ireland_material_conclusion_proof` | `ireland_restore_constitutional_calendar` | `ireland_northern_policy_proof` | require `ireland_restore_constitutional_calendar` only when a route failure/recovery state makes restoration necessary |

Do not detach local convergence inside one semantic family. In particular,
retain the multiple prerequisites on `ireland_foreign_safeguards`, the
component proof on `ireland_provision_conclusion`, the operational proof on
`ireland_readiness_conclusion`, and all concealed evidence requirements.

## Lane and connector rules

1. Hard authored bounds are x `-14..14`, y `0..26`. A focus outside the bounds
   fails this pass.
2. Reserve one empty x column between simultaneously visible macro-families.
3. Direct parent/child spacing is one or two y rows and at most three x
   columns. No visible connector may exceed six x units or three y rows.
4. A same-family AND join places parents on the same preceding row and within
   four x units of the child.
5. A material, Northern, foreign, or cultural proof that does not represent
   narrative descent is an `available` condition with a custom tooltip, not a
   cross-map prerequisite.
6. No connector crosses a focus box, branch label, or another connector.
7. Only the shared root and the seven named semantic roots may have more than
   three visible outgoing connectors.
8. The renderer must show whitespace and a distinct root icon at the entrance
   to every family. Do not commission new branch background art; reuse the
   existing icon set and spacing.
9. The post-rewrite MCP record must report the seven-family branch registry,
   zero crossings, zero node intersections, zero long connectors, and no
   sibling-anchor warning that obscures a route choice.

## Reward-depth contract

A reward is judged by what the player can understand and use, not by the
number of flags it writes. Every focus may retain bookkeeping needed by
existing systems, but each focus must also satisfy one named reward class.

| Class | Required player-facing outcome |
| --- | --- |
| Gateway | opens a named GUI/category and identifies at least one newly usable action or mission |
| Operational | unlocks at least two named existing actions/missions, or unlocks one and makes one visible ledger/capability change |
| Physical | starts or completes a named building, equipment, unit, convoy, agency, or regional project with its delivery constraints |
| Training | grants branch-appropriate army/air/navy XP or a bounded tech bonus and explains the institution that produced it |
| Route anchor | commits the route, transforms the existing three spirit families/authority identity, and unlocks a route action |
| Capstone | opens a visible conclusion review/mission, applies the final route identity/spirit state, and owns cleanup/recovery handoff |

Rules:

- a flag, `recompute_*`, `commit_route`, or `begin_conclusion_review` call does
  not by itself satisfy the contract;
- use `unlock_decision_tooltip`, a named custom effect tooltip, and visible
  dynamic deltas so the focus screen exposes the real consequence;
- no focus may use generic PP as its primary or secondary reward in this
  correction pass;
- remove PP from `ireland_rebuild_marine_service`,
  `ireland_atlantic_convoy_office`, and
  `ireland_regional_maritime_defence_pact`; retain their maritime capability,
  buildings/equipment, XP, dynamic modifier, and exact decision unlocks;
- do not paste the same stability/XP/equipment bundle across routes;
- any new tuning values belong in subsystem script constants, not duplicated
  file-local magic numbers; and
- preserve the three-persistent-spirit ceiling.

### Priority 0: visible spine and branch roots

Implement these before polishing any concealed route:

| Focus IDs | Required depth using existing surfaces |
| --- | --- |
| `ireland_national_settlement`, `ireland_election_timetable`, `ireland_constitutional_draft`, `ireland_election_mandate`, `ireland_government_formation` | expose the Parliament programme; unlock electoral register, campaign freedom, candidate organisation, vote count, coalition negotiation, alternative Taoiseach, cabinet portfolios, and government-formation mission as their stages become legal |
| `ireland_public_order_review`, `ireland_command_audit`, `ireland_defence_estimates` | make Intelligence Coordination/Command and Training consequences visible; unlock command exercise, agent control, protected-plan, and command-district proof actions at their lawful gates |
| `ireland_church_labour_consultation`, `ireland_cultural_survey` | unlock education compact, collective bargaining, minority institutions, Gaeltacht administration, folklore collection, archives, and regional cultural congress actions rather than hiding them behind readiness flags |
| `ireland_economic_war_review`, `ireland_rural_price_board`, `ireland_provision_baseline` | open the Provision category and identify tillage quotas, seed/fertiliser, agricultural prices, mill/storage, fuel, rail, and maritime project families |
| `ireland_1938_trade_settlement`, `ireland_treaty_port_transfer` | expose the British supply/settlement and port-defence obligations; unlock harbour defence and Treaty Port mission work rather than treating transfer flags as the payoff |
| `ireland_readiness_baseline`, `ireland_maritime_protection`, `ireland_establish_naval_staff` | unlock cadre reserve, LSF/LDF, coastwatch, harbour defence, marine patrol, naval staff/agency, and readiness proof; preserve the naval staff's existing XP/tech/agency depth |
| `ireland_active_neutrality`, `ireland_strict_neutrality` | open the neutrality-incident actions and make Neutrality Integrity/current stance visible |
| `ireland_northern_settlement_ledger` | open the six-value ledger and the cross-border confidence/delegation actions; do not present a claim as the whole reward |

### Priority 1: operational support families

| Family and exact focus IDs | Existing action/mission families that must be named in the rewards |
| --- | --- |
| Provision: `ireland_food_ledger`, `ireland_energy_board`, `ireland_transport_priority`, `ireland_maritime_reserve`, `ireland_domestic_manufacturing`, `ireland_rural_credit`, `ireland_emergency_stockpiles`, `ireland_development_authority`, `ireland_social_cooperatives`, `ireland_producer_accounting`, `ireland_provision_conclusion` | tillage, seed/fertiliser, mills/storage, livestock, protected workshops, developmental plant, ration books, fuel allocation, turf, rail corridor, depot, foreign tonnage, merchant vessel, essential cargo, housing, western portfolio, and their existing delivery missions |
| Readiness: `ireland_readiness_command`, `ireland_coastwatch`, `ireland_air_warning`, `ireland_port_defence_project`, `ireland_professional_army`, `ireland_civilian_oversight`, `ireland_interoperability`, `ireland_emergency_mobilisation`, `ireland_readiness_conclusion` | command exercise, equipment standardisation/procurement, cadre reserve, LSF/LDF, motorised route, coastwatch sectors, harbour defences, marine patrols, G2 liaison, agent control, protected plans, demobilisation, and their proof missions |
| Foreign: `ireland_treaty_port_diplomacy`, `ireland_british_leverage_management`, `ireland_american_diaspora_mission`, `ireland_vatican_small_state_mediation`, `ireland_foreign_safeguards`, `ireland_neutrality_posture` | British supply contract and Plan W liaison; American procurement and diaspora relief; Vatican humanitarian mediation; neutral-states consultation; anti-dependency clauses; channel delivery missions |
| Northern: `ireland_northern_local_authorities`, `ireland_northern_trade_corridor`, `ireland_northern_labour_social_bridge`, `ireland_northern_federal_preparation`, `ireland_northern_unitary_preparation`, `ireland_northern_wartime_bargain`, `ireland_northern_policy_proof` | confidence measures, delegations, British flexibility, campaign freedom, federal conference, unitary safeguards, labour-industrial settlement, wartime bargain, lawful deferment, representative convention, and settlement missions |
| Culture: `ireland_archival_record`, `ireland_serious_cultural_stewardship`, `ireland_cultural_evidence_ledger` | archives, folklore, sites, language services, restoration testing, hidden evidence council, and evidence verification |

### Priority 2: route anchors and capstones

Apply the Route-anchor contract to every focus that calls
`ireland_commit_route`. Apply the Capstone contract to every focus that calls
`ireland_begin_conclusion_review`. The visible review must name its duration,
current material/Northern/foreign proof, full/partial/failure result, and
recovery path. Do not add route nodes; deepen the existing root and capstone.

### Reward acceptance

- all 150 focuses have a visible effect description tied to one reward class;
- zero focuses remain player-facing flag-only, even when flags remain in the
  backend;
- all branch roots and capstones pass the Gateway/Route/Capstone contracts;
- the three generic PP grants are gone;
- no new action or mission is added merely to pad a focus reward; and
- focus tooltips name the exact existing action, mission, ledger, building,
  equipment, XP, spirit, or review they affect.

## Parliament functional interaction contract

### Ownership

Humans use the four scripted-GUI buttons. AI uses the four existing native
decisions. Both paths call the same executor. There is no human-visible native
duplicate and no GUI AI path.

| Stage | Human button | AI decision | Canonical trigger | Shared executor | Cost |
| ---: | --- | --- | --- | --- | ---: |
| 1 | `ireland_parliament_dail_button` | `ireland_action_convene_the_dail` | `ireland_parliament_dail_action_available` | `ireland_execute_parliament_dail_action` | 15 PP |
| 2 | `ireland_parliament_seanad_button` | `ireland_action_negotiate_seanad_support` | `ireland_parliament_seanad_action_available` | `ireland_execute_parliament_seanad_action` | 25 PP |
| 3 | `ireland_parliament_confidence_button` | `ireland_action_secure_a_confidence_compact` | `ireland_parliament_confidence_action_available` | `ireland_execute_parliament_confidence_action` | 25 PP |
| 4 | `ireland_parliament_budget_button` | `ireland_action_pass_a_joint_budget` | `ireland_parliament_joint_budget_action_available` | `ireland_execute_parliament_budget_action` | 35 PP |

Each executor must recheck its canonical trigger, deduct PP once from script
constants, call the existing `ireland_record_parliament_*` effect, and become
idempotent through the existing stage/completion flag. The native AI decision
has `is_ai = yes`, no second engine cost, preserves `ai_hint_pp_cost`, and calls
the executor in `complete_effect`. The GUI uses `button_name_click` to call the
same executor and `button_name_click_enabled` to read the same trigger.
`ai_enabled = { always = no }` prevents scripted-GUI AI execution.

Before `ireland_settlement_open`, show the chamber summary and hide the action
grid. After the gate, show all four steps: completed steps disabled/secured,
the current legal step enabled when affordable, and later steps disabled and
locked. Route archival hides the complete surface and both controller paths.

### Exact alignment and sizing

Use a fixed `510x248` root. The 510-pixel legacy width is the only exception to
the 4-pixel internal grid. All child y positions and all reusable component
sizes use the 4-pixel grid; the two `247px` chamber cards remain symmetrically
placed around the x `255` centre line.

| Element | Exact bounds |
| --- | --- |
| root/background | `0,0,510,248` |
| title | `0,2,510,18` |
| Dail card | `4,22,247,120` |
| Seanad card | `259,22,247,120` |
| Dail seat strip | card-local `61,19,126,67`; 21-frame source strip `2646x67` |
| Seanad seat strip | card-local `61,18,126,70`; 21-frame source strip `2646x70` |
| chamber support ratio | card-local `0,89,247,18`, centred, minimum 18px display font |
| chamber composition/status | card-local `0,106,247,14`, centred, minimum 14px font |
| programme heading | `0,148,510,16` |
| Dail / Seanad buttons | `10,168,238,32` and `262,168,238,32` |
| Confidence / Budget buttons | `10,208,238,32` and `262,208,238,32` |
| state icons | `13,169,31,31`; `265,169,31,31`; `13,209,31,31`; `265,209,31,31`, click-through |
| button labels | `47,176,190,16`; `299,176,190,16`; `47,216,190,16`; `299,216,190,16`, click-through |

This gives each action a `238x32` hit region, 8px vertical separation, 8px
bottom safety, and sufficient label width for cost plus action name. Do not use
four `123px` buttons in one row; that repeats the truncation and alignment
problem.

### State semantics

| State | Chamber/action treatment |
| --- | --- |
| summary only | chambers visible; programme heading and buttons hidden before `ireland_settlement_open` |
| future/locked | neutral slate lock/seal, disabled button, tooltip names previous stage and other unmet requirements |
| current but unaffordable | muted amber state, disabled, cost and PP shortfall explicit |
| current and available | gold/cream outline, enabled with native hover/press states, exact cost and outcome in tooltip |
| completed | green secured seal/check, disabled, result retained |
| failure/crisis | red is reserved for an actual failure/crisis state; ordinary incomplete steps are never red |
| archived | entire category header, panel, human buttons, and AI decisions hidden |

The old passive red/green checkbox strip is retired. If a small state icon is
overlaid on a button, it is click-through and never the action owner. Seat
arcs show live support ratio and majority threshold; opposition uses neutral
slate rather than failure red. Each button tooltip binds the scripted-GUI
effect and enable output so the player sees the canonical effect and unmet
requirements, not raw flags or state ID 113.

## AI, asset, localisation, and documentation handoff

- Preserve the AI weights `10/9/8/7` and the `15/25/25/35` PP reservation
  hints. AI never clicks the GUI.
- Produce two 21-frame static seat strips at the exact frame sizes above and a
  `238x32` button sprite with normal, hover, pressed, and disabled rendering.
  Keep source PNG, DDS, manifest, and contact sheet. No animation package is
  needed.
- Localisation must name branch families, focus consequences, Parliament
  costs, current stage, missing requirements, and outcomes. It must not expose
  implementation flags or describe the correction history.
- If accepted, promote the semantic branch registry, reveal roots, detach list,
  and reward-depth contract into the architecture map and relevant numbered
  specs. Promote the Parliament ownership/layout contract into the
  constitutional politics spec and GUI/asset ledger.
- Amend the canonical GUI wording from “exactly three scripted GUI surfaces”
  to “three overview ledgers plus one embedded Parliament action presenter.”
  This is a classification correction for an already implemented panel, not
  authorisation for another GUI.

## Implementation order

1. Freeze the 150-ID roster and record the seven-family branch manifest.
2. Apply the exact prerequisite detach/reattach list.
3. Place the common hinge and seven root anchors, then compact each family
   inside its window; do not tune rewards until the render is readable.
4. Add ordinary progressive reveal roots and re-run focus inspect/render.
5. Implement Priority 0 rewards and tooltips, then Priority 1 support families,
   then route roots/capstones. Remove the three PP grants.
6. Implement shared Parliament executors and the human/AI split before wiring
   buttons, so no duplicate/free-cost path exists at any intermediate point.
7. Replace the panel geometry/assets and verify click regions at target UI
   scales.
8. Reconcile specs/status/audit records and run the task-specific scenarios.

## Acceptance scenarios

### Focus tree

- The opening camera shows one root and three clear early choices.
- The MCP semantic branch record reports seven named families, not zero.
- Authored bounds are no wider than x `-14..14` and y `0..26`.
- There are zero crossings, node intersections, long connectors, or
  out-of-family capstone jumps.
- Each ordinary late family reveals only after its named gateway; concealed
  content remains concealed.
- Every focus has a visible reward class; no focus presents only internal
  flags/recompute/review helpers; all three generic PP grants are absent.
- Each route capstone visibly opens its conclusion review and recovery result.

### Parliament

- A human can complete the four stages only through the four GUI buttons.
- AI can complete the same stages only through the native decisions.
- Each action charges exactly `15/25/25/35` once; repeated, double, rapid, or
  stale clicks cannot charge or credit twice.
- The exact canonical trigger controls both button enable state and AI
  decision availability.
- Before the settlement gate, only the two chamber summaries are visible.
- At every stage, completed/current/locked states are distinguishable without
  treating incomplete as failure.
- The `126x67` Dail and `126x70` Seanad frames remain legible at the supported
  resolutions and UI scales.
- No action label clips, no click-through overlay steals the hit region, and
  the bottom row retains its 8px safety margin.
- Route archival removes both controller paths and the panel without erasing
  intentional historical completion state.

## Blockers and scope boundary

There is no unresolved design blocker. The prior native-decision-versus-GUI
ownership question is resolved by the shared executor and human/AI split.

Implementation must still prove two things before completion:

1. a fresh MCP inspect/render must recognise the seven-family semantic plan and
   must no longer return `branchCount = 0`; and
2. the in-flight Parliament edits in the current dirty worktree must be
   reconciled against this exact executor and `2x2` layout contract. Directly
   duplicated GUI cost/effect bodies or four narrow one-row buttons do not pass.

Do not add focuses, routes, decisions, missions, GUI surfaces, animation,
quote research, audio, or generic reward bundles under this addendum. After
the accepted correction is promoted into specs and the two evidence items
pass, broad expansion should stop; only final localisation, asset-manifest,
focus/GUI audit, and cleanup work remains.

