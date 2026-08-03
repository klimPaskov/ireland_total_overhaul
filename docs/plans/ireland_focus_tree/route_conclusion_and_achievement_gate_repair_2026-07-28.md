# Ireland route-conclusion and achievement-gate repair

Date: 2026-07-28
Feature: `ireland_focus_tree`
Namespace: `slopx`

## Scope

This tranche repairs the lifecycle boundary between a route capstone, the shared
route-conclusion review, and the achievement-history writers. It also corrects
three achievement gates identified by the completion audit:

- route-specific conclusion flags were being written at capstone completion,
  before the 180-day conclusion review resolved full, partial, or failed;
- the Constitution-restored achievement rejected the same permanent-emergency
  recovery history that should be allowed to recover into a valid settlement;
- the Atlantic achievement's four-member counter accepted unrelated policy
  milestones instead of four distinct sovereign diplomatic members.

This is an implementation repair, not a route redesign. Political conclusion
flags remain downstream of the shared review, and no route conclusion grants
free territory, cores, industry, equipment, units, fuel, shipping, supply,
administration, alignment, offices, or recognition.

## Route conclusion lifecycle

Each route capstone now records only its route-specific `*_capstone_complete`
or pending gate. The scripted trigger
`slopx_ireland_has_route_conclusion_capstone` reads those pending capstone
markers, so the 180-day review can still find a route that is ready for review.

`slopx_ireland_finalize_route_conclusion` remains the single resolution point.
It classifies the review as `slopx_ireland_route_conclusion_full` or
`slopx_ireland_route_conclusion_partial`, calls
`slopx_ireland_record_route_conclusion_flags`, then proceeds through the normal
Clann handling and cleanup. The new recorder maps only the completed route
capstone markers to route-specific `*_concluded` flags after the review has
resolved. Failure and blocked outcomes do not become political victories.

The achievement-history and runtime trackers require the shared full-result
flag for conclusion achievements. A partial settlement can retain its
route-specific concluded state for ordinary route cleanup and presentation,
but it cannot satisfy a full political-victory achievement.

## Achievement repairs

### A-20: four durable leverage ledgers

The sponsor-dependence condition now checks the durable high-water variables
for British, Vatican, American, and German leverage. It no longer relies on
the current aggregate `slopx_ireland_achievement_sponsor_dependence`, which is
overwritten as live leverage changes.

### A-21: recoverable emergency settlement

The contradictory negative condition for
`slopx_ireland_achievement_permanent_emergency_failure` was removed. The
achievement instead requires the live emergency-overreach flag, emergency
powers crisis flag, and emergency-law failure stage to be cleared. The
historical failure flags remain recorded for other history-sensitive outcomes.

### A-26: sovereign Atlantic members

The four member records now come from four named live diplomatic channels:
British, American, German, and Vatican/Italian. Each channel uses its existing
partner-validity trigger, including `is_subject = no`, and each record remains
one-time through its existing `*_member_[1-4]_recorded` flag. A neutral-state
forum can support charter drafting but cannot count as a sovereign member.
Unrelated charter-ratification, liberated-authority, contribution, and
guarantee-review milestones no longer increment the member count.

## Touched implementation surfaces

- `common/national_focus/slopx_ireland_focus_tree.txt`
- `common/scripted_triggers/slopx_ireland_triggers.txt`
- `common/scripted_effects/slopx_ireland_effects.txt`
- `common/scripted_effects/slopx_ireland_runtime.txt`
- `common/scripted_effects/slopx_ireland_achievement_history.txt`
- `common/achievements/slopx_ireland_achievements.txt`
- `docs/plans/ireland_focus_tree/source_of_truth_map.md`
- `docs/plans/ireland_focus_tree/project_status.md`

## Evidence and limits

The touched Clausewitz files have balanced braces and the focused diff has no
whitespace errors. Static searches confirm that route capstone source no longer
writes route-specific `*_concluded` flags directly, that A-20 uses the four
durable maxima, and that A-26's member records are bound to the four named
channels.

HOI4 was not launched, in accordance with the user's instruction. Live parser,
fresh-save, achievement-display, route-review, diplomatic-partner,
subject-status, failure/recovery, and cleanup scenarios therefore remain
not-run. Source-clearance decisions and the canonical Radical/Underground
two-slot mission-inventory contradiction remain separate blockers recorded in
the source-of-truth ledger.
