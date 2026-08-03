# Ireland localisation recheck — 2026-07-22

Feature slug: `ireland_focus_tree`

Scope: read-only source and localisation coverage check. HOI4 was not launched and the offline MCP transport was unavailable for a fresh engine parse.

## Results

- `events/slopx_ireland_flavour_events.txt` contains 236 unique flavour events, IDs 500–735.
- `localisation/english/slopx_ireland_l_english.yml` contains 944 flavour keys for those events: 236 titles, 236 descriptions, and 472 option labels.
- All 944 source-referenced flavour keys resolve to a localisation key; no missing keys or duplicate localisation keys were found in the Ireland flavour namespace.
- All 236 descriptions have distinct substantive bodies after removing the legacy wrapper, and all 472 option labels are distinct within the inspected namespace.
- The previous repeated bodies and labels, including the generic relief, development, witnessed-accord, and reconstruction strings, no longer occur in the Ireland flavour localisation.
- The localisation file retains a UTF-8 BOM (`EF BB BF`).

## Boundary

This recheck proves source coverage and distinct player-facing copy only. It does not prove Clausewitz localisation parsing, dynamic selector behavior, event firing, or option-effect behavior. Those remain part of the blocked live/reference validation gate in `docs/plans/ireland_focus_tree/source_of_truth_map.md`.
