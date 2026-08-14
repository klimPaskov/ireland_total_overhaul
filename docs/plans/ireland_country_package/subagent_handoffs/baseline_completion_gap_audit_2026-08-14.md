# Ireland country package baseline completion gap audit - 2026-08-14

Feature slug: `ireland_country_package`

Mode: read-only baseline completion audit. This is not a final completion
claim and it does not validate the concurrent implementation tranche.

## Audit anchor and authority

The gameplay baseline is revision `3dbd237`, the last committed gameplay state
before the 2026-08-14 campaign-depth work began. The current target contract is
the specification committed in `df65d37`, especially:

- `docs/specs/ireland_country_package/index.md`
- `docs/specs/ireland_country_package/campaign_architecture.md`
- `docs/specs/ireland_country_package/economy_defence_and_statecraft.md`
- `docs/specs/ireland_country_package/territorial_campaign.md`
- `docs/specs/ireland_country_package/systems_and_lifecycles.md`
- `docs/specs/ireland_country_package/ai_balance_assets_and_text.md`
- `docs/specs/ireland_country_package/implementation_matrix.md`

The new index explicitly supersedes completion claims based on focus count,
flag output, or the existence of a detached decision category. The implementation
matrix itself records the baseline territorial lane as a detached x9-21 island,
records many rewards as helper or institution flags, and leaves 1946-1951
family play as required repair. Uncommitted gameplay edits that appeared during
this audit were preserved and excluded from the baseline verdict.

## Verdict

**Incomplete for the requested campaign-depth overhaul.**

The baseline is a large, technically wired package rather than an empty or
generic country. It has 215 focuses, exactly three opening trunks, five public
political family flags and gateways, multiple concealed routes, active national
systems, nine industrial capabilities, route AI plans, 511 events, extensive
localisation, and broad asset coverage. Those facts make it a strong foundation.

They do not close the current request. The main blockers are player-facing:

1. the five public gateways are not a readable post-Settlement choice band;
2. the National Question is an isolated revealed root with no visible connector
   or navigation handoff;
3. the Northern plebiscite has a duplicate low-cost launcher that bypasses the
   existing material launcher;
4. non-coercive Northern methods mostly record ledger or diplomatic state rather
   than resolving a staged settlement;
5. Wales and Cornwall receive direct claim war goals without their own refusal
   chains;
6. reward density still includes eleven 2-percent focus rewards and uniformly
   priced PP-only industrial contracts;
7. route-specific failure, recovery, and 1946-1951 conclusions are not complete;
8. much of the exceptional-route depth promised in Part 3 remains event or flag
   state rather than selectable focus architecture;
9. static event counts substantially overstate what the paced dispatcher can
   surface in one campaign;
10. existing completion and planning records contradict the source and the new
    authority package.

## Completion status by surface

| Surface | Baseline status | Evidence and qualification |
| --- | --- | --- |
| Three opening trunks | Complete | `ireland_state_still_defined`, `ireland_economic_war_review`, and `ireland_defence_estimates` are the three ordinary opening roots. Later roots are reveal-gated. |
| Opening navigation | Partial | Only politics, industry, and defence shortcuts exist at `common/national_focus/ireland_focus_tree.txt:53-55`. There is no National Question navigation handoff. |
| Public political families | Partial | Democratic, Congress, O'Duffy, producer-estate, and High King gateways exist, but their baseline coordinates are scattered from y3 to y10 rather than forming one post-Settlement band. |
| Historical democratic campaign | Partial | Constitutional, election, Treaty Ports, Emergency, neutrality, republic, and reconstruction systems exist. The postwar focus conclusion remains shared and the family-specific 1946-1951 sequence is not proven. |
| Congress socialist campaign | Partial | Plural and vanguard profiles, a public cabinet cluster, union and self-defence content, and liberation posture exist. Supply failure, armed-dominance recovery, and a distinct postwar conclusion are not presented as a complete selectable sequence. |
| Blueshirt campaign | Partial | Personal and corporate profiles, command institutions, motorisation, ultimatum, and coercive policy exist. Failure recovery is generic and fascist route AI stops in late 1944. |
| Producer-estate oligarchy | Partial | An eight-focus public cluster, concerns, producer institutions, and Belfast commercial diplomacy exist. The compact does not itself deliver a staged Northern constitutional outcome, and rollback or producer-crisis recovery is not a complete focus path. |
| Constitutional restoration | Partial | Evidence, elective and guardian crown choices, household advisers, provincial assent, and a Dál Riata claim exist. Abdication, rejection, captured-crown recovery, and sacral branches are not fully selectable focus paths. |
| Hidden and absurd routes | Partial | Ailtirí, Five Provinces, High King, and Otherworld routes are permission or evidence gated and mechanically connected to systems. Their selectable focus depth remains substantially below the canonical Part 3 design. |
| Territorial campaign | Blocking gap | A 24-focus tail begins with isolated `ireland_define_the_national_question`. Coercive Northern and Highland response chains exist, but non-coercive settlement, Wales/Cornwall refusal, and player navigation remain incomplete. |
| Decisions and missions | Partial | The repository has broad active Provision, Readiness, neutrality, Northern, Marine Service, postwar, and territorial systems. New industrial contracts are PP-only purchases and the territorial plebiscite duplicates an older material launcher. |
| Events | Partial | Event IDs, options, exact-effect tooltips, images, and a paced broker exist. The ordinary dispatcher cannot expose most of its 459 scheduled entries in one campaign and its cursor does not control scan order. |
| Material rewards | Partial and balance-blocking | Construction, equipment, fuel, XP, research, advisors, companies, MIOs, and one bounded Marine Service unit exist. Tiny focus rewards and low-input contracts remain common. |
| Units and force development | Partial | `ireland_train_marine_service_reserve` creates one `Marine Service Company`. No focus creates or loads a route-specific unit, and the public routes have no distinct late-war force reward sequence. |
| Advisors and country identity | Mostly complete | Forty-five advisor roles, route leaders, offices, cosmetic identities, cabinet unlocks, and approved runtime portraits are wired. Three non-runtime exact-person manifest rows remain blocked. |
| Companies and MIOs | Implemented but shallow in use | Seven concerns plus Ford Cork and Harland and Wolff MIOs exist. Nine one-use contracts exist, but every contract costs 25 PP and 35 days and none consumes factory time, equipment, fuel, or resources. |
| Route AI | Partial | Profile and family plans cover the focus IDs, event options have AI chances, and historical AI avoids coercive decisions. Recovery behavior and late-game continuation are not demonstrated, and fascist plans have a 1944 cutoff. |
| Focus and event assets | Mostly complete | Focus icons, shines, decision/category icons, event images, and territorial report art resolve statically. The blocking presentation issue is architecture and visibility, not a missing baseline DDS. |
| Parliament and national GUIs | Mostly complete | Parliament, Northern Ledger, and Concealed Evidence surfaces exist. No territorial overview or navigation surface compensates for the detached focus lane. |
| Localisation and exact tooltips | Mostly complete statically | Focuses, decisions, missions, event options, advisors, companies, and territorial results have extensive English text and exact-effect lines. Some exact text faithfully describes rewards that are themselves too small or non-consequential. |
| Achievements | Implemented against old contract | Thirty-two achievements and durable history trackers exist. They have not been reconciled to the new campaign-depth acceptance scenarios. |
| Documentation | Blocking inconsistency | The old final audit says complete with no simplifications, while the new canonical package says those count-based claims are superseded and lists substantial repairs. |

## Detailed findings

### 1. Opening roots are correct, but the public family band is not

The baseline keeps the required three opening problems. This should be
preserved.

The five public gateways also exist:

- `ireland_republican_government`
- `ireland_congress_reform_bridge`
- `ireland_oduffy_network_revival`
- `ireland_vocational_constitution`
- `ireland_high_king_evidence_gate`

Their baseline coordinates are `(-16,4)`, `(-12,3)`, `(-6,10)`, `(-8,7)`, and
`(-4,4)`. They therefore do not form the one-row, pairwise readable family band
required by `campaign_architecture.md`. O'Duffy and vocational government are
several rows away from the other family choices. The existence of durable
`ireland_family_*` flags does not solve this navigation and identity problem.

The public reserve clusters contain only six democratic focuses, six Congress
focuses, six Blueshirt focuses, eight producer-estate focuses, and five
restoration focuses. Older profile branches add content, but the prior exact
contract requiring at least sixteen substantive focuses per public family was
never demonstrated with a route-by-route playable ledger. The family AI queues
also expose the thinness: their public programmes list 6, 11, 12, 9, and 9
focuses respectively, including older profile nodes. The current specification
correctly requires a fresh proof of opening, commitment, split, economy,
security, diplomacy, Northern method, failure/recovery, and conclusion for every
family.

### 2. Expansion exists in source but is easy to miss

At the baseline, `ireland_national_settlement` sets
`ireland_territorial_lane_revealed`, but `ireland_define_the_national_question`
is a new root at x13/y8 with `allow_branch` and no prerequisite connector. Its
availability additionally requires:

- political family commitment;
- `ireland_northern_policy_proof`;
- `ireland_foreign_safeguards`;
- `ireland_provision_conclusion`;
- `ireland_readiness_conclusion`.

The player sees neither a connector from politics nor a foreshadowing card that
explains those four proof families. The three shortcuts at lines 53-55 point to
government, development, and maritime protection only. This exactly matches the
reported experience that expansion is not visible even though a territorial
category and focus tail technically exist.

The target focus `ireland_unfinished_national_question` named by the new
implementation matrix is absent from baseline revision `3dbd237`.

### 3. Northern methods are asymmetric and the plebiscite is duplicated

The coercive route is the most complete baseline route. It saves requester,
controller, and state targets and fires target-country events for acceptance,
counteroffer, or refusal.

The democratic territorial launcher
`ireland_territorial_open_northern_plebiscite` at
`common/decisions/ireland_expansion_decisions.txt:205` activates
`ireland_mission_conduct_a_supervised_plebiscite` for 25 PP and 35 days. The
older action `ireland_action_protect_northern_campaign_freedom` at
`common/decisions/ireland_decisions.txt:37004` activates the same mission but
requires controlled state 119, mission capacity, Command Power, and infantry
equipment. Its completion charges 25 Command Power and 100 Infantry Equipment
at lines 37119-37128. The territorial launcher does not charge those material
inputs. This is a duplicate access path and a balance bypass.

The mission itself checks a controlled state 119 in its objective at
`common/decisions/ireland_decisions.txt:39383-39415`. It prepares or legitimises
an already controlled Northern Ireland. It does not negotiate a lawful transfer
from Britain or the current controller.

The other non-coercive baseline methods also stop short of the new target:

- `ireland_territorial_workers_border_campaign` changes consent ledgers only;
- `ireland_territorial_convene_provincial_assent` changes consent ledgers only;
- `ireland_territorial_offer_belfast_compact` opens a target event whose accepted
  baseline result gives military access and records compact state, but does not
  transfer state 119 or open a complete federal settlement sequence.

Repository-wide source search finds state transfer only in
`events/ireland_territorial_diplomacy_events.txt`. The state 119 transfers at
lines 73, 115, and 447 belong to coercive acceptance or counteroffer paths. The
state 120 transfer at line 313 belongs to the Highland demand. No parallel
lawful transfer or accepted constitutional settlement exists for the democratic,
Congress, producer-estate, or crown-federal Northern methods.

### 4. Wales and Cornwall bypass the refusal contract

The baseline territorial event file contains four response families: Ulster
ultimatum, Belfast compact, Highland demand, and Ulster enforcement. Wales and
Cornwall have no target-country demand event.

`ireland_territorial_claim_wales` at
`common/decisions/ireland_expansion_decisions.txt:517` and
`ireland_territorial_claim_cornwall` at line 570 directly add claims and create
180-day war goals at lines 562 and 615 after readiness, naval, strength, and
staging checks. They do not require a Wales-specific or Cornwall-specific
recorded refusal. This fails the new territorial contract that force follows a
live target demand and refusal.

The coercive readiness trigger at
`common/scripted_triggers/ireland_triggers.txt:4643` checks manpower, infantry
equipment, support equipment, convoys, fuel, Command Power, readiness, Dublin,
and Dáil majority. Those resources are reserve gates only. The territorial
decision file contains no negative equipment, fuel, manpower, convoy, or Command
Power effects. Force therefore costs PP and time while leaving all military and
logistical reserves intact. That is weaker than the material-input and partial
refund contract in the new specification.

### 5. Reward impact does not meet the new standard

The baseline has real rewards. Static inventory finds 21 focuses with
construction, 30 with equipment, 24 with technology bonuses, one bounded unit
creation in the Marine Service, five cabinet unlock clusters, seven concerns,
and two MIOs. The problem is uneven impact and incomplete route totals, not total
absence.

`common/national_focus/ireland_focus_tree.txt:30` defines
`@IRELAND_FOCUS_STABILITY_MINOR = 0.02`. It is used eleven times, including:

- `ireland_trade_union_congress`;
- `ireland_personal_command_or_corporate_state`;
- `ireland_claimants_convention`;
- four public cabinet or council focuses;
- the Congress, producer-estate, and restoration Northern methods;
- `ireland_atlantic_concessions`;
- `ireland_postwar_settlement_office`.

These are 70-day political or territorial cards whose visible immediate payoff
is often 2 percent Stability or War Support plus a helper or later unlock. The
exact localisation at `localisation/english/ireland_l_english.yml:5360-5552`
confirms those values. `ireland_material_conclusion_proof_reward_tt` at line
5208 grants only Administrative Reach +3 and Cabinet Cohesion +3.

The nine industrial contracts at
`common/decisions/ireland_expansion_decisions.txt:42-202` all cost 25 PP and 35
days. None consumes civilian-factory time, resources, equipment, fuel, trains,
or convoys. Outputs range from 25 trucks, one train, five convoys, 250 fuel, two
transport planes, or 5 XP to one free civilian or military factory. The identical
input pattern makes them a one-use PP store rather than distinct industrial
operations. It also produces a poor internal value ratio between a 250-fuel
purchase and a permanent factory.

The old index says 32 focus IDs have material, construction, or fuel effects, 24
have research or other capabilities, and 59 expose named decision or mission
unlocks. That leaves a large remainder that must be classified as a visible
institution or immediate route commitment. The prior 2026-08-11 semantic audit
already identified hook-only and flag-only risks. The 2026-08-13 completion
audit closed those concerns on tooltip presence rather than cumulative route
impact. No cumulative route reward budget or alternative-route total is current.

### 6. Exceptional-route focus depth remains simplified

The hidden routes are serious in tone and properly use evidence or permission
gates. They are not mechanically complete against the detailed Part 3 source.

The baseline focus surface contains:

- High Kingship: `ireland_high_king_evidence_gate`, `ireland_elective_crown`,
  `ireland_guardian_crown`, `ireland_crown_powers_charter`, and
  `ireland_high_king_capstone`;
- Five Provinces: `ireland_five_province_mandates`,
  `ireland_federal_republic`, `ireland_pentarchy_guardians`, and
  `ireland_five_provinces_capstone`;
- Otherworld: `ireland_otherworld_investigation`,
  `ireland_otherworld_evidence_ledger`, `ireland_compact_with_otherworld`,
  `ireland_containment_protocol`, `ireland_dominion_claim`, and
  `ireland_otherworld_capstone`.

The detailed Part 3 specification also promises captured-crown and sacral High
King outcomes, Irish Confederation, Crown and Five Provinces, Four Provinces and
an Empty Chair, the Fifth Province, Rival Irelands, Tuatha sovereignty, Fianna
guardianship, regional courts, exploitation, and cross-route conclusions. Many
of those states have flags, events, ideas, or cosmetic identities, but they are
not selectable focus architecture. The older semantic audit explicitly called
out these omissions. The later 65-focus expansion added public family, company,
and territorial cards rather than closing those exceptional branches.

### 7. Failure and recovery are shared rather than family-complete

`ireland_recovery_bridge` at
`common/national_focus/ireland_focus_tree.txt:3104` is the main public recovery
focus. It requires late emergency-repeal and review state, then uses the shared
`ireland_cleanup_route_state` effect at
`common/scripted_effects/ireland_effects.txt:4105`.

There is no public-family-specific cleanup effect even though the current
`systems_and_lifecycles.md` requires one per family. There is also no complete
focus sequence for:

- democratic cabinet collapse, coalition fracture, or electoral defeat;
- Congress armed dominance, strike exhaustion, clerical backlash, or supply
  collapse;
- O'Duffy incapacity, army refusal, failed ultimatum, or shortage;
- producer veto, rural-price crisis, or democratic rollback;
- claimant scandal, provincial refusal, army concern, public rejection, or
  abdication.

Events and failure ideas cover parts of this design, but the focus tree normally
funnels failures through one shared bridge and constitutional-calendar proof.
That is recovery infrastructure, not five distinct failure campaigns.

### 8. Postwar systems exist, but route conclusions are not deep enough

The late game is not absent. `ireland_postwar` contains actions for emergency
review, supply replacement, veteran demobilisation, merchant-fleet renewal,
reconstruction, the republic question, Commonwealth relations, UN application,
reconstruction aid, and a conclusion review. It also includes missions such as
`ireland_mission_settle_the_demobilised_forces`,
`ireland_mission_bring_the_republic_settlement_into_force`, and
`ireland_mission_complete_national_reconstruction`. Event and flavour windows
extend to 1956.

The gap is route ownership and focus continuity. The baseline focus tree has a
shared recovery/material-proof sequence and one Atlantic
`ireland_postwar_settlement_office`, but no unmistakable 1946-1951 continuation
for each public family. Rural electrification, emigration, coalition government,
republic status, demobilisation, and reconstruction mainly live in shared
decisions or events. This satisfies the existence of late-game systems but not
the current promise that every family changes its postwar identity and continues
to play after its capstone.

### 9. Event quantity overstates playable event depth

The five event files have the previously reported 511 IDs and extensive exact
option tooltips. Direct source confirms 236 flavour events and 257 route events,
plus territorial and conclusion files.

The ordinary programme dispatcher at
`common/scripted_effects/ireland_runtime.txt:7951` contains 223
`ireland_events.*` launches and 236 `ireland_flavour_events.*` launches, 459
scheduled entries in total. `on_monthly_IRE` calls it once per month at
`common/on_actions/ireland_on_actions.txt:66-94`. A successful dispatch sets a
one-month cooldown at runtime line 18819 using
`event_dispatch_cooldown_months = 1` from
`common/script_constants/ireland_constants.txt:811`.

Even with the programme continuously open from January 1937 to January 1956,
the broker can show at most 114 ordinary events. Route events and flavour events
compete for those slots. The count of 459 scheduled entries therefore cannot be
used as proof that the content is experienced in one campaign.

The declared durable cursor is also not an ordering cursor. It is checked only
for an invalid value at runtime lines 7957-7958, then every monthly scan begins
with event 100. Per-entry limits never compare against the cursor. Earlier
eligible unseen events always take priority, which can starve later route or
postwar material within bounded date windows.

There is also route-identity leakage. For example,
`ireland_flavour_events.500`, labelled F01 De Valera constitutional government,
accepts `ireland_plausible_route_active` or `ireland_absurd_route_active` at
`events/ireland_flavour_events.txt:23-25`, not only the De Valera profile. Its
description at `localisation/english/ireland_l_english.yml:2068` explicitly
describes de Valera's authority. That event can therefore appear after a
plausible or absurd government has replaced him. This is authored text, but its
gate is generic.

### 10. AI coverage exists, but late-game and recovery behavior is not closed

The baseline has a substantial route AI file and focus-ID references are broad.
Family programmes, narrower profile plans, decision AI weights, and event option
AI chances exist. Historical AI is explicitly prevented from using coercive
territorial decisions.

Three O'Duffy surfaces stop at 29 November 1944:

- `IRE_ireland_route_oduffy_personal`, lines 669-672;
- the broader O'Duffy corporate plan, lines 820-825;
- `IRE_ireland_family_fascist_programme`, line 1001.

There is no named fascist postwar or defeat-recovery AI plan that takes over
from that cutoff. Static focus references therefore do not prove that a fascist
AI can finish its family conclusion, recover from a failed demand, or play the
1946-1951 package. The same scenario proof is missing for public-family failure
and recovery more broadly.

### 11. Assets are strong, but the registry and presentation claims are not closed

The baseline has registered focus icons and shines, a territorial decision
category icon, claim/action icons, five territorial report images, three
scripted GUI surfaces, route flags, advisor cards, and event pictures. No
baseline missing-sprite fallback was found for the inspected country package.

The current `docs/plans/ireland_focus_tree/source_of_truth_map.md` still marks
source-backed asset clearance blocked at line 640 and records 166 complete and
three blocked rows at lines 661-662. The remaining exact-person rows are P-26
Patrick Cogan, P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh. They have no
runtime sprite consumers, so this is not a loader or placeholder blocker. It is
an unresolved manifest and documentation gap that contradicts the old final
audit's statement that no asset blocker remains.

The 2026-08-14 user portrait handoff replaces five leader portraits and three
existing advisor cards. It does not resolve P-26, P-45, or P-55.

The major player-facing asset gap is not another icon. It is the lack of a
connected territorial presentation. The baseline provides no territorial GUI,
focus shortcut, dossier, or visible foreshadowing card to explain how the
National Question becomes playable.

## Accepted plans and disposition

| Plan or completion record | Formal disposition | Baseline audit disposition |
| --- | --- | --- |
| `ireland_focus_tree_political_and_territorial_expansion_addendum_2026-08-13.md` | Marked accepted, implemented, and promoted | Formally resolved under the old feature slug. It does not cover the new player-depth correction. Its own body is stale: line 13 says 215 focuses, line 179 says the accepted runtime is 188, and line 782 checks off a 188-focus runtime. |
| `ireland_focus_tree_concrete_reward_density_addendum_2026-08-13.md` | Marked implemented and promoted | Closed for tooltip and direct-effect density, but reopened in substance by the new canonical payoff standard and current user feedback. No cumulative route reward budget proves impact. |
| `ireland_focus_tree_layout_reveal_addendum_2026-08-09.md` | Marked superseded | Historical evidence only. It does not authorize treating the detached territorial island as current completion. |
| `final_combined_completion_audit_2026-08-13.md` | Claims repository completion at static boundary | Stale for the current goal. Lines 221-225 say there are no omissions or blockers, while the 2026-08-14 canonical package explicitly supersedes count-based completion and lists navigation, payoff, failure, AI, and late-game repairs. |
| `docs/specs/ireland_country_package/` | Current source of truth from `df65d37` | Accepted target contract. Its implementation matrix is not yet disposed as implemented, queued, rejected, or superseded. |

There is no unresolved `hoi4_improvement_loop_planner` addendum for the new
`ireland_country_package` feature slug. The older planner addenda are formally
closed or superseded. They should not block a new planner pass after the new
implementation tranches are materially complete.

## Meaningful validation and remaining limits

Performed against the gameplay baseline:

- direct focus parser inventory: 215 unique focus blocks, 27 `allow_branch`
  blocks, exactly three ordinary opening roots, 24 focuses from
  `ireland_define_the_national_question` through the Atlantic conclusion;
- direct reward inventory: 21 construction focuses, 30 equipment focuses, 24
  technology-bonus focuses, eleven uses of the 2-percent minor reward, no focus
  unit creation, and one Marine Service decision unit;
- direct decision comparison of both plebiscite launchers and the shared mission;
- direct territorial crosswalk of state transfers, target response events,
  Wales/Cornwall war goals, resource gates, and resource consumption;
- direct dispatcher crosswalk of 459 scheduled launches, monthly cadence,
  cooldown, cursor use, and date horizon;
- direct AI review of public family plans and the 1944 O'Duffy abort conditions;
- direct source and documentation comparison of focus IDs, route depth,
  postwar systems, assets, and planning dispositions.

Fresh baseline focus inspection and render artifacts:

- focus inspect:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/e800ccc3b3e3a67b36b76b0b0033f571ce089564f6ce2c387d48040a5fd420fe/34106beff1d9cba779577cfb0a55d86ab51e0f3687ff04797d5fd4dfe4853324/focus-inspect.1e67a8146c878756.json`
- focus HTML:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/a9d06b7529a0bbb370351f609ac24dfbf51ea2178212a1163cade9acde24c85e/5229a7787b4643eb9265dd6ee7d2e7112a3b9be416477d2bf66791aa1dc8eaf0/ireland_focus_tree.focus.html`
- focus SVG:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d896988a8486cdcb3b6403090c891004943443fc4cd9758e5d041467d933b0ba/e82293ba2c4fd672c91b91bddeb07f503faf839b9090af293bf3525b2c7c5174/ireland_focus_tree.focus.svg`

The current event workspace scan yielded only a partial workspace-scale artifact:

- event scan:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/7adb8eb7cd26af26cc36b8df2399670896aa2ab97af47729e6ac387cde0c2bfe/f31533c571acc49f5a5b09fd45901f628807c6b210ba3ff85e1335595e139a75/event-scan-586c951a24d6.json`
- narrow route-event lint:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/f8121fa2cba47fe56e840c429b0d19de2fbb579131dd63f35f51f01e1448d904/dfe173c26224619fe85b02f9b7fb16a135f10a82e0ffd4b2d351f018961e0872/event-lint-586c951a24d6.json`

The MCP artifacts support graph and narrow event-source inspection. They do not
prove campaign pacing, player discoverability, route balance, AI recovery,
target-country choice quality, or 1936-1951 scenario completion. The old final
audit also explicitly used a static-source boundary and did not supply those
scenario results.

## Remaining blockers

1. Connected National Question foreshadowing and reflow are absent from the
   committed gameplay baseline.
2. Family gateways are not a readable choice band.
3. The duplicate plebiscite launch path and material-cost bypass are unresolved.
4. Non-coercive Northern settlement lacks a complete transfer, deferment, or
   constitutional reopening lifecycle.
5. Wales and Cornwall lack target response and refusal chains.
6. Coercive operations check but do not consume the promised reserves.
7. Focus and contract reward impact has no current cumulative route budget.
8. Family-specific failure, recovery, conclusion, and cleanup are incomplete.
9. Exceptional focus routes remain simplified against Part 3.
10. Ordinary event dispatch cannot surface most scheduled content and does not
    use its cursor to order the scan.
11. Fascist AI has no demonstrated late-game continuation after its 1944 abort.
12. The three blocked portrait-manifest rows and contradictory completion records
    remain unresolved documentation surfaces.

## Recommended next actions

1. Implement architecture tranche A first. Add the visible Unfinished National
   Question handoff, connect the gateway, move the family and territorial bands,
   preserve exactly three opening roots, and rerender before adding more cards.
2. Reconcile the five public family paths with a route ledger that names each
   selectable focus, institution, decision, failure, recovery, AI handoff, and
   1946-1951 conclusion.
3. Remove the duplicate plebiscite launcher or make it call the same guarded,
   material executor as the existing action. Preserve one mission lifecycle.
4. Implement complete democratic, Congress, producer-estate, and restoration
   Northern outcomes. Include success, counteroffer, failure, partition retained,
   and later reopening where the specification requires them.
5. Add Wales and Cornwall demand events with live target scope, AI choices,
   recorded refusal, cooldown, stale-controller handling, and cleanup before any
   war goal can be issued.
6. Make industrial and territorial operations consume fiction-matched inputs.
   Rebalance the nine contracts as distinct projects instead of a flat 25-PP
   store.
7. Audit every focus into the five reward classes. Replace helper-only or tiny
   payoff cards with named operations, visible institutions, immediate route
   commitments, or historically bounded material results. Produce cumulative
   totals per normal playable route.
8. Expand the exceptional routes only from the canonical Part 3 promises. Give
   High King, Five Provinces, and Otherworld their missing meaningful splits,
   failures, recoveries, and conclusions without exposing them in 1936.
9. Turn the shared postwar system into family-owned continuation. Preserve the
   existing demobilisation, republic, reconstruction, UN, shipping, and
   electrification actions while giving each public family a distinct conclusion
   and continuing loop.
10. Rework ordinary event dispatch around route-owned pools and a real rotating
    cursor. Set a per-campaign event budget that can actually surface the highest
    value events within their date windows.
11. Add explicit AI transitions for failure, postwar government, and territorial
    restraint. Remove or replace the 1944 fascist cutoff with a documented
    defeat, demobilisation, or continuation plan.
12. Reconcile current plans, manifests, specs, and completion reports after each
    tranche. Do not leave the old 188/215 contradiction or no-blocker claim as
    current authority.

## Improvement-loop recommendation

Run one new `hoi4_improvement_loop_planner` pass for
`ireland_country_package` after architecture, payoff, active-system,
territorial, identity, and AI tranches are materially implemented. The current
specification already requires that order. A planner pass before those tranches
would mostly rediscover the gaps recorded here. A planner pass afterward should
test whether the technically working routes have distinct internal conflicts,
historical connections, continuing late-game decisions, non-duplicated support
lanes, and meaningful failure/recovery loops.

No unresolved older planner addendum covers this new campaign-depth gap. The
2026-08-13 political/territorial and reward-density addenda are formally closed
under the older feature contract.

## Audit changes

Only this handoff was created. No gameplay, localisation, asset, manifest,
specification, plan, or thumbnail file was changed by this audit.
