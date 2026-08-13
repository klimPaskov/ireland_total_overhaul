# Territorial diplomacy and settlement implementation handoff

Date: 2026-08-13
Owner: `/root/territorial_diplomacy_settlement`
Parent: `/root`

## Scope delivered

The territorial response chain is implemented in `events/ireland_territorial_diplomacy_events.txt` under the `ireland_territorial_diplomacy` namespace. The chain is explicitly event-driven and stores the requester, target controller, and target state in global event targets until a terminal response cleans them up.

Event IDs:

- `.1-.4`: State 119/Ulster ultimatum, including target-controller accept/counteroffer/refusal and requester-side resolution.
- `.5-.8`: Belfast compact, including accept/counteroffer/refusal and requester-side resolution.
- `.9-.12`: State 120/Highlands demand, including accept/counteroffer/refusal and requester-side resolution.
- `.13-.16`: State 119 border-enforcement follow-up, including accept/counteroffer/refusal and requester-side resolution.

Every player option has an exact `custom_effect_tooltip` key in `localisation/english/ireland_l_english.yml`; terminal options show the state transfer/access/claim/wargoal, ledger, cooldown, and cleanup effects.

`common/decisions/ireland_expansion_decisions.txt` now fires the event phases rather than applying direct self-timed coercion for the State 119 ultimatum, Belfast compact, State 119 enforcement, and Highlands demand. Each decision saves the requester/controller/state targets and sets a pending flag. Wales and Cornwall escalation require staged naval proof from `common/scripted_triggers/ireland_triggers.txt`:

- Wales: Irish control of a naval base in state 120 plus naval control of strategic region 2 (Northern England).
- Cornwall: Irish control of a naval base in state 122 plus naval control of strategic region 1 (Southern England).

The same trigger file contains `ireland_atlantic_settlement_all_relevant_resolved`, which evaluates each currently controlled state 120/122/123 and requires reconstruction completion for retained SCO/WLS subjects. The postwar conclusion and mission use this trigger; the parent-side cleanup and protectorate reconstruction decisions are preserved.

Each diplomacy decision also checks the timed `ireland_territorial_diplomacy_cooldown` flag, so a completed or stale response cannot immediately reopen the same coercive surface. Stale-result branches apply that cooldown before clearing their saved targets.

## Shared tuning and lifecycle

Ledger deltas and cooldown/wargoal durations use `common/script_constants/ireland_constants.txt` (`territorial_diplomacy_*`). Event-only AI weights and the stale-response political-power refund remain file-local macros because the affected fields are static event fields. There are no daily/on-action polling hooks. `ireland_clear_territorial_diplomacy_targets` is called by every terminal branch; the parent-side route cleanup also clears stale diplomacy flags and reconstruction obligations.

## Validation performed

- Event braces: 176 opening/176 closing; all IDs `.1` through `.16` are unique.
- Decision and trigger files were checked for balanced script blocks after the shared edits.
- All 31 `custom_effect_tooltip` identifiers in the event file have matching localisation keys.
- Event source contains no direct numeric `base`, `value`, or `add_political_power` literals for the response tuning; the ledger values resolve through shared constants.
- The decision source contains event calls for all four diplomatic surfaces and no direct State 119/Highlands coercive wargoal effect in their completion branches.

## Asset blocker and risks

The registered `GFX_report_event_ireland_report_flavour_northern_bridge` is thematically suitable for the Ulster/Belfast chain and remains on events `.1-.8` and `.13-.16`. No exact Scottish Highlands/Scotland settlement report image was registered when this source tranche was written. Events `.9-.12` intentionally omit `picture` rather than reuse Northern Bridge art as a fallback; reconcile those four fields with the dedicated Scottish report art now in production once its exact asset ID and `.gfx` registration are available.

Runtime/headless game validation was not available in this workspace; event-target scope, `transfer_state_to`, `give_military_access`, `create_wargoal`, and naval-base proof follow the consulted vanilla documentation and precedents. Review the Highlands accepted/counteroffer policy flags against the final focus-route expectations during integration.

The per-holding trigger and parent-side reconstruction obligations are intentionally coupled: a retained SCO/WLS subject keeps the conclusion blocked until its corresponding `*_reconstruction_complete` flag is set by the reconstruction decision. Route archival clears both obligation flags and all pending diplomacy targets/flags, preventing stale global state from reopening the chain.
