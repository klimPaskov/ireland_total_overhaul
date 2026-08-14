# Parser and Parliament Button Fix — 2026-08-14

Status: implemented in commit `070fbb5`; the lifecycle/parser follow-up is
covered by commit `1984ff0`. This document is a bounded repair record, not a
feature-completion claim.

## Scope

This tranche fixes the reported Ireland-owned trigger/parser errors and restores a visually distinct enabled state for the National Settlement Parliament controls.

## Script corrections

- Replaced invalid `is_at_war = no` country triggers with the documented `has_war = no` trigger in the territorial decisions and shared Atlantic enforcement trigger.
- Replaced malformed scalar `free_building_slots > 0` tests with typed `free_building_slots` trigger blocks. Civilian reconstruction checks `industrial_complex`; producer armament checks `arms_factory`.
- No costs, route gates, completion effects, or AI weights were changed.

## Parliament enabled state

- The prior `parliament_step_button` source was charcoal grey even when enabled, so engine state shading could not communicate availability clearly.
- The enabled source is now bottle green with an antique-brass frame. The engine's `buttonstate.lua` treatment remains responsible for disabled, hover, and pressed states.
- The four canonical `<element>_click_enabled` scripted GUI triggers and shared guarded executors remain authoritative. This is a presentation-state repair, not a bypass of the gameplay requirements.

## Files

- `common/decisions/ireland_expansion_decisions.txt`
- `common/national_focus/ireland_focus_tree.txt`
- `common/scripted_triggers/ireland_triggers.txt`
- `gfx/interface/ireland/gui/parliament/parliament_step_button.dds`
- `docs/assets/ireland_parliament_panel/processed_png/parliament_step_button_204x32.png`
- `docs/assets/ireland_parliament_panel/source_png/parliament_step_button_active_source.png`
- `docs/assets/ireland_parliament_panel/prompts/parliament_step_button_active_prompt.md`
- `docs/assets/ireland_parliament_panel/manifest.md`

## Evidence

- Scripted GUI inspection parses and links the Parliament source graph with no blocking source diagnostic or visible-overlap diagnostic.
- The enabled PNG and runtime DDS are both 204x32 and preserve the existing stable sprite name `GFX_ireland_gui_parliament_step_button`.
- Analyzer cost notices are limited to its inability to follow the thin GUI click wrappers into the shared guarded Parliament executors; the executable costs remain centralized in those helpers.

## Simplifications, omissions, and blockers

None for this bounded parser and button-state repair.
