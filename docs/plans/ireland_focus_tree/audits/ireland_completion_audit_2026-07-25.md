# Ireland Completion Audit — 2026-07-25

## Verdict

The `ireland_focus_tree` overhaul remains incomplete. This audit was read-only; no HOI4 process was launched and no gameplay files were changed by the auditor.

## Confirmed structural surfaces

- 216 national focuses with the regenerated v4 goal-icon package bound to the runtime `gfx` path.
- 13 decision categories, 140 actions, and 54 mission families.
- 251 main events and 236 flavour events.
- 30 durable AI profiles, 10 temporary overlays, and 32 achievement definitions.
- Northern claim/control/occupation/settlement/integration/core separation is present in source; the sole Ireland core grant remains behind the final review helper.
- Neutrality Integrity opens at 72 and the incident signals are separated into the authored incident families.

## Blocking findings

1. Source clearance is incomplete: 28 review-gated and 102 blocked manifest rows remain, including review-gated portraits used by live character content.
2. The required engine/reference and 22 scenario-family validation programme has not been run. Live focus/event/mission timers, AI queues, GUI state and clicks, animation playback, dynamic localisation, Northern transitions, neutrality cleanup, hidden content, and achievement disqualifiers remain unproven.
3. The canonical 140-row material/safeguard disposition is not closed. Aggregate progress is 61 actions with physical or manpower inputs, 33 refund branches, and 12 factory reservations; remaining action-specific leverage, tied-unit, aircraft, ship, local-support, and foreign-channel cases still need per-ID evidence.
4. The standard event and repeated action-description template findings are closed at source level; mission descriptions still require an objective-by-objective review against the 54 canonical mission families, and the 140-row action/material mapping remains open.
5. A-22, A-27, and A-28 are permanently hidden despite the staged-visibility contract requiring later reveal conditions.
6. Much of the implementation remains modified or untracked in the worktree and therefore is not yet reproducibly integrated beyond the committed goal-icon tranche.

## Current positive evidence

- The reconstruction-aid action now requires the named FR11/RC07 foreign or multilateral programme offer lifecycle rather than a postwar date alone. See `docs/plans/ireland_focus_tree/reconstruction_aid_programme_gate_tranche_2026-07-25.md`.
- `Review Commonwealth Relations` now requires a recorded constitutional or republican status transition before its British-relations review can open. See `docs/plans/ireland_focus_tree/commonwealth_status_gate_tranche_2026-07-25.md`.
- Static H14 wartime-unity lifecycle tranche is documented in `docs/plans/ireland_focus_tree/wartime_unity_lifecycle_tranche_2026-07-25.md`.
- Static goal-icon v4 QA, contact sheet, DDS checks, and runtime promotion are documented in the Ireland asset handoff and icon QA records.
- The focus reachability tranche found 216 unique IDs, zero unknown prerequisite references, and removed the eleven circular ready-flag entry gates identified by the focus auditor; see `docs/plans/ireland_focus_tree/focus_reachability_gate_tranche_2026-07-25.md`.
- The route-voice tranche now covers the standard event surface with 220 unique descriptions, 217 unique standard `a`/`b` choices, and 236 distinct flavour-event descriptions; all 140 action descriptions are also unique after the route-specific tail cleanup, while mission descriptions remain open. See `docs/plans/ireland_focus_tree/localisation_route_voice_tranche_2026-07-25.md`.
- The repository’s current project status and source-of-truth map retain the open blockers rather than treating static counts as completion.

## Engine-reference result: staged achievement visibility

The required staged visibility for A-22, A-27, and A-28 cannot be expressed by the stock custom-achievement schema consulted for this feature. The offline achievement reference documents only `possible`, `happened`, and static `hidden`; it states that `possible` is evaluated at game start. The installed vanilla precedent in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\achievements.txt` uses `hidden = yes` as a fixed definition field and contains no trigger-valued visibility field. Therefore, replacing the three static `hidden = yes` entries with an undocumented `visible = { ... }` block would be an unverified engine fallback, while removing `hidden` would expose them before their canonical reveal flags. The source remains intentionally unchanged and this is an engine-reference blocker, not a silently accepted simplification.

## Post-audit implementation notes

The reconstruction-aid programme-offer gate is closed for that action specifically; the broader 140-row material/safeguard disposition remains open.

The Commonwealth status-transition gate is closed for that action specifically; broader postwar action mapping, mission review, source clearance, and live validation remain open.

The focus reachability finding is closed at source level. Four other route
milestones still use their own ready markers alongside external route state;
they were not part of the audited dead chain. The standard event route-voice
finding and repeated action-description tails are closed at source level by the
expanded tranche; mission wording, action/material mapping, and live
localisation checks remain completion blockers.

## Disposition

No fallback, shortened route, generic ideology replacement, free Northern core, or HOI4 launch was used in this audit. Do not mark the goal complete until the blocking findings are resolved and the full validation programme has fresh evidence.
