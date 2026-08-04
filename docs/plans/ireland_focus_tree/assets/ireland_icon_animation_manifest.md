# Ireland focus-tree icon and animation implementation handoff

Status: asset production complete for the requested static classes and seven independent frame-based animations as of 2026-07-18. Current Ireland-owned interface files contain the runtime registrations; the source-package manifest remains separate and is not cleared by this handoff.

Feature: `ireland_focus_tree`
Canonical asset ledger: `assets/ireland_focus_tree/icons/ireland_icon_animation_manifest.md`
Worker handoff: `docs/plans/ireland_focus_tree/assets/ireland_icon_asset_handoff.md`

## Delivered static classes

| Class | Final files | Source PNGs | Processed PNGs | DDS |
| --- | ---: | ---: | ---: | ---: |
| Mission icons | 54 | 54 | 54 | 54 |
| Persistent route/law spirits | 63 | 63 | 63 | 63 |
| Temporary overlays | 27 | 27 | 27 | 27 |
| Law icons | 51 | 51 | 51 | 51 |
| Mechanic/ledger icons | 45 | 45 | 45 | 45 |
| Achievement states | 96 | 96 | 96 | 96 |

The source, processed, and final paths, exact spirit runtime mapping, and
contact sheets are recorded in the canonical manifest. The ordinal source rows
for missions, temporary overlays, laws, mechanics, and achievements are mapped
to their owning runtime IDs in `interface/ireland_secondary_assets.gfx`.
Spirits use their exact runtime names.

## Delivered independent animations

All seven packages contain independently produced source frames, processed frames, a PNG sheet, a static PNG fallback, a GIF preview, and a contact sheet in the temporary `assets/` staging tree. The corresponding final DDS sheet and static fallback are promoted to the standard `gfx/` tree and are the only runtime texture files. The required stable sprite names are:

| Slug | Frames | FPS | Loop | Static sprite | Animated sprite |
| --- | ---: | ---: | --- | --- | --- |
| `hidden_evidence_seal_reveal` | 6 | 6 | no | `GFX_ireland_hidden_evidence_seal_reveal` | `GFX_ireland_hidden_evidence_seal_reveal_animated` |
| `ailtiri_takeover_seal` | 8 | 8 | no | `GFX_ireland_ailtiri_takeover_seal` | `GFX_ireland_ailtiri_takeover_seal_animated` |
| `high_kingship_crown_selection` | 8 | 8 | no | `GFX_ireland_high_kingship_crown_selection` | `GFX_ireland_high_kingship_crown_selection_animated` |
| `five_provinces_compact` | 8 | 8 | no | `GFX_ireland_five_provinces_compact` | `GFX_ireland_five_provinces_compact_animated` |
| `verified_otherworld_entry` | 10 | 8 | no | `GFX_ireland_verified_otherworld_entry` | `GFX_ireland_verified_otherworld_entry_animated` |
| `compact_breach_warning` | 6 | 6 | yes | `GFX_ireland_compact_breach_warning` | `GFX_ireland_compact_breach_warning_animated` |
| `convergence_conclusion_seal` | 12 | 8 | no | `GFX_ireland_convergence_conclusion_seal` | `GFX_ireland_convergence_conclusion_seal_animated` |

## Implemented owning surfaces

`interface/ireland_animation_assets.gfx` registers all seven static
fallbacks and seven `frameAnimatedSpriteType` definitions with the documented
frame counts, rates, and loop flags. The three Ireland GUI files consume the
seven animated/static pairs:

- `ireland_concealed_evidence.gui`: evidence reveal and Otherworld entry;
- `ireland_northern_ledger.gui`: Ailtirí takeover and compact breach;
- `ireland_conditions.gui`: High Kingship, Five Provinces, and convergence.

No fourth GUI, still-image substitution, or staging ordinal is used.
