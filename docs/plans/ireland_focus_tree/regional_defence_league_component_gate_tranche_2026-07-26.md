# Regional defence league component-gate tranche

Feature slug: `ireland_focus_tree`

Status: implemented source tranche; the Ireland overhaul remains incomplete because source clearance, live engine checks, AI queue behaviour, GUI rendering, and required runtime scenarios remain open.

## Scope

The canonical statecraft material requires a regional defence league to be more than a high aggregate Readiness display. The proposal already requires a fully ratified regional charter, valid members, a defined military contribution, sovereignty safeguards, a real division in a named southern region, a common threat, Readiness 75, and Provision 65. This tranche adds the four specified operational component floors without changing the action or mission inventory.

## Implemented gate

`ireland_action_propose_a_regional_defence_league` now requires all of the following through shared `script_constants` values:

- Readiness display at least `75`;
- Provision display at least `65`;
- Warning at least `45`;
- Maritime Protection at least `45`;
- Command at least `45`;
- Intelligence at least `45`.

The aggregate and component gates are in the same availability wrapper and are described together in the player-facing requirement text. No territory, faction membership, subject, core, equipment, unit, fuel, shipping, administration, office, alignment, recognition, or political-power store is granted.

## Evidence and boundaries

- `common/script_constants/ireland_constants.txt` owns the shared thresholds.
- `common/decisions/ireland_decisions.txt` applies the thresholds before the action can launch.
- `localisation/english/ireland_l_english.yml` names the current component requirements.
- The existing force, charter, member, safeguard, common-threat, category-cap, and dynamic Political Power/Command Power gates remain unchanged.
- The later `Ratify a Regional Charter` and `Meet the Member Contribution Schedule` missions still own named map objectives, deadlines, partial success, failure, escalation, and cleanup.

## Remaining validation

Static source checks can verify constant use, balanced blocks, and localisation encoding. Live action admission, mission timing, AI queue selection, foreign reactions, GUI display, and fresh-save route scenarios remain not-run by request.
