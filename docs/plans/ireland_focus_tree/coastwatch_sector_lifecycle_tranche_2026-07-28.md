# Ireland Coastwatch sector lifecycle tranche — 2026-07-28

## Scope

The canonical statecraft specification defines 83 historical lookout posts in six operational sectors. Each sector must retain separate coverage, observer training, communications reliability, recognition, weather reporting, rescue access, and security-exposure state.

## Implementation

- Added canonical Coastwatch constants for the 83-post total, six-sector count, full/partial component scores, and exposure bands.
- Initialised the six sector ledgers in `slopx_ireland_initialize_campaign`.
- Added deterministic next-sector selection and aggregate post recomputation in the Ireland runtime.
- Reworked the Coastwatch map-objective and mission-validity triggers to use the active named sector's regional platform.
- Made the existing Coastwatch action/mission repeatable until all six operational records exist. Partial results remain retryable; full results advance the next sector; failure and escalation preserve exposure without falsely completing a sector.
- Replaced the previous achievement-history inference from air warning, harbour defence, and marine patrol actions with direct Coastwatch sector records.
- Added scripted localisation for the named active sector and updated the action, mission, map-objective, and Coastwatch spirit descriptions.

## Runtime contract

No Coastwatch result creates territory, cores, equipment, manpower, units, factories, shipping, or recognition. The action still consumes the documented support equipment and staff inputs, and cancellation still refunds only the existing documented amounts. Sector post allocation is bounded to exactly 83 after six full sector results; partial results can be replaced by a later full result.

## Validation evidence

- Six sector component families are present and initialised for all six sectors.
- Only `slopx_ireland_record_coastwatch_sector_result` writes operational sector records.
- The achievement-history writer reads those sector records and no longer reads unrelated air, harbour, or patrol completion flags.
- No HOI4 process was launched; live mission resolution remains an explicit validation blocker for the larger Ireland goal.

## Remaining review

The wider feature still has unresolved source clearance, the canonical Radical/Underground mission-capacity contradiction, unsupported staged achievement visibility under the offline engine references, and no live engine scenario validation.
