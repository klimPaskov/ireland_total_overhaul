# Ireland P0/P1 AI Priority — Handoff

Date: 2026-08-14

Owner: `p0_p1_ai_priority`

Scope: Ireland AI strategy, focus-plan routing, and the AI-only runtime queue
projection for family postwar settlement and conclusion recovery. No decision,
focus-tree, trigger, event, constant, localisation, asset, map, or thumbnail
source was edited by this subtask.

## Changed files

- `common/ai_strategy/ireland_ai_strategy.txt`
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`
- `common/scripted_effects/ireland_runtime.txt` (AI queue changes are now
  present in the concurrent `317ce37` territorial-recovery commit; no further
  uncommitted runtime delta remains.)
- This handoff

`common/scripted_effects/ireland_runtime.txt` also contains concurrent parent
P1 territorial-recovery edits (including the workers-border mission counter
surface). Those lines were observed and preserved; they are not part of this
AI patch.

No commit was created by this subtask, per parent instruction. The parent-side
territorial-recovery commit includes the runtime hunks listed above; the
remaining uncommitted source delta from this subtask is limited to the two AI
files.

## Implemented AI contracts

### P0 family recovery ordering

- `ireland_sync_ai_overlays` clears the optional
  `ireland_overlay_postwar_demobilisation_and_reconstruction` and
  `ireland_overlay_route_conclusion_review_and_consolidation` projections while
  `ireland_conclusion_recovery_open` is set.
- `ireland_sync_ai_priority_flags` clears durable/profile-derived
  `ireland_ai_priority_postwar` during the same recovery window, so optional
  postwar work does not retain its postwar multiplier while the family repair
  action is available.
- `ireland_sync_ai_decision_utility` explicitly restores recovery pressure and
  clears stale conclusion pressure while `ireland_conclusion_recovery_open` is
  live. `ireland_sync_ai_candidate_ledger` records the matching postwar repair
  candidate from that marker.
- `ireland_rebuild_mission_counters` treats recovery as a route-review queue
  reservation and sets `ireland_critical_slot_reserved`; routine mission
  admission therefore waits for the family recovery lane, while critical
  missions carrying their own slot marker remain eligible.
- The strategy registry mirrors this rule by disabling optional postwar
  construction pressure during recovery.

### Settlement, conclusion, and material gates

- The existing five family settlement decisions were verified read-only:
  `ireland_action_ratify_the_postwar_republic`,
  `ireland_action_civilianise_the_workers_congress`,
  `ireland_action_place_the_directorate_under_statute`,
  `ireland_action_convert_contracts_to_reconstruction_credit`, and
  `ireland_action_define_the_postwar_crown` add
  `constant:ireland.ai_critical_score` only when
  `ireland_postwar_foundation_ready = yes`.
- The existing five family recoveries were verified read-only to use
  `constant:ireland.ai_recovery_bonus` while
  `ireland_conclusion_recovery_open` is set.
- Their own availability/cost surfaces still own the concrete free-civilian-
  factory requirement. The AI runtime now advertises material readiness only
  when provision, readiness, and
  `num_of_civilian_factories_available_for_projects > 0` all pass.
- The existing route-conclusion decision was verified read-only to require
  `ireland_family_postwar_settlement_complete = yes`; the new post-settlement
  focus plan also waits for that flag before taking optional Atlantic
  postwar-conclusion focuses.

### Historical non-coercion

- `ireland_historical_de_valera` now excludes stale Atlantic force/claim flags
  and raises its `avoid_starting_wars` strategy to 220.
- The historical plan keeps all existing focus references but assigns zero
  factor to `ireland_atlantic_ambition`,
  `ireland_atlantic_security_compacts`,
  `ireland_postwar_settlement_office`,
  `ireland_local_rights_charter`, and
  `ireland_atlantic_settlement_concluded`.

### Ahistorical family Atlantic mapping

The five family plans now carry the shared territorial spine and the compatible
Atlantic outcome only:

| Family plan | Northern policy | Atlantic policy/outcome |
| --- | --- | --- |
| `IRE_ireland_family_democratic_programme` | `ireland_settlement_under_law` | `ireland_atlantic_security_compacts` |
| `IRE_ireland_family_communist_programme` | `ireland_all_island_workers_republic` | `ireland_republics_across_the_channel` |
| `IRE_ireland_family_fascist_programme` | `ireland_force_the_border_question` | `ireland_gaelic_marches`, then `ireland_enforce_atlantic_claims` |
| `IRE_ireland_family_oligarchic_programme` | `ireland_belfast_compact` | `ireland_atlantic_concessions` |
| `IRE_ireland_family_restoration_programme` | `ireland_restore_ulsters_place` | `ireland_dal_riata_claim` after `ireland_high_king_capstone` |

`ireland_postwar_settlement_office`, its three Atlantic review branches, and
`ireland_atlantic_settlement_concluded` are held in
`IRE_ireland_family_postwar_conclusion`, which is enabled only after
`ireland_family_postwar_settlement_complete` and an external policy marker,
and is paused again while `ireland_conclusion_recovery_open` is live.

## Coverage checklist

- Country/tag scope: `original_tag = IRE` preserved in every owned AI strategy
  and plan; no tag or country definition change.
- Politics, leaders, portraits, flags, advisors, and parties: outside this
  AI-only ownership surface; no change claimed.
- Map/state setup: outside this AI-only ownership surface; no map rewrite or
  territorial ownership change claimed.
- Focus loading/route locks: all pre-existing focus refs preserved; only
  existing IDs were reused in family plan routing.
- Decisions/missions: no decision source changed; P0 decision IDs, factory
  costs, foundation/recovery gates, and settlement-before-conclusion gate were
  read-only verified.
- Ideas/assets/localisation: outside this AI-only ownership surface; no asset
  or localisation change claimed.
- Starting military, technology, industry, supply, and production: no direct
  setup change; only AI strategy pressure and material-readiness scoring were
  changed.
- AI/playability: recovery reservations, historical guard, family policy
  routing, and free-factory/material/readiness gating were patched.

## Missing or stale surfaces / remaining risks

1. The P1 territorial-recovery decision identifiers have landed in the
   concurrent `317ce37` commit. Their own decision-level AI weights and
   availability gates are present, so no speculative P1 focus-plan or strategy
   entries were added here; parent can follow up only if live AI testing shows
   a missing route preference.
2. The direct recovery reservation is intentionally in the existing
   `ireland_rebuild_mission_counters` AI scheduler block because that is where
   `ireland_critical_slot_reserved` is rebuilt. Parent review should confirm
   that this shared mission-counter effect remains within the accepted AI-only
   ownership boundary.
3. Engine load/AI runtime simulation was not run. The local workspace had no
   callable HOI4 MCP inspection endpoint in this turn, and an engine launch was
   outside the subagent scope. Parent should validate one blocked family case,
   one foundation-ready settlement case, and one historical AI case in game.

## Validation

- Compared `HEAD` and the working tree: all 218 unique pre-existing focus IDs
  remain present; no focus reference was removed.
- Checked all 218 plan focus IDs against
  `common/national_focus/ireland_focus_tree.txt`; no missing focus ID was found.
- Confirmed the five family-to-Atlantic mappings against the live focus
  availability blocks and restoration's `ireland_high_king_capstone` gate.
- Confirmed balanced Clausewitz braces and ran `git diff --check` on the three
  owned source files.
- Read the offline AI, data-structure, trigger, effect, scope, localisation,
  on-action, event, decision, and idea wiki snapshots plus the vanilla AI
  strategy documentation and plan precedents before editing.

## Skills used

- `hoi4-subagents`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`

No simplification was made within the P0 AI surface. P1 territorial AI-plan
expansion was intentionally omitted because the landed decisions already carry
their compatible policy weights and no stable need for duplicate focus-plan
pressure was established.
