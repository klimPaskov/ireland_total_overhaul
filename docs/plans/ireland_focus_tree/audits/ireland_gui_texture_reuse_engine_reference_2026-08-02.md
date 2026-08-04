# Ireland GUI texture-reuse engine-reference audit — 2026-08-02

## Purpose

This audit records the fresh offline MCP result for the Ireland GUI source and
the vanilla interface precedent for repeated `texturefile` paths. It resolves
whether the `INDEX_SYMBOL_COLLISION` messages reported for Ireland decision
action sprites represent duplicate sprite definitions or intentional named
aliases over a controlled texture budget.

HOI4 was not launched. This is a local source and engine-reference check only;
the user explicitly excluded live in-game testing and scenario playthroughs
from the completion gate.

## Ireland source contract

`interface/ireland_icons.gfx:219-361` defines 140 unique decision-action
sprite names backed by 70 unique action DDS textures. The source comment at
the start of that block records the contract: named action sprites remain
distinct for the 140 actions while the 70-texture allocation is intentionally
reused. A direct source sweep found:

- 140 action sprite names;
- 140 unique action sprite names (no duplicate sprite identifiers);
- 70 unique action `texturefile` paths;
- every referenced action texture path resolves to a final DDS beneath the
  standard runtime `gfx/` tree;
- the 140 decision definitions retain their own named `icon` references.

The aliases are required by the canonical 140-action surface and do not create
atlas crops, neighboring-icon bleed, or a second active definition of the same
sprite name. Removing the aliases would hide action-specific names and break
the decision-to-icon coverage contract.

## Fresh MCP result

The 2026-08-02 `hoi4_gui_inspect` call for workspace
`mod_ireland_total_overhaul_65a6b5f140a7` returned `GUI_INSPECTED` with `complete: true`:

| graph inventory | result |
|---|---:|
| nodes | 45,018 |
| edges | 101,982 |
| GUI elements | 23,370 |
| sprites | 17,457 |
| fonts | 183 |
| scripted GUIs | 20 |

The aggregate graph is connected and the validator returned `passed: true`.
The diagnostic list still labels repeated texture paths as
`INDEX_SYMBOL_COLLISION`, including the 140-action/70-texture aliases. That
diagnostic is an index-model warning about repeated texture paths, not a
duplicate sprite identifier or a missing runtime texture.

## Vanilla precedent

A read-only comparison of the installed vanilla `interface/**/*.gfx` files
found repeated texture paths throughout the game interface:

| corpus | `.gfx` files | texture entries | repeated paths |
|---|---:|---:|---:|
| vanilla HOI4 | 162 | 26,694 | 4,312 |
| Ireland Total Overhaul interface | 9 | 1,625 | 314 |

The most frequently repeated vanilla path is the shared goal shine overlay,
which is registered thousands of times. Repeated title-bar, button, status,
spirit, goal, and icon texture paths are also normal vanilla registrations.
Therefore the Ireland action aliases follow the established engine-facing
pattern: unique sprite names may intentionally point to a shared texture.

## Disposition

No GFX definitions were removed or collapsed. The 140 named action sprites,
70 final action textures, decision registrations, and runtime paths remain
unchanged. The fresh GUI inspection, the direct source sweep, the runtime
icon-surface audit, and the vanilla precedent together classify the Ireland
action collision messages as intentional controlled reuse. There is no
unresolved Ireland-local GUI texture or sprite-identity defect in this class.

The separate offline limitations—font metrics, static-fallback inference, and
unsupported render fields—remain documented in
`ireland_gui_surface_reaudit_2026-07-29.md`. They do not justify changing the
runtime aliases or introducing fallback art.
