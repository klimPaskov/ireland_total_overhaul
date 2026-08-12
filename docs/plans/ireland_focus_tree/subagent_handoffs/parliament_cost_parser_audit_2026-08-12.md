# Parliament cost parser audit — 2026-08-12

## Scope and verdict

Read-only audit of the Parliament `ai_hint_pp_cost` parser correction. No
gameplay, GUI, focus, localisation, script-constant, or asset source was
edited. This handoff is the only file written by the audit.

**Verdict: the four replacements are parser-compatible and currently fully
synchronised. Retain the file-local macros.** `ai_hint_pp_cost` requires one
fixed PP amount; it is not a generally supported script-constant field. The
four `@` macros are file-local fixed numeric constants and resolve to the
literal amounts expected by that field. They therefore avoid the malformed
`constant:ireland.parliament_*_pp_cost` tokens without changing any executable
cost, gate, or outcome.

The official script-constant documentation explicitly limits script constants
to fields that document support. The offline Decision modding page separately
states that `ai_hint_pp_cost` must be a constant amount rather than a variable.
The offline Data structures page documents file-local `@` constants as usable
in decision text files. Vanilla uses numeric literals for every inspected
`ai_hint_pp_cost` precedent (for example, `common/decisions/SOV.txt:596`).

## Exact definition and use pairs

All four macros have one definition and one use in
`common/decisions/ireland_decisions.txt`; no other reference exists in that
file. Their static expansion is shown below.

| Action / native decision | Local definition | Hint use | Expanded hint | Shared executable cost |
| --- | --- | --- | ---: | ---: |
| Dáil / `ireland_action_convene_the_dail` | `@IRELAND_PARLIAMENT_DAIL_AI_PP_COST = 15` at line 21 | line 214 | 15 | `ireland.parliament_dail_pp_cost = 15` |
| Seanad / `ireland_action_negotiate_seanad_support` | `@IRELAND_PARLIAMENT_SEANAD_AI_PP_COST = 25` at line 22 | line 246 | 25 | `ireland.parliament_seanad_pp_cost = 25` |
| Confidence / `ireland_action_secure_a_confidence_compact` | `@IRELAND_PARLIAMENT_CONFIDENCE_AI_PP_COST = 25` at line 23 | line 278 | 25 | `ireland.parliament_confidence_pp_cost = 25` |
| Budget / `ireland_action_pass_a_joint_budget` | `@IRELAND_PARLIAMENT_BUDGET_AI_PP_COST = 35` at line 24 | line 310 | 35 | `ireland.parliament_budget_pp_cost = 35` |

The shared costs are defined at
`common/script_constants/ireland_constants.txt:49,52,55,58` respectively.
The bounded static expansion is therefore:

```txt
ai_hint_pp_cost = 15
ai_hint_pp_cost = 25
ai_hint_pp_cost = 25
ai_hint_pp_cost = 35
```

## Issue list, ordered by severity

- **No critical, high, or medium issue found.** The malformed
  `constant:ireland.parliament_*_pp_cost` forms are absent from all
  `ai_hint_pp_cost` fields under `common/`.
- **Low — future tuning coupling only, not a current behavior defect.** The
  parser-required macro literals necessarily mirror their shared script
  constants. The source comment at
  `common/decisions/ireland_decisions.txt:18-24` calls out this pairing. A
  later balance edit must update the matching macro and script constant as one
  change; replacing the macro with `constant:` would reintroduce the parser
  defect.

## Cost, requirement, and controller synchronisation

For each action, the audit verified all of the following exact equalities:

- `AI hint = shared PP cost` (15 / 25 / 25 / 35).
- `availability gate = cost - 1` (14 / 24 / 24 / 34), correctly paired with
  strict `has_political_power >` in
  `common/scripted_triggers/ireland_parliament.txt:45,63,76,91`.
- `executor debit = -cost` through the corresponding
  `ireland.parliament_*_pp_delta` in
  `common/scripted_effects/ireland_parliament.txt:13-42`.
- Native AI decisions and human GUI buttons invoke the same four guarded
  executors. The GUI bindings are at
  `common/scripted_guis/ireland_scripted_guis.txt:40-50`.
- Native custom-cost text and GUI labels display the same four numbers in
  `localisation/english/ireland_l_english.yml:3429-3443`.

Consequently, the fix only changes what the AI cost-hint parser receives. It
does not alter the PP paid, the PP threshold, the human button presentation,
or the record effect reached after payment.

## Decision-category lifecycle notes

- **Owner/category:** original `IRE` /
  `ireland_settlement_government`.
- **Reveal and progression:** the settlement route reveals the programme; only
  the current stage is visible to AI, progressing Dáil → Seanad → confidence
  → budget. The prior Parliament interaction audit identifies
  `ireland_national_settlement` as the focus opening the human programme.
- **Controller split:** the four native rows are `is_ai = yes`; humans use the
  scripted-GUI controls, and both paths converge on the same executor.
- **Terminal cleanup:** every native row has `fire_only_once = yes` and is
  removed when the original tag changes or `ireland_route_archived` is set.
  Retained completion flags are intentional historical state, not stale
  actions.

## Mission quality notes

No Parliament-owned mission is present or changed. These are immediate,
one-time institutional decisions: owner `IRE`, category
`ireland_settlement_government`, regional requirement Dublin (state 113), no
duration, success through its matching `ireland_record_parliament_*` helper,
no failure or partial-success branch, and no duplicate-mission risk. The
parser correction does not justify adding a timer, mission, or failure roll.

## AI validity and route-lock notes

The native AI path retains original-IRE, settlement-reveal, stage, completion,
and route-archive locks. The four actions have no country target, border,
dead-tag, escalation-variant, or external-route dependency. Their base
weights remain 10 / 9 / 8 / 7, but stage visibility makes only the next valid
action eligible. The corrected hints now accurately tell AI to retain the PP
that the shared executor actually debits.

## Localisation, tooltip, cleanup, and exploit notes

No localisation or tooltip gap was introduced. The four custom-cost keys and
human GUI cost labels match the shared executable values. The change does not
add a free-click, duplicate-charge, equipment, unit, claim, core, or war-goal
loop: guarded executors, completion flags, stage gates, and `fire_only_once`
remain the only action paths.

## Validation and limits

Meaningful static validation passed:

- a pairwise source check confirmed exactly one macro definition and one hint
  use per action;
- it confirmed each macro, shared cost, strict PP gate, negative executor
  delta, visible custom-cost label, native executor call, scripted-trigger
  gate, and GUI executor binding agree for all four actions;
- a targeted scan found **zero** remaining malformed
  `ai_hint_pp_cost = constant:ireland.parliament_*_pp_cost` forms; and
- a constrained macro substitution produced only numeric parser inputs
  `15`, `25`, `25`, and `35`.

Skipped meaningful validation: no standalone in-repository HOI4 decision
parser or live-game load was available to independently execute the engine
parser. The conclusion is grounded in the official script-constant constraint,
the offline decision and macro references, vanilla literal precedents, and the
fully numeric expansion above. No GUI render artifact was needed because this
audit changed neither GUI layout nor GUI source.

## Recommended follow-up

No gameplay fix is required. When retuning an opening Parliament PP cost,
change the corresponding pair in
`common/decisions/ireland_decisions.txt:21-24` and
`common/script_constants/ireland_constants.txt:49-58` together, preserving
the gate at `cost - 1` and the debit at `-cost`. Do not use a `constant:`
token in `ai_hint_pp_cost`.
