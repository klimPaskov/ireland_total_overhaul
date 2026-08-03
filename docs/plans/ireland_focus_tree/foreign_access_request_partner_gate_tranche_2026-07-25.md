# Foreign access request partner gate tranche — 2026-07-25

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`

## Canonical requirement

The neutrality decision map defines `Answer a Foreign Access Request` as a response to a partner seeking port, airfield, corridor, repair, weather, or intelligence access. It must carry sovereignty safeguards, leverage, public-consent, incident, deadline, and cleanup meaning. A date and a generic access law do not identify a requesting partner.

## Implementation

The action now consumes `slopx_ireland_foreign_access_request_partner_valid`. The trigger requires:

- one of the five named N07 access-chain source flags (`254` through `258`),
- a live valid British, American, German, Vatican, or neutral channel, or the recorded N07 foreign-reaction subject, and
- the sovereignty-mandate or sovereignty-safeguard record.

The existing active access law, state-135 map gate, Neutrality Integrity ceiling, category capacity, and dynamic Political Power/Command Power scarcity costs remain in the owning decision. The action does not grant access, alignment, recognition, territory, cores, industry, equipment, units, fuel, shipping, administration, offices, or free supply; the foreign-reaction and incident helpers own the bounded answer and cleanup.

## Evidence

- Trigger: `common/scripted_triggers/slopx_ireland_triggers.txt`
- Action admission: `common/decisions/slopx_ireland_decisions.txt`
- Player-facing requirements: `localisation/english/slopx_ireland_l_english.yml`
- Reusable-helper contract: `docs/slopx_dynamic_effects.md`
- Source chain: `common/scripted_effects/slopx_ireland_operational_state.txt` and `events/slopx_ireland_events.txt`
- Canonical row: `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`

## Remaining proof

Static source and localisation checks are required after the edit. A live engine scenario still needs to prove that the action remains hidden for a date-only incident, appears with a named source and valid channel, closes the N07 incident, records the foreign reaction, and cleans up after sponsor invalidation or route closure.
