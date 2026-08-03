# Ireland mission/localisation re-audit — 2026-07-29

Status: **structurally complete for the 54 canonical mission families; live
engine and gameplay validation intentionally excluded from the completion gate**.

The audit read the current mission blocks in
`common/decisions/slopx_ireland_decisions.txt` and the UTF-8 localisation file
`localisation/english/slopx_ireland_l_english.yml`. It did not change either
file.

## Coverage

- 54 mission blocks were found, matching the canonical 54-family inventory.
- Every mission has a title and description localisation key.
- All 54 titles and all 54 descriptions are distinct; no generic copied
  mission prose remains in this surface.
- Every mission has a registered mission icon, activation gate, named map
  objective tooltip, scripted deadline, cancellation trigger/effect, timeout
  effect, completion effect, and authored `ai_will_do` block.
- All 54 description deadlines match the corresponding
  `days_mission_timeout` value in source. This includes the scripted deadline
  repair for the formerly mismatched descriptions.
- All 54 mission bodies expose the shared full-success, partial-success,
  failure, and escalation result branches, record the result, and clear the
  active/temporary mission state through the route cleanup path.
- All 54 map-objective tooltip keys resolve in the final localisation file.

The result interface remains explicit: full success is `1`, partial success
is `2`, failure is `3`, cancellation is `4`, and escalation is `5`, as stated
by the decision-file header and consumed by the shared mission-result ledger.
Mission descriptions name the work, place, deadline, full and partial result,
failure consequence, and escalation or cleanup consequence rather than
describing passive rewards.

## Remaining scope

This source re-audit does not claim live Clausewitz parsing, mission ticking,
AI queue behaviour, or scenario execution. It also does not resolve the
canonical wording contradiction that describes two Radical/Underground
mission slots while the fixed 54-family inventory contains no Radical mission
rows; that remains recorded in the dedicated capacity reconciliation note.
