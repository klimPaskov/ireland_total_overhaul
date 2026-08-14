# Ireland national-question focus icon GFX handoff

Status: wired by the parent implementation. The proposed names in the original
handoff were adopted unchanged in `interface/ireland_icons.gfx`; this note is
retained as the asset provenance and registration record.

Scope: three generated static focus icons. This worker created source PNGs, processed 94x86 RGBA PNGs, runtime DDS files, manifest, prompt log, and checkerboard contact-sheet evidence only. No `.gfx`, gameplay, localisation, or GUI files were edited.

Registered target sprite surface: `interface/ireland_icons.gfx` (matching the
existing Ireland focus expansion handoff). The three sprite names below are
the adopted stable names.

```text
spriteType = { name = GFX_focus_ireland_unfinished_national_question texturefile = "gfx/interface/goals/ireland_unfinished_national_question.dds" }
spriteType = { name = GFX_focus_ireland_border_and_atlantic_dossier texturefile = "gfx/interface/goals/ireland_border_and_atlantic_dossier.dds" }
spriteType = { name = GFX_focus_ireland_test_the_state_instruments texturefile = "gfx/interface/goals/ireland_test_the_state_instruments.dds" }
```

| Focus ID | Final DDS | Registered sprite | Target size | Review evidence |
|---|---|---|---:|---|
| `ireland_unfinished_national_question` | `gfx/interface/goals/ireland_unfinished_national_question.dds` | `GFX_focus_ireland_unfinished_national_question` | 94x86 RGBA | `docs/assets/ireland_focus_expansion/national_question_additions_contact_sheet.png` |
| `ireland_border_and_atlantic_dossier` | `gfx/interface/goals/ireland_border_and_atlantic_dossier.dds` | `GFX_focus_ireland_border_and_atlantic_dossier` | 94x86 RGBA | `docs/assets/ireland_focus_expansion/national_question_additions_contact_sheet.png` |
| `ireland_test_the_state_instruments` | `gfx/interface/goals/ireland_test_the_state_instruments.dds` | `GFX_focus_ireland_test_the_state_instruments` | 94x86 RGBA | `docs/assets/ireland_focus_expansion/national_question_additions_contact_sheet.png` |

Apply the shared focus-button shine layer `gfx/interface/goals/shine_overlay.dds` through the existing focus-button shine mechanism; no per-icon shine texture is included. All three DDS files have transparent unused corners and were verified as 94x86 uncompressed 32-bit BGRA/RGBA with alpha.

Uncertainty: the generated map artwork is an illustrative 1930s cartographic
emblem, not an archival map. No icons are blocked or marked needs_user_review.
