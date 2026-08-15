# Ireland Mechanics Hub asset manifest

Feature slug: `ireland_mechanics_hub`

## `focus_inlay_background`

- Asset name: Ireland National Situation focus-tree inlay background
- Asset type: static scripted-GUI / focus-tree inlay background panel
- Intended use: 460x248 four-card Cabinet Briefing shown in the decision view and beside the Ireland focus branches
- Source mode: `$imagegen`
- Generation rationale: This is bespoke fictional/symbolic UI art for the Ireland mechanics hub. The existing conditions dashboard background establishes the family style but does not provide the compact inlay canvas or its title/row/button negative-space layout.
- Generation prompt: [focus_inlay_background_prompt.md](prompts/focus_inlay_background_prompt.md)
- Source PNG: `docs/assets/ireland_mechanics_hub/source_png/focus_inlay_background_source.png`
- Processed RGBA PNG: `docs/assets/ireland_mechanics_hub/processed_png/focus_inlay_background.png`
- Final DDS: `gfx/interface/ireland/gui/conditions/focus_inlay_background.dds`
- Target size: `460x248`
- Sprite name: `GFX_ireland_mechanics_hub_inlay_background`
- Suggested `.gfx` file: `interface/ireland_gui_assets.gfx`
- Related GUI consumer: `interface/ireland_national_situation_inlay.gui`, background element `ireland_focus_inlay_background`
- Animation: none; static is sufficient because motion would not communicate additional state
- Contact sheet: not needed; this package contains one final variant. See [contact-sheet record](contact_sheets/NOT_NEEDED.md).
- Visual notes: Deep green leather/painted-wood frame, aged cream paper, restrained brass rules and fasteners, quiet title band, four-card negative space, and a quiet bottom band for one optional action. No baked text, flags, portraits, status colours, icons, button states, or click-region ornament.
- Status: `complete` and wired through `interface/ireland_gui_assets.gfx`, `interface/ireland_national_situation.gui`, and `interface/ireland_national_situation_inlay.gui`.

## `national_situation`

- Asset name: Ireland National Situation Ledger decision-category icon
- Related feature slug: `ireland_mechanics_hub`
- Asset type: static decision-category icon
- Intended in-game use: decision-category button for the Ireland Cabinet Briefing
- Source mode: `$imagegen`
- Generation rationale: A bespoke fictional/symbolic category emblem was required; the canonical decision-category references establish the compact transparent HOI4 silhouette, while the mechanics-hub prompt requires a distinct ledger/dashboard subject.
- Generation prompt: [national_situation_prompt.md](prompts/national_situation_prompt.md)
- Source PNG: `docs/assets/ireland_mechanics_hub/source_png/national_situation_source.png`
- Processed RGBA PNG: `docs/assets/ireland_mechanics_hub/processed_png/national_situation.png`
- Final DDS: `gfx/interface/decisions/categories/ireland/ireland_national_situation.dds`
- Target size: `52x40`
- Sprite name: `GFX_decision_category_ireland_national_situation`
- Suggested `.gfx` file: `interface/ireland_icons.gfx`
- Related decision category: `ireland_national_situation`
- Related GUI surface: `interface/ireland_national_situation.gui`; the small coloured register marks are decorative document dividers and do not correspond to tabs or extra player-facing values
- Visual notes: Open cream ledger with six distinct colored register tabs/marks, deep Irish green leather/painted wood, restrained brass, dark outline and subtle shadow. No text, people, flag, Parliament seal, or reused settlement-government emblem.
- Contact sheet: `docs/assets/ireland_mechanics_hub/contact_sheets/contact_sheet.png`
- Status: `complete` and wired through `interface/ireland_icons.gfx`, `common/decisions/categories/ireland_categories.txt`, and `interface/ireland_national_situation.gui`.

## `tab_selected`

- Asset name: Ireland National Situation Ledger selected-tab marker
- Related feature slug: `ireland_mechanics_hub`
- Asset type: static scripted-GUI selection marker
- Intended in-game use: selected-state underline below the six National Situation Ledger tabs
- Source mode: `$imagegen`
- Generation prompt: [tab_selected_prompt.md](prompts/tab_selected_prompt.md)
- Source PNG: `docs/assets/ireland_mechanics_hub/source_png/tab_selected_source.png`
- Processed RGBA PNG: `docs/assets/ireland_mechanics_hub/processed_png/tab_selected.png`
- Final DDS: `gfx/interface/ireland/gui/conditions/tab_selected.dds`
- Target size: `48x8`
- Sprite name: `GFX_ireland_mechanics_hub_tab_selected`
- Suggested `.gfx` file: `interface/ireland_gui_assets.gfx`
- Related GUI elements: `ireland_mechanics_hub_state_selected`, `ireland_mechanics_hub_provision_selected`, `ireland_mechanics_hub_readiness_selected`, `ireland_mechanics_hub_foreign_selected`, `ireland_mechanics_hub_northern_selected`, `ireland_mechanics_hub_culture_selected`
- Visual notes: One thin aged-brass horizontal rule with dark bronze edge and transparent corners; decorative selected-state marker, not a click region.
- Contact sheet: `docs/assets/ireland_mechanics_hub/contact_sheets/contact_sheet.png`
- Status: `superseded presentation asset`; retained as source evidence and registered for compatibility, but not consumed by the Cabinet Briefing.

## `row_selected`

- Asset name: Ireland National Situation Ledger selected-row marker
- Related feature slug: `ireland_mechanics_hub`
- Asset type: static scripted-GUI selection marker
- Intended in-game use: selected-state brass diamond/arrow at the left edge of each ledger value row
- Source mode: `$imagegen`
- Generation prompt: [row_selected_prompt.md](prompts/row_selected_prompt.md)
- Source PNG: `docs/assets/ireland_mechanics_hub/source_png/row_selected_source.png`
- Processed RGBA PNG: `docs/assets/ireland_mechanics_hub/processed_png/row_selected.png`
- Final DDS: `gfx/interface/ireland/gui/conditions/row_selected.dds`
- Target size: `14x14`
- Sprite name: `GFX_ireland_mechanics_hub_row_selected`
- Suggested `.gfx` file: `interface/ireland_gui_assets.gfx`
- Related GUI elements: `ireland_mechanics_hub_row_1_selected` through `ireland_mechanics_hub_row_7_selected`
- Visual notes: One small aged-brass diamond with a right-pointing notch, dark bronze outline, and transparent corners; decorative selected-state marker, not a click region.
- Contact sheet: `docs/assets/ireland_mechanics_hub/contact_sheets/contact_sheet.png`
- Status: `superseded presentation asset`; retained as source evidence and registered for compatibility, but not consumed by the Cabinet Briefing.
