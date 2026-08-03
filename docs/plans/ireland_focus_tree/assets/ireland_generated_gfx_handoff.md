# Ireland Generated Icon and Animation GFX Handoff

This handoff is limited to generated assets produced by the icon worker. It does not replace the source-package handoff. Runtime `.gfx` registrations are maintained by the main implementation under `interface/`; final DDS files are shipped under `gfx/`, while source and processing material remains under `assets/`.

Scope reconciliation (2026-07-22): the statement above that no `.gfx` files were edited is a worker-scope statement, not current repository status. Current structural registrations are evidenced by `interface/slopx_ireland_icons.gfx` and the Ireland-owned `.gfx` files; source clearance remains governed by `docs/plans/ireland_focus_tree/assets/source_manifest.json` and `docs/plans/ireland_focus_tree/assets/clearance_audit.md`. Use `docs/plans/ireland_focus_tree/source_of_truth_map.md` for the cross-document disposition.

## Ready static sprites

The following completed classes have source PNG, processed PNG, final DDS, exact dimensions, and contact-sheet evidence:

```text
focus:              goal_<exact_focus_id>                 100x88  (216; current fresh vanilla-emblem package)
decision category:  decision_category_ireland_<001-013>   52x40  (13)
decision action:    decision_action_ireland_<001-066,077-080> 33x32 (70 allocated; 140 named aliases)
law state:          law_ireland_<001-051>                 60x68  (51; fresh centered three-state idea-emblem package)
```

Suggested sprite naming pattern for the main agent:

```text
GFX_slopx_ireland_<sprite_suffix>
```

Suggested texture roots:

```text
gfx/interface/goals/slopx_ireland/
gfx/interface/decisions/categories/slopx_ireland/
gfx/interface/decisions/slopx_ireland/actions/
```

The current focus source, processed preview, staging DDS, and runtime hash
manifest is `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/manifest.json`.
The current law source triptychs, state crops, processed previews, staging DDS,
and centered-placement audit are in
`assets/ireland_focus_tree/icons/regenerated_law_icons_hoi4_idea_emblems_fresh_2026-07-28_v1/`.
The final runtime DDS files remain under `gfx/interface/goals/slopx_ireland/`
and `gfx/interface/ideas/slopx_ireland/laws/`; source and processing material
under `assets/` is temporary staging evidence.

The parent must replace ordinal category/action suffixes with exact runtime IDs if those IDs are supplied later. The ordinal names are explicitly proposed, not parent-provided names.

## Spirit runtime names reserved by parent

Use the exact names listed in `ireland_icon_animation_manifest.md`, including:

```text
GFX_slopx_ireland_spirit_governing_order
GFX_slopx_ireland_spirit_organised_society
GFX_slopx_ireland_spirit_security_external_position
```

All 63 names are listed in the manifest and registered in `interface/slopx_ireland_secondary_assets.gfx` against `gfx/interface/ideas/slopx_ireland/spirits/`.

## Animation wiring templates

For each approved animation, the implementation agent should verify the target surface against local vanilla/repository examples before use:

```text
spriteType = {
    name = "GFX_slopx_ireland_<slug>"
    texturefile = "gfx/interface/animated/slopx_ireland/<slug>/<slug>_static.dds"
}

frameAnimatedSpriteType = {
    name = "GFX_slopx_ireland_<slug>_animated"
    texturefile = "gfx/interface/animated/slopx_ireland/<slug>/sheets/<slug>_sheet.dds"
    noOfFrames = <ledger frame count>
    animation_rate_fps = <ledger fps>
    looping = <ledger loop>
    play_on_show = yes
}
```

The seven exact frame counts, sizes, FPS values, loop behavior, and runtime names are in the manifest. Static fallbacks and animated sheets are registered in `interface/slopx_ireland_animation_assets.gfx` under `gfx/interface/animated/slopx_ireland/`.

## Missing wires

- Runtime registrations cover the 369 generated icon rows plus missions, spirits, temporary overlays, laws, mechanic ledger, achievements, scripted-GUI art, and animation fallbacks/sheets.
- Achievement DDS files are shipped under `gfx/achievements/` using the exact achievement IDs declared in `common/achievements/slopx_ireland_achievements.txt`; the source/processed staging rows may retain ordinal package basenames, while the 96 unregistered ordinal DDS copies found by the all-icon sweep are staging-only cleanup evidence under `assets/ireland_focus_tree/icons/runtime_cleanup/legacy_numeric_achievements_2026-07-28/`.
- The authoritative source/clearance manifest remains under `docs/plans/ireland_focus_tree/assets/`; runtime placement does not change a source item's clearance state.

## Completion state

Do not claim the Ireland asset task complete. The package is partially complete with exact completed counts and explicit blockers recorded in the manifest.
