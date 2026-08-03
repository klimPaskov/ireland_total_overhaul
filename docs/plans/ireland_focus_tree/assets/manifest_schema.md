# Ireland sourced-asset manifest schema

The machine-readable manifest is [source_manifest.json](source_manifest.json). It is source-side documentation only and does not wire gameplay or `.gfx` files.

## Required record fields

Each `entries[]` record contains:

| Field | Meaning |
| --- | --- |
| `id` | Stable entry ID: `P-01`–`P-60`, `S-01`–`S-40`, or `EV-SRC-001`–`EV-SRC-069`. |
| `family` | `portrait`, `symbol_document`, or `event_news`. |
| `canonical_name` | Exact canonical roster/package/allocation name. |
| `intended_use` | Planned in-game presentation role. |
| `source_mode` | `internet source image` for every sourced entry. |
| `source_tier` | Ledger tier 1–11. |
| `holding_institution` | Archive, library, government, museum, or identified holding source. |
| `catalogue_or_object_id` | Object/catalogue identifier, or an explicit `not established` lead marker. |
| `creator_or_author` | Creator/photographer/author or an explicit unknown marker. |
| `source_date_or_range` | Source date or estimated date range. |
| `source_url` | Provenance or source-page URL. A discovery page is never treated as permission. |
| `rights_holder` | Rights owner or explicit unresolved marker. |
| `license_or_permission` | Public-domain statement, licence, permission, or unresolved rights note. |
| `clearance_state` | Exactly one of `C0 discovered only`, `C1 provenance identified`, `C2 restricted or review pending`, `C3 cleared with conditions`, or `C4 cleared for unrestricted project use`. |
| `required_credit` | Credit that must travel with a C3/C4 asset. |
| `intended_crop` | Crop and target-role instruction. |
| `era_fit` | Era and authenticity note. |
| `rejected_alternatives` | Rejected modern, wrong-era, invented, unclear, or rights-unsafe alternatives. |
| `source_path` | Unmodified canonical source input. Complete portrait rows point directly to a flat `docs/portraits/P-xx_*` original; non-portrait source objects remain in temporary staging; blocked rows use `not_created`. |
| `source_research_path` / `source_research_sha256` | Optional blocked-row research lead and its hash. These fields never designate a portrait source input and never authorize processing or runtime use. |
| `source_staging_path` | Optional prior temporary staging location retained for provenance after a source input is promoted to the flat `docs/portraits/` root. |
| `processed_png_path` | Processed preview under `assets/ireland_focus_tree/sourced/processed_png/`, or `not_created`. |
| `final_dds_path` | Final runtime DDS under the mod's standard `gfx/` tree, or `not_created`. The assets tree is never the runtime final-DDS root. |
| `target_size` | Native target canvas, or an explicit not-assigned marker. |
| `dimensions` / `processed_mode` | Measured processed preview dimensions and mode when available. |
| `final_dds_sha256` | SHA-256 checksum of the final DDS when available. |
| `intended_sprite_name` | Proposed stable sprite name for the main agent. |
| `suggested_gfx_file` | Suggested target definition surface; no `.gfx` file is edited here. |
| `controlled_reuse` | Explicit reuse boundary. Reuse is never a blanket image substitute. |
| `status` | `complete`, `needs_user_review`, or `blocked` in this package. |
| `uncertainty` | Remaining source, identity, rights, semantic-fit, or crop uncertainty. |

S-01 may additionally carry `runtime_flag_paths`, `runtime_flag_source`,
`runtime_flag_processing`, and `runtime_flag_clearance_note`. These fields
record the source-derived HOI4 normal/medium/small TGA outputs without changing
the five-state source-clearance contract.

## Clearance rules

- C0–C2 entries are research leads and are unavailable for final DDS use.
- C3 entries may be used only with their exact credit and recorded conditions.
- C4 entries have verified public-domain or project-compatible permission for the intended use.
- Catalogue discovery, Wikimedia hosting, a search result, or a secondary biography does not itself establish image permission.

## Count contract

The manifest asserts exactly 60 portrait entries, 40 symbol/document packages, and 69 sourced event/news entries. The 69 entries are distributed as 18 historical-chain reports, 12 constitutional/social/institutional crisis reports, 13 sourced historical news entries, and 26 sourced flavour-family entries. They are not a claim that 69 image files have already cleared; unavailable records remain explicit.
