# Ireland error-log repair — 2026-08-05

## Mod-owned repairs

- Removed UTF-8 byte-order marks from the focus shine interface, secondary asset interface, and Ireland national spirits files so the files parse normally.
- Corrected the concealed-evidence and northern-ledger GUI definitions: button sizes use `x`/`y`, while text boxes use `maxWidth`/`maxHeight`.
- Added compatibility entity definitions for the missing Italian mechanized, German super-heavy armor, and Soviet super-heavy armor entity references used by the installed game content.

## Runtime verification

- Launched the executable directly from `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\hoi4.exe`; Steam was not used for the final validation.
- Confirmed the game reached a responsive DirectX 11 window.
- Confirmed the freshly generated `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\logs\error.log` remained empty after the game loaded and during an additional 15-second check.
- Closed the game after verification; no HOI4 process remains running.

## Static verification

- Runtime icon-surface audit: all required surfaces complete.
- BOM checks, GUI-size checks, entity-reference checks, and `git diff --check`: passed.
