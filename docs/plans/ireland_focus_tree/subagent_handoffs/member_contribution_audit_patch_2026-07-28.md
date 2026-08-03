# Member Contribution Audit Patch — 2026-07-28

## Scope

Bounded audit follow-up for the `ireland_focus_tree` member-contribution tranche and its equipment-token repair. This handoff records one local lifecycle correction; it does not expand the decision system.

## Changed files and identifiers

- `common/decisions/slopx_ireland_decisions.txt`
  - `slopx_ireland_mission_meet_the_member_contribution_schedule`
- `docs/plans/ireland_focus_tree/subagent_handoffs/member_contribution_audit_patch_2026-07-28.md`

## Corrected behaviour

Before this patch, the decision's `available` block still required Northern Integration Capacity of 50 for the `complete` flag and 30 for the `partial` flag. Commit `cebbface` had already replaced the runtime's equivalent generic capacity checks with `slopx_ireland_member_contribution_full` and `slopx_ireland_member_contribution_partial`.

That left a contradictory terminal path: a class could satisfy its documented full or partial trigger, receive the corresponding mission flag, and still be unable to execute the result until the timer expired. A full flag also prevents the runtime from setting partial, so the timeout took the failure branch.

The mission now resolves directly from its class-derived `complete` or `partial` flag. The map objective remains mandatory through the class-specific triggers; the removed state and capacity checks were obsolete duplicates.

## Validation performed

- Compared the `cebbface` runtime diff with the decision terminal condition.
- Traced the counterexample: class-full trigger true below Capacity 50 previously set `complete`, failed `available`, prevented `partial`, then reached timeout failure.
- Confirmed the player-facing objective localisation says full and partial standards follow the selected payload.
- No HOI4 launch, by request. Engine execution of immediate mission completion remains a live-session check.

## Remaining risks

- Verify in a live session that a full and a partial result resolve immediately for each selected class, including capacity values below the old 50/30 thresholds.
- Confirm the event's immediate option evaluation still sees post-action resource values and that cancellation returns only the documented class-specific recoverable inputs.
