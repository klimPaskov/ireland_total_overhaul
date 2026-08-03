# Ireland map reference re-audit — 2026-07-29

## Scope

This audit records the offline `hoi4-agent-tools` map inspection for the Ireland
focus-tree map references. It is a source/reference check only; live HOI4
testing is intentionally excluded from the completion gate.

## Inspected references

The inspection covered the Ireland-related states used by the Northern Ireland,
occupation, integration, and regional-external systems:

- State `113` — Belfast / Northern Ireland reference.
- State `119` — the state used by the Northern control, settlement, and final
  core-review helpers.
- State `135` — the adjacent regional reference used by the Ireland map
  objective set.

The map inspection reported no unknown or missing province IDs for the selected
states.

## Result

The offline map validation returned `MAP_INSPECTED` with no blocking
diagnostics. All five map checks passed:

1. map files and definitions
2. map bitmap geometry
3. map state and region membership
4. map networks and adjacencies
5. map positions and locators

The inspected map revision reported 5,632×2,048 geometry, 13,414 province
definitions, 1,081 states, 304 regions, and 534 ports. The inspection covered
3 states and returned an empty unknown/missing-province set.

## Evidence

The MCP artifact was:

`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/52518c08163ce44fbc5b4f2c118377877079468e2c85c5914df690e04a18062f/b460e5aa6607f0a806d1e387659a469524f94da2fa4e8d4e95b3b728e583fcc6/map-inspect.d880d0ee0b0f40c8.json`

This result supports the named map-objective and Northern-state references at
the static map-data layer. It does not replace source-level checks for control,
occupation, settlement, integration, and core-review gates, which remain
separate in the Ireland runtime scripts.

## Remaining boundary

The canonical Radical and Underground Transition mission-cap contradiction and
the source-clearance/engine-reference blockers remain open. No gameplay or
runtime asset changes were made by this audit.
