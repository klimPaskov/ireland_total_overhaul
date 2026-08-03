# Ireland v8 HOI4 focus-goal icon regeneration

Feature slug: `ireland_focus_tree`

Date: 2026-07-28

## Reason for the regeneration

The earlier v7 package was technically transparent and complete but did not
meet the requested HOI4 goal-icon style. The user specifically required a
fresh regeneration rather than reprocessing. v8 therefore regenerated all
216 subjects from new built-in image-generation output and replaced the final
runtime DDS set. No earlier Ireland icon was used as a source or reference.

## Production boundary

The temporary package is:

`assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v8/`

It contains fourteen source atlases, alpha atlases, 216 source crops, 216
processed previews, 216 DDS files, a row-level manifest, prompts, audit,
visual review, and runtime handoff. The final runtime directory is:

`gfx/interface/goals/slopx_ireland/`

Only the 216 audited DDS files belong in the runtime `gfx/` tree. The stable
registration file is `interface/slopx_ireland_icons.gfx`; no registration was
changed to point at `assets/`.

## Art direction

The fresh prompt targets the readable HOI4 national-focus emblem language:
large central silhouettes, dark brown/black ink contours, flatter painterly
shading, aged period materials, restrained bronze/parchment/steel/deep-green/
navy/oxblood accents, and distinct route-specific civic, military, maritime,
industrial, rural, cultural, constitutional, and symbolic subjects. It
prohibits readable text, portraits, UI panels, square boxes, plaques, glossy
toy-like rendering, and a full-field green background. Green is a temporary
chroma-key matte only.

## Build and audit evidence

The manifest records all 216 focus-to-cell mappings and source/processed/DDS
SHA-256 values. The pre-promotion audit found exact 216/216/216 name sets,
216 unique hashes in each output class, 100x88 processed and DDS dimensions,
transparent corners, no empty or off-center outputs, no edge contact, no
readback failures, and zero source or processed hash overlap with v7. A
separate post-promotion comparison matched all 216 runtime DDS hashes to the
v8 staging hashes.

The complete contact sheet and alpha atlas review found no final square tile,
full-field matte, or greenscreen residue. Intentional olive and deep-green
painted details remain part of route-specific subjects. The v8 package is the
only current Ireland goal-icon runtime set; v7 and older packages are retained
as historical review evidence and are not runtime inputs.

## Remaining validation boundary

This tranche is static asset and registration evidence. HOI4 was not launched,
as directed by the user. Live focus-tree loading, in-game scaling/readability,
and the broader Ireland feature validation programme remain open and are not
closed by this asset replacement.
