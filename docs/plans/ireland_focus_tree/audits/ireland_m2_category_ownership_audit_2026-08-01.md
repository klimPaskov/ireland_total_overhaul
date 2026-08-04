# Ireland M2 category-ownership audit

Date: 2026-08-01
Feature slug: `ireland_focus_tree`
Scope: static source ownership and count audit for the approved M2 decision.

## Result

The current decision source contains exactly 13 categories, 140 action
definitions, and 54 mission definitions. Mission identifiers are unique and
the source has balanced braces. The two replacement mission declarations are
physically children of `ireland_radical_underground`; they are not merely
activated by Radical/Underground actions.

| category | missions | actions | total child definitions |
|---|---:|---:|---:|
| Settlement & Government | 3 | 10 | 13 |
| Elections | 2 | 10 | 12 |
| Organised Society | 2 | 10 | 12 |
| Cultural & Archival | 3 | 10 | 13 |
| Radical & Underground | 2 | 10 | 12 |
| National Provision | 10 | 16 | 26 |
| Readiness | 8 | 14 | 22 |
| Neutrality & Incidents | 4 | 10 | 14 |
| Foreign | 4 | 10 | 14 |
| Northern | 4 | 10 | 14 |
| Occupation & Integration | 4 | 10 | 14 |
| Regional & External | 3 | 10 | 13 |
| Postwar | 5 | 10 | 15 |
| **Total** | **54** | **140** | **194** |

## M2 ownership checks

- `ireland_mission_conduct_a_free_general_election` remains in
  `ireland_elections` and carries the approved general-election and
  by-election modes.
- `ireland_mission_keep_essential_services_running` remains in
  `ireland_organised_society` and carries the approved normal-service
  and parish-audit modes.
- `ireland_mission_consolidate_the_movement_network` is a child of
  `ireland_radical_underground` and uses ordinal 006.
- `ireland_mission_secure_constituent_authority` is a child of
  `ireland_radical_underground` and uses ordinal 009.
- No active mission target references the retired standalone
  `protect_a_by_election` or `audit_parish_service_contracts` identifiers.
- The count-preserving merge therefore leaves the decision surface at 140
  actions and 54 missions while giving Radical/Underground both approved
  mission families.

This is a source-structure audit only. It does not claim live HOI4 launch or
in-game testing; those are explicitly outside the completion gate.
