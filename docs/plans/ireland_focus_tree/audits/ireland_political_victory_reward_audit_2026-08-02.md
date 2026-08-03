# Ireland political-victory reward audit — 2026-08-02

This is a non-live source audit of the route capstones, the shared conclusion
review, the route-conclusion decision, and the core-review helper. It does not
claim that an in-game scenario was run; live HOI4 testing is outside the
user-approved completion gate.

## Route conclusion surface

The 18 route and convergence capstones in
`common/national_focus/slopx_ireland_focus_tree.txt` set a route-complete flag
and call `slopx_ireland_begin_conclusion_review`. The capstone rewards do not
call `add_building_construction`, `add_equipment_to_stockpile`, `create_unit`,
`add_fuel`, `add_convoy`, `add_dockyard`, `add_research_slot`, `create_faction`,
`change_tag`, `set_cosmetic_tag`, or `set_politics`.

The shared review in `common/scripted_effects/slopx_ireland_effects.txt` only
records route flags, checks government/law/economy/defence/foreign/Northern/
objective surfaces, consolidates reactions, closes incidents, and invokes
route cleanup. It resolves full, partial, blocked, or failed outcomes; it does
not manufacture material capacity, military power, diplomatic alignment,
offices, or recognition.

The conclusion decision at
`common/decisions/slopx_ireland_decisions.txt:52952` charges political and
command power, applies the named settlement scarcity surcharge, advances the
settlement ledger, and calls the shared finalizer. Its completion effect has
no positive political-power grant and no free industry, equipment, unit, fuel,
shipping, supply, administration, office, alignment, recognition, territory,
or core reward.

## Northern core boundary

The sole Ireland Northern core writer is
`slopx_ireland_apply_northern_core_review` in
`common/scripted_effects/slopx_ireland_runtime.txt:6584`. Its trigger requires
the integration stage and ledger to reach the core-eligible threshold, a
completed settlement ledger, all consent/flexibility/security/integration
floors, state 119 control, low resistance, the completed regional/final review
proof flags, every rights/service/policing/finance/transport/resistance/
guarantee/withdrawal/demobilisation/security/emergency-law review flag, and
no occupation or settlement failure. It is idempotent and is not called as a
focus reward.

## Sweep result

The direct source sweep found no prohibited material-grant effect in the
Ireland focus tree or Ireland event files. Equipment and fuel effects in the
decision file belong to explicit operational action costs/commitments and are
not political-victory rewards. The single positive/negative political-power
event adjustment found in `events/slopx_ireland_events.txt:22802-22810` is a
priced Frank Ryan custody/hearing choice, not a conclusion reward.

Conclusion: the political-victory boundary is structurally satisfied. The
feature remains incomplete for the independent source-clearance blockers
listed in `ireland_final_non_live_completion_audit_2026-08-02.md`.
