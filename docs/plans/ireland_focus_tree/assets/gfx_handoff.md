# Ireland focus-tree GUI asset handoff

Status: complete for asset production; the main-agent source-side `.gfx` registration now covers all 34 complete manifest records while review-gated candidates remain explicitly marked.

Scope reconciliation (2026-07-22): the original asset-worker boundary did not include `.gfx` edits; the main implementation has since registered the cleared source package in `interface/ireland_sourced_assets.gfx`. Live GUI validation and source-clearance decisions remain open.

Runtime portrait reconciliation (2026-07-22): the unrestricted William Norton package is applied to the vanilla `IRE_william_norton` country-leader character when the Norton parliamentary route activates, through `set_portraits` in `common/scripted_effects/ireland_runtime.txt`. The other conditional source portraits remain registered for review-gated use and are not silently treated as unrestricted.

Historical source integration (2026-07-22): S-02's official Government of Ireland harp reference is registered as `GFX_ireland_official_state_harp_reference` in `interface/ireland_sourced_assets.gfx`; the older Dalway-harp candidate remains research-only. S-03's 1937 Official Seal of the President of Ireland is registered as `GFX_report_event_ireland_report_presidential_seal` and consumed by `ireland_events.106`, the presidential-dissolution case. Both packages are C4 in the authoritative source manifest with their source URLs, permission records, processed derivatives, DDS hashes, and attribution retained.

Source mode: generated fictional/institutional interface art via Codex built-in `image_gen`. The art contains no real-person likenesses, historical documents, real flags, attested symbols, readable generated text, watermarks, or modern UI branding.

Runtime registrations are in `interface/ireland_gui_assets.gfx`; this handoff records the shipped `gfx/` paths while source, processed, and static-fallback evidence remains in `assets/`.

## Runtime placement

Final DDS files are shipped under the mod's `gfx/` tree. `assets/ireland_focus_tree/generated/gui/` is staging and provenance material only; it is not a runtime texture root.

Each close action sets its surface's one-day `*_panel_closed` flag and dirties the scripted GUI, so the close control hides the active panel while the normal decision-category surface can reopen it after the timed flag expires.

## Final sprites

| Sprite name | Surface/use | Final DDS | Dimensions | Static fallback DDS |
| --- | --- | --- | --- | --- |
| `GFX_ireland_gui_conditions_background` | National Conditions Panel background | `gfx/interface/ireland/gui/conditions/background.dds` | `920x704` | `assets/ireland_focus_tree/generated/gui/conditions/static_fallback/conditions_background_static_fallback.dds` |
| `GFX_ireland_gui_northern_background` | Northern Settlement Ledger background | `gfx/interface/ireland/gui/northern/background.dds` | `920x704` | `assets/ireland_focus_tree/generated/gui/northern/static_fallback/northern_background_static_fallback.dds` |
| `GFX_ireland_gui_evidence_background` | Concealed Evidence Ledger background | `gfx/interface/ireland/gui/evidence/background.dds` | `920x704` | `assets/ireland_focus_tree/generated/gui/evidence/static_fallback/evidence_background_static_fallback.dds` |
| `GFX_ireland_gui_status_ready` | Shared approved/ready state | `gfx/interface/ireland/gui/shared/status_ready.dds` | `32x32` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/status_ready_static_fallback.dds` |
| `GFX_ireland_gui_status_locked` | Shared locked state | `gfx/interface/ireland/gui/shared/status_locked.dds` | `32x32` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/status_locked_static_fallback.dds` |
| `GFX_ireland_gui_status_warning` | Shared warning state | `gfx/interface/ireland/gui/shared/status_warning.dds` | `32x32` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/status_warning_static_fallback.dds` |
| `GFX_ireland_gui_status_critical` | Shared critical state | `gfx/interface/ireland/gui/shared/status_critical.dds` | `32x32` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/status_critical_static_fallback.dds` |
| `GFX_ireland_gui_value_row` | Shared value row | `gfx/interface/ireland/gui/shared/value_row.dds` | `420x30` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/value_row_static_fallback.dds` |
| `GFX_ireland_gui_compact_row` | Shared compact row | `gfx/interface/ireland/gui/shared/compact_row.dds` | `272x30` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/compact_row_static_fallback.dds` |
| `GFX_ireland_gui_review_button` | Shared review action plate | `gfx/interface/ireland/gui/shared/review_button.dds` | `280x38` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/review_button_static_fallback.dds` |
| `GFX_ireland_gui_close_button` | Shared close action plate | `gfx/interface/ireland/gui/shared/close_button.dds` | `44x38` | `assets/ireland_focus_tree/generated/gui/shared/static_fallback/close_button_static_fallback.dds` |

## Shared-reuse rule

The eight status/row/button sprites are one intentionally controlled-reused shared set consumed by all three surfaces. The family count remains three: Conditions, Northern Settlement, and Evidence. Per-item manifests record all three family uses and the reuse decision.

## Review aids and provenance

- `assets/ireland_focus_tree/generated/gui/conditions/contact_sheet.png`
- `assets/ireland_focus_tree/generated/gui/northern/contact_sheet.png`
- `assets/ireland_focus_tree/generated/gui/evidence/contact_sheet.png`
- `assets/ireland_focus_tree/generated/gui/shared/contact_sheet.png`
- `assets/ireland_focus_tree/generated/gui/manifest.json`
- Per-item manifests under `conditions/manifest/`, `northern/manifest/`, `evidence/manifest/`, and `shared/manifest/`
- Static fallback documentation under the package root and each family folder

## Remaining blockers

No generation or DDS-conversion blocker remains. Source-side `.gfx` registration is present; the remaining release work is live GUI/engine validation plus the manifest’s outstanding clearance decisions.

## Sourced Ireland event/news handoff

Suggested target surface: `interface/ireland_sourced_assets.gfx`. The table uses the manifest's stable sprite names with a `GFX_report_event_` or `GFX_news_event_` surface prefix. All listed DDS files are final and registered in the runtime `.gfx` surface.

| Slot | Proposed sprite name | Final DDS | Size | Clearance |
| --- | --- | --- | --- | --- |
| EV-SRC-002 | `GFX_report_event_ireland_report_historical_chain_report_02` | `gfx/event_pictures/ireland/event_ev_src_002_report.dds` | 210x176 | C3: Oireachtas Open Data / Irish Statute Book credit and licence condition |
| EV-SRC-003 | `GFX_report_event_ireland_report_historical_chain_report_03` | `gfx/event_pictures/ireland/event_ev_src_003_report.dds` | 210x176 | C3: legislation.gov.uk Open Government Licence attribution |
| EV-SRC-005 | `GFX_report_event_ireland_report_historical_chain_report_05` | `gfx/event_pictures/ireland/event_ev_src_005_report.dds` | 210x176 | C3: Open Parliament Licence attribution |
| EV-SRC-014 | `GFX_report_event_ireland_report_historical_chain_report_14` | `gfx/event_pictures/ireland/event_ev_src_014_report.dds` | 210x176 | C3: IWM credit/non-commercial condition |
| EV-SRC-019 | `GFX_report_event_ireland_report_constitutional_crisis_report_01` | `gfx/event_pictures/ireland/event_ev_src_019_report.dds` | 210x176 | C3: Oireachtas Open Data / Bill 41 credit and licence condition |
| EV-SRC-011 | `GFX_report_event_ireland_report_historical_chain_report_11` | `gfx/event_pictures/ireland/event_ev_src_011_report.dds` | 210x176 | C3: IWM credit/non-commercial condition |
| EV-SRC-012 | `GFX_report_event_ireland_report_historical_chain_report_12` | `gfx/event_pictures/ireland/event_ev_src_012_report.dds` | 210x176 | C3: IWM credit/non-commercial condition |
| EV-SRC-013 | `GFX_report_event_ireland_report_historical_chain_report_13` | `gfx/event_pictures/ireland/event_ev_src_013_report.dds` | 210x176 | C3: IWM credit/non-commercial condition |
| EV-SRC-015 | `GFX_report_event_ireland_report_historical_chain_report_15` | `gfx/event_pictures/ireland/event_ev_src_015_report.dds` | 210x176 | C4 |
| EV-SRC-017 | `GFX_report_event_ireland_report_historical_chain_report_17` | `gfx/event_pictures/ireland/event_ev_src_017_report.dds` | 210x176 | C4 |
| EV-SRC-018 | `GFX_report_event_ireland_report_historical_chain_report_18` | `gfx/event_pictures/ireland/event_ev_src_018_report.dds` | 210x176 | C3: source/archive credit and link |
| EV-SRC-029 | `GFX_report_event_ireland_report_constitutional_crisis_report_11` | `gfx/event_pictures/ireland/event_ev_src_029_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-030 | `GFX_report_event_ireland_report_constitutional_crisis_report_12` | `gfx/event_pictures/ireland/event_ev_src_030_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-031 | `GFX_news_event_ireland_news_historical_news_01` | `gfx/event_pictures/ireland/event_ev_src_031_news.dds` | 397x153 | C3: PRONI credit/copy-order condition |
| EV-SRC-033 | `GFX_news_event_ireland_news_historical_news_03` | `gfx/event_pictures/ireland/event_ev_src_033_news.dds` | 397x153 | C4 |
| EV-SRC-035 | `GFX_news_event_ireland_news_historical_news_05` | `gfx/event_pictures/ireland/event_ev_src_035_news.dds` | 397x153 | C4 |
| EV-SRC-047 | `GFX_report_event_ireland_report_flavour_family_04` | `gfx/event_pictures/ireland/event_ev_src_047_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-048 | `GFX_report_event_ireland_report_flavour_family_05` | `gfx/event_pictures/ireland/event_ev_src_048_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-049 | `GFX_report_event_ireland_report_flavour_family_06` | `gfx/event_pictures/ireland/event_ev_src_049_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-051 | `GFX_report_event_ireland_report_flavour_family_08` | `gfx/event_pictures/ireland/event_ev_src_051_report.dds` | 210x176 | C4 |
| EV-SRC-053 | `GFX_report_event_ireland_report_flavour_family_10` | `gfx/event_pictures/ireland/event_ev_src_053_report.dds` | 210x176 | C4 |
| EV-SRC-065 | `GFX_report_event_ireland_report_flavour_family_22` | `gfx/event_pictures/ireland/event_ev_src_065_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-066 | `GFX_report_event_ireland_report_flavour_family_23` | `gfx/event_pictures/ireland/event_ev_src_066_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-067 | `GFX_report_event_ireland_report_flavour_family_24` | `gfx/event_pictures/ireland/event_ev_src_067_report.dds` | 210x176 | C3: PRONI credit/copy-order condition |
| EV-SRC-069 | `GFX_report_event_ireland_report_flavour_family_26` | `gfx/event_pictures/ireland/event_ev_src_069_report.dds` | 210x176 | C4 |

Ready-to-copy definitions (place in the suggested event-picture `.gfx` surface):

```text
spriteType = {
	name = GFX_report_event_ireland_report_historical_chain_report_11
	texturefile = "gfx/event_pictures/ireland/event_ev_src_011_report.dds"
}

spriteType = {
	name = GFX_news_event_ireland_news_historical_news_01
	texturefile = "gfx/event_pictures/ireland/event_ev_src_031_news.dds"
}
```

The remaining 18 definitions follow the exact slot-to-path table above. The complete source records, credits, conditions, crop notes, and DDS SHA-256 values remain in `source_manifest.json`; no `.gfx` file was edited by this worker.
