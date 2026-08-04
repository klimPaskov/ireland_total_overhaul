# Ireland event engine-reference reaudit — 2026-07-29

Feature slug: `ireland_focus_tree`

This is an offline source and reference audit. Hearts of Iron IV was not
launched, and live event firing is excluded from the goal completion gate by
user direction.

## Runtime event inventory

The 2026-08-01 reconciliation of the current `events/ireland*.txt` files
finds 494 unique authored event IDs. One additional nested dispatch block in
the standard event source brings the raw block count to 495:

| source | unique event IDs | raw blocks |
|---|---:|---:|
| `events/ireland_events.txt` | 255 | 256 |
| `events/ireland_flavour_events.txt` | 236 | 236 |
| `events/ireland_member_contribution_events.txt` | 1 | 1 |
| `events/ireland_public_conclusion_events.txt` | 2 | 2 |

The 236-event consequential flavour floor remains exact. The additional
standard, member-contribution, and public-conclusion events do not change the
canonical 18 historical-chain, 18 political-crisis, 12 foreign-reaction, or
12 response-class family counts.

## Event inspector result

The local event inspector ran namespace-filtered lint passes for
`ireland_events` and `ireland_flavour_events`. Both returned
`EVENT_INSPECTED_PARTIAL`, no tool blocker, no skipped source, no blocking
diagnostic, and an empty issue array. A later aggregate namespace pass against
the current 494-ID workspace also returned `EVENT_INSPECTED_PARTIAL`
with zero blocking diagnostics. The reports remain partial because the
workspace is large and the event-only catalogue deferred helper projection.

Artifacts:

- standard events:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/fd0fee6e15fad7070f9da0ec0aa2fa6991d4600d0e3f031710b69885bc60e18c/cadf2327b0086e21168c4dc5d4d62019a77d3ba05e8fdcee4055ba3207f3adb2/event-lint-5ef211f1cf1f.json`;
- flavour events:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/44af126b0060c1673fde41a7a616be6da42ac989ff18b095cd9967828a7fa9e9/da035c45e7ecc5250efdcc68266b74a4a2bab445a9210c6da6fd3204df6444a6/event-lint-5ef211f1cf1f.json`.

## Helper-catalogue disposition

The inspector retained 724 Ireland `missing_helper` observations. They resolve
to 25 unique helper names, led by the settlement-stage, Provision, Readiness,
foreign-reaction, and neutrality-incident helpers. The report itself records
zero loaded helpers, so these observations describe the event-only catalogue,
not absent repository definitions.

Direct source lookup resolves all 25 reported names under
`common/scripted_effects/`. A wider independent sweep extracted every
indented `ireland_* = yes/no/{` custom call from the two principal event
files and the Ireland on-action file, then compared those 45 unique call names
with top-level definitions under `common/scripted_effects/` and
`common/scripted_triggers/`. Result: 45 call names, 363 available definitions,
zero unresolved call names.

The event helper-reference gate therefore passes at source level. The
inspector's aggregate partial result remains a documented catalogue limitation,
not an implementation defect and not a live-engine claim.

## Result

No event source change was required. The authored event inventory and custom
helper references are complete at the local static-reference boundary. Source
clearance for historical event images and the separate canonical/schema
decisions remain outside this audit.
