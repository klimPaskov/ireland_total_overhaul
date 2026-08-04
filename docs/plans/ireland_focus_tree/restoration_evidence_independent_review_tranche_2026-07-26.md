# Restoration Evidence Independent-Review Tranche

Feature slug: `ireland_focus_tree`

Status: source-level implementation tranche; HOI4 was not launched.

## Canonical row

The canonical Part 5 decision/mission map requires `Verify the Restoration Evidence` to name archives and sites, require provenance, independent review, site custody, and an unusual campaign condition, and resolve with full, partial, failure, escalation, and cleanup outcomes. The existing lifecycle already owns the 270-day deadline, result flags, partial/failure/escalation records, and route cleanup; its admission and map objective were too permissive.

## Implemented contract

- Added `ireland_restoration_evidence_authority` to centralise the admission proof.
- Required the serious-culture or archive lane, Cultural Service, Diaspora Exchange, named archive provenance, historic-site custody, royal evidence thresholds `4/3/3`, an unusual live campaign condition, and zero evidence disqualifiers.
- Added the authority, active action, and active mission flags to the named Leinster map objective. Full control, industrial capacity, and naval-base presence remain separate physical map proofs.
- Replaced the restoration action's generic serious-culture/archive gate with the named authority helper while preserving its dynamic Political Power/Command Power costs and existing mission-capacity checks.
- Updated player-facing tooltips to show current evidence counters and the independent-review, custody, and unusual-condition requirements without exposing a future hidden route name.
- Centralised the full, partial, and public-panic evidence floors as script constants so the authored admission and mission outcome thresholds stay aligned.
- Classified restoration timeout failures into false lead, fraud/disqualification, public panic, or route closure from the live evidence, disqualifier, and public-knowledge state. The existing panic-containment action and failed-restoration archive now consume those classifications, clear transient flags, and retain the durable mission-result history.

## Boundary and cleanup

The helper does not grant territory, cores, industry, equipment, units, fuel, shipping, administration, alignment, offices, recognition, or a political-power store. It does not set `ireland_independent_evidence_ready`; that flag remains downstream of a full restoration record or an approved achievement provenance path, preventing circular admission. The authored lifecycle now classifies timeout failure and wires panic containment and failed-restoration archiving to explicit cleanup flags; full, partial, escalation, hidden reveal, and live recovery behavior still require scenario validation.

## Evidence

- `common/scripted_triggers/ireland_triggers.txt`
- `common/decisions/ireland_decisions.txt`
- `localisation/english/ireland_l_english.yml`
- `docs/ireland_dynamic_effects.md`
