# Ireland user-approved conditional asset re-audit — 2026-08-01

Feature slug: `ireland_focus_tree`
Namespace: `ireland`

This is the non-live audit for the explicit user-approved conditional source
promotion. It covers exact source objects, processed previews, final runtime
DDS files, SHA-256 reconciliation, and source-side GFX registration. It does
not claim C4 or unrestricted redistribution permission for any C3 package.

## Manifest result

The authoritative `assets/source_manifest.json` parses as 169 entries:

| Family | Complete | Blocked | C3 complete | C4 complete |
| --- | ---: | ---: | ---: | ---: |
| Portrait | 45 | 15 | 35 | 10 |
| Symbol/document | 25 | 15 | 18 | 7 |
| Event/news | 54 | 15 | 40 | 14 |
| Total | 124 | 45 | 93 | 31 |

There are no `needs_user_review` rows in the 169-row machine manifest. The
Daniel Morrissey route extension remains separately review-gated, and Father
Edward Cahill remains blocked without an exact portrait object.

## Promoted exact packages

| Row | Final runtime DDS | Dimensions | SHA-256 prefix | Runtime sprite | Consumer boundary |
| --- | --- | ---: | --- | --- | --- |
| S-24 | `gfx/interface/ireland/sourced/symbol_document_s_24.dds` | 128×128 | `F5D04C827EE2F2A3` | `GFX_ireland_symbol_document_s_24` | registration-only; no unrelated consumer invented |
| S-27 | `gfx/interface/ireland/sourced/symbol_document_s_27.dds` | 397×153 | `6A88D55EBFCD3E6B` | `GFX_ireland_symbol_document_s_27` | registration-only; armband/date uncertainty retained |
| EV-SRC-007 | `gfx/event_pictures/ireland/event_ev_src_007_report.dds` | 210×176 | `26C3E290E85EC8D8` | `GFX_report_event_ireland_report_historical_chain_report_07` | registration-only; exact consumer remains unassigned |
| EV-SRC-010 | `gfx/event_pictures/ireland/event_ev_src_010_report.dds` | 210×176 | `09E2E88C621DEF23` | `GFX_report_event_ireland_report_historical_chain_report_10` | registration-only; observation-sheet candidate remains distinct |
| EV-SRC-016 | `gfx/event_pictures/ireland/event_ev_src_016_report.dds` | 210×176 | `9E929A4BEC494E99` | `GFX_report_event_ireland_report_historical_chain_report_16` | registration-only; Dúchas conditions retained |
| EV-SRC-025 | `gfx/event_pictures/ireland/event_ev_src_025_report.dds` | 210×176 | `49F444EA747E96A8` | `GFX_report_event_ireland_report_constitutional_crisis_report_07` | registration-only; exact consumer remains unassigned |
| EV-SRC-034 | `gfx/event_pictures/ireland/event_ev_src_034_news.dds` | 397×153 | `8A7F303FC1EBB524` | `GFX_news_event_ireland_news_historical_news_04` | registration-only; folklore is not labelled as wartime evidence |
| EV-SRC-043 | `gfx/event_pictures/ireland/event_ev_src_043_news.dds` | 397×153 | `12909A3B00911A06` | `GFX_news_event_ireland_news_historical_news_13` | registration-only; no unrelated news event rewired |
| EV-SRC-052 | `gfx/event_pictures/ireland/event_ev_src_052_report.dds` | 210×176 | `C81F9316EFC311F5` | `GFX_report_event_ireland_report_flavour_family_09` | registration-only; maritime folklore boundary retained |
| EV-SRC-061 | `gfx/event_pictures/ireland/event_ev_src_061_report.dds` | 210×176 | `DC89D02A7B820F04` | `GFX_report_event_ireland_report_flavour_family_18` | registration-only; no unrelated flavour event rewired |

All ten rows have existing source objects and processed previews recorded in
the manifest. Four raw Military Archives LOP page rasters are preserved under
`assets/ireland_focus_tree/sourced/research_2026-08-01/event_news_user_approved_conditional/source_rasters/`.
Final DDS files are under the mod runtime `gfx/` tree; no runtime texture path
points into `assets/`.

## Static checks

- Every complete manifest row has an existing final DDS and processed output.
- Every complete manifest SHA-256 matches its final DDS; the EV-SRC-034 hash was
  corrected during this audit to match the runtime file.
- The ten promoted DDS headers match their manifest dimensions.
- The Ireland source-side GFX file has 128 texture references, zero missing
  texture files, zero duplicate sprite names, and no `assets/` runtime texture
  paths.
- Every complete manifest final DDS path is represented by a registered texture
  path in `interface/ireland_sourced_assets.gfx`.
- No consumer was fabricated for a promoted row merely to increase the image
  count. Existing consumer repairs and the registration-only boundary remain
  separately documented.

## Remaining asset blockers

The runtime event-picture inventory is 106 DDS files: 54 cleared or
user-approved conditional sourced packages, the separately manifested S-03
presidential-seal crop, and 51 generated images. The canonical 120-image budget
therefore remains open by fifteen blocked sourced event/news rows. The fifteen
blocked event rows, fifteen blocked symbol/document rows, and fifteen blocked
portrait rows remain in the machine manifest with their original provenance and
rights uncertainty. No duplicate, generic, generated, or fallback image was
used to close them.

Live HOI4 launch, in-game testing, fresh saves, and scenario playthroughs are
intentionally excluded from this audit by user direction.
