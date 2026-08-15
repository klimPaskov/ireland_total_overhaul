# Supplied Error Cleanup — Decision and Parser Audit

## Scope and outcome

Assigned source surfaces:

- `common/decisions/ireland_decisions.txt`
- `common/decisions/ireland_expansion_decisions.txt`
- `common/scripted_triggers/ireland_triggers.txt`
- `common/scripted_localisation/ireland_exceptional_routes.txt`

No gameplay source was changed. Every supplied, mod-owned parser or script error
within this scope is already corrected in the current worktree, which is
unchanged from baseline `a899c94` for all four assigned files. The only file
created by this task is this handoff.

External vanilla diagnostics for `IRQ`, `GER`, and `CHL` were deliberately not
overridden.

## Issue list, sorted by severity

| Severity | Supplied diagnostic | Current finding | Disposition |
| --- | --- | --- | --- |
| Blocker | Fianna dynamic cost tokens | All four reported tokens are absent. The mission uses file-local charge macros. | Already corrected; no patch. |
| Blocker | `constant:ireland.postwar_family_factory_use` in `civilian_factory_use` | The malformed use is absent. All postwar project modifiers use `@IRELAND_POSTWAR_FAMILY_FACTORY_USE`, defined as `1` in the same decision file. | Already corrected; no patch. |
| Blocker | Invalid `is_at_war` in decisions/triggers | `is_at_war` is absent from all four assigned files. War checks use documented `has_war = yes/no`. | Already corrected; no patch. |
| Blocker | Malformed `free_building_slots` | The six expansion instances use the documented state-trigger form: `free_building_slots = { building = industrial_complex size > 0 }`. | Already corrected; no patch. |
| High | Unexpected scripted-localisation key | `GetIrelandExceptionalRouteStatus` uses the vanilla spelling `localization_key`; all five referenced keys exist in `localisation/english/ireland_exceptional_routes_l_english.yml`. | Already corrected; no patch. |
| High | Non-reciprocal focus exclusions | Read-only verification finds reciprocal blocks for the provincial council versus federal/pentarchy pair and contact-extraction versus compact/containment pair. | Already corrected; focus file is outside this ownership. |
| High | `KOM_democratic` flag format | Read-only TGA header audit: base `82x52`, medium `41x26`, small `10x7`; each is image type `2`, 32-bit, with alpha descriptor `8`. | Already corrected; flag assets are outside this ownership. |

No remaining reproducible error exists in an assigned source file.

## Exact reported form versus current form

- `ireland_mission_equip_a_fian_company` no longer refers to
  `ireland_exceptional_fian_manpower_cost`,
  `ireland_exceptional_fian_infantry_equipment_cost`,
  `ireland_exceptional_fian_support_equipment_cost`, or
  `ireland_exceptional_fian_command_cost`. Its completion effect uses
  `@IRELAND_EXCEPTIONAL_FIAN_MANPOWER_CHARGE`,
  `@IRELAND_EXCEPTIONAL_FIAN_INFANTRY_EQUIPMENT_CHARGE`,
  `@IRELAND_EXCEPTIONAL_FIAN_SUPPORT_EQUIPMENT_CHARGE`, and
  `@IRELAND_EXCEPTIONAL_FIAN_COMMAND_CHARGE`.
- Postwar project modifiers use
  `civilian_factory_use = @IRELAND_POSTWAR_FAMILY_FACTORY_USE`, never
  `civilian_factory_use = constant:ireland.postwar_family_factory_use`.
- The scripted-localisation records use `localization_key`, exactly as vanilla
  `common/scripted_localisation/00_scripted_localisation.txt` does.
- Expansion reconstruction decisions use documented `free_building_slots`
  state blocks; no malformed block remains in the assigned expansion file.

## Decision category lifecycle notes

`ireland_mission_equip_a_fian_company` belongs to `ireland_readiness`.

- It activates only with an active-mission slot, a Fianna equipment commitment,
  and no readiness-capacity collision.
- It is visible only while the exceptional route and commitment remain open;
  availability additionally requires the service charter and the named
  material/deployment trigger.
- Completion consumes the stated manpower, infantry equipment, support
  equipment, and command power; records a full result; clears the commitment;
  and opens the follow-up objective.
- Timeout records failure, marks route fraud, and clears the commitment.
  Cancellation also clears the commitment. These paths prevent a stale active
  mission.

## Mission quality notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate/exploit risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ireland_mission_equip_a_fian_company` | IRE | `ireland_readiness` | One owned division meeting strength and organisation thresholds in state 113, 134, or 135 | Service charter; 500 manpower, 500 infantry equipment, 20 support equipment, 20 command power; an eligible deployed company | 120 days | Consumes the same resources, records full success, adds Fianna readiness, and advances the route | Records failure, marks Fianna route fraud, clears the commitment | Low: capacity and commitment gates control activation; all resource inputs are consumed; no unit or equipment is created. |

## Cost and requirement clarity

The Fianna gate and charge pair is exact: strict gates of `> 499`, `> 499`,
`> 19`, and `> 19` safely cover charges of `-500`, `-500`, `-20`, and `-20`.
The availability block wraps the trigger in
`ireland_mission_equip_a_fian_company_requirements_tt`, while the completion
effect exposes `ireland_mission_equip_a_fian_company_cost_tt`; the player does
not receive raw variable-token diagnostics.

## AI validity and route-lock notes

- This mission has no country target and therefore no dead-target or impossible
  border path.
- It is route-locked by `ireland_exceptional_route_open`, then by the service
  charter and commitment state; its AI weighting also includes the material
  readiness condition.
- Current expansion and trigger files use `has_war`, a documented country
  trigger, rather than the invalid supplied `is_at_war` form.

## Localisation and tooltip notes

`GetIrelandExceptionalRouteStatus` is parser-valid and its five candidate
keys resolve in `ireland_exceptional_routes_l_english.yml`. The helper has no
current call site outside its own definition and an older repository-map note;
that is a low-priority wiring observation, not a supplied parser error and was
left untouched under the bounded correction scope.

## Cleanup and exploit-risk notes

The Fianna commitment is cleared on completion, timeout, and cancellation.
Because the mission grants neither a division nor a stockpile reward and each
run consumes matched gated inputs, this audit found no free-unit or equipment
farming loop in the affected mission.

## Validation

- Compared every assigned file against `a899c94`: no source drift; the
  corrected forms are already baseline content.
- Searched the assigned files for all four supplied dynamic cost names, the
  malformed postwar constant use, and `is_at_war`: each is absent.
- Matched every remaining expansion `free_building_slots` block to the official
  vanilla trigger schema (`building = building_type`, `size > n`), and checked
  the six active instances.
- Checked vanilla decision documentation, trigger documentation (`has_war` and
  `free_building_slots`), script-constant documentation, and vanilla scripted
  localisation examples before judging the current forms.
- Parsed the three `KOM_democratic` TGA headers read-only; dimensions and
  32-bit true-colour layout match the flag tiers.

Skipped meaningful validation: no runtime-log search was performed, per the
task constraint; no engine load was invoked because this task required no
gameplay source change and the supplied errors are resolved statically.

## Changed files and identifiers

- Changed: `docs/plans/ireland_country_package/subagent_handoffs/supplied_error_cleanup_2026-08-15.md` only.
- Gameplay identifiers audited: `ireland_mission_equip_a_fian_company`,
  `ireland_exceptional_fian_material_ready`,
  `GetIrelandExceptionalRouteStatus`, the Scottish and Welsh protectorate
  reconstruction site checks, and the two supplied focus-exclusion groups.

No plan handoff was needed: this was a bounded parser-correction audit rather
than a design gap.
