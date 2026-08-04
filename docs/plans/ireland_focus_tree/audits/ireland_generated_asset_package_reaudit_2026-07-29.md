# Ireland generated asset package re-audit — 2026-07-29

## Scope and placement

This is an offline audit of the generated Ireland event/news, alternate-flag,
and route-emblem package. Hearts of Iron IV was not launched.

`assets/ireland_focus_tree/generated/` contains temporary source masters,
processed PNGs, manifests, retained alternatives, and review contact sheets.
The authoritative engine files remain under the standard `gfx/` tree. The
aggregate manifest records every per-item source, processed, final, purpose,
generation rationale, sprite handoff, static-fallback relationship, and
controlled-reuse rule.

## Generated event and news allocation

The package contains exactly 51 generated event/news concepts:

- 51 unique source PNGs;
- 51 unique processed PNGs;
- 51 unique runtime DDS files under `gfx/event_pictures/ireland/`;
- six `397x153` black-and-white news strips;
- 45 `210x176` sepia report cards.

All 51 runtime paths are registered in
`interface/ireland_event_art.gfx`, and all 51 registered sprites have an
Ireland event consumer. The High Kingship and Northern unity images are
consumed by the bounded public conclusion records
`ireland_events.432` and `.433`; the former begins the existing
conclusion review, while the latter records the public settlement after the
H14 outcome has opened its existing foreign-reaction window. Neither grants
territory, cores, industry, equipment, units, fuel, shipping, offices,
alignment, or recognition.

The complete contact sheet was reviewed after rebuilding the processed
family. Forty-five report cards contained low-alpha colour contamination at
their transparent edges. Only pixels with alpha at or below 16 were
neutralised, after which all 45 runtime DDS files and the contact sheet were
rebuilt. A scan of the 51 source, 51 processed, and 51 runtime images found no
bright-green key pixels; the processed and runtime sets retain 51 unique
hashes apiece.

## Alternate route flags

The package contains exactly eighteen generated alternate route identities.
Each identity has one source crop and normal, medium, and small processed
forms. The package therefore contains 54 processed PNGs and 54 final DDS
handoff textures at `82x52`, `41x26`, and `10x7`.

The authoritative engine flag files are the 54 TGA files under `gfx/flags/`,
`gfx/flags/medium/`, and `gfx/flags/small/`. Every size root contains exactly
eighteen `IRE_IRELAND_*` files, all eighteen cosmetic tags are defined and
called by the route runtime, and every size group has eighteen unique hashes.
No source, processed, DDS, or runtime TGA flag contains a bright-green key
pixel.

## Route emblems

The package contains exactly eight generated faction or regional-order
emblems. Each has one source crop, a `128x128` static form, and a `32x32` UI
form: eight unique sources, sixteen unique processed PNGs, and sixteen unique
runtime DDS files under `gfx/interface/ireland/emblems/`.

All sixteen runtime paths are registered in
`interface/ireland_route_assets.gfx`. The contact sheet shows a
consistent transparent emblem treatment with no atlas-neighbour bleed, boxed
source tiles, or green-screen residue.

## Result and remaining boundary

The generated 51-image, eighteen-flag, and eight-emblem package is complete at
the source, processed, manifest, registration, consumer, and static-runtime
layers. This does not close the separate 69 sourced event/news allocation, 60
sourced portrait allocation, 40 historical source packages, source-clearance
queue, achievement visibility schema limitation, or Radical/Underground
mission-capacity contradiction.
