# Ireland post-exceptional acceptance scenarios — 2026-08-14

## Evidence boundary

This record validates the current 256-focus package against the nine scenarios
in `docs/specs/ireland_country_package/implementation_matrix.md`. It is a
source-backed, offline acceptance pass: focus inspection/rendering, event and
decision lifecycle audits, AI-plan crosswalks, scripted-GUI inspection, and
asset/localisation audits. It does not claim a live engine playthrough.

## Scenario matrix

| Scenario | Result | Current evidence |
| --- | --- | --- |
| Historical 1936–1951 | pass | Historical strategy queues resolve against the current focus roster; every exceptional focus and exceptional event option has a historical factor of zero. The ordinary monthly dispatcher advances a durable cursor and cannot produce daily report spam. |
| Democratic family | pass | The republican gateway, cabinet/ministry programme, lawful Northern plebiscite, non-coercive Atlantic access, postwar settlement and coalition recovery all have focus, decision, event, AI and localisation owners. |
| Communist family | pass | Congress commitment, plural/vanguard split, workers' programme, Northern campaign/rebuild, liberation outcome, postwar settlement and reconvened-congress recovery are route-locked and AI-owned. |
| Fascist family | pass | O'Duffy commitment, personal/corporate split, material command programme, ultimatum/refusal chain, staged coercive targets, withdrawal/demobilisation recovery and postwar settlement retain readiness and strength gates. |
| Oligarchic family | pass | Vocational commitment, creditor/estate/producer programme, customs and protectorate outcomes, managed settlement and producer-estate recovery have distinct focus and decision ownership. |
| Restoration family | pass | Constitutional crown, provincial assent, Dál Riata demand/refusal/enforcement, postwar settlement and Crown Council recovery are connected; the captured and sacral crown escalations remain separately concealed and permission-gated. |
| Failure and recovery | pass | Timed projects use cancel/timeout cleanup, mission-capacity accounting and route-specific recovery records. Failed or blocked conclusions stay open for recovery rather than being archived as success. |
| Hidden-route boundary | pass | Serious cultural work remains available without revealing impossible content. High Kingship escalation, Five Provinces extremes, Otherworld sovereignty and convergence require their explicit permission, evidence, family and readiness gates. |
| Exceptional routes and convergence | pass | The 38-focus tranche has 22 action/mission cards, events 438–460, seven same-slot spirits and ten cosmetics. Fianna certification requires a player-built deployed division at 90% strength and 80% organisation and consumes manpower, equipment and command power. The final convergence starts a 180-day review; only the mission result commits the terminal conclusion. |

## Balance and exploit checks

- No exceptional focus grants a free division, core, state, war, subject,
  equipment stockpile, or resource deposit.
- Exceptional action costs, mission durations, thresholds, deltas and AI values
  are centralised in `common/script_constants/ireland_exceptional_routes.txt`;
  native fields that reject script constants use synchronized file-local macros.
- Mission cleanup removes active markers and updates the shared mission-capacity
  ledger. Household audits are capped, material commitments are consumed once,
  and failed paths retain explicit recovery rather than a repeatable reward.
- The final focus inspection reports 256 focuses, 265 connectors, exactly three
  opening roots, and zero crossings, node intersections, long connectors,
  duplicate positions, or cramped same-row pairs.

## Artifacts and bounded limitations

Current focus evidence is recorded in
`docs/plans/ireland_country_package/subagent_handoffs/final_focus_audit_256_2026-08-14.md`.
Decision/event evidence is recorded in
`docs/plans/ireland_country_package/subagent_handoffs/final_exceptional_decision_event_audit_2026-08-14.md`.
Country, localisation and asset evidence is recorded in
`docs/plans/ireland_country_package/subagent_handoffs/final_exceptional_country_package_integration_audit_2026-08-14.md`.
The offline GUI renderer cannot execute `buttonstate.lua`; the Parliament
enabled-state result is therefore proven by the shared trigger/executor source,
the green normal button texture, and the clean GUI graph rather than a simulated
shader transition.
