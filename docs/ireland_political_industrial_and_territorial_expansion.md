# Ireland political, industrial, and territorial expansion

## Overview

The National Settlement reveals five mutually exclusive political families: parliamentary democracy, the Republican Congress workers' republic, O'Duffy's corporate state, a producer-estate oligarchy, and a constitutional High Kingship restoration. The family lock is separate from the older profile lock, so each family can still resolve its internal leadership and constitutional questions without reopening another family.

The focus tree contains 218 focuses and 222 prerequisite connectors. Its three
opening trunks remain settlement, economy, and defence. Political families
appear after the National Settlement, then reveal self-contained democratic,
communist, fascist, oligarchic, or restoration programmes without cross-tree
connector clutter. Industrial concerns form a compact extension of the existing
provision programme, and territorial policy occupies a dedicated right-hand
lane. Concealed Ailtirí, clerical, IRA, Five Provinces, and Otherworld
escalations retain their evidence or failure gates. The accepted coordinate-only
family-lane reflow in `89ff719` centers the five substantive lanes within x
`-26..21` and y `0..22`, with zero structural defects and one retained
nonblocking clerical linear detour.

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

Nine national focuses unlock real industrial capabilities: the Electricity Supply
Board, Irish Sugar Company, Turf Development Board, Great Southern Railways,
Ford Cork Works, Aer Lingus, Irish Shipping, Irish Steel, and lawful Harland and
Wolff access after settlement of state 119. The first seven are selectable
industrial concerns; Ford Cork and Harland and Wolff are country military
industrial organisations with their own production profiles.

Each of the seven concerns and two MIOs exposes one named 35-day material
contract. The contract reserves one or two civilian factories and produces its
distinct grid, rolling-stock, merchant-hull, civilian-plant, truck, aircraft,
fuel, foundry, or dockyard/experience output. Every contract is limited to one
completion. Company emblems live in `gfx/interface/ideas/ireland/companies/`,
are registered by `interface/ireland_industrial_concerns.gfx`, and have source,
processed, prompt, contact-sheet, and manifest evidence under
`docs/assets/ireland_industrial_concerns/`.

## Territorial policy

`ireland_define_the_national_question` opens the Territorial Policy decision category after the political family and Northern settlement proof are established. Every family receives a distinct reunification method and external policy:

- Democratic: plebiscite guarantees, settlement under law, and security compacts without external claims.
- Communist: an all-island workers' republic and liberation-oriented links across the channel without Irish claims.
- Fascist: an Ulster ultimatum and staged claims against states 120, 122, and 123.
- Oligarchic: customs leverage, a Belfast compact, and leases or concessions without blanket annexation.
- Restoration: a crown-and-province settlement and a historically framed claim on state 120 only.

Coercive claims never start a free war. They require the readiness conclusion, manpower, infantry equipment, support equipment, convoys, fuel, command power, control of Dublin, a Dáil majority, Political Power, preparation time, a route-authorised claim, and a favourable strength ratio against the exact target controller. The decisions issue target-specific 180-day war goals only after revalidating the target. State 119 remains governed by the existing Northern review; no external focus grants automatic cores.

The territorial category contains five route-specific Northern instruments,
democratic and oligarchic access diplomacy, communist support for Welsh and
Scottish republics, staged coercive claims, and the P1 recovery paths for
democratic plebiscite relaunch, the Congress workers' border campaign, fascist
border withdrawal, restoration Provincial Assent reconvening, and the existing
producer-estate Belfast compact. These paths are connected to the National
Question chain and do not refund their material reserve. The Atlantic Settlement
mission uses the shared global and postwar capacity system with its authored
180-day lifecycle; its active state clears on conclusion, expiry, route cleanup,
or loss of every relevant controlled-state and subject relationship. Occupied
states can receive local-rights settlements, Scottish or Welsh protectorate
treatment, or a narrow Highlands integration review; none of these procedures
grants an external core automatically.

The category and decision icons are registered in `interface/ireland_icons.gfx`. Focus icons and their shared shine registrations live in `gfx/interface/goals/` and `interface/ireland_focus_expansion_shine.gfx`; their manifest and contact sheet are under `docs/assets/ireland_focus_expansion/`.

## Parliament relationship

The four Parliament buttons use the registered green/brass enabled treatment and
the engine-darkened unavailable treatment. Each button tooltip prints every
live prerequisite using the same scripted triggers as the click gate, including
stage, focus, Dublin, completion-state, chamber-majority, and Political Power
requirements. The bounded Parliament repair therefore keeps the visual state
and guarded executor in agreement without introducing a second action path.

## AI behavior

Historical AI follows the democratic family and peaceful territorial programme.
Alternate family gateways retain zero historical weight. The route-reactive plan
covers all new cabinets, companies, territorial methods, conclusions, and
recovery surfaces, but family and availability triggers prevent it from crossing
political locks. Historical AI never uses coercive territorial decisions.

## Postwar family conclusions

Each of the five families has one 180-day settlement project and one 120-day
recovery project. Selection reserves the documented inputs and marks the project
in progress; natural expiry produces the durable settlement or recovery result,
while cancellation only cleans launch state and route-specific temporary flags.
Each settlement opens a direct player-facing conclusion report with distinct
210x176 report art, then archives the route result so it cannot be replayed as a
generic flavour event. The five exact settlement/recovery decision pairs and
their terminal lifecycle are maintained in
`docs/specs/ireland_country_package/systems_and_lifecycles.md`.

## Future extensions

- Add company-specific timed procurement missions once their production and AI opportunity costs can be balanced against the one-shot contracts.

## Validation contract

- Exactly three ungated opening trunks.
- Exactly one public political family can be selected.
- Every new focus has title, description, reward tooltip, icon, shine, and AI coverage.
- No focus connector crossings, node intersections, long connectors, duplicate coordinates, or same-row spacing defects.
- All nine company flags resolve to seven selectable concern ideas or the two country MIOs, with registered DDS sprites and one 35-day material contract each.
- Territorial decisions use the exact controller of states 120, 122, and 123 and never grant external cores.
- Parliament requirement rows match the canonical click triggers.
