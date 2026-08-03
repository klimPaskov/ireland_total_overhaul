# Ireland named persistent-spirit failure forms

Feature slug: `ireland_focus_tree`
Namespace: `slopx`
Date: 2026-07-29

## Outcome

The Ireland runtime still exposes exactly three persistent spirit families:
Governing Order, Organised Society, and Security and External Position. Route
selection installs one exclusive three-spirit profile. A second ordered pass
may replace at most one member of each family with a named failure form; it
cannot stack another persistent spirit or remove an unaffected family.

Thirteen named failure forms distinguish the route and system failures that
were previously compressed into six generic ideas:

- Governing Order: Clerical Veto, the Captive Crown, and Rival Provincial
  Sovereignties.
- Organised Society: Emergency Shortage Order, Captured Estates, Sectarian
  Administration, and Forced Mobilisation.
- Security and External Position: Neutrality Breakdown, Client State, Occupied
  Order, Fragmented Armed Wings, Uncommanded Provincial Guards, and Compact
  Breach.

The six generic forms remain registered for their generic failure records.
Every named form has distinct player-facing localisation and concrete
modifiers. No form grants political power, material, industry, units, fuel,
shipping, administration, alignment, offices, recognition, territory, claims,
or cores.

## Runtime ordering

The governing chain prioritises a captured crown, rival Five Provinces
sovereignties, and clerical vetoes before generic collapse or corruption. The
society chain prioritises captured estates, sectarian administration, forced
mobilisation, and provision breakdown before generic service or patronage
failure. The security chain prioritises compact breach, occupation, the
Five-Provinces-specific command failure, general armed-wing fragmentation,
foreign client dependence, and Neutrality Integrity below 40 before generic
disarmament or crisis.

Each branch calls one of three family-local cleanup effects before installing
its replacement. The cleanup registries include opening, route-profile,
subprofile, named-failure, and generic-failure forms, so stale ideas cannot
survive a route transition.

## Art and registration

This tranche adds no runtime image and creates no asset in `assets/`. The named
forms reuse the six already approved failure-family sprite registrations in
`interface/slopx_ireland_secondary_assets.gfx`. All final textures remain under
`gfx/interface/ideas/slopx_ireland/spirits/`; the exact runtime spirit-art
budget remains 63 DDS files.

## Files

- `common/ideas/slopx_ireland_spirits.txt`
- `common/script_constants/slopx_ireland_constants.txt`
- `common/scripted_effects/slopx_ireland_runtime.txt`
- `localisation/english/slopx_ireland_l_english.yml`
- `docs/slopx_dynamic_effects.md`

## Validation boundary

Static checks cover the 13 idea definitions, 26 localisation keys, family
membership of every cleanup registry, exclusive `if`/`else_if` precedence,
the shared Neutrality Integrity threshold, runtime texture paths, and the
unchanged 63-file spirit-art budget. HOI4 launch and live playthrough testing
are excluded from the goal by user direction.
