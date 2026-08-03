# Ireland fresh icon package audit — 2026-08-02

## Scope

This audit covers the regenerated Ireland focus-goal and law-stage package,
the seven spirit replacements, and the Ireland-owned runtime icon surfaces.
It is static file and image evidence only; no HOI4 process or live-save test
was used.

## Fresh goal/law package

Package: `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/`

- 216/216 focus sources, alpha PNGs, processed PNGs, and staged DDS files.
- 51/51 law sources, alpha PNGs, processed PNGs, and staged DDS files.
- 267/267 rows pass `audits/alpha_centering_audit.json`.
- 267/267 staged and runtime DDS rows pass
  `audits/dds_readback_audit.json`, including dimensions, transparent
  corners/borders, centering, visible chroma checks, and staged/runtime SHA
  equality.
- Six focus contact sheets and three law contact sheets were visually
  reviewed. The rows have compact centered HOI4 emblems with consistent
  padding and no boxes, atlas tiles, neighboring bleed, clipping, or visible
  chroma-key matte.

The final files are installed only at:

- `gfx/interface/goals/slopx_ireland/` — 216 DDS.
- `gfx/interface/ideas/slopx_ireland/laws/` — 51 DDS.

## Spirit replacements

Package: `assets/ireland_focus_tree/icons/regenerated_spirit_icons_fresh_2026-08-02_v1/`

Rows `003`, `009`, `011`, `032`, `034`, `043`, and `062` pass the seven-row
alpha/centering audit and `audits/spirit_dds_readback.json`. Their verified DDS files are
installed at `gfx/interface/ideas/slopx_ireland/spirits/` without changing
the existing sprite names or idea wiring.

## Runtime surface readback

`audit_runtime_icon_surfaces.py` reports all expected Ireland-owned surfaces
complete:

| surface | rows | target/readback |
|---|---:|---|
| focus goals | 216 | `100x88`, clean transparent edges |
| law stages | 51 | `60x68`, clean transparent edges |
| route spirits | 63 | `60x68`, clean transparent edges |
| decision categories | 13 | `52x40` |
| decision actions | 70 | `32x32` |
| missions | 54 | `33x32` |
| mechanic/ledger | 45 | `64x64` |
| temporary overlays | 27 | `32x32` |
| emblems | 16 | expected opaque emblem canvases |
| flags | 54 | expected opaque flag canvases |

The audit distinguishes intentionally green/teal subject paint in presentation
art from visible chroma-key residue. The animated contact sheets remain
transparent-ready and were not treated as green-screen failures merely
because their Otherworld or heraldic subjects use green/teal paint.
