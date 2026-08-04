# Ireland Decisions and Missions Audit Handoff — 2026-07-29

## Scope and authority

This is a source-only audit of the Ireland decision surface. It replays the exact
140-action / 54-mission inventory in
`docs/plans/ireland_focus_tree/action_material_safeguard_ledger_2026-07-29.md`
against `common/decisions/ireland_decisions.txt`, the canonical Ireland
decision/mission map and lifecycle documents, matching triggers/constants,
localisation, and the directly referenced member-contribution event. No live
HOI4 test was run by request.

The audit snapshot did **not** decide the existing Radical/Underground
canonical contradiction. That historical uncertainty was later resolved by
the approved M2 ruling in
`docs/plans/ireland_focus_tree/authority_rulings_m2_a2_c3_2026-08-01.md`.

## Sources and precedents checked

- Required offline Paradox wiki pages: Data structures, Triggers, Effects,
  Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding,
  Idea modding, and AI modding.
- Vanilla documentation: decision schema, effects, triggers, script constants,
  and script concepts documentation.
- Vanilla decision precedents: `common/decisions/FIN.txt` and
  `common/decisions/BALTIC.txt`.
- By Blood Alone precedent: `events/BFTB_Bulgaria.txt` uses a
  `NOT = { has_dlc = "By Blood Alone" }` legacy-fighter branch and the
  `small_plane_airframe` BBA branch. `common/units/equipment/plane_airframes.txt`
  defines `small_plane_airframe` as an archetype.
- Vanilla stockpile precedent: `events/SOV.txt` removes generic
  `infantry_equipment` with negative `add_equipment_to_stockpile`; official
  effects documentation explicitly states that negative amounts remove
  equipment.
- Canonical Ireland sources: focus-tree index, decision/mission prompt,
  decision-and-mission map, part 5 lifecycle specification, lifecycle matrix,
  and the material-safeguard ledger named above.

The read-only `hoi4.event_inspect` attempt was rejected as evidence because it
selected a different workspace. The direct source trace below is authoritative
for this audit. There is no decision-owned scripted GUI declaration in the
Ireland decision file, so no GUI artifact applies.

## Inventory reconciliation

The ledger was replayed one source block at a time. All entries resolve to one
unique decision block and no decision block is absent from the ledger.

| Category | Actions | Missions | Audit result |
|---|---:|---:|---|
| Settlement Government | 10 | 3 | matched |
| Elections | 10 | 2 | matched to the approved M2 merge |
| Society | 10 | 2 | matched to the approved M2 merge |
| Cultural Restoration | 10 | 3 | matched |
| Radical / Underground | 10 | 2 | matched to the approved M2 inventory |
| Provision | 16 | 10 | matched |
| Readiness | 14 | 8 | matched |
| Neutrality | 10 | 4 | matched |
| Foreign Affairs | 10 | 4 | matched |
| Northern Question | 10 | 4 | matched |
| Occupation Administration | 10 | 4 | matched |
| Regional Order | 10 | 3 | matched |
| Postwar Settlement | 10 | 5 | matched |
| **Total** | **140** | **54** | **matched** |

The complete per-ID action evidence remains the 140 ledger rows in
`action_material_safeguard_ledger_2026-07-29.md`; it was verified rather than
accepted on trust. The following source mission manifest is the exact
54-ID replay, including owner, named objective family, and deadline.

| Mission ID | Owner action(s) | Objective family / region | Days |
|---|---|---|---:|
| `ireland_mission_maintain_cabinet_discipline` | `ireland_action_convene_a_cabinet_cohesion_review` | Dáil / national cabinet | 90 |
| `ireland_mission_assemble_seventy_votes` | `ireland_action_request_a_confidence_vote` | Dáil confidence vote | 45 |
| `ireland_mission_complete_the_six_month_review` | `ireland_action_review_the_six_month_settlement` | national constitutional review | 180 |
| `ireland_mission_conduct_a_free_election` | `ireland_action_update_the_electoral_register` | contested electoral areas | 105 |
| `ireland_mission_form_a_government` | `ireland_action_open_coalition_negotiations` | Dáil coalition | 60 |
| `ireland_mission_protect_the_by_election` | `ireland_action_prepare_a_by_election` | constituency campaign | 100 |
| `ireland_mission_conclude_the_education_compact` | `ireland_action_negotiate_an_education_compact` | education network | 150 |
| `ireland_mission_settle_the_essential_service_dispute` | `ireland_action_mediate_an_essential_service_dispute` | essential services | 60 |
| `ireland_mission_audit_parish_service_dependency` | `ireland_action_audit_church_service_dependency` | parish-service network | 120 |
| `ireland_mission_expand_the_folklore_collection` | `ireland_action_expand_the_folklore_collection` | Gaeltacht / provincial archive | 180 |
| `ireland_mission_hold_the_provincial_cultural_congress` | `ireland_action_hold_a_provincial_cultural_congress` | provincial cultural centres | 210 |
| `ireland_mission_test_the_restoration_claim` | `ireland_action_test_the_restoration_claim` | archives and historic sites | 270 |
| `ireland_mission_meet_the_tillage_quota` | `ireland_action_set_county_tillage_quotas` | rural counties | 150 |
| `ireland_mission_secure_the_harvest` | `ireland_action_repair_mills_and_storage` | rural-to-city food route | 120 |
| `ireland_mission_establish_protected_workshops` | `ireland_action_license_protected_workshops` | industrial workshops | 180 |
| `ireland_mission_commission_the_developmental_plant` | `ireland_action_commission_a_developmental_plant` | development plant | 270 |
| `ireland_mission_stabilise_winter_rations` | `ireland_action_issue_ration_books` | Dublin ration network | 120 |
| `ireland_mission_mobilise_emergency_turf` | `ireland_action_mobilise_emergency_turf` | Midlands / western fuel districts | 120 |
| `ireland_mission_repair_the_dublin_cork_corridor` | `ireland_action_repair_the_dublin_cork_rail_corridor` | Dublin–Cork rail corridor | 180 |
| `ireland_mission_keep_an_essential_cargo_route_open` | `ireland_action_charter_foreign_tonnage`; `ireland_action_reroute_essential_cargo`; conditional procurement branch of `ireland_action_procure_rifles_and_support_equipment` | state 135–113 cargo route | 120 |
| `ireland_mission_purchase_a_merchant_vessel` | `ireland_action_purchase_a_merchant_vessel` | merchant fleet | 270 |
| `ireland_mission_fund_the_western_regional_portfolio` | `ireland_action_fund_a_western_regional_portfolio` | western regional portfolio | 300 |
| `ireland_mission_run_the_command_district_exercise` | `ireland_action_run_a_command_district_exercise` | command district | 105 |
| `ireland_mission_activate_the_cadre_reserve` | `ireland_action_activate_the_cadre_reserve` | mobilisation districts | 150 |
| `ireland_mission_motorise_the_strategic_route` | `ireland_action_motorise_the_strategic_route` | Dublin–Belfast corridor | 120 |
| `ireland_mission_build_the_coastwatch_network` | `ireland_action_build_a_coastwatch_network` | coastwatch sectors | 120 |
| `ireland_mission_install_harbour_defences` | `ireland_action_install_harbour_defences` | treaty-port / harbour sectors | 210 |
| `ireland_mission_organise_the_marine_patrols` | `ireland_action_organise_marine_patrols` | coastal sectors and ports | 105 |
| `ireland_mission_protect_the_operational_plan` | `ireland_action_protect_the_operational_plan` | border commands | 120 |
| `ireland_mission_demobilise_the_force_tier` | `ireland_action_demobilise_a_force_tier` | national force posture | 210 |
| `ireland_mission_intern_belligerent_aircrew` | `ireland_action_intern_belligerent_crew` | internment site | 90 |
| `ireland_mission_investigate_the_neutral_shipping_loss` | `ireland_action_investigate_a_neutral_shipping_loss` | shipping-loss route / home port | 120 |
| `ireland_mission_mark_equal_neutrality` | `ireland_action_mark_and_publicise_neutral_shipping` | neutral-shipping channels | 150 |
| `ireland_mission_share_the_blacksod_weather_report` | `ireland_action_share_a_controlled_weather_report` | Blacksod, Mayo | 105 |
| `ireland_mission_secure_the_british_delivery` | `ireland_action_renegotiate_the_british_supply_contract`; conditional procurement branch of `ireland_action_procure_rifles_and_support_equipment` | British–Irish supply route | 150 |
| `ireland_mission_secure_the_american_delivery` | `ireland_action_send_an_american_procurement_mission`; conditional procurement branch of `ireland_action_procure_rifles_and_support_equipment` | Atlantic / American procurement route | 240 |
| `ireland_mission_secure_the_german_delivery` | `ireland_action_demand_proof_of_german_delivery`; conditional procurement branch of `ireland_action_procure_rifles_and_support_equipment` | German delivery route | 150 |
| `ireland_mission_seek_vatican_mediation` | `ireland_action_seek_vatican_mediation` | Vatican humanitarian channel | 120 |
| `ireland_mission_open_cross_border_confidence` | `ireland_action_open_cross_border_confidence` | border districts | 150 |
| `ireland_mission_convene_the_northern_convention` | `ireland_action_invite_northern_delegates` | Belfast / Derry convention | 210 |
| `ireland_mission_protect_the_northern_plebiscite` | `ireland_action_protect_northern_campaign_freedom` | Northern campaign districts | 240 |
| `ireland_mission_convene_the_federal_powers_conference` | `ireland_action_convene_a_federal_powers_conference` | Dáil / Northern / British conference | 300 |
| `ireland_mission_plan_the_belfast_operation` | `ireland_action_plan_a_coercive_campaign` | Belfast | 150 |
| `ireland_mission_vet_and_rebuild_policing` | `ireland_action_vet_and_rebuild_policing` | Northern policing districts | 240 |
| `ireland_mission_restore_belfast_industry` | `ireland_action_restore_belfast_contracts` | Belfast industry / state 119 | 300 |
| `ireland_mission_complete_the_northern_stage_five_review` | `ireland_action_conduct_a_core_eligibility_review` | all Northern administration | 365 |
| `ireland_mission_draft_the_atlantic_charter` | `ireland_action_invite_a_celtic_partner` | member capitals | 240 |
| `ireland_mission_integrate_the_voluntary_member_contribution` | `ireland_action_integrate_a_voluntary_member_contribution` | contributing member states | 180 |
| `ireland_mission_fulfil_the_compact_obligation` | `ireland_action_fulfil_a_compact_obligation` | five compact sites | 300 |
| `ireland_mission_replace_emergency_rations` | `ireland_action_replace_emergency_supply` | national urban supply | 240 |
| `ireland_mission_demobilise_and_settle_veterans` | `ireland_action_demobilise_and_settle_veterans` | national veteran settlement | 300 |
| `ireland_mission_settle_the_republic_question` | `ireland_action_settle_the_republic_question` | Dáil / presidency | 150 |
| `ireland_mission_apply_for_un_membership` | `ireland_action_apply_for_un_membership` | eligible members / Security Council | 300 |
| `ireland_mission_launch_the_reconstruction_portfolio` | `ireland_action_launch_a_reconstruction_portfolio` | three reconstruction regions | 365 |

## Corrected findings

### High — BBA airframe admission and consumption was blind to custom designs (fixed)

**Identifiers:** `ireland_action_intercept_an_airspace_violation`,
`@IRELAND_AIRSPACE_INTERCEPT_FIGHTER_GATE`,
`@IRELAND_AIRSPACE_INTERCEPT_FIGHTER_CHARGE`.

The interrupted patch only scanned six legacy concrete fighter types. That
excluded By Blood Alone custom designs, which vanilla represents through the
`small_plane_airframe` archetype rather than one of those legacy equipment
tokens.

The repaired action is DLC-aware:

- with By Blood Alone, admission is `small_plane_airframe > 4` and the effect
  removes five `small_plane_airframe`;
- without By Blood Alone, the first stockpile containing five of the existing
  six legacy fighter types is charged five units;
- both branches preserve the existing 100-fuel charge, and neither can
  overdraw its checked material.

Negative `add_equipment_to_stockpile` on `small_plane_airframe` is a
source-level inference supported by the archetype definition, official effect
documentation, and vanilla generic-archetype removal. No vanilla file was
found using that exact negative BBA airframe form, and live verification is
explicitly excluded from this task.

### Medium — Dublin–Cork rail fuel gate rejected an exact payment (fixed)

**Identifiers:** `ireland_action_repair_the_dublin_cork_rail_corridor`,
`@IRELAND_RAIL_CORRIDOR_FUEL_GATE` in both the decision and matching
Ireland trigger file.

The action consumes 200 fuel but tested `has_fuel > 200`, which requires 201.
The gate is now `> 199`, so exactly 200 fuel is valid and the visible 200-fuel
charge is exact.

## Action-category lifecycle notes

- Every action has a visible gate, individual lock/removal path, native PP
  cost, dynamic custom-cost requirement text, matching material/CP/other
  admission logic, Action Burden, AI weight, and removal effect.
- The highest static command-power payment is 35 plus a maximum scarcity
  surcharge of 10, or 45 total. This remains below the canonical 60 CP ceiling.
- There are 112 direct material charge lines. Replaying their gate/charge
  pairs found 15 helper-owned or literal-equivalent checks; each was traced.
  After the rail correction, every strict `>` material gate admits the exact
  requested payment (gate is one lower than the positive charge).
- All 59 mission activation call sites resolve to the 54 manifest IDs. The
  five repeated activation sites are intentional: three procurement delivery
  branches select one mutually exclusive supplier via the source variable, and
  the remaining two reuse the cargo mission through distinct, normal route
  actions.
- The global mission capacity helper resolves to the canonical 8 / 10 / 12
  ladder, with one / two / three critical reserves. Every action that starts a
  mission refreshes the relevant capacity counters.

## Mission quality and lifecycle notes

- All 54 are automatic (`selectable_mission = no`) and good missions.
- All 54 have an activation condition, `available` requirement, a localised
  named map-objective tooltip, deadline, completion effect, timeout effect,
  cancellation condition/effect, AI weight, and each of the canonical
  outcome records: 1 full success, 2 partial success, 3 failure, 4
  cancellation, and 5 escalation.
- Deadline range is 45–365 days; the manifest above records each duration.
- Mission result branches, not a generic `remove_effect`, own their cleanup.
  A generic source scan therefore reported no `remove_effect` on mission
  blocks, but this is not a missing lifecycle implementation.
- 33 material-heavy missions invoke
  `ireland_refund_cancelled_material_inputs`. Its one-time action guard
  prevents cancellation farming; the per-action helper supplies capped
  recoveries. The rail case, for example, returns 3 trains, 175 manpower, and
  140 fuel only on eligible cancellation.
- Foreign route actions and missions use partner validity checks (existing,
  sovereign, non-capitulated) at admission, activation, objective, and route
  closure/cancellation points. The related owner actions have AI weights and
  route-lock cleanup. The one direct decision event reference,
  `ireland_events.431`, is defined in
  `events/ireland_member_contribution_events.txt`; its five paid choices
  also have availability, AI weights, and one-time cleanup. No event change
  was made.

## Outstanding issues and uncertainty, sorted by severity

### Closed - action and category reveal contracts

The earlier pre-reveal finding is superseded by the separate
`docs/plans/ireland_focus_tree/action_reveal_contract_handoff_2026-07-29.md`.
The current source has one reusable `ireland_reveal_*` call inside each
of the 140 action `visible` blocks, and the thirteen category headers each call
their matching category reveal helper. The action helpers are backed by the
authored opening, recovery, route, incident, dated, occupation-stage, and
concealed-authority conditions; they do not alter action availability, costs,
mission capacity, AI, or cleanup.

The handoff's static recheck records 140/140 action reveal calls, 13 category
helpers, 123 action-stage helpers, and one category parent for every action
helper. This closes the audit finding without changing the approved
13-category / 140-action / 54-mission inventory. No additional gameplay change
is required for this row; live HOI4 testing remains excluded by user direction.

### Closed by later authority — Radical/Underground mission ownership

The historical audit snapshot recorded ten Radical/Underground actions and no
mission while the canonical category material reserved two mission families.
The approved M2 ruling now assigns ordinals 006 and 009 to the physically
nested `Consolidate the Movement Network` and `Secure Constituent Authority`
missions. The by-election and parish-audit modes remain distinct modes of the
base election and essential-services missions, preserving exactly 13
categories, 140 actions, and 54 missions. The current source-structure proof
is `docs/plans/ireland_focus_tree/audits/ireland_m2_category_ownership_audit_2026-08-01.md`.

### Non-live confidence boundary — BBA archetype subtraction

The DLC-aware repair uses `add_equipment_to_stockpile = { type =
small_plane_airframe amount = -5 }`. Its validity is well-supported by local
documentation and archetype precedents, but no exact vanilla negative
`small_plane_airframe` example was found. A runtime test would be the final
engine confirmation, and was intentionally not performed.

## Files changed by this audit

- `common/decisions/ireland_decisions.txt`
  - `ireland_action_intercept_an_airspace_violation`: BBA-aware aircraft
    admission and consumption.
  - `@IRELAND_RAIL_CORRIDOR_FUEL_GATE`: exact 200-fuel admission.
- `common/scripted_triggers/ireland_triggers.txt`
  - matching `@IRELAND_RAIL_CORRIDOR_FUEL_GATE`: exact 200-fuel
    admission.
- `docs/plans/ireland_focus_tree/audits/ireland_decision_mission_audit_handoff_2026-07-29.md`
  - this audit and handoff.

No localisation, focus, event, GUI, asset, specification, achievement, or
unrelated workspace file was changed.

## Non-live validation performed

- Reconciled exact source counts: 140 actions, 54 missions, 13 categories.
- Replayed all action cost gates and charges; verified the 45 CP maximum and
  the 8/10/12 capacity ladder with reservations.
- Checked every mission's objective, duration, result record, deadline,
  cancellation, route/cap cleanup, and AI hook.
- Traced all repeated mission activations, foreign target validity helpers,
  refund guard paths, matching localisation keys, and the member-contribution
  event reference.
- Compared the BBA branch to local vanilla DLC guards, archetype definitions,
  and stockpile-removal documentation.

Skipped: live HOI4 load/save/gameplay testing, by user direction.
