# Ireland GUI engine-reference re-audit — 2026-08-03

Feature slug: `ireland_focus_tree`
Namespace: `ireland`
Scope: the three authored scripted GUI windows
HOI4 was not launched.

## MCP inspection

The current workspace `mod_ireland_total_overhaul_65a6b5f140a7` was inspected against the
offline `ireland_audit` scenario:

| window | elements | reported visible overlaps | source result |
| --- | ---: | ---: | --- |
| `ireland_conditions_panel_window` | 58 | 10 | complete |
| `ireland_northern_settlement_ledger_window` | 40 | 9 | complete |
| `ireland_concealed_evidence_ledger_window` | 57 | 29 | complete |

All three calls returned `GUI_INSPECTED` with `complete: true`. The aggregate
MCP graph reports 97 blocking diagnostics and a false aggregate validation, but
the returned inline diagnostic set consists of the bounded-collection notices
and the 18 expected `INDEX_SYMBOL_COLLISION` entries for the first eighteen
140-action names sharing the canonical 70 DDS textures. The Ireland source
contract deliberately keeps 140 named action sprites over 70 controlled-reuse
textures; the source-level icon audit confirms 140 unique sprite names and 70
unique runtime texture paths.

## Overlap disposition

The overlap counts are not accidental placement collisions:

- Conditions: three animation/fallback pairs, six mutually exclusive status
  medallion pairs, and review-button text over its button surface.
- Northern: two animation/fallback pairs, six mutually exclusive status
  medallion pairs, and review-button text over its button surface.
- Concealed Evidence: two animation/fallback pairs, six mutually exclusive
  status medallion pairs, the public-dossier title/state layers, and the three
  A-22/A-27/A-28 state rows; those rows are hidden or shown by the scripted-GUI
  visibility triggers and never display simultaneously in a valid state.

The matching scripted-GUI trigger table owns each state swap. The runtime icon
surface audit reports all ten required icon surfaces complete, and the
deterministic GUI render for the conditions window returned `GUI_RENDERED` at
1280×720 for normal, locked, warning, and long-text states. No GFX, DDS, GUI,
or gameplay change was required by this re-audit.

## Engine precedent and disposition

The separate vanilla comparison records repeated texture paths as normal
engine-facing registrations. This re-audit therefore classifies the aggregate
MCP result as a documented index/reference limitation plus intentional GUI
state layering, not a missing sprite, atlas bleed, invisible click blocker, or
unresolved runtime texture. The earlier controlled-reuse evidence remains at
`audits/ireland_gui_texture_reuse_engine_reference_2026-08-02.md`.

## Fresh deterministic render check

On 2026-08-03 all three authored windows were rendered against the offline
`ireland_audit` scenario at 1280×720 in `normal`, `locked`, `warning`, and
`long-text` states. The three calls returned `GUI_RENDERED`; the renderer’s
response was truncated only by the MCP wire-budget notice, with complete
artifacts retained by the linked MCP evidence. No runtime or source change was
required by this render pass.
