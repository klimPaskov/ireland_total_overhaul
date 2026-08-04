# Ireland Naval Service implementation prompt

Implement `feature_spec.md` in the Ireland Total Overhaul repository. Use `AGENTS.md`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `hoi4-feature-assets`, and the local Paradox wiki/vanilla documentation before editing.

Implement the maritime focus branch, the phased decision family, the Irish OOB templates, division/ship name groups, Ireland intelligence agency, route-specific AI, localized tooltips, proper icons, report images, and documentation described by the spec. Preserve existing political, cultural, Northern, neutrality, and Otherworld systems. Use the `ireland` namespace everywhere.

The focus branch must be compact, visually readable, and connected to existing maritime/recovery mechanics. Use valid `search_filters`, not an invented `tags` token. Keep naval and army support branches compatible unless the route logic explicitly requires a lock. Historical focus mode must keep alternate-history route entry weights at zero.

Use real costs and bounded effects: convoys, fuel, manpower, equipment, dockyard time, navy experience, command power, and political power where appropriate. Prevent repeated free units, equipment, agency, factory, convoy, and patrol loops. Add all player-facing localization in UTF-8 with BOM, and use texticons for visible costs.

Before completion, run source audits for focus IDs/prerequisites/coordinates/filters, OOB syntax, ship names, agency GFX frame size, localization coverage, texture paths, latest error-log signatures, and remaining legacy namespace strings. Attempt the HOI4 MCP focus/GUI inspect and render calls; if the workspace remains unregistered, record that blocker and rely on the local structural audits without claiming a live MCP render.
