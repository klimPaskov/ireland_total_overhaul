# Ireland decision requirement-risk audit — 2026-07-26 sidecar 01

**Scope:** bounded, static comparison of the canonical decision/mission map and Part 5 against the current `ireland` decisions, triggers, constants, and English localisation. This is audit evidence only; it does not establish feature completion or live-game behaviour. The two findings below were subsequently closed at source level by `docs/plans/ireland_focus_tree/historic_site_patrol_craft_implementation_tranche_2026-07-26.md`; live engine and scenario behaviour remain open.

## Closed canonical rows (static source evidence)

- **Dynamic material admissions:** the previously open rows are paired gates and deductions in `ireland_action_expand_folklore_collection`, `ireland_action_negotiate_british_flexibility`, and `ireland_action_merge_tax_and_debt_administration`. The last also has state 119 and a live named creditor route.
- **Aircraft:** `ireland_action_intercept_an_airspace_violation` requires the incident and intercept authority, an air base, fighters, and fuel; its completion effect removes the fighter equipment and fuel.
- **Tied units / no free contribution:** `ireland_action_integrate_a_voluntary_member_contribution` requires `ireland_has_regional_contribution_force`, route/policy safeguards, and support equipment before its linked mission can run. `ireland_action_fulfil_a_compact_obligation` likewise names a real division through its stewardship-force trigger.
- **Foreign-channel and safeguard admissions:** source and the 26 July tranche evidence close the explicit live-channel/cause/creditor checks for `ireland_action_share_a_controlled_weather_report`, `ireland_action_release_or_exchange_internees`, `ireland_action_open_a_g2_liaison_channel`, `ireland_action_formalise_plan_w_liaison`, `ireland_action_mobilise_diaspora_relief`, `ireland_action_receive_a_german_emissary`, `ireland_action_procure_rifles_and_support_equipment`, `ireland_action_recognise_a_liberated_authority`, and `ireland_action_merge_tax_and_debt_administration`.
- **Deadlines, partial/failure, cleanup, and AI:** the static inventory is 140 action blocks and 54 mission blocks. The mission blocks contain mission timeout, cancellation, timeout resolution, partial/failure handling, route-state cleanup, and `ai_will_do`; action blocks contain route-state cleanup and `ai_will_do`. This is token/source coverage, not a live scenario result.

## Historical findings - closed at source level

1. **Closed — local support and maintenance for the `Protect a Historic Site` row.**
   - Canonical row: **Protect a Historic Site** requires guards, transport, **local support**, and maintenance.
   - The action now requires site-local support/authority, Social Consent, regional participation, state 135 control, manpower, trucks, and Support Equipment maintenance supply; its direct cultural-ledger result rechecks the admission contract.
   - Evidence: `docs/plans/ireland_focus_tree/historic_site_patrol_craft_implementation_tranche_2026-07-26.md` and the current decision, trigger, effect, and localisation sources.

2. **Closed — patrol craft are tied to the `Organise Marine Patrols` / `Patrol the Neutral Approaches` rows.**
   - Canonical rows: **Organise Marine Patrols** and **Patrol the Neutral Approaches** call for small craft/craft coverage, fuel, crews, rescue/inspection coverage, and repair.
   - The action now binds an action-specific dedicated patrol-craft coverage flag to its 3-Convoy craft allocation, with fuel, crews, rescue, inspection, and repair gates. The Neutral Approaches map objective rechecks that flag and terminal paths clear it.
   - The canonical map and tooltip explicitly state that the convoy charge represents dedicated patrol craft rather than ordinary merchant stock. No unit is spawned, moved, deleted, or mutated.
   - Evidence: `docs/plans/ireland_focus_tree/historic_site_patrol_craft_implementation_tranche_2026-07-26.md` and the current decision, trigger, effect, and localisation sources.

## Risk notes and exclusions

The findings above are retained as the original audit snapshot, with the current disposition recorded inline. The implementation tranche adds the historic-site local-support and maintenance admission plus its direct-result recheck, and adds an action-specific patrol-craft commitment bound to the Convoy charge and rechecked by the Neutral Approaches map objective. It does not spawn, move, delete, or mutate units, and it preserves the canonical H/P/A boundary.

- The patrol craft are represented by an action-specific bound allocation rather than a physical naval unit. This is sufficient for the source-level objective and cleanup contract, but live overlap behavior and mission feasibility still require engine validation.
- No additional missing aircraft, foreign safeguard, leverage, or material-charge row was found in this bounded pass. AI target validity and route/sponsor invalidation remain static-only evidence; their runtime resolution was not exercised.
- `civilian_factory_use` on the Republic-question decision was excluded as a false positive: it is an active decision modifier, not an unpaired completion-time material charge, and has a vanilla `common/decisions/AST.txt` precedent.

## Evidence consulted

- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md`
- `common/decisions/ireland_decisions.txt`
- `common/scripted_triggers/ireland_triggers.txt`
- `common/script_constants/ireland_constants.txt`
- `localisation/english/ireland_l_english.yml`
- Relevant 2026-07-26 material, foreign-channel, readiness, and mission-lifecycle tranche evidence under this plan directory.
