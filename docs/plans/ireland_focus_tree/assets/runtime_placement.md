# Ireland runtime asset placement

`assets/ireland_focus_tree/` is the temporary source, processing, manifest, contact-sheet, and fallback-evidence package. It is not a runtime texture root.

Final DDS files used by the mod are under the standard `gfx/` tree:

- Focus goals: `gfx/interface/goals/ireland/`
- Focus shine registrations: `interface/ireland_focus_shine.gfx`, masking the final goal DDS under `gfx/interface/goals/ireland/` and using the standard HOI4 shine effect surface copied into `gfx/interface/goals/shine_overlay.dds`.
- Decision categories/actions/missions: `gfx/interface/decisions/`
- Spirits and laws: `gfx/interface/ideas/ireland/`
- Ireland overlays, ledger art, emblems, flags, and scripted-GUI art: `gfx/interface/ireland/`
- Event/news pictures and sourced report art: `gfx/event_pictures/ireland/`
- Leader portraits: `gfx/leaders/ireland/`
- Achievement states: `gfx/achievements/`
- Animation static fallbacks and sheets: `gfx/interface/animated/ireland/`

Route flag TGAs use the engine's standard `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` directories. The staged `final_tga` directory under `assets/` remains a provenance/rebuild copy.

All Ireland-owned `.gfx` registrations use `gfx/` paths. Source, processed, static-fallback, contact-sheet, and per-item manifest files remain under `assets/` so the final package can be audited or regenerated without mixing staging material into the shipped mod.

Blocked event-source candidates with manifest status `not_created` are retained only under `assets/ireland_focus_tree/sourced/review/blocked_runtime_candidates/`; they are not runtime DDS files and are not registered by any `.gfx` sprite.
