# Ireland goal-icon visual QA — historical 2026-07-24 package

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`

Superseded by the fresh v12 package at
`assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/`.
Its authoritative static review is `audit_v12.md`: 216 independent rows at
100x88, zero atlas-cell bleed, zero chroma residue, zero edge contact, and zero
staging/runtime hash mismatches. The v3 atlas package described below is
retained only as rejected historical evidence.

This record covers the 216 national-focus goal icons and supplements the
static registration audit. It does not close the separate source-clearance or
live-engine gates.

## Current disposition

The earlier 2026-07-23 extraction/normalization batch is rejected for visual
style and retained under
`assets/ireland_focus_tree/icons/rejected_normalized_2026-07-23/` for technical
comparison only. It is not part of the runtime package.

The v3 replacement was a fresh built-in image-generation package. Most rows were generated as four-emblem source atlases and retained as individual source tiles; the remaining rows were generated as individual source images. Each source tile was freshly generated for the exact focus semantic; no rejected icon,
previous source, processed PNG, runtime DDS, contact sheet, or vanilla PNG was
used as imagegen input. The replacement is staged under
`assets/ireland_focus_tree/icons/regenerated_goal_icons_v3_2026-07-24/` and
the final DDS files live only under the standard mod `gfx/` tree.

## HOI4 goal-icon acceptance rules

Every goal row must have:

- one freshly generated source PNG tile and one processed RGBA preview in its
  v3 package;
- one `94x86` runtime DDS at
  `gfx/interface/goals/slopx_ireland/goal_<exact_focus_id>.dds`;
- a centered, readable painted subject with consistent transparent breathing
  room;
- dark hand-painted contour, aged brush texture, restrained 1930s palette, and
  varied silhouettes suitable for the vanilla national-focus surface;
- no circular badge template, wreath/seal/coin framing, hard rectangular card,
  text, logo, fake checkerboard, white matte, chroma green, or opaque canvas.

Rectangular objects that are the subject of the icon (books, ledgers,
documents, crates, ballots, or buildings) are retained. A painted rectangular
background surrounding a subject is not.

## Generation and processing record

The fresh source atlases and source PNG tiles remain unchanged as provenance evidence. The
approved local chroma-key, shared-canvas fitting, and DDS conversion tools were
used only after fresh generation; no prior art was used as an input to this
replacement package. The v3 source paths, processed paths, runtime paths, audit,
and review sheet are recorded in:

`assets/ireland_focus_tree/icons/regenerated_goal_icons_v3_2026-07-24/`

The complete visual review is:

`assets/ireland_focus_tree/icons/regenerated_goal_icons_v3_2026-07-24/v3_goal_icons_contact_sheet.png`

The rejected package is intentionally preserved and never referenced by the
runtime `.gfx` registrations. The v3 package was the prior runtime source and
is superseded by the direct-source v4 package recorded in the current QA file.

## Static evidence

The parent verifier is:

`python -B assets/ireland_focus_tree/icons/tools/review_goal_icons_v3.py`

It checks every focus ID for source, processed, DDS, and runtime coverage; 94x86
processed dimensions; green residue; opaque corners; empty alpha; centered
bounds; duplicate names; old-source/processed hash reuse; unique hashes; and
empty temporary DDS staging. Runtime DDS headers and the 216 stable `.gfx`
registrations are checked in the companion handoff audit.

This report is evidence for the goal-icon package only; it does not claim
overall Ireland feature completion.

## Final disposition

The completed v3 audit reports 216/216 source, processed, DDS, and runtime rows;
216 exact `.gfx` path pairs; 94x86 DDS headers; 216 unique processed hashes;
no reused old source or processed rows; no green residue, opaque corners, empty
rows, off-centre rows, edge contact, missing rows, or temporary DDS staging.
The visual acceptance sheet is the v3 contact sheet linked above.
