# P0 postwar conclusion architecture handoff

Date: 2026-08-14  
Owner: `hoi4_scripted_system_architect` subagent  
Parent: `/root`  
Status: implemented in the delegated scripted-system surfaces; no commit made.

## Files changed

- `common/script_constants/ireland_constants.txt`
- `common/scripted_triggers/ireland_triggers.txt`
- `common/scripted_effects/ireland_effects.txt`
- `docs/ireland_dynamic_effects.md`
- this handoff

No decisions, events, focus-tree, localisation, AI, asset, or thumbnail file
was edited.

## Helper map and caller contracts

| Identifier | Scope | Inputs | Outputs and side effects | Direct call sites |
| --- | --- | --- | --- | --- |
| `ireland_family_postwar_settlement_complete` | Country trigger | initialized Ireland plus shared settlement flag | true only after one family settlement action sets `ireland_family_postwar_settlement_complete`; no side effects | `ireland_archive_successful_route`; intended report-option guards |
| `ireland_has_active_route_review_critical_mission` | Country trigger | seven route-review critical mission active flags | true while any named route-review mission is active; no side effects | `ireland_postwar_foundation_ready` |
| `ireland_family_postwar_*_repair_recorded` | Country triggers | recovery-complete marker, active family, and that family's `ireland_postwar_*` repair record | surface-specific evaluator override for government/law/defence/economy/identity; no side effects or history deletion | `ireland_finalize_route_conclusion` blocked-surface checks |
| `ireland_postwar_foundation_ready` | Country trigger | date/war state, emergency review, full/partial mission records, UN-or-alternate record, and no active route-review mission | true only when every material foundation proof is present; no side effects | family settlement decision availability/AI blocks (already present in concurrent decision work) |
| `ireland_begin_conclusion_review` | Country effect | no parameters; settlement/recovery caller state | starts 180-day countdown using `constant:ireland.postwar_family_review_days`; after recovery completion sets `ireland_route_failure_recovered`; refuses to start while recovery is open | existing settlement/recovery action callers; existing route callers remain compatible |
| `ireland_open_family_conclusion_recovery` | Country effect | blocked or failed route result | sets `ireland_conclusion_recovery_open`, clears cycle-local recovery markers/timer, preserves every named blocked flag and durable failure history | `ireland_finalize_route_conclusion`; blocked/failed report options may safely call it idempotently |
| `ireland_dispatch_family_conclusion_event` | Country effect | one family flag | dispatches exactly one triggered-only event: democratic `.1`, communist/Congress `.2`, fascist/Blueshirt `.3`, oligarchic/producer-estate `.4`, restoration `.5` | `ireland_finalize_route_conclusion` |
| `ireland_archive_successful_route` | Country effect | review complete, full/partial result, family settlement complete, recovery closed | closes reactions/incidents, sets route cleanup/closed/archived, runs route cleanup/counter rebuild, requests spirit/profile sync | full/partial options in `ireland_country_conclusion.1-.5` (parent event caller) |

`ireland_finalize_route_conclusion` remains the evaluator. It now clears the
current result surface, classifies failed/blocked/partial/full, includes missing
family settlement in the named objectives block, clears the due timer, opens
recovery for blocked/failed results, and dispatches the matching family report.
It does not set `ireland_route_cleanup`, `ireland_route_closed`, or
`ireland_route_archived`.

The evaluator treats an existing `ireland_route_failure` as fatal only while
`ireland_route_failure_recovered` is absent. Recovery actions set
`ireland_family_conclusion_recovery_complete`, clear their own recovery-open
state, and call `ireland_begin_conclusion_review`; the helper then marks the
route as recovered without deleting `ireland_route_failure` history.

The evaluator consumes the five recovery-action repair records by surface:
democratic coalition repairs government/law, communist Congress repairs
government/defence, fascist directorate repairs defence, oligarchic estates
repair economy, and restoration Crown Council repairs government/identity.
Each override requires the matching family and the recovery-complete marker;
other surfaces are still evaluated normally and can reopen recovery.

## Constants and tuning table

Added to the existing global `ireland` category:

```text
postwar_family_settlement_days = 180
postwar_family_recovery_days = 120
postwar_family_factory_use = 1
postwar_family_review_days = 180
```

All four are consumed by concurrent family settlement/recovery decisions or the
conclusion countdown. Existing action-burden and AI score constants remain the
shared tuning source; no per-action magic numbers were added.

## Event dispatch and cleanup plan

- Dispatch is direct from the evaluator. There is no daily/world-country scan,
  generic monthly flavour candidate, or `fire_only_once` helper guard.
- The ordered family `else_if` chain ensures at most one report event in a
  malformed scope with multiple family flags.
- Full/partial report options must record their durable family report flag and
  then call `ireland_archive_successful_route`.
- Blocked/failed report options must not archive. They should retain the named
  blocked-surface flags and keep `ireland_conclusion_recovery_open` until the
  matching recovery action clears it.
- Archive is idempotent and guarded by unarchived route, completed review,
  full/partial result, shared settlement, and closed recovery state.
- No event target is needed: the report is fired in the current Ireland country
  scope and no scope pointer crosses an event chain.

## Alternate-order caller contract

`ireland_postwar_alternate_order_resolved` is intentionally a new explicit
country flag. The UN admission surface may set it only when
`ireland_un_admission_authority` is false and the world state makes the named
United Nations path invalid. A player or AI skipping a valid UN mission may not
set it. This is the only alternate-order branch accepted by
`ireland_postwar_foundation_ready`.

## Migration from the previous evaluator

1. Existing callers continue to call `ireland_finalize_route_conclusion` after
   the due review; no decision call-site rename is required.
2. The evaluator no longer performs terminal route cleanup or archival.
3. Parent event implementation must add namespace
   `ireland_country_conclusion` IDs `.1-.5`, with family/result-specific options.
4. Parent event success/partial options must call
   `ireland_archive_successful_route`; blocked/failed options must leave the
   route unarchived and preserve recovery state.
5. The conclusion decision should not be `fire_only_once` if failed review
   retries are to remain available; this was intentionally outside this
   subagent's ownership.

## Risks and unsupported analysis

- The read-only MCP impact inspection was run before source changes for helper
  `ireland_finalize_route_conclusion`. Artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/6fadc70d167060e3796657aa614c56abe6d23f53ae2d2e35c541d0920a03de15/7be81046f88b4f9994f1f4689e23f199bc640d6fc16830e772f17f07f5d2cfa3/event-impact-17a86c65a0fb.json`.
- MCP classified the large workspace impact as partial and reported zero
  parsed helpers for this scripted-effect subject; direct source inspection was
  therefore authoritative for the evaluator and caller contract.
- The event namespace/file and localisation are parent-owned. The five-event
  file appeared concurrently after the initial source inspection; its `.1-.5`
  IDs and archive call sites were then read-only checked against this contract.
  Localisation remains parent-owned.
- `ireland_postwar_alternate_order_resolved` has no existing caller in this
  delegated surface. Until the parent adds the explicit invalid-UN resolution
  branch, the foundation trigger correctly remains false when UN admission is
  unavailable.
- Existing runtime/focus systems may set or retain `ireland_route_failure` for
  other failures. The recovery marker is intentionally separate so durable
  failure history is not erased by family recovery.

## Parent integration closure

The parent added the five terminal report events and their archive-only success
options, removed one-shot behavior from the final review, and added the explicit
`ireland_action_record_an_alternate_postwar_order` caller. That action is visible
only when `ireland_un_admission_authority` is false, so it cannot bypass a valid
United Nations application.

## Validation

- Read all required offline wiki core pages and the vanilla script-constant,
  script-concept, effects, and triggers documentation before editing.
- Inspected vanilla `MTG_USA`/`BFTB_Turkey` event dispatch and event-target
  cleanup precedents.
- Ran targeted `rg` identifier audits for every new constant, trigger, effect,
  flag, and event ID; verified no duplicate existing caller or alternate-order
  flag existed before defining the documented contract.
- Ran `hoi4_event_inspect` read-only impact inspection before source edits.
- Ran a post-edit read-only event lint against
  `events/ireland_country_conclusion_events.txt`; artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/fd8edc03419dc0548171736bfbbbbbf31fdcfd263235189240ddfbaa24ae792a/8ce1ca0080a2bbe78093af775ae726a443821f143463a0b0b8bfd198cea8d7e5/event-lint-0850e2d2e45b.json`.
- Full game parser/live event rendering was not available in the delegated
  scripted-system surface. The MCP lint result was partial for the large
  workspace, so the parent should still run the final game/event validation
  pass after all localisation and decision changes are merged.
