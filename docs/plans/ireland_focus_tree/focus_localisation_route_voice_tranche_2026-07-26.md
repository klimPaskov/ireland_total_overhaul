# Ireland focus localisation route-voice tranche — 2026-07-26

This tranche replaces the mechanically templated focus descriptions in the Ireland tree with authored route-specific prose. It changes no focus IDs, prerequisites, rewards, icons, route gates, or counts.

## Scope

The edited surface is `localisation/english/slopx_ireland_l_english.yml`, covering the 216 national-focus title and description pairs used by `common/national_focus/slopx_ireland_focus_tree.txt`.

The revised descriptions distinguish the shared opening, constitutional and electoral routes, De Valera, Lemass, Fine Gael/Cosgrave, Mulcahy, Costello, Dillon, Norton, Clann, vocational politics, serious culture, Provision, Readiness, active neutrality, Northern policy, recovery, IRA, Republican Congress, O'Duffy, clerical and producer politics, dated Ailtirí, High Kingship, Five Provinces, Otherworld, and convergence. They describe the actual institutional or material trade-off of each focus instead of repeating a generic settlement sentence.

## Static evidence

- The focus source still contains 216 national focuses; the root `focus_tree` identifier is excluded from the focus-node count.
- Every focus has its title and `_desc` key; the expected 432 focus keys have 0 missing.
- A targeted sweep of the 216 focus descriptions finds 0 remaining instances of the retired generic templates (`part of a settlement that can be defended in public`, `before officials who can record its cost and limits`, and the route-wide repeated system boilerplates).
- The localisation file remains UTF-8 with BOM.
- Action, mission, event, GUI, and achievement localisation identifiers were not renamed by this tranche.

## Boundaries

This is a player-facing text improvement and does not prove parser loading, line wrapping, focus-tree render readability, dynamic tooltip evaluation, or hidden-content concealment. Those remain part of the live engine/reference and scenario validation programme. Source clearance and the unresolved Radical/Underground mission-capacity contradiction are also unaffected.
