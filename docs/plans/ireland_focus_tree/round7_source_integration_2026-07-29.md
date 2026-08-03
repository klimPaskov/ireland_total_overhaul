# Ireland round-seven source integration

Date: 2026-07-29
Feature: `ireland_focus_tree`

## Integrated dispositions

The three bounded source-research passes are preserved in:

- `docs/plans/ireland_focus_tree/assets/source_research_handoffs/blocked_portraits_round7_2026-07-29.md`
- `docs/plans/ireland_focus_tree/assets/source_research_handoffs/blocked_symbols_round7_2026-07-29.md`
- `docs/plans/ireland_focus_tree/assets/source_research_handoffs/blocked_event_news_round7_2026-07-29.md`

The authoritative manifest now records:

| Family | Complete | Needs review | Blocked |
| --- | ---: | ---: | ---: |
| Portraits | 11 | 34 | 15 |
| Symbols/documents | 8 | 17 | 15 |
| Event/news | 29 | 13 | 27 |
| Total | 48 | 64 | 57 |

Clearance totals are C1/C2/C3/C4 = 35/26/82/26. Source-tier totals are
T1..T11 = 45/18/27/19/8/9/25/9/7/0/2.

P-33 John Hayes advances to C3 review on an exact named circa-1940s portrait.
EV-SRC-055 remains a rights-only C3 review record because the exact legal text
is available only in a modern eISB presentation. S-13, S-22, S-25, S-29,
S-31, and S-37 advance to C3 review with their exact conditions retained.

S-19 is the sole new C4 package. The selected object is the exact
public-domain 1903 *An Claidheamh Soluis* publication. It is explicitly not
identified as the separately controlled NLI 1915 handbill.

## Runtime placement

Only S-19 is promoted from the round-seven staging packages:

- DDS: `gfx/interface/ireland/sourced/symbol_document_s_19.dds`
- Sprite: `GFX_ireland_symbol_document_s_19`
- Registration: `interface/slopx_ireland_sourced_assets.gfx`
- SHA-256: `63f1827f2d651e3b54103db32f3bbfbf331be8ba56e1f2df75fbf5dfd5cd04a4`
- Dimensions: 397x153

Every C3 symbol DDS remains under the temporary round-seven `assets/` package.
No blocked or review-gated round-seven portrait, symbol, or event/news asset is
registered in runtime by this integration.

## Portrait-source preservation

Exact portrait source bytes remain under `docs/portraits/`. The round-seven
directory adds the John Hayes source image and Commons record plus the exact
Tomás Ó Dochartaigh 1944 campaign-poster source and its SHA-256 inventories.
The archive contains 213 files.

A byte-level comparison confirms that all 57 portrait identities with a
current manifest or route-extension source object have at least one
byte-identical archived copy under `docs/portraits/`. The four canonical rows
without any exact source object remain explicit and are not substituted.

## Verification

- The 169-row manifest parses with unique IDs and totals 48/64/57.
- All 48 complete rows have existing final DDS files whose recorded hashes
  match.
- Every blocked row retains `final_dds_path = not_created`.
- The 48-entry symbol round-seven hash inventory, three-entry portrait-source
  inventory, and 69-entry event/news inventory match current file sizes and
  SHA-256 values.
- All nine Ireland `.gfx` files resolve every texture path, and none points
  into `assets/`.
- The S-19 runtime DDS decodes from its header as 397x153 and matches its
  manifest hash.
- Runtime inventory is 857 DDS files total / 856 Ireland-owned. The established
  Ireland registration metric is 1,085 texture references and 325 unique
  sprite names.

HOI4 was not launched. Live testing is excluded from the completion gate by
user direction.

## Remaining blockers

The 64 review-gated and 57 blocked rows remain completion blockers. In
particular, seven review-gated portrait DDS files are still consumed by current
route-character definitions. No approval is inferred from source recovery or
from a staging DDS.
