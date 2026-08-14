# Ireland National Situation Ledger

Status: accepted for implementation on 2026-08-14.

This package is the source-of-truth design for the Ireland mechanics dashboard and its national-focus inlay. It replaces the expectation that the player must infer the purpose of dozens of country variables from events and decision requirements.

The package contains:

- `ireland_mechanics_hub_spec.md`: player experience, scripted-GUI, focus-inlay, action, AI, lifecycle, and validation contract;
- `value_purpose_matrix.md`: the authoritative list of player-facing mechanic values and their purpose;
- `asset_prompt.md`: the presentation and asset contract;
- `implementation_prompt.md`: the bounded implementation order and acceptance checklist.

The hub does not expose event preview variables, dispatch cursors, temporary calculations, dirty counters, cached thresholds, or other implementation state. Those values are not mechanics the player can meaningfully influence. Route-specific values remain visible in the dedicated Northern and Evidence ledgers and are summarised in the hub only when their systems are active.

