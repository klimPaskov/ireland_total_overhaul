# Ireland Parliament panel asset manifest

Feature slug: `ireland_parliament_panel`

Asset type: scripted-GUI background panel / custom feature UI art

Source mode: `$imagegen` (generated)
Source rationale: this is a fictional, symbolic 1930s Irish parliamentary dossier surface with no single real archival image requirement; generated art provides the required wide, low-contrast layout and material treatment without inventing a real document or person.

## Asset

- Asset name: `parliament_summary_background`
- Intended use: decorative background texture behind two balanced chamber summaries in the upper area and a four-step progress strip in the lower area of the Ireland Parliament decision-category scripted GUI.
- Source prompt: [prompts/parliament_summary_background_prompt.md](prompts/parliament_summary_background_prompt.md)
- Source PNG: `docs/assets/ireland_parliament_panel/source_png/parliament_summary_background_source.png` (2014x780 RGB)
- Processed PNG: `docs/assets/ireland_parliament_panel/processed_png/parliament_summary_background_510x198.png` (510x198 RGBA)
- Final DDS: `gfx/interface/ireland/gui/parliament/parliament_summary_background.dds` (510x198 RGBA, repository converter output)
- Target size: `510x198`
- Proposed sprite: `GFX_ireland_parliament_summary_background`
- Suggested `.gfx`: `interface/ireland_gui_assets.gfx`
- Related GUI surface: Ireland Parliament decision-category scripted GUI; decorative only, not state-driven.
- Status: `wired`
- Generation notes: restrained dark green leather, aged cream paper, walnut and tarnished brass details; broad low-contrast negative space is intentional. No people, flags, readable text, buttons, charts, checkmarks, icons, seals, or watermarks are present.
- Contact sheet: `not_needed` (single final asset; no alternatives retained).

## Review notes and risks

- The source crop is nearly the requested aspect ratio and was cover-cropped to preserve the central paper field and lower leather band.
- The generated image includes edge fasteners and folio corners only at the perimeter; keep interactive text and progress elements away from those edges where possible.
- The art is intentionally low contrast so overlaid UI text remains legible; overly strong tinting or opacity changes in the GUI may reduce material separation.
- The main implementation registers the sprite in `interface/ireland_gui_assets.gfx` and consumes it as the decorative base layer in `interface/ireland_parliament_scripted_gui.gui`.

## Supporting chamber derivative

- Asset name: `seanad_chamber_ui_compact`.
- Source: existing project-owned `gfx/interface/ireland/gui/parliament/seanad_chamber_ui.dds`, a 2772x73 strip of 21 frames at 132x73 each.
- Processed PNG: `docs/assets/ireland_parliament_panel/processed_png/seanad_chamber_ui_compact_90x50.png` (1890x50 RGBA; 21 frames at 90x50).
- Final DDS: `gfx/interface/ireland/gui/parliament/seanad_chamber_ui_compact.dds` (1890x50 RGBA).
- Processing: each source frame was resized independently with Lanczos resampling, then reassembled in its original frame order. This gives the Seanad and Dáil equal 50px visual height without relying on sub-pixel GUI scaling.
- Runtime sprite: `GFX_ireland_parliament_seanad_compact_ui` in `interface/ireland_gui_assets.gfx`.
- Runtime consumer: `seanad_icon` in `interface/ireland_parliament_scripted_gui.gui`.
