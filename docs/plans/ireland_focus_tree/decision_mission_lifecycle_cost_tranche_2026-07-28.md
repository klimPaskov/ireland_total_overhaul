# Ireland decision and mission lifecycle/cost tranche — 2026-07-28

Feature slug: `ireland_focus_tree`

This tranche records bounded source repairs found by the decision/mission and completion audits. HOI4 was not launched; the evidence below is static source and localisation evidence.

## Automatic objective missions

All 54 canonical `slopx_ireland_mission_*` objective blocks now use `selectable_mission = no`. They remain activated by their paired actions and resolve through their existing automatic `available`, timeout, cancellation, escalation, and cleanup effects. This prevents a completed map objective from waiting for a second player click.

## Named action-cost presentation

All 140 actions retain their native `cost =` field and their existing completion-time named-ledger surcharge logic. Their `custom_cost_text` entries now point to the named ledger actually used by that action's surcharge checks, with 50 shared ledger-specific localisation keys covering the 140 actions. The requirements tooltips no longer display the unrelated global maximum scarcity band; they explain the action-specific severe/watch/stable bands while the cost text shows the current named ledger value.

The underlying bands remain: below 15 adds 10 Political Power and Command Power plus 2 burden; 15 through 29 adds 5 Political Power and Command Power plus 1 burden; 30 or above adds no surcharge. The command-power ceiling remains 60, and the native AI budget signal remains present.

The 2026-07-29 row audit found 77 stale `custom_cost_text` ledger labels whose displayed scarcity variable differed from the variable used by the action's surcharge checks. Those labels are now aligned in `common/decisions/slopx_ireland_decisions.txt`; the 140-row disposition is recorded in `docs/plans/ireland_focus_tree/action_material_safeguard_ledger_2026-07-29.md`, and the post-repair sweep reports 140/140 matches.

## Achievement correction

`slopx_ireland_resurrection_without_sponsor` now checks current `slopx_ireland_german_leverage < 40` for its A-22 success condition. It no longer checks the historical high-water mark, so the achievement can be earned after the German channel is reduced below the canonical threshold.

## Remaining boundary at tranche time

The full 140-row material/safeguard audit was still being expanded when this
2026-07-28 record was written. The member-contribution route now exposes the
mapped troop/ship/finance/intelligence/infrastructure choice; its live engine
and refund scenarios remain unrun. The former Radical/Underground two-slot
wording question is superseded by the accepted M2 ruling: the exact 54-family
inventory uses physically nested ordinal 006 and 009 mission families. The
current non-live decision/mission contract and source-clearance status are
recorded in `project_status.md` and
`audits/ireland_final_non_live_completion_audit_2026-08-02.md`.

## Equipment archetype and physical-input repair

The bounded decision/mission audit found invalid vanilla equipment identifiers in
the Ireland action and refund paths. Stockpile effects and `has_equipment`
triggers now use the vanilla archetypes `train_equipment` and
`motorized_equipment`; descriptive `TRAIN`/`TRUCK` macro names remain unchanged
where they describe the project commitment. The ten direct numeric equipment
deductions are now paired with local gate/charge macros and their admission
checks: mills support equipment, rail trains, strategic-depot infantry
equipment, essential-cargo convoys, command-exercise infantry equipment,
motorised-route transport, coastwatch support equipment, harbour artillery,
Northern-campaign infantry equipment, and the merchant-fleet convoy charge.

Static post-patch evidence: 140 action definitions, 54 mission definitions, no
direct numeric equipment deductions, no remaining `train`/`truck` equipment
archetype tokens in `common/`, and only vanilla-recognized stockpile types.
HOI4 was not launched.
