# Focus rewrite MCP retry — 2026-08-05

## Source state

The compact 157-focus source from the 2026-08-05 working tree was replaced
with the immediately preceding complete authored source. The restored source
contains 226 unique Ireland focuses, preserves the full reward and route
surfaces, and keeps the existing historical-AI gates. The Otherworld dominion
focus now has an explicit prerequisite edge to
`ireland_containment_protocol`; that dependency is no longer hidden only in
`available`.

Static source review reports one connected component with
`ireland_state_still_defined` as its only root, 257 prerequisite connectors,
no duplicate coordinates, and no coordinate overlaps. The longest raw source
connector spans eight horizontal units; this is recorded as a review item and
has not been called MCP-clean.

## MCP status

The target source was retried with `hoi4.focus_inspect`,
`hoi4.focus_render`, and `hoi4.focus_rewrite` after restoration, including a
direct authored-layout rewrite attempt. Each call in this desktop session
returned `Transport closed`, so no MCP rewrite or render was applied and no
MCP layout-completion claim is made. The three GUI windows were also retried
with `hoi4.gui_inspect`; an event-inspector health check and a
`resources/list` probe returned the same transport failure.

No fallback layout was substituted. The next valid focus pass is an authored
MCP inspect/render/rewrite against this 226-focus source once the server
transport is available.
