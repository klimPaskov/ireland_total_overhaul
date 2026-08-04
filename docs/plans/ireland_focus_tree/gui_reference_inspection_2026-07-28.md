# Ireland GUI reference inspection — 2026-07-28

Feature slug: `ireland_focus_tree`

This is offline MCP reference evidence only. HOI4 was not launched and no live GUI interaction or save-game scenario was run.

## Conditions panel inspection

The offline GUI inspection used workspace `mod_ireland_total_overhaul_65a6b5f140a7`, window `ireland_conditions_panel_window`, and scenario `ireland_conditions_opening`.

The tool completed its source scan (`GUI_INSPECTED`) and reported 58 inspected elements. Its source-graph validation was not a pass: it reported 73 blocking diagnostics, ten `GUI_VISIBLE_OVERLAP` observations, four missing elements, 51 unsupported elements, one unresolved element, and font/glyph/resolution-fidelity limitations.

The repeated-texture `INDEX_SYMBOL_COLLISION` observations point at the 70 unique decision-action textures that are deliberately registered under 140 named decision-action sprites. This is the canonical controlled-reuse budget: action classes may share an icon, while sprite names remain unique and no visible decision list may repeat an icon. The registrations use ordinary `spriteType` definitions with unique `name` values and shared `texturefile` paths; the MCP index warning is therefore not evidence of duplicate artwork, a missing icon, or a reason to expand the 70-texture budget. Live list visibility and duplicate-icon behavior remain unverified until the engine is run.

The later element-level extraction identifies all ten overlap observations
exactly: three animation/static-fallback pairs, six pairwise combinations among
the four mutually exclusive status medallions, and the review-button label
drawn over its button texture. The scripted-GUI visibility table prevents the
paired state layers from being shown together. The button label is intentional
button composition. No observation describes two independent player-facing
content rows or labels, so no GUI source file was changed.

## Offline render

The matching offline render completed with `GUI_RENDERED` for 1280×720 and 1920×1080 across the requested normal, hover, selected, locked, warning, minimum-value, maximum-value, long-text, and missing-localisation states. The returned render artifact is:

`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/f551c7f07c8090bc1a2438f74abd3edeb00c8c9f10c0337ef7e7c1a22e7c7d01/3047f20da08d2e025eeaec50bea791f03a402f29a724746c69238ec734f74cd3/ireland_conditions_panel_window-full.svg`

The response was truncated by the MCP transport and supplied no independent validation result. This artifact is useful for reference inspection, not a live-engine proof.

## Follow-up three-window render

The conditions, Northern, and concealed-evidence windows were rerendered on
2026-07-29 at `1920x1080` and `1280x720` in normal, warning, locked, and
long-text states. All three requests returned `GUI_RENDERED` with no blocker.
Their overlap totals are 10/9/9 and are exhausted by animation/fallback,
mutually exclusive status, and button-label shared slots. The exact
disposition and current artifact URIs are recorded in
`audits/ireland_gui_surface_reaudit_2026-07-29.md`.

## Completion boundary

The three panels are structurally wired and their source-level overlap reports
are fully classified. The aggregate inspector still reports false because
controlled action-texture reuse, unavailable offline font metrics, static
fallback inference, and unsupported render fields remain in its global source
graph. That aggregate is not converted into a live-engine claim. The current
goal-icon package is separately audited and lives at
`gfx/interface/goals/ireland/`; this GUI inspection does not authorize
replacing those freshly generated focus emblems with older staging batches.
