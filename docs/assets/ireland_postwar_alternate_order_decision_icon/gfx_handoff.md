# Alternate postwar order decision icon GFX handoff

Status: wired by the parent implementation. The exact sprite is registered in
`interface/ireland_icons.gfx` and is consumed by
`ireland_action_record_an_alternate_postwar_order`; this handoff remains the
asset registration and provenance record.

Scope: source PNG, processed 32x32 RGBA PNG, runtime DDS, contact sheet, manifest, prompt record, and handoff only. No `.gfx`, gameplay, localisation, decision, GUI, or thumbnail files were edited.

The parent supplied the exact decision ID, sprite name, and runtime DDS path. These values are not proposed and must remain stable:

```text
Decision ID: ireland_action_record_an_alternate_postwar_order
Sprite name: GFX_decision_ireland_action_record_an_alternate_postwar_order
Texture path: gfx/interface/decisions/ireland/actions/decision_ireland_record_an_alternate_postwar_order.dds
Target size: 32x32
Suggested .gfx file: interface/ireland_icons.gfx
```

Ready-to-copy sprite definition for the parent-owned `.gfx` file:

```text
spriteType = {
	name = GFX_decision_ireland_action_record_an_alternate_postwar_order
	texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_record_an_alternate_postwar_order.dds"
}
```

Related consumer: `ireland_action_record_an_alternate_postwar_order`. The icon depicts an open diplomatic ledger, globe, and compass; it intentionally contains no United Nations emblem or laurel motif. The parent owns final `.gfx` insertion and decision-file wiring.
