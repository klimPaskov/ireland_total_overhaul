# Ireland flag budget re-audit — 2026-07-29

## Canonical budget

The Ireland asset ledger requires one historical base flag and eighteen
alternate route-flag sets. Every set must follow the engine flag roots and
normal, medium, and small size conventions.

## Base flag

The sourced base tricolour package is `S-01` in
`docs/plans/ireland_focus_tree/assets/source_manifest.json`. Its runtime files
exist at:

- `gfx/flags/IRE.tga` — 82×52
- `gfx/flags/medium/IRE.tga` — 41×26
- `gfx/flags/small/IRE.tga` — 10×7

All three files read back as RGB TGA assets at the declared dimensions. The
manifest records their individual SHA-256 hashes and retains the S-01 C3
attribution and official-colour/proportion review conditions.

## Alternate route identities

The runtime contains exactly eighteen `IRE_SLOPX_*` flag identities in each of
the three engine flag roots: 54 alternate TGAs in total. Every file has the
correct dimensions for its root, and every size group contains eighteen unique
hashes.

The identities are:

1. `IRE_SLOPX_ARMY_COUNCIL`
2. `IRE_SLOPX_CIVIL_REPUBLICAN`
3. `IRE_SLOPX_WORKERS_PARTY`
4. `IRE_SLOPX_WORKERS_SMALLHOLDERS`
5. `IRE_SLOPX_CORPORATE_ESTATE`
6. `IRE_SLOPX_ODUFFY_PERSONAL`
7. `IRE_SLOPX_CATHOLIC_GUARDIANS`
8. `IRE_SLOPX_GAELIC_CORPORATE`
9. `IRE_SLOPX_CHRISTIAN_NATIONAL`
10. `IRE_SLOPX_REGIONAL_AIS_EIRGHE`
11. `IRE_SLOPX_AIS_EIRGHE`
12. `IRE_SLOPX_HIGH_KING_SACRAL`
13. `IRE_SLOPX_HIGH_KING_CONSTITUTIONAL`
14. `IRE_SLOPX_PENTARCHY`
15. `IRE_SLOPX_FIVEFOLD_FEDERATION`
16. `IRE_SLOPX_OTHERWORLD_DOMINION`
17. `IRE_SLOPX_COMPACT_TWO_IRELANDS`
18. `IRE_SLOPX_CONVERGENCE_ORDER`

`common/countries/slopx_ireland_cosmetic.txt` defines exactly these eighteen
cosmetic identities. The Ireland runtime route helpers reference all eighteen;
no defined identity is unused and no referenced identity is missing.

## Result and boundary

The one-base-plus-eighteen-alternate flag budget is complete at the static
runtime layer. The alternate flags are generated post-divergence assets and do
not assert historical provenance. This audit does not close the separate
portrait, symbol/document, sourced event-image, Radical mission-capacity, or
achievement-schema blockers. No live HOI4 launch was used.
