# Ireland AI route-selection repair — 2026-08-02

## Scope

This audit records the source repair for non-historical Ireland AI opening
selection. It covers the pre-commit profile selector and the focus-plan
handoff; it does not claim live or save-game execution.

## Finding and repair

The prior initialization selected only one of eight constitutional base
profiles. Radical and concealed route plans existed, but no initial AI intent
could select their route-family plan before a route flag had been committed.
The route synchronizer therefore had no source-level queue for the IRA,
Republican Congress, O'Duffy, clerical/producer, serious-culture, High King,
Five Provinces, Otherworld, or rare Ailtirí opening families.

The initialization effect now keeps the historical branch fixed to de Valera,
keeps the existing constitutional base distribution, and adds a separate
non-historical opening-intent draw. It can set only preference flags for the
eight additional route families, plus a permission-gated rare Ailtirí intent.
The ordered route synchronizer maps those flags to the existing generic
profile flags and the existing three route-spirit families. It refuses to use
them after `ireland_route_committed`, so route commitment remains owned
by the authored focus gateways.

The corresponding route-family focus plans are enabled by their generic
pre-commit profile and now queue the necessary authored readiness/culture
focuses before their opener where those prerequisites are known. IRA,
Congress, O'Duffy, clerical/producer, Ailtirí, High King, Five Provinces, and
Otherworld continue to require their original flags, dates, evidence, material
conditions, hidden-content permissions, and mutually-exclusive focus gates.
No route flag, core, territory, equipment, unit, industry, or political-power
grant was added by this repair.

## Static evidence

- `common/scripted_effects/ireland_effects.txt` contains the existing
  historical/constitutional selector plus the non-historical route-intent
  draw and permission-gated Ailtirí draw.
- `common/scripted_effects/ireland_runtime.txt` maps all nine new intent
  flags to existing profile flags only while the route is uncommitted; the
  H/P/A boundary helper remains called after synchronization.
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` contains 31
  balanced Ireland focus plans, including the shared reactive plan and all
  route-family plans. Generic pre-commit family plans now recognize their
  corresponding profile selectors.
- A brace/source-reference sweep reports balanced touched script blocks;
  all new flag names occur in initialization, synchronization, and no other
  gameplay surface.

## Validation boundary

The user explicitly excluded running HOI4 and live in-game testing from the
completion gate. This document therefore records static source evidence only;
it does not convert the remaining canonical source-clearance blockers into
completed assets.
