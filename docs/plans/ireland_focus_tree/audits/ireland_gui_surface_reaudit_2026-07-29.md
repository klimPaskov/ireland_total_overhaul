# Ireland GUI surface reaudit — 2026-07-29

## Current completion-audit reconciliation

The fresh 2026-07-29 completion audit supersedes the earlier zero-element and
missing-window observation recorded below. The three exact windows now inspect
as 58, 40, and 36 elements respectively: National Conditions Panel, Northern
Settlement Ledger, and Concealed Evidence Ledger. A follow-up inspection
classified every predicted overlap by element name. All 28 observations are
intentional shared slots governed by mutually exclusive scripted visibility:
animation/static-fallback pairs, four-state status medallions, and text placed
inside its clickable review button. No observation identifies two
simultaneously visible player-facing content rows or labels. Local validation
still reports `false` because the inspector treats these state layers, the
canonical 140-sprite/70-texture reuse contract, unavailable offline font
metrics, and unsupported render fields as source-graph diagnostics. No live
testing is required or claimed.

## Scope

This is a current-worktree, offline audit of the exact three canonical Ireland GUI
families. Hearts of Iron IV was not launched. The runtime surfaces remain under
`interface/` and `gfx/`; `assets/ireland_focus_tree/generated/gui/` is the
source, processed, manifest, contact-sheet, and static-fallback package only.

## Exact family inventory

| family | authored window | decision-category registration | runtime background |
|---|---|---|---|
| National Conditions Panel | `ireland_conditions_panel_window` | `ireland_conditions_panel_scripted_gui` on `ireland_settlement_government` | `gfx/interface/ireland/gui/conditions/background.dds` |
| Northern Settlement Ledger | `ireland_northern_settlement_ledger_window` | `ireland_northern_settlement_ledger_scripted_gui` on `ireland_northern` | `gfx/interface/ireland/gui/northern/background.dds` |
| Concealed Evidence Ledger | `ireland_concealed_evidence_ledger_window` | `ireland_concealed_evidence_ledger_scripted_gui` on `ireland_cultural_archival` | `gfx/interface/ireland/gui/evidence/background.dds` |

The current source contains exactly three `.gui` files, three top-level
`containerWindowType` windows, three scripted-GUI registrations, and three
unique decision-category bindings. All windows are authored at `920x704`.

## Interaction and state wiring

The current source-graph inspection resolves 58 National Conditions Panel
elements, 40 Northern Settlement Ledger elements, and 36 Concealed Evidence
Ledger elements. Their scripted-GUI contracts contain:

- 32 click effects;
- 32 matching `_click_enabled` triggers;
- 54 visibility triggers;
- seven scripted-localisation projections used directly by the layouts.

Every click-effect base name, click-enabled base name, and visibility-trigger
base name resolves to an element in one of the three layouts. Every click effect
has a matching enable trigger. All 74 direct player-facing localisation
references resolve, and all seven dynamic localisation function names resolve
to authored `defined_text` entries.

Those source-level resolutions do not change the inspector's aggregate
`false` result. The element-level follow-up shows that the overlap component is
not an unclassified layout defect:

| window | reported overlaps | exact disposition |
|---|---:|---|
| National Conditions Panel | 10 | three animation/static-fallback pairs, six pairwise combinations among four mutually exclusive status medallions, and review-button text inside the review button |
| Northern Settlement Ledger | 9 | two animation/static-fallback pairs, six pairwise combinations among four mutually exclusive status medallions, and review-button text inside the review button |
| Concealed Evidence Ledger | 9 | two animation/static-fallback pairs, six pairwise combinations among four mutually exclusive status medallions, and inspect-button text inside the inspect button |

The scripted-GUI visibility table owns each animation/fallback and status swap.
Button labels are intentionally drawn over their button texture and are not
separate click blockers. The tool reports no click-bounds mismatch, invisible
click blocker, conflicting click region, missing sprite, missing texture,
missing localisation, text overflow, child-outside-clipped-parent, or
resolution drift.

The concealed ledger keeps its evidence rows hidden until
`ireland_concealed_evidence_revealed`; its inspect button requests review
but does not grant the reveal flag. Its ready/warning/critical display thresholds
now read the shared constants contract, including
`constant:ireland.evidence_gui_ready_public_threshold`.

## Visual and runtime asset evidence

The three generated background families and their shared controls were visually
reviewed from the four contact sheets. They have distinct institutional visual
languages and leave the authored text areas readable:

- forest-green civic records for National Conditions;
- blue-grey map and operations furniture for the Northern ledger;
- sealed dark archival material for concealed evidence.

The layouts reference 25 unique `GFX_ireland_*` sprites. All 25 names are
registered, have texture bindings, and resolve to runtime files. The GUI package
itself contains eleven final runtime textures under
`gfx/interface/ireland/gui`: three `920x704` backgrounds, four `32x32` status
medallions, `420x30` and `272x30` rows, a `280x38` review button, and a `44x38`
close button. DDS readback found no bright-green key pixels in any of the eleven
files.

The three surfaces collectively consume all seven authored animation families,
each paired with its registered static fallback:

- High Kingship crown selection;
- Five Provinces compact;
- convergence conclusion seal;
- Ailtirí takeover seal;
- compact-breach warning;
- hidden-evidence seal reveal;
- verified Otherworld entry.

The per-item GUI manifests point to the temporary source and processed package
under `assets/` and to the authoritative final DDS paths under `gfx/`.

## Offline inspector and render status

The fresh inspection provides nonzero element counts for all three exact
identifiers, as recorded in the current reconciliation above. Its aggregate
validation remains false, but the predicted-overlap subset is fully
dispositioned above. The remaining aggregate source-graph reports are:

- `INDEX_SYMBOL_COLLISION` for the canonical 140 named action sprites sharing
  70 action textures;
- unavailable `hoi_16mbs` metrics and deterministic substitute glyph paths in
  the offline renderer;
- unsupported or approximated GUI fields preserved for the engine;
- static-fallback warnings on animated sprite definitions even though each
  animation has a separately registered static sprite and a state-swapped GUI
  element.

These are inspector-model/reference limitations or intentional source
contracts, not evidence of a missing runtime texture or an unclassified
player-visible collision.

All three windows were rendered again at `1920x1080` and `1280x720` in normal,
warning, locked, and long-text states. Each request returned `GUI_RENDERED`
with no blocker. The response summaries were transport-truncated, so the
linked SVGs are offline review evidence rather than an independent live-engine
result:

- conditions:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/b5c91f6b263dc1760b35a671297d3a4fe5e1a947d974feaead5ee8f198d81dff/50efba274135d3fda26d76e2cfac0346a58435fd9edd66855017a12472cfb065/ireland_conditions_panel_window-full.svg`;
- Northern:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/3c36e4fd4edc66023c2f6b6f9132f9624da19a20b0186e70182c4c36cef5ed95/4b132c38d6ccd9c0b0eb29e84357d64f5218ee7b902ca9c040138ced41f1b5c6/ireland_northern_settlement_ledger_window-full.svg`;
- concealed evidence:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/5f1fb646c9dcf711263014f949854bd49973c4f63b6c572324d8e120023ba17c/0b9e0c73da6f5ede1b6c16a4478e81fbdc5d12009a84989d2d919e04e8ea4546/ireland_concealed_evidence_ledger_window-full.svg`.

### Superseded historical inspector observation

The earlier registered `ireland_audit` run recorded complete source models and
successful deterministic renders for all three windows at `1920x1080` and
`1280x720` in normal, warning, locked, and long-text states; that evidence
remains in `ireland_completion_recheck_2026-07-23.md`. A subsequent workspace
index observation returned `GUI_INSPECTED` with zero inspected elements and a
missing window for each identifier, alongside global source-graph blockers.
That zero-element observation is retained as historical tool evidence and is
superseded for current element counts by the fresh 58/40/36 inspection. It must
not be used as a current GUI pass or as a reason to rename valid windows.

## Result

The exact three GUI families, runtime placement, gameplay bindings,
localisation, generated source packages, static fallbacks, and seven-animation
handoffs are present in the current source. No placeholder or `assets/` path is
used as a runtime texture. Every predicted overlap has an intentional
state-layer or button-label explanation and the offline renders completed
without a blocker. The aggregate inspector result remains `false` for the
controlled-reuse and offline-fidelity reasons above; no live in-game testing is
required or claimed.
