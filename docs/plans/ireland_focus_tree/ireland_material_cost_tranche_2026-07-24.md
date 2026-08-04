# Ireland material-cost tranche — 2026-07-24

Feature slug: `ireland_focus_tree`

Status: implemented source tranche; the Ireland overhaul remains incomplete because source clearance, live engine checks, and required runtime scenarios are still open.

## Scope

This tranche deepens the existing 13-category, 140-action, 54-mission decision system without changing its inventory contract. It closes concrete stockpile and personnel burdens where the canonical decision/mission map names rifles, support matériel, trains, trucks, convoys, or operational manpower. Political power remains the native action cost, while physical inputs are separate scarcity commitments.

The static inventory after the tranche is:

- 140 actions in 13 top-level categories.
- 54 named mission families.
- 61 actions with explicit physical or manpower inputs and matching completion charges.
- 33 coded cancellation-refund branches in the shared capped recoverable-input helper.

## Action groups wired

The following canonical action groups now consume named material inputs in addition to their existing political and ledger costs:

- Agricultural logistics: Distribute Seed and Fertiliser consumes support equipment, trains, trucks, and manpower; Mobilise Emergency Turf consumes trucks and manpower; Purchase Emergency Livestock consumes trucks and manpower.
- Reserve and security forces: Activate a Cadre Reserve consumes infantry equipment, support equipment, and manpower; Expand the Local Security Force consumes rifles and manpower; Expand the Local Defence Force consumes rifles, support equipment, and manpower.
- Authority and command: Recognise a Liberated Authority consumes rifles and convoys; Integrate or Devolve Military Command consumes support equipment; Fulfil a Compact Obligation consumes support equipment and manpower.
- Local administration and relief: Update the Electoral Register, Protect Campaign Freedom, Secure Polling Stations, Fund Gaeltacht Administration, Survey Provincial Archives, Set County Tillage Quotas, Open a Border Corridor, Mobilise Diaspora Relief, Mark and Publicise Neutral Shipping, and Issue Ration Books now reserve and charge the named staff, transport, shipping, support-equipment, or manpower pools described by their requirements.

- Food infrastructure: Repair Mills and Storage now reserves fuel as well as its factory and spare-equipment commitment; cancellation recovers only the capped fuel and equipment fraction.

- Operational and security burdens: the named rail corridor, coastwatch sector, Belfast industrial contract, and foreign-agent action now carry the labour, fuel, and security-staff commitments named by the canonical map.

- Public and Northern administration: the Public Health Board, bilingual services, Border Belt confidence mission, and Transitional Authority now reserve their named trained-staff, local-staff, or administrator/guard manpower pools.

- Cultural and regional delivery: the Provincial Cultural Congress and Western Regional Portfolio now reserve 5-Truck transport pools; historic-site protection consumes 250 manpower and 5 Trucks.

- Neutrality operations: aircrew internment consumes 250 guard manpower, while Blacksod reporting consumes 250 station staff and 10 Support Equipment; both missions expose capped cancellation recovery.

- Regional command: Integrate a Voluntary Member Contribution commits 20 Support Equipment to the 180-day schedule and requires a ratified organisation, agreed safeguards, and a division in a named southern region; cancellation recovers at most 14 Support Equipment.

All completion charges are paired with their gates. The source does not award the consumed stockpile items back on success.

## Cancellation and cleanup

The shared `ireland_refund_cancelled_material_inputs` effect now handles the new cultural-congress, western-portfolio, aircrew-internment, and Blacksod-station branches as well as the earlier emergency turf, cadre reserve, compact-obligation, ration-book, charter, procurement, tillage, neutral-shipping, train, fuel, and campaign branches. Refunds are bounded recoveries only; they do not refund political power, command power, factories, ledgers, offices, territory, cores, or recognition.

The new coded refund values are:

- electoral register: 175 manpower;
- Border Belt confidence: 175 manpower;
- harvest/mills: 105 fuel in addition to 14 support equipment;
- emergency turf: 3 trucks;
- cadre reserve: 70 infantry equipment and 17 support equipment;
- compact obligation: 350 manpower and 14 support equipment;
- ration books: 350 manpower.
- cultural congress: 3 Trucks;
- western regional portfolio: 3 Trucks;
- aircrew internment: 175 manpower;
- Blacksod station: 175 manpower and 7 Support Equipment.
- member contribution: 14 Support Equipment against its 20-equipment commitment.

The origin flags and duplicate-refund guards are cleared on mission completion, cancellation, timeout, and preemption paths covered by the source audit. Mission-specific refund caps remain at or below the authored recoverable fraction.

## Evidence

- `common/decisions/ireland_decisions.txt` — action gates, completion charges, and mission cancellation wiring.
- `common/script_constants/ireland_constants.txt` — shared refund codes and quantities.
- `common/scripted_effects/ireland_effects.txt` — cancellation-safe material recovery helper.
- `docs/ireland_dynamic_effects.md` — helper contract and branch documentation.
- Static audit: 140 actions, 54 missions, 61 resource-gated actions, no gate/charge gaps, no mission-refund gaps, 132 defined and used-or-accepted decision macros, and refund caps within the authored ceiling.

## Remaining gates

This tranche does not close every canonical resource row. Remaining review work includes action-specific leverage, tied-unit, aircraft, ship, local-support, and foreign-channel safeguards where the map requires them; source-clearance manifests; live GUI and engine-reference checks; and the required gameplay scenarios. These remain explicit blockers to a completion claim.
