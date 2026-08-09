# GFX handoff — Ireland Parliament summary background

Wired by the main implementation.

- Final DDS: `gfx/interface/ireland/gui/parliament/parliament_summary_background.dds`
- Proposed sprite name: `GFX_ireland_parliament_summary_background`
- Suggested target file: `interface/ireland_gui_assets.gfx`
- Target size: `510x198`
- Suggested sprite definition:

```text
spriteType = {
	name = "GFX_ireland_parliament_summary_background"
	texturefile = "gfx/interface/ireland/gui/parliament/parliament_summary_background.dds"
}
```

- Intended GUI use: decorative panel background behind two chamber summaries in the upper 110 px and a four-step progress strip in the lower 70 px.
- State semantics: none; this is a single static background layer.
- Avoid covering the perimeter brass fasteners/folio corners with essential text or controls. The central paper and lower leather areas are deliberately low contrast for overlaid scripted-GUI content.
- Runtime registration: `interface/ireland_gui_assets.gfx`.
- Runtime consumer: `ireland_parliament_background` in `interface/ireland_parliament_scripted_gui.gui`.
- The asset package itself did not edit `.gfx`, `.gui`, localisation, or gameplay files.

The same wired surface also uses a mechanically resized copy of the existing
21-frame Seanad chamber strip:

```text
spriteType = {
	name = "GFX_ireland_parliament_seanad_compact_ui"
	texturefile = "gfx/interface/ireland/gui/parliament/seanad_chamber_ui_compact.dds"
	noOfFrames = 21
}
```

Each compact frame is 90x50, matching the Dáil strip's 50px height while
preserving all 21 live support states and avoiding fractional GUI scaling.
