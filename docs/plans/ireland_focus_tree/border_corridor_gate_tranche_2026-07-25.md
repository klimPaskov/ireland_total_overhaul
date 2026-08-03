# Border Corridor Gate Tranche (2026-07-25)

Feature slug: `ireland_focus_tree`

## Scope

This tranche binds `Open a Border Corridor` to the concrete border capacity named by the canonical decision map. The action remains a controlled crossing measure in Border Belt; it does not claim, control, occupy, settle, integrate, or core Northern territory.

## Canonical requirements and effects

The canonical row admits the action for refugee, trade, relief, Plan W, or Northern settlement need and names units, police, transport, and leverage as the cost directions. Success supports relief or cooperation; failure remains exposed to smuggling, infiltration, communal violence, and foreign incursion.

## Current implementation

`common/decisions/slopx_ireland_decisions.txt` now requires:

- a named border, war-spillover, relief, Plan W, trade, or Northern-settlement pressure flag;
- at least one controlled division in the named Border Belt force area through `slopx_ireland_has_regional_contribution_force`;
- a completed local security, local defence, or policing preparation action;
- the existing 250-manpower and 5-Truck commitment, Border Belt control, Neutrality Integrity ceiling, and dynamic scarcity costs.

On completion, the action retains its 5-point Neutrality Integrity improvement and additionally moves the Northern Security Stability and British Leverage ledgers by the authored corridor deltas. It creates no free military or territorial reward.

The action description and requirements tooltip identify the pressure record, named division presence, local safeguards, manpower, trucks, and leverage exposure. Constants live in `common/script_constants/slopx_ireland_constants.txt` so the two ledger deltas remain tunable.

## Validation boundary

Static source, constant, localisation, and trigger checks are required after this tranche. HOI4 was not launched; live decision visibility, map control, division-count behavior, failure escalation, and route cleanup remain open evidence gates.
