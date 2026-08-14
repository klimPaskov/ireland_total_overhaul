# Inlay asset handoff — 2026-08-14

## Result

Created the final static 460x248 Ireland National Situation focus-tree inlay background using `$imagegen`, then processed it to RGBA PNG and converted it with the repository DDS workflow.

## Files created

- Source generated PNG: `docs/assets/ireland_mechanics_hub/source_png/focus_inlay_background_source.png`
- Processed RGBA PNG: `docs/assets/ireland_mechanics_hub/processed_png/focus_inlay_background.png`
- Runtime DDS: `gfx/interface/ireland/gui/conditions/focus_inlay_background.dds`
- Prompt record: `docs/assets/ireland_mechanics_hub/prompts/focus_inlay_background_prompt.md`
- Manifest: `docs/assets/ireland_mechanics_hub/manifest.md`
- Contact-sheet decision: `docs/assets/ireland_mechanics_hub/contact_sheets/NOT_NEEDED.md`
- GFX handoff: `docs/assets/ireland_mechanics_hub/gfx_handoff.md`

## Handoff

- Sprite to register: `GFX_ireland_mechanics_hub_inlay_background`
- Suggested registration file: `interface/ireland_gui_assets.gfx`
- Final DDS path: `gfx/interface/ireland/gui/conditions/focus_inlay_background.dds`
- GUI consumer: `interface/ireland_national_situation_inlay.gui`
- Static only: no animation package was created because motion would not communicate additional state.

## Visual/functional constraints satisfied

- Deep green leather or painted-wood frame, cream ledger surface, restrained brass rules and fasteners.
- Low-contrast negative space for the live title, six status rows, and two bottom buttons.
- No baked text, flags, portraits, status colours, icons, buttons, watermarks, or click-region ornament.
- No `.gfx`, `.gui`, gameplay, localisation, specs, or `thumbnail.png` edits were made.

## Validation evidence

- Processed PNG inspected at exactly 460x248 and RGBA mode.
- DDS conversion completed successfully at exactly 460x248.
- Existing `gfx/interface/ireland/gui/conditions/background.dds` was inspected as the adjacent presentation reference and left unchanged.

Asset production is complete; main-agent sprite registration and GUI wiring remain pending.

## Integration closure appended 2026-08-15

The production handoff above is retained as the historical asset boundary. Parent integration has since completed the previously pending registration and wiring:

- `GFX_ireland_mechanics_hub_inlay_background` is registered in `interface/ireland_gui_assets.gfx` against `gfx/interface/ireland/gui/conditions/focus_inlay_background.dds`.
- `interface/ireland_national_situation_inlay.gui` consumes the registered sprite as the 460x248 inlay background.
- `common/focus_inlay_windows/ireland_national_situation_inlay.txt` and `common/national_focus/ireland_focus_tree.txt` expose the inlay, with the focus declaration at `x = -600, y = 10`.
- Focus inspection revision `90beeec44304c287` and GUI inspection revision `7f7b1126f87a3ebc` provide the current structural and inlay review evidence; no asset-production action remains for this package.
