# Concealed Transition Authority Tranche — 2026-07-26

Feature slug: `ireland_focus_tree`

Status: source-wired, live engine and scenario validation not-run.

## Scope

This tranche closes the concealed A-route authorization gap identified in the completion audit. `Convene a Hidden Evidence Council` is no longer a generic cultural action that can create hidden evidence. It now admits only after the authored restoration review is complete, independent evidence is ready, hidden-content permission and the enabled game rule are present, and no restoration failure or route-closure state survives.

The council completion writes `ireland_concealed_evidence_revealed` as a durable presentation/reveal state and retains `ireland_action_convene_a_hidden_evidence_council_complete` as the gameplay authorization. The scripted-GUI inspect button only requests a row review and cannot set the reveal flag. The council does not add to `ireland_hidden_evidence`.

## Runtime gates

- `ireland_concealed_transition_authority` centralizes the restoration, independent-review, permission, game-rule, failure-class, archive, and closure requirements.
- High Kingship, Five Provinces impossibility, Otherworld dominion/impossible confirmation, and `ireland_verified_impossible_reveal` additionally require the completed Hidden Evidence Council.
- The constitutional High Kingship and federal Five Provinces plausible-route gates remain independent P-route gates; this tranche does not force them behind concealed evidence.
- The existing Otherworld investigation, evidence, and compact gates remain separate from the concealed A-route handoff.

## Files

- `common/scripted_triggers/ireland_triggers.txt`
- `common/decisions/ireland_decisions.txt`
- `common/scripted_effects/ireland_runtime.txt`
- `localisation/english/ireland_l_english.yml`
- `docs/ireland_dynamic_effects.md`

## Static validation target

The source audit must show that partial, cancelled, false-lead, fraud, panic, route-closure, and archived restoration states cannot open the council or any concealed A-route flag; full restoration plus permission can open the council once; historical AI cannot select the council or concealed A-route content; and the council/reveal flags have gameplay consumers rather than GUI-only use. Live focus, event, AI, GUI, map-objective, and deadline scenarios remain open because HOI4 was not launched.

No asset changes are required. The current regenerated goal-icon package remains the accepted runtime art under `gfx/interface/goals/ireland/`.
