# Ireland animation chroma cleanup audit — 2026-07-29

## Finding and repair

The static animation package audit found that the seven generated frame
families still displayed their bright green source-key field in the processed
contact sheets. This was a real transparency defect, not a GUI render warning.

The shared build script at
`assets/ireland_focus_tree/animations/package_ireland_animations.py` now runs
the repository's green-spill removal and edge-decontamination logic before
resizing every source frame. The original generated source frames were not
changed. The seven processed packages, previews, horizontal sheets, static
fallbacks, and runtime DDS files were rebuilt.

## Static package evidence

| Family | Frame size | Frames | Sheet | Processed PNGs | Source hashes | Green-key pixels | Opaque corners |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `hidden_evidence_seal_reveal` | 64×64 | 6 | 384×64 | 6 | 6 | 0 | 0 |
| `ailtiri_takeover_seal` | 96×96 | 8 | 768×96 | 8 | 8 | 0 | 0 |
| `high_kingship_crown_selection` | 96×96 | 8 | 768×96 | 8 | 8 | 0 | 0 |
| `five_provinces_compact` | 96×96 | 8 | 768×96 | 8 | 8 | 0 | 0 |
| `verified_otherworld_entry` | 128×128 | 10 | 1280×128 | 10 | 10 | 0 | 0 |
| `compact_breach_warning` | 64×64 | 6 | 384×64 | 6 | 6 | 0 | 0 |
| `convergence_conclusion_seal` | 128×128 | 12 | 1536×128 | 12 | 12 | 0 | 0 |

Every source frame has a distinct SHA-256 hash. Each processed frame has the
declared target dimensions, and each sheet width equals its frame width times
its declared frame count. The contact sheets were reviewed over a checkerboard
field after rebuilding.

## Runtime DDS evidence

The fourteen runtime files were rebuilt under the standard mod tree:

`gfx/interface/animated/slopx_ireland/<family>/`

Each family has one static fallback DDS and one horizontal sheet DDS. DDS
readback reports the declared static/sheet dimensions for all fourteen files,
zero visible green-key pixels, and transparent corners. No live HOI4 launch or
playback test was used, in accordance with the completion boundary.

## Remaining boundary

This closes the animation transparency defect. It does not close the separate
source-clearance, achievement schema, Radical mission-capacity, or other
engine-reference blockers recorded in the Ireland completion ledger.
