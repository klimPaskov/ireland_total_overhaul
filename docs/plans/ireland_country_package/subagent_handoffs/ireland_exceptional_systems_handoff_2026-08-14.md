# Exceptional route systems handoff

## Changed gameplay surfaces

- `common/script_constants/ireland_exceptional_routes.txt`: canonical values,
  thresholds, cost tiers, durations, and AI bases.
- `common/scripted_triggers/ireland_exceptional_routes.txt`: conclusion,
  recovery, Fian, lawful-mandate, and convergence gates.
- `common/scripted_effects/ireland_exceptional_routes.txt`: initialization,
  cost payment, conclusion recognition, spirit/identity refresh, and cleanup.
- `common/scripted_effects/ireland_effects.txt`: ordinary route cleanup now
  clears exceptional active state.
- `common/scripted_effects/ireland_runtime.txt`: all eleven exceptional
  missions now occupy the existing global and category capacities; their
  critical crown, Rival Irelands, and convergence cases enter the existing
  reserved-slot calculation.
- `common/decisions/ireland_decisions.txt`: all 22 mapped action/mission ids
  in existing category containers.
- `events/ireland_exceptional_route_events.txt`: direct triggered-only events
  `ireland_events.438` through `.460`, each with a complete four-option
  nonhistorical AI pool. Every branch has a file-scoped base tier, a hard
  `ireland_profile_historical_de_valera` zero factor, a route gate, and its
  own ledger threshold modifier.
- Same-slot ideas, cosmetic definitions, scripted localisation, English
  localisation, helper documentation, and mechanic documentation.

## Focus integration contract

Every exceptional focus completion must call
`ireland_refresh_exceptional_route_state = yes`. Terminal focus ids are read by
`ireland_commit_exceptional_conclusion`; focus rewards need no duplicate
conclusion setters. Events 440–460 are direct and never dispatcher candidates.

## Lifecycle and exploit notes

- Missions: royal circuit 120, party-crown break 120, common compact 120,
  fifth seat 180, Rival Irelands prevention 120, Fian company 120, five sites
  180, broken compact 120, regional reconciliation 150, extraction 90, and
  convergence review 180 days.
- Cleanup retains patron, fabrication, breach, and conclusion history while
  clearing only active missions and temporary due-benefit state.
- No new effect grants core, claim, state, war goal, war, division, manpower,
  equipment, stockpile, or resource deposit.

## Validation evidence

- All 23 event ids `.438`–`.460` are unique and each has four option branches.
- Event viewer lint artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/e82f2e132348b73552aa59083c6ffa07354705f412bb6ee0f408627fa42a7f21/ff53170f1c0326b9ba3db8a51682c7a1524c1c79b964da1f4cbfbadf4183a72f/event-lint-e0d88ff43013.json`.
- Event `.440` option render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ccf832de8d833f0aa351806480e6ea15979bde8325c3616615d0bab467a4ead5/24005ea61a32d20b633d6d3f4d5f7e1991e3b3cad3a6fde99beeacc8880001d4/event-options-e0d88ff43013.json`.
- Event `.460` option render: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/8cc3896e3fc24b86ba8590b9f3562c5ae924154eb33b1258b2d0ce38942f0f8a/e68a2f863969df147bb715f8f742ef603af1350a1d4d73790e282c9b49945c63/event-options-e0d88ff43013.json`.
- Probability inspection classifies `ireland_events.438` as a complete,
  exactly supported four-option `event_option_ai_chance` pool:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/fe48f5e05d3fb0b1db7836e97112314c103956101a9014bb3224b5f3e351dc00/413af27eab2bd5aab351cb1e5bb1cee3d122abf8872d48bf40390b1fb53a498a/probability-inspect-14ff275e14bc.json`.
- Static checks covered definition counts, option localisation, braces, BOM, and
  existing GFX references.

## Final tuning and identity hardening

- `common/script_constants/ireland_exceptional_routes.txt` is the exceptional
  tuning source for conclusion/action/mission gates, cost-anchor thresholds,
  result deltas, AI bases and modifiers, and cosmetic-spirit modifier values.
  Static resolution found 114 unique `constant:ireland_exceptional_routes.*`
  consumers and no undefined constant reference.
- Native decision costs and durations, native resource triggers, idea modifier
  fields, and event-option AI chance fields retain documented file-local
  `@IRELAND_EXCEPTIONAL_*` substitution only. Each defining file records the
  exact matching global constant and value. The six native decision costs remain
  five `@IRELAND_EXCEPTIONAL_COST_WATCH_PP` (20 PP) and one
  `@IRELAND_EXCEPTIONAL_COST_SEVERE_PP` (25 PP); no native decision `cost`
  uses an unsupported `constant:` token.
- All direct event outcome deltas use centralized constants. The event package
  still has 23 events, 92 options, 92 AI pools, 92 historical-profile blocks,
  92 route-match modifiers, and 92 branch-ledger modifiers.
- `ireland_conclusion_high_king_captive_throne` now selects
  `IRE_IRELAND_CAPTIVE_THRONE` before the mutually exclusive convergence
  cosmetic branches. All ten exceptional cosmetic tags have one runtime
  consumer and base/ADJ/DEF English localisation.

### Hardening validation

- Targeted exceptional action and mission scans found no remaining raw tuning
  threshold, gate, delta, native cost, duration, or AI weight. The prior direct
  decision checks such as `has_political_power > 19` resolve through exact
  file-local macros synchronized to the constant source.
- Static macro audit found no undefined exceptional macro in decisions,
  triggers, ideas, or the direct event file. Event effects have no raw numeric
  `add_to_variable` delta.

## Remaining parent-owned integration

- Focus rewards must use the refresh contract and mapped direct events. The
  parent focus patch remains the source of those call sites.
- The asset team must supply and wire the nine planned report-event GFX ids for
  captive throne, palace break, Empty Chair, Rival Irelands, Tuatha courts,
  Sealed State, Crown and Provinces, High King of Two Irelands, and Five Courts,
  plus normal/medium/small files for the ten cosmetic tags. No placeholder or
  fallback art was introduced here.
- Re-run event comparison and full decision/focus audit after focus and asset
  work is integrated.
