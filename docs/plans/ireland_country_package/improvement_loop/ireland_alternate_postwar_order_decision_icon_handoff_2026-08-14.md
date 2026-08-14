# Alternate postwar order decision-icon asset handoff

Status: complete asset package, ready for parent wiring.  
Produced: 2026-08-14  
Parent: `/root`  
Scope: one static 32x32 decision icon for the alternate postwar-order action. No commit made.

## Exact runtime contract

- Decision ID: `ireland_action_record_an_alternate_postwar_order`
- Sprite: `GFX_decision_ireland_action_record_an_alternate_postwar_order`
- DDS: `gfx/interface/decisions/ireland/actions/decision_ireland_record_an_alternate_postwar_order.dds`
- Suggested target `.gfx`: `interface/ireland_icons.gfx`
- Target: 32x32 transparent decision icon

## Deliverables

- Generated source PNG: `docs/assets/ireland_postwar_alternate_order_decision_icon/source_png/ireland_action_record_an_alternate_postwar_order_source.png`
- Exact processed PNG: `docs/assets/ireland_postwar_alternate_order_decision_icon/processed_png/ireland_action_record_an_alternate_postwar_order.png`
- Runtime DDS: `gfx/interface/decisions/ireland/actions/decision_ireland_record_an_alternate_postwar_order.dds`
- Review contact sheet: `docs/assets/ireland_postwar_alternate_order_decision_icon/contact_sheet.png`
- Prompt record: `docs/assets/ireland_postwar_alternate_order_decision_icon/prompts.md`
- Manifest: `docs/assets/ireland_postwar_alternate_order_decision_icon/manifest.md`
- GFX handoff: `docs/assets/ireland_postwar_alternate_order_decision_icon/gfx_handoff.md`

## Art direction and evidence

The selected generated artwork uses an open diplomatic ledger, compact globe, and brass compass as one sober institutional silhouette. It is distinct from the existing family settlement icons and was designed specifically for 32x32 decision readability. The final source contains no UN emblem, laurel, text, or UI plate. The checkerboard contact sheet was reviewed after alpha crop and resize.

DDS verification found exact 32x32 dimensions, 32-bit uncompressed BGRA masks, and a 4096-byte pixel payload. No fallback or placeholder was used. The parent owns `.gfx` insertion, decision wiring, localisation, and final game validation.
