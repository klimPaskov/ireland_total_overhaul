# Ireland asset budget and runtime placement audit

Feature slug: `ireland_focus_tree`

Audit date: 2026-07-26

This is a static reconciliation of the canonical asset ledger against the
current runtime tree. It does not grant source clearance, replace historical
material, or claim live engine validation.

## Runtime counts

| Surface | Canonical budget | Current runtime observation | Result |
| --- | ---: | ---: | --- |
| focus goal icons | 216 | 216 DDS under `gfx/interface/goals/ireland/` | exact |
| focus shine and masks | 216 / 432 mask references | 216 shine entries and paired mask references | exact by static registration |
| decision categories | 13 | 13 DDS under `gfx/interface/decisions/categories/ireland/` | exact |
| decision actions | 70 | 70 DDS under `gfx/interface/decisions/ireland/actions/` | exact |
| mission families | 54 | 54 DDS under `gfx/interface/decisions/ireland/missions/` | exact |
| persistent spirit states | 63 | 63 DDS under `gfx/interface/ideas/ireland/spirits/` | exact |
| temporary overlays | 27 | 27 DDS under `gfx/interface/ireland/temporary_overlays/` | exact |
| law family icons | 51 | 51 DDS under `gfx/interface/ideas/ireland/laws/` | exact |
| mechanic and value icons | 45 | 45 DDS under `gfx/interface/ireland/mechanic_ledger/` | exact |
| achievement states | 96 | 96 named `ireland_*` DDS (32 concepts x 3 states) | exact for registered package |
| scripted GUI surfaces | 3 | conditions, northern, and evidence surfaces are registered | exact by source registration |
| animations | 7 | seven source-frame sets, sheets, previews, and runtime static fallbacks | exact by static inventory |

The `gfx/` runtime tree is the only final texture location. Source atlases,
processed previews, contact sheets, manifests, and review material remain under
the temporary `assets/ireland_focus_tree/` tree. No Ireland-owned runtime GFX
registration points into `assets/`.

## Source clearance boundary

The source manifest contains 169 historical source entries. Its current status
totals are 40 complete, 28 needing user review, and 101 blocked. The family
breakdown relevant to final historical material is:

| Family | Complete | User review | Blocked |
| --- | ---: | ---: | ---: |
| real-person portraits | 10 | 28 | 22 |
| event/news source rows | 26 | 0 | 43 |
| symbol/document rows | 4 | 0 | 36 |

The runtime contains 78 Ireland event/news DDS files: the 51 generated
alternate/symbolic/impossible images, the 26 cleared source images, and the
explicit Constitution/seal source aliases. The remaining canonical historical
event/news rows are not promoted while their clearance remains unresolved.
Likewise, runtime leader textures include the 14 generated collective portraits
and source-side real-person candidates, but only the nine complete portrait
rows are clearance-complete. The 28 review rows are not evidence of clearance
and must not be treated as final source approval.

The canonical ledger still requires 120 total event/news image allocations and
60 sourced real-person portraits. Completing those totals requires the missing
source permissions or user decisions; generated historical substitutes are not
permitted.

## Known inventory cleanup note

The runtime achievement directory also contains 96 unreferenced legacy files
named `achievement_ireland_001` through `achievement_ireland_032`, each with
three states. They are not referenced by the current achievement GFX package;
the exact 32-achievement package is the 96 named `ireland_*` files. They
are recorded here for deliberate cleanup rather than being treated as part of
the canonical budget.

## Open validation gates

- historical source clearance and per-item credit/license review remain open;
- local engine-reference checks for every GFX, GUI, and animation surface remain
  to be run;
- live focus rendering and runtime asset loading remain unverified because the
  user explicitly requested that HOI4 not be launched;
- the canonical Radical/Underground two-slot mission wording still conflicts
  with the fixed 54-row mission inventory and requires a design decision.
