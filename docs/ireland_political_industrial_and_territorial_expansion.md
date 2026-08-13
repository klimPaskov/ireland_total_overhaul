# Ireland political, industrial, and territorial expansion

## Overview

The National Settlement reveals five mutually exclusive political families: parliamentary democracy, the Republican Congress workers' republic, O'Duffy's corporate state, a producer-estate oligarchy, and a constitutional High Kingship restoration. The family lock is separate from the older profile lock, so each family can still resolve its internal leadership and constitutional questions without reopening another family.

The focus tree contains 215 focuses. Its three opening trunks remain settlement, economy, and defence. Political families appear after the National Settlement, then reveal self-contained democratic, communist, fascist, oligarchic, or restoration programmes without cross-tree connector clutter. Industrial concerns form a compact extension of the existing provision programme, and territorial policy occupies a dedicated right-hand lane. Concealed Ailtirí, clerical, IRA, Five Provinces, and Otherworld escalations retain their evidence or failure gates.

## Political families and advisors

Each public family has a cabinet focus that unlocks real selectable advisors through explicit pool flags:

- `ireland_constitutional_service_cabinet`: Oscar Traynor, the Hyde/O'Kelly succession, Frank Aiken, and Seán MacEntee.
- `ireland_congress_workers_cabinet`: George Gilmore and Nora Connolly O'Brien, with the vanguard advisers governed by the later Congress split.
- `ireland_blueshirt_patronage_board`: Patrick Belton, Ernest Blythe, and J. J. Walsh.
- `ireland_estates_and_professions_council`: Edward Joseph Byrne, Michael Browne, and Alfred O'Rahilly.
- `ireland_household_council`: John Hayes, Frank Duff, and Alfred O'Rahilly.

Advisor availability remains controlled by the existing route, office, date, and vacancy triggers. The lifecycle does not retire a character merely because their cabinet focus has not yet unlocked the pool.

All 45 Ireland advisor cards use the current Chaos Redux advisor-card workflow and canonical measured opening. The runtime DDS files live under `gfx/interface/ideas/ireland/advisors/`; the current manifest, review sheets, alignment sheets, source provenance, and independent approval live under `docs/plans/ireland_focus_tree/assets/advisors/` and `docs/plans/ireland_focus_tree/subagent_handoffs/`.

## Industrial concerns and contracts

Nine national focuses unlock real industrial capabilities: the Electricity Supply Board, Irish Sugar Company, Turf Development Board, Great Southern Railways, Ford Cork Works, Aer Lingus, Irish Shipping, Irish Steel, and lawful Harland and Wolff access after settlement of state 119. Ford and Harland and Wolff are military industrial organisations; the remaining civil firms are industrial concerns.

Each concern is selectable for Political Power, while Ford and Harland and Wolff are country MIOs with their own production profiles. Every company focus unlocks one named material contract under the existing provision category. The nine contracts respectively provide grid infrastructure, trucks and rolling stock, merchant hulls, a civilian materials plant, Ford trucks and Army Experience, Aer Lingus transport aircraft and Air Experience, a turf fuel reserve, a military foundry, or a Belfast dockyard and Navy Experience. Every contract is limited to one completion. Company emblems live in `gfx/interface/ideas/ireland/companies/`, are registered by `interface/ireland_industrial_concerns.gfx`, and have source, processed, prompt, contact-sheet, and manifest evidence under `docs/assets/ireland_industrial_concerns/`.

## Territorial policy

`ireland_define_the_national_question` opens the Territorial Policy decision category after the political family and Northern settlement proof are established. Every family receives a distinct reunification method and external policy:

- Democratic: plebiscite guarantees, settlement under law, and security compacts without external claims.
- Communist: an all-island workers' republic and liberation-oriented links across the channel without Irish claims.
- Fascist: an Ulster ultimatum and staged claims against states 120, 122, and 123.
- Oligarchic: customs leverage, a Belfast compact, and leases or concessions without blanket annexation.
- Restoration: a crown-and-province settlement and a historically framed claim on state 120 only.

Coercive claims never start a free war. They require the readiness conclusion, manpower, infantry equipment, support equipment, convoys, fuel, command power, control of Dublin, a Dáil majority, Political Power, preparation time, a route-authorised claim, and a favourable strength ratio against the exact target controller. The decisions issue target-specific 180-day war goals only after revalidating the target. State 119 remains governed by the existing Northern review; no external focus grants automatic cores.

The territorial category contains five route-specific Northern instruments, democratic and oligarchic access diplomacy, communist support for Welsh and Scottish republics, staged coercive claims, and a one-year postwar settlement mission. The mission participates in both global and postwar mission capacity and clears its active state when every relevant holding is resolved, on expiry, route cleanup, or loss of every relevant controlled-state and subject relationship. The explicit Atlantic Settlement focus records the final outcome after that work. Occupied states can receive local-rights settlements, Scottish or Welsh protectorate treatment, or a narrow Highlands integration review; none of these procedures grants an external core automatically.

The category and decision icons are registered in `interface/ireland_icons.gfx`. Focus icons and their shared shine registrations live in `gfx/interface/goals/` and `interface/ireland_focus_expansion_shine.gfx`; their manifest and contact sheet are under `docs/assets/ireland_focus_expansion/`.

## Parliament relationship

The four Parliament buttons intentionally remain grey whenever their canonical action trigger is false. Each button tooltip prints every live prerequisite using the same scripted triggers as the click gate, including stage, focus, Dublin, completion-state, chamber-majority, and Political Power requirements. This makes a grey button diagnostic rather than ambiguous.

## AI behavior

Historical AI follows the democratic family and peaceful territorial programme. Alternate family gateways retain zero historical weight. The route-reactive plan covers all new cabinets, companies, territorial methods, and conclusions, but family and availability triggers prevent it from crossing political locks. Historical AI never uses coercive territorial decisions.

## Future extensions

- Add company-specific timed procurement missions once their production and AI opportunity costs can be balanced against the one-shot contracts.

## Validation contract

- Exactly three ungated opening trunks.
- Exactly one public political family can be selected.
- Every new focus has title, description, reward tooltip, icon, shine, and AI coverage.
- No focus connector crossings, node intersections, long connectors, duplicate coordinates, or same-row spacing defects.
- All nine company flags resolve to seven selectable concern ideas or the two country MIOs, with registered DDS sprites and one material contract each.
- Territorial decisions use the exact controller of states 120, 122, and 123 and never grant external cores.
- Parliament requirement rows match the canonical click triggers.
