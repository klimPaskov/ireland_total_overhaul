# Reconstruction-aid programme gate tranche — 2026-07-25

Feature slug: `ireland_focus_tree`

Status: implemented source tranche; the Ireland overhaul remains incomplete because source clearance, live engine checks, and required runtime scenarios are still open.

## Canonical requirement

The decision and lifecycle specifications define **Accept or Refuse Reconstruction Aid** as a postwar statecraft action available only when a valid foreign or multilateral reconstruction programme exists. The programme must expose money, goods, markets, planning, access, and conditions as separate political questions. A calendar date or a generic postwar review is not itself an aid offer.

## Source wiring

`common/decisions/slopx_ireland_decisions.txt` now requires one of the existing FR11/RC07 reconstruction-offer states before the action can be selected:

- `slopx_ireland_foreign_reaction_event_426_available` — the foreign-reaction scheduler has produced the reconstruction-conditions offer;
- `slopx_ireland_event_426_open` — the offer is currently being resolved;
- `slopx_ireland_foreign_fr11_postwar_reconstruction_conditions_accepted` — the programme was accepted under the recorded terms; or
- `slopx_ireland_foreign_fr11_postwar_reconstruction_conditions_refused` — the programme was refused and the refusal remains part of the postwar record.

This keeps the action coupled to the named foreign-reaction chain while preserving recovery and refusal play. The action still pays its dynamic Political Power and Command Power costs, increases Foreign Exposure only through its authored effect, and does not grant equipment, factories, shipping, units, territory, cores, recognition, or passive political power.

The confirmation localisation names the programme/offer requirement so the player can distinguish it from the separate postwar date and review gates.

## Cleanup and validation

The existing route-cleanup branch clears the action's active flag. No new persistent aid flag was introduced, and no foreign-reaction resolution flags are cleared by the action; the foreign chain owns those lifecycle flags and its existing route cleanup remains authoritative.

Static source inspection was used for this tranche. HOI4 was not launched, and the offline MCP transport/live engine checks and scenario programme remain open blockers.
