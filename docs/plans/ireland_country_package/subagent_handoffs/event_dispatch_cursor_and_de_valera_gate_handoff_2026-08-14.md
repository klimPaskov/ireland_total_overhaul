# Ordinary Event Cursor and de Valera Gate Handoff — 2026-08-14

## Result

The two event blockers recorded by the read-only audit at revision
`8fe5c6248a3328968bc98d97557312dda63931ae` are repaired in the current
worktree.

- The ordinary monthly programme resumes from a durable next-entry cursor
  across all 457 scheduled launches.
- An ineligible entry advances to the next catalogue position during the same
  monthly scan, so an early closed or out-of-window entry cannot starve later
  reports.
- A successful launch advances the cursor, sets the existing dispatch-admission
  flag, and stops that monthly scan.
- The existing one-month cooldown still leaves the next monthly pulse empty,
  preserving the maximum six ordinary reports per year.
- `ireland_flavour_events.500` now requires the historical de Valera profile,
  Éamon de Valera as the active ruling country leader, and a valid occupied
  Taoiseach and cabinet registry without a government vacancy.

No fallback, route redesign, event replay, daily dispatcher, or change to the
foreign-reaction broker was introduced.

## Files changed

- `common/scripted_effects/ireland_runtime.txt`
- `common/script_constants/ireland_constants.txt`
- `common/on_actions/ireland_on_actions.txt`
- `events/ireland_flavour_events.txt`
- `docs/ireland_event_programme.md`
- `docs/ireland_dynamic_effects.md`
- `docs/ireland_systems.md`
- `docs/specs/ireland_country_package/systems_and_lifecycles.md`
- `docs/plans/ireland_focus_tree/source_of_truth_map.md`
- this handoff

The pre-existing `thumbnail.png` worktree modification was not touched.

## Durable cursor contract

`ireland_dispatch_event_programme` treats
`ireland_event_dispatch_cursor` as the next ordered position to consider.
Every scheduled launch has two paired blocks:

1. The launch block admits its position when the durable cursor is at that
   position or at an unused lower gap. If the event-specific trigger is valid,
   it writes the following position before firing the event and sets
   `ireland_event_dispatch_taken`.
2. The immediately following advance block has only the same cursor admission
   and the no-dispatch guard. If the launch was ineligible, it writes the same
   following position and lets the scan continue. If the launch succeeded,
   `ireland_event_dispatch_taken` prevents this and every later slot from
   running in the same pulse.

The sequence contains 221 `ireland_events` launches and 236
`ireland_flavour_events` launches. The internal chain is continuous across all
456 edges. It intentionally crosses the separately paced 400–430 foreign-event
range through `constant:ireland.event_dispatch_foreign_skip_cursor`, then
continues at `ireland_events.434`. The last ordinary entry advances from 735 to
100, allowing a later monthly scan to reconsider unseen events whose world-state
conditions have become valid.

Out-of-range cursor values still recover to
`constant:ireland.event_dispatch_first`. Unused in-range gaps are accepted by
the next real catalogue position. This makes recovery deterministic without
restarting every valid monthly pulse at entry 100.

The recurring caller remains only `on_monthly_IRE`. The existing
`constant:ireland.event_dispatch_cooldown_months = 1` is written only after a
successful dispatch and decremented on the next monthly pulse. No event launch
was added to `on_daily_IRE`.

## `ireland_flavour_events.500` eligibility

The source trigger and the runtime dispatcher gate now agree on all of the
following:

- `ireland_profile_historical_de_valera`
- `has_country_leader` with `ruling_only = yes` and
  `character = IRE_Éamon_de_valera`
- `ireland_office_taoiseach_occupied = constant:ireland.one`
- `ireland_office_cabinet_minister_occupied = constant:ireland.one`
- no `ireland_office_taoiseach_vacant`
- no `ireland_office_cabinet_minister_vacant`
- no `ireland_government_vacancy`
- the existing 1937–1950 date window, positive social consent, route-open
  state, no close flag, and no seen flag

The monthly hook synchronises the office registry before it invokes the
dispatcher. If de Valera has been displaced when cursor position 500 is
examined, the event does not fire, does not set its seen flag, and does not
consume the monthly dispatch admission. The cursor advances to 501 and later
eligible reports remain reachable. A lawful restoration can make event 500
eligible when the ordered catalogue returns to that position in a later
rotation.

The existing localisation is specifically about de Valera's cabinet authority.
No localisation text or key was changed because the exact trigger now guarantees
that context. The relevant unchanged keys are:

- `ireland_flavour_events.f01_cabinet_routine.title`
- `ireland_flavour_events.f01_cabinet_routine.desc`
- `ireland_flavour_events.f01_cabinet_routine.constitutional_stewardship`
- `ireland_flavour_events.f01_cabinet_routine.constitutional_stewardship.effects`
- `ireland_flavour_events.f01_cabinet_routine.county_compromise`
- `ireland_flavour_events.f01_cabinet_routine.county_compromise.effects`

## Tuning and no-replay guarantees

The dispatcher timing remains centralised in
`common/script_constants/ireland_constants.txt`. The same table now also names
the foreign-range skip cursor. Event 500's option bases and profile factors are
file-scoped constants at the top of `events/ireland_flavour_events.txt`.

Because the historical profile is an event prerequisite, the effective option
weights remain 110 for constitutional stewardship and 22.5 for county
compromise. This is approximately 83.02% versus 16.98%, the same relative
historical weighting as before the gate repair.

All 457 existing seen checks, `fire_only_once` declarations, family close flags,
and event consequences remain unchanged. The cursor advances before a launch,
so it does not redispatch the same slot while the event is open. The catalogue
wrap does not bypass seen or close guards.

The `hoi4-mtth` skill was reviewed. No MTTH entry was added because this patch
does not change a timing distribution, and four local option-weight constants
are clearer than introducing a cross-file MTTH table for one triggered event.

## Meaningful validation

### Bounded catalogue audit

A direct parser over `ireland_dispatch_event_programme` found:

- 457 launches, comprising 221 main and 236 flavour events
- 457 unique event identifiers
- 914 cursor guards, exactly one launch guard and one paired advance guard per
  scheduled event
- zero legacy equality-only cursor guards
- zero launch/advance current-position or next-position mismatches
- zero discontinuities across the 456 internal edges
- first edge `ireland_events.100`: first-cursor to 101
- event 500 edge: 500 to 501
- final edge `ireland_flavour_events.735`: 735 to 100

Targeted source comparison also found every required de Valera/profile/office
condition in both the event trigger and runtime gate, with no plausible-route or
absurd-route alternative remaining in either event-500 block.

### Event tools

Focused event lint and reachability render used current event revision
`680531e6490e17234440c8ae9f4ef55ab6e7c34a68759b8e222835de741ca124`
and graph hash
`68877e073be889bca4d8b35d809ac05be654d91e380532593bd30d4a75e6f116`.
Both calls returned `status = ok` and no blocker. They report partial analysis
because the large workspace defers workspace-wide helper projections and
lifecycle passes. The bounded source audit above is therefore the authoritative
proof of the unrolled cursor chain.

- Lint artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/9926e9fb2977b395a15980a1b51cac984c8fc3441c4af1b483460937a6b375f9/de77eee6766f1033a5b0e67ff241dc2ef9f81dda18c77765b56554feb7468ffc/event-lint-680531e6490e.json`
- Focused trace artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/937b387e54d663320ca679b101b828d41e752576acef46260c0a9248d2fadb08/20e7d14945b5e279303f1d175e27dc4eeb50f74bb695b7806f2c32f486418997/event-trace-680531e6490e.json`
- Reachability manifest:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/865bd327fd66648b277919311fd18ddcc2e11b143556bfb6490a4d8e5b27fb8b/19b3cff4af7993e3c5389d521af0cfaec308f78c0e1d57432abe6b99c2b0f937/event-reachability-680531e6490e-manifest.json`
- Reachability data:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d520ef68107c579c39af9d06ca0c8d2f7b9baa88e0c15c85aede6a0e7de36907/f6557d590c97790943a5b377360d784885565cd1ce89afc72a9b3b5da9b668da/event-reachability-680531e6490e.json`
- Reachability SVG:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d3a632b892a4e7ae0cfc59c77c649eb59f18bbd31241766cc70768c3e325ad1b/f785a2109a149e1e5d7a3e08a4bd598a9a65fbfa761751aff8a1a72724e83c2d/event-reachability-680531e6490e.svg`

The weighted-option inspector classified event 500's two-option
`event_option_ai_chance` pool as complete and exactly supported, with all four
file-scoped constants resolved:

- Probability inspection artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/206a1b36c6c2e4389a5dfd15245384365c36d0973513dd03caf285e7eb250dbd/d3458c033612235f20f753a278c131bb5bbeb4e5d69569d19cf6a17511798269/probability-inspect-af9c732a8280.json`

The cached pre-edit graph revision was unavailable to the comparison endpoint,
and its earlier scan artifact used an unsupported comparison schema. No
before/after event-graph comparison claim is made.

## Documentation disposition and remaining scope

`docs/plans/ireland_country_package/final_completion_report_2026-08-14.md`
remains an immutable read-only audit of revision
`8fe5c6248a3328968bc98d97557312dda63931ae`. Its event blocker is superseded for
the current worktree by this implementation handoff, not rewritten inside that
historical report.

The parent still owns review, any successor completion disposition, integration
with concurrent changes, and the requested commit. Portrait clearance,
exceptional-route depth, broader documentation reconciliation, and the package
acceptance-scenario matrix were outside this bounded event patch and remain as
recorded by the final audit.

## Simplifications, omissions, and blockers

- No event-system simplification or fallback was used.
- No requested event route, localisation key, cooldown, replay guard, or
  scheduled launch was omitted.
- Focus routes, decisions, assets, and broader country-package blockers were not
  redesigned in this bounded patch.
- The event tools' workspace-wide analysis remained partial as described above.
  The focused calls returned no blocker, and the complete 457-slot continuity
  proof was performed directly against the dispatcher source.
