# GFX handoff — Ireland mechanics hub inlay background

- Final DDS: `gfx/interface/ireland/gui/conditions/focus_inlay_background.dds`
- Proposed sprite: `GFX_ireland_mechanics_hub_inlay_background`
- Suggested target: `interface/ireland_gui_assets.gfx`
- Intended consumer: `interface/ireland_national_situation_inlay.gui`, `ireland_focus_inlay_background`

Ready-to-copy sprite definition:

```text
spriteType = { name = GFX_ireland_mechanics_hub_inlay_background texturefile = "gfx/interface/ireland/gui/conditions/focus_inlay_background.dds" }
```

The current inlay GUI reserves a 460x248 surface, a title/instruction band at the top, six status placements in the middle, and two action-button positions at the bottom. The art intentionally leaves those regions quiet; render all text, status sprites, and button states separately. No `.gfx` or `.gui` file was edited by this asset subagent.

## National Situation Ledger category icon

- Final DDS: `gfx/interface/decisions/categories/ireland/ireland_national_situation.dds`
- Exact runtime sprite: `GFX_decision_category_ireland_national_situation`
- Suggested target: `interface/ireland_icons.gfx`
- Target size: `52x40` RGBA/DDS
- Intended consumer: decision category `ireland_national_situation` and the National Situation Ledger tab identity in `interface/ireland_national_situation.gui`

Ready-to-copy sprite definition:

```text
spriteType = { name = GFX_decision_category_ireland_national_situation texturefile = "gfx/interface/decisions/categories/ireland/ireland_national_situation.dds" }
```

The emblem is a distinct open cream ledger with six colored register tabs/marks, deep Irish green leather/painted wood, and restrained brass. It is not a Parliament seal, flag, or settlement-government derivative. No `.gfx`, decision, GUI, or localisation file was edited by this asset subagent.

## Selected-tab marker

- Final DDS: `gfx/interface/ireland/gui/conditions/tab_selected.dds`
- Exact runtime sprite: `GFX_ireland_mechanics_hub_tab_selected`
- Suggested target: `interface/ireland_gui_assets.gfx`
- Target size: `48x8` RGBA/DDS
- Intended consumers: `ireland_mechanics_hub_state_selected`, `ireland_mechanics_hub_provision_selected`, `ireland_mechanics_hub_readiness_selected`, `ireland_mechanics_hub_foreign_selected`, `ireland_mechanics_hub_northern_selected`, and `ireland_mechanics_hub_culture_selected`

Ready-to-copy sprite definition:

```text
spriteType = { name = GFX_ireland_mechanics_hub_tab_selected texturefile = "gfx/interface/ireland/gui/conditions/tab_selected.dds" }
```

This is a decorative brass selected-state underline with transparent corners; the GUI owns its placement and visibility.

## Selected-row marker

- Final DDS: `gfx/interface/ireland/gui/conditions/row_selected.dds`
- Exact runtime sprite: `GFX_ireland_mechanics_hub_row_selected`
- Suggested target: `interface/ireland_gui_assets.gfx`
- Target size: `14x14` RGBA/DDS
- Intended consumers: `ireland_mechanics_hub_row_1_selected` through `ireland_mechanics_hub_row_7_selected`

Ready-to-copy sprite definition:

```text
spriteType = { name = GFX_ireland_mechanics_hub_row_selected texturefile = "gfx/interface/ireland/gui/conditions/row_selected.dds" }
```

This is a decorative brass diamond/arrow selected-state marker with transparent corners; the GUI owns its placement and visibility.
