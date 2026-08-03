# Dillon and O'Duffy Route-Gate Repair Audit

Feature slug: `ireland_focus_tree`
Namespace: `slopx`
Audit date: 2026-08-01
Scope: non-live static and source review only

## Authority

This repair follows the canonical Dillon requirements in
`docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_2_constitutional_politics.md`,
Part 4's statecraft-and-war gate, and the statecraft matrix. Live HOI4 launch,
in-game testing, fresh saves, and scenario playthroughs are intentionally
excluded from this goal's completion gate by user direction.

## Dillon repairs

The Dillon route now has separate writers and gates for the route's actual
political progression:

- `slopx_ireland_advance_dillon_mandate` and
  `slopx_ireland_setback_dillon_mandate` write the 0-100 Intervention Mandate
  from Social Consent, Neutrality Integrity, British Leverage, and the P04
  platform/flavour decisions. The runtime no longer derives the mandate from
  the final material gate.
- The caucus threshold is a distinct 60-point gate. The named Dáil vote is a
  separate transition and cannot be created by the material/safeguard check.
  `slopx_ireland_dillon_named_vote_gate` preserves the political platform,
  majority, consent, leverage, and constitutional safeguards needed to put the
  question before the chamber, while allowing direct attack to bypass only the
  90-point mandate threshold. The named vote remains mandatory before war
  assent; only the final material war-entry trigger can complete the route.
- The final political gate requires the documented democratic Allied war,
  public dissent, mandate/readiness/consent, government majority, British
  leverage ceiling, dedicated P04 platform result, and non-radical route
  conditions. A direct attack may satisfy the mandate branch only; it never
  bypasses the named Dáil assent.
- Ten live safeguard records are projected into separate enforceable flags:
  home-defence reserve, military contribution, access, command, customs,
  finance, Northern policy, withdrawal, review, and the sovereignty base
  record. The final gate requires all ten. No focus reward grants the package
  directly.
- The native `slopx_ireland_national_settlement` balance-of-power range
  `slopx_ireland_armed_dual_authority_range` is a live constitutional-crisis
  boundary and blocks the Dillon gate while active.
- Daily and monthly Ireland hooks refresh the route records and crisis
  boundary. Closing the route clears its detailed enforceable safeguard flags
  and stale named-vote state on the next scoped refresh.

## O'Duffy repairs

`slopx_ireland_oduffy_personal_command` now has a dated bypass on and after
1944-11-30 that records expiry and clears its readiness flag. The matching AI
plan aborts on and after the same date or on normal route cleanup, so the dated
personal-command branch cannot remain as a reachable dead end after expiry.

## Static evidence

- Focus file brace balance: 1168/1168.
- Runtime file brace balance: 9815/9815.
- Dillon helper file brace balance: 8/8.
- Trigger file brace balance: 1762/1762.
- Main and flavour event files: 9374/9374 and 10379/10379.
- AI strategy plans: 214/214; on-actions: 17/17.
- Unsupported `<=`/`>=` operators in touched script files: 0.
- Direct Dillon safeguard grants remaining in focus rewards: 0.
- Dillon mandate writers: three variable writes, confined to the advance and
  setback helpers.
- Direct writes to `slopx_ireland_dillon_vote_passed`: one named Dáil-vote
  option in `slopx_ireland_events.1840`; the runtime no longer synthesizes
  assent from an invasion flag or material gate.
- Decision/mission structural counts remain 13 categories, 140 actions, and
  54 unique missions after the M2 merge.

## Remaining blockers

This repair does not resolve the separate source-clearance and visual-budget
blockers recorded by the completion audit. The current 169-row manifest has
124 complete rows and 45 blocked rows; the blocked set is fifteen portraits,
fifteen symbol/document packages, and fifteen sourced event/news packages.
The whole Ireland goal therefore remains incomplete until those canonical asset,
route, AI, achievement, and audit requirements are resolved. No live-game
validation is claimed.
