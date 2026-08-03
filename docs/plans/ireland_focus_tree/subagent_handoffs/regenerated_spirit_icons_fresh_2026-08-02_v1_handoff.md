# Fresh Ireland spirit icon source package — 2026-08-02 v1

## Scope

Generated exactly seven independent source PNGs for the Ireland persistent spirit rows with residual chroma-key pixels. Following the parent alpha audit, only `spirit_ireland_032` and `spirit_ireland_043` were regenerated completely fresh and their exact source filenames were overwritten. No existing or prior art was used as an edit target. This correction stops before alpha extraction, resizing, DDS conversion, GFX changes, gameplay changes, and localisation changes. Any pre-existing `alpha_png/`, `processed_png/`, audit, or tool artifacts in the package belong to the parent workflow and were not modified by this pass.

Package: `assets/ireland_focus_tree/icons/regenerated_spirit_icons_fresh_2026-08-02_v1/`

Runtime target retained for downstream work: **60x68**.

Source treatment: built-in `$imagegen`, compact centered HOI4 idea/national-spirit emblem, aged painterly material, dark outline, no UI box, no text, no matte, no neighboring tile/bleed, flat magenta chroma-key field requested as `#ff00ff`.

## Manifest

| Runtime row | Existing spirit meaning / picture | Source PNG | Status |
| --- | --- | --- | --- |
| `spirit_ireland_003` | `slopx_ireland_spirit_security_external_position` / `GFX_slopx_ireland_spirit_security_external_position` — external security | `source_png/spirit_ireland_003_source.png` | generated source only |
| `spirit_ireland_009` | `slopx_ireland_spirit_governing_costello_coalition` / `GFX_slopx_ireland_spirit_governing_costello_coalition` — coalition government | `source_png/spirit_ireland_009_source.png` | generated source only |
| `spirit_ireland_011` | `slopx_ireland_spirit_governing_norton_parliamentary` / `GFX_slopx_ireland_spirit_governing_norton_parliamentary` — parliamentary government | `source_png/spirit_ireland_011_source.png` | generated source only |
| `spirit_ireland_032` | `slopx_ireland_spirit_society_ira_republican` / `GFX_slopx_ireland_spirit_society_ira_republican` — republican society | `source_png/spirit_ireland_032_source.png` | fresh replacement source only |
| `spirit_ireland_034` | `slopx_ireland_spirit_society_oduffy` / `GFX_slopx_ireland_spirit_society_oduffy` — O'Duffy society | `source_png/spirit_ireland_034_source.png` | generated source only |
| `spirit_ireland_043` | `slopx_ireland_spirit_security_cosgrave_institutional` / `GFX_slopx_ireland_spirit_security_cosgrave_institutional` — institutional security | `source_png/spirit_ireland_043_source.png` | fresh replacement source only |
| `spirit_ireland_062` | `slopx_ireland_spirit_society_ira_ghq_command` / `GFX_slopx_ireland_spirit_society_ira_ghq_command` — IRA GHQ command | `source_png/spirit_ireland_062_source.png` | generated source only |

Full prompts and source dimensions are recorded in `generation_plan.json` beside the source PNGs.

## Replacement note

The parent alpha audit identified one bright-green residual pixel for `spirit_ireland_032` and one magenta residual pixel for `spirit_ireland_043`. Both source PNGs were regenerated with new built-in `$imagegen` calls, no input images, and tightened subject-palette exclusions. Their exact existing filenames were overwritten in place. The other five source rows were not regenerated or touched.

## GFX / runtime handoff

Keep the existing Ireland spirit sprite/picture registration and runtime row stems. The main agent should apply the downstream 60x68 crop/alpha-key workflow and replace only the seven corresponding runtime textures. No new sprite names or GFX edits are requested from this package; do not touch any other spirit row.

No DDS path is emitted because DDS processing is explicitly out of scope for this bounded handoff. No alpha-processed preview is emitted by this correction because alpha processing is explicitly out of scope; pre-existing parent workflow outputs were left untouched.

## Review note

Canonical references reviewed before generation: `vanilla_reference/icons/ideas/contact_sheet.png`, `generic_wall_line.png`, `idea_generic_flexible_foreign_policy.png`, and `idea_generic_purge.png`. The two replacement source PNGs are raw generated outputs and are not final runtime assets until the main agent performs the separately requested downstream processing.
