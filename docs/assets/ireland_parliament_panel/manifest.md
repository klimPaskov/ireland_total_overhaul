# Ireland Parliament panel asset manifest

Feature slug: `ireland_parliament_panel`

Asset type: scripted-GUI background, live chamber indicators, and action-control art

Source mode: generated background plus project-owned mechanical derivatives

## Background

- Asset name: `parliament_summary_background`.
- Intended use: decorative texture behind two enlarged chamber summaries and a two-by-two grid of parliamentary action controls.
- Source prompt: `docs/assets/ireland_parliament_panel/prompts/parliament_summary_background_prompt.md`.
- Source PNG: `docs/assets/ireland_parliament_panel/source_png/parliament_summary_background_source.png` (2014x780 RGB).
- Processed PNG: `docs/assets/ireland_parliament_panel/processed_png/parliament_summary_background_510x248.png` (510x248 RGBA).
- Final DDS: `gfx/interface/ireland/gui/parliament/parliament_summary_background.dds` (510x248 RGBA).
- Runtime sprite: `GFX_ireland_parliament_summary_background` in `interface/ireland_gui_assets.gfx`.
- Status: `wired`.
- Visual contract: restrained dark-green leather, aged cream paper, walnut, and tarnished brass. The central fields are deliberately low contrast and contain no people, flags, readable text, buttons, charts, checkmarks, icons, seals, or watermarks.

## Live chamber derivatives

- Assets: `dail_chamber_ui_large` and `seanad_chamber_ui_large`.
- Sources: the existing 21-frame Dáil and Seanad support strips.
- Processed PNGs: `dail_chamber_ui_large_126x70.png` and `seanad_chamber_ui_large_126x70.png` (2646x70 each).
- Final DDS files: `gfx/interface/ireland/gui/parliament/dail_chamber_ui_large.dds` and `gfx/interface/ireland/gui/parliament/seanad_chamber_ui_large.dds`.
- Processing: each source frame was resized independently with Lanczos resampling, then reassembled in its original order. This preserves all 21 live support states without fractional GUI scaling.
- Runtime sprites: `GFX_ireland_parliament_dail_large_ui` and `GFX_ireland_parliament_seanad_large_ui`.
- Runtime consumers: `dail_icon` and `seanad_icon` in `interface/ireland_parliament_scripted_gui.gui`.

## Action-control derivative

- Asset name: `parliament_step_button`.
- Source: existing project-owned `gfx/interface/ireland/gui/shared/action_button.dds`.
- Processed PNG: `docs/assets/ireland_parliament_panel/processed_png/parliament_step_button_204x32.png`.
- Final DDS: `gfx/interface/ireland/gui/parliament/parliament_step_button.dds` (204x32 RGBA).
- Runtime sprite: `GFX_ireland_gui_parliament_step_button`.
- Runtime use: four 204x32 click regions in a two-column, two-row grid. Each completion mark occupies its own 31px status column outside the click region, while the button natively centres its label.

## Action-state derivative

- Asset name: `parliament_action_states`.
- Sources: project-owned shared `status_locked`, `status_warning`, and
  `status_ready` seals.
- Processed PNG:
  `docs/assets/ireland_parliament_panel/processed_png/parliament_action_states_32x32.png`
  (four 32x32 frames in a 128x32 strip).
- Final DDS:
  `gfx/interface/ireland/gui/parliament/parliament_action_states.dds`.
- Runtime sprite: `GFX_ireland_gui_parliament_action_state`, four frames.
- Frame contract: slate locked, amber current-but-unaffordable, cream-gold
  current-and-available, green secured. Red is reserved for genuine failure.
- Runtime consumers: the four `ireland_parliament_power_*_state` icons. Their
  frame variables are recomputed from the same canonical triggers that enable
  the buttons and AI-only decisions.

## Review notes

- Keep essential controls away from the perimeter fasteners and folio corners.
- The background, chamber strips, and button texture match their declared GUI dimensions exactly.
- Contact sheet: `not_needed`; the generated package has one selected background and mechanical derivatives only.
