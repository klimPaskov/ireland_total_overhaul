# Expansion decision and mission final audit — 2026-08-13

Mode: active final audit with narrow decision, event, cleanup, localisation,
and documentation patches. No focus source, focus coordinates, report-event
`picture` field, thumbnail, category source, or GUI source was edited.

## Frozen verdict

**No remaining blockers in the political, industrial, territorial-decision,
and territorial-diplomacy event scope.** The Atlantic settlement mission now
has a coherent native mission lifecycle: it closes the review when settlement
work is complete but cannot set the final conclusion. The visible
`ireland_atlantic_settlement_concluded` focus remains the only finalisation
surface.

## Changed files and identifiers

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `common/decisions/ireland_expansion_decisions.txt` | `ireland_territorial_open_postwar_review`; `ireland_mission_complete_atlantic_settlement` | The review could start even if no outstanding holding required settlement; the mission cancellation condition also used the normal success condition and its cancellation set the conclusion flag. | Launch explicitly requires an unresolved relevant holding. Mission success requires extant scope plus every current holding resolved, and `complete_effect` only releases review/capacity flags. Cancellation covers final conclusion, route cleanup removal of the review-start flag, and loss of all scope. |
| same | `ireland_territorial_apply_local_rights_highlands`, `ireland_territorial_apply_local_rights_wales`, `ireland_territorial_apply_local_rights_cornwall`, `ireland_territorial_release_scottish_protectorate`, `ireland_territorial_release_welsh_protectorate`, `ireland_territorial_review_highlands_integration` | A state-control or integration-gate change during the 35-day timer could record settlement despite the action no longer being valid. | Each rechecks its state/review condition through `cancel_trigger`; a changed condition cancels and refunds 25 PP with a specific tooltip. |
| same | `ireland_territorial_reconstruct_scottish_protectorate`, `ireland_territorial_reconstruct_welsh_protectorate` | A subject with no controlled state having a free civilian-factory slot could finish reconstruction without constructing the promised factory. | Availability and cancellation both require the current subject relationship and an owned, controlled state with an `industrial_complex` slot. A changed condition cancels/refunds instead of marking the obligation complete. |
| `common/scripted_effects/ireland_effects.txt` | `ireland_cleanup_route_state` | Route archival cleared only the active mission projection, leaving the Atlantic review-start flag able to keep an activated mission orphaned. | Cleanup also clears `ireland_atlantic_postwar_review_started`; the mission's cancellation branch releases the remaining capacity state. |
| `events/ireland_territorial_diplomacy_events.txt` | `ireland_territorial_diplomacy.3`, `.5`, `.8`, `.9`, `.11`, `.13`, `.15` | Several recipient and Irish counteroffer options had no AI weight. | Every real multi-option response uses the existing 20/35/45 accept/counteroffer/refusal table. All terminal branches retain cooldown and global-event-target cleanup. Parent-owned report-event `picture` fields were preserved unchanged. |
| `localisation/english/ireland_l_english.yml` | `ireland_territorial_postwar_unresolved_requirement_tt`, `ireland_territorial_protectorate_reconstruction_site_requirement_tt`, `ireland_territorial_reconstruction_cancelled_tt`, `ireland_territorial_settlement_review_cancelled_tt` | The new state-dependent availability/cancellation cases were not player-explained. | Adds exact player-facing requirement and refund explanations. UTF-8 BOM retained. |
| `docs/ireland_political_industrial_and_territorial_expansion.md` | Territorial policy overview | The mission description implied its completion was the conclusion. | Documents the distinct review-completion and explicit-focus finalisation steps. |

## Issue list, resolved by severity

1. **High — conclusion bypass / orphaned mission:** `cancel_trigger` contained
   the same all-resolved condition used by mission completion, while
   `cancel_effect` set `ireland_atlantic_settlement_concluded`. Under native
   mission semantics that could bypass the explicit conclusion focus. Resolved
   as described above. The stale
   `ireland_atlantic_state_settlement_recorded` clear was removed; the flag has
   no current setter and is not part of the per-holding ledger.
2. **High — false protectorate reconstruction completion:** an absent free
   building site still allowed the reconstruction-complete flag. Resolved with
   subject/site availability and cancellation proof.
3. **Medium — settlement recorded after loss of state or integration gate:**
   six timed settlement decisions lacked lifecycle revalidation. Resolved with
   cancel/refund branches.
4. **Medium — non-player diplomacy could select unweighted counteroffer
   responses:** resolved with the existing central event-file AI table.
5. **Low — unavailable review launch lacked a precise unresolved-holding
   explanation:** resolved through a custom trigger tooltip.

## Category lifecycle notes

- `ireland_provision` contains nine one-use company contracts. They are visible
  only after their company flag, spend 25 PP over 35 days, and use named
  industrial/material outputs. The Belfast refit additionally requires state
  119 to remain Irish-owned and controlled. All have finite `fire_only_once`
  lifecycles and route-aware AI weights; no contract creates a repeatable
  equipment, factory, or experience loop.
- `ireland_territorial_policy` is original-Ireland and route/archival gated by
  its category. Northern policy, diplomatic demand, direct claim, and postwar
  decisions are visible through their exact route flags and retire with their
  completion flags. The active-diplomacy flag serialises all response windows.
- The staged coercive route is State 119 ultimatum → refusal/counteroffer →
  separate final enforcement, then Highlands → Wales → Cornwall. Direct
  Wales/Cornwall claims require the prior issued war-goal flag, exact foreign
  controller, no shared faction, readiness, and the relevant sea-region plus
  controlled naval-base proof.

## Mission quality note

| Mission | Owner/category | Region and requirement | Duration | Success | Failure/cancel | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `ireland_mission_complete_atlantic_settlement` | Ireland / Territorial Policy postwar review | Any currently Irish-controlled 120/122/123 or SCO/WLS subject; every such holding must have its own settlement/reconstruction record | 365 days | Native `available`: scope still exists and all relevant holdings resolve; clears review and capacity state only | No scope, route cleanup, or final focus cancels cleanly. Timeout penalises only unresolved holdings, archives the review, and releases capacity. | Prevented by one review-start flag, mission active flag, capacity helper, and explicit terminal cleanup. |

## Cost, requirements, AI, and cleanup findings

- The claim path uses 50 PP/70 days, exact controller `strength_ratio`,
  readiness stocks, Dáil support, peace, staged flags, and 180-day
  state-specific war goals. Final-tick revalidation refunds cancellation rather
  than granting a stale war goal.
- The postwar and local-rights surfaces use 25 PP/35 days. Their player-facing
  descriptions and new requirement/cancellation tooltips reflect current
  world-state gates.
- Recipient event choices now use declared 20/35/45 weights; historical AI is
  explicitly zeroed for coercive decision actions. Invalid/dead controller
  paths are handled by stale-result branches that refund, cool down, clear
  pending flags, and clear all three global targets.
- `ireland_clear_territorial_diplomacy_targets` clears requester, controller,
  and state pointers on every reviewed terminal event branch. The shared
  cooldown is assigned through its script constant using a temporary duration
  variable, which is appropriate for native timed flags.
- All expansion decision icon tokens resolve in `interface/ireland_icons.gfx`;
  category sprite and external claim DDS references are present. The five
  current territorial event picture sprite tokens resolve in
  `interface/ireland_event_art.gfx`; those parent-owned picture lines were not
  modified.

## Validation

- Confirmed map validity and inspected states 119, 120, 122, and 123 with the
  HOI4 map inspector. Artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/61c6c0781053cf78457013ae6b71724f36e955cdd8c71a37c99ca7643714a2cd/cf5fe27f84d4b6311ffcc92e3c71b379d9a7f0dfb667c7911eb7833f8218e2c5/map-inspect.91e3eb29d9c6b0ee.json`.
- Ran focused event lint for `events/ireland_territorial_diplomacy_events.txt`.
  It reports no blocking diagnostic; the tool labels the full-workspace helper
  projection partial because of workspace scale. Artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/14b2d51efd645240a35f0fbfb29b83dbc9dce288b48e090551ade7e74ddf9ff9/60d68ccc174187abf56594f411135788ecf19df39c2c7c119655fe7429231f5c/event-lint-586c951a24d6.json`.
- Cross-checked native mission, `cancel_trigger`, state iteration, and free-slot
  syntax against the offline wiki and vanilla documentation/decision
  precedents. Verified every territorial event custom-effect tooltip (31), all
  five event-picture sprite tokens, and all 11 decision icon tokens resolve.

## Skipped meaningful validation

No engine-session simulation was available for a day-by-day mission timeout,
subject release, or controller-change transition. Static native semantics,
vanilla precedents, focused event lint, and exact trigger/effect-path review
are the available confidence evidence.

## Remaining blockers

None in this audit scope. No plan handoff is required.
