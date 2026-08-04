# Ireland localisation audit and handoff — 2026-07-29

Status: static localisation audit complete. Two narrow player-facing corrections were applied. Gameplay, specifications, assets, manifests, and unrelated worktree changes were not edited. Live HOI4 testing was intentionally skipped at the user's request.

## Scope and canonical references

Reviewed the Ireland localisation file, Ireland game-rule localisation, linked focus/decision/event/idea/law/achievement/scripted-localisation/GUI sources, and the canonical Ireland requirements in:

- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_6_ai_assets_achievements_and_text.md`
- `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_3_radical_and_hidden_routes.md`
- `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_achievement_matrix.md`
- `prompts/ireland_focus_tree_decision_mission_system_prompt.md`
- `prompts/ireland_focus_tree_achievement_system_prompt.md`
- `prompts/ireland_focus_tree_text_audio_research_prompt.md`
- Earlier Ireland audits and re-audits under `docs/plans/ireland_focus_tree/audits/`.

The required offline wiki pages and installed vanilla documentation for localisation, dynamic values, scripted localisation, events, focuses, decisions, ideas, achievements, GUI, scopes, triggers, effects, and modifiers were also consulted.

## Coverage result

- Focuses: 216 source IDs; all 432 title/description keys present.
- Categories: 13; all 26 name/description keys present.
- Actions: 140; all 280 name/description keys present, with all current source custom-cost, custom-trigger-tooltip, and custom-effect-tooltip localisation references resolving.
- Missions: 54; all 108 name/description keys present. All 54 deadlines match `days_mission_timeout`; every description states an objective, deadline, full success, partial success, and failure outcome.
- Ideas: 63 source blocks; all 126 name/description keys present.
- Laws: 17 live law matrix families; all current law-review scripted-localisation outputs resolve. The current contract exposes four review states (`abuse`, `due`, `active`, `open`) and has no missing family/stage key requested by source.
- Achievements: 32; all 64 name/description keys present. Public conclusion event titles, descriptions, and options are covered.
- Events: 494 raw `country_event` blocks, consisting of 493 top-level player-facing definitions plus one nested dispatch block (`ireland_events.219`). The 493 top-level IDs are unique and all 1,978 title/description/option localisation references resolve. Main event source has 512 options; flavour source has 473 options.
- GUIs: exactly three Ireland windows. Their 135 static localisation references resolve; all seven scripted-localisation calls resolve to the eight defined-text contracts. Existing offline GUI audits report the conditions, Northern settlement, and concealed-evidence surfaces as covered; no live render was run here.
- Game rules: the one Ireland hidden-content rule has all six expected localisation keys semantically present.

## Required audit lists

### Missing keys

None found in the requested focus, category, action, mission, idea, law-review, achievement, event, conclusion, GUI, or game-rule source contracts.

### Duplicate keys

None found in `localisation/english/ireland_l_english.yml` or the Ireland game-rule localisation. Ireland source IDs for focuses, decisions/missions, ideas, achievements, and top-level events were also unique.

### Scripted-localisation issues

None found. `common/scripted_localisation/ireland_localisation.txt` and `common/scripted_localisation/ireland_coastwatch.txt` contain eight defined-text contracts with 84 output branches (57 unique output keys); all outputs exist and all seven GUI calls resolve. The current Northern failure-state branches and plebiscite model branch are distinct, and concealed-evidence values remain generic before reveal.

### Dynamic-text opportunities

- Existing action cost text covers 140 actions through 51 cost localisation keys and exposes current ledgers, values, Political Power, Command Power, and burden bands. The member-contribution requirement was brought into that same readable contract by the patch below.
- Numeric dynamic values use formatted `|0` tokens and current GUI/event ledgers expose current values, timers, selections, regions, and outcomes.
- The 60 route-variant spirit descriptions under `ireland_spirit_governing_*`, `*_society_*`, and `*_security_*` use a shared sentence scaffold. Making each route spirit more individually voiced is a broad text/design pass, not a narrow correction, so it remains queued.
- Law localisation currently exposes review status rather than every family/stage. A future source-level request for family-specific law display should add a dynamic contract then; no missing key was invented here.

### Cross-surface mismatch notes and blockers

- Radical wording and mission ownership are settled by the approved M2 ruling: the current source has ten Radical and Underground actions plus the two physically nested ordinal 006/009 mission families, while the by-election and parish-audit modes remain distinct modes of their base missions. No route wording was silently substituted.
- Achievement staging is settled by the approved A2 ruling. A-22, A-27, A-28, and A-29 through A-32 remain source-hidden (seven hidden achievements total); A-22, A-27, and A-28 retain their canonical reveal-related `happened` flags. The local schema provides no supported dynamic visibility contract, so the implementation claims the documented static-hidden form and does not invent a trigger-valued field.
- Follow-up complete: twelve player-facing strings that exposed raw state numbers (`113`, `119`, and `134/135`) now name Ireland, Northern Ireland, Connaught, and Munster as appropriate. The engine-facing state checks are unchanged.
- Follow-up complete: the six keys in `localisation/english/ireland_game_rules_l_english.yml` no longer have a leading space.
- No generic filler or update-history wording was found in the reviewed player-facing text. Focus, action, mission, and event prose remained route-distinct in the static comparison; the spirit scaffold noted above is the only broad sameness concern.
- Concealed GUI and Northern model text does not statically reveal hidden route names before reveal. Runtime reveal timing remains unverified because live HOI4 testing was excluded.

## Exact changes applied

Changed file: `localisation/english/ireland_l_english.yml`

- `ireland_action_prepare_a_wartime_unity_bargain_requirements_tt` (line 1082): added the missing `Category: Northern Settlement.` label.
- `ireland_action_integrate_a_voluntary_member_contribution_requirements_tt` (line 1104): added the standard named-ledger surcharge explanation, including current-value display and the existing +10/+5/+0 Political Power and Command Power bands with matching burden values.

Before these edits, the first action omitted its category and the second described a surcharge without telling the player how the selected action's current ledger and bands are displayed. After the edits, both requirements follow the established action tooltip contract; gameplay values and effects are unchanged.

## Encoding and validation

- The main Ireland localisation remains UTF-8 with BOM (`EF BB BF`), strict UTF-8 decodable, with 3,574 parsed keys, no duplicates, no malformed leading-key lines, and no `:0` keys.
- The game-rule localisation is also UTF-8 with BOM and strict UTF-8 decodable; its six semantically present keys are the indentation concern listed above.
- Static source/reference scans were rerun for the changed action keys and the complete requested surface counts. No live HOI4 test, runtime GUI test, or engine log check was performed.

## Handoff

The narrow patch and state-name/style follow-up are ready for review. The later M2 and A2 authority rulings close the mission-slot and achievement-visibility decisions; the broad spirit-voice pass remains a separate queued text/design improvement. No gameplay/specification/assets/manifests were changed by this historical localisation audit.
