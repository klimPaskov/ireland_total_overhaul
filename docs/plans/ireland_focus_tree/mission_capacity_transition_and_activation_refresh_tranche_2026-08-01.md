# Ireland mission-cap transition and activation-refresh tranche

Date: 2026-08-01
Scope: `ireland_focus_tree`, namespace `slopx`
Authority: approved M2 mission merge and A2 static-hidden achievement ruling

## Changes

- `slopx_ireland_update_mission_capacity` now keeps the explicit cap ladder in
  one runtime variable: 8 in normal peace, 10 during a national emergency or
  war, and 12 only while both the national emergency and Northern occupation
  are active.
- Leaving either emergency condition returns to the 10-slot band first. The
  10-slot band decays to 8 only after 30 consecutive stable days, including
  the transition from the conditional 12-slot band.
- `slopx_ireland_has_active_mission_capacity` reads the current dynamic cap
  rather than reconstructing only the three flag-based states. This keeps the
  temporary post-emergency 10-slot band usable by ordinary mission admission.
- Critical admission retains strict post-activation `greater_than` handling:
  the active counter is rebuilt after activation, so an entry into a free
  reserved slot must not pre-empt a routine mission merely because the
  rebuilt count equals the cap.
- All eight Radical/Underground mode activations now refresh mission capacity
  immediately after activating their merged M2 mission. The mutually
  exclusive foreign procurement branches refresh once after the selected
  branch, preserving one capacity rebuild per action.

## Static evidence

- `common/decisions/slopx_ireland_decisions.txt` contains 67 activation call
  sites representing exactly 54 unique mission IDs, matching M2.
- The eight Radical/Underground call sites have direct refresh effects. The
  two existing multi-step activations refresh after their timeout adjustment,
  and the four mutually exclusive procurement branches share one guarded
  refresh after branch selection.
- Category counters and caps remain rebuilt from the 54 active mission flags;
  critical reservations remain 1/2/3 for normal/emergency/conditional
  states, with the existing category-cap overlays intact.

## Remaining work

This tranche does not close the full Ireland goal. Priority scoring and
per-category admission still require a separate static audit, as do AI parity,
achievement delivery, portrait token closure, cosmetic identity localisation,
GUI write paths, remaining source-clearance rows, and the non-live completion
matrix. Live HOI4 testing remains explicitly excluded by the user ruling.
