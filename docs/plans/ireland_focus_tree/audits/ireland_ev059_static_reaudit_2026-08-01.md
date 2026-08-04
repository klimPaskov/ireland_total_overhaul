# Ireland EV-SRC-059 static re-audit

Feature slug: `ireland_focus_tree`
Namespace: `ireland`
Date: 2026-08-01
Scope: source manifest, source bytes, processed PNG, runtime DDS, GFX registration, event consumer, and read-only engine checks

## Result

EV-SRC-059 is promoted to `complete` under conditional C3 clearance. The
exact UWM/AGSL Admiralty Chart 1765 source is registered and consumed by the
Cork ports flavour event. The runtime DDS is under the standard `gfx/` root;
`assets/` remains staging/evidence only.

Current manifest counts after promotion: 110 complete, 2 needs-user-review,
and 57 blocked. Event/news counts are 42 complete, 0 needs-user-review, and 27
blocked. Clearance totals are C1 35, C2 24, C3 83, and C4 27.

## Static checks

| Check | Result |
|---|---|
| Manifest row `EV-SRC-059` | `complete`; `C3 cleared with conditions` |
| Source path exists | exact UWM ContentDM JP2 exists; `8457x12404`, RGB |
| Source SHA-256 | `700EC148FEE9C00736818A4A21DEA600F00BAEE7894D6E9D82E08A7CDEF941E6` |
| Processed PNG | `210x176`, RGBA; SHA `BE38AD2B65832D1FF28F061563271782C338C575B6C12DBFDF9B5CFC363B5921` |
| Staging DDS | `210x176`; SHA `85E52AB22BEBEDE14E192BF2EF6BC825EE78E8E35C466EE77C5A395BF4881668` |
| Runtime DDS | `gfx/event_pictures/ireland/ireland_report_flavour_family_16.dds`; same SHA and dimensions |
| GFX registration | one `GFX_report_event_ireland_report_flavour_family_16` entry in `interface/ireland_sourced_assets.gfx` |
| Event consumer | `events/ireland_flavour_events.txt`, event `.683`, `f17_cork_ports` |
| Crosswalk | regenerated from the manifest after promotion; row reports registered GFX, runtime DDS, and consumer |

## Read-only event inspection

`mcp__hoi4_agent_tools__hoi4_event_inspect` was rerun in `lint` mode for the
`ireland_flavour_events` namespace after the picture wiring. The result
was `status: ok`, `EVENT_INSPECTED_PARTIAL`, with zero blocking diagnostics.
The linked report is the authoritative artifact
`event-lint-d83b61d809e9.json` (revision
`d83b61d809e971c35e6410a7bb3e7ca7c1c1cff1d6166c5e175359575fa5e347`). The
workspace-wide helper/lifecycle projection remained deferred by the MCP
large-workspace limit; that is recorded as an informational diagnostic, not
an EV-SRC-059 blocker.

## Clearance boundary

The source record’s title states publication at the Admiralty on 23 January
1891 and the survey is 1888; UWM also retains a 1898 catalogue/publication
date and `BA 1765 1898` item identifier. Both records are preserved in the
manifest and handoff. The exact chart is used as a pre-war Cork Harbour
geographic context for flavour family 16, not as the separate 1941 claim
record. The underlying UK government chart’s public-domain record and UWM’s
credit/no-permission guidance are retained as conditional C3 requirements.

No generic harbour image, AI reconstruction, facsimile, placeholder, fallback,
or unrelated event consumer was used. Live HOI4 launch and in-game testing were
not run, per user direction.
