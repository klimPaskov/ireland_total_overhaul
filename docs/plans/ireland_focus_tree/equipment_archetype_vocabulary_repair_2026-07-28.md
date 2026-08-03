# Ireland equipment-archetype vocabulary repair — 2026-07-28

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`  
Status: source-level repair complete; live parser and gameplay scenarios are excluded by user direction.

## Finding

The Ireland package used the supply-vehicle shorthand `train` and `truck`
inside `has_equipment` stockpile triggers. The airspace interception action
also used bare `fighter_equipment` for a stockpile check and deduction. The
local vanilla precedent uses `train_equipment` for trains and
`motorized_equipment` for trucks in `has_equipment`, while `train`/`truck` are
the documented `type` values for the separate `get_supply_vehicles` effect.
Without By Blood Alone, vanilla plane definitions expose fighter types as
`fighter_equipment_0` through `_3` and `jet_fighter_equipment_1`/`_2`. With
By Blood Alone, custom small-aircraft designs resolve through the
`small_plane_airframe` archetype. Bare `fighter_equipment` is not a defined
stockpile type in either branch. The same Ireland actions already charge and
refund the valid supply archetypes.

## Repair

The remaining five trigger checks and three AI feasibility checks now use the
vanilla equipment identifiers:

- member infrastructure contribution: train and motorized equipment;
- Dublin–Cork rail corridor admission and AI floor: train equipment;
- essential cargo admission and AI floor: train equipment;
- Belfast industrial contract admission and AI floor: motorized equipment.

The named constants and player-facing truck/train wording were left intact;
only the engine-facing equipment tokens changed. No new archetype, equipment
definition, stockpile grant, refund amount, route, or mission was added.

The airspace action is now DLC-aware:

- with By Blood Alone, it admits five custom small-aircraft designs through
  `small_plane_airframe` and removes five from that archetype;
- without By Blood Alone, it admits any one of the six defined legacy fighter
  types at the existing five-aircraft gate, then consumes five aircraft from
  the first qualifying type in the same order.

Its existing negative aircraft charge and negative fuel charge remain
unchanged, so the repair does not add equipment or fuel to a successful
interception.

## Evidence

- Local vanilla `documentation/triggers_documentation.md` documents
  `has_equipment` as the country stockpile trigger.
- Vanilla `common/decisions/_generic_decisions.txt`, `common/decisions/SOV.txt`,
  and `common/national_focus/persia.txt` use `train_equipment` in
  `has_equipment` blocks.
- Vanilla `common/units/equipment/plane_airframes.txt` defines
  `small_plane_airframe` as an archetype. Vanilla By Blood Alone branches use
  that archetype where non-BBA branches use concrete fighter equipment.
- Official effects documentation states that a negative
  `add_equipment_to_stockpile` amount removes equipment. Vanilla removes
  generic archetypes with the same effect. No exact negative
  `small_plane_airframe` example exists in vanilla, so the BBA subtraction is
  a source-level inference from those two documented contracts.
- A focused Ireland scan now finds zero `has_equipment` blocks containing the
  bare `train`, `truck`, or `fighter_equipment` tokens, and finds the
  corresponding valid equipment checks and deductions.
- The two touched Clausewitz files have balanced braces.

Excluded by user direction: HOI4 launch, live parser output, mission timing,
and AI selection scenarios.
