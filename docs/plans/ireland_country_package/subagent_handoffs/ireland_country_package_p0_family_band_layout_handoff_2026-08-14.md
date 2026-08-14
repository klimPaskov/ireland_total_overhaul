# P0 family-band layout handoff — 2026-08-14

## Status

Superseded by `ireland_country_package_family_lane_reflow_completion_2026-08-14.md`. This file records the rejected gateway-only experiment and its baseline evidence; it is not the final layout contract.

No gameplay source change was retained from this rejected attempt. `common/national_focus/ireland_focus_tree.txt` was restored byte-for-byte after the proposed band pass produced a worse layout. No localisation, icon, reward, ID, AI, decision, event, effect, asset, spec, or thumbnail files were changed by that attempt.

## Clean baseline evidence

`hoi4.focus_inspect` on `ireland_focus_tree` reports 218 focuses and 226 connectors:

- crossing count: 0
- node-intersection count: 0
- long-connector count: 0
- duplicate coordinates: 0
- same-row spacing: minimum 2, required 2, too-close pairs 0
- maximum vertical span: 2
- one pre-existing `FOCUS_LAYOUT_LINEAR_DETOUR`: `ireland_clerical_failure_bridge` (-10,3) -> `ireland_clerical_guardianship` (-8,4)

Baseline artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0c1bfc2be06cd2272bbe9441bcf71240b15d0ebdaf870d39ef6c1ba22673aa8a/2fcea3a82c7f84222d21203d39950141c328eb43798a5cc064cd5580b97bfebf/focus-inspect.c382493ac46546f9.json`

The only other inspector warning is the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference.

## Requested band plan (not applied)

The accepted centered band would use these visible gateway coordinates and visible prerequisites:

| order | focus | target | visible prerequisite |
| --- | --- | --- | --- |
| democratic | `ireland_republican_government` | (-16,3) | `ireland_public_order_review` |
| Congress | `ireland_congress_reform_bridge` | (-14,3) | `ireland_election_timetable` |
| producer-estate | `ireland_vocational_constitution` | (-12,3) | `ireland_church_labour_consultation` |
| Blueshirt | `ireland_oduffy_network_revival` | (-10,4) | `ireland_constitutional_draft` |
| restoration | `ireland_high_king_evidence_gate` | (-8,4) | `ireland_cultural_evidence_ledger` |

The clerical failure/guardianship pair should be placed on one x-column (for example (-6,3) and (-6,4)) in the final authored reflow. The five existing shortcut targets remain exactly three and were not edited.

## Exact blocker from bounded trial

Applying only the gateway moves and visible prerequisite relocation, without reflowing their direct descendants, left the source parser-valid but not layout-clean. The inspector measured:

- 18 connector crossings
- 11 node intersections
- 4 long connectors
- 1 same-row spacing pair was briefly created before the constitutional-draft move; moving it removed the duplicate but left 18 crossings and 11 intersections
- maximum vertical span 7

The crossings were concentrated in the unavoidable child corridors of the moved gateways: constitutional draft -> election mandate/replacement charter crossing the Congress -> organise corridor and democratic profile children; church/labour -> vocational constitution crossing election timetable -> constitutional draft; Congress vanguard capstone crossing the vocational capstone; and the moved O'Duffy gateway reaching its original y11 programme children through the vocational corridor. This means a clean implementation requires reflowing each affected descendant chain (and the public-family programme clusters) as one authored coordinate pass, rather than moving only the five gateway nodes.

## Next bounded implementation

Preserve the clean baseline, then author one coordinated coordinate-only pass that:

1. applies the five target gateway coordinates/prerequisites above;
2. moves every direct descendant of the relocated vocational and O'Duffy gateways to y+1/y+2 corridors, retaining same-row spacing;
3. routes the democratic and Congress election corridors around the band without changing their prerequisite semantics;
4. attaches and centers the detached public-family programme clusters on their selected family capstones, with only the required prerequisite/available relocation;
5. aligns clerical failure -> guardianship vertically; and
6. reruns `hoi4.focus_inspect` and `hoi4.focus_render` until crossings, intersections, long connectors, spacing failures, duplicate coordinates, and linear-detour diagnostics are all zero.

No game-runtime validation was run because no source change was retained and this handoff is coordinate-only.
