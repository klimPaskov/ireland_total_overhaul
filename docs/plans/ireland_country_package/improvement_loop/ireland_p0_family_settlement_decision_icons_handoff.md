# P0 family settlement decision-icon asset handoff

Status: complete asset package; runtime wiring closed by the parent.
Produced: 2026-08-14  
Scope: ten static decision icons requested for the accepted P0 “Five Families Survive the Peace” tranche.

## Deliverables

- Source PNGs: `docs/assets/ireland_p0_family_settlement_decision_icons/source_png/` (ten generated RGBA sources).
- Exact 32x32 processed RGBA PNGs: `docs/assets/ireland_p0_family_settlement_decision_icons/processed_png/`.
- Runtime DDS: `gfx/interface/decisions/ireland/actions/` using the final `decision_ireland_<name>.dds` paths recorded in the package manifest.
- Review contact sheets: `docs/assets/ireland_p0_family_settlement_decision_icons/contact_sheet.png` plus the source and processed sheets under `contact_sheets/`.
- Prompt log: `docs/assets/ireland_p0_family_settlement_decision_icons/prompts.md`.
- Manifest: `docs/assets/ireland_p0_family_settlement_decision_icons/manifest.md`.
- GFX handoff: `docs/assets/ireland_p0_family_settlement_decision_icons/gfx_handoff.md`.

## Exact IDs covered

Settlement actions:

- `ireland_action_ratify_the_postwar_republic`
- `ireland_action_civilianise_the_workers_congress`
- `ireland_action_place_the_directorate_under_statute`
- `ireland_action_convert_contracts_to_reconstruction_credit`
- `ireland_action_define_the_postwar_crown`

Recovery actions:

- `ireland_action_reconstitute_the_postwar_coalition`
- `ireland_action_reconvene_the_workers_congress`
- `ireland_action_demobilise_the_failed_directorate`
- `ireland_action_rebalance_the_producer_estates`
- `ireland_action_reconvene_the_crown_council`

## Runtime closure

The parent registered all ten sprites in `interface/ireland_icons.gfx` using
`GFX_decision_<exact decision ID>` names, including the `ireland_action_`
segment, and the decision implementation consumes those stable IDs. The
shorter proposed names from this historical handoff are superseded by the
registered names documented in
`docs/assets/ireland_p0_family_settlement_decision_icons/manifest.md`.
No gameplay, localisation, `.gfx`, or thumbnail files were edited here.

## Evidence and review

All ten source images came from separate `$imagegen` prompts and are not placeholders or fallbacks. The generated art was reviewed against the canonical decision reference contact sheet. Every processed PNG is 32x32 RGBA with real transparency; every listed DDS exists, reports 32x32 in its DDS header, uses the repository's 32-bit BGRA masks, and retains transparent pixels. The processed contact sheet shows the ten icons at enlarged nearest-neighbour scale over a checkerboard for visual review.
