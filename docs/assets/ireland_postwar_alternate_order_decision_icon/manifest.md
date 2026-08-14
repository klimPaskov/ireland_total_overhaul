# Alternate postwar order decision icon manifest

Feature slug: `ireland_postwar_alternate_order_decision_icon`  
Asset type: generated HOI4 decision icon  
Source mode: built-in `$imagegen` generation  
Generation date: 2026-08-14  
Related decision: `ireland_action_record_an_alternate_postwar_order`  
Visual purpose: Ireland formally records a non-UN alternate postwar diplomatic order after the UN admission authority is unavailable.  
Reference inspected: `.agents/skills/hoi4-feature-assets/assets/vanilla_reference/README.md`, `CATALOG.md`, `icons/decisions/contact_sheet.png`, and individual decision references including `decision_usa_congress.png`, `decision_generic_disband_irregulars.png`, `decision_bra_integralism.png`, and `decision_generic_intelligence_operation.png`.  
Processing: alpha-aware crop to the generated subject bounds, LANCZOS resize to exact 32x32 RGBA, then `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py` using the repository's 32-bit BGRA DDS workflow.  
Scope note: no gameplay, decision, localisation, `.gfx`, GUI, or thumbnail file was edited.

Runtime wiring status: the parent has registered the exact sprite
`GFX_decision_ireland_action_record_an_alternate_postwar_order` in
`interface/ireland_icons.gfx`; the asset package is wired. The separate
family-lane focus layout is accepted at `89ff719`; parent completion
audit/live evidence remains separate.

## Requirement-to-runtime coverage

| Requirement | In-game purpose | Source package and manifest entry | Runtime registration | Live consumer | Status |
| --- | --- | --- | --- | --- | --- |
| `ALT-ORDER-ICON-01` | Compact diplomatic ledger / globe / compass emblem for the alternate postwar-order decision | This package; `ireland_action_record_an_alternate_postwar_order` | `gfx/interface/decisions/ireland/actions/decision_ireland_record_an_alternate_postwar_order.dds` through the parent-supplied sprite `GFX_decision_ireland_action_record_an_alternate_postwar_order` | Decision ID `ireland_action_record_an_alternate_postwar_order` | complete |

## Asset entry

| Field | Value |
| --- | --- |
| Asset name | `ireland_action_record_an_alternate_postwar_order` |
| Asset type | Decision icon; separate 32x32 decision-specific artwork |
| Intended use | Decision action icon for recording the alternate postwar diplomatic order |
| Source mode | `$imagegen`; fictional/alternate-history institutional symbol |
| Source PNG | `docs/assets/ireland_postwar_alternate_order_decision_icon/source_png/ireland_action_record_an_alternate_postwar_order_source.png` |
| Processed PNG | `docs/assets/ireland_postwar_alternate_order_decision_icon/processed_png/ireland_action_record_an_alternate_postwar_order.png` |
| Final DDS | `gfx/interface/decisions/ireland/actions/decision_ireland_record_an_alternate_postwar_order.dds` |
| Target size | 32x32 RGBA source/processed preview and 32x32 DDS |
| Sprite name | `GFX_decision_ireland_action_record_an_alternate_postwar_order` (parent-supplied exact value) |
| Suggested `.gfx` file | `interface/ireland_icons.gfx` (handoff only; not edited) |
| Localisation key | Not applicable to this asset package |
| Contact sheet | `docs/assets/ireland_postwar_alternate_order_decision_icon/contact_sheet.png` |
| Status | complete |

## Visual and validation notes

- The generated source is an open diplomatic ledger with a compact brass globe and compass, using sober bronze, parchment, charcoal, and muted sea-green tones.
- No United Nations emblem, laurel, UN globe-and-wreath mark, text, or UI plate is present.
- The source and processed PNGs contain real alpha transparency; unused canvas pixels remain transparent.
- The checkerboard contact sheet confirms the processed icon remains centered and readable at 32x32.
- DDS header verification: `DDS ` magic, 32x32 dimensions, 32-bit uncompressed BGRA masks (`R=0x00FF0000`, `G=0x0000FF00`, `B=0x000000FF`, `A=0xFF000000`), one mip level, and 4096-byte pixel payload.
- No fallback, placeholder, recolour-only substitute, or reused decision icon was used.
