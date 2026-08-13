# Focus Reward Contracts

## Purpose

Ireland focuses use route-specific decisions and missions, proof records,
institutional transitions, named projects, physical deliveries, and bounded
ledger changes. Every focus has its own completion tooltip. Backend flags and
recompute calls may support a reward, but they are never presented as the
reward itself.

## Contracts

- Constitutional and government focuses open a named parliamentary stage,
  record a mandate, commit a route, or hand control to a decision lifecycle.
- Provision and readiness focuses open named projects and recompute the
  corresponding ledger. Their project milestones also deliver factories,
  infrastructure, anti-air defence, rifles, support equipment, trucks, trains,
  or convoys where the focus represents that physical work.
- Foreign and Northern focuses open named channels, negotiations, or settlement
  proofs; they do not grant territory, cores, recognition, or alignment.
- Radical and hidden focuses record authority, evidence, or transition state
  and remain gated by their action and mission results.
- Route capstones open the public conclusion review and perform route-specific
  cleanup or institutional transition. They do not receive a universal bundle.
- The Marine Service sequence retains bespoke ships, facilities, experience,
  and ledger changes because those effects are the physical project itself.

## Physical delivery schedule

| Focus | Concrete delivery |
| --- | --- |
| `ireland_defence_estimates` | 250 rifles and 25 support equipment |
| `ireland_energy_board` | 500 fuel and one infrastructure level in controlled Connaught |
| `ireland_transport_priority` | 25 trucks and 2 trains |
| `ireland_maritime_reserve` | 5 convoys |
| `ireland_domestic_manufacturing` | one civilian factory and shared slot in an Irish core state |
| `ireland_emergency_stockpiles` | 300 rifles and 50 support equipment |
| `ireland_development_authority` | one infrastructure level in an Irish core state |
| `ireland_provision_conclusion` | one civilian factory and shared slot in an Irish core state |
| `ireland_readiness_command` | 200 rifles and 25 support equipment |
| `ireland_coastwatch` | one radar level in controlled Dublin |
| `ireland_air_warning` | one anti-air level in Dublin |
| `ireland_port_defence_project` | one anti-air level in controlled Munster |
| `ireland_maritime_protection` | 5 convoys |
| `ireland_professional_army` | 200 rifles and 25 support equipment |
| `ireland_interoperability` | 25 trucks and 25 support equipment |
| `ireland_emergency_mobilisation` | 300 rifles |
| `ireland_readiness_conclusion` | one military factory and shared slot in an Irish core state |
| `ireland_armed_neutrality` | 250 rifles and 25 support equipment |
| `ireland_arms_before_authority` | 250 rifles and 25 support equipment |
| `ireland_northern_question_in_arms` | 25 trucks |
| `ireland_ira_army_council` | 250 rifles and 25 support equipment |
| `ireland_congress_vanguard_cell` | 250 rifles |
| `ireland_oduffy_personal_command` | 250 rifles and 25 support equipment |
| `ireland_army_acceptance` | 25 trucks |
| `ireland_ailtiri_cell_network` | 250 rifles and 25 support equipment |
| `ireland_ceannaire_state` | 25 trucks |

These additions supplement the existing Marine Service facilities, radar,
coastal defences, convoys, equipment, agency, and research bonus. Amounts are
file-local tuning constants in the focus source because the affected equipment
and building fields use preprocessing constants rather than cross-file script
constant tokens.

The full current source has 32 focus IDs with direct material, construction, or
fuel effects. The table above documents the non-Marine additions; the Marine
sequence retains its trawler package, Cork naval base, coastal fortifications,
Cobh factory and dockyard, Lough Swilly radar, and Atlantic convoys.

## Capability and procedure density

Twenty-four focus IDs grant research, doctrine, agency, or event capabilities.
Ordinary bonuses use one 50% research use; doctrine grants use one 50% cost
reduction. Fifty-nine focus IDs also expose 60 native
`unlock_decision_tooltip` effects for 58 existing actions or missions, so the
player sees the playable procedure opened by the focus instead of only a
backend readiness flag.

## Visual assets

No visual asset is required for a shared reward profile because shared reward
profiles have been retired. Bespoke project effects use the focus icon and the
standard engine texticons for the concrete resources they affect.

## Future extension

When a focus gains a new effect, connect it to the named route, project, ledger,
decision, mission, idea, or review state. Do not reintroduce a generic bundle to
make an otherwise passive focus appear rewarding.
