# High Kingship branch lifecycle tranche - 2026-07-27

Feature slug: `ireland_focus_tree`

Namespace: `ireland`

Status: source-level branch reconciliation; live engine, GUI, AI, source-clearance, and fresh-save scenarios remain not-run.

## Scope

This tranche gives the High Kingship route distinct lawful household, sacral-crown, and captured-crown branch state while preserving the canonical 216-focus inventory. The branch surfaces use the existing High Kingship focuses and the F12 cultural-event chain; no new focus, icon, office, core, territory, or free political victory reward was introduced.

## Branch lifecycle

- Elective and Guardian openings retain their existing constitutional focus gates and feed the crown-powers charter.
- A verified evidence-and-convention path records `ireland_high_king_sacral_path` and `ireland_high_king_sacral_crown_path`; the charter and capstone write separate sacral-crown conclusion records.
- The F12 household appointment outcomes write either an independent-household or provincial-steward branch. The crown-powers charter records a lawful household conclusion only when the household branch is not the captured-crown failure lane.
- The captured-crown event outcome is a real failure path. It applies the canonical consent, exposure, and settlement shocks, opens the foreign-reaction handoff, marks route failure, and clears the lawful household marker. The recovery bridge converts a recovered captured crown into a new household/constitutional attempt and records rescue; it does not grant an automatic conclusion.
- The capstone records the branch-specific conclusion marker after the normal constitutional review and conclusion-proof requirements. Captured-crown history remains ineligible for the clean royal achievements.

## Source surfaces

- Focus gates and branch conclusion writers: `common/national_focus/ireland_focus_tree.txt`
- Evidence, convention, sacral, profile, and recovery synchronization: `common/scripted_effects/ireland_runtime.txt`
- Route qualification and conclusion writer: `common/scripted_triggers/ireland_triggers.txt`, `common/scripted_effects/ireland_effects.txt`
- Captured-crown failure and household outcomes: `events/ireland_flavour_events.txt`
- Achievement-history exclusions: `common/scripted_effects/ireland_achievement_history.txt`
- Player-facing branch text: `localisation/english/ireland_l_english.yml`

## Static evidence

- Focus inventory remains 216; the exact icon/runtime package remains 216 fresh goal sprites under `gfx/interface/goals/ireland/`.
- The touched script files have balanced braces and no unsupported `<=` or `>=` operators.
- Captured-crown state is referenced by the failure, recovery, charter, capstone, AI, and achievement-history surfaces; it is not a claim, core, occupation, or recognition writer.

## Remaining proof and blockers

- Live parser/load, focus rendering, hidden-content concealment, event timing, AI route choice, achievement unlock, and cleanup scenarios remain unrun because HOI4 was not launched.
- The source manifest still contains uncleared historical records and user-review items; generated focus art does not clear those records.
- The canonical Radical/Underground two-slot mission wording still conflicts with the exact 54-family inventory and remains explicitly unresolved.
