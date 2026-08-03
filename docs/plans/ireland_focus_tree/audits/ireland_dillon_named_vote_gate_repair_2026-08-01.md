# Dillon named Dáil vote gate repair

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`  
Scope: non-live static repair; live in-game testing is excluded by user direction.

## Canonical boundary

Part 2 requires Intervention Mandate `90`, Social Consent `60`, National
Readiness `45`, a government majority, British Leverage below `60`, sovereignty
safeguards, a Northern policy or lawful deferment, and no active constitutional
crisis for formal belligerency. A direct attack may bypass the mandate
threshold only during the final invasion-response/war-entry state; it does not
bypass the named Dáil assent.

## Runtime enforcement

`common/scripted_triggers/slopx_ireland_dillon_gate_repair.txt` defines
`slopx_ireland_dillon_named_vote_gate_strict`. It composes the existing
political platform, caucus, majority, consent, leverage, and constitutional
safeguards with an explicit `Intervention Mandate >= 90` check.

Both named-vote entry points use the strict helper:

- `common/decisions/slopx_ireland_decisions.txt` opens the named-vote event only
  through the strict helper.
- `events/slopx_ireland_events.txt` requires the strict helper before presenting
  the named vote.
- `slopx_ireland_events.1840` remains the sole writer of
  `slopx_ireland_dillon_vote_passed` on the carried vote option.
- `slopx_ireland_can_dillon` retains the direct-attack `invasion_danger` branch
  only at the final material war-entry gate, after the named vote flag exists.

This keeps invasion danger from synthesising parliamentary assent while still
allowing the canonical emergency exception at final war entry.

## Static checks

- Named-vote callers: 2; both use `slopx_ireland_dillon_named_vote_gate_strict`.
- Strict helper mandate check: one explicit `greater_than_or_equals` comparison
  against `constant:slopx_ireland.dillon_intervention_mandate`.
- Direct writes of `slopx_ireland_dillon_vote_passed`: one carried option in
  event `.1840`.
- Live HOI4 launch, save testing, and in-game validation: intentionally not run.
