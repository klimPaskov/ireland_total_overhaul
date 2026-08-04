# Ireland focus-AI reconciliation — 2026-07-28

Feature slug: `ireland_focus_tree`

Namespace: `ireland`

## Scope

This read-only reconciliation revisits the historical audit finding that the
Ireland national-focus file had no route-aware AI. That finding predates the
current focus-plan and strategy registries. No focus count, route gate, or
runtime gameplay file was changed by this audit.

## Current evidence

The Ireland focus source contains 216 authored focus blocks. The surrounding
`focus_tree` wrapper is excluded from that count. The route-AI layer contains
31 `IRE_ireland_*` focus plans:

- one historical opening plan;
- one shared route-reactive plan;
- 22 route and route-support plans for the durable political, constitutional,
  cultural, security, and conclusion families; and
- seven composite/recovery plans for Congress, O'Duffy, clerical/producer,
  High Kingship, Five Provinces, Otherworld, and convergence states.

Every focus named by `ai_national_focuses` or `focus_factors` resolves to an
authored Ireland focus ID. The 17 visible route gateways are all present in at
least one route-specific or route-reactive plan. Route plans are enabled by
their durable route/profile flags and abort on `ireland_route_cleanup`,
so a completed route does not leave obsolete focus priorities active.

The strategy registry contains exactly 40 Ireland blocks. Its source roster is
30 durable profiles plus 10 temporary overlays. Profile strategies remain
responsible for diplomacy, construction, research, war posture, and route
validity, while focus plans own focus selection and `focus_factors` priority.
This separation mirrors the installed vanilla `ai_strategy_plans` precedent.

The single node-level `ai_will_do` in the focus file belongs to the concealed
Ailtirí gateway. It is intentionally stricter than ordinary plan weighting:
the AI cannot select that hidden route unless the relevant game-rule or rare-AI
permission is present. Ordinary routes use plan-level `focus_factors` so their
weights remain attached to the active profile instead of being duplicated in
216 focus blocks.

## Disposition

The old “zero focus AI” finding is superseded by this source evidence. No
redundant per-focus weighting pass is warranted: it would duplicate the
existing 31-plan priority layer and could make a concealed route visible to the
AI without its explicit permission gate.

This does not prove live focus selection, probability balance, or engine
loading. Those checks still require the local focus MCP workspace or a live
HOI4 validation run and remain open under the project completion gate.
