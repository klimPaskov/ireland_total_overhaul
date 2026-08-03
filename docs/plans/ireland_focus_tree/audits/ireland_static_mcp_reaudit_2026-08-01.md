# Ireland static MCP re-audit

Date: 2026-08-01

Status: current offline engine-reference evidence; HOI4 was not launched.

## Workspace and scope

The checks below use the Ireland workspace selector
`mod_ireland_total_overhaul_65a6b5f140a7` and the current worktree. They are read-only
inspections. Live game execution, fresh saves, and in-game playthroughs remain
outside the completion gate by user direction.

## Focus tree and icon references

`hoi4.focus_inspect` resolved `slopx_ireland_focus_tree` from
`common/national_focus/slopx_ireland_focus_tree.txt` with 216 Ireland focus
nodes, 197 connectors, zero connector crossings, zero node intersections, and
zero long connectors. The 14 blocking diagnostics returned by the global
inspection are unrelated vanilla continuous-focus references (missing
continuous-focus sprites); no Ireland-local focus diagnostic was returned.

`hoi4.focus_raster` completed a decoded raster review of the same tree and
resolved the Ireland goal sprites from the runtime `gfx/interface/goals/`
package. Its only listed errors are the same 14 unrelated vanilla continuous
focus references. The tool produced the HTML, SVG, PNG, JSON, source-map, and
plan artifacts without proposing or changing files.

## Map references

`hoi4.map_inspect` checked states 113, 119, 134, and 135. The map validation
passed all five available checks: province definitions and IDs, bitmap
geometry, state/region membership, networks/adjacencies, and positions/ports.
There were no unknown or missing-geometry province IDs. State 119 therefore
remains a valid engine-reference target for the Northern review and does not
grant ownership, control, occupation, settlement, integration, or a core by
itself.

## Scripted GUI references

`hoi4.gui_inspect` resolved the Conditions Panel window with 58 inspected
elements and a complete source graph. Its validation remains false because the
offline graph reports 97 blocking diagnostics: the intentional 140 named
action / 70 texture reuse contract, offline font/fallback inference, and
unsupported renderer fields. Ten visible overlaps are the authored
animation/static-fallback pairs, mutually exclusive status medallions, and
button labels over their own plates. They are not detached icon fragments or
runtime cross-surface bleed.

Fresh `hoi4.gui_render` calls for the Conditions Panel, Northern Settlement
Ledger, and Concealed Evidence Ledger at 1280x720 across normal, warning,
locked, and long-text states returned `GUI_RENDERED` with no tool blockers.
The wire response was truncated for each large SVG artifact; the linked
artifacts remain the authoritative visual records. Earlier 1920x1080 and
1280x720 renders for all three surfaces remain recorded in
`audits/ireland_gui_surface_reaudit_2026-07-29.md`.

The repeated-texture diagnostics are classified against vanilla rather than
removed by duplicating the action budget: vanilla `.gfx` files reuse
`gfx/interface/goals/shine_overlay.dds` and other shared textures across many
sprite definitions. Ireland retains unique sprite names, explicit 140-to-70
consumer mapping, and the canonical source/runtime audit.

## Event inspection boundary

The focused `hoi4.event_inspect` namespace lint returned no blocking
diagnostics in its bounded result, but its validation remained false because
the large workspace deferred helper and lifecycle projections. The tool also
reported global counts rather than an Ireland-only proof surface. This result
is retained as partial evidence and does not replace the current Ireland event
source comparison and non-live scenario trace.

## Disposition

No gameplay, GUI, `.gfx`, or asset file was changed by this re-audit. The
current remaining non-live work is source clearance and any genuinely
Ireland-local static defect discovered by a bounded inspection; the global
vanilla diagnostics, intentional texture reuse, and mutually exclusive GUI
overlays are not treated as Ireland implementation defects.
