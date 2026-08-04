# Ireland decision cost contract audit - 2026-08-02

Scope: the 140 ireland_action_* decisions in the Ireland overhaul.
This is a static audit; HOI4/live validation was intentionally excluded.

## Engine contract

The offline Decision modding reference documents regular cost and
custom_cost_trigger/custom_cost_text as alternative cost modes. A custom cost
does not charge resources by itself; its complete effect must perform the
deduction. The vanilla SOV custom-cost precedent also supplies
ai_hint_pp_cost and manually subtracts Political Power in a hidden effect.

## Ireland result

- 140/140 actions use custom-cost-only presentation.
- 0 regular cost = lines remain in the 140 action blocks.
- 140/140 actions have ai_hint_pp_cost.
- Hints range from 23 to 29 PP, matching each action's maximum base-plus-10
  scarcity exposure and its strict availability gate.
- 140/140 actions manually deduct their fixed base PP in complete_effect.
- Existing named-ledger branches continue to deduct the dynamic +10/+5/+0 PP
  and Command Power surcharge and update burden. The repeated severe and
  watch arithmetic is now centralized in
  `ireland_apply_action_scarcity_severe_surcharge` and
  `ireland_apply_action_scarcity_watch_surcharge`; each action still
  owns its distinct base values and calls the appropriate helper exactly once.
- 140/140 action-specific custom-cost localisation keys resolve and display
  the fixed base, named ledger, current value, and surcharge bands.
- The command-power charge remains bounded at 35-50, below the requested 60
  ceiling.

The change preserves action availability thresholds, physical commitments,
mission activation, cancellation/refund paths, AI utility blocks, and the
13-category/140-action/54-mission inventory.

Evidence:

- common/decisions/ireland_decisions.txt
- localisation/english/ireland_l_english.yml
- docs/plans/ireland_focus_tree/decision_mission_audit_2026-08-02.md
- paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/SOV.txt
