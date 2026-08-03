# Ireland EV-SRC-055 static re-audit

Feature slug: `ireland_focus_tree`
Namespace: `slopx`
Date: 2026-08-01
Scope: source manifest, runtime DDS, GFX registration, event consumer, and read-only MCP event inspection

## Result

EV-SRC-055 is complete under conditional C3 clearance. The exact-period
Houses of the Oireachtas scan of the Constitution (Consequential Provisions)
Bill 1937, Bill No. 41a, as passed by Dáil Éireann, is processed to the
canonical 210×176 report surface and promoted to the standard runtime `gfx/`
tree. The modern eISB Act page remains supporting legal evidence and is not
used as the visual source.

| Check | Result |
| --- | --- |
| Manifest entries | 169 total; 109 complete, 3 review, 57 blocked |
| EV-SRC-055 | `complete`; `C3 cleared with conditions` |
| Processed PNG | 210×176 RGBA; manifest hash matches local output |
| Runtime DDS | valid DDS header; 210×176; manifest/runtime SHA-256 match `EBAB386050E1D0FC5CAF49133EE59FD3B5930224E10F39966AA16B3EA9F2A63E` |
| GFX registration | exactly one `GFX_report_event_ireland_report_flavour_family_12` registration in `interface/slopx_ireland_sourced_assets.gfx` |
| Consumer | exactly one `picture = GFX_report_event_ireland_report_flavour_family_12` reference in H01 event `slopx_ireland_events.102` |
| Crosswalk | rebuilt from the current manifest and GFX sources; EV-SRC-055 row reports complete C3 coverage |

## MCP evidence

Read-only `hoi4_event_inspect` was run against workspace
`mod_ireland_total_overhaul_65a6b5f140a7` with `mode = lint`, the
`slopx_ireland_events` namespace selector, `maxNodes = 260`, `maxEdges = 520`,
`maxDepth = 8`, and `expandHelpers = false`. The tool returned
`EVENT_INSPECTED_PARTIAL` with status `ok`, zero blocking diagnostics, and a
linked authoritative event-lint artifact. Its aggregate validation remained
false because the large workspace deferred workspace-wide helper/lifecycle
projections; that is a tool-scope limitation, not an EV-SRC-055 diagnostic.

No live HOI4 launch, in-game test, save test, or scenario playthrough was run.
