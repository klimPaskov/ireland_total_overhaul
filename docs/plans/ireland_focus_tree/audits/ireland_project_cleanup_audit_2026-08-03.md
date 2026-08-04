# Ireland project cleanup audit — 2026-08-03

## Scope

This pass covered the Ireland-owned runtime and source surfaces for
`ireland_focus_tree` / `ireland` after the final non-live implementation audit.
It did not launch Hearts of Iron IV or perform live-save testing; the project
owner will perform that test independently.

The repository was already dirty outside this package. The cleanup therefore
preserved unrelated staging, archive, skill, and research changes and touched
only the Ireland scripted cleanup contract and this audit record.

## Repair applied

`common/scripted_effects/ireland_effects.txt` contained eleven
`clear_global_event_target` effects for Ireland names that had no matching
`save_event_target_as`, `save_global_event_target_as`, `event_target:`, or
`has_event_target` use anywhere in `common/`, `events/`, or `interface/`.
Those calls were dead cleanup residue rather than live scope ownership. They
were removed. Variable, flag, mission-result, foreign-reaction, integration,
and route cleanup remains in place.

## Cross-reference results

- All 1,227 Ireland `GFX_` references resolve to unique interface sprite
  definitions.
- All 1,659 Ireland interface texture references resolve to files under the
  runtime `gfx/` tree. Active runtime source contains no `assets/` texture
  path; the two remaining `assets/ireland_focus_tree` mentions are comments
  documenting the staging boundary.
- The ten runtime icon surfaces contain their expected counts and dimensions:
  216 goals, 51 laws, 63 route spirits, 13 categories, 70 action textures,
  54 mission textures, 45 ledger textures, 27 overlays, 16 emblems, and 54
  flags. The readback found no visible chroma-key pixels or transparent-surface
  edge contact in the strict icon surfaces.
- The two Ireland English localisation files are UTF-8 with BOM, contain 4,094
  unique keys, and have no duplicate keys. All eleven GUI scripted-localisation
  calls resolve to defined-text contracts.
- The source manifest contains 169 rows: 166 complete and three intentionally
  blocked. All complete source and final DDS paths resolve; the 57 complete
  portrait rows source original files directly from the flat `docs/portraits/`
  root and none is a 156×210 derivative.
- The remaining blocked source rows are P-26 Patrick Cogan, P-45 Mick
  Fitzpatrick, and P-55 Liam D. Walsh. No fallback portrait or unapproved
  substitute was introduced.

## Offline engine checks

- Ireland focus inspection: 216 nodes, 197 authored connectors, zero
  Ireland-local layout diagnostics.
- Ireland map inspection: state and map validation passed for the checked
  Ireland/Northern Ireland state references.
- Ireland event inspection: zero blocking diagnostics; workspace-wide helper
  projection remains the MCP's documented partial-analysis limitation.
- GUI inspection: the Ireland graph is connected and has no missing source
  files. The inspector's repeated action-texture collision diagnostic is the
  documented intentional reuse of 70 action DDS files by 140 named action
  sprites, not duplicate sprite definitions; all 1,227 sprite names remain
  unique under the source-level audit.

## Disposition

The Ireland-owned code and asset-reference cleanup is complete for the
non-live scope. The overall Ireland overhaul remains externally blocked only
by the three exact historical portrait sources listed above. Live HOI4 testing
is intentionally left to the project owner and is not represented as passed
here.
