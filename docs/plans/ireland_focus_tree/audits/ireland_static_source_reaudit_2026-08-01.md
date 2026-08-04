# Ireland static source re-audit

Date: 2026-08-01

Status: current non-live source evidence. HOI4 was not launched and no live
save, in-game scenario, or fresh-save playthrough was used.

## Event inventory

The four Ireland event sources contain 494 unique event identifiers:

- `events/ireland_flavour_events.txt`: 236 flavour events.
- `events/ireland_events.txt`: 255 core event definitions.
- `events/ireland_member_contribution_events.txt`: 1 event.
- `events/ireland_public_conclusion_events.txt`: 2 events.

The core namespace therefore contains 258 numeric events, with no duplicate
numeric identifiers, and the flavour namespace contains the exact 236-event
floor. The allocation comments in the core source retain the 18 historical
chains, 18 political-crisis families, nine material/neutrality families, eight
Northern families, 12 foreign-reaction families, and four postwar families.

The bounded offline `hoi4.event_inspect` namespace lint returned `status: ok`
with zero blocking diagnostics. Its workspace-wide helper/lifecycle analysis
was deferred by the MCP result budget, so this is source-reference evidence,
not a global parser or gameplay claim.

## Decisions and missions

Static parsing of `common/decisions/ireland_decisions.txt` finds exactly
13 decision categories, 140 unique action definitions, and 54 unique mission
definitions. Every mission block has the native `icon`, `activation`,
`available`, `days_mission_timeout`, `cancel_trigger`, `cancel_effect`,
`timeout_effect`, `complete_effect`, and `ai_will_do` fields.

All 54 mission blocks expose a named map-objective gate and a native deadline.
The 52 ordinary inline mission blocks contain their own full/partial/failure/
escalation result paths. The two mode-multiplexed missions deliberately route
those paths through the shared helpers below, so their block-local token count
is not a missing-outcome finding:

- `ireland_mission_conduct_a_free_general_election` uses the election
  cancellation, timeout, and completion helpers for the ordinary and
  by-election modes.
- `ireland_mission_keep_essential_services_running` uses the service
  obligations helpers for the ordinary and parish-audit modes.

All six helpers provide result recording, the appropriate full/partial/failure
or cancellation record, family cleanup, and route-cleanup handling. The
mission-capacity tranche is documented in
`../mission_capacity_transition_and_activation_refresh_tranche_2026-08-01.md`:
the runtime cap is 8 in ordinary peace, 10 during war or emergency, and 12
only during emergency plus Northern occupation, with a 30-day stable return to
the ordinary cap.

## GUI and GFX registration

The three intended windows were inspected with the Ireland workspace and the
`ireland_audit` offline scenario:

| Window | Inspected elements | MCP status |
| --- | ---: | --- |
| Conditions panel | 58 | `GUI_INSPECTED` |
| Northern settlement ledger | 40 | `GUI_INSPECTED` |
| Concealed-evidence ledger | 36 | `GUI_INSPECTED` |

The GUI inspector reports the known global/offline limitations: 97 combined
source diagnostics for each Ireland surface, including intentional animation /
fallback and status-overlay geometry, unsupported renderer fields, and the
controlled action-texture reuse. The current Ireland GFX parse finds 369 unique
sprite names in `interface/ireland_icons.gfx`, with no duplicate sprite
names. The 140 decision sprite names intentionally consume 70 unique DDS
texture paths; the MCP texture-symbol collision diagnostic is the indexer's
representation of that reuse, not a duplicate sprite registration or a visual
bleed defect.

All 857 unique physical `texturefile` paths in the interface GFX audit resolve
to files under the mod's runtime `gfx/` tree (1,607 references including
intentional reuse). No missing Ireland-scoped portrait
sprite token or portrait texture was found. Preserved leader source packages
remain under `docs/portraits`.

## Achievements and country identity

The achievement source contains 32 definitions with `unique_id =
ireland_total_overhaul_ireland_focus_tree`. Seven are statically hidden: A-22, A-27, A-28,
and the four postwar/advanced hidden entries A-29 through A-32. The current
runtime package contains 32 complete three-state DDS triplets (96 files), and
all 32 achievement name/description pairs are present in the English
localisation. This preserves the approved A2 static-hidden decision without
introducing unsupported dynamic achievement visibility syntax.

The cosmetic-country source contains 18 Ireland route identities. Every
identity has matching `_ADJ` and `_DEF` localisation entries.

## Disposition

No gameplay or asset source was changed by this audit. The current manifest
now records 132 complete rows and 37 remaining source-clearance blockers (15
portraits, 7 symbols, and 15 event/news packages, including rights-gated art).
S-06 and S-08 were promoted as exact C3 poster alternates by the independent
clearance pass; S-15, S-20, S-23, S-26 and S-33 were subsequently promoted under the
project owner's explicit conditional approval; S-12 remains blocked after the
candidate was rejected as semantically wrong. The remaining blockers are any unresolved
canonical audit item recorded in the project status authority, and the
separate non-live completion checks.
Live HOI4 testing remains excluded by explicit user direction.
