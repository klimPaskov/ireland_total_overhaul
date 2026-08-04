# Ireland Readiness Objective-Truth Tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

Status: source-level partial implementation; live engine and scenario evidence remain open

## Purpose

This tranche closes the largest remaining semantic weakness in four National Readiness actions and missions. The old admission layer could treat a low readiness component, a few buildings, or generic state control as an operational plan, a demobilisable force, a protected corridor, or a Belfast occupation. The linked canonical map rows require authored plans, real formations, depots and records, transport infrastructure, supply, civilian passage, and a bounded security ledger instead.

The implementation keeps Northern claims, control, occupation, settlement, integration, and cores separate. It creates no unit, moves no unit, grants no territory or core, and awards no free equipment, fuel, shipping, supply, administration, alignment, office, recognition, or political power.

## Source rows addressed

The changes follow the action and mission rows in:

- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_4_statecraft_and_war.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_lifecycle_matrix.md`
- `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_statecraft_and_war_matrix.md`

The bounded rows are:

- Protect an Operational Plan / Protect Plan W: an authored Plan W, Northern, invasion, or occupation plan; operational formation; depot and command/liaison record; communications or local authority.
- Demobilise a Force Tier / Demobilise Without Losing the Cadre: a selected cadre, Local Security Force, or Local Defence Force tier; a real formation; depot and command record; a falling-danger or postwar window; preserved cadre and records.
- Secure the Dublin–Belfast Corridor: control, rail, a supplied formation, depot, supply floor, and a recorded border/trade/wartime civilian-passage basis.
- Take and Hold Belfast: control of both named states, rail service, a supplied formation, depot, coercive campaign authority, Belfast port/industry, and a Northern Security Stability floor that limits civilian-harm and occupation-zone failure.

## Implementation surface

### Reusable triggers

`common/scripted_triggers/ireland_triggers.txt` adds:

- `ireland_has_northern_operational_force`: requires a real Irish division in state 113 or 119.
- `ireland_demobilisation_force_tier_selected`: requires completion of one of the three named mobilisation-tier actions.
- `ireland_has_demobilisable_cadre`: combines a selected tier, a real division in states 113/119/134/135, and the completed Strategic Depot record.
- `ireland_operational_plan_authority`: accepts only a fully linked Plan W/G2/British authority, a Northern plan with a local partner, a cause-valid coercive campaign, or a live occupation authority with provisional/integration review.
- `ireland_demobilisation_authority`: requires no active war and a postwar review, recorded major-war end, or the demobilisation-ready milestone with invasion danger and war spillover cleared.

These helpers are documented in `docs/ireland_dynamic_effects.md`. They are proof triggers only and have no side effects.

### Actions

`common/decisions/ireland_decisions.txt` now makes the two actions consume the proof triggers rather than the former generic low-component OR block. Motorise a Strategic Route reuses the real operational-force proof. The new gates leave the existing dynamic Political Power/Command Power, material, category-capacity, law, route, and mission-capacity checks intact.

### Missions and map objectives

The four linked map-objective triggers now recheck the physical and documentary conditions at completion time. This prevents a launch-time paper record from satisfying a mission after the formation, depot, supply, railway, route, or security situation has disappeared.

The demobilisation mission writes durable outcome records:

- Partial: `ireland_demobilised_cadre_partial` and `ireland_veteran_settlement_pending`.
- Full: `ireland_demobilised_cadre_preserved` and `ireland_force_records_archived`.

These records are separate from the postwar `Demobilise and Settle Veterans` action and do not silently settle veterans or delete the readiness ledger. Existing full/partial/failure/escalation deadlines and cleanup remain in the mission source.

### Localisation and tuning

`localisation/english/ireland_l_english.yml` explains the authored-plan, formation, depot, command, route, supply, civilian-passage, and security requirements with current dynamic values. `common/script_constants/ireland_constants.txt` centralises the command-readiness floor used by the demobilisation objective.

## Validation evidence

- Static source diff reviewed for the four intended actions/objectives; the unrelated Command District Exercise and Standardise Infantry Equipment readiness gates remain unchanged.
- The readiness helper IDs have documentation and source references.
- The implementation does not alter the canonical counts: 13 decision categories, 140 actions, 54 mission families, and 216 focus nodes.
- No HOI4 process was launched, per the user's instruction. The live engine, live AI queue, mission firing, unit-placement, deadline, partner-invalidation, and cleanup scenarios remain not-run.

## Remaining boundary

This tranche does not close the remaining canonical source rows for treaty-port and neutral approaches, folklore and supernatural proof, British/American/German/Vatican procurement and reaction branches, coastwatch and shipping depth, the broad 140-action material/safeguard mapping, source clearance, or the completion audit's engine-reference and 22-scenario programme. The feature remains incomplete.
