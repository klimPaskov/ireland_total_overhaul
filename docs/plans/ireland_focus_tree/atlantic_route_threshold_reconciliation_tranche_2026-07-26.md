# Ireland Atlantic route threshold reconciliation — 2026-07-26

Feature slug: `ireland_focus_tree`

## Scope

The durable `ireland_atlantic_route` writer in `common/scripted_effects/ireland_runtime.txt` now follows the late-game Atlantic defence requirements instead of treating the route as formed at the old 35/35 readiness point.

## Required route evidence

The route writer now requires:

- a completed Atlantic charter and regional-defence proposal;
- a fully ratified regional charter with a valid two-channel partner pair;
- a full member-contribution schedule;
- a common threat through war, invasion danger, or an active neutrality incident;
- National Provision at least 65 and National Readiness at least 75;
- Maritime Access and Transport Serviceability at least 50;
- Warning, Maritime Protection, Command, and Intelligence each at least 45;
- no recorded sponsor-dependence or foreign-access failure.

The shared `regional_defence_league_*` constants own the common 65/75 and 45-point floors. The two Atlantic Provision floors use dedicated constants because the route map separately requires Maritime Access and Transport Serviceability at least 50.

## Boundaries

The route writer creates no faction, subject, territory, core, unit, factory, equipment, fuel, shipping, recognition, alignment, administration, office, or passive Political Power. It only records route eligibility after the authored actions, missions, partners, threat, and capability state exist.

Live route formation, partner invalidation, contribution failure, foreign reaction, AI transition, and cleanup scenarios remain not-run; no HOI4 process was launched.
