# GFX handoff — Ireland Parliament interactive panel

Wired by the main implementation.

- Background DDS: `gfx/interface/ireland/gui/parliament/parliament_summary_background.dds` (510x248).
- Background sprite: `GFX_ireland_parliament_summary_background`.
- Dáil DDS: `gfx/interface/ireland/gui/parliament/dail_chamber_ui_large.dds` (21 frames at 126x70).
- Dáil sprite: `GFX_ireland_parliament_dail_large_ui`.
- Seanad DDS: `gfx/interface/ireland/gui/parliament/seanad_chamber_ui_large.dds` (21 frames at 126x70).
- Seanad sprite: `GFX_ireland_parliament_seanad_large_ui`.
- Button DDS: `gfx/interface/ireland/gui/parliament/parliament_step_button.dds` (204x32).
- Button sprite: `GFX_ireland_gui_parliament_step_button`.
- Action-state DDS: `gfx/interface/ireland/gui/parliament/parliament_action_states.dds` (four 32x32 frames).
- Action-state sprite: `GFX_ireland_gui_parliament_action_state`.
- Registration file: `interface/ireland_gui_assets.gfx`.
- Runtime consumer: `interface/ireland_parliament_scripted_gui.gui`.

The upper 148 pixels hold the two balanced chamber summaries. The lower 100
pixels hold four functional parliamentary actions in a two-by-two grid. Button
textures and click regions have identical dimensions. Each status mark sits in
a separate column outside the click region, and each label uses the button's
native centring so neither can intercept or offset the action.

The generated background has no state semantics. The chamber sprites use the
live Dáil and Seanad frame variables, while scripted-GUI visibility and enabled
triggers own the action states. Each action has one non-overlapping state seal:
slate locked, amber unaffordable, gold current, or green secured. The gold state
uses the enabled button's native hover and pressed treatment; red is reserved
for actual failure states.
