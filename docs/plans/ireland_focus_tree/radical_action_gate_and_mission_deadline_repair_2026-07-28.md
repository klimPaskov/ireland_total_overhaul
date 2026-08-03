# Radical action gates and mission deadline repair

Date: 2026-07-28
Feature: `ireland_focus_tree`
Namespace: `slopx`

## Scope

This tranche repairs two bounded implementation mismatches found during the decision and mission audit. It does not add mission families, alter the fixed 54-family inventory, or resolve the still-open canonical question about the two reserved Radical and Underground mission slots.

## Radical and Underground action gates

The ten actions in `slopx_ireland_radical_underground` no longer share the broad `slopx_ireland_radical_transition_gate` admission test. Their `available` blocks now consume the derived readiness flags that the runtime already maintains:

| Action | Admission surface |
| --- | --- |
| Audit the Republican Commands | IRA organisation readiness or a live security crisis |
| Convene the Convention of Commands | IRA transition and public-base readiness |
| Create a Civil Republican Directorate | IRA civil-authority readiness |
| Rebuild the Republican Congress | Congress organisation and transition readiness |
| Ratify the Common Programme | A plural or vanguard Congress delegate mandate |
| Reassemble the National Corporate Party | O'Duffy crisis and network readiness |
| Impose Compulsory Estates | O'Duffy route, corporate-estates readiness, and Army acceptance |
| Organise Ailtirí Cells | Dated Ailtirí cell readiness, including the existing culture/evidence/crisis derivation |
| Launch the Ailtirí Party State | Public-launch readiness and the Ailtirí crisis record |
| Dissolve the Failed Underground | A route-failure or accepted-recovery record |

This keeps the existing category-capacity, named state, dynamic PP/CP, ledger, and cleanup logic intact while preventing unrelated constitutional, law, or office states from exposing radical actions.

## Mission deadline localisation

All 54 mission blocks were compared with their `_desc` localisation. The 38 descriptions whose prose deadline differed from `days_mission_timeout` were corrected in `localisation/english/slopx_ireland_l_english.yml`; the script values remain the timing authority. No mission deadline was made dynamic or changed in the decision source.

## Evidence

- `common/decisions/slopx_ireland_decisions.txt`: ten radical availability blocks use the route-specific readiness gates above; no radical availability block contains the former broad transition gate.
- `localisation/english/slopx_ireland_l_english.yml`: all 54 mission descriptions are present and their stated day value matches the corresponding `days_mission_timeout` value.
- Localisation remains UTF-8 with BOM.
- No HOI4 process, live save, or in-game scenario was used. The user-directed completion authority excludes live in-game testing; local static/reference checks and unresolved source-clearance or canonical-design blockers remain separate.

## Remaining blockers

- The canonical Radical and Underground mission-capacity wording still reserves two slots while the fixed implementation inventory remains 54 families with no Radical mission block. This requires a design ruling before code changes.
- Historical source clearance and the staged-achievement visibility questions remain open elsewhere in the completion ledger.
