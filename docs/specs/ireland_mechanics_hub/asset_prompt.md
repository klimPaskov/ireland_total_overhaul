# National Situation Ledger asset prompt

## Existing assets to reuse

- `gfx/interface/ireland/gui/conditions/background.dds` — 510 by 590 dashboard background;
- `gfx/interface/ireland/gui/shared/value_row.dds` — 420 by 30 selectable row;
- `gfx/interface/ireland/gui/shared/compact_row.dds` — compact row;
- `gfx/interface/ireland/gui/shared/action_button.dds` — guarded action button;
- `gfx/interface/ireland/gui/shared/status_ready.dds`, `status_warning.dds`, `status_critical.dds`, `status_locked.dds` — common state vocabulary.

## Visual direction

Use a restrained 1930s Irish civil-service ledger: aged cream paper, deep green leather or painted wood, brass rules, inked tab labels, and high-contrast values. Decoration must stay outside click regions. No national flag wallpaper, no portraits, and no ornamental icons that imply a mechanic which does not exist.

The focus inlay should look like the compact summary sheet pinned beside the focus branches. Its state colours and icon vocabulary must exactly match the full dashboard.

## Information requirements

- Tabs remain clearly distinct at normal and selected states.
- Row values remain readable at 100% UI scale.
- Available buttons are not grey; locked buttons carry a visible lock marker and an exact requirement tooltip.
- Green, amber, red, and lock-grey are never used decoratively.
- The static frame communicates the complete state. If an animated warning is produced, it must use planned source frames, a static fallback, manifest, contact sheet, and preview; it may not be a transform-only animation.

## Asset gate

Do not create new assets if the existing conditions and shared GUI package meets the layout and state requirements. Any new sprite receives a stable `GFX_ireland_mechanics_hub_*` identifier, source PNG, processed PNG, runtime DDS, manifest row, contact sheet, and `.gfx` handoff before wiring.

