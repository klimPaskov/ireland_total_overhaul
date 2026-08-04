# Ireland Focus Layout Inspection — 2026-07-28

Feature slug: `ireland_focus_tree`
Tree: `ireland_focus_tree`
Source: `common/national_focus/ireland_focus_tree.txt`
Workspace: `mod_ireland_total_overhaul_65a6b5f140a7`
Mode: national focus inspection and render; HOI4 was not launched.

## Final authored-tree inspection

The offline `hoi4.focus_inspect` pass resolved the authored Ireland tree with:

| Measure | Result |
| --- | ---: |
| Focus blocks | 216 |
| Resolved focus titles | 216 |
| Connectors | 197 |
| Ireland-local crossing diagnostics | 0 |
| Ireland-local node-intersection diagnostics | 0 |
| Ireland-local long-connector diagnostics | 0 |
| Ireland-tree diagnostic count | 0 |

The source keeps the port-and-coast audit and presidential settlement as hard
`available` gates while the authored coordinates avoid long cross-branch
connectors. The layout-only changes were:

- moved `ireland_replacement_charter` left;
- moved `ireland_treaty_port_transfer` left;
- moved `ireland_sovereignty_mandate` and
  `ireland_presidential_settlement` inward;
- moved `ireland_active_neutrality` left;
- retained the route gates in `available` rather than relying on a long
  visible connector.

No focus identifier, title, icon, reward, count, or route condition was
removed by this layout tranche.

## Current-source recheck — 2026-07-29

A fresh offline inspection of the current source used workspace
`mod_ireland_total_overhaul_65a6b5f140a7` with the authored/default spacing contract. It
again resolved 216 focuses and 216 titles, with 197 connectors, zero
Ireland-local crossings, zero node intersections, zero long connectors, and
zero Ireland-tree diagnostics.

The aggregate validation remains false only because the inspector also loads
the vanilla continuous-focus palette and reports fourteen missing vanilla
sprite definitions outside the Ireland tree. The Ireland tree's own
`diagnosticCount` is zero.

Current artifact:
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/bf271dd014cceef77ddba32cb9376ec5f253db3a45ddbb58a3a974d114555e8f/c6e6ae6b1317a2d0499231b40833647da19c5fc0fe27fa204bd4f2e8f52c2548/focus-inspect.27198cb55408735c.json`.

## Render artifact

The matching `hoi4.focus_render` pass succeeded and produced the following
offline artifacts:

- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/82002eee60460d236ee6970dd61ffc5ce7daa98a99aacef032d27559d5962b11/4731cf2ec88aad0f3958a17b6bf06754f016c6780c61aa3736e44742191ad1eb/ireland_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/4bd2dade3ab7b5567fb29102749854d459e546157c00528f3d2fac7682aa9619/86318dc8fc80407d9fc63d33c76a283585c1aa6bb47ad41a013bf79bb9508286/ireland_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/7ee74f7e8dc78f5985094d1a746e758338dc02343f68f8156fbc8c81daf3d806/1e22d5b2367174bad1c10a09bf31f2ba878e66fe84f123e57b8420ecd343e4ef/ireland_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/5625628ce190a21d23092c072d63bd3c73010b8bd97273faa15d7be8eae44f58/831e1a4908cc981b9b30c10d1a1f16672ecb32148955bd41ad41a9b5dc45177bda908/ireland_focus_tree.focus.source-map.json`

The render reported width `79504`, height `5920`, and layout hash
`1cfbb1f7ca61d5fe3683561dd504dd6ec82d606112dc036ea314f09e64339847`.

## Decoded runtime-sprite raster

The offline `hoi4.focus_raster` pass decoded the runtime `.gfx` references and
produced a 14288 by 1290 PNG raster with the same layout hash. Its Ireland
focus source inventory includes the promoted DDS files under
`gfx/interface/goals/ireland/`, rather than the temporary `assets/`
package. The raster artifacts are:

- PNG: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/b227654b510a3d7a8352709b547a5fe25a7960e9565f7068d30d288b6e88072a/b6ffceee119afc397dbc7b2f52064d92396676954fc664b16d4b1d2fda577d2b/ireland_focus_tree.focus.png`
- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/d051b4ed07f83da85e9c5f022137f47762404bb521eee5dc37b0f33183eef4c3/d81bab9f3a2b58f18eba13991baabbae3a55a91605ff62298ccb4f14dda3c1c8/ireland_focus_tree.focus.html`

The raster response had the same fourteen unrelated vanilla continuous-focus
diagnostics as the structural render. No Ireland-local missing-sprite
diagnostic was reported.

The MCP response still reports `validation.passed = false` at the global
workspace level because fourteen unrelated vanilla continuous-focus entries
have missing sprites or localisation. Those diagnostics do not belong to the
Ireland tree; the Ireland-tree diagnostic count is zero. Full engine loading,
live save scenarios, AI focus selection, and prerequisite/bypass behaviour
remain not-run.
