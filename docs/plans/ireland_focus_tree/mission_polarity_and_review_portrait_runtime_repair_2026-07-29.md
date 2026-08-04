# Ireland mission polarity and review-portrait runtime repair

Date: 2026-07-29

## Mission presentation repair

All 54 Ireland missions are non-selectable objective missions. Their
`available` blocks are the success conditions and their `complete_effect`
blocks apply full or partial success. The previous `is_good = yes` setting
made the engine label those success effects as failure effects in the mission
tooltip.

`common/decisions/ireland_decisions.txt` now uses `is_good = no` for all
54 mission families. This matches the offline Decision Modding reference:
`is_good = no` presents `available` as successful completion and
`timeout_effect` as the result of missing the deadline. No objective, deadline,
outcome, escalation, AI weight, capacity rule, or cleanup effect changed.

## Review-only portrait runtime cleanup

Twenty-two C3 portrait packages marked `needs_user_review` had no gameplay
consumer but were registered in
`interface/ireland_sourced_assets.gfx` and copied into
`gfx/leaders/ireland/`. Their runtime registrations and DDS copies have been
removed:

`P-09`, `P-13`, `P-14`, `P-17`, `P-18`, `P-19`, `P-21`, `P-22`, `P-23`,
`P-25`, `P-28`, `P-29`, `P-30`, `P-34`, `P-36`, `P-40`, `P-44`, `P-47`,
`P-49`, `P-52`, `P-53`, and `P-58`.

Their source originals and provenance remain preserved byte-for-byte under
`docs/portraits/`. Their processed review files remain under the temporary
`assets/ireland_focus_tree/` staging tree. No manifest row was promoted,
rejected, or reclassified by this cleanup.

The seven review-gated portraits that currently have gameplay consumers remain
explicit blockers: `P-05`, `P-06`, `P-27`, `P-43`, `P-46`, `P-56`, and
`RC-PORTRAIT-01`.

## Static evidence

- `is_good = yes`: 0 Ireland mission rows.
- `is_good = no`: 54 Ireland mission rows.
- Runtime DDS inventory after removing the 22 unconsumed review copies:
  856 total, of which 855 are Ireland-owned under the established audit scope.
- The nine Ireland GFX files contain 1,084 texture references under the
  established audit scope and 324 unique sprite names.
- The canonical manifest plus route-character extensions contain 57
  review-gated rows. Exactly seven have runtime DDS files, and each is a
  current character consumer listed above. No other review-gated symbol,
  document, event/news, or portrait row has a runtime DDS file.
- The same combined inventory contains 67 blocked rows, and none has a runtime
  DDS file.
- The portrait archive remains 208 files.

HOI4 was not launched. Live testing is excluded from this goal's completion
gate by user direction.

## Round-seven source integration

The later round-seven pass preserves five additional portrait-source inventory
files, bringing `docs/portraits/` to 213 files. P-33 John Hayes becomes a
conditional review package; no round-seven portrait enters runtime.

The independently cleared S-19 *An Claidheamh Soluis* package adds one runtime
DDS and one source-side sprite registration. The post-integration inventory is
857 runtime DDS files total / 856 Ireland-owned, with 1,085 texture references
under the established Ireland audit scope and 325 unique sprite names. The
earlier 856/855 and 1,084/324 figures above remain the exact snapshot taken
immediately after the portrait cleanup.
