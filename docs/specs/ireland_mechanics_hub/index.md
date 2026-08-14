# Ireland National Situation Ledger

Status: implemented on 2026-08-15.

The accepted design is implemented in the current decision-category ledger and focus-tree inlay. Frozen evidence is recorded in `docs/plans/ireland_mechanics_hub/completion_report_2026-08-15.md`: focus inspection revision `90beeec44304c287` (256 focuses, 234 connectors, zero crossings, node intersections, long connectors, and too-close pairs), plus final dashboard/inlay GUI inspection revisions `f8fc5fbe5ea0d72c` and `33f76c15e0ae8ae6` with no blockers at 1920x1080 and 2560x1440.

This package is the source-of-truth design for the Ireland mechanics dashboard and its national-focus inlay. It replaces the expectation that the player must infer the purpose of dozens of country variables from events and decision requirements.

The package contains:

- `ireland_mechanics_hub_spec.md`: player experience, scripted-GUI, focus-inlay, action, AI, lifecycle, and validation contract;
- `value_purpose_matrix.md`: the authoritative list of player-facing mechanic values and their purpose;
- `asset_prompt.md`: the presentation and asset contract;
- `implementation_prompt.md`: the bounded implementation order and acceptance checklist.

The hub does not expose event preview variables, dispatch cursors, temporary calculations, dirty counters, cached thresholds, or other implementation state. Those values are not mechanics the player can meaningfully influence. Route-specific values remain visible in the dedicated Northern and Evidence ledgers and are summarised in the hub only when their systems are active.
