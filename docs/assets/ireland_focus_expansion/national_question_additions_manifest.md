# Ireland national-question focus icon additions manifest

Feature slug: `ireland_focus_tree`

Source mode: generated symbolic art via Codex built-in image generation (`image_gen`). No real photographs, archival maps, or sourced documents were used. The canonical national-focus reference contact sheet at `.agents/skills/hoi4-feature-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png` was inspected before generation, along with the existing Ireland focus expansion contact sheet. All three assets are distinct generated artworks and have no controlled reuse approval.

| ID | Type | Target | Source PNG | Processed PNG | Final DDS | Sprite | Size | Source mode | Status |
|---|---|---|---|---|---|---|---:|---|---|
| `ireland_unfinished_national_question` | focus | `focus:ireland_unfinished_national_question` | `assets/ireland_focus_tree/icons/expansion_focus_icons/source_png/ireland_unfinished_national_question.png` | `assets/ireland_focus_tree/icons/expansion_focus_icons/processed_png/ireland_unfinished_national_question.png` | `gfx/interface/goals/ireland_unfinished_national_question.dds` | `GFX_focus_ireland_unfinished_national_question` | 94x86 RGBA | generated | complete / wired |
| `ireland_border_and_atlantic_dossier` | focus | `focus:ireland_border_and_atlantic_dossier` | `assets/ireland_focus_tree/icons/expansion_focus_icons/source_png/ireland_border_and_atlantic_dossier.png` | `assets/ireland_focus_tree/icons/expansion_focus_icons/processed_png/ireland_border_and_atlantic_dossier.png` | `gfx/interface/goals/ireland_border_and_atlantic_dossier.dds` | `GFX_focus_ireland_border_and_atlantic_dossier` | 94x86 RGBA | generated | complete / wired |
| `ireland_test_the_state_instruments` | focus | `focus:ireland_test_the_state_instruments` | `assets/ireland_focus_tree/icons/expansion_focus_icons/source_png/ireland_test_the_state_instruments.png` | `assets/ireland_focus_tree/icons/expansion_focus_icons/processed_png/ireland_test_the_state_instruments.png` | `gfx/interface/goals/ireland_test_the_state_instruments.dds` | `GFX_focus_ireland_test_the_state_instruments` | 94x86 RGBA | generated | complete / wired |

## Generation and processing notes

- The source PNGs are the original transparent outputs copied from the Codex image-generation workspace; no local drawing, recolouring, compositing, or panel reuse was used.
- `ireland_unfinished_national_question` shows a folded government map dossier, the Ireland island silhouette, one dark partition border, and Atlantic approach routes. Its visual map is illustrative rather than archival.
- `ireland_border_and_atlantic_dossier` is a separate coastwatch survey folio with rolled charts, coastwatch pins, binoculars, and shipping-route arcs; it is not a crop or variant of the unfinished-question icon.
- `ireland_test_the_state_instruments` is a separate legal/diplomatic folio with tied cable papers, a wax seal, signet, pen, and dispatch ribbon; it contains no map or military weapon.
- Every generated prompt prohibited readable text, labels, letters, numerals, watermarks, and modern symbols. The output was resized directly to the owning 94x86 focus canvas with RGBA preserved.
- Review evidence: `docs/assets/ireland_focus_expansion/national_question_additions_contact_sheet.png` shows each processed icon over a checkerboard, with its ID and 94x86 RGBA dimensions.
- DDS conversion used `.agents/skills/hoi4-feature-assets/tools/convert_to_dds.py` with `--width 94 --height 86`. DDS headers report 94x86 uncompressed 32-bit BGRA with alpha masks, and Pillow reopens each file as RGBA with transparent corner pixels.
- Generated source outputs retained for provenance in `C:\Users\klimp\.codex\generated_images\019fff94-e7a0-7442-ab22-196b5bbf3238`:
  - `exec-23f3014c-f5f4-4464-9215-d0160847eccd.png` → `ireland_unfinished_national_question`
  - `exec-d507ac86-4768-4650-9801-59f95501b8a6.png` → `ireland_border_and_atlantic_dossier`
- `exec-7b1a8134-d39f-4286-9803-7081b6259bd4.png` → `ireland_test_the_state_instruments`

## Runtime wiring status

The three sprite names are no longer proposed. They are registered in
`interface/ireland_icons.gfx`, with matching focus shine registrations in
`interface/ireland_focus_expansion_shine.gfx`. The runtime focus source,
localisation, and AI references resolve against these stable names. The final
family-lane layout is a separate accepted presentation surface at `89ff719`;
parent completion audit/live evidence remains separate.
